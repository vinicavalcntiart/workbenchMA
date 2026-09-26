---
titulo: MANIFESTO — Transcrições de palestras Blender sobre hair curves, grooming e simulação de cabelo
coletado_em: 2026-09-26
---

# Manifesto da coleta

Escopo: transcrições em texto de palestras da Blender Conference (BCON) e vídeos oficiais do canal Blender / Blender Studio sobre **hair curves, grooming com Geometry Nodes, curves sculpt e simulação de hair**. Conteúdo estritamente Blender — nenhum vídeo sobre XGen, Houdini ou addons de terceiros foi incluído.

## Método de coleta

1. Busca inicial via API pública do video.blender.org (PeerTube):
   `https://video.blender.org/api/v1/search/videos?search=<termo>&count=50`, com os termos: `hair`, `grooming`, `curves`, `hair curves`, `geometry nodes hair`, `hair simulation`, `fur`, `Lukas Tonne`, `Cosmos Laundromat`, `Bystedt`, `Matsumoto`, `hair system`, `sculpt hair`, `particle hair`, `hair nodes`. Isso cobriu ~150 vídeos únicos e permitiu localizar o UUID de cada palestra-alvo.
2. **Nenhum dos vídeos-alvo tinha legenda (`captions`) publicada no video.blender.org** (`GET /api/v1/videos/<uuid>/captions` retornou `{"total":0,"data":[]}` para todos). Por isso, seguindo a regra de fallback do brief, a coleta de transcrição foi feita via **YouTube** (canal oficial "Blender" / "Blender Studio"), localizando cada vídeo por busca de título exato e confirmando o canal/autor via `oembed`.
3. Extração das legendas automáticas (ASR, inglês) do YouTube: inicialmente via scraping da página + endpoint `timedtext` (bloqueado por captcha/429 na maior parte das tentativas), depois com sucesso via `yt-dlp --write-auto-sub --sub-lang en --extractor-args youtube:player_client=android` (e `player_client=ios` como alternativa). As legendas `.vtt` foram convertidas para texto corrido com um script Python (remove timestamps/tags, remove duplicatas consecutivas).
4. Metadados (palestrante, evento/ano, URL, duração, data) foram confirmados cruzando a descrição do vídeo no `video.blender.org` (quando existente) com os dados do YouTube.
5. Cada arquivo `.md` traz: cabeçalho YAML (título, palestrante, evento/ano, URLs, duração, data, idioma, fonte da legenda), a transcrição integral (legenda automática, sem cortes — pode conter pequenos erros de reconhecimento de fala, mantidos como estão, já que o texto é ASR e não editorial) e uma seção `## Pontos técnicos (resumo em português)` com 10–20 bullets cobrindo nomes de nodes, ordem de operações, valores e problemas/soluções citados.

## Observações importantes

- Nenhuma legenda humana (não-ASR) foi encontrada para nenhum dos vídeos; todo o texto vem de legendas automáticas do YouTube (idioma "en", tipo "asr"). Pequenos erros de transcrição de nomes próprios foram anotados quando identificados (ex.: "doniel bisat" = Daniel Bystedt).
- A palestra de Lukas Tönne ("Hair Simulation: From Cosmos Laundromat to Geometry Nodes", BCON 2025) **não foi encontrada no video.blender.org** nas buscas realizadas (termos "hair simulation", "Lukas Tonne", "Cosmos Laundromat" não a retornaram); foi coletada via YouTube, canal oficial "Blender". Não foi encontrada uma segunda versão ("re-record") desta palestra nas buscas feitas — aparenta existir apenas uma gravação publicada.
- A palestra "Building a Complete Animation Pipeline for a Feature Film with a Woolly Look" (BCON26) fala majoritariamente sobre o pipeline geral de lookdev/lighting do longa "Pikkuli and the Starlight Reindeer"; o segmento de "groom"/pelo é uma parte dela — isso está sinalizado no próprio arquivo.
- A palestra "How to Make Procedural Fur in Blender Geometry Nodes" (Blender Studio, referenciada no vídeo "Introducing: Hair Assets in Blender 3.5!" como o tutorial complementar) teve a coleta de legenda dificultada por bloqueio persistente (HTTP 429) do endpoint de legendas do YouTube mesmo após múltiplas tentativas com diferentes clientes (`android`, `ios`) e atrasos — ver status na tabela abaixo.
- Todos os vídeos coletados são do canal oficial "Blender" ou "Blender Studio" no YouTube (confirmado via `oembed`), e a maioria também está espelhada no video.blender.org (PeerTube) — as duas URLs são citadas no cabeçalho de cada arquivo quando disponíveis.

