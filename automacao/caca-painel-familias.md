# Caça no painel pelas cinco famílias que passam

**Rodada:** madrugada de 09/09/2026. **Método:** só `curl`, nenhum navegador aberto.
**Famílias procuradas (as PROVADAS):** Greenhouse, Teamtailor, Jobvite, Breezy, Workday.

---

## O NÚMERO, antes de tudo

| Etapa | Quantidade |
|---|---|
| Entradas no `PORTAIS` | 762 |
| Entradas abertas (`done` ≠ true) | 485 |
| Dessas, registradas pelo **site próprio do estúdio** (não por ATS) | 333 |
| Com URL de estúdio de verdade, sondáveis (tirando linhas de levantamento que apontam pra github/gamedevmap/sitemap/notion) | **317 — este é o universo que eu examinei** |
| Páginas que responderam com conteúdo | 300 de 317 |
| Sondagens de slug disparadas (882 slugs × Greenhouse + Breezy + Teamtailor + Jobvite) | 3.528 |
| Segunda varredura, raiz do domínio (`/careers`, `/jobs`) | 547 |
| **Quadros vivos revelados numa família que passa** | **31 quadros, 27 casas** |
| **Quadros com pelo menos uma vaga da disciplina** | **9** |
| Sobreviveram ao escopo geográfico | 7 |
| Sobreviveram à régua de dezessete termos | 5 |
| **Sobreviveram ao dedupe por ID** | **4 pra clicar + 3 com ressalva escrita** |

A leitura honesta da rodada está no fim. O resumo dela: **a hipótese rendeu pouco**. A esmagadora maioria das 317 casas de site próprio não tem quadro escondido em família que passa — elas simplesmente não têm quadro nenhum, ou têm um formulário de WordPress. O que rendeu foi outra coisa: **três requisições vivas, limpas e nunca enviadas que estavam paradas atrás de uma decisão de ritmo de 07/09 que venceu**.

---

# FILA PRONTA PARA CLICAR

Cada linha foi conferida hoje, uma por uma: quadro vivo por HTTP 200, texto integral lido, régua de dezessete termos rodada frase a frase, e dedupe pelo **ID da requisição** nos três arquivos.

---

### 1. beffio — Lead 3D Artist / Environment / World Building / Unity3D
**Família:** Teamtailor (provada) · **Local:** Poznań, Polônia — **Fully Remote** · **Permanente**

**CLIQUE:** https://careers.beffio.com/jobs/6653367-lead-3d-artist-environment-world-building-unity3d-remote-permanent/applications/new
(o link do anúncio é o mesmo sem `/applications/new`)

- **ID da requisição: 6653367.**
- **DEDUPE FEITO E LIMPO:** `grep 6653367` → `docs/index.html` **0**, `enviados.csv` **0**, `automacao/processados.csv` **0**. Também procurei pelo título (`world building`): zero nos três. **Está limpo.**
- **Por que ela é a melhor da fila:** a beffio já tem TRÊS candidaturas confirmadas da campanha (Lead 3D Character Artist 6217989, Senior Character Artist Unity3D 7242656, Senior Character Concept Artist 6984394 — as três `done=true` no painel). O que ninguém viu é que existe uma **quarta requisição no mesmo quadro** que nunca foi tocada. A casa responde rápido ("We usually respond within a day") e já conhece o nome dele.
- **Disciplina, texto do anúncio:** "Deliver exceptional 3D content, from environments, world building and props to lighting and composition"; "Create high-quality 3D assets, including environments, props, and lighting setups"; "**Work across both stylized and realistic art directions**"; "Establish efficient workflows for **modeling, texturing**, and scene assembly"; "Prior experience mentoring or managing a small team of artists". É liderança de arte 3D + ambiente + props + texturização, e pede estilizado com todas as letras.
- **Régua de dezessete termos:** rodei os 17 no texto integral. **NENHUM dos dezessete aparece.** Não há `authoriz`, `sponsor`, `eligib`, `based in`, `relocat`, `resident`, `days a week` — nada. O único requisito de idioma é "**Fluent English**", que ele tem. **Veto: zero.**
- **Ressalva de encaixe, honesta:** pede "At least 1–2 shipped AA or AAA games as a 3D Artist or Lead". O crédito dele é série de animação e jogos; se ele não tiver título AA/AAA shipado, esse é o ponto fraco declarado. Não é veto escrito, é requisito de currículo.

