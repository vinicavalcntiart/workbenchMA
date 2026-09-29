// Despeja as perguntas customizadas de um formulario Teamtailor: indice, TIPO e opcoes.
// Existe porque o preenchedor so mostra o TEXTO da pergunta quando ela esta sem resposta, e
// sem o tipo nao da para escrever o ansq_*.json sem adivinhar (e adivinhar tipo choice ja
// marcou "Yes" sozinho em campo de elegibilidade uma vez).
// Uso: sh hb_run.sh tt_qdump.js <url>
const {chromium}=require('playwright');
const url=process.argv[2];
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2400},
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-US'})).newPage();
 await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'}); await p.waitForTimeout(4000);
 for(const t of ['Accept all','Accept All','Accept']){ const e=await p.$(`button:has-text("${t}")`); if(e){ await e.click().catch(()=>{}); await p.waitForTimeout(1200); break; } }
 for(let i=0;i<12 && !(await p.$('#candidate_first_name'));i++){ await p.mouse.wheel(0,2500); await p.waitForTimeout(900); }
 await p.waitForTimeout(3000);
 const g=await p.evaluate(()=>{
   const v={};
   document.querySelectorAll('[name^="candidate[answers_attributes]"]').forEach(e=>{
     const m=e.name.match(/\[(\d+)\]\[(text|boolean|choice|choices|range|date)\]/); if(!m) return;
     const i=m[1];
     if(!v[i]) v[i]={idx:i,tipo:m[2],pergunta:'',opcoes:[]};
     v[i].tipo=m[2];
     if(m[2]==='range'){ v[i].min=e.getAttribute('min'); v[i].max=e.getAttribute('max'); v[i].step=e.getAttribute('step'); v[i].valorAtual=e.value; }
     if(m[2]==='choice'||m[2]==='choices'){
       let lab=''; if(e.id){const l=document.querySelector(`label[for="${CSS.escape(e.id)}"]`); if(l) lab=l.innerText.trim();}
       if(!lab&&e.closest('label')) lab=e.closest('label').innerText.trim();
       v[i].opcoes.push({value:e.value,label:lab.slice(0,90)});
     }
     if(!v[i].pergunta){
       let q='',x=e.closest('fieldset')||e.closest('div');
       for(let k=0;k<6&&x;k++){ const t=(x.innerText||'').replace(/\s+/g,' ').trim();
         if(t&&t.length>6&&!/^(Yes|No)\b/i.test(t)){ q=t; break; } x=x.parentElement; }
       v[i].pergunta=q.slice(0,220);
     }
   });
   return Object.values(v);
 });
 console.log(JSON.stringify(g,null,1));
 await b.close();
})();
