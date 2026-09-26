---
titulo: Blender 4.2 LTS Release Notes: Import & Export - Hair Curves (USD/Alembic)
autor: n/d (Blender Developer Documentation)
url: https://developer.blender.org/docs/release_notes/4.2/pipeline_assets_io/
data: n/d (Blender 4.2 LTS, lancado jul/2024)
idioma: en
coletado_em: 2026-09-26
---

## USD

USD
¶
The hair curves object type is now supported for both import and export. (
ea256346a8
,
21db0daa4e
)
Point cloud import is now supported. (
e4ef0f6ff4
)
Unicode names are now supported on import and are optional for export. Only software using USD 24.03 or greater can support Unicode files. (
9ad2c7df0b
)
New Import options
Import only defined prims or all (
bfa54f22ce
)
Convert USD dome light to a world shader (
e1a6749b3d
)
Validate meshes on import (
2548132e23
)
New Export options
Filter which types to export (
a6a5fd053a
)
Convert the world shader to a USD dome light (
e1a6749b3d
)
Stage up axis (
2415380061
)
XForm operator convention (
36f1a4f94f
)
Triangulate meshes (
b2d1979882
)
Down-sample exported textures for USDZ (
3e73b9caa5
)
Generate MaterialX network from Blender shader nodes. Supports a subset of all shader nodes and their functionality. (
PR#122575
)
Rename active UV map to
st
, following USD conventions. This is enabled by default. (
eaeb8ba8cd
)

## Alembic

Alembic
¶
The hair curves object type is now supported for both import and export. (
ea256346a8
,
b24ac18130
)
Import multiple files at once. (
PR#121492
)
Fix: Addressed long-standing issue where animated curves would not update during render. (
ea256346a8
)



## Nota de coleta

Esta pagina de release notes cobre varias areas de Blender; conforme instrucao, foi coletada apenas a secao relevante a hair/Huang/curves. A pagina completa esta em https://developer.blender.org/docs/release_notes/4.2/pipeline_assets_io/ (pagina inteira nao coletada, apenas as secoes USD e Alembic referentes a hair curves).