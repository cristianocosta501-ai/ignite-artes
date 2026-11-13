import sys, os, pathlib
sys.path.insert(0, "/home/claude/linkedin/sistema"); sys.path.insert(0, "/home/claude/linkedin/semana-2026-11-16")
sys.argv = [sys.argv[0], "/dev/null"]
import p1v3
from criador import *

AV = pathlib.Path("/home/claude/linkedin/avatar/avatar.png").as_uri()
OUT = "html2"; os.makedirs(OUT, exist_ok=True)
def w(n, h): open(f"{OUT}/{n}.html", "w").write(h)
def av(x, y, s=170, rot=6): return f'<img class="ab" src="{AV}" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;transform:rotate({rot}deg);filter:drop-shadow(0 14px 12px rgba(20,21,24,.35))">'
def big(t, top, size, color=INK): return f'<div class="big" style="top:{top}px;font-size:{size}px;color:{color}">{t}</div>'
def sub(t, top, size=54): return f'<div class="sub" style="top:{top}px;font-size:{size}px">{t}</div>'
def org(h): return f'<div class="org" style="height:{h}px"></div>'
def card(html, x, y, rot, wd): return f'<div class="tc" style="left:{x}px;top:{y}px;width:{wd}px;transform:rotate({rot}deg)">{html}</div>'
ADX = p1v3.css + ".f-ph{position:relative;left:0;top:0;transform:none}"

# ============ 16/11 · Meta ============
b = f"""{org(520)}{chip("Meta Ads · termos de IA")}{logo()}
{big("A Meta<br>pausou", 150, 186)}{sub("os novos termos de IA.", 486)}{av(836, 250, 180)}
{tag("<s>20.11</s>", "w", 66, 590, -5)}{tag("sem nova data", "o", 250, 612, 3)}
{card("<div><b>Traduzir o texto</b><small>ligado por padrão</small></div><u></u>", 60, 724, -4, 330)}
{card("<div><b>Gerar fundo da imagem</b><small>ligado por padrão</small></div><u></u>", 150, 842, 3, 330)}
<div class="ab" style="left:722px;top:548px;transform:rotate(6deg) scale(1.100)">{p1v3.phone}</div>
{blk("mas o risco continua", 1004, 60, -1.5)}{blk("com <em>o anunciante</em>", 1082, 76, 1)}
{pill("revise as melhorias de IA da sua conta →", 1168)}
{foot("Interface e marca ilustrativas · Fontes: Search Engine Journal, 10.11.26 · The Keyword, 23.10.26")}"""
w("p1_meta", page(b, ADX + CSS))

