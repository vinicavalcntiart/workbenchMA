/**
 * Agente da agenda da mentoria — Vini Cavalcanti
 * =============================================
 *
 * O PROBLEMA
 * Convites da E-Line (e de qualquer outro time) chegam no email e entram na agenda
 * como "sem resposta". O Vini não clica em Sim. O agendamento de horários do Google
 * (calendar.app.google) só evita conflito com o que ele considera ocupado, então
 * esses compromissos passam batido e o aluno marca o one-on-one em cima da reunião.
 *
 * A SOLUÇÃO
 * Este agente varre os compromissos reais e, para cada um, cria na agenda um bloqueio
 * próprio ("guard"): evento do próprio Vini, sem convidados, marcado como Ocupado.
 * Bloqueio assim o agendamento NUNCA ignora. É o mesmo compromisso, mas numa forma
 * que a página de reservas obrigatoriamente enxerga.
 *
 * REGRA DE OURO (pedido explícito do Vini)
 * O agente só TIRA disponibilidade. Ele nunca abre horário, nunca mexe na configuração
 * do agendamento, nunca alarga janela de trabalho. A única remoção de bloqueio que ele
 * faz é a do bloqueio que ele mesmo criou quando o compromisso de origem sumiu, foi
 * cancelado ou foi recusado — e mesmo isso é desligável em REMOVER_ORFAOS.
 *
 * COMO USAR (uma vez)
 * 1. https://script.google.com > "Novo projeto" > cole este arquivo inteiro.
 * 2. Menu da esquerda, "Serviços" (+): adicione "Google Calendar API" (fica como `Calendar`).
 * 3. Confira o bloco CFG abaixo. Com SIMULAR = true, rode `sincronizarAgenda` e autorize.
 *    O log (Ctrl+Enter) lista tudo que ele criaria sem tocar em nada.
 * 4. Troque SIMULAR para false e rode `instalarAcionador` uma vez. A partir daí ele
 *    roda sozinho a cada 15 minutos.
 * 5. No calendar.google.com, abra o agendamento "Vini Cavalcanti Mentorship" e confirme
 *    que a agenda em CALENDARIO_ALVO está na lista de "agendas verificadas".
 */

/* ============================== CONFIGURAÇÃO ============================== */

const CFG = {
  // Agenda onde os bloqueios são criados. Tem que ser uma das agendas que o
  // agendamento de horários verifica para conflito.
  CALENDARIO_ALVO: 'primary',

  // Agendas onde os compromissos reais aparecem. Acrescente aqui o id de qualquer
  // agenda secundária (E-Line, pessoal) que também deva tirar disponibilidade.
  CALENDARIOS_FONTE: ['primary'],

  // Quantos dias à frente o agente cuida.
  HORIZONTE_DIAS: 60,

  // Respiro antes e depois de cada compromisso, em minutos.
  BUFFER_ANTES_MIN: 15,
  BUFFER_DEPOIS_MIN: 15,

  // Situações de RSVP que contam como ocupado. 'needsAction' é o ponto central:
  // é o convite que ele nunca confirma. 'declined' fica de fora de propósito.
  RSVP_OCUPADO: ['accepted', 'needsAction', 'tentative'],

  // Como reconhecer um one-on-one vindo do link de agendamento.
  PADRAO_ONE_ON_ONE: 'mentorship|mentoria|one[- ]?on[- ]?one|1:1',

  // Títulos que nunca geram bloqueio.
  IGNORAR_TITULO: 'anivers[áa]rio|birthday|feriado|holiday',

  // Evento de dia inteiro derruba o dia todo. Por padrão ele é ignorado.
  BLOQUEAR_DIA_INTEIRO: false,

  // Janelas fixas que ficam sempre fora do alcance dos alunos.
  // dias: 0=domingo ... 6=sábado. Exemplo pronto, é só descomentar:
  // JANELAS_PROTEGIDAS: [{ dias: [1,2,3,4,5], de: '12:00', ate: '13:30', motivo: 'almoço' }],
  JANELAS_PROTEGIDAS: [],
  HORIZONTE_JANELAS_DIAS: 21,

  // Teto de one-on-ones por dia. Batido o teto, o resto do dia é fechado.
  // 0 desliga.
  MAX_ONE_ON_ONE_POR_DIA: 0,

  // Antecedência mínima que o aluno precisa dar para marcar, em horas.
  // A trava de verdade é a nativa do agendamento do Google (README, seção
  // "Antecedência mínima"). Aqui ela serve de rede: o agente flagra a sessão
  // marcada em cima da hora e avisa você. 0 desliga.
  AVISO_MINIMO_HORAS: 24,

  // Trava dura: bloqueio contínuo cobrindo as próximas AVISO_MINIMO_HORAS.
  // Funciona, mas te deixa permanentemente ocupado nas próximas 24h para QUALQUER
  // um que consulte sua agenda, inclusive o pessoal da E-Line procurando horário.
  // Por isso vem desligado. Use só se a trava nativa não der conta.
  BLOQUEIO_ROLANTE: false,

  // Varredura do Gmail: pega convite .ics que ainda não virou evento na agenda.
  VARRER_GMAIL: true,
  DIAS_GMAIL: 14,

  // Apagar o bloqueio quando o compromisso de origem some, é cancelado ou recusado.
  REMOVER_ORFAOS: true,

  // Quando uma reunião nova cai em cima de um one-on-one JÁ marcado, o agente
  // sempre avisa o Vini. Com true, ele também escreve para o aluno pedindo
  // remarcação. Fica false porque é ação de mão única com terceiro.
  AUTO_REMARCAR: false,

  LINK_AGENDAMENTO: 'https://calendar.app.google/tFZdRSApDvE1xqsS8',
  NOME_MENTOR: 'Vini',

  // Vazio = a própria conta que roda o script.
  EMAIL_AVISO: '',

  // true = só escreve no log, não cria nem apaga nada.
  SIMULAR: true,
};

