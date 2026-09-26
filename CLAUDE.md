# Instrucoes para o Claude neste repositorio

## Perguntas sobre Blender

Antes de responder qualquer duvida sobre Blender (interface, hair curves,
Geometry Nodes, fisica, render, export, API Python, addons), consulte a base
local em `Estudos Extras Curriculares/_referencia/`:

1. Para grooming, comece por `grooming/CEREBRO_GROOMING.md`: e a sintese com
   a stack canonica, o funcionamento interno dos nodes, os problemas comuns e
   as citacoes. Siga as citacoes para as pastas `grooming/essentials-internals/`
   (como cada node group funciona por dentro), `grooming/blender-dev/`,
   `grooming/comunidade/`, `grooming/blogs-jp-zh/` e `grooming/palestras/`.
2. Para definicao de node, brush ou parametro, `blender-manual-5.2-lts/manual/`.
3. Para API Python e addons, `blender-python-api-5.2/api/`.

Use `grep`, cite o arquivo consultado, e diga quando a resposta veio de
memoria em vez da fonte. Quando o usuario relatar algo que funcionou ou
quebrou no groom dele, registre no CEREBRO_GROOMING.md como "observado em
producao" com data e versao. O README de `_referencia/` explica a organizacao.
Escopo: so Blender e Geometry Nodes; nao trazer XGen, Houdini nem addons de
terceiros para a base.

O usuario e Senior 3D Character Artist com experiencia em XGen, Houdini e
particle hair. Respostas tecnicas curtas, sem padding. Quando ele disser que
o texto esta longo ou tecnico demais, reduza para passos numerados curtos.
