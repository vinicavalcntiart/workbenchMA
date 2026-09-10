# Bancos de talentos sem captcha — varredura de 10/09/2026, madrugada

Rodada de `curl` puro, **sem navegador** (o Chrome estava com outros agentes). Entrega uma
**fila pronta**, não envios: quem clica é a rodada seguinte.

O gatilho foi a Fenris Creations às 04h de hoje: a rota `/register-your-interest/new` do
Pinpoint fechou uma candidatura de personagem **sem captcha nenhum**. A pergunta desta rodada
foi uma só: **quantas outras portas dessas existem?**

---

## 1. PLACAR DE COBERTURA

| Família | Rota testada | Slugs sondados | Quadros que existem | Rota espontânea respondendo 200 |
|---|---|---|---|---|
| **Pinpoint**, varredura desta rodada | `https://<slug>.pinpointhq.com/register-your-interest/new` | **14.387** (1.365 da lista da campanha + 13.022 gerados dos CSVs de estúdio) | **69** | **62** |
| **Pinpoint**, os 29 quadros já conhecidos de 09/09 | mesma rota | 29 (relistados, a rodada anterior nunca testou esta rota) | 29 | **23** |
| **Pinpoint, total sem repetição** | | 14.387 slugs | **79 quadros reais** | **70 rotas abertas** |
| **Teamtailor Connect** | `https://<slug>.teamtailor.com/connect` | 62 slugs conhecidos da campanha | 62 | **43** (15 em 200 direto, 28 em 301 para domínio próprio) |
| **Homerun** | `https://<slug>.homerun.co/open-application` | 5 inquilinos vivos conhecidos | 3 | **1** (`totalmayhemgames`, **e já foi usada**) |
| **Recruitee** | `https://<slug>.recruitee.com/o/open-application` | 4 inquilinos vivos conhecidos | 3 | **0** |

Um `trust.pinpointhq.com` respondeu 200 nas duas rotas e **não é Pinpoint**: o título da página é
`Vanta`. Ele está fora dos 79 e dos 70 acima, e não conta como quadro.

**Leitura honesta destes números.** As 70 do Pinpoint são *rotas abertas*, não *casas úteis*:
a maioria esmagadora é empresa de fora do setor ou conta de demonstração. Depois da triagem de
disciplina, de escopo geográfico e do dedupe, **sobraram 11 casas**. Esse é o número que vale.

**Sinal de existência medido:** slug inexistente devolve **404 limpo**
(`naodeveexistirxyz123.pinpointhq.com/register-your-interest/new` → 404). **302 na rota com o
quadro vivo quer dizer banco de talentos DESLIGADO** naquela casa (`appquantum`,
`tripledotstudios`, `buildarocketboy`, `everi`, `ruckus-games`, `bandainamcomobile`,
`theready`). Zero erro de rede em 14.387 sondagens; o proxy aguentou concorrência 20.

---

## 2. O ACHADO QUE EVITA UMA FILA DE MENTIRA: **ACME e Hooli**

O relatório de 09/09 já avisava que o Pinpoint serve **vagas de demonstração** em quadros não
configurados. Hoje eu achei a assinatura **dentro do próprio formulário**, e ela é infalsificável.

Um quadro de demonstração traz, no combobox de `Locations` e `Departments`, sempre este conjunto:

- **Locations:** `Belfast, London, New York, Paris, Sydney, Washington`
- **Departments:** `Engineering, Finance, Marketing, Operations, Product, Sales`
- **Divisions:** **`ACME`** e **`Hooli`** ← nomes de empresa fictícia que a Pinpoint usa na conta de teste

**Quem cai nisso, e são casas de verdade com conta de teste abandonada:** `framestore`,
`frontierdevelopments`, `kwalee`, `moonbug`, `hornet`, `metaphysic`, `pushgaming`,
`tensquaregames`, `reply`, `realtimeuk`, `moonactive`, `improbable`, `yodo1`, `amplitude`,
`cube`, `digibc`, `elastic`, `exp`, `focus`, `light`, `merge`, `metropolis`, `muse`, `prosper`,
`redox`, `refuge`, `remarkable`, `rewind`, `spin`, `surgicalscience`, `stepchange`, `uncommon`,
`vanilla`, `hercules`, `stellar` (esta com `Guildford` real no meio do conjunto falso).

**Isto dói porque a Framestore é a melhor casa de criatura da lista inteira.** O quadro
`framestore.pinpointhq.com` responde 200, tem o título `Register Your Interest | Framestore
Careers`, não tem captcha, e mesmo assim **não entra na fila**: os departamentos oferecidos são
`Engineering, Finance, Marketing, Operations, Product, Sales` e as divisões são `ACME` e `Hooli`.
A Framestore recruta de verdade por outro ATS (o Recruitee, já registrado nesta campanha). Uma
candidatura ali cai numa conta de avaliação que ninguém abre. Registrei como descarte, não como
achado.

**Regra prática, para não se repetir:** antes de enfileirar um quadro Pinpoint, leia as opções
de `Locations` e `Departments`. **Se aparecer `ACME` ou `Hooli`, ou o par
`Belfast/London/New York/Paris/Sydney/Washington` completo, é conta de demonstração.**

---

## 3. A FILA PRONTA — 11 casas, ordenadas por quanto a casa encosta em personagem

### Campos, iguais em todas (nomes reais, medidos no HTML servido)

