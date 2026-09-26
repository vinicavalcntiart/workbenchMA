---
titulo: 「Blender4.5」Hair Curvesの使い方を解説：Geometry Nodes-based Hair System
autor: 管理人 (blog 点P空間)
url: https://blog.tenp-kukan.com/5032/
data: 2025-09-24 (atualizado 2025-11-16)
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do blog. O conteúdo abaixo é uma extração técnica fiel (passos, parâmetros e valores), obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Tutorial prático de como usar Hair Curves do zero, usando como exemplo um penteado curto repartido no meio.

### Estrutura
1. Comparação Hair Particles vs Hair Curves
2. Explicação do objeto Curves
3. Fluxo de trabalho em 3 etapas principais
4. Tutorial detalhado do penteado curto repartido no meio, por regiões
5. Referência ao "Hair Curves Guide" (o artigo 7027)

### As 3 etapas principais
- Mesh → atribuição de Hair Curves
- Modo Sculpt/Edit para modelar o formato
- Ajustes via Geometry Nodes

### Configuração inicial
- Adicionar via: Shift+A > Curves > Empty Hair
- Opções: Empty Hair (parcial) ou Fur (cobertura total)
- Requer malha com UV mapeado e Subdivision Surface "UV Smooth" definido como "None"

### Configurações do modo Sculpt (formato da curva)
- Length: ajustável
- Points: padrão 8 (16 para cabelo longo)
- Interpolate: ativado para herdar atributos

### Ferramentas de pincel usadas
Add (plantar cabelo), Grow/Shrink (ajuste de comprimento), Comb (pentear), Selection Paint (seleção de curvas), Smooth (suavizar), Puff (levantar volume), Slide (reposicionar).

### Configurações de colisão
- Use Sculpt Collision: ativado
- Distância de colisão: faixa 0.001–0.005 m

### Nodes de Geometry Nodes aplicados (com valores de exemplo)
| Node | Parâmetro | Valor |
|---|---|---|
| Interpolate Hair Curves | Surface | malha da cabeça |
| | Surface Rest Position | marcado |
| | Distance to Guides | 0,01 m |
| | Density | 300.000 |
| Set Hair Curve Profile | Radius | 0,0003 m |
| Hair Curves Noise | Factor | 0,2 |
| | Distance | 0,02 m |
| | Scale | 300 |
| Clump Hair Curves | Shape | 0,220 |
| | Clump Offset | 0,015 m |
| | Distance Threshold | 0,005 m |

Ordem dos modificadores: Interpolate Hair Curves (topo) → Set Hair Curve Profile → outras modificações → Deform Curves on Surface (por último).

### Regiões do penteado (cores usadas na explicação)
1. Nuca (roxo)
2. Parte de trás da cabeça (azul)
3. Laterais/têmporas (azul-esverdeado)
4. Costeletas (verde-amarelado)
5. Topo/coroa (vermelho)
6. Franja (amarelo)

### Configuração de material
- Shader: Principled Hair BSDF
- Gradiente raiz-a-ponta usando o node Curve Info

### Opções de render no EEVEE
Curves > Shape: Strand (leve, iluminação básica) ou Strip (tipo fita/mesh, normais mais precisas). Subdivisão adicional disponível para mais detalhe.

### Criação da malha da franja/testa (para o repartido central)
Duplicar a malha da cabeça → modo Edit, selecionar a aresta central → Ctrl+B para inserir edge loop → apagar as faces centrais para separar. **Part by Mesh Islands** é ativado para impedir interpolação cruzando os limites da malha.

### Artigos relacionados citados
"Hair Curves Geometry Nodes Explicado" (o artigo 6019), "Guia de material Principled Hair BSDF" (5043), "Conversão de Mesh para Hair Curves" (6199), "Textura de sobrancelha com Hair Curves" (6844), "Método de criação de Hair Cards" (6878).

### Notas de fluxo de trabalho
Edição não destrutiva; múltiplas curvas por malha suportadas; seções diferentes usam objetos de curva separados; refinamento iterativo de trás para frente; recomenda-se checar vários ângulos durante a modelagem; recomenda-se refazer com múltiplas curvas por seção para aprender melhor.

## Resumo em portugues (tecnicas)

Tutorial prático de "como usar Hair Curves", usando um penteado curto repartido ao meio como exemplo guiado.

**As 3 etapas do fluxo:** 1) atribuir Hair Curves à malha (mesh); 2) modelar a forma em modo Sculpt/Edit; 3) ajustar com Geometry Nodes.

**Configuração inicial:** `Shift+A > Curves > Empty Hair` (opções "Empty Hair", parcial, ou "Fur", cobertura total). A malha precisa ter UV mapeado e o modificador Subdivision Surface com "UV Smooth" = None.

**Modo Sculpt:** forma da curva com Length ajustável e Points = 8 por padrão (16 para cabelo longo); "Interpolate" ligado para herdar atributos. Pincéis usados: Add, Grow/Shrink, Comb, Selection Paint, Smooth, Puff, Slide. Colisão (Use Sculpt Collision) com distância entre 0,001–0,005 m.

**Pilha de Geometry Nodes e valores de exemplo:**
- `Interpolate Hair Curves`: Surface = malha da cabeça; Surface Rest Position marcado; Distance to Guides = 0,01 m; Density = 300.000.
- `Set Hair Curve Profile`: Radius = 0,0003 m.
- `Hair Curves Noise`: Factor = 0,2; Distance = 0,02 m; Scale = 300.
- `Clump Hair Curves`: Shape = 0,220; Clump Offset = 0,015 m; Distance Threshold = 0,005 m.
- Ordem final: Interpolate Hair Curves → Set Hair Curve Profile → outros efeitos → `Deform Curves on Surface` por último.

**Divisão do penteado em regiões** (cada uma como objeto de curva separado): nuca, parte de trás, laterais/têmporas, costeletas, topo/coroa, franja.

**Material:** shader `Principled Hair BSDF`, com gradiente raiz→ponta usando o node `Curve Info`.

**Render no EEVEE:** em Curves > Shape, escolher `Strand` (leve) ou `Strip` (tipo fita, normais melhores); há opção de subdivisão adicional.

**Malha da franja (repartido central):** duplicar a cabeça, selecionar aresta central, `Ctrl+B` (edge loop), apagar faces centrais para separar a franja do resto; ativar **Part by Mesh Islands** no Interpolate Hair Curves para não interpolar entre ilhas de malha diferentes.

**Boas práticas:** fluxo não destrutivo, várias curvas por malha, refinar de trás para frente e conferir vários ângulos da câmera durante o processo.
