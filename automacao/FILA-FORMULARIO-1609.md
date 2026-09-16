# FILA DE FORMULÁRIO — 16/09/2026 (Jhon B, triagem; **nada foi enviado aqui**)

Agente de **triagem**, sem navegador. Zero envio, zero rascunho, zero linha nova em
`enviados.csv`, `processados.csv`, `docs/index.html`, `pessoas.csv` ou `PESSOAS-SEM-CARTA.md`.
Isto é **fila pronta para o Jhon A consumir de cima para baixo**: quanto mais alto, menos atrito.

**Ordem do arquivo:** Personio → Teamtailor (vaga servida) → Teamtailor Connect → Pinpoint →
Greenhouse → JazzHR (parede medida) → Recruitee → Workable → não conferido. Dentro de cada
faixa, **personagem primeiro**.

## O que foi medido nesta rodada, em números

| Medida | Valor |
|---|---|
| Quadros de ATS lidos por API | **694** (142 Teamtailor + 19 TT novos + 14 TT novos por token europeu + 91 Greenhouse + 39 Personio + 3 Personio novos + 79 BambooHR + 74 Recruitee + 21 Pinpoint + 10 JazzHR + SmartRecruiters global (9 termos) + Workable global (6 termos)) |
| Vagas lidas, título a título | **≈ 7.400** (1.745 TT + 96 TT novos + 2.179 GH + 124 Personio + 285 BambooHR + 662 Recruitee + 37 Pinpoint + 60 JazzHR + 302 SR + ~1.900 Workable) |
| Sondagens de token cegas | **7.581** (1.454 tokens × Greenhouse/Teamtailor/Personio/Pinpoint + 1.662 tokens europeus × Personio/Teamtailor) |
| Quadros NOVOS achados por adivinhação de token | **36** (11 Greenhouse, 19 Teamtailor, 18 Personio, com repetição entre listas) |
| Vagas de PERSONAGEM inéditas nesses quadros novos | **ZERO** — a adivinhação achou quadro, não achou vaga da disciplina |
| Portas prontas nesta fila | **41** |
| Portas de personagem/disciplina literal | **9** |
| Caíram na régua de veto (frase escrita) | **5** |
| Caíram no dedupe (ID já enviado) | **31** |
| `NÃO CONFERIDO` | **2** |

**A leitura honesta, e ela manda no resto do dia:** a superfície de *vaga aberta de personagem*
nos ATS que a campanha conhece está **seca** — 31 das requisições que bateram a régua de
disciplina hoje já tinham envio registrado (Imageworks, Cloud Chamber, 2K, Hasbro, Bluehole,
Loonshot, Riot, Epic, Mob, High Dive, Sway Box, Absurd, Scopely). O estoque que sobra é
**candidatura espontânea e banco de talentos em lane que passa** (Personio, Teamtailor, Pinpoint),
mais **três vagas de personagem atrás de parede de captcha** (Zoic Vancouver, Stellar Vancouver,
Side). Fila inflada seria pior que o número honesto.

## BLOCO PADRÃO DE RESPOSTAS (vale para TODAS as portas; só o que muda está em cada ficha)

| Campo | Valor |
|---|---|
| Nome | `Vini` / `Cavalcanti` |
| Email | `contact@vinicavalcanti.art` |
| Telefone | **nunca escrito aqui.** `VINI_TEL` no ambiente, ou `pessoal.json` em `/home/user/apply` (fora do repositório). Sempre com **código do país explícito** — o widget `intl-tel-input` já transformou o número dele em `+81`/Japão uma vez |
| Endereço / cidade | Olinda, Pernambuco, Brasil — **escolhido da lista** de sugestões quando o campo for autocomplete (se ficar só "Brazil", o `place_id` vem vazio) |
| LinkedIn | `https://www.linkedin.com/in/vinicavalcnti/` |
| Portfólio | `https://www.artstation.com/viniciuscavalcanti` |
| CV | `/home/user/apply/Vini_Cavalcanti_CV.pdf` |
| Carta | `/home/user/apply/Vini_Cavalcanti_Cover_Letter.pdf` (campo de carta é **separado** do de CV; no BambooHR o de carta vem ANTES e também aceita PDF) |
| Autorização de trabalho | **a verdade, sempre.** EUA / Canadá / Austrália / NZ / Reino Unido / UE: **No**. Precisa de patrocínio: **Yes**. Ele não é cidadão da UE |
| Liderança de equipe | **Yes** (cinco anos de Senior na E-Line, professor, fundador da própria escola, mestrando) |
| Pretensão | base da faixa publicada; sem faixa, a regra de 04/09 (abaixo, por porta). Sempre com a abertura **"Open to aligning with your band for the role"**. **Salário atual da E-Line nunca se revela** |
| Pronomes | `He/Him` |
| Campo isca | conferir que ficou **vazio** todo campo cujo `name` case com `/^hp[_-]|honeypot|nickname_|bot[_-]?field/i` ou cujo rótulo diga "leave this field blank" |

