#!/usr/bin/env bash
# ============================================================
#  VC_Smooth - instalador para Linux
#  Baixa o Blender, aplica o patch e compila. Rode uma vez:
#      bash instalar_linux.sh
#  Requisitos: git, cmake, gcc/g++ (sudo apt install build-essential cmake git)
# ============================================================
set -e
BASE_COMMIT=08bed5b5b42ec017e8dcc87b76f6c373c322b086
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PATCH="$SCRIPT_DIR/zbrush-style-smooth.patch"

[ -f "$PATCH" ] || { echo "[ERRO] zbrush-style-smooth.patch precisa estar na mesma pasta."; exit 1; }
command -v git >/dev/null || { echo "[ERRO] git nao encontrado."; exit 1; }

mkdir -p "$HOME/blender-vc"
cd "$HOME/blender-vc"
if [ ! -d blender ]; then
  echo "[1/4] Clonando o Blender..."
  git clone https://projects.blender.org/blender/blender.git blender
fi
cd blender

echo "[2/4] Fixando na versao base do patch..."
git fetch origin "$BASE_COMMIT" 2>/dev/null || true
git checkout "$BASE_COMMIT" || echo "[AVISO] Sem o commit base; seguindo com a versao atual."

echo "[3/4] Aplicando o patch VC_Smooth..."
git apply --check "$PATCH" && git apply "$PATCH" || {
  echo "[ERRO] O patch nao aplicou nesta versao. Me avisa que eu regenero."; exit 1; }

echo "[4/4] Baixando bibliotecas e compilando (30-90 min na primeira vez)..."
make update
make

echo
echo "============================================================"
echo " PRONTO! Blender modificado em: $HOME/blender-vc/build_linux/bin/blender"
echo " Agora importe o brush: veja o README (passo 'Importar o brush')."
echo "============================================================"
