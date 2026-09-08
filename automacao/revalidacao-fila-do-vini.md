> # CORREÇÃO DO MAESTRO, 08/09 às 22h, feita ANTES de qualquer mudança na fila
>
> **A linha da nº 43 (TTK Games) deste relatório está INVERTIDA, e por pouco eu não troquei um
> link certo por um morto.** O relatório manda trocar `561860` por `558871`. Medi os dois **com o
> navegador**, que é o que o Vini vai usar, e o resultado é o contrário:
>
> | id | O que a página do estúdio renderiza | API que ela mesma chama |
> |---|---|---|
> | **`561860`** (o link que já está na fila) | **Character Artist**, Stockholm / Hybrid / Permanent, com a faixa **ainda publicada**: *"...SEK per month, rising to 47,000 with experience"* | `.../api/pinpoint/job/561860` → **200** |
> | `558871` (o que o relatório mandava usar) | **"Position not available"** | `.../api/pinpoint/job/558871` → **404** |
>
> O quadro do próprio site (`ttkgames.com/careers`) lista **14 vagas** e a Character Artist nele é
> a `561860`. **O link da fila estava certo e não foi trocado.**
>
> **Por que a divergência, e a lição vale para as próximas rodadas:** o relatório mediu no
> `ttkgames.pinpointhq.com/postings.json`, que é o quadro cru do ATS, e o site do estúdio consome
> **outra rota**, `ttk-strapi-....ondigitalocean.app/api/pinpoint/job/<id>`, com **outro espaço de
> identificadores**. As duas respondem 200 e as duas parecem oficiais. **Quem decide é a rota que o
> CANDIDATO usa**, porque é nela que ele clica em Apply. Quando duas fontes oficiais discordarem
> sobre um id, abra a página no navegador: ela é o desempate.
>
> **De quebra, o quadro do site revelou um alvo novo que o `postings.json` não fez aparecer:**
> **Lead Environment Artist** (`562172`), Stockholm / Hybrid / Permanent, com faixa publicada
> *"Starting from 60,000 SEK per month, rising to 85,000"* e **zero dos dezessete termos**. Entrou
> na fila como a nova nº 46.
>
> O resto deste relatório foi conferido por amostra e bateu: Netflix deslistada (paginei a busca do
> quadro e o id `790317384604` não está lá), Asobo com *"un niveau de français et anglais
> opérationnel"* na API do Lever, DreamWorks com `active: false` no SmartRecruiters, e Quantic
> Dream nº 27 e nº 41 com o mesmo uuid. A nº 44 da Behaviour foi resolvida pelo Gmail: recibo do
> Lever em 30/08, **já enviada**.

# REVALIDAÇÃO DA FILA DO VINI — 46 entradas, medidas uma a uma na fonte oficial

**Rodada de 08/09/2026, noite.** Tudo abaixo foi medido por mim com `curl`, nesta sessão.
Sem navegador. Nada foi enviado, nada foi commitado, nenhum formulário foi preenchido.
`FILA-DO-VINI.md` e `docs/index.html` não foram tocados.

---

## OS NÚMEROS

| | |
|---|---|
| Entradas na fila | **46** |
| Revalidadas (link + estado + régua dos 17) | **46** |
| **SEGUE NA FILA** | **35** |
| **SAI DA FILA** | **5** |
| **MUDOU** (segue, mas com fato novo que muda a decisão) | **6** |
| Não consegui medir (nenhuma entrada inteira) | **0** — 3 medições parciais, listadas no fim |

Links que responderam com erro: **zero**. Nenhuma das 46 URLs devolveu 404, 403 ou 410.
**As portas mortas desta rodada não se anunciam pelo código HTTP** — as três mais graves
respondem 200 e mesmo assim não valem mais o clique. É esse o achado da rodada.

---

## A LISTA CURTA — AS 5 QUE SAEM (economize o tempo dele aqui)

