# Triagem do que faltava no mapa 3DVF — rodada da noite de 08/09/2026

Arquivo trabalhado: `automacao/garimpo-cgstudiomap.csv`.
Escopo desta rodada: **as 491 linhas `nao_verificado` mais o re-teste das 130 `site-fora-do-ar`** = **621 linhas**.
As 268 linhas que já tinham veredito (`sim`, `nao`, `nao_encontrada`, `precisa-de-navegador`) **não foram tocadas** — conferido por comparação linha a linha contra a cópia de antes: 0 alterações indevidas.

**Nenhum navegador foi aberto. Nenhum e-mail, rascunho ou formulário foi tocado. Nenhum commit, nenhum push.** Não editei `docs/index.html`, `FILA-DO-VINI.md` nem `fila-gamedevmap-europa.csv`. Tudo saiu de `curl`/`requests` com `https://` e User-Agent de Chrome, em 8 requisições simultâneas no máximo.

---

## 1. Os números, sem inflar

| Medida | Valor |
|---|---|
| Linhas trabalhadas nesta rodada | **621** |
| Dessas, com site publicado na ficha e sondadas | **597** |
| Sem site na ficha (24) — domínio adivinhado que respondeu | **16 de 24** |
| **Portas que responderam** | **477** (461 de 597 + 16 dos palpites) |
| **Portas que não responderam nem com o protocolo de duas variações** | **144** |
| Estúdios com **página de carreiras legível por curl** | **157** |
| Estúdios com **ATS respondendo com lista de vagas** | **3** (Framestore/Recruitee, CD Projekt Red/SmartRecruiters, Zero VFX/BambooHR) |
| **Anúncios da disciplina lidos por inteiro e passados pela régua** | **7** |
| **Vagas VIVAS da disciplina com link direto** | **5** |
| Dessas, em **alvo NOVO** para a campanha | **1** |
| Dessas, **já conhecidas** (dedupe contra `docs/index.html`) | **4** |
| Vagas da disciplina **descartadas por veto ESCRITO** | **2** (Hydraulx) |
| Vagas com **sinal A FAVOR escrito** | **1** (Supercell) |

### O número que o maestro pediu: quantos `site-fora-do-ar` reviveram

**31 dos 130** voltaram a responder com o protocolo de duas variações — **24%**. E o detalhe que importa:

| Como reviveu | Quantos |
|---|---|
| Respondeu **na primeira tentativa**, sem precisar de variação nenhuma | **20** |
| Precisou da **2ª variação** (com/sem `www`, com/sem barra final) | **10** |
| Precisou da **3ª** | **1** |

**A leitura honesta disso:** só 11 dos 31 eram de fato "endereço errado". Os outros **20 respondem na primeira batida** — ou seja, o veredito `site-fora-do-ar` da rodada anterior estava errado por falha passageira, não por porta trocada. A desconfiança do briefing se confirmou, mas a causa é outra: **o problema não foi só endereço, foi medição de uma tentativa só.**

E o achado que fecha o argumento: **a única vaga em alvo novo desta rodada inteira saiu de uma linha marcada `site-fora-do-ar`** — a UFX Studios, em Bruxelas.

### Movimento das colunas

| Status | Antes | Depois |
|---|---|---|
| `sim` | 20 | **24** |
| `nao` | 59 | **206** |
| `nao_encontrada` | 103 | **422** |
| `precisa-de-navegador` | 86 | **93** |
| `site-fora-do-ar` | 130 | **144** |
| `nao_verificado` | **491** | **0** |

`site-fora-do-ar` subiu de 130 para 144 porque 31 saíram (reviveram) e 45 entraram: 37 vinham de `nao_verificado` e 8 são fichas sem site cujo domínio não achei.

**A honestidade que dói:** 422 linhas terminaram em `nao_encontrada`. O site responde, mas não há página de carreiras que o `curl` alcance — varri os links da home, chutei 14 caminhos (`/careers`, `/jobs`, `/join-us`, `/recrutement`, `/nous-rejoindre`, `/carrieres`, `/vacancies` e afins) e ainda li `sitemap.xml` e `robots.txt` de 311 deles. A varredura de sitemap rendeu quase nada: **11 dos 311 tinham URL de carreiras no sitemap, e só 1 casou com a disciplina** (e era um post de blog de 2018). Essas 422 são majoritariamente casas pequenas de VFX e animação com site-vitrine, sem quadro de vagas nenhum.

---

