# CAÇA JOIN.COM · GREENHOUSE · WORKABLE — candidatura espontânea, 11/09/2026 (noite)

Tudo por `curl` e pelas **APIs e objetos de configuração públicos** das três famílias.
**Nenhum navegador foi aberto, nada foi enviado, nenhum formulário foi preenchido, nenhum
email foi mandado.** A entrega é fila pronta com dossiê; quem clica é o Vini.

Não toquei em `enviados.csv`, em `automacao/FILA-DO-VINI.md` nem em `docs/index.html`. Criei
este arquivo e acrescentei **uma** linha em `automacao/processados.csv`.

Lido antes de começar: `BRIEFING.md` (inclusive as cinco seções novas de 11/09 no fim),
`automacao/BRIEF-JHON.md`, e `automacao/caca-ashby-lever-1109.md`, que é o formato desta
entrega e a lista do que **não** precisava ser refeito.

---

## 1. PLACAR — os números medidos, antes de qualquer narrativa

| Família | Rota sondada | Sondagens | Inquilinos vivos | Anúncios lidos | Anúncios espontâneos | Inquilinos com rota | Passaram escopo + disciplina | Dedupe limpo | **Na fila** |
|---|---|---|---|---|---|---|---|---|---|
| **Greenhouse** | `boards-api.greenhouse.io/v1/boards/<slug>/jobs` | **83.223** | **376** | **10.755** | **77** | **54** | 11 | 4 | **5** |
| **join.com** | `HEAD join.com/companies/<slug>` + `__NEXT_DATA__` | **83.223** | **526** | **290** | **12** (a flag `isSpontaneousApplicationEnabled`) | **12** | 0 | — | **0** |
| **Workable** | `apply.workable.com/<slug>/` (só medição de porteiro) | 1.500 tentadas, **808 recusadas com 1015** | — | — | — | — | — | — | **0** (§6) |
| **TOTAL** | | **~168.000 requisições** | **902 inquilinos** | **11.045 anúncios** | **89 rotas espontâneas** | **66** | **11** | **4** | **5 rotas na fila** |

**Quebra que o Vini pede (regra de 10/09): das 5 rotas da fila, 5 são PORTA ESPONTÂNEA
genérica — nenhuma é anúncio de vaga aberta.** Duas caem em departamento nomeado
(`General Application` da Absurd Ventures, e o seletor de departamento da Jam Filled onde
existe a opção literal **`CG Assets (Modeling/Surfacing)`**). **Nenhuma candidatura foi
enviada nesta rodada, por regra do enunciado.**

### 1.1 O PLACAR DE CAPTCHA, medido no objeto de configuração e não no grep

| Família | O que o objeto de configuração mostra | Veredito medido | Rotas medidas |
|---|---|---|---|
| **Greenhouse** (`job-boards.greenhouse.io/<slug>/jobs/<id>`) | `window.ENV.GOOGLE_RECAPTCHA_INVISIBLE_KEY = 6LfmcbcpAAAAAChNTbhUShzUOAMj_wY9LQIvLFX0` com `GOOGLE_RECAPTCHA_ENDPOINT = https://www.recaptcha.net/recaptcha/enterprise.js`; **a mesma chave em todo inquilino, é chave de plataforma**. No bundle: `invisibleCaptcha(){return window.grecaptcha.enterprise.execute(this.invisibleKey,{action:"apply_to_job"})}` | **reCAPTCHA ENTERPRISE por pontuação (v3), invisível**, com **fallback de código de 8 dígitos por email** quando a pontuação reprova (§3.2) | **295 de 376 inquilinos** |
| **join.com** (`join.com/companies/<slug>/apply`) | `var env = {... "RECAPTCHA_SITE_KEY":"6LcBKJEdAAAAAOns5uYTQrLbrHXWtoFXb5sMjmxH" ...}`. No bundle: script montado como `api.js?render=${key}` e `grecaptcha.execute(n,{action:e})`, com a ação **`SpontaneousApplication`** amarrada ao submit, e `.grecaptcha-badge{display:none!important}` injetado | **reCAPTCHA v3 por pontuação**, mais **cabeçalho `fingerprint`/`uberctx-fingerprint`**, mais **link de verificação por email** antes de fechar a candidatura | **rota de espontânea medida ponta a ponta** |
| **Workable** (`apply.workable.com/<slug>/`) | `window.careers.features.recaptcha = **false**` (a armadilha), **mas** `wjb_acp_turnstile_captcha_enabled: true` e `config.turnstileWidgetSiteKey = "0x4AAAAAAAVY8hH3nz6RxaK0"`, **igual em dois inquilinos diferentes**, logo chave de plataforma; mais `cdn-cgi/challenge-platform/scripts/jsd/main.js` num iframe oculto | **Cloudflare Turnstile de plataforma + desafio JS do Cloudflare**; a API ainda devolve **1015** para esta rede | **2 inquilinos** |

**Tradução prática: nenhuma das três lanes é sem porteiro.** O Personio segue sendo a única
sem captcha que esta campanha mediu. O que muda aqui é que o Greenhouse tem **uma chave
por inquilino que dá para medir por `curl` antes de gastar rodada** — ver §3.1.

### 1.2 A armadilha do meu próprio método, e desta vez ela mordeu duas vezes

A lição de `caca-ashby-lever-1109.md` §1.2 diz que grepar a palavra `captcha` no HTML não é
medição. **Nesta rodada, as duas famílias novas tinham exatamente essa armadilha montada:**

1. **Workable.** O `grep -i recaptcha` no `/apply` acha **`"recaptcha":false`** dentro de
   `window.careers.features`. Parar ali dá **"Workable desligou o captcha"**, que é falso —
   três linhas adiante, no mesmo objeto, está `"wjb_acp_turnstile_captcha_enabled":true`, e
   noutro ramo do mesmo JSON está a `turnstileWidgetSiteKey`. A leitura certa é: o Workable
   **trocou** reCAPTCHA por Turnstile, e a flag `recaptcha:false` é o registro da *troca*, não
   da ausência.
2. **Greenhouse.** A chave `GOOGLE_RECAPTCHA_INVISIBLE_KEY` aparece no HTML de **todo**
   anúncio, inclusive nos inquilinos que **desligaram** o captcha. Concluir "tem captcha
   porque a chave está lá" também é errado. Quem decide é **outro campo, do objeto do
   quadro**: `disable_captcha`.

**Regra que sai daí e complementa a de ontem: em SPA, não basta abrir o objeto de
configuração — é preciso achar QUAL campo o código lê.** Prova disso, extraída do bundle do
Greenhouse:

