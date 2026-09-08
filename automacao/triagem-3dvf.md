# Triagem dos estúdios novos do mapa 3DVF — rodada de 08/09/2026

Arquivo trabalhado: `automacao/garimpo-cgstudiomap.csv` (889 linhas de dados).
**Nenhum e-mail, rascunho ou formulário foi tocado. Nenhum arquivo compartilhado foi editado. Nenhum navegador foi aberto** — todo o trabalho saiu de `curl`, WebSearch e WebFetch, com `https://` e User-Agent de Chrome em todas as chamadas.

---

## 1. Os números, sem inflar

| Medida | Valor |
|---|---|
| Linhas do CSV varridas nesta rodada | **859** (todas as que têm site publicado e ainda não eram `sim`) |
| **Linhas convertidas de `nao_verificado`/`nao_encontrada` em status medido** | **289** |
| Estúdios com **ATS identificado e API respondendo** | **78 detectados, 46 com API respondendo + 21 medidos à mão + 12 por sitemap de Teamtailor** |
| **Vagas vivas da disciplina com link direto e busca de veto conferida** | **22** (em 14 estúdios) |
| Dessas, **NOVAS para a campanha** (cruzadas por referência de requisição) | **5** — e 3 das 5 são estágio/júnior |
| Vagas que **OFEREM patrocínio ou realocação por escrito** | **2** (Frontier e Floating Rock) |
| Vagas **descartadas por veto ESCRITO** | **3** |
| Estúdios que **precisam de navegador** | **86** |
| Estúdios cujo **site não respondeu** | **130** |
| Continuam **por verificar** | **491 `nao_verificado` + 103 `nao_encontrada`** |

**Movimento da coluna de status:**

| Status | Antes | Depois |
|---|---|---|
| `sim` | 6 | **20** |
| `nao` (quadro oficial lido, nada da disciplina — afirmação medida) | 0 | **59** |
| `precisa-de-navegador` | 0 | **86** |
| `site-fora-do-ar` | 0 | **130** |
| `nao_encontrada` | 179 | 103 |
| `nao_verificado` | 704 | 491 |

**A honestidade que importa:** triei 859 e converti **289**. Não triei os 668 novos por completo. Dos 22 achados da disciplina, **17 já eram conhecidos da campanha** — o dedupe por referência de requisição, cruzado contra `docs/index.html`, `enviados.csv` e `automacao/processados.csv`, matou 17 de 22. Isso confirma o alerta do briefing.

---

## 2. Vagas vivas da disciplina — link direto, ATS, formato e veto LITERAL

### 2.1 DESTAQUE — as que OFERECEM realocação ou patrocínio

**⭐ Frontier — Experienced Character Artist — Cambridge, Reino Unido**
`https://jobs.eu.lever.co/frontier/3571ace3-9f1a-4db2-9e2b-5eb8c8487181`
- **ATS:** Lever EU (token `frontier`, achado no HTML de frontier.co.uk, não adivinhado). Quadro com 14 vagas.
- **Formato:** efetivo (`Permanent Employment`), **híbrido — mínimo 3 dias no estúdio**. Sem faixa publicada.
- **Busca literal de veto no anúncio integral (5.115 caracteres):** `authoriz` = 0, `eligib` = 0, `sponsor` = 0, `work permit` = 0, `must be based` = 0, `LMIA` = 0, `days a week` = 0, `French` = 0, `français` = 0, `resident` = 0.
- **SINAL POSITIVO ESCRITO:** *"We can provide a comprehensive relocation support package as part of any offer, should you need to relocate."* E nos benefícios: *"support with relocation"*.
- Conteúdo: ZBrush, Maya, Substance Painter, sculpting, topologia, UVs, baking, texturização, personagem e criatura.
- **DUPLICATA — já está no painel com esta mesma URL.**

**⭐ Floating Rock — Character Artist | Games — Wellington, Nova Zelândia**
`https://floating-rock.com/careers/`
- **ATS:** nenhum; quadro em HTML próprio, legível por curl.
- **Formato:** híbrido, **pelo menos 60% presencial no estúdio de Wellington**. Sem faixa publicada.
- **Busca literal:** `authoriz` = 0, `eligib` = 0, `sponsor` = 0, `must be based` = 0, `LMIA` = 0, `French` = 0, `resident` = 0. Aparecem `days a week` (*"Hybrid work (WFH 2 days a week if you'd like)"*, outra vaga do mesmo quadro), `relocat` e `visa` — **os três são positivos**.
- **SINAL POSITIVO ESCRITO:** *"Visa support to live in New Zealand"* e *"Relocation and Visa support to live in beautiful New Zealand."*
- Também abre **3D Environment Artist | Games** no mesmo quadro (prioridade média).
- **DUPLICATA — a casa já está no painel, com dossiê de formulário pronto e carta enviada em 07/09.**

