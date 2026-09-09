# Caça ao Workday — LOTE 2 — 09/09/2026

Segunda varredura do Workday, feita depois de ler `automacao/caca-workday.md` (lote 1) e usando o
mesmo oráculo do `robots.txt`. Tudo abaixo foi **rodado com `curl`/`python3` nesta sessão**, no
máximo 5 conexões simultâneas, **nenhum navegador aberto**. Nada foi commitado, nada foi enviado,
nenhum formulário foi preenchido, e `docs/index.html`, `enviados.csv`, `automacao/processados.csv`
e `automacao/FILA-DO-VINI.md` **não foram tocados**.

---

## PLACAR, antes de qualquer narrativa

| Medida | Número |
|---|---|
| Nomes de pod sondados (`wd1`–`wd20`, `wd100`–`wd112`, `wd500`–`wd510`) | **43** |
| Pods que **existem de verdade** | **15** |
| — destes, **pods que o lote 1 não conhecia** | **3** (`wd107`, `wd109`, `wd504`) |
| Slugs de locatário únicos testados | **2.365** |
| Requisições de sondagem de locatário (`robots.txt`) | **17.808** |
| **`422`** (locatário NÃO existe naquele pod) | **17.743** |
| **Locatários que EXISTEM** | **65** |
| — `200`, `robots.txt` revela os sites | **34** |
| — `401`, API pública fechada | **30** |
| — `410`, locatário aposentado (`comcast`) | **1** |
| **Locatários `200` que o lote 1 NÃO conhecia** | **18** |
| **Locatários `401` que o lote 1 NÃO conhecia** | **10** |
| Sites descobertos pelo `robots.txt` nos locatários novos | **31** |
| Quadros novos paginados 100% | **24** |
| **Vagas colhidas em quadros NOVOS** | **5.329** |
| Vagas colhidas em reauditoria de quadros conhecidos (Tencent, Aristocrat, Pixar, Sony) | **738** |
| **Total de vagas lidas nesta sessão** | **6.067** |
| Bateram no filtro de título da disciplina | **74** |
| **Vagas realmente DA DISCIPLINA** (após ler título e corpo) | **0** |
| Sobreviveram ao **escopo** | **0** |
| Sobreviveram à **régua de veto** | **0** |
| Sobreviveram ao **dedupe por ID de requisição** | **0** |
| **FILA NOVA PRONTA PARA CLICAR** | **0** |
| Fila do lote 1 **ainda aberta, reconferida hoje e ainda inédita** | **8** |

**Seja honesto com o número: esta caça rendeu ZERO vaga nova.** Dezoito locatários Workday
inéditos entraram no mapa, três pods novos entraram no mapa, e **nenhum deles tem uma única vaga
de modelagem, texturização, look dev, escultura, grooming ou arte de personagem/ambiente dentro do
escopo geográfico.** O que existe de clicável hoje no Workday continua sendo o que o lote 1 já
tinha achado — e oito daquelas vagas seguem abertas e nunca foram enviadas. Elas estão na §2.

---

## 1. FILA NOVA: VAZIA

Não há fila nova. Não inventei nenhuma. As 74 vagas que bateram no filtro de título estão
dissecadas na §5, e **todas caem por disciplina ou por escopo, nenhuma por régua de veto** —
a régua nem chegou a ser exercida sobre uma candidata viável, porque não sobrou nenhuma.

---

## 2. O QUE ESTÁ CLICÁVEL HOJE — a fila do lote 1 que ninguém consumiu

Isto **não é descoberta minha** e está marcado como tal. Mas é o achado mais acionável da sessão,
então vai no topo: das doze linhas do lote 1, **quatro foram enviadas na madrugada**
(`10137201`, `JR40923`, `JR41751`, `JR101515` — todas com 1 ocorrência em `enviados.csv`) e
**oito nunca foram**. Reconferi as oito hoje, uma por uma:

- **detalhe `GET .../wday/cxs/<loc>/<site><externalPath>` → HTTP 200** nas oito;
- **página pública `https://<host>/en-US/<site>/job/<jobpath>` → HTTP 200** nas oito;
- **régua de veto rodada de novo sobre o texto integral de hoje**, casamento por casamento;
- **dedupe por ID de requisição refeito nos quatro arquivos** — as quatro contagens estão abaixo.

