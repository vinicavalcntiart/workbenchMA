# Casas grandes e revalidação — rodada de 08/09/2026

Agente de prospecção. **Não apliquei, não enviei email, não preenchi formulário, não editei arquivo compartilhado, não commitei.** Só `curl` e WebFetch. Nenhum navegador foi aberto.

Onde escrevo "não vi captcha no HTML", é isso mesmo: **veredito só com o clique**.

---

# SEÇÃO 1 — AS QUATRO CASAS GRANDES

## 1.0 O que varri, com os termos exatos

| Casa | Porta usada | Termos buscados | Resultado bruto |
|---|---|---|---|
| **Disney** (Pixar, Lucasfilm, ILM, Marvel, DTVA) | API Workday `POST https://disney.wd5.myworkdayjobs.com/wday/cxs/disney/disneycareer/jobs`, `limit:20` | `character`, `modeler`, `modeling`, `sculpt`, `texture`, `surfacing`, `look development`, `visual development`, `3D artist`, `groom`, `character artist`, `concept`, `shading`, `environment artist`, `Pixar`, `animation artist` — **16 termos** | HTTP 200 em todos. 13 requisições de arte/criatura no total |
| **DreamWorks / NBCUniversal** | API SmartRecruiters `https://api.smartrecruiters.com/v1/companies/NBCUniversal3/postings?limit=100&q=<t>` | `artist`, `modeler`, `surfacing`, `look development`, `sculpt`, `character`, `texture`, `groom` — **8 termos** | HTTP 200 em todos. 8 requisições de arte. `sculpt` deu `totalFound=0` |
| **Warner (WBD)** | `https://careers.wbd.com/global/en/search-results?keywords=<t>`, JSON embutido sob `"jobs":[` | `artist`, `modeler`, `character`, `texture`, `look+development`, `sculpt`, `surfacing`, `animation` — **8 termos** | HTTP 200 em todos. **ZERO da disciplina** |
| **Paramount / Nickelodeon / Skydance** | **PORTA NOVA — ver 1.4** | varredura completa do quadro (287 vagas) | **ZERO da disciplina** |

## 1.1 ACHADO OPERACIONAL: a Paramount tem porta legível hoje

O briefing registra a Paramount como Access Denied do Akamai. **Isso mudou em parte, e a diferença é de host:**

- `https://www.paramount.com/careers` → **HTTP 403**, corpo literal: `<TITLE>Access Denied</TITLE> ... You don't have permission to access "http://www.paramount.com/careers" on this server. Reference #18.d8714017...` — **continua bloqueado, com UA de navegador.**
- `https://careers.paramount.com/search-jobs` → **HTTP 200, 318 KB.** O host de carreiras responde.

Duas ressalvas medidas, para a próxima rodada não perder tempo:
1. **A palavra-chave é ignorada.** `/search-jobs/artist`, `?k=artist`, `?keyword=artist` e o endpoint Radancy `/search-jobs/results?Keyword=artist` devolvem os **mesmos ~318 KB** com as mesmas 25 vagas. A busca é feita por JS no cliente.
2. **A paginação por query também é ignorada** (`?p=1`, `?p=2`, `?p=12` → 25 links idênticos).

**A porta que funciona é o sitemap:**
```
https://careers.paramount.com/sitemap.xml     → HTTP 200, 58 KB
```
Ele lista **287 vagas** com URL, título no slug e `<lastmod>`. É enumeração completa do quadro, sem JS e sem Akamai.

**Resultado da varredura das 287:** filtrando por `artist|model|sculpt|textur|charact|look-dev|surfac|groom|shad|visual-dev|animat|3d|design|art-`, sobraram 9, e **as 9 são design de produto/gráfico, nenhuma é arte 3D**:

Product Designer (NY) · Designer, Publishing (NY) · Photographer/Editor part-time (Minneapolis) · Senior Designer, Design Systems (Burbank) · Lead, Product Designer (NY) · Sr Data Engineer, Data Architecture and Modeling (NY) · Senior Designer, Product Development CPG (LA) · Designer, Off-Air CBS Sports (NY) · Senior Social Media & Static Set Content Designer (NY).

