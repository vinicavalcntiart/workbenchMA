#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SONDA-LOTE-ATS — pega uma lista de nomes de casa e descobre quem tem quadro de ATS vivo.

NASCEU EM 15/09, junto com o colhe-wikidata.py, para responder à cobrança do Vini
(*"precisamos de mais formularios, ta mt lento"*). A dupla é o conserto do gargalo real: o
colhe traz ESTOQUE DE NOMES NOVO (4.483 casas inéditas na primeira colheita) e este aqui
converte nome em PORTA.

**AS FAMÍLIAS AQUI SÃO SÓ AS QUE RESPONDEM DESTA REDE**, e cada exclusão é medida, não achismo:
  - Workable fica FORA: `error code: 1015` da Cloudflare, por IP, medido em curl E em navegador.
  - Dayforce fica fora desta sonda porque o quadro dele não se lê por token simples; tem sonda
    própria (`sonda-dayforce.sh`), com o oráculo do `candidateCorrespondenceClientName`.

**O ORÁCULO DE CADA FAMÍLIA, e por que não basta olhar o código HTTP:** vários ATS devolvem
"200 educado" para qualquer token que um dia existiu, e o briefing manda desconfiar disso. Então
cada família tem um teste de CONTEÚDO, e o script roda um CONTROLE POSITIVO e um NEGATIVO antes
de começar. Se o controle falhar, ele sai com código 2 e a palavra NAO CONFERIDO, em vez de
entregar um zero que parece medido.

    python3 automacao/sonda-lote-ats.py <arquivo.csv> [coluna_do_token] [--familias gh,lever]
    python3 automacao/sonda-lote-ats.py /tmp/novos.csv token
