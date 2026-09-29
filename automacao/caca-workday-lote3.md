# Caça ao Workday — LOTE 3 — 10/09/2026, madrugada

Terceira varredura do Workday, feita depois de ler `automacao/caca-workday.md` (lote 1),
`automacao/caca-workday-lote2.md` (lote 2) e `automacao/PROXIMA-RODADA-workday.md`. Tudo abaixo foi
rodado com `python3`/`requests` e `curl`, **nenhum navegador foi aberto** (o Chrome estava com outro
agente, `pgrep -c chrome` = 10 durante a sessão inteira). Nada foi enviado, nenhum formulário foi
preenchido, e `docs/index.html`, `enviados.csv` e `automacao/FILA-DO-VINI.md` **não foram tocados**.

Esta rodada obedece à **REGRA DO VINI de 10/09**: personagem e criatura primeiro, modelagem e
superfície genéricas só quando o corpo do anúncio cita personagem, e ambiente por último e nunca
como carro-chefe.

---

## 1. PLACAR, antes de qualquer narrativa

| Medida | Número |
|---|---|
| Nomes de locatário (slugs) sondados | **5.448** |
| Pods testados | **15** (todos os que existem) |
| Requisições de sondagem (`GET robots.txt`) | **83.175** |
| **`422`** (locatário NÃO existe naquele pod) | **83.124** |
| **Locatários que EXISTEM** | **47** |
| — destes, **novos para a campanha** | **46** (o 47º é `ea`, parede de `401` já catalogada) |
| — `200`, o `robots.txt` revela os sites | **37** |
| — `401`, API pública fechada | **10** |
| Sites revelados pelo `robots.txt`, sem um palpite | **93** |
| Quadros com vaga dentro, paginados 100% | **71** |
| **Vagas colhidas em locatários NOVOS** | **14.378** |
| Vagas colhidas na **reauditoria** dos quadros de arte já conhecidos | **3.608** (25 quadros) |
| **Total de vagas lidas nesta sessão** | **17.986** |
| Bateram no filtro de título | **135** |
| — destas, **ruído de título** (RH, engenharia, finanças, ator fantasiado) | **69** |
| — **vagas de ARTE de verdade** | **66** |
| Sobreviveram ao **escopo geográfico** | **49** (17 caíram: Índia, China, Japão, Ucrânia) |
| Sobreviveram ao **filtro de DISCIPLINA**, com o corpo lido | **16** (33 caíram) |
| Sobreviveram à **régua de veto** | **16** (o único veto escrito já tinha caído por disciplina) |
| Sobreviveram ao **dedupe por ID de requisição** | **2** (14 já enviadas ou já recusadas) |
| **FILA FINAL PRONTA PARA DISPARAR** | **2** — **1 de PERSONAGEM e 1 de AMBIENTE** |

**Seja honesto com o número: 46 locatários Workday inéditos entraram no mapa e eles renderam UMA
vaga.** A reauditoria dos quadros de arte que a campanha já lê rendeu outra, e ela é de ambiente.
**A quebra que o Vini pediu: 1 de personagem, 1 de ambiente, 0 enviadas nesta rodada** (esta rodada
não envia; quem envia é a seguinte).

**A quebra por disciplina, que é o número que o Vini pediu.** Das 16 que passaram por escopo e
disciplina:

- **PERSONAGEM: 2.** `JR41751` Character Modeling Supervisor da Netflix Animation Sydney — **e ela
  já foi enviada em 09/09**, com prova de `jobTasks/completed/application`. Sobra **uma**, a da
  Razer, que é a nº 1 da fila.
- **AMBIENTE: 5.** `JR41734`, `JR41749`, `JR39446` e `JR39273` da Netflix Animation **já saíram
  todas em 09/09**; sobra `JR41288`, que é a nº 2 e está em último de propósito.
- **Modelagem e superfície genéricas: 9**, e **as nove já foram enviadas ou recusadas** (as três da
  Eyeline de Seul, as três de textura e modelagem da ILM, a Vehicle Artist da CIG, e as duas
  generalistas da ILM).

**Ambiente descartado antes da fila: 4** — `JR40916` Environment Lead da Eyeline Seul (matte
painting), `10153285` Real-Time Environment Artist da ILM São Francisco (tempo real, já recusada de
propósito) e `10146395`/`10146393` da ILM Mumbai (Índia). **Nenhuma delas foi apresentada como
resultado.**

---

## 2. A FILA PRONTA

Ordenada por quanto encosta no centro do portfólio: personagem primeiro.
As duas URLs públicas foram testadas nesta sessão e devolveram **HTTP 200**.

O comando é sempre o mesmo, trocando os quatro últimos argumentos:

```
cd /home/user/apply
VINI_TEL="<telefone, do doc privado do Drive>" VINI_RUA="<rua>" VINI_CEP="<cep>" \
VINI_SAL="<pretensão>" \
sh hb_run.sh wd_geral.js <host> <site> <jobpath> <apelido> [ENVIAR]
```

Sem o `ENVIAR` no fim ele para na Review e não envia. **Refaça o dedupe no minuto do disparo**
(`sh automacao/dedupe-agora.sh <ID> "<Casa>"`), nunca contra esta fila: fila envelhece em horas.

---

### 2.1 — PERSONAGEM

**1. Senior Character Designer (6 months contract) — Razer, Singapura**

