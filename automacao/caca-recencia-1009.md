# Caça por RECÊNCIA — janela de 24 horas — 10/09/2026, 02h36 UTC

**Para a virada das 03h00 UTC.** Só `curl` + `python3`. **Nenhum navegador aberto, nenhum
Playwright, nenhum commit, nenhum push, nenhum email, nenhum formulário preenchido.**
`docs/index.html`, `enviados.csv`, `automacao/processados.csv` e `automacao/FILA-DO-VINI.md`
foram **lidos e nunca tocados**. Este arquivo é o único que nasceu na rodada.

**Janela usada:** publicadas a partir de **2026-09-08T22:36-04:00** (24 horas cheias contadas da
hora em que a rodada começou, 2026-09-10T02:36 UTC). O corte foi medido nos dois sentidos: alargar
para 08/09 22h36 **não trouxe nenhuma vaga a mais** que o corte de 09/09 00h00 no Greenhouse, então
a janela de 24h e a janela "09/09 em diante" são o mesmo conjunto nesta rodada.

---

## PLACAR

| Medida | Número |
|---|---|
| Quadros **Greenhouse** consultados pela listagem barata `/jobs` (minha lista) | **56 slugs**, **55 vivos (200)**, 1 morto (404) |
| Vagas Greenhouse lidas na listagem | **1.982** |
| Quadros Greenhouse extras reconferidos por mim (o scratchpad tinha arquivo de outro agente — ver §4.8) | **26 slugs**, 21 vivos, **376 vagas** |
| Sondagem de slugs Greenhouse novos (varredura de nomes de estúdio) | **100 slugs**, 3 vivos, **os 3 falso-amigo** |
| **Greenhouse publicadas na janela (`first_published`)** | **45** |
| Corpos Greenhouse recentes lidos por inteiro | **45 de 45** |
| Quadros **Workday** paginados 100% | **7** (`disneycareer` 635, `disneycareerdc` 650, `warnerbros/global` 332 nas 4 primeiras páginas ordenadas por data, `pixar` 3, `sega` 28, `unitytech` 124, `aristocrat` 179, `spinmaster` 54) |
| Vagas Workday lidas | **2.005** |
| **Workday com `postedOn` = Today/Yesterday** | **193** (127 Disney + 33 Warner + 22 Unity + 5 Aristocrat + 5 Spin Master + 1 SEGA) |
| Quadros **SmartRecruiters** (inclui NBCU/DreamWorks, regra 14) | **14**, 1.361 vagas, **58 recentes** |
| Quadros **Lever** | **15**, 250 vagas — **recência NÃO medível, ver §4.4** |
| Quadros **Ashby** | **6**, 112 vagas, **4 recentes** |
| Quadros **Teamtailor** | **29**, 156 vagas, **1 recente** |
| Quadros **Recruitee** | **5**, 62 vagas, **0 recentes** |
| Quadros **Breezy** | **3**, 37 vagas, **1 recente** |
| **Netflix (Eightfold)** — 9 termos de busca | **0 recentes** (o `t_create` mais novo do quadro inteiro é **2026-08-24**) |
| **Da disciplina, no escopo, sem veto escrito e inédita nos quatro arquivos** | **1** |
| Descartadas com frase colada | **3** |
| Sem veredito medido, e digo por quê | **0** |

**A fila tem UMA linha.** Não inflei. Zero medido vale mais que fila inventada, e o que sustenta a
linha única está na §6: em 24 horas, as sete famílias inteiras produziram **193 vagas Workday +
45 Greenhouse + 58 SmartRecruiters + 4 Ashby + 1 Teamtailor + 1 Breezy = 302 publicações**, e
**o mundo fez UMA vaga da disciplina dele dentro do recorte geográfico**.

---

# 1. A FILA — uma linha

### 1. Riot Games · `Principal 3D Character Artist - Unpublished R&D Product`

| Campo | Valor medido |
|---|---|
| **Estúdio** | Riot Games |
| **Título exato** | `Principal 3D Character Artist - Unpublished R&D Product` |
| **ID de requisição** | **`8163170`** · **`internal_job_id` `3532778`** |
| **Cidade/País** | **Los Angeles, EUA** (campo `offices` traz só `Los Angeles, USA`; sem localização alternativa — `Additional Location` = `null`) |
| **Família de ATS** | **Greenhouse** (board `riotgames`) — família **provada**, com duas candidaturas da campanha já aceitas neste mesmo board em 03/09 |

**URLs, com código HTTP medido AGORA nesta rodada:**

| URL | HTTP medido |
|---|---|
| `https://job-boards.greenhouse.io/embed/job_app?for=riotgames&token=8163170` | **200** ← **é por aqui que se clica** |
| `https://boards.greenhouse.io/embed/job_app?for=riotgames&token=8163170` | **301 → 200** no link acima |
| `https://www.riotgames.com/en/work-with-us/job/8163170?gh_jid=8163170` | **200** (o anúncio) |
| `https://job-boards.greenhouse.io/riotgames/jobs/8163170` | **302** → redireciona para `riotgames.com` (**não é 403 como na Epic**, mas prefira o embed) |
| `https://boards-api.greenhouse.io/v1/boards/riotgames/jobs/8163170` (corpo integral) | **200** |

