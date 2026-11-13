import sys; sys.path.insert(0, "/home/claude/linkedin/sistema")
from parts import page, sig

# ---------- produto (SVG) ----------
def bottle(h):
    return f'''<svg viewBox="0 0 120 224" height="{h}" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="st" x1="0" x2="1"><stop offset="0" stop-color="#15161A"/><stop offset=".3" stop-color="#3B3F45"/><stop offset=".46" stop-color="#737981"/><stop offset=".6" stop-color="#2C2F34"/><stop offset="1" stop-color="#121316"/></linearGradient>
<linearGradient id="cp" x1="0" x2="1"><stop offset="0" stop-color="#0E0F11"/><stop offset=".45" stop-color="#4A4E55"/><stop offset="1" stop-color="#0E0F11"/></linearGradient></defs>
<ellipse cx="60" cy="214" rx="46" ry="7" fill="#000" opacity=".22"/>
<rect x="40" y="4" width="40" height="26" rx="6" fill="url(#cp)"/><rect x="45" y="28" width="30" height="12" fill="#1A1B1E"/>
<rect x="22" y="38" width="76" height="174" rx="20" fill="url(#st)"/>
<rect x="33" y="52" width="5" height="146" rx="2.5" fill="#fff" opacity=".2"/>
<rect x="22" y="100" width="76" height="52" fill="#EFEBE3"/>
<text x="60" y="126" text-anchor="middle" font-family="ID" font-weight="600" font-size="15" letter-spacing="2" fill="#141518">AURA</text>
<text x="60" y="142" text-anchor="middle" font-family="MO" font-size="8" fill="#55585D">500 ML · 24 H</text></svg>'''

TROP = '''<svg class="bgsvg" viewBox="0 0 246 200" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F6B98D"/><stop offset=".55" stop-color="#F8D9B6"/><stop offset="1" stop-color="#FBEBD3"/></linearGradient>
<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3E9AA8"/><stop offset="1" stop-color="#7CC3C2"/></linearGradient></defs>
<rect width="246" height="200" fill="url(#sky)"/><circle cx="182" cy="62" r="26" fill="#FFF3DC" opacity=".9"/>
<rect y="104" width="246" height="34" fill="url(#sea)"/><path d="M0 112 q30 -5 60 0 t60 0 t60 0 t66 0" stroke="#fff" stroke-width="1.2" fill="none" opacity=".5"/>
<path d="M0 134 C60 126 150 140 246 130 V200 H0Z" fill="#EBD3A8"/><path d="M0 150 C80 142 170 158 246 146 V200 H0Z" fill="#E2C592"/>
<g fill="#2F6B4F"><path d="M-6 0 C30 14 52 40 58 78 C38 52 16 36 -6 30Z"/><path d="M-6 26 C22 40 34 62 34 96 C22 72 8 60 -6 56Z" fill="#3D8262"/><path d="M252 -4 C214 12 196 36 192 70 C210 46 230 34 252 28Z"/></g></svg>'''

ICON = {
 "grid": '<path d="M2 2h5v5H2zM9 2h5v5H9zM2 9h5v5H2zM9 9h5v5H9z"/>',
 "mega": '<path d="M2 6v4l2 .5V5.5zM4 5.5L13 2v12L4 10.5M6 11v3h2v-2.4"/>',
 "users": '<circle cx="6" cy="5" r="2.4"/><path d="M1.5 14c0-2.6 2-4.2 4.5-4.2S10.500 11.400 10.500 14M11 3.200a2.200 2.200 0 010 4.200M12.200 9.800c1.500.5 2.300 1.900 2.300 4.200"/>',
 "img": '<rect x="2" y="3" width="12" height="10" rx="1.500"/><circle cx="6" cy="6.500" r="1.200"/><path d="M2.500 12l3.500-3.500 2.500 2.500 2-2 3 3"/>',
 "chart": '<path d="M2 14h12M4 14V8M8 14V3M12 14V6"/>',
 "card": '<rect x="1.500" y="3.500" width="13" height="9" rx="1.500"/><path d="M1.500 6.500h13"/>',
 "gear": '<circle cx="8" cy="8" r="2.200"/><path d="M8 1.500v2M8 12.500v2M1.500 8h2M12.500 8h2M3.400 3.400l1.400 1.400M11.200 11.200l1.400 1.400M3.400 12.600l1.400-1.400M11.200 4.800l1.400-1.400"/>',
}
def ic(n): return f'<svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round">{ICON[n]}</svg>'