- Locatário / site / pod: `razer` / `Careers` / **`wd3`** — **casa nova, a campanha nunca tocou nela**
- host: `razer.wd3.myworkdayjobs.com`
- jobpath: `Singapore/Senior-Character-Designer--6-months-contract-_JR2026007640`
- **Requisição: `JR2026007640`** · Singapura (**dentro do escopo asiático permitido**)
- Postada 2026-07-06 · `Full time`, contrato de 6 meses · Faixa: **não publicada**
- URL pública (testada hoje, **200**):
  https://razer.wd3.myworkdayjobs.com/en-US/Careers/job/Singapore/Senior-Character-Designer--6-months-contract-_JR2026007640
- **Régua de veto, termo a termo sobre o DETALHE completo (5.337 caracteres):**
  `authoriz` 0 · `eligib` 0 · `sponsor` 0 · `work permit` 0 · `must be based` 0 · `LMIA` 0 ·
  `days a week` 0 · `citizen` 0 · `resident` 0 · `visa` 0 · `relocat` 0 · `onsite`/`on-site` 0 ·
  `in-office` 0 · `hybrid` 0 · `right to work` 0 · `security clearance` 0.
  **ZERO casamento dos 17 termos. Nenhum veto escrito. Limpa.**
- **Dedupe `JR2026007640`:** `enviados.csv` **0** · `automacao/processados.csv` **0** ·
  `docs/index.html` **0** · `automacao/FILA-DO-VINI.md` **0**. **INÉDITA.**
  A casa também é inédita: as três "ocorrências" de `razer` no painel são a palavra portuguesa
  **tra*zer*** dentro de "trazer de volta", conferidas uma a uma. **Razer nunca recebeu nada.**
- **Por que é a nº 1:** é a **única vaga com PERSONAGEM no centro** que as 17.986 vagas desta
  varredura produziram dentro do escopo. Frase do anúncio: *"The Senior Character Designer conceives
  and leads the creation of new avatars from the ground up (including the identity, backstory,
  emotional register, visual world). This role owns how the avatars look, moves, and express
  themselves. Directs the full visual pipeline from concept art through animation to marketplace
  skins."*
- **RESSALVA HONESTA, e ela é grande:** o anúncio **não pede modelagem 3D em nenhum ponto**. Não
  cita Maya, ZBrush, Substance nem Blender. É **direção de personagem**, não produção: *"This is a
  review and direction role, not hands-on trait tuning"*, e a qualificação pedida é *"Background in
  character design, art direction, or creative direction — ideally in games, animation, or
  interactive entertainment where characters are products, not illustrations"*, mais *"Experience
  directing external studios or production houses"*. O trabalho hands-on vai para um estúdio
  externo. Não é escultura nem modelagem, e por isso não é encaixe perfeito — **mas é personagem,
  é sênior, é casa grande de jogos e está no escopo.** Pela regra 13 (porta de entrada) e pela ordem
  do Vini de 10/09, ela vem antes de qualquer ambiente. **A decisão de disparar é da rodada
  seguinte, com esta ressalva na mão.**
- **Pretensão a usar:** sem faixa publicada, Singapura não está na tabela do briefing. Use o texto
  que passou na Eyeline de Seul em 09/09, sem número:
  `Open to aligning with your band for the role.`
- **Comando:**

```
cd /home/user/apply
VINI_TEL="<telefone>" VINI_RUA="<rua>" VINI_CEP="<cep>" \
VINI_SAL="Open to aligning with your band for the role." \
sh hb_run.sh wd_geral.js razer.wd3.myworkdayjobs.com Careers \
  "Singapore/Senior-Character-Designer--6-months-contract-_JR2026007640" razerchar
```

(rode primeiro **sem** `ENVIAR`, leia a Review, e só então repita com `ENVIAR` no fim)

---

### 2.2 — AMBIENTE (por último, e não é o carro-chefe da rodada)

**2. Head of Environments — Netflix Animation Studios, Vancouver**

- Locatário / site / pod: `netflix` / `Netflix` / `wd108`
- host: `netflix.wd108.myworkdayjobs.com`
- jobpath: `Vancouver/Head-of-Environments_JR41288`
- **Requisição: `JR41288`** · Vancouver, BC, Canadá · Postada 2026-08-06 · `Full time`
- **Faixa publicada: `"The overall market range for this role is typically $204k - 279k CAD. This
  reflects total compensation; we do not have stock options."`** — é a maior faixa que a campanha
  já viu numa vaga de arte.
- URL pública (testada hoje, **200**):
  https://netflix.wd108.myworkdayjobs.com/en-US/Netflix/job/Vancouver/Head-of-Environments_JR41288
- **Régua de veto, termo a termo sobre o DETALHE completo (5.842 caracteres) — 2 casamentos,
  NENHUM é veto:**
  - `days a week` → frase inteira: *"This role is based in Vancouver, British Columbia. Hybrid Role
    (Minimum of 3 days a week in the office)."* → **restrição de presença no escritório, não regra
    de quem pode se candidatar.** É o mesmo padrão já classificado pela campanha em 09/09 nas
    quatro da Netflix Animation.
  - `hybrid` → a mesma frase. Mesma classificação.
  - `authoriz` 0 · `eligib` 0 · `sponsor` 0 · `work permit` 0 · `must be based` 0 · `LMIA` 0 ·
    `citizen` 0 · `resident` 0 · `visa` 0 · `relocat` 0 · `right to work` 0 · `security clearance` 0.
    **Nenhum termo de imigração casou.**