**DATA DE PUBLICAÇÃO, COM A FONTE:**
`first_published` = **`2026-09-09T18:51:43-04:00`** = **2026-09-09 22h51 UTC**, ou seja **três horas
e quarenta e cinco minutos antes desta rodada**. Fonte: campo `first_published` da listagem
`https://boards-api.greenhouse.io/v1/boards/riotgames/jobs` (o campo barato, sem `content=true`).
**`updated_at` é o mesmo carimbo** (`2026-09-09T18:51:43-04:00`), então **não é republicação de
requisição velha** — é requisição nova de verdade.
**Ela é posterior à rodada de recência de 09/09** (`caca-wd-gh-recencia-0909.md`, escrito às 20h31
UTC): aquela rodada leu o board `riotgames` inteiro e registrou por escrito *"Riot Games (163 vagas,
so Principal Concept Artist de ambiente e personagem, que e concept 2D)"*. **Esta vaga ainda não
existia quando aquela varredura rodou.**

**RÉGUA DE VINTE TERMOS, rodada frase a frase sobre o anúncio INTEGRAL — UM acerto no corpo, e é
falso positivo catalogado:**

- `within the` → *"As a **Principal 3D Character Artist within the Research & Development** team,
  you'll work on a new unpublished AAA game."* → **`within the` de time, não de território.**
  Falso positivo já catalogado no briefing (`within the industry/team`).
- **NÃO aparecem no corpo:** `authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`,
  `based in`, `only from`, `LMIA`, `days a week`, `days per week`, `days in the office`, `resident`,
  `relocat`, `located in`, `unable to support`, `no relocation`, `x a week`, `x per week`, `only`.
- **Buraco da régua também rodado** (a lição da ILM de 09/09): regex `days?.{0,25}(per week|a week)`
  → **zero acertos**. Não há cláusula de presença escrita de nenhuma forma.
- **Idioma local:** regex de `french|german|korean|japanese|swedish|spanish|dutch|bilingual|native
  speaker|fluent in` → **zero acertos**. Não há exigência de idioma.
- **VETO ESCRITO: ZERO.**

**Os acertos que EXISTEM estão nos metadados estruturados do Greenhouse, e os três jogam A FAVOR
dele — leia, porque é o achado mais forte da linha:**

```
Visa Eligible        = True
Relocation Package   = Platinum
Relocation Eligible? = None
Job Family Group     = Art
Craft                = Art
```

`eligib` e `relocat` batem na régua **dentro dos campos `Visa Eligible: true` e
`Relocation Package: Platinum`**. Isso é **oferta, não veto** — é a Riot declarando, em campo
estruturado do próprio ATS, que **a vaga patrocina visto e paga mudança no nível mais alto da
tabela deles**. É o falso positivo catalogado de `relocation assistance` que é oferta, na sua forma
mais literal. O acerto de `only` é o rótulo da faixa salarial, `"(Los Angeles Only) Base salary
range…"`, que diz **onde a faixa vale**, não quem pode se candidatar.

**DEDUPE, E FIZ OS DOIS — pela ferramenta pronta, `sh automacao/dedupe-agora.sh 8163170 "Riot"`:**

*(1) Por ID de requisição, lendo TODAS as ocorrências até o fim da célula:*

| Arquivo | `8163170` | `3532778` (internal) |
|---|---|---|
| `enviados.csv` | **0** | **0** |
| `automacao/processados.csv` | **0** | **0** |
| `docs/index.html` | **0** | **0** |
| `automacao/FILA-DO-VINI.md` | **0** | **0** |

Saída literal da ferramenta: *"(nenhuma — o ID é inédito nos quatro arquivos)"* e
*"(nenhuma marca de envio)"*. Nenhum `/confirmation`, nenhum `ENVIADA`, nenhum
`Thank you for applying` colado ao ID.

*(2) Pelo NOME DA CASA — e aqui a ferramenta trouxe coisa que MUDA como você escreve a carta:*

- **NÃO É PAREDE.** Registro de 04/09 em `processados.csv`, medido sem enviar nada:
  *"Teste sem enviar nada mediu se cada board carrega reCAPTCHA: Imageworks e 2K carregam (objeto
  grecaptcha definido e iframe do desafio na pagina), **Epic e Riot nao**. Isso explica o placar
  real: as candidaturas de Epic (tres) e **Riot (duas) passaram em 03/09**."*
- **Duas candidaturas anteriores nesta casa, as duas aceitas**, em 03/09: Principal Concept Artist
  Environment/Character `8070799` e Senior Art Outsourcing Manager Weapon Concept `8003925` — as
  duas com *"tela de confirmacao; codigo de seguranca lido no Gmail"*. **Esta seria a terceira.**
- **RECUSA DE ONTEM À NOITE, e ela é a ressalva grande.** `processados.csv`, linha datada
  `2026-09-10`: *"**RECUSA as 23h09** na Principal Concept Artist, Environment/Character de League
  of Legends, Los Angeles: '**After reviewing, we have decided to pursue other candidates at this
  time.**' Endereco no-reply, entao SO REGISTRO, sem resposta."* Ou seja: a recusa caiu **~3h30
  antes desta rodada**, e a vaga nova foi publicada **~18 minutos antes da recusa chegar**.
- **Duas tentativas por email pessoal quicaram** em 05/09 (`ybourykina@`) e 06/09 (`kbourykina@`);
  a terceira, `barmitage@riotgames.com`, saiu em 07/09 e está sem resposta.
- **Riot NÃO está na lista de casas com cadência ocupada em 09/09** (Epic, Blizzard/Activision,
  Makeshift, Netflix, Eyeline, Disney/ILM, Sony Pictures Imageworks, 2K/Cloud Chamber, Hasbro,
  Airship, Mob Entertainment, ustwo games). **Sem trava de ritmo.**

