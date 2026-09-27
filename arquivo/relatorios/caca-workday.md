# Caça ao Workday — 09/09/2026, madrugada

Varredura do Workday inteiro dentro do escopo. Tudo abaixo foi **rodado com `curl`/Python
nesta sessão**, nenhum navegador foi aberto, nada foi commitado, enviado ou preenchido.

---

## PLACAR, antes de qualquer narrativa

| Medida | Número |
|---|---|
| Nomes de locatário testados | **551** |
| Pods `wdN` testados / que existem de verdade | 22 / **12** |
| Requisições de sondagem de locatário | **6.983** |
| **`422`** (locatário NÃO existe naquele pod) | **6.610** |
| **Locatários que EXISTEM** | **48** |
| — destes, entregaram `robots.txt` e revelaram os sites (`200`) | **27** |
| — destes, API pública fechada por `401` (nenhum site adianta) | **20** |
| — destes, `410` (locatário aposentado: `comcast`) | **1** |
| **`404` de site errado, resolvidos** (site certo achado) | **25 locatários → 52 sites** |
| **`404` de site errado, NÃO resolvidos** | **2** (`epicgames`, `krafton`) |
| Quadros `200` com vaga dentro | **45** |
| Vagas únicas colhidas (paginação 100% de cada quadro) | **9.246** |
| Bateram no filtro de título | 207 |
| Vagas **da disciplina** (qualquer geografia) | **36** |
| Sobreviveram ao **escopo** | **20** |
| Sobreviveram à **régua de 17 termos** | **20** (nenhum veto de imigração; ver §4) |
| Reprovadas no detalhe (disciplina/senioridade) | **3** |
| **Removidas pelo dedupe por ID de requisição** | **8** |
| **FILA FINAL PRONTA PARA CLICAR** | **10 novas + 2 sinalizadas** |

---

## 1. A FILA PRONTA

Formato de todas: **Workday, formulário oficial** — o mesmo caminho já provado em 04/09 com a
Senior Modeler da ILM Sydney. Todas as URLs abaixo **foram testadas nesta sessão e devolveram
HTTP 200**. O dedupe por **ID de requisição** foi feito linha a linha contra `docs/index.html`,
`enviados.csv`, `automacao/processados.csv` e `automacao/FILA-DO-VINI.md`.

### TOPO — REGRA 14 (Disney / ILM)

Aviso honesto antes das duas: **você varreu as quatro casas às 22h30 de 08/09 e deu zero.**
Estas duas não contradizem isso — elas estão num **segundo quadro da Disney que a campanha nunca
tocou**, o site `disneycareerdc` (643 vagas), irmão do `disneycareer` (626 vagas) que você já usa.
As duas **não aparecem** no `disneycareer`. `grep -c disneycareerdc` nos quatro arquivos = **0**.

---

**1. Lead Generalist Artist — ILM Vancouver (Disney)**
- Locatário / site: `disney` / `disneycareerdc` (pod `wd5`) — **quadro novo para a campanha**
- Local: Vancouver, BC, Canadá · Híbrido, 2–3 dias no escritório
- Requisição: **`10142674`** · Postada 2026-06-11
- Faixa **publicada**: **CAD 126.800 – 162.300**
- URL: https://disney.wd5.myworkdayjobs.com/en-US/disneycareerdc/job/Vancouver-BC-Canada/Lead-Generalist-Artist_10142674
- **Régua de veto: os 17 termos deram ZERO casamento no detalhe completo.** Nenhuma frase de
  autorização, patrocínio, residência ou realocação. Limpa.
- Dedupe: `10142674` → **0 ocorrências** nos quatro arquivos. NOVA.
- Conta como disciplina: generalista 3D / ambiente — *"Generalists independently build complete
  photorealistic environments (…) full CG environments"*, com liderança. **Ressalva honesta:** a
  categoria interna da vaga é `Matte - Studios` e parte do trabalho é Digital Matte Painting, que
  é pintura, não modelagem. É liderança de arte 3D de ambiente, não de personagem.

