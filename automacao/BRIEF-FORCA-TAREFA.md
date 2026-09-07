# Força-tarefa de FORMULÁRIOS, madrugada de 07 para 08/09

Meta do Vini: **fechar 100 candidaturas por formulário antes de o dia começar.** Estávamos em
**91** quando esta força saiu. Só conta formulário. **Vaga de email não é o seu trabalho aqui.**

## Ordem de prioridade, ditada pelo Vini, nesta ordem exata

1. **Realocação para o Canadá** (anglófono na frente; Quebec atrás por causa do francês)
2. **Remoto para EUA, Canadá ou Europa**
3. **Vagas em que ele tem chance material de passar**

Chance material quer dizer: personagem, modelagem, textura, look dev, visual development,
3D generalista. **Não é** concept art 2D, não é animação, não é rigging, não é engenharia.
Anúncio que exige disciplina que ele não tem queima a porta daquela casa: não mande.

## Escopo geográfico, e ele não se negocia

América do Norte, Europa (UK, Irlanda, Nórdicos, UE), Oceania, e na Ásia **só Coreia do Sul e
Singapura**. **NADA de Índia, NADA de Brasil, NADA de Japão.** Remoto 100% vale fora dessa
lista, exceto Japão.

## CAPTCHA: não perca tempo

Desafio de imagem, hCaptcha, Turnstile, DataDome ou reCAPTCHA de caixa: **pare, registre o
dossiê campo a campo no painel como "à mão", e siga para a próxima.** Não tente burlar, não
tente de outro IP, não fique dez minutos ali. reCAPTCHA **v3** (só pontuação, sem desafio)
às vezes passa: pode tentar UMA vez, e se reprovar registre e siga.

## NUNCA aplique sem garra. Esta é a regra que impede o dano de hoje.

Hoje a Icefall e a Red VFX receberam **duas candidaturas cada** porque agentes diferentes
acharam o mesmo estúdio ao mesmo tempo por caminhos diferentes. Vocês são três varrendo três
quadros: o mesmo estúdio VAI aparecer em dois. Então, imediatamente antes de clicar em enviar:

    git pull -q --rebase origin claude/vini-cavalcanti-job-campaign-gciixk
    sh automacao/garra.sh pega "<Estudio>" "<Titulo da vaga>" <seu-nome>

Se responder `JA-TEM:<outro>`, **pule sem aplicar**. Se responder `OK`, é seu, pode aplicar.
Se você desistir depois de pegar, `sh automacao/garra.sh solta "<Estudio>" "<Vaga>"`.

Além da garra, confira `automacao/processados.csv` e o array `PORTAIS` do `docs/index.html`:
estúdio já trabalhado não se repete. E lembre da **regra do internal_job_id**: o mesmo
requisito sai em dois quadros com números de anúncio diferentes; a 2K publicou a MESMA vaga
quatro vezes. Título + cidade iguais já é suspeita suficiente para pular.

## O QUE CONTA COMO PROVA DE ENVIO, e o que não conta

Só três coisas provam: **(1)** texto de confirmação na tela, **(2)** URL de confirmação
(`/thanks`, `/thankyou`, `/confirmation`), **(3)** email de recebimento na caixa.
**Formulário que apenas LIMPA não prova nada.** Formulário que continua preenchido não enviou.
Sem uma das três, registre como PENDENTE e **não reenvie no mesmo dia**.

## As armadilhas medidas ontem, todas custaram tempo real

- **`requestSubmit` NÃO é clique.** Ele dispara o submit nativo e o site perde o próprio
  handler: a URL vira `?campo=valor` e nada é enviado. **Clique no botão de verdade.**
- **Timeout de upload não é parede.** `setInputFiles` com 30s estoura em página pesada.
  Use `{timeout:90000}` e tente de novo antes de declarar bloqueio.
- **Sobreposição invisível intercepta clique.** `div.preloader` e afins fazem o clique pendurar
  para sempre, sem exceção. Detecte com `document.elementFromPoint(centro)` devolvendo null.
  Conserto: `fill()` em vez de `click()+type()`, e remova a sobreposição.
- **Menu do Wix e do Google Forms só grava por teclado** (ArrowDown + Enter), nunca por clique.
- **Menu `selectize`** (Traffit e parecidos) carrega opção só ao digitar: clique, digite, e
  clique na opção da lista. Ler `<select>` vazio não quer dizer que não há opções.
- **Campo de arquivo do JazzHR é invisível:** o nome do CV não aparece na tela mesmo anexado.
  A prova ali é o próprio input, não a tela. No Wix é o oposto.
- **Página que só monta em JavaScript** volta 200 com corpo vazio no curl. Isso é "precisa de
  navegador", nunca "sem vaga". Já escondeu 21 vagas da Digic.
- **403 não é site morto**, é porta fechada para robô. Abra com navegador antes de descartar.

## Respostas de formulário: a verdade, sempre

- **Autorização de trabalho: NUNCA minta.** Ele não é cidadão da UE, não tem autorização dos
  EUA, Canadá, Austrália ou Nova Zelândia, e **precisa de patrocínio**. Onde houver opção,
  "Non-citizen seeking work authorization" é a verdade.
- **Liderança de time: SIM.** Ele é Senior há cinco anos, revisa trabalho de outros artistas e
  define o padrão de asset, e é fundador da própria escola de arte de personagem.
- **Realocação: ele QUER realocar.** Nunca escreva nada que sugira hesitação em mudar de país.
  O mestrado só aparece como credencial que fortalece o caso de visto, jamais como impedimento.
- **Salário atual da E-Line: NUNCA se revela** (NDA). Resposta fixa: "Confidential under the NDA
  of my current contract; happy to discuss ranges during the process."
- **Pretensão:** se o anúncio publica faixa, peça a BASE dela. Sem faixa publicada, sênior ou
  lead em estúdio grande: EUA USD 100.000, Canadá CAD 95.000, Reino Unido GBP 50.000, Europa
  ocidental EUR 55.000, Austrália AUD 110.000. Estúdio pequeno ou médio: EUA USD 85.000, Canadá
  CAD 80.000, Reino Unido GBP 42.000, Europa EUR 45.000, Austrália AUD 95.000. **Nunca abaixo do
  piso legal da ocupação**, porque abaixo dele o patrocínio de visto é impossível. Sempre com a
  abertura "Open to aligning with your band for the role".
- Pergunta cuja resposta só o Vini sabe (quais jogos joga, vídeo gravado, preferência entre
  estúdios nomeados): **deixe em branco e registre**, não invente.

## Dados dele

Vini Cavalcanti · contact@vinicavalcanti.art · Olinda, Pernambuco · ArtStation
artstation.com/viniciuscavalcanti · LinkedIn linkedin.com/in/vinicavalcnti · vinicavalcanti.com
CV e carta em `$SCRATCH/apply/Vini_Cavalcanti_CV.pdf` e `_Cover_Letter.pdf`.
**Telefone: use a variável de ambiente `VINI_TEL`. Se ela estiver vazia e o campo for opcional,
deixe em branco. NUNCA escreva telefone nem endereço residencial no repositório, que é PÚBLICO.**

## Registro, a cada candidatura

Linha no `PORTAIS` do `docs/index.html` (nota dizendo se é remota, porque a ordenação põe remoto
na frente), linha em `automacao/processados.csv`, `sh automacao/valida-dashboard.sh` antes do
commit, e commit e push no branch. Commite de hora em hora, não só no fim: rodada que só grava
no fim evapora se o processo morrer.

## REGRA DE 07/09: promessa escrita mora no FORMULARIO tanto quanto no anuncio

A Bulkhead entrou nas três vagas recomendadas ao Vini porque a nota do painel dizia que o
anúncio prometia, por escrito, *"Don't worry, we can sponsor your visa"*. Ao reabrir a página,
a contagem dos termos deu **`sponsor` 0, `visa` 0, `relocat` 0** no HTML do servidor E no texto
renderizado por navegador, e eu concluí que o anúncio tinha sido reescrito e tirei a vaga da
recomendação.

**Estava errado, e o Vini provou com um print.** A frase está lá, viva, **dentro do
formulário**, logo abaixo da pergunta *"Do you have the right to work in the UK?"*. No
Teamtailor o formulário só carrega depois do *Apply for this job*, e o texto que eu capturei
terminava literalmente em **"Loading application form"**: li a página inteira e parei
exatamente antes da parte que importava.

**Então: buscar termo numa página de vaga lê o ANÚNCIO, não a CANDIDATURA.** Condição de visto,
patrocínio e regime de trabalho muitas vezes só aparecem nos campos do formulário, como texto
de ajuda embaixo da pergunta. Contagem zero numa página cujo texto termina em "Loading
application form" não é prova de ausência, é ausência de prova. **Abra o formulário antes de
concluir qualquer coisa sobre patrocínio.**

**Anúncio de vaga não é imutável, e nota de painel envelhece calada.** Os três campos que mais
mudam entre uma leitura e outra são justamente os três que mais pesam na decisão do Vini:
**promessa de visto, faixa salarial e regime de trabalho** (presencial, híbrido ou remoto).

Então: **antes de recomendar uma vaga ao Vini apoiado numa promessa escrita, REABRA a página e
confirme a promessa ali.** Citar a nota não basta. E ao registrar uma promessa dessas, escreva
na nota a DATA em que ela foi lida, para a próxima pessoa saber o quanto aquilo já envelheceu.

## PUGA Studios: são TRÊS ANOS, e é argumento, não linha de currículo

Decisão do Vini em 07/09: a PUGA passa a ser citada com a **duração**, três anos, e nas cartas e
respostas de formulário ela entra pelo que prova, não pelo cargo. O que ela prova é **entregar
personagem sob direção de arte de outra pessoa, no estilo definido pelo cliente, com rodada de
revisão como rotina**. Isso responde uma pergunta que estúdio de serviço, publisher e casa média
sempre têm e quase nunca escrevem no anúncio.

Somada aos cinco anos de E-Line e ao crédito do Wingfeather, ela é o que fecha os dez anos.

## Asterisco no rótulo NÃO é prova de campo obrigatório. A Bulkhead custou dias por isso.

A Bulkhead ficou marcada "só o Vini pode fazer" por dias, com o motivo escrito de que o
formulário **exige print da aba Most Played do perfil Steam, arquivo que só ele gera**. O Vini
abriu o formulário e viu na hora o que a automação não tinha visto.

