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
        'id="plot_basic-31-2-formula-expression"',
        'class="equation equation-standard"',
    ]
    missing_plot_markers = [marker for marker in required_plot_markers if marker not in html]
    if missing_plot_markers:
        fail("chapter 31 comparison/formula markers missing: " + ", ".join(missing_plot_markers))

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

    print(
        "PASS: manual structure is valid "
        f"({len(sections)} sections, {len(nav_items)} nav items, {len(ids)} ids)"
    )


if __name__ == "__main__":
    main()
