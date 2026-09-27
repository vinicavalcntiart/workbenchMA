#!/usr/bin/env python3
# TRIAGEM dos locatarios vivos do Pinpoint na rota /register-your-interest/new.
#
# DOIS DISCRIMINADORES, e o segundo nasceu de um FALSO NEGATIVO medido em 20/09:
# (1) ACME/Hooli no HTML (assinatura de conta de demonstracao, regra de 10/09);
# (2) O CONJUNTO DE DEPARTAMENTOS. O locatario "dynamo" NAO tem ACME nem Hooli no HTML e
#     mesmo assim e' quadro de demonstracao: os departamentos sao exatamente
#     {Engineering, Finance, Marketing, Operations, Product, Sales}, o conjunto padrao da
#     conta de teste. Testar so por ACME/Hooli deixa passar demo como casa real.
# As opcoes NAO estao em <option>: vivem no JSON embutido do componente React
# Shared::Form::Multiplechoiceselectfield. Procurar <option> devolve lista vazia e isso vira
# "casa sem departamento", que e' zero falso.
import json,re,sys,html,urllib.request,os
DEMO={'engineering','finance','marketing','operations','product','sales'}
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36'}
def opcoes(h,chave):
    for m in re.finditer(r'data-component-name="Shared::Form::Multiplechoiceselectfield"[^>]*>(\{.*?\})</script>',h,re.S):
        try: d=json.loads(html.unescape(m.group(1)))
        except Exception: continue
        if chave in (d.get('name') or ''):
            return [o.get('label') for o in (d.get('options') or [])]
    return []
def ficha(slug,h):
    t=re.search(r'<title[^>]*>(.*?)</title>',h,re.S)
    titulo=html.unescape(re.sub(r'<[^>]+>','',t.group(1))).strip() if t else ''
    dep=opcoes(h,'department_ids'); loc=opcoes(h,'location_ids')
    demo = ('ACME' in h and 'Hooli' in h) or (set(x.lower() for x in dep)==DEMO and dep)
    return {'slug':slug,'titulo':titulo,'departamentos':dep,'locais':loc,'demo':bool(demo)}
if __name__=='__main__':
    saida=[]
    for slug in [l.split(',')[0].strip() for l in open(sys.argv[1]) if l.strip()]:
        cache=os.path.join(os.path.dirname(sys.argv[1]),'pp_%s.html'%slug)
        try:
            h=open(cache,encoding='utf-8',errors='replace').read() if os.path.exists(cache) else None
            if h is None:
                r=urllib.request.Request('https://%s.pinpointhq.com/register-your-interest/new'%slug,headers=UA)
                h=urllib.request.urlopen(r,timeout=30).read().decode('utf-8','replace')
                open(cache,'w',encoding='utf-8').write(h)
        except Exception as e:
            print(json.dumps({'slug':slug,'erro':str(e)[:80]},ensure_ascii=False)); continue
        f=ficha(slug,h); saida.append(f)
        print(json.dumps(f,ensure_ascii=False))
    reais=[f for f in saida if not f['demo']]
    print('\n--- REAIS (nao-demo):',len(reais),'de',len(saida))
