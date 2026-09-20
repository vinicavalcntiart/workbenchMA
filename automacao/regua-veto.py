#!/usr/bin/env python3
# REGUA DE VETO CORRIGIDA - quarto turno de 16/09, depois de dois envios errados na Snowprint.
# O que mudou, e o motivo de cada mudanca:
#  1. LE NA URL FINAL, com redirect seguido (-L equivalente). O teamtailor.com devolve 200 e
#     REDIRECIONA para o dominio proprio da casa; quem le a primeira resposta le pagina
#     incompleta e conclui "zero veto" com a palavra relocation no texto.
#  2. TERMOS NOVOS, que faltavam e que foram exatamente os que deixaram a Snowprint passar:
#     located in, based in, relocation, no relocation, unable to support.
#  3. CONTA E IMPRIME o numero de caracteres do texto limpo, para a medicao ser conferivel.
import re, html, subprocess, sys

TERMOS = [
 # --- os cinco novos, que a Snowprint provou que faltavam ---
 'located in', 'based in', 'relocation', 'no relocation', 'unable to support',
 # --- residencia e autorizacao ---
 'must be located', 'must reside', 'must live', 'residing in', 'right to work',
 'work authorization', 'work authorisation', 'authorized to work', 'authorised to work',
 'no sponsorship', 'not sponsor', 'cannot sponsor', 'unable to sponsor', 'without sponsorship',
 'visa', 'work permit', 'eligible to work', 'legally entitled to work', 'citizen', 'eu national',
 # --- idioma ---
 'fluent in', 'native speaker', 'mother tongue', 'francais', 'français', 'german language',
 'deutsch', 'svenska', 'proficiency in',
 # --- presenca ---
 'on-site only', 'onsite only', 'in-office', 'no remote', 'not remote', 'hybrid',
 # --- nivel ---
 'internship', 'must be enrolled', 'student',
 # --- 19/09 20h15: OS TERMOS QUE A STIRLING PROVOU QUE FALTAVAM. A regua tinha 'based in' e
 # 'must be located', e nenhum dos dois casa com a frase que veta de verdade no anuncio 77 da
 # Stirling Animation Studios: "Artists must be based regionally within the UK (outside the
 # M25)". O acerto unico que ela devolveu foi 'hybrid', um falso positivo de beneficio, e a
 # leitura ingenua seria "zero veto" numa vaga de personagem com veto de residencia ESCRITO.
 # Mesma familia do erro da Snowprint: a regua so mede o que ela sabe procurar.
 'must be based', 'must be a resident', 'must be resident', 'based regionally',
 'regionally within', 'based within', 'residency', 'residents', 'resident of',
 'local candidates', 'locally based', 'permanent resident', 'pr status',
 'open to canadian', 'canadian based', 'uk based', 'us based', 'eu based',
 'only accepting applications from',
 # --- 20/09 00h50 (Jhon A, 37o turno): A TERCEIRA RECORRENCIA DA MESMA CEGUEIRA. A regua
 # ja tinha sido consertada pela Snowprint (16/09) e pela Stirling (19/09), e mesmo assim
 # devolveu UM UNICO acerto no anuncio 254 da Crafty Apes ("CG Artist (Assets) Mid/Senior -
 # London"), e esse acerto era 'proficiency in', vindo de "Expert proficiency in
 # industry-standard software" - frase de REQUISITO TECNICO, nao de veto. A frase que
 # restringe de verdade esta na segunda linha do anuncio e a regua nao a conhecia:
 #     "Contract - 100% Remote within the UK"
 # A familia do erro e sempre a mesma: a regua sabe procurar "based in <pais>" e nao sabe
 # procurar "<modalidade> within <pais>". Como a campanha caca muito cargo REMOTO, e
 # justamente em vaga remota que essa forma aparece, o buraco era do tamanho da veia.
 'within the uk', 'within the us', 'within the usa', 'within canada', 'within the eu',
 'within the uk only', 'remote within', 'remote in the uk', 'remote in the us',
 'remote in canada', 'anywhere in the uk', 'anywhere in the us', 'anywhere in canada',
 'work from the uk', 'work from canada', 'located within', 'reside within',
 'authorized to work in', 'authorised to work in', 'restricted to candidates',
]

def texto(url):
    r = subprocess.run(['curl','-sL','--max-time','60','-A',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',
        url,'-w','\n@@FINAL@@%{url_effective}'], capture_output=True, text=True)
    b = r.stdout
    m = re.search(r'@@FINAL@@(\S+)\s*$', b)
    final = m.group(1) if m else url
    b = b[:m.start()] if m else b
    t = re.sub(r'<script.*?</script>', ' ', b, flags=re.S)
    t = re.sub(r'<style.*?</style>', ' ', t, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    t = re.sub(r'\s+', ' ', t).strip()
    return final, t

for url in sys.argv[1:]:
    final, t = texto(url)
    print('=' * 100)
    print('PEDIDA :', url)
    print('FINAL  :', final)
    print('CARACTERES DO TEXTO LIMPO:', len(t))
    achou = False
    for termo in TERMOS:
        for m in re.finditer(re.escape(termo), t, re.I):
            achou = True
            ini = max(0, m.start() - 130)
            print(f'  [{termo}] ...{t[ini:m.start()+150]}...')
    if not achou:
        print('  ZERO ACERTO dos', len(TERMOS), 'termos')