| Campo | Seletor | O que vai |
|---|---|---|
| First Name | `#job_seeker_form_job_seeker_first_name` | `Vini` |
| Last Name | `#job_seeker_form_job_seeker_last_name` | `Cavalcanti` |
| Email | `#job_seeker_form_job_seeker_email` | `contact@vinicavalcanti.art` |
| Telefone | `#phone-input` (ou `job_seeker_form[job_seeker][phone]`) | **formato internacional, valor SÓ na variável `VINI_TEL`** — não existe neste arquivo nem em nenhum arquivo do repositório |
| LinkedIn | `#job_seeker_form_linkedin_url` **ou** `#job_seeker_form_job_seeker_linkedin_url` (varia por casa, ver cada ficha) | `https://www.linkedin.com/in/vinicavalcnti/` |
| Personal Summary | `#personal-summary` | o texto da ficha |
| CV | `input[type=file]` | `Vini_Cavalcanti_CV.pdf` |
| Consentimento | `#job_seeker_form_process_information` | marcar |
| Locations | `[id="job_seeker_form[interest_options][location_ids][]"]` | ver ficha |
| Departments | `[id="job_seeker_form[interest_options][department_ids][]"]` | ver ficha |

**Régua de veto** (`authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`,
`citizen`, `resident`) rodada sobre o texto visível inteiro de cada uma das 11 páginas:
**nenhum dos oito termos casou em nenhuma**. Não há veto escrito em lugar nenhum desta fila.

**Nenhuma das 11 páginas tem iframe de reCAPTCHA, hCaptcha, Turnstile ou DataDome no HTML
servido.** Isso é ausência no HTML, não prova de que o POST passa; a prova é a tela `/thanks`.

---

### 1. Rocksteady Studios · Londres, Reino Unido

- **URL:** `https://rocksteady.pinpointhq.com/register-your-interest/new`
- **Por que é a primeira:** o quadro tem um departamento chamado **`Character`**, listado à parte
  de `Art` e de `Animation`. É a única casa das 53 que nomeia personagem como equipe própria.
  Batman Arkham e Suicide Squad são catálogo de herói e vilão estilizado.
- **Locations:** `London` (única). **Departments:** `Animation, Art, Character, Code: Engine & DevOps, Code: Gameplay & AI, Game Design & Production, IT, Lighting / VFX, Marketing, Office Management & Finance, QA` → **marcar `Character` e `Art`**.
- **LinkedIn:** `#job_seeker_form_linkedin_url`.
- **Perguntas do estúdio:** **nenhuma**. Não há campo booleano nesta casa.
- **Dedupe:** `sh automacao/dedupe-agora.sh "rocksteady" "Rocksteady"` → uma ocorrência em
  `enviados.csv`, e é **carta fria de 02/09 para `rocksteadyltd.com`**, mais um rascunho de
  follow-up em `processados.csv`. **Zero marca de envio por portal. Rota inédita. LIMPO.**

### 2. Playground Games · Leamington Spa, Reino Unido

- **URL:** `https://playground-games.pinpointhq.com/register-your-interest/new`
- **Por quê:** Fable tira o estúdio do carro e o põe em gente e criatura. É a casa de personagem
  mais óbvia da fila depois da Rocksteady.
- **Locations:** `Leamington Spa` (real). **Departments:** `Engineering, Finance, Marketing, Operations, Product, Sales` → **atenção, esta lista é a de demonstração**: o quadro está meio configurado, local verdadeiro e departamentos ainda de fábrica. **Marcar `Product`** e dizer a disciplina no Personal Summary, que é onde ela vai ser lida.
- **LinkedIn:** `#job_seeker_form_linkedin_url`.
- **Perguntas do estúdio:** nenhuma. Nenhuma booleana.
- **Dedupe:** `sh automacao/dedupe-agora.sh "playground-games" "Playground Games"` → carta fria
  entregue e **resposta humana da Tolani Durojaye, Associate Recruiter**, registrada em
  `processados.csv` (07/09: *"os dados dele entram no talent pool"*). **Isso reforça, não bloqueia:**
  a recrutadora disse que guardaria os dados e esta é a porta oficial de fazer isso. Zero
  candidatura por portal. LIMPO.

### 3. Magnopus · Los Angeles, EUA e St Albans, Reino Unido

- **URL:** `https://magnopus.pinpointhq.com/register-your-interest/new`
- **Por quê:** quadro **totalmente configurado**, com departamento `Art & Animation` e uma divisão
  literalmente chamada **`Virtual Art Department`**. Duas cidades, as duas em escopo.
- **Locations:** `Los Angeles`, `St Albans` → **marcar as duas**. **Departments:** `Art & Animation, Product Management, Technology` → **`Art & Animation`**. **Divisions:** `Generative AI, Product Management, Virtual Art Department` → **`Virtual Art Department`**.
- **LinkedIn:** `#job_seeker_form_linkedin_url`.
- **Perguntas do estúdio:** nenhuma. Nenhuma booleana.
- **Dedupe:** `sh automacao/dedupe-agora.sh "magnopus" "Magnopus"` → **zero ocorrências nos quatro
  arquivos. Casa inédita na campanha.**

### 4. Singularity 6 · Los Angeles, EUA

- **URL:** `https://singularity6.pinpointhq.com/register-your-interest/new`
- **Por quê:** Palia é jogo de personagem estilizado, que é exatamente o portfólio dele.
- **Locations:** `Los Angeles, CA` (real). **Departments:** conjunto de demonstração → marcar `Product`, disciplina pelo texto.
- **LinkedIn:** `#job_seeker_form_linkedin_url`. **Perguntas:** nenhuma.
- **Dedupe:** `sh automacao/dedupe-agora.sh "singularity6" "Singularity 6"` → carta fria de 02/09
  para `singularity6.com` e um rascunho de follow-up. **Zero por portal. LIMPO.**
- **Ressalva honesta:** o estúdio encolheu depois da aquisição em 2024. O quadro está vivo e a
  rota está aberta; o retorno esperado é menor que o das duas primeiras.

### 5. Pipeworks Studios · Eugene (Oregon), EUA — com Virtuos Montreal no mesmo quadro

- **URL:** `https://pipeworks.pinpointhq.com/register-your-interest/new`
- **Por quê:** quadro configurado de verdade, com `Art` entre os departamentos, e o co-desenvolvimento
  é onde artista que entrega o asset inteiro vale mais. Tem **Montreal** na lista, que é Canadá,
  país prioritário da campanha.
