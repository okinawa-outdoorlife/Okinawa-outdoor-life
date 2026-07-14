from pathlib import Path

index_file = Path("index.html")
daily_dir = Path("daily")

files = sorted(daily_dir.glob("*.html"), reverse=True)

cards = []

for file in files[:30]:
    date = file.stem

    cards.append(f'''
    <div class="card">
      <a href="daily/{date}.html">
        📰 沖縄アウトドアイベント情報 {date}
      </a>
    </div>
''')

content = index_file.read_text(encoding="utf-8")

start = "<!-- DAILY_ARTICLES_START -->"
end = "<!-- DAILY_ARTICLES_END -->"

before = content.split(start)[0]
after = content.split(end)[1]

new_content = (
    before
    + start
    + "\n"
    + "\n".join(cards)
    + "\n"
    + end
    + after
)

index_file.write_text(new_content, encoding="utf-8")

print("index updated")