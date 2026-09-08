# Triagem do RESTO do Canada (tudo que nao e Vancouver, Montreal nem Toronto)

Fatia: 176 estudios da `automacao/fila-gamedevmap-canada.csv`, colhidos do gamedevmap em 08/09.
Nao encostei em Toronto e regiao. Alem dos quatro satelites nomeados no brief (Mississauga,
Markham, Oakville, Waterloo) tambem deixei **Scarborough, Vaughan e Bradford** para o agente de
Toronto, porque sao GTA e o risco de dois agentes escreverem a mesma linha nao vale 3 estudios.
Bradford segue `pendente`; Scarborough e Vaughan o outro agente ja preencheu.

**Ferramenta: so `curl` e leitura de JSON de ATS. Nenhum navegador foi aberto.**

## Vocabulario de status que usei
Copiei o que Vancouver e Montreal ja usavam e me alinhei com o agente de Toronto onde ele ja
tinha escrito:

| status | significado |
|---|---|
| `sem-pagina-de-carreira` | site abriu, nao existe pagina de carreira |
| `pagina-sem-ats` | tem pagina de carreira, mas sem ATS: ou quadro vazio, ou candidatura por email |
| `site-fora-do-ar` | dominio nao responde, expirou ou foi sequestrado |
| `porta:<host>` | ATS/quadro achado, **nenhuma** vaga da disciplina |
| `porta+disciplina:<host>` | ATS/quadro achado **com** vaga da disciplina viva; `nenhum` quando nao ha host de ATS (mesma convencao da Eidos-Montreal) |
| `porta+disciplina:veto-clearance` | vaga da disciplina existe mas o anuncio traz veto escrito |
| `bloqueado:cloudflare` | nao consegui ler sem navegador; **nao e** veredito |

## Numeros honestos

- **176** estudios na fatia. **167** com o site aberto por curl (homepage + sondagem de
  `/careers`, `/jobs`, `/join-us`, `/work-with-us`, `/emplois`, `/carrieres`, `/about/careers`,
  `/company/careers`). **9 fora do ar** (7 nao respondem, 1 dominio sequestrado, 1 expirado).
- **33** com pagina de carreira de verdade. **18** com ATS ou quadro identificado.
- **1** que nao consegui ler sem navegador (Hyper Hippo, Cloudflare) — nao entra em nenhuma das
  contas acima, e buraco declarado.
- **Vagas vivas da disciplina, com anuncio inteiro baixado e busca de veto feita: 3.**
  Uma limpa, uma com veto escrito de frances, uma com veto escrito de clearance.
- **176 de 176 sao NOVOS para a campanha.** Cruzei nome e dominio contra os 736 `PORTAIS` e os
  665 `STUDIOS` do painel: zero colisao.

### Por cidade

Contado direto do CSV depois de escrito. "Abertos" exclui os fora do ar; "pag. carreira" e a soma
de `pagina-sem-ats` com `porta*`; "ATS" e so `porta*`.

| Cidade | Estudios | Abertos | Pag. carreira | ATS/quadro |
|---|---:|---:|---:|---:|
| Edmonton | 23 | 23 | 4 | 2 |
| Halifax | 21 | 20 | 4 | 3 |
| Quebec City | 17 | 15 | 4 | 2 |
| Calgary | 15 | 13 | 2 | 1 |
| Ottawa | 12 | 10 | 0 | 0 |
| Victoria | 9 | 9 | 3 | 1 |
| London | 7 | 7 | 4 | 3 |
| Saskatoon | 7 | 7 | 0 | 0 |
| Winnipeg | 7 | 6 | 2 | 1 |
| Hamilton | 5 | 5 | 0 | 0 |
| Kitchener | 4 | 4 | 0 | 0 |
| St. Catherines | 4 | 4 | 2 | 1 |
| Regina | 3 | 3 | 0 | 0 |
| St. Johns | 3 | 3 | 0 | 0 |
| Coquitlam, Fredericton, Guelph, Longueuil, Sherbrooke, Sydney (2 cada) | 12 | 12 | 0 | 0 |
| 27 cidades de 1 estudio | 27 | 26 | 8 | 5 |
| **TOTAL** | **176** | **167** | **33** | **18** |

