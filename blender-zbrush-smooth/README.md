# VC_Smooth — Smooth estilo ZBrush para o Sculpt do Blender

Patch para o código-fonte do Blender que cria o brush **VC_Smooth**
("Vini Cavalcanti Smooth"): um smooth estilo ZBrush em que cada passada
suaviza a **forma** (Laplacian smooth) e ao mesmo tempo relaxa a **topologia**
(o mesmo algoritmo tangencial e preservador de superfície usado pelo brush
**Slide Relax** no modo Relax). A superfície amacia e a distribuição dos
vértices se equaliza junto, como o Smooth do ZBrush.

O **Smooth padrão do Blender fica intacto**: o comportamento combinado só é
ativado para brushes de smooth cujo nome começa com `VC_Smooth` ou
`Vini Cavalcanti`.

## Como funciona

Arquivo modificado: `source/blender/editors/sculpt_paint/mesh/brushes/smooth.cc`

- No `do_smooth_brush`, o nome do brush ativo é verificado
  (`is_vc_smooth_brush`). Se começar com `VC_Smooth` ou `Vini Cavalcanti`,
  cada iteração do smooth também calcula a translação de relax via
  `smooth::calc_relaxed_translations_*` (a função interna do Slide Relax), que
  desloca cada vértice em direção à média dos vizinhos **projetada no plano
  tangente da normal** — equaliza a topologia sem alterar a forma.
- As duas translações são calculadas sobre o mesmo snapshot de posições e
  aplicadas somadas numa única deformação (com clip/lock de simetria normal).
- Funciona nas três representações do sculpt: **Mesh**, **Multires (Grids)** e
  **Dyntopo (BMesh)**.
- Bordas e cantos são protegidos pelo próprio algoritmo de relax (mesma
  proteção do Slide Relax). Máscara, automasking, face sets e textura do
  brush são respeitados.

A intensidade do relax em relação ao smooth é a constante
`topology_relax_factor` no topo do `smooth.cc` (padrão `1.0f`; `0.5f` para um
relax mais discreto).

## Instalação rápida (recomendada)

1. **Compilar** (uma vez): rode `instalar_windows.bat` (Windows) ou
   `bash instalar_linux.sh` (Linux). O script baixa o Blender, aplica o
   patch e compila sozinho — só esperar.
2. **Importar o brush**: o arquivo **`VC_Smooth_brush.blend`** já vem pronto
   nesta pasta, com o brush marcado como asset (salvo na versão 4.3, abre em
   qualquer Blender 4.3+). **Atenção: não abra o .blend com dois cliques** —
   ele vai parecer uma cena vazia, porque o brush não é um objeto. O caminho
   certo é registrar a pasta como Asset Library:
   - Coloque o `VC_Smooth_brush.blend` numa pasta fixa (ex.:
     `Documentos\BlenderAssets`).
   - No Blender compilado: `Edit → Preferences → File Paths → Asset
     Libraries → +` e aponte para essa pasta.
   - Entre no **Sculpt Mode** e abra o **asset shelf** (a barrinha na parte
     de baixo da viewport — arraste a borda inferior pra cima se estiver
     recolhida). O **VC_Smooth** aparece lá (se tiver filtro de catálogo
     ativo, olhe em "All"/"Unassigned").
   - Vale para todos os projetos, para sempre.

Alternativa sem o .blend: duplicar o brush Smooth na UI (clique-direito no
asset shelf → **Duplicate Asset**) e renomear para `VC_Smooth` — o código
reconhece qualquer smooth cujo nome comece com `VC_Smooth` ou
`Vini Cavalcanti`.

O Smooth original continua 100% vanilla. Observação: o smooth de atalho
(segurar **Shift**) usa o brush Smooth padrão, então continua vanilla — use o
VC_Smooth diretamente (dá para fixar no asset shelf ou mapear num atalho).

## Base do patch

- Repositório: https://projects.blender.org/blender/blender (mirror no GitHub:
  https://github.com/blender/blender)
- Alvo dos instaladores: branch **`blender-v5.2-release`** (Blender 5.2 LTS —
  a mesma versão que o Vini usa). Verificado: o patch aplica limpo e passa
  checagem de tipos (`clang -fsyntax-only`) tanto no 5.2 LTS quanto no `main`
  (commit `08bed5b5`, ago/2026).
- Patch pequeno, num arquivo só. Se falhar em outra versão, aplique as
  mudanças à mão (são blocos pequenos).

## Como aplicar e compilar

```bash
# 1. Clonar o Blender (ou usar seu checkout existente)
git clone https://projects.blender.org/blender/blender.git
cd blender

# 2. Aplicar o patch
git apply /caminho/para/zbrush-style-smooth.patch

# 3. Baixar as bibliotecas pré-compiladas e compilar
#    (Windows: Visual Studio 2022 + CMake; Linux: gcc/clang + CMake)
make update
make          # build release

# Binário: ../build_linux/bin/blender (Linux)
# Windows: make.bat update && make.bat  → build_windows\...\bin\Release
```

Guia oficial de build: https://developer.blender.org/docs/handbook/building_blender/

## Verificação feita

- O `smooth.cc` modificado passou verificação completa de tipos com
  `clang++ -fsyntax-only -std=c++20` contra os headers reais da árvore do
  Blender no commit base (assinaturas de
  `calc_relaxed_translations_faces/grids/bmesh` e helpers conferidas na
  fonte).
- Não foi possível compilar/rodar o Blender inteiro neste ambiente (sem GPU e
  sem as bibliotecas pré-compiladas), então o teste visual final é na sua
  máquina.

## Ajuste fino

```cpp
constexpr float topology_relax_factor = 1.0f;  // 0.0 = só forma, 1.0 = relax total
```

Edite no `smooth.cc` e recompile (rebuild incremental é rápido, só um arquivo
muda).