/* =============================== CONSTANTES =============================== */

const MARCA = 'mentoria-guard';
const VERSAO = 'v1';
const TITULO_BLOQUEIO = 'Busy';
const COR_BLOQUEIO = '8'; // grafite
const CHAVE_ULTIMO_RESUMO = 'mentoria.ultimoResumo';
const CHAVE_AVISOS = 'mentoria.avisos';

/* ============================ FUNÇÃO PRINCIPAL ============================ */

function sincronizarAgenda() {
  const tz = fusoDoCalendario();
  const agora = new Date();
  const ini = new Date(agora.getTime() - 60 * 60 * 1000);
  const fim = new Date(agora.getTime() + CFG.HORIZONTE_DIAS * 24 * 60 * 60 * 1000);

  const compromissos = [];
  const oneOnOnes = [];

  CFG.CALENDARIOS_FONTE.forEach(function (calId) {
    listarEventos(calId, ini, fim).forEach(function (ev) {
      if (ehBloqueio(ev)) return;
      if (!ocupado(ev)) return;
      const item = { calId: calId, ev: ev, inicio: quando(ev.start), fim: quando(ev.end) };
      if (!item.inicio || !item.fim) return;
      compromissos.push(item);
      if (ehOneOnOne(ev)) oneOnOnes.push(item);
    });
  });

  // ---- o que deveria existir ----
  const desejados = {};
  compromissos.forEach(function (c) {
    const chave = c.calId + ':' + c.ev.id;
    desejados[chave] = {
      chave: chave,
      inicio: new Date(c.inicio.getTime() - CFG.BUFFER_ANTES_MIN * 60000),
      fim: new Date(c.fim.getTime() + CFG.BUFFER_DEPOIS_MIN * 60000),
      motivo: (c.ev.summary || 'compromisso sem título') + rsvpRotulo(c.ev),
    };
  });

  janelasProtegidas(ini, fim, tz).forEach(function (d) { desejados[d.chave] = d; });
  diasNoTeto(oneOnOnes, ini, fim, tz).forEach(function (d) { desejados[d.chave] = d; });
  if (CFG.VARRER_GMAIL) {
    convitesSoNoGmail(ini, fim).forEach(function (d) { desejados[d.chave] = d; });
  }
  const rolante = bloqueioRolante(agora);
  if (rolante) desejados[rolante.chave] = rolante;

  // ---- o que já existe ----
  const existentes = {};
  listarEventos(CFG.CALENDARIO_ALVO, ini, fim, { privateExtendedProperty: 'marca=' + MARCA })
    .forEach(function (ev) {
      const p = (ev.extendedProperties || {}).private || {};
      if (p.chave) existentes[p.chave] = ev;
    });

  // ---- diferença ----
  const criados = [], ajustados = [], removidos = [];

  Object.keys(desejados).forEach(function (chave) {
    const d = desejados[chave];
    const atual = existentes[chave];
    const assin = assinatura(d.inicio, d.fim);
    if (!atual) {
      criarBloqueio(d, tz);
      criados.push(d);
    } else if (((atual.extendedProperties || {}).private || {}).assinatura !== assin) {
      ajustarBloqueio(atual, d, tz);
      ajustados.push(d);
    }
  });

  if (CFG.REMOVER_ORFAOS) {
    Object.keys(existentes).forEach(function (chave) {
      if (desejados[chave]) return;
      apagarBloqueio(existentes[chave]);
      removidos.push(existentes[chave].summary + ' ' + formata(quando(existentes[chave].start), tz));
    });
  }

  const colisoes = detectarColisoes(compromissos, oneOnOnes);
  const emCimaDaHora = detectarAvisoCurto(oneOnOnes, agora);
  relatar(criados, ajustados, removidos, colisoes, emCimaDaHora, tz);

  return {
    criados: criados.length,
    ajustados: ajustados.length,
    removidos: removidos.length,
    colisoes: colisoes.length,
    emCimaDaHora: emCimaDaHora.length,
  };
}

