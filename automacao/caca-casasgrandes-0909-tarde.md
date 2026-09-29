# Caça às casas grandes — 09/09, tarde

Varredura dos quadros das casas grandes atrás de vaga de arte 3D / personagem / modelagem
**ainda não candidatada**, incluindo requisição publicada nas últimas 48h.

Rodada só com `curl` e leitura de arquivo. Nenhum navegador, nenhum commit, nenhum e-mail.

---

## 1. Os números, sem inflar

| Etapa | Nº |
|---|---|
| Casas grandes sondadas | **28** |
| Quadros vivos encontrados (HTTP 200 com vagas) | **22** |
| Quadros mortos / não resolvidos | **13** |
| Postings lidos (únicos por requisição) | **2.654** |
| Passaram no filtro de **disciplina** | **69** |
| Passaram também no **escopo geográfico** | **59** |
| Passaram também na **régua de veto** | **57** |
| Passaram também no **dedupe por ID de requisição** | **13** |
| Sobraram após o corte de **requisição-espelho / bilíngue** | **9** |
| Sobraram após o **veto de idioma local** (Quebec) | **7** |
| **Na fila, após releitura de disciplina no texto integral** | **6** |

**Seis linhas na fila.** Uma da Disney/ILM (REGRA 14, publicada ontem), duas da 2K/Cloud Chamber
e três da Ubisoft.

Composição dos 2.654 postings: 1.314 únicos no Workday (137 chamadas paginadas, 6 quadros × 9
termos de busca), 964 no Greenhouse (19 tokens), e o restante na Ubisoft e na NBCUniversal via
SmartRecruiters, mais 5 buscas no SuccessFactors da Paramount.

---

## 2. FILA PRONTA PARA CLICAR

> **Aviso de cadência.** A campanha roda uma candidatura por casa por rodada.
> As nº 2 e 3 são **a mesma casa (2K/Cloud Chamber)** e as nº 4, 5 e 6 são **a mesma casa
> (Ubisoft)** — escolha **uma de cada bloco**. Nem a 2K nem a Ubisoft receberam qualquer coisa em
> 09/09 (o último contato com a Ubisoft foi 07/09, e-mail na Massive), então as duas portas estão
> livres. A Disney **já recebeu duas** hoje (`10137201` e `10142674`), ambas pela exceção da REGRA 14.

---

### 1. Disney / ILM London — FaceSwap Artist (todos os níveis)

| Campo | Valor |
|---|---|
| **Estúdio** | Industrial Light & Magic, London Studio (grupo Disney) |
| **Título exato** | `FaceSwap Artist - all levels - London Studio` |
| **ID de requisição** | `10160278` |
| **Cidade / país** | Londres, Reino Unido |
| **Publicada** | **2026-09-08 — ontem.** O anúncio traz `Date Posted: 2026-09-08`; a listagem diz `Posted Yesterday` |
| **Tipo** | Full time |
| **Família de ATS** | Workday — `disney.wd5` · tenant `disney` · site `disneycareer` (também visível em `disneycareerdc`) |
| **URL de candidatura** | https://disney.wd5.myworkdayjobs.com/en-US/disneycareer/job/London-United-Kingdom/FaceSwap-Artist---all-levels---London-Studio_10160278 |
| **URL verificada** | HTTP 200 |

**Régua de veto — vinte termos no anúncio integral (2.392 caracteres). Um acerto, falso positivo:**

> `within` — *"FaceSwap is a new, exciting, and growing discipline **within the visual effects
> industry**, using Machine Learning (AI) to create digital faces and likenesses."*

É `within the industry`, falso positivo nominal da lista. **Os outros dezenove termos não aparecem
em lugar nenhum**: nada de `authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`,
`based in`, `only from`, `LMIA`, `days a week`, `days per week`, `days in the office`, `resident`,
`relocat`, `located in`, `unable to support`, `no relocation`, `x a week`, `x per week`, nem
exigência de idioma local. O anúncio termina no bloco administrativo (`Job Posting Segment: ILM
London` … `Date Posted: 2026-09-08`) — **não existe bloco de Eligibility Requirements**, que é
onde a Rebellion e a NBCU escondem o veto.

**Veto escrito: ZERO.**

**Dedupe por ID de requisição:** `10160278` → **0** em `enviados.csv`, **0** em
`automacao/processados.csv`, **0** em `docs/index.html`, **0** em `automacao/FILA-DO-VINI.md`.
Inédita na campanha.

