# Get Hair Surface Geometry

Fonte: Essentials asset library do Blender 5.2.2 LTS (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Surface Geometry (Geometry, default None)
- OUTPUT Surface UV Map (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38)
- OUTPUT Exists (Bool, default False)
- INPUT Geometry (Geometry, default None) — Geometry to get the bundle of

## Nodes (5)
- **Get Attachment Surface.001** [GeometryNodeGroup] -> grupo 'Get Attachment Surface'
- **Group Output** [NodeGroupOutput]
- **Group Input** [NodeGroupInput]
- **Warning** [GeometryNodeWarning]
    inputs livres: Message = Missing hair surface geometry. Use 'Attach Hair Curves to Surface'.
- **Boolean Math.002** [FunctionNodeBooleanMath] {operation=NOT}

## Ligacoes (6)
- Get Attachment Surface.001.Surface Geometry -> Group Output.Surface Geometry
- Get Attachment Surface.001.Surface UV Map -> Group Output.Surface UV Map
- Group Input.Geometry -> Get Attachment Surface.001.Geometry
- Get Attachment Surface.001.Exists -> Group Output.Exists
- Boolean Math.002.Boolean -> Warning.Show
- Get Attachment Surface.001.Exists -> Boolean Math.002.Boolean
