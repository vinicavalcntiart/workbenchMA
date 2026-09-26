# Blend Hair Curves

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- INPUT Geometry (Geometry, default None) — Input Geometry (may include other than curves)
- INPUT Factor (Float, default 1.0, min 0.0, max 1.0) — Factor to blend overall effect
- INPUT Blend Radius (Float, default 0.05, min 0.0, max 3.4028234663852886e+38) — Radius to select neighbors for blending
- INPUT Blend Neighbors (Int, default 10, min 1, max 2147483647) — Amount of neighbors used for blending
- INPUT Preserve Length (Bool, default False) — Preserve each curve's length during deformation

## Nodes (36)
- **Position** [GeometryNodeInputPosition]
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Group Output** [NodeGroupOutput]
- **Separate Components** [GeometryNodeSeparateComponents]
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Group Input.005** [NodeGroupInput]
- **Group Input** [NodeGroupInput]
- **Interpolate Curves.002** [GeometryNodeInterpolateCurves]
- **Group Input.003** [NodeGroupInput]
- **Curve to Points.002** [GeometryNodeCurveToPoints] {mode=COUNT, label='Root Points'}
    inputs livres: Count = 1
- **Merge by Distance** [GeometryNodeMergeByDistance]
    inputs livres: Mode = All
- **Interpolate Curves.003** [GeometryNodeInterpolateCurves]
- **Spline Parameter.001** [GeometryNodeSplineParameter]
- **Group.001** [GeometryNodeGroup] -> grupo 'Curve Info'
- **Sample Curve.001** [GeometryNodeSampleCurve] {data_type=FLOAT, mode=FACTOR}
- **Set Position.001** [GeometryNodeSetPosition]
    inputs livres: Offset = (0.0, 0.0, 0.0)
- **Position.002** [GeometryNodeInputPosition]
- **Group Input.004** [NodeGroupInput]
- **Mix.001** [ShaderNodeMix] {data_type=VECTOR, blend_type=MIX}
- **Group** [GeometryNodeGroup] -> grupo 'Restore Curve Segment Length'
    inputs livres: Factor = 1.0; Pin at Parameter = 0.0

## Ligacoes (45)
- Curve to Points.002.Points -> Merge by Distance.Geometry
- Capture Attribute.Geometry -> Curve to Points.002.Curve
- Interpolate Curves.003.Curves -> Interpolate Curves.002.Guide Curves
- Curve to Points.002.Points -> Interpolate Curves.002.Points
- Group Input.004.Factor -> Mix.001.Factor
- Mix.001.Result -> Set Position.001.Position
- Spline Parameter.001.Factor -> Sample Curve.001.Factor
- Group.001.Curve Index -> Sample Curve.001.Curve Index
- Sample Curve.001.Position -> Mix.001.B
- Capture Attribute.Geometry -> Set Position.001.Geometry
- Interpolate Curves.002.Curves -> Sample Curve.001.Curves
- Position.002.Position -> Mix.001.A
- Capture Attribute.Geometry -> Interpolate Curves.003.Guide Curves
- Merge by Distance.Geometry -> Interpolate Curves.003.Points
- Group Input.003.Blend Neighbors -> Interpolate Curves.003.Max Neighbors
- Group Input.003.Blend Neighbors -> Interpolate Curves.002.Max Neighbors
- Group Input.003.Blend Radius -> Merge by Distance.Distance
- Set Position.001.Geometry -> Group.Curves
- Group Input.Preserve Length -> Group.Selection
- Position.Position -> Capture Attribute.Value
- Capture Attribute.Value -> Group.Reference Position
- Separate Components.Mesh -> Join Geometry.Geometry
- Separate Components.Point Cloud -> Join Geometry.Geometry
- Separate Components.Volume -> Join Geometry.Geometry
- Separate Components.Instances -> Join Geometry.Geometry
- Group.Curves -> Join Geometry.Geometry
- Join Geometry.Geometry -> Group Output.Geometry
- Separate Components.Curve -> Capture Attribute.Geometry
- Group Input.005.Geometry -> Separate Components.Geometry
- Separate Components.Grease Pencil -> Join Geometry.Geometry
