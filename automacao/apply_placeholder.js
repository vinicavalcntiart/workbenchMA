// Formulario proprio SEM atributo `name` nos campos, que e o padrao de site montado em
// Webflow/Wix/tema fechado. O casamento e feito pelo PLACEHOLDER (ou pelo rotulo, quando existe),
// porque e a unica coisa estavel nesses formularios.
//
// Uso: VINI_TEL='<formato internacional>' sh hb_run.sh apply_placeholder.js <url> <slug> <respostas.json> [--submit]
//
// O arquivo de respostas tem tres blocos: `texto` (regex do placeholder -> valor),
// `arquivos` (regex do rotulo ou do accept -> nome do arquivo em $SCRATCH/apply) e
// `enviar` (texto do botao). Valor especial "$TEL" vira a variavel de ambiente VINI_TEL,
// que nunca fica escrita em arquivo: o repositorio e publico.
const {chromium} = require('playwright');
const fs = require('fs');
const [url, slug, ansFile, flag] = process.argv.slice(2);
const SUBMIT = flag === '--submit';
const D = __dirname;
const A = JSON.parse(fs.readFileSync(ansFile, 'utf8'));
const log = (...a) => console.log('[' + slug + ']', ...a);
const val = v => String(v) === '$TEL' ? (process.env.VINI_TEL || '') : String(v);

(async () => {
  const b = await chromium.launch({headless: false, proxy: {server: 'http://127.0.0.1:18080'}, args: ['--no-sandbox', '--ignore-certificate-errors']});
  const p = await (await b.newContext({ignoreHTTPSErrors: true, viewport: {width: 1280, height: 2400}, acceptDownloads: true,
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36', locale: 'en-US'})).newPage();
  try {
    await p.goto(url, {timeout: 120000, waitUntil: 'domcontentloaded'});
    await p.waitForTimeout(4000);
    for (const t of ['Accept all', 'Accept All', 'Accept', 'Allow all', 'I agree', 'Got it', 'OK']) {
      const e = await p.$(`button:has-text("${t}"), a:has-text("${t}")`);
      if (e && await e.isVisible().catch(() => false)) { await e.click().catch(() => {}); await p.waitForTimeout(1200); break; }
    }
    for (const t of (A.abrir || [])) { const e = await p.$(t); if (e) { await e.click().catch(() => {}); await p.waitForTimeout(2500); } }
    for (let i = 0; i < 8; i++) { await p.mouse.wheel(0, 1600); await p.waitForTimeout(400); }

    const faltando = [];
    for (const [rx, v] of Object.entries(A.texto || {})) {
      const el = (await p.$$('input, textarea')).find(async () => true);
      const alvos = await p.$$('input, textarea');
      let achou = null;
      for (const e of alvos) {
        const ph = (await e.getAttribute('placeholder')) || (await e.getAttribute('aria-label')) || '';
        if (ph && new RegExp(rx, 'i').test(ph)) { achou = e; break; }
      }
      if (!achou) { log('CAMPO NAO ACHADO pelo placeholder', rx); faltando.push(rx); continue; }
      await achou.fill(val(v)).catch(e => { log('falha no fill', rx, e.message.split('\n')[0]); faltando.push(rx); });
      log('preenchido', rx, '=>', val(v).slice(0, 60));
      void el;
    }
    for (const [rx, arq] of Object.entries(A.arquivos || {})) {
      const files = await p.$$('input[type="file"]');
      let achou = null;
      for (const e of files) {
        const ctx2 = await e.evaluate(x => (x.closest('label') || x.parentElement || {}).innerText || '');
        if (!rx || new RegExp(rx, 'i').test(ctx2) || files.length === 1) { achou = e; break; }
      }
      if (!achou) { log('CAMPO DE ARQUIVO NAO ACHADO', rx); faltando.push(rx); continue; }
      await achou.setInputFiles(D + '/' + arq).catch(e => log('falha no anexo', e.message.slice(0, 60)));
      await p.waitForTimeout(2500);
      log('anexado', rx, '=>', arq);
    }
    await p.waitForTimeout(1200);
    await p.screenshot({path: `filled_${slug}.png`, fullPage: true});
    const rb = await p.evaluate(() => [...document.querySelectorAll('input, textarea')]
      .filter(e => e.type !== 'hidden')
      .map(e => [(e.getAttribute('placeholder') || e.getAttribute('aria-label') || e.type), e.type === 'file' ? (e.files && e.files.length ? e.files[0].name : '(VAZIO)') : (e.value || '(VAZIO)')]));
    for (const [n, v] of rb) log('  leitura de volta', String(n).slice(0, 40), '=>', String(v).slice(0, 70));
    if (faltando.length) log('PENDENCIAS:', JSON.stringify(faltando));
    if (!SUBMIT) { log('DRY RUN'); await b.close(); return; }
    if (faltando.length) { log('NAO VOU ENVIAR com pendencia'); await b.close(); return; }

    const antes = (await p.evaluate(() => document.body.innerText)).replace(/\s+/g, ' ');
    const bt = A.enviar || 'Submit';
    const sb = await p.$(`button:has-text("${bt}"):visible, input[type="submit"][value*="${bt}" i]:visible, a:has-text("${bt}"):visible`);
    if (!sb) { log('SEM BOTAO DE ENVIO VISIVEL para', bt); await b.close(); return; }
    await sb.click();
    await p.waitForTimeout(12000);
    await p.screenshot({path: `result_${slug}.png`, fullPage: true});
    const dep = (await p.evaluate(() => document.body.innerText)).replace(/\s+/g, ' ');
    // A prova e estreita de proposito: em 08/09 uma regex larga casou com o texto de ABERTURA
    // de um formulario ("Thank you for considering a career at...") e deu envio por confirmado.
    const ok = /(application|message|submission).{0,40}(received|sent|submitted)|thank you for (applying|your application|your submission)|we (have )?(received|got) your/i.test(dep)
      && dep !== antes;
    log(ok ? 'SUBMITTED OK' : 'RESULTADO DUVIDOSO', '| url:', p.url(), '| texto:', dep.slice(0, 400));
  } catch (e) {
    log('ERR', e.message.split('\n')[0]);
    await p.screenshot({path: `err_${slug}.png`, fullPage: true}).catch(() => {});
  }
  await b.close();
})();
