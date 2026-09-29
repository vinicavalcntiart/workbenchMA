// Stubs mínimos do Apps Script para exercitar a lógica pura do agente no node.
function wallToInstant(y, mo, d, h, mi, s, tz) {
  let guess = Date.UTC(y, mo - 1, d, h, mi, s);
  for (let i = 0; i < 3; i++) {
    const p = new Intl.DateTimeFormat('en-US', { timeZone: tz, year: 'numeric', month: '2-digit',
      day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false })
      .formatToParts(new Date(guess)).reduce((a, x) => (a[x.type] = x.value, a), {});
    const got = Date.UTC(+p.year, +p.month - 1, +p.day, p.hour === '24' ? 0 : +p.hour, +p.minute, +p.second);
    const diff = Date.UTC(y, mo - 1, d, h, mi, s) - got;
    if (diff === 0) break;
    guess += diff;
  }
  return new Date(guess);
}
global.Utilities = {
  parseDate(str, tz, fmt) {
    let m;
    if (fmt === "yyyyMMdd'T'HHmmss" && (m = str.match(/^(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})$/)))
      return wallToInstant(+m[1], +m[2], +m[3], +m[4], +m[5], +m[6], tz);
    if (fmt === 'yyyy-MM-dd HH:mm' && (m = str.match(/^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})$/)))
      return wallToInstant(+m[1], +m[2], +m[3], +m[4], +m[5], 0, tz);
    throw new Error('formato não coberto pelo stub: ' + fmt + ' / ' + str);
  },
  formatDate(date, tz, fmt) {
    const p = new Intl.DateTimeFormat('en-US', { timeZone: tz, year: 'numeric', month: '2-digit',
      day: '2-digit', hour: '2-digit', minute: '2-digit', weekday: 'short', hour12: false })
      .formatToParts(date).reduce((a, x) => (a[x.type] = x.value, a), {});
    if (fmt === 'yyyy-MM-dd') return `${p.year}-${p.month}-${p.day}`;
    if (fmt === 'EEE') return p.weekday;
    if (fmt === "dd/MM 'às' HH:mm") return `${p.day}/${p.month} às ${p.hour}:${p.minute}`;
    throw new Error('formato não coberto pelo stub: ' + fmt);
  },
};
global.Logger = { log: (...a) => global.LOG.push(a.join(' ')) };
global.LOG = [];
global.Session = { getScriptTimeZone: () => 'America/Sao_Paulo', getActiveUser: () => ({ getEmail: () => 'vini@example.com' }) };
global.PROPS = {};
global.resetProps = () => { global.PROPS = {}; };
global.PropertiesService = { getScriptProperties: () => ({
  getProperty: (k) => (k in global.PROPS ? global.PROPS[k] : null),
  setProperty: (k, v) => { global.PROPS[k] = String(v); },
}) };
global.ScriptApp = { getProjectTriggers: () => [], newTrigger: () => ({ timeBased: () => ({ everyMinutes: () => ({ create: () => {} }) }) }) };
global.GmailApp = { search: () => [], sendEmail: (...a) => global.EMAILS.push(a) };
global.EMAILS = [];
