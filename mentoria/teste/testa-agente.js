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

const guards = [
  { id: 'g-orfao', summary: '🔒 Indisponível (agente)', status: 'confirmed',
    start: { dateTime: `${AMANHA}T20:00:00-03:00` }, end: { dateTime: `${AMANHA}T21:00:00-03:00` },
    extendedProperties: { private: { marca: 'mentoria-guard', chave: 'primary:sumiu', assinatura: 'x' } } },
  { id: 'g-desatualizado', summary: '🔒 Indisponível (agente)', status: 'confirmed',
    start: { dateTime: `${AMANHA}T10:00:00-03:00` }, end: { dateTime: `${AMANHA}T11:00:00-03:00` },
    extendedProperties: { private: { marca: 'mentoria-guard', chave: 'primary:sessao1', assinatura: 'antiga' } } },
];

const acoes = { insert: [], patch: [], remove: [] };
global.Calendar = {
  Calendars: { get: () => ({ timeZone: 'America/Sao_Paulo' }) },
  Events: {
    list: (calId, p) => {
      if (p.privateExtendedProperty) return { items: guards };
      if (p.iCalUID) return { items: [] };
      const ini = dia(p.timeMin), fim = dia(p.timeMax);
      return { items: fontes.filter(e => dia(e.start.dateTime) < fim && dia(e.end.dateTime) > ini) };
    },
    insert: (body, calId) => acoes.insert.push(body),
    patch: (body, calId, id) => acoes.patch.push({ id, body }),
    remove: (calId, id) => acoes.remove.push(id),
  },
};

vm.runInThisContext(fs.readFileSync(require('path').join(__dirname, '..', 'agente-agenda.gs'), 'utf8'));
CFG.SIMULAR = false;
CFG.VARRER_GMAIL = false;

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

console.log(falhas ? `\n${falhas} FALHA(S)` : '\ntudo passou');
process.exit(falhas ? 1 : 0);
