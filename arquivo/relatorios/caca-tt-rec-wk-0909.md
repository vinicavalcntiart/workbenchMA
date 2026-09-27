# CAÇA TEAMTAILOR · RECRUITEE · WORKABLE · PERSONIO — 09/09

**Método:** só `curl`. Nenhum navegador, nenhum Playwright, nenhum `hb_run.sh`.
**Nada commitado, nada empurrado.** `docs/index.html`, `enviados.csv`, `automacao/processados.csv` e
`automacao/FILA-DO-VINI.md` foram **lidos e não tocados**. Este arquivo é o único criado.

---

## 0. O NÚMERO, ANTES DA FILA

| Etapa | Valor |
|---|---|
| Nomes de estúdio extraídos (`STUDIOS` + `PORTAIS` do painel + `alvos.csv`) | 1.629 |
| Variantes de slug geradas | **3.381** |
| Sondagens disparadas (Recruitee + Teamtailor + Personio, 1 por slug) | **10.143** |
| Consultas ao índice de busca do Workable (19 termos × até 4 páginas) | 62 |
| **Quadros vivos medidos** | **137** (20 Recruitee · 71 Teamtailor · 46 Personio) |
| Vagas lidas nesses quadros | 189 + 325 + 931 = **1.445** |
| Vagas únicas colhidas no índice do Workable | **540** |
| Batem a disciplina **pelo título** | 26 (TT) + 2 (Rec) + 0 (Personio) + 82 (Workable) = **110** |
| Sobreviveram ao recorte geográfico | 96 |
| **Sobreviveram ao dedupe por ID de requisição** | **5** |
| **Sobreviveram à régua de vinte termos** | **3** |
| **FILA FINAL** | **3 linhas** (1 delas com cadência ocupada hoje) |

**Três linhas.** Duas em casas que nunca receberam candidatura por portal, uma numa casa que já
recebeu hoje e por isso vai marcada. O rendimento é baixo de propósito: o dedupe derrubou 5 vagas que
pareciam novas e a régua derrubou 2 com veto escrito literal.

---

# FILA PRONTA

---

### 1. Sperasoft / AMC Studio — **Lead Props/Environment 3D Artist** — Bucareste, Romênia

**Família:** Workable · **Local:** Bucareste, Romênia · marcado **TELECOMMUTE** no próprio anúncio

**CLIQUE:** https://jobs.workable.com/view/bgM2Eip6fX6RA8zmRDZV2K/remote-lead-props%2Fenvironment-3d-artist-in-bucharest-at-sperasoft
**HTTP medido nesta rodada: 200.**

- **ID da requisição:** uuid `532f4b03-d196-42bf-bb46-72979c256131` · token de anúncio `bgM2Eip6fX6RA8zmRDZV2K`
- **DEDUPE, arquivo por arquivo:**
  - `enviados.csv` — uuid **0**, token **0**, título "Props/Environment" **0**
  - `automacao/processados.csv` — uuid **0**, token **0**, título **0**
  - `docs/index.html` — uuid **0**, token **0**, título **0**
  - `automacao/FILA-DO-VINI.md` — uuid **0**, token **0**, título **0**
  - Teste barato do recibo: `<uuid>/confirmation` **0**, `ENVIADA` colado ao id **0**.
  - **Grep pelo NOME DA CASA, como manda a regra:** `Sperasoft` aparece **2×** em `enviados.csv`,
    5× em `processados.csv`, 10× em `docs/index.html`. **Li todas.** A única linha de envio é
    *"2026-08-26,Sperasoft,jobs@sperasoft.com,Senior Character Artist · Wingfeather Saga credit ·
    stylized + grooming,recusado (respondido; recruiter sugere acompanhar vagas no site)"* — é
    **candidatura por EMAIL, recusada em 26/08**, e **nenhuma candidatura por portal**. O painel
    também guarda um dossiê da *Material Artist (stylization)* da mesma casa, que é **outra
    requisição**. `AMC Studio` — o nome do estúdio que assina este anúncio — **não aparece em nenhum
    dos quatro arquivos**. **Requisição inédita.**
