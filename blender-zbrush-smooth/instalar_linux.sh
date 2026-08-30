#!/usr/bin/env bash
# ============================================================
#  VC_Smooth - instalador para Linux
#  Baixa o Blender, aplica o patch e compila. Rode uma vez:
#      bash instalar_linux.sh
#  Requisitos: git, cmake, gcc/g++ (sudo apt install build-essential cmake git)
# ============================================================
set -e
BASE_BRANCH=blender-v5.2-release
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

echo "[2/4] Mudando para o Blender 5.2 LTS..."
git fetch origin "$BASE_BRANCH"
git checkout -B vc-smooth "origin/$BASE_BRANCH"

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
