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


# ---------------------------------------------------------------- 1 BEHAVIOUR
vaga(
    id='behaviour', studio='Behaviour Interactive',
    role='Senior 3D Character Artist, Dead by Daylight · Montréal, híbrido',
    chips=[('wall', 'hCaptcha de imagem'), ('plain', 'Lever'), ('plain', 'personagem')],
    url='https://jobs.lever.co/bhvr/18024240-e637-409f-a647-b422541e2dc7/apply',
    ok='O anúncio pede exatamente o que você faz: "hero character assets from concept '
       'interpretation through final implementation", "clothing, hair, textures, materials", '
       '"LOD creation, and asset integration into Unreal Engine" e "6+ years as a 3D Character '
       'Artist". Cada uma dessas frases está no seu currículo.',
    note='O anúncio está em inglês e francês na mesma página. O formulário aceita inglês. '
         'Esta é a terceira requisição de personagem da Behaviour: a de 7 Days to Die já foi '
         'enviada em 30/08, não repita aquela.',
    campos=[
        ('Resume/CV e Cover letter', 'Vini_Cavalcanti_CV.pdf + Vini_Cavalcanti_Cover_Letter.pdf', None, True),
        ('Full name / Email', 'Vini Cavalcanti\n' + EMAIL, None, True),
        ('Current location', LOC, None, True),
        ('Current company', 'E-Line Media', None, True),
        ('LinkedIn / Portfolio / Other website', LI + '\n' + ART + '\n' + SITE, None, True),
        ('Are you legally eligible to work in Canada?', 'No', 'Não responda Yes. Mentir na triagem derruba a candidatura depois.', True),
        ('Aceita o híbrido de 3 dias no escritório?', 'Yes', None, True),
        ('Pretensão salarial', 'Open to aligning with your band for the role; as a reference, around CAD 95,000 per year.', None, True),
        ('Salário atual', NDA, None, True),
        ('Pesquisa demográfica', 'Prefer not to say', None, True),
        ('Why are you interested in this role?',
         "Dead by Daylight ships characters continuously, killers and licensed survivors, and the "
         "posting asks for ownership of complex and hero character assets from concept "
         "interpretation through final implementation. That is the loop I have been running for "
         "years.\n\n"
         "For almost five years at E-Line Media I have taken Endstar's hero characters from first "
         "sculpt to engine: high poly, retopology, UVs, baking, PBR texturing, LODs and integration "
         "in Unreal. Clothing, hair and materials are part of that same pass, and I groom hair and "
         "fur in Houdini. On The Wingfeather Saga season 1 at Angel Studios I modeled and hand "
         "painted the season's characters, which is where I learned to hold a look across a whole "
         "cast rather than one hero.\n\n"
         "I have been Senior for five years. I review other artists' work and set the asset "
         "standard, and I founded and run my own character art school, so mentoring less "
         "experienced artists is something I already do every week rather than something I would "
         "be starting.\n\n"
         "I already applied to your 7 Days to Die opening because Behaviour is a studio I want to "
         "work at. I want to relocate to Montréal and I am fully open to moving for the role. I am "
         "not a Canadian citizen and would need visa sponsorship; my academic background, with an "
         "honors laurea, a postgraduate specialization in Game Art, a master's in progress, IELTS "
         "and publications, makes a strong case.\n\n"
         "Portfolio: " + ART, None, False),
    ])

