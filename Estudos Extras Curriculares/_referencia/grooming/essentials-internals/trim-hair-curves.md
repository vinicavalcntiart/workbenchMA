# Trim Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- INPUT Geometry (Geometry, default None) — Input Geometry (May include other than curves)
- INPUT Scale Uniform (Bool, default False) — Scale each curve uniformly to reach the target length
- INPUT Length Factor (Float, default 1.0, min 0.0, max 10000.0) — Multiply the original length by a factor
- INPUT Replace Length (Bool, default True) — Use the length input to fully replace the original length
- INPUT Length (Float, default 1.0, min 0.0, max 3.4028234663852886e+38) — Target length for the operation
- INPUT Mask (Float, default 1.0, min 0.0, max 1.0) — Mask to blend overall effect
- INPUT Random Offset (Float, default 0.0, min 0.0, max 3.4028234663852886e+38) — Trim hair curves randomly up to a certain amount
- INPUT Pin at Parameter (Float, default 0.0, min 0.0, max 1.0) — Pin each curve at a certain point for the operation
- INPUT Seed (Int, default 0, min -10000, max 10000) — Random Seed for the operation

## Nodes (104)
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Group Input.002** [NodeGroupInput]
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Group Output** [NodeGroupOutput]
- **Switch.001** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Separate Components** [GeometryNodeSeparateComponents]
- **Group.006** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Set Position.002** [GeometryNodeSetPosition]
- **Group Input.009** [NodeGroupInput]
- **Position.001** [GeometryNodeInputPosition]
- **Vector Math.003** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.009** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.002** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Math.013** [ShaderNodeMath] {operation=DIVIDE}
- **Curve of Point** [GeometryNodeCurveOfPoint]
- **Mix.002** [ShaderNodeMix] {data_type=FLOAT, blend_type=MIX}
- **Math.016** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 1.0
- **Spline Length** [GeometryNodeSplineLength]
- **Sample Curve** [GeometryNodeSampleCurve] {data_type=FLOAT, mode=LENGTH}
- **Compare.001** [FunctionNodeCompare] {operation=LESS_THAN, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0
- **Compare** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
- **Group.003** [GeometryNodeGroup] -> grupo 'Curve Tip'
- **Group.007** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Math.001** [ShaderNodeMath] {operation=SUBTRACT}
- **Vector Math.010** [ShaderNodeVectorMath] {operation=SCALE}
    inputs livres: Scale = -1.0
- **Vector Math.001** [ShaderNodeVectorMath] {operation=SCALE}
- **Boolean Math** [FunctionNodeBooleanMath] {operation=AND}
- **Vector Math** [ShaderNodeVectorMath] {operation=SCALE}
- **Boolean Math.003** [FunctionNodeBooleanMath] {operation=AND}
- **Vector Math.004** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.005** [ShaderNodeVectorMath] {operation=SCALE}
- **Math.007** [ShaderNodeMath] {operation=MAXIMUM}
    inputs livres: Value = 0.0
- **Math.006** [ShaderNodeMath] {operation=MINIMUM}
- **Group.004** [GeometryNodeGroup] -> grupo 'Redistribute Curve Points'
    inputs livres: Factor = 1.0; Feature Awareness = False
- **Position** [GeometryNodeInputPosition]
- **Sample Curve.001** [GeometryNodeSampleCurve] {data_type=FLOAT, mode=FACTOR}
- **Vector Math.006** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.008** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.007** [ShaderNodeVectorMath] {operation=ADD}
- **Set Position.003** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Group Input.004** [NodeGroupInput]
- **Group.001** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Math.014** [ShaderNodeMath] {operation=DIVIDE}
- **Group.002** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Math.009** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.010** [ShaderNodeMath] {operation=SUBTRACT}
- **Math.011** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.005** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.004** [ShaderNodeMath] {operation=ADD}
- **Math.003** [ShaderNodeMath] {operation=MULTIPLY}
- **Group Input.003** [NodeGroupInput]
- **Math.008** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 1.0
- **Group Input.001** [NodeGroupInput]
- **Math.002** [ShaderNodeMath] {operation=ADD}
- **Math.015** [ShaderNodeMath] {operation=MAXIMUM}
    inputs livres: Value = 0.0001
- **Math.012** [ShaderNodeMath] {operation=MULTIPLY}
- **Switch** [GeometryNodeSwitch] {input_type=FLOAT}
- **Group Input.007** [NodeGroupInput]
- **Group Input.008** [NodeGroupInput]
- **Math** [ShaderNodeMath] {operation=MULTIPLY}
- **Random Value** [FunctionNodeRandomValue] {data_type=FLOAT}
    inputs livres: Min = -1.0; Max = 0.0
- **Group Input** [NodeGroupInput]
- **Group Input.006** [NodeGroupInput]
- **Group.005** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Mix.001** [ShaderNodeMix] {data_type=FLOAT, blend_type=MIX}
- **Group Input.005** [NodeGroupInput]
- **Hash Value** [FunctionNodeHashValue] {data_type=INT}
    inputs livres: Seed = 14699

## Ligacoes (126)
- Random Value.Value -> Math.Value
- Math.Value -> Math.002.Value
- Mix.001.Result -> Math.003.Value
- Math.008.Value -> Math.003.Value
- Math.004.Value -> Compare.A
- Capture Attribute.Value -> Compare.B
- Math.010.Value -> Compare.001.A
- Math.004.Value -> Math.006.Value
- Capture Attribute.Value -> Math.006.Value
- Math.010.Value -> Math.007.Value
- Capture Attribute.Value -> Math.001.Value
- Math.004.Value -> Math.001.Value
- Compare.Result -> Boolean Math.Boolean
- Math.001.Value -> Vector Math.Scale
- Compare.001.Result -> Boolean Math.003.Boolean
- Math.010.Value -> Vector Math.001.Scale
- Group Input.003.Pin at Parameter -> Math.008.Value
- Math.003.Value -> Math.004.Value
- Group Input.003.Pin at Parameter -> Math.005.Value
- Capture Attribute.Value -> Math.005.Value
- Math.005.Value -> Math.004.Value
- Group Input.003.Pin at Parameter -> Math.009.Value
- Capture Attribute.Value -> Math.009.Value
- Math.009.Value -> Math.010.Value
- Mix.001.Result -> Math.011.Value
- Math.011.Value -> Math.010.Value
- Group Input.003.Pin at Parameter -> Math.011.Value
- Group Input.Length Factor -> Math.012.Value
- Math.012.Value -> Math.002.Value
- Capture Attribute.Value -> Switch.False
- Switch.Output -> Math.012.Value
- Math.015.Value -> Mix.001.B
- Capture Attribute.Value -> Mix.001.A
- Group Input.001.Mask -> Mix.001.Factor
- Group Input.002.Scale Uniform -> Switch.001.Switch
- Curve of Point.Curve Index -> Sample Curve.Curve Index
- Capture Attribute.Geometry -> Sample Curve.Curves
- Sample Curve.Position -> Vector Math.002.Vector
- Math.007.Value -> Mix.002.A
- Math.006.Value -> Mix.002.B
- Curve of Point.Index in Curve -> Math.013.Value
- Vector Math.004.Vector -> Vector Math.002.Vector
- Vector Math.002.Vector -> Vector Math.003.Vector
- Vector Math.005.Vector -> Vector Math.003.Vector
- Vector Math.001.Vector -> Vector Math.004.Vector
- Vector Math.Vector -> Vector Math.005.Vector
- Boolean Math.003.Boolean -> Vector Math.004.Scale
- Boolean Math.Boolean -> Vector Math.005.Scale
- Capture Attribute.Geometry -> Set Position.002.Geometry
- Math.016.Value -> Math.013.Value
- Math.013.Value -> Mix.002.Factor
- Mix.002.Result -> Sample Curve.Length
- Vector Math.010.Vector -> Vector Math.001.Vector
- Capture Attribute.Geometry -> Sample Curve.001.Curves
- Position.Position -> Vector Math.006.Vector
- Sample Curve.001.Position -> Vector Math.006.Vector
- Vector Math.006.Vector -> Vector Math.008.Vector
- Vector Math.008.Vector -> Vector Math.007.Vector
- Sample Curve.001.Position -> Vector Math.007.Vector
- Vector Math.007.Vector -> Set Position.003.Position
- Capture Attribute.Geometry -> Set Position.003.Geometry
- Mix.001.Result -> Math.014.Value
- Math.014.Value -> Vector Math.008.Scale
- Math.002.Value -> Math.015.Value
- Group.004.Curves -> Switch.001.False
- Vector Math.009.Vector -> Set Position.002.Offset
- Position.001.Position -> Vector Math.009.Vector
- Vector Math.003.Vector -> Vector Math.009.Vector
- Separate Components.Mesh -> Join Geometry.Geometry
- Separate Components.Point Cloud -> Join Geometry.Geometry
- Separate Components.Volume -> Join Geometry.Geometry
- Separate Components.Instances -> Join Geometry.Geometry
- Join Geometry.Geometry -> Group Output.Geometry
- Switch.001.Output -> Join Geometry.Geometry
- Separate Components.Curve -> Capture Attribute.Geometry
- Spline Length.Point Count -> Math.016.Value
- Set Position.003.Geometry -> Switch.001.True
- Set Position.002.Geometry -> Group.004.Curves
- Group.003.Tip Selection -> Boolean Math.Boolean
- Group.003.Tip Direction -> Vector Math.Vector
- Group.007.Root Selection -> Boolean Math.003.Boolean
- Group.007.Root Direction -> Vector Math.010.Vector
- Group.001.Curve Index -> Sample Curve.001.Curve Index
- Group.002.Length -> Math.014.Value
- Group.005.Curve ID -> Random Value.ID
- Group.006.Length -> Capture Attribute.Value
- Group Input.004.Pin at Parameter -> Sample Curve.001.Factor
- Group Input.006.Random Offset -> Math.Value
- Group Input.007.Length -> Switch.True
- Group Input.008.Replace Length -> Switch.Switch
- Group Input.009.Geometry -> Separate Components.Geometry
- Separate Components.Grease Pencil -> Join Geometry.Geometry
- Group Input.005.Seed -> Hash Value.Value
- Hash Value.Hash -> Random Value.Seed
