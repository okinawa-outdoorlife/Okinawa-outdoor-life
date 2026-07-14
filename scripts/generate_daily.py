from datetime import date
from pathlib import Path

today = date.today().strftime("%Y-%m-%d")

html = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>沖縄アウトドアイベント情報 {today}</title>
</head>
<body>

<h1>沖縄アウトドアイベント情報 {today}</h1>

<p>
本日の沖縄アウトドア情報です。
</p>

<ul>
<li>キャンプ関連ニュース更新予定</li>
<li>沖縄イベント情報更新予定</li>
<li>アウトドアスポット紹介予定</li>
</ul>

<p>
Okinawa Outdoor Base 自動生成記事
</p>

</body>
</html>
"""

Path("daily").mkdir(exist_ok=True)

filename = f"daily/{today}.html"

with open(filename, "w", encoding="utf-8") as f:
    f.write(html)

print("created:", filename)