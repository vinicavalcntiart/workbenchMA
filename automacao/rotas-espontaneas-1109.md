# ROTAS DE CANDIDATURA ESPONTÂNEA SEM CAPTCHA — caça de 11/09/2026

Tudo por `curl`. **Nenhum navegador aberto, nenhum envio, nenhum email, nenhum formulário
preenchido.** Entrega é fila pronta com dossiê; quem clica é a rodada de envio.

O gatilho: a lane Pinpoint `/register-your-interest/new`, que rendeu onze envios confirmados
em 10/09, **secou** — dez dos onze slugs já receberam candidatura e o décimo primeiro
(hyperhippo) devolve 404 no navegador. Esta rodada foi procurar a lane seguinte.

---

## 1. PLACAR DA VARREDURA, e ele vem antes de qualquer narrativa

| Plataforma | Rota testada | Slugs testados | Rotas vivas | Passaram escopo + disciplina | Passaram no dedupe |
|---|---|---|---|---|---|
| **Teamtailor `/connect`** (banco de talentos) | `https://<slug>.teamtailor.com/connect` | **152** | **127** em 200 | 24 | **12** |
| **Teamtailor, anúncio espontâneo** (`jobs.json`) | `.../jobs/<id>/applications/new` | **152** feeds lidos | **41 anúncios** em 24 inquilinos | 7 | **3** |
| **Recruitee** | `/api/offers/` + página do anúncio | **72** | **17 anúncios** em 13 inquilinos | 5 | **0** (parede, ver §5) |
| **Homerun** | `<slug>.homerun.co/` + `/open-application` + `/open-applications` | 5 inquilinos vivos × 3 rotas = **15 sondagens** | **1** | 1 | **0** (já usada) |
| **Pinpoint, slugs NOVOS** | `/en/register-your-interest/new` | **21** nomes inéditos desta rodada | **0** | — | **0** |
| **TOTAL** | | **402 sondagens** | | | **15 rotas na fila** |

**Leitura honesta.** O rendimento real desta rodada está quase todo numa plataforma só: o
**Teamtailor**. Recruitee, Homerun e Pinpoint deram **zero** e o motivo de cada um está medido
em §5, §6 e §7 — não é "não achei", é "medi e não existe".

**Correção de premissa, e ela precisa ficar escrita:** o briefing desta rodada dizia que a
campanha "nunca varreu Homerun". **Varreu:** `automacao/caca-breezy-homerun.md`, 09/09,
3.521 slugs testados, 3 quadros vivos, 1 rota espontânea, já usada. Não refiz a varredura de
slug; refiz só as rotas dos inquilinos vivos, que é o que ainda podia ter mudado.

---

## 2. A LACUNA QUE ESTA RODADA FECHOU

A varredura de 10/09 (`automacao/bancos-de-talentos-1009.md`, §5) testou o `/connect` em
**62 slugs Teamtailor**. A campanha conhece **152**: 32 no `censo-boards-0809.csv`, 95 no
`quadros-tt-rec-1545-1009.csv` e o resto espalhado em `enviados.csv`, `processados.csv`,
`docs/index.html` e nos relatórios de caça. Colhi os 152 por `grep` de `*.teamtailor.com` no
repositório inteiro e testei **todos**. Foi aí que estavam as portas novas.

E apareceu uma **segunda rota espontânea do Teamtailor que a campanha usava sem nomear**: o
**anúncio de candidatura espontânea** (`Open Application`, `Unsolicited Application`,
`General Application`, `Expression of interest`, `Spontanansökan`, `Initiativbewerbung`). Ela
não é o `/connect`: é uma requisição de verdade, com id próprio, que entra no funil como
candidatura e não como cadastro de banco. Foi por ela que saíram Axolot, Funday, CI Games e
Ankama em 07/09. Varri os 152 feeds `jobs.json` procurando esses títulos e achei **41 anúncios
em 24 inquilinos**.

---

## 3. FILA FINAL NUMERADA — 15 rotas

Ordem: encaixe de personagem primeiro, depois porte da casa, depois confiabilidade da rota.
**Em todas: escopo conferido, disciplina conferida, `dedupe-agora.sh` rodado com os dois
argumentos.**

> **Aviso que vale para as 15:** "sem sinal de captcha no HTML" é o que eu medi. **Não é
> "sem captcha".** O desafio do Teamtailor, quando existe, é **verificação por email depois
> do Submit** (a tela diz *Verify your email* e quem parar aí acha que enviou). Quem enviar
> tem que abrir o link do email e conferir que a tela passa a dizer *Applied to*.

---

### 1. Liquid Swords — Suécia — `Open Application`

- **Por que presta:** estúdio AAA sueco de IP própria, produção interna de personagem, e o
  próprio anúncio convida: *"Still want to be part of writing future history in the games
  industry with Liquid Swords? (...) please register your interest to work with us"*.
