"""法華落地頁實拍動圖片段（2026-11-24）。11/25 起改用原始 Log＋從丁丁法華成片反推的 LUT（dingding_fahua_edit.cube），裁 4:5，不再加彩度。"""
import subprocess,os,shutil,sys
from concurrent.futures import ThreadPoolExecutor
M="/Volumes/品牌發展培訓部/Ning's剪輯資料庫/○煦暖曆/01_廣告投放/日日法華曆/毛片/丁丁_新拍_1110/"
FPS=15
C={
 'f_tear': (M+'C0031.MP4', 14.0, 22.0, 1.3, 0.40),
 'f_back': (M+'C0208.MP4', 1.0, 9.0, 1.2, 0.35),
 'f_copy': (M+'C0210.MP4', 1.0, 10.0, 1.5, 0.85),
 'f_flip': (M+'C0044.MP4', 0.0, 7.0, 1.3, 0.40),
}
def run(item):
    n,(src,t0,t1,sp,cy)=item
    od=os.path.dirname(os.path.abspath(__file__))+f'/clips/{n}'; shutil.rmtree(od,ignore_errors=True); os.makedirs(od)
    L=os.path.dirname(os.path.abspath(__file__))+"/dingding_fahua_edit.cube"
    vf=(f"lut3d={L},setpts=PTS/{sp},fps={FPS},crop=iw:iw*1.25:0:(ih-iw*1.25)*{cy},scale=1080:1350:flags=lanczos")
    subprocess.run(['ffmpeg','-v','error','-ss',str(t0),'-t',str(t1-t0),'-i',src,'-vf',vf,'-q:v','2',f'{od}/%03d.jpg'],check=True,stdin=subprocess.DEVNULL)
    return n,len(os.listdir(od))
sel=sys.argv[1:] or list(C)
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(run,[(k,C[k]) for k in sel]): print(r)
