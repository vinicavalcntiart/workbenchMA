# Straighten Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- INPUT Geometry (Geometry, default None) — Input Geometry (May include other than curves)
- INPUT Amount (Float, default 1.0, min -1.0, max 1.0) — Amount of straightening
- INPUT Shape (Float, default 0.0, min -1.0, max 1.0) — Shape of the influence along curves (0=constant, 0.5=linear)
- INPUT Preserve Length (Bool, default True) — Preserve each curve's length during deformation

## Nodes (67)
- **Group Output** [NodeGroupOutput]
- **Switch.001** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Compare.008** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Accumulate Field** [GeometryNodeAccumulateField] {data_type=INT, domain=CURVE}
- **Sample Index** [GeometryNodeSampleIndex] {data_type=INT, domain=CURVE}
    inputs livres: Index = 0
- **Compare.004** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Group Input.008** [NodeGroupInput]
- **Group Input.007** [NodeGroupInput]
- **Group.006** [GeometryNodeGroup] -> grupo 'Restore Curve Segment Length'
    inputs livres: Pin at Parameter = 0.0
- **Capture Attribute.001** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Position.002** [GeometryNodeInputPosition]
- **Separate Components** [GeometryNodeSeparateComponents]
- **Group Input.002** [NodeGroupInput]
- **Spline Resolution** [GeometryNodeInputSplineResolution]
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Set Spline Type.001** [GeometryNodeCurveSplineType]
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Boolean Math** [FunctionNodeBooleanMath] {operation=AND}
- **Compare.001** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0
- **Compare.002** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Group Input.006** [NodeGroupInput]
- **Group Input.005** [NodeGroupInput]
- **Set Position.001** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Mix.002** [ShaderNodeMix] {data_type=VECTOR, blend_type=MIX}
- **Position.001** [GeometryNodeInputPosition]
- **Mix.003** [ShaderNodeMix] {data_type=VECTOR, blend_type=MIX}
- **Group Input.004** [NodeGroupInput]
- **Spline Parameter.001** [GeometryNodeSplineParameter]
- **Group Input.003** [NodeGroupInput]
- **Boolean Math.003** [FunctionNodeBooleanMath] {operation=AND}
- **Group Input.009** [NodeGroupInput]
- **Spline Parameter.002** [GeometryNodeSplineParameter]
- **Group.003** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Group.004** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Group.005** [GeometryNodeGroup] -> grupo '.shape_range'
    inputs livres: Min = 0.0; Max = 1.0; Base = 2.7183
- **Compare.005** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Switch.004** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: True = 12
- **Set Spline Resolution.001** [GeometryNodeSetSplineResolution]
- **Set Spline Type** [GeometryNodeCurveSplineType]
- **Compare.006** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Compare** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Math** [ShaderNodeMath] {operation=MINIMUM}
    inputs livres: Value = 1.0
- **Math.001** [ShaderNodeMath] {operation=MULTIPLY}

## Ligacoes (72)
- Capture Attribute.001.Geometry -> Set Position.001.Geometry
- Group.003.Root Position -> Mix.002.A
- Group.004.Root Position -> Mix.002.B
- Spline Parameter.001.Factor -> Mix.002.Factor
- Mix.003.Result -> Set Position.001.Position
- Math.Value -> Mix.003.Factor
- Mix.002.Result -> Mix.003.B
- Position.001.Position -> Mix.003.A
- Math.Value -> Compare.A
- Group Input.006.Amount -> Compare.002.A
- Compare.002.Result -> Boolean Math.Boolean
- Group Input.005.Preserve Length -> Compare.001.A
- Compare.001.Result -> Boolean Math.Boolean
- Group Input.004.Amount -> Math.001.Value
- Math.001.Value -> Math.Value
- Group.005.Value -> Math.001.Value
- Group Input.003.Shape -> Group.005.Shape
- Spline Parameter.002.Factor -> Group.005.Value
- Set Position.001.Geometry -> Group.006.Curves
- Boolean Math.Boolean -> Group.006.Selection
- Capture Attribute.001.Value -> Group.006.Reference Position
- Group Input.005.Preserve Length -> Group.006.Factor
- Position.002.Position -> Capture Attribute.001.Value
- Compare.Result -> Boolean Math.003.Boolean
- Boolean Math.003.Boolean -> Set Position.001.Selection
- Compare.008.Result -> Accumulate Field.Value
- Accumulate Field.Total -> Sample Index.Value
- Sample Index.Value -> Compare.004.A
- Compare.004.Result -> Switch.001.Switch
- Group Input.007.Amount -> Compare.008.A
- Switch.001.Output -> Group Output.Geometry
- Separate Components.Mesh -> Join Geometry.Geometry
- Separate Components.Point Cloud -> Join Geometry.Geometry
- Separate Components.Volume -> Join Geometry.Geometry
- Separate Components.Instances -> Join Geometry.Geometry
- Set Spline Resolution.001.Curve -> Join Geometry.Geometry
- Join Geometry.Geometry -> Switch.001.False
- Group Input.002.Geometry -> Separate Components.Geometry
- Spline Resolution.Resolution -> Capture Attribute.002.Value
- Set Spline Type.Curve -> Set Spline Resolution.001.Curve
- Group.006.Curves -> Set Spline Type.Curve
- Capture Attribute.002.Value -> Compare.005.A
- Compare.005.Result -> Switch.004.Switch
- Capture Attribute.002.Value -> Switch.004.False
- Switch.004.Output -> Set Spline Resolution.001.Resolution
- Capture Attribute.002.Geometry -> Set Spline Type.001.Curve
- Separate Components.Curve -> Capture Attribute.002.Geometry
- Set Spline Type.001.Curve -> Capture Attribute.001.Geometry
- Group Input.009.Amount -> Compare.006.A
- Compare.006.Result -> Boolean Math.003.Boolean
- Group Input.008.Geometry -> Switch.001.True
- Group Input.008.Geometry -> Sample Index.Geometry
- Separate Components.Grease Pencil -> Join Geometry.Geometry
