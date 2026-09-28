# Regras em uso da campanha (fonte única, atualizada em 27/09/2026)

Este é o resumo do que vale HOJE. O `CLAUDE.md` manda em tudo (quem decide é o Vini, tom, rota
do clique, estúdios grandes). Os `BRIEF-*.md` têm o passo a passo de cada frente. O `BRIEFING.md`
da raiz é o diário da campanha desde 26/08: serve para consulta e história, não para regra nova.
Em conflito, vale nesta ordem: o que o Vini disse no chat, `CLAUDE.md`, este arquivo, os `BRIEF-*`,
o `BRIEFING.md`.

## Quem é o Vini, em uma linha
Senior 3D Character Artist, 10+ anos em personagem estilizado: The Wingfeather Saga (Angel
Studios, elenco da 1ª temporada modelado e pintado à mão), Endstar (E-Line Media, quase 5 anos,
do sculpt à engine), grooming em Houdini como diferencial. Portfolio artstation.com/viniciuscavalcanti,
LinkedIn linkedin.com/in/vinicavalcnti, site vinicavalcanti.com (nunca vinicavalcanti.art, que não tem site).

## O que se busca
- **Cargo:** personagem 3D (modelagem, escultura, textura e look dev de personagem, vis dev). Grooming é diferencial, vaga só de groom é plano B.
- **Nunca:** ambiente, props, veículos, hard surface.
- **Estúdio grande** (lista no CLAUDE.md): aplica também em 2D, vis dev, direção de arte e vizinhos de personagem (rig, CFX, look dev, textura), em qualquer senioridade, mesmo com veto escrito de residência.
- **Porta de entrada:** vaga de outra função numa casa sem vaga de personagem vale, pedindo encaminhamento no campo livre.
- **Onde:** América do Norte, Europa (com Reino Unido, Irlanda e Nórdicos), Oceania, Coreia do Sul e Singapura. Fora: Japão, Índia, Brasil, resto da Ásia. Remoto primeiro, presencial com visto vale.

## Metas
- **10 formulários enviados e confirmados por dia, no mínimo 5 de personagem.** Enviar vem antes de varrer.
- Prova de envio é só uma destas: URL de confirmação, texto do servidor ou recibo por email.

## Formulários
- **Leva do navegador na nuvem só quando o Vini pedir (28/09):** *"só monte a fila quando eu pedir. Derrube tudo pq tá contando."* O maestro não abre a tela nem monta abas por conta própria; a cobrança é por hora de tela aberta. Quando ele pedir, abre, preenche, envia e fecha logo depois.
  - **Esclarecimento do Vini (28/09):** isso vale só para formulário com caixa "sou humano" EXPLÍCITA. Formulário sem caixinha que o navegador local não consegue abrir ou enviar (site que não abre daqui, bloqueio de rede, DataDome sem desafio visível) o maestro leva para o navegador na nuvem por conta própria, na hora, envia e fecha a sessão logo depois: *"use o mais rápido possível"*.
  - **Cronômetro (Vini, 28/09):** *"sempre cronometre seu tempo nesse navegador, pra saber o quanto gastou"*. Toda vez que uma sessão na nuvem fechar, rodar `python3 automacao/cronometro-nuvem.py` (lê o tempo medido pela própria Kernel e atualiza `automacao/NUVEM-TEMPO.md`) e contar ao Vini, numa linha, os minutos e o custo estimado da sessão e do dia.
- Tudo é trabalho do maestro pelo navegador na nuvem: DataDome, 403, "spam", conta, código por email, termos e consentimentos.
- Só a caixa "sou humano" VISÍVEL vai para o Vini, na leva das 8h47 de Recife (CLAUDE.md, rota do clique).
- Lever (jobs.lever.co, hCaptcha "secure-api") não entra na leva: a verificação recusa o navegador na nuvem mesmo com a caixa marcada pelo Vini e apaga o CV (4 de 4 tentativas: Behaviour 25/09 x2, Kolibri 27/09 x2), e o navegador local cai no mesmo desafio. Vaga boa no Lever vira carta a pessoa (Joe).
- **Antes de enviar:** anúncio inteiro lido na fonte oficial do empregador (job board só descobre, nunca confirma); régua de veto (`automacao/regua-veto.py`); dedupe por ID da requisição no ATS, por URL e pelo nome da casa em `enviados.csv`, `automacao/processados.csv`, `docs/index.html` e na caixa do Gmail (`automacao/garra.sh`, `automacao/dedupe-agora.sh`). Quem diz qual vaga recebeu a candidatura é o email de confirmação.
- **Veto que derruba** (em casa que não é grande): idioma local exigido por escrito (ex.: francês no Quebec, espanhol, polonês), residência ou cidadania exigida por escrito, "sem patrocínio" escrito, estágio.
- **Respostas prontas do Vini (28/09):** idiomas = português nativo, inglês fluente, espanhol básico; anos de experiência = 10; pergunta "que jogos você joga" = sempre um jogo do próprio estúdio da vaga.
- **Respostas de fato, sempre a verdade:** autorização de trabalho "No" e patrocínio "Yes" fora do Brasil; anos de experiência reais; nunca revelar o salário da E-Line (NDA).
- **CV (Vini, 28/09): sempre ANEXADO, o PDF de verdade.** Email: anexo no rascunho. Formulário: upload do arquivo. NUNCA link do Google Drive (a pasta do Drive guarda dados privados do Vini), nunca link no corpo da carta. Se o formulário só aceitar link, o link é o litterbox 72h conferido com `%PDF-`; se o litterbox falhar, a vaga espera, e não vai com link do Drive. Nunca no repositório.
- **Resposta e email sempre com htmlBody (Vini, 28/09):** o Gmail da ferramenta transforma todo link em endereço longo do google.com/url. Em email só de texto isso aparece feio para o estúdio. Então toda resposta e todo rascunho vai com htmlBody, com texto curto no link (artstation.com/viniciuscavalcanti), e nunca só com body.

