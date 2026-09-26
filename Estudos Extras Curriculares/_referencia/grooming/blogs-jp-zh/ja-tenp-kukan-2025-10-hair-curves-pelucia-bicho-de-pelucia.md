---
titulo: 【Blender4.5】ヘアーカーブでふわふわぬいぐるみを作ろう：Fur
autor: 管理人 (blog 点P空間)
url: https://blog.tenp-kukan.com/6354/
data: 2025-10-07 (atualizado 2025-11-16)
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do blog. O conteúdo abaixo é uma extração técnica fiel (passos, parâmetros e valores), obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Tutorial estilizado: criar um bicho de pelúcia fofo (ふわふわ) usando Hair Curves + Fur.

### Configuração de material (partes rígidas)
- Olhos/nariz: Principled BSDF, Base Color preto, Roughness 0
- Costuras: Principled BSDF, Base Color branco, Roughness 0,7
- Corpo: Principled BSDF, Base Color branco/cinza, Roughness 1,0

### Processo de aplicação de fur
1. Selecionar o objeto do corpo
2. Aplicar: Shift+A > Curve > Fur
3. Apagar o modificador "Hair Curves Noise" desnecessário
4. Adicionar "Trim Hair Curves" via biblioteca do Asset Browser

### Parâmetros de Geometry Nodes
**Interpolate Hair Curves:** Density: 30.000
**Trim Hair Curves:** Length Factor: 0,6; Replace Length: desmarcado; Random Offset: 0,01

### Material do pelo
Ativar "Use Nodes" no objeto de Hair Curves; usa o Principled BSDF padrão, ajustável conforme preferência de cor.

Nível de dificuldade: 3,0 (intermediário)

## Resumo em portugues (tecnicas)

Tutorial estilizado para criar um **bicho de pelúcia fofo** usando o preset "Fur" do sistema Hair Curves.

**Material das partes rígidas:** olhos/nariz em preto (Roughness 0); costuras em branco (Roughness 0,7); corpo em branco/cinza (Roughness 1,0) — todos com Principled BSDF simples.

**Aplicação do pelo:**
1. Selecionar o objeto do corpo.
2. `Shift+A > Curve > Fur` (preset pronto do Blender, já vem com alguns modificadores).
3. Apagar o modificador `Hair Curves Noise` que vem por padrão (não é necessário aqui).
4. Adicionar `Trim Hair Curves` a partir do Asset Browser (biblioteca de assets de Hair).

**Parâmetros usados:**
- `Interpolate Hair Curves`: Density = 30.000.
- `Trim Hair Curves`: Length Factor = 0,6; Replace Length desmarcado; Random Offset = 0,01.

**Material do pelo:** ativar "Use Nodes" no próprio objeto de Hair Curves, usando o Principled BSDF padrão do Blender (não o Hair BSDF), com a cor ajustada livremente.

Nível de dificuldade indicado pelo autor: 3,0 (intermediário).
