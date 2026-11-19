"""Conferencia automatica de layout de pecas e diagramas em HTML/SVG.
Uso: python3 conferir_layout.py peca.html --largura 1080 --altura 1350 [--topo 0 --base 0]
Marque no HTML:
  data-protegido  -> elemento que nada pode cobrir (ex.: o titulo)
  data-caixa      -> container cujo texto nao pode transbordar (em SVG, um <g> com o <rect> do no)
  data-livre      -> elemento que pode sobrepor outros de proposito (adesivo, selo)
Saida: lista de problemas; codigo 1 se houver algum.
"""
import argparse, sys, pathlib
from playwright.sync_api import sync_playwright

JS = r"""
([W, H, topo, base]) => {
  const vis = e => { const s = getComputedStyle(e); return s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0; };
  const caixa = e => { const r = e.getBoundingClientRect(); return {x:r.left, y:r.top, r:r.right, b:r.bottom, w:r.width, h:r.height}; };
  const nome = e => (e.textContent || e.tagName).trim().replace(/\s+/g,' ').slice(0, 40);
  const cruza = (a, b, folga=2) => Math.min(a.r,b.r)-Math.max(a.x,b.x) > folga && Math.min(a.b,b.b)-Math.max(a.y,b.y) > folga;
  const probs = [];
  const textos = [...document.querySelectorAll('body *')].filter(e => vis(e) &&
      [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()));
  for (const t of textos) {
    const c = caixa(t);
    if (c.w === 0) continue;
    if (c.x < -1 || c.y < -1 || c.r > W + 1 || c.b > H + 1) probs.push(`FORA DA AREA: "${nome(t)}"`);
    else if (c.y < topo || c.b > H - base) probs.push(`FORA DA AREA SEGURA: "${nome(t)}"`);
    const cx = t.closest('[data-caixa]');
    if (cx && cx !== t) { const k = caixa(cx.tagName.toLowerCase() === 'g' ? (cx.querySelector('rect') || cx) : cx);
      if (c.x < k.x - 1 || c.r > k.r + 1 || c.y < k.y - 1 || c.b > k.b + 1) probs.push(`TRANSBORDA A CAIXA: "${nome(t)}"`); }
  }
  for (let i = 0; i < textos.length; i++) for (let j = i + 1; j < textos.length; j++) {
    const a = textos[i], b = textos[j];
    if (a.contains(b) || b.contains(a) || a.closest('[data-livre]') || b.closest('[data-livre]')) continue;
    if (cruza(caixa(a), caixa(b))) probs.push(`TEXTO SOBRE TEXTO: "${nome(a)}" x "${nome(b)}"`);
  }
  const todos = [...document.querySelectorAll('body *')].filter(vis);
  for (const p of document.querySelectorAll('[data-protegido]')) {
    const cp = caixa(p);
    for (const e of todos) {
      if (p.contains(e) || e.contains(p) || e.closest('[data-livre]')) continue;
      if (p.compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING && cruza(caixa(e), cp, 4))
        probs.push(`COBRE O PROTEGIDO: <${e.tagName.toLowerCase()}> "${nome(e)}" sobre "${nome(p)}"`);
    }
  }
  return [...new Set(probs)];
}
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arquivo"); ap.add_argument("--largura", type=int, default=1080)
    ap.add_argument("--altura", type=int, default=1350)
    ap.add_argument("--topo", type=int, default=0); ap.add_argument("--base", type=int, default=0)
    a = ap.parse_args()
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pg = nav.new_page(viewport={"width": a.largura, "height": a.altura})
        pg.goto(pathlib.Path(a.arquivo).resolve().as_uri()); pg.wait_for_timeout(600)
        probs = pg.evaluate(JS, [a.largura, a.altura, a.topo, a.base])
        nav.close()
    for x in probs: print("-", x)
    print("OK, nada encontrado." if not probs else f"{len(probs)} problema(s).")
    sys.exit(1 if probs else 0)

if __name__ == "__main__":
    main()
