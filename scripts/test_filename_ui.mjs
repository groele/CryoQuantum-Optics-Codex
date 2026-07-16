import assert from 'node:assert/strict';
import { openPage } from './ui_test_support.mjs';

const browser = await openPage();
const send = browser.send;

await send('Page.enable');
await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride', {
  width: 1440, height: 1000, deviceScaleFactor: 1, mobile: false,
});
const url = `http://127.0.0.1:8765/${encodeURIComponent('低温量子光学测试系统手册.html')}#toolbox`;
await send('Page.navigate', { url });
await new Promise(resolve => setTimeout(resolve, 1800));

const evaluated = await send('Runtime.evaluate', {
  returnByValue: true,
  expression: `(() => {
    document.querySelector('[data-panel="naming"]').click();
    const panel = document.querySelector('#panel-naming');
    const input = document.querySelector('.filename-generator-input');
    const output = document.querySelector('.filename-generator-output');
    const inputBox = input.getBoundingClientRect();
    const outputBox = output.getBoundingClientRect();
    document.querySelector('#fnType').value = 'CircularPol';
    document.querySelector('#fnRegion').value = 'R03';
    document.querySelector('#fnT').value = '2';
    document.querySelector('#fnB').value = '+9';
    updateFilenameForm();
    const circular = document.querySelector('#filenameOut').textContent;
    document.querySelector('#fnType').value = 'LinearPolPL';
    document.querySelector('#fnB').value = '+9';
    updateFilenameForm();
    document.querySelector('#fnPol').value = 'Pol045deg';
    makeFilename();
    const linearPL = document.querySelector('#filenameOut').textContent;
    const linearBVisible = getComputedStyle(document.querySelector('#lbl_fnB')).display !== 'none';
    document.querySelector('#fnType').value = 'LinearPolRaman';
    updateFilenameForm();
    document.querySelector('#fnPol').value = 'Pol090deg';
    makeFilename();
    const linearRaman = document.querySelector('#filenameOut').textContent;
    document.querySelector('#fnType').value = 'PL';
    document.querySelector('#fnRegion').value = 'R01';
    document.querySelector('#fnT').value = '1.65';
    updateFilenameForm();
    const decimal = document.querySelector('#filenameOut').textContent;
    return {
      panelActive: panel.classList.contains('active'),
      inputVisible: getComputedStyle(input).display !== 'none',
      outputVisible: getComputedStyle(output).display !== 'none',
      sameRow: Math.abs(inputBox.top - outputBox.top) < 3,
      balanced: outputBox.width / inputBox.width > 0.9 && outputBox.width / inputBox.width < 1.1,
      separated: outputBox.left > inputBox.right,
      circular,
      linearPL,
      linearRaman,
      linearBVisible,
      decimal,
    };
  })()`,
});
const result = evaluated.result.value;
assert.equal(result.panelActive, true);
assert.equal(result.inputVisible, true);
assert.equal(result.outputVisible, true);
assert.equal(result.sameRow, true);
assert.equal(result.balanced, true);
assert.equal(result.separated, true);
assert.equal(result.circular, 'PL_CP_1L_MoS2_R03_45_0_+9T_2K');
assert.equal(result.linearPL, 'PL_LP_1L_MoS2_R03_Pol045deg_+9T_2K');
assert.equal(result.linearRaman, 'Raman_LP_1L_MoS2_R03_1800g_Pol090deg_+9T_2K');
assert.equal(result.linearBVisible, true);
assert.equal(result.decimal, 'PL_1L_MoS2_R01_1.65K');