# ============ 17/11 · Atribuição ============
REC = """<div class="rc"><b>LOJA EXEMPLO</b><i>pedido #48213 · 16.11 · 14:07</i><hr>
<p><span>1 x Garrafa 500 ml</span><span>129,90</span></p><p><span>Frete</span><span>0,00</span></p><hr>
<p class="t"><span>TOTAL</span><span>R$ 129,90</span></p><p><span>Pagamento</span><span>PIX</span></p><em>PAGO</em></div>"""
x2 = """.rc{position:absolute;width:300px;background:#fff;padding:22px 22px 34px;font-family:"MO";font-size:17px;color:#141518;filter:drop-shadow(0 18px 14px rgba(20,21,24,.4));
 clip-path:polygon(0 0,100% 0,100% calc(100% - 12px),95% 100%,90% calc(100% - 12px),85% 100%,80% calc(100% - 12px),75% 100%,70% calc(100% - 12px),65% 100%,60% calc(100% - 12px),55% 100%,50% calc(100% - 12px),45% 100%,40% calc(100% - 12px),35% 100%,30% calc(100% - 12px),25% 100%,20% calc(100% - 12px),15% 100%,10% calc(100% - 12px),5% 100%,0 calc(100% - 12px))}
.rc b{display:block;text-align:center;font-weight:500;font-size:20px;letter-spacing:.12em}.rc i{display:block;text-align:center;font-style:normal;font-size:13px;color:#6B6E73;margin:4px 0 10px}
.rc hr{border:0;border-top:1.500px dashed #9A9DA2;margin:10px 0}.rc p{display:flex;justify-content:space-between;margin:5px 0}.rc p.t{font-weight:500;font-size:21px}
.rc em{display:inline-block;margin-top:12px;font-style:normal;font-weight:500;letter-spacing:.16em;color:#23764A;border:2px solid #23764A;border-radius:4px;padding:2px 10px;transform:rotate(-5deg)}
.pl{font-family:"MO";font-size:15px;letter-spacing:.08em;text-transform:uppercase;color:#6B6E73;display:block;margin-bottom:4px}"""
def painel(nome, tipo, quando): return f'<div style="flex:1"><span class="pl">{nome}</span><b>{tipo}</b><small>{quando}</small></div><div class="n">1</div>'
b = f"""{org(470)}{chip("Mensuração · atribuição")}{logo()}
{big("Uma<br>venda.", 150, 200)}{sub("Dois painéis dizendo que é deles.", 520)}{av(800, 230, 190, -5)}
{card(painel("Google Ads", "conversão", "clique · 3 dias antes"), 60, 630, -4, 430)}
{card(painel("Meta Ads", "resultado", "visualização · 1 dia antes"), 150, 760, 3, 450)}
<div class="ab" style="left:700px;top:640px;transform:rotate(5deg)">{REC}</div>
{tag("painéis: <s>2 vendas</s>", "w", 66, 902, -3, 36)}{tag("caixa: 1 venda", "k", 420, 930, 2, 36)}
{blk("divida a verba pelo", 1030, 60, -1.5)}{blk("custo por <em>venda real</em>", 1108, 76, 1)}
{pill("compare os painéis com o caixa toda semana →", 1194, 66, -2, 36)}
{foot("Exemplo ilustrativo")}"""
w("p2_atribuicao", page(b, CSS + x2))

# ============ 20/11 · Black Friday ============
CHAT = """<div class="ch"><div class="chh"><span></span>Assistente de IA</div>
<div class="bu">garrafa térmica Aura 500 ml: onde está mais barato hoje?</div>
<div class="ba">Encontrei 3 ofertas para esse modelo:
 <div class="of"><b>Loja A</b><span>R$ 119,90</span><i>frete grátis · 4,8</i></div>
 <div class="of"><b>Loja B</b><span>R$ 124,00</span><i>entrega amanhã · 4,6</i></div>
 <div class="of"><b>Loja C</b><span>R$ 129,90</span><i>loja oficial · 4,9</i></div>
 O preço mais baixo dos últimos 30 dias foi R$ 117,00.</div>
<div class="in">Pergunte sobre preço, loja ou prazo</div></div>"""
x5 = """.ch{padding:8px 10px;display:flex;flex-direction:column;gap:8px;height:calc(100% - 40px);background:#fff;font-size:11px;line-height:1.35}
.chh{display:flex;align-items:center;gap:7px;font-weight:600;font-size:12px;padding:2px 2px 8px;border-bottom:1px solid #ECEEF1}.chh span{width:20px;height:20px;border-radius:6px;background:#141518}
.bu{align-self:flex-end;max-width:82%;background:#141518;color:#fff;border-radius:14px 14px 4px 14px;padding:8px 10px}
.ba{background:#F1F2F4;border-radius:14px 14px 14px 4px;padding:9px 10px}
.of{display:grid;grid-template-columns:1fr auto;background:#fff;border-radius:8px;padding:6px 8px;margin:6px 0}.of b{font-weight:600}.of span{font-weight:600}.of i{grid-column:1/3;font-style:normal;font-size:9.500px;color:#737A85}
.in{margin-top:auto;border:1px solid #D9DDE3;border-radius:16px;padding:8px 12px;color:#8B929C;font-size:10.500px}"""
b = f"""{org(470)}{chip("Black Friday 2026 · dados")}{logo()}
{big("Black<br>Friday", 150, 190)}{sub("premia a marca que já é conhecida.", 496, 46)}{av(820, 210, 180)}
{tag("+13 p.p. recompra de marcas conhecidas", "o", 62, 590, -3, 27)}
{tag("−8 p.p. marcas desconhecidas", "w", 90, 664, 2, 27)}
{card('<div class="n">86%</div><div><b>vão pesquisar com IA</b><small>antes de comprar</small></div>', 60, 766, -3, 440)}
{card('<div class="n">56%</div><div><b>pesquisam preço</b><small>com mais de 30 dias</small></div>', 120, 892, 2.5, 420)}
{phone(CHAT, 730, 640, 6, 1.100)}
{blk("a decisão acontece", 1040, 60, -1.5)}{blk("antes do <em>clique no anúncio</em>", 1118, 76, 1, 46)}
{pill("quem não é lembrado paga mais caro →", 1202, 66, -2, 36)}
{foot("Tela ilustrativa · Fonte: pesquisa Stefanini Marketing, via Brasil Inovador, 28.10.26")}"""
w("p5_blackfriday", page(b, CSS + x5))

