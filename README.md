# CryoQuantum-Optics-Codex (低温量子光学测试系统手册)

> **Version: 2.4**
> 
> A comprehensive, self-contained offline user manual and interactive data analysis system for low-temperature micro-spectroscopy (PL, Raman, and Reflectance) with multi-field coupling (cryostat temperature, high magnetic field, and gate/bias voltages) and polarization resolution.

---

## 🌟 Features & Highlights

This manual is compiled into a single, fully offline, interactive HTML document:

### 1. Reorganized Modular Chapters (1–34)
- **Tier 1: Overview & Preparation (Ch 1–5)**: Standard coordinates, optical polarizations, checklist, and sample naming conventions.
- **Tier 2: Spectroscopy Testing & Optical Theory (Ch 6–17)**: Photoluminescence (PL), Raman, Reflectance, linear/circular polarization resolves, electrical coupling, magneto-optics, temperature/power/time dependencies, spatial mapping, **2D materials exciton physics, valley selection rules, valley Zeeman splitting g-factor theory, Faraday/Voigt geometry, and quick reference tables (TMD properties, Raman modes, units conversion)**.
- **Tier 3: Data Analysis & Calibration (Ch 18–23)**: Processing pipelines, polarization calibration (Mueller/Stokes matrices), statistical uncertainties, and templates.
- **Tier 4: Outputs, Safety & Quality Gates (Ch 24–30)**: Academic reporting, laser safety, checklists, device acceptance, and data quality scores.
- **Tier 5: Scientific Plotting & Panel Layouts (Ch 31–34)**: Basic plotting standards, font hierarchies, mathematical symbols formatting, color accessibility, and multi-panel grid alignment.

### 2. Interactive Analytical Toolbox
- **g-Factor Fitting**: Dynamic linear regression on Valley Zeeman splitting $\Delta E(B) = g_{\text{eff}} \mu_B B + \Delta E_0$, outputting standard error and 95% confidence intervals with full physical formula displays.
- **Linear Polarization Fit & Polar Plots**: Peanut-shaped/dipole emission profile rendering in a high-tech polar coordinate system. Supports three independent angle sweeps (0-360°, 180-540°, 360-720°) with direct intensity Y-value extraction.
- **Four-Channel Circular Polarization**: Corrects circular intensities, subtracts substrate backgrounds, and executes Monte Carlo simulations for valley polarization (DOCP) uncertainties.
- **Power Law Fit**: Exponent $\alpha$ fitting with statistical significance reporting.
- **Filename Generator**: Generates standardized file names matching Chapter 5 guidelines with conditional input layouts.
- **Data Importing**: Automatically reads `.csv`, `.txt`, and `.dat` local files directly into the calculators.

### 3. Rich Premium UI Aesthetics
- Modern typography utilizing *Outfit*, *Inter*, and *Fira Code* Google Fonts.
- Dark/Light mode toggles with smooth transitions.
- macOS-style terminal console windows for code blocks and LaTeX-like formula structures.
- Dot-matrix grid backgrounds on SVG plots matching high-end oscilloscope outputs.
- Floating sidebar navigations with visual notes active indicators (`📝`).

### 4. Equipment Operation & Maintenance SOP (attoDRY 2100 设备维护与洗气规范)
Located in [`Equipment gas washing and maintenance/`](Equipment%20gas%20washing%20and%20maintenance/):
- **`低温设备使用手册.html`**: Comprehensive offline SOP manual for attocube attoDRY 2100 cryostat & superconducting magnet operations, gas washing, vacuum regeneration, and cooldown.
- **`低温设备操作速查卡_简化版.html`**: Compact quick-reference card tailored for laboratory bench execution.
- **`低温设备使用手册.pptx`**: Original training slide deck and hardware/pipeline schematic illustrations.
- **8-Step Gas Washing Protocol**: Standardized procedures for warmup, turbopump relocation, trap degassing at 8h, deep vacuuming at 12h, 3×N₂ + 1×He gas cycles, buffer dump refill (950 mbar), and automated cooldown to 1.65 K.

---

## 🚀 Quick Start

1. **Optics & Spectroscopy System**:
   - Download [`低温量子光学测试系统手册.html`](file:///d:/Dev%20Studio/User%20guide/低温量子光学测试系统手册.html).
   - Double-click to open in any modern web browser. Fully self-contained offline handbook with interactive analysis tools.
2. **Cryogenic Equipment & Maintenance SOP**:
   - Open [`Equipment gas washing and maintenance/低温设备使用手册.html`](file:///d:/Dev%20Studio/User%20guide/Equipment%20gas%20washing%20and%20maintenance/低温设备使用手册.html) for the full interactive SOP manual.
   - Open [`Equipment gas washing and maintenance/低温设备操作速查卡_简化版.html`](file:///d:/Dev%20Studio/User%20guide/Equipment%20gas%20washing%20and%20maintenance/低温设备操作速查卡_简化版.html) for the quick operation checklist.

---

## 📝 Contribution & Licensing

- This project is compiled and maintained by the research laboratory team members.
- Feel free to submit pull requests or raise issues for any formula corrections or device configuration updates.
