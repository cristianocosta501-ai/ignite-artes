"""Piloto Instagram Ignite · carrossel 'Google ou Instagram' (Dom 15/11 12h, Brasil, palavra-chave: anúncios no Google)."""
import sys, os
sys.path.insert(0, "/home/claude/linkedin/sistema")
from criador import *
OUT = "/home/claude/linkedin/ig-piloto/html"; os.makedirs(OUT, exist_ok=True)
def w(n, h): open(f"{OUT}/{n}.html", "w").write(h)
def big(t, top, size, color=INK): return f'<div class="big" style="top:{top}px;font-size:{size}px;color:{color}">{t}</div>'
def sub(t, top, size=54, extra=""): return f'<div class="sub" style="top:{top}px;font-size:{size}px;{extra}">{t}</div>'
def foot2(t): return f'<div class="foot" style="bottom:96px;font-size:15px">{t}</div>'
def org(h): return f'<div class="org" style="height:{h}px"></div>'
xc = f""".wrap{{position:absolute;left:60px;right:60px;top:404px}}.wrap .st{{position:static;font-size:88px}}.wrap .sb{{position:static;margin-top:34px;padding-right:40px;font-size:46px}}
.tb{{position:absolute;left:60px;right:60px;background:#fff;border-radius:26px;padding:14px 30px 20px;box-shadow:0 22px 26px -14px rgba(20,21,24,.5);transform:rotate(-1deg)}}
.tb .h{{display:grid;grid-template-columns:1fr 150px 150px;font-family:"MO";font-size:17px;letter-spacing:.08em;text-transform:uppercase;color:rgba(20,21,24,.6);padding:12px 0;border-bottom:2px solid {INK}}}
.tb .r{{display:grid;grid-template-columns:1fr 150px 150px;align-items:center;padding:22px 0;border-bottom:1.5px solid #ECEAE5;font-weight:600;font-size:34px;letter-spacing:-.02em}}.tb .r:last-child{{border:0}}
.tb .r b{{font-weight:700;font-size:44px}}.tb .r b.o{{color:{OR}}}.tb .h span:nth-child(n+2),.tb .r b{{text-align:right}}
.bar{{grid-column:1/4;display:flex;height:16px;border-radius:8px;overflow:hidden;margin-top:12px;background:#C9C6BE}}.bar i{{background:{OR}}}
.cta{{position:absolute;left:60px;top:610px;background:{INK};color:#fff;font-weight:700;font-size:150px;letter-spacing:-.045em;line-height:1;padding:22px 40px 30px;border-radius:30px;transform:rotate(-3deg);box-shadow:0 30px 34px -18px rgba(20,21,24,.6)}}.cta em{{font-style:normal;color:#FF7A3D}}
.cm{{position:absolute;left:330px;top:880px;width:660px;background:#fff;border-radius:26px;padding:22px 26px;transform:rotate(2deg);box-shadow:0 22px 26px -14px rgba(20,21,24,.5);font-weight:500;font-size:32px;line-height:1.2}}
.cm small{{display:block;font-family:"MO";font-size:16px;letter-spacing:.08em;text-transform:uppercase;color:{OR};margin-bottom:8px}}"""
xc += f"""
.sr{{position:absolute;left:60px;width:700px;height:84px;border-radius:42px;background:#fff;display:flex;align-items:center;gap:18px;padding:0 30px;font-weight:500;font-size:34px;box-shadow:0 18px 22px -12px rgba(20,21,24,.45);transform:rotate(-2deg)}}
.sr:before{{content:"";width:26px;height:26px;border:5px solid {INK};border-radius:50%;flex:none}}.sr u{{text-decoration:none;width:3px;height:40px;background:{OR}}}
.rs{{position:absolute;width:560px;background:#fff;border-radius:20px;padding:16px 22px;box-shadow:0 18px 22px -12px rgba(20,21,24,.45);font-weight:600;font-size:28px;line-height:1.15}}
.rs small{{display:inline-block;font-family:"MO";font-size:14px;letter-spacing:.08em;text-transform:uppercase;background:{INK};color:#fff;border-radius:6px;padding:3px 8px;margin-bottom:8px}}.rs span{{display:block;font-weight:500;font-size:22px;color:rgba(20,21,24,.6);margin-top:4px}}
.pt{{position:absolute;width:300px;background:#fff;border-radius:22px;padding:12px;box-shadow:0 18px 22px -12px rgba(20,21,24,.45)}}
.pt .im{{height:120px;border-radius:14px;background:{OR};position:relative;overflow:hidden}}.pt .im:before{{content:"";position:absolute;left:34px;top:26px;width:90px;height:90px;border-radius:50%;background:#fff;opacity:.9}}.pt .im:after{{content:"";position:absolute;right:-20px;bottom:-40px;width:170px;height:120px;border-radius:30px;background:{INK};transform:rotate(-14deg)}}
.pt small{{display:block;font-family:"MO";font-size:13px;letter-spacing:.08em;text-transform:uppercase;margin:10px 4px 2px;color:rgba(20,21,24,.6)}}.pt b{{display:block;margin:0 4px 4px;font-size:24px}}"""
OBJ = {
 1: '<div class="sr" style="top:850px">encanador urgente<u></u></div><div class="rs" style="left:330px;top:940px;transform:rotate(2deg)"><small>Patrocinado</small><br>Seu negócio aparece aqui<span>anúncio ilustrativo</span></div>',
 2: '<div class="pt" style="left:80px;top:812px;transform:rotate(-4deg)"><div class="im"></div><small>Patrocinado · ilustrativo</small><b>Coleção nova</b></div>' + tag("vi e quis", "k", 470, 880, 4, 44) + tag("nem estava procurando", "w", 420, 980, -3, 36),
 3: tag("Instagram apresenta", "w", 62, 870, -3, 44) + '<div class="hw" style="left:520px;top:880px;font-size:90px;transform:rotate(8deg)">→</div>' + tag("Google fecha", "k", 600, 960, 3, 44),
 4: '<div class="sr" style="top:790px">o que você vende<u></u></div><div class="rs" style="left:330px;top:880px;transform:rotate(2deg)"><small>Patrocinado</small><br>Concorrente anunciando<span>resultado ilustrativo</span></div>',
}
N = "Anúncios no Google ou no Instagram"; T = 8
def step(i, title, text, lk, lv):
    return page(f"""{chip(N)}{logo()}<div class="num">{i}</div>
<div class="wrap"><div class="st">{title}</div><div class="sb">{text}</div></div>
{OBJ[i]}<div class="look"><small>{lk}</small><b>{lv}</b></div>{dots(i + 2, T)}<div class="nx">arrasta →</div>""", xc)

