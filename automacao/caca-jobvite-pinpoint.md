# Caça Jobvite + Pinpoint — 09/09/2026, madrugada

## Placar de cima

| Etapa | Jobvite | Pinpoint |
|---|---|---|
| Slugs testados | **4.375** | **4.428** |
| Quadros que responderam 200 | 10 | 28 |
| Quadros VIVOS de verdade (200 + conteúdo real) | **8** | **8** |
| Vagas da disciplina achadas | **12** | **2** |
| Sobreviveram ao escopo geográfico | 5 | 2 |
| Sobreviveram à régua de dezessete termos | 4 | 2 |
| **Sobreviveram ao dedupe por ID de requisição** | **1** | **0** |

Somando as duas famílias: **2 linhas prontas para clicar** (uma Jobvite, uma Pinpoint —
a de Pinpoint é candidatura espontânea, não vaga nomeada). A fila é curta porque foi
medida, não porque foi pouco procurada: 8.803 slugs testados por `curl`, sem navegador.

**O achado que vale mais que a fila:** encontrei a rota de formulário do Pinpoint, que é o
equivalente do `/apply` do Jobvite, e ela **destrava as duas vagas da TTK Games que estão
na fila desde 08/09 e nunca foram enviadas** porque o POST do site do estúdio devolveu 500
`ReCaptcha Failed`. Está no bloco B, logo abaixo da fila.

---

# A. FILA PRONTA PARA CLICAR

### A1 — DNEG · Lead LookDev TD (DNEG VFX) · Londres, Reino Unido · JOBVITE

- **Estúdio:** DNEG (Double Negative Visual Effects)
- **Cargo:** Lead LookDev TD (DNEG VFX) — *Expression of interest*
- **País/cidade:** Reino Unido, Londres (presencial; o quadro não marca hybrid nesta vaga)
- **URL DE CANDIDATURA (com `/apply`, como você pediu):**
  `https://jobs.jobvite.com/double-negative-visual-effects/job/oLCvzfwb/apply`
- **ID da requisição:** `oLCvzfwb`
- **Formato:** efetivo, presencial em Londres, departamento *Build*
- **Faixa:** **não publicada** (busca por `salary`, `£`, `GBP`, `compensation`, `per annum`
  no texto integral: zero ocorrência)
- **Régua de dezessete termos, resultado literal:** `(nenhum dos 17 termos casou)`.
  Rodei sobre o texto integral baixado da página da vaga (3.975 caracteres), não sobre o resumo.
- **Dedupe (obrigatório, feito por ID):** `grep oLCvzfwb` em `docs/index.html`,
  `enviados.csv`, `automacao/processados.csv` e `automacao/FILA-DO-VINI.md` →
  **0 / 0 / 0 / 0. LIMPO.**
- **Medição do formulário:** a página `/job/oLCvzfwb` tem **2 campos** e nenhum deles é do
  formulário (`twitter:card`, `viewport`). A página `/job/oLCvzfwb/apply` responde 200 com
  85.204 bytes e traz `jv-apply`, `name="consentForm"`, `name="policyIds"`. **A armadilha que
  você mediu ontem se confirma nesta vaga: o link sem `/apply` não serve.**
- **RESSALVA QUE VOCÊ PRECISA LER ANTES DE CLICAR, e ela é do próprio anúncio:** o texto
  abre com *"\* This role is currently not open. Please apply knowing that it is to make us
  aware of your interest, should future roles open up - thank you!!!\*"*. Ou seja: o
  formulário está vivo e aceita candidatura, mas é **banco de talentos**, não requisição
  aberta. Coloquei na fila porque é a única linha Jobvite genuinamente nova e ela passa em
  disciplina, escopo, régua e dedupe — mas o valor por clique é menor que o de uma vaga aberta.
  Decida com esse número na mão.

### A2 — Maverick Games · Speculative Applications · Warwick, Reino Unido · PINPOINT

