#!/usr/bin/env python3
"""Audita se toda candidatura por portal de um dia tem PROVA escrita na linha.

POR QUE EXISTE: o numero de candidaturas e a coisa que o Vini mais cobra, e linha sem prova
e candidatura que ninguem consegue defender depois. Este script le o enviados.csv e separa
as linhas de portal do dia em COM PROVA e SEM PROVA.

LICAO QUE ESTE ARQUIVO CARREGA, e ela ja custou tres sustos em 09/09: FALSO NEGATIVO DE REGEX
E O ERRO MAIS CARO DESTA CAMPANHA. Na primeira versao, esta auditoria acusou tres candidaturas
como "sem prova" (Cloud Imperium, Eyeline Seul e Netflix Sydney) e as tres tinham prova farta;
o que faltava era a regex conhecer o vocabulario do Workday. No mesmo dia a mesma familia de
defeito apareceu no verificador do GoHire, que deu NAO CONFIRMADA para uma candidatura ENVIADA
porque nao conhecia "Application Sent!", e antes disso na Scopely. A regra que fica: quando um
verificador acusar falha, o primeiro suspeito e o verificador.
"""
import csv, io, re, sys

DIA = sys.argv[1] if len(sys.argv) > 1 else '2026-09-09'
ARQ = sys.argv[2] if len(sys.argv) > 2 else 'enviados.csv'

# Vocabulario de prova, por familia de ATS. Acrescente aqui quando encontrar frase nova.
PROVA = re.compile(
    r'confirmation'                                  # Greenhouse, Breezy
    r'|thanks? for applying'                         # Teamtailor, Greenhouse
    r'|thank you for applying'
    r'|application (submitted|received|sent)'        # Workday, Scopely, GoHire
    r'|application has been received'
    r'|we have received|we\'ve received'
    r'|/thanks'                                      # Teamtailor
    r'|responses submitted'                          # Breezy
    r'|jobTasks/completed/application'               # WORKDAY: a URL e a prova
    r'|successfully been submitted'                  # Workday
    r'|you applied for this job'                     # Workday, marcador na propria vaga
    r'|currently evaluating your experience'         # Workday da Cloud Imperium
    r'|under review'                                 # area do candidato
    r'|POST 200|POST 204'                            # prova de rede
    r'|TRES PROVAS|DUAS PROVAS',                     # marcador escrito pelo proprio registro
    re.I)

linhas = [r for r in csv.reader(io.open(ARQ, encoding='utf8')) if r and r[0] == DIA]
portal = [r for r in linhas if any('portal' in c for c in r)]
sem = [r for r in portal if not PROVA.search(' '.join(r))]

print(f'{DIA}: {len(linhas)} linhas, {len(portal)} por portal')
print(f'  COM prova escrita: {len(portal) - len(sem)}')
print(f'  SEM prova escrita: {len(sem)}')
for r in sem:
    print('   !', r[1], '|', (r[2] if len(r) > 2 else '')[:60])
if sem:
    print('\nANTES DE CORRIGIR O REGISTRO, LEIA A LINHA INTEIRA: pode ser a regex que nao conhece')
    print('a frase de confirmacao daquele ATS. Falso negativo aqui e mais provavel que candidatura')
    print('sem prova, e ja aconteceu tres vezes em 09/09.')