---

### 2. Bluehole Studio (KRAFTON) — 3D Environment Artists (Lead / Senior), Project V
**Família:** Greenhouse (provada) · **Local:** Pangyo, Coreia do Sul — presencial · **Coreia do Sul está no recorte**

**CLIQUE:** https://job-boards.greenhouse.io/bluehole/jobs/8517791002

- **ID da requisição: 8517791002** (internal_job_id 6395160002).
- **DEDUPE FEITO E LIMPO quanto a ENVIO:** `grep 8517791002` → `docs/index.html` 1 ocorrência, `processados.csv` 2. **Li as três: nenhuma é recibo de envio.** Todas dizem a mesma coisa — "REQUISICAO LIVRE E NAO ENVIADA POR DECISAO ESCRITA, em 07/09 pela fatia JHONB, e o motivo nao e da vaga, e de ritmo. (…) O QUE SEGURA: a Bluehole JA RECEBEU DUAS CANDIDATURAS HOJE". `enviados.csv` **0**. **Nunca foi enviada.**
- **POR QUE ELA VOLTA PRA FILA:** a trava era a regra de uma mensagem por casa por dia, e ela era de **07/09**. Hoje é **09/09**. A trava venceu há dois dias e ninguém reabriu a linha. É exatamente o caso de "impedimento operacional que já foi resolvido por outra rodada sem a linha ser fechada" — só que aqui o que resolveu foi o calendário.
- **Quadro vivo hoje:** conferi agora, API do Greenhouse do board `bluehole` devolve 16 vagas e esta é uma delas. HTTP 200 na URL de cima.
- **Régua de dezessete termos:** rodada no texto integral. Único acerto é um bloco de links institucionais em coreano (krafton.com/studios, krafton.com/games) que casou por acidente. **Falso positivo. Veto escrito: zero.**
- **Prova de que a porta funciona:** a campanha JÁ enviou e confirmou duas candidaturas neste mesmo quadro em 07/09 (3D Character Artists 8517790002 e Lead Character Artist TERA2 8520212002), as duas com `/confirmation` e email de `career@bluehole.com`.

---

### 3. Loonshot Games (KRAFTON) — 3D Environment Modeler, Project Camp (5년 이상)
**Família:** Greenhouse (provada) · **Local:** Seul, Coreia do Sul · **no recorte**

**CLIQUE:** https://job-boards.greenhouse.io/loonshotgames/jobs/8651145002

- **ID da requisição: 8651145002** (internal_job_id 6455018002).
- **DEDUPE FEITO E LIMPO quanto a ENVIO:** `docs/index.html` 1, `processados.csv` 2, `enviados.csv` **0**. Li as ocorrências: a do painel diz "REQUISICAO LIVRE E NAO ENVIADA POR DECISAO ESCRITA, em 07/09 pela fatia JHONB, mesmo motivo da Bluehole acima". As de `processados.csv` são o recibo da vaga **IRMÃ** (3D Character Artist 8725151002, essa sim enviada) citando esta de passagem. **Esta nunca foi enviada.**
- **Mesma história da Bluehole:** trava de ritmo de 07/09, vencida.
- **Régua de dezessete termos:** único acerto é "Those eligible for an affirmative action…", que é a cláusula legal coreana de ação afirmativa para veteranos e pessoas com deficiência. **Falso positivo, é a favor e não contra.** Veto escrito: zero.
- **Título é modelagem com todas as letras:** *3D Environment Modeler*. Centro do portfólio dele.

---

### 4. Loonshot Games (KRAFTON) — 3D Environment Artist, Project AA (3년 이상)
**Família:** Greenhouse (provada) · **Local:** Seul, Coreia do Sul · **no recorte**

**CLIQUE:** https://job-boards.greenhouse.io/loonshotgames/jobs/8085897002

