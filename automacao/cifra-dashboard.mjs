#!/usr/bin/env node
/* Cifra o dashboard para publicação.
 *
 * O site do GitHub Pages é público para quem tem o endereço, e o painel carrega
 * dados pessoais do Vini (kit de aplicação, pretensão salarial, histórico de
 * candidatura). Este script troca a página publicada por uma tela de senha em
 * que o conteúdo vai CIFRADO de verdade: quem abrir o código-fonte encontra só
 * bytes embaralhados, não o painel escondido atrás de um if.
 *
 * AES-256-GCM com chave derivada da senha por PBKDF2-SHA256, 310 mil iterações,
 * sal e IV aleatórios a cada build. A senha nunca é gravada em arquivo nenhum:
 * entra por variável de ambiente e sai da memória junto com o processo.
 *
 * Uso:
 *   DASHBOARD_SENHA='...' node automacao/cifra-dashboard.mjs docs/index.html saida.html
 */
import crypto from "node:crypto";
import fs from "node:fs";

const senha = process.env.DASHBOARD_SENHA;
if (!senha) {
  console.error("ERRO: defina DASHBOARD_SENHA. Nada foi gravado.");
  process.exit(1);
}

const entrada = process.argv[2] || "docs/index.html";
const saida = process.argv[3] || "index.html";
// O painel traz o marcador __BUILD__ no lugar do carimbo de publicação. Ele é
// trocado aqui, na hora de cifrar, para que o site sempre mostre quando aquela
// versão foi publicada de verdade, sem ninguém precisar editar a data à mão.
const agora = new Date();
const dois = n => String(n).padStart(2, "0");
const carimbo = `${dois(agora.getUTCDate())}/${dois(agora.getUTCMonth() + 1)} às ${dois(agora.getUTCHours())}h${dois(agora.getUTCMinutes())} UTC`;
const plano = Buffer.from(fs.readFileSync(entrada, "utf8").replaceAll("__BUILD__", carimbo), "utf8");

const ITERACOES = 310000;
const sal = crypto.randomBytes(16);
const iv = crypto.randomBytes(12);
const chave = crypto.pbkdf2Sync(senha, sal, ITERACOES, 32, "sha256");
const cifra = crypto.createCipheriv("aes-256-gcm", chave, iv);
// WebCrypto espera ciphertext e tag grudados, então já saem concatenados.
const corpo = Buffer.concat([cifra.update(plano), cifra.final(), cifra.getAuthTag()]);

const b64 = b => b.toString("base64");

