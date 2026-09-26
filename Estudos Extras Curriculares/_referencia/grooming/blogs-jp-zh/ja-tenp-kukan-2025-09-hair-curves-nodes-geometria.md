---
titulo: 「Blender4.5」Hair Curves（ヘアーカーブ）のよく使うジオメトリノード解説
autor: 管理人 (blog 点P空間)
url: https://blog.tenp-kukan.com/6019/
data: 2025-09-21 (atualizado 2025-11-16)
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do blog. O conteúdo abaixo é uma extração técnica fiel (nomes de nodes, parâmetros e valores de exemplo), obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Este é o artigo mais denso em nomes de nodes de toda a série. Ele explica, node a node, os principais nodes de Geometry Nodes usados com Hair Curves no Blender 4.5, com tabela de parâmetros para cada um.

### Princípio de ordenação dos modificadores enfatizado pelo autor
1. Interpolate/Duplicate Hair Curves (gera curvas a partir das guias) — primeiro
2. Outras operações de deformação/estilo no meio
3. Deform Curves on Surface — sempre por último

O autor destaca que **Surface Rest Position** deve ficar habilitado em Interpolate Hair Curves para manter o alinhamento correto com a deformação da malha.

### Nodes documentados (nome em japonês / inglês, e parâmetros)

1. **Interpolate Hair Curves** (ヘアーカーブ補間) — gera curvas interpoladas a partir das curvas-guia sobre a geometria de superfície.
   Parâmetros: Surface / Surface UV Map (obrigatórios), Surface Rest Position (recomendado ligado), Follow Surface Normal, Part by Mesh Islands, Interpolation Guides (faixa 1–10), Distance to Guides, Poisson Disk Distribution, Density / Density Mask, Mask Texture, Viewport Amount, Seed.

2. **Hair Curves Noise** — aplica textura de ruído para gerar ondulação natural.
   Parâmetros: Cumulative Offset, Factor, Distance, Shape (-1.0 a 1.0), Scale, Scale along Curve, Offset per Curve, Preserve Length, Seed.

3. **Frizz Hair Curves** (縮毛・ちぢれ髪) — cria efeito de frizz/crespo, textura de permanente.
   Parâmetros: Cumulative Offset, Factor, Distance, Shape (-1 só raiz a 1 só ponta), Seed, Preserve Length.

4. **Set Hair Curve Profile** — controla o raio (espessura) ao longo da curva.
   Parâmetros: Replace Radius, Radius, Shape (perfil de afinamento, 0 = uniforme), Factor Min (razão de espessura na raiz), Factor Max (razão de espessura na ponta).

5. **Clump Hair Curves** (髪を房にする) — agrupa curvas vizinhas em torno de uma curva-guia (mechas/tufos).
   Parâmetros: Guide Distance, Guide Mask (vertex group), Existing Guide Map, Factor, Shape, Tip Spread, Clump Offset, Distance Falloff, Distance Threshold, Seed, Preserve Length.

6. **Trim Hair Curves** (髪の長さを変える) — ajusta/corta o comprimento das curvas de forma uniforme ou aleatória.
   Parâmetros: Scale Uniform, Length Factor, Replace Length, Length, Mask, Random Offset, Pin at Parameter (raiz/centro/ponta), Seed.

7. **Roll Hair Curves** (カーブを巻く) — deformação em espiral/enrolamento ao longo da curva.
   Parâmetros: Factor, Subdivision, Variation Level, Roll Length, Roll Radius, Roll Depth, Roll Taper, Retain Overall Shape, Random Orientation, Seed, Preserve Length.

8. **Curl Hair Curves** (髪カーブをカールさせる) — cria cachos/ondas verticais seguindo curvas-guia.
   Parâmetros: Guide Distance, Guide Mask, Existing Guide Map, Factor, Subdivision, Curl Start, Radius, Factor Start, Factor End, Frequency, Random Offset, Seed.

9. **Braid Hair Curves** (髪カーブを三つ編みにする) — trança as curvas em padrão de três fios.
   Parâmetros: Guide Distance / Guide Mask / Existing Guide Map, Factor / Subdivision, Braid Start (% de início), Radius, Shape, Factor Min / Factor Max, Frequency, Thickness, Thickness Shape, Shape Asymmetry, Flare Length, Flare Opening, Hair Tie (objeto de instância), Hair Tie Scale.

