"""Um cartao por brush: curva de falloff (como o widget do Blender, com os pontos para copiar),
dab isolado, traco, e o corte do traco comparado com o dab. Usa as formulas de brush_soft_sim.py."""
import os, math, numpy as np
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "brush_soft_sim.py")).read().split("V = [")[0]
exec(src)
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
CARDS = os.path.join(OUT, "cards"); os.makedirs(CARDS, exist_ok=True)
BG, PANEL, GRID, INK, MUTED, CURVE, ACC = "#232325", "#161618", "#3a3a3e", "#ececec", "#9c9ca3", "#e8e8e8", "#f0a33a"
plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": INK, "axes.labelcolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.edgecolor": GRID})

def prof(kind, strength=1.0, spacing=10, accumulate=False, atten=False, peak=1.0, **_):
    fd0 = falloff_fn(kind); fd = lambda d: peak*fd0(d)
    af = overlap(fd, spacing) if (accumulate and atten) else 1.0
    step = 2*spacing/100.0; xs = np.arange(-1.2, 1.2+1e-9, step); ys = np.linspace(0, 1, 101); out = []
    for y in ys:
        acc = 0.0
        for x in xs:
            f = fd(math.hypot(x, y)); acc = min(acc + strength*f*af, 1.0) if accumulate else max(acc, acc*(1-f) + strength*f)
        out.append(acc)
    return ys, np.array(out), np.array([strength*fd(y) if not accumulate else fd(y) for y in ys])

def fmt(v): return f"{v:.2f}".replace(".", ",")

def card(i, name, settings, kind, pts=None, **kw):
    fig = plt.figure(figsize=(13, 3.0), dpi=110, facecolor=BG)
    gs = GridSpec(1, 4, width_ratios=[1.15, 0.85, 2.3, 1.2], left=0.035, right=0.975, top=0.68, bottom=0.17, wspace=0.18)
    fig.text(0.035, 0.91, name, fontsize=15, weight="bold", color=INK)
    fig.text(0.035, 0.815, settings, fontsize=10.5, color=MUTED)
    # 1. falloff, como no widget: esquerda = centro do brush, direita = borda
    ax = fig.add_subplot(gs[0]); ax.set_facecolor(PANEL)
    fd = falloff_fn(kind); peak = kw.get("peak", 1.0)
    xs = np.linspace(0, 1, 301); ys = [peak*fd(x) for x in xs]
    ax.plot(xs, ys, color=CURVE, lw=2, solid_capstyle="round")
    if pts:
        for j, (px, py) in enumerate(pts):
            ax.plot(px, py*peak, "o", ms=7, mfc="white", mec=PANEL, mew=2, zorder=3)
            if (px, py) == (1.0, 0.0): continue   # ponto final e sempre 1; 0
            left = px > 0.55
            ax.annotate(f"{fmt(px)}; {fmt(py)}", (px, py*peak), textcoords="offset points",
                        xytext=(-9, -3 - 11*(j % 2)) if left else (9, 3), ha="right" if left else "left", va="center",
                        fontsize=8, color=INK, zorder=4, bbox=dict(boxstyle="round,pad=0.15", fc=PANEL, ec="none", alpha=0.9))
    ax.set_xlim(-0.02, 1.02); ax.set_ylim(-0.03, 1.08); ax.set_xticks([0, 0.5, 1]); ax.set_yticks([0, 0.5, 1])
    ax.set_xticklabels(["centro", "0,5", "borda"], fontsize=8); ax.set_yticklabels(["0", "0,5", "1"], fontsize=8)
    ax.grid(color=GRID, lw=0.6); ax.set_title("Falloff" + (" (Custom)" if pts else ""), fontsize=9.5, color=MUTED, loc="left")
    for s in ax.spines.values(): s.set_visible(False)
    # 2. dab isolado
    ax = fig.add_subplot(gs[1]); n = 161; g = np.linspace(-1.15, 1.15, n); X, Y = np.meshgrid(g, g); D = np.hypot(X, Y)
    lut_d = np.linspace(0, 1, 1001); lut = np.array([peak*fd(d) for d in lut_d])
    dab = np.where(D < 1, np.interp(np.minimum(D, 1), lut_d, lut), 0) * (kw.get("strength", 1.0) if not kw.get("accumulate") else 1.0)
    ax.imshow(1 - 0.92*dab, cmap="gray", vmin=0, vmax=1, interpolation="bilinear")
    ax.set_xticks([]); ax.set_yticks([]); ax.set_title("Um dab", fontsize=9.5, color=MUTED, loc="left")
    for s in ax.spines.values(): s.set_visible(False)
    # 3. traco
    ax = fig.add_subplot(gs[2]); a = stroke(kind, **kw)
    ax.imshow(1 - 0.92*a, cmap="gray", vmin=0, vmax=1, interpolation="bilinear", aspect="auto")
    ax.set_xticks([]); ax.set_yticks([]); ax.set_title("Traço", fontsize=9.5, color=MUTED, loc="left")
    for s in ax.spines.values(): s.set_visible(False)
    # 4. corte do traco x dab
    ax = fig.add_subplot(gs[3]); ax.set_facecolor(PANEL)
    ys_, st, db = prof(kind, **kw); c = st[0] if st[0] > 0 else 1
    ax.plot(ys_, db, color=MUTED, lw=1.6, ls=(0, (4, 3)), label="dab")
    ax.plot(ys_, st, color=ACC, lw=2.2, label="traço")
    w, y50, cc = profile1d(kind, **kw)
    ax.set_xlim(0, 1); ax.set_ylim(-0.03, 1.08); ax.set_xticks([0, 0.5, 1]); ax.set_yticks([0, 0.5, 1])
    ax.set_xticklabels(["meio", "0,5 R", "borda"], fontsize=8); ax.set_yticklabels(["0", "0,5", "1"], fontsize=8)
    ax.grid(color=GRID, lw=0.6); ax.legend(loc="lower left", fontsize=8, frameon=False, labelcolor=INK)
    ax.set_title(f"Corte do traço · borda {fmt(w)} R", fontsize=9.5, color=MUTED, loc="left")
    for s in ax.spines.values(): s.set_visible(False)
    p = os.path.join(CARDS, f"{i:02d}_{name.split(' (')[0].lower().replace(' ', '_').replace(',', '').replace('ã','a')}.png")
    fig.savefig(p, facecolor=BG); plt.close(fig); print("CARD", p, w, y50, cc); return p

