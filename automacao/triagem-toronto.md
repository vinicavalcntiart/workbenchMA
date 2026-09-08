# Triagem da fatia TORONTO da fila do gamedevmap (Canadá)

Data: 08/09. Fonte: `automacao/fila-gamedevmap-canada.csv`, linhas 168-255 (Toronto) mais as
18 linhas da região ampliada que o brief mandou incluir. Só `curl` e `WebFetch`; nenhum
navegador foi aberto. Nada foi commitado, nada foi enviado.

## 1. Os números, sem inflar

| | Toronto | Região ampliada | Total |
|---|---:|---:|---:|
| Estúdios na fatia | 88 | 18 | 106 |
| Site abriu (HTTP 200/202) | 79 | 15 | 94 |
| Site não abriu | 9 | 3 | 12 |
| Tem quadro/página de carreira que responde | 20 | 0 | 20 |
| Porta de ATS externo identificada | 5 | 0 | 5 |
| Vaga VIVA da disciplina achada | 1 | 0 | 1 |
| Vaga viva da disciplina SEM veto e NOVA para a campanha | **0** | 0 | **0** |
| Estúdios novos para a campanha (não estavam no painel) | 86 | 18 | 104 |

Região ampliada = Markham (1), Oakville (1), Ottawa (12), Scarborough (1), Vaughan (1),
Waterloo (2). **Mississauga não existe na colheita do gamedevmap** — zero linhas.

Cruzamento com o painel (`PORTAIS` 736, `STUDIOS` 665): das 106 linhas, só duas já eram
conhecidas — **Jam City** (linha 226, o painel já tem `Jam City (Principal 3D Generalist)`)
e **Glu Toronto**, que hoje é Electronic Arts, já no painel como `ea.gg/jobs`. As outras 104
são casa nova. Isso é o valor real desta fatia: não são vagas, é estoque de porta.

## 2. A única vaga viva da disciplina encontrada na fatia

### Komi Games — 3D Environment Artist — **DESCARTADA por veto de residência**
- Link direto: https://www.komigames.com/3d-artist
- ATS: **nenhum**. É página Wix estática; a candidatura é por formulário/e-mail do próprio site.
- Prioridade da disciplina: MÉDIA (ambiente, não personagem).
- Estúdio real e relevante: trabalharam em Psychonauts 2, Star Wars: Tales from the Galaxy's
  Edge e King of Fighters XV, e têm parceria com a SEGA num "character-focused action title".
- Busca literal de veto no texto integral do anúncio (baixado inteiro, 4.623 caracteres):

  > "Applicants **must reside** and work within Canada; international applicants will **not be
  > considered**, though your interest in our studio is appreciated!"

  Termos que bateram: `reside`. Não bateram: `authoriz`, `eligib`, `sponsor`, `work permit`,
  `must be based`, `LMIA`, `days a week`, `French`, `français`, `bilingue`.

  **É veto ESCRITO de residência, e é explícito ao recusar candidato internacional.** Descarte.

Komi tem outras quatro páginas de vaga no mesmo site — VFX Artist, 3D Animator, Game Designer
e Bilingual Administrative Assistant — nenhuma é da disciplina do Vini.

## 3. As duas vagas de personagem que a porta de Toronto revelou — e que a campanha JÁ ENVIOU

A linha 169 (2K Play, Toronto) aponta para `2k.com`, cujo `/careers` leva ao Greenhouse
corporativo `job-boards.greenhouse.io/2k` (120 requisições). Filtrando Canadá + disciplina:

| Vaga | Local | Link | Veto literal | Situação |
|---|---|---|---|---|
| Senior Character Artist (2K Sports Lab / Small Axe) | Burnaby, BC | https://job-boards.greenhouse.io/2k/jobs/7835808003 | só `eligib`, e é sobre benefício: "temporary or intern roles will not be eligible for many of these payments or benefits". **Nenhum veto de trabalho.** | **JÁ ENVIADA** — painel `PORTAIS[435]`, `done=true` |
| Lead Character Artist (Cloud Chamber, BioShock, estilizado) | Montréal, QC | https://job-boards.greenhouse.io/2k/jobs/7888173003 | `French`: "For candidates located in Quebec: This position requires professional proficiency in both French and English." Veto de idioma **condicional** a quem mora no Quebec. | **JÁ ENVIADA** — painel `PORTAIS[412]`, `done=true` |