Ordenadas por proximidade do centro do portfólio dele: personagem/criatura primeiro, depois
ambiente, depois generalista, e o 2D por último.

### 2.1 — Modelagem com personagem e criatura dentro

**1. Modeling Supervisor — Eyeline Studios, Seul**
- host: `netflix.wd108.myworkdayjobs.com` · site: `Eyeline`
- jobpath: `Eyeline-Seoul/Modeling-Supervisor_JR40941`
- Requisição: **`JR40941`** · Seul, **Coreia do Sul** (dentro do escopo asiático permitido)
- Formato: presencial · Postada 2026-06-08 · Faixa: **não publicada**
- **Régua, resultado literal: 0 casamentos dos 16 termos.** Nenhuma frase de autorização,
  patrocínio, residência, realocação ou presença. Limpa.
- **Dedupe `JR40941`:** `docs/index.html` **0** · `enviados.csv` **0** ·
  `automacao/processados.csv` **0** · `automacao/FILA-DO-VINI.md` **0**. **INÉDITA.**
- Disciplina: modelagem 3D com liderança — qualidade artística e técnica de todos os modelos,
  fluxos de trabalho, gestão e formação do time de modelagem. Maya, ZBrush.

**2. Lead Surfacing Artist — Eyeline Studios, Seul**
- host: `netflix.wd108.myworkdayjobs.com` · site: `Eyeline`
- jobpath: `Eyeline-Seoul/Lead-Surfacing-Artist_JR40928`
- Requisição: **`JR40928`** · Seul, Coreia do Sul
- Formato: presencial · Postada 2026-06-08 · Faixa: **não publicada**
- **Régua: 0 casamentos.** Limpa.
- **Dedupe `JR40928`:** index **0** · enviados **0** · processados **0** · fila **0**. **INÉDITA.**
- Disciplina: texturização + look development, com **trabalho de criatura hero** explícito no
  corpo, hard surface e orgânico.

### 2.2 — Ambiente, com liderança

**3. Environment Modeling Supervisor — Netflix Animation Studios, Sydney**
- host: `netflix.wd108.myworkdayjobs.com` · site: `Netflix`
- jobpath: `Sydney/Environment-Modeling-Supervisor_JR41734`
- Requisição: **`JR41734`** · Sydney, Austrália · Postada 2026-08-07 · Faixa: não publicada
- Formato: **híbrido, mínimo 3 dias no escritório**
- **Régua: 1 casamento, e NÃO é veto.** Frase inteira:
  *"This role is based out of Sydney, Australia. Hybrid Role (Minimum of 3 days a week in the
  office)."* → o termo `days a week` é **regra de presença no escritório**, não regra de quem pode
  se candidatar. Nenhum termo de imigração casou.
- **Dedupe `JR41734`:** index **0** · enviados **0** · processados **0** · fila **0**. **INÉDITA.**

**4. Environment Modeling Supervisor — Netflix Animation Studios, Vancouver**
- host: `netflix.wd108.myworkdayjobs.com` · site: `Netflix`
- jobpath: `Vancouver/Environment-Modeling-Supervisor_JR39446`
- Requisição: **`JR39446`** · Vancouver, BC, Canadá · Postada 2026-08-06
- Formato: híbrido, mínimo 3 dias no escritório
- Faixa **publicada**: *"The overall market range for this role is typically **$167k – 212k CAD**.
  This reflects total compensation; we do not have stock options."*
- **Régua: 2 casamentos, nenhum é veto.** Frases inteiras:
  - `based in` → *"This role is based in Vancouver, British Columbia."* → **falso positivo já
    catalogado pela campanha: diz onde o CARGO fica, não de onde o candidato precisa ser.**
  - `days a week` → *"Hybrid Role (Minimum of 3 days a week in the office)."* → presença, não veto.
- **Dedupe `JR39446`:** index **0** · enviados **0** · processados **0** · fila **0**. **INÉDITA.**

**5. Environment Surfacing Supervisor — Netflix Animation Studios, Sydney**
- host: `netflix.wd108.myworkdayjobs.com` · site: `Netflix`
- jobpath: `Sydney/Environment-Surfacing-Supervisor_JR41749`
- Requisição: **`JR41749`** · Sydney, Austrália · Postada 2026-08-07 · Faixa: não publicada
- Formato: híbrido, mínimo 3 dias no escritório
- **Régua: 1 casamento, não é veto.** *"This role is based out of Sydney, Australia. Hybrid Role
  (Minimum of 3 days a week in the office)."* → presença.