- **Locations:** `CounterPunch - Los Angeles, Eugene, OR, Los Angeles, Virtuos Montreal, Virtuos North America` → **marcar `Eugene, OR`, `Los Angeles` e `Virtuos Montreal`**. **Departments:** `Art, CP- Los Angeles, Design, Engineering, Finance, HR, IT, Marketing, Production, QA, VMTL-Design, VMTL-HR, VMTL-Production` → **`Art`**.
- **LinkedIn:** `#job_seeker_form_linkedin_url`.
- **Pergunta do estúdio, uma só:** slot 0, tipo `long_text`, **não obrigatória**, id `726078`:
  *"Please include a link to your portfolio, demo, or reel if it is not already listed on your resume."*
  → **Responder:** `https://www.artstation.com/viniciuscavalcanti`
  **Não é booleana.** Campo `job_seeker_form[job_seeker][answers_attributes][0][text_answer]`.
- **Dedupe:** `sh automacao/dedupe-agora.sh "pipeworks" "Pipeworks"` → **zero ocorrências. Inédita.**

### 6. Outpost VFX · Bournemouth, Reino Unido

- **URL:** `https://outpost-vfx.pinpointhq.com/register-your-interest/new`
- **Por quê:** VFX de cinema e televisão, onde criatura e humano digital são o produto. E há um
  motivo tático: **a porta que a campanha conhecia era o SmartRecruiters deles, que é parede de
  DataDome** (três vagas registradas no painel como "à mão por DataDome"). Esta rota é outra porta,
  do outro lado da casa, e não tem captcha nenhum.
- **Locations:** `Bournemouth` (real). **Departments:** conjunto de demonstração → `Product`.
- **LinkedIn:** `#job_seeker_form_linkedin_url`. **Perguntas:** nenhuma.
- **Dedupe:** `sh automacao/dedupe-agora.sh "outpost-vfx" "Outpost VFX"` → aparece no painel e na
  `FILA-DO-VINI.md` como **formulário de contato sem anexo, para ele preencher à mão**, e três vagas
  de SmartRecruiters barradas por DataDome. **Nenhuma marca de envio. A rota Pinpoint é inédita. LIMPO.**
- **Ressalva:** quadro meio configurado (local real, departamentos de fábrica). Vale o clique porque
  é a única porta deles sem parede.

### 7. Hyper Hippo Entertainment · Remoto no Canadá, sede em Kelowna, Colúmbia Britânica

- **URL:** `https://hyperhippo.pinpointhq.com/register-your-interest/new`
- **Por quê:** departamentos **reais e detalhados**, com `Art`, `Game Design`, `Production (Games)`
  e `UI / UX`. E o painel registra a casa como **parede**: *"a página de carreiras nem chega a
  montar"*. Esta rota entra por trás dessa parede.
- **Locations:** `Remote (Canada)` (única). **Departments:** `Art, Communications, Data, Engineering, Executive, Finance & Accounting, Game Design, Global Platforms & Player Experience (PX), Lab, Marketing & Content, P&C (Test), People & Culture, Player Experience, Production (Games), QA, UI / UX, Workplace & Technology` → **`Art`**.
- **LinkedIn:** `#job_seeker_form_linkedin_url`.
- **Pergunta do estúdio, uma só:** slot 0, `short_text`, **não obrigatória**, id `237602`:
  *"What are your pronouns?"* → **Responder:** `He/Him`. **Não é booleana.**
- **Dedupe:** `sh automacao/dedupe-agora.sh "hyperhippo" "Hyper Hippo"` → uma ocorrência no painel,
  e é a **parede de JavaScript de 08/09**, sem envio. **LIMPO.**

### 8. Ingenuity Studios · Los Angeles, EUA

- **URL:** `https://ingenuitystudios.pinpointhq.com/register-your-interest/new`
- **Por quê:** casa de VFX de Los Angeles, com CG de personagem e criatura. E o painel diz, com
  todas as letras, que **o quadro deles "não tem opção de candidatura espontânea"**. Tem: é esta.
- **Locations:** `Los Angeles, California` (real). **Departments:** conjunto de demonstração → `Product`.
- **LinkedIn:** `#job_seeker_form_linkedin_url`. **Perguntas:** nenhuma.
- **Dedupe:** `sh automacao/dedupe-agora.sh "ingenuitystudios" "Ingenuity Studios"` → uma ocorrência
  no painel, e ela é a medição de 0 vagas: *"There are currently no open roles. Come back later!,
  sem opcao de candidatura"*. **Sem envio. Esta rota corrige aquela nota. LIMPO.**

### 9. Wushu Studios · Liverpool, Reino Unido

- **URL:** `https://wushustudios.pinpointhq.com/register-your-interest/new`
- **Por quê:** co-desenvolvimento britânico, onde a entrega é casar com a direção de arte alheia,
  asset por asset. É o que dez anos de outsourcing treinam.
- **Locations:** `Liverpool` (real). **Departments:** conjunto de demonstração → `Product`.
- **LinkedIn:** `#job_seeker_form_linkedin_url`. **Perguntas:** nenhuma.
- **Dedupe:** `sh automacao/dedupe-agora.sh "wushustudios" "Wushu Studios"` → **zero ocorrências. Inédita.**

### 10. Flix Interactive · Bromsgrove, Reino Unido

- **URL:** `https://flixinteractive.pinpointhq.com/register-your-interest/new`
- **Por quê, e isto foi conferido no site deles hoje:** o projeto atual em Unreal Engine 5 anuncia
  vaga de *"Designer to own the creation, implementation and feel of **character combat** from Maya
  through to Unreal Engine 5"*. Há personagem na produção; o que falta lá é quem modele.
