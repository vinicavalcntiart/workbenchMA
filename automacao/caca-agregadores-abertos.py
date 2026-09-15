#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CACA-AGREGADORES-ABERTOS — acha porta de formulário buscando por VAGA, não por nome de casa.

POR QUE ISTO EXISTE, e é a resposta a uma cobrança do Vini em 15/09: *"precisamos de mais
formularios, ta mt lento"*. Ele está certo, e a causa não era falta de esforço. **A campanha
inteira descobre porta de um jeito só: ADIVINHANDO NOME DE ESTÚDIO** contra as APIs de ATS
(62.891 slugs no Greenhouse, 9.643 no Personio, 960 no Recruitee, e por aí). Esse universo está
esgotado, e varrer de novo devolve o mesmo zero com um custo cada vez maior.

**A VIRADA: procurar pela VAGA e deixar o anúncio revelar a casa.** Um agregador aberto devolve
o endereço de candidatura DE VERDADE, e esse endereço entrega o ATS de graça. Isso acha casas
cujo token jamais seria adivinhado, que é precisamente o buraco do método antigo.

**O que JÁ FOI minerado e não se repete aqui:** Hitmarker, gamejobs.co, RemoteGameJobs,
workwithindies, 80.lv e o Grackle. Todos são de JOGOS. As fontes abaixo são GERAIS, e é por isso
que entram: elas alcançam animação, VFX, publicidade e produto, onde também se modela personagem.

**A REGRA DE HONESTIDADE VALE IGUAL.** Agregador é fonte de TERCEIRO: o anúncio pode estar morto,
o título pode mentir e o nome da casa pode ser de intermediário. Nada aqui vira fila sem passar,
depois, pela régua de veto no anúncio INTEIRO da fonte oficial e pelo dedupe no minuto do clique.
O que este arquivo entrega é PISTA COM ENDEREÇO DE CANDIDATURA, não vaga aprovada.

    python3 automacao/caca-agregadores-abertos.py            # todas as fontes
    python3 automacao/caca-agregadores-abertos.py arbeitnow  # uma só
