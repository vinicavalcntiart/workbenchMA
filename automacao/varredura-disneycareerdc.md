# Varredura do quadro `disneycareerdc` — 09/09/2026

Quadro irmão do `disneycareer` no locatário Workday da Disney (pod `wd5`).
Tudo abaixo foi rodado com `curl` + Python nesta sessão. Nenhum navegador aberto, nada
commitado, nada enviado, nenhum formulário preenchido, nenhum arquivo protegido tocado.

Aviso de cabeçalho, porque muda a leitura do relatório inteiro: **a premissa de que este
quadro "nunca foi varrido" não se sustentou na medição.** Metade das requisições dele já
estava no `disneycareer` que a campanha usa, e 16 IDs deste quadro já aparecem nos arquivos
da campanha — inclusive duas candidaturas já enviadas e confirmadas. Os números estão na
§4 e na §5. A fila real é pequena e eu não vou inflá-la.

---

## 1. PLACAR

| Medida | Número |
|---|---|
| Vagas totais no quadro (`total` declarado pela API) | **642** |
| Linhas devolvidas somando as 33 páginas | **642** |
| `externalPath` únicos / `jobReqId` únicos | **642 / 642** |
| Requisições HTTP de paginação (limit=20, 5 conexões) | 33 |
| Bateram na peneira ampla de título (56 termos de arte/3D) | **56** |
| Descrições completas baixadas e lidas na íntegra | **20** |
| **Passaram o filtro de DISCIPLINA** (regra 1) | **11** |
| **Passaram o ESCOPO geográfico** (regra 2) | **5** |
| **Passaram a RÉGUA de 17 termos** (regra 3) | **5** (zero veto real) |
| **Passaram o DEDUPE por ID de requisição** (regra 4) | **1** |
| **FILA PRONTA PARA CLICAR** | **1 nova + 1 sinalizada para redecidir** |

Funil de disciplina → escopo, aberto porque a perda foi quase toda geográfica:
das 11 da disciplina, **6 caíram só por serem em Mumbai / West Mumbai (Índia)**, entre elas
`Sr Character Modeler`, `Lead Modeler` e `Lead Environment Artist` — que seriam alvo central
se a Índia estivesse no escopo.

---

## 2. A FILA

Ordenada por proximidade do centro do portfólio (personagem estilizado → ambiente → generalista).
Nenhuma vaga de **personagem** sobreviveu ao dedupe: as duas que existiam já foram enviadas.
Então a fila começa em ambiente/generalista, e isso é o que o quadro rendeu de verdade.

---

### 1. Lead Generalist Artist — ILM Vancouver (Disney / Lucasfilm)

| Campo | Valor |
|---|---|
| Estúdio / marca | **ILM (Lucasfilm)** — segmento `ILM Vancouver` |
| Cargo | Lead Generalist Artist |
| Cidade / país | **Vancouver, BC, Canadá** |
| Formato | **Híbrido** — 2–3 dias no escritório |
| Requisição | **`10142674`** |
| Data de publicação | **2026-06-11** (`Posted 30+ Days Ago`) |
| Faixa salarial publicada | **C$ 126.800 – C$ 162.300 / ano** (semana de 40h) |
| `canApply` | `true` (verificado no JSON de detalhe) |
| Exclusiva deste quadro? | **SIM** — `10142674` não existe no `disneycareer` |

**URL de candidatura (testada nesta sessão, HTTP 200):**
`https://disney.wd5.myworkdayjobs.com/en-US/disneycareerdc/job/Vancouver-BC-Canada/Lead-Generalist-Artist_10142674`

**Régua de veto, resultado literal:** os 17 termos deram **ZERO casamento** no texto integral
(5.065 caracteres lidos). Nenhuma frase de autorização, elegibilidade, patrocínio, permissão
de trabalho, residência, LMIA ou realocação. **Limpa.**

**Dedupe nos quatro arquivos, contagem literal de ocorrências da string `10142674`:**

