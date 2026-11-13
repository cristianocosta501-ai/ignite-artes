"""Transforma uma peça estática (HTML do sistema 'criador') em vídeo curto com entrada dos elementos.
Uso: python3 motion.py peca.html saida.mp4 [duracao_s]
Ordem de entrada: chip, logo, título, apoio, etiquetas, cartões, cena (.ab/.ph), blocos, pílula, rodapé."""
import sys, pathlib, subprocess, tempfile, json, numpy as np
from playwright.sync_api import sync_playwright
from scipy.io import wavfile

src, out = sys.argv[1], sys.argv[2]
DUR = float(sys.argv[3]) if len(sys.argv) > 3 else 12.0
FPS = 30
JS = """
() => {
  const q = s => [...document.querySelectorAll(s)];
  const plan = []; let t = 150;
  const add = (els, gap, kf, dur=460) => els.forEach(e => { plan.push([e, t, kf, dur]); t += gap; });
  const pop = [{opacity:0, scale:'.7', translate:'0 34px'}, {opacity:1, scale:'1', translate:'0 0'}];
  const rise = [{opacity:0, translate:'0 70px'}, {opacity:1, translate:'0 0'}];
  const side = [{opacity:0, translate:'380px 60px'}, {opacity:1, translate:'0 0'}];
  const up = [{translate:'0 100%'}, {translate:'0 0'}];
  add(q('.chipt'), 150, pop); add(q('.logo'), 300, pop);
  add(q('.big'), 420, rise, 560); add(q('.sub'), 700, rise, 520);
  add(q('.org'), 250, up, 700);
  add(q('.tagw'), 380, pop); t += 250;
  add(q('.tc'), 450, pop); t += 150;
  add(q('.fr > .ab, .fr > .ph'), 900, side, 800);
  add(q('.blk'), 480, pop); t += 250;
  add(q('.pill'), 450, pop); add(q('.foot'), 0, rise);
  const times = [];
  plan.forEach(([e, d, kf, dur]) => { const a = e.animate(kf, {duration: dur, delay: d, fill: 'both', easing: 'cubic-bezier(.2,1.25,.35,1)'}); a.pause(); times.push(d); });
  window.__seek = ms => document.getAnimations().forEach(a => a.currentTime = ms);
  return times;
}"""
tmp = tempfile.mkdtemp()
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    pg.goto(pathlib.Path(src).resolve().as_uri()); pg.wait_for_timeout(400); pg.evaluate("document.fonts.ready")
    times = pg.evaluate(JS)
    for i in range(int(DUR * FPS)):
        pg.evaluate(f"window.__seek({i * 1000 / FPS})")
        pg.screenshot(path=f"{tmp}/f{i:04d}.jpg", type="jpeg", quality=93)
    b.close()

# trilha sintetizada simples: batida suave desde o segundo 0 + 'pop' em cada entrada
SR = 44100; N = int(SR * DUR); mix = np.zeros(N); rng = np.random.default_rng(3)
def add(sig, t, g):
    i = int(t * SR); sig = sig[:max(0, N - i)]; mix[i:i + len(sig)] += sig * g
def env(n, a, d):
    t = np.arange(n) / SR; return np.minimum(t / a, 1) * np.exp(-t / d)
def kick():
    n = int(.4 * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * np.cumsum(46 + 100 * np.exp(-t * 26)) / SR) * env(n, .001, .15)
def hat():
    n = int(.08 * SR); x = rng.standard_normal(n); x = x - np.convolve(x, np.ones(8) / 8, "same"); return x * env(n, .0005, .025)
def pop(f=420):
    n = int(.22 * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * (f + 600 * np.exp(-t * 30)) * t) * env(n, .001, .06)
def pad(fr, d):
    n = int(d * SR); t = np.arange(n) / SR; s = sum(np.sin(2 * np.pi * f * t) + .3 * np.sin(4 * np.pi * f * t) for f in fr) / len(fr)
    return s * np.clip(np.minimum(t / .5, 1) * np.minimum((d - t) / .5, 1), 0, 1)
B = .5
for i in range(int(DUR / B)):
    add(kick(), i * B, .7); add(hat(), i * B + B / 2, .12)
for k, t0 in enumerate(np.arange(0, DUR, 4)):
    add(pad([[220, 261.6, 329.6], [174.6, 220, 261.6], [196, 246.9, 293.7]][k % 3], min(4, DUR - t0)), t0, .16)
for k, ms in enumerate(times): add(pop(380 + 40 * (k % 5)), ms / 1000, .5)
mix = np.tanh(mix * 1.1); fade = np.ones(N); fl = int(.8 * SR); fade[-fl:] = np.linspace(1, 0, fl); mix *= fade; mix /= max(1e-9, np.abs(mix).max()) / .85
wavfile.write(f"{tmp}/a.wav", SR, (mix * 32767).astype(np.int16))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{tmp}/f%04d.jpg", "-i", f"{tmp}/a.wav",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
                "-map_metadata", "-1", "-movflags", "+faststart", "-shortest", out], check=True)
print(out, json.dumps(times))
