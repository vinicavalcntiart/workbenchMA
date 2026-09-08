# Colheita europeia do gamedevmap — 08/09

Fila gerada: `automacao/fila-gamedevmap-europa.csv` (4148 linhas de dado + cabeçalho).
Escopo: os 17 países europeus pedidos, mais Austrália e Nova Zelândia no fim.

---

## 1. O parâmetro de paginação e a prova de que ele pagina

Usei:

```
https://www.gamedevmap.com/index.php?location=&country=<Pais>&state=&city=&query=&type=&start=<1|101|201|...>&count=100
```

**Prova, medida hoje na Suécia** (primeiro e último nome de cada resposta):

| requisição | primeiro nome | último nome |
|---|---|---|
| `start=1&count=100` | 10 Chambers | Coldwood Interactive |
| `start=101&count=100` | Collecting Smiles | Frostrok |
| `start=201&count=100` | Frostspektrum Interactive | Laser Rabbit |
| `start=301&count=100` | Lavapotion (Coffee Stain) | Omniscapes Interactive |
| `start=401&count=100` | One Potato Kingdom | Skildra |
| `start=501&count=100` | Skildra Sverige Ekonomisk | Uncloudy Labs |
| `start=601&count=100` | Unity Technologies Sweden | Ztar Games (45 linhas, fim) |
| **`page=2`** | **10 Chambers** | **Coldwood Interactive** |

Os nomes de `start=101` são **diferentes** dos de `start=1`: pagina de verdade, e a progressão
alfabética é contínua e limpa nas sete páginas. Já `page=2` devolve **byte a byte a mesma
página 1** (91.560 bytes nos dois casos, mesmo primeiro e mesmo último nome). Com `page=` a
Suécia teria virado 100 estúdios em vez de 644.

Também confirmei a segunda armadilha do briefing: `http://` puro devolve 400 com corpo vazio
neste ambiente. Tudo foi por `https://`.

## 1b. Armadilha NOVA, que o briefing não previa: o Reino Unido não existe como um país só

`country=United Kingdom` devolve **17 estúdios** e mais nada — parecem ser resíduos de
cadastro. O Reino Unido de verdade está partido em quatro valores no `<select>` do site:

| valor | estúdios |
|---|---|
| England | 790 |
| Scotland | 101 |
| Wales | 27 |
| Northern Ireland | 21 |
| United Kingdom (resíduo) | 17 |
| **total britânico** | **956** |

Quem pedir só `country=United Kingdom` reporta 17 e perde 939. Pela mesma lógica a Tchéquia é
**`Czechia`**; `Czech Republic` devolve **zero linhas**, e zero linhas aqui não é país sem
estúdio, é nome de país errado. Descobri as duas lendo a lista de `<option>` do próprio
formulário do site — vale conferir essa lista antes de assumir o nome de qualquer país.

---

## 2. Total colhido por país

Depois de deduplicar por (nome, cidade): **4148 estúdios únicos**.

| país | total | em escopo | NOVOS p/ campanha |
|---|---:|---:|---:|
| England | 790 | 696 | 683 |
| Sweden | 644 | 590 | 358 |
| Germany | 417 | 361 | 217 |
| France | 372 | 321 | 344 |
| Poland | 276 | 248 | 74 |
| Spain | 252 | 232 | 73 |
| Australia | 224 | 203 | 164 |
| Netherlands | 223 | 199 | 94 |
| Finland | 130 | 117 | 74 |
| Italy | 114 | 100 | 25 |
| Scotland | 101 | 98 | 94 |
| Belgium | 79 | 68 | 22 |
| New Zealand | 74 | 70 | 51 |
| Switzerland | 72 | 58 | 38 |
| Denmark | 70 | 65 | 18 |
| Czechia | 65 | 62 | 53 |
| Ireland | 53 | 46 | 19 |
| Norway | 46 | 41 | 17 |
| Portugal | 43 | 39 | 15 |
| Austria | 38 | 33 | 14 |
| Wales | 27 | 25 | 26 |
| Northern Ireland | 21 | 20 | 20 |
| United Kingdom (resíduo) | 17 | 16 | 2 |
| **TOTAL** | **4148** | **3708** | **2495** |

- **Em escopo: 3708.** Fora de escopo são 440 do tipo Investment, Incubator/Accelerator,
  Organization, Health, School, Recruiting e Publisher puro — não têm time de arte de personagem.
