# CAÇA A AGREGADORES E FAMÍLIAS NOVAS DE ATS — 09/09

**Resultado curto e honesto: a rodada rendeu UMA vaga nova com formulário aberto e UMA porta de
e-mail. Todo o resto que a caça encontrou já estava na campanha, quase tudo varrido em 07/09.**

O motivo é medido e está na última seção: as duas fontes que eu tratei como descoberta —
o sitemap do Hitmarker e o quadro do workwithindies — **já tinham sido mineradas em 07/09**, e a
família HiBob, que eu achei que estava estreando, **já está registrada no `processados.csv` desde
07/09** como "ATS NOVO PARA A CAMPANHA". Refiz trabalho feito. Isso está contado abaixo como erro
de método, não como rendimento.

---

## 1. Placar

### 1.1 Fontes

| Fonte | Resposta | Aproveitável | Observação |
|---|---|---|---|
| `gamejobs.co` | 200 | **sim, 100 vagas** | paginação só com login (302 → `/login`) |
| `workwithindies.com` | 200 | **sim, 97 vagas** | HTML servido inteiro, sem JS |
| `hitmarker.net` | 200 | **sim, 5.000 URLs** | só pelo `sitemap-jobs.xml/p1`; `/jobs` é Vue |
| `remotegamejobs.com` | 200 | **sim, 29 vagas** | só pelo `feed.rss`; HTML é paywall |
| `cgmeetup.com` | 200 | marginal, 5 vagas | quadro quase vazio, nada da disciplina |
| `gamejobs.work` | 200 | **não** | categorias certas, mas vaga exige `/seeker/login` |
| `grackle.jobs` | 000 | não | não conecta |
| `thegamedevjobs.com` | 000 | não | não conecta |
| `animationjobboard.com` | 000 | não | não conecta |
| `3dvf.com/emploi` | 301 | não | redireciona para artigo de 2020 |
| `awn.com/jobs` | 403 | não | bloqueio |
| `screenskills.com/job-board` | 403 | não | bloqueio |

**12 consultadas, 5 renderam, 7 mortas ou fechadas.**

### 1.2 Funil

| Etapa | Número |
|---|---|
| Links de vaga colhidos | **5.231** |
| Batem a disciplina pelo título | **105** |
| Abertos e lidos em TEXTO INTEGRAL | **30** |
| Dentro do escopo geográfico | **27** |
| Passaram a régua de veto | **25** |
| **Passaram o dedupe** | **2** |
| **Passaram o teste do Accept** | **1** |

Os 5.231: 5.000 do sitemap do Hitmarker, 100 do gamejobs.co, 97 do workwithindies, 29 do RSS do
remotegamejobs, 5 do cgmeetup.

**23 das 25 que passaram a régua morreram no dedupe.** A lista do que já estava na campanha está
na seção 4, com o registro literal de cada uma, porque isso é o resultado principal da rodada.

---

## 2. A fila

Ordenada por proximidade do centro do portfólio. São duas entradas. Não invento fila.

### Nº 1 — Activision, Associate Art Director

| Campo | Valor |
|---|---|
| **Estúdio** | Activision (projeto mobile 3D de IP estabelecida) |
| **Cargo** | Associate Art Director |
| **Cidade/País** | Santa Monica, Califórnia, **EUA** |
| **Formato** | Presencial, 4 dias por semana no escritório |
| **Requisição** | **R028122** (id do portal: `ACPUUSR028122EXTERNAL`) |
| **Faixa publicada** | não publica faixa no corpo do anúncio |
| **URL DE CANDIDATURA** | `https://xboxgaming.wd1.myworkdayjobs.com/External/job/Santa-Monica/Associate-Art-Director_R028122-1/apply` |

**Disciplina.** Conta por liderança/supervisão: o anúncio diz que o cargo dá "creative oversight
across character, enemy, environment, animation, VFX, UI, and concept" e é "steward of the IP...
supporting the project's unique **stylized** identity". Supervisão de personagem e ambiente em
projeto estilizado é o centro do portfólio dele, não a borda.

**Régua — 4 casamentos, os 4 falsos positivos:**

- `eligib` → "Subject to **eligib**ility requirements, the Company offers comprehensive benefits
  including: Medical, dental, vision..." — **falso positivo**, bloco de benefícios.
