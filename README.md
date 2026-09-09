# CryoQuantum-Optics-Codex (低温量子光学测试系统手册)

<div align="center">

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg?style=flat-square)](https://github.com/groele/CryoQuantum-Optics-Codex)
[![Offline](https://img.shields.io/badge/offline-100%25%20standalone-emerald.svg?style=flat-square)](https://github.com/groele/CryoQuantum-Optics-Codex)
[![Base Temperature](https://img.shields.io/badge/temperature-1.65_K-cyan.svg?style=flat-square)](https://github.com/groele/CryoQuantum-Optics-Codex)
[![Magnetic Field](https://img.shields.io/badge/magnet-%C2%B19_T-purple.svg?style=flat-square)](https://github.com/groele/CryoQuantum-Optics-Codex)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg?style=flat-square)](https://github.com/groele/CryoQuantum-Optics-Codex)

**面向二维半导体材料微区量子光学实验与 attocube attoDRY 2100 低温恒温器/超导磁体运维洗气规范的离线交互式全栈知识库**

[🌟 打开门户主页](index.html) · [🔬 光学测试手册](optics/低温量子光学测试系统手册.html) · [❄️ 设备维护 SOP](equipment/低温设备使用手册.html) · [⚡ 现场速查卡](equipment/低温设备操作速查卡_简化版.html)

</div>

---

## 🧭 模块快速直达

| 模块类别 | 核心入口 / 文件 | 类型 | 适用场景与说明 |
| :--- | :--- | :--- | :--- |
| **统一门户** | **[`index.html`](index.html)** | Web 门户 | 全局导航主页，支持明暗主题切换，直达所有手册与规范文档 |
| **光学光谱** | **[`optics/低温量子光学测试系统手册.html`](optics/低温量子光学测试系统手册.html)** | 交互式手册 | 单文件 100% 离线，涵盖 PL / Raman / 反射 / 偏振 / 谷 Zeeman / 离线工具箱 |
| **设备运维** | **[`equipment/低温设备使用手册.html`](equipment/低温设备使用手册.html)** | 交互式 SOP | attoDRY 2100 闭循环系统与超导磁体运维全流程，含交互打卡与 P&ID 原理图 |
| **现场速查** | **[`equipment/低温设备操作速查卡_简化版.html`](equipment/低温设备操作速查卡_简化版.html)** | 实验台速查 | 8 大步骤快速比对阀门编号与设定参数，适合实验台现场执行打卡 |
| **培训课件** | **[`equipment/低温设备使用手册.pptx`](equipment/低温设备使用手册.pptx)** | 演示幻灯片 | 原厂及实验室培训幻灯片，含 16 张高精度步骤实物图与气路管网结构 |
| **数据规范** | **[`docs/conventions/FILENAME_NAMING_CONVENTIONS.md`](docs/conventions/FILENAME_NAMING_CONVENTIONS.md)** | 技术规范 | PL/Raman/偏振/磁场/变温标准文件名词元（Tokens）命名规范 |
| **工具中心** | **[`tools/`](tools/)** | 工具链 | 手册编译生成工具（`builders/`）与自动化离线完整性校验脚本（`tests/`） |

---

## 📂 仓库目录结构规范

整个仓库采用清晰的模块化分层设计，分类合理、条目清晰、无空格路径，兼顾直观阅读与自动化脚本调用：

```
CryoQuantum-Optics-Codex/
│
├── index.html                               # 🌟 统一门户导航主页 (GitHub Pages / 离线即开即用)
├── README.md                                # 📖 仓库总览与架构导航文档
├── .gitignore                               # 🛡️ Git 统一忽略规则
│
├── optics/                                  # 🔬 模块一：低温量子光学测试系统 (Optics & Spectroscopy)
│   ├── README.md                            # 光学测试手册导读与模块解析
│   └── 低温量子光学测试系统手册.html         # 核心单文件离线交互式手册 (PL/Raman/反射/偏振/谷Zeeman)
│
├── equipment/                               # ❄️ 模块二：attoDRY 2100 低温设备运维与洗气 SOP (Equipment SOP)
│   ├── README.md                            # 设备运维导读、8大核心洗气步骤一览
│   ├── 低温设备使用手册.html                 # 完整交互版 SOP 操作与维护手册
│   ├── 低温设备操作速查卡_简化版.html         # 实验台现场精炼打卡速查卡
│   ├── 低温设备使用手册.pptx                 # 原始培训与管路原理演示幻灯片 (13MB)
│   ├── manual.css                           # 手册专用离线样式文件
│   └── images/                              # 设备实物照片、P&ID 原理图与软件面板截图 (slide_1 ~ 16)
│       ├── slide_1.jpg ... slide_16.jpg
│
├── docs/                                    # 📚 模块三：技术规范与设计文档 (Documentation & Specs)
│   ├── README.md                            # 技术文档索引目录
│   ├── conventions/                         # 实验与数据命名规范
│   │   └── FILENAME_NAMING_CONVENTIONS.md   # 数据采集与文件命名标准化规范 (V3.0)
│   └── archive/                             # 历史版本实施计划与技术规格归档
│       ├── plans/                           # 功能迭代实施计划 (Plans)
│       └── specs/                           # 技术设计规格方案 (Specs)
│
├── tools/                                   # 🛠️ 模块四：开发构建与测试工具链 (Tools & Toolchain)
│   ├── README.md                            # 工具链使用说明与运行指南
│   ├── builders/                            # HTML 手册编译与生成工具
│   │   ├── build_optimized_manual.py        # 编译生成完整版《低温设备使用手册.html》
│   │   ├── build_compact_manual.py          # 编译生成精炼版《低温设备操作速查卡_简化版.html》
│   │   ├── update_manual_highlights.py      # 手动/软件操作高亮批处理脚本
│   │   ├── tailwind.config.cjs              # Tailwind CSS 配置文件
│   │   └── tailwind-input.css               # Tailwind 基础样式输入
│   └── tests/                               # 单元测试与完整性校验脚本
│       ├── validate_manual.py               # 手册离线完整性、锚点闭环与图片引用综合校验
│       ├── test_filename_generator.mjs      # 命名生成器逻辑测试
│       ├── test_filename_ui.mjs             # 命名工具 UI 自动化测试
│       └── test_spectral_conversion.mjs     # 光谱单位换算测试
│
└── .codex/                                  # ⚙️ 环境与编辑器配置
    └── config.toml
```

---

## 🌟 核心功能一览

### 1. 低温量子光学测试手册 (Optics Handbook)
- **单文件纯离线体系**: [`optics/低温量子光学测试系统手册.html`](optics/低温量子光学测试系统手册.html) 内嵌所有样式、矢量图与交互逻辑，零外部依赖。
- **出版级内联 SVG 矢量图**: 共聚焦显微 PL 激发与复合路径、虚能级 Stokes / Anti-Stokes Raman 能级图、双程共用波片偏振光路图、K 与 K′ 谷选择跃迁与谷间散射。
- **全栈光谱分析体系**:
  - **PL**: 载流子热化、激子形成、辐射复合速率方程及功率指数 $I \propto P^\alpha$。
  - **Raman**: 声子偏振张量选择定则、Anti-Stokes/Stokes 温度计测温修正。
  - **反射与吸收**: 薄膜差分反射 $\Delta R/R$ 计算原理与衬底干涉效应。
  - **偏振光学**: 线偏振度 (DOLP) 与圆偏振度 (DOCP) 拟合模型及消光比校准。
  - **谷物理**: 自旋-谷锁定、四通道谷极化矩阵（$I_{++}, I_{+-}, I_{-+}, I_{--}$）、Faraday 与 Voigt 磁光 Zeeman 能级劈裂。
- **离线计算工具箱**: 内置 DOCP/DOLP 计算器、激子有效 $g$ 因子估算工具、激光波长与光子能量双向精确换算器。

### 2. attoDRY 2100 低温与磁体运维 SOP
标准化的 8 步管路循环洗气与降温维护流程：
1. **升温与停机准备**: 软件升温至 300 K，切换 `Expert` 电磁阀，关闭干式膜泵、氦压缩机与水冷机。
2. **转移分子泵与初抽保压**: 转移分子泵至压缩机顶部服务口，机械泵粗抽检漏保压。
3. **吸附过滤器加热脱气再生 (8h)**: 隔离过滤器两端直通阀，开启侧向排气阀，加热套 8 小时深度脱水脱气。
4. **分子泵抽过滤器高真空**: 保持直通阀关闭，侧向阀接分子泵抽至高真空（$< 10^{-4}\text{ mbar}$）。
5. **全系统管路深度抽真空 (12h)**: 接入压缩机主气路，全开阀门连续抽真空 12 小时以上。
6. **循环洗气 (3×N₂ + 1×He)**: 高纯氮气（5N）充至 950–1000 mbar 抽空重复 3 次；高纯氦气冲洗 1 次。
7. **DUMP 气缸补气与外杜瓦抽真空**: 缓冲气缸补入氦气至 **950 mbar** 稳定压力；外杜瓦抽高真空。
8. **样品腔注气与降温启动**: 回充微量氦气交换气，启用水冷机与压缩机，软件点击 `Cool Down` 自动降温至 1.65 K。

---

## 🚀 快速开始与使用指南

### 1. 浏览手册与速查卡
直接使用任何现代网页浏览器双击打开：
- 统一门户导航：`index.html`
- 低温量子光学手册：`optics/低温量子光学测试系统手册.html`
- 低温设备运维 SOP：`equipment/低温设备使用手册.html`
- 实验现场速查卡：`equipment/低温设备操作速查卡_简化版.html`

### 2. 运行完整性自动化校验
在仓库根目录执行以下命令，全面检查手册完整性、离线合规性与图片引用：
```bash
python tools/tests/validate_manual.py
```

### 3. 重新编译低温设备 HTML 手册
若修改了操作流程或样式模板，可通过顶层工具链快速重新编译生成：
```bash
# 重新生成完整版低温设备 SOP 手册
python tools/builders/build_optimized_manual.py

# 重新生成现场精炼速查卡
python tools/builders/build_compact_manual.py
```

---

## 🔬 实验与数据哲学

> **Every physical conclusion should remain traceable to the optical state, sample coordinate system, excitation power, collection geometry, calibration record, fitting model and uncertainty definition.**  
> 每一个物理结论，都必须能够严格追溯至其光路偏振态、样品晶向坐标、激发功率密度、收集几何配置、仪器校准记录、拟合函数模型以及确切的不确定度（误差）定义。

---

## 📝 维护与贡献

本项目由 **groele** 维护。欢迎对物理公式、符号约定、实验 SOP 或设备操作细节提出反馈与改进建议。
