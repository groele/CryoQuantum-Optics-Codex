# -*- coding: utf-8 -*-
from pathlib import Path

target_file = Path(__file__).resolve().parent / 'build_optimized_manual.py'
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Section 2 Header Legend
legend_html = """          <div class="mt-4 p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 flex flex-wrap items-center gap-3 text-xs sm:text-sm">
            <span class="font-bold text-slate-800 dark:text-slate-200">🏷️ 操作类型快速识别标识：</span>
            <span class="manual-tag">✋ 现场物理手动</span>
            <span class="text-slate-600 dark:text-slate-300 text-xs mr-3">（扳动物理手阀、插拔波纹管卡箍、操作硬件总开关、温控器通电）</span>
            <span class="software-tag">💻 软件界面控制</span>
            <span class="text-slate-600 dark:text-slate-300 text-xs">（attoDRY 软件设置目标温、切换电磁阀、点击 Start/Cool Down）</span>
          </div>"""

# Replace Section 2 intro note
old_s2_intro = """          <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed mt-4">
            开始前必须核对本机阀门编号、压力表量程、气体纯度、原厂文件版本和设备序列号。网页复选框仅作临时进度提示，不构成正式维护记录。
          </p>"""

new_s2_intro = """          <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed mt-4">
            开始前必须核对本机阀门编号、压力表量程、气体纯度、原厂文件版本和设备序列号。网页复选框仅作临时进度提示，不构成正式维护记录。
          </p>
""" + legend_html

content = content.replace(old_s2_intro, new_s2_intro, 1)

# Step 1
old_step1_body = """                <div class="space-y-2.5 text-sm sm:text-base">
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">1</span>
                    <div><strong>设定升温参数</strong>：在控制软件 <code>Main</code> &rarr; <code>Temperature Control</code> 中将 Reservoir Target Temperature 设为 <strong class="text-brand-600">300 K</strong>，点击 <code>Start</code> 启动加热。</div>
                  </div>
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">2</span>
                    <div><strong>配置气路电磁阀</strong>：在 <code>Expert</code> 界面将 Scroll Pump 设为 <code>OFF</code>、Cryo-out <code>CLOSED</code>、Cryo-in <code>CLOSED</code>、Dump-out <code>OPEN</code>、Dump-in <code>OPEN</code>。</div>
                  </div>
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">3</span>
                    <div><strong>切断外围硬件</strong>：关闭干式膜泵；将 CRYOMECH 压缩机电源旋钮旋至 <code>OFF</code>；将中和水冷机开关拨至 <code>STOP / OFF</code>。</div>
                  </div>
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">4</span>
                    <div><strong>回设目标温度</strong>：<code>Target temperature [K]</code> 在设备升至 <strong class="text-amber-600">300 K</strong> 后，将 <code>Target temperature [K]</code> 温度调整至 <strong class="text-brand-600">3.7 K</strong>（防止后续冷却降温阶段加热器持续干烧）。</div>
                  </div>
                </div>"""

new_step1_body = """                <div class="space-y-3 text-sm sm:text-base">
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">1</span>
                    <div><span class="software-tag">💻 软件设置</span><strong>设定升温参数</strong>：在控制软件 <code>Main</code> &rarr; <code>Temperature Control</code> 中将 Reservoir Target Temperature 设为 <strong class="text-brand-600">300 K</strong>，点击 <code>Start</code> 启动加热。</div>
                  </div>
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">2</span>
                    <div><span class="software-tag">💻 软件设置</span><strong>配置气路电磁阀</strong>：在 <code>Expert</code> 界面将 Scroll Pump 设为 <code>OFF</code>、Cryo-out <code>CLOSED</code>、Cryo-in <code>CLOSED</code>、Dump-out <code>OPEN</code>、Dump-in <code>OPEN</code>。</div>
                  </div>
                  <div class="flex items-start gap-2.5 manual-action-card">
                    <span class="w-5 h-5 rounded-full bg-amber-500 text-white text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">3</span>
                    <div><span class="manual-tag">✋ 现场手动</span><strong>切断外围硬件物理总开关</strong>：<br>
                      • <strong>关闭干式膜泵物理电源开关</strong>（图 1 红色圈）；<br>
                      • <strong>将 CRYOMECH 氦压缩机电源总旋钮旋至 <code>OFF</code></strong>；<br>
                      • <strong>将中和水冷机面板开关拨至 <code>STOP / OFF</code></strong>。
                    </div>
                  </div>
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">4</span>
                    <div><span class="software-tag">💻 软件设置</span><strong>回设目标温度</strong>：<code>Target temperature [K]</code> 在设备升至 <strong class="text-amber-600">300 K</strong> 后，<strong>必须将 <code>Target temperature [K]</code> 温度调整至 <strong class="text-brand-600">3.7 K</strong></strong>（防止后续冷却降温阶段加热器持续干烧）。</div>
                  </div>
                </div>"""

