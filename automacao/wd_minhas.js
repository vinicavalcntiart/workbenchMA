// LE a lista "My Applications" de um locatario Workday onde o Vini JA TEM CONTA.
// uso: sh hb_run.sh wd_minhas.js <host> <site> <slug>
//
// POR QUE EXISTE, medido em 12/09 na Blizzard: a tela de confirmacao de um envio mostrou TRES
// candidaturas ativas naquela casa, e o repositorio inteiro so conhecia UMA. Uma delas era de
// AMBIENTE, contra a regra de personagem primeiro. Ou seja: o empregador sabe mais sobre o que
// ja recebeu do que o nosso arquivo, que e registro manual. Esta e a fonte de dedupe mais
// confiavel que existe para casa com Workday e conta.
//
// === A ROTA, MEDIDA EM 12/09 AS 22h NA BLIZZARD (controle com resposta conhecida) ===
// A tela /en-US/<site>/candidateHome devolve "There are 1 error(s). Use View All button for
// details." e NAO renderiza a lista. O erro e de RENDERIZACAO do SPA, nao de permissao e nao
// da casa: a mesma pagina, no mesmo carregamento, BUSCA E RECEBE os dados com HTTP 200 em
//
//     GET https://<host>/wday/cxs/<locatario>/<site>/applications?type=active&limit=4
//
// que respondeu {"total":3,...} com R028136, R028112 e R028122, exatamente as tres que a tela
// de confirmacao tinha mostrado uma hora antes. Ou seja: ler innerText da tela foi o defeito.
// A lista vem da API CXS, e ela aceita ?type=active e ?type=inactive.
// As rotas /userHome, /candidateHome/jobApplications, /myapplications e os endpoints CXS
// inventados (/candidateHome, /jobApplications, /candidate/applications) foram testados e
// devolvem HTTP 406. Nao insista neles.
//
// A sessao AINDA precisa ser de navegador logado: a chamada vai com os cookies da pagina.
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
  L('locatario:',LOC,'| site:',site,'| entrada propria?',!!CRED,'| nota:',(CRED&&CRED.nota)||'(sem)');
  const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
  const opts={ignoreHTTPSErrors:true,viewport:{width:1400,height:2000},locale:'en-US',
    userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'};
  if(fs.existsSync(estado)) opts.storageState=estado;
  const ctx=await b.newContext(opts); const p=await ctx.newPage();
  p.on('dialog',async d=>{await d.accept().catch(()=>{});});
  try{
    const base='https://'+host+'/en-US/'+site;
    await p.goto(base+'/candidateHome',{timeout:90000,waitUntil:'domcontentloaded'});
    await p.waitForTimeout(8000);
    // AVISO DE COOKIES tapa o formulario em varios locatarios (medido na Disney em 12/09).
    for(const r of ['Accept Cookies','Accept all','Accept']){
      const e=await p.$(`button:has-text("${r}")`);
      if(e && await e.isVisible().catch(()=>0)){ await e.click().catch(()=>{}); await p.waitForTimeout(2500); break; }
    }
    // MEDIDO NA DISNEY EM 12/09: o candidateHome deslogado tem ZERO <input>. O "Sign In" e um
    // BOTAO que abre o formulario, e nao o formulario.
    if(!(await p.$('input[data-automation-id="email"]'))){
      const sb=await p.$('button:has-text("Sign In"), a[role=button]:has-text("Sign In")');
      if(sb){ L('abrindo o formulario de login'); await sb.click({force:true}).catch(()=>{}); await p.waitForTimeout(7000); }
    }
    if(await p.$('input[data-automation-id="email"]')){
      L('pedindo login, entrando');
      await p.fill('input[data-automation-id="email"]',EMAIL).catch(()=>{});
      await p.fill('input[data-automation-id="password"]',SENHA).catch(()=>{});
      const bt=await p.$('[data-automation-id="signInSubmitButton"]')||await p.$('button[type=submit]');
      if(bt) await bt.click({force:true}).catch(()=>{}); else await p.keyboard.press('Enter').catch(()=>{});
      await p.waitForTimeout(13000);
      await p.goto(base+'/candidateHome',{timeout:90000,waitUntil:'domcontentloaded'}).catch(()=>{});
      await p.waitForTimeout(7000);
    }
    // PROVA DE SESSAO: o /userprofile so responde 200 com email quando ha login de verdade.
    const perfil=await p.evaluate(async u=>{try{const r=await fetch(u,{credentials:'include'});return {s:r.status,t:(await r.text()).slice(0,200)};}catch(e){return{s:-1,t:String(e)};}},
      '/wday/cxs/'+LOC+'/'+site+'/userprofile');
    let logado=false;
    try{ logado=!!JSON.parse(perfil.t.replace(/,"phone".*$/,'}')).emailAddress; }catch(e){ logado=/emailAddress/.test(perfil.t); }
    L('SESSAO userprofile ->',perfil.s,'| logado?',logado,'|',perfil.t.replace(/\s+/g,' ').slice(0,120));
    if(!logado){ L('!! SEM SESSAO. Nao da para ler a lista; nao conclua nada sobre a casa.'); }
    else{
      const pega=async(u)=>p.evaluate(async x=>{try{const r=await fetch(x,{credentials:'include'});return {s:r.status,t:await r.text()};}catch(e){return{s:-1,t:String(e)};}},u);
      for(const tipo of ['active','inactive']){
        // LIMITE: limit=50 devolve HTTP 400 (medido). O SPA usa limit=4. Pagina-se com offset.
        let dados=[],total=null,off=0,r0=null;
        for(let volta=0;volta<15;volta++){
          const r=await pega('/wday/cxs/'+LOC+'/'+site+'/applications?type='+tipo+'&limit=4&offset='+off);
          if(!r0) r0=r;
          if(r.s!==200) break;
          let j; try{ j=JSON.parse(r.t); }catch(e){ break; }
          total=j.total; const d=j.data||[];
          dados=dados.concat(d);
          if(d.length===0||dados.length>=total) break;
          off+=d.length;
        }
        if(r0.s!==200){ L('applications',tipo,'->',r0.s,r0.t.slice(0,200)); continue; }
        const j={total:total,data:dados};
        L('=== '+tipo.toUpperCase()+' | total:',j.total,'| lidas:',dados.length);
        // CAMPOS REAIS, conferidos no corpo cru da Blizzard em 12/09:
        // postingTitle ("Character Artist - StarCraft | Irvine, CA"), jobRequisitionId
        // ("R028136"), dateApplied ("September 12, 2026"), status ("Under Review"),
        // jobPostingAnchorId (titulo+req com hifen), draft (rascunho nao e candidatura).
        for(const a of (j.data||[])){
          L('  *',a.postingTitle||a.jobPostingAnchorId||'(sem titulo)',
            '| req:',a.jobRequisitionId||'?',
            '| enviada:',a.dateApplied||'?',
            '| status:',a.status||'?',
            (a.draft?'| RASCUNHO (nao e candidatura)':''));
        }
        console.log('    [cru]',JSON.stringify(j).slice(0,2600));
      }
    }
    await ctx.storageState({path:estado}).catch(()=>{});
  }catch(e){ L('ERRO',e.message.split('\n')[0].slice(0,180)); }
  await b.close();
})();
