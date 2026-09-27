# CAÇA: ASHBY · BAMBOOHR · GOHIRE · LEVER · BREEZY · JAZZHR · HOMERUN — 09/09/2026 (noite)

**Método: só `curl` e as APIs públicas das sete famílias. Nenhum navegador, nenhum Playwright,
nenhum `hb_run.sh`, nenhum formulário preenchido, nenhum e-mail, nenhum commit, nenhum push.**
Não toquei em `docs/index.html`, `enviados.csv`, `automacao/processados.csv` nem
`automacao/FILA-DO-VINI.md`. Este arquivo é o único que criei.

Busca na web usada **duas vezes e só para DESCOBRIR endereço de quadro** (o hash de cliente do
GoHire), nunca como prova de vaga viva: todo achado foi reconferido no quadro oficial por `curl`.

---

## 1. O NÚMERO, ANTES DA NARRATIVA

**Universo de sondagem:** 3.154 slugs gerados dos arrays `PORTAIS`/`STUDIOS`/`PROSPECTOS`/`GRANDES`
/`NOVIDADES`/`DOSSIES` de `docs/index.html` (1.497 nomes), de `alvos.csv` e dos 590 arquivos de
`drafts/`, em duas variantes cada (com hífen e colada) mais a variante sem palavra genérica final —
**mais** 76 slugs já conhecidos, colhidos por `grep` de host em todo o repositório e dos tokens do
`censo-boards-0809.csv`. Os oito slugs genéricos que o `caca-painel-familias.md` marcou como
armadilha (`career`, `jobs`, `explore`, `system`, `company`, `onyx`, `recruit`, `artstation`) foram
removidos antes de disparar.

| Família | Sondagens | Quadros vivos (HTTP 200) | Vagas da disciplina | No recorte geográfico | Passaram na régua | Dedupe limpo | **Na fila** |
|---|---|---|---|---|---|---|---|
| **Ashby** | 3.230 | **35** | 8 | 5 | 0 | — | **0** |
| **Lever** | 3.230 | **19** | 20 | 16 | 16 | 4 | **2** |
| **BambooHR** | 3.230 | **98** (48 com ≥1 vaga) | 23 | 19 | 0 | — | **0** |
| **JazzHR** | 3.230 | **37** (16 com quadro de verdade) | 2 | 2 | 2 | 0 | **0** |
| **Breezy** | 3.154 | **7 com vaga** | 12 | 6 | 1 | 0 | **0** |
| **Homerun** | 3.154 | **9 feeds vivos** | 1 | 1 | 1 | 1 | **1** |
| **GoHire** | sitemap de **20.436** URLs | 6 quadros resolvidos | 5 | 4 | 4 | 3 | **0 (+3 com ressalva)** |
| **TOTAL** | **~19.400 requisições** | **204 quadros** | **71** | **53** | **24** | **8** | **3 + 4 com ressalva** |

**A fila tem TRÊS linhas para clicar e QUATRO registradas com ressalva.** Uma das três é a mais
importante da rodada e não veio de quadro novo: veio de um quadro que o painel **já tinha visto em
07/09 e descartou por escrito com um erro de leitura de disciplina** (§2.1). É o mesmo erro do caso
Epic documentado no `caca-painel-familias.md`, três dias depois, em outra casa.

---

## 2. FILA PRONTA PARA CLICAR

---

### LINHA 1 — ustwo games · Senior 3D Environment Artist ⭐ A MELHOR DA RODADA

| Campo | Valor |
|---|---|
| **Estúdio** | ustwo games (Monument Valley, Alba, Desta) |
| **Título exato** | `Senior Environment Artist` (no corpo do anúncio: *"Senior 3D Environment Artist"*) |
| **ID da requisição** | **`job_Kn8xX76scpWFSwBrWpGA`** |
| **Cidade/País** | Londres (Oval), **Reino Unido** — híbrido OU remoto |
| **Família de ATS** | **HOMERUN** — família provada (a campanha já enviou pelo Homerun da Total Mayhem em 06/09) |
| **URL do anúncio** | `https://ustwo-games.homerun.co/senior-environment-artist` — **HTTP 200** (22.462 bytes) |
| **URL de candidatura** | `https://ustwo-games.homerun.co/senior-environment-artist/en/apply` — **HTTP 200** (40.789 bytes, redireciona para `/en_GB/apply`) |
| **Publicada / atualizada** | `2026-07-21 11:34:15` (campo `<updated>` do feed Atom oficial) |
| **Formato** | **Contrato temporário de 12 meses (FTC)**, salariado por preferência, mas *"we are also open to day-rate contractors"* |
| **Faixa publicada** | **NÃO.** O campo `<salary_indication>` do feed vem literalmente como `£ per year`, sem número |
| **Captcha** | A página `/apply` não traz `recaptcha`, `hcaptcha`, `turnstile` nem `captcha` — **zero casamentos**. Preenchimento direto |

**DISCIPLINA — é o centro do filtro, com citação:**

> *"Owning the full environment pipeline: **modelling in Blender, texturing**, dressing and composing
> scenes in Unity"*
> *"Full-pipeline 3D environment craft, with strong composition, colour and shape language sensibilities"*
> *"painterly, colourful, **sitting between realistic and stylised**, where lighting, colour and
> materials do the heavy lifting rather than dense geometry"*
> *"Senior-level ownership: you'll be the primary environment artist on the vertical slice phase"*

Arte de ambiente 3D com modelagem e texturização declaradas, e o registro **estilizado** dito com
todas as letras. Está dentro do filtro de disciplina desta campanha sem margem para dúvida.

**RÉGUA DE VETO — texto integral de 2.897 caracteres, extraído do `<description>` do feed Atom
oficial (`https://feed.homerun.co/ustwo-games`, HTTP 200, 25.826 bytes). Resultado: ZERO
casamentos.** Nenhuma ocorrência de `authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`,
`based in`, `only from`, `LMIA`, `days a week`, `days per week`, `days in the office`, `resident`,
`relocat`, `located in`, `unable to support`, `no relocation`, `x a week`, `x per week`,
`within the`, `only`, nem exigência de idioma local. **Veto escrito: zero.**

