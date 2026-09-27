#!/bin/sh
# Sonda de ROTA ESPONTANEA. Recebe "familia|slug".
# Discriminador (controlado em 20/09 nas duas pontas):
#   recruitee: 200 = rota aberta; 404 = locatario existe e NAO tem a rota (framestore);
#              301 = slug inexistente.
#   homerun:   200 = rota aberta (totalmayhemgames); 302 = inexistente ou rota desligada.
# O cabecalho Accept de NAVEGADOR e obrigatorio: em 20/09 o Pinpoint devolveu 200 com
# Accept: */* e 404 com o Accept de navegador na MESMA URL (bildstudios). Sondar com o
# Accept do curl conta porta que o navegador nao consegue abrir.
A='text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
fam=$(echo "$1" | cut -d'|' -f1); slug=$(echo "$1" | cut -d'|' -f2)
case "$fam" in
  recruitee) u="https://${slug}.recruitee.com/o/open-application";;
  homerun)   u="https://${slug}.homerun.co/open-application";;
  *) exit 0;;
esac
code=$(curl -s -o /dev/null --max-time 12 -w '%{http_code}' -H "Accept: $A" -H 'Sec-Fetch-Mode: navigate' "$u")
[ "$code" = "200" ] && echo "${fam},${slug},200"
[ "$code" = "000" ] && echo "${fam},${slug},FALHA" >&2
exit 0
