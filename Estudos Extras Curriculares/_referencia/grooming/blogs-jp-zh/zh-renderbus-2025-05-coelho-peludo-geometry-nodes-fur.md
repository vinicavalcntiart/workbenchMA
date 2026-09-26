---
titulo: 案例：用Blender做一个毛茸茸穿衣服的兔子
autor: Isaac Huerta (artista CG mexicano, 22 anos)
url: https://www.renderbus.com/share/post-id-1842/
data: 2025-05-08
idioma: zh
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do artigo. O conteúdo abaixo é uma extração técnica fiel, obtida via ferramenta de leitura automática e reorganizada por mim. Observação: este case usa o sistema de fur baseado em Geometry Nodes combinado com partículas, não o fluxo clássico de "hair curves manual" dos outros artigos deste acervo — incluído por se encaixar no critério "几何节点毛发" (pelo via Geometry Nodes) pedido na coleta.

## Notas técnicas (extração fiel do conteúdo original)

Case de um coelho peludo vestido, feito em Blender, com foco em pelo molhado/seco controlado por peso.

### Técnica de pelo
Usa o **sistema de fur em Geometry Nodes** combinado com sistema de partículas: "结合了粒子系统和地理节点毛皮系统" (combina sistema de partículas e sistema de pelo em Geometry Nodes).

### Processo
- Weight painting como mecanismo de controle: o sistema de partículas de água funciona como "pincel", e o modelo do coelho como "tela" (水的粒子系统是画笔，兔子模型是画布).
- Grupos de vértices gerados controlam propriedades das partículas de pelo: agrupamento (clustering), torção (twisting) e rugosidade (roughness).
- Efeito de pelo molhado implementado via máscaras pintadas por peso (weight paint).

### Configuração de material
- Mapas de "molhado" (wet maps) pré-calculados (bake), aplicados como máscara no material do pelo
- Transições suaves entre estados de pelo seco e molhado
- Pequenas gotas de líquido adicionadas usando modificador de instância de partícula

### Simulação adicional
Instanciamento de partículas para gotas de água na superfície do pelo molhado.

## Resumo em portugues (tecnicas)

Case de um **coelho peludo vestido**, com foco no efeito de pelo seco vs. molhado controlado por peso.

**Sistema de pelo:** combina **sistema de partículas** com **fur em Geometry Nodes** (não é o fluxo manual clássico de "hair curves" dos outros artigos deste acervo, mas se enquadra no pedido de "几何节点毛发" / pelo via Geometry Nodes).

**Ideia central do processo:** usar um sistema de partículas de água como "pincel" e o modelo do coelho como "tela" — ou seja, grupos de vértices (vertex groups) gerados a partir dessa simulação controlam propriedades do pelo (agrupamento/clump, torção, rugosidade).

**Material:** mapas de "molhado" pré-calculados (bake) usados como máscara no shader do pelo, permitindo transição suave entre pelo seco e molhado; gotas de líquido adicionadas via modificador de instância de partículas.

**Resultado:** efeito de pelo realista reagindo à água, sem usar diretamente o fluxo de "Hair Curves esculpidas à mão" — o controle vem de simulação + weight paint + Geometry Nodes.
