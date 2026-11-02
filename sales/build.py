# 営業担当がそのまま渡せる「Instagram広告 運用代行のご案内」PDF（2026-11-02 三上様「料金もすべて入れて」）
# 一次資料：紹介ページ（../index.html）・特商法の表記（../legal.html）・確定料金（2026-09-30 三上様）・手順書（ig-ads.s-toru.com/start/）
# 料金は 2026-09-30 確定値（広告費の20%＋税・最低11,000円・最低3か月）。広告費の具体額は書かない（CLAUDE.md）
# 使い方: python3 build.py → Instagram広告運用代行_ご案内.html / .pdf
import base64, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
def img(name):
    ext = name.rsplit('.', 1)[1].replace('jpg', 'jpeg')
    return f"data:image/{ext};base64," + base64.b64encode(open(os.path.join(HERE, name), 'rb').read()).decode()
FORM = "https://docs.google.com/forms/d/e/1FAIpQLScQxGrWcsL7z5hQ7KLK3hqWy9I5c64KNhe9HicYCiDJB3c03Q/viewform"
FOOT = "Instagram広告 運用代行のご案内 ｜ 株式会社しっとる"

pages = []
def page(eb, title, body, dark=False):
    n = len(pages) + 1
    cls = "pg dark" if dark else "pg"
    head = f'<p class="eb">{eb}</p><h2>{title}</h2>' if title else ""
    pages.append(f'<section class="{cls}">{head}{body}<p class="foot">{FOOT}<span>{n:02d}</span></p></section>')

def note(t): return f'<p class="note">{t}</p>'
def gl(*items): return '<div class="gl">' + "".join(f'<p><b>{a}</b>：{b}</p>' for a, b in items) + '</div>'

# 1 表紙
pages.append(f'''<section class="pg cover"><div class="cv">
<p class="eb">株式会社しっとる　SNS集客のパートナー</p>
<h1>Instagram広告<br>運用代行のご案内</h1>
<p class="lead">スマホで撮った素材から、リール動画づくり・お店のInstagramへの投稿・広告の配信・毎月のレポートまで、まとめてお任せいただけます。</p>
<div class="chips"><span>リール動画制作込み</span><span>投稿も代行</span><span>来店できる範囲に絞って配信</span><span>毎月のレポート</span></div>
</div><img class="cvimg" src="{img('reel.png')}" alt="制作例のリール動画"><p class="cvcap">制作例（導入店舗の整体院のリール広告）</p></section>''')

# 2 お悩み
page("お困りごと", "こんなお悩みはありませんか", '''<div class="pains">
<div>ポータルサイトの掲載料は高いのに、効果が見合わない</div>
<div>SNSが大事なのは分かっているが、時間もノウハウもない</div>
<div>広告を出してみたが、予約や来店につながらなかった</div>
<div>リール動画が大事らしいが、作り方が分からない</div></div>
<p class="big">ひとつでも当てはまったら、このサービスがお役に立てます。</p>''' + gl(("Instagram広告", "お金を払って、見てほしい人のInstagramにお店の投稿を出すことです"), ("リール", "Instagramの縦型の短い動画です。いま最も見られている形です")))

# 3 原因と解決
page("なぜ予約につながらないのか", "成果が出ない原因は、ほとんどがこの2つです", '''<div class="two">
<div class="card stop"><p class="tag">原因 1</p><h3>見せる相手が広すぎる</h3><p>お店のお客様の多くは近くにお住まいの方です。設定を誤ると、来店できない遠くの人にまで広告費が使われます。</p><p class="arrow">→ お店から半径5km圏内・1歳単位の年齢・性別・興味関心で、来てほしい人だけに届けます</p></div>
<div class="card stop"><p class="tag">原因 2</p><h3>写真1枚では指が止まらない</h3><p>いまのInstagramで最も見られているのはリールです。写真1枚の広告は素通りされやすく、押される単価も高くなりがちです。</p><p class="arrow">→ スマホで撮った素材から、指が止まるリール動画をしっとるが企画・編集します</p></div></div>''')

