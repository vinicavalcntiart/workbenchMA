# Braid Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- OUTPUT Flare Parameter (Float, default 0.0, min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Parameter from 0 to 1 along the flare
- OUTPUT Strand Index (Int, default 0, min -2147483648, max 2147483647) — Index of the strand within a braid that each curve belongs to
- INPUT Geometry (Geometry, default None)
- INPUT Factor (Float, default 1.0, min 0.0, max 1.0) — Factor to blend overall effect
- INPUT Subdivision (Int, default 1, min 0, max 6) — Subdivision level applied before deformation
- INPUT Braid Start (Float, default 0.1, min 0.0, max 1.0) — Percentage along each curve to blend deformation from the root
- INPUT Radius (Float, default 0.1, min 0.0, max 3.4028234663852886e+38) — Overall radius of the braids
- INPUT Shape (Float, default 0.5, min -1.0, max 1.0) — Shape of the braid radius along each curve
- INPUT Frequency (Float, default 1.0, min 0.0, max 10000.0) — Frequency factor of the braids
- [painel] Shape Parameters
- INPUT Factor Min (Float, default 0.0, min 0.0, max 10000.0) — Factor of the minimum radius of the braids
- INPUT Factor Max (Float, default 1.0, min 0.0, max 10000.0) — Factor of the maximum radius of the braids
- INPUT Thickness (Float, default 1.0, min -10000.0, max 10000.0) — Thickness of each strand of hair
- INPUT Thickness Shape (Float, default 0.5, min -10000.0, max 10000.0) — Shape adjustment of the strand thickness for the braids
- INPUT Shape Asymmetry (Float, default 0.0, min -10000.0, max 10000.0) — Asymmetry of the shape adjustment of the strand thickness
- INPUT Flare Length (Float, default 0.0, min 0.0, max 3.4028234663852886e+38) — Length of the flare at the end of the braid
- INPUT Flare Opening (Float, default 0.0, min 0.0, max 3.4028234663852886e+38) — Opening radius of the flare at the tip of the braid
- [painel] Hair Tie
- INPUT Hair Tie (Bool, default False)
- INPUT Hair Tie Input Type (Menu, default Object) — Select the input type for the hair tie geometry.
- INPUT Hair Tie (Geometry, default None) — Geometry used for the hair tie instance (priority)
- INPUT Hair Tie (Object, default None) — Object used for the hair tie instance
- INPUT Hair Tie Scale (Float, default 1.0, min -10000.0, max 10000.0) — Scale of the hair tie instance
- [painel] Guide Map
- OUTPUT Guide Index (Int, default 0, min -2147483648, max 2147483647) — Guide index map that was used for the operation
- INPUT Guide Index (Int, default -987654, min -2147483648, max 2147483647) — Guide index map to be used. This input has priority
- INPUT Guide Distance (Float, default 0.1, min 0.0, max 3.4028234663852886e+38) — Minimum distance between two guides for new guide map
- INPUT Guide Mask (Float, default 1.0, min 0.0, max 1.0) — Mask for which curves are eligible to be selected as guides
- INPUT Existing Guide Map (Bool, default True) — Use the existing guide map attribute if available

## Nodes (262)
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Separate Components** [GeometryNodeSeparateComponents]
- **Group Input** [NodeGroupInput]
- **Spline Resolution** [GeometryNodeInputSplineResolution]
- **Capture Attribute.003** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Set Spline Type.002** [GeometryNodeCurveSplineType]
- **Set Spline Resolution.001** [GeometryNodeSetSplineResolution]
- **Set Spline Type.001** [GeometryNodeCurveSplineType]
- **Compare.004** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Switch.006** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: True = 12
- **Instance on Points** [GeometryNodeInstanceOnPoints]
    inputs livres: Pick Instance = False
- **Group Input.016** [NodeGroupInput]
- **Sample Curve.002** [GeometryNodeSampleCurve] {data_type=FLOAT, mode=LENGTH}
- **Set Position** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Curve to Points** [GeometryNodeCurveToPoints] {mode=COUNT}
    inputs livres: Count = 1
- **Vector Math** [ShaderNodeVectorMath] {operation=SCALE}
    inputs livres: Scale = -1.0
