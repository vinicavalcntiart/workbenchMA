# Só o Vini pode fazer — refeito em 07/09, 06h40 UTC

O arquivo anterior era de 02h50 e ficou velho em quase tudo. Este é o estado real de agora.
Nada aqui é "tente de novo": em todos os casos alguém já foi até a parede e voltou com o mapa.

Ordenado pelo que rende mais por minuto do seu tempo.

---

## 0. A COISA MAIS IMPORTANTE, e leva um minuto: o painel está congelado

**O painel que você abre no navegador está parado em 06/09 às 14h06.** Ele não está quebrado:
está velho. Aberto num navegador de verdade, o `docs/index.html` do repositório renderiza
**478 linhas com zero erro de JavaScript**. A sua tela mostra 236 rotas e 60 à mão; o número
real é **478 de pé, 259 sem candidatura e 102 à mão**.

**A causa:** o secret `DASHBOARD_SENHA` sumiu do repositório, e sem ele o job que publica é
**pulado**. Job pulado faz o run contar como *success*, com check verde, então foram catorze
horas de commits que nunca chegaram ao site e nenhum sinal apontou isso.

**O conserto, e só você pode fazer:** GitHub → Settings → Secrets and variables → Actions →
New repository secret. Nome exato **`DASHBOARD_SENHA`**, valor = a senha que você usa para
abrir o painel. Depois disso qualquer push republica sozinho.

Já deixei o workflow gritando: agora ele grava aviso amarelo com título e escreve no resumo do
run o que houve e como consertar. Continua sem falhar e sem te mandar email, mas para de mentir
calado.

---

## 1. Três formulários prontos, esperando um clique seu

Todos com o formulário **preenchido e conferido campo a campo**. Para você é menos de um minuto
cada, porque só falta o que a automação não pode fazer.

### 1a. Engine Room Hollywood, Los Angeles — falta só ANEXAR UMA IMAGEM
https://www.engineroomhollywood.com/careers/ (role até *READY TO JOIN US*)

**Não tem captcha nenhum.** O envio parou num detalhe só: o campo `File` é obrigatório e o
`accept` dele é `audio/*,video/*,image/*`, ou seja **recusa PDF**. Tentei baixar uma imagem do
seu ArtStation para resolver sozinho e não consegui: o site está atrás do Cloudflare.

**Anexe qualquer render do seu trabalho** e o envio passa. O resto está preenchido.

### 1b. Floating Rock, Wellington — Character Artist do *Kyōryū*
O encaixe mais direto que apareceu na madrugada. Parede: reCAPTCHA do HubSpot.
**As duas respostas que não podem errar:** `Modeller - Character` e `10+ years`.
Dossiê campo a campo em `automacao/respostas-formularios.md`.

### 1c. Plastic Wax, Sydney — banco de talentos
Formulário Wix de quatro etapas, preenchido inteiro **com CV anexado**. O reCAPTCHA aparece
num modal **depois** do Submit. **A resposta que não pode errar:** Working Rights =
`Seeking Sponsorship in Australia`, que é a quarta opção. A terceira, *Valid Working Visa*,
seria mentira — e foi exatamente nela que um seletor da automação caiu na primeira passada.
O defeito já está corrigido no script, que agora **recusa adivinhar** em vez de pegar a
primeira opção da lista.

---

## 1d. UM PDF DE PORTFÓLIO destrava uma classe inteira de formulário

Hoje **duas** candidaturas pararam pelo mesmo motivo, e não é captcha: o formulário exige
**arquivo** de portfólio e a campanha não tem nenhum.

- **Engine Room Hollywood**: campo de arquivo obrigatório que aceita só imagem ou vídeo, e
  recusa PDF. Tentei baixar um render do seu ArtStation para resolver sozinho e o Cloudflare
  bloqueou pelos dois caminhos.
- **Ironbird Creations** (3D Artist, Cracóvia, Teamtailor **sem captcha**, mapeado inteiro):
  *"Please share your portfolio"* é **upload obrigatório, sem alternativa de link**.

**Se você exportar um PDF do portfólio e deixar em `$SCRATCH/apply/`, as duas saem na mesma
rodada, e toda vaga futura com esse campo deixa de ser parede.** É provavelmente a coisa de
maior alavancagem que você pode fazer em cinco minutos, porque destrava um tipo de formulário
inteiro em vez de uma vaga.

---

## 2. Rainbow CGI, Roma e Milão: pendência honesta, decida você
https://www.rbw-cgi.it/careers/

A casa das Winx, animação de personagem estilizado, que é o seu registro. O menu de função tem
**`3D Character`** escrito. Preenchi o formulário inteiro, com CV anexado, e cliquei em enviar:
**os campos limparam, mas não houve POST capturado, texto de confirmação, URL de confirmação
nem email.** Pela regra que fechamos, isso **não conta como enviada**.

