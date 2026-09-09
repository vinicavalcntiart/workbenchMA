# Caça no painel pelas cinco famílias que passam

**Rodada:** madrugada de 09/09/2026. **Método:** só `curl`, nenhum navegador aberto.
**Famílias procuradas (as PROVADAS):** Greenhouse, Teamtailor, Jobvite, Breezy, Workday.

---

## O NÚMERO, antes de tudo

| Etapa | Quantidade |
|---|---|
| Entradas no `PORTAIS` | 762 |
| Entradas abertas (`done` ≠ true) | 485 |
| Dessas, registradas pelo **site próprio do estúdio**, não por ATS | 333 |
| Com URL de estúdio de verdade, sondáveis (fora as linhas de levantamento que apontam pra github/gamedevmap/sitemap/notion) | **317 — este é o universo que eu examinei** |
| Páginas que responderam com conteúdo | 300 de 317 |
| Sondagens de slug disparadas (882 slugs × Greenhouse + Breezy + Teamtailor + Jobvite) | 3.528 |
| Segunda varredura, raiz do domínio (`/careers`, `/jobs`) | 547 |
| **Quadros vivos revelados numa família que passa** | **31 quadros, 27 casas** |
| **Quadros com pelo menos uma vaga da disciplina** | **9** |
| Sobreviveram ao escopo geográfico | 7 |
| Sobreviveram à régua de dezessete termos | 5 |
| **Sobreviveram ao dedupe por ID** | **2 pra clicar + 2 com ressalva escrita** |

**Duas certas valem mais que cinquenta duvidosas, e é o que tem.** A hipótese da tarefa — "muitas dessas casas hospedam as vagas num ATS que a automação sabe atravessar" — **não se confirmou**, e o número está aí. A leitura honesta está no fim, junto com um erro meu que eu peguei sozinho na última conferência e que quase virou trabalho repetido pra você.

---

# FILA PRONTA PARA CLICAR

Duas linhas. Cada uma com quadro conferido vivo hoje por HTTP 200, texto integral lido, régua de dezessete termos rodada frase a frase, e dedupe pelo **ID da requisição** nos três arquivos — mais uma varredura do ID em **todo o repositório**, que é o que salvou esta lista de estar errada.

---

### 1. beffio — Lead 3D Artist / Environment / World Building / Unity3D
**Família:** Teamtailor (provada) · **Local:** Poznań, Polônia — **Fully Remote** · **Permanente**

**CLIQUE:** https://careers.beffio.com/jobs/6653367-lead-3d-artist-environment-world-building-unity3d-remote-permanent/applications/new
(o anúncio é o mesmo link sem `/applications/new`)

- **ID da requisição: 6653367.**
- **DEDUPE FEITO E DEU LIMPO:** `grep 6653367` → `docs/index.html` **0**, `enviados.csv` **0**, `automacao/processados.csv` **0**. Rodei também pelo título (`world building`): **zero nos três**. E varri o ID no repositório inteiro: só aparece neste arquivo. **Limpo.**
- **Por que é a melhor da fila:** a beffio já tem **três candidaturas confirmadas** da campanha (Lead 3D Character Artist 6217989, Senior Character Artist Unity3D 7242656, Senior Character Concept Artist 6984394 — as três `done=true`). O que nenhuma rodada listou é que existe uma **quarta requisição no mesmo quadro**, aberta e intocada. A casa já conhece o nome dele e o próprio anúncio promete "*We usually respond within a day*".
- **Disciplina, texto do anúncio:** "*Deliver exceptional 3D content, from environments, world building and props to lighting and composition*"; "*Create high-quality 3D assets, including environments, props, and lighting setups*"; "***Work across both stylized and realistic art directions***"; "*Establish efficient workflows for **modeling, texturing**, and scene assembly*"; "*Prior experience mentoring or managing a small team of artists*". É liderança de arte 3D + ambiente + props + texturização, e pede **estilizado com todas as letras** — que é o registro dele.
- **Régua de dezessete termos, texto integral:** **nenhum dos dezessete aparece.** Sem `authoriz`, sem `sponsor`, sem `eligib`, sem `based in`, sem `relocat`, sem `resident`, sem `days a week`. O único requisito de idioma é "*Fluent English*". **Veto: zero.**
- **Ressalva de encaixe, honesta:** pede "*At least 1–2 shipped AA or AAA games as a 3D Artist or Lead*". Se ele não tiver título AA/AAA shipado, esse é o ponto fraco declarado do currículo. **Não é veto escrito**, então não desqualifica — mas você decide como escrever a carta.

