"""Capa da página da Ignite no LinkedIn · 1128x191 (desenhada em 2256x382; zona do logo: canto inferior esquerdo, livre)."""
import sys
sys.path.insert(0, "/home/claude/linkedin/sistema")
from criador import *
xc = f""".fr{{width:2256px;height:382px}}
.pn{{position:absolute;right:0;top:0;bottom:0;width:500px;background:{OR}}}.pn:before{{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(0,0,0,.10) 1.3px,transparent 1.6px);background-size:30px 30px}}
.chipt{{left:572px;top:22px;font-size:22px;padding:8px 16px 8px 12px}}
.logo{{right:44px;top:26px;font-size:24px;padding:9px 22px 9px 12px}}
.big{{left:568px}}.pill{{left:auto}}"""
b = f"""<div class="pn"></div>{chip("Time no Brasil · atendimento em português")}{logo()}
<div class="big" style="top:78px;font-size:70px">Agência de performance</div>
<div class="big" style="top:146px;font-size:98px;color:{OR}">Mídia paga.</div>
{tag("Google Ads", "w", 572, 262, -3, 28)}{tag("Meta Ads", "k", 758, 270, 2, 28)}{tag("TikTok Ads", "w", 926, 260, -2, 28)}
{tag("Criação", "k", 1118, 268, 3, 28)}{tag("Dashboards e B.I.", "w", 1268, 262, -2, 28)}{tag("Sites", "k", 1540, 270, 2, 28)}
{pill("peça seu RAIO-X →", 128, 1846, -4, 38)}
{tag("auditoria da sua conta", "w", 1806, 244, 3, 28)}"""
open("capa_ignite.html", "w").write(page(b, xc))
