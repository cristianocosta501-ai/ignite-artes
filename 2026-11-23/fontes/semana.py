"""Peças da semana 23 a 27/11/2026 · LinkedIn pessoal do Cristiano (linguagem 'criador').
Uso: python3 semana.py  (gera html/ ao lado; render feito por build.sh)"""
import sys, os, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "sistema"))
from criador import *

AV = (ROOT / "avatar" / "avatar.png").as_uri()
OUT = pathlib.Path(__file__).resolve().parent / "html"; OUT.mkdir(exist_ok=True)
def w(n, h): (OUT / f"{n}.html").write_text(h)
def av(x, y, s=170, rot=6): return f'<img class="ab" src="{AV}" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;transform:rotate({rot}deg);filter:drop-shadow(0 14px 12px rgba(20,21,24,.35))">'
def big(t, top, size, color=INK, left=60): return f'<div class="big" style="top:{top}px;left:{left}px;font-size:{size}px;color:{color}">{t}</div>'
def sub(t, top, size=54, extra=""): return f'<div class="sub" style="top:{top}px;font-size:{size}px;{extra}">{t}</div>'
def org(h): return f'<div class="org" style="height:{h}px"></div>'
def card(html, x, y, rot, wd): return f'<div class="tc" style="left:{x}px;top:{y}px;width:{wd}px;transform:rotate({rot}deg)">{html}</div>'
def ab(html, x, y, rot=0, scale=1): return f'<div class="ab" style="left:{x}px;top:{y}px;transform:rotate({rot}deg) scale({scale})">{html}</div>'

