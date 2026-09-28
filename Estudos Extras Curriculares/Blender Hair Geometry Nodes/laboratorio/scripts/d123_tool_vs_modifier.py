"""Tool x Modifier no Geometry Nodes: esquema visual."""
import os, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img", "123_tool_vs_modifier.png")
BG, BOX, INK, MUTED, MOD, TOOL = "#1d1d1d", "#2e2e30", "#ececec", "#a0a0a6", "#1d725e", "#b8612a"
fig, ax = plt.subplots(figsize=(13, 8.2), dpi=120, facecolor=BG); ax.set_facecolor(BG)
ax.set_xlim(0, 130); ax.set_ylim(0, 82); ax.axis("off")
def box(x, y, w, h, text, fc=BOX, ec="#444", fs=10, color=INK, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=1.2", fc=fc, ec=ec, lw=1.2))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs, color=color, weight="bold" if bold else "normal", linespacing=1.4)
def arrow(a, b, c):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=16, color=c, lw=2))
# titulos
box(2, 72, 60, 7, "MODIFIER  ·  o groom", fc=MOD, ec=MOD, fs=13, bold=True)
box(68, 72, 60, 7, "TOOL  ·  um comando", fc=TOOL, ec=TOOL, fs=13, bold=True)
# fluxos
box(2, 56, 17, 11, "Curvas\noriginais"); box(23, 56, 17, 11, "Modificador\nGN", ec=MOD); box(44, 56, 18, 11, "Resultado\nna tela e no render")
arrow((19, 61.5), (23, 61.5), MOD); arrow((40, 61.5), (44, 61.5), MOD)
ax.text(32, 52.5, "original intacto  ·  recalcula a cada mudança e a cada frame", ha="center", fontsize=9.5, color=MUTED)
box(68, 56, 17, 11, "Curvas\n(Edit Mode)"); box(89, 56, 17, 11, "Roda 1 vez\npelo menu", ec=TOOL); box(110, 56, 18, 11, "Curvas alteradas\nde verdade")
arrow((85, 61.5), (89, 61.5), TOOL); arrow((106, 61.5), (110, 61.5), TOOL)
ax.text(98, 52.5, "grava nos dados, como um pincel  ·  Ctrl+Z desfaz", ha="center", fontsize=9.5, color=MUTED)
# listas
mod = ["Interpolate, Clump, Curl, Noise, Profile", "Anima, simula (Simulation Zone), renderiza", "Tem Viewer e inspeção de valores", "Não enxerga seleção, mouse nem 3D Cursor"]
tool = ["Selection, Set Selection, Active Element", "Mouse Position, 3D Cursor, Viewport Transform", "Sem Viewer e sem Simulation Zone", "Precisa de Identifier, Types e Modes marcados"]
for i, t in enumerate(mod): ax.text(4, 44 - i*5, "•  " + t, fontsize=10.5, color=INK)
for i, t in enumerate(tool): ax.text(70, 44 - i*5, "•  " + t, fontsize=10.5, color=INK)
# juntos
box(2, 2, 126, 17, "", fc="#262628", ec="#555")
ax.text(65, 15.5, "No seu groom os dois trabalham juntos", ha="center", fontsize=12, color=INK, weight="bold")
box(8, 4.5, 34, 8, "TOOL: seleciona guias e grava\natributo Front_Guides_02_R", ec=TOOL, fs=9.5)
box(50, 4.5, 30, 8, "atributo Boolean\nno domínio Curve", fs=9.5)
box(88, 4.5, 34, 8, "MODIFIER: Named Attribute\nlê e usa a cada frame", ec=MOD, fs=9.5)
arrow((42, 8.5), (50, 8.5), TOOL); arrow((80, 8.5), (88, 8.5), MOD)
fig.savefig(OUT, facecolor=BG, bbox_inches="tight", pad_inches=0.2); print("OK")
