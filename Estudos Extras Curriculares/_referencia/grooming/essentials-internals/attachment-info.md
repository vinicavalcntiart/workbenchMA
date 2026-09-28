# Attachment Info

Fonte: Essentials asset library do Blender 5.2.2 LTS (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Surface Geometry (Geometry, default None)
- OUTPUT Surface Exists (Bool, default False)
- OUTPUT Attachment UV (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Surface attachment UV coordinates stored on each curve
- OUTPUT Attachment Is Valid (Bool, default False) — Whether the stored attachment UV coordinate is valid
- OUTPUT Surface Normal (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Normal direction of the surface mesh at the attachment point
- INPUT Hair Curves (Geometry, default None) — Surface geometry of the curve attachment

## Nodes (15)
- **Group Output** [NodeGroupOutput]
- **Named Attribute.002** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_uv_coordinate
- **Evaluate on Domain** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=POINT}
- **Group Input** [NodeGroupInput]
- **Normal** [GeometryNodeInputNormal]
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Named Attribute.001** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_uv_coordinate
- **Switch** [GeometryNodeSwitch] {input_type=VECTOR}
- **Sample UV Surface** [GeometryNodeSampleUVSurface] {data_type=FLOAT_VECTOR}
- **Named Attribute** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_normal
- **Get Surface Geometry** [GeometryNodeGroup] -> grupo 'Get Attachment Surface'
- **Warning** [GeometryNodeWarning]
    inputs livres: Message = Missing hair surface geometry.
- **Boolean Math.002** [FunctionNodeBooleanMath] {operation=NOT}
- **Switch.001** [GeometryNodeSwitch] {input_type=GEOMETRY}

## Ligacoes (20)
- Capture Attribute.Geometry -> Sample UV Surface.Mesh
- Named Attribute.Exists -> Switch.Switch
- Evaluate on Domain.Value -> Group Output.Surface Normal
- Named Attribute.001.Attribute -> Sample UV Surface.Sample UV
- Sample UV Surface.Value -> Switch.False
- Named Attribute.Attribute -> Switch.True
- Normal.Normal -> Capture Attribute.Value
- Capture Attribute.Value -> Sample UV Surface.Value
- Switch.Output -> Evaluate on Domain.Value
- Named Attribute.002.Attribute -> Group Output.Attachment UV
- Sample UV Surface.Is Valid -> Group Output.Attachment Is Valid
- Get Surface Geometry.Surface UV Map -> Sample UV Surface.UV Map
- Group Input.Hair Curves -> Get Surface Geometry.Geometry
- Get Surface Geometry.Surface Geometry -> Capture Attribute.Geometry
- Boolean Math.002.Boolean -> Warning.Show
- Get Surface Geometry.Exists -> Boolean Math.002.Boolean
- Get Surface Geometry.Exists -> Group Output.Surface Exists
- Switch.001.Output -> Group Output.Surface Geometry
- Warning.Show -> Switch.001.Switch
- Get Surface Geometry.Surface Geometry -> Switch.001.False
