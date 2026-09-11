# Caça 11/09 — estúdios de personagem estilizado FORA de ATS

Só `curl`. Nenhum navegador, nenhum envio, nenhum formulário preenchido, nenhum email nem
rascunho criado. A entrega é fila com dossiê. Quem escreve e quem clica é o Vini.

## PLACAR MEDIDO (números antes de qualquer narrativa)

| O que | Número |
|---|---|
| Casas candidatas montadas (3 lotes) | **241** |
| Cortadas antes de sondar, por já terem linha em `enviados.csv` | **88** |
| Domínios efetivamente sondados | **153** |
| Sondagens HTTP feitas (raiz + 6 caminhos + links colhidos + leitura profunda) | **1.397** |
| Domínios com raiz viva (200 e > 500 bytes) | **109** |
| Domínios mortos, parados ou bloqueados por esta rede | **44** |
| Domínios com **página de carreira viva** | **67** |
| Desses, com marcador de **ATS de terceiro** (fora do alvo desta caça) | **17** |
| **Formulário próprio COM campo de arquivo** | **4** (+2 achados em `/contact`, fora do caminho de carreira) |
| Formulário próprio sem campo de arquivo | 20 |
| Só email de recrutamento publicado | 15 |
| Página de carreira viva sem porta nenhuma (nem form nem email) | 16 |
| **Fila final depois do dedupe** | **4 de formulário + 9 de email** |

**O número que dói e que é o achado de método do dia:** dos oito melhores formulários próprios
que eu tinha na mão, **três caíram no dedupe** — Wise Blue Studios (candidatura enviada e
confirmada em 27/08 pelo formulário próprio), Storm Studios (confirmada em 30/08) e Trixter (já
na `FILA-DO-VINI.md`). A hipótese que abriu a missão — "formulário próprio é terreno que a
campanha nunca varreu" — **está parcialmente errada e foi medida como errada**. A campanha já
trabalhou essa lane; o que faltava era exaustividade, não a lane.

## Como a lista foi montada, na ordem que o brief mandou

1. **Do que o repositório já conhece.** `alvos.csv` (585 linhas) cruzado contra `enviados.csv`,
   `processados.csv` e `docs/index.html` devolveu **4 casas sem linha de envio**, e três delas
   com motivo escrito (Índia fora de escopo, etc.). `pessoas.csv` (228 linhas) devolveu 8 nomes,
   todos de casas grandes já em thread. **`alvos.csv` está seco** — negativo medido, e ele vale.
2. **Casas de fora do repositório.** 241 nomes de animação CG estilizada, jogo estilizado de
   time pequeno e médio e estúdio de serviço de personagem, dentro do escopo. O cruzamento
   contra o repositório inteiro (`git ls-files`) mostrou que **88 já tinham envio** e outras
   dezenas já estavam registradas sem envio.
3. **Sonda de porta.** `<dominio>/` mais `/careers`, `/jobs`, `/join-us`, `/work-with-us`,
   `/contact`, `/about`; depois colheita de `href` de carreira da raiz (151 links, 120 depois de
   filtrar CSS/JS/Wix) e leitura profunda das finalistas.

---

# FILA 1 — PORTA DE FORMULÁRIO (o Vini pode enviar daqui)

## 1. Nine Dots Studio — Québec, Canadá — a melhor porta da rodada

- **Por que presta para personagem estilizado:** casa de **Outward** e **Outward 2**, RPG de
  fantasia estilizada em primeira/terceira pessoa, com personagens e criaturas próprios. O
  formulário tem categoria **Art** separada de Animation, e o próprio site diz, no fim do
  formulário: *"Your application will be processed solely by Nine Dots Studio."*
- **URL exata da porta:** `https://www.ninedotsstudio.com/careers`
- **Medido:** HTTP **200**, **67.734 bytes**. A única vaga aberta hoje é
  `Capture Artist / Artiste video et capture`, Québec — **não é dele**; o que serve é o
  **formulário espontâneo** da mesma página.