"""
import json
import re
import sys
import urllib.request

UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/128.0 Safari/537.36')

# PERSONAGEM PRIMEIRO. O título nunca decide sozinho, mas serve de peneira barata; quem decide
# é o corpo do anúncio, lido depois na fonte oficial.
DISC = re.compile(r'character|creature|3d artist|3d model|modeler|modeller|sculpt|groom|'
                  r'texture artist|look ?dev|surfacing|visual development', re.I)
# fora da disciplina, medido e escrito no briefing: CFX e simulação, rigging, concept 2D
FORA = re.compile(r'\brig(ging|ger)\b|creature fx|character fx|\bcfx\b|concept artist|'
                  r'2d animator|matte painter|technical artist|character design(er)?\b', re.I)

FAMILIAS = [('greenhouse', 'greenhouse.io'), ('lever', 'lever.co'), ('ashby', 'ashbyhq.com'),
            ('workday', 'myworkdayjobs'), ('smartrecruiters', 'smartrecruiters.com'),
            ('teamtailor', 'teamtailor.com'), ('recruitee', 'recruitee.com'),
            ('bamboohr', 'bamboohr.com'), ('workable', 'workable.com'),
            ('personio', 'personio'), ('jobvite', 'jobvite.com'), ('join', 'join.com'),
            ('breezy', 'breezy.hr'), ('jazzhr', 'applytojob.com'), ('pinpoint', 'pinpointhq'),
            ('dayforce', 'dayforcehcm'), ('gohire', 'gohire.io'), ('homerun', 'homerun.co'),
            ('recruiterbox', 'recruiterbox'), ('rippling', 'rippling.com')]


def pega(url, timeout=40):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': '*/*'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode('utf8', 'replace')


def familia(url):
    u = (url or '').lower()
    return next((n for n, p in FAMILIAS if p in u), '')


# --- as fontes. Cada uma devolve lista de (titulo, casa, url_de_candidatura, local) -----------

def arbeitnow():
    """Feed aberto e grande (2 MB numa página). Paginado por ?page=."""
    vagas, pagina = [], 1
    while pagina <= 8:
        try:
            st, corpo = pega('https://www.arbeitnow.com/api/job-board-api?page=%d' % pagina)
        except Exception as e:
            print('   arbeitnow NAO CONFERIDO na pagina %d: %s' % (pagina, str(e)[:60]))
            break
        d = json.loads(corpo)
        itens = d.get('data') or []
        if not itens:
            break
        for j in itens:
            vagas.append((j.get('title', ''), j.get('company_name', ''),
                          j.get('url', ''), ', '.join(j.get('location', '') or [])
                          if isinstance(j.get('location'), list) else (j.get('location') or '')))
        pagina += 1
    return vagas


def remotive():
    st, corpo = pega('https://remotive.com/api/remote-jobs?limit=1500')
    d = json.loads(corpo)
    return [(j.get('title', ''), j.get('company_name', ''), j.get('url', ''),
             j.get('candidate_required_location', '')) for j in d.get('jobs', [])]


def jobicy():
    st, corpo = pega('https://jobicy.com/api/v2/remote-jobs?count=100')
    d = json.loads(corpo)
    return [(j.get('jobTitle', ''), j.get('companyName', ''), j.get('url', ''),
             j.get('jobGeo', '')) for j in d.get('jobs', [])]


def himalayas():
    st, corpo = pega('https://himalayas.app/jobs/api?limit=100')
    d = json.loads(corpo)
    return [(j.get('title', ''), j.get('companyName', ''),
             j.get('applicationLink') or j.get('url', ''),
             ', '.join(j.get('locationRestrictions') or [])) for j in d.get('jobs', [])]


def weworkremotely():
    st, corpo = pega('https://weworkremotely.com/categories/remote-design-jobs.rss')
    itens = re.findall(r'(?is)<item>(.*?)</item>', corpo)
    saida = []
    for it in itens:
        t = re.search(r'(?is)<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it)
        u = re.search(r'(?is)<link>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>', it)
        titulo = (t.group(1) if t else '').strip()
        casa = titulo.split(':')[0].strip() if ':' in titulo else ''
        saida.append((titulo, casa, (u.group(1) if u else '').strip(), ''))
    return saida


FONTES = {'arbeitnow': arbeitnow, 'remotive': remotive, 'jobicy': jobicy,
          'himalayas': himalayas, 'weworkremotely': weworkremotely}


def main():
    quais = sys.argv[1:] or list(FONTES)
    total, acertos = 0, []
    for nome in quais:
        if nome not in FONTES:
            print('fonte desconhecida: %s' % nome)
            continue
        try:
            vagas = FONTES[nome]()
        except Exception as e:
            # resposta vazia NAO e zero: se a fonte falhou, isso se diz com estas palavras
            print('%-16s NAO CONFERIDO: %s' % (nome, str(e)[:70]))
            continue
        total += len(vagas)
        hits = [v for v in vagas if DISC.search(v[0]) and not FORA.search(v[0])]
        print('%-16s %5d vagas lidas | %2d da disciplina por titulo' % (nome, len(vagas), len(hits)))
        for t, casa, url, local in hits:
            acertos.append((nome, t, casa, url, local))

    print('\n== TOTAL lido: %d vagas | acertos de disciplina: %d' % (total, len(acertos)))
    if not acertos:
        print('   Zero MEDIDO: as fontes responderam e nao havia nada da disciplina.')
        return 0
    print('\n== ACERTOS, com a familia de ATS revelada pelo endereco de candidatura')
    for fonte, t, casa, url, local in acertos:
        fam = familia(url) or '(site proprio ou agregador)'
        print('\n  [%s] %s' % (fonte, t[:78]))
        print('     casa: %-34s local: %s' % (casa[:34], (local or '-')[:40]))
        print('     ATS:  %-16s %s' % (fam, url[:104]))
    print('\nLEMBRE: isto e PISTA, nao fila. Cada uma passa pela regua de veto no anuncio INTEIRO')
    print('da fonte oficial e pelo dedupe no minuto do clique antes de virar candidatura.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
