"""Linguagem visual 'criador' do LinkedIn (título gigante, adesivos, laranja Ignite).
Sempre com o logo da Ignite; nunca o nome do Cristiano na arte."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
F = (ROOT / "fonts").as_uri()
OR = "#F6490D"; INK = "#141518"; PAPER = "#F3F2EF"

RAIO = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="316 142 446 794"><path fill="{c}" d="M456,920 C462,913 470,902 476,896 C481,889 488,881 490,878 C496,872 504,862 532,827 C540,817 547,808 547,808 C547,808 549,806 551,803 C553,800 566,785 579,768 C593,752 608,733 614,726 C620,718 625,712 625,712 C625,712 632,704 640,694 C647,685 663,666 674,652 C685,638 700,620 706,612 C713,603 720,594 722,592 C734,577 759,546 759,545 C759,544 740,544 668,544 C607,544 576,544 576,543 C576,542 580,538 585,532 C616,499 640,461 651,428 C661,396 662,390 662,360 C662,342 662,334 661,327 C659,317 655,301 652,292 C648,279 638,256 636,256 C635,256 635,259 635,264 C635,272 633,287 630,294 C626,307 614,328 612,325 C611,324 611,317 611,310 C611,251 588,194 547,152 C543,147 541,146 541,148 C541,149 541,157 542,167 C545,211 538,260 524,298 C518,311 508,331 501,342 C492,356 492,356 492,343 C492,328 491,318 487,305 C484,294 478,282 477,282 C476,282 471,294 465,308 C449,349 446,356 438,376 C433,387 427,402 424,411 C416,428 404,460 394,485 C390,494 382,513 376,528 C370,542 362,563 357,574 C353,586 346,604 342,614 C338,623 331,639 327,649 C323,659 320,667 320,668 C321,669 338,669 406,669 C456,669 492,669 492,670 C493,670 492,675 491,681 C488,696 484,718 474,770 C469,797 464,824 462,831 C461,838 460,845 460,846 C459,848 457,858 456,868 C454,878 451,892 450,898 C449,904 447,913 446,919 C444,929 444,935 446,932 C446,932 451,926 456,920Z"/></svg>')

CSS = f"""
@font-face{{font-family:"ID";src:url("/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf");font-weight:500}}
@font-face{{font-family:"ID";src:url("/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf");font-weight:600}}
@font-face{{font-family:"ID";src:url("/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf");font-weight:700}}
@font-face{{font-family:"IT";src:url("/usr/share/fonts/opentype/inter/Inter-Regular.otf");font-weight:400}}
@font-face{{font-family:"IT";src:url("/usr/share/fonts/opentype/inter/Inter-Medium.otf");font-weight:500}}
@font-face{{font-family:"IT";src:url("/usr/share/fonts/opentype/inter/Inter-SemiBold.otf");font-weight:600}}
@font-face{{font-family:"MO";src:url("{F}/PlexMono-400.woff2");font-weight:400}}
@font-face{{font-family:"MO";src:url("{F}/PlexMono-500.woff2");font-weight:500}}
@font-face{{font-family:"HW";src:url("{F}/Caveat-600.woff2")}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{-webkit-font-smoothing:antialiased;font-family:"ID";color:{INK}}}
.fr{{width:1080px;height:1350px;position:relative;overflow:hidden;background:{PAPER}}}
.fr.wide{{width:1920px;height:1080px}}
.fr.o{{background:{OR}}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(20,21,24,.16) 1.300px,transparent 1.600px);background-size:30px 30px}}
.o .dots{{background-image:radial-gradient(rgba(0,0,0,.11) 1.300px,transparent 1.600px)}}
.org{{position:absolute;left:0;right:0;bottom:0;background:{OR}}}
.org:before{{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(0,0,0,.10) 1.300px,transparent 1.600px);background-size:30px 30px}}
.ab{{position:absolute}}
.chipt{{position:absolute;left:64px;top:60px;display:flex;align-items:center;gap:10px;background:{INK};color:#fff;font-weight:600;font-size:24px;padding:10px 18px 10px 14px;border-radius:14px;transform:rotate(-2deg);box-shadow:0 8px 14px -6px rgba(20,21,24,.45);white-space:nowrap}}
.chipt i{{width:14px;height:14px;border-radius:50%;background:{OR}}}
.o .chipt i{{background:#fff}}
.logo{{position:absolute;right:60px;top:56px;display:flex;align-items:center;gap:10px;background:#fff;border-radius:999px;padding:9px 20px 9px 12px;font-weight:700;font-size:22px;letter-spacing:.02em;box-shadow:0 8px 14px -6px rgba(20,21,24,.45);transform:rotate(1.500deg)}}
.logo span{{width:40px;height:40px;border-radius:50%;background:{INK};display:grid;place-items:center}}.logo svg{{height:26px}}
.big{{position:absolute;left:60px;font-weight:700;line-height:.86;letter-spacing:-.045em;text-transform:uppercase}}
.sub{{position:absolute;left:66px;font-weight:500;font-size:54px;letter-spacing:-.025em;line-height:1.05}}
.tagp{{position:absolute;font-weight:700;font-size:40px;letter-spacing:-.02em;padding:12px 22px 12px 38px;clip-path:polygon(22px 0,100% 0,100% 100%,22px 100%,0 50%);white-space:nowrap}}
.tagw{{position:absolute;filter:drop-shadow(0 10px 8px rgba(20,21,24,.28))}}
.tagp{{position:relative}}
.tagp:before{{content:"";position:absolute;left:18px;top:50%;width:10px;height:10px;border-radius:50%;transform:translateY(-50%);background:{PAPER}}}
.tagp.w{{background:#fff;color:{INK}}}.tagp.w:before{{background:{OR}}}
.tagp.o{{background:{OR};color:#fff}}
.tagp.k{{background:{INK};color:#fff}}.tagp.k:before{{background:{OR}}}
.tagp s{{text-decoration-thickness:4px;text-decoration-color:{OR}}}
.tc{{position:absolute;background:#fff;border-radius:22px;padding:18px 22px;display:flex;align-items:center;gap:16px;box-shadow:0 2px 0 rgba(20,21,24,.08),0 22px 26px -14px rgba(20,21,24,.45)}}
.tc b{{display:block;font-weight:600;font-size:27px;letter-spacing:-.02em;line-height:1.08}}
.tc small{{display:block;font-family:"MO";font-size:14px;letter-spacing:.08em;color:#8A4B06;margin-top:6px;text-transform:uppercase}}
.tc .n{{font-weight:700;font-size:64px;letter-spacing:-.04em;line-height:.9}}
.tc u{{flex:none;width:74px;height:42px;border-radius:21px;background:{OR};position:relative;margin-left:auto}}
.tc u:after{{content:"";position:absolute;right:4px;top:4px;width:34px;height:34px;border-radius:50%;background:#fff;box-shadow:0 2px 4px rgba(0,0,0,.25)}}
.blk{{position:absolute;left:60px;font-weight:700;font-size:56px;letter-spacing:-.03em;line-height:1;background:{INK};color:#fff;padding:14px 22px 16px;border-radius:16px;white-space:nowrap}}
.blk em{{font-style:normal;color:#FF7A3D}}
.pill{{position:absolute;left:66px;background:#fff;border-radius:999px;padding:8px 26px 12px;font-family:"HW";font-size:40px;color:{INK};transform:rotate(-2deg);box-shadow:0 10px 14px -8px rgba(20,21,24,.5);white-space:nowrap}}
.foot{{position:absolute;left:64px;right:64px;bottom:34px;font-family:"MO";font-size:13px;letter-spacing:.03em;color:rgba(20,21,24,.8);white-space:nowrap}}
.hw{{position:absolute;font-family:"HW";font-size:44px;line-height:.95;color:{OR}}}
.o .hw{{color:#fff}}
/* celular */
.ph{{position:absolute;width:268px;height:556px;background:linear-gradient(145deg,#2A2C30,#0E0F11);border-radius:44px;padding:10px;box-shadow:0 0 0 1.500px #3A3D42 inset,0 60px 60px -36px rgba(20,21,24,.7),18px 30px 50px -20px rgba(20,21,24,.35)}}
.ps{{background:#F3F4F6;border-radius:35px;height:100%;overflow:hidden;position:relative;font-family:"IT";color:#14171C}}
.ps:after{{content:"";position:absolute;inset:0;background:linear-gradient(125deg,rgba(255,255,255,.22) 0%,rgba(255,255,255,0) 30%);pointer-events:none}}
.pst{{height:40px;display:flex;align-items:center;justify-content:space-between;padding:6px 22px 0;background:#fff;font-size:11.500px;font-weight:600}}
.pisl{{position:absolute;left:50%;top:9px;transform:translateX(-50%);width:76px;height:22px;border-radius:12px;background:#0B0C0D}}
.pic{{display:flex;align-items:flex-end;gap:2px}}.pic i{{width:3px;background:#14171C;border-radius:1px}}.pic i:nth-child(1){{height:4px}}.pic i:nth-child(2){{height:6px}}.pic i:nth-child(3){{height:8px}}.pic i:nth-child(4){{height:10px}}
.pic u{{width:20px;height:10px;border:1.200px solid #14171C;border-radius:3px;margin-left:5px;position:relative}}.pic u:after{{content:"";position:absolute;inset:1.500px;right:5px;background:#14171C;border-radius:1px}}
/* carrossel */
.num{{position:absolute;left:60px;top:150px;width:210px;height:210px;border-radius:50%;background:{OR};color:#fff;display:grid;place-items:center;font-weight:700;font-size:150px;letter-spacing:-.05em;transform:rotate(-6deg);box-shadow:0 22px 26px -14px rgba(20,21,24,.5)}}
.st{{position:absolute;left:60px;right:60px;top:410px;font-weight:700;font-size:92px;line-height:.92;letter-spacing:-.04em;text-transform:uppercase}}
.sb{{position:absolute;left:64px;right:120px;font-weight:500;font-size:40px;line-height:1.18;letter-spacing:-.02em}}
.look{{position:absolute;left:60px;right:90px;bottom:120px;background:#fff;border-radius:24px;padding:24px 28px;transform:rotate(-1.500deg);box-shadow:0 2px 0 rgba(20,21,24,.08),0 22px 26px -14px rgba(20,21,24,.45)}}
.look small{{display:block;font-family:"MO";font-size:16px;letter-spacing:.1em;text-transform:uppercase;color:{OR};margin-bottom:8px}}
.look b{{font-weight:600;font-size:31px;line-height:1.15;letter-spacing:-.02em}}
.pg{{position:absolute;left:64px;bottom:50px;display:flex;gap:8px}}.pg i{{width:12px;height:12px;border-radius:50%;background:rgba(20,21,24,.18)}}.pg i.on{{background:{INK}}}
.nx{{position:absolute;right:60px;bottom:38px;font-family:"HW";font-size:36px}}
"""

def logo(): return f'<div class="logo"><span>{RAIO.format(c=OR)}</span>IGNIT AGENCY</div>'
def chip(t): return f'<div class="chipt"><i></i>{t}</div>'
def tag(t, kind, x, y, rot, size=40): return f'<div class="tagw" style="left:{x}px;top:{y}px;transform:rotate({rot}deg)"><div class="tagp {kind}" style="font-size:{size}px">{t}</div></div>'
def blk(t, y, x=60, rot=0, size=56): return f'<div class="blk" style="top:{y}px;left:{x}px;transform:rotate({rot}deg);font-size:{size}px">{t}</div>'
def pill(t, y, x=66, rot=-2, size=40): return f'<div class="pill" style="top:{y}px;left:{x}px;transform:rotate({rot}deg);font-size:{size}px">{t}</div>'
def foot(t): return f'<div class="foot">{t}</div>'
def phone(inner, x, y, rot=6, scale=1.160, time="9:41"):
    return (f'<div class="ph" style="left:{x}px;top:{y}px;transform:rotate({rot}deg) scale({scale})"><div class="ps">'
            f'<div class="pst"><b>{time}</b><span class="pisl"></span><span class="pic"><i></i><i></i><i></i><i></i><u></u></span></div>{inner}</div></div>')
def page(body, extra="", cls="fr"):
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}{extra}</style></head><body><div class="{cls}"><div class="dots"></div>{body}</div></body></html>'
def dots(i, n): return '<div class="pg">' + ''.join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(1, n + 1)) + '</div>'
