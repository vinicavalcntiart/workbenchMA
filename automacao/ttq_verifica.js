// PROVA de persistencia do questionario Connect: recarrega cada slide e LE O VALOR DE VOLTA.
// Existe porque "pathname avancou" nao e prova de que a resposta gravou: nesta familia so o
// ultimo botao ("All done") faz POST, e os Next intermediarios sao navegacao pura.
const {chromium}=require('playwright'); const {abrirLocal,abrirPerfil}=require('./navegador');
const HOST=process.argv[2]; const slug=HOST.split('.')[0];
(async()=>{
 const ctx=await abrirPerfil('/home/user/apply/prof_tt_'+slug,{headless:false,args:['--disable-blink-features=AutomationControlled'],ignoreHTTPSErrors:true,viewport:{width:1280,height:1200},locale:'en-US'});
 const p=ctx.pages()[0]||await ctx.newPage();
 for(const rota of ['/connect/questions/info','/connect/questions/locations','/connect/questions/pitch']){
   await p.goto('https://'+HOST+rota,{timeout:90000,waitUntil:'domcontentloaded'});
   await p.waitForTimeout(3500);
   console.log(rota,JSON.stringify(await p.evaluate(()=>({
     campos:[...document.querySelectorAll('input,textarea')].filter(e=>!!e.offsetParent).map(e=>({
       t:e.type||e.tagName,n:e.name||e.id,
       v:(e.type==='checkbox'||e.type==='radio')?e.checked:(e.value||'').slice(0,70)}))}))));
 }
 await ctx.close();
})();