# 4 できること
page("できること", "しっとるが行うこと、お店にお願いすること", '''<div class="three">
<div class="card ok"><h3>しっとるが行うこと</h3><ul>
<li>リール動画の企画・編集（スマホの素材から・撮り方もお伝え）</li><li>広告文・見出しの作成</li><li><b>お店のInstagramへの投稿</b>（内容はLINEで確認してから）</li><li>広告マネージャーでの広告の作成と配信</li><li>配信先の絞り込み（半径5km・年齢・性別・興味関心）</li><li>成績の確認、広告の見直し・入れ替え・停止</li><li>毎月のレポート</li></ul></div>
<div class="card warn"><h3>お店にお願いすること</h3><ul>
<li>Facebookページ・Instagram・広告アカウントの「使ってよい」という許可を、しっとるに渡す（手順はURLでご案内）</li><li>広告費のカードをMetaに登録する（カード番号はご自身で）</li><li>スマホで撮った素材を送る</li><li>できた広告・投稿と、毎月の結果を確認する</li></ul></div>
<div class="card soft"><h3>安心していただけること</h3><ul>
<li>パスワードやカード番号を、しっとるがお聞きすることはありません</li><li>広告費はお店からMeta社へ直接。しっとるがお預かりすることはありません</li><li>予算を上げるのは、文字でご了解をいただいたときだけ</li><li>お店のアカウントは、お店のもののまま</li></ul></div></div>''' + gl(("広告マネージャー", "Meta社（Instagram・Facebookの会社）の、広告を作って出すための画面です"), ("広告費", "広告を出すためにMeta社へ払うお金です。しっとるへの料金とは別です")))

# 5 実物
page("お届けするもの", "実際にお届けするもの", f'''<div class="shots3">
<figure><img src="{img('reel.png')}" class="tall"><figcaption><b>リール動画</b><br>スマホの素材から企画・編集します。<span class="lbl">制作例</span></figcaption></figure>
<figure><img src="{img('target.png')}"><figcaption><b>配信の設定</b><br>お店から半径5km圏内など、来てほしい人に絞ります。<span class="lbl">見本</span></figcaption></figure>
<figure><img src="{img('report.png')}"><figcaption><b>毎月のレポート</b><br>表示・クリック・予約や問い合わせを、前の月と比べてお伝えします。<span class="lbl">見本</span></figcaption></figure></div>''' + note("制作例は導入店舗（整体院）の実際の広告動画です。配信の設定とレポートは見本で、店名・数値は例です。"))

# 6 比べ
page("ほかの頼み方との比べ", "どんな頼み方が合うか", '''<div class="tw"><table>
<tr><th></th><th>ご自身で広告を出す</th><th>一般的な広告代理店</th><th class="hl">しっとる</th></tr>
<tr><td>リール動画づくり</td><td>ご自身で撮影・編集</td><td>別料金のことが多い</td><td class="hl">運用代行費に込み（スマホの素材でOK）</td></tr>
<tr><td>Instagramへの投稿</td><td>ご自身で</td><td>広告のみのことが多い</td><td class="hl">しっとるが代わりに投稿</td></tr>
<tr><td>配信の絞り込み</td><td>設定を覚える必要あり</td><td>代理店が設定</td><td class="hl">半径5km・年齢・性別・興味関心で設定</td></tr>
<tr><td>結果の見え方</td><td>管理画面を自分で読む</td><td>月1回の報告が多い</td><td class="hl">毎月のレポート＋気になることはLINEで</td></tr>
<tr><td>お店の手間</td><td>大きい</td><td>打ち合わせが中心</td><td class="hl">許可を渡す・素材を送る・確認するだけ</td></tr>
<tr><td>向いている方</td><td>時間があり、広告を学びたい方</td><td>大きな予算で、幅広く出したい方</td><td class="hl">近くのお客様を増やしたい店舗の方</td></tr>
</table></div>''' + note("ほかの頼み方は一般的な傾向で、会社によって異なります。"))

