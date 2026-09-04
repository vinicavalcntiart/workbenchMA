// Greenhouse job-boards filler. Uso: node apply_gh.js <url> <slug> <answers.json> [--submit]
const {chromium}=require('playwright'); const fs=require('fs');
const [url,slug,ansFile,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const A=JSON.parse(fs.readFileSync(ansFile));
const BASE={first:'Vini',last:'Cavalcanti',email:'contact@vinicavalcanti.art',phone:'+55 81 97306 2286',country:'Brazil',city:'Olinda, Pernambuco, Brazil',
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
  if(await p.$('#phone')){ await p.fill('#phone',BASE.phone); }
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
    const sel='#'+q.id.replace(/([\[\]])/g,'\\$1');
    const el=await p.$(sel); if(!el){ log('missing',q.id,q.label); continue; }
    const role=await el.getAttribute('role'); const cls=(await el.getAttribute('class'))||'';
    // Campo que o Greenhouse renderiza como combobox mas que a resposta trata como
    // texto (State, por exemplo) chegava aqui sem prefs e derrubava a execucao inteira.
    if(q.type==='select'||role==='combobox'||/select__input/.test(cls)){ await pick(sel,q.prefs||[q.text||''],q.label,q.first); }
    else { await p.fill(sel,q.text||''); log('filled',q.label); }
  }
  // EEO / demographic selects: decline
  for(const id of ['gender','hispanic_ethnicity','veteran_status','disability_status','race']){ if(await p.$('#'+id)) await pick('#'+id,['don\'t wish','not wish','Decline','Prefer not'],id).catch(()=>{}); }
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
    let v=(el.value||'').trim();
    if(!v){
      // react-select nao guarda o texto no input: o escolhido fica em single-value ou multi-value.
      const box=el.closest('[class*="select__control"]')||el.closest('[class*="select-shell"]')||el.parentElement;
      if(box){ const parts=[...box.querySelectorAll('[class*="single-value"], [class*="multi-value__label"]')].map(n=>n.innerText.trim()).filter(Boolean);
        v = parts.length ? parts.join(' + ') : box.innerText.replace(/\s+/g,' ').trim().slice(0,80); }
    }
    return [id, v||'(VAZIO)'];
  }), ['first_name','last_name','email','phone'].concat(A.questions.map(q=>q.id.replace(/\[\]$/,''))));
  for(const [id,v] of readback) log('  leitura de volta', id, '=>', v);
  const vazios=readback.filter(([,v])=>v==='(VAZIO)'||v==='(CAMPO NAO ENCONTRADO)').map(([id])=>id);
  if(vazios.length) log('ATENCAO, campos sem valor lido:',JSON.stringify(vazios));
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