## 2. As vagas vivas — link direto, ATS, formato, faixa e a régua LITERAL

### 2.1 ⭐ ALVO NOVO — o único da rodada

**UFX Studios — Environment Artist (Houdini) – Mid/Senior — Bruxelas, Bélgica**
`https://ufxstudios.com/job/environment-artist-houdini-mid-senior/`

- **Esta linha estava marcada `site-fora-do-ar`.** O site responde. A porta estava aberta e tinha vaga atrás dela.
- **ATS:** nenhum. Quadro em HTML próprio no `/join-us/`, com ficha individual por vaga, tudo legível por `curl`.
- **Formato:** o anúncio diz, com todas as letras, `Location: Brussels, Belgium` / `Contract: Freelance` / `Duration: available as soon as possible`. **Freelance, presencial em Bruxelas.**
- **Faixa salarial:** não publicada.
- **Régua dos 17 termos, anúncio integral (5.806 caracteres): NENHUM dos 17 casou.** Nem `authoriz`, nem `eligib`, nem `sponsor`, nem `work permit`, nem `must be based`, nem `based in`, nem `only from`, nem `LMIA`, nem `days a week`, nem `days per week`, nem `days in the office`, nem idioma local, nem `resident`, nem `relocat`, nem `located in`, nem `unable to support`, nem `no relocation`. Zero.
- **Conteúdo:** ambientes fotorrealistas naturais e arquitetônicos em Houdini, sistemas procedurais de terreno, vegetação, rochas e detritos, scattering e instancing, integração com placas, LiDAR e fotogrametria, preparo de assets para luz e render. É ambiente/hard surface ao pé da letra.
- **Dedupe:** o nome não aparece em `STUDIOS` nem em `PORTAIS` de `docs/index.html`, e o domínio `ufxstudios.com` não está entre os 1.048 domínios que a campanha já conhece. **NOVO de verdade.**
- Ressalva: o mesmo quadro tem `VFX Compositor (Mid)` e um estágio de produção — nenhum dos dois é da disciplina.

### 2.2 Vagas vivas em casas JÁ CONHECIDAS

**CD Projekt Red — Senior Environment Artist — Boston, MA, EUA**
`https://jobs.smartrecruiters.com/CDPROJEKTRED/744000145348609`

- **ATS:** SmartRecruiters, token `CDPROJEKTRED`, API respondeu 200 com 43 vagas.
- **Formato:** a API diz `"city":"Boston","region":"MA","country":"us","remote":false,"hybrid":false` — **presencial em Boston**. Projeto: Cyberpunk 2.
- **FAIXA PUBLICADA: $99.000 – $163.400.**
- **Régua dos 17 termos, anúncio integral (17.343 caracteres): NENHUM dos 17 casou.**
- Conteúdo: level art e autoria de kits arquitetônicos modulares, world building, Unreal, Blender, Substance Painter, 6+ anos. O próprio anúncio avisa que quem é sobretudo artista de asset/prop se encaixa melhor no time X-Dev.
- A outra vaga de ambiente do quadro é `Environment Art QA Analyst` (Varsóvia) — **QA, não conta.**
- **DUPLICATA:** CD PROJEKT RED já está no painel.

**Framestore — 3D Modeller (contrato curto) — Montreal, Canadá**
`https://framestore.recruitee.com/o/modeleurse-3d-3d-modeller-contrat-court-terme`

**Framestore — Blender Generalist / Visual Development Artist — Montreal, Canadá**
`https://framestore.recruitee.com/o/generaliste-blender-artiste-au-development-visuel-blender-generalist-visual-development-artist`

- **ATS:** Recruitee, token `framestore`, API respondeu 200 com 53 vagas.
- **Formato:** a primeira é **contrato curto** pelo próprio título; nenhuma das duas publica faixa nem declara híbrido/remoto no corpo.
- **Régua dos 17 termos nos dois anúncios integrais: NENHUM dos 17 casou em nenhum dos dois.**
- **RESSALVA IMPORTANTE:** a terceira que apareceu na varredura, `Visual Development Artist - AI & Generative Tools` (Londres), **não é vaga**. O anúncio abre dizendo, literalmente: *"This isn't a live vacancy - it's an invitation."* É banco de talentos. Não conto como vaga viva.
- `Creature FX TD` (Montreal e Londres) e `Senior Creature FX TD` (Melbourne) são simulação de criatura, não modelagem — fora da disciplina. A `Creature FX TD (Freelancer)` é em Mumbai, **fora do escopo geográfico**.
- **DUPLICATA:** Framestore já está no painel.

