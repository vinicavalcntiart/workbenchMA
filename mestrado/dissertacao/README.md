# Dissertação

Pasta de trabalho da dissertação. Tudo que é texto vive aqui em Markdown; a versão final para a banca sai daqui para Word só no fechamento.

| Campo | Valor |
|---|---|
| Título | **Traço Brasileiro: identidade visual no design de personagens da cultura pop** |
| Autor | Vinícius Vieira Cavalcanti |
| Programa | Mestrado Profissional em Indústrias Criativas, PPGIC, UNICAP (Recife) |
| Linha de pesquisa | Tecnologias, Linguagens e Produtos |
| Orientador | Prof. Dr. Breno José Andrade de Carvalho |
| Ingresso | 2026 |
| Qualificação | projeto de produto pronto (versão de 03/08/2026); data da banca _a confirmar_ |
| Defesa prevista | Ago–Dez 2026 pelo cronograma do projeto (Quadro 3) |

## Drive

| Pasta | Link | Conteúdo |
|---|---|---|
| `Dissertacao_Referencias/` | https://drive.google.com/drive/folders/1oWi0raS6E4nOfEj0OL-OXYhWsnkj4aSB | raiz |
| `Bibliografia/` | https://drive.google.com/drive/folders/1BHMUIFvBDq18YE3TmtHyj4XblWQUjsht | 42 arquivos: PDFs da bibliografia, fontes primárias (revistas Mônica, Menino Maluquinho), manuais ABNT da UNICAP e o projeto de qualificação em DOCX e PDF |
| `Dissertação/` | https://drive.google.com/drive/folders/1HWVZzbvuF9hx69RiphfGsty89XyBXT6y | exportação do Zotero (`Dissertação.rdf` + `files/`) |

O projeto de qualificação vivo é o arquivo `Traço Brasileiro - desvendando a identidade visual no design de personagens da cultura pop.docx` dentro de `Bibliografia/`. Os próximos chats podem ler esse arquivo direto pelo conector do Drive.

## O projeto em um parágrafo

Pergunta-problema: de que forma obras de diferentes períodos da cultura pop nacional permitem identificar elementos recorrentes que constituem uma identidade visual brasileira no design de personagens? Estudo de casos múltiplos descritivo (Yin, 2015) sobre três obras de períodos e mídias distintos: **Turma da Mônica** (Revista Mônica nº 1, Panini, 2007), **Menino Maluquinho** (Ziraldo, 1980) e **Irmão do Jorel** (Cartoon Network, 2014). Análise em três escalas: descrição técnica (Loomis: proporção, volume e massa), interpretação comunicativa (Rossi, Gomes e Andrade: Teoria da Forma) e historicização sociocultural (Bakhtin: dialogismo e autor-herói). Produto técnico: **manual de diretrizes para o design de personagens brasileiros**, em PDF, estruturado a partir da metodologia de Rocha (2023), distribuído em site próprio com acesso aberto. Sem sujeitos humanos, sem CEP.

## Sumário do projeto de qualificação

1. Introdução
2. Justificativa
3. Objetivos (geral e específicos)
4. Fundamentação teórica: design de personagens e cultura pop; dialogismo, autor-herói e identidade cultural; proporção, volume e massa; racismo algorítmico; síntese
5. Metodologia: caracterização; posicionamento ético; proposições; seleção dos casos; fontes de evidência; instrumento de coleta e análise; validade e confiabilidade; produto técnico
6. Resultados esperados
7. Impactos esperados
8. Transferência de resultados
9. Cronograma

## Cronograma (Quadro 3 do projeto)

| Atividade | Ago–Dez 2026 | Jan–Jun 2027 | Jul–Dez 2027 |
|---|---|---|---|
| Análise individual das três obras | ● | | |
| Análise cruzada e elementos recorrentes | ● | | |
| Desenvolvimento do manual | ● | | |
| Artigos e eventos científicos | ● | ● | ● |
| Redação final | ● | ● | |
| Preparação e defesa | ● | | |

Nota: o cronograma do projeto concentra quase tudo em Ago–Dez 2026. Vale rever com o orientador depois da qualificação.

## Estrutura

```
dissertacao/
├── README.md           <- esta ficha e o estado atual do trabalho
├── projeto/            <- projeto de pesquisa: problema, objetivos, justificativa, metodologia
├── capitulos/          <- um arquivo por capítulo, numerado (01-introducao.md, 02-...)
├── leituras/           <- fichamentos específicos da dissertação (mesmo formato das disciplinas)
├── referencias/        <- referencias.md em ABNT (já populado a partir do projeto)
├── orientacao/         <- atas das reuniões de orientação, uma por data (AAAA-MM-DD.md)
├── qualificacao/       <- texto entregue, parecer da banca e plano de ajustes
├── defesa/             <- versão final, apresentação e ata
├── figuras/            <- imagens, renders, diagramas usados no texto
└── dados/              <- material de análise (fichas das obras, quadros de análise)
```

## Regras

- Cada capítulo é um arquivo. Não fragmentar em seções separadas até o texto ter forma.
- Toda mudança de rumo no projeto (problema, objeto, método, corpus) entra em `projeto/decisoes.md` com data e motivo.
- Fichamentos de disciplina que virarem base da dissertação são **copiados** para `leituras/` aqui, não movidos. A disciplina mantém o histórico dela.
- `orientacao/` recebe uma nota depois de cada reunião: o que foi pedido, o que foi decidido, prazo.
- `referencias/referencias.md` é a fonte única da bibliografia. Novo texto entra primeiro ali, depois no Zotero e no Word.
- PDFs não entram no git. Ficam no Drive em `Bibliografia/`; aqui só o fichamento.

## Estado atual

Projeto de qualificação escrito e revisado (03/08/2026). Próximos passos: confirmar data da banca; depois da qualificação, registrar o parecer em `qualificacao/` e abrir `projeto/decisoes.md` com os ajustes pedidos. A análise das três obras (etapa 1 do cronograma) ainda não começou no repositório.
