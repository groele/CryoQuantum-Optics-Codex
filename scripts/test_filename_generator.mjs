import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const html = fs.readFileSync(new URL('../低温量子光学测试系统手册.html', import.meta.url), 'utf8');
const start = html.indexOf('function updateFilenameForm()');
const end = html.indexOf('function initChecks()', start);
assert.ok(start >= 0 && end > start, 'filename-generator functions must be extractable');

const values = {
  fnType: 'PL',
  fnMaterial: 'MoS2',
  fnLayer: '1L',
  fnRegion: 'R01',
  fnT: '1.65',
  fnB: '+9',
  fnV: '+1.0',
  fnP: '0.05mW',
  fnPol: '45_0',
  fnGrating: '1800g',
};

const elements = {};
for (const [id, value] of Object.entries(values)) {
  elements[id] = {
    value,
    style: {},
    options: [],
    addEventListener() {},
    appendChild(option) { this.options.push(option); },
  };
}
for (const id of [
  'lbl_fnGrating', 'lbl_fnPol', 'lbl_fnP', 'lbl_fnV', 'lbl_fnB',
  'fnConditionsWrap', 'filenameOut',
]) {
  elements[id] ??= { style: {}, textContent: '' };
}
Object.defineProperty(elements.fnPol, 'innerHTML', {
  set() { this.options = []; },
});

const context = {
  console,
  document: { createElement: () => ({ value: '', textContent: '' }) },
  $: selector => elements[selector.replace(/^#/, '')] ?? null,
};
vm.createContext(context);
vm.runInContext(html.slice(start, end), context);

function generate(type, overrides = {}) {
  Object.assign(elements.fnType, { value: type });
  for (const [id, value] of Object.entries(overrides)) elements[id].value = value;
  context.updateFilenameForm();
  return elements.filenameOut.textContent;
}

const optionOrder = [...html.matchAll(
  /<option value="(PL|CircularPol|LinearPolPL|Raman|LinearPolRaman|PowerDep|MagnetDep|GateDep|TempDep|Reflect)">/g,
)].map(match => match[1]);
assert.deepEqual(optionOrder, [
  'PL', 'CircularPol', 'LinearPolPL', 'Raman', 'LinearPolRaman',
  'PowerDep', 'MagnetDep', 'GateDep', 'TempDep', 'Reflect',
]);

assert.equal(generate('PL'), 'PL_1L_MoS2_R01_1.65K');
assert.equal(generate('CircularPol', { fnRegion: 'R03', fnT: '2', fnB: '+9' }), 'PL_CP_1L_MoS2_R03_45_0_+9T_2K');
assert.equal(generate('LinearPolPL', { fnRegion: 'R01', fnT: '1.65' }), 'PL_LP_1L_MoS2_R01_1.65K');
elements.fnPol.value = 'Pol045deg';
context.makeFilename();
assert.equal(elements.filenameOut.textContent, 'PL_LP_1L_MoS2_R01_Pol045deg_1.65K');
assert.equal(generate('LinearPolRaman', { fnRegion: 'R03', fnT: '2', fnPol: '' }), 'Raman_LP_1L_MoS2_R03_1800g_2K');

for (const type of optionOrder) {
  assert.ok(!generate(type).includes('.csv'), `${type} must not append .csv`);
}

assert.ok(!html.includes('data-panel="test-reference"'), 'standalone test-reference tab must be removed');
assert.ok(!html.includes('id="panel-test-reference"'), 'standalone test-reference panel must be removed');
const wizardPanel = html.slice(html.indexOf('id="panel-wizard"'), html.indexOf('id="panel-four"'));
assert.match(wizardPanel, /class="wizard-reference-section"/);
assert.match(wizardPanel, /测试数据内容参考/);
assert.match(html, /class="tool-card filename-generator-input"/);
assert.match(html, /class="tool-card filename-generator-output"/);
assert.match(html, /输入变化后自动刷新/);
assert.match(html, /无可靠变化时可略过重复测试/);
assert.match(html, /data-panel="naming">命名规范<\/button>/);
assert.match(html, /id="panel-naming"/);
assert.match(html, /data-panel="time-estimate">采集时间估算<\/button>/);
assert.match(html, /id="panel-time-estimate"/);
assert.ok(!html.includes('data-panel="acq"'), 'legacy acq tab must be removed');
assert.ok(!html.includes('>采集规划</button>'), 'legacy 采集规划 tab label must be removed');
const namingChapter = html.slice(
  html.indexOf('id="sample_labels"'),
  html.indexOf('id="pl"'),
);
for (const match of namingChapter.matchAll(/<span class="field-name">([^<]+)<\/span>/g)) {
  assert.ok(!match[1].endsWith('.csv'), `chapter 5 naming example must omit .csv: ${match[1]}`);
}
for (const marker of [
  'PL_1L_MoS2_R01_1.65K',
  'PL_CP_1L_MoS2_R01_45_0_+9T_1.65K',
  'PL_LP_1L_MoS2_R01_1.65K',
  'Raman_1L_MoS2_R01_1800g_1.65K',
  'Raman_LP_1L_MoS2_R01_1800g_1.65K',
]) {
  assert.ok(namingChapter.includes(marker), `chapter 5 must include ${marker}`);
}
console.log('PASS: filename generator behavior, compact layout, and merged experiment guidance are valid');
