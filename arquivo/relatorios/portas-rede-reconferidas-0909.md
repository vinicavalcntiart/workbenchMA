# Portas fechadas por REDE, reconferidas em 09/09

**Regra que gerou esta caça, e ela acabou de se pagar:** em 07/09 a Game Boost foi fechada como
"NÃO ALCANÇADA PELA NOSSA REDE" com 502 e *Hostname does not match certificates altnames*; em 09/09
respondeu 200 e a candidatura saiu com página de agradecimento na tela. **502, 403, 429, 1015 e
timeout do proxy são ESTADO, não veredito.** Parede de captcha é do estúdio e não cai sozinha;
bloqueio de rede cai.

Tudo abaixo foi medido por `curl`, sem navegador, no máximo 5 conexões simultâneas, entre
04h38 e 04h50 UTC de 09/09. Nenhuma candidatura foi enviada, nenhum formulário foi preenchido,
nenhum arquivo protegido foi tocado.

---

## PLACAR

| Medida | Número |
|---|---|
| Entradas varridas (array PORTAIS de `docs/index.html`) | 775 |
| Entradas varridas (`automacao/FILA-DO-VINI.md`) | 46 blocos |
| Casamentos brutos dos termos de rede | **90** (89 no PORTAIS + 1 na FILA) |
| Descartadas por impedimento ser CAPTCHA NOMEADO (Turnstile, reCAPTCHA, DataDome, hCaptcha) | 11 |
| Descartadas por VETO ESCRITO no anúncio | 4 |
| Descartadas por vaga expirada / casa fechada / quadro vazio já resolvido | 17 |
| Descartadas por já enviada (`done=true` ou lista de não-repetir) | 14 |
| Descartadas por serem entrada de MÉTODO/levantamento, não porta | 10 |
| Descartadas por escopo geográfico (Room 8 Studio) | 1 |
| **Entradas com impedimento de REDE de verdade → reconferidas** | **29** |
| Tiros disparados (URL registrada + cabeçalho de navegador + rota de candidatura + controle) | 76 |
| **Voltaram a responder** | **9** |
| Continuam bloqueadas | 14 |
| **Inconclusivas: responderam 200 mas o teste não mediu nada** | **6** |
| Das 9 que voltaram, ainda têm vaga/porta viva | 3 |
| Passaram a régua de vinte termos | 3 |
| Passaram o dedupe por ID de requisição | 3 |
| **Passaram o teste dos três tiros** | **3** |

**Fila final: 3 entradas.** Uma requisição viva confirmada, duas candidaturas espontâneas
com porta aberta.

---

## A FILA — as que destravaram

Ordenada por quanto encosta no centro do portfólio dele: personagem estilizado primeiro,
depois ambiente, depois generalista.

---

### 1. Rebel Wolves — Open Application, departamento **Art**

| Campo | Valor |
|---|---|
| Estúdio | Rebel Wolves Sp. z o.o. (fundadores de *The Witcher 3*, projeto *Dawnwalker*) |
| Cargo | Open Application — o candidato escolhe o departamento; **Art** está na lista |
| Cidade / País | Varsóvia, **Polônia** (Dereniowa 60/U4, 02-776 Warsaw) — UE, dentro do recorte |
| Formato | Presencial/híbrido em Varsóvia |
| Requisição | `WebID=d2fa13d6d9cd47a6aa9010c9e9294d74` (eRecruiter) |
| Faixa | Não publicada — o formulário PERGUNTA: "What are your net financial expectations?" |
| **URL COMPLETA de candidatura** | `https://system.erecruiter.pl/FormTemplates/RecruitmentForm.aspx?WebID=d2fa13d6d9cd47a6aa9010c9e9294d74` |

**Por que é a primeira:** é candidatura espontânea, então quem nomeia a disciplina é ele.
Marcando **Art** e escrevendo "Senior 3D Character Artist" no campo *Information for the recruiter*,
a porta aponta direto para o centro do portfólio — personagem estilizado — em vez de aceitar o
recorte que o anúncio impôs.

