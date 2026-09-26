# Set Hair Curve Profile

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- INPUT Geometry (Geometry, default None)
- INPUT Replace Radius (Bool, default True) — Replace the original radius
- INPUT Radius (Float, default 0.01, min 0.0, max 3.4028234663852886e+38) — Base radius to be set if 'Replace Radius' is enabled
- INPUT Shape (Float, default 0.5, min -1.0, max 1.0) — Shape of the radius along the curve
- INPUT Factor Min (Float, default 0.0, min 0.0, max 10000.0) — Factor of the radius at the minimum
- INPUT Factor Max (Float, default 1.0, min 0.0, max 10000.0) — Factor of the radius at the maximum

## Nodes (13)
- **Switch** [GeometryNodeSwitch] {input_type=FLOAT}
- **Radius** [GeometryNodeInputRadius]
- **Math.001** [ShaderNodeMath] {operation=MULTIPLY}
- **Set Curve Radius** [GeometryNodeSetCurveRadius]
- **Mix.002** [ShaderNodeMix] {data_type=FLOAT, blend_type=MIX}
- **Group.002** [GeometryNodeGroup] -> grupo '.shape_range'
    inputs livres: Min = 0.0; Max = 1.0; Base = 2.0
- **Group Input.001** [NodeGroupInput]
- **Math.006** [ShaderNodeMath] {operation=SUBTRACT}
    inputs livres: Value = 1.0
- **Spline Parameter.004** [GeometryNodeSplineParameter]
- **Group Input** [NodeGroupInput]
- **Group Output** [NodeGroupOutput]

## Ligacoes (16)
- Set Curve Radius.Curve -> Group Output.Geometry
- Group Input.Geometry -> Set Curve Radius.Curve
- Group Input.Replace Radius -> Switch.Switch
- Radius.Radius -> Switch.False
- Group Input.Radius -> Switch.True
- Math.001.Value -> Set Curve Radius.Radius
- Switch.Output -> Math.001.Value
- Group.002.Value -> Mix.002.Factor
- Group Input.Shape -> Group.002.Shape
- Math.006.Value -> Group.002.Value
- Spline Parameter.004.Factor -> Math.006.Value
- Mix.002.Result -> Math.001.Value
- Group Input.001.Factor Min -> Mix.002.A
- Group Input.001.Factor Max -> Mix.002.B
