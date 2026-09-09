# Caça por RECÊNCIA nas famílias Workday e Greenhouse — 09/09/2026, noite

**Método:** ordenar por **data de publicação** e ler o **corpo** dos anúncios dos últimos 4 dias,
em vez de filtrar por palavra-chave de título. Só `curl` + `python3`. **Nenhum navegador aberto,
nenhum Playwright, nenhum `hb_run.sh`, nenhum commit, nenhum push.** `docs/index.html`,
`enviados.csv`, `automacao/processados.csv` e `automacao/FILA-DO-VINI.md` foram **lidos e nunca
tocados**. Este arquivo é o único que nasceu na rodada.

---

## PLACAR, antes da narrativa

| Medida | Número |
|---|---|
| Slugs de quadro Greenhouse testados pela API | **658** |
| **Quadros Greenhouse vivos (HTTP 200)** | **63** |
| — quadros vivos que o repositório **não conhecia** | **19** |
| Vagas Greenhouse lidas (listagem integral dos 63) | **2.093** |
| **Publicadas (`first_published`) em 05/09 ou depois** | **75** |
| Corpos Greenhouse recentes lidos por inteiro | **72** |
| Quadros Workday paginados 100% | **14** |
| Vagas Workday lidas | **2.788** |
| **Postadas nos últimos 4 dias (`postedOn` ≤ 4d)** | **321** |
| Corpos Workday recentes lidos por inteiro (após corte de escopo) | **273** |
| Sondagens de locatário Workday da regra 14 (15 nomes × 15 pods) | **225**, todas `422` |
| **Da disciplina, no escopo, sem veto e inéditas** | **1** |
| Da disciplina que o **dedupe matou** | **1** (e era a melhor da noite) |
| Da disciplina descartadas com motivo escrito | **5** |

**A fila tem UMA linha.** Não inflei. O achado mais importante da noite não é uma vaga: é a
**armadilha de recência do Workday** descrita na §4, que quase produziu a quinta reaplicação da
campanha na mesma requisição.

---

# 1. A FILA — uma linha

### 1. Mob Entertainment — Senior Hard Surface Artist

**Estúdio:** Mob Entertainment (*Poppy Playtime*) · **Título exato:** `Senior Hard Surface Artist`
**ID de requisição:** `5233607007` · **`internal_job_id`: `4679041007`**
**Cidade/País:** *United States* — o anúncio termina com **`#LI-Remote`**, ou seja remoto nos EUA
**Família:** Greenhouse

**URL de candidatura, com código medido nesta rodada:**

| URL | HTTP medido |
|---|---|
| `https://job-boards.greenhouse.io/mobentertainment/jobs/5233607007` | **200** |
| `https://boards.greenhouse.io/embed/job_app?for=mobentertainment&token=5233607007` | **301 → 200** em `https://job-boards.greenhouse.io/embed/job_app?for=mobentertainment&token=5233607007` |
| `https://boards-api.greenhouse.io/v1/boards/mobentertainment/jobs/5233607007` (corpo integral) | **200** |

**Data de publicação:** **`first_published` = 2026-09-09T13:09:34-04:00** — publicada **hoje**,
e `updated_at` é o mesmo carimbo, ou seja não é republicação de requisição velha.

**Régua de vinte termos, rodada sobre o anúncio INTEGRAL — 3 acertos, os TRÊS falsos positivos
já catalogados. Frases literais:**

- `eligib` → *"Mob Entertainment offers the following benefits to all **eligible** U.S.-based
  full-time employees: profit sharing; medical, dental, and vision insurance; 401(k) matching…"*
  → **elegibilidade de BENEFÍCIO**, falso positivo catalogado.
- `within the` → *"Final compensation **within the** applicable salary range will be determined
  based on factors such as the applicant's experience, qualifications, and work location."*
  → falso positivo catalogado.
- exigência de idioma local → **acerto só na palavra "polish"** dentro de
  *"Conduct regular **polish** passes to ensure visual consistency"*. É polimento de arte, não
  idioma polonês. Falso positivo.
- **Não aparecem:** `authoriz`, `sponsor`, `work permit`, `must be based`, `based in`, `only from`,
  `LMIA`, `days a week`, `days per week`, `days in the office`, `resident`, `relocat`,
  `located in`, `unable to support`, `no relocation`, `x a week`, `x per week`, `only`.
  **Veto escrito: ZERO.**

**Dedupe por ID de requisição, arquivo por arquivo, lendo até o fim de cada célula:**

