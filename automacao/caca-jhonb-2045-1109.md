# Caça do Jhon B — 11/09/2026, 20h45 — QUATRO FAMÍLIAS DE ATS SONDADAS, FILA ZERO

Rodada de **caça**, não de envio: nada foi enviado, nenhum formulário preenchido, **nenhum
navegador aberto**. Tudo por `curl` e API pública. `enviados.csv`, `docs/index.html`,
`automacao/FILA-DO-VINI.md` e `automacao/FILA-PERSONAGEM-1209.md` **não foram tocados**.

Obedece à regra do Vini de 10/09 (personagem e criatura primeiro; modelagem e superfície
genéricas só com a frase do corpo citando personagem; ambiente por último e nunca como
carro-chefe), ao escopo geográfico e à ronda fixa do grupo Disney.

---

## 1. PLACAR — o número vem antes da narrativa

| Medida | Número |
|---|---|
| Slugs de estúdio gerados dos CSVs da campanha (6.304 nomes → 4 variantes) | **15.010** |
| **Sondagens de ATS** (SmartRecruiters + Pinpoint + Breezy, os mesmos 15.010 em cada) | **45.030** |
| Quadros vivos achados: **SmartRecruiters** | **48** (1.147 vagas somadas) |
| Quadros vivos achados: **Pinpoint** | **78 respostas, 16 com corpo, 0 quadro real novo** |
| Quadros vivos achados: **Breezy** | **19** |
| **Jobylon**: anúncios vivos da plataforma inteira, lidos por título | **9.084** |
| Anúncios lidos no **grupo Disney** (Workday Disney ×2 sites, Pixar, Warner, NBCU, Skydance) | **1.564** |
| Quadros do SmartRecruiters já conhecidos, relidos inteiros | **14** (994 vagas) |
| **Total de anúncios lidos** | **≈ 11.320** |
| Bateram título da disciplina | **31** |
| Sobreviveram ao escopo geográfico | **19** |
| Sobreviveram à disciplina (personagem/modelagem/superfície, corpo lido) | **7** |
| Sobreviveram à régua de veto | **5** |
| **Sobreviveram ao DEDUPE** | **0** |
| **FILA NOVA** | **0** |

**A quebra que o Vini pede: 0 de PERSONAGEM, 0 de AMBIENTE, 0 enviadas.** Nenhuma vaga de
ambiente foi empurrada para a fila para inflar o número.

---

## 2. O QUE ESTA RODADA NÃO REFEZ, de propósito

Medido hoje por outras rodadas e **não repetido**: Greenhouse (62.891 slugs, 10.599 anúncios),
Ashby, Lever e Personio (`caca-ashby-lever-1109.md`), Join.com e Workable
(`caca-join-greenhouse-1109.md`), Workday (1.942 slugs em 15 pods, `caca-workday-1109.md`),
Teamtailor Connect e anúncio espontâneo (`rotas-espontaneas-1109.md` + a rodada em curso nos
15 slugs reservados), planilha da comunidade e agregadores (`caca-1109-18h`).
**Os 17 alvos reservados à outra rodada não foram tocados** (os 15 slugs de Teamtailor, Gamecan
e Mino Games).

---

## 3. LANE NOVA Nº 1 — SMARTRECRUITERS POR SLUG: 15.010 SONDAGENS, 48 QUADROS, ZERO PERSONAGEM

A campanha já tinha adivinhado slug no Greenhouse (2.934) e no Teamtailor (2.928), e **nunca no
SmartRecruiters**: o censo conhece **14 tokens** dessa família. Esta é a primeira sondagem.

**O oráculo, e ele é limpo:** `GET api.smartrecruiters.com/v1/companies/<slug>/postings?limit=1`
responde **200 para tudo**; quem decide é o campo **`totalFound`**. Tiro de controle feito antes
de confiar: `zzzznaoexistezzz9` e `naoexiste-teste-xyz` devolvem `totalFound: 0`, `ubisoft2`
devolve 293. Ritmo medido: **300 slugs em 16s** com 12 conexões; os 15.010 em **755s**.

