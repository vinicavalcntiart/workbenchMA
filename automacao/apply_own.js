// Preenchedor de formulario proprio com campos por name/id. Uso: sh hb_run.sh apply_own.js <respostas.json> <slug> [--submit]
// json: {"url","campos":{"#id":"valor"},"selects":{"#position":"3D Generalist"},"botao":"SUBMIT"}
// O telefone entra como __TEL__ e vem de VINI_TEL: o repositorio e publico.
const {chromium}=require('playwright'); const fs=require('fs');
const [ansFile,slug,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const A=JSON.parse(fs.readFileSync(ansFile)); const D=__dirname;
for(const k of Object.keys(A.campos||{})) if(A.campos[k]==='__TEL__'){
  if(!process.env.VINI_TEL){ console.error('[erro] o arquivo pede __TEL__ e falta VINI_TEL'); process.exit(1); }
  A.campos[k]=process.env.VINI_TEL;
}
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1400,height:2600},locale:'en-US',
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 // LICAO DE 09/09 NA FUTURE ASSOCIATE: a primeira versao so escutava 'response' e o log saiu
 // LIMPO, sem POST nenhum, enquanto o texto da tela casava com a regex de sucesso. Ou seja: o
 // verificador disse "positivo" sobre uma pagina que nao tinha enviado nada. Escutar tambem
 // 'request' e 'requestfailed' separa as tres coisas que o log antigo confundia: nao clicou,
 // clicou e o pedido falhou, clicou e o servidor respondeu.
 p.on('request',r=>{ if(r.method()==='POST') log('[pedido POST]', r.url().slice(0,110)); });
 p.on('requestfailed',r=>{ if(r.method()==='POST') log('[pedido POST FALHOU]', r.url().slice(0,110), r.failure()&&r.failure().errorText); });
 p.on('response',async r=>{ if(r.request().method()==='POST'&&!/analytics|sentry|gtag|facebook/i.test(r.url())){ let t=''; try{t=(await r.text()).slice(0,220);}catch(e){} log('[rede POST]',r.status(),r.url().slice(0,100),t.replace(/\s+/g,' ')); } });
 try{
  await p.goto(A.url,{waitUntil:'domcontentloaded',timeout:120000}); await p.waitForTimeout(7000);
  for(const t of ['Accept','Accept All','I agree','Got it','OK']){ const e=p.getByRole('button',{name:new RegExp('^'+t+'$','i')}).first();
    if(await e.count().catch(()=>0)){ await e.click().catch(()=>{}); await p.waitForTimeout(1200); break; } }
  for(const [sel,v] of Object.entries(A.selects||{})){
    const el=await p.$(sel); if(!el){ log('NAO ACHEI o select',sel); continue; }
    await el.scrollIntoViewIfNeeded().catch(()=>{});
    await el.selectOption({label:v}).catch(async()=>{ await el.selectOption(v).catch(()=>{}); });
    log('select',sel,'=>',await el.inputValue().catch(()=>'?'));
  }
  for(const [sel,v] of Object.entries(A.campos||{})){
    const el=await p.$(sel); if(!el){ log('NAO ACHEI o campo',sel); continue; }
    await el.scrollIntoViewIfNeeded().catch(()=>{});
    await el.click({force:true}).catch(()=>{}); await el.fill('').catch(()=>{});
    await el.type(String(v),{delay:3}).catch(()=>{});
    const lido=await el.inputValue().catch(()=>'');
    log('campo',sel, lido.length? '('+lido.length+' chars) '+lido.slice(0,50) : '(NAO ENTROU NADA)');
  }
  await p.waitForTimeout(1200);
  // leitura de volta imediatamente antes do clique: formulario que redesenha apaga campo em silencio
  let vazio=false;
  for(const sel of Object.keys(A.campos||{})){ const v=await p.$eval(sel,e=>e.value).catch(()=>null);
    if(v===null||!String(v).trim()){ log('  leitura final',sel,'=>',v===null?'(CAMPO SUMIU)':'(VAZIO)'); vazio=true; }
    else log('  leitura final',sel,'=>',String(v).length,'chars'); }
  if(vazio) log('!! PARE: obrigatorio vazio na leitura final');
  await p.screenshot({path:D+'/own_'+slug+'_pre.png',fullPage:true}).catch(()=>{});
  log('captcha iframes:',JSON.stringify(await p.$$eval('iframe',fs=>fs.map(f=>f.src).filter(s=>/recaptcha|hcaptcha|turnstile|datadome/i.test(s))).catch(()=>[])));
  if(!SUBMIT){ log('MODO SECO, nada enviado'); await b.close(); return; }
  const sb=await p.$('button:has-text("'+(A.botao||'SUBMIT')+'"), input[type=submit], button[type=submit]');
  if(!sb){ log('!! nao achei o botao de envio'); await b.close(); return; }
  await sb.scrollIntoViewIfNeeded().catch(()=>{}); await p.waitForTimeout(900);
  const cx=await sb.boundingBox().catch(()=>null); log('caixa do botao:',JSON.stringify(cx));
  if(cx) await p.mouse.click(cx.x+cx.width/2, cx.y+cx.height/2).catch(()=>{}); else await sb.click({force:true}).catch(()=>{});
  await p.waitForTimeout(15000);
  const txt=(await p.innerText('body')).replace(/\s+/g,' ');
  const chal=await p.$$eval('iframe',fs=>fs.filter(f=>/hcaptcha|recaptcha/i.test(f.src)&&f.getBoundingClientRect().height>100).length).catch(()=>0);
  await p.screenshot({path:D+'/own_'+slug+'_post.png',fullPage:true}).catch(()=>{});
  const ok=/thank you|thanks|submitted|received|success|we'll be in touch|confirm your human|in touch soon/i.test(txt);
  log(ok?'RESPOSTA POSITIVA NA TELA (leia o texto)':'NAO CONFIRMADA','| desafio visivel:',chal,'| url:',p.url());
  log('TEXTO COMPLETO:',txt.slice(0,2500));
 }catch(e){ log('ERR',e.message.split('\n')[0]); await p.screenshot({path:D+'/own_'+slug+'_err.png',fullPage:true}).catch(()=>{}); }
 await b.close();
})();