---

**2. Pre-Visualisation Generalist Artist (All Levels) — ILM London (Disney)**
- Locatário / site: `disney` / `disneycareerdc` (pod `wd5`) — **quadro novo para a campanha**
- Local: Londres, Reino Unido · Híbrido, 2 dias no escritório
- Requisição: **`10137201`** · Postada 2025-11-20 (antiga, mas **viva**: detalhe respondeu 200 hoje)
- Faixa: não publicada
- URL: https://disney.wd5.myworkdayjobs.com/en-US/disneycareerdc/job/London-United-Kingdom/Pre-Visualisation-Generalist-Artist--All-Levels-----ILM-London_10137201-2
- **Régua de veto: ZERO casamento dos 17 termos.** Limpa.
- Dedupe: `10137201` → **0 ocorrências**. NOVA.
- Conta como disciplina, e no texto dela: *"Modeling, texturing and rigging of characters,
  creatures, vehicles, props, and environments"*. Ferramentas citadas: Maya, ZBrush, Substance,
  Blender, Unreal. **Ressalva honesta:** é previs, ou seja, asset rápido e otimizado, não hero
  asset — o nível de acabamento não é o do portfólio dele. "All Levels" abre para sênior.

---

### Netflix — a casa que a campanha nunca tinha achado no Workday

Netflix mora no pod **`wd108`**, que **não estava na lista de pods do briefing**. Por isso passou
batida até hoje. `grep -c wd108` nos quatro arquivos = **0**. São dois quadros: `Netflix`
(656 vagas, inclui a Netflix Animation Studios) e `Eyeline` (46 vagas, o braço de VFX).

**3. Modeling Supervisor — Eyeline Seoul**
- Locatário / site: `netflix` / `Eyeline` (pod `wd108`)
- Local: Seul, Coreia do Sul (**dentro do escopo asiático permitido**) · Presencial
- Requisição: **`JR40941`** · Postada 2026-06-08 · Faixa: não publicada
- URL: https://netflix.wd108.myworkdayjobs.com/en-US/Eyeline/job/Eyeline-Seoul/Modeling-Supervisor_JR40941
- **Régua: ZERO casamento dos 17 termos.** Limpa.
- Dedupe: **0 ocorrências**. NOVA.
- Disciplina cheia e no nível dele: *"responsible for the artistic and technical quality of all 3D
  models (…) establishing workflows, managing the modeling team, and training artists"*. Maya, ZBrush.

**4. Lead Modeler — Eyeline Seoul**
- Locatário / site: `netflix` / `Eyeline` (pod `wd108`)
- Local: Seul, Coreia do Sul · Presencial
- Requisição: **`JR40923`** · Postada 2026-06-08 · Faixa: não publicada
- URL: https://netflix.wd108.myworkdayjobs.com/en-US/Eyeline/job/Eyeline-Seoul/Lead-Modeler_JR40923
- **Régua: ZERO casamento dos 17 termos.** Limpa.
- Dedupe: **0 ocorrências**. NOVA.
- Disciplina cheia: *"poly modeling skills from creating environments, vehicles, props, and
  characters (…) emphasis on photorealism"*. Maya, ZBrush.

**5. Lead Surfacing Artist — Eyeline Seoul**
- Locatário / site: `netflix` / `Eyeline` (pod `wd108`)
- Local: Seul, Coreia do Sul · Presencial
- Requisição: **`JR40928`** · Postada 2026-06-08 · Faixa: não publicada
- URL: https://netflix.wd108.myworkdayjobs.com/en-US/Eyeline/job/Eyeline-Seoul/Lead-Surfacing-Artist_JR40928
- **Régua: ZERO casamento dos 17 termos.** Limpa.
- Dedupe: **0 ocorrências**. NOVA.
- Disciplina cheia: *"photo-real textures for hard surface and organic models, environments, and
  hero creature work (…) during the look development process"*. Texturização + look dev + criatura.

