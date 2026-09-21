# Grooming realista com Hair Curves + Geometry Nodes no Blender

Levantamento fechado em 21/09/2026. Versão de referência: **Blender 5.2.2 LTS**
(lançada em 15/09/2026). A outra LTS viva é a 4.5, atualizada para 4.5.14 na
mesma data. Fonte: https://www.blender.org/download/lts/

> Nota sobre a versão: o pedido original trazia `[SUA VERSÃO]` em branco. O
> documento foi montado em cima da 5.2 LTS, que é a atual, e marca
> explicitamente o que muda para quem está em 4.5 LTS.

---

## 1. Resumo

O material do Blender Studio continua parado em 2023 e não há substituto único.
As duas aulas de hair do Simon Thommes seguem rotuladas como 3.5 dentro do curso
Geometry Nodes from Scratch, que ganhou extras para 3.6, 4.0, 4.2 e 4.3, nenhum
deles sobre cabelo. A URL `/training/procedural-hair-nodes/` nem existe.
A boa notícia é que a biblioteca de nodes mudou muito menos do que parece: o
manual da 5.2 lista os mesmos 26 node groups em seis categorias que já existiam
na 3.5, e as release notes oficiais nunca citam a Essentials pelo nome entre
3.5 e 5.2. O que envelheceu no material do Studio não foram os nodes, foi o
entorno: shading (modelo Huang na 4.0), pipeline (USD e Alembic na 4.2) e
simulação (física XPBD na 5.2).
O melhor material atual não está em curso, está em palestra, post de dev e
documentação de addon. As três palestras da Blender Conference (Bystedt 2023,
Matsumoto 2024, Tönne 2025) valem mais que qualquer tutorial de YouTube achado.
O conteúdo escrito mais completo e atualizado do mundo sobre a Essentials é um
blog japonês, em Blender 4.5, node a node. Em português e espanhol não existe
nada: nem um curso, nem uma série.
Comece pela palestra do Bystedt, siga para o blog japonês como dicionário, faça
o capítulo 22 do curso da CGBoost para ver o fluxo dentro de um personagem
inteiro, e só então vá para a física da 5.2, que ainda é experimental por
rótulo oficial.

---

## 2. Tabela principal

Nota 1 a 5 de relevância para o objetivo: **grooming realista com hair curves +
Geometry Nodes, em versão atual**.

### 2.1 Palestras, posts de dev e documentação (o núcleo)

| Título | Autor | Tipo | Plataforma | Link | Blender | Preço | Idioma | Duração | O que cobre | Nota |
|---|---|---|---|---|---|---|---|---|---|---|
| Character grooming with the new hair system | Daniel Bystedt | palestra | Blender Conference 2023 | https://conference.blender.org/2023/presentations/1861/ · vídeo https://video.blender.org/videos/watch/2982655c-be93-4e5b-9bc5-267808e35d84 | n/d (out/2023, era 3.6/4.0) | gratuito | inglês | 50 min | Penteado de personagem no sistema novo, lado técnico e artístico, com foco declarado em realismo. Autor com histórico de groom em The Walking Dead e Cyberpunk 2077 | **5** — coautor dos hair nodes falando de realismo, não de features |
| Hair Simulation: From Cosmos Laundromat to Geometry Nodes | Lukas Tönne | palestra | Blender Conference 2025 | https://conference.blender.org/2025/presentations/4074/ · vídeo https://www.youtube.com/watch?v=sfUDDKSx-1c · re-record https://conference.blender.org/2025/presentations/4123/ | contexto 5.x | gratuito | inglês | 50 min + re-record de 20 min | Histórico da simulação de cabelo de 2015 até a integração em Geometry Nodes. É o pano de fundo do Hair Dynamics que saiu na 5.2 | **5** — único lugar que explica por que a física da 5.2 é assim |
| Mesh Hair with Geometry Nodes and Hair Curves | Sara Matsumoto | palestra | Blender Conference 2024 | https://conference.blender.org/2024/presentations/1990/ · vídeo https://www.youtube.com/watch?v=vXBL-oiqY7Q | n/d (out/2024, era 4.2/4.3) | gratuito | inglês | 50 min | Parte de hair curves realistas e gera mesh hair editável por Geometry Nodes, mantendo o groom re-editável | **5** — cobre a ponte curves para mesh sem abandonar o groom |
| Geometry Nodes Physics | Jacques Lucke | post de dev | code.blender.org | https://code.blender.org/2026/07/geometry-nodes-physics/ | 5.2 LTS | gratuito | inglês | artigo | Anúncio técnico da física da 5.2: XPBD Solver, Hair Dynamics, Cloth Dynamics, os três Effectors, Capture Rest Geometry, e o roadmap seguinte | **5** — fonte primária do sistema de física |
| Experimental Physics Feedback for Blender 5.2 LTS | thread aberta por Jacques Lucke | thread técnica | devtalk.blender.org | https://devtalk.blender.org/t/experimental-physics-feedback-for-blender-5-2-lts/45449 | 5.2 LTS | gratuito | inglês | thread longa | Feedback real de artistas: attach 2x mais lento que Surface Deform, clipping explosivo em collider, falta de collision offset, escala da superfície propagando errado, jitter na geração por frame | **5** — a lista honesta do que quebra antes de você adotar |
| Geometry Nodes Workshop: October 2024 | Jacques Lucke | post de dev | code.blender.org | https://code.blender.org/2024/11/geometry-nodes-workshop-october-2024/ | pré-5.2 | gratuito | inglês | artigo | Escolha do XPBD como solver e o problema aberto de guide hair mapping, que torna qualquer fluxo baseado em guides pouco confiável na simulação | **5** — nomeia uma limitação de design que afeta groom real |
| Procedural Hair Nodes: Nodegroup Assets for Blender 3.5 | Simon Thommes e comunidade | thread técnica | devtalk.blender.org | https://devtalk.blender.org/t/procedural-hair-nodes-nodegroup-assets-for-blender-3-5/27601 | 3.5 | gratuito | inglês | 4 páginas | Origem dos node groups da Essentials com as críticas de workflow da época: modifier stack poluído, máscaras escondidas no node editor, guides proceduralmente instáveis demais para VFX | **5** — as queixas de 2023 ainda descrevem o sistema de hoje |
| Hair Dynamics (manual) | equipe de doc do Blender | documentação | docs.blender.org | https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/simulation/hair_dynamics.html | 5.2 LTS | gratuito | inglês | página | Modos Animation e Physics, com Mass, Friction, Stretchiness, Bendiness, Root Bendiness, Structure Randomness, Substeps, Constraint Iterations, Time Scale. Traz o aviso oficial de feature experimental | **5** — parâmetros documentados em nenhum outro lugar |
| XPBD Solver (manual) | equipe de doc do Blender | documentação | docs.blender.org | https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/simulation/xpbd_solver.html | 5.2 LTS | gratuito | inglês | página | O solver por baixo de Hair Dynamics e Cloth Dynamics, alimentado por Typed Bundles na entrada World. Node complexo, feito para viver dentro de assets mais amigáveis | **5** — obrigatório para quem quiser sair do node group pronto |
| Hair Nodes (índice do manual) | equipe de doc do Blender | documentação | docs.blender.org | https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/hair/index.html | 5.2 LTS | gratuito | inglês | página | Os 26 node groups atuais em seis categorias: Deformation, Generation, Guides, Read, Utility, Write | **4** — o inventário canônico do que existe hoje |
| Create Guide Index Map (manual) | equipe de doc do Blender | documentação | docs.blender.org | https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/hair/guides/create_guide_index_map.html | 5.2 LTS | gratuito | inglês | página | Gera o atributo `guide_curve_index` mapeando cada curva ao guide mais próximo, consumido por Clump e Braid | **4** — a chave do clump em múltiplos níveis |
| 2025-06-26 Storm Hair Pipeline | Dalai Felinto e Simon Thommes | nota de reunião | devtalk.blender.org | https://devtalk.blender.org/t/2025-06-26-storm-hair-pipeline/41221 | n/d | gratuito | inglês | nota | Requisitos de hair do Project Storm: hair solver como node group, interpolação de tangente, correção de UV smoothing, e o fluxo ideal Bones → Guiding Hair → Children Hair | **4** — o que um estúdio pede ao sistema, por dentro |
| Projects to Look Forward to in 2026 | Dalai Felinto | roadmap | blender.org | https://www.blender.org/development/projects-to-look-forward-to-in-2026/ | ciclo 5.x | gratuito | inglês | artigo | Hair dynamics como destaque do ano e o objetivo declarado de aposentar o sistema de partículas, com a ressalva de que ainda há um longo caminho | **4** — calibra expectativa de prazo |
| Geometry Nodes Workshop: July 2025 | Jacques Lucke | post de dev | code.blender.org | https://code.blender.org/2025/07/geometry-nodes-workshop-july-2025/ | pré-5.2 | gratuito | inglês | artigo | Design declarativo do sistema de hair, e a distinção entre um sistema usável em produção e um workflow bom para qualquer usuário | **4** — explica por que a 5.2 saiu "meio pronta" |
| The Future of Hair Grooming | Dalai Felinto | post de dev | code.blender.org | https://code.blender.org/2022/07/the-future-of-hair-grooming/ | visando 3.3 LTS | gratuito | inglês | artigo | Anúncio do objeto Curves, os brushes de sculpt e a meta de 120 mil strands editáveis. Ressalva: 2022, valor histórico | **3** — contexto de origem, não workflow |

