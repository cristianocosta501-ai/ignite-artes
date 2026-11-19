"""Capa do perfil LinkedIn do Cristiano · 1584x396 (zona da foto: canto inferior esquerdo, livre)."""
import sys
sys.path.insert(0, "/home/claude/linkedin/sistema")
from criador import *
xc = f""".fr{{width:1584px;height:396px}}
.pn{{position:absolute;right:0;top:0;bottom:0;width:420px;background:{OR}}}.pn:before{{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(0,0,0,.10) 1.3px,transparent 1.6px);background-size:30px 30px}}
.chipt{{left:404px;top:30px;font-size:19px;padding:8px 15px 8px 12px}}
.logo{{right:36px;top:28px;font-size:18px;padding:7px 16px 7px 9px}}.logo span{{width:34px;height:34px}}.logo svg{{height:22px}}
.big{{left:400px}}
.rc{{position:absolute;background:#fff;border-radius:18px;padding:12px 18px;box-shadow:0 2px 0 rgba(20,21,24,.08),0 18px 22px -12px rgba(20,21,24,.5);display:flex;align-items:center;gap:18px}}
.rc small{{display:block;font-family:"MO";font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:#8A4B06}}.rc b{{display:block;font-weight:600;font-size:22px;letter-spacing:-.02em}}.rc .n{{font-weight:700;font-size:50px;letter-spacing:-.04em;line-height:.9;margin-left:auto}}
.nt{{position:absolute;right:38px;bottom:12px;font-family:"MO";font-size:11px;color:rgba(255,255,255,.85)}}"""
b = f"""<div class="pn"></div>{chip("Growth & Performance · mídia paga")}{logo()}
<div class="big" style="top:84px;font-size:88px">Verba decidida</div>
<div class="big" style="top:164px;font-size:88px;color:{OR}">pelo caixa.</div>
{tag("Google Ads", "w", 404, 282, -3, 28)}{tag("Meta Ads", "k", 590, 290, 2, 28)}{tag("TikTok Ads", "w", 756, 280, -2, 28)}
<div class="rc" style="left:1196px;top:100px;width:270px;transform:rotate(-4deg)"><div><small>Google Ads</small><b>conversão</b></div><div class="n">1</div></div>
<div class="rc" style="left:1270px;top:178px;width:270px;transform:rotate(3deg)"><div><small>Meta Ads</small><b>resultado</b></div><div class="n">1</div></div>
{tag("painéis: <s>2 vendas</s>", "w", 1060, 286, -4, 26)}{tag("caixa: 1 venda", "k", 1330, 300, 3, 26)}
<div class="nt">exemplo ilustrativo</div>"""
open("capa.html", "w").write(page(b, xc))