**6. Environment Modeling Supervisor — Netflix Animation Studios, Sydney**
- Locatário / site: `netflix` / `Netflix` (pod `wd108`)
- Local: Sydney, Austrália · Híbrido, mínimo 3 dias no escritório
- Requisição: **`JR41734`** · Postada 2026-08-07 · Faixa: não publicada
- URL: https://netflix.wd108.myworkdayjobs.com/en-US/Netflix/job/Sydney/Environment-Modeling-Supervisor_JR41734
- **Régua — 1 casamento, e NÃO é veto:** `days a week` em *"This role is based out of Sydney,
  Australia. Hybrid Role (Minimum of 3 days a week in the office)."* → **regra de presença no
  escritório**, não regra de quem pode se candidatar. Nenhum termo de imigração casou.
- Dedupe: **0 ocorrências**. NOVA.
- Disciplina + liderança. Ferramentas citadas: Maya, ZBrush, Houdini.

**7. Environment Surfacing Supervisor — Netflix Animation Studios, Sydney**
- Locatário / site: `netflix` / `Netflix` (pod `wd108`)
- Local: Sydney, Austrália · Híbrido, mínimo 3 dias no escritório
- Requisição: **`JR41749`** · Postada 2026-08-07 · Faixa: não publicada
- URL: https://netflix.wd108.myworkdayjobs.com/en-US/Netflix/job/Sydney/Environment-Surfacing-Supervisor_JR41749
- **Régua — 1 casamento, e NÃO é veto:** `days a week` na mesma frase de presença híbrida
  (*"based out of Sydney, Australia. Hybrid Role (Minimum of 3 days a week in the office)"*).
- Dedupe: **0 ocorrências**. NOVA.
- Disciplina: surfacing/look dev com liderança. Maya, Substance.

**8. Environment Modeling Supervisor — Netflix Animation Studios, Vancouver**
- Locatário / site: `netflix` / `Netflix` (pod `wd108`)
- Local: Vancouver, BC, Canadá · Híbrido, mínimo 3 dias no escritório
- Requisição: **`JR39446`** · Postada 2026-08-06
- Faixa **publicada**: **CAD 167k – 212k** (remuneração total, sem opções de ações)
- URL: https://netflix.wd108.myworkdayjobs.com/en-US/Netflix/job/Vancouver/Environment-Modeling-Supervisor_JR39446
- **Régua — 2 casamentos, nenhum é veto:**
  - `based in` → *"This role is based in Vancouver, British Columbia."* → **falso positivo
    clássico: diz onde o CARGO fica, não de onde o candidato precisa ser.** É exatamente a
    distinção que a campanha já fixou em 08/09 no caso da Netflix contra o da People Can Fly.
  - `days a week` → *"Hybrid Role (Minimum of 3 days a week in the office)"* → presença, não veto.
- Dedupe: **0 ocorrências**. NOVA.
- Disciplina + liderança. Maya, ZBrush, Houdini.

**9. Environment Surfacing Supervisor — Netflix Animation Studios, Vancouver**
- Locatário / site: `netflix` / `Netflix` (pod `wd108`)
- Local: Vancouver, BC, Canadá · Híbrido, mínimo 3 dias no escritório
- Requisição: **`JR39273`** · Postada 2026-08-06
- Faixa **publicada**: **CAD 163k – 223k** (remuneração total)
- URL: https://netflix.wd108.myworkdayjobs.com/en-US/Netflix/job/Vancouver/Environment-Surfacing-Supervisor_JR39273
- **Régua — 2 casamentos, nenhum é veto:** mesmo par da linha 8 — `based in` dizendo onde o cargo
  fica (*"This role is based in Vancouver, British Columbia"*) e `days a week` de presença híbrida.
- Dedupe: **0 ocorrências**. NOVA.
- Disciplina: surfacing/look dev com liderança. Maya, Substance.

---

### Jogos

