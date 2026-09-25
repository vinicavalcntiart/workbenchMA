# Plano do fim de semana: personagem fechada até domingo à noite

Sábado 26 e domingo 27 de setembro de 2026. Entrada: grooming fechado na
madrugada (ou congelado no melhor estado), sculpt, retopo, pose, UVs e bake
prontos.

## Meta

Domingo à noite: peça publicável no ArtStation e material pronto pra levar na
one-on-one final com o Charles. Publicável, não perfeita.

## Prioridade (o que entra primeiro se o tempo apertar)

1. Render principal: pose inteira, 3/4, olhos e risada como ponto focal.
2. Close do rosto com cabelo.
3. Turntable curto (ou 4 vistas estáticas, se o render de vídeo não couber).
4. Silhueta em preto como imagem de apoio (o Charles gosta dessa prova).
5. Breakdown: clay render, wireframe, cabelo isolado.
6. Texto curto de post e três perguntas pra one-on-one.

Se só o 1 e o 2 saírem, a peça já existe. O resto é multiplicador.

## Sábado

| Bloco | Trabalho | Saída |
|---|---|---|
| Manhã (cabeça descansada) | Retomar o que congelou na madrugada. Sobrancelhas e cílios como hair curves curtas, uma stack mínima (Interpolate + Profile + Trim) | Grooming fechado de vez |
| Meio-dia | Pausa longa. Comida de verdade | |
| Tarde 1 | Lookdev no Blender: materiais com os bakes, couro, tecido, vidro dos frascos com líquido azul, polvo. Fio em Principled Hair. Um material de cada vez, sempre olhando o conjunto | Personagem vestida em Cycles |
| Tarde 2 | Passe de cor pela régua: marrom base, turquesa e laranja como acento, azul dos frascos como focal secundário, vermelho do lenço puxando pro rosto. Saturação em favor da leitura, não do realismo | Paleta batendo com o concept |
| Noite | Luz e câmera. Três luzes no máximo: key quente, fill fria fraca, rim atrás dos coques. Fundo neutro. Câmera 3/4 com lente 65 a 85 mm | Render de teste do frame principal |

## Domingo

| Bloco | Trabalho | Saída |
|---|---|---|
| Manhã | Render final do frame principal e do close. Resolução de entrega, samples suficientes pro cabelo não chiar (denoise ligado, 512 a 1024 samples) | Imagens 1 e 2 |
| Meio-dia | Pausa | |
| Tarde 1 | Turntable ou 4 vistas. Silhueta em preto. Clay, wireframe, cabelo isolado | Imagens 3, 4 e 5 |
| Tarde 2 | Compositing leve: contraste, um leve vignette, nada de glow. Montagem das pranchas | Pranchas prontas |
| Noite | Post no ArtStation. Nota de uma página pra one-on-one: o que se buscou, o que ficou, três perguntas pro Charles | Peça publicada |

## Régua de qualidade no render

- Lê em preto? A silhueta em Solid preto confirma antes de qualquer luz.
- Os olhos são o primeiro lugar pra onde o olho vai? Se o frasco ou o cabelo
  roubam, baixar contraste neles, não subir nos olhos.
- Superfície limpa. Ruído de detalhe que aparece só no close sai da imagem
  principal.
- Cabelo: mecha grande lê à distância, mecha pequena lê no close, frizz não
  aparece em nenhum dos dois.

## Perguntas pra levar pro Charles (rascunho)

- A hierarquia coque / rosto / props está na ordem certa de leitura?
- O polvo está ajudando a história ou competindo com o rosto?
- Pra portfólio de feature animation, esse nível de acabamento de cabelo
  (strands) é o que ele espera, ou cards estilizados leriam melhor?

## Regras da casa pro fim de semana

- Save incremental a cada bloco. Render de teste salvo com o nome do bloco.
- Bloco que estoura 30 minutos congela e vai pra lista de "depois".
- "Depois" é depois do post. A peça publicada com uma pendência vale mais que
  a peça perfeita na pasta.
- Pausas contam como trabalho. Elas são o que faz o bloco seguinte render.
