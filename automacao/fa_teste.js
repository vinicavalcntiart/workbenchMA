// EXPERIMENTO NAO DESTRUTIVO. A pagina da Future Associate manda o registro de verdade por
// GET no Apps Script (mode no-cors, fire and forget) e a notificacao por POST no web3forms
// dentro de try/catch VAZIO. Depois disso ela escreve "Application Received" na tela SEM
// OLHAR se algum dos dois funcionou. Ou seja: a tela mente por construcao.
// Este script clica no Submit mas INTERCEPTA e ABORTA os dois pedidos, so para responder uma
// pergunta: o navegador chega a EMITIR o GET do Apps Script? Se emite, as duas tentativas de
// antes tambem emitiram e o estudio ja tem o registro. Se nao emite, nao chegou nada.
// Nenhuma linha nova e criada porque nada sai da maquina.
const {chromium}=require('playwright'); const fs=require('fs');
const A=JSON.parse(fs.readFileSync('ans_futureassoc.json'));
for(const k of Object.keys(A.campos)) if(A.campos[k]==='__TEL__') A.campos[k]=process.env.VINI_TEL;
const log=(...a)=>console.log('[fa-teste]',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1400,height:2600},locale:'en-US',
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 let viuSheet=false, viuW3=false;
 await p.route('**script.google.com/**', r=>{ viuSheet=true; log('>>> o navegador EMITIU o GET do Apps Script:', r.request().method(), r.request().url().slice(0,150)); r.abort(); });
 await p.route('**api.web3forms.com/**', r=>{ viuW3=true; log('>>> o navegador EMITIU o POST do web3forms'); r.abort(); });
 await p.goto(A.url,{waitUntil:'domcontentloaded',timeout:120000}); await p.waitForTimeout(7000);
 await p.selectOption('#position',{label:'3D Generalist'}).catch(()=>{});
 for(const [sel,v] of Object.entries(A.campos)){ const el=await p.$(sel); if(el){ await el.fill(String(v)).catch(()=>{}); } }
 const sb=await p.$('button:has-text("SUBMIT")');
 await sb.scrollIntoViewIfNeeded().catch(()=>{}); await p.waitForTimeout(600);
 const cx=await sb.boundingBox(); await p.mouse.click(cx.x+cx.width/2, cx.y+cx.height/2);
 await p.waitForTimeout(9000);
 log('VEREDITO | GET do Apps Script emitido:', viuSheet, '| POST do web3forms emitido:', viuW3);
 log('tela depois do clique:', (await p.innerText('body')).replace(/\s+/g,' ').slice(0,220));
 await b.close();
})().catch(e=>console.log('ERR',e.message));