# ---------------------------------------------------------------- 2 FRONTIER
vaga(
    id='frontier', studio='Frontier Developments',
    role='Experienced Character Artist · Cambridge, Reino Unido, híbrido',
    chips=[('wall', 'hCaptcha de imagem'), ('plain', 'Lever EU'), ('ok', 'paga realocação')],
    url='https://jobs.eu.lever.co/frontier/3571ace3-9f1a-4db2-9e2b-5eb8c8487181/apply',
    ok='O anúncio escreve, com todas as letras: "We can provide a comprehensive relocation '
       'support package as part of any offer, should you need to relocate." E na lista de bônus: '
       '"Passion for creatures and anatomy."',
    note='O formulário já pergunta sobre patrocínio de visto, ou seja, eles contratam quem '
         'precisa. A pretensão antiga de USD 46.000 está morta, use o número abaixo.',
    campos=[
        ('Resume/CV', 'Vini_Cavalcanti_CV.pdf', None, True),
        ('Nome / Email', 'Vini Cavalcanti\n' + EMAIL, None, True),
        ('LinkedIn / Portfolio / Other', LI + '\n' + ART + '\n' + SITE, None, True),
        ('Tem experiência com escultura orgânica?', 'Yes', None, True),
        ('País de residência', 'Brazil', None, True),
        ('Híbrido ou presencial?', 'Hybrid, relocating to Cambridge.', None, True),
        ('Precisa de patrocínio de visto?', 'Yes', None, True),
        ('Entende que a vaga exige realocação para Cambridge?', 'Yes', None, True),
        ('Salário atual', NDA, 'Não deixe em branco nem escreva valor. A frase do NDA é a resposta.', True),
        ('Pretensão salarial', "Open to aligning with Frontier's band for the role; as a reference, around GBP 50,000 per year.", None, True),
        ('Aviso prévio', 'A standard transition period with my current studio; glad to align dates in the process.', None, True),
        ('Detalhe sobre elegibilidade no Reino Unido',
         "I answered yes: I would need Skilled Worker sponsorship. My academic background, with an "
         "honors laurea, a postgraduate specialization in Game Art, a master's in progress, IELTS "
         "and publications, supports the visa case, and I can start remotely while it is "
         "processed, which is how I already work today for a studio in another country.", None, True),
        ('Campo livre / carta',
         "The posting asks for polished, optimised character and creature assets from concept to "
         "implementation, and for someone who mentors, writes briefs and gives outsourcing "
         "feedback without needing a lead title to do it. Both halves of that describe my week.\n\n"
         "I have more than ten years in 3D characters. For almost five of them, at E-Line Media, I "
         "have taken Endstar's hero characters end to end: sculpting in ZBrush, modelling, "
         "topology, UVs, baking, texturing in Substance Painter, LODs and checking assets into the "
         "engine. On The Wingfeather Saga season 1 at Angel Studios I modeled and hand painted the "
         "season's characters. Creatures and anatomy are the part I enjoy most, and they are the "
         "spine of my portfolio.\n\n"
         "On the mentoring side, I have been Senior for five years reviewing other artists' work "
         "and setting the asset standard, and I founded and run my own character art school, so "
         "giving clear, actionable feedback is a habit rather than an extra duty. I have also "
         "delivered under another studio's art direction at PUGA Studios, which is the same "
         "muscle as writing briefs for an outsourcing vendor and holding the quality bar on what "
         "comes back.\n\n"
         "I want to relocate to Cambridge and I am fully open to moving for the role. I would need "
         "Skilled Worker sponsorship.\n\n"
         "Portfolio: " + ART, None, False),
    ])

