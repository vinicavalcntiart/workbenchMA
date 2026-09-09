# Próxima rodada: duas candidaturas de Workday prontas para clicar

> **ATUALIZADO às 10h UTC de 09/09: a nº 7, ILM Vancouver `10142674`, JÁ FOI ENVIADA E CONFIRMADA.**
> Ela não esperou a virada da rodada porque o Vini mandou, por escrito, ser o primeiro em qualquer
> vaga de arte do grupo Disney. A regra de uma por casa por rodada cedeu para a ordem dele.
> Sobram sete, todas da Netflix ou da Eyeline.

Escrito em 09/09/2026, depois da madrugada que enviou treze candidaturas. **Nenhuma destas oito
está enviada**, e o motivo não é técnica: é a regra da campanha de **uma mensagem por casa por
rodada**. As quatro casas abaixo já receberam uma candidatura em 09/09, então estas ficam para a
rodada seguinte.

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
| 2 | **Lead Surfacing Artist** `JR40928` | Eyeline, Seul | `netflix.wd108.myworkdayjobs.com` | `Eyeline` | `Eyeline-Seoul/Lead-Surfacing-Artist_JR40928` | não publicada |
| ~~3~~ | ~~**Environment Modeling Supervisor** `JR39446`~~ | ~~Netflix Animation, Vancouver~~ | **ENVIADA em 09/09** | | | ~~CAD 167k–212k~~ |
| ~~4~~ | ~~**Environment Surfacing Supervisor** `JR39273`~~ | ~~Netflix Animation, Vancouver~~ | **ENVIADA em 09/09** | | | ~~CAD 163k–223k~~ |
| ~~5~~ | ~~**Environment Modeling Supervisor** `JR41734`~~ | ~~Netflix Animation, Sydney~~ | **ENVIADA em 09/09** | | | |
| 6 | **Environment Surfacing Supervisor** `JR41749` | Netflix Animation, Sydney | `netflix.wd108.myworkdayjobs.com` | `Netflix` | `Sydney/Environment-Surfacing-Supervisor_JR41749` | não publicada |
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