- **ID da requisição: 8085897002** (internal_job_id 6202395002).
- **DEDUPE FEITO E LIMPO:** `docs/index.html` 1 ocorrência, `enviados.csv` **0**, `processados.csv` 0 por ID. A única ocorrência do painel é **dentro da nota de outra vaga** e diz literalmente: "Sobra livre no mesmo quadro a 3D Environment Artist - Project AA (**8085897002**), segurada agora pela mesma regra de uma mensagem por casa por dia." **Não tem linha própria e não tem recibo. Nunca foi enviada.**
- **Régua de dezessete termos:** mesmo texto-padrão da KRAFTON, mesmo falso positivo de ação afirmativa. **Veto escrito: zero.**
- **AVISO DE RITMO, decida você:** os itens 3 e 4 são o **mesmo quadro**. Se a regra de uma mensagem por casa por dia continua valendo, mande **só um dos dois hoje** — eu mandaria o **3D Environment Modeler (item 3)**, porque "Modeler" é o título mais direto do portfólio dele — e deixe o outro pra amanhã. Os itens 2 e 3/4 também são do mesmo grupo (KRAFTON), mas são **quadros e estúdios diferentes** (bluehole vs loonshotgames), e a campanha já tratou os dois como casas separadas em 07/09.

---

# COM RESSALVA ESCRITA — leia antes de clicar

### 5 e 6. Epic Games — Principal Environment Artist e Senior Environment Artist, Cary NC
**JÁ FORAM REGISTRADAS NO PAINEL POR OUTRA RODADA, ESTA MADRUGADA, ENQUANTO EU TRABALHAVA.**

- Principal Environment Artist — **ID 6121292004**, internal_job_id 5189997004
  Formulário: https://boards.greenhouse.io/embed/job_app?for=epicgames&token=6121292004
- Senior Environment Artist — **ID 6001731004**, internal_job_id 5157239004
  Formulário: https://boards.greenhouse.io/embed/job_app?for=epicgames&token=6001731004

**O que aconteceu, e por que está escrito:** quando rodei o dedupe às 00h05, os dois IDs davam **zero nos três arquivos**. Refiz o dedupe às 00h20 e os dois **apareceram no `docs/index.html`**, com nota datada de "09/09 de madrugada" e texto "VAGA NOVA ACHADA em 09/09 de madrugada, na varredura de 2.934 slugs de Greenhouse". Ou seja: **outra fatia achou as mesmas duas requisições em paralelo comigo, no mesmo horário.** Não são minhas descobertas e não são novas — são as mesmas.

**O que continua valendo:** as duas estão **registradas mas NÃO enviadas** (`enviados.csv` 0, `processados.csv` 0 por ID). Régua de dezessete termos rodada por mim no texto integral das duas: o único acerto é "Epic does not accept any unsolicited resumes (…) from any unauthorized third party" e "We will not pay any fees to any unauthorized third party" — é a **cláusula anti-agência de recrutamento**, **falso positivo clássico**, não é veto de autorização de trabalho. Nenhum dos outros dezesseis termos aparece.

**Ponto de método que vale mais que a vaga:** um censo de 06/09 (`processados.csv` linha 898) viu essas duas requisições e as **descartou por escrito** com a frase "*Principal e Senior Environment Artist da Epic sao ambiente*". Pela régua de disciplina desta campanha, **ambiente CONTA**. Foram três dias de porta aberta perdidos por um recorte de disciplina mais estreito do que o combinado.

**ATENÇÃO OPERACIONAL:** `job-boards.greenhouse.io/epicgames/jobs/<id>` **redireciona para epicgames.com e devolve 403** contra o nosso IP. A porta que responde 200 é o **embed do Greenhouse** que está nos links acima. É por ali que as candidaturas anteriores da Epic saíram ("Greenhouse epicgames token 6020680004"), com código de segurança lido no Gmail.

---

### 7. Swaybox Studios — Unreal Generalist, New Orleans
**Família:** Greenhouse (provada) · **Local:** New Orleans, LA, EUA · presencial

**LINK:** https://job-boards.greenhouse.io/swayboxstudios/jobs/4390537009