## Pretensão salarial (regra do Vini, 04/09)
1. Anúncio com faixa publicada: pedir a base da faixa, desde que acima do piso legal de visto do país (se a base ficar abaixo, pedir o piso ou o topo da faixa).
2. Sem faixa, casa grande: USD 100.000 · CAD 95.000 · GBP 50.000 · EUR 55.000 · AUD 110.000.
3. Sem faixa, casa pequena ou média, ou cargo abaixo de sênior: USD 85.000 · CAD 80.000 · GBP 42.000 · EUR 45.000 · AUD 95.000.
4. Campo livre: "Open to aligning with your band for the role; as a reference, I'm looking at around <valor>." Campo numérico: só o número.

## Cartas e emails para estúdios
- **Nunca oferecer teste de arte (Vini, 28/09):** *"Teste de arte é coisa de Junior ou pra quem n tem projetos o suficiente no portfólio."* Nenhuma carta, resposta ou campo de formulário oferece art test por iniciativa própria. O portfólio fala por ele: **47 projetos, mais de 60 personagens, 10 anos de experiência**. Se um estúdio mandar teste, vira aviso ao Vini para ele decidir.
- **Carta fria para pessoa** (Joe): assunto fixo `Senior Character Artist · Wingfeather Saga credit · stylized + grooming`, sem emoji no assunto; abre com o nome; uma frase de por que aquela pessoa, com a frase da casa entre aspas; teto de 250 palavras; frase do portfólio ("My portfolio holds **47 projects** with **over 60 characters** across many titles, and my **personal projects** are some of the strongest pieces in it"); fecho pedindo direção; fora dos EUA, "I am ready to move for the role, and I would need visa sponsorship."; rodapé Portfolio / LinkedIn / Site. Detalhes em `BRIEF-JOE.md`.
- **Conferência antes do rascunho:** `python3 automacao/confere-carta.py` e HTML por `automacao/monta-html-carta.py`; semelhança acima de 60% entre cartas, reescrever.
- **Proibido em carta:** a palavra Brazil, travessão, floreio de IA, email montado por padrão de domínio (só vale email publicado numa página aberta).
- **Emoji em email para estúdio:** ☺️ e 😊, um por lugar; 1 a 2 em carta para pessoa e em resposta a pessoa (inclusive recusa escrita por pessoa); 1 em carta para caixa geral; zero em formulário de ATS e em follow-up de silêncio.
- **Envio das cartas:** o maestro deixa o rascunho; quem envia é o programa do Vini no Google (`automacao/envia-rascunhos.gs`, gatilho de 2 em 2 horas depois de instalado e armado).
- **Respostas:** pessoa que escreve recebe resposta na mesma rodada (`BRIEF-COMUNICADOR.md`); recusa de robô não se responde; convite para entrevista, teste, salário ou oferta vira rascunho pronto e aviso imediato ao Vini.
- **Follow-up:** um só, 7 dias depois, no mesmo fio, sem emoji, nunca para quem já recusou ou respondeu.
- **Nunca escrever para Charles Ellison** (foi professor do Vini). Não cobrar a Margot Ingrassia (Imageworks) na thread de julho; a Imageworks segue alvo normal.

## Segurança do repositório (ele é público)
Nunca entra no repositório: telefone, endereço, senhas, salário da E-Line, data de nascimento,
respostas de EEO, links de Meet, link da tela ao vivo, CV, email completo de pessoa (no repositório
vai mascarado, `j***@dominio.com`; o completo fica só no scratchpad). Dados pessoais dos formulários
moram em `/home/user/apply/pessoal.json`, fora do repositório. Nunca `git add -A`; commit arquivo por arquivo.

## Onde fica cada coisa
Ver `LEIA-ME.md` na raiz.