### 2.2 Cursos, séries e tutoriais

| Título | Autor | Tipo | Plataforma | Link | Blender | Preço | Idioma | Duração | O que cobre | Nota |
|---|---|---|---|---|---|---|---|---|---|---|
| Master 3D Characters in Blender (cap. 22) | Jim Morren | curso | CGBoost Academy | https://www.cgboost.com/courses/master-3d-characters-in-blender | n/d na página; curso em atualização contínua, última em ago/2026 | USD 99 + impostos | inglês | cap. de hair: 15 vídeos, ~3h46 | Usa hair curves primeiro num suéter peludo, depois em sobrancelhas, cílios e no penteado completo, montando setups de Geometry Nodes reutilizáveis com otimização | **5** — único curso pago confirmado com hair curves + GN dentro de um personagem realista |
| 【Blender】ヘアーカーブガイド (Guia de Hair Curves: de cabelo e pelo até hair cards) | 管理人 (blog 点P空間) | série / guia | blog.tenp-kukan.com | https://blog.tenp-kukan.com/7027/ | 4.5 | gratuito | japonês | artigo longo | Guia completo: escultura de guias, edição, nodes para cabelo humano, fur animal e conversão para hair cards, com Principled Hair BSDF | **5** — o material escrito mais completo e atual que existe sobre a Essentials |
| 【Blender4.5】Hair Curvesのよく使うジオメトリノード解説 (Nodes de GN mais usados em Hair Curves) | 管理人 (blog 点P空間) | post técnico | blog.tenp-kukan.com | https://blog.tenp-kukan.com/6019/ | 4.5 | gratuito | japonês | artigo médio/longo | Interpolate, Hair Curves Noise, Frizz, Set Hair Curve Profile, Clump, Trim, Roll, Curl e Braid, node a node, com ordem recomendada de uso e exemplos (afro, ondulado, trança) | **5** — é o dicionário da Essentials que o Blender Studio nunca escreveu |
| 写实毛发 (coleção "Cabelo Realista", 28 episódios) | 王也道长OS | série | Bilibili | coleção https://space.bilibili.com/317042327/channel/collectiondetail?sid=1280450 · ep. 15 https://www.bilibili.com/video/BV1zA4m1A7FE/ · ep. 16 https://www.bilibili.com/video/BV1wK421v7qw/ | 3.5 (ressalva de versão) | gratuito | chinês | ep. 15: 8m51s · ep. 16: 14m46s | Coleção inteira dedicada a cabelo realista por Geometry Nodes: guias, cabelo masculino, cabelo longo feminino, pelo de animal, barba, rabo de cavalo | **5** — a série mais extensa e focada em realismo que existe; nomes de nodes podem divergir na 5.2 |
| 【Blender4.5】Hair Curvesの使い方を解説 (Como usar Hair Curves) | 管理人 (blog 点P空間) | post técnico | blog.tenp-kukan.com | https://blog.tenp-kukan.com/5032/ | 4.5 | gratuito | japonês | artigo médio | Base do sistema: escultura, edit mode, GN para densidade, com um exercício de cabelo curto repartido ao meio | **4** — porta de entrada atualizada |
| [Blender 4.4] リアルな髪の毛チャレンジ④ (Desafio de cabelo realista, parte 4) | JUKKA | série (devlog) | blog.jukkagraph.net | https://blog.jukkagraph.net/archives/6952 | 4.4 | gratuito | japonês | post de série | Processo real: partir de esfera UV, separar mechas frente e trás, alinhar curvas, converter para Hair Curves, ajustar overlay no edit mode e escala do personagem | **4** — devlog honesto, com os tropeços à mostra |
| 【Blender 4.1】ジオメトリノードヘアーの使い方 (Como usar cabelo por Geometry Nodes) | CGbox編集部 | post técnico | cgbox.jp | https://cgbox.jp/2024/04/21/blender-geometory-node-hair/ | 4.1 | gratuito | japonês | artigo médio | Duplicate Hair Curves, Set Hair Curve Profile, Frizz, sculpt mode, exibição em Cycles e EEVEE, material com Curve Info, conversão para malha e simulação por cloth + GN | **4** — panorama técnico com foco declarado em realismo |
| Blender毛发测试！创建一只逼真写实的帝王猫！ (Criando um gato fotorrealista) | Andrii Karpylenko (republicado) | breakdown | Renderbus | https://www.renderbus.com/share/post-id-1688/ | n/d (art. de 2023, provável 3.5/3.6) | gratuito | chinês | artigo com imagens | Fur de criatura fotorrealista: Interpolate, raio de fio, Clump, Noise, máscaras procedurais, vertex color painting e collision, em pipeline com ZBrush e Substance | **4** — um dos poucos breakdowns de fur realista com processo visível |
| NEW Hair Dynamics in Blender 5.2 | KennyPhases | vídeo avulso | YouTube | https://www.youtube.com/watch?v=PWxxqKk4zsg | 5.2 (no título) | gratuito | inglês | n/d | Cabelo procedural e ativação da física pelo node Hair Dynamics | **4** — aparentemente o primeiro tutorial de terceiros sobre a física da 5.2; metadados não confirmados |
| Directing Fur/Hairs with Curves using Geometry Nodes | 3DSinghVFX | tutorial com arquivo | BlenderNation | https://www.blendernation.com/2023/06/05/directing-fur-hairs-with-curves-using-geometry-nodes-tutorial/ | 3.5x | gratuito | inglês | n/d | Uso de guide curves para direcionar fur, com arquivo de projeto gratuito linkado | **3** — direcionamento de fur por guides; versão antiga |
| Blender 3.5 New Hair Tools and Assets | stache | vídeo avulso | YouTube | https://www.youtube.com/watch?v=i5EanKOhb9c | 3.5 | gratuito | inglês | n/d | Apresenta Generate, Interpolate, Trim, Hair Curves Noise e Frizz, e o Asset Browser com as 26 entradas de hair em seis categorias | **3** — mapa útil da biblioteca, que mudou pouco desde então |
| [Tut] New Hair Curves - Blender 5.0 Geometry Nodes Beginner | Bradley Animation | vídeo avulso | YouTube | https://www.youtube.com/watch?v=FMWw6XEcY4Y | 5.0 (no título) | gratuito | inglês | n/d | Introdução ao sistema em 5.0 | **3** — dos poucos já rotulados para 5.x |
| Get into Geometry Node Hair Fast | Martin Klekner | vídeo avulso | YouTube | https://www.youtube.com/watch?v=bIsJquzVsPY | n/d (mar/2024) | gratuito | inglês | n/d | Fluxo rápido de criação com GN hair | **3** — visão geral prática |
| Hair Grooming in Blender ft. New Hair System (Hair Curves) | adiidiin | vídeo avulso | YouTube | https://www.youtube.com/watch?v=pQcYoH4H1MM | n/d (maio/2025) | gratuito | inglês | n/d | Cabelo, sobrancelhas e cílios no sistema novo | **3** — cobre sobrancelha e cílio, que quase ninguém cobre |
| Simulate hair with Geometry Nodes Hair System | munorr | vídeo avulso | YouTube | https://www.youtube.com/watch?v=q4uzLyjjxFU | n/d | gratuito | inglês | n/d | Simulação de cabelo pelo sistema GN, provavelmente anterior ao Hair Dynamics nativo | **3** — útil para comparar com a abordagem da 5.2 |
| Tiger Fur Groom - Blender 4.3 | canal Polycount | breakdown | YouTube | https://www.youtube.com/watch?v=UbIukaLwGxo | 4.3 (no título) | gratuito | inglês | n/d | Groom de pelo de tigre em 4.3 | **3** — fur de criatura em versão recente; não confirmei os nodes usados |
| 笨蛋流几何节点毛发（三）常用修改器介绍 (GN Hair parte 3: modificadores comuns) | 安扣王UncleWang | série (5 eps) | Bilibili | https://www.bilibili.com/video/BV1UNquBhEjw/ | n/d | gratuito | chinês | 8m06s | Os modificadores e nodes mais usados no fluxo de grooming | **3** — o conteúdo mais recente da praça chinesa (jan/2026) |
| Create Realistic Hair in Blender with Geometry Nodes! | Nino (NinoDefoq) | vídeo avulso | YouTube | https://www.youtube.com/watch?v=87ICxDHi9bc | n/d (jan/2023) | gratuito | inglês | n/d | Cabelo com foco em realismo por Geometry Nodes | **3** — de 2023, anterior à Essentials madura |
| blender毛发 (coleção, 65 episódios) | 宇庭_特效师 | série | Bilibili | coleção https://space.bilibili.com/433276269/channel/collectiondetail?sid=2967568 · ep. 1 https://www.bilibili.com/video/BV1Pu4m1c7FY/ · ep. 21 https://www.bilibili.com/video/BV1Yh4y1B7ZZ/ | 4.1 (ep. 1) | gratuito | chinês | ep. 21: 14m08s | Bake de dinâmica de cabelo por GN, uso dos node groups nativos, conversão para FBX e OBJ | **3** — mistura realista com anime, exige curadoria episódio a episódio |
| ヘアデザインメモ (Construindo uma ferramenta de GN para design de cabelo) | へあでざいん(仮) | devlog | note.com | https://note.com/hair_drawings/n/neb3a7c4dff61 | n/d (refs à 3.6) | gratuito | japonês | post | Ferramenta autoral em GN para cabelo de comprimento único, unindo hair curves, dynamics e booleanas | **3** — relato de construção de node group próprio |
| 【Blender 4.1】いろんな髪の作り方 (Vários métodos de criar cabelo) | CGbox編集部 | post técnico | cgbox.jp | https://cgbox.jp/2024/05/24/blender-various-hair/ | 4.1 | gratuito | japonês | artigo longo | Metade é comparação realista (partícula legada vs GN hair, conversão para malha); a outra metade é estilizado e deve ser ignorada | **3** — ler só a seção de GN hair |
| blender 几何节点毛发曲线制作头发 (Cabelo com hair curves por GN) | ANSHITE | vídeo avulso | Bilibili | https://www.bilibili.com/video/BV1pUxpefESD/ | n/d | gratuito | chinês | n/d | Criação de cabelo com Hair Curves e GN | **3** — tema certo, detalhes não confirmados |
| Blender黑科技！用几何节点把任意网格变头发 (Transformando qualquer malha em cabelo) | 老CG了 (técnica atribuída a Xeofrios) | vídeo avulso | Bilibili | https://www.bilibili.com/video/BV1UQK7zAEsL/ | n/d | gratuito | chinês | n/d | Converter geometria de malha em fios de cabelo por GN | **3** — técnica não trivial, verificação parcial |
| 블렌더3D (4.x) - 헤어 커브 (Blender 3D 4.x — Hair Curves) | canal 블렌더3D | vídeo avulso | YouTube | https://www.youtube.com/watch?v=W0-YUAd5pkg | 4.x (no título) | gratuito | coreano | n/d | Plantio de curvas, combing, duplicação e materiais de cabelo | **3** — único achado coreano; não confirmei uso da Essentials |
| How to Make Procedural Fur in Blender 3.5 | Simon Thommes | aula de curso | Blender Studio | https://studio.blender.org/training/geometry-nodes-from-scratch/how-to-make-procedural-fur-in-blender-35/ | 3.5 | gratuito | inglês | vídeo ~1,3 GB | Fur 100% procedural com GN, com arquivo de demonstração CC-BY | **3** — é o baseline a superar; entra só porque fur de criatura é pouco coberto |
| How to Make Procedural Fur in Blender Geometry Nodes | Blender Studio | vídeo | YouTube | https://www.youtube.com/watch?v=gCQN5vNgHiI | 3.5 | gratuito | inglês | n/d | Versão em vídeo da aula acima | **3** — mesma ressalva |
| Are You Using Blender's Hair Assets? | SouthernShotty | vídeo avulso | YouTube | https://www.youtube.com/watch?v=gyb4MCDiQQY | n/d | gratuito | inglês | n/d | Provável introdução ao Asset Browser de hair nodes | **2** — conteúdo não confirmado |
| Creating a REALISTIC Hair Shader in Blender! | Aneesh Arts | vídeo avulso | YouTube | https://www.youtube.com/watch?v=M2e3hIfbu44 | n/d | gratuito | inglês | n/d | Shading de cabelo, provavelmente Principled Hair BSDF | **2** — não confirmei se a origem é hair curves ou hair cards |
| The EASIEST Hair Grooming Method With Blender's Geometry Node System | Kenny Praise | vídeo avulso | YouTube | https://www.youtube.com/watch?v=G_iPk5SrEHc | n/d | gratuito | inglês | n/d | Método de grooming por GN | **2** — sem confirmação de foco em realismo |
| Introduction to Hair Grooming in Blender | Luwizart | vídeo avulso | YouTube | https://www.youtube.com/watch?v=s9NDZ5q3SaE | n/d | gratuito | inglês | n/d | Introdução ao grooming | **2** — nível iniciante, sem confirmação |
| How to Convert Curves to Hair in Blender | Danny Mac 3D | vídeo avulso | YouTube | https://www.youtube.com/watch?v=7-y1HuyLeTs | n/d (jan/2025) | gratuito | inglês | n/d | Converter curvas comuns em objeto Hair Curves | **2** — passo de workflow isolado |
| HAIR for AAA GAMES #129 · Blender.Today LIVE | canal Blender | live | YouTube | https://www.youtube.com/watch?v=oqjKMd9CYI4 | n/d | gratuito | inglês | n/d | Pipeline de cabelo para jogos AAA | **2** — viés de games, pode divergir do realismo de render |
| Procedural Eyelashes/Eyebrows with Geometry Nodes in Blender 3.3 | thetony20 | thread técnica | Blender Artists | https://blenderartists.org/t/procedural-eyelashes-eyebrows-with-geometry-nodes-in-blender-3-3/1405907 | 3.3 | gratuito | inglês | thread | Guides de cílio e sobrancelha ajustados por parâmetros de GN, e o problema de manter curvatura ao encurtar | **2** — de 2022, controle paramétrico mais que realismo |
| HAIR SYSTEM 3.5 - NOVO SISTEMA DE CABELOS NO BLENDER | LucViana | vídeo avulso | YouTube | https://www.youtube.com/watch?v=ddh86sFJ9qE | 3.5 (no título) | gratuito | português | n/d | Introdução ao sistema novo sobre um busto realista | **2** — único vídeo em português sobre o sistema novo em base realista |
| Hair Nodes (manual traduzido) | Blender Foundation | documentação | docs.blender.org | https://docs.blender.org/manual/pt/latest/modeling/geometry_nodes/hair/index.html | 5.2 LTS | gratuito | português | página | Referência traduzida de todos os node groups de hair | **3** — dicionário em português, não ensina workflow |
| Nodos de pelo (manual traduzido) | Blender Foundation | documentação | docs.blender.org | https://docs.blender.org/manual/es/latest/modeling/geometry_nodes/hair/index.html | 5.2 LTS | gratuito | espanhol | página | Mesma referência em espanhol | **3** — mesma ressalva |

