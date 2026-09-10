# -*- coding: utf-8 -*-
# Gera a pagina FILA DO VINI na versao PERSONAGEM PRIMEIRO.
# O texto de cada campo vive aqui em Python puro; o HTML sai escapado pela stdlib,
# entao nao existe risco de aspas quebrarem o atributo data-t do botao de copiar.
import html, io, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(BASE, 'fila-formularios.html')
CSS = re.search(r'<link rel="stylesheet".*?</style>', open(ORIG, encoding='utf-8').read(), re.S).group(0)

EMAIL = 'contact@vinicavalcanti.art'
ART = 'https://www.artstation.com/viniciuscavalcanti'
SITE = 'https://vinicavalcanti.com'
LI = 'https://www.linkedin.com/in/vinicavalcnti/'
LOC = 'Olinda, Pernambuco, Brazil'
NDA = ('Confidential under the NDA of my current contract; happy to discuss ranges '
       'during the process.')

VAGAS = []


def vaga(**kw):
    VAGAS.append(kw)


# ---------------------------------------------------------------- 7 VALVE
vaga(
    id='valve', studio='Valve',
    role='3D Character Artist · Bellevue, Washington, EUA, presencial',
    chips=[('wall', 'reCAPTCHA de caixa'), ('plain', 'formulário próprio'), ('ok', 'dois minutos')],
    url='https://www.valvesoftware.com/en/jobs?job_id=2',
    ok='Formulário curtíssimo e a casa patrocina sem drama. O anúncio pede "High-level organic and '
       'hard-surface modeling", "Your ability to model characters in a variety of styles with an '
       'emphasis on character design" e "A thorough understanding of human anatomy".',
    note='O anúncio avisa: "Sorry, we do not accept student portfolios." O seu não é, então mande '
         'o ArtStation direto, que é o link com prioridade sobre o PDF.',
    campos=[
        ('Name / Email', 'Vini Cavalcanti\n' + EMAIL, None, True),
        ('Portfolio / links', ART + '\n' + SITE, None, True),
        ('Como descobriu a vaga', 'Valve careers page', None, True),
        ('CV', 'Vini_Cavalcanti_CV.pdf', None, True),
        ('Campo livre, se houver',
         "Valve asks character artists to contribute across the whole pipeline: sculpt high "
         "resolution in ZBrush, craft the low resolution game model, author PBR textures, and work "
         "with concept artists and animators so the character reads and performs. That full span "
         "is what I have been doing for ten years, and for almost five of them at E-Line Media "
         "specifically: Endstar's hero characters from first sculpt to engine, including high "
         "poly, retopology, UVs, baking, texturing, LODs and integration, plus hair and fur "
         "grooming in Houdini.\n\n"
         "On range of styles: The Wingfeather Saga season 1 at Angel Studios was hand painted and "
         "stylized, Endstar is a different stylization again, and my personal work goes realistic. "
         "Anatomy is the constant underneath all three. My portfolio holds more than 45 projects "
         "with over 60 characters, and the personal pieces are some of the strongest in it.\n\n"
         "I would need visa sponsorship to work in the United States, and I am fully open to "
         "relocating to Bellevue.\n\n"
         "Portfolio: " + ART, None, False),
    ])