As cidades de 1 estudio que renderam alguma coisa: **Comox** (Blue Wizard, vaga da disciplina),
**New Westminster** (Nightmarket), **Saint-Laurent** (CAE), **Remote** (Fortis), **Mahone Bay**
(Hutch), **Banff** (GabaGoo), **Lucan** (Aerosoft), **Surrey** (Conquer Experience). **Kelowna**
(Hyper Hippo) e o bloqueado.

---

## AS VAGAS DA DISCIPLINA (as tres, com link direto e busca de veto literal)

### 1. Senior Character Artist — Small Axe Studios / 2K Sports Lab — Burnaby, BC — **SEM VETO**

Esta e a melhor coisa da rodada inteira.

- Link direto: https://job-boards.greenhouse.io/2k/jobs/7835808003
- ATS: **Greenhouse**, board `2k`. JSON integral em
  `https://boards-api.greenhouse.io/v1/boards/2k/jobs/7835808003`
- Referencia da requisicao (dedupe por AQUI, nao pelo titulo): **`R_118477`**
- Publicada 10/08/2026, atualizada 21/08/2026. Viva.
- Como cheguei: pela linha **Gearbox Studio Quebec (Take-Two Interactive)**, cujo
  `gearboxsoftware.com` empurra para a pagina de carreira da 2K, que serve este board unico para
  todos os estudios da 2K.

Por que e dele, palavra por palavra do anuncio:
> "Build high quality digital sculpts, textures and groom hair."
> "Create Industry-Leading Grooms: Procedurally groom realistic hair using industry-standard
> tools (XGen, Ornatrix), as well as author highly optimized hair cards for real-time rendering."
> "Knowledge of Maya, Unreal Engine, Substance Painter/Designer, PBR Workflow, zBrush, Marvelous
> Designer and Photoshop."
> "5+ years of experience in the games, film, or animation industry." / "Previous experience
> shipping at least 1 AAA title."

