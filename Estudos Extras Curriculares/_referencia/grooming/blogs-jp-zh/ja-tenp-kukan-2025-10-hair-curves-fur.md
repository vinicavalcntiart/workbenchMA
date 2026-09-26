---
titulo: 【Blender4.5】ヘアーカーブでFur（ファー）を作ろう
autor: 管理人 (blog 点P空間)
url: https://blog.tenp-kukan.com/6245/
data: 2025-10-09 (atualizado 2025-11-16)
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do blog. O conteúdo abaixo é uma extração técnica fiel (passos, parâmetros e valores), obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Tutorial de criação de fur (pelo) realista para um personagem tipo gato, usando Hair Curves.

### Configuração inicial
- Adicionar "Empty Hair" via Shift+A > Curve > Empty Hair
- Entrar em modo Sculpt no objeto de Hair Curves

### Pincel de densidade (curvas-guia)
- Mode: Auto
- Distance Min: 0,02 m
- Curve Shape: Length 0,1 m; Points 6
- X Symmetry e Use Sculpt Collision ativados

### Ajuste de comprimento
- Pincel Grow/Shrink: Minimum Length 0,07 m na área do rosto, reduzindo progressivamente a 0,05 m e depois 0,03 m perto de olhos/nariz

### Penteação (grooming)
- Pincel Comb: X Symmetry ativado; Use Sculpt Collision ativado; distância de colisão 0,002 m; cria fluxo direcional saindo dos traços do rosto

### Posicionamento do pelo
- Pincel Puff: Strength 0,25; Effect Range: Projected; levantar 60–70% (elevação parcial)

### Configuração de Geometry Nodes
1. **Interpolate Hair Curves** — Surface: malha da cabeça; Surface Rest Position ✓; Follow Surface Normal ✓; Distance to Guides: 0,01–0,02 m; Density: 10.000+ (ajustar conforme desempenho do PC)
2. **Set Hair Curve Profile** — Radius: 0,003 m (pelo do corpo); 0,001 m (interior da orelha); 0,01 m (bigodes/sobrancelhas); Shape: 0,8 (bigodes)
3. **Trim Hair Random** (node customizado, duplicando "Trim Hair Curves" e adicionando Random Value na entrada Selection) — Length Factor: 1,5–1,8; Random Offset: 0,3 m; Probability: 0,1–0,5 (taxa de corte aleatório)

### Configuração de material
**Pelo do corpo — Principled Hair BSDF:** Color: padrão pintado via textura; Roughness: 0,7; Radial Roughness: 0,3–0,5; Random Roughness: 0,1–0,2.
**Bigodes/sobrancelhas — Principled Hair BSDF:** Color: branco; Roughness: 0,5.

### Abordagem multi-curva
Corpo principal: pelo base (0,1 m); pelo curto da orelha: gradiente 0,03–0,1 m; pelo longo da orelha: comprimento variável com randomização; volume adicional pescoço/orelha: densidade 50.000; bigodes/sobrancelhas: 8–10 curvas, shape suave.

### Notas críticas
- Referência de tamanho da malha: cabeça de gato com 1,46 m de largura (escala do arquivo/projeto, não realista)
- Ativar "Front Faces Only" (pincel Add) em geometria fina
- Copiar modificadores entre curvas via Ctrl+L > Copy Modifiers
- Ao duplicar setups, casar a malha de Surface no node Interpolate

## Resumo em portugues (tecnicas)

Tutorial de criação de **fur (pelo) realista** para um personagem tipo gato, usando Hair Curves.

**Setup inicial:** `Shift+A > Curve > Empty Hair`, depois entrar em modo Sculpt.

**Pincel de densidade (guias):** Mode Auto; Distance Min 0,02 m; Curve Shape Length 0,1 m, Points 6; X Symmetry e Use Sculpt Collision ligados.

**Comprimento:** pincel Grow/Shrink com comprimento mínimo 0,07 m no rosto, reduzindo para 0,05 m e depois 0,03 m perto de olhos/nariz.

**Penteação:** pincel Comb com simetria X, colisão ativada (distância 0,002 m), criando fluxo saindo dos traços faciais.

**Volume:** pincel Puff, Strength 0,25, Effect Range Projected, elevação de 60–70%.

**Geometry Nodes:**
- `Interpolate Hair Curves`: Surface = cabeça; Surface Rest Position e Follow Surface Normal ligados; Distance to Guides 0,01–0,02 m; Density 10.000+ (ajustar pela performance da máquina).
- `Set Hair Curve Profile`: Radius 0,003 m (corpo), 0,001 m (dentro da orelha), 0,01 m (bigodes/sobrancelhas); Shape 0,8 para bigodes.
- Node customizado "Trim Hair Random" (duplicata de `Trim Hair Curves` + `Random Value` na Selection): Length Factor 1,5–1,8; Random Offset 0,3 m; Probability 0,1–0,5.

**Material (Principled Hair BSDF):** pelo do corpo com Roughness 0,7, Radial Roughness 0,3–0,5, Random Roughness 0,1–0,2; bigodes/sobrancelhas brancos com Roughness 0,5.

**Estratégia multi-curva:** objetos de curva separados para corpo (base 0,1 m), pelo curto/longo da orelha, volume extra no pescoço/orelha (densidade 50.000) e bigodes/sobrancelhas (8–10 curvas).

**Dicas práticas:** ativar "Front Faces Only" no pincel Add em áreas de geometria fina; copiar modificadores entre objetos de curva via `Ctrl+L > Copy Modifiers`; ao duplicar um setup para outra parte do corpo, sempre reatribuir a malha de Surface correta no Interpolate Hair Curves.
