#!/usr/bin/env python3
"""Gera o htmlBody de uma carta a partir do .txt, com o NEGRITO FIXO do BRIEF-JOE.

Uso: python3 automacao/monta-html-carta.py carta.txt   -> grava carta.html ao lado
Depois: python3 automacao/confere-carta.py carta.txt  (ele acha o .html do par sozinho)
e o create_draft recebe body = .txt e htmlBody = .html.

Criado em 24/09/2026, depois de o Vini notar que as cartas iam sem negrito.
"""
import html, os, re, sys

NEGRITO = [
    r'Senior 3D Character Artist with more than (?:ten|10) years',
    r'The Wingfeather Saga season 1',
    r'E-Line Media',
    r'more than 45 projects with over 60 characters',
    r'I am ready to move for the role',
    r'grooming in Houdini',
]

def monta(txt):
    partes = []
    for par in txt.strip().split('\n\n'):
        linhas = []
        for l in par.split('\n'):
            e = html.escape(l, quote=False)
            for rx in NEGRITO:
                e = re.sub('(%s)' % rx, r'<b>\1</b>', e, count=1)
            e = re.sub(r'(https?://[^\s<]+)', lambda m: '<a href="%s">%s</a>' % (
                m.group(1), re.sub(r'^https?://(www\.)?', '', m.group(1)).rstrip('/')), e)
            linhas.append(e)
        partes.append('<p>' + '<br>'.join(linhas) + '</p>')
    return '<div>' + ''.join(partes) + '</div>'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    for f in sys.argv[1:]:
        h = monta(open(f, encoding='utf8').read())
        out = os.path.splitext(f)[0] + '.html'
        open(out, 'w', encoding='utf8').write(h)
        print('%s -> %s (%d negritos)' % (os.path.basename(f), os.path.basename(out), h.count('<b>')))