---

# ÍNDICE

## Faixa 1 — PERSONIO (formulário monta no clique em "Apply for this job"; **zero captcha no HTML**)

| # | Casa | Porta | País/Cidade | Lane | Disciplina |
|---|---|---|---|---|---|
| 1 | Bongfish | Open Application `366240` | Áustria (Graz) | Personio | espontânea (arte) |
| 2 | Deck13 Interactive | General Application (f/m/x) `2725779` | Alemanha (Frankfurt) / Remote (EU) | Personio | espontânea (arte) |
| 3 | Chimera Entertainment | speculative application `150955` | Alemanha (Munique) | Personio | espontânea (arte) |

## Faixa 2 — TEAMTAILOR, vaga com formulário SERVIDO NO HTML (zero captcha)

| # | Casa | Porta | País/Cidade | Lane | Disciplina |
|---|---|---|---|---|---|
| 4 | **Snowprint Studios** | **Senior 3D Character Artist `8341580`** | Suécia (Estocolmo) | Teamtailor | **PERSONAGEM** |
| 5 | Snowprint Studios | Senior 3D Environment Artist `8380596` | Suécia (Estocolmo) | Teamtailor | ambiente |
| 6 | Gigglebug Entertainment | Open application! `1838376` | Finlândia (Helsinque) e Espanha (Las Palmas) | Teamtailor | espontânea (animação) |
| 7 | Untold Studios | General Application `1314008` | EUA (Los Angeles) | Teamtailor | espontânea (VFX) |
| 8 | Star Stable Entertainment | Open Application `244302` | Suécia (Estocolmo) | Teamtailor | espontânea, área **Art** |
| 9 | Fully | Open application `6360996` | Suécia (Gotemburgo, híbrido) | Teamtailor | espontânea (Games Development) |
| 10 | North Kingdom | Freelancers of Europe `7362964` | Suécia (Estocolmo/Skellefteå) | Teamtailor | espontânea (design digital) |

## Faixa 3 — TEAMTAILOR CONNECT (banco de talentos; zero captcha; **não há script pronto na caixa nova**)

| # | Casa | Porta | País/Cidade | Lane | Disciplina |
|---|---|---|---|---|---|
| 11 | **Tactical Adventures** | Connect, cargo **Lead 3D Character Artist `644185`** (dep. Art `246284`) | França (Paris) | TT Connect | **PERSONAGEM** |
| 12 | Princess Bento | Connect, cargo **Character Artist `1240636`** (dep. Art `488901`) | Reino Unido (Londres) | TT Connect | **PERSONAGEM com ressalva (casa 2D)** |
| 13 | Envar Studio | Connect, dep. **3D Art `395135`** | Noruega (Oslo) | TT Connect | ambiente/3D |
| 14 | Black Kite Studios | Connect, dep. **CG `155713`** | Reino Unido (Londres) | TT Connect | CG/VFX |
| 15 | Territory Studio | Connect, dep. **VFX `119793`** | Reino Unido (Londres) | TT Connect | VFX |
| 16 | Untold Studios | Connect, dep. **VFX `88810`** | Reino Unido (Londres) / EUA (LA) | TT Connect | VFX |
| 17 | Raw Fury | Connect, cargo **Freelancer - 3D Artist `121776`** | Suécia (Estocolmo) | TT Connect | 3D |
| 18 | Goodgame Studios | Connect, dep. **Game Art `309870`** | Alemanha (Hamburgo) | TT Connect | arte de jogo |
| 19 | New Moon Production | Connect, dep. **Game Art `325621`** | Alemanha (Hamburgo) | TT Connect | arte de jogo |
| 20 | OFM Studios | Connect, dep. **Game Art `374882`** | Alemanha | TT Connect | arte de jogo |
| 21 | Playa Games | Connect, dep. **Game Art `339731`** | Alemanha (Hamburgo) | TT Connect | arte de jogo |
| 22 | Sandbox Interactive | Connect, dep. **Game Art `359924`** | Alemanha (Berlim) | TT Connect | arte de jogo |
| 23 | Stillfront Group | Connect, dep. **Game Art `305316`** | Suécia (Estocolmo) | TT Connect | arte de jogo (holding) |
| 24 | Swift Games | Connect, dep. **Art `269483`** | Suécia | TT Connect | arte de jogo |
| 25 | Triband | Connect, dep. **Game Production** | Dinamarca (Copenhague) | TT Connect | espontânea (jogos) |
| 26 | TapNation | Connect, dep. **Product** | França (Paris) | TT Connect | espontânea (mobile) |

