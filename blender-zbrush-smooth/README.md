# Smooth estilo ZBrush para o Sculpt do Blender

Patch para o código-fonte do Blender que transforma o brush **Smooth** do Sculpt
em um smooth estilo ZBrush: cada passada suaviza a **forma** (Laplacian smooth,
comportamento original) e ao mesmo tempo relaxa a **topologia** (o mesmo
algoritmo tangencial e preservador de superfície usado pelo brush **Slide
Relax** no modo Relax). Resultado: a superfície amacia e a distribuição dos
vértices se equaliza junto, como o Smooth do ZBrush.

## O que o patch faz

Arquivo modificado: `source/blender/editors/sculpt_paint/mesh/brushes/smooth.cc`

- Em cada iteração do Smooth, além da média Laplaciana dos vizinhos, é
  calculada a translação de relax via `smooth::calc_relaxed_translations_*`
  (a função interna do Slide Relax), que desloca cada vértice em direção à
  média dos vizinhos **projetada no plano tangente da normal** — ou seja,
  equaliza a topologia sem alterar a forma.
- As duas translações são calculadas sobre o mesmo snapshot de posições e
  aplicadas somadas numa única deformação (com clip/lock de simetria normal).
- Funciona nas três representações do sculpt: **Mesh**, **Multires (Grids)** e
  **Dyntopo (BMesh)**.
- Vértices de borda e cantos são protegidos pelo próprio algoritmo de relax
  (mesma proteção do Slide Relax).
- Como o Smooth também é o que roda ao segurar **Shift** com qualquer brush,
  o smooth estilo ZBrush vale para o atalho Shift também.

A intensidade do relax em relação ao smooth é a constante
`topology_relax_factor` no topo do `smooth.cc` (padrão `1.0f`; use `0.5f` para
um relax mais discreto, `0.0f` restaura o comportamento original do Blender).

## Base do patch

- Repositório: https://github.com/blender/blender (mirror oficial)
- Commit base: `08bed5b5b42ec017e8dcc87b76f6c373c322b086` (branch `main`, ago/2026)
- O patch é pequeno e localizado num arquivo só; tende a aplicar limpo em
  qualquer 4.5+/5.x recente. Se falhar, aplique as mudanças à mão (são 6
  blocos pequenos).

## Como aplicar e compilar

```bash
# 1. Clonar o Blender (ou usar seu checkout existente)
git clone https://projects.blender.org/blender/blender.git
cd blender

# 2. Aplicar o patch
git apply /caminho/para/zbrush-style-smooth.patch

# 3. Baixar as bibliotecas pré-compiladas e compilar
#    (Windows: instale Visual Studio 2022 + CMake; Linux: gcc/clang + CMake)
./build_files/utils/make_update.py --use-linux-libraries   # Linux
make update                                                # alternativa
make                                                       # build release

# Binário sai em ../build_linux/bin/blender (Linux)
# No Windows: make.bat update && make.bat  → build_windows\...\bin\Release
```

Guia oficial de build: https://developer.blender.org/docs/handbook/building_blender/

## Verificação feita

- O `smooth.cc` modificado passou verificação completa de tipos com
  `clang++ -fsyntax-only -std=c++20` contra os headers reais da árvore do
  Blender no commit base (todas as assinaturas de
  `calc_relaxed_translations_faces/grids/bmesh` e helpers conferidas na
  fonte).
- Não foi possível compilar/rodar o Blender inteiro neste ambiente (sem GPU e
  sem as bibliotecas pré-compiladas), então o teste visual final é na sua
  máquina.

## Ajuste fino

Depois de testar, se quiser mais ou menos "escorregamento" de topologia,
edite no `smooth.cc`:

```cpp
constexpr float topology_relax_factor = 1.0f;  // 0.0 = só forma, 1.0 = relax total
```

e recompile (rebuild incremental é rápido, só um arquivo muda).
