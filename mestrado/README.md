# Mestrado

Pasta raiz de tudo que é do mestrado. Nada da campanha de vagas entra aqui, e nada do mestrado sai daqui.

## Regra para os próximos chats

Cada disciplina tem a sua própria subpasta, uma por disciplina, com nome em `kebab-case`, sem acento e sem espaço:

```
mestrado/
├── README.md                       <- este arquivo
├── narrativas-transmidiaticas/     <- disciplina 1
├── outra-disciplina/               <- disciplina 2, e assim por diante
└── dissertacao/                    <- estrutura já criada, ver README próprio
```

Se a disciplina que o Vini estiver estudando ainda não tem pasta, crie a pasta antes de qualquer outra coisa. Não jogue arquivo solto na raiz de `mestrado/`.

## Estrutura dentro de cada disciplina

Toda pasta de disciplina começa com um `README.md` contendo: nome da disciplina, professor, semestre, ementa resumida e forma de avaliação. A partir daí, use as subpastas conforme o material aparecer:

```
<disciplina>/
├── README.md        <- ficha da disciplina (obrigatório)
├── ementa/          <- plano de curso, cronograma, bibliografia oficial
├── leituras/        <- fichamentos e resumos, um arquivo por texto
├── aulas/           <- anotações de aula, uma por data (AAAA-MM-DD-tema.md)
├── trabalhos/       <- rascunhos e versões dos trabalhos avaliativos
└── referencias.md   <- bibliografia consolidada em ABNT
```

Só crie a subpasta quando for usar. Pasta vazia não entra no git.

## Convenções

- Idioma: português, salvo citação direta.
- Fichamento de leitura: nome do arquivo é `sobrenome-ano-palavra-chave.md` (ex.: `jenkins-2009-cultura-da-convergencia.md`). Dentro, referência ABNT completa no topo, depois resumo, conceitos-chave, citações com página e um bloco final de "como isso conversa com a minha pesquisa".
- Trabalhos: versionar com sufixo `v1`, `v2`, e manter só a última como `final`.
- Commits: uma frase curta no imperativo, em português, prefixada com a disciplina. Ex.: `narrativas: fichamento de Scolari 2013`.
- Se o Vini quiser cruzar a disciplina com a produção em 3D e animação dele, isso entra no README da disciplina, na seção "Ligação com a pesquisa".

## Drive

Os arquivos pesados (PDFs, slides, DOCX) ficam no Google Drive, não no git. A raiz é a pasta `Mestrado_InLocal`:
https://drive.google.com/drive/folders/1-tqXd67gGBylIGXIv3lj-qlyzElDdb7q

Cada disciplina tem a pasta correspondente lá dentro. O link específico fica no README de cada disciplina. Os próximos chats têm acesso ao Drive pelo conector e podem ler os arquivos direto de lá.

Pastas já existentes no Drive que ainda **não** têm pasta aqui no repositório (criar quando forem trabalhadas): `Mídias digitais`, `Design da Info`, `Estágio de Docência`.

## Disciplinas

| Pasta | Disciplina | Status |
|---|---|---|
| `narrativas-transmidiaticas/` | Narrativas Transmidiáticas | em curso |
| `dissertacao/` | Dissertação (não é disciplina, tem regras próprias no README dela) | estrutura pronta |

Atualize esta tabela quando criar uma disciplina nova.