**O QUE EU AINDA ASSIM PRECISO TE MOSTRAR, porque é material mesmo não batendo na régua.** O
parágrafo "Important details" traz duas frases que se puxam para lados opostos, e as duas estão
inteiras aqui:

> *"Time together at our London (Oval) studio is encouraged where possible, especially early on,
> but **we're not limiting this search by geography**."*
> *"Our preference is to have some weekly in-studio time, but we will consider strong applicants who
> are **based anywhere in the UK or Europe**, with preparedness for travel to the studio regularly."*

A primeira é frase A FAVOR e explícita. A segunda descreve o alcance esperado da busca. **Nenhuma
das duas bate literalmente na régua** — o termo é `based in` e o texto escreve "based anywhere in",
que é outra construção e outro sentido. Não é veto de autorização, não é exigência de residência
prévia, não é cláusula de patrocínio. **Registro porque é honesto, não porque desqualifique.**

**Formulário — o que ele vai perguntar, medido na página `/apply`:** *"Where are you currently
based?"*, *"**Do you have the legal right to work in the UK?**"*, *"Are you aware that this is a
12-month fixed-term contract role…"*, *"What is your preferred working arrangement? (Fully remote,
hybrid, or onsite)"*, *"If you're not based in London, are you able and willing to travel to the
studio?"*, *"What are your salary expectations?"* e uma carta motivacional. A pergunta sobre direito
de trabalho no Reino Unido é **pergunta de formulário, não veto de anúncio** — pela regra da
campanha, precisar de patrocínio é contexto e se responde com a verdade.

**DEDUPE — arquivo por arquivo, pelo ID da requisição:**

| Arquivo | `job_Kn8xX76scpWFSwBrWpGA` | `Kn8xX76scpWFSwBrWpGA` |
|---|---|---|
| `enviados.csv` | **0** | **0** |
| `automacao/processados.csv` | **0** | **0** |
| `docs/index.html` | **0** | **0** |
| `automacao/FILA-DO-VINI.md` | **0** | **0** |

**Grep pelo NOME da casa, porque a casa É familiar** (regra 6): `ustwo` aparece **1 vez** em
`docs/index.html` e **0** nos outros três. Li a ocorrência inteira até o fim da célula, e ela é a
descoberta desta linha:

> `["ustwo games","United-Kingdom","https://www.ustwogames.co.uk/careers/","portal","MEDIDO em 07/09 (Monument Valley): a url real e /join-us/, com vagas no Homerun (ustwo-games.homerun.co): Senior Level Designer, **Senior Environment Artist**, Senior Technical Artist, Senior Programmer e Associate Community Manager. **Nenhuma de personagem, modelagem, textura, look dev, visual dev ou generalista 3D.**",false,"baixa"]`

**#### 2.1 — O ERRO QUE ESTA LINHA CORRIGE, e ele é do painel, não meu**

A nota de 07/09 **viu a Senior Environment Artist com o nome certo** e escreveu, na mesma frase,
que ali não havia "modelagem" nem "textura". O anúncio diz, literalmente: *"Owning the full
environment pipeline: **modelling in Blender, texturing**, dressing and composing scenes in Unity"*.
A casa foi rebaixada para `baixa`, nenhum ID de requisição foi registrado, nenhuma candidatura saiu,
e a porta ficou aberta e intocada por **dois dias**.

É exatamente o mesmo padrão que o `caca-painel-familias.md` documentou no caso Epic: *"um censo de
06/09 viu essas duas requisições e as descartou por escrito com a frase 'Principal e Senior
Environment Artist da Epic sao ambiente'. Pela régua de disciplina desta campanha, ambiente CONTA"*.
**Ambiente conta. Ambiente com modelagem e texturização conta duas vezes.** Vale marcar a regra:
quando a nota de descarte diz "nenhuma de modelagem" sem colar frase do anúncio, o descarte não foi
medido — foi lido pelo título.

**RESSALVA HONESTA DE ENCAIXE.** É contrato de 12 meses, não efetivo. É ambiente, não personagem —
disciplina secundária do portfólio dele, ainda que declarada no filtro. E o anúncio pede um perfil
de gosto específico: *"Artists who take influences from editorial design, illustration and graphic
design excite us more than traditional environment art. **Wacky beats safe.**"* e *"Blender
proficiency is preferred"* — se o pipeline dele é Maya/ZBrush, isso precisa ser endereçado na carta.
Por outro lado o anúncio pede *"A technical lean towards lighting especially, or shaders and
materials"*, e material/shading é exatamente o terreno dele.

---

### LINHA 2 — Skydance Animation Madrid · Environment Surfacing Artist

| Campo | Valor |
|---|---|
| **Estúdio** | Skydance Animation Madrid (grupo **Paramount** — a regra 14 se aplica) |
| **Título exato** | `Environment Surfacing Artist` |
| **ID da requisição** | **`c5793932-893f-418a-a24a-7749fcf1c90e`** |
| **Cidade/País** | Madri, **Espanha** — `workplaceType: hybrid`, `country: ES` |
| **Família de ATS** | **LEVER** |
| **URL do anúncio** | `https://jobs.lever.co/skydance/c5793932-893f-418a-a24a-7749fcf1c90e` |
| **URL de candidatura** | `https://jobs.lever.co/skydance/c5793932-893f-418a-a24a-7749fcf1c90e/apply` — **HTTP 200** (778.677 bytes) |
| **Publicada** | `createdAt 1785402803635` → **2026-07-30** |
| **Formato** | `Full Time`, híbrido |
| **Faixa publicada** | **NÃO.** `salaryRange: null` na API do Lever |

**DISCIPLINA — é o núcleo exato do portfólio dele:**

> *"Creates textures using photographic references, digital hand-painted techniques, existing texture
> assets, and procedural workflows."*
> *"**Paints stylized textures** based on concept art while maintaining the visual style of the show
> using **Substance 3D Paint and Photoshop**."*
> *"Creates procedural textures using **Substance 3D Designer**."*
> *"Demonstrates a strong understanding of **physically based shading principles**, including material
> properties such as albedo, reflection, refraction, roughness, and subsurface scattering."*

Textura/surfacing estilizado. É a disciplina dele escrita palavra por palavra.