| Arquivo | Ocorrências |
|---|---|
| `docs/index.html` | **0** |
| `enviados.csv` | **0** |
| `automacao/processados.csv` | **0** |
| `automacao/FILA-DO-VINI.md` | **0** |

→ **NOVA. Zero nos quatro. É a única vaga genuinamente inédita que o quadro produziu.**

**Por que conta como disciplina:** o corpo pede explicitamente construção de asset —
*"Build assets (model, texture, look development)"*, *"Create full CG environments from
scratch for establishing shots or multi shot sequences"*, *"Set dress and assemble
environments"* — mais liderança: *"manage a small part of the crew"*, *"mentor the artists"*.
Modelagem + texturização + look dev + liderança, tudo escrito.

**Ressalva honesta:** é ambiente fotorrealista, não personagem estilizado, e o próprio anúncio
diz *"The work varies a lot from set extension using Digital Matte Painting techniques to full
CG environments"* e *"Understand DMP techniques and know when it is best to use them"*. Uma
parte do trabalho é pintura. Não é o centro do portfólio dele — é a borda dele. Mas passa a
regra 1 por ser modelagem/texturização/look dev de ambiente com liderança, e a faixa é a
melhor do quadro inteiro.

---

### 2. [SINALIZADA, NÃO NOVA] Real-Time Environment Artist — ILM San Francisco (Project Hire)

Esta **não é uma vaga nova**. Ela já foi registrada e **deliberadamente NÃO enviada em 07/09**,
com razão escrita no `docs/index.html`. Eu a trago de volta só porque a leitura do corpo
completo que eu fiz hoje contradiz em parte a razão registrada, e essa decisão é do dono da
campanha, não minha.

| Campo | Valor |
|---|---|
| Estúdio / marca | **ILM (Lucasfilm)** — segmento `ILM San Francisco`, categoria interna `Environment - Studios` |
| Cargo | Real-Time Environment Artist (Project Hire) |
| Cidade / país | **San Francisco, CA, EUA** |
| Formato | **Presencial** (registro da campanha: Workday marca *Primarily On-Site*) |
| Requisição | **`10153285`** |
| Data de publicação | **2026-06-05**, republicada **2026-08-25** (`Posted 14 Days Ago`) |
| Faixa salarial publicada | **US$ 104.300 – US$ 136.900 / ano** |
| `canApply` | `true` |
| Exclusiva deste quadro? | **NÃO** — está nos dois quadros |

**URL (canônica, HTTP 200):**
`https://disney.wd5.myworkdayjobs.com/en-US/disneycareerdc/job/San-Francisco-CA-USA/Real-Time-Environment-Artist---Expression-of-Interest---ILM-San-Francisco_10153285-1`

**Régua de veto:** **ZERO casamento** dos 17 termos em 5.988 caracteres. Limpa.

**Dedupe:**

| Arquivo | Ocorrências |
|---|---|
| `docs/index.html` | **2** |
| `enviados.csv` | **0** |
| `automacao/processados.csv` | **1** |
| `automacao/FILA-DO-VINI.md` | **0** |

→ **Conhecida, registrada, NUNCA enviada.** Está em `index.html` sob a URL do quadro
`disneycareer`, não deste aqui.

**A razão registrada em 07/09, colada:**
> *"REGISTRADA E NAO ENVIADA DE PROPOSITO (…) arte de CENARIO, portfolio que ele nao tem, e
> Project Hire, que e o vinculo mais fraco para visto"*

**O que a leitura de hoje acrescenta:** o corpo **não** é VFX em tempo real (que a regra 1
manda descartar) — é modelagem de ambiente feita em engine. Literal:
*"Model, texture, assemble, edit, and set dress detailed 3D environments in a real-time
engine"*, *"Create and maintain both organic and hard-surface environment assets, materials,
and textures"*, *"Process and clean up photogrammetry assets"*. Ferramentas de bônus: Houdini,
Mari, Quixel, World Machine, Unreal.