- **Dedupe `JR41749`:** index **0** · enviados **0** · processados **0** · fila **0**. **INÉDITA.**

**6. Environment Surfacing Supervisor — Netflix Animation Studios, Vancouver**
- host: `netflix.wd108.myworkdayjobs.com` · site: `Netflix`
- jobpath: `Vancouver/Environment-Surfacing-Supervisor_JR39273`
- Requisição: **`JR39273`** · Vancouver, BC, Canadá · Postada 2026-08-06
- Formato: híbrido, mínimo 3 dias no escritório
- Faixa **publicada**: *"The overall market range for this role is typically **$163k – 223k CAD**.
  This reflects total compensation; we do not have stock options."*
- **Régua: 2 casamentos, nenhum é veto.** *"This role is based in Vancouver, British Columbia."*
  (`based in`, onde o cargo fica) e *"Hybrid Role (Minimum of 3 days a week in the office)."*
  (`days a week`, presença).
- **Dedupe `JR39273`:** index **0** · enviados **0** · processados **0** · fila **0**. **INÉDITA.**

### 2.3 — Generalista

**7. Lead Generalist Artist — ILM Vancouver (Disney)**
- host: `disney.wd5.myworkdayjobs.com` · site: `disneycareerdc`
- jobpath: `Vancouver-BC-Canada/Lead-Generalist-Artist_10142674`
- Requisição: **`10142674`** · Vancouver, BC, Canadá · Postada 2026-06-11 · Full time
- Faixa **publicada**: **C$126.800 – C$162.300**
- **Régua: 0 casamentos dos 16 termos.** Limpa.
- **Dedupe `10142674`:** index **0** · enviados **0** · processados **0** · fila **0**. **INÉDITA.**
- Ressalva honesta mantida do lote 1: a categoria interna é `Matte - Studios` e parte do trabalho é
  Digital Matte Painting, que é pintura. É liderança de arte 3D de ambiente, não de personagem.

### 2.4 — Fora do centro, decida você

**8. Visual Development Artist — Ink (Netflix), Los Angeles / Vancouver / Los Gatos**
- host: `netflix.wd108.myworkdayjobs.com` · site: `Netflix`
- jobpath: `Los-Angeles/Visual-Development-Artist--Ink_JR41753`
- Requisição: **`JR41753`** · Postada 2026-07-22 · Faixa: não publicada
- **Régua: 0 casamentos.** Limpa.
- **Dedupe `JR41753`:** index **0** · enviados **0** · processados **0** · fila **0**. **INÉDITA.**
- **Mas é visual development 2D** (*"design and paint"*, pipeline GenAI) e o time Ink já está no
  painel por outras três requisições. Prioridade baixa, por isso é a última.

---

## 3. O MAPA DE PODS, corrigido de novo

Sondei **43 nomes de pod** com um locatário-lixo (`zzprobe0`). Pod que existe devolve `422`; pod
que não existe não resolve (o proxy corta a conexão e o `http_code` volta `000`).

**Os 15 pods que existem hoje:**
`wd1` · `wd3` · `wd5` · `wd10` · `wd12` · `wd102` · `wd103` · `wd105` · **`wd107`** · `wd108` ·
**`wd109`** · `wd501` · `wd502` · `wd503` · **`wd504`**

- **Três pods novos, que nem o lote 1 tinha:** `wd107`, `wd109`, `wd504`. O lote 1 parou em 12.
- **Confirmado que `wd2` não existe** — o lote 1 já tinha dito isso, e continua verdade.
- **`wd101` e `wd505`, que estão na lista do briefing, também NÃO existem.** São gasto puro, como
  o `wd2`. A lista do briefing tem três nomes mortos e faltam-lhe cinco vivos.
- Honestidade sobre o rendimento dos pods novos: testei os 2.365 slugs contra os três e o resultado
  foi **um único locatário, `carbon`/`wd504`, cujo quadro `carboncareers` está VAZIO (total 0)**.
  Os pods novos existem, mas hoje não escondem nada da área.

---

## 4. OS 18 LOCATÁRIOS NOVOS — o que cada um é e o que entregou

Todos com `robots.txt` `200`, sites extraídos das linhas `Allow:`/`Disallow:` **sem um único
palpite**, e quadro paginado 100%.