Ambas atualizadas em 21/08/2026, ambas vivas. A de Burnaby pede literalmente groom
(XGen, Ornatrix) — é o ponto forte do Vini — e a de Montréal é personagem estilizado. Se
fossem novas, seriam as duas melhores da fatia. Não são: o dedupe por ID de requisição
mostrou as duas com `done=true` no painel. Registrei a linha 169 como
`porta+disciplina:duplicata-greenhouse-2k` para o maestro não gastar navegador de novo.

Observação de método: a triagem de Montréal marcou a 2K Games só como `porta:greenhouse` e
não desceu no board. O board tinha as duas. Vale a pena descer sempre.

## 4. As cinco portas de ATS achadas na fatia (todas com quadro vazio ou sem disciplina)

| # | Estúdio | ATS | URL da porta | Quadro |
|---|---|---|---|---|
| 176 | Alpha Channel (grupo Kepler Interactive), Liberty Village | **Teamtailor** | https://jobs.alphachannelgames.com/jobs | **Vazio.** `jobs.rss` volta sem um único `<item>`. Tem filtro de departamento "Art" — vale revisitar. Estúdio de veteranos AAA, 25 pessoas, híbrido. Melhor porta nova da fatia. |
| 192 | Certain Affinity (Toronto) | **Jobvite** | widget `app.jobvite.com/...ci=q8CaVfwz` na página `certainaffinity.com/careers/` | **NÃO LIDO.** `jobs.jobvite.com` é bloqueado pelo proxy de egress deste contêiner (curl e WebFetch, os dois). O feed XML da conta volta vazio. Precisa do navegador do maestro. |
| 196 | Dark Slope Studios | **BambooHR** | https://darkslope.bamboohr.com/careers/list | **Vazio** (`totalCount: 0`). A página `darkslope.com/careers` confirma: "We have no open opportunities at this time." O HTML ainda mostra um Technical Artist antigo (req 44/45), mas as duas dão `not_found` na API — vaga morta. Domínio real é `darkslope.com`, não `darkslopestudios.com` como está no CSV. |
| 226 | Jam City (Toronto) | **Lever** | https://api.lever.co/v0/postings/jamcity?mode=json | 18 vagas. Em Toronto só **Game Director**. Da disciplina só fora do Canadá: 3D Artist (Montevidéu) e Principal 3D Generalist (São Francisco) — este último já está no painel. |
| 243 | Lucky VR / Lucky Logic | **Breezy HR** | https://lucky-logic.breezy.hr/ | 1 vaga: Technical Animator, remoto. Não é da disciplina. |
| 216 | Golden Ventures | **Consider** (agregador de VC) | https://jobs.golden.ventures/ | Board de portfólio de fundo, renderizado em JS, não é estúdio. Prioridade baixa. |

## 5. Descartes com motivo literal

Vagas vivas fora da disciplina, com o título como consta no anúncio:

- **Game Hive** (207/208) — https://gamehive.com/careers/ — WP Job Manager, sem ATS externo.
  4 vagas: "INTERMEDIATE / SENIOR SOFTWARE DEVELOPER (UNITY)", "SOFTWARE DEVELOPER (UNITY) -
  LIVE OPS", "SOFTWARE DEVELOPER (BACKEND)", "SENIOR GAME DESIGNER". Nenhuma de arte.
- **Massive Damage** (249) — https://massivedamagestudios.com/jobs/ — 1 vaga: "Senior UE/C++
  Gameplay Software Developer". Candidatura por e-mail (`jobs@massdmg.com`).
- **Autonomicity Games** (178) — https://www.acitygames.com/careers — 1 vaga: "Unreal Engine
  Developer / Designer". Candidatura por e-mail. Site com camada de carteira Solana.
- **Lucky VR** (243) — "Technical Animator", remoto, $110k–$130k. Animação, não é dele.
- **Jam City Toronto** (226) — "Game Director".
- **Hand Eye Society** (217) — https://www.handeyesociety.com/were-hiring/ — "Executive
  Director", e a página traz veto de local: *"This position is only open to those located in
  the city of Toronto."* Cargo administrativo de ONG, fora da disciplina de qualquer jeito.

Vagas que pareciam vivas na varredura de palavra e são **anúncio morto** (a data está no
próprio anúncio, conferida uma a uma):

