# Triagem da fila europeia do gamedevmap — 08/09

Fonte: `automacao/fila-gamedevmap-europa.csv` (4.148 estúdios, 777 já triados na colheita).
Esta rodada resolveu **1.664 linhas**: 1.651 que estavam `nao-triado` e 13 que estavam em `porta-ok`
e ganharam veredito de vaga depois de eu abrir o anúncio.

Estado da fila depois desta rodada: **2.428 triados de 4.148 (58,5%)**, contra 777 (18,7%) antes.
**Ainda faltam 1.281 linhas em-escopo** marcadas `nao-triado` — quase todas em cidades de segunda e
terceira densidade que não entraram no recorte, mais a Oceania inteira.

Nada foi enviado: nenhum email, nenhum rascunho, nenhum formulário preenchido, nenhum navegador aberto.
Só `curl`, WebSearch e WebFetch.

---

## 1. O QUE FOI TRIADO, por cidade

| cidade | linhas | | cidade | linhas |
|---|---:|---|---|---:|
| Stockholm | 107 | | Cologne | 28 |
| Warsaw | 85 | | Hamburg | 27 |
| Barcelona | 59 | | Milan | 27 |
| Gothenburg | 55 | | Helsinki | 26 |
| London | 43 | | Leamington Spa | 26 |
| Copenhagen | 43 | | Zürich | 26 |
| Berlin | 43 | | Manchester | 25 |
| Madrid | 41 | | Dublin | 24 |
| Brighton | 37 | | Lyon | 24 |
| Skövde | 36 | | Brno | 22 |
| Dundee | 34 | | Vienna | 21 |
| Malmö | 32 | | Liverpool | 21 |
| Guildford | 32 | | Wrocław | 20 |
| Amsterdam | 31 | | Munich | 18 |
| Utrecht | 30 | | Oslo | 15 |
| Edinburgh | 30 | | Lisbon | 14 |
| Kraków | 29 | | Paris | 10 |
| Bristol | 28 | | Prague / Brussels | 8 / 8 |

(mais ~40 cidades menores com menos de 20 linhas cada)

## 2. O QUE FOI TRIADO, por país

| país | linhas | | país | linhas |
|---|---:|---|---|---:|
| Suécia | 294 | | Dinamarca | 50 |
| Inglaterra | 277 | | Finlândia | 48 |
| Polônia | 172 | | Suíça | 38 |
| Alemanha | 157 | | Irlanda | 31 |
| Espanha | 128 | | Tchéquia | 30 |
| Holanda | 113 | | Bélgica | 30 |
| França | 65 | | Áustria | 25 |
| Escócia | 64 | | Portugal | 22 |
| Itália | 56 | | Noruega | 20 |
|  |  | | Irl. do Norte / R.U. / País de Gales | 18 / 13 / 13 |

## 3. Distribuição dos veredictos

| veredito | linhas |
|---|---:|
| site vivo, porta de carreiras não localizada no HTML | 905 |
| `porta-ok:<url>` (página de carreiras viva, sem quadro legível) | 482 |
| quadro de ATS aberto e lido | 111 |
| porta sem resposta | 105 |
| veredito manual (vaga aberta, descarte ou veto) | 51 |
| linhas cujo veredito começa em **VAGA VIVA** da disciplina | 10 |

(a última linha conta **linhas do CSV** escritas nesta rodada, não requisições: um mesmo estúdio aparece
em várias cidades. Somadas às 3 que já existiam na colheita, o arquivo tem hoje 13 linhas `VAGA VIVA`)

**Quadros de vaga com pulso**: abri e li **111 quadros** (Greenhouse, Lever/Lever EU, Ashby, Recruitee,
Teamtailor, BambooHR, Workable, SmartRecruiters, Personio, Pinpoint, Breezy, eRecruiter, Elevato,
formulário próprio). Somaram **mais de 900 anúncios**. Depois de ler o texto inteiro sobraram
**12 requisições vivas da disciplina** e 11 de prioridade MÉDIA.

