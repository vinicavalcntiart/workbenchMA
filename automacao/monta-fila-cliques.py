#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MONTA-FILA-CLIQUES — gera a página pública "Fila de Cliques" a partir de dados, não à mão.

POR QUE A VERSAO 3, e ela responde a uma cobrança literal do Vini em 16/09:
*"nessa fila de cliques n tem as cartas de recomendacoes e bio (texto) especificas pra cada
estudio"*. Ele estava certo. A versao 2 entregava os 77 ENDERECOS agrupados pelo clique que ele
tem de dar, e em 43 deles a resposta campo a campo. Faltava o que mais custa tempo humano:
**O TEXTO que ele cola no campo de cover letter e no de "tell us about yourself"**. Sem isso,
cada porta ainda obrigava ele a escrever, e escrever 77 vezes e exatamente o gargalo que a
pagina existia para tirar.

**A PAGINA E PUBLICA.** Por isso ha um esfregao aqui, e ele nao e decorativo: telefone, endereco,
data de nascimento e qualquer valor pessoal sao BLOQUEADOS na geracao. O que sai e NOME DE CAMPO
e FORMATO, nunca o valor; o valor mora so no documento privado do Drive. Se o esfregao achar um
numero com cara de telefone ou um CEP, ele para a geracao em vez de publicar.

Entradas, as duas VERSIONADAS no repositorio para a pagina ser reproduzivel sem o /tmp:
    automacao/fila-cliques-portas.json     as 77 portas: metadado, agrupamento e dossie
    automacao/cartas-formulario-1609.json  carta, bio e bio_curta de cada porta

    python3 automacao/monta-fila-cliques.py [saida.html]
