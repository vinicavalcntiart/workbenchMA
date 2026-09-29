# Caçada na web aberta — 08/09/2026

Agente de prospecção externa. Missão: achar vaga VIVA e RECÉM-PUBLICADA que a campanha ainda não tem.
Nada foi enviado, nada foi preenchido, nenhum arquivo compartilhado foi tocado, nenhum navegador foi aberto. Só `curl`, WebSearch e WebFetch.

**Resultado honesto: 2 vagas NOVAS que passaram na conferência na fonte oficial e na busca de veto.** Mais 1 correção de veto numa vaga que já está no painel e que, pelo texto integral, deveria estar descartada.

O painel está muito bem coberto. De 40 e poucas requisições da disciplina que achei vivas em fonte oficial, quase todas já tinham entrada no painel (lista completa do cruzamento na seção "JÁ ESTAVA NO PAINEL"). O que sobrou de novo é pouco, mas está conferido linha por linha.

---

## 1. TTK Games AB — Character Artist — Estocolmo, Suécia

- **Link DIRETO da requisição:** https://ttkgames.pinpointhq.com/jobs/561860
- **Link DIRETO do formulário de candidatura:** https://ttkgames.pinpointhq.com/postings/88f9f885-d2a6-4815-953d-2866d92fe370/applications/new
- **ATS: PINPOINT (`pinpointhq.com`) — ATS NOVO PARA A CAMPANHA.** Não existe nenhuma ocorrência de "pinpoint" no painel (`grep -ic pinpoint` = 0). Vale mais que a vaga: a Pinpoint é muito usada por estúdio britânico e nórdico, e todo quadro Pinpoint serve `/(...)pinpointhq.com/jobs.rss` com o **texto integral do anúncio dentro do RSS**, o que dispensa navegador para a busca de veto.
- **Data de publicação:** 10/08/2026 (`<pubDate>Mon, 10 Aug 2026 16:02:02 +0100</pubDate>`, do RSS oficial da própria Pinpoint, puxado hoje 08/09 e ainda no ar).
- **Efetivo ou contrato:** EFETIVO. O anúncio diz literalmente `Employment Type: Permanent`.
- **Presencial, híbrido ou remoto:** HÍBRIDO. Campo `Workplace type: Hybrid`, `Location: Stockholm, Sweden`.
- **BUSCA LITERAL DE VETO no texto integral** (`authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`, `days a week`, `French`, `français`, `bilingue`, `resident`): **NENHUMA apareceu.** O texto completo (1.714 caracteres, tirado do RSS oficial, não da listagem) vai de "At TTK Games we are fuelled by a passion..." até a linha de salário e não tem bloco de direito ao trabalho, não tem exigência de residência e não tem número de dias de escritório por semana.
- **Faixa salarial publicada:** SIM, publicada no próprio anúncio: `Starting from 34,000 SEK per month, rising to 47,000 with experience, plus bi-annual bonus, and perks.`
- **Por que vale:** é a descrição do trabalho dele com todas as letras — "Create high-quality, game-ready 3D character models based on concept art, using both scanning, sculpting and modeling techniques" com ZBrush, Maya/Blender, Substance Painter e Unreal/Unity, num estúdio efetivo e híbrido em Estocolmo que ainda publica salário.
- **Já existe no painel?** NÃO. Nem o estúdio, nem a requisição, nem o ATS. O painel não tem nenhuma linha com "TTK".
- **Quem é a casa:** TTK Games AB, Estocolmo, estúdio novo fundado por veteranos da indústria, fazendo um shooter online de nova geração (texto do próprio site). O quadro tem 12 vagas abertas; a de personagem é a única da disciplina dele.
- **Como achei, para quem quiser repetir:** o site ttkgames.com é Nuxt e não serve a vaga por `curl` (a página só diz "Fetching job..."). O caminho foi ler a config do bundle Nuxt, achar a chave `PINPOINT_URL`, deduzir o quadro `ttkgames.pinpointhq.com` e puxar o `jobs.rss`.
- **Formulário, mapeado campo a campo por `curl` (nada foi enviado):** First Name (obrigatório), Last Name (obrigatório), Email Address (obrigatório), Phone (opcional), LinkedIn URL, uma pergunta curta opcional "Link to portfolio / LinkedIn (or upload CV below)", e anexo "Attach Résumé / CV". **Não vi captcha no HTML, veredito só com o clique.**

---

## 2. Behaviour Interactive — Senior 3D Character Artist, 7 Days to Die — Montréal, Canadá