Grooming e o ponto forte dele e o anuncio pede grooming duas vezes. Ressalva honesta: e esporte,
pede personagem **realista** ("authentic and believable characters", "proven understanding of
human anatomy"), nao estilizado. Ele tem 10+ anos, entao o "5+" e o AAA passam.

**Busca literal de veto no texto INTEGRAL do anuncio** (nao na listagem — puxei o `content` do
JSON do Greenhouse, 4351 caracteres, ate o bloco do fim):

| termo | ocorrencias | veredito |
|---|---:|---|
| `authoriz` | 0 | — |
| `eligib` | 1 | **nao e veto.** E o boilerplate de remuneracao: "temporary or intern roles will not be eligible for many of these payments or benefits" |
| `sponsor` | 0 | — |
| `work permit` | 0 | — |
| `must be based` | 0 | — |
| `LMIA` | 0 | — |
| `days a week` | 0 | — |
| `French` / `français` / `bilingue` | 0 | — |
| `resident` | 0 | — |

Tambem procurei `onsite`, `on-site`, `hybrid`, `in office`, `remote`, `relocat`: **zero
ocorrencias**. O anuncio nao impoe presenca nenhuma por escrito.

**Conclusao: nenhum veto escrito. Esta vaga passa.**

Nota que o maestro precisa ver: **2K Sports Lab e a linha 14 do CSV, cidade Vancouver, e a
passagem de Vancouver a marcou `pagina-sem-ats`.** O quadro nao estava no `sportslab.2k.com`, e
sim no board corporativo da 2K. Foi um furo da rodada de Vancouver, e a vaga esta em Burnaby.

---

### 2. Lead Character Artist — Cloud Chamber (BioShock) — Montreal, QC — **VETO ESCRITO DE FRANCES**

- Link direto: https://job-boards.greenhouse.io/2k/jobs/7888173003
- ATS: Greenhouse, mesmo board `2k`. Referencia: **`R_118561`**. Publicada 19/08/2026, viva.
- Perfil: "craft compelling **stylized** character assets", BioShock, lidera time de artistas.
  No papel e a vaga perfeita para ele — estilizado e personagem.

**Busca literal de veto no texto integral (9683 caracteres):** um unico acerto, e ele mata.

> `French` :: **"For candidates located in Quebec: This position requires professional proficiency
> in both French and English. Proficiency in English is required to collaborate with our U.S.
> teams and international partners, as well as to handle specialized technical documentation
> (reading, writing, and communication)."**

Os outros dez termos (`authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`,
`days a week`, `français`, `bilingue`, `resident`) deram zero.

O brief diz que exigencia de frances fluente ja derrubou duas candidaturas desta campanha e e
veto real. A clausula esta condicionada a "candidates located in Quebec", e a vaga e em Montreal,
entao ele estaria localizado no Quebec. **Marco como veto.** Se o maestro quiser contestar, o
argumento existe e esta acima na literal; nao decido isso sozinho.

Esta linha **nao e da minha fatia** (Montreal). O board tambem nao esta na minha linha: o agente
de Toronto ja marcou `2K Play` como `porta+disciplina:duplicata-greenhouse-2k`. Registro aqui
para o board `2k` nao ser aberto uma terceira vez.

---

### 3. 3D Character Artist — Blue Wizard Digital — Comox, BC — **SEM VETO no bloco da vaga**

- Link direto: https://bluewizard.com/jobs (a vaga esta nessa mesma pagina, nao tem URL propria)
- ATS: **nenhum.** Candidatura por email para `jobs@bluewizard.com`. Status no CSV:
  `porta+disciplina:nenhum`, mesma convencao da Eidos-Montreal.
- Estudio do Jason Kapalka (co-fundador da PopCap). Ilha de Vancouver.

Por que e dele, do anuncio:
> "seeking to contract a creative and talented 3D Artist to work on an upcoming mobile game
> project being built in the Unity engine. We are looking for artists who are confident creating
> **cartoon/stylized** visuals"
> "Take established character design concepts and translate them into attractive, low-poly 3D
> models." / "Model and texture 3D assets to be used within Unity"
> "3+ years 3D modeling and texturing skills in Maya or Blender."
> "Job Type Full Time; Term employment; **Remote or in-studio**."

Estilizado + personagem + texturizacao. Contrato a termo com possibilidade de extensao, e aceita
remoto. Prioridade alta pelo encaixe, media pela forma de contratacao.

**Busca literal de veto na pagina inteira** (43863 caracteres de texto, todas as vagas da pagina):

| termo | ocorrencias | veredito |
|---|---:|---|
| `authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`, `French`, `français`, `bilingue`, `resident` | 0 | — |
| `days a week` | 1 | **nao e da vaga dele.** O trecho e "Our preference for a schedule would 4-6 hours per day for 4 days a week to start" e esta em OUTRA vaga da mesma pagina (a de apoio administrativo). O bloco do 3D Character Artist diz "Remote or in-studio" |

**Conclusao: nenhum veto escrito na vaga da disciplina.**

---

## OS DESCARTES DA DISCIPLINA, com motivo literal entre aspas

### Modest Tree — Halifax — 3D Modeller — **VETADA**
- https://www.modesttree.com/about/careers (vaga num acordeao da propria pagina, sem ATS)
- Encaixe real: "Experience optimizing 3D models for real-time applications, including geometry
  reduction, efficient UV layouts, texture optimization, normal map workflows, and LOD creation",
  "Strong UV unwrapping skills", "Experience creating PBR and tiling textures", "Experience with
  Substance Painter". E modelagem e texturizacao, so que hard-surface industrial/CAD, nao
  personagem.
- **Veto escrito, acerto do termo `eligib`, no bloco do fim da vaga:**
  > "Security Clearance — Due to the nature of our work with defence and government clients:
  > **Candidates must be eligible to obtain Canadian Security Clearance (Reliability Status or
  > Secret) Canadian citizenship or permanent residency may be required**"
- Status: `porta+disciplina:veto-clearance`.

### Digital Extremes — London, ON — quadro vivo, **nenhuma vaga da disciplina**
- Greenhouse board `digitalextremes`, 5 vagas, todas em London, Ontario. As duas de arte sao
  **"Concept Artist"** e **"Senior VFX Artist"** — o brief diz explicitamente que concept 2D e
  VFX em tempo real **nao sao dele**. As outras tres sao marketing, recrutamento e engenharia web.
- `porta:boards.greenhouse.io`. Vale reabrir daqui a algumas semanas: e o maior estudio da fatia
  e o board mexe.

### Complex Games — Winnipeg — o Character Artist existe mas **nao e no Canada**
- A Complex Games virou parte da Frontier Developments; a pagina de carreira dela empurra para
  https://www.frontier.co.uk/careers/jobs
- O board tem **"Experienced Character Artist"**, mas as 14 vagas do board, sem excecao, dizem
  **"Location: Cambridge / Hybrid"** — Reino Unido. Nao ha uma unica vaga de Winnipeg, e
  `frontier.co.uk/careers/complex-games` devolve **"Error 404 Department Not Found"**.
- `porta:frontier.co.uk`. Descarte para a fila do Canada. Se o maestro quiser o Reino Unido, o
  anuncio esta la e nao fiz a busca de veto nele porque esta fora do escopo desta rodada.

### Hatchery Games — Quebec City — falso positivo de "Character Artist"
- https://hatcherygames.com/#jobs. O grep acertou "Character Artist" porque e a legenda de uma
  **foto do time** ("Olenka Denis — Character Artist"). A unica vaga aberta e **"UI Director"**.
- `pagina-sem-ats`.

### Beenox (Activision) — Quebec City — quadro grande, **nada da disciplina**
- Board real: https://careers.beenox.com/us/en/search-results (Phenom People, nao aparece no HTML
  do `beenox.com`; o link vivo e `careers.beenox.com/us/en/art-animation`).
