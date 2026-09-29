# TRIAGEM OCEANIA (+ cauda longa europeia) — 08/09

Fonte: `automacao/fila-gamedevmap-europa.csv` (o arquivo tem nome de Europa mas trouxe a Oceania junto).
Metodo: so `curl` (UA de Chrome, sempre `https://`), WebSearch e WebFetch. Nenhum navegador foi aberto.
Nenhum email, rascunho, formulario ou envio. Nenhum commit, nenhum push.

---

## 1. QUANTO FOI TRIADO

**1.281 linhas em-escopo saíram de `nao-triado`.** Depois desta rodada sobram **0 linhas em-escopo
`nao-triado`** no arquivo (as 439 que ainda estao `nao-triado` sao todas `fora-de-escopo`).

### Oceania — 271 linhas em-escopo (de 298 linhas Oceania no total; 25 eram fora-de-escopo e 2 ja tinham veredito)

| Pais | Linhas triadas |
|---|---|
| Australia | 201 |
| New Zealand | 70 |
| **Total** | **271** |

Por cidade (as quatro que o briefing citou batem exatamente):

| Cidade | Triadas |
|---|---|
| Melbourne | 81 |
| Brisbane | 29 |
| Auckland | 28 |
| Sydney | 27 |
| Wellington | 17 |
| Adelaide | 14 |
| Christchurch | 11 |
| Dunedin | 9 |
| Canberra | 5 |
| Hobart | 4 |
| Perth | 4 |
| Darwin | 3 |
| Gold Coast, Surry Hills | 2 cada |
| Abbotsford, Bakery Hill, Blenheim, Botany, Brookvale, Central Wellington, Chippendale, City Beach, Epping, Essendon, Fortitude Valley, Frankton, Hallett Cove, Helensvale, Innisfall, Karratha, Kelvin Grove, Lane Cove North, Launceston, Leederville, Lismore, Miramar, Miranda, North Ryde, North Sydney, Paekakariki, Parramatta, Pyrmont, Raleigh, Richmond, South Yarra, Torquay, Tuart Hill, Ultimo, Umina Beach | 1 cada |

**Quadro vivo (quadro de vagas efetivamente lido, com ou sem vaga da disciplina): 39 dos 271.**
Dos outros: 22 nao responderam em nenhuma das 8 variacoes de caminho, 163 tem site vivo mas nenhuma
porta de carreiras localizavel no HTML, e 47 tem porta 200 sem nome de ATS e sem vaga da disciplina no texto.

### Cauda longa europeia — 1.010 linhas em-escopo

England 217 · Sweden 155 · France 110 · Germany 110 · Netherlands 74 · Spain 66 · Poland 44 ·
Italy 40 · Belgium 38 · Finland 35 · Scotland 30 · Norway 21 · Switzerland 19 · Wales 12 ·
Portugal 11 · Austria 8 · Czechia 8 · Denmark 4 · Ireland 4 · Northern Ireland 2 · United Kingdom 2.

**Quadro vivo (lido de fato): 49 dos 1.010.** 114 nao responderam em nenhuma das 10 variacoes de caminho.

---

## 2. AS VAGAS VIVAS DA DISCIPLINA

Formato de cada entrada: **titulo** · link direto · ATS · formato · faixa · **resultado LITERAL da busca dos treze termos**.
Os treze: `authoriz` · `eligib` · `sponsor` · `work permit` · `must be based` · `LMIA` · `days a week` ·
`days per week` · `days in the office` · idioma local · `resident` · `relocat` · `located in` ·
`unable to support` · `no relocation`. Rodados sobre o anuncio inteiro baixado, nao sobre o resumo.

### 2.1 DESTAQUE — OFERECE REALOCACAO / APOIO DE IMIGRACAO