X = """
.pn{background:#fff;border-radius:24px;padding:22px 26px;box-shadow:0 2px 0 rgba(20,21,24,.08),0 26px 30px -16px rgba(20,21,24,.5);font-family:"IT";color:#141518}
.pn .hd{display:flex;justify-content:space-between;align-items:center;font-family:"MO";font-size:15px;letter-spacing:.09em;text-transform:uppercase;color:#6B6E73;margin-bottom:14px}
.mono{font-family:"MO"}
/* barras */
.bc{display:flex;gap:34px;align-items:flex-end;height:260px;border-bottom:2px solid #141518;padding:0 10px}
.bc .g{flex:1;display:flex;gap:10px;align-items:flex-end;justify-content:center;height:100%}
.bc .b{width:74px;border-radius:8px 8px 0 0;position:relative}.bc .b span{position:absolute;top:-36px;left:-20px;right:-20px;text-align:center;font-family:"ID";font-weight:700;font-size:28px}
.bc .a{background:#C9C6BE}.bc .d{background:#D9480F}.bc .k{background:#141518}
.bl{display:flex;gap:34px;padding:12px 10px 0}.bl div{flex:1;text-align:center;font-family:"ID";font-weight:600;font-size:24px}
.lg{display:flex;gap:22px;margin-top:14px;font-family:"MO";font-size:14px;color:#55585D}.lg i{display:inline-block;width:13px;height:13px;border-radius:3px;margin-right:7px;vertical-align:-1px}
/* semana */
.wk{display:grid;grid-template-columns:repeat(7,1fr);gap:10px;align-items:end;height:250px}
.wk div{border-radius:10px 10px 4px 4px;background:#E7E4DD;position:relative}
.wk div.on{background:#D9480F}
.wk div span{position:absolute;bottom:-34px;left:0;right:0;text-align:center;font-family:"MO";font-size:15px;color:#55585D}
/* telas */
.sc{height:calc(100% - 40px);background:#fff;display:flex;flex-direction:column;font-size:11px;line-height:1.3}
.sch{padding:8px 12px;font-weight:600;font-size:13px;border-bottom:1px solid #ECEEF1;display:flex;align-items:center;gap:8px}
.sch i{width:22px;height:22px;border-radius:7px;background:#141518;display:inline-block}
.nt{margin:7px 9px 0;background:#F1F2F4;border-radius:12px;padding:8px 10px}
.nt b{display:block;font-weight:600;font-size:11.5px}.nt span{color:#6B7280;font-size:10px}
.nt em{font-style:normal;color:#C2410C;font-weight:600}
.rep{padding:12px}.rep .sc1{display:flex;align-items:center;gap:10px;margin:6px 0 10px}
.rep .nb{font-family:"ID";font-weight:700;font-size:40px;letter-spacing:-.03em}
.rep .st{height:8px;border-radius:4px;background:#ECEEF1;margin:6px 0 2px;position:relative;overflow:hidden}.rep .st i{position:absolute;left:0;top:0;bottom:0;background:#23764A;border-radius:4px}
.rep .rw{display:flex;justify-content:space-between;font-size:10.5px;color:#4B5563;margin-top:8px}
.rep .rc{margin-top:10px;border:1px solid #ECEEF1;border-radius:10px;padding:8px}.rep .rc b{font-size:11px}.rep .rc p{color:#6B7280;font-size:10px;margin-top:3px}
.rep .ok{display:inline-block;margin-top:5px;font-size:9.5px;font-weight:600;color:#23764A;background:#E7F4EC;border-radius:6px;padding:2px 6px}
/* lista de checagem */
.ck>div:not(.hd){display:grid;grid-template-columns:44px 1fr;align-items:center;padding:12px 0;border-bottom:1.5px solid #ECEAE5;font-family:"ID";font-weight:600;font-size:28px;letter-spacing:-.02em}
.ck>div:last-child{border:0}.ck>div:not(.hd)>span{width:32px;height:32px;border-radius:8px;border:2.5px solid #141518;display:grid;place-items:center;font-size:20px}
.ck>div:not(.hd)>span.y{background:#D9480F;border-color:#D9480F;color:#fff}
/* url */
.url{display:flex;align-items:center;gap:10px;background:#F1F2F4;border-radius:12px;padding:12px 16px;font-family:"MO";font-size:19px;color:#141518;white-space:nowrap}
.url i{width:12px;height:12px;border-radius:50%;background:#23764A}.url b{color:#D9480F;font-weight:500}
.tb{width:100%;border-collapse:collapse;margin-top:14px;font-family:"IT";font-size:20px}
.tb th{font-family:"MO";font-weight:400;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:#6B6E73;text-align:left;padding:8px 6px;border-bottom:1.5px solid #ECEAE5}
.tb td{padding:11px 6px;border-bottom:1.5px solid #F1EFEA}.tb tr:last-child td{border:0}
.mt{display:inline-block;font-family:"MO";font-size:16px;font-weight:500;padding:3px 10px;border-radius:6px;background:#141518;color:#fff}
.mt.a{background:#D9480F}
/* painel */
.kp{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.kp div{background:#F6F5F2;border-radius:16px;padding:14px 16px}
.kp small{display:block;font-family:"MO";font-size:12.5px;letter-spacing:.07em;text-transform:uppercase;color:#6B6E73}
.kp b{display:block;font-family:"ID";font-weight:700;font-size:40px;letter-spacing:-.03em;margin-top:4px}
.kp em{font-style:normal;font-family:"MO";font-size:14px}.up{color:#23764A}.dn{color:#B42318}
.kp div.w{grid-column:1/3;display:flex;justify-content:space-between;align-items:center}
.kp .q{font-family:"HW";font-size:28px;color:#D9480F;display:block;margin-top:2px}
/* conversa */
.cv{margin:6px 9px 0;display:flex;gap:8px;align-items:center;padding:7px 4px;border-bottom:1px solid #F1F2F4}
.cv i{width:30px;height:30px;border-radius:50%;background:#D1D5DB;flex:none}.cv b{display:block;font-size:11px}.cv span{color:#6B7280;font-size:9.5px}
.cv u{margin-left:auto;text-decoration:none;background:#23764A;color:#fff;border-radius:9px;font-size:9px;font-weight:700;padding:1px 6px}
/* crm */
.crm td:last-child{font-family:"MO";color:#9A9DA2}
/* fluxo */
.fl{display:flex;align-items:center;gap:14px}
.fl .bx{background:#fff;border-radius:20px;padding:18px 20px;box-shadow:0 22px 26px -14px rgba(20,21,24,.45);font-family:"ID";font-weight:700;font-size:30px;letter-spacing:-.02em;text-align:center;min-width:200px}
.fl .bx small{display:block;font-family:"MO";font-weight:400;font-size:13px;letter-spacing:.08em;color:#6B6E73;text-transform:uppercase;margin-top:4px}
.fl .ar{font-family:"HW";font-size:56px;color:#141518}
.big2{position:absolute;left:60px;right:60px;font-weight:700;line-height:.88;letter-spacing:-.045em;text-transform:uppercase}
"""
def P(body, extra="", cls="fr"): return page(body, X + extra, cls)

