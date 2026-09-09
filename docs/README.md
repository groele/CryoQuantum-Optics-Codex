# 📚 技术规范与设计文档 (Documentation & Specs)

本目录归档低温量子光学测试系统的实验数据规范、设计方案与技术规格说明。

---

## 📂 目录结构

```
docs/
├── conventions/                         # 实验与数据命名规范
│   └── FILENAME_NAMING_CONVENTIONS.md   # 数据采集与文件命名标准化规范 (V3.0)
│
└── archive/                             # 历史版本实施计划与技术规格归档
    ├── plans/                           # 功能迭代实施计划 (Plans)
    │   ├── 2026-07-10-chapter-12-2-zeeman-explanation.md
    │   ├── 2026-07-10-chapter-31-1-plot-comparison.md
    │   ├── 2026-07-10-filename-generator-and-test-reference.md
    │   ├── 2026-07-10-merge-guide-and-expand-spectral-conversion.md
    │   ├── 2026-07-10-split-naming-and-time-estimate-modules.md
    │   └── 2026-07-10-synchronized-spectral-converter.md
    └── specs/                           # 技术设计规格方案 (Specs)
        ├── 2026-07-10-chapter-12-2-zeeman-explanation-design.md
        ├── 2026-07-10-experiment-guide-and-spectral-conversion-design.md
        ├── 2026-07-10-manual-functional-diagrams-design.md
        ├── 2026-07-10-naming-and-acquisition-time-modules-design.md
        └── 2026-07-10-synchronized-spectral-converter-design.md
```

---

## 📌 核心规范索引

- **数据命名标准化规范**: [`conventions/FILENAME_NAMING_CONVENTIONS.md`](conventions/FILENAME_NAMING_CONVENTIONS.md)  
  规定了 PL、Raman、差分反射、线偏振、四通道圆偏振、变温、变磁场以及变栅压实验的标准命名词元（Tokens）与文件组织方式，确保实验数据追溯性与批量分析自动化。
