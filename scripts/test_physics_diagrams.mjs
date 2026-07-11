import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const manualPath = path.join(root, '低温量子光学测试系统手册.html');
const html = fs.readFileSync(manualPath, 'utf8');

function chapter(id, nextId) {
  const idPosition = html.indexOf(`id="${id}"`);
  const start = html.lastIndexOf('<section class="manual-section"', idPosition);
  const nextIdPosition = nextId ? html.indexOf(`id="${nextId}"`, start + 1) : -1;
  const end = nextId ? html.lastIndexOf('<section class="manual-section"', nextIdPosition) : html.length;
  if (start < 0 || end < 0) throw new Error(`Cannot isolate chapter ${id}`);
  return html.slice(start, end);
}

function includesAll(source, label, markers) {
  const missing = markers.filter((marker) => !source.includes(marker));
  if (missing.length) throw new Error(`${label} missing markers: ${missing.join(', ')}`);
}

const pl = chapter('pl', 'raman');
includesAll(pl, 'PL diagram', [
  'id="pl-process-diagram-v2"', '光吸收', '声子冷却', '谷内 / 谷间弛豫',
  '发光态形成', '辐射复合', '非辐射竞争', 'τ_relax ≪ τ_rad', 'X⁰', 'X±',
  '只适用于理想中性激子的一级近似', '能量与时间尺度不按比例',
  'data-formula="E_g = E_b + E_PL"', 'data-inverse="E_PL = E_g − E_b"',
  'E_PL：直接测得的 PL 峰能量', 'E_g：由模型推断的带隙'
]);

const raman = chapter('raman', 'reflectance');
includesAll(raman, 'Raman diagram', [
  'id="raman-process-diagram-v2"', '虚中间态：非稳定电子本征态',
  '产生声子', '振动态不变', '湮灭声子', 'ωS = ωL − Ω',
  'ωS = ωL', 'ωR = ωL', 'ωAS = ωL + Ω', 'ℏΩ', '玻色占据',
  '湮灭声子 · 蓝移', '振动态不变 · 弹性', '产生声子 · 红移',
  '能量与时间尺度不按比例'
]);

const circular = chapter('circular_pol', 'electrical');
includesAll(circular, 'valley-selection diagram', [
  'id="valley-selection-diagram"', '沿 +z 传播', 'σ+ → K', 'σ− → −K',
  '同谷辐射', '谷间散射', 'I++', 'I+-', 'I-+', 'I--',
  '传播或观察方向反转', '波片设置', '通道定义', '能量与时间尺度不按比例'
]);
if ((circular.match(/data-band="cb" data-curvature="up"/g) || []).length !== 2
  || (circular.match(/data-band="vb" data-curvature="down"/g) || []).length !== 2) {
  throw new Error('Both valleys must show upward-opening CB and downward-opening VB curves');
}

const renderedBody = html.slice(0, html.indexOf('<script'));
const rawMath = [...renderedBody.matchAll(/\$[^$\r\n]+\$/g)].map((match) => match[0]);
if (rawMath.length) {
  throw new Error(`Raw LaTeX delimiters remain in rendered content: ${rawMath.slice(0, 6).join(', ')}`);
}
includesAll(renderedBody, 'stable inline Zeeman symbols', [
  'E<sub>σ<sup>+</sup></sub>(B)', 'E<sub>σ<sup>−</sup></sub>(B)',
  'g<sub>eff</sub>', 'μ<sub>B</sub>', 'ΔE(B)'
]);

const svgIds = [...html.matchAll(/<svg\b[^>]*\bid="([^"]+)"/g)].map((match) => match[1]);
for (const expected of ['pl-process-diagram-v2', 'raman-process-diagram-v2', 'valley-selection-diagram']) {
  if (svgIds.filter((id) => id === expected).length !== 1) {
    throw new Error(`SVG id must be unique: ${expected}`);
  }
}

console.log('Physics diagram semantic checks passed.');