---

## 4. VAGAS VIVAS DA DISCIPLINA

### 4.1 A ÚNICA REQUISIÇÃO NOVA, SEM VETO E AINDA NÃO TOCADA

**Snowprint Studios — Senior 3D Character Artist — Estocolmo**
- Link direto: <https://career.snowprintstudios.com/jobs/8341580-senior-3d-character-artist>
- Formulário: <https://career.snowprintstudios.com/jobs/8341580-senior-3d-character-artist/applications/new> (HTTP 200)
- **ATS: Teamtailor em domínio próprio** (`career.snowprintstudios.com`). Não existe
  `snowprint.teamtailor.com`: só apareceu porque eu sondei `career.<domínio>/jobs.json`.
- Requisição `8341580`, uuid `70f94180-fa55-4de5-8fe5-d6e06a7a4aef`, **publicada em 08/09/2026 às 14h28** — nasceu hoje.
- Formato: **híbrido**, escritório em Södermalm, Estocolmo. "We work from the office on Tuesdays and
  Fridays." Tipo de contrato **não publicado**. **Faixa salarial não publicada.**
- Busca literal de veto, resultado palavra por palavra:
  `authoriz` NENHUM · `eligib` NENHUM · `sponsor` NENHUM · `work permit` NENHUM ·
  `must be based` NENHUM · `days a week` NENHUM · `resident` NENHUM · `visa` NENHUM ·
  `relocat` NENHUM · `citizen` NENHUM · `svenska`/sueco NENHUM.
  Os dois únicos acertos foram `hybrid` ("hybrid working model") e `fluent in` ("You're fluent in
  ZBrush, Maya, Substance Painter" — ferramenta, não idioma).
- Frase que fecha o anúncio: *"We are an international company with many nationalities represented.
  Our company language is English, so your application should therefore be in English."*
- Encaixe: pede personagem **estilizado**, ZBrush/Maya/Substance, Unity, 10–30k polígonos, e
  **coordenação de outsourcing** ("coordinating our external character art production… review
  deliveries and provide clear, constructive feedback"), que casa com o histórico de outsourcing dele.
- **Dedupe conferido**: o id `8341580` e o uuid não aparecem em `docs/index.html`, `enviados.csv` nem
  `processados.csv`. O estúdio já era conhecido — em 07/09 a campanha fez cadastro no **Connect**
  (banco de talentos) da Snowprint — mas **isso não é candidatura a esta requisição**, que nem existia.
- Marca de captcha no HTML da página: **nenhuma**. Não escrevo "sem captcha": veredito só com o clique.

### 4.2 VAGA DA DISCIPLINA QUE **OFERECE REALOCAÇÃO** (já no painel, ainda pendente)

**Gaijin Entertainment — Lead Material & Texture Artist**
- Link direto: <https://gaijinent.com/job/material--texture-artist>
- ATS: **formulário próprio** no site (sem ATS de terceiro); alternativa declarada por email para
  `job@gaijinent.com` com pretensão salarial no corpo.
- Formato: **"Work format: remote or office"**. Salário: *"competitive salary (the level of salary is
  discussed individually with the candidate at the interview)"* — **não publicado**.
- **SINAL POSITIVO, frase literal**: *"Our company helps with relocation to: Hungary, Cyprus, Germany,
  Dubai, Montenegro, Latvia, and Armenia."*
- Busca literal de veto: `authoriz` NENHUM · `eligib` NENHUM · `sponsor` NENHUM · `work permit` NENHUM ·
  `must be based` NENHUM · `days a week` NENHUM · `resident` NENHUM · `citizen` NENHUM.
  Únicos acertos: `relocat` (a frase positiva acima) e `remote` (formato de trabalho).
- Pede 7+ anos, Substance Designer/Painter, PBR, materiais de hard-surface, arquitetura e terreno,
  e liderança sobre time de outsourcing.
- **Dedupe**: já está em `PORTAIS` como *"Gaijin Entertainment (Lead Material & Texture Artist)"*, com
  `done = False`. Ou seja, conhecida mas **não enviada**. A entrada do painel não registrava a oferta
  de realocação; agora registra.
- O HTML da página tem a palavra `captcha`. Não escrevo "sem captcha"; veredito só com o clique.

### 4.3 VAGA DA DISCIPLINA COM **VETO ESCRITO** (descarte)

**PixelAnt Games (Sumo Digital) — Experienced 3D Character Artist — Wrocław**
- Link: <https://pixelantgames.com/careers/experienced-3d-character-artist/>
- Formulário: <https://system.erecruiter.pl/FormTemplates/RecruitmentForm.aspx?WebID=1dd6299e378243219024961e94cfe392>
- ATS: **eRecruiter** (Polônia). Formato: *"Flexible work model: onsite in our Wrocław office, hybrid,
  or remote"*, **contrato B2B**. Salário não publicado.
- **VETO ESCRITO, frase literal**: *"Communicative level of English and Polish is a must."*
- Fora isso o anúncio é um encaixe perfeito (anatomia, roupa, cabelo, ZBrush, Marvelous, UE5, 5+ anos
  AA/AAA). O veto é de **idioma**, não de residência — se o Vini falar polonês, ela volta à mesa.
- `authoriz` NENHUM · `eligib` NENHUM · `sponsor` NENHUM · `work permit` NENHUM · `resident` NENHUM.

### 4.4 VAGAS DA DISCIPLINA QUE A CAMPANHA **JÁ CONHECIA** (dedupe pegou)

| estúdio | vaga | link | situação já registrada |
|---|---|---|---|
| Teyon | Senior/Lead Character Artist, Cracóvia (Elevato) | <https://teyon.elevato.net/en/seniorlead-character-artist,j,158> | **RECUSADA em 03/09** por `system@elevato.net`. Não reenviar. O anúncio **oferece realocação**: *"Relocation support for candidates willing to move to Kraków"*, híbrido 3+2, só exige *"Fluency in English"* |
| Playdead | Experienced Material and Texture Artist, Copenhague (Breezy `d6b5a5e4f54a01`) | <https://playdead.breezy.hr/p/d6b5a5e4f54a01-experienced-material-and-texture-artist> | **CANDIDATURA ENVIADA em 06/09**, confirmada na tela. Busca de veto no texto inteiro: **NENHUM termo**; só diz *"You should be willing to work at the Playdead office in Copenhagen"* |
| Asobo Studio | Character Artist H/F, Bordeaux (Lever EU) | <https://jobs.eu.lever.co/asobostudio/1ab1d28f-6f7c-4106-b43f-6ef78dcb7603> | **Mesmo uuid já em `PORTAIS`**. Faixa publicada 32k–47k EUR/ano, 35h/semana. Único ponto novo que registro: pede *"un niveau de français et anglais opérationnel"* — exigência escrita de **francês** |
| Ubisoft Massive | Lead Character Artist, Malmö (SmartRecruiters `744000144027102`, REF31739L) | <https://jobs.smartrecruiters.com/Ubisoft2/744000144027102> | Já no painel e revalidada em 06/09 |
| Wargaming | 3D Character Artist, Nicósia (Greenhouse `8161671`) | <https://job-boards.greenhouse.io/wargamingen/jobs/8161671> | Já no painel desde 05/09 |
| Larian Studios | Character Artist – Open Application (Lever `64e1e658-…`) | <https://jobs.lever.co/larian/64e1e658-7c7a-4c7f-b950-f997d40a9d8e> | Já em `PORTAIS` com `done = True`. É **banco de talentos**, não requisição datada |
| Studio RUCACH | Stylized 3D Character Artist, Galway | <https://www.rucach.com/jobs/> | Email **já enviado em 06/09**. É **subcontrato** para um estúdio britânico, página datada de 2024, sem formulário |
| Cast Iron Games | Lead 3D Artist, Wakefield (Teamtailor, 02/02) | <https://careers.castirongames.com/jobs/7154430-lead-3d-artist> | Já em `PORTAIS` como **"DESCARTADA POR VETO DE RESIDÊNCIA"** |

**Placar honesto do dedupe: de 12 vagas vivas da disciplina que apareceram, 9 já eram conhecidas.**
Duas dessas já tinham desfecho (uma recusa na Teyon e uma candidatura enviada na Playdead) e uma já
estava marcada como descartada por veto (Cast Iron) — exatamente o risco que o brief mandou eliminar.
Das 3 novas, **uma está limpa** (Snowprint) e **duas têm veto escrito** (PixelAnt, idioma polonês;
Just Won't Die, residência no Reino Unido).

---

## 5. Prioridade MÉDIA (ambiente, prop, 3D genérico) — vivas e conferidas

| estúdio | vaga | cidade | link | veto literal |
|---|---|---|---|---|
| **Grimlore Games (THQ Nordic)** | (Senior/Principal) Environment Artist (m/f/d) | Munique | <https://grimloregames.com/senior-environment-artist/> | Sem veto. **Sinal positivo**: *"you are welcome to join us in Munich, Germany but we do also offer a **full remote position**"* e *"EU applicants will be fulltime employees, **externals will work on a service agreement basis**"* — ou seja, não-europeu entra por contrato de serviço |
| Envar Games | Senior 3D Environment Artist (contrato a termo) | Estocolmo | <https://careers.envarstudio.com/jobs/8281404-senior-3d-environment-artist-fixed-term> | Sem veto escrito; marcado **Onsite**, publicada 31/08 |
| Embark Studios | Environment Artist | Estocolmo | <https://careers.embark-studios.com/jobs/7964466-environment-artist> | publicada 24/06 |
| Stillfront / Sandbox Interactive | Lead 3D Environment Artist (m/f/d) | Berlim | <https://stillfrontgroup.teamtailor.com/jobs/8094866-lead-3d-environment-artist-m-f-d> | — |
| Scopely / Niantic | 3D Artist · Senior 3D Artist · Lead 3D Artist (MONOPOLY GO!) | Barcelona | <https://job-boards.greenhouse.io/scopely/jobs/5398026008> (senior) | Híbrido em Barcelona. Único acerto de `resident` é o link da política de privacidade da Califórnia. **Já está no painel** |
| Jagex | Environment Artist (RuneScape: Dragonwilds) | Cambridge | <https://www.jagex.com/careers> (quadro Workable `jagex-limited`) | quadro é SPA, o detalhe de cada vaga não abre por curl |
| Lucid Games | Senior / Lead / Principal Environment Artist | Liverpool | <https://www.lucidgames.co.uk/careers/> | anúncios datados de **2024**, quadro velho |
| Nordcurrent | Lead 2D/3D Artist | Vilnius | <https://nordcurrent.com/jobs/> | **faixa publicada: a partir de 4.400 EUR/mês bruto**, full-time. Disciplina 2D/3D misturada |
| A4VR | Senior 3D Artist | Düsseldorf | <https://www.a4vr.com/jobs> | anúncio inteiro em alemão, foco em foliage/archviz; página com copyright de 2018 |
| Pathos Interactive | 3D Artist (lista permanente, sem data) | Gotemburgo | <https://www.pathosinteractive.net/Contact/?Job> | sem veto; é lista permanente, não requisição |
| Cosmico | SENIOR 3D ARTIST (sem descrição nem data) | Estocolmo | <https://www.cosmicogames.com/career> → link vai para `/contact` | sem texto de vaga para buscar veto |

---

## 6. PORTAS COM APOIO DE IMIGRAÇÃO DECLARADO (sem vaga da disciplina hoje)

Guardar para quando abrir vaga; são os estúdios que **escreveram** que pagam a mudança.

- **IO Interactive** (Copenhague / Malmö / Barcelona / Brighton) — a página de carreiras lista, palavra
  por palavra: *"visa support · work permit · finding an apartment · tax office registration · finding a
  bank and setting up a bank account"* e *"flight tickets for you and your family"*.
  Quadro Teamtailor em <https://apply.ioi.dk/jobs.json>: **1 vaga viva hoje (HR Consultant)**, nenhuma de
  arte. Porta espontânea: <https://apply.ioi.dk/jobs/2380320-unsolicited-applications>.
  Estúdio já trabalhado pela campanha (perfil do Connect completado em 07/09).
- **EB Studio (Ernst Borg), Malmö** — estúdio **totalmente novo**, não aparece em `PORTAIS`, `STUDIOS`,
  `enviados.csv` nem `processados.csv`. Texto: *"EB Studio offers help with relocation for the right
  candidate."* **ARMADILHA MEDIDA**: a página mostra descrições completas de **Environment Artist,
  Lighting Artist, Material Artist e Prop Artist**, e só no rodapé, depois de todas elas, diz
  *"We have no open positions at this time. Want to submit an open application? Send us an email with
  your CV and portfolio to job@ernstborg.studio"*. Quem parasse na descrição do Material Artist
  registraria vaga que não existe. Vale como porta espontânea de alta qualidade.
- **Teyon, Cracóvia** — *"Relocation support for candidates willing to move to Kraków"* (a vaga em si já
  foi recusada em 03/09, mas a política vale para a próxima).
- **Gaijin Entertainment** — realocação para 7 países, ver 4.2.
- **Grimlore Games, Munique** — remoto total e contrato de serviço para não-europeus, ver seção 5.

---

## 7. DESCARTES, com a frase do anúncio entre aspas

**Veto escrito de residência ou autorização de trabalho**

- **Just Won't Die Games** (Senior 3D/Character Artist, Cambridge) —
  *"To Apply — You must be eligible to work in the UK."* O texto ainda fala em *"due to the current
  pandemic"*, então é anúncio antigo. <https://www.justwontdie.com/senior-3d-character-artist>
- **Interior Night** (Mid-Senior Environment Artist, 9 meses, Londres) — título literal
  *"MID-Senior Environment Artist - 9 months contract - **UK based candidate**"* e, nos requisitos,
  *"right to work in the UK"*. <https://www.interiornight.com/jobs>
- **SquarePlay Games** (Londres) — *"We are looking for **UK-based**, freelancers for the following
  roles: … 3D environment and prop artist."* <https://www.squareplaygames.com/jobs>
- **Sassybot** (Breda, Holanda) — *"Must be a EU citizen or have a work permit for The Netherlands"*, e
  a própria página abre com *"currently have no open positions"*. <https://www.sassybot.com/jobs/>
- **Dionic Software** (Munique) — *"people living in and able to work in Germany"*, e a vaga está
  marcada *"Closed: Lead 3D Artist (Full Time, Germany) — This position is closed now."*
- **Cast Iron Games** (Wakefield) — já estava no painel como descartada por veto de residência.

**Veto escrito de idioma**

- **PixelAnt Games** — *"Communicative level of English and Polish is a must."* (detalhe em 4.3)
- **Asobo Studio** — *"Tu disposes d'un niveau de français et anglais opérationnel."* (vaga já conhecida)

**Descarte de disciplina (é 2D, é técnico, ou é outra coisa)**

- **Dark Cloud Games** (Lisboa) — a vaga se chama **Character Artist** mas o texto diz
  *"Como ilustrador 2D, irás trabalhar em um ambiente…"* e pede *"Excelente ilustração… Conhecimentos
  avançados de Adobe Photoshop"*. É ilustração 2D. Pena, porque oferece
  *"AUXÍLIOS: Moradia e realocação"*. <https://www.darkcloud.games/character-artist/>
- **Triband** (Copenhague) — Senior Game Artist exige *"expert-level skills in **vector art software**
  (we use Illustrator)"* com 3D low-poly só *"at least at an intermediate level"*.
  <https://careers.triband.net/jobs/8220733-senior-game-artist>
- **Herobeat Studios** (Barcelona) — a única vaga é Technical Artist.
- **Anshar Studios** (Katowice) — a única de personagem é **Junior** Character Artist.
- **Little Chicken Game Company** (Amsterdã) — só **estágios**: *"3D Artist Internship… We're looking for
  3D Art interns"*, mais candidatura espontânea por email.

**Quadro morto, anúncio arquivado ou vaga fechada**

- **ByteBarrel** (Gdańsk) — a vaga 3D Artist no skillshot.pl abre com **"Ogłoszenie zarchiwizowane"**
  (anúncio arquivado). <https://www.skillshot.pl/jobs/39305-3d-artist-at-byte-barrel-s-a>
- **Campfire Cabal** (Copenhague) — o topo diz *"We currently have no open positions"* e o texto do
  3D Artist ainda traz *"Application deadline: October 21st, **2022**"*.
- **Slug Disco Studios** — as vagas estão marcadas *"(closed)"* e *"We are no longer accepting
  applications"* na própria página.
- **Classy Games** — todas as vagas, inclusive 3D Artist (Blender), estão marcadas *"Coming Soon"*.
- **Ironbird Creations** (Cracóvia) — quadro Teamtailor com 3D Artist e Level Artist **de 2022**.
- **Twirlbound** — a única de 3D é estágio *"First Semester 2021-2022 year"*.
- **Housemarque** (Helsinque) — a Lead Character Artist que a busca na web indexou não existe mais:
  `boards-api.greenhouse.io/v1/boards/housemarque/jobs` devolve `{"jobs":[],"meta":{"total":0}}`.

**Menção de arte que NÃO é vaga (o filtro por palavra-chave erra aqui, fica registrado)**

- **Kevuru Games** e **Moonmana** — "Character artists / 3D Artists" é catálogo de serviço de outsourcing.
- **Black Shamrock**, **Infinity Vector**, **Puny Astronaut**, **Frame Break**, **Future Mark**,
  **INCISIV** — a menção é página de time ou depoimento de funcionário.
- **Sumo Digital** — "Visual Development" é nome de serviço do estúdio.
- **OZWE Games** — as menções a 3D Artist são posts de blog.
- **Frozenbyte** (Helsinque) — a página descreve as disciplinas de arte mas é **candidatura espontânea
  por email**, sem vaga datada; e diz *"We don't offer remote work possibilities, so we expect all our
  applicants are willing and able to relocate closer to our office if need be."*

---

## 8. MÉTODO: o que rendeu e o que não rendeu (para a próxima rodada não refazer)

**1. Sondar `career.<domínio>/jobs.json` acerta onde adivinhar slug não acerta.**
Rodei em 1.850 domínios de estúdio: **48 quadros Teamtailor/Recruitee em domínio próprio**, entre eles
Sharkmob, 10 Chambers, Arrowhead, Embark, Envar, Hazelight, Starbreeze, Coffee Stain, Ghost Ship,
Funcom, Coatsink, Dovetail, Fingersoft, Keen Games, Red Rover, Fool's Theory, Creepy Jar,
Ten Square Games, Stunlock, Neon Giant, MindArk, Vivid Games — e a **Snowprint**, que é a achada da
rodada. Nenhum desses tem subdomínio no fornecedor. Confirma a lição registrada em 07/09 e dá o
caminho certo: **não adivinhe `<nome>.teamtailor.com`, sonde `career./careers./jobs./job.` no domínio do estúdio**.

**2. Ler o TEXTO da página de carreiras rende mais que caçar link de ATS.**
Achei ATS no HTML de só **8%** das páginas. Mas varrer o texto visível atrás dos nomes de cargo achou
**44 páginas** com menção de disciplina, e foi daí que saíram PixelAnt, Teyon, Gaijin, EB Studio,
Just Won't Die, Dark Cloud e Cosmico. Recomendo inverter a ordem na próxima rodada: **texto primeiro, ATS depois.**

**3. O `sitemap.xml` não rende.** Rodei em 418 domínios sem porta de carreiras: **1 acerto**, e falso
(post de blog). Não repetir.

**4. Aggregadores não renderam nada aqui.** `jobs.workable.com/api/v1/jobs` devolve
`{"error":"rate_limit"}`; `gamesjobsdirect.com` casa por proximidade e devolve vaga de outra disciplina;
`builtin.com` e `relocateme.substack.com` são **bloqueados pelo proxy de egress** deste ambiente.

**5. Adivinhar token de ATS continua ruim.** Testei 10 palpites óbvios em Greenhouse
(massive, ubisoft, iointeractive, sharkmob, avalanchestudios, embracer, funcom…): **1 respondeu 200 e
era a empresa errada** — `remedy` no Greenhouse é uma farmácia dos Estados Unidos, com vagas em
Houston e Syracuse. Confere o número da rodada anterior (57 em 1.627).

**6. Workday e alguns Workable ficaram de fora, e isso é buraco declarado.**
12 quadros não abriram: Workday precisa do `Job_Posting_Site_ID` de cada tenant (Xbox/Activision,
Aristocrat/Product Madness, SEGA/Sports Interactive, Unity) e alguns tokens de Workable/Personio que eu
extraí do HTML estavam errados (Sperasoft, Team17, Arkadium, BeamNG, btf, astragon, Homa). Sobram
como dívida para a próxima rodada.

**7. A armadilha da EB Studio vale como regra nova.** Página que mostra descrições completas de cargo e
só no rodapé diz *"We have no open positions at this time"*. **Ler sempre o FIM da página de carreiras,
não só o bloco do cargo** — é o mesmo padrão do veto que mora no fim do anúncio.

---

## 9. O QUE TRAVOU, sem maquiagem

- **1.281 linhas em-escopo continuam `nao-triado`.** Cobri as 26 cidades do briefing mais uma segunda
  camada de ~80 cidades europeias, e ainda assim sobrou a cauda longa (cidades com menos de 15 estúdios)
  e a **Oceania inteira** (Melbourne 81, Brisbane 29, Sydney 27, Auckland 28), que está no arquivo mas
  fora do recorte pedido.
- **905 sites responderam 200 e não expuseram porta de carreiras no HTML.** São SPA em JavaScript, e sem
  navegador eu não passo dessa parede. É o maior bolsão restante e o mais caro de furar.
- **105 domínios não responderam** (DNS morto ou TLS recusado pelo proxy). Marcados `porta-sem-resposta`,
  não como estúdio fechado — não é a mesma coisa.
- **Nenhum captcha foi testado com clique.** Onde escrevi que o HTML não tem marca de captcha, o veredito
  ainda depende do clique — o desafio costuma carregar só depois do Submit.
- **A Oceania e as vagas de Workday não foram tocadas.**

---

## 10. RESUMO EM UMA LINHA

De 1.664 linhas triadas em 21 países, **12 vagas vivas da disciplina** com o texto inteiro lido,
das quais **8 já eram conhecidas** e **1 é requisição nova, sem veto e ainda intocada**:
**Senior 3D Character Artist da Snowprint Studios, Estocolmo, publicada hoje**.
A segunda melhor porta é a **Lead Material & Texture Artist da Gaijin**, que já está no painel como
pendente e que **oferece realocação para sete países** — isso o painel não sabia.
