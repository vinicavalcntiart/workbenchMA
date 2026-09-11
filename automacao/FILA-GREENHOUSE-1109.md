# FILA GREENHOUSE — re-triagem das rotas espontâneas sob a regra nova, 11/09/2026 (noite)

Tudo por `curl` e pela API pública do Greenhouse. **Nenhum navegador foi aberto, nada foi
enviado, nenhum formulário foi preenchido, nenhum email foi mandado.** A entrega é a fila.

Não toquei em `enviados.csv`, em `automacao/FILA-DO-VINI.md` nem em `docs/index.html`. Criei
este arquivo e acrescentei **uma** linha em `automacao/processados.csv`.

Lido antes de começar, por inteiro: `BRIEFING.md` (inclusive as seções novas do fim, que são
as que mudam a triagem), `automacao/BRIEF-JHON.md` e
`automacao/caca-join-greenhouse-1109.md`, que é a rodada que esta aqui re-tria.

---

## 0. A PREMISSA QUE MUDOU, E O QUE ELA CUSTOU DE VERDADE

A caça de hoje tratou `"disable_captcha":false` como **parede** e mandou as cinco rotas da
fila para a mão do Vini. **A premissa morreu no mesmo dia, medida três vezes:** Jam Filled
`7685474003`, Absurd Ventures `4141408007` e Tactile Games `4319957101` foram enviadas e
confirmadas com `/confirmation` na URL, as três por quadros que medem
`"disable_captcha":false`. O reCAPTCHA Enterprise do Greenhouse é **pontuação**, e quando a
pontuação reprova ele **manda um código de oito caracteres por email e aceita o envio com
ele** (regra 19 do briefing; fluxo `needcode_<slug>.txt` → Gmail → `code_<slug>.txt`).

**Confirmei por `curl` que as cinco casas desta fila estão no mesmo regime das três enviadas:**

| Inquilino | `disable_captcha` | Leitura |
|---|---|---|
| `wbpa` | `false` | mesmo regime da Jam Filled, que passou hoje |
| `absurdventures` | `false` | **já passou hoje**, na porta irmã `4141408007` |
| `atomiccartoons` | `false` | mesmo regime |
| `sphereentertainment` | `false` | mesmo regime |
| `jamfilled` / `tactilegames` (controle) | `false` | **as duas enviadas e confirmadas hoje** |

**A conclusão honesta, e ela é desconfortável para os dois lados.** A premissa morta **não
estava segurando fila**: das 93 rotas espontâneas desta varredura, **nenhuma** caiu por
captcha — as peneiras que cortaram foram indústria, disciplina e dedupe. O que a premissa
morta custou foi **quem clica**: cinco rotas foram empurradas para a mão do Vini quando a
automação podia ter enviado as três que enviou depois. **Quadro do Greenhouse não é parede, é
fila da automação.**

---

## 1. PLACAR — os números medidos, antes de qualquer narrativa

| Medida | Número |
|---|---|
| Slugs sondados contra `boards-api.greenhouse.io/v1/boards/<slug>/jobs` | **62.891** |
| Quadros vivos (HTTP 200) | **375** |
| Quadros vivos porém **vazios** (zero anúncio) | **83** |
| Anúncios lidos | **10.599** |
| **Rotas espontâneas achadas** | **93**, em **63 quadros** |
| — achadas por padrão de título | 86 |
| — achadas **à mão**, porque o título não denuncia | 7 |
| Falsos positivos de título descartados (General Manager, General Counsel, General Nurse…) | 28 |

### 1.1 As quatro peneiras, com o número de cada uma

| Peneira | Rotas | O que é |
|---|---|---|
| **Fora da indústria** | **56** | Nem jogos, nem animação, nem VFX: saúde, encanamento, consultoria, imobiliária, seguro, porta de garagem |
| **Fora da disciplina** (é indústria, mas o corpo do anúncio não leva a personagem) | **19** | Localização e LQA, TCG 2D, engenharia de backend, produção, agência de publicidade, balcão por cargo de diretoria |
| **Fora de escopo geográfico** | **0** | Medido e é zero: nenhuma rota espontânea de indústria caiu só por país. As casas fora de escopo (Nex em Hong Kong, Tango Gameworks em Tóquio) **não publicam rota espontânea nenhuma** |
| **Dedupe** | **13** | 11 por ID já enviado, **2 por NOME com ID inédito** |
| **NA FILA** | **5** | §3 |

93 = 56 + 19 + 0 + 13 + 5.

**Quebra por disciplina, que é a regra de 10/09:** das 5 da fila, **1 é de PERSONAGEM com a
palavra escrita no próprio formulário** (a Warner Bros. Pictures Animation tem a opção
literal `Modeling/Sculpt` e a `Texture/Look Dev`), **3 são porta espontânea de casa de
animação e jogo** onde o encaminhamento é para personagem, e **1 é porta de entrada da regra
13 sem encaixe de personagem** e está marcada como tal. **Zero de ambiente.**

### 1.2 O FURO DO MÉTODO ANTERIOR: consertado, e ele rendeu o melhor achado da rodada

A rodada de hoje escreveu que o slug `2k` ficou fora do universo por um filtro de comprimento
mínimo de três caracteres. **Tirei o filtro.** O universo passou a aceitar slug de uma e duas
letras e o resultado se mede:

- **`2k` sondado: quadro vivo, 120 anúncios.** Rota espontânea: **nenhuma**. As três de
  personagem (`7888174003`, `7888173003` e `7835808003`) **já foram enviadas em 02/09 e
  recusadas em 03 e 09/09**. **O furo era real e o prejuízo dele, nesta lane, é zero.**
- **Outros 131 slugs curtos (até quatro caracteres) responderam 200**, e **26 deles têm uma
  ou duas letras** (`2`, `2k`, `3`, `ag`, `bw`, `cc`, `ce`, `ec`, `ee`, `ex`, `hs`, `ie`,
  `ii`, `jb`, `lv`, `ma`, `mm`, `na`, `pm`, `pt`, `sa`, `sc`, `si`, `sj`, `st`, `us`, `ww` —
  e `mm` é a **Media Molecule**). Entre os de três e quatro letras: `5ca`,
  `akqa`, `icon`, `keen`, `koch`, `flix`, `fox`, `vgw`, `warp`, `onyx`, `seed`, `spin`,
  `kano`, `hiro`, `moon`, `zoo`, `map`, `nix`, `hook`. Sem eles a varredura anterior perdeu
  quadro de verdade.
