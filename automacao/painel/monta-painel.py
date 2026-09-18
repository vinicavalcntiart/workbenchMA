#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MONTA-PAINEL: recompoe docs/index.html a partir dos DADOS que ja estao nele e da
APRESENTACAO que vive nesta pasta (estilo.css, corpo.html, app.js).

Por que existe (19/09/2026, "nova era" da campanha, pedido do Vini de refazer o site do zero):
o painel tinha 6.000 linhas num arquivo so, dados e codigo misturados, e toda mudanca de visual
arriscava os arrays que as rotinas e os scripts em python leem (pulso.sh, poe-no-painel.py,
conta-hoje.sh, garra.sh, gera-pessoas.mjs, gera-preenchedor.mjs, valida-formato.mjs). Agora a
apresentacao e reescrita a vontade aqui, e o montador so transporta os dados, byte a byte.

CONTRATO QUE FICA (as ferramentas dependem dele):
  - docs/index.html continua sendo O arquivo: dados dentro dele, em `const NOME = [ ... ];`
    com UMA linha por registro, e STUDIOS/PORTAIS terminando em `].map(...)`.
  - marcadores // <PESSOAS> ... // </PADROES> e /*<PREENCHEDOR>*/ ... /*</PREENCHEDOR>*/ mantidos.
  - DAILY passa a ter CINCO campos: [data, emails, respostas humanas, formularios, formularios de personagem].
    Linha antiga com tres campos continua valendo (os dois ultimos contam como zero).
  - AGENDA: [dataISO ou data-hora ISO, titulo, texto, link opcional]. META: {formularios, personagem}.

Uso:
  python3 automacao/painel/monta-painel.py                 # recompoe o index.html com os dados atuais
  python3 automacao/painel/monta-painel.py --daily-de-enviados   # tambem recalcula formularios/dia do enviados.csv
