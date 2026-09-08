# TEAMTAILOR REFEITO PELAS DUAS ROTAS — 08/09

Missão: refazer todo quadro Teamtailor identificado pela campanha, medindo `jobs.json` **contra**
`sitemap.xml`, para provar ou desmentir o defeito registrado hoje ("o `jobs.json` mente, devolve lista
vazia com vaga viva; na Paradox `jobs.json` = 0 e `sitemap` = 18").

**Só `curl`. Nenhum navegador aberto. Nenhum email, rascunho, formulário ou envio. Nenhum arquivo
compartilhado editado. Sem commit e sem push.**

---

## 0. O VEREDITO, ANTES DA TABELA

**O defeito NÃO se confirma. Ele se inverte.**

Medi **102 hostnames Teamtailor** (91 quadros distintos — 11 aparecem em dois hostnames). Em
**100 dos 102**, `jobs.json` e `sitemap.xml` devolveram **exatamente o mesmo conjunto de requisições**,
conferido **por ID de requisição**, não por contagem.

Nos **2 casos divergentes**, quem mentiu foi o **`sitemap.xml`**:

| Quadro | `jobs.json` | `sitemap.xml` | Quem escondeu |
|---|---|---|---|
| `stillfrontgroup.teamtailor.com` | **39** | 4 | o **sitemap** escondeu 35 |
| `careers.kepler-interactive.com` | **7** | 1 | o **sitemap** escondeu 6 |

Somando as duas rotas nos 102 hostnames: **`jobs.json` = 402 vagas · `sitemap.xml` = 361 vagas.**
O `jobs.json` viu **41 vagas a mais**. Em nenhum quadro o `sitemap` viu uma vaga que o `jobs.json`
não visse — o conjunto `sitemap − jobs.json` ficou **vazio nos 102**.

E o caso do Kepler **custa uma vaga da disciplina**: a **Lead 3D Character Artist** (`8311973`) está no
`jobs.json` e **não está** no `sitemap.xml`. Quem tivesse trocado o `jobs.json` pelo `sitemap` como
"rota certa" teria perdido exatamente o tipo de vaga que esta campanha procura.

### De onde veio o "0" da Paradox

O zero era **slug errado lido como quadro vazio**, não quadro vazio. Medido agora, um por um:

| URL sondada | HTTP | itens |
|---|---|---|
| `career.paradoxplaza.com/jobs.json` | **200** | **18** |
| `paradoxinteractive.teamtailor.com/jobs.json` | 404 | — |
| `paradoxplaza.teamtailor.com/jobs.json` | 404 | — |
| `paradox.teamtailor.com/jobs.json` | 404 | — |

O quadro real da Paradox **sempre respondeu 18** pelo `jobs.json` — o mesmo 18 do sitemap. Chamei
`career.paradoxplaza.com/jobs.json` **12 vezes seguidas**: 200 e 18 itens nas doze. Chamei **sem
`User-Agent`**: 200 e 18 itens. Não há limitação de taxa, não há bloqueio por UA, não há lista vazia.
O que existe é um 404 de slug inexistente cujo corpo, contado como JSON, vira zero.

Mesma coisa nos outros dois casos que a triagem tinha registrado como defeito:

- **SYBO** — `sybogames.teamtailor.com` = 404; `sybo.teamtailor.com` = **200, 5 vagas** pelas duas rotas.
- **Goodbye Kansas** — `goodbyekansasstudios.teamtailor.com` = 404;
  `goodbyekansas.teamtailor.com` e `career.goodbyekansas.com` = **200, 3 vagas** pelas duas rotas.

É a **mesma armadilha que o brief já documentou para o 403** (`playgroundgames` dá 403,
`playground-games` dá 200), só que aqui ela veste 404 e se disfarça de "quadro vazio".

**Consequência prática para a campanha:** os vereditos de "sem vaga" dados hoje **não precisam ser
refeitos por causa do `jobs.json`** — as duas rotas concordam. Mas **precisam ser refeitos onde o slug
foi adivinhado**, e essa é uma lista diferente e menor. E a recomendação de "trocar o `jobs.json` pelo
`sitemap.xml`" deve ser **revertida**: em quadro de grupo o sitemap é que trunca.

### A regra correta, medida

1. **Leia as DUAS e una os conjuntos por ID de requisição.** Custa duas chamadas por quadro.
2. **Se for ler uma só, leia o `jobs.json`** — ele foi superconjunto do sitemap em 102 de 102.
3. **Nunca conte um corpo não-JSON como zero.** Confira o HTTP e confira que o corpo tem
   `jsonfeed.org/version` antes de escrever "quadro vazio".

---

## 1. A TABELA DA DIVERGÊNCIA

102 hostnames, as duas rotas, contagem por ID de requisição. 77 com vaga, 25 vazios nas duas.

| Quadro (careersite) | Estúdio | `jobs.json` | `sitemap.xml` | Divergência |
|---|---|---|---|---|
| `stillfrontgroup.teamtailor.com` | Stillfront | 39 | 4 | **+35 a mais no jobs.json** |
| `untoldstdfg1324556.teamtailor.com` | Untold Studios | 23 | 23 | nenhuma |
| `beffio.teamtailor.com` | Beffio | 21 | 21 | nenhuma |
| `career.paradoxplaza.com` | Paradox Interactive | 18 | 18 | nenhuma |
| `careers.embark-studios.com` | Embark Studios | 18 | 18 | nenhuma |
| `embarkstudios.teamtailor.com` | Embark Studios | 18 | 18 | nenhuma |
| `careers.madbox.io` | Madbox | 15 | 15 | nenhuma |
| `careers.yodo1.com` | Yodo1 | 14 | 14 | nenhuma |
| `ankama.teamtailor.com` | Ankama | 13 | 13 | nenhuma |
| `twinharbour.teamtailor.com` | Twin Harbour Interactive | 11 | 11 | nenhuma |
| `gameboost.teamtailor.com` | Game Boost | 9 | 9 | nenhuma |
| `pfx.teamtailor.com` | PFX | 9 | 9 | nenhuma |
| `careers.triband.net` | Triband | 8 | 8 | nenhuma |
| `sandboxinteractive.teamtailor.com` | Sandbox Interactive | 8 | 8 | nenhuma |
| `careers.castirongames.com` | Cast Iron Games | 7 | 7 | nenhuma |
| `careers.kepler-interactive.com` | Kepler Interactive | 7 | 1 | **+6 a mais no jobs.json** |
| `careers.theyard-vfx.com` | The Yard VFX | 7 | 7 | nenhuma |
| `blackkitestudios.teamtailor.com` | Black Kite Studios | 6 | 6 | nenhuma |
| `bulkheadinteractive.teamtailor.com` | BULKHEAD | 6 | 6 | nenhuma |
| `careers.bulkhead.com` | BULKHEAD | 6 | 6 | nenhuma |
| `careers.ironbirdcreations.com` | Ironbird Creations | 6 | 6 | nenhuma |
| `houseofhow.teamtailor.com` | House of How Games | 6 | 6 | nenhuma |
| `jobs.funcom.com` | Funcom | 6 | 6 | nenhuma |
| `careers.1920vfx.com` | nineteentwenty | 5 | 5 | nenhuma |
| `fatshark.teamtailor.com` | Fatshark | 5 | 5 | nenhuma |
| `jobs.arrowheadgamestudios.com` | Arrowhead Game Studios | 5 | 5 | nenhuma |
| `sybo.teamtailor.com` | SYBO | 5 | 5 | nenhuma |
| `career.geoguessr.com` | GeoGuessr | 4 | 4 | nenhuma |
| `career.sharkmob.com` | Sharkmob | 4 | 4 | nenhuma |
| `careers.foolstheory.com` | Fool's Theory | 4 | 4 | nenhuma |
| `cigames.teamtailor.com` | CI Games | 4 | 4 | nenhuma |
| `jobs.stunlockstudios.com` | Stunlock Studios | 4 | 4 | nenhuma |
| `stunlocksstudios.teamtailor.com` | Stunlock Studios | 4 | 4 | nenhuma |
| `wetaworkshop.teamtailor.com` | Wētā Workshop | 4 | 4 | nenhuma |
| `career.goodbyekansas.com` | Goodbye Kansas | 3 | 3 | nenhuma |
| `careers.adventurepartygames.com` | Adventure Party Games | 3 | 3 | nenhuma |
| `careers.envarstudio.com` | Envar Studio | 3 | 3 | nenhuma |
| `careers.tap-nation.io` | TapNation | 3 | 3 | nenhuma |
| `envarstudio.teamtailor.com` | Envar Studio | 3 | 3 | nenhuma |
| `goodbyekansas.teamtailor.com` | Goodbye Kansas | 3 | 3 | nenhuma |
| `axolotgamesab.teamtailor.com` | Axolot Games | 2 | 2 | nenhuma |
| `career.snowprintstudios.com` | Snowprint Studios | 2 | 2 | nenhuma |
| `careers.aonic.co` | Aonic | 2 | 2 | nenhuma |
| `careers.pneumagroup.co.uk` | Pneuma Group | 2 | 2 | nenhuma |
| `careers.rawpowergames.com` | Raw Power Games | 2 | 2 | nenhuma |
| `careers.sloclap.com` | Sloclap | 2 | 2 | nenhuma |
| `clickoutmedia.teamtailor.com` | ClickOut Media | 2 | 2 | nenhuma |
| `coffeestainstudios.teamtailor.com` | Coffee Stain | 2 | 2 | nenhuma |
| `fundaygames.teamtailor.com` | Funday Games | 2 | 2 | nenhuma |
| `hampastudio.teamtailor.com` | Hampa Studio | 2 | 2 | nenhuma |
| `ilpvfx.teamtailor.com` | Important Looking Pirates | 2 | 2 | nenhuma |
| `jobs.coffeestain.com` | Coffee Stain | 2 | 2 | nenhuma |
| `jobs.riftgaming.gg` | Rift Gaming | 2 | 2 | nenhuma |
| `jobs.vinefx.com` | Vine FX | 2 | 2 | nenhuma |
| `playagames.teamtailor.com` | Playa Games | 2 | 2 | nenhuma |
| `sloclap.teamtailor.com` | Sloclap | 2 | 2 | nenhuma |
| `tacticaladventures.teamtailor.com` | Tactical Adventures | 2 | 2 | nenhuma |
| `vinefx.teamtailor.com` | Vine FX | 2 | 2 | nenhuma |
| `apply.ioi.dk` | IO Interactive | 1 | 1 | nenhuma |
| `career.capsule.studio` | Capsule Studio | 1 | 1 | nenhuma |
| `careers.captureage.com` | CaptureAge | 1 | 1 | nenhuma |
| `careers.lastarrowgames.com` | Last Arrow Games | 1 | 1 | nenhuma |
| `careers.lightheart.games` | Lightheart Entertainment | 1 | 1 | nenhuma |
| `careers.northkingdom.com` | North Kingdom | 1 | 1 | nenhuma |
| `careers.realtimeuk.com` | REALTIME | 1 | 1 | nenhuma |
| `careers.steelcityinteractive.co.uk` | Steel City Interactive | 1 | 1 | nenhuma |
| `gigglebug.teamtailor.com` | Gigglebug | 1 | 1 | nenhuma |
| `ioi.teamtailor.com` | IO Interactive | 1 | 1 | nenhuma |
| `jobs.creepyjar.com` | Creepy Jar | 1 | 1 | nenhuma |
| `jobs.lingokids.com` | Lingokids | 1 | 1 | nenhuma |
| `jobs.neongiant.se` | Neon Giant | 1 | 1 | nenhuma |
| `jobs.rawfury.com` | Raw Fury | 1 | 1 | nenhuma |
| `jobs.starbreeze.com` | Starbreeze | 1 | 1 | nenhuma |
| `jobs.vividgames.com` | Vivid Games | 1 | 1 | nenhuma |
| `realtime.teamtailor.com` | REALTIME | 1 | 1 | nenhuma |
| `starbreeze.teamtailor.com` | Starbreeze | 1 | 1 | nenhuma |
| `starstable.teamtailor.com` | Star Stable Entertainment | 1 | 1 | nenhuma |

**Vazios nas DUAS rotas (25) — confirmados vazios, não "não medidos":**
`career.maginteractive.com`, `career.mindark.com`, `career.opusmajor.io`, `careers.10chambers.com`,
`careers.adhocla.com`, `careers.coatsink.com`, `careers.fingersoft.com`, `careers.hazelight.se`,
`careers.kindabrave.com`, `careers.lucky-kat.com`, `careers.otherside-e.com`,
`careers.playerunknownproductions.net`, `careers.radicalforge.com`, `careers.redroverinteractive.com`,
`careers.rokoko.com`, `careers.thegang.io`, `jobs.alphachannelgames.com`, `jobs.beyondframes.com`,
`jobs.chiefrebel.com`, `jobs.framebreak.se`, `jobs.ghostship.dk`, `jobs.invisiblewalls.co`,
`jobs.keengames.com`, `jobs.ohbibi.com`, `jobs.resolutiongames.com`.

Nesses 25 o `jobs.json` devolveu HTTP 200 com `"items":[]` **e** o `sitemap.xml` devolveu 200 com as
páginas institucionais (`/jobs`, `/people`, `/departments`, `/privacy-policy`) e **nenhum `/jobs/<id>`**.
As duas rotas dizem a mesma coisa. Os vereditos de "sem vaga" desses quadros **estão certos**.

---

## 2. AS VAGAS DA DISCIPLINA

Varri as **402 vagas** dos 102 hostnames, pelas duas rotas, por título e por slug de URL, atrás de
Character Artist, 3D Modeller, Modeling Artist, Texture, Material, Look Development/Lookdev,
Surfacing, Groom, Sculptor, Visual Development e Character Modeler.

**Resultado bruto: 18 acertos de palavra-chave. Depois de ler cargo a cargo, 7 são da disciplina.
E as 7 já estão no painel.**

### 2.1 Snowprint Studios — Senior 3D Character Artist — **VETO ESCRITO**

- Link direto: <https://career.snowprintstudios.com/jobs/8341580-senior-3d-character-artist>
- Formulário: <https://career.snowprintstudios.com/jobs/8341580-senior-3d-character-artist/applications/new> — HTTP **200**
- Requisição `8341580`, publicada 08/09/2026. Quadro Teamtailor em domínio próprio.
- Formato: **híbrido**, escritório em Södermalm, Estocolmo, presencial terça e sexta.
  Tipo de contrato **não publicado**. **Faixa salarial não publicada.**
- **No painel:** SIM — `PORTAIS`, como *"Snowprint Studios (Senior 3D Character Artist, Estocolmo) —
  VETO ESCRITO, NAO APLICAR"*.
- **Busca de veto, os treze termos, resultado literal do anúncio inteiro baixado:**

  | termo | resultado |
  |---|---|
  | `authoriz` | NENHUM |
  | `eligib` | NENHUM |
  | `sponsor` | NENHUM |
  | `work permit` | NENHUM |
  | `must be based` | NENHUM |
  | `LMIA` | NENHUM |
  | `days a week` | NENHUM |
  | idioma local (`French`/`Polish`/`Swedish`/`German`/`Danish`/`Finnish`) | NENHUM |
  | `resident` | NENHUM |
  | **`relocat`** | **ACHADO** — *"You are currently located in Stockholm, Sweden. We are unable to support relocation for this position."* |
  | **`located in`** | **ACHADO** — mesma frase, e ainda *"Our Stockholm studio is located in Södermalm, with a hybrid working model."* |
  | **`unable to support`** | **ACHADO** — mesma frase |
  | `no relocation` | NENHUM |

  **A régua corrigida se prova aqui:** os **nove termos antigos deram NENHUM** e os **três dos quatro
  novos pegaram o veto**. Sem a correção de hoje, esta vaga passaria como limpa.

### 2.2 Kepler Interactive / Tactical Adventures — Lead 3D Character Artist — **limpa, já enviada**

- Requisição `8311973`, publicada 02/09/2026. **A mesma requisição em dois quadros**: aparece em
  `careers.kepler-interactive.com` (grupo) e em `tacticaladventures.teamtailor.com` (estúdio).
- Link direto (estúdio): <https://tacticaladventures.teamtailor.com/jobs/8311973-lead-3d-character-artist>
- Link direto (grupo): <https://careers.kepler-interactive.com/jobs/8311973-lead-3d-character-artist>
- Formulário: <https://tacticaladventures.teamtailor.com/jobs/8311973-lead-3d-character-artist/applications/new> — HTTP **200**.
  O caminho equivalente sob `careers.kepler-interactive.com` devolve **404** — o formulário mora no
  quadro do estúdio, não no do grupo.
- Formato: Paris. Tipo de contrato **não publicado**. **Faixa salarial não publicada.**
- **No painel:** SIM — *"Tactical Adventures (Lead 3D Character Artist) — CANDIDATURA ENVIADA e
  CONFIRMADA em 06/09"*, com realocação dita explicitamente e a pergunta de autorização de trabalho
  respondida com a verdade.
- **Busca de veto, os treze termos, anúncio inteiro:** `authoriz` NENHUM · `eligib` NENHUM ·
  `sponsor` NENHUM · `work permit` NENHUM · `must be based` NENHUM · `LMIA` NENHUM ·
  `days a week` NENHUM · idioma local NENHUM · `resident` NENHUM · `relocat` NENHUM ·
  `located in` NENHUM · `unable to support` NENHUM · `no relocation` NENHUM.
  **Nenhum dos treze. Anúncio limpo.**
- **É a vaga que o `sitemap.xml` escondia** no quadro do grupo Kepler.

### 2.3 Fatshark — Character Artist — **limpa, com SINAL POSITIVO, já enviada**

- Link direto: <https://fatshark.teamtailor.com/jobs/8190501-character-artist>
- Formulário: <https://fatshark.teamtailor.com/jobs/8190501-character-artist/applications/new> — HTTP **200**
- Requisição `8190501`, publicada 07/08/2026. Estocolmo (Södermalm).
- Formato: **presencial 4 dias por semana**, 1 dia opcional de casa; *onboarding* inteiro no escritório.
  Tipo de contrato **não publicado**. **Faixa salarial não publicada.**
- **No painel:** SIM — *"CANDIDATURA ENVIADA e CONFIRMADA em 06/09"*.
- **SINAL POSITIVO, literal:** *"Relocation package for international talent"*. Também
  *"paid overtime · Occupational pension · Health benefits and health check ups · Bonus program"*.
- **Busca de veto, os treze termos:** `authoriz` NENHUM · `eligib` NENHUM · `sponsor` NENHUM ·
  `work permit` NENHUM · `must be based` NENHUM · `LMIA` NENHUM · `days a week` NENHUM ·
  `resident` NENHUM · `unable to support` NENHUM · `no relocation` NENHUM.
  - `Swedish` **ACHADO**, mas **não é veto**: *"We are a Swedish game development studio located in
    Södermalm, Stockholm"* — descrição do estúdio, não exigência de idioma.
  - `relocat` **ACHADO**, e é **o contrário de veto**: *"Relocation package for international talent"*.
  - `located in` **ACHADO**, e é sobre o escritório: *"Dog-friendly office located in central Stockholm"*.
  - **Veredito: nenhum veto escrito. Sinal positivo de relocação.**

### 2.4 Beffio — três requisições — **já enviadas**

Quadro em `beffio.teamtailor.com`, com URLs canônicas em `careers.beffio.com`. As duas rotas
concordaram: 21 e 21.

| Requisição | Cargo | Data | Link | No painel |
|---|---|---|---|---|
| `7242656` | Senior Character Artist Unity3D, Europe, Remote/Permanent | 17/02/2026 | <https://careers.beffio.com/jobs/7242656-senior-character-artist-unity3d-europe-remote-permanent> | SIM, candidatura enviada |
| `6217989` | Lead 3D Character Artist (Remote/Permanent) | 23/07/2025 | <https://careers.beffio.com/jobs/6217989-lead-3d-character-artist-remote-permanent> | SIM, candidatura enviada |
| `6984394` | Senior Character **Concept** Artist | 27/12/2025 | <https://careers.beffio.com/jobs/6984394-senior-character-concept-artist-remote-permanent-european-union> | SIM, candidatura enviada |

O painel registra as três num único cartão: *"beffio (3 candidaturas: Lead 3D Character Artist,
Senior Character Artist Unity3D, Senior Character Concept Artist)"*, com a observação de que os
emails *"Complete the application"* pareciam candidatura pendente e **não eram**.
A `6984394` é **concept 2D de personagem**, que o brief marca como **não é dele** — fica registrada só
porque já foi enviada.

