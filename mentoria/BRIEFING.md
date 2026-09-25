# Mentoria da escola (Vini Cavalcanti School) — briefing
Criado em 11/09/2026. Vale para toda resposta a aluno ou interessado na mentoria.
É assunto separado da campanha de emprego (ver `BRIEFING.md` na raiz): outra caixa
de entrada mental, outra voz, outras regras.

Página oficial: https://vinicavalcanti.com/mentorship/one-on-one-mentorship/
Discord da escola (convite gratuito, sempre oferecer): https://discord.gg/MuEwrCS46r
Checkout (Hotmart): https://pay.hotmart.com/D105581670W?bid=1781143563417&sck=lp_mentoria
Caixa que recebe o formulário do site: contact@vinicavalcanti.art
(o aviso chega de `submissions@formsubmit.co` com assunto "New message from vinicavalcanti website")

## Como a mentoria funciona de verdade (regra do Vini, 11/09)
Estes fatos passam por cima do que a página do site diz hoje.

- **Ao vivo, um a um.** Google Meet, no fuso do aluno.
- **Até 2 sessões por semana.** Não é "uma por semana".
- **Sem prazo.** As sessões continuam até o personagem ficar pronto. Não é um curso de 10 semanas.
- **Lifetime access** às aulas da plataforma.
- Entre sessões: canal privado no Discord com o Vini, mais aulas estruturadas na plataforma.
- Entrega: um personagem estilizado completo, do blockout ao render final. Etapas: formas
  primárias, feições, mãos, cabelo, roupa, pose, textura, groom, render. Última etapa é
  revisão de portfólio.
- Software: ZBrush e Blender (obrigatórios), Substance Painter, Houdini para groom e render
  (opcional). Sem exigência de nível. Algumas horas por semana.
- Preço: **US$ 600**, à vista ou em 3x. Cupom **MENTORSHIP20** dá 20% por tempo limitado.
  Cartão internacional aceito.
- Bônus: curso completo Intro to ZBrush: Mushroom (13 aulas).

**Pendência no site (11/09):** a página ainda anuncia "10 weeks", "Season 2 · 10 Weeks" e
"weekly live session" em 14 trechos, e não fala de lifetime access. O pedido de correção já
foi entregue ao Vini para repassar ao Claude que cuida do site. Enquanto não corrigir, o
e-mail ao aluno segue os fatos acima, não a página.

## Regras de escrita para e-mail de aluno (regra do Vini, 11/09)
1. **Sempre em inglês.** Vale mesmo quando o aluno escreve em outra língua.
2. **Simples e direto, sem excesso de texto, mas bem explicativo.** Cada seção diz uma coisa
   e diz inteira. Nada de parágrafo enfeitado.
3. **Sem firula de IA.** Nada de "I hope this finds you well", "it's worth noting", "genuinely",
   "delve", travessão, listas de três adjetivos.
4. **Negrito nos pontos que importam:** títulos de seção, "up to twice a week", "until your
   character is finished", "lifetime access", preço, cupom.
5. **Emojis simpáticos, poucos.** ☺️ na abertura, ✨ no convite do Discord, ☀️ no fechamento,
   e no máximo um por título de seção (🎯 🧌 🛠️ 💳). Nunca mais que isso.
6. **Sempre em HTML** (`htmlBody` no `create_draft`/`update_draft`). Rascunho em texto puro
   faz o Gmail mostrar as URLs envolvidas em `google.com/url?q=...`, feio e quebrado no
   celular. Em HTML os links viram texto curto e clicável: "Full details", "Sign up here",
   "Join the Discord". Mandar também o `body` em texto puro como alternativa.
7. **Sempre incluir o convite gratuito do Discord**, deixando claro que vale com ou sem
   mentoria.
8. **Fechar pedindo contexto:** o que a pessoa está fazendo agora, que personagem quer
   construir, link de portfólio. Isso dá material para a segunda resposta.
9. **Rascunho novo para o aluno, nunca "responder" o aviso do FormSubmit.** Responder aquele
   aviso manda o e-mail para `submissions@formsubmit.co`, não para o aluno. Pegar o e-mail do
   aluno do corpo do aviso e criar o rascunho endereçado a ele.
10. **Só rascunho.** Quem envia é o Vini.
11. Assinatura: `Vini Cavalcanti / Senior 3D Character Artist / vinicavalcanti.com`.
12. **"Hoje" e "amanhã" se contam no fuso de Recife (America/Recife, UTC-3), nunca em UTC.**
    Erro de 24/09: às 21:50 de quinta em Recife já era sexta em UTC, e um e-mail ao Ray saiu
    com "today" para uma sessão que era "tomorrow". O Vini enviou antes da correção. Conferir
    o relógio local antes de escrever qualquer data relativa.
