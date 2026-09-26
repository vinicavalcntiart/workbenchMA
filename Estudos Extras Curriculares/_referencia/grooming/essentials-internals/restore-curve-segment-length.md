# Restore Curve Segment Length

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Curves (Geometry, default None)
- INPUT Curves (Geometry, default None)
- INPUT Selection (Bool, default True) — Only affect selected elements
- INPUT Factor (Float, default 1.0, min 0.0, max 1.0) — Factor to blend overall effect
- INPUT Reference Position (Vector, default (8.1465, 4.9699, 9.8745), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Reference position before deformation
- INPUT Pin at Parameter (Float, default 0.0, min 0.0, max 1.0) — Pin each curve at a certain point for the operation

## Nodes (53)
- **Group Input.006** [NodeGroupInput]
- **Index** [GeometryNodeInputIndex]
- **Sample Curve.001** [GeometryNodeSampleCurve] {data_type=FLOAT_VECTOR, mode=FACTOR}
- **Group Input.003** [NodeGroupInput]
- **Vector Math.006** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Interpolate Domain** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Group Input.005** [NodeGroupInput]
- **Boolean Math.002** [FunctionNodeBooleanMath] {operation=AND}
- **Field at Index.002** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Vector Math.004** [ShaderNodeVectorMath] {operation=DISTANCE}
- **Accumulate Field** [GeometryNodeAccumulateField] {data_type=FLOAT_VECTOR, domain=POINT}
- **Curve of Point** [GeometryNodeCurveOfPoint]
- **Vector Math** [ShaderNodeVectorMath] {operation=SCALE}
- **Index.001** [GeometryNodeInputIndex]
- **Curve of Point.001** [GeometryNodeCurveOfPoint]
- **Switch** [GeometryNodeSwitch] {input_type=INT}
- **Math** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 1.0
- **Compare** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Set Position.001** [GeometryNodeSetPosition]
- **Boolean Math** [FunctionNodeBooleanMath] {operation=AND}
- **Compare.002** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0
- **Group Input.002** [NodeGroupInput]
- **Switch.001** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Group Output** [NodeGroupOutput]
- **Attribute Statistic** [GeometryNodeAttributeStatistic] {data_type=FLOAT, domain=CURVE}
- **Group** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Position.001** [GeometryNodeInputPosition]
- **Named Attribute** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = rest_position
- **Switch.003** [GeometryNodeSwitch] {input_type=VECTOR}
- **Switch.002** [GeometryNodeSwitch] {input_type=VECTOR}
- **Compare.004** [FunctionNodeCompare] {operation=EQUAL, data_type=VECTOR, mode=ELEMENT}
    inputs livres: B = (8.1465, 4.9699, 9.8745); Epsilon = 0.0
- **Group Input** [NodeGroupInput]
- **Set Position.002** [GeometryNodeSetPosition]
- **Group Input.001** [NodeGroupInput]
- **Mix** [ShaderNodeMix] {data_type=FLOAT, blend_type=MIX}
- **Group.001** [GeometryNodeGroup] -> grupo 'Curve Segment'
- **Compare.003** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Compare.005** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0

## Ligacoes (62)
- Group Input.Curves -> Set Position.001.Geometry
- Curve of Point.Curve Index -> Accumulate Field.Group ID
- Field at Index.002.Value -> Vector Math.004.Vector
- Switch.002.Output -> Vector Math.004.Vector
- Switch.002.Output -> Field at Index.002.Value
- Index.001.Index -> Math.Value
- Switch.Output -> Field at Index.002.Index
- Vector Math.Vector -> Accumulate Field.Value
- Curve of Point.001.Index in Curve -> Compare.A
- Math.Value -> Switch.False
- Compare.Result -> Switch.Switch
- Index.001.Index -> Switch.True
- Group Input.Reference Position -> Switch.002.False
- Group.Root Position -> Set Position.001.Position
- Vector Math.004.Value -> Mix.B
- Mix.Result -> Vector Math.Scale
- Group Input.001.Factor -> Mix.Factor
- Group Input.002.Factor -> Compare.002.A
- Accumulate Field.Leading -> Set Position.001.Offset
- Compare.002.Result -> Boolean Math.Boolean
- Group Input.002.Selection -> Boolean Math.Boolean
- Set Position.001.Geometry -> Sample Curve.001.Curves
- Sample Curve.001.Position -> Vector Math.006.Vector
- Sample Curve.001.Value -> Vector Math.006.Vector
- Set Position.001.Geometry -> Set Position.002.Geometry
- Interpolate Domain.Value -> Set Position.002.Offset
- Index.Index -> Sample Curve.001.Curve Index
- Group Input.005.Selection -> Boolean Math.002.Boolean
- Compare.003.Result -> Boolean Math.002.Boolean
- Group Input.003.Pin at Parameter -> Sample Curve.001.Factor
- Group Input.006.Pin at Parameter -> Compare.003.A
- Group Input.Reference Position -> Compare.004.A
- Compare.004.Result -> Switch.002.Switch
- Named Attribute.Attribute -> Switch.003.True
- Named Attribute.Exists -> Switch.003.Switch
- Position.001.Position -> Switch.003.False
- Switch.003.Output -> Switch.002.True
- Switch.002.Output -> Sample Curve.001.Value
- Group.001.Segment Length -> Mix.A
- Group.001.Segment Direction -> Vector Math.Vector
- Vector Math.006.Vector -> Interpolate Domain.Value
- Boolean Math.002.Boolean -> Attribute Statistic.Attribute
- Attribute Statistic.Max -> Compare.005.A
- Set Position.002.Geometry -> Switch.001.True
- Set Position.001.Geometry -> Switch.001.False
- Boolean Math.002.Boolean -> Set Position.002.Selection
- Compare.005.Result -> Switch.001.Switch
- Set Position.001.Geometry -> Attribute Statistic.Geometry
- Boolean Math.Boolean -> Set Position.001.Selection
- Switch.001.Output -> Group Output.Curves
