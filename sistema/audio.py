# -*- coding: utf-8 -*-
import sys, json, numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt
SR = 44100; D = 30.0; N = int(SR * D)
CUTS = [4.5, 9.0, 13.5, 18.0, 22.5]; LOGO = 27.0
mix = np.zeros((N, 2)); rng = np.random.default_rng(7)
def add(sig, t, gain=1.0, pan=0.0):
    i = int(t * SR)
    if i >= N: return
    sig = sig[: max(0, N - i)]
    l, r = np.sqrt(0.5 * (1 - pan)), np.sqrt(0.5 * (1 + pan))
    mix[i:i + len(sig), 0] += sig * gain * l; mix[i:i + len(sig), 1] += sig * gain * r
def env(n, a=0.002, d=0.2):
    t = np.arange(n) / SR; return np.minimum(t / a, 1) * np.exp(-t / d)
def filt(x, kind, f): return sosfilt(butter(2, f, kind, fs=SR, output="sos"), x)
def kick():
    n = int(.45 * SR); t = np.arange(n) / SR; f = 45 + 110 * np.exp(-t * 28)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, .001, .16)
def hat(dec=.04):
    n = int(.12 * SR); return filt(rng.standard_normal(n), "highpass", 7000) * env(n, .0005, dec)
def clap():
    n = int(.25 * SR); x = filt(rng.standard_normal(n), "bandpass", [900, 2500])
    e = sum(env(n, .0005, .012) * (np.arange(n) >= int(k * SR)) for k in (0, .011, .022)) + env(n, .001, .09) * .6
    return x * e
def whoosh(dur=.45, up=True):
    n = int(dur * SR); x = rng.standard_normal(n); out = np.zeros(n); blk = 1024
    for s in range(0, n, blk):
        p = s / n; fc = 400 + 6000 * p + 300
        out[s:s + blk] = filt(x[s:s + blk], "bandpass", [fc * .7, min(fc * 1.4, 18000)])
    return out * np.sin(np.pi * np.linspace(0, 1, n)) ** 2
def tick():
    n = int(.03 * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * 2400 * t) * env(n, .0003, .006)
def pop():
    n = int(.25 * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * (300 + 700 * np.exp(-t * 30)) * t) * env(n, .001, .07)
def boom():
    n = int(2.2 * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * np.cumsum(38 + 80 * np.exp(-t * 6)) / SR) * env(n, .002, .7)
    return s + filt(rng.standard_normal(n), "lowpass", 3000) * env(n, .001, .25) * .5
def riser(dur=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    x = whoosh(dur, True) * np.linspace(0, 1, n) ** 2
    return x + np.sin(2 * np.pi * np.cumsum(200 + 900 * (t / dur) ** 2) / SR) * (t / dur) ** 3 * .25
def pad(freqs, dur):
    n = int(dur * SR); t = np.arange(n) / SR; s = np.zeros(n)
    for f in freqs:
        for det in (-.15, .15):
            ph = 2 * np.pi * f * (1 + det / 100) * t; s += (2 * (ph / (2 * np.pi) % 1) - 1)
    s = filt(s, "lowpass", 1400) / (len(freqs) * 2)
    return s * np.clip(np.minimum(t / .4, 1) * np.minimum((dur - t) / .4, 1), 0, 1)
def bass(f, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    return np.tanh(2 * np.sin(2 * np.pi * f * t)) * env(n, .005, dur * .6)
B = .5
prog = [([220, 261.6, 329.6], 55), ([174.6, 220, 261.6], 43.65),
        ([196, 261.6, 329.6], 65.4), ([196, 246.9, 293.7], 49)]
for k, t0 in enumerate([0, 4.5, 9.0, 13.5, 18.0, 22.5]):
    add(pad(prog[k % 4][0], min(4.5, LOGO - t0)), t0, .22)
add(pad(prog[0][0], D - LOGO), LOGO, .22)
for i in range(int(D / B)):
    t = i * B
    if LOGO - 1 <= t < LOGO: continue
    add(kick(), t, .9)
    if i % 2 == 1: add(clap(), t, .35)
    if i % 4 in (1, 3) and t < LOGO:
        add(bass(prog[int(t // 4.5) % 4][1], .45), t, .35)
    add(hat(), t + B / 2, .18, .3)
    if t >= CUTS[0]: add(hat(.02), t + B * .75, .1, -.3)
for c in CUTS: add(whoosh(.45), c - .3, .45)
cfg = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
for t0, n, step in cfg.get("ticks", [[0.35, 16, 0.042]]):
    for k in range(int(n)): add(tick(), t0 + k * step, .24)
for t0 in cfg.get("pops", []): add(pop(), t0, .7)
add(riser(1.0), LOGO - 1, .55); add(boom(), LOGO, 1.0); add(kick(), LOGO, 1.0)
mix = np.tanh(mix * 1.1) * .9
fade = np.ones(N); fl = int(.9 * SR); fade[-fl:] = np.linspace(1, 0, fl) ** 1.5
mix *= fade[:, None]; mix /= max(1e-9, np.abs(mix).max()) / .89
wavfile.write(sys.argv[1], SR, (mix * 32767).astype(np.int16))
