#!/bin/sh
# RONDA DA PARAMOUNT (regra 14), pelo SITEMAP.
#
# POR QUE ESTE SCRIPT EXISTE, medido em 13/09:
# A campanha registrou a Paramount como ILEGIVEL desde 31/08, com a nota
# "responde Access Denied do Akamai, coberta pelo alerta de email". Isso e
# verdade para  www.paramount.com/careers  -> HTTP 403 do Akamai.
# E e FALSO para  careers.paramount.com    -> HTTP 200.
# O subdominio de carreiras abre. So que a BUSCA dele e SPA: qualquer termo
# devolve a MESMA casca de ~319 KB, entao o curl nao le resultado filtrado e
# quem tentar por ali tem que escrever NAO CONFERIDO, nunca zero.
#
# O que le de verdade e o SITEMAP, que lista TODAS as vagas com o titulo
# dentro da URL:  https://careers.paramount.com/sitemap.xml
#
# ARMADILHA QUE JA MORDEU UMA VEZ, em 13/09: um laco de curl que reusava o
# mesmo arquivo de saida sobrescreveu o sitemap com o robots.txt, o parser
# achou zero <loc> e quase virou "zero vagas" no registro. Saida propria por
# arquivo, sempre. Falha de parser e NAO CONFERIDO, nunca zero.
#
# Uso:  sh automacao/ronda-paramount.sh
set -u
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36'

code=$(curl -s -m 40 -o "$TMP/sitemap.xml" -w '%{http_code}' -H "User-Agent: $UA" \
  "https://careers.paramount.com/sitemap.xml")

if [ "$code" != "200" ]; then
  echo "NAO CONFERIDO: o sitemap da Paramount respondeu http=$code (nao e zero, e falta de leitura)."
  exit 1
fi

python3 - "$TMP/sitemap.xml" <<'PY'
import re,sys,urllib.parse
s=open(sys.argv[1],encoding='utf-8',errors='replace').read()
locs=re.findall(r'<loc>(.*?)</loc>',s)
jobs=[u for u in locs if '/job/' in u]
if not jobs:
    print("NAO CONFERIDO: o sitemap respondeu 200 mas nao traz nenhuma URL /job/.")
    print("Conferir se o formato mudou antes de registrar qualquer numero.")
    raise SystemExit(1)

# disciplina do Vini. 'animat' entra so para o olho humano decidir depois.
termos=re.compile(r'character|model(?:er|ing|ler)|texture|texturing|groom|'
                  r'surfac|look-?dev|visual-?dev|3d-artist|sculpt|animat',re.I)
hits=[(urllib.parse.unquote(u.split('/job/')[1]),u) for u in jobs if termos.search(u)]

print(f"vagas no quadro da Paramount: {len(jobs)} (sitemap respondeu 200)")
if hits:
    print(f"acertos da disciplina: {len(hits)} — CLASSIFIQUE CADA UM A MAO,")
    print("porque 'Data Architecture and Modeling' ja apareceu como falso positivo:")
    for slug,u in hits:
        print("  *",slug[:100])
        print("   ",u)
else:
    print("ZERO MEDIDO: nenhuma vaga da disciplina nas",len(jobs),"do quadro.")
    print("amostra de 8 titulos, para provar que o parser esta lendo:")
    for u in jobs[:8]:
        print("   -",urllib.parse.unquote(u.split('/job/')[1])[:80])
PY