- **ID da requisição: 4390537009** (internal_job_id 4226353009).
- **DEDUPE FEITO E DEU LIMPO:** `docs/index.html` **0**, `enviados.csv` **0**, `processados.csv` **0**. Requisição inédita nos três arquivos.
- **Disciplina:** generalista 3D em Unreal — "creation and execution of CG replacements and set extensions", trabalho através do processo de CG. Conta como generalista 3D.
- **Régua de dezessete termos:** nenhum dos dezessete aparece. O acerto de `proficiency` é "technical proficiency in Unreal Engine", **falso positivo**.
- **POR QUE ESTÁ AQUI EMBAIXO E NÃO NA FILA DE CIMA:** a Swaybox é a **terceira** requisição desta casa. A campanha mandou na Senior CG Generalist (Modeler) **4337866009** em 02/09 e **levou RECUSA EXPLÍCITA em 05/09 às 17h15**. Depois disso, a fatia JHONB escreveu uma decisão de não mandar na irmã CG Modeler 4337820009 *justamente por causa da recusa recente*. Esta terceira requisição não foi coberta por aquela decisão, e já se passaram quatro dias — mas é a **mesma casa que acabou de recusar**. **Decisão sua.** Eu registro e não recomendo hoje.

---

# DESCARTADAS COM MOTIVO ESCRITO

Vagas da disciplina que eu achei numa família que passa e que **NÃO devem ser clicadas**. Cada uma com a frase inteira colada.

| Casa / vaga | ID | Motivo |
|---|---|---|
| **2K — Art Director, Core** (LA/Novato) | 7964926003 | **VETO ESCRITO, duplo.** Frase 1: "*Please note that 2K Publishing is unable to provide visa sponsorship or assistance for this position.*" Frase 2: "*All candidates must be legally authorized to work in United States without requiring current or future employer sponsorship.*" Bate em `sponsor`, `authoriz` e `unable to support`. Além disso é direção de arte de **marca e embalagem**, não de arte 3D. |
| **2K — Associate Art Director** (Montréal) | 7714527003 | **VETO ESCRITO DE IDIOMA LOCAL:** "*For candidates located in Quebec: This position requires professional proficiency in both French and English.*" Ele não tem francês profissional. |
| **2K — Lead Character Artist** (Montréal / Novato) | 7888173003 / 7888174003 | **DEDUPE PEGOU:** as duas já foram **enviadas E recusadas**. `processados.csv`: "*formulario preenchido e enviado pela automacao (…) com confirmacao na tela; respondido que nao tem autorizacao para trabalhar na America do N…*". Além disso as duas compartilham o internal_job_id 5834551003 — é uma requisição, não duas. A de Montréal também tem a cláusula de francês. |
| **2K — Senior Character Artist** (Burnaby, BC) | 7835808003 | **DEDUPE PEGOU:** já enviada, "*Greenhouse 2k 7835808003 com codigo de verificacao por email; formulario preenchido e enviado pela automacao (…) com confirmacao na tela*". |
| **Hasbro — Lead Character Artist** (Canadá) | 4318250009 | **DEDUPE PEGOU:** "*E a MESMA requisicao ja enviada em 02/09 pelo Greenhouse da Hasbro (4318250009), aquela sim com CV e carta anexados.*" |
| **Epic — Hard Surface Outsource Lead** (Multiple Locations) | 6142982004 | **MESMA REQUISIÇÃO, OUTRO ANÚNCIO DE LOCAL.** internal_job_id **5199732004**, idêntico ao da versão de Cary **6142980004**, que já foi enviada e confirmada. É a regra 18: segundo local da mesma requisição. |
| **Epic — Modeling Outsource Lead** (Montreal / Porto Alegre) | 6020682004 / 6031088004 | **MESMA REQUISIÇÃO.** internal_job_id **5165648004**, idêntico ao da de Cary 6020680004, já enviada em 03/09. (A de Porto Alegre também é Brasil, fora do recorte.) |
| **HighDive — Generalist Content Tech Director** (Toronto) | 4964067007 | Dedupe limpo (0/0/0), mas cai duas vezes: é **direção técnica**, não arte 3D; e carrega a cláusula de Quebec "*Tous les efforts ont été faits pour éviter d'exiger une langue autre que le français pour ce poste*" — **idioma local**. |
| **Fanatics Collectibles — Art Director** (Londres) | 4397677009 | Dedupe limpo (0/0/0), régua limpa, escopo OK — mas **fora da disciplina**: "*Art Directors at The Topps Company/Fanatics Collectibles are the captains of our **graphic design** team (…) As veteran **graphic designers***", "*Proficient in Adobe Creative Cloud apps*", "*Determine the print technology of each release*". É direção de arte gráfica de carta colecionável e impressão. |
| **KRAFTON — [PUBG Franchise] Art Director** (Seul) | 8470910002 | Dedupe limpo (0/0/0), sem veto escrito. **Não recomendo:** o corpo do anúncio é só em coreano, é direção de arte **de IP e transmídia** ("*IP Visual Core 및 세계관 고도화 / Franchise 확장을 위한 장기적 visual system 구축*"), não produção 3D, e pede 10년 이상. Marginal nos dois eixos. Fica registrada. |
| **Amber Studio — 3D Artist Characters / 3D Artist Generalist** | o5cgufwL / omcgufw2 | **FORA DO ESCOPO GEOGRÁFICO.** Li o quadro Jobvite inteiro (61 vagas): as duas são "*Remote, **Brazil***". As outras duas da disciplina (3D Art Lead oNE2yfwL, 3D Artist orE2yfwp) são **Manila, Filipinas**. Nenhuma vaga 3D no recorte. **Esta linha aberta do painel pode ser fechada.** |
| **Good Job Games — 3D Artist / Senior 3D Artist** | 7491067003 e outras | **FORA DO ESCOPO.** Todas em Sarıyer, **Istambul, Turquia**. Turquia não é UE, nem Reino Unido, nem Irlanda, nem Nórdico. |
| **Sony (siei) — 3D Artist / 3D Environmental Artist, Team ASOBI** | 6138372004 / 6127308004 | **FORA DO ESCOPO.** Tóquio, Japão — excluído por escrito no briefing. |
| **Riot Games — Principal Concept Artist Env/Char** | 8070799 | **FORA DA DISCIPLINA.** Arte conceitual 2D. (A de Guangzhou também é fora do escopo: China.) |
| **teamLFG — Tech Art Lead** | 5659232004 | Dedupe limpo, mas **arte técnica**, não modelagem/textura/look dev. |