**Armadilha da Epic conferida** (mesma requisição publicada duas vezes com IDs diferentes): varri as
147 vagas do board `riotgames` procurando outro anúncio com `internal_job_id` **3532778** →
**apenas um**. Não é anúncio duplicado.

**VEREDITO DE DISCIPLINA, com citação do corpo — é o centro do portfólio dele, não a borda:**

> *"you will bring characters to life by crafting and **texturing high fidelity models**"*
> *"Your **sculpting and texturing** skills, artistic eye, and understanding of **anatomy, form, and
> color** will make you one of our key **style advocates**"*
> *"Produce the look and feel of **high fidelity 3D characters** and cosmetic assets"*
> *"8+ years of **character modeling** experience as a Senior or Principal Artist"*
> *"Strong experience working with **modeling, sculpting and texturing** programs such as **Maya,
> Zbrush, and Substance Painter**"*
> *"Deep knowledge of **human anatomy**, form, and color theory"*
> *"A portfolio that shows a **range of character styles and fidelities**"*
> *"You will be a **mentor to other character artists** and support the upholding and sometimes
> creation of **style guides**"*

Escultura + modelagem + texturização de personagem, com o ferramental exato dele (Maya, ZBrush,
Substance Painter), pedindo **variedade de estilos** e **defensor de estilo** — que é o registro
estilizado dele — e com mentoria, que é o nível de 10+ anos. **Sem CFX, sem arte técnica, sem
conceito 2D.**

**FAIXA SALARIAL PUBLICADA** (campo `Location Range 1` do metadata do anúncio):
> *"(Los Angeles Only) **Base salary range between $166,600.00 - $232,800.00 USD** + incentive
> compensation + equity + 401K with company match + medical, dental, vision, and life insurance +
> short and long-term disability + open PTO."*

**RESSALVA HONESTA — quatro pontos, e o primeiro é o que pode te fazer segurar:**

1. **A recusa da Riot chegou há três horas e meia.** É outra requisição (a Principal Concept Artist
   `8070799`, conceito 2D, que entrou pela estratégia de porta de entrada) e é recusa de `no-reply`
   sem menção a visto — não é porta fechada da casa. **Mas é o mesmo padrão do caso Swaybox**, onde
   a campanha decidiu por escrito não bater na irmã depois de uma recusa recente. A diferença aqui:
   lá era a **mesma disciplina** e a mesma sub-casa; aqui a recusada é **conceito 2D** e esta é
   **modelagem de personagem 3D**, com `Job Family Group = Art / Craft = Art`. Decisão sua. Se for,
   eu escreveria a carta reconhecendo a candidatura anterior e marcando a diferença de disciplina.
2. **`Extensive Unreal Engine 5+ experience` é requisito obrigatório, não desejável.** Se o UE5 dele
   é de uso e não de produção pesada, esse é o ponto fraco declarado do currículo contra este
   anúncio. **Não é veto**, é encaixe.
3. **`8+ years of character modeling experience as a Senior or Principal Artist in the gaming
   industry`** — ele tem 10+ anos, mas parte forte do registro é **cinema/TV** (Wingfeather Saga,
   Angel Studios). Os créditos de jogo (Endstar, E-Line Media) contam, mas o anúncio escreve
   "in the gaming industry" com todas as letras.
4. **Grooming em Houdini não aparece no anúncio.** O diferencial de apoio dele não é pedido aqui;
   o que é pedido é escultura, modelagem e textura. Não pesa contra, só não pesa a favor.

**Captcha da família:** o board `riotgames` do Greenhouse foi medido em 04/09 pela campanha como
**SEM** o desafio (*"Epic e Riot nao [carregam]"*), e as duas candidaturas de 03/09 passaram por ali.
**Ressalva de método na minha própria medição:** eu reconferi hoje baixando a página do embed
(90.172 bytes, HTTP 200) e o objeto **`grecaptcha` aparece 0 vezes**; mas a página traz, no bloco de
configuração global do renderizador do Greenhouse, `GOOGLE_RECAPTCHA_INVISIBLE_KEY` e
`GOOGLE_RECAPTCHA_ENDPOINT: https://www.recaptcha.net/recaptcha/enterprise.js`. **Isso é a config da
plataforma, que vem em toda página `job-boards.greenhouse.io`, e não prova que este board ativa o
desafio** — a distinção entre board com e sem desafio é um teste de *runtime*, que só o navegador
faz. **Curl não decide isso.** O que decide é o registro de 04/09 + os dois envios aceitos.
O Greenhouse manda **código de segurança por email**, então tenha o Gmail aberto.

---

# 2. DESCARTADAS COM FRASE COLADA DO ANÚNCIO

Nenhum descarte por disciplina sem citação. Quando não consegui o corpo, digo isso em vez de
descartar.

### 2.1 AGBO — `Sr. Cinematic Layout Artist` — `5487a9089f02` — Raleigh, NC, EUA
**Breezy** · publicada **2026-09-09T14:16:59Z** (campo `published_date` do feed `/json`) ·
`https://agbo.breezy.hr/p/5487a9089f02-sr-cinematic-layout-artist` → **HTTP 200** ·
departamento `GAMES` · `salary` vem **vazio**.
Casa nova para a campanha, dedupe do ID limpo. **E mesmo assim cai por disciplina, com o corpo lido
por inteiro:**

> *"AGBO is seeking a Senior Cinematic Layout Artist to help bring our in-game cinematics to life
> with strong **staging, camera work, and visual storytelling**."*
> *"Build and refine cinematic sequences in Unreal Engine using **Sequencer**, establishing **shot
> composition, camera blocking, and pacing**"*
> *"**Frame and animate cameras** to support storytelling intent, emotional beats, and gameplay
> context"*

