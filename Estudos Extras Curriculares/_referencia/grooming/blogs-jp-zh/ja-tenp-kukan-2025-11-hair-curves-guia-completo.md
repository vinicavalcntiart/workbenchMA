---
titulo: 「Blender」ヘアーカーブガイド：ヘアー、ファーからヘアーカード作成まで
autor: 管理人 (blog 点P空間)
url: https://blog.tenp-kukan.com/7027/
data: 2025-11-16
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal (verbatim) do texto do blog. O conteúdo abaixo é uma extração técnica fiel (passos, nomes de nodes, parâmetros e estrutura), obtida via ferramenta de leitura automática da página e reorganizada por mim. Para o texto exato do autor, consulte a URL original.

## Notas técnicas (extração fiel do conteúdo original)

Este post funciona como um "hub"/guia geral do blog 点P空間 (tenp-kukan) sobre o sistema Hair Curves do Blender, cobrindo desde cabelo humano até fur (pelo de animal) e hair cards.

### Estrutura do guia
1. Visão geral: Hair Curves é definido como "cabelo baseado em curvas" (カーブベースの髪) que usa Geometry Nodes.
2. Início rápido: adicionar Curve (Hair Curves) → aplicar Geometry Nodes → ajustar parâmetros.
3. Coleção de tutoriais organizada por dificuldade e caso de uso.

### Nodes de Geometry Nodes citados no panorama geral
- **Deform Curves on Surface**
- **Trim Hair Curves**
- **Interpolate Hair Curves** — gera curvas filhas a partir de curvas-guia; o autor observa que às vezes as curvas não são geradas corretamente (bug/pegadinha comum)
- **AOV Output** — usado em fluxos de geração de textura (bake de mapas a partir das hair curves)

### Categorias de conteúdo do guia
**Hair (cabelo humano):**
- Fundamentos de uso básico
- Explicação dos nodes mais usados
- Métodos de conversão de malha (mesh) para Hair Curves
- Criação de textura de sobrancelha
- Geração de hair cards

**Fur (pelo de animal):**
- Criação de pelo realista
- Variações para bichos de pelúcia: feltro, fofo (fluffy), texturas "puffy"
- Aplicação de textura para padrões de pelagem

**Solução de problemas:**
- Falhas de geração do Interpolate Hair Curves
- Problemas de textura que não aparece

### Caminho de aprendizado recomendado pelo autor
Primeiro entender o básico em "como usar Hair Curves", depois ler "nodes mais usados" para dominar o vocabulário de nodes, depois avançar para simulação de qualidade e por fim integração em pipeline de jogos.

## Resumo em portugues (tecnicas)

Este artigo é um guia-índice do blog点P空間 sobre o sistema **Hair Curves** (カーブヘアー, cabelo baseado em curvas + Geometry Nodes) do Blender. Ele não traz um tutorial passo a passo único, mas organiza e resume os principais posts da série.

**Fluxo básico ensinado:** adicionar um objeto Curve do tipo Hair Curves → aplicar um modificador Geometry Nodes → ajustar parâmetros.

**Nodes de Geometry Nodes mencionados** (nomes mantidos em inglês, como aparecem no Blender):
- *Deform Curves on Surface* (deforma as curvas para acompanhar a superfície/malha animada)
- *Trim Hair Curves* (corta/ajusta o comprimento das curvas)
- *Interpolate Hair Curves* (interpola curvas-filha a partir das curvas-guia; o autor alerta sobre bugs onde as curvas não são geradas)
- *AOV Output* (saída de AOV, usada para gerar texturas via bake a partir das próprias curvas)

**Divisão temática do conteúdo do blog:**
- Cabelo humano (ヘアー/hair): uso básico, nodes frequentes, conversão de mesh para hair curves, textura de sobrancelha, criação de hair cards.
- Pelo de animal (ファー/fur): pelo realista e variações estilizadas para bichos de pelúcia (feltro, fofo, "puffy"), aplicação de textura de padrão de pelagem.
- Solução de problemas: falha de geração do Interpolate Hair Curves; textura que não aparece nas curvas.

**Trilha de estudo sugerida pelo autor:** primeiro o "como usar Hair Curves" (fundamentos) → depois "nodes mais usados" (vocabulário de nodes) → depois simulação com mais qualidade → por fim, otimização/pipeline para jogos.
