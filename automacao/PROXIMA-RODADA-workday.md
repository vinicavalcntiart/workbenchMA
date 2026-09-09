# Fila do Workday: ZERADA DE VERDADE em 09/09 — as OITO saíram

> **Correção das 20h30.** Este arquivo continuava listando a nº 2 (Eyeline `JR40928`) e a nº 6
> (Netflix Sydney `JR41749`) como esperando a próxima rodada. **As duas já tinham sido enviadas
> e confirmadas horas antes**, com prova de `jobTasks/completed/application`. Fui disparar a nº 2
> e o dedupe na hora do clique pegou.
>
> **É a terceira fila desatualizada em uma hora**, junto com a preparação da Imageworks e as três
> da Ubisoft. O padrão é sempre o mesmo: **arquivo de fila escrito de manhã envelhece em horas,
> porque outra rodada envia a partir dele e não volta para riscar a linha.** A defesa que
> funcionou nas três vezes é a mesma e é barata: **refazer o dedupe contra `enviados.csv` e
> `processados.csv` no minuto do disparo**, nunca contra a fila.

> As oito saíram todas, ou foram recusadas com motivo escrito. Nada aqui espera a mão dele.

> **ATUALIZADO às 10h UTC de 09/09: a nº 7, ILM Vancouver `10142674`, JÁ FOI ENVIADA E CONFIRMADA.**
> Ela não esperou a virada da rodada porque o Vini mandou, por escrito, ser o primeiro em qualquer
> vaga de arte do grupo Disney. A regra de uma por casa por rodada cedeu para a ordem dele.
> Sobram sete, todas da Netflix ou da Eyeline.

Escrito em 09/09/2026, depois da madrugada que enviou treze candidaturas. **O texto original dizia
que nenhuma das oito estava enviada**, e isso era verdade na hora em que foi escrito: o que segurava
todas era a regra da campanha de **uma mensagem por casa por rodada**. Ao longo do dia as oito foram
resolvidas uma a uma — sete enviadas e uma recusada com motivo escrito —, e a tabela abaixo é a que
vale. **O parágrafo antigo fica riscado aqui como lembrete de que fila envelhece.**

Todas foram reconferidas em 09/09 por um agente: detalhe da API **200**, página pública **200**,
régua rodada de novo sobre o texto integral e **dedupe por ID de requisição 0/0/0/0** nos quatro
arquivos (`docs/index.html`, `enviados.csv`, `automacao/processados.csv`,
`automacao/FILA-DO-VINI.md`).

## Como disparar cada uma

O fluxo genérico está em `/home/user/apply/wd_geral.js` e já resolve as armadilhas de Workday
listadas no briefing. O comando é sempre este, trocando os quatro últimos argumentos:

```
cd /home/user/apply
VINI_TEL="<telefone, do doc privado>" VINI_RUA="<rua>" VINI_CEP="<cep>" \
VINI_SAL="<pretensão>" \
sh hb_run.sh wd_geral.js <host> <site> <jobpath> <apelido> [ENVIAR]
```

Sem o `ENVIAR` no fim ele **para na Review** e não envia. Rode primeiro sem, leia a Review, e só
então repita com `ENVIAR`. A conferência final do próprio script **recusa enviar** se a Review
mostrar mestrado concluído (é falso, o dele está em andamento) ou autorização legal respondida
como "sim".

## A fila, na ordem de quanto encosta no centro do portfólio

