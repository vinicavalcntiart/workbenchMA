---
titulo: "Help! Hair Stylized - Geometry nodes"
autor: "Metrons (pergunta), Charles_Weaver (resposta)"
url: https://blenderartists.org/t/help-hair-stylized-geometry-nodes/1405817
data: 2022-09-09
tipo: thread
versao_blender: nao informado
coletado_em: 2026-09-28
---

## Nota de coleta

Thread do Blender Artists, coletada via API JSON publica do Discourse
(`/t/help-hair-stylized-geometry-nodes/1405817.json`), que nao tem o
bloqueio anti-bot que o HTML normal do site tem. Datas e texto abaixo sao
literais do post.

## Receita

Contexto do post original (Metrons, 09/09/2022): ele fazia cabelo
estilizado para um jogo com o metodo antigo, mesh/curva comum, nao hair
curves: "Create a curve, assign a profile, taper the end point and
duplicate the curve over and over." Ele pergunta como reproduzir esse
efeito de mecha em fita, com ponta afiada, usando geometry nodes.

Resposta de Charles_Weaver (10/09/2022), unica solucao concreta no thread:

1. **Set Curve Tilt**: usar esse node com o parametro Spline Parameter
   para torcer o perfil da curva ao longo do fio. Isso da o giro que faz
   uma mecha "fita" ler como fita e nao como cilindro reto.
2. **Float Curve**: usado para desenhar o falloff da torcao (por exemplo,
   mais torcao perto da ponta, menos na raiz, ou vice versa). Valor nao
   informado (formato exato da curva).
3. **Multiply**: usado depois do Float Curve para escalar a forca do
   falloff. Valor nao informado.

Limitacao registrada no proprio thread: o autor original (Metrons) aponta
que essa solucao torce todas as mechas igual, e pergunta como variar a
torcao mecha por mecha: "What if I wanted to... Adjust the twisting on an
individual curve though? I really miss the control of the old style
curves where I could just grab a point and twist. I can't think of a way
where I can do this without affecting every hair strand?" Ninguem
responde essa parte no thread. Ou seja, a receita acima resolve torcao
global, nao variacao por guia.

## Truques

- Twist de perfil de curva com Set Curve Tilt + Spline Parameter e a base
  nativa (sem addon) para simular o efeito de "mecha em fita torcida" que
  no metodo antigo se fazia manualmente ponto a ponto.
- Combinar Set Hair Curve Profile (perfil achatado, tipo fita, nao
  circular) com esse twist do Set Curve Tilt e o caminho mais provavel
  para reproduzir o visual descrito pelo autor original ("assign a
  profile, taper the end point"), mas essa combinacao especifica nao foi
  testada nem confirmada no thread, e inferencia minha.
- Se quiser variacao por guia (o problema nao resolvido no thread), o
  caminho nativo seria usar Create Guide Index Map ou um atributo por
  curva (indice da curva) como entrada do Float Curve, em vez do Spline
  Parameter sozinho. Isso nao esta no thread, e sugestao minha a partir do
  que se sabe da stack Essentials (ver `../CEREBRO_GROOMING.md`).
