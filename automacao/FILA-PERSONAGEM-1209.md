# Fila de personagem — 12/09

Agente de **preparação de fila**. **Nada foi enviado, nenhum rascunho criado, nenhum formulário submetido, nenhuma mensagem mandada.** O `enviados.csv` não foi tocado. Isto é dossiê, não candidatura.

## O número que decide a rodada

Dos 15 slugs livres da reconciliação de 11/09, **14 tiveram o menu do Connect lido**. Destes:

| Medida | Valor |
|---|---|
| Slugs com menu lido | **14 de 15** (a `liquidswords` não foi lida — borda, ver abaixo) |
| **Com nome de personagem no menu** | **2** (`capsulestudio`, `princessbento`) |
| **Sem nada de personagem** | **12 de 14 — 86%** |
| Dos 2 positivos, casas de **3D** | **1** (`capsulestudio`) |
| Navegadores gastos | **0** |
| Recibos de portal encontrados para os 15 | **0** (rota livre confirmada na caixa) |

**A rodada rende exatamente uma aposta forte: a Capsule Studio, em Paris.** É um estúdio de animação **3D** com um departamento `CHARACTER` inteiro e quatro cargos de personagem/criatura. A segunda positiva (Princess Bento) tem o nome, mas é casa de **2D** — isso está medido, não suposto, e está explicado na seção 4.

---

## 0. Método — e a correção que barateia as próximas rodadas

**Não foi preciso navegador.** A lição gravada no `tt_ids.js` ("headless não monta a lista de departamentos") levou a assumir que só um Chrome com Xvfb lê o menu. **Isso é falso para o que interessa aqui:** o HTML **servido** do `/connect` já traz os departamentos **e** os cargos, e cada cargo carrega o atributo `data-for-department` com o ID do departamento dono. Um `curl` resolve tudo.

Antes de confiar nisso, validei contra os **dois controles que já tinham medida na campanha**:

| Controle | O que já se sabia | O que o `curl` + parser devolveu | Bate? |
|---|---|---|---|
| `mindark` | departamento `Character Art` = **164025** | `DEPARTAMENTO 164025 "Character Art"` | **sim** |
| `goals` | cargo `Character Art` = **873551** | `CARGO 873551 "Character Art"`, dentro do dep. `Art` 124153 | **sim** |

Os dois IDs saíram exatos. Só então varri os 15.

Cada verdicto negativo passou por **duas checagens independentes**: o parser (que só olha rótulos de `<label>` de departamento e cargo) e um `grep` cru das 14 palavras-chave no arquivo inteiro. Os dois concordaram nos 14 slugs. A divergência útil apareceu na `princessbento`, onde o `grep` cru acusou `material` e o parser não: era texto de privacidade ("audition **material**s"), não rótulo de menu. O parser estava certo; registro isso porque mostra que o filtro por rótulo é o que vale.

O parser validado ficou em `automacao/tt_menu.py`. Uso: `python3 automacao/tt_menu.py <arquivo.html>`.

`pgrep -c chrome` foi 0 no começo e 0 no fim. **Nenhum navegador foi aberto nesta rodada.**

---

## 1. Tabela dos 15

`D` = departamentos, `C` = cargos. IDs completos na seção 3 (positivas) e no anexo (negativas).

