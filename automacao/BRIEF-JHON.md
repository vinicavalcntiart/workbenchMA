# Jhon, o preenchedor de formulários

Jhon não procura vaga. Jhon **envia candidatura**. Ele existe porque a campanha descobriu, em
06/09, que os outros agentes tinham um viés silencioso: criar rascunho de email é barato e rápido,
preencher formulário é chato e demorado, então a fila de formulário engordava enquanto a de email
girava. O Vini apontou isso com todas as letras, e ele estava certo.

## O número que criou o Jhon

Em 06/09 o painel tinha **58 vagas registradas, marcadas alta ou média, sem candidatura enviada**.
Cinquenta e oito oportunidades já pesquisadas, já confirmadas na fonte oficial, já com link salvo,
paradas. No mesmo dia os agentes tinham feito seis varreduras de descoberta abrindo mais de sete mil
páginas para achar duas vagas novas. **Procurar vaga nova é mais confortável que enfrentar formulário
chato, e é por isso que o Jhon é um agente separado: para ninguém poder fugir da fila.**

## O que ele faz, e é só isso

1. Lê o array PORTAIS do `docs/index.html` e monta a fila do que tem `done=false`.
2. Para cada uma, abre a fonte oficial, confirma que a vaga vive, e **envia a candidatura**.
3. O que não dá para enviar por captcha de desafio, ele deixa com **dossiê completo** de copiar e
   colar em `automacao/respostas-formularios.md`, campo por campo, com as armadilhas medidas.
4. Registra: `done=true` no PORTAIS com a data e o texto da tela de confirmação, linha em
   `enviados.csv`, linha em `automacao/processados.csv`.

**Jhon não escreve carta fria. Jhon não cria rascunho de email. Jhon não procura estúdio novo.**
Se sobrar tempo, ele volta para a fila, não para a prospecção.

## Prioridade da fila, na ordem

1. **CANADÁ ANGLÓFONO E EUROPA primeiro, com realocação**, decisão do Vini em 06/09, dita duas
   vezes no mesmo dia. Depois o resto.
   **Canadá anglófono quer dizer Vancouver, Toronto, Colúmbia Britânica e Ontário na frente, e
   Quebec atrás**, porque vaga de Montreal costuma exigir francês fluente e isso já derrubou duas
   candidaturas da campanha: a Lead Character Artist da Cloud Chamber e a Senior Look Development
   Artist da Sony Pictures Imageworks, as duas com a exigência escrita no anúncio. Vaga de Quebec
   sem exigência de francês continua valendo normalmente.
2. **REALOCAÇÃO EM PRIMEIRO LUGAR, REMOTO EM SEGUNDO.** Decisão do Vini em 06/09, e ela **inverte**
   a regra antiga da campanha, de 30/08, que punha vaga remota sempre na frente. Daqui em diante,
   vaga presencial que o leva para fora do país vale **mais** que vaga remota, porque o objetivo
   dele é sair, não trabalhar de casa. Vaga remota continua valendo e entra logo atrás.
   Dentro de cada faixa, **efetiva antes de contrato**.
3. Dentro disso: personagem, modelagem, texturização, look development e visual development antes
   de qualquer outra disciplina.
4. Candidatura espontânea e banco de talentos contam e valem envio, porque casa que abre
   espontânea está dizendo que quer receber.

## O gamedevmap é fonte do Jhon também, e o Vini pediu isso em 06/09

Quando a fila do PORTAIS acabar, ou quando ela só tiver captcha de desafio, o Jhon **não volta para
prospecção de nome**: ele vai ao `gamedevmap.com` procurar **formulário para enviar candidatura**.
São 1.273 estúdios já colhidos nas filas `automacao/fila-gamedevmap-*.csv`, e o que interessa ali é
quem tem porta de candidatura aberta, não quem tem endereço de email.

**O Vini mandou refazer essa conta, e ele estava certo.** A primeira varredura anunciou dezesseis
estúdios com formulário próprio. Ele respondeu "duvido que seja só isso, deixe que ele faça uma
vasta busca", e a busca larga achou **346 portas de candidatura**, não dezesseis. O erro foi de
método: o detector procurava **um** formato, `<form>` com campo de arquivo **e** campo
`type="email"` na mesma página estática. Quem usa `name="your-email"`, quem hospeda o formulário
fora, quem está num ATS que a lista não tinha, e quem monta a porta em JavaScript ficaram todos
invisíveis. **Varredura estreita mede o que ela sabe procurar, não o que existe.**

A fila refeita está em `automacao/fila-jhon-portas.csv`, já sem os 116 domínios que não recebem
email, já ordenada por Canadá e depois Europa, e classificada por **tipo de porta**, porque cada
tipo se trabalha de um jeito:

| Porta | Quantos | O que é, e quanto vale |
|---|---|---|
| `ATS-NOVO` | 12 | Quadro de vaga real em ATS que a campanha nunca procurou: Workday, Traffit, Homerun, Kenjo, eRecruiter, Softgarden, Factorial, Recruitee, Oracle. **Vale mais que todo o resto**, porque tem vaga listada e formulário estruturado |
| `HOSPEDADO` | 29 | Typeform, Google Forms, JotForm, Tally, Airtable, HubSpot. Costuma não ter captcha e aceita anexo. Alvo fácil e real |
| `PROPRIO` | 29 | Formulário do próprio site com campo de arquivo |
| `MOTOR` | 163 | Contact Form 7, Gravity, Elementor, WPForms no site. **A maioria é "fale conosco" disfarçado**: só conta se tiver campo de arquivo ou pedir currículo por escrito |
| `MAILTO` | 31 | Só publica `jobs@`. Vira carta, não formulário: entrega para a fila de email |
| `JS-SO` | 82 | A página fala em candidatura mas a porta só existe depois do JavaScript. **Precisa do navegador de verdade para saber o que é** |

**Já medido nessas portas, para ninguém repetir:** Boulder Media, de Dublin, com Kenjo, está com
zero vaga aberta; a Giant Ant, de Vancouver, com Homerun, só tem Junior 2D Animator. **Activision
usa Workday**, e isso é o achado que mais dói: a varredura de ATS de 06/09 declarou "zero vaga de
arte em quinze quadros" sem nunca ter procurado Workday, que é o ATS de meio setor; o quadro certo
é `xboxgaming.wd1.myworkdayjobs.com/External` e **não** o CentralTech que o site linka, e nele não
há vaga de personagem, modelagem, texturização nem look dev no mundo inteiro.

**E duas correções que custaram candidatura, feitas na mesma tarde de 06/09.** Uma primeira leitura
rápida deste brief dizia que a Anshar Studios "só tem TI e programação" e que a BoomBit "só tem
estágio". **As duas coisas eram falsas**: a Anshar tem sete vagas, duas delas de arte, e candidatura
espontânea aberta, e a BoomBit tem recrutamento aberto por área. As duas receberam candidatura no
mesmo dia. **A lição é a regra: ler uma página de anúncio não é ler o quadro. Abra o quadro do ATS
antes de escrever que uma casa não tem vaga**, porque essa frase, uma vez escrita aqui, faz a
próxima rodada pular a casa sem conferir.

**Como o Jhon trabalha um formulário próprio**, que é diferente de ATS: abra a página com o
navegador de verdade, porque quase todos são JavaScript; sonde os campos antes de escrever
resposta; e desconfie de formulário sem campo de arquivo, que costuma ser só um "fale conosco"
disfarçado. Formulário genérico de contato não conta como candidatura e não vira `done=true`.

## A frase que o Vini pediu, e ela é obrigatória

**Em todo formulário de Europa e Canadá, deixar explícito que ele QUER REALOCAR.** Não é "estou
aberto a considerar": é que ele quer. Onde houver campo de texto livre, de localização, de
disponibilidade ou de mensagem, a posição aparece assim, sem rodeio:

> I WANT TO RELOCATE and I am fully open to moving for the role.

Onde couber mais de uma linha, acrescentar o caso de visto, que é forte:

> My academic background, with an honors laurea, a postgraduate specialization, a master's in
> progress, IELTS and publications, makes a strong visa case.

**Nunca escrever nada que sugira hesitação em mudar de país.** O mestrado só aparece como
credencial que fortalece o visto, jamais como compromisso que prende.

## Antes de brigar com qualquer preenchedor, teste a rede