- `based in` → "This role is **based in** our Santa Monica, CA office and follows an onsite work
  schedule of four days per week." — **falso positivo**, diz onde o CARGO fica.
- `days per week` → mesma frase acima, "onsite work schedule of four **days per week**" —
  **falso positivo** de presença híbrida/presencial. Precedente da própria campanha: a Fatshark
  foi enviada em 06/09 com "4 days in the office per week" registrado como "presencial 4 dias".
- `relocat` → "If the Company requires that you move geographic locations for the job, then you may
  also be eligible for **relocat**ion assistance." — **falso positivo, e favorável**: oferece ajuda
  de realocação.

**Nenhum veto escrito.** Precisar de patrocínio de visto é contexto, não critério.

**Dedupe por id de requisição — `R028122` e `ACPUUSR028122EXTERNAL`:**

| Arquivo | Ocorrências |
|---|---|
| `docs/index.html` | **0** |
| `enviados.csv` | **0** |
| `automacao/processados.csv` | **0** |
| `automacao/FILA-DO-VINI.md` | **0** |

**Ressalva que precisa ser dita:** o locatário Workday `xboxgaming.wd1.myworkdayjobs.com/External`
**já foi varrido inteiro em 07/09** ("Quadro External paginado inteiro com limit 20: total 87").
Esta requisição não ficou em nenhum registro, então ou é posterior à varredura, ou escapou dela.
Não é board novo; é requisição nova num board conhecido.

**Teste do Accept:**

| Requisição | Código | Tamanho |
|---|---|---|
| `Accept: */*` | **200** | 23.902 |
| `Accept: text/html,...` + UA de navegador | **200** | 23.902 |
| **Controle**, id inexistente `R999999` | 200 | **5.866** |

Duas 200, sem 302 para o site do estúdio: **é porta.** O controle discrimina (23.902 contra 5.866),
o que prova que o 200 responde ao conteúdo real e não é casca fixa.

---

### Nº 2 — Bunch o Nerds, 3D Artist (environment / map design)

| Campo | Valor |
|---|---|
| **Estúdio** | Bunch o Nerds (indie, Unity) |
| **Cargo** | 3D Artist — environment / map design |
| **Cidade/País** | Remoto, "with a preference for EU/UK time zone; there might be exceptions" |
| **Formato** | Remoto |
| **Requisição** | não tem id; a casa recebe por e-mail |
| **Faixa publicada** | não publica |
| **PORTA DE CANDIDATURA** | `dev@bunchofnerds.studio` (anúncio: `https://www.workwithindies.com/careers/bunch-o-nerds-3d-artist-environment-map-design`) |

**Disciplina.** Ambiente 3D e props para jogo em Unity — conta.

**Régua:** **NENHUM CASAMENTO** nos dezoito termos. Régua limpa. O "preference for EU/UK time zone"
é preferência escrita de fuso, com exceção admitida no próprio texto — não é veto de elegibilidade.

**Dedupe** (por nome, porque não há id): `Bunch o` / `bunchofnerds` →
`docs/index.html` **0**, `enviados.csv` **0**, `processados.csv` **0**, `FILA-DO-VINI.md` **0**.
É casa nova de verdade.

**Teste do Accept: NÃO SE APLICA** — é porta de e-mail, não formulário. Entra na fila de e-mail,
fora da fila de formulário, no mesmo critério que a campanha usou em 07/09 para Sad Owl e Stingbot.

---

### Casa nova achada SEM porta

**Bladework Games — Hard Surface Artist (Contract).** Veio do gamejobs.co, roda em **Polymer**
(`https://jobs.polymer.co/bladework-games/41076`). Dedupe 0/0/0/0, é casa inédita na campanha.
Mas **não é porta**: 403 nas DUAS requisições do teste do Accept. Fica registrada como casa nova
conhecida e parede medida.

### Pendência não resolvida

**Torpor Games — Senior 3D Artist (Generalist), Berlim, híbrido, EUR 4.500–5.000/mês.**
O `processados.csv` de 07/09 diz que o anúncio está **FECHADO**. O workwithindies ainda o serve
com texto integral e o HiBob responde 200 na URL de candidatura. **Não consegui decidir por curl**,
e a razão está na seção 5: o HiBob devolve 200 até para inquilino inexistente. Fica como pendência
para uma sessão com navegador, não como fila. A régua nela, se servir: `days in the office` é
"Work 3 days in the office and 2 days remotely (**Berlin employees**)", bloco de benefícios, falso
positivo; e `resident` é "As **President** Rayne", o falso positivo já catalogado da palavra
President.

