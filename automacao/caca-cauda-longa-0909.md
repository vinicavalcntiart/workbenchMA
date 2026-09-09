# Caça de CAUDA LONGA — 09/09/2026, noite

**Famílias desta rodada:** Jobvite, Pinpoint, Dayforce, SuccessFactors, iCIMS, Avature, Eightfold,
Phenom, Factorial, Traffit, eRecruiter, Humi, JazzHR e formulário próprio de WordPress.
**Método:** só `curl`. Nenhum navegador, nenhum Playwright, nenhum `hb_run.sh`. Concorrência 8-10.
**Não commitei, não dei push, não preenchi nem enviei formulário nenhum.** Não toquei em
`docs/index.html`, `enviados.csv`, `automacao/processados.csv` nem `automacao/FILA-DO-VINI.md`.
Este arquivo é o único que criei.

---

## PLACAR DE CIMA

| Etapa | Número |
|---|---|
| Slugs/URLs sondados no total | **9.955** |
| JazzHR `applytojob.com` | 3.122 slugs |
| JazzHR `applytojobs.ca` | 1.409 slugs |
| Traffit (pela API `/public/an/list/`) | 1.420 slugs |
| Humi `humi.ca/job-board` | 1.411 slugs |
| Factorial `factorialhr.com` | 1.367 slugs |
| Avature `avature.net/careers` | 1.367 slugs |
| Eightfold `eightfold.ai/careers` | 1.367 slugs |
| WordPress/formulário próprio (páginas de carreira já confirmadas) | 1.406 URLs, 1.364 com corpo real |
| Pinpoint (re-teste dos quadros do relatório da madrugada) | 15 quadros |
| Jobvite (re-enumeração do único quadro da área) | 101 ids da DNEG |
| iCIMS / Dayforce / SuccessFactors / Phenom | sondagem dirigida (ver §4) |
| **Quadros vivos revelados nas famílias novas** | **JazzHR 21 · Traffit 7 · Factorial 7 · Humi 1 · Avature 0 · Eightfold 0** |
| Vagas da disciplina que chegaram à régua | 17 |
| **Sobreviveram a escopo + disciplina + régua + dedupe** | **9 linhas, em 4 casas** |

**Fila: 9 linhas em 4 casas — Jungler (França, 6 perfis), Flaming Fowl (Reino Unido/remoto mundial),
Future Associate (Sydney) e Glinda Games (Melbourne).**
A casa que mais rende é a **Jungler**, e ela é o caso exato que o painel já viu na UFX: aparece
**só em arquivo de garimpo**, nunca como candidatura, e ninguém tinha achado a porta de ATS dela.

**Aviso de captcha, que decide quem clica:** **três das quatro casas da fila têm parede conhecida
ou provável.** Só a **Future Associate** tem porta medida **sem captcha nenhum**. Detalhe em cada linha.

---

# A. FILA PRONTA PARA CLICAR

## A1 a A6 — JUNGLER · La Plaine Saint-Denis (Paris), França · JAZZHR

**A descoberta desta rodada.** A Jungler é um estúdio de animação 2D/3D de Paris (publicidade,
longas e séries, fundado em 2015). O painel só conhecia `jungler.tv/jobs` pelo `garimpo-cgstudiomap.csv`.
**Eu achei o quadro de ATS: `jungler.applytojob.com` (JazzHR), com 31 perfis abertos, seis deles
exatamente da disciplina dele.**

**Dedupe, arquivo por arquivo, por ID E pelo nome da casa:**

| Busca | `enviados.csv` | `automacao/processados.csv` | `docs/index.html` | `automacao/FILA-DO-VINI.md` |
|---|---|---|---|---|
| `jungler` (nome da casa) | **0** | **0** | **0** | **0** |
| `LaJk360GBo` | 0 | 0 | 0 | 0 |
| `C6fYfcxuWg` | 0 | 0 | 0 | 0 |
| `KvYb9uJMHM` | 0 | 0 | 0 | 0 |
| `2Ft7PxD7Nn` | 0 | 0 | 0 | 0 |
| `vao65i7Ttc` | 0 | 0 | 0 | 0 |
| `p2hqhQuoBt` | 0 | 0 | 0 | 0 |

**Teste barato de recibo, como você mandou:** `grep "<id>/confirmation"` e `grep -i "<id>.*ENVIADA"`
nos quatro arquivos → **0 em todas as 48 combinações**. Nunca foi enviada.
Fora dos quatro arquivos, `jungler` aparece só em `automacao/garimpo-cgstudiomap.csv`,
`automacao/garimpo-cgstudiomap.md` e `automacao/fila-remotegamejobs-estudios.csv` — **três arquivos
de fila, zero candidatura.** É o padrão UFX: casa fichada, porta nunca aberta.

**Régua de vinte termos + idioma local, rodada no texto INTEGRAL da página de candidatura
(3.366 caracteres na 3D Surfacing, idênticas nas outras cinco). Três acertos, os três falsos positivos catalogados:**

- `based in` → *"Jungler is a 2D and 3D animation studio created in 2015 and **based in** Paris."*
  → diz onde o **ESTÚDIO** fica. Falso positivo do tipo que você já catalogou.
- `relocat` → *"Are you willing to **relocate**? No answer / Yes / No"*
  → é **pergunta do formulário**, não restrição do anúncio. E é sinal a favor: eles contemplam mudança.
- `only` → *"Please let us know if you're **only** available until a certain date (other project incoming, etc.)"*
  → pergunta do formulário sobre disponibilidade.

**IDIOMA LOCAL: NÃO HÁ EXIGÊNCIA DE FRANCÊS.** O anúncio é bilíngue (francês e inglês, lado a lado),
mas a única linha de idioma é *"**Pratique de l'anglais** en fonction des projets"* — **inglês**,
conforme o projeto. Nenhum `français obligatoire`, nenhum `French required`. Isto é importante porque
anúncio escrito em francês parece veto de idioma e **não é**.

**Frase de presencial, e ela não casa com nenhum dos vinte termos:** *"Le travail au studio est
privilégié"* / *"**Studio work is preferred**. The studio is located at La Plaine Saint-Denis
(metro line 12 - Front Populaire)"*. É preferência escrita, não exigência, e o `located at` nem é
`located in`. **Veto escrito: ZERO nas seis.**

**Faixa salarial publicada: NENHUMA.** O formulário tem campo *"Desired salary"* — quem informa é ele.