**Não reenviei de propósito**, para não trocar uma dúvida por uma candidatura repetida. Se em
alguns dias não vier resposta, mande você e veja a confirmação com os próprios olhos. Parede
declarada: reCAPTCHA v3, que é pontuação de sessão e passa no seu navegador.

---

## 3. O que EU mandei enquanto você dormia, para você não repetir

- **Bulkhead Interactive [IN-STUDIO], Derby** — ENVIADA às 05h30, com URL de confirmação.
  **É a que realoca**: presencial integral, ajuda de realocação e a frase *"Don't worry, we can
  sponsor your visa"*, todas confirmadas na tela. Você tinha mandado a **[REMOTE]** às 04h45,
  que é por projeto e de casa; são requisições diferentes e agora as duas estão feitas.
- **BoomBit, Gdańsk** — ENVIADA, com prova dupla. Ela só existiu porque a resposta automática
  deles dizia, no meio do texto padrão, que **candidatura por email é apagada por GDPR**: a
  carta de 06/09 foi destruída sem leitura. Vale ler o corpo das automáticas antes de arquivar.
- **Larian, Gent** — você mandou, e a confirmação do Lever chegou às 04h35.

---

## 4. Erro meu da madrugada, dito com todas as letras

**Mandei duas candidaturas repetidas para a Sony Pictures Imageworks**, na mesma noite em que
escrevi a trava que deveria impedir isso. A *Experienced Modeler* já tinha ido em 02/09 e a
*Experienced Texture Artist* em 05/09, e eu reenviei as duas.

**Como passou:** escolhi no que trabalhar filtrando o painel por `done=false`; as vagas de
Vancouver estavam com `done=true` e ficaram invisíveis para o meu filtro. Depois reachei as
mesmas requisições pela API do Greenhouse e tratei como novidade. A trava que eu tinha escrito
protegia contra dois agentes ao mesmo tempo, não contra trabalho feito dias antes.

**Consertado na hora e testado:** a `garra.sh` ganhou o comando `checa` e passou a aceitar a URL
da vaga, e recusa com `JA-FEITO` qualquer requisição cuja URL ou ID já apareça no painel ou no
`processados.csv`, **sem olhar estado nenhum**. Os cinco agentes que estavam rodando foram
avisados um a um.

**Por causa disso, a contagem honesta de hoje é 101 estúdios, não 102:** a Sony já era estúdio
trabalhado, e as minhas repetidas a fizeram contar como nova.

---

## 5. Perguntas que só você responde, e por isso ficaram em branco de propósito

Nenhuma foi inventada.

| Onde | O que falta |
|---|---|
| **IOI** | experiência em indústria AAA, e quais jogos você joga |
| **Ghost Ship** e **Keen Games** | vídeo gravado por câmera, impossível por automação |
| **Keen Games** | número de títulos publicados |
| **Coffee Stain** | qual estúdio do grupo você prefere: são 8 opções nomeadas, nenhuma neutra |
| **Sharkmob** e **Weta Workshop** | departamento no genérico porque **nenhuma opção do menu é arte de personagem** |
| **Untold Studios** | departamento no genérico; decisão anterior sua, não revertida |
| **FIN Design** | o email de verificação expira em 1 hora e pedir outro exige login com senha |
| Aba **References** de qualquer Teamtailor | dispara email ao contato na hora e exige pessoa real |

---

## 6. A fila grande, e a leitura honesta dela

`PORTAIS` tem **259 entradas sem candidatura**, mas isso **não são 259 portas abertas**. Depois
de varrer a noite inteira, o veredito dos agentes é que a esmagadora maioria já tem motivo
escrito: captcha de desafio, vaga expirada, **veto de residência** ou porta de email.

**Veto de residência foi a descoberta mais cara da madrugada.** Muita vaga remota exige já morar
no país, e isso não aparece no título: Image Engine (*"required to be based in British Columbia
and eligible to work in Canada"*), thatgamecompany, Shishi, Panna Cotta e People Can Fly caíram
por isso. A Image Engine em especial: eu tinha te recomendado como a sua rota de mudança mais
realista, e ela exige exatamente o que você ainda não tem.

---

## 7. Três fontes do PDF paradas pelo NOSSO ambiente, não pelos sites

`worldwidestudios.net`, `gamedevjobs.io` e `gamefilmhub.com` devolvem, por extenso, do proxy de
saída: **`Host not in allowlist`**. Falham igual no navegador. **Só destrava se você liberar
esses hosts nas configurações de egresso do ambiente.** São três fontes inteiras.

---

## 8. Um canal passivo que trabalha sozinho depois de criado

`80.lv/talent` **não é quadro de vagas**: é marketplace de perfil, com conta obrigatória
(*"Create, publish, and share your profile and your work samples seen by hiring companies"*).
Conta criada trabalha sozinha, e só você pode criar.
