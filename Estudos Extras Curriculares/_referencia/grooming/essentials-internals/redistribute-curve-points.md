# Redistribute Curve Points

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Curves (Geometry, default None)
- INPUT Curves (Geometry, default None)
- INPUT Factor (Float, default 1.0, min 0.0, max 1.0) — Factor to blend overall effect
- INPUT Feature Awareness (Bool, default False) — Use simple feature awareness to keep feature definition

## Nodes (36)
- **Group Input** [NodeGroupInput]
- **Blur Attribute** [GeometryNodeBlurAttribute] {data_type=FLOAT}
    inputs livres: Iterations = 10
- **Spline Parameter.001** [GeometryNodeSplineParameter]
- **Spline Parameter** [GeometryNodeSplineParameter]
- **Group Input.002** [NodeGroupInput]
- **Group Input.001** [NodeGroupInput]
- **Set Position.002** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Group Output** [NodeGroupOutput]
- **Sample Curve.001** [GeometryNodeSampleCurve] {data_type=FLOAT_VECTOR, mode=FACTOR}
- **Group.001** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Mix.001** [ShaderNodeMix] {data_type=FLOAT, blend_type=MIX}
- **Switch** [GeometryNodeSwitch] {input_type=FLOAT}
- **Spline Parameter.002** [GeometryNodeSplineParameter]
- **Math.002** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 1.0
- **Group.002** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Points of Curve** [GeometryNodePointsOfCurve]
    inputs livres: Sort Index = 0
- **Math.001** [ShaderNodeMath] {operation=DIVIDE}
- **Endpoint Selection.001** [GeometryNodeCurveEndpointSelection]
    inputs livres: Start Size = 1; End Size = 1
- **Group** [GeometryNodeGroup] -> grupo 'Curve Segment'
- **Curve Tangent** [GeometryNodeInputTangent]
- **Boolean Math.001** [FunctionNodeBooleanMath] {operation=NOT}
- **Math.003** [ShaderNodeMath] {operation=MULTIPLY}
- **Map Range** [ShaderNodeMapRange] {data_type=FLOAT}
    inputs livres: From Min = 0.0; From Max = 1.0; To Min = 0.0; To Max = 1.0
- **Math** [ShaderNodeMath] {operation=ABSOLUTE}
- **Vector Math** [ShaderNodeVectorMath] {operation=DOT_PRODUCT}
- **Endpoint Selection** [GeometryNodeCurveEndpointSelection]
    inputs livres: Start Size = 1; End Size = 1
- **Group Input.003** [NodeGroupInput]
- **Boolean Math** [FunctionNodeBooleanMath] {operation=NOT}
- **Boolean Math.002** [FunctionNodeBooleanMath] {operation=AND}
- **Compare** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0

## Ligacoes (31)
- Group Input.Curves -> Sample Curve.001.Curves
- Group Input.Curves -> Set Position.002.Geometry
- Math.002.Value -> Math.001.Value
- Spline Parameter.002.Index -> Math.001.Value
- Points of Curve.Total -> Math.002.Value
- Sample Curve.001.Position -> Set Position.002.Position
- Set Position.002.Geometry -> Group Output.Curves
- Endpoint Selection.Selection -> Boolean Math.Boolean
- Spline Parameter.001.Factor -> Blur Attribute.Value
- Endpoint Selection.001.Selection -> Boolean Math.001.Boolean
- Math.003.Value -> Blur Attribute.Weight
- Mix.001.Result -> Sample Curve.001.Factor
- Curve Tangent.Tangent -> Vector Math.Vector
- Group.Segment Direction -> Vector Math.Vector
- Vector Math.Value -> Math.Value
- Math.Value -> Map Range.Value
- Boolean Math.001.Boolean -> Math.003.Value
- Map Range.Result -> Math.003.Value
- Group Input.002.Factor -> Mix.001.Factor
- Spline Parameter.Factor -> Mix.001.A
- Switch.Output -> Mix.001.B
- Math.001.Value -> Switch.False
- Group Input.001.Feature Awareness -> Switch.Switch
- Blur Attribute.Value -> Switch.True
- Boolean Math.Boolean -> Boolean Math.002.Boolean
- Boolean Math.002.Boolean -> Set Position.002.Selection
- Compare.Result -> Boolean Math.002.Boolean
- Group Input.003.Factor -> Compare.A
- Group.001.Curve Index -> Sample Curve.001.Curve Index
- Group.002.Curve Index -> Points of Curve.Curve Index
