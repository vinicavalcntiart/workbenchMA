# Manifesto da coleta: cabelo e pelo estilizado (Blender, Geometry Nodes)

Coleta feita em 2026-09-28. Escopo: cabelo/pelo com visual estilizado
(Disney, Pixar, DreamWorks, Sony Animation, "cartoon") usando so hair
curves nativas e node groups da Essentials, mais principios de estudio
(traduzidos para GN, nunca receitas literais). Proibido addon de
terceiros; toda fonte com addon foi descartada.

## Metodo de coleta

- Busca no YouTube via `ytsearch.py` (scraping de `ytInitialData`), em
  ingles e espanhol/portugues/japones. Metadados (titulo, canal, data,
  descricao, capitulos) via `ytvid3.py` e oEmbed.
- **Transcricao de video: bloqueada nesta sessao.** Toda tentativa de
  `yt-dlp --write-auto-sub` (clientes android, ios, tv, web_embedded,
  mweb, web_safari), de `youtube_transcript_api`, do endpoint
  `timedtext` direto e de espelhos Invidious publicos (inv.nadeko.net,
  yewtu.be, invidious.jing.rocks, vid.puffyan.us) falhou com HTTP 429
  ("Too Many Requests") ou captcha "Sign in to confirm you're not a
  bot"/reCAPTCHA. O IP deste ambiente ja tinha sido usado para varias
  buscas no YouTube antes desta tarefa (evidencia: arquivos antigos
  `yt1.html`, `yt_test.html` no scratchpad), o que provavelmente
  contribuiu para o bloqueio. Por isso, todo arquivo de video nesta
  pasta usa so titulo, descricao publica e capitulos (quando existem)
  como fonte, nunca a fala do autor. Isso esta marcado explicitamente em
  cada arquivo de video, na secao "Nota de coleta" e na secao
  "Transcrição".
- WebSearch e WebFetch para blogs, BlenderArtists, SIGGRAPH/ACM,
  Pixar/Disney/DreamWorks. Threads do BlenderArtists foram lidas via API
  JSON publica do Discourse (`/t/<slug>/<id>.json`), que nao tem o
  bloqueio anti-bot que o HTML normal do forum tem.
- Todo URL usado como fonte foi verificado por fetch direto (HTTP 200)
  nesta sessao, exceto os casos marcados abaixo como "verificado por
  oEmbed" (videos, onde o fetch direto do HTML deu 429 mas o oEmbed
  confirmou titulo e canal) ou "existencia confirmada, conteudo nao
  lido" (paginas com bloqueio de bot/paywall, HTTP 403).

## Fontes usadas (arquivo, uma linha)

1. `yt-sina-sinaie-serie-stylized-hair-gn.md`: 3 videos do canal Sina
   Sinaie sobre "stylized hair with geometry nodes" (2023 e 2025).
   Verificado por oEmbed. Sem transcricao, sem descricao tecnica; valor
   baixo, mas confirma o genero de tutorial.
2. `yt-aaron-vdw-stylized-fur-eevee.md`: video de Aaron Van de
   Weijenberg sobre fur estilizado com cor pintada, normais e sombra
   controlada a parte (2025). Verificado por oEmbed, descricao com
   capitulos.
3. `yt-blender-studio-procedural-fur.md`: tutorial oficial do canal
   Blender Studio (Simon Thommes), Blender 3.5, com capitulos detalhados
   incluindo "Detail Layering (Frizz + Clumping)" (2023). Verificado por
   oEmbed.
4. `ba-hair-stylized-curve-tilt-twist.md`: thread do BlenderArtists
   (2022) com receita real de twist de perfil de curva via Set Curve
   Tilt + Spline Parameter + Float Curve + Multiply, para simular mecha
   em fita torcida. Verificado via API JSON, texto lido por inteiro.
5. `ba-tolkfan-chonky-stylized-hair.md`: post do BlenderArtists (2022)
   descrevendo hair sculpting (Blender 3.3 alpha) + geometry nodes para
   "chonky stylized hair". Verificado via API JSON, texto lido por
   inteiro.
6. `artigo-80lv-sculpting-stylized-hair.md`: cobertura jornalistica do
   mesmo post do Tolkfan. Fetch direto confirmado.
7. `siggraph-pixar-brave-curly-hair.md`: principios do cabelo cacheado de
   Merida (Brave/Valente, Pixar 2012), via artigo da fxguide com
   entrevista da equipe. Fetch direto confirmado.
8. `siggraph-dreamworks-trolls-hairy-effects.md`: paper SIGGRAPH 2017
   "Hairy Effects in Trolls". PDF lido por inteiro.
9. `artigo-dreamworks-puss-in-boots-fur.md`: entrevista tecnica sobre o
   pelo estilizado de Puss in Boots: The Last Wish (befores & afters,
   2023). Fetch direto confirmado.
10. `artigo-dreamworks-wild-robot-painterly.md`: entrevista sobre o
    visual "impressionista" de The Wild Robot (Creative Bloq, 2024).
    Fetch direto confirmado (texto completo extraido via curl, o
    WebFetch generico so trouxe o menu).
11. `artigo-disney-tangled-rapunzel-hair.md`: cabelo de Rapunzel em
    Tangled (Disney 2010), via artigo 80.lv mais pagina oficial de
    publicacao da Disney. Fetch direto confirmado.