- **Tipo de porta:** formulário próprio, submissão por JS (Next.js), sem `action`.
- **Campos medidos:**
  `website` (texto, **HONEYPOT — tem de ficar VAZIO**), `name` (obrigatório), `email`
  (obrigatório), `phone`, `jobType` (select: Game design, Programming, **Art**, Animation,
  Narrative, Audio, Production, QA, Marketing, Other), `portfolioUrl` (url),
  `cv` (file, `accept=.pdf,.doc,.docx`), `message` (textarea).
- **Captcha medido:** **ZERO.** Busca por `recaptcha`, `hcaptcha`, `turnstile`, `sitekey` e
  `cf-turnstile` no HTML inteiro: nenhuma ocorrência.
- **Dedupe:** `sh automacao/dedupe-agora.sh "ninedotsstudio.com" "Nine Dots Studio"` →
  *"(nenhuma — o ID é inédito nos quatro arquivos)"*, zero marca de envio, zero histórico de
  parede. **Casa 100% nova.**
- **Francês:** o anúncio é bilíngue no título, mas a busca por `français`, `francais`,
  `bilingue`, `francophone` e `oral et écrit` na página da vaga deu **zero**. Não há exigência
  de idioma escrita. Québec, então vale conferir de novo se a conversa avançar.
- **Precisa de navegador?** **Sim**, porque o envio é por JavaScript e há anexo. Mas **não há
  porteiro**, então é caso do `preencher-formulario.js` e não da fila da mão dele.

## 2. Peekaboo Animation — Barcelona, Espanha

- **Por que presta:** produtora de animação infantil que **cria as próprias séries**. Frase do
  site: *"Established in Barcelona in 2015, Peekaboo Animation focuses on producing high-quality
  children's animation for television and emerging platforms. At Peekaboo we create, draw, write,
  produce and finance our own shows."* E, no formulário, em letra do próprio site:
  ***"IF YOU WANT TO WORK WiTH US, PLEASE ATTACH YOUR PORTFOLIO"*** — convite explícito.
- **URL exata da porta:** `https://www.peekabooanimation.com/contact/`
- **Medido:** HTTP **200**, **77.739 bytes**.
- **Tipo de porta:** formulário próprio **Contact Form 7**, `action=/contact/#wpcf7-f9-p24-o1`.
- **Campos medidos:** `text-898` (nome), `email-978`, `textarea-838` (mensagem),
  **`file-703` (anexo do portfólio)**, `acceptance-408` (consentimento de dados),
  `coupon_question` (**honeypot, deixar vazio**), mais os `_wpcf7*` de sessão.
- **Captcha medido:** **reCAPTCHA v3** — o campo `_wpcf7_recaptcha_response` está servido no
  HTML. É pontuação invisível, não é desafio de clique; pode passar, pode não passar.
- **Ressalva honesta de rota:** a casa **também** tem `/jobs` apontando para
  `https://app.dover.com/jobs/peekabooanimation` (ATS Dover, 200, 4.105 bytes, com Turnstile).
  A porta sem ATS é a de `/contact/`, e é a que entra nesta fila.
- **Dedupe:** inédito nos quatro arquivos, zero marca de envio.
- **Precisa de navegador?** Sim, pelo anexo e pelo reCAPTCHA v3.

## 3. HAEGIN — Seul, Coreia do Sul

- **Por que presta:** casa de **Play Together** (플레이투게더), mundo social 3D de personagem
  estilizado com colaboração de marca (a mais recente com *Catch! Teenieping*), e de
  *2026 프로야구GO!*. A página de carreira tem a categoria **아트&디자인 (Art & Design)**
  separada de 개발 (dev), 게임기획 (design) e 사업&마케팅.
- **URL da página de carreira:** `https://www.haegin.kr/career.php` — HTTP **200**, **16.408 bytes**.
  As cinco vagas listadas hoje são marketing, cliente, dados e financeiro; **nenhuma de arte aberta**.
- **URL exata da porta:** `https://www.haegin.kr/contact.php` — HTTP **200**, **14.474 bytes**.
- **Tipo de porta:** formulário próprio em PHP puro, `action=/contact_send.php` (POST).
- **Campos medidos:** `type` (hidden), `name`, `phone`, `email`, `subject`, `content`
  (textarea), **`file_upload`** (anexo), submit.
