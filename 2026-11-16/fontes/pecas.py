import sys, os
sys.path.insert(0, "/home/claude/linkedin/sistema")
from parts import page, sig, RAIO

OUT = "html"; os.makedirs(OUT, exist_ok=True)
def w(name, html): open(f"{OUT}/{name}.html", "w").write(html)

# ---------- 17/11 · Atribuição (diagrama UI) ----------
css2 = """
.dg{position:relative;margin-top:56px;height:640px}
.dg .ui{position:absolute;width:420px}
.dg .g{left:0;top:0}.dg .m{right:0;top:0}
.dg .c{left:50%;transform:translateX(-50%);top:396px;width:470px;border-color:var(--ink)}
.dg .c .bar{background:var(--ink);color:#F1EFEA;border-radius:13px 13px 0 0;border-color:var(--ink)}
.dg .c .bar .dot{background:var(--ember-hi)}
.dg svg.ln{position:absolute;inset:0;width:100%;height:100%}
.row{display:flex;justify-content:space-between;align-items:flex-end}
.sum{position:absolute;left:var(--pad);right:var(--pad);bottom:150px;display:grid;grid-template-columns:1fr 1fr;border-top:1.5px solid var(--ink)}
.sum div{padding-top:18px}
.sum .n{font-family:"ID";font-weight:600;font-size:76px;letter-spacing:-.03em;line-height:1}
.sum .k{font-family:"MO";font-size:18px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);margin-bottom:10px}
"""
b2 = f"""
<div class="mast"><span><span class="tag">Mensuração</span> · Atribuição</span><b>17.11.2026</b></div>
<h1 class="h1" style="margin-top:52px;font-size:72px">Uma venda. <span class="em">Dois painéis</span> dizendo que ela é deles.</h1>
<div class="dg">
  <svg class="ln" viewBox="0 0 904 640" fill="none">
    <path d="M210 206 C210 310 330 330 400 396" stroke="#77797E" stroke-width="1.5" stroke-dasharray="5 6"/>
    <path d="M694 206 C694 310 574 330 504 396" stroke="#77797E" stroke-width="1.5" stroke-dasharray="5 6"/>
  </svg>
  <div class="ui g"><div class="bar"><span><span class="dot"></span>Google Ads</span><span class="mono" style="font-size:15px;color:var(--mute)">Pesquisa</span></div>
    <div class="cell"><div class="lbl">Conversões</div><div class="row"><div class="val">1</div><span class="chip">Clique · 3 dias antes</span></div></div></div>
  <div class="ui m"><div class="bar"><span><span class="dot"></span>Meta Ads</span><span class="mono" style="font-size:15px;color:var(--mute)">Vendas</span></div>
    <div class="cell"><div class="lbl">Resultados</div><div class="row"><div class="val">1</div><span class="chip">Visualização · 1 dia antes</span></div></div></div>
  <div class="ui c"><div class="bar"><span><span class="dot"></span>CRM / caixa</span><span class="mono" style="font-size:15px;color:#8E9096">Fonte da verdade</span></div>
    <div class="cell"><div class="lbl">Vendas registradas</div><div class="row"><div class="val">1</div><span class="chip ok">1 pedido pago</span></div></div></div>
</div>
<div class="sum">
  <div><div class="k">Soma dos painéis</div><div class="n">2</div></div>
  <div style="padding-left:28px;border-left:1px solid var(--line)"><div class="k">Vendas no caixa</div><div class="n em">1</div></div>
</div>
<div style="position:absolute;right:var(--pad);top:930px"><span class="note">Exemplo ilustrativo</span></div>
{sig()}
"""
w("p2_atribuicao", page(b2, css2))