- **Link DIRETO da requisição:** https://jobs.lever.co/bhvr/976b2a8c-9cb4-4066-a755-d0994af408c2
- **Link DIRETO do formulário:** https://jobs.lever.co/bhvr/976b2a8c-9cb4-4066-a755-d0994af408c2/apply
- **ATS:** LEVER (token `bhvr`), conferida pela API pública `api.lever.co/v0/postings/bhvr?mode=json` hoje 08/09. A vaga está viva na API, não é isca de agregador.
- **Data de publicação:** 25/08/2026 (`createdAt` = 2026-08-25T17:44:26Z).
- **Efetivo ou contrato:** EFETIVO. `commitment: "Permanent Full-Time | Permanent temps-plein"`.
- **Presencial, híbrido ou remoto:** HÍBRIDO (`workplaceType: hybrid`), `location: Montreal, QC`, `country: CA`.
- **BUSCA LITERAL DE VETO no texto integral** (8.208 caracteres, descrição em inglês + a versão francesa que vem no mesmo anúncio): **NENHUMA das palavras de veto apareceu.** Detalhe para não confundir quem repetir a busca: `authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`, `days a week`, `bilingue`, `resident`, `visa`, `permis`, `citoyen`, `admissib`, `semaine` — todos ZERO. A única coisa que casa com o padrão `fran` no texto é a palavra **"franchise"** ("an iconic survival franchise"), e o único `statut` é "statut familial" dentro do parágrafo de igualdade de oportunidades. Ou seja: **não há veto escrito, e não há exigência de francês escrita.**
- **Faixa salarial publicada:** não há.
- **Por que vale:** "Own the creation of complex and hero character assets from concept interpretation through final implementation", incluindo "characters, clothing, hair, textures, materials, and supporting props" — é personagem de ponta a ponta, sênior, efetivo, num estúdio de 1.200 pessoas em Montréal, e é uma vaga nova de agosto num IP que acabou de ser comprado (7 Days to Die, Behaviour + The Fun Pimps).
- **Já existe no painel?** NÃO. O painel tem as OUTRAS três requisições de personagem da Behaviour (Dead By Daylight `18024240`, Projet non annoncé `86ddd557`, Senior Texture Artist `55fa65fe`), mas **não tem esta**, que é de 7 Days to Die e foi publicada depois. Conferido pelo id da requisição, não pelo título.

---

## 3. Nota que vale uma rodada: uma vaga do painel tem veto ESCRITO e está sem essa marca

**Rebellion — Senior Character Artist — Oxford / Warwick, Reino Unido**
`https://apply.workable.com/rebellion/j/331FDD9137/` — entrada do painel: "PORTAL|Rebellion|Reino Unido (Oxford)".

Baixei o texto integral pela API oficial do Workable (`apply.workable.com/api/v1/widget/accounts/rebellion?details=true`) e a busca de veto **acusou**:

> "**Right to Work Statement** — This role is only open to applicants who have the permanent right to work in the UK. We are unable to provide or take over visa sponsorship, either now or in the future. Applicants must therefore be able to demonstrate their ongoing eligibility to work in the UK without the need for employer sponsorship."

Isso é veto ESCRITO de direito ao trabalho (`sponsor`, `eligib`, `visa`), não é apenas "precisa de patrocínio". O bloco fica no fim do anúncio, depois dos benefícios, que é exatamente onde a listagem não mostra. Curiosidade: o mesmo anúncio diz, mais acima, "We can provide a relocation package, including moving assistance, temporary accommodation" — a mudança eles pagam, o patrocínio eles recusam.

O mesmo bloco aparece na "Open Art Application - Senior, Lead and Director" da Rebellion (`https://apply.workable.com/rebellion/j/7DA712F769/`, publicada 30/06/2026, Oxford/Warwick/Runcorn/Wakefield), que **não está no painel** — e que por causa desse bloco também já nasce descartada. Registro as duas aqui para ninguém gastar rodada de navegador nelas.

---

## DESCARTADAS, com o motivo LITERAL

### Veto escrito no anúncio

**Snowprint Studios — Senior 3D Character Artist — Estocolmo, Suécia**
`https://career.snowprintstudios.com/jobs/8341580-senior-3d-character-artist` (Teamtailor, viva hoje, foi o único achado de personagem no feed de 7 dias do gamejobs.co).
Motivo, palavra por palavra do anúncio: **"You are currently located in Stockholm, Sweden. We are unable to support relocation for this position."**
Isto é veto de "must be based" escrito. O painel tem a Snowprint só como banco de talentos ("Connect"); a requisição em si não serve.

