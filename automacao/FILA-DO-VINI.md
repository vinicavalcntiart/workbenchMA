# FILA DO VINI — 43 candidaturas VIVAS (revalidada uma a uma na fonte oficial em 08/09 à noite)

## 🖱️ A FILA DE CLIQUES AGORA VEM COM O TEXTO ESCRITO — https://claude.ai/artifact/QcAt1Ym3zeCWZM764LLq9N

**Cobrança dele em 16/09, e ela estava certa:** *"nessa fila de cliques n tem as cartas de
recomendacoes e bio (texto) especificas pra cada estudio"*. A página tinha os endereços e o
dossiê campo a campo, mas não o texto. Agora cada porta abre em três blocos com botão de copiar:
**carta escrita para aquela vaga**, **bio de "tell us about yourself"** e **resumo de uma linha**.

### 🟠 ATUALIZADO 21/09 02h5x UTC (Mágico) — **ALERTA DE VAGA DA MICROSOFT / XBOX GAME STUDIOS**: a barreira de área foi resolvida, mas apareceu uma NOVA e ela não é captcha

`https://careers.microsoft.com/careers/join?domain=microsoft.com` ← Cobre 343 (Halo), The Coalition, Rare, Obsidian, inXile, Double Fine, Playground, Turn 10, Mojang, ZeniMax e Bethesda, e a campanha nunca teve alerta nenhum desse grupo.

**O que mudou:** o campo "Desired area of work" (que travava a rodada de 20/09) foi resolvido —
é um react-select v1 que abre por mousedown e "Design & Creative" é escolhido e gravado
corretamente, confirmado na tela. Não é mais parede.

**O que apareceu no lugar, medido em CINCO tentativas reais de envio (não é palpite):** o clique
em "Join Talent Network" sempre dispara o POST real (`/api/apply/v2/resume?domain=microsoft.com&
source=talentnetwork`), mas o servidor devolve, sempre, `HTTP 400` com o corpo literal
`{"message": "Please try again"}`. Nas cinco tentativas testei formas diferentes de marcar a
caixa obrigatória "I agree to receive electronic communication..." (clique no ícone visível,
clique real no input escondido, clique via label, tecla Espaço, combinação de todas) e CONFIRMEI
por leitura do corpo real enviado (`postData()`, não a leitura de volta da tela) que o campo
`notifications_checkbox_accepted` do formulário sai **sempre `false`** no POST, mesmo quando o
ícone mostra marcado e o `<input>` real mostra `checked:true` no DOM. Ou seja: a marcação visual
não é a mesma coisa que o estado que o formulário de fato envia — parece bug de sincronização
da própria página da Microsoft/Eightfold, não campo obrigatório esquecido por nós.

**Por que isto pode ser rate-limit e não bug de checkbox:** as cinco tentativas foram todas com a
mesma identidade (mesmo CV, candidato reconhecido pelo servidor como `enc_id R3AV9MGO6b8`) em
menos de 20 minutos. O erro genérico "Please try again", idêntico em todas as tentativas
independente do estado real da caixa, é a assinatura clássica de bloqueio anti-abuso, não de
validação de campo. Zero captcha, zero desafio de imagem, zero Turnstile: o reCAPTCHA v3
invisível da página RODA sozinho e devolve token (`rresp`) sem pedir nada visível — não há
desafio interativo aqui, então este item **não se qualifica** para "prova de desafio interativo".

**Recomendação para reabrir:** esperar pelo menos algumas horas (o bloqueio, se for por IP/
identidade, deve resetar) e tentar UMA VEZ pelo navegador do Vini (rede e sessão diferentes das
nossas, tal como a família Ashby). Passos: abrir a URL, anexar o CV, escolher a área de trabalho
mais próxima de Art/Design (aparece como **"Design & Creative"** na lista), marcar a caixa de
consentimento e clicar em **Join Talent Network** (o botão do formulário, não o link do menu, que
só reabre a página numa aba nova sem POST nenhum). Controle: um e-mail de `microsoft.com` ou
`eightfold.ai` na caixa confirma.

### 🔴 ENTROU EM 20/09 05h40 UTC (Jhon A, rodada 04h15) — **ONZE PORTAS DE ASHBY ABREM DO SEU NAVEGADOR SEM CAPTCHA NENHUM**, e o rótulo "reCAPTCHA invisível" que as segurava desde 11/09 estava ERRADO

**O que foi medido hoje, com clique:** o Ashby não pede desafio. Ele recusa **por reputação do IP** da
sessão e escreve o motivo na tela: *"Your application submission was flagged as possible spam"* e
*"Turn off your VPN or proxy"*. Do seu computador, com a sua rede, ele aceita: as três candidaturas
de Ashby que a campanha já tem (thatgamecompany, redlygames, stellarentertainment) saíram exatamente
assim, pela sua mão.

**As onze portas, todas sem veto escrito, formulário curto (nome, e-mail, CV, LinkedIn, portfólio):**

| Casa | Quadro | Nota |
|---|---|---|
| Redly Games (Finlândia, remoto global, EU/Canadá preferidos) | https://jobs.ashbyhq.com/redlygames/3c2a1d1e-5e80-4b4e-895d-f43d0efe4d3b/application | General Interest, a que foi clicada hoje |
| ArenaNet (Bellevue, EUA) | https://jobs.ashbyhq.com/arenanet | abra o quadro e escolha a de personagem ou a espontânea |
| Chromatic | https://jobs.ashbyhq.com/chromatic | idem |
| Colonist | https://jobs.ashbyhq.com/colonist | idem |
| Interplay | https://jobs.ashbyhq.com/interplay | idem |
| Stellar Entertainment (Reino Unido) | https://jobs.ashbyhq.com/stellarentertainment | segunda requisição da casa, se houver de personagem |
| Vizcom | https://jobs.ashbyhq.com/vizcom | idem |
| Kolibri Games (Berlim) | https://jobs.ashbyhq.com/kolibrigames | idem |
| Immutable (Sydney) | https://jobs.ashbyhq.com/immutable | idem |
| Jito | https://jobs.ashbyhq.com/jito | idem |
| Daily Wire (Nashville) | https://jobs.ashbyhq.com/dailywire | animação própria (Bentkey); espontânea |

Texto para o campo de carta: o mesmo bloco ATS da fila de cliques (sem emoji). Autorização de
trabalho sempre com a verdade.

> **CORREÇÃO DE 21/09 11h4x UTC (Mágico): a tabela acima promete mais do que existe, e eu medi as
> onze uma a uma.** Pela API pública da plataforma e, onde ela dá 404, pela API interna do próprio
> quadro: **`kolibrigames`, `immutable` e `dailywire` devolvem `jobBoard: null`** — não existe
> quadro nesses três endereços; **`jito` só responde como `jito-labs`** e são quatro vagas de cripto
> nos EUA; **`interplay` não é a Interplay dos jogos**, é um *venture studio* de Nova York (Bowery
> Legal, Vandrel, Lykos: advogado de M&A, engenheiro mecânico, sócio de private equity), 18 anúncios
> e zero de arte; **`arenanet` General Applications já foi enviada em 30/08** (recibo do Ashby no
> Gmail) e a outra vaga da casa é de engenharia; **`stellarentertainment` já tem candidatura** e hoje
> só tem Talent Pool e engenharia; **`chromatic`** é ferramenta de desenvolvedor e **`vizcom`** é
> ferramenta de IA de desenho, as duas sem nada de personagem; e o **`colonist`** só tem *UI Artist*
> (com "AI first-mindset") e um *Talent Pool* cujos campos obrigatórios pedem o **perfil dele no
> colonist.io**, um **quiz sobre o produto** e duas respostas livres, uma delas com a instrução
> escrita *"Please don't use AI. We appreciate a genuine answer."* **Resultado: das onze, zero vaga
> da disciplina dele hoje.** Não gaste clique aqui; a reputação de IP do Ashby nem chegou a ser o
> problema.

### 🔴 REVALIDADA EM 20/09 05h40 UTC — **Character Artist – Hair Specialist**, **Keywords Studios / Lakshya Digital**, remoto (Canadá, EUA, Reino Unido): a régua de 82 termos dá **ZERO acerto** no anúncio inteiro

`https://apply.workable.com/keywords-intl1/j/CA33DB1208/` ← **ABRA ESTA do seu navegador.**

A decisão antiga de "exige residência" apoiava-se na linha *Location: Canada, US, UK*, que é lista de
local e **não** veto escrito. O que bloqueia a automação é só a parede do Workable (Turnstile de
plataforma, recusa deste IP). Do seu navegador o Workable passa. É a **única vaga só de grooming de
personagem** que a campanha já viu. Requisições vivas hoje: `9b90b38f` e `be8477ea` (Canadá e Reino
Unido). Se ao abrir a página disser "expired", registre e siga.

### 🟡 DOIS LINKS DO SEU PDF ("Links Jobs - Rodrigo.pdf") SÓ ABREM LOGADO — custo de um minuto

1. `tinyurl.com/mapOfStudios` → Google My Maps em modo de edição, pede login. Se você abrir logado e
   exportar o KML (menu ⋮ → "Exportar para KML/KMZ"), mande o arquivo; eu varro as casas.
2. `tinyurl.com/Animation-VFX-Game-job-studios` → planilha do Google não compartilhada com a conta
   da campanha (`export?format=csv` dá 401). Compartilhe com contact@vinicavalcanti.art como leitor,
   ou baixe o CSV e mande. Até lá a fonte fica como **não lida**, não como "sem resultado".

### 🔴 ENTROU EM 19/09 20h40 UTC (Jhon A, 35o turno) — **Character Sculptor, Adult Series**, **ICON CREATIVE STUDIO**, **VANCOUVER, BC**: a melhor porta de personagem do estoque, e a parede foi medida COM CLIQUE pela **terceira vez** hoje. Você só marca a caixa do reCAPTCHA

`https://iconcreative.bamboohr.com/careers/150` ← **ABRA ESTA. Clique em "Apply for This Job".**

**Por que é você e não a automação, em uma frase:** ao clicar em *Submit Application* o BambooHR
**injeta** um reCAPTCHA v2 **de caixa de marcar** e nada sai — não é campo faltando, não é POST
recusado, é porteiro humano, e caixa de desafio não se burla.

**A medição de hoje, 20h30 UTC, com o navegador de verdade e os dois passos separados:**

| Passo | O que o servidor e o DOM devolveram |
|---|---|
| Ensaio (sem enviar) | 14 campos e as 9 perguntas preenchidos; CV anexado com `attachTemporary.php` **200** (`errorType: ok`, 45.459 B); **zero** obrigatório vazio; leitura de volta campo a campo conferindo |
| Envio (com `--submit`) | botão `BUTTON`, **`disabled=false`**, clicado por coordenada; `erros: []` (**nenhuma** validação reclamou); `g-recaptcha-response` = **VAZIO**; iframes `recaptcha/api2/anchor` com **`size=normal`** e `recaptcha/api2/bframe` **presentes**; **nenhum POST de candidatura saiu**; a página voltou ao formulário **ainda cheio** |
| Controle no Gmail | `from:bamboohr newer_than:1d` = **zero email**. Ou seja não é falso negativo: a candidatura realmente **não** chegou |

`size=normal` **com** `bframe` presente é a assinatura de caixa de desafio que o `BRIEF-JHON`
manda condenar sem gastar rodada. É a **terceira** medição com clique neste mesmo quadro (06/09,
18/09 às 00h44 e hoje), e as três deram o mesmo resultado.

**Por que a vaga vale, com as frases do anúncio:** é **escultura de personagem**, o centro exato
dele, e não disciplina vizinha — *"Sculpt high-quality stylized characters from concept artwork"*,
*"Advanced proficiency in ZBrush"*, *"Strong understanding of human anatomy, facial anatomy,
proportion, gesture, silhouette"*, e o anúncio diz que o sculpt tem de servir a jusante para
*"topology, rigging, deformation, grooming, surfacing, and animation requirements"* — modelagem,
texturização e groom, os três que ele tem. A casa é a maior de animação CG independente do Canadá,
em Gastown, entregando para Netflix, Disney+, Apple TV+, Amazon, Peacock e Paramount+.