- **Locations:** `Bromsgrove` (real). **Departments:** conjunto de demonstração → `Product`.
- **LinkedIn:** `#job_seeker_form_linkedin_url`. **Perguntas:** nenhuma.
- **Dedupe:** `sh automacao/dedupe-agora.sh "flixinteractive" "Flix Interactive"` → carta fria de
  02/09 e uma **auto-resposta** registrada. **Nenhum envio por portal. LIMPO.**

### 11. Gameplay Galaxy · totalmente remoto

- **URL:** `https://gameplaygalaxy.pinpointhq.com/register-your-interest/new`
- **Por quê fica em último:** o jogo é de moto (Trial Xtreme, Trailblazer), então personagem é
  piloto e não elenco. Entra porque o quadro tem departamento **`Art`** de verdade e porque é a
  **única da fila que é 100% remota**, o que dispensa visto.
- **Locations:** `Remote` (única). **Departments:** `Art, Business Development, Data, Design, Development, HR, Marketing, Product, Sound` → **`Art`**.
- **Dedupe:** `sh automacao/dedupe-agora.sh "gameplaygalaxy" "Gameplay Galaxy"` → **zero ocorrências. Inédita.**
- **É a única da fila com formulário longo. Nove perguntas, e QUATRO SÃO BOOLEANAS.**

| slot | id | tipo | obrigatória | pergunta | resposta decidida |
|---|---|---|---|---|---|
| 0 | 361845 | `short_text` | sim | *"What are your salary expectations ?"* (pede a moeda, valor bruto) | `Open to aligning with your band for the role; as a reference, I am looking at around USD 85,000 gross per year.` |
| 1 | 361846 | **`boolean`** | sim | *"Do you have experience working within the games industry?"* | **`true`** |
| 2 | 977132 | `long_text` | sim, **condicional** do slot 1 valer `true` | *"What are the most successful games you've worked on?"* | `Endstar at E-Line Media, where I have built hero characters from sculpt to engine for close to five years, and The Wingfeather Saga at Angel Studios, where I modelled and hand painted the season one characters.` |
| 3 | 361844 | **`boolean`** | sim | *"Are you happy to work 100% remote?"* | **`true`** |
| 4 | 366823 | **`boolean`** | sim | *"...we ask for exclusivity. That means you wouldn't be able to work as freelance with other companies. Are you ok with that?"* | **`true`** |
| 5 | 363341 | `multiple_choice` | sim | *"How many years of experience do you have in a similar position?"* | `More than 10 years` |
| 6 | 366840 | `short_text` | sim | *"When would you be available to join?"* | `Four weeks from an offer.` |
| 7 | 850215 | **`boolean`** | sim | *"Do you require any form of visa sponsorship to work on your current location?"* | **`false`** — leia a justificativa abaixo |
| 8 | 988660 | `long_text` | sim | *"How do you use AI in your position?"* | `I use it for reference gathering, for naming and sorting files, and for boilerplate scripting. Sculpting, retopology, UV, texturing and grooming stay hand made, because that is what the work is judged on.` |

**Por que o slot 7 é `false` e por que isso NÃO é mentira.** A pergunta é *sponsorship to work
**on your current location***, e não sponsorship para o cargo. A vaga é 100% remota e a casa
contrata remoto no mundo todo; ele já trabalha remoto com time americano hoje, de onde mora, sem
visto nenhum. Responder `true` aqui diria que ele não pode trabalhar de onde está, o que é falso.
A verdade sobre visto para cargo presencial vai escrita no Personal Summary, com todas as letras.

**ARMADILHA, e ela custou um dia à campanha:** os quatro radios booleanos do Pinpoint **não valem
`Yes` e `No`, valem `true` e `false`**. Montar o id como `_text_answer` acha campo que não existe,
o combo é pulado em silêncio e o servidor recusa com `Answers boolean answer can't be blank`. O
`pin_interesse.js` já está consertado; no arquivo de respostas, use `"valores": ["Yes"]` que o
script traduz, ou escreva `true` direto.

**Os slots 1, 3, 4, 5, 6 ausentes na leitura de HTML da Fenris eram condicionais.** Aqui só o
slot 2 é condicional (aparece quando o slot 1 vira `true`). Os outros oito vêm de cara.

---

## 4. OS TEXTOS DE PERSONAL SUMMARY, um por casa

Todos abaixo de 250 palavras, sem frase em capslock, sem a palavra proibida, sem travessão, com a
linha de realocação uma vez só, assinados **Vini Cavalcanti**.

### 1. Rocksteady

> I am registering my interest in character work at Rocksteady. The Arkham games and Suicide Squad built a house style where hero and villain silhouettes have to read at cinematic range and still hold up in close gameplay, and your own board lists Character as a department of its own, which is exactly the seat I work in.
>
> I am a senior 3D character artist with more than ten years on stylized characters and creatures. At Angel Studios I modelled and hand painted the season one characters of The Wingfeather Saga. For close to five years at E-Line Media I have built hero characters end to end on Endstar, from sculpt to engine, working remotely with an American team. I came up through outsourcing at PUGA Studios, which is where I learned to match someone else's art direction asset for asset.
>
> I take a character all the way: high poly, sculpt, retopology, UV, bake, texture, LODs and engine setup, with grooming in Houdini as a support skill. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it: https://www.artstation.com/viniciuscavalcanti
>
> I am not a UK or EU citizen, so I would need work authorization sponsorship. I am ready to move for the role.
>
> Vini Cavalcanti

### 2. Playground Games