# =================== 23/11 · Carrossel Black Friday (notícia) ===================
NB = "Black Friday 2026 · dados"; TB = 8
FB = "Fonte: pesquisa Reclame Aqui, via Mercado &amp; Consumo, 18.11.26 · telas ilustrativas"
def phone_(inner, x, y, rot, sc): return ab(f'<div class="ph" style="position:relative"><div class="ps"><div class="pst"><b>9:41</b><span class="pisl"></span><span class="pic"><i></i><i></i><i></i><i></i><u></u></span></div>{inner}</div></div>', x, y, rot, sc)
def nxt(): return '<div class="nx">arrasta →</div>'
REP = """<div class="sc"><div class="sch"><i></i>Reputação de lojas</div><div class="rep">
<span style="font-size:10px;color:#6B7280">LOJA EXEMPLO · ilustrativo</span>
<div class="sc1"><div class="nb">8,1</div><div style="font-size:10.5px;color:#4B5563">nota geral<br><b style="color:#23764A">recomendada</b></div></div>
<div class="rw"><span>reclamações respondidas</span><b>96%</b></div><div class="st"><i style="width:96%"></i></div>
<div class="rw"><span>voltaria a fazer negócio</span><b>78%</b></div><div class="st"><i style="width:78%"></i></div>
<div class="rw"><span>prazo médio de resposta</span><b>2 dias</b></div>
<div class="rc"><b>Pedido chegou depois do prazo</b><p>Comprei na promoção e a entrega atrasou 5 dias...</p><span class="ok">resolvido</span></div>
<div class="rc"><b>Cupom não aplicado no carrinho</b><p>O desconto da página não apareceu no...</p><span class="ok">resolvido</span></div></div></div>"""
ALERT = """<div class="sc" style="background:#F3F4F6"><div style="padding:16px 14px 6px;font-family:'ID';font-weight:600;font-size:30px;letter-spacing:-.02em">9:41</div>
<div style="padding:0 14px 8px;font-size:10px;color:#6B7280">segunda-feira, 23 de novembro</div>
<div class="nt"><span>LOJA A · agora</span><b>Fone sem fio caiu para R$ 189</b><span>era R$ 229 · <em>−17%</em></span></div>
<div class="nt"><span>ALERTA DE PREÇO · 12 min</span><b>TV 50" no menor preço em 30 dias</b><span>R$ 2.149 em 3 lojas</span></div>
<div class="nt"><span>LOJA B · 1 h</span><b>Frete grátis só até quarta</b><span>esquenta Black Friday</span></div>
<div class="nt"><span>LOJA C · ontem</span><b>Você deixou 2 itens no carrinho</b><span>cupom de 10% guardado</span></div>
<div class="nt"><span>ALERTA DE PREÇO · ontem</span><b>Air fryer: preço subiu R$ 40</b><span>acompanhando há 18 dias</span></div></div>"""

b = f"""{org(450)}{chip(NB)}{logo()}
{big("Metade", 150, 210)}{big("ainda não<br>decidiu", 330, 132, OR)}{av(850, 390, 170, 6)}
{sub("a uma semana da Black Friday.", 600, 46)}
{tag("indecisos: 51,6%", "k", 62, 690, -3, 38)}{tag("decididos: 32,3%", "w", 100, 776, 2, 38)}
{card('<div class="n">17,4%</div><div><b>vão concentrar as compras na sexta</b></div>', 60, 880, -3, 470)}
{ab(f'<div class="ph" style="position:relative">{"" }<div class="ps"><div class="pst"><b>9:41</b><span class="pisl"></span><span class="pic"><i></i><i></i><i></i><i></i><u></u></span></div>{ALERT}</div></div>', 690, 600, 6, 1.12)}
{blk("a verba desta semana", 1040, 60, -1.5)}{blk("rende <em>antes</em> da sexta", 1118, 76, 1)}
{pill("arrasta para ver os números →", 1204, 66, -2, 36)}{dots(1, TB)}"""
w("cbf_01", P(b))

b = f"""{chip(NB)}{logo()}
{big("Agosto ×<br>novembro", 150, 132)}{sub("Quem já decidiu comprar quase dobrou.", 400, 42)}
{ab('''<div class="pn" style="width:900px"><div class="hd"><span>Intenção de compra na Black Friday</span><span>% dos entrevistados</span></div>
<div class="bc" style="height:300px"><div class="g"><div class="b a" style="height:57px"><span>19%</span></div><div class="b d" style="height:97px"><span>32,3%</span></div></div>
<div class="g"><div class="b a" style="height:183px"><span>61%</span></div><div class="b k" style="height:155px"><span>51,6%</span></div></div></div>
<div class="bl"><div>decididos a comprar</div><div>indecisos</div></div>
<div class="lg"><span><i style="background:#C9C6BE"></i>agosto</span><span><i style="background:#D9480F"></i>novembro</span></div></div>''', 60, 500, -1.5)}
{tag("+13,3 p.p.", "o", 760, 190, -4, 40)}{tag("−9,4 p.p.", "k", 800, 290, 3, 40)}
{blk("metade ainda está", 1010, 60, -1.5)}{blk("<em>comparando</em> preço", 1088, 76, 1)}
{pill("e compara ao longo do mês →", 1176, 66, -2, 36)}{dots(2, TB)}{nxt()}"""
w("cbf_02", P(b))