**Família tem captcha conhecido: SIM, e é o decisivo.** O formulário JazzHR da Jungler traz
`Human Check *` como campo obrigatório, e o HTML servido carrega `g-recaptcha`, `recaptcha/api.js`,
`recaptcha-field`, `recaptcha-label` e `sitekey`. **É a mesma parede que o painel já mediu duas vezes
nesta família:** a Obsidian (*"reCAPTCHA de caixa de marcar"*) e a Certain Affinity, onde
`docs/index.html` registra em 07/09 *"O 'Human Check' e reCAPTCHA v2; o clique no quadrinho NAO marcou
sozinho e abriu DESAFIO DE IMAGEM, que nao se burla. Fica A MAO"*. **Portanto: as seis linhas da
Jungler vão para a MÃO DELE, não para a automação.**

**Campos do formulário, medidos:** First Name, Last Name, Email, Phone, Address (city/state/postal),
Resume (anexo ou colado), Cover Letter, *"Are you willing to relocate?"*, LinkedIn Profile URL,
*"Website, blog or portfolio"* (obrigatório), *"What is your previous experience in production?"*
(0-2 / 3-5 / 6-10 / +10 anos), disponibilidade, Desired salary, Human Check.

**Controle de rota, para provar que os 200 são reais:** `jungler.applytojob.com/apply/zzqxNAOEXISTE/x`
devolve **410**, não 200. Os seis links abaixo devolvem 200 com corpo de ~110 KB.

### As seis linhas, em ordem de encaixe

| # | Título exato | ID de requisição | Nível no quadro | Ferramentas citadas | URL de candidatura + HTTP |
|---|---|---|---|---|---|
| **A1** | **3D Surfacing** | `LaJk360GBo` | Entry Level | Maya, **Substance**, Redshift | `https://jungler.applytojob.com/apply/LaJk360GBo/3D-Surfacing` — **200**, 110.804 B |
| **A2** | **Groom Artist** | `C6fYfcxuWg` | Entry Level | Maya, **Yeti** | `https://jungler.applytojob.com/apply/C6fYfcxuWg/Groom-Artist` — **200**, 110.761 B |
| **A3** | **3D Look Dev** | `KvYb9uJMHM` | Entry Level | Maya, Redshift | `https://jungler.applytojob.com/apply/KvYb9uJMHM/3D-Look-Dev` — **200**, 110.763 B |
| **A4** | **3D Modeling - Environments** | `vao65i7Ttc` | **Mid Level** | Maya | `https://jungler.applytojob.com/apply/vao65i7Ttc/3D-Modeling-Environments` — **200**, 110.855 B |
| **A5** | **3D Modeling - Characters** | `2Ft7PxD7Nn` | Student (College) | Maya, **ZBrush**, Mudbox, Photoshop | `https://jungler.applytojob.com/apply/2Ft7PxD7Nn/3D-Modeling-Characters` — **200**, 111.395 B |
| **A6** | **3D Generalist** | `p2hqhQuoBt` | Entry Level | Maya, Nuke, Unreal | `https://jungler.applytojob.com/apply/p2hqhQuoBt/3D-Generalist` — **200**, 111.570 B |

**Veredito de disciplina, com citação do anúncio:**
- A1 Surfacing: *"postuler en tant que graphiste **Surfacing 3D**"*, *"We mainly work on Maya, **Substance** and Redshift"* — texturização/surfacing, o núcleo dele.
- A2 Groom: *"apply as a **3D Groom Artist**"*, *"We mainly work on Maya and **Yeti**"* — groom é o diferencial declarado dele.
- A3 Look Dev: *"apply as a **Look Dev 3D Artist**"*, *"Maya / Redshift"*.
- A4 Environments: *"postuler en tant que **Environment Artist 3D**"* — arte de ambiente 3D.
- A5 Characters: *"apply as a **3D Character Artists**"*, *"Nous travaillons essentiellement sur **Maya / ZBrush**"* — escultura e modelagem de personagem.
- A6 Generalist: *"Jungler is currently recruiting **3D generalists**"* — o termo que o filtro de hoje tinha perdido.

**RESSALVAS HONESTAS, e são três:**

1. **Não são requisições datadas, são POOLS DE PERFIL.** O texto de cinco das seis é literalmente
   *"You have come to the right place for apply as a … ! **We will get back to you if we have a
   project to submit**"*. Vale como porta de candidatura viva com formulário completo e anexo de CV,
   **mas não como vaga aberta com vaga a preencher hoje.** O `garimpo-cgstudiomap.csv` já tinha
   registrado isso em outras palavras: *"ALTA (pool de perfis, nao vaga datada)"*.
2. **Nível declarado é baixo para o currículo dele.** A2/A3/A6 são "Entry Level", A5 é
   "Student (College)", só A4 é "Mid Level". Não é veto — é ruído de configuração do quadro em pool
   de perfil — mas se ele quiser mandar só uma, **A4 (Mid Level) e A1 (Surfacing)** são as que menos
   destoam.
3. **O texto da A6 ainda fala em "2024"** (*"des sup. 3D pour 2024"*), o que sugere anúncio não
   revisado. E a A4 tem um **erro de copiar-e-colar dos próprios donos**: o título é
   "3D Modeling - Environments" mas a versão em inglês do corpo diz *"apply as a 3D Character Artist"*.
   Registro porque muda o que ele escreve na carta.

**Regra de cadência:** seis linhas na mesma casa. **Uma por dia**, como o painel já faz.

---

## A7 — FLAMING FOWL STUDIOS · Lead 3D Artist · Reino Unido, **totalmente remoto** · WORDPRESS (porta de email)

- **Estúdio:** Flaming Fowl Studios — *"an independent studio raised from the ashes of the renowned
  Lionhead Studios"*; fez *Gloomhaven* e *Konfronto*.
- **Título exato:** **Lead 3D Artist**
- **ID de requisição:** não existe id numérico. O identificador estável é o slug da página:
  **`lead-3d-artist`** em `flamingfowlstudios.com`.
- **Cidade/país:** time majoritariamente no Reino Unido, **operação totalmente distribuída**.
- **Família de ATS:** nenhuma. **WordPress** (Elementor + Contact Form 7) com **porta de email** no anúncio.
- **URL do anúncio + código HTTP medido:** `https://www.flamingfowlstudios.com/lead-3d-artist/` — **200**, 52.435 B.
  **Controle de rota:** `https://www.flamingfowlstudios.com/zqx-nao-existe-123/` → **404** (não é site que devolve 200 pra tudo).
  **Liveness confirmada:** o link aparece no índice `https://www.flamingfowlstudios.com/jobs/` (**200**) e na home (**200**).