content = content.replace(old_step1_body, new_step1_body, 1)

# Step 2
old_step2_body = """                <div class="space-y-3 text-sm sm:text-base">
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">1</span>
                    <div>
                      <strong>机械泵粗抽（&lt; 10 mbar）</strong>：先关闭分子泵马达（在 DCU 面板将参数 <code>023</code> 改为 <code>off</code>），仅开启机械干泵。打开 Bypass 与 Service 手阀（中南大学 1、2 号阀），打开软件 4 个气控阀，将系统粗抽至 <span class="param-pill bg-blue-100 text-blue-900 dark:bg-blue-950 dark:text-blue-200">&lt; 10 mbar</span>。
                    </div>
                  </div>
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">2</span>
                    <div>
                      <strong>分子泵精抽（10⁻⁴ mbar）</strong>：开启分子泵马达（<code>023</code> 改为 <code>on</code>），对循环气路深度抽空，将 Cryo-out、Cryo-in 与 Dump 压力抽至 <span class="param-pill bg-purple-100 text-purple-900 dark:bg-purple-950 dark:text-purple-200">10⁻⁴ mbar 量级</span>。
                    </div>
                  </div>
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">3</span>
                    <div>
                      <strong>保压密封性验证（30 分钟）</strong>：关闭 Bypass/Service 手阀及 Dump 进出阀，静态保压观察 Cryo out/in 压力 30 分钟。若压力反弹过快，说明存在杂质大量脱附，必须彻底烘烤再生冷阱。
                    </div>
                  </div>
                </div>"""

new_step2_body = """                <div class="space-y-3 text-sm sm:text-base">
                  <div class="flex items-start gap-2.5 manual-action-card">
                    <span class="w-5 h-5 rounded-full bg-amber-500 text-white text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">0</span>
                    <div>
                      <span class="manual-tag">✋ 现场手动</span><strong>硬件转接连线</strong>：<strong>拆除低温腔体波纹管，将 Pfeiffer 分子泵移动至压缩机顶部，通过金属波纹管连接至 Service 口并卡紧 KF 卡箍</strong>。
                    </div>
                  </div>
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">1</span>
                    <div>
                      <span class="manual-tag">✋ 现场手动</span><span class="software-tag">💻 软件配合</span><strong>机械泵粗抽（&lt; 10 mbar）</strong>：<br>
                      • <span class="manual-tag">✋ 现场手动</span>在 Pfeiffer DCU 面板同时按住左右键进入参数，<strong>将代码 [023] 改为 <code>off</code></strong>（仅开机械干泵）；<br>
                      • <span class="manual-tag">✋ 现场手动</span><strong>手动拧开 Bypass 手阀（V4）与 Service 手阀（V3，中南大学 1、2 号阀）</strong>；<br>
                      • <span class="software-tag">💻 软件设置</span>在 Expert 界面打开 4 个气控阀（Cryo-out, Cryo-in, Dump-out, Dump-in），粗抽至 <span class="param-pill bg-blue-100 text-blue-900 dark:bg-blue-950 dark:text-blue-200">&lt; 10 mbar</span>。
                    </div>
                  </div>
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">2</span>
                    <div>
                      <span class="manual-tag">✋ 现场手动</span><strong>分子泵精抽（10⁻⁴ mbar）</strong>：粗抽达标后，在 DCU 面板<strong>将参数 [023] 改为 <code>on</code></strong>，启动分子泵精抽至 <span class="param-pill bg-purple-100 text-purple-900 dark:bg-purple-950 dark:text-purple-200">10⁻⁴ mbar 量级</span>。
                    </div>
                  </div>
                  <div class="flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-brand-100 text-brand-700 dark:bg-brand-900 dark:text-brand-300 text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">3</span>
                    <div>
                      <span class="manual-tag">✋ 现场手动</span><span class="software-tag">💻 软件配合</span><strong>保压密封性验证（30 分钟）</strong>：<br>
                      • <span class="manual-tag">✋ 现场手动</span><strong>手动关紧 Bypass 与 Service 手阀</strong>；<br>
                      • <span class="software-tag">💻 软件设置</span>关闭 Dump-in 和 Dump-out 阀门，静态保压观察 Cryo out/in 压力 30 分钟。
                    </div>
                  </div>
                </div>"""