# ============ Carrosséis ============
xc = """.wrap{position:absolute;left:60px;right:60px;top:404px}.wrap .st{position:static;font-size:106px}.wrap .sb{position:static;margin-top:34px;padding-right:40px;font-size:47px}
.look{padding:30px 34px;bottom:130px}.look small{font-size:19px;margin-bottom:10px}.look b{font-size:38px}
.rcp{position:absolute;left:60px;right:60px;background:#fff;border-radius:24px;padding:10px 28px;box-shadow:0 22px 26px -14px rgba(20,21,24,.5);transform:rotate(-1deg)}
.rcp div{display:grid;grid-template-columns:64px 1fr;padding:15px 0;border-bottom:1.500px solid #ECEAE5;font-weight:600;font-size:32px;letter-spacing:-.02em}.rcp div:last-child{border:0}.rcp span{font-family:"MO";font-weight:500;color:#F6490D;font-size:24px;padding-top:5px}
.bars{position:absolute;left:60px;right:60px;top:560px;background:#fff;border-radius:26px;padding:70px 40px 26px;box-shadow:0 22px 26px -14px rgba(20,21,24,.45);transform:rotate(-1deg)}
.gb{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;align-items:end;height:340px;border-bottom:2px solid #141518}
.gb .g{display:flex;gap:12px;align-items:flex-end;justify-content:center;height:100%}.gb .b{width:84px;border-radius:8px 8px 0 0;position:relative}
.gb .b span{position:absolute;top:-38px;left:0;right:0;text-align:center;font-weight:700;font-size:28px}.gb .a{background:#C9C6BE}.gb .d{background:#F6490D}
.gl{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;padding-top:14px;font-weight:700;font-size:30px;text-align:center}
.lgd{display:flex;gap:26px;margin-top:20px;font-family:"MO";font-size:16px}.lgd i{display:inline-block;width:14px;height:14px;border-radius:3px;margin-right:8px;vertical-align:-2px}"""

def step(name, i, n, title, text, lk, lv, total):
    return page(f"""{chip(name)}{logo()}<div class="num">{i}</div>
<div class="wrap"><div class="st">{title}</div><div class="sb">{text}</div></div>
<div class="look"><small>{lk}</small><b>{lv}</b></div>{dots(i + 1, total)}<div class="nx">arrasta →</div>""", xc)

# ---- 18/11 · 30 minutos ----
N1 = "Auditoria · 30 minutos"
s30 = [("Rastreio contra caixa", "Se as conversões da plataforma não batem com as vendas, nenhuma otimização feita depois se sustenta.", "Conversões da plataforma × vendas no CRM, no mesmo período"),
 ("Termos de pesquisa", "No Google Ads, é ali que aparece a verba indo para buscas que nunca vão comprar.", "Termos com custo e sem conversão, ordenados por gasto"),
 ("Marca × aquisição", "Campanha de marca com CPA baixo costuma esconder uma aquisição cara.", "CPA da busca de marca separado do resto da conta"),
 ("Criativos ativos", "Conta com um ou dois criativos rodando há meses está pagando pela fadiga.", "Quantos criativos entregam, com frequência e CTR no tempo"),
 ("Tempo de resposta ao lead", "Lead que espera um dia por retorno esfria, e a mídia leva a culpa.", "Tempo entre a entrada do lead e o primeiro contato")]