### 2.5 Cast Iron Games — Lead 3D Artist — **já descartada por veto**

- <https://careers.castirongames.com/jobs/7154430-lead-3d-artist> · requisição `7154430`, 02/02/2026,
  Wakefield, presencial.
- **No painel: DUAS vezes** — uma como *"VAGA CONFERIDA NA FONTE OFICIAL em 05/09 e NÃO ENVIADA"* e
  outra como *"DESCARTADA POR VETO DE RESIDÊNCIA"*. Não reabrir.

### 2.6 Ironbird Creations — 3D Artist — **já enviada**

- <https://careers.ironbirdcreations.com/jobs/2228715-3d-artist> · requisição `2228715`, **17/11/2022**.
  Anúncio de quase quatro anos, ainda listado pelas duas rotas.
- **No painel:** *"CANDIDATURA ENVIADA E CONFIRMADA PELO JHON em 07/09"*.

### 2.7 Prioridade MÉDIA (ambiente) — registrado, não é o alvo

- **Sandbox Interactive / Stillfront** — Lead 3D Environment Artist (m/f/d), Berlim,
  <https://stillfrontgroup.teamtailor.com/jobs/8094866-lead-3d-environment-artist-m-f-d>. **Já no painel.**
  Só o `jobs.json` a lista; o sitemap da Stillfront não.
