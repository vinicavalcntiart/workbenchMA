# Curl Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- INPUT Geometry (Geometry, default None)
- INPUT Factor (Float, default 1.0, min 0.0, max 1.0) — Factor to blend overall effect
- INPUT Subdivision (Int, default 1, min 0, max 6) — Subdivision level applied before deformation
- INPUT Curl Start (Float, default 0.1, min 0.0, max 1.0) — Percentage along each curve to blend deformation from the root
- INPUT Radius (Float, default 0.1, min 0.0, max 3.4028234663852886e+38) — Overall radius of the curls
- INPUT Factor Start (Float, default 1.0, min 0.0, max 10000.0) — Factor for the radius at the curl start
- INPUT Factor End (Float, default 1.0, min 0.0, max 10000.0) — Factor for the radius at the curl end
- INPUT Frequency (Float, default 1.0, min 0.0, max 10000.0) — Frequency factor of the curls
- INPUT Random Offset (Float, default 0.25, min 0.0, max 1.0) — Amount of random offset per curve
- INPUT Seed (Int, default 0, min -10000, max 10000) — Random Seed for the operation
- [painel] Guide Map
- OUTPUT Guide Index (Int, default 0, min -2147483648, max 2147483647) — Guide index map that was used for the operation
- INPUT Guide Index (Int, default -987654, min -2147483648, max 2147483647) — Guide index map to be used. This input has priority
- INPUT Guide Distance (Float, default 0.1, min 0.0, max 3.4028234663852886e+38) — Minimum distance between two guides for new guide map
- INPUT Guide Mask (Float, default 1.0, min 0.0, max 1.0) — Mask for which curves are eligible to be selected as guides
- INPUT Existing Guide Map (Bool, default True) — Use the existing guide map attribute if available

## Nodes (124)
- **Separate Components** [GeometryNodeSeparateComponents]
- **Group Input** [NodeGroupInput]
- **Subdivide Curve.002** [GeometryNodeSubdivideCurve]
- **Math.003** [ShaderNodeMath] {operation=POWER}
    inputs livres: Value = 2.0
- **Math.004** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 1.0
- **Group Input.005** [NodeGroupInput]
- **Capture Attribute.001** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Sample Curve** [GeometryNodeSampleCurve] {data_type=FLOAT, mode=LENGTH}
- **Spline Parameter.002** [GeometryNodeSplineParameter]
- **Compare.003** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Set Spline Type.001** [GeometryNodeCurveSplineType]
- **Set Spline Resolution.001** [GeometryNodeSetSplineResolution]
- **Switch.004** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: True = 12
- **Group Input.002** [NodeGroupInput]
- **Position** [GeometryNodeInputPosition]
- **Vector Math.008** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.010** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.009** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.006** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.005** [ShaderNodeVectorMath] {operation=CROSS_PRODUCT}
- **Vector Math.007** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.011** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.012** [ShaderNodeVectorMath] {operation=ADD}
- **Separate XYZ.001** [ShaderNodeSeparateXYZ]
- **Set Position.001** [GeometryNodeSetPosition]
- **Math** [ShaderNodeMath] {operation=POWER}
    inputs livres: Value = 0.5
- **Map Range** [ShaderNodeMapRange] {data_type=FLOAT}
    inputs livres: From Min = -0.0; To Min = 0.0; To Max = 1.0
- **Group Input.006** [NodeGroupInput]
- **Spline Parameter.003** [GeometryNodeSplineParameter]
- **Group Output** [NodeGroupOutput]
- **Capture Attribute.004** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Random Value.001** [FunctionNodeRandomValue] {data_type=FLOAT}
    inputs livres: Min = 0.0; Max = 3.9
- **Sample Index.001** [GeometryNodeSampleIndex] {data_type=INT, domain=CURVE}
- **Group.003** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Evaluate on Domain.001** [GeometryNodeFieldOnDomain] {data_type=FLOAT, domain=CURVE}
- **Math.048** [ShaderNodeMath] {operation=COSINE}
- **Math.049** [ShaderNodeMath] {operation=SINE}
- **Math.038** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = 6.2832
- **Combine XYZ.001** [ShaderNodeCombineXYZ]
    inputs livres: Z = 0.0
- **Vector Math** [ShaderNodeVectorMath] {operation=SCALE}
- **Map Range.002** [ShaderNodeMapRange] {data_type=FLOAT}
    inputs livres: From Min = 0.0; From Max = 1.0