# ---------------------------------------------------------------- 8 SKYDANCE GROOMING
vaga(
    id='grooming', studio='Skydance Animation',
    role='Senior Grooming TD · Madri, Espanha, híbrido',
    chips=[('wall', 'hCaptcha de imagem'), ('plain', 'Lever'), ('ok', 'Paramount')],
    url='https://jobs.lever.co/skydance/9ad28cab-87cd-4235-ae9b-b4c53a3457e5/apply',
    ok='Esta é a que mais aproveita o Houdini. O anúncio pede grooms para "human characters, furry '
       'creatures, feathered characters" e "Strong knowledge of Houdini". É Paramount: a política '
       'de privacidade do próprio anúncio aponta para privacy.paramount.com, o que aciona a regra '
       '14 da campanha.',
    note='Ressalva honesta: o cargo é TD, mais técnico do que o seu dia a dia, e a lista pede '
         '"5+ years in VFX or animation industries" mais "3+ years in the animation industry". '
         'Wingfeather cobre a segunda. CFX e simulação aparecem como "a plus", não como '
         'requisito, então não é a disciplina que você não tem.',
    campos=[
        ('Resume/CV', 'Vini_Cavalcanti_CV.pdf', None, True),
        ('Full name / Email', 'Vini Cavalcanti\n' + EMAIL, None, True),
        ('Current location', LOC, None, True),
        ('LinkedIn / Portfolio', LI + '\n' + ART, None, True),
        ('How did you hear about this position?', 'Skydance Website', None, True),
        ('Status de trabalho na Espanha', 'I am not an EU citizen and would need visa sponsorship to work in Spain.', None, True),
        ('Pretensão', 'Open to aligning with your band for the role; as a reference, around EUR 55,000 per year.', None, True),
        ('Campo livre / carta',
         "The posting asks for complex, artistically appealing hairstyles, grooms and surfacing for "
         "human characters, furry creatures and feathered characters, with strong knowledge of "
         "Houdini. Grooming hair and fur in Houdini is part of my normal asset pass, not a side "
         "skill I picked up for this application.\n\n"
         "On The Wingfeather Saga season 1 at Angel Studios I modeled and hand painted the "
         "season's characters, which is animation work on a stylized show where the groom has to "
         "serve the design rather than fight it. For almost five years at E-Line Media I have "
         "taken Endstar's hero characters from first sculpt to engine, and surfacing and look "
         "development sit inside that: PBR texturing, trim sheets and material work alongside the "
         "groom.\n\n"
         "I work inside established pipelines and I am comfortable contributing to departmental "
         "tools. I have been Senior for five years supporting other artists, and I founded and run "
         "my own character art school, so guidance and instruction are already part of the job "
         "for me.\n\n"
         "I want to relocate to Madrid and I am fully open to moving for the role. I am not an EU "
         "citizen and would need sponsorship.\n\n"
         "Portfolio: " + ART, None, False),
    ])

def campo(nome, valor, nota, curto):
    o = io.StringIO()
    o.write('      <div class="field">\n')
    o.write('        <div class="fhead"><span class="fname">%s</span>'
            '<button class="copy" data-t="%s">Copiar</button></div>\n'
            % (html.escape(nome), html.escape(valor, quote=True).replace('\n', '&#10;')))
    o.write('        <p class="val%s">%s</p>\n' % (' short' if curto else '', html.escape(valor)))
    if nota:
        o.write('        <p class="note">%s</p>\n' % html.escape(nota))
    o.write('      </div>\n')
    return o.getvalue()


def artigo(n, v):
    o = io.StringIO()
    o.write('  <article class="job" id="%s">\n' % v['id'])
    o.write('    <header>\n')
    o.write('      <h2 class="studio">%d. %s</h2>\n' % (n, html.escape(v['studio'])))
    o.write('      <p class="role">%s</p>\n' % html.escape(v['role']))
    o.write('      <div class="meta">\n')
    for cls, txt in v['chips']:
        o.write('        <span class="chip %s">%s</span>\n' % (cls, html.escape(txt)))
    o.write('      </div>\n')
    o.write('      <a class="open" href="%s" target="_blank" rel="noopener">Abrir o formulário</a>\n'
            % html.escape(v['url'], quote=True))
    o.write('    </header>\n    <div class="fields">\n')
    o.write('      <div class="field">\n        <p class="okbox">%s</p>\n' % html.escape(v['ok']))
    if v.get('note'):
        o.write('        <p class="note">%s</p>\n' % html.escape(v['note']))
    o.write('      </div>\n')
    for c in v['campos']:
        o.write(campo(*c))
    o.write('    </div>\n  </article>\n\n')
    return o.getvalue()


SCRIPT = re.search(r'<script>.*</script>', open(ORIG, encoding='utf-8').read(), re.S).group(0)