- **Dedupe `JR41288`:** `enviados.csv` **0** · `automacao/processados.csv` **0** ·
  `docs/index.html` **1 ocorrência SEM marca de envio** (*"JR41288, lideranca de todos os ambientes,
  cenarios e props, tambem sem veto: o based in que aparece diz onde o cargo FICA, nao quem pode se
  candidatar"*) · `automacao/FILA-DO-VINI.md` **1 ocorrência**. **REGISTRADA E NUNCA ENVIADA.**
  A seção 2 do `dedupe-agora.sh` (marcas de envio) deu **vazia**.
- **Disciplina, sem maquiagem:** é **AMBIENTE**, e por isso está em último. O corpo diz
  *"the show-based leader for all digital environments, sets, and props"* e
  *"oversee the environment asset teams—including Modeling, Surfacing, and Matte Painting"*.
  Pede *"At least 10 years of experience in environment asset creation"* e
  *"Proven production-level proficiency in Maya and ZBrush/Mudbox, texturing packages (Substance,
  Mari, Photoshop)"*. **Nenhuma menção a personagem ou criatura no anúncio inteiro.**
- **Nota de cadência:** a Netflix recebeu **seis candidaturas em 09/09** pelo Workday. Se a regra de
  uma casa por rodada valer, esta espera a virada.
- **Pretensão a usar:** faixa publicada, pede-se a base → `CAD 204,000`, com a frase de alinhamento.
- **Comando:**

```
cd /home/user/apply
VINI_TEL="<telefone>" VINI_RUA="<rua>" VINI_CEP="<cep>" \
VINI_SAL="CAD 204,000" \
sh hb_run.sh wd_geral.js netflix.wd108.myworkdayjobs.com Netflix \
  "Vancouver/Head-of-Environments_JR41288" nasheadenv
```

---

## 3. EPIC GAMES E KRAFTON — RESOLVIDOS, e a resposta é ruim

O lote 1 deixou os dois como "nunca resolvidos": `robots.txt` devolvia `200` com **corpo vazio** e
o endpoint de vagas devolvia `404` em ~75 caminhos de site testados. **Achei os dois sites, e não foi
por palpite: foi por eliminação do erro.** O truque é que a mensagem de erro do `404` distingue duas
coisas que o lote 1 tratava como uma só.

```
POST https://<pod>.myworkdaysite.com/wday/cxs/<locatario>/<SITE>/jobs
```

- `404 {"message":"not found: Job_Posting_Site_ID=<SITE>"}` → **o locatário responde, o SITE é que
  está errado.** Vale continuar procurando.
- `403 {"errorCode":"S22","message":"permission denied"}` → **o SITE EXISTE e a API pública está
  desligada por permissão.** Não adianta mais nenhum palpite.
- `401 {"message":"Unable to verify credentials for system user"}` → **o LOCATÁRIO inteiro está
  fechado.** É a parede que o lote 1 chamou de `401`.

Medido:

| Locatário | Site verdadeiro | Resposta da API | Veredito |
|---|---|---|---|
| `epicgames` / `wd5` | **`Epic_Games`** | `403 permission denied` | **precisa-de-navegador** |
| `krafton` / `wd3` | **`KRAFTON`** | `403 permission denied` | **precisa-de-navegador** |

As URLs públicas para o navegador dele são
`https://epicgames.wd5.myworkdayjobs.com/en-US/Epic_Games` e
`https://krafton.wd3.myworkdayjobs.com/en-US/KRAFTON`. **Nenhum `curl` vai ler essas duas.**
Os dois sobem para o topo da lista de `precisa-de-navegador`, acima de EA, DNEG e Keywords, porque
os dois são casas de jogos que contratam artista de personagem e porque **agora se sabe o caminho
exato**, o que economiza a busca dentro do navegador.

**Descoberta lateral que vale para toda a campanha: `https://<pod>.myworkdaysite.com/wday/cxs/...`
é um host ALTERNATIVO que serve a mesma API.** Conferido contra a Disney: o mesmo POST em
`wd5.myworkdaysite.com/wday/cxs/disney/disneycareer/jobs` devolveu `200` com `"total":633`, idêntico
ao host `disney.wd5.myworkdayjobs.com`. Serve de rota de contorno se um dos dois hosts cair.
**Não abre nada que o outro não abra:** os `401` de EA, DNEG, Riot, Keywords, Sony Interactive,
Roblox, Mattel, Discord, Twitch, Gameloft, Saber, Motive e Bungie **respondem `401` idêntico pelos
dois hosts.** Testei os treze.

---

## 4. OS LOCATÁRIOS NOVOS QUE EXISTEM E NÃO TÊM VAGA DA DISCIPLINA

Para a próxima rodada não gastar sondagem neles de novo. Todos com quadro **paginado 100%** nesta
sessão, salvo onde escrito.