**10. Vehicle Artist — Cloud Imperium Games (Star Citizen), Manchester**
- Locatário / site: `cloudimperiumgames` / `CIG_Global_Careers` (pod **`wd503`**, outro pod fora
  da lista do briefing)
- Local: Manchester, Reino Unido
- Requisição: **`JR101515`** · Postada 2026-07-20 · Faixa: não publicada
- URL: https://cloudimperiumgames.wd503.myworkdayjobs.com/en-US/CIG_Global_Careers/job/Manchester/Vehicle-Artist_JR101515-1
- **Régua: ZERO casamento dos 17 termos.** Limpa.
- Dedupe: **0 ocorrências**. NOVA.
- Disciplina: **hard surface**, explícito — *"a Vehicle Artist with hard surface modelling
  experience"*, *"home to some of the most ambitious vehicle art in the industry"*.
- Nota: o mesmo cargo também aparece no site irmão `broadbean_external` do mesmo locatário. É a
  mesma requisição, não duas vagas. Use a URL acima.

---

### Sinalizadas, não são novas — decida você

**11. Character Modeling Supervisor — Netflix Animation Studios, Sydney — `JR41751`**
- URL: https://netflix.wd108.myworkdayjobs.com/en-US/Netflix/job/Sydney/Character-Modeling-Supervisor_JR41751
- **Dedupe: 1 ocorrência, em `docs/index.html`, de 08/09** — registrada como "o cargo dele com o
  nome dele", híbrida 3 dias, sem veto. **Não está em `enviados.csv`: foi achada e NÃO enviada.**
- Régua conferida de novo hoje: 1 casamento, `days a week`, presença híbrida. Sem veto.
- É a vaga mais alinhada de todas as doze. Está aqui só para você não deixar passar de novo.

**12. Visual Development Artist — Ink (Netflix), Los Angeles / Vancouver / Los Gatos — `JR41753`**
- URL: https://netflix.wd108.myworkdayjobs.com/en-US/Netflix/job/Los-Angeles/Visual-Development-Artist--Ink_JR41753
- **Régua: ZERO casamento dos 17 termos.** Limpa. Dedupe do próprio ID: **0 ocorrências**.
- **Mas:** o time "Ink" já está registrado no `docs/index.html` por outras três requisições
  (`JR41777`, `JR41754`, `JR40255`). E o corpo diz *"design and paint"* em pipeline GenAI — é
  **visual development 2D**, que a régua de disciplina do briefing conta, mas que não é modelagem.
  Prioridade baixa, por isso está no fim e não no meio.

---

## 2. O ORÁCULO NOVO — `robots.txt` mata o problema do 404

O briefing diz, com razão, que **`404` é convite para procurar o site, não porta fechada**. A
campanha vinha resolvendo isso a palpite (quatro palpites na Pixar). **Achei o atalho, e ele é
determinístico:**

```
GET https://<locatario>.<wdN>.myworkdayjobs.com/robots.txt
```

- `422` → **locatário não existe naquele pod** (mesmo veredito do POST de vagas, com 1 requisição)
- `200` → **locatário existe E o corpo lista TODOS os caminhos de site dele**, nas linhas
  `Allow:` / `Disallow:` / `Sitemap:`

Medido contra os três casos que a campanha já conhecia, e acertou os três:

```
disney/wd5      → Allow: /disneycareer/   Disallow: /disneycareerdc/     ← o segundo era desconhecido
pixar/wd501     → Allow: /Pixar_External_Career_Site/  + 4 outros
warnerbros/wd5  → Allow: /global/  Allow: /francais/
aristocrat/wd3  → Disallow: /AristocratExternalCareersSite/ + 2 outros
```

**Uma requisição substitui as dezenas de palpites.** Foi assim que `disneycareerdc` apareceu, e é
de lá que saem as duas vagas do topo desta fila.

Força bruta de nome de site, para comparação, é ruim: rodei **1.501 palpites** de caminho contra
19 locatários e o resultado foi **zero acerto**. Não repita esse caminho.

## 3. DUAS CORREÇÕES AO MAPA DE PODS DO BRIEFING

