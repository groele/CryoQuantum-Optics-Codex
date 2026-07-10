# Filename Generator and Test Reference Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Unify the filename generator, merge circular-polarization/four-channel wording, preserve decimal temperature notation, and add a physically cautious test-data reference panel.

**Architecture:** Keep the existing single-file HTML architecture. Add source-level regression assertions to `scripts/validate_manual.py`, then update the embedded HTML/JavaScript so filename field visibility and output formats follow one confirmed convention. Add one static toolbox panel for test planning; no remote dependencies are introduced.

**Tech Stack:** HTML, CSS, browser JavaScript, Python 3 source validator.

## Global Constraints

- Test-type order is: PL, circular-polarized PL, linear-polarized PL, Raman, linear-polarized Raman, power, magnetic field, voltage, temperature, reflectance.
- Measurement name precedes `LP`: `PL_LP_...` and `Raman_LP_...`.
- Preserve the existing circular-polarization channel values `45_0`, `45_90`, `-45_0`, and `-45_90`.
- Circular-polarized PL uses the `PL_CP_` prefix.
- Naming outputs do not include a file-format suffix such as `.csv`.
- Decimal points remain decimal points: `1.65` becomes `1.65K`, never `1p65K`.
- Temperature is defined for every test type.
- Reflectance at base temperature is optional; repeated measurements may be skipped when no physical change exceeds repeatability or uncertainty.
- Preserve unrelated existing changes in the monolithic manual.

---

### Task 1: Add filename and toolbox regression contracts

**Files:**
- Modify: `scripts/validate_manual.py`

**Interfaces:**
- Consumes: UTF-8 source of `低温量子光学测试系统手册.html`.
- Produces: validation failures for missing ordered options, unsafe decimal replacement, wrong LP prefix order, missing temperature definition, missing merged circular/four-channel wording, or missing reference-panel content.

- [ ] **Step 1: Write failing source-contract assertions**

Add exact marker checks for the ten ordered `<option>` elements, `PL_LP_${sampleLabel}`, `Raman_LP_${sampleLabel}`, `1.65K`, the four unchanged circular channel values, `panel-test-reference`, and the physical-change decision note. Also reject the literal JavaScript transform `.replace(/\./g, 'p')`.

- [ ] **Step 2: Run the validator and verify failure**

Run: `python scripts/validate_manual.py`

Expected: `FAIL` because the reference panel, LP prefix order, and temperature definition are not yet present.

- [ ] **Step 3: Keep the failing assertions for implementation guidance**

Do not weaken the checks while modifying the manual.

### Task 2: Correct the filename generator

**Files:**
- Modify: `低温量子光学测试系统手册.html`

**Interfaces:**
- Consumes: values from `fnType`, sample fields, temperature, magnetic field, voltage, power, polarization, and grating inputs.
- Produces: filenames in `filenameOut`, with literal decimal points and measurement-first LP prefixes.

- [ ] **Step 1: Make temperature an explicit always-active condition**

Move the temperature input into a labeled temperature-definition block and keep it visible for all ten test types. Explain that it is the actual sample temperature for ordinary measurements and the current set point for a temperature scan.

- [ ] **Step 2: Preserve current circular channel values**

Keep the four existing values and labels unchanged in both initial markup and dynamic option population.

- [ ] **Step 3: Add an unspecified/full-scan linear-polarization choice**

Use an empty value for “未指定／完整角度扫描”; individual angles use identifiable values `Pol000deg`, `Pol045deg`, `Pol090deg`, and `Pol135deg`.

- [ ] **Step 4: Fix output ordering and suffix composition**

Generate `PL_LP_${sampleLabel}${polToken}_${t}K` and `Raman_LP_${sampleLabel}_${grating}${polToken}_${t}K`, where `polToken` is empty or `_${pol}`. Generate circular-polarized PL as `PL_CP_${sampleLabel}_${pol}_${b}T_${t}K`. Preserve decimal points and omit `.csv` in every output.

- [ ] **Step 5: Include temperature in dependency and reflectance outputs**

Ensure power, magnetic-field, voltage, temperature, and both reflectance filenames carry `${t}K` so the experimental environment is not lost.

### Task 3: Merge circular-polarization and four-channel presentation

**Files:**
- Modify: `低温量子光学测试系统手册.html`

**Interfaces:**
- Consumes: existing `panel-four` calculations and experiment wizard.
- Produces: one consistently named circular-polarization/four-channel module without changing calculation behavior.

- [ ] **Step 1: Rename the toolbox tab**

Change “四通道分析” to “圆偏振 PL / 四通道分析”.

- [ ] **Step 2: Rename the wizard measurement**

Change “四通道圆偏振 PL” to “圆偏振 PL（四通道）”.

- [ ] **Step 3: Add a short equivalence note**

Explain that the four channels are the excitation/detection combinations used to reconstruct circular-polarization observables, so they belong to one module.

### Task 4: Add the test-data reference panel

**Files:**
- Modify: `低温量子光学测试系统手册.html`

**Interfaces:**
- Consumes: confirmed measurement matrix from the user.
- Produces: a new `data-panel="test-reference"` tab and `panel-test-reference` panel.

- [ ] **Step 1: Add the toolbox tab and panel shell**

Place “测试数据参考” after “实验设计向导” and add a responsive card grid.

- [ ] **Step 2: Add the four condition cards**

Base temperature contains PL, circular-polarized PL, linear-polarized PL, Raman, linear-polarized Raman, power dependence, and optional reflectance. Magnetic field, temperature, and voltage each contain the five PL/Raman polarization measurements.

- [ ] **Step 3: Add the measurement decision rule**

State that peak position, linewidth, integrated intensity, polarization response, Raman mode position/shape, and other relevant observables should be compared against repeatability and uncertainty; expand the scan only when a reliable physical change exists, otherwise retain representative data and skip duplicates.

### Task 5: Verify behavior and structure

**Files:**
- Test: `scripts/validate_manual.py`
- Test: `低温量子光学测试系统手册.html`

**Interfaces:**
- Consumes: completed source changes.
- Produces: passing structural validation and deterministic filename examples.

- [ ] **Step 1: Run the structural validator**

Run: `python scripts/validate_manual.py`

Expected: `PASS: manual structure is valid ...`.

- [ ] **Step 2: Verify representative filename cases**

Confirm source behavior for `PL_LP_1L_MoS2_R03_2K`, `Raman_LP_1L_MoS2_R03_1800g_2K`, `PL_1L_MoS2_R03_1.65K`, and `PL_CP_1L_MoS2_R03_45_0_+9T_2K`; verify that none carries `.csv`.

- [ ] **Step 3: Check the final diff for scope**

Run: `git diff --check` and inspect `git diff -- scripts/validate_manual.py 低温量子光学测试系统手册.html` to ensure no unrelated user changes were removed.
