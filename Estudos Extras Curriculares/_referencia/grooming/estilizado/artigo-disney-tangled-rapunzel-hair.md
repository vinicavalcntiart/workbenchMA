---
titulo: "Simulating Rapunzel's hair in Disney's Tangled (via artigo 80.lv) e pagina de publicacao da Disney"
autor: "Kelly Ward, Maryann Simmons, Andy Milne, Hidetaka Yosumi, Xinmin Zhao (Walt Disney Animation Studios); artigo secundario 80.lv"
url: https://80.lv/articles/how-disney-simulated-rapunzel-s-70-feet-of-hair-in-tangled
data: 2010-07-28
tipo: artigo
versao_blender: nao se aplica (Disney, ferramenta propria "dynamicWires")
coletado_em: 2026-09-28
---

## Nota de coleta

Paper original: "Simulating Rapunzel's hair in Disney's Tangled", SIGGRAPH
2010 Talks, DOI 10.1145/1837026.1837055. Pagina oficial de publicacao
confirmada em
disneyanimation.com/publications/simulating-rapunzels-hair-in-disneys-tangled/
(HTTP 200, abstract lido: "We present several key techniques used for
simulating Rapunzel's 70 feet of hair for the animated feature 'Tangled';
these techniques range from methods to improve the run-time efficiency of
the simulations to achieving the desired art direction of the hair.").
O texto completo do paper fica atras de paywall da ACM; uso o artigo do
80.lv como fonte secundaria para o numero de fios e o nome da ferramenta.

## Princípios

1. **Volume extremo como decisao de design, nao de fisica.** Rapunzel
   tem 70 pes (~21 metros) de cabelo com cerca de 140.000 fios
   individuais simulados. Esse volume nao existe na natureza; e uma
   escolha de silhueta e narrativa (o cabelo e a "corda" magica da
   historia) que a equipe tecnica teve que viabilizar depois, nao o
   contrario.

2. **Ferramenta de simulacao propria construida para o estilo do filme,
   nao generica.** A equipe criou o software "dynamicWires", um sistema
   mass-spring dedicado as curvas de cabelo, porque nenhuma ferramenta
   generica aguentava o volume e o comportamento pedido pela direcao de
   arte. Principio geral: quando o volume/estilo do cabelo foge do
   padrao, a equipe tecnica adapta a ferramenta ao estilo, nao o estilo a
   ferramenta.

3. **Atrito direcional para controlar comportamento em contato com
   chao.** Uma tecnica especifica citada: adicionar um parametro de
   atrito tangencial para contato com o chao, separando a componente de
   atrito na direcao tangente ao fio e escalando ela para baixo (ate duas
   ordens de grandeza menor que o atrito normal). Isso evita que o
   cabelo "trave" contra o chao de um jeito que pareceria errado ao
   olho, mesmo sendo fisicamente mais correto sem esse ajuste.

## Como aplicar em Geometry Nodes (traducao minha, nao veio da fonte)

- Principio 1 (volume como decisao de design): decidir o comprimento e a
  contagem de guias pela leitura de silhueta desejada, nao por
  "realismo" (por exemplo, cabelo bem mais comprido que o corpo do
  personagem e uma escolha valida se a historia pedir).
- Principio 3 (atrito/contato ajustado pelo olho, nao pela fisica pura):
  ao usar o modificador Shrinkwrap Hair Curves para tirar o cabelo de
  dentro da mesh, testar visualmente o resultado perto de superficies de
  contato (chao, ombro) e preferir o ajuste que "parece certo" ao ajuste
  fisicamente mais exato, seguindo o mesmo raciocinio da equipe de
  Tangled.