**RÉGUA DE VETO — texto integral de 8.346 caracteres da API do Lever. 4 casamentos, os 4 falsos
positivos:**

- `authoriz` ×2 → *"If you suspect that you are being contacted by an **unauthoriz**ed person or
  believe that the correspondence you have received is suspicious…"* — é o **Recruitment Fraud
  Alert**, aviso antifraude de recrutamento. **Falso positivo**, mesmo gênero da cláusula
  anti-agência já catalogada.
- `within the` → *"Authors and modifies materials using standard and procedural shading workflows
  **within the** main rendering engines."* — é o pipeline técnico. **Falso positivo.**
- `only` → *"Skydance will **only** contact you from an official '@skydance.com' email address."* —
  mesmo aviso antifraude. **Falso positivo.**
- `spanish` (lista de idioma local) → *"High English level desirable. **Spanish desirable.**"* —
  **DESEJÁVEL, não exigido.** A régua veta *exigência* de idioma local; "desirable" não é exigência.
  **Falso positivo**, e registro a frase inteira para você julgar sozinho.

**Nenhum dos vinte termos aparece como veto. Veto escrito: zero.**

**DEDUPE — arquivo por arquivo, pelo ID:**

| Arquivo | `c5793932-893f-418a-a24a-7749fcf1c90e` |
|---|---|
| `enviados.csv` | **0** |
| `automacao/processados.csv` | **0** |
| `docs/index.html` | **0** |
| `automacao/FILA-DO-VINI.md` | **0** |

**Grep pela CASA, porque a Skydance é familiar (regra 6).** `grep -oE "jobs.lever.co/skydance/[a-z0-9-]{20,}"` nos quatro arquivos devolve **seis** requisições, e **nenhuma é esta**:

| ID no painel | Título | Estado que li até o fim da célula |
|---|---|---|
| `9084fa54-…` | Character Designer, Santa Monica | registrada |
| `90d2f2b7-…` | **Senior** Environment Surfacing Artist, Madri | registrada, "A MAO POR hCAPTCHA" — **e hoje NÃO está mais no quadro do Lever: fechou** |
| `9ad28cab-…` | Senior Grooming TD, Madri | registrada, na `FILA-DO-VINI.md` |
| `9f8e7d96-…` | Visual Development, LA | **VAGA EXPIRADA (404 na API em 07/09)** |
| `ebbcdae8-…` | Environment Modeling Artist, Madri | registrada, "A MAO por hCaptcha" |
| `f3ee86d4-…` | Environment Surfacing **Lead** Artist, Madri | `processados.csv` 07/09, "A MAO por hCaptcha do Lever" |

A `90d2f2b7` é a **Senior** Environment Surfacing Artist e a `f3ee86d4` é a **Lead**. Esta
(`c5793932`) é a **Environment Surfacing Artist** sem qualificador — **terceira requisição distinta
da mesma família de surfacing, e a única das três que nunca foi registrada.** O quadro do Lever hoje
lista sete vagas de Madri e esta é uma delas; a `90d2f2b7` sumiu.

**RESSALVA HONESTA, e ela é operacional, não de encaixe.** **O Lever é parede conhecida desta
campanha.** Medi hoje: a página `/apply` devolve 200 mas o HTML traz `hcaptcha`, `recaptcha` e
`captcha`. O painel já documentou a parede com clique real na Behaviour, na Quantic Dream e na
própria Avalanche. **Esta linha é para a SUA mão, não para a automação**, e o dossiê campo a campo
da Skydance já está pronto em `automacao/respostas-formularios.md` — as respostas de
`ebbcdae8`/`f3ee86d4` servem, é o mesmo formulário.

Ressalva de cadência, também honesta: a campanha tem **duas** candidaturas Skydance paradas na
parede do hCaptcha (`f3ee86d4` de 07/09 e `ebbcdae8`). **Nenhuma delas consta como enviada em
`enviados.csv`** — conferi, `grep` de `skydance` em `enviados.csv` devolve **zero**. Ou seja: a casa
ainda não recebeu nada. Se você for mandar uma à mão hoje, esta é a de senioridade certa (as outras
novas do quadro são Trainee e Junior, §4).

---

### LINHA 3 — Jam City · Level Design Artist

| Campo | Valor |
|---|---|
| **Estúdio** | Jam City (divisão Narrative Games) |
| **Título exato** | `Level Design Artist` |
| **ID da requisição** | **`787abb3b-1009-42f3-bf82-9846dff0e646`** |
| **Cidade/País** | San Francisco, CA, **EUA** — `workplaceType: onsite`, `country: US` |
| **Família de ATS** | **LEVER** |
| **URL do anúncio** | `https://jobs.lever.co/jamcity/787abb3b-1009-42f3-bf82-9846dff0e646` |
| **URL de candidatura** | `https://jobs.lever.co/jamcity/787abb3b-1009-42f3-bf82-9846dff0e646/apply` — **HTTP 200** (743.133 bytes) |
| **Publicada** | `createdAt 1787167666762` → **2026-08-19** |
| **Faixa publicada** | **SIM: `Pay Range: $90,000 — $110,000 salary per year.`** |

**DISCIPLINA — é level art COM modelagem, que o briefing aceita por escrito:**

> *"**Edit or create high-quality and optimized 3D environments and props.**"*
> *"Lit 3d scenes that are optimized for mobile devices."*
> *"3+ years of 3D game experience"* · *"Complete mastery of Unity Engine"* ·
> *"Great knowledge of **Maya** and Adobe Creative Suite"* · *"Experience with **PBR materials**"*
> *"Identify, troubleshoot and resolve visual issues with in-game **environment assets** and character
> environment interaction."*

Não é design de nível puro: o anúncio manda criar e editar ambiente e prop 3D, iluminar cena e
trabalhar material PBR em Maya/Unity. **Entra pela regra "level art com modelagem".**

**RÉGUA DE VETO — texto integral de 10.958 caracteres. 8 casamentos, os 8 falsos positivos:**

- `sponsor` ×4 → *"100% Covered Medical and **Company-Sponsored** Dental & Vision (Plans Vary)"* —
  é o **bloco de benefícios**. **Falso positivo**, exatamente o caso já catalogado.
- `only` ×4 → *"***Only** applies to full-time positions.*" — é a nota de rodapé do bloco de
  benefícios. **Falso positivo.**

