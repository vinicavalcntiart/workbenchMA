require('./stubs.js');
const fs = require('fs'), vm = require('vm');

const dia = (iso) => new Date(iso);
const AMANHA = '2026-09-04';

// ---- agenda falsa ----
const fontes = [
  { id: 'eline1', summary: 'E-Line weekly sync', status: 'confirmed',
    start: { dateTime: `${AMANHA}T14:00:00-03:00` }, end: { dateTime: `${AMANHA}T15:00:00-03:00` },
    attendees: [{ self: true, responseStatus: 'needsAction' }, { email: 'pm@eline.com' }] },
  { id: 'recusada', summary: 'Reunião que recusei', status: 'confirmed',
    start: { dateTime: `${AMANHA}T09:00:00-03:00` }, end: { dateTime: `${AMANHA}T10:00:00-03:00` },
    attendees: [{ self: true, responseStatus: 'declined' }] },
  { id: 'livre', summary: 'Lembrete solto', status: 'confirmed', transparency: 'transparent',
    start: { dateTime: `${AMANHA}T11:00:00-03:00` }, end: { dateTime: `${AMANHA}T11:30:00-03:00` } },
  { id: 'aniv', summary: 'Aniversário da Ana', status: 'confirmed',
    start: { dateTime: `${AMANHA}T08:00:00-03:00` }, end: { dateTime: `${AMANHA}T08:30:00-03:00` } },
  { id: 'sessao1', summary: 'Vini Cavalcanti Mentorship', status: 'confirmed',
    start: { dateTime: `${AMANHA}T14:30:00-03:00` }, end: { dateTime: `${AMANHA}T15:30:00-03:00` },
    attendees: [{ self: true, responseStatus: 'accepted' }, { email: 'aluno@escola.com', displayName: 'Marina Reis' }] },
];

// A agenda de trabalho, que o agente NÃO está lendo: é o caso do Team playtest.
const elineEventos = [
  { id: 'playtest', summary: 'Team playtest!', status: 'confirmed',
    start: { dateTime: `${AMANHA}T13:30:00-03:00` }, end: { dateTime: `${AMANHA}T15:00:00-03:00` },
    attendees: [{ self: true, responseStatus: 'needsAction' }] },
];

const guards = [
  { id: 'g-orfao', summary: 'Busy', status: 'confirmed',
    start: { dateTime: `${AMANHA}T20:00:00-03:00` }, end: { dateTime: `${AMANHA}T21:00:00-03:00` },
    extendedProperties: { private: { marca: 'mentoria-guard', chave: 'primary:sumiu', assinatura: 'x' } } },
  { id: 'g-desatualizado', summary: 'Busy', status: 'confirmed',
    start: { dateTime: `${AMANHA}T10:00:00-03:00` }, end: { dateTime: `${AMANHA}T11:00:00-03:00` },
    extendedProperties: { private: { marca: 'mentoria-guard', chave: 'primary:sessao1', assinatura: 'antiga' } } },
];

const acoes = { insert: [], patch: [], remove: [] };
const agendas = [
  { id: 'vini@gmail.com', summary: 'Vini Cavalcanti', primary: true, accessRole: 'owner' },
  { id: 'c_eline@group.calendar.google.com', summary: 'E-Line', accessRole: 'reader' },
];
const porAgenda = { 'vini@gmail.com': fontes, 'c_eline@group.calendar.google.com': elineEventos };
global.Calendar = {
  CalendarList: { list: () => ({ items: agendas }) },
  Calendars: { get: () => ({ timeZone: 'America/Sao_Paulo' }) },
  Events: {
    list: (calId, p) => {
      if (p.privateExtendedProperty) return { items: guards };
      if (p.iCalUID) return { items: [] };
      const ini = dia(p.timeMin), fim = dia(p.timeMax);
      const lista = porAgenda[calId] || (calId === 'primary' ? fontes : []);
      return { items: lista.filter(e => dia(e.start.dateTime) < fim && dia(e.end.dateTime) > ini) };
    },
    insert: (body, calId) => acoes.insert.push(body),
    patch: (body, calId, id) => acoes.patch.push({ id, body }),
    remove: (calId, id) => acoes.remove.push(id),
  },
};

