---
titulo: 【Blender 4.1】いろんな髪の作り方・表現方法を紹介！ (apenas a parte de cabelo realista/Geometry Nodes)
autor: CGbox編集部
url: https://cgbox.jp/2024/05/24/blender-various-hair/
data: 2024-05-24
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: coletada apenas a parte do artigo relativa a cabelo realista / Geometry Nodes, conforme solicitado (as seções de hair cards estilo anime/outras técnicas foram ignoradas). Por política de direitos autorais, não foi feita cópia literal do texto do blog; o conteúdo abaixo é uma extração técnica fiel, reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

### 1. Hair Particle (ヘアーパーティクル)
Usa o sistema de partículas para gerar muitos fios a partir da superfície de um objeto; serve para cabelo humano, pelo de animal e grama.

**Passos básicos:**
- Selecionar objeto → Particle Properties → adicionar novo slot de partícula
- Selecionar tipo "Hair" → configurar quantidade de cabelo e ajustes

**Ajustes disponíveis:** densidade do pelo (毛の密度), comprimento (長さ) e grau de curvatura (曲がり具合), via painel Particle Properties.

### 2. Geometry Nodes Hair (ジオメトリノードヘアー)
Disponível desde o Blender 3.3+. Mais leve em performance que o Hair Particle; editável via Geometry Nodes.

**Passos básicos:**
- Selecionar objeto → Shift+A → Curves → "Empty Hair" (空のヘアー)
- Alternar para Hair Sculpt Mode (Ctrl+Tab) → pintar com pincel para adicionar fios

**Edição:** adicionar Hair Nodes em Geometry Nodes para ajustar densidade, espessura (太さ) e curvatura.

### 3. Converter para malha (メッシュに変換する)
Processo: converter partículas/nodes de cabelo em malha para reduzir peso de dados, melhorar renderização e compatibilidade com animação.
Passos: preparar textura de cabelo → converter hair nodes em malha → gerar UV → aplicar textura.
Fluxo relacionado: é possível fazer bake do Geometry Nodes Hair usando métodos de baking para resultados otimizados.

## Resumo em portugues (tecnicas)

Trecho do artigo (as demais seções, sobre hair cards estilo anime, foram deixadas de fora por não serem o foco pedido) sobre as duas formas "clássicas" de fazer cabelo realista no Blender:

**1) Hair Particle (sistema de partículas):** selecionar o objeto → Particle Properties → novo slot de partícula → tipo "Hair" → ajustar quantidade. Parâmetros ajustáveis: densidade do pelo, comprimento e curvatura.

**2) Geometry Nodes Hair (Hair Curves, desde o Blender 3.3+):** mais leve que partículas e editável via Geometry Nodes. Passos: selecionar objeto → `Shift+A → Curves → Empty Hair` → entrar em Hair Sculpt Mode (`Ctrl+Tab`) → pintar fios com pincel. Depois, adicionar Hair Nodes no modificador Geometry Nodes para ajustar densidade, espessura e curvatura.

**3) Converter para malha:** transforma partículas ou hair nodes numa malha comum — reduz o peso de dados, melhora a renderização e a compatibilidade com animação. Fluxo: preparar a textura do cabelo → converter os hair nodes em malha → gerar UV → aplicar a textura. O artigo também menciona a possibilidade de fazer bake do Geometry Nodes Hair para otimização.
