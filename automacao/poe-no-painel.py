#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""POE-NO-PAINEL — acrescenta UMA linha a um array de dados do docs/index.html sem errar vírgula.

POR QUE ISTO EXISTE, e a medição é do mesmo dia em que o arquivo nasceu. Em 15/09 os arrays
`PORTAIS` e `STUDIOS` terminavam com **vírgula sobrando** antes do `]`. JavaScript aceita, então
a página abria perfeita e o `valida-dashboard.sh` (que valida rodando o JS) dava OK; quem morria
era `json.loads`, e com ele TODO leitor em python do painel, incluindo as seções 2 e 4 do
`pulso.sh`, que é onde cada rodada escolhe o que fazer.

A vírgula foi removida e o `valida-dashboard.sh` ganhou uma porta que reprova array inválido.
**E a porta disparou DUAS VEZES no mesmo dia, nas duas vezes contra quem a escreveu**, ao
acrescentar linha à mão: uma vez por esquecer a vírgula de separação, outra por deixar vírgula
sobrando na última linha. Convenção que erra duas vezes em duas tentativas não é convenção, é
armadilha. Então o acréscimo vira ferramenta, e ninguém mais conta vírgula.

Ele lê o array, junta o registro, e reescreve **uma linha por registro**, que é a regra de
serialização da campanha (despejar o array numa linha só reprova na validação de formato).

Uso:
    python3 automacao/poe-no-painel.py PORTAIS '["Nome","Pais","url","origem","nota",false,"alta"]'
    python3 automacao/poe-no-painel.py PORTAIS registro.json
    python3 automacao/poe-no-painel.py --confere          # so verifica os quatro arrays

Sai com 1 se o registro não for uma lista JSON válida ou se o array não voltar a ser JSON válido
depois da escrita: melhor não escrever do que cegar os leitores de novo.
"""
import json
import os
import sys

ARQ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'index.html')
ARRAYS = ('PORTAIS', 'STUDIOS', 'PESSOAS', 'ENVIOS')
# quantos campos cada registro tem, para pegar no ato o erro que ja quebrou o painel antes:
# o STUDIOS e [nome, pais, email, lote, delivery, stage] com o stage no SEXTO campo, e escrever
# no quinto publica a etapa no lugar errado sem quebrar nada visivelmente.
TAMANHO = {'PORTAIS': 7, 'STUDIOS': 6}


def fatia(h, nome):
    """Devolve (inicio, fim) do array, andando pelo texto e pulando o conteudo das aspas."""
    k = h.find('const ' + nome)
    if k < 0:
        return None, None
    i = h.index('[', k)
    d, j = 0, i
    while j < len(h):
        c = h[j]
        if c == '"':
            j += 1
            while j < len(h) and h[j] != '"':
                j += 2 if h[j] == '\\' else 1
        elif c == '[':
            d += 1
        elif c == ']':
            d -= 1
            if d == 0:
                break
        j += 1
    return i, j


def confere(h):
    ruins = []
    for nome in ARRAYS:
        i, j = fatia(h, nome)
        if i is None:
            continue
        try:
            arr = json.loads(h[i:j + 1])
            print('  %-8s OK, %d linhas' % (nome, len(arr)))
        except Exception as e:
            ruins.append('%s: %s' % (nome, str(e)[:70]))
    for r in ruins:
        print('  QUEBRADO %s' % r)
    return not ruins


def main():
    h = open(ARQ, encoding='utf-8').read()
    if '--confere' in sys.argv:
        return 0 if confere(h) else 1
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    nome, bruto = sys.argv[1], sys.argv[2]
    if nome not in ARRAYS:
        print('array desconhecido: %s (conhecidos: %s)' % (nome, ', '.join(ARRAYS)))
        return 1
    if os.path.exists(bruto):
        bruto = open(bruto, encoding='utf-8').read()
    try:
        reg = json.loads(bruto)
    except Exception as e:
        print('o registro nao e JSON valido: %s' % str(e)[:90])
        return 1
    if not isinstance(reg, list):
        print('o registro tem de ser uma LISTA, veio %s' % type(reg).__name__)
        return 1
    esperado = TAMANHO.get(nome)
    if esperado and len(reg) != esperado:
        print('o %s tem %d campos por registro e este veio com %d. Nao escrevi nada.'
              % (nome, esperado, len(reg)))
        return 1

    i, j = fatia(h, nome)
    arr = json.loads(h[i:j + 1])
    arr.append(reg)
    corpo = ',\n'.join(json.dumps(r, ensure_ascii=False, separators=(',', ':')) for r in arr)
    novo = h[:i] + '[\n' + corpo + '\n]' + h[j + 1:]

    # nunca escreve sem reler: o ponto do arquivo e nao cegar leitor nenhum
    try:
        json.loads(novo[fatia(novo, nome)[0]:fatia(novo, nome)[1] + 1])
    except Exception as e:
        print('a escrita deixaria o %s invalido (%s). NAO escrevi.' % (nome, str(e)[:70]))
        return 1
    open(ARQ, 'w', encoding='utf-8').write(novo)
    print('%s: registro acrescentado, agora com %d linhas' % (nome, len(arr)))
    print('rode `sh automacao/valida-dashboard.sh` antes do commit.')
    return 0


if __name__ == '__main__':
    # `... | head -3` fecha o cano e o print seguinte levanta BrokenPipeError com traceback,
    # que numa rodada parece defeito do painel quando e so o head. Medido ao testar este
    # proprio arquivo em 15/09. Sai calado, como todo utilitario de linha de comando faz.
    try:
        sys.exit(main())
    except BrokenPipeError:
        try:
            sys.stdout.close()
        except Exception:
            pass
        sys.exit(0)