Contagem literal no corpo: `layout` **21**, `camera` **10**, `staging` **4** — e
`model` **0**, `sculpt` **0**, `texture` **0**, `Maya` **0**, `ZBrush` **0**, `character` **0**.
**É cinematografia e câmera, que está na lista de exclusão por escrito.** Não é modelagem, não é
textura, não é personagem.

### 2.2 Hasbro — `Assoc Graphic Designer (3D Focus)` — `4398927009` — **Hong Kong**
**Greenhouse** · publicada **2026-09-09T22:31:04-04:00** — **a mais recente das 45**, e por título
seria candidata forte (`3D Focus`, e o corpo bate em `blender`, `maya`, `zbrush`).
**FORA DO ESCOPO GEOGRÁFICO:** Hong Kong não é América do Norte, Europa, Oceania, Coreia do Sul nem
Singapura. Cai antes da disciplina. Registro porque é a prova de que a leitura de corpo funcionou —
um filtro de título de "graphic designer" teria descartado por motivo errado.

### 2.3 Gameloft — `3D Environment Supervisor` — `744000148441789` — **Yogyakarta, Indonésia**
**SmartRecruiters** · publicada **2026-09-09T08:40:47Z**.
Disciplina certa (arte de ambiente 3D, supervisão). **FORA DO ESCOPO GEOGRÁFICO:** Indonésia não
está no recorte — na Ásia só Coreia do Sul e Singapura.

### 2.4 ILM Londres — `FaceSwap Artist - all levels - London Studio` — `10160278` — **NÃO É MINHA E CAI POR DISCIPLINA**
Casa da **regra 14**, e é exatamente o caso que o briefing cita como "escaparia de qualquer filtro
de disciplina". **Fui ler o corpo. Cai, e agora com frase colada:**

> *"FaceSwap is a new… discipline within the visual effects industry, using **Machine Learning (AI)**
> to create digital faces and likenesses."*
> *"**Working knowledge of Nuke** to prepare **precomps and slap comps**"*
> *"**Some experience with CG compositing**"*
> *"Familiarity with **ComfyUI and other GenAI tools**"*
> *"Interested in, or have basic familiarity with, **deep neural networks**"*
> *"Any experience using or training deep neural networks models, such as **Nuke Copycat,
> DeepFaceLab**"*

É **composição em Nuke + treino de rede neural**, não modelagem, escultura, groom, look dev nem
texturização. Zero menção a ZBrush, Maya, Substance, topologia ou UV.

**E ela também está fora da janela de 24h, medida pelo método do briefing:**
`postedOn` da listagem diz **"Posted Yesterday"**, mas o **rodapé do corpo traz `Date Posted:
2026-09-08`** e o `startDate` da API confirma **2026-09-08**. Cruzamento feito, os dois batem.
**E ela já está registrada por outra rodada:** `processados.csv` traz 3 ocorrências, entre elas
*"10160278, publicada em 08/09, canApply true, **ADIADA PARA A PROXIMA RODADA e nao descartada**.
Regua de vinte termos no texto integral: ZERO acertos, nenhum veto"*. **Não é achado meu; confirmo
que continua viva e com `canApply: true`, e acrescento o veredito de disciplina que faltava.**

### 2.5 As demais recentes de arte, em uma linha cada (todas com motivo escrito)

| Casa / vaga | ID | Publicada | Motivo |
|---|---|---|---|
| Scopely — `2D Artist` (Barcelona) | `5409498008` | 09/09 14h15 | **2D**, exclusão escrita. Já descartada em `caca-wd-gh-recencia-0909.md`; confirmo. |
| Scopely — `Senior Art Manager` (Barcelona) | `5409477008` | 09/09 14h09 | *"**primarily focused on people management**"* — gestão, não produção. Já descartada; confirmo. |
| Sony Interactive — `Video Game Capture Artist` Remote/Onsite | `6178395004` / `6178391004` | 09/09 14h14 | Captura de imagem de gameplay. Já descartadas; confirmo. E Sony foi usada em 09/09. |
| Mob Entertainment — `Senior Technical Animator` | `5233450007` | 09/09 12h39 | Animação técnica, exclusão escrita. |
| Sony Interactive — `Senior Gameplay Animator` (Remote EUA) | `6138861004` | 09/09 14h42 | Animação. |
| CD PROJEKT RED — `Senior Cinematic Animator` (Boston) | `744000148596821` | 09/09 19h45 | Animação cinemática. |
| Outpost VFX — `Senior FX Artist` / `Senior Compositor` (Montreal) | `…457729` / `…457160` | 09/09 09h49 | FX/simulação e composição — as duas na lista de exclusão. |
| Rodeo FX — `UX Specialist` (Montreal) | `…584589` | 09/09 18h30 | UX, exclusão escrita. |
| Gameloft — `Graphic Designer` ×2 (Barcelona) | `…474527` / `…452684` | 09/09 | Design gráfico. |
| Starbreeze — `Senior Engine Programmer` | `8352293` | 09/09 12h49 | Programação. |
| Supercell — `Senior Match-3 Designer` / `Marketing Creative Lead` / `Studio Tools Lead` | — | 09/09 | Design de jogo, marketing e ferramentas. |
| Keen Software House — `Senior Marketing Artist` / `Senior UX Designer` (Praga / remoto Europa) | `4971572101` / `4971868101` | 09/09 | Arte de marketing e UX. O corpo bate só em `asset` e `blender`; não há modelagem, textura nem personagem. |
| 31st Union — `Lead Producer` · 2K — `Lead Producer` / `Director, Program Management` | `7986008003` · `7990280003` / `7978906003` | 09/09 | Produção e gestão. |
| Riot — `Principal Content Producer` / `Manager, Narrative Writing` / `Market Community Lead DACH` | `8148779` / `8187620` / `8187640` | 09/09 | Produção, narrativa e comunidade. |
| Epic Games — `Backend Services Programmer Intern` / `UI Programmer Intern` | `6183293004` / `6183401004` | 09/09 20h22–20h30 | **As duas únicas vagas novas da Epic nas 24h são estágios de programação.** |
| Disney/ILM Vancouver — `CG Technology Supervisor` `10160228`, `Jr Lighting TD` `10124854` · Lucasfilm — `Storyboard Artist` `10157624` · ESPN — `Sr Technical Director` `10159739` | — | 08–09/09 | **Já descartadas por escrito em `caca-wd-gh-recencia-0909.md`.** Confirmo que continuam vivas e que os motivos seguem válidos. |
| Disney/ILM Mumbai — `Lighting Technical Director (Junior & Mid-FTC)` | `10159099` | 08/09 | **Índia, fora do recorte** — e é iluminação/TD. |

