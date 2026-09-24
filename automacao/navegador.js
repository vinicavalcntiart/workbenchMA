// NAVEGADOR UNICO DA CAMPANHA (24/09/2026, pedido do Vini: "helper unico para todos os
// scripts abrirem o navegador no padrao que a gente usa").
//
// Antes, 61 scripts chamavam chromium.launch() cada um do seu jeito (cinco variantes, duas
// delas com o proxy local fixo em 127.0.0.1:18080). Agora todo mundo abre por aqui.
//
// O PADRAO, e ele nao e parametro:
//   - stealth DESLIGADO, saida direta, sem proxy da Kernel e sem resolvedor de captcha.
//     A caixa "sou humano" e do Vini (rota do clique, CLAUDE.md). Este arquivo nunca clica,
//     nunca resolve e nunca espera um resolvedor passar por ela.
//   - navegador na nuvem nasce com 24h de porta aberta (86400 s), para o formulario
//     preenchido esperar o clique do Vini sem morrer no meio (licao da DreamWorks, 24/09).
//   - navegador local usa o proxy do ambiente (APPLY_PROXY ou HTTPS_PROXY), com o antigo
//     127.0.0.1:18080 so como ultimo recurso.
//
// USO (local, o caso dos 61 scripts):
//   const {abrirLocal}=require('./navegador');
//   const b=await abrirLocal({headless:false});     // devolve o Browser do Playwright
//   const ctx=await abrirPerfil('/home/user/apply/prof_x',{headless:false}); // com login guardado
//
// USO (nuvem, a rota do clique):
//   const {abrirKernel,fecharKernel}=require('./navegador');
//   const s=await abrirKernel({nome:'sony-character'}); // {id, cdp, aoVivo}
//   ... conectar por chromium.connectOverCDP(s.cdp), preencher tudo, conferir ...
//   console.log(s.aoVivo);   // link da tela ao vivo: vai para o Vini SO NO CHAT, nunca no repo
//   await fecharKernel(s.id);
//
// A chave da Kernel vem de KERNEL_API_KEY no ambiente. Nunca no repositorio.
const {chromium}=require('playwright');

const PORTA_ABERTA=86400;           // 24h, em segundos
const ARGS=['--no-sandbox','--ignore-certificate-errors'];

function proxyLocal(){
  return process.env.APPLY_PROXY||process.env.HTTPS_PROXY||'http://127.0.0.1:18080';
}

async function abrirLocal(o={}){
  return chromium.launch({headless:o.headless===undefined?true:o.headless,
    proxy:{server:proxyLocal()},args:ARGS.concat(o.args||[])});
}

// Perfil persistente (login guardado em /home/user/apply/prof_*): mesmo padrao, mesma saida.
async function abrirPerfil(dir,o={}){
  const {headless,args,...resto}=o;
  return chromium.launchPersistentContext(dir,{headless:headless===undefined?true:headless,
    proxy:{server:proxyLocal()},args:ARGS.concat(args||[]),...resto});
}

async function kernel(metodo,rota,corpo){
  const chave=process.env.KERNEL_API_KEY;
  if(!chave) throw new Error('navegador: KERNEL_API_KEY nao esta no ambiente (a chave nunca vai para o repositorio)');
  const r=await fetch('https://api.onkernel.com'+rota,{method:metodo,
    headers:{'Authorization':'Bearer '+chave,'Content-Type':'application/json'},
    body:corpo?JSON.stringify(corpo):undefined});
  if(!r.ok) throw new Error('navegador: Kernel '+metodo+' '+rota+' -> '+r.status+' '+(await r.text()).slice(0,200));
  return r.status===204?null:r.json();
}

async function abrirKernel(o={}){
  const s=await kernel('POST','/browsers',{
    stealth:false,                         // fixo. Nao e parametro de proposito.
    headless:false,                        // a tela ao vivo precisa existir para o Vini clicar
    timeout_seconds:o.porta||PORTA_ABERTA,
    ...(o.nome?{name:o.nome}:{})
  });
  return {id:s.session_id,cdp:s.cdp_ws_url,aoVivo:s.browser_live_view_url,bruto:s};
}

async function fecharKernel(id){ return kernel('DELETE','/browsers/'+encodeURIComponent(id)); }

module.exports={abrirLocal,abrirPerfil,abrirKernel,fecharKernel,PORTA_ABERTA};
