import json, re, pathlib
H = pathlib.Path(__file__).resolve().parent.parent
T = {}
T["bf"] = """A uma semana da Black Friday, metade dos consumidores ainda não tinha decidido se ia comprar.

A pesquisa do Reclame Aqui divulgada em 18 de novembro mostra a mudança de agosto para novembro:

1. Os decididos a comprar foram de 19% para 32,3%
2. Os indecisos caíram de 61% para 51,6%
3. 48,1% não definiram orçamento e vão acompanhar as ofertas ao longo do mês
4. Só 17,4% pretendem concentrar as compras na sexta
5. 76,1% dizem que vão consultar o Reclame Aqui durante o evento

Na minha leitura, isso muda onde a verba desta semana rende mais. O consumidor compara ao longo do mês, e a sexta concentra uma parte pequena da decisão.

O que eu faria com a verba desta semana:

1. Proteger o remarketing de quem visitou e comparou
2. Cortar o público frio que não converteu em outubro, com CPM mais baixo
3. Distribuir a verba pelos dias da semana em vez de guardar tudo para a sexta
4. Conferir a reputação da loja antes de subir lance, porque o cliente vai conferir

Na sua conta, a verba da Black Friday está concentrada na sexta ou espalhada pela semana?

#blackfriday #midiapaga #performance"""
C_BF = "Fonte: pesquisa do Reclame Aqui, via Mercado & Consumo, 18/11/2026: https://mercadoeconsumo.com.br/18/11/2026/ecommerce/black-friday-2026-fatia-de-consumidores-decididos-a-comprar-salta-para-323/\nA matéria não informa amostra nem datas de campo."

T["aimax"] = """Quase 29% das impressões de palavra-chave exata já vinham do AI Max em julho, numa análise de e-commerce na região EMEA.

O dado é da Smarter Ecommerce, citado pela PPC Land. E o relatório tinha um problema: o AI Max marcava a expansão com o tipo de correspondência da própria palavra-chave. Um clique "exato" podia ter vindo de uma busca que ninguém escolheu.

Agora a ajuda do Google Ads lista um parâmetro de rastreio novo, o {search_term_matchtype}. Ele grava na URL do clique se a busca chegou pela palavra-chave (e, p ou b) ou por expansão do AI Max (a).

Na minha leitura, quem ligou o AI Max precisa separar esse tráfego antes de avaliar a campanha. O que eu faria:

1. Incluir o parâmetro no modelo de acompanhamento da conta
2. Levar o valor para o GA4 ou para o CRM
3. Comparar custo por venda entre clique de palavra-chave e clique de expansão
4. Limitar a expansão onde ela vende pior

A ressalva: as páginas de ajuda do Google ainda divergem sobre o método, e mudança no modelo leva de 24 a 48 horas para valer.

Você sabe quanto do seu tráfego "exato" veio do AI Max?

#googleads #aimax #midiapaga #performance"""
C_AIMAX = "Fontes:\nPPC Land, 15/11/2026: https://ppc.land/googles-new-parameter-shows-when-an-exact-click-was-really-ai-max/\nRelevant Audience, 12/11/2026: https://www.relevantaudience.com/google-ads-en/google-ads-search-term-matchtype-valuetrack-ai-max/\nGoogle Ads Help, parâmetros ValueTrack: https://support.google.com/google-ads/answer/2375447"

T["painel"] = """Toda segunda de manhã abro o mesmo painel antes de qualquer reunião de cliente.

Ele tem cinco números, e cada um responde a uma pergunta:

1. Investimento da semana: a verba saiu como planejado?
2. Custo por venda ou por lead qualificado: a eficiência se manteve?
3. Volume de vendas ou de leads qualificados: o resultado acompanhou a verba?
4. Taxa de conversão do lead em venda: o gargalo está na mídia ou no comercial?
5. Frequência e CTR dos criativos: está na hora de trocar peça?

Se um número não muda nenhuma decisão, ele não entra no painel. Relatório com 40 métricas costuma esconder o único número que importa naquela semana.

No vídeo, o painel com números ilustrativos e a pergunta que cada bloco responde.

Quais números entram no seu relatório semanal?

#dashboard #midiapaga #growth"""