> I am registering my interest in character work at Playground Games. Fable moves the studio from vehicles into a world made of people and creatures, and stylized character sculpting, surfacing and grooming for a British fantasy is the brief my portfolio was built for.
>
> I am a senior 3D character artist with more than ten years on stylized characters and creatures. At Angel Studios I modelled and hand painted the season one characters of The Wingfeather Saga. For close to five years at E-Line Media I have built hero characters end to end on Endstar, from sculpt to engine, working remotely with an American team. Before that I came up through outsourcing at PUGA Studios.
>
> I take a character all the way: high poly, sculpt, retopology, UV, bake, texture, LODs and engine setup, with grooming in Houdini as a support skill. That full ownership is the part game studios get from me that a single stage specialist cannot give. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it: https://www.artstation.com/viniciuscavalcanti
>
> Your recruiter Tolani Durojaye kindly said in September that my details would go into the talent pool, so I am registering here properly.
>
> I am not a UK or EU citizen, so I would need work authorization sponsorship. I am ready to move for the role.
>
> Vini Cavalcanti

### 3. Magnopus

> I am registering my interest in the Art and Animation team at Magnopus, and in the Virtual Art Department in particular. Your work puts believable characters inside real time environments for film, location based and immersive projects, and taking a character from a sculpt to a shipped real time asset is what I do every day.
>
> I am a senior 3D character artist with more than ten years on stylized characters and creatures. At Angel Studios I modelled and hand painted the season one characters of The Wingfeather Saga. For close to five years at E-Line Media I have built hero characters end to end on Endstar, from sculpt to engine, working remotely with an American team. I came up through outsourcing at PUGA Studios.
>
> I take a character all the way: high poly, sculpt, retopology, UV, bake, texture, LODs and engine setup, with grooming in Houdini as a support skill. Coming from games means I hand over an asset that is already budgeted, rigged for real time and running in engine, not a model that still needs a pipeline around it. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it: https://www.artstation.com/viniciuscavalcanti
>
> I am a citizen of neither the United States nor the United Kingdom, so I would need work authorization sponsorship for either office. I am ready to move for the role.
>
> Vini Cavalcanti

### 4. Singularity 6

> I am registering my interest in character work at Singularity 6. Palia is carried by warm, readable, stylized characters, and stylized humans and creatures are the centre of my portfolio rather than a side of it.
>
> I am a senior 3D character artist with more than ten years on stylized characters and creatures. At Angel Studios I modelled and hand painted the season one characters of The Wingfeather Saga. For close to five years at E-Line Media I have built hero characters end to end on Endstar, from sculpt to engine, working remotely with an American team on Pacific hours. I came up through outsourcing at PUGA Studios.
>
> I take a character all the way: high poly, sculpt, retopology, UV, bake, texture, LODs and engine setup, with grooming in Houdini as a support skill. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it: https://www.artstation.com/viniciuscavalcanti
>
> I do not hold work authorization in the United States, so I would need visa sponsorship. I am ready to move for the role.
>
> Vini Cavalcanti

### 5. Pipeworks Studios

> I am registering my interest in the Art team at Pipeworks Studios, for Eugene, Los Angeles or Virtuos Montreal. Co-development means picking up someone else's style guide and matching it asset for asset, and that is the exact skill outsourcing taught me before I ever worked in house.
>
> I am a senior 3D character artist with more than ten years on stylized characters and creatures. At Angel Studios I modelled and hand painted the season one characters of The Wingfeather Saga. For close to five years at E-Line Media I have built hero characters end to end on Endstar, from sculpt to engine, working remotely with an American team. I came up through outsourcing at PUGA Studios.
>
> I take a character all the way: high poly, sculpt, retopology, UV, bake, texture, LODs and engine setup, with grooming in Houdini as a support skill. On a co-development team that means one person carries the character from concept handoff to engine, instead of three handoffs. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it: https://www.artstation.com/viniciuscavalcanti
>
> I do not hold work authorization in the United States or Canada, so I would need visa sponsorship. I am ready to move for the role.
>
> Vini Cavalcanti

### 6. Outpost VFX

> I am registering my interest in character and creature work at Outpost VFX. Film and television work asks for digital humans and creatures that survive a close up, and modelling, surfacing and grooming characters is my whole discipline rather than one station in it.
>
> I am a senior 3D character artist with more than ten years on stylized characters and creatures. At Angel Studios I modelled and hand painted the season one characters of The Wingfeather Saga, an animated series where every hero and creature had to hold up shot after shot. For close to five years at E-Line Media I have built hero characters end to end on Endstar, from sculpt to engine. I came up through outsourcing at PUGA Studios.
>
> I take a character all the way: high poly, sculpt, retopology, UV, bake, texture and look development, with grooming in Houdini as a support skill. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it: https://www.artstation.com/viniciuscavalcanti
>
> I am not a UK or EU citizen, so I would need work authorization sponsorship. I am ready to move for the role.
>
> Vini Cavalcanti

### 7. Hyper Hippo Entertainment

> I am registering my interest in the Art team at Hyper Hippo Entertainment. Your games live on cartoon characters with shapes that read instantly at small sizes, and stylized character modelling and hand painted texturing is what my portfolio is made of.
>
> I am a senior 3D character artist with more than ten years on stylized characters and creatures. At Angel Studios I modelled and hand painted the season one characters of The Wingfeather Saga. For close to five years at E-Line Media I have built hero characters end to end on Endstar, from sculpt to engine, working remotely with an American team. I came up through outsourcing at PUGA Studios.
>
> I take a character all the way: high poly, sculpt, retopology, UV, bake, texture, LODs and engine setup, with grooming in Houdini as a support skill. Remote work with a distributed team is how I have worked for five years, so a remote Canadian team is familiar ground. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it: https://www.artstation.com/viniciuscavalcanti
>
> I do not hold work authorization in Canada, so I would need visa sponsorship for an employed position there. I am ready to move for the role.
>
> Vini Cavalcanti

### 8. Ingenuity Studios

