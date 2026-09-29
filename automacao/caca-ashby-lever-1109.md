# CAÇA ASHBY · LEVER · PERSONIO — candidatura espontânea, 11/09/2026 (noite)

Tudo por `curl` e pelas **APIs públicas** das três famílias. **Nenhum navegador foi aberto,
nada foi enviado, nenhum formulário foi preenchido, nenhum email foi mandado.** A entrega é
fila pronta com dossiê; quem clica é o Vini.

Não toquei em `enviados.csv` nem em `docs/index.html`. Criei este arquivo e acrescentei
**uma** linha em `automacao/processados.csv`.

Lido antes de começar: `BRIEFING.md`, `automacao/BRIEF-JHON.md`,
`automacao/rotas-espontaneas-1109.md` (formato desta entrega),
`automacao/caca-workday-1109.md` (para não repetir o Workday),
`automacao/caca-ashby-bamboo-gohire-0909.md` (a varredura anterior de Ashby e Lever) e
`automacao/caca-personio-0909.md`.

---

## 1. PLACAR — os números medidos, antes de qualquer narrativa

| Família | Rota sondada | Sondagens | Quadros vivos | Anúncios lidos | Anúncios espontâneos | Inquilinos com rota | Passaram escopo + disciplina | Dedupe limpo | **Na fila** |
|---|---|---|---|---|---|---|---|---|---|
| **Ashby** | `api.ashbyhq.com/posting-api/job-board/<slug>` | **21.420** | **185** | **2.408** | **19** | **15** | 5 | 3 | **3** |
| **Lever** | `api.lever.co/v0/postings/<slug>?mode=json` | **21.420** | **59** | **1.131** | **40** | **15** | 9 | 3 | **3** |
| **Personio** | `HEAD <slug>.jobs.personio.com/` + `/search.json` | **21.208** | **121** (90 reais, 31 de modelo) | **356** | **53** brutos, **23** em quadro real | **21** | 4 | 1 | **1** |
| **SmartRecruiters** | sonda de DataDome | **12** | 6 | — | — | — | — | — | **0** (§9) |
| **TOTAL** | | **~64.100 requisições** | **365 quadros** | **3.895 anúncios** | **112 brutos, ou 82 descontando os 30 do quadro-modelo do Personio (§7)** | **51 inquilinos** | **18** | **7** | **7 rotas na fila** |

**Quebra que o Vini pede (regra de 10/09): das 7 rotas da fila, 7 são PORTA ESPONTÂNEA
genérica — nenhuma é anúncio de ambiente.** Duas delas caem direto em departamento de arte
(`Art` na thatgamecompany, `Art & Design` na Stratosphere Games). **Nenhuma candidatura foi
enviada nesta rodada, por regra do enunciado.**

### 1.1 O PLACAR DE CAPTCHA, que é o resultado mais útil da rodada

| Família | O que o HTML servido mostra | Veredito medido | Rotas medidas |
|---|---|---|---|
| **Personio** (`/job/<id>/apply`) | Formulário **inteiro no HTML**: `first_name`, `last_name`, `email`, `phone`, `location`, `available_from`, `salary_expectations`, `documents.cv`, `documents.cover-letter`, `documents.work-sample`, `documents.other` e os `custom_attribute_*` da casa | **SEM CAPTCHA NENHUM.** Busca por `captcha`, `recaptcha`, `hcaptcha`, `turnstile`, `friendlycaptcha`, `datadome`, `perimeterx`, `akamai`, `botd`, `challenge`, `honeypot`, `sitekey` e `cloudflare`: **ZERO ocorrência** | **4 de 4** |
| **Ashby** (`/application`) | Casca de SPA de 15 a 36 KB, **zero campo de formulário** | **reCAPTCHA v2 invisível.** `window.__appData.recaptchaPublicSiteKey` = `6LeFb_YUAAAAALUD5h-BiQEp8JaFChe0e0A6r49Y` — **a mesma chave em todos os inquilinos**, é chave de plataforma | **6 de 6** |
| **Lever** (`/apply`) | Página cheia, 724 a 773 KB, formulário inteiro no HTML | **hCaptcha ATIVO**: `hcaptcha.render` com sitekey `e33f87f8-88ec-4e1a-9a13-df9bbb1d8120` e `hcaptcha.execute` amarrado ao `#btn-submit`, **mais** `cdn-cgi/challenge-platform/scripts/jsd/main.js` (Cloudflare) | **8 de 8** |

**Tradução prática: a lane que o enunciado pediu existe, e ela é o PERSONIO.** É a única das
três em que o formulário vem servido e sem porteiro. Ashby e Lever têm rota espontânea de
sobra, mas **as duas são clique dele, no navegador dele.**

E os dois vereditos de parede **não são teoria**: a chave do Ashby é exatamente a que esta
campanha mediu **com clique** em 07/09 na Stellar Entertainment, quando o envio voltou com
*"Your application submission was flagged as possible spam"*; e o hCaptcha do Lever é o mesmo
muro que já barrou Larian, Frontier, Asobo, Behaviour, Skydance, Avalanche, Jam City, Kabam e
Blackbird nesta campanha, com o quadro de imagem aparecendo na tela.

### 1.2 A armadilha do meu próprio método, e ela quase virou erro escrito

O primeiro `grep` por `recaptcha` no HTML do Ashby achou **uma** ocorrência, e ela era lixo: a
string `MigrateGoogleRecaptchaAutomatedLegal`, nome de um *feature flag* numa lista de flags.
Se eu tivesse parado ali, teria escrito **"Ashby sem sinal de captcha"**, que é falso — e essa
frase teria mandado a automação bater de novo na mesma parede que já reprovou o IP dela em
07/09. O que resolveu foi **abrir o `window.__appData` inteiro** em vez de grepar a palavra.

**Regra que sai daí, e ela vale para toda rodada futura: em página de SPA, "a palavra captcha
não aparece no HTML" NÃO é medição. Medição é abrir o objeto de configuração.** É a mesma
razão pela qual eu me recuso a concluir ausência de DataDome no SmartRecruiters (§9).

---

## 2. O QUE ESTA RODADA NÃO REFEZ, e por quê

- **Não repeti o Workday.** `automacao/caca-workday-1109.md` o varreu hoje: 1.942 slugs
  inéditos, 29.130 sondagens, **zero personagem**.
- **Não repeti Teamtailor, Recruitee, Pinpoint nem Homerun.**
  `automacao/rotas-espontaneas-1109.md` fechou os quatro hoje.