- **Embark Studios** — Environment Artist, <https://careers.embark-studios.com/jobs/7964466-environment-artist>. Já conhecida.
- **Envar Studio** — Senior 3D Environment Artist, `careers.envarstudio.com`. Já conhecida.
- **Beffio `6653367`** — Lead 3D Artist / Environment / World Building. Ambiente.

### 2.8 Acertos de palavra-chave que NÃO são da disciplina (fica registrado para o filtro não repetir)

- `wetaworkshop.teamtailor.com` — *Technician - Props* (`8252505`) e *Senior Technician - Molding,
  Props & Hair* (`8231885`): fabricação **física** de adereços, não modelagem digital.
- `stillfrontgroup.teamtailor.com` — *HR / People & Culture **Generalist*** (`7854278`).
- `gameboost.teamtailor.com` — *Graphics Programmer* (`6866951`) e
  `jobs.riftgaming.gg` — *Sr **Generalist** Programmer* (`5942846`): programação.
- `jobs.vinefx.com` — *3D Generalist* (`1637991`, 2022) e *CG Generalist & Compositors* (`7219993`):
  generalista com composição, e o segundo diz *"Manchester Based"* no próprio título.
- `beffio.teamtailor.com` — *Senior Technical Animator (Rigging...)* (`7148147`): rigging e animação.