- **Geometry to Instance** [GeometryNodeGeometryToInstance]
- **Object Info** [GeometryNodeObjectInfo] {transform_space=ORIGINAL}
    inputs livres: As Instance = True
- **Math.003** [ShaderNodeMath] {operation=SUBTRACT}
- **Group.003** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Group Input.014** [NodeGroupInput]
- **Group Input.015** [NodeGroupInput]
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Index** [GeometryNodeInputIndex]
- **Set Position.001** [GeometryNodeSetPosition]
- **Vector Math.010** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.008** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.006** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.007** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.011** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Position** [GeometryNodeInputPosition]
- **Vector Math.012** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.005** [ShaderNodeVectorMath] {operation=CROSS_PRODUCT}
- **Separate XYZ.001** [ShaderNodeSeparateXYZ]
- **Math** [ShaderNodeMath] {operation=POWER}
    inputs livres: Value = 0.5
- **Map Range** [ShaderNodeMapRange] {data_type=FLOAT}
    inputs livres: From Min = -0.0; To Min = 0.0; To Max = 1.0
- **Spline Parameter.003** [GeometryNodeSplineParameter]
- **Group Input.006** [NodeGroupInput]
- **Sample Curve** [GeometryNodeSampleCurve] {data_type=FLOAT, mode=LENGTH}
- **Spline Parameter.002** [GeometryNodeSplineParameter]
- **Group Input.002** [NodeGroupInput]
- **Vector Math.009** [ShaderNodeVectorMath] {operation=SCALE}
- **Math.011** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 1.0
- **Math.010** [ShaderNodeMath] {operation=POWER}
    inputs livres: Value = 2.0
- **Group Input.005** [NodeGroupInput]
- **Subdivide Curve.002** [GeometryNodeSubdivideCurve]
- **Vector Math.013** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.018** [ShaderNodeVectorMath] {operation=SCALE}
- **Switch.008** [GeometryNodeSwitch] {input_type=VECTOR}
    inputs livres: True = (0.0, 0.0, 0.0)
- **Switch.007** [GeometryNodeSwitch] {input_type=FLOAT}
    inputs livres: False = 0.0
- **Math.055** [ShaderNodeMath] {operation=DIVIDE}
    inputs livres: Value = 3.1416
- **Math.061** [ShaderNodeMath] {operation=ADD}
- **Math.054** [ShaderNodeMath] {operation=MULTIPLY}
- **Group Input.013** [NodeGroupInput]
- **Map Range.001** [ShaderNodeMapRange] {data_type=FLOAT}
    inputs livres: From Min = 0.0; From Max = 1.0
- **Group Input.020** [NodeGroupInput]
- **Math.064** [ShaderNodeMath] {operation=ADD}
    inputs livres: Value = 1.0
- **Math.063** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 1.0
- **Group Input.012** [NodeGroupInput]
- **Math.056** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.062** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.009** [ShaderNodeMath] {operation=MULTIPLY}
- **Evaluate on Domain.001** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Math.052** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = 6.2832
- **Combine XYZ.002** [ShaderNodeCombineXYZ]
    inputs livres: Y = 0.0; Z = 0.0
- **Math.053** [ShaderNodeMath] {operation=ARCCOSINE}
- **Vector Rotate** [ShaderNodeVectorRotate]
    inputs livres: Center = (0.0, 0.0, 0.0)
- **Separate XYZ.002** [ShaderNodeSeparateXYZ]
- **Random Value** [FunctionNodeRandomValue] {data_type=FLOAT_VECTOR}
    inputs livres: Min = (0.0, 0.0, 0.0); Max = (1.0, 1.0, 1.0); Seed = 287
- **Math.033** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.031** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 1.0
- **Value.004** [ShaderNodeValue] {label='Size'}
- **Value.005** [ShaderNodeValue] {label='Flatness'}
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Capture Attribute.006** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Capture Attribute.005** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Capture Attribute.004** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Capture Attribute.007** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Compare.006** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0
- **Group Output** [NodeGroupOutput]
- **Float Curve** [ShaderNodeFloatCurve]
    inputs livres: Factor = 1.0
