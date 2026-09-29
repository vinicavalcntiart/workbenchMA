// Talentsoft. uso: node apply_talentsoft.js <urlDaVaga> <slug> [--submit]
// Credenciais SO por ambiente (TS_LOGIN, TS_SENHA): o repositorio da campanha e PUBLICO.
// ARMADILHA 1: candidatura exige CONTA. O botao Apply leva a /my-account/log-in.aspx.
// ARMADILHA 2: a pagina de login tem TRES campos de senha (a caixa lateral tambem tem um) e
// TRES botoes de submit. Mire pelo sufixo do name, nunca pelo primeiro que aparecer.
const {chromium}=require('playwright');
const [url,slug,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const LOGIN=process.env.TS_LOGIN, SENHA=process.env.TS_SENHA; const D=__dirname+'/';
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1300,height:2600},userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-CA'})).newPage();
 const dump=async(tag)=>{
  const c=await p.evaluate(()=>[...document.querySelectorAll('input,select,textarea')].filter(e=>e.type!=='hidden'&&e.offsetParent!==null)
    .map(e=>({n:(e.name||e.id||'').split('$').pop(),t:e.type||e.tagName,req:!!(e.required||e.getAttribute('aria-required')==='true'),
      v:(e.value||'').slice(0,30),lab:((e.labels&&e.labels[0]?e.labels[0].innerText:'')||e.getAttribute('aria-label')||e.placeholder||'').replace(/\s+/g,' ').trim().slice(0,55)})));
  log('=== CAMPOS ('+tag+'):',c.length,'==='); c.forEach(x=>log('   ',JSON.stringify(x)));
  const bt=await p.evaluate(()=>[...document.querySelectorAll('input[type=submit],button')].filter(e=>e.offsetParent!==null)
    .map(e=>({n:(e.name||e.id||'').split('$').pop(),v:(e.value||e.innerText||'').trim().slice(0,35)})));
  log('botoes:',JSON.stringify(bt));
  const err=await p.evaluate(()=>[...new Set([...document.querySelectorAll('[class*="error"],[role="alert"],[class*="validation"]')].filter(e=>e.offsetParent!==null).map(e=>(e.innerText||'').replace(/\s+/g,' ').trim()).filter(t=>t&&t.length<140))]);
  if(err.length){ log('VALIDACAO:'); err.forEach(e=>log('   !',e)); }
  return c; };
 try{
  const base=new URL(url).origin;
  await p.goto(base+'/my-account/log-in.aspx',{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(6000);
  for(const s of ['#onetrust-accept-btn-handler','button:has-text("Accept")']){const e=await p.$(s);if(e){await e.click().catch(()=>{});await p.waitForTimeout(1500);break;}}
  const u=await p.$('input[name$="tbxIdentifiant"]'), s2=await p.$('input[name$="tbxPassword"]');
  if(!u||!s2){ log('SEM formulario de login na pagina'); await dump('login'); await b.close(); return; }
  await u.fill(LOGIN); await s2.fill(SENHA);
  const bl=await p.$('input[name$="btnConnexionViaPage"]');
  await bl.click({timeout:20000}).catch(e=>log('login',e.message.split('\n')[0]));
  await p.waitForTimeout(9000);
  log('url depois do login:',p.url());
  const txt=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
  log('entrou?',!/Username \(email address\)/i.test(txt.slice(0,600))?'parece que SIM':'NAO, ainda na tela de login');
  await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(7000);
  const ap=await p.$('input[name$="bt_Postuler_Haut"], input[name$="bt_Postuler"]');
  if(ap){ await ap.scrollIntoViewIfNeeded().catch(()=>{}); await ap.click({timeout:20000}).catch(e=>log('apply',e.message.split('\n')[0])); await p.waitForTimeout(9000); }
  else log('SEM botao de candidatura na vaga');
  log('url da candidatura:',p.url());
  log('texto:',(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ').slice(0,400));
  await dump('formulario');
  await p.screenshot({path:D+'ts_'+slug+'.png',fullPage:true});
  const cap=await p.evaluate(()=>({fr:[...document.querySelectorAll('iframe')].map(f=>f.src||'').filter(x=>/captcha|challenges|turnstile/i.test(x)),w:document.querySelectorAll('.g-recaptcha,[data-sitekey],.h-captcha,.cf-turnstile').length}));
  log('captcha no HTML (sem veredito):',JSON.stringify(cap));
 }catch(e){ log('ERR',e.message.split('\n')[0]); await p.screenshot({path:D+'ts_'+slug+'_err.png',fullPage:true}).catch(()=>{}); }
 await b.close();
})();