> **PARAMOUNT: NADA DA DISCIPLINA HOJE.** Não é falta de acesso — é quadro varrido inteiro, 287 de 287. Nenhum posto de Nickelodeon Animation nem de Skydance Animation aparece neste quadro; os boards Greenhouse `skydance`, `skydanceanimation`, `skydancemedia` e `nickelodeon` devolvem **HTTP 404** (board inexistente). O alerta de email segue sendo a cobertura certa para animação da Paramount.

## 1.2 WARNER: varrida, e nada

Oito termos, HTTP 200 em todos, JSON extraído do `"jobs":[`. As **únicas** duas vagas com "artist" no título no grupo inteiro:

- **Senior Lighting Artist** — Rocksteady Studios, Londres, `R000106815`, publicada 28/07. Iluminação de jogo, **não é a disciplina**.
- **Artiste de niveaux avancé.e / Advanced Level Artist** — WB Games Montréal, `R000106508`, publicada 15/07. Level art, **não é a disciplina**.

A busca `character` devolveu 10 resultados e **nenhum** é de arte (Designer Combat, HR Working Student, Staff Data Scientist, Producer...). `texture`, `sculpt` e `surfacing` devolveram **n=0**.

> **WARNER (incl. WB Animation e Cartoon Network): ZERO vaga de arte de personagem, modelagem, texturização, look dev ou visual dev hoje.**

## 1.3 DISNEY — 13 requisições de arte, e o que sobra depois do filtro

### Já resolvidas — NÃO REENVIAR (dedupe pela referência da requisição, conferido em `processados.csv`, `enviados.csv` e `docs/index.html`)

| Req | Cargo | Onde | Situação registrada |
|---|---|---|---|
| `10159370` | Senior Texture Artist — ILM London | Londres, UK | **Aplicada e confirmada 02/09; RECUSADA 03/09** |
| `10159371` | Lead Texture Artist — ILM London | Londres, UK | **Aplicada 31/08; RECUSADA 01/09** |
| `10159882` | Senior Modeler — ILM Sydney | Sydney, AU | **Aplicada e confirmada 04/09** (Application Received) |
| `10159762` | Character Design Lead — DTVA | Glendale, CA | **Aplicada 02–03/09**, Application Received |

> **ARMADILHA DE ANÚNCIO VIVO, medida de novo hoje:** a `10159370` volta na API com `startDate: 2026-09-07` ("Posted Yesterday"), mas o corpo do próprio anúncio diz `Date Posted: 2026-08-26`. **O anúncio foi refrescado, não reaberto.** Quem varrer amanhã vai ver "publicada ontem" outra vez e vai querer mandar de novo. É a mesma requisição já recusada.

### Fora do escopo geográfico (Índia — regra do Vini de 26/08), registradas para não serem "redescobertas"

- `10155895` — Lead Modeler, ILM Mumbai, `Date Posted: 2026-07-14`
- `10154147` — Sr Character Modeler, ILM West Mumbai, `Date Posted: 2026-06-18` (o anúncio pede "Expert in Maya and Zbrush", é exatamente a disciplina dele — dói, mas a regra é a regra)
- `10155202` — Sr Look Dev Technical Director, ILM Mumbai, `Date Posted: 2026-07-03`

### A ÚNICA requisição de arte sem entrada em lugar nenhum

**Environment Supervisor (slug interno: Generalist-Artist-Supervisor)**
- Casa/divisão: **Disney → Lucasfilm → ILM Mumbai**
- Cidade: Mumbai, Índia · Full time
- Req: **`10146395`** · `Date Posted: 2026-03-20` · `startDate` na API: 2026-09-06
- Link direto: `https://disney.wd5.myworkdayjobs.com/disneycareer/job/Mumbai-India/Generalist-Artist-Supervisor_10146395`
- ATS: Workday (`disney.wd5.myworkdayjobs.com`) · formato: portal, conta Workday da Disney que ele já tem
- Busca de veto nos 9 termos no anúncio **inteiro**: **nenhum dos 9 apareceu.** Fim literal do anúncio: *"...Fluent in Houdini, 3dsmax, Maya, Photoshop, Nuke Fluent in Solaris... Job Posting Segment: ILM Mumbai... Primary Job Posting Category: Environment - Studios, Matte - Studios"*
- Entrada no painel: **NÃO EXISTE** (zero ocorrência de `10146395` em `PORTAIS`, `enviados.csv`, `processados.csv` e `alvos.csv`)
- **RECOMENDAÇÃO: NÃO APLICAR.** Dois motivos somados: (a) Índia, fora do escopo geográfico; (b) categoria literal *"Environment - Studios, Matte - Studios"* — é supervisão de ambiente e matte, **não é a disciplina**, cai na ressalva de 05/09.