**48 quadros vivos, e o que eles são:** `wetadigital`, `fusefx`, `mavericksvfx`, `ssvfx`,
`frimastudio`, `wildbrain`, `blueislestudios`, `dontnod`, `digitaldistrict`, `cartoonnetwork`,
`paradox`, `silkroad`, `luciddreams`, `jumpgate`, `reanimateddigital`, `socialquantum`,
`realitygames`, `tatsuworks`, `meta4`, `moonycatentertainment` e mais 28 de fora do setor.

**Zero vaga de personagem inédita.** Por que cada nome de peso morreu:

| Quadro | O que tem hoje | Veredito |
|---|---|---|
| `wetadigital` (Weta Digital) | **1** vaga, *VFX Producer*, Wellington, **de 2018-05-10** | Quadro zumbi: a Weta não usa mais este canal. |
| `fusefx` (FuseFX / FOLKS) | 74 vagas, **todas de setembro de 2022** | Quadro zumbi inteiro. A única de disciplina (*Modeling*, *Look Development Artist*, *Grooming Artist*) está em **Mumbai e Bogotá**, fora do escopo, e morta há três anos. |
| `mavericksvfx` (Toronto) | 1, *Senior Compositor*, **2019** | Zumbi, e composição não é disciplina dele. |
| `ssvfx` (Dublin) | 1, *Compositing Artist*, **2023** | Zumbi, disciplina errada. |
| `frimastudio` (Québec) | 18 **vivas** (2026), e são programação, produção e animação técnica | Nada de arte. A `REF30D` *Spontaneous Application* existe, mas é **casa francófona de Québec** e a rota é espontânea de baixo valor. |
| `wildbrain` | 20 **vivas**, todas marketing, licenciamento e operação | Nada de arte. A thread do Groom Supervisor segue sendo outro canal. |
| `blueislestudios` (Toronto) | *Senior Environment Artist* | **2019-12-12**: zumbi, e é ambiente. |
| `dontnod` | 3 espontâneas (`REF75J` Montréal em inglês e francês, `REF15S` Paris) | **Já no painel desde 07/09** como "à mão por DataDome". |
| `paradox`, `silkroad`, `cartoonnetwork` | quadros de **teste** | ver §3.1 |

### 3.1 Armadilha nova: **conta de DEMONSTRAÇÃO com nome de marca famosa**

O slug `cartoonnetwork` responde com **748 vagas** — o maior quadro achado na rodada, e numa casa
do **grupo Warner**, o que faria qualquer rodada parar tudo. **Não é a Cartoon Network.** Os
títulos são `test 42`, `test video`, `wdasd`, `sr eng`, `Plant 1 PLT 100% Visual Inspector #8`,
em Chongqing, Cracóvia e Albânia. É conta de teste do próprio SmartRecruiters usando o nome.
O mesmo vale para `paradox` (*Paradox Job Test 1*, *Paradox - Altru Test*, Scottsdale — **não é
a Paradox Interactive**) e `silkroad` (RH corporativo de 2015, não a Silkroad de jogos).

**É a mesma família do `chopchop` do Teamtailor, que parecia estúdio sueco e era rede de
fast-food.** A regra vale escrita de novo, agora com número: **de 48 quadros vivos, 3 eram
homônimo ou conta de teste, e um deles era o maior de todos.** Confira a identidade da casa pelo
campo `company.name` e por dois ou três títulos antes de gastar rodada.

---

## 4. LANE NOVA Nº 2 — PINPOINT POR SLUG: 15.010 SONDAGENS, E O QUADRO DEMO APARECE TRUNCADO

Rota sondada: `https://<slug>.pinpointhq.com/postings.json`. Ritmo: **10 slugs/s** com 6
conexões (a nota antiga de "1 host por segundo pelo proxy" **não vale para este host**).

**78 responderam, e só 16 com corpo.** Dessas 16, **nenhuma é quadro novo de estúdio**:

- **Quadro DEMO do Pinpoint: 9 contas** (`amplitude`, `cube`, `elastic`, `habitat`, `improbable`,
  `metropolis`, `vanilla`, `kwalee`, `muse`, `exp`, `focus`, `framestore`, `digibc`, `hercules`).
  **Correção do que o brief dizia:** a assinatura não são "cinco vagas sempre iguais". O quadro
  demo vem **truncado em 3, 4 ou 5 itens**, e o discriminador é o CONJUNTO de títulos —
  *Head of DEI* (Belfast/US/UK), *Marketing Manager* (Paris), *Marketing Executive* (Paris),
  *Customer Service Rep* (New York) —, nunca a contagem. Contar cinco deixa passar as truncadas.