## Faixa 4 — PINPOINT, banco de talentos (rota `register-your-interest`, zero captcha, 10 envios confirmados nesta lane em 10/09)

| # | Casa | Porta | País/Cidade | Lane | Disciplina |
|---|---|---|---|---|---|
| 27 | **Hyper Hippo Entertainment** | Register Your Interest, dep. **Art** | Canadá (**Remote Canada**, sede Kelowna BC) | Pinpoint | arte de jogo |
| 28 | Sun Creature | Register Your Interest | Dinamarca (Copenhague) | Pinpoint | espontânea (animação estilizada) |

## Faixa 5 — GREENHOUSE (reCAPTCHA **invisível**, pontuação de sessão + código por email: lane que passa)

| # | Casa | Porta | País/Cidade | Lane | Disciplina |
|---|---|---|---|---|---|
| 29 | Eleventh Hour Games | Senior Environment Artist `8501085002` | Remoto (EUA, núcleo 10h–16h CT) | Greenhouse | ambiente |

## Faixa 6 — JAZZHR: **reCAPTCHA v2 de caixa, medido com clique em 12/09** (parede; só vai à mão, e só o que for Vancouver pela regra de 16/09)

| # | Casa | Porta | País/Cidade | Lane | Disciplina |
|---|---|---|---|---|---|
| 30 | **Zoic Studios** | **BC, 3D Character Modeler, Senior** | Canadá (**Vancouver**) | JazzHR (parede) | **PERSONAGEM** |
| 31 | Certain Affinity | Advanced Material Artist `AgAMjfmeKe` | Canadá (Grande Vancouver, BC) | JazzHR (parede) | **surfacing/material** |
| 32 | Certain Affinity | Advanced Material Artist `eJTHIpzicy` | Canadá (Grande Toronto, ON) | JazzHR (parede) | **surfacing/material** |
| 33 | Zoic Studios | BC General Application | Canadá (Vancouver) | JazzHR (parede) | espontânea |
| 34 | Next Level Games (Nintendo) | General Application | Canadá (Vancouver) | JazzHR (parede) | espontânea |
| 35 | Zoic Studios | U.S. General Application | EUA (Culver City) | JazzHR (parede) | espontânea |
| 36 | Obsidian Entertainment | General Application | EUA (Irvine, CA) | JazzHR (parede) | espontânea |
| 37 | Outplay Entertainment | Speculative Applications | Reino Unido (Dundee) | JazzHR (parede) | espontânea |

## Faixa 7 — RECRUITEE (hCaptcha de imagem **depois** do Send: parede provável)

| # | Casa | Porta | País/Cidade | Lane | Disciplina |
|---|---|---|---|---|---|
| 38 | Framestore | 3D Modeller — contrato curto `2120070` | Canadá (Montréal) | Recruitee (parede) | **PERSONAGEM (modelagem)** |

## Faixa 8 — WORKABLE (Turnstile depois do submit + 429 do IP: parede)

| # | Casa | Porta | País/Cidade | Lane | Disciplina |
|---|---|---|---|---|---|
| 39 | Side (PTW) | 3D Character Artist — Talent Pool (EU) | Reino Unido (Londres) | Workable (parede) | **PERSONAGEM** |
| 40 | Side (PTW) | Senior Texture Artist | Canadá (Toronto) | Workable (parede) | **PERSONAGEM (textura)** |
| 41 | Side (PTW) | Senior Texture Artist | Canadá (Montréal) | Workable (parede) | **PERSONAGEM (textura)** |

