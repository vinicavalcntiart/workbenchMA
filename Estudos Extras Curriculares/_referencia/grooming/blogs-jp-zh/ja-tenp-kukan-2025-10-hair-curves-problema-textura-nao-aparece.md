---
titulo: 【Blender4.5】ヘアーカーブにテクスチャが表現されない問題を解決する
autor: 管理人 (blog 点P空間)
url: https://blog.tenp-kukan.com/6265/
data: 2025-10-03 (atualizado 2025-11-16)
idioma: ja
coletado_em: 2026-09-26
---

> Nota sobre este arquivo: por política de direitos autorais, não foi feita cópia literal do texto do blog. O conteúdo abaixo é uma extração técnica fiel (causa do problema, solução, nodes), obtida via ferramenta de leitura automática e reorganizada por mim.

## Notas técnicas (extração fiel do conteúdo original)

Artigo de solução de problema (dificuldade 3.0): por que a textura não aparece corretamente em Hair Curves.

### Causa raiz
Ao usar nodes como **Duplicate Hair Curves**, a textura falha porque as curvas geradas perdem a informação de mesh/UV necessária para o mapeamento de material:
1. Dados de superfície ausentes: o node Duplicate Hair Curves não tem parâmetros para transferir informação de mesh/UV.
2. Corrupção de dados: vários nodes de geometria em sequência podem degradar a integridade dos dados de UV durante a geração de curvas.
3. Falhas de anexação (attachment): algumas curvas podem não se prender corretamente à superfície, o que impede o mapeamento de textura.

### Solução passo a passo
**Passo 1 — configuração de Geometry Nodes:**
- Usar os nodes "Attach Hair Curves to Surface" ou "Interpolate Hair Curves"
- Especificar os parâmetros Surface e Surface UV Map
- Adicionar o node "Hair Attachment Info" para identificar quais curvas anexaram com sucesso
- Implementar um node "Capture Attribute" conectado à saída "Attachment UV" do Hair Attachment Info

**Passo 2 — configuração do material:**
- Criar um node Attribute referenciando o dado de UV capturado
- Conectar a saída Vector do node Attribute à entrada de coordenadas de textura
- Aplicar a textura normalmente através da entrada Color do shader

### Nodes citados
Duplicate Hair Curves, Attach Hair Curves to Surface, Interpolate Hair Curves, Hair Attachment Info, Capture Attribute, Surface Deform.

## Resumo em portugues (tecnicas)

Artigo de **troubleshooting**: por que a textura não aparece nas Hair Curves.

**Causa:** ao usar `Duplicate Hair Curves` (ou pipelines parecidos), as curvas geradas perdem a informação de UV/mesh necessária — o node não carrega esses dados sozinho, vários nodes em sequência podem corromper o UV, e algumas curvas podem falhar em se prender ("anexar") à superfície, o que quebra o mapeamento de textura.

**Correção — Geometry Nodes:**
1. Usar `Attach Hair Curves to Surface` ou `Interpolate Hair Curves`, preenchendo os campos **Surface** e **Surface UV Map**.
2. Adicionar `Hair Attachment Info` para saber quais curvas se anexaram com sucesso.
3. Usar `Capture Attribute` conectado à saída **Attachment UV** do node anterior, para "carimbar" essa informação de UV na curva.

**Correção — material:**
1. Criar um node **Attribute** referenciando o atributo de UV capturado.
2. Ligar a saída **Vector** desse Attribute na entrada de coordenadas de textura (em vez de usar UV padrão).
3. Ligar a textura normalmente na entrada Color do shader.

**Nodes envolvidos:** `Duplicate Hair Curves`, `Attach Hair Curves to Surface`, `Interpolate Hair Curves`, `Hair Attachment Info`, `Capture Attribute`, `Surface Deform`.