- **RÉGUA DE VINTE TERMOS, texto integral (3.326 caracteres), frase literal de cada acerto:**
  - `based in` — **ACHADO**: *"AMC Studio is a world-leading 3D art and game development studio **based in** Bucharest, Romania, and part of the Keywords Studios international group."* → descreve onde o **ESTÚDIO** fica. **FALSO POSITIVO catalogado.**
  - `within the` — **ACHADO**: *"Manage the distribution of tasks **within the** team and ensure deadlines are met"* → **FALSO POSITIVO catalogado** (`within the team`).
  - Os outros **18 termos: NENHUM.** Sem `authoriz`, `eligib`, `sponsor`, `work permit`,
    `must be based`, `relocat`, `resident`, `located in`, `unable to support`, `days a week`,
    `days per week`, `days in the office`, `LMIA`, `only from`, `no relocation`.
  - **Exigência de idioma local: NENHUMA.** O único requisito é *"Strong **English** communication skills, both written and verbal"*.
  - **VETO ESCRITO: ZERO.**
- **DISCIPLINA — citação do anúncio:** *"set a high quality bar for **props and environment art**"*;
  *"Develop and optimize efficient **modeling and texturing** workflows (**PBR**)"*; *"expert-level
  skill in creating high-quality **hard-surface and organic props**"*; *"Expert knowledge of Maya,
  3ds Max, or Blender, as well as **ZBrush** and the **Substance Suite (Painter/Designer)**"*;
  *"Complete mastery of PBR workflows, **UV optimization, baking, and LOD management**"*; *"Proven
  ability to **switch between different art styles**"* e *"adaptability across art styles - **from
  stylized to photorealistic**"*. **É modelagem + textura/surfacing + ambiente/props, com escultura
  na pilha. Encaixa.**
- **Faixa salarial publicada:** **nenhuma.**
- **RESSALVA HONESTA, três:** (1) é cargo de **LIDERANÇA** — pede *"at least 2 years in a Lead or
  Supervisory role"*; (2) a **mesma requisição tem gêmea em Varsóvia/Polônia**
  (`Lead Props/Environment 3D Artist / Główny Artysta...`) — **é uma vaga só, mande em UMA**;
  (3) a casa **já recusou** a candidatura por email de 26/08 — mas a recusa veio com convite escrito
  para *"acompanhar vagas no site"*, e esta é exatamente uma vaga do site, então a porta está aberta
  por convite e não por teimosia.

---

### 2. Magic Media — **Senior 3D Generalist Artist** — remoto na Polônia (e Espanha, Romênia, Bulgária)

**Família:** Workable · **Local:** **TELECOMMUTE**, anúncio por país

**CLIQUE:** https://jobs.workable.com/view/fETqLf4yCZ6XDqX9KTXYwG/remote-senior-3d-generalist-artist-in-poland-at-magic-media
**HTTP medido nesta rodada: 200.**

- **ID da requisição:** uuid `76cde5c1-4b15-471c-9e2e-358ec9d842fc` · token `fETqLf4yCZ6XDqX9KTXYwG`
- **Publicada em 09/09/2026 às 14h35 UTC — é de HOJE.**
- **DEDUPE, arquivo por arquivo:**
  - `enviados.csv` — uuid **0**, token **0**, título `3D Generalist Artist` **0**, `Magic Media` **0**
  - `automacao/processados.csv` — uuid **0**, token **0**, título **0**, `Magic Media` **0**
  - `docs/index.html` — uuid **0**, token **0**, título **0**, `Magic Media` **1**
  - `automacao/FILA-DO-VINI.md` — uuid **0**, token **0**, título **0**, `Magic Media` **0**
  - **Li a ocorrência única até o fim da célula**, e ela é um **veredito vencido**, não um recibo:
    *"Magic Media","Chipre","https://careers.magicmedia.studio/","portal","Vagas permanentemente
    remotas. **SEM VAGAS (verificado 02/09)**: a listagem oficial mostra só GameMaker Developer, dois
    Senior Game Producer e Senior Real-time VFX Artist; nada de character ou 3D, e
    careers.magicmedia.studio não abriu"*. Nenhum `/confirmation`, nenhum `ENVIADA`. **A casa nunca
    recebeu nada e o "sem vagas" de 02/09 caducou: as requisições de arte 3D entraram depois.**
- **RÉGUA DE VINTE TERMOS, texto integral (3.573 caracteres):**
  - `within the` — **ACHADO**: *"We work with leading developers and publishers **within the** games and tech industry"* → **FALSO POSITIVO catalogado** (`within the industry`).
  - Os outros **19 termos: NENHUM.** Sem `authoriz`, `eligib`, `sponsor`, `work permit`,
    `must be based`, `based in`, `relocat`, `resident`, `located in`, `unable to support`,
    `days a week`, `days per week`, `days in the office`, `LMIA`, `only from`, `only`, `no relocation`.
  - **Exigência de idioma local: NENHUMA.**
  - **VETO ESCRITO: ZERO.**
