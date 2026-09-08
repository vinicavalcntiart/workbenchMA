// Blue Zoo (careers.blue-zoo.co.uk, ASP.NET proprio). uso: node apply_bluezoo.js <VacancyID> <slug> [--submit]
// Credenciais SO por ambiente (BZ_SENHA): o repositorio da campanha e PUBLICO.
// ARMADILHA: /vacancies/vacancy-apply.aspx?VacancyID=<id> REDIRECIONA para /registration.aspx.
// A candidatura exige conta, e o cadastro ja pede senha na propria tela (diferente do Talentsoft,
// que manda link por email).
const {chromium}=require('playwright');
const [VID,slug,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const SENHA=process.env.BZ_SENHA; const D=__dirname+'/';
const log=(...a)=>console.log('['+slug+']',...a);
if(!SENHA){ console.log('faltou BZ_SENHA no ambiente'); process.exit(1); }
const RESP=[
 ['CanC_FirstName','Vini'],
 ['CanC_Surname','Cavalcanti'],
 ['CanC_Email','contact@vinicavalcanti.art'],
 ['Email_Copy1','contact@vinicavalcanti.art'],
 ['CanC_WebsiteAddress','https://www.artstation.com/viniciuscavalcanti'],
 ['Question_1_199','No password, the portfolio is public.'],
];
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1300,height:2800},userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-GB'})).newPage();
 const dump=async(tag)=>{
  const c=await p.evaluate(()=>[...document.querySelectorAll('input,select,textarea')].filter(e=>e.type!=='hidden'&&e.offsetParent!==null)
    .map(e=>({n:(e.name||e.id||'').split('$').pop(),t:e.type||e.tagName,req:!!(e.required||e.getAttribute('aria-required')==='true'),
      v:(e.type==='password'?(e.value?'(preenchida, '+e.value.length+' caracteres)':''):(e.value||'').slice(0,28)),lab:((e.labels&&e.labels[0]?e.labels[0].innerText:'')||e.getAttribute('aria-label')||e.placeholder||'').replace(/\s+/g,' ').trim().slice(0,50)})));
  log('=== CAMPOS ('+tag+'):',c.length,'==='); c.forEach(x=>log('   ',JSON.stringify(x)));
  const err=await p.evaluate(()=>[...new Set([...document.querySelectorAll('[class*="error"],[role="alert"],[class*="validation"],[class*="required"]')].filter(e=>e.offsetParent!==null).map(e=>(e.innerText||'').replace(/\s+/g,' ').trim()).filter(t=>t&&t.length<130))]);
  if(err.length){ log('VALIDACAO ('+tag+'):'); err.slice(0,12).forEach(e=>log('   !',e)); }
  return c; };
 try{
  await p.goto(`https://careers.blue-zoo.co.uk/vacancies/vacancy-apply.aspx?VacancyID=${VID}`,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(7000);
  // o banner de cookie daqui e um input[type=submit] com value "Accept All Cookies", entao
  // seletor de button/a nao pega e o banner fica por cima do formulario.
  // ARMADILHA CARA, medida em 08/09: o banner de cookie daqui e um input[type=submit] do
  // ASP.NET, entao aceitar dispara um POSTBACK que RECARREGA a pagina e APAGA todo campo ja
  // preenchido. O sintoma final e "You must complete the following before you can proceed",
  // que parece formulario mal preenchido e e na verdade formulario limpo pelo banner.
  // Aceite PRIMEIRO, espere o recarregamento TERMINAR, confirme que o banner sumiu, e so entao preencha.
  for(let t=1;t<=3;t++){
    const e=await p.$('input[type=submit][value*="Accept" i], #onetrust-accept-btn-handler, button:has-text("Accept All")');
    if(!e){ log('banner de cookie ausente na tentativa',t); break; }
    await Promise.all([
      p.waitForLoadState('domcontentloaded').catch(()=>{}),
      e.click({timeout:10000}).catch(()=>{})
    ]);
    await p.waitForTimeout(6000);
    log('aceitei o banner de cookie, tentativa',t);
  }
  await p.waitForTimeout(2000);
  log('url:',p.url());
  await dump('cadastro');
  const set=async(suf,val)=>{ const el=await p.$(`input[name$="${suf}"], textarea[name$="${suf}"]`);
    if(!el){ log('SEM CAMPO',suf); return false; }
    await el.scrollIntoViewIfNeeded().catch(()=>{}); await el.fill(String(val)); log('fill',suf,'=>',String(val).slice(0,40)); return true; };
  for(const [suf,val] of RESP) await set(suf,val);
  // "How did you hear about us?" e obrigatorio
  const sel=await p.$('select[name$="CanC_InfluenceToApply"]');
  if(sel){
    const ops=await sel.$$eval('option',os=>os.map(o=>({v:o.value,t:(o.textContent||'').trim()})));
    log('opcoes de origem:',JSON.stringify(ops.map(o=>o.t).slice(0,14)));
    const alvo=ops.find(o=>/other|website|search|internet|google/i.test(o.t)&&o.v)||ops.find(o=>o.v);
    if(alvo){ await sel.selectOption(alvo.v); log('origem =>',alvo.t); }
  }
  // ORDEM MEDIDA EM 08/09, e ela decide se o cadastro passa: os campos de email disparam um
  // AJAX (JSFunctions.asmx/CheckEmailValidation) que RE-RENDERIZA o formulario. Radio, caixa e
  // senha marcados por check({force:true}) ou fill ANTES disso somem, e o erro final vira
  // "Password is a required field" com a senha aparentemente escrita. Espere o AJAX assentar e
  // marque por CLIQUE NO ROTULO, que e o que o ASP.NET escuta.
  await p.waitForTimeout(4000);
  for(const [suf,rot] of [['CanC_IsEmployee','No'],['CanC_IsPreviousEmployee','No'],['CanC_OccasionalContact','Yes']]){
    const loc=p.locator(`input[type=radio][name$="${suf}"]`);
    const n=await loc.count(); let ok=false;
    for(let i=0;i<n;i++){
      const id=await loc.nth(i).getAttribute('id');
      let lab=''; if(id) lab=await p.locator(`label[for="${id}"]`).first().innerText().catch(()=>'');
      if(!lab) lab=(i===0?'Yes':'No');
      if(lab.trim().toLowerCase()===rot.toLowerCase()){
        if(id) await p.locator(`label[for="${id}"]`).first().click({timeout:8000}).catch(async()=>{await loc.nth(i).check({force:true});});
        else await loc.nth(i).check({force:true});
        ok=await loc.nth(i).isChecked().catch(()=>false); break;
      }
    }
    log('radio',suf,'=>',rot,ok?'MARCADO':'NAO CASOU');
    await p.waitForTimeout(600);
  }
  const cbs=await p.$$('input[type=checkbox]');
  let marcadas=0;
  for(const c of cbs){
    const nm=(await c.getAttribute('name'))||'';
    if(!/Consent|Declaration/i.test(nm)) continue;
    const id=await c.getAttribute('id');
    if(id) await p.locator(`label[for="${id}"]`).first().click({timeout:8000}).catch(async()=>{await c.check({force:true});});
    else await c.check({force:true});
    if(await c.isChecked().catch(()=>false)) marcadas++;
    await p.waitForTimeout(500);
  }
  log('caixas de consentimento marcadas:',marcadas);
  // a SENHA vai por ultimo, e por digitacao e nao por fill
  let sen=await p.$('input[type=password][name*="RegistrationHolder"], input[type=password][name*="Registration"]');
  if(!sen){
    const nomes=await p.evaluate(()=>[...document.querySelectorAll('input[type=password]')].map(e=>e.name||e.id||''));
    for(const n of nomes){ if(!/Login|sidebar/i.test(n)){ sen=await p.$(`input[type=password][name="${n}"]`); break; } }
  }
  if(sen){ await sen.scrollIntoViewIfNeeded().catch(()=>{}); await sen.click({timeout:8000}).catch(()=>{});
    await p.keyboard.type(SENHA,{delay:35});
    const tam=await sen.evaluate(e=>e.value.length);
    log('senha digitada no campo do cadastro, caracteres:',tam); }
  else log('NAO ACHEI o campo de senha do cadastro');
  await p.waitForTimeout(1200);
  await dump('preenchido');
  await p.screenshot({path:D+'bz_'+slug+'.png',fullPage:true});
  const cap=await p.evaluate(()=>({fr:[...document.querySelectorAll('iframe')].map(f=>f.src||'').filter(x=>/captcha|challenges|turnstile/i.test(x)),w:document.querySelectorAll('.g-recaptcha,[data-sitekey],.h-captcha,.cf-turnstile').length}));
  log('captcha no HTML (sem veredito):',JSON.stringify(cap));
  if(!SUBMIT){ log('MODO SECO — nada enviado'); await b.close(); return; }
  p.on('response',async r=>{ if(r.request().method()==='POST'&&!/analytics|collect|gtm/i.test(r.url())) log('  RES',r.status(),r.url().split('?')[0]); });
  const bt=await p.$('input[name$="btnSubmit"], input[type=submit][value*="Register" i], button:has-text("Register")');
  if(!bt){ log('NAO ACHEI o botao de cadastro'); await b.close(); return; }
  await bt.scrollIntoViewIfNeeded().catch(()=>{});
  await bt.click({timeout:25000}).catch(e=>log('cadastro',e.message.split('\n')[0]));
  await p.waitForTimeout(9000);
  // ARMADILHA: este cadastro REVELA obrigatorios novos so depois da primeira tentativa
  // (Have you previously worked for us, Preferred Specialism, Preferred Location). Uma
  // passada so nunca fecha. Preencha o que apareceu e tente de novo.
  for(let volta=1; volta<=3; volta++){
    const falta=await p.evaluate(()=>{
      const t=document.body.innerText||'';
      const m=t.match(/You must complete the following before you can proceed:([\s\S]{0,600})/);
      return m?m[1].replace(/\s+/g,' ').trim().slice(0,400):'';
    });
    if(!falta){ log('sem lista de pendencias na volta',volta); break; }
    log('volta',volta,'| ainda falta:',falta);
    // selects obrigatorios vazios: escolhe a primeira opcao com valor
    const sels=await p.$$('select');
    for(const sl of sels){
      const nm=(await sl.getAttribute('name'))||'';
      if(/Influence/i.test(nm)) continue;
      const v=await sl.inputValue().catch(()=>'');
      if(v) continue;
      const ops=await sl.$$eval('option',os=>os.map(o=>({v:o.value,t:(o.textContent||'').trim()})));
      const alvo=ops.find(o=>o.v&&!/please select|^--/i.test(o.t));
      if(alvo){ await sl.selectOption(alvo.v).catch(()=>{}); log('  select',nm.split('$').pop(),'=>',alvo.t); await p.waitForTimeout(500); }
    }
    // radios obrigatorios ainda sem marca: marca No, que e a resposta verdadeira nas duas
    const grupos=await p.evaluate(()=>[...new Set([...document.querySelectorAll('input[type=radio]')].filter(e=>e.offsetParent!==null).map(e=>e.name))]);
    for(const g of grupos){
      const marcado=await p.evaluate(n=>!!document.querySelector(`input[type=radio][name="${n}"]:checked`),g);
      if(marcado) continue;
      const loc=p.locator(`input[type=radio][name="${g}"]`);
      const n=await loc.count();
      for(let i=0;i<n;i++){
        const id=await loc.nth(i).getAttribute('id');
        let lab=''; if(id) lab=await p.locator(`label[for="${id}"]`).first().innerText().catch(()=>'');
        if((lab||'').trim().toLowerCase()==='no'){
          if(id) await p.locator(`label[for="${id}"]`).first().click({timeout:8000}).catch(()=>{});
          log('  radio',g.split('$').pop(),'=> No'); break;
        }
      }
      await p.waitForTimeout(400);
    }
    const bt2=await p.$('input[name$="btnSubmit"]');
    if(!bt2) break;
    await bt2.scrollIntoViewIfNeeded().catch(()=>{});
    await bt2.click({timeout:25000}).catch(e=>log('  resubmit',e.message.split('\n')[0]));
    await p.waitForTimeout(9000);
  }
  log('url depois:',p.url());
  log('texto:',(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ').slice(0,500));
  await dump('depois do cadastro');
  await p.screenshot({path:D+'bz_'+slug+'_depois.png',fullPage:true});
 }catch(e){ log('ERR',e.message.split('\n')[0]); await p.screenshot({path:D+'bz_'+slug+'_err.png',fullPage:true}).catch(()=>{}); }
 await b.close();
})();