| nº | Vaga | Por que sai, medido |
|---|---|---|
| **2** | **Netflix Animation Studios — Head of Characters, Vancouver** | **DESLISTADA.** A página responde **HTTP 200** e a API de detalhe também, mas o id `790317384604` **não existe** no quadro oficial: paginei as **498 vagas** do `explore.jobs.netflix.net` e o id não está em nenhuma. Busca por *"Head of Characters"* devolve 65 resultados e ela não está entre eles, enquanto as irmãs (Head of Character Effects Vancouver, Head of Environments, Head of Effects) estão. O `t_update` da requisição é de **hoje, 08/09 às 20:08 UTC**. Era a **nº 2 da fila**. |
| **13** | **Asobo Studio — Character Artist H/F, Bordeaux** | **VETO DE IDIOMA.** O texto integral na API do Lever exige, literalmente: *"Tu disposes d'un niveau de **français** et anglais opérationnel"*. A régua velha via a palavra e passava; a nova pega. Francês já derrubou duas candidaturas desta campanha. |
| **38** | **DreamWorks / NBCUniversal — Visual Development Artist, Glendale** | **REQUISIÇÃO ENCERRADA.** API do SmartRecruiters: **`active: false`**. A própria página do anúncio escreve *"This job has expired"* e *"Sorry, this job has expired"*. Não aparece na listagem pública da NBCUniversal3 (273 vagas). |
| **41** | **Quantic Dream — Candidature Spontanée, Paris** | **DUPLICATA INTERNA DA PRÓPRIA FILA.** É **exatamente a mesma requisição da nº 27**: mesmo uuid Lever `cc1dacb2-01b7-47c0-b827-9b9b786d1dd7`, mesma URL, mesmo formulário. Mandar as duas é mandar duas vezes a mesma candidatura espontânea. Mantenha a nº 27. |
| **46** | **Gigantic Duck — 3D Artist, remoto** | **DUPLICATA INTERNA DA PRÓPRIA FILA.** É **exatamente a mesma porta da nº 33**: mesma URL `giganticduck.com/application/`, mesmo Contact Form 7, mesmos campos, mesma opção `3D Artist`. Não existem dois formulários. Mantenha uma só — e como a nº 46 é a que está corretamente descrita (remoto, efetivo, 40h), **prefira apagar a nº 33**. |

> Só as duas duplicatas internas (41 e 46) já devolvem **~2 min** ao dia dele, e a nº 2 tira do
> caminho a segunda coisa que ele ia clicar.

---

## AS 6 QUE MUDARAM

| nº | Vaga | O que mudou |
|---|---|---|
| **4** | Gaijin Entertainment, Budapeste | **Virou também remota.** O anúncio agora diz *"Work format: **remote or office**"*. E a lista de realocação paga cresceu: *"Our company helps with relocation to: Hungary, Cyprus, Germany, **Dubai**, Montenegro, Latvia, and Armenia"* — Dubai não estava na versão da fila. O quadro reforça: *"Gaijin Entertainment considers candidates from all over the world, regardless of citizenship or place of residence."* Continua sendo o melhor sinal de visto da fila. |
| **7** | Avalanche Studios, Estocolmo | **Apareceu recusa explícita de realocação:** *"please note that **relocation assistance is not available for this role**"*. Não é veto legal — ele pode se candidatar —, mas a fila vende esta como "melhor relação valor/minuto" e o Vini vai ter que se mudar por conta própria para a Suécia. Decida sabendo. |
| **24** | TRIXTER, Munique/Berlim | **É FREELANCE.** A ficha do anúncio diz *"Employment Type **Freelance** · Schedule Full-time"*. A fila não registra isso, e a regra da campanha é vaga fixa. Continua sendo a única porta da casa, mas entra como freelance, não como efetivo. |
| **32** | Keywords / Lakshya, Hair Specialist | **Virou contrato e perdeu os EUA.** API do Workable: `type: **contract**`, `workplace: remote`, `state: published`. As localidades publicadas hoje são só **Canadá e Reino Unido** — os **EUA saíram**. A fila anuncia "Canadá, EUA e Reino Unido". |
| **43** | TTK Games, Estocolmo | **O LINK DA FILA APONTA PARA UMA REQUISIÇÃO QUE NÃO EXISTE MAIS — e a vaga está viva em outro id.** O id `561860` **não está** entre as 14 vagas publicadas em `ttkgames.pinpointhq.com/postings.json`, e `postings/561860.json` devolve **404**. A **Character Artist** viva é o id **`558871`** (Stockholm, `permanent`, `hybrid`). **E a faixa salarial sumiu:** `compensation_visible: false`, `compensation_minimum` e `compensation_maximum` **nulos** — os 34.000–47.000 SEK/mês que a fila usa como argumento **não estão mais publicados**. Links que eu testei e responderam 200: `https://ttkgames.pinpointhq.com/en/postings/88f9f885-d2a6-4815-953d-2866d92fe370` e `https://ttkgames.com/careers/job?id=558871`. |
| **44** | Behaviour, *7 Days to Die* | **RISCO DE DUPLICATA NÃO RESOLVIDO, e é interno ao próprio arquivo.** A requisição está viva (Lever 200, `createdAt` 25/08). Mas a fila **se contradiz**: o bloco "Cuidados" da **nº 1** e da **nº 3** diz *"a de 7 Days to Die já foi enviada em 30/08, não repita aquela"*, e as duas cartas prontas afirmam *"I already applied to your 7 Days to Die opening"* — enquanto a nº 44 afirma ser requisição nova nunca enviada. `automacao/cacada-web.md` diz só que ela "não existe no painel", que não é o mesmo que "não foi enviada". **Não consegui medir o envio** (não tenho acesso ao Gmail nesta sessão e `enviados.csv` não tem uma linha sequer de Behaviour/bhvr). **Resolva antes de clicar**, senão são três Behaviour no mesmo dia mais uma provável duplicata. |

