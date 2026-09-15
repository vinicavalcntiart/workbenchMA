#!/bin/sh
# LE-ATS — lê o quadro de vagas de um ATS por curl, com a receita de CADA um já medida.
#
# POR QUE ISTO EXISTE. Cada ATS esconde a lista num lugar diferente, e descobrir onde custa
# meia rodada. Pior: quando a sonda erra o endereço, ela devolve silêncio, e silêncio parece
# ZERO. Em 15/09 isso quase virou número duas vezes num intervalo de minutos. Aqui a receita
# de cada um está gravada, e o script diz NÃO CONFERIDO quando não pode afirmar zero.
#
#   sh automacao/le-ats.sh <ats> <slug>
#   sh automacao/le-ats.sh jobvite double-negative-visual-effects
#   sh automacao/le-ats.sh bamboohr imageengine
#   sh automacao/le-ats.sh recruitee framestore
#
# REGRA DE OURO, paga com erro: rode um CONTROLE com slug que existe ANTES e DEPOIS de
# qualquer varredura. O Workable estrangula (HTTP 429) e o silêncio dele é indistinguível de
# quadro vazio; sem os dois controles, o número não vale.
ATS="$1"; SLUG="$2"
[ -z "$SLUG" ] && { sed -n '2,20p' "$0"; exit 2; }
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
TMP="${TMPDIR:-/tmp}/leats.$$"

case "$ATS" in
  jobvite)
    # MEDIDO EM 15/09: /api devolve 302 e /jobs.json devolve 200 com CASCA DE SPA, que é a
    # armadilha. Quem serve as vagas em HTML de verdade é /<slug>/search, e o título NÃO é o
    # texto da âncora: é um <p> dentro dela, na classe jv-job-list-name. Contar âncora sem
    # ler o <p> devolve "N vagas, zero da disciplina" com N certo e zero falso.
    URL="https://jobs.jobvite.com/$SLUG/search"; MODO=html ;;
  bamboohr)
    URL="https://$SLUG.bamboohr.com/careers/list"; MODO=bamboo ;;
  recruitee)
    # O corpo pode passar de 800 KB (o da Framestore tem 833). Junta corpo e código HTTP na
    # mesma variável de shell e ele trunca CALADO, acusando "falha de parser" onde há quadro
    # de 55 vagas. Por isso aqui o corpo vai para ARQUIVO e o código vem separado.
    URL="https://$SLUG.recruitee.com/api/offers/"; MODO=recruitee ;;
  workable)
    URL="https://apply.workable.com/api/v1/widget/accounts/$SLUG?details=true"; MODO=workable ;;
  ashby)
    URL="https://api.ashbyhq.com/posting-api/job-board/$SLUG"; MODO=ashby ;;
  *) echo "ATS desconhecido: $ATS (jobvite, bamboohr, recruitee, workable, ashby)"; exit 2 ;;
esac

CODE=$(curl -s -m 25 -A "$UA" -o "$TMP" -w '%{http_code}' "$URL")
case "$CODE" in
  200) ;;
  429) echo "NÃO CONFERIDO: $ATS/$SLUG devolveu 429, que é estrangulamento. Silêncio aqui NÃO é zero."; rm -f "$TMP"; exit 9 ;;
  *)   echo "NÃO CONFERIDO: $ATS/$SLUG devolveu HTTP $CODE (não é 200, então não dá para afirmar zero)."; rm -f "$TMP"; exit 9 ;;
esac

ARQ="$TMP" MODO="$MODO" SLUG="$SLUG" python3 - <<'PY'
import json, os, re, sys
arq, modo, slug = os.environ['ARQ'], os.environ['MODO'], os.environ['SLUG']
bruto = open(arq, encoding='utf8', errors='replace').read()
disc = re.compile(r'character|creature|model|sculpt|groom|texture|look ?dev|surfac', re.I)
vagas = []
try:
    if modo == 'html':
        for u, t, l in re.findall(
                r'href="(/[^"]+/job/[^"]+)".*?jv-job-list-name"><p[^>]*>([^<]+)</p>'
                r'.*?jv-job-list-location"><p[^>]*>\s*([^<]*?)\s*</p>', bruto, re.S):
            vagas.append((t.strip(), re.sub(r'\s+', ' ', l).strip(), u))
    elif modo == 'bamboo':
        for j in (json.loads(bruto).get('result') or []):
            loc = j.get('location') or {}
            vagas.append((str(j.get('jobOpeningName', '')),
                          ' '.join(str(loc.get(k) or '') for k in ('city', 'state', 'country')).strip(),
                          str(j.get('id'))))
    elif modo == 'recruitee':
        for o in (json.loads(bruto).get('offers') or []):
            vagas.append((o.get('title', ''), '%s %s' % (o.get('city') or '', o.get('country_code') or ''),
                          o.get('careers_url', '')))
    elif modo == 'workable':
        for j in (json.loads(bruto).get('jobs') or []):
            loc = j.get('location') or {}
            vagas.append((j.get('title', ''), '%s %s' % (loc.get('city') or '', loc.get('country') or ''),
                          j.get('shortlink', '')))
    elif modo == 'ashby':
        for j in (json.loads(bruto).get('jobs') or []):
            vagas.append((j.get('title', ''), j.get('location', ''), j.get('jobUrl', '')))
except Exception as e:
    print('NÃO CONFERIDO: falha de parser em %s (%s)' % (slug, str(e)[:70]))
    sys.exit(9)

if not vagas:
    print('%s: HTTP 200 e NENHUMA vaga na lista. Este zero é medido.' % slug)
    sys.exit(0)

hit = [v for v in vagas if disc.search(v[0])]
print('%s: %d vagas | da disciplina por título: %d' % (slug, len(vagas), len(hit)))
for t, l, u in hit:
    print('   >>', t[:60], '|', l[:30], '|', u[:70])
# os títulos inteiros saem sempre, porque zero que depende de regex não é zero medido
print('   --- todos os títulos:')
for t, l, u in vagas:
    print('      -', t[:58], '|', l[:26])
PY
rm -f "$TMP"
