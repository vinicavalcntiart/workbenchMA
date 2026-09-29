# CAÇA A AGREGADORES — 09/09, TARDE

**Janela: anúncios publicados entre 06/09 15h00 e 09/09 15h00 (72h).**
**Fila final: 5 linhas — 4 de família que a automação atravessa, 1 parede marcada.**

Método desta rodada, e é a diferença dela: **a janela de 72h foi medida pela data de publicação
declarada pelo próprio anúncio** (`datePosted` do JSON-LD, `releasedDate` da API, `startDate` do
Workday), **não pelo `lastmod` do sitemap**. O `lastmod` é data de reindexação e mente: das 744
URLs do Hitmarker com `lastmod` nas últimas 72h, só **9** foram de fato publicadas nas últimas
72h. As outras 735 são anúncios de junho, maio, 2025 e até 2024 que o Hitmarker toca de novo.
Filtrar por `lastmod` teria enchido esta fila de vaga velha.

---

## 1. Placar

### 1.1 Funil por agregador

| Agregador | Vagas lidas na janela 72h | Da disciplina | Passaram no escopo | Passaram na régua | Passaram no dedupe |
|---|---|---|---|---|---|
| **Hitmarker** | **9** | **8** | **5** | **5** | **4** |
| **Grackle HQ** | **12** | **2** | **2** | **2** | **1** |
| WorkWithIndies | 9 | 0 | — | — | — |
| RemoteGameJobs | 4 | 0 | — | — | — |
| Skillsearch | 2 | 0 | — | — | — |
| Amiqus | 0 | 0 | — | — | — |
| Values Value | 0 | 0 | — | — | — |
| ArtStation Jobs | **0 — não abriu** | — | — | — | — |
| CreativeHeads | **0 — site desligado** | — | — | — | — |
| The Rookies | **0 — não tem quadro** | — | — | — | — |
| **TOTAL** | **36** | **10** | **7** | **7** | **5** |

### 1.2 Estado de cada fonte

| Fonte | HTTP | Caminho que funcionou | Rendeu |
|---|---|---|---|
| hitmarker.net | 200 | `sitemap-jobs.xml/p1` (5.000 URLs com `lastmod`) + página da vaga com JSON-LD | **sim** |
| gracklehq.com | 200 | `/jobs?department=Art` — 30 vagas com **idade em dias** no cartão; `/rd/<id>` redireciona para o ATS real | **sim** |
| workwithindies.com | 200 | HTML servido inteiro, 95 cartões; `datePosted` na página da vaga | sim, mas seco |
| remotegamejobs.com | 200 | só `feed.rss` (29 itens). `www.` não resolve; o HTML do quadro não tem link de vaga | sim, mas seco |
| skillsearch.com | 200 | `vacancysitemap.xml` (82 vagas). `/jobs` dá 404 e `/jobs/` cai em HTTP 403 | sim, mas seco |
| amiqus.com | 200 | `sitemap.xml` só tem 11 vagas, todas com `lastmod` 13/07 | quase nada |
| valuesvalue.com | 200 | o quadro deles **não fica no site**: fica em `ingamejob.com/en/company/values-value` | sim, mas seco |
| artstation.com/jobs | **403** | Cloudflare. `jobs.json` devolve só a casca do SPA; a API `/api/v2/jobs/search.json` exige CSRF e o token só sai de uma página que também dá 403 | **não** |
| creativeheads.net | 200 | `<title>CreativeHeads.net — Under Reconstruction</title>` | **não** |
| therookies.co | 200 | `/blog/jobs/` é um **artigo recomendando outros quadros** (Hitmarker, ArtStation, ShowbizJobs). Não é quadro | **não** |

**10 agregadores consultados, 7 responderam com vaga legível, 3 mortos.**

### 1.3 Busca multilíngue — negativo medido

O briefing cobra busca em PT/FR/DE/ES/IT/SV/PL porque o filtro só-inglês deixou vaga passar três
rodadas seguidas. Rodei 47 termos (`artiste`, `artista`, `personnage`, `personaje`, `personagem`,
`personaggio`, `charakter`, `charaktere`, `karaktär`, `postać`, `modelador`, `modellierer`,
`environnement`, `umgebung`, `miljö`, `środowisk`, `sculpteur`, `esculp`, `cheveux`, `haare`,
`włos`, `texturen`…) contra as 744 URLs do Hitmarker e os 95 cartões do WorkWithIndies.