- **PORTA DE CANDIDATURA:** *"Please send your CV to **jobs@flamingfowl.com**"*.
- **Régua de vinte termos, texto integral (3.159 caracteres). Três acertos, os três falsos positivos:**
  - `based in` → *"Although the team is mainly **based in** the UK, we operate remotely so we would
    encourage applications from all over."* → diz onde o TIME fica **e convida gente de fora**. É sinal A FAVOR.
  - `only` → *"You will **not only** establish the visual DNA, look, and feel of our projects **but also**
    jump into development"* → o `not only… but also` que você já catalogou.
  - `only` → *"\*\*Individuals **only**, no outsource studios, no recruiters\*\*"* → **cláusula anti-agência**,
    falso positivo clássico. Ele é pessoa física, não estúdio de outsourcing.
  - Idioma local: nenhum. Pede *"Excellent verbal and written communication skills"*, sem nomear língua.
  - **Veto escrito: ZERO.**
- **SINAL A FAVOR, e é o mais forte da fila inteira:** *"we operate remotely so we would encourage
  applications from all over"* e *"with all the flexibility of working from **anywhere in the world**"*
  e *"We are a fully distributed team… currently have team members from all over Europe."*
  Este é o único da rodada que **convida explicitamente candidatura de qualquer lugar do mundo**.
- **Veredito de disciplina, com citação:** *"**Create stylised 3D** board game board and pieces and work
  with the code department to implement them in game"*, *"You will not only establish the visual DNA,
  look, and feel of our projects but also **jump into development to create and implement assets**"*,
  *"Experience **creating and implementing 3D assets in Unreal**"*. É **modelagem e criação de asset 3D
  estilizado** com responsabilidade de direção visual — não é direção de arte gráfica, não é UI,
  não é arte técnica. **Entra.** Ressalva de encaixe abaixo.
- **Faixa salarial publicada: NENHUMA** (busca por `salary`, `£`, `GBP`, `compensation`, `per annum` no
  texto integral: zero ocorrência).
- **CAPTCHA CONHECIDO NA FAMÍLIA: SIM, mas a porta desvia dele.** O site carrega **Contact Form 7 +
  Cloudflare Turnstile** (`cloudflare-turnstile-js`, `cloudflare.com/turnstile/v0/`) — é a parede que o
  painel já registrou em Curve Digital, Lipsync Post e Upsurge. **Mas o anúncio não manda usar o
  formulário: manda mandar CV para `jobs@flamingfowl.com`.** Porta de email não tem Turnstile.
  **Esta é uma linha de EMAIL, não de formulário** — pode sair pelo disparador de cartas.
- **RESSALVA HONESTA:** o produto é **adaptação digital de jogo de tabuleiro** — *"Create stylised 3D
  board game board and pieces"*. É asset 3D estilizado de verdade, mas **não é personagem nem criatura**,
  e boa parte da vaga é direção visual junto com o Lead UI Artist. O portfólio dele encaixa pelo
  estilizado e pela modelagem; não encaixa pelo tema. E é **Lead**, com pedido de
  *"games where you have helped define the artistic vision"*.

---

## A8 — FUTURE ASSOCIATE · 3D Generalist · Marrickville, Sydney, Austrália · FORMULÁRIO PRÓPRIO

**A única porta desta rodada com CAPTCHA ZERO medido.**

- **Estúdio:** Future Associate Pty Ltd — estúdio de VFX de Sydney, *"We work on major film and
  television productions"*.
- **Título exato:** **3D Generalist**
- **ID de requisição:** não há id. O identificador é o **valor do `<option>` no `<select name="position">`**:
  `3D Generalist`.
- **Cidade/país:** Marrickville, Sydney, NSW, Austrália. **Sydney — On site** (o próprio cartão da vaga diz isso).
- **Família de ATS:** nenhuma. Formulário próprio `#apply-form`, que posta para um **Google Apps Script**
  (`script.google.com/macros/s/AKfycbzH…/exec`) e para **web3forms** (`api.web3forms.com/submit`).
- **URL de candidatura + código HTTP medido:** `https://www.future-associate.com/careers` — **200**, 14.997 B.
  **Controle de rota:** `https://www.future-associate.com/zqx-nao-existe-123` → **404**.
- **Régua de vinte termos, texto integral (1.806 caracteres). UM acerto, falso positivo:**
  - `based in` → *"**Based in** Marrickville, Sydney. We work on major film and television productions"*
    → diz onde o **ESTÚDIO** fica. Catalogado.
  - **Nenhum outro dos vinte termos casa. Nenhuma exigência de idioma. Veto escrito: ZERO.**
  - Observação de honestidade: o formulário tem um campo **"City of Residence"** obrigatório. Não é veto
    escrito e nem casou na régua (`Residence` ≠ `resident`), mas **é uma pergunta que vai expor
    Olinda/Pernambuco antes de qualquer conversa.** Ele decide se vale.
- **Veredito de disciplina, com citação do anúncio:** *"**3D Generalist** — Maya, Houdini, Redshift across
  film and TV production. You cover the pipeline: **modelling**, FX, lighting, rendering. Comfortable
  working to brief and to deadline on live action projects."* Generalista com modelagem no centro —
  é o termo que o filtro de hoje perdeu, e aqui ele rende.
- **Faixa salarial publicada: NENHUMA.**
- **CAPTCHA: NENHUM, MEDIDO.** Varri o HTML servido por `recaptcha`, `hcaptcha`, `turnstile`, `datadome`,
  `cloudflare` e `sitekey` → **zero ocorrências**. O `submit` é um `fetch` direto, sem token de desafio.
  **Ressalva metodológica que eu não vou esconder:** ausência no HTML servido não é prova de que o POST
  passa; é prova de que não há desafio configurado na página. **É a linha mais barata de testar da rodada.**
- **Campos medidos, todos obrigatórios:** `position` (select), `name`, `email`, `phone`,
  `city` (City of Residence), `showreel` (URL), `message`.
- **RESSALVA HONESTA E IMPORTANTE:** **não há campo de anexo.** Não dá para mandar CV nem PDF —
  o portfólio entra como **URL de showreel** e o resto vai no `message`. E a vaga está marcada
  **"On site"**, sem menção a remoto ou a patrocínio. É VFX de cinema/TV, não jogo.

---

## A9 — GLINDA GAMES · 3D Artist · Ferntree Gully, Victoria (Melbourne), Austrália · FORMULÁRIO PRÓPRIO (Wix)

- **Estúdio:** Glinda Games PTY LTD — *"Founded by Daniel Visser following the acquisition of
  **Wicked Witch**"*; crédito em *Age of Empires II: Definitive Edition*, *MultiVersus*, *Catapult King*.
- **Título exato:** **3D ARTIST** (subtítulo do próprio anúncio: *"ART TEAM | HYBRID/REMOTE"*)
- **ID de requisição:** não há id. Identificador estável: o slug **`/jobs/3d-artist`**.
- **Cidade/país:** endereço registrado na política de privacidade: *"Glinda Games PTY LTD at
  1/43 Francis Crescent, **Ferntree Gully, Victoria, Australia**. 3156"* (grande Melbourne). Oceania, no recorte.