# ---------------------------------------------------------------- 3 LIGHTHOUSE
vaga(
    id='lighthouse', studio='Lighthouse Games',
    role='Lead Character Artist · Royal Leamington Spa, Reino Unido',
    chips=[('wall', 'Turnstile depois do Submit'), ('plain', 'Workable'), ('ok', 'só nome e email obrigatórios')],
    url='https://apply.workable.com/lighthousegames/j/F7F90250DA/apply/',
    ok='É a candidatura mais barata desta lista inteira. O /form oficial do Workable mostra que os '
       'ÚNICOS campos obrigatórios são First name, Last name e Email. Todo o resto, currículo '
       'inclusive, é opcional. Se você tiver dois minutos, é esta.',
    note='O anúncio inteiro foi buscado termo a termo em 07/09: zero "authoriz", "eligib", '
         '"sponsor", "work permit". Não há veto de residência escrito. Hoje o Workable recusou '
         'minha releitura do texto (limite de requisições contra este IP), então as frases do '
         'anúncio abaixo vêm do que ficou registrado em 07/09, não de uma leitura de hoje.',
    campos=[
        ('First name / Last name / Email', 'Vini\nCavalcanti\n' + EMAIL, None, True),
        ('Address / City / Country', LOC, 'Apague antes o "Columbus, United States of America" que o autofill do Workable escreve sozinho.', True),
        ('Headline', 'Senior 3D Character Artist, 10+ years in stylized characters, hair and fur grooming in Houdini', None, True),
        ('Resume / Cover letter', 'Vini_Cavalcanti_CV.pdf + Vini_Cavalcanti_Cover_Letter.pdf', None, True),
        ('Portfolio / showreel', ART, None, True),
        ('Do you have the right to work in the UK?', 'No, I would need Skilled Worker sponsorship.', None, True),
        ('Willing to relocate to Leamington Spa?', 'Yes', None, True),
        ('Salary expectation', 'Open to aligning with your band for the role; as a reference, around GBP 50,000 per year.', None, True),
        ('Summary (opcional)',
         "Lighthouse was built by the people who made Forza Horizon, which means the studio is "
         "assembling a character team from scratch rather than inheriting one, and a Lead there "
         "sets the standard that everything after it is measured against. That is the part of the "
         "job I want.\n\n"
         "I have more than ten years in 3D characters and I have been Senior for five, reviewing "
         "other artists' work and defining what counts as finished. At E-Line Media I have spent "
         "almost five years taking Endstar's hero characters from first sculpt to engine: high "
         "poly, retopology, UVs, baking, PBR texturing, LODs and integration. I groom hair and fur "
         "in Houdini. On The Wingfeather Saga season 1 at Angel Studios I modeled and hand painted "
         "the season's characters, holding one look across an entire cast.\n\n"
         "I also teach: I founded and run my own character art school, so building other artists "
         "up is what I already do, and it is the difference between a senior who delivers and a "
         "lead who raises a team.\n\n"
         "I want to relocate to Leamington Spa and I am fully open to moving for the role. I would "
         "need Skilled Worker sponsorship.\n\n"
         "Portfolio: " + ART, None, False),
    ])