**Resultado: 2 casamentos, os 2 falsos positivos** — `figur` dentro de
`nvidia-product-management-and-**configur**ation-engineer` e de
`hp-**configur**e-price-and-quote-tools-optimization-senior-manager`.

**Nenhuma vaga da disciplina escapou por idioma nesta janela.** Isso é resultado, não ausência de
resultado: a hipótese foi testada e deu negativo.

Um achado lateral que vale registrar: o Grackle publica a **mesma requisição em dois idiomas**
(`Senior Technical Artist` ×4 e `Artiste technique` da Epic; `Principal Technical VFX Artist` ×5 e
`Artiste VFX principal`). Ou seja, o risco de duplicata bilíngue que o `RISCO-DUPLICATA.md`
descreve **está vivo no Grackle**. Nenhuma delas é da disciplina, então não afetou esta fila.

---

## 2. FILA PRONTA PARA CLICAR

Ordenada por família de ATS: primeiro as que a automação atravessa, parede por último.

---

### Nº 1 — Blizzard Entertainment · Environment Artist — Unannounced Game

| Campo | Valor |
|---|---|
| **Estúdio** | Blizzard Entertainment |
| **Título exato** | `Environment Artist – Unannounced Game \| Irvine, CA` |
| **ID da requisição** | **R028112** (`jobPostingId` interno `1b592db4093510011fd21586fcec0000`) |
| **Cidade/País** | Irvine, Califórnia, **EUA** — presencial, `Irvine - Blizzard - Blizzard Way` |
| **URL do formulário** | `https://xboxgaming.wd1.myworkdayjobs.com/Blizzard_External_Careers/job/Irvine---Blizzard---Blizzard-Way/Environment-Artist---Unannounced-Game---Irvine--CA_R028112/apply` |
| **Família de ATS** | **WORKDAY — PASSA** |
| **Publicada** | `startDate: 2026-09-08`, `postedOn: "Posted Yesterday"` |
| **Achada em** | Grackle HQ, `/rd/382111` |

**Disciplina.** Environment art de AAA. `5+ years of experience in AAA Environment Art`.

**Régua — 7 casamentos, os 7 falsos positivos:**

- `eligib` ×4 → todos no bloco de benefícios: *"Subject to **eligib**ility requirements, the Company
  offers comprehensive benefits including: Medical, dental, vision…"* — **falso positivo**.
- `relocat` → *"If the Company requires that you move geographic locations for the job, then you may
  also be eligible for **relocat**ion assistance."* — **falso positivo, e favorável**: oferece ajuda
  de realocação.
- `within the` → *"Work with production to complete tasks **within the** given timeframe identifying
  any blockers…"* — **falso positivo**, é o cronograma de produção, exatamente o caso
  `within the production schedule` que o briefing lista.
- `only` ×2 → *"…beloved across platforms, borders, backgrounds, and generations - **only** made
  possible by building a work environment that nurtures the artistry…"* e *"Our ability to build
  immersive and innovate worlds is **only** enhanced by diverse teams…"* — **falso positivo**, é
  retórica institucional, não restrição.

**Nenhum veto escrito.** Nenhuma linha de autorização, patrocínio ou residência.

**Dedupe — `R028112`:** 0 em `enviados.csv`, 0 em `processados.csv`, 0 em `docs/index.html`,
0 em `FILA-DO-VINI.md`. As requisições Blizzard/Activision já registradas são `R000106`,
`R025229`, `R027817`, `R027931`, `R028122` — **nenhuma é esta**.

**Duas ressalvas que precisam ser ditas:**

1. **Blizzard está na lista de vigilância do `RISCO-DUPLICATA.md`** (1 aberta | 2 enviadas). Conferi:
   os três contatos anteriores foram **por e-mail** (`crobinson@` entregue em 05/09; `jhwang@` e
   `lli@` deram bounce). **Nenhuma candidatura por portal foi enviada à Blizzard.** É requisição
   nova por porta nova.
2. **O site `careers.blizzard.com/global/en/job/R028112` diz "the job you are trying to apply for
   has been filled".** Mas o Workday por trás dele **contradiz o wrapper**: a API
   `wday/cxs/.../R028112` devolve `"canApply": true`, `"posted": true` e a descrição inteira
   (14.776 bytes). Teste do Accept no `/apply`: `Accept: */*` → **200 / 24.458**; Accept de
   navegador → **200 / 24.458**; **controle** com id inexistente `R999999` → 200 / **5.973**.
   O controle discrimina, então o 200 responde ao conteúdo real. **É porta** — mas o Vini deve
   saber que o site público está dizendo o contrário, e que isso pode virar um "preenchida" mais
   à frente.