SMOOTH_PTS = [(0.0,1.0),(0.25,0.94),(0.75,0.06),(1.0,0.0)]
CAUDA = [(0.0,1.0),(0.25,0.45),(0.6,0.1),(1.0,0.0)]
def hard(h): return [(round(h + x*(1-h), 3), y) for x,y in SMOOTH_PTS]
B = [
 ("Paint Soft (Essentials, padrão)", "Falloff Smooth · Strength 1 · Spacing 10% · Accumulate desligado", "SMOOTH", None, {}),
 ("Paint Hard (Essentials, padrão)", "Falloff Custom · Strength 1 · Spacing 10% · Accumulate desligado", [(0.75,1.0),(0.81,0.95),(0.96,0.06),(1.0,0.0)], [(0.75,1.0),(0.81,0.95),(0.96,0.06),(1.0,0.0)], {}),
 ("Soft Round", "Falloff Smooth · Strength 1 · Spacing 5% · Accumulate + Adjust Strength for Spacing", "SMOOTH", None, dict(accumulate=True, atten=True, spacing=5)),
 ("Airbrush", "Falloff Custom (cauda longa) · Spacing 5% · Accumulate + Adjust Strength for Spacing", CAUDA, CAUDA, dict(accumulate=True, atten=True, spacing=5)),
 ("Hardness 0,5", "Falloff Custom · Strength 1 · Spacing 10% · Accumulate desligado", hard(0.5), hard(0.5), {}),
 ("Hardness 0,8", "Falloff Custom · Strength 1 · Spacing 10% · Accumulate desligado", hard(0.8), hard(0.8), {}),
 ("Hardness 0,8 com Accumulate (não use)", "Falloff Custom · Spacing 5% · Accumulate + Adjust: a soma amacia qualquer curva", hard(0.8), hard(0.8), dict(accumulate=True, atten=True, spacing=5)),
]
paths = [card(i+1, *b[:4], **b[4]) for i, b in enumerate(B)]
from PIL import Image
ims = [Image.open(p) for p in paths]; W = ims[0].width; H = sum(im.height for im in ims)
S = Image.new("RGB", (W, H), BG); y = 0
for im in ims: S.paste(im, (0, y)); y += im.height
S.save(os.path.join(OUT, "brush_cards_sheet.jpg"), quality=90); print("SHEET ok")
