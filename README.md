# CryoQuantum-Optics-Codex (低温量子光学测试系统手册)

> **Version: 2.3**
> 
> A comprehensive, self-contained offline user manual and interactive data analysis system for low-temperature micro-spectroscopy (PL, Raman, and Reflectance) with multi-field coupling (cryostat temperature, high magnetic field, and gate/bias voltages) and polarization resolution.

---

## 🌟 Features & Highlights

This manual is compiled into a single, fully offline, interactive HTML document:

### 1. Reorganized Modular Chapters (1–34)
- **Tier 1: Overview & Preparation (Ch 1–5)**: Standard coordinates, optical polarizations, checklist, and sample naming conventions.
- **Tier 2: Spectroscopy Testing Modules (Ch 6–14)**: Photoluminescence (PL), Raman, Reflectance, linear/circular polarization resolves, electrical coupling (gate scan, Stark shifts, ferroelectric loops), magneto-optics (Valley Zeeman splits, Faraday configuration), temperature/power/time dependencies, and spatial mapping.
- **Tier 3: Data Analysis & Calibration (Ch 15–20)**: Processing pipelines, polarization calibration (Mueller/Stokes matrices), statistical uncertainties, and templates.
- **Tier 4: Outputs, Safety & Quality Gates (Ch 21–27)**: Academic reporting, laser safety, checklists, device acceptance, and data quality scores.
- **Tier 5: Scientific Plotting & Panel Layouts (Ch 28–31)**: Basic plotting standards, font hierarchies, mathematical symbols formatting, color accessibility, and multi-panel grid alignment.
- **Tier 6: Optical Theory & Materials Parameters (Ch 32–34)**: 2D materials exciton physics, valley selection rules, valley Zeeman splitting g-factor theory, Faraday/Voigt geometry, and quick reference tables (TMD properties, Raman modes, units conversion).

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

---

## 🚀 Quick Start

1. Download [`低温量子光学测试系统手册.html`](file:///d:/Dev%20Studio/User%20guide/低温量子光学测试系统手册.html).
2. Double-click the file to open it in any modern web browser (Chrome, Edge, Firefox, Safari).
3. The document is **completely self-contained** and operates offline (all fitting, rendering, and note savings are executed locally in the browser).

---

## 📝 Contribution & Licensing

- This project is compiled and maintained by the research laboratory team members.
- Feel free to submit pull requests or raise issues for any formula corrections or device configuration updates.
