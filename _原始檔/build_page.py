"""日日法華曆落地頁 page.html（照旅行 v28 規範），2026-11-24。base.css 共用，法華專屬放 EXTRA。"""
import json, random, os
D = os.path.dirname(os.path.abspath(__file__))
css = open(f'{D}/base.css').read()
EXTRA = '''
.cd .tk p mark{color:inherit;background:linear-gradient(100deg,transparent 2%,rgba(248,222,96,.72) 4%,rgba(246,214,80,.6) 60%,rgba(248,222,96,.75) 96%,transparent 98%) no-repeat 0 72%/100% 58%;padding:0 3px;margin:0 -1px;border-radius:2px 5px 3px 6px}
.cd .tk .route{width:92px}.cd .tk .route b{font-size:15px}
#s03b .sh{animation:sweep 2.5s linear infinite}
#s03b .sp{animation:tw 2.5s linear infinite}
@keyframes sweep{0%{left:-40%}55%{left:120%}100%{left:120%}}
@keyframes tw{0%,100%{opacity:0;transform:scale(.4)}12%{opacity:1;transform:scale(1.15) rotate(20deg)}26%{opacity:0;transform:scale(.4)}}
#s04 .n{font-size:28px}
/* 05 內頁牆 */
#s05{background:var(--night);padding:38px 0 0}
#s05 .eyebrow{color:#E9A493}#s05 h2{color:#fff;margin-top:10px}#s05 .lead{color:#C9C1B5;margin-top:8px;padding:0 16px}
#s05 .wall{position:relative;height:520px;margin-top:22px;overflow:hidden}
#s05 .wall img{position:absolute;width:80px;box-shadow:0 6px 14px rgba(0,0,0,.45)}
#s05 .wall:after{content:"";position:absolute;left:0;right:0;bottom:0;height:90px;background:linear-gradient(transparent,var(--night))}
/* 06 一頁拆解 */
#s06{padding:40px 20px 34px;background:var(--paper)}
#s06 .box{margin-top:20px;background:#fff;border-radius:8px;box-shadow:0 8px 22px rgba(30,27,25,.12);overflow:hidden}
#s06 .cap{height:62px;background:var(--paper2);border-bottom:1px solid var(--line);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:15.5px;color:var(--ink);letter-spacing:.05em;text-align:center;padding:0 12px}
#s06 .cap small{font-size:11.5px;color:var(--brick);letter-spacing:.14em;margin-bottom:3px}
#s06 .pgv{position:relative;height:381px}
#s06 .pgi{position:absolute;left:96px;top:16px;width:200px;height:349px;background-size:cover;box-shadow:0 6px 16px rgba(30,27,25,.22)}
#s06 .lb{position:absolute;width:62px;font-size:12.5px;color:var(--ink);letter-spacing:.04em;line-height:1.35}
#s06 .lb b{display:block;font-family:"Helvetica Neue",Arial;font-size:10px;color:var(--brick);letter-spacing:.16em;margin-bottom:2px}
#s06 .lb.l{left:6px;text-align:left}#s06 .lb.r{right:6px;text-align:right}
#s06 .ln{position:absolute;height:0;border-top:1px dashed var(--brick)}
/* 08 full */
/* 09 三個時刻 */
#s09{background:var(--paper2);padding:38px 16px 30px}
#s09 h2{margin-top:10px;color:var(--ink)}#s09 .lead{margin-top:8px;color:var(--text)}#s09 .eyebrow{color:var(--brick)}
.tm{display:flex;gap:12px;margin-top:16px;background:#fff;border-radius:6px;overflow:hidden;box-shadow:0 6px 16px rgba(30,27,25,.1)}
.tm .im{width:150px;height:150px;flex:none;background-size:cover;background-position:center}
.tm .tx{padding:16px 14px 14px 2px;display:flex;flex-direction:column;justify-content:center}
.tm .tx .en{font-size:10px;color:var(--brick);letter-spacing:.2em}
.tm .tx b{font-size:19px;color:var(--ink);letter-spacing:.08em;margin-top:4px}
.tm .tx p{font-size:13px;line-height:1.7;color:var(--text);margin-top:6px;letter-spacing:.03em}
.tm.rv{flex-direction:row-reverse}.tm.rv .tx{padding:16px 2px 14px 16px}
/* 10 三色 */
#s10 .ph{width:432px;height:268px;background:url(img/colors.jpg) center/cover;margin-top:20px}
#s10 .sw{justify-content:center;gap:34px}
/* 11 */
#s11 .ph{height:440px;background-image:url(img/spec.jpg);background-position:center 75%}
#s12 .ph{height:540px}
/* v10 禪意元素 */
.seal{position:absolute;z-index:4;background:#9E2B2B;color:#F8EEE2;font-family:Cream;display:flex;align-items:center;justify-content:center;border-radius:5px;box-shadow:inset 0 0 0 3px #9E2B2B,inset 0 0 0 4.5px rgba(248,238,226,.9);filter:url(#ink)}
.seal.big{width:66px;height:66px;font-size:23px;line-height:1.02;writing-mode:vertical-rl;letter-spacing:.04em}
.seal.one{width:50px;height:50px;font-size:27px;border-radius:50%;box-shadow:inset 0 0 0 3px #9E2B2B,inset 0 0 0 4.5px rgba(248,238,226,.9),0 4px 10px rgba(0,0,0,.22)}
#s03 .hdr{position:relative}
#s03 .hdr .seal{right:30px;top:112px;transform:rotate(-7deg)}
.cd .ov .no{font-family:Cream;font-size:13px;letter-spacing:.3em}
.sig{position:absolute;z-index:3;top:18px;writing-mode:vertical-rl;background:#F6F0E4;color:#2A231F;font-size:16px;line-height:1.7;letter-spacing:.14em;padding:16px 8px 26px;box-shadow:0 5px 14px rgba(0,0,0,.22);border-top:4px solid #9E2B2B;border-bottom:4px solid #9E2B2B}
.sig:after{content:"";position:absolute;left:50%;bottom:8px;width:9px;height:9px;margin-left:-4.5px;background:#9E2B2B;border-radius:2px}
.pgc{position:absolute;z-index:3;width:86px;height:153px;background-size:cover;box-shadow:0 6px 14px rgba(0,0,0,.38)}
.pgc:before{content:"";position:absolute;left:50%;top:-8px;width:54px;height:17px;margin-left:-27px;background:rgba(170,62,55,.62);transform:rotate(-4deg)}
.how .mv .seal{right:14px;top:14px;transform:rotate(8deg)}
/* 06b 看不懂翻過來 */
#s06b{padding:40px 18px 34px;background:var(--paper2)}
#s06b h2{margin-top:10px}#s06b .lead{margin-top:8px}
#s06b .pair{display:flex;justify-content:center;align-items:center;gap:0;margin-top:22px;position:relative}
#s06b .pg{width:172px}
#s06b .pg .im{width:172px;height:306px;background-size:cover;box-shadow:0 8px 20px rgba(30,27,25,.2)}
#s06b .pg .t{text-align:center;font-size:13px;color:var(--taupe);letter-spacing:.16em;margin-top:10px}
#s06b .pg .t b{color:var(--ink);font-size:15px;margin-left:4px}
#s06b .pair .seal{position:relative;margin:0 -6px;z-index:5;transform:rotate(-6deg) translateY(-14px)}
#s06b .cmp{margin-top:22px;background:#fff;border-radius:8px;box-shadow:0 6px 16px rgba(30,27,25,.1);overflow:hidden}
#s06b .cmp .r{display:flex;align-items:center;padding:14px 16px;gap:12px;border-bottom:1px dashed var(--line)}
#s06b .cmp .r:last-child{border:0}
#s06b .cmp .k{flex:none;width:58px;font-size:12.5px;color:#9E2B2B;letter-spacing:.14em}
#s06b .cmp .v{font-size:15px;line-height:1.7;color:var(--ink);letter-spacing:.03em}
#s06b .cmp .r.b .v mark{background:linear-gradient(transparent 58%,rgba(246,214,80,.6) 58%);color:inherit}
#s12 .tx{top:30px;bottom:auto}#s12 .shade{top:0;bottom:auto;height:240px;background:linear-gradient(rgba(20,16,12,.55),transparent)}
'''

