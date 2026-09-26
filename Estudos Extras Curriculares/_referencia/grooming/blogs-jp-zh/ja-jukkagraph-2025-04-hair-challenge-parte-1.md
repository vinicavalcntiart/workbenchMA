---
titulo: "[Blender 4.4] リアルな髪の毛チャレンジ①"
autor: JUKKA
url: https://blog.jukkagraph.net/archives/6937
data: 2025-04-11/12
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do blog. O conteúdo abaixo é uma extração técnica fiel, obtida via ferramenta de leitura automática e reorganizada por mim. Este post tem tom de "diário de desenvolvimento" pessoal, com poucos parâmetros numéricos exatos.

## Notas técnicas (extração fiel do conteúdo original)

Primeiro post de uma série de tentativas de fazer cabelo realista no Blender 4.4.

**Fluxo seguido:** criação de malha → conversão para curva → ajuste de direção das normais → conversão para hair curves.

**Passos principais:**
1. Converter a malha em curva, depois ajustar a orientação das normais antes de transformar em hair curves.
2. Após converter em hair curves, o autor arrastou dois assets da biblioteca: "Set Hair Curve Profile" e "Duplicate Hair Curves".
3. Adicionou geometria extra para evitar buracos na linha do cabelo (nascimento), com parâmetros específicos mostrados apenas nas imagens (não descritos em texto).

**Dificuldades:** a conversão para hair curves produziu resultados inesperados no início, exigindo ajuste dos assets; a linha do cabelo ficou rígida/"quebrada" demais (パキっとしてしまう) apesar de seguir o tutorial de referência; atribuído a densidade alta demais e poucos pontos na curva perto do nascimento do cabelo; não conseguiu estilizar a franja, ficando com corte de um só comprimento (ワンレングス).

**Resultado:** não fotorrealista ainda; autor identifica melhorias futuras — aumentar pontos de ancoragem e refinar a geometria do cabelo frontal.

## Resumo em portugues (tecnicas)

Primeiro post do "desafio de cabelo realista" (série pessoal do autor JUKKA).

**Fluxo:** malha → curva (ajustando a direção das normais) → hair curves.

**Assets usados (arrastados da biblioteca do Blender):** `Set Hair Curve Profile` e `Duplicate Hair Curves`. Foi adicionada geometria extra manualmente para evitar falhas visuais na linha do nascimento do cabelo (parâmetros exatos só nas imagens, não descritos em texto).

**Problemas encontrados:** resultado inicial da conversão para hair curves veio errado, precisou reajustar os assets; a linha do cabelo ficou "rígida"/quebrada, provavelmente por densidade alta demais e poucos pontos de controle na curva perto da raiz; não conseguiu estilizar a franja (ficou com corte único, "one length").

**Conclusão do autor:** resultado ainda não fotorrealista; próximos passos planejados: aumentar o número de pontos de ancoragem e refinar a geometria da parte frontal do cabelo.
