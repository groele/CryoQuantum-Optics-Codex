# Synchronized Spectral Converter Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace selector-based photon conversion with three synchronized editable fields and update filename defaults to 1.65 K and R01.

**Architecture:** Three input rows call one `syncPhotonUnits(source)` function with an explicit source key. The function writes only the two derived fields, updates one source-state class, and reports validation through one status element. Existing Raman conversion remains unchanged.

**Tech Stack:** HTML, CSS, browser JavaScript, Node VM regression tests, Edge CDP smoke test.

## Global Constraints

- Remove the source-type selector, single-value field, action button, and text result panel.
- Keep wavelength, energy, and absolute-wavenumber fields directly editable.
- Preserve the source field string and never dispatch synthetic input events.
- Empty source clears derived values without an error.
- Non-positive or non-finite source clears derived values and shows `请输入有限的正数`.
- Filename defaults are `1.65 K` and `R01`.

---

### Task 1: Update failing behavior contracts

**Files:**
- Modify: `scripts/test_spectral_conversion.mjs`
- Modify: `scripts/test_filename_generator.mjs`
- Modify: `scripts/test_filename_ui.mjs`

**Interfaces:**
- Consumes: `syncPhotonUnits(source)`, three field IDs, source-row classes, filename defaults.
- Produces: deterministic source switching and default-value regression coverage.

- [ ] Replace selector-based test fixtures with `specWavelength`, `specEnergy`, `specWavenumber`, and `specSyncStatus`.
- [ ] Verify all three source directions, empty input, invalid input, and source string preservation.
- [ ] Verify default generator output is `PL_1L_MoS2_R01_1.65K`.
- [ ] Run tests and confirm failure before implementation.

### Task 2: Implement synchronized UI and logic

**Files:**
- Modify: `低温量子光学测试系统手册.html`

**Interfaces:**
- Consumes: user input events from three fields.
- Produces: synchronized values and active-source state.

- [ ] Replace the old controls with three `.spectral-sync-row` labels and fixed unit suffixes.
- [ ] Add `.is-source` styling and a compact status/definition footer.
- [ ] Replace `convertPhotonUnits()` with `syncPhotonUnits(source)` and initialize from wavelength.
- [ ] Change `fnT` to `1.65` and `fnRegion` to `R01`.

### Task 3: Verify runtime and scope

**Files:**
- Test: `scripts/test_spectral_conversion.mjs`
- Test: `scripts/test_filename_generator.mjs`
- Test: `scripts/test_filename_ui.mjs`

**Interfaces:**
- Consumes: completed source.
- Produces: passing source, browser, responsive-layout, and diff checks.

- [ ] Run all Node tests and require exit code 0.
- [ ] Verify active-source highlighting and synchronized values in Edge.
- [ ] Run `git diff --check` and confirm no whitespace errors.