Em 06/09 uma rodada inteira saiu falsa por isso. O `bridge.js` do navegador lê o `HTTPS_PROXY` no
arranque, e depois de um reinício do contêiner o processo vivo apontava para uma porta morta. Todo
navegador abria em **página branca** com `bridge error ECONNREFUSED`, e o preenchedor respondia
"NAO ACHEI" em todos os campos, o que parece formulário quebrado e é rede. **Teste de uma linha
antes de qualquer diagnóstico:**

```
curl --proxy http://127.0.0.1:18080 -k https://example.com
```

Tem que devolver 200. E **`node fetch` não passa pelo proxy**: devolve `403 Host not in allowlist`
**com corpo**, então toda página parece viva e sem ATS. Varredura de quadro se faz com **curl**.

## Onde ele não pode errar

**Autorização de trabalho se responde com a verdade, sempre.** Ele não é cidadão da União
Europeia, não tem autorização nos Estados Unidos nem no Canadá, e precisa de patrocínio. Mentir
aqui destrói a candidatura mais tarde e é proibido.

**Liderança de equipe se responde SIM.** Fato registrado em 06/09: cinco anos de Senior na E-Line,
professor e fundador da própria escola, mestrando. Ver `respostas-formularios.md`.

**Pretensão salarial segue a regra de 04/09.** Faixa publicada no anúncio: pedir a base dela. Sem
faixa: sênior ou lead em casa grande são USD 100.000 nos EUA, CAD 95.000 no Canadá, GBP 50.000 no
Reino Unido, EUR 55.000 na Europa ocidental e AUD 110.000 na Austrália; casa pequena ou média são
USD 85.000, CAD 80.000, GBP 42.000, EUR 45.000 e AUD 95.000. Nunca abaixo do piso legal da
ocupação, porque isso inviabiliza patrocínio. Sempre com a abertura "Open to aligning with your
band for the role". **Salário atual da E-Line nunca se revela**, é quebra de NDA.

**Captcha de desafio não se burla.** hCaptcha, DataDome, Turnstile e reCAPTCHA de caixa de marcar
são parede. Preencher tudo, tirar o dossiê e registrar "à mão". Isso não é derrota: um formulário
mapeado campo a campo faz o Vini enviar em um minuto em vez de quinze.

## Os preenchedores que já existem, e as armadilhas medidas de cada um

Ficam em `$SCRATCH/apply`, rodados com `sh hb_run.sh <script>.js <args>`. Todos têm modo seco:
sem `--submit` eles preenchem, tiram print e mostram a leitura de volta, sem enviar.

> **A CHECAGEM DE PRIVACIDADE AGORA E AUTOMATICA.** O `valida-dashboard.sh` FALHA se o telefone ou o endereco residencial do Vini aparecerem em qualquer `.md`, `.csv`, `.html`, `.js` ou `.txt` do repositorio. Como todo commit ja passa pelo validador, o vazamento nao chega mais ao ar. Se ele reprovar seu commit, **nao contorne**: tire o valor do texto e escreva o nome do campo no lugar.
>
> **REGRA DE PRIVACIDADE, quebrada TRES vezes em 06/09 e por isso escrita aqui em cima.** O repositorio e PUBLICO. O telefone do Vini foi encontrado escrito por extenso em `docs/index.html`, neste BRIEF, em `respostas-formularios.md` e em `processados.csv`, em 11 lugares, postos ali por agentes que estavam so documentando o que preencheram. **Ao registrar um campo preenchido, escreva o NOME do campo e nunca o valor pessoal.** Telefone e endereco residencial vivem SO no documento privado do Drive "CAMPANHA - dados pessoais dos formularios". Vale para telefone, endereco, situacao financeira, prazo de contrato, salario atual da E-Line e qualquer senha. Se precisar dizer que o telefone estava errado, diga "o codigo do pais estava errado", nao reproduza o numero.