**Sem empurrar:** os dois motivos originais continuam de pé — continua sendo **cenário e não
personagem**, e continua sendo **Project Hire** (contrato de projeto, o vínculo mais fraco
para visto). Nada mudou no status da vaga: o título já dizia "Project Hire" em 07/09, e o
slug antigo "Expression-of-Interest" na URL é só resíduo. **A decisão de 07/09 se sustenta.**
Fica aqui como sinalização, não como recomendação de reverter.

---

## 3. O QUE CAIU E POR QUÊ

### 3a. Título bom, corpo reprovou — as armadilhas de verdade

**`10052606` — Sr Generalist Artist, ILM Vancouver** (exclusiva deste quadro, C$ 112.200 –
143.600, publicada 2026-05-27, `canApply: true`, régua **zero casamento**, dedupe **0/0/0/0**).
Passaria em tudo. **Reprovou na disciplina, pelo corpo.** O título diz "Generalist Artist"; a
segunda frase da descrição diz o que o cargo é de fato:

> *"We are looking for a talented and collaborative artist to join our Environments team.
> **As a Digital Matte Painter**, you will create striking digital environments (…) you'll
> craft **digital matte paintings** that blend seamlessly into the animated world, using a mix
> of painted, photographic, and rendered CG elements."*

E os requisitos confirmam: *"Minimum 3 years of production experience in **matte painting**"*,
*"**Proficiency with Photoshop and Nuke**"*, com 3ds Max/Maya/Houdini apenas como *"Good
knowledge"* e ZBrush/Substance como *"is a plus"*. É pintura, não modelagem — exatamente o caso
que a regra 1 manda descartar. **Esta é a vaga que um filtro por título teria colocado na fila
por engano.**

**`10154021` — CG Supervisor (Expression of Interest), ILM Vancouver** (exclusiva, C$ 159.000
– 203.500, régua zero, dedupe 0/0/0/0). Reprovou na disciplina: não é supervisão de modelagem/
texturização/look dev, é supervisão de **pipeline e infraestrutura** — *"manage rendering and
storage resources"*, *"Oversee pipeline ticket queues"*, *"Resource Forecasting"*, *"Asset &
Data Security"*. Some-se que o próprio anúncio avisa que a vaga **não está aberta**:
> *"This posting is an opportunity to submit your resume for future consideration; **this is
> not a role that is open at this time**."*

**`10160228` — CG Technology Supervisor, ILM Vancouver** (exclusiva, régua zero, dedupe
0/0/0/0). Mesma reprovação, mais funda: é estratégia global de tecnologia e pipeline
(*"Pipeline Strategy & Workflow team"*, *"roadmapping"*, *"global prioritization processes"*).
TD/engenharia pura.

**`10157562` — Creature TD (all levels), ILM London.** Título com "Creature" atrai, corpo
descarta: *"responsible for setting up and running flesh-surface, hair, cloth, rigid body
**simulations** as well as being able to wrangle **rigging**"*. A categoria interna do próprio
Workday é `Rigging - Studios`. CFX/simulação + rigging puro — as duas exclusões explícitas.

**`10158840` — Sr. VFX Artist, Glendale.** É **VFX em tempo real**, a primeira exclusão da
regra 1: *"atmospherics, weather and environmental effects created in **Unreal 5, Niagara***"*,
*"shaders, particles systems, physics, ribbons"*.

**`10153466` — Senior Technical Artist, ILM SF.** Arte técnica / ponte com engenharia:
*"key liaison between the content and engineering teams"*. TD puro.

**`10157163` — Senior Concept Artist, ESPN (Remoto EUA)**, US$ 112.700 – 154.800. Não é
visual development de personagem: é **motion graphics e identidade de marca esportiva** —
*"broadcast graphics, video editing, motion design"*, *"on-air motion graphic brand
identities"*. 2D/broadcast, nada de 3D.