### 2.3 Addons e packs de nodes

| Título | Autor | Tipo | Plataforma | Link | Blender | Preço | Idioma | Tamanho | O que cobre | Nota |
|---|---|---|---|---|---|---|---|---|---|---|
| Facial Hair Toolkit v2.2.5 | learnasimakeit | addon + assets | Gumroad | https://learnasimakeit.gumroad.com/l/trwVm | até 5.2 LTS (changelog explícito) | USD 49 | inglês | n/a | Sobrancelha, barba e cílios distribuídos como hair curves na superfície, com GN para gerar hair cards e bake de textura, e guia de export para Unreal 5 | **5** — cobre exatamente os pelos faciais pedidos, e está em dia com a 5.2 |
| GroomFlow Pro (guidebook) | Chamiseul Studio Ci / mayalhc | addon | doc oficial: https://mayalhc.github.io/GroomFlow_Pro/ (venda em Superhive e ArtStation) | https://mayalhc.github.io/GroomFlow_Pro/ | 5.2+ (changelog v1.8.1) | preço não confirmado | inglês e coreano | n/a | Hair Curve Layers, máscaras de textura, forma de fio, thickness e noise, stack de style nodes, dinâmica com colisão, children em tempo real, clumping, braid, export para Unreal, e um capítulo sobre por que a sim explode em rig de escala MetaHuman | **5** — documentação viva, atualizada para 5.2, e endereça problemas reais |
| StrandKit · The Hair, Fur & Dynamics Library | Nino (ninodefoq) | pack de node groups | Gumroad | https://ninodefoq.gumroad.com/l/strandkit | n/d na página | USD 54,53 | inglês | n/a | 24 sistemas de tipo de cabelo (1A liso a 4C crespo), 15 de pelagem animal, conversão para hair card e física com vento, colisão e gravidade. Declarado como setups GN limpos | **4** — cobertura de tipo de cabelo e fur que nenhum outro pack tem; 5 avaliações só |
| Hair Tool 4 | Bartosz Styperek | addon | Gumroad | https://bartoszstyperek.gumroad.com/l/hairtool | 4.6.1 para 5.2 · 4.5.9 para 4.5–5.1 · 4.3.0 para 4.2+ · 3.x para 3.6–4.1 | USD 52 | inglês | n/a | Gera hair cards a partir de um sistema procedural em GN e de guide mesh, com bake de normal, AO, diffuse, tangent, ID, root e flow, UVs, ossos com jiggle e 30+ presets. Desde a 3.x abandonou particle hair e curvas antigas, roda sobre o objeto Hair Curves | **4** — maduro, usado em estúdio, mas o alvo é hair card, não fio fotorrealista |
| Groom Exporter | turbocheke | addon | Gumroad | https://turbocheke.gumroad.com/l/Groomexporter | fóruns citam 4.1+ | gratuito (0,00 nos metadados) | inglês | n/a | Exporta objetos Curves como Alembic no schema Groom que a Unreal espera, com ajuste de coordenada e escala e suporte a múltiplos objetos como grupos | **4** — resolve o buraco entre o Alembic nativo e o Groom da Unreal |
| Braidify (Procedural Braid Generator) | Nino (DefoQ) | pack de nodes | Gumroad | https://ninodefoq.gumroad.com/l/braidify | 3.5 mínimo | gratuito | inglês | n/a | Gera tranças a partir de curvas desenhadas no viewport, com controle de espessura e frequência, em saída de geometria ou de strands | **4** — a saída em strands serve a realismo, não só a estilizado |
| Blender geometry nodes — Hair cards from curves | Daniel Bystedt | pack de nodes | Gumroad | https://3dbystedt.gumroad.com/l/hairCardsFromCurves | 3.6+ | gratuito | inglês | n/a | Recebe hair curves, cards e a superfície da cabeça, deforma os cards ao longo das curvas e alinha o twist à superfície | **4** — melhor referência gratuita de engenharia reversa para curves → cards |
| Hair Tool 3 (divulgação JP) | Bproduction / Bartosz Styperek | addon | CGinterest | https://cginterest.com/2023/08/01/blender-%E3%81%AE%E6%96%B0%E3%81%97%E3%81%84%E3%83%98%E3%82%A2%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%82%92%E3%83%95%E3%83%AB%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%81%97%E3%81%9F%E3%83%98%E3%82%A2/ | 3.6–4.1 | pago, valor n/d | japonês | n/a | Cobertura em japonês do Hair Tool com suporte ao sistema novo, para trança, cacho e cílio | **3** — redundante com a ficha do Hair Tool acima |
| Medusa Nodes (Beta) | Irakli Kupunia | addon | Gumroad | https://ikakupa.gumroad.com/l/XEzSy | 4.2 (v1.1.5) | USD 17,22 | inglês | n/a | Node groups espelhando a Essentials (Guide, Clump, Noise, Curl, Braid, Children, Trim) mais mask groups, mapas de região e parting, e solver Verlet próprio com freezing para performance | **3** — conceito alinhado, mas o autor avisa que está parado e não está pronto para produção |
| BGEN Hair Systems (BGEN Groom e BGEN Flow) | MUNORR | packs de nodes | Gumroad (divulgação em 3dnchu.com) | https://3dnchu.com/archives/bgen-hair-systems/ | 3.5+ | CAD 5 cada | inglês (artigo em japonês) | n/a | Groom organiza o fluxo em GN sem exigir conhecimento de nodes; Flow converte malha em fios e simula | **3** — a resenha classifica o resultado como procedural, não fotorrealista |
| Hair Modeller | Blender Easy | addon | divulgação em cgbox.jp | https://cgbox.jp/2025/01/27/news-addon-hair-modeller/ | n/d | USD 15 | inglês (artigo em japonês) | n/a | Adiciona cabelo e pelo por escultura sobre o sistema nativo, com densidade, raio, agrupamento e ondulação | **3** — não confirmei se o núcleo é GN ou só sculpt |
| Procedural Human Hair for Blender | TAU (creamtau) | asset pack | itch.io | https://creamtau.itch.io/procedural-human-hair | 3.x, v1.5 (nov/2023) adicionou 4.0 | pague quanto quiser | inglês | .blend de 97 MB | 5 presets de sobrancelha, 5 de cílio, 1 de vellus e 5 de pelo pubiano, com shader Huang. **Ressalva importante: o próprio autor diz "geometry nodes only (no hair curves)"**, então não parte do objeto Curves | **3** — cobre vellus e cílio, mas foge do escopo do objeto Curves |
| Geometry Nodes Hair Generator | xeofrios | pack de nodes | Gumroad | https://xeofrios.gumroad.com/l/gnhair | 3.4+ | gratuito | inglês | n/a | Gera guias a partir de curves ou de mesh | **2** — básico e provavelmente defasado frente aos nodes nativos |
| Grease Pencil to Curves | DadsCastle | addon | Blender Extensions | https://extensions.blender.org/add-ons/gp-to-curves/ | 4.3+ | gratuito | inglês | n/a | Suaviza traços de Grease Pencil e converte em hair curve já anexada à superfície. Não usa Geometry Nodes | **2** — atalho de entrada de guias, não é sistema de grooming |