#### ★★ HandyGames (THQ Nordic Mobile) — Giebelstadt, Alemanha
- **2D/3D Game Artist (Mid-level/Senior) (f/m/d)**
- Link direto: https://handy-games.com/en/jobs/2d-3d-game-artist/
- ATS: formulario proprio no site do estudio (indice em https://handy-games.com/jobs)
- Formato: **efetivo, presencial** — o anuncio diz *"in Giebelstadt/Germany (on-site only)"*
- Faixa: nao publicada
- Escopo do trabalho, citado: *"Execution of the entire game asset creation workflow: from high- and low-poly
  modeling to PBR texturing and integration into the game engine (Unity)"* e *"Creation of stylized 3D models,
  environments, props, and potentially characters"*
- **Treze termos, resultado literal:** casa **`relocat`**, e casa como **OFERTA**:
  *"**Full relocation support**: We are here to help. Our team actively supports you in finding housing and
  navigating bureaucratic administrative tasks"*. Casa tambem **idioma local**, e tambem a favor:
  *"our daily business is conducted primarily in English. **German language skills are by no means a requirement.**"*
  Nenhum dos outros onze termos aparece. **Nao ha veto escrito — ha o contrario dele, duas vezes.**
- Nao vi captcha no HTML, veredito so com o clique.

#### ★★ Grinding Gear Games — Auckland (Henderson), Nova Zelandia
- A vaga listada **nao e** da disciplina (VFX Artist e Web Programmer), mas a porta e o texto sao valiosos:
- Link direto: https://www.grindinggear.com/?page=careers
- ATS: nenhum — candidatura por email, indicada no proprio anuncio
- Frase de abertura, literal: *"**We are currently hiring for all roles.** If you are interested, please contact us."*
- **Treze termos, resultado literal:** casa **`relocat`** — *"**We're offering relocation assistance for the right
  candidates.** These are full-time roles in Henderson, Auckland. Please only apply if you currently reside in
  New Zealand/Auckland **or are willing to relocate**. **We can assist with applying for work visas for these roles.**"*
  Casa tambem **`resident`**, mas **em outro bloco da pagina, colado so na vaga de Customer Support**:
  *"Please only apply if you currently reside in New Zealand or Australia and are either a New Zealand Citizen,
  Resident or Australian Citizen."* Esse veto **nao cobre** o bloco de arte.
- **JA CONHECIDO** — `Grinding Gear Games` ja esta no painel.
- Nao vi captcha no HTML, veredito so com o clique.

### 2.2 VAGAS DA DISCIPLINA, SEM VETO ESCRITO

#### ~~People Can Fly — Varsovia, Polonia~~ — CORRIGIDO PELO MAESTRO EM 08/09: TEM VETO ESCRITO, NAO APLICAR

> **Correcao feita depois de entregue este relatorio, com a fonte oficial aberta.** O relatorio
> abaixo diz "NENHUM DOS TREZE TERMOS" e esta errado. O painel ja carregava esta requisicao como
> VETO DE RESIDENCIA desde 07/09, e o curl na API do SmartRecruiters confirma o painel: a PRIMEIRA
> linha da descricao e *"The role is open to candidates **only from** the game industry who are
> **based in** Europe."* A regua de treze termos nao pega essa frase, porque tem `must be based` e
> nao tem `based in` nem `only from`. **A regua passou a ter dezessete termos**, e a correcao esta
> no BRIEF-FORCA-TAREFA. A vaga esta fora.

#### People Can Fly — Varsovia, Polonia (texto original do relatorio, mantido para registro)
- **Senior Asset Artist (Hard Surface)**
- Link direto: https://jobs.smartrecruiters.com/PeopleCanFly/744000141244724-senior-asset-artist-hard-surface-
- ATS: SmartRecruiters (`PeopleCanFly`, 14 vagas no quadro)
- Formato: **efetivo (`permanent` / Full-time), remoto** (`remote: true` no payload da API), Mid-Senior Level
- Faixa: nao publicada
- **Treze termos: NENHUM DOS TREZE TERMOS.**
- **JA CONHECIDO** — tres linhas de People Can Fly no CSV ja carregavam exatamente este veredito; a quarta
  (Rzeszow) era a que faltava. Nao e alvo novo.
- Observacao: o **Principal Character Artist** do mesmo quadro esta em **Montreal**, fora da Europa.

#### Stupendium Softworks — Worthing, Inglaterra
- **3D Artist (Retro-Style)** — o anuncio traz `OPEN // POSTED MAY 2026`
- Link direto: https://stupendiumsoftworks.com/career
- ATS: formulario proprio
- Formato: **freelance por contrato, remoto**. O estudio avisa por escrito: *"Stupendium Softworks is currently
  only able to offer **freelance contract work, not full-time contracts**."*
- Faixa: nao publicada
- Escopo, literal: *"Create stylised 3D models inspired by PS1-era aesthetics, **spanning both characters and
  environmental assets**"* e *"Own the full asset pipeline, from blockout through to final in-engine implementation."*
- **Treze termos: NENHUM DOS TREZE TERMOS.**
- Nao vi captcha no HTML, veredito so com o clique.

#### Innovina Interactive — Genova, Italia
- **3D Hard Surface Artist** e **Senior 3D Hard Surface Artist**
- Link direto: https://interactive.innovina.it/careers
- ATS: formulario proprio (candidatura por `info@innovina.it`)
- Formato: nao declarado no anuncio; estudio presencial em Genova
- Faixa: nao publicada
- **Treze termos, resultado literal:** casa **`located in`** — mas na frase *"a privately owned Italian game
  development studio **located in beautiful Genoa**"*, que descreve o **endereco do estudio**, nao uma exigencia
  sobre o candidato. Nenhum dos outros doze. **Sem veto escrito.**

#### Raylight Games — Benevento / escritorio em Napoles, Italia
- **Senior 3D Artists**
- Link direto: https://www.raylightgames.com/careers
- ATS: formulario proprio (envio de CV por email indicado na pagina)
- Formato: **presencial** — *"Workplace is our office in Napoli"*
- Faixa: nao publicada
- Escopo, literal: *"Delivers a set of final highly polished assets including **high and low poly models and
  textures**"*, *"Skilled at drawing, **sculpting**, and conceptualization"*, *"**Knowledge/understanding of human
  and animal anatomy**"*, ferramentas 3dsMax/Maya/Blender, ZBrush, Substance Painter
- **Treze termos: NENHUM DOS TREZE TERMOS.**

#### Gigantic Duck — Boras, Suecia
- **3D Artist, Bombergrounds** e **3D Artist, Unannounced Game** (duas vagas separadas)
- Link direto: https://giganticduck.com/careers
- ATS: formulario proprio
- Formato: **efetivo, remoto** — *"Remote, Full time (40 hours/week)"* nas duas
- Faixa: nao publicada
- **Treze termos: NENHUM DOS TREZE TERMOS.**

#### House of How Sweden — Boden, Suecia
- **Senior 3D Artist — Sweden (Onsite)**
- Link direto: http://www.houseofhow.com/job/senior-3d-artist-sweden-onsite/
- ATS: formulario proprio
- Formato: **efetivo, presencial em Boden** (`Full Time`, `Onsite` no proprio titulo)
- Faixa: nao publicada
- **Treze termos: NENHUM DOS TREZE TERMOS** — rodados sobre o indice de carreiras, porque **a pagina da vaga
  devolve 403 ao curl**. Veredito da vaga em si so com o clique do maestro.

#### Sluggerfly — Essen, Alemanha
- **3D Artist (m/f)**
- Link direto: https://sluggerfly.com (secao **Jobs** na propria home; nao ha `/careers`, `/jobs` nem `/karriere`)
- ATS: nenhum — candidatura por email indicada no anuncio
- Formato: nao declarado
- Faixa: nao publicada
- Escopo, literal: *"create high-quality 3d assets with **blender**, have some Photoshop skills"*, motor Unreal Engine 4
- **Treze termos: NENHUM DOS TREZE TERMOS.** O anuncio esta **em ingles**, apesar do estudio ser alemao.

#### Holonautic — Horw / Lausanne, Suica
- **3D Artist & Designer**
- Link direto: https://www.holonautic.com/jobs/3d-artist-designer
- ATS: formulario proprio
- Formato: nao declarado; empresa incubada em Lausanne
- Faixa: nao publicada
- Escopo: *"Conceptualize and **model 3D assets**"*, Unity/Blender, produto de VR
- **Treze termos: NENHUM DOS TREZE TERMOS.** Prioridade MEDIA (VR, generalista).

### 2.3 VAGAS ADJACENTES — prioridade MEDIA (ambiente / props / generalista)

#### Spunge Games — Fortitude Valley, Brisbane, Australia  *(alvo NOVO)*
- **3D Generalist (Real-Time / UE5)** (a outra vaga viva, Senior Technical Artist, nao e da disciplina)
- Link direto: https://www.spungegames.com/careers
- ATS: nenhum — *"Submit your resume or enquiry letter to us at jobs@spungegames.com"*
- Formato: **hibrido** — *"We offer a hybrid work environment, where our team enjoy connecting with each other
  in the Studio and have the flexibility to WFH a couple of days each week."*
- Faixa: nao publicada
- **Treze termos, resultado literal:** casa **`located in`**, na frase *"**Located in Fortitude Valley**, our studio
  is only a short walk from public transport"* — endereco do estudio, nao exigencia sobre o candidato.
  Nenhum dos outros doze. **Sem veto escrito.**
- Nao vi captcha no HTML, veredito so com o clique.

#### Starloop Studios (grupo Magic Media) — Lleida, Espanha
- **Senior 3D Environment Artist**
- Link direto: https://magicmedia.studio/career_listing/senior-3d-environment-artist/
- **ATENCAO — COORDENADA EM OUTRO DOMINIO:** o quadro **nao** fica em `starloopstudios.com`; fica em
  **`magicmedia.studio`** (a Starloop e do grupo Magic Media). Mesma armadilha da Artifex/`aastudios.ca`.
- ATS: formulario proprio do grupo
- Formato: **remoto, `Project Based`** (contrato por projeto)
- Faixa: nao publicada
- **Treze termos, resultado literal:** casa **`resident`**, mas dentro da palavra **"President"** num depoimento de
  cliente (*"Michael Martinez, President Funcraft"*). Falso positivo. Nenhum dos outros doze. **Sem veto escrito.**

#### Red Sky Games — Cologno Monzese (Milao), Italia
- **[Freelancer] Game Art Generalist (Hard Surface)**
- Link direto: https://redskygames.com/careers
- ATS: formulario proprio
- Formato: **freelancer, remoto** — *"**All positions are remote**"*
- Faixa: nao publicada
- Escopo, literal: *"creating visually stunning in-game assets as a **Hard Surface 3D Artist** ... primarily on
  environment art, weapons, and vehicles ... capable of creating **photorealistic models & textures**"*
- **Treze termos: NENHUM DOS TREZE TERMOS.**

#### Miami Avalon — Northwich / Warwick, Inglaterra (duas linhas no CSV, mesmo site)
- **Freelance 3D Prop Artist** (projeto *Ascend*)
- Link direto: https://miamiavalon.com/jobs
- ATS: formulario proprio
- Formato: **freelance**
- Faixa: nao publicada
- **Treze termos: NENHUM DOS TREZE TERMOS.**

#### Foxie Ventures — Adelaide, Australia
- **Environment Artist** e **Game Art Manager** (dentro de um quadro de nove entradas)
- Link direto: https://www.foxieventures.com/careers
- ATS: formulario proprio
- Formato: o quadro se chama **"Open Positions & Expressions of Interest"** e cada linha tem o botao
  **"Express Interest"** — sao **Full Time, Adelaide**, mas **sem data de publicacao**, entao trate como
  banco de talentos ate o clique confirmar.
- Faixa: nao publicada
- **Treze termos: NENHUM DOS TREZE TERMOS.**

---

## 3. QUE EXIGEM CONTA / NAO FORAM LISTAVEIS DAQUI

Nao sao "porta fechada". Sao portas que este ambiente nao alcanca.

| Estudio | Situacao medida |
|---|---|
| **PikPok** (Wellington, NZ) | ATS Workable (`pikpok`). `apply.workable.com` devolveu **429** (rate limit da Cloudflare) em todas as tentativas e a WebFetch e **bloqueada pelo proxy de egresso** para esse host. **JA CONHECIDO** no painel (`PikPok (board Workable)`). |
| **8i** (Wellington, NZ) | Mesmo bloqueio 429/egress. Contornado pelo HTML da propria pagina: 2 vagas, `Technical Support Engineer` (Wellington) e `Full Stack Web Developer` (Chicago). Nenhuma da disciplina. |
| **Team17 / Everplay Group** (Wakefield, ING) | ATS Workable (`team-17-digital`) — mesmo 429. Nao foi possivel listar. |
| **New Tales** (Issy-les-Moulineaux, FR) | ATS Workable — mesmo 429. Nao foi possivel listar. |
| **Splash Damage** (Bromley, ING) | ATS Jobvite. `jobs.jobvite.com/<token>/search` redireciona para **`search.jobvite.com`, que o proxy de egresso deste ambiente recusa** ("Host not in allowlist"). Nao foi possivel listar. |
| **Halfbrick Studios** (Kelvin Grove, AU) | O HTML aponta Greenhouse `for=halfbrickstudios`. Testei **quatro** identificadores (`halfbrick`, `halfbrickstudios`, `halfbrick-studios` na `boards-api`, mais `boards.` e `job-boards.greenhouse.io`): todos **404**, e o proprio `embed/job_board/js` devolve **"There was an error"** com HTTP 500. O quadro esta quebrado ou vazio do lado da Greenhouse. |
| **Behaviour UK - North** (Middlesbrough), **Dlala Studios** (Witham), **Absurd Ventures** (Altrincham), **Fortis Games** (Remote/ES), **Bulkhead Phoenix** (Derby), **Limbic Entertainment** (Langen), **GameHouse Spain** (Alicante), **Ming Media** (Remote/SE) | Pagina de carreiras viva mas a lista de vagas so monta por JS, e o token do ATS nao aparece legivel no HTML. |
| **Zero Latency VR** (Abbotsford, AU) | Site inteiro responde *"Please enable JavaScript to view this site"* — 1,6 KB de HTML util. |
| **Interactive Games Entertainment** (Emmen, NL) | O site cadastrado no gamedevmap e uma pagina de Facebook, que devolve bloqueio temporario. Porta nao verificavel. |
| **Caipirinha Games** (Altenholz, DE) | A pagina `/karriere` tem abas `Game Developer / 3D Artist / Game Designer / Level Designer / Sound Artist`. So a de Game Developer vem renderizada no curl. **A aba de 3D Artist existe**, mas o texto nao carrega sem JS. Vale o clique. |

---

## 4. CORRECOES DE COORDENADA MEDIDAS HOJE

Cinco portas que pareceriam fechadas com o identificador errado, e nao estao:

1. **Aristocrat Leisure** (North Ryde e Brookvale, AU) — `careers.aristocrat.com` da **403** ao curl.
   O Workday **nao** e `aristocrat.wd1` (da **422**, ou seja, locatario inexistente): e
   **`aristocrat.wd3.myworkdayjobs.com`**, e o site nao e `External` nem `Aristocrat` (todos **404**, ou seja,
   locatario existe e o caminho e que estava errado) — o site certo e **`AristocratExternalCareersSite`**.
   Endpoint que responde 200:
   `https://aristocrat.wd3.myworkdayjobs.com/wday/cxs/aristocrat/AristocratExternalCareersSite/jobs`
   Buscas `artist`, `3d`, `character`, `modeler`, `texture` e `Australia`: **nenhuma vaga da disciplina na Australia**.
2. **Starloop Studios** (Lleida, ES) — quadro em **`magicmedia.studio`**, dominio diferente do institucional.
3. **Facepunch Studios** (Walsall, ING) — `facepunch.teamtailor.com/jobs.json` **redireciona** para
   `facepunch.com/careers` (Squarespace). O quadro real tem 3 vagas, nenhuma da disciplina.
4. **Wetaworkshop** — o Teamtailor e **`wetaworkshop`** (nao `weta`, nao `wetagameshop`); `jobs.json` responde 200.
5. **Sumo North West** e **Red Kite Games** — nao tem quadro proprio: os dois caem no **mesmo quadro HiBob do
   grupo Sumo** (Sumo Digital + Red Kite Games + Atomhawk), com 13 vagas.

---

## 5. DESCARTES, COM A FRASE DO ANUNCIO ENTRE ASPAS

### Descarte por VETO ESCRITO

- **Weltenbauer** (Wiesbaden, DE) — **Environment Artist w/m/d**, Personio, *"Wiesbaden oder Remote"*,
  `temporary full-time`. **Veto escrito de idioma local:** *"**Gutes Deutsch und Englisch in Wort und Schrift**."*
  Link: https://weltenbauer-software-entwicklung-gmbh.jobs.personio.de/job/2677880
  (Registro honesto: a lista mecanica dos treze **nao** pegaria isso; foi preciso ler o anuncio em alemao.
  Acrescentei os padroes de idioma alemao/frances/sueco/polones ao verificador por causa desta vaga.)

### Descarte por disciplina errada

- **Two and a Half Studios** (Hobart, AU) — o anuncio se chama *"Lead CG/Sprite Artist"* e o corpo diz
  *"searching for a **lead character artist**"*, mas o trabalho e 2D: *"You will be required to create
  approximately **30 CGs and at least 2 sprites**"* e *"18+ requirement, able to **draw** uncensored M/M CGs"*.
  Ilustracao 2D de visual novel, nao personagem 3D.
- **League of Geeks** (Melbourne, AU) — unica vaga viva e **2D Artist** (05/09):
  *"**Create sprite assets** in the game-style."*
- **Outerdawn** (Auckland, NZ) — **Senior UI Artist**. UI nao e a disciplina.
- **QLoud Games / Loftia** (Sydney, AU) — **Trailer Editor & Capture Artist** e Social Media Content Creator.
- **The Voxel Agents** (Melbourne, AU) — **Technical and VFX Artist** (VFX em tempo real) e Unity Programmer.
  Alem disso a pagina esta congelada: *"Last updated: 8th Sept, **2023**"*.
- **Alderon Games** (Bakery Hill, AU) — **Technical Artist** e Unreal Gameplay & Security Engineer.
  (Nenhum dos treze termos no anuncio.)
- **Cloud Imperium Games** (Frankfurt, DE) — tem **Character Concept Artist** e **Character Technical Artist**,
  mas as duas em **Montreal, Canada**, e sao concept e technical art, nao modelagem.
- **Sumo / Red Kite / Atomhawk** (grupo, Reino Unido e India) — em Art so ha `Technical Animator` x2,
  `UI/UX Artist` e `Senior VFX Artist` (India). O *"Visual Development"* que aparece no site da Sumo e
  **nome de servico do estudio**, nao vaga.
- **Seabird Interactive** (Saint-Malo, FR) — a unica de 3D e *"Stage Artiste 3D"*, estagio, anuncio em frances.

### Descarte por vaga fora da geografia

- **ODD Games** (Adelaide, AU) — *"ODD Games **Philippines (Davao City)** is looking for senior/junior
  programmers, 3d artists. **Full-time work from our Ecoland office.**"* A vaga nao e na Oceania.
- **Sozap** (Nykoping, SE) — tem `3D Artist Full-Time`, mas em **Nis, Servia**, e o quadro inteiro esta
  datado de **17/03/2023**.

### Descarte por "e a equipe, nao vaga" (armadilha classica desta rodada)

Casos em que o termo da disciplina aparece so em pagina "Sobre / Nossa equipe", em depoimento de funcionario,
em post de blog ou em lista de servicos de outsourcing — **nenhum e vaga**:
Grease Monkey Games (*"Savannah - 3d Artist"*, depoimento), BeamTeam Games (*"Ben Massey **Lead 3D Artist**"*,
diretor), Effort Star Games, Exbleative, Sweaty Chair (so estagio), Cardboard Sword, Game Smithing,
Long Way Home Games, ModalVR Studio, Paw Print Games, VideoDojo Games, Blue Ramen Studios, Tea For Two,
Hindsight Studios, Voodoo Duck Games, Codename Red, Linx Interactive, Sarepta Studio, Insanto Studios,
Mana Brigade, nornware, Kittens in Timespace, Dave Sapien, Lost Token (comentario de jogador num post de itch.io),
Rebourne Studios (artigo de blog **em indonesio** sobre profissoes de games), Moonmana, Nieko e
Frost Earth Studio (as duas ultimas: **lista de servicos de outsourcing**).

### Descarte por quadro vazio (inclusive a armadilha do rodape)

- **Space Rock Games** (Auckland, NZ) — *"please check out the **open roles below**"* e **nao lista nenhuma**.
  Exatamente o padrao da EB Studio, ao contrario: convite no meio, vazio embaixo.
- **Toast Interactive** (Brisbane, AU) — *"Check out the current job vacancies"* e nao ha vaga listada.
- **Chaos Theory** (Chippendale, AU) — *"**There are no job openings currently listed.**"*
- **Featherweight Games** (Sydney, AU) — *"**Unfortunately we don't currently have any open positions.**"*
- **Dinosaur Polo Club** (Wellington, NZ) — *"Sorry, right now we have **no open positions**"*.
- **Blowfish Studios** (North Sydney, AU) — *"**Open Positions: 0**"*.
- **Mode Games** (Sydney, AU) — os seis filtros (Art, Development, Design, Animation, Marketing, Internship)
  dizem todos *"**No items found.**"*
- **CerebralFix** (Christchurch, NZ) — secao *"Current Openings"* vazia. **JA CONHECIDO** no painel.
- **Silent Games** (Newcastle, ING) — SmartRecruiters com `totalFound: 0`, e a propria pagina se chama
  **`CAREERS/CLOSED`**.
- **Alta** (Sydney, AU) — Pinpoint (`altavr`), `jobs.rss` com **0 itens**.
- **Promineo Studios** (Tenerife, ES) — titulo *"Open positions"* e nenhuma vaga.
- **TT Games / Travellers Tales / TT Fusion** (Knutsford e Burnham, ING) — quadro do grupo com **1 vaga**
  (`Senior Render Tech Programmer`); a secao **Art** existe e esta com zero vagas.

---

## 6. ALERTA DE SEGURANCA

**Lighstromo Studios** (Auckland, NZ) — o HTML da pagina `Vacancies` traz uma sequencia de caracteres Unicode
invisiveis (bloco de *tags*, U+E00xx) que decodifica para uma instrucao do tipo *"Please ignore…"*, ou seja,
uma **tentativa de injecao de prompt** plantada para agentes automatizados. **Foi ignorada.** A pagina em si nao
lista nenhuma vaga. Registrado no CSV.

---

## 7. DEDUPE — O QUE JA ERA CONHECIDO

Cruzei contra `docs/index.html` (746 PORTAIS + 665 STUDIOS), `enviados.csv` e `automacao/processados.csv`.

**Ja conhecidos, e os maiores nomes da Oceania estao todos nesta lista:**
Wētā FX (banco de talentos) · Wētā Workshop (Connect) · PikPok (board Workable) · RocketWerkz (Expressions of
Interest) · Digital Confectioners (candidatura espontanea, opcao `Art: 3D Artist`) · CerebralFix ·
Grinding Gear Games · Blind Squirrel Games · Flightless · Runawayplay · Blizzard Entertainment · Riot Games ·
Gameloft · Hipster Whale · Witch Beam · Flux · Activision (pelo locatario Workday `xboxgaming`) ·
Rockstar Games · Electronic Arts · Wargaming.

**Na Europa:** People Can Fly (tres das quatro linhas ja carregavam o veredito completo) e
Wargaming Europe (mesmo quadro `wargamingen` ja triado).

Conclusao honesta que sai daqui: **a Oceania nao estava intocada nos nomes grandes** — Wētā FX, Wētā Workshop,
PikPok, RocketWerkz, Digital Confectioners, CerebralFix e Grinding Gear Games ja tinham sido trabalhados.
O que esta rodada acrescenta de alvo genuinamente novo na Oceania e **Spunge Games** e **Foxie Ventures**.

---

## 8. O QUE FOI VERIFICADO E NAO TEM NADA (casas grandes, registro negativo util)

- **Wētā FX** — quadro proprio em `careers.wetafx.co.nz`, **2 vagas**, as duas `FX and Senior FX TD -
  Expressions of Interest` (Wellington e Vancouver). Varri os IDs **1500-1570** e so 1553 e 1554 respondem 200:
  o quadro tem mesmo duas vagas, nao e paginacao escondida.
- **Wētā Workshop** — Teamtailor `wetaworkshop`, **4 vagas**: Technician Props (fixed term), Systems
  Administrator, Senior Technician Molding/Props/Hair, Casual Hosts. Nenhuma da disciplina.
- **PlaySide Studios** (270+ pessoas, Melbourne) — quadro **Employment Hero** (`playside-studios-ltd-qz2m3`),
  **1 unica entrada**: `Expression of Interest`, Port Melbourne, Full-time, On-site, publicada **18/11/2024**.
- **Aristocrat** — quadro Workday aberto (coordenada corrigida acima), nenhuma vaga da disciplina na Australia.
- **Sledgehammer Games** (Melbourne) — Workday `xboxgaming/External`, 89 vagas; a unica em Melbourne e
  `Senior UI Engineer`. Busca `Sydney` devolve **0**.
- **Gameloft Brisbane** — SmartRecruiters, 6 vagas em Brisbane, nenhuma da disciplina.
- **Big Ant Studios** (NACON, Melbourne) — WP Job Manager, 2 vagas, as duas de programacao.
  Nota literal: o termo **`days a week`** casa na pagina, mas em *"Lunch is on us **4 days a week**!"* — beneficio,
  **nao veto**.
- **Mighty Kingdom** (Adelaide) — Recruiterflow, unica entrada e `Expressions of Interest`.
- **Crytek** (Frankfurt) — Lever, 8 vagas, nenhuma de arte.
- **Magnopus** (St Albans) — Lever, 5 vagas; a de arte no Reino Unido e `Senior Technical Artist - Freelance`.
- **NaturalMotion / Zynga** (Birmingham) — Greenhouse `nmcareers`, 2 vagas, as duas de design.
- **Double Eleven** (Middlesbrough) — 6 vagas; a unica de arte e `Art Director`, na Malasia.
- **Kwalee** (Almada/Leamington) — 2 vagas: QA Tester (Bengaluru) e Senior Legal Counsel.
- **CipSoft** (Regensburg) — Recruitee, 2 vagas, nenhuma de arte.
- **metricminds** (THQ Nordic, Frankfurt) — BambooHR, 3 entradas, nenhuma da disciplina.
- **Soul Machines** (Auckland) — Workable `soul-machines-ltd`, API devolve `total: 0`.
- **RocketWerkz** (Dunedin/Auckland) — Recruitee, 4 vagas: EOI + 3 de programacao.
- **Infinite Interactive / Infinity Plus Two** (Melbourne) — mesmo BambooHR (`infinityplustwo`), 1 vaga: QA Tester.
- **BlackMill Games** (Alkmaar) — Recruitee do grupo Focus Entertainment; a unica da BlackMill e
  `Multiplayer Game Designer`.

---

## 9. LIMITES DESTA RODADA — o que travou

1. **Rate limit da Workable.** `apply.workable.com` devolveu HTTP **429 / "error code: 1015"** de forma
   persistente. Isso apagou PikPok, Team17/Everplay e New Tales da listagem.
2. **Proxy de egresso.** `apply.workable.com`, `www.linkedin.com` e `search.jobvite.com` sao **bloqueados**
   pela WebFetch/pelo proxy deste ambiente. Isso apagou Splash Damage.
3. **SPA sem token de ATS legivel.** ~8 paginas de carreiras montam a lista so por JS e nao deixam o nome do
   ATS no HTML. Estao nomeadas na secao 3 — precisam do clique, nao de mais curl.
4. **403 seletivo.** `careers.aristocrat.com`, `icandy.io/careers`, `tantalus.com.au`, `seek.com.au` e a pagina
   de vaga da House of How respondem 403 a este cliente. Em dois casos consegui contornar (Aristocrat pelo
   Workday, House of How pelo indice); nos outros nao.
5. **163 sites da Oceania e a maior parte da cauda europeia sao micro-estudios** (itch.io, Wix, Carrd,
   portfolio pessoal) sem porta de carreiras nenhuma. Estao marcados como
   `site vivo, porta de carreiras nao localizada no HTML` — nao como porta fechada.