| # | slug | menu lido | personagem? | veredito |
|---|---|---|---|---|
| 1 | **capsulestudio** | 12 D / 37 C | **SIM** | **ENFILEIRAR.** Dep. `CHARACTER` + 4 cargos de personagem/criatura. Estúdio de animação **3D**, Paris |
| 2 | captureage | 6 D / 18 C | NÃO | Cai. Art tem só `2D Artist`, `3D Artist`, `Art director` — nada de personagem |
| 3 | goodgamestudios | 17 D / 0 C | NÃO | Stillfront. Só `Game Art`, sem cargos. Ver ressalva de grupo (seção 5) |
| 4 | houseofhow | 9 D / 11 C | NÃO | Cai. O dep. `Design` só tem `UX/UI`; os cargos vivos são vendas, marketing e suporte |
| 5 | keplerinteractive | 16 D / 0 C | NÃO | Cai. Departamentos são publisher e estúdios do portfólio (Sloclap, Shapefarm, Ebb); `Creative` é genérico e sem cargos |
| 6 | **liquidswords** | **não lida** | **desconhecido** | Borda medida, **não gastei navegador** (instrução). Ver seção 6 |
| 7 | newmoonproduction | 17 D / 0 C | NÃO | Stillfront, template idêntico. Ver seção 5 |
| 8 | ofmstudios | 17 D / 0 C | NÃO | Stillfront, template idêntico. **Zero vagas abertas.** Ver seção 5 |
| 9 | opusmajor | 9 D / 0 C | NÃO | Cai. `Art Team` genérico, sem cargos |
| 10 | **princessbento** | 10 D / 45 C | **SIM (com ressalva grave)** | Nome existe (`Character Layout`, `Character Artist`), mas a casa é **2D**. Ver seção 3.2 |
| 11 | rawfury | 8 D / 27 C | NÃO | Cai. Publisher: o mais perto é `Freelancer - 3D Artist` (121776) e `Graphic Artist` (121772). Sem arte interna de personagem |
| 12 | stillfrontgroup | 19 D / 0 C | NÃO | Holding do grupo, não estúdio. Ver seção 5 |
| 13 | swiftgames | 5 D / 9 C | NÃO | Cai. `Art` tem **um** cargo: `2D Artist` (708468). Mobile |
| 14 | tapnation | 5 D / 0 C | NÃO | Cai. Departamentos são Monetization/UA, Product, Tech, WEB 3.0, Business Support. **Não existe departamento de arte** |
| 15 | territorystudio | 15 D / 0 C | NÃO | Cai para personagem. Tem `VFX`, `Motion`, `Gaming`, `XR/Realtime`, mas nenhum cargo e nenhum nome de personagem — é motion design, como a reconciliação suspeitava |

**12 das 14 lidas não têm absolutamente nada de personagem no menu.** A leitura rápida da reconciliação estava certa no geral, e a rodada confirma isso com número: o universo Teamtailor para personagem está mesmo perto do fim. O que ela **não** tinha visto é a Capsule Studio, que é o achado.

---

## 2. As que têm nome de personagem — dossiê para disparo

### 2.1 CAPSULE STUDIO — a aposta da rodada

| Campo | Valor |
|---|---|
| slug | `capsulestudio` |
| porta do Connect | `https://career.capsule.studio/connect` (o `https://capsulestudio.teamtailor.com/connect` redireciona para lá, HTTP 200) |
| o que é | **Estúdio de animação 3D.** Descrição do próprio site: *"Capsule is a 3D animation studio that tell stories inside digital worlds"* — game trailers, cinematics, comerciais, VR. CG, full CG, VFX |
| onde | **Paris, França** (schema.org da vaga aberta: `addressLocality: Paris`, `addressCountry: FR`) |
| site em | francês (a vaga aberta está em francês) |
| vagas abertas | **1**, e **não é de arte**: `Assistant de production`. **Portanto a rota é o Connect (banco de talentos), não uma vaga** |
| captcha | **nenhum** — varri `captcha`, `recaptcha`, `hcaptcha`, `turnstile`, `datadome`, `sitekey`: zero ocorrências |
| recibo na caixa | **nenhum** — rota livre |

**Por que esta casa importa:** o menu não tem só o nome "character" solto. Tem um **departamento inteiro** de personagem, com a cadeia de produção 3D completa ao lado (mocap, blendshapes, grooming, CFX, matchmove, lighting). É o perfil do Vini quase literalmente.

**IDs exatos a marcar:**

```
DEPARTAMENTO   78709   CHARACTER
  cargo       195207   Character Artist              <-- ALVO PRINCIPAL
  cargo       195208   Character Blendshapes Artist
  cargo       195235   Character Grooming Artist
  cargo       195673   Creature Artist
```

Segunda opção, em outro departamento:

```
DEPARTAMENTO   78704   CREATIVE DEVELOPMENT
  cargo       195190   Character Designer
```

Menu completo da casa, para contexto (12 departamentos, 37 cargos):

