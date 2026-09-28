# Rotate Hair Curves

Fonte: Essentials asset library do Blender 5.2.2 LTS (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- INPUT Geometry (Geometry, default None) — Input geometry (may include geometry other than curves)
- INPUT Factor (Float, default 1.0, min 0.0, max 1.0) — Factor to influence the rotation angle
- INPUT Axis (Vector, default (0.0, 0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Rotation axis (default: tangent at root)
- INPUT Angle (Float, default 0.0, min -3.4028234663852886e+38, max 3.4028234663852886e+38) — Angle of rotation
- INPUT Random Offset (Float, default 0.3491, min 0.0, max 3.4028234663852886e+38) — Random offset to the rotation angle per curve
- INPUT Lock Ends (Bool, default False) — Lock rotation to the axis between the curve ends
- INPUT Seed (Int, default 0, min -10000, max 10000) — Random seed for the operation

## Nodes (44)
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Group Output** [NodeGroupOutput]
- **Compare.004** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Switch.004** [GeometryNodeSwitch] {input_type=INT}
    inputs livres: True = 12
- **Set Spline Type.001** [GeometryNodeCurveSplineType]
- **Set Spline Resolution** [GeometryNodeSetSplineResolution]
- **Set Position** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Math.001** [ShaderNodeMath] {operation=ADD}
- **Vector Rotate** [ShaderNodeVectorRotate]
- **Position** [GeometryNodeInputPosition]
- **Evaluate on Domain** [GeometryNodeFieldOnDomain] {data_type=FLOAT_VECTOR, domain=POINT}
- **Group Input** [NodeGroupInput]
- **Math** [ShaderNodeMath] {operation=MULTIPLY}
- **Group Input.006** [NodeGroupInput]
- **Group.001** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Group Input.004** [NodeGroupInput]
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Set Spline Type** [GeometryNodeCurveSplineType]
- **Spline Resolution** [GeometryNodeInputSplineResolution]
- **Switch.002** [GeometryNodeSwitch] {input_type=VECTOR}
- **Compare.002** [FunctionNodeCompare] {operation=EQUAL, data_type=VECTOR, mode=ELEMENT}
    inputs livres: B = (0.0, 0.0, 0.0); Epsilon = 0.0
- **Group.005** [GeometryNodeGroup] -> grupo 'Curve Root'
- **Group Input.002** [NodeGroupInput]
- **Group Input.005** [NodeGroupInput]
- **Group.003** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Evaluate on Domain.002** [GeometryNodeFieldOnDomain] {data_type=BOOLEAN, domain=CURVE}
- **Random Value** [FunctionNodeRandomValue] {data_type=FLOAT}
    inputs livres: Min = -0.5; Max = 0.5
- **Group Input.003** [NodeGroupInput]
- **Group.004** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Evaluate on Domain.001** [GeometryNodeFieldOnDomain] {data_type=FLOAT, domain=CURVE}
- **Math.002** [ShaderNodeMath] {operation=MULTIPLY}
- **Switch.003** [GeometryNodeSwitch] {input_type=VECTOR}
- **Group Input.001** [NodeGroupInput]
- **Hash Value** [FunctionNodeHashValue] {data_type=INT}
    inputs livres: Seed = -87614
- **Get Geometry Component** [GeometryNodeGetGeometryComponent]
    inputs livres: Type = Curve; Remove = True

## Ligacoes (42)
- Set Spline Type.Curve -> Set Position.Geometry
- Vector Rotate.Vector -> Set Position.Position
- Position.Position -> Vector Rotate.Vector
- Math.Value -> Vector Rotate.Angle
- Evaluate on Domain.Value -> Vector Rotate.Center
- Switch.003.Output -> Compare.002.A
- Switch.003.Output -> Switch.002.False
- Compare.002.Result -> Switch.002.Switch
- Math.001.Value -> Math.Value
- Evaluate on Domain.001.Value -> Math.002.Value
- Math.002.Value -> Math.001.Value
- Random Value.Value -> Evaluate on Domain.001.Value
- Group.004.Curve ID -> Random Value.ID
- Switch.002.Output -> Vector Rotate.Axis
- Evaluate on Domain.002.Value -> Switch.003.Switch
- Group.003.Direction -> Switch.003.True
- Group Input.002.Lock Ends -> Evaluate on Domain.002.Value
- Set Spline Resolution.Curve -> Join Geometry.Geometry
- Join Geometry.Geometry -> Group Output.Geometry
- Spline Resolution.Resolution -> Capture Attribute.Value
- Capture Attribute.Geometry -> Set Spline Type.Curve
- Set Position.Geometry -> Set Spline Type.001.Curve
- Set Spline Type.001.Curve -> Set Spline Resolution.Curve
- Group.001.Root Position -> Evaluate on Domain.Value
- Group.005.Root Direction -> Switch.002.True
- Capture Attribute.Value -> Compare.004.A
- Compare.004.Result -> Switch.004.Switch
- Capture Attribute.Value -> Switch.004.False
- Switch.004.Output -> Set Spline Resolution.Resolution
- Group Input.003.Random Offset -> Math.002.Value
- Group Input.004.Angle -> Math.001.Value
- Group Input.005.Axis -> Switch.003.False
- Group Input.006.Factor -> Math.Value
- Group Input.001.Seed -> Hash Value.Value
- Hash Value.Hash -> Random Value.Seed
- Get Geometry Component.Geometry -> Join Geometry.Geometry
- Get Geometry Component.Component -> Capture Attribute.Geometry
- Group Input.Geometry -> Get Geometry Component.Geometry
