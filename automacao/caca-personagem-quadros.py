# -*- coding: utf-8 -*-
# Varredura PERSONAGEM PRIMEIRO: relê os 123 quadros do censo de 08/09 na fonte oficial
# e devolve SÓ o que é personagem, criatura, groom ou cabelo no TÍTULO.
# Nada de ambiente, prop, level art, hard surface ou generalista.
import json, re, sys, urllib.request, urllib.error, csv
from concurrent.futures import ThreadPoolExecutor

CENSO = '/home/user/workbenchMA/automacao/censo-boards-0809.csv'
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Accept': 'application/json'}

# o título tem de conter uma destas
ALVO = re.compile(r'\b(character|characters|creature|creatures|groom|grooming|hair|fur|'
                  r'personnage|personagem|personaje)\b', re.I)
# ...e não pode ser nenhuma destas
FORA = re.compile(r'\b(concept|2d|design(er)?\b(?!.*3d)|rigger|rigging|animator|animation\s+(?!.*character\s+art)|'
                  r'technical\s+animator|cfx|simulation|programmer|engineer|producer|recruiter|'
                  r'writer|qa|marketing|intern|internship|student|trainee|junior)\b', re.I)


def get(u, timeout=35):
    try:
        return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=timeout).read().decode('utf-8', 'replace')
    except Exception as e:
        return '__ERR__' + repr(e)[:90]


def gh(tok):
    d = get('https://boards-api.greenhouse.io/v1/boards/%s/jobs' % tok)
    if d.startswith('__ERR__'):
        return [('greenhouse', tok, d, '', '', '')]
    out = []
    for j in json.loads(d).get('jobs', []):
        out.append(('greenhouse', tok, j.get('title', ''), (j.get('location') or {}).get('name', ''),
                    j.get('absolute_url', ''), j.get('first_published') or j.get('updated_at') or ''))
    return out


def lever(tok):
    for host in ('api.lever.co', 'api.eu.lever.co'):
        d = get('https://%s/v0/postings/%s?mode=json' % (host, tok))
        if d.startswith('__ERR__') or not d.strip().startswith('['):
            continue
        out = []
        for j in json.loads(d):
            out.append(('lever', tok, j.get('text', ''), (j.get('categories') or {}).get('location', ''),
                        j.get('hostedUrl', ''), str(j.get('createdAt', ''))))
        return out
    return [('lever', tok, '__ERR__sem resposta', '', '', '')]


def ashby(tok):
    d = get('https://api.ashbyhq.com/posting-api/job-board/%s?includeCompensation=true' % tok)
    if d.startswith('__ERR__'):
        return [('ashby', tok, d, '', '', '')]
    out = []
    for j in json.loads(d).get('jobs', []):
        out.append(('ashby', tok, j.get('title', ''), j.get('location', ''),
                    j.get('jobUrl', ''), j.get('publishedAt', '')))
    return out


def bamboo(tok):
    d = get('https://%s.bamboohr.com/careers/list' % tok)
    if d.startswith('__ERR__'):
        return [('bamboohr', tok, d, '', '', '')]
    out = []
    try:
        r = json.loads(d).get('result', [])
    except Exception:
        return [('bamboohr', tok, '__ERR__json', '', '', '')]
    for j in r:
        loc = j.get('location') or {}
        out.append(('bamboohr', tok, j.get('jobOpeningName', ''),
                    ', '.join(x for x in [loc.get('city'), loc.get('state'), loc.get('country')] if x),
                    'https://%s.bamboohr.com/careers/%s' % (tok, j.get('id')), ''))
    return out


