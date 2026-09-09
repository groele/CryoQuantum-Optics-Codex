# Chapter 31.1 PL Plot Comparison Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild Section 31.1 so the same illustrative PL dataset clearly demonstrates why publication-grade axes, uncertainty, peak decomposition, residuals, conditions, and annotations improve scientific communication.

**Architecture:** Keep the manual as one offline HTML file. Extend the existing Chapter 31 component styles, replace only the 31.1 comparison markup and SVG content, and strengthen the existing Python validator with semantic markers that describe the new figure contract.

**Tech Stack:** Self-contained HTML5, CSS, inline SVG, Python standard-library validation, Playwright browser inspection.

## Global Constraints

- Preserve all 34 chapters, sidebar navigation, local interactivity, formulas, dark mode, print mode, and offline operation.
- Treat all plotted values as illustrative and label them “示意数据，不代表实测结果”.
- Use the same conceptual PL dataset in the low-efficiency and effective panels.
- Do not imply that a fitted component, residual, uncertainty, peak assignment, or sample condition was experimentally measured in this manual.
- The effective chart must remain readable without relying on color alone.
- Modify only `低温量子光学测试系统手册.html`, `scripts/validate_manual.py`, and this plan.

---

### Task 1: Add a failing semantic regression contract

**Files:**
- Modify: `scripts/validate_manual.py`
- Test: `scripts/validate_manual.py`

**Interfaces:**
- Consumes: the manual HTML as UTF-8 text.
- Produces: validation failure until the enhanced 31.1 figure contract exists.

- [ ] **Step 1: Extend `required_plot_markers`**

```python
required_plot_markers = [
    'id="plot_basic-31-1-comparison"',
    'class="figure-compare-grid"',
    'class="figure-panel bad"',
    'class="figure-panel good"',
    'id="plot-example-ineffective"',
    'id="plot-example-effective"',
    'class="figure-data-summary"',
    'class="figure-caption"',
    'class="figure-audit-table"',
    'data-plot-role="data-with-uncertainty"',
    'data-plot-role="residuals"',
    '残差 (data − fit)/σ',
    '示意数据，不代表实测结果',
    'id="plot_basic-31-2-formula-expression"',
    'class="equation equation-standard"',
]
```

- [ ] **Step 2: Run the validator and confirm RED**

Run: `python scripts/validate_manual.py`

Expected: exit 1 with `FAIL: chapter 31 comparison/formula markers missing` and one or more new markers listed.

### Task 2: Refine the comparison component styles

**Files:**
- Modify: `低温量子光学测试系统手册.html` in the Chapter 31 CSS block.
- Test: `scripts/validate_manual.py`

**Interfaces:**
- Consumes: existing `.figure-compare-grid`, `.figure-panel`, and `.figure-callouts` styles.
- Produces: responsive academic comparison cards, captions, data-summary chips, and a compact audit table.

- [ ] **Step 1: Add the new style contract**

```css
.figure-compare-intro {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 14px;
  align-items: start;
  margin: 12px 0 18px;
}
.figure-data-summary {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  gap: 6px;
  max-width: 360px;
}
.figure-data-summary span {
  padding: 4px 8px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--paper2);
  color: var(--muted);
  font-size: 0.74rem;
  font-weight: 700;
  line-height: 1.3;
}
.figure-panel svg {
  aspect-ratio: 560 / 420;
}
.figure-caption {
  margin: -2px 2px 0;
  color: var(--muted);
  font-size: 0.84rem;
  line-height: 1.55;
}
.figure-audit-table {
  width: 100%;
  margin: 18px 0 22px;
  border-collapse: separate;
  border-spacing: 0;
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 10px;
  font-size: 0.9rem;
}
.figure-audit-table th,
.figure-audit-table td {
  padding: 10px 12px;
  border-bottom: 1px solid var(--line);
  vertical-align: top;
  text-align: left;
}
.figure-audit-table tr:last-child td {
  border-bottom: 0;
}
.figure-audit-table th {
  background: var(--paper2);
}
.figure-audit-table td:first-child {
  width: 16%;
  color: var(--accent);
  font-weight: 800;
}
@media (max-width: 900px) {
  .figure-compare-intro {
    grid-template-columns: 1fr;
  }
  .figure-data-summary {
    justify-content: flex-start;
    max-width: none;
  }
}
@media print {
  .figure-panel,
  .figure-audit-table {
    break-inside: avoid;
    box-shadow: none;
  }
}
```

- [ ] **Step 2: Confirm the validator remains RED for missing markup**

Run: `python scripts/validate_manual.py`

Expected: exit 1 for missing 31.1 HTML markers, demonstrating that CSS alone does not satisfy the regression contract.

### Task 3: Rebuild the two PL plots and explanatory copy

**Files:**
- Modify: `低温量子光学测试系统手册.html` around `id="plot_basic-31-1-comparison"`.
- Test: `scripts/validate_manual.py`

**Interfaces:**
- Consumes: the styles from Task 2 and the existing illustrative two-peak PL concept.
- Produces: two semantic SVG panels using a shared energy range of 1.80–2.04 eV and a shared two-peak profile.

