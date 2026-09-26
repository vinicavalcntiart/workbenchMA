# Interpolate Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- OUTPUT Guide Index (Int, default 0, min -2147483648, max 2147483647) — Index of the main guide curve per curve
- OUTPUT Surface Normal (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Normal direction of the surface mesh at the attachment point
- INPUT Geometry (Geometry, default None) — Input Geometry (May include other than curves)
- INPUT Surface Input Type (Menu, default Object) — Select the input type for the surface geometry.
- INPUT Surface (Geometry, default None) — Surface geometry for generation
- INPUT Surface (Object, default None) — Surface object for generation (needs matching transforms)
- INPUT Surface UV Map (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Surface UV map used for attachment
- INPUT Surface Rest Position (Bool, default False) — Set the surface mesh into its rest position before attachment
- INPUT Follow Surface Normal (Bool, default False) — Align the interpolated curves to the surface normal
- INPUT Part by Mesh Islands (Bool, default True) — Use mesh islands of the surface geometry for parting
- INPUT Interpolation Guides (Int, default 4, min 1, max 2147483647) — Amount of guides to be used for interpolation per curve
- INPUT Distance to Guides (Float, default 0.0, min 0.0, max 3.4028234663852886e+38) — Distance around each guide to spawn interpolated curves
- [painel] Distribution
- INPUT Distribution Method (Menu, default Random)
- INPUT Density (Float, default 10.0, min 0.0, max 10000.0) — Surface density of generated hair curves
- INPUT Density Mask (Float, default 1.0, min 0.0, max 1.0) — Factor applied on the density for curve distribution
- INPUT Mask Texture (Image, default None) — Discard points based on a mask texture after distribution
- INPUT Viewport Amount (Float, default 1.0, min 0.0, max 1.0) — Factor applied on the density for the viewport
- INPUT Seed (Int, default 0, min -2147483648, max 2147483647) — Random seed for the operation

## Nodes (194)
- **Group Input** [NodeGroupInput]
- **Separate Components** [GeometryNodeSeparateComponents]
- **Join Geometry.001** [GeometryNodeJoinGeometry]
- **Capture Attribute.007** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Named Attribute** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = rest_position
- **Set Position** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Switch** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Group Input.005** [NodeGroupInput]
- **Group Input.013** [NodeGroupInput]
- **Object Info** [GeometryNodeObjectInfo] {transform_space=ORIGINAL}
    inputs livres: As Instance = False
- **Group Input.011** [NodeGroupInput]
- **Interpolate Curves.003** [GeometryNodeInterpolateCurves]
    inputs livres: Max Neighbors = 1
- **Delete Geometry** [GeometryNodeDeleteGeometry] {domain=POINT, mode=ALL}
- **Boolean Math** [FunctionNodeBooleanMath] {operation=NOT}
- **Image Texture** [GeometryNodeImageTexture] {interpolation=Linear}
    inputs livres: Frame = 0
- **Image Info** [GeometryNodeImageInfo]
    inputs livres: Frame = 0
- **Group Input.008** [NodeGroupInput]
- **Capture Attribute.003** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Switch.005** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Group Input.017** [NodeGroupInput]
- **Random Value** [FunctionNodeRandomValue] {data_type=BOOLEAN}
- **Compare.001** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Curve to Points** [GeometryNodeCurveToPoints] {mode=COUNT}
    inputs livres: Count = 1
- **Separate Geometry.001** [GeometryNodeSeparateGeometry] {domain=POINT}
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Store Named Attribute** [GeometryNodeStoreNamedAttribute] {data_type=FLOAT2, domain=CURVE}
    inputs livres: Name = surface_uv_coordinate
- **Math.005** [ShaderNodeMath] {operation=ADD}
- **Capture Attribute.006** [GeometryNodeCaptureAttribute] {domain=CURVE}
    inputs livres: Value = True
- **Compare.004** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
- **Sample UV Surface.002** [GeometryNodeSampleUVSurface] {data_type=FLOAT}
- **Random Value.005** [FunctionNodeRandomValue] {data_type=FLOAT}
    inputs livres: Min = 0.0; Max = 0.01; Seed = 0
- **Group.002** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Sample Nearest.008** [GeometryNodeSampleNearest] {domain=POINT}
- **Sample Index** [GeometryNodeSampleIndex] {data_type=BOOLEAN, domain=CURVE}
- **Group Input.009** [NodeGroupInput]
- **Group.001** [GeometryNodeGroup] -> grupo 'Hair Attachment Info'
- **Sample Nearest.003** [GeometryNodeSampleNearest] {domain=POINT}
- **Sample Nearest.004** [GeometryNodeSampleNearest] {domain=POINT}
- **Index.003** [GeometryNodeInputIndex]
- **Sample Index.001** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
- **Compare.006** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
- **Capture Attribute.004** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Normal** [GeometryNodeInputNormal]
- **Named Attribute.001** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_uv_coordinate
- **Sample UV Surface** [GeometryNodeSampleUVSurface] {data_type=FLOAT_VECTOR}
- **Group Input.007** [NodeGroupInput]
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Compare.007** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Accumulate Field** [GeometryNodeAccumulateField] {data_type=INT, domain=POINT}
- **Boolean Math.001** [FunctionNodeBooleanMath] {operation=AND}
- **Compare** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
- **Geometry Proximity** [GeometryNodeProximity] {target_element=POINTS}
- **Group Input.010** [NodeGroupInput]
- **Switch.002** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Delete Geometry.003** [GeometryNodeDeleteGeometry] {domain=POINT, mode=ALL}
- **Compare.008** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Sample Index.005** [GeometryNodeSampleIndex] {data_type=BOOLEAN, domain=POINT}
    inputs livres: Index = 0
- **Switch.001** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Switch.003** [GeometryNodeSwitch] {input_type=VECTOR}
- **Group Input.002** [NodeGroupInput]
- **Distribute Points on Faces** [GeometryNodeDistributePointsOnFaces] {distribute_method=POISSON}
- **Distribute Points on Faces.001** [GeometryNodeDistributePointsOnFaces] {distribute_method=RANDOM}
- **Switch.004** [GeometryNodeSwitch] {input_type=FLOAT}
    inputs livres: False = 1.0
- **Clamp** [ShaderNodeClamp]
    inputs livres: Min = 0.0; Max = 1.0
- **Group Input.001** [NodeGroupInput]
- **Is Viewport** [GeometryNodeIsViewport]
- **Math.010** [ShaderNodeMath] {operation=MULTIPLY}
- **Mesh Island** [GeometryNodeInputMeshIsland]
- **Group Input.012** [NodeGroupInput]
- **Capture Attribute.001** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Math.011** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.008** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = 2.0
- **Math.007** [ShaderNodeMath] {operation=SQRT}
- **Math.006** [ShaderNodeMath] {operation=DIVIDE}
    inputs livres: Value = 0.3
- **Math.009** [ShaderNodeMath] {operation=MULTIPLY}
- **Group Input.003** [NodeGroupInput]
- **Index** [GeometryNodeInputIndex]
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Sample Index.004** [GeometryNodeSampleIndex] {data_type=FLOAT_VECTOR, domain=POINT}
- **Position.001** [GeometryNodeInputPosition]
- **Set Position.002** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Group Input.016** [NodeGroupInput]
- **Switch.012** [GeometryNodeSwitch] {input_type=INT}
- **Sample Nearest.007** [GeometryNodeSampleNearest] {domain=POINT}
- **Vector Math.002** [ShaderNodeVectorMath] {operation=ADD}
- **Sample Nearest.005** [GeometryNodeSampleNearest] {domain=POINT}
- **Set Position.001** [GeometryNodeSetPosition]
- **Position** [GeometryNodeInputPosition]
- **Vector Math.001** [ShaderNodeVectorMath] {operation=SCALE}
    inputs livres: Vector = (100.0, 100.0, 100.0)
- **Delete Geometry.001** [GeometryNodeDeleteGeometry] {domain=POINT, mode=ALL}
- **Switch.008** [GeometryNodeSwitch] {input_type=VECTOR}
    inputs livres: False = (0.0, 0.0, 1.0)
- **Switch.009** [GeometryNodeSwitch] {input_type=VECTOR}
    inputs livres: False = (0.0, 0.0, 1.0)
- **Group Input.014** [NodeGroupInput]
- **Capture Attribute.005** [GeometryNodeCaptureAttribute] {domain=POINT}
- **ID** [GeometryNodeInputID]
- **Group Input.004** [NodeGroupInput]
- **Interpolate Curves** [GeometryNodeInterpolateCurves]
- **Capture Attribute.010** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Switch.015** [GeometryNodeSwitch] {input_type=INT}
- **Curve of Point** [GeometryNodeCurveOfPoint]
- **Sample Index.002** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
- **Sample Index.003** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
- **Sample Nearest.006** [GeometryNodeSampleNearest] {domain=POINT}
- **Index.001** [GeometryNodeInputIndex]
- **Group Input.015** [NodeGroupInput]
- **Switch.010** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: False = 0
- **Switch.011** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: False = 0
- **Set ID** [GeometryNodeSetID]
- **Group Output** [NodeGroupOutput]
- **Menu Switch** [GeometryNodeMenuSwitch] {data_type=GEOMETRY}
- **Group Input.018** [NodeGroupInput]
- **Switch.017** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Compare.005** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Domain Size.003** [GeometryNodeAttributeDomainSize]
- **Menu Switch.001** [GeometryNodeMenuSwitch] {data_type=GEOMETRY}
- **Group Input.019** [NodeGroupInput]
- **Hash Value** [FunctionNodeHashValue] {data_type=INT}

## Ligacoes (239)
- Capture Attribute.001.Geometry -> Distribute Points on Faces.Mesh
- Capture Attribute.010.Geometry -> Interpolate Curves.Points
- Switch.017.Output -> Set Position.Geometry
- Named Attribute.Attribute -> Set Position.Position
- Switch.009.Output -> Interpolate Curves.Point Up
- Capture Attribute.004.Geometry -> Sample UV Surface.Mesh
- Switch.008.Output -> Interpolate Curves.Guide Up
- Named Attribute.001.Attribute -> Sample UV Surface.Sample UV
- Math.005.Value -> Group Output.Guide Index
- Interpolate Curves.Curves -> Store Named Attribute.Geometry
- Capture Attribute.003.Value -> Store Named Attribute.Value
- Capture Attribute.007.Geometry -> Capture Attribute.002.Geometry
- Index.Index -> Capture Attribute.002.Value
- Capture Attribute.002.Value -> Math.005.Value
- Store Named Attribute.Geometry -> Join Geometry.Geometry
- Group Input.004.Interpolation Guides -> Interpolate Curves.Max Neighbors
- Math.011.Value -> Distribute Points on Faces.Density Max
- Math.006.Value -> Math.007.Value
- Group Input.002.Density -> Math.006.Value
- Math.007.Value -> Distribute Points on Faces.Distance Min
- Group Input.002.Density -> Math.008.Value
- Set Position.Geometry -> Switch.True
- Switch.017.Output -> Switch.False
- Group Input.005.Surface Rest Position -> Switch.Switch
- Math.009.Value -> Distribute Points on Faces.001.Density
- Distribute Points on Faces.Points -> Switch.001.True
- Distribute Points on Faces.001.Points -> Switch.001.False
- Menu Switch.001.Poisson Disk -> Switch.001.Switch
- Capture Attribute.001.Geometry -> Distribute Points on Faces.001.Mesh
- Group Input.002.Density -> Math.009.Value
- Math.010.Value -> Math.009.Value
- ID.ID -> Capture Attribute.005.Value
- Group Input.003.Seed -> Distribute Points on Faces.001.Seed
- Group Input.003.Seed -> Distribute Points on Faces.Seed
- Is Viewport.Is Viewport -> Switch.004.Switch
- Group Input.007.Surface UV Map -> Sample UV Surface.UV Map
- Join Geometry.Geometry -> Set ID.Geometry
- Capture Attribute.Geometry -> Capture Attribute.003.Geometry
- Group Input.008.Mask Texture -> Image Texture.Image
- Capture Attribute.003.Value -> Image Texture.Vector
- Image Texture.Color -> Random Value.Probability
- Capture Attribute.003.Geometry -> Delete Geometry.Geometry
- Group Input.003.Seed -> Random Value.Seed
- Random Value.Value -> Boolean Math.Boolean
- Boolean Math.Boolean -> Delete Geometry.Selection
- Group Input.008.Mask Texture -> Image Info.Image
- Image Info.Width -> Compare.001.A
- Delete Geometry.Geometry -> Switch.005.True
- Capture Attribute.003.Geometry -> Switch.005.False
- Compare.001.Result -> Switch.005.Switch
- Capture Attribute.006.Geometry -> Join Geometry.Geometry
- Clamp.Result -> Switch.004.True
- Switch.004.Output -> Math.010.Value
- Group Input.012.Density Mask -> Math.010.Value
- Group Input.012.Density Mask -> Distribute Points on Faces.Density Factor
- Math.008.Value -> Math.011.Value
- Switch.004.Output -> Math.011.Value
- Index.003.Index -> Compare.006.B
- Curve to Points.Points -> Sample Index.001.Geometry
- Sample Nearest.004.Index -> Sample Index.001.Index
- Sample Nearest.003.Index -> Sample Index.001.Value
- Sample Index.001.Value -> Compare.006.A
- Curve to Points.Points -> Sample Nearest.004.Geometry
- Switch.005.Output -> Sample Nearest.003.Geometry
- Separate Components.Curve -> Interpolate Curves.003.Guide Curves
- Delete Geometry.001.Geometry -> Interpolate Curves.003.Points
- Separate Components.Curve -> Interpolate Curves.Guide Curves
- Capture Attribute.005.Geometry -> Capture Attribute.010.Geometry
- Compare.006.Result -> Separate Geometry.001.Selection
- Separate Geometry.001.Inverted -> Capture Attribute.005.Geometry
- Group Input.011.Surface -> Object Info.Object
- Named Attribute.Exists -> Set Position.Selection
- Sample UV Surface.Value -> Switch.008.True
- Capture Attribute.Value -> Switch.009.True
- Group Input.014.Follow Surface Normal -> Switch.008.Switch
- Group Input.014.Follow Surface Normal -> Switch.009.Switch
- Switch.002.Output -> Capture Attribute.Geometry
- Capture Attribute.Value -> Group Output.Surface Normal
- Switch.Output -> Capture Attribute.001.Geometry
- Mesh Island.Island Index -> Capture Attribute.001.Value
- Switch.011.Output -> Interpolate Curves.Point Group ID
- Switch.005.Output -> Sample Nearest.006.Geometry
- Switch.005.Output -> Sample Index.002.Geometry
- Sample Nearest.006.Index -> Sample Index.002.Index
- Capture Attribute.001.Value -> Sample Index.002.Value
- Switch.010.Output -> Interpolate Curves.Guide Group ID
- Group Input.015.Part by Mesh Islands -> Switch.010.Switch
- Group Input.015.Part by Mesh Islands -> Switch.011.Switch
- Capture Attribute.010.Value -> Math.005.Value
- Delete Geometry.001.Geometry -> Set Position.001.Geometry
- Vector Math.001.Vector -> Set Position.001.Offset
- Capture Attribute.001.Value -> Vector Math.001.Scale
- Set Position.001.Geometry -> Sample Nearest.005.Geometry
- Sample Nearest.005.Index -> Switch.012.True
- Sample Nearest.007.Index -> Switch.012.False
- Delete Geometry.001.Geometry -> Sample Nearest.007.Geometry
- Switch.012.Output -> Capture Attribute.010.Value
- Group Input.016.Part by Mesh Islands -> Switch.012.Switch
- Vector Math.002.Vector -> Sample Nearest.005.Sample Position
- Position.Position -> Vector Math.002.Vector
- Vector Math.001.Vector -> Vector Math.002.Vector
- Index.001.Index -> Sample Index.003.Index
- Curve to Points.Points -> Sample Index.003.Geometry
- Sample Index.002.Value -> Sample Index.003.Value
- Sample Index.003.Value -> Switch.010.True
- Group Input.001.Viewport Amount -> Clamp.Value
- Capture Attribute.005.Value -> Switch.015.False
- Capture Attribute.006.Value -> Switch.015.Switch
- Interpolate Curves.003.Curves -> Capture Attribute.007.Geometry
- Capture Attribute.007.Value -> Switch.015.True
- Interpolate Curves.003.Closest Index -> Capture Attribute.007.Value
- Separate Geometry.001.Selection -> Set Position.002.Geometry
- Sample Nearest.004.Index -> Sample Index.004.Index
- Sample Index.004.Value -> Set Position.002.Position
- Position.001.Position -> Sample Index.004.Value
- Separate Components.Mesh -> Join Geometry.001.Geometry
- Separate Components.Point Cloud -> Join Geometry.001.Geometry
- Set ID.Geometry -> Join Geometry.001.Geometry
- Separate Components.Volume -> Join Geometry.001.Geometry
- Separate Components.Instances -> Join Geometry.001.Geometry
- Group Input.Geometry -> Separate Components.Geometry
- Capture Attribute.002.Geometry -> Capture Attribute.006.Geometry
- Group Input.009.Density Mask -> Sample UV Surface.002.Value
- Set Position.002.Geometry -> Delete Geometry.001.Geometry
- Switch.Output -> Sample UV Surface.002.Mesh
- Curve to Points.Points -> Sample Nearest.008.Geometry
- Sample Nearest.008.Index -> Sample Index.Index
- Separate Components.Curve -> Sample Index.Geometry
- Group Input.007.Surface UV Map -> Sample UV Surface.002.UV Map
- Sample Index.Value -> Delete Geometry.001.Selection
- Group.001.Attachment UV -> Sample UV Surface.002.Sample UV
- Sample UV Surface.002.Value -> Compare.004.B
- Random Value.005.Value -> Compare.004.A
- Compare.004.Result -> Sample Index.Value
- Group.002.Curve ID -> Random Value.005.ID
- Switch.001.Output -> Delete Geometry.003.Geometry
- Geometry Proximity.Distance -> Compare.A
- Group Input.010.Distance to Guides -> Compare.B
- Curve to Points.Points -> Geometry Proximity.Geometry
- Delete Geometry.003.Geometry -> Switch.002.False
- Group Input.010.Distance to Guides -> Compare.007.A
- Switch.001.Output -> Switch.002.True
- Compare.Result -> Boolean Math.001.Boolean
- Boolean Math.001.Boolean -> Delete Geometry.003.Selection
- Compare.007.Result -> Accumulate Field.Value
- Accumulate Field.Total -> Compare.008.A
- Compare.008.Result -> Sample Index.005.Value
- Switch.001.Output -> Sample Index.005.Geometry
- Sample Index.005.Value -> Switch.002.Switch
- Distribute Points on Faces.001.Normal -> Switch.003.False
- Distribute Points on Faces.Normal -> Switch.003.True
- Switch.003.Output -> Capture Attribute.Value
- Menu Switch.001.Poisson Disk -> Switch.003.Switch
- Switch.Output -> Capture Attribute.004.Geometry
- Normal.Normal -> Capture Attribute.004.Value
- Capture Attribute.004.Value -> Sample UV Surface.Value
- Separate Components.Curve -> Curve to Points.Curve
- Group Input.017.Surface UV Map -> Capture Attribute.003.Value
- Join Geometry.001.Geometry -> Group Output.Geometry
- Curve to Points.Points -> Sample Index.004.Geometry
- Compare.007.Result -> Boolean Math.001.Boolean
- Capture Attribute.001.Value -> Switch.011.True
- Object Info.Geometry -> Menu Switch.Object
- Group Input.018.Surface Input Type -> Menu Switch.Menu
- Menu Switch.Output -> Switch.017.False
- Domain Size.003.Point Count -> Compare.005.A
- Group Input.013.Surface -> Menu Switch.Geometry
- Separate Components.Mesh -> Switch.017.True
- Menu Switch.Output -> Domain Size.003.Geometry
- Compare.005.Result -> Switch.017.Switch
- Group Input.019.Distribution Method -> Menu Switch.001.Menu
- Separate Components.Grease Pencil -> Join Geometry.001.Geometry
- Switch.015.Output -> Hash Value.Value
- Curve of Point.Index in Curve -> Hash Value.Seed
- Hash Value.Hash -> Set ID.ID
- Switch.005.Output -> Separate Geometry.001.Geometry
