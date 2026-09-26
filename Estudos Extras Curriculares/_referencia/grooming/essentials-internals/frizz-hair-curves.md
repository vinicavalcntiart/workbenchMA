# Frizz Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- OUTPUT Offset Vector (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Vector by which each point was offset during deformation
- INPUT Geometry (Geometry, default None) — Input Geometry (May include other than curves)
- INPUT Cumulative Offset (Bool, default True) — Apply offset cumulatively (previous points affect points after)
- INPUT Factor (Float, default 1.0, min 0.0, max 1.0) — Factor to blend overall effect
- INPUT Distance (Float, default 0.01, min 0.0, max 3.4028234663852886e+38) — Overall distance factor for the deformation
- INPUT Shape (Float, default 0.5, min -1.0, max 1.0) — Shape of the influence along curves (0=constant, 0.5=linear)
- INPUT Seed (Int, default 0, min -10000, max 10000) — Random Seed for the operation
- INPUT Preserve Length (Bool, default False) — Preserve each curve's length during deformation

## Nodes (78)
- **Math.001** [ShaderNodeMath] {operation=MULTIPLY}
- **Group Input.001** [NodeGroupInput]
- **Group Input.006** [NodeGroupInput]
- **Capture Attribute.001** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Group Output** [NodeGroupOutput]
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Set Spline Resolution.001** [GeometryNodeSetSplineResolution]
- **Set Spline Type.001** [GeometryNodeCurveSplineType]
- **Switch.004** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: True = 12
- **Compare.003** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Position.002** [GeometryNodeInputPosition]
- **Vector Math.007** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Curve of Point** [GeometryNodeCurveOfPoint]
- **Field at Index** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Group.002** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Spline Parameter** [GeometryNodeSplineParameter]
- **Group** [GeometryNodeGroup] -> grupo '.shape_range'
    inputs livres: Min = 0.0; Max = 1.0; Base = 2.0
- **Group Input.007** [NodeGroupInput]
- **Vector Math.016** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.014** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.013** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.015** [ShaderNodeVectorMath] {operation=SCALE}
    inputs livres: Scale = 0.5
- **Group Input.005** [NodeGroupInput]
- **Switch** [GeometryNodeSwitch] {input_type=VECTOR}
- **Vector Math.012** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.017** [ShaderNodeVectorMath] {operation=SCALE}
- **Position.001** [GeometryNodeInputPosition]
- **Capture Attribute.003** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Group Input** [NodeGroupInput]
- **Separate Components** [GeometryNodeSeparateComponents]
- **Set Spline Type** [GeometryNodeCurveSplineType]
- **Spline Resolution** [GeometryNodeInputSplineResolution]
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Set Position** [GeometryNodeSetPosition]
- **Group Input.002** [NodeGroupInput]
- **Compare** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Accumulate Field** [GeometryNodeAccumulateField] {data_type=FLOAT_VECTOR, domain=POINT}
- **Separate XYZ** [ShaderNodeSeparateXYZ]
- **Curve Tangent** [GeometryNodeInputTangent]
- **Normal** [GeometryNodeInputNormal]
- **Vector Math.003** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.002** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.004** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.010** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.011** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math** [ShaderNodeVectorMath] {operation=CROSS_PRODUCT}
- **Random Value** [FunctionNodeRandomValue] {data_type=FLOAT_VECTOR}
    inputs livres: Min = (-1.0, -1.0, -1.0); Max = (1.0, 1.0, 1.0)
- **Switch.001** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Group.005** [GeometryNodeGroup] -> grupo 'Restore Curve Segment Length'
    inputs livres: Pin at Parameter = 0.0
- **Sample Index** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
    inputs livres: Index = 0
- **Accumulate Field.001** [GeometryNodeAccumulateField] {data_type=INT, domain=POINT}
- **Compare.002** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0
- **Boolean Math** [FunctionNodeBooleanMath] {operation=AND}
- **Group Input.008** [NodeGroupInput]
- **Group Input.003** [NodeGroupInput]
- **Hash Value** [FunctionNodeHashValue] {data_type=INT}
    inputs livres: Seed = 64785