out = io.StringIO()
out.write('<title>Fila do Vini</title>\n')
out.write(CSS)
out.write('\n\n<div class="wrap">\n\n')
out.write('''  <header>
    <h1>Fila do Vini</h1>
    <p class="sub">Você limpou oito das dez em dezessete minutos, entre 03h53 e 04h10, e as oito são
    de personagem. <strong>Sobraram duas.</strong> As outras saíram daqui e estão carimbadas
    NÃO REAPLICAR no painel.</p>
  </header>

  <div class="howto">
    <p><strong>Como usar.</strong> Abra o link da vaga e, para cada campo, toque em <em>Copiar</em> e cole. Os textos longos já estão prontos e citam o anúncio daquele estúdio, não precisam de edição.</p>
    <p><strong>Telefone e endereço não estão aqui de propósito.</strong> Eles moram só no seu documento privado do Drive, <em>CAMPANHA - dados pessoais dos formulários</em>. Copie de lá quando o campo pedir.</p>
    <p><strong>A etiqueta de captcha diz por que a vaga está com você</strong> e não com a automação. Nenhuma dessas duas foi enviada: conferi uma a uma contra o registro de envios antes de montar a página.</p>
    <p><strong>As duas que sobraram são as mais baratas da lista.</strong> A Valve é um formulário curtíssimo e a Skydance é a que mais aproveita o seu Houdini. Juntas devem custar menos de dez minutos.</p>
  </div>

''')
out.write('  <nav class="jump" aria-label="Ir para uma vaga">\n')
for i, v in enumerate(VAGAS, 1):
    out.write('    <a href="#%s">%d · %s</a>\n' % (v['id'], i, html.escape(v['studio'])))
out.write('  </nav>\n\n')
for i, v in enumerate(VAGAS, 1):
    out.write(artigo(i, v))
out.write('''  <footer>
    <p><strong>As oito que você já mandou</strong>, com o recibo de cada uma lido e carimbado no
    painel: Behaviour (Senior 3D Character Artist, Dead by Daylight), Frontier (Experienced
    Character Artist), Lighthouse Games (Lead Character Artist), Ubisoft Massive (Lead Character
    Artist, The Division 2), Offworld Industries (3D Character Artist), People Can Fly, Avalanche
    Studios (Lead Character Artist) e TTK Games (Character Artist). A Fenris Creations foi enviada
    pela automação às 04h e o recibo chegou às 04h10. Nove candidaturas de personagem e nenhuma de
    ambiente.</p>
    <p><strong>Uma ressalva só, na People Can Fly:</strong> o recibo prova que uma candidatura
    entrou, mas não diz qual requisição recebeu, e a casa tem duas entradas vivas no painel. Antes
    de tocar nela de novo, abra o <em>Access My Application</em> do próprio recibo.</p>
    <p><strong>A Fenris Creations saiu daqui porque foi ENVIADA</strong>, às 04h de hoje, e é a
    primeira candidatura de personagem depois da regra que você escreveu. Três provas: o servidor
    respondeu 302, a página final terminou em <code>/thanks</code> e a tela escreveu
    <em>"Thanks. You have successfully registered your interest."</em> O que travava era um erro meu,
    não uma parede deles: a pergunta de visto é booleana e os botões dela valem <code>true</code> e
    <code>false</code>, não Yes e No, então a resposta obrigatória ia em branco. Corrigido.</p>
    <p><strong>Fora desta lista e sem esforço nenhum:</strong> a <strong>Flaming Fowl Studios</strong>
    (Lead 3D Artist, remoto de qualquer lugar do mundo) já está como rascunho pronto no seu Gmail.
    É só disparar, e a porta é email, então não tem captcha.</p>
    <p>Anúncios relidos na fonte oficial de cada ATS em 10/09 à noite. A única exceção é a
    Lighthouse, cujo texto o Workable recusou a devolver hoje por limite de requisições contra
    este IP; as frases dela vêm do registro de 07/09 e estão marcadas na própria vaga.</p>
  </footer>

</div>

''')
out.write(SCRIPT)
out.write('\n')

open(os.path.join(BASE, 'fila-formularios.html'), 'w', encoding='utf-8').write(out.getvalue())
print('ok', len(out.getvalue()), 'bytes,', len(VAGAS), 'vagas')
