from datetime import date
from pathlib import Path
import random

today = date.today().strftime("%Y-%m-%d")

# 今日のアウトドアワンポイント
tips = [
    "沖縄では突然のスコールに備えてレインウェアを携帯しましょう。",
    "夏場のキャンプでは熱中症対策として十分な水分補給が重要です。",
    "海辺のキャンプでは潮位情報を事前に確認しましょう。",
    "虫よけスプレーを持参すると快適に過ごせます。",
    "強風の日はテント設営場所を慎重に選びましょう。",
    "日差しが強い日はタープを活用すると快適に過ごせます。",
    "キャンプ前には天気予報を確認して安全を確保しましょう。"
]

tip = random.choice(tips)

# 沖縄おすすめスポット
spots = [
    {
        "name": "県民の森キャンプ場",
        "description": "自然豊かな環境で初心者にも人気のキャンプ場です。"
    },
    {
        "name": "ネイチャーみらい館",
        "description": "カヌー体験や自然観察が楽しめる人気スポットです。"
    },
    {
        "name": "屋我地ビーチ",
        "description": "海を眺めながらアウトドアを楽しめる絶景スポットです。"
    },
    {
        "name": "比地大滝",
        "description": "沖縄本島最大級の滝が見られるトレッキングコースです。"
    },
    {
        "name": "東村ふれあいヒルギ公園",
        "description": "マングローブ観察や自然体験が楽しめます。"
    }
]

spot = random.choice(spots)

# 注目イベント
events = [
    {
        "title": "県民の森キャンプ体験会",
        "location": "恩納村",
        "description": "初心者向けのキャンプ体験イベントです。"
    },
    {
        "title": "比地大滝トレッキング",
        "location": "国頭村",
        "description": "沖縄の自然を満喫できる人気トレッキングイベントです。"
    },
    {
        "title": "屋我地島サンセットウォーク",
        "location": "名護市",
        "description": "夕日を眺めながら散策できる人気イベントです。"
    },
    {
        "title": "東村マングローブ観察会",
        "location": "東村",
        "description": "マングローブの自然を学べる体験型イベントです。"
    }
]

event = random.choice(events)

html = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>沖縄アウトドアイベント情報 {today} | Okinawa Outdoor Base</title>

<style>
body {{
    font-family:-apple-system,BlinkMacSystemFont,sans-serif;
    max-width:1000px;
    margin:auto;
    padding:20px;
    line-height:1.8;
    background:#f5f7f9;
}}

header {{
    background:#006d77;
    color:white;
    padding:30px;
    border-radius:10px;
}}

section {{
    background:white;
    margin-top:20px;
    padding:25px;
    border-radius:10px;
    box-shadow:0 2px 8px rgba(0,0,0,.08);
}}

a {{
    color:#006d77;
    text-decoration:none;
}}

a:hover {{
    text-decoration:underline;
}}

footer {{
    margin-top:30px;
    text-align:center;
}}
</style>
</head>

<body>

<header>
<h1>🏕 沖縄アウトドアイベント情報 {today}</h1>
<p>Okinawa Outdoor Base 自動更新記事</p>
</header>

<section>
<h2>🎪 本日の注目イベント</h2>

<h3>{event["title"]}</h3>

<p><strong>開催エリア：</strong>{event["location"]}</p>

<p>{event["description"]}</p>
</section>

<section>
<h2>📍 今日のおすすめスポット</h2>

<h3>{spot["name"]}</h3>

<p>{spot["description"]}</p>
</section>

<section>
<h2>🏕 今週の沖縄アウトドア情報</h2>

<ul>
<li>キャンプイベント情報をチェック</li>
<li>週末のお出かけスポットを確認</li>
<li>人気キャンプ場の最新状況を確認</li>
<li>沖縄各地のアウトドアニュースを紹介</li>
</ul>
</section>

<section>
<h2>📚 おすすめ記事</h2>

<ul>
<li><a href="../camp-okinawa-top10.html">沖縄おすすめキャンプ場10選</a></li>
<li><a href="../okinawa-free-campgrounds.html">沖縄の無料キャンプ場まとめ</a></li>
<li><a href="../solo-camp-guide.html">ソロキャンプ初心者ガイド</a></li>
<li><a href="../camera-beginner-guide.html">初心者向けカメラの選び方</a></li>
<li><a href="../okinawa-photo-spots-top10.html">沖縄の絶景撮影スポット10選</a></li>
</ul>
</section>

<section>
<h2>💡 今日のアウトドアワンポイント</h2>

<p>{tip}</p>
</section>

<footer>
<p>© Okinawa Outdoor Base</p>
<p><a href="../index.html">トップページへ戻る</a></p>
</footer>

</body>
</html>
"""

Path("daily").mkdir(exist_ok=True)

filename = f"daily/{today}.html"

with open(filename, "w", encoding="utf-8") as f:
    f.write(html)

print("created:", filename)
