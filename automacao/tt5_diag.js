// DIAGNOSTICO do formulario de INSCRICAO do Teamtailor Connect (/connect).
// Por que existe: em 16/09 ficou provado que o link "Log in to Connect" NAO abre sessao em 15
// locatarios (tres hipoteses testadas e descartadas: prazo, cookie e pedir o link dentro do
// proprio navegador; e a sonda mostrou que TODO caminho /connect/* redireciona para /connect,
// a tela de inscricao). A pista que sobra e que o proprio CADASTRO ja da sessao: o registro de
// 16/09 diz que, logo depois de inscrever, a URL /connect/dashboard abria com "Welcome to
// Connect". Se for isso, o perfil e o questionario se fazem na MESMA sessao do cadastro, e o
// link de email nunca foi necessario.
// Este script so LE: passo a passo do formulario, com screenshot de cada tela.
// Uso: sh hb_run.sh tt5_diag.js <host>
const {chromium}=require('playwright'); const {abrirLocal,abrirPerfil}=require('./navegador'); const fs=require('fs');
const HOST=process.argv[2]; const slug=HOST.split('.')[0];
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await abrirLocal({headless:false,args:['--disable-blink-features=AutomationControlled']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:1400},locale:'en-US',
   userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'});
 const p=await ctx.newPage();
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
 const dump=async(t)=>{
   await p.waitForTimeout(2500);
   const d=await p.evaluate(()=>({url:location.href,
     campos:[...document.querySelectorAll('input,textarea,select')].filter(x=>!!x.offsetParent||x.type==='hidden')
       .map(x=>({ty:x.type,n:x.name,id:x.id,vis:!!x.offsetParent,
         rot:((x.labels&&x.labels[0]&&x.labels[0].innerText)||x.getAttribute('aria-label')||x.placeholder||'').replace(/\s+/g,' ').trim().slice(0,60)})),
     bt:[...new Set([...document.querySelectorAll('button,a[role=button],input[type=submit]')].filter(x=>!!x.offsetParent)
        .map(x=>((x.innerText||x.value||'')+'').replace(/\s+/g,' ').trim()).filter(x=>x&&x.length<60))],
     txt:((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,700)}));
   log('== '+t+' ==',d.url);
   log('  campos:',JSON.stringify(d.campos.filter(c=>c.vis&&c.ty!=='radio'&&c.ty!=='checkbox')));
   log('  n radios/checks:',d.campos.filter(c=>c.ty==='radio'||c.ty==='checkbox').length);
   log('  botoes:',JSON.stringify(d.bt));
   log('  txt:',JSON.stringify(d.txt));
   await p.screenshot({path:'tt5_'+slug+'_'+t+'.png',fullPage:true}).catch(()=>{});
   return d;
 };
 try{
  await p.goto('https://'+HOST+'/connect',{timeout:120000,waitUntil:'domcontentloaded'});
  await cookies();
  await dump('s1');
  // marca o departamento de arte, se houver, e avanca
  const dep=await p.evaluate(()=>{
    const r=[...document.querySelectorAll('input[type=radio][name="candidate[department_id]"],input[type=checkbox][name="candidate[department_id]"]')];
    const rot=x=>((x.labels&&x.labels[0]&&x.labels[0].innerText)||(x.closest('label')?x.closest('label').innerText:'')||'').replace(/\s+/g,' ').trim();
    const alvo=r.find(x=>/game art|^art$|\bart\b/i.test(rot(x)))||r[0];
    if(!alvo) return null; alvo.click(); return {rotulo:rot(alvo),value:alvo.value,total:r.length};
  });
  log('departamento marcado:',JSON.stringify(dep));
  await p.waitForTimeout(2000);
  for(let i=2;i<=5;i++){
    const av=await p.evaluate(()=>{
      const b=[...document.querySelectorAll('button,a,input[type=submit]')].filter(x=>!!x.offsetParent)
        .filter(x=>/^(continue|next|save|submit|connect|done)$/i.test(((x.innerText||x.value||'')+'').replace(/\s+/g,' ').trim()));
      if(!b.length) return null; b[0].click(); return ((b[0].innerText||b[0].value||'')+'').trim();
    });
    log('avancar para s'+i+':',JSON.stringify(av));
    if(!av) break;
    await p.waitForTimeout(4500); await cookies();
    await dump('s'+i);
  }
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await b.close();
})();
