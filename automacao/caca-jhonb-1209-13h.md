# Caça do JHON B — 12/09/2026, 13h — a lista dos 268 fechada, e um conserto de medição

Rodada de `curl` e API. **Nenhum navegador foi aberto, nada foi enviado, nenhum rascunho foi
criado.** Faixa obedecida: quem envia é o Jhon A.

---

## 1. PLACAR

| Medida | Número |
|---|---|
| Quadros consultados nesta rodada | **322** (290 fora do censo + 32 do censo, remedidos) |
| Quadros que **responderam** | **313** |
| Quadros **NÃO CONFERIDOS**, nomeados um a um | **9** |
| Vagas lidas | **2.366** |
| Casaram na rede larga de disciplina | 46 |
| Sobreviveram ao escopo e ao corpo lido | 6 |
| Sobreviveram à régua de veto | 3 |
| Sobreviveram ao **dedupe por ID de requisição** | **0** |
| **FILA FINAL** | **0 — rodada honesta de zero** |

**A quebra que o Vini pede: 0 de personagem e 0 de ambiente.** E o zero de ambiente é
**decisão, não escassez**: sobrou uma vaga de ambiente limpa e sem veto (Eleventh Hour Games,
§4.1) e eu **não a enfileirei**, pela frase dele de 10/09 — *"eu n vou passar. meu portfolio é
full character. isso é perda de tempo."*

---

## 2. A TAREFA DA RODADA ESTÁ FECHADA: OS 268 VIRARAM 290, E OS 290 FORAM LIDOS

A rodada das 10h45 achou 268 quadros conhecidos fora do censo e leu 95, **mas não gravou
quais**. Sem essa lista não dá para subtrair, então em vez de adivinhar eu **refiz o
cruzamento inteiro e li os 290**, e gravei a lista para que isto nunca mais se perca:
**`automacao/quadros-fora-censo-1209.csv`**, uma linha por token, com status, contagem de
vagas e a coluna `conferido`.

O cruzamento novo (798 arquivos do repositório, 10 famílias de ATS) bate com o da rodada
anterior e acrescenta três famílias que ela não contou:

| Família | Tokens no repositório | No censo | **Fora do censo** |
|---|---|---|---|
| teamtailor | 151 | 32 | **119** |
| recruitee | 72 | 5 | **67** |
| greenhouse | 50 | 31 | **21** |
| workable | 20 | 0 | **20** |
| pinpoint | 19 | 0 | **19** |
| bamboohr | 37 | 20 | **17** |
| personio | 12 | 0 | **12** |
| lever | 20 | 12 | **8** |
| ashby | 10 | 6 | **4** |
| smartrecruiters | 11 | 14 | **3** |
| **TOTAL** | | | **290** |

**Nada sobrou dos 173. A próxima rodada não recomeça: ela lê o CSV.**

---

## 3. O ACHADO DA RODADA É UM ERRO MEU, E ELE VALE MAIS QUE A FILA

### 3.1 — O leitor de Teamtailor perdia o quadro INTEIRO quando a casa usa domínio próprio

Minha primeira varredura disse que **airshipinteractive tinha ZERO vaga**. Fui conferir à mão:
**tem DEZ**, entre elas uma **Character Artist** e uma **Groom Artist**.

**A causa, medida.** O Teamtailor responde **301** de `<slug>.teamtailor.com/jobs` para o
domínio próprio da casa (`careers.airshipinteractive.com/jobs`) e, na página servida, os
`href` são **absolutos naquele domínio**:

```
href="https://careers.airshipinteractive.com/jobs/8281687-character-artist"
```

Minha expressão só aceitava `href` relativo ou `href` em `*.teamtailor.com`. Casava zero, e o
laço registrava **ZERO VAGA** — exatamente como se tivesse conferido.

**É a mesma família do falso negativo da ronda do Disney de 06h45:** a sonda não falha alto,
ela mente baixo. E confirma a regra que já está no BRIEFING — *quadro vazio não é casa sem
vaga* — com um número novo.

**O tamanho do buraco, nos mesmos 119 tokens:**

| | Antes (leitor furado) | Depois (consertado) |
|---|---|---|
| Quadros com vaga | 25 | **79** |
| Vagas visíveis | 141 | **653** |

**Quatro em cada cinco vagas de Teamtailor estavam invisíveis para mim.**

### 3.2 — Por isso remedi também os 32 Teamtailor DE DENTRO do censo

Se o leitor mentia, o censo lido com ele também não valia. Remedi os 32: **32 de 32
responderam, 167 vagas, 13 na rede de disciplina.** O resultado é tranquilizador e vale
registrar: **as três de personagem que apareceram já estavam trabalhadas** — Beffio
`6217989` e `7242656`, Fatshark `8190501`, todas enviadas em 06/09 pela reconciliação de
Teamtailor de 11/09, que usou outra rota e por isso não caiu neste erro.