/* ============================ LEITURA DA AGENDA ============================ */

function listarEventos(calId, ini, fim, extra) {
  const itens = [];
  let pageToken = null;
  do {
    const params = {
      timeMin: ini.toISOString(),
      timeMax: fim.toISOString(),
      singleEvents: true,
      orderBy: 'startTime',
      maxResults: 2500,
      showDeleted: false,
      pageToken: pageToken,
    };
    if (extra) Object.keys(extra).forEach(function (k) { params[k] = extra[k]; });
    const resp = Calendar.Events.list(calId, params);
    (resp.items || []).forEach(function (ev) { itens.push(ev); });
    pageToken = resp.nextPageToken;
  } while (pageToken);
  return itens;
}

function ocupado(ev) {
  if (ev.status === 'cancelled') return false;
  if (ev.transparency === 'transparent') return false;                 // marcado como Livre
  if (ev.eventType === 'workingLocation' || ev.eventType === 'birthday') return false;
  if (ev.start && ev.start.date && !CFG.BLOQUEAR_DIA_INTEIRO) return false;
  if (new RegExp(CFG.IGNORAR_TITULO, 'i').test(ev.summary || '')) return false;
  const eu = (ev.attendees || []).filter(function (a) { return a.self; })[0];
  if (eu && CFG.RSVP_OCUPADO.indexOf(eu.responseStatus) === -1) return false;  // recusado
  return true;
}

function ehBloqueio(ev) {
  const p = (ev.extendedProperties || {}).private || {};
  return p.marca === MARCA;
}

function ehOneOnOne(ev) {
  if (ehBloqueio(ev)) return false;
  const texto = (ev.summary || '') + ' ' + (ev.description || '');
  return new RegExp(CFG.PADRAO_ONE_ON_ONE, 'i').test(texto);
}

function rsvpRotulo(ev) {
  const eu = (ev.attendees || []).filter(function (a) { return a.self; })[0];
  if (!eu) return '';
  if (eu.responseStatus === 'needsAction') return ' [convite sem resposta]';
  if (eu.responseStatus === 'tentative') return ' [talvez]';
  return '';
}

function quando(bloco) {
  if (!bloco) return null;
  if (bloco.dateTime) return new Date(bloco.dateTime);
  if (bloco.date) return new Date(bloco.date + 'T00:00:00');
  return null;
}

function fusoDoCalendario() {
  try {
    return Calendar.Calendars.get(CFG.CALENDARIO_ALVO).timeZone || Session.getScriptTimeZone();
  } catch (e) {
    return Session.getScriptTimeZone();
  }
}

/* ============================ ESCRITA NA AGENDA ============================ */

function assinatura(ini, fim) {
  return ini.toISOString() + '|' + fim.toISOString();
}

function corpoBloqueio(d, tz) {
  return {
    summary: TITULO_BLOQUEIO,
    description: 'Bloqueio automático do agente da mentoria.\nMotivo: ' + d.motivo +
      '\n\nEste evento existe só para o link de agendamento enxergar o horário como ocupado.\n' +
      'Se você apagar à mão, o agente recria na próxima rodada enquanto o compromisso de origem existir.',
    start: { dateTime: d.inicio.toISOString(), timeZone: tz },
    end: { dateTime: d.fim.toISOString(), timeZone: tz },
    transparency: 'opaque',
    visibility: 'private',
    colorId: COR_BLOQUEIO,
    reminders: { useDefault: false, overrides: [] },
    extendedProperties: {
      private: {
        marca: MARCA,
        versao: VERSAO,
        chave: d.chave,
        assinatura: assinatura(d.inicio, d.fim),
      },
    },
  };
}

function criarBloqueio(d, tz) {
  if (CFG.SIMULAR) { Logger.log('[simulação] criaria bloqueio ' + d.chave + ' :: ' + d.motivo); return; }
  Calendar.Events.insert(corpoBloqueio(d, tz), CFG.CALENDARIO_ALVO);
}

function ajustarBloqueio(atual, d, tz) {
  if (CFG.SIMULAR) { Logger.log('[simulação] ajustaria bloqueio ' + d.chave + ' :: ' + d.motivo); return; }
  Calendar.Events.patch(corpoBloqueio(d, tz), CFG.CALENDARIO_ALVO, atual.id);
}

function apagarBloqueio(ev) {
  if (CFG.SIMULAR) { Logger.log('[simulação] apagaria bloqueio órfão ' + ev.id); return; }
  Calendar.Events.remove(CFG.CALENDARIO_ALVO, ev.id);
}