### Exemplos de aplicação com valores citados
- **Afro:** combina Clump + Noise + Curl + Roll com conjuntos específicos de parâmetros (empilhamento de nodes é pesado computacionalmente).
- **Cabelo ondulado (巻き髪):** Curl Hair Curves com Guide Distance 0.25 m, Subdivision 3, Curl Start 2, Radius 0.25 m, Frequency 1.5.
- **Trança:** Braid Hair Curves com Guide Distance 1.6 m, Subdivision 3, Braid Start 0.6, Radius 0.45 m, mais um objeto de instância tipo fita como "hair tie".

### Observações finais do autor
- O Asset Browser do Blender já traz ferramentas pré-configuradas de Hair Curves (arrastar-e-soltar).
- Uso de máscara requer que Interpolate Hair Curves esteja configurado com atributos de weight paint na superfície.
- O impacto de performance cresce muito ao empilhar vários nodes (o exemplo do afro é citado como pesado).

## Resumo em portugues (tecnicas)

Artigo de referência do blog 点P空間 que documenta, **node a node**, os principais nodes de Geometry Nodes do sistema Hair Curves (Blender 4.5).

**Regra de ordenação dos modificadores:** 1) gerar curvas (Interpolate/Duplicate Hair Curves) → 2) aplicar estilos/deformações → 3) por último, sempre `Deform Curves on Surface`. É essencial deixar **Surface Rest Position** ativado em Interpolate Hair Curves para a deformação da malha funcionar corretamente.

**Lista de nodes e para que servem:**
- `Interpolate Hair Curves` — interpola curvas-filha a partir de curvas-guia numa superfície. Parâmetros principais: Surface, Surface UV Map, Surface Rest Position, Follow Surface Normal, Part by Mesh Islands, Interpolation Guides (1–10), Distance to Guides, Poisson Disk Distribution, Density/Density Mask, Mask Texture, Viewport Amount, Seed.
- `Hair Curves Noise` — ruído/ondulação natural. Parâmetros: Cumulative Offset, Factor, Distance, Shape (-1 a 1), Scale, Scale along Curve, Offset per Curve, Preserve Length, Seed.
- `Frizz Hair Curves` — frizz/crespo (efeito de permanente). Parâmetros: Cumulative Offset, Factor, Distance, Shape (-1 raiz / 1 ponta), Seed, Preserve Length.
- `Set Hair Curve Profile` — espessura (raio) ao longo da curva. Parâmetros: Replace Radius, Radius, Shape, Factor Min, Factor Max.
- `Clump Hair Curves` — agrupa mechas em torno de guias. Parâmetros: Guide Distance, Guide Mask, Existing Guide Map, Factor, Shape, Tip Spread, Clump Offset, Distance Falloff, Distance Threshold, Seed, Preserve Length.
- `Trim Hair Curves` — corta/redimensiona comprimento. Parâmetros: Scale Uniform, Length Factor, Replace Length, Length, Mask, Random Offset, Pin at Parameter, Seed.
- `Roll Hair Curves` — enrolamento em espiral. Parâmetros: Factor, Subdivision, Variation Level, Roll Length, Roll Radius, Roll Depth, Roll Taper, Retain Overall Shape, Random Orientation, Seed, Preserve Length.
- `Curl Hair Curves` — cachos. Parâmetros: Guide Distance, Guide Mask, Existing Guide Map, Factor, Subdivision, Curl Start, Radius, Factor Start, Factor End, Frequency, Random Offset, Seed.
- `Braid Hair Curves` — trança de três fios. Parâmetros: Guide Distance/Mask/Existing Guide Map, Factor, Subdivision, Braid Start, Radius, Shape, Factor Min/Max, Frequency, Thickness, Thickness Shape, Shape Asymmetry, Flare Length, Flare Opening, Hair Tie, Hair Tie Scale.

**Exemplos práticos com valores:**
- Afro: pilha de Clump + Noise + Curl + Roll (pesado para processar).
- Cabelo ondulado: `Curl Hair Curves` — Guide Distance 0,25 m; Subdivision 3; Curl Start 2; Radius 0,25 m; Frequency 1,5.
- Trança: `Braid Hair Curves` — Guide Distance 1,6 m; Subdivision 3; Braid Start 0,6; Radius 0,45 m; usa objeto de instância (fita) como "elástico de cabelo".

**Dicas finais:** o Asset Browser do Blender tem esses nodes prontos para arrastar; máscaras exigem que a superfície tenha atributos de weight paint corretamente configurados no Interpolate Hair Curves; empilhar muitos nodes pesa bastante no desempenho do viewport/render.
