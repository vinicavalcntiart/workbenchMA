---
titulo: "[Blender 4.4] リアルな髪の毛チャレンジ⑥"
autor: JUKKA
url: https://blog.jukkagraph.net/archives/6964
data: 2025-04-17
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do blog. O conteúdo abaixo é uma extração técnica fiel, obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Sexta parte: fluxo de trabalho para criar um rabo de cavalo (ponytail).

**Abordagem de modelagem:**
- Cabelo frontal e lateral: UV Sphere escalada em 0,2x, usando apenas as partes necessárias.
- Cabelo de trás: UV Sphere em escala 0,2x, rotacionada 90° no eixo X, ajustada ao formato da cabeça.

**Processo de criação do cabelo:** o autor descreve a conversão das malhas base através de um processo de duas etapas: "メッシュをそれぞれカーブ（向きを揃える）⇒ヘアカーブに変換してアセット追加" — converter cada malha em curva (alinhando a orientação) ⇒ converter em hair curve e adicionar os assets.

**Elementos adicionais:** o autor comenta que adicionar fios soltos ("アホ毛", os famosos "fios rebeldes" de personagens de anime) aumentaria ainda mais o realismo.

**Observação:** o post contém parâmetros técnicos mínimos — foca na metodologia do fluxo de trabalho ao invés de detalhes de node ou shader.

## Resumo em portugues (tecnicas)

Sexta parte: fluxo para criar um **rabo de cavalo (ponytail)**.

**Modelagem da base:**
- Cabelo frontal/lateral: UV Sphere escalada para 0,2x, usando só a parte necessária da esfera.
- Cabelo de trás: UV Sphere em 0,2x, rotacionada 90° no eixo X, ajustada ao formato da cabeça.

**Processo em duas etapas (citado literalmente pelo autor, traduzido):** 1) converter cada malha em curva, alinhando a orientação; 2) converter essa curva em hair curve e adicionar os assets de Geometry Nodes já usados nas partes anteriores.

**Ideia para melhorar o realismo:** adicionar fios soltos/rebeldes (アホ毛, "ahoge", comum em personagens de anime) para quebrar a uniformidade do penteado.

Post com poucos detalhes técnicos numéricos — o foco é na metodologia, não em valores específicos de nodes.