# ---------------------------------------------------------------- 4 UBISOFT MASSIVE
vaga(
    id='massive', studio='Ubisoft Massive Entertainment',
    role="Lead Character Artist, Tom Clancy's The Division 2 · Malmö, Suécia",
    chips=[('wall', 'DataDome no botão'), ('plain', 'SmartRecruiters'), ('plain', 'REF31739L')],
    url='https://jobs.smartrecruiters.com/Ubisoft2/744000144027102',
    ok='Casa grande, motor próprio (Snowdrop), e o anúncio pede "Produce and deliver quality 3D '
       'assets for the game (Character Art, NPCs, weapons and gear, Cinematic assets)" e '
       '"Ability to realize characters from concepts and Art Director briefs".',
    note='Já existe uma carta pessoal sua entregue na Massive: em 07/09 saiu email para '
         'henrick.pelletier@ubisoft.com. A recusa que a Ubisoft mandou em 02/09 era de OUTRA '
         'requisição, em outro estúdio e outro país. Esta aqui está aberta e nunca foi enviada.',
    campos=[
        ('Upload resume / cover letter', 'Vini_Cavalcanti_CV.pdf + Vini_Cavalcanti_Cover_Letter.pdf', None, True),
        ('Nome / Email / Localização', 'Vini Cavalcanti\n' + EMAIL + '\n' + LOC, None, True),
        ('LinkedIn / Portfolio', LI + '\n' + ART, None, True),
        ('Autorizado a trabalhar na Suécia?', 'No', None, True),
        ('Precisa de patrocínio?', 'Yes', None, True),
        ('Aceita realocar para Malmö?', 'Yes', None, True),
        ('Pretensão', 'Open to aligning with your band for the role; as a reference, around EUR 55,000 per year.', None, True),
        ('Carta / mensagem',
         "The Division 2 keeps shipping characters, NPCs, weapons and gear years after launch, and "
         "the posting asks a Lead to produce those assets, prioritise the team's day to day, and "
         "manage the collaboration with codev. I have done the production half for a decade and "
         "the standard-setting half for five years.\n\n"
         "At E-Line Media I have spent almost five years taking Endstar's hero characters from "
         "first sculpt to engine: high poly, retopology, UVs, baking, PBR texturing, LODs and "
         "integration, plus hair and fur grooming in Houdini. Realising characters from concept "
         "and from an Art Director's brief is the normal shape of my work, not the exception. On "
         "The Wingfeather Saga season 1 at Angel Studios I modeled and hand painted the season's "
         "characters.\n\n"
         "On managing codev: I spent three years at PUGA Studios delivering assets under another "
         "studio's art direction, in the client's defined style, with revision rounds as routine. "
         "I have sat on the outsourcing side of that relationship, which is the fastest way to "
         "learn how to give feedback that a partner can actually act on.\n\n"
         "I want to relocate to Malmö and I am fully open to moving for the role. I am not an EU "
         "citizen and would need sponsorship; my academic background, with an honors laurea, a "
         "postgraduate specialization in Game Art, a master's in progress, IELTS and publications, "
         "makes a strong case.\n\n"
         "Portfolio: " + ART, None, False),
    ])

# ---------------------------------------------------------------- 5 OFFWORLD
vaga(
    id='offworld', studio='Offworld Industries',
    role='3D Character Artist · New Westminster, British Columbia, Canadá',
    chips=[('wall', 'reCAPTCHA'), ('plain', 'BambooHR'), ('plain', 'vaga 199')],
    url='https://owi.bamboohr.com/careers/199',
    ok='Título literal da sua disciplina, em Canadá anglófono. O anúncio: "work closely with the '
       'Art Director and Character Art Lead to create high-quality characters, clothing, and '
       'accessories", "collaborate across disciplines and with external partners", '
       '"optimized for in-engine performance". É Unreal, nos jogos Squad e Starship Troopers: '
       'Extermination.',
    note='A vaga irmã, a 198 de 3D Generalist, já estava no painel desde 07/09 e esta não estava, '
         'apesar de ser o encaixe melhor. Foi exatamente o erro que você apontou hoje.',
    campos=[
        ('Resume / Cover letter', 'Vini_Cavalcanti_CV.pdf + Vini_Cavalcanti_Cover_Letter.pdf', None, True),
        ('Nome / Email', 'Vini Cavalcanti\n' + EMAIL, None, True),
        ('Endereço / Cidade / País', LOC, None, True),
        ('LinkedIn / Website', LI + '\n' + ART, None, True),
        ('Are you legally authorized to work in Canada?', 'No', None, True),
        ('Will you now or in the future require sponsorship?', 'Yes', None, True),
        ('Willing to relocate to New Westminster, BC?', 'Yes', None, True),
        ('Pretensão salarial', 'Open to aligning with your band for the role; as a reference, around CAD 80,000 per year.', None, True),
        ('Carta / mensagem',
         "Offworld is asking for a 3D Character Artist who owns the full character asset pipeline "
         "from creation to implementation, working with the Art Director and the Character Art "
         "Lead and with external partners, on Unreal multiplayer games. That is a description of "
         "what I do now.\n\n"
         "At E-Line Media I have spent almost five years taking Endstar's hero characters from "
         "first sculpt to engine: high poly, retopology, UVs, baking, PBR texturing, LODs and "
         "integration, with performance budgets to respect the whole way. Clothing and accessories "
         "are part of that same pass, and I groom hair and fur in Houdini. Before that, three "
         "years at PUGA Studios delivering assets under another studio's art direction, in the "
         "client's defined style, which is the same relationship your external partners are on.\n\n"
         "On The Wingfeather Saga season 1 at Angel Studios I modeled and hand painted the "
         "season's characters. I have been Senior for five years, I review other artists' work and "
         "set the asset standard, and I founded and run my own character art school.\n\n"
         "I want to relocate to British Columbia and I am fully open to moving for the role. I am "
         "not a Canadian citizen and would need visa sponsorship; my academic background, with an "
         "honors laurea, a postgraduate specialization in Game Art, a master's in progress, IELTS "
         "and publications, makes a strong case.\n\n"
         "Portfolio: " + ART, None, False),
    ])

