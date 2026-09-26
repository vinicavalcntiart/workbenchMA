---
titulo: 【Blender4.5】ヘアーカーブで眉毛テクスチャを作る
autor: 管理人 (blog 点P空間)
url: https://blog.tenp-kukan.com/6844/
data: 2025-11-07
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do blog. O conteúdo abaixo é uma extração técnica fiel (passos, parâmetros e valores), obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Guia de nível intermediário (dificuldade 3.0) para criar textura semi-realista de sobrancelha usando Hair Curves + render composto (bake de AOVs).

### Configuração inicial das Hair Curves
- Criar um Plane e adicionar Curve > Empty Hair
- Motor de render: EEVEE
- Curve shape: Strip
- Additional Subdivision: 3

### Configurações do pincel de densidade
- Distance Min: 0,015 m
- Curve Shape Length: 0,3 m
- Points: 6

### Técnica de direção do fio (fluxo)
Duas direções de fluxo que se cruzam:
1. Fluxo superior: horizontal para diagonal-direita
2. Fluxo inferior: para cima → horizontal → diagonal-direita

O autor observa que, da cabeça à cauda da sobrancelha, a direção do fio vai transicionando entre essas direções.

### Aplicação de Geometry Nodes
`Set Hair Curve Profile` com Radius por volta de 0,01 m para afinar as pontas dos fios.

### Saída de textura via AOV
Dados exportados: Curves Info: Intercept (value), Random (value); Geometry: Normal (color); Ambient Occlusion: AO (value); canal Alpha (padrão).

### Configuração de câmera
Tipo: Ortográfica; Resolução: 2048×2048; Fundo: transparente.

### Rede de shader do material final
- Alpha + Normal → direto no Principled BSDF
- AO (Multiply Mix) → Base Color
- Random → variação de cor
- Intercept + Backfacing → Mix Shader Factor (transparência na raiz via Transparent Shader)

Esse fluxo permite iteração rápida: modificar as Hair Curves, renderizar de novo, e atualizar as texturas de imagem, tudo dentro do mesmo processo.

## Resumo em portugues (tecnicas)

Tutorial (dificuldade intermediária) para gerar uma **textura de sobrancelha** semi-realista a partir de Hair Curves, via bake de AOVs.

**Setup:** um Plane com `Curve > Empty Hair`; render engine EEVEE; Curve Shape = Strip; Additional Subdivision = 3.

**Pincel de densidade:** Distance Min = 0,015 m; Curve Shape Length = 0,3 m; Points = 6.

**Direção do fio:** dois fluxos que se cruzam — um de cima (horizontal → diagonal para a direita) e um de baixo (para cima → horizontal → diagonal para a direita), simulando a transição natural da cabeça à cauda da sobrancelha.

**Geometry Nodes:** `Set Hair Curve Profile` com Radius ≈ 0,01 m para afinar as pontas.

**Saída via AOV (para textura):** Intercept (gradiente raiz-ponta), Random (variação de cor), Normal, Ambient Occlusion, Alpha.

**Câmera:** ortográfica, 2048×2048, fundo transparente.

**Shader do material final:** Alpha e Normal ligados direto ao Principled BSDF; AO multiplicado na Base Color; Random usado para variar a cor; Intercept combinado com Backfacing controla o Fac de um Mix Shader com Transparent BSDF (deixa a raiz transparente).

Vantagem do método: iteração rápida — ajusta as Hair Curves, renderiza de novo e atualiza as texturas de imagem, sem precisar refazer tudo manualmente.