```
const no = (internal, embedded, disabled) => { ... if (!(internal && !embedded) && !disabled) { criar cliente reCAPTCHA } }
... no(!!internal, !!embedded, !!(disable_captcha || preview_mode || hideCaptcha))
```

Com `disable_captcha` verdadeiro **o cliente de reCAPTCHA nem é construído** e o token não é
enviado. A chave continua no HTML e não serve para nada.

---

## 2. O QUE ESTA RODADA NÃO REFEZ, e por quê

- **Não repeti Ashby, Lever nem Personio.** `automacao/caca-ashby-lever-1109.md` fechou as três
  hoje: Ashby parede (reCAPTCHA v2 invisível 6/6), Lever parede (hCaptcha + Cloudflare 8/8),
  Personio sem porteiro (21.208 slugs, 121 quadros, 1 rota nova já enviada).
- **Não repeti Workday.** `automacao/caca-workday-1109.md` o varreu hoje: zero personagem.
- **Não repeti Teamtailor, Recruitee, Pinpoint, Homerun nem BambooHR.** Todos varridos e
  registrados entre 09/09 e 11/09.
- **Não varri Workable em volume.** O enunciado condicionava isso a medir a porta antes de
  prometer. Medi, e o que medi (§6) não sustenta fila.

---

## 3. GREENHOUSE — a lane que a campanha já usa, agora medida por dentro

### 3.1 O achado de plataforma mais útil da rodada: `disable_captcha` é POR INQUILINO e dá para medir por `curl`

O quadro do Greenhouse serve, no HTML da própria página, um objeto de configuração do quadro
que contém, entre outros, `button_shape`, `display_departments`, `preview_mode` e
**`disable_captcha`**. É esse campo, e não a chave do reCAPTCHA, que decide se o envio passa
por pontuação do Google.

Sonda de uma linha, sem navegador:

```
curl -sL "https://job-boards.greenhouse.io/<slug>" | grep -o '"disable_captcha":[a-z]*'
```

**Censo desta rodada, sobre os 376 quadros vivos:**

| Resultado | Quadros | Leitura |
|---|---|---|
| `"disable_captcha":false` | **290** | captcha ligado — é clique dele |
| `"disable_captcha":true` | **5** | **captcha desligado — a automação pode enviar** |
| não avaliável | **81** | 56 publicam no **domínio próprio do empregador** (o objeto não mora no host do Greenhouse), 13 usam o renderizador antigo `boards.greenhouse.io` (que não serve esse campo), 12 têm quadro vazio |

**Os 5 inquilinos sem captcha são:** `gusto`, `latitude` (Latitude AI), `nex` (Nex, Hong Kong),
`raven` (Raven, farmacêutica de Boston) e — o único que interessa — **`wargamingen`, a
Wargaming**.

**E aí vem a parte honesta: a Wargaming não rende nada hoje.** Ela não publica anúncio de
candidatura espontânea nenhum (li os 49 anúncios do quadro), e a única vaga de personagem dela,
a `3D Character Artist (World of Tanks: HEAT)` de Nicósia, id `8161671`, **já recebeu
candidatura em 06/09, uma segunda por engano em 07/09, e foi RECUSADA em 10/09**, com a recusa
dizendo explicitamente que olharam o portfólio. O `dedupe-agora.sh 8161671 "Wargaming"` devolve
uma ocorrência em `enviados.csv`, **seis** em `processados.csv` e três em `index.html`, com
marca de envio nas três seções.

**O que fica escrito para a próxima rodada:** quando aparecer vaga nova na Wargaming, ela é
**candidatura automática**, não fila da mão dele. É o único inquilino de jogos do Greenhouse
medido sem porteiro.

### 3.2 O porteiro do Greenhouse por dentro, e ele explica o código por email da regra 19

O bundle `entry.client` do renderizador de quadros deixa o desenho inteiro à vista:

- A classe de captcha lê `window.ENV.GOOGLE_RECAPTCHA_INVISIBLE_KEY` e chama
  `window.grecaptcha.enterprise.execute(key, {action: "apply_to_job"})` — ou seja, **reCAPTCHA
  Enterprise por pontuação**, não caixa de clicar. Não existe desafio de imagem a resolver;
  existe uma **nota de sessão**, e IP de datacenter reprova.
- O envio monta o corpo assim: se houver `security_code`, manda `security_code`; **senão**
  manda `g-recaptcha-enterprise-token`. E marca `captcha_retried` quando é segunda tentativa.
- A resposta de erro tem dois códigos: `captcha-failed`, que — quando vem com
  `security_code_recipient` — **abre a tela de verificação por email**, e `captcha-retry`.
- A tela de código tem **oito casas** (`bt = 8` no componente `email-verification`).

**É exatamente isto que a regra 19 do briefing descreve por fora.** O código por email não é um
passo a mais do Greenhouse: **é o que acontece quando a pontuação do reCAPTCHA reprova a
sessão.** Daí a espera de seis minutos, daí o código velho não servir na tentativa seguinte
(cada tentativa gera o seu), e daí o `processados.csv` registrar pedido de código na NC America,
na PlayQ, na Brand New School, na Swaybox e na Mob Entertainment.

### 3.3 A rota de dossiê que dispensa abrir a página

O Greenhouse serve a definição do formulário na API pública:

```
https://boards-api.greenhouse.io/v1/boards/<slug>/jobs/<id>?questions=true
```

Devolve `questions[]` com `label`, `required`, `fields[].name`, `fields[].type` e, nas listas,
**todas as opções**. Foi assim que os campos desta fila foram conferidos — **lidos da fonte, não
presumidos**. `boards-api.greenhouse.io/v1/boards/<slug>` devolve o nome da casa, e
`boards-api.greenhouse.io/v1/boards/<slug>/jobs` devolve o quadro inteiro com `internal_job_id`,
que é o identificador que a regra 18 do briefing manda guardar.

**Nota de rede:** `boards-api.eu.greenhouse.io` é recusado por este proxy (`connect_rejected`),
mas **não precisa**: o host americano serve os inquilinos europeus também, e o
`absolute_url` de cada anúncio já vem apontando para `job-boards.eu.greenhouse.io`. Foi assim
que a KSWH e a Tactile Games foram lidas.

### 3.4 O universo de slug, e a confirmação do que ontem já tinha medido