**Ressalva honesta de disciplina — leia antes de clicar.** Entra pela REGRA 14 (vaga de arte da
Disney/ILM entra na fila imediatamente), o título é literalmente *Artist* e a categoria interna é
`Faceswap - Studios` da ILM London. Mas o corpo **não é modelagem nem escultura**:

> *"Working knowledge of Nuke to prepare precomps and slap comps"* · *"Some experience with CG
> compositing"* · *"Comfortable working with or learning command-line based tools"* ·
> *"Interested in, or have basic familiarity with, deep neural networks"* · *"Familiarity with
> ComfyUI and other GenAI tools"*.

É composição + machine learning, não ZBrush. O que joga a favor está escrito na abertura:
*"While a background in compositing is advantageous, **artists with visual effects experience in
any discipline are encouraged to apply**"*, e o *nice to have* é *"Experience working on projects
with realistic looking CGI humans or other face replacement approaches"*. **A decisão é do Vini.**
A REGRA 14 e a régua limpa colocam ela aqui; a disciplina diz que é a mais distante do centro do
portfólio nesta fila.

---

### 2. 2K / Cloud Chamber — Senior Level Artist (BioShock), Novato

| Campo | Valor |
|---|---|
| **Estúdio** | Cloud Chamber (2K / Take-Two) — franquia BioShock |
| **Título exato** | `Senior Level Artist` |
| **ID de requisição** | `7731298003` |
| **Cidade / país** | Novato, Califórnia, EUA |
| **Publicada** | 2026-05-21, atualizada 2026-08-21 |
| **Faixa publicada** | **USD 100.200 – 148.320 / ano** (na Califórnia) |
| **Família de ATS** | Greenhouse (board `2k`, departamento `Art - Cloud Chamber`) |
| **URL de candidatura** | https://job-boards.greenhouse.io/2k/jobs/7731298003 |
| **URL verificada** | HTTP 200 |

**Régua de veto — anúncio integral (7.433 caracteres). Cinco acertos, todos falsos positivos:**

> `eligib` ×3 — *"…a bonus and/or equity awards and **eligibility to participate in our 401(K)
> plan** and Employee Stock Purchase Program. Regular, full-time employees are also **eligible for
> a range of benefits**…"* e *"…paid vacation time per calendar year (ranging from 15 to 25 days)
> or **eligibility to participate** in the Company's discretionary time off program…"*
>
> É o bloco de **benefícios**, não de elegibilidade para trabalhar. Nenhum dos três fala de
> autorização de trabalho.

> `only` — *"When emailing prospective employees, we **only use** 2K.com accounts."* Cláusula
> anti-golpe, padrão do setor.

> `located in` — *"For candidates **located in Quebec**: This position requires professional
> proficiency in both French and English."*
>
> **Condicional e geograficamente delimitada a Quebec.** Esta é a vaga de **Novato, Califórnia**
> — o texto de pagamento confirma: *"The pay range for this position **in California**…"*.
> Candidato que não está em Quebec não é alcançado pela cláusula. Ela existe no texto porque a
> requisição é publicada nos dois escritórios; a gêmea de Montréal (`7731297003`) **está vetada
> por ela** e foi descartada (seção 3.3).

**Nenhum dos demais termos aparece:** sem `authoriz`, `sponsor`, `work permit`, `must be based`,
`based in`, `LMIA`, `days a week`, `days per week`, `days in the office`, `relocat`,
`no relocation`, `unable to support`, `resident`.

**Veto escrito: ZERO** para candidato fora de Quebec.

**Dedupe:** `7731298003` → **0** em `enviados.csv`, `processados.csv`, `docs/index.html`,
`FILA-DO-VINI.md`, `casas-grandes-e-revalidacao.md`, `MANHA-09-09.md`, `fila-do-maestro.md` e
`alvos.csv`. Inédita.

**Disciplina — passa com folga, e é a mais próxima do centro do portfólio nesta fila:**
> *"**Create believable, functional, and visually strong environments from scratch**"* ·
> *"Create and compose **modular kits** and collection sets to form optimized yet dramatic and
> detailed spaces"* · *"Participate in **look development**, creating visual benchmark
> environments"* · *"Work with Leads to develop **world building and modeling processes** (…) and
> ensure that quality is maintained for **environment art**"*.

Requisito de entrada: *"Experience shipping at least one 3D AAA title in FPS or Third Person"*.
Environment art de verdade, com criação do zero e look dev no corpo da vaga.

---

### 3. 2K / Cloud Chamber — Lead Level Artist (BioShock), Novato