---

## COMO LI A RÉGUA DOS 17

Rodei os dezessete termos no **texto integral** de cada anúncio (JSON da API onde havia API;
HTML servido, inclusive o conteúdo dentro de `<script>`, nas páginas próprias).
Padrões de falso positivo que apareceram e que **não** são veto:

- **`french` na lista de países do seletor.** BambooHR (19, 20, 26, 28) e Wix/Squarespace (14, 18)
  carregam a lista mundial de países: *"France"*, *"French Guiana"*, *"French Polynesia"*,
  *"Saint Martin (French part)"*. Seis entradas acusaram por isso. Nenhuma exige francês.
- **`located in` = endereço do estúdio.** Frontier: *"The modern studio is **located in** the vibrant
  technology hub of Cambridge (UK)"*. EF Games: *"a game development studio **located in** the heart of Madrid"*.
- **`resident` dentro de outra palavra.** Distillery: a opção de menu *"Permanent **Resident**"*.
- **`authoriz` no aviso antifraude.** Skydance: *"If you suspect that you are being contacted by an
  **unauthorized** person…"* — é o aviso contra golpe de recrutamento, não requisito.
- **`sponsor` em benefício.** Jam City: *"100% Covered Medical and Company-**Sponsored** Dental & Vision"*.
- **`work permit` / `eligib` / `sponsor` como PERGUNTA do formulário.** Framestore (11, 16),
  Cinesite (19, 20), TRIXTER (24), Distillery (18), One Of Us (40). **Perguntar não é vetar** —
  é justamente o contrário, é casa que contrata quem precisa.
- **`deutsch` / `french` no seletor de idioma do site.** Gaijin (*"de / Deutsch"*), Fortiche
  (*"LAUREATE OF … SUPPORTED BY THE **FRENCH** GOVERNMENT"*, rodapé de financiamento CNC).
- **`relocat` / `eligib` como nome de campo JSON.** Eidos-Montréal: `"relocationEligible": null`.

Casaram **a favor** (é benefício, não barreira):

- **5 Gameloft:** *"Support for new employees **relocating** from countries or regions outside Quebec"*.
- **12 Frontier:** *"We can provide a comprehensive **relocation** support package as part of any offer,
  should you need to relocate"*.
- **35 RocketWerkz:** *"Assistance is provided for **relocation** & support for obtaining a visa"*.
- **4 Gaijin:** *"Our company helps with **relocation** to: Hungary, Cyprus, Germany, Dubai, …"*.

