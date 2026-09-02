#!/usr/bin/env python3
"""Gera drafts/<slug>.md, linhas de alvos.csv, linhas do array STUDIOS e o JSON
com body/htmlBody para os rascunhos do Gmail a partir de um JSON de aprovados.

Uso: python3 automacao/gera-rascunhos.py aprovados.json [--lote N] [--out saida.json]

Cada item do JSON de entrada:
{
  "nome": "Studio X", "slug": "studio-x", "pais": "França", "cidade": "Paris",
  "trilha": "A", "email": "jobs@studiox.com", "fonte": "https://studiox.com/jobs",
  "encaixe": "forte", "obs": "nota para o alvos.csv (sem vírgulas)",
  "saudacao": "Studio X team", "gancho": "One or two specific sentences.",
  "eua": false, "remoto": false, "vaga": "Senior Character Artist" (opcional)
}
Regras fixas da campanha: frase de portfólio, frase de realocação fora dos EUA,
sem travessão, sem emoji, sem 'Brazil'. A frase de remoto entra quando remoto=true.
"""
import json, sys, os, re, html as htmlmod

ASSUNTO = "Senior Character Artist · Wingfeather Saga credit · stylized + grooming"
P1 = ("I'm Vini Cavalcanti, Senior 3D Character Artist (**The Wingfeather Saga**, **Endstar**), "
      "MA cand. in Creative Industries and Game Art Specialist (PG Dip), with **10+ years in stylized characters**.")
P2_A = ("On **The Wingfeather Saga** at Angel Studios I modeled and hand-painted characters for Season 1. "
        "For almost five years now I've been with **E-Line Media in Arizona, US**, taking Endstar's hero characters "
        "from first sculpt to engine. I also do character grooming in **Houdini**. My portfolio holds more than "
        "**45 projects** with **over 60 characters** across many titles, and my **personal projects** are some of the "
        "strongest pieces in it. ")
REMOTO = "I've worked fully remote with a US studio for almost five years, so a distributed team is my normal working mode. "
RELOC = ("I'm open to relocating as well; my academic background (honors laurea, postgraduate specialization, "
         "master's in progress, IELTS, publications) makes a strong visa case.")
FECHO = ("CV and cover letter attached.\n\nBest,\nVini Cavalcanti\n"
         "Portfolio: https://www.artstation.com/viniciuscavalcanti\n"
         "LinkedIn: https://www.linkedin.com/in/vinicavalcnti/\n"
         "Founder, Vini Cavalcanti School: https://vinicavalcanti.com")
FECHO_HTML = ('<p>CV and cover letter attached.</p><p>Best,<br>Vini Cavalcanti<br>'
              'Portfolio: <a href="https://www.artstation.com/viniciuscavalcanti">artstation.com/viniciuscavalcanti</a><br>'
              'LinkedIn: <a href="https://www.linkedin.com/in/vinicavalcnti/">linkedin.com/in/vinicavalcnti</a><br>'
              'Founder, Vini Cavalcanti School: <a href="https://vinicavalcanti.com">vinicavalcanti.com</a></p>')

PROIBIDO = ["—", "Brazil", "Brasil"]

def md_to_plain(t):
    return t.replace("**", "")

def md_to_html_par(t):
    t = htmlmod.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return "<p>" + t + "</p>"

def build(item):
    p1 = P1
    if item.get("vaga"):
        p1 += f" I'm writing about the **{item['vaga']}** position on your careers page."
    p2 = P2_A + item["gancho"].strip()
    if not p2.endswith((".", "!", "?")):
        p2 += "."
    p2 += " "
    if item.get("remoto"):
        p2 += REMOTO
    if not item.get("eua"):
        p2 += RELOC
    p2 = p2.strip()
    saud = f"Dear {item['saudacao']},"
    for bad in PROIBIDO:
        for txt in (item["gancho"], item["saudacao"]):
            if bad in txt:
                raise SystemExit(f"PROIBIDO '{bad}' em {item['nome']}")
    md = f"# {item['nome']}\n\n**Para:** {item['email']}\n**Assunto:** {ASSUNTO}\n\n{saud}\n\n{p1}\n\n{p2}\n\n{FECHO}\n"
    body = f"{saud}\n\n{md_to_plain(p1)}\n\n{md_to_plain(p2)}\n\n{FECHO}"
    html = f"<p>{htmlmod.escape(saud, quote=False)}</p>" + md_to_html_par(p1) + md_to_html_par(p2) + FECHO_HTML
    return md, body, html

def main():
    args = sys.argv[1:]
    src = args[0]
    lote = int(args[args.index("--lote") + 1]) if "--lote" in args else 15
    out = args[args.index("--out") + 1] if "--out" in args else "rascunhos-gmail.json"
    items = json.load(open(src))
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    gmail, alvos, studios = [], [], []
    for it in items:
        md, body, html = build(it)
        path = os.path.join(root, "drafts", it["slug"] + ".md")
        if os.path.exists(path):
            raise SystemExit(f"já existe: {path}")
        open(path, "w").write(md)
        obs = it["obs"].replace(",", ";")
        alvos.append(f'{it["nome"]},{it["pais"]},{it.get("trilha","A")},{it["email"]},{it["fonte"]},{it.get("encaixe","forte")},{obs}')
        studios.append(f' ["{it["nome"]}","{it["pais"]}","{it["email"]}",{lote},"rascunho"],')
        gmail.append({"nome": it["nome"], "to": it["email"], "subject": ASSUNTO, "body": body, "htmlBody": html})
    json.dump(gmail, open(out, "w"), ensure_ascii=False, indent=1)
    open(out.replace(".json", "-alvos.csv"), "w").write("\n".join(alvos) + "\n")
    open(out.replace(".json", "-studios.txt"), "w").write("\n".join(studios) + "\n")
    print(f"{len(items)} rascunhos .md gerados; gmail em {out}")

if __name__ == "__main__":
    main()