- **Captcha medido:** **ZERO** — nenhuma ocorrência de recaptcha, hcaptcha, turnstile ou
  datadome no HTML.
- **Emails públicos da casa:** `hr@haegin.kr` (rotulado **Recruit** no rodapé) e
  `biz@haegin.kr` (Business). **O `hr@` também serve como porta de email**, e é a mais direta.
- **Dedupe:** inédito nos quatro arquivos.
- **Precisa de navegador?** Provavelmente não para os campos, mas sim para o anexo com garantia.
  Site majoritariamente em coreano; o alternador EN existe mas o miolo de carreira volta para KR.

## 4. Blowfish Studios — Sydney, Austrália

- **Por que presta:** desenvolve e publica jogo estilizado próprio. Frase do site:
  *"We develop and publish fantastic games! Our versatile team excels in every aspect of game
  creation: from eye-catching concept art and immersive audio to precise motion tracking."*
  O destaque da home é um jogo de personagem estilizado — *"the young Nadira and her pet lizard
  Jiji begin their journey through desert sands... only she can fulfill Nadira's deepest wish."*
- **URL exata da porta:** `https://www.blowfishstudios.com/careers`
- **Medido:** HTTP **200**, **1.597.683 bytes** (Wix, por isso o tamanho).
- **Tipo de porta:** formulário próprio Wix, **dois formulários na página**; o de recrutamento
  tem `text` (×3), `email`, `textarea` e **TRÊS campos de arquivo** (`type=file`), o que combina
  com CV + portfólio + carta.
- **Campos:** o Wix não põe `name` nos inputs, só id gerado — **os rótulos só saem no navegador**.
- **Captcha medido:** **ZERO** ocorrência de recaptcha, hcaptcha, turnstile ou datadome.
- **Dedupe:** inédito nos quatro arquivos.
- **Precisa de navegador?** **Sim, obrigatoriamente** — Wix monta o formulário por JS e o
  envio não existe no HTML servido.

---

# FILA 2 — PORTA DE EMAIL (vira rascunho de carta fria)

Ordenada por encaixe de PERSONAGEM 3D, e a nota de encaixe é honesta: da metade para baixo o
portfólio dele compete menos, e isso está escrito em cada item em vez de maquiado.

## 1. Paper Owl Films — Belfast, Reino Unido — `jobs@paperowlfilms.com`

- **URL da porta:** `https://paperowlfilms.com/careers` — HTTP **200**, **48.566 bytes**.
- **Frase do próprio site, e é o convite mais explícito da rodada:**
  *"Can I submit a speculative application? Yes. We welcome speculative CVs and portfolios at
  jobs@paperowlfilms.com. Please note that we receive a lot of emails and may not always respond."*
- **Tipo de porta:** só email. Zero formulário na página de carreira, zero marcador de ATS.
- **Dedupe:** `paperowlfilms.com` inédito nos quatro arquivos.
- **RESSALVA MEDIDA, e ela é contra a casa:** a página `/services`
  (HTTP 200) descreve **pós-produção e áudio** — cabine de voz, sound design, Pro Tools,
  grading em DaVinci, masterização — e **não cita 3D, CGI, Maya, Blender nem character em
  lugar nenhum**. O encaixe de personagem 3D **não está provado**. A porta é ótima, a
  disciplina é duvidosa. Se ele escrever, é aposta de porta de entrada (regra 13), não de vaga.

## 2. Capybara Games — Toronto, Canadá — `jointheteam@capybaragames.com`

- **URL da porta:** `https://www.capybaragames.com/careers/` — HTTP **200**, **68.777 bytes**.
- **Frase do site:** *"There are no open positions at the moment, but feel free to send us your
  resume. We love to hear from friendly, talented people... we're always interested in hearing
  from other developers who share our values... Just shoot us an email at
  jointheteam@capybaragames.com."*
- **Tipo de porta:** só email. Zero formulário de candidatura, zero ATS.
- **Aviso de golpe publicado pela própria casa, e vale para a carta:** *"Only trust email
  addresses ending in @capybaragames.com."* Ou seja, endereço correto e conferido na fonte.
