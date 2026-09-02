# Campanha de emprego do Vini Cavalcanti — briefing
Atualizado em 31/08/2026. Painel ao vivo: https://vinicavalcntiart.github.io/workbenchMA/

## Quem é
Senior 3D Character Artist, 10+ anos em personagens estilizados.
- **The Wingfeather Saga** (Angel Studios): modelou e pintou à mão os personagens da 1ª temporada.
- **Endstar** (E-Line Media, Arizona, EUA): há quase 5 anos, personagens herói do sculpt à engine. Trabalha remoto com time americano.
- Passado de outsourcing na PUGA Studios. Grooming em Houdini como diferencial.
- Formação: láurea com honors, especialização em Game Art (Méliès SP), mestrado em andamento (UNICAP), IELTS, publicações.
- Portfólio: artstation.com/viniciuscavalcanti · LinkedIn: linkedin.com/in/vinicavalcnti · Escola: vinicavalcanti.com

## Regras fixas (não violar)
1. **Só rascunho pela automação.** A automação nunca envia email frio pelo conector: ela deixa o rascunho no Gmail (sem assinatura, sem anexos) e quem envia é o Apps Script do Vini (`automacao/envia-rascunhos.gs`), rodando na conta dele, que coloca a assinatura padrão, anexa CV e carta e manda. Exceções permitidas ao conector: a resposta-padrão de recusa em thread existente (rotina de monitoramento) e os follow-ups em thread existente, quando o Vini autorizar (02/09: 71 enviados).
2. **Cargo:** ele é **visual development e character modeler**. Grooming é diferencial de apoio, nunca o cargo procurado. Vaga só de groom entra como plano B.
3. **Remoto primeiro.** Vaga 100% remota é o ideal. Presencial com visto NÃO se descarta, só vem depois.
4. **Discrição:** nunca escrever, em carta, formulário ou resposta, qualquer motivo pessoal que sugira dificuldade ou hesitação em mudar de país. Se perguntarem, a posição é uma só: ele quer realocar. O mestrado só aparece como credencial que fortalece o caso de visto.
5. **Escopo geográfico:** América do Norte, Europa (incl. UK/Irlanda/Nórdicos), Oceania e, na Ásia, só Coreia do Sul e Singapura. **Japão está fora** (idioma, fuso, moeda). Não prospectar Índia nem Brasil (a antiga exceção, Estúdio Pé Grande, fechou em agosto de 2026). Room 8 Studio e grupo estão fora.
6. **Fonte oficial:** job board serve para DESCOBRIR vaga, nunca para confirmar. Só escrever "vaga confirmada" depois de abrir a página do próprio empregador ou o ATS dele.
7. **Salário:** USD 3.840 por mês. **Nunca revelar o salário da E-Line** (quebra de NDA).
8. **Right to work:** nunca mentir em caixa de autorização de trabalho. Responder "No" para EUA e "Yes" para sponsorship, e vender o caso de visto no campo de texto livre.
9. **Frase fixa de portfólio** (usar sempre, com negrito nos trechos indicados): "My portfolio holds more than **45 projects** with **over 60 characters** across many titles, and my **personal projects** are some of the strongest pieces in it."
10. **Frase fixa de realocação** (só para estúdios FORA dos EUA): "I'm open to relocating as well; my academic background (honors laurea, postgraduate specialization, master's in progress, IELTS, publications) makes a strong visa case."
11. **Proibido em carta:** a palavra Brazil, travessão, emoji, floreio de IA.
12. **Ponto forte a usar:** artista de jogos entrega o asset inteiro (high poly, retopo, UV, bake, textura, LODs, engine). Artista de animação/VFX costuma ser especialista de uma etapa só. Isso é vantagem, nunca lacuna.
13. **Porta de entrada:** ele aplica de propósito em vagas de outra função onde não há vaga de personagem, apostando em encaminhamento interno. Não tratar como engano. Em campo livre, declarar na primeira linha que a área dele é personagem e pedir o encaminhamento.

## Números (31/08)
- 159 emails em 14 lotes para 154 estúdios; 148 entregues, 6 bounces.
- 172 estúdios alcançados (148 por email + 24 só por portal).
- 12 respostas humanas, 10 recusas (todas respondidas), 0 entrevistas.
- 33 candidaturas por portal confirmadas.
- Estúdios grandes da animação americana: **16 de 17** (falta Walt Disney Animation Studios).
- 12 vagas morreram em poucos dias desde o começo. Vaga sênior de personagem em estúdio grande dura de 3 a 7 dias.

## Threads vivas
Passion Republic (em análise), TAT Productions (vaga nomeada + recrutadora Julie Goutheraud), WildBrain (Groom Supervisor), Psyop, Superprod Milano, Nuare, Plastic Wax, Submarine (recusa morna), DreamWall (prazo vence 13/09), Black Kite (Angus Edhouse respondeu).

## Não fazer
- Não aplicar de novo na Sony Pictures Imageworks (Margot Ingrassia). Ele já cobrou.
- Não cobrar a Polygon Pictures: cancelada com a saída do Japão.
- Angel Studios: Keith Lango disse em 04/08 que o time de asset está completo. Ele aplicou mesmo assim como porta de entrada em 31/08. A janela boa é quando a 5ª temporada montar equipe.

## Pendências dele
- Formulário da **Fortiche** (envio falhou em 27/08).
- **Walt Disney Animation Studios**, único dos grandes sem candidatura.
- Assinar alerta de vaga nos ATS: Insomniac, Pixar, Disney, Nickelodeon, PlayStation, Blizzard.

## Calendário
- 02/09: onda de follow-up enviada (71 nas threads da primeira onda); segunda onda de 175 emails frios enviada à mão; lote 17 (70) enviado pelo Apps Script.
- 04/09: segunda onda, com os lotes 10 e 11.
- 13/09: vence o prazo da DreamWall.

## Automação em funcionamento
- Monitor a cada 2h: lê respostas, bounces e confirmações de ATS; responde recusa com template; notifica no celular se pedirem entrevista, teste ou portfólio.
- Prospecção a cada 4h: varre vagas remotas primeiro, revalida vagas antigas, alimenta o painel e a newsletter.
- Envio: os rascunhos da campanha (assunto fixo) saem pelo Apps Script `automacao/envia-rascunhos.gs`, na conta do Vini, com assinatura e anexos; ele roda à mão (40 por execução) ou por acionador de tempo, se ele ligar. O monitor marca os estúdios como enviados quando vê a mensagem em Enviados.
- Formulários: a automação preenche formulários sem captcha de desafio pelo navegador headless (Greenhouse, Ashby, Breezy, JotForm, Teamtailor Connect, formulários próprios); hCaptcha, reCAPTCHA de caixa, Turnstile, DataDome e portais com conta ficam para o Vini, listados em `automacao/respostas-formularios.md`.
