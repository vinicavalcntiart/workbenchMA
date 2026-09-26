# Attach Hair Curves to Surface

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- OUTPUT Surface UV Coordinate (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Surface UV coordinates at the attachment point
- OUTPUT Surface Normal (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Surface normal at the attachment point
- INPUT Geometry (Geometry, default None) — Input Geometry (may include other than curves)
- INPUT Surface Input Type (Menu, default Object) — Select the input type for the surface geometry.
- INPUT Surface (Geometry, default None) — Surface geometry to attach hair curves to
- INPUT Surface (Object, default None) — Surface Object to attach to (needs to have matching transforms)
- INPUT Surface UV Map (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Surface UV map used for attachment
- INPUT Surface Rest Position (Bool, default False) — Set the surface mesh into its rest position before attachment
- INPUT Sample Attachment UV (Bool, default True) — Sample the surface UV map at the attachment point
- INPUT Snap to Surface (Bool, default True) — Snap the root of each curve to the closest surface point
- INPUT Align to Surface Normal (Bool, default True) — Align the curve to the surface normal (needs a guide as reference)
- INPUT Blend along Curve (Float, default 0.0, min 0.0, max 1.0) — Blend deformation along each curve from the root

## Nodes (100)
- **Group Output** [NodeGroupOutput]
- **Switch** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Store Named Attribute** [GeometryNodeStoreNamedAttribute] {data_type=FLOAT2, domain=CURVE}
    inputs livres: Name = surface_uv_coordinate
- **Group Input.007** [NodeGroupInput]
- **Store Named Attribute.001** [GeometryNodeStoreNamedAttribute] {data_type=FLOAT_VECTOR, domain=CURVE}
    inputs livres: Name = surface_normal
- **Named Attribute.004** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_normal
- **Named Attribute.003** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_uv_coordinate
- **Switch.008** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Switch.009** [GeometryNodeSwitch] {input_type=VECTOR}
- **Switch.010** [GeometryNodeSwitch] {input_type=VECTOR}
- **Set Position.001** [GeometryNodeSetPosition]
- **Group Input.009** [NodeGroupInput]
- **Position** [GeometryNodeInputPosition]
- **Named Attribute.001** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_uv_coordinate
- **Capture Attribute.001** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Group Input.004** [NodeGroupInput]
- **Object Info.001** [GeometryNodeObjectInfo] {transform_space=ORIGINAL}
    inputs livres: As Instance = False
- **Group Input.002** [NodeGroupInput]
- **Domain Size.003** [GeometryNodeAttributeDomainSize]
- **Compare.002** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Named Attribute** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = rest_position
- **Group Input.005** [NodeGroupInput]
- **Set Position** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Switch.007** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Group Input** [NodeGroupInput]
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Sample Nearest Surface** [GeometryNodeSampleNearestSurface] {data_type=FLOAT_VECTOR}
- **Group** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Group Input.001** [NodeGroupInput]
- **Normal** [GeometryNodeInputNormal]
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Sample UV Surface** [GeometryNodeSampleUVSurface] {data_type=FLOAT_VECTOR}
- **Sample UV Surface.003** [GeometryNodeSampleUVSurface] {data_type=FLOAT_VECTOR}
- **Sample UV Surface.001** [GeometryNodeSampleUVSurface] {data_type=FLOAT_VECTOR}
- **Group.001** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Position.001** [GeometryNodeInputPosition]
- **Vector Math** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.001** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.004** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.003** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Group Input.003** [NodeGroupInput]
- **Group Input.006** [NodeGroupInput]
- **Switch.003** [GeometryNodeSwitch] {input_type=VECTOR}
    inputs livres: False = (0.0, 0.0, 0.0)
- **Switch.002** [GeometryNodeSwitch] {input_type=VECTOR}
- **Vector Math.002** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.005** [ShaderNodeVectorMath] {operation=SCALE}
- **Boolean Math** [FunctionNodeBooleanMath] {operation=OR}
- **Spline Parameter** [GeometryNodeSplineParameter]
- **Group Input.008** [NodeGroupInput]
- **Map Range** [ShaderNodeMapRange] {data_type=FLOAT}
    inputs livres: From Min = 0.0; To Min = 1.0; To Max = 0.0
- **Compare** [FunctionNodeCompare] {operation=EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Switch.004** [GeometryNodeSwitch] {input_type=FLOAT}
    inputs livres: True = 1.0
- **Position.002** [GeometryNodeInputPosition]
- **Evaluate on Domain** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Evaluate on Domain.002** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Switch.006** [GeometryNodeSwitch] {input_type=VECTOR}
- **Vector Rotate** [ShaderNodeVectorRotate]
    inputs livres: Center = (0.0, 0.0, 0.0)
- **Vector Rotate.003** [ShaderNodeVectorRotate]
    inputs livres: Center = (0.0, 0.0, 0.0)
- **Align Euler to Vector.003** [FunctionNodeAlignEulerToVector]
    inputs livres: Factor = 1.0
- **Align Euler to Vector.002** [FunctionNodeAlignEulerToVector]
    inputs livres: Factor = 1.0
- **Evaluate on Domain.003** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Switch.001** [GeometryNodeSwitch] {input_type=VECTOR}
- **Accumulate Field** [GeometryNodeAccumulateField] {data_type=FLOAT, domain=POINT}
- **Sample Index.001** [GeometryNodeSampleIndex] {data_type=BOOLEAN, domain=CURVE}
    inputs livres: Index = 0
- **Named Attribute.002** [GeometryNodeInputNamedAttribute] {data_type=INT}
    inputs livres: Name = guide_curve_index
- **Sample Index** [GeometryNodeSampleIndex] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Menu Switch** [GeometryNodeMenuSwitch] {data_type=GEOMETRY}
- **Group Input.010** [NodeGroupInput]

## Ligacoes (122)
- Group Input.002.Surface -> Object Info.001.Object
- Group Input.001.Surface UV Map -> Sample Nearest Surface.Value
- Menu Switch.Output -> Set Position.Geometry
- Menu Switch.Output -> Switch.007.False
- Set Position.Geometry -> Switch.007.True
- Group Input.005.Surface Rest Position -> Switch.007.Switch
- Named Attribute.Attribute -> Set Position.Position
- Named Attribute.Exists -> Set Position.Selection
- Switch.007.Output -> Sample Nearest Surface.Mesh
- Group.Root Position -> Sample Nearest Surface.Sample Position
- Group Input.009.Surface UV Map -> Sample UV Surface.UV Map
- Position.Position -> Sample UV Surface.Value
- Capture Attribute.002.Value -> Sample UV Surface.Sample UV
- Capture Attribute.001.Geometry -> Set Position.001.Geometry
- Capture Attribute.Geometry -> Sample UV Surface.001.Mesh
- Capture Attribute.002.Value -> Sample UV Surface.001.Sample UV
- Group Input.009.Surface UV Map -> Sample UV Surface.001.UV Map
- Normal.Normal -> Capture Attribute.Value
- Capture Attribute.Value -> Sample UV Surface.001.Value
- Sample UV Surface.Value -> Vector Math.Vector
- Group.001.Root Position -> Vector Math.Vector
- Vector Math.Vector -> Evaluate on Domain.Value
- Position.001.Position -> Vector Math.001.Vector
- Group.001.Root Position -> Vector Math.001.Vector
- Switch.006.Output -> Vector Rotate.Vector
- Capture Attribute.Geometry -> Sample Index.Geometry
- Named Attribute.002.Attribute -> Sample Index.Index
- Position.002.Position -> Vector Math.004.Vector
- Vector Math.002.Vector -> Vector Math.003.Vector
- Switch.003.Output -> Vector Math.002.Vector
- Switch.002.Output -> Vector Math.002.Vector
- Vector Math.001.Vector -> Vector Rotate.003.Vector
- Evaluate on Domain.002.Value -> Vector Rotate.003.Rotation
- Evaluate on Domain.003.Value -> Vector Rotate.Rotation
- Group.001.Root Position -> Vector Math.004.Vector
- Vector Math.004.Vector -> Vector Math.003.Vector
- Set Position.001.Geometry -> Store Named Attribute.Geometry
- Group Input.Geometry -> Capture Attribute.002.Geometry
- Capture Attribute.002.Value -> Store Named Attribute.Value
- Sample Nearest Surface.Value -> Capture Attribute.002.Value
- Switch.007.Output -> Capture Attribute.Geometry
- Align Euler to Vector.003.Rotation -> Evaluate on Domain.002.Value
- Align Euler to Vector.002.Rotation -> Evaluate on Domain.003.Value
- Capture Attribute.Value -> Sample UV Surface.003.Value
- Group Input.009.Surface UV Map -> Sample UV Surface.003.UV Map
- Capture Attribute.Geometry -> Sample UV Surface.003.Mesh
- Named Attribute.001.Attribute -> Sample UV Surface.003.Sample UV
- Sample UV Surface.003.Value -> Switch.001.True
- Capture Attribute.002.Geometry -> Sample Index.001.Geometry
- Named Attribute.001.Exists -> Accumulate Field.Value
- Accumulate Field.Total -> Sample Index.001.Value
- Sample Index.001.Value -> Switch.001.Switch
- Sample UV Surface.001.Value -> Sample Index.Value
- Vector Rotate.Vector -> Switch.002.True
- Vector Math.001.Vector -> Switch.002.False
- Group Input.003.Align to Surface Normal -> Switch.002.Switch
- Vector Math.005.Vector -> Set Position.001.Offset
- Evaluate on Domain.Value -> Switch.003.True
- Group Input.006.Snap to Surface -> Switch.003.Switch
- Group Input.006.Snap to Surface -> Boolean Math.Boolean
- Group Input.003.Align to Surface Normal -> Boolean Math.Boolean
- Boolean Math.Boolean -> Set Position.001.Selection
- Switch.009.Output -> Group Output.Surface UV Coordinate
- Store Named Attribute.Geometry -> Switch.True
- Group Input.007.Sample Attachment UV -> Switch.Switch
- Set Position.001.Geometry -> Switch.False
- Switch.Output -> Store Named Attribute.001.Geometry
- Capture Attribute.002.Geometry -> Capture Attribute.001.Geometry
- Capture Attribute.001.Value -> Store Named Attribute.001.Value
- Switch.010.Output -> Group Output.Surface Normal
- Sample UV Surface.001.Value -> Capture Attribute.001.Value
- Vector Math.003.Vector -> Vector Math.005.Vector
- Spline Parameter.Factor -> Map Range.Value
- Group Input.008.Blend along Curve -> Map Range.From Max
- Group Input.008.Blend along Curve -> Compare.A
- Compare.Result -> Switch.004.Switch
- Map Range.Result -> Switch.004.False
- Switch.004.Output -> Vector Math.005.Scale
- Switch.001.Output -> Align Euler to Vector.003.Vector
- Sample Index.Value -> Switch.001.False
- Named Attribute.002.Exists -> Switch.006.Switch
- Vector Math.001.Vector -> Switch.006.False
- Vector Rotate.003.Vector -> Switch.006.True
- Store Named Attribute.001.Geometry -> Switch.008.False
- Group Input.Geometry -> Switch.008.True
- Switch.008.Output -> Group Output.Geometry
- Capture Attribute.002.Value -> Switch.009.False
- Capture Attribute.001.Value -> Switch.010.False
- Domain Size.003.Face Count -> Compare.002.A
- Menu Switch.Output -> Domain Size.003.Geometry
- Compare.002.Result -> Switch.008.Switch
- Compare.002.Result -> Switch.009.Switch
- Compare.002.Result -> Switch.010.Switch
- Named Attribute.003.Attribute -> Switch.009.True
- Named Attribute.004.Attribute -> Switch.010.True
- Sample UV Surface.001.Value -> Align Euler to Vector.002.Vector
- Capture Attribute.Geometry -> Sample UV Surface.Mesh
- Object Info.001.Geometry -> Menu Switch.Object
- Group Input.004.Surface -> Menu Switch.Geometry
- Group Input.010.Surface Input Type -> Menu Switch.Menu
