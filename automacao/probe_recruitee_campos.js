const {chromium}=require('playwright');
const url=process.argv[2];
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2600},locale:'en-US'})).newPage();
 await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'});
 await p.waitForTimeout(9000);
 const campos=await p.evaluate(()=>{
  const acha=e=>{ let n=e,c=''; for(let i=0;i<6&&n;i++){n=n.parentElement; if(n){const t=(n.innerText||'').trim(); if(t.length>c.length&&t.length<200)c=t;}} return c.replace(/\s+/g,' '); };
  return [...document.querySelectorAll('input,select,textarea')]
   .filter(e=>e.type!=='hidden')
   .map(e=>({name:e.name||'',tipo:e.type||e.tagName,value:(e.value||'').slice(0,45),
             req:!!(e.required||e.getAttribute('aria-required')==='true'),
             visivel:e.offsetParent!==null, ctx:acha(e).slice(0,130)}));
 });
 campos.forEach(c=>console.log(JSON.stringify(c)));
 await b.close();
})();