Repeti o método da rodada anterior — nome do estúdio, coluna `token` dos censos, e o **segundo
nível de todo domínio citado no repositório** — e o universo subiu de 21.420 para **83.223
slugs** (12.112 nomes e 8.303 domínios colhidos de `alvos.csv`, `enviados.csv`, `pessoas.csv`,
`processados.csv`, `docs/index.html`, `drafts/`, os `censo-boards-*.csv`, as filas do gamedevmap
e o `garimpo-cgstudiomap.csv`). Rendeu **376 quadros vivos do Greenhouse**.

**Confirmação incômoda, e ela vale registrar:** o slug `2k` **não foi sondado**, porque o meu
filtro exigia mais de dois caracteres. É um quadro que a campanha usa desde 30/08. **O filtro de
comprimento mínimo é um furo do método e fica anotado para a próxima rodada consertar** — slug de
duas letras existe e é justamente o de casa grande.

---

## 4. FILA FINAL NUMERADA — 5 rotas

Ordem: encaixe de personagem primeiro, depois porte da casa, depois confiabilidade da rota.
**Em todas: escopo conferido, disciplina conferida, `dedupe-agora.sh` rodado com OS DOIS
argumentos, grep pelo NOME da casa em `enviados.csv`, `alvos.csv`, `processados.csv` e
`docs/index.html`, e régua de veto passada no texto integral do anúncio.**

> **As 5 precisam do navegador dele.** Todas medem `"disable_captcha":false`, ou seja,
> reCAPTCHA Enterprise por pontuação no envio, com o código de oito dígitos por email como
> desempate. **Nenhuma é candidatura automática.**

---

### 1. Absurd Ventures — `General Game Development Application` — a melhor porta da rodada

- **Por que a casa presta:** estúdio novo de **Dan Houser**, co-criador de *Grand Theft Auto*,
  com sede em **Santa Monica e San Rafael, Califórnia**, e — o que importa aqui — **duas
  divisões**: jogos e **série animada**. O quadro vivo mostra que o jogo está em produção de
  verdade: `Lead Open World Designer`, `Mission Design Lead (Campaign)`, `Principal Gameplay
  Animator`, `Cinematic Technical Designer`, `Software Engineer, Cinematic Tools`. Casa de mundo
  aberto narrativo em produção é casa que vai contratar personagem. **Casa 100% nova para a
  campanha.**
- **URL exata:** `https://job-boards.greenhouse.io/absurdventures/jobs/4141408007`
- **ID da requisição:** `4141408007` · **`internal_job_id`: `4098775007`**
- **Local:** `Santa Monica OR San Rafael` (escritório declarado: Santa Monica). Publicada em
  **09/11/2023**, atualizada em **22/05/2025**, ainda listada.
- **Medido:** **HTTP 200, 46.638 bytes.**
- **Sinal de captcha (medido, não grepado):** `"disable_captcha":false` no objeto do quadro, e a
  chave de plataforma `6Lfmcbcp…LFX0` presente → **reCAPTCHA Enterprise por pontuação ligado**.
- **Campos do formulário conferidos** (lidos em `?questions=true`, não presumidos):
  `first_name` (obrigatório), `last_name` (obrigatório), `email` (obrigatório), `phone`,
  `resume` **arquivo, obrigatório**, **`cover_letter` arquivo, OBRIGATÓRIO** (é a única da fila
  que exige carta), `question_4835774007` *Website or portfolio link* (texto),
  `question_4835775007` *Work samples* (**arquivo**), `question_4835776007` *LinkedIn Profile*,
  `question_4835777007` *Are you lawfully authorized to work in the United States?*
  (lista **Yes/No**, obrigatória), `question_4835778007` *Are you able to work in our Santa
  Monica, CA or San Rafael, CA office?* (lista **Yes/No**, obrigatória),
  `question_4835779007` *How many games/products have you launched?* (lista
  **0 / 1-3 / 3-5 / 5-10 / 10+**, obrigatória). Sem consentimento GDPR.
- **Como responder, pela regra do briefing:** a caixa de autorização nos EUA é a da **regra 8** —
  responde-se **No** e o caso de visto vai no campo livre; **nunca mentir ali**. A caixa de
  escritório é de disponibilidade, não de autorização, e a posição da campanha (regra 4) é que
  ele quer realocar.
- **Texto integral do anúncio** (são 201 caracteres, cabem inteiros): *"We will be staffing more
  roles for our Game Development teams in the future. If you would like to submit a general
  application purely for us to have your resume on file, feel free to do so here."*
- **Régua de veto neste anúncio: ZERO acertos** de `authoriz`, `eligib`, `sponsor`,
  `work permit`, `must be based`, `reside`, `relocat`, `only`, `citizen` no texto.
- **Dedupe:** `sh automacao/dedupe-agora.sh 4141408007 "Absurd Ventures"` → **seção 1: nenhuma
  ocorrência nos quatro arquivos. Seção 2: nenhuma marca de envio. Seção 3: nada.** Por nome:
  `Absurd` = **0** em `enviados.csv`, **0** em `alvos.csv`, **0** em `processados.csv`, **0** em
  `docs/index.html`. **Casa 100% nova.**
- **Precisa de navegador? SIM.**

### 2. Jam Filled — `Expression of Interest` — a única com departamento de modelagem nomeado

- **Por que a casa presta:** estúdio de animação canadense com três unidades (**Toronto, Ottawa,
  Halifax**), série para TV e streaming. **Canadá anglófono é a prioridade 1 da fila do Jhon.** E
  o que faz esta linha valer mais que o resto: no seletor obrigatório de departamento existe a
  opção literal **`CG Assets (Modeling/Surfacing)`** — a disciplina dele, pelo nome, sem ter que
  entrar por porta de outra função.
- **URL exata:** `https://job-boards.greenhouse.io/jamfilled/jobs/7685474003`
- **ID da requisição:** `7685474003` · **`internal_job_id`: `5740534003`**
- **Local:** `Toronto, Ottawa, Halifax`; escritório declarado `Jam Filled - Toronto`. Publicada em
  **01/04/2026**, atualizada em **01/06/2026**.