| # | Vaga | Casa (já usada em 09/09) | host | site | jobpath | Faixa |
|---|---|---|---|---|---|---|
| ~~1~~ | ~~**Modeling Supervisor** `JR40941`~~ | ~~Eyeline, Seul~~ | **ENVIADA em 09/09** | | | |
| ~~2~~ | ~~**Lead Surfacing Artist** `JR40928`~~ | ~~Eyeline, Seul~~ | **ENVIADA em 09/09, três provas incluindo `jobTasks/completed/application`** | | | |
| ~~3~~ | ~~**Environment Modeling Supervisor** `JR39446`~~ | ~~Netflix Animation, Vancouver~~ | **ENVIADA em 09/09** | | | ~~CAD 167k–212k~~ |
| ~~4~~ | ~~**Environment Surfacing Supervisor** `JR39273`~~ | ~~Netflix Animation, Vancouver~~ | **ENVIADA em 09/09** | | | ~~CAD 163k–223k~~ |
| ~~5~~ | ~~**Environment Modeling Supervisor** `JR41734`~~ | ~~Netflix Animation, Sydney~~ | **ENVIADA em 09/09** | | | |
| ~~6~~ | ~~**Environment Surfacing Supervisor** `JR41749`~~ | ~~Netflix Animation, Sydney~~ | **ENVIADA em 09/09, três provas** | | | |
| ~~7~~ | ~~**Lead Generalist Artist** `10142674`~~ | ~~Disney / ILM Vancouver~~ | **ENVIADA em 09/09, Application Received** | | | ~~CAD 126.800–162.300~~ |
| ~~8~~ | ~~**Visual Development Artist, Ink** `JR41753`~~ | ~~Netflix, LA~~ | **RECUSADA em 09/09 com motivo escrito: é desenho e pintura 2D** | | | |

**Pretensão a usar em cada uma.** Faixa publicada, pede-se a BASE: nº 3 → `CAD 167,000`;
nº 4 → `CAD 163,000`; nº 7 → `CAD 126,800`. Sem faixa, casa grande: `CAD 95,000` para as do
Canadá, `AUD 110,000` para as de Sydney, e para Seul use `Open to aligning with your band for the
role.` sem número, que foi o que passou na Eyeline em 09/09. Sempre com a frase de alinhamento.

## Ressalvas honestas, uma por linha

- **nº 1 e nº 2 (Eyeline Seul):** são VFX fotorrealista, e o centro do portfólio dele é estilizado.
  A nº 2 tem trabalho de **criatura hero** escrito no corpo, o que puxa a favor.
- **nº 3 a nº 6 (Netflix Animation):** são **ambiente**, não personagem, mas com supervisão, e a
  casa é animação, que é onde está o crédito do Wingfeather. As duas de Vancouver pagam mais.
- **nº 7 (ILM Vancouver): ENVIADA em 09/09 às 10h UTC**, requisição `10142674`, status
  **Application Received**. A ressalva original continua valendo e foi mandada assim mesmo: é
  generalista de ambiente e parte do trabalho é digital matte painting, que é pintura e não
  modelagem. A régua de vinte termos deu **zero** veto. Ela saiu na frente porque o Vini disse com
  todas as letras que vaga de arte do grupo Disney a gente aplica primeiro, e ordem dele vale mais
  que regra interna de cadência.
- **nº 8 (Ink): RECUSADA em 09/09, com o anúncio integral lido.** A régua deu zero e não há veto
  nenhum, mas as Qualifications pedem *"Excellence in draftsmanship with a working knowledge of
  anatomy and/or volumetric drawing"*, *"Advanced working knowledge of digital drawing tools"* e
  *"Demonstrated and genuine interest in Generative AI imagery and video"*. Maya, Unreal e Blender
  aparecem só como *"a significant plus"*: o 3D é o acessório e o desenho é o cargo. O portfólio
  dele é escultura e modelagem. Netflix Los Angeles não tinha recebido nada hoje, então a cadência
  não era o impedimento, a disciplina é.

## O que NÃO entra e por quê

- `10153285` Real-Time Environment Artist, ILM São Francisco: recusada de propósito em 07/09, com
  razão escrita, e a releitura de 09/09 manteve os dois motivos originais.
- `10052606` Sr Generalist Artist, ILM Vancouver: título passa, corpo reprova. *"As a Digital Matte
  Painter, you will (…) craft digital matte paintings"*, requisito é Photoshop e Nuke, ZBrush é
  "a plus". É pintura, não modelagem.
- ILM Mumbai (`10154147` Sr Character Modeler, `10155895` Lead Modeler, `10146393` Lead Environment
  Artist): são os três alvos mais centrais que apareceram em 642 vagas e **morrem no escopo**.
  Índia está fora, e isso não se contorna.

---

# ~~PRIMEIRO ENVIO DE 10/09~~ — **CANCELADO ÀS 20h20 DE 09/09. NÃO DISPARE ESTE COMANDO.**