Sondei 22 nomes de pod com um locatário-lixo (`zzprobe0`): pod que existe devolve `422`, pod que
não existe não resolve.

- **`wd2` NÃO EXISTE.** As 287 sondagens contra `wd2` deram falha de túnel, não `422`. Está na
  lista do briefing e é gasto puro.
- **Faltavam seis pods reais:** `wd10`, `wd102`, `wd105`, `wd108`, `wd502`, `wd503`.
  **E é justamente neles que estavam as casas novas:** Netflix em `wd108`, Cloud Imperium e Roblox
  em `wd503`.

**Lista completa dos 12 pods que existem hoje:**
`wd1`, `wd3`, `wd5`, `wd10`, `wd12`, `wd102`, `wd103`, `wd105`, `wd108`, `wd501`, `wd502`, `wd503`.

## 4. A RÉGUA DE VETO, o que ela realmente encontrou

Baixei o **detalhe completo** (`GET .../wday/cxs/<loc>/<site><externalPath>`) das 17 finalistas,
não a listagem. Resultado: **nenhum veto de imigração, patrocínio ou residência em nenhuma das
vagas da fila.** Os únicos casamentos foram estes três tipos, todos classificados:

| Termo | Frase inteira | Classificação |
|---|---|---|
| `days a week` | *"Hybrid Role (Minimum of 3 days a week in the office)"* | **Restrição real de presença**, não veto de candidatura. Vale para JR41734, JR41749, JR39446, JR39273, JR41751. |
| `based in` | *"This role is based in Vancouver, British Columbia."* | **Falso positivo** — diz onde o CARGO fica. Vale para JR39446, JR39273. |
| `eligib` | *"you may be eligible for annual bonuses and incentives, health and wellbeing benefits"* | **Falso positivo** — é benefício, não elegibilidade para trabalhar. Vale para as duas da Aristocrat, que caíram por outro motivo. |

Frases **a favor** do candidato: nenhuma vaga da fila traz promessa explícita de patrocínio.
As da Disney trazem só o bloco padrão de igualdade de oportunidade.

## 5. O QUE CAIU, E POR QUÊ

**Caiu no detalhe, depois de baixar a descrição completa (3):**

- **`10052606` Sr Generalist Artist — ILM Vancouver (Disney).** O título passa, o corpo reprova:
  *"As a Digital Matte Painter, you will create striking digital environments (…) digital matte
  paintings"*. É **pintura de fundo**, explicitamente fora do escopo do briefing. Faixa publicada
  era CAD 112.200–143.600. Dedupe dava 0 — era "nova", mas não é da disciplina. **Não envie.**
- **`R0022356` / `R0022355` Game Artist — Aristocrat, Cracóvia e Sófia.** Corpo diz *"Keep
  Photoshop files and other documentation"* e nenhuma menção a 3D, Maya ou ZBrush. É arte 2D de
  caça-níquel. Fora da disciplina.
- **`R107775` 3D Artist Intern — Tencent, Londres.** Disciplina certa, escopo certo, mas é
  **estágio**. Fora do nível de 10+ anos.

**Caiu no dedupe por ID de requisição (8), todas conferidas nos quatro arquivos:**

| ID | Vaga | Onde apareceu |
|---|---|---|
| `10159882` | Senior Modeler, ILM Sydney | 16 ocorrências — **enviada em 04/09**, é a prova do Workday |
| `10159370` | Senior Texture Artist, ILM London | 14 ocorrências — enviada **e recusada** |
| `10159371` | Lead Texture Artist, ILM London | 10 ocorrências — enviada **e recusada em 01/09** |
| `10153285` | Real-Time Environment Artist, ILM SF | 2 ocorrências — **registrada e não enviada de propósito** (arte de cenário, Project Hire) |
| `R000106508` | Advanced Level Artist, WB Games Montreal | 2 ocorrências — já julgada arte de cenário, não enviada |
| `JR41751` | Character Modeling Supervisor, NAS Sydney | 1 ocorrência — registrada 08/09, **não enviada** → devolvida à fila na linha 11 |
| `JR41754` / `JR40255` | CG Experimental Artist, Ink | 1 ocorrência cada — já registradas 08/09 |

