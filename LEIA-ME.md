# Campanha de emprego do Vini Cavalcanti: mapa das pastas

Objetivo único: o Vini conseguir o emprego dos sonhos como Senior 3D Character Artist.
Painel ao vivo: https://vinicavalcntiart.github.io/workbenchMA/

## Regras (ler nesta ordem)
1. `CLAUDE.md`: quem manda (o Vini), o tom com ele, a leva da manhã das caixinhas "sou humano", estúdios grandes.
2. `automacao/REGRAS.md`: o resumo de tudo que vale hoje (o que se busca, metas, formulários, salário, cartas, segurança).
3. `automacao/BRIEF-*.md`: o passo a passo de cada frente.
   - `BRIEF-JHON.md`: formulários e caça de vagas.
   - `BRIEF-JOE.md`: pessoas com email publicado e cartas.
   - `BRIEF-COMUNICADOR.md`: caixa de entrada, respostas e follow-up.
   - `BRIEF-GRANDES.md` e `BRIEF-GRANDES-JOGOS.md`: rotina diária dos estúdios grandes.
   - `BRIEF-EDITOR.md`: o painel.
   - `BRIEF-HALF-BREAKS.md` e `BRIEF-FORCA-TAREFA.md`: forças-tarefa antigas de formulário, para consulta.
4. `BRIEFING.md` (raiz; `automacao/BRIEFING.md` aponta para ele): o diário da campanha desde 26/08, com cada lição medida. É história e consulta, não fonte de regra nova.

## Registros (só se acrescenta, nunca se apaga)
- `enviados.csv`: toda candidatura e carta enviada.
- `automacao/processados.csv`: o diário de cada rodada, decisão e descarte.
- `automacao/pessoas.csv` e `automacao/PESSOAS-SEM-CARTA.md`: as fichas do Joe (emails mascarados).
- `docs/index.html`: o painel (dados nos arrays DAILY, PORTAIS, STUDIOS, NOVIDADES, AGENDA).
- `alvos.csv`: a lista-mãe de estúdios.

## Filas vivas
- `automacao/FILA-PERSONAGEM-1209.md`, `automacao/bancos-de-talentos-1009.md`, `automacao/fila-do-maestro.md`, `automacao/FILA-DO-VINI.md`, `automacao/ESTUDIOS-SEM-CARTA.md`, `automacao/backlog-estudios.md`.
- `automacao/cartas-prontas/`: fila de cartas lida pelo programa de envio.
- `automacao/ALERTA-CHICO.md` e `automacao/ALERTA-VIGIA.md`: aparecem quando os vigias acham vaga nova.

## Ferramentas (scripts em `automacao/`)
- Conferência: `valida-dashboard.sh` (antes de todo commit), `confere-carta.py`, `monta-html-carta.py`, `regua-veto.py`, `garra.sh`, `dedupe-agora.sh`.
- Caça: `varre-janela-ats.py`, `ronda-disney.sh`, `ronda-paramount.sh`, `jobboard-mayne.py`.
- Envio de cartas: `envia-rascunhos.gs` (roda na conta Google do Vini).
- Painel: `automacao/painel/` (visual) e `monta-painel.py`.

## Outras pastas
- `drafts/`: cartas por estúdio geradas pelo `gera-rascunhos.py`.
- `portfolio/`: o PDF do portfólio.
- `arquivo/`: tudo que já foi usado e saiu de circulação, guardado para consulta.
  - `relatorios/`: relatórios de caça e triagem.
  - `levantamentos/`: censos, filas antigas e varreduras.
  - `cartas-antigas/`: lotes de cartas já enviados.
  - `followups/`: lotes antigos de lembretes.
  - `filas-antigas/`: filas de formulário já esvaziadas.
  - `respostas-antigas/`: respostas de formulários já enviados.
  - `ferramentas-antigas/`: scripts de teste que não rodam mais.
  - `raiz/`: arquivos que estavam soltos na raiz.

## Fora do repositório (nunca entra aqui, o repositório é público)
Dados pessoais dos formulários, senhas, CV e scripts de navegador ficam em `/home/user/apply/`.
O link do CV que expira e os emails completos das fichas ficam só no scratchpad da sessão.
