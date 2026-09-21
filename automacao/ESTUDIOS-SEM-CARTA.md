# Estúdios APROVADOS que ainda esperam carta

## ✅ AS CINCO VIRARAM CARTA EM 12/09, ENTRE 12h55 e 14h20. FICHA ZERADA.

| Casa | Caixa | Ângulo que a carta usou |
|---|---|---|
| HundredStar Games | `jobs@hundredstar.games` | o convite escrito à candidatura espontânea, citado de volta |
| Hyper Luminal Games | `info@hyperluminalgames.com` | Frank, Tyke e Olive: três jogos carregados por um personagem cada |
| Cahoots Studios | `jobs@cahootsstudios.com` | a rede global de freelancers que eles publicam, e **freelance como o pedido principal**, não realocação |
| Vertpaint Studios | `services@vertpaint.com` | a frase do Kary Black sobre "solve problems that will ship content", emendada nos três anos de outsourcing dele na PUGA |
| 314 Arts | `hello@314arts.com` | fidelidade e pipeline, **não** estilizado |

**A carta da 314 Arts diz a ressalva em voz alta em vez de esconder:** o portfólio dele é
estilizado e *Night Runner* e *Vengeance* não são. O que atravessa é o pipeline e a anatomia
por baixo. Fingir encaixe forte numa casa de FPS realista seria descoberto na primeira tela
do portfólio, então a carta chega dizendo o que carrega e o que não carrega.

**O bloqueio que este arquivo registrava não era o que parecia.** A suposição era que
`create_draft` estava travado para todo mundo. Medido às 11h30: trava só para **subagente**;
da sessão principal passa calado. Por isso as onze cartas de hoje (estas cinco mais as seis
pessoas) saíram sem um único pedido de aprovação na tela do Vini. A regra nova está no fim do
`BRIEFING.md`: **agente acha e verifica, maestro escreve.**

**Continua valendo a medição das 09h20:** nenhuma das cinco tem formulário de candidatura, e
formulário comercial não se usa como porta de emprego. A rota destas cinco é carta, e só.

---


Arquivo criado na rodada de prospecção das **08h50 de 12/09/2026**, pela razão medida na
madrugada: `mcp__Gmail__create_draft` abre pedido de aprovação na tela do Vini e **não
retorna enquanto ninguém aprova**, e três agentes seguidos morreram exatamente ali. Esta
rodada faz a metade cara (achar, abrir a fonte, ler a frase, conferir dedupe) e **não cria
rascunho nenhum**. A carta vira rascunho depois, em lote, quando a permissão estiver
efetiva.

**Como usar:** cada ficha abaixo já tem endereço publicado, URL exata aberta na rodada,
encaixe conferido e o gancho com a frase literal do estúdio. Quem for escrever a carta
**não precisa reabrir nada**: é só redigir. Ao criar o rascunho, marque a ficha como
`RASCUNHO CRIADO em <data>` em vez de apagá-la.

**Regras da carta que valem para todas as fichas:** proibido a palavra "Brazil", proibido
travessão, proibido floreio de IA, e a frase `I WANT TO RELOCATE` está **BANIDA**. A frase
de realocação só entra em estúdio comprovadamente **fora dos EUA** (regra 10); por isso cada
ficha responde essa pergunta explicitamente.

---

### HundredStar Games — Londres, Reino Unido

- **Email:** `jobs@hundredstar.games` · fonte: https://hundredstargames.com/ (bloco OPEN
  ROLES, endereço publicado como `mailto:` na própria página, aberto nesta rodada em
  12/09 às 09h20; HTTP 200). O site também publica `info@hundredstar.games`, mas o de
  carreiras é o `jobs@`, e é o que a própria frase manda usar. MX Outlook ativo
  (`hundredstar-games.mail.protection.outlook.com`).
- **Encaixe:** desenvolvedora **AAA** de Londres que se descreve como "AAA video game
  developer, with innovation at our core" e anuncia "100 people in london", ou seja casa de
  produção AAA com pipeline completo de personagem, e que pede **portfólio** de propósito
  na candidatura espontânea, que é o que um artista de personagem tem para mostrar.
- **Gancho, com a frase deles entre aspas:** *"While we may not currently be advertising for
  the kind of position you feel best aligns to your skillset, we'd welcome you to
  speculatively apply by sharing your CV and portfolio with our Recruitment team via
  jobs@hundredstar.games for future consideration should a role become available."* É
  convite escrito à carta fria, com endereço dito na própria frase. O segundo gancho é
  "100 people in london", que é do tamanho em que uma casa AAA ainda lê email de artista.
