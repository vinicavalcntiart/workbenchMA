---
titulo: ヘアデザインメモ　Blenderジオメトリノードでヘアデザインの為のツールを作る
autor: へあでざいん(仮）
url: https://note.com/hair_drawings/n/neb3a7c4dff61
data: 2024-01-09
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do artigo. O conteúdo abaixo é uma extração técnica fiel, obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Artigo em note.com descrevendo uma ferramenta procedural própria, feita com Geometry Nodes, para acelerar o design de penteados.

### Função principal
A ferramenta gera um penteado de comprimento único (ワンレングス, "one length") aceitando um comprimento de cabelo especificado via parâmetro de altura de um plano, produzindo arestas de malha que resultam em cabelo reto quando "solto" (cai naturalmente pela gravidade).

### Passos do fluxo de trabalho mencionados
1. Selecionar a linha de arestas do nascimento do cabelo (hairline mesh row)
2. Executar a ferramenta de Geometry Nodes
3. Modificar a contagem de subdivisão
4. Converter em curvas (curves)
5. Converter em hair curves
6. Configurar Surface e UV da hair curve
7. Transformar em partículas
8. Aplicar dinâmica de cabelo (hair dynamics)

### Parâmetros-chave
- Slider "One Length Line": ajusta o comprimento total do cabelo
- Zona de correção do "diamond-plane": estende arestas acima deste plano de referência, compensando a curvatura do couro cabeludo e a gravidade
- Recursos de correção disponíveis tanto para vértices superiores quanto inferiores

### Objetivo do fluxo
A ferramenta prevê refinamento pós-aplicação usando ferramentas de corte e correções de comprimento após a simulação de dinâmica do cabelo.

### Referências citadas pelo autor
- "Blenderジオメトリノードではじめるプロシージャルモデリング" (livro de Simon Lenz / Simen Lenz, em japonês)
- Documentação de geometry nodes por 風見ひよこ, versão 3.6

## Resumo em portugues (tecnicas)

Artigo/nota descrevendo uma **ferramenta procedural própria em Geometry Nodes** para acelerar o design de penteados.

**O que a ferramenta faz:** gera um penteado de **comprimento único** ("one length") a partir da altura de um plano (que define o comprimento do cabelo), produzindo arestas que resultam em cabelo reto ao "cair" naturalmente.

**Fluxo de uso:**
1. Selecionar a linha de arestas do nascimento do cabelo.
2. Rodar a ferramenta de Geometry Nodes.
3. Ajustar a contagem de subdivisão.
4. Converter em Curves.
5. Converter em Hair Curves.
6. Configurar Surface e UV Map da hair curve.
7. Transformar em partículas.
8. Aplicar dinâmica de cabelo (simulação física).

**Parâmetros principais da ferramenta:**
- Slider **"One Length Line"** — controla o comprimento geral do cabelo.
- Zona de correção "diamond-plane" — estica arestas acima de um plano de referência para compensar a curvatura do couro cabeludo e o efeito da gravidade (com correção tanto para vértices de cima quanto de baixo).

**Uso previsto:** depois da simulação de dinâmica, o cabelo ainda passaria por corte e correção de comprimento manual.

**Referências citadas pelo autor:** o livro "Blenderジオメトリノードではじめるプロシージャルモデリング" (de Simon Lenz) e documentação de geometry nodes por 風見ひよこ (v3.6).