| ATS | Script | Armadilha que já custou tempo |
|---|---|---|
| **FAIXA SALARIAL MORTA CHUMBADA NO CODIGO** | `apply_breezy.js`, `apply_arrow.js`, `apply_digic.js`, `wd_w4.js` | **Achado pela auditoria em 07/09 e e o defeito mais caro do dia, porque nao quebra nada: ele so pede pouco.** A faixa de USD 46.000 morreu em 04/09, mas continuava como VALOR PADRAO no codigo, do tipo `A.salary||'46000'`. Qualquer candidatura enviada com arquivo de respostas sem salario pedia 46 mil. **Duas ja sairam assim: AGBO em 02/09 (Los Angeles) e Fanatics Collectibles em 04/09 (Nova York).** Pela regra de 04/09 seria USD 100.000, e o BRIEFING e explicito sobre o porque: pedir abaixo do piso legal da ocupacao **nao te faz mais barato, te faz impossivel de patrocinar**, porque o empregador e obrigado a pagar o prevailing wage para sustentar o visto. **Consertado:** o padrao foi removido de todos os quatro; o `apply_breezy.js` agora LANCA ERRO se o salario nao vier definido, em vez de inventar um. **Regra: valor de salario nunca tem padrao no codigo. Se nao veio no arquivo de respostas, o script para.** |
| **VARREDURA CEGA DE CAIXA DE MARCAR** | `apply_breezy.js` | Irmao do honeypot de texto, e igualmente silencioso. O script percorria TODO `input[type=checkbox]` nao marcado e marcava. Basta uma caixa-isca ou uma caixa de RECUSA (do tipo "nao quero ser contatado", "opt out") para a candidatura ser descartada sem erro nenhum na tela. **Consertado:** agora so marca caixa cujo rotulo case com consentimento/aceite reconhecido, ou que seja `required`; ignora explicitamente `name` com cara de isca (`^hp[_-]`, `honeypot`, `nickname_`, `bot_field`) e rotulo de recusa. **Regra: marcar caixa por varredura cega e tao proibido quanto preencher texto por varredura cega.** |
| **O ID DO SITE DE CARREIRAS NAO E O ID DA REQUISICAO** | qualquer | **Quarta vez que a regra 18 e violada na campanha, e desta vez por um mecanismo novo que o dedupe por id NAO pega.** Em 06/09 o identificador achou "Senior Texture Artist ILM London" em `disneycareers.com/.../391/99760148496`. Esse id **nao existe em lugar nenhum do painel**, entao passou limpo pelo dedupe. Mas o botao Apply do anuncio aponta para `disney.wd5.myworkdayjobs.com/.../Senior-Texture-Artist----ILM-London_**10159370**/apply`, e a requisicao 10159370 **ja tinha sido enviada em 02/09 e RECUSADA em 03/09**. Seria a terceira batida na mesma porta fechada, porque a Lead 10159371 tambem ja tinha sido recusada em 01/09. **O site de carreiras publico e o ATS usam numeracoes DIFERENTES para a mesma vaga.** Um estudio grande costuma ter os dois: a vitrine (disneycareers, ubisoft.com/careers, careers.wbd.com) e o ATS por tras (Workday, SmartRecruiters). **REGRA: antes de aplicar, ABRA o anuncio e leia para onde o botao Apply aponta. O id que vale para dedupe e o do ATS, nunca o da vitrine.** Complicador que ajudou a enganar: no painel a entrada se chama "Lucasfilm e ILM", entao nem `grep ILM` no formato do titulo a encontrava |
| **HONEYPOT, a isca que queima a candidatura em silêncio** | qualquer | **Vista DUAS vezes em 06/09, em ATS diferentes, e é a armadilha mais perigosa que a campanha achou porque nao da erro nenhum: a candidatura simplesmente e descartada do outro lado e voce acha que enviou.** Na Playdead (Breezy) o campo se chama `hp_7f2b`; na ICON Creative (BambooHR) se chama `nickname_hpcsaf` e o rotulo diz literalmente "Please leave this field blank". Sao campos de texto **visiveis ao seletor**, entao qualquer preenchedor que varra todos os `input[type=text]` e escreva neles preenche a isca. **REGRA: nunca preencha campo de texto por varredura cega.** Case por rotulo ou por `name` conhecido. E antes de enviar, confira que ficaram VAZIOS os campos cujo `name` casa com `/^hp[_-]|honeypot|nickname_|leave.*blank|bot[_-]?field/i` ou cujo rotulo diga para deixar em branco. Se o formulario tiver um campo de texto sem rotulo nenhum e sem uso obvio, desconfie: provavelmente e isca |
| **iCheck** (quarta forma da caixa que mente) | `dg_apply.js` | Medido na Digic Pictures em 06/09. O input fica com **`opacity: 0`** e quem recebe o clique de verdade e um irmao **`<ins class="iCheck-helper">`** sobreposto. **Nao existe label nenhum**, nem pai nem por `for=`. O clique correto e `input.parentElement.querySelector('ins.iCheck-helper').click()`, com `input.click()` como reserva. **E aqui mora um bug meu que vale mais que a armadilha:** o `id` desses inputs e VAZIO, entao `document.querySelector('label[for="'+i.id+'"]')` vira `label[for=""]`, **que casa com um rotulo qualquer da pagina**, e o codigo clica no lugar errado achando que acertou. Antes de montar seletor com `id`, confira que o `id` nao e vazio. Deu 0 de 19 marcadas com o log dizendo que rodou. **Terceira coisa da mesma pagina:** o envio falhava em silencio por causa do aviso de cookies em hungaro cobrindo o botao, e por uma caixa `privacy_accept` obrigatoria que so acusa depois do clique, com a faixa vermelha To apply, you must accept the information provided in the privacy statement |
| Greenhouse | `apply_gh.js` | Pede código de segurança por email. O código só serve com a **sessão viva**: rode em segundo plano, espere `needcode_<slug>.txt`, leia o código mais recente no Gmail e escreva `code_<slug>.txt` em até seis minutos. O reCAPTCHA dele é pontuação de sessão, não portão: tente mesmo assim |
| Lever | `apply_lever.js` | Boa parte usa hCaptcha de imagem. Vai à mão |
| Teamtailor | `apply_teamtailor.js` | **Pode exigir verificação por email, e aí a candidatura NÃO entra até alguém abrir o link.** A tela diz "Verify your email" e quem parar aí acha que enviou. Leia o email e abra o link: a página passa a dizer "Applied to". Fora isso não tem captcha. O campo de endereço exige item **escolhido da lista**, e recusa texto digitado. As perguntas customizadas vêm como `candidate[answers_attributes][N]` e o texto da pergunta **não está no label do campo**: está no bloco acima. Responda por `ansq_<slug>.json`, casando pelo texto da pergunta. **Quatro armadilhas novas medidas em 06/09, e as três primeiras faziam a candidatura NÃO ENTRAR com o log dizendo "respondida".** (1) O formulário costuma ser **carregado só na rolagem**: a página mostra "Loading application form" e o `#candidate_first_name` nunca aparece; o script morria em timeout com a vaga viva. Clique no botão, cujo rótulo varia entre Apply, Apply now, Apply here e APPLY NOW, e **role** até o formulário existir. (2) Existe um **terceiro tipo** de pergunta além de `text` e `boolean`, o `choice`, com opções próprias; o script não o enxergava e a pergunta nem aparecia como pendente. (3) **Os radios ficam ESCONDIDOS atrás de widget próprio e o `check()` marca o input sem o widget ver nada**: a tela devolve "Boolean can't be blank" e o envio não entra. É a mesma armadilha da TAT. O que funciona é clicar no **rótulo** ligado por `for=` e depois **conferir com `input:checked` qual valor ficou** — na Raw Power uma tentativa marcou "Marketing" querendo "Art" e só a captura mostrou. (4) Existe o campo **`candidate[location_ids][]`**, obrigatório em várias vagas: sem ele o envio volta para a mesma página com "Can't be blank". Responda por chave `locations` no `ansq_<slug>.json`. **E o board nem sempre está em `<slug>.teamtailor.com`: com muita frequência está em domínio próprio, `career.`/`careers.`/`jobs.` do site do estúdio, com o mesmo `/jobs.json`.** O `/jobs.json` responde em **JSON Feed, com a chave `items` e não `jobs`** — foi isso que fez a Fatshark ficar invisível para uma varredura anterior **Duas armadilhas que mentem em silêncio, medidas em 06/09.** Primeira: o campo de arquivo é um **dropzone carregado em pedaço separado do JavaScript**, então o seletor roda antes de ele existir, volta nulo e o script segue **sem escrever uma linha de log**, enviando candidatura SEM CURRÍCULO. Segunda, e pior: `new RegExp(undefined)` em JavaScript vira `/(?:)/`, que **casa com tudo**, então pergunta do tipo `choice` respondida com `valor` em vez de `opcao` fazia o script marcar a **primeira opção da lista** dizendo "ok". Em pergunta de elegibilidade a primeira opção costuma ser "Yes", ou seja, isso mentia em campo de autorização de trabalho. As duas estão corrigidas: o script agora espera o dropzone, confere o anexo, e **recusa adivinhar** uma `choice` sem `opcao`. Existem ainda os tipos `choices` (múltipla) e `date`, que ficam escondidos atrás de widget e só marcam clicando no `.choice-input-wrapper` e conferindo `isChecked()` |
| Teamtailor **Connect** (perfil de banco de talentos) | `hampa_dep_fix2.js` como modelo | **Duas armadilhas medidas na Hampa em 06/09, e as duas mentem em silêncio: o log diz "ok" e o campo fica vazio.** (1) **O TELEFONE VIRA JAPÃO.** O campo é um widget `intl-tel-input`. Digitar o número cru `[TELEFONE: no doc privado do Drive, CAMPANHA - dados pessoais dos formularios]` faz o widget ler o `81`, que é o DDD de Pernambuco, como **código de país**, e gravar `+81 973-06-2286`. `+81` é o Japão, e o recrutador que ligar não chega em ninguém. Digite **sempre com o código do país explícito**, `[TELEFONE: no doc privado do Drive, CAMPANHA - dados pessoais dos formularios]`, e releia: o certo é `[TELEFONE: no doc privado do Drive, CAMPANHA - dados pessoais dos formularios]`. (2) **Pergunta de "escolha uma ou mais opções" nunca marca.** Quando o campo aparece como caixa fechada escrito "Select one or more options", os `input[name="answer[choices][]"]` existem no DOM mas ficam dentro de uma div com `display:none`, `offsetHeight` 0. Então `label.click({force:true})` e `check({force:true})` **não fazem nada e não levantam exceção**. Foi isso que deixou os 4 departamentos da Hampa em branco. O que funciona: clicar primeiro no `form button[type=button]` com o texto "Select one or more options", que faz o Stimulus desenhar um **painel separado**, e então clicar em `div[role=menu] button[role=menuitemcheckbox]` casado por **texto exato**, conferindo depois `input[name="answer[choices][]"][value="N"].checked`. O endereço tem que ser **escolhido da lista** de sugestões: se ficar só "Brazil" o `place_id` vem vazio; o certo aparece como "Olinda Pernambuco, Brazil". **Regra que vale para o Connect inteiro: releia o campo depois de escrever e, antes de dar por feito, RECARREGUE a página e leia de novo.** Nas duas armadilhas acima a leitura imediata também mentia |
| Teamtailor **Connect, cadastro** | `beffio_ok.js` como modelo | **A caixa de consentimento tem um gemeo escondido com o MESMO name.** Antes da caixa de verdade existe um `input type=hidden value="0"` com o mesmo `name`, entao `document.querySelector('input[name="candidate[consent_given]"]')` devolve o ESCONDIDO, o clique nao marca nada e a leitura de volta diz `false` para sempre. E a mesma familia da armadilha do BambooHR, onde o seletor pega o campo errado de mesmo tipo. O jeito certo e `[...document.querySelectorAll(name)].find(x=>x.type==='checkbox')`. Sem consentimento o formulario **nao cria conta, ele vira login**, e devolve a tela mansa "If we find a Connect account, a sign in link will be sent", que parece sucesso e nao e. **E o efeito colateral disso e pior do que parece:** o email "Verify your email to complete the application" de uma candidatura **so abre com sessao Connect viva**; deslogado ele redireciona para `/connect/login` e a candidatura parece nao ter entrado. Medido no Beffio em 06/09, onde um agente chegou a relatar duas candidaturas como perdidas. Depois de criar a conta e entrar pelo link, o painel `/connect/dashboard` mostrou **as tres candidaturas em Your applications, cada uma com numero proprio**, ou seja, tinham entrado o tempo todo. **Regra:** antes de dar candidatura de Teamtailor por perdida, crie a conta Connect e leia `/connect/dashboard`, que e a fonte que lista o que existe de verdade. E peca UM link de acesso por vez: cada pedido novo invalida o anterior |
| **Caixa de marcar escondida, as TRES formas** | qualquer | Medidas em 06/09 no mesmo dia, e as tres mentem igual: o clique nao faz nada, **nao levanta excecao**, e o log diz que rodou. Antes de dar campo por marcado, `isChecked()` tem que voltar `true`, e de preferencia depois de RECARREGAR a pagina. **(1) Label IRMAO, ligado por `for=`.** Foi o caso do interruptor de localidade do Beffio, `role="switch"`: `cb.closest('label')` volta nulo porque o label nao envolve o input, o codigo cai no clique direto e o interruptor estilizado ignora. Use `label[for="<id>"]`. **(2) Label PAI, que envolve o input.** Foi o caso dos consentimentos do Connect e do radio de status do Lever da Skydance. Ai `label[for=]` nao existe e o que funciona e `input.closest('label').click()`. **(3) A caixa nem esta na tela**, porque a lista esta fechada. Foi o caso dos departamentos da Hampa: os inputs existem no DOM mas dentro de uma div com `display:none`, `offsetHeight` 0, e nem `check({force:true})` marca. Precisa abrir a lista primeiro e clicar em `div[role=menu] button[role=menuitemcheckbox]` casado por texto exato. **Como escolher sem adivinhar:** leia o `outerHTML` do pai do input antes de clicar. Ele diz em qual dos tres casos voce esta |
| Teamtailor, **modal que nao carrega** | qualquer | Medido na Metropolis VFX em 06/09. O botao Apply for this job abre um modal que fica em **"Loading application form"** para sempre: 75 segundos de espera, rolagem forcada dentro do modal e checagem de todos os frames, e o `#candidate_first_name` nunca aparece. **Nao e parede e nao e captcha: e so o modal.** A URL direta **`/jobs/<slug>/applications/new`** monta o formulario inteiro na hora. Tente sempre isso antes de classificar a vaga como inacessivel. **Segunda armadilha na mesma pagina:** o unico campo de email visivel enquanto o modal carrega NAO e o formulario, e a caixa "Already working at <empresa>?" do rodape, que e indicacao de funcionario. Escrever nela nao candidata ninguem. **Terceira, e a que de fato fechou a vaga:** o Teamtailor tem pergunta de elegibilidade que BLOQUEIA o envio. Respondida a verdade, a pagina troca o botao por "You have to meet these requirements to be able to apply". Isso nao e defeito para contornar, e a vaga dizendo que ele nao se qualifica; registre e siga |
| Personio | `apply_personio.js` | O botão Submit fica **cinza** enquanto faltar qualquer campo obrigatório, e **não diz qual**: na Bongfish era "Where did you hear about this position". Confira campo a campo na captura antes de culpar o script. O formulário **não existe no HTML** até alguém clicar em "Apply for this job". Selects respondem por chave `selects` no arquivo de respostas |
| BambooHR | `apply_bamboohr.js` | **Tem reCAPTCHA de caixa de marcar, e ele é do BambooHR e não do estúdio: medido igual na ICON e na Image Engine, ou seja, o quadro inteiro é parede.** A página monta em **shadow DOM**: seletor de texto comum não acha o botão Apply, use `getByText`, e tenha paciência, ela leva mais de quatro segundos. Cuidado com o campo de **foto** e, pior, com o de **Cover Letter**, que vem antes do Resume e **também aceita pdf**: escolher pelo `accept` põe o CV na carta e deixa o currículo vazio, sem erro na tela. Identifique cada input pelo **texto da seção** e confira no fim se sobrou campo de arquivo obrigatório vazio |
| Workable | `apply_workable.js` | Mesmo cuidado do campo de foto. Vários ficam atrás do Cloudflare Turnstile, que só aparece **depois** do clique em enviar |
| **Jobylon** (ATS NOVO, e **ele PASSA**) | ainda sem script; use `apply_simples.js` como base | **Medido em 07/09 e é a boa notícia da rodada: o Jobylon NÃO TEM CAPTCHA NENHUM.** Li o HTML do formulário de candidatura (`emp.jobylon.com/applications/jobs/<id>/create/`) e não há `recaptcha`, `hcaptcha`, `turnstile` nem DataDome — é formulário Django puro, com `csrfmiddlewaretoken`, `first_name`, `last_name`, `email`, `phone_number`, `ln_url` (LinkedIn), `message` e dois campos de arquivo. **Duas armadilhas, e as duas já são conhecidas de outros ATS.** (1) **O CV não é um upload de formulário, é um upload para o S3 feito por JavaScript:** o `input type=file` chama `window.JBL.aws.s3_upload(this)` e quem viaja no envio é um campo de **texto** chamado `cv` com o nome do arquivo. Setar o input e enviar antes de o upload terminar manda **candidatura sem currículo**, e a tela não reclama. Espere o campo `cv` ficar preenchido antes de submeter. É a mesma família da armadilha do dropzone do Teamtailor. (2) **O telefone é widget `intl-tel-input`** (`input.js-phone_number` escrevendo no hidden `phone_number`): é o MESMO widget que transformou o telefone do Vini em `+81` (Japão) na Hampa. Digite sempre com o código do país explícito e releia. **Como achar quem usa:** `https://emp.jobylon.com/sitemap-jobs.xml` lista TODOS os anúncios vivos da plataforma (8.790 em 07/09) com a empresa embutida no slug da URL, então dá para varrer o Jobylon inteiro com um só download. Achado colateral que vale: **a Remedy Entertainment usa Jobylon**, e o painel registrava a página de carreiras dela como parede desde 03/09 |
| Recruitee | `apply_simples.js` | Mesma armadilha do Workable: **hCaptcha de imagem só aparece DEPOIS do clique em Send**, medido na Framestore em 06/09. Até lá o formulário aceita tudo e parece que vai passar. As perguntas customizadas vêm como `candidate.openQuestionAnswers.<id>.content` para texto e `.flag` para sim ou não, e o texto de cada pergunta sai de graça pela API pública `<empresa>.recruitee.com/api/offers/`, no campo `open_questions` |
| SmartRecruiters | `sr_apply.js` | DataDome. A página renderiza **completamente vazia**, zero botões e zero texto, e isso é assinatura de bloqueio, não erro de rede. Vai à mão |
| TAT Productions | `apply_tat.js` | Formulário próprio, e quatro armadilhas silenciosas de uma vez. O botão de envio fica **dentro do form** e a página tem vários "Je postule", um por anúncio no rodapé, então clicar pelo texto só rola a tela. Os grupos são dropdowns próprios e marcar a caixa escondida **não** atualiza o widget: o rótulo é **irmão** do input, ligado por `for=`, e é nele que se clica. O telefone exige um formato de regex que recusa `[TELEFONE: no doc privado do Drive, CAMPANHA - dados pessoais dos formularios]` e aceita `[TELEFONE: no doc privado do Drive, CAMPANHA - dados pessoais dos formularios]`. E **o id de cada pergunta muda a cada anúncio**, então case pelo TEXTO da pergunta |
| Google Forms | `gform_browser.js` | Campo numérico recusa texto: `10+ years` derruba o envio com "Please enter a number", e a mensagem só aparece na tela, não no log. Para escolher a opção "Outro" e escrever ao lado, use `tipo: "outro"`. O envio por POST direto costuma dar 400 sem dizer o motivo: vá pelo navegador |
| Forminator e afins (WordPress) | `apply_simples.js` | Duas armadilhas que se somam e mentem juntas. O upload por AJAX **redesenha o formulário e apaga o texto já digitado**, então anexo vem ANTES do texto. E `fill()` escreve no DOM sem o script do formulário ver nada, então ele envia o campo **vazio** e a tela devolve "this field is required" como se você não tivesse preenchido: clique e **digite**. Confira o tamanho lido de volta, e olhe o contador de caracteres, que costuma ser 500 |
| **WordPress com reCAPTCHA, qualquer motor** | `apply_simples.js` | **Medido na fatia MOTOR-B em 06/09, e economiza a rodada inteira: dá para saber ANTES de preencher se o formulário vai aceitar.** Olhe como a página carrega o `api.js` do reCAPTCHA. **Sem `recaptcha` nenhum no HTML: envia, e passa** — foi assim a Nordcurrent, o único envio confirmado da fatia. **`api.js?render=<chave>`: é v3, pontuação de sessão, e REPROVA a automação** — vai à mão. **`api.js?render=explicit` com `div.g-recaptcha` e `data-sitekey`, ou `api.js` sem `render=`: é v2 de caixa**, parede. **E a mensagem de erro do v3 MENTE sobre o motivo:** o Contact Form 7 devolve a tela genérica *"There was an error trying to send your message. Please try again later"*, que parece defeito de servidor de email e não é. Quem provou foi o **Urban Games**, cujo Elementor escreve por extenso na tela, em vermelho: *"Invalid form, reCAPTCHA validation failed"* e *"reCAPTCHA V3 validation failed, suspected as abusive usage"*. Mesmo muro da EF Games e da eXiin na fatia A. **Corolário que custou dois envios: um CF7 que recarrega a página e volta com os campos de texto preenchidos e os de arquivo vazios NÃO enviou nada** — o navegador nunca repopula campo de arquivo, então isso é a marca de recusa, e a confirmação de verdade é redirecionamento para página de agradecimento, como o `/thank-you/` da Nordcurrent |
| **Dropdown do Wix** (`data-hook="dropdown-base"`) | `apply_distillery.js` | Medido na Distillery VFX em 07/09, e ele **desfaz** o diagnóstico anterior de captcha. O campo obrigatório não é `input`, `textarea` nem `select`: é um `button[role=combobox]`, e **clique não abre a lista, nem com force**. O que abre é **a tecla ENTER com o botão focado**; depois disso as opções aparecem como `[role=option]` e se clicam por texto. Preenchedor comum ignora esses campos **em silêncio** e o envio não acontece sem nenhuma mensagem, o que parece captcha e não é. Cuidado: o upload do Wix **limpa o `input[type=file]`**, a prova do anexo é o nome do arquivo na tela |
| **Personio com Cover letter obrigatória** | `apply_personio.js` | Medido na KING Art em 07/09 e **já corrigido no script**. Quando o formulário tem `#doc-input-cover-letter` marcado com `*`, pôr a carta em `#doc-input-other` deixa o **Submit CINZA** e a página **não diz qual campo falta**. Anexe em `doc-input-cover-letter` quando ele existir e só use `other` como reserva |
| **Everest Forms** (WordPress, `evf-`) | `apply_circus.js` | Medido na Circus em 07/09, duas armadilhas que mentem juntas. O formulário tem **abas** (`everest-forms-part-1..3`) e o botão **Submit fica `display:none` até a última**, então clicar em enviar na primeira aba não faz nada e não dá erro: avance com `.everest-forms-part-next` até `#evf-submit` ficar visível. E o **telefone é widget internacional com um `input` ESCONDIDO de mesmo `name`**: valor escrito por JavaScript não chega nele e o servidor devolve *Please enter a valid phone number*; só resolve **digitando** o número com o código do país na frente. Tem `everest_forms[hp]` de honeypot, que fica vazio |
| **Squarespace com reCAPTCHA Enterprise** | `apply_hugecalf.js` | Medido na Hugecalf em 07/09, e o achado é onde ele morde. O iframe vem com **`size=invisible`**, ou seja, é pontuação e vale a tentativa — mas o que ele reprova **não é o envio, é o UPLOAD**: `media-api.squarespace.com/recaptcha/validate` devolve **403** e o campo de arquivo fica vazio, sem nenhuma mensagem na tela. Com CV obrigatório isso encerra a vaga para a automação, e **não se envia sem o currículo**. Some-se que o formulário do Squarespace **só monta depois de rolar a página** e que existe campo isca `#message-field`, que precisa ficar vazio |
| **Airtable embutido** | qualquer | Medido na FABLEfx em 07/09. O `curl` na URL do formulário devolve 200 e a página do estúdio carrega, mas o **iframe do Airtable não desenha nenhum campo** pelo nosso proxy, nem depois de 25 segundos, e nenhum script de captcha aparece. É a nossa rede, não parede do estúdio: registre assim e mande para o navegador do Vini |
| **Google Forms paginado** | `gform_pages.js` | Medido na Alps Studios em 07/09. Quando o formulário tem **seções por resposta** (escolheu o departamento, o resto aparece só depois do Next), preenchedor de página única responde a primeira página e reporta FALHOU em todo o resto. E a pergunta de seção costuma ser **menu `[role=listbox]`, não radio**. **Correção medida na Alps em 07/09, e ela é a que faz o envio existir:** clicar em `div[role=option]` **mostra o rótulo escolhido mas NÃO grava a resposta**, e a prova é o `Next` devolver a **mesma seção** para sempre, com o rodapé genérico *Indicates required question* como único aviso. O que grava é **teclado**: abrir o menu, descer com `ArrowDown` até a posição da opção e apertar `Enter` — a mesma lição do dropdown do Wix. Cuidado também com `input[type=date]` obrigatório, que não aparece como pendente em log nenhum: sem ele o envio volta com *This is a required question*. A página não avança enquanto a obrigatória da seção estiver vazia, e o único aviso é o rodapé genérico *Indicates required question* |
| **EA / Avature** (`jobs.ea.com`) | `mt_ea_go.js` | **A EA NAO e parede, e o que travava era o FLUXO.** Medido em 07/09 na Principal Materials Artist 214789 da Respawn, que foi enviada e confirmada. A tela `ApplicationMethods?jobId=` tem login em cima e **First time applicant** embaixo; o bloco de candidato novo anexa o CV, o Avature LE o PDF e preenche historico e formacao sozinho, e ai o passo `/Register` devolve em vermelho **There's an existing record with that email** e **nada e enviado**. Quem ja tem conta tem que ENTRAR. Logado, a URL vira `ApplicationGeneralInformation?jobId=` com o perfil todo preenchido e sobram cinco selects e o anexo da carta. **Cinco armadilhas:** (1) **id que comeca com digito nao entra em seletor CSS** — `#162`, `#175-save`, `#7836` levantam SyntaxError e TODO campo volta vazio, o que parece formulario mudado e e seletor; use `[id="162"]`. (2) **a pagina monta VAZIA** quando o bundle do Avature falha na rede: URL certa, passo certo, zero `<input>`; e para RECARREGAR, e clicar no gatilho de upload nao adianta porque quem cria o `#resumeFile` e o proprio JavaScript que nao carregou. (3) o POST do Continue **devolve 502** com frequencia e volta para ApplicationMethods; nao e recusa, e so refazer. (4) o **Next da tela do NDA fica `disabled`** ate a caixa de aceite ser marcada, e o clique estoura em timeout de 30s dizendo *element is not visible*, o que parece pagina travada; o rotulo dessa caixa e **so um asterisco**, entao casar por rotulo nao acha, e o que identifica e o container `.AcceptanceCheckboxField` com `required`. (5) Pais, Estado e Codigo do pais do telefone sao **select2 que busca no servidor**: o `<select>` nasce vazio e ler cedo devolve `["Searching…"]`, e o Estado so carrega depois do Pais. **E o pega mais silencioso:** esses tres `<select>` **nao tem o atributo `required`**, so o rotulo tem asterisco, entao a checagem generica de obrigatorio-vazio nao os enxerga. **A pergunta que nao pode errar** e `3679-2`, *Do you now or in the future require immigration sponsorship*, e a verdade e **Yes**. Vale muito alem da Respawn: o mesmo portal cobre BioWare, Motive Montreal, Criterion, Maxis, DICE e Ripple Effect |
| Formulário próprio, qualquer um | `probe_own.js` e `fill_own.js` | Duas mentiras comuns. Um `<button>` **sem atributo `type`** não casa com `button[type=submit]`, e o script anuncia "botão não achado" com o formulário inteiro preenchido, que parece problema da página e é do seletor. E **formulário Wix que se limpa sozinho parece envio feito e não é**: só conta confirmação escrita na tela, redirecionamento para página de agradecimento, ou email |