---

# 3. AS CASAS DA REGRA 14, UMA POR UMA, COM NÚMERO

Ordem de prioridade do briefing. **Nenhuma rendeu vaga da disciplina nas 24h**, e é assim que fica
medido:

- **Disney (inclui ILM, Pixar, Lucasfilm, Marvel).** Os **dois** sites do locatário `disney`/`wd5`
  paginados 100%: `disneycareer` **635 vagas**, `disneycareerdc` **650**. Cruzando os dois por
  `jobReqId`, **127 requisições únicas** com `postedOn` = Today/Yesterday. Li os títulos das 127 e
  fui ao corpo de todas as que tocam arte. **Zero da disciplina.** O que existe de arte recente já
  está resolvido: FaceSwap (§2.4), CG Technology Supervisor, Jr Lighting TD, Storyboard, ESPN Sr
  Technical Director, Lighting TD de Mumbai. O resto das 127 é parque de Orlando, engenharia de
  produto, finanças, marketing, estágios de 2027 e vagas da Disneyland Paris.
- **Pixar.** `pixar`/`Pixar_External_Career_Site` = **3 vagas no total**, a mais nova
  *"Posted 19 Days Ago"* (On-Call Chef). **Zero recentes, zero de arte.** Segue seco, como em 09/09.
- **Warner.** `warnerbros`/`global` = **332 vagas**, ordenadas por data pelo próprio Workday.
  **33 recentes** lidas: CNN, TNT Sports, HBO Max, engenharia, produto, varejo do Studio Tour.
  A única com cara de arte é `Staff Product Designer` (Burbank), que é design de produto digital.
  **Zero de arte 3D.**
- **DreamWorks / NBCUniversal.** `nbcuniversal3` no SmartRecruiters = **369 vagas**, **19 recentes**,
  todas de TV/notícia/marketing/finanças (Telemundo, Universal City, produção de commerce).
  **Zero de arte.**
- **Paramount / Skydance.** O board `skydance` do Lever tem **28 vagas** e a disciplina está lá
  (`Environment Modeling Artist`, `Environment Surfacing Artist`, `Character Surfacing Trainee`,
  `Senior Grooming TD` — Madri). **Mas nenhuma é das últimas 24h**: o `createdAt` mais novo do board
  inteiro é **2026-09-04** (`VP, Head of Strategy`). Ver a ressalva de método da §4.4 — no Lever o
  `createdAt` é criação de requisição, e ele **não** é data de publicação; então o correto é dizer
  que **não consigo medir recência no Lever por esta rota**, e não que "não há nada".

---

# 4. O QUE ESTA RODADA MEDIU DE MÉTODO

**4.1 O `first_published` do Greenhouse vem na listagem barata, e vem em 100% dos casos.**
Confirmado com número: nos **55 quadros vivos / 1.982 vagas**, o conjunto de boards sem o campo
`first_published` é **vazio**. Não precisa baixar corpo para ordenar por recência. A rotina barata
que a rodada de 09/09 sugeriu **funciona**: 55 requisições, poucos segundos, e sai a janela inteira.

**4.2 O `postedOn` do Workday se rearma, e a Disney é o caso extremo.**
Das **127** requisições Disney marcadas "Posted Today/Yesterday", há `jobReqId` como **10118902**,
**10124854**, **10131802**, **10133432** e **10142528** — números **quarenta mil abaixo** dos que a
Disney está emitindo hoje (a mais nova da lista é `10160365`). São requisições de semanas atrás
reempurradas para o topo da recência. **A regra do briefing se confirmou de novo e eu a apliquei:**
na FaceSwap `10160278` o `postedOn` dizia "Posted Yesterday", e o **rodapé do corpo** trouxe
`Date Posted: 2026-09-08`, batendo com o `startDate` da API. **Cruze sempre.**

