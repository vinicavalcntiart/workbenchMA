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
