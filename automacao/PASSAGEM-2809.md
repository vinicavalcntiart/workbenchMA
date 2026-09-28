# Passagem de bastão, 28/09/2026

Você é o maestro, o parceiro do Vini nessa campanha. O sonho é dele e agora é seu também: um emprego incrível num estúdio de animação, morando fora. Este arquivo conta onde a campanha está para você continuar daqui.

## Quem é o Vini

Senior 3D Character Artist em Olinda, com mais de dez anos em personagens e criaturas estilizados. Tem crédito em The Wingfeather Saga (Angel Studios) e quase cinco anos em Endstar (E-Line Media), e faz grooming em Houdini. Para trabalhar fora precisa de patrocínio de visto.

Portfólio: https://www.artstation.com/viniciuscavalcanti

## Placar

- **27/09:** 23 formulários confirmados, 9 de personagem. Foram também 26 cartas novas em rascunho.
- **28/09, até 01h UTC:** 6 formulários (2K Small Axe, Sledgehammer, BeamNG, Framestore x2 e Ten Square Games), 2 deles de personagem.
- **Tudo:** o histórico completo está em `enviados.csv`, o diário em `automacao/processados.csv` e o painel em `docs/index.html`.

## Terça, 29/09: o dia dos 100 formulários

- **O pedido:** o Vini quer pelo menos 100 formulários na terça.
- **O estoque:** está em `automacao/FILA-TERCA.csv`, com 168 linhas (fonte, casa, cargo, país, URL, família do formulário, personagem s/n). Vieram do painel, do gamedevmap, de quadros de vagas e de casas grandes. Seis já saíram no domingo: Ubisoft x3, Sony Imageworks e Netflix x2. Antes de enviar, confira sempre no `enviados.csv`.
- **O plano:** vários agentes em paralelo, cada um com a sua fatia da fila.

## O navegador

**Local, gratuito, para tudo que não tem caixa "sou humano":**
- Playwright com o Chromium do ambiente, aberto por `automacao/navegador.js`.
- Os scripts por sistema da sessão antiga (Greenhouse, Workday, Recruitee, Teamtailor, Lever, BambooHR, SmartRecruiters) ficaram só no container dela e não estão no repositório. O que já se aprendeu com eles:
  - **Greenhouse:** as perguntas vêm de `boards-api.greenhouse.io/v1/boards/<conta>/jobs/<id>?questions=true`. Quando o formulário pede, chega um código de segurança por email com o assunto "Security code for your application to ...". Leia o código no Gmail e cole no formulário.
  - **Workday:** a conta de cada estúdio usa o email e a senha das credenciais no Drive. O caminho da vaga vai sem o prefixo `job/` duplicado. A tela final "Application Submitted" e a lista "My Applications" provam o envio.
  - **SmartRecruiters (Ubisoft):** o formulário de um clique usa componentes com shadow DOM. A cidade é um autocomplete ("Olinda, Pernambuco, Brazil"), e o telefone tem um seletor de país separado.
  - **Recruitee e Workable:** a caixa hCaptcha ou Cloudflare aparece no envio, então esses vão para o Kernel.

**Kernel, só para caixa "sou humano" explícita:**
- A conta está no plano Free, sem cartão, com US$ 5 de crédito por mês. Em 28/09 os créditos acabaram e a conta ficou pausada até renovar.
- Cada navegador aberto custa cerca de US$ 0,48 por hora.
- O jeito combinado: abrir a sessão só quando o Vini chamar, preencher na hora, anexar o CV por último, passar o link e fechar a sessão logo depois do envio. Assim os créditos rendem e nada fica aberto de madrugada.
- O `automacao/navegador.js` ainda cria a sessão na nuvem com 24h de porta aberta, que era o jeito antigo. No jeito novo, a sessão é apagada assim que o envio termina.
- As duas sessões antigas (hh7p38x... e ikj9geg...) ficaram abertas com abas velhas. Podem ser apagadas quando o Kernel voltar.

## O que depende de caixa "sou humano"

**Falharam na leva de 28/09 e precisam ser refeitos no Kernel:**
- **Relic e Stormind (BambooHR):** o anexo venceu enquanto a aba esperava.
- **Jungler (JazzHR):** o CV sumia a cada verificação.

**Sem recibo até agora:** Framestore Montreal (Généraliste Blender), Obsidian e Mediawan.

**Lever recusa a verificação feita a partir de servidor:** Kolibri, Behaviour, Quantic Dream e Larian. As de Quantic e Larian já viraram carta.

## Cartas

- **A fila:** 59 rascunhos com o assunto `Senior Character Artist · Wingfeather Saga credit · stylized + grooming` esperam o Apps Script do Vini, que roda na conta Google dele (projeto "campanha"). O envio automático parou em 24/09.
- **O formato:** o `.txt` vira HTML com `automacao/monta-html-carta.py` e passa por `automacao/confere-carta.py`.
- **As pessoas:** o Joe (agente campanha-detetive) acha pessoas com email publicado. As fichas ficam em `automacao/PESSOAS-SEM-CARTA.md` e `automacao/pessoas.csv`. Uma rodada do Joe saiu às 01h35 UTC de 28/09, e as fichas dela aparecem em `pessoas.csv` com `PENDENTE-maestro-escreve`.

## Agenda

- **28/09, 11h00 UTC:** email para o Tero, da Animagency.
- **CV:** o link do currículo (litterbox, 72h) precisa ser renovado antes de 29/09 12h UTC. O PDF original está no Drive do Vini.
- **Rotinas:** as rotinas agendadas (formulários a cada 2h, caixa de entrada, Joe, rede :42, fechamento do dia) disparam na sessão antiga. `list_triggers` mostra todas, para apontar para a sessão nova ou recriar.

## Onde ficam os dados privados

Nada disso vai para o repositório, que é público. Tudo está no Drive do Vini, na pasta da campanha:
- **Dados pessoais:** "CAMPANHA - dados pessoais dos formulários (privado)".
- **Credenciais:** "CAMPANHA - credenciais dos portais (privado)", o adendo de 09-09 (Disney), o de 07-09 (EA e 80 Level) e o do Hitmarker.
