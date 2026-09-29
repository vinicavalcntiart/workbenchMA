#!/bin/sh
# ronda-disney.sh — a ronda obrigatória do grupo Disney, por DELTA e com falha ALTA.
#
# POR QUE EXISTE. A ronda do grupo Disney é ordem fixa do Vini e vale TODA rodada. Repetir
# as 24 consultas de hora em hora é desperdício, então o método é comparar o CONJUNTO DE IDs
# da disciplina contra a linha de base da rodada anterior: se nenhum ID novo aparece, o zero
# está provado por medição e custa segundos.
#
# O DEFEITO QUE ESTE SCRIPT NASCEU PARA CONSERTAR, medido em 12/09 às 06h45:
# a sonda anterior era um pipeline de curl para python. Quando a API parou de responder, o
# curl devolveu corpo vazio, o python não imprimiu nada, e o laço concluiu "zero novo" —
# exatamente como se tivesse conferido e não achado nada. Foram 12 IDs às 04h45 e 0 às 06h45,
# e a diferença não era o quadro esvaziando: era HTTP 303 para
# https://community.workday.com/maintenance-page, ou seja o Workday em manutenção.
#
# Isso é FALSO NEGATIVO, que nesta campanha é o erro mais caro que existe: ele faz uma vaga
# nova passar despercebida no único lugar onde a regra 14 manda aplicar na hora.
#
# A REGRA: resposta vazia NÃO é zero. Zero é "a API respondeu e não havia nada".
# Quando não dá para medir, este script diz NAO CONFERIDO e sai com código 2.
#
# Uso:  sh automacao/ronda-disney.sh
#       sh automacao/ronda-disney.sh "<ids conhecidos separados por espaço>"

CONHECIDOS="${1:-10154147 10155895 10155332 10155202 10145923 10157562 10155976 10144787 10126752 10159762 10160266 10159370 10159371 10159882}"
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36'
TMP=$(mktemp -d)
OK=0
FALHAS=0

for site in disneycareer disneycareerdc; do
  for termo in character modeler sculpt texture creature groom; do
    COD=$(curl -s --max-time 25 -o "$TMP/r.json" -w '%{http_code}' \
      -X POST "https://disney.wd5.myworkdayjobs.com/wday/cxs/disney/$site/jobs" \
      -H 'Content-Type: application/json' -H 'Accept: application/json' -H "User-Agent: $UA" \
      -d "{\"appliedFacets\":{},\"limit\":20,\"offset\":0,\"searchText\":\"$termo\"}" 2>/dev/null)
    # 200 com JSON de verdade é a ÚNICA coisa que conta como "conferi".
    if [ "$COD" = "200" ] && [ -s "$TMP/r.json" ] && head -c 1 "$TMP/r.json" | grep -q '{'; then
      OK=$((OK+1))
      python3 - "$TMP/r.json" >> "$TMP/ids.txt" <<'PY'
import sys, json, re
T = re.compile(r'character|creature|modeler|modelling|modeling|sculpt|texture|texturing|'
               r'surfacing|look ?dev|visual development|groom|shading|material', re.I)
try:
    d = json.load(open(sys.argv[1], encoding='utf-8'))
except Exception:
    sys.exit()
for p in d.get('jobPostings', []):
    t = p.get('title', '')
    if not T.search(t):
        continue
    m = re.search(r'_(\d{6,})', p.get('externalPath', ''))
    if m:
        print(m.group(1), '|', t, '|', p.get('locationsText', ''))
PY
    else
      FALHAS=$((FALHAS+1))
      echo "  [falhou] $site/$termo -> http $COD" >&2
    fi
  done
done

echo "consultas que responderam: $OK · que falharam: $FALHAS"

if [ "$OK" = 0 ]; then
  echo
  echo "!! NAO CONFERIDO. Nenhuma consulta respondeu, entao esta rodada NAO mediu nada."
  echo "   Isto NAO e zero: e ausencia de medicao, e a diferenca importa porque a regra 14"
  echo "   manda aplicar NA HORA em vaga da disciplina nestas casas."
  echo "   Causa mais provavel, medida em 12/09: o Workday redireciona (303) para"
  echo "   https://community.workday.com/maintenance-page durante a janela de manutencao."
  echo "   Confira com:  curl -s -o /dev/null -w '%{http_code}\\n' -X POST \\"
  echo "     https://disney.wd5.myworkdayjobs.com/wday/cxs/disney/disneycareer/jobs \\"
  echo "     -H 'Content-Type: application/json' -d '{\"limit\":1,\"offset\":0,\"searchText\":\"art\"}'"
  echo "   Repita a ronda mais tarde. NAO registre zero."
  rm -rf "$TMP"
  exit 2
fi

sort -u "$TMP/ids.txt" 2>/dev/null > "$TMP/u.txt"
echo "IDs da disciplina no ar: $(wc -l < "$TMP/u.txt")"
NOVO=0
while IFS= read -r linha; do
  id=$(echo "$linha" | cut -d' ' -f1)
  case " $CONHECIDOS " in
    *" $id "*) ;;
    *) echo "  ID NOVO -> $linha"; NOVO=1 ;;
  esac
done < "$TMP/u.txt"

if [ "$NOVO" = 0 ]; then
  echo "  zero novo, e este zero FOI MEDIDO ($OK consultas responderam)."
fi
[ "$FALHAS" -gt 0 ] && echo "  RESSALVA: $FALHAS consulta(s) falharam, entao a cobertura desta rodada e parcial."
rm -rf "$TMP"
exit 0