| Arquivo | `5233607007` | `4679041007` |
|---|---|---|
| `enviados.csv` | **0** | **0** |
| `automacao/processados.csv` | **0** | **0** |
| `docs/index.html` | **0** | **0** |
| `automacao/FILA-DO-VINI.md` | **0** | **0** |

Teste barato rodado além da contagem: `grep "5233607007/confirmation"` → **nada**;
`grep` de `ENVIADA` na vizinhança do ID → **nada**. **Nunca foi enviada.**

**Checagem do `internal_job_id` contra as outras requisições da mesma casa** (a armadilha da Epic):
o quadro `mobentertainment` tem 14 vagas e os internos são todos distintos. As duas que a campanha
já enviou são `5207518007`/interno `4666360007` (Senior Character Artist) e `5195729007`/interno
`4660644007` (Senior Environment Artist). **`4679041007` não colide com nenhuma delas.** É
requisição nova de verdade, não a mesma vaga republicada.

**Veredito de disciplina, com citação do corpo:** *"Design and build detailed and highly realistic
interactive props, weapons, and objects"*; *"Own full process including **blockout, high poly, and
final textured game-ready models**"*; *"Strong portfolio demonstrating mastery of hard surface
interactive props, **modeling and texturing**"*; *"High proficiency in industry-standard tools
(e.g., **Maya, Blender, ZBrush, Substance Designer/Painter**, Photoshop)"*; *"Contribute to larger
scale **environments**, building architecture, structures, and other assets to support
**environment art** needs"*. É **modelagem hard surface + texturização + arte de ambiente**, com o
ferramental exato dele. Centro do portfólio, não borda.

**Faixa salarial publicada** (o anúncio publica três faixas por região):
- São Francisco / Nova York / LA / Seattle / Boston / DC: **US$ 110.000 – 140.000/ano**
- Austin / Denver / Nashville / Atlanta / Chicago / Dallas / Miami: **US$ 96.000 – 120.000**
- **Demais localidades dos EUA: US$ 82.000 – 102.000**

