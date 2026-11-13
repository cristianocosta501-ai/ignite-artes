import sys; sys.path.insert(0, "/home/claude/linkedin/sistema")
from parts import page, sig

css = """
.tl{margin-top:58px;display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--line)}
.tl .st{padding:26px 26px 0 0;position:relative}
.tl .st:before{content:"";position:absolute;top:-6px;left:0;width:11px;height:11px;border-radius:50%;background:var(--ink)}
.tl .st.x:before{background:var(--paper);border:1.5px solid var(--mute)}
.tl .st.now:before{background:var(--ember)}
.tl .d{font-family:"MO";font-size:22px;letter-spacing:.06em;color:var(--ink)}
.tl .x .d{color:var(--mute);text-decoration:line-through;text-decoration-thickness:1.5px}
.tl .t{margin-top:10px;font-size:24px;line-height:1.35;color:var(--ink-2)}
.q{margin-top:64px;padding:40px 44px;background:var(--card);border:1px solid var(--line);border-radius:14px;position:relative}
.q .serif{font-size:52px;line-height:1.08;color:var(--ink)}
.q .src{margin-top:22px}
.q:before{content:"";position:absolute;left:0;top:28px;bottom:28px;width:4px;background:var(--ember);border-radius:0 3px 3px 0}
"""

body = f"""
<div class="mast"><span><span class="tag">Análise</span> · Meta Ads</span><b>16.11.2026</b></div>
<h1 class="h1" style="margin-top:60px">A Meta pausou os novos termos de IA. <span class="em">O risco continua com o anunciante.</span></h1>
<div class="tl">
  <div class="st x"><div class="d">30.10 → 20.11</div><div class="t">Vigência dos novos termos, já adiada uma vez</div></div>
  <div class="st"><div class="d">10.11</div><div class="t">Meta pausa a mudança, sem nova data</div></div>
  <div class="st now"><div class="d">Hoje</div><div class="t">Seguem valendo os termos atuais</div></div>
</div>
<div class="q">
  <div class="serif it">Pelos termos em vigor, cabe ao anunciante decidir se o conteúdo gerado por IA está correto antes de ir ao ar.</div>
  <div class="source src">Leitura dos termos atuais segundo o Search Engine Journal (10.11.2026)</div>
</div>
<div class="source" style="position:absolute;left:var(--pad);right:var(--pad);bottom:150px">Fontes: Search Engine Journal, 10.11.2026 · The Keyword, 23.10.2026</div>
{sig()}
"""
open(sys.argv[1], "w").write(page(body, css))
