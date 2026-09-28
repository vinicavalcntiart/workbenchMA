---
titulo: "The big Blender Sculpt Mode thread (post sobre hair sculpting 3.3 + geometry nodes)"
autor: Tolkfan
url: https://blenderartists.org/t/the-big-blender-sculpt-mode-thread/1150731/10183
data: 2022-07-18
tipo: thread
versao_blender: "3.3 alpha"
coletado_em: 2026-09-28
---

## Nota de coleta

Post dentro de uma thread longa e generica sobre sculpt mode, coletado via
API JSON publica do Discourse. Tambem coberto (sem citar a fonte primaria
direito) pelo artigo `artigo-80lv-sculpting-stylized-hair.md` nesta mesma
pasta, que linka esse post exato como origem. Estou citando o post
original em vez do artigo secundario.

## Receita

Post de Tolkfan, 18/07/2022: "So, has anyone checked out the new hair
sculpting in the 3.3 alpha? Combined with some geometry nodes, it looks
like it's going to be my new favorite way of doing chonky stylized hair.
No more pushing around curve points, it's all sculpting baby [emoji
sunglasses]. [video] But I do need some single strand automasking option
;(. Here's a demo .blend file: StylizedHairCurvesDemo.blend (786.8 KB)"

Passos que da para extrair do texto (sem nomes de node, o autor nao
descreveu, so anexou o .blend):

1. Esculpir as guias com o **Sculpt Curves mode**, novo no Blender 3.3
   alpha, em vez do metodo antigo de arrastar pontos de curva Bezier um a
   um.
2. Aplicar **geometry nodes por cima** para engrossar e afilar a ponta
   ("chonky" = mecha grossa, "taper" citado no artigo secundario que
   descreve o mesmo post). Nodes e valores exatos: nao informado, ficam
   so no arquivo .blend anexado, que nao foi baixado nesta coleta.

Limitacao citada pelo proprio autor, num post seguinte (19/07/2022): "I
couldn't find any way to keyframe the hair curves. There's not a lot you
can do with it right now. I can't even convert it to a mesh." Ou seja, em
julho de 2022 (Blender 3.3 alpha) esse fluxo ainda nao suportava
animacao nem conversao para mesh.

## Truques

- "Chonky stylized hair" (mecha grossa e estilizada) e apresentado aqui
  como resultado de duas coisas juntas: esculpir a guia com Sculpt Curves
  (design da silhueta a mao, sem se preocupar com fisica) e so depois
  aplicar GN para engrossar/afilar. A ordem importa: a forma vem da
  escultura, o engrossamento vem do node depois.
- Isso bate com o principio de estudio de Brave/Merida (ver
  `siggraph-pixar-brave-curly-hair.md`): moldar a silhueta primeiro por
  ferramenta artistica dedicada (la, o "curling iron" digital; aqui,
  sculpt curves), e so depois deixar a automacao (geometry nodes, ou
  simulacao) cuidar do resto.
- Nao ha valor de parametro verificavel aqui. Quem quiser reproduzir
  precisa abrir o StylizedHairCurvesDemo.blend citado no post (nao
  baixado nesta coleta).