- **DISCIPLINA — citação do anúncio:** *"you will be responsible for the creation of different types
  of assets such as **characters or environment props**"*; *"Generate high quality models (both
  **hard surface and organic**) and **textures** from concepts and photos"*; *"extensive and
  demonstrable experience creating any kind of 3D asset **in different styles and pipelines**"*;
  *"Serve as a **mentor** to more junior environment artists"*; *"Knowledge of the standard 3D
  packages, 3Ds max, Maya, Blender"*. **Personagem + ambiente + modelagem + textura. Encaixa, e o
  pedido de "different styles" é o registro dele.**
- **Faixa salarial publicada:** **nenhuma.**
- **RESSALVA HONESTA, três:** (1) **é generalista, não personagem puro** — o anúncio põe personagem e
  props de ambiente na mesma frase, então é encaixe largo e não cravado; (2) a **mesma requisição está
  anunciada em 6 países** (Polônia, Espanha, Romênia, Bulgária, Ucrânia, Sérvia) — pela regra de
  requisição repetida em vários locais, **é UMA vaga, mande em UMA**, e escolhi a da Polônia por ser
  UE; as versões da **Ucrânia e Sérvia estão fora do recorte** e não devem receber envio; (3) existe
  no mesmo quadro a **Middle 3D Generalist Artist** (Itália, Chéquia, Portugal, Hungria) — é
  **nível abaixo do dele** e fica registrada, não recomendada.

---

### 3. beffio — **3D Artist (Mid-Senior)** — requisição `1471127` — **CADÊNCIA OCUPADA HOJE**

**Família:** Teamtailor · **Local:** Poznań, Polônia — **Fully Remote** · **Permanente**

**CLIQUE:** https://careers.beffio.com/jobs/1471127-3d-artist-mid-senior/applications/new
**HTTP medido nesta rodada: 200.** (o anúncio, sem `/applications/new`, também **200**)

- **ID da requisição: `1471127`.**
- **⚠️ CADÊNCIA OCUPADA HOJE.** A beffio **já recebeu candidatura em 09/09**: a *Lead 3D Artist /
  Environment / World Building / Unity3D* `6653367` saiu às **00h29–00h30 UTC**, com recibo em
  `enviados.csv`. Esta é a **quinta** candidatura na casa. **Entra na fila marcada, como manda a
  regra 8 — decisão de disparo é sua.**
- **DEDUPE, arquivo por arquivo — e este deu limpo em TUDO:**
  - `enviados.csv` — **0**
  - `automacao/processados.csv` — **0**
  - `docs/index.html` — **0**
  - `automacao/FILA-DO-VINI.md` — **0**
  - Teste barato do recibo: `1471127/confirmation` **0** · `ENVIADA` colado ao id **0**.
  - **Grep pelo nome da casa:** a beffio é casa familiar e aparece dezenas de vezes; **li as
    entradas**. O painel registra **quatro** candidaturas (`6217989`, `7242656`, `6984394`,
    `6653367`) e a auditoria de 09/09 no Connect confirma **quatro**. A varredura de Teamtailor de
    09/09 registrada em `processados.csv` diz, literalmente, *"beffio as cinco"* — e as cinco
    listadas ali **não incluem a `1471127`**. **Esta é a sexta requisição do quadro e ninguém a
    tinha listado.**
- **RÉGUA DE VINTE TERMOS, texto integral (5.859 caracteres, tirado do JSON-LD da página):**
  **NENHUM DOS VINTE APARECE.** Sem `authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`,
  `based in`, `only from`, `LMIA`, `days a week`, `days per week`, `days in the office`, `resident`,
  `relocat`, `located in`, `unable to support`, `no relocation`, `within the`, `only`.
  **Exigência de idioma local: NENHUMA** — o único requisito é *"Excellent verbal and written
  communication skills in **English**"*. **VETO ESCRITO: ZERO.**
- **DISCIPLINA — citação do anúncio:** *"creating high-quality 3D art assets in both realistic and
  stylized styles, including **props, hard surface models, foliage, vehicles, weapons, and
  environment elements**"*; *"**Expertise in hard surface and organic modeling**"*; *"**Excellent
  skills in texturing materials using Substance Designer and Substance Painter**"*; *"Strong skills
  in creating both **procedural and handmade materials**"*; *"Proficiency in achieving believable
  **physically based rendering (PBR)** materials"*; *"**Artistic Versatility:** Proven ability to
  work in both **realistic and stylized** art styles is **required**"*; bônus *"**3D Sculpting:**
  Skills in **ZBrush** or Mudbox"*. **Modelagem + textura/surfacing + materiais + ambiente, com
  escultura no bônus. Encaixa direto.**