def smartr(tok):
    out, off = [], 0
    while True:
        d = get('https://api.smartrecruiters.com/v1/companies/%s/postings?limit=100&offset=%d' % (tok, off))
        if d.startswith('__ERR__'):
            return out or [('smartrecruiters', tok, d, '', '', '')]
        j = json.loads(d)
        for p in j.get('content', []):
            loc = p.get('location') or {}
            out.append(('smartrecruiters', tok, p.get('name', ''),
                        ', '.join(x for x in [loc.get('city'), loc.get('country')] if x),
                        'https://jobs.smartrecruiters.com/%s/%s' % (tok, p.get('id')),
                        p.get('releasedDate', '')))
        off += 100
        if off >= j.get('totalFound', 0) or off > 500:
            break
    return out


def teamtailor(tok):
    d = get('https://%s.teamtailor.com/jobs.json' % tok)
    if d.startswith('__ERR__'):
        return [('teamtailor', tok, d, '', '', '')]
    try:
        j = json.loads(d)
    except Exception:
        return [('teamtailor', tok, '__ERR__json', '', '', '')]
    arr = j if isinstance(j, list) else j.get('jobs', [])
    out = []
    for p in arr:
        out.append(('teamtailor', tok, p.get('title', ''), str(p.get('location', '')),
                    p.get('url', ''), str(p.get('created-at', p.get('createdAt', '')))))
    return out


def recruitee(tok):
    d = get('https://%s.recruitee.com/api/offers/' % tok)
    if d.startswith('__ERR__'):
        return [('recruitee', tok, d, '', '', '')]
    out = []
    for p in json.loads(d).get('offers', []):
        out.append(('recruitee', tok, p.get('title', ''), p.get('location', ''),
                    p.get('careers_url', ''), p.get('published_at', '')))
    return out


def breezy(tok):
    d = get('https://%s.breezy.hr/json' % tok)
    if d.startswith('__ERR__'):
        return [('breezy', tok, d, '', '', '')]
    try:
        arr = json.loads(d)
    except Exception:
        return [('breezy', tok, '__ERR__json', '', '', '')]
    out = []
    for p in arr:
        out.append(('breezy', tok, p.get('name', ''), str((p.get('location') or {}).get('name', '')),
                    p.get('url', ''), p.get('published_date', '')))
    return out


F = {'greenhouse': gh, 'lever': lever, 'ashby': ashby, 'bamboohr': bamboo,
     'smartrecruiters': smartr, 'teamtailor': teamtailor, 'recruitee': recruitee, 'breezy': breezy}

pares = set()
with open(CENSO, encoding='utf-8') as fh:
    for row in csv.DictReader(fh):
        if row['ats'] in F:
            pares.add((row['ats'], row['token']))
pares = sorted(pares)
print('quadros a reler:', len(pares), file=sys.stderr)


def um(p):
    ats, tok = p
    try:
        return F[ats](tok)
    except Exception as e:
        return [(ats, tok, '__ERR__' + repr(e)[:80], '', '', '')]


tudo = []
with ThreadPoolExecutor(max_workers=12) as ex:
    for r in ex.map(um, pares):
        tudo.extend(r)

erros = [t for t in tudo if t[2].startswith('__ERR__')]
vivas = [t for t in tudo if not t[2].startswith('__ERR__')]
print('linhas lidas:', len(vivas), '| quadros com erro:', len(erros), file=sys.stderr)

hits = [t for t in vivas if ALVO.search(t[2] or '') and not FORA.search(t[2] or '')]
with open('/tmp/claude-0/-home-user-workbenchMA/98c8eec1-87ea-55f1-bd77-423c5af62326/scratchpad/personagem_hits.csv',
          'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['ats', 'token', 'titulo', 'local', 'url', 'data'])
    for h in sorted(hits, key=lambda x: (x[0], x[1])):
        w.writerow(h)
print('ACERTOS DE PERSONAGEM:', len(hits), file=sys.stderr)
for h in sorted(hits, key=lambda x: (x[0], x[1])):
    print(' | '.join(str(x)[:70] for x in h))
print('--- erros ---', file=sys.stderr)
for e in erros[:20]:
    print(e[0], e[1], e[2][:70], file=sys.stderr)
