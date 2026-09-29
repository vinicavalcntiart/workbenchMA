# VIGIA DO GRUPO DISNEY — 10/09/2026, madrugada

Primeira rodada da varredura **de rotina** do grupo (regra do Vini de 10/09: *"n esqueça da
disney. sempre olho no grupo disney pixar etc."*). Casa por casa, paginação integral, sem
`searchText`, **sem navegador**: tudo por `curl` e `python3/urllib`, no máximo 7 conexões.

**O resultado desta rodada é ZERO candidatura nova, e o número está abaixo, casa por casa.**
Rodada de zero com número vale mais que fila inflada — mas ela não é vazia: ela fecha cinco
quadros, mata quatro dúvidas antigas com frase colada e devolve uma pendência decidida.

---

## 1. COBERTURA POR CASA — o número honesto

| Casa | Quadro lido | Linhas paginadas | Requisições únicas | Bateram no título | Sobreviveram ao escopo | Sobreviveram à disciplina | Sobreviveram à régua | Sobreviveram ao dedupe | **Na fila** |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Disney** (ILM, Lucasfilm, DTVA, ESPN, 20th) | `disney`/`wd5`/**`disneycareer`** + **`disneycareerdc`** | **1.281** | **955** | 57 | 45 | 12 | 8 | **0** | **0** |
| **Pixar** | `pixar`/`wd501`, **os 5 sites do robots.txt** | **4** | **3** | 0 | 0 | 0 | 0 | 0 | **0** |
| **DreamWorks / NBCUniversal** | SmartRecruiters `nbcuniversal3` + `nbcuniversal1` | **375** | **375** | 18 | 17 | 3 | **0** | 0 | **0** |
| **Paramount / Skydance Animation** | Lever `skydance` | **28** | **28** | 14 | 14 | 7 | 7 | **0** | **0** |
| **Warner** | Workday `warnerbros`/`wd5` (`global`+`francais`) **e** `careers.wbd.com` | **336** + 332 | **332** | 6 | 5 | 1 | 1 | 0 | **0** |
| | **TOTAL** | **2.024** | **1.693** | **95** | **81** | **23** | **16** | **0** | **0** |

**Como ler as três últimas colunas, para o número não parecer maquiado.** Na DreamWorks as três
que passaram na disciplina morreram TODAS na régua, com veto escrito (§3.5). Na Skydance as sete
passaram na régua (nenhuma tem veto) e morreram todas no dedupe ou no nível: seis são de ambiente
ou estágio (§3.6) e **a sétima, a Senior Grooming TD de Madri, é a única viva e limpa do grupo
inteiro — mas já está na `FILA-DO-VINI.md` item 23**, esperando a mão dele por parede de hCaptcha
do Lever. Não é vaga nova e não entra em fila de disparo. Detalhe no §2.

### Fatos de cobertura que valem para as próximas rodadas

- **A PIXAR ESTÁ VAZIA DE ARTE, e isso é medido, não suposto.** Os **cinco** sites do
  `robots.txt` (`Pixar_External_Career_Site`, `Pixar_External_Tech_Jobs`, `Pixar_External_Events`,
  `pixar_invite_to_apply`, `Pixar_External_Internships`) somam **4 anúncios, 3 requisições
  únicas**: On-Call Chef, Staff Systems Engineer (Data Streaming) e Senior Research Scientist,
  os três em Emeryville. Três dos cinco sites devolvem `total: 0`. **Zero arte, zero animação.**
- **`careers.wbd.com` É O MESMO QUADRO do Workday `warnerbros`, provado pelo número e pelo link.**
  O widget de busca (`POST https://careers.wbd.com/widgets`, `keywords:""`) devolve
  `totalHits: 332`, exatamente o `total` do `warnerbros`/`wd5`/`global`, e cada resultado traz
  `imApplyUrl` apontando para `warnerbros.wd5.myworkdayjobs.com/global/...`. **Varrer os dois é
  varrer um.** De brinde, o widget reproduz o defeito do alerta: `keywords:"modeler"` devolve
  `totalHits: 2`, e o primeiro é *"Staff, Architect - Tax Systems (OneSource)"* em Atlanta.
  Casamento por substring, confirmado na fonte, não conta como cobertura.
- **Não existe outro locatário Workday do grupo.** Sondei `robots.txt` de **35 nomes × 12 pods =
  420 requisições** (`lucasfilm`, `marvel`, `ilm`, `disneyanimation`, `wdas`, `disneyparks`, `abc`,
  `espn`, `hulu`, `searchlight`, `20thcentury`, `marvelstudios`, `skydance`, `paramount`,
  `nickelodeon`, `wbanimation`, `cartoonnetwork`, `wbgames`, `rocksteady`, `netherrealm`,
  `ttgames`, `avalanchesoftware`, `dreamworksanimation`, `universal`, `nbcuni` e outros).
  **Todos `422`, com uma exceção: `fox`/`wd1`, que é a Fox Corporation** (notícias e esportes),
  empresa separada desde a venda de 2019 e **fora do grupo Disney**. Anote como falso amigo.
- **SmartRecruiters do grupo: só `nbcuniversal3` presta.** `nbcuniversal` = 0, `nbcuniversal2` = 0,
  `dreamworksanimation` = 0, `dreamworks` = 0, `universalpictures` = 0 (a API devolve `200` com
  `totalFound: 0` para qualquer slug inexistente — o teste é o `totalFound`, nunca o código HTTP).
  `nbcuniversal1` existe com **6 vagas**, todas de notícias e marketing, e foi lida inteira.
- **Lever do grupo: só `skydance`.** `skydanceanimation`, `skydancemedia`, `paramount` e
  `nickelodeon` devolvem `404`.

---

## 2. A FILA PRONTA

# **A FILA ESTÁ VAZIA. NENHUMA CANDIDATURA NOVA SAI DESTA RODADA.**

Não há nada para disparar com `wd_geral.js`, `sr_apply.js` ou `apply_lever.js`. Os cinco quadros
do grupo estão **esgotados**: tudo que é da disciplina e do escopo já foi enviado, já foi recusado
com motivo escrito, ou tem veto escrito de autorização.

**A única coisa aberta do grupo inteiro, e ela é de PERSONAGEM:**

**Skydance Animation — Senior Grooming TD — Madri, Espanha**
- Casa: Paramount / Skydance Animation. **Prova do grupo:** a política de privacidade do próprio
  anúncio aponta para `https://privacy.paramount.com/recruitment-privacy-notice`.
- ID da requisição (Lever): **`9ad28cab-87cd-4235-ae9b-b4c53a3457e5`**
- URL pública: https://jobs.lever.co/skydance/9ad28cab-87cd-4235-ae9b-b4c53a3457e5 — **HTTP 200 hoje**
- Faixa: **não publicada**
- **Disciplina: PERSONAGEM, e a frase é do anúncio:** *"As a Senior Grooming TD, you will create
  the highest quality grooms, hair shading lookdev for characters of the production"*, e as
  Responsibilities listam *"Creates complex, artistically appealing hairstyles, grooms & surfacing
  for: human characters / furry creatures / feathered characters / props and elements"*.
  Groom + surfacing + look dev **de personagem**, no nível Senior. É o centro do portfólio dele.
- **Régua de veto, termo a termo, sobre o detalhe completo da API do Lever:**
  - `authoriz` → **1 acerto, FALSO POSITIVO**: *"If you suspect that you are being contacted by an
    unauthorized person or believe that the correspondence you have received is suspicious…"* —
    é o aviso de fraude de recrutamento, não fala de autorização de trabalho.
  - `hybrid` → **1 acerto, NÃO É VETO**: a etiqueta `#Animation #LI-Hybrid` no rodapé. Formato de
    trabalho, não regra de candidatura.
  - `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`, `days a week`, `citizen`,
    `resident` → **ZERO acerto**. **Nenhum veto escrito.**
- **Dedupe (`sh automacao/dedupe-agora.sh "9ad28cab-87cd-4235-ae9b-b4c53a3457e5" "Skydance
  Animation"`): NÃO É NOVA.** 1 ocorrência em `processados.csv` (07/09, tipo `vaga-a-mao`,
  reclassificada de baixa para alta prioridade), 1 em `docs/index.html` e **1 em
  `FILA-DO-VINI.md`, item 23**. Zero marca de envio.
- **Comando para disparar: NÃO EXISTE, e é de propósito.** A parede está escrita na fila dele:
  *"hCaptcha de imagem do Lever, depois do Submit."* `apply_lever.js` não passa disso de IP de
  datacenter. **É clique dele, com o preenchedor de formulário, pelo link
  `.../9ad28cab-87cd-4235-ae9b-b4c53a3457e5/apply`.** Continua sendo o item 23 da fila dele.

---

## 3. O QUE CAIU, COM O MOTIVO LITERAL DO ANÚNCIO

### 3.1. Disney — as QUATRO dúvidas que esta rodada mata com o corpo na mão

**`10160278` — FaceSwap Artist (all levels) — ILM London.** Estava **pendente de decisão dele**
desde a rodada do Workday. **DECIDIDA: FORA.** A régua deu **ZERO acerto nos nove termos** (não há
veto nenhum), então o que reprova é a disciplina, e ela está escrita: *"FaceSwap is a new,
exciting, and growing discipline within the visual effects industry, using Machine Learning (AI)
to create digital faces and likenesses"*, e o What We're Looking For pede *"Working knowledge of
Nuke to prepare precomps and slap comps"* e *"Some experience with CG compositing"*. A categoria
interna é `Faceswap - Studios`. **É composição em Nuke mais treino de rede neural, não é escultura
nem modelagem.** Não reabrir.

**`10157163` — Senior Concept Artist — Remote Worker Location, EUA.** ID **inédito** nos quatro
arquivos, faixa publicada de **USD 112.700 a 154.800**, 100% remota, régua com **ZERO acerto**.
E mesmo assim **FORA**, porque é da ESPN e não de estúdio de animação: *"ESPN is seeking a highly
imaginative and versatile Senior Concept Artist to help shape the future of sports storytelling
across broadcast, digital, social, experiential, and emerging platforms"*, com entregas de
*"storyboards, proof-of-concept frames, motion studies"* e ferramentas *"Cinema 4D, Houdini,
Unreal Engine, Redshift, After Effects, Premiere, Photoshop, Illustrator, Figma"*. Categoria
interna: `Concept Design - Sports`. **É concept 2D e motion graphics de transmissão esportiva.**

**`10153466` — Senior Technical Artist — ILM San Francisco (Project Hire).** Faixa publicada de
**USD 134.300 a 171.800**, régua com **ZERO acerto**. **FORA por disciplina:** o time é o ILM
Immersive e o corpo pede *"in-depth knowledge of real-time shader implementations, limitations of
shaders in VR"* e *"extensive experience working with UE workflows: Blueprints, material networks,
real-time lighting and simulations, post processing"*. **VFX em tempo real e tech art**, as duas
coisas na lista de descarte.

**`10158840` — Sr. VFX Artist — Glendale.** Já tinha sido **recusada em 05/09 com motivo escrito**
(*"pede portfolio de VFX em tempo real feito para jogos (particula, shader, Niagara)"*).
Reconferida hoje, continua no ar e continua fora. Não reabrir.

### 3.2. Disney — as OITO que caíram no dedupe por ID de requisição

Todas conferidas com `dedupe-agora.sh` contra `enviados.csv`, `processados.csv`,
`docs/index.html` e `FILA-DO-VINI.md`:

| ID | Vaga | Situação |
|---|---|---|
| `10159882` | Senior Modeler — ILM Sydney | **ENVIADA em 04/09.** 1 em enviados, 15 em processados, 3 no painel |
| `10159370` | Senior Texture Artist — ILM London | **ENVIADA e RECUSADA** |
| `10159371` | Lead Texture Artist — ILM London | **ENVIADA e RECUSADA em 01/09** |
| `10142674` | Lead Generalist Artist — ILM Vancouver | **ENVIADA em 09/09**, Application Received |
| `10137201` | Pre-Visualisation Generalist Artist — ILM London | **ENVIADA**, com três provas incluindo `jobTasks/completed/application` |
| `10159762` | Character Design Lead — Disney Television Animation | **ENVIADA.** Além disso é design de personagem **2D**, fora da disciplina 3D |
| `10052606` | Sr Generalist Artist — ILM Vancouver | **RECUSADA com motivo escrito:** *"As a Digital Matte Painter, you will create striking digital environments"* |
| `10153285` | Real-Time Environment Artist — ILM San Francisco | **RECUSADA de propósito em 07/09**, arte de cenário em tempo real |

### 3.3. Disney — as armadilhas de título, confirmadas de novo

**Fora pelo título, com a armadilha já medida e reconfirmada hoje:** `10157562` Creature TD
(all levels) ILM London, `10155976` e `10144787` Creature Technical Director **(Rigging)** ILM
Vancouver — **o próprio título traz a palavra Rigging entre parênteses** —, `10126752` Creatures
FX Expression of Interest (Iver Heath). **"Creature TD" é rigging e "Creature FX" é simulação.**
A palavra *creature* não abre exceção.

**Fora por disciplina, sem dúvida nenhuma (Disney, no escopo):** onze de animação (`10154115`,
`10109625`, `10149584`, `10149583`, `10039748`, `10131866`, `10148013`, `10042254`, `10095267`,
`10120274`, e o Facial Animator de Mumbai que também morre no escopo); pintura e design 2D da
Disney Television Animation (`10159662` Background Paint Lead, `10151474` Background Painter,
`10151476` Color Designer, `10159759` Location Design Lead, `10151479` Location Designer,
`10151475` Storyboard Artist, `10151018` FX Artist); `10157624` Storyboard Artist da Lucasfilm
Animation; `10087909` Sr Paint & Roto Artist (Sydney); iluminação (`10152348`, `10152857`);
`10155419` Design and Motion Graphics Artist; e três de maquiagem e cabelo de gente de verdade
(`10156726` do Lion King e as duas `DLP-…` da Disneyland Paris), que só bateram no filtro porque
a palavra *hair* está na lista.

### 3.4. Disney — o que caiu no ESCOPO GEOGRÁFICO (12 requisições, e são as melhores)

**Mumbai / West Mumbai, Índia — fora por regra, e não se contorna:** `10154147` **Sr Character
Modeler**, `10155895` **Lead Modeler**, `10146393` Lead Environment Artist, `10146395` Environment
Supervisor, `10145923` Creature Supervisor, `10155202` Sr Look Dev TD, `10155332` Look Dev TD,
`10152359` Generalist Artist Mid-Senior (DMP Specialized), `10152365` Sr Generalist Artist,
`10157861` Facial Animator. São **dez** — e as duas primeiras são, no papel, as vagas mais
alinhadas do grupo inteiro. **Índia está fora.** Some-se, na Warner, `R000078656` *Chief,
Publicity Producer, Anime Production* em Minato-ku, Tóquio: **Japão está fora.**

### 3.5. DreamWorks / NBCUniversal — o veto de Montréal, RELIDO E CONFIRMADO PALAVRA POR PALAVRA

A instrução era não recomendar sem reler. Reli as três hoje, no detalhe completo da API do
SmartRecruiters. **O veto é ESCRITO e é idêntico nas três, dentro de um bloco chamado
`Eligibility Requirements`:**

> *"Eligibility Requirements — Interested candidates must apply to be considered. **Must be willing
> to work in our Montreal office a minimum of 4 days a week. Must be legally authorized to work in
> Canada.** Must be willing to travel for work related business, if necessary"*

| ID | Vaga | Disciplina | Veredito |
|---|---|---|---|
| `744000137526729` | **Lead Character Artist (Body/Crowd, Face, Hair & Wardrobe)** | **PERSONAGEM CHEIO** — *"Character body modeling, anatomy, and proportion systems"*, *"Hair, grooming, clothing… XGen, Houdini Groom, Metahuman"*, *"Facial modeling and likeness"* | **FORA: veto escrito de autorização no Canadá** |
| `744000137526669` | **Lead Material Artist (Character/Wardrobe, World/Props)** | **SUPERFÍCIE DE PERSONAGEM** — *"Character track: body, skin, fabrics, accessories and wardrobe materials"* | **FORA: mesmo veto escrito** |
| `744000133659271` | Associate Art Director (Characters, Concepts, Lighting & VFX, World) | direção de arte, mais concept que modelagem | **FORA: mesmo veto escrito** |

**Isto encerra a pendência das três de Montréal:** patrocínio seria contexto, mas *"Must be legally
authorized to work in Canada"* é **veto escrito**, e veto escrito desqualifica. As duas primeiras
doem, porque são personagem de verdade em casa do grupo. Não reabrir sem o anúncio mudar de texto.

**A única vaga de arte da DreamWorks propriamente dita, e ela é CFX:** `744000145325278`
**DreamWorks Feature - Character Effects Artist**, Glendale, faixa publicada **USD 89.752 a
130.000**, híbrida 4 dias. **Sem veto escrito** (é nos EUA e a régua só acerta `citizen` no bloco
de igualdade de oportunidade). **Cai pela disciplina, e a frase é a primeira do cargo:**
*"The Character Effects department and CFX Artists at DreamWorks Animation are responsible for
both the set up and shot simulation of cloth, fur, hair, foliage, feathers, props, and other
simulations"*. **CFX e simulação estão na lista de descarte.** Não reabrir.

**Também fora, no cluster de jogos de Montréal (mesmo veto escrito, e nenhuma é da disciplina):**
`744000137526799` Lead Artist (Procedural), `744000138731580` Lead Technical Artist,
`744000137525680` Lead Lighting Artist, `744000133440061` Lead Animator Gameplay,
`744000133438169` Principal Animator, `744000147027149` Senior Animator Gameplay,
`744000132948219` Senior Technical Designer, `744000132455262` Senior UI & UX Technical Designer,
`744000140055099` Senior Producer (Assets), `744000147372549` Lead Audio Designer.
Fora do cluster: `744000138335610` Real-Time Graphic Artist (Miami), `744000145276521`
Generalist **de Recursos Humanos** (Nova York, falso positivo do filtro), `744000143182849`
Assistant Manager, WW New Media Metadata & **Art Servicing** (idem).

### 3.6. Paramount / Skydance Animation — só sobrou ambiente, e ambiente não é carro-chefe

Das 28 do Lever `skydance`, 14 bateram no título. Depois de ler o corpo:

- **`ebbcdae8-…` Environment Modeling Artist (Madri).** *"As an Environment Modeling Artist, you
  will participate in many aspects of the look… to deliver a visually impressive first look of the
  Environment"*, e pede *"3-5 years in VFX industries"*. **Ambiente E abaixo do nível dele.**
  Dedupe: 2 ocorrências em `docs/index.html`, já registrada.
- **`f3ee86d4-…` Environment Surfacing Lead Artist (Madri).** *"As an Environment Surfacing Lead,
  you will be leading a team of surfacing artists… to create the desired look for the environments
  and props"*. **Ambiente.** Dedupe: 1 em `processados.csv`, 1 no painel.
- **`c5793932-…` Environment Surfacing Artist (Madri).** *"…working in coordination with the
  Production team, Art Director, Environment Supervisor… Paints stylized textures based on concept
  art"*. **Ambiente.** Dedupe: 1 em `processados.csv`, 1 na `FILA-DO-VINI.md`.
- **`4c18ce73-…` Junior Environment Surfacing Artist** — ambiente **e** júnior. Fora duas vezes.
- **`7b435bb2-…` Character Surfacing Trainee (Madri).** ID **inédito** e o título é de personagem,
  mas cai pelo nível, com a frase do anúncio: *"It is an ideal experience for those moving from
  the classroom to the industry"* e *"Must be currently enrolled in your last year in an Associate,
  Bachelor, or Master's program at an accredited institution"*, 3 meses presenciais, 35h. **Estágio.
  Dez anos de carreira não entram em estágio.**
- **`f5cdab33-…` Environment Surfacing Trainee** e **`570eb832-…` Environment Set Dressing
  Trainee** — estágio e ambiente.
- **`3c0632d5-…` Art Director (Santa Monica).** ID **inédito**, mas fora: *"Define, develop, and
  clearly communicate the film's artistic style, with a particular focus on **environments, sets,
  props, and color design**"* e *"Create and contribute high-quality **concept art**, visual
  development materials, and key imagery"*, com *"Prior experience on an animated feature film is
  required"*. **Direção de arte de ambiente e concept 2D.**
- **Fora pelo título, sem discussão:** `53d76f8f` 2D Effects Artist, `95e3b293` Animator,
  `60f265de` Senior Animator, `855b4875` Senior Rigging Artist, `ba65408a` Senior Crowds Technical
  Artist. Rigging e crowds estão na lista de descarte.

### 3.7. Warner — a casa continua sem nada, pela sexta varredura

Das 332 requisições dos dois quadros (que são o mesmo quadro), **cinco** sobreviveram ao escopo e
**uma** é da disciplina, de longe:

**`R000106508` — Artiste de niveaux avancé.e / Advanced Level Artist — WB Games Montréal.**
- Régua: **1 acerto, `citizen`, e é FALSO POSITIVO** — está no bloco de igualdade de oportunidade
  (*"without regard to race, color, religion, national origin, gender… citizenship status,
  military status…"*). **Nenhum veto escrito, ao contrário das de Montréal da NBCUniversal.**
- **Cai pela disciplina, e a frase é a primeira do cargo:** *"In this role you will work closely
  with the Lead Level Artist and other members of the team to create **high quality environment
  art and/or props**"*, e a primeira accountability é *"Create any required hard surface or organic
  **environment** models and texturing"*. **Ambiente, prop e hard surface: os três últimos da fila
  de disciplina, e o Vini acabou de dizer que ambiente é perda de tempo.**
- Dedupe: 3 ocorrências em `processados.csv` e 1 no painel, **já julgada e não enviada de
  propósito** em rodada anterior. Mantida fora.

As outras quatro: `R000106815` Senior Lighting Artist (Rocksteady, Londres — **iluminação**),
`R000104758` Advanced Animator (Montréal — **animação**), `R000106773` Executive Assistant e
`R000106777` VP, Content Strategy — as duas últimas só bateram no filtro por substring.

---

## 4. A QUEBRA FINAL

| | Quantidade |
|---|---|
| Candidaturas de **PERSONAGEM** nesta rodada | **0** |
| Candidaturas de **AMBIENTE** nesta rodada | **0** |
| **Total de candidaturas nesta rodada** | **0** |

**Nenhuma candidatura saiu, e nenhuma de ambiente foi empurrada para inflar o número.** As três
vagas de personagem de verdade que apareceram no grupo hoje morreram assim, e nesta ordem:
duas em **Mumbai** (`10154147` Sr Character Modeler e `10155895` Lead Modeler, escopo), duas em
**Montréal** (`744000137526729` Lead Character Artist e `744000137526669` Lead Material Artist,
veto escrito de autorização no Canadá) e uma em **Madri** (Skydance Senior Grooming TD, viva e sem
veto, mas atrás do hCaptcha e já na fila da mão dele).

**Onde a régua de disciplina realmente atuou:** de 81 vagas dentro do escopo geográfico, **57 nem
chegaram à régua de veto** porque eram animação, iluminação, rigging, CFX, composição, roto,
storyboard, pintura de fundo, design de locação, concept 2D, tech art, UI ou maquiagem de gente de
verdade. Isso é o filtro funcionando, não é perda.

---

## 5. COMO ISTO FOI RODADO, para quem repetir amanhã

Nenhum navegador foi aberto. Nada foi enviado, nenhum formulário foi preenchido, nenhum
`searchText` foi usado.

1. **`GET https://<loc>.<pod>.myworkdayjobs.com/robots.txt`** para descobrir os sites de cada
   locatário, mais 420 sondagens de locatário nos 12 pods reais. `422` = não existe.
2. **`POST https://<loc>.<pod>.myworkdayjobs.com/wday/cxs/<loc>/<site>/jobs`** com
   `{"limit":20,"offset":N,"searchText":""}`, paginando de 20 em 20 até o `total`.
   **`limit:20` funciona; `limit:50` devolve HTTP 400.** 2.024 linhas colhidas, zero falha.
3. **`GET https://api.smartrecruiters.com/v1/companies/nbcuniversal3/postings?limit=100&offset=N`**
   até `totalFound`. Detalhe em `.../postings/<id>`.
4. **`GET https://api.lever.co/v0/postings/skydance?mode=json`**, e o detalhe da vaga em
   `.../postings/skydance/<uuid>?mode=json`.
5. **`POST https://careers.wbd.com/widgets`** com `ddoKey: refineSearch` e `keywords: ""` para o
   quadro inteiro da WBD (é Phenom; o `api/apply/v2/jobs` responde *"Tenant not identified"*).
6. **Régua de veto sobre o DETALHE completo**, nunca sobre a listagem, com os termos `authoriz`,
   `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`, `days a week`, `citizen`,
   `resident` (mais `relocat`, `visa`, `based in`, `located in`, `onsite`, `hybrid`), 200
   caracteres de contexto de cada lado e classificação manual de cada acerto.
7. **Dedupe por ID de requisição** com `sh automacao/dedupe-agora.sh "<ID>" "<Casa>"`, os dois
   argumentos, contra os quatro arquivos.
8. **Conferência de liveness:** as URLs públicas citadas neste arquivo foram batidas com `curl` e
   **todas devolveram HTTP 200**.

`docs/index.html`, `enviados.csv` e `FILA-DO-VINI.md` **não foram tocados**.