---

### Nº 2 — Makeshift Software · Senior Environment Artist

| Campo | Valor |
|---|---|
| **Estúdio** | Makeshift Software Inc. (jogo: *Hexborn*, action-RPG dark fantasy) |
| **Título exato** | `Senior Environment Artist` |
| **ID da vaga** | **300611** (client hash do quadro: `hnqMpHxc`) |
| **Cidade/País** | Columbus, Ohio, **EUA** — remoto 3–6 meses, depois híbrido presencial |
| **Faixa publicada** | **USD 145.000 – 150.000 / ano** |
| **URL do formulário** | `https://jobs.gohire.io/makeshift-software-hnqmphxc/senior-environment-artist-300611/` |
| **Família de ATS** | **GOHIRE — PASSA** (ver nota abaixo) |
| **Publicada** | `Date Posted: September 7th, 2026` (declarado na própria página do GoHire) |
| **Achada em** | Hitmarker `4718837` |

**Disciplina.** *"You'll take concept art and turn it into fully realized terrain and environment
assets inside Unity, using our terrain toolchain and a modern PBR texturing pipeline."*

**Régua — ZERO casamentos.** Passei os 20 termos pelo texto integral da página do GoHire (3.047
caracteres). Nenhum termo da régua aparece. O trecho mais próximo de uma condição é:

> *"**Work Arrangement.** We'll start fully remote for a 3–6 month grace period while you ramp up
> and get embedded with the team, then transition to a hybrid on-site schedule."*

Isso é **arranjo de trabalho**, não veto: diz onde o cargo fica e quando, sem exigir nada do
candidato quanto a autorização, residência ou nacionalidade.

**Dedupe — `300611`:** 0 em `enviados.csv`, 0 em `processados.csv`, 0 em `docs/index.html`,
0 em `FILA-DO-VINI.md`. Nenhuma caça anterior.

---

### Nº 3 — Makeshift Software · Associate Character Modeler

| Campo | Valor |
|---|---|
| **Estúdio** | Makeshift Software Inc. (*Hexborn*) |
| **Título exato** | `Associate Character Modeler` |
| **ID da vaga** | **300872** |
| **Cidade/País** | Columbus, Ohio, **EUA** — remoto 3–6 meses, depois híbrido |
| **Faixa publicada** | **USD 145.000 – 150.000 / ano** |
| **URL do formulário** | `https://jobs.gohire.io/makeshift-software-hnqmphxc/associate-character-modeler-300872/` |
| **Família de ATS** | **GOHIRE — PASSA** |
| **Publicada** | `Date Posted: September 9th, 2026` — **a mais nova da fila, publicada hoje** |
| **Achada em** | Hitmarker `4739682` |

**Disciplina — é o centro exato do portfólio dele.** O anúncio pede personagem estilizado:

> *"We're in the midst of an art direction shift — moving from a strongly **stylized** anime
> aesthetic into a blend of photorealism and anime influence."*
> *"**Support both stylized and photorealistic character work**… Model 3D characters — heroes,
> guild allies, and enemies — from concept art through to final, game-ready assets."*

**Régua — ZERO casamentos** no texto integral (4.243 caracteres). Mesma frase de Work Arrangement
do nº 2, mesmo enquadramento.

**Dedupe — `300872`:** 0 em todos os quatro registros.

**Ressalva de senioridade, escrita porque é real:** o Hitmarker classifica esta vaga como
`Entry (0–1 years)` e o anúncio diz *"a character modeler early in their career"*. O Vini é sênior
com crédito em *The Wingfeather Saga*. **Isto não é veto** — não há termo da régua e a faixa
publicada é de sênior (USD 145–150k, idêntica à do Senior Environment Artist, o que sugere que o
rótulo "Entry" do Hitmarker está errado). Mas é desalinhamento de rótulo, e ele deve decidir.

---

### Nº 4 — Makeshift Software · Associate Environment Artist

