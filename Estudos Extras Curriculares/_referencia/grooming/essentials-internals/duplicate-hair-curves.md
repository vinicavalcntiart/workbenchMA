# Duplicate Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- OUTPUT Guide Index (Int, default 0, min -2147483648, max 2147483647) — Guide index map that was used for the operation
- INPUT Geometry (Geometry, default None) — Input Geometry (May include other than curves)
- INPUT Amount (Int, default 10, min 0, max 2147483647) — Amount of duplicates per curve
- INPUT Viewport Amount (Float, default 1.0, min 0.0, max 1.0) — Percentage of amount used for the viewport
- INPUT Radius (Float, default 0.1, min 0.0, max 3.4028234663852886e+38) — Radius in which the duplicate curves are offset from the guides
- INPUT Distribution Shape (Float, default 0.0, min -10.0, max 10.0) — Shape of distribution from center to the edge around the guide
- INPUT Tip Roundness (Float, default 0.0, min 0.0, max 1.0) — Offset of the curves to round the tip
- INPUT Even Thickness (Bool, default False) — Keep an even thickness of the distribution of duplicates
- INPUT Seed (Int, default 0, min -10000, max 10000) — Random Seed for the operation

## Nodes (87)
- **Group Input** [NodeGroupInput]
- **Group Output** [NodeGroupOutput]
- **Separate Components** [GeometryNodeSeparateComponents]
- **Math.053** [ShaderNodeMath] {operation=ARCCOSINE}
- **Math.055** [ShaderNodeMath] {operation=DIVIDE}
    inputs livres: Value = 1.5708
- **Math.056** [ShaderNodeMath] {operation=POWER}
    inputs livres: Value = 2.0
- **Group Input.006** [NodeGroupInput]
- **Separate XYZ.002** [ShaderNodeSeparateXYZ]
- **Math.054** [ShaderNodeMath] {operation=POWER}
- **Math.052** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = 6.2832
- **Combine XYZ.002** [ShaderNodeCombineXYZ]
    inputs livres: Y = 0.0; Z = 0.0
- **Math.059** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 0.5
- **Math.058** [ShaderNodeMath] {operation=POWER}
    inputs livres: Value = 2.0
- **Vector Rotate** [ShaderNodeVectorRotate]
    inputs livres: Center = (0.0, 0.0, 0.0)
- **Math.057** [ShaderNodeMath] {operation=ADD}
- **Group Input.007** [NodeGroupInput]
- **Combine XYZ** [ShaderNodeCombineXYZ]
    inputs livres: X = 0.0; Y = 0.0
- **Vector Math.014** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.013** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Set Position** [GeometryNodeSetPosition]
- **Set Position.001** [GeometryNodeSetPosition]
- **Normal** [GeometryNodeInputNormal]
- **Curve Tangent** [GeometryNodeInputTangent]
- **Separate XYZ** [ShaderNodeSeparateXYZ]
- **Vector Math.001** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.003** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.002** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.009** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.010** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math** [ShaderNodeVectorMath] {operation=CROSS_PRODUCT}
- **Group.001** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Evaluate on Domain.002** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Separate XYZ.001** [ShaderNodeSeparateXYZ]
- **Vector Math.011** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.005** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.007** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.008** [ShaderNodeVectorMath] {operation=CROSS_PRODUCT}
- **Evaluate at Index** [GeometryNodeFieldAtIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Vector Math.012** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.006** [ShaderNodeVectorMath] {operation=SCALE}
- **Evaluate on Domain.001** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=POINT}
- **Curve Tangent.001** [GeometryNodeInputTangent]
- **Normal.001** [GeometryNodeInputNormal]
- **Is Viewport** [GeometryNodeIsViewport]
- **Switch** [GeometryNodeSwitch] {input_type=INT}
- **ID** [GeometryNodeInputID]
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Set ID** [GeometryNodeSetID]
- **Store Named Attribute** [GeometryNodeStoreNamedAttribute] {data_type=INT, domain=CURVE}
    inputs livres: Name = guide_curve_index
- **Math** [ShaderNodeMath] {operation=MULTIPLY}
- **Group Input.002** [NodeGroupInput]
- **Group Input.004** [NodeGroupInput]
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=POINT}
    inputs livres: Value = True
- **Vector Math.004** [ShaderNodeVectorMath] {operation=SCALE}
- **Group Input.003** [NodeGroupInput]
- **Random Value.001** [FunctionNodeRandomValue] {data_type=FLOAT_VECTOR}
    inputs livres: Min = (0.0, 0.0, 0.0); Max = (1.0, 1.0, 1.0)
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Duplicate Elements** [GeometryNodeDuplicateElements] {domain=SPLINE}
- **Join Geometry.001** [GeometryNodeJoinGeometry]
- **Index** [GeometryNodeInputIndex]
- **Capture Attribute.001** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Switch.001** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Group** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Group Input.001** [NodeGroupInput]
- **Group Input.005** [NodeGroupInput]
- **Hash Value** [FunctionNodeHashValue] {data_type=INT}
- **Hash Value.001** [FunctionNodeHashValue] {data_type=INT}
    inputs livres: Seed = 296

