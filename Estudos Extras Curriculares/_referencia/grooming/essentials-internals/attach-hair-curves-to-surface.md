# Attach Hair Curves to Surface

Fonte: Essentials asset library do Blender 5.2.2 LTS (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- OUTPUT Surface UV Coordinate (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Surface UV coordinates at the attachment point
- OUTPUT Surface Normal (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Surface normal at the attachment point
- INPUT Geometry (Geometry, default None) — Input geometry (may include geometry other than curves)
- INPUT Surface Source (Menu, default Object) — Select the input source for the surface geometry.
- INPUT Surface Geometry (Geometry, default None) — Surface geometry to attach hair curves to
- INPUT Surface Object (Object, default None) — Surface Object to attach to
- INPUT Surface UV Map (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Surface UV map used for attachment
- INPUT Resting Surface (Bool, default False) — Use the surface's resting state to preserve stability under deformation
- INPUT Use Existing Attachment (Bool, default False) — Sample the surface UV map at the attachment point
- [painel] Snap to Surface
- INPUT Snap to Surface (Bool, default True) — Snap the root of each curve to the closest surface point
- INPUT Blend along Curve (Float, default 0.0, min 0.0, max 1.0) — Blend deformation along each curve from the root
- INPUT Align to Surface Normal (Bool, default False) — Align the curve to the surface normal (needs a guide as reference)

## Nodes (122)
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
- **Position** [GeometryNodeInputPosition]
- **Named Attribute.001** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_uv_coordinate
- **Capture Attribute.001** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Domain Size.003** [GeometryNodeAttributeDomainSize]
- **Compare.002** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Group Input.005** [NodeGroupInput]
- **Switch.007** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Sample Nearest Surface** [GeometryNodeSampleNearestSurface] {data_type=FLOAT_VECTOR}
- **Group** [GeometryNodeGroup] -> grupo 'Curve Root'
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
- **Switch.002** [GeometryNodeSwitch] {input_type=VECTOR}
- **Vector Math.002** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.005** [ShaderNodeVectorMath] {operation=SCALE}
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
- **Evaluate on Domain.002** [GeometryNodeFieldOnDomain] {data_type=QUATERNION, domain=CURVE}
- **Switch.006** [GeometryNodeSwitch] {input_type=VECTOR}
- **Evaluate on Domain.003** [GeometryNodeFieldOnDomain] {data_type=QUATERNION, domain=CURVE}
- **Switch.001** [GeometryNodeSwitch] {input_type=VECTOR}
- **Accumulate Field** [GeometryNodeAccumulateField] {data_type=INT, domain=POINT}
- **Sample Index.001** [GeometryNodeSampleIndex] {data_type=BOOLEAN, domain=CURVE}
    inputs livres: Index = 0
- **Named Attribute.002** [GeometryNodeInputNamedAttribute] {data_type=INT}
    inputs livres: Name = guide_curve_index
- **Sample Index** [GeometryNodeSampleIndex] {data_type=FLOAT_VECTOR, domain=CURVE}
- **Align Rotation to Vector** [FunctionNodeAlignRotationToVector]
    inputs livres: Factor = 1.0
- **Align Rotation to Vector.001** [FunctionNodeAlignRotationToVector]
    inputs livres: Factor = 1.0
- **Rotate Vector** [FunctionNodeRotateVector]
- **Rotate Vector.001** [FunctionNodeRotateVector]
- **Invert Rotation** [FunctionNodeInvertRotation]
- **Set Attachment Surface** [GeometryNodeGroup] -> grupo 'Set Attachment Surface'
    inputs livres: Mode = Geometry
- **Get Geometry Bundle** [GeometryNodeGetGeometryBundle]
    inputs livres: Remove = False
- **Separate Bundle** [NodeSeparateBundle]
- **Group Input.004** [NodeGroupInput]
- **Group.003** [GeometryNodeGroup] -> grupo 'Rest Surface'
- **Switch.005** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Group Input** [NodeGroupInput]
- **Switch.003** [GeometryNodeSwitch] {input_type=VECTOR}
- **Named Attribute.005** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_normal
- **Switch.011** [GeometryNodeSwitch] {input_type=VECTOR}
- **Named Attribute.006** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_uv_coordinate
- **Boolean Math** [FunctionNodeBooleanMath] {operation=AND}
- **Group Input.002** [NodeGroupInput]
- **Boolean Math.001** [FunctionNodeBooleanMath] {operation=NOT}
- **Named Attribute.007** [GeometryNodeInputNamedAttribute] {data_type=FLOAT_VECTOR}
    inputs livres: Name = surface_uv_coordinate
- **Menu Switch.001** [GeometryNodeMenuSwitch] {data_type=GEOMETRY}
- **Group Input.006** [NodeGroupInput]
- **Set Attachment Surface.001** [GeometryNodeGroup] -> grupo 'Set Attachment Surface'
    inputs livres: Mode = Geometry; Surface Object
- **Set Attachment Surface.002** [GeometryNodeGroup] -> grupo 'Set Attachment Surface'
    inputs livres: Mode = Object
- **Get Attachment Surface** [GeometryNodeGroup] -> grupo 'Get Attachment Surface'
- **Get Attachment Surface.001** [GeometryNodeGroup] -> grupo 'Get Attachment Surface'
- **Domain Size** [GeometryNodeAttributeDomainSize]
- **Compare.001** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Switch.012** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Separate Components** [GeometryNodeSeparateComponents]
- **Group Input.009** [NodeGroupInput]
- **Group Input.010** [NodeGroupInput]

## Ligacoes (156)
- Separate Bundle.surface_geometry -> Switch.007.False
- Group Input.005.Resting Surface -> Switch.007.Switch
- Switch.007.Output -> Sample Nearest Surface.Mesh
- Group.Root Position -> Sample Nearest Surface.Sample Position
- Get Attachment Surface.001.Surface UV Map -> Sample UV Surface.UV Map
- Position.Position -> Sample UV Surface.Value
- Switch.011.Output -> Sample UV Surface.Sample UV
- Capture Attribute.001.Geometry -> Set Position.001.Geometry
- Capture Attribute.Geometry -> Sample UV Surface.001.Mesh
- Switch.011.Output -> Sample UV Surface.001.Sample UV
- Get Attachment Surface.001.Surface UV Map -> Sample UV Surface.001.UV Map
- Normal.Normal -> Capture Attribute.Value
- Capture Attribute.Value -> Sample UV Surface.001.Value
- Sample UV Surface.Value -> Vector Math.Vector
- Group.001.Root Position -> Vector Math.Vector
- Vector Math.Vector -> Evaluate on Domain.Value
- Position.001.Position -> Vector Math.001.Vector
- Group.001.Root Position -> Vector Math.001.Vector
- Capture Attribute.Geometry -> Sample Index.Geometry
- Named Attribute.002.Attribute -> Sample Index.Index
- Position.002.Position -> Vector Math.004.Vector
- Vector Math.002.Vector -> Vector Math.003.Vector
- Switch.002.Output -> Vector Math.002.Vector
- Group.001.Root Position -> Vector Math.004.Vector
- Vector Math.004.Vector -> Vector Math.003.Vector
- Switch.005.Output -> Store Named Attribute.Geometry
- Menu Switch.001.Output -> Capture Attribute.002.Geometry
- Switch.011.Output -> Store Named Attribute.Value
- Sample Nearest Surface.Value -> Capture Attribute.002.New Attachment UV
- Switch.007.Output -> Capture Attribute.Geometry
- Capture Attribute.Value -> Sample UV Surface.003.Value
- Get Attachment Surface.001.Surface UV Map -> Sample UV Surface.003.UV Map
- Capture Attribute.Geometry -> Sample UV Surface.003.Mesh
- Named Attribute.001.Attribute -> Sample UV Surface.003.Sample UV
- Switch.003.Output -> Switch.001.True
- Accumulate Field.Total -> Sample Index.001.Value
- Sample Index.001.Value -> Switch.001.Switch
- Sample UV Surface.001.Value -> Sample Index.Value
- Rotate Vector.001.Vector -> Switch.002.True
- Vector Math.001.Vector -> Switch.002.False
- Group Input.003.Align to Surface Normal -> Switch.002.Switch
- Vector Math.005.Vector -> Set Position.001.Offset
- Switch.009.Output -> Group Output.Surface UV Coordinate
- Store Named Attribute.Geometry -> Switch.True
- Group Input.007.Use Existing Attachment -> Switch.Switch
- Switch.005.Output -> Switch.False
- Switch.Output -> Store Named Attribute.001.Geometry
- Capture Attribute.002.Geometry -> Capture Attribute.001.Geometry
- Capture Attribute.001.New Surface Normal -> Store Named Attribute.001.Value
- Switch.010.Output -> Group Output.Surface Normal
- Sample UV Surface.001.Value -> Capture Attribute.001.New Surface Normal
- Vector Math.003.Vector -> Vector Math.005.Vector
- Spline Parameter.Factor -> Map Range.Value
- Group Input.008.Blend along Curve -> Map Range.From Max
- Group Input.008.Blend along Curve -> Compare.A
- Compare.Result -> Switch.004.Switch
- Map Range.Result -> Switch.004.False
- Switch.004.Output -> Vector Math.005.Scale
- Sample Index.Value -> Switch.001.False
- Named Attribute.002.Exists -> Switch.006.Switch
- Vector Math.001.Vector -> Switch.006.False
- Store Named Attribute.001.Geometry -> Switch.008.False
- Menu Switch.001.Output -> Switch.008.True
- Switch.008.Output -> Group Output.Geometry
- Switch.011.Output -> Switch.009.False
- Capture Attribute.001.New Surface Normal -> Switch.010.False
- Domain Size.003.Face Count -> Compare.002.A
- Separate Bundle.surface_geometry -> Domain Size.003.Geometry
- Compare.002.Result -> Switch.008.Switch
- Compare.002.Result -> Switch.009.Switch
- Compare.002.Result -> Switch.010.Switch
- Named Attribute.003.Attribute -> Switch.009.True
- Named Attribute.004.Attribute -> Switch.010.True
- Capture Attribute.Geometry -> Sample UV Surface.Mesh
- Align Rotation to Vector.Rotation -> Evaluate on Domain.002.Value
- Sample UV Surface.001.Value -> Align Rotation to Vector.001.Vector
- Align Rotation to Vector.001.Rotation -> Evaluate on Domain.003.Value
- Vector Math.001.Vector -> Rotate Vector.Vector
- Rotate Vector.Vector -> Switch.006.True
- Evaluate on Domain.002.Value -> Rotate Vector.Rotation
- Switch.006.Output -> Rotate Vector.001.Vector
- Invert Rotation.Rotation -> Rotate Vector.001.Rotation
- Switch.001.Output -> Align Rotation to Vector.Vector
- Evaluate on Domain.003.Value -> Invert Rotation.Rotation
- Group Input.004.Surface Object -> Set Attachment Surface.Surface Object
- Group Input.010.Geometry -> Set Attachment Surface.Geometry
- Menu Switch.001.Output -> Get Geometry Bundle.Geometry
- Get Geometry Bundle.Bundle -> Separate Bundle.Bundle
- Separate Bundle.surface_geometry -> Group.003.Surface
- Group.003.Rest Surface -> Switch.007.True
- Set Position.001.Geometry -> Switch.005.True
- Capture Attribute.001.Geometry -> Switch.005.False
- Group Input.Snap to Surface -> Switch.005.Switch
- Evaluate on Domain.Value -> Vector Math.002.Vector
- Sample UV Surface.003.Value -> Switch.003.False
- Named Attribute.005.Exists -> Switch.003.Switch
- Named Attribute.005.Attribute -> Switch.003.True
- Capture Attribute.002.New Attachment UV -> Switch.011.True
- Group Input.002.Use Existing Attachment -> Boolean Math.Boolean
- Menu Switch.001.Output -> Sample Index.001.Geometry
- Boolean Math.Boolean -> Boolean Math.001.Boolean
- Boolean Math.001.Boolean -> Capture Attribute.002.Selection
- Capture Attribute.002.Selection -> Switch.011.Switch
- Named Attribute.006.Exists -> Boolean Math.Boolean
- Named Attribute.007.Exists -> Accumulate Field.Value
- Named Attribute.007.Attribute -> Switch.011.False
- Group Input.006.Surface Source -> Menu Switch.001.Menu
- Switch.012.Output -> Set Attachment Surface.001.Surface Geometry
- Group Input.004.Geometry -> Set Attachment Surface.001.Geometry
- Group Input.004.Surface UV Map -> Set Attachment Surface.001.Surface UV Map
- Group Input.004.Surface Geometry -> Set Attachment Surface.002.Surface Geometry
- Set Attachment Surface.Geometry -> Menu Switch.001.Attached
- Set Attachment Surface.001.Geometry -> Menu Switch.001.Input
- Set Attachment Surface.002.Geometry -> Menu Switch.001.Object
- Group Input.010.Geometry -> Get Attachment Surface.Geometry
- Get Attachment Surface.Surface Geometry -> Set Attachment Surface.Surface Geometry
- Get Attachment Surface.Surface UV Map -> Set Attachment Surface.Surface UV Map
- Menu Switch.001.Output -> Get Attachment Surface.001.Geometry
- Get Attachment Surface.001.Surface UV Map -> Sample Nearest Surface.Value
- Group Input.004.Surface Geometry -> Domain Size.Geometry
- Domain Size.Point Count -> Compare.001.A
- Compare.001.Result -> Switch.012.Switch
- Group Input.004.Geometry -> Separate Components.Geometry
- Separate Components.Mesh -> Switch.012.True
- Group Input.009.Geometry -> Set Attachment Surface.002.Geometry
- Group Input.009.Surface Object -> Set Attachment Surface.002.Surface Object
- Group Input.009.Surface UV Map -> Set Attachment Surface.002.Surface UV Map
- Group Input.004.Surface Geometry -> Switch.012.False