**Rebellion — Open Art Application (Senior, Lead and Director) — Reino Unido**
`https://apply.workable.com/rebellion/j/7DA712F769/`
Motivo: **"Our roles are only open to applicants who have the permanent right to work in the UK. We are unable to provide or take over visa sponsorship, either now or in the future."**

### Vaga morta, apesar de o agregador manter no ar

**Larian Studios — Lead Character Artist**
Aparece viva em resultado de busca (`jobs.lever.co/larian/ac451c4d-49a0-400a-ad17-634ee67e5529`). Na API oficial `api.lever.co/v0/postings/larian?mode=json` (68 vagas hoje) **essa requisição não existe mais**. A única coisa de personagem viva na Larian é a "Character Artist – Open Application" de 15/05/2025, que já está no painel.

**Blackbird Interactive — Character Artist (8-month contract), Vancouver**
Aparece viva em resultado de busca (`jobs.lever.co/blackbirdinteractive/7eb62bc1-...`). Na API oficial a Blackbird tem **10 vagas e nenhuma é de personagem** (são engenharia, level design, UI/UX, animação técnica e VFX). Morta.

**Housemarque — Lead Character Artist**
Aparece em resultado de busca como `job-boards.greenhouse.io/housemarque/jobs/5528945004`. A API oficial da Greenhouse responde literalmente: **`{"status":404,"error":"Job not found"}`**, e o quadro `housemarque` inteiro está com **0 vagas**.

**Amazon Games Montréal — Character Artist / Artiste de personnages**
Dois ids indexados (`amazon.jobs/en/jobs/2772693` e `/2515730`), os dois devolvem **404** no amazon.jobs hoje. A busca oficial do amazon.jobs por "Amazon Games" devolve 14 vagas e **nenhuma é de arte** (são finanças, jurídico, TPM e um Game Designer em Culver City). O texto do anúncio antigo, aliás, exigia "proficiency in both French and English" — mesmo se voltasse, entra com veto de francês.

**Wētā FX — Look Dev Artist (Senior e Lead), Wellington**
A página da requisição citada em busca, `https://careers.wetafx.co.nz/jobs/1450`, devolve **404**. O quadro `careers.wetafx.co.nz/jobs` responde 200 mas é renderizado por JavaScript e não entrega a lista por `curl`; não achei o endpoint de dados. **Não consigo afirmar que exista requisição de Look Dev viva hoje na Wētā** — fica como alvo para quem tiver navegador. O painel já tem a Wētā FX como banco de talentos.

**Cove Studio — Character Artist 3D Freelance, Lyon/remoto (França)**
`https://emploi.afjv.com/emploi-jeux-video/EINF2346-29045`
Motivo, palavra por palavra: **"Le recrutement pour ce poste est maintenant terminé."**

### Fora da disciplina (li o anúncio inteiro para ter certeza)

**Rodeo FX — "Artiste de maquette" — Montréal** (`https://jobs.smartrecruiters.com/rodeofx/744000143547729`, publicada 14/08/2026, efetiva, NÃO está no painel).
Parecia modelagem pelo nome. Não é. O anúncio diz: **"L'artiste de maquettes conçoit et assemble la mise en page 3D des plans et des séquences (...) structure les scènes dans Maya, définit les caméras"** — é LAYOUT, não modelagem. Fora da disciplina dele. De quebra, tem veto de presença escrito: **"les employé.e.s doivent travailler à partir du studio au moins trois jours par semaine"** (`days a week`).

**Skydance Animation Madrid — Character Surfacing Trainee** (`jobs.lever.co/skydance/7b435bb2-...`, 01/09/2026) e **Environment Surfacing Trainee** (`f5cdab33`) e **Junior Environment Surfacing Artist** (`4c18ce73`). São vagas de estagiário e júnior; ele é Senior com 10+ anos. As irmãs sênior da mesma casa (Senior Grooming TD `9ad28cab`, Senior Environment Surfacing `90d2f2b7`) já estão no painel.

**Framestore — Senior Creature FX TD, Melbourne** (`framestore.recruitee.com/o/senior-creature-fx-td-4`, 01/09/2026, não está no painel). Creature FX é simulação e dinâmica, não modelagem/textura. Mesma razão para as Character FX da Sony Imageworks.

**Insomniac — Senior Facial Character TD (CONTRACT), remoto EUA** (`job-boards.greenhouse.io/insomniac/jobs/6143980004`, 02/09/2026). É TD de rig facial, não de modelagem, é contrato e é remoto restrito aos EUA.