| Campo | Valor |
|---|---|
| **Estúdio** | Cloud Chamber (2K / Take-Two) — franquia BioShock |
| **Título exato** | `Lead Level Artist` |
| **ID de requisição** | `7812710003` |
| **Cidade / país** | Novato, Califórnia, EUA |
| **Publicada** | 2026-07-31, atualizada 2026-08-21 |
| **Faixa publicada** | **USD 125.400 – 185.580 / ano** (na Califórnia) — a mais alta desta fila |
| **Família de ATS** | Greenhouse (board `2k`, departamento `Art - Cloud Chamber`) |
| **URL de candidatura** | https://job-boards.greenhouse.io/2k/jobs/7812710003 |
| **URL verificada** | HTTP 200 |

**Régua de veto — anúncio integral (6.810 caracteres). Os mesmos cinco falsos positivos da nº 2**,
palavra por palavra: `eligib` ×3 no bloco de benefícios (401K, férias, licença), `only` na
cláusula anti-golpe (*"we only use 2K.com accounts"*) e `located in` na cláusula condicional
*"For candidates located in Quebec"* — que não alcança esta vaga, cuja faixa é declarada
*"for this position **in California**"*. Nenhum dos outros quinze termos aparece, e não há
exigência de idioma local para o candidato da Califórnia.

**Veto escrito: ZERO** para candidato fora de Quebec.

**Dedupe:** `7812710003` → **0** nos oito arquivos conferidos. Inédita.

**Disciplina — passa:**
> *"lead a team of artists responsible for creating compelling, stylized, **high-quality level art
> and immersive world-building**"* · *"**Design and improve upon the modular systems of
> architecture** for our levels"* · requisito: *"7 or more years of experience in internal game
> development with an **emphasis on environmental art or level architecture**"*.

**Ressalva:** é cargo de **liderança** — gerir, mentorar, montar cronograma. Menos mão na
ferramenta que a nº 2. Note também o *"stylized"* escrito no primeiro parágrafo, que é exatamente
o eixo do portfólio dele.

---

### 4. Ubisoft Montréal — Level Artist (Unreal)

| Campo | Valor |
|---|---|
| **Estúdio** | Ubisoft Montréal |
| **Título exato** | `Level Artist (Unreal)` |
| **ID de requisição** | `REF31656C` (posting `744000145286834`) |
| **Cidade / país** | Montreal, Canadá |
| **Publicada** | 2026-08-24 |
| **Família de ATS** | SmartRecruiters — empresa **`Ubisoft2`** (não `Ubisoft`; ver seção 4.2) |
| **URL de candidatura** | https://jobs.smartrecruiters.com/Ubisoft2/744000145286834 |
| **URL verificada** | HTTP 200 |

**Régua de veto — vinte termos no anúncio integral (2.191 caracteres): NENHUM ACERTO.**
Zero literal. Nem `authoriz`, nem `eligib`, nem `sponsor`, nem `work permit`, nem `based in`,
nem `days a week`, nem `relocat`, nem `located in`, nem `resident`, nem `only`, nem `within the`.
**E — apesar de ser Montréal — nenhuma exigência de francês nem de qualquer idioma local
no texto do anúncio.** É a diferença literal entre esta e as gêmeas de Montréal da 2K.

**Veto escrito: ZERO.**

**Dedupe:** `REF31656C` → **0** em `enviados.csv`, `processados.csv`, `docs/index.html`,
`FILA-DO-VINI.md`, `casas-grandes-e-revalidacao.md`, `MANHA-09-09.md`, `colheita-europa.md`,
`fila-do-maestro.md` e `alvos.csv`. Inédita.

**Disciplina — passa:**
> *"As a Level Artist at Ubisoft Montréal, you will create immersive and memorable **3D
> environments**"* · *"Place proxies and **communicate modeling and texturing needs** with art
> teams"* · qualificações: *"Proficiency with 3D software such as Maya or 3ds Max"*,
> *"**Experience with modeling, texturing**, lighting, or image processing"*.

**Ressalva:** é montagem e integração em Unreal; a modelagem aparece como necessidade a comunicar
aos times de arte, não como o ofício central do cargo.

---

### 5. Ubisoft Annecy — Lead Level Artist (F/M/NB) [AAA Project]

| Campo | Valor |
|---|---|
| **Estúdio** | Ubisoft Annecy |
| **Título exato** | `Lead Level Artist (F/M/NB) [AAA Project]` |
| **ID de requisição** | `REF31639U` (posting `744000140062829`) |
| **Cidade / país** | Annecy, França |
| **Publicada** | 2026-07-27 |
| **Família de ATS** | SmartRecruiters (`Ubisoft2`) |
| **URL de candidatura** | https://jobs.smartrecruiters.com/Ubisoft2/744000140062829 |
| **URL verificada** | HTTP 200 |

