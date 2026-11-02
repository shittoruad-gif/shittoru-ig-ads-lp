# 営業担当がそのまま渡せる「Meta広告 運用サービス マカセル のご案内」PDF（2026-11-02 三上様「Meta広告としてマカセルを使う前提とした料金や機能なども含めて」）
# 元の「Instagram広告 運用代行のご案内」（build.py）（2026-11-02 三上様「料金もすべて入れて」）
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


FOOT = "Meta広告 運用サービス「マカセル」のご案内 ｜ 株式会社しっとる"
# 料金・機能の一次資料：makaseru/shared/const.ts（PLANS・DONE_FOR_YOU・HUMAN_SUPPORT・ADDON_PACKS・ANNUAL_PAID_MONTHS）と特商法（client/src/pages/Legal.tsx）
PLANS = [("ライト", 19800, 1, 1, 60, "1人"), ("プロ", 33000, 3, 3, 120, "3人"), ("ビジネス", 49500, 6, 5, 200, "何人でも")]
yen = lambda n: f"{n:,}円"

pages.append(f"""<section class="pg cover"><div class="cv">
<p class="eb">株式会社しっとる　Meta広告（Instagram・Facebook）</p>
<h1>Meta広告 運用サービス<br>「マカセル」のご案内</h1>
<p class="lead">お店の動画から、ショート動画と広告をつくり、Instagramへの投稿・広告の配信・入れ替え・毎週のレポートまで。確認は公式LINEのボタンだけ。しっとるの担当者のサポート付きです。</p>
<div class="chips"><span>7日間無料でお試し</span><span>しっとるが代わりに作る</span><span>確認は公式LINEで</span><span>毎週の成績レポート</span></div>
</div><img class="cvimg" src="{img('reel.png')}" alt="制作例のショート動画"><p class="cvcap">制作例（導入店舗の整体院のショート動画広告）</p></section>""")

page("お困りごと", "こんなお悩みはありませんか", """<div class="pains">
<div>広告を出したいが、何から始めればいいか分からない</div>
<div>動画が大事なのは分かっているが、作る時間がない</div>
<div>広告を任せても、何をしているのか中身が見えない</div>
<div>出した広告を、いつ止めて、いつ替えればいいか分からない</div></div>
<p class="big">マカセルなら、作る・出す・見直すを、しっとるがまとめて行います。</p>""" + gl(("Meta広告", "Meta社が運営するInstagram・Facebookに出す広告です"), ("マカセル", "しっとるの、広告づくりと運用の仕組みです。お店の方は公式LINEで確認するだけです")))

page("マカセルとは", "作るのも、出すのも、見直すのも、ひとつの仕組みで", """<div class="flow" style="grid-template-columns:repeat(4,1fr);flex:none">
<div><span>1</span><b>作る</b><small>お店の動画・写真から、ショート動画と広告の文章・画像を作ります。しっとるが代わりに作る本数がプランに入っています</small></div>
<div><span>2</span><b>確かめる</b><small>できた案が公式LINEに届きます。「承認」のボタンを押すだけです。使えない言葉がないかも確かめます</small></div>
<div><span>3</span><b>出す</b><small>お店のInstagramへの投稿と、Meta広告の配信を行います。お店から近い人に絞って届けます</small></div>
<div><span>4</span><b>見直す</b><small>毎朝、広告ごとに「続ける・止める・替える」を判定。替える広告は、新しい動画を作って入れ替えます</small></div></div>
<p class="big">毎週月曜の朝には、広告の成績レポートが公式LINEに届きます。</p>""")

page("できること", "マカセルでできること", """<div class="reasons">
<div><b>1</b><h3>お店の動画からショート動画</h3><p>お店で撮った動画・写真から、テロップ入りのショート動画を作ります。見た目は見本の9種類から選ぶだけです。</p></div>
<div><b>2</b><h3>広告の文章と画像</h3><p>お店の情報から、広告の文章と画像の案を作ります。打ち合わせのメモからも、広告の案を組み立てられます。</p></div>
<div><b>3</b><h3>公式LINEで確認・承認</h3><p>できた案はLINEに届き、ボタンで承認・作り直しを選べます。パソコンを開く必要はありません。</p></div>
<div><b>4</b><h3>Instagramへの投稿</h3><p>承認した動画を、お店のInstagramに投稿します。お店と先生個人など、投稿先が2つある場合はその都度選べます。</p></div>
<div><b>5</b><h3>配信・毎朝の判定・入れ替え</h3><p>投稿から広告を作って配信。毎朝の判定で反応が落ちた広告は、新しい動画を作ってLINEで確認のうえ入れ替えます。</p></div>
<div><b>6</b><h3>言葉のチェックとレポート</h3><p>健康・美容などで使えない言葉がないかを確かめます。毎週月曜の朝、成績レポートがLINEに届きます。</p></div></div>""")