- **Alientrap** (175) — https://www.alientrap.com/2018/02/06/were-hiring-3d-artist-and-unity-c-developer/
  — "3d artist and Unity C# developer", **06/02/2018**. Batia na busca de disciplina, e é de
  oito anos atrás. O post mais recente da categoria Jobs é de dezembro de 2022.
- **Mighty Yell Studios** (252) — https://www.mightyyell.com/jobs/ — "Dance Consultant",
  *"Application Deadline Nov 30th, 2023"*. Prazo vencido, e é consultoria de dança.
- **M5 Games** (245) — https://www.m5games.com/now-hiring-2d-pixel-artist — "Now Hiring: 2D
  Pixel Artist (Contract)", **26/01/2017**, *"please contact us at info@m5games.com before
  February 8th 2017"*. Pixel art 2D, não é dele.

Páginas de carreira vivas que dizem por escrito que não há vaga:

- Capybara Games (191): *"There are no open positions at the moment"*
- Finish Line Games (202): *"No open roles right now."*
- Kitten Cup Studio (229): *"No open positions at this time"*
- BancyCo (181): *"Currently we have no positions open at BancyCo."*
- Games by Stitch / Stitch Media (209): *"There are no open positions at this time."*
- Dark Slope (196): *"We have no open opportunities at this time."*
- Alpha Channel (176): *"Our Current Opportunities — No matching jobs"*
- Lightning Rod Games (236): página de carreira sem nenhuma listagem
- GestureTek Health (211): só interesse geral, *"is always interested in hearing from ... people"*
- Little Guy Games (239): só `mailto:jobs@littleguygames.com`

## 6. O que travou, nominalmente

**Domínio não conecta** (o proxy devolve `CONNECT tunnel failed, response 502` em `https://`;
`http://` não é opção neste contêiner). Sete em Toronto, três na região:

| # | Estúdio | Domínio | Diagnóstico |
|---|---|---|---|
| 213 | Glu Toronto (Electronic Arts) | glu.com | **DNS não resolve.** É EA hoje, e a EA já está no painel. |
| 214 | Gnometech | gnometech.com | DNS resolve, TLS não sobe |
| 220 | Household Games | household-games.com | DNS resolve, TLS não sobe |
| 228 | Jim Guthrie | swordandsworcery.com | DNS resolve, TLS não sobe |
| 233 | LABS Works | mattkap.net | DNS resolve, TLS não sobe |
| 247 | Magitech Corporation | magitechcorp.com | DNS resolve, TLS não sobe |
| 248 | Maple Powered Games | maplepoweredgames.com | Responde 200 com 114 bytes e redireciona para `/lander`: **domínio estacionado** |
| 361 | A-Game Studios | agamestudios.ca | Raiz devolve 404 |
| 369 | Magmic Games | magmic.com | TLS não sobe, com e sem `www` |
| 430 | Lunarch Studios | prismata.net | TLS não sobe |

**Parede de cliente** (o site está no ar, mas não me entrega o HTML):

| # | Estúdio | O que aconteceu |
|---|---|---|
| 179 | Axon Interactive | 403 e redireciona para `quenchgame.com`, que também dá 403, mesmo com UA de navegador |
| 189 | Brandon Braun | Tumblr devolve **429** (limite de taxa) |
| 253 | Nihilocrat | Tumblr devolve **429** |
| 238 | Little Buffalo | Responde 202 com um `<meta refresh>` para `/.well-known/sgcaptcha/` — **parede de captcha na raiz** |
| 246 | Magic Leap | `resources.magicleap.cloud/careers` (a URL que o próprio sitemap publica) devolve **500** em três variantes; o Workday `magicleap.wd1.myworkdayjobs.com` também 500 |
| 192 | Certain Affinity | `jobs.jobvite.com` **bloqueado pelo proxy de egress** deste contêiner |
| 362 | Conatus Creative | 403 na raiz e em `/careers` |

Sobre captcha, o que o brief manda dizer e é o que sei: **não vi captcha no HTML da maioria
das páginas, e isso não tem veredito** — só a Little Buffalo mostrou parede antes do clique,
e ela mostrou porque a parede está na raiz, não atrás de um botão.

## 7. Método, para quem repetir