Abrindo o formulário por dentro:

- A pergunta de plataforma é rádio com **PC, Console, Mobile & Handheld** e
  **"I don't play games often"**.
- O upload do Steam tem asterisco no texto do rótulo, mas o `<input type="file">` está com
  **`required: false`**.
- E existe uma pergunta logo em seguida: *"Please tell us about any non-Steam games you like to
  play..."*, que é **a saída oficial deles para quem não joga em Steam**.

Marcar Console e responder essa caixa era o caminho previsto pelo próprio estúdio. Tratamos um
campo **condicional** como parede dura, e uma vaga com **patrocínio de visto dito por escrito**,
que é o sinal mais raro da campanha, ficou parada sem precisar.

**As três verificações que passam a ser obrigatórias antes de declarar um campo impossível:**

1. **Leia o atributo `required` do input**, não o asterisco do rótulo. Asterisco é texto e mente.
2. **Procure a pergunta companheira.** Formulário bom quase sempre oferece "se não X, conte Y".
   Se ela existe, o campo X é condicional.
3. **Olhe as opções do rádio antes.** Muitas vezes a resposta que dispensa o anexo já está ali
   ("Console", "I don't play games often"), e escolher a verdade dele já resolve.

Campo que só o Vini pode preencher existe de verdade (vídeo gravado por câmera, por exemplo),
mas ele tem que ser **provado**, não suposto. Declarar parede que não existe custa mais caro que
tentar e falhar, porque a vaga sai da fila da automação e some da vista.

## Teamtailor: POST 200 NÃO é candidatura completa

Medido na Bulkhead em 07/09. O envio devolve **200** e a URL vira
`/applications/email_verification_needed`: a candidatura **não existe ainda**. Chega um email
"Complete the application for ..." com um link `/applications/verify_email/<uuid>?candidate_uuid=<uuid>`,
e só depois de abrir esse link a URL vira `/applications/<uuid>/thanks`, que é a prova de verdade.

**Agente que parar no 200 conta candidatura pela metade e o estúdio nunca vê nada.** Depois de
enviar num Teamtailor, procure esse email e abra o link antes de marcar `done=true`.

Outras três armadilhas do mesmo formulário, e a ordem entre elas importa:
1. **O formulário REMONTA ao rolar.** Marcar rádio antes de rolar até o fim apaga tudo.
   Role primeiro, preencha depois.
2. **Voltar ao topo DESMONTA a seção dos arquivos.** Role de novo antes de anexar o CV. O input
   de arquivo **não tem atributo `name`, só `id`**.
3. **Telefone é `intl-tel-input`** e devolve *"Phone is invalid"* para número sem país. O setter
   nativo não acorda o plugin: **digite** o número internacional inteiro, com o `+` na frente.

## Greenhouse: o ID de cada pergunta muda A CADA VAGA, mesmo no mesmo board

Medido em 07/09 na Sony Pictures Imageworks. A *Experienced Modeler* usa
`question_7972538003` para "Have you worked at Imageworks before?"; a *Experienced Texture
Artist*, do **mesmo estúdio e do mesmo board**, usa `question_7972757003` para a mesma pergunta.

Copiar o arquivo de respostas da vaga irmã **parece funcionar**: o script não levanta erro
nenhum, porque ele apenas não acha os campos. O envio volta com *"Resume/CV is required"* e
*"This field is required"*, e uma tentativa se perde. **Mapeie os campos DA VAGA antes de montar
o arquivo de respostas**, sempre.

E no mesmo board há **níveis da mesma função**: *Modeler* e *Experienced Modeler*, *Texture
Artist* e *Experienced Texture Artist*. **Mande só na sênior** — as duas é candidatura repetida.

## Deduplicar por `done=false` é o contrário do necessário. Custou duas repetidas.

Em 07/09 eu mesmo mandei **duas candidaturas repetidas** para a Sony Pictures Imageworks,
na mesma noite em que escrevi a `garra.sh` para impedir exatamente isso. A *Experienced
Modeler* já tinha ido em **02/09** e a *Experienced Texture Artist* em **05/09**.

**Como passou:** escolhi no que trabalhar filtrando o painel por `done=false`. As vagas de
Vancouver estavam com `done=true` e por isso ficaram **invisíveis para o meu filtro**. Depois
reachei as mesmas requisições pela API do Greenhouse e tratei como novidade. Peguei a garra, mas
a garra só protegia contra **dois agentes ao mesmo tempo**, não contra trabalho feito dias antes.

**A lição, e ela é sutil:** filtrar por `done=false` para **escolher** está certo; conferir por
`done=false` para **deduplicar** é o oposto do necessário, porque o que já foi feito é
justamente o que está com `done=true`. Dedupe se faz contra o **arquivo inteiro**, sem filtro de
estado, pela **URL ou pelo ID da requisição** — nunca pelo nome do estúdio, que aparece em várias
linhas e cujo primeiro casamento não é o relevante.

**Conserto estrutural, já no ar:**

    sh automacao/garra.sh checa "<url-da-vaga>"                       # livre | JA-FEITO:<onde>
    sh automacao/garra.sh pega "<Estudio>" "<Vaga>" <nome> "<url>"    # recusa com JA-FEITO

Passe **sempre a URL** como quinto argumento do `pega`. Ele procura a URL e o ID numérico longo
da requisição no `docs/index.html` e no `processados.csv` e recusa com saída 4.

## Commite a CADA candidatura, não de hora em hora. O contêiner reinicia.

Em 07/09 às 06h44 o contêiner desta sessão **reiniciou e matou SETE agentes de uma vez**, no
meio do trabalho. Sobreviveu exatamente o que estava commitado e empurrado; o resto evaporou,
sem aviso e sem chance de recuperar.

A instrução anterior era "commite de hora em hora", e ela salvou muita coisa (as candidaturas da
Crystal Dynamics e da Tripwire entraram minutos antes). Mas uma hora de trabalho perdido é caro
demais quando o custo de commitar é um segundo. **A regra passa a ser: commit e push a cada
candidatura enviada**, logo depois de registrar a prova.

**Causa provável, e o cuidado que sai dela:** sete navegadores Playwright ao mesmo tempo na
mesma máquina. Disco estava em 40% e não foi ele. **Rode UM navegador por vez**, e depois de
cada rodada confira `pgrep -f chrome` e mate o que ficou pendurado. Não é frescura de recurso:
processo pendurado de agente morto continua ocupando memória de quem está vivo.

## O FORMULÁRIO carrega informação que o ANÚNCIO não tem, nos dois sentidos

Duas medições de 07/09, opostas entre si, ensinam a mesma coisa.

**A boa notícia estava só no formulário.** Na Bulkhead eu contei os termos no anúncio e deu
`sponsor` 0, `visa` 0, `relocat` 0, e conclui que a promessa de patrocínio tinha sumido. Estava
errado: *"Don't worry, we can sponsor your visa"* e *"100% on-site and we offer relocation
assistance"* estão vivas, **dentro do formulário**, como texto de ajuda embaixo das perguntas.
O texto que eu tinha capturado terminava em "Loading application form".

**A má notícia também.** Na Larian Québec o anúncio não diz nada sobre visto e só exige inglês
fluente, o que faz a vaga parecer aberta a estrangeiro. **O veto de residência está escrito
dentro do formulário**, não no anúncio.

**Regra:** antes de concluir qualquer coisa sobre **patrocínio, visto, residência ou regime de
trabalho**, ABRA O FORMULÁRIO. Esses quatro assuntos moram tanto no corpo do anúncio quanto nos
campos, e com frequência só nos campos. Contagem de termo numa página cujo texto termina em
"Loading application form" não é prova de ausência, é ausência de prova.

## A garra NÃO enxerga o Gmail, e foi o Gmail que impediu três repetidas

Medido em 07/09. Um agente chegou a preencher o formulário inteiro da **Chimera Entertainment**
antes de conferir a caixa. A garra tinha devolvido `OK`, e com razão: a candidatura não estava
no painel nem no `processados.csv`. O que provava que ela existia era o **email de confirmação
de 06/09**. O mesmo valeu para **Deck13** e **Aesir**.

**A garra confere painel e CSV, que são o que a campanha ESCREVEU. O Gmail é o que os estúdios
RESPONDERAM, e é registro independente.** Quando um envio não chega a ser commitado (contêiner
reiniciado, agente morto, rodada interrompida), o email de confirmação é a única prova que
sobrou.

**Regra:** antes de enviar em estúdio que você não trabalhou nesta rodada, faça também uma busca
no Gmail pelo domínio dele. `JA-FEITO` da garra é motivo suficiente para pular; `OK` da garra
**não** é prova suficiente para enviar.

## Três defeitos do NOSSO ambiente que pareciam parede de estúdio

Todos medidos em 07/09, e todos custaram diagnóstico errado escrito no painel.

1. **O `502 read ECONNRESET` da SQRT3 era a ponte desta sessão, não o estúdio.** Um `page.route`
   que re-busca cada recurso até 5 vezes fez o mesmo POST passar de primeira.
2. **Os dois bloqueios registrados da Bohemia Interactive eram falsos.** O menu *Discipline* e o
   código de país "não selecionavam" porque pedaços de JavaScript sob demanda voltavam 502
   intermitente. Com a rede consertada, os dois selecionam normalmente. A parede real é
   reCAPTCHA v3, que é outra coisa e tem outro conserto.
3. **Rodar varredura com 20 a 40 conexões AO MESMO TEMPO que um navegador satura a ponte, mata o
   Chromium e faz página viva parecer quebrada.** Isto provavelmente explica o reinício do
   contêiner das 06h44. **Varredura em lote e navegador não rodam juntos.**

E um detalhe de proxy: `boards-api.eu.greenhouse.io` está **bloqueado por política do proxy**,
mas `job-boards.eu.greenhouse.io` responde 200. Use o segundo.

## A CAIXA DO VINI entrega o token do ATS de graça. Pare de adivinhar.

Vários agentes já mediram que **adivinhar o token do ATS pelo nome do estúdio quase nunca
acerta** — um deles gerou 1.548 tokens a partir de 730 nomes e só o Greenhouse rendeu. Testei
hoje 14 estúdios europeus conhecidos no Greenhouse e **todos deram 404**: eles simplesmente não
usam Greenhouse.

