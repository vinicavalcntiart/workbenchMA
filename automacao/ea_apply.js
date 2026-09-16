// UMA tentativa de envio na EA 215788 (Senior Character Artist, EA Sports FC Vancouver).
// Entra pelo LOGIN da conta, abre ApplicationGeneralInformation, preenche SO o que esta
// vazio e VISIVEL, le de volta, e clica em Next. Se vier Internal server error, registra.
const {chromium}=require('playwright'); const fs=require('fs');
const C=JSON.parse(fs.readFileSync('/home/user/apply/cred.json')).ea;
const JOB='215788'; const SUBMIT=process.argv.includes('ENVIAR');
const log=(...a)=>console.log('[ea]',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:process.env.APPLY_PROXY||process.env.HTTPS_PROXY},
   args:['--no-sandbox','--ignore-certificate-errors','--disable-blink-features=AutomationControlled']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1366,height:1100},
   userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',locale:'en-US'});
 await ctx.addInitScript(()=>{Object.defineProperty(navigator,'webdriver',{get:()=>undefined});});
 const p=await ctx.newPage();
 p.on('response',r=>{ if(r.request().method()==='POST') log('[rede]',r.status(),r.url().slice(0,110)); });
 try{
  await p.goto('https://jobs.ea.com/en_US/careers/Login',{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(6000);
  for(const t of ['Accept','Accept All Cookies','Accept all','Agree','Got it','OK']){ const e=await p.$(`button:has-text("${t}")`); if(e&&await e.isVisible().catch(()=>0)){ await e.click().catch(()=>{}); await p.waitForTimeout(1500); break; } }
  let ok=false;
  for(let i=0;i<4 && !ok;i++){
    if(await p.$('#username')){ ok=true; break; }
    log('tela de login ainda sem #username, recarregando', i);
    await p.reload({timeout:120000,waitUntil:'domcontentloaded'}).catch(()=>{});
    await p.waitForTimeout(7000);
  }
  if(!ok){ log('SEM #username depois de 4 tentativas | titulo:',await p.title()); await b.close(); return; }
  await p.fill('#username',C.email); await p.fill('#password',C.senha);
  await p.keyboard.press('Enter'); await p.waitForTimeout(9000);
  if(!/Profile|careers/i.test(p.url())){ log('login nao concluiu | url:',p.url()); await b.close(); return; }
  await p.goto(`https://jobs.ea.com/en_US/careers/ApplicationGeneralInformation?jobId=${JOB}`,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(9000);
  // id que comeca com digito NAO entra em seletor CSS: sempre [id="..."]
  const sel=id=>`[id="${id}"]`;
  // 1) os tres selects obrigatorios vazios
  const escolhas=[['7836','EA Careers Website'],['17623','More Than 3 Years'],['17624','No']];
  for(const [id,rot] of escolhas){
    const el=await p.$(sel(id)); if(!el){ log('campo ausente',id); continue; }
    await el.selectOption({label:rot}).catch(async()=>{ await el.selectOption({label:rot.trim()}).catch(e=>log('falhou select',id,e.message.split('\n')[0])); });
    log('select',id,'=>',rot);
  }
  // 2) caixas obrigatorias VISIVEIS de consentimento
  const marcadas=await p.evaluate(()=>{
    const out=[];
    for(const c of document.querySelectorAll('input[type=checkbox]')){
      if(!c.required) continue;
      if(c.offsetParent===null) { out.push([c.id,'ESCONDIDA, nao marquei']); continue; }
      let l=''; if(c.id){const x=document.querySelector(`label[for="${CSS.escape(c.id)}"]`); if(x)l=x.innerText.trim();}
      if(!/agree|consent|acknowledg|accept/i.test(l)) { out.push([c.id,'rotulo nao e de consentimento: '+l.slice(0,50)]); continue; }
      if(!c.checked){ c.click(); }
      out.push([c.id, c.checked?'MARCADA':'NAO MARCOU']);
    }
    return out;
  });
  log('caixas obrigatorias:',JSON.stringify(marcadas));
  // 3) leitura de volta de TODO obrigatorio visivel
  const faltando=await p.evaluate(()=>{
    const out=[];
    for(const e of document.querySelectorAll('input,select,textarea')){
      if(e.type==='hidden'||!e.required) continue;
      if(e.offsetParent===null) continue;
      let l=''; if(e.id){const x=document.querySelector(`label[for="${CSS.escape(e.id)}"]`); if(x)l=x.innerText.trim();}
      const vazio=(e.type==='checkbox'||e.type==='radio')? !e.checked : !(e.value||'').trim();
      if(vazio) out.push([e.id,(l||'(sem rotulo)').replace(/\s+/g,' ').slice(0,70)]);
    }
    return out;
  });
  log('OBRIGATORIOS VISIVEIS AINDA VAZIOS:',JSON.stringify(faltando));
  // confere que a pergunta de patrocinio, se existir, esta com a VERDADE
  const patroc=await p.evaluate(()=>{
    const out=[];
    for(const e of document.querySelectorAll('input,select')){
      let l=''; if(e.id){const x=document.querySelector(`label[for="${CSS.escape(e.id)}"]`); if(x)l=x.innerText.trim();}
      const cont=e.closest('div'); const ctx=cont?(cont.innerText||'').slice(0,160):'';
      if(/sponsor|immigration|work authoriz|legally authorized|right to work/i.test(l+' '+ctx)) out.push([e.id,e.type,(l||ctx).replace(/\s+/g,' ').slice(0,110),e.type==='radio'||e.type==='checkbox'?e.checked:e.value]);
    }
    return out;
  });
  log('CAMPOS DE AUTORIZACAO/PATROCINIO encontrados:',JSON.stringify(patroc).slice(0,900));
  await p.screenshot({path:'ea_pre.png',fullPage:true});
  if(!SUBMIT){ log('MODO SECO, nao cliquei em Next'); await b.close(); return; }
  const next=await p.$('button:has-text("Next"), input[value="Next"], a:has-text("Next"), [id$="-save"]');
  if(!next){ log('botao Next NAO achado'); await b.close(); return; }
  await next.scrollIntoViewIfNeeded().catch(()=>{});
  await next.click().catch(async e=>{ log('clique falhou',e.message.split('\n')[0]); await next.click({force:true}).catch(()=>{}); });
  await p.waitForTimeout(15000);
  log('DEPOIS DO NEXT | url:',p.url().slice(0,160));
  const t=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
  log('TEXTO (900):',t.slice(0,900));
  await p.screenshot({path:'ea_pos.png',fullPage:true});
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await b.close();
})();
