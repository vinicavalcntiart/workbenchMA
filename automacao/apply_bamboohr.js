// BambooHR careers filler. Uso: node apply_bamboohr.js <url> <slug> <ans.json> [--submit]
// A campanha ja tem nove quadros de BambooHR (Image Engine, Cinesite, nWave, Amuse, Ember Lab,
// Stirling, Streamline, Random Studio, BetaDwarf) e nao tinha preenchedor para nenhum.
const {chromium} = require('playwright');
const fs = require('fs');
const [url, slug, ansFile, flag] = process.argv.slice(2);
const SUBMIT = flag === '--submit';
const A = JSON.parse(fs.readFileSync(ansFile));
const D = __dirname;
const log = (...a) => console.log('[' + slug + ']', ...a);

(async () => {
  const b = await chromium.launch({proxy: {server: 'http://127.0.0.1:18080'}, args: ['--no-sandbox', '--ignore-certificate-errors']});
  const p = await (await b.newContext({ignoreHTTPSErrors: true, viewport: {width: 1280, height: 2600}, userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36', locale: 'en-US'})).newPage();
  try {
    await p.goto(url, {timeout: 120000, waitUntil: 'domcontentloaded'});
    await p.waitForTimeout(4000);
    for (const t of ['Accept all', 'Accept All', 'Accept', 'Got it', 'I agree']) {
      const e = await p.$(`button:has-text("${t}")`); if (e) { await e.click().catch(() => {}); await p.waitForTimeout(1200); break; }
    }
    // O BambooHR monta a pagina em SHADOW DOM: p.$('button:has-text(...)') NAO acha o botao.
    // O que funciona e o getByText do Playwright, medido em 06/09 na BetaDwarf.
    let clicou = false;
    for (let tent = 0; tent < 6 && !clicou; tent++) {
      for (const t of ['Apply for This Job', 'Apply for this job', 'Apply Now']) {
        const loc = p.getByText(t, {exact: false});
        if (await loc.count().catch(() => 0)) {
          await loc.first().click({timeout: 15000}).catch(e => log('click err', e.message.split('\n')[0]));
          log('cliquei em', t, '(tentativa', tent + 1, ')');
          clicou = true;
          await p.waitForTimeout(6000);
          break;
        }
      }
      if (!clicou) await p.waitForTimeout(4000);
    }
    if (!clicou) log('NAO ACHEI o botao Apply nem depois de 6 tentativas');
    await p.locator('input[name=firstName]').first().waitFor({timeout: 60000});

    for (const [name, val] of Object.entries(A.fields || {})) {
      const loc = p.locator(`[name="${name}"]`).first();
      if (!await loc.count().catch(() => 0)) { log('CAMPO AUSENTE', name); continue; }
      const el = await loc.elementHandle();
      const tag = await el.evaluate(e => e.tagName);
      if (tag === 'SELECT') {
        const opts = await el.evaluate(e => [...e.options].map(o => o.text));
        const alvo = opts.find(o => new RegExp(val, 'i').test(o));
        if (alvo) { await el.selectOption({label: alvo}); log('select', name, '=>', alvo); }
        else log('SELECT SEM OPCAO', name, '=>', val);
        continue;
      }
      await el.fill(String(val)).catch(async () => { await el.type(String(val), {delay: 30}).catch(() => {}); });
      log('preenchido', name);
    }

    // curriculo: o input que aceita pdf, nunca o de foto
    const fis = await p.locator('input[type=file]').elementHandles();
    let posto = false;
    for (const fi of fis) {
      const acc = ((await fi.getAttribute('accept')) || '').toLowerCase();
      const nm = ((await fi.getAttribute('name')) || '').toLowerCase();
      if (/image|photo/.test(acc + nm)) continue;
      await fi.setInputFiles(D + '/Vini_Cavalcanti_CV.pdf');
      log('CV anexado em', nm || acc || '(sem nome)');
      posto = true;
      await p.waitForTimeout(6000);
      break;
    }
    if (!posto) log('ATENCAO: nao achei input de arquivo para o curriculo');

    for (const cb of await p.locator('input[type=checkbox]').elementHandles()) {
      const req = await cb.evaluate(e => e.required || /privacy|consent|agree|policy/i.test((e.closest('label') || e.parentElement || {}).innerText || ''));
      if (req) { const on = await cb.isChecked().catch(() => false); if (!on) await cb.check({force: true}).catch(() => {}); }
    }

    await p.waitForTimeout(1500);
    await p.screenshot({path: `filled_${slug}.png`, fullPage: true});
    const rb = await p.evaluate(names => names.map(n => {
      const e = document.querySelector(`[name="${n}"]`) || document.getElementById(n);
      return [n, e ? (e.value || '(VAZIO)') : '(AUSENTE)'];
    }), Object.keys(A.fields || {}));
    for (const [n, v] of rb) log('  leitura de volta', n, '=>', String(v).slice(0, 60));

    if (!SUBMIT) { log('DRY RUN'); await b.close(); return; }
    const sbLoc = p.getByText('Submit Application', {exact: false});
    const sb = (await sbLoc.count().catch(() => 0)) ? await sbLoc.first().elementHandle() : await p.locator('button[type=submit]').first().elementHandle().catch(() => null);
    if (!sb) { log('SEM BOTAO DE ENVIO'); await b.close(); return; }
    const on = await sb.isEnabled().catch(() => false);
    if (!on) { log('BOTAO DESABILITADO, falta campo obrigatorio'); await p.screenshot({path: `err_${slug}.png`, fullPage: true}); await b.close(); return; }
    await sb.click();
    await p.waitForTimeout(12000);
    await p.screenshot({path: `result_${slug}.png`, fullPage: true});
    const txt = (await p.evaluate(() => document.body.innerText)).replace(/\s+/g, ' ').slice(0, 400);
    const ok = /thank you|thanks|received|successfully|submitted/i.test(txt);
    log(ok ? 'SUBMITTED OK' : 'RESULTADO DUVIDOSO', '| url:', p.url(), '| texto:', txt);
  } catch (e) {
    log('ERR', e.message.split('\n')[0]);
    await p.screenshot({path: `err_${slug}.png`, fullPage: true}).catch(() => {});
  }
  await b.close();
})();
