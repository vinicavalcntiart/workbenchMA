# Regras do repositório para qualquer agente (leia antes de abrir navegador)

Briefing completo: `BRIEFING.md`. Briefs por função: `automacao/BRIEF-*.md` e `.claude/agents/`.

## Navegador: SEMPRE Kernel em modo stealth (ordem do Vini, 24/09/2026)

1. **Todo navegador nasce pelo helper**, nunca por `chromium.launch()` nem por
   `Kernel().browsers.create()` direto:
   - Node: `const {abrir, esperarDesafio} = require('./navegador_kernel');` → `const b = await abrir({nome: 'meu_script'});`
   - Python: `from navegador_kernel import abrir, esperar_desafio, fechar`
   O helper fixa `stealth=True` e mantém o proxy padrão do stealth. Isso não é parâmetro.
2. **Nunca desligar o stealth nem o proxy** (`stealth: false`, `disable_default_proxy`,
   `clear_proxy`, proxy `direct`). O gancho de commit `automacao/valida-stealth.sh` recusa.
3. **Captcha, Cloudflare, Turnstile ou teste parecido: espera, não clica.** Chame
   `esperarDesafio(page)` / `esperar_desafio(page)`; o resolvedor embutido do Kernel trabalha
   sozinho. Se em 3 minutos ainda estiver na parede, é reputação de IP: registre `bloqueado`
   e siga. Não existe "tentar sem stealth".
4. **Preenchimento e extração são 100% automáticos até o limiar de envio.** O script
   preenche tudo, anexa o que puder e para antes do clique final de enviar, que é do Vini
   (regra 17 do BRIEFING). `--submit` só quando ele autorizar a vaga.
5. **Chave:** `KERNEL_API_KEY` no ambiente da máquina que roda o script. Nunca no repositório.
   Dentro da sessão do Claude o conector do Kernel entra por OAuth e não precisa de chave.
6. Não pergunte se deve usar stealth. A resposta já é sim.

## Outras travas que já existem
- Só rascunho de email pela automação, nunca envio (`.claude/settings.json`, lista deny).
- Telefone, endereço e salário da E-Line nunca entram no repositório (`automacao/valida-dashboard.sh`).
- Ligue os ganchos uma vez por clone: `git config core.hooksPath .githooks`.