/* ======================== BLOQUEIOS QUE NÃO VÊM DE EVENTO ======================== */

function janelasProtegidas(ini, fim, tz) {
  const saida = [];
  if (!CFG.JANELAS_PROTEGIDAS.length) return saida;
  const limite = new Date(Math.min(fim.getTime(), ini.getTime() + CFG.HORIZONTE_JANELAS_DIAS * 24 * 60 * 60 * 1000));
  for (let dia = new Date(ini); dia < limite; dia = new Date(dia.getTime() + 24 * 60 * 60 * 1000)) {
    const rotulo = Utilities.formatDate(dia, tz, 'yyyy-MM-dd');
    const diaSemana = diaDaSemana(dia, tz); // 0=domingo ... 6=sábado
    CFG.JANELAS_PROTEGIDAS.forEach(function (j) {
      if (j.dias.indexOf(diaSemana) === -1) return;
      const a = horaNoDia(rotulo, j.de, tz);
      const b = horaNoDia(rotulo, j.ate, tz);
      if (b <= ini) return;
      saida.push({
        chave: 'janela:' + rotulo + ':' + j.de + '-' + j.ate,
        inicio: a,
        fim: b,
        motivo: 'janela protegida (' + (j.motivo || j.de + '-' + j.ate) + ')',
      });
    });
  }
  return saida;
}

function diasNoTeto(oneOnOnes, ini, fim, tz) {
  const saida = [];
  if (!CFG.MAX_ONE_ON_ONE_POR_DIA) return saida;
  const porDia = {};
  oneOnOnes.forEach(function (s) {
    const dia = Utilities.formatDate(s.inicio, tz, 'yyyy-MM-dd');
    porDia[dia] = (porDia[dia] || 0) + 1;
  });
  Object.keys(porDia).forEach(function (dia) {
    if (porDia[dia] < CFG.MAX_ONE_ON_ONE_POR_DIA) return;
    saida.push({
      chave: 'teto:' + dia,
      inicio: horaNoDia(dia, '00:00', tz),
      fim: horaNoDia(dia, '23:59', tz),
      motivo: 'teto de ' + CFG.MAX_ONE_ON_ONE_POR_DIA + ' one-on-ones no dia',
    });
  });
  return saida;
}

function diaDaSemana(d, tz) {
  const mapa = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
  const sigla = Utilities.formatDate(d, tz, 'EEE').substring(0, 3);
  return mapa[sigla] !== undefined ? mapa[sigla] : d.getDay();
}

/**
 * Trava dura da antecedência mínima: um bloqueio contínuo cobrindo daqui até o fim
 * da janela de aviso. Ele rola junto com o relógio, arredondado para múltiplos de
 * 15 min (para baixo no começo, para cima no fim, nunca cobrindo menos do que a
 * política pede). Desligado por padrão.
 */
function bloqueioRolante(agora) {
  if (!CFG.BLOQUEIO_ROLANTE || !CFG.AVISO_MINIMO_HORAS) return null;
  const QUARTO = 15 * 60000;
  return {
    chave: 'aviso-minimo',
    inicio: new Date(Math.floor(agora.getTime() / QUARTO) * QUARTO),
    fim: new Date(Math.ceil((agora.getTime() + CFG.AVISO_MINIMO_HORAS * 3600000) / QUARTO) * QUARTO),
    motivo: 'antecedência mínima de ' + CFG.AVISO_MINIMO_HORAS + 'h para novas reservas',
  };
}

/**
 * Sessões marcadas com menos antecedência do que a política pede.
 * Compara o horário da sessão com o momento em que ela foi CRIADA, não com agora.
 * Sessão marcada há duas semanas para amanhã está em dia; sessão marcada hoje de
 * manhã para hoje à tarde, não.
 */
function detectarAvisoCurto(oneOnOnes, agora) {
  if (!CFG.AVISO_MINIMO_HORAS) return [];
  const limite = CFG.AVISO_MINIMO_HORAS * 3600000;
  return oneOnOnes.filter(function (s) {
    if (s.inicio <= agora) return false;
    if (!s.ev.created) return false;
    return (s.inicio.getTime() - new Date(s.ev.created).getTime()) < limite;
  });
}

function horaNoDia(diaISO, hhmm, tz) {
  return Utilities.parseDate(diaISO + ' ' + hhmm, tz, 'yyyy-MM-dd HH:mm');
}

/* ===================== CONVITES QUE FICARAM SÓ NO GMAIL ===================== */

