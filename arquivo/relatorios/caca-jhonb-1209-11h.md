# Caça do JHON B — 12/09/2026, 11h — fila pronta, zero envio

Rodada de `curl` e API. **Nenhum navegador foi aberto, nada foi enviado, nenhum rascunho foi
criado.** Obedece à regra do Vini de 10/09 (personagem primeiro) e à divisão de faixa: quem envia
é o Jhon A.

---

## 1. PLACAR, antes de qualquer narrativa

| Medida | Número |
|---|---|
| Quadros de ATS consultados e **que responderam** | **400** |
| Vagas lidas nesta sessão | **~7.100** |
| Fontes de vaga lidas fora de ATS | 2 (planilha da comunidade, 2.686 linhas · skillshot.pl, 124 anúncios) |
| Candidatas que bateram no filtro de disciplina | 88 |
| Sobreviveram ao **escopo geográfico** | 54 |
| Sobreviveram ao **filtro de disciplina com o corpo lido** | 9 |
| Sobreviveram à **régua de veto** | 5 |
| Sobreviveram ao **dedupe por ID de requisição** | **1** |
| **FILA FINAL** | **1 — de PERSONAGEM** |

**A quebra que o Vini pediu: 1 de PERSONAGEM, 0 de ambiente.** E não é que ambiente tenha ficado
para depois: **não sobrou ambiente nenhum** — o que apareceu de ambiente (Framestore Environment
Artist e Realtime Generalist, Epic Principal/Senior Environment Artist, Sandbox Lead 3D Environment)
já estava na fila, já estava enviado, ou está atrás de parede medida.

---

## 2. A FILA — 1 entrada, e ela é a nº 51 da `FILA-DO-VINI.md`

### Absurd Ventures — **CHARACTER ART LEAD** — Santa Monica, Califórnia (efetiva, presencial)

- **URL:** https://job-boards.greenhouse.io/absurdventures/jobs/5236256007
- **ID da requisição:** `5236256007` · **`internal_job_id`:** `4680308007`
- **Publicada em 2026-09-11T19:11:12-04:00**, com `updated_at` no mesmo carimbo: vaga nova de
  ontem, **não** anúncio refrescado (a armadilha "Posted Yesterday" da Disney).
- **Faixa publicada: USD 150.000 a 185.000/ano** → pela política de 04/09, pede-se **a base**.
- **Régua de veto, termo a termo, no texto inteiro baixado pela API:** zero veto escrito.
  `eligib` é *"Certain roles may also be eligible for bonus and equity"* (benefício, falso positivo
  clássico); `within the` é *"within the constraints of a large game production"*; e o único de
  fato relevante é presença, não candidatura: *"Role is on-site in Santa Monica, CA."*
  Nenhuma ocorrência de `authoriz`, `sponsor`, `work permit`, `must be based`, `based in`,
  `only from`, `resident`, `citizen`, `relocat`, `no relocation`, `days a week`.
- **Dedupe:** `sh automacao/dedupe-agora.sh 5236256007 "Absurd"` → **ID inédito nos quatro
  arquivos**. As duas candidaturas de 11/09 nessa casa são **outras requisições**, as espontâneas
  `4141408007` (19h04) e `4141404007` (21h22). **Conferido também no Gmail, por JANELA DE TEMPO**
  (`Absurd newer_than:3d`): os dois recibos de `no-reply@us.greenhouse-mail.io` dizem apenas
  *"Thank you for submitting a general application"* e **nenhum nomeia Character Art Lead**.
- **Enviável pela automação**, e isso está medido e não suposto: o mesmo quadro aceitou duas
  candidaturas nossas ontem, com código de segurança por email resolvido dentro da janela.
- **Dossiê campo a campo, com os ids DESTA vaga, comando exato de disparo, carta escrita e arquivo
  de respostas prontos:** entrada **nº 51** da `automacao/FILA-DO-VINI.md`.

---

## 3. O QUE CAIU, E POR QUÊ — com a frase literal de cada um

### 3.1 — Caiu por VETO DE IDIOMA (1), e é o achado mais caro da rodada

**Anshar Studios — Senior/Mid Character Artist — Katowice, Polônia.** Vaga viva, título exato,
casa de 180 pessoas em AAA e AA, formulário Traffit **sem nenhuma marca de captcha no HTML**. E o
anúncio diz, na lista de requisitos:

> *"Communicative English, both spoken and written (B1/B2 level). **Fluent Polish, both spoken and
> written.** Willingness to work from our office in Katowice, Poland (on-site position only)."*

É **veto de idioma escrito**, da mesma família do francês da TAT medido em 11/09. Pela regra dessa
medição, isto **não descarta a casa**: vira **porta condicionada ao idioma**. Salário publicado
8.350–15.050 PLN brutos, e a casa oferece *"Help with relocation"* — ou seja, a porta é boa e o
idioma é o que fecha.

