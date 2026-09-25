# Plano da madrugada: grooming fechado até o amanhecer

Data: noite de 25 pra 26 de setembro de 2026.
Ferramenta: Blender 5.2 LTS, objeto Curves + hair nodes da Essentials, sem addon.
Ponto de partida: `Curves.001` com 110 guias e o Interpolate Hair Curves já
no modificador (screenshot da sessão). Os dois coques já existem como volume.

## A meta da noite, em uma frase

Ao amanhecer, o cabelo lê como no concept a dois metros de distância, com os
coques como forma primária e fio como textura. Nada além disso é obrigatório.

## O que "pronto" significa (critério de parada)

Feito quando os cinco estiverem verdadeiros:

1. Silhueta em preto (viewport em Solid, cor preta, sem luz): os dois coques e a
   franja lêem igual ao concept.
2. Nenhum fio atravessa o crânio, a testa ou o outro coque.
3. Direção de fluxo clara: os fios saem da raiz e giram em espiral pro coque,
   sem cruzamento aleatório.
4. Clump visível em dois níveis (mecha grande, mecha pequena), sem frizz que sujei a leitura.
5. Render de teste em Cycles com Principled Hair BSDF em loiro, sem estourar.

Qualquer coisa que não sirva a um desses cinco fica pro fim de semana ou sai.

## Mapa mental Houdini → Blender

O que travou até aqui é vocabulário, não capacidade. A tabela abaixo é a tradução.

| Houdini | Blender 5.2 | Observação |
|---|---|---|
| Guide Groom (pentear guias) | Sculpt Curves mode, brushes Comb, Snake Hook, Slide, Puff, Smooth, Pinch | Mesmo gesto. O Comb com Deform Type "Curvature" é o mais próximo do Guide Groom padrão |
| Guide Process (Set Length, Bend, Smooth) | Trim Hair Curves, Straighten Hair Curves, Smooth Hair Curves, Curl / Roll | Cada um é um node group na stack, empilhado como Guide Process empilha operações |
| Hair Generate | Interpolate Hair Curves | Densidade por atributo da superfície (weight paint na mesh de skin, lido por Named Attribute). Guide Count = quantas guias influenciam cada filho |
| Hair Clump | Clump Hair Curves | Precisa do atributo `guide_curve_index`. Gera com Create Guide Index Map antes |
| Clump em 2 níveis (Blend com clump maior) | Create Guide Index Map com Guide Distance grande → Clump 1 → Create Guide Index Map com distância pequena → Clump 2 | É o "feijão com arroz" do Houdini e é subdocumentado no Blender. Funciona empilhando dois pares Map + Clump |
| Frizz | Frizz Hair Curves | Amplitude pequena. Em estilizado, quase zero |
| Hair Noise / Lift | Hair Curves Noise | Noise de baixa frequência ajuda a quebrar a regularidade do Interpolate |
| Guide Mask (por região) | Atributo pintado na mesh de skin, lido por Named Attribute e ligado no Factor/Selection do node | Todo node da Essentials tem um Factor que aceita field |
| Hair Group | Um objeto Curves por região | Coque esquerdo, coque direito, franja, flyaways. Modificadores independentes, controle de peso de render separado |
| Guide Deform / skin binding | Attach Hair Curves to Surface + Surface Deform já vem do Empty Hair | Já está resolvido se o objeto nasceu de Add > Curve > Empty Hair |
| Hair Width ramp | Set Hair Curve Profile | Raiz grossa, ponta fina. Em estilizado, raiz mais grossa que em realismo |
| Shrinkwrap de guias na skin | Shrinkwrap Hair Curves | Segura o volume pra dentro do coque, evita fio flutuando |

## Stack de nodes sugerida, na ordem

Por objeto Curves (um por região). A ordem importa: a Essentials espera
profile e clump antes de noise, e trim por último.

```
Interpolate Hair Curves        (densidade por atributo, Guide Count 2 a 3)
Set Hair Curve Profile         (raiz ~0.0025, ponta ~0.0004 em escala de metro)
Create Guide Index Map  [grande]
Clump Hair Curves       [nível 1, mecha grande, Factor 0.7 a 0.9, Shape 0.3]
Create Guide Index Map  [pequeno]
Clump Hair Curves       [nível 2, mecha pequena, Factor 0.4 a 0.6, Distance ativo]
Hair Curves Noise              (Factor 0.05 a 0.15, escala grande)
Frizz Hair Curves              (quase zero; ligar só nos flyaways)
Shrinkwrap Hair Curves         (se algum fio escapar do volume do coque)
Trim Hair Curves               (variação de comprimento 5 a 10 %)
```