- **Conhecidos:** `ccpgames` e `fenriscreations` (**bytes idênticos, 31.534**: é o mesmo quadro,
  Fenris é a ex-CCP), `frontierdevelopments`, `blackbirdinteractive`, `brazenanimation`,
  `buildarocketboy`, `curvedigital`, `hyperhippo`, `bandainamcomobile`.
- **Homônimos:** `embark` é a **Embark Student Corp** do Canadá (poupança educacional), não a
  Embark Studios; `novascotia` é o governo provincial; `ggtech` é operação de cassino em Kiev.

**Os dois quadros reais de casa de jogos que apareceram, e os dois morreram no dedupe:**

| Casa | O que tem | Dedupe |
|---|---|---|
| **Rocksteady Studios** (Londres, Pinpoint `rocksteady`) | 5 vagas: *Senior Technical Animator*, *Web UI/UX*, *QA Manager*, 2 de programação. **Zero da disciplina.** O `/en/register-your-interest/new` responde **200** | **JÁ ENVIADA em 10/09** pelo mesmo register-your-interest (linha no `enviados.csv`) |
| **Maverick Games** (Warwick, `maverick-games`) | 1: *Speculative Applications* `2cfec945-308c-4ab1-aace-a2398c2daf87` | **JÁ ENVIADA em 09/09**, com `/applications/thanks` e texto na tela. Foi a primeira candidatura da campanha por Pinpoint |

---

## 5. LANE NOVA Nº 3 — BREEZY POR SLUG: 19 QUADROS, E OS DOIS BONS JÁ ERAM NOSSOS

Rota: `https://<slug>.breezy.hr/json`. 19 quadros vivos, e a disciplina aparece em **dois**:

- **Warhorse Studios** (Praga): *Open Application* `fabe03688c9401` e *Level Artist*
  `5e0abb1243c101`. A espontânea **já foi enviada em 06/09** (primeira candidatura da campanha na
  Chéquia) e a Level Artist **já está vetada por escrito** desde 09/09.
- **Playdead** (Copenhague): *Experienced Material and Texture Artist* `d6b5a5e4f54a01`
  (**enviada em 06/09**) e *3D Environment Artist* `a235c228566a01` (**enviada em 08/09**,
  com recibo do Breezy). A *Speculative Applications* `fbda7a56839001` fica de pé, mas mandar
  espontânea numa casa que já recebeu duas candidaturas nossas é gerar terceira mensagem.

O resto é fora do setor (`sunday` é seguradora tailandesa, `img` é metalurgia neozelandesa,
`passion` é uma igreja de Atlanta com 11 vagas) ou fora da disciplina (**League of Geeks**,
Melbourne, só *2D Artist*; **Pine Creek Games**, Dinamarca, *2d Artist* e *Tech Artist 2D*;
**Trailmix**, Londres, engenharia).

---

## 6. LANE NOVA Nº 4 — JOBYLON: A PLATAFORMA INTEIRA NUM DOWNLOAD, E DÁ ZERO

O `BRIEF-JHON` registra desde 07/09 que **o Jobylon não tem captcha nenhum** — é a lane mais
barata de enviar que existe — e que `https://emp.jobylon.com/sitemap-jobs.xml` lista todos os
anúncios vivos. **A plataforma inteira nunca tinha sido passada pela régua da disciplina.** Foi
agora: **1 download de 1,49 MB, 9.084 anúncios vivos**, título embutido na URL.

**Resultado por termo, e ele é brutal:** `character` 0, `creature` 0, `modeler` 0, `modeller` 0,
`sculpt` 0, `groom` 0, `surfacing` 0, `look development` 0, `visual development` 0, `texture` 0,
`texturing` 0, `shading` 0, `3d-artist` 0, `vfx` 0.

Os únicos acertos são falsos positivos: `modeling` (3, e são *valuation modeling* da KPMG,
*AI structural modeling* de um hospital e *workforce planning*), `material` (25, todas de
logística, construção e injeção plástica), `artist` (3: a **Remedy** *Senior Performance Capture
Artist*, que é captura de movimento, e duas da myLiaison de 2019-2020).

