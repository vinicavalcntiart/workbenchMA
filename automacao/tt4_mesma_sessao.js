// TESTE QUE FALTAVA (pedido no registro de 16/09): o link de acesso do Connect nao abria
// sessao. Duas hipoteses sobraram, as duas ja com prazo e cookie DESCARTADOS:
//   (a) o candidato existe como APLICANTE mas nao tem inscricao de Connect;
//   (b) o locatario exige que o link seja aberto na MESMA sessao/navegador que o PEDIU.
// Este script testa (b) da unica forma honesta: pede o link DENTRO do navegador (POST no
// formulario de /connect/login servido pela propria pagina) e abre o link na MESMA sessao,
// com contexto PERSISTENTE em disco (prof_tt_<slug>), para as duas etapas partilharem cookie.
// Uso: sh hb_run.sh tt4_mesma_sessao.js pede <host>
//      sh hb_run.sh tt4_mesma_sessao.js abre <host> <link-do-email>
const {chromium}=require('playwright'); const {abrirLocal,abrirPerfil}=require('./navegador'); const fs=require('fs');
const ETAPA=process.argv[2], HOST=process.argv[3], LINK=process.argv[4];
const P=JSON.parse(fs.readFileSync('/home/user/apply/pessoal.json','utf8'));
const slug=HOST.split('.')[0];
const log=(...a)=>console.log('['+slug+'/'+ETAPA+']',...a);
(async()=>{
 const ctx=await abrirPerfil('/home/user/apply/prof_tt_'+slug,{headless:false,args:['--disable-blink-features=AutomationControlled'],ignoreHTTPSErrors:true,viewport:{width:1280,height:1200},locale:'en-US',userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'});
 const p=ctx.pages()[0]||await ctx.newPage();
 const cookies=async()=>{
   for(let v=0;v<3;v++){
     const c=await p.evaluate(()=>{
       const a=[...document.querySelectorAll('button,a,[role=button]')].filter(x=>{
         const t=(x.innerText||'').toLowerCase().replace(/\s+/g,' ').trim();
         return !!x.offsetParent && /^(accept all cookies|accept all|accept cookies|accept|allow all|i accept|got it)$/.test(t);
       });
       if(!a.length) return null; a[0].click(); return (a[0].innerText||'').trim().slice(0,40);
     });
     if(c){ log('cookies:',JSON.stringify(c)); await p.waitForTimeout(1500); return; }
     await p.waitForTimeout(800);
   }
 };
 try{
  if(ETAPA==='pede'){
   await p.goto('https://'+HOST+'/connect/login',{timeout:120000,waitUntil:'domcontentloaded'});
   await p.waitForTimeout(3500); await cookies();
   log('url:',p.url());
   const campos=await p.evaluate(()=>[...document.querySelectorAll('input')].filter(x=>!!x.offsetParent)
     .map(x=>({t:x.type,n:x.name,id:x.id})));
   log('campos:',JSON.stringify(campos));
   const em=await p.$('input[type=email]')||await p.$('input[name*="email"]');
   if(!em){ log('SEM campo de email em /connect/login'); await ctx.close(); return; }
   await em.fill(P.email); await p.waitForTimeout(600);
   const bt=await p.evaluate(()=>{
     const b=[...document.querySelectorAll('button[type=submit],input[type=submit],button')].filter(x=>!!x.offsetParent)
       .filter(x=>/log ?in|send|continue|sign in/i.test(((x.innerText||x.value||'')+'').trim()));
     if(!b.length) return null; b[0].click(); return ((b[0].innerText||b[0].value||'')+'').trim().slice(0,40);
   });
   log('botao de pedido:',JSON.stringify(bt));
   await p.waitForTimeout(7000);
   log('depois do pedido, url:',p.url());
   log('tela:',JSON.stringify(await p.evaluate(()=>((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,260))));
   await p.screenshot({path:'tt4_'+slug+'_pede.png'}).catch(()=>{});
  }
  if(ETAPA==='sonda'){
   // SONDA: abre o link e pergunta a CADA caminho do Connect se ha sessao, porque barrar por
   // um caminho so (o /connect/profile/settings) pode estar lendo a tela errada.
   await p.goto(LINK,{timeout:120000,waitUntil:'domcontentloaded'});
   await p.waitForTimeout(5000); await cookies();
   log('depois do link, url:',p.url());
   for(const c of ['/connect/dashboard','/connect/profile','/connect/profile/settings','/connect/resume','/connect/questions/start','/connect/candidates/new']){
     await p.goto('https://'+HOST+c,{timeout:90000,waitUntil:'domcontentloaded'}).catch(e=>log(c,'goto:',e.message.split('\n')[0]));
     await p.waitForTimeout(3500); await cookies();
     const d=await p.evaluate(()=>({url:location.pathname,
       campos:[...document.querySelectorAll('input,textarea,select')].filter(x=>!!x.offsetParent).map(x=>x.type+':'+(x.name||x.id)).slice(0,12),
       txt:((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,180)}));
     log('  SONDA',c,'->',JSON.stringify(d));
   }
   await p.screenshot({path:'tt4_'+slug+'_sonda.png',fullPage:true}).catch(()=>{});
  }

  if(ETAPA==='abre'){
   await p.goto(LINK,{timeout:120000,waitUntil:'domcontentloaded'});
   await p.waitForTimeout(5000); await cookies();
   log('depois do link, url:',p.url());
   await p.goto('https://'+HOST+'/connect/profile/settings',{timeout:90000,waitUntil:'domcontentloaded'});
   await p.waitForTimeout(4500); await cookies();
   const tem=await p.$('#candidate_first_name');
   log('RESULTADO:',tem?'SESSAO ABERTA (#candidate_first_name existe)':'SEM SESSAO');
   log('tela:',JSON.stringify(await p.evaluate(()=>((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,260))));
   await p.screenshot({path:'tt4_'+slug+'_abre.png'}).catch(()=>{});
  }
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await ctx.close();
})();
