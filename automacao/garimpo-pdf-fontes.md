# Garimpo das tres fontes do PDF de links do Vini

Rodado em 08/09/2026. Ferramentas: `curl` e APIs publicas dos ATS. **Nenhum navegador foi aberto.**
Nada foi enviado, nenhum formulario preenchido, nenhum arquivo compartilhado da campanha foi tocado.

Saida de dados: `automacao/garimpo-pdf-fontes.csv` (454 linhas).

---

## Resumo em uma tabela

| Fonte | O que e | Itens | Em escopo | Estudios NOVOS | Vagas vivas da disciplina, sem veto |
|---|---|---|---|---|---|
| 1. `tinyurl.com/mapOfStudios` | Google My Maps classico, **desativado** | 0 | 0 | 0 | 0 |
| 2. `tinyurl.com/Animation-VFX-Game-job-studios` | Planilha Google viva, atualizada 07/09/2026 | 2.356 vagas / 628 estudios | 565 estudios | **354** | **40** (destas 32 de disciplina alta) |
| 3. `games-career.com` | Portal alemao de vagas de games | 44 vagas / 14 empregadores | 14 | 13 | **0** |

---

## FONTE 1 — `https://tinyurl.com/mapOfStudios`

### Para onde resolve
`curl -sSIL` devolve **HTTP 301** para:

```
http://www.google.com/maps/ms?ie=UTF8&hl=en&msa=0&msid=113662601588408460998.00047bb475f51963d7c48&ll=84.474065,-152.578125&spn=112.417883,360&z=1
```

E um **Google My Maps do formato antigo** (parametro `msid`, nao `mid`), da epoca do "Google Maps Classic".

### O que aconteceu
O proprio Google converte o `msid` antigo para o identificador novo `19reUmf7JAbj6w3BHokdlpQ1HcoA`
(isso aparece no `url_effective` do redirecionamento) e entao devolve **404 em todas as portas testadas**:

| Porta tentada | Resultado |
|---|---|
| `https://www.google.com/maps/d/kml?mid=19reUmf7JAbj6w3BHokdlpQ1HcoA&forcekml=1` | HTTP 404, 1652 bytes |
| `https://www.google.com/maps/d/viewer?mid=19reUmf7JAbj6w3BHokdlpQ1HcoA` | HTTP 404, 1652 bytes |
| `https://maps.google.com/maps/ms?msid=<msid>&msa=0&output=kml` | HTTP 404 apos redirecionar para o mid novo |
| `https://www.google.com/maps/ms?...&output=kml` | HTTP 404 apos redirecionar |
| `https://mapsengine.google.com/map/kml?mid=<msid>` | HTTP 404 |

Trecho literal do corpo devolvido:

```html
<title>Error 404 (Not Found)!!1</title> ... <p><b>404.</b> <ins>That's an error.</ins>
```

### Veredicto
**Fonte morta. Zero estudios extraidos, zero vagas.** Nao e bloqueio de user-agent nem timeout: o 404
vem com corpo de erro do proprio Google, identico nas cinco portas, e o `content-type` e `text/html`.
Mapas My Maps criados no formato classico foram descontinuados; sem o KML nao ha o que raspar.
**Nao vale insistir nesta URL** — se o Vini quiser esse mapa de volta, precisa de uma copia nova.

---

## FONTE 2 — `https://tinyurl.com/Animation-VFX-Game-job-studios`

### Para onde resolve
HTTP 301 para `https://docs.google.com/spreadsheets/d/1eR2oAXOuflr8CZeGoz3JTrsgNj3KuefbdXJOmNtjEVM/`,
que redireciona (302) para `/edit`. Titulo: **"Animation/VFX/Game Industry Job Postings"**.

### Como extrai
O caminho `/export?format=csv` **falhou com HTTP 401** (a planilha e publica para leitura mas nao
esta "publicada na web", que e o que o `export` exige). O que funcionou foi o endpoint de visualizacao:

```
https://docs.google.com/spreadsheets/d/1eR2oAXOuflr8CZeGoz3JTrsgNj3KuefbdXJOmNtjEVM/gviz/tq?tqx=out:csv
```

