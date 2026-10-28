from pathlib import Path
from html import escape
from html.parser import HTMLParser
import re

BASE = Path(__file__).resolve().parent.parent

class Headings(HTMLParser):
    def __init__(self):
        super().__init__()
        self.level = None
        self.text = []
        self.headings = []
    def handle_starttag(self, tag, attrs):
        if tag in ('h1', 'h3'):
            self.level, self.text = tag, []
    def handle_data(self, data):
        if self.level:
            self.text.append(data)
    def handle_endtag(self, tag):
        if tag == self.level:
            self.headings.append((tag, ''.join(self.text).strip()))
            self.level = None

def subject(file):
    parser = Headings()
    parser.feed(file.read_text(encoding='utf-8'))
    # Facility and spot headings describe the article without claiming an event today.
    topics = [text for tag, text in parser.headings if tag == 'h3']
    if topics:
        return '・'.join(dict.fromkeys(topics[:2])) + '｜沖縄アウトドア案内'
    return '沖縄のお出かけ・自然体験ガイド'

def card(file, prefix):
    return f'<div class="card"><a href="{prefix}{file.name}">{escape(subject(file))}</a></div>'

files = sorted((p for p in (BASE / 'daily').glob('*.html')
                if re.fullmatch(r'\d{4}-\d{2}-\d{2}', p.stem)), reverse=True)
index = BASE / 'index.html'
content = index.read_text(encoding='utf-8')
start, end = '<!-- DAILY_ARTICLES_START -->', '<!-- DAILY_ARTICLES_END -->'
if content.count(start) != 1 or content.count(end) != 1 or content.index(start) >= content.index(end):
    raise ValueError('Daily article markers are missing or invalid')
before, rest = content.split(start, 1)
_, after = rest.split(end, 1)
cards = '\n'.join(card(p, 'daily/') for p in files[:10])
archive_link = '<p><a href="daily/index.html">過去記事一覧を見る →</a></p>'
index.write_text(before + start + '\n' + cards + '\n' + archive_link + '\n' + end + after, encoding='utf-8')
older = '\n'.join(card(p, '') for p in files[10:]) or '<p>過去の記事はまだありません。</p>'
archive = f'''<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>過去記事一覧 | Okinawa Outdoor Base</title>
<link rel="stylesheet" href="../css/style.css"></head><body>
<header><h1>過去記事一覧</h1><p>最新10件より前のアウトドア記事</p></header>
<nav aria-label="ページナビゲーション"><a href="../index.html#daily-articles">最新の記事へ戻る</a></nav>
<main class="container"><section class="section"><h2>これまでの記事</h2>{older}</section></main>
<footer>© 2026 Okinawa Outdoor Base</footer></body></html>'''
(BASE / 'daily' / 'index.html').write_text(archive, encoding='utf-8')
print(f'Top: {min(10, len(files))}, archive: {len(files[10:])}')