---

### 2. Loonshot Games (KRAFTON) — 3D Environment Artist, Project AA (3년 이상)
**Família:** Greenhouse (provada) · **Local:** Seul, Coreia do Sul · **Coreia do Sul está no recorte**

**CLIQUE:** https://job-boards.greenhouse.io/loonshotgames/jobs/8085897002

- **ID da requisição: 8085897002** (internal_job_id 6202395002).
- **DEDUPE FEITO E DEU LIMPO:** `enviados.csv` **0**, `processados.csv` **0 por ID**, `docs/index.html` 1 ocorrência — e eu **li a ocorrência inteira**: ela não é linha própria nem recibo, é uma menção **dentro da nota de outra vaga**, dizendo "*Sobra livre no mesmo quadro a 3D Environment Artist - Project AA (8085897002), segurada agora pela mesma regra de uma mensagem por casa por dia*". Varri o ID no repositório inteiro: aparece em `processados.csv`, `docs/index.html`, `BRIEF-FORCA-TAREFA.md` e nos dois censos, e em **todas as cinco** o texto é "livre", "também livre", "livre e conferida viva". **Nenhuma ocorrência de `/confirmation`, `ENVIADA`, `Thank you for applying` ou `portal-aplicado` colada neste ID. Nunca foi enviada.**
- **POR QUE ELA É DE HOJE, com data:** o recibo da vaga irmã, em `processados.csv` de **08/09**, termina assim: "***FICA PARA AMANHA**, pela mesma regra de uma por casa por dia: a 3D Environment Artist - Project AA, requisicao 8085897002, livre e conferida viva hoje na API do quadro*". **"Amanhã" é hoje.** A trava era de ritmo, tinha hora marcada, e a hora chegou.
- **Quadro vivo agora:** conferido nesta rodada — API do Greenhouse do board `loonshotgames` devolve 23 vagas e esta é uma delas; a URL acima responde **200**.
- **Régua de dezessete termos:** único acerto no texto integral é "*Those eligible for an affirmative action…*", que é a **cláusula legal coreana de ação afirmativa** para veteranos e pessoas com deficiência. **Falso positivo — é a favor, não contra.** **Veto escrito: zero.**
- **Prova de que a porta funciona:** a campanha já enviou e confirmou **duas** candidaturas neste mesmo quadro (3D Character Artist 8725151002 em 07/09 e 3D Environment Modeler 8651145002 em 08/09), as duas com `/confirmation` e "Thank you for applying" na tela.
- **Detalhe de formulário já documentado, use:** no Loonshot as duas perguntas de dados são **AVISO e não consentimento** — a opção certa é **Confirmed / 확인하였습니다**, e **não** "Agree". O Greenhouse manda **código de segurança por email**, então tenha o Gmail aberto.

---

# COM RESSALVA ESCRITA — leia antes de clicar

### 3 e 4. Epic Games — Principal Environment Artist e Senior Environment Artist, Cary NC
**JÁ ESTÃO REGISTRADAS NO PAINEL POR OUTRA RODADA, DESTA MADRUGADA. Não são achado meu.**

- Principal Environment Artist — **ID 6121292004**, internal_job_id 5189997004
  Formulário: https://boards.greenhouse.io/embed/job_app?for=epicgames&token=6121292004
- Senior Environment Artist — **ID 6001731004**, internal_job_id 5157239004
  Formulário: https://boards.greenhouse.io/embed/job_app?for=epicgames&token=6001731004

