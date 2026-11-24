"""法華落地頁實拍動圖片段（2026-11-24）。丁丁用調色對齊麻豆版，裁 4:5，彩度 1.3、對比 1.04。"""
import subprocess,os,shutil,sys
from concurrent.futures import ThreadPoolExecutor
M="/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/01_廣告投放/日日法華曆/毛片/丁丁_新拍_1110_調色對齊麻豆/"
FPS=15
C={
 'f_tear': (M+'C0031.mp4', 14.0, 22.0, 1.3, 0.40),
 'f_back': (M+'C0208.mp4', 1.0, 9.0, 1.2, 0.35),
 'f_copy': (M+'C0210.mp4', 1.0, 10.0, 1.5, 0.45),
 'f_flip': (M+'C0044.mp4', 0.0, 7.0, 1.3, 0.40),
}
def run(item):
    n,(src,t0,t1,sp,cy)=item
    od=os.path.dirname(os.path.abspath(__file__))+f'/clips/{n}'; shutil.rmtree(od,ignore_errors=True); os.makedirs(od)
    vf=(f"setpts=PTS/{sp},fps={FPS},crop=iw:iw*1.25:0:(ih-iw*1.25)*{cy},scale=1080:1350:flags=lanczos,eq=saturation=1.3:contrast=1.04")
    subprocess.run(['ffmpeg','-v','error','-ss',str(t0),'-t',str(t1-t0),'-i',src,'-vf',vf,'-q:v','2',f'{od}/%03d.jpg'],check=True,stdin=subprocess.DEVNULL)
    return n,len(os.listdir(od))
sel=sys.argv[1:] or list(C)
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(run,[(k,C[k]) for k in sel]): print(r)
