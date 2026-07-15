from datetime import datetime
from pathlib import Path

# 今日の日付
today = datetime.now().strftime("%Y-%m-%d")

# フォルダ
daily_dir = Path("daily")
daily_dir.mkdir(exist_ok=True)

# 記事ファイル
article_file = daily_dir / f"{today}.html"

# すでに存在する場合は終了
if article_file.exists():
    print("記事はすでに存在します")
    exit()

# 記事テンプレート
html = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>沖縄アウトドアイベント情報 {today}</title>

<style>
body {{
    font-family: sans-serif;
    line-height: 1.8;
    padding:20px;
}}

h1 {{
    color:#0066cc;
}}

.box {{
    background:#f5f5f5;
    padding:15px;
    border-radius:10px;
}}
</style>

</head>

<body>

<h1>🏝 沖縄アウトドアイベント情報 {today}</h1>

<div class="box">

<h2>🏕 本日のおすすめイベント</h2>

<p>
現在、沖縄で開催予定のアウトドアイベント情報を紹介します。
</p>

<ul>
<li>キャンプイベント情報</li>
<li>自然体験イベント情報</li>
<li>海・ビーチ関連イベント情報</li>
</ul>

</div>


<h2>🌊 沖縄の自然を楽しむポイント</h2>

<p>
沖縄は一年を通してアウトドアを楽しめる場所です。
キャンプ、海遊び、自然体験など、
家族でも楽しめるスポットが数多くあります。
</p>


<h2>関連記事</h2>

<ul>
<li><a href="../index.html">沖縄アウトドア情報トップ</a></li>
</ul>


<footer>
<p>© 2026 沖縄アウトドア情報</p>
</footer>

</body>
</html>
"""


# 保存
article_file.write_text(html, encoding="utf-8")

print(f"作成しました: {article_file}")