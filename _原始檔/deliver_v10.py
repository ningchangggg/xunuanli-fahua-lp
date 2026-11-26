"""法華 v10 交件：新做 03、06b 靜態與 05a/06a/07/08 GIF，其餘沿用 v9／v8b。先組在本機再整包複製到 NAS。"""
import os, shutil, base64, io
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__))
NAS="/Volumes/品牌發展培訓部/Ning's剪輯資料庫/○煦暖曆/04_內容企劃/_多產品/落地頁改版設計_1122/"
V9=NAS+"11.26_日日法華曆_落地頁改版_v9_加送禮範例_綠紅雙色外盒/"
V8=NAS+"11.25_日日法華曆_落地頁改版_v8_抄經兩張與收尾照片上移/"
B8=NAS+"11.26_日日法華曆_現貨三日出貨改熱騰騰到貨現貨直出_v1/"
NAME="11.26_日日法華曆_落地頁改版_v10_掛軸禪意_內頁心聲籤_翻過來就懂"; SHORT="11.26_日日法華曆_落地頁改版_v10"
O=D+"/out/"+NAME; shutil.rmtree(O,ignore_errors=True)
for s in ['說明圖_1080寬','動圖_MP4備用','_原始檔']: os.makedirs(f'{O}/{s}')
# (檔名, 來源圖, 來源mp4)
L=[('03_誰適合日日法華曆_內頁心聲籤.jpg',('new','s03'),None),
   ('03b_熱騰騰到貨_金光_GIF.gif',V9+'說明圖_1080寬/03b_熱騰騰到貨_金光_GIF.gif',B8+'動圖_MP4備用/fahua-lp-v8b-03b-instock.mp4'),
   ('03c_送禮範例_綠紅雙色外盒_GIF.gif',V9+'說明圖_1080寬/03c_送禮範例_綠紅雙色外盒_GIF.gif',V9+'動圖_MP4備用/03c_送禮範例_綠紅雙色外盒.mp4'),
   ('03d_送禮範例_送給長輩.jpg',V9+'說明圖_1080寬/03d_送禮範例_送給長輩.jpg',None),
   ('04_數字列.jpg',V9+'說明圖_1080寬/04_數字列.jpg',None),
   ('05_365頁內頁牆.jpg',V9+'說明圖_1080寬/05_365頁內頁牆.jpg',None),
   ('05a_閱讀今日法華_撕印_GIF.gif',D+'/gif/enc/s05a.gif',D+'/gif/enc/s05a.mp4'),
   ('06_一頁拆解_正背面輪播_GIF.gif',V9+'說明圖_1080寬/06_一頁拆解_正背面輪播_GIF.gif',V8+'動圖_MP4備用/06_一頁拆解_正背面輪播_GIF.mp4'),
   ('06a_翻到背面讀白話_讀印_GIF.gif',D+'/gif/enc/s06a.gif',D+'/gif/enc/s06a.mp4'),
   ('06b_看不懂經文翻過來就懂.jpg',('new','s06b'),None),
   ('07_對照經文抄一句_抄印_GIF.gif',D+'/gif/enc/s07.gif',D+'/gif/enc/s07.mp4'),
   ('08_HOWTOUSE04_放在每天經過的地方_放印_GIF.gif',D+'/gif/enc/s08.gif',D+'/gif/enc/s08.mp4'),
   ('09_一天三個時刻.jpg',V9+'說明圖_1080寬/09_一天三個時刻.jpg',None),
   ('10_三色底座.jpg',V9+'說明圖_1080寬/10_三色底座.jpg',None),
   ('11_規格.jpg',V9+'說明圖_1080寬/11_規格.jpg',None),
   ('12_轉折.jpg',V9+'說明圖_1080寬/12_轉折.jpg',None)]
parts=[]; imgs=[]
for nm,src,mp4 in L:
    dst=f'{O}/說明圖_1080寬/{nm}'
    if isinstance(src,tuple): Image.open(f'{D}/sec/{src[1]}.png').convert('RGB').save(dst,quality=90)
    else: shutil.copy(src,dst)
    imgs.append(nm)
    if mp4:
        shutil.copy(mp4,f'{O}/動圖_MP4備用/{nm.rsplit(".",1)[0]}.mp4')
        parts.append(f'<video autoplay muted loop playsinline src="data:video/mp4;base64,{base64.b64encode(open(mp4,"rb").read()).decode()}"></video>')
    else:
        im=Image.open(dst); im=im.resize((864,round(im.height*864/im.width)),Image.LANCZOS); b=io.BytesIO(); im.save(b,'JPEG',quality=86)
        parts.append(f'<img src="data:image/jpeg;base64,{base64.b64encode(b.getvalue()).decode()}">')
head='<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>日日法華曆落地頁 v10</title><style>body{margin:0;background:#888}main{max-width:432px;margin:0 auto;background:#fff}img,video{display:block;width:100%}</style><main>'
open(f'{O}/{SHORT}_整頁預覽_動態.html','w').write(head+'\n'.join(f'<img src="說明圖_1080寬/{n}">' for n in imgs)+'</main>')
open(f'{O}/{SHORT}_整頁預覽_單檔整合.html','w').write(head+''.join(parts)+'</main>')
for f in ['build_page.py','page.html','base.css','fonts_cream.otf','shot.py','deliver_v10.py','dingding_fahua_edit.cube']: shutil.copy(f'{D}/{f}',f'{O}/_原始檔/{f}')
for f in ['clips_fh.py','render_gif.py','enc.sh','caps_f_days.json','caps_f_lbs.json']: shutil.copy(f'{D}/gif/{f}',f'{O}/_原始檔/{f}')
shutil.copytree(f'{D}/img',f'{O}/_原始檔/img')
print(O)