"""
import csv
import json
import queue
import re
import sys
import threading
import urllib.request

UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/128.0 Safari/537.36')
TIMEOUT = 14
LINHAS = 28  # trabalhadores em paralelo; acima disso os ATS comecam a estrangular


def http(url, timeout=TIMEOUT):
    # DEFEITO MEDIDO NO PROPRIO DIA EM QUE ESTE ARQUIVO NASCEU: eu lia so os primeiros 400 KB,
    # para economizar. Corpo truncado vira JSON INVALIDO, o json.loads morre, a familia inteira
    # e descartada como "controle falhou" e a rodada perde a lane sem perceber. Aconteceu com o
    # Lever (skydance) e com o Ashby (supercell), que respondem 200 perfeitamente quando o corpo
    # vem inteiro. Economia de bytes que produz zero falso nao e economia.
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': '*/*'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf8', 'replace')
    except Exception as e:
        cod = getattr(e, 'code', None)
        return (cod or 0), ''


def gh(t):
    s, c = http('https://boards-api.greenhouse.io/v1/boards/%s/jobs' % t)
    if s != 200 or '"jobs"' not in c:
        return None
    try:
        n = len(json.loads(c).get('jobs', []))
    except Exception:
        return None
    return ('greenhouse', 'https://job-boards.greenhouse.io/%s' % t, n)


def lever(t):
    s, c = http('https://api.lever.co/v0/postings/%s?mode=json' % t)
    if s != 200 or not c.strip().startswith('['):
        return None
    try:
        n = len(json.loads(c))
    except Exception:
        return None
    return ('lever', 'https://jobs.lever.co/%s' % t, n) if n else None


def ashby(t):
    s, c = http('https://api.ashbyhq.com/posting-api/job-board/%s' % t)
    if s != 200 or '"jobs"' not in c:
        return None
    try:
        n = len(json.loads(c).get('jobs', []))
    except Exception:
        return None
    return ('ashby', 'https://jobs.ashbyhq.com/%s' % t, n)


def recruitee(t):
    s, c = http('https://%s.recruitee.com/api/offers/' % t)
    if s != 200 or '"offers"' not in c:
        return None
    try:
        n = len(json.loads(c).get('offers', []))
    except Exception:
        return None
    return ('recruitee', 'https://%s.recruitee.com/' % t, n)


def personio(t):
    # medido em 15/09: slug inexistente devolve 307, entao 200 aqui e significativo; e o XML
    # repete TITULO DE SECAO dentro de <name>, entao conta-se <position>, nunca <name>.
    s, c = http('https://%s.jobs.personio.com/xml' % t)
    if s != 200 or '<position>' not in c:
        return None
    return ('personio', 'https://%s.jobs.personio.com/' % t, c.count('<position>'))


def teamtailor(t):
    s, c = http('https://%s.teamtailor.com/jobs' % t)
    if s != 200 or 'teamtailor' not in c.lower():
        return None
    n = len(re.findall(r'/jobs/\d+', c))
    return ('teamtailor', 'https://%s.teamtailor.com/jobs' % t, n)


def smartrecruiters(t):
    # medido em 15/09: token inexistente devolve 200 com totalFound 0, entao o oraculo e o NUMERO
    s, c = http('https://api.smartrecruiters.com/v1/companies/%s/postings?limit=100' % t)
    if s != 200 or 'totalFound' not in c:
        return None
    try:
        d = json.loads(c)
    except Exception:
        return None
    n = d.get('totalFound', 0)
    return ('smartrecruiters', 'https://jobs.smartrecruiters.com/%s' % t, n) if n else None


def bamboo(t):
    s, c = http('https://%s.bamboohr.com/careers/list' % t)
    if s != 200 or '"result"' not in c:
        return None
    try:
        n = len(json.loads(c).get('result') or [])
    except Exception:
        return None
    return ('bamboohr', 'https://%s.bamboohr.com/careers' % t, n)


FAMILIAS = {'gh': gh, 'lever': lever, 'ashby': ashby, 'recruitee': recruitee,
            'personio': personio, 'teamtailor': teamtailor,
            'smartrecruiters': smartrecruiters, 'bamboohr': bamboo}
# controles medidos: token VIVO conhecido e token que nao existe
CONTROLE = {'gh': ('absurdventures', 'zzznaoexistexyz'),
            'lever': ('skydance', 'zzznaoexistexyz'),
            'ashby': ('supercell', 'zzznaoexistexyz'),
            'recruitee': ('framestore', 'zzznaoexistexyz'),
            'personio': ('aesir', 'zzznaoexistexyz'),
            'teamtailor': ('airshipinteractive', 'zzznaoexistexyz'),
            'smartrecruiters': ('RodeoFX', 'zzznaoexistexyz'),
            'bamboohr': ('owi', 'zzznaoexistexyz')}


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    arq = sys.argv[1]
    col = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else 'token'
    quais = list(FAMILIAS)
    if '--familias' in sys.argv:
        quais = sys.argv[sys.argv.index('--familias') + 1].split(',')

    print('== controles (positivo tem de achar, negativo NAO pode achar)')
    validas = []
    for f in quais:
        vivo, morto = CONTROLE[f]
        a, b = FAMILIAS[f](vivo), FAMILIAS[f](morto)
        ok = (a is not None) and (b is None)
        print('   %-16s positivo=%-5s negativo=%-5s %s'
              % (f, 'achou' if a else 'NADA', 'achou' if b else 'nada',
                 'ok' if ok else '!! NAO CONFERIDO, familia descartada desta rodada'))
        if ok:
            validas.append(f)
    if not validas:
        print('\n!! NENHUMA familia passou no controle. Esta rodada NAO mediu nada.')
        return 2

    tokens = []
    for r in csv.DictReader(open(arq, encoding='utf-8')):
        t = (r.get(col) or '').strip()
        if len(t) >= 4:
            tokens.append((t, r.get('nome', ''), r.get('pais', '')))
    vistos, tokens2 = set(), []
    for t, n, p in tokens:
        if t not in vistos:
            vistos.add(t)
            tokens2.append((t, n, p))
    print('\n== varrendo %d tokens unicos contra %d familias (%d sondagens)'
          % (len(tokens2), len(validas), len(tokens2) * len(validas)))

    fila, achados, trava = queue.Queue(), [], threading.Lock()
    for x in tokens2:
        fila.put(x)

    def trabalha():
        while True:
            try:
                t, nome, pais = fila.get_nowait()
            except queue.Empty:
                return
            for f in validas:
                try:
                    r = FAMILIAS[f](t)
                except Exception:
                    r = None
                if r:
                    with trava:
                        achados.append((nome, pais, t) + r)
                        print('   ACHOU %-16s %-18s %-30s %s vagas'
                              % (r[0], t, nome[:28], r[2]))
            fila.task_done()

    ths = [threading.Thread(target=trabalha, daemon=True) for _ in range(LINHAS)]
    [t.start() for t in ths]
    [t.join() for t in ths]

    print('\n== %d quadros vivos achados' % len(achados))
    com = [a for a in achados if a[5]]
    print('== %d deles COM vaga publicada' % len(com))
    with open('/tmp/claude-0/quadros-novos.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['nome', 'pais', 'token', 'familia', 'url', 'vagas'])
        w.writerows(sorted(achados, key=lambda a: -a[5]))
    print('gravado em /tmp/claude-0/quadros-novos.csv')
    return 0


if __name__ == '__main__':
    sys.exit(main())
