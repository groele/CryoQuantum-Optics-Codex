# Split Naming and Acquisition Time Modules Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rename the existing acquisition-planning child module to naming standards and move acquisition-time estimation into its own child module inside the same interactive toolbox.

**Architecture:** Keep both features inside `交互式实验设计与快速分析工具` and reuse its generic tab switcher. The naming generator remains a two-card panel; the existing time-estimation fields and `estimateTime()` function move unchanged into a new two-card panel with a dedicated result card.

**Tech Stack:** HTML, CSS, browser JavaScript, Node.js regression scripts.

## Global Constraints

- “采集规划” is renamed to “命名规范”.
- “采集时间估算” is a sibling child-module tab inside the existing interactive toolbox.
- Tab order ends with `光谱换算 → 命名规范 → 采集时间估算`.
- Existing filename output rules and existing acquisition-time calculation behavior remain unchanged.
- Desktop layout uses two equal columns; narrow screens stack the cards.
- No remote resources or third-party dependencies are added.

---

### Task 1: Add regression assertions for toolbox hierarchy

**Files:**
- Modify: `scripts/test_filename_generator.mjs`
- Modify: `scripts/test_filename_ui.mjs`

**Interfaces:**
- Consumes: tab and panel markup in `低温量子光学测试系统手册.html`.
- Produces: failures when `采集规划` remains, either new tab/panel is missing, or time estimation changes behavior.

- [ ] **Step 1: Add failing source assertions**

Assert exact markers `data-panel="naming"`, `id="panel-naming"`, `data-panel="time-estimate"`, and `id="panel-time-estimate"`; assert that `data-panel="acq"` and the tab label `采集规划</button>` are absent.

- [ ] **Step 2: Add a real-browser time calculation case**

Open the time-estimate tab, set the existing default values, invoke `estimateTime()`, and assert output includes `总光谱数：160`, `44.2 min`, and `0.74 h`.

- [ ] **Step 3: Run tests and verify failure**

Run: `node scripts/test_filename_generator.mjs`

Expected: failure because the new tab and panel IDs do not exist yet.

### Task 2: Split the toolbox panels

**Files:**
- Modify: `低温量子光学测试系统手册.html`

**Interfaces:**
- Consumes: existing generic `.tool-tab` click handler, filename fields, time-estimation fields, `makeFilename()`, and `estimateTime()`.
- Produces: `panel-naming` and `panel-time-estimate` sibling child modules.

- [ ] **Step 1: Replace the old tab**

Replace `<button class="tool-tab" data-panel="acq">采集规划</button>` with two buttons using `naming` and `time-estimate` data-panel values.

- [ ] **Step 2: Rename the existing panel and retain only naming cards**

Change `panel-acq` to `panel-naming`, keep `filename-generator-input` and `filename-generator-output`, and remove the `acquisition-time-card` from that panel.

- [ ] **Step 3: Create the independent time-estimation panel**

Create `panel-time-estimate` with a left input card containing the eight existing fields and button, and a right output card containing `id="timeOut"`, a concise explanation, and the existing 15–30% contingency guidance.

- [ ] **Step 4: Remove obsolete layout overrides**

Delete `.acquisition-time-card` grid positioning and ensure the two new panels rely on the existing `.tool-grid` desktop and responsive behavior.

### Task 3: Verify functionality and scope

**Files:**
- Test: `scripts/test_filename_generator.mjs`
- Test: `scripts/test_filename_ui.mjs`
- Test: `低温量子光学测试系统手册.html`

**Interfaces:**
- Consumes: completed panel split.
- Produces: reproducible source-level and real-browser verification.

- [ ] **Step 1: Run source and filename behavior tests**

Run: `node scripts/test_filename_generator.mjs`

Expected: `PASS: filename generator behavior, compact layout, and test-reference panel are valid`.

- [ ] **Step 2: Run real-browser UI tests**

Run: `node scripts/test_filename_ui.mjs`

Expected: confirmation that naming and time-estimate tabs open independently, desktop cards align, mobile cards stack, and time output is unchanged.

- [ ] **Step 3: Run final diff checks**

Run: `git diff --check`

Expected: exit code 0 with no whitespace errors.
