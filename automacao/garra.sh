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
#   sh automacao/garra.sh pega "<estudio>" "<vaga>" <meu-nome> [url]  -> OK, JA-TEM:<quem> ou JA-FEITO
#   sh automacao/garra.sh checa "<url-da-vaga>"                     -> livre ou JA-FEITO:<onde>
#   sh automacao/garra.sh solta "<estudio>" "<vaga>"             -> devolve se nao aplicou
#   sh automacao/garra.sh lista
ARQ="$(dirname "$0")/garras.txt"; TRAVA="$ARQ.lock"; touch "$ARQ"
# chave normalizada: minusculas, so letras e numeros, para "Ninja Theory" == "ninja  theory"
chave() { printf '%s|%s' "$1" "$2" | tr 'A-Z' 'a-z' | sed 's/[^a-z0-9|]//g'; }
# CHECAGEM DE JA-FEITO, adicionada em 07/09 depois de EU MESMO mandar duas candidaturas
# repetidas para a Sony Pictures Imageworks na mesma noite em que escrevi esta garra.
#
# A garra protegia contra dois agentes ao MESMO TEMPO. Ela nao protegia contra trabalho ja
# feito DIAS ATRAS, e foi por ai que o erro passou: eu filtrei o painel por done=false para
# escolher no que trabalhar, as vagas de Vancouver estavam com done=true, e por isso ficaram
# invisiveis; depois reachei as mesmas vagas pela API do Greenhouse e apliquei como se fossem
# novas. A Experienced Modeler ja tinha ido em 02/09 e a Experienced Texture Artist em 05/09.
#
# A licao, e ela e sutil: filtrar por done=false para ESCOLHER esta certo, mas conferir por
# done=false para DEDUPLICAR e exatamente o contrario do necessario, porque o que ja foi feito
# e justamente o que esta com done=true. A conferencia tem que ser pela URL ou pelo ID DA
# REQUISICAO, contra o arquivo inteiro, sem filtro de estado nenhum.
feito() {
  U="$1"; [ -z "$U" ] && return 1
  ID=$(printf '%s' "$U" | grep -o '[0-9]\{7,\}' | tail -1)
  D="$(dirname "$0")"
  for alvo in "$D/../docs/index.html" "$D/processados.csv"; do
    [ -f "$alvo" ] || continue
    grep -qF "$U" "$alvo" 2>/dev/null && { echo "$alvo (url)"; return 0; }
    [ -n "$ID" ] && grep -qF "$ID" "$alvo" 2>/dev/null && { echo "$alvo (id $ID)"; return 0; }
  done
  return 1
}

case "$1" in
  checa)
    ONDE=$(feito "$2") && { echo "JA-FEITO: $ONDE"; exit 4; }
    echo livre; exit 0
    ;;
  pega)
    K=$(chave "$2" "$3"); QUEM="${4:-anon}"
    # 5o argumento opcional: a URL da vaga. Se vier, a garra RECUSA o que ja esta no painel.
    if [ -n "$5" ]; then
      ONDE=$(feito "$5") && { echo "JA-FEITO: $ONDE"; exit 4; }
    fi
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