Nenhuma ocorrência de `authoriz`, `eligib`, `work permit`, `must be based`, `based in`, `only from`,
`LMIA`, `days a week`, `days per week`, `days in the office`, `resident`, `relocat`, `located in`,
`unable to support`, `no relocation`, `within the`, nem exigência de idioma local — o único requisito
de idioma é *"Excellent grasp of the English language."* **Veto escrito: zero.**

**DEDUPE — arquivo por arquivo, pelo ID:**

| Arquivo | `787abb3b-1009-42f3-bf82-9846dff0e646` |
|---|---|
| `enviados.csv` | **0** |
| `automacao/processados.csv` | **0** |
| `docs/index.html` | **0** |
| `automacao/FILA-DO-VINI.md` | **0** |

**Grep pela CASA (regra 6):** `jobs.lever.co/jamcity/` devolve **uma** requisição nos quatro
arquivos, `14272af5-efc7-4150-8b59-dcabdaa8c578` (Principal 3D Generalist, San Francisco), presente
em `docs/index.html` ×2 e na `FILA-DO-VINI.md` ×1, e **zero em `enviados.csv` e `processados.csv`** —
ou seja, registrada e não enviada. **Esta é requisição diferente e inédita.**

**RESSALVAS HONESTAS, três, e você decide:**
1. **Parede do Lever**, igual à linha 2: `/apply` responde 200 mas o HTML traz `hcaptcha` e
   `recaptcha`. Clique seu, não da automação. O painel já lista a Jam City entre as casas onde a
   parede do hCaptcha foi medida com clique real.
2. **`onsite` em San Francisco**, sem uma linha de remoto no anúncio. Não há veto escrito de
   autorização — não há uma única menção a visto no texto inteiro —, mas o cargo é presencial nos EUA.
3. **É jogo mobile de objetos escondidos (Hidden Object)**, não AAA nem animação. O anúncio pede
   *"3+ years of 3D game experience, with HIdden Object Game experience preferred"*. Encaixe de
   disciplina: sim. Encaixe de prestígio de portfólio: fraco. A faixa publicada de USD 90–110k é o
   dado a favor.

---

## 3. REGISTRADAS COM RESSALVA — leia antes de clicar

### 3.1 Makeshift Software · Associate Character Modeler `300872` e Associate Environment Artist `300742` — ⛔ **CADÊNCIA OCUPADA HOJE**

| | Associate Character Modeler | Associate Environment Artist |
|---|---|---|
| **ID** | `300872` | `300742` |
| **URL (HTTP medido)** | `https://jobs.gohire.io/makeshift-software-hnqmphxc/associate-character-modeler-300872/` — **200** (20.947 b) | `https://jobs.gohire.io/makeshift-software-hnqmphxc/associate-environment-artist-300742/` — **200** (21.031 b) |
| **Dedupe pelo ID** | `enviados.csv` 0 · `processados.csv` 0 · `docs/index.html` 0 · `FILA-DO-VINI.md` 0 | idem, **0/0/0/0** |

**Dedupe pelo ID dá limpo nas duas. E mesmo assim eu SEGURO, e o motivo está escrito em
`enviados.csv` de hoje.** Grep de `makeshift`/`300611` até o fim da célula:

> `…"Columbus, Ohio, EUA (remoto 3 a 6 meses, depois hibrido)",portal,https://jobs.gohire.io/makeshift-software-hnqmphxc/senior-environment-artist-300611/,**enviada**,"DUAS PROVAS: POST 200 em api.gohire.io/apply?clientHash=hnqMpH…`
> `docs/index.html`: *"**ENVIADA E CONFIRMADA em 09/09**, vaga 300611, publicada em 07/…"*

**A Makeshift recebeu candidatura HOJE (09/09, a `300611`) e já tinha recebido em 07/09 (a `299993`,
Senior Character Modeler).** Pela regra 8, casa que recebeu candidatura hoje só entra na fila
marcada: **está marcada, "cadência ocupada hoje".** São três batidas na mesma caixa de um estúdio de
dez vagas em três dias. O aviso do `caca-agregadores-0909-tarde.md` já dizia isso e a `300611` foi
enviada mesmo assim — **as outras duas eu não empurro sem você mandar.**

Nota de senioridade que continua valendo: as duas são "Associate", nível abaixo do dele, e a
`300872` é descrita como *"a character modeler early in their career"*. Disciplina certa, rótulo
errado.

### 3.2 Larian Studios · Environment Artist – Open Application `9bd7d394-e1cc-4acf-8176-68eb2b08aa18`

- **URL de candidatura:** `https://jobs.lever.co/larian/9bd7d394-e1cc-4acf-8176-68eb2b08aa18/apply` — **HTTP 200** (741.709 bytes)
- **Local:** `Any` (Gent, Dublin, Barcelona, Guildford, Varsóvia, Quebec, Kuala Lumpur) · `onsite`
- **Publicada:** `createdAt 1747305090649` → **2025-05-15** — banco de talentos antigo
- **Régua:** 4 casamentos, os 4 no marcador `(Version française ci-dessous)` e no corpo francês do
  próprio anúncio bilíngue. **Falso positivo**: é a tradução do anúncio, não exigência de idioma.
  Nenhum dos vinte termos aparece. **Veto: zero.**
- **Dedupe pelo ID:** `enviados.csv` 0 · `processados.csv` 0 · `docs/index.html` 0 · `FILA-DO-VINI.md` 0. **Limpo.**

**POR QUE MESMO ASSIM EU SEGURO.** Grep pela casa: `jobs.lever.co/larian/` devolve duas requisições
nos quatro arquivos, e li a de `64e1e658-7c7a-4c7f-b950-f997d40a9d8e` até o fim da célula:

> *"AVISO DE DUPLICIDADE, para ninguem mandar uma terceira: a MESMA requisicao
> 64e1e658-7c7a-4c7f-b950-f997d40a9d8e tem DUAS entradas no painel, uma pelo jobs.lever.co e outra
> pelo larian.com/careers, e **as duas passam a valer como enviadas**. A candidatura cobre os sete
> escritorios da Larian…"*