- [ ] **Step 1: Replace the introductory paragraph with a shared-data statement**

```html
<div class="figure-compare-intro">
  <p>下面两图表达同一组双峰 PL 示意数据。左图故意保留论文中常见的表达缺陷；右图不改变峰形和趋势，只补齐数据层、模型层、不确定度、残差与测试条件，使读者能够判断“数据是否支持拟合”，而不只是看到一条平滑曲线。</p>
  <div class="figure-data-summary" aria-label="示意数据条件">
    <span>单层 TMD</span><span>10 K</span><span>532 nm</span><span>50 μW</span><span>mean ± s.d.</span>
  </div>
</div>
```

- [ ] **Step 2: Rebuild the low-efficiency SVG**

Use `id="plot-example-ineffective"` and `viewBox="0 0 560 420"`. Draw the shared two-peak profile as two thick red/green lines, retain incomplete axes and overlapping legend, and add numbered callouts for missing units, color-only encoding, occluded peak region, absent uncertainty, and absent residual/conditions. The panel caption must state that the visual defects are intentional teaching examples.

- [ ] **Step 3: Rebuild the effective SVG**

Use `id="plot-example-effective"` and `viewBox="0 0 560 420"`. The main plot occupies `x=84..526`, `y=60..286`; the aligned residual strip occupies `x=84..526`, `y=320..374`. Include:

```html
<g data-plot-role="data-with-uncertainty" aria-label="实验点和标准差误差棒"></g>
<g data-plot-role="fit-components" aria-label="总拟合与分峰拟合"></g>
<g data-plot-role="residuals" aria-label="归一化残差"></g>
<text>残差 (data − fit)/σ</text>
<text>示意数据，不代表实测结果</text>
```

Render raw data as dark circular markers with vertical error bars, the total fit as a solid near-black line, X− and X0 components as blue dashed and vermilion dash-dot lines, and direct peak labels containing both state and illustrative energy. Add a zero line and ±2σ guide band in the residual strip. Put the legend in unused upper-right space and repeat distinctions with line style, not color alone.

- [ ] **Step 4: Replace three generic callouts with five evidence-focused callouts**

The low-efficiency panel covers axes, encoding, occlusion, uncertainty, and reproducibility. The effective panel covers complete axes, data/model layering, uncertainty, residual diagnostics, and conditions/traceability.

- [ ] **Step 5: Add the compact audit table**

```html
<table class="figure-audit-table">
  <thead><tr><th>检查维度</th><th>低效表达</th><th>有效表达</th><th>科学意义</th></tr></thead>
  <tbody>
    <tr><td>坐标</td><td>变量和单位缺失</td><td>变量、单位、刻度方向完整</td><td>避免把归一化量误读为绝对强度</td></tr>
    <tr><td>数据与模型</td><td>粗线混在一起</td><td>散点、总拟合、分峰分层</td><td>拟合不能伪装成原始数据</td></tr>
    <tr><td>不确定度</td><td>无误差和样本口径</td><td>误差棒与 mean ± s.d. 明示</td><td>读者能判断差异是否超过测量散布</td></tr>
    <tr><td>拟合质量</td><td>只展示平滑曲线</td><td>残差、零线与 ±2σ 参考带</td><td>暴露系统偏差、漏峰和模型失配</td></tr>
    <tr><td>可复现性</td><td>无样品与测试条件</td><td>材料、温度、激发波长和功率齐全</td><td>图可与原始记录和方法部分对应</td></tr>
  </tbody>
</table>
```

- [ ] **Step 6: Run the validator and confirm GREEN**

Run: `python scripts/validate_manual.py`

Expected: exit 0 with `PASS: manual structure is valid`.

### Task 4: Browser and responsive verification

**Files:**
- Verify: `低温量子光学测试系统手册.html`
- Output: `output/playwright/` only when screenshots are needed.

**Interfaces:**
- Consumes: final offline HTML.
- Produces: evidence that 31.1 is readable and aligned in the rendered page.

- [ ] **Step 1: Open the local HTML and navigate to 31.1**

Open the file URL with Playwright, take a fresh snapshot, and navigate to `#plot_basic-31-1-comparison`.

- [ ] **Step 2: Verify the desktop layout**

At approximately 1440 px viewport width, confirm both panels sit side by side, SVG text is not clipped, the residual strip is aligned to the main x-axis, and the audit table fits the content column.

- [ ] **Step 3: Verify the narrow layout**

At approximately 390 px viewport width, confirm panels stack, captions remain readable, SVGs scale without horizontal overflow, and the summary chips wrap.

- [ ] **Step 4: Verify light and dark themes**

Confirm both exported-figure canvases remain intentionally white while surrounding cards, captions, badges, and the audit table retain sufficient contrast.

- [ ] **Step 5: Run final automated checks**

Run: `python scripts/validate_manual.py`

Run: `git diff --check -- scripts/validate_manual.py 低温量子光学测试系统手册.html`

Expected: validator PASS and `git diff --check` exits 0.