T["cpl"] = """Já tive conta com CPL de R$7 em que eu não sabia quanto custava cada venda.

Na Sullato, com R$4 mil por mês somando duas contas, o custo por lead ficou em R$7, com 10 a 18 contatos por dia. Para quem anuncia veículo, é um número bom.

O que faltava era o outro lado. O fechamento da venda não era informado. Eu sabia quanto custava cada contato, mas não quanto custava cada venda.

Por isso defendo que o CPL seja só o começo da conversa. Um exemplo com números redondos:

Campanha A: CPL de R$15 e 1 venda a cada 40 leads. Custo por venda de R$600.
Campanha B: CPL de R$40 e 1 venda a cada 8 leads. Custo por venda de R$320.

Pelo CPL, a A parece melhor. Pelo caixa, a B custa quase metade por venda.

O que eu defendo combinar antes de a campanha subir:

1. Marcar no CRM qual lead virou oportunidade e qual virou venda
2. Devolver esses eventos ao Google Ads e ao Meta Ads, por conversão offline ou integração
3. Otimizar para a etapa mais funda do funil que tenha volume

Sem esse retorno, a plataforma segue buscando o lead mais barato.

Na sua operação, a venda volta para a plataforma ou a mídia ainda é medida por CPL?

#marketingdeperformance #googleads #metaads #crm"""

T["raiox"] = """Hoje é Black Friday, e o painel de cada plataforma vai mostrar o melhor resultado do ano.

Antes de tirar conclusão, na semana que vem eu confiro quatro pontos:

1. Conversões das plataformas contra vendas no caixa ou no CRM, no mesmo período
2. Quanto veio de remarketing e da busca pela marca, e quanto de cliente novo
3. CPM e custo por venda da semana contra outubro
4. Ticket médio e margem dos pedidos, além do volume

Na semana mais cara do ano, comparar um painel com outro engana. O que serve para planejar dezembro e janeiro é saber qual público e qual criativo trouxeram cliente novo a um custo que se paga.

Na Ignit Agency, o RAIO-X é a auditoria de conta que responde a essas perguntas. Se quiser que a gente olhe a sua conta depois da Black Friday, comente RAIO-X que eu te chamo.

O seu relatório da Black Friday vai separar cliente novo de quem já ia comprar?

#blackfriday #midiapaga #growth"""