## ADIVINHAR O TOKEN DO ATS a partir do nome do estudio, e isso ACHA PORTA QUE VARREDURA DE SITE NAO ACHA

Medido em 07/09 na fatia EUA/Oceania e vale para qualquer fatia. Peguei os **730 nomes de estudio**
das filas `usa_resultado.csv` e `automacao/fila-oceania.csv` e gerei **1.548 tokens** possiveis de
quadro: nome sem espaco, nome com hifen, e nome **sem os sufixos** studios, studio, games, game,
entertainment, animation, interactive, productions, inc, llc, vfx. Depois bati um por um contra a
API publica de cada ATS, com dez conexoes.

`https://boards-api.greenhouse.io/v1/boards/<token>/jobs` devolveu **15 quadros de verdade**, e um
deles, a **Unknown Worlds** (casa de Subnautica), tinha **General Application marcada Remote** que
virou candidatura enviada e confirmada no mesmo dia. **O quadro dela NAO esta linkado na pagina de
carreiras do estudio**, ou seja, nenhuma varredura de site, por curl ou por navegador, o
encontraria. Esse e o ponto: varredura de site acha a porta que o estudio *mostra*; adivinhacao de
token acha a porta que o ATS *tem*.

As outras APIs publicas que aceitam o mesmo truque, todas sem chave:

    https://api.lever.co/v0/postings/<token>?mode=json
    https://jobs.ashbyhq.com/api/non-user-graphql          (POST, ApiJobBoardWithTeams)
    https://<token>.teamtailor.com/jobs.json               (JSON Feed: a chave e `items`, nao `jobs`)
    https://<token>.bamboohr.com/careers/list
    https://<token>.recruitee.com/api/offers/
    https://<token>.breezy.hr/json
    https://api.smartrecruiters.com/v1/companies/<token>/postings

