const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1300,height:2600},locale:'en-US',
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 await p.goto(process.argv[2],{waitUntil:'domcontentloaded',timeout:120000}).catch(()=>{});
 await p.waitForTimeout(6000);
 for(let t=0;t<5;t++){ const loc=p.getByText('Apply for This Job',{exact:false});
   if(await loc.count().catch(()=>0)){ await loc.first().click({timeout:15000}).catch(()=>{}); await p.waitForTimeout(8000); break; }
   await p.waitForTimeout(3000); }
 await p.waitForTimeout(6000);
 const anchors=await p.$$eval('iframe',fs=>fs.map(f=>f.src).filter(s=>/recaptcha.*anchor/i.test(s)));
 for(const a of anchors){ const u=new URL(a); console.log('  anchor | size=',u.searchParams.get('size'),'| host=',u.host); }
 if(!anchors.length) console.log('  nenhum anchor carregado');
 console.log('  bframes:',JSON.stringify(await p.$$eval('iframe',fs=>fs.filter(f=>/bframe/i.test(f.src)).map(f=>({h:Math.round(f.getBoundingClientRect().height)})))));
 await b.close();
})().catch(e=>console.log('ERR',e.message));