- **URL:** `https://liquidswords.teamtailor.com/jobs/1851070-open-application/applications/new`
- **Medido:** `000` / 0 bytes. O 301 leva para `https://careers.liquidswords.com/...` e o
  domínio próprio **não resolve por esta rede** (três tentativas, todas 000). O anúncio existe:
  o `jobs.json` do inquilino o devolve, com id `1851070`.
- **Captcha no HTML:** não avaliável — corpo vazio.
- **Dedupe:** `sh automacao/dedupe-agora.sh 1851070 "Liquid Swords"` → **nenhuma ocorrência
  nos quatro arquivos**; `grep -i "liquid swords"` em `enviados.csv` e `processados.csv` → 0 e 0.
- **PRECISA DE CONFIRMAÇÃO NO NAVEGADOR? SIM, e é obrigatória.** É o mesmo padrão do
  `careers.ilpvfx.com`, que o BRIEF-JHON registra como domínio próprio bloqueado pelo nosso
  proxy e acessível no navegador do Vini. Vai em primeiro lugar porque é a melhor casa da lista,
  não porque é a rota mais fácil.

### 2. Facepunch Studios — Reino Unido (Walsall) — `/connect`

- **Por que presta:** Rust e Garry's Mod, arte de personagem feita em casa, estúdio próprio
  sem publisher.
- **URL:** `https://facepunch.teamtailor.com/connect` → `https://careers.facepunch.com/connect/candidates/new`
- **Medido:** **200**, **69.616 bytes**.
- **Captcha no HTML:** **nenhum sinal** (zero ocorrência de `recaptcha`, `hcaptcha`,
  `turnstile`, `datadome`, `challenges.cloudflare`).
- **Formulário conferido:** `candidate[consent_given]`, `candidate[department_id]`,
  `candidate[email]`, `candidate[role_id]` — os quatro presentes, é cadastro de verdade.
- **Dedupe:** `sh automacao/dedupe-agora.sh facepunch "Facepunch"` → **inédito nos quatro
  arquivos**; 0 ocorrências em `alvos.csv`.
- **Navegador antes do envio?** Não. Corpo grande e formulário completo no HTML servido.

### 3. Neon Giant — Suécia (Uppsala) — DUAS rotas

- **Por que presta:** The Ascent. Casa pequena de veteranos AAA, personagem estilizado e
  criatura no núcleo do jogo. O anúncio espontâneo diz: *"We're always on the lookout for
  senior professionals of exceptional talent (...) want to work on AAA quality titles"*.
- **URL A (anúncio espontâneo, preferida):** `https://neongiant.teamtailor.com/jobs/1518164-rockstar/applications/new`
  — **200**, **97.325 bytes**, **nenhum sinal de captcha**.
- **URL B (banco de talentos):** `https://neongiant.teamtailor.com/connect` →
  `https://jobs.neongiant.se/connect/candidates/new` — **200**, **50.274 bytes**,
  **nenhum sinal de captcha**.
- **Dedupe:** `sh automacao/dedupe-agora.sh 1518164 "Neon Giant"` → **inédito**; 0 em `alvos.csv`.
- **Atenção medida:** no `/connect` o HTML servido traz `candidate[department_id]` e
  `candidate[email]` mas **não traz `candidate[consent_given]`**. Pelo BRIEF-JHON, caixa de
  consentimento **ausente** (`null`) é a variante de login e pode enviar; caixa que **existe e
  não marcou** (`false`) é a armadilha do gêmeo escondido. Conferir na hora.
- **Navegador antes do envio?** Não.

### 4. The Gang — Suécia, Portugal, Reino Unido e Montreal — `/connect`

- **Por que presta:** um dos maiores estúdios de UGC do mundo (Roblox e UEFN), arte 3D
  estilizada em volume, times em quatro países do escopo.
- **URL:** `https://thegang.teamtailor.com/connect` → `https://careers.thegang.io/connect/candidates/new`
- **Medido:** **200**, **105.307 bytes**.
- **Captcha no HTML:** **nenhum sinal**.
- **Formulário conferido:** consentimento, departamento, email e **função** — os quatro.
- **Dedupe:** `sh automacao/dedupe-agora.sh thegang "The Gang"` → **inédito nos quatro
  arquivos**; 0 em `alvos.csv`.
- **Navegador antes do envio?** Não.

### 5. MindArk — Suécia (Gotemburgo) — `/connect`

- **Por que presta:** Entropia Universe, MMO cujo produto é avatar e personagem.
- **URL:** `https://mindark.teamtailor.com/connect` → `https://career.mindark.com/connect/candidates/new`
- **Medido:** **200**, **51.928 bytes**. Quadro público com **zero vaga** — ou seja, o banco
  **é** a porta.
