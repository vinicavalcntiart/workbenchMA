# Shrinkwrap Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- INPUT Geometry (Geometry, default None) — Input Geometry (May include other than curves)
- INPUT Surface Input Type (Menu, default Object) — Select the input type for the surface geometry.
- INPUT Surface (Object, default None) — Surface object used for shrinkwrap
- INPUT Surface (Geometry, default None) — Surface geometry used for shrinkwrap
- INPUT Factor (Float, default 1.0, min 0.0, max 1.0) — Factor
- INPUT Offset Distance (Float, default 0.0, min 0.0, max 3.4028234663852886e+38) — Distance from the surface used for shrinkwrap
- INPUT Above Surface (Float, default 0.5, min 0.0, max 1.0) — Blend shrinkwrap for points above the surface
- INPUT Smoothing Steps (Int, default 0, min 0, max 2147483647) — Amount of steps of smoothing applied after shrinkwrap
- INPUT Lock Roots (Bool, default True) — Lock the position of root points

## Nodes (96)
- **Separate Components** [GeometryNodeSeparateComponents]
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Position.001** [GeometryNodeInputPosition]
- **Vector Math.003** [ShaderNodeVectorMath] {operation=ADD}
- **Mix** [ShaderNodeMix] {data_type=VECTOR, blend_type=MIX}
- **Vector Math** [ShaderNodeVectorMath] {operation=SCALE}
- **Group Input.001** [NodeGroupInput]
- **Blur Attribute.002** [GeometryNodeBlurAttribute] {data_type=FLOAT}
    inputs livres: Weight = 1.0