# ---------- 20/11 · Black Friday dados ----------
css5 = """
.chart{margin-top:76px;border-top:1.5px solid var(--ink);padding-top:30px}
.chart .r{display:grid;grid-template-columns:280px 1fr;align-items:center;gap:24px;margin-bottom:30px}
.chart .lb{font-size:24px;line-height:1.3;color:var(--ink-2)}
.track{position:relative;height:64px}
.track .axis{position:absolute;left:50%;top:-14px;bottom:-14px;width:1.5px;background:var(--ink)}
.bar{position:absolute;top:8px;height:48px;border-radius:3px}
.bar.pos{left:50%;background:var(--ember)}
.bar.neg{right:50%;background:#8D8F94}
.vv{position:absolute;top:8px;height:48px;display:flex;align-items:center;font-family:"ID";font-weight:600;font-size:30px;letter-spacing:-.02em;white-space:nowrap}
.ax{display:grid;grid-template-columns:280px 1fr;gap:24px}
.ax .s{display:flex;justify-content:space-between;font-family:"MO";font-size:16px;color:var(--mute)}
.tiles{margin-top:72px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.tile{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:26px 24px}
.tile .n{font-family:"ID";font-weight:600;font-size:52px;letter-spacing:-.03em;line-height:1}
.tile .n small{font-size:28px;letter-spacing:-.01em}
.tile .t{margin-top:12px;font-size:20px;line-height:1.35;color:var(--ink-2)}
"""
# escala: 13 p.p. = 300px
b5 = f"""
<div class="mast"><span><span class="tag">Dados</span> · Black Friday 2026</span><b>20.11.2026</b></div>
<h1 class="h1" style="margin-top:52px;font-size:70px">Na Black Friday, o consumidor está voltando para <span class="em">quem ele já conhece.</span></h1>
<div class="chart">
  <div class="r"><div class="lb">Recompra de marcas conhecidas</div>
    <div class="track"><div class="axis"></div><div class="bar pos" style="width:160px"></div><div class="vv" style="left:calc(50% + 174px)">+13 p.p.</div></div></div>
  <div class="r"><div class="lb">Experimentação de marcas desconhecidas</div>
    <div class="track"><div class="axis"></div><div class="bar neg" style="width:98px"></div><div class="vv" style="right:calc(50% + 112px)">−8 p.p.</div></div></div>
  <div class="ax"><div></div><div class="s"><span>queda</span><span>variação em pontos percentuais</span><span>alta</span></div></div>
</div>
<div class="tiles">
  <div class="tile"><div class="n"><small>R$</small> 790,71</div><div class="t">ticket médio projetado, queda de 2,14%</div></div>
  <div class="tile"><div class="n">86%</div><div class="t">pretendem usar IA generativa para pesquisar</div></div>
  <div class="tile"><div class="n">56%</div><div class="t">começam a pesquisar preço com mais de 30 dias</div></div>
</div>
<div class="source" style="position:absolute;left:var(--pad);right:var(--pad);bottom:150px">Fonte: Stefanini Marketing, com Gauge, Ecglobal e W3haus (painel de 1.000 respondentes), via Brasil Inovador, 28.10.2026</div>
{sig()}
"""
w("p5_blackfriday", page(b5, css5))

# ---------- Carrossel base ----------
cssC = """
.cv .h1{font-size:92px;line-height:.98}
.cv .lead{margin-top:36px;max-width:820px}
.prog{display:flex;gap:10px}
.prog i{flex:1;height:6px;border-radius:3px;background:var(--line)}
.dark .prog i{background:var(--dark-line)}
.prog i.on{background:var(--ember)}
.dark .prog i.on{background:var(--ember-hi)}
.num{font-family:"SR";font-size:380px;line-height:.78;color:var(--ember);letter-spacing:-.04em}
.step .h2{margin-top:44px;font-size:76px}
.step .body{margin-top:30px;font-size:35px;line-height:1.4;max-width:880px}
.look{position:absolute;left:var(--pad);right:var(--pad);bottom:170px;padding:26px 28px;background:var(--card);border:1px solid var(--line);border-radius:14px;display:grid;grid-template-columns:200px 1fr;gap:20px;align-items:start}
.look .k{font-family:"MO";font-size:17px;letter-spacing:.1em;text-transform:uppercase;color:var(--ember);padding-top:5px}
.look .v{font-size:28px;line-height:1.38;color:var(--ink)}
.end .serif{font-size:84px;line-height:1.02}
.big{position:absolute;right:var(--pad);bottom:150px;font-family:"SR";font-size:560px;line-height:.75;color:var(--ember-hi);letter-spacing:-.05em}
.recap{position:absolute;left:var(--pad);right:var(--pad);bottom:160px;border-top:1px solid var(--dark-line)}
.recap div{display:grid;grid-template-columns:60px 1fr;padding:16px 0;border-bottom:1px solid var(--dark-line);font-size:26px;color:#C9C7C2}
.recap span{font-family:"MO";color:var(--ember-hi)}
.btn{display:inline-flex;align-items:center;gap:16px;margin-top:56px;padding:22px 30px;border-radius:999px;background:var(--ember-hi);color:#141518;font-family:"ID";font-weight:600;font-size:34px}
.btn small{font-family:"MO";font-weight:400;font-size:18px;letter-spacing:.1em;text-transform:uppercase;opacity:.75}
"""

def cover(tag, folio, title, lead, n_total, dark=True, glyph=""):
    return page(f"""
<div class="mast"><span><span class="tag">{tag}</span></span><b>{folio}</b></div>
<div class="cv" style="margin-top:120px"><h1 class="h1">{title}</h1><p class="lead">{lead}</p></div>
<div class="big">{glyph}</div>
<div style="position:absolute;left:var(--pad);width:380px;bottom:170px">
  <div class="prog">{''.join('<i></i>' for _ in range(n_total))}</div>
  <div class="source" style="margin-top:16px">Arraste para o lado</div></div>
{sig(dark=dark)}""", cssC, "frame dark" if dark else "frame")