**O QUE MUDOU HOJE (o destrave).** A parede registrada em 06/09 e 07/09 não era captcha: o
formulário do eRecruiter **não tem captcha nenhum no HTML** (o painel já tinha medido isso: nada de
recaptcha, hcaptcha, turnstile ou datadome). O muro era o **POST do upload do CV para
`form.erecruiter.pl/form/<WebID>` voltando 403 do Cloudflare contra o nosso IP** — 403 puro, ou seja,
estado de rede. Hoje:

- `https://form.erecruiter.pl/` (raiz do host que dava 403) → **200**, 42.826 bytes.
- `https://form.erecruiter.pl/form/d2fa13d6d9cd47a6aa9010c9e9294d74` → **200**, 542.978 bytes.
- A página do formulário → **200**, 543.525 bytes, `<title>Application form - Open Application</title>`.

**RESSALVA HONESTA, e ela é a parte que importa:** eu medi o **GET** do endpoint que antes devolvia
403. Eu **não** medi o **POST**, porque medir o POST significaria enviar a candidatura, e isso está
fora do meu escopo. O que está provado é que o host e a rota saíram do 403 e servem o formulário
inteiro. Se o upload do CV ainda morrer, morre no POST, e aí é rodada nova.

**TRÊS TIROS — PASSOU.**

| Tiro | Resultado |
|---|---|
| Real, `Accept: */*` | **200** · 542.978 bytes |
| Real, cabeçalho de navegador | **200** · 543.525 bytes · título `Application form - Open Application` |
| **Controle** `WebID=00000000000000000000000000000000` (página do formulário) | **200** · 26.243 bytes · **sem título** |
| **Controle** `form.erecruiter.pl/form/00000000000000000000000000000000` | **307** → página `__next_error__`, 13.750 bytes |

O real serve 543 KB com título; o impossível serve 26 KB sem título, e no endpoint de upload devolve
307 para erro. **O teste discrimina. Mediu de verdade.**

**RÉGUA DE VINTE TERMOS sobre o texto integral** (2.732 caracteres): **1 casamento, e é falso positivo
catalogado.**

- `resident` → *"You may request us to give you an access to your personal data, their correction, deletion, limitation of processing, transfer to other administrator, as well as you have the right to object or file a complaint to the **Presid**ent of Personal Data Protection Office."* — **FALSO POSITIVO.** É "President" contendo `resident`, exatamente o caso catalogado.
- `authoriz` 0 · `eligib` 0 · `sponsor` 0 · `work permit` 0 · `must be based` 0 · `based in` 0 · `only from` 0 · `LMIA` 0 · `days a week` 0 · `days per week` 0 · `days in the office` 0 · `relocat` 0 · `located in` 0 · `unable to support` 0 · `no relocation` 0 · `x a week` 0 · `x per week` 0 · `within the` 0 · `only` 0 · idioma local exigido: **0** (o formulário é inteiro em inglês, não pede polonês).

**NENHUM VETO ESCRITO. Passa.**

**DEDUPE por ID de requisição** (`d2fa13d6d9cd47a6aa9010c9e9294d74`), as quatro contagens:

| Arquivo | Ocorrências |
|---|---|
| `docs/index.html` | 2 |
| `enviados.csv` | **0** |
| `automacao/processados.csv` | 1 |
| `automacao/FILA-DO-VINI.md` | 1 |

As três ocorrências fora do `enviados.csv` foram lidas uma a uma e **todas dizem NÃO ENVIADA**:
o registro de 07/09 no processados diz *"Formulario eRecruiter preenchido inteiro e conferido campo a
campo em modo seco, com CV anexado e visivel na tela. O envio…"* travou; o de 06/09 diz *"o POST para
form.erecruiter.pl/form/<WebID> volta 403 e o nome do arquivo nunca aparece na tela"*. **Zero em
`enviados.csv` é o que decide: nunca foi enviada. Dedupe PASSA.**

---

### 2. Volka — 3D Artist (time de marketing)

| Campo | Valor |
|---|---|
| Estúdio | Volka (*Taonga: the Island Farm*) |
| Cargo | 3D Artist |
| Cidade / País | Limassol, **Chipre** — UE, dentro do recorte |
| Formato | **FullTime, presencial** (`isRemote: false`, `workplaceType` presencial), efetiva |
| Requisição | `fa36e503-daf1-44d8-be2c-260cea2dd300` · publicada 19/08/2026 · `isListed: true` · sem prazo de encerramento |
| Faixa | Não publicada (`compensationTiers: []`) |
| **URL COMPLETA de candidatura** | `https://jobs.ashbyhq.com/volka/fa36e503-daf1-44d8-be2c-260cea2dd300/application` |