**4.3 O Breezy não entrega o corpo pelo feed, e o `/p/` só renderiza para navegador — medido.**
O feed `https://<slug>.breezy.hr/json` traz `id`, `name`, `location`, `published_date` e `url`,
mas o campo `description` **vem vazio**. E a página do anúncio, buscada com o User-Agent padrão do
curl, devolve **um esqueleto de SPA com marcadores literais** `%BREADCRUMB_JOB_OPENINGS%`,
`%BUTTON_APPLY_TO_POSITION%` — nada de texto. **Com `-A "Mozilla/5.0 … Chrome/126"` a mesma URL
devolve 24.177 bytes com o anúncio inteiro** dentro do `og:description` e do JSON-LD. Foi assim que
o corpo da AGBO virou descarte medido em vez de palpite. **Anote: no Breezy, User-Agent de navegador
não é enfeite, é o que separa ler de não ler.** As rotas `/position/<id>?format=json`,
`/api/portal/<slug>/position/<id>` e `/json/<id>` devolvem **302 para a raiz**; `api.breezy.hr/v3/portal/…` devolve **404**.

**4.4 No Lever, `createdAt` NÃO é data de publicação — e a API pública não tem data de publicação.**
Este é o buraco honesto da rodada. O board `avalanchestudios` traz `Art Director` com
`createdAt = 2026-04-13` e `Lead Character Artist` com `2026-05-21`, as duas **vivas e listadas
hoje**. O campo é a criação da requisição no ATS. Nos **15 quadros / 250 vagas** de Lever que li,
**nenhuma tem `createdAt` dentro das 24h** — mas isso significa apenas que ninguém *criou* requisição
nova, não que ninguém publicou. **Recência no Lever não é medível por `api.lever.co/v0/postings`.**
Quem quiser fechar esse buraco precisa guardar um retrato do board e comparar dia a dia, ou abrir
navegador. **Eu não abri.**

**4.5 Netflix não é Workday, e o Eightfold dele está parado há duas semanas.**
`netflix.<pod>.myworkdayjobs.com/wday/cxs/netflix/Netflix/jobs` devolve **422 em wd1, wd3, wd5 e
wd103** (o wd101 nem resolve pelo proxy). A rota viva é o **Eightfold**:
`explore.jobs.netflix.net/api/apply/v2/jobs?domain=netflix.com&query=<termo>`. Rodei **nove termos**
(`artist`, `character`, `modeler`, `texture`, `environment`, `groom`, `sculpt`, `surfacing`,
`generalist`) e o `t_create` mais novo do conjunto inteiro é **1784937600 = 2026-08-24**
(*Head of Character Effects (CFX)*, Sydney — que é CFX, exclusão escrita). **Zero na janela.**

**4.6 Blizzard/Activision no Workday: seis nomes de site, seis 422.**
Testei `activision`/`wd1` com `External`, `Blizzard_External_Careers`, `ABK_External_Careers`,
`King_External_Careers`, `Activision_External_Careers` e `ABKCareers` — **todos 422**. A rota real da
casa é `careers.blizzard.com`, que já está registrada no repositório. A casa foi usada em 09/09 de
qualquer forma.

**4.7 Nove falso-amigos NOVOS de slug do Greenhouse, para ninguém repetir.**
Além dos já catalogados (`career`, `jobs`, `explore`, `system`, `company`, `onyx`, `recruit`,
`artstation`, `nix`, `remedy`, `ghost`, `sunrise`, `nexus`, `motive`, `teravision`, `foundry`,
`liftoff`), a varredura de hoje bateu e eu conferi a identidade de cada um pela amostra de vagas:

| Slug | Quem é de verdade | Prova |
|---|---|---|
| `elastic` | **Elastic** (busca/observabilidade), 349 vagas | *ABM Manager, Global Public Sector* |
| `mill` | **Mill** (eletrodoméstico de compostagem, San Bruno), 25 vagas | *Computer Vision Engineer, San Bruno* |
| `raven` | **Raven StealthCo** (biotech, Boston), 4 vagas | *Principal Scientist, In Vivo Pharmacology* |
| `lighthouse` | consultoria/hotelaria, 59 vagas | *Area Director - Japan* |
| `carbon` | **Carbon** (impressão 3D industrial, Sunnyvale), 15 vagas | *Director, Hardware Engineering* |
| `flix` | **FlixBus/Flix SE**, 150 vagas | *Ingenieur Fahrzeugabnahme, Berlin* |
| `moon` | hardware em Palo Alto, 7 vagas | *3D Printing Technician – Production* |
| `twinpines` | administração predial em NY, 23 vagas | *Area Manager, Queens NY* |
| `mighty` | 1 vaga, *Senior AI Software Engineer, NY* | não é estúdio |

**`moon` e `carbon` são as mais perigosas:** as duas batem em `3D` e em `printing`/`modeling` e
passariam num filtro de palavra-chave sem ninguém perceber que é **impressão 3D industrial**, não
arte 3D.

**4.8 O scratchpad desta sessão está sendo escrito por outro agente ao mesmo tempo.**
Eu criei um diretório `gh/` e pedi **56** slugs; ao conferir, havia **84 arquivos**, com nomes que eu
nunca busquei (`artstation`, `company`, `explore`, `onyx`, `system`, `nexus`, `carbon`, `flix`,
`twinpines`, `moon`, `mighty` e outros). **Não usei nenhum desses dados.** Refiz por conta própria,
num diretório isolado, os 26 slugs em questão — e é dessa refação que saem os números da §4.7 e a
linha "quadros extras reconferidos" do placar. **Registro porque, num repositório com vários agentes
rodando, arquivo de scratchpad com nome previsível é fonte contaminada.**

---

# 5. O QUE VARRI, PARA NINGUÉM REPETIR