---

## 3. FALHA NOVA DA RÉGUA DE TREZE TERMOS

A régua corrigida hoje pegou a Snowprint, mas **ela ainda tem um buraco medido, e é no termo
`days a week`**.

O anúncio da **Fatshark** diz, literalmente:

> *"We have a policy of working **4 days in the office per week**, with 1 day optional to work from home."*

O termo `days a week` **não casa** com "days in the office per week". A frase determina presença
física quatro dias por semana e **passaria em branco**. Na Fatshark isso não descarta (o anúncio
oferece relocação), mas em outro estúdio a mesma construção esconderia uma exigência real.

**Sugestão de correção, para quem mantém a régua:** trocar o termo `days a week` por um que case com
as duas construções — `days a week`, `days per week` e `days in the office`. Não apliquei a mudança em
nenhum arquivo compartilhado; fica como recomendação.

---

## 4. QUADROS EM DOMÍNIO PRÓPRIO — A SEGUNDA SONDAGEM

Rodei `career.<domínio>/jobs.json`, `careers.<domínio>/jobs.json` e `jobs.<domínio>/jobs.json` sobre
**4.960 domínios** extraídos de `fila-gamedevmap-europa.csv`, `fila-gamedevmap-canada.csv` e
`garimpo-cgstudiomap.csv`. Confirmei Teamtailor exigindo `jsonfeed.org/version` no corpo.

