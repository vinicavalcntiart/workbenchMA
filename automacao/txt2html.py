#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o `htmlBody` a partir da carta em texto. Existe por causa de dois defeitos de 14/09.

DEFEITO 1: mandei `reply` passando SO `body`. A API do Gmail converte sozinha para HTML e
linkifica cada URL pelo redirecionador dela, deixando `https://www.google.com/url?q=...` A VISTA
na tela do destinatario. O conserto e sempre passar TAMBEM `htmlBody` com ancora de verdade.

DEFEITO 2: escrevi o htmlBody escapado e a Ines Laborda, da Drakhar, recebeu `&lt;p&gt;` como
texto na tela. Por isso a regra aqui e literal: TAG VAI CRUA, ACENTO VAI POR ENTIDADE.

Uso:
    python3 automacao/txt2html.py carta.txt           # escreve carta.html ao lado
    python3 automacao/txt2html.py pasta/              # o lote inteiro

O arquivo .txt pode ter cabecalho (PARA:/ASSUNTO:/PESSOA:/ESTADO:) terminado por uma linha `---`;
o cabecalho NAO entra no HTML, so o corpo depois dele.
"""
import sys, os, re, glob

RX_URL = re.compile(r'https?://[^\s<>"\')]+')


def corta_cabecalho(t):
    """Devolve so o corpo. O cabecalho e para o humano, nao para o destinatario."""
    if '\n---\n' in t:
        return t.split('\n---\n', 1)[1].lstrip('\n')
    return t


def entidades(s):
    """& < > viram entidade SEMPRE (senao o texto quebra o HTML). Acento tambem, porque carta
    que sai sem charset declarado chega com acento trocado em cliente antigo."""
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    saida = []
    for c in s:
        # emoji e o seletor de variacao U+FE0F ficam CRUS: "☺️" e U+263A + U+FE0F, e virar
        # `&#65039;` separa o par que o cliente precisa ver junto para desenhar o emoji certo.
        if ord(c) > 127 and c not in '☺😊️‍':
            saida.append('&#%d;' % ord(c))
        else:
            saida.append(c)
    return ''.join(saida)


def linha_html(l):
    """Escapa a linha e SO DEPOIS troca cada URL por ancora, para a tag nascer crua."""
    marcas, resto = [], l
    for i, m in enumerate(RX_URL.finditer(l)):
        marcas.append(m.group(0))
    for i, u in enumerate(marcas):
        resto = resto.replace(u, '\x00%d\x00' % i, 1)
    resto = entidades(resto)
    for i, u in enumerate(marcas):
        curto = u.replace('https://', '').replace('http://', '').rstrip('/')
        resto = resto.replace('\x00%d\x00' % i,
                              '<a href="%s">%s</a>' % (u, entidades(curto)))
    return resto


def html(txt):
    corpo = corta_cabecalho(txt).rstrip()
    blocos = [b for b in re.split(r'\n\s*\n', corpo) if b.strip()]
    saida = []
    for b in blocos:
        linhas = [linha_html(l) for l in b.split('\n')]
        saida.append('<p>' + '<br>'.join(linhas) + '</p>')
    return '\n'.join(saida) + '\n'


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    alvo = sys.argv[1]
    arquivos = (sorted(glob.glob(os.path.join(alvo, '*.txt')))
                if os.path.isdir(alvo) else [alvo])
    for f in arquivos:
        h = html(open(f, encoding='utf8').read())
        destino = os.path.splitext(f)[0] + '.html'
        open(destino, 'w', encoding='utf8').write(h)
        n = len(RX_URL.findall(h.replace('href="', ' ')))
        print('%s  ->  %s  (%d ancora(s))' % (os.path.basename(f), os.path.basename(destino),
                                              h.count('<a href=')))
    return 0


if __name__ == '__main__':
    sys.exit(main())