| Dep. ID | Departamento | Cargos (ID) |
|---|---|---|
| **78709** | **CHARACTER** | **Character Artist (195207)**, **Character Blendshapes Artist (195208)**, **Character Grooming Artist (195235)**, **Creature Artist (195673)** |
| 78704 | CREATIVE DEVELOPMENT | **Character Designer (195190)**, Concept Artist / Matte Painting (195204), Environment Designer (195203), Scriptwriter (195188), Storyboard Artist (195189) |
| 78720 | ANIMATION & RIGG | Key Frame Animator (195239), Mocap Editor (195237), Mocap Facility (195236), Setup / Rigg (195238) |
| 78721 | ENVIRONMENT | Environment Artist (195240), Generalist (195245) |
| 78722 | EFFECTS | CFX Artist (196967), FX Artist (195241) |
| 78723 | LIGHTING & COMPOSITING | Compositor (195243), Lighting Artist (195242), Matchmove Artist (195246), Motion Designer (195244) |
| 78705 | EDITORIAL & CAMERA | Camera Artist (195206), Editor (195205) |
| 78724 | SOUND & MUSIC | Music Composer (195247), Sound Designer (195248) |
| 78725 | TALENT | Casting Director (195249), Mocap Talent (195252), Voice Director (195250), Voice Talent (195251) |
| 78726 | ADMINISTRATION & MANAGEMENT | Accounting (195269), Business Developer (195255), Human Ressources (195268), Office Manager (195253), Production Coordinator (195254) |
| 78731 | TD / IT | It Manager (195272), Network & Security (195270), Software Development (195271) |
| 169748 | STAGE | (sem cargos) |

**Campos do primeiro passo do Connect** (nome do campo e formato, nunca o valor):

| Campo | Tipo | Obrigatório |
|---|---|---|
| `candidate[email]` | email | sim |
| `candidate[consent_given]` | checkbox (consentimento GDPR) | sim |
| `candidate[department_id]` | radio — marcar **78709** | — |
| `candidate[role_id]` | radio — marcar **195207** | — |
| `authenticity_token`, `ctoken`, `city` | hidden, preenchidos pela própria página | — |

Sem captcha. O passo seguinte (perfil, CV, portfólio) vem depois do e-mail, como nas outras Teamtailor da campanha.

### 2.2 PRINCESS BENTO — o nome existe, mas leia a ressalva antes de gastar

| Campo | Valor |
|---|---|
| slug | `princessbento` |
| porta | `https://careers.princessbento.com/connect` (HTTP 200) |
| onde | **South Melbourne, Austrália** |
| vagas abertas | **4 — e todas as quatro dizem "2D" no título** |
| recibo na caixa | nenhum — rota livre |

As quatro vagas abertas, textualmente: `2D Rigged Animators`, `EOI - 2D Animation Directors`, `EOI - 2D Episodic Directors`, `EOI - 2D Art Directors`.

**A ressalva:** o menu tem os nomes, mas em animação 2D `Character Layout` é função de layout de cena 2D e `Character Artist` sob `Design` é design de personagem 2D — **não é modelagem 3D de personagem**. O resto do menu confirma a leitura: `Storyboards`, `Retakes`, `Scene Assembly`, `Compositing`, `Animator (hand drawn)`. É pipeline de série animada 2D. Para um Senior 3D Character Artist isso é **fora de disciplina**, e a chance de leitura como candidatura desalinhada é real.

**Recomendação honesta: não disparar.** Se você quiser mandar assim mesmo — a casa é boa e o nome bate —, os IDs são:

```
DEPARTAMENTO  488906   Character Layout
  cargo      1240655   Character Layout Artist
  cargo      1240653   Character Layout Lead
  cargo      1240654   Character Layout Supervisor

DEPARTAMENTO  488901   Design
  cargo      1240636   Character Artist        <-- o mais próximo do perfil
```

---

## 3. Gamecan e Mino Games

Aqui a reconciliação de 11/09 (seção 4c) precisa de **duas correções**, e nenhuma delas é boa notícia.

### 3.1 Gamecan — a porta É Teamtailor, e está quebrada