await send('Emulation.setDeviceMetricsOverride', {
  width: 700, height: 1000, deviceScaleFactor: 1, mobile: false,
});
await new Promise(resolve => setTimeout(resolve, 150));
const mobileEvaluated = await send('Runtime.evaluate', {
  returnByValue: true,
  expression: `(() => {
    const inputBox = document.querySelector('.filename-generator-input').getBoundingClientRect();
    const outputBox = document.querySelector('.filename-generator-output').getBoundingClientRect();
    return {
      stacked: outputBox.top > inputBox.bottom,
      aligned: Math.abs(inputBox.left - outputBox.left) < 3,
      equalWidth: Math.abs(inputBox.width - outputBox.width) < 3,
    };
  })()`,
});
assert.deepEqual(mobileEvaluated.result.value, {
  stacked: true,
  aligned: true,
  equalWidth: true,
});

await send('Emulation.setDeviceMetricsOverride', {
  width: 1440, height: 1000, deviceScaleFactor: 1, mobile: false,
});
await new Promise(resolve => setTimeout(resolve, 150));
const timeEvaluated = await send('Runtime.evaluate', {
  returnByValue: true,
  expression: `(() => {
    document.querySelector('[data-panel="time-estimate"]').click();
    estimateTime();
    const panel = document.querySelector('#panel-time-estimate');
    const input = panel.querySelector('.time-estimate-input');
    const output = panel.querySelector('.time-estimate-output');
    const inputBox = input.getBoundingClientRect();
    const outputBox = output.getBoundingClientRect();
    return {
      panelActive: panel.classList.contains('active'),
      sameRow: Math.abs(inputBox.top - outputBox.top) < 3,
      balanced: outputBox.width / inputBox.width > 0.9 && outputBox.width / inputBox.width < 1.1,
      result: document.querySelector('#timeOut').textContent,
    };
  })()`,
});
assert.equal(timeEvaluated.result.value.panelActive, true);
assert.equal(timeEvaluated.result.value.sameRow, true);
assert.equal(timeEvaluated.result.value.balanced, true);
assert.match(timeEvaluated.result.value.result, /总光谱数：160/);
assert.match(timeEvaluated.result.value.result, /44\.2 min/);
assert.match(timeEvaluated.result.value.result, /0\.74 h/);

const mergedAndConversion = await send('Runtime.evaluate', {
  returnByValue: true,
  expression: `(() => {
    document.querySelector('[data-panel="wizard"]').click();
    const wizard = document.querySelector('#panel-wizard');
    const reference = wizard.querySelector('.wizard-reference-section');
    const merged = wizard.classList.contains('active') && !!reference && !document.querySelector('#panel-test-reference');
    document.querySelector('[data-panel="convert"]').click();
    document.querySelector('#specWavelength').value = '620';
    syncPhotonUnits('wavelength');
    const convertPanel = document.querySelector('#panel-convert');
    const left = convertPanel.querySelector('.spectral-unit-card').getBoundingClientRect();
    const right = convertPanel.querySelector('.raman-convert-card').getBoundingClientRect();
    return {
      merged,
      convertActive: convertPanel.classList.contains('active'),
      sameRow: Math.abs(left.top - right.top) < 3,
      balanced: right.width / left.width > 0.9 && right.width / left.width < 1.1,
      energy: document.querySelector('#specEnergy').value,
      wavenumber: document.querySelector('#specWavenumber').value,
      sourceHighlighted: document.querySelector('#rowSpecWavelength').classList.contains('is-source'),
      densityRemoved: !document.querySelector('#densityOut'),
    };
  })()`,
});
assert.equal(mergedAndConversion.result.value.merged, true);
assert.equal(mergedAndConversion.result.value.convertActive, true);
assert.equal(mergedAndConversion.result.value.sameRow, true);
assert.equal(mergedAndConversion.result.value.balanced, true);
assert.equal(mergedAndConversion.result.value.energy, '1.999745');
assert.equal(mergedAndConversion.result.value.wavenumber, '16129.032258');
assert.equal(mergedAndConversion.result.value.sourceHighlighted, true);
assert.equal(mergedAndConversion.result.value.densityRemoved, true);
browser.close();
console.log('PASS: toolbox modules, merged guidance, spectral conversion, and responsive layouts are functional');