- **Captcha no HTML:** **nenhum sinal**.
- **Formulário:** `candidate[department_id]` e `candidate[email]`; **sem `consent_given` no
  HTML servido** (mesma ressalva do item 3).
- **Dedupe:** `sh automacao/dedupe-agora.sh mindark "MindArk"` → **inédito**; 0 em `alvos.csv`.
- **Navegador antes do envio?** Não.

### 6. Kinda Brave Entertainment Group — Suécia (Umeå) — `/connect`

- **Por que presta:** grupo sueco de estúdios de jogo com produção própria de arte.
- **URL:** `https://kindabrave.teamtailor.com/connect` → `https://careers.kindabrave.com/connect/candidates/new`
- **Medido:** **200**, **40.549 bytes**. Quadro público com zero vaga; o banco é a porta.
- **Captcha no HTML:** **nenhum sinal**.
- **Formulário:** consentimento, departamento e email.
- **Dedupe:** `sh automacao/dedupe-agora.sh kindabrave "Kinda Brave"` → **inédito**; 0 em `alvos.csv`.
- **Navegador antes do envio?** Não.

### 7. Last Arrow Games — Reino Unido (Gateshead) — `/connect`

- **Por que presta:** a única vaga aberta do quadro é **Senior / Lead Animator**, o que prova
  pipeline de personagem montado. Casa nova, time pequeno.
- **URL:** `https://lastarrowgames.teamtailor.com/connect` → `https://careers.lastarrowgames.com/connect/candidates/new`
- **Medido:** **200**, **46.465 bytes**.
- **Captcha no HTML:** **nenhum sinal**.
- **Formulário:** `candidate[consent_given]` e `candidate[email]`; **sem `department_id`** no
  HTML servido, então ou é casa de departamento único ou a lista é desenhada por JavaScript
  (o BRIEF-JHON avisa que a lista de departamentos do `/connect` costuma ser Stimulus).
- **Dedupe:** `sh automacao/dedupe-agora.sh lastarrowgames "Last Arrow"` → **1 ocorrência, e
  ela NÃO é envio**: a linha de `processados.csv` é a lista de "QUADROS NOVOS GUARDADOS" de
  uma varredura, sem marca de candidatura. Seção 2 do dedupe: **nenhuma marca de envio**.
- **Ressalva do anúncio, e ela é real:** *"This role is based at our studio in Gateshead and
  therefore it is imperative that you live within a commutable distance"*. Isso vale para a
  **vaga de animador**, não para o banco de talentos, mas mostra a inclinação da casa.
- **Navegador antes do envio?** Não.

### 8. Pixion Games — 100% remoto, time distribuído — `/connect`

- **Por que presta:** Fableborne, ARPG mobile estilizado, personagem no centro. O próprio
  texto: *"Pixion is a globally distributed, fully remote and multicultural team"*. Casa
  totalmente remota vale pelo briefing mesmo fora da lista de países.
- **URL:** `https://pixiongames.teamtailor.com/connect`
- **Medido:** **200**, **39.552 bytes**.
- **Captcha no HTML:** **nenhum sinal**.
- **Formulário:** consentimento, departamento e email.
- **Dedupe:** `sh automacao/dedupe-agora.sh pixiongames "Pixion"` → **1 ocorrência, e ela NÃO
  é envio**: mesma lista de "QUADROS NOVOS GUARDADOS". Nenhuma marca de envio.
- **Navegador antes do envio?** Não.

### 9. PFX — Tchéquia (Praga) — `Expression of interest` (requisição NOVA)

- **Por que presta:** casa de VFX com criatura e personagem digital.
- **URL:** `https://pfx.teamtailor.com/jobs/8104758-expression-of-interest/applications/new`
- **Medido:** **200**, **227.545 bytes**.
- **Captcha no HTML:** **nenhum sinal**.
- **Dedupe:** `sh automacao/dedupe-agora.sh 8104758 "PFX"` → **id inédito nos quatro arquivos**.
- **PORÉM, e leia isto antes de clicar:** a campanha **já enviou** para a PFX pela
  `General Application` **5428747** em 06/09, e mandou carta fria para `info@pfx.tv` em
  28/08. A casa respondeu agradecendo e dizendo que não tem vaga aberta. A `8104758` é uma
  **requisição diferente e mais nova**, aberta pela própria casa, então não é duplicata pela
  régua da regra 18 — mas é a **terceira batida na mesma porta em duas semanas**. Fica na
  fila porque o dedupe deu limpo por id; a decisão de clicar é de quem envia, e eu escreveria
  que **não vale o desgaste agora**.

### 10. Lightheart Entertainment — Finlândia (Helsinque) — `Open Application` + `/connect`