| Campo | Medida |
|---|---|
| porta real hoje | `https://gamecan.eu/career/` (HTTP 200; `gamecan.eu/careers` dá 404) |
| ATS | **Teamtailor** — a página de carreira linka `https://careers.gamecan.eu/connect` |
| **correção da reconciliação** | A 4c diz *"404 no Teamtailor, a porta deles é gamecan.eu/career, não Teamtailor"*. **Está errado.** A Gamecan **usa Teamtailor**, num domínio próprio. O que 404 é só o slug nu `gamecan.teamtailor.com` — testei também `gamecanou`, `gamecangames`, `gamecan-ou`, `gamecanstudio`: todos 404 |
| **estado da porta** | **inacessível desta sessão.** `curl` falha com *"no alternative certificate subject name matches target host name 'careers.gamecan.eu'"* em 3 tentativas; `WebFetch` devolve **HTTP 503**. Não desabilitei verificação TLS |
| vagas de arte/personagem | **nenhuma.** A seção "Job openings" da página não lista uma única posição. O texto é *"We are looking for new talent who resonates with our values! If you didn't find a suitable position, please connect with us"* — ou seja, só banco de talentos |
| captcha | **nenhum** na página de carreira (varri `captcha`, `recaptcha`, `hcaptcha`, `turnstile`, `datadome`, `sitekey`: zero) |
| campos do formulário da página | É um **contato genérico** de WordPress (Fluent Forms), **não um formulário de candidatura**: `input_text` (texto, obrigatório), `email` (email, obrigatório), `message` (textarea, obrigatório), mais `_fluentform_1_fluentformnonce` e `_wp_http_referer` (hidden) e `item_1__fluent_sf` (campo-armadilha anti-robô) |
| canal alternativo | há um `mailto:` para o endereço `info@` do domínio deles na página |

**Veredito:** a única porta de candidatura da Gamecan é o Connect do Teamtailor, que **não abre daqui**. O falhanço é idêntico em classe ao da `liquidswords` (`careers.liquidswords.com`) — os dois são domínios próprios de Teamtailor e os dois quebram no nome do certificado. **É borda deles/da rota, não erro de execução.** Como não há vaga aberta nenhuma, o custo de esperar é baixo.

### 3.2 Mino Games — a casa tem três portas e duas estão mortas

| Campo | Medida |
|---|---|
| domínio | `minogames.com` **falha TLS** (`tlsv1 alert internal error`); **`www.minogames.com` funciona** (HTTP 200). Use sempre o `www` |
| site | Webflow |
| porta que o site anuncia #1 | `https://jobs.lever.co/minogames` → **HTTP 404**. A API da Lever confirma: `{"ok":false,"error":"Document not found"}` |
| porta que o site anuncia #2 | `https://minogames.teamtailor.com/` e `/connect` → **HTTP 404** |
| terceira porta, no JS da página | a página chama `https://api.teamtailor.com/v1/jobs` com um bearer token embutido no cliente. Testei: **HTTP 401**. Token revogado |
| **porta real e viva hoje** | **Workable** — `https://apply.workable.com/mino-games/` (HTTP 200, título *"Mino Games - Current Openings"*) |
| **vagas abertas** | **ZERO.** A API oficial do widget (`apply.workable.com/api/v1/widget/accounts/mino-games`) devolve `{"name":"Mino Games","description":null,"jobs":[]}` |
| campos do formulário | **não há formulário para ler** — no Workable o formulário é por vaga, e não existe vaga. Nada de candidatura espontânea |
| captcha | o bundle da página do Workable referencia `captcha`, `recaptcha`, `turnstile` e `sitekey`. Ou seja: **quando houver vaga, espere captcha** — ao contrário da Capsule e da Gamecan |

**Veredito: Mino Games cai.** Não é questão de ajuste de rota: não existe vaga aberta e não existe porta de candidatura espontânea. A página de carreira deles está desatualizada em três lugares ao mesmo tempo.

> **Nota de higiene, sem valor registrado:** a página pública da Mino expõe no JS do cliente um *bearer token* da API do Teamtailor. Ele está revogado (401), então não há risco ativo, e **não registrei o valor dele em lugar nenhum** — menciono só porque é o tipo de coisa que explica por que a listagem de vagas do site deles não carrega mais.

---

## 4. O que cai, e por quê

