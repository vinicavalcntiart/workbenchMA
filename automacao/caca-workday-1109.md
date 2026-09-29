# Caça ao Workday — 11/09/2026, tarde — RODADA DE ZERO PERSONAGEM

Quarta varredura do Workday, feita depois de ler `BRIEFING.md` inteiro, `automacao/BRIEF-JHON.md`
e `automacao/caca-workday-lote3.md`. Tudo abaixo saiu de `python3`/`requests` e `curl`.
**Nenhum navegador foi aberto.** Nada foi enviado, nenhum formulário foi preenchido, e
`enviados.csv`, `automacao/pessoas.csv` e `docs/index.html` **não foram tocados**.

Esta rodada obedece à **REGRA DO VINI de 10/09** (personagem e criatura primeiro; modelagem e
superfície genéricas só com a frase do corpo citando personagem; ambiente por último e nunca como
carro-chefe) e ao **escopo geográfico** (América do Norte, Europa, Oceania, e na Ásia só Coreia do
Sul e Singapura).

---

## 1. PLACAR — o número honesto vem antes da narrativa

| Medida | Número |
|---|---|
| Nomes de locatário (slugs) sondados, **inéditos nesta rodada** | **1.942** |
| Pods testados | **15** (`wd1 wd3 wd5 wd10 wd12 wd102 wd103 wd105 wd107 wd108 wd109 wd501 wd502 wd503 wd504`) |
| Requisições de sondagem (`GET robots.txt`) | **29.130** |
| **`422`** (o locatário NÃO existe naquele pod) | **29.053** |
| **Locatários que EXISTEM** | **77** |
| — destes, **novos para a campanha** (não constam dos lotes 1, 2 e 3) | **45** |
| — `200`, o `robots.txt` revela os sites | **52** |
| — `401`, API pública fechada (parede) | **24** |
| — `410`, **código novo:** `ERR_TENANT_MIGRATED` | **1** (`comcast`/wd5) |
| Sites revelados pelo `robots.txt`, **sem um palpite** | **143** |
| Sites com vaga dentro | **97** |
| Vagas existentes nesses quadros (soma dos `total`) | **21.333** |
| **Anúncios distintos LIDOS** (9 termos × 143 sites) | **3.758** |
| Anúncios lidos na **rotina fixa do grupo Disney** (6 quadros) | **1.008** (333 deles são os mesmos dois quadros da Netflix da linha acima) |
| **Total de anúncios distintos lidos nesta sessão** | **4.433** |
| Registros relidos na **passagem sem teto de paginação** (25 quadros grandes) | **1.457** |
| Bateram no filtro de título da disciplina | **90** |
| — **ruído de título** (esqui, barbeador, BIM, analytics, yoga) | **71** |
| — quadro de arte que a campanha **já lê** (Netflix e Eyeline), IDs todos já tratados | **18** |
| — **já descartada hoje mesmo** (Razer `JR2026007640`) | **1** |
| — **vagas de personagem/criatura/modelagem de arte INÉDITAS** | **0** |
| **FILA NOVA** | **0** |

**Seja honesto com o número: 1.942 slugs inéditos, 29.130 sondagens, 45 locatários Workday novos
no mapa da campanha, e eles renderam ZERO vaga de personagem.** Nenhuma linha foi acrescentada a
`automacao/FILA-DO-VINI.md`, porque não havia o que acrescentar. **A quebra que o Vini pediu:
0 de PERSONAGEM, 0 de AMBIENTE, 0 enviadas.**

---

## 2. O QUE ESTA RODADA NÃO REFEZ, de propósito

