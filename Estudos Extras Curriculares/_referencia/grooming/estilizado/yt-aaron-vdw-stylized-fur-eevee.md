---
titulo: "Make stylized fur and hair in Blender (Eevee)"
autor: Aaron Van de Weijenberg
url: https://www.youtube.com/watch?v=XiylyjCpljs
data: 2025-10-02
tipo: video
versao_blender: nao informado
coletado_em: 2026-09-28
---

## Nota de coleta

Video de 16min09s, canal youtube.com/@aaronvdw. Existencia e descricao
confirmadas por oEmbed em duas tentativas (a primeira falhou por
instabilidade da conexao, a segunda trouxe titulo, canal, data e a
descricao completa com os capitulos abaixo). A transcricao automatica nao
pode ser baixada nesta sessao: o YouTube bloqueou o yt-dlp (HTTP 429 e
captcha anti-bot) em todos os clientes testados. O conteudo abaixo vem
apenas da descricao publica do autor, que neste caso e detalhada o
suficiente para dar uma receita de alto nivel (por etapa, sem valores de
parametro).

Descricao do autor: "In this video I'll show you how I manage colors,
shadows and normals to create stylized fur in EEVEE using Blender's
geometry nodes hair system. As a bonus I show a simple way to animate a
wind effect. This technique will work particularly well for anime style."

Capitulos do autor:
[00:00] Intro
[00:25] Creating the fur
[03:00] Shadows
[03:44] Normals
[06:14] Converting normals object space
[07:35] Painting fur colors
[11:42] Animating wind effect

## Receita

Ordem das etapas (do titulo dos capitulos, sem valores, ja que a
transcricao nao pode ser coletada):

1. Gerar o fur com o sistema nativo de hair curves + geometry nodes do
   Blender (capitulo "Creating the fur"). Valor nao informado (contagem de
   guias, densidade, comprimento).
2. Resolver sombra do fur separadamente (capitulo "Shadows"). Tecnica nao
   informada, mas o fato de ter um capitulo dedicado sugere que o autor usa
   algo alem da sombra padrao do Eevee para o pelo, coerente com o objetivo
   de silhueta legivel em vez de sombra realista.
3. Ajustar normais do fur (capitulo "Normals", depois "Converting normals
   object space"). Converter normal para espaco de objeto e uma tecnica
   comum para simular "fake shading" de fur em toon shaders, mas o autor
   nao descreve o node exato aqui, so o nome do capitulo.
4. Pintar cor por regiao do fur (capitulo "Painting fur colors"). Isso bate
   com o principio de estudio "cor por mecha/clump" citado nos papers da
   DreamWorks (ver `artigo-dreamworks-puss-in-boots-fur.md` nesta pasta),
   mas aqui e pintura direta, nao clump coloring automatico. Valor nao
   informado (metodo de pintura: vertex paint, textura, ou atributo).
5. Animar vento (capitulo "Animating wind effect"), descrito pelo autor
   como "simple way". Metodo nao informado.

## Truques

- O autor afirma que a tecnica funciona bem para "anime style", ligando
  fur estilizado a normais convertidas para espaco de objeto e sombra
  controlada a parte, em vez de depender so da iluminacao fisica do
  Eevee.
- Separar "criar o fur" de "resolver sombra" e "resolver normal" como
  passos distintos sugere que, no fluxo dele, a leitura toon do pelo vem
  do shading, nao da geometria do clump. Isso e coerente com o principio
  de estudio do Wild Robot (ver `artigo-dreamworks-wild-robot-painterly.md`):
  fur/fio tratado para reagir a luz como superficie, nao como fio realista.

## Transcrição

Nao disponivel (YouTube bloqueou a coleta nesta sessao). Conteudo acima
limitado a titulo, descricao e capitulos publicados pelo autor.