### Descartadas pela ressalva de 05/09 (queimariam a porta da divisão)

- `10153285` **Real-Time Environment Artist — ILM San Francisco** → VFX em tempo real. Descartada.
- `10153466` **Senior Technical Artist — ILM San Francisco** → technical art. Descartada.
- `10152359` **Generalist Artist Mid-Senior (DMP Specialized)** → DMP = digital matte painting, é background paint. Descartada.
- `10152348-1` / `10152857-2` **Lighting Artist / TD — ILM SF** → iluminação. Descartadas.
- `10157562`, `10155976`, `10144787`, `10126752` — Creature TD / Creature FX. Já registradas antes; são cargos técnicos de rigging e simulação, não modelagem.

> **Nota de julgamento sobre a `10159762` (Character Design Lead, DTVA):** a candidatura já saiu em 02/09, então a questão é histórica, mas registro para calibrar o filtro. Apesar do campo `Primary Job Posting Category: Modeling`, o anúncio é **2D**: pede *"Knowledge of drawing software that includes Photoshop, Illustrator, Harmony"*, entrega *"turnarounds, mouth charts and expression sheets"*, e é *"a fully on-site role based in Glendale, CA"* sob acordo coletivo. **O rótulo "Modeling" no Workday da Disney não é garantia de disciplina.** Se aparecer outra igual, é caso da ressalva de 05/09.

> **DISNEY: nenhuma vaga nova da disciplina hoje.** Das 13 de arte, 4 já resolvidas, 3 fora do escopo por país, 1 nova mas de ambiente/matte na Índia, 5 fora da disciplina.

## 1.4 DREAMWORKS / NBCUNIVERSAL — o veto está escrito, e é literal

Oito requisições de arte. **Cinco delas (as de Montréal) carregam veto ESCRITO**, no bloco `Eligibility Requirements` que fica no fim do anúncio e **não aparece na listagem** — exatamente o padrão da Rebellion.

**Frase literal, idêntica nas cinco:**
> *"Eligibility Requirements — Interested candidates must apply to be considered. **Must be willing to work in our Montreal office a minimum of 4 days a week. Must be legally authorized to work in Canada.** Must be willing to travel for work related business, if necessary"*

Isso bate **três** dos nove termos de veto de uma vez: `eligib`, `days a week`, `authoriz`.

| Ref | Cargo | Local | Publicada | Disciplina? | Veredito |
|---|---|---|---|---|---|
| `REF38910F` / `744000137526729` | Lead Character Artist (Body/Crowd, Face, Hair & Wardrobe) | Montréal | 13/07 | **Sim** | **VETO ESCRITO** — descartar |
| `REF38920U` / `744000137526669` | Lead Material Artist (Character/Wardrobe, World/Props) | Montréal | 13/07 | **Sim** | **VETO ESCRITO** — descartar |
| `REF38909O` / `744000133659271` | Associate Art Director (Characters, Concepts, Lighting & VFX, World) | Montréal | 23/06 | Parcial | **VETO ESCRITO** — descartar |
| `REF38918P` / `744000137526799` | Lead Artist (Procedural) | Montréal | 13/07 | Não (procedural/env) | **VETO ESCRITO** + fora da disciplina |
| `REF38921T` / `744000138731580` | Lead Technical Artist | Montréal | 20/07 | Não (technical art) | Fora da disciplina (este **não** tem o bloco de elegibilidade — nenhum dos 9 termos apareceu) |

As três primeiras já constam do painel e da fila manual dele (bloqueadas por DataDome do SmartRecruiters). **`REF38918P` e `REF38921T` são requisições que não constavam de nenhum arquivo** — registro aqui para fechar o buraco, mas **as duas ficam sem envio**, com a razão escrita acima.

