---
titulo: 【Blender毛发教程】使用Blender制作一只茸茸的鸵鸟（上）
autor: Kevin Ruffenach
url: https://www.renderbus.com/share/blender-blender/
data: 2020-10-22
idioma: zh
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do artigo. O conteúdo abaixo é uma extração técnica fiel, obtida via ferramenta de leitura automática e reorganizada por mim. Esta é a Parte 1 (上) de duas; o texto disponível foca na modelagem base e iluminação — o detalhamento técnico do sistema de pelo em si fica reservado para a Parte 2 (下), que não foi localizada/coletada nesta pesquisa (o artigo é anterior ao sistema Hair Curves atual do Blender, de 2020).

## Notas técnicas (extração fiel do conteúdo original)

### Fase de modelagem
- Construção base: modelos separados para bico e olhos
- Método de escultura: dyntopo (topologia dinâmica) para detalhes
- Abordagem: ajuste da forma do bico e da cabeça, com escultura de detalhes usando dyntopo

### Configuração de iluminação
- Sistema: iluminação de três pontos
- HDRI: obtido do HDRI Haven
- Configuração de reflexão do HDRI: aproximadamente 0,6
- Fundo: superfície curva com textura em gradiente

### Notas sobre a implementação de pelo
Este é a Parte 1 (上) e foca em trabalho de fundação. Nomes de node de pelo, configurações de partícula e parâmetros de shader **não são detalhados nesta seção** — o guia enfatiza que os diferentes comprimentos de pena do avestruz oferecem um bom campo de testes para diferentes tipos de pelo, mas reserva a execução técnica para a continuação (Parte 2).

### Decisão de produção
Priorizou a aparência voltada para a câmera em vez da limpeza completa da topologia do modelo, dado o caráter de pesquisa/teste do projeto.

## Resumo em portugues (tecnicas)

Parte 1 (上) de um tutorial de pelo em avestruz. Como o artigo publicado é de 2020 (antes do sistema Hair Curves atual do Blender, lançado em 2022 no 3.3), o sistema de pelo provavelmente usado aqui é o **Hair Particle System** clássico — mas essa parte específica do texto **não chega a detalhar o sistema de pelo em si**, apenas a base do projeto.

**Modelagem:** bico e olhos como modelos separados; escultura de detalhes com **dyntopo** (topologia dinâmica no Sculpt Mode).

**Iluminação:** esquema de três pontos; HDRI da HDRI Haven com força de reflexão ≈ 0,6; fundo em superfície curva com gradiente.

**Observação importante:** o detalhamento técnico do sistema de pelo (nodes/partículas/shader) fica reservado para a Parte 2 (下) do tutorial, que não foi encontrada/coletada nesta pesquisa — a busca não localizou uma URL publicada para essa segunda parte.

**Decisão de produção:** o autor priorizou a aparência da vista de câmera principal em vez de otimizar a topologia completa do modelo, por ser um projeto de caráter exploratório/teste.
