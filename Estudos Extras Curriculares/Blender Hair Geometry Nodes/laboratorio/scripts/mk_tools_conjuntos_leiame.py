import bpy
LEIA = """COMO USAR OS TOOLS DE CONJUNTO DE GUIAS (Blender 5.2)

1. Objeto Cabelo em Edit Mode (ja abre assim).
2. Na barra da viewport, clique no icone de pagina tracejada
   logo depois de Segments. Ali estao os 3 tools:
   - Salvar Selecao: grava as guias selecionadas num atributo.
   - Selecionar Conjunto: seleciona so as guias de um atributo.
   - Apagar Conjunto: apaga as guias de um atributo (os outros atributos ficam).
3. Logo depois de rodar, abra o painel de redo no canto inferior
   esquerdo e troque o Nome do conjunto.

Conjuntos ja criados: Front_Guides_02_R (57 guias) e Back_Guides_01_R (185).
Os nodes de cada tool: editor da direita, modo Tool (dropdown no canto
superior esquerdo do editor), escolha o grupo no seletor de data-block.
Cada tool tem Identifier proprio (Options) e Fake User ligado.
"""

t = bpy.data.texts.new("LEIA-ME"); t.write(LEIA); t.use_fake_user = True
ob = bpy.data.objects["Cabelo"]; bpy.context.view_layer.objects.active = ob
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.wm.save_mainfile(compress=True); print("RESULT salvo com LEIA-ME", ob.mode)