page("実際の画面", "公式LINEで、ここまでできます", f"""<div class="shots5">
<figure><img src="{img('mk_menu.jpg')}" class="wide"><figcaption><b>公式LINEのメニュー</b><br>動画・広告をつくる、確認・承認、規約チェックなどをボタンで</figcaption></figure>
<figure><img src="{img('mk_proposal.png')}"><figcaption><b>広告の案</b><br>画像つきの案が届き、承認か作り直しを選ぶ</figcaption></figure>
<figure><img src="{img('mk_looks.png')}"><figcaption><b>ショート動画の見た目</b><br>見本の9種類から選ぶだけ</figcaption></figure>
<figure><img src="{img('mk_report.png')}"><figcaption><b>成績レポート</b><br>直近7日の数字と、今週やること</figcaption></figure>
<figure><img src="{img('mk_judge.png')}"><figcaption><b>広告ごとの判定</b><br>続ける・止める・画像や動画を替える</figcaption></figure></div>""" + note("画面は2026年10月のものです。店名・数値は見本です。"))

page("役割", "しっとるが行うこと、お店にお願いすること", """<div class="three">
<div class="card ok"><h3>しっとるが行うこと</h3><ul>
<li>はじめの設定（Zoomで一緒に。Meta広告の準備から最初の広告まで）</li><li>お店の登録と、Meta（Instagram・Facebook）とのつなぎ</li><li>ショート動画・広告の作成（プランの本数まで）</li><li>Instagramへの投稿、広告の配信・入れ替え・停止</li><li>毎朝の判定の確認と、反応が落ちた広告の作り直し</li></ul></div>
<div class="card warn"><h3>お店にお願いすること</h3><ul>
<li>Facebookページ・Instagram・広告アカウントの「使ってよい」という許可を、しっとるに渡す（手順はURLでご案内）</li><li>広告費のカードをMetaに登録する（カード番号はご自身で）</li><li>お店の動画・写真をスマホで撮って送る</li><li>公式LINEに届く案を確認して、承認する</li></ul></div>
<div class="card soft"><h3>安心していただけること</h3><ul>
<li>パスワードやカード番号を、しっとるがお聞きすることはありません</li><li>広告費はお店からMeta社へ直接。しっとるがお預かりすることはありません</li><li>予算を上げるのは、文字でご了解をいただいたときだけ</li><li>お店のアカウントは、お店のもののまま</li></ul></div></div>""")

page("ほかの頼み方との比べ", "どんな頼み方が合うか", """<div class="tw"><table>
<tr><th></th><th>ご自身で広告を出す</th><th>一般的な広告運用代行</th><th class="hl">マカセル</th></tr>
<tr><td>動画づくり</td><td>ご自身で撮影・編集</td><td>別料金のことが多い</td><td class="hl">料金に込み（しっとるが作る本数＋ご自身でも作れる）</td></tr>
<tr><td>確認のしかた</td><td>—</td><td>メールや打ち合わせ</td><td class="hl">公式LINEのボタンで承認</td></tr>
<tr><td>Instagramへの投稿</td><td>ご自身で</td><td>広告のみのことが多い</td><td class="hl">承認した動画を投稿</td></tr>
<tr><td>見直しの早さ</td><td>ご自身で数字を読む</td><td>月1回の報告が多い</td><td class="hl">毎朝の判定・毎週のレポート</td></tr>
<tr><td>料金</td><td>広告費のみ</td><td>広告費の何割か＋制作費が多い</td><td class="hl">月額の定額（広告費は別）</td></tr>
<tr><td>向いている方</td><td>時間があり、広告を学びたい方</td><td>大きな予算で、幅広く出したい方</td><td class="hl">近くのお客様を、手間をかけずに増やしたい店舗の方</td></tr>
</table></div>""" + note("ほかの頼み方は一般的な傾向で、会社によって異なります。"))