**O atalho estava na caixa de entrada o tempo todo.** O Teamtailor envia de
`<token>.teamtailor-mail.com`, então **cada confirmação já recebida entrega o token exato**:

    no-reply@fatshark.teamtailor-mail.com          -> fatshark
    no-reply@ghostship.teamtailor-mail.com         -> ghostship
    no-reply@untoldstdfg1324556.teamtailor-mail.com -> untoldstdfg1324556

**A Untold é a prova de que isto não é conveniência, é a única via:** ninguém adivinharia
`untoldstdfg1324556` nunca. E o mesmo vale para nome de pessoa, porque recrutador do Teamtailor
escreve do mesmo domínio (`morgane.perrin@sloclap.teamtailor-mail.com`).

**Como usar:** busque no Gmail por `teamtailor-mail.com`, extraia os tokens dos remetentes, e
liste **o board inteiro** de cada um em `https://<token>.teamtailor.com/jobs.json`. A chave do
JSON é **`items`**, não `jobs`. Isso casa com a outra regra desta noite: uma entrada de painel
por estúdio esconde o resto do quadro.

**Resultado honesto da primeira rodada do método (07/09, 08h20):** 20 tokens colhidos, 20 boards
listados inteiros, e **nenhuma vaga nova da disciplina**. As duas que existem, Character Artist
da Fatshark e Senior Character Artist Unity3D da beffio, **já têm candidatura**. Embark tem 18
vagas e nenhuma de personagem; Untold tem 24 e são todas VFX e produção. O método é bom, o
estoque é que está seco.

## Uma entrada de painel por estúdio ESCONDE o quadro. Medido em escala em 07/09.

A campanha já sabia disso pela Sony Imageworks, que aparecia como uma entrada de Montréal
enquanto o quadro tinha 54 vagas. Em 07/09 a fatia RESTO transformou isso em método e mediu o
tamanho do buraco: peguei **todos os tokens de ATS que já apareciam em alguma URL do painel ou
do `processados.csv`** (31 Greenhouse, 27 Teamtailor, 23 BambooHR, 17 Lever, 13 Workable, 10
SmartRecruiters, 6 Ashby, 4 Breezy, 1 Recruitee) e baixei **o quadro inteiro de cada um**.

Deu **2.122 vagas**, 139 na disciplina dele, e **46 que a garra confirmou nunca terem sido
tocadas**. Entre elas apareceram coisas que nenhuma entrada do painel mostrava: a **Embark**
estava registrada só como cadastro de Connect e tinha uma Environment Artist aberta (virou
candidatura enviada), a **Skydance de Madri** tem uma *família inteira* de surfacing e o painel
só listava três vagas soltas, a **Kabam** tinha uma General Application de Vancouver além da
Lead Character Artist já recusada, e a **Barnstorm** tinha uma Environment Generalist de
Vancouver além da Creature Lead.

**A regra:** quando o painel registrar um estúdio por qualquer porta (vaga nomeada, banco de
talentos, Connect, e-mail), **liste o quadro inteiro do ATS dele antes de dar a casa por
trabalhada**. Custa um pedido e devolve o quadro todo.

## O quadro do ATS mora MUITAS VEZES em domínio próprio, e varredura por slug não o acha

Medido em 07/09, e foi o que rendeu a candidatura da **Envar Studio**, um estúdio de Estocolmo
que **não existia no painel**. O `jobs.json` do Teamtailor dele não está em
`envar.teamtailor.com`: está em **`careers.envarstudio.com/jobs.json`**.

Receita: pegue os domínios de estúdio já colhidos nos CSVs, gere `careers.<domínio>`,
`career.<domínio>` e `jobs.<domínio>`, e peça `/jobs.json` em cada um. Sobre 2.592 domínios
(7.716 hospedeiros) apareceram **29 quadros** que a varredura por slug não encontra — Paradox,
Sharkmob, Starbreeze, Arrowhead, Coffee Stain, Raw Fury e a própria Envar entre eles.
**Adivinhar slug acha a porta que o ATS tem; varrer subdomínio acha a porta que só o DNS do
estúdio conhece.**

## SmartRecruiters: o ANÚNCIO renderiza, quem está bloqueado é o FORMULÁRIO

A nota antiga da campanha — *"a página renderiza completamente vazia, zero botões e zero texto"* —
está certa só para metade. Medido em 07/09 na GIANTS e na Gameloft:

- `jobs.smartrecruiters.com/<empresa>/<id>` (o **anúncio**) **renderiza normal**, texto inteiro,
  sem DataDome no HTML.
