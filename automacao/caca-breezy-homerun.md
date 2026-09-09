# CAÇA A QUADROS: BREEZY, HOMERUN, JOIN.COM E SOFTGARDEN — 09/09/2026 (madrugada)

Tudo por `curl`. Nenhum navegador aberto, nenhum formulário preenchido, nenhum commit, nenhum email.
Nada foi editado em `docs/index.html`, `FILA-DO-VINI.md`, `enviados.csv` ou `automacao/processados.csv`.

---

## 1. OS NÚMEROS, ANTES DE QUALQUER NARRATIVA

| família | slugs testados | quadros vivos | vagas no total | da disciplina | passaram no escopo | passaram na régua | passaram no dedupe |
|---|---|---|---|---|---|---|---|
| **Breezy** | 3.635 | **51** | 77 | **10** | 10 | 5 | **2** |
| **Homerun** | 3.521 | 3 | 1 | 1 (porta espontânea) | 1 | 1 | **0** |
| **Join.com** | 3.521 | 66 | 4 | 0 | — | — | **0** |
| **Softgarden** | 3.521 | 11 | (ver §5) | 0 | — | — | **0** |
| **TOTAL** | **14.198 requisições de sonda** | **131** | 82 | 11 | 11 | 6 | **2** |

**A fila limpa tem DUAS linhas, e só UMA delas eu recomendo clicar.** Escrevo isso de propósito: o
rendimento honesto destas quatro famílias, para esta disciplina e este escopo, é baixo. O que sobrou
está no §2. O que morreu e por quê está no §3 e no §4 — e o §3 é a parte que mais vale a sua leitura,
porque quatro títulos perfeitos da AGBO morrem no rodapé.

---

## 2. FILA PRONTA PARA CLICAR

### LINHA 1 — CLICAR (única candidatura de verdade desta rodada)

| campo | valor |
|---|---|
| **estúdio** | Walla Walla Studio |
| **cargo** | 3D Environment/Tech artist (Unity) |
| **país/cidade** | Estúdio em Kyiv, UA — **anúncio marcado `REMOTE_ANY` (remoto de qualquer lugar)** |
| **URL de candidatura** | `https://wws.breezy.hr/p/f1578014d426-3d-environment-tech-artist-unity/apply` |
| **URL do anúncio** | `https://wws.breezy.hr/p/f1578014d426-3d-environment-tech-artist-unity` |
| **id da requisição** | `f1578014d426` (Breezy) |
| **formato** | **Contrato / temporário**, remoto, nível Mid/Senior. Pagamento **em USD/EUR**, e o anúncio pede que você **indique a taxa por hora desejada** |
| **faixa publicada** | Não. O campo `salary` do Breezy vem vazio e o anúncio inverte o ônus: *"Please send your Portfolio and CV and indicate the desired rate per hour."* |
| **régua de veto** | **ZERO dos 17 termos casou.** Rodei os 17 mais a lista de idioma local sobre o texto integral (2.141 caracteres extraídos): nenhuma ocorrência de `authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `based in`, `only from`, `LMIA`, `days a week`, `days per week`, `days in the office`, `resident`, `relocat`, `located in`, `unable to support`, `no relocation`, nem exigência de ucraniano ou de qualquer idioma. É um anúncio limpo. |
| **dedupe** | **FEITO E LIMPO.** `grep` do id `f1578014d426` em `docs/index.html`, `enviados.csv` e `automacao/processados.csv`: **0, 0 e 0**. Também conferi por nome (`Walla Walla`) e por host (`wws.breezy`): **0, 0 e 0** nos três arquivos. Estúdio novo na campanha. |
| **captcha** | A página `/apply` responde 200 e o HTML **não traz** `recaptcha`, `hcaptcha` nem `turnstile`. Deve ser preenchimento direto. |

**RESSALVA HONESTA DE ENCAIXE, e ela é grande.** Isto é **ambiente**, que conta pela regra de
disciplina, mas é ambiente **fotorrealista em Unity com peso técnico**: o anúncio pede portfólio
"in a photorealistic style in Unity", Quixel, Speedtree, e a lista de tarefas é iluminação,
post-processing, otimização de draw calls, contagem de polígonos, memória de textura, LOD groups e
imposters. O portfólio dele é **personagem estilizado**. Não é outra disciplina, é outro registro
dentro dela, e o encaixe é **fraco**, não médio. Some a isso que é **contrato por hora, não efetivo**.
Mando mesmo assim porque é a única porta desta rodada que passou nas três peneiras, o estúdio é
full-cycle de arte (o próprio texto diz que fazem "high-end 3D characters" para clientes do mundo
inteiro), e a porta é remota sem uma linha de exigência de autorização de trabalho — o que é raro.
**Se você só tiver fôlego para um clique hoje, este é o clique.**

---

### LINHA 2 — NÃO RECOMENDO CLICAR (fica registrada porque o dedupe deu limpo e a decisão é sua)

| campo | valor |
|---|---|
| **estúdio** | Playdead |
| **cargo** | Speculative Applications (candidatura espontânea) |
| **país/cidade** | Dinamarca (Copenhague), presencial |
| **URL de candidatura** | `https://playdead.breezy.hr/p/fbda7a56839001-speculative-applications/apply` |
| **id da requisição** | `fbda7a56839001` (Breezy) |
| **formato** | Efetivo, presencial no escritório de Copenhague |
| **faixa publicada** | Não |
| **régua de veto** | **Nenhum veto de verdade.** Único casamento: `based in` em *"We're Playdead, an independent game company **based in** the heart of Copenhagen, Denmark"* — **falso positivo**, é o endereço do estúdio. O anúncio ainda pede *"You should be willing to work at the Playdead office in Copenhagen, Denmark"*, que é onde o cargo fica, não uma barreira de nacionalidade. |
| **dedupe** | **FEITO E LIMPO.** `grep` do id `fbda7a56839001` nos três arquivos: **0, 0 e 0.** |