b = f"""{chip(NB)}{logo()}
{big("Só 17,4%", 150, 160, OR)}{big("deixam para<br>a sexta", 300, 116)}
{sub("A maioria espalha as compras pelo mês.", 540, 40)}
{ab('''<div class="pn" style="width:900px;padding-bottom:50px"><div class="hd"><span>Semana da Black Friday · onde cai a verba</span><span>ilustrativo</span></div>
<div class="wk"><div style="height:42%"><span>seg</span></div><div style="height:46%"><span>ter</span></div><div style="height:50%"><span>qua</span></div><div style="height:58%"><span>qui</span></div><div class="on" style="height:100%"><span>sex</span></div><div style="height:48%"><span>sáb</span></div><div style="height:30%"><span>dom</span></div></div></div>''', 60, 620, 1.5)}
{tag("tudo na sexta?", "k", 640, 440, -4, 38)}
{blk("verba toda no pico", 1040, 60, -1.5)}{blk("é verba no <em>CPM mais caro</em>", 1118, 76, 1, 50)}
{pill("distribua pelos dias →", 1204, 66, -2, 36)}{dots(3, TB)}{nxt()}"""
w("cbf_03", P(b))

b = f"""{org(430)}{chip(NB)}{logo()}
{big("48,1%", 150, 200)}{big("sem orçamento", 340, 100, OR)}{big("definido", 452, 100, OR)}
{sub("Vão acompanhar as ofertas ao longo de novembro.", 576, 38, "right:380px")}
{ab(f'<div class="ph" style="position:relative"><div class="ps"><div class="pst"><b>9:41</b><span class="pisl"></span><span class="pic"><i></i><i></i><i></i><i></i><u></u></span></div>{ALERT}</div></div>', 712, 640, 5, 1.1)}
{card('<div><b>Alerta de preço ligado</b><small>quem compara, volta</small></div><u></u>', 60, 700, -3, 400)}
{card('<div><b>Carrinho salvo</b><small>esperando o desconto</small></div><u></u>', 110, 820, 3, 380)}
{blk("quem compara", 1040, 60, -1.5)}{blk("volta pelo <em>remarketing</em>", 1118, 76, 1)}
{pill("proteja essa verba primeiro →", 1204, 66, -2, 36)}{dots(4, TB)}{nxt()}"""
w("cbf_04", P(b))

b = f"""{chip(NB)}{logo()}
{big("76,1%", 150, 200, OR)}{big("vão checar a", 340, 110)}{big("reputação", 446, 110)}
{sub("Antes de comprar, consultam o Reclame Aqui.", 590, 38, "right:400px")}
{ab(f'<div class="ph" style="position:relative"><div class="ps"><div class="pst"><b>9:41</b><span class="pisl"></span><span class="pic"><i></i><i></i><i></i><i></i><u></u></span></div>{REP}</div></div>', 712, 650, -5, 1.1)}
{tag("o clique no anúncio", "w", 62, 700, -3, 36)}{tag("passa por aqui", "k", 150, 784, 2, 36)}
{card('<div class="n">0</div><div><b>lance que compense nota ruim</b><small>na hora da decisão</small></div>', 60, 880, -2.5, 520)}
{blk("reputação também", 1040, 60, -1.5)}{blk("<em>converte</em> anúncio", 1118, 76, 1)}
{pill("confira antes de subir o lance →", 1204, 66, -2, 36)}{dots(5, TB)}{nxt()}"""
w("cbf_05", P(b))

AUD = """<div class="sc"><div class="sch"><i></i>Públicos · semana 48</div>""" + "".join(
    f'<div class="cv"><div><b>{n}</b><span>{m}</span></div><u style="background:{c}">{k}</u></div>' for n, m, k, c in [
     ("Visitou o produto · 30 dias", "remarketing", "+ verba", "#23764A"), ("Carrinho abandonado", "remarketing", "+ verba", "#23764A"),
     ("Clientes da base", "e-mail e lista", "manter", "#23764A"), ("Interesse amplo A", "frio · sem venda em out.", "pausar", "#B42318"),
     ("Interesse amplo B", "frio · sem venda em out.", "pausar", "#B42318"), ("Semelhante 5%", "frio · 2 vendas", "manter", "#6B7280")]) + "</div>"
def ckl(items, wd=600): return f'<div class="pn ck" style="width:{wd}px;padding:14px 30px"><div class="hd" style="margin:8px 0 0"><span>O que eu faria com a verba desta semana</span><span>1 de 2</span></div>' + "".join(f'<div><span class="{c}">{m}</span>{t}</div>' for c, m, t in items) + '</div>'
b = f"""{chip(NB)}{logo()}
{big("O que eu<br>faria", 150, 160)}{sub("com a verba desta semana.", 445, 46)}
{ab(ckl([("y","1","Proteger o remarketing de quem visitou"),("y","2","Cortar o frio sem venda em outubro"),("","3","Espalhar a verba pela semana"),("","4","Conferir a reputação")]).replace("1 de 2","passos 1 e 2"), 50, 580, -2)}
{phone_(AUD, 730, 560, 5, 1.1)}
{tag("01 remarketing", "o", 62, 516, -3, 34)}
{blk("CPM de outubro já", 1040, 60, -1.5)}{blk("<em>testou</em> esse público", 1118, 76, 1)}
{pill("o que não vendeu barato não vende caro →", 1204, 66, -2, 34)}{dots(6, TB)}{nxt()}"""
w("cbf_06", P(b))