**O que aconteceu:** quando rodei o dedupe às 00h05, os dois IDs davam **zero nos três arquivos**. Refiz às 00h20 e os dois **já estavam no `docs/index.html`**, com nota datada de "09/09 de madrugada" e a frase "*VAGA NOVA ACHADA em 09/09 de madrugada, na varredura de 2.934 slugs de Greenhouse*". Outra fatia achou as mesmas duas requisições **em paralelo comigo, no mesmo horário**. Registro pra você não contar a mesma vaga duas vezes.

**O que continua valendo:** as duas estão **registradas mas NÃO enviadas** (`enviados.csv` 0, `processados.csv` 0 por ID). Rodei a régua de dezessete termos no texto integral das duas por conta própria: o único acerto é "*Epic does not accept any unsolicited resumes or approaches from any unauthorized third party*" e "*We will not pay any fees to any unauthorized third party*" — é a **cláusula anti-agência de recrutamento**, **falso positivo clássico**, não é veto de autorização de trabalho. Nenhum dos outros dezesseis aparece.

**Ponto de método que vale mais que as duas vagas:** um censo de 06/09 (`processados.csv`, linha 898) **viu essas duas requisições e as descartou por escrito** com a frase "*Principal e Senior Environment Artist da Epic sao ambiente*". Pela régua de disciplina desta campanha, **ambiente CONTA**. Foram **três dias** de porta aberta perdidos por um recorte de disciplina mais estreito do que o combinado, numa casa onde a campanha já tem candidatura confirmada.

**ATENÇÃO OPERACIONAL, medida hoje:** `job-boards.greenhouse.io/epicgames/jobs/<id>` **redireciona pra epicgames.com e devolve 403** contra o nosso IP. A porta que responde **200** é o **embed do Greenhouse**, que são os dois links acima. É por ali que as candidaturas anteriores da Epic saíram ("Greenhouse epicgames token 6020680004"), com código de segurança lido no Gmail.

---

### Fora da fila, mas registrado: Swaybox Studios — Unreal Generalist, New Orleans
https://job-boards.greenhouse.io/swayboxstudios/jobs/4390537009 — **ID 4390537009** (internal 4226353009).

**Dedupe limpo nos três arquivos (0/0/0)**, requisição inédita, quadro Greenhouse vivo, régua limpa (o acerto de `proficiency` é "*technical proficiency in Unreal Engine*", falso positivo), disciplina OK como generalista 3D. **E mesmo assim eu não recomendo hoje:** é a **terceira** requisição desta casa. A campanha mandou na Senior CG Generalist (Modeler) **4337866009** em 02/09 e **levou recusa explícita em 05/09 às 17h15**; depois disso uma fatia escreveu a decisão de não mandar na irmã CG Modeler 4337820009 *por causa da recusa recente*. Esta terceira não foi coberta por aquela decisão e já se passaram quatro dias — mas é a **mesma casa que acabou de recusar**. **Decisão sua**, eu registro e seguro.

---

# DESCARTADAS COM MOTIVO ESCRITO

Vagas da disciplina que apareceram numa família que passa e que **NÃO devem ser clicadas**. Frase inteira colada.

