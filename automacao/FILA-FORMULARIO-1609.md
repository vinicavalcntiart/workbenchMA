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
| Portas prontas nesta fila | **40** |
| Portas de personagem/disciplina literal | **8** |
| Caíram na régua de veto (frase escrita) | **8** |
| Caíram no dedupe (ID já enviado, recusado ou com recibo) | **59** |
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

## Faixa 6 — JAZZHR: **reCAPTCHA v2 de caixa, medido com clique em 12/09** (parede; vai à mão, e pela regra de 16/09 só o que for Vancouver entra na lista da mão dele)

| # | Casa | Porta | País/Cidade | Lane | Disciplina |
|---|---|---|---|---|---|
| 30 | **Certain Affinity** | Advanced Material Artist `AgAMjfmeKe` | Canadá (Grande **Vancouver**, BC) | JazzHR (parede) | **surfacing/material** |
| 31 | Certain Affinity | Advanced Material Artist `eJTHIpzicy` | Canadá (Grande Toronto, ON) | JazzHR (parede) | **surfacing/material** |
| 32 | Zoic Studios | BC General Application | Canadá (**Vancouver**) | JazzHR (parede) | espontânea (VFX) |
| 33 | Next Level Games (Nintendo) | General Application | Canadá (**Vancouver**) | JazzHR (parede) | espontânea (jogos) |
| 34 | Zoic Studios | U.S. General Application | EUA (Culver City) | JazzHR (parede) | espontânea (VFX) |
| 35 | Obsidian Entertainment | General Application | EUA (Irvine, CA / Remote) | JazzHR (parede) | espontânea (jogos) |
| 36 | Outplay Entertainment | Speculative Applications | Reino Unido (Dundee) | JazzHR (parede) | espontânea (mobile) |

## Faixa 7 — RECRUITEE (hCaptcha de imagem **depois** do Send: parede provável)

| # | Casa | Porta | País/Cidade | Lane | Disciplina |
|---|---|---|---|---|---|
| 37 | Framestore | 3D Modeller — contrato curto `2120070` | Canadá (Montréal) | Recruitee (parede) | **PERSONAGEM (modelagem)** |

## Faixa 8 — WORKABLE (Turnstile depois do submit + 429 do IP: parede)

| # | Casa | Porta | País/Cidade | Lane | Disciplina |
|---|---|---|---|---|---|
| 38 | Side (PTW) | 3D Character Artist — Talent Pool (EU) `77511296` | Reino Unido (Londres) | Workable (parede) | **PERSONAGEM** |
| 39 | Side (PTW) | Senior Texture Artist `59e81e55` | Canadá (Toronto, híbrido) | Workable (parede) | **PERSONAGEM (textura)** |
| 40 | Side (PTW) | Senior Texture Artist `4552bd5b` | Canadá (Montréal, híbrido) | Workable (parede) | **PERSONAGEM (textura)** |

**Caíram na régua de veto** (frase literal na seção final, 8 portas): Stirling Animation,
Image Engine General Application, weltenbauer Environment Artist, weltenbauer Tech Artist,
Stellar Creative Lab Modeling Artists, Stellar Creative Lab Surfacing Artists, **Zoic BC 3D
Character Modeler Senior** e Chimera (só o bloco de estágio, que não derruba a espontânea).
**Caíram no dedupe** (59 IDs, na seção final). **`NÃO CONFERIDO`:** Liquid Swords (TLS) e
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
# FAIXA 3 — TEAMTAILOR CONNECT (banco de talentos)

> **O que foi medido nas 146 páginas de Connect lidas hoje:** 122 servem formulário de cadastro
> no HTML; **nenhuma** tem `recaptcha`, `hcaptcha`, `turnstile` ou `datadome`. Os campos do
> primeiro passo são `candidate[email]`, `candidate[department_id]`, `candidate[role_id]`,
> `candidate[consent_given]` e `candidate[consent_given_future_jobs]`.
> **Régua de veto:** as páginas de Connect não têm anúncio. Os únicos acertos dos 22 termos são,
> em todas elas, o mesmo par de **falsos positivos** da política de privacidade — *"...which you
> can find listed here if you are based in the EU"* e *"If you are based in the UK, you can lodge
> a complaint with the Information Commissioner's Office"*. **Nenhum veto escrito em nenhuma.**
>
> **AS QUATRO ARMADILHAS DESTA LANE, e todas já custaram candidatura:**
> 1. **A caixa de consentimento tem um gêmeo escondido com o MESMO `name`** (`input type=hidden value="0"`). `querySelector` pega o escondido, o clique não marca nada e a leitura devolve `false` para sempre. Use `[...document.querySelectorAll('input[name="candidate[consent_given]"]')].find(x=>x.type==='checkbox')`.
> 2. **Sem consentimento o formulário não cria conta: ele vira login**, e devolve a tela mansa *"If we find a Connect account, a sign in link will be sent"*, que parece sucesso e não é.
> 3. **O cadastro é em dois passos.** Passo 1 é email + departamento/cargo + consentimento; o perfil (telefone, endereço, CV, departamentos) se completa depois de entrar pelo **magic link** do email. Peça **um link por vez**: cada pedido novo invalida o anterior.
> 4. **A lista de departamentos fecha em `display:none`** e `check({force:true})` não marca nada sem erro: abra o botão "Select one or more options" e clique em `div[role=menu] button[role=menuitemcheckbox]` casando por **texto exato**, conferindo `.checked` depois. E **recarregue a página** antes de dar por feito.
>
> **NÃO HÁ SCRIPT PRONTO PARA O CONNECT em `/home/user/apply`.** Os modelos que funcionavam
> (`hampa_dep_fix2.js`, `beffio_ok.js`) morreram com o contêiner antigo. Para estas 16 portas:
> ou o Jhon A refaz o modelo a partir das armadilhas acima, ou preenche pelo
> `preencher-formulario.js` no navegador de tela. **A prova de que entrou é
> `/connect/dashboard` listando o cadastro**, não a tela de agradecimento.

## 11. ★ Tactical Adventures — Connect, cargo Lead 3D Character Artist (Paris) — **PERSONAGEM**

- **Formulário:** `https://tacticaladventures.teamtailor.com/connect/candidates/new`
- **O que marcar:** departamento **`Art` (`246284`)**, cargo **`Lead 3D Character Artist` (`644185`)** — o outro cargo do mesmo departamento é `Concept Artist` (`644184`), que **não** é dele.
- **País/cidade:** França, Paris · **Casa:** Tactical Adventures (Solasta, D&D digital)
- **Pretensão (se o perfil pedir):** EUR 45.000/ano + abertura padrão
- **Dedupe:** `sh automacao/dedupe-agora.sh "644185" "Tactical Adventures"` → o ID do cargo do Connect não existe em arquivo nenhum. O que a casa já tem: **carta fria para `jobs@tactical-adventures.com` em 02/09** e a **vaga `8311973` (Lead 3D Character Artist) ENVIADA e confirmada** (registro no painel). **Esta porta é o banco de talentos, objeto diferente da vaga** — e é o caminho de ficar na base depois de a requisição fechar. Se o Jhon A preferir não repetir a casa no mesmo dia, esta é a primeira a adiar.
- **Gancho:** o nome do cargo no próprio menu da casa, **"Lead 3D Character Artist"**, é o gancho: é a casa dizendo que tem cargo de personagem 3D na estrutura dela.
- **Ressalva honesta:** consentimento não aparece nesta página (`consent_given` = 0 ocorrências), o que significa passo 1 mais curto — mas também que é preciso conferir no `/connect/dashboard` se o cadastro entrou.

## 12. Princess Bento — Connect, cargo Character Artist (Londres) — **PERSONAGEM com ressalva**

