# Rest Surface

Fonte: Essentials asset library do Blender 5.2.2 LTS (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Rest Surface (Geometry, default None)
- OUTPUT Exists (Bool, default False)
- INPUT Surface (Geometry, default None)

## Nodes (9)
- **Group.003** [GeometryNodeGroup] -> grupo 'Get Rest Geometry'
- **Group Output** [NodeGroupOutput]
- **Group Input** [NodeGroupInput]
- **Switch.011** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Warning.001** [GeometryNodeWarning]
    inputs livres: Message = Missing rest geometry on surface. Use 'Capture Rest Geometry' or enable 'Add Rest Position'.
- **Boolean Math.001** [FunctionNodeBooleanMath] {operation=NOT}
- **Boolean Math** [FunctionNodeBooleanMath] {operation=OR}

## Ligacoes (12)
- Group Input.Surface -> Group.003.Geometry
- Group.003.Rest Geometry -> Switch.011.False
- Boolean Math.001.Boolean -> Warning.001.Show
- Warning.001.Show -> Switch.011.Switch
- Switch.011.Output -> Group Output.Rest Surface
- Group.003.Rest Geometry Found -> Group Output.Exists
- Group.003.Rest Geometry Found -> Boolean Math.Boolean
- Group.003.Rest Attribute Found -> Boolean Math.Boolean
- Boolean Math.Boolean -> Boolean Math.001.Boolean
- Group Input.Surface -> Switch.011.True