- **Estúdio:** Maverick Games (Warwick, Inglaterra)
- **Cargo:** Speculative Applications (candidatura espontânea — **não é vaga nomeada**)
- **País/cidade:** Reino Unido, Warwick
- **URL DE CANDIDATURA (rota de formulário do Pinpoint — ver bloco C):**
  `https://maverick-games.pinpointhq.com/en/postings/2cfec945-308c-4ab1-aace-a2398c2daf87/applications/new`
- **ID da requisição:** `76058` (uuid `2cfec945-308c-4ab1-aace-a2398c2daf87`)
- **Formato:** `full_time` + `hybrid`, conforme os campos estruturados do quadro
- **Faixa:** `compensation_visible: false` — **não publicada**
- **Régua de dezessete termos, resultado literal:** `(nenhum dos 17 termos casou)`, rodada
  sobre título + descrição + responsabilidades + requisitos + benefícios + tipo de contrato
  + tipo de local, concatenados do `postings.json`.
- **Dedupe (por ID):** `grep 76058`, `grep 2cfec945` e `grep -i maverick` em
  `docs/index.html`, `enviados.csv`, `automacao/processados.csv`, `automacao/FILA-DO-VINI.md`
  → **0 em todos os quatro arquivos, nas três buscas. LIMPO.**
- **Medição do formulário:** 200, 88.828 bytes, `<title>New Application | Speculative
  Applications | Maverick Games Careers`, com os campos reais
  `application_form[application][first_name]`, `[last_name]`, `[email]`, `[summary]`, `[uuid]`.
- **Texto integral do anúncio, na íntegra (é curto):** *"We are a developer-first video game
  studio, an environment where talented individuals are nurtured, inspired and flourish. If
  you don't see a role that is fitting for your skills and experience on our website, we are
  welcome to receive Speculative Applications to keep your information on file, we will
  endeavour to reach out should a suitable role become available in the future."*
- **RESSALVA:** é porta espontânea, não requisição. Estúdio britânico real, fundado por gente
  que saiu da Playground Games, quadro Pinpoint vivo com essa única entrada. Entrego rotulado
  para você decidir; não vou fingir que é vaga de personagem.

---

# B. PORTA NOVA PARA DUAS VAGAS QUE JÁ ESTÃO NA FILA E NUNCA FORAM ENVIADAS

Isto **não** é alvo novo e o dedupe **acusou duplicata** — estou entregando porque o que
mudou não é a vaga, é a porta.

O painel registra que em 08/09 você preencheu a **TTK Games · Character Artist** inteira e o
POST para `ttkgames.com/api/pinpoint/apply` devolveu **500 com corpo `ReCaptcha Failed`**, e
que **nada foi enviado**. Confirmei por `grep` que nenhuma das duas vagas da TTK aparece em
`enviados.csv`: elas estão na fila, **não estão enviadas**.

Medi hoje que o Pinpoint serve um formulário **nativo**, em host próprio, que **não é** a
rota do site do estúdio e **não passa** pelo `/api/pinpoint/apply` que quebrou:

| Vaga | ID no `postings.json` | ID na rota do site (já na fila) | Porta nativa do Pinpoint |
|---|---|---|---|
| Character Artist | `558871` | `561860` | `https://ttkgames.pinpointhq.com/en/postings/88f9f885-d2a6-4815-953d-2866d92fe370/applications/new` |
| Lead Environment Artist | `559201` | `562172` | `https://ttkgames.pinpointhq.com/en/postings/c29471f7-46df-49ee-8d62-f7646b2acf9a/applications/new` |

**Medido:** as duas rotas respondem **200**, ~89,5 KB, **sem redirecionar**, e trazem os
campos reais `application_form[application][first_name]`, `[last_name]`, `[email]`,
`[summary]`, `[uuid]`, mais `Shared::Form::Filefield` (anexo) e `application_form[linkedin_url]`.
O `<title>` da primeira é literalmente `New Application | Character Artist | TTK Games AB Careers`.