13. **Agenda da mentoria fica em contact@vinicavalcanti.art.** O conector do Google Calendar
    precisa estar autorizado nessa conta (ou a agenda compartilhada com edição). Remarcar é
    `update_event` no evento "Vini Cavalcanti Mentorship (Nome)" com `notificationLevel: ALL`,
    que já avisa o aluno pelo próprio Agenda. Os blocos "Busy" são do agente `AGENDA_MENTORIA`
    e se ajustam sozinhos; não mexer.

## Modelo aprovado (11/09, rascunho para Shreya Sateesh)
Assunto: `Re: Mentorship inquiry`

```html
<div style="font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.5;color:#222;">
<p>Hi {{Name}} ☺️</p>

<p>Thanks for your message! Here is how the mentorship works.</p>

<p><b>🎯 Format</b><br>
It is a live one-on-one program. We meet <b>up to twice a week</b> on Google Meet, in your time zone, and keep going <b>until your character is finished</b>. No deadline. Between sessions you have a <b>private Discord channel</b> with me for questions and feedback, plus structured lessons on the learning platform with <b>lifetime access</b>.</p>

<p><b>🧌 The project</b><br>
One complete stylized character, from blockout to final render. We go through primary forms, facial features, hands, hair, clothing, posing, texturing, grooming and rendering. The last stage is a portfolio review.</p>

<p><b>🛠️ Software</b><br>
ZBrush and Blender (required), Substance Painter, and Houdini for grooming and render (optional). No experience level required. Plan for a few hours per week.</p>

<p><b>💳 Price</b><br>
<b>$600</b>, one payment or 3 installments. The coupon <b>MENTORSHIP20</b> gives 20% off for a limited time.<br>
👉 <a href="https://vinicavalcanti.com/mentorship/one-on-one-mentorship/">Full details</a><br>
👉 <a href="https://pay.hotmart.com/D105581670W?bid=1781143563417&amp;sck=lp_mentoria">Sign up here</a></p>

<p><b>✨ Free Discord invite</b><br>
You are welcome to join the school's Discord for free, mentorship or not. It is where students share work and get feedback:<br>
👉 <a href="https://discord.gg/MuEwrCS46r">Join the Discord</a></p>

<p>If you tell me what you are working on now and the kind of character you want to build, I can tell you how the program would fit. A portfolio link helps too ☀️</p>

<p>Best,<br>
<b>Vini Cavalcanti</b><br>
Senior 3D Character Artist<br>
<a href="https://vinicavalcanti.com">vinicavalcanti.com</a></p>
</div>
```

Quando a mensagem do aluno for específica (pergunta de preço, de nível, de software, de
horário), responder a pergunta primeiro, no primeiro parágrafo, e só depois o resto do
modelo, cortando o que não interessa.

## Modelo aprovado para compra de curso (20/09, rascunho para Sol Valvoi)
Chega aviso da Hotmart ("Congratulations! You have just sold a copy of the product ...") com nome
e e-mail do comprador. Rascunho novo para o comprador, curto: agradecer, "Vini Cavalcanti here",
convite do Discord, "any questions, just reply". Assunto: `Thank you for getting {{Course}}`.

```html
<p>Hi {{Name}} ☺️</p>
<p>Vini Cavalcanti here. Thank you for getting <b>{{Course}}</b>! I hope you enjoy the course.</p>
<p>You are welcome to join the school's Discord. It is free, and it is where students share their work and get feedback:<br>
👉 <a href="https://discord.gg/MuEwrCS46r">Join the Discord</a></p>
<p>If you have any questions along the way, just reply to this email. I am here to help ✨</p>
```
(mesma assinatura e mesmo `div` de estilo do modelo da mentoria)

## Registro de contatos
| Data | Nome | E-mail | Mensagem | Estado |
|---|---|---|---|---|
| 11/09/2026 | Shreya Sateesh | shreyanimates@gmail.com | "I wanted to inquire about the mentorship program." | Rascunho pronto no Gmail (draft `r-393674080718726483`), aguardando o Vini enviar |
| 20/09/2026 | Sol Valvoi | sol.valvoi@icloud.com | Comprou Intro to ZBrush: Mushroom (Hotmart HP3645967361) | Rascunho de agradecimento pronto no Gmail (draft `r4677622785483422638`), aguardando o Vini enviar |
| 22/09/2026 | Stanislav | stanislavpostolovskiy12@gmail.com | 4 perguntas: escolhe o personagem? requisito de dificuldade? perguntas fora das sessões? sessões pagas depois do fim? | Rascunho pronto no Gmail (draft `r-1466894231428855755`), aguardando o Vini enviar. Respostas de dificuldade e de continuação foram suposição minha, conferir |
| 24/09/2026 | Ray Blair | saycebuckley2@yahoo.com | Sessão de 25/09 11:30 remarcada para 02/10 11:30 BRT (compromisso de trabalho imprevisto) | Evento movido no Agenda e e-mail enviado pelo Vini |
