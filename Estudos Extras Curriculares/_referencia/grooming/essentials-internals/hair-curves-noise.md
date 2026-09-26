# Hair Curves Noise

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- OUTPUT Offset Vector (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38)
- INPUT Geometry (Geometry, default None)
- INPUT Cumulative Offset (Bool, default True) — Apply offset cumulatively (previous points affect points after)
- INPUT Factor (Float, default 1.0, min 0.0, max 1.0) — Overall factor for the deformation
- INPUT Distance (Float, default 0.01, min 0.0, max 3.4028234663852886e+38) — Overall distance factor for the deformation
- INPUT Shape (Float, default 0.5, min -1.0, max 1.0) — Shape of amount along each curve (0=constant, 0.5=linear)
- INPUT Scale (Float, default 1.0, min -10000.0, max 10000.0) — Scale of the noise texture by root position
- INPUT Scale along Curve (Float, default 1.0, min 0.0, max 10000.0) — Scale of noise texture along each curve
- INPUT Offset per Curve (Float, default 0.0, min -10000.0, max 10000.0) — Random offset of noise texture for each curve
- INPUT Seed (Int, default 0, min -10000, max 10000) — Seed value for randomization
- INPUT Preserve Length (Bool, default False) — Preserve the length of the curves on a segment basis

## Nodes (100)
- **Separate Components** [GeometryNodeSeparateComponents]
- **Group Input** [NodeGroupInput]
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Group Output** [NodeGroupOutput]
- **Switch.001** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Boolean Math** [FunctionNodeBooleanMath] {operation=AND}
- **Group.005** [GeometryNodeGroup] -> grupo 'Restore Curve Segment Length'
    inputs livres: Pin at Parameter = 0.0
- **Group Input.008** [NodeGroupInput]
- **Sample Index** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
    inputs livres: Index = 0
- **Compare.002** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0
- **Accumulate Field.001** [GeometryNodeAccumulateField] {data_type=INT, domain=POINT}
- **Set Spline Resolution.001** [GeometryNodeSetSplineResolution]
- **Set Spline Type.001** [GeometryNodeCurveSplineType]
- **Compare.003** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Switch.004** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: True = 12
- **Capture Attribute.003** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Position.001** [GeometryNodeInputPosition]
- **Position.002** [GeometryNodeInputPosition]
- **Vector Math.007** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Capture Attribute.001** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Set Spline Type** [GeometryNodeCurveSplineType]
- **Spline Resolution** [GeometryNodeInputSplineResolution]
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Evaluate on Domain** [GeometryNodeFieldOnDomain] {data_type=FLOAT, domain=CURVE}
- **Vector Math.020** [ShaderNodeVectorMath] {operation=SCALE}
    inputs livres: Vector = (0.0, 0.0, 1.0)
- **Vector Math.019** [ShaderNodeVectorMath] {operation=ADD}
- **Group Input.006** [NodeGroupInput]
- **Group.001** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Vector Math.009** [ShaderNodeVectorMath] {operation=SCALE}
- **Spline Parameter.001** [GeometryNodeSplineParameter]
- **Group Input.007** [NodeGroupInput]
- **Math.001** [ShaderNodeMath] {operation=MULTIPLY}
- **Noise Texture.002** [ShaderNodeTexNoise]
    inputs livres: Scale = 5.0; Detail = 0.0; Roughness = 0.0; Lacunarity = 2.0; Distortion = 0.0
- **Vector Math.006** [ShaderNodeVectorMath] {operation=SCALE}
    inputs livres: Scale = 2.0
- **Vector Math.005** [ShaderNodeVectorMath] {operation=SUBTRACT}
    inputs livres: Vector = (0.5, 0.5, 0.5)
- **Vector Math** [ShaderNodeVectorMath] {operation=CROSS_PRODUCT}
- **Curve Tangent** [GeometryNodeInputTangent]
- **Vector Math.003** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.002** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.004** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.010** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.011** [ShaderNodeVectorMath] {operation=ADD}
- **Normal** [GeometryNodeInputNormal]
- **Separate XYZ** [ShaderNodeSeparateXYZ]
- **Group Input.001** [NodeGroupInput]
- **Group Input.010** [NodeGroupInput]
- **Math.004** [ShaderNodeMath] {operation=MULTIPLY}
- **Compare** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Group Input.002** [NodeGroupInput]
- **Curve of Point** [GeometryNodeCurveOfPoint]
- **Group Input.005** [NodeGroupInput]
- **Vector Math.012** [ShaderNodeVectorMath] {operation=SCALE}
- **Accumulate Field** [GeometryNodeAccumulateField] {data_type=FLOAT_VECTOR, domain=POINT}
- **Group.002** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Switch** [GeometryNodeSwitch] {input_type=VECTOR}
- **Vector Math.016** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.013** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.014** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.015** [ShaderNodeVectorMath] {operation=SCALE}
    inputs livres: Scale = 0.5