### 2.4 Pipeline, export e simulação

| Título | Autor | Tipo | Plataforma | Link | Blender | Preço | Idioma | Tamanho | O que cobre | Nota |
|---|---|---|---|---|---|---|---|---|---|---|
| Release notes 4.2 · Pipeline & I/O | Blender | documentação | developer.blender.org | https://developer.blender.org/docs/release_notes/4.2/pipeline_assets_io/ | 4.2 LTS | gratuito | inglês | página | O marco do pipeline: "The hair curves object type is now supported for both import and export" em **USD e Alembic**. O importador Alembic também ganhou import multi-arquivo e correção de curvas animadas que não atualizavam no render | **5** — a data em que hair curves viraram formato de troca |
| USD (manual) e limitações atuais | Blender | documentação | docs.blender.org | https://docs.blender.org/manual/en/latest/files/import_export/usd.html | 5.2 LTS | gratuito | inglês | página | Strands pai exportados como sistema de curvas e `UsdGeomBasisCurves` importados como objeto Curves. Limitações confirmadas: cor de fio não exporta, atributos de UV/st não são incluídos, e há bug aberto de material se desconectando na importação | **5** — leia antes de prometer USD num pipeline |
| Release notes 5.2 · Physics | Blender | documentação | developer.blender.org | https://developer.blender.org/docs/release_notes/5.2/physics/ | 5.2 LTS | gratuito | inglês | página | Hair Dynamics exige mesh de superfície e o modificador Capture Rest Geometry, que guarda a geometria em bundles para rastrear a deformação do rest ao deformado. O operador Empty Hair foi atualizado para automatizar o setup | **5** — a checagem de pré-requisito antes de simular |
| Integrating Blender Hair into Unreal Engine Groom System | Linh Nguyen (iRender) | post técnico | irendering.net | https://irendering.net/integrating-blender-hair-into-unreal-engine-groom-system/ | n/d no texto; cita UE 4.26 e UE5 | gratuito | inglês | artigo | Passo a passo com funcionalidade nativa: desabilitar child hairs e dynamics antes do export, transforms corretos no scalp e nas curvas, export Alembic com dados de curva, import por plugin Groom, binding a skeletal mesh e física do lado da Unreal | **4** — recente (jan/2026) e prático |
| Rig and simulate Hair Curves on Blender 3.3 | SSBB210 | thread técnica | Blender Artists | https://blenderartists.org/t/rig-and-simulate-hair-curves-on-blender-3-3/1407111 | 3.3 (notas até 3.5.1) | gratuito | inglês | thread | O workaround clássico pré-5.2: proxy mesh gerado das hair curves, Cloth no proxy com vertex groups pintados e Surface Deform devolvendo o movimento às curvas, usando nodes do filme Heist | **5** — ainda é o plano B quando o XPBD explode |
| Blender 5.3a · GroomFlow & New Hair Simulation Geometry Nodes Test | ChamIseul_ZEPETO | thread técnica | Blender Artists | https://blenderartists.org/t/blender-5-3a-groomflow-new-hair-simulation-geometry-nodes-test/1645689 | 5.3a | gratuito | inglês | thread + vídeo | Teste real com 50 guides e 100 strands atacando o descolamento de raiz, resolvido pela correção automática do GroomFlow | **5** — teste do sistema nativo em uso, com problema e solução |
| How to render alembic curves/hairs from Houdini with this hack | pullpullson e SamuliPahaoja | thread técnica | devtalk.blender.org | https://devtalk.blender.org/t/how-to-render-alembic-curves-hairs-from-houdini-with-this-hack/24945 | 3.3 alpha | gratuito | inglês | thread | Roundtrip Houdini: converter curvas em polígonos com o nó `ends`, importar como mesh cache Alembic e reconverter no Blender com Mesh to Curve e Set Spline Cyclic | **4** — de 2022; o suporte nativo da 4.2 pode dispensar parte do hack |

### 2.5 Conteúdo em russo

A praça russa quase não tem tutorial autoral no sistema novo. O que tem de bom
é cobertura jornalística de release, pelo portal render.ru. O resto ainda é
particle hair.

