#!/usr/bin/env python3
"""Varredura de quadros de vaga, com as quatro licoes de 06 e 07/09 ja dentro.

POR QUE ESTE ARQUIVO EXISTE, no repositorio e nao no scratchpad: cada agente vinha
escrevendo a propria varredura do zero, e cada versao nova repetia os mesmos erros que a
anterior tinha acabado de pagar. Varredura e infraestrutura, nao rascunho. Quem for varrer
quadro usa esta, e quando aprender algo novo, conserta AQUI.

AS QUATRO LICOES, todas medidas e todas caras:

1. HTTP 403 NAO E SITE MORTO, e chamar de erro foi o engano mais caro da noite. Na fatia
   M-R da Europa, 142 dos 253 "erro" eram 403, ou seja, bloqueio de robo com o site vivo
   atras. Por isso 403, 401, 429 e a familia do Cloudflare saem daqui com estado
   'bloqueado', que quer dizer ABRA COM NAVEGADOR, e nunca 'erro'.

   MAS CUIDADO COM O EXAGERO OPOSTO, medido em 07/09 e que corrigiu um numero meu: de nove
   "bloqueados" abertos com navegador, so UM era bloqueio de IP de verdade. Quatro estavam
   mortos por certificado vencido, DNS caido ou dominio revendido, e cinco estavam vivos e
   sem parede nenhuma. A etiqueta 'bloqueado' da varredura grande estava INFLADA porque a
   versao anterior juntava erro de TLS com 403. Agora sao tres etiquetas distintas, porque o
   conserto de cada uma e diferente: 'bloqueado' abre com navegador, 'certificado' abre com
   curl -k, e 'dns-morto' geralmente esta morto mesmo. Contagem de bloqueio nunca deve ser
   citada como se fosse contagem de vaga escondida sem antes abrir uma amostra no navegador.

2. FILTRO EM INGLES SO ACHA VAGA EM INGLES. A "Artiste 3D" da Ankama passou batida em tres
   varreduras, e no recorte do Quebec duas vagas so apareceram por 'personnage' e
   'artiste 3d'. O vocabulario aqui e multilingue de proposito: frances, alemao, espanhol,
   italiano, portugues, sueco e polones.

3. VARREDURA QUE SO ESCREVE NO FIM EVAPORA. Uma rodada inteira se perdeu quando o processo
   estourou o tempo antes de imprimir a primeira linha. Aqui grava e da flush a cada achado.

6. CAPTCHA QUE RESPONDE 2xx. Medido em 09/09: o captcha do SiteGround devolve HTTP 202 com
   corpo de 179 bytes, cabecalho 'sg-captcha: challenge' e um meta refresh para
   /.well-known/sgcaptcha/. Codigo 2xx faz qualquer varredura marcar "porta aberta", e a
   etiqueta 'js' faria alguem gastar navegador nela a toa, porque captcha de desafio nao se
   burla nem com navegador. Sai com etiqueta propria, 'captcha-siteground'. Pegou tres casas
   de uma vez: Payload Studios, Stargate Studios Malta e Nice Shoes.

4. CALIBRAGEM: 20 segundos de tempo limite e 10 conexoes renderam 234 vagas; 6 segundos e
   mais de 20 conexoes renderam ZERO na mesma lista. Zero ali era pressa, nao ausencia.
   Os padroes abaixo sao esses, e apertar a concorrencia nao acelera, cega.

E a quinta, que nao e do codigo mas anda com ele: pagina que so monta em JavaScript volta
200 com corpo quase vazio. Isso sai como 'js', que quer dizer PRECISA DE NAVEGADOR, e nunca
como 'sem-arte'. Ja escondeu 21 vagas da Digic e 9 da Gaijin.

Uso:
    python3 automacao/varre-quadros.py entrada.tsv saida.csv
    entrada.tsv: linhas com estudio<TAB>cidade<TAB>regiao<TAB>url
"""
import csv
import re
import ssl
import sys
import urllib.error
import urllib.request
import concurrent.futures as cf

TEMPO_LIMITE = 20   # licao 4: nao baixe
CONEXOES = 10       # licao 4: nao aumente

# Licao 2: o vocabulario e multilingue, e cada termo aqui ja achou vaga que o ingles perdeu.
DISCIPLINA = re.compile(
    r'character\s*artist|3d\s*artist|modell?er|modeling artist|texture\s*artist|'
    r'look\s*dev|lookdev|surfacing|groom|sculpt|visual\s*development|cg\s*artist|'
    r'artiste\s*3d|personnage|modelisation|texturation|modeleur|developpement visuel|'
    r'charakter|3d-?k(ue|ü)nstler|modellierung|'
    r'artista\s*3d|personaje|modelado|texturizado|'
    r'modellatore|personaggio|'
    r'personagem|modelagem|'
    r'modellering|karakt(a|ä)r|'
    r'posta(c|ć)|modelowanie',
    re.I)

UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/128.0 Safari/537.36')
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def variantes(url):
    """https e http, com e sem www. Um dominio que recusa uma forma costuma aceitar outra."""
    m = re.match(r'^(https?)://(www\.)?(.+)$', url.strip())
    if not m:
        return [url.strip()]
    _, _, resto = m.groups()
    saida, vistos = [], set()
    for v in (f'https://{resto}', f'https://www.{resto}',
              f'http://{resto}', f'http://www.{resto}'):
        if v not in vistos:
            vistos.add(v)
            saida.append(v)
    return saida


