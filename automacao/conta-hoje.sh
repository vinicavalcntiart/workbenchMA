#!/bin/sh
# Conta quantos ESTUDIOS receberam candidatura por FORMULARIO num dia.
#
# Existe porque o Vini pediu a contagem do dia e pediu para receber sempre. Contar a mao
# refazendo o filtro toda vez erra de um jeito silencioso: cada rodada escreve a nota com
# uma redacao diferente, e filtro improvisado deixa envio de fora sem avisar.
#
# Uso:  sh automacao/conta-hoje.sh            (hoje e ontem, que e o "hoje" do fuso dele)
#       sh automacao/conta-hoje.sh 06/09      (um dia especifico)
#       sh automacao/conta-hoje.sh 06/09 -v   (com a lista dos estudios)
#
# O "hoje" do Vini e UTC-3, entao o dia dele atravessa a virada de UTC: por isso o padrao
# olha DOIS dias e nao um. Ele devolve DOIS numeros de proposito, e a diferenca entre eles
# e informacao, nao ruido: o ESTRITO exige verbo de envio junto da data e e o piso; o LARGO
# aceita qualquer entrada de portal fechada com a data e e o teto. O numero verdadeiro esta
# entre os dois, e dizer so um dos dois seria fingir precisao que o dado nao tem.
DIR="$(cd "$(dirname "$0")/.." && pwd)"
DIAS="${1:-}"
VERBOSE="${2:-}"
python3 - "$DIR/docs/index.html" "$DIAS" "$VERBOSE" <<'PY'
import re, sys, unicodedata, datetime

def n(s):
    return unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode().lower()

caminho, dias_arg, verbose = sys.argv[1], sys.argv[2], sys.argv[3]
if dias_arg:
    dias = [dias_arg]
else:
    hoje = datetime.datetime.utcnow().date()
    ontem = hoje - datetime.timedelta(days=1)
    dias = [d.strftime('%d/%m') for d in (ontem, hoje)] + \
           [d.strftime('%Y-%m-%d') for d in (ontem, hoje)]

alvo = '|'.join(re.escape(d) for d in dias)
ENVIO = re.compile(
    r'(enviad\w*|candidatura confirmada|confirmada na tela|aplicad\w*|cadastro (feito|criado)|'
    r'application (submitted|received|sent)|thanks for applying)[^.]{0,90}?(' + alvo + r')'
    r'|(' + alvo + r')[^.]{0,90}?(enviad\w*|confirmad\w*|aplicad\w*)')
DATA = re.compile(alvo)

h = open(caminho, encoding='utf-8').read()
estrito, largo = {}, {}
for linha in h.split('\n'):
    l = linha.strip().rstrip(',')
    if not (l.startswith('[') and ',true,' in l):
        continue
    m = re.match(r'\["([^"]+)","([^"]*)","([^"]*)","([^"]*)","(.*)",true,"\w+"\]', l)
    if not m:
        continue
    nome, local, _url, tipo, nota = m.groups()
    if tipo != 'portal':
        continue
    chave = n(nome.split('(')[0].strip())
    if DATA.search(n(nota)):
        largo.setdefault(chave, (nome, local))
    if ENVIO.search(n(nota)):
        estrito.setdefault(chave, (nome, local))

print(f"Dias considerados: {', '.join(dias[:2])}")
print(f"ESTUDIOS com candidatura por formulario, contagem ESTRITA (piso): {len(estrito)}")
print(f"ESTUDIOS com entrada de portal fechada na data, contagem LARGA (teto): {len(largo)}")
if verbose == '-v':
    print()
    for nome, local in sorted(estrito.values()):
        print(f"  {nome[:46]:46} | {local[:34]}")
PY
