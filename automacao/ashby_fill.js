// Preenchedor de formulario do ASHBY (jobs.ashbyhq.com/<slug>/<uuid>/application).
// Uso: sh hb_run.sh ashby_fill.js <url> <slug> [--submit]
// MEDIDO EM 20/09: o reCAPTCHA do Ashby carrega com size=invisible e SEM bframe, ou seja nao ha
// desafio humano na carga. Pela regra do BRIEF-JHON isso NAO garante passagem, mas autoriza a
// tentativa - a familia estava condenada como "parede de plataforma" sem nunca ter sido clicada.
// ARMADILHA: o PRIMEIRO input[type=file] da pagina e o "Autofill from resume", nao o campo de
// curriculo. O campo de verdade e #_systemfield_resume. Anexar no errado deixa o obrigatorio vazio.
const {chromium}=require('playwright'); const {abrirLocal}=require('./navegador'); const fs=require('fs');
const [url,slug,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const CV='/home/user/apply/Vini_Cavalcanti_CV.pdf';
const log=(...a)=>console.log(`[${slug}]`,...a);
(async()=>{
 const b=await abrirLocal({headless:false});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2400},userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-GB'})).newPage();
 try{
  await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForSelector('#_systemfield_name',{timeout:60000}); await p.waitForTimeout(2500);
  await p.fill('#_systemfield_name','Vini Cavalcanti');
  await p.fill('#_systemfield_email','contact@vinicavalcanti.art');
  await p.setInputFiles('#_systemfield_resume',CV); await p.waitForTimeout(6000);
  // campo de localizacao: input de texto com sugestao; escolher da lista quando houver
  const outros=await p.$$('form input[type="text"]:not(#_systemfield_name)');
  for(const el of outros){
    const lab=await el.evaluate(e=>{const l=e.closest('div')?e.closest('div').innerText:''; return (l||'').slice(0,60);});
    if(/location|city|where/i.test(lab)){
      await el.click(); await el.type('Olinda, Pernambuco, Brazil',{delay:60}); await p.waitForTimeout(3000);
      const opts=await p.$$eval('[role="option"], [class*="option"]',els=>els.filter(e=>e.offsetParent!==null).map(e=>e.innerText.trim()).slice(0,8));
      log('opcoes de local:',JSON.stringify(opts));
      if(opts.length){ await p.keyboard.press('ArrowDown'); await p.waitForTimeout(400); await p.keyboard.press('Enter'); }
      await p.waitForTimeout(800);
      log('local lido de volta:',await el.inputValue());
    }
  }
  // iscas: nenhum campo de texto sem rotulo e preenchido por varredura cega aqui.
  const antes=await p.evaluate(()=>document.body.innerText.slice(0,400));
  await p.screenshot({path:`filled_${slug}.png`,fullPage:true});
  const lido=await p.evaluate(()=>({name:(document.querySelector('#_systemfield_name')||{}).value,email:(document.querySelector('#_systemfield_email')||{}).value}));
  log('leitura de volta:',JSON.stringify(lido));
  const temCV=await p.evaluate(()=>/Vini_Cavalcanti_CV|\.pdf/i.test(document.body.innerText));
  log('CV visivel no formulario:',temCV);
  const frames=p.frames().map(f=>f.url()).filter(u=>/recaptcha|hcaptcha|turnstile|captcha-delivery/i.test(u));
  log('captcha na carga:',JSON.stringify(frames.map(u=>u.replace(/.*\/(api2|enterprise)\//,'$1/').slice(0,60))));
  if(!SUBMIT){ log('DRY RUN done'); await b.close(); return; }
  const bt=await p.$('button:has-text("Submit Application")');
  if(!bt){ log('[erro] botao de envio nao achado'); await b.close(); return; }
  const urlAntes=p.url();
  await bt.click({force:true});
  let txt='',urlDepois=urlAntes;
  for(let i=0;i<16;i++){ await p.waitForTimeout(5000); txt=await p.evaluate(()=>document.body.innerText.slice(0,900)); urlDepois=p.url();
    if(/thank|received|submitted|success|application sent/i.test(txt)) break; }
  log('URL antes:',urlAntes); log('URL depois:',urlDepois);
  log('TEXTO DEPOIS:',txt.replace(/\s+/g,' ').slice(0,700));
  await p.screenshot({path:`sent_${slug}.png`,fullPage:true});
 }catch(e){ log('ERR',e.message); }
 await b.close();
})();