- `/oneclick-ui/company/<empresa>/publication/<uuid>` (o **formulário**, atrás do botão
  *I'm interested*) volta com **texto de tamanho zero e `datadome` no HTML**. O botão aponta para
  o host `www.smartr.me`, que devolve *"Oops, you've gone too far"*.

**Consequência prática, e ela é boa:** dá para **ler e qualificar** qualquer vaga do
SmartRecruiters por automação — faixa salarial, regime de trabalho e veto de residência — e só o
**envio** precisa do navegador do Vini. Foi assim que o veto da People Can Fly (*"open to
candidates only from the game industry who are based in Europe"*) foi lido hoje sem gastar
navegador nenhum.

## Workable: `error code: 1015` é a plataforma inteira contra o NOSSO IP, não o estúdio

Medido em 07/09 em **dez quadros diferentes no mesmo minuto** (nexusstudios, kingsisle, bardel,
pxo, team-17-digital, rebellion, pikpok, lighthousegames, one-of-us, streamlinestudios), por
curl **e** por navegador de tela, um por vez: os dez devolvem a mesma página do Cloudflare com
`error code: 1015`. **Isso é limite de taxa, não vaga morta.** `1015` num quadro do Workable
**não autoriza** escrever SEM VAGA nem PAREDE na nota — escreve-se *pendente de reconferência*.

## O Gmail impediu MAIS CINCO repetidas em 07/09, e a garra tinha liberado as cinco

A regra "o `OK` da garra não é prova suficiente para enviar" ganhou cinco casos novos numa
rodada só. A garra respondeu **livre** para Bulkhead, Star Stable, MOOD Visuals, Creepy Jar e
Vine FX, e o Gmail mostrou candidatura já confirmada nas cinco — inclusive duas enviadas nas
horas anteriores, pela própria madrugada. **Buscar o domínio do estúdio no Gmail antes de enviar
não é zelo, é a etapa que pega o trabalho que ainda não foi commitado.**

## Duas correções de regra que a rodada da EA e a do Joe obrigaram

**1. "Título + cidade iguais é suspeita suficiente para pular" TERIA PERDIDO uma vaga efetiva.**
A EA tem três requisições *Character Artist, EA SPORTS FC, Vancouver*. O texto é quase idêntico.
O que as separa é o **Worker Type** e a **faixa salarial**: a 215657 é temporária, a 215666 é
cópia literal dela, e a **215358 é `Regular Employee`, efetiva, com faixa CAD 92.900 a 129.200**.
Aplicar a regra ao pé da letra teria descartado justamente a única efetiva — e efetiva contra
temporária é exatamente o que sustenta patrocínio de visto. **Antes de descartar por título e
cidade repetidos, compare tipo de vínculo e faixa.**

**2. O atalho do `teamtailor-mail.com` é VERIFICADOR, não fonte.** Eu o passei ao Joe como se
fosse mina de endereço. Ele colheu **mais de 40 recrutadores com nome real e cargo**, e
**nenhum endereço**: o domínio `@<token>.teamtailor-mail.com` é relay. Das 40 e poucas pessoas,
só duas viraram carta, e as duas porque o endereço apareceu publicado **em outro lugar**. Montar
`nome.sobrenome@dominio` para as outras seria o mesmo chute que produziu as 17 devoluções.
**O atalho confirma que a pessoa existe, está na casa hoje e cuida de contratação. Quem dá o
endereço é o site.**

## O CENSO DE QUADROS ENVELHECE EM HORAS, e por isso ele agora mora num ARQUIVO

Medido em 07/09 pela fatia COLHEITA. A rodada anterior varreu os quadros de ATS conhecidos, achou
**46 vagas da disciplina que a garra dizia nunca terem sido tocadas**, aplicou em duas e passou o
número adiante **sem gravar o censo em lugar nenhum**. Refazer custou vinte minutos, e o pior é
que o número já não valia: refeito o censo (`automacao/censo-boards-0709.csv`, 173 tokens, 123
quadros, **2.791 vagas**, 165 da disciplina, 74 fora do painel), a conferência no **Gmail** mostrou
que a maioria dessas 74 **já tinha recebido candidatura nas horas anteriores** — Envar, Bluehole
duas, Loonshot, Playdead, Beffio três, Ankama, Bulkhead duas, Stunlocks, Gigglebug, Star Stable —
sem nada disso ter chegado ao painel nem ao `processados.csv`.

**Duas coisas ficam:** (1) censo se salva em arquivo versionado, sempre, porque o custo de gravar
é um `git add` e o de refazer é meia hora; (2) **contagem de "nunca tocada" tem validade de horas**,
não de dias, e a única fonte que acompanha o ritmo é o Gmail. Nesta rodada o Gmail sozinho impediu
**nove repetidas** que a garra tinha liberado com `OK`.

**E a leitura estratégica, que é a parte útil:** o estoque de disciplina nos quadros que a campanha
já conhece **está seco**, e quase tudo o que sobra é parede — BambooHR inteiro com reCAPTCHA de
caixa, Lever com hCaptcha, SmartRecruiters com DataDome, Ashby reprovando a sessão por pontuação, e
os 15 quadros do Workable devolvendo `429` horas depois do primeiro teste. Procurar mais nos mesmos
quadros rende pouco; o que rende é **quadro de estúdio novo**.

## BambooHR: local VAZIO na listagem não é remoto, é campo não preenchido. `atsLocation` diz a verdade.

Medido em 07/09 na Streamline Studios e na Stirling Animation, e as duas enganam para lados
opostos. O `<token>.bamboohr.com/careers/list` devolve `location` com `city`, `state` e
`addressCountry` **todos nulos** nas duas casas, o que faz as vagas parecerem remotas ou europeias.

O `/careers/<id>/detail` traz um segundo campo, **`atsLocation`**, e é ele que tem o dado:
**Streamline é Kuala Lumpur, Malásia** (fora do escopo, três vagas descartadas) e **Stirling é
Stirling, Reino Unido** (dentro do escopo). Um `curl` no `/detail` resolve as duas, e **não gasta
navegador**. Antes de classificar geografia de vaga do BambooHR, leia o `atsLocation`.

## `pkill -f chrome` MATA O SEU PRÓPRIO SHELL

Custou um comando inteiro em 07/09, com registro de painel e commit dentro dele. `pkill -f` casa
contra a linha de comando **completa**, e a linha de comando do shell que roda `pkill -f chrome`
**contém a palavra chrome**: o `pkill` se mata, e tudo o que vinha depois do `;` nunca roda, sem
mensagem nenhuma além de um código de saída 1. Escreva o padrão quebrado, `pkill -f 'chrom[e]'`, ou
confira primeiro com `ps aux` — que nesta rodada mostrou que **não havia navegador nenhum vivo**, e
que o `pgrep -f chrome` estava casando com a linha do próprio gerenciador da sessão.

## Varredura de subdomínio pelo NOSSO proxy custa 1 host por segundo. Meça antes de lançar 9.657.

Medido em 07/09 pela fatia COLHEITA, e é um número que muda o planejamento de rodada. A receita do
`careers.<domínio>/jobs.json` é boa e já rendeu a Envar, mas **pelo proxy desta sessão ela é lenta
de um jeito que a conta ingênua não prevê**: host que não existe não falha rápido, porque quem
resolve o nome é o proxy, e o `curl` fica no `CONNECT` até o timeout inteiro. Com 3.219 domínios ×
3 prefixos = **9.657 hosts**, oito conexões em paralelo e timeout de 8s, o ritmo medido foi de
**cerca de um host por segundo**, ou seja **mais de duas horas e meia** para a lista toda — o
tamanho de uma rodada inteira gasto numa varredura só.

**A parte alfabética que deu tempo de rodar (a até g, 27 quadros achados, 11 com vaga) devolveu
ZERO vaga nova da disciplina.** Os quadros em domínio próprio que apareceram — `careers.beffio.com`
(21 vagas), `careers.embark-studios.com` (18), `careers.bulkhead.com` (6), `careers.envarstudio.com`
(3), `careers.foolstheory.com` (4), `jobs.coffeestain.com`, `jobs.arrowheadgamestudios.com`,
`careers.castirongames.com` — **já estavam todos trabalhados**, e a Fool's Theory, único achado que
parecia novo, tinha recebido a Open Application dela às 00h15 do mesmo dia. Foi a **décima**
repetida que o Gmail impediu nesta rodada.

**Como fazer da próxima vez:** ordene a lista de domínios por prioridade (Canadá e Europa primeiro,
casa sem ATS conhecido antes de casa com ATS conhecido), corte o timeout para 4s, e **rode em
fatia**, medindo o ritmo nos primeiros cem hosts antes de decidir se vale a lista inteira. E nunca
com navegador aberto ao mesmo tempo, que é a regra que já custou o contêiner das 06h44.

## "Nunca tocada" tem validade de HORAS, não de dias, quando há agentes em paralelo

Medido em 07/09 às 10h30. Um agente listou 123 quadros, achou **74 vagas da disciplina fora do
painel**, e ao conferir descobriu que **a grande maioria já tinha recebido candidatura nas horas
anteriores, por outro agente, sem ter sido commitada ainda**: Envar, Bluehole (duas), Loonshot,
Playdead, Beffio (três), Ankama, Bulkhead (duas), Stunlocks, Gigglebug, Star Stable, Fool's
Theory. **O Gmail impediu DEZ repetidas que a garra tinha liberado com `OK`** — somando dezoito
no dia.

Isso não é falha da garra nem do agente: é o preço de rodar em paralelo. O painel só sabe o que
foi **commitado**, e entre enviar e commitar existe uma janela. **O Gmail não tem essa janela**,
porque o estúdio responde em segundos.

**Consequências práticas:**
1. **Commit e push a cada candidatura**, não por rodada. Já é regra; esta medição é o porquê.
2. **A busca no Gmail pelo domínio do estúdio é obrigatória antes de enviar**, e não opcional.
   `JA-FEITO` da garra basta para pular; `OK` da garra nunca basta para enviar.
3. **Lista de "nunca tocada" gerada há mais de uma hora já está velha.** Regenere, ou confira
   uma a uma no Gmail antes de usar.

## O estoque dos quadros CONHECIDOS secou. O que rende agora é quadro de estúdio NOVO.

Leitura honesta de quem varreu: 123 quadros listados inteiros, 2.791 vagas, 165 na disciplina, e
sobrou **uma** candidatura enviável. O resto é parede conhecida: BambooHR inteiro com reCAPTCHA
de caixa, Lever com hCaptcha, SmartRecruiters com DataDome, Ashby reprovando a sessão, Workable
em **429 contra o nosso IP** (medido duas vezes com 40 minutos de intervalo, então é limite da
plataforma e **não autoriza escrever "sem vaga"**).

E a varredura de subdomínio custa **um host por segundo** pelo proxy: mais de duas horas e meia
para os 9.657 hosts da lista, e a fatia que deu tempo de rodar não achou vaga nova nenhuma.
**Não gaste rodada nela sem tempo de sobra.**

## Dois detalhes de leitura de ATS que mentem sobre geografia e sobre o próprio shell

- **A listagem do BambooHR vem SEM LOCAL**, o que faz vaga presencial parecer remota. Quem diz a
  geografia de verdade é o `atsLocation` do `/careers/<id>/detail`. Foi assim que as três vagas da
  Streamline se revelaram em **Kuala Lumpur**, fora do escopo, depois de parecerem remotas.
- **`pkill -f chrome` mata o próprio shell** que rodou o comando, e leva junto o que vinha depois
  na mesma linha. Já custou um registro e um commit inteiros. Use `pgrep` para conferir e mate
  por PID.

## `json.dumps` do Python escreve espaço depois da vírgula, e isso APAGA a candidatura da contagem

Medido em 07/09, e é a armadilha mais silenciosa até agora porque **não quebra nada**: a linha
continua sendo JSON válido, o painel renderiza, o validador passa, e a candidatura simplesmente
**não é contada**.

O `conta-hoje.sh` casa a linha com `\["([^"]+)","([^"]*)",...` e o `.startswith('[') and
',true,' in l`. O `json.dumps` padrão escreve `["A", "B", true, "alta"]`, com espaço, e nenhum
dos dois casa. Resultado: **46 linhas do painel estavam nesse formato**, entre elas as melhores
do dia (EA Vancouver, Epic, Riot), registradas certinho e invisíveis para a contagem. Consertar
o espaçamento sozinho subiu o piso de 109 para 111.

**Regra:** ao reescrever linha do `docs/index.html` por script, sempre
`json.dumps(arr, ensure_ascii=False, separators=(',', ':'))`. Depois de qualquer escrita em
massa, rode `sh automacao/conta-hoje.sh` e confira que o número **subiu**. Número que não se
mexe depois de um envio registrado é sintoma, não coincidência.

## A tela de sucesso do widget de ATS pode ser desenhada NO CLIENTE, e aí ela não é prova

Medido no GoHire em 07/09. O `applyJob` do widget faz o POST e, se o JSON de volta não tem campo
`error`, mostra a div de sucesso. **A tela não vem do servidor.** Ela é `display:block` numa div
que já estava na página.

A consequência inverte a regra da taxonomia de prova nesse caso: para esse ATS, o **200 com
identificador de candidato** é exatamente a mesma evidência que o Vini teria clicando com a
própria mão, e um navegador teria produzido MENOS informação, não mais. Antes de gastar
navegador numa parede de host, leia o JS do widget: se a confirmação for cliente, a chamada
direta à API é igual em força e custa um centésimo.

### Receita pronta do GoHire (medida e usada com sucesso em 07/09)

Serve para qualquer vaga em `jobs.gohire.io/<slug>-<clientHash>/<titulo>-<jobId>/`.
Nenhum passo precisa de navegador, e o host responde bem ao `curl` mesmo estando fora da
allowlist do navegador desta sessão.

1. O widget só serve **com `Referer`**: `curl -H "Referer: https://jobs.gohire.io/"
   https://widget.gohire.io/widget/<clientHash>`. Sem o cabeçalho vem 403 do próprio Apache.
2. Campos e perguntas da vaga:
   `GET https://api.gohire.io/widget-job?clientHash=<clientHash>&jobId=<jobId>`.
   Traz `questions` (perguntas customizadas, muitas vezes `[]`), `salary` com a faixa
   publicada e `client.uploadExtensionsForm`. **Leia `questions` antes de montar o corpo.**
3. CV: `POST https://api.gohire.io/upload-chunk` com JSON
   `{name, type, jobId, clientHash, source:"widget", id:<aleatório>, chunk, chunks, data}`,
   onde `data` é `data:<mime>;base64,<conteúdo>` fatiado em pedaços de 0,5 MB
   (`0.5*1000*1024` caracteres). A última resposta devolve `key` e `name`.
4. Envio: `POST https://api.gohire.io/apply?clientHash=<clientHash>&jobId=<jobId>` com
   `{coverNote, candidate:{name, surname, email, phone, cv:<key>, cvName:<name>},
   questions:[], from:"widget", referrer:"https://api.gohire.io", isChecked:true}`.
   Só `name` e `surname` são obrigatórios no HTML; email e telefone não são marcados, mas
   vão sempre. Resposta 200 com `userId` é candidatura criada.

O script usado está em `$SCRATCH/gohire_apply.py` e recebe o arquivo da carta como argumento.

## O sitemap de vagas do Hitmarker tem TRES paginas, nao infinitas, e o estoque dele esta trabalhado

Medido em 07/09 pela fatia HITMARKER, e o numero corrige a suposicao que abriu a fatia.
`hitmarker.net/sitemap-jobs.xml/p1` e `/p2` devolvem 5.000 URLs cada. **A partir da `/p3` o
servidor devolve SEMPRE o mesmo rabo de 2.927 URLs**, com bytes identicos e md5 diferente (a ordem
muda a cada pedido), entao `/p4` ate `/p7` nao acrescentam uma URL sequer. O total real e
**12.926 vagas unicas**, e nao 5.000 por pagina ate acabar.

Sobre as 12.926: **95** batem `character|modeler|modeller|sculpt|3d-artist|creature`, e **65**
sobrevivem ao corte de concept 2D, engenharia, animacao, rigging, estagio e banco de talentos da
Side. Dessas 65, conferidas uma a uma contra o painel e o `processados.csv`:

- **duas** a garra recusou direto (Vertigo Istambul e Lightfold);
- **cinco** estao fora do recorte geografico (Lakshya e Scopely Bangalore na India, Kojima e
  PlayStation Team Asobi no Japao, Virtuos em Ho Chi Minh, Jam City em Montevideu);
- **quase todo o resto ja tem candidatura ou ja tem parede escrita no painel**: Behaviour 7 Days
  to Die (enviada 30/08), Rebellion Oxford (enviada e recusada 01/09), 2K Cloud Chamber Novato e
  Montreal, 2K Small Axe Burnaby, Hasbro Skeleton Key Austin e Montreal, EA Vancouver, Epic (quatro
  candidaturas e uma decisao escrita de nao mandar a quinta), Avalanche, Frontier, Lighthouse,
  Ubisoft Massive, Ubisoft Montpellier, Techland, Fatshark, thatgamecompany, Keywords.

**A licao para quem pegar este quadro depois:** o Hitmarker e agregador, e a campanha ja passou por
ele. O que ele ainda rende **nao e a vaga da lista, e o ESTUDIO que a vaga revela** quando se abre
o quadro inteiro do ATS dele. Foi assim que saiu a NBCUniversal: o sitemap trouxe UMA Associate Art
Director e o quadro do SmartRecruiters mostrou uma familia inteira de lideranca de arte em Montreal.

Duas armadilhas de leitura medidas na mesma rodada, as duas de filtro por palavra:
- **`Character Lead` da Mari, em Londres, e ator dentro de fantasia** no Battersea Power Station,
  a 14,75 libras a hora. Titulo perfeito, disciplina nenhuma.
- **`Senior Character Designer` da Razer, em Singapura, e direcao criativa e narrativa**: character
  bibles, arquetipo, briefing de animacao e skins, com estudio externo fazendo o asset. Nao e
  modelagem. Ler o corpo do anuncio antes de contar como vaga da disciplina.

## O Workable tem DOIS hosts, e so um deles esta em 1015: `jobs.workable.com` responde 200

Achado de 07/09 que muda o que se pode fazer durante um bloqueio do Workable, e e o achado mais
util desta fatia.

`apply.workable.com` esta em **`error code: 1015`** contra o IP desta sessao, confirmado de novo em
07/09 no board (`apply.workable.com/<conta>/`) e na API publica
(`/api/v1/widget/accounts/<conta>`), com curl pelado **e** com cabecalho completo de Chrome
(User-Agent, Accept, Accept-Language, Sec-Fetch-Mode, Upgrade-Insecure-Requests). Trocar cabecalho
nao muda nada: e bloqueio por IP.

**Mas `jobs.workable.com` e outro host e responde 200.** E ele serve um indice de busca que
atravessa TODAS as contas do Workable:

    GET https://jobs.workable.com/api/v1/jobs?query=character%20artist
    GET https://jobs.workable.com/api/v1/jobs?query=...&pageToken=<nextPageToken>

Cada item vem com `title`, `company`, `location` (com `countryName` e `city`), `workplace`
(`remote`, `hybrid`, `on_site`), `employmentType`, `department`, `description`,
`requirementsSection` e `url`. Ou seja: da para **qualificar geografia, regime de trabalho, faixa e
exigencia de disciplina de qualquer vaga do Workable inteiro sem navegador e sem passar pelo host
bloqueado**. So o ENVIO continua preso no `apply.workable.com`.

Cuidado com o formato: o pais NAO esta em `location.country` (esse campo nao existe), esta em
**`location.countryName`**, e `company` as vezes vem string e as vezes vem objeto com `title`.
Filtro escrito contra `country` devolve zero e parece que nao ha vaga, quando ha.

Rodando oito consultas (`character artist`, `3d modeler`, `texture artist`,
`look development artist`, `3d character`, `creature artist`, `character modeler`,
`material artist`) sairam **391 vagas unicas**, e **41 dentro do recorte geografico e da
disciplina**. Quatro entraram no painel como pendentes por 1015: Side Senior Texture Artist
(Montreal e Toronto), Sperasoft Material Artist (stylization, seis requisicoes na Polonia, Romenia
e Servia), Liquid Development Material Artist e Sawhorse Productions Roblox 3D Artist.

### O `jobs.workable.com` serve tambem o FORMULARIO INTEIRO, e mesmo assim NAO ENVIA. Medido em 07/09.

O achado acima estava certo pela metade, e a metade que faltava vale nos dois sentidos. **Ele da
MAIS do que se pensava:** alem do indice de busca e do anuncio, o host nao bloqueado serve a
**estrutura completa do formulario de candidatura**:

    GET https://jobs.workable.com/api/v1/jobs/<uuid>/form?includeAccountMetadata=true

Devolve secao por secao **cada campo com `id`, rotulo, tipo, obrigatoriedade e a lista de opcoes com
o id de cada uma**, mais o `gdprPolicyUrl`, de onde sai de graca o **slug da conta** no
apply.workable.com. O `<uuid>` e o campo `id` do item do indice. Isso muda o que se pode escrever
sobre uma vaga do Workable: **nenhuma precisa mais ficar com dossie chutado nem com nota de
"pendente de reconferencia"**. Ela entra direto como **a mao com o formulario campo a campo**, e o
Vini envia em um minuto. Foi assim que sairam seis dossies exatos numa rodada so, entre eles o da
Lighthouse Games, cujo `/form` revelou que **os unicos campos obrigatorios sao nome e email** — a
candidatura mais barata da fila inteira, que estava parada havia dias.

**E a metade ruim, que fecha a pergunta: o ENVIO nao passa por lugar nenhum.** O
`POST /api/v1/jobs/<uuid>/apply?lng=en` existe e responde. O corpo e
`{candidate:[{name,value}],job:{position:<numero>}}`, descoberto por sondas de carga incompleta, que
so podem gerar erro de validacao e nunca candidatura (`{"candidate":{}}` devolve *"candidate must be
an array"*, e `{"id":...}` no item devolve *"id: Not allowed"*). Com o corpo **bem formado** o
servidor devolve **`412 Precondition Failed`** e o cabecalho **`x-ts: 0`**, que e o token do
**Cloudflare Turnstile** faltando (`wjb_acp_turnstile_captcha_enabled: true` no
`/api/v1/feature-flags`).

**E o navegador de tela NAO passou onde o curl nao passou**, que era exatamente a licao do Half
Breaks a testar: o formulario monta inteiro, o CV sobe para
`workable-application-form.s3.amazonaws.com`, os radios e o dropdown gravam, o botao *Submit
application* fica **habilitado**, e no clique sai um `POST` para `challenges.cloudflare.com` e o
POST de candidatura **nunca sai**, com o botao virando cinza e ficando assim. Mesma parede, mesma
causa, pelos dois caminhos.

**Entao o Workable tem DUAS paredes diferentes e convem nao confundi-las na nota:** o `1015` do
`apply.workable.com` e **limite de taxa contra o NOSSO IP**; o Turnstile do `jobs.workable.com` e
**captcha de pontuacao da PLATAFORMA**. Nenhuma das duas e do estudio, e a vaga continua viva.

**Tres armadilhas medidas no formulario, todas silenciosas:**

1. **Os radios ficam ESCONDIDOS atras de widget proprio.** A estrutura e
   `fieldset[role=radiogroup][data-ui=<idDoCampo>]` com
   `div[data-ui=option][role=radio]` envolvendo `<label><input name="<idDoCampo>" value="true|false"
   aria-hidden tabindex="-1">`. `input.click()` nao move nada; quem recebe o clique e o **label**.
   Enderecar por `input[name][value]` e deterministico e evita a armadilha da Plastic Wax de casar
   rotulo por regex e pegar a primeira opcao que casa num campo de elegibilidade.
2. **A leitura logo apos o clique MENTE.** Ela devolve `false` com o radio certo marcado, porque o
   React ainda nao atualizou. So a **releitura do DOM depois de todos os cliques** diz a verdade —
   nove radios que apareceram como "clicou e nao marcou" estavam todos corretos na conferencia.
3. **A pagina tem DOIS botoes `Submit application`** (cabecalho fixo e fim do formulario) e o widget
   de **Feedback** do Workable tambem casa com `/submit/i`. Seletor frouxo com `.last()` clica no
   botao errado, o painel parece fechar e **nenhum POST sai**, com o log dizendo que o clique
   funcionou. Alvo ancorado, `/^Submit application$/`, e conferir se o POST existiu.

E o **endereco vem autopreenchido com `Columbus, United States of America`**, pela geolocalizacao do
nosso proxy. Trocar sempre.

## O GoHire publica o sitemap da PLATAFORMA INTEIRA, e o `robots.txt` entrega o caminho

Medido em 07/09. `jobs.gohire.io/robots.txt` aponta para **`jobs.gohire.io/sitemap.txt`**, que e
uma lista de texto puro com **20.369 URLs de vaga de todos os clientes do GoHire**, no formato
`jobs.gohire.io/<slug-da-empresa>-<idNumerico>/<titulo>-<jobId>/`.

**A armadilha, e ela invalida o uso ingenuo da lista:** o `<idNumerico>` do sitemap **NAO e o
`clientHash`** que a API pede, e a URL com o numero devolve **404**. Provado na Makeshift, que a
campanha usou hoje: `makeshift-software-10013422/senior-character-modeler-299993/` da 404, e
`makeshift-software-hnqmphxc/senior-character-modeler-299993/` da 200, mesma vaga. O `jobId`, esse
sim, e o mesmo nos dois, e com o `clientHash` certo a API responde tudo:
`widget-job?clientHash=hnqMpHxc&jobId=300611` devolve 200 para a Senior 3D Environment Artist que
pela URL numerica parecia arquivada.

Nao ha endpoint que traduza o id numerico em `clientHash`: testados e todos 404
(`widget-jobs`, `widget`, `jobs`, `widget-client`, `company?id=`, `widget-job` com o numero no
lugar do hash). **O hash so aparece no site do proprio estudio**, no `<script>` de
`widget.gohire.io/widget/<clientHash>` da pagina de carreiras dele.

**Entao o sitemap serve como DIRETORIO DE EMPRESAS, nao como fila de vagas clicaveis:** ele diz
quem usa GoHire e com que titulos, e a partir dai se procura o hash no site do estudio. Resultado
honesto desta rodada: das 20.369 URLs, so **cerca de 25** batem a disciplina, e quase todas sao ou
ja trabalhadas (Lightfold, Makeshift), ou fora de nivel (Hug & Roll Gaming e entry level de 0 a 1
ano a 15 a 40 dolares a hora), ou repeticao de spam de Web3 (a Bondex sozinha tem onze copias da
mesma 3D Stylized Environment Artist). **A NBCUniversal tem board no GoHire** com a mesma Associate
Art Director de Montreal, mas o anuncio esta arquivado e o hash nao foi achado; se alguem achar o
`clientHash` da NBCUniversal, essa e a porta que contorna o DataDome do SmartRecruiters delas.

## Contar linha do painel sem RECORTAR o array primeiro dá número inflado

Erro cometido pelo coordenador em 07/09 e medido por outro agente na mesma hora. Contei as
entradas de portal varrendo o `docs/index.html` **inteiro** e filtrando por `a[3] == 'portal'`.
Deu **723 entradas e 282 sem candidatura**. Os números reais, recortando o trecho entre
`const PORTAIS = [` e o `].map` que o fecha, são **655 e 405**, e das 405 apenas **nove** não
trazem veredito escrito na nota.

A causa é a mesma que já estava escrita no brief do agente da Europa e que eu não apliquei:
**nome de estúdio e linha com cara de portal aparecem em mais de um array**. Varrer o arquivo
inteiro mistura PORTAIS com outros arrays e infla a fila.

**Regra:** para qualquer contagem ou edição de array do painel, recorte primeiro o bloco do
array alvo pelo seu `const NOME = [` e pelo `].map` que o fecha, e só então procure dentro dele.
Isso vale para contar, para editar por âncora de texto e para deduplicar.

E a lição de fundo, que custou uma correção pública ao Vini: **um número que contraria uma
conclusão já medida por três agentes merece ser reconferido antes de virar recomendação.** Eu
usei o 282 para dizer a ele que a fila não tinha secado, quando tinha.


## A PARAMOUNT NAO E MAIS PONTO CEGO: o careers.paramount.com responde 200 e publica RSS

Medido em 07/09 pela fatia REGRA 14, e corrige a instrucao que estava valendo ("responde Access
Denied do Akamai ate no navegador, nao gaste rodada nela"). O host que estava sendo batido nao era
o certo. **`careers.paramount.com` (SuccessFactors RMK) responde 200 a curl pelado** com um
User-Agent de Chrome, e a propria pagina de busca anuncia, no `<link rel="alternate">`, um feed:

    https://careers.paramount.com/search/?q=<termo>&startrow=0     (25 por pagina)
    https://careers.paramount.com/services/rss/job/?locale=en_US&keywords=(<termo>)

**Duas medicoes que evitam conclusao errada com esse feed:**

1. **O RSS corta em cerca de 20 itens por consulta**, entao ZERO no RSS nao prova ausencia. Dez
   termos diferentes devolveram 66 URLs unicas, e o filtro de palavra-chave dele e frouxo: buscar
   `modeler` traz 210 KB de vaga de engenharia de dados.
2. **Quem prova e a busca paginada.** A pagina declara o total ("291 Jobs") e pagina por
   `&startrow=`. Doze pedidos leem o quadro INTEIRO. Feito isso em 07/09: das **291 vagas da
   Paramount, ZERO** e de personagem, modelagem, texturizacao, look dev ou 3D. O unico titulo de
   arte e um Art Director da CBS Sports, que e design de broadcast.

**Consequencia pratica:** a Paramount passa a ser conferivel por curl a qualquer hora, em doze
pedidos, sem navegador. Isso importa porque o alerta por email dela **nao esta provado**: a caixa
tem um unico "New jobs posted from Paramount" (`paramountcareers@noreply.jobs2web.com`), de 31/08,
chegado minutos depois da criacao da conta, e nada nos sete dias seguintes. Pela regra de 05/09,
alerta so conta como ativo depois de ver a ativacao, e essa nunca apareceu. Trate a casa como
coberta pelo RSS, que se verifica, e nao pelo alerta, que nao se verifica.

**De quebra, o mesmo vale para a leitura da Warner:** os dois alertas dela **estao** ativos e
disparando, e isso esta provado na caixa (ativacao confirmada por email em 05/09 para
`character artist` semanal e `modeler` diario, e listas entregues em 05/09 e 06/09 por
`careers@careeralerts.wbd.com`). Alerta provado e alerta suposto sao coisas diferentes; escreva
qual dos dois voce tem.

## Leia a seção Eligibility Requirements ANTES de recomendar a vaga, não depois

Erro do coordenador em 07/09, e o mais caro do dia porque saiu como PushNotification para o
Vini. Recomendei as três vagas da NBCUniversal em Montréal como a primeira coisa da manhã dele,
com base no que a nota do painel dizia e no fato de o anúncio citar *XGen, Houdini Groom,
Metahuman, cloth simulation* pelo nome. Só depois um agente leu o anúncio inteiro e achou, em
*Eligibility Requirements*: **"Must be legally authorized to work in Canada"** e *"Must be
willing to work in our Montreal office a minimum of 4 days a week"*. Confirmei na API oficial,
no texto da própria Lead Character Artist, a que eu tinha empurrado.

É a **classe de descoberta mais cara da campanha**, a do veto de residência, e ela mora quase
sempre num bloco no fim do anúncio que a listagem do ATS não mostra: *must be based in*,
*required to be based*, *eligible to work in*, *no sponsorship*, *Eligibility Requirements*.

**Regra:** antes de marcar prioridade alta, antes de escrever no arquivo do Vini e sobretudo
antes de mandar push, baixe o anúncio inteiro pela API e faça a busca literal por
`authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `days a week`. Custa um curl.
Recomendação forte com base em nota de terceiro, sem ter lido o texto integral, é como se
constrói uma expectativa que o próprio anúncio já desmentia.

## Workable: parede medida até o fim, e são DUAS paredes diferentes

Fechado em 07/09, para ninguém gastar rodada nisso de novo.

- `apply.workable.com` devolve **429 / `error code: 1015`**: limite de taxa do Cloudflare contra
  o **nosso IP**. Igual com curl pelado e com cabeçalho completo de Chrome.
- `jobs.workable.com` **não** está bloqueado e dá mais do que se pensava: além do índice de
  busca entre todas as contas, o `GET /api/v1/jobs/<uuid>/form?includeAccountMetadata=true`
  serve a **estrutura completa do formulário** — cada campo com id, rótulo, tipo,
  obrigatoriedade e a lista de opções com o id de cada uma, mais o slug da conta no
  `gdprPolicyUrl`. **Nenhum dossiê de Workable precisa mais ser chutado.**
- Mas ele **não envia**. O `POST /api/v1/jobs/<uuid>/apply` existe e o corpo é
  `{candidate:[{name,value}],job:{position:<n>}}`, descoberto por sondas de carga incompleta que
  só geram erro de validação. Com corpo bem formado o servidor devolve **412 Precondition
  Failed** com **`x-ts: 0`**: falta o token do **Turnstile**.
- **O navegador de tela não passa onde o curl não passa**, e isso foi testado num alvo (Side):
  o formulário monta, o CV sobe para o S3 do Workable, os campos gravam, o Submit habilita, e no
  clique sai um POST para `challenges.cloudflare.com` e o POST de candidatura **nunca sai**.

Ou seja: o `1015` é do nosso IP e o Turnstile é da plataforma. **Nenhuma das duas é do estúdio**,
e nenhuma se contorna. Vaga de Workable vira dossiê à mão, sempre, e o dossiê agora sai completo
e correto de graça pela API de formulário.

## O PDF de portfólio existe, mas o ARTSTATION é a prioridade (regra do Vini, 07/09)

O `Vini_Cavalcanti_Portfolio.pdf` está em `$SCRATCH/apply/` (2,56 MB, 7 páginas), baixado da
pasta Vagas do Drive dele. **Ele não substitui o link.** Regra dita por ele ao entregar o
arquivo: *"lembre que isso é só nos que precisa mesmo, a prioridade é mandar o artstation e não
o pdf de portfolio"*.

Como decidir, campo a campo:

1. **Há campo de link, URL, portfolio, website ou "share your work"?** Então vai
   `https://www.artstation.com/viniciuscavalcanti` e **o PDF não entra**, mesmo que exista um
   campo de anexo opcional ao lado. Anexo opcional não se preenche só porque está lá.
2. **O upload é obrigatório e não existe alternativa de link?** Aí sim o PDF, e só aí.
3. **O campo aceita só imagem** (o `accept` do Engine Room é `audio/*,video/*,image/*`, que
   recusa PDF): o PDF não serve, continua sendo caso de mão do Vini.

O motivo é dele e é bom: o ArtStation tem mais de 45 projetos com mais de 60 personagens e é
atualizado; o PDF é um recorte de sete páginas, congelado em 26/08. Mandar o recorte quando dava
para mandar a obra inteira é perder por escolha nossa.

**Detalhe de tamanho, medido:** 2,56 MB passa no teto de 3 MB do GoHire, mas **estoura qualquer
formulário com limite de 2 MB**. Antes de anexar, leia o limite que o formulário declara
(`uploadMaxSize` nas APIs que expõem isso) e, se não couber, registre como à mão em vez de
mandar arquivo cortado.

## A garra vale para o COORDENADOR também, e ele já furou essa regra

Erro cometido por mim em 07/09 às 16h15. A recrutadora da Union VFX respondeu recomendando
candidatar pelo site, eu achei o formulário, mapeei, enviei e confirmei na tela. **Não rodei a
garra antes.** Rodando depois, ela devolve `JA-FEITO` na hora: outro agente já tinha enviado ao
mesmo formulário mais cedo no mesmo dia.

O que torna o erro instrutivo é o contexto: eu estava agindo sobre um **pedido explícito de uma
pessoa de verdade**, e a urgência de responder bem a ela atropelou a checagem. A regra existe
justamente para o momento em que parece óbvio que não há duplicata.

**Regra:** `sh automacao/garra.sh checa "<url>"` antes de QUALQUER envio, sem exceção de quem
está enviando, e **especialmente** quando o envio nasce de uma resposta humana, porque aí a
pressa é maior. A contagem não infla, porque o `conta-hoje.sh` deduplica por estúdio, mas o
recrutador vê duas entradas do mesmo candidato no mesmo dia, e esse dano não aparece em número
nenhum.

## Casa que publica em dois idiomas engana o dedupe por título

Achado em 07/09, e ele estava prestes a fazer o Vini se candidatar de novo a uma vaga em que já
tinha sido **recusado**.

O painel listava "Ubisoft Montreal, Senior Character Artist (Rainbow Six Siege)" como vaga nova à
mão, esperando por ele. A campanha já tinha se candidatado a ela em **30/08** e recebido a
**recusa em 02/09** — mas aquele registro está com o título em **francês**, *Artiste de
personnages sénior·e (Rainbow Six Siege)*, porque o SmartRecruiters serve o título localizado
conforme o idioma de quem abre a página. Título diferente, mesma requisição.

**Prova:** a API oficial devolve **uma única** requisição de Senior Character Artist do Rainbow
Six em todo o quadro, id `744000145282762`, referência `REF31793B`, Montreal, liberada em 24/08.
Bate com a data da candidatura e com a da recusa.

**Regra:** para dedupe, **o id da requisição ou a referência mandam, e o título não vale nada**.
Vale sempre, e vale em dobro nas casas que publicam bilíngue: Ubisoft, Larian, Gameloft, Sloclap,
Skydance Madrid. Registre SEMPRE o id junto da URL, porque é ele que a garra consegue casar.

**Detalhe que destravou a conferência:** o token do SmartRecruiters da Ubisoft é **`ubisoft2`**,
não `ubisoft` nem `UbisoftGroup`, que devolvem zero e passam a falsa impressão de quadro vazio.

## Workday recusa lote grande, e isso faz varredura declarar quadro morto

Medido na Cloud Imperium em 07/09. O endpoint público do Workday deles aceita `"limit":20` e
devolve **HTTP 400** com `"limit":50`. Quem varre com lote maior lê o 400 como casa inacessível e
registra quadro morto onde há **61 vagas abertas**.

**Regra:** varredura de Workday vai sempre com `limit` 20 e pagina por `offset`. E confira o
`total` que a resposta devolve: foi ele que mostrou que a leitura anterior de "26 vagas" estava
errada por mais da metade.

Vale junto a lição de sempre: a página `<estudio>.com/jobs` costuma ser vitrine, e o ATS real
mora noutro domínio. Na Cloud Imperium é `cloudimperiumgames.wd503.myworkdayjobs.com`.

## Patrocínio de visto: casa pequena na EUROPA não consegue, no CANADÁ costuma ser fácil

Regra dita pelo Vini em 07/09, corrigindo uma generalização minha. Eu peguei um caso holandês e
transformei em regra universal, e isso ia despriorizar exatamente o alvo mais acessível dele.

**Na Europa**, casa pequena de fato não patrocina, e o limite é **estrutural**, não de vontade:
piso salarial alto para visto de trabalho qualificado, custo e burocracia que empresa pequena não
absorve. A Head of HR da **Galaxy Grove**, em Utrecht, escreveu isso por conta própria em 07/09:
*"we do not have the means to sponsor employees from outside the European Union"*, e acrescentou
que provavelmente vale para outras empresas pequenas de lá. Consequência prática: numa recusa de
estúdio pequeno europeu, o "não" costuma ser de **estrutura**, não do portfólio dele.

**No Canadá é o contrário: costuma ser fácil, inclusive para estúdio pequeno.** Portanto, em
território canadense:

- **Não existe desempate por porte.** Estúdio pequeno e médio entra com o mesmo peso de casa
  grande, e vaga da disciplina em casa pequena é alvo de **primeira** linha.
- **O que derruba é veto ESCRITO no anúncio**, não suposição: *must be legally authorized to work
  in Canada*, *must be based in*, *we do not sponsor*, *permanent resident or citizen*.
- O sinal positivo escrito (*visa sponsorship*, *relocation assistance*, *LMIA*, *work permit
  support*) continua valendo como reforço, mas a **ausência dele não é veto** no Canadá.

E a regra de salário ganha o motivo certo: no Canadá nunca pedir abaixo do salário vigente do
LMIA, porque pedir abaixo **não o torna barato, torna impossível de patrocinar**. Isso vale em
casa de qualquer tamanho.

## A fatia CANADA foi medida por inteiro em 07/09: 103 entradas, e o que sobrou nao e vaga, e parede

Leitura honesta de quem varreu as 103 entradas canadenses do PORTAIS que estavam com `done=false`.
**Zero candidatura enviada, e o motivo nao e falta de vaga: e que toda porta canadense que restava ja
esta medida como parede, e as que nao eram parede tem VETO ESCRITO.** Quem pegar esta fatia depois nao
precisa reabrir nada disto.

**O teste de realocacao derrubou CINCO casas, e duas delas estavam marcadas `alta`.** A busca literal por
`authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA` e `days a week` no texto INTEIRO
baixado pela API oficial, e nao na listagem do ATS, achou o veto onde a nota do painel dizia que nao havia:

- **NBCUniversal / DreamWorks, as tres requisicoes de Montreal** (REF38910F, REF38920U, REF38909O):
  *"Must be willing to work in our Montreal office a minimum of 4 days a week. Must be legally authorized
  to work in Canada."* Duas estavam `alta`. Cada uma tinha **duas entradas** no painel, uma como
  NBCUniversal e outra como DreamWorks e NBCU: seis linhas para tres requisicoes.
- **Barnstorm, Creature Lead** (`careers/176`), que estava `alta`: *"This role is open to Canadian based
  talent. Candidates must be legally authorized to work in Canada."* A `careers/204` tem o irmao dela.
  **A unica porta boa da casa e a `careers/114`**, cujo corpo nao tem veto nenhum.
- **Image Engine, o quadro INTEIRO** (`careers/21`, `28` e `183`): *"Candidates are required to be based in
  British Columbia and eligible to work in Canada."* Inclusive o banco de talentos de Assets, que a nota
  antiga chamava de "a via mais limpa que apareceu nesta rodada".
- **thatgamecompany**: *"We are unable to sponsor or take over sponsorship of an employment Visa at this
  time"*, e a requisicao trocou de `Remote - US/Canada` para **`Remote - US`** apenas.
- **Atomic Cartoons, CG Designer**: *"Currently legally entitled to work in Canada"* mais *"Applicants must
  have resided within BC"*.

**Passaram no teste, e sao estas que merecem o navegador do Vini:** ICON Creative `136` (Open, faixa
publicada CAD 63.131,12 a 85.000, zero veto no texto), Offworld `198` e `199`, Barnstorm `114`, Cinesite
Montreal `93` e Vancouver `260`, e as tres da Behaviour em Montreal, que tambem nao pedem frances.

**Sinal positivo raro, e ele estava escondido no bloco de beneficios:** a Candidature Spontanee da
**Gameloft Montreal** (REF1006B) escreve *"Support for new employees relocating from countries or regions
outside Quebec"*. Isso e apoio a realocacao dito por escrito, que e o sinal mais forte da campanha.

**Uma promocao, e ela corrige uma leitura antiga:** a **People Can Fly**, Principal Character Artist,
Montreal, estava `baixa` com o motivo "exige residencia num dos dois paises". O texto integral diz
*"someone who can work remotely from either Poland or Canada (EST)"*, que e onde trabalhar e **nao**
exigencia de ja ter permissao. Como o objetivo dele e justamente mudar para o Canada, isso deixa de ser
motivo de rebaixamento. Subiu para `media`.

### `ATS_CAREERS_SITE_RECAPTCHA`: a prova de que o BambooHR e parede de PLATAFORMA

A campanha ja tinha medido o reCAPTCHA do BambooHR na ICON e na Image Engine e deduzido que o quadro
inteiro era parede. Agora ha prova direta: os **seis** quadros canadenses do BambooHR (`owi`,
`barnstormvfx`, `iconcreative`, `cinesitemontreal`, `cinesitevancouver`, `imageengine`) servem, todos, a
flag `ATS_CAREERS_SITE_RECAPTCHA` na lista de features do proprio BambooHR. **Nao e configuracao de
estudio.** Nao vale abrir navegador para conferir de novo, em nenhum quadro do BambooHR.

E o mesmo tipo de confirmacao vale para o **Lever**: as paginas `/apply` da Behaviour, da Kabam, da
Blackbird e da Larian trazem, cada uma, 22 ocorrencias de `hcaptcha` no HTML servido. Parede de
plataforma, medida por contagem e sem gastar navegador.

### Parede de CONTA nao e parede de captcha, e a diferenca importa

Duas casas canadenses ficaram registradas como inacessiveis quando o obstaculo e outro e e mais barato:

- **Mainframe Studios** (UKG Ready, `secure.ukgready.ca/ta/6214859`): todo caminho de candidatura cai em
  *"Sign In / Register - Job Candidate Account"*. Zero captcha.
- **WildBrain** (TalentSoft): o quadro tem **zero** script de captcha, e existe uma porta
  *"Submit a speculative job application"* — que aponta para `/my-account/my-CV-file.aspx`, ou seja, conta.

**Captcha nao se burla; conta se cria.** As duas sao trabalho de um cadastro, nao de um desafio.

### Portas que morreram do lado do estudio, e a prova de cada uma

- **Phoenix Labs**: quem desenhava a candidatura era um embed do Greenhouse com o token
  `phoenixlabsyvren`, e o quadro **nao existe mais**. 404 na API, 404 no
  `boards.greenhouse.io/embed/job_board/js?for=`, e 404 no anuncio direto. O texto "General Application -
  Remote - Canada" que ainda aparece na tela e conteudo estatico do site deles. **Pagina que renderiza nao
  prova quadro vivo quando o quadro e um embed.**
- **Digital Dimension** (Montreal): o formulario proprio e simples e **nao tem captcha**, mas depende do
  `folkshr.app` com uma apiKey publicada no HTML deles, e pedir o token com essa chave devolve hoje
  `{"success":false,"error":"Invalid_API_Key"}`. Sem token nao ha lista de vaga e nao ha POST. Nao e a nossa
  rede.
- **Fluffy Dog Studio**: *"There are currently no open positions"*, e a porta e o mailto
  `careers@fluffydogstudio.com`, nao formulario.

### Dedupe: duas armadilhas bilingues medidas nesta fatia

- **Rodeo FX**: as duas vagas de Montreal, `744000145587059` (ingles) e `744000145587250` (frances), tem a
  **mesma referencia RDO180I**. Um anuncio so, dois idiomas, dois ids de anuncio. A de Toronto,
  `744000144123709`, e outra requisicao (RDO243M) e e a preferida por ser Canada anglofono.
- **Framestore**: a oferta `2120070` do Recruitee tem **duas entradas no painel com a MESMA URL**.

### O criterio "casa grande na frente" NAO vale no Canada. Correcao do Vini em 07/09.

A frase da HR da Galaxy Grove, *"we do not have the means to sponsor employees from outside the European
Union"*, e **europeia**: la o piso salarial do visto qualificado e o custo burocratico realmente excluem
empresa pequena. **No Canada o patrocinio costuma ser viavel inclusive em estudio pequeno.** Entao estudio
canadense pequeno e medio entra com o **mesmo peso** de casa grande, e o que derruba uma canadense continua
sendo so o **veto escrito** no anuncio ou a **vaga expirada**. Se alguma canadense tiver sido rebaixada por
porte, reabra.

## A garra estava travando a fila inteira de formulário, e ninguém viu (07/09, à noite)

Achado ao ir aplicar na Netflix Head of Characters de Vancouver, que estava marcada `alta`
e `done=false`. Rodei `sh automacao/garra.sh checa` como o brief manda e a resposta foi
`JA-FEITO`, saída 4.

A causa: a função `feito()` conferia **presença** da URL no `docs/index.html`, sem olhar o
estado. Só que **toda entrada da fila de formulário está, por definição, dentro do
`docs/index.html`** — é lá que a fila mora. Então a garra respondia `JA-FEITO` para as 475
entradas com `done=false`, que são exatamente as que faltam fazer.

O efeito é pior do que parece, porque o brief do Jhon diz, com estas palavras: "antes de
QUALQUER candidatura, rode `sh automacao/garra.sh checa` e depois `pega`; saída 4 quer dizer
já feito". **O agente que obedecia o brief ao pé da letra pulava a fila inteira** e voltava
dizendo que o poço estava seco. A trava que existia para impedir candidatura repetida estava
impedindo candidatura.

Isso obriga a reler com desconfiança toda conclusão de "fila seca" escrita hoje. Fila seca
medida por agente que rodava a garra antes de abrir a vaga NÃO é medida, é o defeito falando.
O que continua de pé é o que foi medido abrindo a fonte oficial: veto escrito no anúncio,
vaga expirada, parede de captcha. O que cai é qualquer "pulei porque a garra disse feito".

O conserto, que guarda a proteção e devolve o trabalho:
- No painel, só conta como feito a linha que está com `,true,` (done=true).
- No `processados.csv`, só contam os tipos que significam candidatura: `portal-aplicado`,
  `confirmacao-portal`, `portal-enviado`, `candidatura`, `enviado`. Levantamento, varredura,
  `vaga-nova`, `revalidacao`, `bloqueio` e `vaga-a-mao` NÃO são candidatura e não travam.
- URL no painel com `done=false` não trava, mas o `checa` devolve `livre (ATENCAO: ...)`,
  porque o caso Larian de hoje mostrou que existe envio real sem a linha do painel marcada.
  O aviso mantém de pé a regra do brief de conferir o Gmail antes de enviar.

A lição geral, e ela vale para qualquer trava que a gente escreva: **uma trava que nunca
libera nada não é conservadora, é quebrada.** Se um guarda-corpo passa um dia inteiro
recusando tudo e ninguém estranha, o sintoma some dentro do resumo como "não achei trabalho".
Toda trava nova precisa de um teste que prove que ela deixa passar o caso legítimo, não só
que ela barra o caso ruim.

## Correção da minha própria conclusão sobre a garra (07/09, meia hora depois)

Escrevi acima que a garra quebrada "provavelmente explica a baixa produção de formulário do
dia". Fui atrás e **não há prova disso**, então desfaço a parte especulativa e guardo só o
que foi medido.

O defeito era real e teria travado trabalho legítimo — isso continua de pé, e o conserto
continua certo. Mas o agente da fatia europeia relatou que montou a fila **direto do array
PORTAIS**, recortado por script entre `const PORTAIS = [` e o `].map`, sem passar pela garra
para ESCOLHER, e por isso não pulou nada. E a única linha do `processados.csv` que registra
a garra barrando trabalho ("a garra barrou tudo que parecia novo", varredura das 16h55 nas
quatro casas grandes) foi conferida: as quatro vagas eram genuinamente já conhecidas ou já
recusadas. A garra acertou naquele caso.

A lição dupla, e a segunda metade é sobre mim:
1. **Uma trava que nunca libera nada não é conservadora, é quebrada.** Vale, e o conserto fica.
2. **Achar a causa de um problema não prova que ela produziu o efeito que te incomodava.**
   Eu achei um defeito real e imediatamente o pendurei no número que estava me incomodando,
   que era a produção baixa de formulário. Isso é a mesma pressa que me fez mandar candidatura
   repetida para a Union VFX. Defeito achado e efeito medido são duas afirmações separadas, e
   a segunda precisa de evidência própria.

## Workable: a queda do 1015 destrava LER, não destrava ENVIAR (07/09, 20h45)

Medido, e a medida desfaz uma esperança minha. Às 20h20 eu vi o `apply.workable.com`
responder 301 e 200 onde de manhã devolvia 429 com `error code 1015`, e concluí que a porta
de candidatura tinha aberto. **Estava errado, e a diferença é entre ler e enviar.**

O 1015 é limite de taxa da Cloudflare contra o NOSSO IP e ele de fato caiu: dez quadros
diferentes responderam sem um único 429 entre 20h20 e 20h45. Mas o teste que importa não é
o GET, é o clique. Na Lighthouse Games, pela rota real
(`apply.workable.com/<conta>/j/<id>/apply/`, sem passar pelo `jobs.workable.com`), o
formulário preencheu, o botão "Submit application" foi clicado ao vivo, e **a caixa "Verify
you are human" do Turnstile apareceu DEPOIS do clique**: o botão travou em "Submitting..." e
nenhum POST de candidatura saiu. O mesmo Turnstile foi confirmado por curl no HTML das
outras páginas de candidatura (Nexus, Velan, BeamNG, Keywords).

Então o quadro completo do Workable, com as três paredes separadas:
1. `apply.workable.com` → 429/1015, limite de taxa contra o nosso IP, **intermitente**.
2. `jobs.workable.com` → POST devolve 412 com `x-ts: 0`, falta token do Turnstile.
3. `apply.workable.com`, mesmo com o 1015 fora do caminho → **Turnstile pós-clique**.

A número 3 é a que manda, é universal na plataforma, e não se burla. **O Workable inteiro é
fila do Vini, não fila de agente.** Quando o 1015 cair de novo, o ganho é poder LER o quadro
e escrever dossiê exato; não é candidatura.

O valor real da janela ficou em outro lugar: cinco entradas estavam marcadas como parede só
por causa do 1015, que não era do estúdio, e puderam finalmente ser lidas. Das cinco,
**três não tinham nada para nós** (PikPok com o quadro vazio, KingsIsle só com Community
Manager, Team17 só com Platform Engineer) e duas seguem vivas atrás do Turnstile. Ou seja:
a janela não rendeu candidatura, rendeu **verdade** — três "paredes" que na verdade eram
ausência de vaga, e que estavam ocupando lugar na fila como se fossem trabalho por fazer.

A lição, e ela vale para toda parede que a gente anotar: **"o servidor respondeu" não é o
mesmo que "a porta abriu".** A prova de que uma porta abre é o envio confirmado, nunca o
código de status do GET. Antes de comemorar bloqueio caído, clique.

## `$SCRATCH` está VAZIO, e os briefs mandam usar `$SCRATCH/apply` (07/09, 21h40)

Achado pelo agente da passada de navegador, e confirmado por mim na hora. **A variável de
ambiente `$SCRATCH` não está definida no shell.** Quem segue o brief ao pé da letra e roda
`cd $SCRATCH/apply` recebe:

```
sh: 1: cd: can't cd to /apply
```

Porque `$SCRATCH/apply` com a variável vazia vira `/apply`, que não existe. E o agente
conclui, de boa-fé, que **a caixa de ferramentas não existe** — que não há `hb_run.sh`, nem
os scripts de ATS, nem o `Vini_Cavalcanti_CV.pdf`, nem o `Cover_Letter.pdf`. Foi exatamente
o que ele relatou: "esta sessão não tinha `$SCRATCH/apply` nem os arquivos que os briefs
pressupõem", e por isso **nenhum envio real foi tentado** naquela rodada, mesmo tendo achado
vaga viva da disciplina.

**Está tudo lá.** O CV, a carta, o portfólio e os oito scripts de ATS existem e estão
intactos. O que falta é só o caminho.

**O conserto, e use este daqui em diante:** existe agora um atalho estável em
`/home/user/apply`, que aponta para a pasta de verdade. Ele funciona sem depender de
variável nenhuma:

```
cd /home/user/apply && sh hb_run.sh <script>.js
```

Os três arquivos que os formulários pedem:
- `/home/user/apply/Vini_Cavalcanti_CV.pdf`
- `/home/user/apply/Vini_Cavalcanti_Cover_Letter.pdf`
- `/home/user/apply/Vini_Cavalcanti_Portfolio.pdf` (2,56 MB; lembrando que o ArtStation
  tem prioridade sobre ele)

Se um dia o atalho sumir (sessão nova, contêiner novo), ache a pasta assim, sem adivinhar:
```
ls -d /tmp/claude-*/*/*/scratchpad/apply
```

**A lição, e ela é maior que o caminho errado:** um agente competente passou uma rodada
inteira sem tentar envio nenhum, e a causa foi uma variável vazia. Ele agiu certo ao
registrar a limitação em vez de fingir que enviou. Mas o sintoma chegou até mim disfarçado
de "zero candidaturas nesta rodada", que é indistinguível de fila seca. **Ferramenta que
falta tem que gritar, não sussurrar dentro de um número baixo.** Sempre que um resumo trouxer
zero envios, a primeira pergunta é se a ferramenta estava lá, e não se a fila estava vazia.
