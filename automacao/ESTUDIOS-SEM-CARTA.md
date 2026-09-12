# Estúdios APROVADOS que ainda esperam carta

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

## Placar das fichas

| | |
|---|---|
| Fichas esperando carta | **3** |
| Rascunhos criados nesta rodada | **0, de propósito** |