**Caíram na régua de veto** (frase literal na seção final): Stirling Animation, Image Engine
General Application, weltenbauer Environment Artist, weltenbauer Tech Artist, Stellar Creative Lab.
**Caíram no dedupe** (31 IDs, na seção final). **`NÃO CONFERIDO`:** Liquid Swords (TLS) e
Side/Workable (corpo do anúncio não lido por 429 do IP).

---
# FAIXA 1 — PERSONIO

> **Como a lane se comporta, medido hoje:** o HTML servido das três páginas **não tem
> `recaptcha`, `hcaptcha`, `turnstile`, `datadome` nem `perimeterx`** (grep no HTML inteiro).
> O formulário **não existe no HTML** até alguém clicar em **"Apply for this job"**: ele monta
> em JavaScript no mesmo endereço. **Não há `apply_personio.js` na caixa nova de
> `/home/user/apply`** (ele morreu com o contêiner antigo); o que existe e serve é
> `preencher-formulario.js` (preenche por rótulo, no navegador) ou `apply_own.js` com o mapa de
> campos. **Armadilha conhecida da lane:** o Submit fica **cinza** enquanto faltar obrigatório e
> **não diz qual**; e quando existir `#doc-input-cover-letter` marcado com `*`, a carta tem de
> ir nesse campo, não em `other`.

## 1. Bongfish — Open Application (Graz, Áustria)

- **Formulário:** `https://bongfish.jobs.personio.com/job/366240?display=en` → botão *Apply for this job*
- **Requisição:** `366240` · **Casa:** Bongfish GmbH · **Cargo:** Open Application Bongfish
- **País/cidade:** Áustria, Graz (Am Eisernen Tor 3/2) · presencial
- **Faixa publicada:** nenhuma. **Pretensão:** EUR 45.000/ano (regra de 04/09, casa pequena/média na Europa) + *"Open to aligning with your band for the role"*
- **Régua de veto:** rodada no texto visível inteiro (974 caracteres): **zero acertos** dos 22 termos. Sem veto escrito.
- **Dedupe:** `sh automacao/dedupe-agora.sh "366240" "Bongfish"` → ocorrências em `processados.csv` (2) e `docs/index.html` (1), **nenhuma com marca de envio**; a casa aparece como quadro lido, não como candidatura. Gmail por "Bongfish": nada.
- **Perguntas customizadas:** a armadilha desta casa já foi medida em rodada anterior — **"Where did you hear about this position"** é obrigatória e é a que deixa o Submit cinza. Responder: `Personio careers page`.
- **Script e comando:**
  `cd /home/user/apply && VINI_TEL='<código do país + número>' sh hb_run.sh preencher-formulario.js` (ou `apply_own.js ans_bongfish.json bongfish` com o mapa de campos depois do clique em Apply)
- **Gancho (texto literal do anúncio):** *"There are currently no fitting vacancies, but you would be interested to work with us? We are always working on new projects and looking for motivated talents to join us."*
- **Ressalva honesta:** é espontânea, não vaga; Bongfish é co-desenvolvimento (Motocross/Grip), personagem não é o produto central.

## 2. Deck13 Interactive — General Application (f/m/x) (Frankfurt / Remote EU)

