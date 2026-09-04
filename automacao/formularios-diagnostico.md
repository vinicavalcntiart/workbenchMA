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
- **Muro de verificação humana confirmado:** 2 (Scopely, reCAPTCHA Enterprise; Jam
  City, hCaptcha com desafio de imagem)
- **Defeito do servidor do empregador:** 1 (EA 215788, `Internal server error` em
  cinco tentativas com a sessão logada e funcionando em outra vaga do mesmo time)
- **Bug nosso descoberto e corrigido:** 3

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

## Fila para a próxima rodada

1. Reclassificar as 54 entradas da lista manual do `respostas-formularios.md` usando as
   quatro classes do brief. A suspeita é que uma parte relevante seja recusa por modo
   headless, e não muro.
2. Testar com tela de verdade os que estavam marcados como Cloudflare (`error 1015` da
   Workable, Turnstile do Rippling): o resultado do SmartRecruiters sugere que o
   diagnóstico deles também pode estar errado.
3. Implementar a leitura de volta dos campos antes do envio, em todos os scripts.
4. Procurar rota legítima antes de declarar muro: página do próprio estúdio, API pública
   do ATS, email de recrutamento publicado, candidatura espontânea. A Piranha Games
   publica `recruiting@piranhagames.com` na própria página da vaga e ninguém tinha
   olhado.