"""
import csv, json, os, re, sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PAG = os.path.join(RAIZ, 'docs', 'index.html')
AQUI = os.path.dirname(os.path.abspath(__file__))

def ler(p):
    with open(p, encoding='utf-8') as f: return f.read()

h = ler(PAG)

def fatia(nome, abre='[', fecha=']'):
    """Devolve o texto do literal (array ou objeto) de `const nome = ...`, pulando aspas."""
    k = h.find('const ' + nome + ' ')
    if k < 0: k = h.find('const ' + nome + '=')
    if k < 0: return None
    i = h.index(abre, k); d, j = 0, i
    while j < len(h):
        c = h[j]
        if c == '"':
            j += 1
            while j < len(h) and h[j] != '"': j += 2 if h[j] == '\\' else 1
        elif c == abre: d += 1
        elif c == fecha:
            d -= 1
            if d == 0: break
        j += 1
    return h[i:j+1]

def linha(nome, padrao=None):
    m = re.search(r'^const ' + nome + r' = .*?;\s*$', h, re.M)
    if not m:
        if padrao is None: sys.exit('ERRO: nao achei const %s no painel' % nome)
        return padrao
    return m.group(0)

def entre(a, b):
    i, j = h.find(a), h.find(b)
    if i < 0 or j < 0: sys.exit('ERRO: marcadores %s ... %s nao encontrados' % (a, b))
    return h[i:j+len(b)]

# --- pedacos de dados, verbatim ---
SENT = linha('SENT'); UPDATED = linha('UPDATED'); BUILD = 'const BUILD = "__BUILD__";'
ALERTA = linha('ALERTA'); FOLLOWUP = linha('FOLLOWUP_PRONTO'); PORTA_CURTA = linha('PORTA_CURTA')
META = linha('META', 'const META = {formularios:10, personagem:5};')
DAILY = fatia('DAILY'); STUDIOS = fatia('STUDIOS'); PROSPECTOS = fatia('PROSPECTOS'); PORTAIS = fatia('PORTAIS')
GRANDES = fatia('GRANDES'); JOE_PASSOS = fatia('JOE_PASSOS'); NOVIDADES = fatia('NOVIDADES'); KIT = fatia('KIT'); DOSSIES = fatia('DOSSIES')
LOTE_DATA = fatia('LOTE_DATA', '{', '}')
AGENDA = fatia('AGENDA') or '[\n]'
PESSOAS_BLOCO = entre('// <PESSOAS>', '// </PADROES>')
PREENCHEDOR = entre('/*<PREENCHEDOR>*/', '/*</PREENCHEDOR>*/')
for n, v in [('DAILY',DAILY),('STUDIOS',STUDIOS),('PROSPECTOS',PROSPECTOS),('PORTAIS',PORTAIS),('GRANDES',GRANDES),('JOE_PASSOS',JOE_PASSOS),('NOVIDADES',NOVIDADES),('KIT',KIT),('DOSSIES',DOSSIES),('LOTE_DATA',LOTE_DATA)]:
    if not v: sys.exit('ERRO: nao achei o array %s' % n)

# --- DAILY com cinco campos, recalculado do enviados.csv quando pedido ---
def daily_rows():
    rows = json.loads(DAILY)
    if '--daily-de-enviados' in sys.argv:
        CHAR = re.compile(r'character|personagem|creature|criatura|vis dev|visual development|groom', re.I)
        AMB = re.compile(r'environment|ambiente|prop artist|vehicle|hard surface', re.I)
        EMAIL = re.compile(r'^[^@\s]+@[^@\s]+$')
        forms, chars = {}, {}
        with open(os.path.join(RAIZ, 'enviados.csv'), encoding='utf-8') as f:
            for r in list(csv.reader(f))[1:]:
                if not r or not re.match(r'\d{4}-\d{2}-\d{2}', r[0]): continue
                st = r[4] if len(r) > 4 else ''
                e_form = len(r) > 5 or not EMAIL.match(r[2].strip()) or 'portal' in st.lower() or 'formul' in st.lower()
                if not e_form: continue
                d = r[0][:10]; forms[d] = forms.get(d, 0) + 1
                txt = r[1] + ' ' + r[2] + ' ' + (r[3] if len(r) > 3 else '')
                if CHAR.search(txt) and not AMB.search(r[2]): chars[d] = chars.get(d, 0) + 1
        por_data = {r[0]: r for r in rows}
        for d in sorted(set(forms) | set(por_data)):
            r = por_data.get(d) or [d, 0, 0]
            r = list(r[:3]) + [forms.get(d, 0), chars.get(d, 0)]
            por_data[d] = r
        rows = [por_data[d] for d in sorted(por_data)]
    return rows
DAILY_TXT = '[\n' + ',\n'.join(' ' + json.dumps(r, ensure_ascii=False, separators=(',', ',')) for r in daily_rows()) + '\n]'
# json.dumps com separators sem espaco escreve ["2026-09-18",45,8,7,3], a forma que o painel sempre usou

if not fatia('AGENDA'):
    AGENDA = '[\n ["2026-09-21T16:00:00Z","Babaroga · Google Meet com Andy Bagdady (Studio Director) e Andreja Djokovic (CEO)","30 minutos, 13h de Brasília. Dois projetos novos de personagem. Briefing em automacao/briefing-babaroga.md; link do Meet no convite do Gmail."],\n ["2026-09-22","Animagency · Google Meet com Tero Suomela (CEO), dia a confirmar","Tero volta ao escritório na terça 22/09 e pediu um lembrete. O Comunicador manda o lembrete e grava o horário aqui quando ele responder."]\n]'

dados = '\n'.join([
 '// ===================== DADOS DA CAMPANHA =====================',
 '// Este bloco e a base de dados do painel e e lido por rotinas e scripts (pulso.sh, poe-no-painel.py,',
 '// conta-hoje.sh, garra.sh, gera-pessoas.mjs, gera-preenchedor.mjs, valida-formato.mjs).',
 '// Regras: uma linha por registro; sem virgula sobrando antes do ]; acrescente com',
 '// python3 automacao/poe-no-painel.py. A apresentacao vive em automacao/painel/ e e montada por monta-painel.py.',
 SENT, UPDATED, BUILD,
 '// Preenchido pela automacao quando algo quebra (ex.: sem acesso ao Gmail). Vazio = tudo ok.',
 ALERTA,
 '// Meta diaria (ordem do Vini de 16/09): formularios confirmados por dia e minimo de personagem.',
 META,
 '// Compromissos marcados: [dataISO ou data-hora ISO em UTC, titulo, texto, link opcional]. Passado some sozinho.',
 'const AGENDA = ' + AGENDA + ';',
 '// Follow-ups de 02/09: rascunhos prontos no Gmail dentro da thread original (automacao/followup-0209.csv)',
 FOLLOWUP,
 '// Uma linha por dia: [data, emails enviados, respostas humanas recebidas, formularios confirmados, formularios de personagem].',
 '// Os dois ultimos campos existem desde 19/09; linha antiga com tres campos vale zero neles.',
 'const DAILY = ' + DAILY_TXT + ';',
 '// Emails: [nome, pais, email, lote, entrega (ok|conf|reenvio|bounce|rascunho|fechado), etapa opcional]',
 'const STUDIOS = ' + STUDIOS + '.map(([name,country,email,batch,delivery,stage])=>({name,country,email,batch,delivery,stage}));',
 'const CONTACTED = STUDIOS.filter(s=>s.delivery!=="rascunho");',
 '// Prospeccao: [nome, "cidade, pais", site oficial, email verificado ou "", nota, "alta|media|baixa|fora"]',
 'const PROSPECTOS = ' + PROSPECTOS + ';',
 '// Formularios e portais: [nome, pais, url, origem (portal|email|vaga|linkedin), nota, feito(bool), prioridade (alta|media|baixa)]',
 '// done=true so quando a candidatura foi CONFIRMADA, com o texto literal da confirmacao na nota.',
 'const PORTAIS = ' + PORTAIS + '.map(([name,country,url,origem,note,done,prio])=>({name,country,url,origem,note,done,prio}));',
 '// Data de envio de cada lote de email, conferida contra enviados.csv. Lote sem data cai na mais recente.',
 'const LOTE_DATA = ' + LOTE_DATA + ';',
 '// Estudios grandes: [nome, sede, url oficial, via (ats|form|email), nota, feito(bool)]',
 'const GRANDES = ' + GRANDES + ';',
 '/* PESSOAS e PADROES sao gerados de automacao/pessoas.csv e automacao/padroes-dominio.md',
 '   por `node automacao/gera-pessoas.mjs`. Nao edite a mao entre os marcadores. */',
 PESSOAS_BLOCO,
 '// Passos da cacada do Joe: [titulo, texto, estado (rodando|proximo|regra)]',
 'const JOE_PASSOS = ' + JOE_PASSOS + ';',
 '// Novidades: [data ISO, tipo (viva|vaga|porta|nao|alerta|envio), titulo, texto, link opcional]. Mais recente primeiro.',
 'const NOVIDADES = ' + NOVIDADES + ';',
 '// Kit de aplicacao: [grupo, [[rotulo, texto], ...]]. {STUDIO} e trocado pelo estudio escolhido.',
 'const KIT = ' + KIT + ';',
 PORTA_CURTA,
 '// Dossies por vaga: [estudio, cargo e local, url, [[rotulo, texto], ...], falta enviar (bool)]',
 'const DOSSIES = ' + DOSSIES + ';',
 '// O codigo do preenchedor vive em automacao/preencher-formulario.js e e injetado aqui por',
 '// automacao/gera-preenchedor.mjs. Nao editar a linha abaixo a mao.',
 'const PREENCHEDOR_SRC = ' + PREENCHEDOR + ';',
])

pagina = '\n'.join([
 '<!doctype html>', '<html lang="pt-BR">', '<head>', '<meta charset="utf-8">',
 '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
 '<meta name="robots" content="noindex, nofollow">',
 '<title>Campanha Vini Cavalcanti</title>',
 '<!-- Montado por automacao/painel/monta-painel.py. Apresentacao em automacao/painel/; dados no primeiro bloco de script. -->',
 '<style>', ler(os.path.join(AQUI, 'estilo.css')).rstrip(), '</style>', '</head>', '<body>',
 ler(os.path.join(AQUI, 'corpo.html')).rstrip(),
 '<script>', dados, '</script>',
 '<script>', ler(os.path.join(AQUI, 'app.js')).rstrip(), '</script>',
 '</body>', '</html>', ''])

with open(PAG, 'w', encoding='utf-8') as f: f.write(pagina)
print('painel montado: %d bytes, DAILY %d dias, NOVIDADES %d, PORTAIS %d' % (len(pagina.encode('utf-8')), len(daily_rows()), NOVIDADES.count('\n'), PORTAIS.count('\n')))
