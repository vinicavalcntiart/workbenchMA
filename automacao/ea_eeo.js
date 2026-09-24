// EA (Avature) - o passo EEO/NDA, que e onde a ApplicationGeneralInformation para.
// MEDIDO em 19/09 as 17h05 na 216159: o Next da tela EEO nao clica (timeout de 30s) porque
// existe UM obrigatorio vazio, o campo 17505, cujo rotulo e so "*" - a leitura por
// label[for] nao diz o que ele e. Este script DUMPA a tela inteira antes de tocar em nada.
// Uso: sh hb_run.sh ea_eeo.js <jobId> [ENVIAR]
const {chromium}=require('playwright'); const {abrirLocal,abrirPerfil}=require('./navegador'); const fs=require('fs');
const C=JSON.parse(fs.readFileSync('/home/user/apply/cred.json')).ea;
const JOB=process.argv[2]; const SUBMIT=process.argv.includes('ENVIAR');
const log=(...a)=>console.log('[eeo'+JOB+']',...a);
(async()=>{
 const b=await abrirLocal({headless:false,args:['--disable-blink-features=AutomationControlled']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1366,height:1200},
   userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',locale:'en-US'});
 await ctx.addInitScript(()=>{Object.defineProperty(navigator,'webdriver',{get:()=>undefined});});
 const p=await ctx.newPage();
 p.on('response',r=>{ if(r.request().method()==='POST') log('[rede]',r.status(),r.url().slice(0,120)); });
 try{
  await p.goto('https://jobs.ea.com/en_US/careers/Login',{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(6000);
  for(let i=0;i<4;i++){ if(await p.$('#username')) break; await p.reload({waitUntil:'domcontentloaded'}).catch(()=>{}); await p.waitForTimeout(6000); }
  await p.fill('#username',C.email); await p.fill('#password',C.senha);
  await p.keyboard.press('Enter'); await p.waitForTimeout(10000);
  log('pos-login:',p.url().slice(0,120));
  await p.goto(`https://jobs.ea.com/en_US/careers/ApplicationEEO?jobId=${JOB}`,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(9000);
  log('url:',p.url().slice(0,150));
  const campos=await p.evaluate(()=>[...document.querySelectorAll('input,select,textarea,button')].map(e=>{
    let l='';
    if(e.id){const x=document.querySelector(`label[for="${CSS.escape(e.id)}"]`); if(x)l=x.innerText.trim();}
    if(!l&&e.closest('label'))l=e.closest('label').innerText.trim();
    if(!l&&e.getAttribute('aria-label'))l='(aria)'+e.getAttribute('aria-label');
    const cont=e.closest('.FieldContainer,.field,fieldset,div');
    const ctxt=cont?(cont.innerText||'').replace(/\s+/g,' ').slice(0,200):'';
    const o=e.tagName==='SELECT'?[...e.options].map(x=>x.text.trim()).slice(0,25):undefined;
    return {tag:e.tagName,type:e.type,id:e.id,name:e.name,req:e.required,vis:e.offsetParent!==null,
            val:(e.value||'').slice(0,50),checked:e.checked,label:(l||'').replace(/\s+/g,' ').slice(0,80),
            ctx:ctxt,opts:o};
  }).filter(x=>x.type!=='hidden'&&x.vis));
  log('CAMPOS VISIVEIS:',campos.length);
  for(const c of campos) log('   ',JSON.stringify(c));
  await p.screenshot({path:`ea_${JOB}_eeo.png`,fullPage:true});
  if(!SUBMIT){ log('MODO SECO'); await b.close(); return; }
  // O 17505 e a ASSINATURA do NDA de entrevista (texto livre com o nome).
  const as=await p.$('[id="17505"]');
  if(as){
    const tp=await as.evaluate(e=>e.type);
    if(tp==='checkbox'||tp==='radio'){ await as.check().catch(e=>log('check falhou',e.message.split('\n')[0])); }
    else { await as.fill('Vini Cavalcanti').catch(e=>log('fill falhou',e.message.split('\n')[0])); }
    log('17505 tipo',tp,'preenchido');
  } else log('17505 NAO achado');
  // EEO: as perguntas de genero/etnia/veterano/deficiencia sao VOLUNTARIAS. Marco
  // "decline to self-identify" onde existir, e nunca invento dado demografico.
  const decl=await p.evaluate(()=>{
    const out=[];
    for(const s of document.querySelectorAll('select')){
      if(s.value) continue;
      const op=[...s.options].find(o=>/decline|do not wish|prefer not|i don't wish/i.test(o.text));
      if(op){ s.value=op.value; s.dispatchEvent(new Event('change',{bubbles:true})); out.push([s.id,op.text.trim()]); }
    }
    return out;
  });
  log('EEO declinados:',JSON.stringify(decl));
  for(let passo=1;passo<=5;passo++){
    const faltando=await p.evaluate(()=>{
      const out=[];
      for(const e of document.querySelectorAll('input,select,textarea')){
        if(e.type==='hidden'||!e.required||e.offsetParent===null) continue;
        const vazio=(e.type==='checkbox'||e.type==='radio')? !e.checked : !(e.value||'').trim();
        if(vazio) out.push(e.id);
      }
      return out;
    });
    log('passo',passo,'obrigatorios vazios:',JSON.stringify(faltando));
    // O botao de avancar do Avature tem innerText VAZIO: o rotulo "Next" mora no
    // container pai. Casar por texto do proprio elemento nao acha nada, e foi isso que
    // fez o laco anterior clicar em coisa errada por seis passos. O que acha e o id
    // terminado em "-goto" com type=submit.
    const clicou=await p.evaluate(()=>{
      let c=[...document.querySelectorAll('button[type=submit],input[type=submit]')]
        .filter(x=>x.offsetParent!==null)
        .find(x=>/-goto$/.test(x.id||''));
      if(!c) c=[...document.querySelectorAll('button,input[type=submit],input[type=button],a')]
        .filter(x=>x.offsetParent!==null)
        .find(x=>/^(next|submit|submit application|finish|continue)$/i.test(((x.innerText||x.value||'').trim())));
      if(!c) return null; c.click(); return (c.id||c.innerText||c.value||'').trim();
    });
    if(!clicou){ log('sem botao clicavel no passo',passo); break; }
    log('cliquei',clicou);
    await p.waitForTimeout(15000);
    const tt=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
    log('url:',p.url().slice(0,160));
    log('texto (1000):',tt.slice(0,1000));
    await p.screenshot({path:`ea_${JOB}_s${passo}.png`,fullPage:true});
    if(/thank(s| you) for applying|application (has been )?(submitted|received)|we will take it from here/i.test(tt)){ log('>>> CONFIRMACAO NA TELA'); break; }
    if(/internal server error/i.test(tt)){ log('>>> INTERNAL SERVER ERROR'); break; }
  }
  // prova na propria conta
  await p.goto('https://jobs.ea.com/en_US/careers/Profile',{timeout:120000,waitUntil:'domcontentloaded'}).catch(()=>{});
  await p.waitForTimeout(6000);
  const lk=await p.$('a:has-text("Job Applications")');
  if(lk){ await lk.click().catch(()=>{}); await p.waitForTimeout(9000); }
  const fin=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
  log('JOB APPLICATIONS DA CONTA (2500):',fin.slice(0,2500));
  log('ID NA LISTA?',fin.includes(JOB)?'SIM':'NAO');
  await p.screenshot({path:`ea_${JOB}_conta.png`,fullPage:true});
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await b.close();
})();