**Medido também, e leia o limite:** procurei `recaptcha`, `hcaptcha`, `turnstile` e
`cf-challenge` no HTML servido dessas duas páginas e **não achei nenhum**; o `<form>` posta
para `/en/postings/<uuid>/applications`, endpoint do próprio Pinpoint. **Isso é ausência no
HTML servido, não é prova de que o envio passa** — captcha pode ser injetado por JS na hora
do submit. Mas é uma porta diferente da que reprovou, e custa um clique testar.

Régua nas duas, sobre o texto integral do `postings.json` (descrição + responsabilidades +
requisitos + benefícios + local): **`(nenhum dos 17 termos casou)`** nas duas.
Faixas publicadas no corpo do anúncio: Character Artist *"Starting from 34,000 SEK per month,
rising to 47,000 with experience, plus bi-annual bonus"*; Lead Environment Artist
*"Starting from 60,000 SEK per month, rising to 85,000 with experience, plus bi-annual bonus"*.
Ambas Estocolmo, Suécia, `permanent` + `hybrid`.

---

# C. AS DUAS ARMADILHAS DE ROTA, MEDIDAS HOJE

**JOBVITE — sua armadilha se confirma, e eu a reproduzi.** Em `job/ovLGAfwg` a página da vaga
tem 2 campos, nenhum de formulário; `job/ovLGAfwg/apply` tem `jv-apply` + `consentForm` +
`policyIds`. Todo link Jobvite nesta entrega termina em `/apply`.

**PINPOINT — achei o `/apply` equivalente, e ele resolve o problema dos dois espaços de ID.**
Você me avisou que o quadro cru e a rota do site não se conversam. Medi os dois lados:

- `https://<empresa>.pinpointhq.com/postings/<uuid>` e `/jobs/<id-numérico>` → **302 para a
  home do quadro, ou redirect JS para o site do estúdio**. Reproduzido em `gameplaygalaxy`
  (302 `location: https://gameplaygalaxy.pinpointhq.com/`), `tripledotstudios` e
  `buildarocketboy` (caem na home), e `ttkgames` (vai parar em `ttkgames.com/careers/`).
  **Esses links parecem vaga morta mesmo quando a vaga está viva.**
- `https://<empresa>.pinpointhq.com/en/postings/<uuid>/applications/new` → **200, não
  redireciona, e renderiza o formulário com os campos reais.** Confirmado em `ttkgames` (duas
  vezes) e `maverick-games`.

**Regra prática que eu deixo escrita: no Pinpoint, o link que se dá para clicar é
`/en/postings/<uuid>/applications/new`. Ele contorna os dois espaços de identificador, porque
o uuid do `postings.json` funciona nessa rota mesmo quando o site do estúdio usa outro id.**

Sobre a `ttk-strapi-tnje3.ondigitalocean.app` que você citou: `/api/pinpoint/jobs` e
`/api/pinpoint/job/<id>` respondem **403 Forbidden** ao `curl` (testei com os ids `558871`,
`559201` e com o uuid). Precisa de credencial que só o site carrega — **`precisa-de-navegador`**
se você quiser ler por ali. Mas não precisa: a rota `/applications/new` do Pinpoint dá o
formulário sem isso.

---

# D. ARMADILHA NOVA, E ELA CUSTARIA UMA FILA INTEIRA DE MENTIRA

**O Pinpoint entrega dados de DEMONSTRAÇÃO em quadros não configurados, com HTTP 200.**
A assinatura é sempre a mesma trinca (às vezes com variações de "Head of DEI"):

> `Head of DEI - UK | London` · `Marketing Manager | Paris` · `Customer Service Rep | New York`

Se eu tivesse contado esses como quadros vivos, teria te entregado **10 estúdios "achados"**
que não têm vaga nenhuma. Os dez que caíram nessa: `frontierdevelopments`, `kwalee`,
`framestore`, `realtimeuk`, `tensquaregames`, `moonbug`, `hornet`, `metaphysic`, `pushgaming`,
`reply`. **Framestore e RealtimeUK são estúdios de verdade com quadro Pinpoint reservado e
vazio — não são porta.**

