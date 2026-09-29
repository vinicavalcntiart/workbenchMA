# PORTAS REABERTAS — teste da hipótese do ENDEREÇO ERRADO

Rodada de 08/09. Levantamento, **não candidatura**: nenhum email foi mandado, nenhum
rascunho criado, nenhum formulário preenchido nem enviado. Nenhum navegador foi aberto —
só `curl` (sempre `https://`, sempre com User-Agent de Chrome), WebSearch e WebFetch.
Nenhum arquivo compartilhado foi editado; este relatório é o único arquivo criado.

---

## 1. O NÚMERO DOS DOIS LADOS

**509 entradas examinadas. 22 portas reabertas de verdade. 2 vagas da disciplina apareceram
atrás delas — as duas na mesma casa (UFX Studios, Bruxelas).**

De onde vieram as 509:

| Fonte | Entradas marcadas como porta fechada | Quantas reabri |
|---|---|---|
| `PORTAIS` do `docs/index.html` (748 linhas) | 195 casaram com as palavras-chave; 108 sobraram depois de tirar censo e candidatura já enviada; **48 reconferidas uma a uma** | 14 |
| `automacao/garimpo-cgstudiomap.csv` (`site-fora-do-ar`) | **130, todas reconferidas** | 5 com porta de carreiras; 23 sites vivos |
| `automacao/fila-gamedevmap-canada.csv` (`site-fora-do-ar` + `bloqueado:*`) | **21 reconferidas** (3 das 24 não tinham URL utilizável) | 2 sites vivos, 0 porta de carreiras |
| `automacao/fila-gamedevmap-europa.csv` (`porta-sem-resposta`) | **310 URLs únicas, todas reconferidas** | 3 |

**A hipótese se confirma, mas em escala muito menor do que os seis casos de hoje sugeriam.**
Ela vale forte para um subgrupo específico e não vale para a maioria. O número honesto está
na seção 5.

### O que o teste mostrou sobre CADA variação do protocolo

| Variação | Resultado medido |
|---|---|
| **Caminho errado** (`/careers` vs `/jobs` vs `/join-us` vs barra final) | **A que mais rendeu: 9 das 22 reaberturas.** `/jobs/` reabriu BUF, Red Star, Sabotage, Painting Practice e 11 bit; `/join-us/` reabriu a UFX; `/recruitment/` reabriu a Peerless; `/career` (singular) reabriu a Koala FX; `/careers` **sem barra final** reabriu a Hard Light, cujo registro dizia `/careers/` 404 |
| **Domínio institucional diferente** (caso Artifex) | 2 casos: RyseUp Studios (o quadro vive no SmartRecruiters) e Radiant Worlds (virou **Rebellion Warwick** em 2018, por isso o domínio morreu) |
| **Slug de ATS com/sem sufixo** (caso Snowprint) | **1 acerto em 24 tentativas.** `funcom.teamtailor.com` responde 200 com 6 vagas. Gamecan, Blur, Gravity Well, Day 9, SuperNatural e Mino Games: todas as variações deram 404 ou quadro vazio de verdade |
| **`https://` + User-Agent de Chrome** (403 ≠ site morto) | **Grande:** 20 dos 24 registros `403` do cgstudiomap viraram 200 com conteúdo real. O `403` do registro antigo era o cliente, não o estúdio |
| **Subdomínio de carreiras** (`careers.<domínio>`) | 1 caso: `rebellion.com/jobs` → `careers.rebellion.com` |
| **Workday 404 = caminho errado, 422 = não existe** | Não teve caso novo nesta fatia; as entradas de Workday do painel já estão resolvidas |

---

## 2. AS 22 PORTAS REABERTAS, uma a uma

Formato: URL antiga → URL nova, com o código HTTP dos dois lados.

### 2.1 As que reabriram COM vaga da disciplina atrás

**UFX Studios — Bruxelas, Bélgica** *(o único achado com vaga da disciplina)*
- Registro antigo (`garimpo-cgstudiomap.csv`): `site-fora-do-ar`, `http://www.ufxstudios.com` **HTTP 403**
- Porta nova: **`https://ufxstudios.com/join-us/` → HTTP 200** (47.646 bytes)
- Duas coisas erradas somadas no registro antigo: `http://` simples e caminho `/careers`
  (que não existe ali). Com `https://` + UA de Chrome + `/join-us/`, abre inteira.