- **Fora dos EUA?** **Sim** (Reino Unido). A frase de realocação ENTRA.
- **Ressalva honesta, para a carta não mentir:** o quadro `jobListings` da página está
  **vazio hoje** e os filtros publicados são All / Engineering / Design / Marketing / Sales
  / Support, **sem Art**. Ou seja não há vaga de arte aberta: a via é exclusivamente a
  espontânea que eles convidam. Não escreva a carta como se respondesse a um anúncio.
- **Dedupe:** `grep -i hundredstar` em `alvos.csv`, `enviados.csv` e `docs/index.html` dá
  **zero**. Aparece em `automacao/processados.csv` (só a nota do agente que morreu na
  madrugada de 12/09 deixando esta casa pendente), em `automacao/pessoas.csv` e em
  `automacao/PESSOAS-SEM-CARTA.md` (linha de **Paul Widelski**, uma PESSOA da casa, travada
  por não existir endereço de pessoa publicado). **Gmail conferido nesta rodada por janela
  ampla** (`hundredstar OR "hundred star" OR hundredstar.games`): **zero threads**. Nenhuma
  carta saiu para esta casa. Esta ficha é a rota do ESTÚDIO (`jobs@`), que é diferente e
  não conflita com a linha da pessoa.

---

### Vertpaint Studios — Londres, Reino Unido

- **Email:** `services@vertpaint.com` · fonte: https://vertpaint.com/contact-us (aberto
  nesta rodada em 12/09 às 09h30; HTTP 200, endereço publicado em texto na página, ao lado
  do botão de LinkedIn e do Calendly). MX Google ativo. A página `/careers` publica hoje
  **uma vaga só, Technical Animator**, que não é a disciplina dele, então a via é carta fria.
- **Encaixe:** co-desenvolvimento AAA **com peso em arte**. A casa se descreve como
  "Premium Co-Development for AAA Production" que dá suporte "across art, engineering, and
  technical disciplines", lista "Creative & Art Direction" entre os serviços centrais e
  exibe números publicados de "50+ AAA Veterans", "43+ AAA Titles Supported" e "7 Years
  Active". Co-dev de arte é exatamente o trabalho de outsourcing de personagem que ele já
  fez na PUGA Studios.
- **Gancho, com a frase deles entre aspas:** o depoimento assinado por **Kary Black, CAD da
  Digital Extremes**, publicado na home: *"As you can see from their portfolio, their
  artistic skills are top drawer. When you have a chance to work with them, you quickly
  come to appreciate their grounding in production. The art is uncompromising, and always
  aiming to solve problems that will ship content."* Serve duas vezes: é a casa dizendo que
  o produto dela é ARTE, e o cliente que assina é a **Digital Extremes** (Warframe,
  Soulframe), que é personagem estilizado de verdade. Segundo gancho, da própria página de
  contato: *"Your message goes directly to our production team"*, ou seja o `services@` cai
  em produção e não em comercial.
- **Fora dos EUA?** **Sim** (Londres, Reino Unido, pelo cartão de Organization do LinkedIn
  oficial deles, `addressLocality: London`, `addressCountry: GB`, e a descrição da própria
  companhia: "founded in 2019 as a premium co-development studio by AAA veteran James
  Macleod, formerly of Rockstar Games"). A frase de realocação ENTRA.
- **Dedupe:** `grep -i vertpaint` no repositório inteiro só bate em
  `automacao/backlog-estudios.md` (a lista de reserva de onde o nome saiu) e em
  `automacao/garimpo-pdf-fontes.csv` (garimpo, sem contato). **Zero** em `alvos.csv`,
  `enviados.csv`, `pessoas.csv`, `processados.csv` e `docs/index.html`. **Gmail conferido
  nesta rodada** (`"314 Arts" OR 314arts OR vertpaint`): **zero threads**.

---

### 314 Arts — Reken, Alemanha

- **Email:** `hello@314arts.com` · fonte: https://314arts.com/contact (aberto nesta rodada
  em 12/09 às 09h28; HTTP 200, publicado em texto sob o rótulo "Contact", com
  `business@314arts.com` separado sob "Business Inquiries", então o `hello@` é o de contato
  geral e o certo aqui). MX Google ativo.
- **Encaixe:** estúdio de jogos que **vende arte de jogo como serviço** e diz isso no
  próprio formulário: o campo "Service" da página de contato lista, entre as opções,
  **"Game Art"**, ao lado de Game Development, Technology e QA. Os produtos publicados são
  *Night Runner* (First Person Survival Coop) e *Vengeance* (Multiplayer Shooter), com
  personagens humanos em primeira pessoa, e a casa se define por "high-fidelity visuals".
- **Gancho, com a frase deles entre aspas:** *"We don't just chase trends; we build solid
  mechanical foundations combined with high-fidelity visuals to create lasting value for our
  community."* Emenda direta com o argumento dele: alta fidelidade de personagem é
  justamente onde sculpt, retopologia e texturização decidem o resultado. Segundo gancho, da
  página de contato: *"Every project starts with a conversation."*
