import bpy

linhas = []
cena = bpy.context.scene.collection
vl = bpy.context.view_layer
achados = 0

# 1. Colecoes de guias ocultas: liga o olho e tira da exclusao
def liga(lc):
    if "guias ocultas" in lc.collection.name:
        lc.hide_viewport = False
        lc.exclude = False
        lc.collection.hide_viewport = False
        linhas.append(f"colecao '{lc.collection.name}': ligada, {len(lc.collection.objects)} objeto(s)")
    for filho in lc.children:
        liga(filho)
liga(vl.layer_collection)

# 2. Objetos de curvas: lista todos e traz os escondidos pelo addon
for o in list(bpy.data.objects):
    if o.type != 'CURVES':
        continue
    dono = None
    try:
        dono = o.groom_hide.owner
    except Exception:
        pass
    estacionado = (".oculto." in o.name) or (dono is not None)
    cols = [c.name for c in o.users_collection]
    linhas.append(f"objeto '{o.name}': {len(o.data.curves)} curvas, colecoes={cols}, estacionado={estacionado}")
    if estacionado:
        achados += 1
        if o.name not in cena.objects:
            cena.objects.link(o)
        o.hide_viewport = False
        o.hide_select = False
        o.hide_render = False
        if o.name in vl.objects:
            o.hide_set(False)

# 3. Dados de curvas sem objeto (orfaos): cria um objeto para cada um
for cd in list(bpy.data.hair_curves):
    if cd.users == 0 and len(cd.curves) > 0:
        ob = bpy.data.objects.new(cd.name + "_recuperado", cd)
        cena.objects.link(ob)
        linhas.append(f"RECUPERADO dado orfao '{cd.name}': {len(cd.curves)} curvas -> objeto '{ob.name}'")
        achados += 1

linhas.append(f"TOTAL de conjuntos de guias encontrados: {achados}")
txt = bpy.data.texts.get("relatorio_guias") or bpy.data.texts.new("relatorio_guias")
txt.clear()
txt.write("\n".join(linhas))
print("\n".join(linhas))
