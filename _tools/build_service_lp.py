"""makaseru/business/index.html（ビジネスプラン・特別料金のご案内）から、
全プラン共通の makaseru/service/index.html を作る。
business を直したら:  python3 _tools/build_service_lp.py
"""
import re,sys
src='makaseru/business/index.html'; dst='makaseru/service/index.html'
s=open(src,encoding='utf-8').read()
def rep(a,b):
    global s
    if s.count(a)!=1: sys.exit('見つからない/重複: %d %s'%(s.count(a),a[:70]))
    s=s.replace(a,b)
def block(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)
    assert s.count(start)==1
    s=s[:i]+new+s[j:]

rep('<title>マカセル ビジネスプランのご案内</title>','<title>マカセル サービスのご案内</title>')
rep('content="マカセルのビジネスプランでできること、料金、実際の画面、始めるまでの流れ。"','content="マカセルでできること、3つのプランと料金、実際の画面、始めるまでの流れ。"')
rep('<span class="tag">ビジネスプランのご案内</span>','<span class="tag">Instagram・Facebook広告の運用サービス</span>')
rep('<h1>6店舗分の動画と広告。<br>','<h1>動画づくりから広告まで。<br>')
rep('<b>毎月6本を、しっとるが進めます。</b>','<b>毎月の動画と広告を、しっとるが進めます。</b>')
block('<div class="pricepill">','<div class="cta">','''<div class="pricepill">
        <span class="l">月額固定（広告費を増やしても、料金は変わりません）</span>
        <span><span class="u">月額</span> <span class="p num">19,800</span><span class="u">円（税込）から</span></span>
        <s style="text-decoration:none">7日間 無料でお試し</s>
      </div>
      ''')
block('<ul class="stats">','</ul>','''<ul class="stats">
        <li><span class="n num">3<small>プラン</small></span><span class="t">お店の数と<br>動画の本数で選ぶ</span></li>
        <li><span class="n num">1〜6<small>本</small></span><span class="t">月に、しっとるが<br>進める動画</span></li>
        <li><span class="n num">7<small>日間</small></span><span class="t">無料で<br>お試し</span></li>
      ''')
rep('<h2>お店が増えるほど、<br>広告は手が回らなくなります。</h2>','<h2>広告を出したい。<br>でも、続けられるか不安。</h2>')
rep('複数のお店でInstagramの広告を続けようとすると、こんなところで止まりがちです。','Instagramの広告を始めよう、続けようとすると、こんなところで止まりがちです。')
rep('<b>お店ごとにばらばら</b><span>投稿の内容も、広告の出し方も、お店や担当の方によって差が出ます。</span>','<b>何から始めればいいか分からない</b><span>Facebookページ、広告アカウント。準備の段階で止まってしまいます。</span>')
rep('<span class="ic"><svg class="i"><use href="#i-users"/></svg></span><div><b>確認が一人に集まる</b><span>本部の方、店長、担当の方。誰が見て誰が決めるかで、止まります。</span>','<span class="ic"><svg class="i"><use href="#i-yen"/></svg></span><div><b>広告を増やすほど費用も増える</b><span>広告費に応じて代行の料金が上がると、配信を広げにくくなります。</span>')
rep('<h3>ビジネスプランは、<em>','<h3>マカセルは、<em>')
rep('<b>毎月6本、しっとるが進める</b><p>ご希望を伺って、構成案・動画・投稿・広告まで。本数は、ショート動画と広告をあわせた数です。</p>','<b>毎月の動画は、しっとるが進める</b><p>ご希望を伺って、構成案・動画・投稿・広告まで。本数はライト月1本・プロ月3本・ビジネス月6本です。</p>')
rep('<b>6店舗・何人でも、1つの契約で</b><p>広告アカウントは6つまで。確認のお願いやレポートは、何人のLINEにでも届けられます。</p>','<b>料金は、毎月決まった額</b><p>広告費を増やしても、マカセルの料金は変わりません。契約期間の縛りもありません。</p>')
rep('毎月の動画づくり（月6本）','毎月の動画づくり（ライト月1本・プロ月3本・ビジネス月6本）')
rep('<h2>ご自身でも、月200まで作れます。</h2>','<h2>ご自身でも、公式LINEから追加で作れます。</h2>')
rep('しっとるが進める月6本とは別の枠です。','しっとるが進める分とは別の枠です（ライト月60・プロ月120・ビジネス月200）。')
rep('※この画面はプロプランの例です。ビジネスプランは月200です。','※この画面はプロプランの例です。')
rep('しっとるが進める月6本・自動の作り直し・音楽だけ替える','しっとるが進める月の分・自動の作り直し・音楽だけ替える')
rep('<h3>広告アカウントは6つまで（6店舗分）</h3>\n        <p>動画の希望や広告の条件は、お店ごとにお伺いします。</p>','<h3>プロは3つまで、ビジネスは6つまで</h3>\n        <p>お店ごとに、広告アカウントとInstagramを分けて管理できます。ライトはお店1つです。下の図は、ビジネスプランの例です。</p>')
rep('<p class="sub">下の内容がすべて入って、この料金です。</p>','<p class="sub">動画の本数とお店の数で選ぶ、3つのプラン。金額は月額・税込です。</p>')
block('<div class="pbox rv">','<p class="note rv"><svg class="i"><use href="#i-info"/></svg><span>広告費は、お店のカードからMetaへ直接','''<div class="plans">
      <div class="plan rv"><h3>ライト</h3><p class="yen">19,800<small>円</small></p><ul>
        <li><span>広告アカウント</span><b>1つ（お店1つ）</b></li>
        <li><span>しっとるが進める動画</span><b>月1本</b></li>
        <li><span>ご自身で作れる数</span><b>月60</b></li></ul></div>
      <div class="plan rec rv"><span class="rb">おすすめ</span><h3>プロ</h3><p class="yen">33,000<small>円</small></p><ul>
        <li><span>広告アカウント</span><b>3つまで</b></li>
        <li><span>しっとるが進める動画</span><b>月3本</b></li>
        <li><span>ご自身で作れる数</span><b>月120</b></li></ul></div>
      <div class="plan rv"><h3>ビジネス</h3><p class="yen">49,500<small>円</small></p><ul>
        <li><span>広告アカウント</span><b>6つまで</b></li>
        <li><span>しっとるが進める動画</span><b>月6本</b></li>
        <li><span>ご自身で作れる数</span><b>月200</b></li></ul></div>
    </div>
    <div class="allin rv">
      <h3>どのプランにも入っているもの</h3>
      <ul class="inc">
        <li><svg class="i"><use href="#i-zoom"/></svg><b>はじめの設定をZoomで一緒に</b><span>Meta広告の準備から、最初の広告を出すまで。</span></li>
        <li><svg class="i"><use href="#i-video"/></svg><b>毎月の動画づくり・投稿・広告</b><span>希望を伺い、構成案から広告まで、しっとるが進めます。</span></li>
        <li><svg class="i"><use href="#i-chart"/></svg><b>毎週月曜のレポートと改善案</b><span>30日間が終わった翌朝には、まとめも届きます。</span></li>
        <li><svg class="i"><use href="#i-chat"/></svg><b>公式LINEで受け取り・質問</b><span>確認やレポートは、ほかの方のLINEにも届けられます。</span></li>
        <li><svg class="i"><use href="#i-door"/></svg><b>契約期間の縛りなし</b><span>いつでも解約できます。</span></li>
        <li><svg class="i"><use href="#i-clock"/></svg><b>7日間の無料お試し</b><span>お試しにはカードのご登録が必要です。</span></li>
      </ul>
    </div>
    ''')
