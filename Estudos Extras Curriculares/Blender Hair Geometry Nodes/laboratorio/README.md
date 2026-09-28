# Laboratório de grooming estilizado (Blender 5.2)

Tudo aqui foi testado em bpy 5.2.2 e renderizado em Cycles, numa cabeça em
escala real (raio 10 cm). As conclusões estão no cérebro, seção 17:
`../../_referencia/grooming/CEREBRO_GROOMING.md`.

- `receitas_grooming.blend`: biblioteca de node groups prontos.
- `img/`: folhas de contato de cada teste.
- `scripts/`: o laboratório (`lab.py`), um script por teste e as notas brutas.

## Como usar a biblioteca

1. Edit > Preferences > File Paths > Asset Libraries > **+**, aponte para esta
   pasta.
2. No Geometry Nodes do seu Curves, Shift+A > a biblioteca > grupos "GR".
3. Ou File > Append > `receitas_grooming.blend` > NodeTree.

## Os grupos

| Grupo | Faz o quê | Onde vai na cadeia |
|---|---|---|
| GR Densidade Livre | Interpolate sem a trava de 10.000 fios/m² | primeiro |
| GR Mecha Estilizada | mecha em fita, raiz coberta | depois do Interpolate |
| GR Lado da Risca | 0/1 pelo lado da raiz | no Group ID da Mecha Estilizada |
| GR Strays em Arco | 4% dos fios em arco limpo | antes de Curl/Braid |
| GR Cacho por Mecha | cacho com raio e voltas por mecha, em voltas por metro | depois da Mecha |
| GR Onda S | onda plana de desenho | depois da Mecha |
| GR Cor por Mecha | grava `mecha_rand` para o shader | em qualquer ponto depois da Mecha |
| GR Mecha Chunky | fios viram fitas de malha torcidas | último |
| GR Ver em Cores | número vira azul/vermelho no Viewer | fora da cadeia |

Materiais: **GR Cabelo Cor por Mecha** (lê `mecha_rand` e escurece a raiz) e
**GR Cabelo Toon**.

## Ordem que funciona

GR Densidade Livre → GR Mecha Estilizada → GR Strays em Arco → GR Cacho por
Mecha → GR Cor por Mecha → Set Hair Curve Profile → Set Material.

Para variações, ligue um único node Integer no Seed de todos os grupos.