- **Formulário:** `https://princessbento.teamtailor.com/connect/candidates/new`
- **O que marcar:** departamento `Art` (`488901`), cargo **`Character Artist` (`1240636`)**. O menu tem ainda um departamento **`Character Layout` (`488906`)** com três cargos (`Character Layout Artist 1240655`, `Lead 1240653`, `Supervisor 1240654`).
- **Dedupe:** `sh automacao/dedupe-agora.sh "1240636" "Princess Bento"` → **zero ocorrências nos quatro arquivos. Casa inédita.**
- **Gancho:** o menu da casa nomeia `Character Artist` e um departamento inteiro de `Character Layout`.
- **RESSALVA GRAVE, medida em 12/09 e que fica escrita:** a Princess Bento é casa de **2D** — as vagas publicadas são `2D Rigged Animators`, `EOI - 2D Animation Directors`, `EOI - 2D Art Directors`. O cargo "Character Artist" existe no menu, mas o pipeline é 2D. Encaixe **baixo**; entra na faixa de personagem por honestidade de rótulo, e vai depois da Tactical Adventures.

## 13. Envar Studio — Connect, dep. 3D Art (Oslo)

- **Formulário:** `https://envarstudio.teamtailor.com/connect/candidates/new`
- **O que marcar:** departamento **`3D Art` (`395135`)** — o menu tem também `2D Art` (`395308`), `Animation` (`395313`), `Technical Art` (`395321`) e o cargo `3D Environment Artist` (`974955`).
- **País:** Noruega, Oslo
- **Dedupe:** `sh automacao/dedupe-agora.sh "395135" "Envar"` → o ID não aparece. A casa já tem **a vaga `8281404` Senior 3D Environment Artist ENVIADA e confirmada em 07/09** (recibo de Soledad Trejo). **O Connect é porta diferente e está livre.**
- **Gancho:** o próprio departamento `3D Art` no menu, e o histórico: a recrutadora já respondeu a candidatura anterior desta casa.

## 14. Black Kite Studios — Connect, dep. CG (Londres)

- **Formulário:** `https://blackkitestudios.teamtailor.com/connect/candidates/new`
- **O que marcar:** departamento **`CG` (`155713`)**
- **Dedupe:** `sh automacao/dedupe-agora.sh "155713" "Black Kite"` → ID inédito. A casa tem **envio por Teamtailor em 30/08** (recibo de Angus Edhouse) numa vaga anterior. Connect livre.
- **Gancho (literal, da página de vaga aberta da casa):** *"Black Kite is an independent creative studio offering world class visual effects and design."*

## 15. Territory Studio — Connect, dep. VFX (Londres)

- **Formulário:** `https://territorystudio.teamtailor.com/connect/candidates/new`
- **O que marcar:** departamento **`VFX` (`119793`)** (o outro é `Creative Advertising`, `119792`)
- **Dedupe:** `sh automacao/dedupe-agora.sh "119793" "Territory Studio"` → **zero em `enviados.csv`**, 1 ocorrência em `processados.csv` sem marca de envio. Livre.
- **Gancho:** Territory é a casa de UI de cinema (Blade Runner 2049, Guardiões) — o gancho honesto é o departamento `VFX` nomeado no menu; **não citar frase de anúncio, porque não há anúncio nesta rota**.

## 16. Untold Studios — Connect, dep. VFX (Londres / Los Angeles)

- **Formulário:** `https://untoldstdfg1324556.teamtailor.com/connect/candidates/new`
- **O que marcar:** departamento **`VFX` (`88810`)** (existem também `VFX Pipeline` `89440` e `VFX Production` `89439`)
- **Dedupe:** `sh automacao/dedupe-agora.sh "88810" "Untold"` → ID inédito; nenhuma marca de envio de Connect para a casa.
- **Observação de ordem:** é a **mesma casa da porta #7**. Se o Jhon A mandar as duas, manda primeiro a **vaga** (#7) e depois o Connect, nunca o contrário.

## 17. Raw Fury — Connect, cargo Freelancer - 3D Artist (Estocolmo)

- **Formulário:** `https://rawfury.teamtailor.com/connect/candidates/new`
- **O que marcar:** cargo **`Freelancer - 3D Artist` (`121776`)** (o vizinho é `Freelancer - 2D Artist`, `121777`)
- **Dedupe:** `sh automacao/dedupe-agora.sh "121776" "Raw Fury"` → **zero ocorrências em `enviados.csv`. Casa inédita como candidatura.**
- **Gancho:** o cargo de freelance 3D nomeado no menu da própria casa — e freelance dispensa visto, que é o gargalo da campanha.
- **Ressalva:** a Raw Fury é **publisher**, não estúdio: a arte 3D interna é pequena e o rótulo é de freelance.

## 18. Goodgame Studios — Connect, dep. Game Art (Hamburgo)
- **Formulário:** `https://goodgamestudios.teamtailor.com/connect/candidates/new` · **marcar `Game Art` (`309870`)**
- **Dedupe:** `sh automacao/dedupe-agora.sh "309870" "Goodgame"` → ID inédito; `enviados.csv` **0** para a casa. Livre.
- **Ressalva:** grupo **Stillfront**; o quadro é de jogo de navegador (Empire) e a vaga de arte aberta hoje é *AI Artist - Empire*. Encaixe médio-baixo, porta sem atrito.

## 19. New Moon Production — Connect, dep. Game Art (Hamburgo)
- **Formulário:** `https://newmoonproduction.teamtailor.com/connect/candidates/new` · **marcar `Game Art` (`325621`)**
- **Dedupe:** `sh automacao/dedupe-agora.sh "325621" "New Moon Production"` → **zero ocorrências. Casa inédita.**
- **Ressalva:** mesmo molde de quadro da Goodgame (grupo Stillfront), 17 departamentos e zero cargo listado.

## 20. OFM Studios — Connect, dep. Game Art
- **Formulário:** `https://ofmstudios.teamtailor.com/connect/candidates/new` · **marcar `Game Art` (`374882`)**
- **Dedupe:** `sh automacao/dedupe-agora.sh "374882" "OFM Studios"` → **zero em `enviados.csv`**, 1 linha de leitura em `processados.csv`. Livre.
- **Ressalva honesta:** o quadro tem **zero vaga aberta** (medido em 12/09). É cadastro puro.

## 21. Playa Games — Connect, dep. Game Art (Hamburgo)
- **Formulário:** `https://playagames.teamtailor.com/connect/candidates/new` · **marcar `Game Art` (`339731`)**
- **Dedupe:** `sh automacao/dedupe-agora.sh "339731" "Playa Games"` → ID inédito. **ATENÇÃO:** a casa **já recebeu candidatura por Teamtailor em 06/09** (Initiativbewerbung `4985632`, confirmada na tela) e uma carta fria no mesmo dia. O Connect é objeto diferente, mas é **terceira batida na mesma casa** — só mandar se a fila de cima secar.

## 22. Sandbox Interactive — Connect, dep. Game Art (Berlim)
- **Formulário:** `https://sandboxinteractive.teamtailor.com/connect/candidates/new` · **marcar `Game Art` (`359924`)**
- **Dedupe:** `sh automacao/dedupe-agora.sh "359924" "Sandbox Interactive"` → ID inédito; a casa tem a vaga `8094866` (Lead 3D Environment Artist) **enviada em 08/09**. Connect livre.
- **Gancho:** Albion Online é MMO de personagem estilizado com visual próprio.

## 23. Stillfront Group — Connect, dep. Game Art (Estocolmo)
- **Formulário:** `https://stillfrontgroup.teamtailor.com/connect/candidates/new` · **marcar `Game Art` (`305316`)**
- **Dedupe:** `sh automacao/dedupe-agora.sh "305316" "Stillfront"` → ID inédito. A casa tem a espontânea da **Twin Harbour (`6958619`) enviada em 06/09** por este mesmo quadro-guarda-chuva.
- **Ressalva honesta:** é **holding**, não estúdio: o cadastro cai num pool que cobre 20+ estúdios do grupo. Vale como rede, não como vaga.

