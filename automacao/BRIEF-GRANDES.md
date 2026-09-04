# Rotina dos estúdios grandes (diária)

Motivo, na palavra do Vini: vaga de personagem em estúdio grande é muito concorrida, e quem
chega primeiro tem chance real de ser lido por um humano antes da pilha crescer. A campanha já
viu doze vagas morrerem em poucos dias; em estúdio grande a janela útil é de 3 a 7 dias, e as
primeiras 48 horas valem mais que todo o resto. Por isso esta rotina existe separada das outras:
ela não prospecta nomes novos, ela vigia um conjunto fixo de portais e aplica no mesmo dia.

## O que fazer, em ordem

1. **Varrer os portais oficiais** da lista abaixo, um a um, e listar TODA vaga de personagem,
   visual development, character modeling, character art (inclui Lead e Principal).
2. **Aplicar imediatamente** onde der, sem esperar aprovação, com CV e carta.
3. **Criar alerta de vaga por email** em todo portal que ofereça, para o
   contact@vinicavalcanti.art. Isso é permanente: feito uma vez, não repete.
4. **Registrar** no painel e nos CSVs, e avisar por PushNotification quando aplicar numa vaga
   de personagem de estúdio grande.

## Credenciais

Leem-se de `$SCRATCH/apply/cred.json` (fora do repositório, que é público) ou das variáveis de
ambiente `PORTAL_EMAIL` e `PORTAL_SENHA` quando existirem. NUNCA escreva senha em arquivo do
repositório, em nota do painel, em CSV ou em mensagem de commit.

O Vini tem conta no Workday da Disney. **Atenção técnica**: conta de Workday é por locatário,
ou seja, a conta do portal da Disney não vale automaticamente no da Pixar nem no da Lucasfilm.
Em cada locatário novo, tente entrar com a mesma credencial; se não existir, crie a conta com
o mesmo email e a mesma senha e anote em `cred.json`.

## Lista fixa (fonte oficial de cada um)

| Estúdio | Plataforma | Onde |
|---|---|---|
| Walt Disney Animation Studios | Workday (Disney) | disney.wd5.myworkdayjobs.com |
| Pixar | Workday (locatário próprio) | pixar.wd501.myworkdayjobs.com |
| Lucasfilm e ILM | Workday (Disney) | disney.wd5.myworkdayjobs.com |
| Marvel Studios | Workday (Disney) | disney.wd5.myworkdayjobs.com |
| Disney Television Animation | Workday (Disney) | disney.wd5.myworkdayjobs.com |
| DreamWorks Animation | site próprio + NBCUniversal | dreamworks.com/careers |
| Sony Pictures Animation | Greenhouse | sonypicturesanimation.com/careers |
| Sony Pictures Imageworks | site próprio | imageworks.com/careers |
| Skydance Animation | Lever | jobs.lever.co/skydance |
| Illumination | Lever | illumination.com |
| LAIKA | site próprio | laika.com/careers |
| Netflix Animation | Eightfold | explore.jobs.netflix.net |
| Nickelodeon e Paramount | SuccessFactors | careers.paramount.com |
| Warner Bros. Discovery e Cartoon Network | site próprio | careers.wbd.com |
| Titmouse | site próprio | titmouse.net/careers |
| Reel FX | site próprio | reelfx.com/careers |
| Powerhouse Animation | site próprio | powerhouseanimation.com/careers |
| Bento Box | Lever | jobs.lever.co/bentoboxent |
| ShadowMachine | email | rota por email, já em conversa |
| Angel Studios | Paylocity | angel.com/careers |

## Regras de candidatura

Valem as mesmas da campanha, que estão em `automacao/respostas-formularios.md`:

- Verdade sempre. Direito de trabalho nos EUA e Canadá: **No**. Precisa de patrocínio: **Yes**.
  Aceita realocar: **Yes**, sem ressalva.
- Salário atual: "Confidential under NDA", nunca um valor. PRETENSÃO, regra nova do Vini de 04/09:
  pedir a **base da faixa publicada** no anúncio. Sem faixa, em casa grande sênior ou lead:
  EUA USD 100.000, Canadá CAD 95.000, Reino Unido GBP 50.000, Europa ocidental EUR 55.000,
  Austrália AUD 110.000. Nunca abaixo do piso legal da ocupação, que é o que viabiliza o visto.
  A faixa antiga de USD 46.000 está MORTA. Detalhe completo no BRIEFING.md.
- Emprego atual E-Line Media **sem data de fim**. Se o parser preencher, apague.
- Diversidade e EEO: prefere não responder.
- Nunca escrever nada que sugira hesitação em mudar de país. O mestrado só aparece como
  credencial que fortalece o caso de visto.
- Captcha com desafio (reCAPTCHA v2 de caixa, hCaptcha, Turnstile, DataDome) não se burla:
  registra como "à mão" e segue.
- Uma candidatura por vaga. Só conta como enviada com tela ou email de confirmação.

## Prioridade dentro da rotina

REGRA DO VINI, 02/09: **em estúdio grande não filtre por senioridade.** Vale o que tiver.
Júnior, mid, sênior, lead, principal, estágio remunerado, contrato temporário, tudo entra e
tudo recebe candidatura. O raciocínio dele é que entrar no estúdio importa mais que entrar no
nível certo, e que dentro da casa a mudança de posto é muito mais fácil que de fora. A regra de
contrato efetivo, que vale no resto da campanha, **não se aplica aqui**: em estúdio grande,
temporário também vale. Isso não muda a carta, que continua vendendo o perfil sênior real dele.

1. Qualquer vaga de character artist, character modeler, character design ou visual development,
   em qualquer nível.
2. Vaga de arte próxima disso (modeling, texturing, look dev, groom, generalista 3D).
3. Banco de talentos ou candidatura espontânea, quando não houver vaga.
4. Porta de entrada (vaga de outra função no time de arte), sempre marcada como tal.

## Registro

- `docs/index.html`: array GRANDES para o estado de cada estúdio, PORTAIS para cada vaga nova.
  **Cuidado com a estrutura**: o array STUDIOS termina em
  `].map(([name,country,email,batch,delivery,stage])` e o PROSPECTOS vem logo depois. Ao inserir
  linha no STUDIOS use esse `].map` como âncora, nunca o `];` seguinte.
- `automacao/processados.csv`: uma linha por candidatura (tipo `portal-aplicado`), por alerta
  criado (tipo `alerta-criado`) e por vaga nova vista (tipo `vaga-nova`).
- Entrada na newsletter (array NOVIDADES) quando aplicar em vaga de personagem de estúdio grande.