A `64e1e658` é o **Character Artist – Open Application** da mesma casa, e **já foi enviada**. Este
aqui é o **Environment Artist – Open Application**: segundo banco de talentos genérico, na mesma
caixa, com a candidatura anterior cobrindo os mesmos sete escritórios. É o mesmo raciocínio que
segurou a espontânea da Playdead no `caca-breezy-homerun.md`: espontânea vale quando a casa não tem
porta melhor aberta — e aqui a porta espontânea da disciplina principal dele já foi usada.
**Guardar para quando a primeira for respondida ou morrer.**

### 3.3 Behaviour Interactive · Art director – Unannounced project `4db7b168-3106-4b40-9abe-9f27d510f62c`

- **URL de candidatura:** `https://jobs.lever.co/bhvr/4db7b168-3106-4b40-9abe-9f27d510f62c/apply` — **HTTP 200** (734.155 bytes)
- **Local:** Montreal, QC, Canadá · `hybrid` · publicada **2026-06-25**
- **Régua de vinte termos, texto integral de 13.744 caracteres: ZERO casamentos.** Nem `authoriz`,
  nem `sponsor`, nem `resident`, nem `days a week`. **E ZERO menção a francês** — busquei `french`,
  `français` e `francais` no texto inteiro: nenhuma. Numa vaga de Montreal isso é notável e é a favor.
- **Dedupe pelo ID:** **0/0/0/0.** Grep pela casa: `jobs.lever.co/bhvr/` devolve quatro requisições
  registradas (`18024240`, `55fa65fe`, `86ddd557`, `976b2a8c`), **nenhuma é esta.** Requisição inédita.

**POR QUE NÃO PONHO NA FILA PRINCIPAL: disciplina.** O anúncio diz, com todas as letras:

> *"This is **primarily a creative and conceptual role**, where you'll spend most of your time
> **visually exploring ideas** to guide the development team."*
> *"Define the overall art direction and visual identity for a new, unannounced IP"*

É direção de arte conceitual de IP, não produção 3D — o eixo que o briefing exclui ("conceito 2D",
"direção de arte gráfica"). E ele é Senior Character Artist, não Art Director. **Marginal nos dois
eixos, sem veto escrito. Fica registrada, decisão sua.** Se for, é à mão: a Behaviour é uma das casas
onde a parede do hCaptcha do Lever foi medida com clique real.

### 3.4 bondex · 3D Stylized Environment Artist `189496` — GoHire

- **URL de candidatura:** `https://jobs.gohire.io/bondex-vcm9mgen/3d-stylized-environment-artist-189496/` — **HTTP 200** (15.625 bytes)
- **Dedupe pelo ID `189496`:** `enviados.csv` 0 · `processados.csv` 0 · `docs/index.html` 0 · `FILA-DO-VINI.md` 0. **Limpo.**
- **Disciplina: perfeita.** *"Craft **stylized models** for various environments, structures, lighting
  scenarios, and props… utilizing tools like **Maya and ZBrush**"*, *"Expertise in software tools such
  as **Substance Painter, Maya, and ZBrush**"*.
- **Faixa publicada: `Salary 70000 - 150000 USD Per annum`.**
- **Régua:** 1 casamento — *"To be **eligib**le for this role, applicants must meet the following
  criteria: A minimum of 5 years of professional experience as an Environment Artist…"* — é
  **critério de experiência**, não de autorização de trabalho. **Falso positivo.** Frase A FAVOR no
  mesmo anúncio: *"Location: **Fully Remote** · **Global Applicants: Welcomed from all countries**"*.
  **Veto escrito: zero.**

**DUAS RESSALVAS QUE ME FAZEM NÃO PÔR NA FILA:**
1. **`Date Posted: August 30th, 2024`** — o próprio anúncio declara a data. É de **dois anos atrás**.
   O quadro está vivo e a página responde 200, mas isso é anúncio velho parado no ar, não vaga nova.
2. **Local declarado: `Philippines, Panama`.** Nenhum dos dois está no recorte geográfico, ainda que
   o corpo diga "Fully Remote / Global". Fica registrado com a contradição escrita, e a decisão é sua.

---

## 4. DESCARTADAS COM MOTIVO ESCRITO — frase inteira colada

### 4.1 Descartadas por VETO ESCRITO — 4

| Casa / vaga | ID | Família | Frase literal que mata | Classificação |
|---|---|---|---|---|
| **Stirling Animation Studios — Environment Modelers** | `81` | BambooHR | *"**Artists must be based regionally within the UK (outside the M25)** and we're particularly keen to connect with Scotland-based artists."* | **VETO DE VERDADE.** Bate em `must be based`. É exigência escrita de residência prévia, não descrição de onde o cargo fica. Dói registrar: o dedupe pelo ID dava **0/0/0/0**, era a **única** linha limpa de toda a família BambooHR, o quadro responde 200 e a disciplina é exata (*"Demonstrable experience of using Maya for Modelling and Sculpting"*). **Veto escrito desqualifica.** |
| **HyperHug — 3D Environment & Prop Artist** | `bd5519f4-95f9-4c0b-90f2-b191e290b1af` | Ashby | *"**English - B1+ level, Russian - C1 level.**"* | **VETO DE IDIOMA, reconfirmado hoje na fonte.** O painel já registrou este veto em 07/09; conferi que a frase **continua no ar** no `descriptionPlain` da API do Ashby. |
| **HyperHug — 3D Artist (weapon skins)** | `5470c42c-1502-42aa-a3de-3ce213fb62d8` | Ashby | *"**English - B1+ level, Russian - C1 level.**"* | **VETO DE IDIOMA.** Dedupe pelo ID dava **0/0/0/0** (só a irmã estava registrada), mas o veto é o mesmo e está na mesma seção "What We Expect From You". |
| **thatgamecompany — 3D Character Artist (Mid-Senior)** | `36e101a4-c7ba-4884-8999-cd04abb979ee` | Ashby | *"**Applicants must be authorized to work for any employer in the U.S or Canada. We are unable to sponsor or take over sponsorship of an employment Visa at this time.**"* | **VETO DUPLO** (`authoriz` + `sponsor` + `unable to support`). Já registrado no painel em 07/09 com o veredito "VETO DE RESIDENCIA E NAO APLICAR". Confirmado vivo no quadro Ashby hoje. Faixa publicada USD 81.000–114.000. |

