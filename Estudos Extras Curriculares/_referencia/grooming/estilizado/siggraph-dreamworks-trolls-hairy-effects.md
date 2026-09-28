---
titulo: "Hairy Effects in Trolls"
autor: "Brian Missey, Amaury Aubel, Arunachalam Somasundaram, Megha Davalath (DreamWorks Animation)"
url: https://research.dreamworks.com/wp-content/uploads/2018/07/26-0269-missey-Edited.pdf
data: 2017-07-30
tipo: paper
versao_blender: nao se aplica (DreamWorks, ferramenta propria "Willow")
coletado_em: 2026-09-28
---

## Nota de coleta

SIGGRAPH 2017 Talks, DOI 10.1145/3084363.3085070. PDF baixado direto de
research.dreamworks.com e lido por inteiro (2 paginas). Nao e tutorial de
Blender. Trolls (2016) e o exemplo mais citado de cabelo 100% estilizado
como elemento central de design de personagem (o pelo/cabelo dos trolls e
feito de la/feltro estilizado, nao cabelo realista).

## Princípios

1. **Cabelo como mais da metade da silhueta do personagem.** Citacao
   literal: "It is a crucial part of the overall character design of the
   Trolls themselves, typically composing over half the silhouette of the
   character." Isso muda a prioridade de trabalho: o cabelo nao e detalhe,
   e a forma principal do personagem. Em GN isso quer dizer desenhar a
   silhueta das guias mestras antes de qualquer detalhe (clump fino, frizz),
   porque a silhueta e o que carrega o design.

2. **Material tatil unificado.** O mundo de Trolls e feito de materiais
   "palpaveis" (feltro, la), entao ate fogo e destruicao foram
   redesenhados com "look" de cabelo/fibra para caber nesse mundo: "we
   consistently rendered them as hair. This artistic choice helped anchor
   the effect in the tactile environment while giving it a unique yet
   easily recognizable style." Principio: escolher um material/silhueta
   caracteristico (aqui, "fio grosso e fofo") e aplicar ele de forma
   consistente em varios elementos do personagem e do cenario, nao so no
   cabelo da cabeca.

3. **Controle de silhueta via secao transversal, nao so root/tip.** O rig
   de cabelo dos trolls tinha "scale controls with a cage-based surface
   deformer for even more fine tuning of the silhouette", alem de IK
   controls ao longo da curva. Ou seja, a forma da mecha era esculpida
   tanto no comprimento (voltas do rig) quanto na largura (deformador de
   secao), nao so num unico parametro de espessura raiz-ponta.

4. **Guia crescida dentro de um volume, nao só ao longo de uma curva.**
   Para as mechas que crescem "a vontade" (deformando em formas livres),
   a equipe registrava a raiz da guia num plano e fazia ela crescer dentro
   de um tubo NURBS convexo, projetando a posicao da raiz no volume. Isso
   e o analogo conceitual de crescer guias dentro de um volume-alvo em vez
   de so ao longo da normal da superficie.

## Como aplicar em Geometry Nodes (traducao minha, nao veio da fonte)

- Principio 1 (silhueta > detalhe): comecar qualquer groom estilizado
  desenhando so 3 a 5 guias mestras que já formam a silhueta correta em
  Object Mode, antes de ligar Interpolate Hair Curves ou qualquer Clump.
- Principio 3 (secao transversal controla silhueta): usar Set Hair Curve
  Profile com um perfil nao circular (retangular ou achatado) e variar a
  largura por segmento da guia, nao so o raio raiz/ponta.
- Principio 4 (crescer dentro de volume): para mechas tipo "chifre" ou
  "presa" que saem da silhueta normal, gerar a guia com Generate Hair
  Curves e depois usar um Displace/Deform customizado para levar a ponta
  para dentro de um volume alvo (ex.: uma mesh guia escondida), em vez de
  so estirar ao longo da normal.
