# Create Guide Index Map

Fonte: Essentials asset library do Blender 5.0.1 (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- OUTPUT Guide Curves (Geometry, default None)
- OUTPUT Guide Index (Int, default 0, min 0, max 1)
- OUTPUT Guide Selection (Bool, default False)
- INPUT Geometry (Geometry, default None)
- INPUT Guides (Geometry, default None) — Guide curves or points used for the selection of guide curves
- INPUT Guide Distance (Float, default 0.0, min 0.0, max 3.4028234663852886e+38) — Minimum distance between two guides
- INPUT Guide Mask (Float, default 1.0, min 0.0, max 1.0) — Mask for which curves are eligible to be selected as guides
- INPUT Group ID (Int, default 0, min -2147483648, max 2147483647) — ID to group curves together for guide map creation

## Nodes (102)
- **Set Position.002** [GeometryNodeSetPosition]
- **Switch.002** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Set Position** [GeometryNodeSetPosition]
- **Vector Math.003** [ShaderNodeVectorMath] {operation=SCALE}
    inputs livres: Vector = (100.0, 100.0, 100.0)
- **Vector Math.004** [ShaderNodeVectorMath] {operation=SCALE}
    inputs livres: Scale = -1.0
- **Merge by Distance** [GeometryNodeMergeByDistance]
    inputs livres: Mode = All
- **Merge by Distance.001** [GeometryNodeMergeByDistance]
    inputs livres: Mode = All
- **Group Input.001** [NodeGroupInput]
- **Compare.004** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=FLOAT, mode=ELEMENT}
    inputs livres: B = 0.0
- **Group Input** [NodeGroupInput]
- **Separate Components.001** [GeometryNodeSeparateComponents]
- **Group Input.003** [NodeGroupInput]
- **Capture Attribute.003** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Group Input.010** [NodeGroupInput]
- **Capture Attribute.006** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Capture Attribute.001** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Curve to Points** [GeometryNodeCurveToPoints] {mode=COUNT}
    inputs livres: Count = 1
- **Index.001** [GeometryNodeInputIndex]
- **Curve to Points.001** [GeometryNodeCurveToPoints] {mode=COUNT}
    inputs livres: Count = 1
- **Group Input.004** [NodeGroupInput]
- **Mesh to Points** [GeometryNodeMeshToPoints] {mode=VERTICES}
    inputs livres: Radius = 0.05
