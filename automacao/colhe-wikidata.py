#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""COLHE-WIKIDATA — fonte NOVA de nomes de estúdio, estruturada e global.

POR QUE ISTO EXISTE. Em 15/09 o Vini cobrou: *"precisamos de mais formularios, ta mt lento"*.
Ele está certo, e a causa foi diagnosticada nesse mesmo dia: **a campanha só descobre porta de
um jeito, adivinhando NOME DE ESTÚDIO** contra as APIs de ATS. Já foram 62.891 slugs no
Greenhouse, 9.643 no Personio, 15.010 no SmartRecruiters/Pinpoint/Breezy, 20.077 numa rodada só.
Esse universo veio de listas que a campanha já tinha (gamedevmap, a planilha de 6.624 estúdios,
os diretórios nórdico e irlandês), e está **esgotado**: varrer de novo devolve o mesmo zero.

**O gargalo não é a varredura, é o ESTOQUE DE NOMES.** E as fontes que resolveriam isso pelo
lado do anúncio estão todas fechadas para esta rede, cada uma medida em 15/09:
ArtStation Jobs devolve 403 "One more step" **inclusive em navegador de verdade** (não era só
curl, como o registro de 07/09 supunha); o Workable devolve `error code: 1015` da Cloudflare em
curl E em navegador; e o Bing **ignora o operador `site:`** vindo daqui, devolvendo character.ai
para uma busca por `site:job-boards.greenhouse.io`. Agregador geral aberto (arbeitnow, remotive,
jobicy, himalayas, WeWorkRemotely) responde, mas 1.246 vagas lidas deram **zero** da disciplina:
são quadros de tecnologia remota, não de arte 3D.

**O que sobrou aberto, e é muito:** o Wikidata. Ele é estruturado, global, gratuito, responde
200 desta rede, e a campanha **nunca o tocou** (zero menções no registro antes de hoje). Ele dá
nome, país e, o que mais importa, **site oficial** — e do site sai o domínio, que é token de ATS
de graça e ainda permite abrir a página de carreiras da própria casa.

**ARMADILHA MEDIDA, e ela decide o formato deste arquivo:** o endpoint limita a
**1 requisição por minuto** e devolve HTTP 429 com a frase *"Aggressively rate-limiting to
1 req / min"*. Por isso aqui se faz POUCAS consultas GRANDES, com espera de 65 s entre elas, e
nunca uma consulta por classe. 429 lido como "classe vazia" seria zero falso.

    python3 automacao/colhe-wikidata.py                  # colhe e grava o CSV
    python3 automacao/colhe-wikidata.py --saida x.csv
"""
import csv
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/128.0 Safari/537.36 campanha-vini-cavalcanti')
ENDPOINT = 'https://query.wikidata.org/sparql'
ESPERA = 65  # o limite medido e 1 req/min; 65s da folga

# O RECORTE GEOGRAFICO E O DO BRIEFING, e ele nao se afrouxa aqui: America do Norte, Europa
# (UK, Irlanda, Nordicos, UE), Oceania, e na Asia so Coreia do Sul e Singapura.
# NADA de India, Brasil nem Japao.
PAISES = {
    'United States of America', 'United States', 'Canada',
    'United Kingdom', 'Ireland', 'France', 'Germany', 'Spain', 'Portugal', 'Italy',
    'Netherlands', 'Belgium', 'Luxembourg', 'Switzerland', 'Austria', 'Poland',
    'Czech Republic', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Bulgaria', 'Croatia',
    'Slovenia', 'Greece', 'Estonia', 'Latvia', 'Lithuania', 'Sweden', 'Norway', 'Denmark',
    'Finland', 'Iceland', 'Australia', 'New Zealand', 'South Korea', 'Singapore',
    'Malta', 'Cyprus', 'Serbia', 'Ukraine',
}

# uma consulta por bloco de classes, poucas e grandes por causa do limite de 1 req/min
CONSULTAS = [
    ('animacao_e_vfx', """