HTTP 200, 684.502 bytes, 2.357 linhas por 24 colunas.

**Abas**: so existem duas. A de dados (`gid=1184720131`, identica a padrao) e uma aba "Tip Jar"
(`gid=1952335105`, 1.163 bytes, so um pedido de doacao do mantenedor). Nao ha aba escondida com
estudios; **toda a planilha e uma tabela unica de vagas**.

Colunas uteis (com uma coluna vazia entre cada par): Studio, City, Province/State/Region, Country,
Job Title, Experience Level, On-Site/Remote/Hybrid, Date, Source/Contact (a URL da vaga), Software, Notes, Region.

### Quao viva esta
**Muito viva.** A vaga mais recente e de **07/09/2026, ontem**. Distribuicao das datas mais cheias:
04/09 (109), 02/09 (109), 17/08 (92), 22/07 (84). E uma planilha mantida diariamente, nao um arquivo morto.

### Quantos itens tem
- **2.356 vagas**
- **628 estudios distintos**
- Por regiao: Europa 1.046, America do Norte 843, Asia 281, Oceania 78, America do Sul 14, Africa 4

### Quantos em escopo
Aplicando o filtro geografico eliminatorio (America do Norte, Europa, Oceania, e na Asia so Coreia do
Sul e Singapura; sem India, Brasil ou Japao):

- **565 estudios distintos em escopo**
- **125 vagas de disciplina** no total, das quais **97 em escopo geografico** e **93 URLs distintas**
  (dedupe feito pela URL da requisicao, nao pelo titulo — a Wargaming, por exemplo, aparece com o
  mesmo titulo "Character Artist" em 6 requisicoes diferentes)

### Quantos NOVOS para a campanha
Cruzamento contra os 665 registros de `STUDIOS` e os 736 de `PORTAIS` do painel:

- **354 estudios em escopo sao NOVOS** para a campanha
  - **10** deles ja tem vaga da disciplina no ar agora: Folks VFX (CA), ILM Sydney (AU),
    Automatik VFX (DE), Team from Earth (CY), 2K Sports Lab (CA), Miraculous (FR),
    One Man Studio (UK), Naughty Dog (US), Infinity Ward Barcelona (ES), Knifewing Entertainment (US)
  - **344** sao novos mas com vaga de outra area no momento — entram no CSV como pista de prospeccao,
    com a ressalva honesta de que **nao baixei os anuncios deles**
- Dos 58 estudios com vaga da disciplina em escopo, **48 a campanha ja conhecia**

### Verificacao das 93 vagas, uma a uma
Baixei os **93 anuncios inteiros**. Onde o ATS renderiza em JavaScript e o HTML vinha vazio, fui pela API:

| ATS | Como resolvi |
|---|---|
| BambooHR (9 vagas vinham com 8 caracteres de texto) | `https://<sub>.bamboohr.com/careers/<id>/detail` devolve JSON com `jobOpeningName`, `jobOpeningStatus`, `datePosted` e a descricao inteira |
| Workable (2 vagas) | `https://apply.workable.com/api/v2/accounts/<conta>/jobs/<shortcode>` |
| Ashby (thatgamecompany) | POST GraphQL em `jobs.ashbyhq.com/api/non-user-graphql` |
| Workday (Infinity Ward) | endpoint direto deu 403; usei o POST `/wday/cxs/xboxgaming/External/jobs` do quadro |

Em cada texto integral rodei a busca literal por: `authoriz`, `eligib`, `sponsor`, `work permit`,
`must be based`, `LMIA`, `days a week`, `French`, `resident`, `visa`, `citizen`, `relocat`,
`onsite`, `on-site`, `hybrid`, `based in`.

**Resultado:** 63 vivas, 27 mortas, 3 indeterminadas.
Das 63 vivas, **40 sem nenhum veto escrito** e 23 com veto escrito.

### As vagas vivas da disciplina, SEM veto escrito

Disciplina ALTA — personagem, modelagem, texturizacao, look dev, grooming:

| Estudio | Vaga | Local | Link direto | Busca de veto |
|---|---|---|---|---|
| **ILM Sydney** *(NOVO)* | Senior Modeler | Sydney, AU | https://www.disneycareers.com/en/job/moore-park/senior-modeler/391/100108246096 | nenhum veto; unica condicao escrita e hibrido, min. 2 dias/semana |
| **2K Sports Lab** *(NOVO)* | Senior Character Artist | Burnaby, CA | https://job-boards.greenhouse.io/2k/jobs/7835808003 | "2 days a week" e "legally authorized" sao PERGUNTAS do formulario, nao veto |
| **Offworld Industries** | 3D Character Artist | New Westminster, CA | https://owi.bamboohr.com/careers/199 | nenhum; "citizenship" so no paragrafo de igualdade de oportunidades. Aberta 10/07/2026 |
| **Ubisoft Montreal** | Senior Character Artist (Rainbow Six Siege) | Montreal, CA | https://jobs.smartrecruiters.com/Ubisoft2/744000145282762 | nenhum |
| **Ubisoft Montreal** | Team Lead - Modeling (Unreal) | Montreal, CA | https://jobs.smartrecruiters.com/Ubisoft2/744000141713411-team-lead-modeling-unreal | nenhum |
| **Massive Entertainment** | Lead Character Artist (The Division 2) | Malmo, SE | https://jobs.smartrecruiters.com/Ubisoft2/744000144027102 | nenhum |
| **Rodeo FX** | Senior Lookdev Artist (multiplas vagas) | Toronto, CA | https://jobs.smartrecruiters.com/RodeoFX/744000144123709 | nenhum; "hybrid" so na expressao "hybrid environments" |
| **DNEG Montreal** | Character Modeler (DNEG Animation) | Montreal, CA | https://jobs.jobvite.com/double-negative-visual-effects/job/ooyGAfwW | nenhum — ao contrario da irma de Londres |
| **DNEG Londres** | Groom TD (DNEG ANIM) | Londres, UK | https://jobs.jobvite.com/double-negative-visual-effects/job/oQKJAfwD | nenhum. Contraste medido: a outra vaga da DNEG Londres traz o veto em destaque, esta NAO |
| **Framestore** | 3D Modeller, contrato curto | Montreal, CA | https://framestore.recruitee.com/o/modeleurse-3d-3d-modeller-contrat-court-terme | so a PERGUNTA "Will you need visa sponsorship?" no formulario |
| **WildBrain Studios** | Groom Supervisor, CG (Feature) | Vancouver, CA | https://wildbrain-career.talent-soft.com/job/job-groom-supervisor-cg-feature-_5580.aspx | nenhum |
| **Behaviour Interactive** | Senior 3D Character Artist - Dead by Daylight | Montreal, CA | https://jobs.lever.co/bhvr/18024240-e637-409f-a647-b422541e2dc7 | nenhum; permanente full-time, hibrido |
| **Behaviour Interactive** | Senior 3D Character Artist (projeto nao anunciado) | Montreal, CA | https://jobs.lever.co/bhvr/86ddd557-7d9b-48f1-ab04-0a90ba38e2dc | nenhum |
| **Frontier Developments** | Experienced Character Artist | Cambridge, UK | https://jobs.eu.lever.co/frontier/3571ace3-9f1a-4db2-9e2b-5eb8c8487181 | nenhum; o anuncio OFERECE pacote de mudanca |
| **Lighthouse Games** | Lead Character Artist | Royal Leamington Spa, UK | https://apply.workable.com/lighthousegames/j/F7F90250DA/ | nenhum (lido pela API v2 do Workable) |
| **Blue Zoo Animation** | Blender Modeller - Experienced | Londres, UK | https://careers.blue-zoo.co.uk/vacancies/1310/blender-modeller--experienced.html | nenhum; personagens, props e ambientes |
| **Lakshya Digital / Keywords** | Character Artist - Hair Specialist | remoto, Canada e Reino Unido | https://apply.workable.com/keywords-intl1/j/CA33DB1208/ | nenhum. Grooming de cabelo/pelo em tempo real. Contrato |
| **Wargaming** | 3D Character Artist (World of Tanks:HEAT) | Nicosia, CY | https://job-boards.greenhouse.io/wargamingen/jobs/8161671 | o anuncio diz "eligible for relocation & immigration support" — o oposto de veto |
| **Skydance Animation** | Senior Grooming TD | Madrid, ES | https://jobs.lever.co/skydance/9ad28cab-87cd-4235-ae9b-b4c53a3457e5/ | nenhum; "authorized" so no aviso antifraude do estudio |
| **Asobo Studio** | Character Artist H/F | Bordeaux, FR | https://jobs.eu.lever.co/asobostudio/1ab1d28f-6f7c-4106-b43f-6ef78dcb7603 | nenhum; presencial |
| **TAT Productions** | Lead Character Modeling & Blendshape 3D | Toulouse, FR | https://jobs.tatprod.com/fr/offres/lead-character-modeling--blendshape-3d-e13168 | "J'ai besoin d'un visa" e opcao do formulario, nao veto. Aceita 100% teletrabalho. CDD 12 meses |
| **3Doubles Producciones** | 3D Modeler - Lead | Tenerife, ES | https://3doubles.factorial.es/job_posting/3d-modeler-lead-318348 | nenhum; presencial |
| **Techland** | Character Artist | Varsovia, PL | https://jobs.smartrecruiters.com/TechlandSA/744000137670539-character-artist | nenhum |
| **Techland** | Character Artist | Wroclaw, PL | https://jobs.smartrecruiters.com/TechlandSA/744000145235194-character-artist | nenhum; requisicao distinta da anterior |
| **Teyon** | Senior/Lead Character Artist | Cracovia, PL | https://teyon.elevato.net/en/seniorlead-character-artist,j,158 | nenhum; OFERECE apoio de mudanca. Aceita remoto ou hibrido |
| **Awaken Realms** | 3D Character Artist | Wroclaw, PL | https://www.skillshot.pl/jobs/39589-3d-character-artist-at-awaken-realms | nenhum |
| **Mob Entertainment** | Senior Character Artist | St. Louis, US | https://job-boards.greenhouse.io/mobentertainment/jobs/5207518007 | sponsorship so como PERGUNTA de formulario. USD 82-102k |
| **NEOWIZ / NOUGH Studio** | 3D Character Modeler (proximo jogo de Lies of P) | Seongnam, KR | https://jobs.lever.co/neowiz/5ad83a87-38c2-4441-81da-5ab73e3217fc | nenhum; presencial, efetivo. Coreia do Sul esta no escopo |
| **RocketBrush Studio** | 3D Character Artists | Limassol, CY | https://www.linkedin.com/feed/update/urn:li:activity:7479897459117330432/ | nenhum no post; ciclo completo de personagem |
| **Insomniac Games** | Character TD | Burbank, US | https://job-boards.greenhouse.io/insomniac/jobs/6143980004 | so PERGUNTAS de formulario. Disciplina limitrofe (TD e mais tecnico) |
| **Folks VFX** *(NOVO)* | Senior Groom Artist, freelance 3 semanas | Montreal/Toronto/Vancouver, CA | https://www.linkedin.com/feed/update/urn:li:activity:7501380289416294400/ | nenhum. Nao ha requisicao, so o post do recrutador Michael Jalbert. Contrato curtissimo |