## 24. Swift Games — Connect, dep. Art (Suécia)
- **Formulário:** `https://swiftgames.teamtailor.com/connect/candidates/new` · **marcar `Art` (`269483`)**; o único cargo listado é `2D Artist` (`708468`), que **não** é dele — marcar o departamento e dizer a disciplina no campo livre.
- **Dedupe:** `sh automacao/dedupe-agora.sh "269483" "Swift Games"` → **zero em `enviados.csv`**; 4 linhas de leitura em `processados.csv`. Livre.

## 25. Triband — Connect (Copenhague)
- **Formulário:** `https://triband.teamtailor.com/connect/candidates/new` · departamentos: `Game Production`, `Internship and Graduate Program`, `Marketing`, `Non-Production` → **marcar `Game Production`** (não há rótulo de arte)
- **Dedupe:** a casa tem **carta fria para `hello@triband.net` em 06/09**; **nenhuma candidatura por portal**. Connect livre.
- **Gancho:** WHAT THE GOLF? é humor com personagem estilizado — o encaixe de estilo é bom; o rótulo de departamento é que é genérico.

## 26. TapNation — Connect (Paris)
- **Formulário:** `https://tapnation.teamtailor.com/connect/candidates/new` · departamentos: `Business Support`, `Monetization & UA`, `Product`, `Tech`, `WEB 3.0` → **marcar `Product`** e dizer a disciplina no campo livre (não há rótulo de arte)
- **Dedupe:** 1 linha de leitura em `processados.csv`, **zero em `enviados.csv`**. Livre.
- **Ressalva honesta:** mobile hipercasual; personagem 3D não é o produto. Fecha a faixa por isso.

---
# FAIXA 4 — PINPOINT, BANCO DE TALENTOS

> **Por que a lane é confiável:** em 10/09 saíram **dez** candidaturas por esta rota, todas com
> a tela `/themes/<n>/register-your-interest/thanks` registrada em `enviados.csv`. **Zero
> captcha** no HTML servido. Campos (medidos hoje, iguais nas duas):
> `#job_seeker_form_job_seeker_first_name`, `_last_name`, `_email`, `#phone-input`,
> `#job_seeker_form_linkedin_url`, `#personal-summary`, `input[type=file]` para o CV,
> `#job_seeker_form_process_information` (consentimento) e os multisseletores
> `job_seeker_form[interest_options][location_ids][]` e `[department_ids][]`.
> **A armadilha da lane, e ela é infalsificável:** quadro de demonstração traz `Locations` =
> `Belfast, London, New York, Paris, Sydney, Washington`, `Departments` = `Engineering, Finance,
> Marketing, Operations, Product, Sales` e `Divisions` = **`ACME`/`Hooli`**. Se aparecer isso, é
> conta de teste e a candidatura cai num lugar que ninguém abre. **A Moonbug caiu nisso hoje** e
> está na seção de descarte.
> **Script:** `pin_interesse.js` (em `automacao/`, não copiado para a caixa nova — copie antes de rodar).

## 27. ★ Hyper Hippo Entertainment — Register Your Interest (Remote Canada)

- **Formulário:** `https://hyperhippo.pinpointhq.com/register-your-interest/new`
- **País/cidade:** Canadá — **`Remote (Canada)`** é a única localidade oferecida (sede em Kelowna, BC)
- **Departamentos REAIS (17, quadro configurado de verdade):** `Art`, `Communications`, `Data`, `Engineering`, `Executive`, `Finance & Accounting`, `Game Design`, `Global Platforms & Player Experience (PX)`, `Lab`, `Marketing & Content`, `P&C (Test)`, `People & Culture`, `Player Experience`, `Production (Games)`, `QA`, `UI / UX`, `Workplace & Technology` → **marcar `Art`**
- **Pretensão (campo livre, se pedir):** CAD 80.000/ano (casa média, regra de 04/09) + abertura padrão
- **Régua de veto:** nenhum dos 22 termos casa na página. Sem veto escrito.
- **Dedupe:** `sh automacao/dedupe-agora.sh "hyperhippo" "Hyper Hippo"` → **as dez rotas Pinpoint enviadas em 10/09 são `flixinteractive`, `gameplaygalaxy`, `ingenuitystudios`, `magnopus`, `outpost-vfx`, `pipeworks`, `playground-games`, `rocksteady`, `singularity6` e `wushustudios`. A `hyperhippo` NÃO está entre elas** — a fila de 10/09 listava 11 casas e só 10 saíram. A única ocorrência da casa no painel é a **parede de JavaScript de 08/09**, sem envio. **ROTA LIVRE, e é a sobra da fila daquele dia.**
- **Pergunta do estúdio (uma só, slot 0, `short_text`, não obrigatória, id `237602`):** *"What are your pronouns?"* → `He/Him`
- **Comando:** `cp automacao/pin_interesse.js /home/user/apply/ && cd /home/user/apply && VINI_TEL='<código do país + número>' sh hb_run.sh pin_interesse.js hyperhippo`
- **Gancho:** o quadro tem `Art`, `Game Design` e `Production (Games)` reais e a única localidade é **remoto no Canadá** — remoto no Canadá é exatamente o alvo da regra 4 do Vini (Vancouver/BC com patrocínio), sem custo de visto imediato.

## 28. Sun Creature — Register Your Interest (Copenhague)

- **Formulário:** `https://suncreature.pinpointhq.com/register-your-interest/new`
- **País/cidade:** Dinamarca, Copenhague (`Locations` = `Copenhagen`, **real**)
- **Departamentos:** `Engineering, Finance, Marketing, Operations, Product, Sales` → **é o conjunto de fábrica**; quadro meio configurado (localidade real, departamentos de demonstração). **Não há `ACME`/`Hooli`**, então não é conta de teste: é o mesmo caso da Playground Games e da Outpost VFX, que foram enviadas em 10/09. **Marcar `Product`** e dizer a disciplina no `#personal-summary`.
- **Pretensão:** EUR 45.000/ano + abertura padrão
- **Régua de veto:** zero acertos na página.
- **Dedupe:** `sh automacao/dedupe-agora.sh "suncreature" "Sun Creature"` → duas ocorrências em `enviados.csv` e as duas são **carta fria** (`contact@suncreature.com` em 26/08 e 2ª via para `jobs@suncreature.com` em 02/09). **Nenhuma marca de envio por portal. Rota inédita.**
- **Perguntas do estúdio:** nenhuma (zero slots).
- **Comando:** `cd /home/user/apply && VINI_TEL='<...>' sh hb_run.sh pin_interesse.js suncreature`
- **Gancho:** Sun Creature é animação **2D/3D estilizada** de autor (Le Cœur des Lucioles, trailers de Riot) — o `#personal-summary` é o lugar de dizer, com a verdade, que a disciplina é personagem 3D estilizado com grooming.
- **Ressalva honesta:** o quadro **não tem departamento de arte**, então o cadastro depende de o texto ser lido. Encaixe de estilo alto, precisão de fila baixa.

---

# FAIXA 5 — GREENHOUSE

> **Como a lane se comporta:** o HTML do formulário traz `RECAPTCHA_INVISIBLE_KEY` e
> `recaptcha.net/recaptcha/enterprise.js` — é **reCAPTCHA invisível/pontuação de sessão**, não
> caixa de desafio. Pela medida da campanha, **vale tentar**: o Greenhouse manda um **código de
> segurança por email** e o código só funciona com a sessão viva (rode em segundo plano, espere
> `needcode_<slug>.txt`, leia o código no Gmail e escreva `code_<slug>.txt` em até seis minutos).