function convitesSoNoGmail(ini, fim) {
  const saida = [];
  const vistos = {};
  let threads = [];
  try {
    threads = GmailApp.search('has:attachment filename:ics newer_than:' + CFG.DIAS_GMAIL + 'd', 0, 50);
  } catch (e) {
    Logger.log('Gmail indisponível: ' + e);
    return saida;
  }
  threads.forEach(function (t) {
    t.getMessages().forEach(function (m) {
      m.getAttachments({ includeInlineImages: false, includeAttachments: true }).forEach(function (a) {
        const nome = a.getName() || '';
        const tipo = a.getContentType() || '';
        if (!/\.ics$/i.test(nome) && tipo.indexOf('text/calendar') === -1) return;
        let eventos = [];
        try { eventos = lerIcs(a.getDataAsString()); } catch (e) { return; }
        eventos.forEach(function (e) {
          if (!e.uid || !e.inicio) return;
          if (e.metodo === 'CANCEL' || e.status === 'CANCELLED') return;
          if (vistos[e.uid]) return;
          vistos[e.uid] = true;
          const comeco = e.inicio;
          const termino = e.fim || new Date(comeco.getTime() + 60 * 60000);
          if (termino <= ini || comeco >= fim) return;
          if (jaEstaNaAgenda(e.uid)) return;
          saida.push({
            chave: 'gmail:' + e.uid,
            inicio: new Date(comeco.getTime() - CFG.BUFFER_ANTES_MIN * 60000),
            fim: new Date(termino.getTime() + CFG.BUFFER_DEPOIS_MIN * 60000),
            motivo: 'convite no email que não entrou na agenda: ' + (e.summary || 'sem título'),
          });
        });
      });
    });
  });
  return saida;
}

function jaEstaNaAgenda(uid) {
  const alvos = CFG.CALENDARIOS_FONTE.concat([CFG.CALENDARIO_ALVO]);
  for (let i = 0; i < alvos.length; i++) {
    try {
      const r = Calendar.Events.list(alvos[i], { iCalUID: uid, showDeleted: false, maxResults: 5 });
      const vivos = (r.items || []).filter(function (ev) { return ev.status !== 'cancelled'; });
      if (vivos.length) return true;
    } catch (e) { /* agenda sem permissão de busca por uid: segue */ }
  }
  return false;
}

function lerIcs(texto) {
  const cruas = String(texto).replace(/\r\n/g, '\n').split('\n');
  const linhas = [];
  cruas.forEach(function (l) {
    if ((l.charAt(0) === ' ' || l.charAt(0) === '\t') && linhas.length) {
      linhas[linhas.length - 1] += l.substring(1);
    } else {
      linhas.push(l);
    }
  });

  const saida = [];
  let metodo = '';
  let atual = null;
  linhas.forEach(function (l) {
    if (/^METHOD:/i.test(l)) { metodo = l.split(':')[1].trim().toUpperCase(); return; }
    if (/^BEGIN:VEVENT/i.test(l)) { atual = {}; return; }
    if (/^END:VEVENT/i.test(l)) { if (atual) { atual.metodo = metodo; saida.push(atual); } atual = null; return; }
    if (!atual) return;
    const corte = l.indexOf(':');
    if (corte < 0) return;
    const cabeca = l.substring(0, corte);
    const valor = l.substring(corte + 1).trim();
    const nome = cabeca.split(';')[0].toUpperCase();
    if (nome === 'UID') atual.uid = valor;
    else if (nome === 'SUMMARY') atual.summary = valor;
    else if (nome === 'STATUS') atual.status = valor.toUpperCase();
    else if (nome === 'DTSTART') atual.inicio = dataIcs(cabeca, valor);
    else if (nome === 'DTEND') atual.fim = dataIcs(cabeca, valor);
  });
  return saida;
}

function dataIcs(cabeca, valor) {
  if (/^\d{8}$/.test(valor)) return null;                    // dia inteiro: não bloqueia
  if (!/^\d{8}T\d{6}Z?$/.test(valor)) return null;
  if (/Z$/.test(valor)) {
    return Utilities.parseDate(valor.replace(/Z$/, ''), 'UTC', "yyyyMMdd'T'HHmmss");
  }
  const tzid = (cabeca.match(/TZID=([^;:]+)/i) || [])[1];
  try {
    return Utilities.parseDate(valor, tzid || Session.getScriptTimeZone(), "yyyyMMdd'T'HHmmss");
  } catch (e) {
    return Utilities.parseDate(valor, Session.getScriptTimeZone(), "yyyyMMdd'T'HHmmss");
  }
}

/* ================================ COLISÕES ================================ */

function detectarColisoes(compromissos, oneOnOnes) {
  const outros = compromissos.filter(function (c) { return !ehOneOnOne(c.ev); });
  const saida = [];
  oneOnOnes.forEach(function (s) {
    outros.forEach(function (o) {
      if (o.inicio < s.fim && s.inicio < o.fim) {
        saida.push({ sessao: s, conflito: o });
      }
    });
  });
  return saida;
}

/* =============================== AVISOS =============================== */

function destinatario() {
  return CFG.EMAIL_AVISO || Session.getActiveUser().getEmail();
}

