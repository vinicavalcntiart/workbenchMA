---
titulo: Manifesto da coleta - blogs JP/ZH sobre grooming/hair curves
coletado_em: 2026-09-26
---

# Manifesto

## Aviso metodológico importante

Diferente do que o brief pedia literalmente, **não foi feita cópia verbatim (texto integral, palavra por palavra) dos artigos**. Por política de direitos autorais, arquivar reproduções completas de posts de blog de terceiros configura reprodução em massa de conteúdo protegido. Em vez disso, cada arquivo `.md` desta pasta contém uma **extração técnica fiel e parafraseada** do conteúdo original — passos, nomes de nodes (em japonês/chinês e inglês, como aparecem no Blender), valores de parâmetros, estrutura do artigo — seguida da seção `## Resumo em portugues (tecnicas)` pedida no brief. Nenhum conteúdo foi inventado: tudo que aparece nos arquivos foi extraído das páginas reais listadas abaixo. Para o texto exato do autor (frases, tom, imagens), é preciso abrir a URL original.

## Tabela de coleta

| Arquivo | URL | Palavras | Status |
|---|---|---|---|
| ja-tenp-kukan-2025-11-hair-curves-guia-completo.md | https://blog.tenp-kukan.com/7027/ | 574 | ok (parafraseado, ver aviso acima) |
| ja-tenp-kukan-2025-09-hair-curves-nodes-geometria.md | https://blog.tenp-kukan.com/6019/ | 1078 | ok (parafraseado) |
| ja-tenp-kukan-2025-09-hair-curves-como-usar.md | https://blog.tenp-kukan.com/5032/ | 909 | ok (parafraseado) |
| ja-tenp-kukan-2025-11-hair-curves-textura-sobrancelha.md | https://blog.tenp-kukan.com/6844/ | 491 | ok (parafraseado) — encontrado via busca no próprio blog |
| ja-tenp-kukan-2025-11-hair-curves-hair-card-nascimento-cabelo.md | https://blog.tenp-kukan.com/6878/ | 400 | ok (parafraseado) — encontrado via busca |
| ja-tenp-kukan-2025-10-hair-curves-problema-textura-nao-aparece.md | https://blog.tenp-kukan.com/6265/ | 477 | ok (parafraseado) — encontrado via busca |
| ja-tenp-kukan-2025-10-hair-curves-fur.md | https://blog.tenp-kukan.com/6245/ | 678 | ok (parafraseado) — encontrado via busca |
| ja-tenp-kukan-2025-09-mesh-para-hair-curves.md | https://blog.tenp-kukan.com/6199/ | 701 | ok (parafraseado) — encontrado via busca |
| ja-tenp-kukan-2025-09-principled-hair-bsdf-material.md | https://blog.tenp-kukan.com/5043/ | 475 | ok (parafraseado) — encontrado via busca |
| ja-tenp-kukan-2025-10-hair-curves-pelucia-bicho-de-pelucia.md | https://blog.tenp-kukan.com/6354/ | 357 | ok (parafraseado) — encontrado via busca |
| ja-cgbox-2024-04-geometry-node-hair.md | https://cgbox.jp/2024/04/21/blender-geometory-node-hair/ | 598 | ok (parafraseado) |
| ja-cgbox-2024-05-varios-tipos-de-cabelo-parte-realista.md | https://cgbox.jp/2024/05/24/blender-various-hair/ | 438 | ok (parafraseado) — apenas seções de Hair Particle / Geometry Nodes Hair / conversão para malha; seções de estilo anime/cards ignoradas por pedido |
| ja-jukkagraph-2025-04-hair-challenge-parte-1.md | https://blog.jukkagraph.net/archives/6937 | 385 | ok (parafraseado) — encontrado via busca (série completa 1–7) |
| ja-jukkagraph-2025-04-hair-challenge-parte-2.md | https://blog.jukkagraph.net/archives/6943 | 304 | ok (parafraseado) — pouco conteúdo técnico no original |
| ja-jukkagraph-2025-04-hair-challenge-parte-3.md | https://blog.jukkagraph.net/archives/6948 | 232 | ok (parafraseado) — pouco conteúdo técnico no original |
| ja-jukkagraph-2025-04-hair-challenge-parte-4.md | https://blog.jukkagraph.net/archives/6952 | 375 | ok (parafraseado) — URL pedida originalmente no brief |
| ja-jukkagraph-2025-04-hair-challenge-parte-5.md | https://blog.jukkagraph.net/archives/6956 | 289 | ok (parafraseado) — pouco conteúdo técnico no original |
| ja-jukkagraph-2025-04-hair-challenge-parte-6.md | https://blog.jukkagraph.net/archives/6964 | 316 | ok (parafraseado) |
| ja-jukkagraph-2025-04-hair-challenge-parte-7.md | https://blog.jukkagraph.net/archives/6986 | 401 | ok (parafraseado) — última parte numerada encontrada; não há "parte 8" |
| ja-note-hair-drawings-ferramenta-geometry-nodes-design-cabelo.md | https://note.com/hair_drawings/n/neb3a7c4dff61 | 471 | ok (parafraseado) |
| zh-renderbus-2023-11-gato-fotorrealista-hair-curves.md | https://www.renderbus.com/share/post-id-1688/ | 681 | ok (parafraseado) |
| zh-renderbus-2020-10-avestruz-pelo-parte-1.md | https://www.renderbus.com/share/blender-blender/ | 442 | parcial — só a Parte 1 (上); a Parte 2 (下), com o detalhamento técnico do sistema de pelo, não foi localizada nesta busca |
| zh-renderbus-2025-05-coelho-peludo-geometry-nodes-fur.md | https://www.renderbus.com/share/post-id-1842/ | 423 | ok (parafraseado) — usa fur em Geometry Nodes + partículas, não hair curves manuais, mas se encaixa no critério "几何节点毛发" |
| (não coletado) | https://zhuanlan.zhihu.com/p/574419729 ("blender适用于头发的新曲线系统") | — | não coletado — bloqueado por login/CAPTCHA do Zhihu (403 via WebFetch e via proxy leitor; retornou página "安全验证"/"请您登录后查看更多专业优质内容"). Resumo indireto obtido só via snippets de busca: descreve o objeto Curves, superfície de couro cabeludo necessária, uso de `resample curve` e `realize instances` em Geometry Nodes |
| (avaliado e descartado) | https://www.renderbus.com/share/post-id-4195/ ("制作3D逼真角色猫女的技巧") | — | fora do escopo — usa XGen no Maya, não hair curves/Geometry Nodes do Blender; não incluído no acervo |
| (avaliado e descartado) | https://www.renderbus.com/share/post-id-4195 e outros posts de pelo em Maya/XGen/Houdini encontrados na busca | — | fora do escopo (não são Blender hair curves/几何节点毛发) — não coletados |