b = f"""{org(470)}{chip(NB)}{logo()}
{big("E mais<br>dois passos", 150, 150)}{sub("para a verba render antes da sexta.", 440, 44)}
{ab(ckl([("y","✓","Proteger o remarketing"),("y","✓","Cortar o frio sem venda"),("y","3","Espalhar a verba de seg a dom"),("y","4","Ver a nota antes do lance")], 560).replace("1 de 2","passos 3 e 4"), 50, 560, 1.5)}
{ab('''<div class="pn" style="width:400px;padding-bottom:46px"><div class="hd"><span>Verba por dia</span><span>ilustr.</span></div><div class="wk" style="height:200px"><div class="on" style="height:62%"><span>seg</span></div><div class="on" style="height:66%"><span>ter</span></div><div class="on" style="height:70%"><span>qua</span></div><div class="on" style="height:80%"><span>qui</span></div><div class="on" style="height:100%"><span>sex</span></div><div class="on" style="height:72%"><span>sáb</span></div><div class="on" style="height:50%"><span>dom</span></div></div></div>''', 640, 610, -4)}
{tag("03 distribuir", "k", 640, 520, -3, 34)}{tag("04 reputação", "w", 62, 486, 3, 34)}
{blk("a sexta é só", 1040, 60, -1.5)}{blk("<em>um</em> dos dias", 1118, 76, 1)}
{pill("e o atendimento precisa aguentar o pico →", 1204, 66, -2, 34)}{dots(7, TB)}{nxt()}"""
w("cbf_07", P(b))

b = f"""{chip(NB)}{logo()}{av(60, 150, 200, -5)}
{blk("na sua conta,", 400, 60, -1.5, 66)}{blk("a verba está toda", 490, 76, 1, 66)}{blk("<em>na sexta</em> ou espalhada?", 580, 60, -1, 62)}
{card('<div class="n">A</div><div><b>concentrada na sexta</b></div>', 60, 730, -3, 440)}
{card('<div class="n">B</div><div><b>espalhada pela semana</b></div>', 540, 760, 3, 460)}
{pill("me conta nos comentários →", 940, 66, -2, 44)}
<div class="foot" style="bottom:90px">{FB}</div>{dots(8, TB)}"""
w("cbf_08", P(b, "", "fr o"))

# =================== 24/11 · AI Max exata (notícia) ===================
b = f"""{org(470)}{chip("Google Ads · AI Max")}{logo()}
{big("Exata?", 150, 210)}{sub("Quase 29% das impressões de exata vinham do AI Max.", 360, 44, "right:330px")}{av(830, 190, 180, 6)}
{tag("palavra-chave: <s>exata</s>", "w", 62, 480, -3, 36)}{tag("{search_term_matchtype}", "k", 470, 500, 3, 32)}
{ab('''<div class="pn" style="width:960px"><div class="hd"><span>URL do clique · exemplo ilustrativo</span><span>Loja Exemplo</span></div>
<div class="url"><i></i><span>lojaexemplo.com/garrafa?mt=<b>e</b>&amp;stmt=<b>a</b></span></div>
<table class="tb"><tr><th>termo de pesquisa</th><th>palavra-chave</th><th>{matchtype}</th><th>{search_term…}</th></tr>
<tr><td>garrafa térmica 500 ml</td><td>[garrafa térmica]</td><td><span class="mt">e</span></td><td><span class="mt">e</span></td></tr>
<tr><td>presente para corredor</td><td>[garrafa térmica]</td><td><span class="mt">e</span></td><td><span class="mt a">a</span></td></tr>
<tr><td>squeeze barato</td><td>[garrafa térmica]</td><td><span class="mt">e</span></td><td><span class="mt a">a</span></td></tr></table></div>''', 60, 600, -1.5)}
{blk("separe o clique de", 1040, 60, -1.5)}{blk("<em>expansão</em> antes de avaliar", 1118, 76, 1, 50)}
{pill("o parâmetro novo mostra quem é quem →", 1204, 66, -2, 34)}
{foot("Tela ilustrativa · Fontes: PPC Land, 15.11.26 · dado Smarter Ecommerce, e-commerce EMEA, jul.26 · Google Ads Help")}"""
w("p_aimax", P(b))