- **E foi por aí que entrou o achado da rodada:** o slug **`wbpa`**, quatro letras, é a
  **Warner Bros. Pictures Animation**. Ele não estava no universo anterior e **é a primeira
  porta alcançável que esta campanha acha na Warner**, uma das quatro casas da regra 14.

---

## 2. COMO A RE-TRIAGEM FOI FEITA

1. **Universo reconstruído do zero**, sem filtro de comprimento: 10.266 nomes de estúdio dos
   CSVs da campanha e 6.532 domínios de segundo nível colhidos de todo `.csv`, `.md`,
   `.html`, `.txt`, `.json` e `.js` do repositório, mais os `token` dos dois censos, mais os
   slugs do Greenhouse citados em URL no repositório, mais variantes (sem espaço, com hífen,
   sem sufixo de razão social, primeira palavra, duas primeiras, iniciais, e sufixadas com
   `games`/`studios`). **62.891 slugs.**
2. **Sondagem**: `boards-api.greenhouse.io/v1/boards/<slug>/jobs`, 200 é quadro vivo.
3. **Leitura do quadro inteiro** de cada um dos 375 vivos, com `internal_job_id`, que é o
   identificador que a regra 18 do briefing manda guardar.
4. **Detecção de rota espontânea por título** com padrão largo, e **depois uma segunda
   passagem à mão** sobre todo título que contivesse `interest`, `pool`, `community`,
   `submit`, `join`, `resume`, `portfolio`, `opportunit`, `candidat`, `expo`, `register`.
   **Foi a segunda passagem que achou a porta da Warner**, cujo título é
   *"WBPA @ the 2026 LightBox Expo – Let us know you're attending!"* e não tem uma palavra
   dos padrões normais.
5. **Anúncio inteiro baixado** por `boards-api.greenhouse.io/v1/boards/<slug>/jobs/<id>?questions=true`,
   HTML desescapado, tags removidas, e a **régua de veto passada no texto integral**, com cada
   acerto classificado à mão, frase inteira escrita.
6. **Campos lidos da fonte**, nunca presumidos: `label`, `required`, `fields[].name`,
   `fields[].type` e todas as opções das listas. **Consentimento de GDPR lido em
   `data_compliance`**, que é onde ele mora e é o que barrou a primeira tentativa da Tactile
   hoje.
7. **Dedupe com os DOIS argumentos** (`sh automacao/dedupe-agora.sh "<ID>" "<Casa>"`) **mais
   grep pelo NOME** em `enviados.csv`, `automacao/processados.csv`, `docs/index.html` e
   `alvos.csv`, porque a lição de hoje é que ID limpo é metade do dedupe.

---

## 3. FILA FINAL NUMERADA — 5 rotas

Ordem: **encaixe de personagem primeiro**, depois porte da casa, depois confiabilidade.

> **Todas são candidatura da AUTOMAÇÃO, não fila da mão dele.** As cinco medem
> `"disable_captcha":false`, que é exatamente o regime das três que passaram hoje. O código de
> oito caracteres por email é etapa esperada, não recusa: rodar em segundo plano, esperar
> `needcode_<tag>.txt`, ler o código **mais recente pelo horário** no Gmail e escrever
> `code_<tag>.txt` com a sessão viva, dentro de seis minutos.

---

### 1. Warner Bros. Pictures Animation — banco de talentos do LightBox Expo 2026 — **O ACHADO DA RODADA**

- **Por que a casa presta, com a frase do próprio anúncio:** é a **Warner**, uma das quatro
  casas da regra 14, e o anúncio se descreve assim: *"Drawing on a century of studio legacy
  and encompassing achievements in 2D, CG and photoreal animation, Warner Bros. Pictures
  Animation is the revitalized feature animation arm of WB… This next chapter begins with the
  release of the major motion picture, The Cat in the Hat, coming to theaters worldwide on
  November 6, 2026."* É braço de **longa-metragem de animação em CG** montando equipe. E o que
  decide: **o formulário nomeia a disciplina dele duas vezes**, no seletor obrigatório de
  área de interesse — as opções são `Story/Storyboard`, `Visual Development/Design`,
  **`Modeling/Sculpt`**, **`Texture/Look Dev`**, `Pre-Visualization / Rough Layout`,
  `Rigging`, `Animation`, `Edit & Post Production`, `Lighting/Effects`,
  `Production Management`, `Technical Direction / Technology`. Área primária
  **`Modeling/Sculpt`**, secundária **`Texture/Look Dev`**.
- **O que a casa diz que a porta é:** *"If you're attending the Expo and excited about the
  idea of joining our creative community, we'd love to keep you in mind for future
  opportunities. Simply share your PDF resume and information, and we'll add you to our talent
  pool for upcoming projects."*
- **URL exata:** `https://job-boards.greenhouse.io/wbpa/jobs/5371895008`
- **ID da requisição:** `5371895008` · **`internal_job_id`: `null`** (o Greenhouse não expõe
  um para esta; o id do anúncio é o que existe, e fica registrado como tal)
- **Local:** `Pasadena, California, United States` · **Publicada em 08/09/2026 e atualizada no
  mesmo carimbo**, ou seja, **tem três dias de idade**. Vaga de casa grande vive de 3 a 7
  dias, então esta é a que tem relógio.
- **Medido:** HTTP **200**, 53.777 bytes. `"disable_captcha":false`.
- **Escopo:** Estados Unidos. Dentro. **Disciplina:** modelagem e escultura de personagem,
  nomeadas pela própria casa. Dentro, e é o melhor encaixe da fila inteira.
- **RÉGUA DE VETO APLICADA AO ANÚNCIO INTEIRO (1.740 caracteres, baixado, não a listagem):**
  **ZERO acerto** de `authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`,
  `days a week`, `citizen`, `resident`, `visa`, `relocat`, `onsite`, `hybrid`, `legally`.
  **Nenhum veto escrito, e o formulário NÃO TEM pergunta de autorização de trabalho nenhuma** —
  é o único da fila assim.
- **RESSALVA QUE PRECISA SER LIDA ANTES DE CLICAR, e ela é de honestidade:** o título diz
  *"Let us know you're attending!"* e o corpo abre com *"If you're attending the Expo"*. **Ele
  não vai ao LightBox Expo.** Não existe campo perguntando se vai, então nada é afirmado de
  falso ao enviar — mas o enquadramento da casa é de quem vai estar no estande #1118. A casa
  também escreve, com todas as letras: *"Submitting your information isn't an application for
  any current or future roles. It just helps us get to know amazing artists and storytellers
  who may be a great fit down the road."* **É banco de talentos, não vaga aberta.** Quem
  decide se manda é o Vini; a informação está aqui inteira.