**Encaixe, dito com honestidade:** é **ambiente estilizado**, não personagem. O anúncio pede
"Full-cycle creation of **stylized low-poly environment assets** — landscapes, vegetation, buildings,
props and decorative objects", com high-poly e low-poly, retopologia, UV e texturas. É a disciplina
dele (modelagem + textura + estilizado), mas o recorte é ambiente, por isso fica atrás da Rebel Wolves
na ordem. Pede só 2 anos; ele tem 10+.

**O QUE ELA CARREGA E QUASE NADA CARREGA:** *"✈️ **Relocation Support:** Moving countries is stressful.
We handle the tickets, accounts and **permits** for you and your family. We provide temporary
accommodations while you're getting settled, cover the first rent of your own apartment and help with
necessary furnishings."* Mais *"Language Learning + **Naturalization Support**"*. A casa banca
passagem, contas, **autorizações** e primeiro aluguel — e mantém uma vaga aberta de *Immigration
Specialist*, o que mostra que realocam gente de fato. Isso ataca o gargalo número um da campanha.

**O QUE MUDOU HOJE.** O painel tinha esta entrada com dois diagnósticos brigando: 07/09 dizia "a NOSSA
REDE"; 08/09 corrigia para "NÃO é a nossa rede, o quadro renderizado devolve Page not found". **As duas
notas estavam erradas sobre a mesma coisa, e o controle de hoje mostra por quê.** Não é que o quadro
devolva "Page not found" para a vaga real: ele devolve **exatamente a mesma resposta para tudo**.

**TRÊS TIROS — a rota renderizada FALHOU, a rota de API PASSOU.**

Rota renderizada (`jobs.ashbyhq.com`) — **NÃO MEDIU NADA:**

| Tiro | Resultado |
|---|---|
| Vaga real | **200** · **7.270 bytes** · `<title>Jobs</title>` |
| Controle: uuid impossível `00000000-…-000000000000` | **200** · **7.270 bytes** · `<title>Jobs</title>` |
| Controle: inquilino impossível `zzzinquilinofalso` | **200** · **7.270 bytes** · `<title>Jobs</title>` |
| Rota de candidatura real `/application` | **200** · **7.270 bytes** |
| Controle: `/application` com uuid falso | **200** · **7.270 bytes** |
| Controle: `/application` com inquilino falso | **200** · **7.270 bytes** |

Seis respostas, **todas 200 com bytes idênticos**. É a repetição exata do que foi medido no HiBob em
09/09. Quem só olhasse esse quadro não poderia afirmar nem que a porta abriu nem que fechou.

Rota de API — **DISCRIMINA:**

| Tiro | Resultado |
|---|---|
| `api.ashbyhq.com/posting-api/job-board/volka` | **200** · 135.792 bytes · 11 vagas, entre elas `fa36e503… \| 3D Artist \| Cyprus, Limassol \| FullTime \| isListed: True` |
| **Controle** `…/job-board/zzzinquilinofalso` | **404** · 9 bytes · `Not Found` |
| GraphQL `ApiJobPosting`, uuid real | **200** · `{"jobPosting":{"id":"fa36e503-…","title":"3D Artist","locationName":"Cyprus, Limassol","employmentType":"FullTime","isListed":true,"applicationDeadline":null}}` |
| **Controle** GraphQL, uuid impossível | **200** · `{"data":{"jobPosting":null}}` |
| **Controle** GraphQL, inquilino impossível | **200** · `{"data":{"jobPosting":null}}` |

**A vaga existe, está listada e aceita candidatura** (`isListed: true`, `applicationDeadline: null`,
`applyUrl` servido pela própria API). **O teste mediu — pela API, não pelo quadro.**

**INSTRUÇÃO PRÁTICA que sai daí:** a URL de candidatura acima é a que a própria API devolve como
`applyUrl`. Mas como a página renderizada não se distingue de uma falsa por esta rede, **ele deve abrir
o link no navegador dele e confirmar que carrega o formulário com o título "3D Artist"** antes de
preencher. Se aparecer "Page not found", é a nossa rede de novo, não a vaga.

