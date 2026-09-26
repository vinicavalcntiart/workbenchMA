---
titulo: 【Blender4.5】簡単なヘアーカードの作り方：ヘアーカーブで作る生え際
autor: 管理人 (blog 点P空間)
url: https://blog.tenp-kukan.com/6878/
data: 2025-11-09 (atualizado 2025-11-16)
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do blog. O conteúdo abaixo é uma extração técnica fiel (passos, parâmetros e valores), obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Tutorial de criação de hair cards simples para o "生え際" (linha de nascimento do cabelo/franja), a partir de Hair Curves.

### Configuração de render
- Renderer: EEVEE
- Curves Shape: Strip
- Additional Subdivision: ~3

### Pilha de modificadores Geometry Nodes (em sequência)
1. **Interpolate Hair Curves** — Surface = plane; Density controla a quantidade de curvas.
2. **Trim Hair Curves** — Length Factor controla comprimento base; Random Offset varia o comprimento entre fios.
3. **Set Hair Curve Profile** — Radius ajusta espessura; Factor Min controla afinamento na ponta.
4. **Hair Curves Noise** — Distance controla intensidade de deformação; Shape (0 = deformação total); Scale (magnitude do ruído); Scale along Curve (variação raiz-ponta); Offset per Curve (deslocamento aleatório por curva).

### Saída de textura (nodes AOV)
Dados exportados: Intercept (gradiente raiz-ponta), Random (variação de cor), Normal (normais de superfície), Ambient Occlusion, Alpha.

### Câmera
Tipo: Ortográfica; Resolução: 4096×4096 ou 2048×2048.

### Parâmetros de material
Metallic: reflexão sutil; Specular/IOR Level: intensidade do brilho; Anisotropic: no máximo (para destaques direcionais tipo cabelo).

## Resumo em portugues (tecnicas)

Tutorial para criar **hair cards** simples destinados à linha de nascimento do cabelo (生え際), a partir de Hair Curves renderizadas e depois aplicadas como textura numa mesh/card.

**Render:** EEVEE; Curve Shape = Strip; Additional Subdivision ≈ 3.

**Pilha de Geometry Nodes (nesta ordem):**
1. `Interpolate Hair Curves` — Surface = plane; Density controla quantas curvas são geradas.
2. `Trim Hair Curves` — Length Factor (comprimento base); Random Offset (variação de comprimento entre fios).
3. `Set Hair Curve Profile` — Radius (espessura); Factor Min (afinamento na ponta).
4. `Hair Curves Noise` — Distance (intensidade); Shape = 0 (deformação total); Scale (magnitude do ruído); Scale along Curve (variação raiz→ponta); Offset per Curve (deslocamento aleatório entre curvas).

**Bake de textura via AOV:** Intercept, Random, Normal, Ambient Occlusion, Alpha — os mesmos "canais" usados no tutorial de sobrancelha (artigo 6844).

**Câmera:** ortográfica, 4096×4096 ou 2048×2048.

**Material do hair card final:** usa reflexão metálica sutil (Metallic baixo), Specular/IOR Level controlando o brilho, e Anisotropic no máximo para simular os reflexos direcionais típicos de fios de cabelo.