b = f"""{org(560)}{chip(N1)}{logo()}
{big("Os primeiros", 150, 118)}{big("30 minutos", 262, 150, OR)}{sub("numa conta que eu não conheço.", 420)}{av(830, 500, 190, 6)}
{sub("A ordem que sigo para saber se o problema é de mídia, de rastreio ou de atendimento.", 520, 34).replace('class="sub" style="', 'class="sub" style="right:300px;font-weight:500;')}
{tag("01 rastreio", "w", 62, 830, -4, 36)}{tag("02 termos de pesquisa", "k", 330, 850, 3, 36)}
{tag("03 marca × aquisição", "k", 80, 940, 2, 36)}{tag("04 criativos", "w", 560, 950, -3, 36)}
{tag("05 tempo de resposta", "w", 150, 1034, -2, 36)}
{pill("arrasta para ver a ordem →", 1150)}{dots(1, 7)}"""
w("c30_01", page(b, xc))
for k, (t, x, lv) in enumerate(s30, 1): w(f"c30_{k+1:02d}", step(N1, k, 5, t, x, "O que eu olho", lv, 7))
b = f"""{chip(N1)}{logo()}{av(60, 150, 200, -5)}
{blk("se o item 1 falha,", 390, 60, -1.5, 66)}{blk("eu <em>paro ali</em> e corrijo", 480, 76, 1, 66)}{blk("antes de mexer em campanha.", 570, 60, -1, 58)}
<div class="rcp" style="top:700px">{''.join(f'<div><span>{k:02d}</span>{t}</div>' for k, (t, _, _) in enumerate(s30, 1))}</div>
{pill("qual desses você confere primeiro?", 1180)}{dots(7, 7)}"""
w("c30_07", page(b, xc, "fr o"))

# ---- 19/11 · 6 checagens (Ignite) ----
N2 = "Escala de verba · checklist"
ch = [("O rastreio bate com o caixa", "Escalar em cima de conversão errada multiplica o erro junto com a verba.", "Vendas do CRM e conversões da plataforma, no mesmo período"),
 ("Custo por venda estável há 2 semanas", "Escalar no pico de uma oscilação é comprar a média mais cara.", "Variação semanal do custo por venda"),
 ("Campanha fora do aprendizado", "Mudança grande de orçamento devolve a campanha à fase de aprendizado.", "Status de aprendizado de cada campanha e conjunto"),
 ("Pelo menos 3 criativos ativos", "Com mais verba, a frequência sobe e um criativo só cansa rápido.", "Criativos com entrega e sem queda forte de CTR"),
 ("O atendimento aguenta o dobro", "Se o comercial não dá conta, o lead extra vira custo, não venda.", "Tempo de resposta e capacidade do time comercial"),
 ("Aumento em degraus de 20% a 30%", "Degraus menores deixam a conta absorver o aumento sem perder eficiência.", "Novo orçamento e data do próximo degrau")]