nav = [("grid","Visão geral",0),("mega","Campanhas",1),("users","Públicos",0),("img","Criativos",0),("chart","Relatórios",0),("card","Cobrança",0),("gear","Configurações",0)]
rows = [
 ("01","Garrafa 500 ml · Estúdio","ok","Ativo","142","R$ 18,40","R$ 2.612,80",0),
 ("02","Kit 2 garrafas","ok","Ativo","96","R$ 21,75","R$ 2.088,00",0),
 ("03","Garrafa 500 ml · Carrossel","ai","Alterado por IA","61","R$ 27,10","R$ 1.653,10",1),
 ("04","Copo térmico 350 ml","rv","Em análise","—","—","R$ 0,00",0),
 ("05","Garrafa 1 L","pa","Pausado","33","R$ 24,90","R$ 821,70",0),
]
def tr(r):
    n,name,st,stl,res,cpr,sp,sel = r
    return (f'<div class="g-tr{" sel" if sel else ""}"><span class="g-ck{" on" if sel else ""}"></span><span class="g-tg{" on" if st in ("ok","ai") else ""}"></span>'
            f'<span class="g-ad"><i class="g-th t{n}"></i><span><b>Anúncio {n}</b><small>{name}</small></span></span>'
            f'<span class="g-st {st}">{stl}</span><span class="n">{res}</span><span class="n">{cpr}</span><span class="n">{sp}</span></div>')

def tog(a,b,on,pad=True):
    return (f'<div class="g-imp"><div><b>{a}</b><small>{b}</small></div>'
            f'{"<em>Padrão</em>" if on else ""}<span class="g-tg lg{" on" if on else ""}"></span></div>')

ROUGH = '<svg class="rough" viewBox="0 0 300 150" preserveAspectRatio="none"><path d="M18 78 C10 30 70 8 150 9 C236 10 292 34 288 76 C284 122 222 142 146 141 C74 140 24 122 18 80 C16 66 22 52 34 44" fill="none" stroke="#E2470C" stroke-width="3.200" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>'