**`10159662` — Background Paint Lead, DTVA** e **`10159759` — Location Design Lead, DTVA**.
Background paint é pintura; design de locação 2D é exclusão nominal da regra 1. Ambas já
tinham sido barradas pela campanha em 05/09 pelo mesmo motivo.

**`10151474` Background Painter**, **`10151476` Color Designer**, **`10151479` Location
Designer** (DTVA) — mesma família, mesma reprovação: cor e pintura 2D.

**`10159072` Designer I** e **`10157164` Designer II** (ESPN Bristol) — gráficos de transmissão.
**`10159657` Sr Designer** (Seattle) — produto/UX.

### 3b. Caíram só pela geografia — a perda mais cara do quadro

Todas passariam na disciplina com folga. **A Índia está fora do escopo por regra**, e é onde a
ILM concentrou as vagas de personagem e modelagem:

| Req | Cargo | Local | Observação |
|---|---|---|---|
| `10154147` | **Sr Character Modeler** | West Mumbai, Índia | o alvo mais central do quadro inteiro |
| `10155895` | Lead Modeler | Mumbai, Índia | |
| `10146393` | Lead Environment Artist | Mumbai, Índia | exclusiva deste quadro |
| `10155332` / `10155202` | Look Dev TD / Sr Look Dev TD | Mumbai, Índia | |
| `10152365` | Sr Generalist Artist | Mumbai, Índia | exclusiva deste quadro |
| `10152359` | Generalist Artist Mid-Senior (DMP) | Mumbai, Índia | também cairia por ser DMP |
| `10146744` / `10145923` / `10146395` | CG Sup / Creature Sup / Environment Sup | Mumbai, Índia | |

Fora do escopo também: `10099717` (Shanghai), `10043230` (Shanghai), `10124369` (Shanghai),
`10160270` (Filipinas). Nenhuma vaga de arte 3D apareceu em **Coreia do Sul** ou **Singapura**
(Singapura tem 14 vagas no quadro, todas corporativas/comerciais).

### 3c. Removidas pelo dedupe — já são suas

