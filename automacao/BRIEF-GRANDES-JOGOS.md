# Rotina dos estúdios grandes de JOGOS (diária)

Irmã da `BRIEF-GRANDES.md`, que cuida da animação. Mesma lógica e as mesmas regras:
vaga de personagem em estúdio grande dura poucos dias e as primeiras 48 horas valem mais que
todo o resto, então a rotina vigia um conjunto fixo de portais e aplica no mesmo dia.

**REGRA DO VINI, 02/09: em estúdio grande não se filtra senioridade.** Júnior, mid, sênior,
lead, principal e contrato temporário, tudo entra e tudo recebe candidatura. A regra de contrato
efetivo que vale no resto da campanha não se aplica aqui.

## Atalho importante: portais que cobrem vários estúdios

Aplicar num desses cobre uma família inteira, então comece por eles.

| Portal | Cobre |
|---|---|
| **Xbox Gaming Workday** (`xboxgaming.wd1.myworkdayjobs.com`) | Activision, Blizzard, King. O Vini já aplicou por aqui na Lead Character Artist de Overwatch, candidato C1562096, e o fluxo aceitou envio sem conta |
| **Microsoft careers** (`jobs.careers.microsoft.com`) | Xbox Game Studios: 343 e Halo Studios, The Coalition, Rare, Obsidian, inXile, Double Fine, Playground, Turn 10, Mojang, ZeniMax e Bethesda |
| **Sony / PlayStation** (`playstation.com/careers` e `sonyinteractive.wd1.myworkdayjobs.com`) | Naughty Dog, Insomniac, Santa Monica Studio, Sucker Punch, Guerrilla, Bend, Bluepoint, Firesprite, Housemarque |
| **EA** (`jobs.ea.com`) | EA, Respawn, BioWare, Motive, Criterion, Maxis. Conta já existe, senha no documento do Drive |
| **Ubisoft** (`ubisoft.com/careers`, SmartRecruiters) | Todos os estúdios Ubisoft. **Bloqueado por DataDome**, sempre à mão |
| **2K** (Greenhouse `2k`) | Cloud Chamber, Firaxis, Hangar 13, Visual Concepts, Small Axe |
| **Warner Bros. Games** (`careers.wbd.com`) | NetherRealm, Rocksteady, Monolith, Avalanche Software |

## Portais próprios que valem a visita diária

Greenhouse tem API pública, use-a para inventariar antes de abrir o navegador:
`https://boards-api.greenhouse.io/v1/boards/<token>/jobs`

| Estúdio | Token ou portal | Nota |
|---|---|---|
| **Riot Games** | Greenhouse `riotgames` | League e Valorant, estilizado puro, melhor encaixe estético da lista |
| **Epic Games** | Greenhouse `epicgames` | Fortnite, estilizado; ~162 requisições, quase sempre há arte |
| **Bungie** | Greenhouse `bungie` | costuma ter poucas vagas |
| **Roblox** | Greenhouse `roblox` | avatar e personagem estilizado |
| **Rockstar** | `rockstargames.com/careers` | realista, encaixe menor |
| **Valve** | `valvesoftware.com/en/jobs` | **reCAPTCHA de caixa**, sempre à mão |
| **Nintendo** | `careers.nintendo.com` | NoA e NoE |
| **Amazon Games** | `amazon.jobs` | |
| **Netflix Games** | Eightfold, mesma API da Netflix | ver BRIEF-GRANDES.md |
| **Krafton, Nexon, NCSoft, Pearl Abyss, Smilegate** | portais próprios | Coreia do Sul está no escopo |
| **Remedy, Housemarque, Supercell, Rovio** | portais próprios | Finlândia |
| **Larian** | Lever | **hCaptcha**, sempre à mão |
| **CD Projekt Red** | portal próprio | |
| **Embracer**: Coffee Stain, Deep Silver, Plaion | portais próprios | |
| **Sumo Digital, Jagex, Sharkmob, Frontier** | portais próprios | Reino Unido; Frontier tem captcha |

## O que fazer, em ordem

1. **Inventariar** por API onde houver (Greenhouse, Eightfold), e só então abrir o navegador.
   Busque por: character, modeler, modeling, visual development, look development, texture,
   groom, concept, 3D artist. Liste tudo, em qualquer nível.
2. **Aplicar imediatamente** onde não houver captcha de desafio, com CV e carta.
3. **Criar alerta de vaga por email** para contact@vinicavalcanti.art em todo portal que ofereça.
   Isso é permanente e vale mais que a varredura: feito uma vez, não repete.
4. **Registrar** e avisar por PushNotification quando aplicar em vaga de personagem.

## Regras de candidatura

As mesmas da campanha, em `automacao/respostas-formularios.md`. Os pontos que mais erram:

- Direito de trabalho nos EUA e Canadá: **No**. Precisa de patrocínio: **Yes**. Realocar: **Yes**.
- Salário atual: "Confidential under NDA", nunca um valor. Pretensão USD 46.000 por ano;
  no Canadá, CAD 75.000 a 79.999.
- E-Line Media é o emprego **atual**, sem data de fim. Se o parser preencher, apague.
- **Telefone com seletor de país separado**: escolha "BR (+55) Brazil" no seletor e escreva
  apenas os dígitos sem o código de país, sem espaço e sem hífen. Regra descoberta pelo Vini
  em 02/09 depois de duas falhas no Eightfold da Netflix. Se o campo for único, use o formato
  internacional. Os três formatos do número estão no documento privado do Drive
  "CAMPANHA - dados pessoais dos formulários": o repositório é público e o número não fica aqui.
- Captcha com desafio não se burla: registra "à mão" e segue.
- Nunca escrever nada que sugira hesitação em mudar de país.

## Registro

Igual ao da rotina de animação: array GRANDES para o estado do estúdio, PORTAIS para cada vaga,
`automacao/processados.csv` para cada candidatura, alerta e vaga vista, e uma entrada na
newsletter quando aplicar em vaga de personagem.
**Cuidado com a estrutura do arquivo**: o array STUDIOS termina em
`].map(([name,country,email,batch,delivery,stage])` e o PROSPECTOS vem logo depois. Ao inserir
linha no STUDIOS use esse `].map` como âncora, nunca o `];` seguinte.
