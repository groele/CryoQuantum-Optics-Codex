from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OPTICS_MANUAL = ROOT / "optics" / "低温量子光学测试系统手册.html"
EQUIPMENT_MANUAL = ROOT / "equipment" / "低温设备使用手册.html"
COMPACT_MANUAL = ROOT / "equipment" / "低温设备操作速查卡_简化版.html"
EQUIPMENT_DIR = ROOT / "equipment"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def validate_optics_manual() -> None:
    if not OPTICS_MANUAL.exists():
        fail(f"optics manual missing at {OPTICS_MANUAL}")

    html = OPTICS_MANUAL.read_text(encoding="utf-8")

    # Check for duplicate IDs
    ids = re.findall(r'id="([^"]+)"', html)
    duplicate_ids = {name: count for name, count in Counter(ids).items() if count > 1}
    if duplicate_ids:
        fail("duplicate ids in optics manual: " + ", ".join(f"{k}={v}" for k, v in duplicate_ids.items()))

    # Check 12 sections
    sections = re.findall(r'<section id="([^"]+)"', html)
    expected_sections = [
        "overview", "workflow", "pl", "raman", "reflectance",
        "polarization", "valley", "fourchannel", "zeeman",
        "analysis", "calculator", "qa"
    ]
    if sections != expected_sections:
        fail(f"expected sections {expected_sections}, found {sections}")

    # Check anchor hrefs
    hrefs = re.findall(r'href="#([^"]+)"', html)
    id_set = set(ids)
    missing_targets = [h for h in hrefs if h not in id_set]
    if missing_targets:
        fail(f"missing anchor targets in optics manual: {missing_targets}")

    # Check offline purity (no external http/https scripts/stylesheets)
    remote_urls = sorted(set(re.findall(r'https?://(?!www\.w3\.org/2000/svg)[^\'"\s<>)]+', html)))
    if remote_urls:
        fail(f"remote resources violate offline requirement: {remote_urls}")

    # Check required SVG diagrams
    required_markers = [
        "共聚焦 PL 光路",
        "虚能级散射图像",
        "双程共用波片时的偏振链路",
        "谷选择性光学跃迁",
        "calcP()",
        "calcG()",
        "calcPhoton()",
    ]
    for marker in required_markers:
        if marker not in html:
            fail(f"required diagram/calculator marker missing: {marker}")

    print(f"PASS: optics manual is valid ({len(sections)} sections, {len(ids)} ids, fully offline)")


def validate_equipment_manuals() -> None:
    for manual_path, label in [(EQUIPMENT_MANUAL, "full SOP"), (COMPACT_MANUAL, "compact SOP")]:
        if not manual_path.exists():
            fail(f"{label} manual missing at {manual_path}")

        html = manual_path.read_text(encoding="utf-8")

        # Check offline integrity (no remote CDN resources)
        remote_scripts = re.findall(r'<script[^>]+src=["\']https?://', html)
        remote_links = re.findall(r'<link[^>]+href=["\']https?://', html)
        if remote_scripts or remote_links:
            fail(f"{label} manual contains remote script/style tags")

        # Check image references exist on disk
        img_srcs = set(re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html))
        for src in img_srcs:
            img_file = EQUIPMENT_DIR / src
            if not img_file.exists():
                fail(f"{label} references non-existent image: {src}")

        print(f"PASS: {label} is valid (images verified, fully offline)")


def main() -> None:
    print("--- Validating Optics Manual ---")
    validate_optics_manual()
    print("--- Validating Equipment Manuals ---")
    validate_equipment_manuals()
    print("All manuals validated successfully!")


if __name__ == "__main__":
    main()