| Campo | Valor |
|---|---|
| **Estúdio** | Makeshift Software Inc. (*Hexborn*) |
| **Título exato** | `Associate Environment Artist` |
| **ID da vaga** | **300742** |
| **Cidade/País** | Columbus, Ohio, **EUA** — remoto 3–6 meses, depois híbrido |
| **Faixa publicada** | **USD 100.000 – 125.000 / ano** |
| **URL do formulário** | `https://jobs.gohire.io/makeshift-software-hnqmphxc/associate-environment-artist-300742/` |
| **Família de ATS** | **GOHIRE — PASSA** |
| **Publicada** | `Date Posted: September 8th, 2026` |
| **Achada em** | Hitmarker `4728234` |

**Disciplina.** Environment art com kitbash modular: *"A portfolio showing environment art
fundamentals — composition, lighting sensitivity, and material work"*, e
*"leaning on kitbashed modular environment pieces"*.

**Régua — ZERO casamentos** no texto integral (4.278 caracteres).

**Dedupe — `300742`:** 0 em todos os quatro registros.

**É a mais fraca das três da Makeshift** — faixa menor e rótulo associate em disciplina
secundária do portfólio. Fica na fila porque passa em tudo, mas é a última a clicar.

---

> ### ⚠ Aviso obrigatório sobre as três entradas da Makeshift (nº 2, 3 e 4)
>
> **A campanha JÁ ENVIOU candidatura à Makeshift Software em 07/09** — `Senior Character Modeler`,
> vaga **299993**, pela API do GoHire às 11h50 UTC, com resposta 200 e `userId 206760092`.
>
> As três acima são **requisições diferentes** (300611, 300742, 300872 contra 299993), o que a
> regra do `RISCO-DUPLICATA.md` permite explicitamente: *"o dedupe é pela REFERÊNCIA DA REQUISIÇÃO,
> nunca pelo nome do estúdio nem pelo título da vaga."*
>
> **Mas a Makeshift é um estúdio pequeno** (10 vagas abertas no total). Mandar mais três
> candidaturas dois dias depois da primeira, na mesma caixa, é decisão do Vini e não da automação.
> Minha leitura: **enviar no máximo o nº 2 (Senior Environment Artist)**, que é a única
> genuinamente sênior e de disciplina distinta da que já foi enviada. Não estou removendo 3 e 4 da
> fila porque eles passam em tudo que foi medido — estou marcando o risco.

---

### Nº 5 — GIANTS Software · Junior 3D Artist - Vehicle specialist ⛔ PAREDE

| Campo | Valor |
|---|---|
| **Estúdio** | GIANTS Software GmbH (*Farming Simulator*) |
| **Título exato** | `Junior 3D Artist - Vehicle specialist` |
| **ID da requisição** | **744000148212939** · `refNumber: REF45T` |
| **Cidade/País** | Brno, Região da Morávia do Sul, **Chéquia** — presencial (`remote: false, hybrid: false`) |
| **URL do formulário** | `https://jobs.smartrecruiters.com/GIANTSSoftwareGmbH/744000148212939-junior-3d-artist-vehicle-specialist?oga=true` |
| **Família de ATS** | **SMARTRECRUITERS — PAREDE (DataDome)** |
| **Publicada** | `releasedDate: 2026-09-08T11:38:20Z` |
| **Achada em** | Hitmarker `4735711` |

**Disciplina.** Hard-surface modeling puro: *"Precise 3d asset production of all kinds of
agricultural machinery"*, *"Great skills in **hard-surface modeling**"*, *"Ability to create
realistic 3D assets and textures in high quality"*. É borda do portfólio (hard surface realista,
não personagem estilizado), mas é modelagem 3D e está dentro do filtro de disciplina.

**Régua — ZERO casamentos** no texto integral da API do SmartRecruiters (2.437 caracteres).
O trecho que mais se aproxima e **não veta**:

> *"Very good knowledge of English at least at level B2"*

Isso é **inglês**, não o idioma local. O briefing veta "exigência de idioma local" — exigir inglês
B2 num estúdio suíço-alemão-tcheco é o idioma de trabalho da equipe, não uma barreira de
nacionalidade. **Não há exigência de tcheco.**

**Dedupe — `744000148212939` e `REF45T`:** 0 em todos os quatro registros. Atenção: `grep GIANTS`
dá 13 casamentos na campanha, mas **todos são de outras empresas** — GIANTSTEP (Coreia do Sul),
Giant Skull e Giant Sparrow. **GIANTS Software é casa nova para a campanha.**

**Por que está marcada como parede:** SmartRecruiters é DataDome pelo briefing. A página de
candidatura devolve 200/106.312 por `curl`, mas isso é a leitura — o POST do formulário é o que o
DataDome intercepta. **Não priorizar.** Se o Vini quiser esta, é clique manual dele.

