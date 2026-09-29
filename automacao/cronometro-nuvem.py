#!/usr/bin/env python3
"""Cronometro do navegador na nuvem (Kernel). Pedido do Vini, 28/09: "sempre cronometre seu tempo
nesse navegador, pra saber o quanto gastou".

Le da API da Kernel o tempo de uso medido de cada sessao (usage.uptime_ms, o tempo que a propria
Kernel conta; sessao parada em espera nao conta) e grava automacao/NUVEM-TEMPO.md com o total por dia
e por sessao. Custo estimado a US$ 0,48 por hora (anotacao da passagem de 28/09).
A chave vem de KERNEL_API_KEY no ambiente, nunca do repositorio.

Uso: python3 automacao/cronometro-nuvem.py
"""
import os, json, urllib.request, collections
PRECO_HORA = 0.48
chave = os.environ['KERNEL_API_KEY']
itens, off = [], 0
while True:
    req = urllib.request.Request(f'https://api.onkernel.com/browsers?status=all&limit=20&offset={off}',
                                 headers={'Authorization': 'Bearer ' + chave})
    d = json.load(urllib.request.urlopen(req, timeout=60))
    lote = d if isinstance(d, list) else d.get('items', [])
    itens += lote
    if isinstance(d, list) or not d.get('has_more') or not lote: break
    off += len(lote)
linhas, dia = [], collections.defaultdict(float)
for s in sorted(itens, key=lambda x: x['created_at']):
    ms = ((s.get('usage') or {}).get('uptime_ms')) or 0
    aberta = not s.get('deleted_at')
    d0 = s['created_at'][:10]
    dia[d0] += ms
    linhas.append((s['created_at'][:16].replace('T', ' '), (s.get('deleted_at') or 'ABERTA')[:16].replace('T', ' '),
                   s.get('name') or '-', 'sim' if s.get('headless') else 'nao', ms / 60000, aberta))
tot = sum(dia.values())
out = ['# Cronometro do navegador na nuvem', '',
       'Gerado por `automacao/cronometro-nuvem.py` a partir do tempo medido pela propria Kernel (usage.uptime_ms).',
       f'Custo estimado a US$ {PRECO_HORA:.2f} por hora.', '',
       f'**Total medido:** {tot/60000:.1f} min, cerca de US$ {tot/3600000*PRECO_HORA:.2f}', '',
       '## Por dia', '', '| dia (UTC) | minutos | US$ estimado |', '|---|---|---|']
for d0 in sorted(dia):
    out.append(f'| {d0} | {dia[d0]/60000:.1f} | {dia[d0]/3600000*PRECO_HORA:.2f} |')
out += ['', '## Por sessao', '', '| aberta em (UTC) | fechada em (UTC) | nome | sem tela | minutos |', '|---|---|---|---|---|']
for a, f, n, h, m, ab in linhas:
    out.append(f'| {a} | {f} | {n} | {h} | {m:.1f}{" (AINDA ABERTA)" if ab else ""} |')
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'NUVEM-TEMPO.md'), 'w').write('\n'.join(out) + '\n')
print(f'total {tot/60000:.1f} min ~ US$ {tot/3600000*PRECO_HORA:.2f}; hoje {dia.get(max(dia) if dia else "",0)/60000:.1f} min; sessoes abertas: {sum(1 for x in linhas if x[5])}')