12. `siggraph-disney-moana-hair.md`: paper SIGGRAPH 2017 "The Art and
    Technology of Hair Simulation in Disney's Moana". PDF lido por
    inteiro.

Total: 12 arquivos, cobrindo 14 fontes primarias distintas (a serie Sina
Sinaie conta 3 videos num arquivo so).

## O que foi descartado e por que

**Por usar addon de terceiros (proibido pelo escopo):**
- Dean Zarkov, "How to Create Stylized Hair Shapes with Geometry Nodes"
  (youtube.com/watch?v=xcpRdrynShE): o proprio video depende de um node
  group vendido no Gumroad como "Stylized Hair PRO"; descartado.
- ItsPaulTodd, "How to create FAST Stylized Hair/Fur in Blender 4.0"
  (youtube.com/watch?v=ethg2nYSjqg): descricao confirma que e modelagem
  de curva Bezier convertida a mao para mesh, sem o sistema de hair
  curves nem geometry nodes; fora de escopo.
- PixelicaCG, "Ultimate Guide to Creating Stylized Hair in Blender"
  (youtube.com/watch?v=QocAk6TNKp4): mesh de mecha com modificador de
  curva manual, promovendo um "Hair System" pago no Gumroad; fora de
  escopo (nao e o sistema de hair curves nativo).
- Thread BlenderArtists "Geometry Nodes Stylized Hair"
  (blenderartists.org/t/geometry-nodes-stylized-hair/1455508) e "Hair
  using Geometry Nodes" pag. 6
  (blenderartists.org/t/hair-using-geometry-nodes/1446696?page=6):
  o autor (Xeofrios) descreve dependencia do addon Bsurfaces para
  esculpir a superficie base; descartado.

**Por nao ser Blender/Geometry Nodes (fora de escopo tecnico):**
- hart, "The Secrets to Stylized Hair - Episode 1"
  (youtube.com/watch?v=NWg0V9V_7Pk): e escultura em ZBrush, nao Blender;
  descartado.

**Por falta de conteudo tecnico verificavel:**
- CGMatter, "Blender 5.0 Fur (Geometry Nodes)"
  (youtube.com/watch?v=yrUiVsdImLI): descricao publica so tem
  patrocinio (Squarespace), sem nenhuma pista de conteudo tecnico, e sem
  transcricao disponivel; descartado por risco de nao ser
  especificamente estilizado e por nao dar nada para citar com
  confianca.
- Thread BlenderArtists "Stylized Hair with Node tools"
  (blenderartists.org/t/stylized-hair-with-node-tools/1520904): so
  mostra resultado, sem node nem valor discutido no proprio thread;
  descartado.

**Por suspeita de nao ser fonte confiavel/real:**
- Site yelzkizi.org (varios artigos tipo "Realistic 3D Hair Clumping In
  Blender: Easy Step-by-Step Guide", "Blender Roll Hair Curves: 3D
  Comprehensive Guide" etc.): bloqueado por protecao anti-bot (Bunny
  Shield) em toda tentativa de fetch, sem autor identificado, com
  padrao de titulo tipico de fazenda de conteudo gerado para SEO.
  Descartado por nao dar para verificar quem escreveu nem se os valores
  citados nos resumos de busca sao reais.

**Por estar fora do foco de cabelo (mesmo sendo estilizado):**
- awn.com, "Creating A Stylized Universe for Sony's 'Spider-Man: Into
  the Spider-Verse'": lido por inteiro, mas o artigo fala de linework
  facial e composicao 2D, sem nenhuma mencao especifica a tecnica de
  cabelo; descartado por nao ter o que o brief pedia (Spider-Verse foi
  citado no brief como exemplo de estudio, mas esta fonte especifica nao
  entregou conteudo de cabelo).

**Bloqueadas por paywall/anti-bot, nao usadas diretamente:**
- CGW, "The Royal Treatment" (cgw.com, sobre Brave/Merida): HTTP 403 em
  toda tentativa; nao usada, ja que fxguide cobriu o mesmo material e
  foi verificavel.
- ACM Digital Library (dl.acm.org) para as sessoes tecnicas de Puss in
  Boots ("Visual Style of Puss In Boots: The Last Wish") e de The Wild
  Robot ("Painterly Fur and Feathers of The Wild Robot"): HTTP 403 em
  toda tentativa (paywall). Usadas as coberturas de imprensa
  (befores & afters, Creative Bloq) no lugar, com a ressalva registrada
  em cada arquivo.
- DreamWorks, "The Fashionista Twins: Conjoined Hair in Trolls"
  (research.dreamworks.com): encontrado na busca mas nao perseguido;
  trata de rigging de cabelo fundido entre dois personagens, tema mais
  estreito e menos aplicavel a GN estilizado do que os outros papers ja
  cobertos.

**Ja coberto na base existente, nao duplicado aqui:**
- studio.blender.org/blog/procedural-hair-nodes (Simon Thommes, sobre o
  lancamento dos node groups Essentials): ja catalogado em
  `../blender-dev/studio-blender-2023-procedural-hair-nodes.md`. Citado
  por referencia nos arquivos desta pasta quando relevante, sem
  duplicar o arquivo.
- Artigos em japones sobre hair curves em geral (cgbox.jp, note.com
  "hair_drawings"): consultados, mas tratam de fluxo de hair curves
  realista/generico (perfil, frizz para parecer mais real), sem
  proposta estilizada especifica; fora do foco desta coleta.