content = content.replace(old_step2_body, new_step2_body, 1)

# Step 3
old_step3_body = """                <ul class="space-y-2.5 text-sm sm:text-base list-none">
                  <li class="flex items-start gap-2.5">
                    <span class="text-emerald-600 font-bold text-base">🔒</span>
                    <span><strong>两端封起与侧向排气</strong>：<strong>加热的时候把过滤器两端封起来（上下两个阀门 V7、V9 关紧），侧向阀门（V8）打开排气。</strong></span>
                  </li>
                  <li class="flex items-start gap-2.5">
                    <span class="text-orange-600 font-bold text-base">🔥</span>
                    <span><strong>加热烘烤与巡检</strong>：开启温控仪加热套（<strong>连接电源即开始加热</strong>），持续加热 8h 左右；烘烤期间<strong>每隔 1~2h 检查一次氮气流速与气体消耗</strong>（加热套降温 1 小时后可再重复加热一次）。</span>
                  </li>
                  <li class="flex items-start gap-2.5">
                    <span class="text-red-600 font-bold text-base">🛑</span>
                    <span><strong>停热关气四部曲</strong>：加热完后，严格按顺序关断：<strong>① 先关闭加热器</strong>（断开加热套电源） &rarr; <strong>② 停止加热五分钟以后再关闭出气</strong>（关闭侧向出气口） &rarr; <strong>③ 最后关闭进气口</strong> &rarr; <strong>④ 最后关闭供气源（关闭氮气钢瓶阀门）</strong>。</span>
                  </li>
                  <li class="flex items-start gap-2.5">
                    <span class="text-purple-600 font-bold text-base">🌪️</span>
                    <span><strong>后续抽真空衔接</strong>：<strong>加热完并完成气路关断后，对吸附剂进行抽真空，通过侧向阀门抽，即将侧向阀门打开，然后连接泵，将吸附剂抽真空。</strong></span>
                  </li>
                </ul>"""

new_step3_body = """                <ul class="space-y-3 text-sm sm:text-base list-none">
                  <li class="flex items-start gap-2.5 manual-action-card">
                    <span class="text-amber-700 dark:text-amber-400 font-bold text-base">🔒</span>
                    <span><span class="manual-tag">✋ 现场手动</span><strong>两端封起与侧向排气</strong>：<strong>加热的时候把过滤器两端封起来（手动关紧上下两个直通阀 V7、V9），手动拧开侧向阀门（V8 打开排气）。</strong></span>
                  </li>
                  <li class="flex items-start gap-2.5 manual-action-card">
                    <span class="text-orange-600 font-bold text-base">🔥</span>
                    <span><span class="manual-tag">✋ 现场手动</span><strong>加热烘烤与插电启动</strong>：<strong>将温控仪加热套插头连接电源（连接电源即开始加热）</strong>，持续加热 8h 左右（加热套降温 1 小时后可再重复加热一次）。</span>
                  </li>
                  <li class="flex items-start gap-2.5">
                    <span class="text-blue-600 font-bold text-base">⏱️</span>
                    <span><span class="manual-tag">✋ 现场巡检</span><strong>气体流速与消耗巡检</strong>：烘烤期间<strong>每隔 1~2h 现场检查一次浮子流量计氮气流速与钢瓶减压表气量消耗</strong>（防止中途断气）。</span>
                  </li>
                  <li class="flex items-start gap-2.5 manual-action-card">
                    <span class="text-red-600 font-bold text-base">🛑</span>
                    <span><span class="manual-tag">✋ 现场手动</span><strong>停热关气严格四部曲</strong>：加热完后，现场严格按顺序关断：<br>
                      &nbsp;&nbsp;<strong>① 先关闭加热器</strong>（拔掉插头/断开温控加热套电源）；<br>
                      &nbsp;&nbsp;<strong>② 停止加热 5 分钟后，再关闭出气</strong>（手动关紧侧向出气口 V8）；<br>
                      &nbsp;&nbsp;<strong>③ 接着关闭进气口</strong>（手动关闭过滤器氮气进气口手阀）；<br>
                      &nbsp;&nbsp;<strong>④ 最后关闭供气源</strong>（手动关闭高纯氮气钢瓶总阀及减压阀）。
                    </span>
                  </li>
                  <li class="flex items-start gap-2.5">
                    <span class="text-purple-600 font-bold text-base">🌪️</span>
                    <span><span class="manual-tag">✋ 现场手动</span><strong>后续抽真空衔接</strong>：<strong>加热完并完成气路关断后，对吸附剂进行抽真空，通过侧向阀门抽，即将侧向阀门打开，然后连接泵，将吸附剂抽真空。</strong></span>
                  </li>
                </ul>"""