screen = f'''
<div class="g960">
 <div class="g-top"><span class="g-mark"></span><b>Gerenciador de Anúncios</b><span class="g-acc">Loja Exemplo · BR <i>▾</i></span>
   <span class="g-search">Buscar por nome, ID ou métrica</span><span class="g-sp"></span><span class="g-bell"><i></i></span><span class="g-av">LE</span></div>
 <div class="g-body">
  <div class="g-nav">{''.join(f'<div class="g-ni{" on" if o else ""}">{ic(i)}<span>{l}</span></div>' for i,l,o in nav)}
    <div class="g-quota"><small>Gasto no mês</small><b>R$ 7.175,60</b><div><i></i></div><small>de R$ 12.000,00</small></div></div>
  <div class="g-main">
   <div class="g-crumb">Campanhas › Vendas · Black Friday › Conjunto Brasil 25–54</div>
   <div class="g-tabs"><span>Campanhas</span><span>Conjuntos</span><span class="on">Anúncios <i>5</i></span></div>
   <div class="g-tool"><span class="g-btn pri">+ Criar</span><span class="g-btn">Duplicar</span><span class="g-btn">Editar</span><span class="g-sp"></span><span class="g-btn">Colunas: Desempenho</span><span class="g-btn">10 – 16 nov 2026</span></div>
   <div class="g-table"><div class="g-tr hd"><span></span><span></span><span>Anúncio</span><span>Veiculação</span><span class="n">Compras</span><span class="n">Custo por compra</span><span class="n">Valor usado</span></div>
     {''.join(tr(r) for r in rows)}
     <div class="g-tr ft"><span></span><span></span><span>Resultados de 5 anúncios</span><span></span><span class="n">332</span><span class="n">R$ 21,61</span><span class="n">R$ 7.175,60</span></div></div>
   <div class="g-chart"><div><b>Custo por compra</b><small>Últimos 7 dias · todos os anúncios</small></div>
     <svg viewBox="0 0 420 70" width="420" height="70" fill="none"><path d="M0 60H420M0 35H420M0 10H420" stroke="#EEF0F3"/><path d="M4 50 L70 46 L138 48 L206 30 L274 22 L342 26 L414 14" stroke="#1B3A8A" stroke-width="2"/><circle cx="206" cy="30" r="4" fill="#fff" stroke="#E0780A" stroke-width="2"/><text x="214" y="50" font-size="9.500" fill="#9A4A06" font-family="IT">12 nov · melhorias ativadas</text></svg></div>
  </div>
  <div class="g-drawer">
   <div class="g-dh"><b>Anúncio 03</b><span>✕</span></div>
   <div class="g-dp"><i class="g-th t03 big"></i><div><b>Garrafa 500 ml · Carrossel</b><small>ID 2384 7710 0932 · editado em 12 nov</small></div></div>
   <div class="g-ds"><b>Melhorias de criativo com IA</b><em class="amb">3 ativas</em></div>
   <div class="g-on">{ROUGH}{tog("Traduzir o texto","Exibe o anúncio em outros idiomas",1)}{tog("Gerar fundo da imagem","Cria novos cenários a partir da foto",1)}{tog("Adicionar links do site","Inclui páginas do domínio",1)}</div>
   {tog("Ajustar brilho e contraste","Correção automática",0)}
   <div class="g-warn"><b>Sem revisão registrada</b>As melhorias acima entraram por padrão e já estão em veiculação.</div>
   <div class="g-log"><small>Histórico</small>
     <p><i></i><span>12 nov · 14:32</span>Sistema gerou novo fundo</p><p><i></i><span>12 nov · 14:32</span>Sistema traduziu o texto (PT → EN)</p><p><i class="h"></i><span>03 nov · 10:05</span>Marketing aprovou o criativo</p></div>
   <div class="g-da"><span class="g-btn">Desativar todas</span><span class="g-btn pri">Revisar anúncio</span></div>
   <svg class="cursor" viewBox="0 0 20 24" width="20" height="24"><path d="M2 1.500v17l4.600-3.800 2.900 6.800 3-1.300-2.900-6.700 6.400-.3z" fill="#141518" stroke="#fff" stroke-width="1.400" stroke-linejoin="round"/></svg>
  </div>
 </div>
</div>'''

phone = f'''
<div class="f-ph"><div class="f-s">
 <div class="f-stat"><b>9:41</b><span class="f-isl"></span><span class="f-ic"><i></i><i></i><i></i><i></i><u></u></span></div>
 <div class="f-hd"><span class="f-q">Pesquisar</span><span class="f-dot"></span><span class="f-dot"></span></div>
 <div class="f-post">
  <div class="f-ah"><span class="f-av">A</span><div><b>Aura Garrafas</b><small>Patrocinado</small></div><span class="f-more">···</span></div>
  <p class="f-cp">Thermal bottle 500 ml. Keeps it ice cold for 24h. Shop now.<small>Traduzido automaticamente · <u>ver original</u></small></p>
  <div class="f-img">{TROP}<span class="f-tag">Fundo gerado por IA</span><div class="f-pr">{bottle(150)}</div></div>
  <div class="f-cta"><div><small>AURAGARRAFAS.COM.BR</small><b>Thermal bottle 500 ml</b></div><span>Shop now</span></div>
  <div class="f-re"><span><i></i>128</span><span>14 comentários</span></div>
 </div>
 <div class="f-post sk"><div class="f-ah"><span class="f-av g"></span><div><i></i><i class="s"></i></div></div></div>
</div></div>'''