- **Família de ATS:** nenhuma. Site **Wix** com página de formulário própria.
- **URL do anúncio + HTTP:** `https://www.glindagames.com/jobs/3d-artist` — **200**, 681.309 B.
  **URL DE CANDIDATURA + HTTP:** `https://www.glindagames.com/jobs/apply` — **200**, 1.027.460 B,
  `<title>Job Application Form | Glinda Games</title>`.
  **Controle de rota, obrigatório em site Wix:** `https://www.glindagames.com/jobs/zqx-nao-existe-123`
  → **404**. **Não é o falso positivo da Lightroom 3D** — este Wix devolve 404 de verdade.
- **Régua de vinte termos, texto integral (3.609 caracteres): NENHUM DOS VINTE CASOU.**
  O único acerto da varredura foi a palavra `polish` do meu próprio filtro de idioma, e ela é o
  adjetivo inglês: *"You'll contribute to visual **polish**, optimization…"*, *"Contribute to **polish**
  passes"*, *"delivering **polished**, game-ready work"*. **Não é polonês. Falso positivo do filtro,
  não do anúncio.** Nenhuma exigência de idioma. **Veto escrito: ZERO.**
- **Veredito de disciplina, com citação:** *"you'll work across a wide range of asset types — from
  **environment props and set dressing** to vehicles, signage, and **occasional character or creature
  work**"*; *"**Model and texture** high-quality 3D assets"*; *"Have strong **modeling and texturing
  skills** for a variety of asset types"*; *"Most of our projects are grounded in a realistic, PBR-based
  style, though we also explore **stylised** art directions"*. Modelagem + texturização + ambiente +
  personagem ocasional, estilizado incluído. **Encaixe direto.**
- **Faixa salarial publicada: NENHUMA.**
- **CAPTCHA: NÃO ACHEI WIDGET, MAS NÃO POSSO GARANTIR.** Busca por `sitekey`, `recaptcha/api`,
  `g-recaptcha`, `hcaptcha`, `turnstile` no HTML servido da página de candidatura → **zero ocorrências**.
  A única aparição da palavra `captcha` é dentro da lista genérica `"siteFeatures":[…,"captcha",…]`
  do runtime do Wix, que **está em toda página Wix** e não é widget. **Honestamente: o Wix injeta
  reCAPTCHA invisível por JS na hora do submit em parte das contas. Veredito só com o clique.**
- **Campos medidos:** First name*, Last name*, Email*, Message*, Portfolio Link*, Type* (Programmer /
  **Artist** / Other), Cover Letter (upload), Resume* (upload). **Tem anexo de CV** — melhor que a A8 nisso.
- **RESSALVA HONESTA:** pede *"**2–4 years** of experience in professional game development"*. Ele é
  Senior; é sobrequalificado no papel, o que às vezes queima a candidatura. **Não é veto escrito**, então
  não desqualifica, mas muda o tom da carta. E o estúdio se descreve com
  *"responsible **AI-assisted workflows**"* — vale ele saber antes de escrever.

---

# B. DUPLICATAS QUE O DEDUPE PEGOU — e duas delas eu só peguei pelo NOME DA CASA

**Esta é a seção que justifica a regra que você me deu hoje.** As quatro abaixo passaram em
disciplina, escopo e régua, tinham URL 200, e **teriam entrado na fila se eu tivesse deduplicado só
por ID.** Foi o `grep` pelo NOME DA CASA que barrou.

| Casa / vaga | ID | O que o dedupe achou |
|---|---|---|
| **Floating Rock — Character Artist e 3D Environment Artist (Kyoryu), Wellington NZ** | HubSpot `f77470e8-4000-40a2-89ab-181acbf64568` | **`f77470e8` dá 0 nos quatro arquivos. O nome da casa dá 5.** `docs/index.html` linha 1945: *"Floating Rock (Character Artist, Kyoryu) - **A MAO por reCAPTCHA**, dossie pronto"*; `processados.csv` 07/09: *"**A MAO por reCAPTCHA do HubSpot** (…) o clique em Submit nao mudou a pagina"*; e `enviados.csv` linhas 721-722 registram **duas cartas já enviadas** em 07/09 (`nathan.santell@` e `hello@`). **É parede desde 07/09 e a casa já foi tocada duas vezes.** Confirmei o mecanismo hoje: o embed do HubSpot carrega `recaptcha.net/recaptcha/enterprise.js`. **Não entra.** |
| **Upsurge Studios — Character Artists, Melbourne** | sem id | `docs/index.html` linha 1383: *"**A MAO POR TURNSTILE**, e a VAGA E DA DISCIPLINA LITERAL DELE"*. Já fichada. **Não entra.** |
| **Certain Affinity — Advanced Material Artist (Vancouver e Toronto)** | `AgAMjfmeKe` e `eJTHIpzicy` | Os dois IDs estão em `docs/index.html` linha 2203, com o registro de 07/09: *"O 'Human Check' e reCAPTCHA v2; o clique no quadrinho NAO marcou sozinho e abriu **DESAFIO DE IMAGEM**, que nao se burla. Fica A MAO"*. **Detalhe novo que eu medi hoje: o TÍTULO MUDOU** — era "Senior Material Artist", hoje o quadro diz **"Advanced Material Artist"**. **Mesmos IDs, mesma requisição.** Quem deduplicar por título vai achar que é vaga nova. **Não entra.** |
| **Ars Thanea — "All Stars Come To Us!", Varsóvia (Traffit)** | `advertId 11` | `processados.csv` 07/09: *"**ENVIADA e CONFIRMADA**: All stars! Come to us! (ID 11), Varsovia, Traffit. Prova: POST 302 e URL final /public/form/thankyou/11"*. E `enviados.csv` tem duas cartas (28/08 e 03/09). **Já foi.** |
| **Spunge Games — 3D Generalist (Real-Time/UE5), Brisbane** | tsumea `2608` | `docs/index.html` linhas 473 e 1318 já registram a casa e a vaga desde 08/09. **E tem motivo extra: o anúncio no tsumea traz "Application Deadline: Monday, 31 August, 2026 - 12:00 PM" — venceu há nove dias.** A página do estúdio ainda lista a vaga; o prazo, não. **Não entra.** |
| **DNEG — Lead LookDev TD (`oLCvzfwb`), Londres** | `oLCvzfwb` | Já registrada HOJE em `processados.csv` linha 1964: *"vaga-registrada-nao-enviada… era o item A1 da caca de Jobvite da madrugada"*. **Não é achado meu.** |
| **TTK Games — Character Artist `558871` e Lead Environment Artist `559201`, Estocolmo** | 558871 / 559201 | Já na fila desde 08/09 pelo bloco B do `caca-jobvite-pinpoint.md`. Reconferi hoje: as duas **seguem no `postings.json`**. Não são novas. |
| **Obsidian — General Application** | `21Ud1IGKcj` | `docs/index.html` linha 1802 e `FILA-DO-VINI.md` linha 1256. Já fichada. |

