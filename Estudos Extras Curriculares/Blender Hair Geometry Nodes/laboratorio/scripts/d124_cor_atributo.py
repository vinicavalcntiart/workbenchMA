"""Diagrama: Curve Info -> Random -> Map Range -> Factor do Clump (visual do editor do Blender)."""
import os, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, PathPatch
from matplotlib.path import Path
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img", "124_cor_atributo_nodes.png")
BG, BODY, INK, MUTED = "#1d1d1d", "#303030", "#e6e6e6", "#9a9a9a"
HEAD = {"group": "#1d5c55", "conv": "#246283", "geo": "#1d725e", "input": "#83314a", "shader": "#2a6e2a"}
SOCK = {"geo": "#00d6a3", "float": "#a1a1a1", "col": "#c7c729", "str": "#70b2ff", "sh": "#63c763"}
fig, ax = plt.subplots(figsize=(14, 7.2), dpi=120, facecolor=BG); ax.set_facecolor(BG)
ax.set_xlim(0, 142); ax.set_ylim(-17, 60); ax.axis("off")
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

ax.text(2, 58, "GEOMETRY NODES", color=MUTED, fontsize=10, weight="bold"); ax.text(94, 58, "SHADER (material do cabelo)", color=MUTED, fontsize=10, weight="bold")
ci = node(2, 54, 22, "Curve Info", "group", [("Random", "out", "float")])
sp = node(2, 40, 22, "Spline Parameter", "input", [("Factor", "out", "float")])
ax.text(3, 31.5, "use um ou outro:\nRandom = cor por fio\nSpline Parameter = raiz > ponta", color=MUTED, fontsize=8.5, va="top")
cr = node(30, 54, 22, "Color Ramp", "conv", [("Color", "out", "col"), ("Fac", "in", "float")])
st = node(58, 54, 30, "Store Named Attribute", "geo", [("Color", "field", None), ("Spline  (ou Point)", "field", None), ("Geometry", "out", "geo"), ("Geometry", "in", "geo"), ("Name", "in", "str"), ("Value", "in", "col")])
ax.text(59.3, 26.4, "Name = cor", color="#ffb347", fontsize=9)
at = node(94, 40, 18, "Attribute", "input", [("Geometry", "field", None), ("cor", "field", None), ("Color", "out", "col")])
hb = node(116, 54, 24, "Principled Hair BSDF", "shader", [("Direct Coloring", "field", None), ("BSDF", "out", "sh"), ("Color", "in", "col")])
wire(ci["Randomout"], cr["Facin"], SOCK["float"], dash=True); wire(sp["Factorout"], cr["Facin"], SOCK["float"], dash=True)
wire(cr["Colorout"], st["Valuein"], SOCK["col"], dash=True); wire(at["Colorout"], hb["Colorin"], SOCK["col"], dash=True)
ax.annotate("", xy=(93, 30), xytext=(88, 40), arrowprops=dict(arrowstyle="-|>", color="#ffb347", lw=1.5, ls=(0, (2, 2))))
ax.text(2, -10, "Tipo Color no Store. Dominio Spline = uma cor por fio; Point = varia ao longo do fio. Testado depois do Interpolate e do Clump, antes do Profile.", color=MUTED, fontsize=9)
ax.text(2, -13, "No material: Attribute com Type Geometry e o mesmo nome. Direct Coloring clareia a cor: escolha tons mais escuros do que o desejado.", color=MUTED, fontsize=9)
fig.savefig(OUT, facecolor=BG, bbox_inches="tight", pad_inches=0.25); print("OK")