# =================== 25/11 · Painel (método, vídeo) ===================
PAINEL = '''<div class="pn" style="width:560px"><div class="hd"><span>Painel de segunda · semana 47</span><span>ilustrativo</span></div>
<div class="kp"><div><small>01 investimento</small><b>R$ 12,4 mil</b><em class="up">no plano</em></div>
<div><small>02 custo por venda</small><b>R$ 186</b><em class="dn">+9% semana</em></div>
<div><small>03 vendas</small><b>67</b><em class="up">+4%</em></div>
<div><small>04 lead → venda</small><b>11%</b><em class="dn">era 14%</em></div>
<div class="w"><div><small>05 frequência · CTR</small><b style="font-size:34px">3,8 · 0,9%</b></div><span class="q">hora de trocar peça?</span></div></div></div>'''
b = f"""{org(430)}{chip("Bastidor · segunda de manhã")}{logo()}
{big("5 números.", 150, 150)}{sub("Cada um responde a uma pergunta.", 300, 46)}{av(840, 280, 170, 6)}
{tag("40 métricas", "w", 62, 400, -4, 36)}{tag("<s>40</s> 5 que decidem", "k", 330, 420, 3, 36)}
{ab(PAINEL, 60, 520, -2)}
{card('<div><b>A verba saiu como planejado?</b><small>investimento</small></div>', 650, 540, 4, 370)}
{card('<div><b>O gargalo é mídia ou comercial?</b><small>lead → venda</small></div>', 640, 680, -3, 380)}
{card('<div><b>Está na hora de trocar peça?</b><small>frequência · CTR</small></div>', 660, 820, 3, 360)}
{blk("número que não muda", 1040, 60, -1.5)}{blk("decisão <em>sai do painel</em>", 1118, 76, 1)}
{pill("quais números entram no seu? →", 1204, 66, -2, 36)}
{foot("Painel e números ilustrativos")}"""
w("p_painel", P(b))

# =================== 26/11 · Carrossel CPL (experiência própria) ===================
NC = "Mensuração · CPL × venda"; TC = 8
CONV = '''<div class="sc"><div class="sch"><i></i>Conversas · hoje</div>''' + "".join(
    f'<div class="cv"><i></i><div><b>{n}</b><span>{m}</span></div><u>{k}</u></div>' for n, m, k in [
     ("Contato 1", "Quero saber da van 2022", "2"), ("Contato 2", "Ainda está disponível?", "1"), ("Contato 3", "Aceita troca?", "3"),
     ("Contato 4", "Qual o valor da entrada?", "1"), ("Contato 5", "Vi o anúncio do micro", "2"), ("Contato 6", "Faz financiamento?", "1"),
     ("Contato 7", "Tem fotos do interior?", "1"), ("Contato 8", "Posso ver amanhã?", "2"), ("Contato 9", "Qual a quilometragem?", "1")]) + "</div>"

b = f"""{org(470)}{chip(NC)}{logo()}
{big("CPL de", 150, 150)}{big("R$ 7", 270, 230, OR)}{av(830, 180, 180, 6)}
{sub("e eu não sabia quanto custava a venda.", 500, 44, "right:400px")}
{phone_(CONV, 712, 540, 6, 1.1)}
{tag("10 a 18 contatos/dia", "w", 62, 640, -3, 38)}{tag("venda: ?", "k", 120, 730, 2, 44)}
{card('<div><b>R$ 4 mil por mês</b><small>somando 2 contas</small></div>', 60, 840, -3, 380)}
{blk("contato barato é", 1040, 60, -1.5)}{blk("metade da <em>resposta</em>", 1118, 76, 1)}
{pill("arrasta para ver a outra metade →", 1204, 66, -2, 36)}{dots(1, TC)}"""
w("ccpl_01", P(b))

b = f"""{chip(NC)}{logo()}
{big("O que eu<br>tinha", 150, 150)}{sub("Na Sullato, Veículos e Vans e Micros.", 440, 40)}
{card('<div class="n">R$ 7</div><div><b>custo por lead</b><small>2 contas somadas</small></div>', 60, 540, -3, 470)}
{card('<div class="n">R$ 4 mil</div><div><b>por mês</b><small>investimento</small></div>', 90, 680, 2.5, 470)}
{card('<div class="n">10–18</div><div><b>contatos por dia</b><small>entrada de leads</small></div>', 60, 820, -2, 470)}
{phone_(CONV, 712, 520, -5, 1.08)}
{blk("para quem anuncia", 1040, 60, -1.5)}{blk("veículo, é <em>bom número</em>", 1118, 76, 1)}
{pill("mas faltava uma linha →", 1204, 66, -2, 36)}{dots(2, TC)}{nxt()}"""
w("ccpl_02", P(b))