## Ligacoes (93)
- Set Spline Type.Curve -> Set Position.Geometry
- Random Value.Value -> Separate XYZ.Vector
- Curve Tangent.Tangent -> Vector Math.Vector
- Normal.Normal -> Vector Math.Vector
- Curve Tangent.Tangent -> Vector Math.002.Vector
- Vector Math.Vector -> Vector Math.003.Vector
- Normal.Normal -> Vector Math.004.Vector
- Separate XYZ.X -> Vector Math.002.Scale
- Separate XYZ.Y -> Vector Math.003.Scale
- Separate XYZ.Z -> Vector Math.004.Scale
- Vector Math.002.Vector -> Vector Math.010.Vector
- Vector Math.003.Vector -> Vector Math.010.Vector
- Vector Math.010.Vector -> Vector Math.011.Vector
- Vector Math.004.Vector -> Vector Math.011.Vector
- Vector Math.011.Vector -> Vector Math.012.Vector
- Math.001.Value -> Vector Math.012.Scale
- Spline Parameter.Factor -> Group.Value
- Curve of Point.Curve Index -> Accumulate Field.Group ID
- Vector Math.012.Vector -> Accumulate Field.Value
- Group Input.002.Factor -> Compare.A
- Compare.Result -> Set Position.Selection
- Group.002.Root Index -> Field at Index.Index
- Vector Math.012.Vector -> Field at Index.Value
- Set Position.Geometry -> Group.005.Curves
- Group Input.008.Preserve Length -> Group.005.Factor
- Capture Attribute.003.Value -> Group.005.Reference Position
- Vector Math.017.Vector -> Set Position.Offset
- Field at Index.Value -> Vector Math.013.Vector
- Accumulate Field.Leading -> Vector Math.014.Vector
- Accumulate Field.Trailing -> Vector Math.014.Vector
- Vector Math.014.Vector -> Vector Math.013.Vector
- Vector Math.013.Vector -> Vector Math.015.Vector
- Compare.Result -> Boolean Math.Boolean
- Group Input.008.Preserve Length -> Boolean Math.Boolean
- Group Input.Geometry -> Separate Components.Geometry
- Separate Components.Mesh -> Join Geometry.Geometry
- Separate Components.Point Cloud -> Join Geometry.Geometry
- Separate Components.Volume -> Join Geometry.Geometry
- Separate Components.Instances -> Join Geometry.Geometry
- Vector Math.015.Vector -> Switch.True
- Group Input.005.Cumulative Offset -> Switch.Switch
- Boolean Math.Boolean -> Group.005.Selection
- Set Position.Geometry -> Switch.001.False
- Boolean Math.Boolean -> Accumulate Field.001.Value
- Capture Attribute.001.Geometry -> Join Geometry.Geometry
- Compare.002.Result -> Switch.001.Switch
- Set Position.Geometry -> Sample Index.Geometry
- Sample Index.Value -> Compare.002.A
- Accumulate Field.001.Total -> Sample Index.Value
- Join Geometry.Geometry -> Group Output.Geometry
- Vector Math.012.Vector -> Vector Math.016.Vector
- Field at Index.Value -> Vector Math.016.Vector
- Vector Math.016.Vector -> Switch.False
- Group.005.Curves -> Switch.001.True
- Group Input.001.Factor -> Math.001.Value
- Group Input.006.Distance -> Math.001.Value
- Switch.Output -> Vector Math.017.Vector
- Group.Value -> Vector Math.017.Scale
- Group Input.007.Shape -> Group.Shape
- Spline Resolution.Resolution -> Capture Attribute.002.Value
- Set Spline Type.001.Curve -> Set Spline Resolution.001.Curve
- Capture Attribute.002.Geometry -> Set Spline Type.Curve
- Switch.001.Output -> Set Spline Type.001.Curve
- Capture Attribute.002.Value -> Compare.003.A
- Compare.003.Result -> Switch.004.Switch
- Capture Attribute.002.Value -> Switch.004.False
- Switch.004.Output -> Set Spline Resolution.001.Resolution
- Position.001.Position -> Capture Attribute.003.Value
- Position.002.Position -> Vector Math.007.Vector
- Capture Attribute.003.Value -> Vector Math.007.Vector
- Vector Math.007.Vector -> Capture Attribute.001.Value
- Separate Components.Curve -> Capture Attribute.003.Geometry
- Capture Attribute.003.Geometry -> Capture Attribute.002.Geometry
- Set Spline Resolution.001.Curve -> Capture Attribute.001.Geometry
- Capture Attribute.001.Value -> Group Output.Offset Vector
- Separate Components.Grease Pencil -> Join Geometry.Geometry
- Hash Value.Hash -> Random Value.Seed
- Group Input.003.Seed -> Hash Value.Value
