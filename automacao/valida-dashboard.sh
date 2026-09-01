#!/bin/sh
# Validacao REAL do docs/index.html: extrai os <script> e roda contra um DOM falso.
# node --check so pega erro de sintaxe; este script pega erro de execucao,
# que e o que apaga a pagina inteira no navegador (ex.: virgula faltando num array).
set -e
DIR=$(dirname "$0")
TMP=$(mktemp -d)
python3 - "$DIR/../docs/index.html" > "$TMP/app.js" <<'PY'
import re, sys
s = open(sys.argv[1], encoding='utf-8').read()
print("\n;\n".join(re.findall(r'<script[^>]*>(.*?)</script>', s, re.S)))
PY
cp "$DIR/valida-dashboard.js" "$TMP/stub.js"
cd "$TMP" && node stub.js
