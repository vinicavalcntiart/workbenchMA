#!/usr/bin/env python3
# PREENCHEDOR FLATCHR (careers.flatchr.io), nascido em 21/09 na candidatura da HARI.
# NAO PRECISA DE NAVEGADOR. Rota lida do JS do proprio quadro (chunk 3022, funcao de submit):
#   POST https://careers.flatchr.io/vacancy/<vacancySlug>
#   multipart: data=<json>, file=<CV>, motivationFile=<opcional>
#   200 = aceito (o JS navega para /apply/success); qualquer outro codigo = /apply/error.
# COMO DESCOBRIR OS CAMPOS DE UMA VAGA NOVA, tudo por curl:
#   careers.flatchr.io/fr/company/<slug>/  -> __NEXT_DATA__ -> props.data.spontaneousV.questions
#                                             (e props.data.items[].vacancy.questions para vaga normal)
#   api.flatchr.io/vacancy/<vacancySlug>?lng=fr&fields=company,questions,address
# ARMADILHA QUE CUSTA A RESPOSTA EM SILENCIO: a MESMA pergunta existe com ids DIFERENTES por vaga
#   (na HARI, 'Specialites' e 303545 na vaga de TI e 183880 na espontanea). Leia o id do objeto da
#   vaga que voce vai responder, nunca do irmao.
# CAMPO 'tag' e CAIXA DE MARCAR MULTIPLA: valor vai como string unida por ';'. E o JSON do servidor
#   traz 'multiple':true e 'creatable':true nas tags, ou seja ACEITA VALOR FORA DA LISTA - foi assim
#   que o campo obrigatorio 'Ecole' da HARI foi respondido com a verdade em vez de uma escola falsa.
# Sem --submit ele so imprime o payload (modo seco). O telefone nunca e impresso.
import json, sys, os
import requests

SLUG = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "vq5r6pyaexgpammv-candidature-spontanee"
URL = "https://careers.flatchr.io/vacancy/" + SLUG
PAGE = "https://careers.flatchr.io/fr/vacancy/%s/apply" % SLUG

p = json.load(open("/home/user/apply/pessoal.json"))

MOTIV = """Bonjour,

Je suis Senior 3D Character Artist avec plus de dix ans sur des personnages stylises, et je postule en candidature spontanee pour le departement personnage de HARI.

Votre page le dit mieux que moi : "Chaque personnage, chaque episode, chaque plan est un defi creatif". C'est exactement le travail que je cherche. Je prends un personnage de bout en bout : sculpt et high poly, retopologie, UVs, baking, texturing peint a la main et PBR, look development et integration moteur, et je fais aussi le groom des cheveux et de la fourrure dans Houdini, donc modeling, texture et groom sont un seul metier continu pour moi plutot que trois passations. Credite sur The Wingfeather Saga saison 1 chez Angel Studios, ou j'ai modele et peint les personnages a la main ; et depuis presque cinq ans chez E-Line Media (Arizona) je mene les personnages heros d'Endstar du premier sculpt jusqu'au moteur. Senior depuis cinq ans, je relis le travail des autres artistes et je fixe le standard des assets ; j'enseigne comme fondateur de ma propre ecole d'art du personnage et je suis en master.

Specialites cochees : Character Modeling, Texturing, Look Dev, Visual Development.

Sur l'ecole : je n'ai frequente aucune des ecoles francaises de la liste. Ma formation est bresilienne (licence avec mention, specialisation post-universitaire en Game Art, master en cours, IELTS, publications).

Je ne suis pas citoyen de l'Union europeenne et j'aurais besoin d'un parrainage de visa ; mon parcours academique fait un dossier de visa solide. Je suis pret a m'installer a Paris pour le poste. I am ready to move for the role.

Portfolio : https://www.artstation.com/viniciuscavalcanti

Vini Cavalcanti"""

ANSWERS = [
    {"question": 183879, "value": "Paris;Remote"},                                    # Localisation
    {"question": 183880, "value": "Visual Development;Character Modeling;Texturing;Look Dev"},  # Specialites
    {"question": 183881, "value": "Houdini;Maya;Photoshop;ZBrush"},                   # Logiciels
    {"question": 183882, "value": "Senior"},                                          # Niveau d'experience
    {"question": 183883, "value": "Aucune de ces ecoles (formation au Bresil)"},      # Ecole
    {"question": 183884, "value": "https://vinicavalcanti.com"},                      # autre lien
]

data = {
    "firstname": p["nome"],
    "lastname": p["sobrenome"],
    "email": p["email"],
    "phone": p["telefone_internacional"],
    "comment": MOTIV,
    "consent": True,
    "urls": [p["linkedin"], p["portfolio"]],
    "json": True,
    "answers": ANSWERS,
}

if "--no-ecole" in sys.argv:
    data["answers"] = [a for a in ANSWERS if a["question"] != 183883]

red = dict(data); red["phone"] = "<telefone: doc privado>"
print(json.dumps(red, ensure_ascii=False, indent=1))

if "--submit" not in sys.argv:
    print("\n== MODO SECO, nada enviado ==")
    sys.exit(0)

files = {
    "data": (None, json.dumps(data, ensure_ascii=False)),
    "file": ("Vini_Cavalcanti_CV.pdf", open(p["cv"], "rb"), "application/pdf"),
}
h = {
    "Origin": "https://careers.flatchr.io",
    "Referer": PAGE,
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36",
}
r = requests.post(URL, files=files, headers=h, timeout=180)
print("HTTP", r.status_code)
print("HEADERS", dict(r.headers))
print("BODY", r.text[:4000])