- **Medido:** **HTTP 200, 49.618 bytes.**
- **Sinal de captcha (medido):** `"disable_captcha":false` → **reCAPTCHA Enterprise ligado**.
- **Campos do formulário conferidos:** `first_name` (obr.), `last_name` (obr.),
  `preferred_name`, `email` (obr.), `phone`, `resume` **arquivo, obrigatório**, `cover_letter`
  arquivo (opcional), `question_30476363003` *Are you currently residing in Ontario?* (**Yes/No**,
  obrigatória), `question_30279613003` *Your Current Location* (texto, obrigatória),
  `question_30279614003` *Please include a link to your portfolio or demo reel* (textarea,
  **obrigatória**), `question_30279615003` *Password for reel or portfolio if applicable*,
  `question_30279611003` *Please select the department or role you are most interested in*
  (lista obrigatória com **22 opções**, entre elas **`CG Assets (Modeling/Surfacing)`**, e
  também `CG Rigging`, `CG Animation`, `CG FX`, `CG Lighting and Compositing`, `Design`,
  `Matte Painting`, `Storyboards`, `Pipeline`), `question_30279612003` *Eligibility to work in
  Canada* (lista obrigatória de três: *legally entitled without restriction on a permanent
  basis* / *valid open work permit* / **`I will require a work permit`**),
  `question_30290537003` *hybrid, até 3 dias por semana num dos estúdios* (**Yes/No**,
  obrigatória), `question_30279616003` *LinkedIn Profile*, `question_30279617003` *earliest
  start date* (texto, obrigatória). Sem consentimento GDPR.
- **Leitura importante da caixa de elegibilidade:** ela **tem** a opção *"I will require a work
  permit"*. Isso é o contrário de veto — é a casa **prevendo** candidato que precisa de visto.
  Pela regra do briefing (patrocínio é contexto, não critério), a rota fica.
- **Texto do anúncio, na parte que decide:** *"**The Expression of Interest posting does not
  represent an active job opportunity or current open position at Jam Filled**. The purpose of
  the Expression of Interest posting is to gather candidate information into our system to
  consider you for future job openings… Don't see the job you're looking for? Fear not! We're
  always on the lookout for future Jam Friends… So, send us your reel!"*
- **Régua de veto: ZERO acertos** no texto integral.
- **Dedupe:** `sh automacao/dedupe-agora.sh 7685474003 "Jam Filled"` → **seção 1: uma ocorrência,
  em `index.html`, e ela diz *"ROTA OFICIAL NOVA, achada em 02/09 no Greenhouse do próprio
  estúdio"*. Seção 2: NENHUMA marca de envio. Seção 3: nada.** Por nome: `Jam Filled` = **2** em
  `enviados.csv`, **1** em `alvos.csv`, **7** em `processados.csv`, **5** em `index.html`.
- **O que o grep por nome mostra, e você precisa saber antes de clicar:** a casa **já recebeu
  dois emails frios** — um pré-campanha em 11/07 e outro em 26/08, os dois para
  `contact@jamfilled.com`, o segundo com follow-up em 02/09, **e nenhum foi respondido**. A rota
  do Greenhouse foi registrada em 02/09 como "rota oficial média" e **nunca foi enviada**. Ou
  seja: não é repetição de candidatura, é a **primeira** candidatura por porta oficial numa casa
  que ignorou o endereço genérico duas vezes.
- **Precisa de navegador? SIM.**

### 3. Tactile Games — `Open Applications` — casa 100% nova, Copenhague

- **Por que a casa presta:** **350 pessoas em Copenhague**, uma das maiores de jogos da
  Dinamarca, dona de *Lily's Garden*. Escopo europeu, casa grande o bastante para ter time de
  arte de verdade, e o anúncio é balcão aberto. **Casa 100% nova para a campanha.**
- **URL exata:** `https://job-boards.eu.greenhouse.io/tactilegames/jobs/4319957101`
- **ID da requisição:** `4319957101` · **`internal_job_id`: `4202106101`**
- **Local:** `København, Capital Region of Denmark, Denmark`. Publicada em **09/04/2024**,
  atualizada em **18/06/2026**.
- **Medido:** **HTTP 200, 45.374 bytes.**
- **Sinal de captcha (medido):** `"disable_captcha":false` → **reCAPTCHA Enterprise ligado**.
- **Campos do formulário conferidos:** `first_name` (obr.), `last_name` (obr.), `email` (obr.),
  `phone`, `resume` **arquivo, obrigatório**, `cover_letter` arquivo (opcional),
  `question_5621263101` *LinkedIn Profile*, `question_5621264101` *Portfolio*,
  `question_5621273101[]` *What role(s) are you interested in?* (**multi-seleção obrigatória**,
  32 opções; as de arte são `3D Artist`, `2D Artist`, `3D Animator`, `2D Animator`,
  `Concept Artist`, `Graphic Designer`, `Motion Graphics Designer`, `Technical Artist`,
  `UI Designer`, mais `Other (please specify in the textbox below)`), `question_6098143101`
  *Other:* (texto livre), `question_5621275101` **pretensão salarial em DKK, mensal, bruto**
  (texto, obrigatória), `question_5621274101` *2-3 key skills* (textarea, obrigatória),
  `question_5621267101` *a time when you felt really motivated at work* (textarea, opcional).
- **Atenção, e esta é a única da fila com isso: exige TRÊS consentimentos de GDPR**
  (`requires_consent`, `requires_processing_consent`, `requires_retention_consent`), com
  **retenção de 365 dias** declarada. Formulário não passa sem marcar os três.
- **Ressalva honesta de disciplina:** **não existe `Character Artist` na lista de cargos.** O
  mais próximo é `3D Artist`, e a casa faz puzzle casual, onde o personagem não é o produto. É
  uma porta legítima e uma casa grande, mas **não é o encaixe que a Absurd Ventures ou a Jam
  Filled são.** O campo `Other:` existe e é onde a palavra *Character* pode entrar escrita.
- **Texto do anúncio, na parte que decide:** *"**Didn't find the opportunity you were looking
  for?** Please do let us know about your background and career ambitions, and we will be in
  touch should anything come up!"*
- **Régua de veto: ZERO acertos** no texto integral. **Régua de francês: não se aplica.**
- **Dedupe:** `sh automacao/dedupe-agora.sh 4319957101 "Tactile Games"` → **seção 1: nenhuma
  ocorrência nos quatro arquivos. Seção 2: nenhuma marca de envio. Seção 3: nada.** Por nome:
  `Tactile` = **0** em `enviados.csv`, **0** em `alvos.csv`, **0** em `processados.csv`, **0** em
  `docs/index.html`. **Casa 100% nova.**
- **Precisa de navegador? SIM.**

### 4. Absurd Ventures — `General Animated Series Application` — a segunda porta da mesma casa

- **Por que existe separada:** a Absurd Ventures publica **sete** balcões gerais, um por divisão
  (`Game Development`, `Animated Series`, `Film & TV`, `Comics/Graphic Novels`,
  `Audio Fiction`, `Creative Services`, `Corporate`). São **requisições diferentes, com
  `internal_job_id` diferentes**, e o currículo cai em fila diferente. O crédito de **Wingfeather
  Saga** é de série animada; esta é a porta onde ele é mais forte.