| Locatário / pod | Sites revelados pelo robots.txt | Quem é de verdade | Vagas | Da disciplina |
|---|---|---|---|---|
| **`sega`/wd3** | `SEGA_Careers` | **SEGA Europe** (Sports Interactive, Creative Assembly, Horsham/Londres/Sofia) | 29 | **0** |
| **`unitytech`/wd1** | `Unity` | **Unity Technologies** | 121 | **0** |
| **`gearbox`/wd1** | `GEC` | **Gearbox Entertainment**, Frisco TX | 4 | **0** |
| **`spinmaster`/wd3** | `SpinMaster_Careers`, `TocaBoca_Careers`, `SAGOMINI_Careers` | Spin Master + **Toca Boca** + **Sago Mini** | 54 | **0** |
| **`lego`/wd103** | `LEGO_External` (+`LEGO_Executive` privado) | The LEGO Group | 424 | **0** |
| **`nvidia`/wd5** | `NVIDIAExternalCareerSite` | NVIDIA | 2.000+ | **0** |
| **`cae`/wd3** | `career`, `CaeCareer2`, `cae` | CAE, simulação de voo | 338 | **0** |
| **`fox`/wd1** | `Domestic`, `FOXTVST_EAST`, `FOXTVST_Central`, `FOXTVST_WEST` | Fox Corporation | 418 | **0** |
| **`starz`/wd5** | `Starz` | Starz (Lionsgate) | 20 | **0** |
| **`adobe`/wd5** | `external_experienced` | Adobe | 704 | **0** |
| **`autodesk`/wd1** | `Ext`, `uni` | Autodesk | 430 | **0** |
| **`intel`/wd1** | `External` | Intel | 589 | **0** |
| **`qualcomm`/wd12** | `External` | Qualcomm | 0 (vazio) | **0** |
| **`draftkings`/wd1** | `DraftKings` | DraftKings | 90 | **0** |
| **`carbon`/wd504** | `carboncareers` | — | 0 (vazio) | **0** |
| **`deluxe`/wd5** | `USA_CAN`, `AUS`, `External_Colleges_Universities` | **falso amigo** (ver §6) | 78 | **0** |
| **`sds`/wd3** | `Samsung_Careers`, `Samsung_Careers_SDSE` | **falso amigo** (ver §6) | 26 | **0** |
| **`ci`/wd3**, **`tti`/wd1** | financeiro / ferramentas elétricas | **falsos amigos** (ver §6) | 80 / — | **0** |

**Dez locatários `401` novos**, que existem e não abrem por `curl` — mesmo comportamento da parede
já documentada no lote 1 (`401` no `robots.txt` **e** no endpoint de vagas, com qualquer caminho):

`discord`/wd503 · `twitch`/wd12 · `roku`/wd5 · `kindredgroup`/wd3 · `tripledotstudios`/wd3 ·
`softserve`/wd3 · `mercury`/wd503 · `sandiego`/wd1 · `sgs`/wd3 · `aurora`/wd108

Destes, **os únicos que valem `precisa-de-navegador` para a disciplina são `discord`, `twitch` e
`tripledotstudios`** — e os três são casas de produto/mobile, não de arte 3D hero. Prioridade
baixa, bem abaixo dos quatro que o lote 1 já marcou (EA, DNEG, Keywords, Sony Interactive).

---

## 5. AS 74 QUE BATERAM NO TÍTULO, E POR QUE TODAS CAÍRAM

Nenhuma chegou à régua de veto: todas morreram antes, na disciplina ou no escopo. Digo o motivo de
cada bloco, como o briefing manda.

**Caíram por DISCIPLINA — "modeling"/"characterization" que é engenharia de silício, não 3D (39).**
NVIDIA e Intel juntas produzem 39 casamentos do filtro e **nenhum é arte**: *Semiconductor Device
Modeling Engineer*, *Cell Modeling and Verification Engineer*, *SoC Modelling Architect*,
*Post-Silicon Characterization Engineer*, *Architecture Energy Modeling Engineer*, *Spice Modeling
Engineer*, *Simulation and Modeling Lead*. É **engenharia pura**, excluída pelo briefing. A palavra
"characterization" em fabricante de chip significa caracterização elétrica de célula, não
personagem — é a maior fábrica de falso positivo de título que encontrei.