**RÉGUA DE VINTE TERMOS sobre o texto integral** (4.514 caracteres, `descriptionPlain` da API oficial):
**2 casamentos, os dois falsos positivos catalogados.**

- `relocat` → *"✈️ **Relocation Support**: Moving countries is stressful. We handle the tickets, accounts and permits for you and your family."* — **FALSO POSITIVO, e é frase A FAVOR:** a casa OFERECE a mudança. Exatamente o caso catalogado.
- `located in` → *"WHERE YOU'LL BE WORKING AT — **Located in** a historic three-story building in the heart of the city, our office offers a fresh, welcoming atmosphere."* — **FALSO POSITIVO:** é o endereço do escritório, caso catalogado.
- `authoriz` 0 · `eligib` 0 · `sponsor` 0 · `work permit` 0 · `must be based` 0 · `based in` 0 · `only from` 0 · `LMIA` 0 · `days a week` 0 · `days per week` 0 · `days in the office` 0 · `resident` 0 · `unable to support` 0 · `no relocation` 0 · `x a week` 0 · `x per week` 0 · `within the` 0 · `only` 0 · idioma local exigido: **0** (grego aparece só como aula PAGA pela empresa, benefício, não requisito).

**NENHUM VETO ESCRITO. Passa.**

**DEDUPE por ID de requisição** (`fa36e503`), as quatro contagens:

| Arquivo | Ocorrências |
|---|---|
| `docs/index.html` | 1 |
| `enviados.csv` | **0** |
| `automacao/processados.csv` | 1 |
| `automacao/FILA-DO-VINI.md` | 0 |

As duas ocorrências foram lidas: a de 07/09 é `vaga-a-mao` com o texto *"NAO ENVIADA, e o motivo e a
NOSSA REDE"*; a de 08/09 é `alvo-descartado` pelo mesmo motivo de acesso. **Zero em `enviados.csv`.
Nunca foi enviada. Dedupe PASSA.** Não está na lista de não-repetir de 09/09.

---

### 3. Crater Studio — Work with Us (Artists)

| Campo | Valor |
|---|---|
| Estúdio | Crater Studio (VFX para cinema, TV e publicidade) |
| Cargo | Convite aberto a **Artists** — "register your interest" |
| Cidade / País | Belgrado, **Sérvia** — Europa, dentro do recorte |
| Formato | Presencial em Belgrado |
| Requisição | Nenhuma — é convite aberto, não requisição numerada |
| Faixa | Não publicada |
| **URL COMPLETA de candidatura** | `https://craterstudio.com/jobs` · e-mail de contato do estúdio: `effects@craterstudio.com` · telefone `+381 11 2620 440` |

**Entra por último e com ressalva grande.** É generalista, é convite e não vaga, e o próprio texto
diz: *"Please apply via job **application form** - register your interest. You'll hear from us for
instructions on how to send your CV and reel."* **Eu não achei esse formulário.** O HTML servido tem
exatamente um link interno de vagas (`href="/jobs"`, que é a própria página) e nenhum link para
formulário; o formulário é montado por JavaScript (a página é Next.js) e não aparece por `curl`.
Então a porta **abriu**, mas o **botão dela não foi localizado por esta rede**. Para o Vini isso é
trivial — abre no navegador dele e o formulário aparece.

**O QUE MUDOU:** já estava resolvido em 07/09 e hoje segue de pé. O 403 é só na **raiz**
(`craterstudio.com` → 403, página própria de 5,5 KB); o **caminho** `/jobs` responde 200. É a lição do
`bugbeargames.com` de novo: caminho diferente muda o veredito, e o 403 da raiz nunca autorizou escrever
casa morta.

**TRÊS TIROS — PASSOU.**

| Tiro | Resultado |
|---|---|
| Real `/jobs`, `Accept: */*` | **200** · 72.978 bytes · `<title>Jobs at Crater</title>` |
| Real `/jobs`, cabeçalho de navegador | **200** · 72.978 bytes · mesmo título |
| **Controle** `craterstudio.com/zzz-nao-existe` | **404** · 7.639 bytes · sem título |

