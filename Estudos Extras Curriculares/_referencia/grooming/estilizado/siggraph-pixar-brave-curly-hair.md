---
titulo: "Artistic Simulation of Curly Hair (cabelo da Merida em Brave)"
autor: "Hayley Iben, Mark Meyer, Lena Petrovic, Olivier Soares, John Anderson, Andrew Witkin (Pixar); artigo secundario de fxguide"
url: https://www.fxguide.com/fxfeatured/brave-new-hair/
data: 2012-06-01
tipo: artigo
versao_blender: nao se aplica (Pixar, ferramenta propria "Taz")
coletado_em: 2026-09-28
---

## Nota de coleta

O paper tecnico original da Pixar ("Artistic Simulation of Curly Hair",
SCA 2013, memo tecnico #12-03a) fica em
graphics.pixar.com/library/CurlyHairA/paper.pdf, mas essa URL redireciona
para www.pixar.com/technology-libraries (o PDF direto nao respondeu com o
paper em si nesta coleta). Uso como fonte principal o artigo da fxguide,
que entrevistou a equipe e cita numeros de producao que o paper tecnico
puro nao da. Existencia confirmada por fetch direto (HTTP 200, conteudo
lido).

Isto nao e um tutorial de Blender. E o princípio de estudio por tras do
cabelo cacheado estilizado mais citado da industria (Merida, Valente/
Brave, Pixar, 2012). Uso "Princípios" no lugar de "Receita" porque nao ha
nodes para reproduzir, so decisões de design que dá para traduzir pra GN.

## Princípios

1. **Poucas guias, muitas curvas finais.** Merida tinha 1.500 curvas
   guia desenhadas a mao, que geravam cerca de 111.000 curvas no render
   final. O artista controla a forma geral com um numero pequeno e
   gerenciavel de guias; o volume visual vem da interpolacao.
   Traduzido pra GN: poucas guias esculpidas a mao, Interpolate Hair
   Curves faz o resto. Ja e exatamente a stack canonica documentada em
   `../CEREBRO_GROOMING.md`.

2. **Ferramenta de curva dedicada em vez de so fisica.** A groomer Lena
   Petrovic descreveu o raciocinio: "How do I do this at home? I use a
   curling iron! So she implemented a curling iron in the computer." A
   ferramenta recebe diametro e comprimento como parametro e gera o
   cacho, que o artista depois ajusta a mao para dar carater. Ou seja, o
   cacho nao nasce da simulacao fisica pura, nasce de uma ferramenta de
   modelagem de curva com controle artistico direto (parecido com o Curl
   Hair Curves do Blender, que recebe raio e numero de voltas como
   parametro artistico, nao fisico).

3. **Densidade "explodida" antes de simular.** Para dar volume de cartoon
   em vez de cabelo colado na cabeca, a equipe penteou o cabelo de um
   jeito propositalmente exagerado antes de rodar a simulacao: "groomed
   hair in an exploded way, as if Merida had her finger in a light
   socket", garantindo que cada cacho tivesse separacao visual clara
   antes de qualquer fisica entrar. Esse e um ponto de partida
   deliberadamente nao realista que so depois vira "natural" com a
   simulacao por cima.

## Como aplicar em Geometry Nodes (traducao minha, nao veio da fonte)

- Poucas guias (principio 1) mais Interpolate Hair Curves para volume:
  ja e a stack padrao do Blender, nada de especial precisa ser inventado.
- Cacho como decisao artistica de raio/voltas (principio 2): usar Curl
  Hair Curves com raio grande e poucas voltas por guia, ajustado guia a
  guia, em vez de aplicar o mesmo raio de curl em toda a cabeca.
- Volume exagerado antes de "assentar" (principio 3): aumentar o Clump
  Hair Curves Factor e o espalhamento entre guias na fase de escultura,
  simulando a etapa "exploded" antes de qualquer suavizacao ou frizz
  final.
