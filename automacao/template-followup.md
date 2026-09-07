# Template de follow-up (1 semana sem resposta)

Usado pela rotina de follow-up de 02/09 (e ondas seguintes). Criar RASCUNHO de resposta
NA MESMA THREAD do email original (create_draft com replyToMessageId da mensagem
original do Vini). NUNCA enviar: o Vini revisa e envia.
Substituir {TEAM} pelo nome do estúdio. Nada além deste texto.
Sem emojis, sem travessão, sem floreio de IA.

REGRA DE ENVIO (obrigatória): sempre body (texto puro) E htmlBody.
No htmlBody, negrito em "45 projects", "over 60 characters" e "personal projects";
link do portfólio como âncora limpa:
<a href="https://www.artstation.com/viniciuscavalcanti">artstation.com/viniciuscavalcanti</a>

Elegibilidade: estúdios de enviados.csv com estado "enviado" simples (sem bounce,
sem recusa, sem resposta humana registrada em processados.csv, sem redirecionamento
para portal). Máximo 1 follow-up por estúdio em toda a campanha.

---

Hi {TEAM},

A quick follow-up on my email from last week. Character seats fill fast, so I wanted to stay on your radar: my portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it: artstation.com/viniciuscavalcanti. The Houdini grooming breakdowns are there as well.

{FECHO}

Best,
Vini Cavalcanti

---

## TESTE DOS DOIS FECHOS (aberto em 07/09, decisão do Vini)

O corpo acima é fixo. **Só a última linha antes da assinatura varia**, e ela é a
única variável do teste. Nada mais muda: nem assunto, nem parágrafo, nem negrito.

**Fecho A**, o que a campanha vinha usando:
`If character work opens up on your side, I'd be glad to talk.`

**Fecho B**, o canônico das cartas frias, e o único dos dois que PEDE o
encaminhamento interno por escrito:
`If character work opens up on your side, I'd like to be on your list. And if someone else there is the right person for this, just point me and I will take it there.`

**Por que o teste existe.** Duas das três respostas boas da campanha inteira
(Flying Bark, que passou o portfólio ao time de recrutamento, e Hampa, que
encaminhou à recrutadora) foram encaminhamento interno, e o texto que estava no
ar nunca pediu isso. 3 respostas em 71 follow-ups é sinal fraco demais para
tratar o fecho atual como intocável.

**Como foi dividido.** A coorte de 02/09, 111 estúdios elegíveis, alternando um
a um na ordem de envio (o primeiro leva A, o segundo B, e assim por diante), o
que deixa as duas metades parecidas em país e em data: 56 com A, 55 com B.

**Onde está o registro.** `automacao/followup-0709.csv`, coluna `fecho` (A ou B)
e coluna `coorte`. A coorte `26/08-01/09` (101 estúdios, enviados em 07/09) levou
o fecho A e serve de base histórica, mas **o teste controlado é só a coorte
02/09**, porque é a única onde os dois fechos saíram no mesmo dia para públicos
comparáveis.

**Quem for ler o resultado:** contar resposta humana por fecho, e contar
separado a resposta que oferece encaminhamento, que é a hipótese que o fecho B
tenta comprar. Não trocar o texto padrão antes de a coorte 02/09 responder.
