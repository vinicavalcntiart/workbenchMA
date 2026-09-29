# Censo de quadros — DIFF 07/09 → 08/09

Recoleta feita em 08/09/2026 (noite), mesmos tokens do `censo-boards-0709.csv`, tudo por `curl`,
concorrência máxima de 6. Censo novo em `automacao/censo-boards-0809.csv` (arquivo novo; o de 07/09
não foi tocado).

---

## RESULTADO EM UMA LINHA

**1 (uma) requisição nova, da disciplina, dentro do escopo e sem veto escrito.**
GIANTS Software — *Junior 3D Artist - Vehicle specialist*, Brno (Chéquia). Régua dos 17: **0 de 17**.

**Regra 14 (Disney / DreamWorks / Paramount / Warner): nada novo hoje.** Detalhe e prova abaixo,
porque quase virou um falso positivo meu.

---

## 1. NÚMEROS

### Tokens

| | |
|---|---|
| Tokens no censo de 07/09 | **123** |
| Tokens lidos hoje com HTTP 200 | **123** |
| Tokens que falharam | **0** |

Distribuição: greenhouse 31, teamtailor 32, bamboohr 20, smartrecruiters 14, lever 12, ashby 6,
recruitee 5, breezy 3.

Duas observações de honestidade sobre o escopo:

- O briefing citou **seis** ATS. O `censo-boards-0709.csv` na verdade tem **oito**: além dos seis,
  `recruitee` (65 linhas, 5 tokens) e `breezy` (38 linhas, 3 tokens). Refiz esses dois também, por
  rotas fora da lista que você passou (`https://<token>.recruitee.com/api/offers/` e
  `https://<token>.breezy.hr/json`). Ambas responderam 200. Estão contadas nos totais.
- Todos os 12 tokens do Lever resolveram em `api.lever.co`. Testei `api.eu.lever.co` nos 12 e os 12
  devolveram **404** — nenhum token europeu de fato hospedado na instância UE.

### Requisições

| | 07/09 | 08/09 |
|---|---|---|
| Linhas totais | 2.791 | **3.588** |
| Linhas no universo comparável (ver §2) | 2.491 | **2.489** |

| | |
|---|---|
| Entradas brutas por ID (existe hoje, não existia em 07/09) | 863 |
| — destas, **artefato de censo truncado** em 07/09 (§2) | **771** |
| **Entradas reais** | **92** |
| **Saídas** (existia em 07/09, sumiu hoje) | **66** |

### Funil das 92 entradas reais

| Etapa | Sobra |
|---|---|
| Entradas reais | 92 |
| ...da disciplina dele | **2** |
| ...dentro do escopo geográfico | **1** |
| ...sem veto escrito (régua dos 17) | **1** |

---

## 2. O ACHADO METODOLÓGICO QUE MUDA A LEITURA DO DIFF

**O censo de 07/09 está truncado em três tokens do SmartRecruiters.** `mattelinc`, `nbcuniversal3` e
`ubisoft2` têm **exatamente 100 linhas cada** no arquivo de 07/09 — a marca do `limit=100` sem
paginar o `offset`.

Hoje, paginando até o `totalFound` que a própria API devolve:

| Token | Linhas em 07/09 | `totalFound` hoje |
|---|---|---|
| mattelinc | 100 | **443** |
| nbcuniversal3 | 100 | **372** |
| ubisoft2 | 100 | **284** |

Comparação crua de IDs acusaria **812 "vagas novas"** nesses três tokens. Quase todas estavam lá em
07/09, apenas depois do corte do offset 100.

**Como desempatei sem chutar:** o SmartRecruiters publica `releasedDate` por requisição. Filtrando os
812 por `releasedDate >= 2026-09-07`, sobram **41** de fato publicadas desde o censo anterior. As
outras **771** são artefato e estão excluídas da contagem de entradas.

Retirando os três tokens dos dois lados, o universo comparável é **2.491 (07/09) contra 2.489 (08/09)**
— confirma que o resto do censo bate e que o salto de 2.791 para 3.588 é paginação, não mercado.

Nenhuma das 41 entradas reais desses três tokens é da disciplina dele: são engenharia, finanças, RH,
jurídico, produção, *game design*, *level design*, animação de gameplay e VFX.

---

## 3. REGRA 14 — DISNEY / DREAMWORKS / PARAMOUNT / WARNER

**Nada novo hoje nesses quatro estúdios.** Mas registro o quase-erro, porque o número teria sido outro.

Varri hoje e o censo de 07/09 atrás de `disney|dreamworks|paramount|warner`. A comparação crua de IDs
apontava como "nova" a seguinte:

> **DreamWorks Feature — Character Effects Artist** — Glendale, CA
> `smartrecruiters` / `nbcuniversal3` / id `744000145325278`

Ela **não é nova**. O `releasedDate` da própria API é **2026-08-24T16:36:55Z** — estava publicada
duas semanas antes do censo de 07/09, e só não aparece no arquivo antigo porque caiu depois do corte
do offset 100 do `nbcuniversal3`. É exatamente o artefato do §2. Não subiu para o topo do relatório
como achado novo, e não está na lista de entradas.