proof = f'''
<div class="p-pf"><span class="p-tape"></span>
 <div class="p-h"><span>PROVA DE CRIATIVO</span><span>03.11.2026</span></div>
 <div class="p-img">{bottle(118)}</div>
 <p>Garrafa térmica 500 ml. Gelada por 24 horas. Compre agora.</p>
 <div class="p-ft"><span class="p-stamp">APROVADO</span><svg viewBox="0 0 90 30" width="80" height="27"><path d="M3 20 C10 4 16 6 14 18 C13 26 22 8 28 12 C33 15 26 24 34 18 C42 12 44 22 52 16 C60 10 62 20 86 14" fill="none" stroke="#1F2A44" stroke-width="1.600" stroke-linecap="round"/></svg></div>
</div>'''

css = r"""
@font-face{font-family:"HW";src:url("../../fonts/Caveat-600.woff2")}
.frame{padding-top:72px;background:#F1EEE8}
.grain{position:absolute;inset:0;opacity:.5;mix-blend-mode:multiply;pointer-events:none}
.light{position:absolute;left:-10%;right:-10%;top:300px;height:820px;background:linear-gradient(104deg,transparent 30%,rgba(255,255,255,.55) 47%,rgba(255,255,255,.15) 60%,transparent 72%)}
.hl{position:relative;margin-top:34px;font-family:"ID";font-weight:600;font-size:54px;line-height:1.03;letter-spacing:-.026em}
/* ---------- notebook ---------- */
.lap{position:absolute;left:44px;top:338px;width:748px;transform:perspective(2600px) rotateY(7deg) rotateX(1.500deg);transform-origin:0 50%}
.lid{background:linear-gradient(#232427,#17181A);border-radius:18px 18px 4px 4px;padding:13px 14px 16px;box-shadow:0 0 0 1px #0C0D0E,0 46px 60px -34px rgba(20,21,24,.6)}
.cam{width:6px;height:6px;border-radius:50%;background:#3A3C41;margin:0 auto 7px;box-shadow:0 0 0 1.500px #111}
.scr{width:720px;height:450px;overflow:hidden;border-radius:3px;position:relative;background:#F4F5F7}
.scr:after{content:"";position:absolute;inset:0;background:linear-gradient(118deg,rgba(255,255,255,.16) 0%,rgba(255,255,255,0) 32%);pointer-events:none}
.deck{height:15px;margin:0 -46px;background:linear-gradient(#E3E0DA 0%,#CBC7BF 55%,#A9A59C 100%);border-radius:2px 2px 16px 16px;position:relative;box-shadow:0 22px 26px -14px rgba(20,21,24,.45)}
.deck:after{content:"";position:absolute;left:50%;top:0;transform:translateX(-50%);width:112px;height:6px;background:#B0ABA1;border-radius:0 0 8px 8px}
.g960{width:960px;height:600px;transform:scale(.75);transform-origin:0 0;font-family:"IT";color:#1C2026;font-size:12px;display:flex;flex-direction:column}
.g960 small{display:block;color:#737A85;font-size:10.500px}
.g-top{height:44px;background:#fff;border-bottom:1px solid #E2E5EA;display:flex;align-items:center;gap:12px;padding:0 14px;flex:none}
.g-top b{font-family:"ID";font-weight:600;font-size:13.500px;letter-spacing:-.01em}
.g-mark{width:20px;height:20px;border-radius:6px;background:#1B3A8A;position:relative}.g-mark:after{content:"";position:absolute;inset:5px;border:2px solid #fff;border-radius:50%;border-right-color:transparent}
.g-acc{border:1px solid #D9DDE3;border-radius:6px;padding:5px 9px;font-weight:500;font-size:11.500px}.g-acc i{font-style:normal;color:#737A85;margin-left:4px}
.g-search{flex:0 0 250px;background:#F1F3F6;border-radius:6px;padding:6px 10px;color:#8B929C;font-size:11.500px}
.g-sp{flex:1}
.g-bell{width:16px;height:17px;border:1.500px solid #5C6470;border-radius:8px 8px 3px 3px;position:relative}.g-bell i{position:absolute;right:-5px;top:-5px;width:9px;height:9px;border-radius:50%;background:#D93025;border:1.500px solid #fff}
.g-av{width:26px;height:26px;border-radius:50%;background:#E7D9C8;color:#5B4630;font-weight:600;font-size:10.500px;display:grid;place-items:center}
.g-body{flex:1;display:flex;position:relative;min-height:0}
.g-nav{width:164px;background:#fff;border-right:1px solid #E2E5EA;padding:12px 8px;display:flex;flex-direction:column;gap:2px;flex:none}
.g-ni{display:flex;align-items:center;gap:9px;padding:7px 9px;border-radius:6px;color:#4A515C;font-weight:500}
.g-ni.on{background:#E8EEFB;color:#1B3A8A}
.g-quota{margin-top:auto;border:1px solid #E2E5EA;border-radius:8px;padding:10px}
.g-quota b{display:block;font-family:"ID";font-size:15px;margin:2px 0 6px;font-variant-numeric:tabular-nums}
.g-quota div{height:5px;border-radius:3px;background:#E9ECF0;margin-bottom:5px}.g-quota div i{display:block;width:60%;height:100%;border-radius:3px;background:#1B3A8A}
.g-main{flex:1;padding:12px 16px;min-width:0}
.g-crumb{color:#737A85;font-size:11px}
.g-tabs{display:flex;gap:20px;border-bottom:1px solid #E2E5EA;margin-top:10px}
.g-tabs span{padding:7px 0;font-weight:500;color:#5C6470}.g-tabs .on{color:#1B3A8A;box-shadow:0 2px 0 #1B3A8A}
.g-tabs i{font-style:normal;background:#E8EEFB;border-radius:8px;padding:1px 6px;font-size:10px;margin-left:3px}
.g-tool{display:flex;gap:7px;margin:10px 0}
.g-btn{border:1px solid #D4D9E0;border-radius:6px;padding:5px 10px;font-weight:500;background:#fff;font-size:11.500px;white-space:nowrap}
.g-btn.pri{background:#1B3A8A;border-color:#1B3A8A;color:#fff}
.g-table{background:#fff;border:1px solid #E2E5EA;border-radius:8px;overflow:hidden}
.g-tr{display:grid;grid-template-columns:22px 34px 214px 118px 70px 104px 1fr;align-items:center;gap:8px;padding:8px 12px;border-bottom:1px solid #EEF0F3;font-variant-numeric:tabular-nums}
.g-tr.hd{background:#F7F8FA;color:#5C6470;font-weight:600;font-size:10.500px;padding:7px 12px}
.g-tr.ft{background:#F7F8FA;font-weight:600;border-bottom:0}
.g-tr.sel{background:#EEF3FE;box-shadow:inset 3px 0 0 #1B3A8A}
.g-tr .n{text-align:right}
.g-ck{width:13px;height:13px;border:1.500px solid #B6BCC6;border-radius:3px}.g-ck.on{background:#1B3A8A;border-color:#1B3A8A}
.g-tg{width:26px;height:14px;border-radius:8px;background:#C6CBD3;position:relative;display:inline-block;flex:none}
.g-tg:after{content:"";position:absolute;top:2px;left:2px;width:10px;height:10px;border-radius:50%;background:#fff}
.g-tg.on{background:#1B3A8A}.g-tg.on:after{left:14px}
.g-tg.lg{width:34px;height:19px;border-radius:10px}.g-tg.lg:after{width:15px;height:15px}.g-tg.lg.on:after{left:17px}
.g-ad{display:flex;gap:9px;align-items:center}.g-ad b{font-weight:600;display:block}
.g-th{width:34px;height:34px;border-radius:5px;flex:none;background:linear-gradient(#E4E2DD,#CFCBC4);position:relative;overflow:hidden}
.g-th:after{content:"";position:absolute;left:12px;top:7px;width:10px;height:22px;border-radius:3px;background:#2B2D31}
.g-th.t02:before{content:"";position:absolute;left:5px;top:10px;width:8px;height:19px;border-radius:3px;background:#55585D}
.g-th.t03{background:linear-gradient(#F6B98D 0 50%,#3E9AA8 50% 66%,#E2C592 66%)}
.g-th.t04{background:linear-gradient(#DCE3E8,#C3CDD4)}.g-th.t04:after{height:14px;top:13px;width:12px;left:11px}
.g-th.t05:after{height:26px;top:4px}
.g-th.big{width:52px;height:52px}.g-th.big:after{left:19px;top:11px;width:14px;height:32px}
.g-st{font-weight:500;font-size:11px;display:flex;align-items:center;gap:6px}.g-st:before{content:"";width:7px;height:7px;border-radius:50%;background:#2E9E5B}
.g-st.ai{color:#9A4A06}.g-st.ai:before{background:#E0780A}.g-st.rv:before{background:#B6BCC6}.g-st.pa:before{background:#B6BCC6}.g-st.pa,.g-st.rv{color:#737A85}
.g-chart{margin-top:10px;background:#fff;border:1px solid #E2E5EA;border-radius:8px;padding:10px 12px;display:flex;gap:14px;align-items:center;width:604px}.g-chart b{font-weight:600;display:block}
.g-drawer{position:absolute;right:0;top:0;bottom:0;width:324px;background:#fff;border-left:1px solid #D9DDE3;box-shadow:-18px 0 30px -18px rgba(20,25,40,.28);padding:0 14px;display:flex;flex-direction:column}
.g-dh{display:flex;justify-content:space-between;align-items:center;height:40px;border-bottom:1px solid #EEF0F3;margin:0 -14px;padding:0 14px}.g-dh b{font-family:"ID";font-size:14px}.g-dh span{color:#737A85}
.g-dp{display:flex;gap:10px;align-items:center;padding:10px 0}.g-dp b{font-weight:600;display:block}
.g-ds{display:flex;justify-content:space-between;align-items:center;padding:6px 0 4px;border-top:1px solid #EEF0F3}.g-ds b{font-weight:600;font-size:12.500px}
.amb{font-style:normal;font-size:10.500px;font-weight:600;color:#8A4B06;background:#FDEBCB;border-radius:9px;padding:2px 8px}
.g-on{position:relative;margin:2px -6px;padding:0 6px}
.g-imp{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid #F1F2F5}.g-imp div{flex:1}.g-imp b{font-weight:500;display:block}
.g-imp em{font-style:normal;font-size:9.500px;color:#737A85;border:1px solid #D9DDE3;border-radius:4px;padding:1px 5px}
.rough{position:absolute;left:196px;top:-6px;width:128px;height:calc(100% + 12px);overflow:visible;z-index:3}
.g-warn{margin-top:9px;background:#FFF6E5;border:1px solid #F3D49A;border-radius:7px;padding:8px 10px;font-size:11px;color:#6B4A12;line-height:1.35}.g-warn b{display:block;color:#8A4B06}
.g-log{margin-top:9px}.g-log p{display:flex;gap:7px;align-items:center;font-size:10.500px;color:#3D434C;padding:3px 0}.g-log p span{color:#737A85;width:78px;flex:none;font-variant-numeric:tabular-nums}
.g-log i{width:6px;height:6px;border-radius:50%;background:#E0780A;flex:none}.g-log i.h{background:#2E9E5B}
.g-da{margin-top:auto;display:flex;gap:8px;justify-content:flex-end;padding:10px 0;border-top:1px solid #EEF0F3}
.cursor{position:absolute;right:128px;bottom:-3px;z-index:4;filter:drop-shadow(0 2px 2px rgba(0,0,0,.3))}
/* ---------- celular ---------- */
.f-ph{position:absolute;left:770px;top:452px;width:268px;height:556px;background:linear-gradient(145deg,#2A2C30,#0E0F11);border-radius:44px;padding:10px;transform:rotate(3.500deg);box-shadow:0 0 0 1.500px #3A3D42 inset,0 60px 60px -36px rgba(20,21,24,.7),18px 30px 50px -20px rgba(20,21,24,.35)}
.f-s{background:#F3F4F6;border-radius:35px;height:100%;overflow:hidden;position:relative;font-family:"IT";color:#14171C}
.f-s:after{content:"";position:absolute;inset:0;background:linear-gradient(125deg,rgba(255,255,255,.22) 0%,rgba(255,255,255,0) 30%);pointer-events:none}
.f-stat{height:40px;display:flex;align-items:center;justify-content:space-between;padding:6px 22px 0;background:#fff;font-size:11.500px}.f-stat b{font-weight:600}
.f-isl{position:absolute;left:50%;top:9px;transform:translateX(-50%);width:76px;height:22px;border-radius:12px;background:#0B0C0D}
.f-ic{display:flex;align-items:flex-end;gap:2px}.f-ic i{width:3px;background:#14171C;border-radius:1px}.f-ic i:nth-child(1){height:4px}.f-ic i:nth-child(2){height:6px}.f-ic i:nth-child(3){height:8px}.f-ic i:nth-child(4){height:10px}
.f-ic u{width:20px;height:10px;border:1.200px solid #14171C;border-radius:3px;margin-left:5px;position:relative;text-decoration:none}.f-ic u:after{content:"";position:absolute;inset:1.500px;right:5px;background:#14171C;border-radius:1px}
.f-hd{background:#fff;display:flex;gap:8px;align-items:center;padding:6px 12px 9px;border-bottom:1px solid #E6E8EC}
.f-q{flex:1;background:#EEF0F3;border-radius:14px;padding:6px 11px;font-size:10.500px;color:#7A818B}.f-dot{width:22px;height:22px;border-radius:50%;background:#EEF0F3}
.f-post{background:#fff;margin-top:7px}
.f-ah{display:flex;gap:8px;align-items:center;padding:9px 11px 6px}.f-ah b{font-size:11.500px;font-weight:600;display:block}.f-ah small{font-size:9.500px;color:#737A85}
.f-av{width:28px;height:28px;border-radius:50%;background:#141518;color:#F1EFEA;display:grid;place-items:center;font-family:"ID";font-weight:600;font-size:12px}.f-av.g{background:#E3E6EA}
.f-more{margin-left:auto;color:#737A85;letter-spacing:1px}
.f-cp{font-size:11px;line-height:1.38;padding:0 11px 8px}.f-cp small{display:block;font-size:9px;color:#737A85;margin-top:3px}.f-cp u{color:#1B3A8A;text-decoration:none}
.f-img{height:196px;position:relative;overflow:hidden}.bgsvg{position:absolute;inset:0;width:100%;height:100%}
.f-pr{position:absolute;left:50%;bottom:8px;transform:translateX(-50%)}
.f-tag{position:absolute;left:8px;top:8px;z-index:2;font-size:9px;font-weight:600;color:#fff;background:rgba(15,18,24,.72);padding:3px 7px;border-radius:9px}
.f-cta{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:8px 11px;background:#F6F7F9}.f-cta small{display:block;font-size:8px;color:#737A85;letter-spacing:.03em}.f-cta b{font-size:11px;font-weight:600}
.f-cta span{font-size:10.500px;font-weight:600;background:#E1E4E9;border-radius:6px;padding:6px 9px;white-space:nowrap}
.f-re{display:flex;justify-content:space-between;padding:7px 11px;font-size:9.500px;color:#737A85}.f-re i{display:inline-block;width:11px;height:11px;border-radius:50%;background:#1B3A8A;margin-right:4px;vertical-align:-2px}
.f-post.sk .f-ah i{display:block;width:92px;height:7px;border-radius:4px;background:#E3E6EA;margin:3px 0}.f-post.sk .f-ah i.s{width:58px}
/* ---------- prova impressa ---------- */
.p-pf{position:absolute;left:78px;top:822px;width:204px;background:#FDFCF9;padding:12px 12px 10px;transform:rotate(-5deg);box-shadow:0 1px 0 rgba(0,0,0,.06),0 18px 24px -12px rgba(20,21,24,.45)}
.p-tape{position:absolute;left:50%;top:-13px;width:74px;height:24px;transform:translateX(-50%) rotate(2deg);background:rgba(232,214,160,.78);box-shadow:0 1px 2px rgba(0,0,0,.12)}
.p-h{display:flex;justify-content:space-between;font-family:"MO";font-size:9px;letter-spacing:.08em;color:#55585D;margin-bottom:8px}
.p-img{height:132px;background:linear-gradient(#E6E4DF 0 68%,#D3CFC8 68%);display:grid;place-items:center}
.p-pf p{font-family:"IT";font-size:11px;line-height:1.35;color:#14171C;margin-top:8px}
.p-ft{display:flex;justify-content:space-between;align-items:center;margin-top:6px}
.p-stamp{font-family:"MO";font-weight:500;font-size:11px;letter-spacing:.14em;color:#23764A;border:1.500px solid #23764A;border-radius:3px;padding:2px 6px;transform:rotate(-6deg);opacity:.85}
/* ---------- anotações ---------- */
.hw{position:absolute;font-family:"HW";color:#D9480F;font-size:40px;line-height:.95;transform:rotate(-3deg)}
.arrow{position:absolute;overflow:visible}
.strip{position:absolute;left:var(--pad);right:var(--pad);top:1098px;display:grid;grid-template-columns:repeat(3,1fr);border-top:1.500px solid var(--ink);padding-top:12px}
.strip div{font-size:17.500px;line-height:1.32;color:var(--ink-2);padding-right:18px}
.strip b{display:block;font-family:"MO";font-weight:500;font-size:16px;letter-spacing:.06em;color:var(--ink);margin-bottom:3px}
.strip .x b{color:var(--mute);text-decoration:line-through}.strip .now b{color:var(--ember)}
.src{position:absolute;left:var(--pad);right:var(--pad);top:1196px;font-family:"MO";font-size:13.500px;color:var(--mute)}
.sig{bottom:44px;padding-top:16px}
"""

