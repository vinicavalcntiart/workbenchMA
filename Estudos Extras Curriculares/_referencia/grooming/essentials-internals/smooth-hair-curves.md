# Smooth Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- INPUT Geometry (Geometry, default None) — Input Geometry (May include other than curves)
- INPUT Amount (Float, default 1.0, min -1.0, max 1.0) — Amount of smoothing
- INPUT Shape (Float, default 0.0, min -1.0, max 1.0) — Shape of the influence along curves (0=constant, 0.5=linear)
- INPUT Iterations (Int, default 10, min 0, max 10000) — Amount of smoothing steps
- INPUT Weight (Float, default 0.5, min 0.0, max 1.0) — Weight used for smoothing
- INPUT Lock Tips (Bool, default False) — Lock tip position when smoothing
- INPUT Preserve Length (Bool, default True) — Preserve each curve's length during deformation

## Nodes (90)
- **Group Input** [NodeGroupInput]
- **Separate Components** [GeometryNodeSeparateComponents]
- **Capture Attribute.001** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Position.007** [GeometryNodeInputPosition]
- **Set Spline Resolution.001** [GeometryNodeSetSplineResolution]
- **Set Spline Type** [GeometryNodeCurveSplineType]
- **Compare.003** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Switch.004** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: True = 12
- **Group.005** [GeometryNodeGroup] -> grupo '.shape_range'
    inputs livres: Min = 0.0; Max = 1.0; Base = 2.7183
- **Boolean Math** [FunctionNodeBooleanMath] {operation=NOT}
- **Group Input.005** [NodeGroupInput]
- **Spline Parameter.002** [GeometryNodeSplineParameter]
- **Group.003** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Math** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.007** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.006** [ShaderNodeMath] {operation=MULTIPLY}
- **Group Input.016** [NodeGroupInput]
- **Spline Resolution** [GeometryNodeInputSplineResolution]
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Set Spline Type.001** [GeometryNodeCurveSplineType]
- **Group Output.001** [NodeGroupOutput]
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Switch** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Compare.008** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Accumulate Field** [GeometryNodeAccumulateField] {data_type=INT, domain=CURVE}
- **Group Input.007** [NodeGroupInput]
- **Group Input.008** [NodeGroupInput]
- **Boolean Math.001** [FunctionNodeBooleanMath] {operation=OR}
- **Group Input.003** [NodeGroupInput]
- **Compare** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Sample Index** [GeometryNodeSampleIndex] {data_type=INT, domain=CURVE}
    inputs livres: Index = 0
- **Compare.004** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Group.001** [GeometryNodeGroup] -> grupo 'Restore Curve Segment Length'
    inputs livres: Factor = 1.0; Pin at Parameter = 0.0
- **Boolean Math.004** [FunctionNodeBooleanMath] {operation=AND}
- **Group Input.012** [NodeGroupInput]
- **Set Position.005** [GeometryNodeSetPosition]
- **Vector Math.002** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.003** [ShaderNodeVectorMath] {operation=SCALE}
- **Group Input.001** [NodeGroupInput]
- **Position.008** [GeometryNodeInputPosition]
- **Blur Attribute.004** [GeometryNodeBlurAttribute] {data_type=FLOAT_VECTOR}
- **Group Input.002** [NodeGroupInput]
- **Position.006** [GeometryNodeInputPosition]
- **Vector Math.001** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Field at Index.001** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Field at Index.002** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Vector Math** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Group.002** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Boolean Math.005** [FunctionNodeBooleanMath] {operation=AND}
- **Compare.006** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0
- **Compare.007** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Group Input.006** [NodeGroupInput]
- **Group Input.015** [NodeGroupInput]
- **Group Input.013** [NodeGroupInput]
- **Boolean Math.002** [FunctionNodeBooleanMath] {operation=NOT}
- **Boolean Math.003** [FunctionNodeBooleanMath] {operation=AND}
- **Group** [GeometryNodeGroup] -> grupo 'Curve Tip'
- **Boolean Math.007** [FunctionNodeBooleanMath] {operation=AND}