Para o coque: a forma do coque vem das guias, não dos nodes. As guias giram em
espiral e terminam dentro do volume. Os nodes só fazem os filhos seguirem.

Para os flyaways, um objeto Curves separado com pouquíssimas guias, Frizz mais
alto e Curl leve. Em estilizado eles são pontuação, não textura.

## Blocos de tempo

Cada bloco fecha com um save incremental (`_v01`, `_v02`...) e uma linha no diário.

| Hora (sugestão) | Bloco | Saída do bloco |
|---|---|---|
| 23:00 – 23:20 | Setup. Silhueta em preto do estado atual, screenshot pra comparar no fim. Split por região se ainda for um objeto só | Arquivo `_v01`, screenshot "antes" |
| 23:20 – 01:00 | Guias dos coques. Pentear até a silhueta e o fluxo lerem. Só guias, nada de Interpolate ligado (ou Groom Hide nas demais) | Critérios 1 e 3 |
| 01:00 – 01:15 | Pausa de verdade. Longe da tela | |
| 01:15 – 02:30 | Interpolate + Profile + Clump 2 níveis nos coques | Critério 4 |
| 02:30 – 03:15 | Franja e linha do cabelo. Raiz limpa na testa, sem fio atravessando | Critério 2 |
| 03:15 – 03:30 | Pausa | |
| 03:30 – 04:15 | Noise leve, Trim, Shrinkwrap. Flyaways como objeto separado | Fio como textura |
| 04:15 – 05:00 | Render de teste em Cycles, Principled Hair, loiro. Comparar com screenshot "antes" | Critério 5 |
| 05:00 | Save final `_groom_v01_final`, entrada no diário, dormir | |

Regra de parada por bloco: se um bloco passar 30 minutos do previsto, ele
congela no estado em que está e o próximo começa. O que ficou volta no sábado
de manhã, com cabeça descansada, e vai custar um terço do tempo.

## Armadilhas conhecidas na 5.2

- Sculpt Curves não esconde curvas nativamente. Pra pentear um coque sem o
  outro atrapalhar, ou separar em objetos, ou usar o Groom Hide do repositório.
- Interpolate ligado enquanto se penteia deixa o viewport pesado e esconde as
  guias. Desligar o modificador no viewport (olho) durante o groom das guias.
- Clump sem Create Guide Index Map antes não faz nada e não avisa.
- Os nodes da Essentials com "Allow Internet Access" ligado podem puxar versões
  online. Pra uma noite de entrega, manter o que já está no arquivo.
- Se o Interpolate gerar filhos cruzando entre os dois coques, o Guide Count
  está alto ou as guias de um coque estão perto demais da mesh do outro. Baixar
  Guide Count pra 2 resolve na maior parte das vezes.
- Escala: a personagem em metros, os raios do Profile em metros. Fio de 0.01 é
  um cabo, não um cabelo.

## Render de teste, o mínimo

- Cycles, 128 samples, denoise ligado.
- Curves > Shape: Rounded Ribbons (rápido) para teste; 3D Curves só no final.
- Principled Hair BSDF, modelo Huang (padrão na 5.x), Melanin ~0.15,
  Melanin Redness ~0.5, Roughness ~0.3 para loiro estilizado.
- Uma key quente 45°, um rim frio atrás do coque pra separar da silhueta.

## Fundo pra noite

- Bloco de precisão (guias, franja, raiz): série que prende sem exigir olho.
  Mr. Robot ou From, o que estiver mais no meio.
- Bloco de setup de nodes ou render: Moana. Quando o "How Far I'll Go" tocar,
  a franja já vai estar pronta.
- Se a energia cair de vez: 15 minutos de pausa longe da tela vale mais que
  meia hora arrastando o Comb sem ver o que faz.

## Se der tudo errado

Houdini deu 10 anos de olho pra grooming. O olho está aqui. A ferramenta é só
outro sotaque, e a tabela lá em cima é o dicionário. Se às 3h o clump ainda
não convence, o cabelo com guias bem penteadas, Interpolate e um clump só já
passa na régua do Charles: forma grande, limpa, legível. O segundo nível de
clump é polimento, não estrutura.