body = f"""
<svg class="grain" xmlns="http://www.w3.org/2000/svg"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 .35  0 0 0 0 .33  0 0 0 0 .3  0 0 0 .09 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>
<div class="light"></div>
<div class="mast" style="position:relative"><span><span class="tag">Análise</span> · Meta Ads</span><b>16.11.2026</b></div>
<div class="hl">A Meta pausou os novos termos de IA. <span class="em">O risco continua com o anunciante.</span></div>
<div class="lap"><div class="lid"><div class="cam"></div><div class="scr">{screen}</div></div><div class="deck"></div></div>
{phone}
{proof}
<div class="hw" style="left:352px;top:968px">o que a marca<br>aprovou</div>
<svg class="arrow" style="left:296px;top:930px" width="70" height="70" viewBox="0 0 70 70"><path d="M62 52 C40 54 22 44 10 20" fill="none" stroke="#D9480F" stroke-width="3" stroke-linecap="round"/><path d="M6 40 L9 17 L28 28" fill="none" stroke="#D9480F" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div class="hw" style="left:520px;top:872px;transform:rotate(2deg)">o que foi ao ar</div>
<svg class="arrow" style="left:690px;top:842px" width="80" height="60" viewBox="0 0 80 60"><path d="M6 46 C24 20 46 12 70 16" fill="none" stroke="#D9480F" stroke-width="3" stroke-linecap="round"/><path d="M52 4 L72 16 L54 30" fill="none" stroke="#D9480F" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div class="strip">
  <div class="x"><b>30.10 → 20.11</b>Vigência prevista dos novos termos</div>
  <div><b>10.11</b>Meta pausa a mudança, sem nova data</div>
  <div class="now"><b>Hoje</b>Revisar o que a IA gera segue com o anunciante</div>
</div>
<div class="src">Interface, marca e dados ilustrativos · Fontes: Search Engine Journal, 10.11.2026 · The Keyword, 23.10.2026</div>
{sig()}
"""
open(sys.argv[1], "w").write(page(body, css))
