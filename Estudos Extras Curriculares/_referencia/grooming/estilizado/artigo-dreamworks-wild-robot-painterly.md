---
titulo: "Inside the impressionistic realism of DreamWorks' The Wild Robot"
autor: "Trevor Hogg (Creative Bloq), com citacoes de Chris Sanders (diretor), Raymond Zibach (production designer) e Jeff Budsberg (VFX supervisor)"
url: https://www.creativebloq.com/3d/3d-animation/creating-the-artisan-aesthetic-for-the-wild-robot
data: 2024-10-01
tipo: artigo
versao_blender: nao se aplica (DreamWorks)
coletado_em: 2026-09-28
---

## Nota de coleta

Artigo de imprensa, fetch direto confirmado (HTTP 200, texto lido por
inteiro via curl e limpeza manual de HTML, ja que o WebFetch generico so
trouxe o menu de navegacao). Ha tambem uma sessao tecnica especifica sobre
o pelo, "Painterly Fur and Feathers of The Wild Robot" (SIGGRAPH Talks
2025, ACM DOI 10.1145/3721239.3734088), que fica atras de paywall (HTTP
403 em todas as tentativas). O resumo dessa sessao, achado via busca,
diz que o visual "mimics how an artist applies detail to a painting: in
layers of brushstrokes that form simplified groupings of light and color,
with surgical placement of highlights" e que "fur and feathers... needed
to respond to light like continuous surfaces to better fit into the
stylized painterly world", mas nao consegui abrir o texto completo nem
confirmar o resto da sessao, entao trato essa frase como citacao de
segunda mao (via resultado de busca), nao verificada linha a linha no
documento original.

## Princípios

Do artigo da Creative Bloq (verificado, fetch completo):

1. **Nao adaptar depois, construir estilizado desde o inicio.** Citacao
   do VFX supervisor Jeff Budsberg: "It doesn't make sense to create a
   realistic bush or tree and try to hammer it in compositing to make it
   look painterly. If you want a stylised-looking plant, you should draw
   the plant." Ou seja, o estilo entra na modelagem/no groom, nao e um
   filtro de composicao por cima de um resultado realista.

2. **Decidir onde o detalhe aparece e onde ele "mente".** Citacao do
   production designer Raymond Zibach: "A lot of what painting is, is
   deciding how much you're going to cheat where the detail is and isn't,
   and how much can you let a brushstroke show or whether you need to
   replace that with something tighter." Aplicado a pelo/cabelo: nem toda
   regiao da mecha precisa do mesmo nivel de detalhe; puxar detalhe (fios
   finos, frizz) so onde a camera vai reparar, e simplificar (poucas
   mechas largas) no resto.

3. **Referencia de traço segue a curvatura do movimento.** Sobre
   atmosfera com pincelada (nao e sobre pelo diretamente, mas o mesmo
   principio se aplica a cabelo em movimento): "they try to follow the
   principal curvature of the direction of the flow... You want them to
   be flowing with the volume." Aplicado a groom: a direcao do pente e do
   clump deve seguir a curvatura da forma que o cabelo acompanha (queda,
   vento), nao uma direcao arbitraria.

4. (nao verificado linha a linha, via busca) O visual de pelo e pena do
   filme usa "layers of brushstrokes that form simplified groupings of
   light and color, with surgical placement of highlights", e o pelo
   precisou "respond to light like continuous surfaces" apesar de ser
   feito de curvas. Trato isso como resumo de terceiros ate conseguir ler
   o paper original.

## Como aplicar em Geometry Nodes (traducao minha, nao veio da fonte)

- Principio 1 (estilizar na origem): decidir o numero de niveis de clump
  e o raio deles antes de pensar em shading; nao tentar "consertar" um
  groom denso e realista com toon shader depois.
- Principio 2 (detalhe seletivo): variar a densidade do Interpolate Hair
  Curves e a intensidade do Frizz por regiao (vertex group de "close-up",
  por exemplo rosto e maos), deixando o resto do corpo com clumps largos e
  poucos filhos.
- Principio 3 (direcao segue a forma): pentear a guia mestra alinhada ao
  fluxo de queda/vento antes de aplicar Clump ou Curl, para que o clump
  amplifique uma direcao que ja faz sentido, em vez de corrigir depois
  uma direcao ruim.
- Principio 4, se confirmado (fio reagindo como superficie): usar normais
  customizadas (Sample Custom Normals no Distribute Points on Faces, ja
  documentado em `../blender-dev/studio-blender-2023-procedural-hair-nodes.md`)
  para o fio herdar uma normal mais suave da superficie, em vez da normal
  real do fio, ajudando o shader toon a ler o pelo como bloco de luz
  continuo e nao como fio por fio.