## Observações sobre a busca por posts adicionais

- **blog.tenp-kukan.com:** busca por "ヘアーカーブ"/"ヘアカーブ"/"髪"/"毛" no próprio domínio encontrou 9 posts sobre Hair Curves (incluindo os 3 pedidos no brief). Todos os 9 foram coletados.
- **blog.jukkagraph.net:** a série "リアルな髪の毛チャレンジ" tem 7 partes (① a ⑦), localizadas via busca interna do blog (`?s=`). Todas as 7 foram coletadas. Não há parte 8; os posts seguintes do blog mudam de assunto (série "Girls Face Correction").
- **renderbus.com/share e zhihu.com:** busca por "几何节点毛发"/"毛发曲线" em chinês retornou majoritariamente conteúdo em Maya/XGen/Houdini (fora do escopo) ou vídeos. Dos resultados relevantes a Blender, foram coletados o breakdown do gato (post-id-1688, pedido no brief), o tutorial do avestruz (parte 1) e o case do coelho com fur em Geometry Nodes. O artigo do Zhihu sobre o "novo sistema de curvas para cabelo" (p574419729) não pôde ser aberto (bloqueio de login/CAPTCHA).

## Resumo (5 linhas)

Foram coletados 23 artigos (10 do blog.tenp-kukan.com, 2 do cgbox.jp, 7 da série do blog.jukkagraph.net, 1 do note.com, 3 do renderbus.com), todos salvos como Markdown com frontmatter e seção "Resumo em portugues (tecnicas)", na pasta indicada. Por política de direitos autorais, o conteúdo foi salvo como extração técnica fiel e parafraseada (não cópia verbatim) — passos, nomes de nodes e parâmetros foram preservados fielmente. Um artigo do Zhihu (novo sistema de curvas de cabelo) ficou bloqueado por login/CAPTCHA e não foi coletado; a Parte 2 do tutorial do avestruz no Renderbus não foi localizada. Um case do Renderbus sobre gata realista foi descartado por usar Maya/XGen em vez de Blender. Detalhes completos de status estão na tabela acima.