## 29. Eleventh Hour Games — Senior Environment Artist (remoto)

- **Formulário:** `https://job-boards.greenhouse.io/eleventhhourgames/jobs/8501085002`
- **Requisição:** `8501085002` · **Casa:** Eleventh Hour Games (Last Epoch), quadro do grupo **KRAFTON Americas**
- **País/cidade:** **Remoto**, com núcleo de horário declarado (10h–16h Central Time). Ele está em UTC-3, o que cai **dentro** da janela.
- **Faixa publicada:** nenhuma no anúncio. **Pretensão:** USD 100.000/ano (casa grande, regra de 04/09) + abertura padrão — o formulário tem campo **`Desired Salary`**.
- **Régua de veto:** 35.265 caracteres lidos (API com `content=true`). Três acertos, **os três falsos positivos**: `Polish` casa dentro de *"...through final in-engine implementation and **polish**"*; `authoriz` casa no bloco de EEO sobre veteranos (*"...for which a campaign badge has been **authorized** under the laws administered by the Department of Defense"*). **Nenhum veto escrito de residência, autorização ou idioma.**
- **Dedupe:** `sh automacao/dedupe-agora.sh "8501085002" "Eleventh Hour"` → `enviados.csv` 0, painel 0, `FILA-DO-VINI.md` 0; 1 linha de leitura em `processados.csv`. **Requisição inédita.**
- **Perguntas customizadas (22, lidas por `?questions=true`; as que exigem decisão):**
  | pergunta | resposta |
  |---|---|
  | *"Are you able to be fully available during Eleventh Hours Games' core hours (10:00AM - 4:00PM Central Time)?"* | **Yes** (UTC-3 cobre 12h–18h locais) |
  | *"Do you currently have a remote work setup capable of fulfilling the needs of this role?"* | **Yes** |
  | *"Do you have experience working in a fully remote studio environment?"* | **Yes** |
  | *"What environments or areas have you fully owned from concept to final implementation? Please describe your process and responsibilities."* | texto com os mundos do Wingfeather Saga e do trabalho na E-Line |
  | *"Describe your experience working directly in engine..."* | Unreal/Unity: import, materiais, otimização |
  | *"How do you approach balancing visual quality with performance constraints? Provide a concrete example."* | exemplo real de orçamento de polígono/textura |
  | *"What types of environments or worlds are you most experienced building (open worlds, linear levels, stylized, realistic, etc)?"* | **stylized** |
  | *"Do you have experience creating or maintaining material/shader systems?"* | Yes, Substance + shaders de personagem |
  | *"Now a fun one! What game have you put the highest amount of playtime hours into throughout your life? More importantly, why do you think that is?"* | resposta humana, curta |
  | `Desired Salary` | `USD 100,000 — open to aligning with your band for the role` |
  Campos base: First/Last, Preferred First Name, Email, Phone, Resume/CV, Cover Letter, LinkedIn, Website, `[Privacy Policy]`.
- **Comando:** `cd /home/user/apply && node apply-greenhouse.js "https://job-boards.greenhouse.io/eleventhhourgames/jobs/8501085002" eleventhhour ans_eleventhhour.json` (sem `--submit` primeiro; depois com, deixando a sessão viva para o código por email)
- **Gancho:** *"As Senior Environment Artist, you will own environment creation from early concept and blockout through final in-engine implementation and polish."*
- **Ressalva honesta:** é **ambiente**, não personagem, e é ARPG isométrico. Entra porque é a única requisição aberta e inédita numa lane que passa, é 100% remota e o quadro é da KRAFTON (a mesma dona da PUBG e da Unknown Worlds).

---

# FAIXA 6 — JAZZHR (parede de reCAPTCHA v2 medida; dossiê pronto para a mão)

> **A medida, e ela é de clique, não de suposição:** em 12/09 a campanha preencheu a
> `Modeling Artists` da Stellar até o fim e clicou em *Submit Application*: **zero POST para o
> host da casa**, com o `anchor` do reCAPTCHA em `size=normal` e o `bframe` presente, rótulo
> **"Human Check*"**. Hoje confirmei que **as cinco páginas de candidatura JazzHR que abri
> trazem `div.g-recaptcha` + `recaptcha/api.js` sem `render=`**, que é a assinatura do **v2 de
> caixa**. Não se burla. Estas portas são dossiê para a mão dele — e, pela regra de 16/09, só
> **Vancouver** justifica a mão: #30, #32 e #33.
> **Campos, iguais nas cinco:** `First Name`, `Last Name`, `Email Address`, `Phone`, `Address`,
> `Resume`, `Cover Letter` + as perguntas de cada casa.

## 30. Certain Affinity — Advanced Material Artist (Grande Vancouver, BC)

- **Formulário:** `https://certainaffinityinc.applytojob.com/apply/AgAMjfmeKe/Advanced-Material-Artist`
- **Requisição:** `AgAMjfmeKe` · Full Time, Mid Level · **Canadá, Grande Vancouver (BC)**
- **Pretensão:** CAD 95.000/ano (casa grande de AAA, regra de 04/09) + abertura padrão
- **Régua de veto:** 4.042 caracteres → **zero acertos dos 22 termos.** Sem veto escrito (nem residência, nem autorização).
- **Dedupe:** `sh automacao/dedupe-agora.sh "AgAMjfmeKe" "Certain Affinity"` → `enviados.csv` **0**. O painel registra a **`Senior Material Artist`** da mesma casa como *"preenchida por inteiro e testada — o reCAPTCHA abriu desafio de imagem"*, **sem envio**. O cargo hoje mudou de nome (**Advanced** Material Artist) e o código da requisição é o mesmo `AgAMjfmeKe` do registro antigo: **é a mesma porta, e ela nunca foi enviada.**
- **Gancho:** *"Would you like to work on some of the greatest franchises in gaming history? What about working on our new original IP?"* — e o anúncio diz *"We are also excited to be the latest recipient of the Canadian Studio of the Year award"*.
- **Por que é a primeira da faixa:** material/surfacing é meia-irmã da disciplina dele (textura e shading de personagem), e é **Vancouver**, que é a frente de prioridade 4 do Vini.

## 31. Certain Affinity — Advanced Material Artist (Grande Toronto, ON)

- **Formulário:** `https://certainaffinityinc.applytojob.com/apply/eJTHIpzicy/Advanced-Material-Artist`
- **Requisição:** `eJTHIpzicy` — **é a segunda requisição da MESMA vaga**, publicada para Toronto. O painel já registrava as duas cidades.
- **Régua, dedupe, pretensão e gancho:** iguais aos da #30 (CAD 95.000).
- **Ressalva:** mandar as duas é legítimo (requisições distintas), mas se o Jhon A quiser só uma, **Vancouver primeiro**.

## 32. Zoic Studios — BC General Application (Vancouver)

- **Formulário:** `https://zoicstudios.applytojob.com/apply/va0rRqNxqm/BC-General-Application`
- **Régua de veto:** 4.288 caracteres. O acerto de `based in` é *"Zoic Studios BC Recruitment Team This position is based in Vancouver."* → **falso positivo de local**, não veto (não há "must reside" nesta porta, ao contrário da vaga de personagem da mesma casa, que caiu na régua e está na seção final). Os outros acertos são **rótulos de pergunta do formulário**, não requisito.
- **Dedupe:** `sh automacao/dedupe-agora.sh "va0rRqNxqm" "Zoic"` → `enviados.csv` tem **duas cartas frias** (jweitzell@ em 05/09, smelchiorre@ em 07/09) e **nenhum envio por portal**. Livre.
- **Perguntas (as que decidem):** *"What's your citizenship / employment eligibility?"* → **`Non-citizen seeking work authorization`**; *"Eligible to work in Canada?"* → **`I require a Work Permit.`**; *"Have you been a resident in BC since December 31st, 2025?"* → **No** (e escrever a data real de mudança: não houve); *"What is your desired hourly rate?"* → CAD equivalente a CAD 95.000/ano; *"In 150 characters or fewer, tell us what makes you unique..."* → frase humana, com o crédito do Wingfeather Saga.
- **Gancho:** *"Zoic Studios is a Visual Effects company that specializes in high end visual effects for television, film, and advertising. Our mantra is Visual Evolution."*

