"""Capa do perfil LinkedIn do Cristiano · v2: profissão como chamariz + habilidades. 1584x396."""
import sys
sys.path.insert(0, "/home/claude/linkedin/sistema")
from criador import *
xc = f""".fr{{width:1584px;height:396px}}
.pn{{position:absolute;right:0;top:0;bottom:0;width:330px;background:{OR}}}.pn:before{{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(0,0,0,.10) 1.3px,transparent 1.6px);background-size:30px 30px}}
.chipt{{left:404px;top:26px;font-size:19px;padding:8px 15px 8px 12px}}
.logo{{right:36px;top:26px;font-size:18px;padding:7px 16px 7px 9px}}.logo span{{width:34px;height:34px}}.logo svg{{height:22px}}
.big{{left:400px}}.pill{{left:auto}}"""
b = f"""<div class="pn"></div>{chip("Fundador e CEO · Ignit Agency")}{logo()}
<div class="big" style="top:76px;font-size:64px">Growth &amp; Performance</div>
<div class="big" style="top:136px;font-size:98px;color:{OR}">Mídia paga.</div>
{tag("Google Ads", "w", 404, 248, -3, 26)}{tag("Meta Ads", "k", 578, 254, 2, 26)}{tag("TikTok Ads", "w", 734, 246, -2, 26)}{tag("Programática", "k", 912, 252, 3, 26)}
{tag("Planejamento e estratégia", "k", 430, 312, 1.5, 26)}{tag("Growth", "w", 806, 316, -3, 26)}{tag("Branding", "k", 946, 312, 2, 26)}
{tag("Retail", "w", 1100, 308, -2, 26)}
{pill("do plano ao resultado →", 100, 1276, -4, 26)}
{tag("Dashboards e B.I.", "w", 1286, 176, 3, 26)}{tag("Kwai Ads", "k", 1262, 250, -4, 26)}{tag("X Ads", "w", 1436, 262, 3, 26)}"""
open("capa2.html", "w").write(page(b, xc))