- 9 vagas, todas Quebec City / Montreal. A unica de arte e **"Artiste d'eclairage expert.e senior
  — Senior Expert Lighting Artist"**: iluminacao, que o brief exclui. O resto e programacao,
  producao e seis estagios.
- Sinal de frances para o maestro: **todos os titulos sao bilingues FR/EN**, o que em Quebec City
  quase sempre vem com a clausula da Lei 96. Nao abri anuncio individual porque nao havia nenhum
  da disciplina para abrir.
- `porta:careers.beenox.com`.

### Os outros quadros vivos, todos sem nada da disciplina
Baixei a lista de vagas de cada um e conferi titulo a titulo:

| Estudio | Cidade | ATS | Vagas | Por que descartei |
|---|---|---|---|---|
| Kano Apps | Victoria | Greenhouse EU `kano` | 2 | "Game Product Analyst, Analytics & AI" e "Growth Marketer" |
| Improbable Games Canada | Edmonton | Ashby `improbable` | 7 | marketing, financeiro, engenharia, design de produto. Nenhuma de arte, e todas "Remote - International" ou Londres |
| Gamemode One | Halifax | BambooHR `gamemodeone` | 3 | "General Application", "Community Manager", "Marketing Manager (Minecraft)" |
| Bluedrop Training and Simulation | Halifax | CareerBeacon | 7 | coordenacao de projeto, engenharia de software, suporte, RH, design instrucional, integracao, compras |
| Big Blue Bubble | London, ON | applytojobs.ca (Humi) | 1 | **"User Interface (UI) Artist"** — UI, nao personagem |
| Fortis Games | Remote | Greenhouse `fortisgames` | 1 | "ASO Specialist (Contractor)", e so Europa |
| CAE INC. | Saint-Laurent | Workday `cae.wd3` | 0 da disciplina | busquei `3D`, `modeler`, `character`, `texture` na API. `modeler` e `texture` deram 0; `3D` deu 4 e nenhuma e de arte 3D ("Senior Visual Database Lead", "Graphic Artist/Multimedia Specialist" x2 nos EUA, "Software Engineer") |
| BioWare Edmonton | Edmonton | quadro proprio da EA em bioware.com | 1 | "Production Director (212271)". Nenhuma vaga de arte, nenhuma de Edmonton |
| Big Viking Games | London, ON | Workable `big-viking-games-3` | 0 | quadro vazio |
| New World Interactive | Calgary | applytojobs.ca | 0 | literal: **"There are currently no job openings, please check back later."** |
| Epic Story Interactive (virou Nightmarket Games) | New Westminster | Indeed | nao lido | o "VISIT JOB BOARD" leva a `ca.indeed.com/cmp/Epic-Story-Interactive-Inc.` |
| Apocalypse Studios | St. Catherines | Indeed | nao lido | "Find positions and apply via Indeed" |

