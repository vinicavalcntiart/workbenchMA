// Typeform sequencial, v2. uso: node apply_typeform2.js <passos.json> <slug> [--submit]
// CORRECAO MEDIDA EM 08/09, duas coisas que a v1 errou:
// 1) A TECLA DA LETRA NAO SELECIONA depois que o foco passa por um campo de texto: o formulario
//    trava com "Please make a selection". Clique no ROTULO da opcao ("Senior"), nao na letra.
// 2) innerText do body traz perguntas fora da tela, entao conferir a pergunta pelo body inteiro
//    da falso OK. Confira pelo bloco de pergunta VISIVEL no viewport.
const {chromium}=require('playwright'); const fs=require('fs');
const [passosFile,slug,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const S=JSON.parse(fs.readFileSync(passosFile)); const D=__dirname+'/';
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:900},locale:'en-GB'})).newPage();
 // so o que esta DENTRO da janela conta como pergunta atual
 const visivel=async()=>p.evaluate(()=>{
   const dentro=e=>{const r=e.getBoundingClientRect();return r.top>=-20&&r.bottom<=window.innerHeight+20&&r.width>0&&r.height>0;};
   return [...document.querySelectorAll('h1,h2,h3,legend,[data-qa*="question"],[class*="question"]')]
     .filter(e=>dentro(e)&&(e.innerText||'').trim().length>3)
     .map(e=>e.innerText.replace(/\s+/g,' ').trim()).join(' || ').slice(0,300);
 });
 const erroNaTela=async()=>p.evaluate(()=>/please make a selection|please fill this in|required/i.test(document.body.innerText||''));
 try{
  await p.goto(S.url,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(9000);
  const inicio=p.locator('button:has-text("Start"), button:has-text("Let\'s"), button:has-text("Begin")').first();
  if(await inicio.count()){ await inicio.click().catch(()=>{}); await p.waitForTimeout(3500); log('cliquei em comecar'); }
  for(let i=0;i<S.passos.length;i++){
    const passo=S.passos[i];
    const q=await visivel();
    if(!new RegExp(passo.espera,'i').test(q)){
      log('PAREI NO PASSO '+(i+1)+': a pergunta visivel nao casa.');
      log('  esperava:',passo.espera); log('  visivel :',q);
      await p.screenshot({path:D+'tf_'+slug+'_parou.png',fullPage:true}); await b.close(); return;
    }
    log('passo '+(i+1)+':',q.slice(0,70));
    if(passo.opcoes){
      for(const rot of passo.opcoes){
        const alvo=p.locator('label,button,[role=button],[role=radio],[role=checkbox]')
          .filter({hasText:new RegExp('^\\s*[A-Z]?\\s*'+rot.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\s*$','i')}).first();
        if(!(await alvo.count())){ log('  OPCAO NAO ACHADA:',rot); await p.screenshot({path:D+'tf_'+slug+'_semopcao.png',fullPage:true}); await b.close(); return; }
        await alvo.click({timeout:8000}).catch(e=>log('  clique',rot,e.message.split('\n')[0]));
        log('  cliquei:',rot); await p.waitForTimeout(900);
      }
    }
    if(passo.texto!==undefined){
      const inp=p.locator('input:visible, textarea:visible').first();
      if(await inp.count()){ await inp.click({timeout:8000}).catch(()=>{}); }
      await p.keyboard.type(String(passo.texto),{delay:20}); await p.waitForTimeout(700);
    }
    // avanca pelo botao OK/Next da propria pergunta, com Enter de reserva
    const ok=p.locator('button').filter({hasText:/^\s*(OK|Next|Continue)\s*$/i}).first();
    if(await ok.count()) await ok.click({timeout:8000}).catch(async()=>{await p.keyboard.press('Enter');});
    else await p.keyboard.press('Enter');
    await p.waitForTimeout(passo.espera_ms||3000);
    if(await erroNaTela()){
      log('  ERRO DE VALIDACAO depois do passo '+(i+1)+'. Parando para nao responder errado.');
      await p.screenshot({path:D+'tf_'+slug+'_erro.png',fullPage:true}); await b.close(); return;
    }
    if(passo.depoisTexto!==undefined){
      const inp2=p.locator('input:visible, textarea:visible').first();
      if(await inp2.count()) await inp2.click({timeout:8000}).catch(()=>{});
      await p.keyboard.type(String(passo.depoisTexto),{delay:20}); await p.waitForTimeout(700);
      const ok2=p.locator('button').filter({hasText:/^\s*(OK|Next|Continue)\s*$/i}).first();
      if(await ok2.count()) await ok2.click({timeout:8000}).catch(async()=>{await p.keyboard.press('Enter');});
      else await p.keyboard.press('Enter');
      await p.waitForTimeout(3000);
    }
  }
  await p.waitForTimeout(2500);
  await p.screenshot({path:D+'tf_'+slug+'_fim.png',fullPage:true});
  log('PERGUNTA VISIVEL NO FIM:',await visivel());
  const capt=await p.evaluate(()=>[...document.querySelectorAll('iframe')].map(f=>f.src||'').filter(s=>/captcha|challenges/i.test(s)));
  log('iframes de captcha:',JSON.stringify(capt));
  if(!SUBMIT){ log('MODO SECO — nao cliquei no envio final'); await b.close(); return; }
  p.on('response',async r=>{ if(r.request().method()==='POST'&&!/analytics|sentry|track/i.test(r.url())) log('  RES',r.status(),r.url().slice(0,110)); });
  const env=p.locator('button').filter({hasText:/^\s*(Submit|Send|Done)\s*$/i}).first();
  if(await env.count()){ await env.click().catch(e=>log('envio',e.message.split('\n')[0])); log('cliquei no envio'); }
  else { await p.keyboard.press('Enter'); log('sem botao de envio, mandei Enter'); }
  for(let i=0;i<10;i++){ await p.waitForTimeout(5000);
    const t=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
    if(/thanks|thank you|received|all set|submitted/i.test(t)){ log('CONFIRMACAO em t+'+((i+1)*5)+'s:',t.slice(0,300)); break; } }
  log('TELA APOS ENVIO:',(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ').slice(0,400));
  await p.screenshot({path:D+'tf_'+slug+'_enviado.png',fullPage:true});
 }catch(e){ log('ERR',e.message.split('\n')[0]); await p.screenshot({path:D+'tf_'+slug+'_err.png',fullPage:true}).catch(()=>{}); }
 await b.close();
})();
