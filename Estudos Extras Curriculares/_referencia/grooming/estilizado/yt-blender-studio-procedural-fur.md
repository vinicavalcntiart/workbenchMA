---
titulo: "How to Make Procedural Fur in Blender Geometry Nodes"
autor: Blender Studio (canal oficial)
url: https://www.youtube.com/watch?v=gCQN5vNgHiI
data: 2023-03-29
tipo: video
versao_blender: "3.5"
coletado_em: 2026-09-28
---

## Nota de coleta

Video oficial do canal Blender Studio, 34min59s, 269 mil views. Existe
tambem como licao em texto/video em
studio.blender.org/training/geometry-nodes-from-scratch/how-to-make-procedural-fur-in-blender-35/,
ja catalogada em `../blender-dev/studio-blender-training-procedural-fur-blender-35.md`
(sem transcricao, so metadados). Este arquivo trata da versao YouTube, que
tem uma descricao com capitulos mais detalhada.

Nao e um tutorial de look "cartoon" explicito, e sim o tutorial de
referencia oficial do fluxo Essentials (guia -> interpolar -> clump ->
frizz -> shading), que e a base tecnica sobre a qual qualquer look
estilizado se constroi. Entra nesta pasta porque a etapa "Detail Layering"
descreve exatamente a tecnica de camadas de clump usada nas receitas de
mecha grossa.

A transcricao automatica nao pode ser baixada nesta sessao (YouTube
bloqueou o yt-dlp com HTTP 429 e captcha em todos os clientes testados).
O que segue vem da descricao publica, que neste video e uma lista de
capitulos com timestamps, publicada pelo proprio canal.

Descricao do autor: "Get a thorough introduction into the new procedural
hair grooming system in Blender 3.5 and learn how to freely stack and
combine procedural operations to create a highly detailed procedural fur
setup using the new node-based workflow."

Capitulos do autor:
00:00 Introduction
00:49 Base Setup
03:46 Initial Modifiers
08:28 Base Customization
10:58 Basic Curling + Guide Workflow
15:04 Detail Layering (Frizz + Clumping)
16:44 Shading + Rendering Setup
21:46 Add Random Variation
23:11 Move to Nodes
25:29 Basic Variation with Nodes
29:20 Additional Variation Detail
32:50 Detail Tweaking
33:57 Final Result

## Receita

Ordem das etapas, direto dos capitulos (nomes dos nodes internos nao
confirmados sem a transcricao, valor nao informado em todos os
parametros):

1. Base Setup: criar o objeto de fur/hair curves sobre a superficie.
2. Initial Modifiers: primeira stack de modificadores do sistema
   Essentials (provavelmente Interpolate Hair Curves como primeiro passo,
   coerente com a stack canonica documentada em `../CEREBRO_GROOMING.md`
   secao 2, mas isso e inferencia minha, nao veio do video).
3. Base Customization: ajuste dos parametros basicos (comprimento,
   densidade). Valor nao informado.
4. Basic Curling + Guide Workflow: aplicar curl nas guias antes de
   multiplicar em filhos, ou seja, Curl entra na guia, nao so no
   resultado final.
5. Detail Layering (Frizz + Clumping): camada de detalhe combinando Frizz
   e Clump. A ordem exata entre os dois nao esta no titulo do capitulo.
6. Shading + Rendering Setup: material do pelo.
7. Add Random Variation: variacao aleatoria por fio ou por clump. Metodo
   nao informado no titulo.
8. Move to Nodes: converter o modificador de UI de painel para o editor
   de nodes completo, ganhando acesso a parametros que o painel do
   modificador nao expoe. Isso confirma o principio ja registrado em
   `../CEREBRO_GROOMING.md`: "os grupos sao assets embarcados; o mesmo
   grupo pode ser aberto no editor de nodes para ir alem do que o painel
   do modificador expoe".
9. Basic Variation with Nodes / Additional Variation Detail / Detail
   Tweaking: refinamento incremental dentro do editor de nodes.

## Truques

- A etapa "Detail Layering (Frizz + Clumping)" nomeada assim (nessa ordem)
  sugere que o Blender Studio recomenda clumping como camada de detalhe,
  depois ou junto do frizz, nao so como primeira operacao. Isso e consistente
  com receitas de mecha grossa estilizada que usam 2 niveis de clump (macro
  e micro) e so depois adicionam frizz sutil por cima.
- "Move to Nodes" e citado como um passo formal do fluxo de trabalho
  oficial, nao um truque avancado escondido. Ou seja, o proprio estudio
  ensina que sair do painel do modificador e ir para o node editor e parte
  normal de qualquer setup de fur/hair um pouco mais customizado.

## Transcrição

Nao disponivel (YouTube bloqueou a coleta nesta sessao). Conteudo acima
limitado ao titulo, descricao e capitulos publicados pelo canal.