b = f"""{org(520)}{chip(N2)}{logo()}
{big("Antes de<br>escalar", 150, 160)}{sub("a verba, confira seis pontos.", 446)}{av(800, 560, 190, 6)}
<div class="num" style="left:800px;top:296px;width:220px;height:220px;font-size:170px;transform:rotate(8deg)">6</div>
{sub("Dobrar o investimento não dobra a venda quando a conta tem um gargalo.", 570, 36).replace('class="sub" style="', 'class="sub" style="right:330px;')}
{tag("rastreio", "w", 62, 870, -4, 36)}{tag("custo estável", "k", 290, 884, 3, 36)}{tag("aprendizado", "w", 600, 872, -2, 36)}
{tag("3 criativos", "k", 90, 968, 2, 36)}{tag("atendimento", "w", 360, 978, -3, 36)}{tag("degraus de 20–30%", "k", 640, 968, 2, 36)}
{pill("arrasta para ver cada uma →", 1150)}{dots(1, 9)}"""
w("c6_01", page(b, xc))
for k, (t, x, lv) in enumerate(ch, 1): w(f"c6_{k+1:02d}", step(N2, k, 6, t, x, "O que confirmar", lv, 9))
b = f"""{chip(N2)}{logo()}
{big("Sem a<br>checagem 5", 150, 130)}{sub("verba e leads dobram. As vendas quase não mudam.", 400, 44).replace('class="sub" style="', 'class="sub" style="right:90px;')}
<div class="bars"><div class="gb">
 <div class="g"><div class="b a" style="height:150px"><span>100</span></div><div class="b d" style="height:300px"><span>200</span></div></div>
 <div class="g"><div class="b a" style="height:150px"><span>100</span></div><div class="b d" style="height:300px"><span>200</span></div></div>
 <div class="g"><div class="b a" style="height:150px"><span>100</span></div><div class="b d" style="height:165px"><span>110</span></div></div></div>
 <div class="gl"><div>Verba</div><div>Leads</div><div>Vendas</div></div>
 <div class="lgd"><span><i style="background:#C9C6BE"></i>antes</span><span><i style="background:#F6490D"></i>depois do aumento</span><span style="margin-left:auto">índice · exemplo ilustrativo</span></div></div>
{dots(8, 9)}<div class="nx">arrasta →</div>"""
w("c6_08", page(b, xc))
b = f"""{chip(N2)}{logo()}{av(60, 150, 200, -5)}
{blk("na Ignite, essa checagem", 400, 60, -1.5, 62)}{blk("vem <em>antes</em> de cada", 486, 76, 1, 62)}{blk("aumento de orçamento.", 572, 60, -1, 62)}
{sub("Quer ver como ela fica na sua conta?", 720, 46)}
{tag("comente RAIO-X", "k", 62, 830, -3, 104)}
{pill("eu te chamo por mensagem →", 1060, 66, -2, 48)}{dots(9, 9)}"""
w("c6_09", page(b, xc, "fr o"))

# ============ Capa do artigo (1920x1080) ============
xa = """.pn{position:absolute;right:110px;top:250px;width:760px;background:#fff;border-radius:28px;padding:30px 34px;transform:rotate(2deg);box-shadow:0 30px 36px -18px rgba(20,21,24,.55)}
.pn .hd{display:flex;justify-content:space-between;font-family:"MO";font-size:17px;letter-spacing:.1em;text-transform:uppercase;color:#6B6E73}
.pn .lg{display:flex;gap:26px;margin-top:10px;font-weight:600;font-size:22px}.pn .lg i{display:inline-block;width:24px;height:5px;border-radius:3px;margin-right:10px;vertical-align:6px}"""
b = f"""<div class="org" style="left:1180px;top:0;height:auto"></div>{chip("Artigo · marca e performance")}
<div class="logo" style="right:60px">{'<span>' + RAIO.format(c=OR) + '</span>'}IGNIT AGENCY</div>
{big("Performance<br>sem marca", 210, 130)}{tag("tem prazo de validade", "o", 62, 500, -3, 70)}
{sub("O que acontece com o custo por venda quando a busca pelo nome da empresa começa a cair.", 700, 42).replace('class="sub" style="', 'class="sub" style="width:900px;')}{av(880, 800, 200, 6)}
<div class="pn"><div class="hd"><span>Busca de marca × custo por venda</span><span>ilustrativo</span></div>
<svg width="692" height="380" viewBox="0 0 692 380" fill="none" style="display:block;margin-top:18px"><g stroke="#ECEAE5" stroke-width="1.5"><line x1="0" x2="692" y1="40" y2="40"/><line x1="0" x2="692" y1="140" y2="140"/><line x1="0" x2="692" y1="240" y2="240"/><line x1="0" x2="692" y1="340" y2="340"/></g>
<line x1="230" x2="230" y1="16" y2="350" stroke="#141518" stroke-width="1.5" stroke-dasharray="5 7"/><text x="242" y="30" fill="#141518" font-family="MO" font-size="16">corte da verba de marca</text>
<path d="M0 80 C120 78 200 82 230 84 C320 92 420 150 520 200 C590 236 650 252 692 262" stroke="#141518" stroke-width="5" stroke-linecap="round"/>
<path d="M0 300 C120 302 200 298 230 296 C330 290 420 250 520 200 C590 166 650 140 692 120" stroke="#F6490D" stroke-width="5" stroke-linecap="round"/></svg>
<div class="lg"><span><i style="background:#141518"></i>busca pela marca</span><span><i style="background:#F6490D"></i>custo por venda</span></div></div>"""
w("art_capa", page(b, xa, "fr wide"))
print("ok")