- **Por que presta:** estúdio finlandês de jogos, time pequeno e autônomo.
- **URL A:** `https://lightheartentertainment.teamtailor.com/jobs/1344945-open-application/applications/new`
  → `https://careers.lightheart.games/...` — **200**, **116.885 bytes**, **nenhum sinal de captcha**.
- **URL B:** `https://lightheartentertainment.teamtailor.com/connect` — **200**, **47.697 bytes**,
  **nenhum sinal de captcha**; formulário com `department_id` e `email`, **sem `consent_given`**.
- **Dedupe:** `sh automacao/dedupe-agora.sh 1344945 "Lightheart"` → **inédito**; 0 em `alvos.csv`.
- **Ressalva escrita pela própria casa:** *"Lightheart is currently not hiring for any role."*
  O anúncio espontâneo continua aberto, então é banco de talentos declarado, não vaga.
- **Navegador antes do envio?** Não.

### 11. GOALS — Suécia (Estocolmo, remote-first) — `/connect`

- **Por que presta:** *"GOALS is a remote-first game studio, with HQ in Stockholm"*, jogo de
  futebol com elenco de personagem realista. Encaixe de personagem existe, mas é registro
  realista e não estilizado.
- **URL:** `https://goals.teamtailor.com/connect` → `https://tt.playgoals.com/connect/candidates/new`
- **Medido:** **200**, **95.505 bytes**. Quadro público com zero vaga.
- **Captcha no HTML:** **nenhum sinal**.
- **Formulário:** os quatro campos, inclusive `role_id`.
- **Dedupe:** `sh automacao/dedupe-agora.sh goals.teamtailor "GOALS"` → **inédito**.
- **Navegador antes do envio?** Não.

### 12. Vivid Games — Polônia (Bydgoszcz) — `/connect`

- **Por que presta:** estúdio de jogos mobile com time de arte próprio (as duas vagas abertas
  são Senior Technical Artist e Senior UI/UX Artist, ou seja, arte é departamento de verdade).
  Encaixe de personagem é **indireto**: nenhuma das vagas abertas é de personagem.
- **URL:** `https://vividgamessa.teamtailor.com/connect` → `https://jobs.vividgames.com/connect/candidates/new`
- **Medido:** **200**, **59.288 bytes**.
- **Captcha no HTML:** **nenhum sinal**.
- **Dedupe:** `sh automacao/dedupe-agora.sh vividgamessa "Vivid Games"` → **1 ocorrência, e ela
  NÃO é envio** (lista de "QUADROS NOVOS GUARDADOS"). Nenhuma marca de envio.
- **Navegador antes do envio?** Não.

### 13. Madbox — França (Paris e Annecy) — `/connect` — **CASA FRANCESA, LER §4**

- **Por que presta:** mobile com personagem estilizado (Pocket Champs), e o quadro tem
  **Art Manager** aberto, o que prova departamento de arte com peso.
