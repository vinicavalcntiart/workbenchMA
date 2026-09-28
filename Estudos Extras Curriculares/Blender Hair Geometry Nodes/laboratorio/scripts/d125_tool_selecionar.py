"""Diagrama do node tool 'Salvar Selecao' no visual do editor de nodes do Blender."""
import os, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.path import Path
from matplotlib.patches import PathPatch
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img", "125_tool_selecionar_conjunto.png")
BG, BODY, INK, MUTED = "#1d1d1d", "#303030", "#e6e6e6", "#9a9a9a"
HEAD = {"input": "#3c3c3c", "geo": "#1d725e", "attr": "#83314a", "out": "#3c3c3c", "obj": "#83314a"}
SOCK = {"geo": "#00d6a3", "bool": "#cca6d6", "str": "#70b2ff"}
fig, ax = plt.subplots(figsize=(12, 4.6), dpi=120, facecolor=BG); ax.set_facecolor(BG)
ax.set_xlim(0, 122); ax.set_ylim(0, 46); ax.axis("off")
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

gi = node(4, 40, 22, "Group Input", "input", [("Geometry", "out", "geo"), ("Nome", "out", "str")])
na = node(32, 22, 24, "Named Attribute", "attr", [("Boolean", "field", None), ("Attribute", "out", "bool"), ("Name", "in", "str")])
ss = node(64, 40, 26, "Set Selection", "geo", [("Spline", "field", None), ("Geometry", "out", "geo"), ("Geometry", "in", "geo"), ("Selection", "in", "bool")])
go = node(98, 40, 20, "Group Output", "out", [("Geometry", "in", "geo")])
wire(gi["Geometryout"], ss["Geometryin"], SOCK["geo"]); wire(gi["Nomeout"], na["Namein"], SOCK["str"])
wire(na["Attributeout"], ss["Selectionin"], SOCK["bool"], dash=True); wire(ss["Geometryout"], go["Geometryin"], SOCK["geo"])
ax.text(4, 3.2, "Options > Identifier: curves.selecionar_conjunto  ·  Types: Curves  ·  Modes: Edit e Sculpt  ·  Default do Nome: Back_Guides_01_R", color=MUTED, fontsize=9)
ax.text(4, 0.6, "Rodar pelo icone depois de Segments: seleciona so as guias do conjunto. Troque o Nome no redo para outro conjunto.", color=MUTED, fontsize=9)
fig.savefig(OUT, facecolor=BG, bbox_inches="tight", pad_inches=0.25); print("OK", OUT)
