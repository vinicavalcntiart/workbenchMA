# Generate Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- OUTPUT Curves (Geometry, default None)
- OUTPUT Surface Normal (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Normal direction of the surface mesh at the attachment point
- INPUT Surface (Geometry, default None) — Surface geometry for generation
- INPUT Surface (Object, default None) — Surface object for generation (needs matching transforms)
- INPUT Surface UV Map (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Surface UV map used for attachment
- INPUT Surface Rest Position (Bool, default False) — Set the surface mesh into its rest position before attachment
- INPUT Hair Length (Float, default 1.0, min 0.0, max 3.4028234663852886e+38) — Length of the generated hair curves
- INPUT Hair Material (Material, default None) — Material of the generated hair curves
- INPUT Control Points (Int, default 12, min 2, max 100000) — Amount of control points of the generated hair curves
- [painel] Distribution
- INPUT Distribution Method (Menu, default Random) — Use Poisson disk distribution method to keep a minimum distance
- INPUT Density (Float, default 10.0, min 0.0, max 10000.0) — Surface density of generated hair curves
- INPUT Density Mask (Float, default 1.0, min 0.0, max 1.0) — Factor applied on the density for curve distribution
- INPUT Mask Texture (Image, default None) — Discard points based on a mask texture after distribution
- INPUT Viewport Amount (Float, default 1.0, min 0.0, max 1.0) — Factor applied on the density for the viewport
- INPUT Seed (Int, default 0, min -2147483648, max 2147483647) — Random seed for the operation

## Nodes (78)
- **Separate Components** [GeometryNodeSeparateComponents]
- **Group Input.013** [NodeGroupInput]
- **Join Geometry.001** [GeometryNodeJoinGeometry]
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Store Named Attribute** [GeometryNodeStoreNamedAttribute] {data_type=FLOAT2, domain=CURVE}
    inputs livres: Name = surface_uv_coordinate
- **Group Input.012** [NodeGroupInput]
- **Group Input.018** [NodeGroupInput]
- **Resample Curve** [GeometryNodeResampleCurve]
    inputs livres: Mode = Count; Length = 0.1
- **Set Material** [GeometryNodeSetMaterial]
- **Curve Line** [GeometryNodeCurvePrimitiveLine] {mode=DIRECTION}
    inputs livres: Start = (0.0, 0.0, 0.0); Direction = (0.0, 0.0, 1.0)
- **Group Input** [NodeGroupInput]
- **Group Input.007** [NodeGroupInput]
- **Group Input.010** [NodeGroupInput]
- **Image Info** [GeometryNodeImageInfo]
    inputs livres: Frame = 0
- **Image Texture** [GeometryNodeImageTexture] {interpolation=Linear}
    inputs livres: Frame = 0
- **Group Input.008** [NodeGroupInput]
- **Switch.005** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Delete Geometry** [GeometryNodeDeleteGeometry] {domain=POINT, mode=ALL}
- **Random Value** [FunctionNodeRandomValue] {data_type=BOOLEAN}
- **Boolean Math** [FunctionNodeBooleanMath] {operation=NOT}
- **Capture Attribute.003** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Interpolate Curves** [GeometryNodeInterpolateCurves]
    inputs livres: Max Neighbors = 1
- **Switch** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Group Input.005** [NodeGroupInput]
- **Compare.002** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Domain Size.001** [GeometryNodeAttributeDomainSize]
- **Switch.007** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Group Input.011** [NodeGroupInput]
- **Object Info** [GeometryNodeObjectInfo] {transform_space=ORIGINAL}
    inputs livres: As Instance = False
- **Set Position** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Named Attribute** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = rest_position
- **Compare.001** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Capture Attribute.005** [GeometryNodeCaptureAttribute] {domain=POINT}
- **ID** [GeometryNodeInputID]
- **Set ID** [GeometryNodeSetID]
- **Curve of Point** [GeometryNodeCurveOfPoint]
- **Vector** [FunctionNodeInputVector]
- **Group Output** [NodeGroupOutput]
- **Group Input.002** [NodeGroupInput]
- **Math.009** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.008** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = 2.0
- **Math.011** [ShaderNodeMath] {operation=MULTIPLY}
- **Math.007** [ShaderNodeMath] {operation=SQRT}
- **Group Input.009** [NodeGroupInput]
- **Math.006** [ShaderNodeMath] {operation=DIVIDE}
    inputs livres: Value = 0.3
- **Group Input.003** [NodeGroupInput]
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Switch.004** [GeometryNodeSwitch] {input_type=FLOAT}
    inputs livres: False = 1.0
- **Group Input.004** [NodeGroupInput]
- **Is Viewport** [GeometryNodeIsViewport]
- **Group Input.001** [NodeGroupInput]
- **Clamp** [ShaderNodeClamp]
    inputs livres: Min = 0.0; Max = 1.0
- **Math.010** [ShaderNodeMath] {operation=MULTIPLY}
- **Switch.001** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Distribute Points on Faces.001** [GeometryNodeDistributePointsOnFaces] {distribute_method=RANDOM}
- **Distribute Points on Faces** [GeometryNodeDistributePointsOnFaces] {distribute_method=POISSON}
- **Switch.002** [GeometryNodeSwitch] {input_type=VECTOR}
- **Menu Switch** [GeometryNodeMenuSwitch] {data_type=GEOMETRY}
- **Group Input.006** [NodeGroupInput]
- **Hash Value** [FunctionNodeHashValue] {data_type=INT}

## Ligacoes (93)
- Switch.Output -> Distribute Points on Faces.Mesh
- Capture Attribute.005.Geometry -> Interpolate Curves.Points
- Switch.007.Output -> Set Position.Geometry
- Named Attribute.Attribute -> Set Position.Position
- Capture Attribute.002.Geometry -> Store Named Attribute.Geometry
- Math.011.Value -> Distribute Points on Faces.Density Max
- Math.006.Value -> Math.007.Value
- Group Input.002.Density -> Math.006.Value
- Math.007.Value -> Distribute Points on Faces.Distance Min
- Group Input.002.Density -> Math.008.Value
- Set Position.Geometry -> Switch.True
- Switch.007.Output -> Switch.False
- Group Input.005.Surface Rest Position -> Switch.Switch
- Math.009.Value -> Distribute Points on Faces.001.Density
- Distribute Points on Faces.Points -> Switch.001.True
- Distribute Points on Faces.001.Points -> Switch.001.False
- Menu Switch.Poisson Disk -> Switch.001.Switch
- Switch.Output -> Distribute Points on Faces.001.Mesh
- Curve Line.Curve -> Resample Curve.Curve
- Group Input.002.Density -> Math.009.Value
- Math.010.Value -> Math.009.Value
- ID.ID -> Capture Attribute.005.Value
- Group Input.003.Seed -> Distribute Points on Faces.001.Seed
- Group Input.003.Seed -> Distribute Points on Faces.Seed
- Is Viewport.Is Viewport -> Switch.004.Switch
- Capture Attribute.Geometry -> Capture Attribute.003.Geometry
- Group Input.007.Surface UV Map -> Capture Attribute.003.Value
- Group Input.008.Mask Texture -> Image Texture.Image
- Capture Attribute.003.Value -> Image Texture.Vector
- Image Texture.Color -> Random Value.Probability
- Capture Attribute.003.Geometry -> Delete Geometry.Geometry
- Random Value.Value -> Boolean Math.Boolean
- Boolean Math.Boolean -> Delete Geometry.Selection
- Group Input.008.Mask Texture -> Image Info.Image
- Image Info.Width -> Compare.001.A
- Delete Geometry.Geometry -> Switch.005.True
- Capture Attribute.003.Geometry -> Switch.005.False
- Compare.001.Result -> Switch.005.Switch
- Clamp.Result -> Switch.004.True
- Switch.004.Output -> Math.010.Value
- Math.008.Value -> Math.011.Value
- Switch.004.Output -> Math.011.Value
- Set Material.Geometry -> Interpolate Curves.Guide Curves
- Group Input.011.Surface -> Object Info.Object
- Resample Curve.Curve -> Set Material.Geometry
- Group Input.012.Hair Material -> Set Material.Material
- Named Attribute.Exists -> Set Position.Selection
- Domain Size.001.Point Count -> Compare.002.A
- Compare.002.Result -> Switch.007.Switch
- Switch.001.Output -> Capture Attribute.Geometry
- Capture Attribute.Value -> Group Output.Surface Normal
- Group Input.001.Viewport Amount -> Clamp.Value
- Group Input.018.Control Points -> Resample Curve.Count
- Group Input.013.Surface -> Join Geometry.001.Geometry
- Set ID.Geometry -> Join Geometry.001.Geometry
- Join Geometry.001.Geometry -> Group Output.Geometry
- Group Input.013.Surface -> Separate Components.Geometry
- Store Named Attribute.Geometry -> Set ID.Geometry
- Vector.Vector -> Interpolate Curves.Guide Up
- Capture Attribute.Value -> Interpolate Curves.Point Up
- Separate Components.Mesh -> Switch.007.False
- Group Input.Hair Length -> Curve Line.Length
- Switch.005.Output -> Capture Attribute.005.Geometry
- Set ID.Geometry -> Group Output.Curves
- Interpolate Curves.Curves -> Capture Attribute.002.Geometry
- Capture Attribute.003.Value -> Capture Attribute.002.Value
- Capture Attribute.002.Value -> Store Named Attribute.Value
- Object Info.Geometry -> Switch.007.True
- Separate Components.Mesh -> Domain Size.001.Geometry
- Group Input.004.Density Mask -> Math.010.Value
- Group Input.009.Density Mask -> Distribute Points on Faces.Density Factor
- Group Input.010.Seed -> Random Value.Seed
- Menu Switch.Poisson Disk -> Switch.002.Switch
- Distribute Points on Faces.001.Normal -> Switch.002.False
- Distribute Points on Faces.Normal -> Switch.002.True
- Switch.002.Output -> Capture Attribute.Value
- Group Input.006.Distribution Method -> Menu Switch.Menu
- Capture Attribute.005.Value -> Hash Value.Value
- Curve of Point.Index in Curve -> Hash Value.Seed
- Hash Value.Hash -> Set ID.ID
