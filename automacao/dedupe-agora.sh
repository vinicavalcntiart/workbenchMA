#!/bin/sh
# dedupe-agora.sh — o teste que se roda NO MINUTO DO CLIQUE, nunca contra a fila.
#
# POR QUE ISTO EXISTE. Em 09/09, entre 20h05 e 20h35, QUATRO candidaturas quase saíram
# repetidas, e as quatro tinham passado por um dedupe antes:
#
#   1. Imageworks Experienced Modeler 4363749003 — eu mesmo tinha deixado o comando
#      "preparado e conferido" na véspera. O ID já tinha saído DUAS vezes (02/09 e 07/09).
#   2. Eyeline Lead Surfacing Artist JR40928 — a fila do Workday listava como esperando a
#      próxima rodada. Já estava enviada e confirmada horas antes.
#   3. Netflix Sydney Environment Surfacing Supervisor JR41749 — idem.
#   4. As três da Ubisoft — dedupe por ID deu zero, e a CASA estava registrada como parede
#      de DataDome desde 06/09.
#
# O padrão é sempre o mesmo: **arquivo de fila envelhece em horas**, porque outra rodada
# envia a partir dele e não volta para riscar a linha. E a defesa não é lembrar, é medir.
#
# DUAS ARMADILHAS QUE ESTE SCRIPT EXISTE PARA COBRIR:
#   - Contar ocorrência do ID NÃO basta: as células do painel são longas e concatenam o
#     adiamento antigo com o recibo de envio novo. Ler a primeira ocorrência e parar já
#     escondeu dois envios reais (Bluehole e Loonshot). Aqui saem TODAS.
#   - Dedupe só por ID NÃO basta: a Ubisoft passou com ID zero e a casa era parede
#     conhecida. Por isso o segundo argumento (nome da casa) não é opcional na prática.
#
# Uso:  sh automacao/dedupe-agora.sh <ID-da-requisicao> "<nome da casa>"
# Ex.:  sh automacao/dedupe-agora.sh 4363749003 "Imageworks"

ID="$1"
CASA="$2"
if [ -z "$ID" ]; then
  echo "uso: sh automacao/dedupe-agora.sh <ID-da-requisicao> \"<nome da casa>\""
  exit 2
fi
RAIZ=$(cd "$(dirname "$0")/.." && pwd)
ARQS="$RAIZ/enviados.csv $RAIZ/automacao/processados.csv $RAIZ/docs/index.html $RAIZ/automacao/FILA-DO-VINI.md"

echo "== 1. TODAS as ocorrências do ID $ID =="
ACHOU=0
for a in $ARQS; do
  [ -f "$a" ] || continue
  N=$(grep -c -- "$ID" "$a" 2>/dev/null)
  [ "$N" -gt 0 ] || continue
  ACHOU=1
  echo "--- $(basename "$a"): $N ocorrência(s)"
  grep -o -- "$ID.\{0,150\}" "$a" | sed 's/^/    /'
done
[ "$ACHOU" = 0 ] && echo "    (nenhuma — o ID é inédito nos quatro arquivos)"

echo
echo "== 2. Marcas de ENVIO junto do ID (o teste barato que resolve) =="
MARCA=0
for a in $ARQS; do
  [ -f "$a" ] || continue
  grep -o -- "$ID.\{0,200\}" "$a" 2>/dev/null \
    | grep -i -- "confirmation\|ENVIADA\|enviada e confirmada\|portal-aplicado\|jobTasks/completed\|/thanks\|applyConfirmation\|Application Submitted" \
    | sed "s|^|    [$(basename "$a")] |" && MARCA=1
done
if [ "$MARCA" = 0 ]; then
  echo "    (nenhuma marca de envio)"
fi

echo
if [ -n "$CASA" ]; then
  echo "== 3. Histórico da CASA \"$CASA\" — parede, recusa e envio anterior =="
  for a in $ARQS; do
    [ -f "$a" ] || continue
    grep -i -o -- ".\{0,60\}$CASA.\{0,220\}" "$a" 2>/dev/null \
      | grep -i -- "parede\|captcha\|datadome\|turnstile\|hcaptcha\|recaptcha\|recusa\|veto\|duplicata\|JA-FEITO\|nao enviar" \
      | head -12 | sed "s|^|    [$(basename "$a")] |"
  done
  echo "    (se aparecer parede aqui, NÃO abra o navegador: é fila da mão dele)"
else
  echo "== 3. SEM NOME DE CASA — metade do teste não foi feita =="
  echo "    A Ubisoft passou com ID zero em 09/09 e a casa era parede conhecida desde 06/09."
  echo "    Rode de novo com o segundo argumento."
fi

echo
echo "VEREDITO: leia as três seções antes de clicar. Ocorrência sem marca de envio pode ser"
echo "adiamento ou descarte; ocorrência COM marca é envio feito, e clicar de novo é repetir."
