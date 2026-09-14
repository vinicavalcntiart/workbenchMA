#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere uma carta ANTES de ela sair. Nasceu de dois defeitos reais de 14/09.

DEFEITO 1, o link. Mandei `reply` passando so `body` em texto puro. A API do Gmail converte
sozinha para HTML e linkifica cada URL pelo redirecionador dela, deixando
`https://www.google.com/url?q=...` A VISTA na assinatura do Carsten Granig, da Swift Games.
Conferido no MIME cru, nao na tela: saiu pelo fio assim. O `limparLinks` do
`automacao/envia-rascunhos.gs` desfaz isso, MAS so no caminho do Apps Script; resposta direta
pela API nao passa por ele.

DEFEITO 2, o robo. Respondi cinco boas-vindas do Teamtailor no mesmo minuto com o mesmo
paragrafo trocando so o nome. Se dois estudios se falarem, o truque aparece.

Uso:
    python3 automacao/confere-carta.py <arquivo.txt> [--html <arquivo.html>] [--tipo TIPO]
    python3 automacao/confere-carta.py <pasta>/          # confere o lote E compara entre si

TIPO muda so a regra de emoji: humana, fria, generica, recusa, ats. Padrao: fria.

Sai com codigo 1 se achar defeito que impede o envio, 0 se estiver limpo.
"""
import sys, os, re, glob, unicodedata

# ---------------------------------------------------------------- regras fixas
LIMITE_PALAVRAS = 250

# Emoji por tipo de carta, tabela do briefing. (minimo, maximo)
EMOJI = {
    'humana':   (1, 2),   # resposta calorosa a pessoa que escreveu
    'fria':     (1, 2),   # carta fria para pessoa com NOME
    'generica': (0, 1),   # caixa generica, 1 no fecho
    'recusa':   (0, 0),   # recusa e follow-up de silencio: emoji soa desdem
    'ats':      (0, 0),   # campo de formulario: ZERO
}

PROIBIDAS = [
    (r'\bBrazil\b',                     'a palavra "Brazil" e proibida na carta'),
    (r'I hope this (?:email )?finds you well', 'abertura de robo'),
    (r'I WANT TO RELOCATE',             'frase banida; use "I am ready to move for the role"'),
    (r'—',                              'travessao e proibido'),
    (r'–',                              'travessao curto tambem'),
]

# Floreio de IA. Cada uma destas ja apareceu em carta que precisou ser reescrita.
FLOREIO = [
    r"I'?m excited to", r'I am excited to', r'\bdelve\b', r'\btapestry\b',
    r'\bleverage\b', r'\bsynergy\b', r'\bpassionate about\b', r'\bcutting[- ]edge\b',
    r'\bstate[- ]of[- ]the[- ]art\b', r'\bworld[- ]class\b', r'\bdive deep\b',
    r"\bit'?s worth noting\b", r'\bthat said,', r'\bfurthermore,', r'\bmoreover,',
    r'\bin conclusion\b', r'\bI would love the opportunity to\b',
    r'\bperfect (?:fit|candidate)\b', r'\bwealth of experience\b',
]

# Sinais de que a carta NAO foi escrita para aquela casa.
SEM_GANCHO = re.compile(
    r'\b(your (?:studio|company|team)|the (?:studio|company))\b', re.I)

RX_URL = re.compile(r'https?://[^\s<>"\')]+')
RX_EMOJI = re.compile(
    '[\U0001F300-\U0001FAFF☀-➿←-⇿⬀-⯿️]')


def palavras(t):
    corpo = re.sub(r'^(Portfolio|LinkedIn|Founder|Best|Hi|Hola|Bonjour)[^\n]*$', '',
                   t, flags=re.M)
    return len(re.findall(r"[A-Za-zÀ-ÿ'’]+", corpo))


def normaliza(t):
    t = unicodedata.normalize('NFKD', t.lower())
    return re.findall(r'[a-z]+', t)


def shingles(t, n=6):
    p = normaliza(t)
    return {tuple(p[i:i + n]) for i in range(max(0, len(p) - n + 1))}


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def confere(txt, html=None, tipo='fria', nome=''):
    """Devolve (erros, avisos). Erro impede envio; aviso pede olhada."""
    erros, avisos = [], []

    # ---- 1. LINK. O defeito que custou a carta do Carsten.
    urls = RX_URL.findall(txt)
    if html is None:
        if urls:
            erros.append(
                'HTML AUSENTE com %d URL(s) no texto. Mandar so `body` faz o Gmail '
                'linkificar pelo redirecionador dele e o embrulho aparece na tela do '
                'destinatario. Passe TAMBEM `htmlBody`.' % len(urls))
    else:
        if re.search(r'&lt;\s*(div|p|a|br)\b', html, re.I):
            erros.append(
                'htmlBody ESCAPADO. `&lt;div&gt;` chega como tag crua na tela: foi o que a '
                'Ines Laborda, da Drakhar, recebeu. Tag vai CRUA; acento e que vai por '
                'entidade (&aacute;).')
        if urls and not re.search(r'<a\s[^>]*href=', html, re.I):
            erros.append('htmlBody sem nenhuma ancora <a href>, mas o texto tem URL.')
        for u in set(urls):
            if u not in html:
                avisos.append('URL no texto e ausente do HTML: %s' % u)
        for m in re.finditer(r'>([^<]*https?://[^<]*)<', html):
            erros.append('URL solta dentro do HTML, fora de ancora: %s'
                         % m.group(1).strip()[:70])
        if 'google.com/url' in html or 'google.com/url' in txt:
            erros.append('link ja embrulhado em google.com/url no que voce escreveu. '
                         'Escreva o endereco final.')

    # ---- 2. TAMANHO
    n = palavras(txt)
    if n > LIMITE_PALAVRAS:
        erros.append('%d palavras, teto e %d. Corte %d.'
                     % (n, LIMITE_PALAVRAS, n - LIMITE_PALAVRAS))
    elif n > LIMITE_PALAVRAS - 20:
        avisos.append('%d palavras, colado no teto de %d.' % (n, LIMITE_PALAVRAS))

    # ---- 3. PROIBIDAS
    for rx, porque in PROIBIDAS:
        m = re.search(rx, txt)
        if m:
            erros.append('%s :: "%s"' % (porque, m.group(0)))

    # ---- 4. FLOREIO DE IA
    achou = [m.group(0) for rx in FLOREIO for m in [re.search(rx, txt, re.I)] if m]
    if achou:
        avisos.append('floreio de IA: ' + ', '.join('"%s"' % a for a in achou[:6]))

    # ---- 5. EMOJI
    lo, hi = EMOJI.get(tipo, EMOJI['fria'])
    linhas = txt.strip().split('\n')
    assunto = next((l for l in linhas if l.lower().startswith('subject:')), '')
    if RX_EMOJI.search(assunto):
        erros.append('EMOJI NO ASSUNTO. O disparador do Apps Script acha o rascunho pelo '
                     'assunto literal: emoji ali some com a carta.')
    e = len(RX_EMOJI.findall(RX_EMOJI.sub('', assunto) and txt.replace(assunto, '') or txt))
    if e < lo:
        avisos.append('%d emoji para tipo "%s", esperado entre %d e %d.' % (e, tipo, lo, hi))
    if e > hi:
        erros.append('%d emoji para tipo "%s", maximo %d.' % (e, tipo, hi))

    # ---- 6. CAPSLOCK
    for m in re.finditer(r'\b[A-Z]{4,}(?:\s+[A-Z]{2,}){2,}\b', txt):
        erros.append('frase em capslock: "%s"' % m.group(0)[:50])

    # ---- 7. ABERTURA SECA
    if re.match(r'^\s*(Hi|Hello|Dear)\s*,', txt):
        erros.append('abertura sem nome. Nome da pessoa na abertura, sempre que houver nome.')

    # ---- 8. GANCHO
    if not SEM_GANCHO.search(txt):
        pass
    elif len(set(re.findall(r'\b[A-Z][a-z]{3,}\b', txt))) < 8:
        avisos.append('a carta fala em "your studio" e cita poucos nomes proprios: '
                      'pode nao ter gancho real na casa.')

    return erros, avisos


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    tipo = 'fria'
    if any(a.startswith('--tipo') for a in args):
        for i, a in enumerate(args):
            if a.startswith('--tipo'):
                tipo = a.split('=', 1)[1] if '=' in a else args[i + 1]
    html_arg = None
    if '--html' in args:
        html_arg = args[args.index('--html') + 1]

    alvo = args[0]
    if os.path.isdir(alvo):
        arquivos = sorted(glob.glob(os.path.join(alvo, '*.txt')))
    else:
        arquivos = [alvo]
    if not arquivos:
        print('nada para conferir em', alvo)
        return 2

    total_erros = 0
    textos = {}
    for f in arquivos:
        txt = open(f, encoding='utf8').read()
        textos[f] = txt
        html = None
        if html_arg:
            html = open(html_arg, encoding='utf8').read()
        else:
            par = os.path.splitext(f)[0] + '.html'
            if os.path.exists(par):
                html = open(par, encoding='utf8').read()
        erros, avisos = confere(txt, html, tipo, os.path.basename(f))
        print('\n=== %s  (%d palavras, html: %s)'
              % (os.path.basename(f), palavras(txt), 'sim' if html else 'NAO'))
        for e in erros:
            print('  ERRO   ', e)
        for a in avisos:
            print('  aviso  ', a)
        if not erros and not avisos:
            print('  limpo')
        total_erros += len(erros)

    # ---- 9. ROBO: duas cartas do mesmo lote parecidas demais
    if len(textos) > 1:
        print('\n=== SEMELHANCA ENTRE AS CARTAS DO LOTE')
        nomes = sorted(textos)
        sh = {n: shingles(textos[n]) for n in nomes}
        pior = 0.0
        for i in range(len(nomes)):
            for j in range(i + 1, len(nomes)):
                s = jaccard(sh[nomes[i]], sh[nomes[j]])
                pior = max(pior, s)
                if s >= 0.60:
                    print('  ERRO    %.0f%% iguais: %s vs %s  -> e o mesmo texto com o nome '
                          'trocado. Reescreva com gancho de cada casa.'
                          % (s * 100, os.path.basename(nomes[i]), os.path.basename(nomes[j])))
                    total_erros += 1
                elif s >= 0.45:
                    print('  aviso   %.0f%% iguais: %s vs %s'
                          % (s * 100, os.path.basename(nomes[i]), os.path.basename(nomes[j])))
        print('  pior par do lote: %.0f%%' % (pior * 100))

    print('\n%s' % ('FALHOU: %d erro(s). NAO ENVIE ASSIM.' % total_erros if total_erros
                    else 'OK: o lote pode sair.'))
    return 1 if total_erros else 0


if __name__ == '__main__':
    sys.exit(main())