rows = "".join(f"<tr><td class='pn'>{n}</td><td class='pp'><b>{yen(p)}</b>／月</td><td>{s}店舗</td><td>月{d}本</td><td>月{c}本</td><td>{l}</td><td>{yen(p*11)}</td></tr>" for n, p, s, d, c, l in PLANS)
page("料金", "料金（すべて税込）", f"""<div class="tw"><table class="plans">
<tr><th>プラン</th><th>月額</th><th>登録できるお店</th><th>しっとるが代わりに作る<br>（ショート動画・広告）</th><th>ご自身でも作れる数</th><th>公式LINEでつなげる人数</th><th>年払い<br>（11か月分）</th></tr>{rows}</table></div>
<div class="two" style="margin-top:2mm"><div class="card ok"><h3>どのプランにも含まれるもの</h3><ul>
<li>はじめの設定（Zoomで一緒に。Meta広告の準備から最初の広告まで）</li><li>広告の案づくりから、出す・入れ替えるまで（おまかせ）</li><li>お店の動画・写真からのショート動画づくり（おまかせ）</li><li>毎週月曜の朝の成績レポート（公式LINE）</li></ul></div>
<div class="card soft"><h3>そのほかの料金</h3><ul><li><b>追加30本</b>：3,300円（買った日から30日間）</li><li><b>広告費</b>：料金とは別に、お店のカードからMeta社へ直接お支払いいただきます。金額はお店でお決めいただきます</li></ul></div></div>""" + gl(("しっとるが代わりに作る", "ショート動画と広告をあわせた本数です。ご自身で作れる数とは別に数えます"), ("年払い", "1年分を一度にお支払いいただく方法です。月額の11か月分で、1か月分お得です")))

page("料金のきまり", "お試し・お支払い・解約について", """<div class="two">
<div class="card"><h3>7日間の無料お試し</h3><ul><li>お申し込み時にカードをご登録いただき、<b>7日間は無料</b>でお試しいただけます</li><li>8日目に初回の決済を行い、以降は毎月（年払いは毎年）同じ日に同じ額を自動で決済します</li><li>お試しはお一人さま1回です。お試し中にご利用いただけるのはアプリと公式LINEの自動の答えで、担当者のサポートは初回の決済の後から始まります</li></ul></div>
<div class="card"><h3>解約・返金</h3><ul><li>料金プランの画面の「解約する」から、<b>いつでも解約</b>できます</li><li>解約後は次回以降の決済は行われず、お支払い済みの期間の終わりまでご利用いただけます</li><li>お試し期間中に解約された場合、料金はかかりません</li><li>デジタルサービスの性質上、お支払い済みの料金は返金いたしかねます</li></ul></div></div>
<div class="card soft" style="margin-top:2mm"><h3>作れる数のきまり</h3><ul><li>作れる数は、お支払いの日から1か月ごとに戻ります（毎月1日ではありません）</li><li>しっとるが代わりに作る本数と、ご自身で作れる数は、別々に数えます</li></ul></div>""")

page("ご利用の流れ", "ご相談から、毎週の見直しまで", """<div class="flow">
<div><span>1</span><b>無料相談</b><small>フォームに入力。お店に合うプランをご提案</small></div>
<div><span>2</span><b>お申し込み</b><small>公式LINEからアカウントを作り、プランを選んでカード登録（7日間無料）</small></div>
<div><span>3</span><b>広告の準備</b><small>URLの手順どおりに、しっとるに許可を渡し、広告費のカードを登録</small></div>
<div><span>4</span><b>はじめの設定</b><small>Zoomで一緒に。お店の登録とMetaとのつなぎは、しっとるが行います</small></div>
<div><span>5</span><b>作る・確認・出す</b><small>動画を送る → 案がLINEに届く → 承認 → 投稿と配信</small></div>
<div><span>6</span><b>見直し</b><small>毎朝の判定で入れ替え。毎週月曜にレポート</small></div></div>""" + note("広告の成果は業種・商圏・ご予算などで異なり、特定の成果をお約束するものではありません。"))