# 7 選ばれる理由
page("選ばれる理由", "しっとるが選ばれる理由", '''<div class="reasons">
<div><b>1</b><h3>「安かろう悪かろう」ではありません</h3><p>多くの店舗様にご利用いただく仕組みで1件あたりのコストを下げています。クリック単価100円以下を基準に、費用対効果にこだわって運用します。</p></div>
<div><b>2</b><h3>代表自身が実店舗の経営者です</h3><p>代表が店舗を経営し、集客を実践してきました。実際に予約につながった導線の作り方を、そのまま貴店に生かします。</p></div>
<div><b>3</b><h3>丸投げでも、任せきりにしません</h3><p>動画づくりから投稿・広告・レポートまで代行しつつ、進み具合はLINEで共有し、ご質問にも気軽にお答えします。</p></div>
<div><b>4</b><h3>素材はスマホでOK</h3><p>撮り方と撮るもの6本をお伝えします。特別な機材はいりません。</p></div>
<div><b>5</b><h3>準備はURLの手順どおりに進めるだけ</h3><p>Facebookも広告も何もない状態から、実際の画面で順に案内します。スマホでもパソコンでも進められます。</p></div>
<div><b>6</b><h3>パスワードは不要</h3><p>お店のアカウントはお店のもののまま、「使ってよい」という許可だけを渡していただきます。</p></div></div>''' + gl(("クリック単価", "広告が1回押されるごとに、かかった広告費です")))

# 8 料金
page("料金", "料金（すべて税込）", '''<div class="price">
<div class="ph"><p class="pl">運用代行費（毎月）</p><p class="pv">広告費の<b>20%</b>＋税</p><p class="pmin">最低料金 <b>月額11,000円</b>（税込）</p><p class="ps">広告費の20%＋税が11,000円に満たない月は、最低料金の11,000円になります。</p><p class="pinc">リール動画の制作・Instagramへの投稿・広告の配信と見直し・毎月のレポートが、すべて含まれます。</p></div>
<div class="pr"><h3>料金とは別にかかるもの</h3><ul><li><b>広告費</b>：お店のカードからMeta社へ直接お支払いいただきます。金額はお店でお決めいただきます（しっとるからお勧めはしません）</li><li><b>銀行振込手数料</b></li></ul>
<h3>契約のきまり</h3><ul><li><b>最低契約期間は3か月</b>です。最初の3か月で、配信しながら見直しを重ねます</li><li>4か月目以降の解約は、<b>翌月の運用開始前（前月末日）まで</b>にご連絡ください</li><li>お支払いは<b>銀行振込（月額前払い）</b>です</li><li>提供開始後の当月分の運用代行費と、Meta社へ支払済みの広告費は返金できません</li></ul></div></div>''')

# 9 流れ
page("ご利用の流れ", "ご相談から、毎月の見直しまで", '''<div class="flow">
<div><span>1</span><b>無料相談</b><small>フォームに約1分で入力。商圏・業種に合わせて無料でプランをご提案</small></div>
<div><span>2</span><b>お申し込み</b><small>LINEのお申し込みフォームに回答し、メールで届く契約書に署名</small></div>
<div><span>3</span><b>広告の準備</b><small>URLの手順どおりに、しっとるに許可を渡し、カードを登録</small></div>
<div><span>4</span><b>素材と決めること</b><small>月の予算・1件にいくらまで・案内先・使わない言葉を決め、動画を送る</small></div>
<div><span>5</span><b>制作・投稿・配信</b><small>リール動画と広告をLINEで確認 → 投稿と配信はしっとるが</small></div>
<div><span>6</span><b>毎月の見直し</b><small>レポートで数字を見て、反応が落ちた広告を入れ替え</small></div></div>''' + note("広告の成果は業種・商圏・ご予算などで異なり、特定の成果をお約束するものではありません。"))