**FAIXA PUBLICADA: CAD 57.372,12 a 80.730,00**, e o próprio anúncio explica que é o piso do acordo
coletivo pela lei de transparência salarial da BC (*"the wage displayed reflects the minimum rate
established under ICON's collective agreement. Additional compensation may be considered based on
experience"*), ou seja há negociação acima disso.

**O MELHOR SINAL DE VISTO DO ESTOQUE, e ele está nas OPÇÕES de um campo obrigatório:** a pergunta
`1528` *"Are you eligible to work in Canada? Please specify your status"* tem quatro opções e a
quarta é **"I need a work permit"** (`option id 449`). A casa **oferece** a resposta honesta dele
em vez de barrar na porta. Some-se que eles mantêm um **RCIC Immigration Coordinator** aberto no
mesmo quadro, e a frase do anúncio *"a diverse team of artists from around the globe who have
joined us here in British Columbia"*.

**RÉGUA DE VETO: ZERO VETO DE TEXTO**, e refeita hoje com a régua corrigida. Cuidado de método que
vale para todo BambooHR: na PÁGINA a régua lê **8 caracteres** (o quadro é SPA) e isso é leitura
inválida, não zero. Refeita em `/careers/150/detail`, **7.393 caracteres**, e os acertos são todos
falsos positivos de estrutura: `located in` vem de *"located in the historic Gastown district"*,
`proficiency in` de *"Advanced proficiency in ZBrush"*, e `british columbia` das duas frases de
benefício e da lei de transparência salarial.

**DEDUPE, os quatro arquivos e o Gmail:** a requisição **150 é inédita** (zero ocorrência em
`enviados.csv`, `processados.csv`, `docs/index.html` e nesta fila) e não existe nenhuma linha com
"Character Sculptor". A **casa** é conhecida e isso não atrapalha: a candidatura de 31/08 foi para
a **136**, *Intermediate Modeling/Texture Artist*, outra requisição e outro nível (recibo de
`notifications@app.bamboohr.com` nomeando o cargo, thread `1a059489a283190b`), e há carta fria de
08/09 para `carson@iconcreativestudio.com`. **A 150 é escultura de personagem; a 136 era modelagem
intermediária.** Não é reenvio.

**O QUE DIGITAR, campo por campo (2 minutos).** Endereço, cidade, província, CEP e telefone saem do
documento privado do Drive *"CAMPANHA - dados pessoais dos formulários"* e **não** entram aqui.

- **Country:** `Brazil` · **Date Available:** `2026-11-01`
- **Website, Blog or Portfolio:** `https://www.artstation.com/viniciuscavalcanti`
- **LinkedIn:** `https://www.linkedin.com/in/vinicavalcnti/`
- **Desired Pay:** `CAD 78,000 - 80,000 (open to your band)`
- `1531` confortável trabalhando presencial em tempo integral → **Yes**
- `1533` está atualmente no Canadá → **No**
- `1529` está ou aceita realocar para a British Columbia → **Yes**
- `1530` amigos ou família na ICON → **No**
- `1528` elegibilidade → **I need a work permit**
- `1532` senha do reel → deixar vazio (o portfólio é público)
- `1534` quando expira o work permit → não se aplica

**TEXTO PARA COLAR em `1526` (pretensão, obrigatória):**

> Open to aligning with your posted range for the role; as a reference, I am looking at around
> CAD 78,000 to 80,000, at the upper end of the listed band, given ten-plus years on stylized
> characters and five as Senior. I am ready to move for the role.

**TEXTO PARA COLAR em `1527` ("anything else", opcional mas é onde o caso de visto entra):**

> Senior 3D Character Artist with more than ten years in stylized characters: sculpt in ZBrush from
> 2D concept, retopology built for rigging and deformation, texturing in Substance and Mari, and
> grooming in Houdini — the exact downstream chain your posting names. Credits include The
> Wingfeather Saga and Endstar. I am ready to move for the role and to be on site in Vancouver full
> time. On status I am direct: I am not authorized to work in Canada and would need a work permit,
> which is why I picked that option above rather than a softer one. My academic background, with an
> honors laurea, a postgraduate specialization, a master's in progress, IELTS and publications,
> makes a strong visa case.

**ARMADILHA JÁ CATALOGADA NESTE QUADRO:** existe um honeypot chamado `nickname_hpcsaf` com o rótulo
*"Please leave this field blank"*. **Deixe em branco** — se preenchido, a candidatura é descartada
em silêncio.

**Custo de não fazer:** é a porta de personagem com melhor sinal de visto do estoque, em Vancouver,
que é a sua prioridade número um, publicada em 17/09. O arquivo de respostas já está pronto fora do
repositório em `/home/user/apply/ans_iconcreative150.json`.

### 🔴 ENTROU EM 19/09 16h30 UTC (Jhon A, 33o turno) — **3D Character Modeler**, **INFOLD GAMES** (Papergames, casa de *Infinity Nikki*), **Los Angeles + Singapura**: personagem por título E por corpo, **zero veto**, casa 100% inédita, e a porta é **login por código de SMS** que só o seu celular recebe

`https://career.infoldgames.com/EN/job/7639286868983384370` ← **ABRA ESTA. É UM CLIQUE: "Continue with Google".**
`https://career.papegames.com/EN/position/7639286868983384370/detail` ← a que você me mandou (mesma vaga, porta de SMS)
`https://www.linkedin.com/jobs/view/3d-character-modeler-at-infold-games-4413879564` (o anúncio do seu print)

**Por que é você e não a automação, em uma frase:** a candidatura exige **conta**, e as duas portas
da casa pedem coisa que eu não tenho — a de Singapura pede **código por SMS no celular** e a de LA
pede **login do Google ou do LinkedIn**, que são as suas contas pessoais e eu não entro nelas.
Não é captcha: não existe reCAPTCHA, hCaptcha, Turnstile nem DataDome em nenhuma das duas telas.

> **ATUALIZAÇÃO DE 21/09 11h25 UTC (Mágico, rodada 3): o formulário já está preenchido até a última
> linha e a única coisa que falta é o seu clique no Google.** Eu reabri a porta e ela abriu mais do
> que estava escrito: o endereço `career.infoldgames.com/EN/apply/7639286868983384370` **renderiza o
> formulário inteiro sem conta**, e eu o preenchi todo (nome, telefone +55, e-mail, LinkedIn, as
> **duas** cidades pretendidas, patrocínio de visto = *Yes*, formação, três empregos com mês e ano do
> seu CV, e o ArtStation como amostra) — **a validação da própria casa passou com zero erro** e o
> modal *"Email Verification"* abriu. O que trava é o **servidor**, e agora com o texto dele na mão:
> o upload do currículo responde `{"msg":"failed","ret":1803001}` ("Upload failed") em seis
> tentativas, e o pedido do código por e-mail responde `ret -702` com
> `action_11413 code 400 "request specified an invalid argument"`. Com um token de sessão **falso** o
> erro **muda**, o que prova que a ação lê a sessão: **a casa só manda o código para candidato
> logado**. Então: **entre uma vez com o Google nessa página** e me avise — o
> `apply_infold.js envia` fecha o resto sozinho. Se preferir não entrar, a outra rota é carta por
> e-mail para **`careers@infoldgames.com`**, que é o endereço publicado pela própria casa na seção 9
> do Privacy Statement do site de recrutamento, e essa é para o agente de carta.

**A DESCOBERTA QUE FAZ VALER O CLIQUE: a mesma requisição tem DUAS portas diferentes, e uma é muito
mais barata que a outra.** Medi as duas hoje:

| Porta | Login que ela exige | Custo para você |
|---|---|---|
| **`career.infoldgames.com`** | **Continue with Google** ou **Continue with LinkedIn**, e nada mais (não tem campo de telefone) | **um clique**, você já está logado no Google |
| `career.papegames.com` (a do seu link) | **só** número de celular + código por SMS, mais Douyin como terceiro | uns dois minutos, e cria conta sozinho |

**As duas servem a MESMA vaga** (o id do anúncio é o mesmo nos dois, `7639286868983384370`), então
escolha a do Google. **Se preferir a do seu link:** o seletor de país abre com **+65** (Singapura),
tem **229 códigos** e **+55 Brazil está lá** — troque o código, ponha seu número, clique em
*Get code*, digite o código do SMS e marque *I have read and agree to the Privacy Statement*.
A tela avisa que *"An account will be created upon mobile number verification"*, ou seja não
precisa criar conta antes. Depois do login ele cai direto em `/resume/7639286868983384370/apply`.

**O LinkedIn NÃO resolve:** o anúncio é **offsite apply** (10 ocorrências de `offsite` no HTML de
convidado, **zero** de *easy apply*), então o botão dele te joga numa dessas duas portas de
qualquer jeito. Não há atalho ali.

**Por que a vaga vale, com as frases do anúncio:** é **personagem puro**, o que a regra de 10/09
manda priorizar. *"Responsible for the high-fidelity facial modeling of main characters
(protagonists, key NPCs), covering the entire pipeline including high-poly sculpting, topology
optimization, UV unwrapping, and low-poly modeling"*; *"Create cinematic-level facial texture
assets, including a full set of PBR textures such as Albedo, Normal, Roughness, and SSS Mask"*;
*"Mentor character modelers within the team"*. Pede **ZBrush, Maya/3ds Max, Substance Painter/Mari
e UE5**, que é o núcleo dele, e o departamento é o **Z1 Studio** da casa.

**Régua de veto: ZERO acerto dos 43 termos** em **2.402 caracteres** do corpo lido pela API oficial
(`career.papegames.com/api/v1/job/posts/7639286868983384370`), acima do piso de leitura válida.
Zero `authorized to work`, zero `visa`, zero `sponsor`, zero `work permit`, zero `based in`, zero
`relocation`, zero exigência de idioma. **E as duas cidades estão no escopo da campanha:** Los
Angeles é EUA e **Singapura é uma das duas exceções da Ásia** na regra 5.

**Dedupe, completo:** `dedupe-agora.sh A167711 "Infold Games"` deu **zero nas três seções**;
`grep -i infold` em `enviados.csv`, `automacao/processados.csv`, `docs/index.html` e nesta fila =
**zero** (a única ocorrência no repositório inteiro é `infoldgames.com` no `censo-wikidata.csv`, que
é censo e não candidatura); `garra.sh checa` = **livre**; e no **Gmail** a busca
`infold OR infoldgames OR papegames OR "Infinity Nikki"` devolveu **{} — nenhum fio, nenhum recibo**.
Casa 100% inédita na campanha. Greenhouse `infoldgames` e Lever `infold` dão 404, e é por isso que
nenhuma varredura de ATS tinha achado: **a casa usa Feishu/Lark Hire**, família que a campanha nunca
tinha visto (zero ocorrência de `feishu`, `lark`, `atsx` e `papegames` no `BRIEFING.md`).

**AS RESPOSTAS, com a verdade (iguais às do `respostas-formularios.md`):**

- Autorizado a trabalhar nos EUA: **No**. Autorizado em Singapura: **No**.
- Precisa de patrocínio de visto, agora ou no futuro: **Yes**.
- Disposto a realocar: **Yes**, para **Los Angeles** ou **Singapura**.
- Anos de experiência: **More than 10 years** (nas escalas fechadas, a faixa mais alta).
- Pretensão: o anúncio **não publica faixa**, e é casa grande nos EUA, então pela política de 04/09
  é **USD 100.000**, com a abertura *"Open to aligning with your band for the role; as a reference,
  I'm looking at around USD 100,000."* **Ressalva honesta: a política do briefing não tem número
  para Singapura**, então se o formulário perguntar em dólar de Singapura, prefira a frase de
  abertura sozinha a chutar um valor.
- Salário atual: *"Confidential under the NDA of my current contract; happy to discuss ranges
  during the process."*
- Disponibilidade: *"A standard transition period with my current studio; glad to align dates in
  the process."*
- Como ficou sabendo da vaga: **LinkedIn** (foi de onde ela veio de verdade, do seu print).
- Diversidade (idade, etnia, gênero): **Prefer not to say**.
- Anexos: `Vini_Cavalcanti_CV.pdf` e `Vini_Cavalcanti_Portfolio.pdf`.

**TEXTO PARA COLAR — carta / campo de "por que você" (231 palavras, sem emoji porque formulário é
registro e não conversa):**

```
Hi Infold Games team,

I'm a senior 3D character artist with over 10 years in stylized characters, and facial work is the part of the pipeline I care most about.

On The Wingfeather Saga at Angel Studios I modeled and hand-painted the season one characters, and at E-Line Media I have spent nearly five years taking hero characters from sculpt to engine: high-poly, retopology, UVs, bakes, PBR textures and LODs. That full-asset ownership is what I would bring to facial assets here, and grooming in Houdini is my extra edge on hair and fur.

My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it.

Being honest about fit: my published work is stylized rather than photoreal, and my facial experience sits inside character modeling rather than four years dedicated only to faces. The anatomy, the topology that has to survive animation, the PBR skin and the blendshape work are the same craft, and your posting asks for control between realistic and stylized directions, which is where I am strongest.

I am ready to move to Los Angeles or Singapore for the role. I am not a US or Singapore citizen, so I would need work authorization sponsorship.

Portfolio: https://www.artstation.com/viniciuscavalcanti
LinkedIn: https://www.linkedin.com/in/vinicavalcnti/
School: https://vinicavalcanti.com

Thanks for the read,
Vini Cavalcanti
```

**TEXTO PARA COLAR — bio de "tell us about yourself":**

```
Senior 3D character artist with over 10 years of experience, focused on stylized characters taken from sculpt all the way to engine. Credits include The Wingfeather Saga for Angel Studios and Endstar for E-Line Media, plus outsourcing work at PUGA Studios. I own the whole asset: high-poly sculpting, retopology, UVs, bakes, PBR texturing, LODs and engine integration, with grooming in Houdini as a specialty. I also teach and run my own art school, so mentoring and giving clear technical feedback are part of my daily work.
```

**TEXTO PARA COLAR — resumo de uma linha:**

```
Senior 3D character artist, 10+ years, stylized hero characters from sculpt to engine, grooming in Houdini; ready to relocate to Los Angeles or Singapore with visa sponsorship.
```

**AS RESSALVAS HONESTAS, e são três, porque esta é a parte que mais pesa contra:**

1. **A vaga é realismo facial, e o portfólio dele é estilizado.** Pede *"at least 4 years of
   in-depth experience specifically in facial modeling"*, *"deep understanding of human facial
   anatomy (bones, muscles, fat layers, and skin micro-details)"*, *"complete PBR textures for
   realistic skin"* e *"Familiar with MetaHuman or equivalent level facial asset production
   standards, with experience in creating BlendShape/FACS expression libraries"*. É a mesma
   ressalva de registro de estilo que a Wargaming e a Rising Sun já carregam. **O que segura a
   candidatura de pé é a última linha das qualificações**, e ela é a favor dele:
   *"with the ability to accurately control the temperament and expressiveness of character faces
   between highly realistic and stylized art directions"*.
2. **O anúncio do LinkedIn é de 1 dia, mas a requisição é de MAIO.** O `publish_time` da API é
   `1778660393058`, que é **13/05/2026**, e o `modify_time` é **14/07/2026**; o `datePosted` do
   LinkedIn é **18/09/2026 14h29 UTC**. Ou seja o que tem um dia é o **repost**, não a vaga. Ela
   segue **ativa** (`job_active_status: 1`, `channel_online_status: 0`, e a página responde 200),
   mas requisição de quatro meses parada é requisição fria.
3. **"Over 200 applicants"**, escrito na própria página do LinkedIn.

**E uma porta de e-mail que existe, para o maestro decidir, não para você:** a política de
privacidade da própria casa publica **`careers@infoldgames.com`** com esta frase —
*"you may contact us by sending an email to careers@infoldgames.com"* — no capítulo *9. Contact Us*
do documento de recrutamento. É caixa de recrutamento de verdade, mas ela está publicada como
contato de **privacidade/dados pessoais** dentro do recrutamento, e não como "mande seu CV aqui".
Fica registrada como rota secundária; **a rota boa é o formulário, e ele é um clique seu.**

### ✅ REVALIDADA HOJE ÀS 14h50 (19/09) — **Principal Character Artist (Face)**, NBCUniversal/DreamWorks Montreal: **o alerta do LinkedIn é a MESMA vaga de ontem, e ela continua viva e sem veto**

`https://jobs.smartrecruiters.com/NBCUniversal3/744000150414819-principal-character-artist-face-i-artiste-principal-e-personnage-face-`
`https://www.linkedin.com/jobs/view/4469197089/` (o mesmo anúncio, pela rota do seu alerta)

**Não é porta nova, e é por isso que esta entrada é curta:** o alerta *"Character Art in Canada"*
das **14h44** trouxe a requisição **`744000150414819`** (ref `51626013`), que já está com **dossiê
campo a campo mais abaixo nesta fila**, escrito em 18/09 às 16h45. Não abri nada duas vezes: o que
fiz hoje foi **revalidar** e trazer o que faltava.

**O que foi medido agora, ponto por ponto:**
- **Viva:** a API do SmartRecruiters devolve `active=true`, `visibility=PUBLIC`, `releasedDate`
  `2026-09-18T15:57:55Z`, e a URL final do anúncio responde **HTTP 200**.
- **Única:** li por inteiro os dois quadros da casa (`NBCUniversal3` + `NBCUniversal1`,
  **375 requisições únicas**) e esta é a **única** *Principal Character Artist (Face)* — o alerta não
  está apontando para uma segunda vaga com o mesmo título.
- **Régua de veto rerodada** nos 10.585 caracteres do corpo da API, com os 43 termos do
  `regua-veto.py`: **3 acertos, os três falso positivo** e os mesmos de ontem — `citizenship` dentro
  da cláusula antidiscriminação e dois `visa` dentro das palavras **francesas** *visages* e *Visage*.
  Zero `Eligibility`, zero `legally authorized`, zero `days a week`, zero `work permit`, zero
  `sponsor`, zero `relocat`, zero exigência de francês no **payload cru**.
- **Controle positivo, e hoje ele veio DOBRADO** (a regra da casa: ausência só vale contra irmã que
  mostre o bloco presente): `744000137526729` (*Lead Character Artist, Body/Crowd, Face, Hair &
  Wardrobe*, 13/07) e `744000149923759` (*Lead Environment Artist*, 16/09) trazem, cada uma, no mesmo
  endpoint, *"**Eligibility Requirements** ... Must be willing to work in our Montreal office a
  minimum of 4 days a week. **Must be legally authorized to work in Canada.**"* A de personagem não
  tem o bloco. **A ausência é real.**
- **Dedupe:** `dedupe-agora.sh 744000150414819 NBCUniversal` + grep de *Principal Character Artist* e
  *(Face)*: **zero em `enviados.csv`** (nunca enviada), e as ocorrências em `processados.csv`,
  `docs/index.html` e nesta fila são **o registro de ontem**, não candidatura. No **Gmail**,
  `NBCUniversal OR DreamWorks OR smartrecruiters newer_than:3d` devolveu **uma** thread, e é o
  próprio alerta do LinkedIn — **nenhum recibo** desta requisição.

**A rota nova que eu trouxe, e ela é para o seu celular:** o anúncio do LinkedIn é **offsite apply**
(10 ocorrências de `offsite` no HTML de convidado de 311.727 caracteres, e **zero** `smartrecruiters`
e `NBCUniversal3` — o destino fica atrás do login). Ou seja: o botão *Apply* do alerta te joga no
**mesmo `/oneclick-ui`** que dá 403 de DataDome para a automação, e **no seu navegador logado ele não
deve nem aparecer**. Pelo alerta é um toque; por mim não existe porta.

**As respostas, com a verdade, iguais às do dossiê abaixo:** autorização para trabalhar no Canadá
**NÃO**; precisa de patrocínio **SIM**; disposto a realocar **SIM** (e a vaga é **híbrida** em
Montréal, `#410, 6300 du Parc Avenue`); pretensão pela política do briefing, faixa não publicada e
casa grande no Canadá → **CAD 95.000**, com a abertura *"Open to aligning with your band for the
role; as a reference, I'm looking at around CAD 95,000."*; salário atual *"Confidential under the NDA
of my current contract."*

**A ressalva honesta continua a mesma, e ela não melhorou com a revalidação:** é **realismo facial
fotorreal AAA** (blendshapes, *scanning*, *performance capture*, Metahuman) e o seu portfólio é
**estilizado**; *Principal* é um degrau acima de sênior. Ela está aqui porque é personagem por
título e por corpo, em casa da regra 14.

**ORDEM DENTRO DA CASA, se for gastar mais de um clique:** personagem primeiro. *Lead Artist (Props)*
`744000150413374` e *Principal Vegetation Artist* `744000150412708` (ambas de 18/09, também sem o
bloco de elegibilidade) são **ambiente** e vêm depois. E **não clique** na *Lead Character Artist*
`744000137526729`: ela é a que **tem** o veto escrito de autorização e de 4 dias no escritório.


### 🔴 ENTROU EM 19/09 15h (Jhon A, 32o turno) — **Asset Generalist Senior Artist** da **FOLKS VFX**, em **TORONTO** e em **MONTREAL**, parede de DataDome

`https://jobs.smartrecruiters.com/PitchBlackCreative/7000000000004158` (Toronto, ON)
`https://jobs.smartrecruiters.com/PitchBlackCreative/7000000000004252` (Montréal, QC)

**Por que é você e não a automação, em uma frase:** é **SmartRecruiters**, e o DataDome da
plataforma nasce **um clique depois do anúncio**, no `/oneclick-ui` — medido em 26º turno em duas
contas independentes, com `ct.captcha-delivery.com` e página de 0 caractere. A página do anúncio é
limpa mesmo; o porteiro é no passo do formulário. Para você, logado num navegador de verdade, é um
clique em *I am interested*.

**O achado que trouxe estas duas portas:** a Folks VFX **não publica no próprio domínio**. O
`folksvfx.com/careers/open-positions` linka `careers.smartrecruiters.com/PitchBlackCreative/folks-`,
ou seja o quadro dela vive no SmartRecruiters de uma **agência** (Pitch Black Creative), com 21
vagas. Procurar por "folks" em qualquer censo de ATS devolve zero por isso.

**Por que ela vale, com as frases do anúncio:** o `typeOfEmployment` da API é **Full-time** (o
"(Freelance)" do título **não** se confirma no corpo), e o corpo diz *"Execute advanced asset work
including **hero characters** and complex assets"*, *"Lead asset development from modelling through
final lookdev"* e pede *"Expert-level proficiency in Maya, ZBrush, Substance Painter, Mari, Katana
and Houdini"*. É a disciplina dele com todas as letras, em **Canadá anglófono** (Toronto) e em
Québec, e o anúncio ainda abre remoto entre as três cidades: *"Remote candidates within Montreal or
Vancouver may also be considered"* (na de Toronto) e *"Remote candidates within Toronto or Vancouver
may also be considered"* (na de Montréal).

**Régua de veto: ZERO veto real em 4.393 caracteres.** Os dois acertos dos 43 termos são falso
positivo e ficam escritos: `citizen` aparece dentro da **cláusula de não discriminação**
(*"...veteran or military status, citizenship, or any other characteristic protected by applicable
federal, state, provincial, or local law"*) e `proficiency in` é a lista de **softwares**.

**Ressalva honesta, e ela é dupla:** (1) o anúncio **não diz nada sobre patrocínio de visto**, nem a
favor nem contra — então "sem veto" aqui é **ausência de frase**, não promessa de patrocínio; (2) a
**terceira** requisição, `7000000000004182` (*Artiste généraliste senior – Assets*, Montréal), é a
**mesma vaga em francês** (corpo de 4.392 caracteres, espelho do inglês) — manda-se **uma** vez por
cidade, nunca nas duas versões, que é a armadilha bilingue da regra do briefing.

**MANDE UMA POR CIDADE E PREFIRA A DE TORONTO**, pela prioridade de Canadá anglófono.


### ✅ RESOLVIDO ÀS 20h10 — VOCÊ NÃO PRECISA CLICAR NADA AQUI: **Senior Character Artist – Outsourcing**, Omeda Studios

**O link do Breezy que você mandou às 20h00 era a porta, e a candidatura foi enviada e confirmada dez
minutos depois.** Requisição `02f381de451501`, em
`https://omeda-studios-limited.breezy.hr/p/02f381de451501-senior-character-artist-outsourcing`.
**Porteiro zero**, medido no navegador aberto. Prova: **POST 204** em
`app.breezy.hr/api/apply/02f381de451501`, URL final `/apply/submitted`, e o texto do servidor
*"Application Submitted. Your application has been submitted successfully. Good luck!"*. Carta de
**250 palavras** escrita para a casa, CV anexado, pretensão **GBP 42.000/ano**.

**E a previsão do fim deste item estava certa sobre o mecanismo e errada sobre a família:** ela dizia
*"o ATS da casa é Teamtailor, que não tem captcha, mas pode exigir verificação por e-mail, e a
candidatura não entra até alguém abrir o link"*. **A família era BREEZY, e a verificação por e-mail
existe mesmo.** Chegou um *"One more step!"* com um código de 4 dígitos, e a pergunta por trás dele
tem `move_to_stage_id: applied` — ou seja, sem digitar o código a candidatura **fica fora do estágio
Applied com a tela dizendo que foi enviada do mesmo jeito**. O código foi lido no Gmail e submetido, e
o servidor respondeu *"Responses Submitted. Your responses have been submitted successfully.
Thanks!"*. **Nada disso sobrou para você.**

**A única coisa que pode pedir sua mão, e só se acontecer:** até o fim do turno **não** chegou o
segundo e-mail, o *"Thank you for your application"* que a Playdead e a Warhorse mandaram. Se nos
próximos dias aparecer algum e-mail da Omeda pedindo qualquer coisa, é só repassar.

**Por que a porta não existia às 12h48, e a lição é minha:** eu sondei os tokens `omeda`,
`omedastudios`, `omeda-studios` e `predecessor` no Breezy e dei a família por morta. O locatário é
**`omeda-studios-limited`, com o sufixo jurídico**. Nome de casa não gera slug de forma confiável, e
"sondei quatro variantes" nunca é "a família não tem esta casa".

<details>
<summary>O que estava escrito aqui antes das 20h10, guardado porque a medição continua valendo</summary>

### 🔴 (histórico) ENTROU A MELHOR PORTA DE HOJE E ELA É DE PERSONAGEM POR TÍTULO — **Senior Character Artist – Outsourcing**, Omeda Studios (Reino Unido, remoto)

`https://www.linkedin.com/jobs/view/4466902903/`

**Por que é você e não a automação, em uma frase:** o anúncio é **offsite apply** e o LinkedIn
**esconde o destino atrás do login**, e o site de carreiras da própria casa
(`careers.omedastudios.com`, que é Teamtailor) **responde 404 em todo caminho**. Você está logado no
LinkedIn e **recebeu este mesmo alerta no celular às 12h44 UTC**: para você é um clique no botão
*Apply*, para mim não existe porta.

**O que foi medido, para você não repetir o caminho:** o HTML de convidado da vaga (334 KB) e a URL
canônica do `uk.linkedin.com` (354 KB) têm **zero ocorrência de `omedastudios`** e **zero bloco
JSON-LD**; o único link externo da página é o perfil do recrutador; o botão carrega
`data-impression-id="public_jobs_apply-link-offsite_contextual-sign-in-modal"` e o modal diz *"Join
to apply for the Senior Character Artist – Outsourcing role at Omeda Studios"*. As três rotas
públicas de redirect de *apply* dão 404. No lado da casa: `omedastudios.com` dá 301 para
`careers.omedastudios.com`, que é Teamtailor da região EU, e devolve **404 em `/`, `/jobs`,
`/jobs.json`, `/jobs.rss`, `/connect`, `/sitemap.xml`, `/api/v1/jobs`, `/uk/jobs` e mais seis
caminhos**, sempre com `x-cache: MISS` e `x-request-id` novo — é o servidor deles respondendo, não
cache velho. O padrão de URL de vaga existe (`/jobs/4912694-qa-lead`, confirmado por terceiro), mas
**sem o ID numérico da vaga de hoje não há porta**, e as vagas antigas também dão 404.

**A vaga, em números:** publicada hoje ~**06h44 UTC**, achada pelo alerta das 12h44 e trabalhada às
12h50. **Casa 100% inédita na campanha:** `dedupe-agora.sh 4466902903 omeda` deu ID inédito nos
quatro arquivos, o grep por `omeda` e `predecessor` em `enviados.csv`, `processados.csv`,
`docs/index.html` e `alvos.csv` deu zero, e o Gmail com `Omeda OR Predecessor OR Voldex
newer_than:40d` devolveu **um único fio, que é o próprio alerta de hoje**.

**Régua de veto: ZERO dos 43 termos**, e ela foi feita do jeito difícil. Rodada na URL do LinkedIn
ela acusa três termos, e **os três são o rodapé de idiomas do próprio LinkedIn** (*français*,
*deutsch*, *svenska*) — não o anúncio. Rodada sobre o texto do anúncio, **4.199 caracteres** (acima
do piso de ~1.000), dá **zero**: zero `relocation`, zero `sponsor`, zero `right to work`, zero
`visa`, zero `work permit`, zero exigência de residência. A única exigência de presença é de **fuso
horário**, e ela é **a seu favor**: *"Working hours aligned with the UK, or slightly later for more
overlap with our US-based team"* — o Brasil é justamente *slightly later* que o Reino Unido. O
anúncio se descreve como *"remote-first game studio"* e lista *"Global, remote team"* nos benefícios.

**O caso a seu favor, com as frases do anúncio:** pede *"5+ years in character art for games, with
at least one shipped title"*, *"Expert knowledge of ZBrush, Substance Painter and Maya"* e
*"Hands-on Unreal Engine 5 experience"*; traz *"Hair card and groom creation with FiberShop"* no
**Nice to Have**, e grooming é o seu diferencial; e valoriza explicitamente quem vem do lado do
fornecedor — *"Time at or with an external development partner is a real advantage here"*, que é a
sua experiência de estúdio-fornecedor.

**A ressalva honesta, e ela é dupla — leia antes de clicar:** (1) o próprio anúncio avisa *"Please
read this part carefully. This is not a pure hero production role. At least half of your time is
outsourcing: reviewing submissions, giving feedback, and holding the technical line"* e *"If your
ambition is to spend most of your week sculpting, this isn't the right role for you"*; metade do
trabalho é revisão e gestão de parceiro. (2) pede *"A strong portfolio of realistic, game-ready
characters"* e o seu portfólio é **estilizado** — a mesma ressalva de registro de estilo que a
Wargaming e a Rising Sun já carregam no painel. As duas coisas não impedem a candidatura; elas só
dizem que o encaixe é de **disciplina certa com ênfase diferente**.

**RESPOSTAS PRONTAS, na ordem em que os formulários pedem:**

- **Autorização de trabalho** — a verdade, sempre: *"I do not currently hold the right to work in
  the UK and would require visa sponsorship."*
- **Realocação / disponibilidade** — *"I am ready to move for the role."* E, onde couber mais de uma
  linha: *"My academic background, with an honors laurea, a postgraduate specialization, a master's
  in progress, IELTS and publications, makes a strong visa case."*
- **Fuso horário**, que aqui é campo forte e não fraqueza: *"I work from Brazil, which sits slightly
  later than the UK — exactly the overlap window the role asks for, and it also covers your US-based
  team."*
- **Pretensão** — **GBP 42.000**, que é a faixa do BRIEFING para casa pequena ou média no Reino
  Unido (o anúncio **não publica faixa**), sempre com *"Open to aligning with your band for the
  role"*. Nunca revelar o salário atual da E-Line.
- **Liderança de equipe** — **sim**, com os cinco anos de Senior na E-Line, professor e fundador da
  própria escola.
- **Anexos** — `Vini_Cavalcanti_CV.pdf` e `Vini_Cavalcanti_Portfolio.pdf`, em `/home/user/apply`.
  Se houver campo de carta, ela ainda **não** foi escrita para esta casa: peça ao maestro, porque o
  Jhon não escreve carta.

**O que provavelmente te espera do outro lado:** o ATS da casa é **Teamtailor** (confirmado pelos
cabeçalhos e pelo painel `app.teamtailor.com/companies/JtMUStwpYVA@eu`), que **não tem captcha**,
mas **pode exigir verificação por e-mail** — a tela diz *"Verify your email"* e **a candidatura não
entra até alguém abrir o link**. Abra o e-mail: a página passa a dizer *"Applied to"*. **E se a URL
de destino aparecer, me mande ou cole no painel**: com o link direto a automação envia sozinha, e a
casa volta a ser fila de agente em vez de fila sua.


</details>

### 🔴 ENTROU UMA PORTA HOJE ÀS 15h57, É DE PERSONAGEM E É DA FAMÍLIA DREAMWORKS — **Principal Character Artist (Face)**, NBCUniversal Montreal

`https://jobs.smartrecruiters.com/NBCUniversal3/744000150414819-principal-character-artist-face-i-artiste-principal-e-personnage-face-`

**Requisição `744000150414819`** (refNumber `51626013`), **publicada hoje às 15h57:55 UTC** e achada
**36 minutos depois** pela varredura por data das 16h45. Montreal, Quebec, **híbrida**, efetiva,
*Mid-Senior Level*, função *Art/Creative*. Em 640 quadros e 7.520 vagas lidas na janela de 8 horas,
**ela é a única da disciplina**.

**Por que é com você, e não é preguiça da automação:** o formulário responde **HTTP 403** e entrega
**captcha de desafio do DataDome**. Medido com navegador de verdade (Xvfb, nenhum concorrente): o
frame principal fica com **0 campos e 0 caracteres em 10 tentativas**, e o formulário real é um
iframe de `geo.captcha-delivery.com` com 16 campos, botões *Verify* e *Send*, e o texto literal
*"Verification Required ... Slide right to secure your access ... We detected unusual activity from
your device or network ... Automated (bot) activity on your network (IP 160.79.106.136)"*. É o
porteiro que cita o IP na tela, exatamente como a regra 17 do briefing descreve. **Na sua rede, com
a sua sessão, ele não deve nem aparecer.**

**Régua de veto: zero veto escrito** — e a leitura foi feita do jeito difícil de propósito. A URL
final é SPA e devolve **63 caracteres** de texto limpo, o que pelo piso de ~1.000 é **leitura
inválida** e não "zero veto"; então a régua correu no **corpo da API**, com 10.706 caracteres. Três
acertos, **os três falso positivo**: `citizen` é a palavra *citizenship* dentro da cláusula
antidiscriminação, e os dois `visa` estão dentro das palavras **francesas** *visages* e *Visage*
(rosto). Zero `relocation`, zero `sponsor`, zero `work permit`, zero exigência de idioma.

**E a parte que mais importa, porque esta casa já custou caro:** em 07/09 três vagas da
NBCUniversal em Montréal foram recomendadas e morreram no bloco *Eligibility Requirements* (*"Must
be legally authorized to work in Canada"*). **Esta não tem o bloco, e isso foi provado contra
controle positivo**, não por leitura otimista: a irmã **Lead Environment Artist `744000149923759`**
de 16/09 carrega `Eligibility`, `legally authorized`, `authorized to work` e `days a week` no
**payload cru inteiro**, nas mesmas quatro seções; a de personagem traz **zero de todos**. Mesma
casa, mesmo endpoint, mesmas chaves — a ausência é real.

**Dedupe quádruplo, feito:** `744000150414819` e `51626013` com **zero ocorrência** em
`enviados.csv`, `processados.csv`, `docs/index.html` e nesta fila. No Gmail a casa só tem as cartas
frias de 03/09 (Matt Baer) e 05/09 (Sean Sexton) e o *Express Future Interest Form* de 17/09 —
**nenhum recibo desta requisição**. Não é duplicata.

#### O que preencher, campo a campo

| Campo | O que vai |
|---|---|
| Nome / e-mail | `Vini Cavalcanti` · `contact@vinicavalcanti.art` |
| Telefone | o seu, formato internacional (não está escrito neste repositório, que é público) |
| CV | `Vini_Cavalcanti_CV.pdf` |
| Links | `artstation.com/viniciuscavalcanti` · `linkedin.com/in/vinicavalcnti` · `vinicavalcanti.com` |
| **Autorização de trabalho no Canadá** | **a verdade: NÃO** — e **SIM** para "precisa de patrocínio" |
| **Pretensão** | faixa não publicada, casa grande no Canadá → **CAD 95.000**, com a abertura: *"Open to aligning with your band for the role; as a reference, I'm looking at around CAD 95,000."* |
| Salário atual | *"Confidential under the NDA of my current contract; happy to discuss ranges during the process."* |

**A ressalva honesta, porque ela pode mudar a sua decisão:** o anúncio é de **realismo facial
fotorreal em AAA** — *"Strong portfolio demonstrating expertise in high-quality facial modeling and
realism"*, blendshapes, *scanning*, *performance capture*, Unreal e **Metahuman** — e o seu
portfólio é personagem **estilizado**. E *Principal* é um degrau acima de sênior. Ela entra porque
é personagem de verdade (modelagem facial, anatomia, pipeline de personagem modular) e porque a
regra 14 manda aplicar em qualquer nível e qualquer disciplina de arte do grupo.

**As outras duas da mesma leva de Montreal, se quiser gastar mais de um clique na casa:** *Lead
Artist (Props)* `744000150413374` e *Principal Vegetation Artist* `744000150412708`, publicadas
hoje às 15h53 e 15h50, **também sem o bloco de elegibilidade**. As duas são **ambiente**, então
pela sua regra de 10/09 elas vêm depois — personagem primeiro.

### 🔴 ENTROU UMA PORTA, e é da EA: Senior Character Artist 215788, EA SPORTS FC Vancouver

`https://jobs.ea.com/en_US/careers/JobDetail/Senior-Character-Artist/215788`

**Revalidada em 16/09 às 03h**, na fonte oficial: a requisição continua no portal (listagem
completa de **325 vagas**, paginada por `jobOffset`) e a página responde **HTTP 200**. Efetiva
(*Regular Employee*), híbrida, Vancouver. **Faixa publicada pela própria EA: CAD 114.300 a
156.200** — pela política, pede-se a **base, CAD 114.300**.

**Régua de veto no texto inteiro: um único acerto, e é falso positivo conhecido** —
`eligib` em *"eligible for bonus and other incentive programs"*. **Nenhum veto escrito.**

**Dedupe, pelo ID e não pelo título:** a irmã **215358** (Character Artist, efetiva, mesmo time)
foi enviada e confirmada em 07/09, e a **215657** (temporária) em 03/09. A **215788 é requisição
própria e mais sênior**, com faixa maior. Não é duplicata.

**Por que é com você:** o botão *Next* da tela de informações gerais devolve `Internal server
error` do Avature em **cinco tentativas**, com e sem anexos, em dois dias diferentes. Não é
captcha nem falta de conta. **E o erro de fluxo que come a rodada:** você já tem conta desde
03/09, então **entre pelo login**; o bloco *First time applicant* preenche tudo e no fim devolve
*"There's an existing record with that email"* sem enviar nada. Campo a campo, com as armadilhas
da tela, está na página de cliques e em `automacao/respostas-formularios.md`.

### 🟢 ENTRARAM MAIS DUAS, achadas cruzando o painel com a página (16/09, 03h30)

**Gigantic Duck — 3D Artist, Bombergrounds — `https://giganticduck.com/careers`**
**REMOTA e efetiva, 40h por semana, escrito na própria página**, então aqui **não há questão de
visto**. Revalidada agora: HTTP 200 e a vaga continua listada. Régua de veto: **zero ocorrência**
dos dezessete termos. A parede é o reCAPTCHA v3 do Contact Form 7, que é pontuação de sessão: do
IP da automação reprova, do seu navegador passa.

**Good Job Games — Senior 3D Artist — `https://job-boards.greenhouse.io/goodjobgames/jobs/7491067003`**
Viva (HTTP 200), zero veto. **Trava numa pergunta que só você pode responder:** *"Match Villains
oyununu kaç level oynadın"*, quantos níveis do jogo você jogou. As outras duas já estão resolvidas:
Maya **sim**, portfólio **ArtStation**. Ressalva escrita: a Turquia está fora da lista de países da
campanha, então ela não é prioridade.

**Eram 77 linhas, agora são 78 portas, e as mexidas estão escritas.** Saíram duas: a mesma
vaga da Framestore aparecia **três vezes**, com o mesmo endereço, em dois grupos diferentes, e
número inflado não é resultado. Entraram três: a EA 215788 e estas duas.

**Sobraram 21 portas de mão da disciplina fora da página**, listadas em
`/tmp/claude-0/fora-da-fila.json` para a próxima rodada triar. A maioria é concept, level design ou
direção de arte, que estão fora da disciplina; a Stirling Animation tem restrição **escrita** de
residência no Reino Unido, além de contrato de *Contractor*.

Nenhuma carta foi escrita duas vezes: o gancho de cada uma sai do anúncio que a campanha leu, a
semelhança máxima entre duas cartas do lote é de 24% (o teto que a campanha aceita é 55%), e
`automacao/confere-lote-formulario.py` reprova emoji, travessão, floreio, menção a salário e
**nome próprio que não esteja na prova daquela porta** — a guarda contra atribuir à casa um
filme, um prêmio ou um cliente que ela não tem.

## 📬 LOTE DE CARTAS — **9 rascunhos na fila, um comando seu** (estado de 15/09 às 19h45)

**O lote anterior SAIU, e isto foi conferido na caixa e não suposto.** As buscas `in:sent` mostram
duas rajadas com a assinatura do `envia-rascunhos.gs`: **34 cartas em 14/09 às 17h54** e mais
**16 em 15/09 às 14h14**. Eram as vinte e nove represadas mais o resto da fila. **Não há nada
daquele lote esperando você.**

**O que isso já rendeu, e é a parte que importa: CINCO PESSOAS RESPONDERAM** —
Eva Balvirčáková (MADFINGER), Giles Sander (Polyester), Michael Bengtsson (Mindbender),
Joost Spek (3Dpicnic) e Gillian Comerford (Boulder Media). As cinco threads estão vivas e todas
já foram respondidas de volta. **Duas quicaram** e os endereços estão mortos:
`hello@314arts.com` e `flord@rodeofx.com` (Rodeo FX).

**O `automacao/pessoas.csv` foi reconciliado contra a caixa em 15/09:** 42 fichas que ainda diziam
`rascunho-criado` ou `ficha-sem-carta` agora dizem **`CARTA ENVIADA`**, com a data e com quem
respondeu. Ficha que diz rascunho quando a carta já saiu é o que faz uma rodada reenviar.

### A fila de agora: 9 rascunhos, todos de assunto fixo

Um comando só, **`enviarRascunhos()`**. Não há nenhum de assunto próprio nesta fila.

| Para | Casa | Quando foi escrita |
|---|---|---|
| tero@animagency.fi | Animagency, Vantaa (FI) | 15/09 19h22 |
| info@allimator.com | Allimator, Estocolmo (SE) | 15/09 19h32 |
| eric@tordenfilm.no | Tordenfilm, Oslo (NO) | 15/09 19h33 |
| juha@fiilin.com | Fiilin Good Films, Helsinque (FI) | 15/09 19h33 |
| hey@kyka.fo | Kyka, Ilhas Faroe | 15/09 19h34 |
| jobs@frontvfx.com | Front VFX, Vancouver (CA) | 15/09 18h09 |
| haukur@gunhil.com | GunHil, Reykjavík (IS) | 15/09 16h42 |
| fmosvold@online.no | Kool Produktion (NO) | 15/09 16h42 |
| contact@sleetfleet.com | sleetfleet, Helsinque (FI) | 15/09 16h42 |

**Antes de rodar, confira duas coisas no editor do Apps Script:** que a cópia colada é a atual do
`automacao/envia-rascunhos.gs` (a lista `ASSUNTO_PROPRIO_PERMITIDOS` ganhou a Lightfox e a
Framestore), e que o disparo está **armado** — com ele desarmado o log lista tudo e **não sai
nada**, e o log parece idêntico ao de um envio real.
---

## 🖐️ DUAS ENTRADAS NOVAS DE 15/09 — **formulário 100% preenchido, faltam só dois cliques seus**

Achadas varrendo BambooHR com controle 200 nas duas pontas. As duas estão **preenchidas e conferidas
campo a campo em modo seco**; o que trava não é captcha, é uma parede da plataforma (detalhe no fim).
Do seu lado é abrir o link, clicar **Apply for This Job** e repetir o que está na tabela.

### 1. nWave — Bruxelas, Bélgica — https://nwave.bamboohr.com/careers/121

A melhor porta de formulário em dias, e o motivo é a pergunta obrigatória de departamento: ela oferece
**Character_Modeling (CHR_MOD)** e **Character_Surfacing/Grooming (CHR_SHD)**. É o cargo dele com todas
as letras. Régua de veto no texto integral da API: **zero acerto**, nenhum veto escrito.

| Campo | O que preencher |
|---|---|
| First / Last Name | `Vini` / `Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Phone | o do doc privado do Drive, formato internacional sem espaço |
| Country | **trocar Belgium por `Brazil` PRIMEIRO** — o BambooHR renomeia os rótulos conforme o país |
| Address / City / Province / Postal Code | os do doc privado do Drive |
| Date Available | `16/11/2026` (aqui a máscara é **dd/mm/yyyy**) |
| Desired Pay | `EUR 55,000 per year. Open to aligning with your band for the role.` |
| Website / LinkedIn | ArtStation e LinkedIn |
| Highest Education Obtained | `Other` |
| College/University | `Melies Sao Paulo` |
| Which Studios | **Brussels** |
| What department(s) | **Character_Modeling (CHR_MOD)** |
| Experience level | **SENIOR** |
| Resume | `Vini_Cavalcanti_CV.pdf` |
| `Please leave this field blank` | **HONEYPOT — deixar VAZIO** |
| Anything you want us to know | o texto abaixo |

```
I am not an EU citizen and I would need visa sponsorship for Brussels. I am ready to move for the role.

I am applying to Character Modeling. I am a Senior 3D Character Artist with more than ten years in stylized characters. I take a character end to end: sculpt, retopology that deforms cleanly, UVs, baking, hand-painted and PBR texturing, look development, cloth in Marvelous Designer and grooming in Houdini, so modeling, surfacing and groom are one continuous job for me rather than three handoffs. If it helps your sorting, I fit CHR_SHD as well as CHR_MOD.

Credited on The Wingfeather Saga season 1 at Angel Studios, where I modeled and hand-painted the show's characters. For almost five years at E-Line Media I have carried Endstar's hero characters from first sculpt into engine. I review other artists' work and set the asset standard, and I teach as founder of my own character art school.

On the visa case, because it is usually the first question: honors degree, a postgraduate specialization in Game Art at Melies Sao Paulo, a master's in Creative Industries in progress, IELTS and publications.

Portfolio: https://www.artstation.com/viniciuscavalcanti
```

**O formulário manda submeter uma vez por departamento.** Vale submeter uma segunda vez em
**CHR_SHD**, trocando só a primeira frase do segundo parágrafo.

### 2. Image Engine — Vancouver, Canadá — https://imageengine.bamboohr.com/careers/21

`General Application - Assets (Modeling/Texturing/LookDev/Grooming)`. Eu tinha fechado esta porta porque
o anúncio traz, em vermelho: *"Candidates are required to be based in British Columbia and eligible to
work in Canada"*. **Você corrigiu e estava certo:** o próprio formulário desmente o aviso, porque a
pergunta obrigatória de status oferece **"Work Permit Required"** como opção. A casa prevê quem precisa
de patrocínio. Então se responde a verdade e se explica no campo livre.

| Campo | O que preencher |
|---|---|
| Nome / Email / Phone / Endereço | os de sempre (telefone e endereço no doc privado do Drive) |
| Country | `Brazil` |
| Date Available | `11/16/2026` — **aqui a máscara é mm/dd/yyyy**, e digitar 16/11 vira `1m/11/2026` |
| Desired Pay | `CAD 95,000 per year. Open to aligning with your band for the role.` |
| Cover Letter / Resume | `Vini_Cavalcanti_Cover_Letter.pdf` e `Vini_Cavalcanti_CV.pdf` — **a carta vem ANTES do CV no DOM** |
| Position of interest | `Modeling. I also cover Texturing and Look Development, and I groom hair and fur in Houdini.` |
| Years of experience | `10+ years` |
| Level of experience | `Senior` |
| **Status para o Canadá** | **`Work Permit Required`** |
| Expiry date do work permit | `N/A. I do not hold a work permit; I would need sponsorship.` |
| Anything else we should know | o texto abaixo |

```
Said first so it is not missed: I am not based in British Columbia and I am not yet eligible to work in Canada. I would need visa sponsorship, and I am ready to move to Vancouver for the role. I am applying because your own form offers Work Permit Required as a status, so I would rather be honest about it up front than leave it out.

Assets is exactly my job. I am a Senior 3D Character Artist with more than ten years in stylized characters, and I take a character end to end: sculpt, retopology that deforms cleanly, UVs, baking, hand-painted and PBR texturing, look development, cloth in Marvelous Designer and grooming in Houdini.

Credited on The Wingfeather Saga season 1 at Angel Studios, where I modeled and hand-painted the show's characters. For almost five years at E-Line Media I have carried Endstar's hero characters from first sculpt into engine. I review other artists' work and set the asset standard, and I teach as founder of my own character art school.

On the visa case: honors degree, a postgraduate specialization in Game Art at Melies Sao Paulo, a master's in Creative Industries in progress, IELTS and publications.

Portfolio: https://www.artstation.com/viniciuscavalcanti
```

### Por que as duas ficaram na sua mão, e eu CLIQUEI antes de dizer isso

**O envio do BambooHR não sai daqui, e isso foi medido em DOIS locatários diferentes.** Não é captcha:
não há desafio nenhum na tela. O que foi conferido, para não virar suposição: clique **sem force** no
botão (o Playwright reclamaria se estivesse coberto, e não reclamou), `form.checkValidity()` devolvendo
**true** com **zero** elemento em `:invalid`, zero campo obrigatório vazio, zero erro de JavaScript no
clique, e o `requestSubmit()` nativo também disparado sem efeito. O **upload funciona** (200 em
`ajax/files/attachTemporary.php`, duas vezes na Image Engine), então não é rede nem proxy. A página
relata uma **exceção própria** ao Rollbar no envio. Falsa pista descartada: o 401 em `/globals/locale`
aparece para qualquer visitante anônimo e não é a causa.

**Consequência para as próximas rodadas: vaga em BambooHR é item de mão.** Não gastar rodada tentando
enviar por aqui; o que rende é chegar com o dossiê pronto, como estes dois.

---

## 🔎 RODADA DE CAÇA DE 14/09 às 00h45 UTC (Jhon B) — **grupo Disney medido em zero · e a fila de Pinpoint ACABOU** (correção de 01h20)

### Grupo Disney, olhado por ordem dele como em toda rodada

`sh automacao/ronda-disney.sh` → **12 consultas responderam, ZERO falharam, 12 IDs da disciplina
no ar, nenhum novo.** Este zero foi MEDIDO, não é resposta vazia: o script falha alto em vez de
devolver zero falso, e os dois quadros do locatário `disney` (`disneycareer` e `disneycareerdc`)
entram na conta.

### A fila de Pinpoint acabou: oito usadas e a nona morta

Das nove portas `register-your-interest` que a rodada de 10/09 levantou, **oito já aparecem no
`enviados.csv`**: rocksteady, playground-games, magnopus, singularity6, pipeworks, outpost-vfx,
ingenuitystudios e wushustudios. A nona eu dei como livre e **estava errado** (leia abaixo):

#### ~~Hyper Hippo Entertainment~~ — **ROTA MORTA. ERRO MEU, CORRIGIDO NA MESMA NOITE.**

> **NÃO CLIQUE AQUI.** Eu enfileirei esta porta às 00h45 de 14/09 depois de um `curl` devolver
> **HTTP 200** com o título `Register Your Interest | Hyper Hippo Entertainment Careers` e zero
> marcador de captcha. **Estava errado, e o registro já avisava.**
>
> Meia hora depois, na rodada de envio, o `dedupe-agora.sh` mostrou o que eu não tinha lido: a
> campanha mediu esta rota **duas vezes no navegador**, em 08/09 e de novo em 11/09, e as duas
> deram **404**. A causa foi isolada por bisseção de cabeçalho na época.
>
> **Reconferi eu mesmo agora, no navegador de verdade:** `HTTP 404`, título `404 Not Found |
> Pinpoint`, texto *"The page you were looking for doesn't exist"*, e **zero campo de formulário
> na página**. O `curl` recebe 200 e o navegador recebe 404, na mesma URL e no mesmo minuto.
>
> **A lição, que vale mais que a porta:** nesta casa, e provavelmente em outras do Pinpoint,
> **`curl` 200 não prova porta aberta**. Só o navegador prova. Quem varrer Pinpoint por curl tem
> que confirmar no navegador antes de enfileirar, e eu não confirmei.
>
> Com isso, das nove portas `register-your-interest` levantadas em 10/09, **oito foram usadas e a
> nona está morta: a fila de Pinpoint acabou.**


---

## 🔎 RODADA DE CAÇA DE 13/09 às 14h45 UTC (Jhon B) — **PORTA DE ESPONTÂNEA SEM CAPTCHA: ZERO NOVA, em 23.161 sondagens**

**O que você precisa fazer nesta seção: nada.** Ela é medição, não tarefa. Está aqui para a
próxima rodada não gastar o dia refazendo o que já foi medido.

O alvo era estreito: **porta de candidatura espontânea que não põe desafio** — a família que já
provou que passa (a Fenris entrou em 10/09 pelo `register-your-interest/new` do Pinpoint).
Quatro famílias sondadas, **zero porta nova depois do dedupe**.

| Família | Rota sondada | Sondagens | Rota viva | Sem desafio no HTML | Nova depois do dedupe |
|---|---|---|---|---|---|
| **Pinpoint**, por slug | `/en/register-your-interest/new` | **2.601** | 23 em 200 · 2 em 302 | 15 servem o formulário inteiro | **0** |
| **Pinpoint**, por domínio próprio | idem em `careers.`/`jobs.`/`career.` de 5.852 domínios | **17.557** | **1** | 1 | **0** |
| **Teamtailor**, slugs conhecidos | `/connect` | **149** | 132 (47 em 200 + 85 em 301) | 132 | **0** |
| **Teamtailor**, slugs novos | `/connect` | **2.572** | 12 | 12 | **0** |
| **Teamtailor**, anúncio espontâneo | `jobs.json` dos 149 inquilinos | **149 feeds** | 40 anúncios | — | **0** |
| **Homerun** | `/`, `/open-application`, `/open-applications` | **12** | 1 (`totalmayhemgames`) | 1 | **0** (já usada) |
| **Recruitee** | — | **0** | — | — | **0** (parede já medida 7×, não remedida) |

**Por que deu zero, em uma linha:** esta lane foi trabalhada em 10 e 11/09 e **foi consumida**.
Os 13 quadros Pinpoint com a porta aberta são os mesmos 11 de 10/09, e o Gmail mostra recibo
nos que interessam; as 15 rotas Teamtailor que a caça de 11/09 enfileirou têm **todas** recibo
de 11/09 às 14h-15h na caixa dele.

### As duas únicas coisas acionáveis que saíram daqui

1. **Os 7 quadros Pinpoint com o banco de talentos DESLIGADO foram re-testados hoje, como
   10/09 mandou, e os 7 continuam desligados** (302 na `register-your-interest/new`):
   `appquantum`, `tripledotstudios`, `buildarocketboy`, `everi`, `ruckus-games`,
   `bandainamcomobile`, `theready`. Ligar o banco é um clique no painel do estúdio, então vale
   re-testar de novo **depois de 27/09** — antes disso é rodada queimada.
   **Mudança de estado medida hoje:** a `hyperhippo`, que 10/09 listava como porta aberta,
   agora devolve **404** — o quadro morreu, e ela sai da lista.
2. **Cinco slugs ficaram `NÃO CONFERIDO`**, e a palavra é essa: `clockwork`, `eallin`,
   `ilogos-game-studios`, `moonbug-entertainment`, `snowdogstudio` devolveram `000` na primeira
   passada **e na reconferência lenta**. Não são zero, são não medidos. (Os outros 111 que
   deram `000` foram reconferidos um a um e eram 404 de verdade.)

### Três armadilhas medidas hoje, para não custarem a rodada de alguém

- **`200` na URL exata do Pinpoint não é Pinpoint.** Na varredura de domínio próprio, **44
  hosts** responderam 200 em `/en/register-your-interest/new` sem redirecionar, e **nenhum
  deles era Pinpoint**: são páginas de erro do próprio site que respondem 200 (`Page not
  found` da Take-Two, `Unknown Domain`, `Example Domain`, `Bizland`). Quem contar código de
  resposta registra 44 portas onde existe **uma**. O que decide é o `<title>` dizer
  *Register Your Interest* **e** o HTML trazer `job_seeker_form`.
- **A régua `ACME`/`Hooli` de 10/09 funcionou de novo, e pegou as duas melhores casas do dia.**
  `moonbug` e `framestore` abrem 200, servem o formulário e não têm captcha nenhum — e são
  **conta de demonstração**: o quadro traz as cinco vagas-semente (*Head of DEI* em Belfast,
  US e UK, *Marketing Manager* Paris, *Customer Service Rep* Nova York) e as divisões `ACME` e
  `Hooli`. Candidatura ali cai numa conta que ninguém abre.
- **`ccpgames.pinpointhq.com` responde 301 para `fenriscreations.pinpointhq.com`.** É a prova
  mecânica de que o quadro da Fenris **é** o da CCP Games: quem sondar a CCP como casa nova
  está reabrindo a candidatura de 10/09.

**Quebra por disciplina, como a regra de 10/09 exige: PERSONAGEM 0, AMBIENTE 0.** Não é "só
sobrou ambiente" — não sobrou nada, porque banco de talentos não tem disciplina de vaga e a
lane inteira já estava consumida.

**A única casa que a varredura trouxe e que não estava na lista de 10/09 era a Sun Creature
(Copenhague), e ela cai com motivo escrito naquele mesmo dia:** *"Estúdio de animação 2D. O
portfólio dele é 3D full character; a casa não tem a produção onde ele compete."* Some-se que
a caixa dele já tem auto-resposta da casa dizendo que **não aceitam candidatura espontânea**.
Registrada como descarte, não como achado.

---

## 🔎 RODADA DE CAÇA DE 13/09 às 12h50 UTC (Jhon B) — **FILA NOVA: ZERO** · corrigida em 14/09: das 15 ditas "da sua mão", **CINCO já eram suas e uma tem veto. Sobram 9**

**O que você precisa fazer nesta seção: nada.** Ela existe por dois motivos, e o segundo é o
que vale o seu tempo.

### 1. As 15 vagas foram RECONFERIDAS na fonte oficial — mas cinco já eram suas

Ninguém tinha feito isso desde 09/09, e vaga sênior de personagem dura de 3 a 7 dias. **Todas
as 15 responderam VIVA, zero morta, zero não conferido**, então nenhum clique seu vai para uma
vaga que já fechou. **O que esta seção errou, e a correção de 14/09 arruma, é outra coisa:
estar VIVA não quer dizer estar POR FAZER.** Cinco destas você já enviou:

| # | Vaga | Onde | Fonte | **Situação real** |
|---|---|---|---|---|
| ~~1~~ | ~~Behaviour — Senior 3D Character Artist, Dead by Daylight~~ | Montréal | Lever US | **JÁ ENVIADA 10/09 03h53** |
| 3 | Behaviour — Senior 3D Character Artist, projeto não anunciado | Montréal | Lever US | falta |
| 5 | Gameloft — Candidature Spontanée | Montréal | SmartRecruiters | falta |
| ~~6~~ | ~~Ubisoft Massive — Lead Character Artist, The Division 2~~ | Malmö | SmartRecruiters | **JÁ ENVIADA 10/09 04h03** |
| ~~7~~ | ~~Avalanche — Lead Character Artist~~ | Estocolmo | Lever US | **JÁ ENVIADA 10/09 04h08** |
| 8 | Rodeo FX — Senior Lookdev Artist | Toronto | SmartRecruiters | falta |
| 9 | Ubisoft Montréal — Team Lead, Modeling (Unreal) | Montréal | SmartRecruiters | falta |
| ~~10~~ | ~~Lighthouse Games — Lead Character Artist~~ | Royal Leamington Spa | Workable | **JÁ ENVIADA 10/09 04h00** |
| 11 | Framestore — 3D Modeller (contrato curto) | Montréal | Recruitee | falta |
| ~~12~~ | ~~Frontier — Experienced Character Artist~~ | Cambridge | **Lever EU** | **JÁ ENVIADA 10/09 03h57** |
| ~~13~~ | ~~Asobo — Character Artist H/F~~ | Bordeaux | **Lever EU** | **VETO DE IDIOMA, não clique** |
| 15 | Rodeo FX — Senior Lookdev Artist | Montréal | SmartRecruiters | falta |
| 16 | Framestore — Blender Generalist / Visual Development Artist | Montréal | Recruitee | falta |
| 17 | Framestore — Blender Generalist | Londres | Recruitee | falta |
| 23 | Skydance — Senior Grooming TD | Madri | Lever US | falta |

> ### ⛔ CORREÇÃO DE 14/09 — a tabela acima mandava você clicar em CINCO vagas que já são suas
>
> A versão anterior desta tabela listava as 15 como "na sua mão" e avisava de UMA só (a
> Frontier). **Cinco já tinham sido enviadas por você mesmo na madrugada de 10/09, entre
> 03h53 e 04h08 UTC, cada uma com recibo na caixa**, e continuaram na lista como se
> faltassem: Behaviour Dead by Daylight, Ubisoft Massive, Avalanche, Lighthouse Games e
> Frontier. **Quatro dessas cinco são exatamente as de personagem**, ou seja, a tabela
> empurrava seus melhores minutos para portas já abertas.
>
> Como isso foi medido, e o método vale mais que a correção: cada ID foi cruzado com o
> `enviados.csv` e depois **lido no CAMPO DE DESFECHO**, nunca pela simples ocorrência do
> nome. As cinco trazem `enviada` no campo e a frase literal do recibo.
>
> Descoberto porque a rodada do Jhon A de 14/09 ia aplicar na Avalanche: o modo seco passou,
> o formulário ficou perfeito na tela, e **o `dedupe-agora.sh` barrou no minuto do clique**.
> Sem ele a campanha teria mandado candidatura repetida para Estocolmo.
>
> **Sobram 9 de verdade**, e a 13 (Asobo) está fora por veto escrito de idioma
> (*"Tu disposes d'un niveau de français et anglais opérationnel"*), então o que resta para
> a sua mão são **9**, das quais **uma é de personagem**: a 3, Behaviour, projeto não
> anunciado.

**Ressalva corrigida em 14/09.** A 12 (Frontier) já foi enviada por você em 10/09 — e ela
**não era a única**: veja o bloco de correção logo acima, são CINCO nessa situação. A 13 (Asobo) continua **fechada pelo idioma**, com o veto relido hoje no anúncio
inteiro: *"Tu disposes d'un niveau de **français** et anglais opérationnel"*. Ela fica na lista
para quando o francês chegar ao nível, e a faixa publicada dela (32k€–47k€) está abaixo do piso
da sua política de pretensão.

### 2. A caça fechou em ZERO vaga nova, e o zero tem número

**54 quadros de Workday lidos com 5.242 vagas** (19 locatários, quadros de até 900 vagas
paginados por inteiro em vez de consultados por termo), **os dois hosts do Lever** com 20
quadros e 298 vagas, **6.938 tokens** sondados no host europeu do Lever, a **regra 14 conferida
pela segunda vez no dia** nas quatro casas, os **quadros nacionais** de Chéquia, Romênia, Nova
Zelândia, Irlanda e Suíça, e o **alerta do LinkedIn das 12h44**. **Nenhuma falha de medição:
`NÃO CONFERIDO` = 0 na varredura do Workday e na sondagem do Lever.**

**Quebra por disciplina do que apareceu:** 2 de personagem/modelagem dentro do escopo (Eyeline
Seoul `JR40923` e `JR40941`), e as duas **já tinham sido enviadas e confirmadas em 09/09** — o
`dedupe-agora.sh` pegou as duas. O resto foi ambiente, concept 2D ou fora do escopo.

### 3. O achado que muda a varredura daqui em diante

**O Lever tem dois hosts de API e a campanha lia só um.** `api.eu.lever.co` existe, e um token
vivo lá devolve **404** em `api.lever.co` — o mesmo 404 que a varredura vinha lendo como "essa
casa não tem quadro". Quatro dos 20 quadros de Lever da campanha existem **só** no host europeu,
e um deles é a **Frontier**, a casa cuja vaga você mandou à mão em 10/09 depois de ela chegar
pelo alerta do LinkedIn. Agora dá para dizer por que ela nunca apareceu na varredura.

---

## 🔎 RODADA DE CAÇA DE 13/09 às 01h45 UTC (Jhon B) — **FILA NOVA: ZERO, e o zero está medido**

**Nada novo para você fazer nesta seção.** Ela existe por duas razões: para o número do zero
ficar escrito, e porque a rodada achou **um erro de registro que valia uma candidatura repetida**.

### ⚠️ NÃO REAPLICAR NA BLUEHOLE: as duas vagas de personagem JÁ FORAM ENVIADAS em 07/09

O Joe listou em 12/09, às 22h, as duas vagas de personagem da **Bluehole Studio (KRAFTON, Pangyo,
Coreia do Sul)** como *"não registradas em lugar nenhum do repositório"*, e o maestro fechou a
medição de idioma às 22h40 deixando-as *"na fila, para o Vini decidir"*. **As duas já tinham sido
enviadas cinco dias antes**, e a prova é o recibo da própria casa na caixa de entrada:

| Requisição (Greenhouse) | Vaga | Recibo de `career@bluehole.com` |
|---|---|---|
| `8517790002` (`internal_job_id` 6395150002) | 3D Character Artists (Lead / Senior) — Project V | **07/09, 05h32** |
| `8520212002` (`internal_job_id` 6386636002) | 리드 캐릭터 아티스트 (Lead Character Artist) — TERA2 | **07/09, 05h38** |
| `8517791002` | 3D Environment Artists (Lead/Senior) — Project V | **08/09, 07h31** |

A terceira linha contraria o painel, que ainda registra a `8517791002` como *"requisição livre e
não enviada por decisão escrita"*: ela foi enviada no dia seguinte à decisão e o registro nunca
foi atualizado.

**Por que o dedupe deixou passar:** `grep -i bluehole enviados.csv` devolve **zero**. As três
candidaturas existem, confirmadas por email, e **nenhuma virou linha no `enviados.csv`** — é a
mesma falha da Stunlock, de 11/09, e ela reaparece porque arquivo não é log. Quem resolveu foi a
caixa de entrada. **`enviados.csv` é do Jhon A e eu não o toquei**; a correção da planilha de
envios fica para ele, com os dados acima já apurados.

### O que foi varrido nesta rodada, fonte por fonte, e o que cada uma devolveu

| Fonte | Volume medido | Da disciplina no escopo | Novo |
|---|---|---|---|
| **Grupo Disney** (`ronda-disney.sh`, os dois sites) | 12 consultas responderam, 12 IDs no ar | 12 | **0** |
| Workday, **28 quadros** de 20 locatários (o `robots.txt` de cada um) | 13 termos por quadro | 8 acertos de título | **0** |
| DreamWorks/NBCU, 4 tokens SmartRecruiters | `NBCUniversal3` 383 vagas + `NBCUniversal1` 7 | 4 | **0** |
| Paramount/Skydance (Lever `skydance`) | 28 anúncios | 7 | **0** |
| **Busca global do Workable** (fonte nova, ver abaixo) | 1.047 anúncios únicos, 14 termos | 22 | **0** |
| **Busca global do SmartRecruiters** (fonte nova) | 551 anúncios únicos, 14 termos | 2 de jogos | **0** |
| Planilha da comunidade (regra 16) | 1.396 linhas desde 19/08 | 42 | **0** |
| Alertas de vaga no Gmail (EUA e Canadá, 12/09) | 9 vagas | 4 | **0** |
| **Personio** sondado com 9.643 tokens | 46 quadros vivos | 1 | **0** (Filipinas) |
| **JazzHR** sondado com 9.643 tokens | 41 respostas, 15 quadros vivos | 0 | **0** |

**Quebra de disciplina da rodada: 0 de personagem, 0 de ambiente.** Não é "só sobrou ambiente" —
não sobrou nada, e o estoque dos quadros conhecidos segue seco pelo quarto dia.

### Os três descartes que valem ficar escritos, com a frase

1. **Razer — Senior Character Designer (6 meses), Singapura**, `JR2026007640`. Singapura está no
   escopo e o título casa, mas o corpo é **direção criativa de conceito**, não modelagem:
   *"Directs the full visual pipeline from concept art through animation to marketplace skins"* e
   *"This is a review and direction role, not hands-on"*. Concept e character design 2D estão na
   lista de descarte. Some-se *"Posted 30+ Days Ago"*.
2. **Cloud Imperium Games** — o quadro irmão `broadbean_external`, que a campanha nunca tinha
   lido, tem quatro vagas com "personagem" no título (Montréal e Manchester) e **as quatro são
   `Character Concept Artist` ou `Character Producer`**: conceito 2D e produção, as duas fora.
3. **Chimera Entertainment — 3D Artist Generalist, Modelling & Texturing** (único acerto de
   título em 46 quadros do Personio): o posto é em **Cebu, nas Filipinas**, fora do recorte
   geográfico, e é freelancer.

---

## ~~🤖 PRONTA PARA DISPARO AUTOMÁTICO (entrada nova de 12/09, 19h55, Jhon B): Blizzard Entertainment — **Character Artist, StarCraft**, Irvine CA — requisição `R028136`~~ — **ENVIADA em 12/09**

> Candidatura confirmada por três provas: o texto na tela, a linha `Under Review · September 12, 2026`
> na própria lista do Workday da Blizzard, e o email de recibo cerca de uma hora depois nomeando o cargo.
> Registrada em `enviados.csv`. A ficha abaixo fica só como histórico.

**Anúncio (fonte oficial, ATS):**
https://xboxgaming.wd1.myworkdayjobs.com/Blizzard_External_Careers/job/Irvine---Blizzard---Blizzard-Way/Character-Artist---StarCraft---Irvine--CA_R028136

| | |
|---|---|
| Requisição | **`R028136`** (é o `jobReqId` do Workday, não id de vitrine) |
| Quadro | Workday, locatário `xboxgaming`, pod `wd1`, site **`Blizzard_External_Careers`** |
| Local / regime | Irvine, CA · **Full time** · híbrido (*"hybrid work week, with a mix of work-from-home and on-site days, based out of our Irvine studio"*) |
| Data no corpo | `Date Posted` do Workday = **2026-09-12**, "Posted Today" |
| Faixa publicada | **USD 30,47 – 56,35 por HORA** |

### Por que ela é dele, com a frase colada

É **personagem puro**, não é modelagem genérica:

> *"you should have extensive experience working with **modeling, sculpting, and texturing** tools
> to achieve **photorealistic characters**, weapons, and props. Additionally, you should have
> expertise in **human and creature anatomy**, hard surface modeling, and Unreal Engine 5"*

> *"Contribute to the creation of high-quality, detailed 3D models from **realistic humans and
> creatures** to vehicles, weapons and props."*

Pede **5+ anos** (ele tem 10+), **Maya, ZBrush, Substance Painter, Photoshop**, e dá pontos extras
por *"Marvelous designer and **hair systems**"*, que é o grooming dele. Mentoria de juniores está
nas responsabilidades, e liderança se responde **sim**.

### Régua de veto, termo a termo, no texto INTEGRAL baixado pela API (não na listagem)

Baixei `wday/cxs/xboxgaming/Blizzard_External_Careers/job/...` (7.942 caracteres) e busquei os vinte
termos mais os idiomas. **Nenhum veto escrito.** Os acertos, classificados um a um:

| termo | frase literal | veredito |
|---|---|---|
| `eligib` | *"Subject to **eligibility** requirements, the Company offers comprehensive benefits"* | benefício, **não** é autorização |
| `eligib` | *"**Eligibility** to participate in these benefits may vary for part time and temporary full-time employees"* | benefício |
| `eligib` | *"employees in this role may be **eligible** for incentive compensation"* | remuneração |
| `relocat` | *"If the Company requires that you move geographic locations for the job, then you may also be eligible for **relocation assistance**"* | **sinal POSITIVO**, apoio a realocação por escrito |
| `only` | *"**Only** online artwork submissions will be accepted"* | portfólio |
| `only` | *"our ability to build immersive and innovate worlds is **only** enhanced by diverse teams"* | texto institucional |

**Zero ocorrência** de `authoriz`, `sponsor`, `work permit`, `visa`, `citizen`, `must be based`,
`based in`, `only from`, `LMIA`, `days a week`, `days per week`, `days in the office`, `resident`,
`located in`, `unable to support`, `no relocation`, `within the`, nem de idioma local.

### Dedupe — feito, e ele salvou meia candidatura

`sh automacao/dedupe-agora.sh "R028136" "Blizzard"`

1. **`R028136` é inédito** nos quatro arquivos.
2. **A CASA não é inédita, e é aqui que estaria o erro:** a requisição **`R027817`, Lead Character
   Artist – Overwatch**, do mesmo quadro e da mesma cidade, foi enviada em **02/09 às 23h32** e
   **RECUSADA HOJE, 12/09 às 08h17**, por `activision@myworkday.com` (thread `1a094b171fb89954`).
   São **requisições diferentes, times diferentes** (StarCraft × Overwatch) e a StarCraft nasceu
   hoje. **A Overwatch não se toca.**
3. Gmail conferido **por janela de tempo** (`Blizzard newer_than:3d`): a única mensagem é a recusa
   acima. Nenhum envio nosso à Blizzard hoje.

### Comando exato de disparo

```
cd /home/user/apply && sh hb_run.sh wd_geral.js xboxgaming.wd1.myworkdayjobs.com Blizzard_External_Careers "/job/Irvine---Blizzard---Blizzard-Way/Character-Artist---StarCraft---Irvine--CA_R028136" blizzard-starcraft ENVIAR
```

Sem `ENVIAR` ele roda seco (preenche, printa e lê de volta). O locatário `xboxgaming` **já tem
conta criada** desde a candidatura de 02/09, então o fluxo é de login, não de cadastro — e vale a
armadilha 7 do `wd_geral.js`: o pêndulo Create Account / Sign In só terminou de trocar quando o
campo `verifyPassword` some.

### Pretensão, pela regra de 04/09

Faixa publicada existe, então **pede-se a base dela: USD 30.47 por hora**, com a abertura padrão
*"Aligned with the posted range for the role, at the lower end."*

### Ressalvas honestas, que enfraquecem a ficha

1. **A faixa é HORÁRIA**, e faixa horária costuma marcar vínculo horista ou por projeto. O anúncio
   diz `Full time` e lista benefícios de efetivo, mas a moeda do anúncio é hora. **Efetivo é o que
   sustenta patrocínio**; se isso for temporário, o valor para visto cai muito. Não dá para
   resolver pelo texto: é pergunta para a primeira conversa.
2. **Ela é dos Estados Unidos e a casa não promete patrocínio.** Não há `sponsor` nem `visa` no
   texto — o que existe é *relocation assistance*, que é outra coisa. Ausência de veto não é
   promessa de visto.
3. **Cadência:** a casa recusou ele hoje de manhã em outra requisição. Isso não proíbe esta, e a
   regra de cadência é sobre **envios nossos** (hoje foram zero para lá), mas é honesto dizer que
   é o mesmo recrutamento olhando o mesmo nome na mesma semana.

### O buraco de cobertura que achou isto, e ele vale mais que a vaga

O `BRIEF-JHON.md` diz, desde 06/09, que *"o quadro certo é `xboxgaming.wd1.myworkdayjobs.com/External`"*
e que nele não há vaga da disciplina no mundo inteiro. **Está certo sobre o `External` e errado
sobre a casa.** O `robots.txt` do mesmo locatário lista **sete sites**, e os quadros grandes de arte
estão nos outros: `Blizzard_External_Careers` (50 vagas), `King_External_Careers` (16),
`CentralTech`, `DL_external`, `SS_external`, `HOH`. As **quatro** vagas de arte da Blizzard —
incluindo as duas de personagem — vivem num site que a campanha nunca abriu.

> **Regra: em Workday, leia o `robots.txt` do locatário antes de dizer que a casa não tem vaga.**
> Ele lista os sites, é uma requisição, e é a mesma lição do `disneycareerdc`.

## 🖐️ ITEM DE MÃO NOVO — NETFLIX ANIMATION STUDIOS, **Character Modeler** (15/09, 01h30)

**É o título literal do cargo dele, e são DUAS requisições irmãs, as duas inéditas na campanha.**

| | Vancouver | Sydney |
|---|---|---|
| Requisição | `790318470000` | `790318471349` |
| Link | https://explore.jobs.netflix.net/careers/job/790318470000 | https://explore.jobs.netflix.net/careers/job/790318471349 |
| Faixa publicada | **CAD 68.000 a 145.000** (total, sem stock) | não publicada |
| Regime | híbrido, mínimo 3 dias no escritório | híbrido, mínimo 3 dias no escritório |

**Dedupe feito em 15/09 às 01h20:** zero ocorrência das duas requisições em `enviados.csv`,
`automacao/processados.csv`, `docs/index.html` e `automacao/FILA-DO-VINI.md`, e **zero na caixa** —
a busca `Netflix newer_than:14d` só mostra o recibo da *Visual Development Artist- Ink* (04/09) e a
recusa da *CG Experimental Artist* (07/09). **Requisições inéditas.**

**Régua de veto rodada termo a termo no anúncio inteiro (3.524 e 3.170 caracteres):** ZERO acerto em
`authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`, `citizen`, `resident`,
`right to work`. O único acerto é `days a week`, e ele é **restrição de presença, não veto**:
*"Hybrid Role (Minimum of 3 days a week in the office)"*.

**Por que ela é a melhor da semana, com a frase deles:** *"We are looking for Character Modeling
Artists who love building appealing stylised characters from strong proportions and clean forms to
production-ready topology and UVs."* E pedem, junto da candidatura, *"Turntables, with wireframes,
of character and creature models"*, que é o que o ArtStation dele já mostra.

### POR QUE FICOU NA SUA MÃO, e eu CLIQUEI antes de dizer isso

O formulário **preenche 100% pela automação** e eu cliquei em SUBMIT APPLICATION. O servidor
recusou: `POST /api/application/v2/submit` devolveu **400** com
`{"message": "Please try again later"}`. É o reCAPTCHA invisível do Eightfold recusando IP de
datacenter, a mesma parede medida em 06/09 e **remedida hoje, 15/09**. Não há tela de captcha
visível para resolver: a recusa é silenciosa e vem do servidor. **Nada foi enviado.**

### O formulário campo a campo, já medido — é só repetir do seu IP

1. Abra o link, **Apply**, anexe `Vini_Cavalcanti_CV.pdf`.
2. Vai subir a janela **Candidate Privacy**: clique em **I ACKNOWLEDGE** (sem isso nada abaixo é clicável).
3. Contato: email `contact@vinicavalcanti.art` · First `Vini` · Last `Cavalcanti` · País `Brazil` ·
   Estado `Pernambuco` · Cidade `Olinda` · código do país **🇧🇷 (+55) Brazil** e o telefone **só com
   os dígitos** (o número está no documento privado do Drive, não neste arquivo).
4. Additional Documents: anexe `carta_nas_charmod.pdf` (já escrita, específica desta vaga, com a
   situação de visto na primeira linha) e no campo **URL** ponha
   `https://www.artstation.com/viniciuscavalcanti`.
5. Application Questions, as três, e a terceira é a que não pode errar:
   - *Are you currently working for Netflix as a contractor?* → **NO**
   - *Have you worked for Netflix or any of Netflix's subsidiaries in the past?* → **NO**
   - *Do you require sponsorship to legally work in the job location?* → **YES** (é a verdade)
6. **SUBMIT APPLICATION**. A mensagem de sucesso desta casa é, literal:
   *"Thank you for your interest! Your application has been received."*

**Dica medida:** a terceira pergunta não abre a lista no clique, porque o menu da pergunta anterior
ainda está fechando. Se travar, clique fora, volte nela e use a **seta para baixo** do teclado.

**Depois de mandar a de Vancouver, mande a de Sydney:** é o mesmo formulário com outro `pid`, e a
Austrália é a rota de visto mais acessível do escopo.


## 🖐️ À MÃO, AGORA (entrada nova de 12/09, 15h30): Stellar Creative Lab — **Modeling Artists (Mid & Senior)**, Vancouver — só falta a caixa do captcha

**Link:** https://stellarcreativelab.applytojob.com/apply/zK3Gust365/Modeling-Artists-Mid-Senior
Vaga **nova**, saiu no seu alerta do LinkedIn de hoje às 12h44 (Character Art, Canadá). Vancouver
BC, efetiva, híbrido flexível, e o projeto é **uma série premium de streaming para a Marvel
Animation**. Faixa publicada **CA$70.000–85.000**. Quadro JazzHR, requisição `zK3Gust365`.

**Por que ela é sua:** o corpo põe personagem em primeiro lugar, *"building **characters**,
sprawling sets, vehicles, or organic hard-surface props"* e *"including **characters**, sets,
props, vehicles"*, e as Core Tools são **Maya, ZBrush e Photoshop**.

**A parede é o reCAPTCHA v2 de caixa** (rótulo *"Human Check\*"*). **Eu cliquei em Submit
Application e medi**, não supus: **zero POST para o domínio deles** (os nove POST que saíram são
todos do New Relic, `bam.nr-data.net`), o formulário continuou cheio, o token
`g-recaptcha-response` ficou com comprimento zero e o site escreveu em vermelho **"Please
verify."** ao lado da caixa *"I'm not a robot"*. Print em
`/home/user/apply/result_stellarmod.png`. **No seu navegador isso é um clique.**

**O formulário inteiro já foi preenchido e conferido campo a campo aqui, duas vezes** (antes e
depois do clique). Basta repetir:

| Campo | Valor |
|---|---|
| First Name / Last Name | `Vini` / `Cavalcanti` |
| Email Address | `contact@vinicavalcanti.art` |
| Phone | **campo único, sem seletor de país** → formato internacional sem espaço (doc privado do Drive, `CAMPANHA - dados pessoais dos formulários`) |
| Address / City / State / Postal | endereço residencial do mesmo doc privado; City `Olinda`, State `Pernambuco` |
| Resume | `Vini_Cavalcanti_CV.pdf` |
| *"link to your portfolio or reel"* | ArtStation, LinkedIn e site, mais a situação de visto **declarada na mesma submissão** (texto abaixo) |
| *"Are you legally entitled to work in Canada?"* | **No** |
| *"What is your employment eligibility?"* | **Non-citizen seeking work authorization** |
| *"Are you currently residing in B.C.?"* | **No** |
| *"...familiar with the salary range stated in the job listing?"* | `Yes. I am familiar with the posted range of CAD 70,000 to 85,000 and I am aligned with it, at the lower end of the band.` |
| *"Have you previously worked for Stellar Creative Lab?"* | **No** |
| Human Check | **a caixa do reCAPTCHA — é a única coisa que falta** |

O texto do campo de portfólio está pronto em `/home/user/apply/ans_stellar_mod.json`, chave
`#resumator-questionnaire-q278966`: ele abre com os links e **diz a verdade sobre o visto na
mesma tela em que as três respostas de elegibilidade aparecem**, que é a regra que você definiu
hoje. Nenhuma caixa foi marcada escondendo nada: aqui não foi preciso, porque o menu **deles**
já oferece a opção honesta.

**Duas coisas que quase pareceram veto e não são:**
1. A lista de requisitos traz *"Eligibility: Legally eligible to work in British Columbia,
   Canada"*, mas o texto renderizado termina com *"**All qualified candidates are encouraged to
   apply**, though priority will be given to BC Residents, Canadians and Canadian Permanent
   Residents"* — é **preferência declarada**, não proibição, e o próprio menu do formulário tem
   a opção de quem precisa de patrocínio.
2. A campanha já tocou esta casa em **31/08**, mas foi **porta de entrada** (Production
   Coordinator), requisição diferente e fora da disciplina. Não é candidatura repetida.

**Ressalva honesta de salário:** a base da faixa publicada (CA$70.000) fica **abaixo** do piso de
referência da campanha para o Canadá (CA$80.000). Segui a regra 1 do briefing, que manda pedir a
**base da faixa publicada** e vence a estimativa; se você preferir pedir 80.000, é trocar uma
linha do campo de salário.

**E tem a irmã, que é sua também:** **Surfacing/Texture Artists (Mid & Senior)**,
`j7JwsT6x1k`, mesma série e mesmo formulário (conferido por curl: mesmos seis ids de pergunta,
mesmo captcha) — *"creating the look, feel, and texture of **characters**, environments, and
objects"*, estética *painterly*. **Não foi tentada hoje de propósito, por cadência de uma casa
por dia. Ela vale a partir de 13/09**, com este mesmo dossiê.

---

## 🖐️ À MÃO, AGORA: Lightfox Games — Senior 3D Artist, Vancouver — **só falta o captcha**

**Link:** https://www.lightfoxgames.com/careers/?id=senior-3d-artist-vancouver&src=linkedin
Vaga que o próprio Vini mandou em 12/09. Vancouver BC, híbrido ~50% presencial, faixa publicada
**CA$95.000–120.000**, jogo mobile não anunciado de IP e publisher grandes. Encaixe real:
*"Create high-quality 3D assets including **characters**, props, and weapons"*, personagem
primeiro na lista, e *"experience with stylized art directions"* em nice-to-have.

**A parede é o Cloudflare Turnstile** (*"Please complete the verification challenge."*, token
vazio). Captcha de desafio não se burla, e ele reprova o IP de datacenter, não a candidatura.
**No navegador dele passa** — foi assim que nove formulários "travados" saíram em dezessete
minutos em 10/09.

| Campo | Valor |
|---|---|
| NAME | `Vini Cavalcanti` |
| EMAIL | `contact@vinicavalcanti.art` |
| RESUME | `Vini_Cavalcanti_CV.pdf` |
| PORTFOLIO / REEL URL | `https://www.artstation.com/viniciuscavalcanti` |
| LINKEDIN URL | `https://www.linkedin.com/in/vinicavalcnti/` |
| As DUAS caixas de acknowledgment | **marcadas** |
| Data de início | **12/10/2026** (um mês; trocar se o prazo real dele for outro) |
| `company` (campo sem rótulo) | **VAZIO** — é honeypot anti-robô |

**No campo ANYTHING ELSE vai o texto da constante `NOTA` em `/home/user/apply/lf_aplica.js`**,
que abre declarando o visto na primeira linha. **Esse texto é a razão de as caixas poderem ser
marcadas:** a situação real chega escrita na mesma submissão, então nada fica escondido e o
recrutador lê o fato em vez de descobrir numa call.

**TRÊS PORTÕES, e os dois primeiros já estão resolvidos no script** — registrados porque a
sequência enganou duas medições minhas: (1) as caixas de acknowledgment; (2) o campo
*"WHAT'S THE SOONEST YOU'D BE AVAILABLE TO START THIS POSITION?"*, que **só renderiza depois**
das caixas e **não é `<input>`**, é `button.datepick-day[data-date]` num widget de div; (3) o
Turnstile, que é o único que sobra.

**Rota paralela, já pronta:** rascunho para `careers@lightfoxgames.com` com assunto próprio
nomeando a vaga (precisa do `enviarAssuntoProprio()`). E **Anthony Tewes, Head of Art**, sem
email publicado, é contato de LinkedIn que só o Vini pode fazer.

---


> ## 🎯 ENTRADA NOVA DE 12/09, 11h — E ELA É A PRIMEIRA DA FILA HOJE
>
> **Absurd Ventures — CHARACTER ART LEAD — Santa Monica, Califórnia.** Publicada **ontem, 11/09 às
> 19h11 (hora de Nova York)**, requisição `5236256007`. É **vaga NOMEADA de personagem** numa casa
> grande nova (a de Dan Houser), com **faixa publicada de USD 150.000 a 185.000**, régua de veto
> limpa e **candidatura possível pela automação** (o Greenhouse dessa casa já aceitou duas
> candidaturas nossas ontem). O dossiê inteiro é a **entrada nº 51** deste arquivo.
>
> **Não confunda com as duas de ontem:** o que saiu em 11/09 foram as espontâneas
> `4141408007` (General Game Development, 19h04) e `4141404007` (Animated Series, 21h22). Esta é
> **outra requisição, e é nomeada**. Conferido no Gmail: nenhum recibo cita Character Art Lead.

> ## SE VOCÊ SÓ TIVER DEZ MINUTOS HOJE, gaste nestas três
>
> O arquivo cresceu muito em 09/09 e você disse que está sem tempo. Então a ordem, com o motivo
> de cada uma em uma linha:
>
> 1. **Flaming Fowl Studios — Lead 3D Artist.** É a mais barata de todas: **o rascunho já está no
>    seu Gmail**, é só disparar. É o único anúncio do dia que convida candidatura de qualquer lugar
>    do mundo por escrito, e a porta é email, então não tem captcha para atravessar.
> 2. **Fenris Creations — Register Your Interest.** É a CCP do *EVE Online*. O processo seletivo
>    deles tem um estágio chamado *"Relocation and Benefits Chat"* e o formulário pergunta se você
>    precisa de patrocínio de visto. Sem captcha, e **todas as respostas já estão decididas na
>    entrada** — é copiar e clicar. **Confira com o olho o campo de localização: escolha `Other`.**
> 3. **Skydance Animation Madrid — Environment Surfacing Artist `c5793932`.** É Paramount (a política
>    de privacidade do anúncio aponta para `privacy.paramount.com`), é surfacing estilizado com
>    Substance 3D Paint, e é a requisição de topo aberta dessa função depois que a Senior morreu hoje.
>    Custa o hCaptcha de imagem do Lever, e o dossiê está pronto.
>
> Depois dessas três, a próxima é a **Ubisoft Montréal `REF31656C`**, que apesar de Quebec não pede
> francês em lugar nenhum do anúncio.


> ## ✅ NOVE JÁ SAÍRAM, ENTRE 03h53 e 04h10 UTC DE 10/09. NÃO REFAÇA NENHUMA DELAS.
>
> Li os recibos na caixa antes de escrever isto, um por um. Todas de personagem, e todas eram
> entradas que este arquivo listava como travadas por captcha:
>
> | Estúdio | Vaga confirmada no recibo | Hora UTC | Quem confirmou |
> |---|---|---|---|
> | Behaviour Interactive | Senior 3D Character Artist, *Dead by Daylight* | 03h53 | Lever |
> | Frontier Developments | Experienced Character Artist | 03h57 | Lever EU |
> | Lighthouse Games | Lead Character Artist | 04h00 e 04h04 | Workable + John Chalkley, Head of Talent Acquisition |
> | Fenris Creations | Register Your Interest, departamento Art | 04h10 | Pinpoint |
> | Ubisoft Massive | Lead Character Artist *[The Division 2]*, `REF31739L` | 04h03 | SmartRecruiters |
> | Offworld Industries | 3D Character Artist | 04h04 | BambooHR |
> | People Can Fly | **o recibo não nomeia a vaga** | 04h07 | SmartRecruiters |
> | Avalanche Studios Group | Lead Character Artist | 04h08 | Lever |
> | TTK Games AB | Character Artist (vaga `561860`) | 04h09 | Pinpoint |
>
> **A única com ressalva é a People Can Fly:** o recibo confirma que uma candidatura entrou, mas
> não diz qual requisição a recebeu, e a casa tem duas entradas vivas no painel. Antes de tocar
> nela de novo, abra o *Access My Application* do próprio recibo. Nas outras oito, reaplicar só
> gera duplicata, que é um erro que esta campanha já cometeu três vezes.
>
> **O que isso prova sobre a fila:** a parede nunca foi o formulário, foi o captcha reprovando o IP
> da automação. As nove atravessaram no seu navegador em dezessete minutos.



**44 vagas VIVAS em 43 entradas numeradas, tempo total estimado cerca de 2h20, todas com
formulário e nenhuma por email.** São 43 e não 42 porque a entrada nº 2 carrega DUAS requisições
da Netflix, a 2a de Sydney e a 2b de Vancouver. As cinco entradas que saíram continuam no arquivo
com o cabeçalho RISCADO e o motivo literal; o texto antigo de cada uma ficou logo abaixo, rebaixado
a subtítulo, para não ser confundido com entrada viva.

**REVALIDAÇÃO DE 08/09 À NOITE, as 46 entradas conferidas uma a uma na fonte oficial de cada ATS,
com a régua nova de dezessete termos. Resultado: 35 seguem, CINCO SAÍRAM, seis mudaram, e duas
requisições novas da Netflix entraram no lugar da que morreu.**

**As cinco que saíram, para você não perder tempo com elas:** nº 2 Netflix Head of Characters
(deslistada, e a página continua respondendo 200, que é a armadilha), nº 13 Asobo (veto de francês
escrito no anúncio), nº 38 DreamWorks VisDev (`active: false`, "This job has expired"), nº 41
Quantic Dream (duplicata exata da nº 27, mesmo uuid) e nº 44 Behaviour *7 Days to Die* (o Gmail
mostra recibo do Lever de 30/08: **já foi enviada**). Todas continuam no arquivo, riscadas e com o
motivo literal, para ninguém reabrir.

**As mais baratas:** nº 33 Gigantic Duck, **40 segundos**, remota e efetiva, campo a campo medido;
e a dupla da TTK Games, nº 43 e nº 46, que são **o mesmo formulário** e saem juntas em três minutos.
Ordem: 1º realocação para Canadá e Europa, 2º remoto em EUA/Canadá/Europa, 3º o resto do escopo.
**As três primeiras:** Behaviour *Dead by Daylight* (Senior Character, Montréal) · Netflix Animation Studios (Head of Characters, Vancouver, faixa publicada CAD 204.000–279.000) · Behaviour (Senior Character, projeto não anunciado).

## ENTRADA NOVA DE 09/09 ÀS 22h50 — FENRIS CREATIONS (a CCP do EVE Online), TRÊS MINUTOS SEUS

**É a casa com o sinal de patrocínio mais forte que a campanha achou hoje**, e o formulário não
tem captcha nenhum. Eu não consegui fechar o envio e digo por quê logo abaixo, mas **todas as
respostas já estão decididas e as listas reais estão medidas**, então para você é copiar e clicar.

**Por que ela importa.** É a CCP Games renomeada, dona do *EVE Online*, independente de novo desde
maio de 2026, com sede em Reykjavík e estúdios em Londres e Xangai. O anúncio de vaga deles lista
**Relocation Package** entre os benefícios, o processo seletivo tem um estágio chamado literalmente
**"Stage 5: Relocation and Benefits Chat"**, e o formulário pergunta, com todas as letras,
*"Would you need a VISA sponsorship in order to relocate for the role?"*, explicando que
*"we will review your application to see if we would legally be able to acquire a VISA sponsorship"*.
Casa que pergunta isso é casa que patrocina.

**A porta:** https://careers.fenriscreations.com/register-your-interest/new (banco de talentos, que
conta como candidatura pela regra da campanha). **Sem captcha.**

**As respostas, todas verdadeiras e já conferidas contra as listas reais do formulário:**

| Campo | Resposta |
|---|---|
| `What is your current location?` | **Other** (as opções são Iceland, United Kingdom, EEA/EU, USA/Canada, Asia, Other) |
| `Would you need a VISA sponsorship…?` | **Yes** |
| `Are you a...` | **None of the above?** (as outras são Current Employee, Former Employee, Current or former EVE Online Player, Current or former intern/contractor) |
| `Where did you hear about this position?` | **Fenris Creations Website** |
| `Are you willing to relocate for the role?` | **Yes** |
| `Locations` | **Reykjavík** · `Departments` | **Art** |
| `Gender` | Prefer Not To Say |
| Aceite obrigatório | *Allow us to process your personal information* |

O texto do **Personal Summary** (1.441 caracteres, já escrito) está em `automacao/ans_fenris.json`,
no campo `#personal-summary` — é só copiar.

**Por que eu não fechei, sem maquiar.** O envio saiu e o servidor recusou com
`Answers boolean answer can't be blank`. A causa é a pergunta de visto: ela é **condicional**, só
aparece depois que a localização é respondida, e é do tipo *boolean*, não lista. Não consegui
desenhar esse clique de forma estável dentro da rodada. **Nada ficou registrado do lado deles**,
porque a validação barrou antes de gravar.

**E um erro meu que você precisa saber, porque quase virou resposta falsa:** eu pedi *Other* na
pergunta de localização e o clique caiu em **USA/Canada**. O log dizia "escolhi Other" porque
olhava o texto da opção que eu mandei clicar, e não o que o controle passou a mostrar. Se o envio
tivesse fechado, o estúdio teria lido que você mora nos Estados Unidos ou no Canadá. **Confira esse
campo com o olho antes de enviar.**

**A única vaga de arte aberta hoje lá eu descartei, com a frase colada:** a `Cinematic Artist` é
*"creating trailers and promotional video content"*, *"film language, pacing, and visual
storytelling"* e *"UE5 cinematic shot creation"*, no departamento de **Marketing**. É
cinematografia e edição, não modelagem. Por isso a porta certa é o banco de talentos.

---

## ENTRADA NOVA DE 09/09 ÀS 21h30 — DUAS DO LEVER, e uma delas é da Paramount

O Lever destas duas casas já foi medido **com clique de verdade** nesta campanha: o hCaptcha é de
**desafio de imagem** e aparece **depois** do Submit. Não abri navegador de novo justamente porque
o histórico da casa já dizia isso — foi o teste de dedupe pelo NOME da casa que economizou a rodada.

1. **Skydance Animation Madrid — `Environment Surfacing Artist`** · Madri, híbrido
   · `c5793932-893f-418a-a24a-7749fcf1c90e` · https://jobs.lever.co/skydance/c5793932-893f-418a-a24a-7749fcf1c90e/apply
   **É requisição INÉDITA**, diferente das duas que você já tem na fila (a `90d2f2b7` Senior e a
   `f3ee86d4` Lead). Pede *"Paints **stylized** textures… using **Substance 3D Paint**"* — surfacing
   estilizado, o centro do seu portfólio. **E vale a regra 14:** a política de privacidade do anúncio
   aponta para `privacy.paramount.com`, ou seja **a Skydance Animation está sob a Paramount**.
   A régua deu quatro acertos e os quatro são falso positivo, dois deles no aviso antifraude do
   próprio anúncio.

   **CORREÇÃO DAS 21h45, e ela muda a recomendação que eu tinha acabado de escrever.** Eu disse
   aqui que, se fosse mandar uma só, a do seu nível seria a `90d2f2b7` (a Senior). **A `90d2f2b7`
   MORREU: `api.lever.co/v0/postings/skydance/90d2f2b7…` responde 404 hoje.** O quadro inteiro da
   Skydance foi listado (28 vagas) e a família de surfacing de Madri **continua viva** — Lead,
   Junior, os dois Trainee, Environment Modeling e Senior Grooming TD. Não foi a casa que fechou,
   **foi o nível SENIOR desta função que sumiu.** Então **a `c5793932` acima passou a ser o topo
   aberto da função**, e é nela que você manda.

2. **Jam City — `Level Design Artist`** · São Francisco, presencial ·
   `787abb3b-1009-42f3-bf82-9846dff0e646` · https://jobs.lever.co/jamcity/787abb3b-1009-42f3-bf82-9846dff0e646/apply
   *"**Edit or create high-quality and optimized 3D environments and props**"*, Maya, Unity, PBR —
   é level art **com** modelagem. **Faixa publicada USD 90.000–110.000**, então a pretensão é a base,
   USD 90.000, com a frase de alinhamento. **Ressalvas honestas:** presencial em São Francisco e o
   produto é jogo mobile de objetos escondidos. Está aqui porque régua e dedupe estão limpos, não
   porque eu a recomende acima das outras.

---

## ENTRADA NOVA DE 09/09 ÀS 21h — DUAS DO WORKABLE, e as duas são boas

O Workable é parede medida com clique real duas vezes (Lighthouse em 07/09, One Of Us em 08/09):
o **Turnstile aparece DEPOIS do Submit**, o botão trava em "Submitting…" e o POST devolve **412
com `x-ts: 0`**. Não é suposição e não se burla. As duas abaixo passaram a régua de vinte termos
com os únicos acertos sendo falsos positivos catalogados, e o dedupe com zero.

1. **Sperasoft / AMC Studio — `Lead Props/Environment 3D Artist`** · Bucareste, Romênia
   (telecommute) · uuid `532f4b03-d196-42bf-bb46-72979c256131`
   · https://jobs.workable.com/view/bgM2Eip6fX6RA8zmRDZV2K/
   Pede *"expert-level skill in **hard-surface and organic props**"*, *"modeling and texturing
   workflows (**PBR**)"*, ZBrush e Substance, *"from **stylized to photorealistic**"*. Idioma: só
   *"Strong English"*. **Detalhe que vale saber antes de clicar:** a campanha já escreveu para a
   Sperasoft por email em 26/08 e **foi recusada** — mas a própria recusa convidou a acompanhar as
   vagas no site, então a porta não está fechada. **Ressalva:** é cargo de liderança, pede dois
   anos como lead. **Tem gêmea em Varsóvia e é a MESMA vaga: mande uma.**

2. **Magic Media — `Senior 3D Generalist Artist`** · remoto Polônia · uuid
   `76cde5c1-4b15-471c-9e2e-358ec9d842fc` · https://jobs.workable.com/view/fETqLf4yCZ6XDqX9KTXYwG/
   **Publicada hoje às 14h35.** Pede *"assets such as **characters or environment props**"* e
   *"models (both **hard surface and organic**) and **textures**"*. **Ressalva:** é generalista, não
   personagem puro, e a mesma requisição está publicada em **seis países** — mande uma só.

---

## ENTRADA NOVA DE 09/09 ÀS 20h — UBISOFT, três vagas, e por que elas caíram na sua mão

**Antes de tudo, a parte que não me favorece: isto já estava escrito.** O painel registra desde
06/09 que *"as duas da Ubisoft esbarram no DataDome"*. Eu gastei uma rodada de navegador para
redescobrir isso porque a caça me entregou as três com "URL de candidatura verificada em HTTP 200"
e eu tratei isso como porta aberta. **A regra que fica: 200 na URL da vaga não é porta verificada —
o dedupe tem que cruzar o histórico da CASA, não só o ID da requisição.** O que a rodada de hoje
acrescenta de verdade é o mecanismo exato, que antes não estava escrito em lugar nenhum.

**A Ubisoft usa**
SmartRecruiters. A página pública da vaga responde 200 normalmente, mas o botão *"I'm interested"*
leva para `jobs.smartrecruiters.com/oneclick-ui/...`, que responde **403** e monta um iframe do
**DataDome** — desafio de arrastar o controle deslizante, com a frase *"Automated (bot) activity on
your network"* e o nosso IP escrito na tela. DataDome está na lista de captcha que não se burla.
**Consequência: Ubisoft, Gameloft e NBCUniversal, as três casas grandes de SmartRecruiters do
painel, só entram pela sua mão.**

As três passaram a régua de vinte termos com **zero acerto** e o dedupe com **zero ocorrência**.
Estão em ordem de quanto encostam no seu portfólio:

1. **Ubisoft Montréal — `Level Artist (Unreal)`** · req `REF31656C` · posting `744000145286834`
   · https://jobs.smartrecruiters.com/Ubisoft2/744000145286834 · publicada 24/08.
   **É a melhor das três.** Apesar de ser Quebec, **não pede francês em lugar nenhum do anúncio** —
   é a diferença literal entre esta e as gêmeas da 2K que eu descartei hoje. E as qualificações
   pedem *"Experience with **modeling, texturing**, lighting, or image processing"*.
   **Ressalva honesta:** o ofício central é montagem e integração em Unreal; a modelagem aparece
   como necessidade a comunicar aos times de arte.

2. **Ubisoft Annecy — `Lead Level Artist (F/M/NB) [AAA Project]`** · req `REF31639U` · posting
   `744000140062829` · https://jobs.smartrecruiters.com/Ubisoft2/744000140062829 · publicada 27/07.
   Num estúdio francês, a única exigência de idioma é *"Fluency in English"* — francês não aparece,
   o que é o oposto de um veto. Pede *"Extensive experience creating environments for video games"*.
   **Ressalva:** é cargo de gestão, com pouca mão na ferramenta.

3. **Ubisoft Montréal — `Senior Level Artist`** · req `REF31781B` · posting `744000145286684`
   · https://jobs.smartrecruiters.com/Ubisoft2/744000145286684 · publicada 24/08.
   **Fica em último por uma frase do próprio anúncio:** *"This position is **not primarily focused
   on creating high-resolution 3D assets or producing full environment models from scratch**."* É
   exatamente o que o seu portfólio é. Régua limpa e dedupe zero são o motivo de estar listada em
   vez de descartada em silêncio — a decisão é sua, com a frase na mão.

**Mande UMA só** (a nº 1, se for escolher pelo meu voto): é uma casa, e a regra de uma candidatura
por casa por rodada vale aqui como vale para as outras.

---

## ATUALIZAÇÃO DE 09/09 À TARDE — três entradas mudaram, e uma delas você ia perder tempo à toa

**nº 7, Avalanche Studios Group (Lead Character Artist, Estocolmo). O motivo do fracasso foi
descoberto hoje, e sem ele você tentaria e desistiria.** O formulário do Lever tem um campo
**Current location** que é autocomplete estruturado: o que vale para o servidor não é o texto
digitado, é a sugestão ESCOLHIDA da lista. A lista vem de uma chamada que o hCaptcha libera, e do
nosso IP ela volta vazia, então o Submit não gera requisição nenhuma e **nenhum erro aparece na
tela**. No seu navegador a lista aparece. Então: digite só `Olinda`, **espere e clique na sugestão**,
e só depois Submit. O resto já está preenchido no dossiê da entrada 7. O currículo já passou pelo
parser do Lever com "Success!".

**nº 43 e 46, TTK Games. Confirmado com navegador de verdade (antes era dedução por cabeçalho):**
a rota do Pinpoint redireciona para `ttkgames.com/careers/` e a página de destino tem ZERO campos.
A casa não usa o formulário do Pinpoint, manda para o site próprio, cujo envio já devolveu
`500 ReCaptcha Failed`. Continua valendo o dossiê, mas pelo site deles.

**Offworld Industries (3D Character Artist, New Westminster, BC) sobe da tabela do fim para entrada
com dossiê completo.** É PERSONAGEM, no CANADÁ, efetiva, faixa publicada **CAD 80.000 a 95.000**, e
o anúncio **não tem veto escrito** (o único acerto da régua é "three days per week" no escritório,
que é presença híbrida). Parede medida com clique, três vezes: reCAPTCHA v2 com desafio de imagem.

Link: https://owi.bamboohr.com/careers/199

**A ORDEM IMPORTA e é o que mais custa tempo aqui:**

1. **Country primeiro, antes de qualquer campo de texto.** Escolha **Brazil**. Com país Canadá o
   campo Province é um menu de províncias; ao trocar para Brazil o BambooHR **troca o elemento por
   um campo de texto livre**. Preenchendo antes, o valor vai para um menu que deixa de existir e a
   província fica vazia sem aviso nenhum.
2. First Name `Vini` · Last Name `Cavalcanti` · Email `contact@vinicavalcanti.art`
3. Phone, Address, City e Postal Code: valores no doc privado do Drive. **Province:** `Pernambuco`
   (campo de texto, depois que o país virou Brazil).
4. **Date Available:** a máscara é **mm/dd/yyyy**. Digitar `2026-10-20` grava `02/dd/yyyy`. Use
   `10/20/2026`.
5. **Desired Pay:** `CAD 80,000 per year, aligned with the posted range for the role, at the lower
   end. Open to aligning with your band for the role.`
6. **Website, Blog or Portfolio:** `https://www.artstation.com/viniciuscavalcanti`
7. **LinkedIn URL:** `https://www.linkedin.com/in/vinicavalcnti/`
8. **Resume:** o formulário tem DOIS campos de arquivo e o **primeiro é o da Cover Letter**. O CV
   vai no segundo, o marcado com asterisco.
9. O campo "Please leave this field blank" é armadilha para robô: **deixe vazio**.

Depois resolva o reCAPTCHA e clique em Submit. Menos de um minuto.

---

Vá de cima para baixo. Cada entrada é autossuficiente: link, parede, campos e textos prontos.
As dez primeiras foram reconferidas no ar hoje, uma a uma, na fonte oficial de cada ATS.

**CORREÇÃO DA NOITE DE 07/09, leia antes de abrir a lista.** Seis entradas saíram desta fila desde a versão da madrugada, porque a medição do dia inteiro as invalidou, e a mais grave era justamente a que estava marcada acima, na versão anterior deste arquivo, como "a segunda coisa a mandar":

- **Ubisoft Montréal, Senior Character Artist (Rainbow Six Siege) — NÃO ENVIAR.** O Vini já se candidatou a esta MESMA requisição (id `744000145282762`, ref `REF31793B`) em 30/08 e foi **recusado em 02/09**. A casa publica o mesmo anúncio com título em francês e em inglês, o que escondeu a duplicata de quem conferiu só pelo título. Dedupe sempre pela referência da requisição, nunca pelo título.
- **DreamWorks Animation / NBCUniversal, as DUAS requisições de Montréal** (Lead Character Artist `744000137526729` e Lead Material Artist `744000137526669`) — o texto integral, buscado na API oficial, diz "**Must be legally authorized to work in Canada**" e "**Must be willing to work in our Montreal office a minimum of 4 days a week**". Ele precisa de patrocínio: não dá.
- **Larian Studios, Character Artist (Open Application) — JÁ ENVIADA.** O Gmail tem o recibo de `no-reply@hire.lever.co`, de hoje às 04h35 UTC, nomeando a requisição.
- **Image Engine, General Application de Assets (Vancouver) — VETO DE RESIDÊNCIA.** O quadro inteiro do BambooHR deles, esta candidatura incluída, escreve "**Candidates are required to be based in British Columbia and eligible to work in Canada**".
- **Prismatic Studios, 3D Character Artist (Auckland) — JÁ ENVIADA E CONFIRMADA hoje** pelo JHON (resposta de rede do próprio formulário, `{"success":true,...}`). De quebra, o próprio anúncio também tem veto: "**you must have the right to work in New Zealand to be eligible for this position**" — então não voltaria a valer o envio mesmo sem a duplicata.

Em troca, a **Netflix Animation Studios (Head of Characters, Vancouver)** subiu da posição 21 para a segunda: revalidada hoje, faixa publicada no próprio anúncio (**CAD 204.000–279.000**), e zero ocorrência de `authoriz`, `eligib`, `sponsor` ou `work permit` no texto integral — nenhum veto escrito, só o híbrido de 3 dias por semana. E entrou uma vaga nova, a **Gameloft Montréal (Candidature Spontanée)**, que declara apoio a realocação por escrito no bloco de benefícios.

**SEGUNDA CORREÇÃO, feita na sequência: saiu a ICON Creative Studio.** Achado na segunda leitura, cruzando com `automacao/RISCO-DUPLICATA.md`: o Gmail tem o email de `notifications@app.bamboohr.com` de **31/08** confirmando candidatura ao **Intermediate Modeling/Texture Artist** da ICON — a mesma e única vaga de modelagem do quadro deles. A entrada que estava nesta fila (posição 9) usava um link diferente do que registrou aquele envio, e por isso passou pela garra sem acusar duplicata. **Fila agora com 39 vagas.** Detalhe de cada corte na seção "O QUE FICOU DE FORA", no fim do arquivo.

---

## COMO USAR ESTE ARQUIVO

Os quatro blocos abaixo se repetiriam em toda entrada, então ficam aqui em cima uma vez só.
Quando uma entrada disser "TEXTO A", volte aqui, copie e cole.

### DADOS FIXOS

| Campo | O que colar |
|---|---|
| First name / Last name | `Vini` / `Cavalcanti` |
| Full name | `Vini Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Telefone | **do documento privado do Drive, CAMPANHA - dados pessoais dos formulários**. Com seletor de país ao lado: escolha `BR (+55) Brazil` primeiro e digite **só os dígitos**, sem +55, sem espaço e sem hífen |
| Endereço, CEP, província | **do documento privado do Drive, CAMPANHA - dados pessoais dos formulários** |
| Cidade / Estado / País | `Olinda` / `Pernambuco` / `Brazil` |
| LinkedIn | `https://www.linkedin.com/in/vinicavalcnti/` |
| Portfólio | `https://www.artstation.com/viniciuscavalcanti` |
| Outro site / escola | `https://vinicavalcanti.com` |
| Empresa atual | `E-Line Media` |
| Anexos | `Vini_Cavalcanti_CV.pdf` e `Vini_Cavalcanti_Cover_Letter.pdf` |

### RESPOSTAS PADRÃO DE TRIAGEM

| Pergunta | Resposta (é a verdade, nunca mude) |
|---|---|
| Precisa de patrocínio de visto, agora ou no futuro? | `Yes` |
| Autorizado a trabalhar nos EUA / Canadá / Austrália / Nova Zelândia? | `No` |
| É cidadão da UE / tem permissão de trabalho na UE? | `No — I would need sponsorship` |
| Tipo de visto | `Skilled-worker sponsorship. I already work remotely for a US studio as an international contractor and can keep working remotely while the process runs.` |
| Disposto a realocar / presencial / híbrido? | `Yes` |
| Anos de experiência | `10` (em escala fechada, a faixa mais alta: `More than 10 years`, `> 7`, `More than 5 years`) |
| Senioridade | `Senior` (quando o menu não tiver "Senior", use `Sr`) |
| Liderou equipe? Anos de liderança? | `Yes` — cinco anos de Senior na E-Line revisando trabalho de outros e definindo padrão de asset, mais professor e fundador da própria escola e mestrando |
| Experiência em games? | `Yes` |
| Salário atual | `Confidential under the NDA of my current contract; happy to discuss ranges during the process.` |
| Aviso prévio / disponibilidade | `A standard transition period with my current studio; glad to align dates in the process.` — ou `Within 30 days of an offer` |
| Pesquisa de diversidade | `Prefer not to say` / `I choose not to disclose` |
| Como soube da vaga | a página de carreiras do próprio estúdio |

**Pretensão salarial, regra de 04/09:** se o anúncio publica faixa, peça **a base dela**. Sem faixa:
casa grande — EUA `USD 100,000`, Canadá `CAD 95,000`, Reino Unido `GBP 50,000`, Europa `EUR 55,000`;
casa pequena ou média — EUA `USD 85,000`, Canadá `CAD 80,000`, Reino Unido `GBP 42,000`, Europa `EUR 45,000`;
Oceania `AUD 110,000` (grande) e `AUD 95,000` (média). Sempre com a frase
`Open to aligning with your band for the role.` Nunca abaixo do piso legal da ocupação: abaixo dele o patrocínio fica inviável.

### TEXTO A — apresentação completa, com realocação (campo livre grande)

```
I am ready to move for the role, on site and full time.

I am a Senior 3D Character Artist with more than 10 years in stylized characters. I take a character end to end: sculpt and high poly, retopology, UVs, baking, hand painted and PBR texturing, look development, LODs and engine integration, plus character grooming in Houdini when hair or fur is part of the design. Tools: ZBrush, Maya, Blender, Substance Painter and Designer, Houdini, Marmoset, Unreal and Unity.

I am credited on The Wingfeather Saga season 1 at Angel Studios, where I modeled and hand painted the characters, and for almost five years at E-Line Media in Arizona I have taken Endstar's hero characters from first sculpt to engine, working fully remote from another country and time zone as an international contractor. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it.

As a Senior I review other artists' work and set the asset standard; I also teach as the founder of my own character art school and I am a master's candidate, so mentoring and holding a quality bar is daily work for me.

I am not an EU citizen and I would need visa sponsorship. My academic background, with an honors laurea, a postgraduate specialization in Game Art, a master's in progress, IELTS and publications, makes a strong visa case, and I can start remotely while the permit is processed.

Open to aligning with your band for the role.
Portfolio: https://www.artstation.com/viniciuscavalcanti
LinkedIn: https://www.linkedin.com/in/vinicavalcnti/
```

### TEXTO B — versão curta (campo de duas ou três linhas)

```
Senior 3D Character Artist, 10+ years in stylized characters: modeling, sculpting, texturing and look development, plus hair and fur grooming in Houdini. Credited on The Wingfeather Saga at Angel Studios and, for almost five years, on Endstar at E-Line Media. I am ready to move for the role; I am not an EU citizen and would need visa sponsorship. Portfolio: https://www.artstation.com/viniciuscavalcanti
```

### TEXTO C — ressalva de realismo (só onde o anúncio pedir realista/fotorreal)

```
My portfolio is mostly stylized, but every sculpt starts from realistic anatomy and I am comfortable delivering realistic organic models in ZBrush with clean game topology, UVs and PBR texturing. I work daily with PBR workflows, UVs, color management and displacement, in Substance Painter and Designer and in Houdini. I would rather say that plainly than overstate it.
```

### TEXTO D — caso de visto em uma frase

```
I am not an EU citizen and I have no work authorization in Canada, the US, Australia or New Zealand: I would need sponsorship. My academic background, with an honors laurea, a postgraduate specialization in Game Art, a master's in progress, IELTS and publications, makes a strong visa case, and I can start remotely while the permit is processed, which is how I already work today.
```

---

# BANDA 1 — REALOCAÇÃO PARA CANADÁ E EUROPA (31 vagas)

## 1. Behaviour Interactive — Senior 3D Character Artist, Dead by Daylight — Montréal, Canadá

**Link direto:** https://jobs.lever.co/bhvr/18024240-e637-409f-a647-b422541e2dc7/apply
**Por que vale:** disciplina literal e senioridade que bate — Senior Character Artist, permanente e híbrida em Montréal, num jogo que vive de assassinos e sobreviventes, ou seja, produção contínua de personagem. **Reconferida no ar hoje na API oficial do Lever.**
**A parede:** hCaptcha com desafio de imagem do Lever, aparece **depois** do clique em Submit.
**Tempo estimado:** 3 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Resume/CV | `Vini_Cavalcanti_CV.pdf` |
| Full name | `Vini Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Phone | telefone do documento privado do Drive, CAMPANHA - dados pessoais dos formulários |
| Current location | `Olinda, Pernambuco, Brazil` |
| Current company | `E-Line Media` |
| LinkedIn URL | `https://www.linkedin.com/in/vinicavalcnti/` |
| Portfolio URL | `https://www.artstation.com/viniciuscavalcanti` |
| Other Website | `https://vinicavalcanti.com` |
| Are you legally eligible to work in Canada? | `No` |
| Aceita ir ao escritório 3 dias por semana (híbrido)? | `Yes` |
| Why are you interested in this role? | o texto abaixo |
| Pesquisa demográfica | `Prefer not to say` |

**Textos longos:**

```
Dead by Daylight is a game made of characters, killers and licensed survivors shipped continuously, and character art end to end is exactly what I do. I have more than 10 years in 3D characters, almost five of them at E-Line Media taking Endstar's hero characters from first sculpt to engine: high poly, retopology, UVs, baking, texturing, LODs and engine integration, plus hair and fur grooming in Houdini. On The Wingfeather Saga at Angel Studios I modeled and hand painted the Season 1 characters. As a Senior I review other artists' work and set the asset standard, I teach as the founder of my own character art school and I am a master's candidate. I already applied to your 7 Days to Die opening because Behaviour is a studio I want to work at. I am ready to move to Montreal for the role; I am not an EU or Canadian citizen and would need visa sponsorship, and my academic background, with an honors laurea, a postgraduate specialization, a master's in progress, IELTS and publications, makes a strong visa case. Portfolio: https://www.artstation.com/viniciuscavalcanti
```

**Cuidados:** o anúncio está em francês na API, mas o formulário é bilíngue e o texto em inglês é aceito. Não responda "Yes" à elegibilidade no Canadá: mentir na triagem derruba a candidatura depois. Esta é a **terceira** requisição de personagem da Behaviour — a de *7 Days to Die* já foi enviada em 30/08, não repita aquela.

## 2. Netflix Animation Studios, Vancouver e Sydney — A VAGA ANTIGA MORREU, DUAS NOVAS ESTÃO VIVAS

> **ATENÇÃO: a Head of Characters de Vancouver SAIU DA FILA em 08/09 à noite, e o jeito como ela
> morreu é a armadilha mais cara desta revalidação.** A página dela **responde 200** e a API de
> detalhe também. Parece viva. Mas o id `790317384604` **não está no quadro oficial**: paginei a
> busca do próprio quadro da Netflix e ele não aparece em nenhuma página, enquanto as irmãs de
> Vancouver aparecem. **Vaga deslistada mantém a página no ar.** Se você tivesse clicado, teria
> preenchido um formulário para uma requisição que não existe mais.
>
> **No lugar dela, duas requisições VIVAS da mesma casa, medidas no anúncio inteiro em 08/09:**
>
> **2a. Character Modeling Supervisor — Netflix Animation Studios — Sydney, Austrália**
> `https://explore.jobs.netflix.net/careers/job/790317298520` (Req `JR41751`)
> **É o cargo dele com o nome dele, em nível de supervisão.** O anúncio diz: *"lead the character
> modeling team"*. Híbrido, mínimo de 3 dias no escritório, e a Austrália está no escopo.
> **Régua de dezessete termos: nenhum veto.** Não há `authoriz`, `eligib`, `sponsor` nem
> `resident`. A única frase de regime é *"This role is based out of Sydney, Australia. Hybrid Role
> (Minimum of 3 days a week in the office)"*, que é presença, não veto. Faixa não publicada: pela
> regra de 04/09, casa grande na Austrália é **AUD 110.000**, com "Open to aligning with your band".
>
> **2b. Head of Environments — Netflix Animation Studios — Vancouver, Canadá**
> `https://explore.jobs.netflix.net/careers/job/790316561602` (Req `JR41288`)
> Liderança de show para **todos os ambientes, cenários e props**. Ambiente é média na régua de
> disciplina, mas isto é **liderança**, é a casa que você mais quer e é Vancouver, prioridade 1.
> **Régua: nenhum veto.** `based in` casa em *"This role is based in Vancouver, British Columbia"*,
> que diz ONDE O CARGO FICA, e não quem pode se candidatar. É a distinção que separa este caso do
> da People Can Fly, onde a frase era *"open to candidates only from ... based in Europe"*. Faixa
> não publicada. Casa grande no Canadá: **CAD 95.000**.
>
> **A parede das duas é a mesma:** o Eightfold da Netflix preenche 100% pela automação e o POST em
> `/api/application/v2/submit` volta 400, que é reCAPTCHA invisível recusando IP de datacenter.
> Do seu navegador passa.

#### (texto original da nº 2, mantido só para registro; a requisição está DESLISTADA, veja o aviso acima)

**Link direto:** https://explore.jobs.netflix.net/careers/job/790317384604
**Por que vale:** **SUBIU PARA O TOPO DA FILA na reconferência de hoje.** Personagem 3D estilizado da modelagem ao CFX, em Vancouver — Canadá anglófono, prioridade 1 do Vini —, híbrido, na casa que já abriu duas portas para ele. **Faixa publicada no próprio anúncio: "the overall market range for this role is typically $204k - $279k CAD"** (compensação total, sem stock). Anúncio buscado termo a termo por `authoriz`, `eligib`, `sponsor` e `work permit`: **zero ocorrências**, nenhum veto de residência escrito. A única ressalva real é o regime híbrido, **mínimo de 3 dias por semana no escritório**. Reconferida no ar hoje: a página responde com o título e com a faixa.
**A parede:** reCAPTCHA **invisível** no envio — não há desafio para resolver; do IP dele reprova, do seu navegador passa. As suas duas candidaturas Netflix que deram certo foram enviadas assim.
**Tempo estimado:** 3 min

**Cole nos campos (o formulário só monta depois do `APPLY NOW`):**

| Campo | O que colar |
|---|---|
| Resume | `Vini_Cavalcanti_CV.pdf` — logo depois aparece o modal **Candidate Privacy**: clicar em **I ACKNOWLEDGE** |
| First name / Last name | `Vini` / `Cavalcanti` (o parser preenche sozinho, só confira) |
| Email | `contact@vinicavalcanti.art` |
| Phone country code | deixar como veio: `BR (+55) Brazil` |
| Phone | **só os dígitos, sem +55, sem espaço e sem hífen** — do documento privado do Drive |
| City / State / Country | `Olinda` / `Pernambuco` / `Brazil` (State e Country vêm preenchidos, não digite por cima) |
| Additional Documents | `Vini_Cavalcanti_Cover_Letter.pdf` |
| URL / Portfolio | `https://www.artstation.com/viniciuscavalcanti` |
| Self-ID (gênero, etnia, orientação, veterano, trans, deficiência) | `I choose not to disclose` em todos |
| É contratante da Netflix hoje? | `No` |
| Já trabalhou na Netflix? | `No` |
| Precisa de patrocínio de visto? | `Yes` |
| Pretensão salarial, se aparecer campo | Pela política de 04/09, pede-se a BASE da faixa publicada: `CAD 204,000. Open to aligning with your band for the role.` |

**Cuidados:** **três coisas que já custaram tempo.** (1) Ir direto na URL `/careers/apply?pid=...` não renderiza nada — tem que clicar em `APPLY NOW` e esperar uns 10 segundos. (2) O modal de privacidade bloqueia todos os cliques seguintes até você aceitar. (3) Digitar por cima de Country e State só concatena texto e quebra o campo. Se pedir código de 6 dígitos por email, ele **só vale na mesma aba** — não feche.

## 3. Behaviour Interactive — Senior 3D Character Artist, projeto não anunciado — Montréal, Canadá

> **TERCEIRA REQUISIÇÃO DA MESMA CASA, medida em 08/09 e deixada FORA da fila de propósito.**
> A Behaviour também tem uma **Senior Texture Artist, Dead by Daylight** (Lever
> `55fa65fe-50b8-41e2-a406-5f185c860295`), Montréal, híbrida, permanente, e ela é da sua
> disciplina com todas as letras. Preenchi o formulário inteiro em 08/09 às 08h20 e cliquei em
> Submit de verdade: o formulário aceita tudo (CV com Success, os três links, BeFlex em Yes,
> elegibilidade no Canadá em No) e aí aparece o hCaptcha de imagem, o mesmo destas duas.
> **Não entra na fila porque seriam TRÊS candidaturas suas na Behaviour no mesmo dia**, e é
> justamente o que a campanha decidiu evitar na Scopely e na Epic. Mande as duas de cima hoje;
> se elas não andarem em algumas semanas, esta é a próxima, e o formulário é idêntico ao da nº 1.

**Link direto:** https://jobs.lever.co/bhvr/86ddd557-7d9b-48f1-ab04-0a90ba38e2dc/apply
**Por que vale:** segunda requisição sênior de personagem da mesma casa, híbrida em Montréal, e o anúncio pede setup e groom de cabelo em Unreal 5, que é exatamente a sua combinação. **Reconferida no ar hoje na API oficial do Lever.**
**A parede:** hCaptcha com desafio de imagem do Lever, no envio.
**Tempo estimado:** 3 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Resume/CV | `Vini_Cavalcanti_CV.pdf` |
| Full name | `Vini Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Phone | telefone do documento privado do Drive, CAMPANHA - dados pessoais dos formulários |
| Current location | `Olinda, Pernambuco, Brazil` |
| Portfolio | `https://www.artstation.com/viniciuscavalcanti` |
| LinkedIn | `https://www.linkedin.com/in/vinicavalcnti/` |
| Other Website | `https://vinicavalcanti.com` |
| Eligible to work in Canada? | `No` |
| Aceita ir ao escritório 3 dias por semana? | `Yes` |
| Why are you interested in this role? | o texto abaixo |

**Textos longos:**

```
The posting asks for a senior character artist who can set up and groom hair in Unreal Engine 5, and that is the combination I bring: 10+ years in 3D characters, almost five of them at E-Line Media taking Endstar's hero characters from first sculpt to engine, plus character grooming in Houdini. On The Wingfeather Saga at Angel Studios I modeled and hand-painted Season 1 characters. I take a character end to end, sculpt through retopology, UVs, baking, texturing and engine integration, and I already applied to your 7 Days to Die opening because Behaviour is a studio I want to work at. I am ready to move to Montreal for the role; my academic background (honors laurea, postgraduate specialization, master's in progress, IELTS, publications) makes a strong visa case.
```

**Cuidados:** é vaga diferente da nº 1 desta fila (aquela é Dead by Daylight); pode mandar as duas, mas com cartas diferentes, que é como estão escritas aqui.

> **MUDOU desde que esta fila foi escrita (revalidação de 08/09):** o anúncio agora diz **"remote
> or office"**, e a lista de destinos de realocação ganhou **Dubai**. Ou seja, a vaga ficou MELHOR:
> continua com realocação paga e agora aceita remoto. Nada a corrigir na resposta, só saiba disso
> ao ler a tela.

## 4. Gaijin Entertainment — Lead Material & Texture Artist — Budapeste, Hungria (com realocação paga)

**Link direto:** https://gaijinent.com/job/material--texture-artist
**Por que vale:** texturização em cargo de liderança, e é o **melhor sinal de visto da fila**: a casa paga realocação para Hungria, Chipre, Alemanha, Montenegro, Letônia e Armênia e diz por escrito que considera candidato de qualquer país. **Reconferida no ar hoje: a página da vaga responde com o título certo.**
**A parede:** captcha de **desafio de imagem próprio deles**, no fim do formulário (`input[name=captcha]`).
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Full name | `Vini Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Additional communication method | `LinkedIn: https://www.linkedin.com/in/vinicavalcnti/` |
| Country | `Brazil` |
| What languages do you speak? | `Portuguese (native), English (IELTS certified), Spanish (working proficiency)` |
| Cover letter | o texto abaixo |
| CV | `Vini_Cavalcanti_CV.pdf` |
| Enter captcha | resolver o desafio de imagem na tela |

**Textos longos:**

```
I am ready to move for the role, and your relocation support to Hungary or Germany is one of the reasons I am writing.

I am a Senior 3D Character Artist with more than 10 years in stylized characters, credited on The Wingfeather Saga season 1 at Angel Studios and, for almost five years, on Endstar at E-Line Media in Arizona, where I take hero characters from first sculpt to engine as a remote international contractor. Texturing and material work are not a separate step for me: I own the asset end to end, sculpt and high poly, retopology, UVs, baking, PBR and hand painted texturing, look development and engine integration, in Substance Painter and Designer, ZBrush, Maya and Houdini, where I also handle grooming.

On the lead side, I have been Senior for five years, which means reviewing other artists' work, setting the asset standard and mentoring juniors; I also teach as the founder of my own character art school and I am a master's candidate, so giving feedback and holding a quality bar is daily work for me.

One thing said plainly: my published portfolio is mostly stylized, while this role asks for realistic materials for hard surface, architecture and terrain. Every sculpt I make starts from realistic anatomy and I work daily with PBR, UVs, color management, trim sheets and tileables, so I am comfortable delivering realistic surfaces, and I would rather say that clearly than overstate it.

I am not an EU citizen and would need work sponsorship. My academic background, with an honors laurea, a postgraduate specialization in Game Art, a master's in progress, IELTS and publications, makes a strong visa case. Open to aligning with your band for the role; as a reference, I am looking at around EUR 55,000 per year.

Portfolio: https://www.artstation.com/viniciuscavalcanti
```

**Cuidados:** o quadro inteiro fica em https://gaijinent.com/job e só existe depois do JavaScript; se abrir vazio, recarregue. A ressalva de realismo já está na carta de propósito — não a tire.

## 5. Gameloft Montréal — Candidature Spontanée / Spontaneous Application — Montréal, Canadá

**Link direto:** https://jobs.smartrecruiters.com/gameloft/744000116612089
**Por que vale:** achada hoje varrendo o quadro inteiro da Gameloft por token de ATS (43 vagas, `company identifier gameloft`); candidatura espontânea aberta em Montréal, Canadá anglófono e prioridade 1. O anúncio escreve por conta própria, no bloco de benefícios: **"Support for new employees relocating from countries or regions outside Quebec"** — apoio a realocação dito por escrito é o sinal mais raro desta campanha. **Confirmada viva hoje na API oficial do SmartRecruiters (ref REF1006B), com zero ocorrência de `authoriz`, `eligib`, `sponsor` ou `work permit` no texto integral.**
**A parede:** DataDome no botão **I'm interested**, igual às outras Ubisoft e NBCUniversal — a página do anúncio renderiza normal, mas o formulário fica vazio para automação.
**Tempo estimado:** 4 min

**Cole nos campos (tela do SmartRecruiters, mesma das outras Ubisoft/NBCUniversal desta fila):**

| Campo | O que colar |
|---|---|
| Upload resume | `Vini_Cavalcanti_CV.pdf` |
| First / Last name | `Vini` / `Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Phone | telefone do documento privado do Drive, CAMPANHA - dados pessoais dos formulários |
| Location / City / Country | `Olinda, Pernambuco` / `Brazil` |
| LinkedIn | `https://www.linkedin.com/in/vinicavalcnti/` |
| Website / Portfolio | `https://www.artstation.com/viniciuscavalcanti` |
| Cover letter (campo ou anexo) | `Vini_Cavalcanti_Cover_Letter.pdf` + TEXTO A |
| Are you legally authorized to work in Canada? | `No` |
| Will you require sponsorship? | `Yes` |
| Aceita realocar para Montréal? | `Yes` |
| Como soube da vaga | `Gameloft careers page` |
| Consentimentos e privacidade | marcar |

**Textos longos:** TEXTO A, acrescentando na primeira linha: `Your benefits page states support for new employees relocating from countries or regions outside Quebec, and that relocation support is exactly what I'm looking for.`
**Cuidados:** é candidatura espontânea (banco de talentos), não vaga nomeada — declare já na primeira linha que sua área é personagem/modelagem e peça encaminhamento interno, como manda a regra de porta de entrada. Se aparecer pergunta sobre nível de francês, responda a verdade, sem inventar: é Montréal/Quebec.

## 6. Ubisoft Massive — Lead Character Artist, The Division 2 — Malmö, Suécia

**Link direto:** https://jobs.smartrecruiters.com/Ubisoft2/744000144027102
**Por que vale:** Lead de personagem, tempo integral, numa das casas que mais patrocinam visto na Europa; Suécia é rota de trabalho conhecida e o time é internacional. **Reconferida no ar hoje na API oficial do SmartRecruiters.**
**A parede:** DataDome no botão **I'm interested**, igual às outras Ubisoft.
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Upload resume | `Vini_Cavalcanti_CV.pdf` |
| First / Last name | `Vini` / `Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Phone | telefone do documento privado do Drive, CAMPANHA - dados pessoais dos formulários |
| Location | `Olinda, Pernambuco, Brazil` |
| LinkedIn / Portfolio | LinkedIn e ArtStation dos DADOS FIXOS |
| Cover letter | `Vini_Cavalcanti_Cover_Letter.pdf` + TEXTO A |
| Anos de experiência | `10` |
| Anos liderando equipe | `5` |
| Direito de trabalho na Suécia / UE | `No, I would need a work permit and sponsorship` |
| Aceita realocar para Malmö? | `Yes` |
| Pretensão | `Open to aligning with your band for the role; as a reference, around EUR 55,000 per year.` |

**Textos longos:** TEXTO A. Se o anúncio insistir em realismo, acrescente o TEXTO C.
**Cuidados:** o anúncio é de jogo realista; não esconda que seu portfólio é estilizado, use o TEXTO C. Suécia exige que a oferta alcance o piso salarial do visto de trabalho — a frase de alinhamento à banda já cobre isso.

> **MUDOU (revalidação de 08/09), e é a mudança que mais dói desta lista:** o anúncio passou a
> dizer, com todas as letras, *"**relocation assistance is not available for this role**"*.
> **Isso NÃO é veto e a vaga CONTINUA na fila:** ele quer mudar de país e a frase fala de AJUDA
> financeira à mudança, não de proibição de candidatar-se nem de patrocínio de visto. Mas mudança
> por conta própria é uma decisão sua, e você merecia saber antes de clicar, não depois.

## 7. Avalanche Studios Group — Lead Character Artist — Estocolmo, Suécia

**Link direto:** https://jobs.lever.co/avalanchestudios/8f7bd580-5877-446e-83cb-97bb1fce0f6a/apply
**Por que vale:** Lead de personagem, **emprego permanente** e híbrido, e o formulário é curto — é a melhor relação entre valor e minuto da fila. **Reconferida no ar hoje na API oficial do Lever: "Lead Character Artist", Stockholm, Permanent Employment, híbrido.**
**A parede:** hCaptcha do Lever no envio.
**Tempo estimado:** 2 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Resume/CV | `Vini_Cavalcanti_CV.pdf` |
| Full name | `Vini Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Phone (obrigatório) | telefone do documento privado do Drive, CAMPANHA - dados pessoais dos formulários |
| Current location (obrigatório) | `Olinda, Pernambuco, Brazil` |
| Current company | `E-Line Media` |
| LinkedIn URL | `https://www.linkedin.com/in/vinicavalcnti/` |
| Portfolio URL | `https://www.artstation.com/viniciuscavalcanti` |
| Additional information (se houver) | TEXTO B |

**Textos longos:** TEXTO B, e o TEXTO C se houver campo livre — o anúncio fala em criatura e animal com ênfase realista.
**Cuidados:** o anúncio diz explicitamente que não é preciso cumprir todos os requisitos para se candidatar; ênfase em **animal e criatura**, que está no seu portfólio, então cite bicho e criatura no campo livre se ele existir.

## 8. Rodeo FX — Senior Lookdev Artist — Toronto, Canadá

**Link direto:** https://jobs.smartrecruiters.com/RodeoFX/744000144123709-senior-lookdev-artist-multiple-positions
**Por que vale:** *look development* é disciplina literal sua, no nível Senior, em **Toronto**, Canadá anglófono, sem exigência de francês, casa grande dona da Mikros. **Reconferida no ar hoje na API oficial do SmartRecruiters (RDO243M, Toronto, full-time).**
**A parede:** DataDome. A página renderiza zero caractere para robô; no seu navegador abre normal.
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Upload resume | `Vini_Cavalcanti_CV.pdf` |
| Nome / email / telefone | dos DADOS FIXOS |
| Portfolio | `https://www.artstation.com/viniciuscavalcanti` |
| LinkedIn | `https://www.linkedin.com/in/vinicavalcnti/` |
| Anos em lookdev ou texturização | `10+` (o anúncio pede no mínimo 6) |
| Autorização de trabalho no Canadá | `No, I would need sponsorship` |
| Aceita realocar para Toronto? | `Yes. I am ready to move to Toronto for the role, on site and full time.` |
| Pretensão | `Open to aligning with your band for the role; as a reference, around CAD 95,000 per year.` |
| Cover letter | `Vini_Cavalcanti_Cover_Letter.pdf` + TEXTO C |

**Textos longos:** TEXTO C, obrigatoriamente — o anúncio pede texturização **realista** e fotorrealismo. Acrescente ao fim:

```
Nuke and Mari are the two tools on your list I would be picking up rather than bringing, and I would rather say that plainly than overstate it.
```

**Cuidados:** o anúncio diz que existe faixa salarial mas **não publica o número**, então vale a política de casa grande no Canadá. A versão de Montréal é a nº 15 desta fila e é outra requisição, pode mandar as duas.

## 9. Ubisoft Montréal — Team Lead, Modeling (Unreal) — Montréal, Canadá

**Link direto:** https://jobs.smartrecruiters.com/Ubisoft2/744000141713411
**Por que vale:** **modelagem** em cargo de liderança, em Montréal, na casa que mais realoca artista internacional no Canadá. **Reconferida no ar hoje na API oficial do SmartRecruiters: "Team Lead - Modeling (Unreal)", Montreal.**
**A parede:** DataDome no botão **I'm interested**.
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Upload resume | `Vini_Cavalcanti_CV.pdf` |
| First / Last name, email, telefone | dos DADOS FIXOS |
| Location | `Olinda, Pernambuco, Brazil` |
| LinkedIn / Portfolio | LinkedIn e ArtStation dos DADOS FIXOS |
| Cover letter | `Vini_Cavalcanti_Cover_Letter.pdf` + TEXTO A |
| Anos de experiência | `10` |
| Anos liderando equipe | `5` |
| Autorização no Canadá / patrocínio | `No` / `Yes` |
| Aceita realocar para Montréal? | `Yes` |
| Pretensão | `Open to aligning with your band for the role; as a reference, around CAD 95,000 per year.` |

**Textos longos:** TEXTO A. Acrescente uma linha sobre Unreal: você integra asset em Unreal e Unity todo dia no Endstar.
**Cuidados:** é a segunda requisição da Ubisoft desta fila (a outra é a nº 6; a Senior Character Artist do Rainbow Six Siege que aparecia aqui como nº 2 SAIU da fila — já recusada em 02/09). São vagas diferentes, mas mande uma por vez.

## 10. Lighthouse Games — Lead Character Artist — Royal Leamington Spa, Reino Unido

**Link direto:** https://apply.workable.com/lighthousegames/j/F7F90250DA/apply/
**Por que vale:** Lead de personagem em estúdio novo da Tencent montado por ex-Playground (Forza Horizon), presencial no Reino Unido, que patrocina Skilled Worker por rotina.
**Por que vale (atualizado):** **Reconferida hoje pelo host `jobs.workable.com`, que não está bloqueado.** Anúncio inteiro buscado termo a termo: ZERO `authoriz`, `eligib`, `sponsor`, `work permit` ou `relocat` — sem veto de residência escrito. E o `/form` oficial do Workable mostra que os ÚNICOS campos obrigatórios são First name, Last name e Email: é a candidatura mais barata da fila inteira.
**A parede (CORRIGIDA hoje):** não é mais o bloqueio 1015 do Workable contra o nosso IP — isso já caiu, e quando cai só permite LER o formulário, não enviar. A parede de verdade é o **Cloudflare Turnstile**, e ele só aparece **DEPOIS do clique em "Submit application"**, testado com um clique real hoje: o formulário inteiro preenche, o botão fica habilitado, e só ali surge a caixa "Verify you are human"; sem resolvê-la o botão trava para sempre em "Submitting...".
**Tempo estimado:** 2 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| First name / Last name | `Vini` / `Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Phone | telefone do documento privado do Drive, CAMPANHA - dados pessoais dos formulários |
| **Address / City / Country** | `Olinda, Pernambuco, Brazil` — **apague antes o "Columbus, United States of America"** que o autofill do Workable escreve sozinho |
| Headline | `Senior 3D Character Artist, 10+ years in stylized characters, character grooming in Houdini` |
| Summary | TEXTO B |
| Resume | `Vini_Cavalcanti_CV.pdf` |
| Cover letter | `Vini_Cavalcanti_Cover_Letter.pdf` |
| Portfolio / showreel | `https://www.artstation.com/viniciuscavalcanti` |
| Do you have the right to work in the UK? | `No — I would need Skilled Worker sponsorship` |
| Willing to relocate to Leamington Spa? | `Yes` |
| Salary expectation | `Open to aligning with your band for the role; as a reference, around GBP 50,000 per year.` |
| Privacy notice | marcar |

**Textos longos:** TEXTO B mais o TEXTO C — o anúncio fala em credibilidade dos personagens, ou seja, realismo.
**Cuidados:** marque a caixa "Verify you are human" **só depois** de clicar em Submit application — ela não existe na tela antes disso. Se a tela ficar presa em "Submitting...", é ela esperando você.

## 11. Framestore — 3D Modeller (contrato curto) — Montréal, Canadá

**Link direto:** https://framestore.recruitee.com/o/modeleurse-3d-3d-modeller-contrat-court-terme
**Por que vale:** **modelagem**, disciplina literal, no departamento de Film de uma casa multipremiada com Oscar, em Montréal. Das 51 vagas do quadro deles é a única de modelagem. **Reconferida no ar hoje.**
**A parede:** hCaptcha de imagem do Recruitee, **só depois do clique em Send**.
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| CV or resume | `Vini_Cavalcanti_CV.pdf` |
| Full name | `Vini Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Phone | **trocar o `+1` que já vem** para o código do Brasil; número do documento privado do Drive |
| Portfolio link | `https://www.artstation.com/viniciuscavalcanti` |
| Portfolio password | `No password, the portfolio is public.` |
| Years of experience in 3D modeling (radio) | `More than 5 years` |
| Availability date | `Within 30 days of an offer.` |
| Current Location | `Olinda, Pernambuco` |
| Citizenship | `Brazilian` |
| **Will you need visa sponsorship? (radio)** | `Yes` |
| Desired salary/rate | `Open to aligning with your band for the role; as a reference, around CAD 95,000 per year equivalent. I am ready to move to Montreal for the role.` |
| What are your pronouns? (radio) | `He/him` |
| Consentimento | marcar |

**Cuidados:** **três armadilhas medidas.** (1) O formulário existe na página mas fica fechado: clique em **Apply** primeiro, senão o botão Send nem aparece. (2) O telefone vem com `+1` num widget que não aceita clique — escreva com o código do país explícito. (3) As três últimas perguntas são **radio, não texto**: anos de experiência, patrocínio e pronomes. Contrato curto, mas contrato por projeto em casa grande de VFX conta pela sua regra de formato.

## 12. Frontier Developments — Experienced Character Artist — Cambridge, Reino Unido

**Link direto:** https://jobs.eu.lever.co/frontier/3571ace3-9f1a-4db2-9e2b-5eb8c8487181/apply
**Por que vale:** personagem puro, casa grande britânica, híbrido em Cambridge, e o formulário já pergunta sobre patrocínio, ou seja, eles contratam quem precisa. **Reconferida no ar hoje na API oficial do Lever: "Experienced Character Artist", Cambridge / Hybrid.**
**A parede:** hCaptcha de desafio de imagem do Lever.
**Tempo estimado:** 5 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Resume/CV | `Vini_Cavalcanti_CV.pdf` |
| Nome, email, telefone | dos DADOS FIXOS |
| LinkedIn | `https://www.linkedin.com/in/vinicavalcnti/` |
| Portfolio | `https://www.artstation.com/viniciuscavalcanti` |
| Other | `https://vinicavalcanti.com` |
| Tem experiência com escultura orgânica? | `Yes` |
| Link do portfólio | `https://www.artstation.com/viniciuscavalcanti` |
| Salário atual | `Confidential under the NDA of my current contract; happy to discuss ranges during the process.` |
| Pretensão salarial | `Open to aligning with Frontier's band for the role; as a reference, I'm looking at around GBP 50,000 per year.` |
| Aviso prévio | `A standard transition period with my current studio; glad to align dates in the process.` |
| País de residência | `Brazil` |
| Híbrido ou presencial? | `Hybrid, relocating to Cambridge.` |
| Precisa de patrocínio de visto? | `Yes` |
| Detalhe sobre elegibilidade no Reino Unido | o texto abaixo |
| Entende que a vaga exige realocação para Cambridge? | `Yes` |
| Pesquisa de diversidade | `Prefer not to say` |

**Textos longos:**

```
I answered yes: I would need Skilled Worker sponsorship. My academic background (honors laurea, postgraduate specialization, master's in progress, IELTS, publications) supports the visa case, and I can start remotely while it is processed, which is how I already work today for a studio in another country.
```

**Cuidados:** a pretensão antiga de USD 46.000 está **morta**; use o número acima. Não deixe o campo de salário atual em branco nem escreva valor: a frase de NDA é a resposta.

## ~~13. Asobo Studio — Character Artist H/F — Bordeaux, França~~ — SAIU EM 08/09: VETO DE IDIOMA

> **Não gaste os seus minutos nesta.** A revalidação com a régua nova achou o que a antiga não
> media, e está escrito no anúncio, em francês:
> *"Tu disposes d'un niveau de **français** et anglais opérationnel"*.
> Francês operacional é exigência, não preferência. Conferido por mim na API do Lever.
> Texto original mantido abaixo para registro.

#### (texto original da nº 13, mantido só para registro; a entrada está MORTA, veja o aviso acima)

**Link direto:** https://jobs.eu.lever.co/asobostudio/1ab1d28f-6f7c-4106-b43f-6ef78dcb7603/apply
**Por que vale:** personagem puro na casa de *A Plague Tale*, presencial em Bordeaux. **Reconferida no ar hoje na API oficial do Lever.**
**A parede:** hCaptcha de desafio de imagem do Lever.
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Resume/CV | `Vini_Cavalcanti_CV.pdf` |
| Nome, email, telefone | dos DADOS FIXOS |
| LinkedIn / Portfolio / Other | LinkedIn, ArtStation e site dos DADOS FIXOS |
| Conte mais sobre você | o texto abaixo |
| Anos de experiência | `> 7` |
| Aceita trabalhar presencial em Bordeaux? | `Oui / Yes` |
| Habilidades em realismo | TEXTO C |
| Experiência em estúdio | `Yes: almost five years full-time at E-Line Media (Endstar), and earlier studio experience at PUGA Studios delivering characters for international clients.` |
| Caixa de consentimento de comunicação | marcar |

**Textos longos:**

```
I'm Vini Cavalcanti, Senior 3D Character Artist with 10+ years in stylized characters. On The Wingfeather Saga at Angel Studios I modeled and hand-painted characters for Season 1, and for almost five years I've been with E-Line Media in Arizona, taking Endstar's hero characters from first sculpt to engine. I also do character grooming in Houdini. A new narrative project at the studio behind A Plague Tale is exactly the kind of character-driven work I want: I take a character end to end, sculpt through retopology, UVs, baking, texturing and engine integration, and I am ready to move to Bordeaux and am fully open to moving for the role; my academic background (honors laurea, postgraduate specialization, master's in progress, IELTS, publications) makes a strong visa case. Portfolio: artstation.com/viniciuscavalcanti
```

**Cuidados:** o anúncio é em francês, mas o formulário aceita resposta em inglês; não invente nível de francês em nenhum campo.

## 14. Cosmico — SENIOR 3D ARTIST — Suécia

**Link direto:** https://www.cosmicogames.com/career (o botão **SENIOR 3D ARTIST →** leva para https://www.cosmicogames.com/contact, que é a porta que o próprio estúdio publicou)
**Por que vale:** vaga sênior de 3D aberta, em estúdio de mundos estilizados, que é o seu registro nativo. **Reconferida no ar hoje: a página lista SENIOR 3D ARTIST.**
**A parede:** não é captcha visível — é o anti-robô do Squarespace, que recusa sessão automatizada com *"Unable to submit form"*. No seu navegador passa.
**Tempo estimado:** 3 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| First Name / Last Name | `Vini` / `Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Message | o texto abaixo |

**Textos longos:**

```
Applying for the SENIOR 3D ARTIST role listed on your careers page. I am ready to move to Sweden for the role, on site and full time.

I am a Senior 3D Character Artist with more than 10 years in stylized characters, and I take an asset end to end: sculpt and high poly, retopology, UVs, baking, hand painted and PBR texturing, look development and engine integration, in Maya, ZBrush, Substance Painter and Designer and Blender. I also groom hair and fur in Houdini, so character, texture and groom are one continuous job for me rather than three handoffs.

I am credited on The Wingfeather Saga season 1 at Angel Studios, where I modeled and hand painted the characters, and for almost five years I have been the character artist on Endstar at E-Line Media in Arizona, taking hero characters from first sculpt to engine while working fully remote from another country and time zone. My portfolio holds more than 45 projects with over 60 characters across many titles.

As a Senior of five years I review other artists' work and set the asset standard; I also teach as the founder of my own character art school and I am a master's candidate.

I am not an EU citizen and I would need visa sponsorship. My academic background, with an honors laurea, a postgraduate specialization in Game Art, a master's in progress, IELTS and publications, makes a strong visa case. Open to aligning with your band for the role; as a reference, I am looking at around EUR 45,000 per year.

Portfolio: https://www.artstation.com/viniciuscavalcanti
LinkedIn: https://www.linkedin.com/in/vinicavalcnti/
Site: https://vinicavalcanti.com
```

**Cuidados:** o formulário tem um **campo isca invisível** (`message-field`) que não pode ser preenchido — preencha só Name, Email e Message. Não há anexo: os links precisam estar no texto, e estão.

## 15. Rodeo FX — Senior Lookdev Artist — Montréal, Canadá

**Link direto:** https://jobs.smartrecruiters.com/RodeoFX/744000145587059-senior-lookdev-artist-multiple-positions
**Por que vale:** mesma disciplina e senioridade da nº 8, requisição diferente, na sede da casa. **Reconferida no ar hoje na API oficial do SmartRecruiters.**
**A parede:** DataDome, igual à de Toronto.
**Tempo estimado:** 3 min

**Cole nos campos:** os mesmos da nº 8, trocando a cidade:

| Campo | O que colar |
|---|---|
| Upload resume | `Vini_Cavalcanti_CV.pdf` |
| Nome, email, telefone | dos DADOS FIXOS |
| Portfolio / LinkedIn | ArtStation e LinkedIn dos DADOS FIXOS |
| Anos em lookdev ou texturização | `10+` |
| Autorização de trabalho no Canadá | `No, I would need sponsorship` |
| Aceita realocar? | `Yes. I am ready to move to Montreal for the role.` |
| Pretensão | `Open to aligning with your band for the role; as a reference, around CAD 95,000 per year.` |
| Cover letter | `Vini_Cavalcanti_Cover_Letter.pdf` + TEXTO C |

**Cuidados:** as duas de Lookdev saíram em inglês e francês; **a terceira vaga deles, "Artiste de développement visuel Senior", saiu só em francês** e ficou fora desta fila de propósito — francês já derrubou duas candidaturas desta campanha.

## 16. Framestore — Blender Generalist / Visual Development Artist — Montréal, Canadá

**Link direto:** https://framestore.recruitee.com/o/generaliste-blender-artiste-au-development-visuel-blender-generalist-visual-development-artist
**Por que vale:** **visual development** é metade do seu título, e **Blender** é ferramenta central do time e está no seu currículo; Montréal, casa com Oscar. **Reconferida no ar hoje.**
**A parede:** hCaptcha de imagem do Recruitee, **só depois do clique em Send**.
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Full name | `Vini Cavalcanti` |
| Email address | `contact@vinicavalcanti.art` |
| Phone number | trocar o país para Brasil no seletor; número do documento privado do Drive |
| CV or resume | `Vini_Cavalcanti_CV.pdf` |
| Cover letter | `Vini_Cavalcanti_Cover_Letter.pdf` |
| Showreel/Portfolio Link | `https://www.artstation.com/viniciuscavalcanti` |
| Showreel/Portfolio password | deixar vazio, o portfólio é público |
| Availability date | `Negotiable, around two months from an offer` |
| Citizenship | `Brazilian` |
| Current location | `Olinda, Pernambuco` |
| Are you open to relocating to Montreal? | `Yes` |
| Desired annual salary (CAD) | `CAD 95,000 per year; open to aligning with your band for the role` |
| Preferred pronoun | `He/him` |
| Legal Agreements | marcar |

**Cuidados:** clique em **Apply** para abrir a seção de envio antes de procurar o botão Send. O anúncio é bilíngue e **não exige francês**.

## 17. Framestore — Blender Generalist — Londres, Reino Unido

**Link direto:** https://framestore.recruitee.com/o/blender-generalist
**Por que vale:** é o time de **Visual Development** de Londres, com Blender no centro; o anúncio cita *IF*, *Loki S2* e *Como Treinar o Seu Dragão*. **Reconferida no ar hoje.**
**A parede:** hCaptcha de imagem do Recruitee depois do Send.
**Tempo estimado:** 4 min

**Cole nos campos:** iguais aos da nº 16, com duas trocas:

| Campo | O que colar |
|---|---|
| Are you open to relocating to London, UK? | `Yes` |
| Desired annual salary (£ GBP) | `GBP 50,000 per year; open to aligning with your band for the role` |
| Todo o resto | igual à nº 16 |

**Cuidados:** mesma armadilha do botão **Apply** antes do Send; o telefone precisa do seletor de país trocado para Brasil.

## 18. Distillery VFX — Job Application Form — Vancouver, Canadá

**Link direto:** https://www.distilleryvfx.com/apply
**Por que vale:** Canadá anglófono, estúdio boutique de VFX para cinema e TV de alto perfil, e o formulário pergunta status no Canadá com valores em CAD, ou seja, contratam de fora. **Reconferida no ar hoje.**
**A PAREDE, CORRIGIDA EM 09/09 COM CLIQUE DE VERDADE — a descrição anterior estava errada e faria você perder a viagem.** Dizia "não é captcha, são dois menus do Wix". Os dois menus **são resolvíveis pela automação**, e eu resolvi: preenchi o formulário inteiro, subi o CV (o nome `Vini_Cavalcanti_CV.pdf` aparece na tela, que é a prova válida), marquei as três caixas de local de trabalho, escolhi `Sr` no nível e **`Need a work permit`** no status, que é a opção verdadeira e fica logo depois de `Open work permit`, que seria mentira.

**O que trava é outra coisa, e ela só aparece DEPOIS do clique em `Apply Now`:** abre uma janela escrita **`Verification — Please confirm you're human`** com o **reCAPTCHA de caixa "I'm not a robot"**. Está no print `dist_pos.png`. Nenhuma varredura de HTML via isso antes do clique, e é mais um caso da regra da campanha: **quem dá o veredito é o clique**.

**Nada foi enviado.** Não há linha no `enviados.csv` para a Distillery, e o formulário continua preenchido esperando você marcar uma caixa.

**Tempo estimado:** 4 min, e o botão chama **`Apply Now`**, não "Submit".

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| First name / Last name | `Vini` / `Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Phone | código do país Brasil; número do documento privado do Drive |
| Current Country of Residence | `Brazil` |
| What role are you interested in? | `Character Modeller and Texture Artist. Senior 3D Character Artist, 10+ years, stylized. I am ready to move to Vancouver for the role; I would need visa sponsorship.` |
| **What is your current level?** (menu) | `Sr` — o menu **não tem "Senior"** |
| LinkedIn Link | `https://www.linkedin.com/in/vinicavalcnti/` |
| Reel or Portfolio Link 1 | `https://www.artstation.com/viniciuscavalcanti` |
| Reel or Portfolio Link 2 | `https://vinicavalcanti.com` |
| Vimeo Password | `No password, the portfolio is public.` |
| Upload Resume | `Vini_Cavalcanti_CV.pdf` |
| **Current Status in Canada** (menu) | `Need a work permit` — **cuidado, "Open work permit" fica logo antes e seria mentira** |
| Select all workplace options | marcar `Studio`, `Hybrid` e `Remote` |
| Rate expectation | `Open to aligning with your band for the role; as a reference, around CAD 80,000 per year.` |
| How did you hear about this role? | `Distillery VFX careers page` |

**Cuidados:** depois do upload, o Wix **limpa o campo de arquivo** — a prova de que o CV subiu é o **nome do arquivo escrito na tela**, não o campo.

## 19. Cinesite — Candidature Spontanée / Speculative Application — Montréal, Canadá

**Link direto:** https://cinesitemontreal.bamboohr.com/careers/93
**Por que vale:** casa grande de animação e VFX em Montréal, candidatura espontânea **aberta e revalidada** (jobOpeningStatus Open). **Reconferida no ar hoje.**
**A parede:** reCAPTCHA de caixa do BambooHR.
**Tempo estimado:** 3 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| First / Last Name, Email, Phone | dos DADOS FIXOS |
| **Country** | trocar por `Brazil` se vier `Canada` |
| Resume / Cover Letter | os dois PDFs, cada um no campo certo |
| LinkedIn | `https://www.linkedin.com/in/vinicavalcnti/` |
| Website / Portfolio | `https://www.artstation.com/viniciuscavalcanti` |
| Qual é o seu status de trabalho no Canadá? | `I will need a work permit` |
| Você está em Montréal? | `No — I am ready to move for the role` |
| Data disponível | cerca de dois meses à frente |
| Pretensão | `CAD 95,000 per year. Open to aligning with your band for the role.` |
| Cargo pretendido / mensagem | TEXTO B |
| reCAPTCHA | marcar a caixa |

**Cuidados:** Montréal é Quebec — se aparecer pergunta sobre francês, responda a verdade, sem inventar nível.

## 20. Cinesite — Speculative Application — Vancouver, Canadá

**Link direto:** https://cinesitevancouver.bamboohr.com/careers/260
**Por que vale:** mesma casa, cidade anglófona, e Vancouver é o cluster mais denso da campanha. **Reconferida no ar hoje.**
**A parede:** reCAPTCHA de caixa do BambooHR.
**Tempo estimado:** 3 min

**Cole nos campos:** iguais aos da nº 19, mais os de endereço:

| Campo | O que colar |
|---|---|
| Address / City / Province / Postal Code / Country | do documento privado do Drive; **Country = `Brazil`** |
| Todo o resto | igual à nº 19, trocando Montréal por Vancouver |

**Cuidados:** o vínculo aqui é **Fixed Term** (prazo determinado) — vale como porta de entrada em casa grande, mas saiba disso antes.

## 21. Fortiche Production — candidatura espontânea "Become a Forticher" — Paris, Montpellier e Las Palmas

**Link direto:** https://forticheprod.com/application/
**Por que vale:** é a Fortiche de *Arcane*, referência máxima de estilizado, e os departamentos que ela lista incluem **Character modeling, Character design, Groom e Texture** — a sua disciplina inteira. **Reconferida no ar hoje.**
**A parede:** o servidor derruba a conexão da automação no envio; o reCAPTCHA é v3 (pontuação, não portão). No seu navegador passa.
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Contract | `Employee / Freelance` |
| Name / Surname | `Vini` / `Cavalcanti` |
| E-mail | `contact@vinicavalcanti.art` |
| Phone | do documento privado do Drive, CAMPANHA - dados pessoais dos formulários |
| Preferred workplace location (marca mais de um) | `Paris`, `Montpellier`, `Las Palmas` e `Remote` |
| Upload your CV | `Vini_Cavalcanti_CV.pdf` |
| Upload your Portfolio | `Vini_Cavalcanti_Cover_Letter.pdf` |
| LinkedIn | `https://www.linkedin.com/in/vinicavalcnti/` |
| Department (marca mais de um) | `Character modeling`, `Character design`, `Groom`, `Texture` |
| Software | `Maya`, `Photoshop`, `Houdini`, `Zbrush` |
| Availability | uma data cerca de dois meses à frente |
| Tell us about you | TEXTO A |
| Acceptance | marcar |

**Cuidados:** o formulário tem **três passos** e o seletor de local é um widget próprio — marque os locais com o mouse e confirme que ficaram marcados antes de avançar, senão o passo 1 não valida e a tela volta ao começo.

## 22. EF Games — Senior 3D Hard Surface and Vehicle Artist — Madri, Espanha

**Link direto:** https://ef.games/jobs/senior-3d-hard-surface/
**Por que vale:** é a única vaga **aberta** de modelagem e texturização achada na varredura de estúdios espanhóis; presencial em Madri, estúdio novo bancado por uma das maiores casas de multiplayer, e o anúncio pede **mentorar outros no departamento**, que é o seu argumento de senioridade. **Reconferida no ar hoje.**
**A parede:** reCAPTCHA v3 invisível do Elementor — pontuação de sessão. No seu navegador passa.
**Tempo estimado:** 5 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| First name / Last name | `Vini` / `Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Phone | formato internacional, do documento privado do Drive |
| Upload CV | `Vini_Cavalcanti_CV.pdf` |
| Additional files | `Vini_Cavalcanti_Cover_Letter.pdf` |
| LinkedIn profile | `https://www.linkedin.com/in/vinicavalcnti/` |
| Link to your website/portfolio | `https://www.artstation.com/viniciuscavalcanti` |
| Other useful links | `https://vinicavalcanti.com` |
| Quantos anos de experiência | `10+ years` |
| Have you worked on AAA video game projects? | `No` (é a verdade; o texto livre explica o alcance) |
| Proficiency in English | `Fluent (C1-C2)` |
| Proficiency in Spanish | **[VOCÊ SABE ESTE]** — a campanha não tem esse dado; o requisito é inglês OU espanhol e o inglês já cumpre |
| Where are you based | `Olinda, Pernambuco, Brazil` |
| Desired salary (bruto/ano, em €) | `Open to aligning with your band for the role; as a reference, I'm looking at around EUR 55,000 gross per year.` |
| Notice needed | `About one to two months, negotiable.` |
| Comfortable in a hybrid environment? | `Yes` |
| Please list all the video games you have contributed to | o texto abaixo |
| Cover letter | o segundo texto abaixo |
| **As DUAS caixas de aceite** | marcar as duas |

**Textos longos:**

```
Endstar (E-Line Media, PC), Senior 3D Character Artist: hero characters from first sculpt to engine, high poly, retopology, UVs, baking, texturing and engine integration. Almost five years, ongoing. The Wingfeather Saga, season 1 (Angel Studios, animated series): character modeling and hand painted texturing. Earlier outsourcing work at PUGA Studios delivering character and asset work for international clients. Full breakdown and images: https://www.artstation.com/viniciuscavalcanti
```

```
My discipline is character: modeling, sculpting, texturing and look development. If a character opening comes up at EF Games I would like this application forwarded there. I am applying to the Hard Surface and Vehicle role because building a game asset end to end is the same job for me, and because I want to work in Madrid.

I am ready to move for the role, on site in Madrid and full time. I am not an EU citizen and I would need visa sponsorship. My academic background, with an honors laurea, a postgraduate specialization in Game Art, a master's in progress, IELTS and publications, makes a strong visa case.

I am a Senior 3D Character Artist with more than 10 years in stylized work. For almost five years at E-Line Media in Arizona I have taken Endstar's hero characters from first sculpt to engine: high poly, retopology, UVs, baking, texturing, LODs and engine integration in Unity and Unreal, which is the whole asset rather than one stage of it. Before that I modeled and hand painted the characters of season 1 of The Wingfeather Saga at Angel Studios. On hard surface specifically, mechanical and articulated shapes are part of my daily modeling work, and I take 2D concept through to a finished asset with clean topology, UV edit, materials and baked textures.

I am a Senior who reviews other artists' work and sets the asset standard, I teach as the founder of my own character art school, and I am a master's candidate, so mentoring inside a department is already part of what I do.

Portfolio: artstation.com/viniciuscavalcanti
```

**Cuidados:** a caixa de aceite da Privacy Policy e a caixa opcional de contato futuro têm o **mesmo id** — marque as duas na tela, uma de cada vez.

## 23. Skydance Animation — Senior Grooming TD — Madri, Espanha

**Link direto:** https://jobs.lever.co/skydance/9ad28cab-87cd-4235-ae9b-b4c53a3457e5/apply
**Por que vale:** grooming é a sua disciplina adjacente, no nível **Senior**, em casa da Paramount, híbrida em Madri. **Reconferida no ar hoje na API oficial do Lever: "Senior Grooming TD", Madrid.**
**A parede:** hCaptcha de imagem do Lever, depois do Submit.
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Resume/CV | `Vini_Cavalcanti_CV.pdf` |
| Full name / Email / Phone | dos DADOS FIXOS |
| **Current location** | cole `Olinda, Pernambuco, Brazil` **de uma vez e não toque mais** — o campo apaga sozinho a cada tecla que não casa com sugestão |
| Current company | `E-Line Media` |
| LinkedIn / Portfolio / Other website | dos DADOS FIXOS |
| How did you hear about this position? | `Skydance Website` |
| What is your working status in Spain? | `Require work permit` |
| Please choose your country of residence | `Brazil` |
| When would you be able to join us? | `Within 30 days of an offer. If it helps the schedule, I can start remotely while the work permit is being processed, which is how I already work today for a studio in another country.` |
| Duas caixas de texto obrigatórias | TEXTO A, com a frase de realocação para Madri na primeira linha |

**Cuidados:** uma pergunta obrigatória fica **escondida atrás do aviso de cookies** ("country of residence") — feche o aviso antes de conferir. Grooming é diferencial de apoio, não o cargo que você persegue: por isso está aqui e não no topo.

> **MUDOU (revalidação de 08/09):** a espontânea agora está classificada como **Freelance**, e não
> mais como efetiva. Continua valendo e continua na fila, mas entre ela e uma efetiva do mesmo
> tempo de preenchimento, faça a efetiva primeiro.

## 24. TRIXTER — Speculative Job Application — Munique e Berlim, Alemanha

**Link direto:** https://www.trixter.de/jobs/job/speculative-job-application-2/
**Por que vale:** TRIXTER de Munique, **A Cinesite Partner Company**, e a própria página diz que **só aceitam candidatura por este formulário**, nunca por email nem LinkedIn — ou seja, é a única porta e ela está aberta. **Reconferida no ar hoje.**
**A parede:** não é captcha — o envio por AJAX não sai do ambiente da automação e a tela mente dizendo que a mensagem não pôde ser enviada. No seu navegador passa.
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| First Name / Last Name | `Vini` / `Cavalcanti` |
| E-mail | `contact@vinicavalcanti.art` |
| Phone | com código do país, do documento privado do Drive |
| **Eligibility to work in Germany** | `No` |
| Availability Date | data cerca de dois meses à frente, no formato `dd.mm.aaaa` |
| Desired Salary / Freelance Daily Rate | `EUR 55,000 per year, or EUR 350 per day freelance. Open to aligning with your band for the role. I am ready to move to München or Berlin for the role; I am not an EU citizen and would need visa sponsorship.` |
| Link to Portfolio/Website | `https://www.artstation.com/viniciuscavalcanti` |
| Portfolio Password | `No password, the portfolio is public` |
| LinkedIn | `https://www.linkedin.com/in/vinicavalcnti/` |
| IMDB | deixar vazio |
| Resume | `Vini_Cavalcanti_CV.pdf` |
| Cover letter | `Vini_Cavalcanti_Cover_Letter.pdf` |
| Caixa de consentimento | marcar |

**Cuidados:** **não existe campo de texto livre** e a vaga pede que a carta diga qual cargo você quer — o PDF da carta precisa dizer *Senior 3D Character Artist / Character Modeler*. E aceite os cookies antes: o aviso fica por cima do botão de envio e o clique leva para a página de privacidade.

## 25. GIANTS Software — Open Application — Erlangen (Alemanha), Zurique (Suíça) e Brno (Chéquia)

**Link direto:** https://jobs.smartrecruiters.com/GIANTSSoftwareGmbH/744000086339075-open-application
**Por que vale:** a página de carreiras deles descreve Brno como o núcleo de 3D com artistas de **veículo e personagem**; candidatura espontânea aberta em três países da Europa. **Reconferida no ar hoje na API oficial do SmartRecruiters.**
**A parede:** DataDome no botão **I'm interested**.
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Resume e Cover Letter (pedem os dois) | os dois PDFs |
| Nome, email, telefone | dos DADOS FIXOS (prefixo BR +55, número sem repetir o código) |
| Cargo pretendido | `3D Character Artist / Character Modeler` |
| Direito de trabalho | `No, I would need sponsorship` |
| Pretensão | `Open to aligning with your band for the role; as a reference, I'm looking at around EUR 55,000 per year, and I understand Swiss levels differ.` |
| Texto de apresentação | o texto abaixo |

**Textos longos:**

```
I'm a Senior 3D Character Artist with more than 10 years in stylized characters, credited on The Wingfeather Saga at Angel Studios and on Endstar at E-Line Media, where for almost five years I have taken hero characters from first sculpt to engine as a remote international contractor.

Your careers page describes the Brno office as the core of 3D art, with artists specialised in vehicle and character creation and character animation. Character creation end to end is my daily work: sculpt, retopology, UVs, baking, texturing and engine integration, with topology built for deformation, plus character grooming in Houdini when hair or fur is part of the design.

My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it. I am ready to move and I am ready to move for the role; I would need work sponsorship, and my academic background (honors laurea, postgraduate specialization in Game Art, master's in progress, IELTS and publications) supports the visa case.

Portfolio: artstation.com/viniciuscavalcanti
```

## 26. nWave Studios — Speculative Application — Bruxelas ou Liège, Bélgica

**Link direto:** https://nwave.bamboohr.com/careers/121
**Por que vale:** o formulário tem departamento **Character_Modeling** e nível **Senior** como opções, ou seja, a casa arquiva sua candidatura exatamente na sua disciplina. **Reconferida no ar hoje.**
**A parede:** reCAPTCHA de caixa do BambooHR.
**Tempo estimado:** 3 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Nome, email, telefone, endereço | dos DADOS FIXOS e do documento privado do Drive |
| Country | `Brazil` |
| Estúdio | `Brussels` |
| Departamento | `Character_Modeling` |
| Nível | `Senior` |
| Escolaridade / universidade | seus dados de formação |
| Resume / Cover Letter | os dois PDFs, cada um no campo certo |
| Desired Pay | `Around EUR 45,000 per year. Open to aligning with your band for the role.` |
| Website / LinkedIn | ArtStation e LinkedIn |
| Mensagem, se houver | TEXTO B |
| reCAPTCHA | marcar a caixa |

**Cuidados:** mesma armadilha do BambooHR: o campo **Cover Letter vem antes do Resume** e aceita PDF.

## 27. Quantic Dream — Candidature Spontanée — Paris, França (CDI)

**Link direto:** https://jobs.eu.lever.co/quanticdream/cc1dacb2-01b7-47c0-b827-9b9b786d1dd7/apply
**Por que vale:** candidatura espontânea em CDI (contrato permanente) numa casa de jogo narrativo com personagem realista de alto nível; formulário curto. **Reconferida no ar hoje na API oficial do Lever.**
**A parede:** hCaptcha de imagem do Lever.
**Tempo estimado:** 2 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Resume/CV | `Vini_Cavalcanti_CV.pdf` |
| Full name / Email / Phone | dos DADOS FIXOS |
| Current location | `Olinda, Pernambuco, Brazil` |
| Current company | `E-Line Media` |
| LinkedIn URL | `https://www.linkedin.com/in/vinicavalcnti/` |
| Portfolio URL | `https://www.artstation.com/viniciuscavalcanti` |
| Campo livre, se houver | TEXTO B |

**Cuidados:** não invente nível de francês.

## 28. BetaDwarf — Unsolicited Application — Copenhague, Dinamarca

**Link direto:** https://betadwarfaps.bamboohr.com/careers/28
**Por que vale:** porta espontânea aberta numa casa dinamarquesa; a Dinamarca só patrocina acima de um piso salarial, e a pretensão abaixo já está calculada para caber nele. **Reconferida no ar hoje.**
**A parede:** reCAPTCHA de caixa do BambooHR.
**Tempo estimado:** 3 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| First / Last Name | `Vini` / `Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Phone | do documento privado do Drive, formato internacional |
| Address / City / Province / Postal Code | do documento privado do Drive |
| **Country** | trocar `Denmark`, que vem preenchido, por `Brazil` |
| Cover Letter | `Vini_Cavalcanti_Cover_Letter.pdf` |
| Resume | `Vini_Cavalcanti_CV.pdf` |
| **Desired Pay** (obrigatório) | `Around DKK 520,000 per year. Open to aligning with your band for the role, and the offer would need to meet the Danish work permit salary threshold for sponsorship.` |
| Website, Blog or Portfolio | `https://www.artstation.com/viniciuscavalcanti` |
| LinkedIn URL | `https://www.linkedin.com/in/vinicavalcnti/` |
| Who referred you | deixar vazio |
| **What role are you seeking?** (obrigatório) | `Senior 3D Character Artist / Character Modeler: modeling, sculpting, texturing and look development, with Houdini grooming as a supporting skill.` |
| Consentimento da Privacy Policy | marcar |
| reCAPTCHA | marcar a caixa |

**Cuidados:** não baixe o número da pretensão: abaixo do piso do visto dinamarquês você não fica barato, fica impossível de patrocinar.

## 29. Grimlore Games (THQ Nordic) — Open Application — Munique, Alemanha

**Link direto:** https://grimloregames.com/open-application/ → botão **APPLY NOW**
**Por que vale:** casa de *Titan Quest II* e *SpellForce 3*, do grupo THQ Nordic/Embracer, e as vagas de arte abertas hoje são de cenário e animação, ou seja, **o lado de personagem e criatura está descoberto**. **Reconferida no ar hoje.**
**A parede:** WPForms com reCAPTCHA v2 de **caixa de marcar**, visível acima do Submit.
**Tempo estimado:** 2 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Name * | `Vini Cavalcanti` |
| Email * | `contact@vinicavalcanti.art` |
| Subject * | `Open Application (m/f/d) - Senior 3D Character Artist / Character Modeler` |
| Message * | o texto abaixo |
| Privacy Policy Checkbox * | marcar |
| reCAPTCHA | marcar a caixa |

**Textos longos:**

```
I am ready to move to Munich for the role, on site and full time.

I am applying as a Senior 3D Character Artist / Character Modeler. I have more than 10 years in stylized characters. For almost five years I have been Senior at E-Line Media in Arizona, taking Endstar hero characters from first sculpt to engine: sculpt and high poly, retopology, UVs, baking, hand painted and PBR texturing, look development and engine integration in Unreal and Unity. Before that I modeled and hand painted the characters of season 1 of The Wingfeather Saga at Angel Studios. I also groom hair and fur in Houdini, so hair is part of the character rather than a separate handoff.

Your open application page says to reach out even when the role is not listed, and Titan Quest II and the RPG and RTS line are exactly the kind of character and creature work I want: heroes, monsters and armour sets built for deformation and for engine, at scale. Your current openings list a Senior/Principal Environment Artist and a 3D Animator, so the character and creature side is where I would strengthen the team.

As a Senior I review other artists' work, set the asset standard and mentor junior artists. I also teach as founder of my own character art school and I am a master's candidate.

Portfolio: https://www.artstation.com/viniciuscavalcanti
LinkedIn: https://www.linkedin.com/in/vinicavalcnti/
School: https://vinicavalcanti.com
CV happy to send by reply.

Compensation: open to aligning with your band for the role; as a reference, I am looking at around EUR 55,000 per year.

Work authorisation: I am not an EU citizen and I would need visa sponsorship. My academic background, with an honors laurea, a postgraduate specialization in Game Art, a master's in progress, IELTS and publications, makes a strong visa case. I can start remotely while the permit is processed.
```

**Cuidados:** o formulário **não tem campo de arquivo**, então o CV vai por link e por resposta ao email deles. Não escreva telefone no texto.

## 30. The Knights of Unity — candidatura espontânea — Wrocław, Polônia

**Link direto:** https://theknightsofunity.elevato.net/pl/nie-znalazles-interesujacego-cie-stanowiska,ja,58 (tem alternador PL/EN no topo)
**Por que vale:** formulário completo, com pretensão, aviso prévio e até quatro anexos, numa casa polonesa de Unity; Polônia é Europa com patrocínio viável e custo de vida que fecha a conta.
**A parede:** reCAPTCHA v2 de caixa de marcar.
**Tempo estimado:** 3 min
**Não reconferida hoje** (registro de 06/09).

**Cole nos campos:**

| Campo (rótulo em polonês) | O que colar |
|---|---|
| Imię * | `Vini` |
| Nazwisko * | `Cavalcanti` |
| Adres e-mail * | `contact@vinicavalcanti.art` |
| Telefon komórkowy * | do documento privado do Drive |
| Jakie stanowisko Cię interesuje? | `Senior 3D Character Artist / Character Modeler` |
| Plik CV (até 4 arquivos, 4 MB cada) | `Vini_Cavalcanti_CV.pdf` e `Vini_Cavalcanti_Cover_Letter.pdf` |
| Kwota (pretensão) | `EUR 45,000` |
| Okres wypowiedzenia (aviso prévio) | cerca de dois meses |
| Adres e-mail de quem indicou | deixar vazio |
| Informacja dodatkowa | TEXTO A, com `I am ready to move to Wroclaw` na primeira linha |
| Zgoda (consentimento) * | marcar |
| reCAPTCHA | marcar a caixa |

## 31. Netflix Animation Studios — Head of Character Effects (CFX) — Vancouver, Canadá

**Link direto:** https://explore.jobs.netflix.net/careers/job/790314413902
**Por que vale:** CFX encosta direto no seu grooming em Houdini, é Vancouver, e o formulário é o mesmo da nº 2 — depois da primeira, esta leva um minuto. **Reconferida no ar hoje.**
**A parede:** reCAPTCHA invisível no envio (sem desafio; do seu navegador passa).
**Tempo estimado:** 2 min

**Cole nos campos:** exatamente os mesmos da nº 2.

**Cuidados:** é chefia de departamento e CFX é diferencial de apoio, não o seu cargo alvo — por isso vem depois das de modelagem e personagem. Existe a irmã de Sydney, que é a nº 39 desta fila.

---

# BANDA 2 — REMOTO EM EUA, CANADÁ E EUROPA (3 vagas)

> **MUDOU (revalidação de 08/09), em dois pontos que mexem na decisão:** o contrato virou
> **`contract`**, e os **Estados Unidos saíram** da lista de países aceitos. Sobram Canadá e Reino
> Unido, que continuam no escopo dele. Segue na fila, mas agora é contrato remoto, não efetiva.

## 32. Keywords Studios / Lakshya Digital — Character Artist, Hair Specialist — remoto (Canadá, EUA e Reino Unido)

**Link direto:** https://apply.workable.com/keywords-intl1/j/CA33DB1208/
**Por que vale:** é a única vaga que a campanha já viu feita **só de grooming**, remota e listando Canadá, EUA e Reino Unido, e você já trabalha remoto internacional todo dia — é a rota mais parecida com a sua vida atual.
**A parede:** Cloudflare Turnstile, o quadrinho "Verify you are human" acima do botão.
**Tempo estimado:** 3 min
**Não reconferida hoje:** o Workable devolve bloqueio de Cloudflare para robô; o registro de 06/09 confirma o anúncio vivo na fonte oficial.

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| First name / Last name | `Vini` / `Cavalcanti` |
| Email / Phone | `contact@vinicavalcanti.art` / telefone do documento privado do Drive |
| **Address / City / Country** | `Olinda, Pernambuco, Brazil` — **limpe antes** o "Columbus, United States of America" que o autofill escreve |
| Headline | `Senior 3D Character Artist, 10+ years in stylized characters, character grooming in Houdini` |
| Summary | o primeiro texto abaixo |
| Resume | `Vini_Cavalcanti_CV.pdf` |
| Income Expectations | `Open to aligning with your band for the role; as a reference, I'm looking at around USD 100,000 per year.` |
| Cover letter | o segundo texto abaixo |
| Privacy Notice | marcar |
| Turnstile | marcar o quadrinho e enviar |

**Textos longos:**

```
Senior 3D Character Artist with more than 10 years in stylized characters, credited on The Wingfeather Saga at Angel Studios and on Endstar at E-Line Media, where I have taken hero characters from first sculpt to engine for almost five years as a remote international contractor. I do character grooming in Houdini and handle hair, fur and facial hair as part of the character, not as a separate step. Portfolio: artstation.com/viniciuscavalcanti
```

```
Hair is the part of a character I keep coming back to, so a role built entirely around it is one I want.

For almost five years I have been the character artist on Endstar at E-Line Media in Arizona, taking hero characters from first sculpt through retopology, UVs, baking, texturing and engine integration, working fully remote from a different country and time zone as an international contractor. That is the exact working pattern this role describes. Before that I modeled and hand-painted characters for the first season of The Wingfeather Saga at Angel Studios.

On grooming specifically: I build character grooms in Houdini, and I work them as part of the character rather than as a bolt-on, which means shape, flow, layering and silhouette read against the sculpt, and the result has to survive deformation and hold up in engine. My published work is stylized, and your requirement lists realistic or highly stylized real-time hair, so I am putting the stylized side forward and I am comfortable working to hair cards and to strand-based setups depending on what the project needs.

I would need work sponsorship for an employment position, and I already work as a remote contractor for a studio abroad, so the contract and remote format here is what I do every day.

Portfolio: artstation.com/viniciuscavalcanti
```

## 33. Gigantic Duck Games — 3D Artist — remoto (estúdio em Borås, Suécia)

> **MEDIDA CAMPO A CAMPO EM 08/09 ÀS 20H50, com clique de verdade, e agora custa 40 segundos.**
> São **duas** requisições vivas no quadro (Bombergrounds e um jogo não anunciado), as duas
> *"Remote, Full time (40 hours/week)"*, e a régua de dezessete termos deu **zero ocorrências**.
> O envio automatizado foi recusado, e a prova de QUE FOI a pontuação e não o preenchimento é
> objetiva: o formulário voltou com a classe `wpcf7-form spam` e a **lista de campos inválidos
> vazia**. Nenhum campo estava errado.
>
> | Campo | O que escolher ou colar |
> |---|---|
> | Position | **3D Artist** |
> | Location | **Remote** (é a única opção) |
> | Full name | `Vini Cavalcanti` |
> | Country | `Brazil` |
> | Email | `contact@vinicavalcanti.art` |
> | Discord | opcional, pode deixar vazio |
> | Portfolio URL | `https://www.artstation.com/viniciuscavalcanti` |
> | Resume | anexar o CV (obrigatório) |
> | Application letter | anexar a carta |
> | Extra attachment | anexar o portfólio PDF |
> | Where did you hear about us? | **Other** |
>
> **Não há campo de texto livre**, então a frase de realocação não tem onde entrar, e não faz
> falta: a vaga é remota.

**Link direto:** https://giganticduck.com/application/
**Por que vale:** vaga **aberta** de 3D Artist, **remota**, 40h semanais, em dois projetos; foi a única vaga de 3D aberta de toda a varredura de WordPress. **Reconferida no ar hoje.**
**A parede:** Contact Form 7 com reCAPTCHA v3 — a tela mente dizendo "error trying to send your message". No seu navegador passa.
**Tempo estimado:** 3 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Position you are applying for (obrigatório) | `3D Artist` |
| Location (obrigatório) | `Remote` |
| Full Name (obrigatório) | `Vini Cavalcanti` |
| Country (obrigatório) | `Brazil` |
| Email (obrigatório) | `contact@vinicavalcanti.art` |
| Discord | deixar vazio |
| Link to portfolio or other site | `https://www.artstation.com/viniciuscavalcanti` |
| CV (obrigatório) | `Vini_Cavalcanti_CV.pdf` |
| Application Letter | `Vini_Cavalcanti_Cover_Letter.pdf` |
| Extra Attachment | deixar vazio |
| Where did you hear about this position (obrigatório) | `Other` |

**Cuidados:** **não existe campo de mensagem livre** — a frase de realocação e o caso de visto só cabem na carta anexada, então confira que o PDF da carta está atualizado antes de enviar.

## 34. Obsidian Entertainment — General Application (Remote) — EUA

**Link direto:** https://obsidian.applytojob.com/apply/21Ud1IGKcj
**Por que vale:** a General Application deles está marcada **Remote e Full Time** e segue aberta; é porta de entrada numa casa grande de RPG. **Reconferida no ar hoje.**
**A parede:** reCAPTCHA de caixa de marcar do JazzHR.
**Tempo estimado:** 3 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| First / Last Name, Email, Phone | dos DADOS FIXOS |
| Location | `Olinda, Pernambuco, Brazil` |
| Resume / Cover Letter | os dois PDFs |
| Website / Portfolio | `https://www.artstation.com/viniciuscavalcanti` |
| LinkedIn | `https://www.linkedin.com/in/vinicavalcnti/` |
| Cargo pretendido | `Senior 3D Character Artist / Character Modeler` |
| Aceita realocar? | `Yes` |
| Autorizado a trabalhar nos EUA? | `No` |
| Precisa de patrocínio? | `Yes` |
| Mensagem / carta | TEXTO A |
| reCAPTCHA | marcar a caixa |

**Cuidados:** a Character Artist que existia no digest do 80.lv **não existe mais**; o que resta é esta candidatura geral. Não perca tempo procurando a outra.

---

# BANDA 3 — RESTO DO ESCOPO (5 vagas)

## 35. RocketWerkz — Expressions of Interest — Auckland, Nova Zelândia

**Link direto:** https://careers.rocketwerkz.com/o/expressions-of-interest-auckland/c/new
**Por que vale:** presencial **com apoio de realocação e de visto dito no anúncio**, que é o sinal mais raro que existe; Nova Zelândia entra pelo escopo da Oceania. **Reconferida no ar hoje.**
**A parede:** hCaptcha de desafio de imagem do Recruitee, no envio.
**Tempo estimado:** 3 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Nome, email, telefone | dos DADOS FIXOS |
| CV e carta | os dois PDFs |
| Função pretendida | `3D Artist – Senior 3D Character Artist` |
| Portfolio | `https://www.artstation.com/viniciuscavalcanti` |
| Tem direito de trabalho na Nova Zelândia? | `No` |
| Está na Nova Zelândia? | `No` |
| Aceita realocar? | `Yes — I am ready to move for the role` |
| Pretensão | `Open to aligning with your band for the role; as a reference, the equivalent of AUD 95,000 per year for a studio of this size.` |
| Campo livre | TEXTO A |

**Cuidados:** clique em **Apply** antes de procurar o botão de envio, como em todo Recruitee.

## 36. Jam City — Principal 3D Generalist — San Francisco, EUA (presencial, USD 75.000–120.000)

**✅ ENVIADA por você em 19/09 às 16h14 UTC (Application submitted!, sem captcha). Item fechado.**

**Link direto:** https://jobs.lever.co/jamcity/14272af5-efc7-4150-8b59-dcabdaa8c578/apply
**Por que vale:** **faixa publicada**, pede personagem explicitamente, ZBrush e Substance, e trata anatomia humana e animal. **Reconferida no ar hoje na API oficial do Lever: "Principal 3D Generalist", San Francisco, CA.**
**A parede:** hCaptcha de desafio de imagem do Lever.
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Resume/CV | `Vini_Cavalcanti_CV.pdf` |
| Full name / Preferred Name | `Vini Cavalcanti` / `Vini` |
| Email / Phone | dos DADOS FIXOS |
| City / State / Country | `Olinda` / `Pernambuco` / `Brazil` |
| LinkedIn / Portfolio | dos DADOS FIXOS |
| Marcar "I agree" | marcar |
| Está empregado hoje? | `Yes` |
| Já trabalhou na Jam City? | `No` |
| Autorizado a trabalhar nos EUA? | `No` |
| Precisa de patrocínio? | o texto abaixo |
| Como soube da vaga | `LinkedIn` |
| Gênero e veterano | `Decline to self-identify` |
| Pretensão, se pedir | `Aligned with the posted range for the role, at the lower end (USD 75,000). Open to aligning with your band.` |

**Textos longos:**

```
Yes. I would need skilled-worker sponsorship (H-1B or O-1). I currently work remotely for a US studio as an international contractor and can keep working remotely while the process runs.
```

**Cuidados:** é presencial em San Francisco, ou seja, depende inteiramente do patrocínio — por isso está na terceira banda e não no topo, apesar da faixa publicada.

## 37. Valve — 3D Character Artist — Bellevue, WA, EUA

**Link direto:** https://www.valvesoftware.com/en/jobs?job_id=2
**Por que vale:** personagem 3D na Valve, formulário curtíssimo, e é uma das casas que patrocinam sem drama. **Reconferida no ar hoje.**
**A parede:** reCAPTCHA com caixa visível.
**Tempo estimado:** 2 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Name | `Vini Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Portfolio / links | `https://www.artstation.com/viniciuscavalcanti` e `https://vinicavalcanti.com` |
| Como descobriu a vaga | `Valve careers page` |
| CV | `Vini_Cavalcanti_CV.pdf` |
| Campo livre, se houver | TEXTO B |
| reCAPTCHA | marcar a caixa |

## ~~38. DreamWorks Animation — Visual Development Artist — Glendale, CA, EUA~~ — SAIU EM 08/09: EXPIRADA

> A API do SmartRecruiters devolve `active: false` para a requisição `744000143937898`, e a página
> escreve *"This job has expired"*. Conferido por mim na API oficial.
> **Isto NÃO fecha a regra 14:** vaga nova de arte na DreamWorks continua sendo candidatura
> imediata. O que morreu foi esta requisição.
> Texto original mantido abaixo para registro.

#### (texto original da nº 38, mantido só para registro; a entrada está MORTA, veja o aviso acima)

**Link direto:** https://jobs.smartrecruiters.com/NBCUniversal3/744000143937898
**Por que vale:** **visual development** é metade do seu título, no time de longa da DreamWorks. **Reconferida no ar hoje na API oficial do SmartRecruiters: "DreamWorks Feature - Visual Development Artist", Glendale.**
**A parede:** verificação humana do SmartRecruiters (desafio de deslizar) contra IP de automação.
**Tempo estimado:** 4 min

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Upload resume / cover letter | os dois PDFs |
| Nome, email, telefone, localização | dos DADOS FIXOS |
| LinkedIn / Portfolio | dos DADOS FIXOS |
| Autorizado a trabalhar nos EUA? | `No` |
| Precisa de patrocínio? | `Yes` |
| Aceita realocar para Glendale? | `Yes` |
| Pretensão | `Open to aligning with your band for the role; as a reference, around USD 100,000 per year.` |
| Self-ID | `I choose not to disclose` |
| Carta / mensagem | TEXTO A |

**Cuidados:** é híbrido com três dias no escritório e presencial nos EUA, ou seja, depende de patrocínio — daí a posição na terceira banda.

## 39. Netflix Animation Studios — Head of Character Effects (CFX) — Sydney, Austrália

**Link direto:** https://explore.jobs.netflix.net/careers/job/790317396721
**Por que vale:** mesma vaga da nº 31 no outro estúdio; a Austrália é rota de visto mais direta que a americana e o formulário é o mesmo, então custa um minuto.
**A parede:** reCAPTCHA invisível no envio.
**Tempo estimado:** 2 min
**Não reconferida hoje** (a irmã de Vancouver foi, e é a mesma requisição em outro estúdio).

**Cole nos campos:** exatamente os mesmos da nº 2.

**Cuidados:** **não aplique** na `790317298520` (Character Modeling Supervisor, Sydney): você já aplicou nela em 31/08.

## 40. One Of Us — Modeller — Paris, França (híbrido, contrato)

**Link direto:** https://jobs.workable.com/view/2rTHdox84n1Ge86ez2adUb/hybrid-modeller-in-paris-at-one-of-us
**Por que vale:** casa de VFX de cinema premiada, com estúdios em Londres e Paris, e esta é a vaga de MODELAGEM, o cargo que o briefing define como o seu. O quadro tem três da disciplina em Paris (Modeller, Texture Artist e Look Development Artist) e **manda-se só esta**, para a casa não receber três do mesmo candidato. **Não há veto de residência nem no anúncio nem no formulário**: a única pergunta de visto é `Do you require sponsorship to work in France?`, e perguntar não é vetar.
**A parede:** Turnstile da Cloudflare, a caixinha **Verify you are human**. Medida por mim em 08/09 às 08h05: preenchi o formulário inteiro e cliquei em Submit application de verdade; o botão congelou em *Submitting...*, a caixinha apareceu por marcar e nenhum POST saiu. Desafio de clique não se contorna, então esta é sua de direito. **Nada foi enviado** e a garra foi solta na sequência.
**Tempo estimado:** 4 min
**Reconferida hoje, 08/09**: anúncio `published` na API do Workable, Paris, Île-de-France.

**Como é a tela:** o anúncio abre na aba *Overview*; clique em **Apply now** e o formulário abre por cima.

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| First name / Last name / Email | DADOS FIXOS |
| Phone | opcional nesta casa, pode deixar em branco |
| Address (obrigatório) | `Olinda, Pernambuco` |
| Resume (obrigatório) | o PDF do CV |
| *Please provide your showreel of production work and necessary passwords* | `https://www.artstation.com/viniciuscavalcanti (no password required)` |
| *Please provide your Linkedin profile* | `https://www.linkedin.com/in/vinicavalcnti/` |
| *What is your current notice period?* | `One month notice from my current contract.` |
| *What are your salary expectations per annum before tax?* | `Open to aligning with your band for the role; as a reference, I'm looking at around EUR 45,000 per year.` |
| *Do you require sponsorship to work in France?* | **YES** (é a verdade) |
| Caixa da Privacy Notice | marcar |

**Carta (obrigatória nesta casa), cole inteira:**

```
Dear One of Us team,

I am writing about the Modeller role in Paris. I am a Senior 3D Character Artist with more than ten years in stylized characters, and modelling is the part of the pipeline I have owned end to end for most of that time.

For almost five years I have been with E-Line Media in Arizona, taking Endstar's hero characters from first sculpt to engine: sculpt, retopology, UVs, baking, PBR texturing, look development and engine integration. On The Wingfeather Saga season 1 at Angel Studios I modelled and hand-painted the characters, so the surface treatment was mine from block-in to final. Before that I spent three years at PUGA Studios delivering characters under another studio's art direction, in the client's defined style, with revision rounds as routine, which is the working relationship a film facility asks for.

I deliver the whole asset rather than one stage of it: high poly, retopology, UVs, bake, texture, LODs and engine. I have been Senior for five years, I review other artists' work and set the asset standard, and I founded and run my own character art school. My tools are ZBrush, Substance Painter and Designer, Maya, Marmoset, Houdini for grooming, and both Unreal and Unity.

My portfolio holds more than 45 projects with over 60 characters across many titles.

I want to relocate and I am fully open to moving to Paris for the role. I would need visa sponsorship in France. My academic background, with an honours laurea, a postgraduate specialization, a master's in progress, IELTS and publications, makes a strong case for it.

Portfolio: artstation.com/viniciuscavalcanti
LinkedIn: linkedin.com/in/vinicavalcnti

Thank you for your time.

Vini Cavalcanti
```

**Cuidados:** as outras duas da mesma casa (Texture Artist e Look Development Artist, também em Paris) ficam **de fora de propósito**, uma por casa. As vagas de arte em Bengaluru estão fora do recorte geográfico.

---

## ~~41. Quantic Dream — Candidature Spontanée — Paris, França (CDI)~~ — SAIU: É A MESMA VAGA DA nº 27

> **Duplicata exata, e o defeito é do arquivo, não da casa.** As duas entradas apontam para o
> mesmo uuid do Lever, `cc1dacb2-01b7-47c0-b827-9b9b786d1dd7`. Conferido caractere a caractere.
> **Faça a nº 27 e pule esta.**

#### (texto original da nº 41, mantido só para registro; é duplicata da nº 27, veja o aviso acima)

**Link direto:** https://jobs.eu.lever.co/quanticdream/cc1dacb2-01b7-47c0-b827-9b9b786d1dd7/apply
**Por que vale:** casa de Detroit Become Human, Heavy Rain e Beyond Two Souls, ou seja jogo narrativo onde o rosto e a performance do personagem são o produto. É CDI, contrato efetivo francês, e não contrato de projeto. Candidatura espontânea conta pela regra da campanha. **Conferida viva em 08/09** na API oficial (`api.eu.lever.co/v0/postings/quanticdream` devolve três vagas; as outras duas são QA em Montréal).
**A parede:** hCaptcha de imagem do Lever. Medida por mim em 08/09 às 08h50: preenchi tudo e cliquei em Submit de verdade; apareceu o quebra-cabeça *"Find items that need what's shown in the reference to operate"*. **Nada foi enviado** e a garra foi solta.
**Tempo estimado:** 2 min
**É a mais barata desta fila inteira.** Só nome e email são obrigatórios, e **não há uma única pergunta customizada**: nada de visto, nada de salário, nada de carta.

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| Full name | `Vini Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Phone | DADOS FIXOS |
| Current location | `Olinda, Pernambuco` (o campo é opcional e o autocompletar do Lever pode não sugerir nada; se não sugerir, deixe em branco) |
| Current company | `E-Line Media` |
| Resume/CV | o PDF do CV, e espere aparecer **Success!** ao lado antes de seguir |
| Portfolio URL | `https://www.artstation.com/viniciuscavalcanti` |
| LinkedIn URL | `https://www.linkedin.com/in/vinicavalcnti/` |
| Other website | `https://vinicavalcanti.com` |

**Cuidados:** **não existe caixa de carta neste formulário**, então quem fala por você é o CV mais o ArtStation. Não use o botão *Apply with LinkedIn*, que sobrescreve o que você digitou com os dados do perfil.

---

## 42. Eidos-Montréal — LEAD ENVIRONMENT ARTIST — Montréal, Canadá (permanente, presencial ou híbrido)

**Link direto:** https://jobs.dayforcehcm.com/en-CA/eic/CANDIDATEPORTAL/jobs/2192 (Req #158)
**Por que vale:** casa AAA de Deus Ex, Shadow of the Tomb Raider e Guardians of the Galaxy, no 400 de Maisonneuve Ouest. **PERMANENT FULL-TIME**, que é o formato fixo que você procura, num RPG em Unreal Engine 5. Busca literal de veto no texto integral (`authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`, `days a week`, `French`, `français`, `bilingue`, `resident`): **nenhum**. Pede 5+ anos (você tem 10+), Maya, pipeline PBR de textura e material, modelagem, UV, bake, hard-surface e orgânico, e mentoria de júnior. É **ambiente e não personagem**, mas o pipeline pedido é o seu inteiro.
**A parede:** reCAPTCHA v2 **de imagem**, e ela só aparece **DEPOIS** do clique em Submit. Medida por mim em 08/09 às 15h49: preenchi o assistente inteiro, marquei o aceite, cliquei em Submit de verdade, e subiu o quebra-cabeça *"Select all images with a bus"*. **Nada foi enviado.** Terceira família de ATS da campanha com esse padrão, junto de Workable e Lever.
**Tempo estimado:** 6 min — o formulário inteiro já está mapeado abaixo, campo a campo, então é só colar.

**O caminho, que não é óbvio:** na página da vaga clique **Apply** → a tela oferece **"Apply without an Account"**, escolha essa (não precisa criar conta) → abre um **modal de Privacy Notice**: marque a caixa e clique **Save**, *não* Next → só então o formulário monta.

**Passo 1 de 3 — Candidate Info.** Suba o **CV primeiro**: o Dayforce faz o *parse* do PDF e **reescreve o bloco Personal Information inteiro**, apagando o que você tiver digitado antes. Depois de subir CV e carta, preencha:

| Campo | O que colar |
|---|---|
| Email Address | `contact@vinicavalcanti.art` |
| Confirm Email Address | `contact@vinicavalcanti.art` |
| First Name | `Vini` |
| Last Name | `Cavalcanti` |
| LinkedIn Profile | `https://www.linkedin.com/in/vinicavalcnti/` |
| Country dialing code | `🇧🇷 +55 Brazil` |
| Mobile Phone Number | DADOS FIXOS, **só os dígitos**, porque o seletor de país é separado |
| Preferred Contact Method | `Email` |
| Country | `Brazil` |
| State/Province | `Pernambuco` |
| City | `Olinda` |
| How did you find out about this job opportunity? | escolha **Company Website** se existir na lista; se você escolher **Other**, nasce um campo obrigatório novo |
| Additional Details (só aparece se a resposta acima for Other) | `Studio careers page` |
| Resume | o PDF do CV |
| Cover Letter | o PDF da carta |

Feito isso, clique no botão **Update** do próprio bloco Personal Information (ele é um sub-formulário e tem botão próprio), espere aparecer *"Personal Information update successful."* e só então **Next**.

**Passo 2 de 3 — Questionnaire.** Duas perguntas, e a primeira é a de autorização:

| Pergunta | Resposta |
|---|---|
| Are you currently authorized to work in Canada? | **No** — é a verdade e não se mente nesse campo |
| If you're not in Quebec, are you willing to move within 6 months? | **Yes** |

**Passo 3 de 3 — Submit.** Marque *"I agree to the Candidate Acknowledgement"* e clique **Submit**. É aqui que o quebra-cabeça de imagem sobe; resolva e confirme que a tela de confirmação apareceu antes de fechar.

**Cuidados:** não há campo de carta escrita nem de portfólio neste formulário, então quem fala por você é o CV, a carta em PDF e o que estiver dentro deles — confira que o link do ArtStation está no CV. Não use *Import Resume* depois de preencher à mão, pelo mesmo motivo do parse.

---

## 43. TTK Games AB — CHARACTER ARTIST — Estocolmo, Suécia (híbrido, PERMANENTE)

**Link direto:** https://ttkgames.com/careers/job?id=561860
**Por que vale:** é **o título dele, ao pé da letra**, efetivo e híbrido em Estocolmo, com **faixa salarial publicada: 34.000 a 47.000 SEK por mês mais bônus**. A busca literal de veto no anúncio inteiro não devolveu **nenhuma** palavra. Achada hoje na caçada da web aberta; a campanha não tinha esta casa.
**A parede:** reCAPTCHA **invisível**, e **não é quebra-cabeça**. Medido por mim em 08/09: preenchi tudo e cliquei em *Submit application*; o `POST /api/pinpoint/apply` voltou **500 com o corpo literal `ReCaptcha Failed`**. É a sessão automatizada sendo reprovada pelo IP de datacenter, a mesma assinatura da Netflix e da Moonmana. **Do seu navegador isso não acontece** — não há nada para resolver, é preencher e clicar.
**Tempo estimado:** 2 min. É das mais baratas da fila.

**ARMADILHA DE ENDEREÇO, que custou duas rodadas:** os links `.../jobs/561860` e `.../postings/<uuid>` do Pinpoint **redirecionam por JavaScript** para `ttkgames.com/careers` e a vaga parece morta. **A porta de verdade é o link acima**, com `?id=`.

**Cole nos campos:**

| Campo | O que colar |
|---|---|
| First Name | `Vini` |
| Last Name | `Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Link to Portfolio/LinkedIn | `https://www.artstation.com/viniciuscavalcanti` |
| Upload CV (20 Mb máx, pdf/doc/docx) | o PDF do CV |
| I have read and agree to the Privacy Policy | **marcar** |

**Não há campo de carta, de salário nem de visto neste formulário** — são seis campos e pronto.

---

## ~~44. Behaviour Interactive — Senior 3D Character Artist, *7 Days to Die*~~ — SAIU: JÁ FOI ENVIADA EM 30/08

> **O próprio arquivo se contradizia**, e a revalidação pegou: os blocos de "Cuidados" das
> entradas nº 1 e nº 3 já diziam que esta tinha sido enviada. **O Gmail fecha a dúvida:** recibo do
> Lever em **30/08 às 02h29**, `no-reply@hire.lever.co`, com o texto literal *"we received your
> application for Senior 3D Character Artist - 7 Days to Die"*. Candidatura existe.
> **Não mande de novo.** As outras três requisições da Behaviour nesta fila continuam valendo.
> Texto original mantido abaixo para registro.

#### (texto original da nº 44, mantido só para registro; ela JÁ FOI ENVIADA, veja o aviso acima)

**Link direto:** https://jobs.lever.co/bhvr/976b2a8c-9cb4-4066-a755-d0994af408c2
**Por que vale:** requisição **nova**, publicada em 25/08, e **não é nenhuma das outras três da Behaviour** que já estão nesta fila — o dedupe foi feito pelo uuid da requisição, não pelo título. Busca literal de veto: **nenhuma**; o único `fran` do texto é a palavra *franchise*, e não exigência de francês.
**A parede:** hCaptcha de imagem do Lever, **só depois do clique em Submit** — a mesma já medida com clique real na própria Behaviour e na Quantic Dream.
**Tempo estimado:** 4 min. **Aproveite que já vai abrir o Lever da Behaviour para as outras**, e use as mesmas respostas da entrada nº 1 desta fila.

---

## 45. Blue Zoo Animation — BLENDER MODELLER (Experienced) — Londres, Reino Unido

**Link direto:** https://careers.blue-zoo.co.uk/vacancies/vacancy-apply.aspx?VacancyID=1310
**Por que vale:** estúdio londrino conhecido, e a descrição diz que o time de modelagem e textura constrói *"the environments, props, **characters**"*. **Busca de veto com a régua nova de treze termos: nenhum.** E há um sinal que vale ouro neste quadro: a Blue Zoo **rotula explicitamente** as vagas restritas com o prefixo **"UK Only |"** — a Senior Blender Lighting ao lado tem o rótulo, **esta não tem**. Vaga sem rótulo num quadro que rotula é sinal real.
**Ressalva honesta:** o dia a dia é *"stylised environment and prop assets"*, ou seja **ambiente e props**, não personagem. Entra como média pela regra de disciplina.
**A parede:** **não é captcha** — conferido de novo em 09/09, zero `iframe` de captcha e zero widget (`{"fr":[],"w":0}`). É que a candidatura **exige criar conta**, e o cadastro tem dois campos que a automação não vence.

**CORREÇÃO DE 09/09, medida em cinco rodadas de navegador, porque a descrição antiga estava errada
e faria você perder tempo:** o resto do cadastro **passa inteiro pela automação**. Nome, sobrenome,
os dois emails, origem "Our Careers Website", os três radios, as duas caixas de consentimento e a
senha ficaram todos preenchidos e lidos de volta, e o botão Register foi clicado três vezes. O que
trava, sempre, é só isto:

> `Preferred Specialism is a required field` · `Preferred Location is a required field`

E o motivo é específico: **esses dois não são `<select>` e não são janela**. São um *itemPicker* do
jQuery UI, com um `<button>` "Select" (`..._CanC_PreferredIndustry1_btnChange` e
`..._CanC_PreferredLocation1_btnChange`), um input de texto `txtMyBox` e um campo **oculto**
`hdnValue`, que fica em `0` e é o que o servidor lê. Medido: o botão existe no DOM mas responde
`Element is not visible`, e toda a cadeia de pais dele tem `offsetHeight: 0`, ou seja o bloco é
renderizado colapsado; clicar pelo DOM não abre janela nenhuma; e digitar `mod` e `lon` no
`txtMyBox` **não produz sugestão** (zero menu de autocomplete). Sem clique numa sugestão, o
`hdnValue` continua `0` e o cadastro nunca fecha.

**Ou seja: no navegador de verdade, com o widget desenhado na tela, isto são dois cliques seus.
Na automação é parede.** Escolha `Modelling` (ou o mais próximo que a lista mostrar) no Specialism
e `London` no Location.

**Tempo estimado:** 3 min, e o resto do formulário provavelmente já vai estar preenchido pelo
navegador se você usar os valores da tabela abaixo.

**Cole no cadastro** (o link acima redireciona para `registration.aspx`):

| Campo | O que colar |
|---|---|
| How did you hear about us? | `Our Careers Website` |
| First Name | `Vini` |
| Last Name | `Cavalcanti` |
| Email / Confirm Email | `contact@vinicavalcanti.art` |
| Password | a senha padrão da campanha (documento privado do Drive) |
| Do you currently work for us? | **No** |
| Have you previously worked for us? | **No** |
| Showreel/Website URL | `https://www.artstation.com/viniciuscavalcanti` |
| Showreel/Website Password | `No password, the portfolio is public.` |
| Stay in the loop about upcoming roles? | **Yes** |
| Data Privacy (I Agree) e "The information I have provided is accurate" | **marcar as duas** |
| **Preferred Specialism** | **é seu, escolha você** — é um seletor próprio que abre uma janela; a opção de modelagem é a certa e eu não chuto especialismo |
| **Preferred Location** | **London** |

**QUATRO ARMADILHAS QUE EU JÁ PAGUEI, para você não pagar:**
1. **O banner de cookies é um `input[type=submit]` do ASP.NET.** Aceitar dispara um postback que **recarrega a página e apaga tudo que já foi digitado**. **Aceite o cookie ANTES de escrever qualquer coisa.**
2. **Há DOIS campos de senha na tela**, um do cadastro e outro da caixa de login na lateral. É fácil digitar no errado.
3. **Os campos de email disparam uma validação por AJAX que re-renderiza o formulário.** Marque os radios e as caixas **depois** de preencher os emails, não antes.
4. **O formulário revela obrigatórios novos a cada tentativa.** Não é erro seu: satisfaça os que ele apontar e envie de novo.

---

## 46. TTK Games AB — LEAD ENVIRONMENT ARTIST — Estocolmo, Suécia (híbrido, PERMANENTE)

**Link direto:** https://ttkgames.com/careers/job?id=562172
**Por que vale:** é **liderança de arte de ambiente**, efetiva e híbrida em Estocolmo, e a casa
**publica a faixa**: *"Salary range Starting from **60,000 SEK per month**, rising to 85,000 with
experience, plus bi-annual bonus, and perks."* Pela regra de 04/09 se pede a BASE: **60.000 SEK por
mês**, com "Open to aligning with your band for the role". O anúncio pede direção artística,
retorno e mentoria para o time de ambiente, mais coordenação da produção.
**Régua de dezessete termos, rodada no anúncio inteiro: NENHUM.** Zero ocorrências.
**A parede é a mesma da nº 43:** reCAPTCHA invisível, sem quebra-cabeça. Preencher e clicar.
**APROVEITE A ABERTURA:** você já vai estar no formulário da TTK pela nº 43. **É o mesmo site e o
mesmo formulário**, então esta custa mais um minuto, não mais dois.

---

## 47. Epic Games — PRINCIPAL ENVIRONMENT ARTIST — Cary, Carolina do Norte, EUA

**Link direto:** https://job-boards.greenhouse.io/epicgames/jobs/6121292004
**Achada em 09/09 de madrugada**, numa varredura de 2.934 slugs de Greenhouse. **Não estava no
censo de 07/09**, ou seja é requisição que a campanha nunca tinha visto. Atualizada em 13/08.
**Régua de dezessete termos: nenhum veto.** O único `authoriz` do texto é o aviso antiagência
(*"Epic does not accept any unsolicited resumes from any unauthorized third party"*), falso
positivo conhecido. **Dedupe por ID: zero ocorrência** no painel, no `enviados.csv` e no
`processados.csv`.

**A parede, medida com navegador, e ela é do QUADRO e não da vaga:** o `job-boards.greenhouse.io`
da Epic devolve *"One more step. Please complete a security check to continue"*, com Session ID e
o IP na tela. É muro de bot contra IP de datacenter, **não** captcha de desafio. **No seu
navegador isso não acontece.** O preenchedor morreu esperando o campo `first_name` por 60 s.

**LEIA ISTO ANTES DE CLICAR, porque é decisão sua:** a campanha **já tem quatro candidaturas
confirmadas na Epic**, de 31/08 e 03/09, e três delas no time de outsourcing (Modeling Outsource
Lead em Cary, em Montréal e na operação brasileira, mais Hard Surface Outsource Lead). Esta é de
**outro time**, Environment Art, e de nível **Principal**, acima do que você já pleiteou, então
não é o caso de "quinta inscrição no mesmo time num nível abaixo" que a campanha decidiu evitar.
Ainda assim é a quinta na mesma casa, e quem decide isso é você.

**Respostas:** as mesmas das quatro anteriores da Epic, que estão em `respostas-formularios.md`:
precisa de patrocínio de visto, nunca trabalhou na Epic, E-Line Media como empregador atual.

**A irmã, se esta for sênior demais:** Senior Environment Artist, mesma casa e mesma cidade,
`https://job-boards.greenhouse.io/epicgames/jobs/6001731004`. **Mande só uma das duas**, e a regra
da campanha é mandar na mais alta.

---

## ~~51. Absurd Ventures — CHARACTER ART LEAD~~ — ✅ **ENVIADA EM 12/09 ÀS 11h24 UTC. NÃO REFAÇA.**

> Enviada pelo maestro no mesmo dia em que o Jhon B a achou. **Prova tripla**: a URL terminou
> em `/jobs/5236256007/confirmation`, a página respondeu *"Thank you for applying to Absurd
> Ventures"*, e às **11h22m05** chegou o recibo por email. Código de segurança `BPjwpS7x`,
> pedido às 11h21m34 e atendido às 11h21m45.
>
> **CORREÇÃO DE MÉTODO, e ela muda o dedupe desta casa.** Este dossiê dizia que *"o recibo por
> email desta casa é mudo, ele não nomeia a requisição"*. **Isso valia só para as espontâneas.**
> O recibo da vaga nomeada chegou assim, com todas as letras:
>
> > *"Thank you for applying to our **Character Art Lead** role here at Absurd Ventures."*
>
> Contra o das espontâneas de ontem, que diziam apenas *"Thank you for submitting a general
> application"*. Ou seja: **o Greenhouse nomeia a vaga quando há vaga a nomear**, e o silêncio
> do recibo era propriedade da porta espontânea, não da casa. Para o dedupe futuro isto
> importa: nesta casa dá para separar candidatura espontânea de candidatura a requisição
> **pelo próprio recibo**, sem depender do arquivo.
>
> **A primeira tentativa foi RECUSADA pelo próprio formulário e não enviou nada**, o que é
> bom: nenhuma duplicata, nenhum código gasto à toa. Faltavam dois campos obrigatórios que
> este dossiê não tinha visto, e os dois viraram conserto no `apply-greenhouse.js`:
>
> 1. **`Discipline` é campo da seção Education**, não é `question_*`, então o `answers.json`
>    nem falava dele e o log não acusava nada — o servidor é que dizia *"Discipline is
>    required."* Agora existe um bloco `education` no arquivo de respostas. A opção honesta,
>    entre as 79 da lista, é **`Game and interactive media design`**, porque a formação dele é
>    Game Art Specialist (PG Dip) pela Melies São Paulo.
> 2. **O "multi-select" do Greenhouse é GRUPO DE CHECKBOX**, não `<select>`. Cada opção tem id
>    próprio `<name>[]_<idDaOpcao>`, então procurar por `#question_12881396007[]` devolvia
>    `null` e o log dizia apenas `missing`. Marcadas **Unity + Unreal 5**.
>
> **E um terceiro defeito, que era o mais perigoso dos três:** a leitura de volta desse campo
> imprimia o rótulo inteiro da pergunta (*"... Unity Unreal 4 Unreal 5 Other None"*) como se
> fosse a resposta, porque existe um elemento com o id do grupo e o teste caía no ramo do
> react-select. Isso é pior que não conferir, porque dá ao operador a impressão de que
> conferiu. Agora o grupo de checkbox é testado PRIMEIRO e só o `.checked` conta — a leitura
> de volta do envio bom diz `Unity + Unreal 5`.

### Texto original da entrada, mantido para referência

## 51. Absurd Ventures — CHARACTER ART LEAD — Santa Monica, Califórnia, EUA (efetiva, presencial)

**Link direto (fonte oficial, o ATS da própria casa):**
https://job-boards.greenhouse.io/absurdventures/jobs/5236256007

**Requisição `5236256007`, `internal_job_id` `4680308007`.** Publicada em **2026-09-11T19:11:12-04:00**
e o `updated_at` é o mesmo carimbo, ou seja **não é anúncio refrescado, é vaga nova de ontem**.
Conferida viva nesta rodada: a API devolveu 200 e a página pública também.

**Por que ela é a primeira da fila:** é a disciplina exata dele com o título mais alto que ele pode
pleitear. O corpo é personagem do começo ao fim — *"lead our character art team and help define the
visual quality and direction of our characters"*, *"setting artistic and technical standards"*,
*"Evaluate character art at key stages of development"*, *"7+ years of professional character art
experience in the video game industry"*. Nenhuma linha de ambiente, prop ou hard surface.

**Faixa publicada, e ela manda na pretensão:** *"The base pay range for this position is $150,000 to
$185,000 per year."* Pela política de 04/09, **pede-se a BASE: USD 150.000**. Não há campo de salário
neste formulário, então isso só entra se alguém perguntar depois.

### Régua de veto, termo a termo, no texto INTEIRO baixado pela API (não na listagem)

| Termo | Frase inteira, como está escrita | Veredito |
|---|---|---|
| `eligib` | *"Certain roles may also be **eligible** for bonus and equity."* | **Falso positivo.** É benefício, não elegibilidade para trabalhar. |
| `within the` | *"make effective decisions **within the** constraints of a large game production"* | **Falso positivo.** |
| `on-site` / `located` | *"Full-time job with benefits. Role is **on-site** in Santa Monica, CA. Office is **located** near downtown Santa Monica"* | **Restrição de presença, não veto de candidatura.** Ele quer realocar. |
| `authoriz`, `sponsor`, `work permit`, `must be based`, `based in`, `only from`, `LMIA`, `resident`, `citizen`, `relocat`, `unable to support`, `no relocation`, `days a week`, `days per week`, `days in the office`, idioma local | **nenhuma ocorrência** | — |

**Veredito: zero veto escrito.** A casa não promete patrocínio e não o proíbe; pelo briefing isso é
contexto, não critério de descarte.

### Dedupe, feito no minuto do achado

`sh automacao/dedupe-agora.sh 5236256007 "Absurd"` → **ID inédito nos quatro arquivos.** A casa tem
histórico e ele NÃO bloqueia esta: as duas candidaturas de 11/09 são espontâneas de outras
requisições (`4141408007` General Game Development às 19h04 e `4141404007` Animated Series às 21h22).
**Conferido também no Gmail, por janela de tempo e não por remetente** (`Absurd newer_than:3d`): os
dois recibos de `no-reply@us.greenhouse-mail.io` dizem *"Thank you for submitting a general
application"* e **nenhum nomeia Character Art Lead**. Rota livre.

**Cadência:** a casa recebeu duas candidaturas ontem e nenhuma hoje. A terceira porta espontânea
(`4141225007`, Film & TV) estava adiada para "outro dia" — **não mande as duas no mesmo dia**. Entre
a espontânea e a vaga nomeada de personagem, a nomeada ganha, e com folga.

### O formulário, campo a campo (ids DESTA vaga — eles mudam de vaga para vaga no Greenhouse)

| Campo | `name` | Resposta |
|---|---|---|
| First / Last / Email | `first_name`, `last_name`, `email` | Vini · Cavalcanti · contact@vinicavalcanti.art |
| Phone (opcional) | `phone` | variável de ambiente `VINI_TEL` |
| Resume/CV (**obrigatório**) | `resume` | `Vini_Cavalcanti_CV.pdf` |
| Cover Letter (opcional, **mandar**) | `cover_letter` | PDF gerado de `carta_absurd_charlead.txt` |
| Website or portfolio link (**obrigatório**) | `question_12881389007` | https://www.artstation.com/viniciuscavalcanti |
| Work samples (opcional) | `question_12881390007` | deixar vazio: há campo de link, e o ArtStation tem prioridade sobre o PDF |
| LinkedIn | `question_12881391007` | https://www.linkedin.com/in/vinicavalcnti/ |
| **Lawfully authorized to work in the US?** | `question_12881392007` | **No** (é a verdade, regra 8) |
| Located in the Los Angeles area? | `question_12881393007` | **No** |
| Open to relocating to LA? | `question_12881394007` | **Yes.** |
| Willing to come into the Santa Monica studio 5 days/week? | `question_12881395007` | **Yes.** |
| Which engines? (**multi-select**) | `question_12881396007[]` | **Unreal 5** e **Unity** |
| How many games have you shipped? | `question_12881397007` | `5-10` (é `input_text` aqui; na espontânea de ontem era `select` e foi escolhido 5-10) |

**Duas ressalvas medidas, para não virar envio silenciosamente errado:**
1. **`question_12881396007` é `multi_value_multi_select`.** O preenchedor trata combo como escolha
   única. **Confira no print se ficaram marcadas as DUAS** antes de aceitar o resultado.
2. **Este quadro pede CÓDIGO DE SEGURANÇA por email** (medido ontem duas vezes:
   `fOWTy8p9` às 19h02 e `gR3eoHvV` às 21h21, de `no-reply@us.greenhouse-mail.io`). Cada clique em
   Submit gera um código NOVO e mata o anterior: rode em segundo plano, espere o
   `needcode_absurd-charlead.txt`, só então leia o código mais recente no Gmail e grave
   `code_absurd-charlead.txt` com a sessão viva.

### Comando exato de disparo

```
cd /home/user/apply
CARTA_TXT=/home/user/apply/carta_absurd_charlead.txt \
CARTA_PDF=/home/user/apply/carta_absurd_charlead.pdf \
sh hb_run.sh carta_pdf.js

sh automacao/dedupe-agora.sh 5236256007 "Absurd"      # refaça no MINUTO do clique

cd /home/user/apply
VINI_TEL="<telefone, do doc privado do Drive>" \
sh hb_run.sh apply-greenhouse.js \
  "https://job-boards.greenhouse.io/absurdventures/jobs/5236256007" \
  absurd-charlead ans_absurd-charlead.json --submit
```

Sem `--submit` ele preenche, tira print e mostra a leitura de volta sem enviar. **A carta e o
arquivo de respostas já estão escritos** em `/home/user/apply/carta_absurd_charlead.txt` (250
palavras, sem capslock, sem a palavra proibida, uma única linha de realocação) e
`/home/user/apply/ans_absurd-charlead.json`.

**Prova de envio que vale aqui:** URL terminando em `/jobs/5236256007/confirmation` **ou** o texto
*"Thank you for applying to Absurd Ventures"*. O recibo por email desta casa é **mudo** — ele diz
apenas *"Thank you for submitting a general application"* e **não nomeia a requisição**, medido nos
dois de ontem. Então a prova é a URL somada ao horário.

---

# O QUE FICOU DE FORA, E POR QUÊ

Para você não gastar minuto reabrindo o que já foi decidido.

**Já enviadas (não repita):** Sony Pictures Imageworks (Texture, Modeler, Look Dev, Expression of Interest), 3Doubles Producciones, Bongfish, Juggler Games, Twin Harbour, Mikros, Miam!, Teyon, beffio, Digic, Lightbox, Mattel, Netflix Visual Development Artist Ink, Disney TV Animation Character Design Lead, EA Character Artist 215657, Techland Character Artist (enviada em 31/08 pelo portal oficial — as duas fichas REF64D do SmartRecruiters são a mesma requisição, então ficaram fora), **Ubisoft Montréal — Senior Character Artist (Rainbow Six Siege)** (id `744000145282762`, ref `REF31793B` — enviada em 30/08 e **RECUSADA em 02/09**; a casa publica o mesmo anúncio em francês e em inglês com títulos diferentes, o que o disfarçou de vaga nova hoje; **NÃO ENVIAR de novo**), **ICON Creative Studio — Intermediate Modeling/Texture Artist** (enviada em 31/08 — email de `notifications@app.bamboohr.com` confirma o recebimento nomeando o cargo; a entrada do painel usava um link diferente, `iconcreative.bamboohr.com/careers/136`, do que registrou o envio de 31/08, `iconcreativestudio.com/careers`, o que escondeu que era a MESMA e única vaga de modelagem do quadro deles), **Larian Studios — Character Artist (Open Application)** (Lever uuid `64e1e658-7c7a-4c7f-b950-f997d40a9d8e` — confirmação por email de `no-reply@hire.lever.co` hoje às 04h35 UTC) e **Prismatic Studios — 3D Character Artist (IP própria, Auckland)** (enviada e confirmada hoje pelo JHON, resposta de rede `{"success":true,...}` do próprio formulário).

**Sem patrocínio ou com exigência de autorização prévia (chance material zero):** thatgamecompany 3D Character Artist ("unable to sponsor"), Atomic Cartoons CG Designer (exige residência na Colúmbia Britânica desde 2025), Stirling Animation (exige residir no Reino Unido fora de Londres, e é contractor), The Third Floor (exige residência em estado americano listado e E-Verify), People Can Fly (exige residir na Polônia ou no Canadá), Keywords Studios Austrália (remoto só dentro da Austrália), Oddshot (exige morar em Flandres), Gamedia (exige morar a 40 km de Alkmaar), **DreamWorks Animation / NBCUniversal — as DUAS requisições de Montréal, Lead Character Artist (`744000137526729`) e Lead Material Artist (`744000137526669`)** ("Must be legally authorized to work in Canada" + mínimo de 4 dias por semana no escritório, confirmado na API oficial em 07/09), **Image Engine — General Application de Assets, Vancouver** ("Candidates are required to be based in British Columbia and eligible to work in Canada", confirmado no `/careers/21/detail` em 07/09; o veto é do quadro inteiro do BambooHR deles), **Prismatic Studios — 3D Character Artist, Auckland** ("you must have the right to work in New Zealand to be eligible for this position", achado no próprio texto do anúncio em 07/09 — mas ela já está enviada de qualquer forma, ver acima).

**Disciplina que não é sua:** Skydance Environment Modeling Artist (Madri), Highdive Senior Modeler (Toronto, modelagem de cenário), Sandbox Interactive Lead 3D Environment Artist, Netflix Character Designer Ink e Skydance Character Designer (design 2D), Netflix Story Artist e as duas Environment Modeling Supervisor, Riot Manager Concept Art (Singapura), Amuse Concept Designer, Plarium Character Concept Artist.

**Porta é email, não formulário (o Apps Script já cuida):** Cakefish/Dreamthorn Principal Character Artist, THQ Nordic Mobile/HandyGames, Alt.VFX, FIN Design, Nabi Studios, MegaZebra, Supermassive, Little Chicken, Red Rover, Oddshot, RaceWard, The Game Kitchen, Gamedia, Inverge e as demais da fatia de email.

**Idioma eliminatório:** Sony Pictures Imageworks Senior Look Development Artist (Montréal) e Rodeo FX *Artiste de développement visuel Senior* exigem francês fluente — francês já derrubou duas candidaturas desta campanha.

**Porta quebrada ou conta obrigatória:** Gamecan (certificado TLS quebrado do lado deles, ninguém consegue aplicar), ZEILT (exige conta e as vagas pedem endereço fiscal no Québec), Mainframe (UKG Ready com conta de candidato), Ánima Kitchent (InfoJobs exige conta), FIN Design (portal exige conta), EA Vancouver 215788 (a requisição devolve *Internal server error* no lado da EA em cinco tentativas; se quiser tentar, entre na sua conta e veja em *Job Applications* se aparece "Finish your application").

**Quadros que não abriram e não confirmam vaga da sua disciplina:** KingsIsle, PikPok, Velan, Digital Domain, Digital Sun, Electric Theatre, Arkane, Tarsier, Carbonated, PLAYERUNKNOWN, VSTEP.

**Parede que também atrapalha você, ficou por último com ressalva:** Bulkhead Open Application [Remote] — exige **print da aba Most Played do seu perfil Steam** e o contrato é por projeto, fora da sua regra de vaga fixa. Se sobrar tempo no fim das três horas: https://careers.bulkhead.com/jobs/5744150-open-application-remote/applications/new

---

# APÊNDICE DE 07/09, DE MADRUGADA: as paredes que foram medidas DEPOIS que esta fila foi montada

Esta fila foi fechada no começo da noite. Entre aquele momento e as duas da manhã os agentes
mediram mais trinta e três portas que ficam à mão, e nenhuma delas está nas 45 entradas acima.
Conferi uma a uma **pela URL**, e não pelo nome do estúdio, porque casar por nome me deu falso
positivo: a DreamWorks e NBCU aparecia como ausente e já é a entrada 4 e a 18 desta fila.

Duas ficaram de fora de propósito: **Studio Bozzetto**, porque o estúdio já respondeu em 02/09 que
não está contratando e exige presença em Bergamo, e **Dream Games**, que é Istambul e está fora do
escopo geográfico.

## As três que valem a mão primeiro

### A. Rainbow SpA — 3D Modeler **e** Surfacing Artist — Roma e Milão, Itália
**Link:** https://www.rbw-cgi.it/careers/
**É a melhor vaga não enviada da Europa nesta madrugada.** A casa é a das Winx Club, italiana e
grande, e o quadro tem **três portas da sua faixa ao mesmo tempo**: 3D Modeler, Surfacing Artist e
General Application. O formulário é Contact Form 7 **com campo de arquivo de verdade**, então CV e
carta sobem normalmente.
**A parede:** reCAPTCHA v3, de pontuação de sessão. Ele reprova a automação e devolve a tela
genérica *"There was an error trying to send your message"*, que mente sobre o motivo. **No seu
navegador passa direto.** É envio de um minuto.

### B. Bulkhead Interactive — Open Application **IN-STUDIO** — Derby, Reino Unido
**Link:** https://careers.bulkhead.com/jobs/5739695-open-application-in-studio
**Atenção, esta não é a mesma que está no fim da seção "o que ficou de fora".** Aquela é a
[Remote], por projeto. Esta é a **presencial**, e é melhor por três motivos escritos no próprio
anúncio: *"Don't worry, we can sponsor your visa"*, *"This role is 100% on-site"* e **oferece ajuda
de realocação**. Patrocínio dito por escrito é raro e vale mais que quase tudo nesta fila.
**Por que fica com você e não é captcha:** o formulário exige um **print da aba Most Played do seu
perfil Steam**, campo de arquivo obrigatório que só você pode gerar.
**Armadilha medida, confira pela tela:** os dois menus, *Where are you currently based* e *Which
department*, continuam mostrando "Select an option" mesmo depois de marcados por script. Olhe a
tela, não confie no primeiro clique.

### C. Urban Games — Head of Art — Schaffhausen, Suíça
**Link da vaga:** https://www.urbangames.com/career/ · descrição em PDF em https://www.urbangames.com/head-of-art-2
**Porta:** o formulário de contato em https://www.urbangames.com/contact
A casa é a de Transport Fever 3, e além do Head of Art eles convidam candidatura espontânea por
escrito, pedindo uma mensagem que explique o encaixe.
**A parede:** reCAPTCHA v3, e aqui ele foi explícito na tela, em vermelho: *"Invalid form, reCAPTCHA
validation failed"* e *"reCAPTCHA V3 validation failed, suspected as abusive usage"*.
**O formulário NÃO tem campo de arquivo**, então o CV e a carta vão por link, e o texto pronto está
em `automacao/respostas-formularios.md`.

## 48. Volka — 3D ARTIST — Limassol, Chipre — A CASA BANCA A AUTORIZAÇÃO, MAS A PORTA ESTÁ QUEBRADA

**CORRIGIDA POUCO DEPOIS DE ESCRITA, em 09/09, e a correção é minha.** Eu tinha posto esta entrada
dizendo que o "Page not found" era a nossa rede e que bastava você abrir no seu navegador. **Isso
está errado**, e o registro da campanha já tinha a medição melhor: em 08/09 uma rodada abriu a
página com navegador de verdade e contou os pedidos de rede, e não houve **nenhum** pedido falhado,
zero 4xx, zero 5xx. Reproduzi hoje, agora no **quadro inteiro** e não só na vaga:
`jobs.ashbyhq.com/volka` renderiza **"Page not found"** com **zero pedidos com problema**.

**Conclusão honesta: a porta pública desta vaga está quebrada do lado da Ashby, não do nosso.**
Abrir no seu navegador quase certamente mostra a mesma coisa. Se mostrar, não é sinal de nada
sobre você nem sobre a vaga.

**A vaga existe mesmo assim.** A API pública da Ashby continua servindo o quadro da Volka com
quatro anúncios, entre eles `3D Artist | Cyprus, Limassol | isListed: true`, requisição
`fa36e503-daf1-44d8-be2c-260cea2dd300`, sem prazo de encerramento.

**Por que ela vale o incômodo:** a frase de benefício, que quase nenhuma casa escreve.

> *"Relocation Support: Moving countries is stressful. We handle the tickets, accounts and
> **permits** for you and your family. We provide temporary accommodations while you're getting
> settled, cover the first rent of your own apartment and help with necessary furnishings."*
> Mais: *"Language Learning + **Naturalization Support**"*. E a casa mantém vaga aberta de
> *Immigration Specialist*.

**Encaixe, sem maquiar:** é **ambiente estilizado low poly** para o time de marketing, não
personagem, e pede 2 anos quando ele tem mais de 10. Régua de vinte termos: dois casamentos, os
dois falsos positivos (`relocat` é a frase a favor acima, `located in` é endereço). Sem veto.

**O QUE FAZER, já que o formulário não abre:** o site próprio, `volka.com/careers/`, responde 200
mas monta a lista em JavaScript e **não publica email nenhum no HTML**. Então isto é trabalho de
navegador seu: abrir `volka.com/careers/`, ver se a lista renderizada oferece uma rota de
candidatura que não seja a Ashby quebrada, e, se não oferecer, procurar o contato de recrutamento
por lá. **Prioridade baixa pelo encaixe, mas alta pela frase de realocação**, e por isso está
escrita e não descartada.

---

## 49. Crater Studio — convite aberto a Artists — Belgrado, Sérvia — PORTA É EMAIL, NÃO FORMULÁRIO

**Link:** https://craterstudio.com/jobs · **Email publicado:** effects@craterstudio.com

O texto da própria página diz *"Please apply via job application form - register your interest"*,
mas **o formulário não existe na página**. Abri com navegador de verdade em 09/09, rolei até o fim
e li o DOM: **zero campo de formulário, zero link de candidatura**. O único contato publicado é o
`effects@craterstudio.com` e dois telefones. Régua de vinte termos: zero casamento.

**Consequência prática:** isto não é fila de formulário, é **carta**, e carta fria nova é sempre
rascunho pela regra da campanha. Fica registrado aqui para a próxima rodada não gastar navegador
procurando um formulário que a página promete e não tem.

---

## 50. Playdead — ZBrush Modeler — Copenhague, Dinamarca — **ENVIADA PELA AUTOMAÇÃO EM 18/09 ÀS 20h38 UTC, SAIU DA SUA FILA**

> **FECHADO, não clique.** A candidatura saiu na rodada das 20h15 de 18/09 com três provas: **POST 204** em
> `app.breezy.hr/api/apply/3be060a4fcf301`, URL final em `/apply/submitted` com o texto literal *"Application
> Submitted. Your application has been submitted successfully. Good luck!"*, e recibo no Gmail às 20h38m58 de
> `candidate-5023de215a1b01@playdead.breezy-mail.com`. Ela entrou porque a rodada leu **11.015 vagas** (janela de
> 4 h por API, casas grandes, cinco famílias novas e os alertas da caixa) e **não existe vaga de personagem nova**
> — é a regra de 10/09 aplicada ao pé da letra: ambiente por último, e só quando não houver personagem.
> **DUAS CORREÇÕES NO TEXTO ABAIXO:** (1) o comando de disparo aponta para `apply_breezy.js`, que **não existe**
> em `/home/user/apply` — o que funcionou foi o `apply_own.js`, que já existia, com três capacidades novas
> (`arquivos`, `marcar`, `proximo`) e o arquivo `ans_playdead.json`; (2) a data de publicação **mudou** de
> 2026-09-10 para **2026-09-14** no MESMO id, porque o Breezy move o `published_date` no republish.


> **Leia esta linha antes de tudo:** a caça das 15h45 de 10/09 leu **359 quadros e 9.345 vagas** e
> **não achou UMA vaga de personagem nova no mundo**. **Só sobrou ambiente**, e é esta. Ela está
> aqui em último lugar de propósito. **Se houver qualquer coisa de personagem em pé** — a Razer
> `JR2026007640`, a Skydance Grooming `9ad28cab` do item 23, ou qualquer uma das travadas por
> captcha — **essa vai primeiro e esta espera.** Dossiê completo em `automacao/caca-1545-1009.md`.

**Anúncio:** https://playdead.breezy.hr/p/3be060a4fcf301-zbrush-modeler — **HTTP 200 hoje**
**Candidatura:** https://playdead.breezy.hr/p/3be060a4fcf301-zbrush-modeler/apply — **HTTP 200 hoje**
**ID da requisição (Breezy):** `3be060a4fcf301` · **Publicada em 2026-09-10, hoje** · `Full-Time`,
presencial em Copenhague.

**POR QUE É AMBIENTE, e não modelagem que sobe pela regra 2.** As palavras *character* e *creature*
**não aparecem uma única vez** no anúncio. O que ele pede, colado:

> *"Your responsibility as our new colleague will be to create and sculpt high quality
> **architectural and organic models within a 3D open world environment**."*
> *"Creating and sculpting high quality architectural and organic models to produce **believable
> locations** within a large, open world."*
> *"Collaborating with other artists and designers to support **level design and construction**."*

**RÉGUA DE VETO, termo a termo, sobre o corpo inteiro:** `authoriz` 0 · `eligib` 0 · `sponsor` 0 ·
`work permit` 0 · `must be based` 0 · `LMIA` 0 · `days a week` 0 · `citizen` 0 · `resident` 0.
**Zero veto escrito.** `visa` 1 e `relocat` 1, e os dois são **a favor**, na mesma frase:

> *"You should be willing to work at the Playdead office in Copenhagen, Denmark. **We can offer
> relocation and visa support if required.**"*

**DEDUPE** (`sh automacao/dedupe-agora.sh "3be060a4fcf301" "Playdead"`): o ID tem **zero ocorrência**
nos quatro arquivos, requisição inédita, nenhuma marca de envio. A **casa** já recebeu duas
candidaturas, em 06/09 (`d6b5a5e4f54a01`, Material and Texture Artist, confirmada) e em 08/09 —
**não é parede**, o Breezy deles não tem captcha nenhum.

**ARMADILHA MEDIDA HOJE NO `/apply`:** o honeypot **`hp_7f2b`** aparece 4 vezes no HTML e **tem que
ficar VAZIO**. Zero marca de reCAPTCHA, hCaptcha, Turnstile ou DataDome.

**COMANDO EXATO DE DISPARO:**

```
cd /home/user/apply
VINI_TEL="<telefone, do doc privado do Drive>" \
VINI_SAL="EUR 45000" \
sh hb_run.sh apply_breezy.js \
   "https://playdead.breezy.hr/p/3be060a4fcf301-zbrush-modeler/apply" \
   playdead-zbrush --submit
```

Sem `--submit` ele para no modo seco. **`VINI_SAL` não tem padrão e o script lança erro se faltar** —
é o conserto de 07/09 da faixa morta de 46 mil. O anúncio **não publica faixa**; Dinamarca é Europa
ocidental e Playdead é casa média, então **EUR 45.000** pela política de 04/09.
**Refaça o dedupe no minuto do clique**, nunca contra esta página.

---

## As outras trinta, se sobrar tempo

Todas já foram abertas e medidas, todas ficam à mão, e o texto de cada uma está no painel. Onde a
coluna diz "à mão, motivo na nota do painel", o obstáculo não é captcha nomeado: abra a entrada no
painel e o motivo está escrito lá.

| Estúdio e vaga | Onde | O que barra | Link |
|---|---|---|---|
| Passion Pictures (candidatura espontanea) | Reino Unido (Londres) | reCAPTCHA v3, que reprova a sessao automatizada pelo IP | https://passion-pictures.com/careers |
| Bandai Namco Mobile (Open Application) | Espanha (Barcelona) | à mão, motivo na nota do painel | https://bandainamcomobile.com/careers/jobs/1199319-open-application |
| Milestone | Itália (Milão) | reCAPTCHA | https://milestone.it/general-application/ |
| Nexus Studios (General Application) | Reino Unido (Londres) | reCAPTCHA v2 de caixa de marcar | https://apply.workable.com/j/4F41AEB27C |
| Ubisoft Montpellier | França (Montpellier, presencial) | DataDome do SmartRecruiters | https://jobs.smartrecruiters.com/Ubisoft2/744000121716487 |
| Palomar Animation (Mediawan Kids & Family) | Itália e França (grupo Mediawan) | reCAPTCHA | https://mediawankidsandfamily.com/jobs |
| Rebel Wolves (Open Application, candidatura espontânea) | Polônia (Varsóvia ou remoto) | **CLOUDFLARE NO UPLOAD, medido em 09/09 com clique real.** O formulário preenche inteiro, com o departamento Art e o consentimento marcados, mas o POST do anexo devolve 403 com `Just a moment...` em três tentativas e a tela diz `Failed to upload the file`. Do seu navegador passa. | https://system.erecruiter.pl/FormTemplates/RecruitmentForm.aspx?WebID=d2fa13d6d9cd47a6aa9010c9e9294d74 |
| PixelAnt Games / Sumo Digital (Future Opportunities, espontânea) | Polônia (Wrocław ou remoto) | à mão, motivo na nota do painel | https://form.erecruiter.pl/form/a66fabf884d24c15beb2ec7854531f0a |
| Game Boost (Open application, Game Artists) | Suecia (Estocolmo; hibrido e remoto) | à mão, motivo na nota do painel | https://gameboost.teamtailor.com/jobs/2814432-open-application-game-artists-game-boost-home-of-game-gigs-sweden-hybrid-remote |
| SQRT3 (Square Root of Tree) | Polônia (Varsóvia) | reCAPTCHA | https://sqrt3.games/#rekrutacja |
| Stormind Games | Itália (Acireale e Milão) | reCAPTCHA v2 de caixa de marcar | https://stormindgames.bamboohr.com/careers/203 |
| Gamious | Holanda (Haarlem) | reCAPTCHA v3, que reprova a sessao automatizada pelo IP | https://gamious.com/jobs/ |
| eXiin | Bélgica (Bruxelas) | reCAPTCHA v3, que reprova a sessao automatizada pelo IP | https://exiin.com/jobs-internships/ |
| Funday Games (Senior Art Director) | Dinamarca | reCAPTCHA v2 de caixa de marcar | https://funday.bamboohr.com/careers/279 |
| Metropolis VFX (Expression of Interest) | Espanha (Madri, híbrida) | à mão, motivo na nota do painel | https://ilpvfx.teamtailor.com/jobs/6941873-metropolis-expression-of-interest |
| Random Studio (3D Artist, Amsterdã) | Holanda (Amsterdã) e França (Paris) | reCAPTCHA v2 de caixa de marcar | https://randomstudio.bamboohr.com/careers |
| Amuse Animation (Concept Designer) | Espanha (Las Palmas de Gran Canária) | reCAPTCHA v2 de caixa de marcar | https://amuseanimation.bamboohr.com/careers/180 |
| DreamWorks e NBCU (Associate Art Director, Montréal) | Canadá (Montréal, presencial) | à mão, motivo na nota do painel | https://jobs.smartrecruiters.com/NBCUniversal3/744000133659271-associate-art-director-characters-concepts-lighting-vfx-world-directeur-rice-artistique-associe-e-personnages-monde-concepts-eclairage-et-vfx- |
| Gameloft Montréal (Lead 3D Character Artist, Disney Dreamlight Valley) | Canadá (Montréal) | à mão, motivo na nota do painel | https://www.artstation.com/jobs/Rdml |
| Offworld Industries (Squad) | Canadá (New Westminster, BC, presencial) | reCAPTCHA | https://owi.bamboohr.com/careers/199 |
| Streamline Studios | Remoto (global) | reCAPTCHA | https://streamlinestudios.bamboohr.com/careers/84 |
| Electronic Arts Vancouver (EA Sports FC) | Canadá (Vancouver) | à mão, motivo na nota do painel | https://jobs.ea.com/en_US/careers/JobDetail/Senior-Character-Artist/215788 |
| Mainframe Studios | Canadá | à mão, motivo na nota do painel | https://www.mainframe.ca/careers/ |
| Stairway Games | Remoto | à mão, motivo na nota do painel | https://stairwaygames.com/careers |
| VOID Interactive | Irlanda/Remoto (UE) | à mão, motivo na nota do painel | https://voidinteractive.net/careers/ |
| Fluffy Dog Studio | Remoto (estúdio 100% remoto; base Vancouver) | à mão, motivo na nota do painel | https://www.artstation.com/jobs/c/fluffy-dog-studio |
| Wicked Fox Games | EUA (remoto) | à mão, motivo na nota do painel | https://wickedfoxgames.com/contact/ |
| Pingle Studio | Ucrânia | à mão, motivo na nota do painel | https://pinglestudio.com/join-the-team/3d-hard-surface-artist/ |
| Outpost VFX | Reino Unido | à mão, motivo na nota do painel | https://careers.outpost-vfx.com/en/careers/ |
| Deep Worlds (Job application, opção Other) | Suíça (Genebra ou remoto) | reCAPTCHA | https://tally.so/r/RGRv7d |
| Liquid Swords (Open Application, candidatura espontânea) | Suécia (Estocolmo) | **FASTLY 421 NO DOMÍNIO PRÓPRIO, medido no navegador em 11/09.** O anúncio 1851070 existe no `jobs.json`, mas o link do Teamtailor manda 301 para `careers.liquidswords.com` e a borda do Fastly devolve 421 com *"Requested host does not match any Subject Alternative Names (SANs) on TLS certificate"* — página com zero campo. Testei a hipótese de coalescência HTTP/2 (`--disable-http2`, indo direto ao domínio próprio, sem passar pelo redirecionamento) e deu o mesmo 421, então é a borda deles somada a este proxy, não o nosso navegador. Mesmo padrão do `careers.ilpvfx.com`. Do seu navegador deve passar. **Vale o clique: é a melhor casa das 15 rotas desta rodada** — AAA sueco de IP própria, produção interna de personagem, e o próprio anúncio convida a registrar interesse. | https://liquidswords.teamtailor.com/jobs/1851070-open-application/applications/new |
| thatgamecompany (General - Art) | EUA (Santa Monica) / remoto | **reCAPTCHA v2 invisível do Ashby**, chave de plataforma `6LeFb_…r49Y`, a mesma que já reprovou o IP daqui na Stellar em 07/09. Ressalva antes de clicar: a casa **já recebeu candidatura em 31/08** e a requisição irmã tem veto escrito de visto — leia antes de gastar. | https://jobs.ashbyhq.com/thatgamecompany/ea5b0730-cb40-4e87-a0dd-f9d43f96ec3f/application |
| Redly Games (General Interest - Open Application) | Finlândia / `Global – Remote (EU & Canada preferred)` | reCAPTCHA v2 invisível do Ashby. Casa nova, aventura 3D em UE5, porta de arte aberta. | https://jobs.ashbyhq.com/redlygames/3c2a1d1e-5e80-4b4e-895d-f43d0efe4d3b/application |
| Stellar Entertainment (Talent Pool) | Reino Unido (Guildford, híbrido) + Holanda (Utrecht) | reCAPTCHA v2 invisível do Ashby — e aqui não é palpite: este IP **já foi reprovado** por ele em 07/09. | https://jobs.ashbyhq.com/stellarentertainment/43711cca-1ec5-40d3-98d7-eeb2740e604d/application |
| Jam City (General Resume Submissions) | EUA (Los Angeles, São Francisco, San Diego) / remoto | **hCaptcha ativo + desafio Cloudflare** do Lever. Departamento de arte 3D provado no quadro. | https://jobs.lever.co/jamcity/136adc53-aeb8-4598-8a62-de5dc6b0150a/apply |
| VRChat (General Opportunity) | Remoto (`Anywhere`) | hCaptcha ativo + Cloudflare. **O produto da casa é avatar**, então o encaixe de personagem é direto. | https://jobs.lever.co/vrchat/0a24ad44-1335-47ac-9081-b5f9b054f105/apply |
| Kolibri Games (Open/Speculative Application) | Alemanha (Berlim) | hCaptcha ativo + Cloudflare. Balcão permanente, aberto desde 2020. | https://jobs.lever.co/kolibrigames/d2ff05ad-e219-4dd9-985a-825d72bcf671/apply |
| Nine Dots Studio (candidatura espontânea, Outward e Outward 2) | Canadá (Québec) | **NÃO É CAPTCHA, é hidratação.** O formulário próprio está completo e **zero captcha medido**; preenchi tudo daqui — nome, email, telefone, `jobType = Art`, portfólio, CV anexado (45.459 B na tela) e carta de 1.634 caracteres, honeypot `website` vazio. O que não acontece é o React **amarrar o handler do botão "JOIN YOUR CV"**: o bundle Next.js não hidrata por esta rede (chunks com `ERR_ABORTED`), e sem isso o clique cai no comportamento padrão do navegador, que serializa tudo na query string e **não envia nada**. Do seu navegador hidrata normal. É a porta mais barata da fila: sem ATS, sem porteiro, com categoria **Art** separada de Animation, e a casa é inédita para a campanha. | https://www.ninedotsstudio.com/careers |
| Blowfish Studios (candidatura espontânea, Sydney) | Austrália (Sydney) | **NÃO É CAPTCHA** (zero medido). Formulário Wix preenchido inteiro daqui — First name, Last name, Preferred name, Email, "A bit about you" com 1.600 caracteres, **CV e portfólio anexados com sucesso** (`POST /_api/form-submission-service/v4/submissions/media-upload-url` → 200 nos dois, e os dois nomes aparecem na tela). O **Submit não dispara**: cliquei no botão certo, o de dentro do próprio formulário, e **nenhum pedido sai**; sem campo inválido, sem obrigatório vazio, sem texto de erro. É o mesmo padrão da Nine Dots: o caminho de envio do SPA não completa por esta rede, embora o upload de arquivo complete. Do seu navegador vai. | https://www.blowfishstudios.com/careers |
| Peekaboo Animation (candidatura espontânea pelo formulário de contato) | Espanha (Barcelona) | **reCAPTCHA v3 reprovou a sessão, e desta vez com a palavra do servidor.** O formulário é Contact Form 7, servido no HTML, e foi preenchido inteiro daqui: nome, email, mensagem de 1.479 caracteres, CV anexado (45.459 B), consentimento `acceptance-408` marcado, honeypot `coupon_question` **desmarcado** e o token `_wpcf7_recaptcha_response` **presente** (gerado pelo próprio navegador, nada foi burlado). O `POST` para `/wp-json/contact-form-7/v1/contact-forms/9/feedback` voltou **200** com `{"status":"spam"}` — é a pontuação do v3 reprovando o IP de datacenter, não um erro nosso. **Nada foi entregue a eles**, então não há risco de duplicata. Do seu navegador passa. O convite é escrito pela própria casa no formulário: *"IF YOU WANT TO WORK WiTH US, PLEASE ATTACH YOUR PORTFOLIO"*. Se for anexar o PDF do portfólio, atenção: o CF7 limita anexo a 1 MB por padrão e o seu PDF tem 2,6 MB — mande o CV e deixe a ArtStation no texto. | https://www.peekabooanimation.com/contact/ |
| **GSC Game World — 3D Character Artist** (S.T.A.L.K.E.R. 2) · requisição `236329` | Praga (RTC), Kyiv ou **remoto dentro da Europa** | **A MELHOR VAGA DA FILA, e é vaga de verdade, não banco de talentos.** Preenchi tudo daqui: nome, email, telefone, carta de 2.158 caracteres no editor rico, CV anexado, pretensão EUR 55.000, e os dois consentimentos de GDPR marcados. O servidor respondeu **422** com a frase dele: *"We could not verify that this application was submitted by a person. Please reload the page and try again."* — é o **reCAPTCHA v3** reprovando o IP de datacenter, a mesma parede da Peekaboo. **Nada foi entregue**, então não há duplicata. Do seu navegador passa. Sem exigência de idioma escrita (a vaga de Concept Artist deles exige ucraniano, a de personagem **não**). | https://gscgameworld.peopleforce.io/careers/v/236329-3d-character-artist/a/new |

---

## ArtStation Jobs — o quadro mais on-target da disciplina, e só o SEU navegador alcança

**Medido em 11/09 às 21h50, e desta vez com navegador de tela de verdade, não só curl.**

O Jhon B tinha fechado em 09/09 dizendo "não é caçável por `curl`": `/jobs` dá **403** com
interstitial do Cloudflare, `/jobs.json` dá 200 mas é a casca da SPA em Angular com zero vaga,
a API v2 dá **500** e o POST dá **412 Invalid CSRF Token**.

Abri com o navegador de tela para ver se a hidratação resolvia. **Não resolve.** A página
carrega e para em:

> *"One more step. Please complete a security check to continue."*

Título da aba: *"Just a moment..."*. **É captcha de DESAFIO do Cloudflare**, e por regra do
briefing desafio não se burla. Zero vaga chegou pela API porque a página nunca passou do muro.

**Por que é o IP e não o navegador:** a sessão sai por IP de datacenter, e o Cloudflare desafia
esse tipo de origem por padrão. **Do seu navegador, em casa, isso passa sem você nem ver.**

### O que isso significa para a campanha

O ArtStation Jobs é, de todos os quadros que a campanha conhece, **o mais alinhado à disciplina
dele**: é o quadro da própria comunidade de arte 3D, onde vaga de personagem aparece com o nome
certo e sem o ruído de marketing e engenharia que enche Workday e SmartRecruiters. E é o único
que nenhuma automação desta campanha consegue ler.

**Portanto ele vale uma visita SUA, à mão, e provavelmente vale mais que uma rodada inteira de
agente.** A conta é simples: agente varre dezenas de milhares de anúncios para achar zero de
personagem, e este quadro é pequeno e quase todo da disciplina.

### O que procurar quando abrir

Termos, na ordem de prioridade do briefing:
`character artist`, `character modeler`, `creature artist`, `3d modeler`, `sculptor`,
`texture artist`, `look development`, `surfacing`, `visual development`, `groom`.

**Descartar pelo CORPO, não pelo título:** `Creature TD` quase sempre é rigging e `Creature FX`
é simulação; os dois estão fora, apesar da palavra creature. Também fora: VFX em tempo real,
design de locação 2D, matte painting, concept e character design 2D.

**Antes de gastar carta:** confira se a vaga já está no `enviados.csv`, e leia o anúncio inteiro
atrás de veto ESCRITO (`authorized to work`, `must be based`, `citizen`, `resident`). Patrocínio
de visto é contexto, não é critério de descarte.

Se achar alguma e me passar o link, eu monto o dossiê e preencho o formulário na hora.

---

## ITEM DE MÃO NOVO — DreamWorks Montreal, **Lead Character Artist** (14/09)

**Esta é, pela leitura do corpo do anúncio, a vaga que mais casa com o portfólio dele em toda a
campanha.** Contagem no texto oficial: `character` 20, `groom` 6, `hair` 4, `fur` 2, `Houdini` 4,
`XGen` 2. O título é literalmente *Lead Character Artist (Body/Crowd, Face, Hair & Wardrobe)*.

- **Requisição:** `744000137526729` · refNumber `REF38910F`
- **Casa:** NBCUniversal / DreamWorks Animation, Montréal, Canadá · **Full time**, presencial
- **Página da vaga:** https://jobs.smartrecruiters.com/NBCUniversal3/744000137526729
- **Publicada:** 13/07 · **Dedupe:** sem candidatura, conferido
- **Régua de veto:** o anúncio diz *"Must be legally authorized to work in Canada"* e *"Must be
  willing to work in our Montreal office a minimum of 4 days a week"*. **Não é veto de patrocínio**:
  ser patrocinado É estar legalmente autorizado, e presença no escritório é restrição de presença,
  não proibição de candidatura. Pelo briefing, isso é contexto.

### Por que ela está na sua mão, e o que EU já testei (cliquei, não supus)

O registro da campanha dizia desde 08/09 que a casa inteira estava travada por DataDome, e por
isso esta vaga passou **seis dias parada**. Isso estava **errado pela metade** e a correção importa:

| O que eu abri | Resultado medido |
|---|---|
| Página da vaga, navegador de verdade | **HTTP 200, livre.** Título certo, zero iframe de captcha, zero bloqueio |
| Formulário `oneclick-ui`, anônimo | **403 + DataDome**, desafio de slider com áudio |
| Formulário `oneclick-ui`, **com a sessão salva** `sr_state.json` | **403 + DataDome** igual. Não é questão de estar logado |
| Rota `external-referrals` (a terceira, tirada do `referralUrl` da API) | **403 + DataDome** |

**Três rotas de candidatura testadas, três barradas no mesmo muro.** Desafio de captcha não se
burla, então aqui para. O que muda em relação ao registro antigo: a casa **não** está fechada, e o
quadro dela continua valendo a varredura de toda rodada. O muro é só do formulário.

**O que fazer, em dois minutos:** abrir a página da vaga acima no seu navegador normal, clicar em
*I'm interested*, resolver o slider uma vez e seguir. O CV e os links são os de sempre.
**Autorização de trabalho no Canadá: responda NÃO**, que é a verdade, e diga que precisa de
patrocínio no primeiro campo de texto livre que aparecer.

As outras duas da mesma casa, se quiser aproveitar a sessão já destravada:
`744000137526669` Lead Material Artist e `744000133659271` Associate Art Director, ambas Montréal.

---

## ~~PORTA NOVA — Dirk Interactive, **3D Character Artist – Unreal Engine 5**~~ — **SAIU EM 19/09: A VAGA FECHOU. NÃO ABRA.**

> **Medido em 19/09 às 00h40 UTC, na fonte do próprio empregador, não em agregador.** O
> `https://dirkinteractive.com/jobs.json` — que é o arquivo que a página de carreiras deles
> carrega — devolve **`"open": false` nas QUATRO vagas** da casa (`3d-character-artist`,
> `3d-generalist`, `concept-artist`, `art-director`). E o Google Form da candidatura responde
> **200 mas com a URL final em `/closedform`**, que é a página de formulário encerrado do Google.
> **Não é a rede nem o login: a requisição foi encerrada.** Texto original mantido abaixo só para
> registro. Se a casa reabrir, o dossiê continua válido.

#### (texto original, mantido só para registro; a vaga ESTÁ FECHADA, veja o aviso acima)

## PORTA NOVA — Dirk Interactive, **3D Character Artist – Unreal Engine 5** (14/09, Jhon caçador)

**É a única porta nova da rodada, e ela é de PERSONAGEM PURO.** Casa inédita em tudo: zero
ocorrência em `enviados.csv`, `processados.csv`, painel, `FILA-DO-VINI.md` **e zero thread no
Gmail** para `dirkinteractive` ou "Dirk Interactive".

- **Casa:** dirk / Dirk Interactive Inc. — Vancouver, British Columbia, Canadá
- **Cargo:** 3D Character Artist – Unreal Engine 5 · **Remoto** · Contrato por comissão
- **Requisição:** id do quadro próprio `3d-character-artist`; **LinkedIn `4464812501`**, publicada
  em **11/09/2026**, `employmentType: CONTRACTOR`, `jobLocation: Vancouver, British Columbia, Canada`
- **Quadro (fonte oficial):** `https://dirkinteractive.com/careers.html`, que carrega
  `https://dirkinteractive.com/jobs.json` — a vaga está com **`"open": true`** lá agora
- **URL DE CANDIDATURA:**
  `https://docs.google.com/forms/d/e/1FAIpQLScgQwRncOu6RSVMCrdkh5DYmuCeUzMxPuyVrJx2qEMzznZhSQ/viewform`
- **Descoberta:** planilha oficial da comunidade (linha de 14/09, Vancouver, Remote), **confirmada
  na fonte do próprio empregador**, nunca no agregador.

### Por que ela é dele, com a frase do anúncio

> *"Strong understanding of anatomy, proportion, clothing, and silhouette."*
> *"High-quality modelling, sculpting, texturing, and material skills."*
> *"Develop character models, clothing, and equipment from approved concepts and references."*
> *"Create topology, UVs, textures, and materials suited to real-time production."*

É o pipeline inteiro de personagem, do sculpt à engine, que é exatamente o ponto forte 12 do
briefing. **Zero ambiente, zero prop, zero level art no corpo da vaga.**

### Régua de veto, termo a termo, no texto INTEIRO baixado da fonte

Rodada sobre o registro completo do `jobs.json` (descrição, responsabilidades, requisitos,
nice-to-have, engajamento e lista de material da candidatura). **Três acertos, os três
classificados à mão:**

| Termo | Frase inteira | Veredito |
|---|---|---|
| `authoriz` | *"share only material you are **authorized** to disclose. Password-protected portfolios are welcome."* | **FALSO POSITIVO.** É NDA de portfólio, não autorização de trabalho |
| `international` | *"**International applicants are welcome**, with availability for occasional discussions during Pacific Time working hours."* | **SINAL POSITIVO**, e é o mais forte que esta campanha já leu num anúncio canadense |
| `Pacific` | mesma frase acima | restrição de **fuso**, não de nacionalidade |

**ZERO ocorrências de:** `sponsor`, `eligib`, `work permit`, `must be based`, `LMIA`,
`days a week`, `citizen`, `resident`, `right to work`, `visa`, e zero exigência de idioma
(`French`, `fluent` e os demais da régua não aparecem). **Nenhum veto escrito.**

Vale o contraste, porque ele mede o quanto isto é raro: a mesma rodada leu a **Rebellion**
(Senior Character Artist, Oxford/Warwick) e ela traz, por escrito, *"This role is only open to
applicants who have the permanent right to work in the UK. We are unable to provide or take over
visa sponsorship, either now or in the future."* — essa é veto e foi descartada.

### A porta: Google Forms, sem captcha, **mas exige conta Google**

Medido por `curl`, não suposto. `GET` no `viewform` responde **HTTP 302 para
`accounts.google.com/ServiceLogin?service=wise&...&ltmpl=forms`** e, seguindo, **401** com a casca
de login. **Zero ocorrência de `captcha`, `recaptcha`, `hcaptcha` ou `turnstile`** no que foi
servido.

**Consequência honesta: a LISTA DE CAMPOS ficou `NÃO CONFERIDO`.** O `FB_PUBLIC_LOAD_DATA_`, que é
onde o Google Forms publica os campos, não é servido a quem não está logado, então eu não posso
dizer quais são os campos sem inventar. O que o anúncio diz que a candidatura tem de levar, e isso
é texto deles:

> *"Portfolio. Résumé or a brief overview of professional experience. Relevant character examples,
> including in-engine work and breakdowns where available. Availability, location or time zone, and
> your usual project pricing or rate expectations."*

**Para você, em dois minutos:** abra o formulário logado na sua conta Google, que ele monta
direto. Leve ArtStation, CV, exemplos de personagem com breakdown, e no campo de
disponibilidade/localização diga o fuso e que há sobreposição confortável com o Pacífico — é
literalmente o que eles pedem. **Não há caixa de autorização de trabalho no anúncio**, e se
aparecer uma no formulário, a resposta é a verdade de sempre.

### Pretensão, e aqui a regra 1 do briefing não se aplica

**A vaga de personagem NÃO publica faixa.** Quem publica é a irmã de Art Director, **CAD 45–65 por
hora**, e usar a faixa de outra requisição seria inventar. Como é contrato por comissão em casa
pequena, a referência da política é o degrau de casa pequena no Canadá; a frase de abertura
continua sendo *"Open to aligning with your band for the role"*.

### As ressalvas, ditas de frente porque elas pesam

1. **É contrato de 3 a 4 meses, remoto, por comissão** — e a ordem do `BRIEF-JHON` é
   **realocação primeiro, remoto segundo, efetiva antes de contrato**. Esta porta está no degrau
   de baixo dessa escada. Ela entra porque é de personagem e porque está aberta, não porque é boa
   colocação.
2. **A casa é muito nova e quase não tem lastro público.** O site é GitHub Pages e as páginas
   `About` e `Games` do próprio menu respondem **404**; não há jogo publicado, nem equipe
   nomeada. O projeto é *"unannounced PC game"* sob NDA. Não é motivo para descartar, é motivo
   para você saber o que está pegando.
3. **Exige NDA e contrato de prestador antes do material confidencial.**
4. A mesma casa tem **3D Generalist** (props, set dressing, montagem de cena) e **Concept Artist**
   (2D) abertas. **As duas estão fora da disciplina** e não entram nesta fila.

---

## Streamline Studios — **3D Character Artist** (freelance, remoto) — entrada de PRIORIDADE BAIXA, 14/09

Entra na fila **como baixa e com as ressalvas na frente**, não como achado do dia. A disciplina
é certa e a régua passou limpa, mas o formato e o país não são o que ele procura.

- **Requisição:** `106` no BambooHR · `https://streamlinestudios.bamboohr.com/careers/106`
- **Casa:** Streamline Media Group, 25 anos, co-desenvolvimento para Sony, Microsoft e editoras AAA
- **Régua de veto, termo a termo:** `authoriz`, `sponsor`, `work permit`, `must be based`, `LMIA`,
  `citizen`, `right to work`, `resident`, `eligib` — **ZERO acerto**. Nenhum veto escrito.
- **Disciplina:** hands-on de verdade. *"specialization in Character production workflow"*, com
  ZBrush, Maya e Substance citados. Não é gestão.
- **Dedupe:** casa inédita no registro.

### As três ressalvas, e elas é que decidem

1. **`atsLocation` diz `Kuala Lumpur, Malásia`**, e a casa é Kuala Lumpur e Tóquio. **A Malásia não
   está no escopo** (na Ásia só Coreia do Sul e Singapura) e o Japão está fora por ordem dele.
2. **É freelance por ordem de serviço:** *"This is a fully remote, project-based engagement: scope,
   deliverables, timelines, and rates are defined per work order."* Pelo briefing, freelance e
   temporário entram **no máximo como baixa**.
3. **Não é rota de visto.** Remoto por contrato não patrocina nada e não realoca ninguém, que é o
   objetivo da campanha.

**O que salva a entrada:** é **100% remota**, então o escopo de país não é violado por realocação,
e a casa entrega para Sony e Microsoft. Fica registrada para ele decidir, não descartada por mim.

### A irmã dela NÃO entra

A **Lead Character Artist** (`84`) da mesma casa também passa a régua, mas o corpo mostra que é
**gestão e não arte**: *"responsible for managing and coordinating art-related project plans"*,
*"oversee the assigning and tracking of art assets"*, *"Create briefs and documentation"*,
*"Prepare and plan content submission packages for clients"*. Cargo de produção com nome de arte.

## Item novo, 18/09 22h15 UTC (Jhon A) — BLIND SQUIRREL GAMES, *General Application*: formulário limpo, sem captcha de desafio, e o envio não sai deste IP

**Por que vem para a sua mão e não para a automação:** o formulário está **preenchido e medido**
campo por campo, **não há captcha de desafio nenhum** para resolver, e ainda assim o clique em
*Apply* não gera **um único POST** para `ats.rippling.com`. Em três tentativas, o que aparece na
rede é `challenges.cloudflare.com/cdn-cgi/challenge-platform` e
`ats.rippling.com/cdn-cgi/challenge-platform` respondendo 200 com corpo `{"i":60}`: é **Turnstile
invisível**, o porteiro da regra 17 do briefing, que pontua a sessão no último clique. Do seu
navegador, com a sua sessão, ele tende a passar.

- **Endereço do formulário:** `https://ats.rippling.com/blind-squirrel-games/jobs/8f652c14-6e37-45a4-b242-67e942d24ef1/apply?step=application`
- **Requisição:** uuid `8f652c14-6e37-45a4-b242-67e942d24ef1`. **Cuidado:** o quadro lista *três*
  "General Application" (Austin TX, Irvine CA, Auckland NZ) e as três são **a mesma requisição**,
  só muda o `workLocation`. Não são três vagas.
- **O que a casa é, sem maquiagem:** estúdio independente de **co-desenvolvimento**, campi nos EUA,
  Colômbia e Nova Zelândia. A candidatura espontânea é do departamento *Development* e **não é vaga
  de personagem** — o anúncio não tem a palavra *character*. A casa já recebeu carta fria em 02/09 e
  follow-up em 07/09, sem resposta.

**As respostas, exatamente como foram preenchidas e conferidas na leitura de volta:**

| campo | resposta |
|---|---|
| CV | `Vini_Cavalcanti_CV.pdf` (o Rippling parseia o CV e reescreve campo, confira depois de anexar) |
| Cover letter | `Vini_Cavalcanti_Cover_Letter.pdf` |
| First / Last name | Vini · Cavalcanti |
| Email | contact@vinicavalcanti.art |
| Current company | E-Line Media |
| Phone number | seletor **+55 BR** separado, e no campo do número **só os dígitos**, sem código e sem espaço (receita do documento privado do Drive) |
| Location | campo obrigatório, veio autopreenchido pela geolocalização |
| LinkedIn / Website | linkedin.com/in/vinicavalcnti · artstation.com/viniciuscavalcanti |
| Preferred Start Date | 02 / 11 / 2026 |
| Desired annual salary in USD | **USD 85,000 base, open to aligning with your band for the role.** (POLÍTICA item 3: casa independente, sem faixa publicada) |
| Do you require sponsorship now or in the future? | **Yes**, com a verdade: não é autorizado a trabalhar nos EUA nem na Nova Zelândia, cinco anos de remoto com time americano, e o caso de visto pelas credenciais acadêmicas |
| Comfortable with in person work at the studio? | *I am open to full onsite campuses.* |
| Open to relocating for a hybrid schedule? | *Yes* |
| Willing to work full-time onsite? | *Strong Yes* |
| Home Address | está no documento privado do Drive, **não neste repositório** |
| Did anyone refer you? | *No referral. I am applying directly through your careers board.* |
| Consentimento de SMS | *No – I do not consent to receiving text messages* |

**Não gaste tentativa em variação de clique.** As três já foram pagas nesta rodada: rótulo do botão
corrigido, clique sintético com `force`, e clique de mouse nas coordenadas da caixa
(`{x:1186,y:2548,w:74,h:40}`). Nenhuma produziu POST. O que falta não é código, é sessão.

---

## Item novo, 19/09 01h50 UTC (Jhon A) — **FOLKS VFX / Pitch Black**, *Asset Generalist Senior Artist*, **Toronto (Ontário), remota**: o anúncio cita *hero characters* e o porteiro é DataDome

**Endereço para clicar (use o de TORONTO, não o de Montreal):**
`https://jobs.smartrecruiters.com/PitchBlackCreative/7000000000004158-asset-generalist-senior-artist-freelance-`

**Por que vem para a sua mão:** o `oneclick-ui` do SmartRecruiters responde **HTTP 403** a este IP e o
frame principal fica com **0 campos e 0 caracteres em 10 tentativas de 4 s**. O que carrega é um iframe
de `geo.captcha-delivery.com/captcha/` com 16 campos e o texto literal *"Verification Required … Slide
right to secure your access … We detected unusual activity from your device or network … Automated (bot)
activity on your network (IP 160.79.106.129)"* (`interstitial_rules 5,37,42,43,44,45`, ID
`37f83562-2b03-c4e2-f500-00369f4d2b46`). É **DataDome com desafio de slider mais verificação visual/áudio**,
que está na lista de captcha que não se burla — e é o mesmo porteiro já medido três vezes nesta família
(Ubisoft, Outpost, NBCU). **Do seu navegador, com a sua sessão, ele tende a não aparecer.**

**DUAS CORREÇÕES ao que o Job Board 2.0 anotou, e as duas mudam a decisão:**

1. **A nota "Must be based in Quebec" NÃO está no anúncio.** A régua de veto rodou no corpo inteiro
   (6.424 caracteres de texto limpo) e devolveu **zero acerto dos 43 termos**. A única frase de geografia
   é **permissiva**: *"Remote candidates within Montreal or Vancouver may also be considered"* na versão
   de Toronto, e *"Remote candidates within Toronto or Vancouver may also be considered"* na de Montreal.
   Não existe veto escrito de residência; a nota é do curador do quadro, não da casa.
2. **São TRÊS anúncios da MESMA requisição, e o que amarra é o `refNumber` REF19P**, idêntico nos três:
   `7000000000004182` (Montreal, francês, 17/09), `7000000000004158` (**Toronto ON, inglês, 17/09**) e
   `7000000000004252` (Montreal, inglês, 18/09). **Clique em UM só.** É a armadilha de 19/09 da 31st
   Union outra vez, agora com o mesmo ATS servindo o mesmo requisito em três anúncios de cidade e idioma
   diferentes. O de Toronto é o escolhido porque Ontário é Canadá anglófono, que o `BRIEF-JHON` põe na
   frente do Quebec.

**Por que ela vale o seu minuto:** é a única linha da rodada cujo corpo **cita personagem por escrito** —
*"Execute advanced asset work including **hero characters** and complex assets"* e *"Lead asset development
from modelling through final lookdev"* — com Maya, ZBrush, Substance Painter, Mari, Katana e Houdini, que
é a pilha dele inteira. Remota (`remote: true`), Mid-Senior, publicada 17/09 15h46 UTC.

**Ressalvas honestas, para você decidir com o quadro todo na mão:** o título diz *Freelance* mas o campo
`typeOfEmployment` da API diz **Full-time / permanent** — os dois se contradizem e só a casa desempata; o
nível é **Mid-Senior**, um degrau abaixo do dele; e o anúncio da Folks é **generalista de assets**, não
personagem puro. A casa é conhecida da campanha: o SuccessFactors do grupo Pitch Black devolvia *No jobs
found* desde 08/09, e a Rising Sun (mesmo grupo) recebeu a *Senior Modelling Artist* em 16/09.

**As respostas para preencher (nada foi enviado, o formulário nunca abriu):**

| campo | resposta |
|---|---|
| Nome / Email | Vini · Cavalcanti · contact@vinicavalcanti.art |
| Telefone | seletor **+55 BR** separado e só os dígitos no campo (receita do documento privado do Drive) |
| Endereço residencial | está no documento privado do Drive, **não neste repositório** |
| CV / Portfólio | `Vini_Cavalcanti_CV.pdf` · `artstation.com/viniciuscavalcanti` · `linkedin.com/in/vinicavalcnti` |
| Autorização de trabalho no Canadá | **Não** — não é cidadão nem residente permanente, **precisa de patrocínio** |
| Disposto a realocar | **Sim.** *"I am ready to move to Toronto for the role."* |
| Pretensão (sem faixa publicada, casa média) | **CAD 95.000**, com *"Open to aligning with your band for the role."* |
| Disponibilidade | 1 de novembro de 2026 |
| Onde nos achou | Careers board / site |