### 2.2 NOVAS para a campanha (as 5 que sobreviveram ao dedupe)

**1. Netflix Animation Studios — Environment Surfacing Supervisor — Vancouver, Canadá**
`https://explore.jobs.netflix.net/careers/job/790314628209`
- **ATS:** Eightfold da Netflix (`explore.jobs.netflix.net/api/apply/v2/jobs`). Achado por outra porta: a Scanline VFX de hoje é a **Eyeline Studios**, da Netflix, e o quadro real dela é este.
- **Formato:** híbrido, **mínimo 3 dias por semana no escritório**, Vancouver. **Faixa publicada: US$/CAD 163k – 223k CAD** (o anúncio diz *"The overall market range for this role is typically $163k - 223k CAD"*).
- **Busca literal:** único termo que aparece é `days a week`, no trecho *"...based in Vancouver, British Columbia. Hybrid Role (Minimum of 3 days a week in the office)."* Nenhum `authoriz`, `eligib`, `sponsor`, `work permit`, `LMIA`, `French`, `resident`.
- É **surfacing**, que é a disciplina dele (textura e material). **Ambiente, então prioridade média pela regra** — mas é Canadá e é supervisão sênior.
- **NOVA:** a referência 790314628209 não aparece em nenhum dos três arquivos da campanha.

**2. DNEG — Facial Modeller (DNEG VFX) — Londres, Reino Unido**
`https://jobs.jobvite.com/double-negative-visual-effects/job/oF9Yyfw4`
- **ATS:** Jobvite (token `double-negative-visual-effects`).
- **Formato:** *Expression of Interest* — ou seja, **banco de talentos, não anúncio datado**. Londres.
- **Busca literal no anúncio inteiro:** nenhum dos termos. Zero `sponsor`, zero `eligib`, zero `visa`.
- Conteúdo: modelagem de rosto em Maya, ZBrush/Mudbox, topologia limpa, UVs, displacement, look development, wrap-based workflows.
- **NOVA:** referência `oF9Yyfw4` não consta em nenhum arquivo da campanha.

**3. Skydance Animation Madrid — Environment Surfacing Artist — Madri, Espanha**
`https://skydance.com/job?id=c5793932-893f-418a-a24a-7749fcf1c90e`
- **ATS:** quadro próprio da Skydance (o formulário final vai para o Lever).
- **Formato:** híbrido (`#LI-Hybrid`), Madri. Sem faixa publicada.
- **Busca literal:** único `authoriz` é do aviso antifraude (*"contacted by an unauthorized person"*), falso positivo. Nada mais.
- Ambiente → **prioridade média**.
- **NOVA:** referência `c5793932` não consta na campanha (as irmãs Lead, Senior e Environment Modeling já constam).

**4 e 5. Skydance Animation Madrid — Junior Environment Surfacing Artist e Environment Surfacing Trainee**
`https://skydance.com/job?id=4c18ce73-8217-44a7-af15-b5a5f18bc07e` e `.../f5cdab33-a028-4fe2-bc19-638926d0ca80`
- Novas por referência, mas **abaixo do nível dele**. Registro por completude, não recomendo gastar rodada.
- Há ainda **Character Surfacing Trainee** (`7b435bb2-09fd-4f2f-8fca-9c2fa6666adc`), nova, mas o anúncio exige por escrito: *"Must be currently enrolled in your last..."* e *"Must be available for at least 3 months onsite (from Monday until Friday, 35h/week)"*. Não serve.

### 2.3 Da disciplina, medidas e confirmadas vivas — mas JÁ CONHECIDAS

Todas foram lidas na fonte oficial nesta rodada e **todas caíram no dedupe por referência de requisição**. Estão aqui para que ninguém gaste rodada de navegador com elas de novo.

