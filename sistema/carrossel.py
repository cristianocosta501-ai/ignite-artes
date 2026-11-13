import sys, pathlib, subprocess, tempfile, os
from playwright.sync_api import sync_playwright
out, pages = sys.argv[1], sys.argv[2:]
tmp = tempfile.mkdtemp(); pngs = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for i, src in enumerate(pages):
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        pg.goto(pathlib.Path(src).resolve().as_uri()); pg.wait_for_timeout(300); pg.evaluate("document.fonts.ready")
        f = f"{tmp}/{i:02d}.png"; pg.screenshot(path=f); pngs.append(f); pg.close()
    b.close()
# JPEG alta qualidade para manter o PDF leve
jpgs = []
from PIL import Image
for f in pngs:
    j = f.replace(".png", ".jpg"); Image.open(f).convert("RGB").save(j, quality=92, subsampling=0); jpgs.append(j)
subprocess.run(["img2pdf", "--pagesize", "1080x1350", "-o", out, *jpgs], check=True)
print(out, os.path.getsize(out))
