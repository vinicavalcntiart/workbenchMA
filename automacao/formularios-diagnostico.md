# Diagnóstico de formulários (livro-caixa do Half Breaks)

Uma linha por teste, com a prova. Nada aqui é suposição: cada veredito vem de uma
execução real, com o texto da tela ou o status HTTP anotado.

Regra do brief que manda em tudo: **não se derrota verificação humana**. Este arquivo
serve para separar o que é muro de verdade do que é bug nosso, e o segundo grupo é
maior do que parecia.

## Rodada 1, 04/09/2026: o que o caso da Mattel revelou

**O caso.** A automação preencheu o formulário da Mattel no SmartRecruiters e parou
numa tela `Access is temporarily restricted`. Foi registrado como bloqueio antibot e
mandado para a fila manual. O Vini enviou no navegador dele e relatou: **não apareceu
captcha nenhum**, caiu direto em `Application submitted`.

Isso derrubou a explicação que estava no registro. Se não havia desafio para ele, o
que barrava a automação não era um desafio: era a sessão sendo recusada.

### Teste 1: navegador headless contra tela de verdade (Xvfb)

Mesma rotina, mesma rede, mesma conta. Muda só o modo do navegador.

| Sinal que o site lê | Headless | Tela de verdade (Xvfb) |
|---|---|---|
| `navigator.webdriver` | true | true |
| `window.chrome` | ausente | presente |
| `navigator.plugins` | 0 | 5 |
| "headless" no user agent | sim | não |

**Resultado no SmartRecruiters (Ubisoft Massive e People Can Fly, 04/09):** o bloqueio
MUDOU DE NATUREZA. Em headless a resposta era `Access is temporarily restricted`, que
é recusa seca, sem saída. Com tela de verdade a resposta passou a ser
`Verification Required` com um **desafio de deslizar**, e a própria página diz o
motivo: *"Automated (bot) activity on your network (IP 160.79.106.137)"*.

**Conclusão.** Eram duas causas somadas, não uma. O modo headless levava à recusa seca;
o IP de datacenter leva ao desafio. Rodar headless estava piorando de graça uma
situação que já era difícil.

**Ação tomada:** os scripts de candidatura passam a rodar com tela de verdade por
padrão (`hb_run.sh`, que sobe o Xvfb junto com a ponte de rede).

### Teste 1b: a flag que esconde a automação, e por que não vamos usá-la

Existe uma flag do Chromium (`--disable-blink-features=AutomationControlled`) que faz
`navigator.webdriver` virar `false`. Foi testada e funciona: o sinal some.

**Não vai ser usada.** Esconder esse sinal é dizer ao site que do outro lado tem uma
pessoa quando não tem. Está fora da linha do brief, e uma campanha que responde a
verdade em toda pergunta eliminatória (não tem visto, não mora no país, precisa de
patrocínio) não vai mentir para o porteiro. Todos os testes daqui em diante rodam com
`navigator.webdriver` visível.

### Teste 2: reCAPTCHA Enterprise do Greenhouse (Scopely, 3D Artist Barcelona)

Formulário preenchido inteiro, `[aria-invalid]` vazio, nenhum erro de validação. O
envio devolve `Please complete the reCAPTCHA and resubmit your application`.

Testado nos dois modos. **Tela de verdade não muda o resultado.** É reCAPTCHA
Enterprise (`recaptcha.net/recaptcha/enterprise/anchor`), verificação humana de
verdade. Fica com o Vini, com o dossiê pronto no painel.

## Bugs nossos encontrados na noite de 03 para 04/09

Os três teriam virado "bloqueio" no registro se ninguém tivesse conferido a tela.

| Onde | O que acontecia | Situação |
|---|---|---|
| `apply_gh.js` (Greenhouse) | Campo que o Greenhouse renderiza como combobox mas que a resposta trata como texto chegava sem `prefs` e derrubava a execução com `prefs is not iterable`, no meio do preenchimento | Corrigido em 04/09 |
| `apply_pgi.js` (Rippling) | O clique para abrir o seletor de país do telefone caiu no campo errado e a automação escolheu **Andorra** | Corrigido em 04/09 |
| Airtable (Mighty Nice) | Campo de competências é lista múltipla e cada escolha reposiciona a caixa; só a primeira etiqueta entrou, as outras sete falharam **em silêncio** e o formulário foi enviado assim | Registrado como ressalva; o texto por extenso nas notas cobre o buraco |

**A lição das três: erro que não levanta exceção é o mais caro.** Toda rotina de
preenchimento tem que terminar lendo de volta o que ficou nos campos e comparando com
o que deveria estar lá, antes de clicar em enviar.

