# Get Attachment Surface

Fonte: Essentials asset library do Blender 5.2.2 LTS (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Surface Geometry (Geometry, default None)
- OUTPUT Surface UV Map (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38)
- OUTPUT Exists (Bool, default False)
- INPUT Geometry (Geometry, default None) — Geometry to get the bundle of

## Nodes (15)
- **Group Input** [NodeGroupInput]
- **Group Output** [NodeGroupOutput]
- **Get Geometry Bundle** [GeometryNodeGetGeometryBundle]
    inputs livres: Remove = False
- **Separate Bundle** [NodeSeparateBundle]
- **Warning** [GeometryNodeWarning]
    inputs livres: Message = Missing surface geometry
- **Domain Size** [GeometryNodeAttributeDomainSize]
- **Compare** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Boolean Math** [FunctionNodeBooleanMath] {operation=NOT}
- **Switch** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Domain Size.001** [GeometryNodeAttributeDomainSize]
- **Compare.001** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Separate Bundle.001** [NodeSeparateBundle]
- **Named Attribute** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
- **Switch.001** [GeometryNodeSwitch] {input_type=VECTOR}
- **Object Info** [GeometryNodeObjectInfo] {transform_space=RELATIVE}
    inputs livres: As Instance = False

## Ligacoes (20)
- Group Input.Geometry -> Get Geometry Bundle.Geometry
- Get Geometry Bundle.Bundle -> Separate Bundle.Bundle
- Separate Bundle.surface_geometry -> Domain Size.Geometry
- Domain Size.Point Count -> Compare.A
- Warning.Show -> Boolean Math.Boolean
- Boolean Math.Boolean -> Group Output.Exists
- Compare.Result -> Switch.Switch
- Separate Bundle.surface_geometry -> Switch.False
- Switch.Output -> Group Output.Surface Geometry
- Domain Size.001.Point Count -> Compare.001.A
- Switch.Output -> Domain Size.001.Geometry
- Compare.001.Result -> Warning.Show
- Get Geometry Bundle.Bundle -> Separate Bundle.001.Bundle
- Separate Bundle.001.surface_uv_map_name -> Named Attribute.Name
- Named Attribute.Attribute -> Switch.001.True
- Compare.Result -> Switch.001.Switch
- Separate Bundle.surface_uv_map -> Switch.001.False
- Switch.001.Output -> Group Output.Surface UV Map
- Separate Bundle.001.surface_object -> Object Info.Object
- Object Info.Geometry -> Switch.True