---

# C. DESCARTADAS COM VETO ESCRITO — frase literal colada

| Casa / vaga | Frase literal que desqualifica | Termos da régua que casaram |
|---|---|---|
| **Foxie Ventures — Environment Artist, Adelaide** (`foxieventures.com/environment-artist/`, **200**) | *"If you meet the requirements, please apply with links to your best work samples… **Australia/New Zealand Permanent Residents Only.**"* | `resident` + `only`. Veto duplo, no meio do requisito. E a casa já está no painel desde 08/09. Formulário é **Contact Form 7** (WordPress). |
| **Lamplight Forest / Orchid of Redemption — Environment Artist para *Mage Drops*, Adelaide** (`lamplightforest.com/jobs.html`, **200**) | *"This is freelance work for hire, **for Adelaide residents only**."* e, reforçado no fim: *"The role will be mostly remote work-from-home, but some face to face will be necessary (**to reiterate, Adelaide residents only**)"* | `resident` + `only`, duas vezes, com a segunda escrita de propósito para não haver dúvida. Dedupe estava **limpo (0/0/0/0)** — a casa é nova, o veto é que fecha. |
| **Industrial Brothers — Senior Designer (3D Preschool Series), Toronto** (Humi, `industrialbrothers.humi.ca/job-board/designer/49602`, **200**) | *"**All candidates must be Canadian citizens or have permanent resident status and reside in Ontario.**"* e antes: *"Applicants must have a valid **CAVCO** number."* | `resident`. Veto de cidadania + residência provincial + número CAVCO. **Cai duas vezes:** fora de disciplina também — pede *"Excellent drawing and painting skills"*, *"Proficiency in industry-standard tools (Adobe Creative Suite)"*, é **design 2D** de personagem/locação, não modelagem 3D. |
| **Cause and FX — Expression of Interest, Auckland** (Workable) | Título literal: *"Expression of Interest (**NZ \| AU Right to Work ONLY**)"* | Já estava registrado em `portas-reabertas.md`. Reconfirmo, fecha a casa. |
| **BoomBit — 2D Artist, Gdańsk** (Traffit `advertId 312`) | Sem veto. **Fora de disciplina:** 2D. | — |
| **Bloober Team — Lighting Artist** (Traffit `advertId 18`) | Sem veto. **Fora de disciplina:** iluminação não está na sua lista (personagem, escultura, groom, look dev, textura, modelagem, ambiente). | — |
| **Flying Bark Productions LA — Lighting Key/Color Script Artist** (JazzHR `HcfBJpoZAy`) | Sem veto. **Fora de disciplina:** color script é 2D. As outras duas do quadro são Animation Director e Recruitment Coordinator. | — |
| **Stellar Creative Lab — Crowd Artists (`IaRPzUt4uQ`) e Crowd TD (`gKfTwrCKL7`)** (JazzHR) | Sem veto. **Fora de disciplina:** crowd é simulação/CFX, expressamente excluído no briefing. | — |
| **Warner Bros. Discovery — Advanced Level Artist, Montreal (`R000106508`) e Senior Lighting Artist, Londres (`R000106815`)** (Phenom) | Sem veto lido. **Não entram nesta fila por outro motivo, e é de método:** o `applyUrl` do próprio Phenom aponta para `warnerbros.wd5.myworkdayjobs.com`. **A porta é Workday, que é a família de outra fatia hoje.** Registro para não haver trabalho duplicado nem candidatura em duplicata. | — |
| **37Degrees Studio — Matte Painter, Wellington** | Sem veto (pede *"your visa situation for working in New Zealand"*, que é **contexto, não descarte**). **Fora de disciplina:** *"combining 2D photobashing skills with 2.5D projection setup in Nuke"* — matte painting. | — |
| **Red Thread Games, Noruega** | *"We do not currently have any open positions. **We will in the very near future** start looking for a 3D generalist to work on environment art and 3D assets"* | Não é vaga: é aviso de vaga futura. **Vale revisitar em duas semanas** — é 3D generalist + ambiente, disciplina cheia. Dedupe limpo (0/0/0/0). |
| **KeelWorks, Reino Unido** | *"While we do not currently have any specific vacancies, we are always on the lookout for talented Artists"* — espontânea por `contact@keelworks.co.uk` | Sem requisição nomeada. Dedupe limpo. Fica registrada, não entra na fila. |

---

# D. O QUE CADA FAMÍLIA ENTREGOU, MEDIDO — para a próxima rodada não refazer

## D1. JazzHR (`applytojob.com` / `applytojobs.ca`) — **a família que rendeu**

- **3.122 slugs** em `.com` e **1.409** em `.ca`. Sinal limpo: slug inexistente em `.com` devolve
  **302 para `jazzhr.com/job-seekers`**; em `.ca` devolve **404**. Quadro vivo devolve **200**.
- **21 quadros com 200 em `.com` e 2 em `.ca`.**
- **ARMADILHA MEDIDA, e ela custaria uma fila inteira: `200` no JazzHR não é quadro vivo.**
  **15 dos 21** devolvem 200 com `<title>**JazzHR - Inactive Career Page**</title>`. Caíram nessa:
  `cloudimperiumgames`, `cloudimperium`, `hello`, `infinite`, `midnightworks`, `pipeline`, `bolder`,
  `capsule`, `cube`, `king`, `miyu`, `moondoganimationstudio`, `unique`, `volta`, `xyz`.
  **É a irmã da armadilha do `important-looking-pirates` no Jobvite: tem que ler o corpo.**
- **Falsos positivos de slug genérico confirmados de novo:** `chimera` é empreiteira de defesa da DARPA,
  `playground` é cassino, `img` é seguradora médica, `squeeze` é rede de massagem, `rethink` é saúde,
  `tendril` é software, `theyard` é coworking, `hoplite` e `jpl` não são da área.
  **`playground` NÃO é a Playground Games.**
- **Quadros reais e vazios agora** (vale re-testar depois): `noodlecake`
  (*"There are no open positions at this time"*), `playableworlds` (mesma frase), `smgstudio`,
  `rocketsciencevfx`, `parallel`.
- **Quadros reais com vaga fora da disciplina:** `outplayentertainment` (só *Speculative Applications*
  `CS3Wh2`), `nextlevelgames` (Level Designer, Game Designer, Automation Engineer),
  `alkemyxinc` (só *Visual Effects Production Intern*), `zoicstudios` (General Applications + Previs +
  2D Compositor), `company3` (color e finishing), `flyingbarkproductions`, `stellarcreativelab`.