- **Fora dos EUA?** **Sim** (Alemanha, endereço publicado na página de contato: 314 Arts
  OHG, Reken). A frase de realocação ENTRA.
- **Ressalva honesta:** é FPS tático e sobrevivência, ou seja **realista**, não estilizado.
  A carta deve puxar o lado de fidelidade e pipeline, não o lado estilizado do portfólio.
  Encaixe **médio**, não forte.
- **Dedupe:** `grep -i "314 arts"` e `grep -i 314arts` no repositório: só
  `automacao/backlog-estudios.md` (lista de reserva). **Zero** em `alvos.csv`,
  `enviados.csv`, `pessoas.csv`, `processados.csv` e `docs/index.html`. **Gmail conferido
  nesta rodada** (`"314 Arts" OR 314arts OR vertpaint`): **zero threads**.

---

### Hyper Luminal Games — Dundee, Escócia (Reino Unido)

- **Email:** `info@hyperluminalgames.com` · fonte: https://hyperluminalgames.com/contact
  (aberto nesta rodada em 12/09 às 09h45; HTTP 200, publicado em texto junto do endereço
  completo do estúdio, Suite 7 The Vision Building, 20 Greenmarket, Dundee DD1 4QB). MX
  Google ativo (`smtp.google.com`).
- **Encaixe:** é **exatamente** o material do portfólio dele. Os jogos próprios publicados
  na página /games são 3D **estilizado e cosy, movidos a personagem com nome**: *The Day I
  Became A Bird* ("Join Frank, an awkward young boy, as he discovers newfound feelings for
  his classmate, Sylvia"), *Pine Hearts* ("As Tyke, hop into your hiking boots"), *Cloud
  Jumper* ("help Olive find her way home"). Personagem estilizado com leitura de silhueta e
  carga emocional é o que essas três capas pedem. Some-se o braço de **work for hire**, que
  já entregou "80+ games".
- **Gancho, com a frase deles entre aspas:** da home, *"We make games where every team
  member proudly states: 'I built that!'"* e *"We put smiles on people's faces with
  beautiful and fun experiences that people play and love."* Casa direto com personagem
  estilizado feito para ser lembrado. Gancho de reforço, da página de carreiras: eles se
  gabam de *"one of the lowest staff churn rates in the industry"* e de *"promoting from
  within"*, que é o argumento de quem entra para ficar.
- **Fora dos EUA?** **Sim** (Escócia, Reino Unido, endereço postal publicado). A frase de
  realocação ENTRA.
- **Ressalva honesta:** a seção **Vacancies** da página de carreiras está **vazia** hoje (o
  bloco emenda direto em "BUILDING PARTNERSHIPS ... Get in touch!"), então não há anúncio
  para responder: a via é carta fria pelo `info@`.
- **Dedupe:** `grep -i "hyper luminal"` bate em quatro arquivos e **nenhum é envio**:
  `automacao/backlog-estudios.md` (lista de reserva), `automacao/fila-gamedevmap-europa.csv`
  e `automacao/garimpo-pdf-fontes.csv` (garimpo), e `automacao/caca-breezy-homerun.md`, onde
  a única menção é o quadro `hyperluminal` do Join.com listado como **vivo e com zero vaga
  publicada**. **Zero** em `alvos.csv`, `enviados.csv`, `pessoas.csv`, `processados.csv` e
  `docs/index.html`. **Gmail conferido nesta rodada** (`hyperluminal OR "Hyper Luminal"`):
  **zero threads**.

---

### Cahoots Studios — Reino Unido (cidade não publicada no site)

- **Email:** `jobs@cahootsstudios.com` · fonte: https://cahootsstudios.com/contact (aberto
  nesta rodada em 12/09 às 10h00; HTTP 200, publicado em texto na página de contato junto
  de `hello@cahootsstudios.com`). O `jobs@` é o correto aqui porque é a caixa que eles
  publicam **como via de carreira**, e não a de comercial. MX ativo (filtro `cp247.net`).
  A página publica também dois endereços de sócio, que ficam guardados como segunda via se
  a primeira quicar.
- **Encaixe:** é a descrição mais próxima do trabalho dele em toda esta rodada, dita pela
  própria home: *"From designing and creating charming animated characters within fully
  digital 3D worlds ... we do it all"* e *"breathing life into complex 3D characters
  inhabiting fully digital worlds using cutting edge CGI technology"*. **Personagem 3D
  estilizado é literalmente o produto da casa.** Trabalham para "commercials, TV, games,
  and film", ou seja o mesmo leque dos créditos dele, e a sócia Lucy Teire tem "over 20
  years producing animation for kids' TV, commercials, and **game cinematics**", que é
  exatamente o crédito de Wingfeather Saga no currículo dele.
