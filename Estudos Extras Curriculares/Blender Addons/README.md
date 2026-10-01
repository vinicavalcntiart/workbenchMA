# Loop LOD (Blender 5.2)

LODs por remoção de edge loops. Mantém a malha em quads, a simetria em X, as
seams, os sharps, as aberturas e as trocas de material.

## Instalar

Edit > Preferences > Get Extensions > seta no canto > **Install from Disk** >
`loop_lod.zip`. O painel fica na Sidebar (N) da viewport, aba **Loop LOD**.

## Usar

1. No Edit Mode, selecione os loops de deformação (cotovelo, joelho, ombro) e
   clique em **Mark Selected as Protected**. Eles vão para o grupo
   `LOD_Protect`.
2. Em Object Mode, monte a lista **LOD Chain** (padrão: 0,5, 0,25 e 0,125 dos
   triângulos) e clique em **Generate LODs**.
3. Os LODs vão para a coleção `LODs`. Se o nome tiver `LOD0`, vira `LOD1`,
   `LOD2`...

## O que muda em relação ao anterior

O loop protegido **fica no mesmo lugar, mas perde vértices em volta**. A
proteção vale para as arestas do loop, então os loops que cruzam ele podem
sair. Antes o anel ficava com todos os vértices e o resto do braço virava
triângulos grandes.

## Geometry Nodes

Com **Use Modifiers (Geometry Nodes)** ligado, o addon usa a malha com os
modificadores aplicados. Ele funciona até num objeto que só tem edges e gera o
tubo pelos nodes. O Armature fica desligado na hora de ler e continua nos LODs.

## Testado no Blender 5.2.0

`loop_lod_testes/`: boneco simétrico, com 2.496 triângulos, um anel protegido
em cada cotovelo, uma seam ao longo de cada braço e o punho sharp.

| LOD | Tris | Anel do cotovelo | Seam | Sem espelho | N-gons |
|---|---|---|---|---|---|
| 0 | 2.496 | 16 vértices | inteira | 0 | 0 |
| 1 | 1.232 | 16 | inteira | 0 | 0 |
| 2 | 608 | 13 | inteira | 0 | 0 |
| 3 | 304 | 8, no mesmo lugar | inteira | 0 | 0 |

Ainda não foi testado num personagem de produção.