**Régua de veto — anúncio integral (5.869 caracteres). Dois acertos, os dois falsos positivos:**

> `located in` — *"…with a technological expertise hub around the Snowdrop engine pipeline (…).
> **Located in one of the most dynamic regions of France**, our Ubisoft studio is settled between
> lake and mountains, in the middle of Annecy…"*
>
> Descreve **onde o estúdio fica**, em parágrafo de propaganda da cidade. É exatamente o falso
> positivo catalogado: `based in` / `located in` descrevendo onde o CARGO fica não veta.

> `within the` — *"**Collaboration within the World Team** • Translate the Art Direction and World
> Director's vision into concrete artistic objectives for the World team."* — `within the team`,
> falso positivo nominal.

Os outros dezoito termos: ausentes. **Sobre idioma: a única exigência é `"Fluency in English"` —
inglês, não o idioma local.** Francês não é pedido em lugar nenhum do anúncio, o que num estúdio
francês é o oposto de um veto.

**Veto escrito: ZERO.**

**Dedupe:** `REF31639U` → **0** nos nove arquivos conferidos. Inédita.

**Disciplina — passa:** *"The Lead Level Artist is responsible for the quality, consistency, and
artistic execution of the **environments** produced by the World team"*; qualificações pedem
*"**Extensive experience creating environments for video games**"* e *"Excellent understanding of
composition, **materials**, color, volume, and environmental storytelling"*.

**Ressalva:** é cargo de **gestão** (organizar o time, mentorar, priorizar riscos de produção),
com pouca mão na ferramenta.

---

### 6. Ubisoft Montréal — Senior Level Artist

| Campo | Valor |
|---|---|
| **Estúdio** | Ubisoft Montréal |
| **Título exato** | `Senior Level Artist` |
| **ID de requisição** | `REF31781B` (posting `744000145286684`) |
| **Cidade / país** | Montreal, Canadá |
| **Publicada** | 2026-08-24 |
| **Família de ATS** | SmartRecruiters (`Ubisoft2`) |
| **URL de candidatura** | https://jobs.smartrecruiters.com/Ubisoft2/744000145286684 |
| **URL verificada** | HTTP 200 |

**Régua de veto — anúncio integral (3.119 caracteres): NENHUM ACERTO** nos vinte termos, e
nenhuma exigência de idioma.

**Veto escrito: ZERO.**

**Dedupe:** `REF31781B` → **0** nos nove arquivos. Inédita.

**Ressalva de disciplina, e é a mais dura da fila — está escrita no próprio anúncio:**
> *"This position is **not primarily focused on creating high-resolution 3D assets or producing
> full environment models from scratch**."*