### 3.2 — Caiu por já ter sido desmentida na fonte oficial (1)

**PixelAnt Games — Experienced 3D Character Artist — Wrocław.** Apareceu de novo no skillshot.pl,
e a rodada de 11/09 já a tinha derrubado com a fonte oficial na mão: *"Communicative level of
English and Polish is a must"*, contrato **B2B** e não emprego efetivo, e a casa é **parede de
eRecruiter** (403 do Cloudflare no upload do CV obrigatório). **Não aplicar.** Fica escrito aqui
porque este anúncio vai reaparecer em agregador.

### 3.3 — Caiu por DISCIPLINA, com a frase colada (2)

- **Epic Games — Modeling Outsource Lead** (`6020682004` Montréal, `6020680004` Cary). Modelagem
  genérica precisa, pela regra 2 do Vini, do corpo citando personagem. O corpo cita **uma vez**, e
  descrevendo o TIME, não o trabalho: *"a team of world-class environment, character and concept
  artists"*. O que a vaga faz é supervisionar fornecedor de outsourcing: *"support and supervise
  creative content provided by outsourcing partners"*. **Não é vaga de personagem.**
- **Insomniac — Senior Facial Character TD (CONTRACT), remoto EUA.** Direção técnica facial, não
  modelagem, e a planilha da comunidade registra *"Must be authorized to work in the US"*.

### 3.4 — Caiu no DEDUPE por ID de requisição (5)

| Vaga | ID | Onde morreu |
|---|---|---|
| Riot Games — Principal 3D Character Artist, Los Angeles | `8163170` | **ENVIADA em 10/09**, com `/confirmation` |
| Wargaming — 3D Character Artist (WoT HEAT), Nicósia | `8161671` | Enviada 06/09, **recusada em 10/09** |
| Kepler Interactive — Lead 3D Character Artist | `8311973` | **Enviada 06/09**: é a mesma requisição da Tactical Adventures, republicada no quadro da holding |
| 2K Sports Lab — Senior Character Artist, Vancouver | `7835808003` | Enviada 02/09 |
| Rebellion — Senior Character Artist, **Warwick** | mesma de Oxford | Requisição enviada 30/08 e **recusada 01/09**; Warwick é o segundo local do mesmo pedido |

### 3.5 — Alvo fraco, registrado mas NÃO enfileirado (1)

**Awaken Realms — 3D Character Artist — Wrocław/remoto.** Sem veto escrito, e o corpo é personagem
e criatura (*"modeli 3D postaci, stworzeń, ubrań oraz pancerzy"*, anatomia humana e de monstro,
ZBrush, Substance, Marvelous, Blender, UE5/Unity). O que a segura:
1. **A faixa publicada é 7.000–9.500 PLN brutos** (cerca de USD 1.900/mês), muito abaixo do piso da
   política de 04/09 para Europa ocidental — e pedir a base de uma faixa dessas é o que a regra
   manda, o que a torna ruim como alvo.
2. **A rota de candidatura é o formulário do próprio agregador** (`skillshot.pl/jobs/39589...?apply_form=1`),
   com um campo anti-spam textual. O site do estúdio, `awakenrealms.com`, é **SPA que não monta por
   esta rede** (2.333 bytes de casca em todas as rotas), então a fonte oficial **não é confirmável
   por curl** — e a regra 6 exige a fonte oficial antes de escrever "vaga confirmada".
3. O anúncio é inteiramente em polonês e exige cláusula de RGPD em polonês dentro do CV.

Fica registrada para quem tiver navegador, não como fila de disparo.

---

## 4. AS DUAS MEDIÇÕES DE MÉTODO QUE VALEM MAIS QUE A VAGA

### 4.1 — **"Quadro conhecido" não é "quadro lido". Foi daí que saiu a Absurd Ventures.**

O `censo-boards-0809.csv` cobre **123 quadros**. Extraí, por expressão regular, **todos os tokens de
ATS que aparecem em qualquer URL do repositório** (painel, `enviados.csv`, `processados.csv`,
`alvos.csv`, relatórios) e cruzei com o censo. O buraco:

| Família | Tokens que a campanha conhece | No censo | **Fora do censo** |
|---|---|---|---|
| teamtailor | 151 | 32 | **119** |
| recruitee | 71 | 5 | **66** |
| greenhouse | 48 | 31 | **17** |
| bamboohr | 35 | 20 | **15** |
| workable | 19 | 0 | **19** |
| pinpoint | 20 | 0 | **20** |
| personio | 12 | 0 | **12** |

Listei inteiros os que valiam: **95 quadros responderam, 756 vagas**. **A Absurd Ventures Character
Art Lead estava exatamente aí** — quadro que a campanha conhecia desde ontem, vaga que ninguém
tinha lido, porque a casa entrou no registro pela porta espontânea e nunca pelo quadro.