- **Atrás dela: 4 vagas.** Environment Artist (Houdini) Mid/Senior, Assistant·es de production
  VFX (estágio), VFX Compositor (Mid) e **Speculative Application**.
- Duas são de interesse — detalhadas na seção 3.
- **Dedupe conferido pela referência:** zero ocorrência de `ufxstudios` em `enviados.csv`,
  em `automacao/processados.csv` e em `automacao/pessoas.csv`. É casa nova na campanha.

### 2.2 As que reabriram com quadro VIVO, mas ZERO na disciplina

**Funcom — Oslo** *(caso Paradox: o domínio próprio mentia)*
- Registro antigo (`PORTAIS` #281): "QUADRO CONFERIDO E VAZIO em 06/09 … `jobs.funcom.com`
  e o `/jobs.json` responde **ZERO**"
- Endereço canônico do Teamtailor: **`https://funcom.teamtailor.com/jobs.json` → HTTP 200 com 6 vagas**
- Reconferido hoje, `https://jobs.funcom.com/jobs.json` **também** responde 200 com as mesmas 6
  (JSON Feed, chave `items` e não `jobs` — a armadilha de leitura que o painel já registrou na Fatshark).
- As 6: Internship 2027 — Finance / Programming / Production Assistant / Design /
  **Concept Art** / Data Analytics. **Nenhuma da disciplina** (Concept Art é 2D, expressamente fora).
- Ressalva honesta: pode ser que o quadro tenha mesmo enchido depois de 06/09, e não que o
  endereço estivesse errado. O que fica provado é que **o quadro não está vazio hoje**.

**RyseUp Studios — Lyon, França** *(caso Artifex: o quadro mora em outro domínio)*
- Registro antigo (`PORTAIS` #630): `ryseupstudios.com` devolve **erro de TLS**
  (`SSL alert internal error`) — reproduzido hoje, continua igual.
- Porta nova, achada pelo NOME e não pelo domínio: **`https://api.smartrecruiters.com/v1/companies/ryseupstudios/postings` → HTTP 200**,
  quadro público em `https://careers.smartrecruiters.com/ryseupstudios`
- **Atrás dela: 1 vaga.** *VFX artist*, Lyon (`https://jobs.smartrecruiters.com/ryseupstudios/743999710587649`).
  **Não é a disciplina** — VFX em tempo real está na lista de exclusão do briefing.
- Dedupe: zero ocorrência de `ryseup` em `enviados.csv` e `processados.csv`.

**Cause and FX — Auckland, Nova Zelândia**
- Registro antigo (`garimpo-cgstudiomap.csv`): `site-fora-do-ar`, `http://www.causeandfx.nz` **HTTP 403**
- Porta nova: **`https://causeandfx.nz/careers` → HTTP 200**, e ela aponta para o quadro real em
  `https://apply.workable.com/cause-and-fx-ltd/`
- Quadro lido pela API pública do Workable (`apply.workable.com/api/v1/widget/accounts/cause-and-fx-ltd?details=true`, HTTP 200):
  **3 vagas**, nenhuma da disciplina — *Lead FX Artist (Contract)*,
  *Senior Compositing Artist — Expression of Interest (Contract, NZ Right to Work)* e
  *Expression of Interest (NZ | AU Right to Work ONLY)*.
- **VETO ESCRITO NO PRÓPRIO TÍTULO** da candidatura espontânea: `NZ | AU Right to Work ONLY`.
  A porta reabriu e está fechada para ele por escrito. Isso encerra a casa.

**Radiant Worlds → Rebellion Warwick** *(o domínio morreu porque o estúdio mudou de nome)*
- Registro antigo (`PORTAIS` #630): `radiantworlds.com` serve certificado de outro domínio
  (altname `reb.to`) — reproduzido hoje: `SSL: no alternative certificate subject name matches`.
- Explicação achada: a Rebellion comprou a Radiant Worlds em 2018 e a renomeou **Rebellion Warwick**.
  O `reb.to` do certificado é a própria Rebellion — o certificado não estava "trocado", estava certo.
- Porta viva: `https://rebellion.com/jobs` → **redireciona 200 para `https://careers.rebellion.com/`**
  (subdomínio de carreiras, mesmo padrão da Folks VFX e da Rising Sun).
- **A lista de vagas não renderiza por `curl`** — o bloco `#vacancies` monta em JavaScript e não
  há endpoint público (`/wp-json/...`, `/api/vacancies`, `/vacancies` todos 404).
  **Marcada `precisa-de-navegador`** — ver seção 5.
- Contexto de dedupe: a campanha **já aplicou e já foi recusada** na Senior Character Artist de
  Oxford (30/08 pelo Workable, recusa em 01/09 registrada em `processados.csv`). A reabertura vale
  como correção de registro do endereço da Radiant Worlds, não como vaga nova.

### 2.3 As que reabriram com porta VIVA de candidatura espontânea (email), sem vaga listada

**BUF — Paris / Los Angeles / Montreal** *(o mais relevante deste grupo: Montreal é prioridade 1)*
- Registro antigo (`garimpo-cgstudiomap.csv`): `site-fora-do-ar`, `https://www.buf.com` **HTTP 0** (não respondeu)
- Porta nova: **`https://buf.com/jobs/` → HTTP 200**. A raiz e todos os outros caminhos continuam
  devolvendo **403** hoje; só `/jobs/` passa.
- Atrás dela: nenhuma vaga listada, e **dois endereços de candidatura publicados**:
  `jobs_paris@buf.com` e **`jobs_montreal@buf.com`**.
- **Dedupe:** `jobs_paris@buf.com` **já recebeu candidatura em 02/09** (`enviados.csv`, auto-reply
  registrado em `processados.csv`). **`jobs_montreal@buf.com` é endereço NOVO**, nunca usado pela campanha.
- Nenhum dos treze termos aparece na página. Sem vaga nomeada, é candidatura espontânea.

**11 bit studios — Varsóvia**
- Registro antigo (`PORTAIS` #49): "**PORTA MORTA**, medido em 08/09: `11bitstudios.com/careers/`
  devolve HTTP 404 … A porta mudou para `/jobs/`, mas lá o bloco CURRENT OPENINGS está VAZIO."
- Reconferido: `/careers/` **404** confirmado; **`https://11bitstudios.com/jobs/` → HTTP 200** (202.513 bytes).
- O bloco CURRENT OPENINGS **continua vazio** — o registro antigo estava certo nisso.
- **O que o registro perdeu:** a mesma página publica convite escrito à espontânea —
  *"HAVEN'T FOUND WHAT YOU'RE AFTER? LET US KNOW WHAT INTERESTS YOU. JUST SEND AN E-MAIL WITH YOUR
  APPLICATION"* — com `mailto:jobs@11bitstudios.com`. **Não é porta morta: é porta de email.**

**SuperNatural Studios — Vancouver**
- Registro antigo (`PORTAIS` #23): quadro do Greenhouse morto, "fica sem porta".
- Reconferido hoje: os tokens do Greenhouse continuam **404** (testei `supernaturalstudios` e
  `supernatural-studios`; o registro antigo já tinha testado outros dois). **O quadro está morto mesmo.**
- **O que o registro perdeu:** a raiz `https://supernaturalstudios.com/` (HTTP 200) publica
  `becurious@supernaturalstudios.com`. É porta de email, não é ausência de porta.

**HB Studios — Lunenburg, Nova Escócia (2K / Take-Two)**
- Registro antigo (`PORTAIS` #78): "**SEM-PORTA** hoje, quadro do Greenhouse VAZIO", URL `boards.greenhouse.io/hbstudios`
- Reconferido: `boards-api.greenhouse.io/v1/boards/hbstudios/jobs` → **HTTP 200 com 0 vagas** (confirmado).
  As variações `hb-studios` e `hbstudios2k` dão 404.
- Porta nova do lado do site: **`https://www.hb-studios.com/work-with-us/` → HTTP 200**, com a seção
  CURRENT OPENINGS (que aponta para o mesmo Greenhouse vazio) e **`jobs@hb-studios.com` publicado**.
- Verdadeiro estado: quadro vazio, porta de email viva. Canadá, vale manter no radar.

### 2.4 As que reabriram com a página de carreiras VIVA e vazia (fecham a dúvida)

| Estúdio | URL antiga (código) | URL nova (código) | O que existe atrás |
|---|---|---|---|
| **Sabotage Studio** (Quebec, *Sea of Stars*) | `sabotagestudio.com/careers/` — **404** | `sabotagestudio.com/jobs/` — **200** (96.948 B) | Página "We are hiring" real, e a frase literal: *"Sorry, no positions available for the moment."* Zero vagas |
| **Red Star 3D** (Sheffield, UK) | `redstar3d.com` registrado `site-fora-do-ar` (403) | `redstar3d.com/jobs/` — **200** (151.021 B) | "Current Jobs at Red Star" sem nenhum link de vaga. Zero vagas. Email `hello@redstar3D.com` — **já contatado em 03/09** (`enviados.csv`) |
| **Peerless** (Covent Garden, Londres) | `peerless.co.uk/careers/` — **404** | `peerless.co.uk/recruitment/` — **200** (29.383 B) | *"There are no positions currently available…"* + convite escrito a CV espontâneo em `jobs@peerless.co.uk`. **VETO ESCRITO, em caixa alta:** *"ALL APPLICANTS MUST HAVE THE LEGAL RIGHT TO WORK IN THE UK TO BE CONSIDERED."* |
| **Hard Light** (SEGA, Leamington Spa) | `hardlightstudio.com/careers/` **com barra** — 404 | `hardlightstudio.com/careers` **sem barra** — **200** (16.839 B) | Página "Become part of the SEGA family". Seção "Available Positions" vazia, e a navegação marca `Careers 0`. Zero vagas |
| **Koala FX** (Reino Unido) | `koalafx.co.uk/careers/` — 404 | `koalafx.co.uk/career` (singular) — **200** (19.469 B) | 3 vagas: VFX Coordinator, Project Manager, Lead Compositor. **Nenhuma da disciplina.** Convite espontâneo `hr@koalafx.co.uk` — o registro antigo já tinha isso pela raiz |
| **Cutting Corner Games** (Europa, fila gamedevmap) | registrado `porta-sem-resposta` | `cuttingcornergames.com/careers/` — **200** (136.809 B) | *"No open positions at the moment"* + convite escrito: *"if you don't find the right role, send us an open application!"*. Zero vagas |
| **Mino Games** (Montreal) | `PORTAIS` #23: quadro do Teamtailor morreu | `minogames.com/careers` — **200** (177.523 B) | Página de carreiras viva. Os tokens `minogames` e `mino-games` do Greenhouse continuam **404** |
| **Painting Practice** (Cardiff) | `paintingpractice.com/careers/` — 404, "SEM PORTA DE CANDIDATURA" | `paintingpractice.com/jobs/` — **200** (175.863 B) | Página "Jobs — Come work with us" listando Houdini Artists, Developer e Environment Artist — **mas o texto das três é *lorem ipsum*** (*"Stet erat, sed diam voluptua…"*). É gabarito do tema, não vaga real. Registrado como porta viva com conteúdo de demonstração |
| **Funrock** (Suécia) | registrado `porta-sem-resposta` | `funrock.com/jobs/` — **200** (45.096 B) | Página existe; o host caiu por `ws_closed_mid_exchange` do proxy em quatro tentativas de leitura do corpo. Conteúdo **não lido** — não afirmo nada sobre as vagas |

### 2.5 Sites institucionais que voltaram a responder (o registro dizia fora do ar)

Estes **não** são portas de carreiras — são o registro `site-fora-do-ar` desmentido. Todos com
`https://` + UA de Chrome, todos com corpo de tamanho real. Testei os caminhos de carreiras em
todos: **nenhum tem página de vagas**, e por isso não contam como porta reaberta.

`Studio Rakete` (DE, 200/44.808 B) · `Greebl Studio` (200/253.807 B) · `Novelab` (200/156.548 B) ·
`Pôle Nord Studio` (200/20.169 B) · `Viewmakers` (200/120.600 B) · `Akama Film Director` (200/38.453 B) ·
`Armada Content Company` (200/57.011 B) · `Cadence Capture` (200/57.316 B) · `Kawanimation` (200/21.788 B) ·
`Le Big Shot` (200/1.562.437 B) · `Le Labo Blanc` (200/125.499 B) · `Protozoaire` (200/38.486 B) ·
`SAS TRIBIA` (200/36.148 B) · `Toonkit Studio` (200/82.567 B) · `Angels & Demons` (200/67.269 B)
— e do Canadá: `Magic Leap` (200/80.542 B, era `bloqueado:500`) e `Infinite Ammo` (200/56.723 B, era `site-fora-do-ar`).

Da Europa, 18 dos 310 `porta-sem-resposta` voltaram 200 com conteúdo real: `razzleberri.es`,
`cuttingcornergames.com`, `studiofirlefanz.com`, `tableflip.nu`, `isitlove.com`, `transcenders.eu`,
`funrock.com`, `rangatang.nl`, `gamelabuk.com`, `hexfoundry.se`, `greyaliengames.com`,
`neckboltgames.com`, `northernergames.com`, `studionachtwerk.com`, `moonmode.com`,
`golfstorygame.com` (→ `sidebargames.com`), `timelessgames` (wixsite) e `MicrowaveGames` (só Facebook).
Destas, só duas tinham página de carreiras (Cutting Corner e Funrock, já listadas acima).

---

## 3. AS VAGAS DA DISCIPLINA ACHADAS ATRÁS DAS PORTAS REABERTAS

**Duas, as duas na UFX Studios.** Nenhuma outra porta reaberta tinha vaga da disciplina.

### 3.1 UFX Studios — Environment Artist (Houdini) Mid/Senior

- **Link direto:** `https://ufxstudios.com/job/environment-artist-houdini-mid-senior/` (HTTP 200)
- **ATS:** nenhum. Formulário próprio na página + candidatura por email.
- **Formato:** Bruxelas, Bélgica. Contrato **Freelance**, disponibilidade "as soon as possible".
- **Encaixe:** é **AMBIENTE**, que pelo briefing é **MÉDIA**, não alta. O peso do anúncio está em
  Houdini procedural (SOP, scattering, instancing, terreno) e não em modelagem/textura de personagem.
  Pede portfólio fotorrealista de ambiente. Registro honesto: encaixa na regra de ambiente = média,
  mas o núcleo técnico é Houdini, que não é a ferramenta dele.
- **Endereço de candidatura publicado no anúncio:** `hiring@ufxstudios.com`
- **BUSCA LITERAL DOS TREZE TERMOS no texto integral (4.965 caracteres):**
  `authoriz` — **não aparece** · `eligib` — **não aparece** · `sponsor` — **não aparece** ·
  `work permit` — **não aparece** · `must be based` — **não aparece** · `LMIA` — **não aparece** ·
  `days a week` — **não aparece** · `days per week` — **não aparece** · `days in the office` — **não aparece** ·
  idioma local (`french`, `français`, `dutch`, `nederlands`) — **não aparece** ·
  `resident` — **não aparece** · `relocat` — **não aparece** · `located in` — **não aparece** ·
  `unable to support` — **não aparece** · `no relocation` — **não aparece**.
  **NENHUM dos treze termos aparece. Não há veto escrito.**
- **Sinal positivo:** não há. O anúncio também não oferece relocação nem patrocínio — é silêncio,
  não é oferta. Não inventei sinal onde não há.
- Não vi captcha no HTML da página; **veredito só com o clique**.

### 3.2 UFX Studios — Speculative Application

- **Link direto:** `https://ufxstudios.com/job/speculative-application/` (HTTP 200)
- **ATS:** nenhum. É **por email**, e o anúncio é explícito sobre isso.
- **Formato:** Bruxelas. Candidatura espontânea permanente.
- **Texto literal:** *"We do accept speculative applications. To apply, please send your CV
  specifying "Jobs" within the subject line at **vfx_hr@ufxstudios.com** (Candidatures sent by any
  other way or to any other e-mail wont be taken into consideration)."*
  Pede também *shot breakdown* por plano/sequência.
- **Atenção operacional:** o anúncio exige a palavra **"Jobs" no assunto** e diz por escrito que
  candidatura por qualquer outro caminho ou endereço **não será considerada**. Se a campanha usar
  o endereço errado (`hiring@`, `info@`) ou assunto livre, a candidatura é descartada na origem.
- **BUSCA LITERAL DOS TREZE TERMOS no texto integral (2.680 caracteres): NENHUM dos treze termos
  aparece.** Não há veto escrito.
- Não vi captcha no HTML da página; **veredito só com o clique**.

### 3.3 Dedupe pela referência da requisição

Cruzado contra `PORTAIS` (748 linhas), `enviados.csv` (753 linhas) e
`automacao/processados.csv` (1.872 linhas):

| Referência | Em `PORTAIS`? | Em `enviados.csv`? | Em `processados.csv`? |
|---|---|---|---|
| `ufxstudios.com/job/environment-artist-houdini-mid-senior` | não | não | não |
| `ufxstudios.com/job/speculative-application` | não | não | não |
| `hiring@ufxstudios.com` / `vfx_hr@ufxstudios.com` | não | não | não |
| `jobs_montreal@buf.com` | não | não | não |
| `jobs_paris@buf.com` | — | **SIM, 02/09** | **SIM, auto-reply** |
| `jobs@11bitstudios.com` | não | não | não |
| `becurious@supernaturalstudios.com` | não | não | não |
| `smartrecruiters.com/ryseupstudios/743999710587649` | não | não | não |

`ufxstudios` aparece só em arquivos de **fila** (`garimpo-cgstudiomap.csv`,
`garimpo-pdf-fontes.csv`, `backlog-estudios.md`, `canada-reabertos-07-09.csv`), nunca como
candidatura. **É casa nova, sem duplicata.**

---

## 4. AS QUE CONFIRMEI MORTAS DE VERDADE

Isto vale tanto quanto as reaberturas: encerra a dúvida e impede que a campanha refaça a varredura.

### 4.1 Domínio que não resolve nem responde — reteste feito com `https://` e UA de Chrome

- **`garimpo-cgstudiomap.csv`: 81 dos 86 registrados com `HTTP 0` continuam `000`** (falha de
  conexão/DNS, 20s de limite). O registro antigo estava certo nessas 81. Só 4 dos 86 voltaram
  (BUF, Toonkit, Angels & Demons e Keyframe Studios com 403).
- **`fila-gamedevmap-europa.csv`: 195 das 310 URLs continuam `000`.** Maioria são microestúdios de
  Londres e Estocolmo cujo domínio caiu. O registro `porta-sem-resposta` estava certo em 63% dos casos.
- **`fila-gamedevmap-canada.csv`: 12 das 21 continuam `000`** — Glu Toronto, Gnometech,
  Household Games, Sword & Sworcery, Magitech, Maple Powered, Evil Objective, Giant Sandbox,
  Bitten Toast, Magmic, DolphinBarn, Prismata (Lunarch), Corbie Games. Mais duas com **404 na raiz**:
  A-Game Studios e Nesting Games.

### 4.2 Morte com evidência nomeada

| Estúdio | Evidência literal |
|---|---|
| **Ánima Estudios** (México) | Todos os 14 caminhos testados devolvem **HTTP 530** com corpo de 17 bytes — inclusive o caminho de controle. O servidor de origem está fora do ar atrás do Cloudflare. Confirma o registro antigo (erro 1016) |
| **Novarama** (Barcelona) | `novarama.com` serve certificado de outro domínio: `SSL: no alternative certificate subject name matches target host name`. Causa confirmada por busca: **a Novarama declarou falência em março de 2024 e o estúdio fechou.** Não é endereço errado, é estúdio extinto. **Pode sair do painel** |
| **Gamecan** (Estônia) | Quatro variações de slug de Teamtailor testadas hoje — `gamecan`, `gamecanoy`, `gamecanstudio`, `gamecangames` — **todas 404**. Não é slug errado |
| **SuperNatural Studios** (Vancouver) | Quadro do Greenhouse morto de verdade: seis tokens já testados no total, todos 404. Sobra só o email |
| **Blur Studio** | `boards-api.greenhouse.io/v1/boards/blurstudio/jobs` → **HTTP 200 com 0 vagas**. As variações `blur` e `blurstudios` dão 404. Quadro vivo e vazio, não é slug errado |
| **Gravity Well** | `gravitywell` → **200 com 0 vagas**; `gravity-well`, `gravitywellgames`, `gravitywellstudio` → 404. Quadro vivo e vazio |
| **Day 9 Game Studio** | `day9` e `day9games` no Greenhouse → 404. Confirma o registro antigo |
| **31st Union Valencia** | `31stunion` → **200 com 5 vagas, todas em San Mateo, Califórnia**: Lead Designer, Lead UI Engineer, Producer, Senior Director Online Services, Shader Technical Artist. Zero na disciplina, zero em Valência. Confirma o registro antigo palavra por palavra |
| **Fireproof Games** | `/vendors/vacancies` responde 200, mas é **um post de blog de 24 de agosto de 2021**, não uma página de vagas. Não é reabertura |
| **Lightroom 3D** | `/about/careers` responde 200 **porque o site é Wix e devolve 200 para qualquer caminho** — o controle `/zqx-nao-existe-123` também dá 200. Falso positivo descartado. E o registro antigo está certo no mérito: é renderização 3D de produto industrial, não é a disciplina |
| **Imaginarium Studios, Mojiworks, Saddington Baynes, Ekstasy, JFX, Revolution Software, d3t, The Line, Zugalu, Get Set Games, GalacticThumb, Frolic Labs, Cococucumber, Cellardoor, Bloom Digital, Toys for Bob, Minimo VFX, Wicked Fox, Like A Photon, Able & Baker** | Todos os 14 caminhos de carreiras testados com controle de caminho inexistente: **nenhum caminho de vagas existe**. Só sobrou `/contact` genérico. Os registros antigos estavam certos. Da Toys for Bob confirmei que o `recruiting@toysforbob.dev` continua publicado na raiz, como o registro já dizia |

### 4.3 O que este teste DESMENTIU

**A hipótese vale para 4,3% das entradas reconferidas (22 em 509), não para a maioria.**
E vale de forma muito desigual:

- Onde o registro dizia `HTTP 0` / não resolve: **94% continuam mortas** (288 de 306). Aqui a
  hipótese está **errada** — o painel acertou. **Não vale refazer esta varredura.**
- Onde o registro dizia `403` ou `site-fora-do-ar` com código não-zero: **~80% eram falso negativo**
  (o `403` era o cliente, não o estúdio). Aqui a hipótese está **certíssima**, e é o único lugar
  onde vale a pena olhar de novo.
- Onde o registro dizia `/careers` 404: **9 de 23 tinham caminho alternativo vivo (39%)** — mas
  só 1 delas tinha vaga da disciplina atrás. **A hipótese acerta o diagnóstico e erra o prêmio.**
- Slug de ATS: **1 acerto em 24 tentativas (4%)**. O caso Snowprint foi sorte, não padrão.

**Conclusão honesta:** o painel **não** está cheio de portas enterradas por endereço errado.
Ele tem um bolso bem definido — os registros de `403` e os `/careers` 404 — que valia mesmo
reabrir, e um corpo grande de domínios mortos que o painel já classificou certo. As seis
reaberturas de hoje de manhã eram casas grandes e visíveis; o resto da cauda é microestúdio
morto. **Depois desta rodada, considere as 306 entradas de `HTTP 0` como fechadas.**

---

## 5. AS QUE PRECISAM DE NAVEGADOR (`precisa-de-navegador`)

O maestro precisa abrir. Todas devolvem parede de rede contra este IP, **não** porta morta.
Confirmei que é parede, e não endereço errado, porque **o caminho de controle inexistente
devolve o mesmo código dos caminhos reais** — ou seja, o servidor barra antes de olhar a URL.

**a) `careers.rebellion.com` — nomeada, e é a mais importante da lista.**
A página abre 200, mas o bloco de vagas monta em JavaScript e não há endpoint público
(`/wp-json/wp/v2/vacancy`, `/api/vacancies`, `/vacancies` → todos 404). É a casa que absorveu a
Radiant Worlds e tem estúdios em Oxford, Warwick, Wakefield, Liverpool e Didcot.
**Abrir `https://careers.rebellion.com/#vacancies` e procurar character/modelling/texture.**

**b) Muro uniforme de WAF (403 em TODOS os caminhos, controle incluído) — 42 casas europeias.**
As que mais valem pelo tamanho e pelo catálogo: **Epic Games**, **Gamigo**, **CrazyLabs**,
**Outright Games**, **Small Giant Games**, **Krillbite**, **Rockpocket Games**, **PlayerThree**,
**Untold Games**, **Pretty Simple Games**, **IMGN.PRO**, **Superlumen**, **Texel Raptor**,
**White Paper Games**, **Frog Collective**, **Studios Drama**, **Goldhawk Interactive**,
**Massive Monster**, **Keoken**, **Propulsion Games**, **Scarlet City Studios**, **Silden**,
**Skyrocketon**, **Fringe Planet**, **Drop of Pixel**, **Gentle Troll**, **Chapatiz**,
**Crowdpark**, **Managames**, **Pixel Wizards**, **Fleetyard**, **Fragile Continuum**,
**Nodbrim**, **Orbifold**, **Strategy Labs**, **Bitbeast**, **Bellyflop**, **Loveshack**,
**Ninja VR**, **Yummy Games**, e duas páginas de ArtStation.

**c) Desafio anti-robô com corpo de 169-174 bytes (HTTP 202, Cloudflare) — 24 casas europeias
   + 2 canadenses.** Europa: `afewbitsshort`, `alamode.games`, `altitude-games`, `avokiddo`,
`badviking`, `beatnikgames`, `curapy`, `dotdot.wtf`, `earthworkgames`, `fundamentalsurgery`,
`gravity.blue`, `ladyluckgames`, `lagrange-studio`, `meangrip`, `meetinvr`, `morbidwaregames`,
`persistant.fr`, `playwing`, `pridefulsloth`, `stutterfoxstudios`, `tsunoagames`,
`underthestairs.studio`, `vivid-storm`, `warpdigital`.
Canadá: **Hyper Hippo Entertainment** (Kelowna) e **Little Buffalo Studios** (Toronto).
Do cgstudiomap, mesma assinatura: `10th Ave Animation`, `Mighty Nice`, `Copernicus Animation`,
`Elliot Animation`, `Copenhagen Bombay`, `Nice Shoes`, `One Tree Forest Films`, `Bolder`,
`Electric Theatre Collective`, `Exient`, `Infocandy`, `Seed Animation`, `Studio Giggle`, `wec360`,
`Cumulus VFX`, `Chicken Bone FX`, `Deeproot Studios`, `Polymorph`.

**d) Servidor devolvendo erro em todos os caminhos (não é 404):** `hexfoundry.se` (503 uniforme),
`lelaboblanc.paris` (500 uniforme, mas `/contact` abre 200), `isitlove.com` (504 nos caminhos de
carreiras), `badmonkee.de`, `blueboxgamestudios.com`, `mudita.games`, `bluedotgames.com`,
`coromon.com`, `envision-entertainment.de`, `eville-game.com`, `exit-vr.de`, `fakt-software.de`,
`kamibox.de`, `monochrome.paris`, `ovosonico.com`, `fancy-bytes.de`.

**e) TLS que não fecha por este ambiente:** `Big Pixel Studios` (certificado genérico
`*.stackcp.com`) — o registro antigo já dizia isso e continua verdade.

**f) Host que o proxy derruba no meio da leitura** (`ws_closed_mid_exchange`):
`funrock.com/jobs/` (página existe, corpo não lido em 4 tentativas), `neckboltgames.com`,
`northernergames.com`. WebFetch também recusou `funrock.com` e `cuttingcornergames.com`
com `EGRESS_BLOCKED`.