# 10 準備
page("広告の準備", "準備は、URLの手順どおりに進めるだけ", f'''<div class="prep">
<figure><img src="{img('guide_where.png')}" class="phone"><figcaption>今の状態に合わせて、始める場所を選べます</figcaption></figure>
<figure><img src="{img('perm.jpg')}" class="pc"><figcaption>最後に、しっとるに3つの許可を渡します（実際のMetaの画面）</figcaption></figure>
<div class="pq"><table><tr><th>渡すもの</th><th>オンにするもの</th></tr><tr><td>広告アカウント</td><td>フルアクセス</td></tr><tr><td>Facebookページ</td><td>広告・コンテンツ・インサイト</td></tr><tr><td>Instagram</td><td>広告・コンテンツ・インサイト</td></tr></table>
<p class="small">手順のページ（スマホでもパソコンでも見られます）</p><img src="{img('qr_guide.png')}" class="qr"><p class="url">ig-ads.s-toru.com/start/</p></div></div>''' + gl(("Facebookページ", "お店の名前で作るFacebookのページです。広告の名義に使います。投稿しなくて大丈夫です")))

# 11 FAQ
page("よくあるご質問", "お客様からよく伺うこと", '''<div class="faq">
<div><h3>SNSや広告の知識が全くなくても大丈夫ですか？</h3><p>大丈夫です。動画づくり、投稿、広告の設定、毎月のレポートまで、しっとるが行います。お店にお願いするのは、許可を渡すこと、素材のご提供、結果のご確認だけです。</p></div>
<div><h3>動画の素材は自分で用意する必要がありますか？</h3><p>スマホで撮った店内や施術・メニューの動画で十分です。撮り方と撮るもの6本をお伝えします。</p></div>
<div><h3>Instagramの投稿もお願いできますか？</h3><p>できます。作った内容をLINEでご確認いただき、OKをいただいてから、しっとるがお店のInstagramに投稿します。</p></div>
<div><h3>パスワードを教える必要はありますか？</h3><p>ありません。Facebook・Instagram・カードのどれも、しっとるにお伝えいただくことはありません。</p></div>
<div><h3>どのくらいで効果が出ますか？</h3><p>広告は配信を始めた直後から届き始めます。業種やご予算によりますが、毎月のレポートで数字を見ながら改善を重ねます（成果をお約束するものではありません）。</p></div>
<div><h3>広告費はいくら必要ですか？</h3><p>お店のご予算に合わせて、無料相談でご相談しながら決めます。金額はお店でお決めください。</p></div></div>''')

# 12 締め
pages.append(f'''<section class="pg dark end"><div class="ec">
<p class="eb">まずは、無料相談から</p><h1>「うちの業種でも合う？」<br>そのご質問だけでも大歓迎です。</h1>
<p class="lead">フォームにご記入いただければ、お店の商圏と業種に合わせた集客プランを無料でご提案します。オンライン対応で、しつこい営業はいたしません。</p>
<p class="co">株式会社しっとる<br><span>〒700-0901 岡山県岡山市北区本町6-36 第一セントラルビル4階 ／ shittoru.ad@gmail.com</span></p></div>
<div class="eq"><img src="{img('qr_form.png')}"><p>無料相談フォーム<br><span>約1分で入力できます</span></p><img src="{img('qr_lp.png')}"><p>サービス紹介ページ<br><span>ig-ads.s-toru.com</span></p></div></section>''')