CRM = '''<div class="pn crm" style="width:900px"><div class="hd"><span>CRM · leads da semana</span><span>ilustrativo</span></div>
<table class="tb"><tr><th>lead</th><th>origem</th><th>contato</th><th>vendeu?</th></tr>
<tr><td>Contato 1</td><td>Meta Ads</td><td>respondido</td><td>—</td></tr>
<tr><td>Contato 2</td><td>Google Ads</td><td>respondido</td><td>—</td></tr>
<tr><td>Contato 3</td><td>Meta Ads</td><td>visita marcada</td><td>—</td></tr>
<tr><td>Contato 4</td><td>Google Ads</td><td>respondido</td><td>—</td></tr></table></div>'''
b = f"""{org(430)}{chip(NC)}{logo()}
{big("O que<br>faltava", 150, 150)}{sub("O fechamento da venda não era informado.", 440, 40)}
{ab(CRM, 60, 560, -1.5)}
{tag("coluna vazia", "o", 720, 330, 4, 40)}
{blk("eu sabia o custo", 1040, 60, -1.5)}{blk("do contato. <em>não o da venda.</em>", 1118, 76, 1, 50)}
{pill("e é a venda que paga a conta →", 1204, 66, -2, 36)}{dots(3, TC)}{nxt()}"""
w("ccpl_03", P(b))

def camp(nome, cpl, taxa, cv, cls=""):
    return f'''<div class="pn" style="width:520px"><div class="hd"><span>{nome}</span><span>números redondos</span></div>
<div style="display:flex;justify-content:space-between;font-family:'ID';font-weight:600;font-size:28px;padding:10px 0;border-bottom:1.5px solid #ECEAE5"><span>CPL</span><b>{cpl}</b></div>
<div style="display:flex;justify-content:space-between;font-family:'ID';font-weight:600;font-size:28px;padding:10px 0;border-bottom:1.5px solid #ECEAE5"><span>leads por venda</span><b>{taxa}</b></div>
<div style="display:flex;justify-content:space-between;align-items:center;font-family:'ID';font-weight:700;font-size:28px;padding:14px 0 4px"><span>custo por venda</span><b style="font-size:54px;letter-spacing:-.03em;color:{cls or INK}">{cv}</b></div></div>'''
b = f"""{chip(NC)}{logo()}
{big("Campanha A", 150, 140)}{sub("Parece a melhor da conta.", 290, 46)}
{ab(camp("Campanha A", "R$ 15", "40", "R$ 600"), 60, 420, -2.5, 1.05)}
{tag("CPL baixo", "w", 650, 420, 4, 40)}
{card('<div class="n">15 × 40</div><div><b>= R$ 600 por venda</b><small>exemplo ilustrativo</small></div>', 120, 840, 2, 600)}
{blk("o algoritmo acha quem", 1040, 60, -1.5)}{blk("<em>preenche formulário</em>", 1118, 76, 1)}
{pill("e não quem compra →", 1204, 66, -2, 36)}{dots(4, TC)}{nxt()}"""
w("ccpl_04", P(b))

b = f"""{org(470)}{chip(NC)}{logo()}
{big("Campanha B", 150, 140)}{sub("Lead mais caro. Venda mais barata.", 290, 46)}
{ab(camp("Campanha B", "R$ 40", "8", "R$ 320", OR), 440, 400, 2.5, 1.05)}
{tag("CPL alto", "k", 62, 440, -4, 40)}
{card('<div class="n">40 × 8</div><div><b>= R$ 320 por venda</b><small>exemplo ilustrativo</small></div>', 60, 820, -2, 600)}
{blk("pelo caixa, a B custa", 1040, 60, -1.5)}{blk("<em>quase metade</em> por venda", 1118, 76, 1)}
{pill("o CPL apontava o contrário →", 1204, 66, -2, 36)}{dots(5, TC)}{nxt()}"""
w("ccpl_05", P(b))

b = f"""{chip(NC)}{logo()}
{big("Lado a lado", 150, 136)}{sub("Mesma conta, duas leituras.", 290, 46)}
{ab(camp("Campanha A", "R$ 15", "40", "R$ 600"), 30, 390, -3, .9)}
{ab(camp("Campanha B", "R$ 40", "8", "R$ 320", OR), 520, 600, 3, .9)}
{tag("pelo CPL: A", "w", 62, 790, -3, 38)}{tag("pelo caixa: B", "o", 100, 890, 2, 38)}
{blk("meta de mídia é custo", 1040, 60, -1.5)}{blk("por <em>lead qualificado</em> ou venda", 1118, 76, 1, 48)}
{pill("e essa informação precisa voltar →", 1204, 66, -2, 36)}{dots(6, TC)}{nxt()}"""
w("ccpl_06", P(b))