function formata(d, tz) {
  return d ? Utilities.formatDate(d, tz, "dd/MM 'às' HH:mm") : '?';
}

function relatar(criados, ajustados, removidos, colisoes, emCimaDaHora, tz) {
  const linhas = [];
  linhas.push(criados.length + ' bloqueio(s) criado(s), ' + ajustados.length + ' ajustado(s), ' +
    removidos.length + ' removido(s), ' + colisoes.length + ' colisão(ões), ' +
    emCimaDaHora.length + ' em cima da hora');
  criados.forEach(function (d) { linhas.push('  + ' + formata(d.inicio, tz) + ' — ' + d.motivo); });
  ajustados.forEach(function (d) { linhas.push('  ~ ' + formata(d.inicio, tz) + ' — ' + d.motivo); });
  removidos.forEach(function (r) { linhas.push('  - ' + r); });
  colisoes.forEach(function (c) {
    linhas.push('  ! ' + formata(c.sessao.inicio, tz) + ' one-on-one com "' + (c.conflito.ev.summary || 'compromisso') + '"');
  });
  emCimaDaHora.forEach(function (s) {
    linhas.push('  ! ' + formata(s.inicio, tz) + ' one-on-one marcado com menos de ' + CFG.AVISO_MINIMO_HORAS + 'h');
  });
  Logger.log(linhas.join('\n'));

  if (CFG.SIMULAR) return;
  if (colisoes.length) avisarColisoes(colisoes, tz);
  if (emCimaDaHora.length) avisarAvisoCurto(emCimaDaHora, tz);
  if (!criados.length && !ajustados.length && !removidos.length) return;

  // Resumo de rotina no máximo uma vez por dia, para não encher a caixa.
  const props = PropertiesService.getScriptProperties();
  const hoje = Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd');
  if (props.getProperty(CHAVE_ULTIMO_RESUMO) === hoje) return;
  props.setProperty(CHAVE_ULTIMO_RESUMO, hoje);
  GmailApp.sendEmail(destinatario(), 'Agenda da mentoria: ' + criados.length + ' novo(s) bloqueio(s)', linhas.join('\n'));
}

/**
 * Guarda o que já foi avisado, para o mesmo conflito não render um email a cada
 * rodada de 15 minutos. Devolve true se este aviso já saiu antes.
 */
function jaAvisado(chave) {
  const props = PropertiesService.getScriptProperties();
  let mapa = {};
  try { mapa = JSON.parse(props.getProperty(CHAVE_AVISOS) || '{}'); } catch (e) { mapa = {}; }
  const agora = Date.now();
  const validade = 30 * 24 * 60 * 60 * 1000;
  Object.keys(mapa).forEach(function (k) { if (agora - mapa[k] > validade) delete mapa[k]; });
  const visto = mapa.hasOwnProperty(chave);
  if (!visto) mapa[chave] = agora;
  props.setProperty(CHAVE_AVISOS, JSON.stringify(mapa));
  return visto;
}

function avisarColisoes(todas, tz) {
  const colisoes = todas.filter(function (c) {
    return !jaAvisado('colisao:' + c.sessao.ev.id + ':' + c.conflito.ev.id);
  });
  if (!colisoes.length) return;

  const linhas = ['Um one-on-one já marcado está em cima de outro compromisso.', ''];
  colisoes.forEach(function (c) {
    linhas.push('One-on-one: ' + formata(c.sessao.inicio, tz) + ' — ' + (c.sessao.ev.summary || ''));
    linhas.push('Conflito:   ' + formata(c.conflito.inicio, tz) + ' — ' + (c.conflito.ev.summary || '') + rsvpRotulo(c.conflito.ev));
    linhas.push('Aluno:      ' + (emailDoAluno(c.sessao.ev) || 'não identificado'));
    linhas.push('');
  });
  linhas.push(CFG.AUTO_REMARCAR
    ? 'AUTO_REMARCAR está ligado: o pedido de remarcação já foi enviado ao aluno.'
    : 'AUTO_REMARCAR está desligado. Nenhum email foi para o aluno. Resolva à mão ou ligue a chave em CFG.');
  GmailApp.sendEmail(destinatario(), 'URGENTE: conflito no one-on-one da mentoria', linhas.join('\n'));

  if (!CFG.AUTO_REMARCAR) return;
  colisoes.forEach(function (c) {
    const email = emailDoAluno(c.sessao.ev);
    if (!email) return;
    GmailApp.sendEmail(email, 'Need to move our one-on-one', textoRemarcacao(c.sessao, tz));
  });
}

