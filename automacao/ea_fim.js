// EA (Avature) - o ULTIMO passo da candidatura, o que tem a pergunta de PATROCINIO.
// MEDIDO em 19/09 as 17h20 na 216159. A tela final do wizard EEO pede tres coisas:
//   3679-2  "Do you now or in the future require immigration sponsorship to work in the
//            country you are applying to?"  -> a VERDADE e YES (ele nao tem autorizacao no Canada)
//   3679-3  "Are you currently subject to any type of restriction that could prevent you
//            from working for EA..."        -> NO
//   3684    "I certify that all information on this application is true and complete."
// O botao e 2680-save (rotulo "Submit"). Dois avisos medidos:
//  - o innerText do botao do Avature e VAZIO; case por id terminado em -save/-goto/-next.
//  - um 502 "upstream request failed" apareceu numa tentativa e NAO e recusa: a lista de
//    candidaturas da conta continuou com "Finish your application", ou seja nada foi enviado.
// Uso: sh hb_run.sh ea_fim.js <jobId> [ENVIAR]
const {chromium}=require('playwright'); const {abrirLocal,abrirPerfil}=require('./navegador'); const fs=require('fs');
const C=JSON.parse(fs.readFileSync('/home/user/apply/cred.json')).ea;
const JOB=process.argv[2]; const SUBMIT=process.argv.includes('ENVIAR');
const log=(...a)=>console.log('[fim'+JOB+']',...a);
const dump=async(p,tag)=>{
  const campos=await p.evaluate(()=>[...document.querySelectorAll('input,select,textarea,button')].map(e=>{
    let l='';
    if(e.id){const x=document.querySelector(`label[for="${CSS.escape(e.id)}"]`); if(x)l=x.innerText.trim();}
    if(!l&&e.closest('label'))l=e.closest('label').innerText.trim();
    const cont=e.closest('.FieldContainer,.field,fieldset,div');
    const ctxt=cont?(cont.innerText||'').replace(/\s+/g,' ').slice(0,180):'';
    const o=e.tagName==='SELECT'?[...e.options].map(x=>x.text.trim()):undefined;
    return {tag:e.tagName,type:e.type,id:e.id,req:e.required,vis:e.offsetParent!==null,
            val:(e.value||'').slice(0,40),checked:e.checked,label:(l||'').replace(/\s+/g,' ').slice(0,90),ctx:ctxt,opts:o};
  }).filter(x=>x.type!=='hidden'&&x.vis));
  log(tag,'CAMPOS:',campos.length); for(const c of campos) log('   ',JSON.stringify(c));
};
(async()=>{
 const b=await abrirLocal({headless:false,args:['--disable-blink-features=AutomationControlled']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1366,height:1200},
   userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',locale:'en-US'});
 await ctx.addInitScript(()=>{Object.defineProperty(navigator,'webdriver',{get:()=>undefined});});
 const p=await ctx.newPage();
 p.on('response',r=>{ if(r.request().method()==='POST') log('[rede]',r.status(),r.url().slice(0,110)); });
 try{
  await p.goto('https://jobs.ea.com/en_US/careers/Login',{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(6000);
  for(let i=0;i<4;i++){ if(await p.$('#username')) break; await p.reload({waitUntil:'domcontentloaded'}).catch(()=>{}); await p.waitForTimeout(6000); }
  await p.fill('#username',C.email); await p.fill('#password',C.senha);
  await p.keyboard.press('Enter'); await p.waitForTimeout(10000);
  log('pos-login:',p.url().slice(0,120));
  // Retoma pelo link "Finish your application" da lista da conta, que e a rota que o
  // proprio Avature oferece; o goto direto no ApplicationEEO reabre o wizard no passo 1.
  await p.goto('https://jobs.ea.com/en_US/careers/Profile',{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(6000);
  const lk=await p.$('a:has-text("Job Applications")');
  if(lk){ await lk.click().catch(()=>{}); await p.waitForTimeout(9000); }
  log('lista:',(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ').slice(0,1500));
  const fin=await p.$(`tr:has-text("${JOB}") a:has-text("Finish")`);
  if(fin){ log('clico em Finish your application'); await fin.click().catch(()=>{}); await p.waitForTimeout(10000); }
  else { log('sem link Finish; vou direto no ApplicationEEO'); await p.goto(`https://jobs.ea.com/en_US/careers/ApplicationEEO?jobId=${JOB}`,{timeout:120000,waitUntil:'domcontentloaded'}); await p.waitForTimeout(9000); }
  log('url:',p.url().slice(0,150));
  let t=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
  log('texto (900):',t.slice(0,900));
  // anda o wizard ate a tela que pede patrocinio
  for(let i=0;i<5 && !/immigration sponsorship/i.test(t); i++){
    // preenche o que este passo pede antes de avancar
    await p.evaluate(()=>{
      const c=document.querySelector('[id="17505"]'); if(c&&!c.checked) c.click();
      for(const s of document.querySelectorAll('select')){
        if(s.value) continue;
        const op=[...s.options].find(o=>/choose not to disclose|decline|prefer not|do not wish/i.test(o.text));
        if(op){ s.value=op.value; s.dispatchEvent(new Event('change',{bubbles:true})); }
      }
    });
    const cl=await p.evaluate(()=>{
      const c=[...document.querySelectorAll('button[type=submit],input[type=submit]')].filter(x=>x.offsetParent!==null)
        .find(x=>/-(goto|next|save)$/.test(x.id||''));
      if(!c) return null; c.click(); return c.id;
    });
    if(!cl) break;
    log('avancei por',cl); await p.waitForTimeout(12000);
    t=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
    log('  texto (400):',t.slice(0,400));
  }
  await dump(p,'FINAL');
  await p.screenshot({path:`ea_${JOB}_final.png`,fullPage:true});
  if(!SUBMIT){ log('MODO SECO, nao respondi nem enviei'); await b.close(); return; }
  if(!/immigration sponsorship/i.test(t)){ log('NAO cheguei na tela de patrocinio; paro sem enviar'); await b.close(); return; }
  // ---- AS RESPOSTAS, e as duas primeiras sao a VERDADE sobre visto ----
  const resp=await p.evaluate(()=>{
    const out=[];
    const porTexto=(re,alvo)=>{
      for(const s of document.querySelectorAll('select')){
        if(s.offsetParent===null) continue;
        const cont=s.closest('div,fieldset'); const ctx=cont?(cont.innerText||''):'';
        if(!re.test(ctx)) continue;
        const op=[...s.options].find(o=>o.text.trim().toLowerCase()===alvo.toLowerCase());
        if(op){ s.value=op.value; s.dispatchEvent(new Event('change',{bubbles:true})); out.push([s.id,ctx.replace(/\s+/g,' ').slice(0,70),op.text.trim()]); }
        return;
      }
    };
    porTexto(/immigration sponsorship/i,'Yes');
    porTexto(/subject to any type of restriction/i,'No');
    for(const c of document.querySelectorAll('input[type=checkbox]')){
      if(c.offsetParent===null) continue;
      const cont=c.closest('div,label'); const ctx=cont?(cont.innerText||''):'';
      if(/certify/i.test(ctx)&&!c.checked){ c.click(); out.push([c.id,'certify',c.checked]); }
    }
    return out;
  });
  log('RESPOSTAS DADAS:',JSON.stringify(resp));
  const faltando=await p.evaluate(()=>[...document.querySelectorAll('input,select,textarea')]
    .filter(e=>e.type!=='hidden'&&e.required&&e.offsetParent!==null)
    .filter(e=>(e.type==='checkbox'||e.type==='radio')? !e.checked : !(e.value||'').trim())
    .map(e=>e.id));
  log('OBRIGATORIOS AINDA VAZIOS:',JSON.stringify(faltando));
  if(faltando.length){ log('PARO SEM ENVIAR: ainda falta obrigatorio'); await p.screenshot({path:`ea_${JOB}_falta.png`,fullPage:true}); await b.close(); return; }
  await p.screenshot({path:`ea_${JOB}_antes_submit.png`,fullPage:true});
  const cl=await p.evaluate(()=>{
    const c=[...document.querySelectorAll('button[type=submit],input[type=submit]')].filter(x=>x.offsetParent!==null)
      .find(x=>/-(save|submit)$/.test(x.id||''));
    if(!c) return null; c.click(); return c.id;
  });
  log('SUBMIT clicado:',cl);
  await p.waitForTimeout(20000);
  const t2=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
  log('url pos-submit:',p.url().slice(0,170));
  log('TEXTO POS-SUBMIT (1500):',t2.slice(0,1500));
  await p.screenshot({path:`ea_${JOB}_pos_submit.png`,fullPage:true});
  // PROVA: a lista de candidaturas da propria conta
  await p.goto('https://jobs.ea.com/en_US/careers/Profile',{timeout:120000,waitUntil:'domcontentloaded'}).catch(()=>{});
  await p.waitForTimeout(6000);
  const lk2=await p.$('a:has-text("Job Applications")');
  if(lk2){ await lk2.click().catch(()=>{}); await p.waitForTimeout(10000); }
  const lista=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
  log('LISTA DA CONTA DEPOIS (2500):',lista.slice(0,2500));
  log('AINDA PEDE FINISH?',/Finish your application/i.test(lista.split(JOB)[1]||'')?'olhar a linha':'ver acima');
  await p.screenshot({path:`ea_${JOB}_conta_final.png`,fullPage:true});
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await b.close();
})();
