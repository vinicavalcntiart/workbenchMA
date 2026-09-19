// EA (Avature, jobs.ea.com) - candidatura em UMA vaga, id por argumento.
// Nasceu em 19/09 as 16h45 do ea_apply.js, que tinha o 215788 cravado no codigo.
// FLUXO MEDIDO: Login -> MyApplications (dedupe da fonte do candidato) -> ApplicationMethods?jobId=
// -> ApplicationGeneralInformation?jobId= -> Next -> (proximos passos, se houver).
// Uso: sh hb_run.sh ea_job.js <jobId> [ENVIAR]
const {chromium}=require('playwright'); const fs=require('fs');
const C=JSON.parse(fs.readFileSync('/home/user/apply/cred.json')).ea;
const JOB=process.argv[2]; const SUBMIT=process.argv.includes('ENVIAR');
if(!JOB){ console.log('falta o jobId'); process.exit(1); }
const log=(...a)=>console.log('[ea'+JOB+']',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:process.env.APPLY_PROXY||process.env.HTTPS_PROXY},
   args:['--no-sandbox','--ignore-certificate-errors','--disable-blink-features=AutomationControlled']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1366,height:1100},
   userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',locale:'en-US'});
 await ctx.addInitScript(()=>{Object.defineProperty(navigator,'webdriver',{get:()=>undefined});});
 const p=await ctx.newPage();
 p.on('response',r=>{ if(r.request().method()==='POST') log('[rede]',r.status(),r.url().slice(0,120)); });
 const dump=async(tag)=>{
   const campos=await p.evaluate(()=>[...document.querySelectorAll('input,select,textarea')].map(e=>{
     let l='';
     if(e.id){const x=document.querySelector(`label[for="${CSS.escape(e.id)}"]`); if(x)l=x.innerText.trim();}
     if(!l&&e.closest('label'))l=e.closest('label').innerText.trim();
     if(!l&&e.getAttribute('aria-label'))l='(aria)'+e.getAttribute('aria-label');
     const cont=e.closest('.FieldContainer,.field,div');
     if(!l&&cont)l=(cont.innerText||'').split('\n')[0];
     const o=e.tagName==='SELECT'?[...e.options].map(x=>x.text.trim()).slice(0,20):undefined;
     return {type:e.type,id:e.id,req:e.required,vis:e.offsetParent!==null,val:(e.value||'').slice(0,40),
             label:(l||'').replace(/\s+/g,' ').slice(0,90),opts:o};
   }).filter(x=>x.type!=='hidden'&&x.vis));
   log(tag,'CAMPOS VISIVEIS:',campos.length);
   for(const c of campos) log('   ',JSON.stringify(c));
   // porteiro: iframe de captcha que de fato carregou
   const ifr=await p.evaluate(()=>[...document.querySelectorAll('iframe')].map(f=>f.src).filter(s=>/captcha|recaptcha|hcaptcha|turnstile/i.test(s)));
   log(tag,'IFRAMES DE CAPTCHA:',JSON.stringify(ifr));
 };
 try{
  await p.goto('https://jobs.ea.com/en_US/careers/Login',{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(6000);
  for(const t of ['Accept','Accept All Cookies','Accept all','Agree','Got it','OK']){ const e=await p.$(`button:has-text("${t}")`); if(e&&await e.isVisible().catch(()=>0)){ await e.click().catch(()=>{}); await p.waitForTimeout(1500); break; } }
  let ok=false;
  for(let i=0;i<4 && !ok;i++){
    if(await p.$('#username')){ ok=true; break; }
    log('login sem #username, recarregando',i);
    await p.reload({timeout:120000,waitUntil:'domcontentloaded'}).catch(()=>{});
    await p.waitForTimeout(7000);
  }
  if(!ok){ log('SEM #username depois de 4 tentativas | titulo:',await p.title()); await b.close(); return; }
  await p.fill('#username',C.email); await p.fill('#password',C.senha);
  await p.keyboard.press('Enter'); await p.waitForTimeout(10000);
  log('pos-login url:',p.url().slice(0,140));
  if(!/Profile|careers/i.test(p.url())){ log('login nao concluiu'); await b.close(); return; }

  // DEDUPE DA FONTE DO CANDIDATO: a propria lista de candidaturas da conta
  await p.goto('https://jobs.ea.com/en_US/careers/MyApplications',{timeout:120000,waitUntil:'domcontentloaded'}).catch(()=>{});
  await p.waitForTimeout(7000);
  let t=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
  log('MINHAS CANDIDATURAS (2000):',t.slice(0,2000));
  if(t.includes(JOB)){ log('!! O ID',JOB,'APARECE NA LISTA DA PROPRIA CONTA - PARO AQUI, e duplicata'); await b.close(); return; }
  log('dedupe da conta: o id',JOB,'NAO aparece na lista de candidaturas');

  await p.goto(`https://jobs.ea.com/en_US/careers/ApplicationMethods?jobId=${JOB}`,{timeout:120000,waitUntil:'domcontentloaded'}).catch(e=>log('goto methods',e.message.split('\n')[0]));
  await p.waitForTimeout(8000);
  log('ApplicationMethods url:',p.url().slice(0,150));
  log('texto (800):',(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ').slice(0,800));
  await p.screenshot({path:`ea_${JOB}_methods.png`,fullPage:true});
  // o metodo "Apply with your profile" / "Use my profile" e o que reaproveita o CV da conta
  for(const rot of ['Apply with my profile','Use my profile','Apply Manually','Apply manually','Continue','Next']){
    const e=await p.$(`button:has-text("${rot}"), a:has-text("${rot}"), input[value="${rot}"]`);
    if(e&&await e.isVisible().catch(()=>0)){ log('clico no metodo:',rot); await e.click().catch(()=>{}); await p.waitForTimeout(9000); break; }
  }
  log('depois do metodo url:',p.url().slice(0,150));

  await p.goto(`https://jobs.ea.com/en_US/careers/ApplicationGeneralInformation?jobId=${JOB}`,{timeout:120000,waitUntil:'domcontentloaded'}).catch(e=>log('goto gi',e.message.split('\n')[0]));
  await p.waitForTimeout(9000);
  log('GeneralInformation url:',p.url().slice(0,150));
  log('texto (900):',(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ').slice(0,900));
  await dump('GI');
  await p.screenshot({path:`ea_${JOB}_gi.png`,fullPage:true});
  if(!SUBMIT){ log('MODO SECO, nao cliquei em Next'); await b.close(); return; }

  // ---- ENVIO ----
  const escolhas=[['7836','EA Careers Website'],['17623','More Than 3 Years'],['17624','No']];
  for(const [id,rot] of escolhas){
    const el=await p.$(`[id="${id}"]`); if(!el){ log('campo ausente',id); continue; }
    await el.selectOption({label:rot}).catch(e=>log('falhou select',id,e.message.split('\n')[0]));
    log('select',id,'=>',rot);
  }
  // Portfolio: o campo 22156 pede arquivo e o PDF de portfolio da campanha existe.
  // NAO anexo carta: o Vini_Cavalcanti_Cover_Letter.pdf e generico e nao da para ler o
  // texto dele nesta maquina (PDF de fonte embutida), entao anexar seria as cegas.
  const pf=await p.$('[id="22156"]');
  if(pf){ await pf.setInputFiles('/home/user/apply/Vini_Cavalcanti_Portfolio.pdf').then(()=>log('portfolio anexado')).catch(e=>log('anexo falhou',e.message.split('\n')[0])); await p.waitForTimeout(6000); }
  const marcadas=await p.evaluate(()=>{
    const out=[];
    for(const c of document.querySelectorAll('input[type=checkbox]')){
      if(!c.required||c.offsetParent===null) continue;
      let l=''; if(c.id){const x=document.querySelector(`label[for="${CSS.escape(c.id)}"]`); if(x)l=x.innerText.trim();}
      if(!/agree|consent|acknowledg|accept/i.test(l)){ out.push([c.id,'rotulo nao e consentimento: '+l.slice(0,50)]); continue; }
      if(!c.checked) c.click();
      out.push([c.id,c.checked?'MARCADA':'NAO MARCOU']);
    }
    return out;
  });
  log('caixas obrigatorias:',JSON.stringify(marcadas));
  for(let passo=1; passo<=6; passo++){
    const faltando=await p.evaluate(()=>{
      const out=[];
      for(const e of document.querySelectorAll('input,select,textarea')){
        if(e.type==='hidden'||!e.required||e.offsetParent===null) continue;
        let l=''; if(e.id){const x=document.querySelector(`label[for="${CSS.escape(e.id)}"]`); if(x)l=x.innerText.trim();}
        const vazio=(e.type==='checkbox'||e.type==='radio')? !e.checked : !(e.value||'').trim();
        if(vazio) out.push([e.id,(l||'(sem rotulo)').replace(/\s+/g,' ').slice(0,70)]);
      }
      return out;
    });
    log('passo',passo,'OBRIGATORIOS VAZIOS:',JSON.stringify(faltando));
    const next=await p.$('button:has-text("Submit"), input[value="Submit"], button:has-text("Next"), input[value="Next"], a:has-text("Next")');
    if(!next){ log('sem botao Next/Submit no passo',passo); break; }
    const rot=(await next.innerText().catch(()=>''))||(await next.getAttribute('value').catch(()=>''))||'?';
    await next.scrollIntoViewIfNeeded().catch(()=>{});
    await next.click().catch(async e=>{ log('clique falhou',e.message.split('\n')[0]); await next.click({force:true}).catch(()=>{}); });
    await p.waitForTimeout(15000);
    log('passo',passo,'clicado',rot.trim(),'| url:',p.url().slice(0,160));
    const tt=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
    log('passo',passo,'TEXTO (1200):',tt.slice(0,1200));
    await p.screenshot({path:`ea_${JOB}_p${passo}.png`,fullPage:true});
    if(/thank you|application (has been )?(submitted|received)|successfully (submitted|applied)/i.test(tt)){ log('>>> CONFIRMACAO NA TELA'); break; }
    if(/internal server error/i.test(tt)){ log('>>> INTERNAL SERVER ERROR do Avature'); break; }
  }
  // prova pela propria conta
  await p.goto('https://jobs.ea.com/en_US/careers/MyApplications',{timeout:120000,waitUntil:'domcontentloaded'}).catch(()=>{});
  await p.waitForTimeout(8000);
  const fin=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
  log('LISTA DA CONTA DEPOIS (2000):',fin.slice(0,2000));
  log('ID NA LISTA DEPOIS?',fin.includes(JOB)?'SIM':'NAO');
  await p.screenshot({path:`ea_${JOB}_apps.png`,fullPage:true});
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await b.close();
})();