## Ligacoes (95)
- Capture Attribute.001.Geometry -> Set Position.005.Geometry
- Position.006.Position -> Blur Attribute.004.Value
- Group Input.002.Iterations -> Blur Attribute.004.Iterations
- Math.006.Value -> Blur Attribute.004.Weight
- Set Position.005.Geometry -> Group.001.Curves
- Position.007.Position -> Capture Attribute.001.Value
- Capture Attribute.001.Value -> Group.001.Reference Position
- Boolean Math.007.Boolean -> Set Position.005.Selection
- Boolean Math.007.Boolean -> Math.Value
- Capture Attribute.001.Value -> Field at Index.001.Value
- Group.002.Root Index -> Field at Index.001.Index
- Blur Attribute.004.Value -> Field at Index.002.Value
- Group.002.Root Index -> Field at Index.002.Index
- Field at Index.001.Value -> Vector Math.Vector
- Field at Index.002.Value -> Vector Math.Vector
- Boolean Math.003.Boolean -> Boolean Math.002.Boolean
- Group Input.013.Lock Tips -> Boolean Math.003.Boolean
- Group Input.012.Preserve Length -> Boolean Math.004.Boolean
- Boolean Math.004.Boolean -> Group.001.Selection
- Compare.006.Result -> Boolean Math.005.Boolean
- Boolean Math.005.Boolean -> Boolean Math.004.Boolean
- Group Input.015.Weight -> Compare.006.A
- Blur Attribute.004.Value -> Vector Math.001.Vector
- Vector Math.Vector -> Vector Math.001.Vector
- Vector Math.001.Vector -> Vector Math.002.Vector
- Position.008.Position -> Vector Math.002.Vector
- Vector Math.003.Vector -> Set Position.005.Offset
- Vector Math.002.Vector -> Vector Math.003.Vector
- Group Input.003.Iterations -> Compare.A
- Separate Components.Mesh -> Join Geometry.Geometry
- Separate Components.Point Cloud -> Join Geometry.Geometry
- Separate Components.Volume -> Join Geometry.Geometry
- Separate Components.Instances -> Join Geometry.Geometry
- Set Spline Resolution.001.Curve -> Join Geometry.Geometry
- Separate Components.Curve -> Capture Attribute.002.Geometry
- Spline Resolution.Resolution -> Capture Attribute.002.Value
- Set Spline Type.Curve -> Set Spline Resolution.001.Curve
- Group Input.Geometry -> Separate Components.Geometry
- Boolean Math.005.Boolean -> Boolean Math.007.Boolean
- Group.001.Curves -> Set Spline Type.Curve
- Capture Attribute.002.Value -> Compare.003.A
- Compare.003.Result -> Switch.004.Switch
- Capture Attribute.002.Value -> Switch.004.False
- Switch.004.Output -> Set Spline Resolution.001.Resolution
- Set Spline Type.001.Curve -> Capture Attribute.001.Geometry
- Capture Attribute.002.Geometry -> Set Spline Type.001.Curve
- Compare.007.Result -> Boolean Math.005.Boolean
- Group Input.001.Amount -> Vector Math.003.Scale
- Group Input.006.Amount -> Compare.007.A
- Switch.Output -> Group Output.001.Geometry
- Spline Parameter.002.Factor -> Group.005.Value
- Group Input.005.Shape -> Group.005.Shape
- Math.Value -> Math.006.Value
- Math.007.Value -> Math.006.Value
- Group.Tip Selection -> Boolean Math.003.Boolean
- Group.005.Value -> Math.007.Value
- Group.003.Root Selection -> Boolean Math.Boolean
- Boolean Math.Boolean -> Math.007.Value
- Join Geometry.Geometry -> Switch.False
- Group Input.016.Weight -> Math.Value
- Compare.008.Result -> Accumulate Field.Value
- Accumulate Field.Total -> Sample Index.Value
- Sample Index.Value -> Compare.004.A
- Group Input.008.Geometry -> Sample Index.Geometry
- Group Input.007.Amount -> Compare.008.A
- Compare.004.Result -> Boolean Math.001.Boolean
- Boolean Math.001.Boolean -> Switch.Switch
- Compare.Result -> Boolean Math.001.Boolean
- Group Input.008.Geometry -> Switch.True
- Boolean Math.002.Boolean -> Boolean Math.007.Boolean
- Separate Components.Grease Pencil -> Join Geometry.Geometry