> I am registering my interest in character and creature work at Ingenuity Studios. Your film, television and music video work leans on CG characters that have to sit next to live action without being noticed, and character modelling, surfacing and grooming is the only discipline I have worked in.
>
> I am a senior 3D character artist with more than ten years on stylized characters and creatures. At Angel Studios I modelled and hand painted the season one characters of The Wingfeather Saga. For close to five years at E-Line Media I have built hero characters end to end on Endstar, from sculpt to engine. I came up through outsourcing at PUGA Studios, which taught me to match an established look exactly.
>
> I take a character all the way: high poly, sculpt, retopology, UV, bake, texture and look development, with grooming in Houdini as a support skill. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it: https://www.artstation.com/viniciuscavalcanti
>
> I do not hold work authorization in the United States, so I would need visa sponsorship. I am ready to move for the role.
>
> Vini Cavalcanti

### 9. Wushu Studios

> I am registering my interest in the art team at Wushu Studios. Co-development in Liverpool means matching an existing art direction asset for asset and shipping to someone else's bar, and that is the skill outsourcing taught me before I ever worked in house.
>
> I am a senior 3D character artist with more than ten years on stylized characters and creatures. At Angel Studios I modelled and hand painted the season one characters of The Wingfeather Saga. For close to five years at E-Line Media I have built hero characters end to end on Endstar, from sculpt to engine, working remotely with an American team. I came up through outsourcing at PUGA Studios.
>
> I take a character all the way: high poly, sculpt, retopology, UV, bake, texture, LODs and engine setup, with grooming in Houdini as a support skill. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it: https://www.artstation.com/viniciuscavalcanti
>
> I am not a UK or EU citizen, so I would need work authorization sponsorship. I am ready to move for the role.
>
> Vini Cavalcanti

### 10. Flix Interactive

> I am registering my interest in character art at Flix Interactive. Your Unreal Engine 5 project is built around character combat from Maya through to engine, and the character models inside that pipeline are the part I own from sculpt to engine.
>
> I am a senior 3D character artist with more than ten years on stylized characters and creatures. At Angel Studios I modelled and hand painted the season one characters of The Wingfeather Saga. For close to five years at E-Line Media I have built hero characters end to end on Endstar, from sculpt to engine, working remotely with an American team. I came up through outsourcing at PUGA Studios.
>
> I take a character all the way: high poly, sculpt, retopology, UV, bake, texture, LODs and engine setup, with grooming in Houdini as a support skill. On a small team that matters, because one person covers what usually takes three. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it: https://www.artstation.com/viniciuscavalcanti
>
> I am not a UK or EU citizen, so I would need work authorization sponsorship. I am ready to move for the role.
>
> Vini Cavalcanti

### 11. Gameplay Galaxy

> I am registering my interest in the Art team at Gameplay Galaxy. Trial Xtreme and Trailblazer put a rider on screen on every single run, and stylized character modelling, texturing and grooming is my whole discipline.
>
> I am a senior 3D character artist with more than ten years on stylized characters and creatures. At Angel Studios I modelled and hand painted the season one characters of The Wingfeather Saga. For close to five years at E-Line Media I have built hero characters end to end on Endstar, from sculpt to engine. That role is fully remote with an American team, so a fully remote, fully invested position is how I already work. I came up through outsourcing at PUGA Studios.
>
> I take a character all the way: high poly, sculpt, retopology, UV, bake, texture, LODs and engine setup, with grooming in Houdini as a support skill. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it: https://www.artstation.com/viniciuscavalcanti
>
> I can work remotely from where I live today with no sponsorship needed. For an onsite position I would need work authorization sponsorship. I am ready to move for the role.
>
> Vini Cavalcanti

---

## 5. TEAMTAILOR, HOMERUN E RECRUITEE

**A conclusão que muda o método: só o Pinpoint e o Teamtailor têm rota espontânea FIXA.**

- **Pinpoint:** `/register-your-interest/new` existe sempre que a casa liga o banco de talentos.
  URL previsível, dá para sondar em lote. É o que esta rodada explorou.
- **Teamtailor:** `/connect` idem. **200 = aberto no subdomínio; 301 = aberto e servido no domínio
  próprio**, terminando em `/connect/candidates/new` (medido: `10chambers` → `careers.10chambers.com`,
  `fatshark` → `jobs.fatsharkgames.com`, `ioi` → `apply.ioi.dk`, `sharkmob` → `career.sharkmob.com`).
  **404 = fechado.** Dos 62 slugs Teamtailor que a campanha já conhece, **43 têm o Connect aberto**.
  A campanha já usou quatro (Sharkmob, Ghost Ship Games, Snowprint Studios e Sloclap, todos em 07/09),
  então **sobram cerca de 39 portas Teamtailor abertas e não usadas**. Isso é fila de outra rodada e
  vale mais que qualquer varredura nova: são casas já validadas.
- **Homerun:** **não há rota fixa.** `/<slug>.homerun.co/open-application` só responde 200 quando o
  estúdio criou uma vaga com esse nome (a `totalmayhemgames` tem, e a campanha já enviou por ela).
  A `ustwo-games`, que recebeu candidatura em 09/09, hoje devolve 302 até na raiz. Descoberta de
  Homerun tem que passar pelo feed `https://feed.homerun.co/<slug>`, um a um. A varredura de 09/09
  já testou 3.521 slugs e achou 3 quadros: **rendimento baixo demais para repetir.**
- **Recruitee:** **não há rota fixa** e, pior, **a família tem parede.** `/o/open-application` deu
  404 ou 302 em todos os inquilinos vivos testados. E a campanha já mediu duas vezes, na Framestore
  e na Reality Games, que **o hCaptcha do Recruitee aparece DEPOIS do Send**, com
  `captcha-base.recruiteecdn.com` do tipo prova de trabalho. **Recruitee não é rota sem captcha.
  Não vale varrer.**

---

## 6. O QUE FOI DESCARTADO, com o motivo literal

**Já enviadas hoje ou antes, por esta mesma rota (não repetir):**

