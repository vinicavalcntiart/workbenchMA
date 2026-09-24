// Preenchedor de formulario proprio com campos por name/id. Uso: sh hb_run.sh apply_own.js <respostas.json> <slug> [--submit]
// json: {"url","campos":{"#id":"valor"},"selects":{"#position":"3D Generalist"},"botao":"SUBMIT"}
// O telefone entra como __TEL__ e vem de VINI_TEL: o repositorio e publico.
const {chromium}=require('playwright'); const {abrirLocal}=require('./navegador'); const fs=require('fs');
const [ansFile,slug,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const A=JSON.parse(fs.readFileSync(ansFile)); const D=__dirname;
// 19/09 (25o turno): o marcador __ENDERECO__ entrou aqui pelo mesmo motivo do __TEL__, e a
// falta dele quase custou uma candidatura: o General Application da Wonder Works (Breezy) tem
// `Address*` OBRIGATORIO e o unico jeito de responder sem escrever o endereco residencial num
// arquivo de repositorio PUBLICO e este. Os dois marcadores caem no pessoal.json de
// /home/user/apply (fora do repositorio), como o apply-greenhouse.js ja fazia desde 16/09.
const PESSOAL=(()=>{ try{ return JSON.parse(fs.readFileSync('/home/user/apply/pessoal.json','utf8')); }catch(e){ return {}; } })();
for(const k of Object.keys(A.campos||{})){
  if(A.campos[k]==='__TEL__'){
    const t=process.env.VINI_TEL||PESSOAL.telefone_internacional||PESSOAL.telefone_normal;
    if(!t){ console.error('[erro] o arquivo pede __TEL__ e nao ha telefone nem em VINI_TEL nem em pessoal.json'); process.exit(1); }
    A.campos[k]=t;
  }
  if(A.campos[k]==='__ENDERECO__'){
    const e1=process.env.VINI_END||PESSOAL.endereco1;
    if(!e1){ console.error('[erro] o arquivo pede __ENDERECO__ e nao ha endereco nem em VINI_END nem em pessoal.json'); process.exit(1); }
    A.campos[k]=e1;
  }
}
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await abrirLocal({headless:false});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1400,height:2600},locale:'en-US',
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 // LICAO DE 09/09 NA FUTURE ASSOCIATE: a primeira versao so escutava 'response' e o log saiu
 // LIMPO, sem POST nenhum, enquanto o texto da tela casava com a regex de sucesso. Ou seja: o
 // verificador disse "positivo" sobre uma pagina que nao tinha enviado nada. Escutar tambem
 // 'request' e 'requestfailed' separa as tres coisas que o log antigo confundia: nao clicou,
 // clicou e o pedido falhou, clicou e o servidor respondeu.
 p.on('request',r=>{ if(r.method()==='POST') log('[pedido POST]', r.url().slice(0,110)); });
 p.on('requestfailed',r=>{ if(r.method()==='POST') log('[pedido POST FALHOU]', r.url().slice(0,110), r.failure()&&r.failure().errorText); });
 p.on('response',async r=>{ if(r.request().method()==='POST'&&!/analytics|sentry|gtag|facebook/i.test(r.url())){ let t=''; try{t=(await r.text()).slice(0,220);}catch(e){} log('[rede POST]',r.status(),r.url().slice(0,100),t.replace(/\s+/g,' ')); } });
 try{
  await p.goto(A.url,{waitUntil:'domcontentloaded',timeout:120000}); await p.waitForTimeout(7000);
  for(const t of ['Accept','Accept All','I agree','Got it','OK']){ const e=p.getByRole('button',{name:new RegExp('^'+t+'$','i')}).first();
    if(await e.count().catch(()=>0)){ await e.click().catch(()=>{}); await p.waitForTimeout(1200); break; } }
  // 18/09 20h50: tres capacidades acrescentadas a ESTE script (nenhum arquivo novo) para
  // atravessar formulario de ATS com anexo, questionario de radio e SECOES, como o Breezy:
  //  "arquivos": {"<seletor de input[type=file]>":"<nome do arquivo em /home/user/apply>"}
  //  "marcar":   ["<seletor de checkbox ou radio>"] -> check({force}) porque o ATS esconde
  //              o input e desenha um rotulo por cima
  //  "proximo":  "<seletor do botao que avanca de secao>" + "passos": N
  // Por que a passada repete: no Breezy as secoes moram no MESMO DOM com ng-show, entao o
  // seletor ACHA o campo e o Playwright nao consegue digitar nele enquanto a secao esta
  // escondida. Preencher o que esta visivel, avancar e repetir e o unico caminho. O botao
  // de ENVIO nunca e clicado aqui: "proximo" e seletor proprio (nextSection()), e o envio
  // fica no bloco --submit. A prova de que cada campo entrou e lida DE VOLTA, nunca assumida.
  const feito=new Set();
  const passada=async(n)=>{
    for(const [sel,v] of Object.entries(A.selects||{})){
      if(feito.has('s'+sel)) continue;
      const el=await p.$(sel); if(!el) continue;
      if(!await el.isVisible().catch(()=>false)) continue;
      await el.scrollIntoViewIfNeeded().catch(()=>{});
      await el.selectOption({label:v}).catch(async()=>{ await el.selectOption(v).catch(()=>{}); });
      feito.add('s'+sel); log('select',sel,'=>',await el.inputValue().catch(()=>'?'));
    }
    for(const [sel,v] of Object.entries(A.campos||{})){
      if(feito.has('c'+sel)) continue;
      const el=await p.$(sel); if(!el) continue;
      if(!await el.isVisible().catch(()=>false)) continue;
      await el.scrollIntoViewIfNeeded().catch(()=>{});
      await el.click({force:true}).catch(()=>{}); await el.fill('').catch(()=>{});
      await el.type(String(v),{delay:3}).catch(()=>{});
      const lido=await el.inputValue().catch(()=>'');
      if(lido.length) feito.add('c'+sel);
      log('campo',sel, lido.length? '('+lido.length+' chars) '+lido.slice(0,50) : '(NAO ENTROU NADA)');
    }
    for(const [sel,arq] of Object.entries(A.arquivos||{})){
      if(feito.has('a'+sel)) continue;
      const el=await p.$(sel); if(!el) continue;
      await el.setInputFiles(D+'/'+arq).catch(e=>log('falha no anexo',sel,e.message.split('\n')[0]));
      const nm=await p.$eval(sel,e=>e.files&&e.files.length?e.files[0].name+' '+e.files[0].size+'B':'(ZERO ARQUIVO)').catch(()=>'?');
      if(nm!=='(ZERO ARQUIVO)') feito.add('a'+sel);
      log('arquivo',sel,'=>',nm); await p.waitForTimeout(4000);
    }
    for(const sel of (A.marcar||[])){
      if(feito.has('m'+sel)) continue;
      const el=await p.$(sel); if(!el) continue;
      await el.scrollIntoViewIfNeeded().catch(()=>{});
      await el.check({force:true}).catch(async()=>{ await el.click({force:true}).catch(()=>{}); });
      const ck=await p.$eval(sel,e=>e.checked).catch(()=>'?');
      if(ck===true) feito.add('m'+sel);
      log('marcar',sel,'=>',ck);
    }
    const faltam=[...Object.keys(A.selects||{}).map(s=>'s'+s),...Object.keys(A.campos||{}).map(s=>'c'+s),
                  ...Object.keys(A.arquivos||{}).map(s=>'a'+s),...(A.marcar||[]).map(s=>'m'+s)]
                  .filter(k=>!feito.has(k));
    log('passada',n,'| ainda faltam',faltam.length, faltam.length?JSON.stringify(faltam.slice(0,6)):'');
    return faltam.length;
  };
  const passos=A.proximo? (A.passos||4) : 1;
  for(let i=1;i<=passos;i++){
    const faltam=await passada(i);
    if(!faltam || i===passos || !A.proximo) break;
    const nx=p.locator(A.proximo).first();
    if(!(await nx.count().catch(()=>0))){ log('nao ha mais botao de avancar'); break; }
    const rot=((await nx.innerText().catch(()=>''))||'').trim();
    await nx.click({force:true}).catch(e=>log('falha ao avancar',e.message.split('\n')[0]));
    await p.waitForTimeout(2500); log('avancei de secao ->',rot);
  }
  await p.waitForTimeout(1200);
  // leitura de volta imediatamente antes do clique: formulario que redesenha apaga campo em silencio
  let vazio=false;
  for(const sel of Object.keys(A.campos||{})){ const v=await p.$eval(sel,e=>e.value).catch(()=>null);
    if(v===null||!String(v).trim()){ log('  leitura final',sel,'=>',v===null?'(CAMPO SUMIU)':'(VAZIO)'); vazio=true; }
    else log('  leitura final',sel,'=>',String(v).length,'chars'); }
  if(vazio) log('!! PARE: obrigatorio vazio na leitura final');
  await p.screenshot({path:D+'/own_'+slug+'_pre.png',fullPage:true}).catch(()=>{});
  log('captcha iframes:',JSON.stringify(await p.$$eval('iframe',fs=>fs.map(f=>f.src).filter(s=>/recaptcha|hcaptcha|turnstile|datadome/i.test(s))).catch(()=>[])));
  if(!SUBMIT){ log('MODO SECO, nada enviado'); await b.close(); return; }
  const sb=await p.$('button:has-text("'+(A.botao||'SUBMIT')+'"), input[type=submit], button[type=submit]');
  if(!sb){ log('!! nao achei o botao de envio'); await b.close(); return; }
  await sb.scrollIntoViewIfNeeded().catch(()=>{}); await p.waitForTimeout(900);
  const cx=await sb.boundingBox().catch(()=>null); log('caixa do botao:',JSON.stringify(cx));
  if(cx) await p.mouse.click(cx.x+cx.width/2, cx.y+cx.height/2).catch(()=>{}); else await sb.click({force:true}).catch(()=>{});
  await p.waitForTimeout(15000);
  const txt=(await p.innerText('body')).replace(/\s+/g,' ');
  const chal=await p.$$eval('iframe',fs=>fs.filter(f=>/hcaptcha|recaptcha/i.test(f.src)&&f.getBoundingClientRect().height>100).length).catch(()=>0);
  await p.screenshot({path:D+'/own_'+slug+'_post.png',fullPage:true}).catch(()=>{});
  // 20/09 (JHON A, 37o turno): a regua de sucesso so entendia INGLES. Ela marcou a PVP como
  // NAO CONFIRMADA com a tela dizendo, em letras grandes, "Votre candidature a ete envoyee.
  // Merci!" - ou seja o servidor confirmou e o medidor disse que nao. Tela de sucesso em casa
  // francofona, hispanofona ou germanofona e sucesso igual, e a campanha ja tem casa francesa
  // (NOID, PVP), quebequense e alema na fila.
  // DUAS decisoes de implementacao, as duas para evitar falso positivo barato:
  //  1) o texto e NORMALIZADO (NFD, diacritico removido, minuscula) antes de casar. Assim
  //     "envoyee", "envoyee" e "ENVOYEE" caem no mesmo termo ASCII e a lista nao precisa de
  //     duas grafias por palavra. /i sozinho NAO normaliza acento.
  //  2) cada termo casa com FRONTEIRA de nao-alfanumerico dos dois lados. Sem isso "recu"
  //     acenderia dentro de "recueil" e "envoye" dentro de qualquer flexao.
  // E a regua agora DIZ QUAL termo acendeu: positivo por "merci" sozinho num rodape e coisa
  // muito diferente de positivo por "candidature a ete envoyee", e quem le o log precisa
  // distinguir os dois sem reabrir a pagina.
  const TERMOS_OK=[
    // ingles (os que ja existiam, nenhum removido)
    'thank you','thanks','submitted','received','success',"we'll be in touch",
    'confirm your human','in touch soon','well received',
    // frances
    'envoyee','envoye','recue','recu','bien recue','merci','enregistree','enregistre',
    'candidature a ete','nous avons bien','transmise','prise en compte',
    // espanhol
    'enviada','enviado','recibida','recibido','gracias','registrada','hemos recibido',
    // alemao
    'gesendet','erhalten','danke','vielen dank','eingegangen','ubermittelt','erfolgreich'
  ];
  const normal=txt.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();
  const achados=TERMOS_OK.filter(t=>new RegExp('(^|[^a-z0-9])'+t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'([^a-z0-9]|$)').test(normal));
  const ok=achados.length>0;
  log(ok?'RESPOSTA POSITIVA NA TELA (leia o texto)':'NAO CONFIRMADA','| termos que acenderam:',JSON.stringify(achados),'| desafio visivel:',chal,'| url:',p.url());
  log('TEXTO COMPLETO:',txt.slice(0,2500));
 }catch(e){ log('ERR',e.message.split('\n')[0]); await p.screenshot({path:D+'/own_'+slug+'_err.png',fullPage:true}).catch(()=>{}); }
 await b.close();
})();
