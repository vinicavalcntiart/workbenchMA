# Curve Info

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Curve Index (Int, default 0, min -2147483648, max 2147483647) — Index of each Curve
- OUTPUT Curve ID (Int, default 0, min -2147483648, max 2147483647) — ID of each curve
- OUTPUT Length (Float, default 0.0, min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Length of each curve
- OUTPUT Direction (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Direction from root to tip of each curve
- OUTPUT Random (Float, default 0.0, min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Random vector for each curve
- OUTPUT Surface UV (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Attachment surface UV coordinates of each curve

## Nodes (19)
- **Group Output** [NodeGroupOutput]
- **Named Attribute** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_uv_coordinate
- **Group.002** [GeometryNodeGroup] -> grupo 'Curve Tip'
- **Group.001** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Evaluate at Index** [GeometryNodeFieldAtIndex] {data_type=FLOAT, domain=POINT}
- **Evaluate on Domain.001** [GeometryNodeFieldOnDomain] {data_type=FLOAT, domain=CURVE}
- **Group.003** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Random Value.002** [FunctionNodeRandomValue] {data_type=FLOAT}
    inputs livres: Min = 0.0; Max = 1.0; Seed = 0
- **Vector Math** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.001** [ShaderNodeVectorMath] {operation=NORMALIZE}
- **Evaluate on Domain** [GeometryNodeFieldOnDomain] {data_type=INT, domain=CURVE}
- **Index.001** [GeometryNodeInputIndex]
- **Spline Length** [GeometryNodeSplineLength]
- **Evaluate at Index.001** [GeometryNodeFieldAtIndex] {data_type=INT, domain=POINT}
- **Evaluate on Domain.002** [GeometryNodeFieldOnDomain] {data_type=INT, domain=CURVE}
- **Group** [GeometryNodeGroup] -> grupo 'Curve Root'
- **ID** [GeometryNodeInputID]

## Ligacoes (18)
- Index.001.Index -> Evaluate on Domain.Value
- Evaluate on Domain.Value -> Group Output.Curve Index
- Named Attribute.Attribute -> Group Output.Surface UV
- Evaluate at Index.001.Value -> Evaluate on Domain.002.Value
- Group.Root Index -> Evaluate at Index.001.Index
- Evaluate on Domain.002.Value -> Group Output.Curve ID
- ID.ID -> Evaluate at Index.001.Value
- Spline Length.Length -> Group Output.Length
- Group.002.Tip Position -> Vector Math.Vector
- Group.001.Root Position -> Vector Math.Vector
- Vector Math.001.Vector -> Group Output.Direction
- Vector Math.Vector -> Vector Math.001.Vector
- Evaluate on Domain.002.Value -> Random Value.002.ID
- Evaluate at Index.Value -> Evaluate on Domain.001.Value
- Evaluate on Domain.001.Value -> Group Output.Random
- Random Value.002.Value -> Evaluate at Index.Value
- Group.003.Root Index -> Evaluate at Index.Index