### 4.2 Descartadas por DEDUPE SUJO — 14 (li todas as ocorrências até o fim da célula)

| Casa / vaga | ID | Onde já estava |
|---|---|---|
| Volka — 3D Artist | `fa36e503-…` | `docs/index.html` 1 + **`FILA-DO-VINI.md` 1** — já está na sua fila |
| Avalanche Studios — Lead Character Artist | `8f7bd580-…` | `docs/index.html` 2 + **`FILA-DO-VINI.md` 1** — parede do Lever medida com clique real, dossiê pronto |
| Behaviour — Senior 3D Character Artist, 7 Days to Die | `976b2a8c-…` | `docs/index.html` 1 + **`FILA-DO-VINI.md` 1** — achada em 08/09 |
| Skydance — Environment Surfacing **Lead** Artist | `f3ee86d4-…` | `processados.csv` 07/09 ("A MAO por hCaptcha") + `docs/index.html` 1 |
| Skydance — Environment Modeling Artist | `ebbcdae8-…` | `docs/index.html` 2 |
| Skydance — Senior Grooming TD | `9ad28cab-…` | `processados.csv` 1 + `docs/index.html` 1 + `FILA-DO-VINI.md` 1 |
| Larian — Character Artist Open Application | `64e1e658-…` | `processados.csv` 2 + `docs/index.html` 2 + `FILA-DO-VINI.md` 1 — **ENVIADA**, com aviso de duplicidade escrito |
| Jam City — Principal 3D Generalist | `14272af5-…` | `docs/index.html` 2 + `FILA-DO-VINI.md` 1 |
| Certain Affinity — Advanced/Senior Material Artist (Vancouver) | `AgAMjfmeKe` | `docs/index.html` 1 — registrada 07/09, **reCAPTCHA v2 com desafio de imagem**, "fica A MAO" |
| Certain Affinity — Advanced/Senior Material Artist (Toronto) | `eJTHIpzicy` | `docs/index.html` 1 — mesma nota, mesmo formulário |
| Image Engine — General Application Assets (Modeling/Texturing/LookDev/Grooming) | `21` | `processados.csv` 2 + `docs/index.html` 1 |
| Image Engine — Look Development Artist Senior / Texture & LookDev Mid | `28`, `183` | `processados.csv` + `docs/index.html` |
| Icon Creative — Intermediate Modeling/Texture Artist | `136` | `processados.csv` 1 + `docs/index.html` 1 + `FILA-DO-VINI.md` 1 |
| Barnstorm VFX (`176`, `204`), IGG (`289`), OWI (`198`, `199`), Budge (`26`), Funday (`279`), Stirling (`77`, `79`, `82`), Playdead (`a235c228566a01`, `d6b5a5e4f54a01`), AGBO (`49a139476416`, `cdc4c6df4fd8`), Walla Walla (`f1578014d426`), Warhorse (`5e0abb1243c101`) | vários | todos com ocorrência registrada nos quatro arquivos; nenhum é achado novo desta rodada |

### 4.3 Descartadas por ESCOPO GEOGRÁFICO — 9

| Vaga | Local | Família |
|---|---|---|
| Supercell — Senior Level Artist, Project R.I.S.E (`8cb16c25-…`) | **Xangai, China** | Ashby |
| Streamline Studios — Lead Environment Artist (`81`), Lead Character Artist (`84`), 3D Character Artist (`106`), 3D Environment Artist (`169`) | **Kuala Lumpur, Malásia** | BambooHR |
| Larian — Environment Artist (`200ba4bf-…`) | **Kuala Lumpur, Malásia** | Lever |
| Jam City — 3D Artist (`5162e400-…`) | **Montevidéu, Uruguai** | Lever |
| Dream Games — Visual Development Artist (`7d2e95ca-…`) | **Istambul, Turquia** | Lever |
| Voldex — Render Artist, Driving Empire (`7ad5ac31-…`) | **Remoto — Brasil** (excluído por escrito no briefing) | Ashby |

### 4.4 Descartadas por DISCIPLINA — 17

| Vaga | Família | Motivo, com citação |
|---|---|---|
| **Funday Agency — Senior Art Director** ×3 (`279` Toronto, `280` Calgary, `281` Vancouver) | BambooHR | **Não é estúdio de jogo nem de animação: é agência de publicidade.** O quadro inteiro são Creative Director ×3, Associate Creative Director (Art) ×3, Senior Copywriter ×3, Strategist (Marketing/Advertising) ×3, Senior Account & Project Manager (Advertising Agency) e "Funday Agency - General Application". É **direção de arte gráfica/publicitária**, eixo excluído. Os IDs `280` e `281` dão dedupe **0/0/0/0**, e mesmo assim não entram. |
| Icon Creative — Senior Matte Painter (Stylized Environment Design Experience required) (`143`) | BambooHR | Dedupe **0/0/0/0**, mas **matte painting é pintura de fundo 2D**, o eixo "design de background/location 2D" que o briefing exclui. |
| Image Engine — General Application Matte Painting/Environment TD/Generalist (`16`) | BambooHR | Dedupe **0/0/0/0**. Metade 2D (matte painting), metade técnica (Environment TD). A porta certa da casa é a `21` (Assets: Modeling/Texturing/LookDev/Grooming) e ela **já foi usada**. |
| Image Engine — General Application Creature FX/Rigging (`15`) | BambooHR | Dedupe **0/0/0/0**. **CFX e rigging**, os dois excluídos. |
| DMFX — Artiste CFX / Creature FX Artist (`129`) | BambooHR | **CFX/simulação**, excluído. |
| Stirling — Character & Prop Riggers (`84`), Rigging Supervisor (`83`) | BambooHR | Rigging, excluído (e o veto de residência do `81` provavelmente vale para todo o quadro). |
| Stellar Entertainment — Senior Generalist & **Physics Engineer** | Ashby | É engenharia, não arte. |
| Skydance — Senior Crowds Technical Artist, Senior Rigging Artist, 2D Effects Artist | Lever | Crowd/simulação, rigging e efeito 2D. |
| Larian — Concept and 2D Artist, Lighting Artist, Technical Artist ×2, VFX Artist, Cinematic Artist (Open Applications) | Lever | Conceito 2D, iluminação, arte técnica e VFX. |
| Blackbird Interactive — VFX Artist (contrato 3 meses) · Kabam — Video Artist · SkyBox Labs — Senior Technical Artist (UE5) · ArenaNet — Technical Artist | Lever/Ashby | VFX, vídeo e arte técnica. |
| Zoic Studios — US Senior Previs Artist · Flying Bark — Lighting Key Color Script Artist · Stellar Creative Lab — Crowd Artists / Crowd TD | JazzHR | Previs, color script 2D e crowd. |
| Neowiz — 3D 애니메이터 (`7995486e-…`) | Lever | Animação. |
| AGBO — FX Artist, Rigging Artist, Technical Artist, Lead Technical Artist, Lead VFX Artist, Sr. Cinematic Layout Artist, Generalist **Engineer** | Breezy | Todos fora do eixo. |