vm.runInThisContext(fs.readFileSync(require('path').join(__dirname, '..', 'agente-agenda.gs'), 'utf8'));
CFG.SIMULAR = false;
CFG.VARRER_GMAIL = false;
CFG.AGENDAS_SEMPRE_BLOQUEIAM = [];   // ligado só na seção própria, mais abaixo

const r = sincronizarAgenda();
let falhas = 0;
const ok = (cond, msg) => { console.log((cond ? '  ok   ' : '  FALHA') + ' ' + msg); if (!cond) falhas++; };

console.log('== diff de bloqueios ==');
const chaves = acoes.insert.map(b => b.extendedProperties.private.chave).sort();
ok(chaves.length === 1 && chaves[0] === 'primary:eline1', 'cria bloqueio só para a reunião sem resposta (' + chaves.join(', ') + ')');
const novo = acoes.insert[0];
ok(novo.start.dateTime === new Date(`${AMANHA}T13:45:00-03:00`).toISOString(), 'aplica buffer de 15 min antes');
ok(novo.end.dateTime === new Date(`${AMANHA}T15:15:00-03:00`).toISOString(), 'aplica buffer de 15 min depois');
ok(novo.transparency === 'opaque', 'bloqueio nasce marcado como Ocupado');
ok(!novo.attendees, 'bloqueio nasce sem convidados (não pode virar convite sem resposta)');
ok(/sem resposta/.test(novo.description), 'descrição registra o motivo');
ok(acoes.patch.length === 1 && acoes.patch[0].id === 'g-desatualizado', 'reajusta o bloqueio da sessão que mudou de horário');
ok(acoes.remove.length === 1 && acoes.remove[0] === 'g-orfao', 'remove só o bloqueio órfão');
ok(!chaves.includes('primary:recusada'), 'reunião recusada não tira disponibilidade');
ok(!chaves.includes('primary:livre'), 'evento marcado como Livre não tira disponibilidade');
ok(!chaves.includes('primary:aniv'), 'aniversário não tira disponibilidade');
ok(r.colisoes === 1, 'detecta o one-on-one em cima da reunião da E-Line');

console.log('== aviso de colisão ==');
const urgente = EMAILS.find(e => /URGENTE/.test(e[1]));
ok(!!urgente, 'manda o alerta de conflito para o Vini');
ok(/aluno@escola.com/.test(urgente[2]), 'o alerta identifica o aluno');
ok(!EMAILS.some(e => e[0] === 'aluno@escola.com'), 'com AUTO_REMARCAR desligado, nada vai para o aluno');

console.log('== AUTO_REMARCAR ligado ==');
EMAILS.length = 0;
resetProps();               // conflito novo: sem isso o dedupe segura o aviso
CFG.AUTO_REMARCAR = true;
sincronizarAgenda();
const aoAluno = EMAILS.find(e => e[0] === 'aluno@escola.com');
ok(!!aoAluno, 'escreve para o aluno');
ok(/Marina/.test(aoAluno[2]) && /calendar\.app\.google/.test(aoAluno[2]), 'email em inglês, com nome e link de reserva');
ok(!/—/.test(aoAluno[2]), 'sem travessão no texto do aluno');

console.log('== leitor de .ics ==');
const ics = [
  'BEGIN:VCALENDAR', 'METHOD:REQUEST', 'BEGIN:VEVENT', 'UID:abc-123@eline.com',
  'SUMMARY:Endstar character re', ' view', 'DTSTART;TZID=America/Phoenix:20260904T090000',
  'DTEND;TZID=America/Phoenix:20260904T100000', 'STATUS:CONFIRMED', 'END:VEVENT', 'END:VCALENDAR',
].join('\r\n');
const evs = lerIcs(ics);
ok(evs.length === 1 && evs[0].uid === 'abc-123@eline.com', 'lê o UID');
ok(evs[0].summary === 'Endstar character review', 'remonta linha dobrada');
ok(evs[0].metodo === 'REQUEST', 'lê o METHOD');
ok(evs[0].inicio.toISOString() === '2026-09-04T16:00:00.000Z', 'converte TZID America/Phoenix para UTC');
const cancel = lerIcs(['BEGIN:VCALENDAR','METHOD:CANCEL','BEGIN:VEVENT','UID:x','DTSTART:20260904T120000Z','END:VEVENT','END:VCALENDAR'].join('\r\n'));
ok(cancel[0].metodo === 'CANCEL' && cancel[0].inicio.toISOString() === '2026-09-04T12:00:00.000Z', 'lê cancelamento e horário em UTC');
ok(lerIcs(['BEGIN:VEVENT','UID:y','DTSTART;VALUE=DATE:20260904','END:VEVENT'].join('\r\n'))[0].inicio === null, 'ignora evento de dia inteiro');