- **Dedupe:** inédito nos quatro arquivos.
- **Ressalva de encaixe:** o catálogo deles (Grindstone, Superbrothers: Sword & Sworcery,
  Super Time Force) puxa para **2D e pixel**. Personagem 3D não é o forte da casa.

## 3. Mr. Klaus Studio — Madrid, Espanha — `info@mrklausstudio.com`

- **URL da porta:** `https://mrklausstudio.com/contact` — HTTP **200**, **275.631 bytes** (Framer).
- **Frase do site:** *"We are a creative studio based in Madrid. Founded in 2015 for a team with
  20 years of experience on their backs in the Animation Industry... Our studio was born in order
  to create and produce our own stories with a unique Look & Feel. We already have 4 Original
  Ideas for TV Series: Spending Days with Mr. Cthulu, BENTO, My Brother is a T-Rez and Bust a Danz."*
  Séries próprias de personagem estilizado, e a frase **"unique Look & Feel"** é exatamente o
  argumento dele.
- **Tipo de porta:** só email. Não existe página de carreira; `/careers`, `/jobs`, `/join-us` e
  `/work-with-us` não respondem 200.
- **Dedupe:** inédito nos quatro arquivos.

## 4. Studio Meala — Boyle, Roscommon, Irlanda — `info@studiomeala.com`

- **URL da porta:** `https://studiomeala.com/pages/jobs` — HTTP **200**, **192.579 bytes**.
- **Frase do site, e o trecho de remoto interessa direto a ele:** *"Our studio operates both
  remote and local pipelines, so working remotely is an option. Some projects will require our
  team to be based in the Republic of Ireland... Job postings will appear below when available."*
  E no rodapé: *"Studio Meala | CREATIVE AND COLLABORATIVE ANIMATION STUDIO... an animation
  studio dedicated to producing high end animated content based in the west of Ireland."*
- **Tipo de porta:** só email. **Nenhuma vaga listada hoje** — o único formulário da página é
  assinatura de newsletter (Shopify + MailerLite), não candidatura.
- **Dedupe:** inédito nos quatro arquivos.

## 5. Thunder Lotus Games — Montreal, Canadá — `careers@thunderlotusgames.com`

- **URL da porta:** `https://thunderlotusgames.com/jobs/` — HTTP **200**, **216.313 bytes**.
- **Tipo de porta:** só email. Zero ATS, zero formulário de candidatura.
- **Dedupe:** inédito nos quatro arquivos.
- **Ressalva de encaixe, e ela é séria:** *Spiritfarer* e *Sundered* são **2D desenhado à mão**.
  A casa é de arte estilizada belíssima e de disciplina errada. Entra por porta de entrada, não
  por encaixe. Montreal, então vale a regra de francês antes de qualquer carta.

## 6. Snowman — Toronto, Canadá — `hello@builtbysnowman.com`

- **URL da porta:** `https://builtbysnowman.com/jobs/` — HTTP **200**, **4.820 bytes**.
- **Tipo de porta:** só email, e a página é uma casca de 4,8 KB sem vaga listada.
- **Dedupe:** inédito nos quatro arquivos.
- **Ressalva:** a série *Alto's Adventure / Odyssey* é silhueta 2D. Encaixe fraco.

## 7. Alientrap Games — Canadá — `jobs@alientrap.org`

- **URL da porta:** `https://www.alientrap.com/contact/` — HTTP **200**, **35.681 bytes**.
  Endereço de recrutamento dedicado, publicado ao lado de `contact@`, `support@` e `requests@`.
- **Medido também:** `https://www.alientrap.com/category/jobs/` (200, 40.298 bytes) usa
  **Google Forms**, então a rota de vaga listada é de terceiro; a porta sem ATS é o `jobs@`.
- **Dedupe:** inédito nos quatro arquivos.
- **Ressalva:** time muito pequeno (Apotheon, Cryptark), estética 2D.

## 8. Six Point Harness — Los Angeles, EUA — `info@sixpointharness.com`

- **URL da porta:** `https://sixpointharness.com/contact` — HTTP **200**, **136.747 bytes**.
- **Medido:** `/jobs` responde 200 com **133.525 bytes** e **zero `<form>` no HTML** — o
  formulário é **Jotform embutido por JS**, ou seja, não dá para medir campo daqui e não é
  formulário próprio. O único endereço servido é o `info@`.