- **Não** repetiu o censo dos 123 quadros (lido inteiro em 08–10/09).
- **Não** repetiu a sondagem dos 1.365 slugs contra Greenhouse e Ashby (deu zero).
- **Não** repetiu a varredura dos 6.260 domínios (85 quadros novos, zero personagem).
- **Não** repetiu os 5.448 slugs do lote 3: a lista desta rodada foi montada nova, a partir de
  `automacao/censo-boards-0809.csv`, `automacao/backlog-estudios.md`, `docs/index.html` e de nomes
  de casas grandes de jogos, animação, VFX, brinquedo, mídia, cassino, parque e tecnologia.
  **Onde houve sobreposição com o lote 3, ela aparece medida na §3**: dos 77 locatários que
  existem, 32 já estavam no mapa e 45 são novos.

**A única coisa que esta rodada REFEZ é a rotina fixa do grupo Disney**, porque o BRIEFING manda
olhar o grupo em toda rodada de caça, sem exceção. O resultado está na §6 e é **zero novo**, a
terceira confirmação do dia.

---

## 3. OS 45 LOCATÁRIOS NOVOS — para a próxima rodada não gastar sondagem neles

Todos conferidos individualmente; nenhum código diferente de `422` entrou no mapa sem reconferência.

### 3.1 — `200`, quadro aberto e lido (33 novos)

> A linha do `adobe` está aqui só como reconferência: ele **já era conhecido** do lote 2 e não conta
> entre os 45 novos.

| Locatário / pod | Sites revelados | Quem é de verdade | Vagas | Da disciplina |
|---|---|---|---|---|
| `accenture`/wd103 | `AccentureCareers`, `AccentureLeadershipCareers`, `AvanadeCareers`, `AvanadeLeadershipCareers` | Accenture + Avanade | 2.606 | **0** |
| `adobe`/wd5 (reconferido) | `external_experienced` | Adobe | 736 | **0** |
| `aenetworks`/wd1 | `AE-Careers` | **A+E Networks** (History, Lifetime) | 16 | **0** |
| `alterra`/wd1 | 20 quadros de estação de esqui | **Alterra Mountain** | 500+ | **0** (ver §5) |
| `amcn`/wd5 | `amcnetworks` | **AMC Networks** | 24 | **0** |
| `american`/wd1 | `AU` | American University | 184 | **0** |
| `cecentertainment`/wd5 | `CEC` | Chuck E. Cheese | — | **0** |
| `cgf`/wd10 | `CG` | **Canaccord Genuity**, banco de investimento | 31 | **0** (ver §5) |
| `daveandbusters`/wd1 | `DaveandBusters` | Dave & Buster's | — | **0** |
| `directv`/wd1 | `Careers` | DirecTV | 25 | **0** |
| `encore`/wd1 | 17 quadros numéricos | Encore (eventos corporativos) | 0 | **0** |
| `federation`/wd105 | `Federation_Careers` | Federation Entertainment (produtora FR) | 7 | **0** |
| `google`/wd501 | `GOCJobs` | Google Operations Center | 109 | **0** |
| `havas`/wd3 | `GroupExternalCareerSite`, `MediaExternalCareerSite`, `CreativeExternalCareerSite`, `PopExternalCareerSite`, `HealthYouExternalCareerSite`, `BETCHavas` | Havas (publicidade) | 671 | **0** |
| `hp`/wd5 e `hpinc`/wd5 | `ExternalCareerSite`, `EXTEU-AC-CareerSite`, `HPINC` | HP | 2.075 | **0** |
| `infosys`/wd103 | `Simplus_Careers`, `WONGDOODY_G_Careers`, `WongDoody_EU_Careers`, `BlueAcorn_Careers`, `GuideVision_Careers`, `Kaleidoscope_Careers`, `Fluido_Careers`, `BLS_Careers` | Infosys + WongDoody | 17 | **0** |
| `just`/wd3 | `JUST_External` | JUST (alimentos) | 16 | **0** |
| `keppel`/wd3 | `KeppelCareers` | Keppel (Singapura, infraestrutura) | 210 | **0** |
| `lifetime`/wd1 | `lifetime` | Life Time (academias) | 2.000 | **0** (ver §5) |
| `nine`/wd105 | `Nine_External_Career_Site` | Nine Entertainment (AU) | 35 | **0** |
| `orange`/wd3 | `Orange_Career` | Orange (telecom) | 2 | **0** |
| `paper`/wd3 | `Paper_Careers` | Paper (educação) | 1 | **0** |
| `philips`/wd3 | `jobs-and-careers`, `Internal-Job-Postings-List-for-Philips-Contingent-Workers` | Philips | 1.060 | **0** (ver §5) |
| `propertyguru`/wd105 | `PropertyGuru` | PropertyGuru (Singapura) | 25 | **0** |
| `ringling`/wd1 | `RinglingExternalCareers`, `RinglingExternalCareersFaculty`, `RinglingStudentEmployment` | **Ringling College of Art and Design** | 8 | **0** — só docência e administração |
| `sands`/wd1 | `sands_careers`, `fortis_careers`, `referral_sands_careers`, `SDSCareers` | Las Vegas Sands | 20 | **0** |
| `sevenwestmedia`/wd105 | `SWM` | Seven West Media (AU) | 57 | **0** |
| `sonos`/wd1 | `Sonos`, `Student_Opportunities` | Sonos | 39 | **0** |
| `telstra`/wd3 | `Telstra_Careers`, `tls-careers`, `Private` | Telstra | 241 | **0** |
| `topgolf`/wd501 | `TopgolfCareers` | Topgolf Callaway | 703 | **0** |
| `treehouse`/wd1 | `TreeHouseCareers` | TreeHouse Foods | 190 | **0** |
| `wpp`/wd3 | **`robots.txt` `200` com corpo VAZIO** | WPP (publicidade) | — | site não revelado; prioridade zero para a disciplina |
| `yle`/wd502 | `External` | Yle (TV pública finlandesa) | 9 | **0** |