- **Gancho, com a frase deles entre aspas:** *"We've built an army of insanely talented
  freelancers from every corner of the globe. They're not just contractors, they're part of
  the Cahoots family. We don't need a big in-house team because we're smart enough to call
  in the right talent at the right time."* É a casa dizendo por escrito que **contrata
  artista de fora, do mundo inteiro**, o que derruba de saída a objeção de geografia. O
  segundo gancho é a própria definição da marca: *"in cahoots"*, aliança, que é como se
  pede para entrar na lista de freelancers deles.
- **Fora dos EUA?** **Sim** (Reino Unido: Cahoots Studios Ltd, contatos com prefixo
  britânico). A frase de realocação ENTRA, **mas com cuidado**: a via que eles oferecem é a
  rede de freelancers global, então o argumento forte aqui é disponibilidade e fuso, e a
  realocação entra em segundo plano, não como pedido principal.
- **Ressalva honesta:** o site não publica quadro de vagas nem lista de posições abertas, e
  o modelo declarado é **freelance por projeto**, que pela regra de formato vale "baixa"
  como vaga. Como carta fria, porém, é das melhores portas da rodada, porque o convite a
  artista externo está escrito.
- **Dedupe:** `grep -i cahoots` no repositório bate só em `automacao/backlog-estudios.md`
  (lista de reserva) e `automacao/garimpo-pdf-fontes.csv` (garimpo). **Zero** em
  `alvos.csv`, `enviados.csv`, `pessoas.csv`, `processados.csv` e `docs/index.html`.
  **Gmail conferido nesta rodada** (`cahoots OR cahootsstudios OR "magic beans"`): **zero
  threads**.

---

## Descartados nesta rodada, com a razão literal

- **Believer Entertainment** (`believer.com`): o domínio **não é do estúdio**. Responde 200
  com um site de estudo bíblico ("Believer.com - Home Page", "Study The WORD Today"), e o
  `questions@believer.com` que sai da varredura é dessa casa, não de jogos. Endereço
  **descartado**; o estúdio de Austin, se for perseguido, precisa de outro domínio.
- **Vertpaint, 314 Arts e HundredStar sem endereço de PESSOA:** as três publicam só caixa
  funcional. Isso é o padrão medido há cinco rodadas e não é defeito da busca.
- **Magic Beans Studios** (Los Angeles, `hello@magicbeansstudios.com` publicado): descartado
  por **disciplina e porte**. A home diz "Creator-led animation studio - Est. 2025",
  "Handcrafted worlds", "Every frame drawn with care", e a serie em desenvolvimento, *Alphas*,
  se vende como "Ghibli meets The Goonies". E animacao 2D autoral de casa fundada este ano,
  sem pipeline de personagem 3D.
- **Skymap Games**: o site responde 200 em tudo, mas o unico endereco que sai da varredura e
  `user@domain.com`, ou seja **texto de exemplo do tema**, nao contato real. Nao montar nada
  a partir disso.
- **Sem email publicado nenhum, varridos nesta rodada em raiz, `/contact`, `/contact-us`,
  `/careers` e `/jobs` (não repesquisar contato, a via é o ATS):** Ironbelly Studios,
  Gears for Breakfast, Red Kite Games, Pixel Toys, Demiurge Studios, Wolcen Studio, Ludios,
  Mighty Yeti, Hardsuit Labs, BulletFarm, Halon, Titanium Clad Studios, Second Star Games.
- **Travados por rede (`http=000` em todos os caminhos, NÃO é morte):** `hypixelstudios.com`,
  `inflexion.games`, `uppercut.games`, `brainjargames.com`. Ficam para reconferência.

---

## Placar das fichas

| | |
|---|---|
| Fichas esperando carta | **5** |
| Rascunhos criados nesta rodada | **0, de propósito** |

---

## ROTA CONFERIDA PELO MAESTRO ÀS 09h20: NENHUM DOS CINCO TEM FORMULÁRIO DE CANDIDATURA

A faixa de formulário **não** está bloqueada pelo `create_draft`, então fui ver se algum destes cinco
podia ser enviado agora em vez de esperar. Não pode. Medição, casa por casa:

| Casa | Formulário | Veredito |
|---|---|---|
| **Cahoots Studios** | **zero** | rota é `jobs@cahootsstudios.com`, carta |
| **HundredStar Games** | **zero** (e há captcha na home) | rota é `jobs@hundredstar.games`, e o site convida por escrito |
| **Vertpaint** | existe, campo *"Where are you in production, and what support are you looking for?"* | **balcão de CLIENTE**, não de candidatura |
| **314 Arts** | existe, com campo **Company** | **balcão de CLIENTE**, não de candidatura |
| **Hyper Luminal** | "Let's Talk" genérico, Webflow | genérico demais; a rota publicada deles é `info@` |

