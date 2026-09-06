#!/bin/sh
# Validacao REAL do docs/index.html: extrai os <script> e roda contra um DOM falso.
# node --check so pega erro de sintaxe; este script pega erro de execucao,
# que e o que apaga a pagina inteira no navegador (ex.: virgula faltando num array).
set -e
DIR=$(dirname "$0")
TMP=$(mktemp -d)

# PRIVACIDADE. O repositorio e PUBLICO e o telefone do Vini ja voltou a ele TRES
# vezes em 06/09, sempre por um agente diferente documentando qual valor tinha
# preenchido num formulario. Aviso escrito em BRIEF nao segurou, entao a checagem
# vira portao: todo commit ja passa por aqui.
DIRR="$(cd "$(dirname "$0")/.." && pwd)"
VAZOU=$(grep -rniE "97306.?2286|81973062286|\+?55[[:space:]-]?\(?81\)?[[:space:]-]?9?7306|Bonsucesso|53240-480" \
  --include="*.md" --include="*.csv" --include="*.html" --include="*.js" --include="*.txt" \
  "$DIRR" 2>/dev/null | grep -v "/.git/" || true)
if [ -n "$VAZOU" ]; then
  echo "FALHA DE PRIVACIDADE: telefone ou endereco residencial no repositorio publico."
  echo "$VAZOU" | cut -c1-160
  echo
  echo "Ao documentar um campo preenchido, escreva o NOME do campo e nunca o valor."
  echo "Telefone e endereco vivem so no doc privado do Drive."
  exit 1
fi

python3 - "$DIR/../docs/index.html" > "$TMP/app.js" <<'PY'
import re, sys
s = open(sys.argv[1], encoding='utf-8').read()
print("\n;\n".join(re.findall(r'<script[^>]*>(.*?)</script>', s, re.S)))
PY
cp "$DIR/valida-dashboard.js" "$TMP/stub.js"
(cd "$TMP" && node stub.js)

# Rodar sem lancar nao basta: uma entrada de NOVIDADES caida dentro do DAILY nao
# quebra a pagina, ela publica "19406porta6" no lugar do total de emails. Este
# segundo passo confere o formato de cada linha dos arrays de dados.
node "$DIR/valida-formato.mjs" "$DIR/../docs/index.html"