Os dois termos novos, **`based in` e `only from`**, pegaram exatamente um padrão:
**Netflix (2, 31, 39)** — *"This role is **based in** Vancouver, British Columbia. Hybrid Role
(Minimum of 3 **days a week** in the office)"* e, em Sydney, *"This role is based out of Sydney, Australia"*.
**Isto NÃO é o caso People Can Fly.** Lá a frase restringe o candidato (*"open to candidates **only from**
… who are based in Europe"*); aqui a frase diz **onde o cargo fica**, e o Vini quer se mudar.
Registro como condição de presença, não como veto. **`only from` não casou em nenhuma das 46.**

---

## CARACTERES INVISÍVEIS — VARREDURA FEITA

Varri todas as 46 respostas por `Cf` (Unicode format), zero-width e tags de seleção.
**Nenhuma tentativa de instrução escondida foi encontrada.** Dois achados, os dois benignos:

- **nº 11 Framestore (3D Modeller Montréal):** quatro `U+200B` (zero-width space), todos dentro de
  `<p>​​</p>` — parágrafo vazio de editor WYSIWYG, entre *"Knowledge of anatomy"* e
  *"Accessibility Statement"*. Sem texto oculto.
- **nº 29 Grimlore Games:** um `U+FEFF` (BOM) no primeiro byte do arquivo. Artefato de codificação.

---

## TABELA DE MEDIÇÃO — AS 46, UMA A UMA

Legenda: **HTTP** = código literal que eu recebi. **Fonte** = onde medi o estado.

### Prioridade 1 — as dez primeiras da fila

| nº | Vaga | HTTP | Fonte oficial e estado literal | Régua dos 17 | Veredito |
|---|---|---|---|---|---|
| 1 | Behaviour — Sr 3D Character Artist, *Dead by Daylight*, Montréal | **200** (API e `/apply`) | `api.lever.co/v0/postings/bhvr/18024240-…` → 200, *"Senior 3D Character Artist - Dead By Daylight"*, `Permanent Full-Time`, `workplaceType: hybrid`, Montreal QC | **zero dos 17** | **SEGUE** |
| 2 | Netflix — Head of Characters, Vancouver | **200** (página, API, `/`, `?microsite=`) | Ausente das **498** vagas do quadro; ausente da busca *"Head of Characters"* (65 res.); `t_update` **hoje 20:08 UTC**; faixa ainda no texto: *"$204k - $279k CAD"* | `based in` (local do cargo), `days a week` (híbrido 3d) | **SAI DA FILA — deslistada** |
| 3 | Behaviour — Sr 3D Character Artist, projeto não anunciado | **200** | Lever API 200, `Permanent Full-Time`, `hybrid`, Montreal QC, `createdAt` 17/07 | **zero dos 17** | **SEGUE** |
| 4 | Gaijin — Lead Material & Texture Artist, Budapeste | **200** (vaga e quadro) | Listada em `gaijinent.com/job`; título confere | `relocat` **a favor**; `deutsch` = seletor de idioma (FP) | **MUDOU** — remoto ou escritório; +Dubai |
| 5 | Gameloft — Candidature Spontanée, Montréal | **200** | `api.smartrecruiters.com/v1/companies/gameloft/postings/744000116612089` → **`active: true`, `visibility: PUBLIC`**, `REF1006B`, Full-time | `relocat` **a favor**; `french` = campo `language: fr-CA` do anúncio (FP) | **SEGUE** |
| 6 | Ubisoft Massive — Lead Character Artist, Malmö | **200** | SmartRecruiters API → **`active: true`, `PUBLIC`**, `REF31739L`, Malmö/Skåne, Full-time, Mid-Senior | **zero dos 17** | **SEGUE** |
| 7 | Avalanche — Lead Character Artist, Estocolmo | **200** | Lever API 200, *"Lead Character Artist"*, `Permanent Employment`, `hybrid`, Stockholm | `relocat` **CONTRA** (ver abaixo) | **MUDOU** |
| 8 | Rodeo FX — Senior Lookdev Artist, Toronto | **200** | SmartRecruiters API → **`active: true`, `PUBLIC`**, `RDO243M`, Toronto ON, Full-time | `days per week`: *"employees are expected to work from the studio at least **three days per week**"* — condição de híbrido, não veto | **SEGUE** |
| 9 | Ubisoft — Team Lead, Modeling (Unreal), Montréal | **200** | SmartRecruiters API → **`active: true`, `PUBLIC`**, `REF31530C`, Montreal QC | **zero dos 17** | **SEGUE** |
| 10 | Lighthouse Games — Lead Character Artist, Leamington Spa | **200** | `apply.workable.com/api/v1/accounts/lighthousegames/jobs/F7F90250DA` → **`state: published`**; consta das 28 vagas publicadas da conta | **zero dos 17** | **SEGUE** |

> **Correção de fato sobre o proxy:** o brief diz que `apply.workable.com` está bloqueado. **Hoje não está.**
> Medi 200 tanto na página `apply.workable.com/lighthousegames/j/F7F90250DA/` quanto na API v1 de conta.
> O que ele devolve, sob rajada, é **429 `error code: 1015`** (limite de taxa da Cloudflare), que passa
> esperando ~40s entre chamadas. `linkedin.com` e `search.jobvite.com` eu não precisei tocar.

### Prioridade 2 — as seis mais novas (40 a 46)

| nº | Vaga | HTTP | Fonte oficial e estado literal | Régua dos 17 | Veredito |
|---|---|---|---|---|---|
| 40 | One Of Us — Modeller, Paris | **200** | Workable, conta `one-of-us`: consta das 21 vagas publicadas, `Modeller · Paris · France`, `employment_type: **Contract**`, `telecommuting: false`, publicada 30/07 | **zero dos 17** | **SEGUE** (contrato, como a fila já diz) |
| 41 | Quantic Dream — Candidature Spontanée, Paris | **200** | `api.eu.lever.co/v0/postings/quanticdream` → 3 vagas; `cc1dacb2-…` presente, `CDI`, Paris | anúncio sem corpo de texto (espontânea): zero | **SAI — duplicata exata da nº 27** |
| 42 | Eidos-Montréal — Lead Environment Artist | **200** | Dayforce API `…/api/geo/eic/jobposting/eic/en-CA/1/2192` → **`postingStatus: 1`**, `postingExpiryTimestampUTC: null`, Req **158**, *"Permanent – Full-Time"*, 400 de Maisonneuve Ouest | `eligib`/`relocat` = nomes de campo JSON (FP). No corpo do anúncio: **zero** | **SEGUE** |
| 43 | TTK Games — Character Artist, Estocolmo | **200** na página; **404** em `postings/561860.json` | O id da fila **não está** entre as 14 publicadas; a viva é **`558871`**, `permanent`, `hybrid`; faixa **não publicada** (`compensation_visible: false`) | **zero dos 17** | **MUDOU — troque o link e apague o argumento da faixa** |
| 44 | Behaviour — Sr 3D Character Artist, *7 Days to Die* | **200** | Lever API 200, `Permanent Full-Time`, `hybrid`, Montreal QC, `createdAt` **25/08** | **zero dos 17** | **MUDOU — risco de duplicata, resolver antes** |
| 45 | Blue Zoo — Blender Modeller (Experienced), Londres | **200** (redireciona para `registration.aspx`, como a fila avisa) | Vaga 1310 viva em `/vacancies/1310/BLENDER_MODELLER.html` → *"Blender Modeller - Experienced"* | **zero dos 17.** E o sinal de ouro se confirma: contei **8** vagas com o prefixo *"UK Only \|"* no quadro (1307, 1306, 1293, 1288, 1274, 1273, 1272, 1267) e **a 1310 não tem o rótulo** | **SEGUE** |
| 46 | Gigantic Duck — 3D Artist, remoto | **200** | `giganticduck.com/careers/` lista *"3D Artist, Bombergrounds — **Remote, Full time (40 hours/week)**"* e *"3D Artist, Unannounced Game — Remote, Full time (40 hours/week)"*; o formulário tem `Position: 3D Artist` e `Location: Remote` | **zero dos 17** | **SAI — duplicata exata da nº 33** (a vaga é ótima; o que sai é a entrada repetida) |

### O resto — 11 a 39

| nº | Vaga | HTTP | Fonte oficial e estado literal | Régua dos 17 | Veredito |
|---|---|---|---|---|---|
| 11 | Framestore — 3D Modeller (contrato curto), Montréal | **200** | `framestore.recruitee.com/api/offers/` (53 ofertas) → **`status: published`**, id 2120070, publicada 26/08 | `sponsor` = pergunta *"Will you need visa sponsorship?"* (FP, a favor) | **SEGUE** |
| 12 | Frontier — Experienced Character Artist, Cambridge | **200** | `api.eu.lever.co/…/frontier/3571ace3-…` → 200, `Permanent`, `Cambridge / Hybrid` | `relocat` **a favor**; `days per week` (mín. 3 no estúdio); `located in` = endereço (FP) | **SEGUE** |
| 13 | Asobo — Character Artist H/F, Bordeaux | **200** | Lever EU API 200, `Full-time`, `onsite`, Bordeaux | **`français`: *"Tu disposes d'un niveau de français et anglais opérationnel"* — VETO REAL** | **SAI DA FILA** |
| 14 | Cosmico — Senior 3D Artist, Suécia | **200** | `cosmicogames.com/career` lista **SENIOR 3D ARTIST**; o botão aponta para `href="/contact"`, como a fila diz | `french` = lista de códigos telefônicos de país (FP) | **SEGUE** |
| 15 | Rodeo FX — Senior Lookdev Artist, Montréal | **200** | SmartRecruiters API → **`active: true`, `PUBLIC`**, `RDO180I`, Montreal QC | `days per week`: mesma frase dos *"three days per week"* de Toronto | **SEGUE** |
| 16 | Framestore — Blender Generalist / VisDev, Montréal | **200** | Recruitee API → **`published`**, id 2718959, publicada 21/08 | `sponsor` = pergunta do formulário (FP) | **SEGUE** |
| 17 | Framestore — Blender Generalist, Londres | **200** | Recruitee API → **`published`**, id 2709436, publicada 13/08 | `relocat` = pergunta *"Are you open to relocating to London, UK?"* (FP) | **SEGUE** |
| 18 | Distillery VFX — Job Application Form, Vancouver | **200** | Formulário Wix íntegro: o menu **Current Status in Canada** ainda traz as 4 opções, com **`"Need a work permit"`** — e `"Open work permit"` logo antes, exatamente a armadilha que a fila avisa | `work permit`/`resident` = opções do próprio menu (FP); `french` = lista de países (FP) | **SEGUE** |
| 19 | Cinesite — Candidature Spontanée, Montréal | **200** | `cinesitemontreal.bamboohr.com/careers/93/detail` → **`jobOpeningStatus: "Open"`**, Montreal/Quebec | `work permit` = pergunta *"What is your working status in Canada ? (work permit required?)"* (FP) | **SEGUE** |
| 20 | Cinesite — Speculative Application, Vancouver | **200** | `cinesitevancouver.bamboohr.com/careers/260/detail` → **`jobOpeningStatus: "Open"`**, `employmentStatusLabel: **Fixed Term**` (a fila já avisa) | `work permit` = pergunta; `french` = lista de países (FP) | **SEGUE** |
| 21 | Fortiche — "Become a Forticher", Paris/Montpellier/Las Palmas | **200** | Formulário de 3 passos íntegro, com o bloco **Department** e *Character modeling* | `french` = *"SUPPORTED BY THE FRENCH GOVERNMENT"*, rodapé de financiamento (FP) | **SEGUE** |
| 22 | EF Games — Senior 3D Hard Surface & Vehicle, Madri | **200** | Anúncio vivo e completo, *"Senior 3D Hard Surface And Vehicle Artist"*, Madri | `located in` = endereço (FP); `bilingual` = opções do menu de idioma do formulário — **confirma** que ele vai ter que responder proficiência em espanhol | **SEGUE** |
| 23 | Skydance Animation — Senior Grooming TD, Madri | **200** | `api.lever.co/…/skydance/9ad28cab-…` → 200, *"Senior Grooming TD"*, `Full Time`, `hybrid`, Madrid | `authoriz` = aviso antifraude *"unauthorized person"* (FP) | **SEGUE** |
| 24 | TRIXTER — Speculative Job Application, Munique/Berlim | **200** | Página viva; ficha: *"Location München/Berlin · Employment Type **Freelance** · Schedule Full-time"* | `eligib` = campo *"Eligibility to work in Germany"* (FP) | **MUDOU — é freelance** |
| 25 | GIANTS Software — Open Application | **200** | SmartRecruiters API → **`active: true`, `PUBLIC`**, `REF72R`, Erlangen/BY, Full-time | **zero dos 17** | **SEGUE** |
| 26 | nWave — Speculative Application, Bruxelas/Liège | **200** | `nwave.bamboohr.com/careers/121/detail` → **`jobOpeningStatus: "Open"`**. Menus intactos: estúdio `Brussels`/`Liege`; departamento **`Character_Modeling (CHR_MOD)`**; nível **`SENIOR`** | `french` = lista de países (FP) | **SEGUE** |
| 27 | Quantic Dream — Candidature Spontanée, Paris | **200** | Lever EU API → presente na lista de 3 vagas da conta, `CDI`, Paris, Ile de France | anúncio sem corpo: zero | **SEGUE** (e é esta que fica, não a 41) |
| 28 | BetaDwarf — Unsolicited Application, Copenhague | **200** | `betadwarfaps.bamboohr.com/careers/28/detail` → **`jobOpeningStatus: "Open"`**, Full-Time | `french` = lista de países (FP) | **SEGUE** |
| 29 | Grimlore Games — Open Application, Munique | **200** | Página viva, *"Open Application (m/f/d) … If you do not see your role posted in our job openings, do not let that stop you"*, botão **APPLY NOW** | **zero dos 17** | **SEGUE** |
| 30 | The Knights of Unity — espontânea, Wrocław | **200** (redireciona para `theknightsofu.elevato.net`) | Formulário íntegro: `Imię`, `Nazwisko`, `Telefon komórkowy`, até **4 arquivos de CV**, **`Oczekiwania finansowe / Kwota`**, **`Okres wypowiedzenia`**, `Informacja dodatkowa`, cláusula de consentimento | **zero dos 17** | **SEGUE** |
| 31 | Netflix — Head of Character Effects (CFX), Vancouver | **200** | **Presente** nas 498 vagas do quadro. Faixa publicada mudou de valor: *"typically **$205k -$259k CAD**"* | `based in`/`days a week` = local do cargo + híbrido 3d, não veto | **SEGUE** |
| 32 | Keywords / Lakshya — Character Artist, Hair Specialist | **200** | Workable API → **`state: published`**, `remote: true`, `workplace: remote`, **`type: contract`**, localidades **Canadá e Reino Unido** | **zero dos 17** | **MUDOU** |
| 33 | Gigantic Duck Games — 3D Artist, remoto | **200** | Mesma porta da nº 46; quadro lista as duas 3D Artist como *"Remote, Full time (40 hours/week)"* | **zero dos 17** | **SEGUE — mas é a mesma entrada da 46; mande UMA** |
| 34 | Obsidian — General Application (Remote), EUA | **200** | Página viva: *"General Application · **Remote** · Full Time · **Entry Level**"*, formulário com *"Are you willing to relocate?"* | `relocat` = pergunta do formulário (FP) | **SEGUE** (repare no rótulo **Entry Level** da requisição) |
| 35 | RocketWerkz — Expressions of Interest, Auckland | **200** | `careers.rocketwerkz.com/api/offers/` (4 ofertas) → **`status: published`** | `based in` + `relocat` **a favor**: *"…based in Auckland with flexible working conditions. **Assistance is provided for relocation & support for obtaining a visa**"*; `located in` = pergunta do formulário | **SEGUE** |
| 36 | Jam City — Principal 3D Generalist, San Francisco | **200** | `api.lever.co/…/jamcity/14272af5-…` → 200, `Full Time`, `onsite`, San Francisco, CA. **Faixa segue publicada:** *"Pay Range: $75,000 — $120,000 salary per year"* | `sponsor` = *"Company-Sponsored Dental & Vision"* (FP) | **SEGUE** |
| 37 | Valve — 3D Character Artist, Bellevue | **200** | Página viva: *"3D Character Artist · We work together in person, in Bellevue, WA, USA · Apply now!"* | **zero dos 17** | **SEGUE** |
| 38 | DreamWorks — Visual Development Artist, Glendale | **200** (a página mente) | SmartRecruiters API → **`active: false`**; página: *"This job has expired"* | — | **SAI DA FILA** |
| 39 | Netflix — Head of Character Effects (CFX), Sydney | **200** | **Presente** nas 498 vagas do quadro; *"This role is based out of Sydney, Australia"* | `days a week` = híbrido 3d | **SEGUE** |

---

## O QUE MEDI PELA REGRA DAS DUAS VARIAÇÕES

Antes de escrever "morreu", testei variações. Três vezes isso mudou a resposta:

1. **nº 43 TTK Games.** `postings/561860.json` → **404**. Mas em vez de declarar morta, li o quadro
   inteiro (`postings.json`) e achei a **Character Artist viva no id 558871**. Porta aberta, identificador
   velho — o sexto caso deste padrão na campanha, e o sétimo se contar o Workable abaixo.
2. **Workable (10, 32, 40).** `…/api/v3/accounts/…` → **404**, `…/api/v1/jobs/…` → **429**.
   A rota certa é **`https://apply.workable.com/api/v1/accounts/<conta>/jobs/<shortcode>`** → 200.
   E `https://www.workable.com/api/accounts/<conta>?details=true` traz o quadro inteiro com descrições,
   numa chamada só — foi assim que peguei a One Of Us.
3. **nº 42 Eidos-Montréal (Dayforce).** Todas as rotas óbvias deram 404. O erro **400** de validação
   entregou a assinatura da rota; a certa é
   **`/api/geo/eic/jobposting/eic/en-CA/1/2192`** (o `1` é o `jobBoardId` numérico). Fica registrada
   para as próximas Dayforce da campanha. Nenhum `422` apareceu — o locatário `eic` existe.

E o contrário também: **nº 2 Netflix responde 200 em quatro variações de URL** (com e sem barra,
com `?microsite=`, e na API de detalhe) e mesmo assim está fora do quadro. **200 não é vida.**

---

## AS 3 MEDIÇÕES PARCIAIS (o que não deu para medir por inteiro)

1. **nº 18 Distillery VFX.** Consegui medir a **página e o formulário** (Wix, os menus e opções estão
   íntegros no HTML servido). O que **não existe** é texto de anúncio: é um formulário genérico de
   candidatura, sem descrição de vaga. Então a régua dos 17 rodou sobre o formulário, não sobre um anúncio.
2. **nº 43 TTK Games.** O corpo do anúncio no `postings.json` vem em campos curtos
   (`key_responsibilities`, `skills_knowledge_expertise`, `benefits`) e a página do Pinpoint monta o
   resto por JavaScript. Rodei a régua sobre os campos da API (2.450 caracteres) — **zero ocorrências** —
   mas não sobre uma renderização completa. Se quiser certeza absoluta do texto integral:
   **precisa-de-navegador** em `https://ttkgames.pinpointhq.com/en/postings/88f9f885-d2a6-4815-953d-2866d92fe370`.
3. **nº 44 Behaviour 7DtD.** Medi que a **requisição está viva**. Não medi, e não tenho como medir aqui,
   **se ela já foi enviada em 30/08** — não tenho acesso ao Gmail nesta sessão e `enviados.csv` não
   contém nenhuma linha de Behaviour. **precisa-de-navegador** (ou de acesso ao Gmail) para fechar isso.

---

## RECOMENDAÇÃO DE ORDEM, JÁ CORRIGIDA

Com a nº 2 fora, a fila útil começa assim:

1. **nº 1 Behaviour — Dead by Daylight** (Lever, viva, sem veto)
2. **nº 44 Behaviour — 7 Days to Die** *(só depois de resolver a duplicata)* ou, se não resolver,
   **nº 3 Behaviour — projeto não anunciado** — mas **não mande as três Behaviour no mesmo dia**,
   que é a regra que a própria fila estabeleceu na Scopely e na Epic
3. **nº 46/33 Gigantic Duck** (40 segundos, remota, efetiva — mande **uma** vez)
4. **nº 5 Gameloft Montréal** (apoio de realocação escrito)
5. **nº 4 Gaijin** (agora também remota, realocação paga para 7 países)
6. **nº 12 Frontier** (pacote de realocação escrito) e **nº 35 RocketWerkz** (realocação + visto escritos)

**Fila efetiva depois desta rodada: 41 entradas** (46 − 5), das quais 6 com fato novo a ler antes de clicar.