**Greenhouse — 55 quadros vivos da minha lista (1.982 vagas), listagem integral:**
`2k` (122), `atomiccartoons` (5), `bethesda` (2), `bluehole` (16), `blurstudio` (0),
`brandnewschool` (5), `bungie` (3), `cloudchamberen` (22), `crystaldynamics` (1),
`digitaleclipse` (2), `digitalextremes` (5), `discord` (46), `eleventhhourgames` (6),
`epicgames` (161), `fanaticscollectibles` (151), `firesprite` (1), `gearbox` (1),
`goodjobgames` (31), `gravitywell` (0), `hasbro` (152), `havenenglish` (2), `hbstudios` (0),
`highdive` (9), `housemarque` (3), `insomniac` (6), `jamfilled` (1), `krafton` (60), `kswh` (3),
`laika` (4), `loonshotgames` (23), `mediatonic` (0), `metacore` (0), `mobentertainment` (14),
`monomipark` (0), `naughtydog` (13), `ncamerica` (5), `nintendo` (53), `nmcareers` (2), `playq` (1),
`riotgames` (147), `roblox` (238), `rockstargames` (61), `scopely` (178),
`sonyinteractiveentertainmentglobal` (180), `sonypicturesanimation` (2),
`sonypicturesimageworks` (50), `studiokraftonboard` (1), `swayboxstudios` (11),
`tangogameworks` (14), `teamlfg` (10), `tripledotstudios` (83), `tripwireinteractive` (1),
`unknownworlds` (2), `wargamingen` (55), `wildlifestudios` (18).
**Morto (404):** `phoenixlabsyvren`.
**Reconferidos por mim** (§4.8) — **26 slugs, 21 vivos, 376 vagas:** `31stunion` (6), `airship` (10),
`bandainamco` (4), `castiron` (0), `coatsink` (0), `disney` (2), `hook` (6), `keen` (1),
`lighthouse` (59), `manvsmachine` (1), `method` (2), `metropolis` (73), `prismatic` (5),
`pubgmadison` (2), `rumble` (8), `turtlerockstudios` (1), `carbon` (15), `flix` (150), `mighty` (1),
`moon` (7), `twinpines` (23).
**404 na reconferência:** `embarkstudios`, `jamcity`, `playdead`, `zynga`, `takes2` — **atenção,
`playdead` e `embarkstudios` têm quadro vivo em OUTRAS famílias** (`playdead.breezy.hr` com 14 vagas
e `embarkstudios.teamtailor.com`), então o 404 é do slug de Greenhouse, não da casa.

**Sondagem de slug nova, 100 nomes de estúdio** (dneg, framestore, weta, wetafx, methodstudios,
pixomondo, cinesite, jellyfishpictures, milkvfx, axisstudios, brownbagfilms, cartoonsaloon,
bouldermedia, titmouse, skydanceanimation, illumination, aardman, reelfx, animallogic, luma,
lumapictures, scanlinevfx, nexusstudios, buck, psyop, themill, chaosgroup, sidefx, maxon, otoy,
pixologic, respawn, infinityward, treyarch, sledgehammer, beenox, raven, toysforbob, demonware,
arkane, machinegames, idsoftware, zenimax, certainaffinity, sumodigital, rare, ninjatheory,
obsidian, compulsion, undeadlabs, worldsedge, turn10, 343industries, thecoalition, mojang, xbox,
xboxgamestudios, king, e outros): **3 responderam 200 e os 3 são falso-amigo** (`elastic`, `mill`,
`raven`). **Nenhum quadro Greenhouse novo de estúdio de arte apareceu.**

**Workday — 7 sites, 2.005 vagas:** `disney`/`disneycareer` (635, 100% paginado),
`disney`/`disneycareerdc` (650, 100%), `warnerbros`/`global` (332, 4 páginas ordenadas por data),
`pixar`/`Pixar_External_Career_Site` (3), `sega`/`SEGA_Careers` (28, 100%), `unitytech`/`Unity`
(124, 100%), `aristocrat`/`AristocratExternalCareersSite` (179, 100%),
`spinmaster`/`SpinMaster_Careers` (54, 100%).
**Não responderam (422 / sem `total`):** `netflix` em quatro pods, `starz`/`Starz`,
`cloudimperiumgames`/`CIG_Global_Careers`, `activision` em seis nomes de site.
**Recentes por casa:** Unity **22** (todas engenharia/ML/marketing; os dois `Senior Software
Engineer, Graphics` são **programação de renderização**, não arte — falso positivo já catalogado),
Aristocrat **5** (vendas e técnico de campo), Spin Master **5** (`Product Designer` de Wilton é
design industrial de brinquedo), SEGA **1** (`Senior Build Tools Engineer`).

**SmartRecruiters — 14 quadros, 1.361 vagas, 58 recentes:** `nbcuniversal3` (369/19),
`mattelinc` (445/16), `ubisoft2` (286/8 — **casa é parede de DataDome desde 06/09, não abrir**),
`gameloft` (49/6), `cdprojektred` (44/2), `keywordsstudios` (52/3 — as três são Tóquio/Manila, fora
do recorte, e uma é literalmente *"TEST TEST TEST DO NOT APPLY"*), `outpostvfx` (30/2),
`rodeofx` (34/2), `peoplecanfly` (14/0), `ghostvfx` (2/0), `techlandsa` (28/0), `blumpstudio` (2/0),
`giantssoftwaregmbh` (5/0), `ryseupstudios` (1/0).