- **NOVOS para a campanha: 2495.** Cruzamento contra `PORTAIS` (736 linhas) e `STUDIOS`
  (665 linhas) do painel, extraídos com o scanner que respeita aspas, mais `enviados.csv`,
  `alvos.csv`, `processados.csv` e `pessoas.csv`, por nome normalizado **e** por domínio.
- **NOVOS e em escopo ao mesmo tempo: 2072.** Esta é a fila útil.
- Outros 1142 já apareceram nas filas gamedevmap europeias de 06/09 (europa2/3/4, se-dk,
  ch-fi-nl, oceania) mas nunca foram contatados; estão marcados
  `ja na fila gamedevmap 06/09`, separados dos 511 realmente já tocados.

### Ressalva de honestidade sobre "ninguém fez a Europa"

O briefing diz que ninguém tinha feito o equivalente europeu. **Isso não confere.** Em 06/09
foram criadas cinco filas europeias do gamedevmap (`fila-gamedevmap-europa2/3/4.csv`,
`se-dk`, `ch-fi-nl`), somando cerca de 1330 nomes. O que esta colheita acrescenta é
(a) o Reino Unido, que aquelas filas praticamente não pegaram por causa da armadilha
England/Scotland/Wales, (b) a Tchéquia, que estava com o nome errado, e (c) as páginas
profundas de vários países. O ganho real são **2495 nomes que não estão nem no painel, nem
nos CSVs da campanha, nem nas filas de 06/09** — a coluna `conhecido` só marca `NOVO` quem
falha nos três testes ao mesmo tempo. Os 1142 marcados `ja na fila gamedevmap 06/09` são um
terceiro estado: já listados naquele dia, mas ainda sem contato.

### Cidades de maior densidade na colheita

Londres 291 · Estocolmo 237 · Paris 136 · Varsóvia 122 · Berlim 105 · Barcelona 93 ·
Malmö 70 · Helsinque 67 · Copenhague 58 · Hamburgo 56 · Madri 53 · Amsterdã 51 ·
Munique 43 · Cracóvia 40 · Dublin 39 · Milão 39 · Praga 31 · Bordeaux 25 ·
Montpellier 25 · Lisboa 24.

O CSV está ordenado exatamente por essa lista de densidade, depois por país e nome.

---

## 3. Quanto consegui triar

**777 estúdios triados de 4148** (18,7%). Detalhe honesto do que "triado" significa:

| etapa | número |
|---|---:|
| candidatos priorizados (NOVO + em escopo + cidade densa + com site) | 739 |
| sondados na porta (`/careers`, `/jobs`, raiz) | 739 |
| responderam 200 com corpo útil | 645 |
| não responderam (DNS morto, TLS quebrado, timeout, egress bloqueado) | 94 |
| slugs de ATS testados contra 8 famílias de ATS | 1627 slugs × 8 endpoints |
| quadros de ATS reais encontrados | 57 |
| anúncios/quadros lidos a fundo, um a um | 25 |

As oito famílias sondadas por slug: Greenhouse US, Greenhouse EU, Lever, Teamtailor,
SmartRecruiters, Workable, Recruitee e Personio. Precisei disso porque a maioria das páginas
de carreira europeias é SPA em JavaScript: o cargo não está no HTML, só o ATS por trás está.

**Os 3371 restantes ficaram como `nao-triado` no CSV.** Não os toquei.

---

## 4. Vagas vivas da disciplina, com link, ATS e busca de veto

Busca literal aplicada ao anúncio inteiro baixado: `authoriz`, `eligib`, `sponsor`,
`work permit`, `must be based`, `days a week`, `resident`, mais o idioma local quando cabia.

### 4.1 APROVADAS — vaga viva na disciplina, sem veto escrito

**1. Techland — Character Artist — Wrocław / Warszawa, Polônia**
- Anúncio: https://techland.net/job-offers/character-artist-06
- Candidatura/ATS: **SmartRecruiters** — https://jobs.smartrecruiters.com/TechlandSA/744000145235194-character-artist
- Modelo: remote / onsite / hybrid (o próprio anúncio lista os três)
- Encaixe: cheio. "Criar modelos 3D de personagens — humanos, monstros", ZBrush, 3ds Max/Maya,
  Substance Painter, Marvelous Designer, Wrap3D, anatomia humana, texturas e materiais de
  personagem. Reporta ao Lead Character Artist e ao Art Director.