function avisarAvisoCurto(todas, tz) {
  const sessoes = todas.filter(function (s) { return !jaAvisado('aviso-curto:' + s.ev.id); });
  if (!sessoes.length) return;

  const linhas = ['Sessão marcada com menos de ' + CFG.AVISO_MINIMO_HORAS + 'h de antecedência.', ''];
  sessoes.forEach(function (s) {
    linhas.push('One-on-one: ' + formata(s.inicio, tz));
    linhas.push('Marcada em: ' + formata(new Date(s.ev.created), tz));
    linhas.push('Aluno:      ' + (emailDoAluno(s.ev) || 'não identificado'));
    linhas.push('');
  });
  linhas.push('Se isso está acontecendo com frequência, a trava nativa do agendamento');
  linhas.push('provavelmente está desligada. Veja "Antecedência mínima" em mentoria/README.md.');
  linhas.push('');
  linhas.push(CFG.AUTO_REMARCAR
    ? 'AUTO_REMARCAR está ligado: o pedido de remarcação já foi enviado ao aluno.'
    : 'AUTO_REMARCAR está desligado. Nenhum email foi para o aluno.');
  GmailApp.sendEmail(destinatario(), 'Mentoria: sessão marcada em cima da hora', linhas.join('\n'));

  if (!CFG.AUTO_REMARCAR) return;
  sessoes.forEach(function (s) {
    const email = emailDoAluno(s.ev);
    if (!email) return;
    GmailApp.sendEmail(email, 'Our one-on-one needs a bit more notice', textoAvisoCurto(s, tz));
  });
}

function emailDoAluno(ev) {
  const outros = (ev.attendees || []).filter(function (a) { return !a.self && !a.resource; });
  return outros.length ? outros[0].email : null;
}

function primeiroNome(ev) {
  const outros = (ev.attendees || []).filter(function (a) { return !a.self && !a.resource; });
  if (!outros.length) return 'there';
  const nome = outros[0].displayName || outros[0].email || '';
  return nome.split(/[\s@.]/)[0] || 'there';
}

function textoRemarcacao(sessao, tz) {
  return [
    'Hi ' + primeiroNome(sessao.ev) + ',',
    '',
    'Something came up on my side and I can no longer keep our one-on-one on ' + formata(sessao.inicio, tz) + '. Sorry for the short notice.',
    '',
    'Please pick a new slot here: ' + CFG.LINK_AGENDAMENTO,
    '',
    'Every slot you see there is free on my end, so whatever you book is confirmed.',
    '',
    'Best,',
    CFG.NOME_MENTOR,
  ].join('\n');
}

function textoAvisoCurto(sessao, tz) {
  return [
    'Hi ' + primeiroNome(sessao.ev) + ',',
    '',
    'I saw you booked our one-on-one for ' + formata(sessao.inicio, tz) + '. I need at least ' +
      CFG.AVISO_MINIMO_HORAS + ' hours of notice so I can prepare and actually look at your work before we talk.',
    '',
    'Could you move it to a later slot? Here is the link: ' + CFG.LINK_AGENDAMENTO,
    '',
    'Best,',
    CFG.NOME_MENTOR,
  ].join('\n');
}

/* ========================= ACOMPANHAMENTO DOS ALUNOS ========================= */

/**
 * Panorama dos mentorados: quantas sessões cada um já teve, desde quando, e
 * quantas semanas faltam para fechar o programa de 10 semanas.
 * Roda à mão quando você quiser olhar. Não mexe em nada.
 */
function resumoMentorados() {
  const tz = fusoDoCalendario();
  const agora = new Date();
  const ini = new Date(agora.getTime() - 180 * 24 * 60 * 60 * 1000);
  const fim = new Date(agora.getTime() + CFG.HORIZONTE_DIAS * 24 * 60 * 60 * 1000);

  const porAluno = {};
  CFG.CALENDARIOS_FONTE.forEach(function (calId) {
    listarEventos(calId, ini, fim).forEach(function (ev) {
      if (!ehOneOnOne(ev) || ehBloqueio(ev)) return;
      const email = emailDoAluno(ev);
      if (!email) return;
      const inicio = quando(ev.start);
      if (!inicio) return;
      const r = porAluno[email] || (porAluno[email] = { nome: primeiroNome(ev), total: 0, primeira: inicio, ultima: inicio, futuras: 0 });
      r.total++;
      if (inicio < r.primeira) r.primeira = inicio;
      if (inicio > r.ultima) r.ultima = inicio;
      if (inicio > agora) r.futuras++;
    });
  });

  const linhas = [];
  Object.keys(porAluno).sort().forEach(function (email) {
    const r = porAluno[email];
    const semanas = Math.floor((agora - r.primeira) / (7 * 24 * 60 * 60 * 1000)) + 1;
    linhas.push([
      r.nome + ' <' + email + '>',
      r.total + ' sessão(ões)',
      'semana ' + Math.max(1, semanas) + ' de 10',
      'primeira ' + formata(r.primeira, tz),
      'última ' + formata(r.ultima, tz),
      r.futuras + ' marcada(s) à frente',
      semanas > 10 ? 'PROGRAMA VENCIDO' : '',
    ].filter(String).join(' | '));
  });

  const texto = linhas.length ? linhas.join('\n') : 'Nenhum one-on-one encontrado na janela.';
  Logger.log(texto);
  return texto;
}

