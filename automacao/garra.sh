#!/bin/sh
# Reserva um estudio+vaga ANTES de aplicar, para dois agentes nunca aplicarem no mesmo.
#
# POR QUE EXISTE: fila-pega.sh resolve fila ESTATICA, onde as linhas ja existem no arquivo.
# Nao resolve descoberta DINAMICA, que e o caso de tres agentes varrendo tres quadros de
# vaga diferentes ao mesmo tempo: o mesmo estudio aparece no Hitmarker e no Grackle, os dois
# agentes acham "novo" no mesmo minuto, e o estudio recebe duas candidaturas. Foi exatamente
# assim que a Icefall e a Red VFX receberam duas hoje, por caminhos diferentes.
#
# A regra que isto impoe: NINGUEM aplica sem garra. Reservar e checar sao o MESMO comando,
# feito sob trava, entao nao existe janela entre "vi que estava livre" e "marquei como meu".
#
# Uso:
#   sh automacao/garra.sh pega "<estudio>" "<vaga>" <meu-nome>   -> imprime OK ou JA-TEM:<quem>
#   sh automacao/garra.sh solta "<estudio>" "<vaga>"             -> devolve se nao aplicou
#   sh automacao/garra.sh lista
ARQ="$(dirname "$0")/garras.txt"; TRAVA="$ARQ.lock"; touch "$ARQ"
# chave normalizada: minusculas, so letras e numeros, para "Ninja Theory" == "ninja  theory"
chave() { printf '%s|%s' "$1" "$2" | tr 'A-Z' 'a-z' | sed 's/[^a-z0-9|]//g'; }
case "$1" in
  pega)
    K=$(chave "$2" "$3"); QUEM="${4:-anon}"
    flock "$TRAVA" sh -c '
      K="$1"; ARQ="$2"; QUEM="$3"
      DONO=$(grep -F "$K	" "$ARQ" | head -1 | cut -f2)
      if [ -n "$DONO" ]; then echo "JA-TEM:$DONO"; else
        printf "%s\t%s\t%s\n" "$K" "$QUEM" "$(date -u +%H:%M)" >> "$ARQ"; echo OK
      fi' _ "$K" "$ARQ" "$QUEM"
    ;;
  solta) K=$(chave "$2" "$3"); flock "$TRAVA" sh -c "grep -vF \"$K	\" '$ARQ' > '$ARQ.t' && mv '$ARQ.t' '$ARQ'"; echo solta ;;
  lista) wc -l < "$ARQ" | tr -d ' '; ;;
  *) sed -n '2,20p' "$0"; exit 2 ;;
esac
