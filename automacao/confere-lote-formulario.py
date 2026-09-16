#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CONFERE-LOTE-FORMULARIO — a regua do `confere-carta.py`, aplicada a texto de CAMPO DE
FORMULARIO em lote, mais UMA guarda que a regua de email nao tem: o CACA-INVENCAO.

POR QUE NASCEU, em 16/09. O Vini cobrou o buraco que sobrou na pagina de cliques:
*"nessa fila de cliques n tem as cartas de recomendacoes e bio (texto) especificas pra cada
estudio"*. A pagina tinha os 77 enderecos e, em 43 deles, a resposta de cada campo, mas nao
tinha O TEXTO que ele cola no campo de cover letter e no de "tell us about yourself". Escrever
77 cartas e trabalho de agente; conferir 77 cartas e trabalho de maquina, e e este arquivo.

**O CACA-INVENCAO E O CORACAO DISTO.** O risco de carta escrita em lote nao e floreio, e MENTIRA
DE CASA: atribuir ao estudio um filme, um premio, um cliente ou um fundador que ele nunca teve.
Isso queima a candidatura de um jeito que carta generica nao queima. A guarda e mecanica: todo
nome proprio da carta tem de aparecer NA PROVA daquela porta (o `nota` e o `dossie`, que sairam
de leitura do anuncio real) ou na lista fechada dos fatos do proprio Vini. O que sobrar sai na
tela para olho humano. Nome proprio que ninguem consegue apontar na prova NAO SAI pelo fio.

A regra de emoji aqui e a do tipo `ats`, e ela e ZERO, nao "pouco".

    python3 automacao/confere-lote-formulario.py /tmp/claude-0/cartas-mao
