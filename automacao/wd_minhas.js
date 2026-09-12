// LE a lista "My Applications" de um locatario Workday onde o Vini JA TEM CONTA.
// uso: sh hb_run.sh wd_minhas.js <host> <site> <slug>
//
// POR QUE EXISTE, medido em 12/09 na Blizzard: a tela de confirmacao de um envio mostrou TRES
// candidaturas ativas naquela casa, e o repositorio inteiro so conhecia UMA. Uma delas era de
// AMBIENTE, contra a regra de personagem primeiro. Ou seja: o empregador sabe mais sobre o que
// ja recebeu do que o nosso arquivo, que e registro manual. Esta e a fonte de dedupe mais
// confiavel que existe para casa com Workday e conta.
const {chromium}=require('playwright');
const fs=require('fs');
const C=require('./cred.json');
const [host,site,slug]=process.argv.slice(2);
const LOC=(host||'').split('.')[0];
const CRED=C[LOC+'_workday'];
const SENHA=(CRED&&typeof CRED==='object'?CRED.senha:CRED)||C.padrao_campanha;
const EMAIL=(CRED&&typeof CRED==='object'&&CRED.email)||C.email;
const estado='wdst_'+slug+'.json';
const L=(...a)=>console.log('[minhas]',...a);
(async()=>{
  L('locatario:',LOC,'| entrada propria?',!!CRED,'| nota:',(CRED&&CRED.nota)||'(sem)');
  const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
  const opts={ignoreHTTPSErrors:true,viewport:{width:1400,height:2200},locale:'en-US',
    userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'};
  if(fs.existsSync(estado)) opts.storageState=estado;
  const ctx=await b.newContext(opts); const p=await ctx.newPage();
  try{
    const base='https://'+host+'/en-US/'+site;
    await p.goto(base+'/candidateHome',{timeout:90000,waitUntil:'domcontentloaded'});
    await p.waitForTimeout(9000);
    // AVISO DE COOKIES tapa o formulario em varios locatarios (medido na Disney em 12/09):
    // o input de email existe no DOM mas fica atras do banner, o login nao acontece e a tela
    // devolve "1 Error" sem dizer nada.
    for(const r of ['Accept Cookies','Accept all','Accept']){
      const e=await p.$(`button:has-text("${r}")`);
      if(e && await e.isVisible().catch(()=>0)){ await e.click().catch(()=>{}); await p.waitForTimeout(2500); break; }
    }
    let t=await p.innerText('body').catch(()=>'');
    // MEDIDO NA DISNEY EM 12/09: o candidateHome deslogado tem ZERO <input>. O "Sign In" e um
    // BOTAO que abre o formulario, e nao o formulario. A versao anterior exigia que o input de
    // email ja existisse, entao nunca tentava logar e so reportava "1 Error".
    if(!(await p.$('input[data-automation-id="email"]'))){
      const sb=await p.$('button:has-text("Sign In"), a[role=button]:has-text("Sign In")');
      if(sb){ L('abrindo o formulario de login'); await sb.click({force:true}).catch(()=>{}); await p.waitForTimeout(7000); }
    }
    if(await p.$('input[data-automation-id="email"]')){
      L('pedindo login, entrando');
      await p.fill('input[data-automation-id="email"]',EMAIL).catch(()=>{});
      await p.fill('input[data-automation-id="password"]',SENHA).catch(()=>{});
      let bt=await p.$('[data-automation-id="signInSubmitButton"]')||await p.$('button[type=submit]:has-text("Sign In")');
      if(bt) await bt.click({force:true}).catch(()=>{}); else await p.keyboard.press('Enter').catch(()=>{});
      await p.waitForTimeout(14000);
      await p.goto(base+'/candidateHome',{timeout:90000,waitUntil:'domcontentloaded'}).catch(()=>{});
      await p.waitForTimeout(8000);
      t=await p.innerText('body').catch(()=>'');
    }
    // LER O DETALHE DO ERRO. A pagina escreve "Use View All button for details", ou seja o
    // motivo existe e so nao esta na tela. Adivinhar aqui ja custou tres tentativas hoje.
    if(/error/i.test(t)){
      const va=await p.$('button:has-text("View All")');
      if(va){ await va.click().catch(()=>{}); await p.waitForTimeout(3000); }
      const det=await p.evaluate(()=>[...document.querySelectorAll('[data-automation-id*="error"],[role="alert"],[class*="error"]')]
        .filter(e=>e.offsetParent!==null).map(e=>(e.innerText||'').replace(/\s+/g,' ').trim()).filter(Boolean).slice(0,6));
      L('DETALHE DO ERRO:',JSON.stringify(det));
    }
    L('=== CANDIDATE HOME ===');
    console.log(t.replace(/\n{2,}/g,'\n').slice(0,3000));
    await ctx.storageState({path:estado}).catch(()=>{});
  }catch(e){ L('ERRO',e.message.split('\n')[0].slice(0,140)); }
  await b.close();
})();