---

# QUADROS QUE ACHEI E QUE ESTAVAM SECOS OU MORTOS

Levantamento, não candidatura. Vale escrever porque fecha linha.

- **SuperNatural Studios** — o painel dizia que ela "linka quadro de ATS que morreu". **Confirmado hoje:** `boards.greenhouse.io/supernaturalstudios` responde **404** na API. Quadro desligado de verdade, não é bloqueio.
- **House of How Games** (Boden, Suécia) — achei `houseofhow.teamtailor.com`, e ele responde 200. **É um quadro de DEMONSTRAÇÃO do Teamtailor, abandonado:** as seis vagas são "Intern", "Social Media Manager", "**Game Changer**", "iOS Developer", "Key Account Manager", "Programmer" — é o conteúdo de exemplo que o Teamtailor cria numa conta nova. A vaga real (Senior 3D Artist) está no site próprio deles, que é onde o painel já registrou. **Não perca tempo com o quadro do Teamtailor.**
- **Funcom** (Oslo) — `jobs.funcom.com` é Teamtailor vivo, mas o quadro inteiro hoje são **seis estágios de 2027** (Data Analytics, Concept Art, Design, Production Assistant, Programming, Finance). Zero vaga sênior, zero da disciplina.
- **Triband** (Copenhague) — `careers.triband.net` é Teamtailor vivo com 8 vagas. A única de arte é a **Senior Game Artist 8220733**, que **já é a entrada do painel**. Nada novo.
- **Cast Iron Games** (Wakefield) — `careers.castirongames.com` é Teamtailor vivo com 7 vagas. A única de arte é o **Lead 3D Artist 7154430**, que **já está no painel com veto de residência escrito**. As outras seis são programação.
- **Snowprint Studios** — `career.snowprintstudios.com` é Teamtailor vivo com 2 vagas. A da disciplina é a **Senior 3D Character Artist 8341580**, já no painel **com veto escrito**. Nada novo.
- **Ten Square Games**, **Digic Pictures**, **Revolution Software** — os três têm quadro Teamtailor vivo (`career.tensquaregames.com`, `career.digicpictures.com`, `revolution.teamtailor.com`), e os três voltaram **sem nenhuma vaga listada** na página `/jobs` no momento da leitura.
- **Blur Studio**, **Coatsink**, **31st Union**, **Turtle Rock Studios**, **ManvsMachine**, **PUBG Madison**, **NaturalMotion**, **Firesprite**, **Haven**, **Naughty Dog**, **PDI**, **Bandai Namco**, **Sony Interactive Global**, **Rockstar Games** — todos com quadro **Greenhouse vivo e confirmado por API hoje**, e **zero vaga da disciplina** neles agora. (Blur, Coatsink e Insomniac vieram com o board **literalmente vazio**, 0 vagas.)