- **Faixa salarial publicada:** **nenhuma.** O anúncio oferece *"flexible contract options,
  including B2B"* e *"20+ days of paid vacation"*.
- **RESSALVA HONESTA, e são duas sérias:**
  1. **O anúncio é de 05/12/2021 — quase cinco anos no ar.** `datePosted` do JSON-LD:
     `2021-12-05T20:35:17+01:00`. Vaga que fica aberta esse tempo ou é banco de talentos permanente
     ou é anúncio que ninguém fechou. Continua **listada e servida pelo `jobs.json` de hoje** e o
     formulário responde 200, mas não espere urgência.
  2. **RESTRIÇÃO ESTRUTURADA QUE A RÉGUA DE TEXTO NÃO PEGA:** o JSON-LD da própria página declara
     `"applicantLocationRequirements": {"@type":"Country","name":"Poland"}`. **O corpo do anúncio
     não diz isso em lugar nenhum** — ele diz *"Job Type: Permanent / Remote"*, *"Location: Fully
     Remote"* e *"Remote Work: Fully remote position"*. É um campo de metadado publicado pelo
     empregador, então é escrito; mas **não é uma frase do anúncio** e não bate em nenhum dos vinte
     termos. **Eu não descarto por ele** — registro para você decidir, e registro na seção 5 como
     buraco novo da régua.

---

# DESCARTADAS COM MOTIVO ESCRITO

Vagas que passaram título e geografia e que **NÃO devem ser clicadas**. Frase inteira colada.