**Teamtailor — 29 quadros, 156 vagas, 1 recente.** Os 28 sem nada na janela: `ankama`,
`axolotgamesab`, `beffio`, `blackkitestudios`, `bulkheadinteractive`, `cigames`,
`coffeestainstudios`, `embarkstudios`, `envarstudio`, `fatshark`, `fundaygames`, `gigglebug`,
`goodbyekansas`, `hampastudio`, `ilpvfx`, `ioi`, `pfx`, `playagames`, `realtime`, `sloclap`,
`starstable`, `stunlocksstudios`, `sybo`, `tacticaladventures`, `twinharbour`,
`untoldstdfg1324556`, `vinefx`, `wetaworkshop`. **Rota barata confirmada:
`https://<slug>.teamtailor.com/jobs.json` devolve JSON Feed com `date_published` por vaga** — é o
equivalente Teamtailor do `first_published`.

**Ashby — 6 quadros, 112 vagas, 4 recentes:** `supercell` (47/3), `thatgamecompany` (40/1),
`stellarentertainment` (12/0), `volka` (11/0), `gardens` (1/0), `seconddinner` (1/0).
Rota: `https://api.ashbyhq.com/posting-api/job-board/<slug>` com `publishedAt` por vaga.

**Recruitee — 5 quadros, 62 vagas, 0 recentes:** `framestore` (52), `huuuge` (7), `squeezestudio`
(2), `dovetailgames` (1), `playrix` (0). Rota: `https://<slug>.recruitee.com/api/offers/` com
`published_at`.

**Breezy — 3 quadros, 37 vagas, 1 recente:** `agbo` (18/1), `playdead` (14/0), `warhorsestudios`
(5/0).

**NÃO varri, e digo por quê:** `nvidia`, `adobe`, `autodesk`, `intel`, `fox`, `cae`, `draftkings`,
`deluxe`, `sds` — o lote 2 de 09/09 leu **6.067 vagas** desses quadros e mediu **zero da disciplina**,
catalogando que ali "modeling"/"characterization" é engenharia de semicondutor. Também não fiz
BambooHR, GoHire, Jobvite, Personio, Homerun, Join e SoftGarden: as rodadas de 09/09 os cobriram
inteiros (`caca-ashby-bamboo-gohire-0909.md`, `caca-jobvite-pinpoint.md`, `caca-personio-0909.md`,
`caca-breezy-homerun.md`) e **nenhuma dessas famílias expõe data de publicação numa listagem barata**
— para janela de 24h, custam uma varredura inteira para achar, no melhor caso, o que a de ontem já
achou. **Se você quiser cobertura formal deles, é um comando e alguns minutos — só dizer.**

---

# 6. LEITURA HONESTA DA RODADA

**O método da recência funcionou, e desta vez pegou a vaga certa em vez de um fantasma.** Em 09/09 a
recência trouxe a Senior Texture Artist da ILM Londres, que estava morta há seis dias e só o dedupe
revelou. Hoje ela trouxe uma requisição que **não existia** quando a varredura anterior rodou:
publicada às **22h51 UTC**, duas horas e vinte depois do arquivo de 09/09 ser fechado, num board que
aquele arquivo tinha lido inteiro e declarado sem nada da disciplina. **É o argumento mais forte que
existe para a rodada de recência ser diária e colada na virada:** vaga de 3h de idade não aparece em
varredura de ontem por definição.

**E o número da rodada é duro.** Nas sete famílias inteiras, em 24 horas, **302 vagas foram
publicadas** (45 Greenhouse + 193 Workday + 58 SmartRecruiters + 4 Ashby + 1 Teamtailor + 1 Breezy).
Dessas, **três tocam a disciplina dele** — Riot, Hasbro Hong Kong e Gameloft Yogyakarta — e **duas
morrem no recorte geográfico**. Sobra **uma**. Não é escassez da minha varredura, é a produção real
do mundo num dia.

**O que me incomoda na única linha, e eu prefiro dizer:** a recusa da Riot chegou às 23h09 de ontem,
**dezoito minutos depois** de a vaga nova ser publicada. As duas coisas não se sabem uma da outra —
sistemas diferentes, times diferentes — mas o efeito prático é que você vai bater numa casa que
acabou de dizer não, e a campanha já tem uma decisão escrita (o caso Swaybox) de segurar nessa
situação. **A diferença que me faz manter a linha na fila em vez de segurá-la:** a Swaybox recusou
na **mesma disciplina** e a irmã era a mesma vaga em outro nível; aqui a recusada é **conceito 2D**
e esta é **modelagem de personagem 3D**, e o anúncio traz `Visa Eligible: true` e
`Relocation Package: Platinum` em campo estruturado — que é a coisa mais próxima de um "sim" ao
patrocínio que apareceu na campanha inteira. **A decisão é sua, e ela está escrita dos dois lados.**

**O buraco que eu não fechei:** o Lever. A API pública não tem data de publicação, e o board da
**Skydance** — casa da regra 14, com `Environment Modeling Artist`, `Environment Surfacing Artist`,
`Character Surfacing Trainee` e `Senior Grooming TD` em Madri, tudo dentro do escopo e tudo dentro
da disciplina — é exatamente onde esse buraco dói. **Não afirmo que não há nada novo lá; afirmo que
não consigo medir por curl.** Se alguma dessas quatro nunca foi tocada, ela vale mais que a linha
que eu entreguei. **Sugiro que a próxima rodada abra o dedupe da Skydance por ID antes de qualquer
outra coisa.**

**O que eu NÃO fiz:** não abri navegador, não usei Playwright, não commitei, não fiz push, não
mandei email, não preenchi formulário nenhum, e não toquei em `docs/index.html`, `enviados.csv`,
`automacao/processados.csv` nem `automacao/FILA-DO-VINI.md`.