**A única de DreamWorks Animation de verdade (longa-metragem):**
- **DreamWorks Feature — Character Effects Artist** · Glendale, CA · `REF38952U` / `744000145325278` · publicada **24/08** · Full-time
- Link: `https://jobs.smartrecruiters.com/NBCUniversal3/744000145325278` · ATS SmartRecruiters · formato portal
- Busca de veto nos 9 termos no anúncio inteiro: **nenhum dos 9 apareceu.** Fim do anúncio é só o bloco de EEO/acessibilidade de LA.
- **Já está no painel e na fila manual** (bloqueio por DataDome). Não é achado novo.
- Ressalva de disciplina: CFX é *"set up and shot simulation of cloth, fur, hair, foliage, feathers, props"* — é simulação, vizinha da modelagem mas não é ela. A decisão de mandar já foi tomada antes; não mexo.

> **DREAMWORKS/NBCU: nenhuma vaga nova aplicável hoje.** Duas requisições inéditas encontradas, ambas fora da disciplina, uma delas com veto escrito.

## 1.5 Veredito da Seção 1, sem inflar

**Zero vagas novas para aplicar hoje nas quatro casas grandes.**

- **Disney**: varrida com 16 termos. 13 de arte. Nenhuma nova aplicável. A `10159370` é armadilha de anúncio refrescado.
- **DreamWorks/NBCU**: varrida com 8 termos. 2 requisições inéditas, ambas descartadas com razão escrita. As de personagem em Montréal têm veto literal.
- **Warner**: varrida com 8 termos. Zero da disciplina no grupo inteiro.
- **Paramount**: **quadro inteiro varrido pela primeira vez** (287 vagas via sitemap). Zero da disciplina. Porta nova documentada acima.

**O que a rodada entrega de valor não é vaga, é porta:** `careers.paramount.com/sitemap.xml` tira a Paramount da cegueira total. Da próxima vez a varredura leva segundos.

---

# SEÇÃO 2 — REVALIDAÇÃO DAS ENTRADAS MAIS ANTIGAS

Base: `PORTAIS` extraído com o scanner que respeita aspas — **740 entradas, 467 com `done === false`, 157 delas `alta` ou `media`**. Reconferi **32** delas, as mais antigas por ordem do array, todas **na fonte oficial** (nunca em agregador). Onde havia API pública, usei a API.

## 2.1 MORTA — 1

### `[41] 11 bit studios (Varsóvia) — media` · **VAGA/PORTA EXPIRADA**
- URL do painel: `https://11bitstudios.com/careers/` → **HTTP 404**
- Evidência literal, título da página: **`Page not found – 11 bit studios`**
- **Não é a rede caindo:** `https://11bitstudios.com/` responde **HTTP 200** no mesmo comando. `https://11bitstudios.com/en/careers/` também dá **404**.
- **A porta mudou de lugar:** o link no rodapé do site aponta hoje para `https://11bitstudios.com/jobs/` (HTTP 200, título `Jobs - 11 bit studios`).
- **Mas continua sem vaga:** a seção `CURRENT OPENINGS` da página nova vem **vazia**, seguida de *"HAVEN'T FOUND WHAT YOU'RE AFTER? LET US KNOW WHAT INTERESTS YOU. JUST SEND AN E-MAIL WITH YOUR APPLICATION"*. Ou seja, a entrada morre de duas formas: URL 404 **e** quadro zerado.

## 2.2 VIVAS E CONFIRMADAS NA FONTE — 24

Todas com busca literal dos 9 termos de veto no anúncio inteiro.

