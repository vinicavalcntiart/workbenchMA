# Curve Tip

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Tip Selection (Bool, default False) — Boolean selection of curve tip points
- OUTPUT Tip Position (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Position of the tip point of a curve
- OUTPUT Tip Direction (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Direction of the tip segment of a curve
- OUTPUT Tip Index (Int, default 0, min -2147483648, max 2147483647) — Index of the tip point of a curve

## Nodes (10)
- **Position.002** [GeometryNodeInputPosition]
- **Interpolate Domain** [GeometryNodeFieldOnDomain] {data_type=INT, domain=CURVE}
- **Interpolate Domain.001** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Field at Index.003** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Curve Tangent** [GeometryNodeInputTangent]
- **Endpoint Selection** [GeometryNodeCurveEndpointSelection]
    inputs livres: Start Size = 0; End Size = 1
- **Field at Index.004** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Interpolate Domain.002** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Group Output** [NodeGroupOutput]
- **Points of Curve** [GeometryNodePointsOfCurve]
    inputs livres: Sort Index = -1

## Ligacoes (11)
- Position.002.Position -> Field at Index.003.Value
- Interpolate Domain.Value -> Field at Index.003.Index
- Points of Curve.Point Index -> Interpolate Domain.Value
- Interpolate Domain.001.Value -> Group Output.Tip Position
- Interpolate Domain.Value -> Group Output.Tip Index
- Endpoint Selection.Selection -> Group Output.Tip Selection
- Field at Index.003.Value -> Interpolate Domain.001.Value
- Interpolate Domain.002.Value -> Group Output.Tip Direction
- Curve Tangent.Tangent -> Field at Index.004.Value
- Interpolate Domain.Value -> Field at Index.004.Index
- Field at Index.004.Value -> Interpolate Domain.002.Value