**Caíram por DISCIPLINA — "generalist" e "environment" que são RH e sustentabilidade (5).**
*HR Generalist* (NVIDIA, Starz), *ERC Generalist* (Adobe), *Senior Finance Manager – Environmental
Sustainability* (LEGO), *Environment and Climate Change Analyst* (CAE), *Environmental, Health and
Safety Engineer* (Intel), *Sr. Manager – Health, Safety & Environment* (Aristocrat).

**Caíram por DISCIPLINA — arte que não é a dele (7).**
- `R50031243` **Real-Time Graphics Artist, Fox News, Nova York.** Corpo: *"proficient with the
  **Vizrt** platform (…) create Vizrt transition logic show packages and the corresponding
  templates (…) These templates require scripting"*. É **grafismo de broadcast em tempo real**,
  fora por dois motivos do briefing: VFX em tempo real e não-modelagem. Escopo e nível estavam OK.
- `R50033285` / `R50033284` **Daily Artist / Freelance Daily Artist, Fox, NY** — arte diária de
  broadcast 2D. `R50024152` **Freelance Makeup Artist and Hairstylist** — maquiagem.
- `JOBREQ-2615809` **Senior Technical Artist, Unity, Remoto BC/Ontário/Montreal.** Escopo perfeito,
  senioridade perfeita, e **cai por disciplina**: o corpo é do time *Unity AI Authoring* —
  *"concevoir et développer des flux de travail, des Pipelines et des outils"*, *"expérience avec
  des jeux de données pour LLM et le benchmarking"*. É **arte técnica / ferramentaria de pipeline**,
  não modelagem, texturização nem look dev. Foi a que mais chegou perto e não passa.
- `R4977` **Senior Art Director (Contract), Spin Master, Nova York** — direção de arte de embalagem
  e marca de brinquedo, sem 3D no corpo. `R0019208` **UI Artist, Product Madness, Barcelona** —
  li o corpo inteiro: *"Great knowledge of Adobe Suite"*, *"Logos, Icons and Typography"*,
  *"Information Architecture and Interaction Design"*. É **UI 2D**.
- `123155` **Multimedia Production Artist, CAE, Homebush (Sydney)** — cai por disciplina
  (*"multimedia assets including artwork, illustrations, animations and video"* com Adobe CC para
  eLearning de Defesa) **e teria caído na régua de qualquer jeito**: *"Australian Citizen with the
  ability to obtain and maintain an NV1 Security Clearance"* — **exigência de cidadania, veto
  escrito**. É o único veto real que encontrei na sessão inteira.

**Caíram por ESCOPO — Índia (12).** Aristocrat concentra a arte 3D dela em Noida e Gurugram:
*Lead Animator (3D)* `R0021742`, *Lead Animator* `R0021747`/`R0021838`, *Sr Lead Animator*
`R0022395`/`R0022396`, *Sr Animator II* `R0021593`, *Sr Artist II* `R0022013`, *Sr. Lead Artist*
`R0022012`, *Sr Lead Tech Artist* `R0021864`, *Sr Lead Technical Artist* `R0022132`,
*Sr Technical Artist I/II* `R0022023`/`R0021922`. **Índia está fora por regra e nenhuma foi
considerada** — e note que a maioria também cairia por disciplina (animação e arte técnica).

**Caíram por ESCOPO — Japão e China (9).** Toda a arte de fundo da Tencent/Lightspeed está em
Tóquio e Osaka: *背景アーティスト｜Environment Artist* `R107842` e `R107441`, *Environment Artist
Intern* `R107266`, *Concept Artist* `R107982`, *Technical Artist* `R107229`, *Motion Technical
Artist* `R105686`, *Rigging Technical Artist* `R105688`. Mais *3D Character Artist* `R107901`
(**Shenzhen, China**) e *Technical Artist* `R108025` (Xangai). **Japão e China estão fora por
regra.** O `3D Character Artist` de Shenzhen é a vaga mais alinhada ao portfólio dele que apareceu
nesta sessão inteira — e o escopo a mata.

**Caíram por NÍVEL (2).** *3D Artist Intern* `R107775` (Tencent, Londres — escopo e disciplina
certos, mas é **estágio**) e *Environment Artist Intern* `R107266`.

---

## 6. FALSOS AMIGOS NOVOS — locatários com nome de estúdio que não são estúdio

