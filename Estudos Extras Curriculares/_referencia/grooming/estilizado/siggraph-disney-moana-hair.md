---
titulo: "The Art and Technology of Hair Simulation in Disney's Moana"
autor: "Marc Thyng, Christopher Evart, Toby Jones, Alex McAdams (Walt Disney Animation Studios)"
url: https://history.siggraph.org/wp-content/uploads/2022/09/2017-Talks-Thyng_The-Art-and-Technology-of-Hair-Simulation-in-Disneys-Moana.pdf
data: 2017-07-30
tipo: paper
versao_blender: nao se aplica (Disney, ferramenta propria)
coletado_em: 2026-09-28
---

## Nota de coleta

SIGGRAPH 2017 Talks, DOI 10.1145/3084363.3085072. PDF publico baixado de
history.siggraph.org e lido por inteiro (2 paginas). Pagina de publicacao
oficial da Disney tambem confirmada:
disneyanimation.com/publications/the-art-and-technology-of-simulating-hair-in-disneys-moana/
(HTTP 200). Este paper e mais sobre fisica de simulacao de cabelo cacheado
do que sobre "look" estilizado especificamente, mas traz um principio de
organizacao (simular por clump, nao por fio) que e diretamente aplicavel
a qualquer groom estilizado.

## Princípios

1. **Simulacao (e, por extensao, qualquer efeito) no nivel do clump, nao
   do fio.** Citacao literal: "For Moana, the hair rigs were simulated at
   the level of individual clumps, and hair-hair interaction was
   controlled by dynamic edge-edge repulsion springs." O cacho
   individual do fio vem de outro lugar (o modelo elastico da guia), mas
   o comportamento de grupo (colisao, atrito, quebra) e resolvido por
   clump. Isso e o oposto de simular ou estilizar fio a fio.

2. **Parametros poucos e intuitivos, para controle artistico rapido.**
   O novo modelo de cabelo foi desenhado para ter "a small number of
   physically intuitive parameters, which allows the simulation artists
   to spend less time searching wide parameter spaces to obtain a desired
   behavior." Ou seja, o objetivo de design da ferramenta era permitir
   iteracao artistica rapida, nao maxima fidelidade fisica com dezenas de
   controles.

3. **Clump como parametro visivel e nomeado, nao efeito colateral.** A
   Figura 2 do paper mostra "different clumping behavior of hair created
   by varying the break distance parameter of dynamic wire connections to
   create a wet-hair look." O grau de clumping (de solto a "cabelo
   molhado") e um unico parametro (distancia de quebra da conexao),
   ajustavel para ir de um extremo ao outro do espectro visual.

4. **Groom e simulacao iteram juntos, nao em sequencia fixa.** Foi criado
   um processo para a artista de grooming ver o estilo em movimento e a
   artista de simulacao ajustar a estrutura do groom antes de finalizar,
   porque espaco negativo no groom colapsava o volume do cabelo sob
   movimento. Ou seja, o groom final so fica bom depois de testado em
   movimento, nao so em pose estatica.

## Como aplicar em Geometry Nodes (traducao minha, nao veio da fonte)

- Principio 1 (efeito por clump, nao por fio): ao desenhar frizz ou
  ruido estilizado, usar o indice de clump (de Create Guide Index Map ou
  do proprio Clump Hair Curves) como semente/entrada de variacao, para
  que fios do mesmo clump se movam e variem juntos, e nao cada fio de um
  jeito independente.
- Principio 3 (clumping como slider unico de "molhado a solto"): expor
  um unico Factor de Clump Hair Curves como o controle principal de
  "estilo" do groom (0 = solto e volumoso, 1 = colado/molhado/mecha
  fechada), em vez de multiplos parametros redundantes.
- Principio 4 (testar em movimento): para grooms que vao ser animados,
  visualizar o resultado do Deform Curves on Surface com a animacao
  rodando antes de fechar os valores de Clump e Frizz, nao so em pose de
  T-pose ou frame parado.