"""
import html
import json
import os
import re
import sys

BASE = '/tmp/claude-0'
SAIDA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, 'art', 'fila-cliques.html')

# ---------------------------------------------------------------- esfregao de privacidade
# Cada padrao aqui ja apareceu em algum dossie da campanha. Telefone e endereco NAO vao para
# pagina publica, e a regra do briefing e escrever o NOME DO CAMPO, nunca o valor.
PROIBIDO = [
    (re.compile(r'\+?55[\s.-]?\(?\d{2}\)?[\s.-]?\d{4,5}[\s.-]?\d{4}'), 'telefone brasileiro'),
    # CEP so conta com o hifen, ou colado na palavra. FALSO POSITIVO MEDIDO em 16/09: sem o
    # hifen, `\d{5}\d{3}` casa com IDENTIFICADOR DE VAGA do Lever (18024240, da Behaviour) e
    # trava a geracao inteira por um numero que nao e endereco de ninguem.
    (re.compile(r'\b\d{5}-\d{3}\b'), 'CEP'),
    (re.compile(r'(?i)\bcep\b[^\n]{0,12}\d{5}'), 'CEP nomeado'),
    (re.compile(r'(?i)\b(rua|avenida|av\.|travessa|apto|apartamento)\s+[A-Z]'), 'endereco'),
    (re.compile(r'(?i)data de nascimento\s*[:=]\s*\d'), 'data de nascimento com valor'),
    (re.compile(r'\b\d{2}/\d{2}/(19[6-9]\d)\b'), 'data que parece nascimento'),
]


def limpa(t):
    """Devolve (texto, achados). Achado nao e corrigido em silencio: ele para a geracao."""
    achados = [porque for rx, porque in PROIBIDO if rx.search(t or '')]
    return t or '', achados


def esc(t):
    return html.escape(t or '', quote=True)


def bloco_texto(rotulo, texto, idt, nota=''):
    if not texto:
        return ''
    return ('<div class="texto"><div class="texto-cab"><span class="texto-rot">%s</span>'
            '<button class="copiar" type="button" data-alvo="%s">copiar</button></div>'
            '%s<pre class="corpo-texto" id="%s">%s</pre></div>'
            % (esc(rotulo), esc(idt),
               ('<p class="texto-nota">%s</p>' % esc(nota)) if nota else '',
               esc(idt), esc(texto)))


def main():
    aqui = os.path.dirname(os.path.abspath(__file__))
    portas = json.load(open(os.path.join(aqui, 'fila-cliques-portas.json'), encoding='utf-8'))
    textos = {}
    for c in json.load(open(os.path.join(aqui, 'cartas-formulario-1609.json'),
                            encoding='utf-8')):
        textos[c['id']] = c
    print('cartas carregadas: %d' % len(textos))

    sujo = []
    for p in portas:
        p.setdefault('dossie', '')
        p.setdefault('nota', '')
        t = textos.get(p.get('id'))
        p['carta'] = (t or {}).get('carta', '')
        p['bio'] = (t or {}).get('bio', '')
        p['bio_curta'] = (t or {}).get('bio_curta', '')
        for campo in ('dossie', 'nota', 'carta', 'bio', 'bio_curta'):
            _, ach = limpa(p[campo])
            if ach:
                sujo.append('%s :: %s :: %s' % (p['casa'][:30], campo, ', '.join(ach)))
    if sujo:
        print('!! A PAGINA E PUBLICA e o esfregao achou dado pessoal. NAO gerei nada:')
        for s in sujo:
            print('   ', s)
        return 2

    com_carta = sum(1 for p in portas if p['carta'])
    com_dossie = sum(1 for p in portas if p['dossie'])
    print('%d portas | %d com carta pronta | %d com dossie campo a campo'
          % (len(portas), com_carta, com_dossie))

    # ------------------------------------------------------------ grupos na ordem da v2
    ordem, grupos = [], {}
    for p in portas:
        if p['grupo'] not in grupos:
            grupos[p['grupo']] = {'expl': p['grupo_expl'], 'itens': []}
            ordem.append(p['grupo'])
        grupos[p['grupo']]['itens'].append(p)

    partes = []
    for g in ordem:
        it = grupos[g]['itens']
        alta = sum(1 for p in it if p['alta'])
        partes.append(
            '<section class="grupo">\n<header class="grupo-cab"><div><h2>%s</h2>'
            '<p class="explica">%s</p></div><div class="grupo-num"><span class="n">%d</span>'
            '<span class="u">portas</span>%s</div></header>\n<ul class="portas">'
            % (esc(g), esc(grupos[g]['expl']), len(it),
               ('<span class="alta">%d de prioridade alta</span>' % alta) if alta else ''))
        for p in it:
            partes.append(linha(p))
        partes.append('</ul>\n</section>')

    modelo = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'fila-cliques-modelo.html'), encoding='utf-8').read()
    html_final = (modelo.replace('{{GRUPOS}}', '\n'.join(partes))
                  .replace('{{N}}', str(len(portas)))
                  .replace('{{COM_CARTA}}', str(com_carta))
                  .replace('{{ALTA}}', str(sum(1 for p in portas if p['alta']))))
    if '{{' in html_final:
        print('!! sobrou marcador no modelo: %s' % re.findall(r'\{\{\w+\}\}', html_final))
        return 2
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    open(SAIDA, 'w', encoding='utf-8').write(html_final)
    print('gravado em %s (%d KB)' % (SAIDA, len(html_final) // 1024))
    return 0


def linha(p):
    pid = p['pid']
    chips = ['<span class="chip d-%s">%s</span>' % (esc(p['disc'] or 'outro'),
                                                    esc(p['disc'] or 'outro'))]
    if p['alta']:
        chips.append('<span class="chip prio">alta</span>')
    if p['nc']:
        chips.append('<span class="chip nc" title="a pagina nao respondeu 200 na revalidacao '
                     'de 16/09">não conferida</span>')
    veto = 'NAO ENVIAR' in (p['vaga'] or '').upper() or 'NÃO ENVIAR' in (p['vaga'] or '').upper()
    if veto:
        chips.append('<span class="chip veto">não enviar</span>')

    corpo = []
    if veto:
        # A carta existe porque o lote era de 77, mas porta com veto escrito no anuncio NAO se
        # envia: o aviso fica ANTES do texto, para nao ser lido depois do Ctrl+V.
        corpo.append('<p class="privado"><b>Não envie esta.</b> O anúncio tem veto escrito de '
                     'residência e de autorização de trabalho. O texto fica aqui só para o caso '
                     'de o veto cair.</p>')
    corpo += [bloco_texto('Carta para o campo de cover letter', p['carta'], 'c-' + pid,
                         'Escrita para esta vaga. Nenhum emoji, porque campo de formulário não '
                         'leva. Cole inteira.'),
             bloco_texto('Bio para "tell us about yourself"', p['bio'], 'b-' + pid),
             bloco_texto('Resumo curto, para campo de uma linha', p['bio_curta'], 's-' + pid)]
    if p['dossie']:
        corpo.append('<div class="texto"><div class="texto-cab">'
                     '<span class="texto-rot">Campo a campo deste formulário</span></div>'
                     '<div class="dossie-txt">%s</div></div>' % marcacao(p['dossie']))
    elif p['nota']:
        corpo.append('<div class="texto"><div class="texto-cab">'
                     '<span class="texto-rot">O que a campanha mediu nesta porta</span></div>'
                     '<div class="dossie-txt">%s</div></div>' % marcacao(p['nota']))

    return (
        '<li class="porta" data-id="%(pid)s"><div class="linha">'
        '<input type="checkbox" class="feito" id="%(pid)s" aria-label="marcar %(casa)s como enviada">'
        '<label class="marca" for="%(pid)s"></label>'
        '<div class="corpo"><div class="topo"><span class="casa">%(casa)s</span>%(chips)s</div>'
        '<p class="vaga">%(vaga)s</p><p class="local">%(local)s</p></div>'
        '<a class="abrir" href="%(url)s" target="_blank" rel="noopener">abrir</a></div>'
        '<details class="textos"><summary>texto pronto para colar</summary>'
        '<div class="textos-corpo">%(corpo)s</div></details></li>'
        % {'pid': esc(pid), 'casa': esc(p['casa']), 'chips': ''.join(chips),
           'vaga': esc(p['vaga']), 'local': esc(p['local']), 'url': esc(p['url']),
           'corpo': ''.join(corpo)})


def marcacao(t):
    """Markdown pobre do dossie -> HTML seguro. Tudo escapado antes; so tabela e negrito voltam."""
    linhas = [l.rstrip() for l in (t or '').split('\n')]
    saida, tabela = [], []

    def fecha():
        if not tabela:
            return
        saida.append('<table class="tab">' + ''.join(
            '<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>' for r in tabela) + '</table>')
        tabela.clear()

    for l in linhas:
        if l.startswith('|') and l.count('|') >= 2:
            cels = [negrito(esc(c.strip())) for c in l.strip('|').split('|')]
            if all(re.fullmatch(r':?-{2,}:?', c.strip()) for c in cels if c.strip()):
                continue
            tabela.append(cels)
            continue
        fecha()
        if not l.strip():
            continue
        if l.startswith('#'):
            saida.append('<p class="dt-tit">%s</p>' % negrito(esc(l.lstrip('# ').strip())))
        elif l.strip().startswith(('-', '*')):
            saida.append('<p class="dt-item">%s</p>' % negrito(esc(l.strip()[1:].strip())))
        else:
            saida.append('<p>%s</p>' % negrito(esc(l.strip())))
    fecha()
    return ''.join(saida)


def negrito(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    # asterisco solto sobra quando o negrito do dossie atravessa a quebra de linha, e na tela
    # ele aparece cru (`obrigatoria**.`). Some com ele em vez de publicar a marcacao quebrada.
    return re.sub(r'\*+', '', t)


if __name__ == '__main__':
    sys.exit(main())