- **URL exata:** `https://job-boards.greenhouse.io/absurdventures/jobs/4141404007`
- **ID da requisição:** `4141404007` · **`internal_job_id`: `4098713007`**
- **Local:** `Santa Monica OR San Rafael`. Publicada em **09/11/2023**, atualizada em
  **22/05/2025**.
- **Medido:** **HTTP 200, 44.077 bytes.**
- **Sinal de captcha (medido):** `"disable_captcha":false` → **reCAPTCHA Enterprise ligado**.
- **Campos do formulário conferidos:** iguais aos da #1 **menos duas coisas**: aqui a
  **`cover_letter` é OPCIONAL** e **não existe** a pergunta *How many games/products have you
  launched?*. As duas caixas obrigatórias de lista continuam: `question_4835737007`
  *Are you lawfully authorized to work in the United States?* (**Yes/No**) e
  `question_4835738007` *Are you able to work in our Santa Monica, CA or San Rafael, CA office?*
  (**Yes/No**). Sem consentimento GDPR.
- **Texto integral:** *"We will be staffing more roles for our Animated Series teams in the
  future. If you would like to submit a general application purely for us to have your resume on
  file, feel free to do so here."*
- **Régua de veto: ZERO acertos.**
- **Dedupe:** `sh automacao/dedupe-agora.sh 4141404007 "Absurd"` → **seção 1: nenhuma ocorrência.
  Seção 2: nenhuma marca de envio. Seção 3: nada.**
- **Ordem recomendada:** mandar a **#1 primeiro** e esta depois, no mesmo dia ou no seguinte. São
  divisões diferentes do mesmo grupo e o texto de cada uma diz explicitamente que é para
  *"our <divisão> teams"*, então não é batida repetida na mesma porta.
- **Precisa de navegador? SIM.**

### 5. Atomic Cartoons — `Expression Of Interest - LA` — entra com ressalva escrita

- **Por que a casa presta:** animação para TV e streaming, grupo Blue Ant, com unidades em
  Vancouver e Los Angeles. O quadro vivo tem `CG Designer`, `Unreal CG Supervisor` e
  `Unreal Previs and Layout Supervisor`, ou seja, pipeline de CG de verdade.
- **URL exata:** `https://job-boards.greenhouse.io/atomiccartoons/jobs/7565513003`
- **ID da requisição:** `7565513003` · **`internal_job_id`: `5691253003`**
- **Local:** `Los Angeles`. Publicada em **02/01/2026**, atualizada em **08/06/2026**.
- **Medido:** **HTTP 200, 55.139 bytes.**
- **Sinal de captcha (medido):** `"disable_captcha":false` → **reCAPTCHA Enterprise ligado**.
- **Campos do formulário conferidos:** `first_name` (obr.), `last_name` (obr.), `email` (obr.),
  `phone`, `resume` **arquivo, obrigatório**, `cover_letter` arquivo (opcional),
  `question_29030023003` *department or role* (**lista obrigatória de 14**),
  `question_29030024003` *Are you legally entitled to work in US for any employer, without
  restriction on a permanent basis?* (**Yes/No**, obrigatória — é a caixa da regra 8),
  `question_29030025003` *Your Current Location* (obr.), `question_29030026003` *portfolio or
  reel*, `question_29030027003` *senha do portfólio*, `question_29030028003` *LinkedIn*,
  `question_29030029003` *earliest start date* (obr.), `question_29030030003` *new graduate
  2026?* (lista obr. de 5), `question_29030033003` *Have you previously worked at Atomic
  Cartoons?* (**Yes/No**, obr.), `question_29030034003` *se sim, qual produção*.
- **LEIA ISTO ANTES DE CLICAR — são duas ressalvas, e as duas são sérias.**
  **(a)** A lista de departamentos da porta de **LA** é `Storyboards`, `Design`, `Editorial`,
  `Directorial`, `Production`, `Finance/Accounting`, `Human Resources`,
  `Sales and Distribution`, `Business Affairs/Legal`, `IT`, `Pipeline`, `Development`,
  `Current Series`, `Scripted Content`. **NÃO existe bucket de CG nem de modelagem** — ao
  contrário da porta de Vancouver da mesma casa, que tem. Marcar aqui é entrar pela **porta de
  entrada da regra 13**, de propósito, declarando na primeira linha do campo livre que a área
  dele é personagem.
  **(b)** A casa **já recebeu uma candidatura**: a `Expression Of Interest - Vancouver`,
  `7565498003`, **enviada e confirmada em 06/09 às 18h11**, com email de confirmação vindo do
  domínio do próprio estúdio (`no-reply@atomiccartoons.com`). E o painel registra **veto de
  residência na província (BC)** para o lado de Vancouver. Esta é requisição **diferente**, em
  país diferente, e **não repete o texto do veto** — pela régua do briefing ela fica na fila.
  Mas é a **segunda batida na mesma casa**, e quem decide o desgaste é você.
