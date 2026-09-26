# Referencia local do Blender 5.2 LTS

Copia em texto da documentacao oficial, para consulta offline e para o Claude
responder duvidas com a fonte na mao em vez de memoria.

## O que tem

| Pasta | Conteudo | Origem | Formato |
|---|---|---|---|
| `blender-manual-5.2-lts/manual/` | Manual do usuario completo, 2.358 paginas | projects.blender.org/blender/blender-manual, branch `blender-v5.2-release`, commit `4a3be8f9ed` de 17/08/2026 | reStructuredText (`.rst`), sem imagens |
| `grooming/` | Base de conhecimento de grooming: sintese `CEREBRO_GROOMING.md`, internals dos 27 node groups da Essentials, 40 fontes de dev e comunidade, 23 artigos JP/ZH, transcricoes de palestras | coletado em 2026-09-26, ver manifestos em cada subpasta | Markdown |
| `blender-python-api-5.2/api/` | Referencia da API Python (bpy, bmesh, mathutils, gpu...), 2.161 paginas | docs.blender.org/api/5.2, zip oficial `blender_python_reference_5_2.zip` | texto extraido do HTML (`.txt`) |

As imagens do manual ficaram de fora de proposito: 17 MB de figuras que nao
ajudam em busca por texto. A versao com figuras esta em docs.blender.org.

## Como achar as coisas

O manual segue a arvore de menus do Blender. Exemplos:

- Hair curves e hair nodes: `manual/modeling/geometry_nodes/hair/`
- Sculpt de curvas: `manual/sculpt_paint/curves_sculpting/`
- Fisica nova (Hair Dynamics, XPBD): `manual/modeling/geometry_nodes/simulation/`
- Shader de cabelo (Principled Hair BSDF): `manual/render/shader_nodes/shader/hair_principled.rst`
- Alembic e USD: `manual/files/import_export/`

Na API, cada tipo e um arquivo: `api/bpy.types.Curves.txt`,
`api/bpy.ops.curves.txt`, `api/bpy.types.NodesModifier.txt`.

Busca rapida no terminal:

```
grep -ril "clump" "Estudos Extras Curriculares/_referencia/blender-manual-5.2-lts/manual"
grep -n "remove_curves" "Estudos Extras Curriculares/_referencia/blender-python-api-5.2/api/bpy.types.Curves.txt"
```

## Licenca

O manual do Blender e CC-BY-SA 4.0 (Blender Manual contributors), texto
integral em `blender-manual-5.2-lts/LICENSE`. A referencia da API e gerada do
codigo-fonte do Blender, GPL-2.0-or-later. Nada aqui foi alterado alem de
tirar imagens e converter HTML em texto.

## Atualizar

```
git clone --depth 1 --branch blender-v5.2-release https://projects.blender.org/blender/blender-manual.git
```

Copiar os `.rst` de `manual/` sem a pasta `images/`. Para a API, baixar o zip
em docs.blender.org/api/5.2 e converter os `.html` para texto.