## Ligacoes (107)
- Join Geometry.001.Geometry -> Group Output.Geometry
- Capture Attribute.Geometry -> Duplicate Elements.Geometry
- Capture Attribute.001.Geometry -> Capture Attribute.Geometry
- Random Value.001.Value -> Separate XYZ.002.Vector
- Math.052.Value -> Vector Rotate.Angle
- Combine XYZ.002.Vector -> Vector Rotate.Vector
- Separate XYZ.002.Y -> Math.052.Value
- Separate XYZ.002.X -> Math.053.Value
- Math.054.Value -> Combine XYZ.002.X
- Group.Curve ID -> Random Value.001.ID
- Vector Math.004.Vector -> Separate XYZ.Vector
- Store Named Attribute.Geometry -> Set Position.Geometry
- Curve Tangent.Tangent -> Vector Math.Vector
- Normal.Normal -> Vector Math.Vector
- Vector Math.Vector -> Vector Math.001.Vector
- Vector Math.001.Vector -> Vector Math.003.Vector
- Vector Math.002.Vector -> Vector Math.003.Vector
- Separate XYZ.X -> Vector Math.001.Scale
- Separate XYZ.Y -> Vector Math.002.Scale
- Normal.Normal -> Vector Math.002.Vector
- Index.Index -> Capture Attribute.001.Value
- Set ID.Geometry -> Store Named Attribute.Geometry
- Capture Attribute.Geometry -> Join Geometry.Geometry
- Capture Attribute.002.Geometry -> Join Geometry.Geometry
- Capture Attribute.001.Value -> Store Named Attribute.Value
- Group Input.004.Amount -> Switch.False
- Switch.Output -> Duplicate Elements.Amount
- Is Viewport.Is Viewport -> Switch.Switch
- Group Input.004.Amount -> Math.Value
- Math.Value -> Switch.True
- Group Input.002.Viewport Amount -> Math.Value
- ID.ID -> Capture Attribute.Value
- Vector Math.009.Vector -> Set Position.Offset
- Group Input.005.Even Thickness -> Switch.001.Switch
- Vector Math.007.Vector -> Vector Math.005.Vector
- Vector Math.006.Vector -> Vector Math.005.Vector
- Separate XYZ.001.X -> Vector Math.007.Scale
- Separate XYZ.001.Y -> Vector Math.006.Scale
- Evaluate on Domain.002.Value -> Set Position.001.Offset
- Curve Tangent.001.Tangent -> Vector Math.008.Vector
- Normal.001.Normal -> Vector Math.008.Vector
- Evaluate at Index.Value -> Evaluate on Domain.002.Value
- Vector Math.008.Vector -> Vector Math.007.Vector
- Normal.001.Normal -> Vector Math.006.Vector
- Evaluate on Domain.001.Value -> Separate XYZ.001.Vector
- Store Named Attribute.Geometry -> Set Position.001.Geometry
- Vector Math.011.Vector -> Evaluate at Index.Value
- Group.001.Root Index -> Evaluate at Index.Index
- Math.055.Value -> Math.054.Value
- Math.053.Value -> Math.055.Value
- Math.056.Value -> Math.054.Value
- Group Input.006.Distribution Shape -> Math.056.Value
- Vector Math.003.Vector -> Vector Math.009.Vector
- Separate XYZ.Z -> Vector Math.010.Scale
- Curve Tangent.Tangent -> Vector Math.010.Vector
- Vector Math.010.Vector -> Vector Math.009.Vector
- Vector Math.005.Vector -> Vector Math.011.Vector
- Vector Math.012.Vector -> Vector Math.011.Vector
- Separate XYZ.001.Z -> Vector Math.012.Scale
- Curve Tangent.001.Tangent -> Vector Math.012.Vector
- Vector Rotate.Vector -> Vector Math.013.Vector
- Vector Math.014.Vector -> Vector Math.013.Vector
- Math.057.Value -> Combine XYZ.Z
- Vector Math.013.Vector -> Vector Math.004.Vector
- Group Input.003.Radius -> Vector Math.004.Scale
- Math.058.Value -> Math.057.Value
- Math.059.Value -> Math.057.Value
- Math.054.Value -> Math.058.Value
- Combine XYZ.Vector -> Vector Math.014.Vector
- Group Input.007.Tip Roundness -> Vector Math.014.Scale
- Separate XYZ.002.Z -> Math.059.Value
- Set Position.001.Geometry -> Switch.001.False
- Set Position.Geometry -> Switch.001.True
- Capture Attribute.002.Value -> Set Position.Selection
- Capture Attribute.002.Value -> Set Position.001.Selection
- Join Geometry.Geometry -> Set ID.Geometry
- Duplicate Elements.Geometry -> Capture Attribute.002.Geometry
- Vector Math.004.Vector -> Evaluate on Domain.001.Value
- Separate Components.Mesh -> Join Geometry.001.Geometry
- Separate Components.Point Cloud -> Join Geometry.001.Geometry
- Separate Components.Volume -> Join Geometry.001.Geometry
- Separate Components.Instances -> Join Geometry.001.Geometry
- Switch.001.Output -> Join Geometry.001.Geometry
- Group Input.Geometry -> Separate Components.Geometry
- Separate Components.Curve -> Capture Attribute.001.Geometry
- Capture Attribute.001.Value -> Group Output.Guide Index
- Separate Components.Grease Pencil -> Join Geometry.001.Geometry
- Hash Value.Hash -> Set ID.ID
- Capture Attribute.Value -> Hash Value.Value
- Duplicate Elements.Duplicate Index -> Hash Value.Seed
- Group Input.001.Seed -> Hash Value.001.Value
- Hash Value.001.Hash -> Random Value.001.Seed