| Locatário / pod | Sites revelados pelo `robots.txt` | Quem é de verdade | Vagas | Da disciplina |
|---|---|---|---|---|
| **`razer`/wd3** | `Careers` | **Razer**, hardware e software de jogos | 168 | **1** → é a nº 1 da fila |
| **`sky`/wd3** | `sky_careers`, `broadbean_external`, `TUX` | **Sky Group** (Comcast), Osterley/Londres | 320 | **0** |
| **`lnw`/wd5** | `LightWonderExternalCareers`, `SciPlayExternalCareersSite`, `GroverGamingExternalCareerSite` | **Light & Wonder** + SciPlay + Grover Gaming | 134 | **0** (ver §6) |
| **`sonyglobal`/wd1** | `SonyGlobalCareers`, `SonyJapanCareers`, `Sony_Europe_Careers` | Sony Corporation of America / Sony Europe / Sony Japan — **corporativo, não é a Imageworks** | 143 | **0** (ver §6) |
| **`maxon`/wd103** | `MAXO` | **Maxon**, a dona do Cinema 4D, do Redshift e do **ZBrush** | 6 | **0** — as 6 são marketing, IT e um dev de Redshift |
| **`iyuno`/wd3** | `Careers` | **Iyuno**, dublagem e legendagem | 56 | **0** — engenharia de áudio, legenda, gestão |
| **`livenation`/wd503** | `LNExternalSite`, `InsomniacExternalSite`, `TMExternalSite`, `RNExternalSite` | **Live Nation / Ticketmaster / Insomniac Events** — o Insomniac aqui é de festas de música eletrônica, **não é o Insomniac Games** | 1.711 | **0** |
| **`seaworldentertainment`/wd1** | `SEA`, `auditions` | SeaWorld / Busch Gardens / Sesame Place | 428 | **0** — os "Character" são **atores fantasiados** |
| **`logitech`/wd5** | `Logitech` | Logitech | 203 | **0** |
| **`mgmresorts`/wd5** | `MGMCareers` + 12 quadros sindicais | MGM Resorts, cassinos de Las Vegas | 520 | **0** |
| **`cognex`/wd1** | `External_Career_Site` | Cognex, visão de máquina industrial | 84 | **0** |
| **`ptc`/wd1** | `PTC` | PTC, software de CAD/PLM | 175 | **0** |
| **`tp`/wd107** | `TP-ICAP` | TP ICAP, corretora financeira | 120 | **0** |
| `ag`/wd3 | `Airbus`, `Airbus_Specific` | Airbus | 2.000 | **0** |
| `wf`/wd1 | `WellsFargoJobs`(+1) | Wells Fargo | 1.747 | **0** |
| `ms`/wd5 | `External`, `private` | Morgan Stanley | 1.713 | **0** |
| `cc`/wd3 | `ChanelCareers` | Chanel | 1.118 | **0** |
| `pg`/wd5 | `1000`, `1001` | Procter & Gamble | 786 | **0** |
| `nc`/wd108 | `NC_Careers` | Estado da Carolina do Norte | 772 | **0** |
| `bne`/wd1 | `Hardees`, `HVAC` + 4 | Boddie-Noell (rede Hardee's) | 867 | **0** |
| `uw`/wd5 | `UWHires` | Universidade de Washington | 565 | **0** |
| `hl`/wd1 | `Lateral`, `Corporate`, `Campus` + 2 | Houlihan Lokey, banco de investimento | 156 | **0** |
| `brown`/wd5 | `staff-careers-brown`(+1) | Universidade Brown | 108 | **0** |
| `mc`/wd1 | `external` + 2 | — corporativo | 76 | **0** |
| `nb`/wd1 | `NBCareers`, `PWM` | Neuberger Berman | 106 | **0** |
| `gh`/wd1 | `gh`, `Private_Posting` | — | 71 | **0** |
| `ig`/wd103 | `EXT_IG` + 6 | Investec | 57 | **0** |
| `bb`/wd3 | `BlackBerry`, `QNX` + 3 | BlackBerry | 49 | **0** |
| `ts`/wd5 | `tishmanspeyer`, `rainbowroom` + 3 | Tishman Speyer, imobiliária | 43 | **0** |
| `us`/wd103 | `Tobii_Dynavox` | Tobii Dynavox | 21 | **0** |
| `aa`/wd105 | `AA` | — | 14 | **0** |
| `ah`/wd108 | `AvenHospitalityJobs`, `confidential` | hotelaria | 33 | **0** |
| `tn`/wd1 | `Telenav_Careers` + 2 | Telenav | 8 | **0** |
| `3i`/wd103 | `Intern_Career`, `Direct_Hire` | 3i Group | 5 | **0** |
| `blvd`/wd501 | `external` | — | 0 (vazio) | **0** |
| `mx`/wd1 | (robots sem `Allow`) | — | — | **0** |
| `fc`/wd10 | **`robots.txt` `200` com corpo VAZIO** | — | — | site não revelado; nome genérico, prioridade zero |

**Nove locatários `401` novos** — existem, e a API pública está desligada. Mesmo comportamento da
parede já documentada nos lotes 1 e 2, e **confirmado hoje pelos dois hosts** (`myworkdayjobs.com`
e `myworkdaysite.com`):

`applovin`/wd1 · `audible`/wd12 · `boydgaming`/wd1 · `lucid`/wd1 · `mt`/wd103 · `siemens`/wd3 ·
`vailresorts`/wd501 · `jp`/wd102 · `rf`/wd504

**Nenhum destes nove vale `precisa-de-navegador` para a disciplina.** O único de jogos é a AppLovin,
que é publicadora mobile e adtech, sem arte 3D hero. A fila de navegador continua sendo, em ordem:
**Epic Games, Krafton, EA, DNEG, Keywords, Sony Interactive.**

---

## 5. FALSOS AMIGOS NOVOS — nome de estúdio que não é estúdio

Some-se aos seis do lote 1 (`mpc`, `axis`, `icon`, `tt`, `spe`, `grab`) e aos dez do lote 2
(`deluxe`, `sds`, `ci`, `tti`, `carbon`, `qualcomm`, `mercury`, `sandiego`, `aurora`, `sgs`).

| Locatário | Quem realmente é | Por que engana |
|---|---|---|
| `livenation`/wd503, quadro `InsomniacExternalSite` | **Insomniac Events**, o produtor do EDC e de festivais de música eletrônica | O quadro se chama "Insomniac". **NÃO é o Insomniac Games** da PlayStation. 201 vagas, nenhuma de arte. |
| `seaworldentertainment`/wd1 | SeaWorld / Busch Gardens / Sesame Place | O filtro de título casa **cinco** vezes com "Character": *Costume Character*, *Character Host*, *ENTERTAINMENT PERFORMER AND CHARACTER AUDITIONS*. São **atores fantasiados**, não arte 3D. É a maior fábrica de falso positivo da palavra "character" que já apareceu. |
| `sonyglobal`/wd1 | **Sony Corporation of America**, Sony Europe e Sony Japan — eletrônica, música e corporativo | Tem "Culver City" nos endereços, que é o lote da Sony Pictures, mas **não é a Imageworks nem a Sony Pictures Animation**. A única vaga 3D dele tem veto escrito (§7). |
| `maxon`/wd103 | Maxon, dona do **ZBrush** | O nome é a ferramenta principal do portfólio dele. **Fabricante de software não contrata artista de personagem**: as 6 vagas são marketing, IT e um dev de Redshift para arquitetura. |
| `tp`/wd107 | **TP ICAP**, corretora interdealer | Sigla que parece estúdio. 120 vagas, zero de arte. |
| `lnw`/wd5 | Light & Wonder / SciPlay | É estúdio de jogos de verdade, mas o produto é **caça-níquel 2D** (§6). |
| `nc`/wd108 | Estado da Carolina do Norte | Parece **NCSOFT**. Não é. 772 vagas públicas. |
| `ag`/wd3 | **Airbus** | Parece sigla de estúdio alemão. Produz 8 casamentos de "Modelling" que são engenharia aeroespacial. |
| `da`/wd109, `gearboxpublishing`/wd10, `dassaultsystemesentertainment`/wd503 | **NÃO EXISTEM** | Devolveram `429` na varredura e `422` na reconferência. Ver §8, armadilha 3. |

---

## 6. O QUE CAIU, E POR QUÊ — as 135 que bateram no título

Nenhuma inventada, nenhuma escondida. Digo o motivo bloco a bloco.

### 6.1 — Caíram por DISCIPLINA, e são as que mais doem (8)

- **`10159762` Character Design Lead — Disney Television Animation, Glendale.** Título perfeito,
  categoria interna do Workday literalmente `Primary Job Posting Category: Modeling`, e o corpo
  reprova: *"Knowledge of drawing software that includes Photoshop, Illustrator, Harmony and 3D
  technology, where applicable"*, *"Create turnarounds, special poses, mouth charts and expression
  sheets and provide a clean pass of the final approved design"*. É **character design 2D**,
  excluído pela regra do Vini de 10/09. Pagava USD 74,68–82,15 por hora por acordo coletivo.
  **E o dedupe resolveria de qualquer jeito: `10159762` tem 10 ocorrências em `processados.csv` e
  foi ENVIADA em 02/09, com status Application Received.** É a prova de que o dedupe por ID pega o
  que a leitura de título deixaria passar.
- **`JR2026007640` da Razer é o contra-exemplo** e por isso está na fila: também é "design", mas o
  corpo é sobre **quem o personagem é e como ele se move**, não sobre desenhar folhas de expressão.
- **`JR-118922` Senior 3D Visualization and Animation Technical Artist — Sony Corporation of
  America, Culver City.** Disciplina errada (**arte técnica**), e tem veto escrito (§7).
  Faixa publicada USD 140.000–155.000, contrato de um ano.
- **`R322557` Senior Game Artist — Light & Wonder, Montreal (Canadá, no escopo).** O título passa,
  o corpo reprova com todas as letras: *"This is a hands-on creative role focused on producing
  high-quality **2D art assets** for our games"* e *"**7+ years of experience in 2D game art** with
  a strong portfolio. Mastery of Adobe Photoshop"*. 3D aparece só em *"Nice to Have: Familiarity
  with 3D tools and workflows"*. **É o mesmo padrão da Aristocrat de 09/09: caça-níquel é arte 2D.**
- **`R322542` Game Artist e `R322543` Associate Game Artist — Light & Wonder, Sófia (Bulgária, no
  escopo).** Li o corpo da `R322542` inteiro: *"**4+ years of experience in 2D game art**"*, mesma
  frase, mesmo produto. As duas caem juntas.
- **`R322584` / `R322582` Game Artist e Associate Game Artist — Light & Wonder, Montreal.** Mesma
  família, mesmo texto, níveis abaixo do dele.
- **`JR40916` Environment Lead — Eyeline Studios, Seul.** Escopo certo (Coreia do Sul), casa que já
  respondeu bem à campanha, ID **inédito nos quatro arquivos**. E cai por disciplina: o corpo é
  matte painting, que o briefing exclui — *"Minimum five (5) years of previous experience as a
  **Digital Matte Painter** or Environment Artist"*, *"Expert in Adobe Photoshop"*,
  *"Approaches will vary from **2.5D Matte Painting projection setups**, through full 3D asset
  builds"*. **Pintura de cenário está fora, e ambiente já entraria por último.**

### 6.2 — Caíram por DISCIPLINA, arte que nunca foi dele (25)

- `JR41810` e `JR39105` **Head of Character Effects (CFX)** — Netflix Animation Sydney e Vancouver.
  **CFX é simulação**, excluída pelo briefing, exatamente a armadilha que o briefing avisa.
- `JR41777` **Character Designer — Ink (Netflix)** e `JR41752` **Story Artist — Ink**: desenho 2D,
  mesma razão pela qual a `JR41753` foi recusada com motivo escrito em 09/09.
- `10157562`, `10155976`, `10144787` **Creature TD (Rigging)** — ILM Londres e Vancouver, e
  `10126752` **Creatures FX** — ILM Iver Heath. **Creature TD é rigging e Creature FX é simulação.**
  Os quatro continuam fora, como nos lotes 1 e 2. (`10145923` Creature Supervisor cairia junto, mas
  é Mumbai e morre antes, no escopo.)
- `JR101414`, `JR101516`, `JR101198` **Character Concept Artist** — Cloud Imperium, Montreal e
  Manchester. Concept 2D.
- `R0051192` **3D Motion Designer** e `R0056149` **Senior VFX Artist (AI Hybrid) – NxGen Studio** — Sky, Osterley.
  Motion graphics de broadcast e VFX em tempo real: os dois fora.
- `JR-90408` **LN Concerts, 3D Visualization Concept Artist** — Live Nation, remoto Nova York.
  Visualização de palco de show, não personagem.
- `10157163` **Senior Concept Artist** — Disney, remoto EUA. Concept 2D, já descartada no lote 1.
- `10153285` **Real-Time Environment Artist — ILM São Francisco (Project Hire)**: arte de cenário em
  tempo real, recusada de propósito em 07/09 e mantida fora na releitura de hoje.
- `10052606` **Sr Generalist Artist — ILM Vancouver**: *"As a Digital Matte Painter, you will (…)
  craft digital matte paintings"*. Pintura, não modelagem. Mantida fora desde o lote 1.
- `10151475` **Storyboard Artist — Disney Television Animation**, `10157624` **Storyboard Artist (PH)
  — Lucasfilm Animation** e `10159662` **Background Paint Lead — Disney Television Animation**:
  storyboard e pintura de fundo, as três 2D, as três em Glendale/São Francisco.
- `JR41753` **Visual Development Artist — Ink (Netflix)**: **recusada com motivo escrito em 09/09**
  (*"Excellence in draftsmanship"*, Maya e Blender só como *"a significant plus"*). Continua fora.
- `R000106508` **Advanced Level Artist — WB Games Montreal**: level art, e **irmão de local** nos
  dois sites da Warner.
- `R4977` **Senior Art Director (Contract) — Spin Master, Nova York**: direção de arte de embalagem
  e marca de brinquedo, sem 3D no corpo. Mantida fora desde o lote 2.
- `R50032377` **Senior Art Director, Creative Technology Design (Motion Designer) — Fox, Los
  Angeles**: motion design de broadcast.
- `R322701` **2D Game Artist — SciPlay, Austin**: o título já diz 2D.

### 6.3 — Caíram por ESCOPO GEOGRÁFICO (17)

Índia continua sendo onde a ILM e a Eyeline concentram a arte central, e **nenhuma foi considerada**.
**Nove da Disney/ILM Mumbai:** `10154147` Sr Character Modeler (West Mumbai) — **a mais alinhada ao
portfólio dele em toda a varredura** —, `10155895` Lead Modeler, `10145923` Creature Supervisor,
`10146393` Lead Environment Artist, `10146395` Environment Supervisor, `10152359` e `10152365`
Generalist, `10155202` e `10155332` Look Dev TD.
**Cinco da Eyeline Hyderabad:** `JR01060` Groom Artist, `JR41016` Lead Surfacing Artist, `JR01007`
Modeling Supervisor, `JR41011` Surfacing/Lookdev Artist, `JR01807` Roto/Paint Lead Artist.
**Uma da Aristocrat Noida:** `R0022012` Sr. Lead Artist.
**Duas dos locatários novos:** Senior Associate Technical Artist da Light & Wonder em **Bangalore**
e Technical Artist da SciPlay em **Kiev, Ucrânia** — a Ucrânia também está fora do escopo do
briefing.

**Índia está fora por regra e isso não se contorna.** Note, para não doer à toa, que a maioria delas
também cairia por disciplina (arte técnica, roto, rigging).

### 6.4 — Caíram pelo DEDUPE por ID de requisição (14)

Estas **passaram por escopo, por disciplina e pela régua** e morreram só no dedupe. Todas conferidas
com `sh automacao/dedupe-agora.sh <ID> "<Casa>"`, nos quatro arquivos.

| ID | Vaga | Onde apareceu |
|---|---|---|
| `10159882` | Senior Modeler, ILM Sydney | **ENVIADA em 04/09** — é a prova original do Workday |
| `10159370` | Senior Texture Artist, ILM London | enviada **e recusada** |
| `10159371` | Lead Texture Artist, ILM London | enviada **e recusada em 01/09** |
| `10142674` | Lead Generalist Artist, ILM Vancouver | **ENVIADA em 09/09**, Application Received |
| `10137201` | Pre-Vis Generalist Artist, ILM London | **ENVIADA em 09/09** |
| `JR41751` | Character Modeling Supervisor, NAS Sydney | **ENVIADA em 09/09**, prova `jobTasks/completed/application` |
| `JR41734` | Environment Modeling Supervisor, NAS Sydney | **ENVIADA em 09/09** |
| `JR41749` | Environment Surfacing Supervisor, NAS Sydney | **ENVIADA em 09/09**, três provas |
| `JR39446` | Environment Modeling Supervisor, NAS Vancouver | **ENVIADA em 09/09** |
| `JR39273` | Environment Surfacing Supervisor, NAS Vancouver | **ENVIADA em 09/09** |
| `JR40941` | Modeling Supervisor, Eyeline Seul | **ENVIADA em 09/09** |
| `JR40923` | Lead Modeler, Eyeline Seul | **ENVIADA em 09/09** |
| `JR40928` | Lead Surfacing Artist, Eyeline Seul | **ENVIADA em 09/09**, três provas |
| `JR101515` | Vehicle Artist, Cloud Imperium Manchester | **ENVIADA em 09/09** |

**Confirmação útil para a próxima rodada: a fila do lote 1 está inteiramente consumida.** As oito de
`automacao/PROXIMA-RODADA-workday.md` foram resolvidas — sete enviadas e uma (`JR41753`, Ink)
recusada com motivo escrito — e a reauditoria de hoje não achou nenhuma delas reaberta.

**Dois casos que caíram ANTES do dedupe mas que o dedupe também pegaria, e vale registrar:**
`10159762` Character Design Lead da Disney TV Animation (2D, **e enviada em 02/09**) e
`R000106508` Advanced Level Artist da WB Games Montreal (level art, já julgada). A `R000106508` é
**irmão de local**: aparece nos dois sites da Warner (`global` e `francais`) com o mesmo ID — **uma
requisição, dois anúncios**, exatamente a armadilha da regra 18.

### 6.5 — Caíram por serem RUÍDO de título (69)

Os três maiores geradores de falso positivo, medidos:

1. **"Character" em parque temático** — 5 casamentos na SeaWorld, todos atores fantasiados.
2. **"Modelling" em engenharia e finanças** — Airbus (8: *Modelling and Simulation System Engineer*,
   *FHS End-to-end Operations Modeller*), Wells Fargo (4: *Senior Quant - Credit risk modelling*),
   Morgan Stanley (3), Houlihan Lokey (1: *Financial Modelling*), Sky (1: *Senior Threat Modelling
   Analyst*). **Zero é arte.**
3. **"Generalist" em RH** — Logitech (2), Live Nation, Tobii Dynavox, Starz, Netflix LATAM, Airbus.
   Some-se "Grooming" na Procter & Gamble (2), que é **higiene masculina**.

---

## 7. A RÉGUA DE VETO — o único veto ESCRITO da rodada

Baixei o **detalhe completo** (`GET .../wday/cxs/<loc>/<site><externalPath>`) de cada finalista, com
os 17 termos e 200 caracteres de contexto de cada lado, e classifiquei **cada casamento à mão**.

| Termo | Frase inteira | Classificação |
|---|---|---|
| `authoriz` | *"Excellent analytic and communication skills. **Authorization to work in the USA.** Preferred Qualifications: M.S. degree in computer science…"* — Sony `JR-118922`, dentro de **Required Qualifications** | **VETO ESCRITO, o único da sessão.** Está na lista de requisitos obrigatórios, não no rodapé jurídico. Ele precisa de patrocínio. **Não envie.** |
| `days a week` | *"This role is based in Vancouver, British Columbia. Hybrid Role (Minimum of 3 days a week in the office)."* — Netflix `JR41288` | **Restrição de presença**, não veto de candidatura. Já catalogada pela campanha em 09/09. |
| `hybrid` | a mesma frase acima; e `#LI-Hybrid` no rodapé das da Light & Wonder | Marcação de formato, não veto. |
| `eligib` | *"SCA offers **benefits-eligible** fixed-term employees…"* e *"other benefits that an individual may be **eligible** for"* — Sony `JR-118922` | **Falso positivo clássico: é benefício**, não elegibilidade para trabalhar. Confirma a medição do lote 1. |
| `authoriz` (2ª ocorrência) | *"We are aware that **unauthorized** individuals or organizations may attempt to solicit personal information…"* — Sony `JR-118922` | **Falso positivo: é aviso antifraude.** Se a régua contasse casamento em vez de ler a frase, este sozinho já vetaria a vaga pelo motivo errado. |
| `right to work` | *"Right to Work (English/Spanish) E-Verify Participation (English/Spanish)"* — Sony `JR-118922` | Rodapé legal obrigatório nos EUA. **Não é veto por si só** — mas aqui acompanha um veto real, e é bom sinal de que a casa exige E-Verify. |

**As duas da fila: ZERO termo de imigração.** Razer `JR2026007640` não casou com nenhum dos 17.
Netflix `JR41288` casou só com presença híbrida.

**Patrocínio de visto continua sendo leitura de contexto, não critério de descarte.** Nenhuma das
duas da fila promete patrocínio e nenhuma o proíbe.

---

## 8. ARMADILHAS DE MÉTODO QUE EU MEDI NESTA SESSÃO

Cinco, todas medidas nesta rodada, não supostas.

**1. `pkill -f <padrão>` mata o próprio shell — e eu caí nela apesar de o lote 2 avisar.**
Rodei `pkill -f "python3 -u sweep.py"` e o comando morreu com código **144**: o padrão casou com a
linha de comando do meu próprio `bash -c`, que continha o texto. A forma que funciona está no lote 2
e eu deveria ter usado de primeira:
`ps -eo pid,args | grep "[s]weep.py" | awk '{print $1}' | xargs -r kill`.

**2. Armadilha nova e perigosa: um laço `until ! ps ... | grep -q "[s]weepB.py"` NUNCA TERMINA se a
linha de comando do próprio laço contiver o texto `sweepB.py`.** O colchete protege o `grep` de
casar consigo mesmo, **mas não protege o laço de casar com um IRMÃO que carrega o nome no texto**.
Eu tinha um `bash -c` cujo corpo continha `nohup python3 -u sweepB.py ...`; cinco laços de espera
ficaram girando em cima dele, um travando o outro, e **a fase C da varredura nunca começou** —
descobri porque `sweepC.log` não existia meia hora depois. **Regra: espera por processo se faz por
PID (`kill -0 $PID`) ou por arquivo-sentinela, nunca por nome dentro de linha de comando que outro
processo possa citar.**

**3. `429` do Workday NÃO significa que o locatário existe.** Três slugs devolveram `429` em vez de
`422` na varredura: `dassaultsystemesentertainment`/wd503, `da`/wd109 e `gearboxpublishing`/wd10.
Reconferidos um a um fora do pico: **os três devolvem `422`, não existem.** Se eu tivesse contado os
`429` como "existe", o placar teria três locatários fantasmas. **Todo código que não seja `422` tem
que ser reconferido sozinho antes de entrar no mapa.** O mesmo vale para o `ReadTimeout` que
`amazongamestech`/wd1 devolveu: na reconferência, `422`.

**4. O teto de vazão é do PROXY, não do número de trabalhadores.** Medi de propósito: 16 threads dão
**24 req/s**, 28 threads dão **15 req/s** e 56 threads dão **16 req/s** — ou seja, **passar de ~16
não acelera nada** e só aumenta a chance de `429`. O custo real da sondagem é
`nº de slugs × nº de pods ÷ 20 req/s`, e é isso que se planeja. As 83.175 requisições desta sessão
levaram cerca de **1h40 de relógio**.

**5. Ordenar os pods por densidade paga.** Dos 47 locatários achados, **42 moram em `wd1`, `wd3`,
`wd5`, `wd12`, `wd103`, `wd108`, `wd501` e `wd503`** — os oito pods densos. Os sete pods esparsos
(`wd10`, `wd102`, `wd105`, `wd107`, `wd109`, `wd502`, `wd504`) custaram 34.671 requisições e
entregaram **5 locatários, nenhum de arte** (`fc`/wd10, `jp`/wd102, `aa`/wd105, `tp`/wd107, `rf`/wd504). Quem tiver pressa varre os oito densos primeiro e tem
**89% do resultado com 53% do custo**.

---

## 9. COMO ISTO FOI RODADO, para quem repetir

Ferramenta: `python3` com `requests` e sessões persistentes, **16 trabalhadores**, tempo limite de
12s na sondagem e 30s no detalhe. Gravação **incremental** em CSV a cada slug terminado, com arquivo
de `done` separado, para que uma queda no meio não perca a varredura — foi por isso que a troca de
estratégia no meio do caminho não custou nada. **Nenhum navegador.** Ordem:

1. **Montagem da lista de candidatos** — 5.448 slugs únicos: variantes normalizadas de ~600 casas
   grandes de jogos, animação, VFX, brinquedo, cassino, parque e tecnologia (minúscula sem
   pontuação, primeira palavra, iniciais, forma com hífen, e sufixos `tech`/`studios`/`games`/
   `entertainment`/`interactive`/`group` — foi um sufixo desses que revelou `unitytech` no lote 2),
   mais os 886 nomes de estúdio de `automacao/garimpo-cgstudiomap.csv`, mais 255 nomes curados à mão
   para cobrir os buracos do gerador (siglas de 2 e 3 letras como `sky`, `bbc`, `wbd`, `lnw`, e
   última-palavra como `imageworks`). **Foi dessa lista curada que saíram `sky` e `lnw`.**
2. **Sondagem de locatário** — `GET robots.txt`, **83.175 requisições**, em quatro fases: 337 slugs
   × 15 pods, 4.953 × 8 pods densos, 4.953 × 7 pods esparsos e 255 × 15 pods.
   `422` descarta; qualquer outro código guarda **e é reconferido sozinho**.
3. **Extração de site** — as linhas `Allow:`/`Disallow:`/`Sitemap:` do `robots.txt` dos 37
   locatários `200` deram **93 caminhos de site, zero palpite**.
4. **Dimensionamento** — um `POST .../jobs` com `offset:0` em cada site para ler o `total`.
   71 têm vaga.
5. **Colheita** — paginação **integral**, `limit:20` e `offset` de 20 em 20 (o `limit:50` continua
   devolvendo `400`), **sem `searchText`**. **14.378 vagas** em locatários novos.
6. **Reauditoria** dos 25 quadros de arte que a campanha já lê (Disney `disneycareer` e
   `disneycareerdc`, Netflix `Netflix` e `Eyeline`, Pixar ×5, Warner `global` e `francais`,
   Cloud Imperium ×2, Aristocrat ×3, Sega, Gearbox, Unity, Spin Master ×3, LEGO, Fox, Starz):
   **3.608 vagas.** É de lá que saiu a nº 2 da fila e é lá que se confirmou que **as oito do lote 1
   foram todas consumidas em 09/09**.
7. **Filtro de título** → 135 candidatas → **leitura do corpo integral** → 3 da disciplina no escopo.
8. **Detalhe e régua** — os 17 termos com 200 caracteres de contexto, classificação manual de cada
   casamento, frase inteira transcrita.
9. **Dedupe** — `sh automacao/dedupe-agora.sh <ID> "<Casa>"` para cada finalista, com as quatro
   contagens reportadas por vaga, e conferência extra da CASA.
10. **Conferência final** — `curl` nas duas URLs públicas da fila. **As duas devolveram 200.**

Nada foi enviado, nenhum formulário foi preenchido, e `docs/index.html`, `enviados.csv` e
`automacao/FILA-DO-VINI.md` não foram tocados. Os únicos arquivos escritos por esta rodada são
**este** e uma linha em `automacao/processados.csv`.