- **Campos do formulário, lidos em `?questions=true`:**
  `first_name` (obrigatório), `last_name` (obrigatório), `preferred_name`, `email`
  (obrigatório), **`phone` (OBRIGATÓRIO** — nome do campo; o valor vive só no doc privado do
  Drive *CAMPANHA - dados pessoais dos formularios*), `resume` **arquivo, obrigatório** (a
  casa pede PDF por escrito), `resume_text` (textarea espelho, obrigatório),
  **`question_18092559008` *What is your Primary Area of Interest?* (lista obrigatória de 11,
  com `Modeling/Sculpt`)**, `question_18092560008` *Secondary Area of Interest* (mesma lista,
  opcional), `question_18092218008` *Portfolio Link*, `question_18092219008` *Additional
  Portfolio Materials* (textarea), **`question_18092220008` *Username and/or Password*
  (texto, OBRIGATÓRIO** — é a senha do portfólio, e como o dele é público a resposta honesta é
  dizer que não há senha), `question_18092216008` *LinkedIn Profile*, `question_18092221008`
  *IMDb*, e `question_18092215008` *If your 'school name' was not listed above, please add it
  here*.
  **O bloco de formação é `education_optional`**: o Greenhouse desenha escola, curso e datas
  e nada ali é obrigatório.
  **NÃO TEM campo de cover letter.** Então a carta não se anexa aqui: o que existe é o
  textarea de *Additional Portfolio Materials*, e é ali que entram a linha de personagem e a
  de realocação.
  **Consentimento de GDPR: NÃO.** `requires_consent`, `requires_processing_consent` e
  `requires_retention_consent` os três `false`.
- **Dedupe rodado:** `sh automacao/dedupe-agora.sh "5371895008" "Warner Bros. Pictures Animation"`
  → **seção 1: nenhuma ocorrência do ID nos quatro arquivos. Seção 2: nenhuma marca de envio.
  Seção 3: nada.** Por NOME: `Warner Bros. Pictures Animation` = **0** em `enviados.csv`,
  **0** em `alvos.csv`, **3** em `processados.csv` e **3** em `docs/index.html`, e **as seis
  ocorrências são todas sobre Charles Ellison**, que saiu da lista de alvo em 05/09 por ter
  sido professor do Vini. `wbpa` = **0** no repositório inteiro.
  **Leitura:** a casa **nunca recebeu candidatura**, e a única via registrada dela estava
  vetada. **Esta é a primeira porta alcançável da Warner nesta campanha.**
- **Comando exato de disparo**, no formato usado hoje:

```sh
cd /home/user/apply
# 1) o texto da resposta (nao ha carta anexada nesta: nao existe campo de cover letter)
#    ans_wbpa.json com: area primaria Modeling/Sculpt, secundaria Texture/Look Dev,
#    portfolio, senha do portfolio ("No password, the portfolio is public."), LinkedIn.
# 2) roda EM SEGUNDO PLANO e fica de olho no needcode
VINI_TEL='<telefone: doc privado do Drive, CAMPANHA - dados pessoais dos formularios>' \
  sh hb_run.sh gh_jamfilled.js \
  "https://job-boards.greenhouse.io/wbpa/jobs/5371895008" wbpa ans_wbpa.json --submit
# 3) quando aparecer /home/user/apply/needcode_wbpa.txt: ler no Gmail o codigo MAIS RECENTE
#    do assunto "Security code for your application to Warner Bros. Pictures Animation"
#    e escrever /home/user/apply/code_wbpa.txt em ate SEIS minutos, com a sessao viva.
```

Modelo do `ans_wbpa.json` (nome de campo e conteúdo, nunca valor pessoal):

```json
{"city":"Olinda, Pernambuco, Brazil","questions":[
 {"id":"question_18092559008","label":"area primaria","type":"select","prefs":["^Modeling/Sculpt$"]},
 {"id":"question_18092560008","label":"area secundaria","type":"select","prefs":["^Texture/Look Dev$"]},
 {"id":"question_18092218008","label":"portfolio","type":"text","text":"https://www.artstation.com/viniciuscavalcanti"},
 {"id":"question_18092220008","label":"senha do portfolio","type":"text","text":"No password, the portfolio is public."},
 {"id":"question_18092216008","label":"LinkedIn","type":"text","text":"https://www.linkedin.com/in/vinicavalcnti/"},
 {"id":"question_18092219008","label":"materiais adicionais","type":"text","text":"<duas linhas: a area dele e personagem 3D estilizado, credito Wingfeather Saga; e a linha de realocacao>"}
]}
```

> **Atenção de preenchimento, medida hoje:** a lista de área de interesse é `react-select`, e
> a regra de 10/09 vale aqui — **apertar `Escape` depois de escolher DESFAZ a escolha**. E o
> alvo tem que ser **ancorado** (`^Modeling/Sculpt$`), nunca regex de OU, porque
> `/model|sculpt/i` casaria com `Visual Development/Design` em outra casa e a lição da Plastic
> Wax é exatamente essa.

---

### 2. Absurd Ventures — `General Animated Series Application` — a divisão onde o crédito dele é mais forte

- **Por que a casa presta:** estúdio de **Dan Houser**, co-criador de *Grand Theft Auto*, em
  Santa Monica e San Rafael, com **duas divisões**, jogos e **série animada**. O quadro vivo
  prova produção de verdade: `Lead Open World Designer`, `Mission Design Lead (Campaign)`,
  `Principal Gameplay Animator`, `Cinematic Technical Designer`, `Software Engineer, Cinematic
  Tools`. **O crédito de Wingfeather Saga é de série animada, e esta é a porta da divisão de
  série animada.**
- **Por que esta entra mesmo com a casa já batida hoje:** ela foi deixada de fora **de
  propósito** na rodada das 19h, e o motivo está escrito no `enviados.csv`: *"e requisicao
  diferente e divisao diferente, mas duas candidaturas na mesma casa na mesma hora leem como
  disparo automatico, nao como interesse."* **A hora já passou.** É requisição diferente, com
  `internal_job_id` diferente, e o texto de cada balcão diz explicitamente que é para
  *"our &lt;divisão&gt; teams"*.