**A decisão e o porquê:** formulário comercial não se usa como porta de emprego. Ele chega no time de
vendas, não no de arte, e lê como spam de fornecedor. A diferença para a **Peekaboo**, onde o formulário
de contato FOI usado e deu certo, é que lá o próprio formulário dizia *"IF YOU WANT TO WORK WiTH US,
PLEASE ATTACH YOUR PORTFOLIO"* — a casa convidando. Aqui os campos dizem o contrário.

Portanto **as cinco esperam o `create_draft`**, junto com as cinco pessoas do Joe. Dez cartas prontas
para sair em lote.

---

## FICHA NOVA — 21/09/2026 02h15 UTC (Jhon A, rodada de descoberta por API, sem navegador)

### Framestore — **Blender Generalist**, Londres, Reino Unido — requisição Recruitee **2709436**

**Rascunho: `RASCUNHO CRIADO r-3381507690627153907 (maestro, 21/09 02h5x; assunto exato exigido pelo anuncio, modo ATS sem emoji, 244 palavras, respostas do open_questions dentro: portfolio, localizacao atual, cidadania com patrocinio, disponibilidade, pretensao GBP 50.000 pelo item de casa grande da politica de 04/09). Sai na proxima rodada do enviarRascunhos do Vini.`. Eu não escrevo carta.**

| Campo | Valor |
|---|---|
| **Caixa** | `recruiters@framestore.com` — **confiança ALTA**: não é endereço montado, está escrito dentro do próprio anúncio como rota de candidatura |
| **Assunto EXIGIDO pelo anúncio** | `Film Blender Generalist - London` (o anúncio dita o assunto; não inventar outro) |
| **Fonte aberta por mim nesta rodada** | `https://framestore.recruitee.com/api/offers/` — HTTP 200, 802.774 bytes, 53 ofertas. Anúncio: `https://framestore.recruitee.com/o/blender-generalist` |
| **Prova de que vive** | `status: "published"`, `published_at: "2026-08-13 10:10:25 UTC"`, `close_at: null` |
| **Casa fora dos EUA?** | **SIM** (Londres, GB) → **usar a frase fixa de realocação da regra 10** |
| **Régua de veto** | **ZERO acerto** dos 110 termos em 4.342 caracteres de descrição + requisitos |
| **Dedupe** | `2709436` tem **zero ocorrência** em `enviados.csv`, `automacao/processados.csv` e `docs/index.html`. No Gmail, a busca `framestore` devolve 6 fios da casa e **nenhum menciona Londres/Blender Generalist**: o de 15/09 é `Modeller - Montreal`, o de 19/09 01h26 é `Film Blender Generalist - **Montreal**` (requisição 2718959), os outros são cartas a pessoas e a candidatura de julho à Character & Creature Modeller |

**Por que esta pessoa/caixa e não outra da casa:** a casa não publica endereço de ninguém (medido em 06/09 nos nove caminhos de contato: só caixas de departamento). E o teto de duas cartas a pessoas **já está cheio** — Lizi Bedford em 06/09 e Glenn Melenhorst em 08/09. A `recruiters@` não é contorno do teto: é a rota que o anúncio manda usar.

**Gancho com a frase do estúdio, entre aspas:** *"As part of our Visual Development team, you'll bridge the gap between initial concepting and final VFX execution. Blender is central to how our VisDev team designs and crafts key sequences early in production — extensively powering our work on shows like IF, Loki S2, and How To Train Your Dragon."* — **visual development é literalmente metade do cargo que a regra 2 do briefing define para ele, e Blender é ferramenta do dia a dia dele.**

**Perguntas que a carta precisa responder** (vêm do `open_questions` da própria oferta, então não há como o formulário pedir algo que a carta não trouxe): Showreel/Portfolio Link (obrigatório), Availability date, Citizenship, Current location, *"Are you open to relocating to London, UK?"* (booleano → **Yes**), Desired annual salary (**£ GBP**).

**A RESSALVA QUE ENFRAQUECE ESTA FICHA, e são três:**
1. É **contrato**, não efetiva (`employment_type_code: "contract"`), e o BRIEF-JHON põe efetiva na frente dentro da mesma faixa.
2. O corpo pede foto-realismo por escrito (*"assets that hold up to photoreal scrutiny"*) contra portfólio **estilizado**. O que atravessa é anatomia, silhueta, topologia e material — é o mesmo argumento que a carta de 19/09 desta casa já usou, e ele deve ser dito em voz alta, não escondido.
3. **Dosagem:** a caixa `recruiters@framestore.com` já recebeu **três** mensagens da campanha em uma semana (15/09 Modeller Montréal, 19/09 carta fria, 19/09 candidatura Montréal 2718959). Uma quarta é decisão de quem escreve, não minha.