| Casa / vaga | ID | Motivo |
|---|---|---|
| **Rebellion — Environment Artist** (Oxford / Warwick / Runcorn) | `40BBC5FAFD` | **VETO ESCRITO, e o dedupe por ID tinha dado 0/0/0/0.** O bloco do FIM do anúncio diz: *"**Right to Work Statement** This role is **only** open to applicants who have the **permanent right to work in the UK**. We are **unable to provide or take over visa sponsorship**, either now or in the future. Applicants must therefore be able to demonstrate their ongoing **eligibility** to work in the UK **without the need for employer sponsorship**."* Bate em `only`, `sponsor` e `eligib`. **NÃO APLICAR.** |
| **Rebellion — Senior Character Artist** (Oxford / Warwick) | `331FDD9137` | **DEDUPE PEGOU** e **veto escrito por cima.** `docs/index.html`: *"Rebellion - VETO ESCRITO, NAO APLICAR (…) **RECUSADO em 01/09**"*. Mesma cláusula de Right to Work. Warwick é o **segundo anúncio da mesma requisição**. |
| **Jagex — Environment Artist, RuneScape: Dragonwilds** (Cambridge) | uuid `6bvKsR8EQ2Ka7QgyWP1hua` | **VETO ESCRITO DUPLO.** *"This role is **only** open to applicants who have the permanent right to work in the UK. We are **unable to provide or take over visa sponsorship** for this position, either now or in the future."* E ainda: *"candidates **must be based** (or be willing to **relocate**) within a comfortable commuting distance of our Cambridge office"*. Bate em `only`, `sponsor`, `eligib`, `must be based` e `relocat`. **NÃO APLICAR.** |
| **Framestore — 3D Modeller (Short term contract)** (Montréal) | `2120070` | **DEDUPE PEGOU, e tem DUAS entradas no painel.** `docs/index.html` registra a mesma oferta duas vezes, com o aviso *"esta MESMA oferta 2120070 tem DUAS entradas no painel (…) E uma vaga so"*, mais *"VERIFICADO 07/09 PELA FATIA CANADA: CONFIRMADA VIVA"* e *"FICA A MAO por hCaptcha de imagem, medido e nao suposto"*. Régua limpa (**zero dos vinte**, zero idioma), mas **não é achado novo**. |
| **Reality Games — 3D Generalist** (Cracóvia) | `1999421` | **DEDUPE PEGOU.** `processados.csv` de 07/09: *"**NAO ENVIADA, barrada pelo CAPTCHA DO RECRUITEE** (…) o botao fica com SPINNER e nao termina (…) captcha-base.recruiteecdn.com com tipo hsw"*. Régua: um acerto, *"This is a full-time, in-office position **based in** the iconic railway station building in Krakow"* — descreve onde o **CARGO** fica, **falso positivo catalogado**. Vaga válida, mas **já tentada e é parede medida**, não linha nova. |
| **Envar Studio — Senior 3D Environment Artist (Fixed term)** (Estocolmo) | `8281404` | **DEDUPE PEGOU.** `processados.csv` e `docs/index.html`: *"**CANDIDATURA ENVIADA E CONFIRMADA NA TELA em 07/09** as 09h07 UTC (…) PROVA TRIPLA: a URL final e /applications/…/thanks"*. **Já foi.** |
| **Airship Interactive — Groom Artist / Character Artist / Environment Artist** (Malvern, rede global) | `8281721` · `8281687` · `8281674` | **DEDUPE PEGOU NAS TRÊS, e as três saíram HOJE.** *"Groom Artist 8281721 enviada as 10h18 e COMPLETADA as 10h25"*; *"Character Artist (…) ENVIADA E CONFIRMADA em 09/09 as 00h22 UTC"*; *"Environment Artist 8281674 enviada as 13h47 e COMPLETADA as 13h52"*. **As três portas do banco da Airship estão cobertas.** |
| **One Of Us — Modeller / Texture Artist / Look Development Artist** (Paris) | uuid `0bb699c6-…` e irmãs | **DEDUPE PEGOU.** Já são o **item nº 40 da `FILA-DO-VINI.md`**, com dossiê campo a campo e a recomendação escrita de *"mandar UMA, a Modeller"*. Régua limpa (**zero dos vinte** nas três). **Não é achado novo — já está na sua fila.** |
| **One Of Us — Senior CFX Artist / Senior Groom TD** (Bengaluru) | — | **FORA DO ESCOPO** (Índia) **e veto escrito**: *"You need to have a current and full **work permit** for the region that you'll be working in."* |
| **Lighthouse Games — Lead Character Artist** (Royal Leamington Spa) | `F7F90250DA` | **DEDUPE PEGOU.** Já é o **item nº 10 da `FILA-DO-VINI.md`**, revalidada em 06/09, com dossiê pronto. |
| **Sperasoft — Material Artist (stylization)** (Bucareste/Cracóvia) | — | **DEDUPE PEGOU.** `processados.csv` de 07/09 registra dossiê campo a campo já escrito para ela em `respostas-formularios.md`. |
| **Sperasoft — Level Artist / Lead Level Artist** (Varsóvia/Bucareste) | — | **DEDUPE PEGOU pelo título:** `Level Artist` aparece **20×** em `processados.csv`, 10× em `docs/index.html` e 3× na `FILA-DO-VINI.md`. Já conhecidas. |
| **Keywords Studios — Environment Artist / Principal Environment Artist (GameSim)** e **Character Artist Hair Specialist (Lakshya)** | vários | Casa **muito** conhecida (47 menções em `docs/index.html`, 15 em `processados.csv`, 3 na `FILA-DO-VINI.md`). A Lakshya é **estúdio na Índia**, fora do recorte por escrito, mesmo com o anúncio marcado remoto no Reino Unido/Canadá. |
| **Side — talent pools 3D Character / 3D Environment / Concept Character** (EU, N.Americas, APAC, MEA) | vários | Casa **massivamente** conhecida (211 menções em `docs/index.html`, 81 em `processados.csv`, 12 na `FILA-DO-VINI.md`). São **bancos de talento** repetidos por cidade, não requisições novas. |
| **Liquid Development — Material Artist Talent Pool** | uuid `dfe6ec01-…` | **DEDUPE PEGOU + veto já registrado:** `processados.csv` 07/09 — *"**VETO ACHADO DENTRO DO FORMULARIO, NAO NO ANUNCIO** (…) O /form oficial mostra TRES obrigatorias que fecham"*. |
| **Bardel Entertainment — 2D Character Layout Artist** (Vancouver) | — | **FORA DA DISCIPLINA:** layout **2D** de série de anime. |
| **Alphatec Spine — Radiologic Technologist, 3D Modeling Tech** (Memphis) | — | **FORA DA DISCIPLINA:** técnico radiologista de dispositivo médico. Acerto de palavra-chave, não de cargo. |
| **Sawhorse Productions — Roblox 3D Artist** (Los Angeles) | — | **DEDUPE PEGOU:** `processados.csv` 07/09 registra dossiê campo a campo já escrito em `respostas-formularios.md`. |
| **Magic Media — Senior 3D Environment Artist** (Rio de Janeiro / Buenos Aires / Kyiv / Belgrado) | vários | **FORA DO ESCOPO.** As versões de Bucareste e Barcelona **estão** no recorte e ficam registradas como segunda porta da casa, atrás da Generalist. |
| **Magic Media — Middle 3D Generalist Artist** (Itália, Chéquia, Portugal, Hungria; também Belarus e Turquia) | vários | **NÍVEL ABAIXO DELE** (Middle). Registrada, não recomendada. As de Belarus e Turquia estão **fora do recorte**. |

