#!/bin/sh
# TRAVA DO STEALTH, criada em 24/09/2026 por ordem do Vini.
#
# REGRA: todo navegador desta campanha nasce pelo helper (automacao/navegador_kernel.js ou
# navegador_kernel.py), com stealth ligado e proxy padrao ligado. Regra escrita nao e trava,
# e pedido (licao do gancho de privacidade de 12/09). Esta e a trava: o commit nao passa se
#   1. algum script fora dos helpers lancar navegador por conta propria
#      (chromium.launch, firefox.launch, webkit.launch, connectOverCDP, browsers.create,
#      sync_playwright), ou
#   2. algum arquivo desligar o stealth ou o proxy (stealth: false, stealth=False,
#      disable_default_proxy, clear_proxy, proxy mode direct), ou
#   3. os helpers deixarem de ter o stealth fixo.
# Roda pelo .githooks/pre-commit. A mao: sh automacao/valida-stealth.sh
DIRR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DIRR" || exit 1
ERRO=0

ARQS=$(find automacao docs -type f \( -name '*.js' -o -name '*.mjs' -o -name '*.py' -o -name '*.sh' -o -name '*.gs' \) \
       ! -name 'navegador_kernel.js' ! -name 'navegador_kernel.py' ! -name 'valida-stealth.sh' 2>/dev/null)

HITS=$(printf '%s\n' $ARQS | xargs grep -nE 'chromium\.launch\(|firefox\.launch\(|webkit\.launch\(|connectOverCDP\(|connect_over_cdp\(|browsers\.create\(|sync_playwright\(' 2>/dev/null)
if [ -n "$HITS" ]; then
  echo "!! STEALTH: navegador lancado fora do helper. Use abrir() de automacao/navegador_kernel.{js,py}:"
  echo "$HITS"; ERRO=1
fi

HITS=$(grep -rnE 'stealth *: *false|stealth *= *False|disable_default_proxy|clear_proxy|mode *: *.direct.' \
       --include='*.js' --include='*.mjs' --include='*.py' --include='*.sh' --include='*.gs' \
       --exclude='valida-stealth.sh' --exclude-dir=.git --exclude-dir=node_modules . 2>/dev/null)
# (.md fica de fora de proposito: a documentacao PRECISA nomear o que e proibido)
if [ -n "$HITS" ]; then
  echo "!! STEALTH: alguem desligou stealth ou proxy. O Vini vetou isso em 24/09:"
  echo "$HITS"; ERRO=1
fi

grep -q 'const STEALTH = true' automacao/navegador_kernel.js || { echo "!! STEALTH: navegador_kernel.js perdeu 'const STEALTH = true'"; ERRO=1; }
grep -q 'stealth: STEALTH' automacao/navegador_kernel.js  || { echo "!! STEALTH: navegador_kernel.js nao passa stealth: STEALTH ao criar"; ERRO=1; }
grep -q '^STEALTH = True' automacao/navegador_kernel.py   || { echo "!! STEALTH: navegador_kernel.py perdeu 'STEALTH = True'"; ERRO=1; }
grep -q 'stealth=STEALTH' automacao/navegador_kernel.py   || { echo "!! STEALTH: navegador_kernel.py nao passa stealth=STEALTH ao criar"; ERRO=1; }

[ $ERRO -eq 0 ] && echo "valida-stealth: ok (stealth fixo, nenhum launch fora do helper)"
exit $ERRO