### 3.2 — `401`, existem e a API pública está desligada (11 novos, de 24 no total)

`bonnier`/wd3 · `cbs`/wd3 · `coupang`/wd3 · `crunchyroll`/wd1 · `dave`/wd1 · `facebook`/wd1 ·
`lenovo`/wd1 · `mediamonks`/wd3 · `panasonic`/wd1 · `plex`/wd1 · `reddit`/wd1

**Nenhum destes vale `precisa-de-navegador` para a disciplina.** O único de mídia com arte plausível
é a **Crunchyroll** (anime, grupo Sony), e ela é distribuição e localização, não produção 3D de
personagem. A fila de navegador continua a mesma do lote 3: **Epic Games, Krafton, EA, DNEG,
Keywords, Sony Interactive.**

### 3.3 — `410`, um código que a campanha nunca tinha visto

`comcast`/wd5 devolve, no corpo do `robots.txt`:

```
{"errorCode":"ERR_TENANT_MIGRATED","httpStatus":410,
 "messageParams":{"outageUrl":"https://wd5.myworkday.com/wday/drs/outage?t=comcast"}}
```

**Isto é um terceiro estado, e ele não é `422` nem `401`: o locatário EXISTIU e foi MIGRADO.**
Conferido nos 15 pods (`422` em todos os outros), no host alternativo `wd5.myworkdaysite.com`
(mesma família de resposta) e com oito palpites de site (`External`, `Comcast`, `ComcastCareers`,
`External_Career_Site`, `careers`, `Careers`, `NBCUCareers`, `comcast_careers`): **todos `303` ou
`410`, nenhum quadro legível.** A Comcast (dona da NBCUniversal e da DreamWorks) **não é lida por
esta API**. A via da DreamWorks continua sendo o SmartRecruiters `nbcuniversal3`, como o BRIEFING
já diz.

---

## 4. O NEGATIVO MEDIDO, que vale tanto quanto o positivo

Estes nomes foram sondados nos 15 pods e devolveram **`422` em todos**, ou seja, **não têm
locatário Workday com esse nome**. Escrevo porque a próxima rodada não precisa gastar sondagem
nem raciocínio com eles:

