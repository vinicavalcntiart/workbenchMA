#!/usr/bin/env node
/* Injeta automacao/preencher-formulario.js dentro do painel.
 *
 * Por que existe: o codigo do preenchedor tem que existir em UM lugar so. Se ele
 * fosse escrito a mao dentro do docs/index.html, a versao do arquivo .js e a do
 * painel divergiriam na primeira correcao, e a que o Vini usa e a do painel.
 *
 * Uso: node automacao/gera-preenchedor.mjs
 */
import fs from "node:fs";

const FONTE = "automacao/preencher-formulario.js";
const PAGINA = "docs/index.html";
const ABRE = "/*<PREENCHEDOR>*/";
const FECHA = "/*</PREENCHEDOR>*/";

const src = fs.readFileSync(FONTE, "utf8");

// Sanidade: o placeholder do telefone precisa continuar existindo, senao o
// gerador do painel troca nada e o favorito sai sem numero, falhando so na hora
// em que ele estiver com o formulario aberto na frente.
const MARCA = "@@TELEFONE@@";
const ocorrencias = src.split(MARCA).length - 1;
if (ocorrencias !== 1) {
  // Tem que ser exatamente uma. Na primeira versao o marcador aparecia tambem no
  // comentario do cabecalho e a troca caiu la, gerando favorito sem telefone.
  console.error("ERRO: " + FONTE + " tem " + ocorrencias + " ocorrencias de " + MARCA + "; precisa ser exatamente 1.");
  process.exit(1);
}
if (/\b(salario|salary) atual da E-Line/i.test(src)) {
  console.error("ERRO: o preenchedor nao pode carregar o salario da E-Line.");
  process.exit(1);
}

let html = fs.readFileSync(PAGINA, "utf8");
const i = html.indexOf(ABRE), j = html.indexOf(FECHA);
if (i < 0 || j < 0 || j < i) {
  console.error("ERRO: marcadores " + ABRE + " ... " + FECHA + " nao encontrados em " + PAGINA);
  process.exit(1);
}

// JSON.stringify resolve aspas, barras e quebras de linha de uma vez, o que evita
// o buraco classico de embutir codigo em template literal e o codigo trazer crase.
const literal = JSON.stringify(src);
html = html.slice(0, i + ABRE.length) + literal + html.slice(j);
fs.writeFileSync(PAGINA, html);

console.log("preenchedor injetado: " + src.length + " caracteres de " + FONTE);