Real 73 KB com título, impossível 404 de 7,6 KB. **Discrimina. Mediu.**

**RÉGUA DE VINTE TERMOS sobre o texto integral** (683 caracteres, a página é curta):
**ZERO casamentos nos vinte termos.** `authoriz` 0 · `eligib` 0 · `sponsor` 0 · `work permit` 0 ·
`must be based` 0 · `based in` 0 · `only from` 0 · `LMIA` 0 · `days a week` 0 · `days per week` 0 ·
`days in the office` 0 · `resident` 0 · `relocat` 0 · `located in` 0 · `unable to support` 0 ·
`no relocation` 0 · `x a week` 0 · `x per week` 0 · `within the` 0 · `only` 0 · idioma local (sérvio)
exigido: **0** (a página é inteira em inglês).

**NENHUM VETO ESCRITO. Passa** — com a ressalva de que a página é curta e o veto, se existir, pode
estar no formulário que não consegui abrir.

**DEDUPE** (`craterstudio`), as quatro contagens:

| Arquivo | Ocorrências |
|---|---|
| `docs/index.html` | 2 |
| `enviados.csv` | **0** |
| `automacao/processados.csv` | 1 |
| `automacao/FILA-DO-VINI.md` | 0 |

**Zero em `enviados.csv`. Dedupe PASSA.**

---

## AS QUE VOLTARAM A RESPONDER MAS NÃO VIRARAM FILA

Estas seis destravaram de verdade — o bloqueio caiu — e mesmo assim não geram candidatura. O motivo de
cada uma está escrito para a próxima rodada não gastar o tempo de novo.

| Casa | O que caiu | O que se achou atrás | Veredito |
|---|---|---|---|
| **VSTEP** (Roterdã, Holanda) | O `ECONNRESET` caiu (parcialmente — ver armadilha 6). E o caminho registrado estava **errado**: `/careers/` dá 404; o real é `/our-company/careers-at-vstep/`, achado pelo `page-sitemap.xml` | Página aberta, `<title>Careers - VSTEP B.V.</title>`, 303.474 bytes | **"Vacancies — Careers at VSTEP: There are currently no positions available."** Casa sem vaga, não parede. Corrigir a URL no painel. |
| **Smoking Gun Interactive / Keywords** (Vancouver) | O `1015` do Workable caiu: `apply.workable.com/api/v1/widget/accounts/580933` → **200** | Quadro lido inteiro | **UMA vaga só: `61BD09F275` Senior/Principal UX Designer.** Zero da disciplina. Mandar UX queima a porta. |
| **VOID Interactive** (Irlanda/remoto) | O 403 do Cloudflare cai com cabeçalho de navegador: `Accept: */*` → **403**; `Accept: text/html` + UA de Chrome → **200**, 47.508 bytes, `<title>Careers – VOID Interactive</title>`. Controle `/zzz-nao-existe/` → 404 "Page not found". **Discrimina.** | Duas vagas: Senior Software Engineer (Unreal) e Brand Manager, as duas *Global, Fully Remote* | Zero da disciplina. **Manter de olho:** a casa é 100% remota e as vagas são globais, então quando abrir arte vale muito. |
| **Keywords Studios** (Senior/Lead Character Artist, Remote EMEA) | O `1015` caiu — mas a resposta nova é pior que bloqueio | `apply.workable.com/api/v1/widget/accounts/keywords-intl1` → **404 `Not Found`**. O token da conta não existe mais. E `…/keywords-intl1/j/D2A45246FA/` devolve **200 com 5.591 bytes idênticos aos do shortcode impossível `ZZZZZZZZZZ`** (título `Keywords Studios - Current Openings`) — ou seja, é o quadro de fallback, não a vaga | **A requisição `D2A45246FA` não resolve mais.** Não é bloqueio: é vaga que saiu do ar ou token trocado. Fechar como não-confirmável e procurar a Keywords pela outra porta já registrada (`careers.smartrecruiters.com/KeywordsStudios`). |
| **Bohemia Interactive** (Praga, Chequia) | O 502 intermitente caiu: `Accept: */*` → **500**; cabeçalho de navegador → **200**, 184.881 bytes, `<title>Application Form \| Bohemia Interactive Careers</title>`. Controle `/en/zzz-nao-existe` → **404**. **Discrimina** | **E o destrave revelou a parede de verdade:** a rota `/apply` carrega `"recaptchaSiteKey":"6LeMdV8tAAAAAHTyvqsOWq_dWnMjOng9FlTYx0L8"` | **RECLASSIFICADA: não é bloqueio de rede, é reCAPTCHA — parede do estúdio.** Sai desta caça e vai para a fila de "à mão". Além disso, as vagas de `character` do quadro são todas de **animação/rigging/tech-anim**, não de modelagem. |
| **GIANTSTEP** (Seul, Coreia do Sul) | O host responde: `giantstepcorp.recruiter.co.kr/career/recruit` → **200**, 20.858 bytes, `<title>채용공고 \| GIANTSTEP 채용</title>`. Controle `/career/zzz-nao-existe` → **404 페이지를 찾을 수 없습니다**. **Discrimina** | Nada — a lista de vagas é montada por JavaScript e não há `__NEXT_DATA__` no HTML. Cinco rotas de API foram tentadas (`/api/career/recruit`, `/api/recruit/list`, `/appApi/…`, `api.recruiter.co.kr/…`, `/career/recruit/list`) e **todas devolveram 404** | **Porta viva, conteúdo ilegível por `curl`.** Coreia do Sul está no recorte. Fica para o navegador do Vini ou para uma rodada com navegador de tela. Não escrever "sem vaga" aqui. |