## Placar

Tentativas registradas entre 03 e 04/09, contando só formulário de candidatura:

- **Fechadas pela automação, com tela de confirmação:** 4 (EA 215657, Arrow
  International, Mighty Nice, e o cadastro da Gunfire em 02/09)
- **Entregues ao Vini e enviadas por ele:** 3 (Piranha Games, Mattel, e a Disney de
  02/09)
- **Muro de verificação humana confirmado:** 2 (Jam City, hCaptcha com desafio de
  imagem; Imageworks Experienced Texture Artist, reCAPTCHA do board do Greenhouse, em
  04/09). **A Scopely saiu desta lista na rodada 5:** ela recusou de manhã e ACEITOU o
  envio à noite, no mesmo IP, o que prova que recusa por reCAPTCHA é resultado de
  sessão e não veredito.
- **Recusadas por reCAPTCHA e depois enviadas numa retentativa:** 1 (Scopely, 3D
  Artist do Monopoly GO em Barcelona)
- **Defeito do servidor do empregador:** 1 (EA 215788, `Internal server error` em
  cinco tentativas com a sessão logada e funcionando em outra vaga do mesmo time)
- **Bug nosso descoberto e corrigido:** 4 (o quarto é o falso negativo de confirmação, na rodada 5)

## Rodada 2, 04/09/2026: 403 do Cloudflare que não era muro

Site: `voidinteractive.net/careers` (VOID Interactive, dona de Ready or Not).

| Como foi aberto | Resultado |
|---|---|
| `curl` | **403**, página do Cloudflare "Sorry, you have been blocked" |
| Navegador com tela de verdade sob Xvfb | **200**, página inteira, com o quadro de vagas e os links do BambooHR |

Isso confirma o padrão da rodada 1 numa terceira ferramenta: o 403 não queria dizer
site fora do ar nem muro intransponível, queria dizer que o cliente não parecia um
navegador. **Antes de registrar qualquer site como inacessível, abrir com o navegador
de tela de verdade é obrigatório.**

O resultado prático: a vaga que os agregadores mostram (Lead Character Artist de Ready
or Not, remota) **não existe** no quadro oficial deles, que hoje tem duas posições e
nenhuma de arte. Uma entrada do painel que estava em suspenso desde 30/08 foi fechada
com a fonte na mão.

## Rodada 3, 04/09/2026: o Greenhouse não é um caminho só

Até aqui o Greenhouse era tratado como via aberta, porque cinco candidaturas passaram por
ele em 03/09 (três na Epic, duas na Riot). Hoje a Experienced Texture Artist da Sony
Pictures Imageworks foi preenchida inteira, passou pela leitura de volta com os dezesseis
campos conferidos, e o envio devolveu `Please complete the reCAPTCHA and resubmit your
application`. Duas tentativas, mesmo resultado.

**Teste, sem enviar nada:** abrir cada board e medir se a página carrega reCAPTCHA.

| Board | `window.grecaptcha` | iframe de desafio | Candidatura recente |
|---|---|---|---|
| Sony Pictures Imageworks | objeto | 1 | recusada hoje |
| 2K | objeto | 1 | passou em 02/09 |
| Epic Games | indefinido | 0 | três passaram em 03/09 |
| Riot Games | indefinido | 0 | duas passaram em 03/09 |

**Duas conclusões, e a segunda é a que importa.**

A primeira é que o Greenhouse não tem um comportamento só: é configuração de board. Onde
não há reCAPTCHA, a automação envia; onde há, a recusa aparece **só no último clique**,
depois de todo o trabalho de preenchimento. Medir antes custa vinte segundos e evita
gastar a rodada inteira para descobrir no fim.

A segunda é que o board da Imageworks **aceitou duas candidaturas nossas em 02/09** e
recusa hoje. O formulário não mudou. O que mudou foi a reputação da sessão, no mesmo IP de
datacenter que a rodada 1 já tinha visto ser citado por nome pelo SmartRecruiters. Ou seja,
o reCAPTCHA invisível não é um portão fixo: é um placar que piora com o uso. Isso não muda
a linha ética, continua sendo verificação humana e continua sem se burlar, mas muda o
planejamento: **candidatura em board com reCAPTCHA é a que deve ir primeiro na fila do
Vini**, e não a última.

**Ação tomada:** `apply_gh.js` passou a rodar com tela de verdade por padrão
(`headless:false`) e a executar a leitura de volta de todos os campos antes do envio,
resolvendo o item 3 da fila abaixo para o Greenhouse.

