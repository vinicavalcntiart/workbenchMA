#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LE-WARNER — lê o quadro da Warner Bros. Discovery, que é casa da REGRA 14.

A RECEITA ANTIGA DO REGISTRO ESTAVA ERRADA EM TRÊS CAMADAS, e as três foram medidas em 15/09.
Ela mandava ler `careers.wbd.com/global/en/search-results?keywords=<termo>` e pegar o JSON
embutido sob `"jobs":[`. O que acontece de verdade:

  1. A regex `"jobs":(\\[.*?\\])` NÃO fecha o array: há colchetes aninhados dentro dele, o `.*?`
     corta no primeiro `]` e o json.loads morre com "Expecting ',' delimiter". Deu falha de
     parser em 3 de 4 termos.
  2. Os campos NÃO ficam sob uma chave `data`. São de primeiro nível (`title`, `reqId`,
     `cityState`). Lendo `v["data"]["title"]` o título vinha None em TODOS os itens, e o efeito
     era "10 vagas, zero da disciplina": número certo, zero falso. Mesma família da armadilha do
     Jobvite, onde o título mora num <p> dentro da âncora.
  3. E o pior: **o parâmetro `keywords` não filtra nada**. A página declara `totalHits: 310` e
     devolve `hits: 10`, sempre os mesmos dez, que na medição eram Combat Designer, HR Working
     Student e Data Scientist. Ou seja, mesmo com o parser certo, o zero seria sobre DEZ vagas
     não filtradas de trezentas e dez.

O QUE FUNCIONA: a Warner roda WORKDAY por baixo, e o próprio HTML entrega o endereço no campo
`imApplyUrl`, que aponta para `warnerbros.wd5.myworkdayjobs.com`. Então aqui se lê pelo oráculo
do Workday, paginando o quadro INTEIRO sem filtro, que é o que separa medição de suposição.
Medido em 15/09: 320 de 320 lidas, zero da disciplina.

    python3 automacao/le-warner.py
"""
import json
import re
import sys
import urllib.request

UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/128.0 Safari/537.36')
BASE = 'https://warnerbros.wd5.myworkdayjobs.com/wday/cxs/warnerbros/%s/jobs'
DISC = re.compile(r'character|creature|model|sculpt|groom|texture|look ?dev|surfac|visual dev', re.I)
# os sites do locatário saem do robots.txt dele; `global` é o grande, `francais` é o espelho
SITES = ('global',)


def pagina(site, offset):
    """Uma página de 20. O `limit` do Workday tem teto 20; pedir mais devolve HTTP 400."""
    corpo = json.dumps({'appliedFacets': {}, 'limit': 20,
                        'offset': offset, 'searchText': ''}).encode()
    req = urllib.request.Request(BASE % site, data=corpo,
                                 headers={'User-Agent': UA,
                                          'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=30) as r:
        if r.status != 200:
            raise RuntimeError('HTTP %s' % r.status)
        return json.loads(r.read().decode('utf8', 'replace'))


def le(site):
    try:
        d = pagina(site, 0)
    except Exception as e:
        return None, 0, 'NAO CONFERIDO: %s' % str(e)[:70]
    total = d.get('total') or 0
    vistas, offset = {}, 0
    while offset < total + 20:
        try:
            d = pagina(site, offset)
        except Exception as e:
            # página que falha no meio deixa a cobertura PARCIAL, e isso se diz em voz alta
            return vistas, total, ('NAO CONFERIDO a partir do offset %d: %s'
                                   % (offset, str(e)[:60]))
        ps = d.get('jobPostings') or []
        if not ps:
            break
        for j in ps:
            vistas[(j.get('bulletFields') or ['-'])[0]] = (
                str(j.get('title')), str(j.get('locationsText')))
        offset += 20
    return vistas, total, None


def main():
    for site in SITES:
        vistas, total, erro = le(site)
        if vistas is None:
            print('%s: %s' % (site, erro))
            continue
        print('%s: %d vagas unicas lidas de %d declaradas' % (site, len(vistas), total))
        if erro:
            print('  RESSALVA: %s' % erro)
        hits = [(i, t, l) for i, (t, l) in vistas.items() if DISC.search(t)]
        print('  da disciplina por titulo: %d' % len(hits))
        for i, t, l in hits:
            print('    >> %-12s %-54s %s' % (i, t[:52], l[:30]))
        if len(vistas) < total:
            print('  ATENCAO: li menos do que o total declarado. Este zero NAO esta medido.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
