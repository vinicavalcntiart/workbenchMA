# Hair Attachment Info

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Attachment UV (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Surface attachment UV coordinates stored on each curve
- OUTPUT Attachment is Valid (Bool, default False) — Whether the stored attachment UV coordinate is valid
- OUTPUT Surface Normal (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Normal direction of the surface mesh at the attachment point
- INPUT Surface Geometry (Geometry, default None) — Surface geometry of the curve attachment
- INPUT Surface UV Map (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Surface UV map used for attachment

## Nodes (12)
- **Group Output** [NodeGroupOutput]
- **Named Attribute.002** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_uv_coordinate
- **Evaluate on Domain** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=POINT}
- **Group Input.001** [NodeGroupInput]
- **Group Input** [NodeGroupInput]
- **Normal** [GeometryNodeInputNormal]
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Named Attribute.001** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_uv_coordinate
- **Switch** [GeometryNodeSwitch] {input_type=VECTOR}
- **Sample UV Surface** [GeometryNodeSampleUVSurface] {data_type=FLOAT_VECTOR}
- **Named Attribute** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_normal

## Ligacoes (13)
- Capture Attribute.Geometry -> Sample UV Surface.Mesh
- Group Input.001.Surface UV Map -> Sample UV Surface.UV Map
- Named Attribute.Exists -> Switch.Switch
- Evaluate on Domain.Value -> Group Output.Surface Normal
- Named Attribute.001.Attribute -> Sample UV Surface.Sample UV
- Sample UV Surface.Value -> Switch.False
- Named Attribute.Attribute -> Switch.True
- Group Input.Surface Geometry -> Capture Attribute.Geometry
- Normal.Normal -> Capture Attribute.Value
- Capture Attribute.Value -> Sample UV Surface.Value
- Switch.Output -> Evaluate on Domain.Value
- Named Attribute.002.Attribute -> Group Output.Attachment UV
- Sample UV Surface.Is Valid -> Group Output.Attachment is Valid