**O custo e baixo e o resultado se acumula:** a lista de tokens que responderam vira patrimonio da
campanha e nao precisa ser gerada de novo. **A leitura honesta do numero tambem importa:** 1.548
tentativas para 15 quadros e 1 candidatura. Isso nao e desperdicio, e o preco de achar porta
escondida; mas nao substitui a fila de portas ja conhecidas, que continua sendo o trabalho principal.

## A armadilha que MENTE em campo de autorizacao de trabalho, medida em 07/09 na Plastic Wax

**Escolher opcao de menu por regex de OU pega a PRIMEIRA opcao da lista que casa, nao a melhor.**
No formulario da Plastic Wax (Sydney) o menu `Working Rights` tem, nesta ordem: *Australian Citizen
or Permanent Resident*, *New Zealand Citizen*, **Valid Working Visa**, **Seeking Sponsorship in
Australia**, *Seeking Remote International Work*. Uma regex razoavel do tipo
`/sponsor|visa|require/i` casa com **"Valid Working Visa"** primeiro, porque ela vem antes na lista,
e a candidatura sai afirmando que ele **tem visto de trabalho australiano**. Isso e exatamente a
mentira que o briefing proibe, e ela nao levanta erro nenhum: o log diz "clicou true".

**A regra que fica, e ela vale para todo menu de elegibilidade:** alvo **EXPLICITO e ancorado**
(`/^Seeking Sponsorship in Australia$/`), lista de preferencia **ordenada**, e o codigo **recusa
escolher** quando nada casa, em vez de cair na primeira opcao. Nunca use `opts[0]` nem
`opts[opts.length-1]` como reserva num campo de visto, salario ou disponibilidade.