- **URL exata:** `https://job-boards.greenhouse.io/absurdventures/jobs/4141404007`
- **ID da requisição:** `4141404007` · **`internal_job_id`: `4098713007`**
- **Local:** `Santa Monica OR San Rafael`. Publicada em 09/11/2023, atualizada em 22/05/2025.
- **Medido:** HTTP **200**, 44.077 bytes. `"disable_captcha":false`.
- **Escopo:** Estados Unidos. Dentro. **Disciplina:** balcão geral de divisão de animação;
  o encaminhamento é declarado pela própria casa.
- **Texto integral do anúncio** (193 caracteres, cabe inteiro): *"We will be staffing more
  roles for our Animated Series teams in the future. If you would like to submit a general
  application purely for us to have your resume on file, feel free to do so here."*
- **RÉGUA DE VETO NO TEXTO INTEGRAL: ZERO acerto** de `authoriz`, `eligib`, `sponsor`,
  `work permit`, `must be based`, `LMIA`, `days a week`, `citizen`, `resident`, `visa`,
  `relocat`, `onsite`, `hybrid`, `legally`. **Nenhum veto escrito.**
- **Campos do formulário, lidos da fonte:** `first_name` (obr.), `last_name` (obr.), `email`
  (obr.), `phone` (opcional), `resume` **arquivo, obrigatório**, `resume_text` (textarea,
  obr.), **`cover_letter` arquivo OPCIONAL** (é a diferença para a #3),
  `question_4835734007` *Website or portfolio link*, `question_4835735007` *Work samples*
  (**arquivo**), `question_4835736007` *LinkedIn Profile*,
  **`question_4835737007` *Are you lawfully authorized to work in the United States?*
  (lista Yes/No, OBRIGATÓRIA)**, **`question_4835738007` *Are you able to work in our Santa
  Monica, CA or San Rafael, CA office?* (lista Yes/No, OBRIGATÓRIA)**.
  **Sem pergunta de pretensão salarial. Sem consentimento de GDPR** (os três `false`).
- **Como responder, e é igual ao que passou hoje na porta irmã:** autorização nos EUA = **No**,
  que é a verdade e custa (regra 8); disponibilidade para o escritório = **Yes**, porque a
  pergunta é de disponibilidade e não de autorização, e a carta diz com todas as letras que
  ele precisaria de patrocínio e que está pronto para mudar.
- **Dedupe rodado:** `sh automacao/dedupe-agora.sh "4141404007" "Absurd Ventures"` →
  **seção 1: 1 ocorrência em `enviados.csv` e 2 em `processados.csv`, e as três são a anotação
  de hoje dizendo que esta NÃO foi enviada de propósito. Seção 2: a única "marca" que aparece
  é a frase `NAO foi enviada de proposito`, ou seja, o contrário de envio. Seção 3: nenhuma
  parede, nenhuma recusa.** Por NOME: `Absurd` em `enviados.csv` = a candidatura de hoje na
  `4141408007`, **requisição e divisão diferentes**.
- **Comando exato de disparo:**

```sh
cd /home/user/apply
CARTA_TXT=/home/user/apply/carta_absurd_animated.txt \
CARTA_PDF=/home/user/apply/carta_absurd_animated.pdf sh hb_run.sh carta_pdf.js
VINI_TEL='<telefone: doc privado do Drive>' CARTA_PDF=/home/user/apply/carta_absurd_animated.pdf \
  sh hb_run.sh gh_jamfilled.js \
  "https://job-boards.greenhouse.io/absurdventures/jobs/4141404007" absurdanim ans_absurdanim.json --submit
# needcode_absurdanim.txt -> Gmail ("Security code for your application to Absurd Ventures")
# -> code_absurdanim.txt em ate 6 minutos
```

---

### 3. Absurd Ventures — `General Film & TV Application` — mesma casa, terceira divisão

- **Por que existe separada:** a Absurd publica **sete** balcões, um por divisão, cada um com
  `internal_job_id` próprio, e o currículo cai em fila diferente. Film & TV é a divisão de
  longa e série live-action/animada da casa.
- **URL exata:** `https://job-boards.greenhouse.io/absurdventures/jobs/4141225007`
- **ID da requisição:** `4141225007` · **`internal_job_id`: `4098715007`**
- **Local:** `Santa Monica OR San Rafael`. Publicada em 09/11/2023, atualizada em 22/05/2025.
- **Medido:** HTTP **200**, 44.100 bytes. `"disable_captcha":false`.
- **Texto integral:** *"We will be staffing more roles for our Film & TV teams in the future.
  If you would like to submit a general application purely for us to have your resume on file,
  feel free to do so here."*
- **RÉGUA DE VETO NO TEXTO INTEGRAL: ZERO acerto** dos mesmos quatorze termos.
- **Campos, e aqui está a diferença que importa:** iguais aos da #2, **menos uma**:
  **`cover_letter` é arquivo OBRIGATÓRIO** (e `cover_letter_text` também), igual à
  `4141408007` que passou hoje. Os ids das perguntas são outros: `question_4833643007`
  *Website or portfolio link*, `question_4833644007` *Work samples* (arquivo),
  `question_4833645007` *LinkedIn Profile*, **`question_4833646007` *Are you lawfully
  authorized to work in the United States?* (Yes/No, obrigatória)**, **`question_4833647007`
  *Are you able to work in our Santa Monica, CA or San Rafael, CA office?* (Yes/No,
  obrigatória)**. **Sem GDPR. Sem pretensão salarial.**
- **Dedupe rodado:** `sh automacao/dedupe-agora.sh "4141225007" "Absurd Ventures"` →
  **seção 1: nenhuma ocorrência — o ID é inédito nos quatro arquivos. Seção 2: nenhuma marca
  de envio. Seção 3: nenhuma parede, nenhuma recusa.**
- **ORDEM RECOMENDADA, e ela é a mesma lição de hoje:** **#2 primeiro, #3 num outro dia.**
  Três candidaturas na mesma casa em 24 horas leem como disparo automático. Se for para cortar
  a fila, a que sai é esta, não a #2.
- **Comando exato de disparo:**

```sh
cd /home/user/apply
CARTA_TXT=/home/user/apply/carta_absurd_filmtv.txt \
CARTA_PDF=/home/user/apply/carta_absurd_filmtv.pdf sh hb_run.sh carta_pdf.js
VINI_TEL='<telefone: doc privado do Drive>' CARTA_PDF=/home/user/apply/carta_absurd_filmtv.pdf \
  sh hb_run.sh gh_jamfilled.js \
  "https://job-boards.greenhouse.io/absurdventures/jobs/4141225007" absurdfilm ans_absurdfilm.json --submit
```

---

### 4. Atomic Cartoons — `Expression Of Interest - LA` — entra com as duas ressalvas já registradas

- **Por que a casa presta:** animação para TV e streaming, grupo Blue Ant, unidades em
  Vancouver e Los Angeles. O quadro vivo tem `CG Designer`, `Unreal CG Supervisor` e
  `Unreal Previs and Layout Supervisor`, ou seja, pipeline de CG de verdade.
- **O que a casa diz que a porta é:** *"Due to the fast paced nature of our industry our needs
  are always changing. Don't see the role you are looking for with our LA Team? Apply here and
  select the department you are interested in and we will keep you in mind for future
  opportunities with our LA Team!"*
- **URL exata:** `https://job-boards.greenhouse.io/atomiccartoons/jobs/7565513003`
- **ID da requisição:** `7565513003` · **`internal_job_id`: `5691253003`**
- **Local:** `Los Angeles`. Publicada em 02/01/2026, atualizada em 08/06/2026.
- **Medido:** HTTP **200**, 55.139 bytes. `"disable_captcha":false`.
- **RÉGUA DE VETO NO TEXTO INTEGRAL (1.625 caracteres): UM acerto, de `citizen`, e é falso
  positivo.** A frase inteira: *"Atomic Cartoons Inc. and Blue Ant Studios are an equal
  opportunity employer and employ personnel without regard to race, ancestry, place of origin,
  colour, ethnic origin, language, **citizenship**, creed, religion, gender, sexual
  orientation, age, marital status, physical and/or mental handicap or financial ability."*
  Isso é parágrafo de igualdade de oportunidades, que é o **contrário** de veto. **Zero acerto
  de `authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`, `days a week`,
  `resident`, `visa`, `relocat`, `onsite`, `hybrid`. Nenhum veto escrito.**
- **Campos do formulário, lidos da fonte:** `first_name` (obr.), `last_name` (obr.), `email`
  (obr.), `phone`, `resume` **arquivo, obrigatório**, `resume_text` (obr.), `cover_letter`
  arquivo (opcional), **`question_29030023003` *Please select the department or role you are
  most interested in.* (lista OBRIGATÓRIA de 14: `Storyboards`, `Design`, `Editorial`,
  `Directorial (Supervisor, Series, Episodic, Art)`, `Production (LP, AP, PM, PC, PA)`,
  `Finance/Accounting`, `Human Resources`, `Sales and Distribution`,
  `Business Affairs/Legal`, `IT`, `Pipeline`, `Development`, `Current Series`,
  `Scripted Content`)**, **`question_29030024003` *Are you legally entitled to work in US for
  any employer, without restriction on a permanent basis?* (Yes/No, OBRIGATÓRIA — é a caixa da
  regra 8, responde-se **No**)**, `question_29030025003` *Your Current Location* (obr.),
  `question_29030026003` *portfolio ou reel* (textarea), `question_29030027003` *senha do
  portfólio*, `question_29030028003` *LinkedIn*, `question_29030029003` *earliest start date*
  (obr.), `question_29030030003` *Are you a new graduate? (2026)* (lista obrigatória de 5, a
  resposta é `No`), `question_29030033003` *Have you previously worked at Atomic Cartoons?*
  (Yes/No, obr., resposta `No`), `question_29030034003` *se sim, qual produção*.
  **Sem pretensão salarial. Sem consentimento de GDPR** (os três `false`).
- **AS DUAS RESSALVAS, e as duas continuam de pé:**
  **(a) A lista de departamentos da porta de LA NÃO TEM bucket de CG nem de modelagem** — ao
  contrário da porta de Vancouver da mesma casa, que tem. Marcar aqui é entrar pela **porta de
  entrada da regra 13**, de propósito, e é obrigatório declarar **na primeira linha** do campo
  livre que a área dele é personagem 3D e pedir o encaminhamento. O departamento menos errado
  é `Design`, e ele **não** é a disciplina dele.
  **(b) A casa já recebeu candidatura**: a `Expression Of Interest - Vancouver`,
  `7565498003`, **enviada e confirmada em 06/09 às 18h11**, com confirmação de
  `no-reply@atomiccartoons.com`. Esta é requisição **diferente**, em **país diferente**, e o
  texto dela não repete o veto de província que o painel registra do lado de Vancouver. Pela
  régua ela fica; mas é a **segunda batida na mesma casa** e quem decide o desgaste é o Vini.
- **Dedupe rodado:** `sh automacao/dedupe-agora.sh "7565513003" "Atomic Cartoons"` →
  **seção 1: 1 ocorrência do ID, em `processados.csv`, e é a anotação de hoje descrevendo
  estas mesmas duas ressalvas. Seção 2: NENHUMA marca de envio. Seção 3: duas linhas, as duas
  citando o veto de província do lado de Vancouver** (uma delas na ficha da Hydraulx,
  comparando). Por NOME: nenhuma candidatura registrada na unidade de LA.
- **Comando exato de disparo:**

```sh
cd /home/user/apply
CARTA_TXT=/home/user/apply/carta_atomic_la.txt \
CARTA_PDF=/home/user/apply/carta_atomic_la.pdf sh hb_run.sh carta_pdf.js
VINI_TEL='<telefone: doc privado do Drive>' CARTA_PDF=/home/user/apply/carta_atomic_la.pdf \
  sh hb_run.sh gh_jamfilled.js \
  "https://job-boards.greenhouse.io/atomiccartoons/jobs/7565513003" atomicla ans_atomicla.json --submit
```

---

### 5. Sphere Entertainment — `Join our Network` — **a mais fraca da fila, e está escrito por quê**

- **Por que entra:** casa grande de entretenimento imersivo (o Sphere de Las Vegas, com
  segunda sede planejada em Abu Dhabi) e **Sphere Studios em Burbank**, que é o braço de
  conteúdo. O balcão é genérico e tem bucket de arte: o seletor obrigatório
  *Which area of the business are you most interested in?* traz **`Art, Design`** e
  **`Creative Development`** entre as 33 opções. O anúncio diz: *"Sphere Entertainment welcomes
  motivated professionals to join our talent network. Even if there is no current opening that
  matches your background, we encourage you to share your information and areas of interest
  with us."*
- **POR QUE ELA É A ÚLTIMA, e isto é o mais importante desta entrada:** **não há personagem
  nenhum nesta casa.** A única requisição de arte no quadro inteiro é `Lead Real-Time Artist`,
  e conteúdo de Sphere é espetáculo imersivo, ou seja, ambiente e tempo real — as duas coisas
  que a regra de 10/09 manda pôr por último e que o briefing lista como fora da disciplina.
  **Isto é porta de entrada da regra 13, não encaixe.** Se a fila for cortada, **esta é a
  primeira a sair.**
- **URL exata:** `https://job-boards.greenhouse.io/sphereentertainment/jobs/5013167007`
- **ID da requisição:** `5013167007` · **`internal_job_id`: `null`**
- **Local:** `Burbank, CA; Las Vegas, NV; New York City, NY`.
- **Medido:** HTTP **200**. `"disable_captcha":false`.
- **RÉGUA DE VETO NO TEXTO INTEGRAL (1.917 caracteres): UM acerto, de `citizen`, e é falso
  positivo.** A frase inteira: *"MSG is an Equal Opportunity Employer and provides equal
  employment opportunities to all employees and applicants for employment without regard to
  race, color, religion, gender, sexual orientation, gender identity or expression, sexual and
  reproductive health choices, national origin, **citizenship**, age, genetic information,
  disability, or veteran status."* Parágrafo de igualdade de oportunidades. **Zero acerto de
  `authoriz`, `eligib`, `work permit`, `must be based`, `LMIA`, `days a week`, `resident`,
  `relocat`, `onsite`, `hybrid`, `legally`.** A palavra `sponsorship` **não** aparece no corpo:
  ela aparece **numa pergunta do formulário**, que é contexto e não veto.
- **Campos do formulário, lidos da fonte:** `first_name` (obr.), `last_name` (obr.),
  `preferred_name`, `email` (obr.), **`phone` (OBRIGATÓRIO)**, `resume` **arquivo,
  obrigatório**, `resume_text` (obr.), `cover_letter` arquivo (opcional),
  **`question_11038617007` *Which area of the business are you most interested in?* (lista
  OBRIGATÓRIA de 33, com `Art, Design`)**, **`question_11038618007` *Which location are you
  interested in?* (lista OBRIGATÓRIA: New York; Burbank; Las Vegas — marcar **Burbank**, que é
  onde fica o Sphere Studios)**, **`question_11038641007` *Will you now, or in the future,
  require immigration sponsorship by the company in order to obtain or maintain U.S. work
  authorization (e.g., H-1B, O-1, TN) for this role?* (Yes/No, OBRIGATÓRIA — a verdade é
  **Yes**, regra 8)**, `question_11038642007` *Have you ever been previously employed with the
  organization?* (Yes/No, obr., resposta `No`).
  **Sem pretensão salarial. Sem consentimento de GDPR** (os três `false`).
- **Dedupe rodado:** `sh automacao/dedupe-agora.sh "5013167007" "Sphere Entertainment"` →
  **seção 1: nenhuma ocorrência do ID. Seção 2: nenhuma marca de envio. Seção 3: nada.** Por
  NOME, `Sphere` aparece uma vez em `processados.csv`, e é a anotação de hoje descartando os
  **balcões por cargo** (`EXPRESSION OF INTEREST - Art Director`, `- Creative Director`,
  `- Designer`). **O `Join our Network` é outra requisição e a rodada anterior não o viu.**
- **Comando exato de disparo:**

```sh
cd /home/user/apply
CARTA_TXT=/home/user/apply/carta_sphere.txt \
CARTA_PDF=/home/user/apply/carta_sphere.pdf sh hb_run.sh carta_pdf.js
VINI_TEL='<telefone: doc privado do Drive>' CARTA_PDF=/home/user/apply/carta_sphere.pdf \
  sh hb_run.sh gh_jamfilled.js \
  "https://job-boards.greenhouse.io/sphereentertainment/jobs/5013167007" sphere ans_sphere.json --submit
```

---

## 4. O QUE CAIU, E POR QUÊ — negativo medido, rota por rota

### 4.1 Caiu no DEDUPE por ID (11 rotas)

| Casa | Rota | ID | Quando saiu |
|---|---|---|---|
| **Jam Filled** | Expression of Interest | `7685474003` | **HOJE**, `/confirmation` + *"Thank you for applying!"* |
| **Absurd Ventures** | General Game Development Application | `4141408007` | **HOJE**, `/confirmation` |
| **Tactile Games** | Open Applications | `4319957101` | **HOJE**, `/confirmation` |
| **Crystal Dynamics** | General Application, Remote/Flexible | `4352498005` | 07/09 |
| **Unknown Worlds** | General Application, Remote | `7535230002` | 07/09 |
| **NC America** | Open Applications, Irvine CA | `4052911009` | 07/09, com código por email |
| **PlayQ** | Don't See What You're Looking For? | `3055199` | 07/09, com código por email |
| **Tripwire Interactive** | General Application, Remote USA | `8282003002` | 07/09 — **e já RECUSADA em 07/09** |
| **Atomic Cartoons (Vancouver)** | Expression Of Interest | `7565498003` | 06/09 |
| **KSWH / Keen Software House** | Spontaneous applications, Praga | `4880719101` | 10/09 |
| **Sony Pictures Imageworks** | Expression of Interest | `4551278003` | casa com histórico extenso; regra 18 |

### 4.2 Caiu no dedupe **POR NOME**, com o ID inédito (2 rotas) — a lição que já tem três dias seguidos

- **Brand New School** — `General Interest - Apply Now`, `5818240004`, Londres / LA / Nova
  York. O ID é **inédito** nos quatro arquivos. O grep por **nome** devolve, no
  `docs/index.html`: *"CANDIDATURA ENVIADA e CONFIRMADA em 06/09 pela força-tarefa… Porta
  Greenhouse, com código de segurança por email"*, e a célula guarda
  `https://boards.greenhouse.io/brandnewschool`, **a URL do quadro, sem ID**. *(Além disso é
  casa de design de marca e motion, não de personagem.)*
- **Firaxis** — `Join Our Talent Community`, `6270031003`, Sparks Glencoe, Maryland. ID
  inédito. O grep por nome devolve, no `processados.csv`:
  `2026-09-07,Firaxis Games,…,ENVIADA,Join Our Talent Community confirmada por email as 06h40
  de no-reply@firaxis.com`, e a célula guarda **o domínio institucional**, não o id do ATS.

**Fica medido pelo terceiro dia seguido: ID limpo não é dedupe, é metade do dedupe.**

### 4.3 Caiu por DISCIPLINA — é indústria, mas o CORPO do anúncio não leva a personagem (19 rotas)

- **Absurd Ventures**, as outras quatro divisões: `General Comics/Graphic Novels Application`
  (`4141411007`) é 2D e narrativa gráfica; `General Audio Fiction Application` (`4141415007`)
  é áudio; `General Corporate Application` (`4141200007`) é administrativo; **`General
  Creative Services Application` (`4141394007`)** é o braço de marca e marketing da casa — e,
  somado a isso, três candidaturas na mesma casa em 24 horas leem como disparo automático.
- **2K Madrid** (`4418963003`, *2K Madrid General*). O texto é balcão legítimo
  (*"Didn't see a role that you're a fit for? Drop us your resume/CV here!"*) e o formulário é
  o mais simples que existe (nome, email, CV, carta e nada mais). **Cai porque o quadro
  inteiro da unidade são 12 anúncios e os 12 são localização e LQA** (`Localization Language
  Lead` em árabe, francês, alemão, italiano, polonês e russo, `Localization Specialist`,
  `LQA Analyst`, `Sr. Manager, LQA`). Não existe arte em Madrid para onde encaminhar um
  modelador, e a 2K já recusou as duas vagas de personagem dele em 03 e 09/09.
- **Fanatics Collectibles** (`4237884009`, *General Interest - Trading Card Games*, Seattle).
  Casa de jogo de cartas, e o anúncio lista as áreas: *"Game Design (Systems, Set, Play
  Design); Narrative design and worldbuilding; Art Direction, Illustration, or Visual
  Development; Production, Content, or Creative Operations; Business development; Partnerships
  management; Product Management; Live Operations, Balance, or Gameplay Analytics."*
  **Nenhuma é 3D**, e a qualificação exigida é *"Professional experience working on trading
  card games, collectible games, or similar products"*, que ele não tem. Some-se a presença
  escrita de `onsite`: *"All employees of Fanatics TCG are expected to be onsite in our
  Seattle office five days per week"* — que é regime, não veto. E a casa **já recebeu
  candidatura em 04/09** (Principal Visual Artist `4274428009`, confirmada por
  `no-reply@collectfanatics.com`), então seria a segunda batida.