rep('広告費を増やしても、マカセルの料金は変わりません。</span></p>\n  </div>\n</section>\n\n<!-- 10','広告費を増やしても、マカセルの料金は変わりません。年払いは、12か月分が11か月分の料金です。</span></p>\n  </div>\n</section>\n\n<!-- 10')
rep('<p class="sub">お店にお願いするのは5つ。そのうち4つはスマホで済みます。</p>','<p class="sub">登録から最初の動画まで、この順に進みます。</p>')
rep('<ol class="start">','<ol class="start n8">')
rep('<span class="chip t">専用のURLから</span></div><b>特別料金のお申し込み画面から申し込む</b><p>利用規約に同意し、しっとるからお送りする専用のURLを開いて、カードを登録します。通常のプランを先に選ぶと、特別料金ではお申し込みいただけなくなります。</p></li>','<span class="chip t">7日間は無料</span></div><b>プランを選んで申し込む</b><p>利用規約に同意し、プランを選んでカードを登録します。7日間は無料でお試しいただけます。</p></li>')
rep('ご登録のメールアドレスに届きます。</p></li>','ご登録のメールアドレスに届きます。</p></li>\n      <li class="rv"><div class="meta"><span class="chip c1">お店</span><span class="chip t">5分ほど</span></div><b>事前のアンケートに答える</b><p>今の準備の状況をお聞きします。分からない所は「わからない」で大丈夫です。</p></li>')
rep('<summary>月6本は、お店ごとの本数ですか。</summary><p>1つのご契約で月6本です（ショート動画・広告をあわせた数）。動画の希望や広告の条件は、お店ごとにお伺いします。これとは別に、ご自身でも月200まで作れます。</p>','<summary>しっとるが進める本数は、プランでどう違いますか。</summary><p>ライト月1本・プロ月3本・ビジネス月6本です（ショート動画・広告をあわせた数）。これとは別に、ご自身でも作れます（ライト月60・プロ月120・ビジネス月200）。</p>')
rep('<summary>しっとるが進める月6本は、ご自身で作れる数（月200）から引かれますか。</summary>','<summary>しっとるが進める分は、ご自身で作れる数から引かれますか。</summary>')
rep('<summary>お店が6つより少なくても申し込めますか。</summary><p>お申し込みいただけます。広告アカウントは6つまで使えます。</p>','<summary>お店が2つ以上あります。どのプランになりますか。</summary><p>広告アカウントは、ライトが1つ、プロが3つまで、ビジネスが6つまでです。お店の数に合わせてお選びください。</p>')
rep('友だち追加のあと、特別料金のお申し込み画面（専用のURL）を、しっとるからお送りします。ご質問も','友だち追加のあと、トークの下のメニュー「アカウントを作る」から始められます。ご質問も')
rep('<a href="../about/">マカセルのご紹介（ほかのプラン）</a>','<a href="../about/">サービス紹介（スライド版）</a>')
for ng in ['特別料金','38,500','貴社','ビジネスプランは','pbox rv']:
    if ng in s: sys.exit('残っている: '+ng)
open(dst,'w',encoding='utf-8').write(s)
print('wrote',dst,len(s))
