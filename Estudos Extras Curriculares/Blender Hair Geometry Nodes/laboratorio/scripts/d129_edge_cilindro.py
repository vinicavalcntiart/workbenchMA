"""Diagrama: Curve Info -> Random -> Map Range -> Factor do Clump (visual do editor do Blender)."""
import os, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, PathPatch
from matplotlib.path import Path
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img", "129_edge_cilindro_nodes.png")
BG, BODY, INK, MUTED = "#1d1d1d", "#303030", "#e6e6e6", "#9a9a9a"
HEAD = {"group": "#3c3c3c", "conv": "#246283", "geo": "#1d725e", "curve": "#2b5d7a"}
SOCK = {"geo": "#00d6a3", "float": "#a1a1a1", "int": "#35b57a"}
fig, ax = plt.subplots(figsize=(15, 6.2), dpi=120, facecolor=BG); ax.set_facecolor(BG)
ax.set_xlim(0, 152); ax.set_ylim(-10, 52); ax.axis("off")
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

gi = node(2, 48, 22, "Group Input", "group", [("Geometry", "out", "geo"), ("Raio", "out", "float"), ("Lados", "out", "int")])
m2c = node(30, 48, 22, "Mesh to Curve", "curve", [("Curve", "out", "geo"), ("Mesh", "in", "geo")])
cc = node(30, 28, 22, "Curve Circle", "curve", [("Radius", "field", None), ("Curve", "out", "geo"), ("Resolution", "in", "int"), ("Radius", "in", "float")])
c2m = node(60, 48, 26, "Curve to Mesh", "geo", [("Mesh", "out", "geo"), ("Curve", "in", "geo"), ("Profile Curve", "in", "geo"), (("Scale", "1,000"), "value", None), (("Fill Caps", "✓"), "value", None)])
ss = node(94, 48, 24, "Set Shade Smooth", "geo", [("Geometry", "out", "geo"), ("Geometry", "in", "geo")])
go = node(126, 48, 22, "Group Output", "group", [("Geometry", "in", "geo")])
wire(gi["Geometryout"], m2c["Meshin"], SOCK["geo"]); wire(m2c["Curveout"], c2m["Curvein"], SOCK["geo"])
wire(gi["Lados" + "out"], cc["Resolutionin"], SOCK["int"], dash=True); wire(gi["Raioout"], cc["Radiusin"], SOCK["float"], dash=True)
wire(cc["Curveout"], c2m["Profile Curvein"], SOCK["geo"]); wire(c2m["Meshout"], ss["Geometryin"], SOCK["geo"]); wire(ss["Geometryout"], go["Geometryin"], SOCK["geo"])
ax.text(2, -4, "Curve Circle = a secao do cilindro (Radius = grossura, Resolution = lados). Fill Caps fecha as pontas. Scale aceita campo: Spline Parameter > Map Range (1 > 0,2) afina o tubo.", color=MUTED, fontsize=9.3)
ax.text(2, -7.4, "Cantos vivos no tubo: entre Mesh to Curve e Curve to Mesh ponha Set Spline Type (Bezier) + Set Handle Type (Auto) + Resample Curve. Testado no Blender 5.2.0.", color=MUTED, fontsize=9.3)
fig.savefig(OUT, facecolor=BG, bbox_inches="tight", pad_inches=0.25); print("OK")