def olha(linha):
    estudio, cidade, regiao, url = (linha + ['', '', '', ''])[:4]
    bloqueado = cert = dns = ultimo = ''
    for v in variantes(url):
        try:
            req = urllib.request.Request(
                v, headers={'User-Agent': UA, 'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8'})
            with urllib.request.urlopen(req, timeout=TEMPO_LIMITE, context=CTX) as r:
                corpo = r.read(400_000).decode('utf-8', 'ignore')
                codigo, final = r.status, r.geturl()
                cabecalhos = {k.lower(): v for k, v in r.headers.items()}
            # LICAO 6, medida em 09/09 na Payload, na Stargate Malta e na Nice Shoes:
            # captcha do SiteGround responde HTTP 202 com corpo de 179 bytes e um
            # <meta refresh> para /.well-known/sgcaptcha/, mais o cabecalho
            # 'sg-captcha: challenge'. Codigo 2xx faz qualquer varredura marcar
            # "porta aberta", e a etiqueta 'js' faria alguem gastar navegador nela.
            # Nao adianta navegador: captcha de desafio nao se burla. Etiqueta propria.
            if 'sg-captcha' in cabecalhos or 'sgcaptcha' in corpo:
                return (estudio, cidade, regiao, final, 'captcha-siteground',
                        f'{codigo}, sg-captcha, corpo de {len(corpo)} bytes', '')
        except urllib.error.HTTPError as e:
            # Licao 1: isto e porta fechada para robo, nao ausencia de vaga.
            if e.code in (401, 403, 406, 429, 503):
                bloqueado = f'HTTP {e.code} em {v}'
                continue
            ultimo = f'HTTP {e.code} em {v}'
            continue
        except Exception as e:
            texto = str(e)[:60]
            baixo = texto.lower()
            # CORRECAO DE 07/09, e ela nasceu de um numero meu que estava errado. A versao
            # anterior marcava erro de TLS como 'bloqueado', e isso INFLOU muito a contagem de
            # bloqueio: de nove "bloqueados" abertos com navegador, so UM era bloqueio de IP de
            # verdade; quatro estavam mortos por certificado expirado, DNS caido ou dominio
            # revendido, e cinco estavam vivos. Juntar as duas coisas faz a varredura mentir
            # nos dois sentidos: esconde site morto atras de "e so bloqueio" e esconde site vivo
            # atras de "nao respondeu". Agora certificado tem etiqueta propria, porque o conserto
            # dele e outro: certificado vencido abre com -k, bloqueio de IP so abre com navegador.
            if 'certificate' in baixo or 'ssl' in baixo or 'cert_' in baixo:
                cert = f'certificado: {texto}'
            elif 'name or service not known' in baixo or 'nodename' in baixo or 'getaddrinfo' in baixo:
                dns = f'DNS: {texto}'
            ultimo = texto
            continue

        limpo = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', corpo,
                       flags=re.S | re.I)
        limpo = re.sub(r'<[^>]+>', ' ', limpo)
        limpo = re.sub(r'\s+', ' ', limpo)
        if len(limpo) < 400:
            # Licao 5: isto e "precisa de navegador", nunca "sem vaga".
            return (estudio, cidade, regiao, final, 'js',
                    f'{codigo}, corpo de {len(limpo)} chars', '')
        achados = sorted({m.group(0).strip().lower()
                          for m in DISCIPLINA.finditer(limpo)})
        if achados:
            return (estudio, cidade, regiao, final, 'ARTE', str(codigo),
                    ', '.join(achados[:8]))
        return (estudio, cidade, regiao, final, 'sem-arte',
                f'{codigo}, {len(limpo)} chars', '')

    if bloqueado:
        return (estudio, cidade, regiao, url, 'bloqueado', bloqueado, '')
    if cert:
        return (estudio, cidade, regiao, url, 'certificado', cert, '')
    if dns:
        return (estudio, cidade, regiao, url, 'dns-morto', dns, '')
    return (estudio, cidade, regiao, url, 'erro', ultimo, '')


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    linhas = [l.rstrip('\n').split('\t')
              for l in open(sys.argv[1], encoding='utf-8') if l.strip()]
    saida = open(sys.argv[2], 'w', encoding='utf-8', newline='')
    w = csv.writer(saida)
    w.writerow(['estudio', 'cidade', 'regiao', 'url', 'estado', 'detalhe', 'disciplinas'])
    saida.flush()  # licao 3
    contagem = {}
    feitos = 0
    with cf.ThreadPoolExecutor(max_workers=CONEXOES) as ex:
        for res in ex.map(olha, linhas):
            feitos += 1
            w.writerow(res)
            saida.flush()  # licao 3: a cada achado, nunca no fim
            contagem[res[4]] = contagem.get(res[4], 0) + 1
            if res[4] in ('ARTE', 'bloqueado', 'js'):
                print(f'{res[4]:10} | {res[0][:32]:32} | {res[1][:14]:14} | {res[6][:52]}',
                      flush=True)
            if feitos % 50 == 0:
                print(f'--- {feitos} de {len(linhas)}', flush=True)
    print(f'\nFIM: {feitos} olhados. {contagem}', flush=True)
    print('ARTE = tem vaga da disciplina na pagina.', flush=True)
    print('bloqueado = 403, 429 ou 503 de verdade. Abra com navegador.', flush=True)
    print('certificado = certificado vencido ou invalido. Abre com curl -k: foi o caso dos', flush=True)
    print('   tres links do studiohog, dados como mortos por dias e vivos o tempo todo.', flush=True)
    print('dns-morto = o dominio nao resolve. Esse sim costuma estar morto de verdade.', flush=True)
    print('js = so monta em JavaScript. NAO e "sem vaga": abra com navegador.', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