| Título | Autor | Tipo | Plataforma | Link | Blender | Preço | Idioma | Tamanho | O que cobre | Nota |
|---|---|---|---|---|---|---|---|---|---|---|
| Blender 5.2 LTS: simulação de tecido e cabelo com Geometry Nodes | Man5ON | notícia técnica | render.ru | https://render.ru/ru/news/post/28294 | 5.2 LTS | gratuito | russo | artigo curto | Cobertura do sistema experimental de física de hair e cloth sobre XPBD, comparando com o Vellum do Houdini e a Unreal, e apontando o que falta: vento pronto e colisão complexa | **4** — release note explicada em russo, sobre a versão atual |
| Hair Cards from Curves (notícia sobre o addon) | Man5ON, sobre addon de Daniel Bystedt | notícia | render.ru | https://render.ru/ru/news/post/25242 | 3.6+ | gratuito | russo | n/d | Cobertura do addon que converte hair curves em hair cards deformados pela curva com alinhamento à superfície | **3** — porta de entrada em russo para a ferramenta |
| Blender em 2026: principais atualizações e planos | redação render.ru | roadmap | render.ru | https://render.ru/ru/news/post/27779 | 5.1, 5.2, 5.3 | gratuito | russo | n/d | Cobertura do roadmap oficial, citando o sistema dinâmico de cabelo em GN e a meta de paridade com o solver de partículas | **3** — contexto, não tutorial |
| Волосы в Blender: как сделать косу с помощью плагина Braidify | não indicado (adaptação de artigo da 3D World) | tutorial escrito | NewArtSchool | https://newartschool.ru/tutorials/volosy-v-blender-plagin-braidify | n/d | gratuito | russo | artigo curto | Trança gerada a partir de uma curva-guia "hair empty" mais modificador de Geometry Nodes, com alternância entre modo realista e anime e controle de densidade e ruído | **3** — confirma curves + GN e tem modo realista, mas é caso único e sem autor/data/versão |
| How to convert hair card to curves: Blender Geometry Nodes | Stanisgrox | post pago | Boosty | https://boosty.to/stanisgrox/posts/73ee13b4-14b2-4c02-b0ba-6526396528f8 | n/d (paywall) | assinatura ~USD 5,10/mês | russo | n/d | Pelo preview: converte hair cards em hair curves por GN, o caminho inverso do addon do Bystedt. Corpo do post atrás do paywall | **2** — não deu para confirmar realismo nem versão |

---

## 3. Os dez melhores, em ordem de estudo

A ordem é deliberada: contexto artístico primeiro, referência de nodes em
seguida, fluxo completo depois, e física por último, porque ela é o que menos
estabilizou.

1. **Character grooming with the new hair system**, Daniel Bystedt, BCON 2023.
   https://conference.blender.org/2023/presentations/1861/
   Começa aqui porque é a única fonte que trata o sistema como ferramenta de
   groom, não como catálogo de nodes. O autor vem de groom AAA e fala de
   decisão artística, que é o que você já sabe fazer em XGen e precisa remapear.
2. **Hair Nodes no manual 5.2**, para fixar o inventário atual.
   https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/hair/index.html
   Vinte e seis node groups em seis categorias. Dez minutos, e evita você
   procurar node que não existe porque o tutorial era de 3.5.
3. **【Blender4.5】Hair Curvesのよく使うジオメトリノード解説**, blog 点P空間.
   https://blog.tenp-kukan.com/6019/
   O dicionário node a node com ordem recomendada de encadeamento. Em japonês,
   mas é tabela e imagem, passa bem no tradutor. Substitui de fato a parte de
   referência do material do Blender Studio.
4. **Procedural Hair Nodes: Nodegroup Assets for Blender 3.5**, thread do devtalk.
   https://devtalk.blender.org/t/procedural-hair-nodes-nodegroup-assets-for-blender-3-5/27601
   Leia depois do dicionário, não antes. É onde os limites do sistema aparecem
   sem marketing: guides proceduralmente instáveis, máscaras escondidas,
   modifier stack poluído.
5. **Master 3D Characters in Blender, capítulo 22**, Jim Morren, CGBoost.
   https://www.cgboost.com/courses/master-3d-characters-in-blender
   Quase quatro horas vendo hair curves dentro de um personagem inteiro, com
   sobrancelha, cílio e penteado no mesmo pipeline. É o único curso pago
   confirmado no sistema novo. USD 99.
6. **写实毛发**, coleção de 28 episódios de 王也道长OS no Bilibili.
   https://space.bilibili.com/317042327/channel/collectiondetail?sid=1280450
   Volume bruto de exemplos realistas: masculino, feminino longo, barba, rabo
   de cavalo, pelo animal. É 3.5, então trate como referência de intenção e
   traduza os nomes de node para os atuais.
7. **Mesh Hair with Geometry Nodes and Hair Curves**, Sara Matsumoto, BCON 2024.
   https://conference.blender.org/2024/presentations/1990/
   Entra aqui porque a essa altura você já tem groom e precisa decidir o que
   fazer com ele fora do Cycles.
8. **Release notes 4.2, Pipeline & I/O**, mais a página de USD do manual.
   https://developer.blender.org/docs/release_notes/4.2/pipeline_assets_io/
   Quinze minutos que definem o que você pode prometer num pipeline: Alembic e
   USD aceitam hair curves desde a 4.2, com buracos conhecidos em UV e material.
9. **Hair Simulation: From Cosmos Laundromat to Geometry Nodes**, Lukas Tönne,
   BCON 2025. https://conference.blender.org/2025/presentations/4074/
   O porquê da física da 5.2, contado por quem escreveu o solver antigo e o novo.
10. **Geometry Nodes Physics**, Jacques Lucke, mais a thread de feedback da 5.2.
    https://code.blender.org/2026/07/geometry-nodes-physics/ e
    https://devtalk.blender.org/t/experimental-physics-feedback-for-blender-5-2-lts/45449
    Último porque é o menos assentado. Leia o post para o modelo mental e a
    thread para saber o que vai quebrar antes de você descobrir sozinho.

---

## 4. Assets e arquivos .blend para engenharia reversa

### Oficiais do blender.org

| Arquivo | Autor | Link | Versão | Licença | Nota |
|---|---|---|---|---|---|
| hair_nodes-female_hair_styles.blend | Daniel Bystedt | https://www.blender.org/download/demo/geometry-nodes/hair_nodes-female_hair_styles.blend | 3.3 LTS ou mais recente | CC-BY-SA | Variações de penteado feminino com guias, interpolação e clumping. É o arquivo por trás do material 3.5, então é a base a superar, mas continua sendo a estrutura de node group mais limpa para abrir e dissecar |
| hair_nodes-animal_fur_examples.blend | Simon Thommes | https://www.blender.org/download/demo/geometry-nodes/hair_nodes-animal_fur_examples.blend | 3.3 LTS ou mais recente | CC0 | Fur animal com direção, frizz e densidade. CC0, então você pode canibalizar à vontade |

Página de origem: https://www.blender.org/download/demo-files/

### Blender Studio

| Arquivo | Link | Versão | Acesso | Nota |
|---|---|---|---|---|
| Charge — Einar, hair grooming file | https://studio.blender.org/projects/charge/gallery/?asset=6072 | n/d na página; o projeto lista shot files em 3.5 | provavelmente exige assinatura, não confirmado | O achado mais valioso desta seção: groom de barba de um personagem de produção real, versão simplificada do progresso do grooming do filme |
| Charge — Curve Stitching Tool | https://studio.blender.org/projects/charge/?asset=6189 | n/d | aparentemente sem paywall | Mapeia a posição de um objeto curva no espaço UV de uma superfície. Não é hair, mas é o mesmo paradigma e vale ler o node tree |

### Gratuitos de terceiros

| Arquivo / pack | Autor | Link | Versão | Por que abrir |
|---|---|---|---|---|
| Hair cards from curves | Daniel Bystedt | https://3dbystedt.gumroad.com/l/hairCardsFromCurves | 3.6+ | O melhor node tree gratuito para estudar deformação de card ao longo de curva com alinhamento de twist à superfície |
| Braidify | Nino (DefoQ) | https://ninodefoq.gumroad.com/l/braidify | 3.5 mínimo | Trança procedural com saída em strands. Bom para entender construção de braid antes de usar o Braid Hair Curves nativo |
| Groom Exporter | turbocheke | https://turbocheke.gumroad.com/l/Groomexporter | 4.1+ segundo fóruns | Gratuito e é o código a ler se você quiser entender o schema Groom da Unreal |
| Directing Fur/Hairs with Curves | 3DSinghVFX | https://www.blendernation.com/2023/06/05/directing-fur-hairs-with-curves-using-geometry-nodes-tutorial/ | 3.5x | Arquivo de projeto gratuito linkado na descrição do vídeo |
| Procedural Human Hair | TAU | https://creamtau.itch.io/procedural-human-hair | 3.x e 4.0 | .blend de 97 MB com sobrancelha, cílio, vellus e pelo pubiano em shader Huang. Ressalva: por declaração do autor não usa hair curves, só GN |

### Nota de método para engenharia reversa

Os demo files oficiais são todos da era 3.5. Isso, na prática, não é tão ruim
quanto soa, porque a Essentials mudou pouco. O que você precisa ter em mente ao
abrir um arquivo de 3.5 na 5.2 é que a release note da 5.1 registra que a
hierarquia de catálogos da Essentials não pode mais ser editada, e a da 5.2
avisa que arquivos de asset com Geometry Nodes tools precisam ser re-salvos
para funcionar direito. Fontes:
https://developer.blender.org/docs/release_notes/5.1/assets/ e
https://developer.blender.org/docs/release_notes/5.2/