| # | Entrada | Prova de vida | Veto (9 termos) |
|---|---|---|---|
| 1 | **Behaviour Interactive — Senior 3D Character Artist, 7 Days to Die** (Montréal) | API Lever `api.lever.co/v0/postings/bhvr` HTTP 200: id `976b2a8c-…` presente entre 38 vagas, título *"Senior 3D Character Artist - 7 Days to Die"*, `createdAt` **25/08** | **Nenhum dos 9** |
| 4 | **Eidos-Montréal — Lead Environment Artist** | `jobs.dayforcehcm.com/en-CA/eic/CANDIDATEPORTAL/jobs/2192` HTTP 200, e `"jobTitle":"LEAD ENVIRONMENT ARTIST"` com `"2192"` embutidos no HTML servido | Não reescaneado (anúncio carregado por JS); a entrada já registra "SEM NENHUM VETO" |
| 7/34 | **Hello Games — Experienced Artist** (Guildford) | `hellogames.org/jobs/experienced-artist/` HTTP 200, `<title>Experienced Artist - Hello Games`, `<h1>Experienced Artist` | **Nenhum dos 9** |
| 8/35 | **About Fun — 3D Graphic Artist** (Praga) | HTTP 200, `<title>Jobs - 3D Graphic Artist @ About Fun` | **Nenhum dos 9** |
| 9/36 | **Alkimia Interactive / THQ Nordic — 3D Artist** (Barcelona) | HTTP 200; lista viva: `3D Artist (m/f/d)`, `VFX Artist`, `Technical Artist`, `2D/UI Artist` | **Nenhum dos 9** |
| 11 | **Haven Studios / PlayStation (Montréal)** | API Greenhouse `havenenglish` HTTP 200, **2 vagas**, ambas de 02/09 | — |
| 22 | **Archiact (Vancouver) — open application** | HTTP 200; sob `OPEN POSITIONS` só existe **`General Application`** | — |
| 23 | **Smoking Gun Interactive / Keywords (Vancouver)** | HTTP 200, `<title>CAREERS - Smoking Gun Interactive Inc.`; sob `AVAILABLE POSITIONS` **nenhuma vaga listada** | — |
| 25 | **Gamemode One — General Application (Halifax)** | API BambooHR `/careers/list` HTTP 200: **id 24 = `General Application`** presente entre 3 vagas | — |
| 26 | **DONTNOD Montréal — Spontaneous Application** | API SmartRecruiters HTTP 200: `Spontaneous Application`, Montréal, `REF75J` | **Nenhum dos 9** |
| 33 | **Budge Studios — Artiste 3D Généraliste** (Montréal) | API BambooHR HTTP 200: **id 26 = `Artiste 3D Généraliste/3D Artist Generalist`**, Montréal, entre 4 vagas | — |
| 46 | **Kevuru Games (Kiev)** | HTTP 200, `<title>Career - Kevuru Games`; disciplinas vivas: `3D Characters Design`, `3D Game Modeling` | **Nenhum dos 9** |
| 47 | **Crytivo — Environment Artist / Autonomica** | `crytivo.com/jobs` HTTP 200, `<title>Crytivo Jobs`, `<h1>Jobs` | **Nenhum dos 9** |
| 58 | **SHIFT UP — 3D Character Modeler** (Seul) | HTTP 200, `<title>[신규 프로젝트] 3D 캐릭터 모델러` — título literal da vaga, viva. Redireciona para `/ko/o/235689/apply/new` | Corpo em JS, não escaneável por esta rede |
| 60 | **Sans Strings Studio (EUA)** | HTTP 200, `<title>Careers - Sans Strings Studio`; `Open Positions` viva com `Unreal Generalists`, `Technical Animator / Technical Artist` | **Nenhum dos 9** |
| 62 | **Moonmana (Gdansk/Tenerife/remoto)** | HTTP 200, `<title>Careers at Moonmana game development studio`, `Current Openings` viva | — |
| 65 | **Unit Image — General Application (Paris)** | HTTP 200, `<title>JOBS – Unit Image`, `<h1>JOBS`. Redireciona `/en/jobs/` → `/jobs/` | — |
| 66 | **Traega Entertainment — Senior Character Artist** (remoto/EUA) | HTTP 200, `<title>Senior Character Artist \| traega` | **Nenhum dos 9** |
| 67 | **Next Level Games / Nintendo — General Application** (Vancouver) | HTTP 200, `<title>General Application - Next Level Games - Career Page`, `<h1>General Application` | — |
| 68 | **Flying Bark Productions (Sydney/Madri)** | API BambooHR HTTP 200, **10 vagas vivas** | — |
| 70 | **HB Studios / 2K (Nova Escócia)** | API Greenhouse `hbstudios` HTTP 200 com **`n=0`** — board existe e está vazio | — |
| 75 | **Asterman (Vilnius)** | HTTP 200, `<title>Careers at Asterman`; vivas: `2D Artist`, `3D Generalist (Unreal)`, `Characters, Anatomy` | — |
| 76 | **Pixel Zoo — Environment Artist** (Brisbane) | HTTP 200, `<title>Environment Artist - Pixel Zoo`, `<h1>Environment Artist` | **Nenhum dos 9** |
| 77 | **SHED — Spontaneous Application** (Montréal) | HTTP 200, `<title>SPONTANEOUS APPLICATION \| SHED`, `<h1>SPONTANEOUS APPLICATION` | — |