**POR QUE MESMO ASSIM EU SEGURO.** A régua e o dedupe passam, mas o contexto reprova: você tem
**duas candidaturas vivas na Playdead com três dias de diferença** — a Experienced Material and
Texture Artist (`d6b5a5e4f54a01`) em 06/09 e a 3D Environment Artist (`a235c228566a01`) em 08/09
às 23h58. Uma terceira batida na mesma porta, agora genérica e sem vaga, em menos de 72 horas, não
adiciona sinal: adiciona ruído no mesmo inbox que já tem duas peças suas com carta e portfólio.
Espontânea vale quando a casa **não** tem vaga da disciplina aberta; a Playdead tem, e você já
mandou nas duas. **Guarde esta linha para o dia em que as duas forem respondidas ou morrerem.**

---

### FRASE A FAVOR — O OURO DA RODADA (destaque pedido)

A Playdead escreve, com todas as letras, no anúncio da **3D Environment Artist** (`a235c228566a01`,
que você enviou às 23h58 de 08/09):

> **"You should be willing to work at the Playdead office in Copenhagen, Denmark. We can offer relocation and visa support if required."**

Confirmei a frase hoje na fonte, no texto integral baixado do próprio `playdead.breezy.hr`. Ela
**continua no ar** e é a única frase pró-realocação que apareceu nas 82 vagas destas quatro famílias.
A Warhorse tem a segunda melhor, e ela também é pró (§3).

---

## 3. O QUE MORREU NA RÉGUA DE VETO — texto integral baixado, frase colada

### AGBO — quatro títulos perfeitos, quatro vetos no rodapé

A AGBO tem **19 vagas** vivas e **quatro** batem a disciplina. As quatro morrem. Baixei o texto
integral de cada uma e colo a frase:

| id | cargo | local | frase que mata |
|---|---|---|---|
| `9428cd65e2b4` | Expression of Interest - Asset Artist | Los Angeles, CA | *"Candidates must be legally authorized to work in the U.S. without the need for sponsorship."* |
| `49a139476416` | Expression of Interest - Character Artist | Los Angeles, CA | *"Candidates must be legally authorized to work in the U.S. without the need for sponsorship."* |
| `477c5544f2b1` | Expression of Interest - Unreal Environment Artist | Los Angeles, CA | *"Candidates must be legally authorized to work in the U.S. without the need for sponsorship."* |
| `cdc4c6df4fd8` | Senior Character Texture Artist | Raleigh, NC | *"Candidates must be legally authorized to work in the U.S."* |

**Classificação: VETO DE VERDADE nas quatro.** Casaram `authoriz` e `sponsor`. Nota de precisão que
vale registrar: a de Raleigh (`cdc4c6df4fd8`) usa a versão **curta** — só *"must be legally authorized
to work in the U.S."*, **sem** a cláusula "without the need for sponsorship". É um veto mais fraco no
papel, mas continua sendo exigência escrita de autorização de trabalho sem oferta de patrocínio, e a
regra é a regra: veto escrito desqualifica. Confirma na íntegra o que você já tinha achado hoje.

Falso positivo descartado nas quatro: `spanish` casou em *"AGBO participates in E-Verify - English | Spanish"*,
que é o rodapé legal do E-Verify e não exigência de idioma. Na Unreal Environment Artist, `polish`
casou dentro de *"from initial blackout to final **polish**/ship"* — palavra inglesa, não o idioma polonês.

Fora da disciplina na mesma AGBO, e por isso nem entraram na conta: Rigging Artist, FX Artist,
Technical Artist, Lead Technical Artist, Lead VFX Artist, Sr. Cinematic Layout Artist.

### Warhorse Studios — Level Artist: veto de idioma local, explícito e no topo

- **id** `5e0abb1243c101` — Level Artist, Praga, CZ, efetivo.
- Disciplina: **conta** (ambiente/level art).
- **VETO DE VERDADE**, e é a primeira linha do anúncio:

> **"This position is available only to Czech-speaking candidates"**

E o corpo inteiro do anúncio está escrito em tcheco (*"Co budeš dělat?"*, *"Co od tebe očekáváme?"*).
Dedupe do id deu **0, 0, 0** — ou seja, é vaga nova que ninguém tinha visto —, mas o dedupe limpo não
salva vaga vetada. **Não enviar.**

### Warhorse Studios — Open Application: frase A FAVOR, mas já enviada

- **id** `fabe03688c9401`.
- Casou `based in` e `czech` em: *"If you want to create wonderful games with us and if you are willing
  to be **based in** Prague, Czech Republic, be sure to get in touch with us, **no matter what your
  nationality**."*
- **Classificação: FRASE A FAVOR**, não veto. "No matter what your nationality" é declaração explícita
  de neutralidade de nacionalidade, e "willing to be based in Prague" diz onde o CARGO fica, não onde
  o candidato precisa já estar.
- **DEDUPE SUJO:** o id `fabe03688c9401` aparece em `docs/index.html` (1 linha) e em
  `automacao/processados.csv` (1 linha). Foi **enviada e confirmada em 06/09** — *"Application
  Submitted, your application has been submitted successfully"*, POST 204. **Não reenviar.**

### Playdead — as duas vagas de verdade: dedupe sujo nas duas

| id | cargo | dedupe |
|---|---|---|
| `a235c228566a01` | 3D Environment Artist | **SUJO.** `docs/index.html` 2 linhas, `enviados.csv` 1 linha, `processados.csv` 1 linha. Enviada 08/09 às 23h58, POST 204 em `app.breezy.hr/api/apply/a235c228566a01`. |
| `d6b5a5e4f54a01` | Experienced Material and Texture Artist | **SUJO.** `docs/index.html` 2, `enviados.csv` 1, `processados.csv` 1. Enviada 06/09. |

Nenhuma das duas tem veto: o único casamento é `based in` no endereço do estúdio, falso positivo, e a
de Environment ainda traz a frase pró-realocação do §2.

### Total Mayhem Games (Homerun) — a única porta da família Homerun, e ela já foi batida

- **URL** `https://totalmayhemgames.homerun.co/open-application`, candidatura em
  `https://totalmayhemgames.homerun.co/open-application/en/apply`.