# 1 capa
b = f"""{org(600)}{chip(N)}{logo()}
{big("Google ou", 150, 150)}{big("Instagram?", 282, 150, OR)}
{sub("Onde seu cliente procura primeiro, por tipo de negócio.", 470, 50, "right:120px;line-height:1.12")}
{tag("encanador", "w", 62, 800, -4, 40)}{tag("clínica", "k", 372, 814, 3, 40)}{tag("moda", "w", 622, 796, -3, 40)}
{tag("restaurante", "k", 96, 910, 2, 40)}{tag("curso", "w", 452, 920, -2, 40)}{tag("reforma", "k", 672, 914, 4, 40)}
{blk("antes de pagar <em>anúncios no Google</em>", 1030, 60, -1.5, 46)}
{pill("arrasta e ache o seu →", 1150)}{dots(1, T)}"""
w("s1", page(b, xc))
# 2 tensão (laranja)
b = f"""{chip(N)}{logo()}
{blk("a verba some quando", 330, 60, -1.5, 70)}{blk("o anúncio aparece", 426, 76, 1, 70)}{blk("<em>no lugar errado.</em>", 522, 60, -1, 78)}
{sub("Antes de escolher a rede, responda uma pergunta:", 720, 46, "right:160px;color:#fff;line-height:1.15")}
<div class="cm" style="left:60px;top:880px;width:820px;transform:rotate(-2deg);font-weight:700;font-size:52px;letter-spacing:-.03em;line-height:1.05"><small>a pergunta</small>Seu cliente já sabe que precisa de você?</div>
{dots(2, T)}<div class="nx" style="color:#fff">arrasta →</div>"""
w("s2", page(b, xc, "fr o"))
# 3-5 desenvolvimento
w("s3", step(1, "Já procura? Google", "Quem tem urgência ou necessidade clara digita o que quer. O anúncio aparece nessa hora.", "Negócios assim", "Encanador, chaveiro, clínica, advogado, conserto, mudança"))
w("s4", step(2, "Ainda não procura? Instagram", "Produto de desejo precisa ser visto antes de ser buscado. O anúncio cria a vontade.", "Negócios assim", "Moda, decoração, doces, estética, presentes"))
w("s5", step(3, "Decisão longa? Os dois", "Compra cara começa numa rede e termina na outra. O Instagram apresenta, o Google fecha.", "Negócios assim", "Curso, reforma, móveis planejados, imóvel, viagem"))
# 6 prova: teste
w("s6", step(4, "O teste de 1 minuto", "Digite no Google o que você vende, do jeito que o cliente escreveria.", "O que olhar", "Se há concorrentes anunciando no topo, existe procura pelo seu serviço"))
# 7 prova: ponto de partida
rows = [("Serviço de urgência", 80, 20), ("Produto de desejo", 30, 70), ("Decisão longa", 50, 50)]
tb = '<div class="h"><span>Tipo de negócio</span><span>Google</span><span>Instagram</span></div>' + ''.join(
    f'<div class="r"><span>{n}</span><b class="o">{g}%</b><b>{i}%</b><div class="bar"><i style="width:{g}%"></i></div></div>' for n, g, i in rows)
b = f"""{chip(N)}{logo()}
{big("Ponto de", 150, 130)}{big("partida", 268, 130, OR)}
{sub("Como dividimos a verba no primeiro mês.", 420, 44)}
<div class="tb" style="top:520px">{tb}</div>
{pill("depois, quem manda é o custo por venda", 1060, 66, -2, 38)}
{foot2("Exemplo ilustrativo · a divisão muda conforme o resultado de cada conta")}{dots(7, T)}<div class="nx">arrasta →</div>"""
w("s7", page(b, xc))
# 8 CTA
b = f"""{org(520)}{chip(N)}{logo()}
{big("Não sabe onde", 150, 112)}{big("está o seu", 256, 112)}{big("cliente?", 362, 150, OR)}
<div class="cta">RAIO-<em>X</em></div>
<div class="cm"><small>comente aqui</small>Escreva RAIO-X e a gente olha onde seu negócio deve anunciar primeiro.</div>
{pill("salva para decidir a verba do mês", 1150, 66, -2, 38)}{dots(8, T)}"""
w("s8", page(b, xc))
print("ok")
