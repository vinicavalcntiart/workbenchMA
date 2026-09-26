---
titulo: 【Blender4.5】メッシュをヘアーカーブに変換する方法：Hair Curvesの応用
autor: 管理人 (blog 点P空間)
url: https://blog.tenp-kukan.com/6199/
data: 2025-09-28 (atualizado 2025-11-16)
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do blog. O conteúdo abaixo é uma extração técnica fiel (passos, parâmetros e erros comuns), obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Tutorial de técnica avançada: converter uma malha (mesh) modelada manualmente em Hair Curves.

### 1. Preparação da malha
- Começar de uma UV Sphere, apagar partes desnecessárias
- Criar área do couro cabeludo com vértices concentrados usando Inset Faces (tecla I)
- Usar modificador Subdivision Surface para aumentar densidade de arestas
- Modelar regiões de cabelo da frente e de trás separadamente

### 2. Extração de arestas
- Selecionar arestas verticais via Select > Select Loops > Edge Rings
- Estender seleção via Select > Select Loops > Edge Loops
- Duplicar (Shift+D) e separar via P > Selection

### 3. Conversão mesh → curva → hair curve
- Converter para Curve: clique direito > Convert To > Curve
- Ativar visibilidade de Normals nos overlays do modo Edit de curva
- Corrigir direção da curva para que as setas apontem para fora, usando "segments > Switch Direction"
- Converter para Curves: clique direito > Convert To > Curves
- Aplicar todas as transformações (Apply All Transform) para evitar problemas nos Geometry Nodes

### 4. Quatro configurações obrigatórias
① **Parent to Mesh:** Object Properties > Relations > Parent → selecionar a malha de superfície
② **Surface & UV Map:** Object Data Properties > Surface > Surface e UV Map → referenciar o objeto de malha
③ **Snap Roots:** em modo Sculpt: Curves > Snap to Nearest Surface
④ **Deform Modifier:** adicionar Geometry Nodes com o node "Deform Curves on Surface" ligando Group Input/Output

### 5. Setup de Geometry Nodes
Cadeia de nodes antes do Deform:
- Duplicate Hair Curves (Amount: 80, Radius: 0,01)
- Set Hair Curve Profile (Radius: 0,0003 m, Shape: 0,160)
- Attach Hair Curves to Surface (todas as caixas de seleção marcadas)
- Delete Geometry (remove curvas com falha de anexação, usando Hair Attachment Info + Not)

### Problemas comuns e soluções
- "Evaluated surface missing attribute: 'rest_position'" → resolvido adicionando/apagando temporariamente uma Empty Hair Curves via Shift+A
- "Invalid surface UVs on [#] curves" → o node Delete Geometry remove as curvas com anexação falha

## Resumo em portugues (tecnicas)

Tutorial avançado: **converter uma malha modelada à mão em Hair Curves** (para ter controle total sobre a forma de cada mecha).

**Preparo da malha:** partir de uma UV Sphere, remover o que não é necessário; criar a área do couro cabeludo com Inset Faces (I); aumentar densidade com Subdivision Surface; modelar frente e trás separadamente.

**Extração das arestas que viram fios:** `Select > Select Loops > Edge Rings`, depois `Edge Loops` para estender a seleção; duplicar (`Shift+D`) e separar (`P > Selection`).

**Conversão em cadeia:** malha → Curve (`clique direito > Convert To > Curve`) → conferir/corrigir direção das normais (setas devem apontar para fora, usar `Switch Direction`) → Curves (`Convert To > Curves`) → **aplicar todas as transformações** (Apply All Transform) para não quebrar os Geometry Nodes depois.

**4 configurações obrigatórias para a curva funcionar como cabelo:**
1. **Parent to Mesh** — em Object Properties > Relations > Parent, apontar para a malha de superfície.
2. **Surface & UV Map** — em Object Data Properties > Surface, apontar Surface e UV Map para o objeto de malha.
3. **Snap Roots** — em modo Sculpt: `Curves > Snap to Nearest Surface`.
4. **Deform Modifier** — Geometry Nodes com o node `Deform Curves on Surface` entre Group Input e Group Output.

**Pilha de Geometry Nodes usada (antes do Deform):**
- `Duplicate Hair Curves` (Amount 80, Radius 0,01)
- `Set Hair Curve Profile` (Radius 0,0003 m, Shape 0,160)
- `Attach Hair Curves to Surface` (todas as opções marcadas)
- `Delete Geometry` (remove curvas que falharam ao anexar, usando `Hair Attachment Info` + `Not` como máscara)

**Erros comuns e correção:**
- *"Evaluated surface missing attribute: 'rest_position'"* → resolvido adicionando e apagando temporariamente uma Empty Hair Curves (via Shift+A) para forçar o Blender a regenerar o atributo.
- *"Invalid surface UVs on [N] curves"* → o node `Delete Geometry` remove as curvas cuja anexação à superfície falhou.