- **Formulário:** `https://deck13.jobs.personio.com/job/2725779?display=en` → *Apply for this job*
- **Requisição:** `2725779` · **Casa:** Deck13 Interactive GmbH · **Departamento no ATS:** `Creative`
- **País/cidade:** Alemanha (Frankfurt, perto da Messe) — a vaga está marcada **Remote (EU)**
- **Faixa publicada:** nenhuma. **Pretensão:** EUR 55.000/ano (casa grande de AA europeia, regra de 04/09) + a abertura padrão
- **Régua de veto:** 2.781 caracteres lidos. Três acertos, **os três falsos positivos**: *"A modern, centrally located office in Frankfurt, Germany (near Messe)"*, *"Free language courses to help you expand your skills"* e *"Since our founding in 2001, in the heart of Frankfurt, Germany"*. **Nenhum veto escrito de residência, idioma ou autorização.**
- **Dedupe:** `sh automacao/dedupe-agora.sh "2725779" "Deck13"` → 1 ocorrência em `processados.csv` sem marca de envio (quadro lido). **Rota inédita.**
- **Perguntas customizadas:** o anúncio pede em texto: carta, CV e portfólio. Campos do formulário só aparecem depois do clique.
- **Script e comando:** `cd /home/user/apply && sh hb_run.sh preencher-formulario.js` (Personio sem script próprio nesta caixa)
- **Gancho:** *"Whether you're an artist, programmer, designer, or have another unique skill set, we'd love to hear from you."* — e o anúncio ainda diz *"If you're a freelancer, we encourage you to use this form as well"*, o que abre a porta de freelance sem visto.
- **Por que vale:** o mesmo quadro tem **Senior VFX Artist** e **Lead VFX Artist** abertos em `Remote (EU)`, o que prova que a casa contrata arte remota na Europa.

## 3. Chimera Entertainment — speculative application (Munique)

- **Formulário:** `https://chimera-entertainment.jobs.personio.com/job/150955?display=en` → *Apply for this job*
- **Requisição:** `150955` · **Departamento no ATS:** `Game Design` · **Local:** DE - Munich Office
- **Faixa publicada:** nenhuma. **Pretensão:** EUR 45.000/ano + abertura padrão
- **Régua de veto:** 2.737 caracteres. Acertos e classificação: *"Chimera Entertainment is a creative and independent game development studio based in the heart of Munich"* → **falso positivo** (`based in` descrevendo a sede); *"we rank among Germany's leading studios"* → **falso positivo**. **Atenção ao que é real:** o anúncio traz um bloco de **estágio obrigatório** (*"The internship must be mandatory and part of your degree program (Pflichtpraktikum...)"*, *"On-site work in our Munich office (remote work is not possible)"*) — isso vale para **estágio**, e é o trecho a ignorar em candidatura sênior, mas é também o motivo de esta porta ficar em terceiro lugar da faixa.
- **Dedupe:** `sh automacao/dedupe-agora.sh "150955" "Chimera"` → 1 ocorrência em `processados.csv`, sem marca de envio. **Inédita.**
- **Script e comando:** `cd /home/user/apply && sh hb_run.sh preencher-formulario.js`
- **Gancho:** *"Our portfolio spans over 25 published titles – including award-winning franchises like \"Angry Birds Epic\" and \"Angry Birds Evolution.\""* — personagem estilizado de IP licenciada é exatamente o registro do portfólio dele.
- **Ressalva:** as três vagas técnicas abertas do mesmo quadro estão em **Cebu, Filipinas**, fora do recorte; a porta de Munique é a espontânea.

---

# FAIXA 2 — TEAMTAILOR, VAGA COM FORMULÁRIO SERVIDO

> **Medido hoje em todas as sete:** `GET <url da vaga>/applications/new` devolve **200 com o
> formulário inteiro no HTML** (`candidate[first_name]`, `candidate[email]`,
> `candidate[resume]`, `candidate[answers_attributes][N][...]`), e **zero** ocorrência de
> `recaptcha`, `hcaptcha`, `turnstile`, `datadome` ou `perimeterx`. A lane passa.
> **Três armadilhas que continuam valendo:** (a) responder pergunta `choice` sem dizer a opção
> faz o script marcar a **primeira** — e em pergunta de elegibilidade a primeira costuma ser
> "Yes", ou seja, mentiria; (b) o dropzone do CV carrega em pedaço separado do JavaScript, então
> **conferir o anexo antes de enviar**; (c) se a tela final disser **"Verify your email"**, a
> candidatura **não entrou** até o link do email ser aberto.

## 4. ★ Snowprint Studios — Senior 3D Character Artist (Estocolmo) — **PERSONAGEM**

