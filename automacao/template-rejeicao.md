# Template de resposta a rejeições

Usado pela automação diária. Responder NA MESMA THREAD da rejeição, em inglês,
sem assinatura extra (a resposta abaixo já fecha com o nome).
Substituir `{TEAM}` pelo nome do estúdio (ex.: "Cartoon Saloon team").
Nada além deste texto. Sem emojis, sem travessão, sem "I hope this finds you well",
sem floreio de IA.

NUNCA ESCAPE O htmlBody (erro real cometido em 01/09 no email para a Amy Hurwitz,
da LAIKA). O campo htmlBody recebe HTML DE VERDADE: `<p>`, `<b>`, `<a href="...">`.
Se você escrever `&lt;p&gt;` no lugar de `<p>`, o Gmail entrega a mensagem com as
tags impressas como texto e o estúdio recebe um email com cara de lixo. Antes de
chamar a ferramenta, olhe o htmlBody: se enxergar `&lt;` ou `&gt;` em qualquer
lugar, está errado, corrija antes de enviar. O body (texto puro) é o oposto: nele
NÃO pode haver tag nenhuma.

REGRA DE ENVIO (obrigatória): sempre enviar com body (texto puro) E htmlBody.
No htmlBody, o link do portfólio vai como âncora com texto limpo:
`<a href="https://www.artstation.com/viniciuscavalcanti">artstation.com/viniciuscavalcanti</a>`
Nunca enviar só body com URL crua: o Gmail converte para HTML embrulhando a URL
no redirecionador google.com/url e ela aparece por extenso, com cara de spam.

---

Hi {TEAM},

Thanks for letting me know, and for taking the time to reply. Most studios don't.

If it's alright, I'd like to stay on your radar for future character work. My portfolio is at artstation.com/viniciuscavalcanti: more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces there, built to the same production standard as my studio work. The Houdini grooming breakdowns are there as well.

If an opening comes up on the character side down the line, I'd be glad to hear from you.

Best,
Vini Cavalcanti