P = [
 dict(n='01', who='想靜下心的人', h='每天忙到停不下來，想找回片刻平靜', k1='每天', v1='一句經文', k2='用來', v2='靜心三分鐘',
      p='撕下今天這一頁，讀一句經文，<br>心就<mark>慢慢安靜下來</mark>。', img='q1', sig='腦袋停不下來，<br>只想安靜三分鐘', sigpos='left:16px', pg='p63', pgpos='right:20px;top:200px;transform:rotate(4deg)'),
 dict(n='02', who='喜歡抄經的人', h='想抄經，卻不知道從哪一句開始', k1='每天', v1='一段經句', k2='用來', v2='對照抄寫',
      p='正面經文、背面白話釋義，<br>每天<mark>抄一句</mark>剛剛好。', img='q2', tall=True, sig='想抄經，<br>不知道從哪一句開始', sigpos='left:16px', pg='p1', pgpos='right:20px;top:26px;transform:rotate(4deg)'),
 dict(n='03', who='交換禮物', h='禮物預算一千，送一份有意義的心意', k1='送給', v1='同事朋友', k2='附', v2='精美外盒',
      p='不俗氣、有意義，<br>水墨留白<mark>放在哪都好看</mark>。', img='q3', sig='預算一千，<br>想送一份有意義的', sigpos='left:8px', pg='p105', pgpos='right:22px;top:24px;transform:rotate(4deg)'),
 dict(n='04', who='聖誕禮物', h='送給家裡的長輩，陪他平安一整年', k1='送給', v1='長輩家人', k2='陪他', v2='365 天',
      p='字大、留白多，<br>每天讀一句<mark>不費力</mark>。', img='q4'),
]
CN={'01':'其一','02':'其二','03':'其三','04':'其四'}
def card(x):
    hh = ';height:540px' if x.get('tall') else ''
    return f'''<div class="cd"><div class="ph" style="background-image:url(img/{x["img"]}.jpg){hh}"><div class="sig" style="{x["sigpos"]}">{x["sig"]}</div><div class="pgc" style="background-image:url(img/pg/{x["pg"]}.jpg);{x["pgpos"]}"></div><div class="ov"><div class="no">{CN[x["n"]]}</div><div class="who">{x["who"]}</div><h3>{x["h"]}</h3></div></div>
<div class="tk"><div class="route"><div>{x["k1"]}<b>{x["v1"]}</b></div><div>{x["k2"]}<b>{x["v2"]}</b></div></div><div><p>{x["p"]}</p></div></div></div>'''

