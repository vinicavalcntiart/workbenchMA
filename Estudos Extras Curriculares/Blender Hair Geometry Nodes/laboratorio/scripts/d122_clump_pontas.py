"""Diagrama: Curve Info -> Random -> Map Range -> Factor do Clump (visual do editor do Blender)."""
import os, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, PathPatch
from matplotlib.path import Path
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img", "122_clump_pontas_nodes.png")
BG, BODY, INK, MUTED = "#1d1d1d", "#303030", "#e6e6e6", "#9a9a9a"
HEAD = {"group": "#1d5c55", "conv": "#246283", "geo": "#1d725e", "input": "#83314a"}
SOCK = {"geo": "#00d6a3", "float": "#a1a1a1"}
fig, ax = plt.subplots(figsize=(14, 7.4), dpi=120, facecolor=BG); ax.set_facecolor(BG)
ax.set_xlim(0, 140); ax.set_ylim(-20, 56); ax.axis("off")
def node(x, y, w, title, kind, rows):
    h = 4 + 3.4*len(rows)
    ax.add_patch(FancyBboxPatch((x, y-h), w, h, boxstyle="round,pad=0,rounding_size=0.8", fc=BODY, ec="#111", lw=1))
    ax.add_patch(FancyBboxPatch((x, y-3.4), w, 3.4, boxstyle="round,pad=0,rounding_size=0.8", fc=HEAD[kind], ec="none"))
    ax.text(x+1.2, y-1.75, title, color=INK, fontsize=10, va="center", weight="bold")
    pos = {}
    for i, (label, side, st) in enumerate(rows):
        yy = y - 5.6 - 3.4*i
        if side == "field":
            ax.add_patch(FancyBboxPatch((x+1, yy-1.2), w-2, 2.4, boxstyle="round,pad=0,rounding_size=0.4", fc="#222", ec="#444"))
            ax.text(x+2, yy, label, color=INK, fontsize=9, va="center"); continue
        if side == "value":
            ax.add_patch(FancyBboxPatch((x+1, yy-1.2), w-2, 2.4, boxstyle="round,pad=0,rounding_size=0.4", fc="#545454", ec="none"))
            a, b = label; ax.text(x+2.2, yy, a, color=INK, fontsize=9, va="center"); ax.text(x+w-2.2, yy, b, color=INK, fontsize=9, va="center", ha="right")
            ax.plot(x, yy, marker="o", ms=6, color=SOCK["float"], mec="#111", zorder=5); continue
        sx = x + w if side == "out" else x
        ax.plot(sx, yy, marker="s" if st == "geo" else "o", ms=6, color=SOCK[st], mec="#111", zorder=5)
        ax.text(x + w - 1.3 if side == "out" else x + 1.3, yy, label, color=INK if label not in ("Factor",) else "#ffb347",
                fontsize=9, va="center", ha="right" if side == "out" else "left", weight="bold" if label == "Factor" else "normal")
        pos[label + side] = (sx, yy)
    return pos
def wire(a, b, color, dash=False):
    (x1, y1), (x2, y2) = a, b; d = (x2 - x1)*0.5
    p = Path([(x1, y1), (x1+d, y1), (x2-d, y2), (x2, y2)], [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])
    ax.add_patch(PathPatch(p, fc="none", ec=color, lw=2, ls=(0, (3, 2)) if dash else "-", zorder=2))

sp = node(2, 52, 24, "Spline Parameter", "input", [("Factor", "out", "float")])
m1 = node(32, 52, 24, "Map Range", "conv", [("Result", "out", "float"), ("Value", "in", "float"),
     (("From Min", "0,600"), "value", None), (("From Max", "1,000"), "value", None), (("To Min", "0,000"), "value", None), (("To Max", "1,000"), "value", None)])
ci = node(2, 20, 24, "Curve Info", "group", [("Random", "out", "float")])
m2 = node(32, 20, 24, "Map Range", "conv", [("Result", "out", "float"), ("Value", "in", "float"),
     (("From Min", "0,000"), "value", None), (("From Max", "1,000"), "value", None), (("To Min", "0,300"), "value", None), (("To Max", "1,000"), "value", None)])
mx = node(64, 40, 22, "Mix", "conv", [("Result", "out", "float"), ("Float", "field", None), ("Factor", "in", "float"), (("A", "1,000"), "value", None), ("B", "in", "float")])
cl = node(96, 52, 28, "Clump Hair Curves", "group", [("Geometry", "out", "geo"), ("Geometry", "in", "geo"), ("Factor", "in", "float"),
     (("Shape", "0,500"), "value", None), (("Tip Spread", "0 m"), "value", None)])
wire(sp["Factorout"], m1["Valuein"], SOCK["float"], dash=True); wire(ci["Randomout"], m2["Valuein"], SOCK["float"], dash=True)
wire(m1["Resultout"], mx["Factorin"], SOCK["float"], dash=True); wire(m2["Resultout"], mx["Bin"], SOCK["float"], dash=True)
wire(mx["Resultout"], cl["Factorin"], SOCK["float"], dash=True)
ax.text(2, -12, "Spline Parameter: 0 na raiz, 1 na ponta. Map Range 0,6 a 1,0 = mascara so nos ultimos 40% do fio (0 no corpo, 1 na ponta).", color=MUTED, fontsize=9.5)
ax.text(2, -14.8, "Mix: no corpo usa A = 1 (mecha fechada); na ponta usa B = Random 0,3 a 1,0 por fio (cada ponta solta de um jeito).", color=MUTED, fontsize=9.5)
ax.text(2, -17.6, "Clump Factor e avaliado por ponto dentro do grupo, por isso aceita a mascara ao longo do fio.", color=MUTED, fontsize=9.5)
fig.savefig(OUT, facecolor=BG, bbox_inches="tight", pad_inches=0.25); print("OK")
