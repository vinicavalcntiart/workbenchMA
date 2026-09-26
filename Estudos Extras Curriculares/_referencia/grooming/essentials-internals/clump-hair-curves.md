# Clump Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- INPUT Geometry (Geometry, default None) — Input Geometry (May include other than curves)
- INPUT Factor (Float, default 1.0, min 0.0, max 1.0) — Factor to blend overall effect
- INPUT Shape (Float, default 0.5, min -1.0, max 1.0) — Shape of the influence along curves (0=constant, 0.5=linear)
- INPUT Tip Spread (Float, default 0.0, min 0.0, max 10.0) — Distance of random spread at the curve tips
- INPUT Clump Offset (Float, default 0.0, min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Offset of each clump in a random direction
- INPUT Distance Falloff (Float, default 0.0, min 0.0, max 3.4028234663852886e+38) — Falloff distance for the clumping effect (0 means no falloff)
- INPUT Distance Threshold (Float, default 0.0, min 0.0, max 3.4028234663852886e+38) — Distance threshold for the falloff around the guide
- INPUT Seed (Int, default 0, min -10000, max 10000) — Random seed for the operation
- INPUT Preserve Length (Bool, default False) — Preserve each curve's length during deformation
- [painel] Guide Map
- OUTPUT Guide Index (Int, default 0, min -2147483648, max 2147483647) — Guide index map that was used for the operation
- INPUT Guide Index (Int, default -987654, min -2147483648, max 2147483647) — Guide index map to be used. This input has priority
- INPUT Guide Distance (Float, default 0.1, min 0.0, max 3.4028234663852886e+38) — Minimum distance between two guides for new guide map
- INPUT Guide Mask (Float, default 1.0, min 0.0, max 1.0) — Mask for which curves are eligible to be selected as guides
- INPUT Existing Guide Map (Bool, default True) — Use the existing guide map attribute if available

## Nodes (144)
- **Group Input.003** [NodeGroupInput]
- **Separate Components** [GeometryNodeSeparateComponents]
- **Group Output.001** [NodeGroupOutput]
- **Join Geometry.001** [GeometryNodeJoinGeometry]
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Position.001** [GeometryNodeInputPosition]
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Spline Resolution** [GeometryNodeInputSplineResolution]
- **Set Spline Type.002** [GeometryNodeCurveSplineType]
- **Switch.006** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: True = 12
- **Compare.004** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Set Spline Resolution.001** [GeometryNodeSetSplineResolution]
- **Set Spline Type.001** [GeometryNodeCurveSplineType]
- **Group.005** [GeometryNodeGroup] -> grupo 'Restore Curve Segment Length'
    inputs livres: Factor = 1.0; Pin at Parameter = 0.0
- **Group Input.010** [NodeGroupInput]
- **Vector Math** [ShaderNodeVectorMath] {operation=CROSS_PRODUCT}
- **Sample Curve** [GeometryNodeSampleCurve] {data_type=FLOAT, mode=FACTOR}
- **Spline Parameter** [GeometryNodeSplineParameter]
- **Vector Math.001** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.002** [ShaderNodeVectorMath] {operation=SCALE}
- **Separate XYZ** [ShaderNodeSeparateXYZ]
- **Vector Math.006** [ShaderNodeVectorMath] {operation=ADD}
- **Evaluate on Domain** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Combine XYZ** [ShaderNodeCombineXYZ]
    inputs livres: Z = 0.0
- **Vector Math.004** [ShaderNodeVectorMath] {operation=DOT_PRODUCT}
- **Vector Math.005** [ShaderNodeVectorMath] {operation=DOT_PRODUCT}
- **Vector Math.008** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.003** [ShaderNodeVectorMath] {operation=CROSS_PRODUCT}
- **Sample Curve.001** [GeometryNodeSampleCurve] {data_type=FLOAT, mode=FACTOR}
    inputs livres: Factor = 0.0
- **Evaluate at Index** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Group** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Evaluate on Domain.001** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Sample Index** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
    inputs livres: Index = 0
- **Accumulate Field.002** [GeometryNodeAccumulateField] {data_type=INT, domain=POINT}
- **Group Input.002** [NodeGroupInput]
- **Boolean Math.001** [FunctionNodeBooleanMath] {operation=AND}
- **Switch.001** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Named Attribute.003** [GeometryNodeInputNamedAttribute] {data_type=INT}
    inputs livres: Name = guide_curve_index
- **Group Input.013** [NodeGroupInput]
- **Group Input.004** [NodeGroupInput]
- **Compare.003** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = -987654
- **Group Input.011** [NodeGroupInput]
- **Accumulate Field** [GeometryNodeAccumulateField] {data_type=INT, domain=CURVE}
- **Switch.003** [GeometryNodeSwitch] {input_type=INT}
- **Compare.001** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Group.003** [GeometryNodeGroup] -> grupo 'Create Guide Index Map'
    inputs livres: Group ID = 0
- **Boolean Math.002** [FunctionNodeBooleanMath] {operation=NIMPLY}
- **Sample Index.001** [GeometryNodeSampleIndex] {data_type=BOOLEAN, domain=CURVE}
    inputs livres: Index = 0
- **Capture Attribute.001** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Position** [GeometryNodeInputPosition]
- **Mix** [ShaderNodeMix] {data_type=VECTOR, blend_type=MIX}
- **Vector Math.009** [ShaderNodeVectorMath] {operation=ADD}
- **Math.002** [ShaderNodeMath] {operation=MULTIPLY}
- **Set Position** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Group Input.001** [NodeGroupInput]
- **Math** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 1.0
- **Vector Math.013** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.007** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.011** [ShaderNodeVectorMath] {operation=ADD}
- **Math.001** [ShaderNodeMath] {operation=MULTIPLY}
- **Vector Math.025** [ShaderNodeVectorMath] {operation=ADD}
- **Switch.002** [GeometryNodeSwitch] {input_type=VECTOR}
    inputs livres: True = (0.0, 0.0, 0.0)
- **Vector Math.020** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.021** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.022** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.015** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.016** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.018** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.019** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.014** [ShaderNodeVectorMath] {operation=SCALE}
- **Switch** [GeometryNodeSwitch] {input_type=VECTOR}
    inputs livres: True = (0.0, 0.0, 0.0)
- **Sample Curve.002** [GeometryNodeSampleCurve] {data_type=FLOAT, mode=FACTOR}
    inputs livres: Factor = 1.0
- **Vector Math.017** [ShaderNodeVectorMath] {operation=CROSS_PRODUCT}
- **Random Value** [FunctionNodeRandomValue] {data_type=FLOAT_VECTOR}
    inputs livres: Min = (-1.0, -1.0, -1.0); Max = (1.0, 1.0, 1.0)
- **Vector Math.026** [ShaderNodeVectorMath] {operation=SCALE}
- **Separate XYZ.002** [ShaderNodeSeparateXYZ]
- **Separate XYZ.001** [ShaderNodeSeparateXYZ]
- **Vector Math.012** [ShaderNodeVectorMath] {operation=SCALE}
- **Group Input.009** [NodeGroupInput]
- **Group Input.012** [NodeGroupInput]
- **Group Input.008** [NodeGroupInput]
- **Random Value.001** [FunctionNodeRandomValue] {data_type=FLOAT_VECTOR}
    inputs livres: Min = (-1.0, -1.0, -1.0); Max = (1.0, 1.0, 1.0)
- **Evaluate at Index.001** [GeometryNodeFieldAtIndex] {data_type=INT, domain=CURVE}
- **Group.006** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Group.007** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Group Input.005** [NodeGroupInput]
- **Compare** [FunctionNodeCompare] {operation=EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Compare.002** [FunctionNodeCompare] {operation=EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: A = 0.0; Epsilon = 0.0
- **Spline Parameter.001** [GeometryNodeSplineParameter]
- **Group Input** [NodeGroupInput]
- **Group.001** [GeometryNodeGroup] -> grupo '.shape_range'
    inputs livres: Min = 0.0; Max = 1.0; Base = 2.0
- **Math.003** [ShaderNodeMath] {operation=ADD}
- **Vector Math.010** [ShaderNodeVectorMath] {operation=LENGTH}
- **Compare.006** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Compare.007** [FunctionNodeCompare] {operation=EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Group Input.007** [NodeGroupInput]
- **Group Input.006** [NodeGroupInput]
- **Compare.005** [FunctionNodeCompare] {operation=LESS_EQUAL, data_type=FLOAT, mode=ELEMENT}
- **Map Range.001** [ShaderNodeMapRange] {data_type=FLOAT}
    inputs livres: To Min = 1.0; To Max = 0.0
- **Boolean Math** [FunctionNodeBooleanMath] {operation=AND}
- **Switch.004** [GeometryNodeSwitch] {input_type=FLOAT}
- **Hash Value** [FunctionNodeHashValue] {data_type=INT}
    inputs livres: Seed = 148762

## Ligacoes (184)
- Group Input.003.Geometry -> Separate Components.Geometry
- Capture Attribute.Geometry -> Group.003.Geometry
- Accumulate Field.002.Total -> Sample Index.Value
- Capture Attribute.Geometry -> Sample Index.Geometry
- Named Attribute.003.Exists -> Accumulate Field.002.Value
- Sample Index.Value -> Compare.001.A
- Group.003.Geometry -> Switch.001.False
- Capture Attribute.Geometry -> Switch.001.True
- Compare.001.Result -> Boolean Math.001.Boolean
- Boolean Math.002.Boolean -> Switch.001.Switch
- Capture Attribute.001.Value -> Sample Curve.Curve Index
- Capture Attribute.001.Geometry -> Sample Curve.Curves
- Sample Curve.Tangent -> Vector Math.Vector
- Sample Curve.Normal -> Vector Math.Vector
- Sample Curve.001.Tangent -> Vector Math.003.Vector
- Sample Curve.001.Normal -> Vector Math.003.Vector
- Vector Math.003.Vector -> Vector Math.004.Vector
- Sample Curve.001.Normal -> Vector Math.005.Vector
- Capture Attribute.001.Geometry -> Sample Curve.001.Curves
- Capture Attribute.001.Value -> Sample Curve.001.Curve Index
- Evaluate on Domain.Value -> Separate XYZ.Vector
- Sample Curve.Normal -> Vector Math.001.Vector
- Separate XYZ.X -> Vector Math.001.Scale
- Vector Math.Vector -> Vector Math.002.Vector
- Separate XYZ.Y -> Vector Math.002.Scale
- Vector Math.001.Vector -> Vector Math.006.Vector
- Vector Math.002.Vector -> Vector Math.006.Vector
- Vector Math.005.Value -> Combine XYZ.X
- Vector Math.004.Value -> Combine XYZ.Y
- Combine XYZ.Vector -> Evaluate on Domain.Value
- Vector Math.008.Vector -> Vector Math.005.Vector
- Vector Math.008.Vector -> Vector Math.004.Vector
- Group.Root Position -> Vector Math.008.Vector
- Group.Root Position -> Evaluate at Index.Value
- Evaluate at Index.Value -> Vector Math.008.Vector
- Capture Attribute.001.Value -> Evaluate at Index.Index
- Mix.Result -> Set Position.Position
- Vector Math.011.Vector -> Vector Math.009.Vector
- Sample Curve.Position -> Vector Math.009.Vector
- Vector Math.006.Vector -> Vector Math.007.Vector
- Group.001.Value -> Math.Value
- Math.Value -> Vector Math.007.Scale
- Vector Math.009.Vector -> Mix.B
- Position.Position -> Mix.A
- Spline Parameter.001.Factor -> Group.001.Value
- Group Input.Shape -> Group.001.Shape
- Group.001.Value -> Math.001.Value
- Group Input.001.Factor -> Math.001.Value
- Math.002.Value -> Mix.Factor
- Group Input.002.Existing Guide Map -> Boolean Math.001.Boolean
- Group Input.004.Guide Distance -> Group.003.Guide Distance
- Math.001.Value -> Math.002.Value
- Vector Math.008.Vector -> Vector Math.010.Vector
- Vector Math.010.Value -> Map Range.001.Value
- Switch.004.Output -> Math.002.Value
- Group Input.006.Distance Threshold -> Map Range.001.From Min
- Group Input.006.Distance Threshold -> Math.003.Value
- Group Input.007.Distance Falloff -> Math.003.Value
- Math.003.Value -> Map Range.001.From Max
- Group Input.008.Tip Spread -> Vector Math.012.Scale
- Random Value.Value -> Vector Math.012.Vector
- Evaluate on Domain.001.Value -> Vector Math.013.Vector
- Group.001.Value -> Vector Math.013.Scale
- Vector Math.007.Vector -> Vector Math.011.Vector
- Capture Attribute.001.Geometry -> Sample Curve.002.Curves
- Vector Math.012.Vector -> Separate XYZ.001.Vector
- Sample Curve.002.Tangent -> Vector Math.014.Vector
- Sample Curve.002.Normal -> Vector Math.015.Vector
- Separate XYZ.001.Z -> Vector Math.014.Scale
- Separate XYZ.001.X -> Vector Math.015.Scale
- Sample Curve.002.Tangent -> Vector Math.017.Vector
- Sample Curve.002.Normal -> Vector Math.017.Vector
- Separate XYZ.001.Y -> Vector Math.016.Scale
- Vector Math.017.Vector -> Vector Math.016.Vector
- Vector Math.015.Vector -> Vector Math.018.Vector
- Vector Math.016.Vector -> Vector Math.018.Vector
- Vector Math.018.Vector -> Vector Math.019.Vector
- Vector Math.014.Vector -> Vector Math.019.Vector
- Capture Attribute.001.Value -> Sample Curve.002.Curve Index
- Vector Math.026.Vector -> Separate XYZ.002.Vector
- Sample Curve.002.Normal -> Vector Math.020.Vector
- Separate XYZ.002.X -> Vector Math.020.Scale
- Separate XYZ.002.Y -> Vector Math.021.Scale
- Vector Math.020.Vector -> Vector Math.022.Vector
- Vector Math.021.Vector -> Vector Math.022.Vector
- Vector Math.017.Vector -> Vector Math.021.Vector
- Random Value.001.Value -> Vector Math.026.Vector
- Group Input.009.Clump Offset -> Vector Math.026.Scale
- Vector Math.013.Vector -> Vector Math.011.Vector
- Switch.Output -> Vector Math.025.Vector
- Switch.002.Output -> Vector Math.025.Vector
- Vector Math.025.Vector -> Evaluate on Domain.001.Value
- Vector Math.022.Vector -> Switch.002.False
- Vector Math.019.Vector -> Switch.False
- Group Input.009.Clump Offset -> Compare.002.B
- Compare.002.Result -> Switch.002.Switch
- Hash Value.Hash -> Random Value.Seed
- Hash Value.Hash -> Random Value.001.Seed
- Capture Attribute.001.Value -> Evaluate at Index.001.Index
- Separate Components.Mesh -> Join Geometry.001.Geometry
- Separate Components.Point Cloud -> Join Geometry.001.Geometry
- Separate Components.Volume -> Join Geometry.001.Geometry
- Separate Components.Instances -> Join Geometry.001.Geometry
- Set Spline Resolution.001.Curve -> Join Geometry.001.Geometry
- Join Geometry.001.Geometry -> Group Output.001.Geometry
- Set Position.Geometry -> Group.005.Curves
- Position.001.Position -> Capture Attribute.Value
- Capture Attribute.Value -> Group.005.Reference Position
- Group Input.010.Preserve Length -> Group.005.Selection
- Spline Parameter.Factor -> Sample Curve.Factor
- Group Input.011.Guide Index -> Compare.003.A
- Named Attribute.003.Attribute -> Switch.003.False
- Compare.003.Result -> Switch.003.Switch
- Group Input.011.Guide Index -> Switch.003.True
- Boolean Math.001.Boolean -> Boolean Math.002.Boolean
- Capture Attribute.001.Value -> Group Output.001.Guide Index
- Separate Components.Curve -> Capture Attribute.002.Geometry
- Spline Resolution.Resolution -> Capture Attribute.002.Value
- Set Spline Type.001.Curve -> Set Spline Resolution.001.Curve
- Set Spline Type.002.Curve -> Capture Attribute.Geometry
- Group.006.Curve ID -> Evaluate at Index.001.Value
- Evaluate at Index.001.Value -> Random Value.001.ID
- Group.007.Curve ID -> Random Value.ID
- Group Input.013.Guide Mask -> Group.003.Guide Mask
- Capture Attribute.002.Value -> Compare.004.A
- Compare.004.Result -> Switch.006.Switch
- Capture Attribute.002.Value -> Switch.006.False
- Group.005.Curves -> Set Spline Type.001.Curve
- Switch.006.Output -> Set Spline Resolution.001.Resolution
- Capture Attribute.002.Geometry -> Set Spline Type.002.Curve
- Compare.003.Result -> Accumulate Field.Value
- Accumulate Field.Total -> Sample Index.001.Value
- Capture Attribute.Geometry -> Sample Index.001.Geometry
- Sample Index.001.Value -> Boolean Math.002.Boolean
- Capture Attribute.001.Geometry -> Set Position.Geometry
- Group Input.012.Tip Spread -> Compare.A
- Compare.Result -> Switch.Switch
- Switch.001.Output -> Capture Attribute.001.Geometry
- Switch.003.Output -> Capture Attribute.001.Value
- Map Range.001.Result -> Switch.004.False
- Vector Math.010.Value -> Compare.005.A
- Compare.005.Result -> Switch.004.True
- Group Input.006.Distance Threshold -> Compare.005.B
- Group Input.006.Distance Threshold -> Compare.006.A
- Group Input.007.Distance Falloff -> Compare.007.A
- Compare.006.Result -> Boolean Math.Boolean
- Compare.007.Result -> Boolean Math.Boolean
- Boolean Math.Boolean -> Switch.004.Switch
- Separate Components.Grease Pencil -> Join Geometry.001.Geometry
- Group Input.005.Seed -> Hash Value.Value