def how(i, sid, h, lead, clip, step, en, ch=''):
    return f'''<section id="{sid}" class="how{' alt' if i % 2 == 0 else ''}">
  <div class="eyebrow">HOW TO USE 0{i}</div><h2>{h}</h2><div class="lead">{lead}</div>
  <div class="mv"><div class="ph" data-clip="{clip}" style="background-image:url(gif/clips/{clip}/001.jpg)"></div><div class="seal one">{ch}</div>
    <div class="stub"><span class="en">STEP 0{i}</span><b>{step}</b><span class="en">{en}</span></div></div>
</section>'''

random.seed(7)
wall = ''
k = 1
for r in range(5):
    for c in range(5):
        if k > 28: break
        x = c * 92 - 20 + (r % 2) * 40 + random.uniform(-6, 6)
        y = r * 118 - 30 + random.uniform(-6, 6)
        wall += f'<img src="img/wall/{k:02d}.jpg" style="left:{x:.0f}px;top:{y:.0f}px;transform:rotate({random.uniform(-4,4):.1f}deg)">'
        k += 1

caps = json.load(open(f'{D}/gif/caps_f_days.json'))
lbs = json.load(open(f'{D}/gif/caps_f_lbs.json'))

body = f'''
<section id="s03"><div class="hdr"><div class="seal big">日日安心</div>
  <div class="eyebrow">誰適合日日法華曆？</div>
  <h2>聖誕禮物 x 交換禮物<br><span class="mark">送禮送到心坎裡</span></h2>
  <div class="lead">每天一句《法華經》，<br>365 天，日日安心。</div></div>
  {''.join(card(x) for x in P[:3])}
</section>
<section id="s03b"><div class="xm"><div class="sh"></div>
  <i class="sp" style="left:8%;top:14%;animation-delay:0s"></i><i class="sp" style="left:88%;top:20%;animation-delay:.5s"></i><i class="sp" style="left:93%;top:72%;animation-delay:1s"></i><i class="sp" style="left:5%;top:78%;animation-delay:1.5s"></i><i class="sp" style="left:50%;top:6%;animation-delay:2s"></i>
  <div class="en sm">IN STOCK · READY TO SHIP</div><div class="big">熱騰騰到貨｜現貨直出</div></div></section>
<section id="s04">
  <div><div class="n">365</div><div class="c">句法華經文</div></div>
  <div><div class="n">2<small>面</small></div><div class="c">經文・白話釋義</div></div>
  <div><div class="n">3<small>色</small></div><div class="c">底座可選</div></div>
</section>
<section id="s05">
  <div class="eyebrow">一年 365 頁</div>
  <h2>一天一句，<br>讀完一整年的法華</h2>
  <div class="lead">水墨留白、直書大字，<br>每一頁都像一幅小小的畫。</div>
  <div class="wall">{wall}</div>
</section>
{how(1, 's05a', '早上撕下一頁，<br>先讀一句再出門', '撕開新的一頁，靜心讀一句經文，<br>帶著定力開始今天。', 'f_tear', '閱讀今日法華', 'READ', '撕')}
<section id="s06">
  <div class="eyebrow">一頁有什麼？</div>
  <h2>正面一句經文，<br><span class="mark">背面白話釋義、輕鬆讀懂</span></h2>
  <div class="box"><div class="cap" data-caps="f_days">{caps[0]}</div>
  <div class="pgv"><div class="pgi" data-clip="f_days" style="background-image:url(gif/clips/f_days/001.jpg)"></div><div data-caps="f_lbs">{lbs[0]}</div></div></div>
</section>
{how(2, 's06a', '翻到背面，<br>經文變成一段白話', '看不懂經文也沒關係，<br>背面的白話釋義一讀就懂。', 'f_back', '讀白話釋義', 'MEANING', '讀')}
<section id="s06b">
  <div class="eyebrow">佛經太難？</div>
  <h2>看不懂經文，<br><span class="mark">翻過來就懂</span></h2>
  <div class="lead">不用硬啃艱澀的佛學，<br>背面把經文說成你聽得懂的話。</div>
  <div class="pair">
    <div class="pg"><div class="im" style="background-image:url(img/pg/p63.jpg)"></div><div class="t">正面<b>經文</b></div></div>
    <div class="seal one">翻</div>
    <div class="pg"><div class="im" style="background-image:url(img/pg/p64.jpg)"></div><div class="t">背面<b>白話</b></div></div>
  </div>
  <div class="cmp">
    <div class="r"><span class="k">經文說</span><span class="v">三界無安，猶如火宅，<br>眾苦充滿，甚可怖畏。</span></div>
    <div class="r b"><span class="k">白話說</span><span class="v">這個世界沒有絕對安全的地方，<br>到處塞滿了<mark>讓人抓狂的苦難與焦慮</mark>。</span></div>
    <div class="r b"><span class="k">今日覺察</span><span class="v">外在的混亂是它的火，<br><mark>內在的平靜是我的自由</mark>。</span></div>
  </div>
</section>
{how(3, 's07', '對照經文抄一句，<br>讓心慢下來', '正面抄經、背面寫下今日覺察，<br>每天十分鐘的安靜時光。', 'f_copy', '對照抄經', 'COPY', '抄')}
{how(4, 's08', '放在每天經過的地方，<br>翻開今天讀一句', '書桌、玄關或佛堂旁，<br>經過時翻一頁，讀一句給自己。', 'f_flip', '翻開今天', 'DAILY', '放')}
<section id="s09">
  <div class="eyebrow">一天三個時刻</div>
  <h2>晨起、午後、夜深，<br>各有一句陪你安下心</h2>
  <div class="tm"><div class="im" style="background-image:url(img/t1.jpg)"></div><div class="tx"><span class="en">MORNING</span><b>晨起開工前</b><p>撕開新的一頁，靜心讀一句，<br>帶著清晰的頭腦開始工作。</p></div></div>
  <div class="tm rv"><div class="im" style="background-image:url(img/t2.jpg)"></div><div class="tx"><span class="en">AFTERNOON</span><b>午後焦慮時</b><p>抬頭看一眼留白與微光，<br>三分鐘，讓心降噪。</p></div></div>
  <div class="tm"><div class="im" style="background-image:url(img/t3.jpg)"></div><div class="tx"><span class="en">NIGHT</span><b>夜深沉澱時</b><p>回顧今天，把情緒隨頁面放下，<br>安心入睡。</p></div></div>
</section>
<section id="s10">
  <div class="eyebrow">底座顏色</div>
  <h2>三種顏色，<br>放在哪都安靜好看</h2>
  <div class="lead">三角摺立底座，不用另外買架子</div>
  <div class="ph"></div>
  <div class="sw">
    <div><i style="background:#4F6B53"></i>松柏綠<small>PINE</small></div>
    <div><i style="background:#7A3B3C"></i>丹心紅<small>CRIMSON</small></div>
    <div><i style="background:#A39580"></i>雲霧灰<small>MIST</small></div>
  </div>
  <div class="nt">實拍色彩依螢幕顯示略有差異</div>
</section>
<section id="s11">
  <div class="ph"></div>
  <div class="stub"><div class="hd"><span class="en">DAILY LOTUS SUTRA 2027</span><span class="en">CALENDAR</span></div>
    <div class="row"><span class="k">尺寸</span><span class="v">9 × 16 公分，直式手撕</span></div>
    <div class="row"><span class="k">內容</span><span class="v">365 天，正面經文＋背面白話釋義與今日覺察</span></div>
    <div class="row"><span class="k">底座</span><span class="v">三角摺立，松柏綠、丹心紅、雲霧灰</span></div>
    <div class="row"><span class="k">重量</span><span class="v">654 g（含外盒 905 g）</span></div>
  </div>
</section>
<section id="s12" class="full">
  <div class="ph" style="background-image:url(img/end.jpg)"></div><div class="shade"></div>
  <div class="tx"><div class="a">撕掉一頁，<br>像放下一件事</div><div class="b">每天一句經文，<br>讓這一年，日日都有平靜的片刻。</div></div>
</section>
'''
html = f'''<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8"><title>日日法華曆落地頁 v10</title>
<style>
{css}
{EXTRA}
</style></head><body>
<svg width="0" height="0" style="position:absolute"><filter id="ink"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="3"/><feDisplacementMap in="SourceGraphic" scale="2.2"/></filter></svg>
{body}
</body></html>'''
open(f'{D}/page.html', 'w').write(html)
print('ok', len(html))