- **Sony Pictures Imageworks** (`6060207003`, *Expression of Interest - Production*, Canadá).
  O seletor obrigatório de cargo tem **quatro opções e as quatro são de produção**:
  `Production Assistant`, `Production Coordinator`, `Senior Production Coordinator`,
  `Assistant Production Manager`. Não é a disciplina dele. *(Nota útil para outra rodada: a
  caixa de elegibilidade desta casa tem a opção `I will need a work permit`, ou seja, a casa
  prevê candidato que precisa de visto.)*
- **Sphere Entertainment**, os três balcões **por cargo**: `EXPRESSION OF INTEREST - Art
  Director` (`5197060007`), `- Creative Director` (`5197050007`) e `- Designer`
  (`5197043007`), todos em Burbank. Diretor de arte e diretor criativo não são o cargo da
  regra 2, e `Designer` ali é design gráfico.
- **Outfit7**, os três `Talent Pool`: **Growth Product Manager** (`7831280003`), **Senior
  Product Manager** (`7820146003`) e **Student Collaboration** (`7650639003`). Nenhum de arte.
- **Rushdown Studios** (`4093292009`, *General Interest - Other*). O quadro inteiro são quatro
  vagas e três são engenharia de backend (`Backend Engineer (Golang)`,
  `Senior Backend Engineer (C++)`, `Senior DevOps`). É co-dev de infraestrutura de
  multiplayer; o departamento do próprio anúncio é `Other`.