1. Toda URL forçada para `https://`; `http://` devolve 400 vazio neste contêiner.
2. `curl -sS -A '<UA de Chrome>' -m 30 -L` em tudo. Sem isso, 403 e timeout viram falso "site morto".
3. Depois da raiz, sonda de caminho em 17 padrões (`/careers`, `/jobs`, `/join-us`,
   `/work-with-us`, `/about/careers`, `/company/careers`, `/join`, `/hiring`, `/opportunities`,
   `/we-are-hiring`, `/about/jobs`, `/company/jobs`, `/studio/careers`, `/careers/jobs`,
   `/team/careers`, `/about-us/careers`, `/get-involved/careers`), descartando o que devolve
   o mesmo tamanho da raiz (catch-all de SPA).
4. **`sitemap.xml` e `robots.txt`, inclusive os sub-sitemaps.** Foi assim que apareceram o
   domínio real da Dark Slope (`darkslope.com`), o `were-hiring` da Hand Eye e o careers da
   Magic Leap. Sites Wix e Squarespace não põem o link no HTML da raiz.
5. JSON do ATS sempre que existir: `api.lever.co/v0/postings/<token>`,
   `boards-api.greenhouse.io/v1/boards/<token>/jobs/<id>`, `<sub>.bamboohr.com/careers/list`,
   e para Teamtailor o **`/jobs.rss`**, que é a maneira mais barata de saber se o quadro está
   mesmo vazio.
6. Dedupe pelo **ID de requisição** contra `PORTAIS`/`STUDIOS` do painel, nunca pelo título:
   foi o `7835808003` e o `7888173003` que mostraram que as duas melhores vagas já tinham ido.

## 8. Vocabulário de status que escrevi no CSV

Mantive o formato de seis campos e o vocabulário de Vancouver/Montréal, com quatro tokens
novos para o que aquelas fatias não tinham encontrado:

- `sem-pagina-de-carreira` — site abre, não há página de carreira (52 em Toronto)
- `pagina-sem-ats` — página de carreira viva, sem ATS externo (14)
- `porta:<ats>` — ATS externo identificado
- `porta+disciplina:nenhum` — porta aberta, disciplina conferida, nada dela (5)
- `porta+disciplina:veto-residencia` — vaga da disciplina achada e descartada por veto escrito (1: Komi)
- `porta+disciplina:duplicata-greenhouse-2k` — vaga da disciplina achada, já enviada (1: 2K Play)
- `site-fora-do-ar` — domínio não conecta ou está estacionado (7 em Toronto)
- `bloqueado:403` / `bloqueado:429` / `bloqueado:500` / `bloqueado:captcha` — o site está no ar
  e não me entregou o conteúdo. **São os que valem uma passada de navegador**, não os `site-fora-do-ar`.

## 9. O que eu passaria ao maestro, em ordem

1. **Alpha Channel Games** (Teamtailor, Liberty Village, grupo Kepler). Quadro vazio hoje,
   mas é a casa mais próxima do perfil na fatia e a porta é barata de reconferir pelo RSS.
2. **Certain Affinity Toronto** (Jobvite). Único quadro que eu não consegui ler, e é a maior
   casa da fatia. Custa uma aba de navegador em `jobs.jobvite.com/certainaffinity`.
3. **Komi Games**. A vaga de hoje tem veto de residência, mas eles fazem "character-focused
   action title" com a SEGA. É porta para quando o Vini tiver situação canadense resolvida.
4. Os sete `bloqueado:*`, se sobrar navegador. Nenhum deles é grande.
5. **Não** gastar navegador nas duas vagas da 2K: as duas já foram enviadas.

## 10. Honestidade

Abri 94 dos 106 sites. Dos 12 que não abriram, 10 têm diagnóstico técnico nomeado acima e 2
(os Tumblr) são limite de taxa que passaria numa segunda rodada. Achei **uma** vaga viva da
disciplina na fatia inteira e ela tem veto escrito; achei **duas** de personagem no Canadá
por trás da porta da 2K e as duas já tinham sido enviadas. O saldo de vaga nova aproveitável
da fatia Toronto é **zero**. O saldo de porta nova é 104 estúdios que a campanha não tinha,
sendo 5 com ATS mapeado e 20 com quadro de carreira que responde.

Toronto rendeu menos que Montréal e na mesma faixa de Vancouver. A leitura que fica é a mesma
das outras duas fatias: a lista canadense do gamedevmap é dominada por microestúdio, indie e
mobile, e as casas de AAA e VFX de Toronto que interessam ao Vini (Ubisoft Toronto, Rockstar
Toronto, Behaviour, Side, Keywords) **não estão nesta fila** porque a campanha já as tocou.