- Rotterdam, Holanda — dentro do escopo. Não é vaga da disciplina: é pool de talentos genérico, e o
  próprio texto avisa *"we unfortunately don't have the capacity to follow up directly with everyone who applies"*.
- Régua: único casamento é `based in` em *"Total Mayhem Games Studios, **based in** Rotterdam"* —
  **falso positivo**, endereço do estúdio. Sem veto.
- **DEDUPE SUJO, e é o caso mais caro da rodada:** `totalmayhemgames` aparece em `docs/index.html` (2),
  `enviados.csv` (1) e `processados.csv` (1). A campanha **já enviou por esta exata porta Homerun em
  06/09**, e em **07/09 a casa RESPONDEU RECUSANDO**, com a carta registrada em `processados.csv`:
  *"We appreciate the time and effort you put into your application"*, dizendo que **não há vaga**.
  Reenviar seria a segunda batida numa porta que já respondeu não por escrito. **Não enviar.**

---

## 4. FALSOS POSITIVOS QUE EU DESCARTEI (para você não refazer a leitura)

- `based in` no endereço do estúdio: Playdead ×3, Total Mayhem ×1. Todos descartados.
- `based in` dizendo onde o CARGO fica, com neutralidade de nacionalidade dita na mesma frase:
  Warhorse Open Application. Descartado, e vira frase a favor.
- `polish` como "polimento" e não idioma polonês: AGBO Unreal Environment Artist.
- `spanish` no rodapé do E-Verify (*"AGBO participates in E-Verify - English | Spanish"*): AGBO ×4.
- Nenhuma ocorrência, em nenhum dos onze anúncios lidos, de `days a week`, `days per week`,
  `days in the office`, `LMIA`, `must be based`, `only from`, `work permit`, `unable to support`,
  `no relocation`, `located in` nem `resident`.

---

## 5. QUADROS VIVOS MAS VAZIOS — a lista de vigia mais útil desta rodada

Estes são **51 quadros Breezy vivos** (HTTP 200 no `/json`, confirmado com três tentativas cada para
matar resultado transitório). **38 estão vivos com ZERO vaga publicada.** Não são parede, não são
domínio morto: são portas abertas de estúdios reais que hoje não têm nada no ar. Vale voltar nelas.

**Estúdios reais da nossa área, quadro vivo e vazio hoje (09/09):**

`axis-studios` (Axis Studios) · `big-shot-pictures` (Big Shot Pictures) · `bohemia-interactive`
(Bohemia Interactive) · `cloud-imperium-games` (Cloud Imperium Games) · `cold-iron-studios`
(Cold Iron Studios) · `fin-design-effects` (Fin Design + Effects) · `grinding-gear-games`
(Grinding Gear Games) · `gunzilla-games` (Gunzilla Games) · `land-sea` (Land & Sea Games) ·
`raid-base-inc` (Raid Base Inc) · `roblox` (Roblox) · `sadfish-inc` (SadFish Inc.) ·
`stormind-games` (Stormind Games) · `sunblink` (Sunblink) · `tat` (TAT) · `world-makers-ltd`
(World Makers) · `possible-inc` (Possible, Inc.) · `tangent` (Tangent) · `pipeline` · `ingenuity` ·
`amuse` · `aruma` · `giant` · `mighty` · `relish` · `trust` · `unfold` · `alta` · `axis` · `one` ·
`random` · `meta` · `amazon` · `media` (Infytel Communications) · `hello`

**Confirmação importante:** a busca na web ainda indexa anúncios destes quadros — Cold Iron Studios
"Senior Character Artist", Land & Sea Games "Contract 3D Character Artist", Raid Base "3D Artist,
Generalist", World Makers "3D Character Artist". **Todos já saíram do ar.** Conferi de duas formas:
o `/json` do quadro devolve lista vazia, e a página HTML do quadro devolve **zero** links `/p/`
(controle: o mesmo comando na AGBO devolve 19). Resultado de busca **não é vaga viva**, e estas quatro
são a prova. `metaverse-game-studios` e `tinybuild`, que a busca também apontava com vaga da
disciplina, dão **404** no quadro inteiro: fecharam a conta Breezy.

