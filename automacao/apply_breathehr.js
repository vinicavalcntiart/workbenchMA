// BreatheHR (hr.breathehr.com) - familia de ATS INEDITA na campanha, medida em 21/09.
// Porteiro: reCAPTCHA v2 INVISIVEL amarrado ao BOTAO (class="g-recaptcha btn" + data-callback),
// nao ha caixa de desafio na carga. So o clique decide.
// uso: node apply_breathehr.js <url_do_/application/<id>/new> <slug> <ans.json> [--submit]
const {chromium}=require('playwright'); const fs=require('fs');
const [url,slug,ansFile,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const A=JSON.parse(fs.readFileSync(ansFile,'utf8'));
const TEL=process.env.VINI_TEL; if(!TEL){console.error('falta VINI_TEL');process.exit(1);}
const L=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await chromium.launch({proxy:{server:process.env.APPLY_PROXY||process.env.HTTPS_PROXY},args:['--no-sandbox','--ignore-certificate-errors']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2400},locale:'en-GB',userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'});
 const p=await ctx.newPage();
 try{
  await p.goto(url,{timeout:120000,waitUntil:'networkidle'}).catch(()=>{});
  await p.waitForSelector('#applicant_first_name',{timeout:60000});
  for(const [sel,val] of Object.entries(A.texto||{})){
    const v=val.replace('__TEL__',TEL);
    const el=await p.$(sel);
    if(el){ await el.fill(v); L('texto',sel,'=>',v.slice(0,40).replace(/\n/g,' ')); } else L('AUSENTE',sel);
  }
  for(const [sel,val] of Object.entries(A.selects||{})){
    const el=await p.$(sel);
    if(el){ try{ await el.selectOption({label:val}); L('select',sel,'=>',val);}catch(e){ L('select FALHOU',sel,val,e.message.split('\n')[0]); const ops=await p.$$eval(sel+' option',o=>o.map(x=>x.label).slice(0,40)); L('opcoes:',JSON.stringify(ops)); } } else L('AUSENTE select',sel);
  }
  for(const sel of (A.checks||[])){ const el=await p.$(sel); if(el){ await el.check().catch(async()=>{await el.click({force:true}).catch(()=>{});}); L('check',sel,await el.isChecked().catch(()=>'?')); } else L('AUSENTE check',sel); }
  await p.waitForTimeout(600);
  await p.screenshot({path:'filled_'+slug+'.png',fullPage:true});
  const lido=await p.evaluate(()=>{const o={};['applicant_first_name','applicant_last_name','applicant_phone_number','applicant_email','applicant_email_confirmation','applicant_notes','applicant_city'].forEach(i=>{const e=document.getElementById(i);o[i]=e?(e.value||'(VAZIO)').slice(0,60):'(AUSENTE)';});return o;});
  L('leitura de volta:',JSON.stringify(lido));
  if(!SUBMIT){ L('DRY RUN done'); await b.close(); return; }
  let postOK=false;
  p.on('response',async r=>{ if(r.request().method()==='POST' && !/recaptcha|gstatic|cloudflare/.test(r.url())){ let t='';try{t=(await r.text()).slice(0,200);}catch(e){} if(/\/application(\b|\/|\?)/.test(r.url()) && r.status()>=200 && r.status()<400) postOK=true; L('POST-RES',r.status(),r.url().slice(0,110),t.replace(/\s+/g,' ')); } });
  p.on('requestfailed',r=>{ if(r.method()==='POST') L('POST-FAILED',r.url().slice(0,110)); });
  const sb=await p.$('input[type=submit], button[type=submit], .g-recaptcha.btn, button:has-text("Submit")');
  if(!sb){ L('!! sem botao de submit'); } else {
    await sb.scrollIntoViewIfNeeded().catch(()=>{});
    await p.waitForTimeout(800);
    const cx=await sb.boundingBox().catch(()=>null);
    L('caixa do submit:',JSON.stringify(cx));
    if(cx) await p.mouse.click(cx.x+cx.width/2,cx.y+cx.height/2).catch(()=>{});
    else await sb.click({force:true}).catch(()=>{});
  }
  await p.waitForTimeout(18000);
  const txt=(await p.innerText('body')).replace(/\s+/g,' ');
  const chal=await p.$$eval('iframe',f=>f.filter(x=>/recaptcha|hcaptcha|challenge/i.test(x.src)&&x.offsetParent!==null&&x.getBoundingClientRect().height>60).length);
  await p.screenshot({path:'result_'+slug+'.png',fullPage:true});
  // PROVA DE ENVIO: 21/09, este script imprimiu SUBMITTED OK com o formulario ainda preenchido,
  // ainda em /application/<id>/new, ZERO POST na rede e o desafio de imagem do reCAPTCHA na tela.
  // A causa foi regex de texto sobre o BODY INTEIRO: a pagina do BreatheHR carrega um <select> com
  // a lista ISO de paises, e qualquer regex larga acha palavra dentro dela. Prova e (1) POST com
  // status 2xx/3xx para /application e (2) a URL DEIXAR de terminar em /new. Nunca regex de corpo.
  const saiuDoNew = !/\/new(\?|#|$)/.test(p.url());
  const ok = postOK && saiuDoNew;
  L(ok?'SUBMITTED OK':'NOT CONFIRMED','| POST aceito:',postOK,'| saiu do /new:',saiuDoNew,'| desafio visivel:',chal,'| url:',p.url(),'| texto:',txt.slice(0,300));
  if(!ok && chal>0) L('VEREDITO: parede de desafio na tela. Olhe result_'+slug+'.png e cite a frase literal.');
  if(!ok && chal===0 && !postOK) L('VEREDITO: nenhum POST e nenhum desafio visivel. NAO conclua porta limpa: o widget do BreatheHR nasce no clique.');
 }catch(e){ L('ERR',e.message.split('\n')[0]); await p.screenshot({path:'err_'+slug+'.png',fullPage:true}).catch(()=>{}); }
 await b.close();
})();