def step(tag, folio, i, n, title, text, look_k, look_v):
    prog = ''.join(f'<i class="{"on" if k <= i else ""}"></i>' for k in range(1, n + 1))
    return page(f"""
<div class="mast"><span><span class="tag">{tag}</span></span><b>{folio}</b></div>
<div class="step" style="margin-top:64px"><div class="prog" style="max-width:420px">{prog}</div>
<div class="num" style="margin-top:64px">{i}</div>
<h2 class="h2">{title}</h2><p class="body">{text}</p></div>
<div class="look"><div class="k">{look_k}</div><div class="v">{look_v}</div></div>
{sig()}""", cssC)

def end(tag, folio, quote, ask, dark=True, extra=""):
    return page(f"""
<div class="mast"><span><span class="tag">{tag}</span></span><b>{folio}</b></div>
<div class="end" style="margin-top:120px"><div class="serif it">{quote}</div>
<p class="lead" style="margin-top:44px">{ask}</p></div>{extra}
{sig(dark=dark)}""", cssC, "frame dark" if dark else "frame")

# ---------- 18/11 · Carrossel 30 minutos ----------
T = "Método · Auditoria"
steps30 = [
 ("Rastreio contra caixa", "Se as conversões da plataforma não batem com as vendas, nenhuma otimização feita depois se sustenta.", "Conversões da plataforma × vendas registradas no CRM, no mesmo período"),
 ("Termos de pesquisa", "No Google Ads, é ali que aparece a verba indo para buscas que nunca vão comprar.", "Termos com custo e sem conversão, ordenados por gasto"),
 ("Marca × aquisição", "Campanha de marca com CPA baixo costuma esconder uma aquisição cara.", "CPA da busca de marca separado do resto da conta"),
 ("Criativos ativos", "Conta com um ou dois criativos rodando há meses está pagando pela fadiga.", "Quantos criativos entregam, com frequência e CTR ao longo do tempo"),
 ("Tempo de resposta ao lead", "Lead que espera um dia por retorno esfria, e a mídia leva a culpa.", "Tempo entre a entrada do lead e o primeiro contato do comercial"),
]
N = 7
w("c30_01", cover(T, f"01/{N:02d}", "Os primeiros 30 minutos numa conta que eu não conheço.", "A ordem que sigo para saber se o problema é de mídia, de rastreio ou de atendimento.", 5, glyph="30′"))
for k, (t, x, lv) in enumerate(steps30, 1):
    w(f"c30_{k+1:02d}", step(T, f"{k+1:02d}/{N:02d}", k, 5, t, x, "O que eu olho", lv))
w("c30_07", end(T, f"07/{N:02d}", "Se o item 1 falha, eu paro ali e corrijo antes de mexer em qualquer campanha.", "Qual desses pontos você confere primeiro numa conta nova?", extra='<div class="recap">'+''.join(f'<div><span>{k:02d}</span>{t}</div>' for k,(t,_,_) in enumerate(steps30,1))+'</div>'))

# ---------- 19/11 · Carrossel 6 checagens (Ignite) ----------
T2 = "Checklist · Escala de verba"
ch = [
 ("O rastreio bate com o caixa", "Escalar em cima de conversão errada multiplica o erro junto com a verba.", "Vendas do CRM e conversões da plataforma, no mesmo período"),
 ("Custo por venda estável há duas semanas", "Escalar no pico de uma oscilação é comprar a média mais cara.", "Variação semanal do custo por venda"),
 ("Campanha fora da fase de aprendizado", "Mudança grande de orçamento devolve a campanha ao aprendizado.", "Status de aprendizado de cada campanha e conjunto"),
 ("Pelo menos 3 criativos ativos", "Com mais verba, a frequência sobe e um criativo só cansa rápido.", "Criativos com entrega e sem queda forte de CTR"),
 ("O atendimento aguenta o dobro de leads", "Se o comercial não dá conta, o lead extra vira custo, não venda.", "Tempo de resposta e capacidade do time comercial"),
 ("Aumento em degraus de 20% a 30%", "Degraus menores deixam a conta absorver o aumento sem perder eficiência.", "Novo orçamento e data do próximo degrau"),
]
N2 = 9
w("c6_01", cover(T2, f"01/{N2:02d}", "6 checagens antes de escalar verba.", "Dobrar o investimento não dobra a venda quando a conta tem um gargalo.", 6, glyph="6"))
for k, (t, x, lv) in enumerate(ch, 1):
    w(f"c6_{k+1:02d}", step(T2, f"{k+1:02d}/{N2:02d}", k, 6, t, x, "O que confirmar", lv))