- **Group** [GeometryNodeGroup] -> grupo '.shape_range'
    inputs livres: Min = 0.0; Max = 1.0; Base = 2.0
- **Group Input.004** [NodeGroupInput]
- **Spline Parameter** [GeometryNodeSplineParameter]
- **Vector Math.017** [ShaderNodeVectorMath] {operation=SCALE}
- **Set Position** [GeometryNodeSetPosition]
- **Field at Index** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Random Value.001** [FunctionNodeRandomValue] {data_type=FLOAT}
    inputs livres: Min = -1.0; Max = 1.0
- **Group Input.009** [NodeGroupInput]
- **Random Value** [FunctionNodeRandomValue] {data_type=FLOAT_VECTOR}
    inputs livres: Min = (-1.0, -1.0, -1.0); Max = (1.0, 1.0, 1.0)
- **Math.002** [ShaderNodeMath] {operation=MULTIPLY}
- **Group Input.003** [NodeGroupInput]
- **Group.004** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Vector Math.018** [ShaderNodeVectorMath] {operation=SCALE}
    inputs livres: Scale = 100.0
- **Vector Math.008** [ShaderNodeVectorMath] {operation=ADD}
- **Math.003** [ShaderNodeMath] {operation=ADD}
- **Hash Value** [FunctionNodeHashValue] {data_type=INT}
    inputs livres: Seed = 368741

## Ligacoes (116)
- Set Spline Type.Curve -> Set Position.Geometry
- Vector Math.006.Vector -> Separate XYZ.Vector
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
- Math.004.Value -> Vector Math.012.Scale
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
- Vector Math.005.Vector -> Vector Math.006.Vector
- Vector Math.009.Vector -> Vector Math.008.Vector
- Group Input.006.Scale -> Vector Math.009.Scale
- Spline Parameter.001.Length -> Math.001.Value
- Group Input.007.Scale along Curve -> Math.001.Value
- Group.001.Root Position -> Vector Math.009.Vector
- Hash Value.Hash -> Random Value.001.Seed
- Random Value.001.Value -> Math.002.Value
- Math.001.Value -> Math.003.Value
- Group Input.009.Offset per Curve -> Math.002.Value
- Math.002.Value -> Evaluate on Domain.Value
- Evaluate on Domain.Value -> Math.003.Value
- Group Input.001.Factor -> Math.004.Value
- Group Input.010.Distance -> Math.004.Value
- Switch.Output -> Vector Math.017.Vector
- Group.Value -> Vector Math.017.Scale
- Capture Attribute.003.Geometry -> Capture Attribute.002.Geometry
- Spline Resolution.Resolution -> Capture Attribute.002.Value
- Set Spline Type.001.Curve -> Set Spline Resolution.001.Curve
- Vector Math.018.Vector -> Vector Math.008.Vector
- Random Value.Value -> Vector Math.018.Vector
- Vector Math.008.Vector -> Vector Math.019.Vector
- Math.003.Value -> Vector Math.020.Scale
- Vector Math.020.Vector -> Vector Math.019.Vector
- Capture Attribute.002.Geometry -> Set Spline Type.Curve
- Switch.001.Output -> Set Spline Type.001.Curve
- Vector Math.019.Vector -> Noise Texture.002.Vector
- Noise Texture.002.Color -> Vector Math.005.Vector
- Capture Attribute.002.Value -> Compare.003.A
- Compare.003.Result -> Switch.004.Switch
- Capture Attribute.002.Value -> Switch.004.False
- Switch.004.Output -> Set Spline Resolution.001.Resolution
- Group Input.003.Seed -> Random Value.ID
- Set Spline Resolution.001.Curve -> Capture Attribute.001.Geometry
- Separate Components.Curve -> Capture Attribute.003.Geometry
- Position.001.Position -> Capture Attribute.003.Value
- Position.002.Position -> Vector Math.007.Vector
- Capture Attribute.003.Value -> Vector Math.007.Vector
- Vector Math.007.Vector -> Capture Attribute.001.Value
- Capture Attribute.001.Value -> Group Output.Offset Vector
- Group Input.004.Shape -> Group.Shape
- Hash Value.Hash -> Random Value.Seed
- Group.004.Curve ID -> Random Value.001.ID
- Separate Components.Grease Pencil -> Join Geometry.Geometry
- Group Input.003.Seed -> Hash Value.Value
