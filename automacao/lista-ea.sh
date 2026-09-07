#!/bin/sh
# Lista o PORTAL INTEIRO da EA (jobs.ea.com, Avature) e grava um CSV.
#
# POR QUE ISTO EXISTE: a busca por palavra-chave do jobs.ea.com IGNORA o termo
# e devolve as MESMAS vinte vagas para qualquer coisa que se digite. Foi isso
# que escondeu a Principal Materials Artist da Respawn por dias. A unica leitura
# confiavel e PAGINAR a lista inteira por jobOffset, 20 por pagina.
# jobRecordsPerPage=100 NAO funciona: o servidor devolve 20 do mesmo jeito.
#
# uso: sh automacao/lista-ea.sh [arquivo-de-saida.csv]
# Roda com curl sequencial (uma conexao), porque varredura em lote junto com
# navegador satura a ponte desta sessao e mata o Chromium.

set -e
OUT="${1:-automacao/ea-portal.csv}"
TMP=$(mktemp -d)
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'
PROXY="${HTTPS_PROXY:-http://127.0.0.1:18080}"

# quantas vagas o portal diz ter
curl -s --proxy "$PROXY" -k -A "$UA" "https://jobs.ea.com/en_US/careers/SearchJobs/" -o "$TMP/p0.html"
TOTAL=$(grep -oE '[0-9]+ results' "$TMP/p0.html" | head -1 | tr -d ' results')
echo "portal diz: $TOTAL vagas"

OFF=20
while [ "$OFF" -lt "$TOTAL" ]; do
  curl -s --proxy "$PROXY" -k -A "$UA" \
    "https://jobs.ea.com/en_US/careers/SearchJobs/?jobOffset=$OFF" -o "$TMP/p$OFF.html"
  OFF=$((OFF+20))
  sleep 1
done

python3 - "$TMP" "$OUT" <<'PY'
import re,glob,html,csv,sys
tmp,out=sys.argv[1],sys.argv[2]
pat=re.compile(
  r'<a class="link link_result" href="(https://jobs\.ea\.com/en_US/careers/JobDetail/[^"]+/(\d+))"[^>]*>\s*(.*?)\s*</a>'
  r'.*?<span class="list-item-location">(.*?)</span>'
  r'.*?<span class="list-item-workerType">(.*?)</span>'
  r'.*?<span class="list-item-department">(.*?)</span>', re.S)
rows={}
for f in glob.glob(tmp+'/p*.html'):
    h=open(f,encoding='utf-8',errors='replace').read()
    for m in pat.finditer(h):
        url,jid,title,loc,wt,dept=[html.unescape(re.sub(r'<[^>]+>','',x)).strip() for x in m.groups()]
        rows[jid]=(jid,title,loc,wt,dept,url)
with open(out,'w',newline='',encoding='utf-8') as fh:
    w=csv.writer(fh); w.writerow(['id','title','location','type','department','url'])
    for k in sorted(rows): w.writerow(rows[k])
print('gravei',len(rows),'vagas em',out)
PY
rm -rf "$TMP"