**Lição de método:** o conserto não achou vaga nova, e mesmo assim é a entrega da rodada.
Sem ele, toda varredura futura de Teamtailor — a família mais numerosa que a campanha
conhece, 151 tokens — continuaria devolvendo um quinto do que existe.

---

## 4. O QUE CAIU, COM A FRASE LITERAL DE CADA UM

### 4.1 — Caiu por DISCIPLINA, e uma delas caiu por decisão do dono

**Eleventh Hour Games — Senior Environment Artist — Remoto** (`8501085002`,
`internal_job_id` `6395734002`, Greenhouse, publicada 10/04 e atualizada 28/08).
Esta é a única sobrevivente limpa da rodada inteira, e por isso ela precisa ficar escrita
com todos os números, para ninguém a "redescobrir" amanhã achando que é achado novo:

- **Régua rodada no corpo inteiro pela API: ZERO veto escrito.** A única ocorrência de
  qualquer termo é *"our recruiters will only reach out to you via @eleventhhour.games..."*,
  que é aviso antifraude. Nada de `authoriz`, `sponsor`, `visa`, `citizen`, `resident`,
  `work permit`, `must be based`, `relocat`, nem idioma.
- **Restrição de presença e de fuso, não veto:** o formulário tem pergunta obrigatória
  *"Are you able to be fully available during Eleventh Hours Games' core hours (10:00AM -
  4:00PM Central Time)?"* — e isso é 12h às 18h no fuso dele, ou seja **responder-se-ia SIM
  com folga**.
- **Dedupe limpo nas duas pontas:** `8501085002` inédito nos quatro arquivos; a casa só
  aparece como `portal-only` de 04/09, sem candidatura. **Gmail conferido por janela de
  tempo** (`"Eleventh Hour" OR eleventhhour OR "Last Epoch"`): **zero mensagem**, nunca houve
  contato. Rota tecnicamente livre, e o Greenhouse é enviável pela automação.
- **NÃO ENFILEIRADA, e o motivo é a regra do Vini de 10/09.** É ambiente puro: zero
  ocorrência de `character` ou `creature` no corpo, e o formulário exige **oito dissertações
  obrigatórias** todas sobre ambiente — *"What environments or areas have you fully owned
  from concept to final implementation?"*, *"Describe your experience working directly in
  engine... (materials, shaders, optimization, layout)"*, *"What types of environments or
  worlds are you most experienced building (open worlds, linear levels...)?"*. Mandar um
  portfólio full-character para responder isso é literalmente o que ele chamou de perda de
  tempo. **Fica registrada como porta aberta, não como fila.**

**Epic Games — Hard Surface Outsource Lead** (`6142980004` Cary e `6142982004` multi-local,
**mesma requisição**, `internal_job_id` `5199732004`, de 17/08). Hard surface é o último balde
da regra 3 e **nunca carro-chefe**. E o corpo confirma: cita `character` **duas vezes e nas
duas descrevendo outra coisa** — *"a team of world-class environment, character and concept
artists"* (o TIME) e *"shipping 3D production assets for games in either character, weapon, or
prop disciplines"* (uma de três opções). O trabalho é supervisionar fornecedor. **Mesmo
veredito que a Modeling Outsource Lead derrubada às 10h45.** ID inédito, mas disciplina barra
antes do dedupe.

**Weta Workshop — Senior Technician, Molding, Props & Hair — Wellington** (`8231885`). A
palavra `hair` casou na rede, e o corpo mostra que **não é groom digital, é artesanato
físico**: *"model making, molding, fibreglassing, casting, and finishing"*, *"from sculpture
and sword-smithing to state-of-the-art robotics and CNC-based milling"*. Fora da disciplina.
Contrato fixo de outubro a dezembro.