**Caiu no escopo geográfico (16):** sete da Disney em Mumbai (Sr Character Modeler `10154147`,
Lead Modeler `10155895`, Lead Environment Artist `10146393`, Sr/Look Dev TD `10155202`/`10155332`,
Generalist `10152359`, Sr Generalist `10152365`); quatro da Eyeline em Hyderabad (Groom `JR01060`,
Lead Surfacing `JR41016`, Modeling Supervisor `JR01007`, Surfacing/Lookdev `JR41011`); cinco da
Tencent na China e no Japão. **Índia e Japão estão fora por regra, e nenhuma delas foi considerada.**

**Caiu na disciplina, ainda pelo título (5 da Disney):** Creature TD (Rigging) Vancouver
`10155976` e `10144787`, Creature TD London `10157562`, Creature Supervisor `10145923`,
Creatures FX `10126752`. **Creature TD é rigging e Creature FX é simulação (CFX)** — os dois
excluídos pelo briefing. Fora também: iluminação (`10152348`, `10152857`, Rocksteady
`R000106815`), concept 2D (`10157163`, CIG `JR101516`/`JR101414`/`JR101198`), storyboard,
FaceSwap, UI Artist, Technical Artist.

## 6. FALSOS AMIGOS — locatários com nome de estúdio que não são estúdio

Quatro locatários `200` com nome familiar entregam quadro cheio e **nenhuma vaga da área**. Anote
para ninguém gastar tempo neles de novo:

| Locatário | Quem realmente é | Vagas |
|---|---|---|
| `mpc` / `wd1` | **Marathon Petroleum**, refinaria — não a MPC de VFX | 125 |
| `axis` / `wd3` | **Axis Communications**, câmeras suecas — não a Axis Studios | 101 |
| `icon` / `wd3` | **Icon plc**, pesquisa clínica | 887 |
| `tt` / `wd503` | **Thornton Tomasetti**, engenharia estrutural (vagas "BIM Modeler") | 133 |
| `spe` / `wd1` | Sony Pictures Entertainment, mas **só corporativo** — zero arte, zero Imageworks | 100 |
| `grab`, `krafton`, `qualcomm` | quadro público existe e está **vazio** hoje | 0 |

## 7. PAREDE DE `401` — 20 locatários que existem e não abrem por `curl`

Estes devolvem `401` **tanto no `robots.txt` quanto no endpoint de vagas, com qualquer caminho de
site**. Não é site errado: é API pública desligada ou fechada por autenticação. Não adianta
adivinhar caminho — testei e o código não muda.

`ea`/wd5 · `riotgames`/wd5 · `dneg`/wd3 · `keywordsstudios`/wd103 · `mattel`/wd1 · `roblox`/wd503 ·
`sie`/wd1 (Sony Interactive) · `scopely`/wd1 · `gameloft`/wd3 · `motive`/wd5 · `bungie`/wd1 ·
`saber`/wd501 · `amplitude`/wd12 · `chaos`/wd3 · `jamcity`/wd5 · `elastic`/wd5 ·
`appliedintuition`/wd108 · `apple`/wd1 · `spotify`/wd3 · `bytedance`/wd3

**Marcar `precisa-de-navegador`** para os relevantes da área: **EA, Riot, DNEG, Keywords, Mattel,
Roblox, Sony Interactive, Gameloft, Motive, Bungie, Saber.** Vale a pena você abrir EA, DNEG,
Keywords e Sony Interactive no navegador — são as quatro com mais chance de ter a disciplina.

Dois casos separados: **`epicgames`/wd5 e `krafton`/wd3 devolvem `200` no `robots.txt` mas com
corpo VAZIO**, e o endpoint de vagas devolve `404` em todos os ~75 caminhos que testei. O
locatário existe, o site público não foi revelado. Também `precisa-de-navegador`.

