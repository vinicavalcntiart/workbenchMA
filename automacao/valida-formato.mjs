#!/usr/bin/env node
/* Confere o FORMATO das linhas dos arrays de dados do painel.
 *
 * Por que existe: em 03/09 o painel publicado mostrou "19406porta6" no lugar do
 * total de emails. A causa foi uma entrada de notícia inserida dentro do array
 * DAILY em vez do NOVIDADES. O `"porta"` daquela linha entrou na soma
 * `DAILY.reduce((a,d)=>a+d[1],0)` e o JavaScript, ao somar número com texto,
 * concatena: 19 + 406 + "porta" + 6 vira "19406porta6".
 *
 * O valida-dashboard.sh não pegava isso porque a página não QUEBRA: ela mente
 * calada, que é pior. Este script confere o tipo de cada campo, e é o único
 * jeito de impedir que a mesma troca de array volte uma terceira vez.
 *
 * Uso: node automacao/valida-formato.mjs [docs/index.html]
 */
import fs from "node:fs";

const arquivo = process.argv[2] || "docs/index.html";
const src = fs.readFileSync(arquivo, "utf8");

const s = v => typeof v === "string";
const n = v => typeof v === "number" && Number.isFinite(v);

// nome do array -> [descrição legível, validador de uma linha]
const REGRAS = {
  DAILY: ["[data, emails enviados, respostas humanas]",
    r => Array.isArray(r) && r.length === 3 && s(r[0]) && /^\d{4}-\d{2}-\d{2}$/.test(r[0]) && n(r[1]) && n(r[2])],
  NOVIDADES: ["[data, tipo, título, texto, link opcional]",
    r => Array.isArray(r) && r.length >= 4 && s(r[0]) && /^\d{4}-\d{2}-\d{2}$/.test(r[0])
         && ["viva","vaga","porta","nao","alerta","envio"].includes(r[1]) && s(r[2]) && s(r[3])],
  STUDIOS: ["[nome, país, email, lote, entrega, andamento opcional]",
    r => Array.isArray(r) && r.length >= 5 && s(r[0]) && s(r[1]) && s(r[2]) && n(r[3]) && s(r[4])],
  PORTAIS: ["[nome, país, url, origem, nota, feito, prioridade]",
    r => Array.isArray(r) && r.length >= 6 && s(r[0]) && s(r[1]) && s(r[2]) && s(r[3]) && s(r[4]) && typeof r[5] === "boolean"],
  PROSPECTOS: ["[nome, onde, site, email, nota, prioridade]",
    r => Array.isArray(r) && r.length >= 6 && s(r[0]) && s(r[1])],
};

let problemas = 0;
for (const [nome, [forma, valido]] of Object.entries(REGRAS)) {
  // STUDIOS e PORTAIS terminam em "].map(...)" e não em "];", que é exatamente a
  // armadilha que já fez duas linhas caírem no array errado. Aceita os dois fins e
  // para no PRIMEIRO, senão engole o código que vem depois.
  const abre = src.indexOf(`const ${nome} = [`);
  if (abre < 0) { console.error(`AVISO: array ${nome} não encontrado, pulando`); continue; }
  const corpoIni = abre + `const ${nome} = [`.length;
  const fins = ["\n];", "\n].map", "\n ].map"]
    .map(f => src.indexOf(f, corpoIni)).filter(i => i > 0);
  if (!fins.length) { console.error(`ERRO: não achei o fim do array ${nome}`); problemas++; continue; }
  const corpo = src.slice(corpoIni, Math.min(...fins));
  let linhas;
  try { linhas = eval("[" + corpo + "]"); }
  catch (e) { console.error(`ERRO: ${nome} não é uma lista válida: ${e.message}`); problemas++; continue; }
  const maus = linhas.filter(r => !valido(r));
  if (maus.length) {
    problemas += maus.length;
    console.error(`ERRO em ${nome}: ${maus.length} linha(s) fora do formato ${forma}`);
    // A linha inteira costuma ser enorme; o começo já identifica qual é.
    maus.slice(0, 3).forEach(r => console.error("  " + JSON.stringify(r).slice(0, 160)));
    if (nome === "DAILY" && maus.some(r => Array.isArray(r) && typeof r[1] === "string"))
      console.error("  DICA: isso tem cara de entrada de NOVIDADES inserida no DAILY por engano.");
  } else {
    console.error(`ok ${nome}: ${linhas.length} linhas`);
  }
}

if (problemas) { console.error(`\nFALHOU: ${problemas} linha(s) fora do formato. Não publique assim.`); process.exit(1); }
console.error("\nOK: formato de todos os arrays confere.");