# ---------------------------------------------------------------- 6 PEOPLE CAN FLY
vaga(
    id='pcf', studio='People Can Fly',
    role='Principal Character Artist · remoto a partir da Polônia ou do Canadá (EST)',
    chips=[('wall', 'DataDome no botão'), ('plain', 'SmartRecruiters'), ('ok', 'zero termo de veto')],
    url='https://jobs.smartrecruiters.com/PeopleCanFly/744000134528029',
    ok='Achada nesta madrugada relendo os 123 quadros do censo. É a descrição de criatura mais '
       'próxima do seu portfólio que apareceu hoje: "Possibilité de créer des créatures complexes, '
       'des bipèdes aux quadrupèdes et au-delà", mais rostos humanos, roupas, PBR em Substance '
       'Painter e Unreal. É AAA de verdade: Gears of War E-Day com a Microsoft, projeto Echo para a '
       'KRAFTON e Lost Rift.',
    note='Passei o anúncio inteiro pela régua de veto, termo a termo: authoriz, eligib, sponsor, '
         'work permit, citizen, resident. ZERO acerto, nem um. O que existe é uma exigência de '
         'lugar, não de cidadania: "We are looking for someone who can work remotely from either '
         'Poland or Canada (EST)". Ou seja, é candidatura para quem vai morar lá, que é exatamente '
         'o que você quer, e a PCF tem escritório na Polônia, no Reino Unido, na Irlanda, nos EUA e '
         'no Canadá. O anúncio é de 26/06 e continua ativo na API oficial hoje.',
    campos=[
        ('Upload resume / cover letter', 'Vini_Cavalcanti_CV.pdf + Vini_Cavalcanti_Cover_Letter.pdf', None, True),
        ('Nome / Email / Localização', 'Vini Cavalcanti\n' + EMAIL + '\n' + LOC, None, True),
        ('LinkedIn / Portfolio', LI + '\n' + ART, None, True),
        ('Precisa de patrocínio?', 'Yes', None, True),
        ('Aceita realocar para a Polônia ou para o Canadá?', 'Yes, and that is what I am looking for.', None, True),
        ('Pretensão', 'Open to aligning with your band for the role; as a reference, around CAD 95,000 per year.', None, True),
        ('Carta / mensagem',
         "The posting asks for complex creatures from bipeds to quadrupeds and beyond, believable "
         "human faces and clothing, hard surface for weapons and armour, PBR in Substance Painter, "
         "and Unreal. That list is my portfolio, in order.\n\n"
         "I have more than ten years in 3D characters. For almost five of them, at E-Line Media, I "
         "have taken Endstar's hero characters from first sculpt to engine: high poly and low poly, "
         "retopology, UVs, baking, PBR texturing, LODs and integration in Unreal. I also groom hair "
         "and fur in Houdini, which is the part that makes quadrupeds and creatures hold up in "
         "close shots. On The Wingfeather Saga season 1 at Angel Studios I modeled and hand painted "
         "the season's characters, creatures included.\n\n"
         "A Principal is expected to hold the bar rather than just clear it. I have been Senior for "
         "five years, I review other artists' work and set the asset standard, and I founded and "
         "run my own character art school, so giving feedback that another artist can act on is "
         "something I do every week. I have also delivered under another studio's art direction at "
         "PUGA Studios, with revision rounds as routine, which is the same discipline as holding "
         "quality across a distributed pipeline.\n\n"
         "I am fully open to relocating, to Poland or to Canada, and I would need visa sponsorship. "
         "My academic background, with an honors laurea, a postgraduate specialization in Game Art, "
         "a master's in progress, IELTS and publications, makes a strong case.\n\n"
         "Portfolio: " + ART, None, False),
    ])