- **Busca de veto, resultado literal:** `authoriz` 0 · `eligib` 0 · `sponsor` 0 ·
  `work permit` 0 · `must be based` 0 · `days a week` 0 · `resident` 0.
  `Polish` aparece **1 vez**, e o contexto é benefício, não exigência: *"financing of English
  and Polish language classes"*. O requisito de idioma escrito é *"Very good command of English"*.
  → **SEM VETO ESCRITO.**
- Contexto: o estúdio já é conhecido da campanha (aparece no painel). A vaga pede "pelo menos
  2 anos", ou seja, a barra é baixa para 10+ anos — vale checar se não é júnior demais em faixa.

**2. Casual Brothers — 3D Artists, Animators & VFX — Londres, Inglaterra**
- Anúncio: https://www.casualbrothers.com/careers (bloco "3D Artists, Animators & VFX", com botão Apply)
- ATS: **nenhum** — formulário próprio no site. Não vi captcha no HTML, veredito só com o clique.
- Encaixe: parcial mas real. *"Create the art, characters and worlds that define our games"*,
  3+ anos em pipeline de arte de jogo, domínio de Blender/Maya/ZBrush/Houdini. É uma vaga
  agrupada (personagem + animação + VFX no mesmo anúncio), então a fatia de personagem
  precisa ser confirmada no contato.
- **Busca de veto, resultado literal:** `authoriz` 1 · `eligib` 0 · `sponsor` 0 ·
  `work permit` 0 · `must be based` 0 · `days a week` 0 · `resident` 0 · `Polish` 1.
  **Os dois achados são falso positivo e eu conferi o contexto de cada um:** o `authoriz` é a
  chave `"unauthorized":"$undefined"` do framework Next.js dentro do JSON da página, e o
  `Polish` é a palavra inglesa *polish* em *"the polish players notice"*.
  → **SEM VETO ESCRITO.**
- **NOVO para a campanha.** Londres.

### 4.2 Achada viva, mas com VETO ESCRITO ou fora da disciplina

**3. MadBox — Senior 3D Marketing Artist — Paris, França**
- Anúncio: https://careers.madbox.io/jobs/7707805-senior-3d-marketing-artist
- ATS: **Teamtailor** (`madbox.teamtailor.com` / `careers.madbox.io`)
- **VETO ESCRITO, literal:** *"Please note: unfortunately, this position is not open to
  relocation and we cannot offer visa sponsorship."* A parte do patrocínio é só contexto pelo
  critério da campanha, mas **"not open to relocation" é veto de localização escrito** e
  desqualifica.
- Além disso está **fora da disciplina**: é render e animação de anúncio de UA em Blender,
  arte de marketing, não personagem de jogo.
- → **DESCARTE.** Estúdio NOVO, fica no CSV para uma futura vaga de personagem.

**4. Sandbox Interactive (Stillfront) — Lead 3D Environment Artist — Berlim, Alemanha**
- Anúncio: https://sandboxinteractive.teamtailor.com/jobs/8094866-lead-3d-environment-artist-m-f-d
- ATS: **Teamtailor**
- **Busca de veto:** `sponsor` 2 e `German` 2, **os quatro falso positivo, contexto conferido**:
  *"company-sponsored training and language courses"*, *"company-sponsored tickets for Gamescom"*
  e *"a free company ticket for Germany's public transportation system"*. `authoriz` 0,
  `eligib` 0, `work permit` 0, `must be based` 0, `days a week` 0, `resident` 0.
  → **SEM VETO ESCRITO.**
- Mas: **ambiente é prioridade MÉDIA** para o Vini, não personagem, e é vaga de Lead. Fica como
  segunda linha, não como alvo principal. Estúdio já conhecido da campanha.
- A "Character 3D Artist" de Albion Online que a busca indexou **não está mais no quadro**: os
  8 anúncios vivos hoje são Level Designer, Senior Game Producer, tradutor freelance, UI Lead,
  Lead 3D Environment Artist, VFX Artist, agente de suporte freelance e Data Engineer.

### 4.3 Vagas que a busca indexou e que eu conferi na fonte estando MORTAS

Registro para ninguém perder tempo indo atrás de novo. **Nenhuma destas eu reporto como viva.**

