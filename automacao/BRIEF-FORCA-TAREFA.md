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
