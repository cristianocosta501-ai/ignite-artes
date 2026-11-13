"""Renderiza HTML em PNG (posts) ou PDF (carrosséis).
Uso: python3 render.py png arquivo.html saida.png [largura altura]
     python3 render.py pdf saida.pdf pagina1.html pagina2.html ...
"""
import sys, pathlib
from playwright.sync_api import sync_playwright

mode = sys.argv[1]
with sync_playwright() as p:
    b = p.chromium.launch()
    if mode == "png":
        src, out = sys.argv[2], sys.argv[3]
        w, h = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (1080, 1350)
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
        pg.goto(pathlib.Path(src).resolve().as_uri()); pg.wait_for_timeout(400)
        pg.evaluate("document.fonts.ready")
        pg.screenshot(path=out, clip={"x": 0, "y": 0, "width": w, "height": h})
    else:
        out, pages = sys.argv[2], sys.argv[3:]
        parts = []
        for i, src in enumerate(pages):
            pg = b.new_page(viewport={"width": 1080, "height": 1350})
            pg.goto(pathlib.Path(src).resolve().as_uri()); pg.wait_for_timeout(300)
            pg.evaluate("document.fonts.ready")
            part = f"{out}.part{i:02d}.pdf"
            pg.pdf(path=part, width="1080px", height="1350px", print_background=True,
                   margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}, page_ranges="1")
            parts.append(part); pg.close()
        import subprocess, os
        subprocess.run(["pdfunite", *parts, out], check=True)
        for x in parts: os.remove(x)
    b.close()
