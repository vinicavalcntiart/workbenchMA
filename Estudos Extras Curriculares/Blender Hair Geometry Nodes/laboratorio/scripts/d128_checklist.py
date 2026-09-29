"""Checklist: por que o tool do arquivo funciona e o do Vini nao."""
import os, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img", "128_checklist_tool.png")
BG, BOX, INK, MUTED, OK, BAD, WARN = "#1d1d1d", "#2a2a2c", "#ececec", "#a0a0a6", "#3fbf7f", "#ff6b5a", "#f0a33a"
rows = [
 ("Onde fica", "Editor de nodes no modo TOOL (dropdown no canto\nsuperior esquerdo) > seletor de data-block", "No modo Modifier o seletor so mostra o groom", WARN),
 ("Identifier", "Options > Identifier unico:\ncurves.selecionar_conjunto", "Copia de outro tool mantem o mesmo Identifier:\no Blender roda so o mais antigo", BAD),
 ("Fake User", "Ligado (escudo no seletor de data-block)", "Sem Fake User o tool nao e salvo no .blend", WARN),
 ("Types / Modes", "Curves  ·  Edit (e Sculpt)", "Sem Curves ou sem Edit, nao aparece no menu", WARN),
 ("Grafo de apagar", "Named Attribute no Selection do Separate;\nsaida Inverted", "Separate sem Selection: Inverted vazio,\napaga guias e atributos", BAD),
 ("Como rodar", "Edit Mode no Cabelo > icone depois de Segments\n> escolher o tool > trocar o Nome no redo", "Rodar fora do Edit Mode ou por outro menu", WARN),
]
fig, ax = plt.subplots(figsize=(13, 8.4), dpi=120, facecolor=BG); ax.set_facecolor(BG); ax.axis("off")
ax.set_xlim(0, 130); ax.set_ylim(0, 84)
ax.text(2, 80, "Por que o tool do arquivo funciona", color=INK, fontsize=16, weight="bold")
ax.text(2, 76.5, "Arquivo tools_conjuntos_guias.blend, testado no Blender 5.2.0: seleciona 57 de 57, apaga 313 → 256, atributos intactos", color=MUTED, fontsize=10)
ax.text(24, 72, "NO ARQUIVO (FUNCIONA)", color=OK, fontsize=10.5, weight="bold"); ax.text(80, 72, "O QUE QUEBRA", color=BAD, fontsize=10.5, weight="bold")
y = 69
for t, ok, bad, c in rows:
    ax.add_patch(FancyBboxPatch((1, y-9.2), 128, 9, boxstyle="round,pad=0,rounding_size=1", fc=BOX, ec="#3a3a3e"))
    ax.text(3, y-4.6, t, color=INK, fontsize=11, weight="bold", va="center")
    ax.plot(22.5, y-4.6, "o", ms=9, color=OK); ax.text(24.5, y-4.6, ok, color=INK, fontsize=9.6, va="center", linespacing=1.35)
    ax.plot(78.5, y-4.6, "o", ms=9, color=c); ax.text(80.5, y-4.6, bad, color=INK, fontsize=9.6, va="center", linespacing=1.35)
    y -= 10.3
ax.text(2, 3.5, "Vermelho = causa provavel do seu caso (atributos sumindo). Laranja = impede o tool de aparecer ou de ser salvo.", color=MUTED, fontsize=9.5)
fig.savefig(OUT, facecolor=BG, bbox_inches="tight", pad_inches=0.2); print("OK")
