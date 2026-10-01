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
4. Opcional: selecione mão ou rosto e clique em **Mark Selected as Locked**
   (grupo `LOD_Lock`). Essa área não muda em nenhum LOD. Os loops que chegam
   nela param na borda e viram um triângulo ali, então o braço continua
   reduzindo.

## O que muda em relação ao anterior

O loop protegido **fica no mesmo lugar, mas perde vértices em volta**. A
proteção vale para as arestas do loop, então os loops que cruzam ele podem
sair. Antes o anel ficava com todos os vértices e o resto do braço virava
triângulos grandes.

## Versão 1.1 (correções do teste no personagem)

- **N-gons:** toda face com mais de 4 lados é triangulada no fim de cada
  passada.
- **Non-manifold:** cada lote é conferido. Se aumentar o non-manifold, o lote
  volta e os loops entram um a um; os que quebram ficam marcados e não são
  tentados de novo.
- **Raio do braço:** só o anel marcado fica. Um loop é tratado como anel
  protegido quando 85% ou mais das arestas dele estão no grupo. Os loops que
  correm ao longo do braço podem sair mesmo cruzando vários anéis.
- **Shape Balance (novo, padrão 1,0):** mantém as faces perto de quadradas.
  Sem isso, num braço reto os anéis no comprimento saem primeiro (erro zero) e
  o raio só cai nos últimos LODs. Com 1,0 o anel cai de 16 para 12 já no LOD1.
  Em 0 volta ao comportamento anterior.
- **Locked Areas (novo):** grupo `LOD_Lock`, descrito no passo 4.

## Versão 1.2 (topologia para deformação)

O LOD3 da 1.1 tinha a ponta do braço dobrada sobre si mesma (cunha escura no
render). Não era non-manifold: a malha estava fechada, mas 8 arestas tinham as
faces viradas uma contra a outra, porque o anel chegou a 5 vértices.

- **Min Ring Verts (novo, padrão 8):** nenhum anel fechado (braço, perna,
  dedo) e nenhuma abertura (barra, gola, punho) fica com menos vértices que
  isso. 8 segura volume e deformação de cotovelo e joelho. Em 0 desliga.
- **Checagem de dobra:** além do non-manifold, cada lote é desfeito se criar
  aresta com as faces a mais de ~100 graus.
- **Só quads:** desligue **Pole Fallback**. O addon para quando acabam os loops
  limpos, sem triângulos novos, mas não chega aos LODs mais baixos.

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

### Teste 1.1: roupa com braços (`t_roupa_braco_520.py`)

Robe simétrico com 1.752 triângulos, braços extrudados em 12 passos, 3 anéis
protegidos no cotovelo e 2 no punho, pescoço em leque (polo cheio de
triângulos) e seams nas laterais. Imagem: `lods_braco_sheet_v2.jpg`.

| LOD | Tris (alvo) | Anéis do cotovelo | N-gons | Non-manifold | Sem espelho | Seams |
|---|---|---|---|---|---|---|
| 0 | 1.752 | 16 vértices | 0 | 0 | 0 | 2 cadeias |
| 1 | 840 (876) | 12 | 0 | 0 | 0 | 2 cadeias |
| 2 | 438 (438) | 8 | 0 | 0 | 0 | 2 cadeias |
| 3 | 344 (219) | 8, no mesmo lugar | 0 | 0 | 0 | 2 cadeias |

Na 1.2 (`lods_braco_sheet_v3.jpg`): zero dobras em todos os LODs, a barra do
robe para em 8 vértices (na 1.1 caía para 4) e o LOD3 para em 344 triângulos
por causa do anel mínimo. Quads e triângulos: LOD1 408/24, LOD2 190/58, LOD3
106/132 (os triângulos novos ficam na axila e no ombro, pelo Pole Fallback).

Com Pole Fallback desligado (`t_roupa_so_quads_520.py`): nenhum triângulo novo
(os 24 são do leque do pescoço original), mas o LOD2 e o LOD3 param em 552.

Com a mão travada (`t_roupa_mao_travada_520.py`): a mão fica com os 82
vértices em todos os LODs e o anel do cotovelo cai 16, 12, 8, 8. O LOD2 e o
LOD3 param em 490 triângulos porque a mão não entra na conta.

Ainda não foi testado no personagem de produção depois da versão 1.2.
