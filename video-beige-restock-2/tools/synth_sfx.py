"""Synthesize the film's sound effects from scratch (no third-party samples).

Usage: python3 tools/synth_sfx.py assets/sfx
Writes 48 kHz stereo 16-bit WAVs, each peak-normalised to -3 dBFS.
Deterministic: every noise source uses a fixed seed.
"""
import sys, os, wave
import numpy as np

SR = 48000
OUT = sys.argv[1] if len(sys.argv) > 1 else "assets/sfx"
os.makedirs(OUT, exist_ok=True)


def t_axis(dur):
    return np.arange(int(SR * dur)) / SR


def noise(n, seed):
    return np.random.default_rng(seed).standard_normal(n)


def onepole_lp(x, fc):
    """Time-varying one-pole low-pass; fc may be an array (Hz)."""
    fc = np.broadcast_to(np.asarray(fc, dtype=float), x.shape)
    a = np.exp(-2 * np.pi * fc / SR)
    y = np.empty_like(x)
    s = 0.0
    for i in range(len(x)):
        s = (1 - a[i]) * x[i] + a[i] * s
        y[i] = s
    return y


def bandpass(x, lo, hi):
    return onepole_lp(x, hi) - onepole_lp(x, lo)


def env_ad(n, attack, decay_pow=2.0):
    a = int(n * attack)
    e = np.ones(n)
    e[:a] = np.linspace(0, 1, a) if a > 0 else 1
    e[a:] = np.linspace(1, 0, n - a) ** decay_pow
    return e


def save(name, mono, pan_width=0.0):
    mono = mono / (np.max(np.abs(mono)) + 1e-9) * 10 ** (-3 / 20)
    if pan_width:
        # tiny stereo spread via a short delay on the right channel
        d = int(SR * 0.004 * pan_width)
        r = np.concatenate([np.zeros(d), mono])[: len(mono)]
        st = np.stack([mono, r * 0.92 + mono * 0.08], axis=1)
    else:
        st = np.stack([mono, mono], axis=1)
    pcm = (np.clip(st, -1, 1) * 32767).astype(np.int16)
    with wave.open(os.path.join(OUT, name + ".wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    print("wrote", name, f"{len(mono)/SR:.2f}s")


# whoosh: band-passed noise whose centre sweeps up then down, swell to the middle
def whoosh(dur=0.55, f0=300, f1=2600, seed=1):
    t = t_axis(dur); n = len(t)
    sweep = f0 + (f1 - f0) * np.sin(np.pi * t / dur) ** 1.5
    x = bandpass(noise(n, seed), sweep * 0.5, sweep * 1.6)
    e = np.sin(np.pi * t / dur) ** 2.2
    return x * e


# swoosh: shorter, brighter, peaks early
def swoosh(dur=0.32, seed=2):
    t = t_axis(dur); n = len(t)
    sweep = 1500 + 5000 * (t / dur) ** 0.6
    x = bandpass(noise(n, seed), sweep * 0.6, sweep * 1.4)
    e = (t / dur) ** 0.4 * (1 - t / dur) ** 1.8
    return x * e


# pop: sine blip with fast pitch drop and a click transient
def pop(dur=0.14, f0=1400, f1=380):
    t = t_axis(dur)
    f = f1 + (f0 - f1) * np.exp(-t * 60)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * np.exp(-t * 32)
    x[: int(SR * 0.002)] += np.linspace(0.6, 0, int(SR * 0.002))
    return x


# ding: bell from inharmonic partials with long decay
def ding(dur=1.1, f=1568):
    t = t_axis(dur)
    parts = [(1, 1.0, 4.0), (2.76, 0.45, 6.5), (5.40, 0.25, 9.0), (8.93, 0.12, 13.0)]
    x = sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t * d) for r, a, d in parts)
    x *= np.minimum(1, t / 0.002)
    return x


# impact: sub drop + low thud + noise crack
def impact(dur=1.2):
    t = t_axis(dur); n = len(t)
    f = 45 + 110 * np.exp(-t * 18)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 3.2)
    crack = onepole_lp(noise(n, 3), 3500) * np.exp(-t * 28)
    x = sub * 1.0 + crack * 0.9
    x *= np.minimum(1, t / 0.0015)
    return np.tanh(x * 1.6)


# cha-ching: two quick metallic dings plus a noisy "drawer" rattle
def cha_ching():
    a = ding(0.5, 2093) * 0.8
    b = ding(1.1, 2637)
    rattle_t = t_axis(0.18)
    rattle = bandpass(noise(len(rattle_t), 4), 2500, 7000) * np.exp(-rattle_t * 25)
    out = np.zeros(int(SR * 1.3))
    out[: len(rattle)] += rattle * 0.6
    out[: len(a)] += a
    o = int(SR * 0.11)
    out[o : o + len(b)] += b[: len(out) - o]
    return out


# zap: fast descending FM sweep
def zap(dur=0.28):
    t = t_axis(dur)
    f = 2400 * np.exp(-t * 14) + 120
    mod = np.sin(2 * np.pi * 60 * t) * 4
    x = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR + mod)) * 0.6
    x = onepole_lp(x, 6000) * np.exp(-t * 9)
    return x


# riser: noise + rising tone, building to the end
def riser(dur=1.8, seed=5):
    t = t_axis(dur); n = len(t)
    f = 220 * 2 ** (3 * t / dur)
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR)
    nz = bandpass(noise(n, seed), 400 + 3000 * t / dur, 1500 + 7000 * t / dur)
    e = (t / dur) ** 2.4
    x = (tone * 0.5 + nz) * e
    x[-int(SR * 0.01):] *= np.linspace(1, 0, int(SR * 0.01))
    return x


# tick: short woody click
def tick(dur=0.05):
    t = t_axis(dur)
    x = np.sin(2 * np.pi * 3200 * t) * np.exp(-t * 180) + np.sin(2 * np.pi * 900 * t) * np.exp(-t * 120) * 0.5
    return x


save("whoosh", whoosh(), 1.0)
save("whoosh-low", whoosh(0.6, 180, 1600, seed=11), 1.0)
save("swoosh", swoosh(), 1.0)
save("pop", pop())
save("pop-high", pop(0.12, 2100, 700))
save("ding", ding())
save("impact", impact())
save("cha-ching", cha_ching())
save("zap", zap())
save("riser", riser())
save("tick", tick())