SELECT DISTINCT ?itemLabel ?countryLabel ?site WHERE {
  VALUES ?classe { wd:Q1107679 wd:Q368290 }
  ?item wdt:P31/wdt:P279* ?classe .
  OPTIONAL { ?item wdt:P17 ?country . }
  OPTIONAL { ?item wdt:P856 ?site . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,fr,de,es,pt,sv,no,da,fi,nl" }
}"""),
    ('jogos', """
SELECT DISTINCT ?itemLabel ?countryLabel ?site WHERE {
  ?item wdt:P31/wdt:P279* wd:Q210167 .
  OPTIONAL { ?item wdt:P17 ?country . }
  OPTIONAL { ?item wdt:P856 ?site . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,fr,de,es,pt,sv,no,da,fi,nl" }
}"""),
]


def sparql(q, tentativas=3):
    """Uma consulta. 429 NAO e resposta vazia: espera e tenta de novo, e diz em voz alta."""
    u = ENDPOINT + '?format=json&query=' + urllib.parse.quote(q)
    req = urllib.request.Request(u, headers={'User-Agent': UA,
                                             'Accept': 'application/sparql-results+json'})
    for n in range(tentativas):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.loads(r.read().decode('utf8', 'replace'))['results']['bindings']
        except Exception as e:
            msg = str(e)[:80]
            if '429' in msg and n < tentativas - 1:
                print('   429 (1 req/min). Esperando %ds e tentando de novo...' % ESPERA)
                time.sleep(ESPERA)
                continue
            print('   NAO CONFERIDO: %s' % msg)
            return None
    return None


def token(nome):
    """Nome de casa -> slug de ATS. Mesma forma que as varreduras da campanha ja usam."""
    t = re.sub(r'[^a-z0-9]+', '', (nome or '').lower())
    return t


def dominio(url):
    m = re.search(r'https?://(?:www\.)?([^/]+)', url or '')
    return m.group(1).lower() if m else ''


def main():
    saida = 'automacao/censo-wikidata.csv'
    if '--saida' in sys.argv:
        saida = sys.argv[sys.argv.index('--saida') + 1]
    linhas, vistos = [], set()
    for i, (rotulo, q) in enumerate(CONSULTAS):
        if i:
            print('esperando %ds por causa do limite de 1 req/min...' % ESPERA)
            time.sleep(ESPERA)
        print('consultando %s ...' % rotulo)
        r = sparql(q)
        if r is None:
            print('%-16s NAO CONFERIDO (a consulta nao respondeu)' % rotulo)
            continue
        dentro = 0
        for b in r:
            nome = b.get('itemLabel', {}).get('value', '')
            pais = b.get('countryLabel', {}).get('value', '')
            site = b.get('site', {}).get('value', '')
            if not nome or nome.startswith('Q'):
                continue
            if pais and pais not in PAISES:
                continue
            chave = (nome.lower(), pais)
            if chave in vistos:
                continue
            vistos.add(chave)
            dentro += 1
            linhas.append([nome, pais, site, dominio(site), token(nome), rotulo])
        print('%-16s %5d itens lidos | %4d dentro do recorte geografico' % (rotulo, len(r), dentro))

    if not linhas:
        print('\nNada colhido. Isto NAO e "o Wikidata nao tem estudio": confira acima se alguma')
        print('consulta saiu como NAO CONFERIDO, porque 429 lido como zero e zero falso.')
        return 1
    cam = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', saida.split('/')[-1]) \
        if saida.startswith('automacao/') else saida
    cam = saida
    with open(cam, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['nome', 'pais', 'site', 'dominio', 'token', 'classe'])
        w.writerows(sorted(linhas))
    print('\n%d casas gravadas em %s' % (len(linhas), cam))
    print('%d com site oficial publicado' % sum(1 for l in linhas if l[2]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