**12 das 14 casas lidas não têm uma única palavra de personagem no menu — 86%.** Não vou suavizar: esta rodada é, em quase toda a sua extensão, negativa. E somando as duas casas da seção 3, **o saldo real da rodada é UMA candidatura** (Capsule Studio), possivelmente duas se você aceitar a Princess Bento fora de disciplina.

Os motivos da queda, agrupados pelo que a medida mostrou:

**Sem departamento de arte nenhum (1):** `tapnation` — Monetization & UA, Product, Tech, WEB 3.0, Business Support. Publisher mobile puro, como a reconciliação suspeitava.

**Arte existe, mas é 2D/genérica (4):** `swiftgames` (o departamento `Art` tem exatamente um cargo, `2D Artist`), `captureage` (`2D Artist`, `3D Artist`, `Art director` — o `3D Artist` é o mais perto que chega), `houseofhow` (o `Design` só tem `UX/UI`), `opusmajor` (`Art Team` sem nenhum cargo).

**Publisher sem arte interna (2):** `rawfury` — o melhor que tem é `Freelancer - 3D Artist` (121776), o que confirma que arte ali é terceirizada; `keplerinteractive` — os departamentos são as próprias empresas do portfólio (Sloclap, Shapefarm, Ebb Software), não disciplinas.

**Motion design, não personagem (1):** `territorystudio` — tem `VFX`, `Motion`, `Gaming`, `XR/Realtime`, `Compositing`, e **zero cargos** em qualquer um deles.

**Stillfront, template corporativo compartilhado (4):** `goodgamestudios`, `newmoonproduction`, `ofmstudios`, `stillfrontgroup` — todos com `Game Art` e nenhum cargo. Seção 5.

**Não lida (1):** `liquidswords`. Seção 6.

---

## 5. Ressalva de grupo — Stillfront. E o grupo é maior do que se pensava

**Correção do briefing:** a ressalva falava em **três** slugs do grupo (`stillfrontgroup`, `newmoonproduction`, `ofmstudios`). **São quatro.** A `goodgamestudios` também é Stillfront, e não por palpite:

- Os três — `goodgamestudios`, `newmoonproduction`, `ofmstudios` — têm o **conjunto de nomes de departamento byte-a-byte idêntico** (os mesmos 17 nomes; só os IDs numéricos diferem, porque cada conta tem os seus). Comparei os conjuntos: iguais.
- A `stillfrontgroup` tem **os mesmos 17 + 2** (`Ad monetization`, `Payment Operations & Fraud`) — é a holding.
- A palavra "Stillfront" aparece no HTML do Connect das quatro (3, 3, 9 e 17 ocorrências). Nas outras 10 casas da lista: zero.

Somando a `twinharbour`, que já recebeu candidatura em **06/09** (linha 517 do `enviados.csv`, e o recibo na caixa diz textualmente *"Thanks for applying for the Unsolicited Application – Twin Harbour Interactive"*, além de um e-mail cujo assunto é *"a proud member of Stillfront"*), enfileirar as quatro daria **cinco candidaturas ao mesmo guarda-chuva em seis dias**. Isso não lê como campanha, lê como script.

### Recomendação: UMA, e é a `goodgamestudios`

**Por quê:** é a única das quatro com qualquer vaga de arte viva. Vagas abertas medidas hoje:

| slug | vagas abertas | tem alguma de arte? |
|---|---|---|
| **goodgamestudios** | várias, incluindo `ai-artist-empire` e `senior-marketing-video-artist` | **sim, duas** |
| stillfrontgroup | várias (data, legal, QA, freelance de suporte) | não — e é holding, não estúdio |
| newmoonproduction | 2 (`product-owner`, `unity-developer`) | não |
| ofmstudios | **zero** | não |

A `ofmstudios` cai sozinha por não ter vaga nenhuma. A `stillfrontgroup` cai por ser sede corporativa. A `newmoonproduction` cai por não ter arte aberta. Sobra a Goodgame, que é a maior, tem `Game Art` de verdade e produção interna em Hamburgo.