- **Dedupe:** inédito nos quatro arquivos.
- **Ressalva:** casa de animação 2D (Dick Figures, The Whistle). Encaixe fraco.

## 9. Viskatoons — Melbourne, Austrália — `peter@viskatoons.com`

- **URL da porta:** `https://viskatoons.com/contact` — HTTP **200**, **30.126 bytes**.
- **Frase do site:** *"Animation studio · Richmond, Melbourne. If it moves, we're on it. The
  longest-running, most trusted animation studio in Melbourne. Series, commercials, explainers,
  music videos and games."*
- **Dedupe:** inédito nos quatro arquivos. Endereço de pessoa nomeada, publicado pela casa.
- **Ressalva:** catálogo de comercial e explainer 2D. Encaixe fraco, porta real.

---

# CAIU NO DEDUPE (e é por isso que a regra existe)

| Casa | O que o dedupe devolveu |
|---|---|
| **Wise Blue Studios** (Madrid) | `docs/index.html`: *"wisebluestudios.com/open-positions/ — Aplicação enviada em 27/08 pelo formulário próprio — confirmação recebida"*, mais 2 linhas em `processados.csv`. **JÁ ENVIADA.** |
| **Storm Studios** (Oslo) | `docs/index.html`: *"CANDIDATURA CONFIRMADA em 30/08 pelo formulário do site, com cópia da inscrição por email."* **JÁ ENVIADA.** |
| **Trixter** (Munique) | `automacao/FILA-DO-VINI.md`: `trixter.de/jobs/job/speculative-job-application-2/`. E `processados.csv` de 08/09: *"NAO ENVIADA... o formulario e um Personio embutido em WordPress e o envio por AJAX nao chega a sair do nosso ambiente."* **Já na fila da mão dele, e não é formulário próprio: é Personio embutido.** |
| **Icon Creative Studio** (Vancouver) | Candidatura **ENVIADA em 31/08** para Intermediate Modeling/Texture Artist, confirmada por `notifications@app.bamboohr.com`. |
| **The Line** (Londres) | **4 linhas** em `enviados.csv` (info@, entertainment@, james@, 2ª via). O `jobs@thelinestudio.com` nunca foi usado, mas a casa já levou quatro cartas. |
| **Titmouse** (LA/NY) | Banco de talentos feito à mão em 30/08, confirmado por Airtable. Quadro em Lever. |
| **Nørlum** (Viborg) | Pessoa achada em 10/09 (`jericca@noerlum.com`), rascunho já na fila. A página publica hoje *"There are no jobs available at the moment. But we're always happy to see your portfolio. Drop us a message... at contact@noerlum.com"* — endereço novo, casa velha. |
| **Mainframe Studios** (Vancouver) | Já na `FILA-DO-VINI.md`. E a razão está medida: a General Application roda em **UKG Ready** (`secure.ukgready.ca/ta/6214859.careers`) e **exige conta de candidato**. |
| **Sumo Digital** | Registrada e revalidada em 07/09: *"a página oficial de carreiras segue sem Character Artist nenhum."* |
| **Boulder Media** (Dublin) | Registrada em 02/09: *"SEM VAGAS... só formulário de contato sem upload."* Reconferido hoje: continua assim, e a **visão declarada da casa é 2D** — *"Our vision is to be both an originator and the best creative animation partner for high end 2D TV content and features."* |
| **Like a Photon Creative** (Brisbane) | Registrada em 02/09 como sem página de carreira. Reconferido: `/contact` existe (200, 74.401 bytes), formulário sem anexo, email ofuscado `hello(at)likeaphoton.com`. |

# VETO E ARMADILHA DE NOME (negativos que valem tanto quanto os positivos)

- **Massive Black — VETO.** A `/careers` deles (200, 40.976 bytes) publica `jobs@massiveblack.com`
  e lista *"3d character / creature artists"*, o que parecia encaixe perfeito. **A mesma página
  diz, no topo:** *"we've moved! Massive Black has joined forces with Room 8 Studio... 2023 R8S
  ENTERTAINMENT LTD da Room 8 Studio... Massive Black operates as a division within Room 8 Studio."*
  **Room 8 está fora da campanha por regra.** Não escrever.