| estúdio | vaga indexada | o que a fonte diz hoje |
|---|---|---|
| Housemarque (Helsinque) | Lead Character Artist, `job-boards.greenhouse.io/housemarque/jobs/5528945004` | quadro Greenhouse responde *"There are no current openings"*; a API devolve `{"jobs":[],"meta":{"total":0}}` |
| Metacore (Helsinque) | 3D Character Artist, Merge Mansion, `job-boards.eu.greenhouse.io/metacore/jobs/4593534101` | o ID redireciona para o quadro, que traz `"jobPosts":{"count":0,"total":0}` |
| Massive Entertainment (Malmö) | Character Artist | o próprio agregador marca **EXPIRED** |
| Fatshark (Estocolmo) | Character Artist temporário 6 meses | não achei o anúncio vivo na fonte; `fatshark.teamtailor.com/jobs` não expõe nenhuma vaga |
| Ringtail Interactive (Solna) | 3D Character Artist | só existe em agregador de terceiro; o Teamtailor do estúdio dá 404. **Não confirmada na fonte, então não conta.** Também não está no gamedevmap |
| Frever AB (Estocolmo) | estágio 3D Artist Character/Wardrobe | slug Teamtailor dá 404; e estágio não serve para 10+ anos |

### 4.4 Falsos positivos de varredura que eu abri e descartei

Onze estúdios deram hit de `character artist` / `3d artist` no HTML mas **a menção é da equipe,
do crédito de um jogo, do serviço vendido ou de trabalho voluntário — não é vaga**:
Opus Major (Paris), Wild Sheep Studio (Montpellier), Skrice (Paris), Yorf Studio (França),
UMA Games, Hole in the Sleeve, Jump Over the Age, Unigine Europe, Team FOLON (modders
voluntários), Plink&Plonk Studio (explicitamente *"We don't have any positions open for paid
work"*, é voluntariado — descarte) e Zero Games Studios (Paris), que lista "Game Artist /
Character Artist" como disciplinas que contrata, não como vaga aberta.
FanStudio (Reino Unido) tem formulário permanente com opção "3D Artist" mas nenhuma vaga
datada. SuperPlay tem 3D Artist vivo, porém em Tel Aviv — fora do escopo europeu.

Quadros de ATS vivos que abri e onde **não havia nada da disciplina**: Bloober Team (Cracóvia,
4 vagas), Huuuge Games (Varsóvia, 7 vagas), DONTNOD (Paris, só candidatura espontânea),
Stratosphere Games (Berlim, só QA e espontânea), Zwift (5 vagas), Yager (Personio vazio),
Homa Games, Panic Stations, Redly, FitXR, MovieStarPlanet, Starberry, Kolibri, Poki,
MAG Interactive, SOFTGAMES, Travian, Outfit7, Amplitude, Tactile, Remedy, Wildlife, 2K Czech.

---

## 5. O que travou

1. **A Europa já tinha sido parcialmente colhida em 06/09** e o briefing dizia que não. Gastei
   a primeira meia hora reconciliando cinco filas antigas para não inflar o número de "novos".
   Está tudo separado em três estados na coluna `conhecido`.
2. **O Reino Unido quase virou 17 estúdios.** Só não virou porque desconfiei do número e fui ler
   a lista de `<option>` do formulário. É a mesma classe de erro que quase custou os 388
   canadenses, e o briefing não a previa. Vale registrar como armadilha permanente.
3. **Página de carreira SPA é a barreira real da triagem em massa.** Dos 645 sites que
   responderam 200, só 14 tinham o cargo no HTML. Foi por isso que precisei adivinhar slug de
   ATS: adivinhação acerta pouco (57 quadros em 1627 slugs) e é o gargalo. Quem continuar isto
   ganha mais mapeando estúdio→ATS uma vez e guardando o token do que refazendo a adivinhação.
4. **Buscador devolve vaga morta com cara de viva.** Quatro das seis pistas mais promissoras
   (Housemarque, Metacore, Massive, Fatshark) estavam mortas na fonte. Conferi cada uma antes
   de escrever; nenhuma entrou como viva.
5. **Egress bloqueado** em alguns domínios (`zerogamesstudios.com`, `www.casualbrothers.com`
   pelo WebFetch, `ludomotion.com`, `macrograph.co.kr`). Onde deu, contornei lendo o HTML que
   o `curl` já tinha baixado; onde não deu, marquei `porta-sem-resposta` em vez de chutar.
6. **Não abri navegador, não commitei, não mandei e-mail, não toquei em `docs/index.html`,
   `enviados.csv`, `pessoas.csv`, `processados.csv` nem `fila-gamedevmap-canada.csv`.**