---

## 3. Padrões de URL de formulário por família

O que foi medido nesta rodada, para valer nas próximas.

| Família | Padrão | Estado |
|---|---|---|
| **Personio** | `https://<estúdio>.jobs.personio.com/xml` → feed XML com `name`, `office`, `id`; vaga em `/job/<id>?apply` | **Funciona.** Feed limpo, sem captcha. Já usado pela campanha (Aesir). |
| **HiBob** | `https://<estúdio>.careers.hibob.com/jobs/<uuid>/apply` | Padrão certo, **mas o 200 não prova nada** (ver seção 5). Já registrado em 07/09. |
| **Polymer** | `https://jobs.polymer.co/<estúdio>/<id>` | **Parede.** 403 nos dois Accept. |
| **Phenom People** | `https://careers.<estúdio>.com/job/<TOKEN>EXTERNAL/<Titulo>` | **Vitrine, não porta** (ver seção 5). |
| **Collage** | `https://secure.collage.co/jobs/<estúdio>/<id>` | Vivo (Riyo Games). Sem vaga da disciplina. |
| **Dover** | `https://app.dover.com/apply/<Estúdio>/<uuid>` | Vivo (Cheat Code). Sem vaga da disciplina. |
| **Tally** | `https://tally.so/r/<id>`; envio em `POST api.tally.so/forms/<id>/respond` | Vivo, sem captcha. Já usado pela campanha (OMG Studios). |
| **Lark/Larksuite** | `https://<estúdio>.sg.larksuite.com/share/base/form/<id>` | Vivo (Evolite). Fora da disciplina. |
| **JotForm** | `https://form.jotform.com/<id>` | Vivo (The Good Evil). Fora da disciplina. |
| **Teamtailor** | vaga `.../jobs/<id>-<slug>`, formulário `.../jobs/<id>-<slug>/applications/new` | Porta, 200/200. Família já varrida. |
| **Greenhouse** | `https://job-boards.greenhouse.io/<estúdio>/jobs/<id>` | Porta, 200/200. Família já varrida. |
| **GoHire** | `https://jobs.gohire.io/<estúdio>-<hash>/<slug>-<id>` | Já registrado pela campanha em 07/09. |

**Famílias da lista da Frente B que NÃO consegui pôr à prova por falta de slug real:** Factorial,
JazzHR, Traffit, eRecruiter, Trakstar/Recruiterbox, Occupop, Rippling, TalentLyft, Zoho Recruit,
Manatal, Comeet, Oracle Taleo, iCIMS, SAP SuccessFactors, Dayforce. Nenhum estúdio de jogo,
animação ou VFX apareceu nelas em nenhuma das cinco fontes que renderam. **Não são parede; são
não-testadas**, e o motivo está no item 5.3.

---

## 4. O que morreu no dedupe (23 vagas)

Ordenado pelo que a campanha já registrou. Este é o resultado mais útil da rodada.

