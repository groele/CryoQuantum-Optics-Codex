from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANUAL = ROOT / "低温量子光学测试系统手册.html"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def main() -> None:
    html = MANUAL.read_text(encoding="utf-8")

    ids = re.findall(r'id="([^"]+)"', html)
    duplicate_ids = {name: count for name, count in Counter(ids).items() if count > 1}
    if duplicate_ids:
        worst = sorted(duplicate_ids.items(), key=lambda item: item[1], reverse=True)[:8]
        fail("duplicate ids: " + ", ".join(f"{name}={count}" for name, count in worst))

    sections = re.findall(r'<section class="manual-section"(?=[\s>])', html)
    if len(sections) != 34:
        fail(f"expected 34 manual sections, found {len(sections)}")

    nav_items = re.findall(r'<a class="nav-item"(?=[\s>])', html)
    if len(nav_items) != 36:
        fail(f"expected 36 sidebar nav items, found {len(nav_items)}")

    headings = re.findall(r"<h1>(\d+)\.\s*([^<]+)</h1>", html)
    chapter_numbers = [int(number) for number, _ in headings]
    expected = list(range(1, 35))
    if chapter_numbers != expected:
        fail(f"chapter h1 sequence is {chapter_numbers}, expected {expected}")

    note_keys = re.findall(r'data-note-key="([^"]+)"', html)
    duplicate_note_keys = {
        name: count for name, count in Counter(note_keys).items() if count > 1
    }
    if duplicate_note_keys:
        worst = sorted(duplicate_note_keys.items(), key=lambda item: item[1], reverse=True)[:8]
        fail("duplicate note keys: " + ", ".join(f"{name}={count}" for name, count in worst))

    href_targets = re.findall(r'href="#([^"]+)"', html)
    id_set = set(ids)
    missing_targets = sorted(
        target for target in set(href_targets) if target and not target.startswith("${") and target not in id_set
    )
    if missing_targets:
        fail("missing href targets: " + ", ".join(missing_targets[:12]))

    remote_urls = sorted(set(re.findall(r'https?://(?!www\.w3\.org/2000/svg)[^\'"\s<>)]+' , html)))
    if remote_urls:
        fail("remote resources break offline mode: " + ", ".join(remote_urls[:8]))

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
    missing_plot_markers = [marker for marker in required_plot_markers if marker not in html]
    if missing_plot_markers:
        fail("chapter 31 comparison/formula markers missing: " + ", ".join(missing_plot_markers))

    required_zeeman_explanation_markers = [
        'class="zeeman-intuition"',
        'aria-label="Zeeman 分裂物理图像"',
        "磁矩与磁场耦合",
        "示意图，不代表实测数据",
        'class="zeeman-sign-note"',
        'class="zeeman-example"',
        "−0.230 meV/T",
        "≈ −3.97",
        'class="zeeman-extraction-steps"',
        'class="zeeman-special-case"',
        "强度差不是 Zeeman 能量分裂",
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

    required_explanation_markers = [
        'class="concept-diagram"',
        'class="theory-note"',
        'id="plot_fonts-32-1-字体与符号总则"',
        'id="plot_colors-33-1-配色与可达性总则"',
        'id="plot_panels-34-1-多面板逻辑总则"',
        "多维参数空间不是数学乘法",
        "Mapping 数据立方体",
        "谷选择定则示意",
        "g 因子拟合示意",
        "从原始谱到论文图",
    ]
    missing_explanation_markers = [
        marker for marker in required_explanation_markers if marker not in html
    ]
    if missing_explanation_markers:
        fail(
            "global theory/visual explanation markers missing: "
            + ", ".join(repr(marker) for marker in missing_explanation_markers)
        )

    formula_blocks = re.findall(r'<div class="equation(?: [^"]*)?"[^>]*>', html)
    formula_contents = re.findall(r'<div class="equation-content"', html)
    if len(formula_contents) < len(formula_blocks):
        fail(
            "formula blocks must use normalized equation-content containers "
            f"({len(formula_contents)} content containers for {len(formula_blocks)} equation blocks)"
        )

    required_formula_layout_markers = [
        ".equation {\n  display: block;\n  width: 100%;",
        ".section-body li:has(> .equation)",
        ".section-body li > .equation",
        ".equation-static {\n  display: block;\n  width: 100%;",
    ]
    missing_formula_layout_markers = [
        marker for marker in required_formula_layout_markers if marker not in html
    ]
    if missing_formula_layout_markers:
        fail(
            "formula width/layout safeguards missing: "
            + ", ".join(repr(marker) for marker in missing_formula_layout_markers)
        )

    filename_type_options = re.findall(
        r'<option value="(PL|CircularPol|LinearPolPL|Raman|LinearPolRaman|PowerDep|MagnetDep|GateDep|TempDep|Reflect)">',
        html,
    )
    expected_filename_type_options = [
        "PL",
        "CircularPol",
        "LinearPolPL",
        "Raman",
        "LinearPolRaman",
        "PowerDep",
        "MagnetDep",
        "GateDep",
        "TempDep",
        "Reflect",
    ]
    if filename_type_options != expected_filename_type_options:
        fail(
            "filename test-type order is "
            f"{filename_type_options}, expected {expected_filename_type_options}"
        )

    if ".replace(/\\./g, 'p')" in html or '.replace(/\\./g, "p")' in html:
        fail("filename sanitizer must preserve decimal points")

    required_filename_tool_markers = [
        'class="temperature-definition"',
        'class="tool-card filename-generator-input"',
        'class="tool-card filename-generator-output"',
        'data-panel="naming">命名规范</button>',
        'id="panel-naming"',
        'data-panel="time-estimate">采集时间估算</button>',
        'id="panel-time-estimate"',
        'class="tool-card time-estimate-input"',
        'class="tool-card time-estimate-output"',
        'class="filename-preview"',
        "function initFilenameGenerator()",
        "输入变化后自动刷新",
        "普通测量中表示样品实际温度",
        "温度依赖中表示当前扫描点温度",
        "{ val: '', text: '未指定 / 完整角度扫描' }",
        "{ val: 'Pol000deg', text: '0° (Pol000deg)' }",
        "{ val: 'Pol045deg', text: '45° (Pol045deg)' }",
        "{ val: 'Pol090deg', text: '90° (Pol090deg)' }",
        "{ val: 'Pol135deg', text: '135° (Pol135deg)' }",
        "{ val: '45_0', text: '45_0 (I++)' }",
        "{ val: '45_90', text: '45_90 (I+-)' }",
        "{ val: '-45_0', text: '-45_0 (I-+)' }",
        "{ val: '-45_90', text: '-45_90 (I--)' }",
        "`PL_CP_${sampleLabel}_${pol}_${b}T_${t}K`",
        "`PL_LP_${sampleLabel}${polToken}_${t}K`",
        "`Raman_LP_${sampleLabel}_${grating}${polToken}_${t}K`",
        "圆偏振 PL / 四通道分析",
        "圆偏振 PL（四通道）",
        'class="wizard-reference-section"',
        'id="specWavelength"',
        'id="specEnergy"',
        'id="specWavenumber"',
        'id="specSyncStatus"',
        "function syncPhotonUnits(source)",
        'id="fnRegion" value="R01"',
        'id="fnT" value="1.65"',
        "测试数据内容参考",
        "反射光谱（可选）",
        "超过实验重复性或测量不确定度",
        "无可靠变化时可略过重复测试",
    ]
    missing_filename_tool_markers = [
        marker for marker in required_filename_tool_markers if marker not in html
    ]
    if missing_filename_tool_markers:
        fail(
            "filename/test-reference markers missing: "
            + ", ".join(repr(marker) for marker in missing_filename_tool_markers)
        )

    if 'data-panel="acq"' in html or '>采集规划</button>' in html:
        fail("legacy acquisition-planning tab must be replaced by naming and time-estimate modules")
    if 'data-panel="test-reference"' in html or 'id="panel-test-reference"' in html:
        fail("test-reference content must be merged into the experiment wizard")
    if "function calcDensity()" in html or 'id="densityOut"' in html or "calcDensity();" in html:
        fail("interactive single-gate density tool must be removed")
    if 'id="specInputType"' in html or 'id="specInputValue"' in html or 'id="specConvertOut"' in html:
        fail("selector-based photon converter must be replaced by synchronized inputs")

    filename_function = re.search(
        r"function makeFilename\(\) \{(?P<body>.*?)\n\}", html, re.DOTALL
    )
    if not filename_function:
        fail("makeFilename function missing")
    if ".csv" in filename_function.group("body"):
        fail("generated naming convention must not append .csv")

    print(
        "PASS: manual structure is valid "
        f"({len(sections)} sections, {len(nav_items)} nav items, {len(ids)} ids)"
    )


if __name__ == "__main__":
    main()