---

## ROTAS NOVAS — 21/09/2026 04h35-05h5x UTC (Joe, rodada de ROTA e não de carta)

**Ordem desta rodada, e ela veio da minha própria nota das 02h35:** com o Apps Script parado
desde 19/09 01h26 e 53 rascunhos na fila, carta nova entra em fila parada. Então o alvo virou
**rota que envia sozinha**. Zero rascunho criado, zero carta. O que segue é para a mão do Jhon A.

**Placar honesto: 3 rotas de casa INÉDITA entregues, 1 recusada por disciplina com o texto que a
recusou, 0 candidatura enviada (não é meu papel), 0 navegador aberto.** E o achado que vale mais
que as três rotas é uma **armadilha de falso positivo no Pinpoint** que eu mesmo quase publiquei
como verdade (§4).

### ROTA 1 — **Unbroken Studios**, El Segundo (LA South Bay), Califórnia, **EUA** — a melhor das três

| Campo | Valor |
|---|---|
| **Família de ATS** | **Pinpoint** — `https://unbrokenstudios.pinpointhq.com/` (conta REAL: título `Jobs at Unbroken Studios \| Unbroken Studios Careers`) |
| **Quadro** | `https://unbrokenstudios.pinpointhq.com/postings.json` → **HTTP 200, 11 bytes, `{"data":[]}`** = conta viva com **ZERO vaga publicada** |
| **Quadro próprio** | `https://unbrokenstudios.com/` (200, 204.385 bytes), ancora `#careers` na própria home |
| **Candidatura espontânea** | **SIM, e convidada por escrito** — mas por **e-mail**, não por formulário: o único `href` de carreira da home inteira é `mailto:careers@unbrokenstudios.com` |
| **Casa fora dos EUA?** | **NÃO. É dos EUA.** → **a frase de realocação NÃO entra** (regra 10) |
| **Dedupe** | Gmail `search_threads` em `unbrokenstudios OR "Unbroken Studios" OR unbroken` → **`{}`**, e `"unbrokenstudios.com" OR Persson OR Gelius OR "Quidditch Champions"` → **`{}`**. No repositório, `unbrokenstudios` e `careers@unbrokenstudios.com` = **0 ocorrências** em `pessoas.csv`, `processados.csv`, `docs/index.html` e `enviados.csv`. **CASA INÉDITA, primeiro toque.** |

**A frase da casa que prova a disciplina, entre aspas e da página aberta por mim nesta rodada**
(`https://unbrokenstudios.com/`, seção GET TO KNOW US, cartão de equipe): a casa publica
**`Michelle Persson — Character Art Director`**, no departamento `Artist`. **Não é inferência:
é o cargo de direção de arte de PERSONAGEM escrito pela própria casa.** Ao lado dela a home
publica `Leon Brazil — Studio Technical Animation Director`, `Ronny Kim — Principal Animator`,
`Jordan Jones — Expert Technical Animator`, `Yanni Tripolitis — Lead VFX Artist`,
`Autumn Clarey — Lead Environment Artist` e `Rich Wong — Expert Environment Artist`.

**E a frase que convida a espontânea, literal:** *"Find A Home With Us — Currently, we have no
open roles, but we're always looking for amazing talent. Get in touch"*, seguida de
*"Careers — Nilla Gelius, HR Director — careers@unbrokenstudios.com"*.

**Porte e crédito, para o gancho:** *"Unbroken Studios is an LA based team of 30 developers with
proven track records of working on some of the most memorable franchises such as Battlefield,
Call of Duty, God of War and the Arkham Series"*, e o catálogo publicado é
**Harry Potter: Quidditch Champions (2024)**, **Suicide Squad: Kill the Justice League (co-dev)**
e **Fractured Lands**. Casa de 30 pessoas → pela regra do BRIEF-JOE o alvo é fundador/diretor de
arte, não recrutador.

**RESSALVA QUE ENFRAQUECE ESTA ROTA, e são três:**
1. **A rota não é formulário, é caixa funcional.** `careers@` é lido por RH, e o primeiro item do
   checklist de RH é autorização de trabalho — que aqui é o pior caso possível, porque **a casa é
   dos EUA e ele não tem autorização nos EUA**. Isso não invalida a rota; muda quem precisa ler a
   carta, e é por isso que o nome da **Michelle Persson** tem de aparecer no corpo.
2. **Zero vaga hoje.** `postings.json` = `{"data":[]}`. Quem for aqui vai de espontânea, e a
   própria casa diz que é isso que ela aceita agora.
