#!/bin/sh
# SONDA-DAYFORCE — descobre locatários do Dayforce por token, com um discriminador que NÃO
# produz zero falso e que ainda diz o NOME DA CASA.
#
# POR QUE ESTA LANE. O BRIEF-JHON lista o Dayforce entre os ATS que ainda rendem, e até 15/09 a
# campanha só o conhecia por TRÊS quadros achados um a um à mão (Crafty Apes, Reflector/Bandai
# Namco e Blue Ant/Thunderbird). Nunca houve varredura por token, porque não se sabia como
# separar locatário vivo de token inventado.
#
# O DEFEITO DO CAMINHO ÓBVIO, medido em 15/09 às 20h: o código HTTP NÃO SERVE de oráculo.
# `https://jobs.dayforcehcm.com/en-US/<token>/CANDIDATEPORTAL` devolve **200 para qualquer
# coisa**, inclusive para `zzznaoexistexyz`. É o "200 educado" contra o qual o briefing avisa.
#
# O QUE DISCRIMINA, e foi medido com controle nas DUAS pontas: o shell da página traz a
# configuração do locatário embutida, e nela o campo **`candidateCorrespondenceClientName`**,
# que só existe quando o locatário existe. No token inventado ele não aparece (e o shell vem
# ~94 KB menor). O valor é a RAZÃO SOCIAL da casa, o que mata de brinde a armadilha do falso
# amigo de token: o token `cinesite` responde
# "Cinesite | Image Engine Design | L'Atelier Animation | Trixter", então não há como confundir
# a casa com outra de nome parecido.
#
# DUAS ARMADILHAS QUE ESTA SONDA JÁ TEM CONSERTADAS DENTRO, as duas medidas no dia:
#   1. `/en-US/<token>/...` responde **307** para o locale da casa (ex.: `/en-CA/...`). Sem
#      `-L` o corpo que volta tem 26 bytes e o grep acha nada: o controle `ref`, que é VIVO,
#      deu ZERO. Isso é zero falso de método, não lane vazia.
#   2. O campo NÃO é `"ClientName":"`. Procurar por essa forma acha nada mesmo na página certa,
#      porque o nome real do campo é `candidateCorrespondenceClientName`.
#
# O QUE ESTA SONDA NÃO FAZ, e está medido: LER AS VAGAS. O endereço das vagas foi achado lendo
# o pacote JavaScript do portal (17 arquivos, 3 MB), e não por chute:
#     POST https://jobs.dayforcehcm.com/api/geo/<token>/jobposting/search
# Ele EXISTE (um GET devolve 405 Method Not Allowed, que é método errado e não ausência), mas
# devolve **403 Forbidden** para `curl`, inclusive com sessão e cookies do próprio portal. Falta
# um token de sessão que só o navegador monta. Portanto: a lista de vagas de um locatário do
# Dayforce é **NÃO CONFERIDO por curl** e precisa de navegador. Não invente zero a partir daqui.
#
# Uso:  sh automacao/sonda-dayforce.sh                  # lista embutida de tokens de estúdio
#       sh automacao/sonda-dayforce.sh tok1 tok2 ...    # tokens próprios
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'

# CONTROLES OBRIGATÓRIOS nas duas pontas. `ref` e `blueantmedia` são locatários conhecidos e
# TÊM de aparecer; `zzznaoexistexyz` NÃO pode aparecer. Se o controle positivo sumir, a sonda
# está quebrada e o zero dela não vale nada.
CTRL_VIVO="ref blueantmedia"
CTRL_MORTO="zzznaoexistexyz"

TOKENS="$*"
[ -z "$TOKENS" ] && TOKENS="craftyapes thunderbird wildbrain nelvana bardel atomiccartoons guru
jamfilled spinvfx zoic imageengine scanlinevfx digitaldomain pixomondo folks raynault realtimeuk
axisstudios milkvfx unionvfx outpostvfx rodeofx mikros cinesite dneg framestore mpc animallogic"

nome_de() {
  curl -sL --max-time 18 -H "User-Agent: $UA" \
    "https://jobs.dayforcehcm.com/en-US/$1/CANDIDATEPORTAL" 2>/dev/null \
    | grep -o 'candidateCorrespondenceClientName":"[^"]\{1,80\}"' \
    | head -1 | sed 's/.*ClientName":"//; s/"$//'
}

echo "== controle positivo (tem de responder com nome)"
FALHOU=0
for c in $CTRL_VIVO; do
  n=$(nome_de "$c")
  if [ -n "$n" ]; then printf '   ok   %-16s %s\n' "$c" "$n"
  else printf '   !!   %-16s SEM NOME\n' "$c"; FALHOU=1; fi
done
echo "== controle negativo (NAO pode responder)"
n=$(nome_de "$CTRL_MORTO")
if [ -n "$n" ]; then printf '   !!   %-16s respondeu "%s" — o discriminador nao discrimina\n' "$CTRL_MORTO" "$n"; FALHOU=1
else printf '   ok   %-16s sem nome, como esperado\n' "$CTRL_MORTO"; fi

if [ "$FALHOU" = 1 ]; then
  echo
  echo "!! NAO CONFERIDO. O controle falhou, entao esta rodada NAO mediu a lane do Dayforce."
  echo "   Zero saido de sonda com controle quebrado e indistinguivel de zero medido."
  exit 2
fi

echo
echo "== varredura"
VIVOS=0; TOT=0
for t in $TOKENS; do
  TOT=$((TOT+1))
  n=$(nome_de "$t")
  [ -n "$n" ] && { VIVOS=$((VIVOS+1)); printf '   VIVO  %-16s %s\n' "$t" "$n"; }
done
echo
echo "sondados $TOT · locatarios vivos $VIVOS"
echo "LEMBRE: locatario vivo NAO e vaga lida. A lista de vagas fica atras de"
echo "  POST /api/geo/<token>/jobposting/search , que devolve 403 para curl e precisa de navegador."
exit 0
