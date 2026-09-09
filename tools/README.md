# 🛠️ 构建与测试工具链 (Tools & Toolchain)

本目录集中管理整个仓库的 HTML 手册构建脚本、CSS 编译配置以及自动化测试与合规性校验工具。

---

## 📂 目录结构

```
tools/
├── builders/                        # 🔨 HTML 手册编译与生成工具
│   ├── build_optimized_manual.py    # 编译生成完整版《低温设备使用手册.html》
│   ├── build_compact_manual.py      # 编译生成精炼版《低温设备操作速查卡_简化版.html》
│   ├── update_manual_highlights.py  # 手动/软件操作高亮批处理脚本
│   ├── tailwind.config.cjs          # Tailwind CSS 编译配置
│   └── tailwind-input.css           # Tailwind 基础样式输入
│
└── tests/                           # 🧪 自动化测试与校验脚本
    ├── validate_manual.py           # 手册离线完整性、锚点有效性与图片引用综合校验
    ├── test_filename_generator.mjs  # 文件名生成器测试脚本
    ├── test_filename_ui.mjs         # 命名工具 UI 交互测试脚本
    └── test_spectral_conversion.mjs # 光谱单位换算测试脚本
```

---

## 🚀 常用命令指南

### 1. 运行全局完整性校验
检查所有手册（光学手册与低温设备手册）的离线合规性、锚点闭环和图片引用完整性：
```bash
python tools/tests/validate_manual.py
```

### 2. 重新编译低温设备 SOP 手册
修改配置或模板后，重新编译生成 `equipment/` 下的 HTML 手册文件：
```bash
# 重新生成完整版低温设备 SOP 手册
python tools/builders/build_optimized_manual.py

# 重新生成精炼版现场速查卡
python tools/builders/build_compact_manual.py
```
