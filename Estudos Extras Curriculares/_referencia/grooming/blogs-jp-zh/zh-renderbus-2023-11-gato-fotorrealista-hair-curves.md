---
titulo: Blender毛发测试！创建一只逼真写实的帝王猫！
autor: Andrii Karpylenko (artista de personagens CG, Ucrânia)
url: https://www.renderbus.com/share/post-id-1688/
data: 2023-11-13
idioma: zh
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do artigo. O conteúdo abaixo é uma extração técnica fiel, obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Breakdown de produção de um gato fotorrealista ("Emperor Cat"), publicado no site Renderbus (瑞云渲染).

### Stack de software
Blender (modelagem principal, grooming, texturização, renderização); ZBrush (escultura, criação de alphas); Marvelous Designer (simulação de roupa/tecido); Substance 3D Painter (textura de armadura/tecido).

### Sistema de cabelo/pelo usado
Hair Curves do Blender (新的毛发曲线系统 — "novo sistema de curvas de cabelo").

### Etapas de grooming citadas
1. Guias de referência consultadas e seguidas cuidadosamente.
2. Modificador de interpolação (Interpolate) aplicado, com ajuste manual.
3. Tufos/mechas adicionados via modificador de "clump" (团块修改器).
4. Modificador de ruído (noise) integrado separadamente da interpolação.
5. Máscaras de cor de vértice pintadas para controlar áreas de redução do efeito.
6. Parâmetros das curvas-guia ajustados iterativamente.

### Setup de nodes (团块和噪音的主要节点 — nodes principais de clump e ruído na cabeça)
- Máscaras procedurais implementadas
- Pintura de cor de vértice no couro cabeludo
- Pintura baseada nas próprias hair curves
- Controle de raio via hair curves

### Refinamento de colisão/grooming
- Modificador de colisão criado para a geometria da cabeça, para evitar interseção do pelo
- Remoção de pelo em áreas de cicatriz via modificador de colisão
- Objetos de colisão da cauda criados para minimizar interseção com o tecido/chão após aplicação do ruído

### Técnicas adicionais
- A penteação da cauda seguiu os mesmos princípios usados na cabeça/patas
- Pintura de textura de cor diretamente no Blender, usando janelas de viewport dedicadas (canais de visualização separados para corpo/couro cabeludo)

### Modelagem e preparação de assets
- Esboço e modelagem base feitos no Blender
- Simulação de tecido feita no Marvelous Designer, depois exportada para o Blender
- Topologia, UV unwrap e refinamento de espessura aplicados após a importação
- Detalhes de armadura: modelados e esculpidos no Blender para criar mapas de profundidade (alpha), usados posteriormente no ZBrush

### Renderização e composição
- Render farm: Renderbus瑞云渲染
- Iluminação: esquema clássico de três pontos (key, fill, edge lights), com luzes acompanhando o movimento de câmera durante o turnaround
- Composição no Blender: glow, vinheta e denoise aplicados no pós-processamento

## Resumo em portugues (tecnicas)

Breakdown de produção de um **gato fotorrealista** feito por Andrii Karpylenko, publicado no Renderbus.

**Software usado:** Blender (modelagem, grooming, textura, render), ZBrush (escultura/alphas), Marvelous Designer (roupa), Substance 3D Painter (textura de armadura/tecido).

**Sistema de pelo:** **Hair Curves** do Blender (o sistema novo de curvas de cabelo, baseado em Geometry Nodes).

**Fluxo de grooming:**
1. Seguir referências visuais cuidadosamente para posicionar as guias.
2. Aplicar `Interpolate Hair Curves` com ajuste manual fino.
3. Adicionar tufos/mechas via modificador de **clump** (agrupamento).
4. Aplicar **ruído** (noise) como modificador separado da interpolação.
5. Pintar **máscaras de cor de vértice** para reduzir o efeito em áreas específicas.
6. Ajustar parâmetros das curvas-guia de forma iterativa (tentativa e erro visual).

**Setup de nodes:** máscaras procedurais + pintura de cor de vértice no couro cabeludo + pintura direto nas hair curves + controle de raio via as próprias curvas.

**Colisão:** modificador de colisão na cabeça para evitar que o pelo atravesse a geometria; usado também para "remover" pelo em cicatrizes; objetos de colisão específicos na cauda para reduzir interseção com roupa/chão depois de aplicar ruído.

**Cauda:** penteada com os mesmos princípios usados na cabeça e nas patas.

**Textura de cor:** pintada diretamente no Blender, com janelas de viewport dedicadas para visualizar corpo e couro cabeludo separadamente.

**Pipeline geral:** modelagem base no Blender → roupa simulada no Marvelous Designer e importada de volta → retopologia/UV/espessura no Blender → detalhes de armadura esculpidos no Blender e levados ao ZBrush para gerar alphas → texturização de armadura/tecido no Substance 3D Painter.

**Render e composição:** renderizado na render farm da Renderbus; iluminação de três pontos (key/fill/edge) acompanhando a câmera no turnaround; composição final no Blender com glow, vinheta e denoise.