---

## 3. O que morreu, e por quê

**Total examinado: 36 vagas dentro da janela de 72h. Sobraram 5. Morreram 31.**

### 3.1 Morreu por DISCIPLINA — 26

| Onde | Quantas | O que era |
|---|---|---|
| WorkWithIndies | 9 | Lead Game Designer, 2D Artist ×2, Tech Artist/2D Unity, Web Developer, Pixel Animator, UI/UX Designer VR, Senior Producer, Animator. **Zero 3D na janela.** |
| Grackle HQ | 10 | Senior Animator, VFX Artist, Senior Technical Artist ×4 + `Artiste technique`, Gameplay Animator, UX Designer ×2, Senior Gameplay Animator |
| RemoteGameJobs | 4 | Lead Game Designer, Roblox Game Producer ×2, Senior Producer |
| Skillsearch | 2 | Account Manager (Speech/AI), Financial Director |
| Hitmarker | 1 | Virtuos, `Stagiaire Technical Artist - Character Pipeline` (Cergy, FR) — estágio de **tech art**, não de arte de personagem |

### 3.2 Morreu por ESCOPO GEOGRÁFICO — 3

| Vaga | Onde | Motivo |
|---|---|---|
| SuperPlay, `3D Artist` (Hitmarker 4725999, pub. 08/09) | **Tel Aviv, Israel** | Ásia fora de Coreia do Sul e Singapura |
| Gameloft, `3D General Artist` (Hitmarker 4735675, pub. 08/09) | **Hanói, Vietnã** | idem |
| Gameloft, `3D General Artist` (Hitmarker 4724199, pub. 08/09) | **Hanói, Vietnã** | idem |

As duas da Gameloft eram **SmartRecruiters** (`744000148170394` e `744000148132989`) — parede de
qualquer forma.

### 3.3 Morreu por RÉGUA DE VETO — 0

**Nenhuma vaga morreu na régua nesta rodada.** Das 7 que chegaram nela, as 7 passaram. Os únicos
casamentos de termo foram os 7 falsos positivos da Blizzard, todos documentados na entrada nº 1.

Isso não é a régua sendo relaxada — é que os anúncios que sobreviveram ao escopo geográfico são de
estúdio pequeno (Makeshift), de casa europeia (GIANTS) ou de AAA que só fala de patrocínio no bloco
de benefícios (Blizzard). **Nenhum deles escreveu uma exigência de autorização, residência ou
nacionalidade.**

### 3.4 Morreu por DEDUPE — 2

| Vaga | ID | Onde já estava |
|---|---|---|
| **Activision, `Associate Art Director`** | **R028122** | `enviados.csv` (**ENVIADA em 09/09**), `processados.csv`, `docs/index.html`, e é o **nº 1 da caça-agregadores desta manhã**. Achei de novo pelo Grackle `/rd/382084`. Dedupe funcionou. |
| **Makeshift Software, `Senior Character Modeler`** | **299993** | `processados.csv` (**ENVIADA em 07/09** pela API do GoHire, 200 + `userId 206760092`), `docs/index.html` ×2 |

### 3.5 Não chegou a ser lida — 3 agregadores

| Fonte | Motivo | O que já foi tentado |
|---|---|---|
| **ArtStation Jobs** | **403 do Cloudflare** em `/jobs`. `jobs.json` devolve 200 mas é a casca do Angular (`<title>ArtStation - Explore</title>`), sem vaga. A API real `POST /api/v2/jobs/search.json` devolve **412 `Invalid CSRF Token`**; o cookie só traz `__cf_bm`, sem `CSRF-TOKEN`, porque a página que emitiria o token é a mesma que dá 403. **Sem navegador, não abre.** |
| **CreativeHeads** | Site fora do ar: `<title>CreativeHeads.net — Under Reconstruction</title>`, 4.918 bytes, com `noindex`. Não é bloqueio, é desligamento. |
| **The Rookies** | `/blog/jobs/` **não é um quadro de vagas** — é um artigo listando outros quadros (Hitmarker, ArtStation, ShowbizJobs, Rebelway). O The Rookies não opera board próprio. Riscar da lista de agregadores. |

E duas que responderam mas quase não rendem:

- **Amiqus** — o quadro vivo roda em **Shazamme** (`sdk.shazamme.io`), carregado por JS, e o
  `sitemap.xml` só indexa **11 vagas, todas com `lastmod 2026-07-13`**. A única da disciplina é
  `3d-artist-in-artist-jobs-1328898` (Guildford, UK) com `datePosted: 03-Oct-2025` — quase um ano.
  `sitemap_jobs.xml` e `jobs-sitemap.xml` dão 404. **Sem navegador, o Amiqus rende zero.**
- **Values Value** — não tem quadro no próprio site (todo caminho redireciona para a home). O
  quadro deles fica em `ingamejob.com/en/company/values-value`: **7 vagas abertas**, a única da
  disciplina é `Level Artist` (remoto), publicada em **19-08-2026**, três semanas fora da janela.
  Escritórios em Kyiv e Kharkiv.

---

## 4. Nota sobre a família GoHire

O briefing não lista GoHire nem entre as que passam nem entre as paredes. **Ela passa, e a campanha
já provou isso**, registrado em `processados.csv` em 07/09:

- `widget.gohire.io/widget/hnqMpHxc` serve o fluxo inteiro (só exige `Referer`);
- `POST api.gohire.io/upload-chunk` sobe o PDF em base64 em pedaços de 0,5 MB e devolve a chave;
- `POST api.gohire.io/apply?clientHash=hnqMpHxc&jobId=<id>` recebe o JSON e devolve 200 com `userId`.

Reconferi hoje: **o widget de 185.863 bytes não contém `recaptcha`, `hcaptcha`, `turnstile`,
`captcha` nem `sitekey`** — zero casamentos. As três páginas de vaga também: zero.
`api2.gohire.io` devolve 403 e `api.gohire.io/jobs` devolve 404, mas o endpoint `/apply` é o que
importa e já foi atravessado.

**Ressalva de método que a própria entrada de 07/09 registra e que eu repito:** a tela de sucesso do
widget é desenhada **no cliente** a partir de um 200 sem campo `error`. Ela não é prova
independente. O que é prova é o 200 com `userId` — a mesma evidência que o Vini teria clicando com
a própria mão, nem mais nem menos.

Controle que fiz hoje para garantir que os 200 respondem ao conteúdo real: id inexistente
`.../associate-character-modeler-999999/` → **404 / 4.289 bytes** com `<title>GoHire</title>`,
contra 200 / ~20.000 bytes com o título certo nas três vagas reais. **O controle discrimina.**

---

## 5. Erros de método desta rodada

Registro porque a rodada da manhã foi punida por não registrar.

1. **Meu primeiro filtro de disciplina perdeu duas vagas.** A lista de termos não tinha
   `general artist`, e as duas `3D General Artist` da Gameloft passaram batidas. Só apareceram
   porque rodei uma varredura larga de conferência sobre as 215 URLs restantes. Elas morreram no
   escopo (Vietnã) de qualquer jeito, mas **o filtro falhou antes do escopo**, e da próxima vez
   pode ser uma que importa. `generalist`/`general artist` entram na lista base.
2. **Paginação do Grackle: gastei quatro requisições à toa.** `?pageNumber=1..5` devolve sempre a
   mesma página de 30 vagas. O "Show More" da página é dos **filtros**, não da lista. O quadro do
   Grackle serve 30 por corte e não pagina por URL — o que salvou a rodada é que ele ordena por
   idade e mostra a idade no cartão, então as 30 mais novas **cobrem a janela de 72h inteira**
   (a 30ª já está em 7d). Para 72h, o Grackle é suficiente; para qualquer janela maior, não serve
   sem filtro.
3. **O `lastmod` do Hitmarker quase me fez inflar a fila.** Se eu tivesse parado no `lastmod`, teria
   entregue 21 "vagas da disciplina das últimas 72h" quando o número real é 8. As outras 13 são de
   junho, maio, janeiro, e duas de 2024/2025. **`lastmod` é reindexação; `datePosted` é publicação.**
   Isto vale para toda caça futura no Hitmarker.

---

## 6. Fechamento

**5 linhas na fila** — 4 de família que a automação atravessa (1 Workday, 3 GoHire) e 1 parede
marcada (SmartRecruiters).

Se o aviso da Makeshift for respeitado e só o nº 2 for enviado, **a fila efetiva é de 2 cliques**:
Blizzard `R028112` e Makeshift `300611`.

Nenhuma vaga foi inventada e nenhuma foi admitida com veto escrito. Os 31 descartes estão contados
um a um na seção 3.