O cargo é montar e integrar asset que já existe (*"Assemble and integrate existing assets into the
game engine"*). O portfólio do Vini é escultura e modelagem, ou seja, exatamente o que a vaga diz
que **não** é o foco. **Fica em último.** Régua limpa e dedupe zero são o motivo de ela estar
listada em vez de descartada em silêncio — a decisão é dele, com a frase acima na mão.

---

## 3. O que morreu, e por quê

### 3.1 Morreu no dedupe — 44 requisições

De longe a maior causa de morte. **A campanha já cobriu quase tudo que estava vivo.** Passaram
disciplina, escopo e régua, e bateram em ID de requisição já registrado:

| Casa | Requisições já trabalhadas |
|---|---|
| Disney / ILM | `10159370` (Senior Texture Artist London, **enviada 02/09**), `10159371` (Lead Texture Artist London), `10159882` (Senior Modeler Sydney, **enviada 04/09**), `10142674` (Lead Generalist Vancouver, **enviada 09/09**), `10137201` (**enviada 09/09**), `10052606`, `10153285` |
| Netflix / Netflix Animation | `JR41751`, `JR41734`, `JR39446`, `JR39273`, `JR41749`, `JR41288` |
| Netflix / Eyeline Seul | `JR40923`, `JR40928`, `JR40941` |
| Ubisoft | `REF31793B` (Senior Character Artist R6 Siege, Montreal), `REF31739L` (Lead Character Artist Division 2, Malmö), `REF31530C` (Team Lead Modeling, Montreal), `REF31279C` (Team lead Character, Montpellier) |
| 2K / Take-Two | `7888173003`, `7888174003` (Lead Character Artist, Montréal e Novato), `7835808003` (Senior Character Artist, Burnaby) |
| Epic Games | `6121292004`, `6001731004` (**enviada 09/09 às 14h19 UTC**), `6142980004` (**enviada 03/09**), `6020682004`, `6020680004` |
| Sony Pictures Imageworks | `4363748003` / `4363749003` (Modeler e Experienced Modeler), `4363798003` / `4363799003` (Texture Artist), `6659179003` (Look Development Artist), `6669063003` (Environment Artist), `7529417003` |
| Loonshot Games (Seul) | `8725151002`, `8085897002`, `8651145002` |
| Scopely (Barcelona) | `5398064008`, `5398038008`, `5398026008` |
| Hasbro | `4318250009` (Lead Character Artist, Canadá) |
| Wargaming (Nicósia) | `8161671` |
| Warner Bros Discovery | `R000106508` (Advanced Level Artist, Montreal) |

O dedupe foi por **ID de requisição com fronteira de palavra**, nunca por título.

**Registro um erro meu que quase virou ruído.** A primeira passada usou `grep -c` cru, que casa ID
numérico dentro de `message_id` de e-mail no `processados.csv` e devolveu "duplicata" onde não
havia — o script chegou a marcar as **treze** requisições inéditas como DUP. Refiz com regex de
fronteira de palavra e conferi o **contexto textual** de cada acerto antes de aceitar. Sem isso,
esta rodada teria entregue zero.

### 3.2 Morreu por requisição-espelho ou gêmea bilíngue — 4

Não são IDs repetidos: é **a mesma requisição publicada duas vezes**, num segundo balde de local
ou num segundo idioma. Aplicar nas duas é candidatura repetida — o erro que o `RISCO-DUPLICATA.md`
documenta e que já aconteceu duas vezes em 07/09.

| ID novo | É espelho de | Prova |
|---|---|---|
| `6130892004` Principal Environment Artist | `6121292004` (no painel como "próxima da Epic") | mesmo escritório `Cary`, `first_published` idêntico `2026-07-30T14:28:07-04:00`, `updated_at` idêntico |
| `6001733004` Senior Environment Artist | `6001731004` (**enviada 09/09 às 14h19 UTC**) | mesmo escritório `Cary`; `first_published` `2026-08-17T11:21:01` contra `…:00` — **um segundo** de diferença |
| `6142982004` Hard Surface Outsource Lead | `6142980004` (**enviada 03/09**) | mesmo escritório `Cary`, mesmo `updated_at` |
| `4318249009` Chef.fe d'équipe - Artist de personnages | `4318250009` Lead Character Artist (já em `processados.csv`) | **é a versão em francês da mesma vaga**, mesmo board Hasbro, mesmo local "Canada" |

A gêmea bilíngue da Hasbro é exatamente a armadilha listada no `RISCO-DUPLICATA.md`
(*"Casa bilíngue publica a mesma vaga em dois idiomas: Ubisoft, Larian, Gameloft, Sloclap,
Skydance Madrid e Rodeo FX já enganaram nosso dedupe assim"*).

### 3.3 Morreu por exigência de idioma local — 2

As gêmeas de **Montréal** das duas vagas da 2K/Cloud Chamber. Veto escrito, literal:

> *"For candidates located in Quebec: **This position requires professional proficiency in both
> French and English.**"*

Francês é o idioma local do Quebec, e a régua veta exigência de idioma local. As gêmeas de
**Novato** sobrevivem porque a cláusula é condicional a estar em Quebec, e essas vagas declaram
faixa salarial *"for this position in California"* — são as nº 2 e nº 3 da fila.

| ID | Cargo | Local |
|---|---|---|
| `7731297003` | Senior Level Artist | Montréal, QC |
| `7812709003` | Lead Level Artist | Montréal, QC |

### 3.4 Morreu na releitura de disciplina, depois do texto integral — 1

**`JR40916` — Environment Lead, Eyeline Seul** (Netflix, `netflix.wd108`, site `Eyeline`).
Dedupe **zero** nos quatro arquivos. Régua **zero** (único acerto: `within the industry`, falso
positivo). Escopo geográfico OK — Coreia do Sul está na lista. Passou tudo, e morreu na leitura:

> Título interno é *"The **Lead Environment Generalist**"*. Responsabilidades: *"Approaches will
> vary from **2.5D Matte Painting projection setups**, through full 3D asset builds"* e
> *"**Creates 2D paintings** and 3D using photography, practical and digital skills"*.
> Qualificações: *"Minimum five (5) years of previous experience as a **Digital Matte Painter** or
> Environment Artist"* e *"**Expert in Adobe Photoshop**"* — Photoshop é a **única** ferramenta com
> nível "Expert"; Maya e Houdini ficam em *"Strong understanding"* e Mari em *"Working knowledge"*.

É o mesmo perfil que a campanha já recusou por escrito em `10052606` (Sr Generalist Artist, ILM
Vancouver) e em `10153285`: pintura digital com 3D de apoio. **Mantive a recusa por coerência com
o precedente, e registro que é reversível** — régua limpa, dedupe zero. Se o Vini quiser disputar
matte painting, está em
`https://netflix.wd108.myworkdayjobs.com/Eyeline/job/Eyeline-Seoul/Environment-Lead_JR40916`.

### 3.5 Morreu na régua, com veto ESCRITO — 4

As quatro de **Montréal da NBCUniversal**, e o veto não é interpretação, é literal. Frase idêntica
nas quatro, no bloco `Eligibility Requirements` que **não aparece na listagem**, só no anúncio:

> *"Eligibility Requirements — Interested candidates must apply to be considered. **Must be willing
> to work in our Montreal office a minimum of 4 days a week. Must be legally authorized to work in
> Canada.** Must be willing to travel for work related business, if necessary"*

Bate três termos de uma vez: `eligib`, `days a week`, `authoriz`.

| Ref | Cargo | Local |
|---|---|---|
| `REF38910F` | Lead Character Artist (Body/Crowd, Face, Hair & Wardrobe) | Montréal |
| `REF38920U` | Lead Material Artist (Character/Wardrobe, World/Props) | Montréal |
| `REF38909O` | Associate Art Director (Characters, Concepts, Lighting & VFX, World) | Montréal |
| `REF38918P` | Lead Artist (Procedural) | Montréal |

Estas quatro já tinham sido levantadas e adjudicadas em `casas-grandes-e-revalidacao.md` (seção
1.4). **Reconfirmei o levantamento pela API hoje** e não mexi no veredito.

### 3.6 Morreu no escopo geográfico — 10

Fora da América do Norte, Europa/UK/Irlanda/Nórdicos/UE, Oceania, Coreia do Sul e Singapura.
Concentrado em dois lugares, e dói:

- **Índia — Disney/ILM Mumbai:** `10155895` Lead Modeler, `10154147` Sr Character Modeler,
  `10146393` Lead Environment Artist, `10152359` e `10152365` Generalist Artist.
- **Índia — Netflix/Eyeline Hyderabad:** `JR01060` Groom Artist, `JR41016` Lead Surfacing Artist,
  `JR01007` Modeling Supervisor, `JR41011` Surfacing/Lookdev Artist.
- **Brasil:** Epic `6031088004` Modeling Outsource Lead, Porto Alegre.

Nove destas dez são de disciplina perfeita — groom, modelagem, surfacing, look dev. Todas barradas
só pelo escopo.

### 3.7 Morreu na disciplina — 10 no filtro de título, mais ~170 na varredura ampla de conferência

Fora do escopo de personagem / modelagem / groom / look dev / environment / sculpt:
CFX e simulação (`JR41810` e `JR39105` Head of Character Effects; `REF38952U` DreamWorks Feature
Character Effects Artist; Sony Imageworks Character FX; `JR01528` Lead Crowd Artist), rigging e TD
(`10155976`, `10144787`, `10157562` Creature TD, `REF31734P` e `REF31683K` Senior Character
Rigger, Insomniac Facial Character TD, `7978391003` 2K Rigger), technical art (`REF38921T`,
Rockstar Senior Technical Artist: Procedural Art ×3, Epic Senior Technical Artist ×6, Hasbro
Senior Technical Artist), lighting (`REF38919W`, `10124854`, `10159099`, Housemarque ×3, 2K ×3),
concept 2D puro (as três da Cloud Imperium, as da Riot, oito da Wargaming, cinco da Loonshot),
desenho e pintura 2D (`JR41777` Character Designer Ink, `JR41752` Story Artist Ink, `10159762`
Character Design Lead da Disney TV Animation, `10087909` Sr Paint & Roto), previz e layout
(`10137201`, já enviada; Sony Imageworks Layout Artist ×2, Scene Assembly Artist ×2), VFX
(`REF31847T`, `REF31778B`, `REF31313P`, CIG ×3), e UI (Ubisoft ×4, Scopely ×3).

Rodei ao fim uma **varredura ampla de conferência** — filtro de disciplina propositalmente frouxo,
sem nenhuma exclusão — sobre os 2.654 postings, para pegar o que um filtro de palavra-chave
deixaria passar. Devolveu 177 inéditos; **todos os 177 caem nas categorias acima**, exceto os 13
que já estavam na minha contagem. Nenhuma vaga de disciplina certa escapou.

---

## 4. Mapa dos quadros — o que está vivo, o que está morto

É o resultado que mais vale para a próxima rodada: **três casas da lista não estão no Workday que o
briefing supunha**, e uma quarta estava com o tenant errado.

### 4.1 Quadros VIVOS confirmados hoje

| Casa | Família | Endereço exato | Vagas lidas |
|---|---|---|---|
| Disney / ILM / Lucasfilm | Workday | `disney.wd5` · tenant `disney` · site **`disneycareerdc`** | 83 em "artist" |
| Disney (corporativo) | Workday | `disney.wd5` · tenant `disney` · site **`disneycareer`** | 54 em "artist" |
| Netflix / Netflix Animation | Workday | **`netflix.wd108`** · tenant `netflix` · site `Netflix` | 64 |
| Netflix / Eyeline | Workday | **`netflix.wd108`** · tenant `netflix` · site `Eyeline` | 46 |
| Cloud Imperium Games | Workday | **`cloudimperiumgames.wd503`** · site `CIG_Global_Careers` | 24 |
| Warner Bros Discovery | Workday | **`warnerbros.wd5`** · tenant **`warnerbros`** · site `global` | 144 |
| **Ubisoft** | **SmartRecruiters** | empresa **`Ubisoft2`** | 227 |
| **NBCUniversal / DreamWorks** | **SmartRecruiters** | empresa `NBCUniversal3` | 227 |
| **Paramount** | **SuccessFactors (j2w)** | `careers.paramount.com/search/?q=` | 5 buscas |
| Greenhouse com vagas (13 tokens) | Greenhouse | `boards-api.greenhouse.io/v1/boards/<token>/jobs` | 964 |

Tokens Greenhouse vivos: `2k` (120), `epicgames` (159), `riotgames` (141), `scopely` (177),
`hasbro` (155), `rockstargames` (62), `wargamingen` (56), `sonypicturesimageworks` (52),
`loonshotgames` (23), `insomniac` (6), `digitalextremes` (5), `atomiccartoons` (5), `housemarque` (3).

### 4.2 Correções ao mapa do briefing

| O briefing dizia | O oráculo respondeu | O certo |
|---|---|---|
| `netflix.wd1` | **422** | `netflix.wd108` |
| `activision.wd1` | **422** em wd1/wd3/wd5/wd103 | tenant `activision` não existe em pod nenhum |
| `cloudimperiumgames.wd1` | **422** | `cloudimperiumgames.wd503` |
| `ubisoft.wd3` | **422** | não é Workday — SmartRecruiters, empresa **`Ubisoft2`** |
| `wbd.wd5` | **422** | tenant é **`warnerbros`**, site `global` |
| `paramount.wd5` | **422** | não é Workday — SuccessFactors em `careers.paramount.com` |
| `nbcuniversal` | **422** | não é Workday — SmartRecruiters **`NBCUniversal3`** |
| `take2games` / `rockstargames` Workday | **422** | são Greenhouse (`2k` e `rockstargames`) |
| `zynga`, `jamcity` | **422** Workday, **404** Greenhouse | quadro não localizado |

Sobre o `Ubisoft2`: o token óbvio (`Ubisoft`) responde **HTTP 200 com `totalFound: 0`** — um zero
que parece resposta legítima e não é. `Ubisoft1` e `UbisoftGroup` fazem o mesmo. Só `Ubisoft2`
devolve as 284 requisições. **Zero com HTTP 200 é a pior armadilha desta rodada**, porque não
levanta suspeita como um 404 levanta.

### 4.3 Quadros mortos ou não resolvidos — 13

- **EA** (`ea.wd5`): tenant existe, mas devolve **401 nos dez nomes de site testados**. Quadro
  fechado para leitura anônima nesta rodada. Não é ausência de vaga, é porta trancada.
- **Sony Pictures Entertainment** (`spe.wd1`): tenant **vivo** (404 = caminho errado, não 422), mas
  os doze nomes de site testados deram 404. **Fica como dívida para a próxima rodada.** A parte de
  arte da casa é a Imageworks, que está no Greenhouse e foi varrida (7 requisições, todas já
  trabalhadas).
- **Comcast** (`comcast.wd5`): devolve **303 para `community.workday.com/maintenance-page`**.
  Tenant em manutenção; a NBCU foi alcançada pelo SmartRecruiters de qualquer forma.
- **Activision / Blizzard / King:** nenhum tenant Workday em 4 pods × 5 grafias (`activision`,
  `activisionblizzard`, `blizzard`, `king`, `abk`). Depois da compra pela Microsoft as requisições
  migraram para o portal da Microsoft — **fora do alcance deste método**.
- **Take-Two / Rockstar Workday:** não existem. Cobertos via Greenhouse.
- **Greenhouse 404:** `embarkstudios`, `playdead`, `jamcity`, `zynga`, `takes2`.
- **`blurstudio`:** HTTP 200 com **zero vagas** — quadro vivo e vazio.
- **Bloqueados pela política de egresso do proxy** (403/502 no CONNECT; não insisti, conforme a
  regra de não contornar): `jobs.nbcuni.com`, `careers.dreamworks.com`, `jobs.sonypictures.com`,
  `careers.riotgames.com`. Os quatro foram alcançados por outra rota (SmartRecruiters e
  Greenhouse), menos a Sony Pictures corporativa.

---

## 5. As casas da REGRA 14, uma por uma

O briefing manda re-rodar sozinha qualquer casa da REGRA 14 que devolva zero. Fiz nas quatro.

- **Disney — NÃO deu zero.** Sete requisições de disciplina e escopo certos; seis já trabalhadas,
  **uma inédita: `10160278`, publicada ontem**, que é a nº 1 da fila. Achei numa segunda passada
  **por data de publicação**, não por palavra-chave — *FaceSwap* não contém nenhum termo de
  disciplina e teria escapado do filtro de título. Registro o quase-erro: sem a passada por
  recência, a Disney teria devolvido zero hoje.
- **Warner Bros Discovery — deu zero, e RE-RODEI.** Não é bug de parser: o parser leu 144 vagas com
  título e local corretos. Re-rodada isolada com nove termos extras (`character artist`,
  `3d artist`, `environment artist`, `modeler`, `sculptor`, `concept`, `art`, `animation`,
  `cinematics`). O quadro inteiro tem **dois** títulos de arte: `R000106815` Senior Lighting Artist
  (Rocksteady, Londres — fora da disciplina) e `R000106508` Advanced Level Artist (Montreal —
  **já em `processados.csv`**). `sculptor` devolveu 0 resultados. **Zero é real.**
- **Paramount — deu zero, e RE-RODEI.** O zero inicial era do endereço errado (`paramount.wd5` =
  422). Achei o quadro de verdade — SuccessFactors em `careers.paramount.com`, identificado pelo
  caminho `platform/css/j2w/` no HTML — e rodei cinco buscas nele. O único título com "arte" é
  `Art Director, Broadcast — CBS Sports, NY`, que é grafismo 2D de transmissão. **Zero é real,
  agora medido no quadro certo.**
- **DreamWorks / NBCUniversal — o zero ERA bug, e a re-rodada pagou.** O `nbcuniversal.wd5` dava
  422 e teria virado "casa sem vaga". Persegui e achei o quadro real (SmartRecruiters
  `NBCUniversal3`, via o HTML de `www.nbcunicareers.com`): **oito requisições de arte**, quatro
  delas de personagem/material em Montréal. Todas morreram — mas por **veto escrito lido no
  anúncio** (seção 3.5), não por ausência. É a diferença entre "não tem vaga" e "tem vaga e ela
  nos exclui".

---

## 6. Resumo de uma linha

**Seis linhas na fila**, todas com régua de veto zero, dedupe por ID de requisição zero e URL de
candidatura verificada em HTTP 200:

1. `10160278` — Disney / ILM London, FaceSwap Artist — **publicada ontem**, REGRA 14
2. `7731298003` — 2K / Cloud Chamber, Senior Level Artist, Novato — USD 100.200–148.320
3. `7812710003` — 2K / Cloud Chamber, Lead Level Artist, Novato — USD 125.400–185.580
4. `REF31656C` — Ubisoft Montréal, Level Artist (Unreal)
5. `REF31639U` — Ubisoft Annecy, Lead Level Artist
6. `REF31781B` — Ubisoft Montréal, Senior Level Artist

**Escolha uma do bloco 2K (nº 2–3) e uma do bloco Ubisoft (nº 4–6)** pela regra de uma candidatura
por casa por rodada. As duas casas estão livres hoje.

Arquivo: `/home/user/workbenchMA/automacao/caca-casasgrandes-0909-tarde.md`