> **A `4363749003` JÁ FOI ENVIADA DUAS VEZES: em 02/09 às 13h20 e de novo em 07/09 às 05h59.**
> A segunda já está registrada em `processados.csv` como `REPETIDA-ERRO-MEU`. Disparar o comando
> abaixo faria o estúdio receber a **mesma requisição pela terceira vez**.
>
> **Como o erro passou:** eu escrevi esta seção depois de um ensaio limpo, e a nota de "preparada e
> conferida" tem a minha própria letra — então ela passa direto pela desconfiança na hora do
> disparo. O dedupe que eu fiz foi da vaga contra a *fila*, não do ID contra o *arquivo*.
> **A regra que fica: o dedupe se refaz NA HORA DO DISPARO, contra `processados.csv` e
> `enviados.csv`, nunca contra a anotação de ontem — inclusive quando a anotação é minha.**
>
> **A casa inteira está esgotada**, conferido no mesmo minuto: Modeler `4363748003` enviada,
> Texture Artist `4363798003` enviada, Experienced Texture Artist `4363799003` enviada depois do
> bloqueio de reCAPTCHA de 04/09, Look Development `6659179003` enviada, Expression of Interest
> `4551278003` enviada em 02/09. **Não sobra requisição na Imageworks.**
>
> O texto abaixo fica de pé só como registro do que tinha sido preparado.

**Sony Pictures Imageworks — Experienced Modeler — Vancouver, BC, Canadá**
`https://job-boards.greenhouse.io/embed/job_app?for=sonypicturesimageworks&token=4363749003`

Requisição `4363749003`, internal `4243531003`. **Régua de vinte termos: ZERO acertos.** Nenhum
veto escrito, nenhuma exigência de francês (o anúncio diz *"Language in work environment -
English"*). *Project based, Full Time*, que conta normalmente em casa grande pela regra de formato.

**Por que esta e não as outras cinco da mesma casa:** o anúncio diz, com todas as letras,
*"Prepares and builds models for characters and stand-ins for layout"*. É modelagem de
PERSONAGEM, o centro dele, no CANADÁ, que é a prioridade um. As outras: Modeler `4363748003` e
Texture Artist `4363798003` já foram enviadas; Look Development `6659179003` pede 3 a 5 anos, que
é abaixo do nível dele; as duas de Character FX são CFX, disciplina que ele não tem.

**A casa está travada hoje só por cadência:** a Environment Artist saiu de manhã, com recibo do
`no-reply@imageworks.com` às 11h24.

## O comando, um só

```
cd /home/user/apply && VINI_TEL='<só os dígitos, do doc privado do Drive>' \
  sh hb_run.sh apply_gh.js \
  "https://job-boards.greenhouse.io/embed/job_app?for=sonypicturesimageworks&token=4363749003" \
  spimod ans_spi_modeler.json --submit
```

Depois do clique, o Greenhouse manda **código de segurança por email**. Ordem obrigatória, já
paga duas vezes nesta campanha: rode o envio EM SEGUNDO PLANO, espere o marcador
`EMAIL CODE REQUIRED`, e SÓ ENTÃO leia o código mais novo no Gmail e escreva `code_spimod.txt`.
Cada clique em Submit gera código novo e invalida o anterior.

## As respostas já estão decididas e conferidas em ensaio, com as listas reais do formulário

| Campo | Resposta | Por quê |
|---|---|---|
| `Where do you currently reside` | **I live outside of CAN** | verdade |
| `Eligibility to work in Canada` | **I will need a work permit** | verdade, ele precisa de patrocínio |
| `How do hear about us?` | **Imageworks Career Site** | verdade: a vaga saiu da varredura do quadro do próprio estúdio, não do LinkedIn |
| `Worked at Imageworks before` | No | verdade |
| `Employed by SPE or Sony Affiliates` | No | verdade |
| `When are you available` | Within 30 days of an offer | não revela prazo de contrato |
| `Voluntary Disclosures` | Yes, I have read and consent to the terms and conditions | única opção |

O ensaio de 19h50 fechou com `pre-submit invalid: []`, ou seja nenhum campo obrigatório vazio.

**ATENÇÃO NO ENSAIO DE 19h50:** um dos ensaios foi rodado com o telefone DIGITADO ERRADO por
mim (um dígito final trocado). Não houve envio, era ensaio. **Amanhã copie o número do documento
privado do Drive, não de memória.**