Outras ocorrências dos quatro nomes, todas **já presentes em 07/09** e portanto fora do diff:
`DreamWorks Technology - Web Tools Engineer` (engenharia, fora da disciplina) e
`Content Producer - Disney` na Fanatics (produção, fora da disciplina).

---

## 4. A VAGA NOVA

### GIANTS Software — Junior 3D Artist - Vehicle specialist

| Campo | Valor |
|---|---|
| **Estúdio** | GIANTS Software GmbH (série *Farming Simulator*) |
| **Local** | Brno, South Moravian Region, **Chéquia** |
| **ATS** | SmartRecruiters — token `giantssoftwaregmbh` |
| **ID da requisição** | `744000148212939` |
| **Publicada em** | **2026-09-08T11:38:20Z** (hoje) |
| **Link de candidatura** | https://jobs.smartrecruiters.com/GIANTSSoftwareGmbH/744000148212939-junior-3d-artist-vehicle-specialist?oga=true |
| **Formato** | Efetiva (`typeOfEmployment: permanent` / Full-time). **Presencial** — a API traz `remote: false` e `hybrid: false` |
| **Nível** | Título diz "Junior", mas o campo estruturado da vaga diz `experienceLevel: mid_senior_level` |
| **Função declarada** | `Art/Creative`, indústria `Computer Games` |
| **Faixa salarial** | **Não publicada.** O texto diz apenas "attractive salary, bonuses" — sem número, sem moeda |

**Por que é da disciplina dele** (citando o anúncio): *"Precise 3d asset production of all kinds of
agricultural machinery"*, *"Great skills in **hard-surface modeling**"*, *"Ability to create realistic
3D assets and **textures** in high quality"*, *"Experience with **PBR workflow**"*, *"Experience with
**Substance Designer / Painter** or 3D Coat"*, *"Good knowledge of **Autodesk Maya**"*.
Modelagem 3D + hard surface + texturização. Cai em cheio.

Pede portfólio: *"Candidates must provide a resume and a portfolio or references to be considered for
the position."*

#### Régua dos 17 termos — resultado literal

Rodei sobre **dois** textos independentes: (a) o corpo completo do anúncio pela API
(`jobAd.sections` — as quatro seções: `companyDescription`, `jobDescription`, `qualifications`,
`additionalInformation`, 2.363 caracteres) e (b) o HTML da página pública renderizada em texto
(2.893 caracteres).

| # | Termo | Resultado |
|---|---|---|
| 1 | `authoriz` | não casou |
| 2 | `eligib` | não casou |
| 3 | `sponsor` | não casou |
| 4 | `work permit` | não casou |
| 5 | `must be based` | não casou |
| 6 | `based in` | não casou |
| 7 | `only from` | não casou |
| 8 | `LMIA` | não casou |
| 9 | `days a week` | não casou |
| 10 | `days per week` | não casou |
| 11 | `days in the office` | não casou |
| 12 | idioma local (`French`, `français`, `Deutsch`, `German language`, `svenska`, `polski`) | não casou |
| 13 | `resident` | não casou |
| 14 | `relocat` | não casou |
| 15 | `located in` | não casou |
| 16 | `unable to support` | não casou |
| 17 | `no relocation` | não casou |