content = content.replace(old_step3_body, new_step3_body, 1)

# Step 4
old_step4_body = """                <ul class="space-y-2.5 text-sm sm:text-base list-disc list-inside pl-1">
                  <li><strong>停热关气与系统隔离</strong>：严格执行关断四步法（<strong>① 先关闭加热器 &rarr; ② 再关闭出气 &rarr; ③ 最后关闭进气口 &rarr; ④ 最后关闭供气源</strong>）；上下两端主阀门（V7, V9）保持关紧隔离。</li>
                  <li><strong>分子泵转接直连侧向口</strong>：使用专用 KF 变径转接环与金属波纹管，将 Pfeiffer HiCUBE 分子泵机组直接连接到<strong>过滤器侧向阀门端口（V8 接口）</strong>。</li>
                  <li><strong>开启侧向抽真空</strong>：<strong>将侧向阀门（V8）打开，然后启动泵，对吸附剂进行深度高真空抽取。</strong></li>
                  <li><strong>终点验收指标</strong>：连续抽真空 7~8 小时，DCU 面板显示真空度必须优于 <span class="param-pill bg-purple-100 text-purple-900 dark:bg-purple-950 dark:text-purple-200">&lt; 10⁻⁵ mbar</span>。</li>
                </ul>"""

new_step4_body = """                <ul class="space-y-3 text-sm sm:text-base list-none">
                  <li class="flex items-start gap-2.5">
                    <span class="text-red-500 font-bold text-base">1.</span>
                    <span><span class="manual-tag">✋ 现场手动</span><strong>前置状态确认</strong>：确认已完成停热关气四步法（加热器关、出气关、进气关、气瓶关），<strong>上下两端直通阀（V7, V9）保持关紧封起隔离</strong>。</span>
                  </li>
                  <li class="flex items-start gap-2.5 manual-action-card">
                    <span class="text-purple-600 font-bold text-base">2.</span>
                    <span><span class="manual-tag">✋ 现场手动</span><strong>分子泵转接直连侧向口</strong>：<strong>使用专用 KF 变径转接环与金属波纹管，将 Pfeiffer 分子泵机组进气口直接连接到过滤器侧向阀门端口（V8 接口），卡紧卡箍</strong>。</span>
                  </li>
                  <li class="flex items-start gap-2.5 manual-action-card">
                    <span class="text-emerald-600 font-bold text-base">3.</span>
                    <span><span class="manual-tag">✋ 现场手动</span><strong>开启侧向抽真空</strong>：<strong>手动将侧向阀门（V8）打开，在 DCU 面板启动分子泵</strong>，对吸附剂内部进行长时间深度高真空抽取。</span>
                  </li>
                  <li class="flex items-start gap-2.5">
                    <span class="text-slate-500 font-bold text-base">4.</span>
                    <span><strong>终点验收指标</strong>：连续抽真空 7~8 小时，DCU 面板 [340] 显示真空度必须优于 <span class="param-pill bg-purple-100 text-purple-900 dark:bg-purple-950 dark:text-purple-200">&lt; 10⁻⁵ mbar</span>。</span>
                  </li>
                </ul>"""

