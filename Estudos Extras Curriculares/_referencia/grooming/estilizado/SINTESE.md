# Sintese: receitas de cabelo e pelo estilizado (Blender, Geometry Nodes)

Coletado em 2026-09-28. Estas sao as receitas/principios mais simples e
mais repetidos entre as fontes desta pasta. A maioria dos valores nao foi
informada pelas fontes (elas descrevem o "o que" e o "por que", quase
nunca o numero exato), entao cada item diz claramente o que e citacao e o
que e inferencia minha para Geometry Nodes. Nao invente valor: onde a
fonte nao da numero, esta escrito "valor nao informado".

## 1. Poucas guias grandes definem a silhueta, o resto e interpolacao

Nodes: Interpolate Hair Curves (poucas guias esculpidas a mao) mais
qualquer clump/curl por cima.
Valor de partida: Merida (Brave) usava 1.500 guias para ~111.000 curvas
finais; ordem de grandeza, nao uma regra fixa.
Fontes: `siggraph-pixar-brave-curly-hair.md`,
`siggraph-dreamworks-trolls-hairy-effects.md` (cabelo como "over half the
silhouette"), `ba-tolkfan-chonky-stylized-hair.md`.

## 2. Esculpir a guia primeiro (Sculpt Curves), aplicar GN depois

Nodes: nenhum node especifico citado; fluxo e Sculpt Curves mode para
desenhar a forma, GN Clump/Set Hair Curve Profile depois para engrossar e
afilar ponta.
Valor: nao informado (o autor nao lista parametros, so anexa um .blend
nao analisado nesta coleta).
Fontes: `ba-tolkfan-chonky-stylized-hair.md`,
`artigo-80lv-sculpting-stylized-hair.md`.

## 3. Clump em camadas (macro e detalhe), nao um Clump so

Nodes: Clump Hair Curves (camada larga) mais Frizz Hair Curves (camada de
detalhe), nessa ordem segundo o proprio Blender Studio.
Valor: nao informado (so a ordem do capitulo "Detail Layering (Frizz +
Clumping)", sem numeros).
Fontes: `yt-blender-studio-procedural-fur.md`, e como principio de
estudio em `siggraph-disney-moana-hair.md` ("hair rigs were simulated at
the level of individual clumps").

## 4. Curl como ferramenta artistica, com raio/voltas ajustados por guia

Nodes: Curl Hair Curves, com Radius e Curls (numero de voltas) variando
guia por guia, nao um valor global.
Valor: nao informado (a fonte descreve o principio de a groomer da Pixar
ter feito uma "curling iron" digital que recebe diametro e comprimento,
nao os numeros exatos usados em Merida).
Fonte: `siggraph-pixar-brave-curly-hair.md`.

## 5. Perfil de curva achatado (fita) mais torcao via Set Curve Tilt

Nodes: Set Hair Curve Profile (perfil nao circular) mais Set Curve Tilt
com Spline Parameter como entrada de torcao, mais Float Curve para o
falloff da torcao ao longo do fio, mais Multiply para escalar a forca.
Valor: nao informado (o post nao da o formato exato do Float Curve nem a
forca do Multiply).
Limitacao registrada na fonte: essa receita torce todas as mechas igual;
nao resolve variacao por guia individual.
Fonte: `ba-hair-stylized-curve-tilt-twist.md`.

## 6. Cor por clump/sub-clump, tipo pincelada, nao por fio

Nodes sugeridos (inferencia minha, nao veio da fonte): indice de clump
(de Create Guide Index Map ou do proprio Clump Hair Curves) alimentando
um Color Ramp no shader.
Valor: nao informado.
Principio citado: controles de matiz por clump e sub-clump criam manchas
de cor grandes "que look like paint strokes", em vez de variacao por fio.
Fonte: `artigo-dreamworks-puss-in-boots-fur.md`. Repetido, de forma mais
simples (pintura manual em vez de automatica por clump), em
`yt-aaron-vdw-stylized-fur-eevee.md` (capitulo "Painting fur colors").

## 7. Guard hair grosso e com transparencia, como linha de acento

Nodes sugeridos (inferencia minha): segundo grupo de guias com Set Hair
Curve Profile de raio maior, alfa do shader variando ao longo do fio.
Valor: nao informado.
Fonte: `artigo-dreamworks-puss-in-boots-fur.md`.

## 8. Buracos de proposito entre clumps, para ler como tufos desenhados

Nodes sugeridos (inferencia minha): Factor do Clump Hair Curves variando
por regiao (vertex group esparso), em vez de clumping uniforme cobrindo
tudo.
Valor: nao informado.
Fonte: `artigo-dreamworks-puss-in-boots-fur.md` (transparencia mapeada
para guias grossas, criando "gaps and broken edges" tipo ilustracao).

## 9. Direcao do pente segue o fluxo do movimento antes do clump/curl

Nodes: pentear/orientar a guia mestra alinhada a direcao de queda ou
vento antes de aplicar Clump Hair Curves ou Curl Hair Curves.
Valor: nao informado.
Fonte: `artigo-dreamworks-wild-robot-painterly.md` (pincelada segue "the
principal curvature of the direction of the flow").

## 10. Detalhe so onde a camera repara, resto simplificado

Nodes sugeridos (inferencia minha): Interpolate Hair Curves com densidade
maior e Frizz Hair Curves com Amount maior num vertex group de
"close-up" (rosto, maos), densidade e frizz baixos no resto do corpo.
Valor: nao informado.
Fonte: `artigo-dreamworks-wild-robot-painterly.md` ("deciding how much
you're going to cheat where the detail is and isn't").

## 11. Shading carrega o estilo, nao so a geometria do clump

Nodes: normais convertidas para espaco de objeto no shader do fur, sombra
do fur resolvida a parte da sombra padrao do motor de render.
Valor: nao informado.
Fonte: `yt-aaron-vdw-stylized-fur-eevee.md` (capitulos "Shadows",
"Normals", "Converting normals object space").

## 12. Testar o groom estilizado em movimento antes de fechar Clump/Frizz

Nodes: nenhum especifico; e um passo de processo, nao de node tree:
rodar a animacao de Deform Curves on Surface e so depois travar os
valores finais de Clump Hair Curves e Frizz Hair Curves.
Valor: nao informado.
Fonte: `siggraph-disney-moana-hair.md` (groom colapsava sob movimento
quando tinha espaco negativo demais; processo de ida e volta entre
grooming e simulacao antes de finalizar).

## 13. Volume/comprimento exagerado e decisao de design, nao de fisica

Nodes: aumentar Length e densidade de Interpolate Hair Curves alem do que
"pareceria real", quando a silhueta ou a narrativa pedir.
Valor de referencia: Rapunzel tinha cerca de 140.000 fios simulados em
21m (70 pes) de cabelo; nao e uma regra, e o exemplo mais extremo
encontrado.
Fonte: `artigo-disney-tangled-rapunzel-hair.md`.

## Observacao final

Nenhuma das fontes de video desta coleta entregou uma transcricao (ver
`MANIFESTO.md`, secao de metodo), entao nenhuma receita acima tem uma
lista completa de nodes com valores prontos para copiar. O que da para
levar com confianca sao os principios (o que cada estudio/artista prioriza
e por que) e os poucos nodes citados literalmente (item 5, `Set Curve
Tilt` + `Spline Parameter` + `Float Curve` + `Multiply`, e os capitulos
nomeados do tutorial oficial do Blender Studio, item 3). O resto e minha
traducao para nodes da Essentials, marcada como tal em cada arquivo.
