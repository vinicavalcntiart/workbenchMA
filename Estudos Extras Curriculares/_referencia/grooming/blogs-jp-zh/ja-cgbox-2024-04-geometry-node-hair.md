---
titulo: 「Blender 4.1」ジオメトリノードヘアーの使い方
autor: CGbox編集部
url: https://cgbox.jp/2024/04/21/blender-geometory-node-hair/
data: 2024-04-21
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do blog. O conteúdo abaixo é uma extração técnica fiel (passos, lista de nodes e técnicas), obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Introdução geral ao "Geometry Node Hair" (Hair Curves) no Blender 4.1.

### 1. Adicionando Geometry Node Hair
Método: Shift+A → Curves → Empty Hair. Cria um objeto "Curves" parentado à malha selecionada. Alternar para modo Sculpt: Ctrl+Tab ou tecla Tab.

### 2. Configurações de exibição do cabelo
Motor de render precisa ser Cycles para a espessura aparecer corretamente. Para exibir no viewport do EEVEE: mudar Curve Shape de "Strand" para "Ribbon" nas propriedades. Curves > Shape controla a aparência.

### 3. Métodos de edição
Duas abordagens principais documentadas:

**Ferramentas do modo Sculpt de cabelo:** Add (追加), Delete (削除), Density (密度), Comb (くし), Snake Hook, Grow/Shrink (伸長/収縮), Pinch (ピンチ), Puff (パフ), Smooth (スムース), Slide (スライド).

**Hair Nodes (Geometry Nodes):** edição não destrutiva via pilha de modificadores.

### 4. Lista de nodes de cabelo principais
**Deformação:** Blend Hair Curves, Displace Hair Curves, Frizz Hair Curves, Hair Curves Noise, Roll Hair Curves, Rotate Hair Curves, Shrinkwrap Hair Curves, Smooth Hair Curves, Straighten Hair Curves, Trim Hair Curves.

**Geração:** Duplicate Hair Curves, Generate Hair Curves, Interpolate Hair Curves.

**Guias:** Braid Hair Curves, Clump Hair Curves, Create Guide Index Map, Curl Hair Curves.

**Leitura/escrita/utilitários:** Curve Info, Curve Root, Curve Segment, Curve Tip, Hair Attachment Info, além de outros nodes utilitários.

### 5. Técnicas úteis com nodes
- **Duplicate Hair Curves:** multiplica o cabelo dentro de um raio e quantidade especificados.
- **Set Hair Curve Profile:** ajusta a espessura (Shape em 0, modificar valor de Radius).
- **Frizz Hair Curves:** adiciona efeito de onda/permanente; ajustar Distance, Shape, Seed.

### 6. Exemplos de aplicação
**Coloração em gradiente:** Curve Info → Color Ramp → Principled Hair BSDF.
**Conversão em malha:** converter curvas em malha low-poly com aplicação de textura.
**Simulação:** simulação de tecido (cloth) ou Simulation Nodes para movimento dinâmico.

## Resumo em portugues (tecnicas)

Introdução geral ao sistema "**Geometry Node Hair**" (Hair Curves) no Blender 4.1.

**Adicionar cabelo:** `Shift+A → Curves → Empty Hair`, criando um objeto Curves filho da malha selecionada; entrar em modo Sculpt com `Ctrl+Tab` ou `Tab`.

**Exibição:** para ver a espessura correta é preciso usar o motor **Cycles**; no viewport do EEVEE, mudar Curve Shape de "Strand" para "Ribbon" (Curves > Shape).

**Duas formas de editar:**
- Modo Sculpt com pincéis: Add, Delete, Density, Comb, Snake Hook, Grow/Shrink, Pinch, Puff, Smooth, Slide.
- Hair Nodes (Geometry Nodes), edição não destrutiva via modificadores.

**Lista de nodes de cabelo (agrupados por categoria):**
- *Deformação:* Blend Hair Curves, Displace Hair Curves, Frizz Hair Curves, Hair Curves Noise, Roll Hair Curves, Rotate Hair Curves, Shrinkwrap Hair Curves, Smooth Hair Curves, Straighten Hair Curves, Trim Hair Curves.
- *Geração:* Duplicate Hair Curves, Generate Hair Curves, Interpolate Hair Curves.
- *Guias:* Braid Hair Curves, Clump Hair Curves, Create Guide Index Map, Curl Hair Curves.
- *Leitura/escrita/utilitários:* Curve Info, Curve Root, Curve Segment, Curve Tip, Hair Attachment Info, entre outros.

**Dicas práticas:** `Duplicate Hair Curves` multiplica fios dentro de um raio/quantidade; `Set Hair Curve Profile` ajusta espessura (Shape = 0 e mudar o Radius); `Frizz Hair Curves` cria efeito de permanente ajustando Distance, Shape e Seed.

**Aplicações extras:** gradiente de cor via `Curve Info → Color Ramp → Principled Hair BSDF`; converter as curvas em malha low-poly com textura para otimização; usar simulação de tecido ou Simulation Nodes para movimento dinâmico do cabelo.