**Casas grandes de jogos:** `ubisoft`, `ubi`, `ubisoftentertainment`, `taketwo`, `take2interactive`,
`rockstargames`, `rockstarnorth`, `2kgames`, `zyngainc`, `nintendoamerica`, `nintendoeurope`,
`valvesoftware`, `bethesda`, `zenimax`, `zenimaxmedia`, `blizzardentertainment`,
`activisionblizzard`, `netease`, `neteasegames`, `squareenixamerica`, `squareenixeurope`,
`bandainamcoentertainment`, `capcom`, `koeitecmo`, `embracer`, `thqnordic`, `plaion`, `crytek`,
`larian`, `cdprojekt`, `techland`, `bloober`, `peoplecanfly`, `paradox`, `starbreeze`,
`frontier`, `codemasters`, `rebellion`, `team17`, `jagex`, `splashdamage`, `creativeassembly`,
`obsidian`, `idsoftware`, `improbable`, `sumodigital`.

**Coreia do Sul e Singapura, que estão no escopo e por isso foram sondadas nome a nome:**
`nexon`, `nexongames`, `nexonamerica`, `ncsoft`, `ncsoftwest`, `netmarble`, `netmarbleus`,
`pearlabyss`, `pearlabysscorp`, `smilegate`, `smilegatewest`, `kakao`, `kakaogames`, `kakaocorp`,
`com2us`, `neowiz`, `webzen`, `shiftup`, `gravity`, `devsisters`, `wemade`, `garena`,
`garenaonline`, `seagroup`, `virtuos`, `virtuosgames`, `mightybear`, `secretlab`, `singtel`,
`temasek`. **Só `krafton`/wd3 e `razer`/wd3 existem, e os dois já eram conhecidos.**

**Animação e VFX:** `weta`, `wetafx`, `wetadigital`, `wetaworkshop`, `animallogic`, `framestore`,
`framestoreltd`, `doublenegative`, `dnegplc`, `cinesite`, `cinesiteinc`, `rodeofx`, `scanlinevfx`,
`pixomondo`, `digitaldomain`, `methodstudios`, `technicolor`, `technicolorgroup`,
`technicolorcreative`, `mikros`, `jellyfishpictures`, `milkvfx`, `outpostvfx`, `aardman`,
`cartoonsaloon`, `wildbrain`, `thunderbird`, `nelvana`, `corus`, `dhx`, `ninestory`, `titmouse`,
`shadowmachine`, `bentobox`, `flyingbark`, `mainframe`, `bardel`, `atomiccartoons`,
`iconcreative`, `guru`, `illumination`, `dreamworks`, `dreamworksanimation`.

**Mídia e grupo grande:** `wb`, `wbd`, `wbgames`, `warnermedia`, `warnerbrosdiscovery`,
`warnerbrosgames`, `nbcu`, `nbcuni`, `nbcuniversal`, `universalstudios`, `universalpictures`,
`universalparks`, `paramountglobal`, `paramountpictures`, `viacomcbs`, `nickelodeon`,
`skydanceanimation`, `skydancemedia`, `lionsgate`, `lionsgatefilms`, `amcnetworks` (o que existe é
`amcn`), `hasbro`, `hasbroinc`, `hasbrogroup`, `wizardsofthecoast`, `wotc`, `funko`, `jakks`,
`sonypicturesanimation`, `sonypicturesimageworks`, `imageworks`, `sonypicturesentertainment`.

**A leitura disso, e ela poupa rodada:** o Workday é ATS de corporação grande de RH, não de estúdio
de arte. As casas de arte que ele cobre **já estão todas mapeadas** (Disney, Netflix, Warner, Pixar,
ILM/Eyeline por dentro da Disney e da Netflix, Cloud Imperium, Aristocrat, Light & Wonder, Sega,
Gearbox, Unity, LEGO, Spin Master, Razer, Krafton, Epic, EA, Sony Interactive, DNEG, Keywords,
MPC, Magic Leap, Tencent, Activision/Xbox). **O Workday, como fonte de descoberta de vaga de
personagem, está esgotado.** Quem quiser achar casa nova tem que ir a outro ATS, não a outro slug.