# ---------------------------------------------------------------- 7 AVALANCHE
vaga(
    id='avalanche', studio='Avalanche Studios Group',
    role='Lead Character Artist · Estocolmo, Suécia, híbrido',
    chips=[('wall', 'hCaptcha'), ('plain', 'Lever'), ('wall', 'não paga realocação')],
    url='https://jobs.lever.co/avalanchestudios/8f7bd580-5877-446e-83cb-97bb1fce0f6a/apply',
    ok='Criatura e animal, que é o que o seu portfólio tem: "a high degree of expertise in animal '
       'and creature design, as well as strong foundations in general character art" e "Deep '
       'understanding of realistic anatomy, materials, fur/skin workflows". O anúncio também diz '
       'para se candidatar mesmo sem cumprir todos os requisitos.',
    note='LEIA ANTES DE GASTAR O SEU TEMPO: o anúncio termina com "please note that relocation '
         'assistance is not available for this role". Não é veto de autorização, e não impede a '
         'candidatura, mas significa que a mudança sai do seu bolso se houver oferta. Eu prefiro '
         'que você saiba disso antes de preencher, e não depois.',
    campos=[
        ('Resume/CV (em inglês, o anúncio pede)', 'Vini_Cavalcanti_CV.pdf', None, True),
        ('Full name / Email', 'Vini Cavalcanti\n' + EMAIL, None, True),
        ('Current location (obrigatório)', LOC, None, True),
        ('Current company', 'E-Line Media', None, True),
        ('LinkedIn / Portfolio', LI + '\n' + ART, None, True),
        ('Additional information',
         "The posting asks for a Lead who is a subject-matter expert in animal anatomy, behavior "
         "and realism, with deep understanding of fur and skin workflows, on top of strong general "
         "character art. Creature and animal work is the spine of my portfolio, and fur is "
         "something I build rather than something I avoid: I groom hair and fur in Houdini as part "
         "of my normal asset pass.\n\n"
         "I have more than ten years in 3D characters and I have been Senior for five. At E-Line "
         "Media I have spent almost five years taking Endstar's hero characters from first sculpt "
         "to engine: high poly, retopology, UVs, baking, PBR texturing, LODs and integration. On "
         "The Wingfeather Saga season 1 at Angel Studios I modeled and hand painted the season's "
         "characters, which included the creature side of that cast.\n\n"
         "On the people half of the role: I review other artists' work and set the asset standard "
         "in my current team, and I founded and run my own character art school, so coaching, "
         "structured feedback and growth paths are already how I spend part of every week.\n\n"
         "I want to relocate to Stockholm and I am fully open to moving for the role, including "
         "the three days a week in Södermalm. I am not an EU citizen and would need sponsorship.\n\n"
         "Portfolio: " + ART, None, False),
    ])

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