---

# TRÊS ENTRADAS DE "IMPEDIMENTO OPERACIONAL" QUE EU FUI CONFERIR

Você mandou procurar o recibo antes de me mandar trabalhar nelas. Fui:

- **Kevuru Games** (Kiev) — "PREENCHIDA SEM PROVA em 07/09". O formulário é **Contact Form 7 dentro de um modal**.
- **Moonmana** (Gdańsk/Tenerife) — "PREENCHIDA SEM PROVA, provável reCAPTCHA". Formulário **WPForms**.
- **L'Atelier Animation** (Montreal) — "ENVIADA DUAS VEZES SEM PROVA".

**As três estão fora do alcance desta caçada** e não entram na fila: nenhuma delas usa uma das cinco famílias que passam. Contact Form 7 com reCAPTCHA está na sua própria lista de parede. **Não achei recibo de resolução para nenhuma das três** — continuam pendentes de verdade, mas por outro caminho que não é este.

---

# A LEITURA HONESTA DA RODADA

**A hipótese não se confirmou, e o número diz por quê.** Das 317 casas de site próprio que eu sondei — 300 responderam, 3.528 sondagens de slug e mais 547 de raiz de domínio — só **31 quadros** apareceram numa família que passa, e a maioria esmagadora deles **já era conhecida do painel** (Epic, Riot, Rockstar, 2K, Hasbro, Sony, os boards da PlayStation). O estúdio médio do `PORTAIS` que está registrado pelo site próprio **não tem quadro escondido**: ele tem um formulário de WordPress, um endereço de email, ou nada.

**As armadilhas de slug que a rodada confirmou.** Das 58 batidas cruas da varredura, **21 eram falso positivo de slug genérico** — `career`, `jobs`, `explore`, `system`, `company`, `onyx`, `recruit`, `artstation` são quadros de **outras empresas** que por acaso ocupam aquele nome no Greenhouse ou no Breezy. `parkerschauffeurs.teamtailor.com` apareceu em três casas de jogos diferentes porque é um asset compartilhado do CDN do Teamtailor. **Bater slug sem confirmar que o quadro é da casa certa produz lixo em escala.**

**Onde a rodada de fato rendeu, e não foi onde eu procurei.** As quatro linhas da fila não vieram de "achei um Greenhouse escondido num site próprio". Três delas vieram de **requisições vivas que já estavam identificadas, com veto limpo, e que ficaram paradas atrás de uma decisão de RITMO tomada em 07/09** — "a casa já recebeu duas candidaturas hoje". Essa trava tinha validade de um dia e ninguém voltou pra reabrir. **Passaram-se dois dias e as portas continuam abertas.** A quarta (beffio) veio de uma casa marcada `done=true` cujo quadro tinha uma **quarta requisição** que nenhuma rodada tinha listado.

**A lição que eu tiraria pro próximo turno:** decisão de "segurar por hoje" precisa nascer com data de vencimento e voltar pra fila sozinha, senão vira decisão de "nunca". E recorte de disciplina precisa ser lido do briefing, não de memória — o descarte de 06/09 que matou as duas vagas de ambiente da Epic com a frase "*são ambiente*" custou três dias de porta aberta numa casa onde a campanha já tem candidatura confirmada.

**O que eu não fiz e você deveria saber:** não abri navegador, não commitei, não enviei nada, não preenchi formulário nenhum e não toquei em `docs/index.html`, `FILA-DO-VINI.md`, `enviados.csv` nem `processados.csv`. Dezessete das 317 páginas não responderam nesta rodada (DNS, TLS ou timeout) e ficaram sem veredito — não são parede, são leitura faltando.
