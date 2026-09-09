# Chapter 12.2 Zeeman Explanation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the formula-only Section 12.2 with a beginner-readable but scientifically bounded explanation of Zeeman splitting and effective g-factor extraction.

**Architecture:** Keep the manual as one offline HTML file. Reuse existing concept-diagram, theory-note, equation, process-step, and callout styles; add only small Zeeman-specific layout rules where the existing components cannot express an aligned energy-level diagram or numbered extraction sequence. Strengthen the Python validator with semantic content markers before modifying the section.

**Tech Stack:** Self-contained HTML5, CSS, inline SVG, existing equation markup, Python validation, ImageMagick SVG rendering.

## Global Constraints

- Preserve the 34-chapter structure, navigation, formulas, interactive tools, offline mode, dark mode, mobile layout, and print behavior.
- Define ΔE as Eσ+ − Eσ− throughout Section 12.2.
- Label the energy-level graphic and numerical calculation as illustrative, not measured data.
- Treat the square-root fine-structure equation as a conditional two-level model, not a universal free-TMD-exciton law.
- Keep deeper microscopic g-factor contributions in Chapter 16 and link to `#magneto-16-1-zeeman`.
- Do not modify unrelated chapters or overwrite existing uncommitted work.

---

### Task 1: Add a failing semantic regression contract

**Files:**
- Modify: `scripts/validate_manual.py`
- Test: `scripts/validate_manual.py`

**Interfaces:**
- Consumes: the manual HTML as UTF-8 text.
- Produces: a validation failure until Section 12.2 contains the full explanation contract.

- [ ] **Step 1: Add the required Section 12.2 markers**

```python
required_zeeman_explanation_markers = [
    'class="zeeman-intuition"',
    'aria-label="Zeeman 分裂物理图像"',
    '磁矩与磁场耦合',
    '示意图，不代表实测数据',
    'class="zeeman-sign-note"',
    'class="zeeman-example"',
    '−0.230 meV/T',
    '≈ −3.97',
    'class="zeeman-extraction-steps"',
    'class="zeeman-special-case"',
    '强度差不是 Zeeman 能量分裂',
    'href="#magneto-16-1-zeeman"',
]
missing_zeeman_explanation_markers = [
    marker for marker in required_zeeman_explanation_markers if marker not in html
]
if missing_zeeman_explanation_markers:
    fail(
        "chapter 12.2 Zeeman explanation markers missing: "
        + ", ".join(repr(marker) for marker in missing_zeeman_explanation_markers)
    )
```

- [ ] **Step 2: Run the validator and confirm RED**

Run: `$env:PYTHONIOENCODING='utf-8'; python scripts/validate_manual.py`

Expected: exit 1 with `FAIL: chapter 12.2 Zeeman explanation markers missing`.

### Task 2: Add the Zeeman teaching layout

**Files:**
- Modify: `低温量子光学测试系统手册.html` in the component CSS area.
- Test: `scripts/validate_manual.py`

**Interfaces:**
- Consumes: existing theme variables and manual-section responsive behavior.
- Produces: two-column intuition cards, a responsive energy-level diagram, sign/example callouts, and a five-step extraction sequence.

- [ ] **Step 1: Add narrowly scoped styles**

```css
.zeeman-intuition {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  margin: 14px 0 18px;
}
.zeeman-intuition > div,
.zeeman-example,
.zeeman-sign-note,
.zeeman-special-case {
  padding: 14px 16px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--paper2);
}
.zeeman-intuition strong,
.zeeman-extraction-steps strong {
  display: block;
  margin-bottom: 5px;
  color: var(--accent);
}
.zeeman-sign-note {
  border-left: 4px solid var(--warn);
  background: rgba(245, 158, 11, 0.08);
}
.zeeman-example {
  border-left: 4px solid var(--accent2);
  background: rgba(var(--accent2-rgb), 0.07);
}
.zeeman-special-case {
  border-left: 4px solid var(--muted);
}
.zeeman-extraction-steps {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 8px;
  margin: 14px 0 20px;
  counter-reset: zeeman-step;
}
.zeeman-extraction-steps > div {
  counter-increment: zeeman-step;
  padding: 12px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: var(--paper);
}
.zeeman-extraction-steps > div::before {
  content: counter(zeeman-step, decimal-leading-zero);
  display: block;
  margin-bottom: 6px;
  color: var(--accent2);
  font-weight: 900;
}
@media (max-width: 900px) {
  .zeeman-intuition,
  .zeeman-extraction-steps {
    grid-template-columns: 1fr;
  }
}
```