- **Formulário:** `https://snowprintstudios.teamtailor.com/jobs/8341580-senior-3d-character-artist/applications/new`
- **Anúncio:** `https://snowprintstudios.teamtailor.com/jobs/8341580-senior-3d-character-artist` · publicado **08/09/2026** · departamento `Art`
- **Requisição:** `8341580` · **Casa:** Snowprint Studios (Estocolmo, Suécia)
- **Faixa publicada:** nenhuma. **Pretensão:** EUR 45.000/ano (casa média; ≈ SEK 520.000/ano) + *"Open to aligning with your band for the role"*
- **Régua de veto:** anúncio inteiro lido, 8.874 caracteres → **ZERO acertos dos 22 termos**. Sem veto de residência, de idioma, de autorização ou de presença.
- **Dedupe:** `sh automacao/dedupe-agora.sh "8341580" "Snowprint"` → `enviados.csv` **0**, `FILA-DO-VINI.md` **0**; 5 ocorrências em `processados.csv` e 1 no painel **sem nenhuma marca de envio** (são a leitura do quadro em rodadas anteriores). O que a casa já tem é o **Connect/banco de talentos, enviado em 07/09** — porta diferente, requisição diferente. Gmail por "Snowprint": 14 linhas em `processados` referem-se ao cadastro do Connect, não a esta vaga. **ROTA LIVRE.**
- **Perguntas customizadas, medidas no HTML:**
  | slot | tipo | pergunta (texto literal) | resposta |
  |---|---|---|---|
  | 0 | `choice` **obrigatória** | *"Do you need visa or relocation support to work in Sweden?"* (opções Yes/No) | **Yes** (a verdade; `opcao: "Yes"`, nunca por valor) |
  | 1 | `text` **obrigatória** | *"Please add a link to your portfolio"* | `https://www.artstation.com/viniciuscavalcanti` |
  Campos de consentimento: `candidate[consent_given]` e `candidate[consent_given_future_jobs]` (marcar os dois). **Não há `candidate[location_ids][]`** nesta vaga.
- **Script e comando:**
  `cd /home/user/apply && VINI_TEL='<código do país + número>' sh hb_run.sh apply_teamtailor.js "https://snowprintstudios.teamtailor.com/jobs/8341580-senior-3d-character-artist" snowprint carta_snowprint.txt`
  (rodar **sem** `--submit` primeiro; as respostas das duas perguntas vão em `/home/user/apply/ansq_snowprint.json`, casando pelo **texto** da pergunta, com `opcao` explícita na `choice`)
- **Gancho (literal):** *"Would you like to take ownership of character art in a small game team, combining hands-on 3D work with shaping how characters are created and delivered?"* — e o anúncio ainda diz *"You'll be the main in-house character artist on the team"*.
- **Por que é a primeira da fila:** é a **única vaga aberta de personagem** achada hoje numa lane sem parede, em país do recorte, com a pergunta de visto respondível com a verdade e sem veto escrito.

## 5. Snowprint Studios — Senior 3D Environment Artist (Estocolmo)

- **Formulário:** `https://snowprintstudios.teamtailor.com/jobs/8380596-senior-3d-environment-artist/applications/new`
- **Requisição:** `8380596` · publicado **15/09/2026** · departamento `Art`
- **Faixa/pretensão:** igual à #4 (EUR 45.000/ano + abertura)
- **Régua de veto:** 8.011 caracteres → **zero acertos**.
- **Dedupe:** `sh automacao/dedupe-agora.sh "8380596" "Snowprint"` → **zero ocorrências nos quatro arquivos**. Inédita.
- **Perguntas:** as mesmas duas da #4 (`choice` de visto/relocação na Suécia → **Yes**; `text` de portfólio).
- **Comando:** `sh hb_run.sh apply_teamtailor.js "https://snowprintstudios.teamtailor.com/jobs/8380596-senior-3d-environment-artist" snowprint-env carta_snowprint_env.txt`
- **Gancho:** *"You'll create stylized environments, props, and items, and assemble them in Unity to procedurally set-dress, light and build clear, immersive worlds that support the gameplay."* e *"What we'll be looking for in your portfolio: Nicely set dressed, lit and composed stylized environments with props made by yourself."*
- **Ressalva honesta:** é **ambiente**, não personagem. Entra porque é a mesma casa da #4 (duas requisições, dois envios legítimos) e porque o anúncio pede **estilizado**, que é o registro dele. Mandar as duas na mesma casa é aceitável; a de personagem vai primeiro.

## 6. Gigglebug Entertainment — Open application! (Helsinque / Las Palmas)

