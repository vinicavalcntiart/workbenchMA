#!/usr/bin/env python3
# Le o menu do Teamtailor Connect (departamentos + cargos, com IDs) direto do HTML SERVIDO.
# Descoberta desta rodada: nao precisa de navegador. Departamentos E cargos vem no HTML,
# e cada cargo carrega data-for-department com o ID do departamento dono.
# Controles usados para validar: mindark (departamento Character Art 164025) e goals (cargo
# Character Art 873551). Ambos batem.
import re, sys, json, html

PALAVRAS = re.compile(r'character|creature|modeler|modeling|modelling|sculpt|groom|surfacing|'
                      r'look\s*dev|visual\s*dev|texture|texturing|shading|material', re.I)

DEP = re.compile(r'<span class="break-words overflow-hidden">([^<]*)</span>\s*'
                 r'<input[^>]*name="candidate\[department_id\]"[^>]*id="candidate_department_id_(\d+)"', re.S)
ROLE = re.compile(r'<span class="break-words overflow-hidden">([^<]*)</span>\s*'
                  r'<input[^>]*data-for-department="(\d*)"[^>]*name="candidate\[role_id\]"[^>]*id="candidate_role_id_(\d+)"', re.S)

def limpa(s):
    return html.unescape(s).replace(' ', ' ').strip()

def parse(path, slug):
    h = open(path, encoding='utf-8', errors='replace').read()
    deps = [{'id': i, 'rotulo': limpa(n)} for n, i in DEP.findall(h)]
    roles = [{'id': i, 'dep': d, 'rotulo': limpa(n)} for n, d, i in ROLE.findall(h)]
    bydep = {}
    for r in roles:
        bydep.setdefault(r['dep'], []).append(r)
    for d in deps:
        d['cargos'] = bydep.get(d['id'], [])
    orfaos = [r for r in roles if r['dep'] not in {d['id'] for d in deps}]
    hits = []
    for d in deps:
        if PALAVRAS.search(d['rotulo']) and d['id'] != '0':
            hits.append({'tipo': 'DEPARTAMENTO', 'id': d['id'], 'rotulo': d['rotulo']})
    for r in roles:
        if PALAVRAS.search(r['rotulo']) and r['id'] != '0':
            dn = next((d['rotulo'] for d in deps if d['id'] == r['dep']), '?')
            hits.append({'tipo': 'CARGO', 'id': r['id'], 'rotulo': r['rotulo'],
                         'dep_id': r['dep'], 'dep_rotulo': dn})
    return {'slug': slug, 'n_dep': len([d for d in deps if d['id'] != '0']),
            'n_cargo': len([r for r in roles if r['id'] != '0']),
            'departamentos': deps, 'orfaos': orfaos, 'personagem': hits,
            'tem_personagem': bool(hits)}

if __name__ == '__main__':
    out = []
    for a in sys.argv[1:]:
        slug = a.split('/')[-1].replace('.html', '')
        try:
            out.append(parse(a, slug))
        except Exception as e:
            out.append({'slug': slug, 'erro': str(e)})
    print(json.dumps(out, ensure_ascii=False, indent=1))