## 33. Next Level Games (Nintendo) — General Application (Vancouver)

- **Formulário:** `https://nextlevelgames.applytojob.com/apply/YyYQvToJW1/General-Application`
- **Régua de veto:** 3.719 caracteres. Único acerto: *"Are you authorized to work in Canada?*"* → é **pergunta obrigatória do formulário**, não veto escrito. Responder **No**, com a verdade, e marcar patrocínio necessário no campo livre.
- **Dedupe:** `sh automacao/dedupe-agora.sh "YyYQvToJW1" "Next Level Games"` → `enviados.csv` tem **uma carta fria** (`careers@nextlevelgames.com`, 01/09). **Nenhum envio por portal.** Livre.
- **Pretensão:** CAD 95.000/ano (estúdio da Nintendo) + abertura
- **Gancho:** o quadro deles é curto e a porta é a espontânea — o gancho honesto é o catálogo (Luigi's Mansion 3, Mario Strikers), personagem estilizado de cabo a rabo. **Não há frase de anúncio para citar nesta porta.**

## 34. Zoic Studios — U.S. General Application (Culver City)

- **Formulário:** `https://zoicstudios.applytojob.com/apply/DoIaRXmt0d/US-General-Application`
- **Dedupe:** mesmas duas cartas frias da #32; sem envio por portal.
- **Perguntas:** o bloco de elegibilidade é o americano — responder **No** para autorização nos EUA e **Yes** para patrocínio.
- **Pretensão:** USD 100.000/ano + abertura. **Ressalva:** a casa marca as vagas de BC como `Contracted`; a porta americana é a de Culver City.

## 35. Obsidian Entertainment — General Application (Irvine, CA)

- **Formulário:** `https://obsidian.applytojob.com/apply/21Ud1IGKcj/General-Application`
- **Régua de veto:** 3.164 caracteres → **zero acertos.**
- **Dedupe:** `sh automacao/dedupe-agora.sh "21Ud1IGKcj" "Obsidian"` → `enviados.csv` **0**. O painel registra a revalidação de 05/09: *"a General Application segue aberta no ATS proprio (obsidian.applytojob.com), marcada Remote e Full Time"*, **sem envio**. Livre.
- **Pretensão:** USD 100.000/ano + abertura
- **Ressalva:** é Xbox Game Studios; o quadro público de arte da casa hoje não tem personagem, e a espontânea é a única porta.

## 36. Outplay Entertainment — Speculative Applications (Dundee, Reino Unido)

- **Formulário:** `https://outplayentertainment.applytojob.com/apply/CS3Wh2/Speculative-Applications`
- **Dedupe:** `sh automacao/dedupe-agora.sh "CS3Wh2" "Outplay"` → `enviados.csv` **0**; o painel tem a porta como *"A MAO em 07/09 ... por reCAPTCHA v2 de caixa; formulario mapeado campo a campo"*, **sem envio**. Livre, e o mapa de campos já existe de 07/09.
- **Pretensão:** GBP 42.000/ano (casa média, Reino Unido) + abertura
- **Ressalva honesta do próprio painel:** *"Encaixe medio-baixo, e mobile match-3"*. Fecha a faixa.

---

# FAIXA 7 — RECRUITEE

## 37. Framestore — 3D Modeller, contrato curto (Montréal) — **PERSONAGEM (modelagem)**

- **Formulário:** `https://framestore.recruitee.com/o/modeleurse-3d-3d-modeller-contrat-court-terme`
- **Requisição:** `2120070` · **Local:** Canadá, Montréal (Québec) · **contrato curto**
- **Faixa publicada:** nenhuma. **Pretensão:** CAD 95.000/ano equivalente, ou taxa semanal proporcional + abertura padrão
- **Régua de veto:** anúncio lido pela API (`/api/offers/2120070`): **zero veto escrito**. O que existe são **perguntas** de elegibilidade, que se respondem com a verdade.
- **Dedupe:** `sh automacao/dedupe-agora.sh "2120070" "Framestore"` → `enviados.csv` 0, `FILA-DO-VINI.md` 0; 3 linhas de leitura em `processados.csv` e 2 no painel, **nenhuma com marca de envio**. Livre.
- **Perguntas customizadas (nove, com id, lidas da API pública):**
  | id | tipo | pergunta | resposta |
  |---|---|---|---|
  | `3148831` | string | Portfolio link | `https://www.artstation.com/viniciuscavalcanti` |
  | `3148832` | string | Portfolio password | (vazio) |
  | `3148839` | single_choice | Years of experience in 3D modeling | 10+ (escolher a faixa mais alta oferecida) |
  | `3148833` | string | Availability date | `Immediately / 30 days notice` |
  | `3148834` | string | Current Location | `Olinda, Pernambuco, Brazil` |
  | `3148835` | string | Citizenship | `Brazilian` |
  | `3148836` | **boolean** | *"Will you need visa sponsorship?"* | **Yes** (a verdade) |
  | `3148837` | string | Desired salary/rate | CAD, com a abertura padrão |
  | `3148838` | single_choice | What are your pronouns? | `He/Him` |
- **Script e comando:** `cd /home/user/apply && VINI_TEL='<...>' sh hb_run.sh apply_recruitee5.js ans_framestore.json framestore` (o `ans.json` usa `texto` por nome de campo, `radios` por id de pergunta e `cover: true`)
- **Gancho:** *"Modellers are responsible for the production of highly accurate and efficient CG models for use in high-end visual effects films"* e *"Modellers work closely with Texture Artists in order to produce models and UVs that meet the specific requirements of a VFX pipeline"*.
- **PAREDE ESPERADA, medida em 06/09 nesta mesma casa:** o **hCaptcha de imagem só aparece DEPOIS do clique em Send**. Até lá o formulário aceita tudo. Preencher, tirar o dossiê e, se o hCaptcha abrir, **não insistir**: vira item de mão. E há a ressalva de formato: **contrato curto**, que contraria a preferência dele por vaga fixa.

---

# FAIXA 8 — WORKABLE

> **Estado da lane, medido hoje:** a **leitura** por `https://jobs.workable.com/api/v1/jobs?query=...`
> **funcionou** (282 resultados para "character artist"), mas o **envio** continua sendo o
> problema conhecido: Cloudflare **Turnstile que só aparece depois do clique em enviar** e o
> estrangulamento de IP (`error code: 1015`) no `apply.workable.com`. Trate como parede até
> alguém medir o contrário. Estão aqui porque são **as três únicas vagas de personagem/textura
> em escopo que a varredura global achou hoje** e porque o dossiê serve tanto para a mão quanto
> para uma carta à casa.

## 38. Side (PTW) — 3D Character Artist, Talent Pool (EU), Londres — **PERSONAGEM**
- **Anúncio:** `https://jobs.workable.com/view/fJyhdFCoapwWKCvpGartD5/3d-character-artist---talent-pool-(eu)-in-london-at-side` · **id** `77511296-932a-4f38-ae1f-0e088c7109ea`
- **Régua de veto:** corpo lido pela API → **zero acertos dos 22 termos**. O que há é aviso de idioma de **currículo**: *"Only resumes submitted in English will be considered"* → falso positivo (não é exigência de falar outra língua), e o CV dele já é em inglês.
- **Dedupe:** `sh automacao/dedupe-agora.sh "77511296" "Side"` → zero por ID. A casa aparece no painel como grupo (PTW/Side), **sem envio para esta requisição**.
- **Pretensão:** GBP 50.000/ano (casa grande, Reino Unido) + abertura
- **Gancho:** *"Please note, this listing is not for an immediate open position but for our Talent Pool for Co-Development Roles."* — é banco de talentos declarado, o que baixa o custo de uma candidatura honesta.

## 39. Side (PTW) — Senior Texture Artist (Toronto, híbrido) — **PERSONAGEM (textura)**
- **Anúncio:** `https://jobs.workable.com/view/c6VkX4b2KPumikGpAnF75s/hybrid-artiste-de-texture-senior-%7C-senior-texture-artist-in-toronto-at-side` · **id** `59e81e55-412b-4f48-ac69-0e5a3fbd1e42`
- **Régua de veto:** **zero acertos**. O anúncio é **bilíngue** (francês primeiro, inglês depois) e **não exige francês em nenhuma frase** — o que derrubaria seria uma exigência escrita, e ela não existe.
- **Contrato:** *"Contrat: 6+ mois"*, híbrido, Montréal **ou** Toronto.
- **Pretensão:** CAD 95.000/ano equivalente + abertura
- **Gancho:** *"Chez Side, nous collaborons avec certains des principaux développeurs de jeux au monde pour résoudre des défis techniques complexes"* (o anúncio traz a versão inglesa logo abaixo).

## 40. Side (PTW) — Senior Texture Artist (Montréal, híbrido) — **PERSONAGEM (textura)**
- **Anúncio:** `https://jobs.workable.com/view/9yuW35zXXRhYX4wgDGcVSQ/hybrid-artiste-de-texture-senior-%7C-senior-texture-artist-in-montreal-at-side` · **id** `4552bd5b-f2d5-44b4-9c87-7ce06167b010`
- **É a segunda cidade da MESMA vaga** (o corpo diz *"Lieu : Montréal, Québec ou Toronto, Ontario"*). **Mandar UMA das duas**, não as duas: é o caso exato da regra 18 (mesma requisição em dois locais), e a Rebellion já custou uma batida repetida assim.
- **Régua, pretensão e gancho:** iguais aos da #39.

---
# O QUE CAIU NA RÉGUA DE VETO — com a frase inteira, e a classificação

A régua é a do brief: `authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`,
`days a week`, `citizen`, `resident`, `right to work`, `only from`, `based in`,
`French/français`, `Polish`, `German/Deutsch`, `Swedish`, `Danish`, `Dutch`, `Spanish`,
`Italian`. **Só veto ESCRITO desqualifica**; rótulo de pergunta de formulário e frase de
benefício não desqualificam, e por isso a classificação vem junto.

| Porta | Frase inteira, literal | Classificação |
|---|---|---|
| **Zoic Studios — BC, 3D Character Modeler, Senior** (Vancouver, JazzHR) | *"3D Senior Character Modeler This position is based in Vancouver. **All applicants must reside in British Columbia.**"* | **VETO ESCRITO de residência.** É a melhor vaga de personagem achada hoje e ela morre aqui: ele não reside na BC. A General Application da mesma casa (#32) **não** tem essa frase e continua aberta. |
| **Stellar Creative Lab — Modeling Artists (Mid & Senior)** (Vancouver, JazzHR) | *"**Eligibility: Legally eligible to work in British Columbia, Canada.**"* e *"All qualified candidates are encouraged to apply, though priority will be given to BC Residents, Canadians and Canadian Permanent Residents."* | **VETO ESCRITO de elegibilidade** na primeira frase; a segunda é só preferência. Some-se a parede de reCAPTCHA v2 medida com clique em 12/09. Dói: é série premium para a **Marvel Animation**, com `characters` no primeiro parágrafo. |
| **Stellar Creative Lab — Surfacing Artists (Mid & Senior)** (Vancouver, JazzHR) | *"**Eligibility: Legally eligible to work in British Columbia, Canada.**"* | **VETO ESCRITO**, mesmo texto-base da irmã. |
| **Stirling Animation Studios — Character Modeling and Surfacing Artists** (Escócia, BambooHR `77`) | *"**Artists must be based regionally within the UK (outside the London region)**"* | **VETO ESCRITO de residência.** A disciplina é literal (character, model, texture, Substance), e é a segunda vez que a campanha confirma este veto (já estava escrito em 14/09). |
| **Image Engine — General Application - Assets (Modeling/Texturing/LookDev/Grooming)** (Vancouver, BambooHR `21`) | o corpo de 490 caracteres traz *"**Candidates are required to be legally eligible to work in Canada**"* (registro de 14/09, reconferido hoje pela API `/careers/21/detail`: departamento `Speculative Application`, `datePosted` 2022-10-04) | **VETO ESCRITO.** Tem a pilha inteira dele no título, grooming incluído, e cai. |
| **weltenbauer. Software Entwicklung — Environment Artist w/m/d** (Wiesbaden ou Remoto, Personio `2677880`) | *"**Gutes Deutsch und Englisch in Wort und Schrift**"* | **VETO ESCRITO de idioma** (alemão). Mesma família do francês da TAT e do polonês da Anshar. |
| **weltenbauer. — Tech Artist Character Animation w/m/d** (Wiesbaden ou Remoto, Personio `2692704`) | *"**Gute Deutsch- und Englischkenntnisse in Wort und Schrift**"* | **VETO ESCRITO de idioma.** |
| Chimera Entertainment — bloco de estágio dentro da espontânea (Munique, Personio `150955`) | *"The internship must be mandatory and part of your degree program (Pflichtpraktikum as defined by your university / study regulations)"* e *"On-site work in our Munich office (remote work is not possible)"* | **NÃO derruba a porta:** o bloco vale para **estágio**. A espontânea sênior continua na fila como #3, e o registro fica para ninguém confundir o parágrafo com veto geral. |

**Falsos positivos que a régua pegou hoje e que NÃO desqualificam nada** (estão escritos aqui
porque cada um deles já custou uma porta descartada por engano em rodadas passadas):
*"A modern, centrally located office in Frankfurt, Germany (near Messe)"* e *"Free language
courses"* (Deck13); *"...studio based in the heart of Munich"* (Chimera); *"...through final
in-engine implementation and **polish**"* (Eleventh Hour, o termo `Polish`); *"...for which a
campaign badge has been **authorized** under the laws administered by the Department of
Defense"* (bloco de EEO, Eleventh Hour); *"if you are based in the EU"* / *"If you are based in
the UK, you can lodge a complaint with the Information Commissioner's Office"* (política de
privacidade, **todas** as 146 páginas de Teamtailor Connect); *"Only resumes submitted in
English will be considered"* (Side); *"This position is based in Vancouver"* na General
Application da Zoic (local, e sem a frase de residência obrigatória).

---

# O QUE CAIU NO DEDUPE — 59 requisições, por ID

Todas foram testadas com `sh automacao/dedupe-agora.sh "<ID>" "<Casa>"` e com leitura das
quatro fontes (`enviados.csv`, `automacao/processados.csv`, `docs/index.html`,
`automacao/FILA-DO-VINI.md`), procurando **marca de envio** junto do ID (`confirmation`,
`ENVIADA`, `portal-aplicado`, `/thanks`, `jobTasks/completed`, `recibo`, `recusada`).

**Personagem / disciplina literal (21):**
`8190501` Fatshark Character Artist (enviada e confirmada) · `8311973` Tactical Adventures
Lead 3D Character Artist (enviada e confirmada; a mesma requisição aparece também no quadro
`keplerinteractive`, que é o publisher — **um ID, dois quadros**) · `8281687` Airship Character
Artist e `8281721` Airship Groom Artist (enviadas em 09/09) · `8517790002` e `8520212002`
Bluehole (enviadas e confirmadas) · `8725151002` Loonshot 3D Character Artist (**recusada**) ·
`8163170` Riot Principal 3D Character Artist (enviada e confirmada) · `7888172003` e `7888170003`
Cloud Chamber Lead Character Artist (enviadas, **recusadas**) · `7888173003` e `7888174003` 2K
Lead Character Artist (espelho das duas de cima, mesmas requisições no quadro do publisher) ·
`7835808003` 2K Senior Character Artist Burnaby (enviada) · `4363749003` Imageworks Experienced
Modeler (enviada **duas vezes**, 02/09 e 07/09) · `4363748003` Modeler · `4363798003` Texture
Artist · `4363799003` Experienced Texture Artist · `6659179003` Look Development Artist ·
`7529417003` Senior Look Development Montréal (todas Imageworks, todas enviadas) · `8161671`
Wargaming 3D Character Artist (enviada em 06/09 e **recusada em 10/09** com crítica escrita ao
portfólio) · `5207518007` Mob Entertainment Senior Character Artist (enviada) · `4318250009`
Hasbro Lead Character Artist Canadá (enviada, **recusada**) · `5236256007` Absurd Ventures
Character Art Lead (enviada e confirmada) · `4337820009` Sway Box CG Modeler (enviada) e
`4337866009` Senior CG Generalist/Modeler (**recusada**) · `5097897007` High Dive Senior Modeler
(enviada e confirmada).

**Arte adjacente e espontâneas (38):** `8517791002` Bluehole 3D Environment · `8651145002`
Loonshot 3D Environment Modeler · `5195729007` e `5233607007` Mob (Environment, Hard Surface) ·
`6020680004` e `6020682004` Epic Modeling Outsource Lead (Cary e Montréal) · `5398064008`,
`5398038008`, `5398026008` Scopely 3D Artist Barcelona (as três) · `8281404` Envar Senior 3D
Environment Artist · `8220733` Triband Senior Game Artist · `8131050` Ankama Artiste 3D ·
`8094866` Sandbox/Stillfront Lead 3D Environment · `8083591` Coffee Stain Art Director ·
`7964466` Embark Environment Artist · `7918450` CI Games Open Application · `7277761` Funday
Unsolicited Application · `6958619` Twin Harbour Unsolicited · `5744150` e `5739695` Bulkhead
Open Application (remoto e in-studio) · `5428747` PFX General Application · `3583177` Axolot
Open Application · `3257938` Stunlock Open Application · `2814432` Game Boost Open application ·
`1907255` HypeHype Open Application · `1344945` Lightheart Open Application · `7535230002`
Unknown Worlds General Application · `4352498005` Crystal Dynamics General Application ·
`8282003002` Tripwire General Application · `4052911009` NC America Open Applications ·
`4319957101` Tactile Games Open Applications · `2615138` KING Art Speculative Application ·
`2385017` Aesir Art Lead · mais as portas de BambooHR já resolvidas: **Offworld `199`** (3D
Character Artist, enviada à mão em 10/09 com recibo), **ICON Creative `136`**
(Intermediate Modeling/Texture, enviada em 31/08 com confirmação do ATS) e **Image Engine `28`**
(Look Development Senior, já trabalhada).

**Connect já cadastrado (64 slugs, por isso fora da faixa 3):** `10chambers`,
`airshipinteractive`, `anima`, `ankama`, `awaceb`, `axolotgamesab`, `beffio`, `bica`,
`bulkheadinteractive`, `capsulestudio`, `captureage`, `chopchop`, `cigames`,
`coffeestainstudios`, `creepyjar`, `delve`, `ember`, `erepublik`, `fabrique`, `facepunch`,
`fatshark`, `firefly`, `fully`*, `funcom`, `gameboost`, `gigglebug`*, `goals`, `goodbyekansas`,
`here`, `hero`, `ilogos`, `ilpvfx`, `ioi`, `juice`, `keplerinteractive`, `kindabrave`,
`lightheartentertainment`, `look`, `madbox`, `mind`, `mindark`, `mob`, `neongiant`, `once`,
`opusmajor`, `pfx`, `pixiongames`, `power`, `proxima`, `realtime`, `sharkmob`, `sloclap`,
`snowprintstudios`, `squeeze`, `starbreeze`, `starstable`, `stunlocksstudios`, `sybo`,
`thegang`, `tic`, `twinharbour`, `vinefx`, `vividgamessa`, `wetaworkshop`.
(*) `fully` e `gigglebug` aparecem aqui pelo **Connect**; a **vaga aberta** das duas continua
livre e está nas posições #9 e #6 desta fila — são objetos diferentes, e o dedupe foi feito por
ID de requisição, não por nome de casa.

**Pinpoint já enviado em 10/09 (10 rotas):** `flixinteractive`, `gameplaygalaxy`,
`ingenuitystudios`, `magnopus`, `outpost-vfx`, `pipeworks`, `playground-games`, `rocksteady`,
`singularity6`, `wushustudios` — cada uma com a tela `/themes/<n>/register-your-interest/thanks`
no `enviados.csv`.

---

# DESCARTES COM MOTIVO ESCRITO (para a próxima rodada não reabrir)

| Porta | Motivo, medido hoje |
|---|---|
| **Moonbug Entertainment** (Pinpoint) | **Conta de demonstração.** `Locations` = `Belfast, London, New York, Paris, Sydney, Washington`, `Departments` = `Engineering...Sales` e **`Divisions` = `ACME` e `Hooli`**. É a assinatura infalsificável do quadro de teste; candidatura ali cai em conta sem dono. |
| **FuturLab, Kaiko, Craftwork, Boxelware, House of Tales** (Personio) | **Quadro de demonstração do Personio, assinatura nova e vale registrar:** os cinco publicam **exatamente as mesmas três vagas** — `SEO Marketing Manager`, `Social Media (Werkstudent/Working Student)` e `Initiativbewerbung/General Application` — e o corpo dos anúncios é **Lorem ipsum** (*"Lorem ipsum dolor sit amet, consetetur sadipscing elitr..."*). É o irmão Personio do `ACME/Hooli` do Pinpoint. **Regra que fica: antes de enfileirar espontânea de Personio, leia o corpo; se for Lorem ipsum e a casa tiver SEO Marketing Manager + Social Media Werkstudent ao lado, é conta de teste.** |
| **The Logic Factory** (Personio, 3 portas: NL `1233168`, UK `1702359`, USA `1702380`) | **Fora do setor.** *"The Logic Factory (TLF) is a global software company that helps customers make lasting performance improvements in their supply chain"*. Não é jogo nem animação. (A quarta porta da casa é `Open Application India`, fora do recorte geográfico.) |
| **`buf` no Personio** | **Falso amigo de token.** `buf.jobs.personio.com` é a **becker + flöge GmbH**, ótica e acústica alemã (*"Deine Fähigkeiten in der Augenoptik, Hörakustik oder Verwaltung"*), **não** a BUF Compagnie de VFX francesa. |
| **`squeeze` no Teamtailor** | **Falso amigo.** `squeeze.teamtailor.com` publica `Massage Therapist` em nove cidades norueguesas — não é a Squeeze Studio Animation do Québec. |
| **Waypoint** (Teamtailor `8125441`) | **Falso amigo.** É a **Waypoint Port Services**; a pergunta obrigatória do formulário é *"Do you have a valid work permit for the country you have selected?"* sobre uma lista de países de operação portuária. |
| **Equilibrium** (Teamtailor `7743496`) | **Fora do setor.** As áreas oferecidas são `BD / Sales`, `Marketing & Content`, `Design & UX`, `Finance & Legal`, `People & Operations`, `Community & Ecosystem`, `Research & Strategy` — nenhuma de arte — e uma pergunta obrigatória é *"Do you have experience working in blockchain / Web3 / crypto?"*. |
| **Bica** (Teamtailor `5804958`) | **Fora do setor.** *"We are actively building a robust talent pipeline to support a wide range of exciting projects with our clients across various industries, including retail, fintech, healthc..."* — consultoria de TI em Sófia. |
| **Ground Control, Dare, LEVEL, Lunar, Stardust, Chief, Avantis, hôma, Osome, Mill, Fuse, Above, Sunday, Genius, Kinetic, Life, Monster, Neat, Salt, Starship, Stim, Sweetspot, Tribes, Unfold, Yonder, ClickOutMedia, Lingokids, Curio, Fathom, Fortis, Graft, Infinity, Antagonist, Axis, Butter, Eclipse, Doktor, Level** (Teamtailor Connect, livres) | **Fora do setor**, um a um pelo menu de departamentos: paisagismo (`Arboriculture in Maintenance`), trading de energia, companhia aérea, banco, consultoria de RH, engenharia, serviços marítimos, varejo, contabilidade, clínica, etc. Ficam nomeados para ninguém gastar rodada nisso de novo. |
| **Black Kite — Freelance DMP / Concept Artists** (Teamtailor `8330454`) | **Fora da disciplina:** *"We're looking for fast, creative Digital Matte Painters (DMP) with strong Concept Art skills to join our roster for upcoming short-form commercial projects."* É pintura digital 2D. (O **Connect** da casa, dep. `CG`, continua na fila como #14.) |
| **Wargaming — CG Artist `8169078` e `8108499`** (Greenhouse) | **Fora do escopo geográfico:** Kyiv, Ucrânia, que não está no recorte (América do Norte, Europa ocidental/UE/UK/Irlanda/Nórdicos, Oceania, Coreia do Sul, Singapura). Registrado porque a requisição é **inédita no dedupe** e só cai pela geografia. |
| **Bluehole `8517835002`, Loonshot `8084569002` / `8085854002` / `8759149002`, Sharkmob `8378495`, Ankama `457385`** | **Fora da disciplina:** são `Character Concept Artist`, `Sr. Character Concept Artist`, `Pixel Artist (Character)`, `Senior Character Concept Artist` e `Character designer` — **personagem 2D**, e a regra 14 é explícita: candidatura de personagem 2D em casa grande morre na primeira tela e queima a porta da divisão. |
| **Framestore Creature FX (`2728197`, `2713294`, `2695789`, `513351`), Barnstorm Lead Creature Artist (`176`), DMFX Artiste CFX (`129`)** | **Fora da disciplina:** `creature` aqui é **simulação e rigging** (a contagem do corpo da Barnstorm dá `creature` 23, mas `rig` 25, `simulation` 20 e Houdini 10). A palavra "creature" no título é armadilha conhecida. |
| **IGG `289`** (BambooHR, 3D Character Artist, Vancouver) | **Veto de residência já registrado no painel em rodada anterior**; presencial integral. |
| **Streamline Studios `84` e `106`** (BambooHR, Lead/3D Character Artist) | **Fora do escopo geográfico:** Kuala Lumpur, Malásia. |
| **Rebellion Senior Character Artist (Oxford e Warwick)** (Workable) | **Mesma requisição que ele mandou em 30/08 e que o Talent Team RECUSOU em 01/09**, publicada em duas cidades. Bater de novo seria a segunda batida na mesma porta fechada. |
| **Keywords / Lakshya (7 vagas de personagem)** | **Fora do escopo geográfico:** Bengaluru, Pune, Gurugram, Ortigas/Pasig. A `Character Artist - Hair Specialist` remota para Canadá/EUA/UK **já está registrada no painel**. |
| **Chimera 3D Artist Generalist `2628421` e Senior Technical Artist `2628436`** | **Fora do escopo geográfico:** Cebu, Filipinas. (A espontânea de **Munique** da mesma casa é a porta #3.) |
| **Good Job Games (7 vagas de 3D Artist)** | **Fora do escopo geográfico:** Sarıyer, Istambul, Turquia. |
| **Vertigo `3D Character Artist`** (Workable) | **Fora do escopo:** Istambul. |
| **Longdue Games `3D Modeler (Junior)`** (Workable) | **Fora do escopo** (África do Sul) e **júnior**. |

---

# O QUE FICOU `NÃO CONFERIDO` — e resposta vazia não é zero

1. **Liquid Swords — Open Application `1851070`** (Estocolmo, Teamtailor). A página da vaga e o
   domínio próprio `careers.liquidswords.com` **não passam por esta rede**: `curl` devolve
   código `000` com erro de conexão segura, e o `jobs.json` do mesmo host responde **200** — ou
   seja, o quadro está vivo e o problema é o certificado no salto final, a mesma família do
   `careers.ilpvfx.com` (cert de `x.sni-498-default.ssl.fastly.net`). **Dedupe:** `enviados.csv`
   0, painel 0; uma linha de leitura em `processados.csv` e uma na `FILA-DO-VINI.md`, sem marca
   de envio. **Para o Jhon A:** o Chromium dos scripts sobe com `--ignore-certificate-errors`,
   então **é provável que abra no navegador** — tente e registre o resultado; não escreva "casa
   sem porta".
2. **Corpo dos anúncios da Side (#38, #39, #40) lido só pela API do `jobs.workable.com`.** O
   `apply.workable.com` continua devolvendo estrangulamento de IP, então **a tela real do
   formulário não foi vista hoje** — o que está escrito sobre Turnstile vem da medição de 06/09,
   não de hoje.
3. **Faixa salarial:** nenhuma das 40 portas publica faixa. Todas as pretensões desta fila são
   **derivadas da regra de 04/09**, não lidas de anúncio.
4. **O que NÃO foi varrido nesta rodada, e fica nomeado:** Workday (a ronda Disney/Netflix/Pixar
   é do maestro e da vigia horária), Ashby e Lever (parede conhecida de hCaptcha/reCAPTCHA),
   SmartRecruiters (DataDome), Dayforce, Oracle/Taleo, Jobvite, Homerun, Breezy e GoHire — o
   GoHire não foi sondado porque o slug dele tem sufixo de hash (`jobs.gohire.io/<nome>-<hash>`)
   e não se adivinha; a lista de slugs que a campanha tem é de três casas, nenhuma da disciplina.

---

# NOTA DE FERRAMENTA PARA O JHON A (medido hoje, e economiza rodada)

- **Não existe `apply_personio.js` nem modelo de Connect (`hampa_dep_fix2.js`, `beffio_ok.js`)
  em `/home/user/apply`.** A caixa reconstruída em 16/09 tem 19 scripts de candidatura, e os
  três que esta fila mais usa — Personio (faixa 1), Teamtailor Connect (faixa 3) e Pinpoint
  (faixa 4, `pin_interesse.js` mora em `automacao/`) — **não estão lá**. Copie de `automacao/`
  o que existir e conte com `preencher-formulario.js` no resto.
- **O `apply_own.js` de `automacao/` ainda aponta para a ponte morta `127.0.0.1:18080`** (linha
  13); a cópia de `/home/user/apply` já está corrigida para
  `process.env.APPLY_PROXY||process.env.HTTPS_PROXY`. **Rode sempre a cópia de
  `/home/user/apply`**, nunca a do repositório.
- **Ordem de consumo sugerida para bater a meta de hoje:** #4 (única vaga de personagem sem
  parede), depois #1–#3 e #5–#10 (espontâneas servidas, atrito mínimo), depois a faixa 3 inteira
  (Connect, duas etapas por casa — o gargalo é o magic link, então **peça um por vez**), depois
  #27 e #28 (Pinpoint, lane com dez envios confirmados), depois #29 (Greenhouse, precisa da
  sessão viva para o código por email). A faixa 6 em diante é dossiê para a mão dele, e pela
  regra de 16/09 só Vancouver (#30, #32, #33) justifica pedir clique.
