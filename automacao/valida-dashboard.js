const el = new Proxy({}, {
  get: (t, k) => {
    if (k === 'innerHTML' || k === 'textContent' || k === 'value' || k === 'className') return '';
    if (k === 'style' || k === 'dataset' || k === 'classList') return new Proxy({}, {get:()=>()=>{}, set:()=>true});
    if (k === 'options') return [];
    if (k === 'querySelectorAll' || k === 'querySelector') return () => [];
    return () => el;
  },
  set: () => true
});
global.document = {
  querySelector: () => el, querySelectorAll: () => [],
  getElementById: () => el, addEventListener: () => {},
  createElement: () => el, body: el, documentElement: el,
  readyState: 'complete'
};
global.window = { addEventListener: () => {}, location: { hash: '' }, matchMedia: () => ({matches:false, addEventListener(){}}) };
global.localStorage = { getItem: () => null, setItem: () => {}, removeItem: () => {} };
global.navigator = { clipboard: { writeText: async () => {} }, userAgent: 'node' };
global.addEventListener = () => {};
global.matchMedia = () => ({matches:false, addEventListener(){}});
global.getComputedStyle = () => ({ getPropertyValue: () => '#000' });
try { require('./app.js'); console.log('OK: script rodou sem lançar'); }
catch (e) {
  console.error('ERRO:', e.constructor.name, '-', e.message);
  console.error(e.stack.split('\n').slice(0, 6).join('\n'));
  // Em 03/09 este passo detectou a página quebrada e mesmo assim saiu com sucesso.
  // O `set -e` do script de shell não tinha o que pegar, e quem olhou só o fim da
  // saída viu o "OK" do segundo passo e publicou um painel que não renderizava nada.
  // Falhar de verdade é o que torna a validação uma trava em vez de um comentário.
  process.exit(1);
}