Anote para ninguém gastar tempo neles de novo. Some-se aos seis que o lote 1 já catalogou
(`mpc`, `axis`, `icon`, `tt`, `spe`, `grab`).

| Locatário | Quem realmente é | Vagas |
|---|---|---|
| `deluxe`/wd5 | **Deluxe Corporation** — cheques, impressão e serviços a bancos (*Remittance Processing Specialist*, *Press Operator*). **NÃO é a Deluxe Entertainment de pós-produção.** | 78 |
| `sds`/wd3 | **Samsung SDS**, TI corporativa. Coreia está no escopo, mas isto não é estúdio. | 26 |
| `ci`/wd3 | **CI Financial / Corient**, gestão de patrimônio. **NÃO é a CI Games.** | 80 |
| `tti`/wd1 | **Techtronic Industries**, ferramentas elétricas (Milwaukee, Ryobi). | — |
| `carbon`/wd504 | quadro público existe e está **vazio** | 0 |
| `qualcomm`/wd12 | quadro público existe e está **vazio** (confirma o lote 1) | 0 |
| `mercury`/wd503 | `401`; é Mercury Systems (defesa), **não a Mercury Filmworks** de animação | — |
| `sandiego`/wd1 | `401`; município/condado, **não o San Diego Studio da Sony** | — |
| `aurora`/wd108 | `401`; Aurora Innovation (veículos autônomos), **não estúdio** | — |
| `sgs`/wd3 | `401`; SGS, inspeção e certificação | — |

---

## 7. ARMADILHAS DE MÉTODO QUE EU MEDI NESTA SESSÃO

Sete, todas medidas, não supostas. As quatro primeiras são novas; as três últimas confirmam o
lote 1 com evidência fresca.

**1. `curl -w` come o formato se ele começa com `@`.**
Perdi duas rodadas inteiras com isto. `-w '@@ %{http_code} %{url_effective}\n'` faz o `curl`
interpretar o `@@` como **"leia o formato deste ARQUIVO"** e morrer com
`curl: option -w: error encountered when reading a file`, código 26 — e, em execução paralela, o
sintoma é pior: o lote inteiro devolve zero linha e o log parece só "rápido demais". **Nunca comece
o `-w` com `@`.** Usei `RSLT %{http_code} %{url_effective}\n` e funcionou de primeira.

**2. `-o /dev/null` na linha de comando NÃO cala o corpo quando as URLs vêm de `-K` com
`--parallel`.** O corpo do `robots.txt` vaza para o `stdout` e se cola no início da linha do `-w`,
produzindo lixo como `{"errorCode":"HTTP_422",...}422 https://...`. A correção medida é escrever
**um par `url =` + `output =` por URL dentro do próprio arquivo de config**, e ainda assim
**parsear o `stdout` com expressão regular ancorada num marcador**, nunca por posição de campo.

**3. `pkill -f <padrão>` mata o próprio shell que o executa.**
`pkill -f sweep.py` casou com a linha de comando do meu próprio `bash -c`, que continha o texto
`sweep.py`, e derrubou a sessão com código 144 antes de a varredura reiniciar. Para matar um filho,
use `ps -eo pid,args | grep "[s]weep.py" | awk '{print $1}' | xargs -r kill` — com o colchete que
impede o padrão de casar consigo mesmo.

**4. Resultado de busca web sobre Workday é ESTRUTURALMENTE VELHO — verifique todo host antes de
acreditar.** A busca me entregou, com aparência perfeita,
`activision.wd1.myworkdayjobs.com/Blizzard_External_Careers` (Senior 3D Character Artist, Barcelona)
e `netflix.wd1.myworkdayjobs.com/Netflix` (Lead Character Artist 3D, Internal Game Studio). As duas
seriam achados enormes. **Testei as duas: `activision.wd1` → `422`, `netflix.wd1` → `422`.** A
Netflix migrou para `wd108` e a Activision saiu do Workday; os índices de busca guardam a URL
antiga por anos. Mesma coisa com `cae.wd3/career/job/Synthetic-Environment-Artist_110559`, que a
busca mostrou e cuja procura direta no quadro hoje devolve **`total 0`**. **Regra: nenhum host vindo
de busca entra no mapa sem passar pelo oráculo do `robots.txt` na mesma sessão.**

