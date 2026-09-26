---
titulo: 【Blender4.5】Principled Hair BSDF、Hair BSDFでリアルな髪の毛マテリアルを作る
autor: 管理人 (blog 点P空間)
url: https://blog.tenp-kukan.com/5043/
data: 2025-09-21 (atualizado 2025-11-16)
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do blog. O conteúdo abaixo é uma extração técnica fiel (parâmetros de shader), obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Explica os dois shaders de cabelo do Blender: **Hair BSDF** (mais simples) e **Principled Hair BSDF** (mais completo, baseado no Chiang model).

### Hair BSDF
Oferece dois componentes: Reflection (reflexo de superfície, cria brilho) e Transmission (luz passando através do fio, permitindo transparência).
Parâmetros principais: Color, Offset (ajusta o ângulo de reflexão/transmissão, posição do highlight), Roughness U/V (U = ao longo do fio; V = perpendicular), Tangent (requer dado de direção do fio).

### Principled Hair BSDF
Shader baseado em física, combina três elementos: método de especificação de cor, modelo de reflexão/transmissão, e opções de randomização.

**Setup recomendado para cabelo realista:** Color Mode = "Melanin Concentration"; Model Type = "Chiang Model".

**Métodos de especificação de cor:**
1. Direct Coloring — RGB direto
2. Melanin Concentration — Eumelanin (0–1) + Pheomelanin, com tingimento opcional
3. Absorption Coefficient — baseado em absorção óptica por comprimento de onda

**Parâmetros do Chiang Model:** Roughness (especularidade ao longo do fio); Radial Roughness (espalhamento perpendicular da luz); Coat (reforça a camada de reflexo inicial).

**Parâmetros do Huang Model:** Aspect Ratio (elipticidade da seção transversal do fio, varia por etnia: 0,5–1,0); Roughness (reflexão/transmissão baseada em microfacetas).

**Parâmetros comuns:** IOR (índice de refração, padrão 1,55); Offset (ângulo da cutícula); Random Roughness e Random Color (variação natural entre fios).

### Exemplo de configuração (cabelo preto)
Melanin: 0,859 | Melanin Redness: 0,145 | Roughness: 0,223 | Radial Roughness: 0,355

## Resumo em portugues (tecnicas)

Guia sobre os dois shaders de cabelo do Blender: `Hair BSDF` (simples) e `Principled Hair BSDF` (físico, baseado no Chiang Model).

**`Hair BSDF`:** dois componentes — Reflection (brilho de superfície) e Transmission (luz atravessando o fio). Parâmetros: Color, Offset (ângulo do highlight), Roughness U (ao longo do fio) e V (perpendicular), Tangent (precisa da direção do fio).

**`Principled Hair BSDF`:** combina método de cor + modelo de reflexão/transmissão + randomização.
- **Configuração recomendada para realismo:** Color Mode = Melanin Concentration; Model Type = Chiang Model.
- **Métodos de cor:** Direct Coloring (RGB); Melanin Concentration (Eumelanin 0–1 + Pheomelanin, com tingimento opcional); Absorption Coefficient (por absorção óptica).
- **Parâmetros do Chiang Model:** Roughness (especular ao longo do fio), Radial Roughness (espalhamento perpendicular), Coat (reforça reflexo inicial/cutícula).
- **Parâmetros do Huang Model:** Aspect Ratio (elipticidade da seção do fio, 0,5–1,0 conforme etnia), Roughness (reflexão/transmissão via microfacetas).
- **Parâmetros comuns:** IOR (padrão 1,55), Offset (ângulo da cutícula), Random Roughness e Random Color (variação entre fios).

**Exemplo de valores para cabelo preto:** Melanin 0,859; Melanin Redness 0,145; Roughness 0,223; Radial Roughness 0,355.