page("広告の準備", "準備は、URLの手順どおりに進めるだけ", f"""<div class="prep">
<figure><img src="{img('guide_where.png')}" class="phone"><figcaption>今の状態に合わせて、始める場所を選べます</figcaption></figure>
<figure><img src="{img('perm.jpg')}" class="pc"><figcaption>しっとるに3つの許可を渡します（実際のMetaの画面）</figcaption></figure>
<div class="pq"><table><tr><th>渡すもの</th><th>オンにするもの</th></tr><tr><td>広告アカウント</td><td>フルアクセス</td></tr><tr><td>Facebookページ</td><td>広告・コンテンツ・インサイト</td></tr><tr><td>Instagram</td><td>広告・コンテンツ・インサイト</td></tr></table>
<p class="small">手順のページ（スマホでもパソコンでも）</p><img src="{img('qr_guide.png')}" class="qr"><p class="url">ig-ads.s-toru.com/start/</p><p class="small">マカセルのアカウント作成は、公式LINEからご案内します</p></div></div>""" + gl(("Facebookページ", "お店の名前で作るFacebookのページです。広告の名義に使います。投稿しなくて大丈夫です")))

page("よくあるご質問", "お客様からよく伺うこと", """<div class="faq">
<div><h3>広告の知識が全くなくても大丈夫ですか？</h3><p>大丈夫です。はじめの設定はZoomで一緒に行い、作る・出す・入れ替えるは、しっとるが行います。お店の方は公式LINEで確認するだけです。</p></div>
<div><h3>動画の素材は自分で用意しますか？</h3><p>スマホで撮ったお店の動画・写真で作れます。撮るものは業種に合わせてご案内します。</p></div>
<div><h3>プランの本数より多く作りたいときは？</h3><p>ご自身で作れる数（ライト月60本など）の中で作れます。足りなければ、追加30本（3,300円）をお求めいただけます。</p></div>
<div><h3>パスワードを教える必要はありますか？</h3><p>ありません。Facebook・Instagram・カードのどれも、しっとるにお伝えいただくことはありません。</p></div>
<div><h3>途中でやめられますか？</h3><p>料金プランの画面から、いつでも解約できます。お支払い済みの期間の終わりまでご利用いただけます。</p></div>
<div><h3>広告費はいくら必要ですか？</h3><p>お店のご予算に合わせて決めます。金額はお店でお決めください。広告費は料金とは別に、Meta社へ直接お支払いいただきます。</p></div></div>""")

pages.append(f"""<section class="pg dark end"><div class="ec">
<p class="eb">まずは、無料相談から</p><h1>7日間、無料で<br>お試しいただけます。</h1>
<p class="lead">「うちのお店でも使える？」というご質問だけでも大歓迎です。フォームにご記入いただければ、お店に合ったプランと進め方をご提案します。</p>
<p class="co">株式会社しっとる<br><span>〒700-0901 岡山県岡山市北区本町6-36 第一セントラルビル4階 ／ shittoru.ad@gmail.com</span></p></div>
<div class="eq"><img src="{img('qr_form.png')}"><p>無料相談フォーム<br><span>約1分で入力できます</span></p><img src="{img('qr_mklp.png')}"><p>マカセルの紹介ページ<br><span>料金プランもこちら</span></p></div></section>""")
CSS = '''
.shots5{display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr 1fr;gap:4mm;align-items:start}.shots5 figure{margin:0}.shots5 img{width:100%;border:1px solid #dcd8cf;border-radius:3mm;display:block}.shots5 figcaption{font-size:8.5pt}
table.plans td,table.plans th{font-size:10pt;text-align:center;vertical-align:middle}table.plans .pn{font-weight:700;color:#1c3f3a;font-size:12pt}table.plans .pp b{font-size:15pt;color:#b4501f}

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
html = f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>Meta広告 運用サービス「マカセル」のご案内</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=BIZ+UDPGothic:wght@400;700&family=BIZ+UDPMincho:wght@700&display=swap">
<style>{CSS}</style></head><body>{"".join(pages)}</body></html>'''
out = os.path.join(HERE, "Meta広告_マカセル_ご案内")
open(out + ".html", "w").write(html)
subprocess.run(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000", f"--print-to-pdf={out}.pdf", "file://" + out + ".html"], check=True, capture_output=True)
print("ok", len(pages), "pages")