---

# QUADROS MEDIDOS SECOS, MORTOS OU FALSOS POSITIVOS

Levantamento, não candidatura — **fecha linha e evita varredura repetida**.

### Recruitee — 20 inquilinos vivos, 189 vagas, **2 da disciplina e as duas já conhecidas**

Vivos e medidos: `11bitstudios` (5) · `dovetailgames` (1) · `framestore` (53) · `huuuge` (7) ·
`realitygames` (31) · `squeezestudio` (2) · `tensquaregames` (9) · `playrix` (0) · `otc` (0) ·
`sandbox` (0) · `storm` (0) · `supercell` (0) · `tab` (0).

**Falsos positivos de slug genérico confirmados no Recruitee** — são **outras empresas**, não estúdios:
`ace`, `bfg`, `bloom`, `dle`, `hmp`, `lss`, `nmbrs`, `redsky`. **Não gaste rodada neles.**

### Teamtailor — 71 quadros vivos, 325 vagas, **26 acertos de título e ZERO requisição nova além da beffio `1471127`**

Quadros com vaga que valem registro: `airshipinteractive` (10, **quadro que não constava da tabela de
102 hostnames de `teamtailor-refeito.md`**), `paradox-interactive` (19), `ilogos` (5), `funcom` (6),
`creepyjar` (1), `careers.castirongames.com` (9 hoje, contra 7 na medição de 08/09).

**Confirmados vazios ou sem nada da disciplina:** `careers.embark-studios.com` (18 vagas, **zero de
arte 3D** — só engenharia, dados e um *2D/Screenshot Artist*), `careers.foolstheory.com` (4),
`jobs.arrowheadgamestudios.com` (5, zero de arte), `careers.adventurepartygames.com` (3, só *open
application*), `careers.aonic.co` (2), `career.geoguessr.com` (3), `cigames` (3), `gameboost` (9,
só programação e *Casual Mobile UI Artist*), `sybo` (5, zero de arte 3D), `twinharbour` (11, zero de
arte 3D), `triband` (8), `starbreeze` (2), `goodbyekansas` (3, só técnico e cinematics),
`blackkitestudios` (6, composição e FX), `wetaworkshop` (4, **fabricação física de props**, não
modelagem digital — falso positivo já catalogado), `hampastudio` (2), `pfx` (8), `playagames` (2),
`fundaygames` (2), `sloclap` (1), `gigglebug` (1), `realtime` (1), `bulkheadinteractive` (6).

**`houseofhow` (6) confirmado outra vez como quadro de DEMONSTRAÇÃO abandonado** — as seis vagas
continuam sendo *Game Changer, Programmer, Key Account Manager, iOS Developer, Social Media Manager,
Intern*. **`funcom` continua sendo só os seis estágios de 2027.** Os dois vereditos de 09/09 de
madrugada se sustentam.

**FALSOS POSITIVOS DE SLUG GENÉRICO NOVOS, medidos e nomeados** — são empresas de outros ramos que
ocupam o slug no Teamtailor, e **nenhuma tem relação com jogos ou VFX**:

| Slug | O que realmente é | Prova (títulos servidos) |
|---|---|---|
| `squeeze` | rede de **massagem** norueguesa | *Massage Therapist in Oslo/Akershus, Bergen, Trondheim, Stavanger…* (10 vagas) |
| `groundcontrol` | manutenção **ferroviária e de terrenos** no Reino Unido | *RRV Operators, Grounds Maintenance Operative, Lead Rotary Driller, Arboricultural Surveyor* (26 vagas) |
| `arc` | **suporte de TI** em Basildon | *1st Line Helpdesk Engineer, Microsoft Purview Consultant* (7 vagas) |
| `spg` | **logística** francesa | *Approvisionneur Cariste F/H - CACES 5* (6 vagas) |
| `juice` | **marketing digital** | *Paid Media Implementation Specialist* (4 vagas) |
| `mob`, `stim`, `unfold`, `antagonist` | diversos, fora do ramo | *Office Manager*, *Principal Engineer (Stim)*, *Produktleder*, *Open sollicitatie* |