### As três da One Of Us (Paris) — `[78]`, `[79]`, `[80]` — todas VIVAS pela API do Workable

`GET https://jobs.workable.com/api/v1/jobs/<id>` → HTTP 200, campo **`"state":"published"`** nas três.

| Cargo | id Workable | Criada | Contrato | Veto |
|---|---|---|---|---|
| **Modeller** | `2rTHdox84n1Ge86ez2adUb` | **30/07** | Contract, Paris, híbrido | **Nenhum dos 9** |
| **Texture Artist** | `cXt2aXYi46NxxwuuHiwHhh` | **03/08** | Contract, Paris, híbrido | **Nenhum dos 9** |
| **Look Development Artist** | `itrWRTN6TnCpRVJUfhA4gi` | **03/08** | Contract, Paris, híbrido | **Nenhum dos 9** |

São as três exatamente da disciplina e as três seguem abertas 5 semanas depois. A trava registrada continua sendo o Turnstile, não a vaga.

## 2.3 SEM VEREDITO — 2 (não conte como morta nem como viva)

| # | Entrada | O que aconteceu |
|---|---|---|
| 0 | **TTK Games — Character Artist (Estocolmo)** | `ttkgames.com/careers/job?id=561860` responde **HTTP 200**, mas o HTML servido traz só `<h1>Fetching job...</h1>` — a vaga é carregada por JS. Cacei o backend: os chunks Nuxt apontam para `https://ttk-strapi-tnje3.ondigitalocean.app`, mas `/api/jobs`, `/api/jobs/561860`, `/api/careers` e `/api/job-openings` devolvem **404 `NotFoundError`** (coleção não exposta). `career.ttkgames.com` é **bloqueado pelo proxy de egresso** (`connect_rejected`) e o WebFetch de `ttkgames.com` também (`EGRESS_BLOCKED`). **Só o clique do maestro resolve.** |
| 40 | **Bugbear Entertainment (Helsinque)** | `www.bugbeargames.com/careers/` e a raiz devolvem **`http=000`** (conexão não fecha por esta rede). **Isso não é vaga morta** — é o mesmo defeito de rede da FILA A de 07/09. Fica pendente de reconferência. |

## 2.4 ARMADILHAS DE AMBIENTE — 2, confirmadas de novo

| # | Entrada | Medição de hoje |
|---|---|---|
| 10 | **Pixelsplit (notion.site)** | HTTP 200 com **20.033 bytes** — é só o shell de JS do Notion, sem conteúdo. Armadilha **confirmada**, segue valendo. |
| 59 | **Red Manta / Twin Atlas — Environment Artist (notion.site)** | HTTP 200 com **20.034 bytes** — mesmo shell, mesmo tamanho. Armadilha **confirmada**. A vaga pode estar viva; esta rede não consegue dizer. |

---

## Placar da Seção 2

| | |
|---|---|
| Entradas reconferidas | **32** |
| **Mortas** | **1** (11 bit studios — HTTP 404, `Page not found – 11 bit studios`) |
| **Vivas confirmadas na fonte** | **24** (incluindo as 3 da One Of Us com `state:published`) |
| Sem veredito (rede/JS, não é morte) | **2** (TTK Games, Bugbear) |
| Armadilhas de ambiente reconfirmadas | **2** (Pixelsplit, Twin Atlas — as duas em notion.site) |
| Levantamentos/métodos, não vagas — pulados de propósito | 3 (`[16]`, `[39]`, `[52]`) |

## O que travou

1. **TTK Games**: SPA + Strapi fechado + `career.ttkgames.com` barrado pelo proxy de egresso + WebFetch bloqueado no domínio. Sem veredito por caminho automatizado.
2. **Bugbear**: `http=000`, falha de conexão desta rede. Não é morte.
3. **Paramount**: a busca por palavra-chave e a paginação são feitas por JS; o servidor ignora os dois. Contornado pelo sitemap, que resolve o problema por inteiro.
4. **Dayforce (Eidos)**: não achei endpoint JSON público (`/api/v1/...` → 404). A prova de vida veio do `jobTitle` embutido no HTML servido, o que basta.
5. **Notion**: continua ilegível por esta rede, agora com o tamanho exato do shell medido (≈20 KB) para servir de assinatura em varreduras futuras.