- **URL:** `https://madbox.teamtailor.com/connect` → `https://careers.madbox.io/connect/candidates/new`
- **Medido:** **200**, **102.230 bytes**.
- **Captcha no HTML:** **nenhum sinal**.
- **Francês, medido nos 13 anúncios abertos:** os textos são **em inglês**; a exigência de
  francês aparece **em um único anúncio**, o HR Intern (*"You're fluent in French and
  English"*), e nenhum anúncio de arte a repete. O Game Designer só cita a cidade
  (*"We opened a new studio in Annecy (...) in the French Alps"*). **Não é porta condicionada
  ao idioma pelo que está publicado hoje**, mas é casa francesa: reconferir a exigência no
  anúncio na hora do envio.
- **Dedupe:** `sh automacao/dedupe-agora.sh madbox "Madbox"` → **inédito**; 0 em `alvos.csv`.
- **Navegador antes do envio?** Não.

### 14. Opus Major — país NÃO confirmado — `/connect`

- **Por que presta:** *"we're building more than a game, we're shaping an entertainment studio
  grounded in trust and kindness, where creativity and a passion for games and music truly
  thrive"*. É estúdio de jogo, mas **não consegui confirmar o país por `curl`**: a página de
  carreiras não publica endereço e o quadro está com zero vaga.
- **URL:** `https://opusmajor.teamtailor.com/connect` → `https://career.opusmajor.io/connect/candidates/new`
- **Medido:** **200**, **53.890 bytes**.
- **Captcha no HTML:** **nenhum sinal**. Formulário com consentimento, departamento e email.
- **Dedupe:** `sh automacao/dedupe-agora.sh opusmajor "Opus Major"` → **inédito**; 0 em `alvos.csv`.
- **Navegador antes do envio? SIM, mas por outro motivo:** não é a rota que está em dúvida, é
  o **escopo geográfico**. Só entra na fila de envio depois de alguém ler o país na tela. Fica
  em último por isso.

### 15. eRepublik Labs — Irlanda (Dublin) — `/connect`

- **Por que presta:** estúdio de jogos em Dublin, dentro do escopo. **Encaixe fraco e honesto:**
  jogo de navegador estratégico, sem elenco de personagem 3D. Entra na fila só como porta de
  entrada (regra 13), nunca como carro-chefe.
- **URL:** `https://erepublik.teamtailor.com/connect`
- **Medido:** **200**, **61.574 bytes**. Quadro público com zero vaga.
- **Captcha no HTML:** **nenhum sinal**.
- **Dedupe:** `sh automacao/dedupe-agora.sh erepublik "eRepublik"` → **inédito**.
- **Navegador antes do envio?** Não.

---

## 4. PORTAS CONDICIONADAS AO IDIOMA (regra nova de 11/09) — NÃO descartadas

Estas três têm rota aberta e sem sinal de captcha, e **ficam fora da fila de envio** porque a
casa trabalha em francês. Voltam quando o francês dele chegar ao nível.

| Casa | Rota medida | O que a medição achou |
|---|---|---|
| **Awaceb** (França/Bordeaux, Tchia) | `https://awaceb.teamtailor.com/connect` — **200**, **40.789 bytes**, nenhum sinal de captcha | A única vaga do quadro, *Animateur / animatrice Technique*, está **inteiramente em francês** (52 marcadores de francês contra 0 de inglês no texto). Casa francófona. |
| **Capsule Studio** (França/Paris) | `https://capsulestudio.teamtailor.com/connect` → `career.capsule.studio` — **200**, **76.229 bytes**, nenhum sinal de captcha | Anúncio *Assistant de production* em francês; o único termo de idioma no quadro é **`anglais`**, citado como competência adicional, o que confirma o francês como língua de trabalho. |
| **Squeeze Studio Animation** (Canadá/Quebec) | `https://squeezestudio.recruitee.com/o/candidatures-spontanees` — **200**, **327.878 bytes**, **`hcaptcha` no HTML** | Dois motivos somados: anúncio *Candidatures spontanées* inteiramente em francês **e** recusa pré-campanha registrada em 14/07 por Sophie Vigne, cujo motivo real, na versão francesa, era prazo de permissão de trabalho longo demais. **Não reabrir agora.** |

**E o caso que junta idioma com duplicata, que é o mais instrutivo da rodada:**
**Kepler Interactive** (`https://keplerinteractive.teamtailor.com/jobs.json`) publica uma
**Lead 3D Character Artist**, id `8311973`, que é título perfeito. **Não é vaga nova:** o corpo
do anúncio diz *"TACTICAL ADVENTURES est un studio (...) créé à Paris"* e pede
*"anglais professionnel (Niveau B2/C1)"* como competência **adicional** — ou seja, é a mesma
requisição da Tactical Adventures que a campanha **já enviou em 06/09**, republicada no quadro
da holding, e a língua de trabalho é francês. É exatamente a armadilha da regra 18 na forma
"mesma requisição, dois quadros, ids diferentes". **Não aplicar.**

---

## 5. RECRUITEE — MEDIDO, E É PAREDE. ZERO ROTAS.

Testei **72 slugs** pela API pública `https://<slug>.recruitee.com/api/offers/` e achei
**17 anúncios espontâneos em 13 inquilinos**. Depois abri a página de cinco deles e medi o HTML:

| Anúncio | HTTP | Bytes | Palavra de captcha achada no HTML |
|---|---|---|---|
| Framestore — *Expression of Interest 2026 - Melbourne* | 200 | 845.826 | **`hcaptcha`** |
| Squeeze Studio Animation — *Candidatures spontanées* | 200 | 327.878 | **`hcaptcha`** |
| Dovetail Games — *Open Applications* | 200 | 233.588 | **`hcaptcha`** |
| SOFTGAMES — *Unsolicited Application* | 200 | 245.348 | **`hcaptcha`** |
| Ten Square Games — *Future opportunities (f/m/d)* | 200 | 466.208 | **`hcaptcha`** |

**Cinco de cinco.** Isso confirma por medição direta o que `bancos-de-talentos-1009.md` já
tinha escrito a partir de dois casos: **o Recruitee inteiro é parede de hCaptcha**, e o
desafio nasce depois do Send. **Recruitee não é lane de envio automático.** Fica assim:

- **Framestore, Expression of Interest 2026 – Melbourne (Austrália)** é a melhor porta que
  esta rodada achou e **não entra na fila de envio, entra na fila da MÃO DELE**. A casa é a
  melhor de criatura da lista inteira, Melbourne está no escopo, e a campanha só mandou carta
  fria para `lizi.bedford@framestore.com` em 06/09 — **nunca candidatura de portal**.
  URL: `https://framestore.recruitee.com/o/expression-of-interest-2026-melbourne`.
- **Dovetail Games** e **Ten Square Games** já tinham dossiê de captcha escrito em 07/09
  (`dossie-captcha` e `portal-amao` no `processados.csv`). Não são novidade.
- **SOFTGAMES** é HTML5 casual em Berlim, sem elenco de personagem: cai por disciplina antes
  da parede.

---

## 6. HOMERUN — ZERO, E O NÚMERO É PEQUENO DE PROPÓSITO

A campanha conhece **5 inquilinos Homerun**. Testei os três formatos de rota espontânea em
cada um, 15 sondagens:

| Inquilino | `/` | `/open-application` | `/open-applications` |
|---|---|---|---|
| `totalmayhemgames` | 200 (20.568 b) | **200 (17.141 b)** | 302 → `404.homerun.co` |
| `twinswans` | 200 (20.162 b) | 302 → `404.homerun.co` | 302 → `404.homerun.co` |
| `ustwo-games` | 302 → `404.homerun.co` | 302 | 302 |
| `media` | 200 (14 b, corpo vazio) | 404 (2.260 b) | 404 |
| `giantant` | 302 → `404.homerun.co` | 302 | 302 |

**Uma única rota viva, `totalmayhemgames/open-application`, e a campanha JÁ ENVIOU por ela**
(registro em `enviados.csv` e `processados.csv`). **Zero rotas novas.**

**Não refiz a varredura de slug**, e a razão é medida, não preguiça: `caca-breezy-homerun.md`
testou **3.521 slugs em 09/09 e achou 3 quadros**. O Homerun também **não tem rota fixa** —
`/open-application` só existe se o estúdio criou uma vaga com esse nome —, então não há URL
previsível para sondar em lote. Descoberta de Homerun tem que passar pelo feed
`https://feed.homerun.co/<slug>`, um a um, com rendimento de 1 por mil.

---

## 7. PINPOINT EM SLUGS NOVOS — ZERO

Os 21 nomes de casa que esta rodada descobriu e que não estão em
`automacao/bancos-de-talentos-1009.md` foram testados contra
`https://<slug>.pinpointhq.com/en/register-your-interest/new`:

`liquidswords`, `lightheart`, `lightheartentertainment`, `neongiant`, `kindabrave`, `thegang`,
`facepunch`, `wetaworkshop`, `wetaworkshopgames`, `mindark`, `aonic`, `lastarrowgames`,
`capsulestudio`, `madbox`, `awaceb`, `pixiongames`, `vividgames`, `territorystudio`,
`erepublik`, `goals`, `opusmajor`.

**Vinte e um em 404 limpo, 11.684 bytes cada.** Nenhum quadro Pinpoint novo. Não toquei em
nenhum dos slugs Pinpoint já levantados, como mandado.

---

## 8. O QUE CAIU, COM O DADO MEDIDO

### 8.1 Caiu no DEDUPE — e duas destas eram repetição na certa

| Casa | Rota | O que o dedupe devolveu |
|---|---|---|
| **Wētā Workshop** (Nova Zelândia) | `/connect`, **200**, 58.188 b, nenhum sinal de captcha | **A pior armadilha da rodada, e ela ia passar.** Casa perfeita (criatura, Wellington, escopo), e `enviados.csv` só mostrava carta fria. Mas o `docs/index.html` diz: *"CADASTRO NO CONNECT em 02/09 pela automação (Teamtailor), disciplina Creative Services e função Concept Artists, com confi..."*, e `processados.csv` tem o email de boas-vindas do Connect (`wetaworkshop.teamtailor-mail.com`, 02/09) mais o perfil reconferido depois. **Já feita.** Some-se que o Game Studio deles **já respondeu em 07/09**. |
| **Stunlock Studios** (Suécia, Skövde) | `Open Application` `3257938`, **200**, 85.058 b, nenhum sinal de captcha | `docs/index.html`: *"CANDIDATURA ENVIADA e CONFIRMADA em 06/09 pela força-tarefa"*. A mesma linha registra que **uma segunda candidatura quase saiu em 09/09** por causa de um `s` a mais no slug. Não repetir. |
| **Untold Studios** (Londres) | `General Application` `1314008` e `1090591` | `processados.csv`: *"As DUAS General Application do quadro (1314008 e 1090591) sao exatamente as duas candidaturas que a casa ja recebeu em 06 e 07/09. (...) a Untold esta esgotada para a campanha por enquanto"*. |
| **Bulkhead Interactive** (Derby) | `OPEN APPLICATION [REMOTE]` `5744150` e `[IN-STUDIO]` `5739695` | *"JA TINHAM SIDO ENVIADAS em 07/09"*, com prova no Gmail (`joe.brammer` no domínio `bulkheadinteractive.teamtailor-mail.com`). |
| **Axolot Games** | `Open Application` `3583177` | Enviada e confirmada em 07/09 (*"Tack för din ansökan"*). |
| **CI Games** | `Open Application` `7918450` | Enviada e confirmada em 06/09, página `/thanks`. |
| **Funday Games** | `Unsolicited Application` `7277761` | Enviada e confirmada em 07/09. |
| **Gigglebug** (Finlândia) | `Open application!` `1838376` | Confirmada em 27/08 por Sanni Vainio. |
| **Star Stable Entertainment** | `Open Application` `244302` | Candidatura espontânea já confirmada; `processados.csv` de 06/09 registra a confirmação. |
| **Game Boost** (Suécia) | `Open application, Game Artists` `2814432` | Enviada em 09/09 **e a fundadora respondeu duas vezes**, a segunda dizendo *"Wow, your portfolio looks awesome!"*. |
| **REALTIME**, **Beyond Frames**, **Twin Harbour**, **Playa Games**, **Stillfront** | `/connect` e anúncios espontâneos | Todos com candidatura ou perfil Connect já registrados entre 06 e 09/09. |
| **Important Looking Pirates / Metropolis VFX** | `Metropolis Expression of Interest` `6941873` | `processados.csv`: **porta fechada medida** — a pergunta de elegibilidade de residência na Espanha bloqueia o envio, e isso é a vaga dizendo não, não defeito. |

### 8.2 Caiu no ESCOPO ou na DISCIPLINA

| Casa | Rota viva | Motivo medido |
|---|---|---|
| **Princess Bento** (Londres) | `/connect` 200 | As **quatro** vagas do quadro são 2D: *2D Rigged Animators*, *EOI - 2D Animation Directors*, *EOI - 2D Episodic Directors*, *EOI - 2D Art Directors*. **2D puro descarta.** |
| **Aonic** (Estocolmo) | `/connect` 200, 43.580 b | Não é estúdio de jogo: *"Aonic is a technology group focused on user engagement platforms for the mobile gaming and consumer insights industries"*. É ad-tech. |
| **CaptureAge** | `/connect` 200 | Única porta espontânea é `Open Application: Engineering`. Sem arte. |
| **Territory Studio** (Londres) | `/connect` 200, 42.218 b | Design de movimento e interface de tela para cinema. Não tem produção de personagem. Dedupe limpo, fica registrada. |
| **Goodgame Studios** e **New Moon Production** (Hamburgo) | `/connect` 200 | Estratégia 4X e farm mobile; as vagas de arte abertas são *Marketing Video Artist* e *AI Artist*. Sem pipeline de personagem. |
| **OFM Studios** | `/connect` 200 | Manager de futebol; sem elenco de personagem. |
| **House of How Games** (Boden, Suécia) | `/connect` 200 | **Veto escrito** já registrado: *"Cleared to work and located in Sweden"*. |
| **Black Kite Studios** (Londres) | `Freelance DMP / Concept Artists - Expression of Interest` `8330454` | Duas razões: a porta aberta é de **matte painting e concept 2D**, que não é a disciplina dele, e a casa está em **thread viva** com Angus Edhouse desde 30/08. |
| **Envar Studio** (Estocolmo) | `/connect` 200 | Candidatura de portal enviada e confirmada em 07/09 (`8281404`). |
| 96 dos 127 quadros `/connect` em 200 | — | Fora do setor. São slugs de palavra genérica que pertencem a empresa de outro ramo: `above`, `black` (Eventus), `butter` (All Gravy), `chief`, `chopchop`, `curio`, `dare`, `doktor` (Doktor.se), `eclipse`, `ember` (ONG neozelandesa), `fortis`, `fully`, `fuse`, `genius`, `groundcontrol`, `habitat` (HEALTH CITY), `here`, `hero`, `homa`, `infinity`, `kinetic`, `level` (companhia aérea), `life`, `lingokids`, `lunar`, `made`, `mill`, `mind`, `monster`, `neat`, `next` (Novati), `once` (ONCE, Espanha), `osome`, `parkerschauffeurs`, `power`, `revolution`, `salt`, `seven` (Baar), `squeeze`, `starship`, `stim`, `sunday`, `sweet` (Smart), `sweetspot`, `tribes`, `unfold`, `waypoint`, `zero` (Eleven) e afins. **O aviso do `quadros-tt-rec-1545-1009.csv` sobre slug de palavra genérica se confirmou por inteiro.** |

### 8.3 Caiu na REDE, e não é porta morta

| Slug | Medido | Leitura |
|---|---|---|
| `liquidswords` | `000`, 0 bytes, redirecionando para `careers.liquidswords.com` | Domínio próprio não resolve por este proxy, três tentativas. **Mesma família do `careers.ilpvfx.com`.** Está na fila em 1º lugar, com confirmação no navegador exigida. |
| `impact` | `000`, 0 bytes, `careers.impactmr.com` | Fora do setor de qualquer modo (pesquisa de mercado). |
| `house`, `mobile`, `rhino`, `united` | **403**, 5.709 a 5.711 bytes, título **`Just a moment...`**, com **`challenges.cloudflare`** literal no HTML | Os quatro redirecionam para `*.tuolavoro.com`, agência de trabalho italiana. É **parede de Cloudflare**, e são fora do setor. |
| 19 slugs em **404 limpo** | `envar`, `foolstheory`, `fundagames`, `gamecan`, `ghostshipgames`, `goodbyekansasstudios`, `keengames`, `invisiblewalls`, `minogames`, `paradox`, `paradoxinteractive`, `paradoxplaza`, `radicalforge`, `slug`, `stunlockstudios`, `snowprint`, `sybogames`, `tt`, `unleash` | São **grafias erradas ou antigas** do mesmo inquilino. A grafia viva está na lista dos 127: `envarstudio`, `stunlocksstudios` (dois `s`), `snowprintstudios`, `sybo`, `goodbyekansas`. **Isso reforça a lição já escrita em 09/09 sobre o `s` do Stunlock: slug errado devolve 404 e parece casa sem porta.** |

---

## 9. MÉTODO, PARA A PRÓXIMA RODADA NÃO REFAZER

1. **A lista de 152 slugs Teamtailor saiu de `grep -rhoE '[a-z0-9._-]+\.teamtailor\.com'` no
   repositório inteiro**, não de um CSV só. O `censo-boards-0809.csv` tem 175 linhas de
   Teamtailor mas só **32 tokens distintos**; o `quadros-tt-rec-1545-1009.csv` traz 95; o resto
   estava solto em `enviados.csv`, `processados.csv`, `docs/index.html` e nos relatórios.
   **Contar linha de CSV em vez de token distinto foi o que fez a rodada de 10/09 testar 62.**
2. **O Teamtailor tem DUAS rotas espontâneas, não uma.** O `/connect` é banco de talentos; o
   anúncio `Open Application` / `Unsolicited Application` / `General Application` /
   `Expression of interest` / `Spontanansökan` / `Initiativbewerbung` é **requisição com id
   próprio** e entra no funil como candidatura. Ler o `jobs.json` procurando esses títulos é
   barato e achou 41 anúncios em 24 inquilinos. **A segunda rota vale mais que a primeira**,
   porque id de requisição é dedupável e cadastro de banco não é.
3. **Sinal de existência do `/connect`:** 404 limpo (1.076 bytes) quando o slug não existe;
   200 quando aberto no subdomínio; 200 depois de 301 quando servido em domínio próprio.
   **Não vi nenhum 404 de "Connect desligado" entre os 127** — o padrão de "quadro vivo, banco
   desligado" que o Pinpoint tem com 302 não apareceu aqui.
4. **A busca de captcha foi por `recaptcha|hcaptcha|turnstile|datadome|challenges.cloudflare|friendlycaptcha`
   no corpo servido.** Deu **zero em 100% das rotas Teamtailor** e **`hcaptcha` em 100% das
   rotas Recruitee abertas**. A assimetria é tão limpa que serve de teste de família: se um dia
   um Teamtailor acusar `hcaptcha`, desconfie da conta, não da plataforma.
5. **Não repetir:** varredura de slug Homerun (3.521 em 09/09, 3 quadros), varredura de slug
   Pinpoint (14.387 em 10/09, 79 quadros), e envio por Recruitee (parede de hCaptcha medida
   agora em cinco páginas de cinco inquilinos diferentes).
6. **Fazer a seguir:** as **39 portas Teamtailor Connect já abertas e não usadas** que
   `bancos-de-talentos-1009.md` §5 listou continuam valendo e **não se sobrepõem** a esta fila;
   e vale reler os 152 feeds `jobs.json` daqui a alguns dias, porque o quadro é o mesmo mas o
   anúncio espontâneo aparece e some.

---

## 10. QUEBRA POR DISCIPLINA, como a regra de 10/09 exige

Das 15 rotas da fila: **9 são de casa com produção de personagem 3D declarada** (Liquid Swords,
Facepunch, Neon Giant, The Gang, MindArk, Last Arrow, Pixion, PFX, Madbox), **4 são de casa de
jogo sem elenco de personagem evidente** (Lightheart, GOALS, Vivid, eRepublik) e **2 estão com
um dado faltando** (Opus Major sem país confirmado, Liquid Swords sem rota acessível por esta
rede). **Nenhuma é de ambiente**, porque banco de talentos não tem disciplina de vaga: a
disciplina se declara no campo de departamento e função na hora do cadastro, e ali a instrução
é a de sempre — **personagem, e não guarda-chuva de arte**, como a Sloclap provou em 07/09
quando o perfil entrou catalogado em `CHARACTER ARTIST`, id 476539.