**A leitura honesta:** o Jobylon é uma plataforma nórdica de RH generalista. A Remedy e a Mojang
estão nela, mas o estoque de arte 3D é **zero**. Vale reconferir **uma vez por semana**, porque
custa um download, e não vale mais que isso.

---

## 7. ARTSTATION JOBS — A DÚVIDA DE 09/09 FECHADA COM CAUSA

A caça de agregadores de 09/09 deixou o ArtStation Jobs como **"0 — não abriu"**, sem causa
escrita. Medido agora, e a causa importa porque o ArtStation é o quadro mais próximo da
disciplina dele que existe:

| Rota | Resposta |
|---|---|
| `www.artstation.com/jobs` | **403** com o desafio do Cloudflare (25 KB de interstitial) |
| `www.artstation.com/jobs.json` | **200**, mas é a **casca da SPA em Angular** — 91 KB de HTML, zero vaga |
| `api/v2/jobs/browse.json`, `search.json`, `index.json` | **500** `An unhandled lowlevel error occurred` |
| `POST api/v2/jobs/search.json` | **412** `Invalid CSRF Token` |

O token de CSRF só existe dentro de uma sessão de navegador; o `GET` da home por `curl` devolve
apenas o cookie `__cf_bm`. **Então o ArtStation Jobs não é caçável por curl: é fila de
navegador.** Isso não é parede do site contra nós, é uma SPA autenticada — e fica registrado para
a próxima rodada não gastar meia hora redescobrindo.

---

## 8. RONDA FIXA DO GRUPO DISNEY — CUMPRIDA, E FECHA EM ZERO

Feita com os **13 termos da lista corrigida hoje** (com `texture`, `texturing`, `shading` e
`material`), nos dois sites do locatário `disney`, na Pixar, na Warner, na NBCU e na Skydance.

| Casa | Onde | Lido | Bateram no filtro de título | Veredito |
|---|---|---|---|---|
| Disney (ILM, Pixar, Marvel, 20th, DTVA) | Workday `disney`/wd5, **`disneycareer` E `disneycareerdc`** | **416 requisições distintas** | 19 no primeiro site, 26 no segundo | **0 novo** |
| Pixar | Workday `pixar`/wd501 | 2 | 0 | On-Call Chef e Staff Systems Engineer |
| Warner | Workday `warnerbros`/wd5 `global` | 185 | 2 | *Advanced Level Artist* Montréal (ambiente, já julgada) e *Senior Lighting Artist* Rocksteady |
| NBCUniversal / DreamWorks | SmartRecruiters `nbcuniversal3` | 330 | 7 | **veto escrito**, ver abaixo |
| Skydance / Paramount | Lever `skydance` | 28 | 10 | só ambiente, rigging, crowds e a Grooming TD já na fila |

**A prova de cobertura que vale mais que a lista:** dos **416** IDs de requisição da Disney lidos
hoje, **363 não aparecem em lugar nenhum do repositório** — ou seja, a leitura foi larga de
verdade, não só das que já conhecíamos. E **nenhuma das 363 é da disciplina**: são engenharia de
software, marketing, parques, estágios, *Motion Editor*, *Lighting TD*, *Compositor*,
*Sr Effects TD* e *QA Analyst*. As de personagem e modelagem que existem continuam sendo as
mesmas de sempre, e todas já resolvidas:

- `10154147` *Sr Character Modeler* e `10155895` *Lead Modeler* — **Mumbai, fora do escopo**.
- `10159370` e `10159371` de textura da ILM London — **enviadas e recusadas**.
- `10159882` *Senior Modeler* ILM Sydney — **enviada em 04/09**.
- `10157562`, `10144787`, `10155976` *Creature TD* — **rigging**, fora pela ressalva do briefing.
- `10126752` *Creatures FX* — **simulação**, fora.
- `10160278` *FaceSwap Artist* — já descartada em 10/09 (é comp em Nuke com rede neural).

**NBCU, o veto recolado palavra por palavra** nas duas que doem (`REF38910F` *Lead Character
Artist* e `REF38920U` *Lead Material Artist (Character/Wardrobe)*, Montréal):