| Vaga | Registro que já existia |
|---|---|
| Fatshark, Character Artist (`8190501`) | **ENVIADA 06/09**, Teamtailor, req. `98c6393c-...` |
| DuskSoft, Stylized 3D Character Artist | **ENVIADA 31/08** (`enviados.csv` linha 162) |
| Mob Entertainment, Senior Character Artist (`5207518007`) | **ENVIADA 02/09** |
| Mob Entertainment, Senior Environment Artist (`5195729007`) | **ENVIADA 07/09** |
| Makeshift, Senior Character Modeler | **ENVIADA 07/09** pela API do GoHire |
| Makeshift, Senior 3D Environment Artist | mesma casa, mesma rodada de 07/09 |
| OMG Studios, 3D Game Artist Generalist (`GxVoJz`) | **ENVIADA 07/09**, POST 200 na Tally |
| Snowprint, Senior 3D Character Artist (`8341580`) | **ENVIADA 07/09** (Connect, banco de talentos) |
| Lighthouse Games, Lead Character Artist | **JÁ NA FILA-DO-VINI**, revalidada 06/09 |
| Lighthouse Games, Senior Material Artist (Hard Surface) | mesma casa, mesmo quadro |
| Sandbox Interactive/Stillfront, Lead 3D Environment Artist | **ABERTA E RECUSADA 07/09** (exige 7+ anos por escrito) |
| Lightfold, 3D Character Artist (`4512208`) | **DESCARTADA 07/09** (entry 0-1 ano; remoto só na Geórgia) |
| Shishi Studios, 3D Environment Artist | **DESCARTADA 07/09** por veto escrito de residência |
| Grumpyface, 3D Game Artist | **VAGA MORTA 07/09**; confirmei hoje: o Google Forms cai em `/closedform` |
| Golden Hind, 3D Hard Surface Artist | skillshot.pl diz "Ogłoszenie **zarchiwizowane**" |
| Panna Cotta, 3D Environment Artist | Google Forms responde **401**, exige login Google |
| Sad Owl, Senior 3D Environment Artist | já na **fila de e-mail** desde 07/09 |
| Stingbot, 3D Environment Artist | já na **fila de e-mail** desde 07/09 |
| Neon Badger, Mid/Senior 3D Generalist | já mapeada na varredura GRACKLE de 07/09 |
| Pretty Cool Games, Environment Artist | já mapeada 07/09 — e **vetada**, ver 5.4 |
| Warhorse, Level Artist | já na campanha; Breezy, família já varrida |
| Avalanche, Lead Character Artist | **VETADA**, ver abaixo |
| Vertigo Games, 3D Character + 3D Environment | **FORA DE ESCOPO**, ver abaixo |

**Os vetos e os fora de escopo, com a frase inteira:**

- **Avalanche Studios, Lead Character Artist — VETO em `relocat`:** "At Avalanche Studios Group
  we're always on the lookout for talented individuals to join our passionate team, but please note
  that **relocation assistance is not available for this role**." Equivale ao termo `no relocation`
  da régua. Cargo presencial em Estocolmo sem qualquer apoio de mudança.
- **Vertigo Games (as duas) — FORA DE ESCOPO:** "This is an on-site role, requiring you to work
  **5 days a week** from our office in Levent." Levent é **Istambul, Turquia**. A Turquia não está
  no escopo (Ásia só Coreia do Sul e Singapura). Cai por escopo e também teria caído pela régua.
- **Gameloft, 3D General Artist — FORA DE ESCOPO:** estúdio de **Hanói, Vietnã**.

---

## 5. Armadilhas de método medidas hoje

### 5.1 O teste do Accept é CEGO para SPA — precisa de um terceiro tiro

Esta é a descoberta mais importante da rodada, e ela **corrige o protocolo de 09/09**.

O teste de duas requisições pega a armadilha do 302 para o site do estúdio. Mas **não pega a
armadilha inversa**: uma aplicação de página única que devolve a MESMA casca 200 para qualquer URL.
Medido no HiBob:

| URL | Código | Tamanho |
|---|---|---|
| vaga real da Torpor | 200 | 1.342 |
| **uuid inexistente** no mesmo inquilino | **200** | **1.342** |
| **inquilino que não existe** (`zzznotarealstudio`) | **200** | **1.342** |

Byte por byte idêntico nos três. Duas 200 no HiBob **não provam vaga viva, nem estúdio vivo**.

**Regra nova:** todo teste de porta precisa de um TERCEIRO tiro de controle numa URL que
obrigatoriamente não existe. Se o controle devolver o mesmo código E o mesmo tamanho, o teste não
mediu nada. Na Activision o controle discriminou (23.902 contra 5.866) e por isso a porta vale.

### 5.2 200 não quer dizer vaga viva, mesmo fora de SPA

Duas medições independentes hoje:

- **skillshot.pl** (Golden Hind): 200 nos dois Accept, e o corpo diz
  "**Ogłoszenie zarchiwizowane**" — anúncio arquivado.
- **Google Forms** (Grumpyface): 200 no fim, mas depois de 2 saltos para `/closedform`.
  O tamanho é grande e o código é 200; só o **caminho final** denuncia.

Conferir sempre a URL final e uma palavra do corpo, não só o código.

### 5.3 Chutar slug de ATS não descobre nada — de novo, e agora com número

O `processados.csv` já registra essa lição em 06/09, duas vezes. Repeti o erro para medi-la na
família nova: **80 slugs de estúdio europeu de jogo, animação e VFX contra o feed do Personio,
resultado 80/80 em 307.** Zero acertos. O 307 é o redirecionamento do Personio para o marketing
quando o inquilino não existe.