| Casa | Motivo literal |
|---|---|
| **Fenris Creations** | `enviados.csv` 10/09: *"CANDIDATURA ENVIADA E CONFIRMADA as 04h5x UTC de 10/09 (...) URL final terminando em /thanks"*. O subdomínio `fenriscreations.pinpointhq.com` responde 200 e é **o mesmo quadro** de `careers.fenriscreations.com`; não é porta nova. |
| **Brazen Animation** | `processados.csv` 10/09: *"CANDIDATURA ENVIADA E CONFIRMADA as 04h40 UTC pelo Jhon, pela rota register-your-interest do Pinpoint"*. Outro agente pegou esta mesma veia às 04h40. |
| **TTK Games AB** | `enviados.csv` 10/09: *"ENVIADA A MAO POR ELE e confirmada pelo recibo do Pinpoint as 04h09 UTC"*. |
| **REALTIME (RealtimeUK)** | `processados.csv` 07/09: *"o /connect/dashboard lista em Your applications UMA candidatura, titulo Register Your Interest (...) Marcado done=true, nao reenviar"*. |
| **Maverick Games** | `enviados.csv` 09/09: *"Thanks. Your application was received successfully"*, mais o recibo em `processados.csv`: *"RECIBO da candidatura espontanea as 03h25"*. A rota `/register-your-interest/new` deles está aberta, mas a espontânea já foi feita pela rota `/applications/new`. |

**Veto escrito, que é o único que desqualifica:**

| Casa | Frase literal |
|---|---|
| **Blackbird Interactive** (Vancouver) | Frase inteira, do anúncio deles, já registrada no painel em 07/09: *"PLEASE NOTE: At this time, we are only able to hire candidates who are legally eligible to work in Canada and reside within Canada."* Casa em `eligib` e em `resident`, e os dois acertos são veto de verdade, não falso positivo de benefício. O painel a marca como **"VETO DE RESIDENCIA, NAO APLICAR"**. Doeu descartar: é Vancouver, Homeworld e Minecraft Legends, e a rota estava aberta. |

**Conta de demonstração, reconhecida por `ACME` e `Hooli` (35 casas).** Rota aberta, formulário sem
captcha, e mesmo assim descartadas porque a candidatura cai numa conta de avaliação: `framestore`,
`frontierdevelopments`, `kwalee`, `moonbug`, `hornet`, `metaphysic`, `pushgaming`, `tensquaregames`,
`reply`, `moonactive`, `improbable`, `yodo1`, `stellar`, `amplitude`, `cube`, `digibc`, `elastic`,
`exp`, `focus`, `light`, `merge`, `metropolis`, `muse`, `prosper`, `redox`, `refuge`, `remarkable`,
`rewind`, `spin`, `surgicalscience`, `stepchange`, `uncommon`, `vanilla`, `hercules`, `realtimeuk`.

**Fora de escopo geográfico:** `bighappy` (as duas vagas são `Front End Developer | India` e
`Back End Developer | India`).

**Homônimo, não é o estúdio que o nome sugere:** `amber` é a **Amber Energy** britânica, e não a
Amber Studio de jogos, provado pelos departamentos `Net-Zero Consultancy`, `Trading and Risk` e
`PBSA`. `embark` é a **Embark Student Corp.**, poupança educacional canadense, e não a Embark
Studios. `trust.pinpointhq.com` responde 200 mas **não é Pinpoint**: o título é `Vanta`.

**Fora do setor, por disciplina:** `artisan` (Artisan Healthcare Consulting, Waltham MA),
`branch` (seguradora, Ohio), `hirewell` (recrutamento, Chicago), `jumpstart` (marketing, e os
"departamentos" são `Coca Cola, Disney, Ford, Gucci, Panasonic, Sprite`), `kinetic` (software de
gestão, Shropshire), `osome` (contabilidade, Londres), `richter` (Buckinghamshire), `shortcut`
(Nova York), `triangle` (Triangle Heavy Equipment, **Cairo**, fora de escopo também), `virtex`
(estádio virtual de esports, produto é ambiente e não personagem), `ggtech` (GG.BET, apostas),
`praxis`, `surgicalscience` (simulação médica, e **animação médica não entra pela regra**),
`uncommon` (Uncommon Creative Studio, **publicidade**, e publicidade de produto não entra).

**Casa de jogo ou animação, mas sem produção de personagem que justifique o clique:**

| Casa | Motivo |
|---|---|
| **Sun Creature** (Copenhague) | Estúdio de animação **2D**. O portfólio dele é 3D full character; a casa não tem a produção onde ele compete. |
| **Curve Digital / Curve Games** (Londres) | **Publisher**, sem produção interna de personagem. O próprio Jhon já a classificou hoje em `processados.csv` como *"curvedigital (Reino Unido, register aberto, publisher)"*. |
| **Tripledot Talent** (Londres, Barcelona, Los Angeles, Varsóvia) | Mobile casual de puzzle e paciência. Tem departamento `Art`, mas não tem elenco de personagem. Fica registrada para quando a régua alargar. |

**Rota fechada apesar do quadro vivo (302 na `/register-your-interest/new`):** `appquantum`,
`tripledotstudios`, `buildarocketboy`, `everi`, `ruckus-games`, `bandainamcomobile`, `theready`.
**Vale re-testar em duas ou três semanas: ligar o banco de talentos é um clique no painel do
estúdio, e quadro que hoje está em 302 pode estar em 200 na semana que vem.**

---

## 7. MÉTODO E LIMITES, para a próxima rodada não refazer

- **14.387 slugs sondados por `curl`**, concorrência 20, zero erro de rede. Os 13.022 novos foram
  gerados a partir dos nomes de estúdio de `fila-gamedevmap-canada.csv`, das quatro fatias de
  `fila-gamedevmap-europa*.csv`, de `fila-gamedevmap-ch-fi-nl.csv`, `fila-gamedevmap-se-dk.csv`,
  `garimpo-cgstudiomap.csv`, `fila-remotegamejobs-estudios.csv`, `fila-jhon-portas.csv` e
  `fila-oceania.csv`, em duas formas cada (com e sem hífen) e com o sufixo de tipo removido.
