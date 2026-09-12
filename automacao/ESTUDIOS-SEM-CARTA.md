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