**Quadros vivos e vazios nas outras famílias:**
- **Homerun:** `twinswans` (Twin Swans) — **e isto resolve uma pendência antiga do painel.** O painel
  registrava a Senior 3D Character Artist da Twin Swans como "NÃO CONFIRMADA desde 30/08" porque o
  proxy bloqueia `twinswans.com`. Achei a porta que não estava bloqueada: `twinswans.homerun.co`
  responde 200, o feed oficial `feed.homerun.co/twinswans` devolve **zero `<entry>`**, e o HTML do
  quadro tem **zero** link de vaga. **A vaga não existe mais. Pode fechar a pendência.**
- **Join.com, quadro vivo e zero vaga publicada, todos estúdios reais:** `deck13` (DECK 13 Interactive),
  `scanline` (ScanlineVFX), `embark` (Embark), `keywordsstudios` (Keywords Studios Berlin),
  `klang-games`, `wooga`, `popcore`, `chimera-entertainment`, `traviangames`, `beamng`, `arxanima`
  (arx anima, Viena), `hyperluminal` (Hyper Luminal, Dundee), `microids`, `parasol-island`,
  `dream-machine`, `galaxy-grove`, `urbangames`, `elysium-studios`, `aaagameartstudio`,
  `unfold`, `frima`, `magoproduction`, `redthread`, `spectral`, `savian`, `cirrus`, `gamehouse`.
- **Softgarden:** 11 quadros vivos e **nenhum** da nossa área com vaga. `techland.softgarden.io`
  existe e responde, **mas o conteúdo é lixo de teste de 2022** — as vagas listadas são "Test 3",
  "Smile Maker", "HR Business Partner", "Project Manager", todas datadas de março/abril de 2022 e
  todas na categoria HR. A Techland não recruta mais por ali. `territory.softgarden.io` é a
  **TERRITORY GmbH**, agência de marketing de conteúdo da Bertelsmann, **não** a Territory Studio de
  VFX — homônimo. `bacon.softgarden.io` redireciona para `igoindustries.softgarden.io` (IGO
  Industries GmbH), também homônimo, não o estúdio de animação dinamarquês.

---

## 6. MÉTODO — o que eu rodei, para você poder repetir ou desconfiar

**Rotas usadas, todas por `curl`, nenhuma exceção:**
- Breezy: `https://<slug>.breezy.hr/json` (JSON limpo com id, nome, local, tipo e url de cada vaga),
  anúncio em `https://<slug>.breezy.hr/p/<friendly_id>`, candidatura em `<url do anúncio>/apply`.
- Homerun: `https://<slug>.homerun.co/` mais o feed Atom oficial `https://feed.homerun.co/<slug>`,
  que é a fonte confiável — o HTML do quadro é montado por JS e engana a leitura.
- Join.com: `https://join.com/companies/<slug>`, com as vagas dentro do `__NEXT_DATA__` da página,
  em `props.pageProps.initialState.jobs.items` (e `jobs.pagination.total` diz quantas há de verdade).
- Softgarden: `https://<slug>.softgarden.io/`, que redireciona para `/<lang>/vacancies` quando vivo.

**Controle negativo, rodado ANTES de tudo, para não confundir "vazio" com "inexistente":**
slug falso `zzqqxxnotreal` devolve **404 limpo nas quatro famílias**. Sem esse controle, o `302` do
Softgarden e o `302` do Homerun seriam lidos ao contrário — no Softgarden o **302 é quadro VIVO**
(redireciona para `/en/vacancies`) e o 404 é inexistente; no Homerun é o inverso, **200 é vivo** e o
302 leva para `404.homerun.co`.