- **Switch.003** [GeometryNodeSwitch] {input_type=FLOAT}
    inputs livres: False = 1.0
- **Spline Parameter.004** [GeometryNodeSplineParameter]
- **Sample Curve.004** [GeometryNodeSampleCurve] {data_type=FLOAT, mode=LENGTH}
- **Math.006** [ShaderNodeMath] {operation=SUBTRACT}
- **Group.005** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Group Input.017** [NodeGroupInput]
- **Math.005** [ShaderNodeMath] {operation=SUBTRACT}
- **Spline Parameter.006** [GeometryNodeSplineParameter]
- **Math.004** [ShaderNodeMath] {operation=DIVIDE}
- **Group Input.018** [NodeGroupInput]
- **Compare.001** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=INT, mode=ELEMENT}
- **Index.001** [GeometryNodeInputIndex]
- **Delete Geometry** [GeometryNodeDeleteGeometry] {domain=CURVE, mode=ALL}
- **Spline Parameter.001** [GeometryNodeSplineParameter]
- **Accumulate Field.001** [GeometryNodeAccumulateField] {data_type=FLOAT, domain=POINT}
- **Curve of Point** [GeometryNodeCurveOfPoint]
- **Sample Curve.001** [GeometryNodeSampleCurve] {data_type=FLOAT, mode=LENGTH}
- **Capture Attribute.001** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Map Range.002** [ShaderNodeMapRange] {data_type=FLOAT}
    inputs livres: From Min = 0.0; From Max = 1.0
- **Spline Parameter** [GeometryNodeSplineParameter]
- **Math.002** [ShaderNodeMath] {operation=MULTIPLY}
- **Group.004** [GeometryNodeGroup] -> grupo '.shape_range'
    inputs livres: Min = 0.0; Max = 1.0; Base = 2.0
- **Group Input.009** [NodeGroupInput]
- **Group Input.010** [NodeGroupInput]
- **Group Input.008** [NodeGroupInput]
- **Math.001** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = -1.0
- **Group Input.007** [NodeGroupInput]
- **Math.036** [ShaderNodeMath] {operation=SUBTRACT}
- **Math.035** [ShaderNodeMath] {operation=ADD}
- **Math.047** [ShaderNodeMath] {operation=ADD}
- **Math.044** [ShaderNodeMath] {operation=DIVIDE}
- **Math.045** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.043** [ShaderNodeMath] {operation=DIVIDE}
    inputs livres: Value = 1.0
- **Math.040** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.046** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = 2.0
- **Math.041** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.059** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = 4.0
- **Group Input.001** [NodeGroupInput]
- **Math.058** [ShaderNodeMath] {operation=PINGPONG}
    inputs livres: Value = 1.0
- **Math.060** [ShaderNodeMath] {operation=SUBTRACT}
- **Combine XYZ.001** [ShaderNodeCombineXYZ]
- **Math.042** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.049** [ShaderNodeMath] {operation=SINE}
- **Math.039** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.048** [ShaderNodeMath] {operation=SINE}
- **Math.038** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = 6.2832
- **Math.037** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = 6.2832
- **Group.001** [GeometryNodeGroup] -> grupo 'Curve Segment'
- **Math.028** [ShaderNodeMath] {operation=DIVIDE}
- **Math.030** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.012** [ShaderNodeMath] {operation=MULTIPLY}
- **Group Input.022** [NodeGroupInput]
- **Math.013** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = 0.1
- **Math.032** [ShaderNodeMath] {operation=DIVIDE}
    inputs livres: Value = 1.0
- **Group.006** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Sample Index** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
    inputs livres: Index = 0
- **Accumulate Field.002** [GeometryNodeAccumulateField] {data_type=INT, domain=POINT}
- **Group Input.003** [NodeGroupInput]
- **Group Input.004** [NodeGroupInput]
- **Group** [GeometryNodeGroup] -> grupo 'Create Guide Index Map'
    inputs livres: Group ID = 0
- **Group Input.019** [NodeGroupInput]
- **Boolean Math** [FunctionNodeBooleanMath] {operation=AND}
- **Boolean Math.001** [FunctionNodeBooleanMath] {operation=NIMPLY}
- **Switch.001** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Named Attribute.001** [GeometryNodeInputNamedAttribute] {data_type=INT}
    inputs livres: Name = guide_curve_index