CSS = '''
@page{size:A4 landscape;margin:0}
*{box-sizing:border-box}body{margin:0;font-family:"BIZ UDPGothic","Hiragino Sans",sans-serif;color:#1f2622;background:#e9e6df}
.pg{width:297mm;height:210mm;padding:14mm 16mm 12mm;background:#f6f4ef;position:relative;page-break-after:always;overflow:hidden;display:flex;flex-direction:column;gap:5mm}
.eb{margin:0;color:#b4501f;font-weight:700;font-size:11pt;letter-spacing:.08em}
h1{font-family:"BIZ UDPMincho",serif;margin:0;line-height:1.2}h2{font-family:"BIZ UDPMincho",serif;font-size:22pt;margin:0 0 2mm;color:#1c3f3a;line-height:1.25}
h3{margin:0 0 2mm;font-size:13pt;color:#1c3f3a}
p,li{font-size:10.5pt;line-height:1.65}ul{margin:0;padding-left:5mm}
.foot{position:absolute;left:16mm;right:16mm;bottom:6mm;margin:0;font-size:8pt;color:#6b7570;display:flex;justify-content:space-between;border-top:1px solid #dcd8cf;padding-top:2mm}
.note{font-size:8.5pt;color:#5d6762;margin:0}
.gl{margin-top:auto;margin-bottom:6mm;border-left:3px solid #dcd8cf;padding-left:4mm}.gl p{margin:0;font-size:8.5pt;color:#4f5b56;line-height:1.5}
.cover{flex-direction:row;background:#1c3f3a;color:#f6f4ef;align-items:center;gap:10mm}.cover .cv{flex:1;display:flex;flex-direction:column;gap:6mm}
.cover h1{font-size:38pt;color:#fff}.cover .eb{color:#f0a074}.cover .lead{font-size:13pt;color:#d6e4e0;margin:0}
.chips{display:flex;flex-wrap:wrap;gap:3mm}.chips span{background:#f0a074;color:#1c3f3a;font-weight:700;padding:2mm 4mm;border-radius:20mm;font-size:10pt}
.cvimg{height:165mm;border-radius:6mm;border:2mm solid #2b5650}.cvcap{position:absolute;right:16mm;bottom:8mm;margin:0;font-size:8pt;color:#a9c2bc}
.pains{display:grid;grid-template-columns:1fr 1fr;gap:5mm}.pains div{background:#fff7ef;border:1px solid #f1d7c4;border-radius:4mm;padding:7mm 8mm;font-size:13pt;font-weight:700;color:#7a3a17}
.big{font-size:15pt;font-weight:700;color:#1c3f3a;margin:2mm 0 0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:6mm}.three{display:grid;grid-template-columns:1fr 1fr 1fr;gap:5mm}
.card{background:#fffdf9;border:1px solid #dcd8cf;border-radius:4mm;padding:6mm 7mm}.card.ok{background:#e2efe3;border-color:#e2efe3}.card.warn{background:#f8e7dc;border-color:#f8e7dc}.card.soft{background:#e3ece9;border-color:#e3ece9}.card.stop{background:#fffdf9}
.card.ok h3{color:#2f6b3a}.card.warn h3{color:#b4501f}.tag{margin:0;color:#b4501f;font-weight:700;font-size:10pt}.arrow{font-weight:700;color:#1c3f3a;background:#e3ece9;border-radius:3mm;padding:3mm 4mm}
.shots3{display:grid;grid-template-columns:.62fr 1fr 1fr;gap:6mm;align-items:start}.shots3 figure{margin:0}.shots3 img{width:100%;border:1px solid #dcd8cf;border-radius:3mm;display:block}.shots3 img.tall{height:120mm;width:auto;margin:0 auto}
figcaption{font-size:9.5pt;line-height:1.5;margin-top:2mm}.lbl{display:inline-block;margin-left:2mm;background:#1c3f3a;color:#fff;font-size:8pt;padding:.3mm 2mm;border-radius:2mm}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #dcd8cf;padding:2.4mm 3mm;font-size:10pt;text-align:left;vertical-align:top;background:#fffdf9}th{background:#e3ece9}.hl{background:#fff1e6;font-weight:700}th.hl{background:#f0a074;color:#1c3f3a}
.reasons{display:grid;grid-template-columns:1fr 1fr 1fr;gap:5mm}.reasons div{background:#fffdf9;border:1px solid #dcd8cf;border-radius:4mm;padding:5mm 6mm;position:relative}.reasons b{color:#b4501f;font-size:20pt;font-family:"BIZ UDPMincho",serif}.reasons p{margin:0;font-size:9.5pt}
.price{display:grid;grid-template-columns:1fr 1.1fr;gap:8mm;flex:1}.ph{background:#1c3f3a;color:#fff;border-radius:5mm;padding:10mm;display:flex;flex-direction:column;gap:3mm}
.pl{margin:0;color:#f0a074;font-weight:700}.pv{margin:0;font-size:24pt;font-family:"BIZ UDPMincho",serif;white-space:nowrap}.pv b{font-size:46pt;color:#f0a074}.pmin{margin:0;font-size:20pt}.pmin b{font-size:28pt}
.ps{margin:0;color:#cfe0dc;font-size:10pt}.pinc{margin:auto 0 0;background:#2b5650;border-radius:3mm;padding:4mm;font-size:10.5pt}
.pr{display:flex;flex-direction:column;gap:2mm}.pr h3{margin-top:2mm}
.flow{display:grid;grid-template-columns:repeat(6,1fr);gap:3mm;flex:1;align-items:stretch}.flow div{background:#fffdf9;border:1px solid #dcd8cf;border-radius:4mm;padding:6mm 4mm;display:flex;flex-direction:column;gap:3mm;text-align:center}
.flow span{color:#b4501f;font-weight:700;font-size:18pt}.flow b{color:#1c3f3a;font-size:12.5pt}.flow small{font-size:9.5pt;line-height:1.55;color:#4f5b56}
.prep{display:grid;grid-template-columns:.55fr 1.25fr .8fr;gap:6mm;align-items:start}.prep figure{margin:0}.prep img.phone{height:118mm;border:1px solid #dcd8cf;border-radius:3mm;display:block;margin:0 auto}.prep img.pc{width:100%;border:1px solid #dcd8cf;border-radius:3mm}
.pq{display:flex;flex-direction:column;gap:2mm;align-items:center}.pq table th,.pq table td{font-size:9pt;padding:1.8mm 2mm}.qr{width:34mm}.small{font-size:9pt;margin:2mm 0 0}.url{margin:0;font-weight:700;color:#1c3f3a}
.faq{display:grid;grid-template-columns:1fr 1fr;gap:4mm}.faq div{background:#fffdf9;border:1px solid #dcd8cf;border-radius:4mm;padding:4mm 5mm}.faq h3{font-size:11pt}.faq p{margin:0;font-size:9.5pt;line-height:1.55}
.end{flex-direction:row;background:#1c3f3a;color:#fff;align-items:center;gap:10mm}.end .ec{flex:1;display:flex;flex-direction:column;gap:6mm}.end .eb{color:#f0a074}.end h1{font-size:27pt;color:#fff}.end .lead{margin:0;font-size:12pt;color:#d6e4e0}
.co{margin:0;font-weight:700}.co span{font-weight:400;font-size:9.5pt;color:#a9c2bc}.eq{display:grid;grid-template-columns:42mm 1fr;gap:4mm 5mm;align-items:center;background:#fff;color:#1c3f3a;border-radius:5mm;padding:7mm}.eq img{width:42mm}.eq p{margin:0;font-weight:700;font-size:12pt}.eq span{font-weight:400;font-size:9pt;color:#4f5b56}
.dark .foot{color:#a9c2bc;border-color:#2b5650}
'''
html = f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>Instagram広告 運用代行のご案内</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=BIZ+UDPGothic:wght@400;700&family=BIZ+UDPMincho:wght@700&display=swap">
<style>{CSS}</style></head><body>{"".join(pages)}</body></html>'''
out = os.path.join(HERE, "Instagram広告運用代行_ご案内")
open(out + ".html", "w").write(html)
subprocess.run(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000", f"--print-to-pdf={out}.pdf", "file://" + out + ".html"], check=True, capture_output=True)
print("ok", len(pages), "pages")