**Armadilha irmã no Jobvite:** `important-looking-pirates` responde **HTTP 200** com corpo
`"Oops, we must have moved it. 404 Error"`. Código 200 não é quadro vivo; tem que ler o corpo.

**Terceira, e é a que mais dói:** `postings.json` **vazio (`{"data":[]}`) não quer dizer
quadro morto por si só** — mas quando eu conferi as vagas que o buscador indexava nesses
quadros vazios (`gameplaygalaxy/jobs/128688`, `tripledotstudios` uuid, `buildarocketboy` uuid),
**todas redirecionavam para a home, ou seja, tinham fechado**. Nos casos que testei,
`postings.json` vazio = sem vaga aberta agora, e o resultado do buscador era índice velho.

**Nada de instrução escondida:** varri o HTML dos quadros que abri e **não encontrei** hoje
nenhuma injeção em Unicode invisível como a que você pegou ontem. Registro isso como
medição, não como garantia — só olhei os quadros que abri.

---

# E. O QUE ESTÁ VIVO, PARA A PRÓXIMA RODADA NÃO REFAZER ESTE TRABALHO

**JOBVITE — 8 quadros vivos com conteúdo, de 4.375 slugs.** Sinal limpo: slug inválido
redireciona para `search.jobvite.com` e volta **403**; 204 de 208 no primeiro lote foram 403.

| Slug | Vagas | Serve para o Vini? |
|---|---|---|
| `double-negative-visual-effects` | 100 | **Sim** — é a única fonte Jobvite da disciplina. Detalhe em E1. |
| `amberstudiocareers` | 60 | Não — as 4 vagas 3D são Brasil (×2) e Manila (×2). Fora de escopo. |
| `playground-games` | 9 | Não — só Design, Engineering, Production. As Character Artist que o buscador ainda indexa (`ozfzufwB`, `obXAnfwP`) **estão 404**. |
| `probablymonsters` | 4 | Não — a única "Artist" é *Cinematic Media Artist*, departamento **Marketing**, captura de gameplay em UE5. Fora de disciplina. |
| `brahma` | 22 | Não — unidade de IA da DNEG, tudo engenharia. |
| `funko` | 29 | Não — as vagas de arte são *Graphic Design*, *Packaging*, *Concept Design* (2D) e *Art Director* da Loungefly (moda). |
| `capcomusa` | 2 | Não — Financial Analyst e Marketing. |
| `ainsworth` | 104 | Não — é a Ainsworth de HVAC/elétrica no Canadá, homônima. Nada de jogos. |
| `kwalee` | 0 | Quadro vivo mas vazio: *"There are currently no open jobs."* Vale reabrir depois. |

### E1 — DNEG, esgotada, e o dedupe provou

Enumerei **100 ids** da DNEG cruzando `/jobs`, `/search`, `/jobs/positions` e
`/search?q=model`, porque **a página do quadro não lista tudo**: o `Model TD` (`oGKA5fwP`) que
um buscador indexa não aparece em nenhuma listagem — e quando fui buscar, **caiu na listagem,
ou seja, já tinha fechado**.

Das 100, as da disciplina e o que aconteceu com cada uma:

| ID | Cargo | Local | Veredito |
|---|---|---|---|
| `oLCvzfwb` | Lead LookDev TD | Londres | **→ FILA A1** |
| `oF9Yyfw4` | Facial Modeller | Londres | régua limpa, mas **DUPLICATA** (5 ocorrências, inclusive `enviados.csv`) |
| `oQKJAfwD` | Groom TD | Londres, híbrido | régua limpa, mas **DUPLICATA** (3 ocorrências) |
| `ooyGAfwW` | Modeleur de personnages / Character Modeler | Montréal, híbrido | régua limpa, sindicalizada IATSE, mas **DUPLICATA** (4 ocorrências) |
| `ovLGAfwg` | Character Modeller for VFX style Creatures | Londres | **VETO DE VERDADE** + duplicata |
| `oLwkzfwU` | Character Modeler (Animation) | Mumbai / Chennai / Bengaluru | **fora de escopo (Índia)** |
| `orV15fwc` | Creature TD | Mumbai / Bengaluru | **fora de escopo (Índia)** |
| `oWKA5fw5` | Creature TD - CFX | Mumbai | **fora de escopo (Índia)** |
| `oktKzfwQ` | Gen AI Model Artist | Londres | **fora de disciplina** — treinar e afinar modelos generativos, curadoria de dataset |
| `oiGMzfw3` | Model AI Artist (VFX) | Londres | **fora de disciplina** — mesma coisa, ML |