# ---------------------------------------------------------------- 9 TTK
vaga(
    id='ttk', studio='TTK Games',
    role='Character Artist · Estocolmo, Suécia, híbrido, permanente',
    chips=[('wall', 'reCAPTCHA'), ('plain', 'site próprio'), ('ok', 'faixa publicada')],
    url='https://ttkgames.com/careers/job?id=561860',
    ok='Faixa salarial publicada no próprio anúncio: "Starting from 34,000 SEK per month, rising '
       'to 47,000 with experience, plus bi-annual bonus". Pede "strong understanding of human '
       'anatomy, form, and character design principles" e ZBrush, Maya/Blender, Substance Painter, '
       'Unreal ou Unity.',
    note='ARMADILHA DE ENDEREÇO: os links do Pinpoint (/postings/... e /jobs/...) devolvem 404 e a '
         'vaga parece morta. A porta de verdade é o link acima, com ?id=. Em 08/09 o envio '
         'automático voltou 500 "ReCaptcha Failed", que é justamente o que a sua mão resolve. '
         'Confira a mensagem de confirmação na tela antes de fechar.',
    campos=[
        ('Nome / Email', 'Vini Cavalcanti\n' + EMAIL, None, True),
        ('Localização', LOC, None, True),
        ('CV / Cover letter', 'Vini_Cavalcanti_CV.pdf + Vini_Cavalcanti_Cover_Letter.pdf', None, True),
        ('LinkedIn / Portfolio', LI + '\n' + ART, None, True),
        ('Precisa de patrocínio na Suécia?', 'Yes', None, True),
        ('Pretensão', 'Your published range works for me. As a reference I am looking at the upper part of it, and I am open to aligning with where my experience places me in your band.', None, True),
        ('Campo livre / carta',
         "You are asking for a 3D artist with a strong understanding of human anatomy, form and "
         "character design principles, working in ZBrush, Maya or Blender, Substance Painter and a "
         "real engine. That is my toolset and it has been for ten years.\n\n"
         "At E-Line Media I have spent almost five years taking Endstar's hero characters from "
         "first sculpt to engine: high poly, retopology, UVs, baking, PBR texturing, LODs and "
         "integration in Unreal. I also groom hair and fur in Houdini. On The Wingfeather Saga "
         "season 1 at Angel Studios I modeled and hand painted the season's characters, so "
         "storytelling through the character rather than around it is something I have practised "
         "on a show as well as in a game.\n\n"
         "I have been Senior for five years, I review other artists' work and set the asset "
         "standard, and I founded and run my own character art school.\n\n"
         "I want to relocate to Stockholm and I am fully open to moving for the role. I am not an "
         "EU citizen and would need sponsorship.\n\n"
         "Portfolio: " + ART, None, False),
    ])

