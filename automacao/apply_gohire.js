// GoHire. Familia de ATS NOVA para a campanha, mapeada em 09/09 na Makeshift Software.
// Uso: VINI_TEL='<so digitos>' sh hb_run.sh apply_gohire.js <url-da-vaga> <slug> <cover.txt> [--submit]
//
// O QUE CUSTOU DUAS SONDAS ATE FICAR CLARO, e por isso esta escrito aqui:
// 1. curl na pagina da vaga devolve 200 e ZERO campo. A pagina e casca; o formulario nao esta
//    nela. "200 no curl de SPA e a casca, nao a porta."
// 2. O botao Apply Now NAO e <a> nem <button>: e <div onclick="apply()">, e apply() chama
//    gohire("open", <id>, "") do script widget.gohire.io.
// 3. O formulario abre num IFRAME em app.gohire.io/widget/<hash>/<id>. Ler o frame principal
//    devolve "sem campos" e da falso negativo. E pior: o frame principal tem SEIS inputs
//    invisiveis do tradutor do Google, entao escolher frame "pelo que tem mais campos" cai
//    neles. O criterio certo e o ENDERECO do frame.
// 4. Nenhum captcha no DOM depois do clique. Mas quem da veredito e o clique no Submit.
const {chromium}=require('playwright'); const fs=require('fs');
const [url,slug,coverFile,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const D=__dirname;
const TEL=process.env.VINI_TEL;
if(!TEL){ console.error('[erro] falta VINI_TEL; o valor mora no documento privado do Drive'); process.exit(1); }
const B={first:'Vini', last:'Cavalcanti', email:'contact@vinicavalcanti.art', tel:TEL,
         art:'https://www.artstation.com/viniciuscavalcanti',
         cv:D+'/Vini_Cavalcanti_CV.pdf'};
const carta=fs.readFileSync(coverFile,'utf8').trim();
const log=(...a)=>console.log('['+slug+']',...a);

(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2200},acceptDownloads:true,locale:'en-US',
  userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'});
 const p=await ctx.newPage();
 p.on('response', async r=>{ try{ if(r.request().method()!=='GET' && /gohire/.test(r.url())) log('[rede]', r.status(), r.request().method(), r.url().slice(0,120)); }catch(_){} });

 await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'}).catch(()=>{});
 await p.waitForTimeout(6000);
 const bt=p.locator('[onclick*="apply"]').first();
 if(await bt.count().catch(()=>0)) await bt.click({force:true}).catch(()=>{});
 await p.waitForTimeout(4000);
 const idVaga=(url.match(/-(\d+)\/?$/)||[])[1];
 if(idVaga) await p.evaluate(id=>{ try{ if(typeof gohire==='function') gohire('open',Number(id),''); }catch(e){} }, idVaga).catch(()=>{});
 await p.waitForTimeout(9000);

 let f=null;
 for(const fr of p.frames()) if(/app\.gohire\.io\/widget\//.test(fr.url())) { f=fr; break; }
 if(!f){ log('!! formulario nao abriu: nenhum frame app.gohire.io/widget'); await p.screenshot({path:D+'/err_'+slug+'.png',fullPage:true}).catch(()=>{}); await b.close(); return; }
 log('frame do formulario:', f.url().slice(0,120));

 const põe=async(sel,valor,rotulo)=>{
   const el=await f.$(sel);
   if(!el){ log('campo ausente:',rotulo); return false; }
   await el.fill(valor).catch(async()=>{ await el.click({force:true}).catch(()=>{}); await f.type(sel,valor,{delay:20}).catch(()=>{}); });
   return true;
 };
 await põe('#first-name',B.first,'nome');
 await põe('#last-name',B.last,'sobrenome');
 await põe('#email',B.email,'email');

 // TELEFONE: a regra do documento privado depende do formulario ter ou nao SELETOR DE PAIS
 // separado. Com seletor, so os digitos; sem seletor, formato internacional. Aqui a decisao
 // e medida no DOM em vez de presumida, porque presumir errado faz a validacao recusar.
 const temSeletorPais=await f.evaluate(()=>!!document.querySelector('.iti__selected-country, .iti__flag-container, select[name*="country" i], [class*="country-select" i]'));
 log('seletor de pais separado no formulario?', temSeletorPais);
 if(temSeletorPais){
   // Com seletor, ele nasce num pais qualquer (costuma ser o do IP). Escolher Brasil ANTES
   // de digitar, senao o numero sai com bandeira errada e ninguem avisa.
   // MEDIDO: o widget usa ngx-intl-tel-input com o conjunto de classes ANTIGO do
     // intl-tel-input, ou seja .iti__selected-flag e nao .iti__selected-country, e ele NASCE
     // em US (div class="iti__flag iti__us"). Sem trocar, o telefone sai como numero dos EUA.
   const cont=await f.$('.iti__selected-flag, .iti__selected-country, .iti__flag-container');
   if(cont){
     await cont.click({force:true}).catch(()=>{});
     await p.waitForTimeout(1200);
     const busca=await f.$('input[class*="search" i], .iti__search-input');
     if(busca){ await busca.fill('Brazil').catch(()=>{}); await p.waitForTimeout(1000); }
     const op=await f.$('li[id*="item-br"], .iti__country[data-country-code="br"], li[data-country-code="br"]');
     if(op) await op.click({force:true}).catch(()=>{});
     else await f.locator('li:has-text("Brazil")').first().click({force:true}).catch(()=>{});
     await p.waitForTimeout(900);
   }
   const bandeira=await f.evaluate(()=>{
     const e=document.querySelector('.iti__selected-flag .iti__flag, .iti__selected-country .iti__flag');
     if(e) return (e.className||'').replace('iti__flag','').trim();
     const s2=document.querySelector('.iti__selected-flag, .iti__selected-country');
     return s2?(s2.getAttribute('title')||s2.innerText||'').replace(/\s+/g,' ').trim().slice(0,40):'(sem)';
   }).catch(()=>'(erro)');
   log('bandeira do telefone =>', bandeira);
 }
 await põe('#phone', temSeletorPais ? B.tel : '+55'+B.tel, 'telefone');

 // REDE DE SEGURANCA DO TELEFONE, e ela e o que de fato resolveu na Makeshift: clicar na
 // bandeira do ngx-intl-tel-input nao trocou o pais (a lista e um dropdown do ngx-bootstrap e
 // o clique programatico nao abre). O componente, porem, RECONHECE o prefixo digitado: escrever
 // +55 no proprio campo troca a bandeira sozinho. Entao a regra aqui e: se depois de tudo a
 // bandeira nao for br, reescreve o numero em formato internacional e confere de novo. Numero
 // com bandeira errada nao levanta erro nenhum, sai como telefone dos EUA e ninguem avisa.
 const leBandeira=async()=>f.evaluate(()=>{
   const e=document.querySelector('.iti__selected-flag .iti__flag, .iti__selected-country .iti__flag');
   return e?(e.className||'').replace('iti__flag','').trim():'(sem)';
 }).catch(()=>'(erro)');
 if(temSeletorPais && !/iti__br/.test(await leBandeira())){
   log('bandeira ainda nao e br; reescrevendo o numero em formato internacional');
   const el=await f.$('#phone');
   if(el){ await el.fill('').catch(()=>{}); await el.type('+55'+B.tel,{delay:60}).catch(()=>{}); await p.waitForTimeout(1500); }
   log('bandeira depois do formato internacional =>', await leBandeira());
 }

 const anexo=await f.$('#attach');
 if(anexo) await anexo.setInputFiles(B.cv).catch(e=>log('anexo falhou:',e.message.slice(0,70)));

 // MEDIDO EM 09/09: o id da textarea da carta NAO sobrevive ao re-render do widget, entao
 // tanto f.$('#cover_letter') quanto o getAttribute('id') falharam, e a carta foi parar no
 // campo errado enquanto o campo do portfolio recebeu a mesma coisa. O que sobrevive e o
 // ROTULO. Identificar campo por rotulo, e nao por id, e a licao.
 const areas=await f.$$('textarea');
 for(const t of areas){
   const rot=await t.evaluate(e=>{
     let s='';
     if(e.id){ const l=document.querySelector('label[for="'+CSS.escape(e.id)+'"]'); if(l) s=l.innerText; }
     if(!s){ const l=e.closest('label'); if(l) s=l.innerText; }
     if(!s){ const w=e.closest('div,li,fieldset'); if(w) s=w.innerText; }
     return (s||e.placeholder||'').replace(/\s+/g,' ').trim().slice(0,90);
   }).catch(()=>'');
   const alvoTexto = /cover letter|motiva|why|message/i.test(rot) ? carta : B.art;
   await t.fill(alvoTexto).catch(()=>{});
   log('textarea', JSON.stringify(rot), '=>', alvoTexto===carta ? 'CARTA' : 'ArtStation');
 }
 await p.waitForTimeout(1500);

 const leitura=await f.evaluate(()=>{
   const out={};
   document.querySelectorAll('input:not([type=hidden]),textarea').forEach((e,i)=>{
     const k=e.id||e.name||('campo'+i);
     out[k]= e.type==='file' ? (e.files&&e.files.length?e.files[0].name:'(VAZIO)') : ((e.value||'').slice(0,70)||'(VAZIO)');
   });
   return out;
 });
 for(const k of Object.keys(leitura)) log('  leitura de volta', k, '=>', leitura[k]);
 await p.screenshot({path:D+'/filled_'+slug+'.png',fullPage:true}).catch(()=>{});

 if(!SUBMIT){ log('ENSAIO, nada enviado'); await b.close(); return; }

 // O widget nao usa <button type=submit>: o envio e um <div> ou <a> com classe do proprio
 // GoHire. Listar o que existe antes de desistir e o que separa "sem botao" de "botao com
 // outro nome", que sao diagnosticos completamente diferentes.
 const botoes=await f.evaluate(()=>[...document.querySelectorAll('button,input[type=submit],a,div[class*=btn i],div[class*=button i],[role=button]')]
   .map(e=>({tag:e.tagName, tipo:e.type||'', cls:(e.className||'').toString().slice(0,60), txt:(e.innerText||e.value||'').replace(/\s+/g,' ').trim().slice(0,40)}))
   .filter(x=>x.txt));
 log('botoes no formulario:', JSON.stringify(botoes).slice(0,700));
 // O :has-text casa tambem ANCESTRAL que contem a palavra, e clicar no ancestral nao envia
 // nada. O alvo tem que ser o elemento cujo texto E "Submit", e no GoHire ele e
 // div.btn.primary-btn.gh-widget-btn.
 let env=f.locator('div.gh-widget-btn.primary-btn, button[type=submit], input[type=submit]')
          .filter({hasText:/^\s*(Submit|Apply)\s*$/i}).first();
 if(!(await env.count().catch(()=>0)))
   env=f.getByText(/^\s*Submit\s*$/).last();
 if(!(await env.count().catch(()=>0))){ log('!! botao de envio nao encontrado'); await p.screenshot({path:D+'/err_'+slug+'.png',fullPage:true}).catch(()=>{}); await b.close(); return; }
 // force:true dispara o evento sem mover o ponteiro, e o botao do GoHire fica FORA da area
 // visivel do modal: o clique ia para o vazio e nao acontecia nada, sem erro nenhum na tela,
 // que e o pior tipo de falha. Rolar ate o botao e clicar de verdade.
 await env.scrollIntoViewIfNeeded().catch(()=>{});
 await p.waitForTimeout(800);
 const cx=await env.boundingBox().catch(()=>null);
 log('caixa do botao Submit:', JSON.stringify(cx));
 if(cx) await p.mouse.click(cx.x+cx.width/2, cx.y+cx.height/2).catch(()=>{});
 else await env.click().catch(()=>{});
 await p.waitForTimeout(14000);
 const erros=await f.evaluate(()=>[...document.querySelectorAll('[class*="error" i],[class*="invalid" i],.ng-invalid.ng-touched')]
   .map(e=>(e.innerText||'').replace(/\s+/g,' ').trim()).filter(Boolean).slice(0,8));
 if(erros.length) log('erros de validacao na tela:', JSON.stringify(erros));
 const txt=(await f.evaluate(()=>document.body.innerText).catch(()=>'')).replace(/\s+/g,' ');
 // FALSO NEGATIVO PAGO DUAS VEZES NA CAMPANHA: a Scopely confirma com "Application Sent!" e o
 // GoHire tambem, e a regex antiga nao pegava nenhuma das duas. Marcar como NAO CONFIRMADA uma
 // candidatura que FOI enviada e o erro mais caro que existe aqui, porque leva a reenviar.
 const ok=/thank you|application (has been |was )?(submitted|received|sent)|application sent|we('ve| have) received|thanks for applying|successfully/i.test(txt);
 await p.screenshot({path:D+'/result_'+slug+'.png',fullPage:true}).catch(()=>{});
 log(ok?'ENVIADA':'NAO CONFIRMADA','| texto:', txt.slice(0,320));
 await b.close();
})();