**O veto literal da `ovLGAfwg`, colado inteiro:**

> *"\*\*\*\*\*\*\*\*Candidates must be local to London to come in the office 3x a week and must
> be eligible to work in the UK without visa sponsorship\*\*\*\*\*\*\*\*"*

Casou em `eligib` e em `sponsor`. **Repare que `days a week` NÃO pegou**, porque o anúncio
escreve **"3x a week"**, não "3 days a week". A régua salvou pelos outros dois termos, mas
fica o aviso: vale acrescentar `x a week` e `x per week` à lista de dezessete.

### E2 — Falsos positivos que a régua produziu hoje, para você não descartar por engano

Da ProbablyMonsters *Cinematic Media Artist* (que já está fora por disciplina, mas serve de
exemplo limpo):

- `eligib` → *"Eligibility to participate in these benefits may vary for part-time and
  temporary full-time employees…"* — **falso positivo, é benefício.**
- `eligib` → *"This is a full-time, benefits-eligible, exempt (salaried) position."* —
  **falso positivo, é categoria de contrato.**
- `eligib` → *"In addition to base pay, employees in this role may be eligible for additional
  incentives…"* — **falso positivo, é remuneração.**
- `located in` → *"This role is an onsite role located in Fort Worth, TX."* — **falso
  positivo do tipo que você já tinha catalogado: diz ONDE o cargo fica, não quem pode se
  candidatar.**

**Nenhuma frase A FAVOR** apareceu em nada que eu abri hoje. Procurei especificamente:
`relocat` não casou em nenhuma das vagas que chegaram até a régua.

**PINPOINT — 8 quadros com vaga real, de 4.428 slugs.** Sinal: slug inexistente é **404** limpo
(151 de 157 no primeiro lote).

| Slug | Vagas | Serve? |
|---|---|---|
| `ttkgames` | 14 | **Só as 2 do bloco B** — na fila desde 08/09, não enviadas |
| `pipeworks` | 8 | Não — Eugene/OR, tudo produção e engenharia |
| `rocksteady` | 5 | Não — Londres, tech animator, programação, QA, UI/UX web |
| `maverick-games` | 1 | **→ FILA A2** (espontânea) |
| `appquantum` | 1 | Não — *3D Playable Ads Developer* é **programação** (JS/ES6, Phaser, PIXI, Three.js) e ainda pede *"Knowledge of Russian language"* |
| `bighappy` | 2 | Não — dev front/back na Índia |
| `eberjey` | 10 | Não — marca de moda em Miami; o "Art Director" é de moda |
| `embark` | 6 | Não — **é a Embark Student Corp**, poupança educacional canadense. **Não é a Embark Studios.** Homônimo, anote |

Vazios agora (`{"data":[]}`), vale re-testar depois: `tripledotstudios`, `gameplaygalaxy`,
`buildarocketboy`, `everi`, `amber`, `flixinteractive`, `playground-games`, `ruckus-games`,
`singularity6`, `suncreature`.
`tripledottalent` tem só uma `test London job`. `trust.pinpointhq.com` **não é Pinpoint**, é
uma página Vanta.

### E3 — Sobra da Tripledot: quadro Greenhouse novo, mas sem vaga da disciplina

