#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sonda ROTA DE BANCO DE TALENTOS (Pinpoint e Teamtailor Connect) a partir de um CSV de nomes.
Nasceu em 19/09 as 17h00 (Jhon A, 33o turno) porque a varredura de bancos de 10/09 gerou slug
dos CSVs de estudio DAQUELA data, e censos novos (censo-artstation-1709.csv, censo-guilde-quebec-1709.csv,
censo-wikidata.csv) nunca tiveram slug gerado - e foi dai que sairam Timberline e Coatsink.

Uso:
  python3 automacao/sonda-slug-bancos.py pinpoint   automacao/censo-artstation-1709.csv slug
  python3 automacao/sonda-slug-bancos.py teamtailor automacao/censo-artstation-1709.csv slug

AS TRES ARMADILHAS MEDIDAS, e sem elas o resultado mente:
 1. CONTA DE DEMONSTRACAO. No Pinpoint a assinatura e `ACME`/`Hooli` nas divisions (regra de
    10/09). No TEAMTAILOR a assinatura foi achada HOJE e e o locatario `faraway`: titulo
    "Far Far Away", departamentos "Ogre Affairs", "Wranglin' Manager", "Test Connect Department",
    "Test Connect - 2", e a unica vaga chamada "Fairytale Wrangler". Quadro com "Test Connect"
    ou nome de conto de fadas nos departamentos e DEMO, nao casa.
 2. SLUG QUE RESPONDE 200 QUASE NUNCA E A CASA QUE O NOME SUGERE (regra do 22o turno). Confira a
    IDENTIDADE pelo <title> e pelo site antes de enfileirar: em 19/09, das 7 rotas reais do
    Pinpoint, ZERO era casa de jogo ou animacao em escopo.
 3. 302 na rota do Pinpoint quer dizer BANCO DE TALENTOS DESLIGADO, nao quadro inexistente;
    404 limpo e que prova que o locatario nao existe.
"""
import csv, sys, re, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                    '(KHTML, like Gecko) Chrome/128.0 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml'}
ROTA = {'pinpoint':   'https://{s}.pinpointhq.com/register-your-interest/new',
        'teamtailor': 'https://{s}.teamtailor.com/connect'}
SUFIXOS = ('-studios', '-studio', '-games', '-entertainment', '-interactive', '-animation')
DEMO = re.compile(r'Ogre Affairs|Wranglin|Test Connect|Fairytale Wrangler', re.I)


def slugs_do_csv(caminho, coluna):
    fora = set()
    for r in csv.DictReader(open(caminho, encoding='utf-8')):
        v = (r.get(coluna) or '').strip()
        if not v:
            continue
        base = re.sub(r'[^a-z0-9]+', '-', v.lower()).strip('-')
        fora.add(base)
        fora.add(base.replace('-', ''))
        for suf in SUFIXOS:
            if base.endswith(suf):
                fora.add(base[:-len(suf)])
                fora.add(base[:-len(suf)].replace('-', ''))
    return sorted(fora)


def main():
    fam, csvf, col = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else 'slug')
    todos = slugs_do_csv(csvf, col)
    print('slugs a sondar: %d' % len(todos), file=sys.stderr)

    def um(s):
        try:
            r = urllib.request.Request(ROTA[fam].format(s=s), headers=UA)
            resp = urllib.request.urlopen(r, timeout=25)
            return (s, resp.status, resp.geturl(), resp.read().decode('utf-8', 'replace'))
        except urllib.error.HTTPError as e:
            return (s, e.code, '', '')
        except Exception:
            return (s, 0, '', '')

    vivos = []
    with ThreadPoolExecutor(max_workers=20) as ex:
        n = 0
        for s, c, url, corpo in ex.map(um, todos):
            n += 1
            if n % 500 == 0:
                print('.. %d' % n, file=sys.stderr)
            if c != 200:
                continue
            tit = re.search(r'<title>(.*?)</title>', corpo, re.S)
            tit = (tit.group(1).strip().replace('\n', ' ') if tit else '')[:70]
            demo = bool(DEMO.search(corpo)) or ('ACME' in corpo and 'Hooli' in corpo)
            vivos.append((s, 'DEMO' if demo else 'REAL', url, tit))
    print('ROTAS COM 200: %d' % len(vivos))
    for v in sorted(vivos):
        print('\t'.join(v))


if __name__ == '__main__':
    main()