content = content.replace(old_step4_body, new_step4_body, 1)

# Step 5
old_step5_body = """                <div class="space-y-2.5 text-sm sm:text-base">
                  <div>1. <strong>冷阱复位</strong>：拆除过滤器下侧抽真空管，<strong>关闭侧阀门</strong>；<strong>重新打开过滤器上下直通主阀（V7, V9）</strong>。</div>
                  <div>2. <strong>分子泵复位</strong>：将分子泵接驳回压缩机顶部 Service 口，打开 Bypass 和 Service 手阀。</div>
                  <div>3. <strong>软件全开阀门</strong>：在 Expert 界面中将 <code>Scroll 泵</code>、<code>Cryo-out</code>、<code>Cryo-in</code>、<code>Dump-out</code>、<code>Dump-in</code> 全部设为打开。</div>
                  <div>4. <strong>分级抽空时序</strong>：先开机械干泵粗抽 1h &rarr; 启动系统膜泵并开启分子泵抽 3~4h &rarr; 打开过滤器侧阀辅助抽空，深度连续抽真空 <strong>12 小时以上（推荐通宵）</strong>。</div>
                </div>"""

new_step5_body = """                <div class="space-y-3 text-sm sm:text-base">
                  <div class="manual-action-card">
                    <span class="manual-tag">✋ 现场手动</span><strong>1. 冷阱复位手阀</strong>：拆除侧向抽真空管，<strong>手动关紧侧向阀门（V8 关）</strong>；<strong>重新手动拧开过滤器上下直通主阀（V7, V9 打开）</strong>将冷阱并入管路。
                  </div>
                  <div class="manual-action-card">
                    <span class="manual-tag">✋ 现场手动</span><strong>2. 分子泵复位接驳</strong>：<strong>将分子泵移回并连接至压缩机顶部 Service 口卡紧卡箍，手动拧开 Bypass（V4）和 Service（V3）手阀</strong>。
                  </div>
                  <div>
                    <span class="software-tag">💻 软件设置</span><strong>3. 软件全开电磁阀</strong>：在 Expert 界面中将 <code>Scroll 泵</code>、<code>Cryo-out</code>、<code>Cryo-in</code>、<code>Dump-out</code>、<code>Dump-in</code> 全部设为 <code>OPEN</code>。
                  </div>
                  <div>
                    <span class="manual-tag">✋ 现场手动</span><span class="software-tag">💻 软件配合</span><strong>4. 分级抽空时序</strong>：<br>
                    • 先开机械干泵粗抽 1h；<br>
                    • 启动系统膜泵，开启分子泵高速精抽 3~4h；<br>
                    • <span class="manual-tag">✋ 现场手动</span><strong>手动打开过滤器侧向阀门（V8 开）辅助抽空</strong>，深度连续抽真空 <strong>12 小时以上（建议通宵）</strong>。
                  </div>
                </div>"""

content = content.replace(old_step5_body, new_step5_body, 1)

# Step 6
old_step6_body = """                <div class="space-y-3 text-sm sm:text-base">
                  <div>1. <strong>气源准备</strong>：关闭 Scroll Pump、关闭 Service 手阀、关闭分子泵，将高纯氮气钢瓶接入充气口。</div>
                  <div class="bg-white dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-700 space-y-1.5">
                    <div class="font-bold text-emerald-600">2. 高纯氮气置换（严格重复 3 轮）：</div>
                    <div class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 space-y-1">
                      • 打开 Service 阀，向 Dump 充入高纯氮气，直到 Dump 压力表达到 <span class="param-pill bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200">950 ~ 1000 mbar</span>。<br>
                      • 关闭气源，开启真空泵抽气，直至 Cryo-in 压力 <span class="param-pill bg-blue-100 text-blue-900 dark:bg-blue-950 dark:text-blue-200">&lt; 10 mbar</span>。<br>
                      • <strong>完整重复上述“充至 1000mbar &rarr; 抽至 10mbar”循环 3 次</strong>。
                    </div>
                  </div>
                  <div class="bg-white dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-700 space-y-1.5">
                    <div class="font-bold text-sky-600">3. 高纯氦气终极洗气：</div>
                    <div class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 space-y-1">
                      • 切换接入高纯氦气（He），充入氦气洗气 1 次。<br>
                      • 洗气完成后，重新开启分子泵对全系统持续深度抽空 <strong>约 12 小时</strong>。
                    </div>
                  </div>
                </div>"""