- **Charles Ellison (Warner Bros. Pictures Animation) — PROIBIDO.** Não apareceu em nenhuma
  página desta caça, e continua proibido por regra do briefing.
- **Homônimos que enganam e custaram sonda:**
  - `zoo.ad` — não é a Zoo Studio de animação; é *"Estudi de disseny gràfic, web i audiovisual"*
    em Barcelona. Branding e packaging. Fora.
  - `daylightstudios.com` — não é o estúdio de jogos de Singapura; é uma casa espanhola de
    **aluguel de estúdio e equipamento de filmagem** (*"Estudios / Alquiler / Vehículos"*). Fora.
  - `somuga.com` — não é o estúdio basco; é um site de **investimento financeiro** em espanhol. Fora.
  - `tuataragames.com` — a casa existe, mas o próprio site diz *"Tuatara is a collective of
    world class artists providing cutting edge **VFX services for games** and other realtime
    experiences"*, e VFX em tempo real está **explicitamente fora da disciplina dele**. Fora.
  - `factorycreate.com` — domínio **estacionado na HugeDomains**. A casa não existe mais nesse
    endereço.
- **Portas fechadas com todas as letras, medidas hoje:** Yowza! Animation
  (*"Currently we have no openings"*), Moetion Films (*"We are not recruiting at the moment"*),
  Turnip + Duck (*"Turnip + Duck is not currently recruiting"*), Iron Galaxy
  (*"No Open Positions"* na fila de Art), Sardine Productions (*"Coming Soon... under
  construction"*).

# ACHADO DE PLATAFORMA: UKG READY É FAMÍLIA NOVA PARA ESTA CAMPANHA

O `mainframe.ca/careers` esconde um `<iframe data-src>` para
`https://secure.ukgready.ca/ta/6214859.careers?CareersSearch&InFrameset=1&HostedBy=www.mainframe.ca&ein_id=18317277`.
A página respondeu **200 com 4.415 bytes** e o corpo útil é só `Career Search` — é frameset com
JS. **`secure.ukgready.ca` não aparece em nenhum varredor de família desta campanha.** Se valer
uma próxima caça de lane, é um universo inteiro não mapeado, e a sonda é o padrão
`/ta/<numero>.careers`.

# ARMADILHA DE REDE MEDIDA (para a próxima rodada não gastar sonda à toa)

**26 domínios responderam `000` por HTTPS nesta rede**, e não é domínio morto: o `curl -v`
devolve `TLSv1.3 (IN), TLS alert, internal error (592)` — a borda derruba o handshake. O status
do proxy registra as mesmas casas como `ws_closed_mid_exchange` e `connect_rejected`.
**Repetir em `http://` recuperou 5 delas** (pikkukala.eu 200/17.878, bugbear.fi → bugbeargames.com
200/105.147, axisstudios.com 404, jellyfishpictures.co.uk 403, ghost.dk 402) e **`--tls-max 1.2`
não recuperou nenhuma**. Regra barata: **domínio que dá `000` por HTTPS merece uma segunda
tentativa em `http://` antes de virar "morto" no relatório.**

# O QUE ESTA CAÇA NÃO ACHOU

**Zero vaga de personagem 3D aberta e inédita** nas 67 páginas de carreira vivas. Nenhuma.
As quatro portas de formulário são todas **candidatura espontânea**, e das nove portas de email
**nenhuma tem vaga de personagem publicada hoje**. É o terceiro fechamento em zero no mesmo dia,
depois do Workday e do Ashby/Lever/Personio. Isso não é falha das três caças: é leitura de
mercado. O estoque de vaga de personagem sênior aberta, dentro do escopo geográfico, **está
esgotado hoje**, e o que resta é banco de talentos e carta fria.

**Nada foi enviado. Nenhum formulário preenchido. Nenhum email nem rascunho criado.**
`enviados.csv`, `automacao/FILA-DO-VINI.md` e `docs/index.html` não foram tocados.
