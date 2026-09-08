// Teamtailor. Uso: VINI_TEL='<formato internacional>' sh hb_run.sh apply_teamtailor.js <url> <slug> <cover.txt> [--submit]
// O telefone NUNCA fica escrito aqui: o repositorio e publico. Vem pela variavel de ambiente
// VINI_TEL, e o valor mora no documento privado do Drive "CAMPANHA - dados pessoais dos
// formularios (privado)".
const {chromium}=require('playwright'); const fs=require('fs');
const [url,slug,coverFile,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const D=__dirname;
const B={first:'Vini',last:'Cavalcanti',email:'contact@vinicavalcanti.art',phone:process.env.VINI_TEL||'',loc:'Olinda'};
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2400},acceptDownloads:true,
  userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-US'});
 const p=await ctx.newPage();
 // REDE, acrescentado em 08/09 na Sandbox Interactive. O Teamtailor grava as PERGUNTAS numa
 // chamada separada do envio, e quando ela falha a tela devolve so "Your answers could not be
 // saved", sem dizer qual pergunta nem por que. Sem este log a gente fica adivinhando.
 p.on('response', async r => {
   try {
     const req = r.request();
     if (req.method() === 'GET') return;
     if (r.status() < 400) return;
     let corpo = '';
     try {
       const bruto = await r.text();
       fs.writeFileSync(D + '/rede_' + slug + '_' + r.status() + '.html', bruto);
       fs.writeFileSync(D + '/rede_' + slug + '_' + r.status() + '.req.txt', req.postData() || '');
       corpo = bruto.replace(/\s+/g, ' ').slice(0, 400);
     } catch (_) {}
     log('[rede]', r.status(), req.method(), r.url().slice(0, 140), '| envio:',
         (req.postData() || '').replace(/\s+/g, ' ').slice(0, 300), '| resposta:', corpo);
   } catch (_) {}
 });
 try{
  await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'}); await p.waitForTimeout(4000);
  for(const t of ['Accept all','Accept All','Accept','Allow all']){ const e=await p.$(`button:has-text("${t}")`); if(e){ await e.click().catch(()=>{}); await p.waitForTimeout(1200); break; } }
  // O rotulo do botao muda de carreira para carreira (APPLY NOW, Apply here, Apply now) e em
  // varias delas o formulario e CARREGADO SO NA ROLAGEM: a pagina mostra "Loading application
  // form..." e o #candidate_first_name nunca aparece se ninguem rolar. Medido na Coffee Stain
  // North em 06/09, onde o script morria em timeout com a vaga viva e o formulario intacto.
  for(const t of ['APPLY NOW','Apply now','Apply here','Apply']){
    const ap=await p.$(`a:has-text("${t}"), button:has-text("${t}")`);
    if(ap){ await ap.click().catch(()=>{}); await p.waitForTimeout(4000); break; }
  }
  for(let i=0;i<12 && !(await p.$('#candidate_first_name'));i++){ await p.mouse.wheel(0,2500); await p.waitForTimeout(900); }
  await p.waitForSelector('#candidate_first_name',{timeout:60000});
  await p.fill('#candidate_first_name',B.first); await p.fill('#candidate_last_name',B.last); await p.fill('#candidate_email',B.email);
  if(await p.$('#candidate_phone')) await p.fill('#candidate_phone',B.phone).catch(()=>{});
  const loc=await p.$('#candidate_location');
  if(loc){
    await loc.click(); await loc.fill(''); await loc.type(B.loc,{delay:120}); await p.waitForTimeout(4000);
    // A lista da Teamtailor e um dropdown proprio: pegar SO os itens visiveis que contem o texto digitado.
    let escolhido=false;
    const cands=await p.$$('li, [role="option"], .pac-item, [class*="suggestion"], [class*="autocomplete"] div');
    for(const c of cands){
      const vis=await c.isVisible().catch(()=>false); if(!vis) continue;
      const t=((await c.innerText().catch(()=>''))||'').trim();
      if(t && t.length<90 && new RegExp(B.loc,'i').test(t)){ log('sugestao escolhida:',t); await c.click().catch(()=>{}); escolhido=true; break; }
    }
    if(!escolhido){ await p.keyboard.press('ArrowDown').catch(()=>{}); await p.waitForTimeout(700); await p.keyboard.press('Enter').catch(()=>{}); log('sem sugestao clicavel, usei teclado'); }
    await p.waitForTimeout(2000);
    const lido=await p.$eval('#candidate_location',e=>e.value).catch(()=>'');
    log('endereco lido de volta:',lido);
  }
  let faltando = [];
  // ARMADILHA MEDIDA NA STUNLOCK EM 06/09, e ela deixava o "Upload CV *" OBRIGATORIO VAZIO
  // sem uma linha de log: o input de arquivo do Teamtailor e um DROPZONE carregado em chunk
  // separado (dropzone-*.chunk.js). No instante em que este bloco rodava, logo depois dos
  // campos de nome, o #candidate_resume_remote_url AINDA NAO EXISTIA, entao o p.$() voltava
  // null, o script seguia calado e so a CAPTURA mostrava o campo vazio. Agora espera, confere
  // se o anexo entrou de verdade, e reclama alto quando o campo e obrigatorio e ficou vazio.
  let cv=await p.$('#candidate_resume_remote_url');
  if(!cv){ cv=await p.waitForSelector('#candidate_resume_remote_url',{timeout:25000,state:'attached'}).catch(()=>null); }
  if(cv){
    await cv.setInputFiles(D+'/Vini_Cavalcanti_CV.pdf').catch(e=>log('falha no anexo do CV',e.message.slice(0,60)));
    await p.waitForTimeout(6000);
    const nomes=await p.evaluate(()=>[...document.querySelectorAll('[data-dz-name],.dz-filename,[class*="filename"]')].map(e=>e.innerText.trim()).filter(Boolean));
    const url=await p.$eval('input[name="candidate[resume_remote_url]"]',e=>e.value).catch(()=>'');
    log('CV anexado | nomes na tela:',JSON.stringify(nomes),'| resume_remote_url:',url?('('+url.length+' chars)'):'(VAZIO)');
    if(!nomes.length && !url){ log('*** ATENCAO: o CV NAO subiu (nem nome na tela nem resume_remote_url) ***'); faltando.push('Upload CV'); }
  } else {
    const obrigCv=await p.$('label[for="candidate_resume_remote_url"] sup[data-asterisk], label[for="candidate_resume_remote_url"] sup').catch(()=>null);
    log('SEM CAMPO DE CV nesta vaga', obrigCv?'(mas o rotulo diz OBRIGATORIO)':'');
    if(obrigCv) faltando.push('Upload CV');
  }
  const cl=await p.$('textarea[name*="cover_letter"]');
  if(cl){ await cl.fill(fs.readFileSync(coverFile,'utf8')); log('carta preenchida'); }
  // PERGUNTAS CUSTOMIZADAS DO TEAMTAILOR, acrescentado em 06/09 porque elas travavam o envio em silencio.
  // Elas vem como candidate[answers_attributes][N][text] ou [N][boolean] (radio Yes/No), e o texto da
  // pergunta NAO fica no label do campo: fica no fieldset ou no bloco acima. Aqui a resposta e casada
  // pelo TEXTO DA PERGUNTA, lido do bloco, e nao pela ordem, que muda de vaga para vaga.
  const ansFile = D + '/ansq_' + slug + '.json';
  const QS = fs.existsSync(ansFile) ? JSON.parse(fs.readFileSync(ansFile, 'utf8')).perguntas : [];
  const grupos = await p.evaluate(() => {
    const vistos = {};
    document.querySelectorAll('[name^="candidate[answers_attributes]"]').forEach(e => {
      // 06/09, Coffee Stain North: existe um TERCEIRO tipo alem de text e boolean, o `choice`,
      // que e radio com opcoes proprias (1-3 people / 4-8 people ...). O script so conhecia
      // text e boolean e por isso NAO VIA a pergunta: ela nao aparecia nem como obrigatoria
      // sem resposta, e o envio parava sem dizer nada. Agora `choice` casa pelo RÓTULO da opcao.
      // 07/09, Fool's Theory: existe tambem o tipo `date` (When are you available to start),
      // OBRIGATORIO, e o detector nao o enxergava, entao a pergunta nao aparecia nem como
      // pendente e o envio voltava para a mesma pagina sem dizer nada.
      // 07/09, Ankama: alem de `choice` (radio, uma so) existe `choices[]` (caixas, varias),
      // e o detector nao o via. As duas obrigatorias da vaga, tipo de contrato e faixa
      // salarial, nao apareciam nem como pendentes e o envio voltaria calado.
      const m = e.name.match(/\[(\d+)\]\[(text|boolean|choice|choices|range|date|number)\]/);
      if (!m) return;
      const i = m[1];
      if (m[2] === 'choices') {
        let lab = '';
        if (e.id) { const l = document.querySelector(`label[for="${CSS.escape(e.id)}"]`); if (l) lab = l.innerText.trim(); }
        if (!lab && e.closest('label')) lab = e.closest('label').innerText.trim();
        if (!lab && e.parentElement) lab = e.parentElement.innerText.trim();
        if (!vistos[i]) vistos[i] = {idx: i, tipo: 'choices', pergunta: '', opcoes: []};
        vistos[i].opcoes.push({value: e.value, label: lab.slice(0, 90)});
        return;
      }
      if (m[2] === 'choice') {
        let lab = '';
        if (e.id) { const l = document.querySelector(`label[for="${CSS.escape(e.id)}"]`); if (l) lab = l.innerText.trim(); }
        if (!lab && e.parentElement) lab = e.parentElement.innerText.trim();
        if (!vistos[i]) vistos[i] = {idx: i, tipo: 'choice', pergunta: '', opcoes: []};
        vistos[i].opcoes.push({value: e.value, label: lab.slice(0, 90)});
      }
      if (!vistos[i]) {
        let q = '';
        let x = e.closest('fieldset') || e.closest('div');
        for (let k = 0; k < 6 && x; k++) {
          const t = (x.innerText || '').replace(/\s+/g, ' ').trim();
          if (t && t.length > 6 && !/^(Yes|No)\b/i.test(t)) { q = t; break; }
          x = x.parentElement;
        }
        vistos[i] = Object.assign(vistos[i] || {}, {idx: i, tipo: m[2], pergunta: q.slice(0, 200)});
      } else if (!vistos[i].pergunta) {
        let q = '';
        let x = e.closest('fieldset') || e.closest('div');
        for (let k = 0; k < 6 && x; k++) {
          const t = (x.innerText || '').replace(/\s+/g, ' ').trim();
          if (t && t.length > 6 && !/^(Yes|No)\b/i.test(t)) { q = t; break; }
          x = x.parentElement;
        }
        vistos[i].pergunta = q.slice(0, 200);
      }
    });
    return Object.values(vistos);
  });
  // Marca um radio do Teamtailor de verdade. Os radios ficam ESCONDIDOS atras de widget
  // proprio (dropdown ou botao estilizado) e o .check() do Playwright marca o input sem o
  // widget ver nada: a tela continua dizendo "can't be blank" e o envio nao entra. Medido
  // na Raw Power Games em 06/09, do mesmo jeito que ja tinha sido medido na TAT.
  // O que funciona e clicar no ROTULO ligado por for=, e depois CONFERIR que ficou marcado.
  // Escreve em campo que esta no DOM mas invisivel (pergunta condicional desligada pela
  // resposta anterior). Medido na Sandbox Interactive em 08/09: o servidor devolveu 422 com
  // aria-invalid="true" justamente na pergunta escondida, ou seja ELA CONTINUA OBRIGATORIA.
  async function escreveEscondido(el, val) {
    await el.evaluate((e, v) => {
      const proto = e.tagName === 'TEXTAREA' ? HTMLTextAreaElement : HTMLInputElement;
      const d = Object.getOwnPropertyDescriptor(proto.prototype, 'value');
      if (d && d.set) d.set.call(e, v); else e.value = v;
      e.dispatchEvent(new Event('input', {bubbles: true}));
      e.dispatchEvent(new Event('change', {bubbles: true}));
      e.dispatchEvent(new Event('blur', {bubbles: true}));
    }, val);
  }
  async function marcaRadio(name, value, rotulo) {
    const inp = await p.$(`input[name="${name}"][value="${value}"]`);
    if (!inp) return '(INPUT NAO ACHADO)';
    const id = await inp.getAttribute('id');
    if (id) { const lab = await p.$(`label[for="${id}"]`); if (lab) { await lab.click({force:true}).catch(()=>{}); await p.waitForTimeout(350); } }
    if (!await inp.isChecked().catch(()=>false)) await inp.check({force:true}).catch(()=>{});
    if (!await inp.isChecked().catch(()=>false)) await inp.evaluate(e=>{e.checked=true;e.dispatchEvent(new Event('change',{bubbles:true}));e.dispatchEvent(new Event('input',{bubbles:true}));}).catch(()=>{});
    const marcado = await p.$eval(`input[name="${name}"]:checked`, e => e.value).catch(()=>null);
    return marcado === String(value) ? 'ok' : `(NAO PEGOU, ficou ${marcado})`;
  }
  for (const g of grupos) {
    // Casar por TEXTO da pergunta e a regra. Mas o tipo `range` engana o detector: o bloco
    // ancestral do slider so contem o valor ("0 years"), nao o enunciado, entao nenhum rx casa
    // e a pergunta OBRIGATORIA aparece como "opcional sem resposta". Por isso o arquivo de
    // respostas tambem aceita `idx`, que casa pela posicao.
    const hit = QS.find(q => (q.idx !== undefined && String(q.idx) === String(g.idx)) || (q.rx && new RegExp(q.rx, 'i').test(g.pergunta)));
    if (!hit) {
      const obrig = /required|\*/i.test(g.pergunta) || g.tipo === 'range';
      log(obrig ? 'PERGUNTA OBRIGATORIA SEM RESPOSTA' : 'pergunta opcional sem resposta', '['+g.idx+']', g.pergunta);
      if (obrig) faltando.push(g.pergunta);
      continue;
    }
    if (g.tipo === 'choice') {
      // DEFEITO QUE QUASE MENTIU EM CAMPO DE AUTORIZACAO DE TRABALHO, medido na PFX em 06/09:
      // `new RegExp(undefined)` em JavaScript vira /(?:)/, que casa com TUDO. Se a resposta veio
      // com `valor` em vez de `opcao`, hit.opcao e undefined e o script marcava a PRIMEIRA opcao
      // da lista dizendo "ok". Em pergunta de elegibilidade, a primeira opcao costuma ser "Yes".
      if (hit.opcao === undefined || hit.opcao === null || String(hit.opcao) === '') {
        log('RECUSO DE ADIVINHAR ['+g.idx+']', g.pergunta.slice(0,70),
            '| esta pergunta e do tipo choice e precisa de "opcao" no arquivo de respostas, nao "valor".',
            '| opcoes:', JSON.stringify((g.opcoes||[]).map(o=>o.label)));
        faltando.push(g.pergunta);
        continue;
      }
      const alvo = (g.opcoes || []).find(o => new RegExp(hit.opcao, 'i').test(o.label));
      if (!alvo) { log('OPCAO NAO ACHADA ['+g.idx+']', g.pergunta.slice(0,60), '| opcoes:', JSON.stringify((g.opcoes||[]).map(o=>o.label))); faltando.push(g.pergunta); continue; }
      const name = `candidate[answers_attributes][${g.idx}][choice]`;
      const r = await p.$(`input[name="${name}"][value="${alvo.value}"]`);
      let estado;
      if (r) estado = await marcaRadio(name, alvo.value, alvo.label);
      else {
        const sel2 = await p.$(`select[name="${name}"]`);
        if (!sel2) { log('CAMPO choice NAO ACHADO ['+g.idx+']'); faltando.push(g.pergunta); continue; }
        await sel2.selectOption(String(alvo.value)).catch(async()=>{ await sel2.selectOption({label: alvo.label}).catch(()=>{}); });
        estado = (await sel2.inputValue().catch(()=>'')) === String(alvo.value) ? 'ok' : '(NAO PEGOU)';
      }
      log('respondida ['+g.idx+']', g.pergunta.slice(0, 60), '=>', alvo.label, '|', estado);
      if (estado !== 'ok') faltando.push(g.pergunta);
    } else if (g.tipo === 'boolean') {
      const val = hit.valor === true || /^(sim|yes|true)$/i.test(String(hit.valor)) ? 'true' : 'false';
      const name = `candidate[answers_attributes][${g.idx}][boolean]`;
      const estado = await marcaRadio(name, val, val);
      log('respondida ['+g.idx+']', g.pergunta.slice(0, 60), '=>', val, '|', estado);
      if (estado !== 'ok') faltando.push(g.pergunta);
    } else if (g.tipo === 'number') {
      // TIPO `number`, medido na Sandbox Interactive em 08/09, e ele custou DOIS envios
      // reprovados com 422 antes de aparecer. E o quinto tipo que o detector nao conhecia
      // (depois de choice, date, choices e range) e falha do mesmo jeito silencioso: a
      // pergunta "How many years of experience do you have in 3D environment art?" nao
      // aparecia nem como pendente, e a tela so dizia "Your answers could not be saved".
      const el = await p.$(`[name="candidate[answers_attributes][${g.idx}][number]"]`);
      if (!el) { log('CAMPO number NAO ACHADO ['+g.idx+']'); faltando.push(g.pergunta); continue; }
      const v = String(hit.valor);
      if (await el.isVisible().catch(() => false)) await el.fill(v).catch(() => {});
      else await escreveEscondido(el, v);
      const lido = await el.inputValue().catch(() => '');
      log('respondida ['+g.idx+']', g.pergunta.slice(0, 60), '=> number', v, '| lido de volta', lido);
      if (String(lido) !== v) faltando.push(g.pergunta + ' (number nao pegou, ficou ' + lido + ')');
    } else if (g.tipo === 'range') {
      // TIPO `range`, medido na Triband em 06/09. E um SLIDER com um numero editavel ao lado
      // (`input[name="range-custom_number"]`). O script nao conhecia esse tipo, entao a pergunta
      // obrigatoria "For how long have you been working in game development" nem aparecia como
      // pendente e o envio voltava para a mesma pagina sem dizer nada.
      const name = `candidate[answers_attributes][${g.idx}][range]`;
      const el = await p.$(`[name="${name}"]`);
      if (!el) { log('CAMPO range NAO ACHADO ['+g.idx+']'); faltando.push(g.pergunta); }
      else {
        const v = String(hit.valor);
        await el.evaluate((e, val) => {
          const set = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
          set.call(e, val);
          e.dispatchEvent(new Event('input', { bubbles: true }));
          e.dispatchEvent(new Event('change', { bubbles: true }));
        }, v);
        await p.waitForTimeout(500);
        const lido = await el.inputValue().catch(() => '');
        log('respondida ['+g.idx+']', g.pergunta.slice(0, 60), '=> range', v, '| lido de volta', lido);
        if (String(lido) !== v) faltando.push(g.pergunta + ' (range nao pegou, ficou ' + lido + ')');
      }
    } else if (g.tipo === 'choices') {
      // MULTI-ESCOLHA. Tres armadilhas ja medidas se somam aqui:
      // (1) as caixas costumam estar dentro de um painel FECHADO (display:none, offsetHeight 0)
      //     e nem check({force:true}) marca; abre-se clicando no botao "Selecionar uma ou mais
      //     opcoes" e clicando em div[role=menu] button[role=menuitemcheckbox] pelo texto exato;
      // (2) o name se repete, entao ler por querySelector mente: confere-se por value;
      // (3) enviar com o PAINEL ABERTO nao grava a resposta, entao fecha-se antes de enviar.
      const alvos = (Array.isArray(hit.opcoes) ? hit.opcoes : [hit.opcao]).filter(Boolean);
      const name = `candidate[answers_attributes][${g.idx}][choices][]`;
      let abriu = false;
      for (const alvoTxt of alvos) {
        const op = (g.opcoes || []).find(o => new RegExp(alvoTxt, 'i').test(o.label));
        if (!op) { log('OPCAO NAO ACHADA ['+g.idx+']', alvoTxt, '| opcoes:', JSON.stringify((g.opcoes||[]).map(o=>o.label))); faltando.push(g.pergunta + ' / ' + alvoTxt); continue; }
        const sel = `input[name="${name}"][value="${op.value}"]`;
        let vis = await p.evaluate(s => { const e=document.querySelector(s); return !!(e && e.offsetHeight); }, sel);
        if (!vis && !abriu) {
          const btn = await p.$('form button[type=button]:has-text("options"), form button[type=button]:has-text("option")');
          if (btn) { await btn.click().catch(()=>{}); await p.waitForTimeout(1200); abriu = true; }
        }
        let ok = false;
        const item = await p.$(`div[role=menu] button[role=menuitemcheckbox]:has-text("${op.label.replace(/"/g,'')}")`);
        if (item) { await item.click().catch(()=>{}); await p.waitForTimeout(500); }
        ok = await p.evaluate(s => { const e=document.querySelector(s); return !!(e && e.checked); }, sel);
        if (!ok) {
          const cb = await p.$(sel);
          if (cb) {
            const id = await cb.getAttribute('id');
            if (id) { const lab = await p.$(`label[for="${id}"]`); if (lab) await lab.click({force:true}).catch(()=>{}); }
            if (!await p.evaluate(s=>{const e=document.querySelector(s);return !!(e&&e.checked);},sel)) await cb.check({force:true}).catch(()=>{});
          }
          ok = await p.evaluate(s => { const e=document.querySelector(s); return !!(e && e.checked); }, sel);
        }
        log('respondida ['+g.idx+'] choices =>', op.label, '|', ok ? 'ok' : '(NAO MARCOU)');
        if (!ok) faltando.push(g.pergunta + ' / ' + op.label);
      }
      if (abriu) {
        const btn = await p.$('form button[type=button]:has-text("options"), form button[type=button]:has-text("option")');
        if (btn) { await btn.click().catch(()=>{}); await p.waitForTimeout(800); log('painel de multi-escolha ['+g.idx+'] FECHADO antes do envio'); }
      }
    } else if (g.tipo === 'date') {
      // input[type=date] NAO aceita digitacao solta: teclar 2026-11-06 grava 1106-02-02 e o log
      // diz ok. Preenche por fill() com ISO e RELE o valor antes de dar por respondida.
      const name = `candidate[answers_attributes][${g.idx}][date]`;
      const el = await p.$(`[name="${name}"]`);
      if (!el) { log('CAMPO date NAO ACHADO ['+g.idx+']'); faltando.push(g.pergunta); }
      else {
        const v = String(hit.valor);
        await el.fill(v).catch(async()=>{ await el.evaluate((e,val)=>{e.value=val;e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));},v); });
        await p.waitForTimeout(400);
        const lido = await el.inputValue().catch(()=>'');
        log('respondida ['+g.idx+']', g.pergunta.slice(0,60), '=> date', v, '| lido de volta', lido);
        if (lido !== v) faltando.push(g.pergunta + ' (date nao pegou, ficou ' + lido + ')');
      }
    } else {
      const el = await p.$(`[name="candidate[answers_attributes][${g.idx}][text]"]`);
      // PERGUNTA CONDICIONAL, medida na Sandbox Interactive em 08/09. A pergunta "Were you
      // referred by someone?" e boolean, e a seguinte, "If so, kindly provide their name",
      // e um texto marcado como OBRIGATORIO que so aparece quando a resposta e Yes. Com a
      // resposta No ela existe no DOM mas fica invisivel, e o `fill` ficava 30 s tentando e
      // MATAVA A RODADA INTEIRA com ERR, com o formulario ja todo preenchido. Campo invisivel
      // nao e campo pendente: e pergunta que a propria vaga desligou.
      if (!el) { log('CAMPO text NAO ACHADO ['+g.idx+']'); continue; }
      const visivel = await el.isVisible().catch(() => false);
      if (visivel) {
        await el.fill(String(hit.valor)).catch(e => { log('FALHA no fill ['+g.idx+']', e.message.split('\n')[0]); faltando.push(g.pergunta); });
      } else {
        // O `fill` do Playwright espera o campo ficar visivel e morre em 30 s. O setter nativo
        // escreve assim mesmo, que e o que este caso pede.
        await escreveEscondido(el, String(hit.valor));
      }
      log('respondida ['+g.idx+']', g.pergunta.slice(0, 60), '=>', String(hit.valor).slice(0, 50), visivel ? '' : '| campo ESCONDIDO, escrito pelo setter nativo');
    }
  }
  if (faltando.length && SUBMIT) {
    log('NAO VOU ENVIAR: ficaram', faltando.length, 'perguntas obrigatorias sem resposta. Responda no ansq_' + slug + '.json e rode de novo.');
    await p.screenshot({path: `err_${slug}.png`, fullPage: true});
    await b.close();
    return;
  }
  // LOCATIONS, campo proprio do Teamtailor e OBRIGATORIO em varias vagas, que o script nao
  // conhecia. Medido na Raw Power Games em 06/09: tudo preenchido, o envio voltou para a
  // mesma pagina e so a captura mostrava o erro Can't be blank em Locations. Sem isto o
  // script anuncia RESULTADO DUVIDOSO e a candidatura simplesmente nao entra.
  const locs = await p.$$('input[name="candidate[location_ids][]"]');
  if (locs.length) {
    const querido = (fs.existsSync(D+'/ansq_'+slug+'.json') ? (JSON.parse(fs.readFileSync(D+'/ansq_'+slug+'.json','utf8')).locations || []) : []);
    let marcou = 0;
    for (const c of locs) {
      const id = await c.getAttribute('id');
      let lab = '';
      if (id) lab = await p.$eval(`label[for="${id}"]`, e => e.innerText.trim()).catch(() => '');
      const quer = querido.length ? querido.some(rx => new RegExp(rx, 'i').test(lab)) : true;
      if (!quer) continue;
      await c.check({force: true}).catch(() => {});
      if (await c.isChecked().catch(() => false)) { marcou++; log('location marcada:', lab); }
    }
    if (!marcou) { log('ATENCAO: nenhuma location marcada, e o campo e obrigatorio'); faltando.push('Locations'); }
  }
  if (faltando.length && SUBMIT) {
    log('NAO VOU ENVIAR: faltou', JSON.stringify(faltando));
    await p.screenshot({path: `err_${slug}.png`, fullPage: true}); await b.close(); return;
  }
  for(const id of ['candidate_consent_given','candidate_consent_given_future_jobs']){
    const c=await p.$('#'+id); if(c){ const on=await c.isChecked().catch(()=>false); if(!on) await c.check({force:true}).catch(()=>{}); log('marcado',id); } }
  await p.waitForTimeout(1500);
  await p.screenshot({path:`filled_${slug}.png`,fullPage:true});
  const rb=await p.evaluate(()=>['candidate_first_name','candidate_last_name','candidate_email','candidate_phone','candidate_location']
    .map(i=>{const e=document.getElementById(i);return [i, e?(e.value||'(VAZIO)'):'(NAO ENCONTRADO)'];}));
  for(const [i,v] of rb) log('  leitura de volta',i,'=>',v);
  if(!SUBMIT){ log('DRY RUN'); await b.close(); return; }
  const sb=await p.$('input[name="commit"], button:has-text("Submit application")');
  if(!sb){ log('SEM BOTAO DE ENVIO'); await b.close(); return; }
  await sb.click(); await p.waitForTimeout(9000);
  await p.screenshot({path:`result_${slug}.png`,fullPage:true});
  const txt=(await p.evaluate(()=>document.body.innerText)).replace(/\s+/g,' ').slice(0,400);
  // FALSO NEGATIVO MEDIDO NA ANKAMA EM 07/09, e ele e o erro mais caro que existe porque leva
  // a REENVIAR: o board estava em frances e a tela dizia "A postule a Artiste 3D. Merci pour
  // votre candidature. Nous avons recu votre candidature", com a URL ja em /thanks/, e a regex
  // so em ingles marcou RESULTADO DUVIDOSO. Agora aceita frances, espanhol e alemao, e a URL
  // /thanks/ conta como prova por si so, que e o que o Teamtailor faz em toda lingua.
  const ok=(/thank you|thanks for|received|we have got|application sent|applied to|merci pour|nous avons re.u|a postul|gracias por|hemos recibido|vielen dank|erhalten|obrigad/i.test(txt)
            || /\/thanks\//.test(p.url()))
           && !(await p.$('#candidate_first_name'));
  log(ok?'SUBMITTED OK':'RESULTADO DUVIDOSO','| url:',p.url(),'| texto:',txt);
 }catch(e){ log('ERR',e.message); await p.screenshot({path:`err_${slug}.png`,fullPage:true}).catch(()=>{}); }
 await b.close();
})();
