import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const html = fs.readFileSync(new URL('../低温量子光学测试系统手册.html', import.meta.url), 'utf8');
for (const id of ['specWavelength', 'specEnergy', 'specWavenumber', 'specSyncStatus']) {
  assert.match(html, new RegExp(`id="${id}"`));
}
assert.ok(!html.includes('id="specInputType"'), 'source-type selector must be removed');
assert.ok(!html.includes('id="specInputValue"'), 'single source input must be removed');
assert.ok(!html.includes('id="specConvertOut"'), 'text result panel must be removed');
assert.match(html, /function syncPhotonUnits\(source\)/);

const start = html.indexOf('function syncPhotonUnits(source)');
const end = html.indexOf('function estimateTime()', start);
assert.ok(start >= 0 && end > start, 'spectral conversion functions must be extractable');

function classList() {
  const values = new Set();
  return {
    add: value => values.add(value),
    remove: value => values.delete(value),
    contains: value => values.has(value),
  };
}
const elements = {
  specWavelength: { value: '620' },
  specEnergy: { value: '' },
  specWavenumber: { value: '' },
  specSyncStatus: { textContent: '', className: '' },
  rowSpecWavelength: { classList: classList() },
  rowSpecEnergy: { classList: classList() },
  rowSpecWavenumber: { classList: classList() },
  laserWl: { value: '532' },
  scatterWl: { value: '545' },
  ramanShift: { value: '448' },
  convertOut: { textContent: '' },
};
const context = {
  Number,
  $: selector => elements[selector.replace(/^#/, '')],
  fmt: (value, digits) => Number(value).toFixed(digits),
};
vm.createContext(context);
vm.runInContext(html.slice(start, end), context);

context.syncPhotonUnits('wavelength');
assert.equal(elements.specWavelength.value, '620');
assert.equal(elements.specEnergy.value, '1.999745');
assert.equal(elements.specWavenumber.value, '16129.032258');
assert.equal(elements.rowSpecWavelength.classList.contains('is-source'), true);

elements.specEnergy.value = '2.000';
context.syncPhotonUnits('energy');
assert.equal(elements.specEnergy.value, '2.000', 'source string must be preserved');
assert.equal(elements.specWavelength.value, '619.920992');
assert.equal(elements.specWavenumber.value, '16131.087879');
assert.equal(elements.rowSpecEnergy.classList.contains('is-source'), true);
assert.equal(elements.rowSpecWavelength.classList.contains('is-source'), false);

elements.specWavenumber.value = '10000';
context.syncPhotonUnits('wavenumber');
assert.equal(elements.specWavenumber.value, '10000');
assert.equal(elements.specEnergy.value, '1.239842');
assert.equal(elements.specWavelength.value, '1000.000000');

elements.specWavelength.value = '';
context.syncPhotonUnits('wavelength');
assert.equal(elements.specEnergy.value, '');
assert.equal(elements.specWavenumber.value, '');
assert.equal(elements.specSyncStatus.textContent, '');

for (const invalid of ['0', '-2', 'Infinity', 'NaN']) {
  elements.specWavelength.value = invalid;
  context.syncPhotonUnits('wavelength');
  assert.equal(elements.specEnergy.value, '');
  assert.equal(elements.specWavenumber.value, '');
  assert.match(elements.specSyncStatus.textContent, /请输入有限的正数/);
}

context.convertSpectra();
assert.match(elements.convertOut.textContent, /Raman 位移/);
assert.match(elements.convertOut.textContent, /Stokes 波长/);
elements.ramanShift.value = '20000';
context.convertSpectra();
assert.match(elements.convertOut.textContent, /不具物理意义/);

assert.ok(!html.includes('function calcDensity()'), 'calcDensity function must be removed');
assert.ok(!html.includes('id="densityOut"'), 'density output must be removed');
console.log('PASS: synchronized photon-unit inputs, validation, and Raman conversion are valid');