- **Não refiz a varredura de disciplina do Ashby e do Lever de 09/09.** A de 09/09 procurava
  **vaga aberta** (3.230 slugs, 35 quadros Ashby, 19 Lever, 2 linhas de fila). Esta procura
  outra coisa: o **anúncio de candidatura espontânea**. São recortes diferentes no mesmo
  universo, e é por isso que esta achou 19 e 40 rotas que aquela não listou — ela não estava
  procurando por elas.
- **Não refiz a varredura de slug do Personio de 09/09** como ela foi feita (2.889 variantes de
  nome). Rodei o universo novo desta rodada, que é sete vezes maior, e o rendimento subiu de
  **52 para 121 inquilinos vivos**.
- **Não varri SmartRecruiters em volume.** O enunciado condiciona isso a medir ausência de
  DataDome, e o que eu medi (§9) não permite afirmar ausência.

---

## 3. COMO EU MULTIPLIQUEI O UNIVERSO DE SLUG — e o número que prova que valeu

| Passada | Fonte de nome | Slugs | Quadros Ashby |
|---|---|---|---|
| 1ª | `alvos.csv`, `drafts/` e os arrays de `docs/index.html` | 2.443 | 38 |
| 2ª | **+** `pessoas.csv`, **+** coluna `token` dos dois `censo-boards-*.csv`, **+** todo nome próprio em texto corrido de `docs/index.html`, `backlog-estudios.md` e `FILA-DO-VINI.md`, **+** todo slug de host de ATS já citado no repositório | 15.839 | 161 |
| 3ª | **+ o segundo nível de TODO domínio citado no repositório** — 7.521 domínios colhidos de `alvos.csv`, `pessoas.csv`, `enviados.csv`, `dominios-sem-email.csv`, `garimpo-cgstudiomap.csv` e das filas do gamedevmap | **21.420** | **185** |