console.log('== janela protegida ==');
CFG.JANELAS_PROTEGIDAS = [{ dias: [5], de: '12:00', ate: '13:30', motivo: 'almoço' }];
const janelas = janelasProtegidas(new Date(`${AMANHA}T00:00:00-03:00`), new Date('2026-09-12T00:00:00-03:00'), 'America/Sao_Paulo');
ok(janelas.length === 2 && janelas[0].chave === 'janela:2026-09-04:12:00-13:30' && janelas[1].chave === 'janela:2026-09-11:12:00-13:30', 'gera a janela nas duas sextas da faixa (' + janelas.map(j => j.chave).join(', ') + ')');

console.log('== não repete aviso do mesmo conflito ==');
resetProps();
CFG.AUTO_REMARCAR = false;
EMAILS.length = 0;
sincronizarAgenda();
const depoisDaPrimeira = EMAILS.length;
sincronizarAgenda();
ok(depoisDaPrimeira >= 1 && EMAILS.length === depoisDaPrimeira, 'segunda rodada com o mesmo conflito não manda email de novo');

console.log('== antecedência mínima ==');
resetProps();
EMAILS.length = 0;
const emCima = { id: 'sessao-tarde', summary: 'Vini Cavalcanti Mentorship', status: 'confirmed',
  created: `${AMANHA}T08:00:00-03:00`,
  start: { dateTime: `${AMANHA}T18:00:00-03:00` }, end: { dateTime: `${AMANHA}T19:00:00-03:00` },
  attendees: [{ self: true, responseStatus: 'accepted' }, { email: 'atrasado@escola.com', displayName: 'Caio Lima' }] };
const comAntecedencia = { id: 'sessao-ok', summary: 'Vini Cavalcanti Mentorship', status: 'confirmed',
  created: '2026-08-20T10:00:00-03:00',
  start: { dateTime: `${AMANHA}T20:00:00-03:00` }, end: { dateTime: `${AMANHA}T21:00:00-03:00` },
  attendees: [{ self: true, responseStatus: 'accepted' }, { email: 'certinho@escola.com' }] };
fontes.push(emCima, comAntecedencia);
const r2 = sincronizarAgenda();
ok(r2.emCimaDaHora === 1, 'flagra só a sessão marcada 10h antes (' + r2.emCimaDaHora + ')');
const alerta = EMAILS.find(e => /em cima da hora/.test(e[1]));
ok(!!alerta && /atrasado@escola.com/.test(alerta[2]), 'o alerta nomeia quem marcou em cima da hora');
ok(!/certinho@escola.com/.test(alerta[2]), 'sessão marcada com semanas de antecedência não entra');
ok(!EMAILS.some(e => e[0] === 'atrasado@escola.com'), 'com AUTO_REMARCAR desligado, o aluno não recebe nada');

resetProps();
EMAILS.length = 0;
CFG.AUTO_REMARCAR = true;
sincronizarAgenda();
const pedido = EMAILS.find(e => e[0] === 'atrasado@escola.com');
ok(!!pedido && /Caio/.test(pedido[2]) && /24 hours of notice/.test(pedido[2]), 'pede remarcação ao aluno, em inglês, citando as 24h');
CFG.AUTO_REMARCAR = false;

console.log('== bloqueio rolante ==');
resetProps();
acoes.insert.length = 0;
ok(!acoes.insert.some(b => b.extendedProperties.private.chave === 'aviso-minimo'), 'vem desligado por padrão');
CFG.BLOQUEIO_ROLANTE = true;
guards.length = 0;
sincronizarAgenda();
const rolante = acoes.insert.find(b => b.extendedProperties.private.chave === 'aviso-minimo');
ok(!!rolante, 'ligado, cria o bloqueio contínuo');
const dur = (dia(rolante.end.dateTime) - dia(rolante.start.dateTime)) / 3600000;
ok(dur >= 24 && dur <= 24.5, 'cobre pelo menos as 24h pedidas, nunca menos (' + dur.toFixed(2) + 'h)');
ok(dia(rolante.start.dateTime) <= new Date(), 'começa agora, não deixa brecha antes');
CFG.BLOQUEIO_ROLANTE = false;