- **Separate Components** [GeometryNodeSeparateComponents]
- **Join Geometry** [GeometryNodeJoinGeometry]
- **Domain Size** [GeometryNodeAttributeDomainSize]
- **Compare.003** [FunctionNodeCompare] {operation=GREATER_THAN, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Group Input.008** [NodeGroupInput]
- **Sample Nearest.002** [GeometryNodeSampleNearest] {domain=POINT}
- **Sample Index.004** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
- **Group Input.009** [NodeGroupInput]
- **Math.003** [ShaderNodeMath] {operation=ADD}
- **Capture Attribute.005** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Capture Attribute.004** [GeometryNodeCaptureAttribute] {domain=POINT}
- **Switch.003** [GeometryNodeSwitch] {input_type=FLOAT}
- **Compare.002** [FunctionNodeCompare] {operation=LESS_THAN, data_type=FLOAT, mode=ELEMENT}
- **Boolean Math** [FunctionNodeBooleanMath] {operation=NOT}
- **Random Value.001** [FunctionNodeRandomValue] {data_type=FLOAT}
    inputs livres: Min = 0.0; Max = 1.0; Seed = 568746
- **Switch** [GeometryNodeSwitch] {input_type=GEOMETRY}
- **Delete Geometry.002** [GeometryNodeDeleteGeometry] {domain=POINT, mode=ALL}
- **Position** [GeometryNodeInputPosition]
- **Vector Math.002** [ShaderNodeVectorMath] {operation=ADD}
- **Vector Math.001** [ShaderNodeVectorMath] {operation=SCALE}
    inputs livres: Vector = (100.0, 100.0, 100.0)
- **Set Position.001** [GeometryNodeSetPosition]
- **Sample Nearest.007** [GeometryNodeSampleNearest] {domain=POINT}
- **Switch.001** [GeometryNodeSwitch] {input_type=INT}
- **Group Input.007** [NodeGroupInput]
- **Math** [ShaderNodeMath] {operation=SUBTRACT}
- **Math.001** [ShaderNodeMath] {operation=ABSOLUTE}
- **Evaluate at Index** [GeometryNodeFieldAtIndex] {data_type=INT, domain=POINT}
    inputs livres: Index = 0
- **Accumulate Field.001** [GeometryNodeAccumulateField] {data_type=INT, domain=POINT}
    inputs livres: Value = 1
- **Sample Index.003** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
    inputs livres: Index = 0
- **Sample Nearest.001** [GeometryNodeSampleNearest] {domain=POINT}
- **Index** [GeometryNodeInputIndex]
- **Sample Index** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
- **Sample Index.002** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
- **Sample Nearest.005** [GeometryNodeSampleNearest] {domain=POINT}
- **Compare** [FunctionNodeCompare] {operation=NOT_EQUAL, data_type=INT, mode=ELEMENT}
    inputs livres: B = 0
- **Capture Attribute.002** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Compare.001** [FunctionNodeCompare] {operation=EQUAL, data_type=INT, mode=ELEMENT}
- **Index.002** [GeometryNodeInputIndex]
- **Join Geometry.001** [GeometryNodeJoinGeometry]
- **Group Output** [NodeGroupOutput]
- **Capture Attribute** [GeometryNodeCaptureAttribute] {domain=CURVE}
- **Separate Geometry** [GeometryNodeSeparateGeometry] {domain=CURVE}
- **Sample Index.001** [GeometryNodeSampleIndex] {data_type=INT, domain=POINT}
- **Store Named Attribute** [GeometryNodeStoreNamedAttribute] {data_type=INT, domain=CURVE}
    inputs livres: Name = guide_curve_index

## Ligacoes (131)
- Capture Attribute.Value -> Group Output.Guide Index
- Capture Attribute.006.Geometry -> Capture Attribute.001.Geometry
- Group Input.001.Guide Distance -> Merge by Distance.Distance
- Curve to Points.Points -> Sample Index.001.Geometry
- Sample Index.001.Value -> Capture Attribute.Value
- Delete Geometry.002.Geometry -> Sample Index.Geometry
- Index.001.Index -> Capture Attribute.001.Value
- Index.Index -> Sample Index.001.Index
- Capture Attribute.006.Geometry -> Capture Attribute.Geometry
- Curve to Points.Points -> Sample Nearest.001.Geometry
- Curve to Points.Points -> Sample Index.002.Geometry
- Sample Nearest.001.Index -> Sample Index.002.Index
- Capture Attribute.Value -> Compare.001.A
- Capture Attribute.002.Value -> Group Output.Guide Selection
- Index.002.Index -> Compare.001.B
- Capture Attribute.002.Geometry -> Separate Geometry.Geometry
- Capture Attribute.002.Value -> Separate Geometry.Selection
- Separate Geometry.Selection -> Group Output.Guide Curves
- Store Named Attribute.Geometry -> Capture Attribute.002.Geometry
- Compare.001.Result -> Capture Attribute.002.Value
- Random Value.001.Value -> Compare.002.A
- Compare.002.Result -> Boolean Math.Boolean
- Switch.002.Output -> Delete Geometry.002.Geometry
- Boolean Math.Boolean -> Delete Geometry.002.Selection
- Group Input.003.Guide Mask -> Capture Attribute.003.Value
- Delete Geometry.002.Geometry -> Set Position.001.Geometry
- Vector Math.001.Vector -> Set Position.001.Offset
- Set Position.001.Geometry -> Sample Nearest.005.Geometry
- Delete Geometry.002.Geometry -> Sample Nearest.007.Geometry
- Vector Math.002.Vector -> Sample Nearest.005.Sample Position
- Position.Position -> Vector Math.002.Vector
- Vector Math.001.Vector -> Vector Math.002.Vector
- Group Input.004.Guides -> Separate Components.Geometry
- Separate Components.Mesh -> Mesh to Points.Mesh
- Mesh to Points.Points -> Join Geometry.Geometry
- Separate Components.Point Cloud -> Join Geometry.Geometry
- Curve to Points.001.Points -> Join Geometry.Geometry
- Domain Size.Point Count -> Compare.003.A
- Sample Nearest.005.Index -> Switch.001.True
- Sample Nearest.007.Index -> Switch.001.False
- Switch.001.Output -> Sample Index.Index
- Separate Components.001.Mesh -> Join Geometry.001.Geometry
- Separate Components.001.Point Cloud -> Join Geometry.001.Geometry
- Separate Components.001.Volume -> Join Geometry.001.Geometry
- Separate Components.001.Instances -> Join Geometry.001.Geometry
- Capture Attribute.002.Geometry -> Join Geometry.001.Geometry
- Join Geometry.001.Geometry -> Group Output.Geometry
- Separate Components.001.Curve -> Capture Attribute.003.Geometry
- Group Input.Geometry -> Separate Components.001.Geometry
- Separate Components.Curve -> Curve to Points.001.Curve
- Capture Attribute.001.Geometry -> Curve to Points.Curve
- Set Position.Geometry -> Merge by Distance.Geometry
- Switch.Output -> Set Position.Geometry
- Vector Math.003.Vector -> Set Position.Offset
- Merge by Distance.Geometry -> Set Position.002.Geometry
- Vector Math.003.Vector -> Vector Math.004.Vector
- Vector Math.004.Vector -> Set Position.002.Offset
- Group Input.007.Group ID -> Math.Value
- Group Input.007.Group ID -> Evaluate at Index.Value
- Curve to Points.Points -> Sample Index.003.Geometry
- Evaluate at Index.Value -> Math.Value
- Accumulate Field.001.Total -> Sample Index.003.Value
- Math.Value -> Math.001.Value
- Sample Index.003.Value -> Compare.A
- Compare.Result -> Switch.001.Switch
- Set Position.002.Geometry -> Switch.002.True
- Compare.Result -> Switch.002.Switch
- Switch.Output -> Merge by Distance.001.Geometry
- Merge by Distance.001.Geometry -> Switch.002.False
- Group Input.001.Guide Distance -> Merge by Distance.001.Distance
- Sample Index.Value -> Sample Index.001.Value
- Capture Attribute.001.Value -> Sample Index.002.Value
- Sample Index.002.Value -> Sample Index.Value
- Join Geometry.Geometry -> Domain Size.Geometry
- Join Geometry.Geometry -> Capture Attribute.004.Geometry
- Capture Attribute.003.Value -> Switch.003.False
- Capture Attribute.004.Value -> Switch.003.True
- Switch.003.Output -> Compare.002.B
- Compare.003.Result -> Switch.003.Switch
- Group Input.008.Guide Mask -> Capture Attribute.004.Value
- Group Input.001.Guide Distance -> Compare.004.A
- Compare.004.Result -> Merge by Distance.Selection
- Compare.004.Result -> Merge by Distance.001.Selection
- Curve to Points.Points -> Sample Nearest.002.Geometry
- Curve to Points.Points -> Sample Index.004.Geometry
- Sample Nearest.002.Index -> Sample Index.004.Index
- Group Input.009.Group ID -> Sample Index.004.Value
- Capture Attribute.004.Geometry -> Capture Attribute.005.Geometry
- Sample Index.004.Value -> Capture Attribute.005.Value
- Capture Attribute.003.Geometry -> Capture Attribute.006.Geometry
- Group Input.010.Group ID -> Capture Attribute.006.Value
- Capture Attribute.005.Value -> Math.003.Value
- Capture Attribute.006.Value -> Math.003.Value
- Math.003.Value -> Vector Math.003.Scale
- Math.003.Value -> Vector Math.001.Scale
- Curve to Points.Points -> Switch.False
- Compare.003.Result -> Switch.Switch
- Capture Attribute.005.Geometry -> Switch.True
- Capture Attribute.Geometry -> Store Named Attribute.Geometry
- Capture Attribute.Value -> Store Named Attribute.Value
- Separate Components.001.Grease Pencil -> Join Geometry.001.Geometry