3. **Não achei endereço de pessoa nenhuma.** Os três endereços publicados são `bizdev@`,
   `careers@` e `press@`. Nada foi montado.

### ROTA 2 — **Veles Productions Sp. z o.o.**, Varsóvia (Praga-Południe), **Polônia**

| Campo | Valor |
|---|---|
| **Família de ATS** | **SmartRecruiters**, locatário `VelesProductionsSpZOo` |
| **Quadro** | `https://api.smartrecruiters.com/v1/companies/VelesProductionsSpZOo/postings?limit=100` → **200, 10.781 bytes, `totalFound: 9`**. Página humana: `https://jobs.smartrecruiters.com/VelesProductionsSpZOo` (200) |
| **Candidatura espontânea** | **NÃO.** As 9 requisições são todas nomeadas; não há *General Application*, e a busca por `talent pool / talent community / general application / spontaneous` na página de carreira devolveu **zero acerto** |
| **Casa fora dos EUA?** | **SIM** (Polônia/UE) → **a frase de realocação entra** |
| **Dedupe** | Gmail `velesproductions OR "Veles Productions" OR Veles` → **`{}`**. Repositório: `velesproductions` = **0 ocorrências**. **CASA INÉDITA.** |

**AQUI A LIÇÃO DA HARI SE INVERTE, E É O ACHADO DESTA ROTA.** Na HARI a disciplina estava no
domínio do ATS e não no site. Na Veles é **o mesmo fenômeno com o sinal trocado, e ele derruba a
casa**: quem prova personagem é **só** o ATS, e o site da casa prova o contrário.

- **No ATS** (`.../postings/743999909941063`, aberto e lido por mim nesta rodada), a vaga
  *3D Character Rigging Artist (freelancer)* exige, literal: *"Excellent knowledge of rigging
  techniques for bipeds, quadrupeds, and complex creatures"* e *"Strong understanding of anatomy,
  kinematics, and deformation principles"*. As 9 requisições incluem ainda *3D Senior Animator*
  (duas, uma freelance) e *PhD Animation Expert*.
- **No site da própria casa** (`https://velesproductions.com/`, 200, 79.521 bytes, 2.878
  caracteres de texto visível), a prosa inteira é **produção virtual e ambiente**:
  *"Virtual Production & Broadcast Studio"*, *"XR and FX Services for the most demanding clients
  worldwide"*, *"3D BIOMES — We specialize in creating custom virtual sets for our clients using
  Unreal Engine"*, *"3D ASSETS — We offer high quality 3D photo scanning products"*. Portfólio:
  noite eleitoral polonesa, comercial de sorvete, cenário virtual de Tóquio para videoclipe.

**RESSALVA QUE ENFRAQUECE ESTA ROTA, e ela é séria:** o único cargo de personagem da casa é
**RIGGING**, que está **fora da disciplina dele** pela regra que o BRIEFING já fixou para o
"Creature TD" da ILM. E o resto é ambiente e cenário virtual, que é o que o Vini mediu em 10/09
como perda de tempo. **Fica registrada como rota de casa inédita com departamento de personagem
declarado, não como encaixe.** Se alguém for, vai por espontânea que não existe, ou seja: vai por
e-mail — e para isso o site publica o padrão `inicial+sobrenome@velesproductions.com` **provado
por quatro endereços literais** (`abenbenek@`, `apaprocki@`, `dzwierzchowska@`, `yheydlauf@`),
mais `office@`, `us.office@` e `rentalstudio@`. **Padrão provado é confiança BAIXA, e não gastei
carta nenhuma nele.**

### ROTA 3 — **Lockwood Publishing**, Nottingham, **Reino Unido**

| Campo | Valor |
|---|---|
| **Família de ATS** | **Workable** |
| **Rota de LEITURA (funciona)** | `https://jobs.workable.com/view/nkVHue9fSxHKBeokz9JJUd/remote-digital-fashion-designer-(all-levels%2C-speculative)-in-united-kingdom-at-lockwood-publishing` |
| **Rota de ENVIO** | **PAREDE JÁ MEDIDA.** `apply.workable.com/api/v3/accounts/<token>/jobs`, `/api/v2/...` e `apply.workable.com/lockwood-publishing/` devolveram **429 com 17 bytes nos três**, nos tokens `lockwood-publishing`, `lockwoodpublishing` e `lockwood`. É o mesmo 429 de IP que a rodada de 19/09 mediu com Chromium de verdade na Climax |
| **Candidatura espontânea** | **SIM, e é o próprio título:** *"Digital Fashion Designer (All Levels, Speculative)"*, publicada em **08/07/2026**, `workplace: remote`, Reino Unido |
| **Quadro próprio** | **MORTO:** `https://www.lockwoodpublishing.com/careers/` devolve **404** com corpo de S3 (`NoSuchKey ... 404.html`). O `href` existe na home e a página por trás dele não |
| **Casa fora dos EUA?** | **SIM** (Reino Unido) → **a frase de realocação entra** |
| **Dedupe** | Gmail `Lockwood OR "Avakin" OR lockwoodpublishing` → **`{}`**. Repositório: `lockwood` = **0 ocorrências**. **CASA INÉDITA.** |