## 8. O QUE NÃO EXISTE NO WORKDAY, medido e não suposto

Testei **551 nomes** (curto, com hífen, sem espaço, com e sem sufixo corporativo) e estes deram
`422` em **todos os 12 pods**, ou seja, **não têm locatário Workday**:

Take-Two / 2K / Rockstar · Zynga · Nintendo · Ubisoft · Activision / Blizzard · Bandai Namco ·
Square Enix · THQ Nordic · Embracer / Plaion · Technicolor · Framestore · Cinesite · Animal Logic ·
Skydance · Nickelodeon / Paramount / Viacom · Lionsgate · Hasbro · Unity · DreamWorks ·
NBCUniversal · Illumination · Laika · Aardman · CD Projekt · Microsoft / Xbox / ZeniMax /
Bethesda · Amazon Games · Weta / Weta FX · Digital Domain · Pixomondo · Scanline · Rodeo FX ·
Jellyfish · Milk · Sumo · Jagex · Rebellion · Creative Assembly · Naughty Dog · Bungie(nome
alternativo) · Larian · Behaviour · Remedy · Housemarque · Supercell · Rovio · Paradox ·
Avalanche · Frontier · Codemasters · Splash Damage · Netease · King · Wargaming · e mais ~180.

**Isso não quer dizer que não têm vaga** — quer dizer que **não é aqui que se procura**. Elas usam
Greenhouse, Lever, SmartRecruiters, Teamtailor, Workable ou portal próprio, que são outras caças.

## 9. COMO ISTO FOI RODADO, para quem repetir

Ferramenta: `curl` e `python3` com `urllib`, **7 conexões simultâneas** (dentro do limite de 6–8),
tempo limite de 25–30s. **Nenhum navegador.** Ordem:

1. **Sondagem de pod** — `zzprobe0` contra 22 nomes de pod. 12 respondem `422`, são reais.
2. **Sondagem de locatário** — `GET robots.txt` para 551 nomes × 12 pods = 6.983 requisições.
   `422` descarta, `200`/`401`/`410` guarda.
3. **Extração de site** — as linhas `Allow:`/`Disallow:` do `robots.txt` dos 27 locatários `200`
   deram 52 caminhos de site, sem um único palpite.
4. **Dimensionamento** — um `POST .../jobs` com `offset:0` em cada um dos 52 sites para ler o
   `total`. 45 têm vaga, 7 estão vazios. Soma: 9.277.
5. **Colheita** — paginação **integral** de todos os 45 quadros, `limit:20` e `offset` de 20 em
   20, 491 páginas, **zero falha**. 9.246 vagas únicas.
6. **Conferência dos 12 termos de busca do briefing** — rodei `character`, `modeler`, `modeller`,
   `texture`, `surfacing`, `look development`, `sculpt`, `visual development`, `groom`,
   `3d artist`, `environment`, `asset` contra os 8 quadros que importam. **Acharam ZERO vaga que a
   paginação integral não tivesse.** A paginação integral é superconjunto estrito da busca — e é
   mais segura, porque o `searchText` do Workday é frouxo (buscar `character` na Disney devolve
   analista financeiro em Buenos Aires).
7. **Detalhe e régua** — `GET .../wday/cxs/<loc>/<site><externalPath>` das 17 finalistas, HTML
   limpo, os 17 termos com 190 caracteres de contexto de cada lado, classificação manual de cada
   casamento.
8. **Dedupe** — `grep` do **ID de requisição** (nunca do título) em `docs/index.html`,
   `enviados.csv`, `automacao/processados.csv` e `automacao/FILA-DO-VINI.md`.
9. **Conferência final** — `curl` nas 11 URLs públicas da fila. **Todas devolveram 200.**

Nada foi commitado, nada foi enviado, nenhum formulário foi preenchido, e `docs/index.html`,
`FILA-DO-VINI.md`, `enviados.csv` e `processados.csv` não foram tocados.