- **Whatwapp** (`4200882101`, Milão). O quadro tem três anúncios e os outros dois são
  `Head of UA` e `Product Manager`. Sem evidência de time de arte.
- **Hook** (`6440798002` *Join our Full-time Community* e `8649337002` *Join our Freelance
  Community*). **Rota nova, que a varredura anterior não viu**, e cai pelo corpo, que lista as
  disciplinas: *"If you're a Motion Designer, Art Director, Copywriter, Creative Director,
  Designer, Design Director, Producer or Engineer we want to meet you."* É agência de conteúdo
  publicitário; não há 3D de personagem.
- **Zero Studios** (`4648558005` *General Employment Inquiry* e `4648362005` *Contractor
  Interest Form*, NYC/LA/MKE/Remoto). O quadro é `Designer: Marketing & Social`. Agência de
  conteúdo social.

### 4.4 Caiu por ESCOPO GEOGRÁFICO: **zero**, e o número é honesto

Nenhuma rota espontânea de casa de jogos, animação ou VFX caiu por país nesta varredura. As
duas casas de indústria fora do escopo que a varredura achou **não publicam rota espontânea
nenhuma**:

- **Nex** (Hong Kong, 57 anúncios, entre eles `3D Game Artist` e `Senior Game Environment
  Artist`): Ásia só Coreia do Sul e Singapura. Fora, e **sem balcão espontâneo**.