- **A varredura de 09/09 tinha testado 4.428 slugs contra `postings.json` e achado 28 quadros.
  Ela não testou a rota do banco de talentos.** Foi aí que estava o achado: **23 daqueles 28
  quadros têm a rota aberta**, incluindo casas com `postings.json` vazio, que a rodada anterior
  tinha marcado como "sem vaga".
- **Limite conhecido 1:** sondar `<slug>.pinpointhq.com` **não acha quadro servido só em domínio
  próprio**. A Fenris só apareceu porque a campanha já sabia o domínio. **Conferido no resultado
  da varredura de domínio que o Jhon rodou em paralelo** (`automacao/quadros-novos-1009.csv`, 4.500
  domínios sondados, 85 quadros novos): ali existe **uma única linha `pinpoint`**, e é a
  `gameplaygalaxy`, que a minha varredura de slug já tinha achado. Ou seja, para o Pinpoint, o eixo
  de domínio **não acrescentou nada** ao eixo de slug nesta rodada. O buraco continua sendo o
  estúdio que serve o Pinpoint em domínio próprio sem citar `pinpointhq.com` no HTML da página de
  carreiras, que foi exatamente o caso da Fenris.
- **Limite conhecido 2:** a leitura do formulário é do HTML servido. **Pergunta condicional só
  aparece depois que a pergunta pai é respondida**, então as casas listadas aqui como "nenhuma
  pergunta" podem revelar uma na hora do preenchimento, como aconteceu na Fenris. Quem enviar
  tem que reler a tela antes do clique, como o `pin_interesse.js` já faz.
- **Limite conhecido 3:** ausência de captcha no HTML servido **não é prova de que o POST passa**.
  Captcha pode ser injetado por JavaScript no submit. A prova é a URL terminando em `/thanks`.
- **Não repetir:** varredura de slug Homerun (3.521 testados em 09/09, 3 quadros) e varredura de
  Recruitee (parede de hCaptcha pós-Send, medida duas vezes).
- **Fazer a seguir, e é o de maior retorno:** as **39 portas Teamtailor Connect já abertas e ainda
  não usadas**, listadas em §5. Não precisam de descoberta nenhuma, só de envio.

---

## 8. ARQUIVOS DE RESPOSTA PRONTOS

Salvar cada bloco como `automacao/ans_<slug>.json` e rodar
`VINI_TEL='<formato internacional>' sh automacao/hb_run.sh pin_interesse.js ans_<slug>.json <slug> --submit`.
O `__TEL__` é substituído pela variável de ambiente; **o número não entra em arquivo nenhum do
repositório**. O `#personal-summary` vai com o texto da §4 daquela casa.

O esqueleto comum, que muda pouco de casa para casa:

```json
{
  "url": "https://<slug>.pinpointhq.com/register-your-interest/new",
  "cv": "Vini_Cavalcanti_CV.pdf",
  "texto": {
    "#job_seeker_form_job_seeker_first_name": "Vini",
    "#job_seeker_form_job_seeker_last_name": "Cavalcanti",
    "#job_seeker_form_job_seeker_email": "contact@vinicavalcanti.art",
    "#phone-input": "__TEL__",
    "#job_seeker_form_linkedin_url": "https://www.linkedin.com/in/vinicavalcnti/",
    "#personal-summary": "<o texto da §4 desta casa>"
  },
  "combos": [
    {"sel": "[id=\"job_seeker_form[interest_options][location_ids][]\"]", "rotulo": "Locations", "valores": ["<ver ficha>"]},
    {"sel": "[id=\"job_seeker_form[interest_options][department_ids][]\"]", "rotulo": "Departments", "valores": ["<ver ficha>"]},
    {"sel": "#job_seeker_form_equality_monitoring_gender", "rotulo": "Gender", "valores": ["Prefer Not To Say"]}
  ]
}
```

**O que muda por casa, e é só isto:**

| Slug | `Locations` | `Departments` | LinkedIn | `combos` extras |
|---|---|---|---|---|
| `rocksteady` | `London` | `Character`, `Art` | `#job_seeker_form_linkedin_url` | nenhum |
| `playground-games` | `Leamington Spa` | `Product` | `#job_seeker_form_linkedin_url` | nenhum |
| `magnopus` | `Los Angeles`, `St Albans` | `Art & Animation` | `#job_seeker_form_linkedin_url` | `division_ids` → `Virtual Art Department` |
| `singularity6` | `Los Angeles, CA` | `Product` | `#job_seeker_form_linkedin_url` | nenhum |
| `pipeworks` | `Eugene, OR`, `Los Angeles`, `Virtuos Montreal` | `Art` | `#job_seeker_form_linkedin_url` | pergunta de portfólio no slot 0, `text_answer` |
| `outpost-vfx` | `Bournemouth` | `Product` | `#job_seeker_form_linkedin_url` | nenhum |
| `hyperhippo` | `Remote (Canada)` | `Art` | `#job_seeker_form_linkedin_url` | pronomes no slot 0, `text_answer` |
| `ingenuitystudios` | `Los Angeles, California` | `Product` | `#job_seeker_form_linkedin_url` | nenhum |
| `wushustudios` | `Liverpool` | `Product` | `#job_seeker_form_linkedin_url` | nenhum |
| `flixinteractive` | `Bromsgrove` | `Product` | `#job_seeker_form_linkedin_url` | nenhum |
| `gameplaygalaxy` | `Remote` | `Art` | `#job_seeker_form_linkedin_url` | **as nove perguntas da tabela da ficha 11, quatro delas booleanas** |

**Conferência antes de cada clique, e ela não é opcional:** o `pin_interesse.js` já lê de volta o
que ficou na tela em cada combo. Se algum devolver `NAO CONFERE` ou `NAO MARCOU`, **não enviar**,
porque em formulário de emprego chute vira resposta falsa entregue ao estúdio.