"""
import glob
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib import import_module

cc = import_module('confere-carta') if os.path.exists(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'confere-carta.py')) else None

TETO_CARTA = 250
FAIXA_BIO = (60, 110)
FAIXA_CURTA = (22, 55)

FRASE_PORTFOLIO = ('my portfolio holds more than 45 projects with over 60 characters '
                   'across many titles')

# Fatos do proprio Vini: nome proprio daqui e dele, nao da casa, e por isso nao e invencao.
MEUS = {
    'vini', 'cavalcanti', 'vinicius', 'wingfeather', 'saga', 'angel', 'studios', 'endstar',
    'eline', 'e-line', 'media', 'arizona', 'houdini', 'maya', 'zbrush', 'substance', 'painter',
    'designer', 'marmoset', 'blender', 'photoshop', 'mari', 'puga', 'ielts', 'artstation',
    'linkedin', 'uvs', 'uv', 'udim', 'udims', 'pbr', 'lod', 'lods', 'ma', 'pg', 'dip',
}
# Palavras que comecam frase em ingles e nao sao nome proprio de ninguem.
COMUNS = set("""a an the i my me we our you your they their he she it its this that these those
and but so then now if when while where what which who whose because since as at in on of for
to from with without into over under after before both each every most more much many one two
three four five ten first second next last same other another all any no not nor only just also
even still yet than too very there here how why do does did done doing have has had having be
been being am is are was were will would can could should shall may might must let make made
work working worked character characters model modelling modeling modelled modeled sculpt
sculpting texture texturing groom grooming asset assets team teams studio studios game games
film films show shows role roles job jobs year years day days time times new senior artist
artists art pipeline engine screen work-ready""".split())


def normaliza(t):
    return unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode('ascii')


def palavras(t):
    return len(re.findall(r"[A-Za-z'’]+", t))


def nomes_proprios(t):
    """Token capitalizado que nao e comum. Inclui inicio de frase de proposito: e melhor
    mostrar demais e o humano descartar do que deixar passar uma invencao."""
    saida = []
    for m in re.finditer(r"\b([A-Z][A-Za-z'’&.-]{1,})\b", normaliza(t)):
        w = m.group(1)
        if w.lower().strip(".'-") in COMUNS or w.lower() in MEUS:
            continue
        saida.append(w)
    return saida


def shingles(t, n=6):
    p = re.findall(r'[a-z]+', normaliza(t).lower())
    return {tuple(p[i:i + n]) for i in range(max(0, len(p) - n + 1))}


def main():
    pasta = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/cartas-mao'
    provas = {}
    for f in sorted(glob.glob(os.path.join(pasta, 'lote-*.json'))):
        for p in json.load(open(f, encoding='utf-8')):
            provas[p['id']] = normaliza(' '.join(
                str(p.get(k) or '') for k in ('casa', 'vaga', 'pais', 'url', 'nota', 'dossie'))).lower()
    cartas = []
    for f in sorted(glob.glob(os.path.join(pasta, 'saida-*.json'))):
        try:
            cartas += json.load(open(f, encoding='utf-8'))
        except Exception as e:
            print('!! %s ilegivel: %s' % (os.path.basename(f), str(e)[:90]))
    print('== %d cartas lidas, %d portas com prova' % (len(cartas), len(provas)))
    if not cartas:
        return 2

    erros_tot, sus_tot = 0, 0
    for c in cartas:
        eid, casa = c.get('id'), c.get('casa', '?')
        prova = provas.get(eid, '')
        erros, avisos = [], []
        carta = c.get('carta') or ''
        bio = c.get('bio') or ''
        curta = c.get('bio_curta') or ''
        if not carta or not bio or not curta:
            erros.append('faltou texto: %s' % ', '.join(
                k for k in ('carta', 'bio', 'bio_curta') if not c.get(k)))

        n = palavras(carta)
        if n > TETO_CARTA:
            erros.append('carta com %d palavras, teto %d' % (n, TETO_CARTA))
        nb = palavras(bio)
        if not (FAIXA_BIO[0] <= nb <= FAIXA_BIO[1]):
            avisos.append('bio com %d palavras, faixa %d a %d' % ((nb, ) + FAIXA_BIO))
        nc = palavras(curta)
        if not (FAIXA_CURTA[0] <= nc <= FAIXA_CURTA[1]):
            avisos.append('bio_curta com %d palavras, faixa %d a %d' % ((nc, ) + FAIXA_CURTA))
        if FRASE_PORTFOLIO not in normaliza(bio).lower():
            erros.append('a bio nao tem a frase fixa de portfolio do briefing')

        junto = carta + '\n' + bio + '\n' + curta
        if cc:
            if cc.conta_emoji(junto):
                erros.append('EMOJI em campo de formulario: tipo ats e ZERO')
            for rx, porque in cc.PROIBIDAS:
                m = re.search(rx, junto)
                if m:
                    erros.append('%s :: "%s"' % (porque, m.group(0)))
            fl = [m.group(0) for rx in cc.FLOREIO for m in [re.search(rx, junto, re.I)] if m]
            if fl:
                erros.append('floreio de IA: ' + ', '.join('"%s"' % a for a in fl[:5]))
        if re.search(r'\b(salary|compensation|USD|EUR|GBP|CAD|AUD)\b', junto):
            erros.append('fala de salario ou moeda')
        if re.search(r'\b[A-Z]{4,}(?:\s+[A-Z]{2,}){2,}\b', junto):
            erros.append('frase em capslock')
        if re.search(r'(your|the)\s+(studio|team|company)\b', carta, re.I) and \
                len(set(nomes_proprios(carta))) < 3:
            avisos.append('fala em "your studio" e quase nao cita nome proprio: gancho fraco')

        # ---- CACA-INVENCAO
        suspeitos = sorted({w for w in nomes_proprios(carta + ' ' + bio)
                            if w.lower().strip(".'-") not in prova})
        if suspeitos:
            sus_tot += len(suspeitos)
            avisos.append('NOME PROPRIO FORA DA PROVA: ' + ', '.join(suspeitos[:12]))

        if erros or avisos:
            print('\n[%s] %s' % (eid, casa[:60]))
            for e in erros:
                print('   ERRO   %s' % e)
            for a in avisos:
                print('   aviso  %s' % a)
        erros_tot += len(erros)

    # ---- semelhanca entre cartas
    sh = {c['id']: shingles(c.get('carta') or '') for c in cartas}
    pares = []
    ids = sorted(sh)
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = sh[ids[i]], sh[ids[j]]
            if a and b:
                pares.append((len(a & b) / len(a | b), ids[i], ids[j]))
    pares.sort(reverse=True)
    print('\n== semelhanca entre cartas (6-shingles), os 8 piores pares')
    nomes = {c['id']: c.get('casa', '?')[:26] for c in cartas}
    for v, i, j in pares[:8]:
        print('   %3d%%  %-26s x %-26s' % (v * 100, nomes.get(i, i), nomes.get(j, j)))
    altos = [p for p in pares if p[0] > 0.55]
    if altos:
        print('   !! %d pares acima de 55%%: carta em serie, reescrever o paragrafo da ponte'
              % len(altos))

    print('\n== %d erros que impedem colar, %d nomes proprios para olho humano' % (erros_tot, sus_tot))
    return 1 if erros_tot else 0


if __name__ == '__main__':
    sys.exit(main())