| Estúdio | Vaga | Ref./link | Veto literal |
|---|---|---|---|
| Avalanche Studios | Lead Character Artist, Estocolmo, híbrido 3 dias, permanente | `jobs.lever.co/avalanchestudios/8f7bd580-...` | Nenhum termo de autorização. **Mas diz por escrito:** *"please note that relocation assistance is not available for this role"* |
| DNEG | Modeleur de personnages / Character Modeler, **Montréal**, Hybrid Remote | `.../job/ooyGAfwW` | Nenhum dos termos |
| DNEG | Groom TD (DNEG ANIM), Londres, Hybrid Remote | `.../job/oQKJAfwD` | Nenhum dos termos |
| Sony Pictures Imageworks | Senior Look Development Artist (Montréal) + Environment Artist, Experienced Modeler, Experienced Texture Artist, Look Development Artist, Modeler, Texture Artist (Vancouver) — 7 requisições | Greenhouse `sonypicturesimageworks` | Nenhum termo nos títulos; várias **já enviadas e confirmadas** |
| Image Engine | Look Development Artist Senior (28), Texture & Look Dev Mid (183), General Application Assets (21), Vancouver | BambooHR `imageengine` | **28 e 183 já marcadas no painel com VETO DE RESIDÊNCIA escrito** |
| ICON Creative Studio | Intermediate Modeling/Texture Artist, Vancouver (136) | BambooHR `iconcreative` | Já enviada 31/08, duplicata confirmada |
| Barnstorm VFX | Lead Creature Artist, Montreal (176) | BambooHR `barnstormvfx` | Já no painel |
| Wargaming.net | 3D Character Artist (World of Tanks: HEAT), Nicósia | Greenhouse `wargamingen/jobs/8161671` | Já enviada 31/08 |
| Asobo Studio | Character Artist H/F, Bordeaux, presencial | Lever EU `asobostudio/1ab1d28f-...` | Já no painel |
| People Can Fly | Senior Asset Artist Hard Surface (Varsóvia) e Principal Character Artist (Montréal) | SmartRecruiters `PeopleCanFly` | A primeira **já marcada no painel com VETO DE RESIDÊNCIA** |
| Skydance Animation Madrid | Senior Grooming TD, Environment Modeling Artist, Senior Env Surfacing, Env Surfacing Lead | `skydance.com/job?id=...` | Só o `authoriz` do aviso antifraude |
| Digic Pictures | Character Modeler, Texture Artist, Shading Artist, Grooming Artist (lista de funções) | `digicgroup.com/job-shorts/` | Candidatura espontânea já enviada 02/09 |
| Outpost VFX | Senior Environment Artist, **Londres**, permanente, presencial, Mid-Senior | SmartRecruiters `OutpostVFX/744000142160019` | **Busca literal: ZERO em todos os termos.** Já está no painel |

---

## 3. Descartes com a frase LITERAL entre aspas

**RISE (Berlim, Colônia, Londres, Estugarda, Munique) — veto que vale para o quadro inteiro**
`https://www.risefx.com/rise-visual-effects-studios-jobs.php`
> *"You need a valid working permit for the European Union in order to apply. Unfortunately, we can't assist you in getting one for the time being."*

E na vaga de Berlim, reforçando:
> *"EU Citizenship or a pre-existing EU work permit is required"*

Além do veto, o quadro tem 8 vagas e **nenhuma é da disciplina**: HR Assistant, VFX Recruiter, Full Stack Developer, VFX Producer, VFX Production Manager, VFX Coordinator, VFX Supervisor.

**DNEG — Character Modeller for VFX style Creatures, Londres**
`https://jobs.jobvite.com/double-negative-visual-effects/job/ovLGAfwg`
> *"Candidates must be local to London to come in the office 3x a week and must be eligible to work in the UK without visa sponsorship"*

É a disciplina exata dele e mesmo assim é descarte: veto escrito de patrocínio.

**DNEG — Lead LookDev TD (DNEG VFX), Londres**
`https://jobs.jobvite.com/double-negative-visual-effects/job/oLCvzfwb`
> *"This role is currently not open. Please apply knowing that it is to ma[intain a talent pool]"*

Sem veto de autorização, mas **a própria vaga diz que não está aberta**.

**Avalanche Studios — atenção, não é veto mas pesa**
> *"At Avalanche Studios Group we're always on the lookout for talented individuals to join our passionate team, but please note that relocation assistance is not available for this role."*

