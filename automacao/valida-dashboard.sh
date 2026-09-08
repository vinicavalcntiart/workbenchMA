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

# PORTA DA CARTA FRIA, instalada em 07/09 depois de a mesma familia de erro aparecer em
# CINCO rascunhos numa hora so. Um deles saiu com assunto trocado, e assunto trocado nao e
# defeito estetico: o envia-rascunhos.gs acha as cartas pelo ASSUNTO LITERAL, entao carta com
# assunto diferente fica invisivel para o envio e nunca sai, parecendo trabalho feito. Aviso
# escrito no brief ja tinha falhado, entao vira porta, como foi com o telefone.
#
# So confere os arquivos de drafts/ MEXIDOS AGORA (modificados ou novos em relacao ao HEAD).
# Os 571 arquivos antigos ficam de fora de proposito: gate que reprova o passado nao e gate,
# e ruido que todo mundo aprende a ignorar.
ASSUNTO_FIXO='Senior Character Artist · Wingfeather Saga credit · stylized + grooming'
FECHO_FIXO='just point me and I will take it there'
CARTAS=$(cd "$DIRR" && git status --porcelain -- 'drafts/*.md' 2>/dev/null | awk '{print $NF}')
PROBLEMAS=""
for c in $CARTAS; do
  f="$DIRR/$c"
  [ -f "$f" ] || continue
  grep -qF "$ASSUNTO_FIXO" "$f" || PROBLEMAS="$PROBLEMAS
  $c: ASSUNTO fora do padrao. O envio acha a carta por esse assunto literal, entao ela nunca sairia."
  grep -qF "$FECHO_FIXO" "$f" || PROBLEMAS="$PROBLEMAS
  $c: falta o fechamento fixo, o que pede direcao em vez de tempo."
  grep -qiE 'chance to talk|a call\b|hop on a call|fifteen minutes|twenty minutes|1[05] minutes|20 minutes' "$f" \
    && PROBLEMAS="$PROBLEMAS
  $c: pede conversa ou tempo. Em carta fria isso custa mais que a recusa."
  grep -q 'artstation.com/viniciuscavalcanti' "$f" || PROBLEMAS="$PROBLEMAS
  $c: falta o link do ArtStation."
  grep -q 'linkedin.com/in/vinicavalcnti' "$f" || PROBLEMAS="$PROBLEMAS
  $c: falta o link do LinkedIn."
  grep -q 'vinicavalcanti.com' "$f" || PROBLEMAS="$PROBLEMAS
  $c: falta o link do site."
  grep -qiE '\bbrazil\b' "$f" && PROBLEMAS="$PROBLEMAS
  $c: contem a palavra Brazil."
  grep -q '—' "$f" && PROBLEMAS="$PROBLEMAS
  $c: contem travessao."
  grep -qi 'hope this finds you well' "$f" && PROBLEMAS="$PROBLEMAS
  $c: contem 'I hope this finds you well'."
  grep -qiE 'attach(ing|ed)? my (cv|resume)' "$f" && ! grep -qi 'anexo\|attached' "$f" && PROBLEMAS="$PROBLEMAS
  $c: diz que anexa o curriculo. Confira se o anexo existe mesmo."
done
if [ -n "$PROBLEMAS" ]; then
  echo "FALHA NA CARTA FRIA. Carta fria e o canal que menos converte, entao ela nao sai fora do padrao."
  echo "$PROBLEMAS"
  echo
  echo "O assunto e sempre este, caractere por caractere:"
  echo "  $ASSUNTO_FIXO"
  echo "E o fechamento e sempre este:"
  echo "  If character work opens up on your side, I'd like to be on your list. And if someone"
  echo "  else there is the right person for this, just point me and I will take it there."
  exit 1
fi

# PORTA DA CONFIANCA DO EMAIL, instalada em 08/09 pela MESMA razao das duas portas acima:
# regra escrita em brief que ja falhou vira porta. Em 06/09 mediu-se que endereco MONTADO por
# padrao de dominio quica em mais de 60% das vezes (dos 24 disparos daquele dia: 17 publicados,
# 16 entregues; 8 montados, 5 quicaram), e padroes-dominio.md passou a dizer que endereco de
# padrao entra como BAIXA, nunca media. O BRIEF-JOE.md continuou ensinando "media" em seis
# lugares contra dois, e a rodada de 08/09 seguiu a maioria: 16 linhas do pessoas.csv estavam
# marcadas media com endereco montado. Confianca inflada e pior que confianca baixa, porque a
# rodada seguinte gasta a unica carta da casa num endereco morto com o formato certo.
INFLADAS=$(python3 - "$DIRR/automacao/pessoas.csv" <<'PY'
import csv, sys
try: linhas = list(csv.reader(open(sys.argv[1], encoding='utf-8')))
except FileNotFoundError: sys.exit(0)
for i, x in enumerate(linhas[1:], start=2):
    if len(x) > 7 and x[6] == 'media' and 'padr' in x[7].lower() and 'publicad' not in x[7].lower():
        print(f"  linha {i}: {x[1]} / {x[3]} / {x[5]}")
PY
)
if [ -n "$INFLADAS" ]; then
  echo "FALHA DE CONFIANCA NO pessoas.csv: endereco MONTADO por padrao marcado como media."
  echo "$INFLADAS"
  echo
  echo "Endereco montado por padrao entra como BAIXA. Padrao prova que o FORMATO existe, nao"
  echo "que a pessoa continua na casa nem que a caixa esta viva. Medicao de 06/09: 5 de 8"
  echo "montados quicaram, contra 1 de 17 publicados. Se o endereco esta PUBLICADO, escreva"
  echo "isso na fonte, e ai ele e alta e nao media."
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