### 4.5 Descartadas por NÍVEL, com dedupe limpo — 3

As três dão **0/0/0/0** nos quatro arquivos e passam na régua, e mesmo assim eu não mando: **nível
abaixo do dele queima a porta da casa**, que é a regra que o próprio painel escreveu para a família
de surfacing da Skydance.

| Vaga | ID | Local |
|---|---|---|
| Skydance — Junior Environment Surfacing Artist | `4c18ce73-8217-44a7-af15-b5a5f18bc07e` | Madri (régua: `authoriz`/`only` no aviso antifraude, `within the` no pipeline, "Spanish desirable" — os 4 falsos positivos, iguais aos da linha 2) |
| Skydance — Character Surfacing Trainee | `7b435bb2-09fd-4f2f-8fca-9c2fa6666adc` | Madri |
| Skydance — Environment Set Dressing Trainee | `570eb832-3f6e-47cc-9a34-f7b34ca74a92` | Madri |

---

## 5. QUADROS MEDIDOS: VIVOS E SECOS, MORTOS, OU FALSO POSITIVO DE SLUG

Levantamento, não candidatura. Fecha linha e evita varredura repetida.

**HOMERUN — 9 feeds vivos em 3.154 slugs, e só UM rendeu.**
`ustwo-games` (a linha 1) · `totalmayhemgames` (só a Open Application, e a casa **já respondeu
recusando em 07/09** — não reenviar) · **`chucklefish`**, **`crowscrowscrows`**, **`buck`** (BUCK) e
**`ghost`** — os quatro com feed vivo e **ZERO `<entry>` de vaga** · `twinswans` continua com zero,
o que **reconfirma a pendência fechada** pelo `caca-breezy-homerun.md` · `ace` e `magic` são
agências de PR/marketing, homônimos.

**Correção de método do Homerun que vale registrar:** o `caca-breezy-homerun.md` diz que "no Homerun
**200 é vivo** e o 302 leva para 404.homerun.co". Medi hoje que **isso pode enganar**:
`https://ustwo-games.homerun.co/` devolve **404** (redireciona para `404.homerun.co/working_at/ustwo-games`)
**enquanto o quadro está vivo e com cinco vagas** — só o feed `https://feed.homerun.co/<slug>`
responde 200 com o conteúdo. **A autoridade é o feed, não a raiz do subdomínio.** Se a varredura de
hoje tivesse usado a raiz, a linha 1 desta fila não existiria.

