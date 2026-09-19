#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Varredura POR DATA das familias de ATS por API, janela configuravel.
Le automacao/tokens-ats-1809.csv. Grava CSV com flush a cada quadro.
Familias sem data na lista (ashby, bamboohr) saem com data vazia e sao
filtradas SO por palavra-chave.
"""
#
# 19/09 — VARREDURA POR DATA das familias de ATS por API, versionada porque cada rodada
# vinha reescrevendo a mesma coisa. Uso:
#     python3 automacao/varre-janela-ats.py /tmp/saida.csv
# A janela fica na constante JANELA. Grava com flush a cada quadro.
#
# AS DUAS ARMADILHAS QUE ELA CARREGA MEDIDAS, e sem elas o numero mente:
# 1. ASHBY, BAMBOOHR, PINPOINT e RIPPLING NAO TRAZEM DATA DE PUBLICACAO NA LISTAGEM. Em 19/09
#    isso eram 1.276 vagas de 8.431 sem data nenhuma. Para essas quatro familias a janela por
#    data NAO EXISTE: elas saem com na_janela=SEMDATA e tem de ser filtradas por palavra-chave
#    sobre o quadro INTEIRO. Escrever 'zero na janela' nelas e zero falso.
# 2. WORKABLE esta em SKIP. O 429 dele e limitador da Cloudflare por IP (error code 1015), com
#    Retry-After de horas, ja medido em navegador de verdade. O silencio dele nunca vira zero.
import csv, json, re, sys, os, urllib.request, urllib.error, time
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

import os as _os
TOK = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'tokens-ats-1809.csv')
OUT = sys.argv[1] if len(sys.argv) > 1 else '/tmp/janela.csv'
# JANELA: default 18/09 16h00 UTC, mas sobrescrita pelo ambiente JANELA_ISO
# (ex.: JANELA_ISO=2026-09-19T00:15:00+00:00) — 19/09 02h20, para nao editar codigo
# a cada rodada de janela curta.
_JI = os.environ.get('JANELA_ISO', '').strip()
JANELA = (datetime.fromisoformat(_JI) if _JI else datetime(2026, 9, 18, 16, 0, 0, tzinfo=timezone.utc))
if JANELA.tzinfo is None:
    JANELA = JANELA.replace(tzinfo=timezone.utc)
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125 Safari/537.36',
      'Accept': 'application/json,text/xml,*/*'}

SKIP = {'workable'}


def get(u, timeout=40, data=None, hdr=None):
    h = dict(UA)
    if hdr:
        h.update(hdr)
    try:
        r = urllib.request.Request(u, headers=h, data=data)
        return urllib.request.urlopen(r, timeout=timeout).read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        return '__HTTP%d__' % e.code
    except Exception as e:
        return '__ERR__' + repr(e)[:70]


def pdate(s):
    if not s:
        return None
    s = str(s).strip()
    if re.fullmatch(r'\d{12,13}', s):
        try:
            return datetime.fromtimestamp(int(s) / 1000.0, timezone.utc)
        except Exception:
            return None
    s = s.replace('Z', '+00:00')
    for f in (None,):
        try:
            d = datetime.fromisoformat(s)
            if d.tzinfo is None:
                d = d.replace(tzinfo=timezone.utc)
            return d
        except Exception:
            pass
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', s)
    if m:
        return datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), tzinfo=timezone.utc)
    return None


# ---------------- familias ----------------

def f_greenhouse(t):
    d = get('https://boards-api.greenhouse.io/v1/boards/%s/jobs?content=false' % t)
    if d.startswith('__'):
        return d, []
    try:
        js = json.loads(d).get('jobs', [])
    except Exception:
        return '__PARSE__', []
    return 'ok', [(str(j.get('id')), j.get('title', ''), (j.get('location') or {}).get('name', ''),
                   j.get('absolute_url', ''), j.get('first_published') or j.get('updated_at') or '') for j in js]


def f_lever(t):
    for host in ('api.lever.co', 'api.eu.lever.co'):
        d = get('https://%s/v0/postings/%s?mode=json' % (host, t))
        if d.startswith('__') or not d.strip().startswith('['):
            continue
        try:
            js = json.loads(d)
        except Exception:
            continue
        return 'ok', [(str(j.get('id')), j.get('text', ''), (j.get('categories') or {}).get('location', ''),
                       j.get('hostedUrl', ''), str(j.get('createdAt', ''))) for j in js]
    return '__semresposta__', []


ASHQ = ('query ApiJobBoardWithTeams($organizationHostedJobsPageName: String!) { jobBoard: '
        'jobBoardWithTeams(organizationHostedJobsPageName: $organizationHostedJobsPageName) '
        '{ jobPostings { id title locationName employmentType } } }')


def f_ashby(t):
    body = json.dumps({'operationName': 'ApiJobBoardWithTeams',
                       'variables': {'organizationHostedJobsPageName': t},
                       'query': ASHQ}).encode()
    d = get('https://jobs.ashbyhq.com/api/non-user-graphql?op=ApiJobBoardWithTeams', data=body,
            hdr={'Content-Type': 'application/json'})
    if d.startswith('__'):
        return d, []
    try:
        jb = json.loads(d).get('data', {}).get('jobBoard')
    except Exception:
        return '__PARSE__', []
    if not jb:
        return '__vazio__', []
    return 'ok', [(str(j.get('id')), j.get('title', ''), j.get('locationName', ''),
                   'https://jobs.ashbyhq.com/%s/%s' % (t, j.get('id')), '') for j in jb.get('jobPostings', [])]


def f_teamtailor(t):
    host = t if '.' in t else '%s.teamtailor.com' % t
    d = get('https://%s/jobs.json' % host)
    if d.startswith('__'):
        return d, []
    try:
        js = json.loads(d)
    except Exception:
        return '__PARSE__', []
    items = js.get('items') or js.get('jobs') or []
    return 'ok:' + (js.get('title') or ''), [(str(j.get('id')), j.get('title', ''),
                    ' / '.join([x for x in [j.get('summary', '')] if x])[:0] or (j.get('tags') and ','.join(j['tags']) or ''),
                    j.get('url', ''), j.get('date_published') or '') for j in items]


def f_recruitee(t):
    d = get('https://%s.recruitee.com/api/offers/' % t)
    if d.startswith('__'):
        return d, []
    try:
        js = json.loads(d)
    except Exception:
        return '__PARSE__', []
    offs = js.get('offers', [])
    nm = offs[0].get('company_name', '') if offs else ''
    return 'ok:' + str(nm), [(str(j.get('id')), j.get('title', ''),
                              '%s %s %s' % (j.get('city') or '', j.get('country') or '', 'REMOTE' if j.get('remote') else ''),
                              j.get('careers_url') or j.get('careers_apply_url') or '',
                              j.get('published_at') or j.get('created_at') or '') for j in offs]


def f_bamboohr(t):
    d = get('https://%s.bamboohr.com/careers/list' % t)
    if d.startswith('__'):
        return d, []
    try:
        js = json.loads(d)
    except Exception:
        return '__PARSE__', []
    out = []
    for j in js.get('result', []):
        loc = j.get('location') or {}
        out.append((str(j.get('id')), j.get('jobOpeningName', ''),
                    '%s %s %s' % (loc.get('city') or '', loc.get('state') or '', 'REMOTE' if j.get('isRemote') else ''),
                    'https://%s.bamboohr.com/careers/%s' % (t, j.get('id')), ''))
    return 'ok', out


def f_breezy(t):
    d = get('https://%s.breezy.hr/json' % t)
    if d.startswith('__'):
        return d, []
    try:
        js = json.loads(d)
    except Exception:
        return '__PARSE__', []
    if not isinstance(js, list):
        return '__naolista__', []
    out = []
    for j in js:
        loc = j.get('location') or {}
        c = (loc.get('city') or '') if isinstance(loc, dict) else str(loc)
        cc = ((loc.get('country') or {}) if isinstance(loc, dict) else {})
        cn = cc.get('name', '') if isinstance(cc, dict) else ''
        out.append((str(j.get('id') or j.get('friendly_id')), j.get('name', ''), '%s %s' % (c, cn),
                    j.get('url', ''), j.get('published_date') or ''))
    return 'ok', out


def f_smartrecruiters(t):
    out, off = [], 0
    tot = None
    while True:
        d = get('https://api.smartrecruiters.com/v1/companies/%s/postings?limit=100&offset=%d' % (t, off))
        if d.startswith('__'):
            return d, out
        try:
            js = json.loads(d)
        except Exception:
            return '__PARSE__', out
        tot = js.get('totalFound', 0)
        for j in js.get('content', []):
            loc = j.get('location') or {}
            out.append((str(j.get('id')), j.get('name', ''),
                        '%s %s %s %s' % (loc.get('city') or '', loc.get('region') or '', loc.get('country') or '',
                                         'REMOTE' if loc.get('remote') else ''),
                        'https://jobs.smartrecruiters.com/%s/%s' % (t, j.get('id')),
                        j.get('releasedDate') or ''))
        off += 100
        if off >= (tot or 0) or off > 1200:
            break
    return 'ok:tot%s' % tot, out


def f_pinpoint(t):
    d = get('https://%s.pinpointhq.com/postings.json' % t)
    if d.startswith('__'):
        return d, []
    try:
        js = json.loads(d)
    except Exception:
        return '__PARSE__', []
    out = []
    for j in js.get('data', []):
        a = j.get('attributes', j) if isinstance(j, dict) else {}
        out.append((str(a.get('id') or j.get('id')), a.get('title', ''),
                    '%s %s' % (a.get('location', {}).get('name', '') if isinstance(a.get('location'), dict) else (a.get('location') or ''),
                               a.get('workplace_type') or ''),
                    a.get('url', ''), a.get('published_at') or a.get('created_at') or ''))
    return 'ok', out


def f_rippling(t):
    d = get('https://api.rippling.com/platform/api/ats/v1/board/%s/jobs' % t)
    if d.startswith('__'):
        return d, []
    try:
        js = json.loads(d)
    except Exception:
        return '__PARSE__', []
    if not isinstance(js, list):
        return '__naolista__', []
    out = []
    for j in js:
        out.append((str(j.get('uuid') or j.get('id')), j.get('name', ''),
                    (j.get('workLocation') or {}).get('label', '') if isinstance(j.get('workLocation'), dict) else '',
                    j.get('url', ''), j.get('createdAt') or ''))
    return 'ok:' + str(js[0].get('companyName', '') if js else ''), out


def f_homerun(t):
    d = get('https://feed.homerun.co/%s' % t)
    if d.startswith('__'):
        return d, []
    out = []
    for m in re.finditer(r'<entry>(.*?)</entry>', d, re.S):
        b = m.group(1)
        ti = re.search(r'<title[^>]*>(.*?)</title>', b, re.S)
        li = re.search(r'<link[^>]*href="([^"]+)"', b)
        up = re.search(r'<(?:updated|published)>(.*?)</', b, re.S)
        idm = re.search(r'<id>(.*?)</id>', b, re.S)
        out.append(((idm.group(1) if idm else ''), (ti.group(1) if ti else '').strip(), '',
                    li.group(1) if li else '', (up.group(1) if up else '').strip()))
    return 'ok', out


def f_personio(t):
    for dom in ('com', 'de'):
        d = get('https://%s.jobs.personio.%s/xml' % (t, dom))
        if d.startswith('__') or '<position>' not in d:
            continue
        out = []
        for m in re.finditer(r'<position>(.*?)</position>', d, re.S):
            b = m.group(1)

            def g(tag):
                mm = re.search(r'<%s>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</%s>' % (tag, tag), b, re.S)
                return (mm.group(1).strip() if mm else '')
            out.append((g('id'), g('name'), '%s %s' % (g('office'), g('subcompany')),
                        'https://%s.jobs.personio.%s/job/%s' % (t, dom, g('id')), g('createdAt')))
        return 'ok', out
    return '__semfeed__', []


FAM = {'greenhouse': f_greenhouse, 'lever': f_lever, 'ashby': f_ashby, 'teamtailor': f_teamtailor,
       'recruitee': f_recruitee, 'bamboohr': f_bamboohr, 'breezy': f_breezy,
       'smartrecruiters': f_smartrecruiters, 'pinpoint': f_pinpoint, 'rippling': f_rippling,
       'homerun': f_homerun, 'personio': f_personio}

# palavras-chave
K1 = re.compile(r'\b(character|characters|creature|creatures|personagem|personnage|personaje)\b', re.I)
K2 = re.compile(r'\b(model+er|modeling|modelling|modeleur|surfacing|texture|texturing|'
                r'look\s*dev|lookdev|look\s*development|groom|grooming|hair\s*&?\s*fur|'
                r'sculptor|zbrush|visual\s*development|vis\s*dev)\b', re.I)
# K3 = ROTA ESPONTANEA. Achado do 23o turno (19/09 00h50): varredura por titulo de DISCIPLINA
# e cega para banco de talentos, que e a porta mais barata que existe. Sao DUAS varreduras.
K3 = re.compile(r'(open\s+application|general\s+application|spontaneous|speculative|unsolicited|'
                r'expression\s+of\s+interest|general\s+interest|talent\s*(pool|community|network)|'
                r'register\s+your\s+interest|initiative\s+application|future\s+opportunit)', re.I)


def main():
    pares = []
    extra = os.environ.get('EXTRA_TOKENS', '')
    with open(TOK, newline='', encoding='utf-8') as fh:
        for row in csv.DictReader(l for l in fh if not l.startswith('#')):
            fa = (row.get('familia') or '').strip().lower()
            tk = (row.get('token') or '').strip()
            if not fa or not tk or fa in SKIP or fa not in FAM:
                continue
            pares.append((fa, tk))
    if extra:
        for p in extra.split(','):
            if ':' in p:
                a, b = p.split(':', 1)
                pares.append((a.strip(), b.strip()))
    pares = sorted(set(pares))
    print('quadros a sondar: %d' % len(pares), flush=True)

    fh = open(OUT, 'w', newline='', encoding='utf-8')
    w = csv.writer(fh)
    w.writerow(['familia', 'token', 'estado', 'id', 'titulo', 'local', 'url', 'data', 'na_janela', 'kw'])
    stats = {}
    seen = set()

    def job(p):
        fa, tk = p
        try:
            st, jobs = FAM[fa](tk)
        except Exception as e:
            st, jobs = '__EXC__' + repr(e)[:60], []
        return fa, tk, st, jobs

    with ThreadPoolExecutor(max_workers=14) as ex:
        futs = [ex.submit(job, p) for p in pares]
        done = 0
        for fu in as_completed(futs):
            fa, tk, st, jobs = fu.result()
            done += 1
            s = stats.setdefault(fa, {'quadros': 0, 'vivos': 0, 'vagas': 0, 'janela': 0, 'kw': 0, 'semdata': 0})
            s['quadros'] += 1
            if st.startswith('ok'):
                s['vivos'] += 1
            for (jid, ti, lo, url, dt) in jobs:
                key = (fa, tk, jid)
                if key in seen:
                    continue
                seen.add(key)
                s['vagas'] += 1
                d = pdate(dt)
                nj = ''
                if d is None:
                    s['semdata'] += 1
                    nj = 'SEMDATA'
                elif d >= JANELA:
                    s['janela'] += 1
                    nj = 'SIM'
                kw = ''
                if K1.search(ti or ''):
                    kw = 'K1'
                elif K2.search(ti or ''):
                    kw = 'K2'
                elif K3.search(ti or ''):
                    kw = 'K3'
                if kw and (nj in ('SIM', 'SEMDATA')):
                    s['kw'] += 1
                    w.writerow([fa, tk, st[:40], jid, ti, lo, url, dt, nj, kw])
                    fh.flush()
                elif nj == 'SIM':
                    w.writerow([fa, tk, st[:40], jid, ti, lo, url, dt, nj, ''])
                    fh.flush()
            if done % 100 == 0:
                print('..%d/%d' % (done, len(pares)), flush=True)
    fh.close()
    print('\n=== ESTATISTICA POR FAMILIA ===', flush=True)
    tot = {'quadros': 0, 'vivos': 0, 'vagas': 0, 'janela': 0, 'kw': 0, 'semdata': 0}
    for fa in sorted(stats):
        s = stats[fa]
        for k in tot:
            tot[k] += s[k]
        print('%-16s quadros=%-4d vivos=%-4d vagas=%-6d janela=%-5d semdata=%-6d kwalvo=%d' %
              (fa, s['quadros'], s['vivos'], s['vagas'], s['janela'], s['semdata'], s['kw']), flush=True)
    print('%-16s quadros=%-4d vivos=%-4d vagas=%-6d janela=%-5d semdata=%-6d kwalvo=%d' %
          ('TOTAL', tot['quadros'], tot['vivos'], tot['vagas'], tot['janela'], tot['semdata'], tot['kw']), flush=True)


if __name__ == '__main__':
    main()