Não impede candidatura (não é veto de direito de trabalho), mas o custo da mudança fica todo com ele.

---

## 4. Os que PRECISAM DE NAVEGADOR (86 no CSV) — os que valem a rodada do maestro

### 4.1 Jobvite — e aqui há uma CORREÇÃO DE AMBIENTE

**O aviso do briefing não se sustentou hoje: `jobs.jobvite.com` RESPONDEU ao curl neste ambiente.**
- `https://jobs.jobvite.com/double-negative-visual-effects/search` → **HTTP 200, 86.094 bytes, 62 vagas no HTML**, títulos e links legíveis sem JavaScript.
- `https://jobs.jobvite.com/playground-games/search` → **HTTP 200, 9 vagas legíveis**.
- Ressalva medida: o token **sem hífen** dá 403. `playgroundgames` → 403; `playground-games` → 200. O 403 é do token errado, não da rede.

Conclusão: **Jobvite não precisa de navegador nesta sessão.** Deixo registrado porque muda diagnóstico já escrito na campanha.

### 4.2 Os que realmente não abriram por API

| Estúdio | País | Por quê |
|---|---|---|
| **Folks VFX** (85) e **Rising Sun Pictures** (27) | Canadá / Austrália | Quadro SAP SuccessFactors do grupo Pitch Black. A listagem só monta em JavaScript. O sitemap do grupo lista **Senior Modelling Artist** e **Senior Look Development Artist** em Adelaide, mas as duas fichas devolvem *"The system can't display the job at this time"* — sitemap velho. Precisa de clique. |
| **MELS** (117) | Canadá | **Correção de erro meu:** meu detector casou a MELS com o SmartRecruiters do **Videotron** (a telecom dona dela), que tem 72 vagas e **zero menção a MELS**. Não é o quadro da MELS. Não registro como porta morta. |
| **Pixar** (353) | EUA | O Workday (`pixar.wd5`, site `Pixar_External_Career_Site`) respondeu uma vez com 1 vaga e depois passou a devolver **HTTP 422 em todas** as consultas, inclusive com busca vazia. **Não tenho medição reproduzível.** |
| **83 estúdios de Europa e Canadá** | — | Página de carreiras responde HTTP 200 mas o corpo tem **menos de 1.800 caracteres de texto** depois de tirar `script` e `style`: o quadro monta em JavaScript. Estão marcados um a um no CSV com o número exato de caracteres que o curl leu. |

### 4.3 Portas de captação permanente por disciplina (valem clique, não são vaga datada)

Estúdios franceses e espanhóis cujo formulário tem **menu de disciplina** com Modeling, Surfacing, Grooming, Look Dev ou Character — porta aberta sem prazo:
- **Circus** (Avignon/Paris) `https://circus.fr/jobs/` — menu com Modeling, Surfacing, Grooming
- **Clutch Frame** (Montry) `https://clutch-frame.com/jobs/` — menu com Character modeling, Grooming, Environment
- **Brunch Studio** (Paris) `https://www.brunchstudio.tv/careers` — menu com 3D Lookdev, Modeling/Surfacing
- **Uchi VFX** (Milão) `https://www.uchivfx.com/join-us` — menu com Modeling + TXT, Lookdev
- **Menhir FX** (Montpellier) `https://menhirfx.com/recrutement/`
- **Gao Shan Pictures** (La Réunion) `https://www.gaoshanpictures.com/recrutement`
- **Cyanide Studio** (França) `https://taleez.com/apply/sp/cyanide` — só candidatura espontânea, medido

---

## 5. Método que rendeu, para a próxima rodada não repetir descoberta

