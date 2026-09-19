#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VIGIA DO JOB BOARD 2.0 (Chris Mayne, Looker Studio) — pedido do Vini em 19/09/2026 01h15 UTC.

O relatorio https://datastudio.google.com/reporting/2f39b56e-7393-4aa2-9fd5-bf8bf615c95f/page/5koHB
e uma tabela de vagas de animacao, VFX e jogos mantida a mao por Chris Mayne, muito acessada: quando
uma vaga entra, so os primeiros candidatos tem chance. Por isso o vigia roda a cada poucos minutos e
quem achar vaga nova da disciplina aplica NA HORA.

COMO LE: a tela e um app JS, mas os dados vem de um unico POST publico em
https://datastudio.google.com/batchedDataV2 (sem login, medido em 19/09 01h25 UTC: 200, 687 KB,
2.842 linhas, 11 colunas). O corpo do POST foi capturado do navegador e vive em
automacao/jobboard-mayne-post.json. Se o Google mudar o appVersion ou o corpo, o replay volta 4xx ou
vazio: ai o caminho e recapturar com `cd /home/user/apply && sh hb_run.sh ls_probe.js <url> ls/jb`.

COLUNAS (na ordem do POST): studio, city, region, country, title, level, mode, date (AAAA-MM-DD),
source (URL ou email), software, notes.

ESTADO: automacao/jobboard-mayne-visto.json guarda a chave de toda linha ja vista. Linha nova e
gravada em automacao/jobboard-mayne-novas.jsonl (uma por linha, com a marca `disciplina`) e impressa.
Primeira execucao: as linhas com data nos ultimos 2 dias saem como novas (podem ainda estar abertas);
o resto e so registrado como visto.

Uso: python3 automacao/jobboard-mayne.py            # roda e imprime as novas
     python3 automacao/jobboard-mayne.py --seco      # so mede, nao grava estado
Saida: ultima linha `NOVAS <n> DISCIPLINA <m>`; codigo 0 sempre que a leitura deu certo, 2 se falhou.
"""
import hashlib, json, os, re, subprocess, sys, datetime

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
POST = os.path.join(RAIZ, 'automacao', 'jobboard-mayne-post.json')
VISTO = os.path.join(RAIZ, 'automacao', 'jobboard-mayne-visto.json')
NOVAS = os.path.join(RAIZ, 'automacao', 'jobboard-mayne-novas.jsonl')
URL = 'https://datastudio.google.com/batchedDataV2?appVersion=20260914_0100'
REF = 'https://datastudio.google.com/reporting/2f39b56e-7393-4aa2-9fd5-bf8bf615c95f/page/5koHB'
COLS = ['studio', 'city', 'region', 'country', 'title', 'level', 'mode', 'date', 'source', 'software', 'notes']
DISC = re.compile(r'character|creature|modeler|modeller|modeling|modelling|sculpt|groom|texture|texturing|surfacing|look ?dev|lookdev|vis(ual)? ?dev|3d artist|generalist|asset artist|prop', re.I)
FORA = re.compile(r'animator|compositor|rigg|lighting|fx artist|effects|producer|recruit|hr |finance|engineer|programmer|developer|designer|writer|editor|matte|roto|prep|layout|storyboard|concept', re.I)
SECO = '--seco' in sys.argv

def baixar():
    body = open(POST, 'rb').read()
    r = subprocess.run(['curl', '-sS', '--max-time', '90', '-X', 'POST', URL, '-H', 'content-type: application/json',
                        '-H', 'origin: https://datastudio.google.com', '-H', 'referer: ' + REF, '--data-binary', '@-'],
                       input=body, capture_output=True)
    txt = r.stdout.decode('utf-8', 'ignore')
    if r.returncode != 0 or '{' not in txt:
        raise RuntimeError('curl %d: %s' % (r.returncode, (r.stderr.decode('utf-8', 'ignore') or txt)[:200]))
    j = json.loads(txt[txt.index('{'):])
    ds = j['dataResponse'][0]['dataSubset'][0]['dataset']['tableDataset']
    cols = []
    for c in ds['column']:
        v = None
        for k in ('stringColumn', 'dateColumn', 'doubleColumn', 'longColumn'):
            if k in c:
                v = list(c[k]['values'])
                for i in c.get('nullIndex', []): v.insert(i, None)
        cols.append(v or [])
    n = max(len(c) for c in cols)
    linhas = []
    for i in range(n):
        d = {COLS[k]: (cols[k][i] if i < len(cols[k]) else None) for k in range(len(COLS))}
        linhas.append(d)
    return linhas, ds.get('totalCount')

def chave(d):
    base = '|'.join(str(d.get(k) or '').strip().lower() for k in ('studio', 'title', 'city', 'date', 'source'))
    return hashlib.sha1(base.encode()).hexdigest()[:16]

def main():
    try:
        linhas, total = baixar()
    except Exception as e:
        print('FALHA NA LEITURA: %s' % e); print('NOVAS 0 DISCIPLINA 0 (NAO CONFERIDO)'); return 2
    if not linhas:
        print('resposta vazia: NAO e zero, e leitura quebrada'); print('NOVAS 0 DISCIPLINA 0 (NAO CONFERIDO)'); return 2
    visto = {}
    if os.path.exists(VISTO):
        visto = json.load(open(VISTO, encoding='utf-8'))
    primeira = not visto
    hoje = datetime.date.today()
    novas = []
    for d in linhas:
        k = chave(d)
        if k in visto: continue
        visto[k] = d.get('date') or ''
        if primeira:
            try: dt = datetime.date.fromisoformat(d.get('date') or '')
            except Exception: dt = None
            if not dt or (hoje - dt).days > 2: continue
        t = d.get('title') or ''
        d['disciplina'] = bool(DISC.search(t)) and not (FORA.search(t) and not re.search(r'character|creature|model', t, re.I))
        novas.append(d)
    if not SECO:
        json.dump(visto, open(VISTO, 'w', encoding='utf-8'))
        if novas:
            with open(NOVAS, 'a', encoding='utf-8') as f:
                for d in novas:
                    d['visto_em'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ')
                    f.write(json.dumps(d, ensure_ascii=False) + '\n')
    print('linhas lidas: %d (totalCount %s), vistas antes: %d, primeira execucao: %s' % (len(linhas), total, len(visto) - len(novas), primeira))
    for d in sorted(novas, key=lambda x: (not x['disciplina'], x.get('date') or ''), reverse=False):
        print(('  ** DISCIPLINA ' if d['disciplina'] else '     ') + '%s | %s | %s, %s | %s | %s | %s | %s' % (
            d.get('date'), d.get('title'), d.get('city'), d.get('country'), d.get('level'), d.get('mode'), d.get('studio'), d.get('source')))
        if d.get('notes'): print('        nota: ' + str(d.get('notes'))[:220])
    print('NOVAS %d DISCIPLINA %d' % (len(novas), sum(1 for d in novas if d['disciplina'])))
    return 0

if __name__ == '__main__':
    sys.exit(main())
