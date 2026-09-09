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
  // Sem log de rede, "RESULTADO DUVIDOSO" nao distingue tres coisas muito diferentes: campo
  // obrigatorio vazio, POST recusado por captcha, e envio que deu certo mas nao mudou a tela.
  p.on('response', async r => {
    try {
      if (r.request().method() === 'GET') return;
      const u = r.url();
      if (!/bamboohr|recaptcha|google\.com\/recaptcha/.test(u)) return;
      let corpo = '';
      try { corpo = (await r.text()).replace(/\s+/g, ' ').slice(0, 200); } catch (_) {}
      log('[rede]', r.status(), r.request().method(), u.slice(0, 110), '|', corpo);
    } catch (_) {}
  });
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

    // SELECT DO BAMBOOHR NOVO (Fabric/MUI), medido em 09/09 na Offworld: o <select> nativo e
    // um esqueleto com aria-hidden, opacity 0, largura 0 e UMA option vazia. selectOption()
    // nao levanta erro, so nao escolhe nada, e o campo obrigatorio fica vazio na hora do envio
    // sem nenhuma mensagem util. Quem escolhe de verdade e o button.fab-SelectToggle, que traz
    // o rotulo no aria-label ("Country Canada"). As opcoes aparecem TRIPLICADAS por causa dos
    // divs aninhados, entao casa-se pelo texto exato e pega-se a primeira.
    for (const f of (A.fabric || [])) {
      // O aria-label do toggle NAO e estavel: depois de trocar o pais, o de provincia deixou
      // de comecar por "Province". Entao procura-se por regex em TODOS os fab-SelectToggle, e
      // lista-se o que existe quando nao acha, para o log dizer o motivo em vez do sintoma.
      const todos = p.locator('button.fab-SelectToggle');
      const n = await todos.count().catch(() => 0);
      let bt = null;
      for (let i = 0; i < n; i++) {
        const al = await todos.nth(i).getAttribute('aria-label').catch(() => '') || '';
        if (new RegExp(f.aria, 'i').test(al)) { bt = todos.nth(i); break; }
      }
      if (!bt) {
        const rotulos = [];
        for (let i = 0; i < n; i++) rotulos.push(await todos.nth(i).getAttribute('aria-label').catch(() => ''));
        log('FABRIC sem botao para', f.aria, '| toggles na tela:', JSON.stringify(rotulos));
        continue;
      }
      await bt.click({force: true}).catch(() => {});
      await p.waitForTimeout(2000);
      const esc = f.escolha.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const op = p.locator('[role=option],[role=listbox] li,li[class*=option i],div[class*=option i]')
                  .filter({hasText: new RegExp('^' + esc + '$')}).first();
      if (await op.count().catch(() => 0)) { await op.click({force: true}).catch(() => {}); log('fabric', f.aria, '=>', f.escolha); }
      else log('FABRIC SEM OPCAO', f.aria, '=>', f.escolha);
      await p.waitForTimeout(2500);
      const agora = await bt.getAttribute('aria-label').catch(() => '');
      log('  aria-label depois:', agora);
    }

    // ORDEM IMPORTA, medido em 09/09 na Offworld: o PAIS tem que ser escolhido ANTES dos
    // campos de texto. Com pais Canada, 'state.value' e um <select> de provincias; ao trocar
    // para Brazil o BambooHR TROCA o elemento por um <input> de texto livre. Preenchendo na
    // ordem antiga, o valor ia para um select que depois deixava de existir, e a provincia
    // ficava vazia sem nenhum aviso ate o Submit.
    for (const [name, val] of Object.entries(A.fields || {})) {
      // HONEYPOT: o BambooHR planta um campo "Please leave this field blank" com nome
      // aleatorio (nickname_hpcsaf na Offworld). Ele NUNCA se preenche.
      if (/honeypot|nickname_hp|^hp_|beecatcher/i.test(name)) { log('honeypot, deixando vazio', name); continue; }
      // Nem todo campo obrigatorio tem name: o "Date Available" da Offworld so tem id gerado
      // (FabricTextField-318). Chave comecando com # e tratada como seletor CSS direto.
      const loc = name.startsWith('#') || name.startsWith('[')
        ? p.locator(name).first()
        : p.locator(`[name="${name}"]`).first();
      if (!await loc.count().catch(() => 0)) { log('CAMPO AUSENTE', name); continue; }
      const el = await loc.elementHandle();
      const tag = await el.evaluate(e => e.tagName);
      if (tag === 'SELECT') {
        const opts = await el.evaluate(e => [...e.options].map(o => o.text));
        const alvo = opts.find(o => new RegExp(val, 'i').test(o));
        if (alvo) { await el.selectOption({label: alvo}); log('select', name, '=>', alvo); }
        else log('SELECT SEM OPCAO', name, '=>', val, '| tinha:', JSON.stringify(opts.slice(0, 12)));
        // O pais REPOVOA a lista de provincia. Sem esta espera, o select seguinte e lido
        // com as opcoes do pais antigo e a escolha falha em silencio.
        await p.waitForTimeout(2500);
        continue;
      }
      await el.fill(String(val)).catch(async () => { await el.type(String(val), {delay: 30}).catch(() => {}); });
      log('preenchido', name);
    }

    // POR ROTULO, e nao por id: os ids do Fabric (FabricTextField-318) sao GERADOS a cada
    // render, entao seletor por id funciona numa rodada e some na seguinte. O rotulo sobrevive.
    for (const r of (A.porRotulo || [])) {
      // Primeiro tenta o caminho honesto: localizar pelo rotulo e DIGITAR. A injecao por JS
      // abaixo e so a rede de seguranca, e ela nao sobrevive ao estado controlado do React.
      const porLabel = p.getByLabel(new RegExp(r.rotulo, 'i')).first();
      if (await porLabel.count().catch(() => 0)) {
        await porLabel.fill(String(r.valor)).catch(async () => { await porLabel.type(String(r.valor), {delay: 40}).catch(() => {}); });
        await p.waitForTimeout(800);
        const v = await porLabel.inputValue().catch(() => '');
        if (v) { log('por rotulo (digitado):', r.rotulo, '=>', v.slice(0, 40)); continue; }
      }
      const achou = await p.evaluate(({rot, val}) => {
        const alvos = [...document.querySelectorAll('input,textarea')];
        for (const e of alvos) {
          let lab = '';
          if (e.id) { const l = document.querySelector('label[for="' + CSS.escape(e.id) + '"]'); if (l) lab = l.innerText; }
          if (!lab) { const l = e.closest('label'); if (l) lab = l.innerText; }
          if (!lab) { const w = e.closest('div'); if (w) lab = (w.innerText || '').slice(0, 80); }
          if (new RegExp(rot, 'i').test(lab || '')) {
            const set = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            set.call(e, val);
            e.dispatchEvent(new Event('input', {bubbles: true}));
            e.dispatchEvent(new Event('change', {bubbles: true}));
            return lab.replace(/\s+/g, ' ').slice(0, 50);
          }
        }
        return null;
      }, {rot: r.rotulo, val: r.valor});
      log(achou ? 'por rotulo: ' + achou + ' => ' + String(r.valor).slice(0, 40) : 'ROTULO NAO ACHADO: ' + r.rotulo);
      await p.waitForTimeout(600);
    }

    // Antes de enviar, listar o que AINDA esta obrigatorio e vazio. Foi a falta disso que fez
    // o primeiro envio na Offworld voltar com quatro "Please fill in this field" na tela.
    const faltando = await p.evaluate(() => [...document.querySelectorAll('input,select,textarea')]
      .filter(e => e.type !== 'hidden' && !e.value)
      .map(e => {
        let lab = '';
        if (e.id) { const l = document.querySelector('label[for="' + CSS.escape(e.id) + '"]'); if (l) lab = l.innerText; }
        if (!lab) { const w = e.closest('div'); if (w) lab = (w.innerText || '').slice(0, 60); }
        return (lab || e.name || '').replace(/\s+/g, ' ').trim().slice(0, 50);
      })
      .filter(x => /\*/.test(x)));
    if (faltando.length) log('AINDA OBRIGATORIOS E VAZIOS:', JSON.stringify(faltando));

    // curriculo: o input que aceita pdf, nunca o de foto
    // MEDIDO EM 09/09 NA OFFWORLD: o formulario tem DOIS inputs de arquivo, e o PRIMEIRO e o
    // da Cover Letter (opcional). O script antigo anexava no primeiro que nao fosse foto e
    // parava, entao o CV ia para a carta e o Resume, que e o obrigatorio, ficava vazio; a tela
    // so dizia "Please upload a file" depois do Submit. Agora o alvo e o input MARCADO como
    // required, ou o que estiver perto do campo escondido resumeFileId, e a carta so recebe
    // arquivo se houver um segundo input livre.
    const fis = await p.locator('input[type=file]').elementHandles();
    let posto = false;
    const ehFoto = async fi => /image|photo/.test((((await fi.getAttribute('accept')) || '') + ((await fi.getAttribute('name')) || '')).toLowerCase());
    for (const fi of fis) {
      if (await ehFoto(fi)) continue;
      const obrig = await fi.evaluate(e => {
        if (e.required) return true;
        const w = e.closest('div');
        return !!(w && (w.querySelector('input[name=resumeFileId]') || /resume|cv\b/i.test(w.innerText || '')));
      }).catch(() => false);
      if (!obrig) continue;
      await fi.setInputFiles(D + '/Vini_Cavalcanti_CV.pdf');
      log('CV anexado no input do RESUME');
      posto = true;
      await p.waitForTimeout(7000);
      break;
    }
    if (!posto) {
      for (const fi of fis) { if (await ehFoto(fi)) continue; await fi.setInputFiles(D + '/Vini_Cavalcanti_CV.pdf'); log('CV anexado no primeiro input livre (nao achei o marcado como resume)'); posto = true; await p.waitForTimeout(7000); break; }
    }
    if (!posto) log('ATENCAO: nao achei input de arquivo para o curriculo');

    for (const cb of await p.locator('input[type=checkbox]').elementHandles()) {
      const req = await cb.evaluate(e => e.required || /privacy|consent|agree|policy/i.test((e.closest('label') || e.parentElement || {}).innerText || ''));
      if (req) { const on = await cb.isChecked().catch(() => false); if (!on) await cb.check({force: true}).catch(() => {}); }
    }

    await p.waitForTimeout(1500);
    await p.screenshot({path: `filled_${slug}.png`, fullPage: true});
    const rb = await p.evaluate(names => names.map(n => {
      const e = n.startsWith('#') || n.startsWith('[') ? document.querySelector(n)
                : (document.querySelector(`[name="${n}"]`) || document.getElementById(n));
      return [n, e ? (e.value || '(VAZIO)') : '(AUSENTE)'];
    }), Object.keys(A.fields || {}));
    for (const [n, v] of rb) log('  leitura de volta', n, '=>', String(v).slice(0, 60));

    if (!SUBMIT) { log('DRY RUN'); await b.close(); return; }
    // O alvo tem que ser o BOTAO, nao o texto dentro dele: getByText devolve o span, e clicar
    // no span de um botao cujo handler esta no <button> nao dispara nada em alguns temas.
    let sbLoc = p.locator('button').filter({hasText: /submit application/i}).first();
    if (!await sbLoc.count().catch(() => 0)) sbLoc = p.locator('button[type=submit]').first();
    if (!await sbLoc.count().catch(() => 0)) sbLoc = p.getByText('Submit Application', {exact: false});
    const sb = await sbLoc.elementHandle().catch(() => null);
    if (sb) log('botao de envio:', await sb.evaluate(e => e.tagName + ' | ' + (e.className || '').toString().slice(0, 50) + ' | disabled=' + !!e.disabled).catch(() => '?'));
    if (!sb) { log('SEM BOTAO DE ENVIO'); await b.close(); return; }
    const on = await sb.isEnabled().catch(() => false);
    if (!on) { log('BOTAO DESABILITADO, falta campo obrigatorio'); await p.screenshot({path: `err_${slug}.png`, fullPage: true}); await b.close(); return; }
    // MESMA LICAO DO GOHIRE, e ela se repetiu aqui: click() num alvo fora da area visivel nao
    // dispara nada e NAO levanta erro. Na primeira tentativa o unico POST que saiu foi o do
    // upload do CV, ou seja o Submit nunca aconteceu, e a tela ficou identica. Rolar ate o
    // botao e clicar por coordenada e o que transforma "duvidoso" em veredito.
    await sb.scrollIntoViewIfNeeded().catch(() => {});
    await p.waitForTimeout(900);
    const cx = await sb.boundingBox().catch(() => null);
    log('caixa do botao de envio:', JSON.stringify(cx));
    if (cx) await p.mouse.click(cx.x + cx.width / 2, cx.y + cx.height / 2).catch(() => {});
    else await sb.click().catch(() => {});
    await p.waitForTimeout(14000);
    await p.screenshot({path: `result_${slug}.png`, fullPage: true});
    const diag = await p.evaluate(() => ({
      recaptchaToken: (document.querySelector('[name="g-recaptcha-response"]') || {}).value ? 'PREENCHIDO' : 'VAZIO',
      iframesCaptcha: [...document.querySelectorAll('iframe')].map(f => f.src).filter(u => /recaptcha|hcaptcha|challenges\.cloudflare/.test(u)).slice(0, 3),
      erros: [...document.querySelectorAll('[class*="error" i],[aria-invalid="true"]')].map(e => (e.innerText || '').replace(/\s+/g, ' ').trim()).filter(Boolean).slice(0, 6),
    }));
    log('DIAGNOSTICO:', JSON.stringify(diag));
    const txt = (await p.evaluate(() => document.body.innerText)).replace(/\s+/g, ' ').slice(0, 400);
    const ok = /thank you|thanks|received|successfully|submitted/i.test(txt);
    log(ok ? 'SUBMITTED OK' : 'RESULTADO DUVIDOSO', '| url:', p.url(), '| texto:', txt);
  } catch (e) {
    log('ERR', e.message.split('\n')[0]);
    await p.screenshot({path: `err_${slug}.png`, fullPage: true}).catch(() => {});
  }
  await b.close();
})();