- **Régua de veto no texto integral:** um acerto de `citizen`, e ele está no **parágrafo
  padrão de igualdade de oportunidades** (*"without regard to race, ancestry, place of origin…
  citizenship…"*), que é o contrário de veto. **Nenhum veto real.**
- **Dedupe:** `sh automacao/dedupe-agora.sh 7565513003 "Atomic Cartoons"` → **seção 1: nenhuma
  ocorrência do ID nos quatro arquivos. Seção 2: nenhuma marca de envio. Seção 3: duas linhas,
  as duas citando o veto de província de Vancouver** (uma delas na ficha da Hydraulx,
  comparando).
- **Precisa de navegador? SIM.**

---

## 5. O QUE CAIU, E POR QUÊ — o negativo medido vale tanto quanto o positivo

### 5.1 Caiu no dedupe por ID (já enviada, com prova no painel)

| Casa | Rota espontânea | ID | Quando saiu |
|---|---|---|---|
| **Crystal Dynamics** | General Application, Remote/Flexible | `4352498005` | 07/09, `/confirmation` + *Thanks for Applying* |
| **Unknown Worlds** | General Application, Remote | `7535230002` | 07/09, *Thank you for applying to Unknown Worlds!* |
| **NC America / NCSOFT West** | Open Applications, Irvine CA | `4052911009` | 07/09, com **código de segurança por email** |
| **PlayQ** | Don't See What You're Looking For?, Santa Monica | `3055199` | 07/09, departamento Art, com código por email |
| **Tripwire Interactive** | General Application, Remote USA | `8282003002` | 07/09 — **e já RECUSADA em 07/09** |
| **Atomic Cartoons (Vancouver)** | Expression Of Interest, Vancouver | `7565498003` | 06/09 |
| **KSWH / Keen Software House** | Spontaneous applications, Praga | `4880719101` | 10/09, pelo formulário de convite `s101.recruiting.eu.greenhouse.io` |
| **Sony Pictures Imageworks** | Expression of Interest | `4551278003` | casa com histórico extenso; ver a regra 18 do briefing |
| **Wargaming** | não tem rota espontânea; a vaga de personagem `8161671` | `8161671` | 06/09 e 07/09, **recusada em 10/09** |

### 5.2 CAIU NO DEDUPE **POR NOME**, com o ID limpo — a lição de ontem se repetiu duas vezes

O `caca-ashby-lever-1109.md` já tinha escrito que dedupe por ID é obrigatório e **insuficiente**,
porque a entrada antiga do painel guardava a URL do quadro e não o ID. **Aconteceu de novo, em
duas casas, e as duas teriam virado candidatura repetida:**

- **Brand New School** — `General Interest - Apply Now` (`5818240004`), Londres / LA / Nova York.
  `dedupe-agora.sh 5818240004 "Brand New School"` devolve **"nenhuma ocorrência — o ID é inédito
  nos quatro arquivos"**. O grep por nome devolve, no `docs/index.html`:
  *"CANDIDATURA ENVIADA e CONFIRMADA em 06/09 pela força-tarefa… Porta Greenhouse, com código de
  segurança por email lido no Gmail e devolvido com a sessão viva"*, e a célula guarda
  **`https://boards.greenhouse.io/brandnewschool`** — a URL do quadro, sem ID nenhum.
  *(Além disso a casa é de design de marca e não de personagem, o que o próprio
  `processados.csv` já tinha escrito em 06/09.)*
- **Firaxis** — `Join Our Talent Community` (`6270031003`), Sparks Glencoe, Maryland.
  `dedupe-agora.sh 6270031003 "Firaxis"` devolve **ID inédito**. O grep por nome devolve, no
  `processados.csv`: **`2026-09-07,Firaxis Games,EUA (Sparks MD),https://firaxis.com,ENVIADA,Join
  Our Talent Community confirmada por email as 06h40 de no-reply@firaxis.com`** — e a célula
  guarda **o domínio institucional**, não o id do ATS.

**As duas passariam.** Este dossiê chegou a ficar pronto para a Firaxis, com os campos lidos e o
texto conferido, antes do grep por nome derrubar. **Fica a regra, agora medida em dois dias
seguidos: ID limpo não é dedupe; é metade do dedupe.**

### 5.3 Caiu por disciplina ou por escopo, com o motivo escrito

- **Rushdown Studios** (`4093292009`, `General Interest - Other`, US remoto) — casa nova e sem
  histórico, mas o quadro inteiro dela são **quatro vagas e três são de engenharia de backend**
  (`Backend Engineer (Golang)`, `Senior Backend Engineer (C++)`, `Senior DevOps`). É co-dev de
  infraestrutura de multiplayer, **não publica arte nenhuma**, e o próprio departamento do
  anúncio é `Other`. Além disso o texto lista os estados onde a casa pode contratar remoto
  (NY, CT, DE, GA, KS, MA, MD, NC, OH, PA, TX, WI). Não é veto escrito, mas não há para onde
  encaminhar um modelador.
- **Zero Studios** (`4648558005`, `General Employment Inquiry`, NYC/LA/MKE/Remoto) — o quadro é
  `Designer: Marketing & Social` e `Social Content Creator`. Agência de conteúdo social.
- **Sphere Entertainment** (`5197060007` *EXPRESSION OF INTEREST - Art Director*, `5197043007`
  *Designer*, `5197050007` *Creative Director*, Burbank) — são balcões **por cargo**, e nenhum
  dos três cargos é modelagem. Diretor de arte não é o cargo da regra 2.
- **Outfit7** (Liubliana/Limassol/Barcelona) — os três `Talent Pool` são para **Product Manager**,
  **Growth Product Manager** e **estudante**. Nenhum de arte.
- **2K Madrid** (`4418963003`, *2K Madrid General*) — o quadro de Madrid é **inteiro de
  localização e LQA** (13 anúncios, todos). Não há arte na unidade.
- **Whatwapp** (`4200882101`, Milão) — o quadro tem três anúncios, dois deles `Head of UA` e
  `Product Manager`. Não há evidência de time de arte.
- **Nex** (Hong Kong) — é um dos 5 inquilinos sem captcha e tem `3D Game Artist` e
  `3D Game Environment Artist`, **mas Hong Kong está fora do escopo** (Ásia só Coreia do Sul e
  Singapura).
- **Fora de indústria, medidos e descartados:** Action Garage Doors, Red Mountain Garage Doors,
  Carta, Cloudflare, Gusto, Oscar Health, Gallup, Netlify, Spire, ZipRecruiter, ZoomInfo, Zwift,
  Indigo, Numa, LINK, Lighthouse, MAP, Avanath, KKR, Automattic, Pulse Healthcare,
  Echo Neurotechnologies, GoodAI, Goodman, CLEVR, Relai, Neo Cybernetica, Zoo (que é fabricante
  de CAD, não estúdio), SHADOW e Fanatics Collectibles.

### 5.4 As vagas de personagem que a varredura encontrou — e o que já era conhecido

Dos 10.755 anúncios lidos, **64 batem na régua de disciplina**. Passando o dedupe, **nenhuma é
vaga de personagem inédita e aproveitável**: Bluehole, Loonshot, Cloud Chamber, Wargaming,
Scopely, Riot, Epic, Good Job Games, Mob Entertainment e Sony Pictures Imageworks já estão todas
no painel, enviadas ou recusadas. As de Seul e Pangyo são Coreia do Sul, que está no escopo, mas
são as mesmas requisições já registradas. **Duas que merecem uma conferência numa próxima rodada
de vaga aberta, porque não são espontâneas e por isso não entram nesta fila:**
`hasbro 4318250009 Lead Character Artist (Canadá)` e
`swayboxstudios 4337820009 CG Modeler / 4337866009 Senior CG Generalist (Modeler)` em
Nova Orleans — a Swaybox, segundo o `processados.csv`, já teve candidatura confirmada pelo
Greenhouse em 04/09, então é conferir e não presumir.

---

## 6. JOIN.COM — a lane foi varrida inteira e está VAZIA para a disciplina dele

### 6.1 Como se mede um inquilino do join.com, sem navegador

- **Existência:** `HEAD https://join.com/companies/<slug>` devolve **200** se existe e **404** se
  não. O subdomínio `https://<slug>.join.com/` redireciona 200 para a mesma página, logo é a
  mesma rota com outro nome — **não são dois universos**.
- **Se a porta espontânea existe:** o `__NEXT_DATA__` da página traz
  `props.pageProps.initialState.company.preference.**isSpontaneousApplicationEnabled**`. É
  **booleano, por inquilino**, e é a resposta exata do que o enunciado pediu.
- **A rota, quando ligada:** `https://join.com/companies/<slug>/spontaneous-application`, que
  entrega o assistente em `https://join.com/companies/<slug>/apply`. Medido na GameDuell:
  **200 / 101.343 bytes** e **200 / 307.696 bytes**, com `<title>Spontaneous Application at
  GameDuell</title>`.

### 6.2 O censo, e ele é um negativo limpo

| Medida | Número |
|---|---|
| Slugs sondados | **83.223** |
| Inquilinos vivos (HTTP 200) | **526** |
| Inquilinos com **alguma** vaga publicada | **67** |
| Vagas publicadas somadas nos 526 | **290** |
| Inquilinos com `isSpontaneousApplicationEnabled: **true**` | **12** |
| Desses 12, casas de jogos, animação ou VFX | **1** (GameDuell) |
| Desses 12, com vaga de personagem, modelagem, textura, look dev ou groom | **ZERO** |

**Os 12 com a porta aberta, por extenso:** Accenture (Zurique), coverletter.tech (Bucareste),
Excellent Personaldienstleistungen (Sursee), expert Warenvertrieb (Langenhagen), Future Energy
Ventures (Berlim), **GameDuell (Berlim)**, Game House Dortmund, Lead Concept, LOS-Verbund
(Saarbrücken), Magic Media GmbH (Berlim, empresa de **pessoal de evento** — **não** é a Magic
Media de outsourcing de jogos), RealStudio (Berlim) e Vox AI.

**A única casa de jogos com a porta aberta é a GameDuell**, e ela não serve: o quadro dela tem
duas vagas e a de arte é **`Game UI Artist (Unity 2D)`**. É casa de jogo de cartas casual em 2D.
Entrar por ali seria porta de entrada da regra 13 numa casa **sem pipeline 3D**, o que é
diferente de porta de entrada numa casa que tem o departamento e não tem a vaga. **Não entra na
fila.**

**E o denominador honesto:** o join.com **tem** casas de jogos de verdade — foram medidas **40**
com sinal de jogos, animação ou VFX no nome ou no setor, entre elas **BeamNG, DECK 13, Chimera
Entertainment, Klang Games, Travian Games, Microids, ScanlineVFX, Keywords Studios, handy-games,
remote control productions, Massive Miniteam, Nurogames, Bright Future, Puny Astronaut (Dundee),
Urban Games (Schaffhausen), Booming Games, Deca, Tribes Studio, Waypoint Studios, Thera Bytes e
Redox Interactive**. **Todas as 40 têm `isSpontaneousApplicationEnabled: false`**, e só cinco
delas publicam alguma vaga hoje (Booming Games, GameDuell, Game House Dortmund, handy-games e
RealStudio), nenhuma de personagem.

**Conclusão da lane, e ela é definitiva até a flag de alguma dessas casas virar:** o join.com é
um ATS de PME alemã e suíça. As casas de jogos que estão lá usam o quadro para vaga aberta e
**mantêm a candidatura espontânea desligada**. Não há o que colher.

### 6.3 O porteiro do join.com, medido no objeto de configuração e no bundle

Não se chegou a precisar, mas fica medido porque o enunciado pede e porque poupa a próxima
rodada:

- A página serve `var env = {…}` com **`RECAPTCHA_SITE_KEY: 6LcBKJEdAAAAAOns5uYTQrLbrHXWtoFXb5sMjmxH`**
  e `GRAPHQL_API_URL: https://join.com/candidate-api/graphql`.
- No bundle do app de candidato, o carregador monta o script como
  **`https://www.google.com/recaptcha/api.js?render=${key}`** e o cliente chama
  **`grecaptcha.execute(key, {action: <ação>})`**. Essa é a assinatura de **reCAPTCHA v3 por
  pontuação**, não de caixa de clicar. O app ainda injeta
  `.grecaptcha-badge{display:none !important}` para esconder o selo.
- **O submit da espontânea é uma das ações protegidas**, e isso está escrito no código:
  `handleSpontaneousApplicationSubmit` faz `await <recaptcha>("SpontaneousApplication")` e manda
  o token em `context:{recaptchaToken:t}` junto da mutação. A ação
  **`SpontaneousApplicationSendVerificationLinkToken`** — o envio do link de verificação por
  email — **também** é protegida, e existe uma mensagem de erro dedicada (`recaptchaError`).
- O cliente ainda manda cabeçalhos **`fingerprint`** e **`uberctx-fingerprint`** em cada chamada.
- O assistente tem **passo de verificação de email por link** (`verification`,
  *"Verify your email address"*, *"Resend verification mail"*) antes do `success`.
- **Cloudflare:** `https://join.com/companies/sitemap-jobs-index.xml` responde **403 com a página
  *Attention Required! | Cloudflare*** para esta rede. O `sitemap-index.xml` responde 200, então
  é regra de WAF por caminho, não bloqueio geral.

**Veredito: parede de pontuação mais link por email.** Se algum dia uma dessas casas ligar a
flag, a rota é do navegador dele, com acesso ao email na mesma sessão.

### 6.4 Os campos do assistente do join.com — e a etiqueta honesta do que isso é

**O formulário do join.com NÃO vem servido no HTML** — o assistente é montado no cliente. Então
**não foi lido do HTML servido**, e eu não vou fingir que foi. O que foi lido são os **nomes dos
passos no código do assistente** e o **catálogo de mensagens do próprio app**, que vêm no
`__NEXT_DATA__`. Pelos dois, os passos são:

`authentication` → `personalInformation` (nome, sobrenome, email, telefone, país de residência,
cidade com autocompletar, bio, foto) → `cv` (upload, limite 10 MB) → `coverLetter` (upload) →
documentos adicionais (**portfolio**, certificado, diploma, carta de recomendação, visto) →
`professionalLinks` (**Portfolio**, LinkedIn, Behance, GitHub, XING, site pessoal) →
`startAvailability` (lista fechada: imediato / 2 semanas / 1, 2, 3 meses / mais de 3) →
`salaryExpectation` (valor bruto, com moeda e periodicidade) → `workAuthorization` (quatro
opções, entre elas *"I require a new sponsorship"*) → perguntas de triagem da casa →
`review` com consentimento de termos e política → `verification` por link de email → `success`.

---

## 7. WORKABLE — medi antes de prometer, e a medição não sustenta fila

O enunciado condicionava esta lane a medir antes. Medi. **Duas coisas mudaram desde a nota de
06/09 da campanha, e as duas pioram o quadro.**

**(a) O porteiro deixou de ser reCAPTCHA e passou a ser Cloudflare Turnstile.** No
`apply.workable.com/<slug>/` o objeto `window.careers` traz **`"recaptcha":false`** — e é
exatamente aí que a medição preguiçosa erra. No mesmo objeto:
`"wjb_acp_turnstile_captcha_enabled":true` e
`"config":{"turnstileWidgetSiteKey":"0x4AAAAAAAVY8hH3nz6RxaK0"}`. **A chave é idêntica em dois
inquilinos diferentes** (Nexus Studios e Cognizant), logo é **chave de plataforma**, o mesmo
padrão do Ashby. O bundle do app de candidatura ainda carrega a mensagem de falha do Turnstile:
*"We couldn't process your request. Please access the application from a different browser and
try again."* — o que confirma que o widget faz parte do fluxo de envio e tem caminho de erro
visível ao candidato. **Ressalva do que NÃO medi:** o `turnstile.render` em si mora num pedaço
carregado sob demanda que eu não abri; o que está medido é a **configuração servida** e a
**mensagem de erro do fluxo**, não a linha que desenha o widget.

**(b) Somando a isso, a página injeta o desafio JS do Cloudflare**
(`/cdn-cgi/challenge-platform/scripts/jsd/main.js`, num iframe de 1×1 pixel), e a API de dados
**recusa esta rede**: `POST apply.workable.com/api/v3/accounts/<slug>/jobs` devolveu **429 com
`error code: 1015`** logo na primeira chamada, e depois de 1.500 sondagens o
`api/v1/accounts/<slug>` passou a devolver **1015 para tudo**, inclusive para inquilino que
minutos antes respondia 200. **808 de 1.500 sondagens foram recusadas com 1015.**

**(c) Armadilha de método que descobri e que precisa ficar escrita, senão a próxima rodada conta
inquilino que não existe:** o endpoint
`apply.workable.com/api/v1/widget/accounts/<slug>?details=true` **devolve 200 com dados de OUTRA
empresa** para slug inexistente. Sondando `10-chambers` ele devolveu **Cognizant Technology
Solutions**; sondando `1000orks` devolveu **Iqra University**. Ele **não serve como sonda de
existência** — e com ele eu teria escrito "422 inquilinos do Workable em 1.500 slugs", que é
mentira. A sonda honesta é `api/v1/accounts/<slug>?details=true`, que devolve **404** de
verdade (conferido com `wooga`) e o campo `subdomain` para bater — mas essa é justamente a que o
1015 fechou.

**Veredito da lane: parede medida, e censo NÃO AVALIÁVEL por esta rede.** Não construí fila e não
vou prometer uma. A rota espontânea que a campanha já conhecia lá — `General Application` da
Nexus Studios, shortcode `4F41AEB27C`, ainda viva e listada — continua registrada no painel como
**inconclusiva por 1015**, e o `processados.csv` já diz isso desde 09/09. Nada a acrescentar
sem sair desta rede.

---

## 8. FERRAMENTAS E SONDAS QUE ESTA RODADA DEIXA PRONTAS

Nada foi commitado como script novo — são uma linha cada, e ficam aqui para copiar:

```sh
# Greenhouse: o quadro inteiro, com internal_job_id (a chave do dedupe da regra 18)
curl -s "https://boards-api.greenhouse.io/v1/boards/<slug>/jobs"

# Greenhouse: os CAMPOS do formulário, lidos da fonte e não presumidos
curl -s "https://boards-api.greenhouse.io/v1/boards/<slug>/jobs/<id>?questions=true"

# Greenhouse: o porteiro, POR INQUILINO — true quer dizer que a automação pode enviar
curl -sL "https://job-boards.greenhouse.io/<slug>" | grep -o '"disable_captcha":[a-z]*'

# join.com: existe o inquilino? (200 existe, 404 não)
curl -sI -o /dev/null -w '%{http_code}\n' "https://join.com/companies/<slug>"

# join.com: a porta espontânea está ligada?
curl -s "https://join.com/companies/<slug>" | grep -o '"isSpontaneousApplicationEnabled": *[a-z]*'

# Workable: o porteiro de hoje (Turnstile), e NÃO o features.recaptcha
curl -s "https://apply.workable.com/<slug>/" | grep -o '"turnstileWidgetSiteKey":"[^"]*"'
```

---

## 9. O QUE EU NÃO CONSEGUI MEDIR, DITO SEM MAQUIAGEM

1. **81 dos 376 quadros do Greenhouse não tiveram o `disable_captcha` medido.** 56 porque o
   quadro é servido no **domínio do próprio empregador** (Epic Games, Bandai Namco América, AKQA,
   Daybreak Games, 5CA e mais 51), 13 porque usam o renderizador antigo `boards.greenhouse.io`,
   que não serve esse campo (AppLovin, Scopely, MobilityWare, Vox Media, Cloudflare, Brand New
   School e outros), e 12 porque o quadro está vazio. **Para esses 81 a resposta é "não
   avaliável", nunca "sem captcha".**
2. **Não abri o pedaço de JavaScript que renderiza o Turnstile do Workable.** O que medi é a
   configuração servida e a mensagem de erro do fluxo de candidatura. É forte, mas não é a linha
   do `render`.
3. **Não fiz introspecção no GraphQL do join.com** e não disparei nenhuma mutação lá — nem de
   leitura com efeito. A lista de campos do assistente vem do código do próprio app, e está
   etiquetada como tal em §6.4.
4. **O slug `2k` ficou de fora do universo** por um filtro meu de comprimento mínimo. É um furo
   conhecido e está escrito em §3.4.
5. **O censo do Workable não existe.** A rede foi fechada com 1015 antes de qualquer número
   confiável, e a sonda alternativa devolve dados de outra empresa. Escrever número ali seria
   inventar.
