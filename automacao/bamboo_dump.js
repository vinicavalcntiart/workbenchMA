// Dump dos campos REAIS de um formulario do BambooHR, depois do clique em Apply.
// Existe porque os nomes de campo NAO sao os mesmos em todos os quadros: na Offworld o
// endereco nao e "address" e a lista de provincia so aparece depois de escolher o pais.
// Uso: sh hb_run.sh bamboo_dump.js <url>
const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2600},locale:'en-US',
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 await p.goto(process.argv[2],{timeout:120000,waitUntil:'domcontentloaded'});
 await p.waitForTimeout(4000);
 for(let t=0;t<6;t++){
   const loc=p.getByText('Apply for This Job',{exact:false});
   if(await loc.count().catch(()=>0)){ await loc.first().click({timeout:15000}).catch(()=>{}); await p.waitForTimeout(6000); break; }
   await p.waitForTimeout(3000);
 }
 await p.locator('input[name=firstName]').first().waitFor({timeout:60000}).catch(()=>{});
 const campos=await p.evaluate(()=>[...document.querySelectorAll('input,select,textarea')].map(e=>{
   let lab='';
   if(e.id){ const l=document.querySelector('label[for="'+CSS.escape(e.id)+'"]'); if(l) lab=l.innerText; }
   if(!lab){ const l=e.closest('label'); if(l) lab=l.innerText; }
   if(!lab){ const w=e.closest('div,li,fieldset'); if(w) lab=(w.innerText||'').slice(0,80); }
   return {name:e.name, id:e.id, tag:e.tagName, type:e.type, req:e.required,
           lab:(lab||'').replace(/\s+/g,' ').trim().slice(0,70),
           val:(e.value||'').slice(0,40),
           op:e.tagName==='SELECT'?[...e.options].map(o=>o.text.trim()).slice(0,8):undefined};
 }));
 campos.forEach(c=>console.log(JSON.stringify(c)));
 await b.close();
})();