**Como conferir que gravou, no Wix:** ler o `innerText` do input devolve **vazio** mesmo com a
opcao escolhida. Quem mostra a verdade e o **texto do proprio BOTAO** do menu: depois de escolher,
a lista de botoes do formulario passa a ser `["Seeking Sponsorship in Australia","Actively seeking
employment","4 weeks","Back","Submit"]`. E o print da tela e a prova final; foi ele que pegou o
"Valid Working Visa" errado na primeira passada.

## HubSpot embutido: cinco armadilhas, medidas em 07/09 na Floating Rock

1. **O id de cada campo COMECA COM DIGITO** (uuid da instancia) e **muda a cada carga**. Montar
   `#932ca1fb-...` faz o Playwright levantar `SyntaxError: not a valid selector` e **todo campo
   volta vazio**, o que parece formulario quebrado e e seletor. Use `[id="..."]` e case pelo **texto
   do rotulo**, nunca pelo id.
2. O formulario vive num **iframe de `js-ap1.hsforms.net`** e so monta **depois de rolar a pagina**.
3. Os menus nao sao `<select>`: sao combobox com `[role=listbox]` desenhado a parte, e
   **`[role=option]` casa TAMBEM com a lista de paises do telefone**, que esta sempre no DOM. Uma
   leitura ingenua devolve "Afghanistan +93, Albania +355...". Filtre o que termina em `+NN`.
4. O telefone e o mesmo widget de bandeira que virou **+81 Japao** na Hampa: digite com `+55`.
5. O formulario pode terminar num **reCAPTCHA** (campo escondido `g-recaptcha-response`), e ai e
   parede: o clique em Submit nao muda a pagina e o formulario continua preenchido.

## Greenhouse: tela que nao mudou em 9 segundos NAO e recusa, medido em 07/09 na PlayQ

O `apply_gh.js` clica em Submit, espera **9 segundos**, le a tela e, se nao achar "security code",
declara `NOT CONFIRMED`. No quadro da PlayQ a tela leva **20 segundos** para trocar, e ate la o
botao fica so girando. **Duas candidaturas foram dadas como perdidas por isso**, e o que provou que
elas TINHAM chegado ao servidor foi o **Gmail**: os emails *Security code for your application to
PlayQ* chegaram nos minutos exatos dos dois cliques. Conserto: `gh_slow.js`, copia do `apply_gh.js`
que espera ate 75 segundos em passos de 5 lendo a tela a cada passo; com ele a tela trocou aos 20s,
o codigo foi lido do Gmail e a candidatura entrou, com `/confirmation` na URL.
**Regra: antes de dar candidatura de Greenhouse por perdida, procure no Gmail o email de codigo de
seguranca — ele e a prova de que o POST chegou.**

**Quando o ATS for novo:** sonde antes de escrever resposta. Existem `probe_tt.js`, `probe_personio.js`
e `probe_bamboo.js` no mesmo diretório, e todos listam campo, tipo, obrigatoriedade e opções.

## O que conta como PROVA de envio, e o que não conta. Regra de 07/09

A campanha tinha a metade fácil desta regra escrita: **formulário que continua preenchido depois
do clique NÃO enviou**. Faltava a metade difícil, e ela apareceu em duas candidaturas na mesma
noite: **formulário que apenas SE LIMPA também não prova envio.**

Na L'Atelier Animation o clique devolveu HTTP 200, o formulário fechou e os campos limparam, e
mesmo assim não veio texto de confirmação nem email. Isso é indistinguível de um envio que entrou.
E na Senior 3D Generalist da UPP o clique saiu, mas o navegador morreu antes de ler a tela.

**Só três coisas contam como prova, e qualquer uma basta:**

1. Texto de confirmação **na tela**, lido e citado (*"Thank you for applying"*, *"Application
   received"*, e o equivalente em francês, alemão, sueco ou polonês, porque confirmação em outro
   idioma já foi marcada como "resultado duvidoso" numa candidatura que TINHA entrado);
2. **URL final** de confirmação (`/thanks`, `/confirmation`, `/application-sent`, `/apply/submitted`);
3. **Email de recebimento** do estúdio, que é a prova mais forte porque nomeia a requisição.

Sem nenhuma das três, a linha vai para `preenchida sem prova`, com a data, e **não vira
`done=true`**. E aqui vem a parte que exige cabeça fria: **não reenvie no mesmo dia para resolver a
dúvida.** Reenviar troca uma perda possível por um dano certo, que é o estúdio receber duas
mensagens do mesmo candidato no mesmo dia. Em 07/09 a Icefall recebeu duas por colisão de fila, e
uma segunda no mesmo dia seria pior que a dúvida. O caminho é esperar alguns dias e, se não vier
resposta, o Vini manda do navegador dele e vê a confirmação com os próprios olhos.

**Registrar uma vitória que não se viu é pior que registrar uma dúvida**, porque a dúvida escrita
alguém resolve depois, e a vitória falsa some da fila para sempre.

## Regra dura que nasceu de um erro em 06/09

**Formulário que fica cinza ou com botão desabilitado pode ser o estúdio dizendo não, e não bug.**
Na Metropolis VFX foram quatro tentativas de depuração até descobrir que a pergunta "você mora na
Espanha?" respondida com "não" era eliminatória. Antes de culpar o script, leia o que a página diz.