## Tabela de arquivos

| Arquivo | URL (video.blender.org / YouTube) | Palavras | Status |
|---|---|---|---|
| bcon2023-daniel-bystedt-character-grooming-hair-system.md | https://video.blender.org/videos/watch/2982655c-be93-4e5b-9bc5-267808e35d84 · https://www.youtube.com/watch?v=Kx88edAbiek | 5568 | ok |
| bcon2024-sara-matsumoto-mesh-hair-geometry-nodes-hair-curves.md | https://video.blender.org/videos/watch/08f2a8f0-c44f-43f7-a4d7-15291b95fdcf · https://www.youtube.com/watch?v=vXBL-oiqY7Q | 8563 | ok |
| bcon2025-lukas-tonne-hair-simulation-cosmos-laundromat-geometry-nodes.md | não encontrado em video.blender.org · https://www.youtube.com/watch?v=sfUDDKSx-1c | 8075 | ok |
| bcon2025-kerstin-schmidbauer-million-little-curves-animal-hair.md | https://video.blender.org/videos/watch/49ebc80d-91fd-4179-8129-72815fa15807 · https://www.youtube.com/watch?v=ZrBbNhCgGww | 7401 | ok |
| bcon2026-christopher-strommer-grooming-seth-rogen.md | https://video.blender.org/videos/watch/57dda10e-4126-44db-b505-dddbfb9d5875 · https://www.youtube.com/watch?v=t9vW-93qaN4 | 4469 | ok |
| bcon2026-steve-chow-photoreal-cat-hair-curves.md | https://video.blender.org/videos/watch/5d00cdb9-c671-43dd-bd29-9deb792d7d11 · https://www.youtube.com/watch?v=SYR4oBiezbc | 3467 | ok |
| bcon2026-bigwater-studios-pikkuli-woolly-look-pipeline.md | https://video.blender.org/videos/watch/fe848992-2113-4631-810d-5d340ce5e696 · https://www.youtube.com/watch?v=P0RvjSfFyLg | 9268 | ok |
| blender-2022-andy-goralczyk-future-of-hair-grooming.md | https://video.blender.org/videos/watch/ab9e8e34-4034-4cdd-98e6-c4aeac0bb565 · https://www.youtube.com/watch?v=6_USH9c_vNU | 3856 | ok |
| blender-2023-simon-thommes-hair-assets-3-5-introducao.md | https://video.blender.org/videos/watch/442b63e6-5f23-4eed-b812-6276bb9c8ea4 · https://www.youtube.com/watch?v=_-d0HaT5f1g | 1964 | ok |
| blender-studio-2021-simon-thommes-hairspray-effects-geometry-nodes.md | https://video.blender.org/videos/watch/52e3f65a-a202-4d05-8bfb-70f1a805228a · https://www.youtube.com/watch?v=T7g4y-lAL9w | 1713 | ok |
| (não gerado) "How to Make Procedural Fur in Blender Geometry Nodes" (Blender Studio, complemento do vídeo de Hair Assets 3.5) | https://video.blender.org/videos/watch/4e8115eb-3230-450e-a6d0-eb56d327bbaf · https://www.youtube.com/watch?v=gCQN5vNgHiI | — | não coletado — legenda automática do YouTube bloqueada por rate-limit/429 persistente em todas as tentativas (client android e ios, múltiplos atrasos); vídeo também não tem legenda no video.blender.org. Conteúdo é citado por referência no arquivo `blender-2023-simon-thommes-hair-assets-3-5-introducao.md`. |

## Outros vídeos considerados e descartados da coleta detalhada

Vídeos do tipo "Blender.Today LIVE" (streams de desenvolvimento de várias horas) que mencionam cabelo em seus títulos foram identificados mas **não transcritos** por serem lives de várias horas sobre estado de desenvolvimento (não palestras estruturadas) e por não terem legendas disponíveis nem no video.blender.org nem indício de legenda no YouTube verificado nesta coleta: "HAIR SCULPT MODE - Blender.Today LIVE #183" (2022), "HAIR IMPROVEMENTS - Blender.Today LIVE #192" (2022), "HAIR STUFF! - Blender.Today LIVE #214" (2023), "NEW HAIR SHADER - Blender Today LIVE #234" (2023). Citados aqui apenas para registro; podem ser revisitados em uma coleta futura se necessário.