ART_T = "O que eu deixo a automação decidir numa conta de mídia, e o que eu não deixo"
ART = ART_T + """

Toda semana aparece um recurso novo que tira uma decisão das mãos de quem opera mídia. O AI Max amplia as buscas em que o anúncio aparece. A Performance Max escolhe canal, público e combinação de peças. O Advantage+ do Meta mexe em público, posicionamento e, em alguns casos, no próprio criativo.

Não sou contra nada disso. A maior parte desses recursos entrega mais do que a configuração manual que veio antes. O ponto é outro: a automação otimiza para a meta que recebe, com os dados que recebe. Se a meta ou o dado estão errados, ela erra mais rápido e com mais verba.

Por isso separo as decisões de uma conta em dois grupos. As que eu entrego para a plataforma e as que continuam comigo.

O que eu deixo a máquina decidir

Lance por leilão. Nenhuma pessoa ajusta lance melhor que o Smart Bidding ou o lance do Meta olhando milhares de sinais por leilão. Lance manual hoje só faz sentido em conta muito pequena ou em teste controlado.

Público dentro do sinal certo. Com uma boa conversão configurada, público amplo costuma achar comprador mais barato que a segmentação detalhada que eu montaria. Os públicos que eu crio passam a funcionar como sinal e como exclusão.

Distribuição de verba entre conjuntos parecidos. Quando os conjuntos disputam o mesmo público, deixar a plataforma distribuir o orçamento evita que eu pague para competir comigo mesmo.

Combinação de peças. Testar qual título vai com qual imagem é trabalho de máquina. Desde que as peças tenham sido escritas e aprovadas por alguém.

O que eu não deixo

Qual conversão a conta otimiza. Essa é a decisão mais importante de uma conta, e a plataforma não tem como tomá-la por mim. Se a meta é formulário enviado, ela vai achar quem envia formulário. Se a meta é venda, alguém precisa devolver a venda para a plataforma, pelo CRM ou por conversão offline. Essa parte cabe ao time.

O texto e a imagem que vão ao ar. Recursos de melhoria automática de criativo podem traduzir texto, gerar fundo e alterar imagem. Ligo só o que a marca aprovou e registro quem aprovou. Quem responde pelo anúncio continua sendo o anunciante.

Termos de pesquisa e expansões. Busca ampla e AI Max podem funcionar bem, mas precisam de lista de negativas, exclusão de marca quando faz sentido e leitura semanal dos termos. A PPC Land citou recentemente uma análise da Smarter Ecommerce com quase 29% das impressões de palavra-chave exata vindo de expansão do AI Max em e-commerce na região EMEA. O Google passou a documentar um parâmetro de rastreio que separa esse tráfego. Quando a plataforma oferece um jeito de separar, eu uso.

Quanto investir. A plataforma sempre vai aceitar mais verba. Quem decide o teto é o custo por venda real, com dado do caixa ou do CRM.

Como eu reviso a automação

Uma vez por semana, olho quatro coisas em cada conta:

1. Se as conversões da plataforma batem com as vendas registradas fora dela
2. Para onde a verba foi: termos, posicionamentos e públicos que mais gastaram
3. Quais melhorias automáticas estão ligadas em cada anúncio ativo
4. Se o custo por venda real mudou depois de alguma mudança automática

Se algum desses pontos sai do esperado, a automação ganha um limite novo: uma negativa, uma exclusão, uma meta de custo ou um recurso desligado.

A divisão que defendo

A máquina decide como chegar ao resultado. Eu decido qual é o resultado, com que dado ele é medido e até onde a verba vai. Quando essa divisão se inverte, a conta continua rodando, os painéis continuam bonitos e o caixa demora alguns meses para mostrar o problema.

Na sua conta, qual decisão você ainda não entrega para a automação?"""

INV = re.compile("[­᠎​-‏‪-‮⁠-⁯﻿]")
def clean(x): return INV.sub("", x)
for k in T: T[k] = clean(T[k])
ART = clean(ART)
for k, v in T.items():
    assert "—" not in v and "–" not in v, k
    print(k, len(v))
print("artigo palavras", len(ART.split()))
assert "—" not in ART
SHA = "{SHA}"
posts = [
 dict(data="2026-11-23", hora="08:00", formato="carrossel", tema="Black Friday: metade ainda indecisa", midia="cbf_black-friday-metade-indecisa.pdf", documentTitle="Black Friday: metade ainda não decidiu", texto=T["bf"], primeiro_comentario=C_BF),
 dict(data="2026-11-24", hora="08:00", formato="estatico", tema="AI Max: a exata deixou de ser exata", midia="p_aimax.png", texto=T["aimax"], primeiro_comentario=C_AIMAX),
 dict(data="2026-11-25", hora="08:00", formato="video", tema="O painel que abro toda segunda", midia="p_painel_motion.mp4", texto=T["painel"], primeiro_comentario=""),
 dict(data="2026-11-26", hora="08:00", formato="carrossel", tema="CPL de R$7 sem custo por venda (Sullato)", midia="ccpl_cpl-de-7-reais.pdf", documentTitle="CPL de R$7 e o custo da venda", texto=T["cpl"], primeiro_comentario=""),
 dict(data="2026-11-27", hora="08:00", formato="estatico", tema="Ignite: RAIO-X depois da Black Friday", midia="p_raiox.png", texto=T["raiox"], primeiro_comentario=""),
]
ag = dict(semana="2026-11-23", posts=posts, artigo=dict(data="2026-11-23", titulo=ART_T, capa="art_capa.png", texto=ART, status="Publicar manualmente"))
(H / "agenda.json").write_text(json.dumps(ag, ensure_ascii=False, indent=1))
print("ok")
