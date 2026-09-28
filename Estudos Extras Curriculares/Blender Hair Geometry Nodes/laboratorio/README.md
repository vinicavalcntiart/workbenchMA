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
| GR Guias Procedurais | gera guias penteadas sem esculpir (Curves vazio com Surface) | antes de tudo, opcional |
| GR Densidade Livre | Interpolate sem a trava de 10.000 fios/m² | primeiro |
| GR Mecha Estilizada | mecha em fita, raiz coberta | depois do Interpolate |
| GR Lado da Risca | 0/1 pelo lado da raiz | no Group ID da Mecha Estilizada |
| GR Strays em Arco | 4% dos fios em arco limpo | antes de Curl/Braid |
| GR Cacho por Mecha | cacho com raio e voltas por mecha, em voltas por metro | depois da Mecha |
| GR Onda S | onda plana de desenho | depois da Mecha |
| GR Cor por Mecha | grava `mecha_rand` para o shader | em qualquer ponto depois da Mecha |
| GR Mecha Chunky | fios viram fitas de malha torcidas | último |
| GR Ponta Virada | ponta para fora (flip) ou para dentro, variando por mecha | depois da Mecha |
| GR Trança Grossa | trança de raio constante | depois de Densidade Livre com Distância das guias ~0,02 |
| GR Corte por Região | curto onde o vertex group vale 0, sem clump ali | depois do Interpolate |
| GR Pelo em Tufos | pelo estilizado com subpelo e pelo de guarda opcionais | sozinho, no lugar do Interpolate |
| GR Volume na Raiz | empurra o fio pela normal do scalp, raiz parada | depois da Mecha |
| GR Máscara por Imagem | apaga fios onde a imagem é preta; devolve o cinza para reusar | depois do Interpolate |
| GR Física Estilizada | Hair Dynamics nas guias, segura o penteado | antes do Interpolate, num modificador só das guias |
| GR Rabo de Cavalo | junta tudo num elástico e deixa cair | depois da Densidade Livre, antes da Mecha |
| GR Forma por Malha | as guias colam numa malha simples (a silhueta) | nas guias, antes do Interpolate |
| GR Corte pela Malha | corte reto: apaga o que passa da malha | depois da Mecha/Onda |
| GR Comprimento até a Malha | fio reto da raiz até a malha (Trolls, espetado) | depois da Densidade Livre, antes do Clump |
| GR Crescer | animação: cada mecha cresce pelo caminho final | no fim, antes do Set Hair Curve Profile |
| GR LOD por Câmera | multidão: menos fios longe, fio mais grosso | no fim, depois do Set Hair Curve Profile |
| GR Ver em Cores | número vira azul/vermelho no Viewer | fora da cadeia |

Materiais: **GR Cabelo Cor por Mecha** (lê `mecha_rand` e escurece a raiz) e
**GR Cabelo Toon**.

## Física

Guias com Snap to Nearest Surface. Modificador 1 só com GR Física
Estilizada. Modificador 2 com a cadeia de groom. Colisão: modificador
Collider na cabeça inteira, a cabeça numa coleção, a coleção na entrada
Colisores. Não ligue Surface Collision no scalp. Vento: entrada Vento
(0,04 brisa, 0,12 vento de cena) e Direção do vento.

## Ordem que funciona

GR Densidade Livre → GR Mecha Estilizada → GR Strays em Arco → GR Cacho por
Mecha → GR Cor por Mecha → Set Hair Curve Profile → Set Material.

Para variações, ligue um único node Integer no Seed de todos os grupos.