1. **O `jobs.json` do Teamtailor MENTE.** Devolve lista vazia mesmo com vagas vivas. Testei em Paradox Interactive: `jobs.json` = 0, **sitemap = 18 vagas**. **A rota certa é `https://<careersite>/sitemap.xml`** e ler os `<loc>` que contêm `/jobs/`. Rendeu 12 estúdios medidos numa tacada (Goodbye Kansas, Realtime, The Yard, Vine FX, Arrowhead, Sharkmob, Starbreeze, Coffee Stain, nineteentwenty, Paradox, Funcom, Capsule Studio) e mais 5 na correção (SYBO, Hampa, CI Games, ILP, Rokoko).
2. **Phenom People (Beenox e outras da Activision) vem no HTML.** O JSON inteiro está embutido em `"eagerLoadRefineSearch"` na página `/search-results` — legível por curl, sem navegador.
3. **Workday tem API POST pública:** `https://<tenant>.<dc>.myworkdayjobs.com/wday/cxs/<tenant>/<site>/jobs` com corpo `{"appliedFacets":{},"limit":20,"offset":0,"searchText":"character artist"}`. Cobre o grupo Activision/Xbox inteiro por `xboxgaming/External`.
4. **Jobylon:** o `jbl_company_id` está em texto puro no HTML da página de carreiras, e o embed **v1** (`https://cdn.jobylon.com/jobs/companies/<id>/embed/v1/?target=x&page_size=50`) devolve os títulos e as URLs. O **v2 não serve** — é template Angular vazio. Remedy = id `2986`.
5. **Netflix/Eightfold:** `https://explore.jobs.netflix.net/api/apply/v2/jobs?domain=netflix.com&query=<termo>` e a ficha em `/api/apply/v2/jobs/<id>?domain=netflix.com`. É a porta da **Eyeline Studios (ex-Scanline)**, cujo site é SPA React vazia.
6. **PlayStation:** os tokens de Greenhouse dos estúdios estão no HTML de `playstation.com/en-gb/corporate/playstation-careers/`. Colhi `firesprite`, `siei`, `naughtydog`, `pdi`, `haven` sem adivinhar nenhum.
7. **Adivinhar slug realmente não presta.** `guerrilla`, `insomniacgames`, `bendstudio` no Greenhouse: 404 nos três. Todos os tokens que renderam vieram de dentro do HTML.

---

## 6. O que travou, dito sem maquiagem

1. **491 linhas continuam `nao_verificado` e 103 continuam `nao_encontrada`.** Não triei os 668 novos por completo. O gargalo não foi a rede, foi que 599 dos 859 estúdios **não expõem ATS nenhum** — a página de carreiras é HTML próprio ou SPA, e sem ATS não há API que devolva o anúncio inteiro para a busca de veto.
2. **130 sites não responderam ao curl** dentro de 18 segundos, com User-Agent de Chrome e `https://`. Marquei `site-fora-do-ar` com o código HTTP, e **não** como "sem vaga" — são coisas diferentes.
3. **O dedupe matou 17 das 22 vagas da disciplina que achei.** Isso não é falha da varredura, é a campanha já estar bem coberta nas casas grandes de VFX de Canadá e Europa. As casas que sobram são pequenas, sem ATS, e por isso caras de medir.
4. **Errei uma atribuição de ATS e corrigi:** casei MELS com o quadro do Videotron. Corrigido para `precisa-de-navegador` em vez de deixar uma medição falsa de "sem vaga".
5. **Pixar não fechou.** API respondeu uma vez e depois 422 permanente. Registrado como não reproduzido, não como zero.
6. **Sobre CAPTCHA:** não abri nenhum formulário e não cliquei em nada. Onde o painel já registra parede de CAPTCHA (BambooHR, Lever, Greenhouse), repito o registro dele; onde não registra, **não vi captcha no HTML, e o veredito só vem com o clique**.

---

## 7. Dicionário atualizado da coluna `tem_vaga_disciplina`

| Valor | O que significa |
|---|---|
| `sim` | Vaga da disciplina confirmada, anúncio baixado, busca literal de veto rodada. **20 linhas** |
| `nao` | **Afirmação medida:** o quadro oficial foi lido inteiro (API do ATS ou sitemap do careersite) e nenhum título é da disciplina. **59 linhas** |
| `precisa-de-navegador` | Quadro em JavaScript, ATS sem rota pública ou API instável. **Não é "sem vaga".** 86 linhas |
| `site-fora-do-ar` | O domínio não serviu conteúdo ao curl. Afirmação sobre a porta, não sobre a vaga. 130 linhas |
| `nao_encontrada` | Herdado da rodada anterior: página lida, nenhum título da disciplina, mas pode ser quadro em JS. 103 linhas |
| `nao_verificado` | Não varrido. 491 linhas |

A coluna `observacao` de toda linha alterada começa com `MEDIDO 08/09` e diz **por qual rota** a medição foi feita, e termina com `| ficha:` e a URL da ficha do estúdio no 3DVF.