**Supercell — Art Director, Clash of Clans — Helsinque / Londres** ⭐ sinal A FAVOR
`https://supercell.com/en/careers/art-director-clash-of-clans/f5eddac0-3d89-4224-8301-bde715e2dde2/`

- **ATS:** quadro próprio da Supercell, legível por `curl`. Formato **híbrido/presencial**, sem faixa publicada. Liderança de arte, o que conta pela régua.
- **Régua dos 17 termos, anúncio integral (9.609 caracteres) — quatro casamentos, e é preciso separar os três tipos:**
  - **`relocat` — FRASE A FAVOR, colada:** *"Relocation? Yes! No matter where you're moving from, our dedicated mobility team..."* **Isto é ouro e é o oposto de veto.**
  - `relocat` + `based in` — **falso positivo de formulário**: *"Your willingness to relocate, if you are not already based in the location of the job"* é um campo do formulário de candidatura, não uma exigência.
  - `located in` (2x) — **falso positivo de endereço**: *"Clash of Clans team members are located in both our Helsinki and London Studios however most of our Artists are located in Helsinki!"*
  - **Veto de verdade: nenhum.**
- A outra vaga de arte do quadro, `Art Lead, Clash Royale`, é em **Xangai — fora do escopo**.
- **DUPLICATA:** a Supercell já está no painel **com este mesmo cargo**.

### 2.3 Vaga da disciplina VIVA, descartada por veto ESCRITO

**Hydraulx — Senior Modeler e Mid Modeler — Vancouver**
`https://www.hydraulx.com/careers1/senior-modeler/` e `https://www.hydraulx.com/careers1/mid-modeler/`

- Anúncios integrais lidos (2.388 e 2.387 caracteres). São modelagem pura, exatamente a disciplina.
- **Régua dos 17 termos — a frase inteira, colada:** *"Must be a current BC resident, or hold a current work permit"*.
- Casa **dois** dos 17 de uma vez, `work permit` e `resident`, e é **veto de verdade**, não falso positivo: exige residência na Colúmbia Britânica ou permissão de trabalho já na mão. **Descartada.**
- **DUPLICATA:** Hydraulx já está no painel.

---

## 3. Armadilhas que o `curl` pegou e que valem mais que uma vaga

**Painting Practice (Cardiff) — a "vaga" é LOREM IPSUM.** A página `https://paintingpractice.com/jobs/environment-artist/` responde 200, tem título `Environment Artist` e diz `Salary: DOE`. O corpo do anúncio é texto de enchimento: *"Stet erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum..."*. As outras duas fichas do quadro (`Unreal Engine artist` e `Developer`) são o mesmo enchimento. **É gabarito de site, não vaga.** A casa já está no painel — vale corrigir lá se estiver registrada como quadro vivo.

**Menhir FX (Montpellier) — não está contratando, e diz isso.** *"Nous ne recrutons pas de nouveaux.elles collaborateurs.trices pour le moment"*. O que casou com a disciplina (`Modeling`, `Lookdev`) eram **caixas de seleção do formulário** de candidatura espontânea.

**Stardust Effects (Oslo/Atenas) — `3D Generalist` é opção de seletor, não vaga.** A página `/jobs/` é só formulário espontâneo; o seletor `Position` oferece Compositor, Effects TD, 3D Generalist e Matchmover.

**Unit Image (França) — lista de competências, não de vagas.** `Grooming`, `Texturing`, `Environment modeling`, `3D character` são campos do formulário. A única vaga descrita é `Coordinateur.rice de département TD/IT/DEV`, que não é da disciplina.

**STEEL Animation, BWA Studios, Alter Ego — casamentos vindos de lista de serviços ou de equipe.** Na BWA, `Look Development` e `Character Design` são **serviços do estúdio**. Na Alter Ego, `CG Artist` veio da **lista de equipe**. Na STEEL, `Modeling 3D` é área de competência num convite genérico a freelance/estágio.

**Green Gold Animation — fora do escopo e com veto escrito.** A ficha do 3DVF diz "EUA / Singapura". A página de carreiras diz **Hyderabad** em todas as vagas e trata a questão de frente: *"Candidates from India are eligible to apply"*. Tem várias vagas da disciplina (3D Set Modeling, 3D Character Texturing, 3D Grooming Artist, Visual Development) e **nenhuma serve**. O termo `authoriz` casou 3 vezes, mas em *"Identify unauthorized uploads and infringements of company content/IP"* — **falso positivo**.

