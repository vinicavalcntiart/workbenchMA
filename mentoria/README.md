# Agente da agenda da mentoria

Guarda os horários do one-on-one contra tudo que aparece na agenda do Vini e nunca
foi confirmado. Roda no Apps Script, dentro da conta Google dele, sem proxy, sem
token e sem credencial versionada. Mesma escolha do `automacao/envia-rascunhos.gs`.

Link de agendamento: https://calendar.app.google/tFZdRSApDvE1xqsS8
(agendamento "Vini Cavalcanti Mentorship")

## O problema

Convite de reunião da E-Line chega no email e entra na agenda como **sem resposta**
(`needsAction`). O Vini não clica em Sim. O agendamento de horários do Google só
desconta da disponibilidade o que ele considera ocupado, e compromisso sem resposta
escorrega. Resultado: o aluno abre o link, vê a quarta às 14h livre, marca, e o
horário já era da E-Line.

## Como o agente resolve

Ele não tenta convencer o agendamento a respeitar o convite. Ele traduz o convite
para uma forma que o agendamento é obrigado a enxergar: um evento **do próprio Vini**,
sem convidados, marcado como Ocupado. Não há RSVP para ficar pendente, então não há
o que ignorar.

```
convite sem resposta            bloqueio criado pelo agente
14:00-15:00                     13:45-15:15
rsvp = needsAction      --->    dono: o Vini
o agendamento ignora            sem convidados, transparency = opaque
                                o agendamento respeita
```

Cada bloqueio carrega uma etiqueta interna (`extendedProperties.private.marca`) com a
chave do compromisso que o originou. É por essa etiqueta que o agente reconhece o que
é obra dele, ajusta quando a reunião muda de horário e limpa quando ela é cancelada.
Ele nunca toca em evento que não criou.

## Regra de ouro

**O agente só tira disponibilidade. Ele nunca abre horário.**

Ele não mexe na configuração do agendamento, não alarga janela de trabalho, não move
sessão de aluno por conta própria. A única remoção que faz é a do bloqueio que ele
mesmo criou, quando o compromisso de origem some, é cancelado ou é recusado. Se nem
isso você quiser, ponha `REMOVER_ORFAOS: false`.

## O que ele cobre

| Situação | O que acontece |
|---|---|
| Convite sem resposta na agenda | vira bloqueio, com respiro de 15 min dos dois lados |
| Convite que você recusou | ignorado, você está livre mesmo |
| Evento marcado como "Livre" | ignorado |
| Aniversário, feriado, local de trabalho | ignorado |
| Reunião que mudou de horário | o bloqueio acompanha |
| Reunião cancelada | o bloqueio some |
| Convite `.ics` que ficou só no email | vira bloqueio, com o UID conferido contra a agenda para não duplicar |
| One-on-one já marcado que ficou em cima de uma reunião nova | email urgente para o Vini; email de remarcação ao aluno só se `AUTO_REMARCAR` estiver ligado |
| Janela protegida (almoço, foco) | bloqueio fixo recorrente, desligado por padrão |
| Teto de one-on-ones por dia | fecha o resto do dia ao bater o teto, desligado por padrão |

## Instalação

1. Abra https://script.google.com, **Novo projeto**, cole `agente-agenda.gs` inteiro.
2. Menu da esquerda, **Serviços** (+): adicione **Google Calendar API**. Ela entra como
   `Calendar`. Sem isso o script não lê o RSVP nem grava a etiqueta dos bloqueios.
3. Confira o bloco `CFG` no topo do arquivo. O que costuma mudar:
   - `CALENDARIOS_FONTE`: acrescente o id de qualquer agenda secundária (E-Line, pessoal)
     que também deva tirar disponibilidade.
   - `BUFFER_ANTES_MIN` / `BUFFER_DEPOIS_MIN`: respiro em volta de cada compromisso.
   - `AUTO_REMARCAR`: false por padrão. Ligue quando quiser que o agente escreva ao aluno
     sozinho pedindo para remarcar.
4. Com `SIMULAR: true`, rode a função **`sincronizarAgenda`** e autorize. Abra o log
   (Ctrl+Enter): ele lista tudo que criaria, sem tocar em nada.
5. Se o log fizer sentido, troque `SIMULAR` para `false` e rode **`instalarAcionador`**
   uma vez. A partir daí ele roda sozinho a cada 15 minutos.
6. Em calendar.google.com, abra o agendamento "Vini Cavalcanti Mentorship" e confirme que
   a agenda de `CALENDARIO_ALVO` está na lista de **agendas verificadas para conflito**.
   Sem isso o bloqueio existe mas não é consultado.

## Funções que você roda à mão

| Função | Para quê |
|---|---|
| `sincronizarAgenda` | a rodada normal; é ela que o acionador chama |
| `diagnostico` | lista os compromissos das próximas 2 semanas e diz, para cada um, se o agente o considera ocupado e por quê. Use quando algo passar batido |
| `resumoMentorados` | panorama dos alunos: sessões, semana do programa de 10, sessões marcadas à frente |
| `instalarAcionador` / `removerAcionador` | liga e desliga a rodada automática |

## Emails que ele manda

- **Urgente, para o Vini**: quando um one-on-one já marcado está em cima de outro
  compromisso. Sempre, sem exceção.
- **Resumo, para o Vini**: no máximo uma vez por dia, e só quando algo mudou. Rodada sem
  novidade não gera email. (A caixa dele já encheu uma vez com aviso automático, em 01/09.)
- **Remarcação, para o aluno, em inglês**: só com `AUTO_REMARCAR: true`. Aponta o link de
  agendamento e não dá motivo pessoal.

## Teste

A lógica pura (diferença de bloqueios, leitura de `.ics`, detecção de colisão, janelas
protegidas) roda fora do Google, com agenda falsa:

```
bash mentoria/teste/roda.sh
```

`mentoria/teste/stubs.js` finge os objetos do Apps Script; `testa-agente.js` monta uma
agenda com reunião sem resposta, reunião recusada, evento livre, aniversário, um
one-on-one em cima da reunião e dois bloqueios antigos, e confere o que o agente faz
com cada um.

## Limites conhecidos

- Evento de dia inteiro é ignorado por padrão (`BLOQUEAR_DIA_INTEIRO: false`). Um "PTO"
  de dia inteiro derrubaria o dia todo, e nem sempre é isso que você quer.
- A varredura do Gmail olha os últimos 14 dias de mensagens com anexo `.ics` e no máximo
  50 conversas por rodada. Convite muito antigo que nunca entrou na agenda fica de fora.
- A execução do Apps Script tem teto de 6 minutos. Com horizonte de 60 dias e a varredura
  do Gmail ligada, a rodada leva segundos; se você esticar muito o horizonte, reduza
  `DIAS_GMAIL` primeiro.
- O agente identifica o one-on-one por texto do título ou da descrição
  (`PADRAO_ONE_ON_ONE`). Se você renomear o agendamento, ajuste o padrão.