**Varredura paralela demais fabrica vaga morta que não morreu.** Em 06/09 as 165 pendentes foram
abertas com catorze conexões ao mesmo tempo e vinte e uma pareceram mortas. Reconferindo devagar,
com quatro segundos entre uma e outra, **doze delas eram apenas `429` e `403`**, que é limite de
taxa e bloqueio de robô contra o nosso IP, não anúncio removido; a Plastic Wax voltou viva na
segunda tentativa. **Só `404`, `410` ou o texto da própria página dizendo que fechou provam vaga
morta.** Nove morreram de verdade naquele dia. Quando for varrer em massa, use poucas conexões, e
antes de escrever VAGA EXPIRADA reconfira a candidata sozinha.

**A checagem de duplicidade se faz no GMAIL, não nos CSVs.** Em 06/09 a campanha aplicou pela
segunda vez na Lead Character Modeling e Blendshape da TAT Productions. O Vini já tinha aplicado
naquela mesma requisição em **27/08**, e a confirmação daquele dia veio do **mesmíssimo endereço**,
`jobs.e13168@studio-tat.werecruit.io`, onde `e13168` é o id que está no fim da URL da vaga. O erro
não foi de leitura de anúncio: foi ter conferido só os CSVs, que começam depois. **Antes de aplicar
em qualquer casa, busque no Gmail confirmação antiga daquele domínio.** E quando o ATS manda a
confirmação de um endereço com o id da requisição embutido, esse endereço é a chave de deduplicação
mais barata que existe: buscar o id no Gmail responde na hora se aquela requisição já foi.

**Cuidado de pontuação ao editar o `docs/index.html`, que quebrou o painel em 06/09.** Toda entrada
do PORTAIS termina em `",true,"alta"],`: a **aspa fecha a nota antes do booleano** e a **vírgula
fecha a linha**. Acrescentar texto ao fim de uma nota buscando por `,false,` e concatenando põe o
texto **fora** das aspas e derruba a página inteira. Rode `sh automacao/valida-dashboard.sh` antes
de todo commit, sem exceção.

**O MESMO PEDIDO DE VAGA APARECE EM DOIS QUADROS DO GREENHOUSE, com IDs diferentes. Medido em
07/09 às 00h30 e é a armadilha mais silenciosa da regra 18, porque nada na tela avisa.** A 2K
publica a mesma requisição no quadro da holding (`boards-api.greenhouse.io/v1/boards/2k`) **e** no
quadro do estúdio (`.../cloudchamberen`). A Lead Character Artist aparece **quatro vezes**: 2k
`7888173003` (Montréal) e `7888174003` (Novato), cloudchamberen `7888170003` (Montréal) e
`7888172003` (Novato). Quatro IDs de anúncio, quatro URLs, e **uma requisição só**. A prova está num
campo que a própria API entrega: **`internal_job_id`, que nas quatro é `5834551003`**. Comparar
título, cidade e ID do anúncio, como a regra 18 mandava, **não pega este caso**: os IDs são
diferentes de verdade. Então a regra ganha um passo obrigatório:

> Antes de aplicar em vaga do Greenhouse, leia `internal_job_id` em
> `https://boards-api.greenhouse.io/v1/boards/<quadro>/jobs/<id>` e compare com o das candidaturas
> já enviadas. **`internal_job_id` igual é a mesma vaga**, mesmo que quadro, URL, cidade e ID do
> anúncio sejam outros.

Eu mesmo caí nisso em 07/09: varri o quadro `cloudchamberen`, ele parecia intocado, e comecei a
enviar a Lead Character Artist de Montréal. **O Gmail é que salvou**: havia email da 2K de 06/09 às
17h30 recusando exatamente essa vaga, de uma candidatura de 02/09 pelo quadro `2k`. Interrompi antes
do envio. Se eu tivesse confiado no painel, seria a segunda candidatura repetida da campanha para a
mesma Cloud Chamber. **Por isso a conferência no Gmail antes de enviar não é zelo, é etapa.**

**E o identificador do anúncio não é identidade de vaga.** Na Imageworks o anúncio de "Modeler"
gerou confirmação nomeando "Experienced Modeler", que já tinha candidatura. Quem diz qual requisição
recebeu a candidatura é o **email de confirmação**. Além disso, a caixa de email guarda candidatura
**pré-campanha**, de julho e agosto, que os CSVs não têm: antes de aplicar em casa que ele já tocou
antes de 26/08, busque no Gmail confirmação antiga daquele domínio.

## Completar PERFIL no Connect: seis armadilhas medidas em 06/09, à noite

Perfil pela metade é candidatura que o recrutador abre e vê metade. Estas seis foram medidas
completando quinze perfis numa rodada só, e **todas mentem em silêncio**.

1. ~~**O magic link tem COTA DIÁRIA de cinco por estúdio por dia.**~~ **DESMENTIDO em 07/09, veja
   o item 11.** Essa cota nunca existiu: os emails chegavam e quem os escondia era o preview de
   busca do Gmail. Não gaste rodada tratando estúdio como trancado.
   **O que continua valendo deste item, e foi medido de verdade: peça UM link e use na hora.**
   Link de duas horas antes já estava morto em dez de onze estúdios; link consumido em menos de
   cinco minutos funcionou em todos, e cada pedido novo invalida o anterior.
2. **`input[type=date]` não aceita digitação solta.** Digitar `2026-11-06` tecla a tecla no
   widget gravou **`1106-02-02`** e o log disse ok. Use `fill()` com ISO e releia.
3. **Multi-escolha com o PAINEL ABERTO não envia.** Na Coffee Stain o item ficou marcado, o
   `Next` foi clicado, e a página voltou para o mesmo slide com a resposta vazia, sem erro. Feche
   o painel (clique de novo no botão que o abriu) e só então envie.
4. **Filtro de escopo tem que valer nos DOIS lugares.** O slide `/connect/questions/locations` e
   a seção de locais dentro de `/connect/profile/settings` editam o mesmo campo. Limpei Bengaluru,
   Hong Kong, Amman, Abu Dhabi e Dubai no slide e o Settings, logo depois, remarcou todos.
5. **Leitor que guarda campo por NOME numa chave só MENTE quando o name se repete.** Com
   `location_ids[]` e `answer[choices][]` o último sobrescreve os outros e a prova diz que só um
   ficou marcado. Na Goodbye Kansas isso me fez achar que Londres tinha sumido. Acumule em lista.
6. **Local fora do escopo vem marcado por padrão e ninguém olha.** Mumbai estava marcado como
   "onde quero trabalhar" na Goodbye Kansas e na Untold, e a Playa tinha Bengaluru, Hong Kong,
   Amman, Abu Dhabi e Dubai. Marcar tudo é tão errado quanto deixar em branco.

**O mapa do wizard, que é slide a slide e não formulário único:** `/connect/questions/info` (nome,
telefone, endereço), `/locations`, `/resume`, `/pitch` e depois `/connect/questions/1..N` numeradas.
O `redirect_url` escondido de cada slide diz qual é o próximo. Fora do wizard ainda existem
`/connect/resume` e `/connect/profile/settings`, e é no Settings que ficam **departamento e função**,
que é o campo que um recrutador já marcou como VERY IMPORTANT nesta campanha. Preenchedor genérico
de formulário único volta "sem campos" em todos eles.

### Mais quatro, medidas na madrugada de 07/09 completando ILP e Twin Harbour

7. **Domínio próprio bloqueado não é vaga inacessível: use o ESPELHO `<slug>.teamtailor.com`.**
   `careers.ilpvfx.com` não passa pelo proxy desta sessão (o certificado servido é de
   `x.sni-498-default.ssl.fastly.net` e o host responde 502), e por isso a Important Looking
   Pirates ficou uma noite inteira registrada como "para o Vini fazer no navegador dele". O
   espelho serve **o mesmo backend** e **o token do magic link vale nele**: basta trocar o host
   do link do email antes de abrir. O link ainda redireciona uma vez para o domínio próprio e
   essa aba morre, mas **o cookie de sessão já ficou gravado**, então voltar ao espelho em
   `/connect/dashboard` entra logado. Receita para todo Teamtailor de domínio próprio bloqueado.
8. **O rótulo da função se REPETE em cada departamento, e os de fora ficam escondidos.** Casar
   `candidate[role_id]` pelo TEXTO do rótulo pega o primeiro "Artist" da página, que é de outro
   departamento; o servidor descarta em silêncio e a função volta para **All roles**. Só valem os
   radios **visíveis**, que são os do departamento escolhido. Foi o que deixou a ILP em All roles
   depois de o log dizer "ok".
