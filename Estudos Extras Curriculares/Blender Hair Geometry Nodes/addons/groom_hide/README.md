# Groom Hide

Esconde guias de hair curves enquanto voce faz grooming, sem mudar o cabelo
gerado. Funciona nos modos Sculpt Curves, Edit e Object, em Blender 4.2 ou
mais novo.

## Instalar

1. Preferences > Get Extensions > menu de seta no canto > Install from Disk.
2. Escolha `groom_hide.zip`.
3. O painel aparece na sidebar (N) do viewport 3D, aba **Groom**, quando o
   objeto ativo e um Curves.

## Usar

| Acao | Atalho | O que faz |
|---|---|---|
| Esconder selecionadas | H | Tira as guias selecionadas da vista |
| Esconder nao selecionadas | Shift+H | Isola as guias selecionadas |
| Revelar todas | Alt+H | Traz tudo de volta |
| Revelar ultimo | painel | Desfaz so o ultimo esconder |
| Revelar conjunto N | painel, icone do olho | Traz um conjunto especifico |

Cada "esconder" cria um conjunto. Da para empilhar varios e revelar em
qualquer ordem.

No modo Sculpt a selecao e suave (0 a 1). Uma guia conta como selecionada se
qualquer ponto dela tiver selecao maior que zero. Se nao houver selecao
nenhuma, o addon avisa em vez de esconder tudo.

## Por que nao e so um H nativo

O Blender 5.2 nao esconde curvas no modo Sculpt. Existe um test build de um
contribuidor (jan/2026) com PRs em revisao, mas ainda nao entrou. E o motivo
tecnico e que o modo Sculpt desenha as guias originais como "cage" por cima do
resultado avaliado, e nenhum modificador filtra esse cage. Esconder de
verdade significa tirar as curvas do objeto.

Entao o addon faz isto:

1. Copia o objeto, deixa na copia so as guias escondidas, e na original so as
   visiveis. A copia vai para uma colecao oculta chamada
   `<objeto> · guias ocultas`.
2. Coloca no topo da stack um modificador de Geometry Nodes chamado
   `Groom Hide (guias ocultas)`, que injeta as guias escondidas de volta na
   avaliacao, na ordem original, antes do Interpolate. Resultado: os filhos
   ficam identicos, o cage so mostra o que voce quer pentear, e os brushes nao
   alcancam as guias escondidas.
3. Ao revelar, junta os objetos de volta, restaura a ordem original das
   curvas (para nao mudar seeds por indice), e remove modificador, colecao e
   atributo auxiliar quando nao sobra nada escondido.

O checkbox **Alimentar interpolacao** controla o passo 2. Ele liga sozinho
quando o objeto gera filhos (avaliacao com mais curvas que o original) e
desliga quando nao gera, porque nesse caso as guias escondidas voltariam a
aparecer no resultado avaliado.

## Cuidados

- Nao apague a colecao `· guias ocultas` nem os objetos `.oculto.NNN` na mao.
  Use Revelar todas. Se apagar, as guias escondidas somem de verdade.
- Salvar o arquivo com guias escondidas e seguro; o estado fica nos objetos.
- Undo: cada esconder e revelar e um passo de undo, mas o operador troca de
  modo por dentro. Se o undo se comportar estranho num caso especifico,
  Revelar todas e o caminho de volta garantido.
- Nao testado com dados linkados de biblioteca.
- Testado em modo headless com o modulo `bpy` 5.0.1 (ver `test_headless.py`);
  nao foi testado com interface grafica nem na 5.2. O teste cobre esconder por
  selecao de ponto e de curva, revelar por conjunto e revelar tudo, e confirma
  que o cabelo avaliado pelo Interpolate Hair Curves da Essentials fica
  identico com guias escondidas.

## Rodar o teste

```
uv venv --python 3.11 bpyenv
uv pip install --python bpyenv/bin/python bpy==5.0.1
bpyenv/bin/python test_headless.py
```
