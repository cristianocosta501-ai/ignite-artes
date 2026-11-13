# Playbook · LinkedIn Cristiano Pereira

Perfil: linkedin.com/in/cristiano-mkt · Posicionamento: Growth & Performance (mídia paga).
Objetivo: dar visibilidade ao perfil do Cristiano e, por ele, levar a Ignit Agency a quem decide verba de mídia.
Calendário contínuo, sem data de término. Revisão de rumo com o Cristiano toda semana.

## 1. Cadência
- 5 posts por semana, segunda a sexta, às 08:00 (America/Sao_Paulo), publicados automaticamente pela Metricool (marca "Cristiano", blogId 8062467). Nunca usar a marca ignit.agency (6822451).
- 1 artigo por semana, na segunda. A Metricool não publica artigo do LinkedIn: o artigo fica pronto na planilha, com capa, para o Cristiano colar e publicar.
- Todo post leva mídia própria: imagem estática (PNG 1080x1350, renderizada em 2x) ou carrossel (PDF 1080x1350). Nada de post só com texto.

## 2. Mix semanal
| Tipo | Quantidade | Exemplo |
|---|---|---|
| Notícia ou caso de outra empresa, com opinião | 2 | mudança de plataforma, campanha de marca, pesquisa de mercado |
| Método ou bastidor de quem opera | 1 | carrossel de checagens, painel, rotina de auditoria |
| Experiência própria do Cristiano | 1 | resultados reais da seção 5, decisão que ele tomou |
| Ignit Agency | 1 | bastidor ou oferta (RAIO-X); um por semana, sempre |
Formatos na semana: pelo menos 2 carrosséis e 2 estáticos.

## 3. Pesquisa
- Rotina diária (seg a sex) alimenta a aba "Radar" da planilha com casos e notícias de marketing, mídia paga, plataformas (Google, Meta, LinkedIn, TikTok), varejo e pesquisas de mercado, sempre com link, data e veículo.
- Só entra fato conferido na fonte primária ou em veículo reconhecido. Agregador e blog de ferramenta servem só para achar a pauta.
- Antes de publicar, confira de novo se a notícia continua valendo (exemplo real: os termos de IA da Meta foram pausados em 10/11/2026, três dias antes do post que falaria da vigência).

## 4. Voz e escrita
- Primeira pessoa, em forma de opinião ("na minha leitura", "defendo", "o que eu faria"), menos casual.
- Gancho na primeira linha, de preferência com número. Parágrafos curtos, frases de até ~12 palavras, lista quando ajudar, fechamento com pergunta concreta, 3 ou 4 hashtags.
- Posts com 700 a 1.300 caracteres. Artigos com 600 a 1.000 palavras e subtítulos simples.
- Sem marcas de texto de IA: nenhum travessão longo, nenhum emoji, nada de "não é X, é Y", "aqui está o segredo", "o que ninguém te conta", frase de efeito no final ou resumo no final. Evitar: alavancar, potencializar, robusto, jornada, desbloquear, transformador.
- Fonte de notícia vai no primeiro comentário (firstCommentText), não no corpo do post, para não derrubar o alcance. A arte traz a linha "Fonte:" em mono.
- Remover caracteres invisíveis (U+00AD, U+180E, U+200B a U+200F, U+202A a U+202E, U+2060 a U+206F, U+FEFF) de todo texto.

## 5. Fatos que podem ser citados
- EstrelaBet: operação saiu de "não entregava" para R$30 milhões em resultado de mídia (programática, Meta, Google, Kwai, X) com CAC de R$69; time de parceiros com mais de R$5 milhões e CAC perto de R$80 por novo apostador com primeiro depósito.
- Sullato (Veículos e Vans e Micros): CPL de R$7 com R$4 mil por mês somando 2 contas; 10 a 18 contatos por dia. Fechamento de venda não era informado pelo cliente.
- Angiclin: +49% em marcações e +63% em contatos para consultas, com R$1 mil por mês, só Google Ads.
- CMais: +58% em contatos e +47% na contratação de acompanhantes e enfermeiros de idosos.
- KPMG (via Brivia): planejamento e estratégia; sem números.
- Ignit Agency: fundada em 01/09/2026 pelo Cristiano (fundador e CEO). Performance, criação, dashboards e B.I., sites. Palavra-chave de oferta: RAIO-X (auditoria de conta).
Nunca inventar número, cliente, case ou processo. Exemplo numérico só com o rótulo "exemplo ilustrativo" ou "números redondos" e conta conferida.

## 6. Sistema visual (pasta sistema/)
- base.css: papel #F3F1EC, grafite #141518, laranja Ignite #D9480F (fundo claro) e #FA581A (fundo escuro), usado só como destaque.
- Tipografia: Inter Display (títulos), Inter (texto), Instrument Serif (citações, numerais grandes), IBM Plex Mono (rótulos, datas, fontes). Fontes extras em fonts/.
- Toda peça: cabeçalho em mono com categoria e data, linha de 1,5 px, assinatura "Cristiano Pereira · Growth & Performance · Mídia paga" e raio + "Ignit Agency" discretos no rodapé.
- Componentes: linha do tempo, cartões de interface (UI), gráfico de barras divergente, blocos de dado, citação em serif, numeral grande em carrossel, caixa "O que eu olho".
- Proibido: degradê, brilho, ícone genérico, foto de banco, ilustração 3D, logo de outra empresa, foto de pessoa pública, reprodução de peça publicitária de terceiros.
- Render: parts.py (componentes), render.py png arquivo.html saida.png [w h], carrossel.py saida.pdf p1.html p2.html ... (rasteriza em 2x e monta o PDF com img2pdf).
- Conferência obrigatória: abrir cada PNG e uma folha de contato de cada carrossel; nada vazando da margem, nada sobreposto, contraste ok, rótulos inteiros.
- Higiene: limpar metadados (PNG re-salvo com Pillow, PDF sem docinfo e XMP via pikepdf) antes de publicar.

## 7. Publicação
- Mídias vão para este ramo (linkedin), pasta AAAA-MM-DD da segunda-feira da semana. Links raw fixados no SHA do commit; conferir que cada link responde 200 antes de agendar.
- Metricool: providers linkedin; autoPublish true; draft false; imagem em media; carrossel como um único PDF em media com linkedinData.documentTitle; firstCommentText com a fonte quando houver.
- Conferir a fila (getScheduledPosts) depois de agendar e atualizar a planilha (status "Agendado", link da arte, id da Metricool).