- **Accumulate Field** [GeometryNodeAccumulateField] {data_type=INT, domain=CURVE}
- **Compare.005** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = -987654
- **Group Input.021** [NodeGroupInput]
- **Sample Index.001** [GeometryNodeSampleIndex] {data_type=BOOLEAN, domain=CURVE}
    inputs livres: Index = 0
- **Switch.004** [GeometryNodeSwitch] {input_type=INT}
- **Compare** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Capture Attribute.008** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Vector Math.015** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.016** [ShaderNodeVectorMath] {operation=DOT_PRODUCT}
- **Vector Math.017** [ShaderNodeVectorMath] {operation=DOT_PRODUCT}
- **Math.008** [ShaderNodeMath] {operation=DIVIDE}
    inputs livres: Value = 6.2832
- **Evaluate at Index** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Evaluate at Index.001** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Evaluate at Index.002** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Vector Math.014** [ShaderNodeVectorMath] {operation=CROSS_PRODUCT}
- **Points of Curve** [GeometryNodePointsOfCurve]
    inputs livres: Sort Index = 0
- **Curve Tangent.002** [GeometryNodeInputTangent]
- **Normal.003** [GeometryNodeInputNormal]
- **Group.002** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Math.057** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.029** [ShaderNodeMath] {operation=WRAP}
    inputs livres: Value = 0.0
- **Evaluate on Domain** [GeometryNodeFieldOnDomain] {data_type=INT, domain=CURVE}
- **Math.007** [ShaderNodeMath] {operation=ARCTAN2}
- **Integer** [FunctionNodeInputInt]
- **Align Rotation to Vector** [FunctionNodeAlignRotationToVector]
    inputs livres: Factor = 1.0
- **Align Rotation to Vector.001** [FunctionNodeAlignRotationToVector]
    inputs livres: Factor = 1.0
- **Menu Switch** [GeometryNodeMenuSwitch] {data_type=GEOMETRY}
- **Group Input.011** [NodeGroupInput]
- **Join Geometry.001** [GeometryNodeJoinGeometry]
- **Switch** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Group Input.023** [NodeGroupInput]