> *"Eligibility Requirements — Interested candidates must apply to be considered. Must be willing
> to work in our Montreal office a minimum of 4 days a week. **Must be legally authorized to work
> in Canada.** Must be willing to travel for work related business, if necessary"*

Bate três termos da régua de uma vez (`eligib`, `days a week`, `authoriz`) e **é veto escrito**.
A `REF38952U` *DreamWorks Feature - Character Effects Artist* de Glendale segue fora por CFX.

**Skydance:** a `9ad28cab` *Senior Grooming TD* de Madri continua sendo a única de personagem
limpa do grupo inteiro, e continua **presa atrás do hCaptcha do Lever** — é a entrada 23 da
`FILA-DO-VINI`. A `7b435bb2` *Character Surfacing Trainee* já tinha sido lida e descartada em
10/09 por ser **estágio** (*"Must be currently enrolled..."*).

---

## 9. O QUE CHEGOU PERTO E MORREU NO DEDUPE — com o ID de cada uma

Esta é a seção que impede a próxima rodada de repetir o caminho:

| Vaga | ID da requisição | Onde morreu |
|---|---|---|
| Maverick Games — *Speculative Applications* | `2cfec945-308c-4ab1-aace-a2398c2daf87` | **Enviada 09/09**, `/applications/thanks` no `enviados.csv` |
| Rocksteady — *Register Your Interest* | `rocksteady.pinpointhq.com/register-your-interest/new` | **Enviada 10/09** |
| Warhorse — *Open Application* | `fabe03688c9401` | **Enviada 06/09** |
| Playdead — *Experienced Material and Texture Artist* | `d6b5a5e4f54a01` | **Enviada 06/09** |
| Playdead — *3D Environment Artist* | `a235c228566a01` | **Enviada 08/09** |
| DONTNOD Montréal — *Spontaneous Application* | `744000056999494` (ref `REF75J`) | No painel desde 07/09, à mão por DataDome. **A versão francesa `744000056999405` tem a MESMA ref**: uma requisição, dois anúncios |
| Techland — *Character Artist* | `744000145235194` e `744000137670539`, ambas ref **`REF64D`** | Já registrada; as duas cidades são **uma requisição só** |
| Ubisoft — *Team Lead Modeling (Unreal)* Montréal | `744000141713411` ref `REF31530C` | Já no painel; casa é parede de DataDome |
| Keywords Australia — *Senior Character Artist* | `744000130680219` | Já no `PORTAIS` |
| Skydance — *Character Surfacing Trainee* | `7b435bb2-09fd-4f2f-8fca-9c2fa6666adc` | Estágio, descartada em 10/09 |

---

## 10. FILA FINAL

**Vazia, e de propósito.** Nenhuma linha foi acrescentada a `automacao/FILA-DO-VINI.md` porque
nenhuma vaga sobreviveu ao dedupe. Não há vaga de ambiente na fila porque **não sobrou nem
ambiente**: o que apareceu de ambiente (Blue Isle 2019, Warhorse Level Artist vetada, Playdead já
enviada) morreu antes, por idade, veto ou envio anterior.

## 11. O QUE A PRÓXIMA RODADA NÃO PRECISA REFAZER

1. **SmartRecruiters por slug**: 15.010 testados, os 48 vivos estão listados na §3. Adivinhar
   slug nessa família rende **zero** — e agora está medido, não suposto.
2. **Pinpoint por slug**: 15.010 testados. O estoque de quadro novo nessa plataforma **acabou**;
   some-se à medição de 10/09 (3.600 tokens → 12 quadros) e à de hoje de manhã (21 nomes → 0).
3. **Breezy por slug**: 15.010 testados, 19 quadros, e os dois de jogos já são nossos.
4. **Jobylon**: zero da disciplina em 9.084 anúncios. Reconferir no máximo uma vez por semana.
5. **ArtStation Jobs**: não abre por curl, e a causa está na §7. Só navegador.

**A leitura estratégica, e ela é a mesma de 08/09 com número novo:** adivinhar slug em qualquer
família já rendeu, somando tudo, 2 vagas em mais de 20 mil tentativas. O que ainda rende é
**casa nova achada por outro caminho** — página de carreiras lida no texto, recibo de ATS na
caixa de entrada, e quadro em domínio próprio.
