import assert from 'node:assert/strict';
import { openPage } from './ui_test_support.mjs';

const browser = await openPage();
const send = browser.send;

await send('Page.enable');
await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 1000, deviceScaleFactor: 1, mobile: false });
const url = `http://127.0.0.1:8765/${encodeURIComponent('低温量子光学测试系统手册.html')}#pl`;
await send('Page.navigate', { url });
await new Promise((resolve) => setTimeout(resolve, 1600));

const desktop = await send('Runtime.evaluate', {
  returnByValue: true,
  expression: `(() => {
    const inspect = id => {
      const svg = document.getElementById(id);
      const rect = svg.getBoundingClientRect();
      const vb = svg.viewBox.baseVal;
      const overflow = [...svg.querySelectorAll('text')].filter(text => {
        const box = text.getBBox();
        return box.x < -2 || box.y < -2 || box.x + box.width > vb.width + 2 || box.y + box.height > vb.height + 2;
      }).map(text => text.textContent.trim());
      return { width: rect.width, height: rect.height, overflow };
    };
    return {
      diagrams: ['pl-process-diagram-v2', 'raman-process-diagram-v2', 'valley-selection-diagram'].map(inspect),
      curvatures: [...document.querySelectorAll('#valley-selection-diagram [data-curvature]')].map(path => {
        const start = path.getPointAtLength(0);
        const middle = path.getPointAtLength(path.getTotalLength() / 2);
        return { band: path.dataset.band, curvature: path.dataset.curvature, centerY: middle.y, edgeY: start.y };
      }),
      legacyPLHidden: getComputedStyle(document.getElementById('pl-process-diagram-v2-legacy').closest('figure')).display === 'none',
      legacyRamanHidden: getComputedStyle(document.querySelector('.raman-test-diagram')).display === 'none',
    };
  })()`,
});
for (const diagram of desktop.result.value.diagrams) {
  assert.ok(diagram.width > 700, `desktop diagram is too narrow: ${diagram.width}`);
  assert.ok(diagram.height > 280, `desktop diagram is too short: ${diagram.height}`);
  assert.deepEqual(diagram.overflow, [], `SVG text exceeds viewBox: ${diagram.overflow.join(', ')}`);
}
assert.equal(desktop.result.value.legacyPLHidden, true, JSON.stringify(desktop.result.value));
assert.equal(desktop.result.value.legacyRamanHidden, true, JSON.stringify(desktop.result.value));
for (const curve of desktop.result.value.curvatures) {
  if (curve.band === 'cb') assert.ok(curve.centerY > curve.edgeY, 'CB must open upward (∪)');
  if (curve.band === 'vb') assert.ok(curve.centerY < curve.edgeY, 'VB must open downward (∩)');
}

await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
await new Promise((resolve) => setTimeout(resolve, 250));
const mobile = await send('Runtime.evaluate', {
  returnByValue: true,
  expression: `(() => ['pl-process-diagram-v2', 'raman-process-diagram-v2', 'valley-selection-diagram'].map(id => document.getElementById(id).closest('figure')).map(figure => ({
    viewportSafe: figure.getBoundingClientRect().width <= innerWidth + 1,
    scrollable: figure.scrollWidth > figure.clientWidth,
    svgWidth: figure.querySelector('svg').getBoundingClientRect().width,
  })))()`,
});
for (const figure of mobile.result.value) {
  assert.equal(figure.viewportSafe, true);
  assert.equal(figure.scrollable, true);
  assert.ok(figure.svgWidth >= 759);
}

browser.close();
console.log('PASS: PL, Raman, and valley-selection diagrams render cleanly on desktop and mobile');