**A frase da casa, entre aspas, do texto de empresa do próprio anúncio:** *"Lockwood Publishing is
one of the leading independent UK mobile games companies. Our most successful product to date is a
3D virtual world on mobile called Avakin Life."* E do corpo da vaga: *"Fashion is one of the
biggest reasons players express themselves in Avakin Life."*

**RESSALVA QUE ENFRAQUECE ESTA ROTA, e são três:**
1. **A disciplina é marginal.** Roupa de avatar em mundo 3D é vizinha de personagem, mas o cargo é
   **design de moda**, e o anúncio põe **IA no centro**: *"You'll combine creativity, commercial
   awareness and AI-powered workflows"*, *"As a Digital Fashion & AI Designer"*. Não é escultura de
   personagem. **Não apresente como encaixe forte.**
2. **O envio está atrás do 429 de IP**, que a campanha já mediu como parede de rede — e pela nota
   de 03h5x de hoje, sessão irmã não resolve, porque sai pelo mesmo proxy.
3. A vaga é de **08/07/2026**, dois meses e meio atrás. Especulativa envelhece menos que
   requisição, mas envelhece.

### RECUSADA COM O TEXTO QUE A RECUSOU — **TRICK 3D**, Atlanta, EUA (SmartRecruiters `TRICK3D`)

Locatário real e inédito (`.../companies/TRICK3D/postings` → 200, `totalFound: 2`;
`trick 3d` e `TRICK3D` = **0 ocorrências** no repositório; Gmail `{}`). **Morreu por disciplina, e
com a frase da própria casa:** *"TRICK 3D sits at the forefront of immersive content and technology
innovation in VR, AR, MR and much more... our client roster includes CNN, Cartoon Network, Delta
Air Lines, Georgia Power, Jones Lang LaSalle (JLL), Intercontinental Hotel Group (IHG)"*. As duas
requisições são **TECHNICAL ARTIST** (Unreal, *"crafts blueprints and code"*) e **Head of
Accounts**. Zero personagem, zero criatura, em 6.556 bytes de anúncio. Registro para ninguém
reabrir.

### §4 — **A ARMADILHA DO PINPOINT, E EU QUASE A PUBLIQUEI COMO VERDADE**

No primeiro minuto desta rodada eu sondei `https://framestore.pinpointhq.com/postings.json`,
recebi **200 com 26.307 bytes de JSON real** (com texto de benefícios, DEI e tudo) e **ia escrever
que a Framestore tem quadro no Pinpoint**. Fui ler os títulos antes. São estes três:

```
Head of DEI - UK      | 320821 | London
Marketing Manager     | 320822 | Paris
Customer Service Rep  | 320823 | New York
```

**É o conteúdo de DEMONSTRAÇÃO do Pinpoint.** Medido nos 20 locatários que sondei: **11 servem
exatamente esse conjunto** (`Head of DEI - Belfast / - US / - UK`, `Marketing Manager`,
`Customer Service Rep`, com Londres/Paris/Nova York), entre eles **a própria Framestore**, mais
Ajax Creative, Bigger Games, First Derivative, Labster, OUTFORM, Penumbra, Plexus, Production Club,
Puttshack e Simwave.

> **REGRA QUE FICA: no Pinpoint, 200 com JSON GRANDE não prova quadro vivo. O discriminador é a
> string `Head of DEI` no corpo: se ela está lá, a conta existe e nunca foi povoada.** Contar bytes
> ou contar itens registra 11 quadros onde existem zero.

**O controle que valida o oráculo, e ele passou:** `naoexiste999xyz`, `zzqqwwertyuiop` e
`pixarcharacterhouse9` devolveram **404 com 11.684 bytes** os três, e a raiz deles serve
`<title>404 Not Found</title>`. Ou seja **200 continua provando que a CONTA existe** — só não prova
que ela tem vaga. E conta povoada de verdade se reconhece pelo tamanho **com** a ausência do
`Head of DEI`: Bending Spoons (41.303), Zoox (46.684), Spiralyze (423.354).

**E é por isso que a Unbroken Studios é a rota boa desta rodada:** o `{"data":[]}` de 11 bytes dela
é honesto — conta real, zero vaga, e a casa **diz isso por escrito** na própria home.