---

## 5. FALSOS AMIGOS NOVOS — a palavra certa no emprego errado

Some-se aos seis do lote 1, dez do lote 2 e nove do lote 3.

| Locatário | Quem realmente é | Por que engana |
|---|---|---|
| `alterra`/wd1 | **Alterra Mountain**, estações de esqui (Steamboat, Deer Valley, Winter Park, Stratton, Crystal Mountain, Snowshoe, Blue Mountain) | **É a maior fábrica de falso positivo da palavra `groom` que já apareceu**: 9 casamentos de *Groomer*, *Advanced Groomer*, *Terrain Park Groomer*, *Grooming Mechanic*, *Slope Grooming*. É **quem alisa a neve com a máquina**, não groom de cabelo e pelo. Pior que a "Grooming" da Procter & Gamble do lote 3, porque aqui o cargo se chama literalmente **Groomer** |
| `philips`/wd3 | Philips | **12 casamentos de `groom`**, todos *Male Grooming* e *Grooming & Beauty*: barbeador elétrico. Mesma família da P&G |
| `lifetime`/wd1 | Life Time (rede de academias) | Casa com `sculpt` em **Yoga Sculpt Instructor**. Também parece a Lifetime da A+E, e não é |
| `cgf`/wd10, quadro `CG` | **Canaccord Genuity**, banco de investimento | O quadro se chama **`CG`**. Nenhuma relação com computação gráfica: as vagas são risco de mercado e finanças em Toronto |
| `tt`/wd503 | **Thornton Tomasetti**, engenharia estrutural | 5 casamentos de *Modeler*: **BIM Modeler** e **Tekla Modeler**, que é modelagem de estrutura de aço |
| `accenture`/wd103 | Accenture | **38 casamentos de `modeling`**, todos *Analytics and Modeling* e *Data Modeler*. Zero é arte |
| `ringling`/wd1 | **Ringling College of Art and Design** | Nome de escola de arte de verdade, e a mais famosa de animação dos EUA. **Mas o quadro é de docência e administração**, não de produção |
| `federation`/wd105 | Federation Entertainment | Produtora francesa de série; 7 vagas, todas de produção e negócio |
| `google`/wd501, quadro `GOCJobs` | **Google Operations Center** | Não é a Google de engenharia: é o centro de operações de suporte |
| `american`/wd1, quadro `AU` | **American University**, Washington | `AU` parece sigla de estúdio australiano |
| `just`/wd3 | JUST (alimentos à base de planta) | Palavra comum que vira slug |
| `encore`/wd1 | Encore Global, produção de evento corporativo | Parece a **Encore Hollywood**, casa de pós-produção. Não é: os 17 quadros dele são numéricos e estão todos vazios |

---

## 6. ROTINA FIXA DO GRUPO DISNEY — feita, e deu zero pela terceira vez hoje

Ordem do Vini de 10/09: *"n esqueça da disney. sempre olho no grupo disney pixar etc."*
Os seis quadros do grupo foram varridos com os **9 termos**, filtro de local aplicado cedo.

| Quadro | Vagas lidas | Acertos de título na disciplina | Novo |
|---|---|---|---|
| `disney`/wd5/`disneycareer` | 273 | 11 | **0** |
| `disney`/wd5/`disneycareerdc` | 255 | 10 | **0** |
| `pixar`/wd501/`Pixar_External_Career_Site` | **0** (quadro vazio) | 0 | **0** |
| `netflix`/wd108/`Netflix` | 300 | 12 | **0** |
| `netflix`/wd108/`Eyeline` | 33 | 6 | **0** |
| `warnerbros`/wd5/`global` | 147 | **0** | **0** |

**Todos os acertos são IDs já tratados**, um a um:

- `10159882` Senior Modeler, ILM Sydney — **ENVIADA em 04/09**.
- `10159370` / `10159371` Texture Artist, ILM London — enviadas **e recusadas**.
- `10157562` Creature TD (all levels), ILM London · `10155976` e `10144787` Creature TD (Rigging),
  ILM Vancouver · `10126752` Creatures FX, Iver Heath — **a armadilha medida: Creature TD é rigging
  e Creature FX é simulação. Os quatro continuam FORA apesar da palavra creature.**
- `10159762` Character Design Lead, Disney TV Animation — **concept 2D, e já enviada em 02/09**.
- `10154147` Sr Character Modeler (West Mumbai), `10155895` Lead Modeler (Mumbai), `10145923`
  Creature Supervisor (Mumbai), `10155202` e `10155332` Look Dev TD (Mumbai) — **Índia, fora do
  escopo, cortadas no filtro de local antes da leitura de corpo**.
- `JR41751` Character Modeling Supervisor, NAS Sydney — **ENVIADA em 09/09** (dedupe rodado hoje,
  §7).
- `JR41810` / `JR39105` Head of Character Effects (CFX) — **CFX é simulação, fora**.
- `JR41777` Character Designer – Ink e `JR41753` Visual Development Artist – Ink — **2D, a `JR41753`
  já recusada com motivo escrito em 09/09**.
- `JR41734`, `JR41749`, `JR39446`, `JR39273` (ambiente, NAS) — **todas ENVIADAS em 09/09**.
- `JR40923`, `JR40928`, `JR40941` Eyeline Seul — **todas ENVIADAS em 09/09**.
  `JR01060`, `JR41011`, `JR41016` Eyeline **Hyderabad — Índia, fora**.
- `AJRT44076`, `JR40624`, `JR37504` da Netflix — engenharia de aprendizado de máquina e produto.

**Terceira confirmação no mesmo dia de que o estoque de personagem do grupo Disney dentro do
escopo está esgotado.**

---

## 7. A RÉGUA — e por que ela quase não teve o que fazer

A régua de veto (`authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`,
`days a week`, `citizen`, `resident`, `visa`, `relocat`, `right to work`, `security clearance`,
`onsite`, `in-office`, `hybrid`, mais os termos de francês `français`, `oral et`, `courant`,
`bilingue`, `francophone`) **só se aplica a vaga que chegou viva ao fim do funil, e nenhuma chegou**.

Os dois únicos IDs da família da disciplina que a varredura reencontrou já estavam resolvidos, e os
dois passaram por `sh automacao/dedupe-agora.sh` **hoje**:

**`JR41751` — Character Modeling Supervisor, Netflix Animation Studios, Sydney**
- `sh automacao/dedupe-agora.sh "JR41751" "Netflix Animation Studios"`
- `enviados.csv` **1 ocorrência COM marca de envio**: *"Application Submitted. Your application has
  successfully been submitted. TRES PROVAS: URL
  netflix.wd108.myworkdayjobs.com/en-US/Netflix/jobTasks/completed/application"*
- `docs/index.html` 2 ocorrências, também com marca. **JÁ ENVIADA em 09/09. Não repetir.**

**`JR2026007640` — Senior Character Designer (6 months contract), Razer, Singapura**
- `sh automacao/dedupe-agora.sh "JR2026007640" "Razer"`
- `processados.csv` **3 ocorrências**, e a terceira é o veredito de hoje:
  *"`JR2026007640`,descarte,DESCARTE POR DISCIPLINA, e uma CORRECAO da classificacao da caca das
  15h45, que a trouxe como personagem."*
- **Era a nº 1 da fila do lote 3 e foi DESCARTADA hoje, 11/09**, porque o cargo dirige concept
  artists e não esculpe nada — a armadilha do *"Character Designer"* que o BRIEFING descreve.
  Esta varredura **confirma o descarte e não a ressuscita**. A vaga continua aberta no quadro
  (`razer`/wd3/`Careers`, 182 vagas), e é assim que ela deve continuar: fora.