**62 quadros Teamtailor em domínio próprio respondendo**, somando **170 vagas**.

**13 deles não constavam de nenhuma lista de quadros já registrada pela campanha:**

| Quadro achado | Estúdio | vagas | tem vaga da disciplina? |
|---|---|---|---|
| `careers.kepler-interactive.com` | Kepler Interactive | 7 | **SIM** — Lead 3D Character Artist `8311973` (já enviada; **invisível no sitemap deste quadro**) |
| `careers.foolstheory.com` | Fool's Theory | 4 | não (Technical Artist, Quest Designer, Business Systems Engineer, Open Applications) |
| `careers.tap-nation.io` | TapNation | 3 | não (Product Analyst, Product Manager, CFO) |
| `careers.sloclap.com` | Sloclap | 2 | não (Responsable IT, Associate Producer) |
| `careers.rawpowergames.com` | Raw Power Games | 2 | não (QA Director, Unsolicited Application) |
| `careers.pneumagroup.co.uk` | Pneuma Group | 2 | não (Bar Staff, Bar Support Staff) |
| `careers.northkingdom.com` | North Kingdom | 1 | não (Freelancers of Europe) |
| `careers.lightheart.games` | Lightheart Entertainment | 1 | não (Open Application, de 2021) |
| `career.maginteractive.com` | MAG Interactive | 0 | quadro vazio |
| `career.opusmajor.io` | Opus Major | 0 | quadro vazio |
| `careers.thegang.io` | The Gang | 0 | quadro vazio |
| `jobs.chiefrebel.com` | Chief Rebel | 0 | quadro vazio |
| `jobs.ohbibi.com` | Oh BiBi | 0 | quadro vazio |