# ---------------------------------------------------------------- 10 FENRIS
vaga(
    id='fenris', studio='Fenris Creations',
    role='Register Your Interest, banco de talentos · Reykjavík, Islândia',
    chips=[('ok', 'sem captcha'), ('plain', 'Pinpoint'), ('ok', 'patrocina visto')],
    url='https://careers.fenriscreations.com/register-your-interest/new',
    ok='É a CCP Games renomeada, dona do EVE Online. O processo seletivo tem um estágio chamado '
       'literalmente "Stage 5: Relocation and Benefits Chat", e o formulário pergunta "Would you '
       'need a VISA sponsorship in order to relocate for the role?". Casa que pergunta isso é casa '
       'que patrocina.',
    note='Eu não fechei o envio: o servidor recusou com "Answers boolean answer can\'t be blank", '
         'porque a pergunta de visto é condicional e só aparece depois que a localização é '
         'respondida. Nada ficou registrado do lado deles. Confira com o olho o campo de '
         'localização: foi exatamente ali que o meu clique caiu em USA/Canada quando eu pedi Other.',
    campos=[
        ('First Name / Last Name / Email', 'Vini\nCavalcanti\n' + EMAIL, None, True),
        ('LinkedIn URL', LI, None, True),
        ('What is your current location?', 'Other', 'As opções são Iceland, United Kingdom, EEA/EU, USA/Canada, Asia e Other.', True),
        ('Would you need a VISA sponsorship…?', 'Yes', 'Só aparece depois que a localização é respondida.', True),
        ('Are you a…', 'None of the above?', None, True),
        ('Where did you hear about this position?', 'Fenris Creations Website', None, True),
        ('Willing to relocate / Locations / Departments / Gender', 'Yes\nReykjavík\nArt\nPrefer Not To Say', None, True),
        ('Personal Summary',
         "I am a Senior 3D Character Artist with more than ten years in stylized characters, and I "
         "am writing to be on your list for character, creature and asset work.\n\n"
         "On The Wingfeather Saga season 1 at Angel Studios I modeled and hand painted the "
         "characters, so the stylized surface treatment was mine from block-in to final. For "
         "almost five years I have been with E-Line Media in Arizona, taking Endstar's hero assets "
         "from first sculpt to engine: sculpt, retopology, UVs, baking, PBR texturing, trim "
         "sheets, material work, look development and engine integration. I also do hair and fur "
         "grooming in Houdini. Before that I spent three years at PUGA Studios delivering assets "
         "under another studio's art direction, in the client's defined style, with revision "
         "rounds as routine.\n\n"
         "Fenris builds deep, player-driven worlds that hold communities together for decades, and "
         "worlds like that are made of assets that have to survive being looked at for years, not "
         "for one shot. That is the kind of asset I like building. I have been Senior for five "
         "years, I review other artists' work and set the asset standard, and I founded and run my "
         "own character art school.\n\n"
         "My portfolio holds more than 45 projects with over 60 characters across many titles, and "
         "my personal projects are some of the strongest pieces in it.\n\n"
         "I want to relocate to Reykjavík and I am fully open to moving for the role. I am not an "
         "EU or EEA citizen, so I would need visa sponsorship; my academic background, with an "
         "honors laurea, a postgraduate specialization in Game Art, a master's in progress, IELTS "
         "and publications, makes a strong visa case.\n\n"
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
    <p class="sub">Onze formulários, <strong>todos de personagem ou criatura</strong>. Você mediu
    certo: das 27 candidaturas de 09 e 10 de setembro, 17 eram de ambiente e 7 de personagem.
    Esta lista é a correção. Nenhuma vaga de ambiente entrou aqui.</p>
  </header>

  <div class="howto">
    <p><strong>Como usar.</strong> Abra o link da vaga e, para cada campo, toque em <em>Copiar</em> e cole. Os textos longos já estão prontos e citam o anúncio daquele estúdio, não precisam de edição.</p>
    <p><strong>Telefone e endereço não estão aqui de propósito.</strong> Eles moram só no seu documento privado do Drive, <em>CAMPANHA - dados pessoais dos formulários</em>. Copie de lá quando o campo pedir.</p>
    <p><strong>A etiqueta de captcha diz por que a vaga está com você</strong> e não com a automação. Nenhuma dessas onze foi enviada: conferi uma a uma contra o registro de envios antes de montar a página.</p>
    <p><strong>Se você só tiver dois minutos hoje:</strong> a nº 3, Lighthouse Games. O formulário oficial exige apenas nome, sobrenome e email. Todo o resto é opcional.</p>
  </div>

''')
out.write('  <nav class="jump" aria-label="Ir para uma vaga">\n')
for i, v in enumerate(VAGAS, 1):
    out.write('    <a href="#%s">%d · %s</a>\n' % (v['id'], i, html.escape(v['studio'])))
out.write('  </nav>\n\n')
for i, v in enumerate(VAGAS, 1):
    out.write(artigo(i, v))
out.write('''  <footer>
    <p><strong>O que saiu da lista anterior e por quê.</strong> A versão que eu te mandei antes tinha
    sete vagas e só uma era de personagem. Saíram daqui Skydance Environment Surfacing, Ubisoft
    Level Artist (três), Sperasoft Lead Props/Environment, Magic Media 3D Generalist, Glinda Games e
    Jam City Level Design Artist. Todas continuam registradas no repositório, mas nenhuma é a sua
    disciplina e nenhuma volta para a sua mão até que a fila de personagem esteja vazia.</p>
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