Disciplina MEDIA (ambiente, shading tecnico) ou fora do perfil, tambem vivas e sem veto:
Skydance Madrid tem quatro de ambiente (Environment Modeling Artist, Environment Surfacing Lead,
Senior Environment Surfacing, Junior Environment Surfacing); Frontier tem Shader Artist;
Dream Games tem Pipeline Look Dev TD em Londres; Swaybox tem CG Modeler de cenarios e veiculos em
Nova Orleans; Illumination Paris e ESTAGIO; Knifewing e Character Designer 2D — **fora da disciplina**.

### As 23 vivas COM veto escrito (nao aplicar)
IGG Canada ("unable to sponsor work permits"), Image Engine x2 ("required to be based in British
Columbia"), Stirling Animation x5 ("must be based regionally within the UK"), DNEG Londres Character
Modeller ("eligible to work in the UK without visa sponsorship" + escritorio 3x/semana), Brown Bag
Toronto ("Ontario residency"), Digital Domain x2 ("BC residents only"), thatgamecompany ("must be
authorized to work in the U.S or Canada. We are unable to sponsor"), Team from Earth ("based in
Europe"), Automatik VFX ("EU candidate ... willing to relocate"), Tonic DNA ("Must be Quebec
residents", e 2D), Avalanche Studios ("relocation assistance is not available"), Skeleton Key
(3 dias presenciais em Montreal), Cloud Chamber x2 (frances profissional para quem esta no Quebec),
Disney TV Animation (fully on-site Glendale, e 2D), Skydance trainees x2 (exigem matricula em curso).

### As 27 mortas (armadilhas de anuncio antigo)
Wargaming 5 requisicoes, Stim Studio 4 (todas 404), ILM Londres 4 (Lead Texture, Senior Texture,
Creature TD, Groom Artist — todas devolvem a pagina generica do Disney Careers; as duas de Texture
o painel ja registra como enviadas e recusadas), Naughty Dog, Krafton Montreal, teamLFG, Atomic
Cartoons, Mob Entertainment (uma das duas), Kabam (404 Lever), Ubisoft March of Giants ("This job
has expired"), Brown Bag Dublin ("no longer open"), Candlestick Games ("This position has been
closed"), Blue Zoo UK-only Environment Modeller ("Vacancy Not Found"), Framestore Melbourne (404),
One Man Studio (404 na API do BambooHR), Prismatic Studios ("We Currently Have No Open Positions"),
Infinity Ward Barcelona (nao aparece na API de busca do Workday).

**Isto e material de anti-duplicata**: 4 dos estudios "novos" da fonte (Naughty Dog, One Man Studio,
Infinity Ward Barcelona, Knifewing) so aparecem porque a planilha guarda o anuncio depois de morto.

### As 3 indeterminadas
- **Rising Sun Pictures**, Senior Modelling Artist, Adelaide — o SAP SuccessFactors responde
  "The system can't display the job at this time" para a requisicao 623 e a busca do quadro nao
  renderiza sem JavaScript. Nao consegui confirmar nem ler.
- **Miraculous** (Paris), Modeler — a fonte e um post de LinkedIn que exige login.
- **Big Shot Pictures** (Los Angeles) — a URL da planilha nao e uma vaga: e a busca generica do
  LinkedIn por "Senior Character Artist in United States", com 491 resultados. Nao ha requisicao.

---

## FONTE 3 — `https://www.games-career.com`

### Para onde resolve
Nao ha redirecionamento: **HTTP 200 direto**, 86.796 bytes. Site vivo.
E o portal alemao de vagas de games da Quinke Networks.

### O que e e como extrai
Portal de anuncios classico, com HTML servido pelo servidor (nao precisa de JavaScript).
A home diz textualmente: **"Currently 44 job offers from 12 employers"**.

**Conferi a paginacao de verdade, como manda a licao 3.** A home lista so 15 vagas.
Testei `?page=2` (conexao resetada), `/Joboffer/2/` e `?start=15`: as duas ultimas devolveram
**exatamente os mesmos 15 ids** (33671, 33730, 33732, 33734, 33736, 33743, 33744, 33750, 33755,
33757, 33759, 33767, 33771, 33772, 33773). Ou seja, **nao ha paginacao** — a home mostra as mais
recentes e o resto so aparece por categoria.

Entao varri **as 13 categorias uma a uma** (`/Joboffer/Art_and_Layout_and_Illustration`,
`/Joboffer/others`, etc.) e uni os resultados: **exatamente 44 vagas distintas**, batendo com o
contador do proprio site. A soma dos contadores por categoria tambem fecha em 44
(Art 10, others 8, Localization 5, Game Design 3, Programmer Game 3, Programmer IT 3, QA 3,
Legal 2, Product Mgmt 2, Programmer Mobile 2, Community 1, Controlling 1, Marketing 1).

### Quantos itens tem e quantos em escopo
- **44 vagas**, **14 empregadores** identificados (o site declara 12 "Top Employer";
  na varredura por categoria aparecem outros anunciantes)
- Todos em escopo geografico: 13 na Alemanha, 1 na Austria, 1 recrutadora com sede em Gdansk (Polonia)
- **13 empregadores sao NOVOS** para a campanha

Empregadores: Nintendo of Europe, InnoGames, Lotum media, XYRALITY, Com2uS Europe, upjers,
Travian Games, Spiele-Palast, Thera Bytes, gameXcite, Articy Software, Mi'pu'mi Games (AT),
8Bit sp. z o.o. (recrutadora, PL), Drafted.GG.

### Vagas da disciplina
**ZERO.** Nenhuma vaga de personagem 3D, modelagem de personagem, texturizacao, look development,
grooming ou visual development em todo o portal.

A categoria "Art / Layout / Illustration", com 10 vagas, e composta inteiramente de:
Product Designer UX/UI (x2, Lotum), Associate Design Coordinator/Specialist e Design Coordinator
Textile (x5, Nintendo — sao cargos de design de produto e textil, nao de arte 3D),
Head of Game Design & Art (Mi'pu'mi), Lead Game Backend Developer (categorizada errado) e
Senior Environment Artist (8Bit).

As duas unicas limitrofes, com anuncio integral baixado e busca de veto rodada:

| Vaga | Local | Link | Busca de veto |
|---|---|---|---|
| Senior/Lead Environment Artist (8Bit para o estudio de Shapez) | remoto integral, DE | https://www.games-career.com/Joboffer/33661_Senior-Environment-Artist_8Bit-sp-zoo | **VETO ESCRITO**: "This position is open to candidates based in Germany". Alem disso e AMBIENTE, disciplina media |
| Technical Artist / 3D Generalist | remoto, DE | https://www.games-career.com/Joboffer/33663_Technical-Artist--3D-Generalist-wmd_Thera-Bytes-GmbH | nenhum veto. Mas e tech art e game design em FPS tatico, nao personagem |

### Veredicto
**Fonte viva mas praticamente esteril para o Vini.** O portal e pequeno (44 vagas), fortemente
concentrado em Alemanha, e nas areas de programacao, localizacao, QA e produto. As duas vagas mais
proximas da disciplina sao de ambiente e de tech art, e a de ambiente tem veto de base na Alemanha.

O valor real desta fonte nao esta nas vagas de hoje e sim nos **13 empregadores alemaes novos**, que
podem entrar na fila fria de contato direto. Vale voltar ao portal periodicamente, mas nao vale
prioridade: o volume e baixo e a rotatividade das vagas de arte 3D e proxima de zero.
Registro que a indicacao veio do estudio Overhype.

---

## O que travou

1. **A fonte 1 esta morta de verdade**, nao por bloqueio de cliente. Cinco portas diferentes de KML
   devolveram 404 com o corpo de erro do Google.
2. **`export?format=csv` nao serve para toda planilha publica.** Deu 401 nesta. O `gviz/tq?tqx=out:csv`
   resolveu, e vale registrar como truque padrao da campanha.
3. **9 vagas ficaram invisiveis no HTML** porque o BambooHR renderiza em JavaScript e o corpo vinha com
   8 caracteres, o que parece vaga morta. A API `/careers/<id>/detail` devolveu o JSON completo com
   status, data de publicacao e texto — foi assim que descobri, por exemplo, que a Image Engine mantem
   aberta uma requisicao publicada em **marco de 2023**.
4. **O Workday da Infinity Ward respondeu 403** no endpoint direto da requisicao. Contornei pela API
   POST de busca do proprio quadro, que confirmou que a requisicao R027813 nao existe mais.
5. **11 das 93 URLs da planilha sao posts ou buscas de LinkedIn**, nao requisicoes. Tres delas nao deram
   para verificar (exigem login ou sao busca generica) e estao marcadas como indeterminadas no CSV,
   nao como boas.
6. **29% das vagas da planilha estavam mortas** (27 de 93). A planilha nao remove anuncio encerrado,
   entao ela e otima como mapa de estudios e perigosa como lista de vagas. As 4 requisicoes da ILM
   Londres reforcam a armadilha ja registrada no painel.