**A regra, que é a de 07/09 ("liste o quadro inteiro antes de dar a casa por trabalhada") com o
número do buraco:** casa que entra no painel por candidatura espontânea entra **sem o quadro**.
Vale rodar esse cruzamento a cada censo novo; custou 95 requisições e rendeu a vaga do dia.

### 4.2 — **A régua de veto não tem POLONÊS, e a Polônia é o terceiro maior bolso de vaga da fila**

A régua de vinte termos traz `French` e a expressão genérica "idioma local exigido". Na prática, a
lista literal que os agentes rodam **não casa com `Polish`**, e a Anshar escreve o veto assim:
*"Fluent Polish, both spoken and written"*. Se eu tivesse rodado só a lista literal, esta vaga teria
passado limpa e virado candidatura que morre na primeira tela — o mesmo custo do caso Snowprint.

**A régua ganha os idiomas por extenso, e não só o francês:**
`Polish`, `polski`, `German`, `Deutsch`, `Swedish`, `svenska`, `Danish`, `Dutch`, `Spanish`,
`Italian`, `Japanese`, mais os já existentes `French`/`français`. São ruidosos e isso é barato: eles
não descartam nada sozinhos, **obrigam a ler a frase**.

---

## 5. O QUE ESTA RODADA MEDIU E A PRÓXIMA NÃO PRECISA REFAZER

1. **Diff do censo de 123 quadros por ID de vaga:** os 123 responderam, **3.583 vagas lidas, 269
   requisições novas em quatro dias, e ZERO de personagem.** As únicas que o filtro pegou eram
   ruído (`Generalist, Human Resources` da NBCU, `doll hair stylist` da Mattel, `Asset Protection`
   da Mattel) mais uma `Realtime Generalist (Expression of Interest)` da Framestore, que é
   generalista em tempo real e a casa é parede de Recruitee medida duas vezes. **O estoque dos
   quadros conhecidos continua seco, e agora com número de hoje.**
2. **Índice global do Workable** (`jobs.workable.com/api/v1/jobs`), 10 termos da disciplina: **856
   linhas, 54 dentro do escopo e da disciplina depois do dedupe, e nenhuma nova.** Tudo o que
   apareceu já está trabalhado (Rebellion, Lighthouse, Side, One Of Us, Sperasoft, Liquid
   Development) ou fora de escopo (Lakshya na Índia, Vertigo na Turquia, Keywords nas Filipinas).
   E o Workable continua sendo fila da mão dele, por Turnstile.
3. **Teamtailor em domínio próprio**, 15 casas cujo slug devolve 404: cinco têm quadro vivo
   (`careers.foolstheory.com` 4, `careers.goodbyekansas.com` 3, `career.paradoxplaza.com` 19,
   `jobs.stunlockstudios.com` 4, `careers.embark-studios.com` 18, `career.snowprintstudios.com` 2)
   e **nenhuma tem vaga de personagem** além da Snowprint já vetada.
4. **Planilha da comunidade (regra 16), 2.686 linhas, filtro de disciplina nos últimos 30 dias: 77
   linhas, e as 77 já estão resolvidas** — enviadas, recusadas, vetadas ou fora de escopo. A
   planilha está sendo lida em dia por outras rodadas; ela não é mais fonte de novidade sozinha.
5. **skillshot.pl (agregador polonês), 124 anúncios em 6 páginas:** é fonte **nova e que funciona**
   por curl, serve o anúncio inteiro em HTML e entrega o link do ATS real de cada casa. Rendeu três
   vagas de personagem vivas (Anshar, PixelAnt, Awaken Realms), e as três caíram por idioma,
   contrato ou salário. **Vale reler uma vez por semana**; a Polônia publica muito personagem.

---

## 6. COMO ISTO FOI RODADO

`python3` com `requests`, 10 a 12 trabalhadores, gravação em CSV a cada quadro. Ordem: (1) diff do
censo por ID; (2) extração de todos os tokens de ATS do repositório e cruzamento com o censo; (3)
listagem integral dos quadros fora do censo; (4) índice global do Workable; (5) quadros conhecidos
de Teamtailor, Recruitee, Personio e Pinpoint ainda não listados; (6) planilha da comunidade;
(7) skillshot.pl; (8) leitura do **corpo integral** de cada finalista pela API, com a régua e a
frase transcrita; (9) `dedupe-agora.sh` por ID mais conferência no **Gmail por janela de tempo**;
(10) conferência final: a URL pública da vaga da fila devolveu **HTTP 200**.

**Grupo Disney não foi tocado nesta rodada de propósito:** o maestro já o mediu às 10h18 com
`ronda-disney.sh`, 12 de 12 consultas responderam e deu zero ID novo. Repetir seria queimar rodada.

Arquivos escritos por esta rodada: **este**, a entrada nº 51 da `automacao/FILA-DO-VINI.md` e uma
linha em `automacao/processados.csv`. `enviados.csv` e `docs/index.html` **não foram tocados**.