### O único ANÚNCIO INTEIRO que valeu a pena baixar, e por que ele cai

Dos 90 acertos de título, **um** não se resolvia pelo empregador mais o título, e por isso foi
baixado por inteiro pela API (`GET .../wday/cxs/lego/LEGO_External/job/Billund/Product-Designer-Talent-Pool---LEGO--DESiGN_0000031821`, **HTTP 200**, 7.808 caracteres):

**`0000031821` — Product Designer Talent Pool, LEGO® DESiGN — Billund, Dinamarca**
(`lego`/wd103/`LEGO_External`, dentro do escopo europeu)

- **Régua de veto, termo a termo, com a frase colada:**
  - `eligib` (1ª) → *"When goals are reached and if **eligible**, you'll be rewarded through our
    bonus scheme."* → **falso positivo: é benefício**, exatamente o padrão já catalogado.
  - `eligib` (2ª) e `hybrid` → *"Our **hybrid** work policy means an average of 3 days per week in
    the office. The hiring team will discuss the policy and role **eligibility** with you."* →
    **restrição de presença**, não regra de quem pode se candidatar.
  - `authoriz` 0 · `sponsor` 0 · `work permit` 0 · `must be based` 0 · `LMIA` 0 · `citizen` 0 ·
    `resident` 0 · `visa` 0 · `relocat` 0 · `right to work` 0 · `security clearance` 0 ·
    `français`/`oral et`/`courant`/`bilingue`/`francophone` 0. **Nenhum veto escrito.**
- **E mesmo assim ela CAI, por disciplina, e a frase é do anúncio:**
  *"In this role, your focus will be on creating **physical LEGO models** that spark creativity and
  joy"*, *"you take the lead in developing and refining LEGO models, ensuring **structural
  stability, build quality**"*, e a única menção a 3D é
  *"Experience with **3D modelling or digital building tools (e.g., LEGO Digital Designer, Studio)
  — a plus**"*. **É design de modelo físico de tijolo, não escultura nem modelagem de personagem 3D.**
  A palavra *character* aparece só em *"models that are playful, clear, and full of **character**"*
  e na lista de tipos de build. Some-se que é **banco de talentos com janela fechada**:
  *"The next application round opens from **February 6 to March 2**."*

**Nenhum veto escrito foi encontrado nesta rodada, e nenhum finalista chegou vivo à régua.**
Os outros 71 acertos de título foram descartados pelo par **empregador + cargo**, que aqui decide
sozinho e sem ambiguidade: *Groomer* numa estação de esqui, *Male Grooming* num fabricante de
barbeador, *BIM Modeler* numa engenharia estrutural, *Analytics and Modeling* numa consultoria e
*Yoga Sculpt Instructor* numa academia **não são vaga de arte** e não pedem leitura de corpo.

---

## 8. ARMADILHAS DE MÉTODO MEDIDAS HOJE

**1. O extrator de site do `robots.txt` pode devolver ZERO sem erro nenhum.** A primeira passagem
desta rodada leu 26 locatários `200` e produziu **`pares site: 0`**, o que parece "nenhum locatário
tem quadro" e é bug de expressão regular: eu exigia **dois** segmentos de caminho (`/a/b`) e o
Workday escreve **`Allow: /NomeDoSite/`**, com um só. O conserto é casar
`(?:Allow|Disallow):\s*/([^/|\s]+)/` e `Sitemap:\s*https?://[^/]*?/([^/]+)/siteMap`, descartando
`refreshFacet`. **Regra: extração que devolve zero em cima de 26 entradas boas é defeito do
extrator, nunca resultado.**

**2. `cd X && cmd1; cmd2` perde o diretório no segundo comando.** Nesta sessão o diretório de
trabalho volta ao padrão entre chamadas, e o `cd` de uma linha composta só vale para o primeiro
comando. Três buscas do grupo Disney saíram com **`Exit 2`** por isso, parecendo quadro fora do ar.
**Use caminho absoluto em todo argumento**, sempre.