**Saldo honesto desta sondagem: 13 quadros novos, 22 vagas somadas, e ZERO vaga da disciplina que a
campanha já não conhecesse.** O único acerto de disciplina (Kepler) é a requisição da Tactical
Adventures, já enviada em 06/09 — mesmo ID, dois quadros. O valor real do achado não é a vaga: é ter
provado que o **sitemap do quadro do grupo esconde a vaga do estúdio**.

### 4.1 A afirmação "domínio próprio não aparece no subdomínio do fornecedor" é **parcialmente falsa**

Sondei o subdomínio do fornecedor para os 62 quadros de domínio próprio, testando variantes de slug.
**27 dos 62 têm espelho vivo em `<slug>.teamtailor.com`**, respondendo pelas duas rotas. Entre eles,
justamente os que a triagem tinha dado como só existentes em domínio próprio:

| O que a triagem de hoje afirmou | O que medi |
|---|---|
| *"Não existe `snowprint.teamtailor.com`"* | Verdade para `snowprint`, **falso para o estúdio**: `snowprintstudios.teamtailor.com` responde **HTTP 200** |
| Kepler só em domínio próprio | `keplerinteractive.teamtailor.com` responde **HTTP 200** |
| Sharkmob só em `career.sharkmob.com` | `sharkmob.teamtailor.com` responde **200** |
| Sloclap só em domínio próprio | `sloclap.teamtailor.com` responde **200** |