**Gearbox Québec** — quadro Greenhouse tem exatamente 1 vaga hoje, "Directeur·rice du design / Design Director". Nada de arte.

### Fora do escopo geográfico

- Gameloft — 3D General Artist, **Hanói, Vietnã** (`jobs.smartrecruiters.com/Gameloft/744000148170394`, publicada 08/09/2026, é a vaga de arte mais fresca que achei no mundo hoje, e está fora).
- Hasbro — Manager Digital Product Design (Digital Sculpting), **Hong Kong**.
- Lakshya Digital (3D Character Artist e Senior Character Artist - Realistic Heads, Bengaluru/Pune/Gurugram) — **Índia**.
- Vertigo (3D Character Artist, Istambul) e Sperasoft (Belgrado, Erevan) — **Turquia, Sérvia e Armênia**, fora de UE/Nórdicos/Reino Unido/Irlanda.
- thatgamecompany — 3D Character Artist (Mid-Senior), **Remote - US** (`jobs.ashbyhq.com/thatgamecompany/36e101a4-...`) — já está no painel de qualquer forma.
- Magic Media, Devoted Studios, Talentgrator, UserWise — vagas remotas ancoradas em Brasil/Ucrânia/Turquia/Sérvia.

---

## JÁ ESTAVA NO PAINEL (achei vivo em fonte oficial, conferi pelo id da requisição, não repito)

Cruzei tudo contra `docs/index.html` (736 portais, 665 estúdios) pelo **id da requisição**. Estas apareceram vivas na varredura e **já têm entrada**, então não entram na lista de cima:

| Casa | Vaga | id conferido |
|---|---|---|
| 2K / Cloud Chamber | Lead Character Artist Montréal; Lead CA Novato; Senior CA Burnaby | 7888173003, 7888174003, 7835808003 |
| Behaviour | Senior 3D CA Dead By Daylight; Senior 3D CA projet non annoncé; Senior Texture Artist DBD | 18024240, 86ddd557, 55fa65fe |
| Ubisoft | Senior CA Rainbow Six (já enviada e recusada); Lead CA Malmö; Team Lead Modeling; Team lead Character Montpellier | 744000145282762, 744000144027102, 744000141713411, 744000121716487 |
| Sony Pictures Imageworks | Senior Look Dev Montréal; Look Dev Vancouver; Texture e Experienced Texture Vancouver | 7529417003, 6659179003, 4363798003, 4363799003 |
| Rodeo FX | Senior Lookdev Montréal e Toronto; Artiste de développement visuel Senior | 744000145587059, 744000144123709, 744000145587250 |
| Framestore | 3D Modeller contrato curto Montréal; Blender Generalist / Visual Development Artist Montréal | modeleurse-3d, generaliste-blender |
| One Of Us | Modeller, Texture Artist e Look Development Artist, Paris | 2rTHdox84n1Ge86ez2adUb, cXt2aXYi46NxxwuuHiwHhh, itrWRTN6TnCpRVJUfhA4gi |
| People Can Fly | Principal Character Artist Montréal; Senior Asset Artist Hard Surface Varsóvia | 744000134528029, 744000141244724 |
| Wargaming | 3D Character Artist, World of Tanks HEAT, Nicósia | 8161671 |
| Hasbro / Skeleton Key | Lead Character Artist Canadá (a `4318249009` é só a gêmea francesa da `4318250009`) | 4318250009 |
| Bluehole / KRAFTON | 3D Character Artists Project V; Lead Character Artist TERA2 | 8517790002, 8520212002 |
| Loonshot Games | 3D Character Artist Project AA, Seul | 8725151002 |
| Fatshark | Character Artist, Estocolmo | 8190501 |
| Avalanche Studios | Lead Character Artist, Estocolmo | 8f7bd580 |
| Tactical Adventures | Lead 3D Character Artist, Paris (publicada 02/09) | 8311973 |
| Asobo Studio | Character Artist H/F, Bordeaux | 1ab1d28f |
| Frontier Developments | Experienced Character Artist, Cambridge | 3571ace3 |
| Lighthouse Games | Lead Character Artist, Royal Leamington Spa (o `F7F90250DA` do painel É esta vaga; conferi pelo `<title>` da página) | F7F90250DA |
| Rebellion | Senior Character Artist, Oxford/Warwick | 331FDD9137 |
| Keywords Studios | Senior Character Artist, Box Hill (Melbourne) | 744000130680219 |
| Skydance Animation Madrid | Senior Grooming TD; Senior Environment Surfacing; Environment Modeling; Environment Surfacing Lead | 9ad28cab, 90d2f2b7, ebbcdae8, f3ee86d4 |