**Só acertam os slugs que vieram de uma fonte.** Os quatro inquilinos reais que apareceram
(`deck13`, `daedalic`, `yager`, `sidekick`) vieram de anúncio de agregador, não de palpite.
É por isso que as quinze famílias da Frente B ficaram não-testadas: sem slug de fonte, não há o
que testar. **A via que funciona continua sendo a inversa: abrir a página de carreiras do estúdio
e ver qual ATS ela embute.**

### 5.4 A régua de dezoito termos tem um buraco

**Pretty Cool Games, Environment Artist: a régua devolveu NENHUM CASAMENTO** — e a vaga é
restrita por escrito. A frase é "**Remote within the UK**". Nenhum dos dezoito termos casa com
"within the UK".

A régua é boa para o que ela cobre, mas "só veto escrito desqualifica" exige ler a linha de
localização mesmo quando os dezoito termos ficam mudos. **Sugestão de termo 19 e 20 para a próxima
rodada: `within the` e `only`** (em "only within", "only in").

### 5.5 Phenom People é vitrine, não porta

`careers.activision.com` roda Phenom People, que não estava em nenhum registro da campanha.
Parecia família nova. **Não é porta:** o campo `applyUrl` do próprio HTML aponta para
`https://xboxgaming.wd1.myworkdayjobs.com/External/...`, isto é, **o Workday que a campanha já
varreu inteiro em 03/09 e 07/09**.

**Lição:** achar um front-end novo não é achar porta nova. Antes de comemorar família nova, ler o
`applyUrl` do anúncio — ele costuma devolver o ATS de verdade, que pode já estar varrido.
O ganho real do Phenom é outro: ele **discrimina vaga morta com 410**, coisa que o Workday cru não
faz, então serve como verificador barato de liveness para o locatário xboxgaming.

### 5.6 Refiz varredura já feita — e o custo foi a maior parte da rodada

Duas fontes que tratei como descoberta já tinham sido mineradas em 07/09:

- **Sitemap do Hitmarker.** Registro de 07/09: "Refeito o cruzamento do sitemap do Hitmarker...
  **12.966 URLs unicas nas tres paginas, 148 batem a disciplina, 87 sobrevivem ao corte. ZERO
  candidatura nova.**" Eu varri a p1 (5.000) e cheguei às mesmas casas.
- **workwithindies.** Registro de 07/09: "workwithindies.com **já foi minerado pela fatia GRACKLE**".

E a família **HiBob já estava registrada em 07/09** como "ATS NOVO PARA A CAMPANHA:
GoHire... e hibob (`<estudio>.careers.hibob.com`)". Eu a "descobri" de novo.

**Lição operacional:** antes de varrer uma fonte, `grep` do nome dela no `processados.csv`. Custa
um comando e teria poupado a maior parte desta rodada. O dedupe por id no fim do funil pega a vaga
repetida, mas não impede o trabalho repetido — para isso o dedupe tem que vir **antes** da fonte,
não depois da vaga.

### 5.7 Duas fontes só entregam por porta lateral

- **remotegamejobs.com**: o HTML é paywall (`/subscriptions/subscribe`), nenhuma vaga no corpo.
  O **`feed.rss` entrega 29 vagas em texto limpo**, sem assinatura.
- **hitmarker.net**: `/jobs` é Vue e não renderiza por curl; o **`sitemap-jobs.xml/p1` entrega
  5.000 URLs** com estúdio e cargo já no slug.
- **gamejobs.co**: a página 1 vem inteira, mas `?p=2` em diante devolve **302 para `/login`**.
  São 100 vagas por sessão anônima, e não há como paginar sem conta.
- **gamejobs.work**: as categorias certas existem (`/category/character-artist`), mas a vaga exige
  `/seeker/login`. Fonte fechada para anônimo.

E uma ressalva sobre o Hitmarker que confirma o registro de 07/09: **o número no fim do slug é o id
INTERNO do agregador, não a requisição do estúdio** — `mob-entertainment-senior-character-artist-4718950`
é a requisição `5207518007` no Greenhouse. Dedupar pelo número do Hitmarker não casa nada.
Além disso o Hitmarker **não expõe o link de candidatura no HTML**: ele fica atrás de um componente
Sprig com token, então o agregador serve para DESCOBRIR estúdio e cargo, e nunca para colher a URL.