**Some-se à lista já registrada** (`career`, `jobs`, `explore`, `system`, `company`, `onyx`,
`recruit`, `artstation`, `parkerschauffeurs`). **`squeeze` é o mais perigoso dos novos**, porque a
campanha tem uma **Squeeze Studio** de verdade no Recruitee (`squeezestudio.recruitee.com`) — o slug
curto no Teamtailor é outra empresa.

### Personio — 46 feeds vivos, 931 entradas, **ZERO da disciplina**

Feeds vivos incluem casas reais do ramo: `trixter` (1, *Speculative Job Application*), `deck13`
(5 — *Lead VFX Artist*, *Senior VFX Artist*, *Principal Game Programmer*, *Senior Producer*, *General
Application*; **VFX em tempo real está fora da disciplina por escrito**), `bongfish` (1, *Open
Application*), `popcore` (9, zero de 3D além de *Motion Designer 2D/3D*), `kaiko`, `circus`,
`spectral`, `feather`, `cosmico`.

**Feeds vivos mas VAZIOS** (inquilino existe, zero posições): `airbornstudios`, `amber`, `daedalic`,
`lighthouse`, `milford`, `bks`. **A Airborn Studios é alvo de trilha A em `alvos.csv` e o feed dela
está vazio — isso é medição, não falta de tentativa.**

**ARMADILHA NOVA E ÚTIL — o Personio semeia CONTEÚDO DE DEMONSTRAÇÃO em conta nova**, exatamente como
o Teamtailor faz. Quatro inquilinos diferentes (`kaiko`, `sandbox`, `boxelware`, `bbg`) devolveram o
**mesmo trio literal**: *"General Application / Initiativbewerbung"*, *"SEO Marketing Manager"* e
*"Social Media (Working Student / Werkstudent)"*. E `100` e `acs` devolveram um **segundo** conjunto
idêntico entre si (*Bewerberpool*, *Fahrer/in*, *Ihre Aufgaben*). **Contar esses feeds como "quadro
com vagas" infla o número e produz lixo.** Some-se ao precedente do `houseofhow` no Teamtailor.

**O zero do Personio se confirma pela segunda rodada seguida**, agora por outro domínio
(`.jobs.personio.de`, contra o `.jobs.personio.com` de madrugada) e com outra lista de slugs.
**Não é rota que valha uma terceira rodada tão cedo.**

---

# AS DUAS PAREDES DE ENVIO, MEDIDAS NESTA RODADA

Isto muda o que "pronta para enviar por automação" quer dizer nestas famílias, e é honesto dizer.