**0 de 17 nos dois textos.** Nenhuma frase para colar: não há veto escrito, e também **não há frase a
favor** — o anúncio não menciona realocação em nenhum sentido. Exige inglês B2 (*"Very good knowledge
of English at least at level B2"*), e não pede tcheco nem alemão.

Também verifiquei a página pública contra o truque de hoje: **zero caracteres Unicode invisíveis**
(varredura de U+200B–U+200F, U+FEFF e tags U+E0000–U+E007F). Nenhuma instrução escondida.

#### Dedupe — a requisição é nova, o estúdio não é

Feito pela **referência da requisição**, como mandado:

1. **ID `744000148212939` contra `censo-boards-0709.csv`** — ausente.
2. **Nome do estúdio contra os arrays `PORTAIS`/`STUDIOS` do `docs/index.html`** — `GIANTSSoftwareGmbH`
   **está** no painel. O estúdio já é conhecido; **esta requisição não**.
3. **`enviados.csv`** — nenhuma linha para GIANTS Software. Atenção ao homônimo: as duas linhas que
   casam com "giants" são da **GIANTSTEP** (`jobs@giantstep.co.kr`, Coreia do Sul), estúdio diferente,
   e uma delas voltou *bounce*.
4. **`automacao/processados.csv`** — o ID `744000148212939` não aparece; as ocorrências de "giants"
   são de outras requisições/estúdios.

Conclusão: **requisição nova em estúdio já mapeado.**

---

## 5. AS OUTRAS DUAS QUE CHEGARAM PERTO E POR QUE CAÍRAM

**Gameloft — 3D General Artist** — `smartrecruiters` / `gameloft` / id `744000148170394`, publicada
hoje. **É** da disciplina (generalista 3D). Caiu na **geografia**: `Hanoi, Vietnam`
(`hybrid: true`, "Max 3 days WFH/Week", ou seja presencial no Vietnã). Ásia só vale Coreia do Sul e
Singapura. **Descartada por escopo, não por veto** — não rodei os 17 termos nela.

**Fanatics Collectibles — Art Director** — `greenhouse` / `fanaticscollectibles` / id `4397677009`,
Londres, `updated_at` 2026-09-08. Puxei o texto integral para decidir e **não é liderança de arte 3D**:
*"Art Directors at The Topps Company/Fanatics Collectibles are the captains of our **graphic design**
team, steering products and leading team members in the creation of all visual elements for our
**trading card** and collectibles business. As veteran **graphic designers**..."*. É direção de arte
gráfica 2D para cartas colecionáveis. **Descartada por disciplina.** (Também conferi a "Vulcan Lead"
da mesma casa: é chefia de operação de máquina de aplicação de foil cromado em cartas — nada a ver.)

---

## 6. AS 66 SAÍDAS — QUAIS QUADROS GIRAM RÁPIDO

Por ATS: greenhouse 29, smartrecruiters 24, lever 6, teamtailor 3, bamboohr 2, ashby 1, recruitee 1.

Giro por token (saídas ÷ base de 07/09), só tokens com base ≥ 10:

| ATS | Token | Saídas / base | Giro |
|---|---|---|---|
| smartrecruiters | peoplecanfly | 2 / 16 | **12,5%** |
| smartrecruiters | rodeofx | 3 / 30 | **10,0%** |
| smartrecruiters | gameloft | 4 / 42 | 9,5% |
| ashby | volka | 1 / 12 | 8,3% |
| smartrecruiters | nbcuniversal3 | 8 / 100 | 8,0% |
| lever | skydance | 2 / 31 | 6,5% |
| lever | avalanchestudios | 1 / 16 | 6,2% |
| lever | bhvr | 2 / 39 | 5,1% |
| lever | neowiz | 1 / 22 | 4,5% |
| smartrecruiters | cdprojektred | 2 / 44 | 4,5% |
| greenhouse | wargamingen | 2 / 48 | 4,2% |
| teamtailor | untoldstdfg1324556 | 1 / 24 | 4,2% |
| bamboohr | iconcreative | 1 / 28 | 3,6% |
| greenhouse | scopely | 6 / 177 | 3,4% |

Leitura: quem gira rápido em 24h é o bloco SmartRecruiters de serviço/terceirização
(People Can Fly, Rodeo FX, Gameloft) e o Lever dos estúdios médios. Os quadros grandes de Greenhouse
(roblox 230, hasbro 159, scopely 177) são estoque parado — muita linha, pouquíssimo movimento diário.
Se for para revisitar diariamente, vale a pena o SmartRecruiters e o Lever; Greenhouse grande dá para
espaçar.

**Duas saídas eram da disciplina dele:**

- `greenhouse` / `scopely` — **Senior/Lead 3D Character Artist - WWE Champions**, IN - Bangalore,
  Índia. Estava fora do escopo geográfico de qualquer forma.
- `lever` / `skydance` — **Senior Environment Surfacing Artist**, Madrid. Esta **estava no escopo** e
  fechou. Se ainda não foi trabalhada, a janela passou.

---

## 7. RESSALVAS, PARA NÃO INFLAR

- **Nada foi commitado, enviado ou preenchido.** Nenhum navegador aberto — tudo `curl`.
- **Nenhum item `precisa-de-navegador` nesta rodada.** Os 123 tokens cederam por API/HTTP.
- Três entradas do Lever (`bhvr` *Player Lifecycle Director*, `dreamgames` *DevOps Engineer*,
  `jamcity` *Senior User Acquisition Specialist*) têm `createdAt` antigo (2026-06-23, 2023-07-07 e
  2025-09-10). Entraram no *quadro* desde 07/09, mas não são requisições recém-criadas — são
  republicações. Nenhuma é da disciplina, então não muda o resultado.
- Os 41 itens realmente novos dos três tokens truncados foram lidos um a um por título e local; nenhum
  é da disciplina. Não puxei texto integral deles porque nenhum passou da triagem de disciplina — e a
  régua dos 17 só se aplica a vaga que eu fosse reportar.
- O `disciplina_vini` do `censo-boards-0809.csv` é uma **triagem automática por título** para permitir
  o próximo diff, não um julgamento vaga a vaga. Os julgamentos manuais desta rodada estão nos §4 e §5.
- O `ja_no_painel` no CSV novo herda o valor de 07/09 quando o ID já existia, e recebe `nova` quando
  o ID é inédito no arquivo antigo.

---

## 8. VEREDITO

Rodada honesta de **uma** vaga nova. O quadro de 08/09 contra o de 07/09 é quase estático na
disciplina dele: 92 requisições realmente entraram nos 123 quadros em 24 horas, e **duas** eram de
arte 3D — uma no Vietnã (fora), uma em Brno (dentro, sem veto).

A entrega prática do dia é uma vaga e uma correção de método: **o censo de 07/09 subestima em ~800
linhas** por causa dos três tokens truncados do SmartRecruiters. O `censo-boards-0809.csv` já está
paginado até o fim e serve de base íntegra para o próximo diff.