---

## AS QUE CONTINUAM BLOQUEADAS — código e mensagem exatos de hoje

Para a próxima rodada saber que ainda não caiu. Medido em 09/09 entre 04h38 e 04h50 UTC.

### Bloqueio de TLS / handshake do nosso lado (`000`, sem resposta)

| Casa | País | Mensagem literal de hoje |
|---|---|---|
| **Gamecan** | Estônia (Pärnu) | `curl: (60) SSL: no alternative certificate subject name matches target host name 'careers.gamecan.eu'` — é o cert genérico da **Fastly**, mesma assinatura do caso Game Boost, mas aqui a config quebrada é do lado **deles** |
| **Digital Domain** | EUA/Canadá | `curl: (35) Recv failure: Connection reset by peer` |
| **Atomic Arts** | Reino Unido | `curl: (35) OpenSSL/3.0.13: error:0A000438:SSL routines::tlsv1 alert internal error` |
| **Glassworks** | Reino Unido | `curl: (35) Recv failure: Connection reset by peer` |
| **Potion Pictures** | Reino Unido | `curl: (35) OpenSSL/3.0.13: error:0A000438:SSL routines::tlsv1 alert internal error` |
| **CherryCherry VFX** | Reino Unido | `curl: (35) Recv failure: Connection reset by peer` |
| **Filament Post** | Reino Unido | `curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to filamentpost.co.uk:443` |
| **roll7** | Reino Unido | `curl: (35) OpenSSL/3.0.13: error:0A000438:SSL routines::tlsv1 alert internal error` |
| **Super Punk Games** | Reino Unido | `curl: (35) Recv failure: Connection reset by peer` |
| **Digital Leisure** | Canadá | `curl: (35) OpenSSL/3.0.13: error:0A00010B:SSL routines::wrong version number` |

Dez casas, o mesmo diagnóstico de 07/09 **inalterado**: é a nossa perna de saída, não os estúdios.
Todas continuam válidas para o navegador do Vini.

### Bloqueio de bot / limite de taxa (respondem, mas com parede)