- **Formulário:** `https://gigglebug.teamtailor.com/jobs/1838376-open-application/applications/new`
- **Requisição:** `1838376` · **Locais:** Helsinki (Finlândia) e Las Palmas (Espanha, Gran Canaria)
- **Faixa:** nenhuma. **Pretensão:** EUR 45.000/ano + abertura
- **Régua de veto:** 3.188 caracteres → **zero acertos**.
- **Dedupe:** `sh automacao/dedupe-agora.sh "1838376" "Gigglebug"` → **zero ocorrências nos quatro arquivos** por ID. A casa tem histórico de **cadastro no Connect (27/08)**, que é porta diferente. **Rota livre.**
- **Perguntas customizadas (nove slots, e três decidem a candidatura):**
  | slot | tipo | pergunta | resposta |
  |---|---|---|---|
  | 0 | text | *"Portfolio link + possible pw"* | `https://www.artstation.com/viniciuscavalcanti` |
  | 1 | text | *"Add the person, their position, the company and their email for reference call."* | referência da E-Line — **não inventar**: usar só contato que ele já autorizou; se não houver, escrever *"Happy to provide references on request"* |
  | 2 | text | *"When is your earliest start date?"* | `Immediately / 30 days notice` |
  | 3 | choice obrigatória | *"Are you already in Finland?"* | **No** |
  | 5 | choice | *"Are you already in the Canaries?"* | **No** |
  | 6 | choice | *"Are you willing to relocate in Gran Canarias?"* | **Yes, I am!** |
  | 7 | choices | *"What type of employment are you most interested in?"* | `Full time` (e `Freelance/Part time` como segunda, se aceitar múltipla) |
  | 8 | choices | *"How did you hear about us?"* | `SoMe` ou `Through network` — **não** marcar a opção "I know someone from Gigglebug", que pede nome na carta |
  **Tem `candidate[location_ids][]`** (obrigatório): marcar **Helsinki e Las Palmas**, pela chave `locations` do `ansq_gigglebug.json`.
- **Comando:** `sh hb_run.sh apply_teamtailor.js "https://gigglebug.teamtailor.com/jobs/1838376-open-application" gigglebug carta_gigglebug.txt`
- **Gancho:** o corpo do anúncio é só o título — **não há frase própria para citar**. O gancho honesto sai da própria pergunta do formulário (*"Are you willing to relocate in Gran Canarias?"*) e do catálogo da casa (animação infantil estilizada). **Não inventar frase de anúncio.**

## 7. Untold Studios — General Application (Los Angeles)

- **Formulário:** `https://untoldstdfg1324556.teamtailor.com/jobs/1314008-general-application/applications/new`
- **Requisição:** `1314008` · **Local:** EUA, Los Angeles · departamento `Untold Studios`
- **Faixa:** nenhuma. **Pretensão:** USD 100.000/ano (casa grande, EUA; regra de 04/09) + abertura
- **Régua de veto:** 3.611 caracteres → **zero acertos**. (Autorização nos EUA é **No** + patrocínio **Yes** nas perguntas.)
- **Dedupe:** `sh automacao/dedupe-agora.sh "1314008" "Untold"` → `enviados.csv` 0, `processados.csv` 0, painel **2 ocorrências sem marca de envio**. Livre.
- **Perguntas customizadas (cinco, todas `text`):** *"Could you share your salary expectations please?"* → `USD 100,000 – open to aligning with your band for the role`; *"When are you available from?"* → `Immediately / 30 days notice`; *"Could you provide your showreel / portfolio link please?"* → ArtStation; *"Where are you currently based?"* → `Olinda, Pernambuco, Brazil (open to relocation, sponsorship required)`; *"What are your preferred pronouns?"* → `He/Him`.
- **Comando:** `sh hb_run.sh apply_teamtailor.js "https://untoldstdfg1324556.teamtailor.com/jobs/1314008-general-application" untold-la carta_untold.txt`
- **Gancho:** *"Our purpose is to do brilliant creative work, to make content that audiences want to watch & to have fun while we're doing it. Join us!"*
- **Ressalva honesta:** o corpo da vaga é de **2021** (*"we are opening in sunny Los Angeles, in the Autumn of 2021"*) — é porta espontânea antiga que continua publicada. O valor é entrar no banco de uma casa de VFX com escritório em LA e em Londres, não uma vaga.

