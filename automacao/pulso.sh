#!/bin/sh
# PULSO — o estado inteiro da campanha em uma olhada, para nenhuma rodada morrer em análise.
#
# POR QUE ISTO EXISTE. O Vini cobrou, em 14/09, que eu passo horas sem trabalhar. A causa não
# é falta de trabalho: é que descobrir O QUE fazer agora custava dezenas de leituras de arquivo,
# e a rodada acabava consumida em diagnóstico. Este script paga esse custo uma vez, em segundos.
#
# REGRA DE USO, e ela é o antídoto: NENHUMA rodada pode terminar sem ação. Se o topo da lista
# estiver vazio, desça a ESCADA DE RECURSO que o script imprime no fim. Ela nunca está vazia.
#
#   sh automacao/pulso.sh
cd "$(dirname "$0")/.." || exit 1

echo "════════ PULSO DA CAMPANHA — $(date -u '+%Y-%m-%d %H:%M UTC')"

echo
echo "── 1. O QUE ESTÁ NA MÃO DELE (só captcha de desafio deve estar aqui)"
grep -nE "🖐️|ITEM DE MÃO" automacao/FILA-DO-VINI.md | sed 's/^/   /' || echo "   (nenhum)"

echo
echo "── 2. PORTAS PENDENTES NO PAINEL, por prioridade"
python3 - <<'PY'
import json,re
h=open('docs/index.html',encoding='utf8').read()
k=h.find('const PORTAIS'); i=h.index('[',k); d=0; j=i
while j<len(h):
    c=h[j]
    if c=='"':
        j+=1
        while j<len(h) and h[j]!='"': j+= 2 if h[j]=='\\' else 1
    elif c=='[': d+=1
    elif c==']':
        d-=1
        if d==0: break
    j+=1
arr=json.loads(h[i:j+1])
pend=[r for r in arr if len(r)>=7 and r[5] is False]
mural=re.compile(r'captcha|datadome|recaptcha|hcaptcha|parede|muro|à mão|a mao|expirad|morta|esgotad|teto de|veto escrito',re.I)
perso=re.compile(r'character|personagem|creature|criatura|modeler|modelagem|sculpt|groom',re.I)
print('   total %d  |  pendentes %d' % (len(arr), len(pend)))
for p in ('alta','media','baixa'):
    f=[r for r in pend if r[6]==p]
    livres=[r for r in f if not mural.search(r[4])]
    pc=[r for r in livres if perso.search(r[0]+' '+r[4])]
    print('   %-6s pendentes %3d | sem parede %3d | DESSAS de personagem %3d'
          % (p, len(f), len(livres), len(pc)))
    for r in pc[:4]:
        print('        -> %s | %s' % (r[0][:64], r[2][:70]))
PY

echo
echo "── 3. ÚLTIMA RODADA REGISTRADA DE CADA AGENTE (silêncio aqui é agente parado)"
for a in "Jhon A" "Jhon B" "Comunicador" "Prospec" "Joe" "detetive"; do
  l=$(grep -F "($a" automacao/processados.csv | tail -1 | cut -c1-10)
  printf "   %-14s %s\n" "$a" "${l:-NUNCA REGISTROU}"
done

echo
echo "── 4. REVALIDAÇÃO DEVIDA (as 3 vagas 'alta' mais antigas sem candidatura)"
python3 - <<'PY'
import json,re
h=open('docs/index.html',encoding='utf8').read()
k=h.find('const PORTAIS'); i=h.index('[',k); d=0; j=i
while j<len(h):
    c=h[j]
    if c=='"':
        j+=1
        while j<len(h) and h[j]!='"': j+= 2 if h[j]=='\\' else 1
    elif c=='[': d+=1
    elif c==']':
        d-=1
        if d==0: break
    j+=1
arr=json.loads(h[i:j+1])
alta=[r for r in arr if len(r)>=7 and r[5] is False and r[6]=='alta']
def data(r):
    m=re.findall(r'(\d{2})/(\d{2})', r[4])
    return min(('%s-%s'%(b,a) for a,b in m), default='99-99')
for r in sorted(alta,key=data)[:3]:
    print('   %s  | mais antiga citada: %s | %s' % (r[0][:56], data(r), r[2][:64]))
PY

echo
echo "── 5. ESCADA DE RECURSO — se nada acima estiver acionável, faça NESTA ORDEM."
echo "   Nenhum degrau depende de fila cheia, então a rodada nunca fecha em nada."
cat <<'TXT'
   1. sh automacao/ronda-disney.sh          grupo Disney, ordem permanente dele
   2. Pixar à parte: locatário próprio pixar.wd501, a ronda acima NÃO o cobre
   3. Revalidar as 3 do item 4 na fonte oficial; expirada vira baixa com a data
   4. Varrer um ATS que a campanha nunca testou (Ashby, Workable, Recruitee, Jobvite)
   5. Conferir a caixa: resposta humana sem resposta é a falha mais cara que existe
   6. Rodar confere-carta.py no lote de rascunhos e consertar o que ele acusar
   7. Reler uma parede antiga com navegador de verdade: a da NBCUniversal estava
      registrada errada e segurou a melhor vaga da campanha por seis dias
TXT
echo
echo "════════ fim do pulso"