| Casa / vaga | ID | Motivo |
|---|---|---|
| **Bluehole Studio — 3D Environment Artists (Lead/Senior), Project V** | 8517791002 | **DEDUPE PEGOU, e quase passou.** O painel diz "**ENVIADA E CONFIRMADA em 08/09 as 07h32 UTC** pelo maestro (…) PROVA DUPLA: URL .../8517791002/confirmation e o texto coreano na tela, (주)블루홀에 지원해주셔서 감사합니다. Codigo de seguranca do Greenhouse (xFU2b7eP) lido no Gmail". **Já foi.** |
| **Loonshot Games — 3D Environment Modeler, Project Camp** | 8651145002 | **DEDUPE PEGOU, e quase passou.** `processados.csv` de 08/09: "**ENVIADA PELO MAESTRO as 07h33 UTC** (…) PROVA DUPLA: URL .../8651145002/confirmation e Thank you for applying na tela". **Já foi.** |
| **2K — Art Director, Core** (LA/Novato) | 7964926003 | **VETO ESCRITO, duplo.** "*Please note that 2K Publishing is **unable to provide visa sponsorship** or assistance for this position.*" e "*All candidates **must be legally authorized to work in United States without requiring** current or future employer **sponsorship**.*" Bate em `sponsor`, `authoriz` e `unable to support`. Além disso é direção de arte de **marca e embalagem**, não de arte 3D. |
| **2K — Associate Art Director** (Montréal) | 7714527003 | **VETO ESCRITO DE IDIOMA LOCAL:** "*For candidates located in Quebec: This position requires **professional proficiency in both French and English**.*" |
| **2K — Lead Character Artist** (Montréal / Novato) | 7888173003 / 7888174003 | **DEDUPE PEGOU:** já **enviadas E recusadas** — "*formulario preenchido e enviado pela automacao (…) com confirmacao na tela; respondido que nao tem autorizacao para trabalhar na America do N…*". As duas ainda compartilham o **internal_job_id 5834551003**: é uma requisição, não duas. A de Montréal tem a cláusula de francês por cima. |
| **2K — Senior Character Artist** (Burnaby, BC) | 7835808003 | **DEDUPE PEGOU:** já enviada — "*Greenhouse 2k 7835808003 com codigo de verificacao por email; formulario preenchido e enviado (…) com confirmacao na tela*". |
| **Hasbro — Lead Character Artist** (Canadá) | 4318250009 | **DEDUPE PEGOU:** "*E a MESMA requisicao ja enviada em 02/09 pelo Greenhouse da Hasbro (4318250009), aquela sim com CV e carta anexados.*" |
| **Epic — Hard Surface Outsource Lead** (Multiple Locations) | 6142982004 | **MESMA REQUISIÇÃO, OUTRO ANÚNCIO DE LOCAL.** internal_job_id **5199732004**, idêntico ao da de Cary **6142980004**, que já foi enviada e confirmada. Regra 18. |
| **Epic — Modeling Outsource Lead** (Montreal / Porto Alegre) | 6020682004 / 6031088004 | **MESMA REQUISIÇÃO.** internal_job_id **5165648004**, idêntico ao da de Cary 6020680004, já enviada em 03/09. A de Porto Alegre ainda é Brasil, fora do recorte. |
| **HighDive — Generalist Content Tech Director** (Toronto) | 4964067007 | Dedupe limpo (0/0/0), mas cai duas vezes: é **direção técnica**, não arte 3D; e traz a cláusula de Quebec "*Tous les efforts ont été faits pour éviter d'exiger une langue autre que le français pour ce poste*" — **idioma local**. |
| **Fanatics Collectibles — Art Director** (Londres) | 4397677009 | Dedupe limpo, régua limpa, escopo OK — **fora da disciplina**: "*Art Directors (…) are the captains of our **graphic design** team*", "*As veteran **graphic designers***", "*Proficient in Adobe Creative Cloud apps*", "*Determine the print technology of each release*". Direção de arte gráfica de carta colecionável e impressão. |
| **KRAFTON — [PUBG Franchise] Art Director** (Seul) | 8470910002 | Dedupe limpo (0/0/0), sem veto escrito, mas **não recomendo**: corpo do anúncio só em coreano, é direção de arte **de IP e transmídia** ("*IP Visual Core 및 세계관 고도화 / Franchise 확장을 위한 장기적 visual system 구축*"), não produção 3D, e pede 10년 이상. Marginal nos dois eixos. Fica registrada. |
| **Amber Studio — 3D Artist Characters / Generalist** | o5cgufwL / omcgufw2 | **FORA DO ESCOPO GEOGRÁFICO.** Li o quadro Jobvite inteiro (61 vagas): as duas são "*Remote, **Brazil***". As outras duas da disciplina (3D Art Lead oNE2yfwL, 3D Artist orE2yfwp) são **Manila, Filipinas**. **Nenhuma vaga 3D no recorte — esta linha aberta do painel pode ser fechada.** |
| **Good Job Games — 3D Artist / Senior 3D Artist** | 7491067003 e outras 3 | **FORA DO ESCOPO.** Sarıyer, **Istambul, Turquia** — não é UE, nem Reino Unido, nem Irlanda, nem Nórdico. |
| **Sony (siei) — 3D Artist / 3D Environmental Artist, Team ASOBI** | 6138372004 / 6127308004 | **FORA DO ESCOPO.** Tóquio, Japão — excluído por escrito no briefing. |
| **Riot Games — Principal Concept Artist Env/Char** | 8070799 | **FORA DA DISCIPLINA:** arte conceitual 2D. A irmã de Guangzhou também é fora do escopo (China). |
| **teamLFG — Tech Art Lead** | 5659232004 | Dedupe limpo, mas **arte técnica**, não modelagem/textura/look dev. |