- **Group Input.007** [NodeGroupInput]
- **Spline Parameter** [GeometryNodeSplineParameter]
- **Group Input.009** [NodeGroupInput]
- **Group Input.010** [NodeGroupInput]
- **Math.033** [ShaderNodeMath] {operation=MULTIPLY}
- **Accumulate Field.001** [GeometryNodeAccumulateField] {data_type=FLOAT, domain=POINT}
- **Math.016** [ShaderNodeMath] {operation=MULTIPLY}
- **Curve of Point** [GeometryNodeCurveOfPoint]
- **Math.015** [ShaderNodeMath] {operation=ADD}
- **Group Input.015** [NodeGroupInput]
- **Math.017** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = 3.0
- **Group.001** [GeometryNodeGroup] -> grupo 'Curve Segment'
- **Group Input.012** [NodeGroupInput]
- **Math.014** [ShaderNodeMath] {operation=MULTIPLY}
- **Random Value** [FunctionNodeRandomValue] {data_type=FLOAT}
    inputs livres: Min = 0.0; Max = 1.0
- **Evaluate on Domain** [GeometryNodeFieldOnDomain] {data_type=FLOAT, domain=CURVE}
- **Group.002** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Group Input.001** [NodeGroupInput]
- **Math.021** [ShaderNodeMath] {operation=ADD}
- **Spline Resolution** [GeometryNodeInputSplineResolution]
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Set Spline Type** [GeometryNodeCurveSplineType]
- **Named Attribute.001** [GeometryNodeInputNamedAttribute] {data_type=INT}
    inputs livres: Name = guide_curve_index
- **Boolean Math** [FunctionNodeBooleanMath] {operation=AND}
- **Sample Index** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
    inputs livres: Index = 0
- **Accumulate Field.002** [GeometryNodeAccumulateField] {data_type=INT, domain=POINT}
- **Compare** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Group Input.003** [NodeGroupInput]
- **Group Input.004** [NodeGroupInput]
- **Group** [GeometryNodeGroup] -> grupo 'Create Guide Index Map'
    inputs livres: Group ID = 0
- **Group Input.008** [NodeGroupInput]
- **Boolean Math.001** [FunctionNodeBooleanMath] {operation=NIMPLY}
- **Sample Index.002** [GeometryNodeSampleIndex] {data_type=BOOLEAN, domain=CURVE}
    inputs livres: Index = 0
- **Accumulate Field** [GeometryNodeAccumulateField] {data_type=INT, domain=CURVE}
- **Group Input.014** [NodeGroupInput]
- **Compare.005** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = -987654
- **Switch.001** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Switch.005** [GeometryNodeSwitch] {input_type=INT}
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Hash Value** [FunctionNodeHashValue] {data_type=INT}
    inputs livres: Seed = 91487