| Casa | Código de hoje | Mensagem / evidência |
|---|---|---|
| **Epic Games** — Principal Environment Artist `6121292004` | **403** · 25.354 bytes (plain) / 25.652 (navegador) | Muro de bot do `job-boards.greenhouse.io` contra o nosso IP de datacenter. **O controle `jobs/9999999999` também dá 403 com 25.209 bytes** — ver armadilha 4 |
| **Epic Games** — Senior Environment Artist `6001731004` | **403** · bytes idênticos aos da irmã | Mesma parede. Regra da campanha: mandar na Principal primeiro |
| **BeamNG** — Unsolicited application | **429** · 17 bytes · `error code: 1015` | O `1015` do Cloudflare no `apply.workable.com/j/4BAB98907E` **não caiu**. O token de conta `beamng` devolve 404, então o token guardado também está errado |
| **Running With Scissors** | **403** · 5.783 bytes · `<title>Attention Required! \| Cloudflare</title>` | Desafio do Cloudflare, idêntico plain e com navegador |
| **Payload Studios** | **202** · 179 bytes | Redirecionamento anti-robô. **O controle também dá 202/186 bytes** — ver armadilha 3 |
| **Nice Shoes** | **202** · 179 bytes | Robot Challenge do Akamai. Controle idêntico |
| **Lipsync Post** | **202** · 179 bytes | Akamai. Controle idêntico |

### Inconclusivas — responderam 200 e o teste NÃO MEDIU NADA

| Casa | Código | Por que não vale |
|---|---|---|
| **Red Manta / Twin Atlas** — Environment Artist (Las Vegas ou remoto) | 200 · 20.036 bytes | `notion.site`: real e impossível são indistinguíveis — ver armadilha 1. **Vaga da disciplina, alta prioridade para o navegador dele** |
| **Pixelsplit** — Join Pixelsplit | 200 · 20.035 bytes | Mesma armadilha |
| **Marshmallow Laser Feast** — Jobs Board | 200 · 20.033 bytes | Mesma armadilha |

As três **não podem** ser escritas como destravadas nem como bloqueadas. O `curl` não alcança conteúdo
de página do Notion, ponto. Só navegador resolve.

---

## AS ARMADILHAS DE MÉTODO QUE EU MEDI

Estas dez foram medidas nesta rodada, com o número na mão. São o produto mais durável do relatório.

**1. `notion.site` devolve 200 para qualquer coisa, e o 200 não significa nada.**
`twinatlas.notion.site/environment-artist` → 200, 20.034 bytes, `<title>Notion</title>`.
`twinatlas.notion.site/zzz-nao-existe-999…` → 200, 19.972 bytes, `<title>Notion</title>`.
Os dois trazem o **mesmo** `og:title` ("Notion | Where teams and agents work together") e a **mesma**
meta description genérica da Notion. Contagem de "environment artist" no HTML: **0 no real e 0 no
falso**. Repetido nos três hosts (Twin Atlas, Pixelsplit, Marshmallow Laser Feast) com o mesmo
resultado. **Qualquer varredura que conte `notion.site` como "200 = porta aberta" está contando
fantasma.**

**2. Ashby renderizado é o caso HiBob de novo, com um agravante.** No HiBob, vaga real, uuid falso e
inquilino falso deram três 200 idênticos. No Ashby deu **seis**: página da vaga real, uuid impossível,
inquilino impossível, e as três rotas `/application` correspondentes — **todas 200 com exatamente 7.270
bytes** e `<title>Jobs</title>`. O que salva é que **existem duas rotas honestas**:
`api.ashbyhq.com/posting-api/job-board/<inquilino>` devolve **404** para inquilino falso, e o GraphQL
`ApiJobPosting` devolve **`{"jobPosting":null}`** para uuid ou inquilino falso. **Em Ashby, nunca meça
pelo quadro; meça pela API.** Isso também desfaz a nota de 08/09 que dizia que a Volka devolvia "Page
not found" — ela devolve a mesma coisa que devolve para tudo.

**3. O `202` de 179 bytes é anti-robô, e ele engole o controle junto.** Payload Studios, Nice Shoes e
Lipsync Post devolvem 202 com 179 bytes na URL real **e 202 com 186 bytes na URL impossível**. Sete
bytes de diferença, que é só o tamanho do caminho ecoado. O `202` do SiteGround/Akamai responde antes
de o site ver o pedido, então ele não sabe nem pode dizer se a página existe. **Um 202 desses não é
porta aberta nem porta fechada: é ausência de medição.**

**4. Um 403 no controle é informação, e é boa.** Na Epic, a vaga real e a vaga impossível
`jobs/9999999999` devolvem **as duas 403** com tamanhos quase iguais (25.354 vs 25.209). Isso confirma
que o 403 é o muro do quadro e não o veredito da requisição — ou seja, **continua proibido escrever
"vaga morta" ali**, exatamente como a regra manda. O controle não abriu a porta, mas provou que a porta
fechada não fala sobre a vaga.

