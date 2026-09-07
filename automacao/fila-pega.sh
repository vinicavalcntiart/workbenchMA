#!/bin/sh
# Pega uma linha da fila para trabalhar, com trava, para dois agentes nunca pegarem a mesma.
#
# POR QUE EXISTE: em 07/09 a Icefall Interactive RECEBEU DUAS CANDIDATURAS porque dois
# aplicadores trabalharam a mesma linha ao mesmo tempo. A marca de "emandamento" que um
# escrevia sumia, e sumia porque o outro reescrevia o ARQUIVO INTEIRO a partir de uma copia
# lida antes. Ler tudo, mudar um campo e regravar tudo apaga o que o vizinho escreveu no
# intervalo, e nao levanta erro nenhum. O estudio e quem paga: recebe duas mensagens do
# mesmo candidato no mesmo dia.
#
# A correcao nao e pedir cuidado, e tirar a possibilidade: aqui a troca de estado acontece
# sob flock e mexe SO na linha pega, com sed, nunca regravando o arquivo a partir de memoria.
#
# Uso:
#   sh automacao/fila-pega.sh <arquivo.csv> <meu-nome>     pega a proxima linha 'novo'
#   sh automacao/fila-pega.sh <arquivo.csv> <meu-nome> --devolve <n>   devolve a linha n
#   sh automacao/fila-pega.sh <arquivo.csv> <meu-nome> --feito <n> <estado>
#
# Ele imprime a linha pega com o numero na frente, ou nada se a fila estiver vazia.
# REGRA: quem pega e nao termina DEVOLVE. Linha presa em emandamento por agente que parou
# bloqueia todo mundo sem ninguem trabalhando nela.

ARQ="$1"; QUEM="$2"; ACAO="$3"; NUM="$4"; EST="$5"
[ -z "$ARQ" ] || [ -z "$QUEM" ] && { sed -n '2,28p' "$0"; exit 2; }
[ -f "$ARQ" ] || { echo "fila nao encontrada: $ARQ" >&2; exit 1; }
TRAVA="$ARQ.lock"

# O estado pode ser o ULTIMO campo da linha, e ai nao existe virgula depois dele. Casar so
# por ",novo," deixa essas linhas invisiveis e a fila parece vazia com trabalho dentro: foi
# o que o teste desta funcao pegou na primeira versao. Por isso todo padrao aqui aceita
# virgula OU fim de linha.
case "$ACAO" in
  --devolve)
    flock "$TRAVA" sh -c "sed -i '${NUM}s/,emandamento:${QUEM}\\(,\\|\$\\)/,novo\\1/' '$ARQ'"
    echo "devolvida a linha $NUM"
    ;;
  --feito)
    [ -z "$EST" ] && EST=enviada
    flock "$TRAVA" sh -c "sed -i '${NUM}s/,emandamento:${QUEM}\\(,\\|\$\\)/,${EST}\\1/' '$ARQ'"
    echo "linha $NUM marcada $EST"
    ;;
  *)
    # Pega a primeira linha com estado 'novo' e marca com o nome de quem pegou, tudo
    # dentro da trava: entre achar e marcar nao existe janela para o outro agente entrar.
    LINHA=$(flock "$TRAVA" sh -c "
      n=\$(grep -n ',novo\\(,\\|\$\\)' '$ARQ' | head -1 | cut -d: -f1)
      [ -z \"\$n\" ] && exit 0
      sed -i \"\${n}s/,novo\\(,\\|\\\$\\)/,emandamento:${QUEM}\\1/\" '$ARQ'
      echo \"\$n\"
    ")
    if [ -z "$LINHA" ]; then
      echo "fila vazia: nenhuma linha 'novo'" >&2
      exit 3
    fi
    echo "$LINHA|$(sed -n "${LINHA}p" "$ARQ")"
    ;;
esac
