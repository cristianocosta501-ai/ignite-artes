import sys,json,glob,numpy as np
from PIL import Image
d=sys.argv[1];rects=json.load(open(d+'/rects.json'));cuts=[0,4.5,9,13.5,18,22.5]
L=lambda i:np.asarray(Image.open(f'{d}/frames/f_{i:05d}.jpg').convert('L'),dtype=np.int16)
for s,c in enumerate(cuts):
    rs=[r for r in rects[s] if r[2]>0 and r[3]>0];a=int(c*30);b=a+135;prev=None;run=best=0
    for i in range(a,b):
        cur=L(i)
        if prev is not None:
            ok=True
            for x,y,w,h in rs:
                A=cur[max(y,0):y+h,max(x,0):x+w];B=prev[max(y,0):y+h,max(x,0):x+w]
                if A.size and (np.abs(A-B)>28).mean()>=.0008: ok=False;break
            run=run+1 if ok else 0;best=max(best,run)
        prev=cur
    print('cena',s+1,'parado',round(best/30,2),'s','OK' if best/30>=3 else 'FALHA')