- **`kickstart.applytojobs.ca` e `sinnstudio.applytojobs.ca` devolvem 403** contra este IP —
  **`precisa-de-navegador`**, não é quadro morto.
- **CAPTCHA DA FAMÍLIA: reCAPTCHA v2 com campo `Human Check` obrigatório.** Confirmado hoje no HTML da
  Jungler e já medido pelo painel na Obsidian e na Certain Affinity (desafio de imagem). **Toda linha
  JazzHR é linha da mão do Vini.**

## D2. Traffit — API achada, e a família é seca para a disciplina

- **A API pública que eu isolei, e ela vale para qualquer locatário:**
  `https://<slug>.traffit.com/public/an/list/?limit=100&page=1` → JSON com `count` e `items`, e cada
  item traz `advertId`, `recruitmentId`, `title`, `description` completa em HTML, `applicationForm`,
  `remote`, `locations`. Achei lendo `/public/an/generateJs/`, que é o gerador do widget da página de
  carreira (`careerFront.js` monta em JS e o `curl` só vê a casca de 11 KB).
  **Isto substitui o navegador nesta família inteira.**
- **1.420 slugs. 7 quadros responderam:** `blooberteam` (4), `boombit` (2), `bossa` (2), `trust` (11),
  `arsthanea` (1), `ansharstudios` (0), `artifexmundi` (0). Slug inexistente devolve **503**.
- `bossa` é corretora polonesa, não a Bossa Studios. `trust` é falso positivo de slug genérico.
- **Zero vaga da disciplina.** A única que era da área (`arsthanea` id 11) **já foi enviada e confirmada
  em 07/09**.

## D3. iCIMS — **parede de captcha da AWS, família inteira, e isso encerra a linha**

- Testei 6 hosts (`careers-technicolor`, `careers-framestore`, `careers-dneg`, `jobs-technicolor`,
  `technicolor`, e um inexistente) × 3 caminhos = 18 requisições.
- **TODAS as 18 devolvem exatamente `405` com corpo de exatamente 2.115 bytes** — inclusive o host
  inexistente. É a assinatura de WAF que o `portas-reabertas.md` já descreve: mesmo código e mesmo
  tamanho de corpo em todo caminho.
- Li o corpo: `<title>**Human Verification**</title>` com `window.awsWafCookieDomainList` e
  `window.gokuProps` — **AWS WAF CAPTCHA**.
- **Veredito: iCIMS é inalcançável por `curl` deste IP, e é família de captcha (AWS WAF).
  `precisa-de-navegador` para descobrir E para enviar.**

## D4. Dayforce — casca de SPA confirmada, API fechada

- `jobs.dayforcehcm.com/en-US/<slug>/CANDIDATEPORTAL` devolve **200 com ~420 KB para slug VÁLIDO E
  PARA SLUG INVENTADO**. É a armadilha da casca que você descreveu no Jobvite, na forma mais pura:
  o texto renderizado é literalmente *"Job Board … Search Jobs **Loading** … Crafty Apes Website"*.
  **Contar 200 aqui produziria uma lista inteira de quadros fantasma.**
- Fui atrás da API da família, como você mandou. O que medi:
  - `__NEXT_DATA__` existe mas só tem `session` e `dehydratedState` — **nenhuma vaga embutida**.
  - `/api/loadseekdata` é **redirect de OAuth do SEEK**, não a lista de vagas (o HTML mostra
    `"SEEK_REDIRECT_URI":"https%3A%2F%2Fjobs.dayforcehcm.com%2Fapi%2Floadseekdata"`). GET dá 500.
  - **`/api/JobPosting/Search` EXISTE** — devolve `405 Method Not Allowed` em GET, que é o sinal de que
    a rota é POST. **Mas todo POST devolve `403 Forbidden` em texto puro**, com e sem `Origin`/`Referer`
    corretos — e não é o proxy: o próprio Dayforce responde JSON de erro (`httpstatuses.io`) nas outras
    rotas, e este devolve texto seco. É WAF.
  - `sitemap.xml`, `/rss`, `/feed`, `FeedRss` e `JobRss`: **404** (com a mesma casca de 280 KB).
  - `marz.dayforcehcm.com` (portal por instância) é **rejeitado no CONNECT pelo proxy**.
  - O portal legado `globalus63.dayforcehcm.com/CandidatePortal/en-US/craftyapes` responde **200 com
    434 KB e a palavra "Loading"** — mesma casca.
- **Veredito: Dayforce é `precisa-de-navegador` para listar. A rota da API está identificada
  (`POST /api/JobPosting/Search`) para quem for tentar com sessão de navegador.**

## D5. SuccessFactors — a régua de liveness que eu achei, e ela **desmente o sitemap**

Isto é o achado de método mais caro da rodada, e ele **poderia ter me feito entregar duas vagas mortas
como fila.**

- O grupo **Pitch Black Company** (dono da **Folks VFX** e da **Rising Sun Pictures**) usa
  SuccessFactors/jobs2web em `careers.pitchblackcompany.com`, `careers.rsp.com.au` e `careers.folksvfx.com`.
- **O `sitemap.xml` das três (idêntico, 3.668 B, `lastmod 2026-09-05`) lista 17 vagas, e duas são
  exatamente a disciplina dele, em Adelaide (Oceania, no recorte):**
  - `rsp/job/Adelaide-**Senior-Modelling-Artist**-SA-5000/**603269517**/`
  - `rsp/job/Adelaide-**Senior-Look-Development-Artist**-SA-5000/**605921817**/`
- **As duas páginas respondem 200.** A Senior Modelling Artist renderiza o anúncio **inteiro**,
  server-side, 3.669 caracteres de corpo real: *"We are looking for a Senior Modeller to join our team
  on a 12 month contract, in our Adelaide studio!"*, *"Advanced knowledge of industry-standard modelling
  and sculpting tools, including **ZBrush, Mudbox, UVLayout and TopoGun**"*, *"Strong understanding of
  topology, UV layout, asset optimisation and modelling requirements for rigging and look development"*.
  **Régua de vinte termos no corpo do anúncio: NENHUM CASOU.** (Na página inteira casam `français` e
  `español` seis vezes — é o **seletor de idioma do site**, falso positivo puro.)
- **E MESMO ASSIM EU NÃO PONHO NA FILA. O motivo, medido:**
  1. O `postings`/listagem do jobs2web é **server-side** — provei com um controle: `careers.paramount.com/search/?q=`
     (mesmo motor, mesmo código) devolve **25 links `href="/job/…"` no HTML cru**.
  2. `careers.rsp.com.au/search/?q=&locationsearch=&searchResultView=LIST` e
     `careers.pitchblackcompany.com/search/?q=` devolvem **ZERO links `/job/`**. O quadro está vazio.
  3. A página de vaga **não serve como prova de vida**: puxei quatro requisições antigas do mesmo sitemap
     (`601539617` CFX Supervisor, `604340717` Compositing Artist, `605922117` Senior Animator,
     `605703117` Senior FX Artist de Mumbai) e **todas renderizam corpo completo igual**.
  4. A rota de candidatura `career17.sapsf.com/career?career_ns=job_application&company=artistesfo&career_job_req_id=<id>`
     devolve **a mesma tela de Sign In (200, ~200 KB) até para o id inventado `999999999`** — não discrimina.
