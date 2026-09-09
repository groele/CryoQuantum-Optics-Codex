# Merge Experiment Guide and Expand Spectral Conversion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Merge experiment guidance into one toolbox child module and replace the density calculator with rigorous energy, wavelength, and absolute-wavenumber conversion.

**Architecture:** Preserve the existing single-file manual and generic tab system. Move the reference-card markup inside `panel-wizard`; add a new pure browser function `convertPhotonUnits()` beside the retained Raman converter; remove the density calculator markup, function, and initializer. Add Node source/behavior tests and extend the real-browser test.

**Tech Stack:** HTML, CSS, browser JavaScript, Node.js built-ins, Edge CDP smoke test.

## Global Constraints

- Keep `实验设计向导` as the only tab for wizard and test-reference content.
- Remove the standalone `测试数据参考` tab and `panel-test-reference`.
- Use `hc = 1239.841984 eV·nm` for photon conversion.
- Treat wavenumber as absolute wavenumber in `cm⁻¹`, not Raman shift.
- Accept only finite positive conversion inputs.
- Remove only the interactive density tool; preserve chapter 11.3 theory content.

---

### Task 1: Add failing regression tests

**Files:**
- Create: `scripts/test_spectral_conversion.mjs`
- Modify: `scripts/test_filename_generator.mjs`
- Modify: `scripts/test_filename_ui.mjs`

**Interfaces:**
- Consumes: `convertPhotonUnits()`, `convertSpectra()`, wizard/reference markup.
- Produces: failures for missing conversion controls, wrong constants, invalid-input leakage, standalone reference panel, or remaining density tool code.

- [ ] **Step 1: Add source contracts**

Assert the reference cards occur inside `panel-wizard`, the standalone reference tab/panel is absent, and `calcDensity`, `densityOut`, `id="er"`, `id="thick"`, `id="vg"`, and `id="v0"` are absent from the toolbox source.

- [ ] **Step 2: Add conversion behavior cases**

Extract the conversion functions into a VM context and verify 620 nm, 2 eV, and 10000 cm⁻¹ cases plus zero, negative, empty, and non-finite invalid cases.

- [ ] **Step 3: Verify tests fail before implementation**

Run: `node scripts/test_spectral_conversion.mjs`

Expected: failure because `convertPhotonUnits()` and its controls do not exist.

### Task 2: Merge experiment guidance

**Files:**
- Modify: `低温量子光学测试系统手册.html`

**Interfaces:**
- Consumes: existing wizard fields, `buildWizard()`, reference cards, and decision rule.
- Produces: one `panel-wizard` containing the wizard grid and reference section.

- [ ] **Step 1: Remove the standalone reference tab**

Delete the `data-panel="test-reference"` button.

- [ ] **Step 2: Move the reference section into the wizard panel**

Replace the standalone panel wrapper with `class="wizard-reference-section"` nested after the wizard two-card grid.

- [ ] **Step 3: Add visual separation**

Use a top border, spacing, and a section heading so the reference matrix remains scannable without looking like another tab.

### Task 3: Rebuild spectral conversion

**Files:**
- Modify: `低温量子光学测试系统手册.html`

**Interfaces:**
- Consumes: `specInputType`, `specInputValue`, Raman inputs.
- Produces: `specConvertOut`, `convertOut`, `convertPhotonUnits()`, and retained `convertSpectra()`.

- [ ] **Step 1: Replace the left card**

Add source-unit selector values `wavelength`, `energy`, and `wavenumber`, one numeric input, calculation button, result panel, and the absolute-wavenumber clarification.

- [ ] **Step 2: Retain Raman conversion in the right card**

Keep laser wavelength, scattering wavelength, Raman shift, result output, and explicit physical-range validation.

- [ ] **Step 3: Implement `convertPhotonUnits()`**

Normalize the source to wavelength, calculate energy and absolute wavenumber from the single constant, and format all three outputs.

- [ ] **Step 4: Remove density tool code**

Delete its card, `calcDensity()` function, and initialization call.

### Task 4: Verify source and runtime behavior

**Files:**
- Test: `scripts/test_spectral_conversion.mjs`
- Test: `scripts/test_filename_generator.mjs`
- Test: `scripts/test_filename_ui.mjs`

**Interfaces:**
- Consumes: final manual source.
- Produces: passing conversion, hierarchy, browser, and diff checks.

- [ ] **Step 1: Run Node behavior tests**

Run all three scripts and require exit code 0.

- [ ] **Step 2: Run real-browser checks**

Verify the merged wizard and both conversion cards render, and conversion output matches the expected default.

- [ ] **Step 3: Run `git diff --check`**

Expected: no whitespace errors.