new_step6_body = """                <div class="space-y-3 text-sm sm:text-base">
                  <div class="manual-action-card">
                    <span class="manual-tag">✋ 现场手动</span><span class="software-tag">💻 软件配合</span><strong>1. 气源连接与准备</strong>：<br>
                    • <span class="software-tag">💻 软件设置</span>关闭 Scroll Pump；<br>
                    • <span class="manual-tag">✋ 现场手动</span><strong>手动关紧 Service 手阀（V3），关闭分子泵，将高纯氮气钢瓶软管连接至充气接口</strong>。
                  </div>
                  <div class="bg-white dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-700 space-y-2">
                    <div class="font-bold text-emerald-600 flex items-center gap-1.5">
                      <span class="manual-tag">✋ 现场手动</span><strong>2. 高纯氮气置换（严格重复 3 轮）：</strong>
                    </div>
                    <div class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 space-y-1.5">
                      • <span class="manual-tag">✋ 现场手动</span><strong>手动打开 Service 手阀，开启氮气瓶减压阀向 Dump 充氮气</strong>，直到 Dump 压力表达到 <span class="param-pill bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200">950 ~ 1000 mbar</span>；<br>
                      • <span class="manual-tag">✋ 现场手动</span><strong>手动关闭氮气瓶阀门，开启真空泵抽气</strong>，直至 Cryo-in 压力 <span class="param-pill bg-blue-100 text-blue-900 dark:bg-blue-950 dark:text-blue-200">&lt; 10 mbar</span>；<br>
                      • <strong>完整重复上述“充至 1000mbar &rarr; 抽至 10mbar”循环 3 次</strong>。
                    </div>
                  </div>
                  <div class="bg-white dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-700 space-y-2">
                    <div class="font-bold text-sky-600 flex items-center gap-1.5">
                      <span class="manual-tag">✋ 现场手动</span><strong>3. 高纯氦气终极洗气：</strong>
                    </div>
                    <div class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 space-y-1.5">
                      • <span class="manual-tag">✋ 现场手动</span><strong>手动切换接入高纯氦气钢瓶（He）</strong>，充入氦气洗气 1 次；<br>
                      • 洗气完成后，在 DCU 面板重新启动分子泵对全系统持续深度抽空 <strong>约 12 小时</strong>。
                    </div>
                  </div>
                </div>"""

content = content.replace(old_step6_body, new_step6_body, 1)

# Step 7
old_step7_body = """                <ul class="space-y-2 text-sm sm:text-base list-disc list-inside pl-1">
                  <li>关闭分子泵与 Scroll Pump。</li>
                  <li>在软件 Expert 界面中<strong>关闭 <code>Cryo-out</code> 与 <code>Dump-out</code></strong> 气控阀。</li>
                  <li>硬件<strong>关闭压缩机后阀（中南大学 1、2 号阀）</strong>及过滤器侧阀门。</li>
                  <li>通过 <code>Dump-in</code> 阀向 Dump 储气罐充入高纯氦气至标准工作压力：<span class="param-pill bg-teal-100 text-teal-900 dark:bg-teal-950 dark:text-teal-200">950 mbar</span>。</li>
                  <li>充气完成后<strong>关闭 Dump-in 阀门</strong>，将连接软管内残存气体抽至 <strong>&lt; 10 mbar</strong> 后拆卸。</li>
                  <li>将分子泵机组移回主机，对<strong>低温真空杜瓦（Vacuum Dewar）</strong>进行独立高真空抽取。</li>
                </ul>"""

