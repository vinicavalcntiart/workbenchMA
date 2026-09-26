# Displace Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- INPUT Geometry (Geometry, default None) — Input Geometry (may include other than curves)
- INPUT Factor (Float, default 1.0, min 0.0, max 1.0) — Factor to scale overall displacement
- INPUT Shape (Float, default 0.5, min -1.0, max 1.0) — Shape of the influence along curves (0=constant, 0.5=linear)
- INPUT Object Space (Object, default None) — Object used to define the displacement space
- INPUT Displace Vector (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Vector for displacement
- [painel] Surface Normal
- INPUT Surface Normal (Bool, default False)
- INPUT Surface Input Type (Menu, default Object) — Select the input type for the surface geometry.
- INPUT Surface (Geometry, default None) — Surface geometry used to sample the normal for displacement
- INPUT Surface (Object, default None) — Surface object used to sample the normal for displacement
- INPUT Surface UV Map (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Surface UV map used to sample the normal for displacement
- INPUT Surface Normal Distance (Float, default 0.0, min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Amount of displacemement along the surface normal

## Nodes (55)
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Group Output** [NodeGroupOutput]
- **Separate Components** [GeometryNodeSeparateComponents]
- **Group Input** [NodeGroupInput]
- **Compare.003** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Domain Size.001** [GeometryNodeAttributeDomainSize]
- **Switch.001** [GeometryNodeSwitch] {input_type=VECTOR}
- **Group Input.001** [NodeGroupInput]
- **Object Info** [GeometryNodeObjectInfo] {transform_space=RELATIVE}
    inputs livres: As Instance = True
- **Group Input.008** [NodeGroupInput]
- **Group Input.005** [NodeGroupInput]
- **Group Input.006** [NodeGroupInput]
- **Group Input.002** [NodeGroupInput]
- **Spline Parameter** [GeometryNodeSplineParameter]
- **Group Input.007** [NodeGroupInput]
- **Group.001** [GeometryNodeGroup] -> grupo '.shape_range'
    inputs livres: Min = 0.0; Max = 1.0; Base = 2.0
- **Vector Math.002** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.001** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.003** [ShaderNodeVectorMath] {operation=ADD}
- **Group** [GeometryNodeGroup] -> grupo 'Hair Attachment Info'
- **Vector Math.004** [ShaderNodeVectorMath] {operation=SCALE}
- **Group Input.003** [NodeGroupInput]
- **Object Info.001** [GeometryNodeObjectInfo] {transform_space=ORIGINAL}
    inputs livres: As Instance = False
- **Group Input.009** [NodeGroupInput]
- **Vector Math** [ShaderNodeVectorMath] {operation=MULTIPLY}
- **Vector Rotate** [ShaderNodeVectorRotate]
    inputs livres: Center = (0.0, 0.0, 0.0)
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Spline Resolution** [GeometryNodeInputSplineResolution]
- **Set Spline Type** [GeometryNodeCurveSplineType]
- **Set Spline Resolution.001** [GeometryNodeSetSplineResolution]
- **Set Spline Type.001** [GeometryNodeCurveSplineType]
- **Set Position** [GeometryNodeSetPosition]
- **Compare.004** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Switch.004** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: True = 12
- **Menu Switch** [GeometryNodeMenuSwitch] {data_type=GEOMETRY}
- **Group Input.004** [NodeGroupInput]
- **Switch** [GeometryNodeSwitch] {input_type=VECTOR}
    inputs livres: False = (0.0, 0.0, 0.0)
- **Group Input.010** [NodeGroupInput]

## Ligacoes (59)
- Group Input.001.Object Space -> Object Info.Object
- Spline Parameter.Factor -> Group.001.Value
- Vector Math.Vector -> Vector Rotate.Vector
- Object Info.Rotation -> Vector Rotate.Rotation
- Vector Math.002.Vector -> Set Position.Offset
- Object Info.Scale -> Vector Math.Vector
- Vector Math.001.Vector -> Vector Math.002.Vector
- Group Input.002.Factor -> Vector Math.002.Scale
- Group Input.003.Surface -> Object Info.001.Object
- Group Input.005.Surface UV Map -> Group.Surface UV Map
- Switch.001.Output -> Vector Math.003.Vector
- Group Input.007.Shape -> Group.001.Shape
- Group Input.008.Displace Vector -> Vector Math.Vector
- Group.Surface Normal -> Vector Math.004.Vector
- Switch.Output -> Vector Math.003.Vector
- Group Input.006.Surface Normal Distance -> Vector Math.004.Scale
- Object Info.Geometry -> Domain Size.001.Geometry
- Domain Size.001.Instance Count -> Compare.003.A
- Vector Rotate.Vector -> Switch.001.True
- Compare.003.Result -> Switch.001.Switch
- Group Input.008.Displace Vector -> Switch.001.False
- Group.001.Value -> Vector Math.001.Scale
- Separate Components.Mesh -> Join Geometry.Geometry
- Separate Components.Point Cloud -> Join Geometry.Geometry
- Separate Components.Volume -> Join Geometry.Geometry
- Separate Components.Instances -> Join Geometry.Geometry
- Set Spline Resolution.001.Curve -> Join Geometry.Geometry
- Separate Components.Curve -> Capture Attribute.002.Geometry
- Spline Resolution.Resolution -> Capture Attribute.002.Value
- Set Spline Type.001.Curve -> Set Spline Resolution.001.Curve
- Capture Attribute.002.Geometry -> Set Spline Type.Curve
- Set Position.Geometry -> Set Spline Type.001.Curve
- Capture Attribute.002.Value -> Compare.004.A
- Compare.004.Result -> Switch.004.Switch
- Capture Attribute.002.Value -> Switch.004.False
- Switch.004.Output -> Set Spline Resolution.001.Resolution
- Group Input.Geometry -> Separate Components.Geometry
- Join Geometry.Geometry -> Group Output.Geometry
- Set Spline Type.Curve -> Set Position.Geometry
- Vector Math.003.Vector -> Vector Math.001.Vector
- Separate Components.Grease Pencil -> Join Geometry.Geometry
- Object Info.001.Geometry -> Menu Switch.Object
- Group Input.009.Surface -> Menu Switch.Geometry
- Menu Switch.Output -> Group.Surface Geometry
- Group Input.004.Surface Input Type -> Menu Switch.Menu
- Vector Math.004.Vector -> Switch.True
- Group Input.010.Surface Normal -> Switch.Switch