- **Tango Gameworks** (Tóquio, 14 anúncios, entre eles `シニアキャラクターアーティスト`, Senior
  Character Artist): **Japão está fora** por regra fixa. Sem balcão espontâneo.
- `Open Application Japan` (`4655923004`) é da **Mirakl**, empresa de software, e cai por
  indústria antes de cair por país.

### 4.5 Caiu por estar FORA DA INDÚSTRIA (56 rotas)

Medidas e descartadas, com o setor entre parênteses: **ASI Hastings** (4 rotas, encanamento e
climatização), **capSpire** (6 rotas, uma por país — Austrália, Bulgária, Países Baixos,
Portugal, Espanha, Suíça — consultoria de energia), **Gusto** (4, folha de pagamento),
**IE** (7, consultoria em Melbourne), **Pulse Healthcare** e **Headspace** (saúde),
**Hazel Health**, **Precision for Medicine**, **WePractice** (`Initiativbewerbung
Psychotherapeut:in`), **Avanath** (imobiliária), **Lincoln Property**, **Kelso Building
Services**, **Garage Door Specialist**, **Red Mountain Garage Doors**, **BPD**, **Innovative
Signal Analysis**, **Lighthouse**, **Netlify**, **Oscar Health**, **Indigo**, **Mantis**
(distribuição de conteúdo), **Moon Creative Lab** (2, venture studio, e uma delas é em
Tóquio), **Praxis**, **Talent Pool**, **Slice**, **Democorp** (conta de demonstração),
**CLEVR** (Mendix), **Neo Cybernetica** (robótica), **Goodman** (data centers),
**MAP** (consultoria Salesforce, apesar do *Unsolicited Application* em Copenhague),
**SHADOW** (agência de relações públicas de Nova York, **não** a SHADOW de cloud gaming),
**N-iX** (2, `Drop a resume`, software), **Zoo** (fabricante de CAD), **Vox Media**,
**Sporty Group**, **GoodAI** (`Spontaneous applications`, Praga — laboratório de pesquisa em
IA, o quadro inteiro é `Senior Robotics Hardware Engineer` e a espontânea; sem pipeline de
arte 3D).

