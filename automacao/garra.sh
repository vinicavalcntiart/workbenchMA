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
# garras.txt NAO e versionado de proposito (esta no .gitignore), e um agente estranhou isso
# achando que a trava "nasce vazia a cada rodada". As duas protecoes sao diferentes e ambas
# existem: garras.txt e a trava de CONCORRENCIA, e serve porque todos os agentes rodam na
# MESMA maquina e no MESMO diretorio, entao eles se enxergam ali; versiona-la so criaria
# conflito de merge a cada reserva. A protecao que atravessa rodadas e dias e outra, e e a
# funcao feito() abaixo, que confere a URL e o ID da requisicao contra o painel e o
# processados.csv, esses sim versionados. Se voce so olhar garras.txt, esta olhando metade.
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
#
# CORRECAO DE 07/09 A NOITE, e ela e grande: a versao acima conferia PRESENCA da URL no
# painel, sem olhar o estado. So que TODA entrada da fila de formulario esta, por definicao,
# dentro do docs/index.html - e por isso a garra respondia JA-FEITO para as 405 entradas
# com done=false, que sao exatamente as que faltam fazer. Como o brief do Jhon manda "rode
# garra.sh checa antes de QUALQUER candidatura; saida 4 quer dizer ja feito", o agente que
# obedecia o brief ao pe da letra pulava a fila INTEIRA e voltava dizendo que o poco estava
# seco. A trava que existia para impedir candidatura repetida estava impedindo candidatura.
#
# O conserto guarda a protecao e devolve o trabalho: no painel so conta como feito a linha
# que esta com done=true, e no processados.csv so contam os tipos que significam candidatura
# (portal-aplicado, confirmacao-portal, portal-enviado, candidatura, enviado). Levantamento,
# varredura, vaga-nova, revalidacao, bloqueio e vaga-a-mao NAO sao candidatura e nao travam.
# E quando a URL esta no painel com done=false, o checa continua avisando, porque o caso
# Larian de hoje mostrou que existe envio real sem a linha do painel marcada: a saida vira
# "livre (ATENCAO: ...)" e a regra do brief continua valendo, confira o Gmail antes.
feito() {
  U="$1"; [ -z "$U" ] && return 1
  ID=$(printf '%s' "$U" | grep -o '[0-9]\{7,\}' | tail -1)
  D="$(dirname "$0")"
  P="$D/../docs/index.html"
  if [ -f "$P" ]; then
    grep -F "$U" "$P" 2>/dev/null | grep -q ',true,' && { echo "$P (url, done=true)"; return 0; }
    [ -n "$ID" ] && grep -F "$ID" "$P" 2>/dev/null | grep -q ',true,' && { echo "$P (id $ID, done=true)"; return 0; }
  fi
  C="$D/processados.csv"
  if [ -f "$C" ]; then
    T='portal-aplicado|confirmacao-portal|portal-enviado|candidatura|^enviado$'
    grep -F "$U" "$C" 2>/dev/null | awk -F, -v t="$T" '$5 ~ t {f=1} END{exit !f}' && { echo "$C (url, candidatura)"; return 0; }
    [ -n "$ID" ] && grep -F "$ID" "$C" 2>/dev/null | awk -F, -v t="$T" '$5 ~ t {f=1} END{exit !f}' && { echo "$C (id $ID, candidatura)"; return 0; }
  fi
  return 1
}
# Presenca no painel SEM done=true: nao trava, mas avisa. Vale como lembrete de conferir o Gmail.
no_painel() {
  U="$1"; [ -z "$U" ] && return 1
  P="$(dirname "$0")/../docs/index.html"
  [ -f "$P" ] || return 1
  grep -qF "$U" "$P" 2>/dev/null
}

case "$1" in
  checa)
    ONDE=$(feito "$2") && { echo "JA-FEITO: $ONDE"; exit 4; }
    if no_painel "$2"; then
      echo "livre (ATENCAO: a URL ja esta no painel com done=false. E alvo em aberto, nao trabalho feito, mas confira o Gmail antes de enviar: existe envio real sem a linha marcada, foi o caso da Larian hoje.)"
    else
      echo livre
    fi
    exit 0
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