1. **RECRUITEE = hCaptcha DEPOIS do Send.** Medido duas vezes pela campanha e reconfirmado por mim na
   leitura dos recibos: na **Framestore** (*"o captcha do Recruitee só aparece DEPOIS do Send"*) e na
   **Reality Games** (*"a rede mostra captcha-base.recruiteecdn.com com tipo hsw, que e prova de
   trabalho"*). **Nenhuma vaga do Recruitee sai por automação headless.** Sai do seu navegador.
2. **WORKABLE = Cloudflare Turnstile no Submit.** *"o POST /api/v1/jobs/<uuid>/apply devolve **412
   Precondition Failed** com o cabecalho **x-ts: 0**, que e o Cloudflare TURNSTILE faltando"*. As
   duas linhas 1 e 2 desta fila **são do Workable**, então **as duas são de clique seu**, não de
   robô. O anúncio e o `/form` abrem normalmente por `jobs.workable.com`.
3. **TEAMTAILOR passa** — é a única das quatro famílias com envio automatizado provado hoje (Airship
   ×3, beffio, Envar). **Mas o envio NÃO completa sozinho:** cai em
   `/applications/email_verification_needed` e **só vira candidatura depois de abrir o link de
   verificação no email dele**. A linha 3 desta fila depende disso.

**Consequência prática:** a fila de hoje é **1 automatizável (beffio, com cadência ocupada) e 2 de
clique seu (Sperasoft, Magic Media)**. Não vou chamar de automatizável o que eu medi que não é.

---

# BURACOS NOVOS DA RÉGUA DE VINTE TERMOS

Dois, os dois medidos nesta rodada, nenhum arquivo compartilhado alterado.

1. **`must be able to work on site in <cidade>` não casa com nenhum dos vinte.** O anúncio da **Envar
   Studio** (`8281404`) diz, literalmente: *"This is an in house position, and candidates **must be
   able to work on site in Stockholm, Sweden**."* Isso é exigência escrita de presença física e
   **passa em branco** pela régua — `must be based` não casa, `based in` não casa, `resident` não
   casa. É o **mesmo tipo de buraco** que o `4 days in the office per week` da Fatshark já tinha
   exposto. **Sugestão:** acrescentar `on site in`, `on-site in` e `in house position`.
2. **`applicantLocationRequirements` do JSON-LD é veto escrito que não é frase.** A beffio `1471127`
   declara `{"@type":"Country","name":"Poland"}` no JSON-LD **enquanto o corpo do anúncio diz "Fully
   Remote" três vezes**. A régua roda no texto e não olha o metadado. **Sugestão:** ler
   `applicantLocationRequirements` do JSON-LD sempre que houver, e tratá-lo como **ressalva**, não
   como veto automático — é campo que estúdio preenche por descuido de formulário tanto quanto por
   política.

---

# O QUE EU NÃO CONSEGUI MEDIR, DITO SEM MAQUIAGEM

- **`apply.workable.com` me bloqueou por taxa (Cloudflare `error code: 1015`) depois de ~20
  chamadas.** Medi o intervalo: **1 requisição bem-sucedida a cada ~30–40 segundos**, o que torna
  inviável varrer 3.381 slugs por ali. **Contornei pelo índice de busca `jobs.workable.com/api/v1/jobs?query=`,
  que NÃO é limitado** e devolve o anúncio integral — foi de lá que saíram as 540 vagas e as duas
  linhas da fila. **Fica registrado como a rota boa do Workable**, e ela substitui o
  `widget/accounts/<co>` para descoberta.
- **ARMADILHA GRAVE que eu peguei e quase me envenenou:** rodando o `widget/accounts` em paralelo,
  o proxy/CDN **devolveu corpo de OUTRA empresa com HTTP 200**. `10-chambers`, `10-ave`, `10tons` e
  mais seis slugs voltaram todos com `"name":"Cognizant Technology Solutions"`, e `1aa`/`1ap`/`1bs`
  voltaram como `"name":"Workable"`. **Se eu tivesse contado 200 como "quadro existe", teria
  inventado dezenas de quadros.** A defesa que funciona: **conferir que o campo `name` do corpo bate
  com o slug pedido** antes de aceitar a resposta. Só `11-bit-studios` → *"11 bit studios"* passou
  nesse teste.
- **159 dos 230 arquivos** que a sondagem de Teamtailor gravou vieram com corpo não-JSON e foram
  descartados na leitura, não contados como zero — a regra de `teamtailor-refeito.md` §0 foi
  respeitada.
- **Não entrei em nenhuma área Connect** (exige login, e o brief proíbe navegador). As candidaturas
  por dentro do portal não foram reconferidas.
- **Não medi o Recruitee em domínio próprio** (`careers.<estúdio>.com` servindo Recruitee). Sondei só
  `<slug>.recruitee.com`. Pelo precedente da Envar no Teamtailor — quadro que **só** existia em
  domínio próprio — **essa é a rodada que falta**, e ela provavelmente rende.

---

# RESUMO

- **10.143 sondagens** por slug + **62 consultas** ao índice do Workable, **137 quadros vivos**,
  **1.985 vagas lidas**, **só `curl`**.
- **FILA: 3 linhas.** Sperasoft/AMC *Lead Props/Environment 3D Artist* (Bucareste, Workable, 200),
  Magic Media *Senior 3D Generalist Artist* (Polônia remoto, Workable, 200, **publicada hoje**) e
  beffio *3D Artist (Mid-Senior)* `1471127` (Teamtailor, 200, **cadência ocupada hoje**).
- **Dedupe derrubou 5** que passaram título e geografia (Framestore, Reality Games, Envar, Airship ×3,
  One Of Us ×3, Lighthouse, Rebellion Senior Character). **A régua derrubou 2 com veto literal**
  (Rebellion Environment Artist e Jagex Dragonwilds — os dois com a mesma cláusula *"only open to
  applicants who have the permanent right to work in the UK"*).
- **Personio: zero, pela segunda rodada e por outro domínio.** Medido, não presumido.
- **Duas paredes de envio confirmadas:** Recruitee (hCaptcha pós-Send) e Workable (Turnstile, 412
  `x-ts: 0`). **Teamtailor é a única das quatro que a automação atravessa**, e mesmo ela exige o
  clique no link de verificação por email.
- **Dois buracos novos da régua** e **seis falsos positivos de slug genérico novos** ficam escritos.

*Nenhum arquivo compartilhado editado. Sem commit, sem push, sem email, sem formulário, sem
navegador. Só `curl`.*