cssEx = cssC + """
.gb{margin-top:60px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px;align-items:end;height:520px;border-bottom:1.5px solid var(--ink);padding:0 20px}
.gb .g{display:flex;gap:14px;align-items:flex-end;justify-content:center;height:100%}
.gb .b{width:96px;border-radius:3px 3px 0 0;position:relative}
.gb .b span{position:absolute;top:-40px;left:0;right:0;text-align:center;font-family:"ID";font-weight:600;font-size:28px}
.gb .a{background:#B9B6AE}.gb .d{background:var(--ember)}
.gl{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;padding:16px 20px 0;font-family:"ID";font-weight:600;font-size:28px;text-align:center}
.lg{display:flex;gap:28px;margin-top:30px;font-size:21px;color:var(--ink-2)}
.lg i{display:inline-block;width:16px;height:16px;border-radius:2px;margin-right:8px;vertical-align:-2px}
"""
ex = page(f"""
<div class="mast"><span><span class="tag">{T2}</span></span><b>08/{N2:02d}</b></div>
<h2 class="h2" style="margin-top:60px">Quando a checagem 5 fica de fora</h2>
<p class="body" style="margin-top:20px">Verba e leads dobram. As vendas quase não mudam.</p>
<div class="gb">
  <div class="g"><div class="b a" style="height:180px"><span>100</span></div><div class="b d" style="height:360px"><span>200</span></div></div>
  <div class="g"><div class="b a" style="height:180px"><span>100</span></div><div class="b d" style="height:360px"><span>200</span></div></div>
  <div class="g"><div class="b a" style="height:180px"><span>100</span></div><div class="b d" style="height:198px"><span>110</span></div></div>
</div>
<div class="gl"><div>Verba</div><div>Leads</div><div>Vendas</div></div>
<div class="lg"><span><i style="background:#B9B6AE"></i>Antes</span><span><i style="background:var(--ember)"></i>Depois do aumento</span><span class="note" style="margin-left:auto">Índice · exemplo ilustrativo</span></div>
{sig()}""", cssEx)
w("c6_08", ex)
w("c6_09", end(T2, f"09/{N2:02d}", "Na Ignite, essa checagem vem antes de cada aumento de orçamento.", "Quer ver como ela fica na sua conta? Comente a palavra abaixo que eu te chamo.", extra='<div style="padding:0 0"><div class="btn">RAIO-X <small>nos comentários</small></div></div>'))

# ---------- 16/11 · Capa do artigo (1920x1080) ----------
cssA = """
.wide .mast{font-size:22px}
.art{display:grid;grid-template-columns:1fr 760px;gap:80px;margin-top:90px;align-items:start}
.art .h1{font-size:104px;line-height:.98}
.art .lead{margin-top:34px;font-size:34px}
.plot{background:var(--dark-2);border:1px solid var(--dark-line);border-radius:16px;padding:30px 32px}
.plot .hd{display:flex;justify-content:space-between;font-family:"MO";font-size:17px;letter-spacing:.1em;text-transform:uppercase;color:var(--dark-mute)}
.plot svg{display:block;margin-top:20px}
.plot .lg{display:flex;gap:26px;margin-top:16px;font-size:20px;color:#C9C7C2}
.plot .lg i{display:inline-block;width:22px;height:3px;margin-right:10px;vertical-align:5px}
"""
bA = f"""
<div class="mast"><span><span class="tag">Artigo</span> · Marca e performance</span><b>16.11.2026</b></div>
<div class="art">
  <div><h1 class="h1">Performance sem marca tem <span class="em">prazo de validade</span></h1>
  <p class="lead">O que acontece com o custo por venda quando a busca pelo nome da empresa começa a cair.</p></div>
  <div class="plot"><div class="hd"><span>Busca de marca × CPA</span><span>Ilustrativo</span></div>
    <svg width="696" height="380" viewBox="0 0 696 380" fill="none">
      <g stroke="#33363B" stroke-width="1">{''.join(f'<line x1="0" x2="696" y1="{y}" y2="{y}"/>' for y in (40,140,240,340))}</g>
      <line x1="232" x2="232" y1="20" y2="350" stroke="#8E9096" stroke-dasharray="4 6"/>
      <text x="242" y="34" fill="#8E9096" font-family="MO" font-size="15">corte da verba de marca</text>
      <path d="M0 80 C120 78 200 82 232 84 C320 92 420 150 520 200 C590 236 650 252 696 262" stroke="#C9C7C2" stroke-width="3"/>
      <path d="M0 300 C120 302 200 298 232 296 C330 290 420 250 520 200 C590 166 650 140 696 120" stroke="#FA581A" stroke-width="3"/>
    </svg>
    <div class="lg"><span><i style="background:#C9C7C2"></i>Busca pela marca</span><span><i style="background:#FA581A"></i>Custo por venda</span></div>
  </div>
</div>
{sig(dark=True)}
"""
w("art_capa", page(bA, cssA, "frame wide dark"))
print("ok")