## Ligacoes (311)
- Group Input.Geometry -> Separate Components.Geometry
- Separate Components.Mesh -> Join Geometry.Geometry
- Separate Components.Point Cloud -> Join Geometry.Geometry
- Separate Components.Volume -> Join Geometry.Geometry
- Separate Components.Instances -> Join Geometry.Geometry
- Set Spline Resolution.001.Curve -> Join Geometry.Geometry
- Set Spline Type.002.Curve -> Group.Geometry
- Capture Attribute.006.Geometry -> Set Position.001.Geometry
- Sample Curve.Tangent -> Vector Math.005.Vector
- Sample Curve.Normal -> Vector Math.005.Vector
- Vector Math.009.Vector -> Set Position.001.Offset
- Vector Math.013.Vector -> Separate XYZ.001.Vector
- Separate XYZ.001.X -> Vector Math.008.Scale
- Sample Curve.Normal -> Vector Math.008.Vector
- Vector Math.008.Vector -> Vector Math.007.Vector
- Vector Math.006.Vector -> Vector Math.007.Vector
- Vector Math.005.Vector -> Vector Math.006.Vector
- Separate XYZ.001.Y -> Vector Math.006.Scale
- Capture Attribute.Value -> Math.028.Value
- Math.012.Value -> Accumulate Field.001.Value
- Math.028.Value -> Math.012.Value
- Math.033.Value -> Math.030.Value
- Capture Attribute.007.Geometry -> Capture Attribute.004.Geometry
- Capture Attribute.004.Geometry -> Capture Attribute.005.Geometry
- Capture Attribute.Value -> Math.033.Value
- Math.031.Value -> Math.030.Value
- Value.004.Value -> Math.033.Value
- Value.004.Value -> Math.032.Value
- Value.005.Value -> Math.031.Value
- Math.038.Value -> Math.049.Value
- Math.041.Value -> Math.035.Value
- Math.040.Value -> Math.036.Value
- Math.037.Value -> Math.048.Value
- Math.042.Value -> Combine XYZ.001.X
- Math.039.Value -> Combine XYZ.001.Y
- Math.043.Value -> Math.036.Value
- Math.036.Value -> Math.037.Value
- Math.035.Value -> Math.038.Value
- Math.049.Value -> Math.042.Value
- Math.048.Value -> Math.039.Value
- Math.047.Value -> Math.041.Value
- Math.047.Value -> Math.040.Value
- Math.032.Value -> Math.046.Value
- Math.046.Value -> Math.040.Value
- Math.032.Value -> Math.041.Value
- Capture Attribute.001.Value -> Math.047.Value
- Evaluate on Domain.Value -> Math.045.Value
- Math.043.Value -> Math.045.Value
- Math.045.Value -> Math.044.Value
- Math.032.Value -> Math.044.Value
- Capture Attribute.001.Value -> Combine XYZ.001.Z
- Math.033.Value -> Math.042.Value
- Math.030.Value -> Math.039.Value
- Combine XYZ.001.Vector -> Capture Attribute.004.Value
- Capture Attribute.008.Geometry -> Subdivide Curve.002.Curve
- Capture Attribute.008.Geometry -> Sample Curve.Curves
- Capture Attribute.008.Value -> Sample Curve.Curve Index
- Curve of Point.Curve Index -> Accumulate Field.001.Group ID
- Integer.Integer -> Math.043.Value
- Vector Math.012.Vector -> Vector Math.010.Vector
- Sample Curve.Position -> Vector Math.011.Vector
- Position.Position -> Vector Math.011.Vector
- Vector Math.007.Vector -> Vector Math.012.Vector
- Vector Math.011.Vector -> Vector Math.012.Vector
- Spline Parameter.003.Factor -> Map Range.Value
- Spline Parameter.002.Length -> Sample Curve.Length
- Capture Attribute.Geometry -> Sample Curve.001.Curves
- Capture Attribute.008.Value -> Sample Curve.001.Curve Index
- Accumulate Field.001.Leading -> Sample Curve.001.Value
- Random Value.Value -> Separate XYZ.002.Vector
- Math.052.Value -> Vector Rotate.Angle
- Combine XYZ.002.Vector -> Vector Rotate.Vector
- Separate XYZ.002.Y -> Math.052.Value
- Separate XYZ.002.X -> Math.053.Value
- Math.053.Value -> Combine XYZ.002.X
- Vector Rotate.Vector -> Evaluate on Domain.001.Value
- Vector Math.018.Vector -> Vector Math.013.Vector
- Math.056.Value -> Math.055.Value
- Math.062.Value -> Math.056.Value
- Capture Attribute.Geometry -> Capture Attribute.001.Geometry
- Sample Curve.001.Value -> Capture Attribute.001.Value
- Capture Attribute.005.Value -> Map Range.001.Value
- Map Range.001.Result -> Math.056.Value
- Math.043.Value -> Math.035.Value
- Math.Value -> Vector Math.010.Scale
- Group.001.Segment Length -> Math.012.Value
- Capture Attribute.008.Value -> Points of Curve.Curve Index
- Points of Curve.Point Index -> Evaluate at Index.Index
- Points of Curve.Point Index -> Evaluate at Index.001.Index
- Group.002.Root Position -> Evaluate at Index.001.Value
- Points of Curve.Point Index -> Evaluate at Index.002.Index
- Normal.003.Normal -> Evaluate at Index.002.Value
- Curve Tangent.002.Tangent -> Evaluate at Index.Value
- Evaluate at Index.Value -> Vector Math.014.Vector
- Evaluate at Index.002.Value -> Vector Math.014.Vector
- Evaluate at Index.001.Value -> Vector Math.015.Vector
- Group.002.Root Position -> Vector Math.015.Vector
- Vector Math.015.Vector -> Vector Math.016.Vector
- Evaluate at Index.002.Value -> Vector Math.016.Vector
- Vector Math.015.Vector -> Vector Math.017.Vector
- Vector Math.014.Vector -> Vector Math.017.Vector
- Vector Math.016.Value -> Math.007.Value
- Vector Math.017.Value -> Math.007.Value
- Math.007.Value -> Math.008.Value
- Math.008.Value -> Math.057.Value
- Integer.Integer -> Math.057.Value
- Math.057.Value -> Math.029.Value
- Integer.Integer -> Math.029.Value
- Math.029.Value -> Evaluate on Domain.Value
- Spline Parameter.001.Length -> Sample Curve.001.Length
- Evaluate on Domain.001.Value -> Vector Math.018.Vector
- Math.061.Value -> Vector Math.018.Scale
- Math.035.Value -> Math.059.Value
- Math.060.Value -> Math.058.Value
- Math.058.Value -> Capture Attribute.005.Value
- Math.059.Value -> Math.060.Value
- Accumulate Field.002.Total -> Sample Index.Value
- Set Spline Type.002.Curve -> Sample Index.Geometry
- Named Attribute.001.Exists -> Accumulate Field.002.Value
- Sample Index.Value -> Compare.A
- Group.Geometry -> Switch.001.False
- Set Spline Type.002.Curve -> Switch.001.True
- Compare.Result -> Boolean Math.Boolean
- Group Input.003.Existing Guide Map -> Boolean Math.Boolean
- Group Input.004.Guide Distance -> Group.Guide Distance
- Vector Math.010.Vector -> Vector Math.009.Vector
- Group Input.002.Factor -> Vector Math.009.Scale
- Group Input.006.Braid Start -> Map Range.From Max
- Math.009.Value -> Math.062.Value
- Map Range.Result -> Math.Value
- Group Input.001.Shape Asymmetry -> Math.060.Value
- Group Input.012.Thickness Shape -> Math.063.Value
- Group Input.012.Thickness Shape -> Math.064.Value
- Math.063.Value -> Map Range.001.To Min
- Math.064.Value -> Map Range.001.To Max
- Group Input.013.Thickness -> Math.062.Value
- Switch.Output -> Group Output.Geometry
- Spline Parameter.Factor -> Group.004.Value
- Math.001.Value -> Group.004.Shape
- Group Input.007.Radius -> Math.002.Value
- Map Range.002.Result -> Math.002.Value
- Group.004.Value -> Map Range.002.Value
- Group Input.008.Shape -> Math.001.Value
- Group Input.009.Factor Min -> Map Range.002.To Min
- Group Input.010.Factor Max -> Map Range.002.To Max
- Subdivide Curve.002.Curve -> Capture Attribute.Geometry
- Math.002.Value -> Capture Attribute.Value
- Capture Attribute.002.Geometry -> Curve to Points.Curve
- Index.Index -> Sample Curve.002.Curve Index
- Capture Attribute.008.Value -> Compare.001.A
- Index.001.Index -> Compare.001.B
- Capture Attribute.008.Geometry -> Delete Geometry.Geometry
- Compare.001.Result -> Delete Geometry.Selection
- Capture Attribute.002.Geometry -> Sample Curve.002.Curves
- Curve to Points.Points -> Set Position.Geometry
- Sample Curve.002.Position -> Set Position.Position
- Group.003.Length -> Math.003.Value
- Group Input.014.Flare Length -> Math.003.Value
- Delete Geometry.Geometry -> Capture Attribute.002.Geometry
- Capture Attribute.002.Value -> Sample Curve.002.Length
- Math.003.Value -> Capture Attribute.002.Value
- Set Position.Geometry -> Instance on Points.Points
- Sample Curve.002.Tangent -> Vector Math.Vector
- Menu Switch.Output -> Instance on Points.Instance
- Group Input.015.Hair Tie -> Object Info.Object
- Group Input.016.Hair Tie Scale -> Instance on Points.Scale
- Group Input.015.Hair Tie -> Geometry to Instance.Geometry
- Group Input.017.Flare Length -> Math.005.Value
- Math.005.Value -> Math.006.Value
- Group.005.Length -> Math.005.Value
- Capture Attribute.005.Geometry -> Capture Attribute.006.Geometry
- Capture Attribute.Geometry -> Sample Curve.004.Curves
- Spline Parameter.004.Length -> Math.006.Value
- Sample Curve.004.Value -> Math.004.Value
- Math.004.Value -> Capture Attribute.006.Value
- Capture Attribute.006.Value -> Group Output.Flare Parameter
- Spline Parameter.006.Length -> Sample Curve.004.Length
- Math.006.Value -> Sample Curve.004.Value
- Capture Attribute.008.Value -> Sample Curve.004.Curve Index
- Group Input.018.Flare Length -> Math.004.Value
- Capture Attribute.006.Value -> Compare.006.A
- Capture Attribute.Value -> Math.009.Value
- Capture Attribute.006.Value -> Float Curve.Value
- Float Curve.Value -> Switch.003.True
- Compare.006.Result -> Switch.003.Switch
- Switch.003.Output -> Math.009.Value
- Math.010.Value -> Math.011.Value
- Group Input.005.Subdivision -> Math.010.Value
- Math.011.Value -> Subdivide Curve.002.Cuts
- Separate Components.Curve -> Capture Attribute.003.Geometry
- Spline Resolution.Resolution -> Capture Attribute.003.Value
- Set Spline Type.001.Curve -> Set Spline Resolution.001.Curve
- Group.006.Curve ID -> Random Value.ID
- Capture Attribute.003.Value -> Compare.004.A
- Compare.004.Result -> Switch.006.Switch
- Capture Attribute.003.Value -> Switch.006.False
- Switch.006.Output -> Set Spline Resolution.001.Resolution
- Set Position.001.Geometry -> Set Spline Type.001.Curve
- Capture Attribute.003.Geometry -> Set Spline Type.002.Curve
- Capture Attribute.006.Value -> Math.054.Value
- Math.055.Value -> Math.061.Value
- Compare.006.Result -> Switch.007.Switch
- Math.054.Value -> Switch.007.True
- Switch.007.Output -> Math.061.Value
- Group Input.020.Flare Opening -> Math.054.Value
- Math.044.Value -> Math.047.Value
- Group Input.019.Guide Mask -> Group.Guide Mask
- Capture Attribute.001.Geometry -> Capture Attribute.007.Geometry
- Capture Attribute.007.Value -> Group Output.Strand Index
- Group Input.021.Guide Index -> Compare.005.A
- Compare.005.Result -> Switch.004.Switch
- Group Input.021.Guide Index -> Switch.004.True
- Compare.005.Result -> Accumulate Field.Value
- Accumulate Field.Total -> Sample Index.001.Value
- Boolean Math.Boolean -> Boolean Math.001.Boolean
- Boolean Math.001.Boolean -> Switch.001.Switch
- Sample Index.001.Value -> Boolean Math.001.Boolean
- Set Spline Type.002.Curve -> Sample Index.001.Geometry
- Named Attribute.001.Attribute -> Switch.004.False
- Capture Attribute.008.Value -> Group Output.Guide Index
- Evaluate on Domain.Value -> Capture Attribute.007.Value
- Compare.006.Result -> Switch.008.Switch
- Capture Attribute.004.Value -> Switch.008.False
- Switch.008.Output -> Vector Math.013.Vector
- Group Input.022.Frequency -> Math.013.Value
- Math.013.Value -> Math.028.Value
- Switch.001.Output -> Capture Attribute.008.Geometry
- Switch.004.Output -> Capture Attribute.008.Value
- Vector Math.Vector -> Align Rotation to Vector.Vector
- Sample Curve.002.Normal -> Align Rotation to Vector.001.Vector
- Align Rotation to Vector.Rotation -> Align Rotation to Vector.001.Rotation
- Align Rotation to Vector.001.Rotation -> Instance on Points.Rotation
- Object Info.Geometry -> Menu Switch.Object
- Geometry to Instance.Instances -> Menu Switch.Geometry
- Group Input.011.Hair Tie Input Type -> Menu Switch.Menu
- Join Geometry.Geometry -> Join Geometry.001.Geometry
- Instance on Points.Instances -> Join Geometry.001.Geometry
- Join Geometry.001.Geometry -> Switch.True
- Join Geometry.Geometry -> Switch.False
- Group Input.023.Hair Tie -> Switch.Switch
- Separate Components.Grease Pencil -> Join Geometry.Geometry