**Slugs, com e sem hífen, sempre.** Gerei 3.521 slugs a partir dos nomes dos arrays `PORTAIS` e
`STUDIOS` de `docs/index.html` (1.731 nomes extraídos), de uma lista curada de ~330 estúdios de
jogos, animação e VFX do escopo, e depois mais 91 de `drafts/` (590 arquivos, já em formato de slug)
e de `alvos.csv` (578 estúdios). Cada nome virou **duas** variantes — com hífen e colada — mais uma
terceira quando terminava em palavra genérica (`studio`, `games`, `entertainment`, `animation`, `vfx`…).

**E a regra do hífen se provou de novo, na mesma rodada:** `warhorse-studios.breezy.hr` responde 200
com **zero** vaga, e `warhorsestudios.breezy.hr` responde 200 com **cinco**. São dois registros
diferentes no Breezy e só a variante colada tem o quadro real. Se eu tivesse testado só a forma com
hífen, teria escrito "Warhorse sem vaga" e perdido a Level Artist inteira. Mesmo padrão em
`axis` vs `axis-studios` (os dois existem, os dois vazios).

**Concorrência:** máximo de 8 requisições simultâneas, e caí para 3 quando o Softgarden começou a
devolver 429 — 754 slugs bateram no limite na primeira passada e foram **todos reprocessados** com
backoff, o que mudou o resultado de 3 deles (`hello`, `paramount`, `website` eram quadros vivos
escondidos atrás do 429). Rodei também uma segunda verificação com três tentativas em cada um dos 51
candidatos do Breezy, porque a primeira passada tinha dado um resultado transitório em
`world-makers-ltd` (404 numa passada, 200 na seguinte).

**Busca na web usada só para DESCOBRIR nome de quadro**, nunca como prova de vaga viva: todo achado
foi reconferido no `/json` oficial do próprio quadro antes de entrar em qualquer conta. Foi assim
que apareceram `wws`, `kitbash3d`, `the-refinery`, `land-sea`, `raid-base-inc`, `possible-inc` e
`world-makers-ltd`, que a adivinhação de slug sozinha não tinha achado — e foi assim também que
quatro "vagas" indexadas se revelaram mortas (§5).

**Dedupe, sempre pelo ID da requisição, nunca por título.** Rodei `grep` do id em `docs/index.html`,
`enviados.csv` e `automacao/processados.csv` para os **11** itens da disciplina, um por um, e o
resultado está escrito linha a linha nos §2 e §3. O caso Playdead prova de novo por que a regra
existe: `a235c228566a01` e `d6b5a5e4f54a01` são a mesma casa, os dois títulos parecem "vaga de arte
da Playdead", e só o id separa a que foi enviada em 06/09 da que foi enviada em 08/09. E a busca na
web ainda indexa um **terceiro** id da Playdead para o mesmo cargo —
`playdead.breezy.hr/p/64eca07e3f5701-3d-environment-artist`, que é um anúncio antigo da mesma 3D
Environment Artist. Dedupe por título teria dado três respostas erradas nesse único estúdio.

---

## 7. NADA MARCADO `precisa-de-navegador`

As duas linhas do §2 respondem 200 na página `/apply` por `curl` e o HTML não traz `recaptcha`,
`hcaptcha` nem `turnstile`. O Breezy já se provou ontem com o POST 204 da Playdead, então o
preenchimento no seu navegador deve correr igual. Não abri nenhum formulário e não enviei nada.

## 8. O QUE EU NÃO CONSEGUI FECHAR

- **Não varri Homerun, Join.com e Softgarden com a segunda leva de slugs** (os 91 de `drafts/` e
  `alvos.csv`) nem com os slugs vindos da busca. Varri as três famílias só com os 3.521 da primeira
  leva. Dado o rendimento medido — 0 vagas da disciplina em 82 vagas totais dessas três famílias
  somadas —, achei que o custo não se pagava, mas é uma lacuna e está escrita.
- **`media.homerun.co` responde 200 e não devolveu título nem feed.** Não consegui identificar de
  quem é. Fica como único quadro Homerun não identificado.
- A conta de "vagas no total" da Softgarden não entra na tabela do §1 porque o único quadro com
  conteúdo listável da nossa área era a Techland, e o conteúdo dela é teste de 2022 (§5); contar
  aquilo como vaga inflaria o número sem significar nada.