**BREEZY — 3.154 slugs, 7 quadros com vaga, ZERO achado novo.** `agbo` (18 vagas, as 4 da disciplina
já vetadas por *"Candidates must be legally authorized to work in the U.S."*), `playdead` (14, as
duas da disciplina já enviadas), `warhorsestudios` (5, a Level Artist já vetada por *"This position
is available only to Czech-speaking candidates"*), `wws` (a Walla Walla, já na fila de hoje de manhã),
`turbulent`, `puzzle-cats`, `lucky-logic` (1 vaga cada, nenhuma da disciplina). `passion` (11 vagas)
e `gaggle` (14) são homônimos fora da área — o único casamento no `gaggle` é "HR Generalist".
**Confirma o rendimento medido de manhã: esta família está esgotada para esta disciplina.**

**JAZZHR — 37 respostas 200, mas só 16 são quadro de verdade.** **Descoberta de método:** 21 das 37
devolveram exatamente **79.750 ou 79.751 bytes** — é a página de quadro vazio/estacionado do
`applytojob.com`, idêntica byte a byte para `blizzard`, `epicgames`, `king`, `linkedin`,
`cloudimperiumgames`, `bellmedia`, `stellar`, `infinite`, `dream`, `domain`, `monsters`, `this`,
`big`… **Não são quadros dessas empresas: é o mesmo shell.** Dos 16 quadros reais, a maioria é
homônimo fora da área (`happycamper` é rede de restaurantes, `playground` é cassino, `chimera` é
defesa/DARPA, `cyber` é TI federal, `city` é prefeitura, `squeeze` é rede de massagem). Da nossa
área e **com quadro vivo e ZERO vaga da disciplina**: `nextlevelgames` (4 vagas, todas design/eng),
`obsidian` (só General Application), `outplayentertainment` (só Speculative Applications),
`sagomini` (1, produto), `smgstudio` (0), `playableworlds` (0), `noodlecake` (0), `alkemyxinc`
(estágio de VFX), `tendril` (vendas), `flyingbarkproductions` (3, nenhuma da disciplina),
`zoicstudios` (5, nenhuma da disciplina).

**ASHBY — 35 quadros vivos, e 15 deles são falso positivo de slug genérico.** Confirmando de novo a
armadilha que o `caca-painel-familias.md` documentou, agora com a lista: **`rain`, `alt`, `sequence`,
`hatch`, `mirage`, `flux`, `outpost`, `resolution`, `pearl`, `union`, `hook`, `aka`, `ghost`,
`superseed`, `kog`** respondem 200 com quadro cheio e **nenhum é da nossa área** — são outras
empresas que ocupam aquele nome no Ashby. `stellar` e `stellarentertainment` são **duas contas
diferentes** e só a segunda é a Stellar Entertainment. **Com quadro Ashby vivo e ZERO vaga da
disciplina:** `amber` (21), `paradox` (7), `playground` (9), `limbic` (6), `dovetail` (8), `arkane`
(2), `arenanet` (2), `gardens` (1), `seconddinner` (2), `snowball`, `voldex` (4, a única de arte é
remoto-Brasil).

**LEVER — 19 quadros vivos.** Com vaga e **zero da disciplina**: `thinkingbox` (17), `bloom` (14),
`bentoboxent` (1), `skyboxlabs` (3, só tech art), `blackbirdinteractive` (9, só VFX), `kabam` (22,
só vídeo). `reply` (49) e `linkedin` (23) são homônimos fora da área.

**BAMBOOHR — 98 quadros vivos, 48 com pelo menos uma vaga, e a família rendeu ZERO linhas.** Casas
reais achadas que o `censo-boards-0809.csv` não listava: `ludia`, `turtlerock`, `gurustudio`,
`quanticdream`, `emberlab`, `relicentertainment`, `mundfish`, `frimastudio`, `iugo`, `uken`,
`artistsanimation`, `reactiv`, `snapshot`, `void`, `arc`, `eden`, `alive`, `avalanche`, `dovetail`,
`sony`, `urban`, `country`, `bellmedia`. **Nenhuma delas tem vaga da disciplina hoje** — a Quantic
Dream, por exemplo, tem duas vagas e as duas são "Concepteur.trice Technique Animation" e
"Animateur.trice Technique".

**GOHIRE — o quadro que mais deu trabalho, e o achado é de método.**
`https://jobs.gohire.io/sitemap.txt` responde **200 com 20.436 URLs de vaga** (o `robots.txt` aponta
para ele; `sitemap.xml` dá 404). Filtrei os 20.436 pela disciplina e sobraram 8 candidatos de
jogos/VFX. **E aí veio a armadilha:** as URLs do sitemap usam o **ID NUMÉRICO da empresa**
(`makeshift-software-10013422`) e **todas dão 404**; a URL que responde 200 usa o **hash de cliente
de 8 caracteres** (`makeshift-software-hnqmphxc`). Provei que **só o hash importa**, com controle:
`https://jobs.gohire.io/**zzz**-88dhofuw/3d-character-artist-240451/` → **200** com o título certo,
e `https://jobs.gohire.io/makeshift-software-hnqmphxc/x-**298040**/` (id de outra empresa sob o hash
da Makeshift) → **404**. O texto do slug é ignorado; o par hash+id é que resolve. **O sitemap do
GoHire não é navegável sem o hash**, e o hash não sai do sitemap.

Resolvi 6 hashes por busca na web e reconferi os quadros por `curl`: **`companion-group-ltd-88dhofuw`
e `snapshot-games-iwnh5ere` respondem 200 com o quadro VAZIO** — as vagas indexadas de "3D Character
Artist", "Senior 3D Environment Artist", "Experienced 3D Character Artist" e "3D Environment Artist"
**saíram do ar**. `supergaming-zikxnf8m` (Índia, fora do recorte) tem 1 vaga, de Roblox.
`humanitarian-operations-szujovmd` tem 1, de produção. `roblox-super-heroes-bv-45gsis6r` tem 1, de
2021. `bondex-vcm9mgen` tem 1 da disciplina, de 2024 (§3.4). `makeshift-software-hnqmphxc` tem 10, e
é a casa de cadência ocupada. **Resultado honesto do GoHire: nenhuma porta nova.**

---

## 6. O QUE EU NÃO CONSEGUI FECHAR, e está escrito

1. **O GoHire fica meio cego sem o hash de cliente.** Consegui 6 hashes por busca na web e não tenho
   como enumerar os outros. As 20.436 URLs do sitemap são a lista completa de IDs de vaga, mas sem o
   hash da empresa nenhuma delas abre. **Se algum estúdio da nossa área abriu vaga no GoHire e o
   quadro dele não está indexado, eu não o vi.** É lacuna real e não sei medi-la.
2. **A busca do próprio GoHire (`jobs.gohire.io/`) é casca de SPA** e confirma o aviso do briefing:
   POST no `searchFilterForm` com `jobTitleSearched=character+artist` devolve **200 com os mesmos
   11.717 bytes** da página vazia, dez consultas seguidas, zero link de vaga. Não conclui nada a
   partir dela.
3. **Não varri Ashby, Lever, JazzHR e GoHire com a lista curada de ~330 estúdios** que o
   `caca-breezy-homerun.md` usou no Breezy; usei os 1.497 nomes do painel, `alvos.csv` e `drafts/`.
   São universos que se sobrepõem muito, mas não são idênticos.
4. **Não reconferi a duplicata bilíngue** das quatro requisições francesas/inglesas da Behaviour
   (o `RISCO-DUPLICATA.md` avisa que o Grackle publica a mesma requisição em dois idiomas). As
   requisições da Behaviour no Lever já vêm com título bilíngue numa linha só, então o risco é baixo
   aqui, mas não medi.
5. **`media.homerun.co` continua sem identificação** — mesma pendência que o `caca-breezy-homerun.md`
   registrou. Responde 200 e não devolve título.

---

## 7. AS DUAS LIÇÕES DE MÉTODO DESTA RODADA

**1. Descarte por disciplina sem frase colada não é descarte medido.** A nota de 07/09 da ustwo
games escreveu "nenhuma de personagem, **modelagem**, textura, look dev, visual dev ou generalista
3D" olhando para uma vaga cujo anúncio diz *"Owning the full environment pipeline: modelling in
Blender, texturing"*. Dois dias de porta aberta. É o segundo caso idêntico documentado nesta campanha
(o primeiro foi a Epic, três dias). **A regra que fica: nota de descarte por disciplina precisa citar
a frase do anúncio que sustenta o descarte. Sem citação, a linha volta para a fila.**

**2. Quando a família tem duas portas, a que responde 404 pode ser a errada.** No Homerun a raiz
`<slug>.homerun.co/` devolveu 404 para um quadro vivo com cinco vagas, e só `feed.homerun.co/<slug>`
mostrou o conteúdo. É o mesmo gênero do aviso do briefing sobre SPA: **200 no curl é a casca, e 404
no curl nem sempre é a porta fechada.** Sempre bater nas duas portas da família antes de escrever
"quadro morto".