**Ressalva honesta, e ela é grande — leia antes de clicar:**
1. **Esta seria a TERCEIRA candidatura na Mob Entertainment.** A campanha mandou a **Senior
   Character Artist `5207518007` em 02/09** (confirmada pelo Greenhouse: *"Thank you for
   applying"*) e a **Senior Environment Artist `5195729007` em 07/09** (`processados.csv`:
   *"ENVIADA E CONFIRMADA — Senior Environment Artist remota EUA — URL /confirmation mais Thank you
   for applying"*). **Nenhuma das duas teve resposta até agora.** A casa **não recusou** — é
   silêncio, não porta fechada, e é diferente do caso Swaybox. Mas é a terceira porta na mesma
   casa em oito dias. **Decisão sua.** Se for, eu escreveria a carta reconhecendo as anteriores.
2. **Mob NÃO está na lista de casas de cadência ocupada hoje** (09/09). Não há trava de ritmo.
3. **Vaga dos EUA e ele precisa de patrocínio.** Isso é **contexto, não veto** — o anúncio não
   escreve uma linha sobre autorização de trabalho. Mas as três faixas salariais são amarradas a
   "work location" nos EUA, e a linha de benefícios diz *"U.S.-based full-time employees"*. Vale
   pretensão pela faixa de **"All Other U.S. Locations"** se ele for responder remoto.
4. **Encaixe:** é hard surface de props/armas para jogo de horror em Unreal 5, com pedido explícito
   de *"realistic, high quality game art"*. O centro dele é estilizado. O anúncio pede realismo
   com todas as letras. **Não é veto, é ressalva de registro.**

---

# 2. O DEDUPE MATOU A MELHOR DA NOITE — e é a lição da rodada

### Disney / ILM Londres — `Senior Texture Artist - ILM London` — `10159370` — **NÃO CLICAR**

Esta vaga **passou em tudo** e é de casa da **regra 14**:

- **Família:** Workday · locatário `disney`, pod `wd5`, **site `disneycareer`** (ela **não** aparece
  no `disneycareerdc`) · Londres, Reino Unido
- `POST .../wday/cxs/disney/disneycareer/jobs` a lista com **`postedOn` = "Posted 2 Days Ago"**;
  detalhe `GET .../wday/cxs/disney/disneycareer/job/London-United-Kingdom/Senior-Texture-Artist----ILM-London_10159370`
  → **HTTP 200**; `startDate` da API = **2026-09-07**
- **Disciplina perfeita:** *"Develop high-quality **textures** for **digital doubles, creatures, and
  hard surface assets**, with a strong focus on surface realism"*; *"Collaborate closely with Show
  supervision, **Modelers**, and **Look-Development TDs**"*; *"Strong production experience using
  **Mari**"*; *"Working knowledge of **UV mapping** principles"*; *"Experience with **Substance
  Designer and/or Painter**"*. Textura/surfacing puro.
- **Régua de vinte termos: ZERO acertos literais.** Nem a cláusula de híbrido casa, porque ela está
  escrita como *"required to work a minimum of 2 days on-site **per week**"* e o termo da régua é
  `days per week` — **a régua não pega "days on-site per week", e isso é um buraco da régua que vale
  anotar.** De qualquer forma seria falso positivo de presença.

**E MESMO ASSIM ELA ESTÁ MORTA. O dedupe por ID pegou, arquivo por arquivo:**

| Arquivo | ocorrências de `10159370` |
|---|---|
| `enviados.csv` | **1** |
| `automacao/processados.csv` | **13** |
| `docs/index.html` | **3** |
| `automacao/FILA-DO-VINI.md` | 0 |

Frases literais, lidas até o fim da célula:

- `enviados.csv`: *"2026-09-02,Disney / ILM London,Senior Texture Artist - ILM London (10159370),
  Reino Unido (Londres),portal,…,**enviada**,… candidatura enviada pelo Workday da Disney com status
  **Application Received** … **RECUSADA em 03/09**"*
- `processados.csv`: *"09-03,Walt Disney Company (ILM London),disney@myworkday.com,…,**recusado**,
  'Senior Texture Artist ILM London 10159370: **the team is considering other candidates whose
  background more closely align**'"*
- `docs/index.html`: *"a Senior Texture Artist ILM London (10159370), publicada ontem, também já foi
  enviada e recusada. As duas requisições da ILM Londres estão esgotadas."*

**Enviada em 02/09, recusada em 03/09.** A irmã `10159371` (Lead Texture Artist) foi enviada em
31/08 e recusada em 01/09. **As duas de textura da ILM Londres estão esgotadas.**

---

# 3. AS OUTRAS QUE APARECERAM POR RECÊNCIA E CAÍRAM, COM MOTIVO ESCRITO

| Casa / vaga | ID | Publicada | Motivo, com citação |
|---|---|---|---|
| **Disney / ILM Londres — FaceSwap Artist, all levels** | `10160278` | 08/09 | **JÁ REGISTRADA E ADIADA HOJE** com dois motivos escritos. `processados.csv` traz 3 ocorrências: *"A única novidade do dia continua sendo a FaceSwap Artist 10160278, já registrada e adiada com os dois motivos escritos."* Não é achado meu; confirmo que continua viva no quadro. |
| **Disney / ILM Vancouver — CG Technology Supervisor** | `10160228` | 08/09 | **FORA DA DISCIPLINA.** Corpo: *"oversee the development, implementation, and communication of **best practices for the execution of CG techniques and workflows**"*, *"act as **product owner** for key development projects"*, *"Represent the local studio priorities at the global level for **technology and workflow planning**"*. É supervisão de **pipeline e tecnologia**, não produção de modelo/textura. Cai pela exclusão de arte técnica. |
| **Disney / ILM Vancouver — Jr Lighting Technical Director** | `10124854` | 08/09 | **FORA DA DISCIPLINA E DO NÍVEL.** É **iluminação/TD** (Katana, Nuke, shader) e é **Jr**. |
| **Disney / ESPN — Sr Technical Director** | `10159739` | 08/09 | **FORA DA DISCIPLINA.** Casa da regra 14, mas é **switcher de transmissão ao vivo da ESPN**: *"operating video switchers, implementing sources… Expert level operation of all broadcast equipment"*. Nada de 3D. |
| **Disney / Lucasfilm Animation — Storyboard Artist (PH)** | `10157624` | 09/09 | **FORA DA DISCIPLINA:** storyboard é desenho 2D. (Publicada nos DOIS sites: `disneycareer` como `…_10157624` e `disneycareerdc` como `…_10157624-1` — **mesma requisição, dois anúncios**, exatamente a armadilha da regra 7 no Workday.) |
| **Disney / ILM Mumbai — Environment Supervisor** | `10146395` | 06/09 | **FORA DO ESCOPO.** Índia. |
| **Cloud Imperium Games — Senior Character Concept Artist / Artiste Concept Personnage Senior** | `JR101414` | **09/09** | Dedupe **limpo 0/0/0/0**, Montreal está no escopo, e o corpo é bem mais 3D do que o título sugere: *"proficient in Photoshop, **ZBrush**, and **Keyshot**"*, *"notable experience with **Substance Painter and Marvelous Designer**"*, *"Excel at creating **organic textures** … and **hard surfaces** (e.g., armor, accessories)"*, *"strong understanding of human **anatomy**"*. **E mesmo assim NÃO entra, por dois motivos:** (a) a entrega é **concept** — *"bring ideas to life, from initial research to **the final image**"*, e conceito está na lista de exclusão; (b) **régua: 1 acerto de idioma local** — *"Can effectively collaborate and communicate in a **bilingual** environment"* / *"communiquer efficacement dans un environnement **bilingue**"*, em Montreal. O aviso de topo diz que **inglês** é obrigatório, o que joga a favor, mas "ambiente bilíngue" é exigência escrita. **Fica registrada, decisão sua se quiser forçar.** |
| **Scopely — Senior Art Manager** | `5409477008` | 09/09 | Barcelona está no escopo, dedupe limpo, mas **fora da disciplina**: *"This role is **primarily focused on people management**, team development, performance, staffing"*, *"its primary responsibility is the **success, wellbeing, and development** of the art team"*. É gestão de pessoas, não produção de arte. |
| **Scopely — 2D Artist** e **Senior Animator / VFX Artist (MONOPOLY GO!)** | `5409498008` · `5396210008` | 09/09 e 08/09 | **FORA DA DISCIPLINA:** 2D e animação/VFX. |
| **Fanatics Collectibles — Art Director, Londres** | `4397677009` | 08/09 | **JÁ DESCARTADA POR ESCRITO** em `automacao/caca-painel-familias.md`: direção de arte **gráfica** de carta colecionável. Confirmo que é a mesma requisição. |
| **Sony Interactive — Video Game Capture Artist (Remote e Onsite)** | `6178395004` · `6178391004` | 09/09 | **FORA DA DISCIPLINA:** captura de imagem de gameplay, não modelagem. E a casa Sony já foi usada hoje. |
| **Mob Entertainment — Senior Technical Animator** e **Contract Game Animator** | `5233450007` · `5232043007` | 09/09 e 08/09 | **FORA DA DISCIPLINA:** animação e arte técnica. |
| **Gearbox — Level Designer** | `7985481003` | 03/09 | Fora da janela de recência **e** fora da disciplina. Fica o registro de que o quadro `gearbox` do Greenhouse **existe e está vivo** — não estava no censo. |

---

# 4. O QUE ESTA RODADA MEDIU DE MÉTODO, e vale mais que a fila

**1. `postedOn` do Workday NÃO é data de publicação. Ele se rearma.**
A `10159370` aparece hoje como **"Posted 2 Days Ago"** e com `startDate` **2026-09-07** na API —
parece publicada em 07/09. **Mas o próprio corpo do anúncio traz, no rodapé, `Date Posted:
2026-08-26`**, e o registro da campanha prova candidatura enviada em **02/09** e recusa em **03/09**.
Ou seja: **o Workday reempurra requisições antigas para o topo da lista de recência.** Ordenar por
`postedOn` acha coisas que o filtro de título perde — que é o ponto da tarefa e funcionou — **mas
não substitui o dedupe por ID em hipótese alguma.** Esta teria sido a **quinta** reaplicação da
campanha na mesma requisição por causa de identificador enganoso; `processados.csv` já registra
*"Quarta vez que a campanha quase reaplica na mesma requisicao por causa de id de URL diferente do
id do ATS"*. **Regra que fica: no Workday, cruze SEMPRE `postedOn` com o `Date Posted:` escrito no
corpo, e só então rode o dedupe.**

**2. No Greenhouse, o campo certo de recência é `first_published`, não `updated_at`.**
Medido: filtrando por `updated_at ≥ 05/09` saem **499** vagas dos 63 quadros; filtrando por
`first_published ≥ 05/09` saem **75**. As 424 de diferença são varredura administrativa em massa
(a Roblox sozinha reeditou dezenas de requisições de julho hoje). `updated_at` produz ruído numa
proporção de 6 para 1. **E `first_published` já vem na listagem barata `/jobs`, sem `content=true`
— não precisa baixar corpo para ordenar por recência.**

**3. Buraco medido na régua de vinte termos.** O anúncio da ILM Londres diz *"a minimum of 2 days
on-site **per week**"* e a régua **não casa**, porque procura `days per week` colado. Um anúncio
que escreva a cláusula de presença assim passa invisível. Não muda veredito nenhum desta rodada
(seria falso positivo de qualquer jeito), mas quem for endurecer a régua deveria usar
`days?.{0,20}per week` e `days?.{0,20}a week` em vez de literal.

**4. A regra 14 está esgotada no Workday, e agora com número.** Sondei **15 nomes de locatário**
(`paramount`, `paramountglobal`, `dreamworks`, `nbcuni`, `nbcuniversal`, `wbd`, `lucasfilm`, `ilm`,
`marvel`, `espn`, `hulu`, `abc`, `20thcentury`, `searchlight`, `pixaranimation`) contra os **15 pods
reais** = **225 sondagens, todas `422`**. Esses nomes **não têm locatário Workday**. As casas da
regra 14 que existem no Workday são exatamente três e todas já estavam mapeadas: **`disney`/wd5**
(só dois sites: `disneycareer` e `disneycareerdc` — o `robots.txt` confirma, não há terceiro),
**`warnerbros`/wd5** e **`pixar`/wd501**.

**5. Pixar e Warner estão secas de arte, e agora está medido nesta janela.**
`pixar`/`Pixar_External_Career_Site` tem **3 vagas no total** (chef de plantão, engenheiro de dados,
cientista de pesquisa) e `Pixar_External_Tech_Jobs` tem **1**. **Zero publicadas nos últimos 4
dias.** `warnerbros`/`global` tem **334 vagas**, **39 nos últimos 4 dias**, e li o corpo de todas as
que estão no escopo geográfico: **zero de arte 3D** — é CNN, TNT Sports, ESPN de Atlanta, engenharia
de produto e marketing. Os acertos de `mari` e `rig` nos corpos da Warner são a cláusula de EEO
(*"**mari**tal status"*) e a palavra *"**rig**hts"*. **Falso positivo de substring, anote.**

**6. Dezenove quadros Greenhouse novos entraram no mapa, e nenhum rendeu.** Os que o repositório não
conhecia e que respondem 200: `riotgames`, `rockstargames`, `nintendo`, `discord`, `nix`,
`wildlifestudios`, `tangogameworks`, `laika`, `remedy`, `bethesda`, `mediatonic`, `gearbox`,
`liftoff`, `motive`, `teravision`, `ghost`, `sunrise`, `foundry`, `nexus`, `metacore`.
**Cinco deles são falsos amigos e valem registro para ninguém repetir:**
- **`nix`** = **N-iX**, consultoria de TI ucraniana. 135 vagas, todas engenharia, e a maioria em
  LATAM/Ucrânia. A palavra "groom" nos anúncios dela é **"backlog grooming"** de Scrum.
- **`remedy`** = **farmácia de manipulação em Houston, Texas** — *"Quality & Compliance Manager –
  Compounding Pharmacy"*. **NÃO é a Remedy Entertainment** de Espoo.
- **`ghost`** = marca de suplemento em Los Angeles (*"Livestream Host"*). **Não é Ghost VFX.**
- **`sunrise`** = **Sunrise Management**, administradora de condomínios da Califórnia. As "vagas" que
  batem em busca são *Maintenance Supervisor*. **Não é a Sunrise de animação.**
- **`nexus`** = **CGS Nexus**, suporte técnico de BPO. **Não é o Nexus Studios de Londres.**
- **`motive`** = agência de publicidade de Denver. **Não é o Motive Studio da EA.**
- **`teravision`** = Teravision Technologies, desenvolvimento web remoto (Colômbia).
- **`foundry`** = uma empresa de mídia de Nova York, **não a Foundry** do Nuke/Mari.
- **`liftoff`** = Liftoff Mobile, adtech.

**7. Não existe endpoint global de recência no Greenhouse.** A única forma de ordenar por data é
paginar quadro a quadro. Foi o que fiz nos 63. **Se a campanha quiser recência de verdade como
rotina, o caminho barato é guardar o `first_published` máximo por quadro e reconsultar só a
listagem `/jobs` (sem `content=true`) — 63 requisições, alguns segundos.**

---

# 5. O QUE VARRI, PARA NINGUÉM REPETIR

**Greenhouse — 63 quadros vivos, listagem integral lida.** Além dos 44 que o repositório já
conhecia: os 19 da §4.6. Os quadros vivos com **zero vaga publicada nos últimos 4 dias**:
`sonypicturesimageworks` (52 vagas), `sonypicturesanimation` (2), `loonshotgames` (23),
`bluehole` (16), `naughtydog` (14), `krafton` (60, a única recente é PM de marketing coreano),
`cloudchamberen` (22), `swayboxstudios` (11), `teamlfg` (10), `highdive` (9), `insomniac` (6),
`ncamerica` (6), `eleventhhourgames` (6), `atomiccartoons` (5), `brandnewschool` (5),
`digitalextremes` (5), `laika` (5), `bungie` (3), `housemarque` (3), `tangogameworks` (14),
`wildlifestudios` (18), `goodjobgames` (31), `digitaleclipse`, `havenenglish`, `nmcareers`,
`unknownworlds`, `crystaldynamics`, `firesprite`, `jamfilled`, `playq`, `studiokraftonboard`,
`tripwireinteractive`. **Vazios (0 vagas):** `blurstudio`, `gravitywell`, `hbstudios`,
`monomipark`, `mediatonic`, `metacore`.

**Workday — 14 quadros paginados 100%:** `disney`/`disneycareer` (635), `disney`/`disneycareerdc`
(651), `warnerbros`/`global` (334), `netflix`/`Netflix` (657), `netflix`/`Eyeline` (46),
`pixar`/`Pixar_External_Career_Site` (3), `pixar`/`Pixar_External_Tech_Jobs` (1),
`cloudimperiumgames`/`CIG_Global_Careers` (56), `sega`/`SEGA_Careers` (28), `unitytech`/`Unity`
(124), `aristocrat`/`AristocratExternalCareersSite` (179), `spinmaster`/`SpinMaster_Careers` (54),
`spinmaster`/`TocaBoca_Careers` (1), `starz`/`Starz` (19).

Recência nesses, medida: **Netflix tem 35 vagas dos últimos 4 dias e nenhuma é de arte** — são
engenharia, ads, vendas e a única de estúdio é *Front-End Developer - Netflix Animation Studios*
`JR42454` em Vancouver, que é programação. **Eyeline tem 1** (*Project Manager, Innovation*).
**Aristocrat tem 5**, todas de vendas/técnico de campo. **Unity tem 36**, todas engenharia — os
acertos de `shader`/`texture` são as três vagas de *Graphics Engineer*, que são **programação de
renderização**, não arte. **Spin Master tem 6**: *Product Designer* (Wilton, CT) e *Senior Designer*
(Hong Kong, fora do escopo) — design industrial de brinquedo, sem 3D no corpo. **Starz, Pixar e
Toca Boca: zero recentes.**

**Não varri, e digo por quê:** `nvidia`/`NVIDIAExternalCareerSite`, `adobe`, `autodesk`, `intel`,
`fox` (4 sites), `cae`, `draftkings`, `deluxe`, `sds`. O lote 2 de 09/09 leu **6.067 vagas** desses
quadros e mediu **zero da disciplina**, e catalogou que "modeling"/"characterization" ali é
**engenharia de semicondutor**, não arte. Repetir isso hoje seria gastar rodada em terreno já
medido. Se você quiser cobertura formal, é um comando e uns minutos — só diga.

---

# 6. LEITURA HONESTA

**A hipótese da tarefa se confirmou em parte, e o número é claro.** Ordenar por data de publicação
**funciona**: ela trouxe à tona a `Senior Texture Artist` da ILM Londres, cujo título tem termo de
disciplina mas que um filtro de título rodado hoje também acharia — e trouxe a **Senior Hard Surface
Artist da Mob**, publicada hoje às 13h09, que **nenhuma varredura anterior podia ter visto porque
ela não existia**. O que a recência **não** faz é criar vaga: em 396 anúncios publicados nos últimos
quatro dias nas duas famílias inteiras (75 no Greenhouse + 321 no Workday), **o mundo produziu duas
vagas da disciplina dele no escopo**, e uma delas já tinha sido enviada e recusada há uma semana.

**A dor da rodada:** a melhor vaga da noite — casa da regra 14, disciplina exata, régua zero, Londres
— estava morta há seis dias, e só o dedupe por ID revelou isso, porque o `postedOn` do Workday
mentia com cara de verdade. **Se eu tivesse confiado na recência sem o dedupe, você teria clicado
numa requisição que já te recusou.**

**O que eu NÃO fiz:** não abri navegador, não usei Playwright nem `hb_run.sh`, não commitei, não fiz
push, não mandei email, não preenchi formulário nenhum, e não toquei em `docs/index.html`,
`enviados.csv`, `automacao/processados.csv` nem `automacao/FILA-DO-VINI.md`.