**5. Não existe atalho sem pod. Medido.** Testei `https://<locatario>.myworkdayjobs.com/robots.txt`,
`https://wd5.myworkdayjobs.com/<locatario>/robots.txt` e `https://<locatario>.myworkdaysite.com/` —
os três são recusados pelo proxy (`connect_rejected`), não resolvem. E
`https://www.myworkday.com/<locatario>/login.htmld` **não serve como oráculo**: redireciona para
`community.workday.com/invalid-url` com **exatamente os mesmos 25.801 bytes** para
`netflix`, `disney`, `pixar` e para `qqnotarealtenantxyz`. **Não distingue locatário real de
inventado.** O custo de sondagem é irredutivelmente `nº de slugs × nº de pods`.

**6. `searchText` do Workday é frouxo a ponto de ser inútil, agora com número.** Rodei 13 termos
contra os quadros novos. Buscar `character artist` na Adobe devolve *Enterprise Account Executive
Retail/Public* em Zurique, *Senior Deal Desk Analyst – German speaker* em Dublin e *Manager,
Accounting*. Buscar `look development` devolve *Business Development Representative*. **A paginação
integral é superconjunto estrito da busca e é a única leitura confiável** — exatamente o que o lote
1 concluiu, agora reconfirmado num conjunto de quadros diferente.

**7. `total` mente em quadro grande: a NVIDIA devolve `"total":2000` e ainda assim entrega vagas em
`offset:2000`.** O campo é um teto de exibição, não a contagem real. Quem parar a paginação quando
`offset >= total` **para cedo** num quadro desses. Contornei conferindo `offset:2000` explicitamente
e, para a disciplina, cruzando com busca por termo — mas registre que a colheita da NVIDIA nesta
sessão é **incompleta por baixo**, e que os 2.000 lidos não têm uma única vaga de arte 3D.

**8. Confirmada a armadilha do `/job/job/` do lote 1, e não caí nela.** O `externalPath` da listagem
**já começa com `/job/`**. A URL de detalhe correta é `https://<host>/wday/cxs/<loc>/<site>` +
`externalPath` **sem acrescentar nada**. As oito verificações da §2 usaram essa forma e deram `200`;
a página pública correspondente é `https://<host>/en-US/<site>/job/<jobpath>`, que é o formato que o
`wd_geral.js` monta na linha 213 — por isso os `jobpath` da §2 estão escritos **sem** o `/job/`
inicial, prontos para colar.

---

## 8. O QUE FOI TESTADO E NÃO EXISTE

Além dos ~551 nomes do lote 1, testei **2.365 slugs únicos** (junto e minúsculo, com hífen, sem
sufixo corporativo, sigla) — os nomes do array `STUDIOS` do painel, os de `alvos.csv`, mais uma
lista curada de 331 empresas de porte enterprise de jogos, animação, VFX, brinquedo, cassino,
parque temático e tecnologia. Deram `422` **nos 15 pods**, ou seja, **não têm locatário Workday**:

Take-Two / 2K / Rockstar · Zynga · Ubisoft · Nintendo · Bandai Namco · Square Enix · Capcom ·
Koei Tecmo · Konami · Nexon · NCSoft · Netmarble · Smilegate · Pearl Abyss · Kakao · Com2uS ·
NHN · Wemade · Devsisters · Garena / Sea / Shopee · NetEase · miHoYo / HoYoverse · Lilith ·
Moonton · Level Infinite · Framestore · Cinesite · Technicolor · The Mill · Digital Domain ·
Pixomondo · Scanline · Rodeo FX · Hybride · Mikros · Weta / Weta FX · Animal Logic · Luma ·
Blur · Jellyfish · Milk · The Third Floor · Halon · Union VFX · BlueBolt · Goodbye Kansas ·
Important Looking Pirates · DreamWorks · Illumination · Laika · Aardman · WildBrain · Thunderbird ·
Boat Rocker · Guru · Mercury Filmworks · Atomic Cartoons · Titmouse · Bento Box ·
Sony Pictures Imageworks · Paramount / NBCUniversal / Lionsgate · Hasbro · Jazwares · Funko ·
MGA · Moose · Ravensburger · Universal Creative · Merlin · SeaWorld · Cedar Fair · Six Flags ·
Virtuos · Room 8 · Testronic · PTW · Pole To Win · Lionbridge · Magic Media · Streamline ·
Kevuru · N-iX · Ciklum · GlobalLogic · EPAM · Luxoft · CD Projekt · Embracer / Plaion / THQ
Nordic · Larian · Remedy · Housemarque · Supercell · Rovio · Frontier · Codemasters ·
Splash Damage · Rebellion · Jagex · Sumo · Creative Assembly · Digital Extremes · Behaviour ·
Ludia · Eidos · Crystal Dynamics · Wargaming · Wizards of the Coast · Paradox · Avalanche ·
Fatshark · Coffee Stain · IO Interactive · Bloober · People Can Fly · Techland · 11 bit ·
Huuuge · CI Games · Nacon · Focus · Dontnod · Quantic Dream · Asobo · Sloclap · Ankama ·
Arkane · MachineGames · id Software · Bethesda / ZeniMax · Obsidian · inXile · Double Fine ·
Ninja Theory · Playground · Rare · 2K Games / Firaxis / Hangar 13 / Visual Concepts ·
Insomniac · Naughty Dog · Sucker Punch · Guerrilla · Media Molecule · Bluepoint · Haven ·
Light & Wonder · SciPlay · IGT · Everi · PlayAGS · Novomatic · Playtech · Evolution ·
Betsson · Flutter · Entain · William Hill · Ballys · Greentube · Relax · Yggdrasil ·
Pragmatic Play · NetEnt · e mais ~1.900 slugs derivados do painel e do `alvos.csv`.

**Isso não quer dizer que não têm vaga** — quer dizer que **não é aqui que se procura**. Elas usam
Greenhouse, Lever, SmartRecruiters, Teamtailor, Workable ou portal próprio, que são outras caças.

**Correção de rumo importante, e é uma lição:** o lote 1 listou **Sega** e **Unity** como
"não existem no Workday". **Existem** — como `sega`/wd3 e `unitytech`/wd1. A `sega` só aparece com
o nome curto e a `unitytech` só aparece com um sufixo que nenhuma normalização mecânica de "Unity
Technologies" produz. **O `422` prova que aquele slug não existe naquele pod, nunca que a empresa
não está no Workday.** Foi por isso que valeu a pena refazer a varredura com uma lista de nomes
curados à mão, e é por isso que os dois locatários novos mais interessantes desta sessão saíram
justamente de nomes que o lote 1 tinha dado por mortos. (Ainda assim: nem Sega nem Unity têm vaga
da disciplina hoje.)

---

## 9. COMO ISTO FOI RODADO, para quem repetir

Ferramenta: `curl` com `--parallel --parallel-max 5` e `-K` (arquivo de config), mais `python3`.
**Nenhum navegador.** Tempo limite de 15s na sondagem, 25s no detalhe. Ordem:

1. **Sondagem de pod** — `zzprobe0` contra 43 nomes. 15 respondem `422`, são reais.
2. **Sondagem de locatário** — `GET robots.txt`, 2.365 slugs × pods = **17.808 requisições**.
   `422` descarta; `200`/`401`/`410` guarda. Quatro varreduras: curada (713 slugs × 15 pods),
   painel+`alvos.csv` (1.511 × 3 pods novos), lacunas do lote 1 (31 × 15) e variantes de nome
   de publicadora (141 × 15).
3. **Extração de site** — linhas `Allow:`/`Disallow:` do `robots.txt` dos 18 locatários novos →
   **31 caminhos de site, zero palpite**.
4. **Colheita** — paginação integral, `limit:20` e `offset` de 20 em 20 (o `limit:50` continua
   devolvendo `400`), de 24 quadros novos + reauditoria de Tencent, Aristocrat, Pixar e Sony.
   **6.067 vagas.**
5. **Filtro de título** → 74 candidatas → leitura do corpo → **0 da disciplina no escopo**.
6. **Reconferência da fila do lote 1** — detalhe, régua de 16 termos com 200 caracteres de contexto
   de cada lado, e URL pública das 8 ainda abertas. **Todas `200`.**
7. **Dedupe** — `grep` do **ID de requisição** (nunca do título) em `docs/index.html`,
   `enviados.csv`, `automacao/processados.csv` e `automacao/FILA-DO-VINI.md`, com as quatro
   contagens reportadas por vaga.

Nada foi commitado, nada foi enviado, nenhum formulário foi preenchido, e os quatro arquivos de
dedupe não foram tocados.