new_step7_body = """                <ul class="space-y-2.5 text-sm sm:text-base list-none">
                  <li><span class="software-tag">💻 软件设置</span>关闭分子泵与 Scroll Pump；在软件 Expert 界面中<strong>关闭 <code>Cryo-out</code> 与 <code>Dump-out</code></strong> 气控阀。</li>
                  <li class="manual-action-card">
                    <span class="manual-tag">✋ 现场手动</span><strong>手动关紧压缩机后部手阀（中南大学 1、2 号阀）及过滤器侧阀门（V8）</strong>。
                  </li>
                  <li><span class="manual-tag">✋ 现场手动</span><span class="software-tag">💻 软件配合</span><strong>通过 <code>Dump-in</code> 阀向 Dump 储气罐充入高纯氦气至标准工作压力：<span class="param-pill bg-teal-100 text-teal-900 dark:bg-teal-950 dark:text-teal-200">950 mbar</span></strong>。</li>
                  <li><span class="manual-tag">✋ 现场手动</span>充气完成后<strong>关闭 Dump-in 阀门</strong>，<strong>手动将充气连接软管内残存气体抽至 &lt; 10 mbar 后拆卸接头</strong>。</li>
                  <li class="manual-action-card">
                    <span class="manual-tag">✋ 现场手动</span><strong>杜瓦抽真空转接</strong>：<strong>将 Pfeiffer 分子泵机组推移至 attoDRY 主机，通过波纹管连接至真空杜瓦抽气口并卡紧卡箍，开启分子泵对低温真空绝热杜瓦（Vacuum Dewar）独立抽高真空</strong>。
                  </li>
                </ul>"""

content = content.replace(old_step7_body, new_step7_body, 1)

# Step 8
old_step8_cards = """            <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
              <div class="p-6 rounded-2xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 space-y-2">
                <div class="font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2 text-base">
                  <span class="w-2.5 h-2.5 rounded-full bg-brand-500"></span> 1. 样品腔充交换气
                </div>
                <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 leading-relaxed">向样品腔（Sample Space）充入微量交换气体（Exchange Gas），恢复腔体与样品之间的热传导路径。</p>
              </div>
              <div class="p-6 rounded-2xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 space-y-2">
                <div class="font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2 text-base">
                  <span class="w-2.5 h-2.5 rounded-full bg-brand-500"></span> 2. 开启水冷与压缩机
                </div>
                <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 leading-relaxed">打开运行手阀；开启中和水冷机（确认水温水压稳定）；旋开 CRYOMECH 氦压缩机电源。</p>
              </div>
              <div class="p-6 rounded-2xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 space-y-2">
                <div class="font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2 text-base">
                  <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span> 3. 点击 Cool Down
                </div>
                <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 leading-relaxed">在 attoDRY 软件主界面点击 <code>Cool Down</code> 按钮，系统自动调配电磁阀与制冷循环，自动降至 <strong>1.65 K</strong> 极限基温。</p>
              </div>
            </div>"""

new_step8_cards = """            <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
              <div class="p-6 rounded-2xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 space-y-2">
                <div class="font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2 text-base">
                  <span class="manual-tag">✋ 现场手动</span> 1. 样品腔充交换气
                </div>
                <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 leading-relaxed"><strong>手动向样品腔（Sample Space）充入适量交换气体（Exchange Gas）</strong>，恢复腔体与样品之间的低温热传导路径。</p>
              </div>
              <div class="p-6 rounded-2xl bg-amber-50/50 dark:bg-amber-950/20 border-2 border-amber-300 dark:border-amber-700 space-y-2">
                <div class="font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2 text-base">
                  <span class="manual-tag">✋ 现场手动</span> 2. 开启水冷与压缩机
                </div>
                <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
                  • <strong>手动拧开管路运行手阀</strong>；<br>
                  • <strong>手动开启中和循环水冷机总电源</strong>（确认水温 &lt; 25℃、水压正常）；<br>
                  • <strong>手动旋转开启 CRYOMECH 氦压缩机电源开关</strong>。
                </p>
              </div>
              <div class="p-6 rounded-2xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 space-y-2">
                <div class="font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2 text-base">
                  <span class="software-tag">💻 软件控制</span> 3. 点击 Cool Down
                </div>
                <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 leading-relaxed">在 attoDRY 控制软件主界面<strong>点击 <code>Cool Down</code> 按钮</strong>，系统自动调配电磁阀与闭环制冷循环，全自动降温至 <strong class="text-brand-600">1.65 K</strong> 极限基温。</p>
              </div>
            </div>"""

content = content.replace(old_step8_cards, new_step8_cards, 1)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated build_optimized_manual.py successfully with manual operation highlights!')