**Sobre os dois do Indeed: nao consegui ler.** O Indeed devolve "Security Check — Additional
Verification Required — Please enable JavaScript to complete the security check." Sem navegador
nao passo. Deixei `porta:ca.indeed.com` nas duas linhas e **nao afirmo que tem ou nao tem vaga.**

---

## O que travou, dito na cara

1. **Hyper Hippo Entertainment (Kelowna)** — o unico estudio de porte da fatia que eu nao
   consegui abrir de jeito nenhum. `hyperhippo.com` devolve **HTTP 202 com corpo vazio** em
   qualquer User-Agent, com e sem `www`, na raiz e em `/careers/`; e Cloudflare. O
   `hyperhippo.bamboohr.com` redireciona para o site de marketing da BambooHR, o que sugere conta
   encerrada, mas isso e inferencia, nao leitura. Status `bloqueado:cloudflare`. **Fica para
   quem tiver o navegador** — e o estudio mais provavel de ter quadro entre os que nao li.
2. **Indeed (Nightmarket e Apocalypse Studios)** — parede de verificacao, ver acima.
3. **Nunca escrevo "sem captcha".** A pagina de carreira da Beenox carrega o plugin
   `gravityformsrecaptcha` no HTML, o que e indicio de reCAPTCHA, mas nao cliquei em nada: **nao
   ha veredito de captcha em nenhuma linha desta rodada.**
4. **`jobs@bluewizard.com` nao foi contatado.** Nenhum email, nenhum rascunho, nenhum formulario
   preenchido nesta rodada.
5. Dois grepes meus deram falso positivo e eu corrigi na mao, registro para nao repetir: (a) o
   padrao de link de carreira com a palavra `team` casa com `steampowered.com`, o que inflou 30
   linhas de "tem pagina de carreira" que na verdade eram links de loja da Steam; (b) sites
   Wix/Squarespace devolvem **200 para qualquer caminho**, entao `/about/careers` "existir" nao
   prova nada — Grizzly Moose, Caldera, gskinner e Baby Ghosts cairam nisso e viraram
   `sem-pagina-de-carreira` depois de eu ler o conteudo.

## Dominios mortos ou sequestrados (7)
`evilobjective.com`, `giantsandbox.com`, `bittentoast.com`, `magmic.com`, `dolphinbarn.com`,
`corbiegames.com` nao respondem. **`infiniteammo.ca` foi sequestrado**: o dominio hoje serve
pagina de afiliado de cassino ("Top Casinos") em cima do nome do Alec Holowka. Nao usar.
`nesting-games.com` devolve "Squarespace — Website Expired".

## O que eu recomendo abrir primeiro amanha
1. **https://job-boards.greenhouse.io/2k/jobs/7835808003** — `R_118477`, Senior Character Artist,
   Burnaby. Greenhouse, veto conferido no texto integral, zero acerto real. A campanha ja sabe
   preencher Greenhouse.
2. **https://bluewizard.com/jobs** — 3D Character Artist estilizado, remoto aceito, mas e email:
   entra na fila do Vini, nao na do automatico.
3. **hyperhippo.com** com navegador, so para fechar o unico buraco de porte da fatia.
