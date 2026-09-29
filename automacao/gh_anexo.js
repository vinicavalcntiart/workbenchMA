// Por que existe: em 09/09 a leitura de volta nova do apply_gh.js listou ZERO input[type=file]
// num formulario cujo Resume/CV a API declara como OBRIGATORIO. Ou o Greenhouse novo cria o
// input so depois de um clique, ou ele vive fora do DOM principal. Candidatura sem curriculo
// e o pior desfecho possivel: ela sai, confirma na tela, e nao vale nada.
// Uso: sh hb_run.sh gh_anexo.js <url>
const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2400},locale:'en-US',
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 await p.goto(process.argv[2],{timeout:120000,waitUntil:'networkidle'}).catch(()=>{});
 await p.waitForSelector('#first_name',{timeout:60000}).catch(()=>{});
 await p.waitForTimeout(4000);
 const conta=async(quando)=>{
   for(const f of p.frames()){
     const d=await f.evaluate(()=>({
       n:document.querySelectorAll('input[type=file]').length,
       ids:[...document.querySelectorAll('input[type=file]')].map(e=>e.id||e.name||'(sem id)'),
       temResume: !!document.getElementById('resume'),
     })).catch(()=>null);
     if(d) console.log(quando,'| frame',f.url().slice(0,70),'| file inputs:',d.n,JSON.stringify(d.ids),'| #resume existe:',d.temResume);
   }
 };
 await conta('ANTES do clique');
 console.log('botoes da area de curriculo:', JSON.stringify(await p.evaluate(()=>
   [...document.querySelectorAll('button,label,a,[role=button]')]
     .filter(e=>/resume|cv|attach|upload|file|dropbox|drive|manually/i.test(e.innerText||''))
     .map(e=>(e.innerText||'').replace(/\s+/g,' ').trim().slice(0,40)).slice(0,15))));
 // o Greenhouse novo troca a area de anexo por um menu; clicar em Attach costuma criar o input
 for(const t of ['Attach','Upload','Choose file','Resume']){
   const el=await p.$(`button:has-text("${t}"), label:has-text("${t}")`);
   if(el){ await el.click({force:true}).catch(()=>{}); console.log('cliquei em',t); await p.waitForTimeout(2500); break; }
 }
 await conta('DEPOIS do clique');
 console.log('HTML da area do curriculo:', (await p.evaluate(()=>{
   const h=[...document.querySelectorAll('*')].find(e=>/Resume\/CV|Resume/i.test(e.textContent||'')&&e.children.length<12&&e.closest('form'));
   return h? (h.closest('div')||h).outerHTML.replace(/\s+/g,' ').slice(0,900) : '(nao achei)';
 }).catch(e=>'erro '+e.message)));
 await b.close();
})().catch(e=>console.log('ERR',e.message));