- [ ] **Step 2: Confirm the validator remains RED for missing content markers**

Run: `$env:PYTHONIOENCODING='utf-8'; python scripts/validate_manual.py`

Expected: exit 1 because CSS alone does not satisfy the Section 12.2 content contract.

### Task 3: Rewrite Section 12.2

**Files:**
- Modify: `低温量子光学测试系统手册.html` from `id="magneto-12-2-zeeman-分裂与-g-因子"` up to the next h2.
- Test: `scripts/validate_manual.py`

**Interfaces:**
- Consumes: the design spec, existing equation components, and styles from Task 2.
- Produces: a complete intuition-to-analysis teaching sequence.

- [ ] **Step 1: Add the physical-intuition introduction**

Explain magnetic-moment coupling and why time-reversal-related valley states move oppositely in an out-of-plane magnetic field. State that circular polarization maps these states into σ+ and σ− detection channels only after the laboratory convention is fixed.

- [ ] **Step 2: Insert the energy-level and spectrum-readout diagram**

Use an inline SVG inside `concept-diagram` with `aria-label="Zeeman 分裂物理图像"`. Show B = 0 degeneracy, B > 0 opposite energy shifts, ΔE, and σ+/σ− peak readout. Include the visible caption `示意图，不代表实测数据`.

- [ ] **Step 3: Reorder and annotate the formulas**

Keep these equations in order:

```text
ΔE(B) = Eσ+(B) − Eσ−(B)
ΔE(B) = geff μB B + ΔE0
geff = (dΔE/dB) / μB
μB = 57.8838 μeV/T = 0.0578838 meV/T
```

Place a prose explanation directly before and after each equation. Explain that ΔE uses fitted peak energies, geff is dimensionless, the slope carries energy-per-field units, and ΔE0 is an intercept that may include residual splitting or systematic offset.

- [ ] **Step 4: Add the sign-convention and numerical-example callouts**

The sign callout must state that reversing the subtraction order or field convention reverses the sign of geff. The example must calculate `−0.230 / 0.0578838 ≈ −3.97` and label the numbers as illustrative.

- [ ] **Step 5: Add the five-step extraction sequence and common mistakes**

Sequence: fit Eσ± at every B; compute same-state ΔE; inspect ΔE–B linearity and residuals; convert slope to geff with uncertainty; report intercept and conventions. Common mistakes include using intensity difference as splitting, mixing exciton species, using a broad-spectrum centroid, and forcing one line across nonlinear or hysteretic data.

- [ ] **Step 6: Reframe the square-root equation as a special case**

Place the existing square-root equation inside `class="zeeman-special-case"`. Define δ as a zero-field coupling/fine-structure energy and require independent zero-field evidence before using the model.

- [ ] **Step 7: Link to Chapter 16 and run GREEN verification**

Add a final link to `#magneto-16-1-zeeman` for microscopic contributions. Run the validator.

Expected: `PASS: manual structure is valid`.

### Task 4: Scientific and rendering verification

**Files:**
- Verify: `低温量子光学测试系统手册.html`
- Verify: `scripts/validate_manual.py`

**Interfaces:**
- Consumes: completed Section 12.2.
- Produces: evidence that the science, units, structure, and diagram are coherent.

- [ ] **Step 1: Verify numerical and unit consistency**

Run a Python assertion that `round(-0.230 / 0.0578838, 2) == -3.97` and confirm μB appears in both μeV/T and meV/T.

- [ ] **Step 2: Verify the Section 12.2 DOM contract**

Parse the manual with BeautifulSoup and assert one intuition block, one diagram, one sign note, one example, five extraction steps, one special-case block, and one Chapter 16 link.

- [ ] **Step 3: Render the Zeeman SVG offline**

Extract the SVG with `aria-label="Zeeman 分裂物理图像"` and pipe it to ImageMagick. Expected: exit 0 without an SVG parse or font error.

- [ ] **Step 4: Run final repository checks**

Run: `$env:PYTHONIOENCODING='utf-8'; python scripts/validate_manual.py`

Run: `git diff --check -- scripts/validate_manual.py 低温量子光学测试系统手册.html`

Expected: validation PASS and diff check exit 0.
