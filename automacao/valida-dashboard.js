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
catch (e) { console.log('ERRO:', e.constructor.name, '-', e.message); console.log(e.stack.split('\n').slice(0,6).join('\n')); }
