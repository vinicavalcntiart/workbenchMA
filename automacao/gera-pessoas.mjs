#!/usr/bin/env node
/* Gera os arrays PESSOAS e PADROES do painel a partir das fontes de verdade.
 *
 * O Joe escreve em automacao/pessoas.csv e automacao/padroes-dominio.md. Se a
 * seção do painel fosse escrita à mão, ela mentiria no dia seguinte à primeira
 * rodada. Este script reescreve o trecho entre os marcadores <PESSOAS> e
 * <PADROES> do docs/index.html a partir dos arquivos, e é para ser rodado toda
 * vez que o Joe acrescentar linha.
 *
 * Uso: node automacao/gera-pessoas.mjs
 */
import fs from "node:fs";

const CSV = "automacao/pessoas.csv";
const MD = "automacao/padroes-dominio.md";
const PAGINA = "docs/index.html";

// CSV com aspas e vírgulas dentro dos campos: parser pequeno, sem dependência.
function lerCsv(txt) {
  const linhas = [];
  let campo = "", linha = [], aspas = false;
  for (let i = 0; i < txt.length; i++) {
    const c = txt[i];
    if (aspas) {
      if (c === '"') { if (txt[i + 1] === '"') { campo += '"'; i++; } else aspas = false; }
      else campo += c;
    } else if (c === '"') aspas = true;
    else if (c === ",") { linha.push(campo); campo = ""; }
    else if (c === "\n") { linha.push(campo); linhas.push(linha); linha = []; campo = ""; }
    else if (c !== "\r") campo += c;
  }
  if (campo || linha.length) { linha.push(campo); linhas.push(linha); }
  return linhas.filter(l => l.some(c => c.trim()));
}

const linhas = lerCsv(fs.readFileSync(CSV, "utf8"));
const cab = linhas[0].map(c => c.trim());
const col = n => cab.indexOf(n);

const pessoas = linhas.slice(1).map(l => ({
  data: l[col("data")] || "",
  estudio: l[col("estudio")] || "",
  pais: l[col("pais")] || "",
  pessoa: l[col("pessoa")] || "",
  cargo: l[col("cargo")] || "",
  email: l[col("email")] || "",
  confianca: (l[col("confianca")] || "").trim() || "sem-email",
  fonte: l[col("fonte")] || "",
  // Situação da abordagem: rascunho, enviado, bounce, sem via. É o que separa
  // "achamos a pessoa" de "a carta chegou nela".
  situacao: (col("situacao") >= 0 && l[col("situacao")]) || "",
}));

// Fonte costuma vir como URL crua, e a coluna é lida por gente na tela. Encurta
// para o domínio quando não houver descrição em texto, mantendo o link inteiro
// no title do elemento.
const ordem = { alta: 0, media: 1, "sem-email": 2 };
pessoas.sort((a, b) =>
  (ordem[a.confianca] ?? 9) - (ordem[b.confianca] ?? 9) ||
  a.estudio.localeCompare(b.estudio, "pt-BR"));

// padroes-dominio.md: uma linha de tabela markdown por padrão, ou nada se o
// arquivo ainda não existe (primeira rodada do Joe).
let padroes = [];
if (fs.existsSync(MD)) {
  padroes = fs.readFileSync(MD, "utf8").split("\n")
    .filter(l => l.trim().startsWith("|") && !/^\|\s*-+/.test(l.trim()))
    .map(l => l.split("|").slice(1, -1).map(c => c.trim()))
    .filter(c => c.length >= 3 && !/^dom[íi]nio$/i.test(c[0]))
    .map(([dominio, formato, ...resto]) => ({ dominio, formato, prova: resto.join(" · ") }));
}

const json = o => JSON.stringify(o, null, 1).replace(/\n /g, "\n ");
const pagina = fs.readFileSync(PAGINA, "utf8");
const troca = (txt, marca, conteudo) => {
  const ini = txt.indexOf(`// <${marca}>`);
  const fim = txt.indexOf(`// </${marca}>`);
  if (ini < 0 || fim < 0) throw new Error(`marcador ${marca} não encontrado em ${PAGINA}`);
  return txt.slice(0, ini) + `// <${marca}>\n${conteudo}\n` + txt.slice(fim);
};

let saida = troca(pagina, "PESSOAS", `const PESSOAS = ${json(pessoas)};`);
saida = troca(saida, "PADROES", `const PADROES = ${json(padroes)};`);
fs.writeFileSync(PAGINA, saida);

const por = c => pessoas.filter(p => p.confianca === c).length;
console.error(`PESSOAS: ${pessoas.length} (alta ${por("alta")}, media ${por("media")}, sem-email ${por("sem-email")}) · PADROES: ${padroes.length}`);
