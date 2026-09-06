#!/usr/bin/env python3
"""Lê um HTML salvo do gamedevmap.com e cospe os estúdios em CSV, já marcando
quais deles a campanha nunca contatou.

Uso:
    python3 automacao/parse-gamedevmap.py <arquivo.html> [<arquivo2.html> ...]

CORRIGIDO EM 06/09: o gamedevmap NÃO bloqueia mais esta automação. O curl simples
com user-agent de navegador responde 200 e devolve a página inteira, então o fluxo
agora é direto, sem depender do Vini salvar HTML:

    curl -s -A "Mozilla/5.0 Chrome/128" \
      "https://www.gamedevmap.com/index.php?country=<Pais>" -o <Pais>.html

Vale também country=Remote, que lista estúdios remote-first. A observação antiga,
de que o site bloqueava o proxy, era do tempo em que a rede do ambiente era fechada.

A saída vai para a saída padrão em CSV (nome,tipo,cidade,estado,pais,site,status)
onde status é "NOVO" ou "ja contatado".
"""
import csv
import html
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tipos que não têm time de arte de personagem: não vale prospectar.
TIPOS_FORA = {"Investment", "Incubator/Accelerator", "Organization", "Health"}


def normaliza(nome):
    n = nome.lower()
    n = re.sub(r"\b(studios?|games?|entertainment|interactive|animation|inc|ltd|llc|the)\b", " ", n)
    return re.sub(r"[^a-z0-9]", "", n)


def ja_contatados():
    vistos = set()
    for caminho, coluna in (("alvos.csv", 0), ("enviados.csv", 1)):
        p = os.path.join(REPO, caminho)
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            for linha in csv.reader(f):
                if len(linha) > coluna and linha[coluna]:
                    vistos.add(normaliza(linha[coluna].split(" (")[0]))
    for caminho in ("portal_only.md", "docs/index.html"):
        p = os.path.join(REPO, caminho)
        if os.path.exists(p):
            texto = open(p, encoding="utf-8").read()
            vistos.add("__texto__")
            globals().setdefault("_TEXTOS", []).append(texto.lower())
    return vistos


def extrai(caminho):
    s = open(caminho, encoding="utf-8", errors="replace").read()
    linhas = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", s, re.S):
        celulas = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
        if len(celulas) < 6:
            continue
        campos = [html.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in celulas]
        nome, _, tipo, cidade, estado, pais = campos[:6]
        if not nome or nome == "Company" or "All Types" in tipo:
            continue
        site = re.search(r'href="(https?://[^"]+)"', tr)
        linhas.append([nome, tipo, cidade, estado, pais, site.group(1) if site else ""])
    return linhas


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    vistos = ja_contatados()
    textos = globals().get("_TEXTOS", [])
    saida = csv.writer(sys.stdout)
    saida.writerow(["nome", "tipo", "cidade", "estado", "pais", "site", "status"])
    novos = 0
    for caminho in sys.argv[1:]:
        for nome, tipo, cidade, estado, pais, site in extrai(caminho):
            if tipo in TIPOS_FORA:
                continue
            chave = normaliza(nome)
            conhecido = chave in vistos or any(nome.lower() in t for t in textos)
            status = "ja contatado" if conhecido else "NOVO"
            novos += status == "NOVO"
            saida.writerow([nome, tipo, cidade, estado, pais, site, status])
    print(f"# {novos} nomes novos", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