**`10159882` — Senior Modeler, ILM Sydney.** É a vaga mais perfeita do quadro para o portfólio
dele (*"both organic sculpting and hard surface modeling"*, *"creatures, characters, vehicles,
props and environments"*, Maya + ZBrush, híbrido 2 dias, `canApply: true`). **Já foi enviada e
confirmada em 04/09.** Dedupe: `index.html` = **3**, `enviados.csv` = 0, `processados.csv` =
**14**, `FILA-DO-VINI.md` = 0. Trecho colado do `processados.csv`:
> *"ENVIADA E CONFIRMADA NA TELA: Senior Modeler da ILM Sydney, requisicao 10159882, pelo
> Workday oficial da Disney; o Candidate Home (…) Application Received September 4, 2026"*

**`10159762` — Character Design Lead, DTVA Glendale** (presencial, US$ 74,68–82/h). Conta como
disciplina pela porta de *visual development de personagem* — *"developing the look, personality
and feel of characters"*, *"Create turnarounds, special poses, mouth charts and expression
sheets"* — com a ressalva honesta de que é design 2D para série, não modelagem. **Já foi
enviada em 02/09.** Dedupe: `index.html` = **3**, `processados.csv` = **9**. Trecho:
> *"NAO REAPLIQUEI: a requisicao 10159762 ja tinha sido enviada em 02/09 pelo Workday da Disney"*

**`10137201` — Pre-Visualisation Generalist Artist, ILM London.** Enviada e confirmada em
09/09, como o próprio briefing já dizia. Dedupe: `index.html` = **3**, `enviados.csv` = **2**.

---

## 4. ARMADILHAS DE MÉTODO ENCONTRADAS

Esta seção vale tanto quanto a fila. Foram quatro, e uma delas invalida a premissa da tarefa.

### 4.1 — A premissa "643 vagas nunca varridas" está metade errada: os dois quadros se sobrepõem em 50%

Eu varri **também** o `disneycareer` (626 vagas, 32 páginas) só para cruzar os IDs de requisição.
Resultado medido:

| Medida | Número |
|---|---|
| IDs únicos em `disneycareer` | 626 |
| IDs únicos em `disneycareerdc` | 642 |
| **Mesma requisição publicada nos DOIS quadros** | **323** |
| **Exclusivas de `disneycareerdc`** | **319** |

Ou seja: **50,3% do `disneycareerdc` é republicação do quadro que a campanha já usa.** O
"quadro novo de 643 vagas" é, na prática, ~319 vagas novas. E o padrão é limpo e verificável:
**toda** vaga deste quadro que já aparece nos arquivos da campanha é uma das 323 compartilhadas
(alcançada pelo `disneycareer`), com uma única exceção — a `10137201`, que é exclusiva daqui e
foi a candidatura que estreou este quadro.

### 4.2 — O quadro já tinha sido tocado: 16 dos 642 IDs já estão nos arquivos da campanha

Contra-medida da premissa "nunca varrido". Cruzei **os 642 IDs, um por um**, contra os quatro
arquivos. **16 já estavam lá** — e não por acaso: são justamente os de arte/3D. Entre eles duas
candidaturas enviadas e confirmadas (`10159882`, `10159762`) e várias recusas com razão escrita
(`10153285`, `10153466`, `10159662`, `10159759`, `10157562`, `10144787`, `10155976`).

O que é verdade é só a versão fraca: a **string** `disneycareerdc` aparece **1 vez** no
`docs/index.html`, **1 vez** no `enviados.csv` e **0** nos outros dois. O quadro estava
sub-representado por nome — mas seu conteúdo de arte já tinha sido, em grande parte, trabalhado
por outra porta.

**Lição de método: dedupe por ID de requisição pegou o que dedupe por nome de quadro não pegaria.**
Se eu tivesse confiado no `grep disneycareerdc = 0`, teria colocado a Senior Modeler de Sydney na
fila e o Vini teria reaplicado numa vaga já confirmada.

### 4.3 — `externalPath` já contém `/job`: montar a URL de detalhe concatenando `.../job` + `externalPath` devolve 406 em 100% dos casos

O endpoint de detalhe do briefing está descrito como
`GET .../disneycareerdc/job/<externalPath>`. Mas o campo `externalPath` da listagem **já vem
com o prefixo `/job`** (ex.: `/job/Vancouver-BC-Canada/Lead-Generalist-Artist_10142674`).
Concatenar os dois produz `.../disneycareerdc/job/job/...` e o Workday responde **`406 Not
Acceptable`** — não 404. As minhas 20 primeiras requisições de detalhe voltaram **20/20 com
406**, e o código enganoso me fez perder um ciclo checando cabeçalhos `Accept` (que estavam
certos). A base correta é `.../disneycareerdc` + `externalPath`. Depois da correção: **20/20
com 200.**

### 4.4 — Slug de URL mente sobre o cargo; o título é o campo confiável

A `10153285` continua com o slug `Real-Time-Environment-Artist---Expression-of-Interest---ILM-
San-Francisco_10153285` nos **dois** quadros, mas o campo `title` nos dois já diz **"(Project
Hire)"**. O slug é resíduo de quando a vaga era Expression of Interest. Quem ler o cargo pela
URL classifica errado o tipo de vínculo — que aqui é justamente o critério que pesou na decisão
de não enviar. **Ler `title`/`jobPostingInfo`, nunca o slug.**

Variante disso, e é erro do lado da Disney: a **`10159662` (Background Paint Lead)** tem o corpo
**trocado**. O texto diz *"you may be considered for any **Character Designer** positions"* e
depois *"The **Character Design Lead** will work directly with the team"* — é o corpo da
`10159762` colado dentro do anúncio de Background Paint. Um filtro que lesse o corpo em busca de
"Character" marcaria uma vaga de pintura de background como vaga de personagem.

### 4.5 — Coisas que checei e que NÃO eram armadilha