- **Math.001** [ShaderNodeMath] {operation=ABSOLUTE}
- **Math** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 0.5
- **Math.002** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 0.5
- **Math.003** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = 2.0
- **Vector Math.008** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Position.002** [GeometryNodeInputPosition]
- **Group Input.002** [NodeGroupInput]
- **Vector Math.009** [ShaderNodeVectorMath] {operation=SCALE}
- **Vector Math.010** [ShaderNodeVectorMath] {operation=ADD}
- **Set Position** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Group Output** [NodeGroupOutput]
- **Domain Size.002** [GeometryNodeAttributeDomainSize]
- **Compare.003** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Group Input.007** [NodeGroupInput]
- **Switch.008** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Normal** [GeometryNodeInputNormal]
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Geometry Proximity** [GeometryNodeProximity] {target_element=FACES}
- **Sample Nearest Surface** [GeometryNodeSampleNearestSurface] {data_type=FLOAT_VECTOR}
- **Group Input.004** [NodeGroupInput]
- **Group** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Boolean Math.001** [FunctionNodeBooleanMath] {operation=NOT}
- **Boolean Math.004** [FunctionNodeBooleanMath] {operation=NOT}
- **Boolean Math.002** [FunctionNodeBooleanMath] {operation=OR}
- **Compare** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0
- **Group Input.003** [NodeGroupInput]
- **Blur Attribute.003** [GeometryNodeBlurAttribute] {data_type=FLOAT_VECTOR}
- **Switch** [GeometryNodeSwitch] {input_type=FLOAT}
- **Boolean Math.003** [FunctionNodeBooleanMath] {operation=AND}
- **Math.005** [ShaderNodeMath] {operation=MULTIPLY}
- **Compare.001** [FunctionNodeCompare] {operation=EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Compare.005** [FunctionNodeCompare] {operation=EQUAL, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0; Epsilon = 0.0
- **Map Range** [ShaderNodeMapRange] {data_type=FLOAT}
    inputs livres: From Min = 0.0; To Min = 1.0
- **Group Input.006** [NodeGroupInput]
- **Group Input.005** [NodeGroupInput]
- **Switch.001** [GeometryNodeSwitch] {input_type=FLOAT}
- **Math.006** [ShaderNodeMath] {operation=MAXIMUM}
    inputs livres: Value = 0.0
- **Boolean Math** [FunctionNodeBooleanMath] {operation=AND}
- **Position.003** [GeometryNodeInputPosition]
- **Vector Math.004** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.005** [ShaderNodeVectorMath] {operation=PROJECT}
- **Group Input** [NodeGroupInput]
- **Object Info.001** [GeometryNodeObjectInfo] {transform_space=RELATIVE}
    inputs livres: As Instance = False
- **Group Input.008** [NodeGroupInput]
- **Set Spline Type.001** [GeometryNodeCurveSplineType]
- **Compare.004** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Switch.006** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: True = 12
- **Set Spline Resolution.001** [GeometryNodeSetSplineResolution]
- **Set Spline Type.002** [GeometryNodeCurveSplineType]
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Spline Resolution** [GeometryNodeInputSplineResolution]
- **Vector Math.001** [ShaderNodeVectorMath] {operation=SUBTRACT}
- **Vector Math.002** [ShaderNodeVectorMath] {operation=DOT_PRODUCT}
- **Position** [GeometryNodeInputPosition]
- **Math.004** [ShaderNodeMath] {operation=MULTIPLY}
    inputs livres: Value = -1.0
- **Menu Switch** [GeometryNodeMenuSwitch] {data_type=GEOMETRY}
- **Group Input.009** [NodeGroupInput]

## Ligacoes (111)
- Menu Switch.Output -> Capture Attribute.Geometry
- Normal.Normal -> Capture Attribute.Value
- Capture Attribute.Geometry -> Sample Nearest Surface.Mesh
- Capture Attribute.Geometry -> Geometry Proximity.Geometry
- Sample Nearest Surface.Value -> Vector Math.Vector
- Set Spline Type.002.Curve -> Set Position.Geometry
- Domain Size.002.Point Count -> Compare.003.A
- Menu Switch.Output -> Domain Size.002.Geometry
- Geometry Proximity.Position -> Vector Math.001.Vector
- Position.Position -> Vector Math.001.Vector
- Vector Math.001.Vector -> Vector Math.002.Vector
- Sample Nearest Surface.Value -> Vector Math.002.Vector
- Vector Math.002.Value -> Compare.A
- Vector Math.Vector -> Vector Math.003.Vector
- Vector Math.004.Vector -> Vector Math.003.Vector
- Boolean Math.Boolean -> Blur Attribute.002.Value
- Mix.Result -> Blur Attribute.003.Value
- Math.Value -> Math.001.Value
- Math.003.Value -> Blur Attribute.003.Weight
- Blur Attribute.002.Value -> Math.Value
- Math.001.Value -> Math.002.Value
- Math.002.Value -> Math.003.Value
- Group Input.003.Smoothing Steps -> Blur Attribute.003.Iterations
- Position.002.Position -> Vector Math.008.Vector
- Position.002.Position -> Vector Math.010.Vector
- Vector Math.008.Vector -> Vector Math.009.Vector
- Vector Math.009.Vector -> Vector Math.010.Vector
- Group Input.002.Factor -> Vector Math.009.Scale
- Group Input.003.Smoothing Steps -> Blur Attribute.002.Iterations
- Compare.Result -> Boolean Math.Boolean
- Boolean Math.001.Boolean -> Boolean Math.002.Boolean
- Group.Root Selection -> Boolean Math.001.Boolean
- Blur Attribute.003.Value -> Vector Math.008.Vector
- Boolean Math.002.Boolean -> Boolean Math.Boolean
- Group Input.004.Lock Roots -> Boolean Math.004.Boolean
- Boolean Math.004.Boolean -> Boolean Math.002.Boolean
- Boolean Math.002.Boolean -> Set Position.Selection
- Geometry Proximity.Distance -> Switch.001.False
- Compare.Result -> Switch.001.Switch
- Math.004.Value -> Switch.001.True
- Geometry Proximity.Distance -> Math.004.Value
- Group Input.001.Offset Distance -> Vector Math.Scale
- Position.001.Position -> Mix.A
- Vector Math.003.Vector -> Mix.B
- Switch.001.Output -> Map Range.Value
- Switch.Output -> Mix.Factor
- Map Range.Result -> Math.005.Value
- Math.005.Value -> Switch.False
- Group Input.005.Offset Distance -> Compare.001.A
- Boolean Math.Boolean -> Switch.True
- Boolean Math.002.Boolean -> Math.005.Value
- Vector Math.010.Vector -> Set Position.Position
- Position.003.Position -> Vector Math.004.Vector
- Vector Math.001.Vector -> Vector Math.005.Vector
- Sample Nearest Surface.Value -> Vector Math.005.Vector
- Vector Math.005.Vector -> Vector Math.004.Vector
- Capture Attribute.Value -> Sample Nearest Surface.Value
- Separate Components.Mesh -> Join Geometry.Geometry
- Separate Components.Point Cloud -> Join Geometry.Geometry
- Separate Components.Volume -> Join Geometry.Geometry
- Separate Components.Instances -> Join Geometry.Geometry
- Set Spline Resolution.001.Curve -> Join Geometry.Geometry
- Group Input.Geometry -> Separate Components.Geometry
- Spline Resolution.Resolution -> Capture Attribute.002.Value
- Set Spline Type.001.Curve -> Set Spline Resolution.001.Curve
- Capture Attribute.002.Value -> Compare.004.A
- Compare.004.Result -> Switch.006.Switch
- Capture Attribute.002.Value -> Switch.006.False
- Switch.006.Output -> Set Spline Resolution.001.Resolution
- Capture Attribute.002.Geometry -> Set Spline Type.002.Curve
- Set Position.Geometry -> Set Spline Type.001.Curve
- Separate Components.Curve -> Capture Attribute.002.Geometry
- Compare.001.Result -> Boolean Math.003.Boolean
- Compare.005.Result -> Boolean Math.003.Boolean
- Group Input.006.Above Surface -> Compare.005.A
- Group Input.006.Above Surface -> Map Range.To Max
- Boolean Math.003.Boolean -> Switch.Switch
- Group Input.005.Offset Distance -> Math.006.Value
- Math.006.Value -> Map Range.From Max
- Join Geometry.Geometry -> Switch.008.False
- Compare.003.Result -> Switch.008.Switch
- Group Input.007.Geometry -> Switch.008.True
- Switch.008.Output -> Group Output.Geometry
- Group Input.008.Surface -> Object Info.001.Object
- Group Input.008.Surface -> Menu Switch.Geometry
- Object Info.001.Geometry -> Menu Switch.Object
- Group Input.009.Surface Input Type -> Menu Switch.Menu
- Separate Components.Grease Pencil -> Join Geometry.Geometry
