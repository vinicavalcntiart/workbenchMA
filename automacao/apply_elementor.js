// FORMULARIO ELEMENTOR PRO (WordPress). Como se reconhece: os campos se chamam
// form_fields[...] e o envio vai por POST em /wp-admin/admin-ajax.php com
// action=elementor_pro_forms_send_form. A PROVA de envio, nesta familia, e dupla:
// (1) o corpo JSON da resposta do admin-ajax, capturado pelo page.on('response'), e
// (2) o texto da .elementor-message-success na tela. Formulario ainda cheio veta.
// Uso: sh hb_run.sh apply_elementor.js <url> <campos.json> [ENVIAR]
const {chromium}=require('playwright'); const fs=require('fs');
const [url,ansFile]=process.argv.slice(2); const SUBMIT=process.argv.includes('ENVIAR');
const A=JSON.parse(fs.readFileSync(ansFile,'utf8'));
const log=(...a)=>console.log('[el]',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:process.env.APPLY_PROXY||process.env.HTTPS_PROXY},
   args:['--no-sandbox','--ignore-certificate-errors','--disable-blink-features=AutomationControlled']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1366,height:900},
   userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',locale:'fr-FR'});
 await ctx.addInitScript(()=>{Object.defineProperty(navigator,'webdriver',{get:()=>undefined});});
 const p=await ctx.newPage();
 const respostas=[];
 p.on('response',async r=>{
   if(/admin-ajax\.php/.test(r.url())){
     let corpo=''; try{ corpo=(await r.text()).slice(0,900); }catch(e){ corpo='(sem corpo)'; }
     respostas.push({status:r.status(),corpo});
     log('RESPOSTA DO SERVIDOR',r.status(),corpo.slice(0,500));
   }
 });
 try{
  await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(6000);
  // parede de captcha: se houver desafio na pagina, nao se burla
  // MEDIDO as 18h05 na Waooh: o detector nao pode confundir reCAPTCHA v3 com desafio.
  // v3 e INVISIVEL e por pontuacao (aqui o script se chama elementor-recaptcha_v3-api-js e
  // o unico "campo" e o textarea oculto g-recaptcha-response): essa e lane que PASSA, a
  // mesma do Greenhouse. Parede e so o desafio visivel: widget de caixa (data-size que nao
  // seja invisible, ou div .g-recaptcha VISIVEL), hCaptcha ou Turnstile.
  const cap=await p.evaluate(()=>{
    const m=[];
    const v3=!!document.querySelector('script[id*="recaptcha_v3"],script[src*="render="]');
    const cx=[...document.querySelectorAll('.g-recaptcha,[data-sitekey]')]
      .filter(x=>x.tagName!=='TEXTAREA' && x.tagName!=='SCRIPT' && !!x.offsetParent
                 && (x.getAttribute('data-size')||'')!=='invisible');
    if(cx.length && !v3) m.push('recaptcha-caixa-visivel');
    if(document.querySelector('iframe[src*="hcaptcha"]')) m.push('hcaptcha');
    if(document.querySelector('iframe[src*="challenges.cloudflare"]')) m.push('turnstile');
    if(v3) console.log('[el] reCAPTCHA v3 invisivel: nao e parede, segue');
    return m;
  });
  log('captcha na pagina:',JSON.stringify(cap));
  if(cap.length){ log('PAREDE DE CAPTCHA: uma tentativa, registro e sigo'); await b.close(); return; }
  for(const [sel,val] of Object.entries(A.campos)){
    const el=await p.$(sel);
    if(!el){ log('NAO ACHEI o campo',sel,'| PARANDO'); await b.close(); return; }
    if(val.arquivo){ await el.setInputFiles(val.arquivo); await p.waitForTimeout(2500);
      const v=await p.$eval(sel,x=>x.value); log('anexo',sel,'=>',JSON.stringify(v.slice(-40)));
      if(!v){ log('anexo NAO colou | PARANDO'); await b.close(); return; } continue; }
    if(val.marcar){ await el.check({force:true,timeout:8000}).catch(async()=>{ await p.evaluate(s=>{const x=document.querySelector(s); x.checked=true; x.dispatchEvent(new Event('change',{bubbles:true}));},sel); });
      const c=await p.$eval(sel,x=>x.checked); log('caixa',sel,'marcada =>',c);
      if(!c){ log('caixa NAO marcou | PARANDO'); await b.close(); return; } continue; }
    await el.fill('');
    await el.type(String(val.texto),{delay:12});
    const lido=await p.$eval(sel,x=>x.value);
    log('campo',sel,'| leitura de volta:',JSON.stringify(lido.slice(0,90)));
    if(lido.trim()!==String(val.texto).trim()){ log('NAO BATE | PARANDO'); await b.close(); return; }
  }
  // campo isca
  const isca=await p.evaluate(()=>[...document.querySelectorAll('input,textarea')]
    .filter(x=>/^hp[_-]|honeypot|nickname_|bot[_-]?field/i.test(x.name||'')||/leave this field blank/i.test((x.labels&&x.labels[0]&&x.labels[0].innerText)||''))
    .map(x=>({name:x.name,valor:x.value})));
  log('campos isca:',JSON.stringify(isca));
  if(isca.some(x=>x.valor)){ log('ISCA PREENCHIDA | PARANDO'); await b.close(); return; }
  await p.screenshot({path:'el_antes.png',fullPage:true});
  if(!SUBMIT){ log('MODO SECO: nao cliquei em enviar'); await b.close(); return; }
  const bt=await p.$(A.botao||'button[type=submit], .elementor-button[type=submit]');
  if(!bt){ log('NAO ACHEI o botao de envio | PARANDO'); await b.close(); return; }
  await bt.click({force:true,timeout:15000});
  await p.waitForTimeout(14000);
  const tela=await p.evaluate(()=>{
    const s=document.querySelector('.elementor-message-success');
    const e=document.querySelector('.elementor-message-danger,.elementor-message-error');
    const vals=[...document.querySelectorAll('input[name^="form_fields"],textarea[name^="form_fields"]')]
      .map(x=>({n:x.name,v:x.type==='checkbox'?x.checked:(x.value||'').slice(0,40)}));
    return {sucesso:s?s.innerText.trim():null, erro:e?e.innerText.trim():null, campos:vals};
  });
  log('TEXTO DE SUCESSO NA TELA:',JSON.stringify(tela.sucesso));
  log('TEXTO DE ERRO NA TELA:',JSON.stringify(tela.erro));
  log('FORMULARIO DEPOIS DO ENVIO (se ainda cheio, NAO vale como prova):',JSON.stringify(tela.campos));
  log('RESPOSTAS DE admin-ajax:',JSON.stringify(respostas));
  await p.screenshot({path:'el_depois.png',fullPage:true});
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await b.close();
})();
