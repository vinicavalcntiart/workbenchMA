const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:3000},userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-GB'})).newPage();
 await p.goto(process.argv[2],{timeout:120000,waitUntil:'networkidle'}).catch(()=>{});
 await p.waitForTimeout(9000);
 const links=await p.evaluate(()=>[...new Set([...document.querySelectorAll('a')].map(a=>((a.innerText||'').replace(/\s+/g,' ').trim().slice(0,60))+' >> '+(a.href||'')))]);
 links.filter(l=>/pinpoint|apply|job|career|posting/i.test(l)).slice(0,40).forEach(l=>console.log(' ',l));
 const frames=p.frames().map(f=>f.url()).filter(u=>u&&u!=='about:blank');
 console.log('FRAMES:',JSON.stringify(frames));
 for(const f of p.frames()){
   if(!/pinpoint/i.test(f.url())) continue;
   const l2=await f.evaluate(()=>[...document.querySelectorAll('a')].map(a=>((a.innerText||'').trim().slice(0,60))+' >> '+(a.href||''))).catch(()=>[]);
   console.log('DENTRO DO FRAME PINPOINT:'); l2.slice(0,30).forEach(x=>console.log('   ',x));
 }
 await b.close();
})();