## 8. Star Stable Entertainment — Open Application (Estocolmo)

- **Formulário:** `https://starstable.teamtailor.com/jobs/244302-open-application/applications/new`
- **Requisição:** `244302` · **Local:** Suécia, Estocolmo
- **Faixa:** nenhuma. **Pretensão:** EUR 45.000/ano + abertura
- **Régua de veto:** 3.454 caracteres → **zero acertos**.
- **Dedupe:** `sh automacao/dedupe-agora.sh "244302" "Star Stable"` → **zero ocorrências por ID**. A casa tem Connect já feito (porta diferente). Livre.
- **Perguntas customizadas:** três slots — dois `text` (um deles rotulado *"Needed for this role"*) e **um `choice` que é o que importa: a lista de áreas**, com as opções `Art`, `Design`, `Animation`, `Production`, `HR/TA/Office`, `Analytics & Insights`, `Marketing`, `Finance/Legal`, `Game Tech`, `Tech`, `QA`, `Internship`, `Other` → **marcar `Art`** (`opcao: "Art"`, explícita).
- **Comando:** `sh hb_run.sh apply_teamtailor.js "https://starstable.teamtailor.com/jobs/244302-open-application" starstable carta_starstable.txt`
- **Gancho:** *"Interested in joining our team but don't see your dream job posted? Leave us your details and if something opens up (which it often does), we will reach out to you!"*
- **Por que vale:** Star Stable é jogo de **personagem estilizado** (cavalos e avatares), e a escolha de área `Art` põe o cadastro na fila certa.

## 9. Fully — Open application (Gotemburgo, híbrido)

- **Formulário:** `https://fully.teamtailor.com/jobs/6360996-open-application/applications/new`
- **Requisição:** `6360996` · **Local:** Suécia, Gotemburgo · **Remote status:** Hybrid
- **Faixa:** nenhuma. **Pretensão:** EUR 45.000/ano + abertura
- **Régua de veto:** 2.246 caracteres → **zero acertos**.
- **Dedupe:** `sh automacao/dedupe-agora.sh "6360996" "Fully"` → **zero ocorrências**. Casa inédita na campanha.
- **Perguntas customizadas:** **nenhuma** (zero slots). Só os campos base + consentimento.
- **Comando:** `sh hb_run.sh apply_teamtailor.js "https://fully.teamtailor.com/jobs/6360996-open-application" fully carta_fully.txt`
- **Gancho:** *"Can't find the right role listed? We're always curious about new talent. Send us your open application and let's explore what we can create together."*
- **Ressalva honesta:** a Fully é consultoria sueca com **departamento `Games Development`** no próprio menu de carreiras — não é estúdio de animação. Encaixe médio-baixo; entra porque é porta sem atrito e a casa coloca gente em estúdio de jogo.

## 10. North Kingdom — Freelancers of Europe (Suécia)

- **Formulário:** `https://northkingdom.teamtailor.com/jobs/7362964-freelancers-of-europe/applications/new`
- **Requisição:** `7362964` · publicado **10/03/2026** · **Casa:** North Kingdom (Estocolmo e Skellefteå)
- **Faixa:** nenhuma. **Pretensão:** EUR 45.000/ano equivalente, ou **dia de freelance** se o formulário pedir — usar a abertura padrão
- **Régua de veto:** o título já delimita o escopo à **Europa**; sem veto de idioma nem de autorização no texto lido.
- **Dedupe:** `sh automacao/dedupe-agora.sh "7362964" "North Kingdom"` → **zero ocorrências nos quatro arquivos. Casa NOVA na campanha** (achada hoje pela sondagem de tokens europeus).
- **Comando:** `sh hb_run.sh apply_teamtailor.js "https://northkingdom.teamtailor.com/jobs/7362964-freelancers-of-europe" northkingdom carta_northkingdom.txt`
- **Gancho:** o próprio título, *"Freelancers of Europe"*, é o gancho: é registro aberto de freelance para a Europa, o que dispensa visto de trabalho.
- **Ressalva honesta:** ele mora no Brasil, não na Europa — a porta diz "of Europe". Vale registrar assim mesmo, com a verdade escrita no campo livre, mas o encaixe geográfico é fraco e por isso ela fecha a faixa.

---