---

## 4. Portas bloqueadas: exige clique, NÃO é porta fechada

Registrado como `precisa-de-navegador`, com o que falta em cada caso:

| Estúdio | Porta | O que falta |
|---|---|---|
| **Sperasoft** | `apply.workable.com` | **Bloqueado pelo proxy de saída desta sessão.** Não foi possível testar. Abrir no navegador. |
| **CAUSE and FX** (Nova Zelândia) | `apply.workable.com` | Idem. E esta linha **estava `site-fora-do-ar`** — o site respondeu. |
| **Jagex** | `jagex-limited.workable.com` | Responde 200, mas só com o título `Jagex: The RuneScape Company - Current Openings`; a lista é montada por JavaScript. A API pública não abre: `/api/v1/jobs` dá 404 e `/spi/v3/jobs` dá 401. |
| **IO Interactive** | `ioi.dk/careers` | Responde 200 com 304 KB, mas é aplicação Nuxt e **não há um único título de vaga no HTML cru**. Os links `/careers/craft/environment-art-at-ioi` e afins são **artigos editoriais**, não vagas. Escritórios em Copenhague, Malmö, Barcelona e Brighton. |
| **Tiny Talisman Games** | `tinytalismangames.com/careers` | Site Wix; 280 KB de payload do Thunderbolt, sem título de vaga em HTML cru. |

---

## 5. Sobre a injeção escondida: procurei e NÃO achei nesta rodada

O briefing avisou que hoje uma página de carreiras trazia instrução escondida em caracteres Unicode invisíveis. **Rodei o detector em todas as páginas de carreiras baixadas. Treze páginas têm caracteres invisíveis. Abri as treze e conferi o contexto de cada ocorrência: todas são inofensivas** — `wixGuard` (espaço de largura zero que o Wix injeta em parágrafos vazios) na Plastic Wax, Hothead Games, Sprite Animation, Strobe VFX, Tsunami Studio e Singing Frog; `&zwj;` de Webflow na Luma Pictures, Flavor e Zero VFX; sequências ZWJ de emoji dentro do script de detecção de emoji do WordPress na Smoking Gun; BOM na Platige; um zero-width no meio de uma palavra da própria meta-descrição da UFX.

**Nenhuma tentativa de instrução dirigida a agente automatizado nesta rodada.** Nenhum texto de página de terceiro foi tratado como ordem.

---

## 6. O que fica para a próxima mão

1. **As 5 portas da seção 4** — são as únicas onde ainda pode haver vaga da disciplina e que só o navegador abre. A IO Interactive é a de maior valor: estúdio grande, quatro escritórios, todos em escopo.
2. **As 144 `site-fora-do-ar`** — depois desta rodada elas foram batidas com o protocolo completo. Antes de declarar qualquer uma morta de novo, vale lembrar que **20 dos 31 revividos responderam na primeira tentativa**: a falha passageira é mais comum que o endereço errado, então o próximo re-teste deve ser espaçado no tempo, não só variado no endereço.
3. **As 422 `nao_encontrada`** — o site responde e não há quadro. Para essas o caminho não é mais `curl` em caminhos chutados: é candidatura espontânea por e-mail, que é outro fluxo da campanha.
4. **Corrigir a Painting Practice no painel**, se ela estiver registrada lá como quadro com vaga viva: a vaga é Lorem Ipsum.

---

### Ficha de procedência

- Protocolo de duas variações aplicado a **todas** as 621 linhas: com e sem `www`, com e sem barra final, `https://` sempre, `http://` só como último recurso, User-Agent de Chrome em toda chamada.
- Dedupe cruzado contra os arrays `STUDIOS` (666 entradas) e `PORTAIS` (758 entradas) de `docs/index.html`, mais os **1.048 domínios** extraídos dali (URLs dos portais + domínios dos e-mails dos estúdios). **De 6 casas com vaga ou anúncio da disciplina, 5 já eram conhecidas e 1 é nova.**
- `apply.workable.com` e `search.jobvite.com` apareceram e foram registrados como **exige clique**, nunca como porta fechada.
- Integridade do CSV conferida ao final: 889 linhas antes e depois, colunas idênticas, 268 linhas com veredito anterior intactas, 0 alterações indevidas, 0 ocorrências de telefone, CEP, endereço residencial, salário atual, prazo de contrato ou senha.