console.log('== diagnóstico acha a agenda que falta ==');
const diag = diagnostico();
ok(/Team playtest/.test(diag), 'enxerga evento de agenda que não é fonte');
ok(/PERDIDO: agenda fora das fontes/.test(diag), 'marca o evento como perdido');
ok(/c_eline@group\.calendar\.google\.com/.test(diag), 'nomeia o id da agenda que falta');
ok(/CALENDARIOS_FONTE: \['primary', 'c_eline@group\.calendar\.google\.com'\]/.test(diag), 'entrega a linha de config pronta para colar');
ok(/Rafa|E-Line weekly sync/.test(diag), 'continua listando os eventos da agenda principal');

const agendasLog = listarAgendas();
ok(/\[LENDO\].*Vini Cavalcanti/.test(agendasLog), 'marca a agenda principal como lida');
ok(/\[ignorada\].*E-Line/.test(agendasLog), 'marca a agenda da E-Line como ignorada');

CFG.CALENDARIOS_FONTE = ['primary', 'c_eline@group.calendar.google.com'];
resetProps(); acoes.insert.length = 0; guards.length = 0;
sincronizarAgenda();
ok(acoes.insert.some(b => /Team playtest/.test(b.description)), 'com a agenda acrescentada, o playtest vira bloqueio');
ok(/nenhuma agenda de fora com compromisso perdido/.test(diagnostico()), 'e o diagnóstico para de reclamar');
CFG.CALENDARIOS_FONTE = ['primary'];

console.log('== agenda de trabalho bloqueia tudo ==');
elineEventos.push(
  { id: 'livre-trabalho', summary: 'Focus block', status: 'confirmed', transparency: 'transparent',
    start: { dateTime: `${AMANHA}T16:00:00-03:00` }, end: { dateTime: `${AMANHA}T17:00:00-03:00` } },
  { id: 'recusada-trabalho', summary: 'Standup opcional', status: 'confirmed',
    start: { dateTime: `${AMANHA}T09:30:00-03:00` }, end: { dateTime: `${AMANHA}T10:00:00-03:00` },
    attendees: [{ self: true, responseStatus: 'declined' }] },
  { id: 'feriado-trabalho', summary: 'Company holiday', status: 'confirmed',
    start: { date: AMANHA }, end: { date: '2026-09-05' } },
);
CFG.CALENDARIOS_FONTE = ['primary'];                       // de propósito: sem a E-Line aqui
CFG.AGENDAS_SEMPRE_BLOQUEIAM = ['c_eline@group.calendar.google.com'];
resetProps(); acoes.insert.length = 0; guards.length = 0;
sincronizarAgenda();
const doTrabalho = acoes.insert.map(b => b.extendedProperties.private.chave);
const temTrabalho = (id) => doTrabalho.includes('c_eline@group.calendar.google.com:' + id);
ok(temTrabalho('playtest'), 'lê a agenda de trabalho sem precisar repetir o id em CALENDARIOS_FONTE');
ok(temTrabalho('livre-trabalho'), 'evento marcado como Livre na agenda de trabalho bloqueia');
ok(temTrabalho('recusada-trabalho'), 'evento recusado na agenda de trabalho bloqueia');
ok(!temTrabalho('feriado-trabalho'), 'dia inteiro continua de fora, mesmo na agenda de trabalho');
ok(/bloqueia \(agenda de trabalho\)/.test(diagnostico()), 'o diagnóstico diz de onde veio a regra');

// e a regra não vaza para a agenda pessoal
ok(!acoes.insert.some(b => b.extendedProperties.private.chave === 'primary:recusada'),
   'reunião recusada na agenda pessoal continua sem bloquear');
ok(!acoes.insert.some(b => b.extendedProperties.private.chave === 'primary:livre'),
   'evento Livre na agenda pessoal continua sem bloquear');

console.log(falhas ? `\n${falhas} FALHA(S)` : '\ntudo passou');
process.exit(falhas ? 1 : 0);