---

## Endpoints úteis que descobri e que a campanha pode reusar

1. **`https://<sub>.pinpointhq.com/jobs.rss`** — ATS Pinpoint. O RSS traz o **texto integral** de cada anúncio, então a busca de veto sai sem navegador. Foi assim que a TTK Games saiu.
2. **`https://<sub>.teamtailor.com/jobs.json`** (e também `/jobs.rss`) — funciona em domínio próprio também, ex. `https://jobs.arrowheadgamestudios.com/jobs.json`. Formato JSON Feed, com `date_published` e `content_html` completo. Cobre quase todo estúdio nórdico.
3. **`https://api.eu.lever.co/v0/postings/<token>?mode=json`** — Lever tem tenant EUROPEU separado. Asobo e Frontier só aparecem aí; `api.lever.co` devolve 404 para eles. Se a campanha só consultou `api.lever.co`, pode ter dado estúdio europeu por morto sem estar.
4. **`https://jobs.workable.com/api/v1/jobs?query=<termo>&limit=20`** — busca GLOBAL do Workable, todos os clientes de uma vez. `limit` máximo é 20 e o Cloudflare corta com `error code: 1015` se apertar; espaçar 3 a 5 segundos entre chamadas resolve.
5. **`https://gamejobs.co/search?a=7d`** e **`https://gamejobs.co/?format=atom`** — feed do que foi publicado nos últimos 7 dias e nas últimas 24h, com data. Hoje o feed de 7 dias inteiro tinha ~100 vagas e **só uma** era de personagem (a Snowprint, vetada). Serve como termômetro do mercado.
6. **`https://www.swedengamejobs.com/`** — o `__NEXT_DATA__` da home traz 111 vagas suecas com `createdAt` e link direto para o ATS de origem. Foi por aí que a TTK apareceu.
7. **`https://emploi.afjv.com/`** — quadro francês; a home traz `data-ts` (timestamp) por vaga, dá para ordenar por data sem navegador.
8. **`https://api.smartrecruiters.com/v1/companies/<empresa>/postings?limit=100`** e **`/postings/<id>`** para o texto integral. Confirmações: Ubisoft é **`ubisoft2`** (o token `Ubisoft` devolve 0). Mikros Animation não tem quadro próprio (`MikrosAnimation` = 0 vagas); as vagas da Mikros ficam dentro do quadro **`rodeofx`**.

## O que travou

- **`fortiche.paris`, `jobs.wetafx.co.nz` e `modusvfx.com` foram recusados pelo proxy de saída** (`connect_rejected`, política da organização). Não são sites fora do ar, eu simplesmente não consigo alcançá-los daqui. Fortiche (Arcane, Paris/Montpellier/Barcelona) é alvo de alto valor para personagem e ficou por medir.
- `gamejobswork.substack.com` está bloqueado pelo proxy (`EGRESS_BLOCKED`).
- **Sites renderizados por JavaScript não entregam vaga por `curl`**: `hitmarker.net`, `amiqus.com`, `careers.wetafx.co.nz`, `animallogic.com`, `digicpictures.com`, `flyingbark.com.au`, `rsp.com.au`, `ttkgames.com` (nesta eu contornei pela config do Nuxt). Esses ficam para quem tiver navegador.
- `apply.workable.com` derruba com `error code: 1015` (Cloudflare) depois de umas poucas chamadas seguidas; consegui a Rebellion mas perdi a leitura do quadro da Lighthouse Games na segunda tentativa.
- A API pública de vagas da ArtStation não responde: `/api/v2/jobs/search.json` devolve 500 com qualquer combinação de parâmetros que tentei, e `/api/v2/jobs.json` devolve 404.
- Sondei ~230 tokens de ATS (Greenhouse, Lever US e EU, Ashby, Recruitee, Workable, SmartRecruiters, Teamtailor, Pinpoint) para estúdios de jogo, animação, VFX e brinquedo em toda a Europa, Canadá, Oceania, Coreia e Singapura. A maioria dos tokens que chutei não existe, e dos que existem quase nenhum tinha vaga da disciplina aberta hoje. **O mercado de personagem está seco nesta semana**: no feed mundial de 7 dias do gamejobs.co havia exatamente 1 vaga de personagem.