---

# QUADROS QUE ACHEI E QUE ESTAVAM SECOS OU MORTOS

Levantamento, não candidatura — vale escrever porque **fecha linha** e evita varredura repetida.

- **SuperNatural Studios** — o painel dizia que ela "linka quadro de ATS que morreu". **Confirmado hoje:** `boards.greenhouse.io/supernaturalstudios` responde **404** na API. Quadro desligado de verdade, não é bloqueio do nosso IP.
- **House of How Games** (Boden, Suécia) — achei `houseofhow.teamtailor.com` e ele responde 200, mas **é o quadro de DEMONSTRAÇÃO do Teamtailor, abandonado**: as seis vagas são "Intern", "Social Media Manager", "**Game Changer**", "iOS Developer", "Key Account Manager", "Programmer" — é o conteúdo de exemplo que o Teamtailor semeia numa conta nova. A vaga real (Senior 3D Artist) está no site próprio, que é o que o painel já registrou. **Não gaste rodada nesse quadro.**
- **Funcom** (Oslo) — `jobs.funcom.com` é Teamtailor vivo, mas hoje o quadro inteiro são **seis estágios de 2027** (Data Analytics, Concept Art, Design, Production Assistant, Programming, Finance). Zero sênior, zero da disciplina.
- **Triband** (Copenhague) — `careers.triband.net`, Teamtailor vivo, 8 vagas. A única de arte é a **Senior Game Artist 8220733**, que **já é a entrada do painel**. Nada novo.
- **Cast Iron Games** (Wakefield) — `careers.castirongames.com`, Teamtailor vivo, 7 vagas. A única de arte é o **Lead 3D Artist 7154430**, **já no painel com veto de residência escrito**. As outras seis são programação.
- **Snowprint Studios** — `career.snowprintstudios.com`, Teamtailor vivo, 2 vagas. A da disciplina é a **Senior 3D Character Artist 8341580**, **já no painel com veto escrito**.
- **Ten Square Games**, **Digic Pictures**, **Revolution Software** — os três com quadro Teamtailor vivo (`career.tensquaregames.com`, `career.digicpictures.com`, `revolution.teamtailor.com`) e os três voltaram **sem nenhuma vaga listada** na hora da leitura.
- **Com Greenhouse vivo e confirmado por API hoje, e ZERO da disciplina:** 31st Union, Turtle Rock Studios, ManvsMachine, PUBG Madison, NaturalMotion (`nmcareers`), Firesprite, Haven, Naughty Dog, PDI, Bandai Namco, Sony Interactive Global, Rockstar Games. **Com o board literalmente vazio (0 vagas):** Blur Studio, Coatsink, Insomniac.

---

# TRÊS ENTRADAS DE "IMPEDIMENTO OPERACIONAL" QUE EU FUI CONFERIR

Você mandou procurar o recibo antes de te mandar trabalhar nelas. Fui:

- **Kevuru Games** (Kiev) — "PREENCHIDA SEM PROVA em 07/09". Formulário é **Contact Form 7 dentro de um modal**.
- **Moonmana** (Gdańsk/Tenerife) — "PREENCHIDA SEM PROVA, provável reCAPTCHA". Formulário **WPForms**.
- **L'Atelier Animation** (Montreal) — "ENVIADA DUAS VEZES SEM PROVA".

**As três estão fora do alcance desta caçada e não entram na fila:** nenhuma usa uma das cinco famílias que passam — Contact Form 7 com reCAPTCHA está na sua própria lista de parede. **Não achei recibo de resolução para nenhuma das três.** Continuam pendentes de verdade, mas por um caminho que não é este.