**É outra vez o mesmo erro de slug**, não uma propriedade do Teamtailor. `snowprint` dá 404,
`snowprintstudios` dá 200 — exatamente o par `playgroundgames`/`playground-games` do brief.

Os outros **35** não apareceram por adivinhação de slug — mas isso mede a fragilidade do chute, não a
ausência do quadro (meu próprio chute errou `bulkhead` quando o certo era `bulkheadinteractive`, e
`realtimeuk` quando o certo era `realtime`).

**A lição que sobrevive à medição:** sondar `career./careers./jobs.` no domínio do estúdio é a rota
**confiável** porque não depende de adivinhar slug nenhum. Manter. Só não é verdade que os quadros
sejam invisíveis no fornecedor.

### 4.2 Onze quadros aparecem em dois hostnames — dedupe obrigatório

Contar hostname como quadro **infla o número**. Estes onze são o mesmo quadro duas vezes, com o
mesmo conjunto de IDs de requisição:

`careers.bulkhead.com` = `bulkheadinteractive.teamtailor.com` · `jobs.coffeestain.com` =
`coffeestainstudios.teamtailor.com` · `careers.embark-studios.com` = `embarkstudios.teamtailor.com` ·
`careers.envarstudio.com` = `envarstudio.teamtailor.com` · `career.goodbyekansas.com` =
`goodbyekansas.teamtailor.com` · `apply.ioi.dk` = `ioi.teamtailor.com` · `careers.realtimeuk.com` =
`realtime.teamtailor.com` · `careers.sloclap.com` = `sloclap.teamtailor.com` · `jobs.starbreeze.com` =
`starbreeze.teamtailor.com` · `jobs.stunlockstudios.com` = `stunlocksstudios.teamtailor.com` ·
`jobs.vinefx.com` = `vinefx.teamtailor.com`.

**102 hostnames = 91 quadros distintos.**

---

## 5. OS QUE EXIGEM CONTA DE CANDIDATO

O Teamtailor **não exige conta para se candidatar a uma requisição** — os formulários
`/jobs/<id>/applications/new` que testei devolveram HTTP 200 anônimos. Mas ele tem uma **área de
candidato separada**, o **Connect**, e é lá que mora o risco que a WildBrain expôs hoje.

**A campanha já tem perfil Connect em pelo menos 22 quadros Teamtailor**, registrados em `PORTAIS`.
Antes de tratar qualquer um destes como alvo novo, é preciso **entrar no Connect e conferir**, porque
o painel registra o cadastro mas não registra candidatura por dentro dele:

Snowprint Studios · Sharkmob · Paradox Interactive (departamento Art) · Starbreeze · Embark Studios ·
Arrowhead Game Studios · SYBO · Sloclap (**departamento CHARACTER ARTIST**) · Resolution Games ·
Ghost Ship Games · Beyond Frames / Cortopia · Gamecan · Frame Break · Funcom · 10 Chambers ·
Invisible Walls · Keen Games (**departamento Character Art**) · IO Interactive · iLogos (área Art / 3D
Artist) · Airship Interactive · Hampa Studio · Radical Forge · PLAYERUNKNOWN Productions ·
Wētā Workshop · Untold Studios · beffio · Realtime UK.

Dois casos no painel provam que a conferência por dentro é obrigatória:

- **beffio** — chegaram três emails *"Complete the application"* que **pareciam candidatura pendente** e
  não eram; a conferência por dentro do portal em 07/09 mostrou as três candidaturas registradas.
- **REALTIME UK** — a tela não confirmou o envio, e a conferência no painel Connect em 07/09 mostrou
  que **a candidatura tinha entrado**.

**Não abri nenhuma dessas áreas nesta rodada** — exigem login e o brief proíbe navegador. Ficam
nomeadas para a fila do Vini.

**Captcha:** nos três formulários que baixei (Snowprint, Fatshark, Tactical Adventures) **não vi
captcha no HTML — veredito só com o clique.**

---

## 6. DEDUPE — O PLACAR

Cruzei **por ID de requisição**, nunca por título, contra `docs/index.html` (745 `PORTAIS`,
665 `STUDIOS`, extraídos com o scanner que respeita aspas), `enviados.csv` (751 linhas) e
`automacao/processados.csv` (1.862 linhas).

| | |
|---|---|
| Vagas da disciplina achadas pelas duas rotas | **7** |
| Já no painel | **7** |
| Novas | **0** |
| Já com candidatura enviada e confirmada | **6** (Tactical Adventures, Fatshark, beffio ×3, Ironbird) |
| Já descartadas por veto escrito | **2** (Snowprint, Cast Iron) |

A `8311973` teria virado "vaga nova" se eu a tivesse trazido pelo nome do quadro
(*Kepler Interactive*) em vez do ID — o painel a registra sob *Tactical Adventures*. **É exatamente o
erro que custou 25 das 31 vagas de ontem.** O ID pegou; o nome não pegaria.

---

## 7. O QUE TRAVOU

- **5 hostnames não responderam** por recusa do proxy de saída ou queda do túnel, não por bloqueio do
  estúdio: `careers.digitaldomain.com`, `careers.bohemia.net`, `careers.gamecan.eu`, `jobs.qi.games`,
  `jobs.r-control.de`. **Não são quadros Teamtailor medidos** e não entram em nenhuma contagem.
- **Áreas de candidato (Connect)**: não conferidas, exigem login e o brief proíbe navegador.
- **Formulários**: nenhum aberto além do HTML. Nada preenchido, nada enviado.
- A sondagem de subdomínio do fornecedor depende de **adivinhar slug**, e adivinhação erra. Os 35
  quadros que marquei como "sem espelho" podem ter espelho sob um slug que não testei. Está declarado
  como limite da medição, não como fato.

---

## 8. RESUMO

- **102 hostnames Teamtailor refeitos** pelas duas rotas = **91 quadros distintos**. 77 com vaga,
  25 vazios confirmados pelas duas rotas.
- **`jobs.json` divergiu do `sitemap.xml` em 2 de 102** — e **nos dois o `sitemap` é que escondeu vaga**
  (Stillfront 39 × 4, Kepler 7 × 1). Totais: **402 × 361**, com o `jobs.json` **41 vagas à frente**.
  O conjunto "vaga que só o sitemap vê" ficou **vazio nos 102 quadros**.
- **O defeito relatado não se confirma.** O "0" da Paradox era **404 de slug inexistente contado como
  zero**: `career.paradoxplaza.com/jobs.json` devolve 18 de forma estável, em 12 chamadas seguidas e
  também sem `User-Agent`. O mesmo vale para SYBO e Goodbye Kansas.
- **Vagas da disciplina que a rota antiga escondia: 1** — a **Lead 3D Character Artist** do quadro do
  grupo Kepler (`8311973`), ausente do `sitemap.xml` e presente no `jobs.json`. E ela **já estava no
  painel** pela Tactical Adventures, com candidatura enviada em 06/09.
- **Vagas da disciplina achadas no total: 7. Já conhecidas: 7. Novas: 0.**
- **Achado extra da régua:** a Fatshark diz *"4 days in the office per week"*, e o termo `days a week`
  **não casa**. Buraco medido, correção sugerida, nenhum arquivo compartilhado tocado.
- **Correção honesta de duas afirmações de hoje:** o `sitemap.xml` **não** é mais confiável que o
  `jobs.json` — é menos, em quadro de grupo; e o Teamtailor em domínio próprio **aparece sim** no
  subdomínio do fornecedor em 27 dos 62 casos, inclusive Snowprint (`snowprintstudios.teamtailor.com`,
  HTTP 200), Kepler, Sharkmob e Sloclap.

*Nenhum arquivo compartilhado editado. Sem commit, sem push, sem email, sem formulário. Só `curl`.*
