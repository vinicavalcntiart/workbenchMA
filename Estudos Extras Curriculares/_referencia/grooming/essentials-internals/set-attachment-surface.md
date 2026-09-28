# Set Attachment Surface

Fonte: Essentials asset library do Blender 5.2.2 LTS (arquivo procedural_hair_node_assets.blend). Dump automatico: interface, nodes internos com valores padrao, e ligacoes. Serve para entender COMO cada node group funciona por dentro.

## Interface
- OUTPUT Geometry (Geometry, default None)
- INPUT Geometry (Geometry, default None)
- INPUT Mode (Menu, default Object)
- INPUT Surface Geometry (Geometry, default None)
- INPUT Surface Object (Object, default None)
- INPUT Surface UV Map (Vector, default (0.0, 0.0), min -3.4028234663852886e+38, max 3.4028234663852886e+38)

## Nodes (22)
- **Get Geometry Bundle** [GeometryNodeGetGeometryBundle]
    inputs livres: Remove = True
- **Set Geometry Bundle** [GeometryNodeSetGeometryBundle]
- **Store Bundle Item.001** [NodeStoreBundleItem]
    inputs livres: Path = surface_uv_map
- **Store Bundle Item.002** [NodeStoreBundleItem]
    inputs livres: Path = surface_geometry
- **Group Input.009** [NodeGroupInput]
- **Menu Switch.004** [GeometryNodeMenuSwitch] {data_type=GEOMETRY}
- **Group Input.010** [NodeGroupInput]
- **Group Input.014** [NodeGroupInput]
- **Get Geometry Bundle.001** [GeometryNodeGetGeometryBundle]
    inputs livres: Remove = True
- **Set Geometry Bundle.001** [GeometryNodeSetGeometryBundle]
- **Store Bundle Item.003** [NodeStoreBundleItem]
    inputs livres: Path = surface_uv_map
- **Store Bundle Item.004** [NodeStoreBundleItem]
    inputs livres: Path = surface_geometry
- **Group Input.015** [NodeGroupInput]
- **Group Input.011** [NodeGroupInput]
- **Group Output** [NodeGroupOutput]
- **Object Info** [GeometryNodeObjectInfo] {transform_space=RELATIVE}
    inputs livres: As Instance = False
- **Get Bundle Item** [NodeGetBundleItem]
    inputs livres: Path = surface_object; Remove = True
- **Get Bundle Item.001** [NodeGetBundleItem]
    inputs livres: Path = surface_uv_map_name; Remove = True
- **Get Bundle Item.002** [NodeGetBundleItem]
    inputs livres: Path = surface_object; Remove = True
- **Get Bundle Item.003** [NodeGetBundleItem]
    inputs livres: Path = surface_uv_map_name; Remove = True

## Ligacoes (23)
- Get Geometry Bundle.Geometry -> Set Geometry Bundle.Geometry
- Get Geometry Bundle.Bundle -> Store Bundle Item.002.Bundle
- Store Bundle Item.002.Bundle -> Store Bundle Item.001.Bundle
- Group Input.010.Mode -> Menu Switch.004.Menu
- Group Input.009.Surface UV Map -> Store Bundle Item.001.Item
- Group Input.014.Surface Geometry -> Store Bundle Item.002.Item
- Group Input.014.Geometry -> Get Geometry Bundle.Geometry
- Set Geometry Bundle.Geometry -> Menu Switch.004.Geometry
- Get Geometry Bundle.001.Geometry -> Set Geometry Bundle.001.Geometry
- Get Geometry Bundle.001.Bundle -> Store Bundle Item.004.Bundle
- Store Bundle Item.004.Bundle -> Store Bundle Item.003.Bundle
- Get Bundle Item.001.Bundle -> Set Geometry Bundle.001.Bundle
- Group Input.015.Geometry -> Get Geometry Bundle.001.Geometry
- Set Geometry Bundle.001.Geometry -> Menu Switch.004.Object
- Group Input.011.Surface UV Map -> Store Bundle Item.003.Item
- Menu Switch.004.Output -> Group Output.Geometry
- Group Input.015.Surface Object -> Object Info.Object
- Object Info.Geometry -> Store Bundle Item.004.Item
- Store Bundle Item.003.Bundle -> Get Bundle Item.Bundle
- Get Bundle Item.Bundle -> Get Bundle Item.001.Bundle
- Get Bundle Item.002.Bundle -> Get Bundle Item.003.Bundle
- Store Bundle Item.001.Bundle -> Get Bundle Item.002.Bundle
- Get Bundle Item.003.Bundle -> Set Geometry Bundle.Bundle