9. **A conferência depois do clique tem que olhar o MESMO input, pelo `value`.** Conferir por
   texto de rótulo devolve **falso negativo** com o campo certo já marcado, pelo mesmo motivo do
   item 8, e faz o script "corrigir" o que já estava certo.
10. **Conta que já existe transforma o cadastro em LOGIN, e isso é a saída quando o pedido de
    link não gera email.** Na Twin Harbour o `/connect/login` não mandou nada, mas passar pelo
    `/connect` escolhendo departamento e enviando devolveu a tela mansa "If we find a Connect
    account, a sign in link will be sent" **e o email chegou**. Detalhe que evita recusa errada:
    nessa variante **as caixas de consentimento nem existem** na tela. Caixa ausente (`null`) é
    login e pode enviar; caixa que existe e não marcou (`false`) é a armadilha do gêmeo escondido
    e aí não se envia. E a lista de departamentos do `/connect` é desenhada por JavaScript: ler o
    DOM cedo demais devolve **zero radios** e o log diz "departamento ausente" com a página viva.

11. **A "COTA DIÁRIA DE CINCO LINKS" NÃO EXISTE. O item 1 desta lista está ERRADO e fica aqui só
    para ninguém repetir o diagnóstico.** O que escondia os links era o **leitor de email**: a
    busca do Gmail devolve, de cada thread, apenas as mensagens **mais antigas**, e **não marca
    que truncou**. Como todo link de acesso do Teamtailor chega com o mesmo assunto e cai na
    **mesma thread**, do sexto email em diante nada aparece na busca. Foi isso, e não cota
    nenhuma, que trancou IOI e Funcom por uma noite inteira: os links estavam chegando o tempo
    todo, **dez na IOI e oito na Funcom**, inclusive às 22h22, 23h12, 23h56 e 00h02. Abertas as
    threads inteiras, os dois perfis entraram na primeira tentativa.
    **A regra que sobra, e ela é de leitura, não de cota:** para achar o link mais recente, abra a
    **THREAD inteira** e ordene por horário; nunca decida pelo resultado de busca. E continua
    valendo pedir **UM e usar na hora**, porque cada pedido novo invalida o anterior e link velho
    morre — isso sim foi medido de verdade.

## Escopo, que é o mesmo da campanha

América do Norte, Europa incluindo Reino Unido, Irlanda, Nórdicos e União Europeia, Oceania, e na
Ásia somente Coreia do Sul e Singapura. **Nada de Índia, Brasil nem Japão.** Room 8 Studio está
fora. Vaga totalmente remota vale fora dessa lista, exceto Japão.

## O que ele entrega no fim de cada rodada

Resumo em português dizendo, nesta ordem: **quantas candidaturas foram ENVIADAS e confirmadas na
tela**, com estúdio, cargo, país e o texto da confirmação; quais ficaram à mão e por qual captcha,
com o dossiê já escrito; o que foi descartado e o motivo, quando o motivo for do anúncio e não
dele; e **quantas ainda sobram na fila**, que é o número que mede se o Jhon está fazendo o trabalho.

## Fatia MOTOR-A medida por inteiro em 06/09, e o que ela ensina sobre o tipo `MOTOR`

Sessenta estúdios de Europa continental, todos classificados `MOTOR` (Contact Form 7, Gravity,
Elementor, WPForms, Forminator, Formidable, Caldera, FluentForm, Ninja). Resultado bruto: **15
duplicados**, **3 candidaturas enviadas e confirmadas**, **2 paredes de captcha com dossiê**, **1
porta quebrada do lado do estúdio** e **39 sem porta de candidatura nenhuma**.

**A linha do brief que dizia "a maioria é fale conosco disfarçado" ficou medida: de 45 estúdios não
duplicados, exatamente UM tinha campo de arquivo no formulário** (EF Games, e é justamente o único
com vaga aberta de modelagem). Nos outros 44 o `type="file"` que a varredura por curl acusava era o
**CSS do plugin Contact Form 7** (`contact-form-7/includes/css/styles.css`), não um campo de
verdade. **Detector de porta que procura `type=file` no HTML bruto conta folha de estilo como
formulário de candidatura.** Filtre `.css` antes de contar.

**O que fez diferença para achar as três portas boas**, e vale repetir na fatia B e nas próximas:
não foi o formulário, foi **o texto da página de carreiras**. As três que valeram diziam, com
todas as letras, que recebiam perfil:

- **Code Horizon** (Polônia): *"The recrutation is currently closed but feel free to drop your CV
  through contact form"*. Quando a página de carreiras aponta para o formulário de contato, aquele
  formulário **deixa de ser genérico** e vira a porta designada por eles. Caldera, sem captcha.
- **Abylight Barcelona**: *"We review and archive every profile we receive to consider them for our
  current and future selection processes"*, com a lista de vagas vazia. Gravity Forms.
- **Frame Break**: o site é WordPress, mas a porta real estava em `jobs.<dominio>`, um **Teamtailor
  Connect** que a classificação `MOTOR` não enxergava. **Antes de tratar um MOTOR como formulário do
  site, procure `jobs.`, `careers.` e `career.` no domínio dele.**

**Duas armadilhas novas, medidas:**

1. **reCAPTCHA v3 nem sempre é só pontuação de fundo, às vezes é o portão inteiro.** O brief dizia
   "tente mesmo assim", e está certo em tentar, mas em 06/09 **duas de três tentativas morreram
   nele**: a EF Games devolveu `reCAPTCHA V3 validation failed, suspected as abusive usage` e a
   eXiin devolveu *Failed to send your message*. A Abylight, também WordPress e também com v3 na
   página, passou. Ou seja: v3 vale a tentativa e o custo dela é baixo, mas **conte com falhar** e
   já tire o dossiê na mesma rodada, antes de fechar o navegador.
2. **Caixa de aceite duplicada com `id` E `name` iguais.** Na EF Games as duas caixas do fim do
   formulário (privacidade obrigatória e contato futuro opcional) compartilham
   `id="form-field-field_91ffee6"`. É prima da armadilha do gêmeo escondido do Teamtailor, só que
   aqui as duas são reais: `querySelector` marca uma e deixa a outra. Use `querySelectorAll` e
   percorra.

**Estúdios desta fatia com veto ESCRITO no próprio anúncio**, para não gastar rodada de novo (a
frase é deles, com a data em que foi lida):

- **Frictional Games** (06/09): *"We can only consider European (EU/EEA) residents for job
  positions"*, e todas as vagas do quadro estão marcadas `-CLOSED-`. Freelance só por email.
- **Finitude** (06/09): as quatro vagas são Narrative Designer, Producer, Senior Programmer e Unity
  Developer, nenhuma de arte, e *"All available positions are fully remote but generally require you
  to reside in Germany"*.
- **Engine Software** (06/09): *"Full Time Positions: We are currently not hiring!"*; estágio só por
  email.
- **FDG Entertainment** (06/09): *"Currently no open positions available"*.
- **Clifftop Games** (06/09): *"Unfortunately, we do not have any open positions at this time"*.
- **Byte Barrel** (06/09): as cinco vagas do site apontam para o Skillshot e as cinco estão
  **`Ogłoszenie zarchiwizowane`**, arquivadas, inclusive a de 3D Artist.
- **Goose Minded** (06/09): o domínio do CSV, `gamedevestonia.ee`, **não é do estúdio**, é da
  associação GameDev Estonia, e o quadro dela tem anúncio de dois e três anos atrás. Domínio errado
  na fila, não estúdio sem vaga.

**Só por email, não é formulário** (viram fila de email, não de Jhon): Arclight Creations
(`jobs@arclightcreations.pl`, e a página diz *"Aktualnie nie prowadzimy rekrutacji"*), Clockstone
(*"Feel free to get in touch via office@clockstone.com"*), Digital Daredevils (só Technical Artist,
e por `office@`), Futurats (espontânea por email; as vagas abertas são de programação e design).

**Não deu para avaliar, e não é vaga morta:** `dgmind.com` devolve **403 do LiteSpeed também no
navegador de verdade**, e `earlymorningstudio.com` e `filimundus.se` derrubam a conexão
(`ECONNRESET`) por curl e por navegador. Ficam para reconferir de outra rede.