/* =============================== ACIONADOR =============================== */

function instalarAcionador() {
  removerAcionador();
  ScriptApp.newTrigger('sincronizarAgenda').timeBased().everyMinutes(15).create();
  Logger.log('acionador criado: sincronizarAgenda a cada 15 minutos');
}

function removerAcionador() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'sincronizarAgenda') ScriptApp.deleteTrigger(t);
  });
}

/**
 * Lista todas as agendas desta conta e diz quais o agente está lendo hoje.
 * É por aqui que se descobre o id da agenda de trabalho (E-Line) para acrescentar
 * em CALENDARIOS_FONTE.
 */
function listarAgendas() {
  const linhas = ['AGENDAS DESTA CONTA', ''];
  todasAsAgendas().forEach(function (c) {
    linhas.push((ehFonte(c) ? '[LENDO]     ' : '[ignorada]  ') + (c.summary || '(sem nome)') +
      (c.primary ? '  (principal)' : ''));
    linhas.push('            id: ' + c.id);
    linhas.push('            acesso: ' + c.accessRole +
      (c.accessRole === 'freeBusyReader' ? '  <- só livre/ocupado, o agente não consegue ler os eventos' : ''));
    linhas.push('');
  });
  linhas.push('Para o agente passar a ler uma agenda ignorada, copie o id dela para');
  linhas.push('CALENDARIOS_FONTE, no topo do script.');
  Logger.log(linhas.join('\n'));
  return linhas.join('\n');
}

function todasAsAgendas() {
  const itens = [];
  let pageToken = null;
  do {
    const r = Calendar.CalendarList.list({ maxResults: 250, pageToken: pageToken });
    (r.items || []).forEach(function (c) { itens.push(c); });
    pageToken = r.nextPageToken;
  } while (pageToken);
  return itens;
}

function ehFonte(cal) {
  if (CFG.CALENDARIOS_FONTE.indexOf(cal.id) !== -1) return true;
  return !!cal.primary && CFG.CALENDARIOS_FONTE.indexOf('primary') !== -1;
}

/**
 * Diagnóstico: varre TODAS as agendas da conta, não só as configuradas, e diz para
 * cada compromisso das próximas 2 semanas se o agente o considera ocupado e por quê.
 * No fim, aponta as agendas que têm compromisso ocupado mas estão fora de
 * CALENDARIOS_FONTE. É o primeiro lugar para olhar quando algo passa batido.
 */
function diagnostico() {
  const tz = fusoDoCalendario();
  const agora = new Date();
  const fim = new Date(agora.getTime() + 14 * 24 * 60 * 60 * 1000);
  const linhas = ['COMPROMISSOS DAS PRÓXIMAS 2 SEMANAS', ''];
  const faltando = {};

  todasAsAgendas().forEach(function (cal) {
    const fonte = ehFonte(cal);
    let eventos = [];
    try {
      eventos = listarEventos(cal.id, agora, fim);
    } catch (e) {
      linhas.push('!! não consegui ler "' + (cal.summary || cal.id) + '": ' + e);
      return;
    }
    eventos.forEach(function (ev) {
      const eu = (ev.attendees || []).filter(function (a) { return a.self; })[0];
      let situacao;
      if (ehBloqueio(ev)) situacao = 'bloqueio do agente';
      else if (!ocupado(ev)) situacao = 'ignorado (evento)';
      else if (!fonte) { situacao = 'PERDIDO: agenda fora das fontes'; faltando[cal.id] = cal; }
      else situacao = 'bloqueia';
      linhas.push([
        formata(quando(ev.start), tz),
        (ev.summary || 'sem título').substring(0, 40),
        (cal.summary || cal.id).substring(0, 22),
        situacao,
        'rsvp=' + (eu ? eu.responseStatus : 'sem convite'),
        'transp=' + (ev.transparency || 'opaque'),
      ].join(' | '));
    });
  });

  const ids = Object.keys(faltando);
  if (ids.length) {
    linhas.push('');
    linhas.push('>> ' + ids.length + ' agenda(s) têm compromisso que deveria tirar disponibilidade');
    linhas.push('>> e o agente não está lendo. Troque CALENDARIOS_FONTE por:');
    linhas.push('');
    linhas.push('  CALENDARIOS_FONTE: [' + CFG.CALENDARIOS_FONTE.concat(ids).map(function (id) {
      return "'" + id + "'";
    }).join(', ') + '],');
  } else {
    linhas.push('');
    linhas.push('>> nenhuma agenda de fora com compromisso perdido.');
  }

  Logger.log(linhas.join('\n'));
  return linhas.join('\n');
}
