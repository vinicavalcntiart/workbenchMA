# Get Rest Geometry

Fonte: Essentials asset library do Blender 5.2.2 LTS (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Rest Geometry (Geometry, default None)
- OUTPUT Rest Geometry Found (Bool, default False)
- OUTPUT Rest Attribute Found (Bool, default False)
- INPUT Geometry (Geometry, default None)

## Nodes (13)
- **Get Bundle Item.001** [NodeGetBundleItem]
    inputs livres: Path = rest_geometry; Remove = True
- **Get Geometry Bundle.001** [GeometryNodeGetGeometryBundle]
    inputs livres: Remove = True
- **Warning** [GeometryNodeWarning]
    inputs livres: Message = Missing rest geometry. Use 'Capture Rest Geometry'.
- **Switch.011** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Named Attribute.006** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = rest_position
- **Set Position.002** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Boolean Math.001** [FunctionNodeBooleanMath] {operation=NOT}
- **Group Output** [NodeGroupOutput]
- **Group Input** [NodeGroupInput]
- **Accumulate Field** [GeometryNodeAccumulateField] {data_type=INT, domain=POINT}
- **Sample Index** [GeometryNodeSampleIndex] {data_type=BOOLEAN, domain=POINT}
    inputs livres: Index = 0

## Ligacoes (18)
- Get Geometry Bundle.001.Bundle -> Get Bundle Item.001.Bundle
- Boolean Math.001.Boolean -> Warning.Show
- Warning.Show -> Switch.011.Switch
- Named Attribute.006.Attribute -> Set Position.002.Position
- Named Attribute.006.Exists -> Set Position.002.Selection
- Set Position.002.Geometry -> Switch.011.True
- Get Bundle Item.001.Exists -> Boolean Math.001.Boolean
- Get Bundle Item.001.Item -> Switch.011.False
- Switch.011.Output -> Group Output.Rest Geometry
- Group Input.Geometry -> Get Geometry Bundle.001.Geometry
- Get Geometry Bundle.001.Geometry -> Set Position.002.Geometry
- Get Bundle Item.001.Exists -> Group Output.Rest Geometry Found
- Get Geometry Bundle.001.Geometry -> Sample Index.Geometry
- Accumulate Field.Total -> Sample Index.Value
- Named Attribute.006.Exists -> Accumulate Field.Value
- Sample Index.Value -> Group Output.Rest Attribute Found