- **Paginação não mente.** `total` declarado = 642; soma das 33 páginas = 642; `externalPath`
  únicos = 642; `jobReqId` únicos = 642; zero página vazia; zero ID repetido. Nenhum
  deslocamento, nenhuma duplicata de fronteira de página.
- **A regra do `limit` confere.** `limit=20` → 200. Testei `limit=50` → **400**; `limit=100` →
  **400**. Exatamente como o briefing dizia.
- **Nenhum dado de demonstração.** Todas as 20 descrições vieram com texto real, específico e
  coerente com o título (fora a 4.4), entre 2.213 e 6.970 caracteres.
- **`canApply: true` nas 20** descrições baixadas — nenhuma vaga zumbi entre as candidatas.

---

## 5. RÉGUA DE VETO — RESULTADO LITERAL, TODAS AS 20 DESCRIÇÕES

Os 17 termos foram rodados sobre o **texto integral** de cada descrição (HTML limpo), não sobre
o resumo. **14 das 20 deram zero casamento.** As 6 com casamento estão abaixo, com a frase em
volta colada e o julgamento.

| Req | Termo | Frase colada | Julgamento |
|---|---|---|---|
| `10159662` | `based in` | *"Location — This is a fully on-site role **based in** Glendale, CA."* | **Falso positivo.** Diz onde o CARGO fica, não quem pode se candidatar. |
| `10159762` | `based in` | *"Job Location — This is a fully on-site role **based in** Glendale, CA."* | **Falso positivo.** Idem. (Útil como dado: confirma presencial.) |
| `10159882` | `located in` | *"ILM is the leading effects facility in the world, with studios **located in** San Francisco, Vancouver, London, Sydney and Mumbai."* | **Falso positivo.** Endereço dos estúdios, exatamente o caso já medido. |
| `10151474` | `based in` | dentro de *"…apply color, textures and details to approved background designs…"* — casamento por colagem de fim/início de frase no texto corrido | **Falso positivo.** Não é sentença de elegibilidade. |
| `10151476` | `based in` | mesma colagem, em bloco de responsabilidades de color design | **Falso positivo.** |
| `10151479` / `10159759` | `based in` | mesma colagem, em bloco de responsabilidades de location design | **Falso positivo.** |

**Nenhum veto escrito em nenhuma das 20 vagas.** Zero ocorrência de `authoriz`, `eligib`,
`sponsor`, `work permit`, `must be based`, `only from`, `LMIA`, `unable to support`,
`no relocation`, `relocat` ou exigência de idioma local em qualquer descrição analisada.
Nenhuma vaga foi descartada pela régua — **as 5 que chegaram nela passaram todas.**
As perdas foram todas de disciplina (regra 1), geografia (regra 2) e dedupe (regra 4).

---

## 6. LEITURA HONESTA DO RESULTADO

O quadro rendeu **uma** vaga nova: a **Lead Generalist Artist da ILM Vancouver (`10142674`)**,
C$ 126.800–162.300, híbrida, régua limpa, zero nos quatro arquivos, URL viva. É ambiente e não
personagem, e tem componente de matte painting — mas é modelagem, texturização e look dev com
liderança, e é a maior faixa publicada do quadro.

O quadro **não** rendeu nenhuma vaga de personagem inédita. As duas que existiam
(`10159882` Senior Modeler Sydney e `10159762` Character Design Lead) **já são candidaturas
enviadas e confirmadas** — 04/09 e 02/09. O pedido "qualquer vaga do grupo Disney em arte
próxima da minha área, somos os primeiros a nos inscrever" já está, nesta parte, cumprido: nas
duas mais próximas do centro do portfólio, a campanha chegou primeiro.

A maior perda do quadro é geográfica e não tem conserto dentro das regras: a ILM concentrou em
**Mumbai** um `Sr Character Modeler`, um `Lead Modeler` e um `Lead Environment Artist` — os três
alvos mais centrais que apareceram em 642 vagas.
