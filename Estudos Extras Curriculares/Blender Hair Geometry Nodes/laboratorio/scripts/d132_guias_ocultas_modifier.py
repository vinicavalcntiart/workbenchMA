"""Diagrama do modificador Guias Ocultas (esconder guias sem addon) no visual do editor de nodes do Blender."""
import os, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.path import Path
from matplotlib.patches import PathPatch
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img", "132_guias_ocultas_modifier.png")
BG, BODY, INK, MUTED = "#1d1d1d", "#303030", "#e6e6e6", "#9a9a9a"
HEAD = {"input": "#3c3c3c", "geo": "#1d725e", "attr": "#83314a", "out": "#3c3c3c", "obj": "#83314a"}
SOCK = {"geo": "#00d6a3", "bool": "#cca6d6", "str": "#70b2ff", "int": "#598c5c", "obj": "#ed9e5c"}
fig, ax = plt.subplots(figsize=(13, 8.2), dpi=120, facecolor=BG); ax.set_facecolor(BG)
ax.set_xlim(0, 132); ax.set_ylim(0, 82); ax.axis("off")
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
        sx = x + w if side == "out" else x
        ax.plot(sx, yy, marker="D" if st == "bool" else ("s" if st == "geo" else "o"), ms=6, color=SOCK[st], mec="#111", zorder=5)
        ax.text(x + w - 1.3 if side == "out" else x + 1.3, yy, label, color=INK, fontsize=9, va="center", ha="right" if side == "out" else "left")
        pos[label + side] = (sx, yy)
    return pos
def wire(a, b, color, dash=False):
    (x1, y1), (x2, y2) = a, b; d = (x2 - x1)*0.5
    p = Path([(x1, y1), (x1+d, y1), (x2-d, y2), (x2, y2)], [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])
    ax.add_patch(PathPatch(p, fc="none", ec=color, lw=2, ls=(0, (3, 2)) if dash else "-", zorder=2))


ax.text(4, 79, "1. Gravar Ordem  (uma vez so: modificador no topo da stack e Apply)", color=INK, fontsize=12, weight="bold")
gi = node(4, 75, 20, "Group Input", "input", [("Geometry", "out", "geo")])
ix = node(30, 60, 16, "Index", "input", [("Index", "out", "int")])
st = node(52, 75, 30, "Store Named Attribute", "attr", [("Integer", "field", None), ("Spline", "field", None), ("Geometry", "out", "geo"), ("Geometry", "in", "geo"), ("Name: ordem", "field", None), ("Value", "in", "int")])
go = node(92, 75, 20, "Group Output", "out", [("Geometry", "in", "geo")])
wire(gi["Geometryout"], st["Geometryin"], SOCK["geo"]); wire(ix["Indexout"], st["Valuein"], SOCK["int"], dash=True); wire(st["Geometryout"], go["Geometryin"], SOCK["geo"])

ax.text(4, 44, "2. Guias Ocultas  (topo da stack, antes do Interpolate)", color=INK, fontsize=12, weight="bold")
gi2 = node(4, 40, 20, "Group Input", "input", [("Geometry", "out", "geo")])
oi = node(4, 28, 24, "Object Info", "geo", [("Original", "field", None), ("Geometry", "out", "geo"), ("Cabelo Guias Ocultas", "field", None)])
jn = node(34, 40, 20, "Join Geometry", "geo", [("Geometry", "out", "geo"), ("Geometry", "in", "geo")])
na = node(34, 20, 24, "Named Attribute", "attr", [("Integer", "field", None), ("Attribute", "out", "int"), ("Name: ordem", "field", None)])
so = node(64, 40, 24, "Sort Elements", "geo", [("Spline", "field", None), ("Geometry", "out", "geo"), ("Geometry", "in", "geo"), ("Selection", "in", "bool"), ("Group ID", "in", "int"), ("Sort Weight", "in", "int")])
go2 = node(98, 40, 20, "Group Output", "out", [("Geometry", "in", "geo")])
wire(gi2["Geometryout"], jn["Geometryin"], SOCK["geo"]); wire(oi["Geometryout"], jn["Geometryin"], SOCK["geo"])
wire(jn["Geometryout"], so["Geometryin"], SOCK["geo"]); wire(na["Attributeout"], so["Sort Weightin"], SOCK["int"], dash=True)
wire(so["Geometryout"], go2["Geometryin"], SOCK["geo"])
ax.text(4, 3.2, "Revelar: Apply no Guias Ocultas (volta tudo na ordem original) e apague o objeto Cabelo Guias Ocultas", color=MUTED, fontsize=10)
fig.savefig(OUT, facecolor=BG, bbox_inches="tight"); print(OUT)
