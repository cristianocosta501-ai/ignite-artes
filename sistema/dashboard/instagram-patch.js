const fs=require('fs'),path=require('path'),R=process.argv[2];
const rep=(f,a,b)=>{const p=path.join(R,f);let s=fs.readFileSync(p,'utf8');if(s.includes(b.slice(0,50))&&!a)return;if(!s.includes(a))throw new Error('nao achei em '+f+': '+a.slice(0,50));fs.writeFileSync(p,s.replace(a,()=>b))};
rep('server.js',"function payload() {",`const IG_URL = 'https://raw.githubusercontent.com/cristianocosta501-ai/ignite-artes/artes/sistema/instagram-metricas.json';
async function syncInstagram() {
  try {
    const r = await fetch(loadConfig().instagramDataUrl || IG_URL, { signal: AbortSignal.timeout(15000) });
    if (!r.ok) throw new Error('HTTP ' + r.status);
    const j = await r.json();
    if (!j || !Array.isArray(j.daily) || !Array.isArray(j.posts)) throw new Error('arquivo inválido');
    write(path.join(DATA, 'instagram.json'), j); state.instagramError = null;
  } catch (e) { state.instagramError = e.message; }
}
function payload() {`);
rep('server.js',"google: googlePayload(), ga4: ga4Payload(),","google: googlePayload(), ga4: ga4Payload(), instagram: read(path.join(DATA, 'instagram.json')), instagramError: state.instagramError || null,");
rep('server.js',"  syncGoogle(); syncGa4();\n","  syncGoogle(); syncGa4(); syncInstagram();\n  setInterval(syncInstagram, HOUR);\n");
rep('public/app.js',"if (h === 'ga4' || h.startsWith('ga4/')) return 'ga4';","if (h === 'ga4' || h.startsWith('ga4/')) return 'ga4'; if (h === 'instagram') return 'instagram';");
rep('public/app.js',"function renderPage() {",`function igHtml() {
  const g = S.data.instagram;
  if (!g) return '<section class="panel"><p class="note" style="margin:0">Aguardando os primeiros dados do Instagram da Ignite.</p></section>';
  const w = windowOf({ key: 'ig', tz: 'America/Sao_Paulo', daily: g.daily }), inW = (d) => d >= w.since && d <= w.until;
  const days = g.daily.filter((x) => inW(x.d)), posts = g.posts.filter((x) => inW(x.date)), inter = (p) => (p.likes || 0) + (p.comments || 0) + (p.saves || 0) + (p.shares || 0);
  const reach = posts.map((p) => p.reach).sort((a, b) => a - b), med = reach.length ? (reach.length % 2 ? reach[(reach.length - 1) / 2] : (reach[reach.length / 2 - 1] + reach[reach.length / 2]) / 2) : null;
  const kp = [['Seguidores', n(g.followers)], ['Alcance somado', n(sum(days, 'reach'))], ['Views', n(sum(days, 'views'))], ['Publicações', n(posts.length)], ['Alcance mediano por post', n(med, med % 1 ? 1 : 0)], ['Interações', n(posts.reduce((t, p) => t + inter(p), 0))], ['Comentários', n(sum(posts, 'comments'))], ['Compartilhamentos', n(sum(posts, 'shares'))]];
  const top = Math.max(1, ...days.map((x) => x.reach));
  const regions = [...new Set(posts.map((p) => p.region || 'Geral'))].map((r) => { const l = posts.filter((p) => (p.region || 'Geral') === r); return { r, c: l.length, reach: sum(l, 'reach'), shares: sum(l, 'shares') }; }).sort((a, b) => b.reach - a.reach);
  const rows = posts.slice().sort((a, b) => b.reach - a.reach);
  return \`<dl class="acct-kpis">\${kp.map(([t, v]) => \`<div><dt>\${esc(t)}</dt><dd>\${v}</dd></div>\`).join('')}</dl>
  <div class="acct-grid" style="--c:var(--instagram)"><section class="panel"><h2 style="margin-bottom:16px">Alcance por dia</h2>\${days.length ? \`<div class="ig-bars" role="img" aria-label="Alcance por dia">\${days.map((x) => \`<i title="\${fdate(x.d)}: \${n(x.reach)} de alcance, \${n(x.views)} views" style="height:\${Math.max(2, x.reach / top * 100)}%"></i>\`).join('')}</div><p class="note" style="margin:10px 0 0">\${fdate(days[0].d)} a \${fdate(days[days.length - 1].d)}. Pico de \${n(top)} em um dia.</p>\` : '<p class="empty">Sem dados neste período.</p>'}</section>
  <section class="panel"><h2 style="margin-bottom:16px">Resultado por região</h2>\${regions.length ? \`<div class="scroll"><table><thead><tr><th>Região</th><th>Posts</th><th>Alcance</th><th>Compart.</th></tr></thead><tbody>\${regions.map((x) => \`<tr><td>\${esc(x.r)}</td><td>\${n(x.c)}</td><td>\${n(x.reach)}</td><td>\${n(x.shares)}</td></tr>\`).join('')}</tbody></table></div>\` : '<p class="empty">Sem publicações neste período.</p>'}</section></div>
  <section class="panel"><h2 style="margin-bottom:16px">Publicações por alcance</h2>\${rows.length ? \`<div class="scroll"><table><thead><tr><th>Publicação</th><th>Data</th><th>Região</th><th>Alcance</th><th>Views</th><th>Curtidas</th><th>Coment.</th><th>Salvos</th><th>Compart.</th></tr></thead><tbody>\${rows.map((p) => \`<tr><td>\${p.url ? \`<a href="\${esc(p.url)}" target="_blank" rel="noopener">\${esc(p.title)}</a>\` : esc(p.title)}<small>\${esc(p.type)}</small></td><td>\${fdate(p.date)}</td><td>\${esc(p.region || 'Geral')}</td><td>\${n(p.reach)}</td><td>\${n(p.views)}</td><td>\${n(p.likes)}</td><td>\${n(p.comments)}</td><td>\${n(p.saves)}</td><td>\${n(p.shares)}</td></tr>\`).join('')}</tbody></table></div>\` : '<p class="empty">Sem publicações neste período.</p>'}</section>
  <section class="panel"><h2 style="margin-bottom:16px">Próximos agendados</h2>\${(g.queue || []).length ? \`<div class="scroll"><table><thead><tr><th>Publicação</th><th>Data</th><th>Hora</th><th>Formato</th><th>Região</th></tr></thead><tbody>\${g.queue.map((p) => \`<tr><td>\${esc(p.title)}</td><td>\${fdate(p.date)}</td><td>\${esc(p.time)}</td><td>\${esc(p.type)}</td><td>\${esc(p.region)}</td></tr>\`).join('')}</tbody></table></div>\` : '<p class="empty">Nada na fila.</p>'}</section>\`;
}
function renderPage() {`);
rep('public/app.js',"p === 'ga4' ? gaHtml() : accountHtml(acct(p));","p === 'ga4' ? gaHtml() : p === 'instagram' ? igHtml() : accountHtml(acct(p));");
rep('public/app.js',"if (p === 'google') bindGoogle(); else if (p === 'ga4') bindGa(); else renderTabs();","if (p === 'google') bindGoogle(); else if (p === 'ga4') bindGa(); else if (p !== 'instagram') renderTabs();");
rep('public/app.js',"p === 'ga4' ? (aSelected() ? `${aSelected().name} no GA4` : 'Google Analytics 4') : `${acct(p).name} no Meta Ads`;","p === 'ga4' ? (aSelected() ? `${aSelected().name} no GA4` : 'Google Analytics 4') : p === 'instagram' ? 'Ignite no Instagram' : `${acct(p).name} no Meta Ads`;");
rep('public/app.js',"const plat = p === 'google' ? 'google' : p === 'ga4' ? 'ga4' : 'meta', hash","const plat = p === 'google' ? 'google' : p === 'ga4' ? 'ga4' : p === 'instagram' ? 'instagram' : 'meta', hash");
rep('public/app.js',"ga4: 'GA4' }[plat]}","ga4: 'GA4', instagram: 'Instagram Ignite' }[plat]}");
rep('public/app.js',"['ga4', 'ga4', 'GA4']]","['ga4', 'ga4', 'GA4'], ['instagram', 'instagram', 'Instagram Ignite']]");
rep('public/app.js',"  if (p === 'ga4') {\n    const ga = d.ga4","  if (p === 'instagram') {\n    const ig = d.instagram, iw = ig && ig.fetchedAt ? new Date(ig.fetchedAt).toLocaleString('pt-BR', { day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit' }) : null;\n    $('#status').textContent = iw ? `Dados de ${iw}, vindos do Metricool. Atualizados uma vez por dia.${d.instagramError ? ' A última leitura falhou e os dados anteriores continuam na tela.' : ''}` : 'Aguardando a primeira leitura.';\n  } else if (p === 'ga4') {\n    const ga = d.ga4");
rep('public/app.js',"  if (page() === 'ga4') return ensureGaRange();","  if (page() === 'ga4') return ensureGaRange();\n  if (page() === 'instagram') return;");
let css=path.join(R,'public/style.css'),c=fs.readFileSync(css,'utf8');
if(!c.includes('--instagram')){c=c.replace(/--ga4:#eda100;/,'--ga4:#eda100;--instagram:#d9480f;').replace(/--ga4:#c98500;/g,'--ga4:#c98500;--instagram:#fa581a;');c+="\n.ig-bars{display:flex;align-items:flex-end;gap:2px;height:210px;border-bottom:1px solid var(--line)}.ig-bars i{flex:1 1 0;min-width:2px;background:var(--instagram);border-radius:3px 3px 0 0}\n";fs.writeFileSync(css,c)}
let rd=path.join(R,'README.txt'),t=fs.readFileSync(rd,'utf8');
if(!t.includes('INSTAGRAM DA IGNITE')){t=t.replace('A dashboard só lê dados',"INSTAGRAM DA IGNITE\nA aba Instagram Ignite lê um resumo do Metricool salvo uma vez por dia no repositório público ignite-artes. Ela não usa token e não altera nada no Instagram.\n\nA dashboard só lê dados");fs.writeFileSync(rd,t)}
console.log('ok');