**Mas seja avisado, porque o número não mente:** nem a Goodgame tem nome de personagem no menu, e as duas vagas de arte dela são `AI Artist` e `Marketing Video Artist` — nenhuma das duas é personagem. É uma entrada espontânea de **valor baixo**. **Mandar nenhuma das quatro é uma decisão defensável**, e eu diria até preferível se a sua prioridade nesta semana é proteger o sinal da campanha depois da Twin Harbour. Se for mandar uma, mande a Goodgame e só ela.

---

## 6. Liquid Swords — o que já se sabe, sem gastar navegador

Conforme a instrução, **não gastei navegador nela**. Registro o que a medida barata mostrou:

- `https://liquidswords.teamtailor.com/connect` responde **301** e redireciona para `https://careers.liquidswords.com/connect`.
- O domínio próprio falha com **erro de nome de certificado** (`no alternative certificate subject name matches target host name 'careers.liquidswords.com'`) — o mesmo sintoma, exato, da `careers.gamecan.eu`.
- Isso é consistente com o **Fastly 421 já medido** e já está na mão do Vini.
- **Portanto o menu dela continua desconhecido.** Não sei se a Liquid Swords tem nome de personagem no Connect. Ela é a única das 15 sem veredito, e é justamente a mais promissora no papel (action-RPG open world, Estocolmo, fundada pelo Christofer Sundberg). Quando a borda liberar, ela é a primeira a reler — e o `curl` resolve, não precisa de navegador.

---

## 7. Dedupe — método novo, feito na caixa de entrada

Segui a regra: **a fonte de verdade é o recibo**, não o nome no CSV.

Consultei o Gmail por `from:<slug>.teamtailor-mail.com` para **todos os 15 slugs** e para `gamecan` e `minogames`. **Resultado: zero threads.** Todas as rotas estão livres.

**E provei que a consulta funciona antes de confiar no vazio** — que é exatamente onde o método antigo falhou. Rodei a mesma forma de consulta contra três slugs com recibo conhecido (`mindark`, `goals`, `twinharbour`) e ela devolveu **5 threads**, incluindo o *"Welcome to MindArk!"* de 11/09 e o *"Twin Harbour Interactive: We've received your application!"* de 06/09. A consulta está boa; o vazio é vazio de verdade, não consulta quebrada.

Cruzamento secundário no `enviados.csv` (por nome, sabendo que é método fraco): das 17 casas conferidas, a única linha que aparece é a 517, da Twin Harbour. Nenhuma menção a Capsule, Princess Bento, Gamecan ou Mino Games em `enviados.csv` nem em `alvos.csv`.

---

## 8. Para você disparar amanhã — em ordem

1. **Capsule Studio** — `https://career.capsule.studio/connect` → departamento **78709** (`CHARACTER`) → cargo **195207** (`Character Artist`). Sem captcha. Rota livre. **É a rodada inteira num alvo só.**
2. *(opcional, valor baixo)* **Goodgame Studios** — `https://goodgamestudios.teamtailor.com/connect` → departamento **309870** (`Game Art`). Sem cargos para marcar. Uma só do grupo Stillfront, e só se você quiser gastar.
3. *(opcional, fora de disciplina)* **Princess Bento** — `https://careers.princessbento.com/connect` → departamento **488901** (`Design`) → cargo **1240636** (`Character Artist`). Casa de 2D; minha recomendação é não.

**Não disparar:** Mino Games (sem vaga e sem porta), Gamecan (porta fora do ar, sem vaga), Liquid Swords (porta fora do ar, menu desconhecido), e as outras 11.

---

## Conferência aritmética

```
15 slugs na fila limpa da reconciliacao
 -1 nao lida (liquidswords, borda de certificado)
=14 menus lidos
    -2 com nome de personagem     capsulestudio, princessbento
   -12 sem nada de personagem
     = 0  ✓

dos 2 positivos:
    1 casa 3D  (capsulestudio)  -> ENFILEIRAR
    1 casa 2D  (princessbento)  -> fora de disciplina

2 casas fora do Teamtailor conferidas:
    gamecan     -> na verdade E Teamtailor (dominio proprio), porta fora do ar, 0 vagas
    minogames   -> Workable vivo, 0 vagas, sem candidatura espontanea
    = 0 candidaturas possiveis  ✓

recibos encontrados para os 17 slugs conferidos: 0
navegadores abertos: 0
```