- **Isso CONFIRMA o registro de 08/09 do painel** (*"QUADRO DO GRUPO VAZIO, medido com navegador… os tres
  devolvem 'No jobs found'"*). **A regra que fica escrita: no SuccessFactors/jobs2web, prova de vida é a
  listagem `/search/?q=` renderizada server-side, com links `/job/`. Sitemap e página de vaga são cache
  velho e mentem.** Se alguém contar sitemap como fila, entrega vaga morta com anúncio bonito.
- **CAPTCHA DA FAMÍLIA: SIM.** A tela de candidatura exige **conta** (*"Not a registered user yet? Create
  an account to apply"*) e o HTML servido traz `ReCaptcha`, `captchaImg` e `CaptchaDisable`.
  **SuccessFactors = conta + captcha. Linha da mão dele, sempre.**
- Dedupe da casa, para o registro: `enviados.csv` linha 216 mostra carta para `recruitment@rsp.com.au`
  em 02/09, e `processados.csv` 1452 um follow-up em 07/09. **A casa já foi tocada duas vezes por email.**

## D6. Phenom — confirma o registro de hoje: **é vitrine, não porta**

- `careers.wbgames.com` responde 200 mas **é redirecionamento de marca para `careers.wbd.com`**
  (Warner Bros. Discovery), que é o locatário Phenom de verdade.
- Li o blob `eagerLoadRefineSearch` do HTML (a técnica que o painel já registrou na Beenox), com duas
  buscas: `artist` → **2 vagas no mundo inteiro**; `character` → 325 hits, 10 na primeira página, nenhuma
  da disciplina.
- **As duas de `artist` levam para `warnerbros.wd5.myworkdayjobs.com`.** Confirma a lição de hoje:
  achar front-end novo não é achar porta nova.
- `careers.paramount.com`, `careers.folksvfx.com` e `careers.pitchblackcompany.com` **não são Phenom**
  (não têm `eagerLoadRefineSearch`) — são SuccessFactors, ver D5.

## D7. Factorial, Avature, Eightfold, Humi, eRecruiter — **zero, e agora está medido**

- **Factorial:** 1.367 slugs. Slug inexistente = **404** limpo. **7 locatários acharam**, e o padrão é
  redirect 302 para o domínio do país (`factorial.it`, `factorial.es`, `factorialhr.co`, `factorialhr.de`).
  Os sete: `34bigthings` (Itália — só página de time, **zero vaga**), `chibig` (Valência — zero vaga),
  `illusorium-studios` (só aponta para o site próprio), `copernicus` (é gestora imobiliária, homônima),
  `mago-production` (audiovisual espanhol, zero vaga da área), `vea` (associação alemã de energia,
  homônima), `usert38`, `nexus`. **`gamehouse` (Barcelona) tem exatamente um Intern e uma Open application.**
  **Zero da disciplina.**
- **Avature:** 1.367 slugs, **todos `000` (DNS não resolve)**. Validei o sinal com locatários reais
  (`pwc.avature.net` e `siemens.avature.net` resolvem e devolvem 404 em `/careers`). **Nenhum estúdio da
  campanha tem locatário Avature. Linha fechada.**
- **Eightfold:** 1.367 slugs, **um único não-`000`**, e é `trust` (slug genérico) com **404**. Validei o
  sinal com `nvidia.eightfold.ai` e `vodafone.eightfold.ai`, que devolvem 200. **Zero. Linha fechada.**
- **Humi:** 1.411 slugs. **Sinal de negativo: corpo 200 com o texto `Job Board Not Configured`.**
  **Um único quadro real: `industrialbrothers`** (Toronto), com 2 vagas — a Senior Designer vetada em §C
  e uma General Application de fevereiro de 2022. **Cuidado com o falso positivo de rede:** 46 slugs
  "bateram" na primeira passada só porque o corpo voltou **vazio** por timeout; reconferidos um a um
  (`zoic`, `rocksteady`, `microids`, `theastronauts`, `rising-sun-pictures`), **todos são
  `Job Board Not Configured`**. Contar corpo vazio como quadro vivo produziria 46 casas fantasma.
  **Rota real do detalhe de vaga no Humi, para quem vier depois:** `https://<slug>.humi.ca/job-board/<categoria>/<id>`
  — os links do índice são **relativos e quebram** se colados direto no domínio (devolvem 404 JSON da API do Humi).
- **eRecruiter:** não é família de quadro público. O que existe no repositório são **URLs de formulário
  individual** (`form.erecruiter.pl/form/<hash>` e
  `system.erecruiter.pl/FormTemplates/RecruitmentForm.aspx?WebID=<hash>`), sem índice, sem slug de
  empresa e sem API de listagem. **Não há como varrer: o hash é a única chave.** Linha fechada por
  ausência de superfície, não por ausência de vaga.

## D8. Jobvite e Pinpoint — re-conferidos, e **nada novo desde a madrugada**

- **Jobvite:** re-enumerei o único quadro da área, `double-negative-visual-effects`: **101 ids hoje**
  (eram 100 na madrugada). **Correção útil ao registro anterior: o quadro `/jobs` é legível por `curl`,
  título por título — não precisa de navegador para listar.** Reconferi os três que a madrugada tinha
  deixado em aberto: `oLwkzfwU` Character Modeler é **Mumbai + Chennai + Bengaluru** (Índia, fora),
  `ozOyAfwf` é **Assistant Editor** (editorial, fora), `oEfvAfwI` é **Unreal Rigging Supervisor**
  (rigging, fora). **Nenhuma vaga nova da disciplina.**
- **Pinpoint:** re-testei os 10 quadros vazios da madrugada — **os 10 continuam em `{"data":[]}`**
  (`tripledotstudios`, `gameplaygalaxy`, `buildarocketboy`, `everi`, `amber`, `flixinteractive`,
  `playground-games`, `ruckus-games`, `singularity6`, `suncreature`).
- **Mudança de estado que vale registrar: `kwalee` passou de 0 para 3 vagas hoje — e as três são a
  trinca de DEMONSTRAÇÃO** (`Head of DEI - UK | London`, `Marketing Manager | Paris`,
  `Customer Service Rep | New York`). **Não é quadro que encheu, é quadro que ganhou dados de exemplo.**
  A armadilha do relatório da madrugada acabou de se provar viva.
- `rocksteady` (5) e `pipeworks` (8) reconferidos: **zero da disciplina**, igual à madrugada.

## D9. Formulário próprio de WordPress — 1.406 páginas lidas

- Fonte: as `porta-ok:` já confirmadas em `fila-gamedevmap-europa*.csv`, `-canada`, `-ch-fi-nl`,
  `-se-dk` e o campo `quadro` de `fila-oceania.csv` → **1.406 URLs únicas, 1.378 responderam,
  1.364 com corpo real.**
- Filtro por 23 padrões da disciplina, **incluindo `generalist` e `general artist`** como você mandou →
  **33 páginas com acerto.** Delas saíram as linhas A7, A8 e A9, mais os vetos da §C.
- **`generalist` rendeu sozinho quatro dos achados** (Future Associate, Spunge, Red Thread, KeelWorks).
  O buraco que você apontou era real.
- **Descartadas por não serem estúdio ou não serem vaga:** `prospereducation`, `supersphera`
  (só descrição de serviço), `binaryspacegames` (post de blog), `sperasoft` (bootcamp/estágio),
  `quelsolaar`, `beardenvy` (blog de barba — "Powerhouse Generalist" é piada),
  `schleuder.games`/`lucernal`/`sutur` (a palavra aparece em **bio de funcionário**, não em vaga),
  `superplusgames` (bio de time), `staplesvr` (página de time), `qxrstudios` (slogan
  "WE ARE WORLD BUILDERS"), `gameslab` (vaga de QA de 2018), `funpunchgames` (Unity dev),
  `chucklefish`, `wargaming`, `tally.so/r/RGRv7d` (formulário de programador), `hashbane` (BambooHR —
  família de outra fatia), `causefx.nz` (veto já conhecido), `digitalconfectioners` (o painel registra
  em 07/09 que **já virou candidatura**), `foxiegames`/`greasemonkeygames` (depoimentos, e a Foxie tem
  veto escrito), `flamingfowlstudios/jobs-producer` (produção — mas foi por essa página que cheguei ao
  **Lead 3D Artist**, que é a A7).

---

# E. TRÊS LIÇÕES DE MÉTODO QUE ESTA RODADA MEDIU

1. **`200` continua não sendo porta, e agora tenho três formas novas da mesma mentira.**
   O JazzHR serve **`Inactive Career Page` com 200** (15 de 21 quadros!). O Dayforce serve **a mesma
   casca de 420 KB para slug válido e inventado**. O Humi serve **200 com `Job Board Not Configured`**,
   e ainda por cima o corpo **vazio por timeout** passa em qualquer filtro que só procure ausência de
   frase. **Todo filtro de quadro vivo tem que exigir corpo E conteúdo, nesta ordem.**

2. **Sitemap não é quadro, e o SuccessFactors provou isso da pior maneira.** Duas vagas perfeitas da
   disciplina, em Adelaide, com anúncio inteiro renderizado e 200 na URL — e a listagem server-side da
   mesma casa devolve zero, com um controle (Paramount, 25 links) provando que a listagem funciona
   quando há vaga. **A prova de vida é a listagem, não o sitemap nem a ficha.**

3. **O `grep` pelo NOME DA CASA salvou quatro linhas desta fila, e o `grep` por ID teria falhado nas
   quatro.** Floating Rock (`f77470e8` → 0 nos quatro arquivos; `Floating Rock` → 5 ocorrências, incluindo
   duas cartas enviadas e um diagnóstico de reCAPTCHA de 07/09), Upsurge (Turnstile), Certain Affinity
   (**o título mudou de "Senior" para "Advanced Material Artist", com os mesmos dois IDs**) e Spunge
   (prazo vencido em 31/08). **A regra que você me deu hoje custou quatro cliques desperdiçados a menos.**

---

# F. RESUMO DE CAPTCHA, porque é o que decide quem clica

| Linha | Família | Captcha | Quem envia |
|---|---|---|---|
| **A8 Future Associate** | formulário próprio + Google Apps Script + web3forms | **NENHUM medido** (zero `recaptcha`/`hcaptcha`/`turnstile`/`sitekey` no HTML) | **automação pode tentar** |
| **A9 Glinda Games** | Wix | **sem widget no HTML**; só a palavra `captcha` na lista genérica `siteFeatures` do runtime Wix. Wix injeta reCAPTCHA invisível em parte das contas | **tentar; veredito no clique** |
| **A7 Flaming Fowl** | WordPress (o site tem CF7 + **Cloudflare Turnstile**) | **a porta do anúncio é EMAIL** (`jobs@flamingfowl.com`) e desvia da parede | **email, não formulário** |
| **A1-A6 Jungler** | JazzHR | **reCAPTCHA v2, campo `Human Check` obrigatório** — mesma parede medida na Obsidian e na Certain Affinity, com desafio de imagem | **MÃO DO VINI** |
| (Floating Rock) | HubSpot | **reCAPTCHA Enterprise** (`recaptcha.net/recaptcha/enterprise.js` no embed) | mão, já fichado 07/09 |
| (iCIMS, família inteira) | iCIMS | **AWS WAF "Human Verification"** em todo host e todo caminho | navegador, para tudo |
| (SuccessFactors) | SAP SF | **conta obrigatória + `ReCaptcha`/`captchaImg` no HTML** | mão |
| (Dayforce) | Dayforce | listagem inacessível; API POST 403 por WAF | navegador |

---

# G. ONDE EU PARARIA DA PRÓXIMA VEZ

1. **Clicar a A8 (Future Associate) primeiro** — é a única porta da rodada sem captcha e custa um clique.
2. **A9 (Glinda) em seguida** — tem anexo de CV e o Wix pode não ter desafio.
3. **A7 (Flaming Fowl) pelo disparador de cartas** — é email, e é a única vaga da fila que **convida por
   escrito candidatura de qualquer lugar do mundo**.
4. **Jungler: uma por dia, na mão dele**, começando por **A1 (3D Surfacing)** ou **A4 (Environments,
   Mid Level)**.
5. **Re-testar `redthreadgames.com/jobs` em duas semanas** — o próprio anúncio diz que vão abrir 3D
   generalist de ambiente *"in the very near future"*, e o dedupe está limpo.
6. **JazzHR merece mais uma passada de slug** — foi a família que rendeu, e dos 3.122 slugs testados
   os acertos vieram quase todos de nomes de estúdio de VFX/animação. **Vale cruzar com o
   `censo-boards-0809.csv` e com `fila-gamedevmap-europa*.csv`, que eu não slugifiquei.**
7. **Não gaste rodada em Avature, Eightfold, Factorial, Traffit, eRecruiter e Humi.** Estão medidos e
   estão secos para esta disciplina, com o número ao lado de cada um em §D7.