**A terceira passada é a que merece ficar escrita.** Ela sozinha acrescentou **5.248 slugs
inéditos** e **24 quadros Ashby novos**, entre eles **VRChat, Kolibri Games, Improbable,
Immutable, Poki e Colonist** — nenhum deles sai do nome do estúdio como a campanha o escreve,
**todos saem do domínio**. O registro de 30/08 no `processados.csv` ("chute de slug não
descobre nada") continua verdadeiro; o que este número acrescenta é **qual lista não é chute**:
**domínio já conhecido é a melhor semente de slug que este repositório tem**, melhor até que a
lista de nomes.

---

## 4. FILA FINAL NUMERADA — 7 rotas

Ordem: encaixe de personagem primeiro, depois porte da casa, depois confiabilidade da rota.
**Em todas: escopo conferido, disciplina conferida, `dedupe-agora.sh` rodado com OS DOIS
argumentos, régua de veto passada no texto integral do anúncio.**

> **A #2 é a única das sete que NÃO precisa do navegador dele.** As três do Ashby têm
> reCAPTCHA v2 invisível e as três do Lever têm hCaptcha com desafio de imagem — as seis são
> clique dele. Se a rodada de envio só tiver fôlego para uma automática, é a #2.

---

### 1. thatgamecompany — `General - Art` — o melhor encaixe da rodada

- **Por que a casa presta:** estúdio de *Journey*, *Flower* e *Sky: Children of the Light*.
  Personagem estilizado sem rosto, que atua por silhueta — o `processados.csv` de 31/08 já
  escreveu que é *"o encaixe mais preciso da campanha"*. E este anúncio não é balcão genérico:
  é o balcão do **departamento de Arte** (`department: Art`, `team: Art`).
- **URL exata:** `https://jobs.ashbyhq.com/thatgamecompany/ea5b0730-cb40-4e87-a0dd-f9d43f96ec3f/application`
- **ID da requisição:** `ea5b0730-cb40-4e87-a0dd-f9d43f96ec3f`
- **Local:** `Remote - US`; endereço da requisição: Los Angeles, Califórnia, Estados Unidos.
  Publicada em **05/06/2024**, ainda listada (`isListed: true`).
- **Medido:** **HTTP 200**, **15.455 bytes**.
- **Sinal de captcha no HTML:** `recaptchaPublicSiteKey = 6LeFb_…r49Y` **presente**;
  `hcaptcha.render` = 0; Cloudflare = 0 → **reCAPTCHA v2 invisível**.
- **Campos do formulário conferidos:** o HTML servido é casca de SPA e **não traz um campo
  sequer** (medido: zero `<input>` de formulário; a definição vem por GraphQL depois do
  render, e a introspecção do endpoint está desligada — §10.1). O que esta campanha **já
  mediu com clique** nesta família (dossiê da Stellar em `automacao/respostas-formularios.md`):
  **Name**, **Email**, **Resume** (arquivo), **Cover letter** (arquivo, opcional),
  **Location** (autocomplete, se aparecer) e **consentimento**, sem perguntas customizadas.
  **Armadilha já documentada:** o board abre na aba *Overview* e o formulário só existe depois
  de clicar na aba *Application*.
- **Texto integral do anúncio** (são 160 caracteres, cabem inteiros): *"GENERAL - ART — This is
  for general ART position applicants that don't fall in the categories of our current
  openings. Please apply here, thank you!"*
- **Régua de veto neste anúncio: ZERO acertos** de `authoriz`, `eligib`, `sponsor`,
  `work permit`, `must be based`, `reside`, `relocat`, `only`.
- **Dedupe:** `sh automacao/dedupe-agora.sh ea5b0730-cb40-4e87-a0dd-f9d43f96ec3f "thatgamecompany"`
  → **seção 1: nenhuma ocorrência nos quatro arquivos (ID inédito). Seção 2: nenhuma marca de
  envio. Seção 3 devolveu duas linhas, e as duas importam:** `processados.csv` —
  *"thatgamecompany 36e101a4 tem veto escrito literal: Applicants must be authorized to work
  for any employer in the U.S or Canada"*; `index.html` — *"o veto de residencia que derrubou
  thatgamecompany"*.
- **LEIA ISTO ANTES DE CLICAR — é a única ressalva séria desta linha.** A casa **já recebeu
  uma candidatura** desta campanha: a *3D Character Artist (Mid-Senior)*, enviada à mão em
  31/08 e confirmada pelo Ashby (`no-reply@ashbyhq.com`, 31/08). Em 05/09 a campanha rebaixou
  a requisição irmã `36e101a4` por **veto escrito** de autorização de trabalho. A `ea5b0730` é
  requisição **diferente**, de departamento e não de vaga, e **não repete o texto do veto** —
  pela régua do briefing (só veto escrito no anúncio desqualifica) ela **fica na fila**. Mas é
  a **segunda batida na mesma porta em onze dias**, e quem decide o desgaste é você.
- **Precisa de navegador? SIM.** reCAPTCHA de sessão.

### 2. Stratosphere Games — `Initiative Application` — ⭐ A ÚNICA ROTA SEM CAPTCHA DA RODADA

- **Por que a casa presta:** estúdio de **Berlim**, 40 pessoas, e o próprio anúncio diz de onde
  vem o time: *"Our team is made up of experts from renowned companies like **Splash Damage and
  Rocksteady**"*, produzindo *"AAA-standard games for mobile platforms and beyond"*. Pedigree de
  Rocksteady é pedigree de personagem. **E o anúncio está classificado no departamento
  `Art & Design`** — não é balcão de RH, é a porta da arte.
- **URL exata:** `https://stratosphere-games.jobs.personio.com/job/1318003/apply`
  (página do anúncio: `https://stratosphere-games.jobs.personio.com/job/1318003`)
- **ID da requisição:** `1318003`
- **Local:** Berlim, Alemanha. `Full or part-time`, `Permanent employee`,
  *"A mixture of office and remote work"*.
- **Medido:** anúncio **HTTP 200 / 69.508 bytes**; formulário **HTTP 200 / 72.380 bytes**.
- **Sinal de captcha no HTML: ZERO.** Busca por `captcha`, `recaptcha`, `hcaptcha`,
  `turnstile`, `friendlycaptcha`, `datadome`, `perimeterx`, `akamai`, `botd`, `challenge`,
  `honeypot`, `sitekey` e `cloudflare` no HTML do `/apply`: **nenhuma ocorrência de nenhum
  deles**.
- **Campos do formulário conferidos — e estes foram lidos no HTML servido, não presumidos:**
  `first_name`, `last_name`, `email` (obrigatório), `phone`, `available_from` (obrigatório),
  `salary_expectations`, `location`, mais os anexos `documents.cv`,
  `documents.cover-letter` e `documents.work-sample`. **Nenhum `custom_attribute_*`, ou seja,
  nenhuma pergunta customizada.** **Nenhuma pergunta de autorização de trabalho no
  formulário.** O campo de pretensão salarial existe e é livre — vale a POLÍTICA DE PRETENSÃO
  do briefing (casa média na Alemanha, faixa não publicada).
- **Texto do anúncio:** *"If there is no fitting offer on our job page, please feel free to
  apply initiative. We love pro-active people and are happy to have a look at your documents."*
  **Régua de veto: ZERO acertos** no texto integral.
- **Escopo:** Alemanha. **Dentro do escopo, sem ressalva.**
- **Dedupe:** `sh automacao/dedupe-agora.sh 1318003 "Stratosphere"` → **seção 1: nenhuma
  ocorrência nos quatro arquivos. Seção 2: nenhuma marca de envio. Seção 3: nada.** Por nome:
  `Stratosphere` = **0** em `enviados.csv`, **0** em `alvos.csv`, **0** em `processados.csv`,
  **0** em `docs/index.html`. **Casa 100% nova para a campanha.**
- **Precisa de navegador? NÃO.** Formulário servido inteiro, sem porteiro nenhum medido. É a
  candidatura mais barata desta fila.

### 3. Redly Games — `General Interest - Open Application` — casa nova, porta de arte aberta

- **Por que a casa presta:** estúdio novo com base medida na **Finlândia** (as outras duas
  vagas do quadro, `Senior Server Engineer` e `Senior Game Engineer (Unreal)`, estão marcadas
  *Finland, Remote*), fazendo o **primeiro título: jogo de aventura 3D mobile em Unreal Engine
  5**. O anúncio chama arte pelo nome: *"Whether your background is in engineering, **art**,
  design, production, community, marketing, or other game dev areas — if you believe you could
  help shape what comes next, we'd love to hear from you"*, e fecha com *"Portfolios, work
  samples… are always welcome where relevant"*.
- **URL exata:** `https://jobs.ashbyhq.com/redlygames/3c2a1d1e-5e80-4b4e-895d-f43d0efe4d3b/application`
- **ID da requisição:** `3c2a1d1e-5e80-4b4e-895d-f43d0efe4d3b`
- **Local:** `Global – Remote (EU & Canada preferred)`, `workplaceType: Remote`. Publicada em
  **19/12/2025**, ainda listada.
- **Medido:** **HTTP 200**, **25.605 bytes**.
- **Sinal de captcha no HTML:** `recaptchaPublicSiteKey` **presente** (a chave de plataforma).
  hCaptcha 0, Cloudflare 0.
- **Campos do formulário:** casca de SPA, zero campo no HTML; família Ashby, campos conforme o
  dossiê citado na linha 1.
- **Régua de veto no texto integral (2.839 caracteres): ZERO acertos.** A frase mais próxima de
  restrição é **a favor**: *"We're based across Europe and North America and generally prefer
  overlapping time zones, but **we're open to exceptional candidates globally** depending on
  the role."* Isso é preferência de fuso, não veto de residência.
- **Dedupe:** `sh automacao/dedupe-agora.sh 3c2a1d1e-5e80-4b4e-895d-f43d0efe4d3b "Redly"` →
  **seção 1: nenhuma ocorrência. Seção 2: nenhuma marca de envio. Seção 3: nada.** Por nome:
  `Redly` = **0/0/0/0** nos quatro arquivos. **Casa 100% nova.**
- **Precisa de navegador? SIM.** reCAPTCHA de sessão.

### 4. Jam City — `General Resume Submissions` — departamento de arte 3D provado

- **Por que a casa presta:** 500 pessoas, estúdios em Los Angeles (sede), São Francisco e San
  Diego, jogos narrativos com licença de Hollywood (Harry Potter, Family Guy, Marvel Avengers,
  Futurama). **A prova de pipeline 3D está no próprio quadro:** o anúncio irmão é
  `Principal 3D Generalist` (São Francisco, time `Art/Art`), que pede *"an understanding of the
  whole art pipeline"* e portfólio obrigatório.
- **URL exata:** `https://jobs.lever.co/jamcity/136adc53-aeb8-4598-8a62-de5dc6b0150a/apply`
- **ID da requisição:** `136adc53-aeb8-4598-8a62-de5dc6b0150a`
- **Local:** `ALL Jam City, CA`, `country: US`, `workplaceType: remote`. Criada em
  **02/10/2017** — balcão permanente, não vaga.
- **Medido:** **HTTP 200**, **736.052 bytes**.
- **Sinal de captcha no HTML:** **hCaptcha ATIVO** (`hcaptcha.render`, sitekey
  `e33f87f8-…`) **+ Cloudflare challenge platform**.
- **Campos do formulário conferidos (o Lever serve o formulário inteiro, então estes foram
  lidos de verdade):** `input[name=name]`, `input[name=email]`, `input[name=phone]`,
  `input[name=org]`, `input[name=resume]` (arquivo), `#location-input` com o campo escondido
  `input[name=location]`, `input[name=urls[LinkedIn]]`, `input[name=urls[Portfolio]]`,
  `textarea[name=comments]`, `input[name=h-captcha-response]` (escondido) e `#btn-submit`.
  **Armadilha que já custou uma candidatura inteira nesta campanha e vale de novo aqui:** o
  `#location-input` é **autocomplete estruturado** — só vale se uma **sugestão for escolhida**;
  digitar o endereço inteiro deixa `input[name=location]` vazio e o Submit **não gera POST
  nenhum, sem erro na tela** (está escrito no cabeçalho do `automacao/apply_lever.js`).
- **Régua de veto no texto integral (4.550 caracteres): ZERO acertos.** O texto é convite
  direto: *"Don't see anything on our Job Boards that fits your experience right now but still
  want to apply? Please submit your resume here!"*
- **Dedupe:** `sh automacao/dedupe-agora.sh 136adc53-aeb8-4598-8a62-de5dc6b0150a "Jam City"` →
  **seção 1: nenhuma ocorrência nos quatro arquivos. Seção 2: nenhuma marca de envio. Seção 3
  devolveu duas linhas, e as duas são de OUTRA requisição:** a `Principal 3D Generalist` de São
  Francisco ficou *"preenchida inteira e travou no hCaptcha de imagem do Lever"* e já está na
  fila da mão dele. **A `General Resume Submissions` nunca foi tocada.**
- **Ressalva honesta:** duas portas na mesma casa. Se ele for resolver o hCaptcha, o melhor uso
  da sessão é mandar as duas de uma vez — a `Principal 3D Generalist`, que é vaga de verdade,
  **primeiro**.
- **Precisa de navegador? SIM.** hCaptcha de desafio.

### 5. Stellar Entertainment — `Talent Pool` — Guildford (UK) + Utrecht (NL)

- **Por que a casa presta:** estúdio de Guildford com segundo escritório em Utrecht, projeto
  novo **não anunciado** com meta AAA. Departamento de arte existe e tem peso: o quadro tem
  `Associate Art Director`, `Lead UI Artist` e `Technical Artist` abertos.
- **URL exata:** `https://jobs.ashbyhq.com/stellarentertainment/43711cca-1ec5-40d3-98d7-eeb2740e604d/application`
- **ID da requisição:** `43711cca-1ec5-40d3-98d7-eeb2740e604d`
- **Local:** `Guildford, UK`, `Hybrid`, com Utrecht nos locais secundários. Publicada em
  **19/12/2025**.
- **Medido:** **HTTP 200**, **17.003 bytes**.
- **Sinal de captcha no HTML:** `recaptchaPublicSiteKey` **presente** — e aqui o sinal **não é
  teórico**: este é exatamente o inquilino onde a campanha mediu a parede **com clique** em
  07/09 e levou *"Your application submission was flagged as possible spam"*.
- **Campos do formulário:** os desta casa estão **mapeados campo a campo** em
  `automacao/respostas-formularios.md` (Name, Email, Resume, Cover letter opcional, Location
  autocomplete, consentimento, reCAPTCHA invisível), porque a automação já preencheu o
  formulário inteiro aqui em 07/09.
- **Texto do anúncio:** *"Can't see your dream role? We are always on the look for new talent,
  drop your CV and cover letter into our talent pool below to keep in touch with our
  recruitment team."* **Régua de veto: ZERO acertos.**
- **Encaixe de personagem — e vou ser honesto, é INDIRETO.** As 12 vagas do quadro são de
  engenharia, UI e direção, e a `Senior Vehicle Handling Engineer` mostra que o projeto é de
  **condução**. Não há elenco de personagem anunciado. Entra pela **regra 13** (porta de
  entrada), não por encaixe de conteúdo.
- **Dedupe:** `sh automacao/dedupe-agora.sh 43711cca-1ec5-40d3-98d7-eeb2740e604d "Stellar Entertainment"`
  → **seção 1: nenhuma ocorrência do ID nos quatro arquivos. Seção 2: nenhuma marca de envio.
  Seção 3: uma linha no `docs/index.html`**, e ela é de **outra** requisição, a `2c053416`
  (`Associate Art Director`), registrada como *"A MAO, por reCAPTCHA invisivel de sessao"* —
  ou seja, **preenchida e NÃO enviada**, esperando ele. `Stellar Entertainment` aparece
  **0 vez** em `enviados.csv`. **Nada foi enviado a esta casa ainda.**
- **Ressalva honesta:** duas portas na mesma casa, e a outra é melhor. Se for clicar, a
  `Associate Art Director` (`2c053416`) vem **primeiro**; o Talent Pool é a segunda porta na
  mesma sessão.
- **Precisa de navegador? SIM.** reCAPTCHA de sessão, já reprovado por IP de datacenter aqui.

### 6. VRChat — `General Opportunity` — remoto "Anywhere"

- **Por que a casa presta:** plataforma social de VR cujo **produto é avatar** — mais de
  250.000 mundos, e o catálogo de personagem é o coração do serviço. Levantou USD 100M
  (Makers Fund, Anthos Capital, HTC). O quadro prova departamento de arte vivo:
  `Unity Technical Artist, Event Pipeline`.
- **URL exata:** `https://jobs.lever.co/vrchat/0a24ad44-1335-47ac-9081-b5f9b054f105/apply`
- **ID da requisição:** `0a24ad44-1335-47ac-9081-b5f9b054f105`
- **Local:** `Anywhere`; `country: US`. Criada em **23/01/2024**.
- **Medido:** **HTTP 200**, **748.450 bytes**.
- **Sinal de captcha no HTML:** **hCaptcha ATIVO** + Cloudflare challenge.
- **Campos do formulário conferidos:** os mesmos campos Lever da linha 4 (nome, email,
  telefone, empresa, currículo, localização com autocomplete estruturado, LinkedIn, portfólio,
  comentário, `h-captcha-response` escondido).
- **Texto do anúncio:** *"The General Application is for candidates who believe they'd be an
  amazing fit at VRChat but don't see any open roles that seem right!"*
  **Régua de veto: ZERO acertos.**
- **Encaixe de personagem — honesto:** o produto é avatar, mas **o conteúdo é feito pela
  comunidade**, e hoje não há artista de personagem anunciado no quadro deles. É porta de
  entrada forte por afinidade de produto, não vaga de personagem.
- **Dedupe:** `sh automacao/dedupe-agora.sh 0a24ad44-1335-47ac-9081-b5f9b054f105 "VRChat"` →
  **seção 1: nenhuma ocorrência. Seção 2: nenhuma marca de envio. Seção 3: nada.** Por nome:
  `VRChat` = **0/0/0/0** nos quatro arquivos. **Casa 100% nova.**
- **Precisa de navegador? SIM.** hCaptcha de desafio.

### 7. Kolibri Games — `Open/Speculative Application (f/m/d)` — Berlim

- **Por que a casa presta:** estúdio de Berlim (*Idle Miner Tycoon*), dentro do escopo, e o
  anúncio é o convite mais explícito que esta rodada achou: *"Interested in joining Kolibri
  Games, but don't see the right job posting? We want you to speak up! **Tell us your story,
  write your job description**, and let us know how you would spend your first 90 days."* É a
  regra 13 do briefing convidada pela própria casa.
- **URL exata:** `https://jobs.lever.co/kolibrigames/d2ff05ad-e219-4dd9-985a-825d72bcf671/apply`
- **ID da requisição:** `d2ff05ad-e219-4dd9-985a-825d72bcf671`
- **Local:** `Berlin, Germany`, `country: DE`. Criada em **21/04/2020** — balcão permanente.
- **Medido:** **HTTP 200**, **724.606 bytes**.
- **Sinal de captcha no HTML:** **hCaptcha ATIVO** + Cloudflare challenge.
- **Campos do formulário conferidos:** os campos Lever da linha 4. **Aviso escrito pela própria
  casa, e ele é operacional:** *"We are an international studio, so don't forget to send in
  your application in English."* Inglês é a língua de trabalho — **não é porta condicionada a
  idioma.**
- **Régua de veto: ZERO acertos** no texto integral.
- **Encaixe de personagem — honesto e fraco:** *idle game* mobile, e o quadro atual não tem uma
  única vaga de arte (analista de dados, designer de economia, QA técnico). Entra pela regra
  13, e é última da fila por isso.
- **Dedupe:** `sh automacao/dedupe-agora.sh d2ff05ad-e219-4dd9-985a-825d72bcf671 "Kolibri"` →
  **seção 1: nenhuma ocorrência. Seção 2: nenhuma marca de envio. Seção 3: nada.** Por nome:
  `Kolibri` = **0/0/0/0** nos quatro arquivos. **Casa 100% nova.**
- **Precisa de navegador? SIM.** hCaptcha de desafio.

---

## 5. O QUE CAIU NO DEDUPE — e três destas iam passar

| Casa | Rota espontânea achada | O que o dedupe devolveu |
|---|---|---|
| **Larian Studios** ⭐ | `Character Artist – Open Application`, Lever `64e1e658-7c7a-4c7f-b950-f997d40a9d8e`, time **`Character Art/Art`**, local `Any` — **o título perfeito da rodada inteira** | **JÁ ENVIADA E CONFIRMADA.** `processados.csv`, 07/09: *"CANDIDATURA CONFIRMADA POR EMAIL… Email de no-reply@hire.lever.co em 07/09 as 04h35 UTC nomeando a requisicao"*; em 08/09 chegou a auto-resposta *"Thank you for your interest in Larian Studios"*. A mesma entrada avisa que as **duas** entradas do painel para esta requisição foram fechadas *"para ninguem mandar uma terceira"*. **Não clicar.** A irmã `Environment Artist – Open Application` (`9bd7d394`) também já está registrada como recusada por duplicidade de casa. |
| **Deck13 Interactive** | `General Application (f/m/x)`, Personio `2725779`, Remote (EU), departamento **`Creative`** — casa de *The Surge* e *Atlas Fallen*, encaixe forte | **JÁ ENVIADA E CONFIRMADA em 06/09.** `docs/index.html`: *"CANDIDATURA ENVIADA e CONFIRMADA em 06/09 pela forca-tarefa… Porta Personio"*. `processados.csv`: *"Personio: Chimera Entertainment, Deck13 General Application, Aesir Art Lead, Bongfish e KING Art TODAS ja com email de confirmacao de recebimento na caixa de 06/09"*. **E ATENÇÃO AO MÉTODO: o dedupe pelo ID `2725779` devolveu ZERO nos quatro arquivos** — a entrada do painel guardou só `https://deck13.jobs.personio.com/`, **sem o número da requisição**. Só o grep pelo NOME pegou. |
| **Chimera Entertainment** | `speculative application (f/m/d)`, Personio `150955`, Munique, departamento `Game Design` | **JÁ ENVIADA E CONFIRMADA em 06/09** (mesma linha do `processados.csv` acima). ID também deu **zero** no dedupe, pela mesma razão da Deck13. |
| **Bongfish** | `Open Application Bongfish`, Personio `366240`, Graz, Áustria | **JÁ ESTÁ NA FILA DELE.** `processados.csv`: *"OPEN APPLICATION PERMANENTE E FULL-TIME NO PERSONIO DA BONGFISH… A automacao preencheu tudo, anexou curriculo e carta"* e travou numa **pergunta obrigatória** — *"Where did you hear about this position?"*, cujas opções não incluem nenhuma verdadeira. Não é rota nova. |
| **ArenaNet** | `General Applications`, Ashby `fc37d644-7d8d-4d50-88e7-1cde6acfe586`, *"Don't see a role we are actively hiring for… Submit your resume to General Applications"* | **JÁ ENVIADA.** `processados.csv`, 30/08: *"Ashby confirmou a candidatura como General Applications; PORTAIS atualizado"*, remetente `no-reply@ashbyhq.com`. |
| **Bento Box Entertainment** | `Bento Box Atlanta - Submit Your Portfolios Here for Future Job Opportunities`, Lever `d7bb6a2c-e196-45d5-948a-665d658a6bf5` | **JÁ ENVIADA.** `processados.csv`, 30/08: *"Vini enviou portfolio na chamada aberta… Lever oficial confirmou"*. **Mesma armadilha da Deck13:** dedupe pelo ID = ZERO, porque a entrada antiga guardou só `jobs.lever.co/bentoboxent`, **sem o uuid**. |
| **Kabam** | `General Application`, Lever `d62974d9-8d92-4c7b-8d56-8ee23d35904d`, Vancouver | **JÁ ESTÁ NA FILA DELE, não é achado novo.** `docs/index.html`: *"A MAO POR hCAPTCHA DE DESAFIO DE IMAGEM, medido na tela em 07/09 as 08h40"*, revalidada em 09/09 e *"CONTINUA ABERTA"*. Some-se que a `Lead Character Artist` da casa foi **recusada em 03/09** (*"the position has now been filled"*). |
| **Quixel** | `General Applications`, Lever `0ad49e17-a9cb-451b-b3dd-fa186eabe60a`, *Flexible* | **ROTA FANTASMA, medida.** A API devolve o anúncio — é o **único** do quadro, criado em **17/06/2019** — mas a página do anúncio **e** a de candidatura devolvem **HTTP 404 com 297.266 bytes** (a página de erro do Lever). Dedupe limpo, mas **não há o que clicar**. |

### 5.1 A LIÇÃO DE MÉTODO DESTA SEÇÃO, e ela é dura

**Três das oito linhas acima passaram pelo `dedupe-agora.sh` com ID e devolveram ZERO** —
Deck13, Chimera e Bento Box — e as três **já tinham recebido candidatura**. O motivo é sempre o
mesmo: **a entrada antiga do painel guardou a URL do QUADRO, não o ID da requisição.** É
exatamente a regra 18 do briefing acontecendo de novo, só que do lado de dentro: a regra manda
guardar o ID, e as entradas anteriores a 06/09 não guardaram.

**Consequência prática que precisa entrar na rotina: dedupe por ID é OBRIGATÓRIO e
INSUFICIENTE. Rodar sempre com o segundo argumento (nome da casa) — que é o que o script pede
— e, quando o ID der zero, ler as ocorrências do NOME até o fim da célula antes de clicar.**
Se eu tivesse confiado só no ID, esta fila teria saído com três repetições.

---

## 6. O QUE CAIU POR VETO ESCRITO, POR IDIOMA E POR HOMÔNIMO

### 6.1 Veto escrito no anúncio

| Casa | Rota | Frase literal |
|---|---|---|
| **Blackbird Interactive** | `General Application`, Lever `498bb3c2-b23f-4aed-8fdd-ee80649e381d`, Vancouver | *"PLEASE NOTE: At this time, we are **only able to hire candidates who are legally eligible to work in Canada and reside within Canada**."* Veto de residência. O painel **já o tinha registrado** em 07/09 (*"VETO DE RESIDENCIA, NAO APLICAR"*); confirmado vivo hoje. |

### 6.2 Porta condicionada ao idioma — registrada, **não descartada**

| Casa | Rota medida | O que a medição achou |
|---|---|---|
| **NEOWIZ** (Coreia do Sul, Pangyo) | `[네오위즈] 인재 Pool`, Lever `c74ffadf-1e4e-4a3e-8ec3-fde9cc8f2aa3`, `country: KR`, time `Talent Pool`, híbrido. **HTTP 200, 773.448 bytes**, hCaptcha ativo | **País DENTRO do escopo** — a Coreia do Sul é uma das duas exceções asiáticas do briefing. Casa de peso na disciplina: *Lies of P*, *DJMAX RESPECT V*, *Skul*, *Sanabi* — elenco de personagem 3D AAA. **O que condiciona é o idioma, e está escrito no anúncio:** o corpo é **inteiramente em coreano** e uma das instruções é literal — *"이름란에는 영문명이 아닌 **한글명**을 기입해주세요"* (*"no campo de nome, escreva o nome em coreano, não em alfabeto latino"*). Isso não é veto de contratação, é formulário desenhado para candidato doméstico. Some-se o campo obrigatório de **informação salarial** (*"연봉 정보 기입 칸"*), que o briefing trata com resposta fixa. **Registro como porta condicionada, exatamente como as francesas de 11/09.** Dedupe: ID **inédito nos quatro arquivos**, nenhuma marca de envio. |

**Sobre as casas francesas:** a busca por `français courant`, `maîtrise du français`,
`oral et écrit`, `bilingue` e `francophone` foi rodada em **todos** os anúncios espontâneos das
três famílias. **Bateu em uma só, a Larian**, cujo texto é **bilíngue EN/FR por obrigação legal
do Quebec** — a versão francesa é tradução do mesmo texto, não exigência de idioma — e a Larian
já está enviada de qualquer forma. **Nenhuma porta francesa nova nesta rodada.**

### 6.3 Homônimo — e dois deles eram armadilhas de nome perfeitas

| Slug | O que eu esperava | O que a API devolveu |
|---|---|---|
| **`arkane`** (Ashby) | Arkane Studios (Lyon/Austin), *Dishonored*, *Deathloop* | **Arkane Cloud**, provedor de nuvem GPU para IA em Lyon. A `Candidature Spontanée` (`eb501536-9e48-422b-8c7f-84eb882fc0e8`, publicada em 08/09) é de infraestrutura: *"on construit un Cloud Service Provider spécialisé dans les infrastructures GPU dédiées à l'IA"*. **Não é o estúdio.** |
| **`paradox`** (Ashby) | Paradox Interactive (Estocolmo) | **Paradox**, empresa de EdTech com escritório em **Dubai**. O `Join Our Talent Network` é `Operations/Operations` nos Emirados Árabes — **fora do escopo** e fora do setor. |
| **`obsidian`** (Personio) | Obsidian Entertainment | **Obsidian Digital**, agência de marketing digital dinamarquesa. A `Unsolicited applications` é do departamento `Admin`. |
| **`mpc`** (Personio) | Moving Picture Company (VFX) | **MPC Oceanic Group AG**, armação e logística marítima em Hamburgo. A `Initiativbewerbung` do "Talent Pool" tem `Tanker Shipbroker` como vizinha de quadro. |
| **`retro`** (Lever) | Retro Studios (Nintendo, *Metroid Prime*) | **Retro Biosciences**, terapias de longevidade em Redwood City. |
| **`cyan`** (Personio) | Cyan Worlds (*Myst*) | **cyan Security Group GmbH**, Viena, cibersegurança. |
| **`choose`** (Lever) · **`brimstone`** (Ashby) · **`chromatic`** (Ashby) | — | App de compras em Paris · descarbonização de cimento · empresa do Storybook. |
| **`level`, `jump`, `focus`, `bio`, `midjourney`, `zero`, `blue`, `ajax`, `phoenix`, `lakestar`** | — | Fora do setor. `level` é companhia aérea, `blue` é consultoria de dados, `phoenix` é design industrial, `lakestar` é fundo de venture capital. |
| **~150 dos 185 quadros Ashby** | — | Slug de palavra genérica ocupado por empresa de outro ramo, confirmando outra vez o aviso do `quadros-tt-rec-1545-1009.csv`: `access`, `agent`, `aim`, `applied`, `assembly`, `base`, `bounce`, `butter`, `casa`, `chief`, `citizen`, `complete`, `console`, `contra`, `cube`, `felix`, `fuse`, `hostinger`, `imprint`, `junior`, `modal`, `moss`, `notion`, `nous`, `overview`, `parallel`, `post`, `rain`, `sent`, `share`, `skip`, `sphere`, `squad`, `sunday`, `tem`, `tempo`, `terminal`, `town`, `universe`, `vercel`, `volta`, `voodoo`, `when`, `wilson`, `writer` e afins. |

### 6.4 Caiu por DISCIPLINA — rota viva e medida, casa sem pipeline de personagem

| Casa | Rota viva e medida | Motivo |
|---|---|---|
| **Colonist** | `Talent Pool`, Ashby `ee99fc96-537a-40f6-966e-c17f207cbba3`, `Any Location`, **200 / 35.611 bytes**, reCAPTCHA de plataforma. Dedupe **limpo** nos quatro arquivos | Jogo de tabuleiro digital (alternativa ao Catan), time 100% remoto e assíncrono. A **única** vaga de arte do quadro é `UI Artist`. Sem elenco 3D. |
| **Improbable** | `General Application`, Ashby `ae853038-5760-40da-b380-c84cef0b5532`, `Remote - International` (Reino Unido), **200 / 18.269 bytes**. Dedupe **limpo** | Hoje é *venture builder* de cripto: as vagas abertas são `Product Marketing Manager, DEX` e `… Prediction Markets`. **Zero arte no quadro.** |
| **Poki** | `Open Application`, Lever `326aa4dc-e1b9-4faf-9258-4e46594b29e3`, Amsterdã, **200 / 728.600 bytes**, hCaptcha ativo. Dedupe **limpo** | Plataforma de jogos de navegador com **50 pessoas**; o conteúdo vem de *"350 game developer teams"* externos. Não produz personagem em casa. |
| **Immutable** | `Expression of Interest`, Lever `5128812a-ca47-4b8e-a59e-57470a298c4b`, Austrália, **200 / 747.724 bytes**, hCaptcha ativo. Dedupe **limpo** | Sydney está no escopo, mas a casa é **infraestrutura**: identidade, analytics e SaaS de crescimento para jogos de terceiros. Sem pipeline de arte. |
| **VirtaMed** | `Open applications welcome!`, Personio `924891`, Schlieren (Suíça), sem captcha | Simulação cirúrgica. É 3D, mas é **3D médico**, não personagem de entretenimento. |

**As cinco estão medidas e com dedupe feito.** Se uma rodada futura decidir que porta de
entrada vale em casa sem pipeline de personagem, elas estão prontas aqui e não precisam ser
remedidas.

---

## 7. PERSONIO — a lane limpa, e a armadilha que quase inflou o número em 22 linhas

**121 inquilinos vivos** (contra 52 em 09/09), **356 anúncios lidos**, **53 títulos de
candidatura espontânea**. Se eu parasse aí, escreveria "53 rotas novas". **Seria falso, e o
erro é medível.**

**31 dos 121 quadros são o QUADRO-MODELO do Personio**, o conjunto de exemplo que vem com a
conta. Reconhece-se por um trio idêntico de títulos:
`SEO Marketing Manager` + `Social Media (Working Student)` / `(Werkstudent)` +
`Initiativbewerbung (Festanstellung)` / `General Application`. Os 31: `acme`, `amazon`, `art`,
`boxelware`, `bright`, `clevr`, `current`, `delete`, `dom`, `framer`, `friends`, `frvr`,
`futurlab`, `heat`, `kaiko`, `kit`, `lessmore`, `levent`, `max`, `more`, `motion`, `nada`,
`sandbox`, `shd`, `sports`, `station`, `strong`, `thomas`, `victoria`, `visual`, `vrtual-x`.

**Os nomes `acme` e `amazon` na mesma lista entregam o jogo**: não são empresas, é a base de
demonstração. **30 das 53 "rotas" eram isso.** Tirando os quadros-modelo, sobram **23 rotas
espontâneas em 21 inquilinos**, e delas **quatro são do setor**: Bongfish, Chimera
Entertainment, Deck13 e Stratosphere Games. **Três das quatro já tinham sido usadas em 06/09**
(§5) — **sobrou uma, a Stratosphere, e ela é a linha 2 da fila.**

**O que o Personio ganha desta rodada, e vale mais que a linha:** é a **única das três famílias
sem porteiro**. Quatro formulários medidos, quatro com os campos servidos no HTML e **zero
ocorrência** de qualquer palavra de anti-bot. Se a campanha vai investir numa família para
envio automático daqui em diante, é nesta.

**Discriminador de inquilino do Personio, medido nesta rodada e útil para quem repetir:**
`HEAD https://<slug>.jobs.personio.com/` devolve **200** se o inquilino existe e **307** se não
existe (20.962 dos 21.087). O `/xml` **não serve como sonda** — devolveu **404 mesmo em
inquilino vivo** (testado em `chimera-entertainment`, cujo quadro tem 4 vagas). Quem lista
vaga é **`/search.json`**, que respondeu **200 em 121 de 121**.

**Vagas da disciplina em todo o Personio: UMA**, a `3D Artist Generalist - Modelling &
Texturing` da Chimera, **em Cebu, nas Filipinas** — fora do escopo, e já registrada assim em
`automacao/caca-personio-0909.md`. Nada mudou nesse ponto em dois dias.

---

## 8. ACHADO LATERAL QUE NÃO ERA A MISSÃO — vagas de personagem abertas nos 365 quadros

Enquanto lia os 3.895 anúncios, filtrei por `character`, `creature`, `sculpt`, `groom`, `hair`,
`fur`, `surfacing`, `look dev`, `modeler`, `modeller`, `modelling` e `visual dev`.
**Catorze acertos, e todos já são conhecidos da campanha.** Registro o número porque negativo
medido vale tanto quanto positivo:

| Casa | Vaga | Situação já registrada |
|---|---|---|
| Behaviour Interactive | 3 × `Senior 3D Character Artist` (7 Days to Die, Dead by Daylight, projeto não anunciado), Montreal | A de Dead by Daylight foi **enviada à mão e confirmada** em 10/09; as outras já estão no painel |
| Avalanche Studios | `Lead Character Artist`, Estocolmo (`8f7bd580`) | **Enviada à mão e confirmada** em 10/09 |
| thatgamecompany | `3D Character Artist (Mid-Senior)` (`36e101a4`) | **Veto escrito** de autorização EUA/Canadá, registrado em 05/09 |
| Skydance Animation Madrid | `Senior Grooming TD`, `Character Surfacing Trainee` (+ 4 de superfície de ambiente) | Casa já registrada, com parede hCaptcha medida |
| Dream Games | `Visual Development Artist`, Istambul | Já registrada em 09/09 (arte conceitual 2D; Turquia é país novo não conversado) |
| Larian | `Character Artist – Open Application` | Já enviada (§5) |
| Chimera Entertainment | `3D Artist Generalist - Modelling & Texturing`, Cebu | Fora do escopo, já registrada em 09/09 |

**Zero vaga de personagem inédita nos 365 quadros.** Isso reforça, por outra família, o mesmo
diagnóstico da caça ao Workday de hoje: **o gargalo não é rota, é estoque.**

---

## 9. SMARTRECRUITERS — NÃO VARRI, E O MOTIVO É MEDIDO

O enunciado condiciona a varredura do SmartRecruiters a **medir que o inquilino não tem
DataDome**. Sondei 6 inquilinos, 12 requisições:

| Inquilino | `api.smartrecruiters.com/v1/companies/<slug>/postings` | `jobs.smartrecruiters.com/<slug>` | `datadome` no HTML |
|---|---|---|---|
| Ubisoft | 200 / 50 b | 200 / 33.160 b | **0** |
| Bosch | 200 / 50 b | 200 / 33.160 b | **0** |
| Mattel | 200 / 50 b | 200 / 97.187 b | **0** |
| SEGA | 200 / 50 b | 200 / 97.300 b | **0** |
| Rockstar | 200 / 50 b | 200 / 97.217 b | **0** |
| TeamViewer | 200 / 50 b | 200 / 97.247 b | **0** |

**Zero acertos de `datadome` — e eu NÃO vou concluir "não tem DataDome" a partir disso**, pela
mesma razão que o Ashby me ensinou hoje (§1.2): o HTML servido a um `curl` não mostra o que o
JavaScript injeta depois. A campanha **já mediu a parede da Ubisoft com clique** em 06/09.
Sem sinal positivo de ausência, a condição do enunciado não foi satisfeita e a lane fica
fechada.

Registro de quebra que as respostas de **50 bytes** na API indicam que essas seis grafias
**não são os slugs reais** do SmartRecruiters (o discriminador é sensível a maiúsculas e usa o
identificador de empresa, não o nome). Quem for varrer essa família precisa resolver isso
antes — e essa é a parte do trabalho que eu não fiz.

---

## 10. O QUE EU NÃO CONSEGUI FECHAR, e está escrito

1. **Não li os campos do formulário do Ashby na fonte.** O `/application` é casca de SPA e a
   definição do formulário vem por GraphQL. Tentei sete nomes de campo (`formDefinition`,
   `sections`, `sectionsWithFields`, `fieldSubmissions`, `formJson`, `questions`, `inputs`) e o
   servidor recusou todos com `GRAPHQL_VALIDATION_FAILED`; **a introspecção está desligada**
   (`"GraphQL introspection has been disabled"`). O que as linhas 1, 3 e 5 dizem sobre campos
   do Ashby vem do dossiê que esta campanha mediu **com clique** em 07/09, e está marcado como
   tal. **Não inventei campo nenhum.**
2. **Join.com ficou de fora.** Não sobrou orçamento de rodada depois de Ashby, Lever e
   Personio. É a única das quatro famílias do enunciado que continua **completamente intocada**
   por esta campanha, e fica como a próxima lane inteira a abrir.
3. **Não sei medir o quanto o universo de 21.420 slugs ainda deixa de fora.** Ele cobre todo
   nome e todo domínio que este repositório cita. Estúdio que a campanha nunca ouviu falar não
   entra por construção.
4. **Não abri o `search.json` dos 31 quadros-modelo do Personio um a um** para confirmar que
   nenhum deles é uma empresa de verdade que por acaso usa os títulos de exemplo. O trio de
   títulos é idêntico byte a byte nos 31 e a lista inclui `acme` e `amazon`, o que me deixa
   confortável — mas é inferência, não medição caso a caso.
5. **`Improbable`, `Colonist`, `Poki`, `Immutable` e `VirtaMed` ficaram fora da fila por
   disciplina, não por rota.** As cinco rotas estão vivas, medidas e com dedupe limpo (§6.4).

---

## 11. RESUMO EM UMA LINHA

**64.100 requisições, 365 quadros vivos, 3.895 anúncios lidos, 112 rotas espontâneas achadas
(82 depois de descontar o quadro-modelo do Personio), e
a fila verdadeira tem SETE** — porque Larian, ArenaNet, Bento Box, Deck13, Chimera, Bongfish e
Kabam já tinham sido usadas, Blackbird tem veto escrito, Quixel é fantasma de 404, NEOWIZ é
porta condicionada ao coreano, 30 "rotas" do Personio eram quadro de demonstração e sete
"estúdios" eram homônimo de outro ramo. **O achado de plataforma: o PERSONIO é a única das três
famílias sem captcha (4 de 4 formulários medidos limpos), enquanto o Ashby é reCAPTCHA v2
invisível em 6 de 6 e o Lever é hCaptcha de desafio em 8 de 8.**
