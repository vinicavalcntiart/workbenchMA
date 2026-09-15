# Dissertação

Pasta de trabalho da dissertação. Tudo que é texto vive aqui em Markdown; a versão final para a banca sai daqui para Word ou LaTeX só no fechamento.

| Campo | Valor |
|---|---|
| Título provisório | _a definir_ |
| Orientador(a) | _a definir_ |
| Linha de pesquisa | _a definir_ |
| Ingresso | 2026 |
| Qualificação prevista | _a definir_ |
| Defesa prevista | _a definir_ |

## Estrutura

```
dissertacao/
├── README.md           <- esta ficha e o estado atual do trabalho
├── projeto/            <- projeto de pesquisa: problema, objetivos, justificativa, metodologia
├── capitulos/          <- um arquivo por capítulo, numerado (01-introducao.md, 02-...)
├── leituras/           <- fichamentos específicos da dissertação (mesmo formato das disciplinas)
├── referencias/        <- referencias.md em ABNT e o .bib, se for usar LaTeX
├── orientacao/         <- atas das reuniões de orientação, uma por data (AAAA-MM-DD.md)
├── qualificacao/       <- texto entregue, parecer da banca e plano de ajustes
├── defesa/             <- versão final, apresentação e ata
├── figuras/            <- imagens, renders, diagramas usados no texto
└── dados/              <- entrevistas, questionários, material de campo (nunca dado sensível sem anonimizar)
```

## Regras

- Cada capítulo é um arquivo. Não fragmentar em seções separadas até o texto ter forma.
- Toda mudança de rumo no projeto (problema, objeto, método) entra em `projeto/decisoes.md` com data e motivo. Isso evita retrabalho e ajuda a escrever a introdução depois.
- Fichamentos de disciplina que virarem base da dissertação são **copiados** para `leituras/` aqui, não movidos. A disciplina mantém o histórico dela.
- `orientacao/` recebe uma nota depois de cada reunião: o que foi pedido, o que foi decidido, prazo.
- Nada de dado pessoal de participante de pesquisa no git. Se houver, fica fora do repositório e `dados/` só guarda o material já anonimizado.

## Estado atual

_Sem projeto definido. Primeiro passo: escrever `projeto/problema.md` com a pergunta de pesquisa em um parágrafo._