**Weltenbauer — Tech Artist Character Animation — Wiesbaden/Remoto** (`2692704`). Cai duas
vezes: é tech art de animação (*"Du setzt Character-Animation-Systeme in der Unreal Engine
um... Animation Blueprints, State Machines"*), e tem **veto de idioma escrito** (ver §4.2).

**HyperHug — 3D Artist (weapon skins)** e **3D Environment & Prop Artist** (Ashby, remoto
mundial, estúdio de Chipre). Zero ocorrência de `character` nos dois corpos; é prop, arma e
ambiente para shooter **mobile**. Balde 3, e fraco.

**Reality Games — 3D Generalist — Cracóvia** (`1999421`). Generalista de jogo mobile que
também faz animação e motion design; cita personagem só dentro de uma lista
(*"Develop 3D city maps, environments, and characters"*). *"This is a full-time, in-office
position based in the iconic railway station building in Krakow"* — presença, não veto.
Balde 3.

**Budge Studios — Artiste 3D Généraliste — Montréal** (`26`). Generalista de jogo infantil
mobile que inclui **rigging, animação, concept 2D e UI**. E não é novidade: a campanha já
mandou carta fria em 02/09 e reconferiu o quadro em 07/09.

**Jagex — o achado de casa, com zero de vaga.** É a única casa desta varredura com **zero
menção em todo o repositório e zero mensagem no Gmail** — inédita de verdade. Li o quadro
inteiro: **20 vagas, ZERO de personagem.** A mais próxima é Environment Artist (RuneScape:
Dragonwilds). Fica anotada como casa nova e não trabalhada, para quando abrir personagem.

### 4.2 — Caiu por VETO DE IDIOMA ESCRITO (1), e ele valida a regra nova das 10h45

**Weltenbauer — Environment Artist — Wiesbaden/Remoto** (`2677880`):

> *"Mehrjährige Erfahrung als Environment Artist... **Gutes Deutsch und Englisch in Wort und
> Schrift.**"*

A irmã dela, a Tech Artist Character Animation, escreve o mesmo: *"Gute Deutsch- und
Englischkenntnisse in Wort und Schrift."*

**É exatamente o caso que a rodada das 10h45 previu.** A régua literal ganhou `German` e
`Deutsch` há duas horas, e a primeira coisa que ela pegou foi isto. Se a régua fosse a antiga,
só com `French`, as duas passariam limpas. **A ampliação dos idiomas está validada com caso
real, não em teoria.**

### 4.3 — Caiu no DEDUPE por ID de requisição (7), e duas foram salvas pela seção 3 do script

| Vaga | ID | Onde morreu |
|---|---|---|
| **TTK Games — Character Artist, Estocolmo** | `558871` (job `561860`) | **ENVIADA À MÃO em 10/09**, recibo de `ttkgames@pinpoint.email` na caixa |
| **Airship — Character Artist** (remoto global) | `8281687` | **ENVIADA 09/09 às 00h22**, recibo de `declan.blayney@airshipinteractive.teamtailor-mail.com` |
| **Airship — Groom Artist** (remoto global) | `8281721` | **ENVIADA 09/09 às 10h18** |
| **Fatshark — Character Artist, Estocolmo** | `8190501` | **ENVIADA 06/09** |
| **Beffio — Lead 3D / Senior Character Artist** | `6217989`, `7242656` | Enviadas 06/09, junto com as outras três do quadro |
| **Lighthouse Games — Lead Character Artist** | `F7F90250DA` | **ENVIADA À MÃO em 10/09**, dois recibos |
| **Kepler / Tactical Adventures — Lead 3D Character Artist** | `8311973` | Enviada 06/09 (mesma requisição em dois quadros) |
| **Rebellion — Senior Character Artist** | `331FDD9137` | **Veto escrito** + **RECUSADA em 01/09** |
| **Snowprint — Senior 3D Character Artist** | `8341580` | Veto escrito de residência em Estocolmo |
| **Riot — Principal 3D Character Artist** | `8163170` | Enviada 10/09 |
| **Absurd Ventures — Character Art Lead** | `5236256007` | Enviada hoje pelo maestro |

**A TTK e a Fatshark merecem nota de método.** As duas passaram **limpas na seção 1** do
`dedupe-agora.sh` — ID inédito nos quatro arquivos — e morreram na **seção 3**, a do nome da
casa. O ID que o quadro publica (`558871`, o *posting*) não é o ID que a candidatura registrou
(`561860`, o *job*). **Segundo argumento do script não é opcional: nestes dois casos ele foi a
única coisa entre a fila e uma candidatura repetida.**

Frase literal do veto da Rebellion, para quem a reencontrar em agregador:
> *"This role is only open to applicants who have the permanent right to work in the UK. We
> are unable to provide or take over visa sponsorship, either now or in the future."*

### 4.4 — Caiu por GEOGRAFIA (2)

- **Keywords Studios — 3D Character Artist** (`8AFF2A41AE`): o JSON-LD da fonte oficial diz
  `"addressRegion":"Metro Manila","addressCountry":"Philippines"`. Fora do recorte.
- **Keywords / Lakshya — Character Artist, Hair Specialist** (`CA33DB1208`): Índia. E já é a
  entrada **nº 32** da fila, parada por parede de Workable.
- **Epic — Modeling Outsource Lead** (`6031088004`) é **Porto Alegre**. Fora.

---

## 5. O QUE FICOU **NÃO CONFERIDO**, nomeado — porque resposta vazia não é zero

Nove quadros dos 322 **não responderam**, e nenhum deles virou zero na planilha:

| Quadro | O que aconteceu |
|---|---|
| `workable/supermassivegames` | **HTTP 429** do Cloudflare |
| `teamtailor/liquidswords` | 301 para `careers.liquidswords.com`, e o domínio **não responde** (código 000) |
| `teamtailor/impact` | 301 para `careers.impactmr.com`, idem |
| `teamtailor/house`, `mobile`, `rhino`, `united` | **HTTP 403** (e são tokens genéricos, provável falso positivo de extração) |
| `pinpoint/trust` | resposta não-JSON |
| `recruitee/careers-analytics` | **HTTP 403** |

**Duas pendências de corpo, e elas são a herança desta rodada para a próxima:**
**Keywords `1A851A0286` (Character Artist)** e **`70A14A1A2F` (3D Hair Artist)** — títulos
lidos, **IDs inéditos nos quatro arquivos**, e **corpo e localização NÃO CONFERIDOS**: o
`apply.workable.com` passou a devolver **429 em tudo** no meio da rodada, e continuou em 429
depois de esperas de 45s, 120s e 10min. O site corporativo da Keywords só expõe duas vagas de
personagem, as duas já resolvidas (Manila e Índia), então estas duas **podem ser de outra
marca do grupo**. **Não conclua zero sobre elas.**

**Quatro domínios de Teamtailor com slug 404 que também não resolvem:**
`careers.ghostshipgames.com`, `careers.keengames.com`, `careers.gamecan.com`,
`careers.invisiblewalls.dk`. `careers.radicalforge.com` responde 200 e diz não ter posições
abertas agora — este é zero de verdade.

**Um zero que eu não assino sozinho:** `playground-games.pinpointhq.com` devolve
`{"data":[]}` — resposta viva e vazia — e `playground-games.com/careers` é SPA que não monta
por curl. Pela regra de 12/09 (o caso NBCUniversal, em que o quadro bom era `NBCUniversal1`),
**casa grande com quadro zerado é suspeita de token errado, não prova de casa sem vaga.**

---

## 6. O QUE ESTA RODADA MEDIU E A PRÓXIMA NÃO PRECISA REFAZER

1. **Os 290 quadros fora do censo, lidos e gravados** em `quadros-fora-censo-1209.csv`.
   2.199 vagas. A lista dos 173 pendentes **não existe mais**.
2. **Os 32 Teamtailor do censo, remedidos com o leitor consertado.** 167 vagas, zero
   personagem não trabalhada.
3. **O leitor de Teamtailor está consertado** e o conserto está descrito no commit e aqui.
   Quem for varrer Teamtailor: aceite `href` absoluto em **qualquer** domínio.
4. **BambooHR: seis contas encerradas**, e isso é resposta, não falha —
   `archiactinteractive`, `hyperhippo`, `hashbane`, `houseofcool`, `snowball`, `wgames` devolvem
   **302 para `www.bamboohr.com`**, que é o que a plataforma faz quando a conta some.
5. **Jagex é casa inédita na campanha** (zero no repositório, zero no Gmail), quadro de 20
   vagas lido inteiro, **zero de personagem**.
6. **Workable está em 429 global contra este IP**, não só em `apply.` — o índice
   `jobs.workable.com/api/v1/jobs` responde
   *"rate_limit ... contact us to be given access to our jobs XML feed"*. Continua fila da mão
   dele.
7. **Grupo Disney NÃO foi tocado**, e de propósito: o maestro mediu às 11h46 com
   `ronda-disney.sh`, 12 de 12 consultas responderam, zero ID novo.

---

## 7. COMO ISTO FOI RODADO

`python3` com `requests`, 8 a 12 trabalhadores, uma linha de CSV por quadro. Ordem: (1)
extração de todos os tokens de ATS das URLs de 798 arquivos do repositório e cruzamento com o
censo; (2) consulta dos 290 pela API oficial de cada família; (3) conferência manual de um
quadro que devolveu zero, que foi o que descobriu o erro do leitor; (4) reconstrução do leitor
de Teamtailor e revarredura dos 119; (5) revarredura dos 32 do censo pelo mesmo motivo; (6)
rede larga de disciplina sobre as 2.366 vagas; (7) leitura do **corpo integral** de cada
finalista pela fonte oficial, com a régua termo a termo e a frase transcrita; (8)
`dedupe-agora.sh` por ID **com o nome da casa**, mais conferência no **Gmail por janela de
tempo**; (9) os que sobraram foram medidos contra a regra do Vini de 10/09.

Arquivos escritos por esta rodada: **este**, `automacao/quadros-fora-censo-1209.csv` e uma
linha em `automacao/processados.csv`. `enviados.csv`, `docs/index.html` e
`automacao/FILA-DO-VINI.md` **não foram tocados** — a fila não mudou porque não havia o que
pôr nela.