---

# A LEITURA HONESTA DA RODADA

**A hipótese não se confirmou, e o número diz por quê.** Das 317 casas de site próprio que sondei — 300 responderam, 3.528 sondagens de slug e mais 547 de raiz de domínio — só **31 quadros** apareceram numa família que passa, e a maioria esmagadora **já era conhecida do painel** (Epic, Riot, Rockstar, 2K, Hasbro, Sony, os boards da PlayStation). O estúdio médio do `PORTAIS` registrado pelo site próprio **não tem quadro escondido**: ele tem um formulário de WordPress, um endereço de email, ou nada. A pergunta valia ser feita; a resposta é "quase não tem", e agora está medida.

**As armadilhas de slug que a rodada confirmou.** Das 58 batidas cruas da varredura, **21 eram falso positivo de slug genérico** — `career`, `jobs`, `explore`, `system`, `company`, `onyx`, `recruit`, `artstation` são quadros de **outras empresas** que por acaso ocupam aquele nome no Greenhouse ou no Breezy. `parkerschauffeurs.teamtailor.com` apareceu em três casas de jogos diferentes porque é um asset compartilhado do CDN do Teamtailor. **Bater slug sem confirmar que o quadro é da casa certa produz lixo em escala** — foi por isso que rodei tudo por API e não por presença de string.

**O ERRO QUE EU COMETI E PEGUEI SOZINHO, e é o mais importante daqui.** Eu tinha esta fila com **quatro** linhas. Duas delas — Bluehole 8517791002 e Loonshot 8651145002 — eu tinha classificado como "livre, segurada por decisão de ritmo de 07/09 que venceu". **Estava errado: as duas foram enviadas e confirmadas em 08/09 às 07h32 e 07h33 UTC.** O que me enganou: as entradas do painel são longas e trazem, **concatenados na mesma célula**, o texto do adiamento de 07/09 **e** o recibo de envio de 08/09. Eu li a primeira ocorrência de cada ID, vi "REQUISICAO LIVRE E NAO ENVIADA POR DECISAO ESCRITA", e parei. Só peguei o erro na conferência final, quando em vez de contar ocorrências do ID fui procurar o **padrão do recibo** — `<id>/confirmation`. **A regra que fica: dedupe por ID não é contar ocorrência, é ler todas as ocorrências até o fim da célula, e o teste barato que resolve é grepar `<id>/confirmation` e `ENVIADA` junto do ID.** Se eu tivesse entregado sem isso, você teria batido duas vezes na mesma porta em duas casas.

**Onde a rodada de fato rendeu, e não foi onde eu procurei.** Nenhuma das duas linhas da fila veio de "achei um Greenhouse escondido num site próprio". A da **beffio** veio de uma casa marcada `done=true` cujo quadro tinha uma **quarta requisição** que nenhuma rodada tinha listado — o painel fecha a casa quando fecha as vagas conhecidas dela. A do **Loonshot** veio de um **adiamento com hora marcada** que ninguém voltou pra cobrar.

**As duas lições de processo, ditas curto:**
1. **Adiamento por ritmo precisa de data de vencimento e precisa voltar sozinho pra fila**, senão "segurar por hoje" vira "nunca" — e desta vez o maestro voltou (Bluehole e Loonshot Modeler saíram em 08/09), mas a terceira (8085897002) ficou pra trás mesmo estando escrita a palavra "AMANHÃ" no recibo.
2. **Casa com `done=true` não é casa esgotada.** Vale revarrer o quadro inteiro das casas onde a campanha já enviou, porque o painel guarda a vaga, não o quadro. Foi assim que a beffio apareceu.

**O que eu NÃO fiz, e você deveria saber:** não abri navegador, não commitei, não fiz push, não mandei email, não preenchi formulário nenhum, e não toquei em `docs/index.html`, `FILA-DO-VINI.md`, `enviados.csv` nem `processados.csv`. **Dezessete das 317 páginas não responderam** nesta rodada (DNS, TLS ou timeout) e ficaram **sem veredito** — não são parede, é leitura faltando, e uma rodada de outra rede as resolve.
