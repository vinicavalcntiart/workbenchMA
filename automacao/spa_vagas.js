// Le a lista de vagas de um quadro que e SPA (curl devolve casca vazia). Uso: sh hb_run.sh spa_vagas.js <url>
const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1400,height:2600},locale:'en-US',
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 const apis=[];
 p.on('response',r=>{ const u=r.url(); if(/api|graphql|jobs|positions|openings|vacanc/i.test(u)&&!/\.(png|jpg|svg|css|woff)/i.test(u)) apis.push(r.status()+' '+u.slice(0,120)); });
 await p.goto(process.argv[2],{waitUntil:'domcontentloaded',timeout:120000}).catch(e=>console.log('goto',e.message.split('\n')[0]));
 for(let i=0;i<8;i++){ await p.waitForTimeout(4000);
   const t=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
   if(t.length>400) break; }
 await p.waitForTimeout(3000);
 console.log('URL final:',p.url());
 console.log('TEXTO:',(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ').slice(0,2500));
 console.log('LINKS de vaga:',JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('a')].map(a=>({t:(a.innerText||'').replace(/\s+/g,' ').trim().slice(0,60),h:a.href})).filter(x=>x.t&&/job|career|position|vacan|apply|artist|engineer|design/i.test(x.t+x.h)).slice(0,30)),null,1));
 console.log('APIs vistas:',JSON.stringify([...new Set(apis)].slice(0,12),null,1));
 await b.close();
})().catch(e=>console.log('ERR',e.message));