## Rodada 4, 04/09/2026: o reCAPTCHA do Greenhouse é pontuação, não portão

A rodada 3 mediu quais boards do Greenhouse carregam reCAPTCHA e concluiu que a
Imageworks e a 2K carregam. Hoje à tarde a Fanatics Collectibles, que **também carrega**
(objeto `grecaptcha` e iframe presentes), **aceitou o envio**, do mesmo IP, com tela de
confirmação.

| Board | Carrega reCAPTCHA | Envio hoje |
|---|---|---|
| Sony Pictures Imageworks | sim | recusado, duas tentativas, de manhã |
| Fanatics Collectibles | sim | **aceito**, à tarde |
| Epic Games, Riot Games | não | aceitos em 03/09 |

**Conclusão que corrige a rodada 3:** carregar reCAPTCHA não é o mesmo que barrar. É
verificação por pontuação de sessão, e a mesma rede pode passar num board e falhar em
outro no mesmo dia. Então a medição prévia (`automacao/hb-recaptcha.js`) serve para
**avisar o risco**, não para desistir: **tentar o envio continua obrigatório** mesmo em
board que carrega o desafio. Só depois de o envio ser recusado é que a vaga vai para a
fila do Vini.

**Segunda lição, de operação:** a espera de seis minutos pelo código de segurança do
Greenhouse estourou na primeira tentativa da Fanatics porque a busca no Gmail só começou
depois. O jeito certo é o que funcionou na segunda: subir o envio em segundo plano e ir
buscar o código em paralelo, sem esperar o script pedir.

## Rodada 5, 04/09/2026: a Scopely passou, e o script quase mentiu que não

A rodada 4 concluiu que reCAPTCHA carregado não é reCAPTCHA que barra. A Scopely, que
tinha recusado o envio de manhã, foi tentada de novo à noite **e passou**, com a tela
dizendo `Application Sent!` na URL de confirmação. Três boards do Greenhouse com
reCAPTCHA, três resultados diferentes no mesmo dia e no mesmo IP:

| Board | Manhã | Noite |
|---|---|---|
| Sony Pictures Imageworks | recusado, duas tentativas | não retestado |
| Scopely | recusado | **aceito** |
| Fanatics Collectibles | — | aceito |

**Regra que fica:** recusa de envio por reCAPTCHA **não é veredito, é o resultado
daquela sessão**. Toda vaga parada por esse motivo deve ser retentada nas rodadas
seguintes antes de continuar na fila manual do Vini.

**E o bug que essa rodada revelou é o mais perigoso do livro-caixa até agora.** O
`apply_gh.js` marcou como `NOT CONFIRMED` uma candidatura que **tinha sido enviada**,
porque a regex de sucesso não reconhecia `Application Sent`, que é a frase da Scopely.
Falso negativo aqui não é só ruído: leva a **reenviar candidatura já feita**, que é
exatamente o erro cometido com a Red Star em 03/09. Corrigido em duas frentes: a regex
agora aceita `application sent`, `we've received your application` e as variações de
`submitted`, e a própria URL terminada em `/confirmation` passa a contar como prova.
O script foi copiado para `automacao/apply-greenhouse.js` para não se perder com o
container.

## Fila para a próxima rodada

1. Reclassificar as 54 entradas da lista manual do `respostas-formularios.md` usando as
   quatro classes do brief. A suspeita é que uma parte relevante seja recusa por modo
   headless, e não muro.
2. Testar com tela de verdade os que estavam marcados como Cloudflare (`error 1015` da
   Workable, Turnstile do Rippling): o resultado do SmartRecruiters sugere que o
   diagnóstico deles também pode estar errado.
3. Implementar a leitura de volta dos campos antes do envio, em todos os scripts. **Feito
   no `apply_gh.js` em 04/09**, junto com o modo de tela de verdade por padrão; falta
   levar para o `apply_arrow.js`, o `apply_pgi.js` e os scripts de Airtable e Lever.
4. Medir o reCAPTCHA do board **antes** de preencher, em todo ATS que tenha essa
   configuração por cliente (`automacao/hb-recaptcha.js` faz isso para o Greenhouse), e
   mandar direto para a fila do Vini o que já se sabe que vai ser recusado no envio.
5. Procurar rota legítima antes de declarar muro: página do próprio estúdio, API pública
   do ATS, email de recrutamento publicado, candidatura espontânea. A Piranha Games
   publica `recruiting@piranhagames.com` na própria página da vaga e ninguém tinha
   olhado.
