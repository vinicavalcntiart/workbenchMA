// Testa se o parametro size= do anchor do reCAPTCHA discrimina parede de nao-parede.
// O briefing PROIBE grep pela palavra recaptcha como criterio, porque ela vem no pacote global
// e nunca libera nada. A pergunta aqui e outra: o size= do widget REALMENTE carregado separa
// "invisible" (que a automacao ja atravessou hoje) de "normal" (caixa de desafio)?
const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1300,height:2400},locale:'en-US',
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 await p.goto(process.argv[2],{waitUntil:'domcontentloaded',timeout:120000}).catch(()=>{});
 await p.waitForTimeout(12000);
 const anchors=await p.$$eval('iframe',fs=>fs.map(f=>f.src).filter(s=>/recaptcha.*anchor/i.test(s)));
 for(const a of anchors){
   const u=new URL(a);
   console.log('  anchor | size=',u.searchParams.get('size'),'| badge=',u.searchParams.get('badge'),'| host=',u.host);
 }
 if(!anchors.length) console.log('  nenhum anchor de reCAPTCHA carregado nesta pagina');
 const bframe=await p.$$eval('iframe',fs=>fs.filter(f=>/bframe/i.test(f.src)).map(f=>({h:f.getBoundingClientRect().height,vis:f.offsetParent!==null})));
 console.log('  bframes:',JSON.stringify(bframe));
 await b.close();
})().catch(e=>console.log('ERR',e.message));
