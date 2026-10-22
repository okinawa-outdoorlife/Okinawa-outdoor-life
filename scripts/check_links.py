"""Validate local links and assets in published HTML without network access."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "name" in attrs:
            self.ids.add(attrs["name"])
        for attribute in ("href", "src"):
            if attribute in attrs:
                self.links.append((self.getpos()[0], attrs[attribute]))


def check(root=ROOT):
    pages = {p.resolve(): Page(p.read_text(encoding="utf-8"))
             for p in root.rglob("*.html")
             if not p.name.startswith("index_backup_")}
    errors = []
    for source, page in pages.items():
        for line, value in page.links:
            label = f"{source.relative_to(root)}:{line}: {value!r}"
            if not value.strip() or value.strip() == "#":
                errors.append(f"{label}: empty destination")
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            # Pages is hosted under a repository subpath; use relative URLs.
            if path.startswith("/"):
                errors.append(f"{label}: use a relative path for GitHub Pages")
                continue
            target = (source.parent / path).resolve() if path else source
            if not target.is_relative_to(root):
                errors.append(f"{label}: outside site root")
                continue
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                errors.append(f"{label}: destination does not exist")
                continue
            if url.fragment and target.suffix == ".html":
                destination = pages.get(target)
                if destination is None:
                    destination = Page(target.read_text(encoding="utf-8"))
                if unquote(url.fragment) not in destination.ids:
                    errors.append(f"{label}: fragment does not exist")
    return len(pages), errors


if __name__ == "__main__":
    count, errors = check()
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {count} HTML pages; {len(errors)} errors")
    sys.exit(bool(errors))
