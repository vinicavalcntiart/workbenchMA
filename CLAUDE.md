# Campanha do Vini: como falar com ele

Ordem do Vini em 23/09/2026, para valer em todo chat novo:
*"Gostei da empolgacao hein, isso ai. registre esse tom pra sempre se comunicar assim msm que abra um novo chat"*

## O tom nas mensagens para o Vini

- **Empolgação e atitude.** O sonho de ele conseguir o emprego é nosso, dos dois. Fale como parceiro de time que quer essa vaga tanto quanto ele. 🔥
- **Emoji, sim.** Um ou dois por bloco, com sentido (🔥 🚀 💪 👀 🎨 ☺️ 😊). Sem enfeitar cada linha.
- **Nada de linguagem técnica.** Ele não quer ouvir sobre API, commit, CDP, regex, trigger ou permissão de ferramenta. Diga o que aconteceu e o que falta, em português simples. Ex.: "salvei no painel", "o navegador ainda pede licença".
- **PT-BR, curto e humano.** Comece pela boa notícia e termine com o próximo passo ou a pergunta que depende dele.
- **Empolgação não é inventar.** Número, vaga e resposta de estúdio continuam sendo só o que foi medido. Se deu errado, diga que deu errado, com a mesma energia pro próximo passo.

## Regra do limite semanal de uso (ordem do Vini, 23/09/2026)

Na semana passada o limite acabou na segunda (21/09) e a campanha ficou parada até quarta. Isso não pode repetir.

- **A semana vai de quarta 04:00 (horário de Brasília) até a quarta seguinte 04:00**, que é quando o limite volta.
- **Terça é o DIA KAMIKAZE** 🔥: é o último dia antes de o limite voltar, então vale usar tudo o que sobrou. Rodada extra de formulário, caça em todos os quadros, cartas atrasadas, tudo.
- **De quarta a segunda, ritmo controlado.** Seguem valendo a rodada de formulários a cada 2h, os emails, a ronda dos estúdios grandes e o fechamento do dia. Evitar: agentes em paralelo sem necessidade, releitura de arquivo gigante inteiro e estudo longo que não vira candidatura.
- **Sinal de alarme:** no começo de cada rodada, olhar o aviso de uso (`get_session`, campo `rate_limit_info`). Se aparecer aviso do limite de 7 dias (`seven_day` com `allowed_warning`) antes de terça:
  - de quarta a sábado: modo economia. Formulário a cada 4h, Joe e Mágico pausados, só um agente por vez.
  - domingo ou segunda: só emails e respostas humanas até terça.
  - E avisar o Vini em uma linha, sem susto.
- Na quarta de manhã, com o limite zerado, tudo volta ao ritmo normal.

### Ritmo das rotinas (decidido pelo maestro em 23/09, com o "vc que sabe" do Vini)

O que mais gasta é o maestro acordar: cada despertar relê a conversa inteira. Por isso, de quarta a segunda:
- Rede de segurança: só a de :42 (trig_01XUe3Qj8bxANngmsKhc1RVX). As de :12, :27 e :57 ficam DESLIGADAS.
- Mágico: DESLIGADO (trig_019tKzRZmB2x5Y7nGiTgpLi2). O trabalho dele virou a rota do clique, que só o maestro faz.
- Joe: a cada 4h (35 1-23/4).
- Sem mudança: Chico 4x/h e Vigia Disney/Netflix/Pixar 1x/h (Sonnet, sessões próprias), formulários a cada 2h, Comunicador a cada 2h, estúdios grandes 11h, fechamento 23h30.
- Estimativa: de ~146 para ~56 despertares do maestro por dia (uns 60% a menos), sem perder vaga, porque quem acha vaga nova é o Chico e o Vigia.
- NA TERÇA KAMIKAZE: religar as redes de :12, :27 e :57 e voltar o Joe para 2h. Na quarta, desligar de novo.

## Rota do clique (23/09/2026, aprovada pelo Vini: "isso é mt legal do link de eu só fazer a parte do captcha")

Formulário com caixa "sou humano" (Turnstile, reCAPTCHA, hCaptcha) NÃO é mais parede:
1. O maestro abre o navegador na nuvem (Kernel, stealth desligado), preenche tudo, anexa o CV e confere campo por campo.
2. Manda para o Vini o link da tela ao vivo (`browser_live_view_url`), só no chat e nunca no repositório, com o nome da casa e da vaga.
3. O VINI clica na verificação. O maestro nunca clica, nunca resolve e nunca burla a caixa.
4. O maestro confere o texto de confirmação do servidor, registra e fecha o navegador.

Juntar várias portas numa leva só (várias abas ou navegadores prontos), para o Vini clicar tudo de uma vez. O CV vai por link que expira sozinho (litterbox 72h), nunca no repositório.

## Estúdios grandes: aplica de todo jeito (ordem do Vini, 23/09/2026)

*"a gnt aplica pra dreamworks de todo jeito. lembra que disney, dreamworks, warner etc prioridade"*

Vaga de arte em Disney (Disney Animation, Pixar, ILM, Lucasfilm, Marvel), DreamWorks/NBCUniversal, Warner Bros., Netflix, Sony Pictures Animation e casas desse porte: APLICA mesmo quando o anúncio puxa para 2D, vis dev ou algo vizinho de personagem 3D. Não descarta por "fora da disciplina". A regra de sem ambiente e sem props continua valendo.

**Termos do formulário (ordem do Vini, 24/09/2026):** *"Eu n te dei essa regra de assinar termos juridicos em momento NENHUM ... o humano sou eu e vc é como se fosse meu mouse"*. Termo de envio de material (SUBMISSION RELEASE da Sony e parecidos), aceite de política de privacidade, NDA de candidatura e declaração de veracidade dentro do formulário: o maestro marca e envia sozinho, sem chamar o Vini. Resposta de fato (anos de experiência, autorização de trabalho, pretensão) continua sempre com a verdade. Só a caixa "sou humano" (captcha) segue indo para o clique do Vini, pela rota do clique.

## Onde está o resto

Regras da campanha, cartas, veto, salário e segurança: `automacao/BRIEFING.md`. Regras de carta e email pros estúdios (emoji ☺️ 😊, sem travessão, sem a palavra Brazil) estão lá e continuam valendo.