---

## 6. LIÇÕES DE MÉTODO MEDIDAS NESTA RODADA

1. **A barra final decide o veredito, e decide nos dois sentidos.** A campanha já sabia que
   `bugbeargames.com/careers` **sem** barra falha e **com** barra abre. Hoje a Hard Light provou o
   inverso: `/careers/` **com** barra dá 404 e **sem** barra dá 200. **Sempre teste as duas formas.**

2. **Use um caminho de controle inexistente antes de comemorar um 200.** Sites em Wix, Framer e
   parte dos WordPress devolvem 200 para qualquer URL. A Lightroom 3D quase entrou como reabertura
   por isso. O controle `/zqx-nao-existe-123` custa uma requisição e evita o falso positivo.

3. **O `403` do registro antigo quase nunca é o estúdio.** Dos 24 registros `403` do cgstudiomap,
   20 viraram 200 só com `https://` + UA de Chrome. **Mas** quando o `403` aparece **também no
   caminho de controle** e em todos os caminhos com o mesmo tamanho de corpo, aí é WAF de verdade
   e só o navegador passa. O tamanho de corpo idêntico em todos os caminhos é a assinatura.

4. **O corpo de 169-174 bytes com HTTP 202 é o desafio do Cloudflare**, não uma página. Qualquer
   varredura que conte 202 como resposta válida vai registrar dezenas de casas como "site vivo, sem
   vagas" quando na verdade nunca viu o site.

5. **Domínio com certificado "trocado" pode ser aquisição, não abandono.** O `radiantworlds.com`
   servindo `reb.to` não era infraestrutura quebrada: era a Rebellion, dona do estúdio desde 2018.
   Antes de marcar domínio revendido, busque o **nome** do estúdio.

6. **O JSON Feed do Teamtailor usa a chave `items`, não `jobs`.** O painel já registrou isso na
   Fatshark; reconfirmei hoje na Funcom. Varredura que só lê `jobs` conta zero em quadro cheio.

7. **`http://` simples e domínio com `www` são duas armadilhas separadas.** A UFX estava registrada
   como `http://www.ufxstudios.com` e falhava por causa das duas.