FLOW = '''<div class="fl"><div class="bx">CRM<small>lead · oportunidade · venda</small></div><div class="ar">→</div>
<div class="bx">Conversão offline<small>ou integração</small></div><div class="ar">→</div><div class="bx">Google · Meta<small>otimiza para a venda</small></div></div>'''
b = f"""{org(520)}{chip(NC)}{logo()}
{big("Devolva a<br>venda", 150, 160)}{sub("para a plataforma aprender com ela.", 450, 44)}
{ab(FLOW, 40, 560, -1.5, .98)}
{card('<div class="n">1</div><div><b>Marcar no CRM o que virou venda</b></div>', 60, 760, -3, 600)}
{card('<div class="n">2</div><div><b>Enviar os eventos ao Google e ao Meta</b></div>', 120, 870, 2, 640)}
{card('<div class="n">3</div><div><b>Otimizar para a etapa mais funda com volume</b></div>', 60, 980, -2, 700)}
{blk("sem retorno, ela busca", 1100, 60, -1.5, 50)}{blk("o <em>lead mais barato</em>", 1170, 76, 1, 50)}
{dots(7, TC)}{nxt()}"""
w("ccpl_07", P(b))

b = f"""{chip(NC)}{logo()}{av(60, 150, 200, -5)}
{blk("na sua operação,", 400, 60, -1.5, 66)}{blk("a venda volta para", 490, 76, 1, 66)}{blk("a <em>plataforma</em>?", 580, 60, -1, 66)}
{card('<div class="n">CPL</div><div><b>meta por lead</b></div>', 60, 730, -3, 420)}
{card('<div class="n">CPLQ</div><div><b>lead qualificado</b></div>', 300, 850, 3, 460)}
{card('<div class="n">CPV</div><div><b>custo por venda</b></div>', 560, 730, -2, 440)}
{pill("me conta qual é a sua meta →", 1010, 66, -2, 44)}
<div class="foot" style="bottom:90px">Exemplo A e B com números redondos · telas ilustrativas</div>{dots(8, TC)}"""
w("ccpl_08", P(b, "", "fr o"))

# =================== 27/11 · Ignite RAIO-X pós Black Friday ===================
CK = '''<div class="pn ck" style="width:560px;padding:14px 26px"><div class="hd" style="margin:8px 0 0"><span>RAIO-X · semana que vem</span><span>4 pontos</span></div>
<div><span class="y">1</span>Plataforma × caixa</div><div><span class="y">2</span>Cliente novo × base</div><div><span class="y">3</span>CPM e custo × outubro</div><div><span class="y">4</span>Ticket e margem</div></div>'''
b = f"""{org(470)}{chip("Ignit Agency · RAIO-X")}{logo()}
{big("Hoje o<br>painel", 150, 170)}{sub("vai mostrar o melhor resultado do ano.", 480, 40, "right:360px")}{av(840, 220, 180, 6)}
{tag("ROAS da semana: 9,2", "w", 62, 580, -3, 36)}{tag("ilustrativo", "k", 520, 590, 3, 28)}
{ab(CK, 60, 680, -2)}
{ab('''<div class="pn" style="width:340px;text-align:center"><div class="hd" style="justify-content:center"><span>caixa · mesmo período</span></div><div style="font-family:'ID';font-weight:700;font-size:64px;letter-spacing:-.03em">?</div><div style="font-family:'MO';font-size:14px;color:#6B6E73">confira antes de concluir</div></div>''', 680, 700, 5)}
{blk("na segunda, separe", 1040, 60, -1.5)}{blk("cliente novo de <em>quem já ia comprar</em>", 1118, 76, 1, 46)}
{pill("comente RAIO-X que eu te chamo →", 1204, 66, -2, 38)}
{foot("Números ilustrativos")}"""
w("p_raiox", P(b))

# =================== Capa do artigo (1920x1080) ===================
b = f"""<div class="org" style="left:1180px;top:0;height:auto"></div>{chip("Artigo · automação em mídia")}
<div class="logo" style="right:60px"><span>{RAIO.format(c=OR)}</span>IGNIT AGENCY</div>
{big("O que eu deixo<br>a máquina decidir", 190, 112)}{tag("e o que eu não deixo", "o", 62, 430, -3, 64)}
{sub("Lance, público, criativo e termos de pesquisa: onde a automação ajuda e onde ela precisa de limite.", 600, 38, "width:980px")}{av(900, 780, 200, 6)}
{blk("a meta <em>continua sendo minha</em>", 830, 60, -1.5, 52)}
{ab('''<div class="pn" style="width:640px"><div class="hd"><span>Quem decide · minha divisão</span><span>opinião</span></div>
<table class="tb" style="font-size:24px"><tr><th>decisão</th><th>máquina</th><th>eu</th></tr>
<tr><td>lance por leilão</td><td><span class="mt a">sim</span></td><td></td></tr>
<tr><td>público dentro do sinal</td><td><span class="mt a">sim</span></td><td></td></tr>
<tr><td>qual conversão otimizar</td><td></td><td><span class="mt">sim</span></td></tr>
<tr><td>texto e imagem no ar</td><td></td><td><span class="mt">sim</span></td></tr>
<tr><td>termos e expansões</td><td>com limite</td><td><span class="mt">sim</span></td></tr></table></div>''', 1110, 450, 2.5, 1.22)}"""
w("art_capa", P(b, "", "fr wide"))
print("ok")