## Ligacoes (137)
- Group Input.Geometry -> Separate Components.Geometry
- Separate Components.Mesh -> Join Geometry.Geometry
- Separate Components.Point Cloud -> Join Geometry.Geometry
- Separate Components.Volume -> Join Geometry.Geometry
- Separate Components.Instances -> Join Geometry.Geometry
- Set Spline Resolution.001.Curve -> Join Geometry.Geometry
- Set Spline Type.Curve -> Group.Geometry
- Capture Attribute.004.Geometry -> Set Position.001.Geometry
- Sample Curve.Tangent -> Vector Math.005.Vector
- Sample Curve.Normal -> Vector Math.005.Vector
- Vector Math.009.Vector -> Set Position.001.Offset
- Capture Attribute.004.Value -> Separate XYZ.001.Vector
- Separate XYZ.001.X -> Vector Math.008.Scale
- Sample Curve.Normal -> Vector Math.008.Vector
- Vector Math.008.Vector -> Vector Math.007.Vector
- Vector Math.006.Vector -> Vector Math.007.Vector
- Vector Math.005.Vector -> Vector Math.006.Vector
- Separate XYZ.001.Y -> Vector Math.006.Scale
- Capture Attribute.001.Geometry -> Capture Attribute.004.Geometry
- Group Input.007.Radius -> Math.033.Value
- Math.038.Value -> Math.049.Value
- Math.049.Value -> Combine XYZ.001.X
- Math.048.Value -> Combine XYZ.001.Y
- Capture Attribute.001.Value -> Math.038.Value
- Capture Attribute.Geometry -> Subdivide Curve.002.Curve
- Capture Attribute.Geometry -> Sample Curve.Curves
- Capture Attribute.Value -> Sample Curve.Curve Index
- Curve of Point.Curve Index -> Accumulate Field.001.Group ID
- Vector Math.012.Vector -> Vector Math.010.Vector
- Sample Curve.Position -> Vector Math.011.Vector
- Position.Position -> Vector Math.011.Vector
- Vector Math.007.Vector -> Vector Math.012.Vector
- Vector Math.011.Vector -> Vector Math.012.Vector
- Spline Parameter.003.Factor -> Map Range.Value
- Spline Parameter.002.Length -> Sample Curve.Length
- Subdivide Curve.002.Curve -> Capture Attribute.001.Geometry
- Math.Value -> Vector Math.010.Scale
- Accumulate Field.002.Total -> Sample Index.Value
- Set Spline Type.Curve -> Sample Index.Geometry
- Named Attribute.001.Exists -> Accumulate Field.002.Value
- Sample Index.Value -> Compare.A
- Group.Geometry -> Switch.001.False
- Set Spline Type.Curve -> Switch.001.True
- Compare.Result -> Boolean Math.Boolean
- Boolean Math.001.Boolean -> Switch.001.Switch
- Group Input.003.Existing Guide Map -> Boolean Math.Boolean
- Group Input.004.Guide Distance -> Group.Guide Distance
- Vector Math.010.Vector -> Vector Math.009.Vector
- Group Input.002.Factor -> Vector Math.009.Scale
- Group Input.006.Curl Start -> Map Range.From Max
- Map Range.Result -> Math.Value
- Join Geometry.Geometry -> Group Output.Geometry
- Spline Parameter.Factor -> Map Range.002.Value
- Group Input.009.Factor Start -> Map Range.002.To Min
- Group Input.010.Factor End -> Map Range.002.To Max
- Math.038.Value -> Math.048.Value
- Random Value.001.Value -> Evaluate on Domain.001.Value
- Accumulate Field.001.Leading -> Math.015.Value
- Math.021.Value -> Math.015.Value
- Math.016.Value -> Accumulate Field.001.Value
- Math.015.Value -> Capture Attribute.001.Value
- Math.004.Value -> Subdivide Curve.002.Cuts
- Random Value.Value -> Math.014.Value
- Hash Value.Hash -> Random Value.Seed
- Group Input.012.Random Offset -> Math.014.Value
- Group Input.005.Subdivision -> Math.003.Value
- Math.003.Value -> Math.004.Value
- Separate Components.Curve -> Capture Attribute.002.Geometry
- Spline Resolution.Resolution -> Capture Attribute.002.Value
- Set Spline Type.001.Curve -> Set Spline Resolution.001.Curve
- Capture Attribute.002.Geometry -> Set Spline Type.Curve
- Capture Attribute.002.Value -> Compare.003.A
- Compare.003.Result -> Switch.004.Switch
- Capture Attribute.002.Value -> Switch.004.False
- Switch.004.Output -> Set Spline Resolution.001.Resolution
- Set Position.001.Geometry -> Set Spline Type.001.Curve
- Group.002.Curve ID -> Random Value.ID
- Group.003.Curve ID -> Sample Index.001.Value
- Sample Index.001.Value -> Random Value.001.ID
- Capture Attribute.Value -> Sample Index.001.Index
- Capture Attribute.Geometry -> Sample Index.001.Geometry
- Map Range.002.Result -> Math.033.Value
- Math.014.Value -> Evaluate on Domain.Value
- Group Input.008.Guide Mask -> Group.Guide Mask
- Group Input.014.Guide Index -> Compare.005.A
- Compare.005.Result -> Switch.005.Switch
- Group Input.014.Guide Index -> Switch.005.True
- Compare.005.Result -> Accumulate Field.Value
- Accumulate Field.Total -> Sample Index.002.Value
- Boolean Math.Boolean -> Boolean Math.001.Boolean
- Sample Index.002.Value -> Boolean Math.001.Boolean
- Named Attribute.001.Attribute -> Switch.005.False
- Set Spline Type.Curve -> Sample Index.002.Geometry
- Capture Attribute.Value -> Group Output.Guide Index
- Group Input.015.Frequency -> Math.017.Value
- Group.001.Segment Length -> Math.016.Value
- Math.017.Value -> Math.016.Value
- Combine XYZ.001.Vector -> Vector Math.Vector
- Vector Math.Vector -> Capture Attribute.004.Value
- Math.033.Value -> Vector Math.Scale
- Hash Value.Hash -> Random Value.001.Seed
- Evaluate on Domain.001.Value -> Math.021.Value
- Evaluate on Domain.Value -> Math.021.Value
- Switch.001.Output -> Capture Attribute.Geometry
- Switch.005.Output -> Capture Attribute.Value
- Separate Components.Grease Pencil -> Join Geometry.Geometry
- Group Input.001.Seed -> Hash Value.Value
