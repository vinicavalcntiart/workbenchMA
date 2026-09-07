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