A Tripledot **saiu do Pinpoint**: `tripledot.com/careers` redireciona para
`https://job-boards.eu.greenhouse.io/tripledotstudios`. Fui conferir para não te deixar com
uma recomendação no escuro. **Quadro vivo, 50 vagas**, e a campanha quase não o tocou
(`tripledot` aparece 1× em `docs/index.html` e 2× em `processados.csv`, **0× em `enviados.csv`**).

**Mas não rende linha para você.** As únicas vagas de arte são:
`2D Artist` (Jakarta — fora de escopo), `Mobile Game Illustrator` (Toronto — ilustração 2D,
fora de disciplina), `Lead Technical Artist` (Toronto) e `Principal Technical Artist`
(Toronto e Dallas). **Technical Art não está na sua lista do que conta**, então não puxei
nenhuma para a fila. Fica registrado caso você queira alargar o critério — aí são três
requisições em Toronto/Dallas, escopo bom.

Observação de rede: a API `boards-api.eu.greenhouse.io` dá **502 no CONNECT** pelo proxy; o
HTML de `job-boards.eu.greenhouse.io` passa normal. Use o HTML.

---

# F. COMO EU PROCUREI, E ONDE PAREI

- **Sem navegador**, tudo `curl`, concorrência **7 a 8** em todos os lotes. O proxy não engasgou.
- Jobvite: 5 lotes (208 + 190 + 155 + 1.304 + 2.521 requisições = **4.375 slugs distintos**).
  Os dois maiores vieram de slugificar os **578 nomes de estúdio de `alvos.csv`** e de cruzar
  120 nomes com 20 sufixos comuns (`careers`, `-games`, `hq`, `talent`, `-studios`…).
  Rendimento dos 2.521 do último lote: **1 quadro** (`kwalee`, vazio).
- Pinpoint: 7 lotes (**4.428 slugs distintos**), mesma base de nomes, mais listas de
  VFX/animação europeia, cassino/slots, mobile e web3.
- Os números da tabela do topo são **slugs distintos**, já sem as repetições entre lotes.
- `search.jobvite.com` **403 pelo proxy**, como você avisou — não gastei tempo. O
  `sitemap.xml` do Jobvite também dá 403.
- `html.duckduckgo.com` dá **connection reset** pelo proxy. Usei a busca da ferramenta.
- Os agregadores (`gamejobs.work`, `vfxengine.com`, `workwithindies.com`) são aplicações JS: o
  HTML servido **não contém** nenhuma URL de Jobvite ou Pinpoint. Não servem para descoberta
  por `curl`. **`precisa-de-navegador`** se alguém quiser raspá-los.
- **Não commitei, não dei push, não mandei e-mail, não preenchi formulário.** Não toquei em
  `docs/index.html`, `FILA-DO-VINI.md`, `enviados.csv` nem `processados.csv`. Só escrevi este arquivo.
- Nenhum telefone, endereço, CEP, salário atual ou senha aparece aqui.

**Onde eu pararia da próxima vez, se fosse eu:** as duas famílias estão perto do fundo para
esta disciplina, e o número que mostra isso é o do último lote — **2.521 slugs Jobvite para
1 quadro, e ele estava vazio**. Jobvite tem **um** estúdio da área com quadro grande (DNEG) e
a campanha já o colheu inteiro; Pinpoint é ATS britânico de porte médio e os estúdios de jogos
que o usam têm quadros de 1 a 14 vagas, quase todas fora da disciplina.

O melhor retorno por hora agora **não é mais slug**. Na ordem:

1. **Clicar o bloco B hoje** — duas vagas de Estocolmo com faixa publicada, régua limpa, que
   estão paradas há um dia por um reCAPTCHA numa porta que agora tem alternativa.
2. **Re-testar os 10 quadros Pinpoint vazios** em duas ou três semanas: são estúdios reais
   com quadro configurado, e `postings.json` é barato (404/200 em um `curl`).
3. Se você decidir alargar o critério para **Technical Art**, a Tripledot no Greenhouse EU tem
   três requisições em Toronto e Dallas (E3).