**3. Teto de paginação por termo esconde vaga em quadro grande.** A colheita normal para em
`offset 200` por termo; quadros como `AccentureCareers` (2.000), `lifetime` (2.000), `LNExternalSite`
(1.449) e `EXTEU-AC-CareerSite` (1.169) estouram esse teto. **Fechei o buraco com uma segunda
passagem sem teto**, só com `character`, `creature`, `sculpt` e `groom`, nos **25 quadros com 200 ou
mais vagas**: 1.457 registros relidos, **nenhum acerto novo**. Sem essa passagem o placar seria
incompleto e eu não saberia.

**4. `robots.txt` `200` com corpo VAZIO continua existindo** (`wpp`/wd3 aqui; `fc`/wd10 e Epic no
lote 3). É locatário vivo com site não revelado, e só palpite ou navegador resolve.

**5. A vazão continua sendo do proxy.** 16 trabalhadores deram **~17 requisições por segundo**
estáveis nas três ondas; as 29.130 sondagens levaram cerca de **29 minutos de relógio**. Bate com a
medição do lote 3 e confirma que passar de 16 não acelera.

---

## 9. COMO ISTO FOI RODADO, para quem repetir

1. **Lista de candidatos, montada nova** — 528 nomes de casa (jogos, animação, VFX, brinquedo,
   mídia, cassino, parque, tecnologia, Coreia do Sul e Singapura), 233 nomes da segunda onda
   (produtoras europeias, Oceania, Coreia, Singapura, entretenimento ao vivo) e 174 **tokens
   alternativos** escritos à mão para casa grande (`wb`, `wbd`, `nbcu`, `zenimax`, `wotc`,
   `imageworks`, `ncwest`…). Normalização em compacto, hifenizado, primeira palavra e forma sem
   sufixo → **1.942 slugs únicos**.
2. **Sondagem** — `GET https://<slug>.<pod>.myworkdayjobs.com/robots.txt` nos 15 pods,
   **29.130 requisições**, 16 trabalhadores, gravação incremental. `422` descarta; **todo outro
   código é reconferido sozinho** (foi assim que o `410` do `comcast` virou achado em vez de ruído).
3. **Extração de site** — as linhas `Allow:`/`Sitemap:` dos 52 locatários `200` deram **143 sites,
   zero palpite**.
4. **Dimensionamento** — um `POST .../jobs` com `offset:0` por site para ler o `total`. 97 têm vaga.
5. **Colheita** — `POST https://<host>/wday/cxs/<locatario>/<site>/jobs` com
   `{"appliedFacets":{},"limit":20,"offset":N,"searchText":"<termo>"}`, **`limit:20` porque `50`
   devolve 400**, nos 9 termos: `character`, `creature`, `modeler`, `modeling`, `sculpt`, `groom`,
   `surfacing`, `look development`, `visual development`.
6. **Segunda passagem sem teto** nos 25 quadros com 200+ vagas (§8, item 3).
7. **Rotina fixa do grupo Disney** nos 6 quadros, com filtro de local aplicado antes da leitura.
8. **Filtro de título → leitura de corpo** — 90 acertos de título: **71 ruído**, 18 do quadro de arte
   que a campanha já lê (Netflix e Eyeline, todos já tratados), 1 já descartada hoje (Razer).
   **Um anúncio inteiro baixado pela API** (LEGO `0000031821`), com a régua termo a termo na §7.
9. **Dedupe** — `sh automacao/dedupe-agora.sh <ID> "<Casa>"` nos dois IDs da família da disciplina
   que apareceram, com as quatro contagens por arquivo (§7).

Os únicos arquivos escritos por esta rodada são **este** e uma linha em
`automacao/processados.csv`. **`automacao/FILA-DO-VINI.md` não foi tocado porque a rodada fechou em
zero, e fila inflada vale menos que rodada de zero com o número medido.**