**5. O quadro do Workable devolve 200 para shortcode que não existe.**
`apply.workable.com/keywords-intl1/j/D2A45246FA/` → 200, **5.591 bytes**.
`apply.workable.com/keywords-intl1/j/ZZZZZZZZZZ/` → 200, **5.591 bytes**, título `Keywords Studios -
Current Openings`. Shortcode morto **redireciona para o quadro** em vez de dar 404. **Um 200 numa URL
`/j/<shortcode>/` do Workable não prova que a requisição existe** — tem que bater na API do widget, que
para `keywords-intl1` devolve **404**, ou seja o token da conta também está errado.

**6. O tiro de controle pode PASSAR enquanto o real FALHA — e aí ele mente ao contrário.** Na VSTEP,
`/our-company/zzz-nao-existe/` devolveu **404 com 256.910 bytes** (site claramente de pé) enquanto
`/our-company/careers-at-vstep/` **resetava a conexão em 3 de 4 tentativas**. Quem medisse só o
controle escreveria "site saudável"; quem medisse só o real escreveria "site bloqueado". **Os dois
tiros têm que ser lidos juntos, e a instabilidade tem que ser medida com repetição, não com uma
tentativa.** Na quarta rodada de tentativas o real estabilizou em 500 com 303.474 bytes e título
`Careers - VSTEP B.V.` — que é o conteúdo de verdade servido com status de erro.

**7. Caminho errado no painel vira "bloqueio" no relatório.** A VSTEP estava registrada em
`/careers/`, que dá **404**. A página real é `/our-company/careers-at-vstep/`, achada em trinta
segundos pelo `page-sitemap.xml`. É a terceira vez que a campanha registra isso (bugbeargames sem barra
final, raynault.com/en/careers, crater na raiz vs `/jobs`). **Antes de escrever bloqueio, ler o
sitemap.**

**8. O cabeçalho muda o veredito, e muda nos dois sentidos.** VOID Interactive: **403** com
`Accept: */*`, **200** com `Accept: text/html` + UA de Chrome. Bohemia: **500** plain, **200** navegador.
E o contrário também acontece: Keywords deu **200** plain e **429** com cabeçalho de navegador; a conta
`580933` da Smoking Gun deu **429** plain e **200** navegador. **Não existe "o" cabeçalho certo; existe
testar os dois, que é por isso que os dois estão no protocolo.**

**9. O `1015` do Workable oscila dentro do mesmo minuto.** `580933` devolveu **429/1015** às 04h41 e
**200** às 04h42. `keywords-intl1` devolveu **429/1015** e depois **404**. `apply.workable.com/j/4BAB98907E`
(BeamNG) devolveu **429** nas duas tentativas. **Uma leitura só do Workable não é medição** — e um
"1015" registrado ontem não autoriza nenhuma conclusão hoje.

**10. Derrubar o bloqueio de rede pode só revelar a parede do estúdio embaixo.** A Bohemia estava
fechada por 502. Com a rede consertada, a rota `/apply` mostra
`"recaptchaSiteKey":"6LeMdV8tAAAAAHTyvqsOWq_dWnMjOng9FlTYx0L8"`. **"O bloqueio caiu" e "a porta abriu"
não são a mesma frase**, e a entrada tem que ser reclassificada de rede para captcha em vez de ser
promovida para a fila. Foi o único caso desta rodada, mas é o erro mais caro possível: mandaria o Vini
gastar tempo numa porta que não abre para ninguém automatizado.

---

## O QUE ESTA RODADA NÃO FEZ

- Não enviou candidatura, não preencheu formulário, não fez `commit` nem `push`.
- Não tocou em `docs/index.html`, `enviados.csv`, `automacao/processados.csv` nem
  `automacao/FILA-DO-VINI.md` — só leu.
- Não testou nenhum **POST** de candidatura, porque testar o POST é enviar. Onde a parede antiga era um
  POST (Rebel Wolves), o que está provado é o GET da mesma rota.
- Não abriu navegador. Tudo é `curl`. As três entradas inconclusivas do Notion e a listagem da
  GIANTSTEP são justamente o que só navegador resolve.