const pagina = `<title>Campanha do Vini</title>
<meta name="robots" content="noindex, nofollow">
<style>
  :root { color-scheme: light dark; --bg:#f6f7f9; --card:#fff; --ink:#12151a; --ink2:#5b6472; --linha:#d8dde5; --acento:#2f6df6; --erro:#c0392b; }
  @media (prefers-color-scheme: dark) {
    :root { --bg:#0e1014; --card:#161a21; --ink:#e8ecf2; --ink2:#98a2b3; --linha:#252b35; --acento:#5b8cff; --erro:#ff6b5e; }
  }
  body { margin:0; min-height:100vh; display:grid; place-items:center; background:var(--bg); color:var(--ink);
         font:14px/1.55 ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; padding:24px; }
  .caixa { width:100%; max-width:340px; background:var(--card); border:1px solid var(--linha); border-radius:14px; padding:26px 24px; }
  h1 { font-size:16px; margin:0 0 4px; }
  p.sub { margin:0 0 18px; color:var(--ink2); font-size:12.5px; }
  input[type=password] { width:100%; box-sizing:border-box; padding:10px 12px; font-size:15px; border-radius:9px;
         border:1px solid var(--linha); background:var(--bg); color:var(--ink); }
  input[type=password]:focus { outline:2px solid var(--acento); outline-offset:1px; border-color:transparent; }
  button { width:100%; margin-top:12px; padding:10px 12px; font-size:14px; font-weight:600; border:0; border-radius:9px;
         background:var(--acento); color:#fff; cursor:pointer; }
  button:disabled { opacity:.6; cursor:progress; }
  label.lembrar { display:flex; align-items:center; gap:7px; margin-top:12px; color:var(--ink2); font-size:12.5px; cursor:pointer; }
  .erro { margin-top:12px; color:var(--erro); font-size:12.5px; min-height:1em; }
</style>
<div class="caixa">
  <h1>🔒 Campanha do Vini</h1>
  <p class="sub">Painel privado. Digite a senha para abrir.</p>
  <form id="f">
    <input id="s" type="password" autocomplete="current-password" placeholder="senha" autofocus>
    <label class="lembrar"><input id="lembrar" type="checkbox" checked> lembrar neste navegador</label>
    <button id="b" type="submit">Abrir</button>
    <div class="erro" id="e" role="alert"></div>
  </form>
</div>
<script>
(function(){
  var SAL = "${b64(sal)}", IV = "${b64(iv)}", DADOS = "${b64(corpo)}", ITER = ${ITERACOES};
  var CHAVE_LS = "campanha-senha-v1";
  var bytes = function(b64){ var s = atob(b64), a = new Uint8Array(s.length);
    for(var i=0;i<s.length;i++) a[i] = s.charCodeAt(i); return a; };

  function guardada(){ try { return localStorage.getItem(CHAVE_LS) || sessionStorage.getItem(CHAVE_LS); } catch(e){ return null; } }
  function guardar(senha, persistir){
    try { (persistir ? localStorage : sessionStorage).setItem(CHAVE_LS, senha); } catch(e){}
  }
  function esquecer(){ try { localStorage.removeItem(CHAVE_LS); sessionStorage.removeItem(CHAVE_LS); } catch(e){} }

  async function abrir(senha){
    var base = await crypto.subtle.importKey("raw", new TextEncoder().encode(senha), "PBKDF2", false, ["deriveKey"]);
    var chave = await crypto.subtle.deriveKey(
      { name:"PBKDF2", salt: bytes(SAL), iterations: ITER, hash:"SHA-256" },
      base, { name:"AES-GCM", length:256 }, false, ["decrypt"]);
    var claro = await crypto.subtle.decrypt({ name:"AES-GCM", iv: bytes(IV) }, chave, bytes(DADOS));
    return new TextDecoder().decode(claro);
  }

  function mostrar(html){
    document.open(); document.write(html); document.close();
    // botãozinho de sair, colado depois que o painel já escreveu a si mesmo
    setTimeout(function(){
      var a = document.createElement("button");
      a.textContent = "🔒 sair";
      a.style.cssText = "position:fixed; right:14px; bottom:14px; z-index:9999; padding:7px 12px; font-size:12px;" +
        "border-radius:8px; border:1px solid rgba(128,128,128,.4); background:rgba(128,128,128,.14);" +
        "color:inherit; cursor:pointer; font-family:inherit;";
      a.onclick = function(){ esquecer(); location.reload(); };
      document.body.appendChild(a);
    }, 0);
  }

  var f = document.getElementById("f"), s = document.getElementById("s"),
      b = document.getElementById("b"), e = document.getElementById("e");

  f.addEventListener("submit", async function(ev){
    ev.preventDefault();
    e.textContent = ""; b.disabled = true; b.textContent = "abrindo...";
    try {
      var html = await abrir(s.value);
      guardar(s.value, document.getElementById("lembrar").checked);
      mostrar(html);
    } catch(err) {
      e.textContent = "Senha errada.";
      b.disabled = false; b.textContent = "Abrir"; s.select();
    }
  });

  var salva = guardada();
  if(salva) abrir(salva).then(mostrar).catch(esquecer);
})();
</script>
`;

fs.writeFileSync(saida, pagina);
const kb = n => (n / 1024).toFixed(0) + " KB";
console.error(`cifrado: ${entrada} (${kb(plano.length)}) -> ${saida} (${kb(pagina.length)})`);
