# Curve Segment

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Segment Length (Float, default 0.0, min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Distance to previous point on curve
- OUTPUT Segment Direction (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Direction from previous neighboring point on segment
- OUTPUT Neighbor Index (Int, default 0, min -2147483648, max 2147483647) — Index of previous neighboring point on segment

## Nodes (20)
- **Vector Math.009** [ShaderNodeVectorMath] {operation=NORMALIZE}
- **Field at Index.001** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Vector Math.008** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Interpolate Domain.002** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=POINT}
- **Group Output** [NodeGroupOutput]
- **Vector Math.007** [ShaderNodeVectorMath] {operation=LENGTH}
- **Interpolate Domain.003** [GeometryNodeFieldOnDomain] {data_type=INT, domain=POINT}
- **Switch.004** [GeometryNodeSwitch] {input_type=VECTOR}
    inputs livres: False = (0.0, 0.0, 0.0)
- **Switch.003** [GeometryNodeSwitch] {input_type=FLOAT}
    inputs livres: False = 0.0
- **Boolean** [FunctionNodeInputBool]
- **Interpolate Domain** [GeometryNodeFieldOnDomain] {data_type=BOOLEAN, domain=CURVE}
- **Switch.005** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: False = 0
- **Index.002** [GeometryNodeInputIndex]
- **Switch.001** [GeometryNodeSwitch] {input_type=INT}
- **Offset Point in Curve** [GeometryNodeOffsetPointInCurve]
    inputs livres: Offset = -1
- **Position.002** [GeometryNodeInputPosition]

## Ligacoes (25)
- Interpolate Domain.002.Value -> Vector Math.007.Vector
- Switch.001.Output -> Field at Index.001.Index
- Vector Math.008.Vector -> Interpolate Domain.002.Value
- Position.002.Position -> Vector Math.008.Vector
- Interpolate Domain.002.Value -> Vector Math.009.Vector
- Position.002.Position -> Field at Index.001.Value
- Field at Index.001.Value -> Vector Math.008.Vector
- Switch.004.Output -> Group Output.Segment Direction
- Switch.005.Output -> Group Output.Neighbor Index
- Boolean.Boolean -> Interpolate Domain.Value
- Switch.001.Output -> Interpolate Domain.003.Value
- Vector Math.007.Value -> Switch.003.True
- Interpolate Domain.Value -> Switch.003.Switch
- Switch.003.Output -> Group Output.Segment Length
- Vector Math.009.Vector -> Switch.004.True
- Interpolate Domain.Value -> Switch.004.Switch
- Interpolate Domain.003.Value -> Switch.005.True
- Interpolate Domain.Value -> Switch.005.Switch
- Offset Point in Curve.Is Valid Offset -> Switch.001.Switch
- Offset Point in Curve.Point Index -> Switch.001.True
- Index.002.Index -> Switch.001.False