### 4.6 As vagas de PERSONAGEM que a varredura encontrou, e o que já era conhecido

Dos 10.599 anúncios, **52 batem na régua de disciplina** por título. **Nenhuma é vaga de
personagem inédita e aproveitável**, e não são espontâneas, então não entram nesta fila:

- **Já enviadas e/ou recusadas:** 2K `7888174003`/`7888173003`/`7835808003`, Cloud Chamber
  `7888170003`/`7888172003` (todas com `internal_job_id` `5834551003` ou `5809117003`, e todas
  já recusadas), **Riot `8163170` Principal 3D Character Artist** (enviada e confirmada em
  10/09 às 03h35), Wargaming `8161671` (recusada em 10/09), Mob Entertainment `5207518007`,
  Highdive `5097897007`, Sony Pictures Imageworks (o bloco inteiro de Vancouver), Bluehole,
  Loonshot, Hasbro `4318250009`, Swaybox `4337820009`/`4337866009`.
- **Fora por disciplina, apesar do título:** Insomniac `6143980004` *Senior Facial Character
  TD (CONTRACT)* — "Character TD" facial é **rigging**, e o briefing é explícito; Imageworks
  `4363707003`/`4363708003` *Character FX Artist* — **Character FX é simulação**; Epic
  `5763803004` *Character Animation Lead* — animação; PlayStation `6166111004` *Lead Character
  Tools Engineer*, Roblox `8016277` *Senior SWE - Non-Playable Character Behavior* e Hasbro
  `4250647009` *Full Stack Engineer – AI Character Platform* — engenharia.
- **Fora por escopo:** Tango Gameworks (Tóquio), as de Hong Kong da Hasbro.

**As de Seul e Pangyo (Bluehole, Loonshot) estão no escopo, mas são as mesmas requisições já
registradas.**

---

## 5. O QUE ESTA RODADA MEDIU E QUE MUDA O MÉTODO

1. **`disable_captcha` deixa de ser critério de fila.** Vira **dado operacional**: diz se o
   envio vai passar direto ou vai pedir o código de oito caracteres por email. Nas duas
   hipóteses a automação envia. O campo continua valendo a pena medir, só não decide mais
   nada.
2. **Filtro de comprimento mínimo de slug é furo, e o conserto pagou.** Cento e trinta e dois
   slugs de até quatro caracteres respondem 200, **26 deles com uma ou duas letras**, e um
   deles é a **Warner Bros. Pictures Animation**.
   **Regra: nenhuma varredura de token pode ter comprimento mínimo.**
3. **Detecção de rota espontânea por padrão de título é insuficiente, e dá para medir o
   quanto.** Sete das 93 rotas — 7,5% — só apareceram numa segunda passagem à mão, e entre
   elas está a melhor da rodada. **Título de balcão nem sempre tem a palavra "general" nem
   "talent": o da Warner é um convite para um evento.** A segunda passagem custa minutos e é
   onde mora o que ninguém achou ainda.
4. **Onde a rodada anterior errou de fato**, e vale escrever com nome: a fila dela não estava
   errada nas cinco entradas; estava incompleta, porque o universo de slug tinha buraco e o
   detector de título era estreito. **O placar de captcha dela estava certo e a conclusão
   operacional estava errada.**

---

## 6. O QUE EU NÃO CONSEGUI MEDIR, DITO SEM MAQUIAGEM

1. **O meu universo tem 62.891 slugs; o da rodada anterior tinha 83.223.** Ela achou 376
   quadros vivos e eu achei 375, mas **não são necessariamente os mesmos 375**. É provável que
   cada uma tenha quadro que a outra não sondou. O que posso afirmar é o que medi.
2. **Não medi `disable_captcha` nos 375 quadros**, só nos cinco da fila mais dois de controle.
   Depois da medição de hoje, o campo não decide fila, então gastar 375 requisições nele seria
   trabalho sem consequência. **Quem quiser o censo completo, ele não está aqui.**
3. **Não abri nenhuma página no navegador**, então não medi qual dos quadros carrega o widget
   com `size=invisible` e qual não carrega. O enunciado proibia navegador e eu não driblei.
4. **A porta da Warner é banco de talentos e está enquadrada para quem vai ao LightBox Expo.**
   Não consigo medir se a casa filtra por presença no evento. **Isso é risco declarado, não
   medição.**
5. **`boards-api.eu.greenhouse.io` continua recusado por este proxy** (`connect_rejected`), e
   continua não fazendo falta: o host americano serve os inquilinos europeus e o
   `absolute_url` de cada anúncio já aponta para `job-boards.eu.greenhouse.io` quando é o caso.

---

## 7. SONDAS DESTA RODADA, PARA COPIAR

```sh
# quadro inteiro, com internal_job_id (a chave do dedupe da regra 18)
curl -s "https://boards-api.greenhouse.io/v1/boards/<slug>/jobs"

# nome da casa por tras do slug (util quando o slug e uma sigla de tres letras)
curl -s "https://boards-api.greenhouse.io/v1/boards/<slug>" | jq -r .name

# CAMPOS do formulario + texto integral do anuncio, lidos da fonte
curl -s "https://boards-api.greenhouse.io/v1/boards/<slug>/jobs/<id>?questions=true"

# consentimento de GDPR: mora em data_compliance, e e ele que barra o envio na validacao
curl -s "https://boards-api.greenhouse.io/v1/boards/<slug>/jobs/<id>" | jq .data_compliance

# o porteiro por inquilino (hoje e dado operacional, nao criterio de fila)
curl -sL "https://job-boards.greenhouse.io/<slug>" | grep -o '"disable_captcha":[a-z]*'
```