---

## 5. Artistas e devs para acompanhar

### Os dois que mais importam para você

**Daniel Bystedt** — artista, Goodbye Kansas. Coautor dos hair nodes procedurais
originais junto com Simon Thommes. Assina a palestra BCON 2023 sobre groom
realista, o demo file oficial de penteados femininos e o setup gratuito Hair
Cards from Curves (mar/2024, Blender 3.6+). É o nome mais próximo de um par
seu no ecossistema: groom de produção AAA, mas dentro do Blender.
Publica em https://3dbystedt.gumroad.com e no YouTube como morriscowboy.

**Lukas Tönne** — dev do módulo Nodes & Physics. Escreveu o solver de hair
dynamics antigo e o novo. Palestra BCON 2025 e as atas regulares de reunião do
módulo no devtalk, que documentam o desenvolvimento mês a mês.
https://devtalk.blender.org/u/LukasTonne

### Devs do core

**Simon Thommes** — autor do material 3.5 que você quer superar e dos node
groups da Essentials. Continua ativo e é a pista mais quente do documento: em
12/09/2025 ele abriu a thread "Geometry Nodes Assets Blender 5.0" no devtalk
anunciando novos node groups nativos (PR #145645), sequência direta do trabalho
de 2023. https://devtalk.blender.org/t/geometry-nodes-assets-blender-5-0/42334 ·
https://www.simon-thommes.com · https://devtalk.blender.org/u/SimonThommes

**Jacques Lucke** — líder técnico de Geometry Nodes. Escreve os workshops em
code.blender.org e abriu a thread de feedback da física experimental. Tudo que
vai mudar nos hair nodes passa por ele primeiro. https://jlucke.com ·
https://github.com/JacquesLucke · https://devtalk.blender.org/u/jacqueslucke

**Hans Goudey** — mexe na estrutura de dados Curves por baixo do capô. O que
ele discute no devtalk costuma aparecer nos hair nodes algumas versões depois.
https://projects.blender.org/HooglyBoogly ·
https://devtalk.blender.org/u/HooglyBoogly

**Dalai Felinto** — direção do projeto. Assina os posts de visão, incluindo
Projects to Look Forward to in 2026, onde hair dynamics é destaque e o objetivo
declarado é aposentar o sistema de partículas.
https://devtalk.blender.org/u/dfelinto
**Atenção:** o domínio dalaifelinto.com não é mais dele, foi tomado por um site
de apostas. Não abra.

**Falk David** — foi central na arquitetura do objeto Curves, mas hoje lidera
Grease Pencil. Fonte secundária, útil para entender a fundação, não para groom.
https://devtalk.blender.org/u/filedescriptor

### Artistas e autores de ferramenta

**Sara Matsumoto** (SM5 by Heledahn, Japão) — palestra BCON 2024 sobre converter
hair curves realistas em mesh hair editável mantendo o groom re-editável.
https://sm5.heledahn.com

**Bartosz Styperek** (joseconseco) — Hair Tool, o addon de hair mais maduro do
ecossistema, 995 avaliações e nota 4,9, acompanhando as versões até a 5.2.
https://bartoszstyperek.gumroad.com/l/hairtool

**Nino / ninodefoq** — StrandKit e Braidify, e um dos primeiros vídeos de
"realistic hair with geometry nodes". https://ninodefoq.gumroad.com

**Chamiseul Studio Ci / mayalhc** — GroomFlow Pro, com a documentação de addon
mais bem mantida que encontrei, já em 5.2+, incluindo um capítulo sobre por que
a simulação explode em rig de escala MetaHuman.
https://mayalhc.github.io/GroomFlow_Pro/

**learnasimakeit** — Facial Hair Toolkit, mantido até 5.2 LTS, focado
exatamente em sobrancelha, barba e cílio. https://learnasimakeit.gumroad.com/l/trwVm

**Autor do blog 点P空間** (anônimo, japonês, https://blog.tenp-kukan.com/) —
escreveu entre set e nov de 2025 a melhor referência escrita da Essentials que
existe hoje, em Blender 4.5.

**王也道长OS** (Bilibili, https://space.bilibili.com/317042327) — 28 episódios
dedicados a cabelo realista por Geometry Nodes.

### Ressalva de cobertura

Esta seção está mais fraca do lado dos artistas independentes do que do lado dos
devs. ArtStation, Reddit e X bloquearam acesso automatizado o tempo todo, então
a varredura de gente que publica groom realista sem ser dev ou autor de addon
ficou incompleta. Um nome que sobrou como pista sem confirmação: **Danil
Gryzlov** (YouTube @dgryzlovart, Boosty boosty.to/dgryzlovart), generalista
russo com pelo menos três vídeos cujo título promete cabelo realista, mas não
deu para confirmar se usa o sistema novo.

---

## 6. Mudanças nos hair nodes, da 3.5 à 5.2

A conclusão mais útil desta seção vem antes da tabela: **as release notes
oficiais nunca citam a biblioteca Essentials pelo nome entre 3.5 e 5.2**. Ela é
um pacote de assets embarcado, não uma feature de código, e por isso não tem
entrada própria. Na prática isso significa que os node groups em si mudaram
pouco, e que a história real do sistema está nos posts de dev e nas threads do
devtalk, não nas release notes.

| Versão | Data | Mudança | Fonte |
|---|---|---|---|
| 3.5 | 29/03/2023 | Node **Interpolate Curves** nativo, que gera curvas filhas entre um conjunto de guides. **Trim Curves** ganha input de seleção | https://developer.blender.org/docs/release_notes/3.5/nodes_physics/ |
| 3.5 | 29/03/2023 | A Essentials passa a embarcar os ~26 assets de hair nas categorias Deformation, Generation, Guides, Utility, Read e Write. Não documentado nas release notes; a fonte é o post do Blender Studio e a thread do devtalk | https://studio.blender.org/blog/procedural-hair-nodes/ · https://devtalk.blender.org/t/procedural-hair-nodes-nodegroup-assets-for-blender-3-5/27601 |
| 3.6 LTS | 27/06/2023 | Nada específico de hair. Cycles registra um bug conhecido de sombra em cabelo no HIP RT experimental em GPU AMD | https://developer.blender.org/docs/release_notes/3.6/cycles/ |
| 4.0 | 14/11/2023 | **Modelo Huang no Principled Hair BSDF**, ao lado do Chiang. Suporta seção transversal elíptica, que é o que cabelo humano real tem, orientação alinhável por normais da curva via geometry nodes, e modelo far-field. Pode ficar mais lento em roughness baixo e parecer achatado em close | https://developer.blender.org/docs/release_notes/4.0/cycles/ |
| 4.1 | 26/03/2024 | Nada de hair em geometry nodes, sculpt, cycles ou pipeline | https://developer.blender.org/docs/release_notes/4.1/nodes_physics/ |
| 4.2 LTS | 16/07/2024 | **O objeto hair curves passa a ser suportado em import e export, tanto em USD quanto em Alembic.** O importador Alembic ganha import multi-arquivo e corrige curvas animadas que não atualizavam no render | https://developer.blender.org/docs/release_notes/4.2/pipeline_assets_io/ |
| 4.2 LTS | 16/07/2024 | **Huang passa a alternar dinamicamente entre near-field e far-field** conforme a distância de câmera, melhorando close-up | https://developer.blender.org/docs/release_notes/4.2/cycles/ |
| 4.3 | 19/11/2024 | Nada de hair | https://developer.blender.org/docs/release_notes/4.3/geometry_nodes/ |
| 4.4 | 18/03/2025 | Nada de hair. O instancing de USD passa a cobrir outros tipos de geometria além de mesh, incluindo curves, mas é mudança genérica | https://developer.blender.org/docs/release_notes/4.4/pipeline_assets_io/ |
| 4.5 LTS | 15/07/2025 | Nada de hair | https://developer.blender.org/docs/release_notes/4.5/geometry_nodes/ |
| 5.0 | 18/11/2025 | Nada de hair. Chegam Bundles e Closures, que são a infraestrutura que a física da 5.2 vai usar | https://developer.blender.org/docs/release_notes/5.0/geometry_nodes/ |
| 5.1 | 17/03/2026 | Nada de hair. Nota administrativa relevante: **a hierarquia de catálogos da Essentials não pode mais ser editada** | https://developer.blender.org/docs/release_notes/5.1/assets/ |
| 5.2 LTS | 14/07/2026 | **Sistema de física experimental baseado em Geometry Nodes, com foco inicial em hair e cloth**, sobre o framework XPBD | https://developer.blender.org/docs/release_notes/5.2/physics/ |
| 5.2 LTS | 14/07/2026 | Node group e modificador **Hair Dynamics**, com modos Animation e Physics. Exige mesh de superfície e o novo modificador **Capture Rest Geometry**, que guarda a geometria em bundles para rastrear a deformação do rest ao deformado. O operador **Empty Hair** foi atualizado para montar isso sozinho | https://developer.blender.org/docs/release_notes/5.2/physics/ |
| 5.2 LTS | 14/07/2026 | Parâmetros do Hair Dynamics: Mass, Friction, Stretchiness, Bendiness, Root Bendiness, Structure Randomness, Substeps, Constraint Iterations, Time Scale, damping linear e angular, e colisão de superfície. Stretchiness 1 deixa o fio crescer até dez vezes o comprimento de repouso sob a própria gravidade | https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/simulation/hair_dynamics.html |
| 5.2 LTS | 14/07/2026 | **Effectors** em três tipos: Collider (qualquer mesh fechada), Custom Force (vetor de força por ponto) e Custom Effector (injeta comportamento por closure em estágios da simulação). Organizáveis por Effector Collection ou Effector Bundle, com filtro por tag | https://developer.blender.org/docs/release_notes/5.2/physics/ |
| 5.2 LTS | 14/07/2026 | **XPBD Solver** como node interno. Dá para adaptar os node groups prontos ou construir um sistema novo direto sobre ele, o que exige bundles e atributos tipados | https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/simulation/xpbd_solver.html |
| 5.2 LTS | 14/07/2026 | **Online Essentials**: a biblioteca passa a incluir assets hospedados online, visíveis quando "Allow Internet Access" está ligado nas preferências | https://developer.blender.org/docs/release_notes/5.2/assets/ |
| 5.3 alpha | em curso | Nada de hair até agora nas páginas de geometry nodes e physics. A de physics está vazia no momento da consulta | https://developer.blender.org/docs/release_notes/5.3/geometry_nodes/ |

### Uma pista em aberto na 5.0

Em 12/09/2025 Simon Thommes abriu no devtalk a thread "Geometry Nodes Assets
Blender 5.0", anunciando novos node groups nativos por meio da PR #145645.
https://devtalk.blender.org/t/geometry-nodes-assets-blender-5-0/42334
As release notes da 5.0 não mencionam nada disso, o que é coerente com o padrão
descrito acima: assets embarcados não ganham entrada própria. Não consegui
confirmar se algum dos node groups novos é de hair, porque projects.blender.org
bloqueou o acesso à PR. Se alguma coisa mudou na Essentials entre 3.5 e 5.2,
é aqui que está. Vale abrir essa PR manualmente.

### Observação de caminho de URL

O padrão muda entre versões e derruba links diretos. A seção de geometry nodes é
`nodes_physics/` em 3.5 e 3.6 e vira `geometry_nodes/` a partir da 4.0.
Import e export é `import_export/` na 4.0, `pipeline_assets_io/` da 4.1 à 4.5, e
`pipeline_io/` a partir da 5.0. As versões 4.0, 4.1, 4.3, 4.4 e 5.1 não têm
página própria de physics. Índice geral:
https://developer.blender.org/docs/release_notes/

### O que isso significa para quem está em 4.5 LTS

Se você ficar na 4.5, você tem a biblioteca de hair nodes completa, o shader
Huang com near e far field dinâmicos, e export de hair curves em USD e Alembic.
O que você não tem é a física: Hair Dynamics, XPBD Solver, Effectors e Capture
Rest Geometry só existem da 5.2 em diante. Para simulação em 4.5 o caminho
continua sendo o proxy mesh com Cloth e Surface Deform descrito na thread do
Blender Artists listada na seção 2.4.

---

## 7. Lacunas

**Ninguém ensinou o sistema atual do começo ao fim.** Não existe hoje um
equivalente atualizado do material do Blender Studio. O que mais chega perto é
a série do blog japonês, que é referência de node e não fluxo completo de
personagem, e o capítulo 22 da CGBoost, que é fluxo completo mas dentro de um
curso de personagem inteiro e não um curso de groom.

**A física da 5.2 é praticamente inédita em conteúdo de terceiros.** Achei um
único tutorial de YouTube dedicado ao Hair Dynamics e uma thread de teste no
Blender Artists. Isso é esperado, saiu em julho de 2026, mas significa que hoje
a documentação oficial, o post do Jacques Lucke e a thread de feedback são
literalmente tudo que existe.

**Nada em português nem em espanhol.** Isso não é falha de busca: foram cerca
de trinta buscas cruzando YouTube, Udemy, Domestika, Hotmart, Gumroad, Patreon
e fóruns. O que existe em PT/ES sobre "cabelo com curvas" é quase todo de
2019–2021 e usa Bézier com bevel ou partículas. Quando alguém usa o sistema
novo, o resultado é estilizado. A única coisa de qualidade é o manual
traduzido, que é dicionário, não aula. **Isso é uma oportunidade de
posicionamento**, não só uma lacuna: você tem o repertório de XGen e Houdini e
poderia ser a primeira pessoa a publicar isso em português.

**Coreia é deserto.** Uma busca dedicada não achou nenhum curso, série ou
breakdown coreano de grooming realista no sistema novo. Coloso e Inflearn têm
Geometry Nodes genérico, sem cabelo.

**Nenhum workflow verificado de XGen para hair curves.** O caminho existe na
teoria, exportar do Maya em Alembic e importar como curves desde a 4.2, mas não
achei um único tutorial ou thread que documente isso funcionando de ponta a
ponta. Para alguém com o seu histórico, esse é provavelmente o conteúdo mais
valioso que ninguém escreveu.

**Guide mapping é um problema aberto reconhecido pelos devs.** O workshop de
outubro de 2024 diz com todas as letras que falta uma forma robusta de
armazenar o mapeamento de cabelo gerado para múltiplos guides, e que isso torna
qualquer workflow baseado em guides pouco confiável, especialmente em
simulação. Ninguém escreveu um tutorial sobre como conviver com isso.

**Clump em múltiplos níveis está subdocumentado.** O Create Guide Index Map é
a peça central e tem uma página de manual. Não achei um único tutorial dedicado
a empilhar clump em dois ou três níveis com guides diferentes, que é o feijão
com arroz de um groom realista.

**Shading de hair em Cycles quase não tem material recente.** O modelo Huang
chegou na 4.0 e ganhou near/far field dinâmico na 4.2, e o único vídeo de
shader realista que achei não deixa claro se parte de hair curves. A diferença
prática entre Chiang e Huang num groom real não está documentada em lugar
nenhum que eu tenha encontrado.

**Marketplaces são um ponto cego desta pesquisa.** Superhive, ArtStation, Udemy,
CG Cookie e FlippedNormals bloquearam acesso automatizado de forma sistemática.
Vários addons potencialmente relevantes ficaram sem verificação. Vale uma
passada manual com navegador logado.

**Cuidado com particle hair disfarçado.** Vários produtos vendem "hair" sem
dizer que operam no sistema de partículas antigo. Os confirmados nesta pesquisa:
Hair Net, que converte mesh e curves em particle hair, portanto na direção
oposta da que interessa; o Hair Extension Toolkit da VFX Grace; e os cursos de
hair da CG Cookie, cuja descrição cita particle hair system junto com curvas
Bézier. Antes de comprar qualquer coisa, procure a palavra "particle" na
descrição.

**O SEO do assunto está tomado.** O domínio yelzkizi.org aparece em quase toda
busca sobre hair curves e geometry nodes, com dezenas de páginas que descrevem
nodes sem ensinar workflow. Foi excluído de todos os itens. Vale saber que
buscar termos genéricos como "realistic hair blender tutorial" devolve quase só
isso.

---

## 8. Não verificado

Itens que não passaram na checagem. Nenhum deles foi usado nas seções acima.

### Bloqueio de acesso (HTTP 403)

| Item | Link | Motivo |
|---|---|---|
| Hair Lab | https://superhivemarket.com/products/hair-painter | Superhive bloqueia acesso automatizado. Busca indica 25+ nodes para sobrancelha, cílio, barba e trança desenhando duas curvas Bézier, Blender 4.2+, não confirmado |
| Hair Proxy | https://superhivemarket.com/products/hair-proxy | Mesmo bloqueio. Busca indica proxy em mesh para shape key e rig sobre hair curves |
| GroomFlow Pro (página de venda e preço) | https://superhivemarket.com/products/groomflow_pro · https://www.artstation.com/marketplace/p/Xoq5l/groomflow-pro | Bloqueio em ambas. A documentação oficial do produto foi verificada à parte; o preço não |
| GroomForge Blender Addon | https://www.artstation.com/marketplace/p/8LnbR/groomforge-blender-addon | Bloqueio. Busca cita USD 25, não confirmado |
| PRO HAIR, Instances on Hair, TubeHair Generator, RapidHair Cards | superhivemarket.com | Bloqueio sistemático no domínio |
| Blender 5 Hair & Fur: Complete Workflow | https://www.udemy.com/course/blender-hair-fur-/ | Bloqueio. Busca sugere que mistura particle hair com geometry nodes, o que precisaria de confirmação |
| CG Cookie — Styling and Shading Realistic Hair | https://cgcookie.com/courses/styling-and-shading-realistic-hair | Bloqueio. Busca indica ajuste de partícula e shader Cycles, ou seja, provavelmente sistema antigo |
| Free Hair Grooms (Blender Project) | https://www.artstation.com/marketplace/p/YDaKB/free-hair-grooms-blender-project | Bloqueio. Busca menciona "hair groom particle system" |
| Dealing with groom in Blender and Unreal Engine | https://www.artstation.com/blogs/eatmylazer/agpQq/dealing-with-groom-in-blender-and-unreal-engine | Bloqueio |
| ANOREK, Blender node hair | https://www.patreon.com/ANOREK | Bloqueio |
| How to use Node Hair (한국어ver), Hezeh | https://www.patreon.com/Hezeh/posts/how-to-use-node-121782084 | Bloqueio. Pelo perfil da autora, pode ser cabelo estilizado para jogo |
| How to Get Blender Hair Into Unreal Engine's Groom System (2026) | https://medium.com/@irenderofficial/how-to-get-blender-hair-into-unreal-engines-groom-system-without-losing-your-mind-2026-f2248ff49bd4 | Cloudflare. Substituído pelo artigo equivalente em irendering.net, esse sim verificado |
| projects.blender.org: task #103730 e PRs #154435, #158038, #159493 | https://projects.blender.org/blender/blender/issues/103730 | 403 persistente no domínio. Os títulos das PRs sugerem que a flag experimental do hair dynamics pode ter sido proposta para remoção; vale reconferir |
| PR #145645, novos Geometry Nodes assets na 5.0 | projects.blender.org | Mesmo bloqueio. É a pista mais importante desta lista: pode conter mudanças na Essentials que as release notes não registram |
| ArtStation, Reddit e X, varredura de artistas | artstation.com · reddit.com · x.com | Bloqueio sistemático (403 e 402). A busca por artistas independentes publicando groom realista ficou incompleta por isso |
| Danil Gryzlov, três vídeos sobre cabelo realista | https://www.youtube.com/watch?v=LS55C8lVjCQ · https://www.youtube.com/shorts/ywzk_Zre39U | Título e canal confirmados por oEmbed; o YouTube bloqueou descrição e data. Não dá para saber se é hair curves ou particle hair |
| Волосы на Geometry Nodes #51, canal Ниворд | https://www.youtube.com/watch?v=qRSVMXXXex0 | Confirmado que é hair em Geometry Nodes, mas é devlog de um jogo estilizado. Foco em realismo não confirmado |
| ffuthoni, Hair Curve Strands using Geometry Nodes | https://ffuthoni.gumroad.com/l/hcurvesgeonodes | A página só retornou o título |
| rakenval, Hair curves to Hair cards converter | https://rakenval.gumroad.com/l/yyufn | A página só retornou o título. Consta 3.6+ e GN, sem confirmação |

### Conteúdo não confirmado

| Item | Link | Motivo |
|---|---|---|
| Introducción al Hair Grooming con Blender, Irene Arnaiz | https://www.latecnocreativa.com/curso-online/introduccion-al-hair-grooming-con-blender-1747 | Curso pago de escola espanhola real, EUR 85, foco declarado em cabelo realista e export para Unreal. **A página não cita "Hair Curves", "Geometry Nodes" nem número de versão em lugar nenhum.** É igualmente compatível com particle hair. Precisa de confirmação humana antes de comprar |
| Dyna Groom, Carlos Eduardo Barreto | https://carlosedubarreto.gumroad.com/l/dyna_groom | A página só retornou o título. Não deu para confirmar preço, versão, nem se usa hair curves |
| StrandKit, versão do Blender | https://ninodefoq.gumroad.com/l/strandkit | Preço e nota confirmados; a página não declara versão mínima do Blender |
| Groom Exporter, versão exata | https://turbocheke.gumroad.com/l/Groomexporter | Preço zero e descrição técnica confirmados; a versão suportada vem de fórum, não da página |
| hair_comb.blend | https://download.blender.org/demo/hair_comb.blend | Não deu para confirmar se usa o objeto Curves ou o sistema de partículas. Pelo contexto, provavelmente partículas, o que o deixaria fora do escopo |
| Charge — Einar, se é gratuito ou exige assinatura | https://studio.blender.org/projects/charge/gallery/?asset=6072 | A página não mostrou selo de paywall, mas downloads do Blender Studio em geral exigem assinatura |
| Preço da assinatura do Blender Studio | studio.blender.org | O valor de EUR 11,50 por mês apareceu em busca e não foi confirmado na página oficial de preços |
| yelzkizi.org | https://yelzkizi.org/realistic-hair-new-hair-geometry-nodes-hair-curves/ | HTTP 403 ao tentar verificar autoria e originalidade. Excluído por ser SEO genérico, conforme o critério; registro aqui por transparência, já que domina os resultados de busca |
| UEとBlenderでリアルな毛を生やす, @tukigaselio | https://qiita.com/tukigaselio/items/85b3fa025884a122dc67 | Artigo de dez/2025 sobre interpolação, ruído e export Alembic para Unreal, mas não confirmei uso explícito de Geometry Nodes |
| 髪モデリングTIPS, パイパイパイ | https://zenn.dev/pipipi22/books/d35eb8d742e17f/viewer/b3a065 | Só o título do capítulo retornou. Não confirmei se é hair curves ou modelagem poligonal |
| Human Hair style braids gameready pbr | https://www.blenderkit.com/asset-gallery-detail/834c56e9-d1e1-4f43-9ce5-4bfaadc66293/ | Página carregou só menus em JS. Não confirmei se é hair curves ou mesh estático |
| Advanced realtime hair tutorial (FlippedNormals) | https://flippednormals.com/product/advanced-realtime-hair-tutorial-59491 | HTTP 404, link morto |
| Developing a Custom Hair Creation System With Blender's Geometry Nodes | https://80.lv/articles/developing-a-custom-hair-creation-system-with-blender-s-geometry-nodes | Página abre, mas é de fev/2023, anterior ao lançamento do hair curves na 3.5. Não dá para saber se o sistema descrito usa o objeto Curves |
| Projects to Look Forward to in 2025 | https://www.blender.org/development/projects-to-look-forward-to-2025/ | Não aberto diretamente, só por snippet de busca |

### Excluídos por estarem fora do escopo, não por falha de verificação

- **Hair Net** (https://extensions.blender.org/add-ons/hair-net/): a descrição
  oficial diz que converte mesh e curves em particle hair, ou seja, o inverso
  do que interessa.
- **Hair Extension Toolkit**, VFX Grace: confirmado no site do fabricante que
  opera sobre o sistema de partículas.
- **Tutorial BOYO**, Alex Treviño (AENDOM): usa o addon Medusa Nodes, que roda
  sobre Curves e GN, mas aplicado a um personagem-gato estilizado.
- **Cabelo no Blender 3.5**, Léo Maciel: sistema novo, personagem cartoon.
- **Cursos de Geometry Nodes em PT/ES** (B-Viz Academy, Blender en Español,
  Etérea/Cristóbal Vila, Zao3D): cobrem GN em geral, nenhum toca cabelo. Ficam
  registrados como ponte para quem quiser firmar a base de nodes de curva antes.
- **Создание реалистичных волос в Blender для рендера Cycles**, curso da Wingfox
  em russo (https://render.ru/ru/Wingfox/post/20745): verificado com sucesso, e
  é particle hair em Blender 2.82.7, de 2021.

---

## Nota de método

O levantamento foi feito em 21/09/2026 por sete varreduras em paralelo,
divididas por plataforma e por idioma: YouTube em inglês mais Blender Studio e
Blender Conference; marketplaces e plataformas de curso; documentação e release
notes; português e espanhol; japonês, chinês e coreano; russo mais artistas e
devs; arquivos, export e simulação. Cada item foi aberto antes de entrar.
Cerca de setenta itens passaram na verificação.

Três limitações honestas sobre a cobertura:

**Marketplaces.** Superhive, ArtStation, Udemy, CG Cookie e FlippedNormals
bloqueiam acesso automatizado. Quando o mesmo produto existia no Gumroad ou em
site do autor, usei essa cópia. Quando não existia, o item foi para a seção 8.

**YouTube.** A página de vídeo não abre para leitura automatizada. Título e
canal foram confirmados pelo endpoint oEmbed, que é confiável, mas duração,
data e descrição ficaram como n/d em vários itens. Por isso alguns vídeos têm
nota mais baixa do que talvez mereçam: é falta de confirmação, não julgamento
de qualidade.

**Busca.** O orçamento de buscas da sessão se esgotou perto do fim, o que
atingiu principalmente a varredura de artistas independentes e a praça russa.
São as duas frentes a retomar se você quiser esgotar o assunto.

Ao fechar o documento rodei uma checagem automática nos 152 links. Nenhum link
das seções 2 a 7 está morto. Os únicos que não respondem a acesso automatizado
são os já declarados na seção 8 como bloqueados, mais três perfis pessoais
(GitHub, ArtStation e projects.blender.org) que devolvem 403 a robô mas abrem
normalmente no navegador. O único 404 real é o tutorial da FlippedNormals,
registrado como link morto. As páginas do YouTube devolvem 429 em acesso
automatizado, o que é limite de taxa, não link quebrado.
