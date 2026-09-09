// Greenhouse job-boards filler. Uso: node apply_gh.js <url> <slug> <answers.json> [--submit]
const {chromium}=require('playwright'); const fs=require('fs');
const [url,slug,ansFile,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const A=JSON.parse(fs.readFileSync(ansFile));
// O telefone NAO fica escrito aqui: este repositorio e publico. Ele vem da variavel de
// ambiente VINI_TEL, e o valor esta no documento privado do Drive "CAMPANHA - dados
// pessoais dos formularios". Sem ela, o script para antes de abrir o navegador em vez de
// mandar formulario sem telefone.
const TEL=process.env.VINI_TEL;
if(!TEL){ console.error('[erro] falta a variavel de ambiente VINI_TEL com o telefone dele'); process.exit(1); }
const BASE={first:'Vini',last:'Cavalcanti',email:'contact@vinicavalcanti.art',phone:TEL,country:'Brazil',city:'Olinda, Pernambuco, Brazil',
 resume:'/tmp/claude-0/-home-user-workbenchMA/98c8eec1-87ea-55f1-bd77-423c5af62326/scratchpad/apply/Vini_Cavalcanti_CV.pdf',
 cover:'/tmp/claude-0/-home-user-workbenchMA/98c8eec1-87ea-55f1-bd77-423c5af62326/scratchpad/apply/Vini_Cavalcanti_Cover_Letter.pdf'};
const log=(...a)=>console.log(`[${slug}]`,...a);
(async()=>{
 // Half Breaks, rodada 1: modo headless levava a recusa seca de sessao em varios ATS.
 // Tela de verdade e o padrao agora; rode sempre por hb_run.sh, que sobe o Xvfb.
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2400},userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-US'});
 const p=await ctx.newPage();
 try{
  await p.goto(url,{timeout:120000,waitUntil:'networkidle'}).catch(()=>{}); await p.waitForSelector('#first_name',{timeout:60000}); await p.waitForTimeout(3000);
  await p.fill('#first_name',BASE.first); await p.fill('#last_name',BASE.last); await p.fill('#email',BASE.email);
  // ARMADILHA MEDIDA NA EPIC (09/09): o Greenhouse novo monta o telefone com o
  // intl-tel-input, que e um SELETOR DE PAIS separado (#iti-0__search-input) grudado no
  // #phone. A regra do documento privado vale aqui: escolher o pais no seletor e escrever
  // no campo do numero SO os digitos, sem +55. Repetir o codigo faz a validacao recusar.
  // Sem esta parte o formulario sai com bandeira errada e numero invalido, e ninguem avisa.
  if(await p.$('#phone')){
    const bandeira=await p.$('.iti__selected-country, [aria-controls*="iti-0__dropdown"], button[class*="iti__selected"]');
    if(bandeira){
      await bandeira.click({force:true}).catch(()=>{});
      await p.waitForTimeout(900);
      const busca=await p.$('#iti-0__search-input');
      if(busca){ await busca.fill('Brazil').catch(()=>{}); await p.waitForTimeout(900); }
      const opcao=await p.$('#iti-0__item-br, li[id*="item-br"], .iti__country[data-country-code="br"]');
      if(opcao){ await opcao.click({force:true}).catch(()=>{}); log('pais do telefone => Brazil (+55)'); }
      else { await p.keyboard.press('Enter').catch(()=>{}); log('pais do telefone: escolhi pelo Enter, confira a leitura de volta'); }
      await p.waitForTimeout(700);
    }
    await p.fill('#phone',BASE.phone);
  }
  // combobox helper: type and pick best option
  async function pick(inputSel, prefs, label, fallbackFirst){
    const inp=await p.$(inputSel); if(!inp){ log('no field',label); return false; }
    const role=await inp.getAttribute('role'); const pop=await inp.getAttribute('aria-haspopup');
    if(role!=='combobox' && !pop){ await inp.fill(prefs[0].replace(/[\^$]/g,'')); log('text-filled',label); return true; }
    await inp.click(); await p.waitForTimeout(500);
    const readOpts=async()=>p.$$eval('[class*="select__menu"] [class*="option"], [id*="react-select"][id*="-option-"]',els=>els.filter(e=>e.offsetParent!==null).map(e=>e.innerText.trim()));
    let opts=await readOpts();
    if(!opts.length){ await p.keyboard.press('ArrowDown'); await p.waitForTimeout(600); opts=await readOpts(); }
    let choice=null;
    for(const pref of prefs){ const re=new RegExp(pref,'i'); choice=opts.find(o=>re.test(o)&&o!=='No options'); if(choice) break; }
    if(!choice){
      for(const pref of prefs){ const word=pref.replace(/[\^$\\]/g,'').slice(0,6); await inp.fill(''); await inp.type(word); await p.waitForTimeout(700); const o2=await readOpts(); const re=new RegExp(pref,'i'); choice=o2.find(o=>re.test(o)&&o!=='No options'); if(choice){ opts=o2; break; } }
    }
    if(!choice && fallbackFirst){ await inp.fill(''); await p.waitForTimeout(500); opts=(await readOpts()).filter(o=>o!=='No options'); if(!opts.length){ await p.keyboard.press('ArrowDown'); await p.waitForTimeout(600); opts=(await readOpts()).filter(o=>o!=='No options'); } choice=opts[0]; }
    if(!choice){ log('OPTIONS for',label,'=>',JSON.stringify(opts.slice(0,15)),'| no match for',prefs); await p.keyboard.press('Escape'); return false; }
    await inp.fill(''); await inp.type(choice.replace(/\s*\+\d+$/,'').slice(0,40)); await p.waitForTimeout(700); opts=await readOpts();
    let idx=opts.findIndex(o=>o===choice); if(idx<0) idx=0;
    for(let i=0;i<idx;i++) await p.keyboard.press('ArrowDown');
    await p.keyboard.press('Enter'); await p.waitForTimeout(400); log('picked',label,'=>',opts[idx]); return true;
  }
  // country/location
  if(await p.$('#country')){ await pick('#country',['^Brazil'],'country'); await p.keyboard.press('Escape'); await p.click('body',{position:{x:5,y:5}}).catch(()=>{}); }
  if(await p.$('#candidate-location')){ const el=await p.$('#candidate-location'); await el.focus(); await el.type(A.city||BASE.city,{delay:60}); await p.waitForTimeout(3500); const o=await p.$$eval('[class*="select__menu"] [class*="option"]',els=>els.map(e=>e.innerText.trim())); log('location options:',JSON.stringify(o.slice(0,3))); if(o.length){ await p.keyboard.press('Enter'); } await p.waitForTimeout(500); log('location value:',await p.$eval('#candidate-location',e=>e.value||e.getAttribute('aria-activedescendant')||'(selected)')); }
  if(await p.$('#resume')) await p.setInputFiles('#resume',BASE.resume);
  if(await p.$('#cover_letter')) await p.setInputFiles('#cover_letter',BASE.cover);
  await p.waitForTimeout(3000);
  // questions
  for(const q of A.questions){
    // ARMADILHA MEDIDA NA EPIC (09/09): os campos de dados demograficos do Greenhouse tem
    // id PURAMENTE NUMERICO (4000367004). '#4000367004' nao e seletor CSS valido, e o
    // querySelectorAll estoura SyntaxError, que caia no catch de fora e abortava o
    // preenchimento inteiro depois de tudo ja estar digitado. Id que comeca com digito vai
    // por seletor de atributo.
    const sel=/^\d/.test(q.id) ? '[id="'+q.id+'"]' : '#'+q.id.replace(/([\[\]])/g,'\\$1');
    const el=await p.$(sel); if(!el){ log('missing',q.id,q.label); continue; }
    const role=await el.getAttribute('role'); const cls=(await el.getAttribute('class'))||'';
    // Campo que o Greenhouse renderiza como combobox mas que a resposta trata como
    // texto (State, por exemplo) chegava aqui sem prefs e derrubava a execucao inteira.
    // CAIXA DE MARCAR: o consentimento de dados demograficos da Epic e um checkbox, e o
    // p.fill() de antes estourava excecao nele, o que abortava o preenchimento INTEIRO
    // pelo catch de fora. Marcar so quando a resposta pedir, nunca por padrao: honeypot
    // (beecatcher, hp_, honeypot) fica SEMPRE vazio.
    const tipo=(await el.getAttribute('type'))||'';
    if(tipo==='checkbox'||tipo==='radio'){
      if(/honeypot|beecatcher|^hp_/i.test(q.id)){ log('honeypot, deixando vazio', q.id); continue; }
      const querMarcar=q.marcar!==false;
      if(querMarcar){ await el.check({force:true}).catch(async()=>{ await el.click({force:true}).catch(()=>{}); }); log('marcado',q.label); }
      else log('deixado desmarcado',q.label);
      continue;
    }
    if(q.type==='select'||role==='combobox'||/select__input/.test(cls)){ await pick(sel,q.prefs||[q.text||''],q.label,q.first); }
    else { await p.fill(sel,q.text||''); log('filled',q.label); }
  }
  // EEO / demographic selects: decline
  // 'I do not want to answer' entrou em 09/09: o disability_status da Mob Entertainment nao
  // oferece 'Decline' nem 'wish', so essa frase, e sem ela o campo ficava sem resposta.
  for(const id of ['gender','hispanic_ethnicity','veteran_status','disability_status','race']){ if(await p.$('#'+id)) await pick('#'+id,['don\'t wish','not wish','do not want to answer','Decline','Prefer not'],id).catch(()=>{}); }
  await p.waitForTimeout(1000);
  await p.screenshot({path:`filled_${slug}.png`,fullPage:true});
  const missing=await p.$$eval('[aria-invalid="true"], .field-error, .error',els=>els.map(e=>e.id||e.innerText.slice(0,60)));
  log('pre-submit invalid:',JSON.stringify(missing.slice(0,10)));
  // Half Breaks, regra da leitura de volta: erro que nao levanta excecao e o mais caro.
  // Antes de enviar, le o que de fato ficou em cada campo e mostra no log. Foi assim que
  // o Airtable da Mighty Nice enviou sete etiquetas de competencia em branco sem avisar.
  const readback=await p.evaluate(ids=>ids.map(id=>{
    const el=document.getElementById(id)||document.getElementById(id+'[]');
    if(!el) return [id,'(CAMPO NAO ENCONTRADO)'];
    // checkbox devolve value="on" marcado ou nao, entao a leitura de volta antiga mentia:
    // dizia "on" para caixa desmarcada. O que vale aqui e o .checked.
    if(el.type==='checkbox'||el.type==='radio') return [id, el.checked?'MARCADO':'DESMARCADO'];
    let v=(el.value||'').trim();
    if(!v){
      // react-select nao guarda o texto no input: o escolhido fica em single-value ou multi-value.
      const box=el.closest('[class*="select__control"]')||el.closest('[class*="select-shell"]')||el.parentElement;
      if(box){ const parts=[...box.querySelectorAll('[class*="single-value"], [class*="multi-value__label"]')].map(n=>n.innerText.trim()).filter(Boolean);
        v = parts.length ? parts.join(' + ') : box.innerText.replace(/\s+/g,' ').trim().slice(0,80); }
    }
    return [id, v||'(VAZIO)'];
  }), ['first_name','last_name','email','phone','country','candidate-location'].concat(A.questions.map(q=>q.id.replace(/\[\]$/,''))));
  for(const [id,v] of readback) log('  leitura de volta', id, '=>', v);
  const vazios=readback.filter(([,v])=>v==='(VAZIO)'||v==='(CAMPO NAO ENCONTRADO)').map(([id])=>id);
  if(vazios.length) log('ATENCAO, campos sem valor lido:',JSON.stringify(vazios));
  // LEITURA DE VOLTA DOS ANEXOS, nova em 09/09. O anexo era o unico obrigatorio que a
  // conferencia NAO olhava: o setInputFiles vai em '#resume', e quadro que renomeia o
  // input deixaria a candidatura sair SEM CURRICULO, com 'pre-submit invalid: []' na tela,
  // que e o retrato do erro caro desta campanha (parece certo, nao levanta excecao).
  // MEDIDO EM 09/09 e a medicao mudou o teste: depois do setInputFiles o React do Greenhouse
  // TROCA a area de anexo por uma etiqueta com o nome do arquivo e TIRA o input do DOM. Entao
  // "zero input[type=file]" nao quer dizer "sem curriculo", quer dizer "ja anexou" — e contar
  // input teria dado um alarme falso bem no minuto do envio. O que prova de verdade e o NOME
  // DO ARQUIVO aparecendo no formulario.
  const nomeCV=BASE.resume.split('/').pop(), nomeCarta=BASE.cover.split('/').pop();
  const prova=await p.evaluate(([cv,carta])=>{
    const t=(document.querySelector('form')||document.body).innerText;
    return {inputs:document.querySelectorAll('input[type=file]').length,
            cv:t.includes(cv), carta:t.includes(carta),
            trecho:(t.match(/[^\n]*\.pdf[^\n]*/g)||[]).slice(0,4)};
  },[nomeCV,nomeCarta]);
  log('  anexo: input[type=file] restantes =',prova.inputs,'| CV visivel no formulario =',prova.cv,'| carta =',prova.carta,'|',JSON.stringify(prova.trecho));
  if(!prova.cv) log('!! PARE: o nome do CV NAO aparece no formulario. Nao envie sem conferir o print.');
  if(!SUBMIT){ log('DRY RUN done'); await b.close(); return; }
  const btn=await p.$('button:has-text("Submit application"), button[type=submit]:has-text("Submit"), input[type=submit]');
  await btn.click(); await p.waitForTimeout(9000);
  let txt=(await p.innerText('body')).replace(/\s+/g,' ');
  if(/verification code|security code/i.test(txt)){
    log('EMAIL CODE REQUIRED; waiting for file code_'+slug+'.txt (up to 6 min)');
    fs.writeFileSync(`needcode_${slug}.txt`, new Date().toISOString());
    let code=null; for(let i=0;i<72;i++){ if(fs.existsSync(`code_${slug}.txt`)){ code=fs.readFileSync(`code_${slug}.txt`,'utf8').trim(); break; } await p.waitForTimeout(5000); }
    if(!code){ log('no code received'); await p.screenshot({path:`result_${slug}.png`,fullPage:true}); await b.close(); return; }
    const inputs=await p.$$('input[autocomplete="one-time-code"], input[name*="code" i], input[id*="code" i], input[aria-label*="code" i], input[aria-label*="digit" i], input[maxlength="1"]');
    log('code inputs found:',inputs.length);
    if(inputs.length>=code.length){ for(let i=0;i<code.length;i++){ await inputs[i].click(); await p.keyboard.type(code[i]); } }
    else if(inputs.length){ await inputs[0].click(); await p.keyboard.type(code); }
    else { await p.keyboard.type(code); }
    await p.waitForTimeout(1500);
    const btn2=await p.$('button:has-text("Submit application"), button:has-text("Submit"), button:has-text("Verify")'); if(btn2) await btn2.click();
    await p.waitForTimeout(9000);
    txt=(await p.innerText('body')).replace(/\s+/g,' ');
  }
  // A Scopely confirma com 'Application Sent!' e a regex antiga nao pegava, o que marcou
  // como NOT CONFIRMED uma candidatura que TINHA sido enviada. Falso negativo aqui e o
  // erro mais caro possivel: leva a reenviar. A URL /confirmation tambem conta como prova.
  const ok=/thank you for applying|application (has been |was )?submitted|application sent|thanks for applying|we have received your application|we've received your application/i.test(txt) || /\/confirmation(\?|$)/.test(p.url());
  const errs=await p.$$eval('[aria-invalid="true"], .field-error, [class*="error"]',els=>els.map(e=>(e.innerText||e.id||'').slice(0,80)).filter(Boolean));
  await p.screenshot({path:`result_${slug}.png`,fullPage:true});
  log(ok?'SUBMITTED OK':'NOT CONFIRMED','| url:',p.url(),'| errs:',JSON.stringify(errs.slice(0,8)),'| text:',txt.slice(0,300));
 }catch(e){ log('ERR',e.message.split('\n')[0]); await p.screenshot({path:`err_${slug}.png`,fullPage:true}).catch(()=>{}); }
 await b.close();
})();
