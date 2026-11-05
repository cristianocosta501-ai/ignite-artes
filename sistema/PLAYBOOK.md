# Playbook do Instagram da Ignite (@ignit.agency)

Metricool: blogId 6822451, fuso America/Sao_Paulo. Artes: branch `artes` deste repositório, com link raw fixado no SHA do commit.

## Público e objetivo
Donos de negócio brasileiros que faturam nos EUA, Portugal, Espanha ou Austrália. Lead qualificado: opera fora, investe a partir de €800/mês em mídia e é decisor. Meta atual: alcance e compartilhamentos; leads viram métrica principal quando houver volume.

## Grade
2 Reels por dia, às 10h e às 18h. Antes de agendar, consulte a fila e não ocupe horário já usado.

- Help (cerca de 9 por semana): dúvida real de quem contrata ou anuncia fora. Fale com o dono do negócio, não com gestor de tráfego.
- Hub (cerca de 4 por semana): séries fixas. "Câmbio da semana" (só com câmbio e fonte verificados), "Raio-X" (leitura de conta com números rotulados como exemplo), "Vida de quem opera fora".
- Hero (cerca de 1 por semana): peça para compartilhar, como comparação de custo entre países, sempre com fonte citada na legenda.

## Direção visual
O gráfico conta a história e o texto só apoia. Máximo de 6 a 8 palavras no título de cada cena. Toda cena tem um objeto visual: relógio, funil, gráfico, comparação, conversa, checklist, mapa ou chips de cidades. Fundo preto com brilho laranja #FA581A e uma cena laranja por vídeo. Não publique vídeo que seja só texto.

## Técnica
Copie `sistema/` para uma pasta nova e use `exemplos/` como modelo. 30 s, 1080x1920, 30 fps, sete cenas (seis de 4,5 s e logo + CTA com 3 s). Entradas terminam até 1,2 s depois do início da cena. A batida entra no segundo 0.

1. `npm` não é necessário: Playwright e Chromium já estão instalados.
2. `node render.js <pasta absoluta>` gera os frames.
3. `python3 audio.py <pasta>/trilha.wav '{"ticks":[],"pops":[]}'` gera a trilha.
4. `ffmpeg -framerate 30 -i <pasta>/frames/f_%05d.jpg -i <pasta>/trilha.wav -c:v libx264 -pix_fmt yuv420p -crf 20 -c:a aac -b:a 192k -movflags +faststart -shortest reel.mp4`
5. `python3 qa.py <pasta>`: as seis cenas precisam de pelo menos 3,00 s parados.
6. Confira uma grade de frames, a área segura (250 px no topo e 380 px na base) e o áudio em janelas de 3 s, sem nenhuma mais de 3 dB abaixo da média.

## Regras
- Nenhum número de mercado sem fonte verificada e citada. Número ilustrativo leva "exemplo" na tela e na legenda.
- Não invente case, cliente ou depoimento. Não prometa resultado.
- Não republique tema ou gancho dos últimos 30 dias; varie ângulo e visual.
- Não publique definição de conceito.
- CTA: CÂMBIO (custo e arbitragem) ou RAIO-X (auditoria de conta).
- Sem gasto com mídia, sem responder directs e sem qualquer custo novo.
- Se uma checagem falhar, não agende essa peça e avise o que falhou.

## Painéis e gravações
Mostre a estrutura de trabalho com painéis de demonstração (`exemplos/painel`). Todo painel fictício leva "Dados fictícios" na tela e "dados fictícios" na legenda, com nome genérico de cliente. Nunca use dado, marca ou tela de cliente real.

## Mercados, moedas e horários
Cada Reel fala com um mercado principal e usa a moeda dele na tela e na legenda. Número de exemplo continua rotulado como exemplo; câmbio real precisa de fonte e data.

| Mercado | Moeda | Por semana | Horário de teste (São Paulo) | Hashtags e termos na legenda |
|---|---|---|---|---|
| EUA | US$ | 5 | 18h (16h em Miami) e 12h (10h em Miami) | #brasileirosnoseua #brasileirosemorlando #brasileirosemmiami; negócio nos EUA, Flórida, em dólar |
| Portugal e Espanha | € | 3 | 10h (13h em Lisboa) | #brasileirosemportugal #brasileirosnaespanha #empreendedorasbrasileiras; negócio em Portugal, Espanha, Europa, em euro |
| Austrália | A$ | 3 | 19h (9h do dia seguinte em Sydney, em novembro) | #brasileirosnaaustralia #brasileirosemsydney; negócio na Austrália, Sydney, Melbourne, em dólar australiano |
| Brasil | R$ | 3 | 12h ou 18h | #pmes #empreendedorbrasileiro #trafegopago; PME, negócio local, sua cidade, em real |

Fusos mudam com o horário de verão: confira antes de citar um horário. Use no máximo 5 hashtags. Registre o mercado e o horário de cada Reel no resumo diário para comparar alcance, views e compartilhamentos. Só conclua algo depois de pelo menos 5 posts por combinação.

Um horário por dia pode ser trocado conforme o mercado, mantendo no máximo 2 Reels por dia e sem ocupar horário já agendado.

## Tema por região
Mesma pergunta central não basta: adapte tema, exemplo e CTA à realidade de cada região.

- EUA, Europa e Austrália: custo em moeda forte, fuso, atendimento em português e como contratar do Brasil. CTA: CÂMBIO ou RAIO-X.
- Brasil: venda local, lead qualificado, WhatsApp, custo por venda e prova de operação. Não use o argumento de câmbio ou de custo em real. CTA: RAIO-X.
- A semana é uma rotação: nunca publique duas regiões iguais seguidas quando houver outra pendente, e varie o ângulo mesmo em temas parecidos.

## Cronograma
Siga `sistema/CRONOGRAMA.md` para data, horário, região e tema. Se um tema não puder ser sustentado com fonte, troque por outro da mesma região e informe no resumo.

## Dados da dashboard
Toda rodada regrava `sistema/instagram-metricas.json` com dados do Metricool, mantendo as chaves `fetchedAt`, `source`, `profile`, `followers`, `daily` (`d`, `followers`, `reach`, `views`), `posts` (`date`, `type`, `region`, `title`, `url`, `reach`, `views`, `likes`, `comments`, `saves`, `shares`) e `queue` (`date`, `time`, `type`, `region`, `title`). Não inclua directs, leads, nomes de pessoas nem dados de clientes: o repositório é público. Se o Metricool falhar, não apague o arquivo anterior.
