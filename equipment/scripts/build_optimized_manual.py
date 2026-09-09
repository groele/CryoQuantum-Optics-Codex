# -*- coding: utf-8 -*-
from pathlib import Path

html_template = """<!DOCTYPE html>
<html lang="zh-CN" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>attocube attoDRY 2100 低温与超导磁体系统操作维护标准手册 (SOP)</title>
  <link rel="stylesheet" href="manual.css">
  <style>
    :root {
      --content-font-size: 16.5px;
      --heading-h1: 1.6rem;
      --heading-h2: 1.42rem;
      --heading-h3: 1.25rem;
      --ink: #172033;
      --paper: rgba(255,255,255,.92);
      --line: rgba(148,163,184,.28);
      --brand-glow: rgba(14,165,233,.16);
    }
    body {
      font-size: var(--content-font-size);
      line-height: 1.82;
      letter-spacing: 0.015em;
      font-family: "Microsoft YaHei UI", "Noto Sans SC", "PingFang SC", "Source Han Sans SC", sans-serif;
      background-image:
        radial-gradient(circle at 8% 4%, rgba(14,165,233,.10), transparent 26rem),
        radial-gradient(circle at 92% 18%, rgba(99,102,241,.07), transparent 28rem),
        linear-gradient(rgba(148,163,184,.055) 1px, transparent 1px),
        linear-gradient(90deg, rgba(148,163,184,.055) 1px, transparent 1px);
      background-size: auto, auto, 32px 32px, 32px 32px;
      background-attachment: fixed;
    }
    .dark body {
      background-image:
        radial-gradient(circle at 8% 4%, rgba(14,165,233,.10), transparent 28rem),
        radial-gradient(circle at 92% 18%, rgba(124,58,237,.08), transparent 30rem),
        linear-gradient(rgba(148,163,184,.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(148,163,184,.035) 1px, transparent 1px);
    }
    .font-scale-sm { --content-font-size: 15px; --heading-h1: 1.45rem; --heading-h2: 1.28rem; --heading-h3: 1.15rem; }
    .font-scale-md { --content-font-size: 16.5px; --heading-h1: 1.6rem; --heading-h2: 1.42rem; --heading-h3: 1.25rem; }
    .font-scale-lg { --content-font-size: 18px; --heading-h1: 1.75rem; --heading-h2: 1.55rem; --heading-h3: 1.38rem; }
    .font-scale-xl { --content-font-size: 19.5px; --heading-h1: 1.9rem; --heading-h2: 1.68rem; --heading-h3: 1.48rem; }

    .h1-title { font-size: var(--heading-h1); }
    .h2-title { font-size: var(--heading-h2); }
    .h3-title { font-size: var(--heading-h3); }
    main h1, main h2, main h3 { line-height: 1.32; letter-spacing: -0.025em; }
    main p, main li { text-wrap: pretty; }
    main code {
      padding: .08rem .34rem;
      border: 1px solid rgba(148,163,184,.32);
      border-radius: .34rem;
      background: rgba(241,245,249,.88);
      color: #0f4c75;
      font-size: .9em;
      font-weight: 750;
    }
    .dark main code { background: rgba(15,23,42,.76); color: #7dd3fc; border-color: rgba(71,85,105,.8); }

    @media print {
      .no-print { display: none !important; }
      .print-break { page-break-before: always; }
      body { background: white !important; color: black !important; font-size: 11pt !important; }
      .card-print { break-inside: avoid; border: 1px solid #ddd !important; box-shadow: none !important; margin-bottom: 1.5rem !important; }
      body { background-image: none !important; }
    }
    
    .img-zoom {
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      cursor: zoom-in;
    }
    .img-zoom:hover {
      transform: scale(1.015);
      filter: brightness(1.02);
    }
    
    /* 细腻滚动条 */
    ::-webkit-scrollbar { width: 7px; height: 7px; }
    ::-webkit-scrollbar-track { background: rgba(0,0,0,0.02); }
    ::-webkit-scrollbar-thumb { background: rgba(3,105,161,0.3); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(3,105,161,0.6); }

    .tag-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      padding: 0.2rem 0.65rem;
      border-radius: 9999px;
      font-size: 0.82rem;
      font-weight: 600;
      letter-spacing: 0.02em;
    }

    .param-pill {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-weight: 700;
      padding: 0.15rem 0.45rem;
      border-radius: 0.375rem;
      font-size: 0.95em;
    }

    .step-badge {
      width: 3.2rem;
      height: 3.2rem;
      border-radius: 0.95rem;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      font-weight: 800;
      box-shadow: 0 4px 10px -2px rgba(0, 0, 0, 0.08);
      flex-shrink: 0;
    }

    .toc-active {
      background-color: rgb(240 249 255 / 1);
      color: rgb(3 105 161 / 1) !important;
      font-weight: 700;
      border-left: 3px solid rgb(3 105 161 / 1);
    }
    .dark .toc-active {
      background-color: rgb(8 47 73 / 0.5);
      color: rgb(186 230 253 / 1) !important;
      border-left: 3px solid rgb(56 189 248 / 1);
    }

    .spec-card {
      position: relative;
      overflow: hidden;
      transition: transform 0.24s ease, box-shadow 0.24s ease, border-color .24s ease;
    }
    .spec-card::after {
      content: "";
      position: absolute;
      width: 5rem;
      height: 5rem;
      right: -2.7rem;
      bottom: -2.7rem;
      border: 1px solid currentColor;
      border-radius: 50%;
      opacity: .12;
    }
    .spec-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 14px 28px -16px rgba(15,23,42,.34);
    }
    :focus-visible {
      outline: 3px solid rgb(14 165 233 / 0.8);
      outline-offset: 3px;
    }
    .source-chip {
      display: inline-flex;
      align-items: center;
      border-radius: 9999px;
      padding: 0.1rem 0.5rem;
      font-size: 0.72rem;
      font-weight: 700;
      background: rgb(241 245 249);
      color: rgb(71 85 105);
      border: 1px solid rgb(203 213 225);
    }
    .manual-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
      font-weight: 800;
      font-size: 0.78rem;
      padding: 0.15rem 0.5rem;
      border-radius: 0.375rem;
      background-color: #fef3c7;
      color: #92400e;
      border: 1px solid #fcd34d;
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
      margin-right: 0.35rem;
      vertical-align: middle;
    }
    .dark .manual-tag {
      background-color: rgba(120, 53, 15, 0.45);
      color: #fde68a;
      border-color: rgba(217, 119, 6, 0.6);
    }
    .software-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
      font-weight: 800;
      font-size: 0.78rem;
      padding: 0.15rem 0.5rem;
      border-radius: 0.375rem;
      background-color: #e0f2fe;
      color: #0369a1;
      border: 1px solid #7dd3fc;
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
      margin-right: 0.35rem;
      vertical-align: middle;
    }
    .dark .software-tag {
      background-color: rgba(8, 47, 73, 0.5);
      color: #bae6fd;
      border-color: rgba(2, 132, 199, 0.5);
    }
    .manual-action-card {
      background-color: rgba(254, 243, 199, 0.45);
      border: 1.5px solid #f59e0b;
      border-left-width: 4.5px;
      padding: 0.6rem 0.85rem;
      border-radius: 0.5rem;
      margin-top: 0.35rem;
      margin-bottom: 0.35rem;
    }
    .dark .manual-action-card {
      background-color: rgba(120, 53, 15, 0.25);
      border-color: #d97706;
    }

    /* 操作分级视觉系统：标签、图标、色带与字重共同编码，不仅依赖颜色 */
    .signal-legend {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 0.65rem;
    }
    .signal-key {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      min-height: 3.15rem;
      padding: 0.65rem 0.8rem;
      border: 1px solid var(--signal-border);
      border-left: 5px solid var(--signal-accent);
      border-radius: 0.8rem;
      background: var(--signal-bg);
      color: var(--signal-text);
      font-size: 0.78rem;
      font-weight: 800;
      line-height: 1.25;
    }
    .signal-key small { display: block; margin-top: 0.14rem; color: #64748b; font-weight: 500; }
    .dark .signal-key small { color: #94a3b8; }
    .signal-icon {
      display: inline-flex;
      width: 1.85rem;
      height: 1.85rem;
      align-items: center;
      justify-content: center;
      flex: 0 0 auto;
      border-radius: 0.52rem;
      background: var(--signal-accent);
      color: white;
      font-size: 0.88rem;
      box-shadow: 0 3px 8px color-mix(in srgb, var(--signal-accent) 28%, transparent);
    }
    .signal-panel {
      --signal-accent: #0284c7;
      --signal-border: #bae6fd;
      --signal-bg: rgba(240, 249, 255, 0.76);
      --signal-text: #075985;
      position: relative;
      border-left: 6px solid var(--signal-accent) !important;
      box-shadow: inset 0 1px 0 rgba(255,255,255,.5);
    }
    .signal-panel[data-signal] { padding-top: 2.55rem !important; }
    .signal-panel[data-signal]::before {
      content: attr(data-signal);
      position: absolute;
      top: 0.72rem;
      left: 0.9rem;
      display: inline-flex;
      align-items: center;
      min-height: 1.25rem;
      padding: 0.15rem 0.52rem;
      border-radius: 0.35rem;
      background: var(--signal-accent);
      color: white;
      font-size: 0.68rem;
      font-weight: 900;
      letter-spacing: 0.08em;
      line-height: 1.2;
    }
    .signal-routine { --signal-accent:#0284c7; --signal-border:#bae6fd; --signal-bg:rgba(240,249,255,.78); --signal-text:#075985; }
    .signal-check { --signal-accent:#059669; --signal-border:#a7f3d0; --signal-bg:rgba(236,253,245,.78); --signal-text:#065f46; }
    .signal-caution { --signal-accent:#d97706; --signal-border:#fde68a; --signal-bg:rgba(255,251,235,.82); --signal-text:#92400e; }
    .signal-stop { --signal-accent:#dc2626; --signal-border:#fecaca; --signal-bg:rgba(254,242,242,.88); --signal-text:#991b1b; }
    .signal-authorized { --signal-accent:#7c3aed; --signal-border:#ddd6fe; --signal-bg:rgba(245,243,255,.82); --signal-text:#5b21b6; }
    .signal-emergency { --signal-accent:#e11d48; --signal-border:#fda4af; --signal-bg:rgba(255,241,242,.92); --signal-text:#881337; }
    .dark .signal-panel { background: color-mix(in srgb, var(--signal-accent) 12%, #0f172a) !important; border-color: color-mix(in srgb, var(--signal-accent) 55%, #334155) !important; }
    .dark .signal-key { background: color-mix(in srgb, var(--signal-accent) 10%, #0f172a); border-color: color-mix(in srgb, var(--signal-accent) 50%, #334155); color: #e2e8f0; }
    .step-card {
      position: relative;
      border-left: 6px solid #7c3aed !important;
      overflow: hidden;
      box-shadow: 0 16px 42px -30px rgba(15,23,42,.5), 0 1px 0 rgba(255,255,255,.82) inset !important;
      transition: transform .24s ease, box-shadow .24s ease, border-color .24s ease;
    }
    .step-card:hover { transform: translateY(-2px); box-shadow: 0 24px 50px -30px rgba(15,23,42,.58) !important; }
    .step-card::before {
      content: "C级 · 授权维护";
      position: absolute;
      top: 0;
      right: 0;
      padding: 0.34rem 0.78rem;
      border-radius: 0 0 0 0.7rem;
      background: #7c3aed;
      color: white;
      font-size: 0.66rem;
      font-weight: 900;
      letter-spacing: 0.08em;
    }
    .step-card h3 { text-wrap: balance; }
    .step-card p, .step-card li { text-wrap: pretty; }
    .step-card > div:first-child {
      margin: -.35rem -.35rem 0;
      padding: .35rem .35rem 1.15rem;
      background: linear-gradient(90deg, rgba(124,58,237,.045), transparent 72%);
    }
    .step-card img.img-zoom {
      width: 100% !important;
      height: auto !important;
      max-height: none !important;
      object-fit: contain;
      background: white;
      box-shadow: 0 10px 28px -18px rgba(15,23,42,.42);
    }
    .step-card img.img-zoom + * { margin-top: 0.5rem; }
    .step-card .img-zoom:hover { transform: scale(1.008); }
    .step-card > .grid > div:last-child > div:first-child {
      padding: clamp(.65rem, 1.2vw, 1rem);
      background-image: radial-gradient(circle at 50% 0%, rgba(14,165,233,.08), transparent 48%);
    }
    .step-card > .grid > div:last-child > p {
      width: fit-content;
      max-width: 100%;
      margin-inline: auto;
      padding: .38rem .72rem;
      border-radius: 999px;
      background: rgba(241,245,249,.8);
      border: 1px solid rgba(148,163,184,.22);
      line-height: 1.45;
    }
    .dark .step-card > .grid > div:last-child > p { background: rgba(15,23,42,.72); border-color: rgba(71,85,105,.7); }
    .step-card > .grid > div:last-child > p::after {
      content: " · 点击图片可放大查看原图";
      color: #0284c7;
      font-weight: 800;
    }
    .image-readability-note {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.3rem 0.65rem;
      border-radius: 999px;
      background: #e0f2fe;
      color: #0369a1;
      font-size: 0.72rem;
      font-weight: 800;
    }
    .dark .image-readability-note { background: rgba(8,47,73,.7); color: #bae6fd; }

    /* 页面层次与信息密度控制 */
    .content-section {
      box-shadow: 0 16px 42px -32px rgba(15,23,42,.52), 0 1px 0 rgba(255,255,255,.78) inset !important;
    }
    header::after {
      content: "";
      position: absolute;
      left: 0;
      right: 0;
      bottom: -1px;
      height: 2px;
      background: linear-gradient(90deg, #0284c7 0 33%, #22d3ee 33% 46%, transparent 70%);
      opacity: .75;
    }
    .w-76 { width: 19rem; }
    .toc-link { border: 1px solid transparent; }
    .toc-link:hover { transform: translateX(3px); border-color: rgba(14,165,233,.2); }
    .toc-link, button, a { transition-duration: .18s; }
    main > section, main > article, main > aside, main > div { scroll-margin-top: 6rem; }
    .content-section > div:first-child h2,
    #sec-cryo-steps > div:first-child h2 { text-wrap: balance; }
    .content-section > div:first-child p,
    #sec-cryo-steps > div:first-child p { max-width: 72rem; }
    table { border-collapse: separate; border-spacing: 0; }
    table thead th {
      position: sticky;
      top: 0;
      z-index: 2;
      letter-spacing: .035em;
      font-weight: 850;
      box-shadow: inset 0 -1px 0 rgba(148,163,184,.28);
    }
    table tbody tr:nth-child(even) { background: rgba(241,245,249,.58); }
    .dark table tbody tr:nth-child(even) { background: rgba(30,41,59,.38); }
    table tbody tr { transition: background-color .16s ease; }
    table tbody tr:hover { background: rgba(224,242,254,.72); }
    .dark table tbody tr:hover { background: rgba(8,47,73,.52); }
    table td, table th { vertical-align: top; }

    /* 八步再生阶段地图 */
    .process-rail {
      position: relative;
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: .75rem;
      margin-top: 1.15rem;
    }
    .process-rail::before {
      content: "";
      position: absolute;
      left: 6%;
      right: 6%;
      top: 1.05rem;
      height: 2px;
      background: linear-gradient(90deg, #0284c7, #7c3aed, #059669);
      opacity: .34;
    }
    .phase-card {
      position: relative;
      z-index: 1;
      padding: .78rem .85rem;
      border: 1px solid rgba(148,163,184,.28);
      border-radius: .85rem;
      background: rgba(255,255,255,.92);
      box-shadow: 0 8px 18px -16px rgba(15,23,42,.6);
    }
    .dark .phase-card { background: rgba(15,23,42,.92); border-color: rgba(71,85,105,.7); }
    .phase-index {
      display: inline-flex;
      width: 2.1rem;
      height: 2.1rem;
      align-items: center;
      justify-content: center;
      border-radius: 999px;
      background: #0f172a;
      color: white;
      font-size: .72rem;
      font-weight: 900;
      box-shadow: 0 0 0 4px rgba(255,255,255,.92);
    }
    .dark .phase-index { background: #38bdf8; color: #082f49; box-shadow: 0 0 0 4px rgba(15,23,42,.92); }
    .phase-card strong { display: block; margin-top: .48rem; color: #172033; font-size: .82rem; }
    .dark .phase-card strong { color: #f8fafc; }
    .phase-card small { display: block; margin-top: .14rem; color: #64748b; font-size: .7rem; line-height: 1.35; }
    .dark .phase-card small { color: #94a3b8; }

    /* 核心洗气八步完整路线图 */
    .gas-roadmap {
      position: relative;
      overflow: hidden;
      background:
        radial-gradient(circle at 100% 0%, rgba(56,189,248,.16), transparent 25rem),
        radial-gradient(circle at 0% 100%, rgba(99,102,241,.08), transparent 28rem),
        linear-gradient(145deg, #ffffff, #f5faff 62%, #f1f5ff);
      color: #334155;
      box-shadow: 0 24px 56px -40px rgba(15,23,42,.48);
    }
    .gas-roadmap::before {
      content:"";
      position:absolute;
      inset:0;
      pointer-events:none;
      background-image:linear-gradient(rgba(14,165,233,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(14,165,233,.055) 1px,transparent 1px);
      background-size:24px 24px;
    }
    .dark .gas-roadmap {
      background:
        radial-gradient(circle at 100% 0%, rgba(56,189,248,.12), transparent 25rem),
        linear-gradient(145deg, #172235, #1d2a40 68%, #1e293b);
      color:#e2e8f0;
      box-shadow:0 24px 56px -40px rgba(2,6,23,.72);
    }
    .dark .gas-roadmap::before {
      background-image:linear-gradient(rgba(148,163,184,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(148,163,184,.055) 1px,transparent 1px);
    }
    .gas-preflight {
      position:relative;
      display:grid;
      grid-template-columns:repeat(4,minmax(0,1fr));
      gap:.55rem;
    }
    .gas-preflight div {
      padding:.58rem .68rem;
      border:1px solid #bae6fd;
      border-radius:.68rem;
      background:rgba(240,249,255,.9);
      color:#075985;
      font-size:.76rem;
      font-weight:750;
      line-height:1.4;
    }
    .dark .gas-preflight div { border-color:rgba(125,211,252,.22); background:rgba(30,41,59,.74); color:#bae6fd; }
    .gas-route-grid {
      position:relative;
      display:grid;
      grid-template-columns:repeat(4,minmax(0,1fr));
      grid-template-rows:auto auto;
      gap:1.1rem 1.35rem;
      margin-top:1.15rem;
    }
    .gas-step {
      --gas-accent:#38bdf8;
      position:relative;
      z-index:1;
      display:block;
      min-height:11.6rem;
      padding:1rem;
      border:1px solid color-mix(in srgb,var(--gas-accent) 30%,#dbe5f0);
      border-top:4px solid var(--gas-accent);
      border-radius:1rem;
      background:rgba(255,255,255,.94);
      box-shadow:0 14px 30px -24px rgba(15,23,42,.42);
    }
    .gas-step:hover { transform:translateY(-3px); background:#fff; box-shadow:0 20px 38px -25px rgba(15,23,42,.5); }
    .dark .gas-step { border-color:color-mix(in srgb,var(--gas-accent) 38%,#475569); background:rgba(30,41,59,.88); box-shadow:0 14px 30px -24px rgba(2,6,23,.85); }
    .dark .gas-step:hover { background:rgba(38,52,74,.98); box-shadow:0 20px 38px -25px rgba(2,6,23,.9); }
    .gas-step-head { display:flex; align-items:flex-start; justify-content:space-between; gap:.55rem; }
    .gas-step-num {
      display:inline-flex;
      width:2rem;
      height:2rem;
      align-items:center;
      justify-content:center;
      border-radius:.58rem;
      background:var(--gas-accent);
      color:#06111f;
      font-weight:950;
      font-size:.78rem;
      box-shadow:0 0 0 4px color-mix(in srgb,var(--gas-accent) 15%,transparent);
    }
    .gas-step-tag { padding:.16rem .48rem; border-radius:999px; background:#f1f5f9; color:#475569; font-size:.68rem; font-weight:850; }
    .gas-step h3 { margin-top:.7rem; color:#0f172a; font-size:.95rem; font-weight:850; line-height:1.42; }
    .gas-step p { margin-top:.48rem; color:#526175; font-size:.78rem; line-height:1.58; }
    .dark .gas-step-tag { background:rgba(255,255,255,.09); color:#dbeafe; }
    .dark .gas-step h3 { color:#f8fafc; }
    .dark .gas-step p { color:#b8c5d6; }
    .gas-target {
      display:block;
      margin-top:.62rem;
      padding:.42rem .5rem;
      border-radius:.5rem;
      border:1px solid color-mix(in srgb,var(--gas-accent) 18%,#e2e8f0);
      background:color-mix(in srgb,var(--gas-accent) 8%,white);
      color:color-mix(in srgb,var(--gas-accent) 70%,#0f172a);
      font-family:ui-monospace,SFMono-Regular,Consolas,monospace;
      font-size:.72rem;
      font-weight:850;
      line-height:1.4;
    }
    .dark .gas-target { border-color:color-mix(in srgb,var(--gas-accent) 20%,#334155); background:color-mix(in srgb,var(--gas-accent) 10%,#1e293b); color:color-mix(in srgb,var(--gas-accent) 68%,white); }
    .gas-step::after {
      position:absolute;
      z-index:3;
      color:#38bdf8;
      font-size:1.2rem;
      font-weight:950;
    }
    .gas-step-1 { --gas-accent:#38bdf8; }
    .gas-step-2 { --gas-accent:#0ea5e9; }
    .gas-step-3 { --gas-accent:#f59e0b; }
    .gas-step-4 { --gas-accent:#a78bfa; }
    .gas-step-5 { --gas-accent:#8b5cf6; grid-column:4; grid-row:2; }
    .gas-step-6 { --gas-accent:#10b981; grid-column:3; grid-row:2; }
    .gas-step-7 { --gas-accent:#14b8a6; grid-column:2; grid-row:2; }
    .gas-step-8 { --gas-accent:#22c55e; grid-column:1; grid-row:2; }
    .gas-step-1::after,.gas-step-2::after,.gas-step-3::after { content:"→"; top:50%; right:-1.2rem; transform:translate(50%,-50%); }
    .gas-step-4::after { content:"↓"; left:50%; bottom:-1rem; transform:translate(-50%,50%); }
    .gas-step-5::after,.gas-step-6::after,.gas-step-7::after { content:"←"; top:50%; left:-1.2rem; transform:translate(-50%,-50%); }
    .gas-gates {
      position:relative;
      display:grid;
      grid-template-columns:1fr 1fr;
      gap:.7rem;
      margin-top:1rem;
    }
    .gas-gate {
      padding:.72rem .82rem;
      border-radius:.72rem;
      font-size:.76rem;
      line-height:1.5;
    }
    .gas-stop { border:1px solid #fda4af; background:rgba(255,241,242,.94); color:#9f1239; }
    .gas-accept { border:1px solid #6ee7b7; background:rgba(236,253,245,.94); color:#065f46; }
    .dark .gas-stop { border-color:rgba(251,113,133,.5); background:rgba(136,19,55,.25); color:#fecdd3; }
    .dark .gas-accept { border-color:rgba(52,211,153,.42); background:rgba(6,78,59,.28); color:#a7f3d0; }

    /* 一页式完整操作路线图 */
    .roadmap-shell {
      position: relative;
      overflow: hidden;
      background:
        linear-gradient(135deg, rgba(14,165,233,.055), transparent 42%),
        rgba(255,255,255,.94);
    }
    .dark .roadmap-shell { background: linear-gradient(135deg, rgba(14,165,233,.08), transparent 42%), rgba(15,23,42,.94); }
    .route-spine {
      display: grid;
      grid-template-columns: repeat(4, minmax(0,1fr));
      gap: 1.05rem;
      align-items: stretch;
    }
    .route-node {
      --route-accent: #0284c7;
      position: relative;
      display: block;
      min-height: 5.4rem;
      padding: .82rem .9rem .78rem;
      border: 1px solid color-mix(in srgb, var(--route-accent) 32%, #cbd5e1);
      border-top: 4px solid var(--route-accent);
      border-radius: .9rem;
      background: rgba(255,255,255,.92);
      box-shadow: 0 10px 22px -18px rgba(15,23,42,.65);
    }
    .dark .route-node { background: rgba(15,23,42,.88); border-color: color-mix(in srgb, var(--route-accent) 52%, #334155); }
    .route-node:hover { transform: translateY(-2px); box-shadow: 0 16px 28px -20px rgba(15,23,42,.68); }
    .route-spine .route-node:not(:last-child)::after {
      content: "→";
      position: absolute;
      z-index: 2;
      top: 50%;
      right: -1rem;
      transform: translate(50%,-50%);
      color: #0284c7;
      font-weight: 900;
      font-size: 1.15rem;
    }
    .route-kicker { display: block; color: var(--route-accent); font-size: .66rem; font-weight: 900; letter-spacing: .09em; }
    .route-node strong { display: block; margin-top: .22rem; color: #172033; font-size: .9rem; line-height: 1.35; }
    .dark .route-node strong { color: #f8fafc; }
    .route-node small { display: block; margin-top: .26rem; color: #64748b; font-size: .72rem; line-height: 1.45; }
    .dark .route-node small { color: #94a3b8; }
    .route-decision { --route-accent:#334155; border-style: dashed; background: rgba(248,250,252,.95); }
    .dark .route-decision { background: rgba(30,41,59,.82); }
    .route-lanes {
      display: grid;
      grid-template-columns: repeat(3, minmax(0,1fr));
      gap: .9rem;
      margin-top: 1.15rem;
    }
    .route-lane {
      --route-accent:#0284c7;
      padding: 1rem;
      border: 1px solid color-mix(in srgb, var(--route-accent) 34%, #cbd5e1);
      border-left: 5px solid var(--route-accent);
      border-radius: 1rem;
      background: color-mix(in srgb, var(--route-accent) 5%, white);
    }
    .dark .route-lane { background: color-mix(in srgb, var(--route-accent) 10%, #0f172a); border-color: color-mix(in srgb, var(--route-accent) 48%, #334155); }
    .route-lane-head { display:flex; align-items:center; justify-content:space-between; gap:.6rem; margin-bottom:.75rem; }
    .route-lane-head strong { color: var(--route-accent); font-size: .86rem; }
    .route-lane-head span { padding:.12rem .42rem; border-radius:999px; background:var(--route-accent); color:white; font-size:.62rem; font-weight:900; }
    .route-track { display: grid; grid-template-columns: 1fr; gap: .48rem; }
    .route-step {
      position: relative;
      padding: .58rem .66rem .58rem 1.85rem;
      border-radius: .65rem;
      background: rgba(255,255,255,.76);
      color: #334155;
      font-size: .74rem;
      font-weight: 700;
      line-height: 1.4;
    }
    .dark .route-step { background: rgba(15,23,42,.62); color:#cbd5e1; }
    .route-step::before {
      content: attr(data-step);
      position:absolute;
      left:.52rem;
      top:.58rem;
      display:inline-flex;
      width:.9rem;
      height:.9rem;
      align-items:center;
      justify-content:center;
      border-radius:50%;
      background:var(--route-accent);
      color:white;
      font-size:.54rem;
      font-weight:900;
    }
    .route-routine { --route-accent:#0284c7; }
    .route-diagnostic { --route-accent:#d97706; }
    .route-authorized { --route-accent:#7c3aed; }
    .route-emergency { --route-accent:#e11d48; }
    .route-emergency-bar {
      display:grid;
      grid-template-columns:auto 1fr auto;
      gap:.9rem;
      align-items:center;
      margin-top:.9rem;
      padding:.78rem .9rem;
      border:1px solid #fda4af;
      border-left:5px solid #e11d48;
      border-radius:.85rem;
      background:rgba(255,241,242,.9);
      color:#881337;
    }
    .dark .route-emergency-bar { background:rgba(76,5,25,.38); color:#fecdd3; border-color:#9f1239; }
    .route-emergency-bar strong { font-size:.78rem; }
    .route-emergency-bar span { font-size:.7rem; line-height:1.45; }
    .route-finish {
      margin-top:.9rem;
      padding:.72rem 1rem;
      border-radius:.8rem;
      background:#0f172a;
      color:white;
      text-align:center;
      font-size:.78rem;
      font-weight:850;
      letter-spacing:.02em;
    }
    .dark .route-finish { background:#e2e8f0; color:#0f172a; }

    /* 文档治理卡：浅色模式融入整页，避免大面积纯黑视觉断层 */
    .governance-panel {
      position: relative;
      overflow: hidden;
      background:
        radial-gradient(circle at 96% 0%, rgba(56,189,248,.14), transparent 22rem),
        linear-gradient(135deg, rgba(255,255,255,.98), rgba(240,249,255,.96) 56%, rgba(238,242,255,.92)) !important;
      color: #334155 !important;
      border-color: rgba(125,211,252,.72) !important;
      box-shadow: 0 18px 42px -30px rgba(14,116,144,.42), inset 0 1px 0 rgba(255,255,255,.94) !important;
    }
    .governance-panel::before {
      content:"";
      position:absolute;
      left:0;
      right:0;
      top:0;
      height:4px;
      background:linear-gradient(90deg,#0284c7,#22d3ee 42%,#818cf8 78%,transparent);
    }
    .governance-meta {
      background:rgba(255,255,255,.72);
      border:1px solid rgba(148,163,184,.24);
      box-shadow:0 6px 16px -14px rgba(15,23,42,.5);
    }
    .governance-role {
      background:rgba(255,255,255,.68) !important;
      border-top:1px solid rgba(255,255,255,.9) !important;
      box-shadow:0 10px 24px -20px rgba(15,23,42,.5);
    }
    .dark .governance-panel {
      background:
        radial-gradient(circle at 96% 0%, rgba(56,189,248,.11), transparent 24rem),
        linear-gradient(135deg,#111827,#14213a 62%,#172554) !important;
      color:#cbd5e1 !important;
      border-color:rgba(56,189,248,.3) !important;
    }
    .dark .governance-meta { background:rgba(30,41,59,.72); border-color:rgba(71,85,105,.72); }
    .dark .governance-role { background:rgba(15,23,42,.62) !important; border-top-color:rgba(71,85,105,.6) !important; }

    @media (prefers-reduced-motion: no-preference) {
      main > * { animation: manual-settle .46s ease both; }
      main > *:nth-child(2) { animation-delay: .04s; }
      main > *:nth-child(3) { animation-delay: .08s; }
      @keyframes manual-settle { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
    }
    @media (max-width: 767px) {
      .signal-legend { grid-template-columns: 1fr 1fr; }
      .step-card::before { position: static; display: table; margin: -1.5rem -1.5rem 0 auto; border-radius: 0 0 0 0.65rem; }
      .step-card img.img-zoom { margin-inline: auto; }
      .step-card > div:first-child {
        flex-direction: column;
        align-items: stretch;
        gap: 0.9rem;
      }
      .step-card > div:first-child > div:first-child { align-items: flex-start; }
      .step-card > div:first-child > div:last-child {
        width: 100%;
        flex-wrap: wrap;
        justify-content: flex-start;
      }
      .step-card > div:first-child button,
      .step-card > div:first-child label { white-space: nowrap; }
      .process-rail { grid-template-columns: 1fr 1fr; }
      .process-rail::before { display: none; }
      .gas-preflight,.gas-gates { grid-template-columns:1fr; }
      .gas-route-grid { grid-template-columns:1fr; grid-template-rows:none; gap:.85rem; }
      .gas-step,.gas-step-5,.gas-step-6,.gas-step-7,.gas-step-8 { grid-column:auto; grid-row:auto; min-height:0; }
      .gas-step-1::after,.gas-step-2::after,.gas-step-3::after,.gas-step-4::after,.gas-step-5::after,.gas-step-6::after,.gas-step-7::after { content:"↓"; top:auto; left:50%; right:auto; bottom:-.72rem; transform:translate(-50%,50%); }
      .route-spine, .route-lanes { grid-template-columns: 1fr; }
      .route-spine { gap:.65rem; }
      .route-spine .route-node:not(:last-child)::after { content:"↓"; top:auto; bottom:-.72rem; right:50%; transform:translate(50%,50%); }
      .route-emergency-bar { grid-template-columns:auto 1fr; }
      .route-emergency-bar a { grid-column:1 / -1; }
    }
    @media (max-width: 479px) { .signal-legend { grid-template-columns: 1fr; } }
    .img-zoom[tabindex="0"] { border-radius: 0.75rem; }
  </style>
</head>
<body class="bg-slate-100/75 text-slate-700 dark:bg-slate-950 dark:text-slate-200 antialiased min-h-screen flex flex-col font-sans transition-colors duration-200">

  <!-- 顶部状态栏与控制面板 (宽幅 1560px) -->
  <header class="sticky top-0 z-40 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-slate-200/90 dark:border-slate-800 shadow-sm no-print">
    <div class="max-w-[1560px] mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
      
      <!-- 标题与版本 -->
      <div class="flex items-center gap-3.5 min-w-0">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-600 to-sky-400 flex items-center justify-center text-white font-bold shadow-md shadow-brand-500/20 text-lg shrink-0">
          ❄️
        </div>
        <div class="hidden lg:block truncate">
          <div class="flex items-center gap-2.5">
            <h1 class="h1-title font-bold tracking-tight text-slate-900 dark:text-white truncate">
              attoDRY 2100 综合操作与维护手册
            </h1>
            <span class="hidden md:inline-flex tag-badge bg-brand-100 text-brand-700 dark:bg-brand-900/60 dark:text-brand-300 border border-brand-200/60 dark:border-brand-800">
              极限 1.65 K / 磁场 ±9 T 标准 SOP
            </span>
          </div>
          <p class="text-xs text-slate-500 dark:text-slate-400 hidden sm:block truncate">
            日常操作 · 授权维护 · P&ID拓扑 · 磁体安全边界 · 交互换算工具
          </p>
        </div>
      </div>

      <!-- 工具控制按钮组：工具箱 / 字号调节 / 搜索 / 主题 / 打印 -->
      <div class="flex items-center gap-2 sm:gap-3 shrink-0">
        
        <!-- 实验室计算换算工具箱开关 -->
        <button type="button" onclick="toggleToolbox()" title="打开实验室换算与速查工具箱" aria-haspopup="dialog" aria-controls="toolboxModal" class="flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-lg bg-sky-50 text-sky-700 dark:bg-sky-950/60 dark:text-sky-300 border border-sky-200 dark:border-sky-800 hover:bg-sky-100 transition shadow-sm">
          <span>🧮</span>
          <span class="hidden md:inline">换算工具</span>
        </button>

        <!-- 字号调节器 -->
        <div class="hidden sm:flex items-center border border-slate-200 dark:border-slate-700 rounded-lg p-0.5 bg-slate-100/90 dark:bg-slate-800/90" title="调整页面字号大小">
          <button type="button" onclick="setFontScale('sm')" id="btn-font-sm" aria-label="使用小字号" class="px-2.5 py-1 text-xs font-semibold rounded hover:bg-white dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition">小</button>
          <button type="button" onclick="setFontScale('md')" id="btn-font-md" aria-label="使用中字号" class="px-2.5 py-1 text-xs font-semibold rounded bg-white dark:bg-slate-700 text-brand-600 dark:text-brand-400 shadow-sm transition">中</button>
          <button type="button" onclick="setFontScale('lg')" id="btn-font-lg" aria-label="使用大字号" class="px-2.5 py-1 text-xs font-semibold rounded hover:bg-white dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition">大</button>
          <button type="button" onclick="setFontScale('xl')" id="btn-font-xl" aria-label="使用特大字号" class="px-2.5 py-1 text-xs font-semibold rounded hover:bg-white dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition">特大</button>
        </div>

        <!-- 快速搜索框 -->
        <div class="relative w-36 sm:w-56">
          <input type="text" id="quickSearch" placeholder="搜索步骤、阀门、代码..." 
                 class="w-full text-xs sm:text-sm pl-8 pr-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-100/90 dark:bg-slate-800 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:bg-white dark:focus:bg-slate-900 transition" />
          <svg class="w-4 h-4 absolute left-2.5 top-2 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
          </svg>
        </div>

        <!-- 主题切换 -->
        <button type="button" onclick="toggleDarkMode()" title="切换亮暗主题" aria-label="切换亮暗主题" class="p-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 transition text-slate-600 dark:text-slate-300">
          <span id="themeIcon">🌓</span>
        </button>

        <!-- 打印导出 -->
        <button type="button" onclick="window.print()" title="打印手册或另存为 PDF" class="hidden md:flex items-center gap-1.5 text-xs font-semibold px-3.5 py-2 rounded-lg bg-slate-800 text-white dark:bg-slate-100 dark:text-slate-900 hover:bg-slate-700 dark:hover:bg-white transition shadow-sm">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
          打印SOP
        </button>
      </div>
    </div>
    
    <!-- 顶部进度条 -->
    <div class="w-full bg-slate-100 dark:bg-slate-800 h-1 overflow-hidden">
      <div id="scrollProgressBar" class="bg-gradient-to-r from-brand-500 to-sky-400 h-full w-0 transition-all duration-100"></div>
    </div>
  </header>

  <!-- 页面主体双栏布局 (宽幅最大 1560px) -->
  <div class="max-w-[1560px] mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full flex-1 flex gap-8 items-start">

    <!-- 左侧目录导航卡 (Sticky Sidebar, 宽 76) -->
    <aside class="w-76 shrink-0 sticky top-24 hidden xl:flex flex-col gap-5 max-h-[calc(100vh-8rem)] no-print">
      
      <div class="bg-white dark:bg-slate-900 p-5 rounded-2xl border border-slate-200/80 dark:border-slate-800 shadow-sm">
        <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-3">快捷板块目录</h3>
        <nav class="space-y-1 text-sm font-medium">
          <a href="#sec-governance" class="toc-link block px-3 py-2 rounded-xl text-red-700 dark:text-red-300 bg-red-50/80 dark:bg-red-950/30 border border-red-200 dark:border-red-900/60">0. 使用边界与文档状态</a>
          <a href="#sec-roadmap" class="toc-link block px-3 py-2 rounded-xl text-sky-700 dark:text-sky-300 bg-sky-50/70 dark:bg-sky-950/30 border border-sky-200 dark:border-sky-900/60">路线图 · 从开机到交接</a>
          <a href="#sec-overview" class="toc-link block px-3 py-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 hover:text-brand-600 transition">1. 系统总览与核心指标</a>
          <a href="#sec-cryo-steps" class="toc-link block px-3 py-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 hover:text-brand-600 transition">2. 低温气路再生 8 步法</a>
          <div class="pl-3.5 border-l-2 border-slate-200 dark:border-slate-800 my-1.5 space-y-1 text-xs text-slate-500 dark:text-slate-400">
            <a href="#sec-gas-roadmap" class="toc-sublink block py-1 font-bold text-sky-700 dark:text-sky-300 hover:text-brand-500 truncate">路线图 · 核心洗气完整流程</a>
            <a href="#step-1" class="toc-sublink block py-1 hover:text-brand-500 truncate">① Reservoir 升温 (300K)</a>
            <a href="#step-2" class="toc-sublink block py-1 hover:text-brand-500 truncate">② 转移分子泵与初抽</a>
            <a href="#step-3" class="toc-sublink block py-1 hover:text-brand-500 truncate">③ 吸附剂加热烘烤再生</a>
            <a href="#step-4" class="toc-sublink block py-1 hover:text-brand-500 truncate">④ 侧向阀连接泵抽真空</a>
            <a href="#step-5" class="toc-sublink block py-1 hover:text-brand-500 truncate">⑤ 全系统管路深度抽真空</a>
            <a href="#step-6" class="toc-sublink block py-1 hover:text-brand-500 truncate">⑥ 循环洗气 (3N2+1He)</a>
            <a href="#step-7" class="toc-sublink block py-1 hover:text-brand-500 truncate">⑦ 补充工作氦气 (950mbar)</a>
            <a href="#step-8" class="toc-sublink block py-1 hover:text-brand-500 truncate">⑧ 自动降温至 1.65 K</a>
          </div>
          <a href="#sec-pid-mapping" class="toc-link block px-3 py-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 hover:text-brand-600 transition">3. P&ID 拓扑与阀门矩阵</a>
          <a href="#sec-pfeiffer-dcu" class="toc-link block px-3 py-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 hover:text-brand-600 transition">4. Pfeiffer 分子泵指令</a>
          <a href="#sec-summary-safety" class="toc-link block px-3 py-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 hover:text-brand-600 transition">5. 参数汇总与安全红线</a>
          <a href="#sec-troubleshooting" class="toc-link block px-3 py-2 rounded-xl text-amber-700 dark:text-amber-300 font-semibold bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-900/60 hover:bg-amber-100 transition">🛠️ 6. 故障排查与磁体连接</a>
          <a href="#sec-maintenance" class="toc-link block px-3 py-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 hover:text-brand-600 transition">7. 日常操作与维护计划</a>
        </nav>
      </div>

      <!-- 实验进度统计仪表盘 (含计时器) -->
      <div class="bg-white dark:bg-slate-900 p-5 rounded-2xl border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-3.5">
        <div class="flex items-center justify-between text-xs font-bold">
          <span class="text-slate-700 dark:text-slate-300">实验再生进度</span>
          <span id="progressPercent" class="text-emerald-600 font-mono text-sm">0/8 完成</span>
        </div>
        <div class="w-full bg-slate-100 dark:bg-slate-800 h-2.5 rounded-full overflow-hidden">
          <div id="stepProgressFill" class="bg-gradient-to-r from-emerald-500 to-teal-400 h-full w-0 transition-all duration-300"></div>
        </div>
        <div class="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
          <span id="remainingTimeText">预计剩余: ~56 小时</span>
          <button type="button" onclick="resetChecklist()" class="text-slate-400 hover:text-red-500 transition underline">重置</button>
        </div>
      </div>

      <!-- 核心规格速查卡 -->
      <div class="bg-gradient-to-br from-brand-50 to-sky-50 dark:from-slate-900 dark:to-slate-800/80 p-4.5 rounded-2xl border border-brand-200/70 dark:border-slate-700 space-y-2 text-xs">
        <div class="font-bold text-brand-800 dark:text-brand-300 flex items-center gap-1.5">
          <span>⚡</span> 系统核心极限技术指标
        </div>
        <div class="grid grid-cols-2 gap-2 text-slate-600 dark:text-slate-300 font-mono">
          <div class="bg-white dark:bg-slate-800 p-2 rounded-lg border border-slate-200/70 dark:border-slate-700 text-center">
            <span class="text-[10px] block text-slate-400">极限基准温度</span><strong class="text-brand-600">1.65 K</strong>
          </div>
          <div class="bg-white dark:bg-slate-800 p-2 rounded-lg border border-slate-200/70 dark:border-slate-700 text-center">
            <span class="text-[10px] block text-slate-400">超导磁场范围</span><strong class="text-purple-600">±9 T</strong>
          </div>
          <div class="bg-white dark:bg-slate-800 p-2 rounded-lg border border-slate-200/70 dark:border-slate-700 text-center">
            <span class="text-[10px] block text-slate-400">回充工作气压</span><strong>950 mbar</strong>
          </div>
          <div class="bg-white dark:bg-slate-800 p-2 rounded-lg border border-slate-200/70 dark:border-slate-700 text-center">
            <span class="text-[10px] block text-slate-400">冷阱脱气极限</span><strong>&lt;10⁻⁵ mbar</strong>
          </div>
        </div>
      </div>

    </aside>

    <!-- 右侧手册正文内容 (充分享用宽幅空间) -->
    <main class="flex-1 space-y-12 min-w-0">

      <details class="xl:hidden no-print bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm p-4">
        <summary class="font-bold text-slate-900 dark:text-white cursor-pointer">章节目录与快速跳转</summary>
        <nav class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-4 text-sm">
          <a href="#sec-governance" class="px-3 py-2 rounded-lg bg-red-50 text-red-700 dark:bg-red-950/30 dark:text-red-300">0. 使用边界</a>
          <a href="#sec-roadmap" class="px-3 py-2 rounded-lg bg-sky-50 text-sky-800 dark:bg-sky-950/30 dark:text-sky-300">路线图 · 完整操作路径</a>
          <a href="#sec-overview" class="px-3 py-2 rounded-lg bg-slate-50 dark:bg-slate-800">1. 系统总览</a>
          <a href="#sec-cryo-steps" class="px-3 py-2 rounded-lg bg-amber-50 text-amber-800 dark:bg-amber-950/30 dark:text-amber-300">2. 受限气路维护</a>
          <a href="#sec-pid-mapping" class="px-3 py-2 rounded-lg bg-slate-50 dark:bg-slate-800">3. P&amp;ID 与阀门</a>
          <a href="#sec-pfeiffer-dcu" class="px-3 py-2 rounded-lg bg-slate-50 dark:bg-slate-800">4. 分子泵</a>
          <a href="#sec-summary-safety" class="px-3 py-2 rounded-lg bg-slate-50 dark:bg-slate-800">5. 参数与安全</a>
          <a href="#sec-troubleshooting" class="px-3 py-2 rounded-lg bg-slate-50 dark:bg-slate-800">6. 故障排查</a>
          <a href="#sec-maintenance" class="px-3 py-2 rounded-lg bg-emerald-50 text-emerald-800 dark:bg-emerald-950/30 dark:text-emerald-300">7. 日常维护</a>
        </nav>
      </details>

      <!-- 快速导航提示横幅 -->
      <div class="p-6 rounded-2xl bg-gradient-to-r from-sky-500/10 via-brand-500/10 to-transparent border border-brand-200/80 dark:border-brand-900/60 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 shadow-sm">
        <div class="space-y-1.5">
          <div class="font-bold text-slate-900 dark:text-white text-base sm:text-lg flex items-center gap-2">
            <span>📌</span> 实验室日常操作与排错指引
          </div>
          <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed">
            • 日常开机、降温、停机和保养？&rarr; 先查阅 <a href="#sec-maintenance" class="font-bold text-brand-600 dark:text-brand-400 hover:underline">第七部分：日常操作与维护计划</a><br>
            • 降温异常或疑似气路污染？&rarr; 先完成只读诊断，再由授权人员决定是否执行 <a href="#sec-cryo-steps" class="font-bold text-amber-600 dark:text-amber-400 hover:underline">受限气路再生流程</a><br>
            • 磁体通信、励磁或失超问题？&rarr; 未确认磁体安全状态前，禁止恢复默认或断电，请查阅 <a href="#sec-magnet-su" class="font-bold text-red-600 dark:text-red-400 hover:underline">磁体安全排错边界</a>
          </p>
        </div>
        <a href="#sec-valve-matrix" class="shrink-0 text-sm font-bold px-4 py-2.5 rounded-xl bg-brand-600 text-white hover:bg-brand-700 shadow-sm transition">
          查看全步骤阀门表 &darr;
        </a>
      </div>

      <aside class="rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 p-5 sm:p-6 shadow-sm" aria-label="操作类型视觉标识图例">
        <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 mb-4">
          <div>
            <div class="text-xs font-black tracking-[0.16em] text-slate-400 uppercase">Operation Signal System</div>
            <h2 class="text-lg font-extrabold text-slate-900 dark:text-white mt-1">操作类型与安全信号图例</h2>
          </div>
          <p class="text-xs text-slate-500 dark:text-slate-400">识别顺序：文字标签 → 图标 → 左侧色带 → 标题颜色</p>
        </div>
        <div class="signal-legend">
          <div class="signal-key signal-routine"><span class="signal-icon">▶</span><span>标准操作<small>按批准SOP正常执行</small></span></div>
          <div class="signal-key signal-check"><span class="signal-icon">✓</span><span>核验／验收<small>确认读数、状态和记录</small></span></div>
          <div class="signal-key signal-caution"><span class="signal-icon">!</span><span>注意事项<small>放慢操作并二次确认</small></span></div>
          <div class="signal-key signal-stop"><span class="signal-icon">⛔</span><span>禁止／停止<small>条件不满足不得继续</small></span></div>
          <div class="signal-key signal-authorized"><span class="signal-icon">🔒</span><span>授权维护<small>需培训、审批或双人复核</small></span></div>
          <div class="signal-key signal-emergency"><span class="signal-icon">SOS</span><span>应急处置<small>先保人员安全并立即上报</small></span></div>
        </div>
      </aside>

      <section id="sec-roadmap" class="content-section roadmap-shell rounded-2xl p-6 sm:p-8 lg:p-10 border border-slate-200/80 dark:border-slate-700 space-y-6" aria-labelledby="roadmap-title">
        <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-4 border-b border-slate-200/80 dark:border-slate-700 pb-5">
          <div>
            <span class="tag-badge bg-sky-100 text-sky-800 dark:bg-sky-950 dark:text-sky-200 border border-sky-200 dark:border-sky-800">一页式总览 · 可点击跳转</span>
            <h2 id="roadmap-title" class="h2-title font-extrabold text-slate-900 dark:text-white mt-2">attoDRY 2100 完整操作路线图</h2>
            <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">共同入口 → 状态判断 → 日常实验／异常诊断／授权维护分流 → 应急旁路 → 记录交接</p>
          </div>
          <div class="text-xs text-slate-500 dark:text-slate-400 lg:text-right"><strong class="text-red-600 dark:text-red-300">红色旁路优先级最高</strong><br>任一节点触发联锁、失超、泄漏或氧亏报警时立即转入应急路径</div>
        </div>

        <div class="route-spine" aria-label="所有任务共同入口">
          <a href="#sec-governance" class="route-node route-routine"><span class="route-kicker">START · 01</span><strong>确认人员权限与任务</strong><small>预约、培训级别、设备序列号、批准参数卡</small></a>
          <a href="#sec-maintenance" class="route-node route-routine"><span class="route-kicker">PRE-CHECK · 02</span><strong>完成开机前核验</strong><small>水冷、真空、供电、报警、磁区清场与初值记录</small></a>
          <a href="#sec-summary-safety" class="route-node route-decision"><span class="route-kicker">DECISION · 03</span><strong>设备状态是否正常？</strong><small>联锁正常且温度、压力、磁场与历史基线一致</small></a>
          <a href="#sec-maintenance" class="route-node route-routine"><span class="route-kicker">DISPATCH · 04</span><strong>按任务类型选择路径</strong><small>正常实验走A；异常走B；批准维护走C</small></a>
        </div>

        <div class="route-lanes" aria-label="任务分流路径">
          <div class="route-lane route-routine">
            <div class="route-lane-head"><strong>▶ A · 日常实验主线</strong><span>A级</span></div>
            <div class="route-track">
              <a href="#sec-maintenance" class="route-step" data-step="1">按插杆SOP装样并确认真空／交换气对象</a>
              <a href="#sec-maintenance" class="route-step" data-step="2">调用批准的自动降温预设并监控趋势</a>
              <a href="#sec-magnet-sop" class="route-step" data-step="3">按参数卡执行温变／场变与测量</a>
              <a href="#sec-maintenance" class="route-step" data-step="4">安全退磁或持场、升温、取样并导出日志</a>
            </div>
          </div>

          <div class="route-lane route-diagnostic">
            <div class="route-lane-head"><strong>! B · 异常诊断主线</strong><span>A→B级</span></div>
            <div class="route-track">
              <a href="#sec-troubleshooting" class="route-step" data-step="1">停止改变状态，保存报警、曲线、截图与初始值</a>
              <a href="#sec-troubleshooting" class="route-step" data-step="2">执行网络、日志、外观和历史基线只读检查</a>
              <a href="#sec-magnet-su" class="route-step" data-step="3">状态不明或磁体异常：停止并提交负责人／厂商</a>
              <a href="#sec-maintenance" class="route-step" data-step="4">仅在批准边界内恢复；完成复测与异常记录</a>
            </div>
          </div>

          <div class="route-lane route-authorized">
            <div class="route-lane-head"><strong>🔒 C · 授权维护主线</strong><span>B／C级</span></div>
            <div class="route-track">
              <a href="#sec-governance" class="route-step" data-step="1">取得负责人批准，核对培训、双人复核和原厂文件</a>
              <a href="#sec-gas-roadmap" class="route-step" data-step="2">气路污染：按八步路线图执行再生、洗气与回充</a>
              <a href="#sec-magnet-sop" class="route-step" data-step="3">磁体／电源：仅按序列号服务文件执行</a>
              <a href="#sec-maintenance" class="route-step" data-step="4">零场、真空、降温和保护参数验收后再放行</a>
            </div>
          </div>
        </div>

        <div class="route-emergency-bar" role="note" aria-label="紧急事件旁路">
          <strong>🚨 应急旁路</strong>
          <span>失超、氧亏、气体泄漏、过温／过压或人员风险 → <b>停止实验、撤离危险区域、保持通风、启动实验室应急预案并立即上报</b>；未经检查批准不得复机。</span>
          <a href="#sec-summary-safety" class="text-xs font-black underline underline-offset-2">查看安全红线 →</a>
        </div>

        <a href="#sec-maintenance" class="route-finish block">FINISH · 所有路径最终汇合：恢复批准状态 → 导出控制器日志 → 填写正式记录 → 完成交接与放行</a>
      </section>

      <section id="sec-governance" class="governance-panel content-section rounded-2xl p-6 sm:p-8 lg:p-10 border shadow-xl space-y-6">
        <div class="flex flex-col lg:flex-row lg:items-start justify-between gap-5">
          <div class="space-y-2">
            <span class="tag-badge bg-sky-100 text-sky-800 dark:bg-sky-950/70 dark:text-sky-200 border border-sky-200 dark:border-sky-800">实验室标准作业指导书 (SOP)</span>
            <h2 class="h2-title font-bold text-slate-900 dark:text-white">0. 使用边界、设备档案与授权分级</h2>
            <p class="text-slate-600 dark:text-slate-300 max-w-4xl">本页用于整合实验室经验，不替代设备序列号对应的 attocube、磁体电源、Pfeiffer 泵站和压缩机原厂手册。出现冲突时，以原厂文件、设备联锁和实验室安全准则为准。</p>
          </div>
          <div class="grid grid-cols-2 gap-2 text-xs min-w-[280px]">
            <div class="governance-meta rounded-xl p-3"><span class="block text-slate-500 dark:text-slate-400">文档版本</span><strong class="text-slate-800 dark:text-white">v2.6-LightGasRoadmap</strong></div>
            <div class="governance-meta rounded-xl p-3"><span class="block text-slate-500 dark:text-slate-400">修订日期</span><strong class="text-slate-800 dark:text-white">2026-08-29</strong></div>
            <div class="governance-meta rounded-xl p-3"><span class="block text-slate-500 dark:text-slate-400">设备型号</span><strong class="text-emerald-700 dark:text-emerald-300">attoDRY 2100</strong></div>
            <div class="governance-meta rounded-xl p-3"><span class="block text-slate-500 dark:text-slate-400">运行状态</span><strong class="text-emerald-700 dark:text-emerald-300">正式发布</strong></div>
          </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="governance-role signal-panel signal-routine rounded-2xl border border-sky-200 dark:border-sky-900 p-5" data-signal="▶ A级 · 标准操作"><div class="font-extrabold text-sky-800 dark:text-sky-200">日常用户</div><p class="text-sm text-slate-600 dark:text-slate-300 mt-2">状态检查、样品测量、经批准的自动温控/磁控、日志导出。不得拆接气路或修改底层参数。</p></div>
          <div class="governance-role signal-panel signal-authorized rounded-2xl border border-violet-200 dark:border-violet-900 p-5" data-signal="🔒 B级 · 授权维护"><div class="font-extrabold text-violet-800 dark:text-violet-200">实验室维护人员</div><p class="text-sm text-slate-600 dark:text-slate-300 mt-2">真空准备、交换气、泵站维护和受控停机。要求培训记录、双人复核和本机参数卡。</p></div>
          <div class="governance-role signal-panel signal-stop rounded-2xl border border-rose-200 dark:border-rose-900 p-5" data-signal="⛔ C级 · 普通用户禁止"><div class="font-extrabold text-rose-800 dark:text-rose-200">厂商／工程师</div><p class="text-sm text-slate-600 dark:text-slate-300 mt-2">循环气路再生、工作氦回充、磁体电源参数、恢复默认、失超后复机。普通用户禁止执行。</p></div>
        </div>
        <div class="signal-panel signal-stop rounded-xl bg-rose-50/90 dark:bg-rose-950/35 border border-rose-200 dark:border-rose-900 p-4 text-sm text-rose-900 dark:text-rose-200" data-signal="⛔ 禁止操作"><strong class="font-black">磁体硬性前置条件：</strong>未确认磁体电流、磁场、Persistent Mode、PS Heater、储能状态及原厂参数备份前，禁止关闭磁体电源、拔除大电流引线、恢复出厂默认或修改磁体常数/斜率。</div>
      </section>

      <!-- ============================================== -->
      <!-- 第一部分：系统总览与架构 -->
      <!-- ============================================== -->
      <section id="sec-overview" class="content-section bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-10 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-8">
        <div class="flex items-center gap-3.5 border-b border-slate-100 dark:border-slate-800 pb-5">
          <span class="p-3 rounded-xl bg-sky-100 text-sky-700 dark:bg-sky-950 dark:text-sky-300 font-bold text-xl">1</span>
          <div>
            <h2 class="h2-title font-bold text-slate-900 dark:text-white tracking-tight">系统总览与核心硬件架构</h2>
            <p class="text-sm text-slate-500 dark:text-slate-400">attocube attoDRY 2100 闭环干式超低温恒温器与 WITec 共聚焦显微拉曼联用系统</p>
          </div>
        </div>

        <!-- 4大核心硬件指标规格卡 (Highlight Box) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          <div class="spec-card p-5 rounded-2xl bg-gradient-to-br from-sky-50 to-blue-50/50 dark:from-sky-950/40 dark:to-slate-800 border border-sky-200/80 dark:border-sky-900/60 space-y-1 text-center shadow-sm">
            <span class="text-xs font-semibold text-sky-600 dark:text-sky-400 uppercase tracking-wider block">极限基准温度</span>
            <div class="text-2xl font-extrabold text-slate-900 dark:text-white font-mono">1.65 K</div>
            <p class="text-[11px] text-slate-500 dark:text-slate-400">温控范围: 1.65 K ~ 300 K</p>
          </div>
          <div class="spec-card p-5 rounded-2xl bg-gradient-to-br from-purple-50 to-indigo-50/50 dark:from-purple-950/40 dark:to-slate-800 border border-purple-200/80 dark:border-purple-900/60 space-y-1 text-center shadow-sm">
            <span class="text-xs font-semibold text-purple-600 dark:text-purple-400 uppercase tracking-wider block">超导磁体范围</span>
            <div class="text-2xl font-extrabold text-slate-900 dark:text-white font-mono">±9 T</div>
            <p class="text-[11px] text-slate-500 dark:text-slate-400">双极性高稳定性螺线管磁场</p>
          </div>
          <div class="spec-card p-5 rounded-2xl bg-gradient-to-br from-emerald-50 to-teal-50/50 dark:from-emerald-950/40 dark:to-slate-800 border border-emerald-200/80 dark:border-emerald-900/60 space-y-1 text-center shadow-sm">
            <span class="text-xs font-semibold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider block">循环氦气回充压</span>
            <div class="text-2xl font-extrabold text-slate-900 dark:text-white font-mono">950 mbar</div>
            <p class="text-[11px] text-slate-500 dark:text-slate-400">超高纯度 ⁴He 闭环工作介质</p>
          </div>
          <div class="spec-card p-5 rounded-2xl bg-gradient-to-br from-amber-50 to-orange-50/50 dark:from-amber-950/40 dark:to-slate-800 border border-amber-200/80 dark:border-amber-900/60 space-y-1 text-center shadow-sm">
            <span class="text-xs font-semibold text-amber-600 dark:text-amber-400 uppercase tracking-wider block">吸附冷阱极限真空</span>
            <div class="text-2xl font-extrabold text-slate-900 dark:text-white font-mono">&lt; 10⁻⁵ mbar</div>
            <p class="text-[11px] text-slate-500 dark:text-slate-400">200L Zeolite 沸石深度脱气</p>
          </div>
        </div>

        <!-- 50:50 宽幅对称布局 -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center pt-2">
          <div class="space-y-4 text-slate-600 dark:text-slate-300 leading-relaxed text-sm sm:text-base">
            <p>
              本系统是专为<strong>超低温（极限基准温度 1.65 K）</strong>与<strong>强磁场（±9 T 垂直超导磁场）</strong>环境设计的顶级干式恒温光学测量平台，联用 WITec 显微拉曼光谱仪实现样品微区拉曼（Raman）、光致发光（PL）及磁光效应的高灵敏、高空间分辨率采集。
            </p>
            <div class="bg-slate-50 dark:bg-slate-800/60 p-5 rounded-2xl border border-slate-200/80 dark:border-slate-700/60 space-y-2.5">
              <div class="font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2 text-base">
                <span class="w-2.5 h-2.5 rounded-full bg-brand-500"></span> 核心子系统组成：
              </div>
              <ul class="list-disc list-inside space-y-1.5 text-slate-600 dark:text-slate-300 pl-1 text-sm sm:text-base">
                <li><strong>主机与光学系统</strong>：attoDRY 2100 低温腔体、样品仓、VTI、<strong class="text-purple-600 dark:text-purple-400">±9 T 超导磁体</strong>、WITec 显微镜与激发激光器。</li>
                <li><strong>循环气路与净化</strong>：Dump 储气罐、Scroll Pump 干式涡旋循环泵、Gas Filter / Zeolite Trap 吸附冷阱推车。</li>
                <li><strong>辅助制冷与温控</strong>：CRYOMECH 氦压缩机、中和（Zhonghe）循环水冷机、HK-06 智能温控仪（加热套）。</li>
                <li><strong>真空与测控电控</strong>：Pfeiffer HiCUBE 分子泵机组、SU（System/Sample Unit）机柜、GHS 气路服务器。</li>
              </ul>
            </div>
          </div>

          <div class="group relative rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 shadow-sm flex flex-col items-center justify-center">
            <img src="images/slide_1.jpg" alt="attoDRY 2100 系统总览" decoding="async" fetchpriority="high" class="w-full h-auto max-h-[500px] object-contain img-zoom" onclick="openLightbox(this.src, 'attoDRY 2100 系统总览与 WITec 光谱仪联用布局')" />
            <div class="p-3 w-full text-center text-xs sm:text-sm text-slate-500 bg-white/90 dark:bg-slate-800/90 backdrop-blur-sm border-t border-slate-200 dark:border-slate-700 font-medium">
              📷 图 1.1：attocube attoDRY 2100 / SU 整体外观与工作站（点击放大）
            </div>
          </div>
        </div>

        <!-- 两个 50:50 图示对照 -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 pt-2">
          <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-4 shadow-sm flex flex-col justify-between">
            <img src="images/slide_16.jpg" alt="控制柜与真空泵布局" loading="lazy" decoding="async" class="w-full h-auto rounded-xl object-contain img-zoom" onclick="openLightbox(this.src, '实验室控制柜、激光器、光谱仪、低温腔体与分子泵机组物理布局')" />
            <div class="mt-3 text-center text-xs sm:text-sm text-slate-500 font-medium">
              📷 图 1.2：实验室实物分布（激光器、控制柜、光谱仪、低温腔体、真空泵）
            </div>
          </div>
          <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-4 shadow-sm flex flex-col justify-between">
            <img src="images/slide_15.jpg" alt="冷阱推车与压缩机实物对照" loading="lazy" decoding="async" class="w-full h-auto rounded-xl object-contain img-zoom" onclick="openLightbox(this.src, '吸附器冷阱机架推车、Scroll 泵与压缩机手阀实物位置对应')" />
            <div class="mt-3 text-center text-xs sm:text-sm text-slate-500 font-medium">
              📷 图 1.3：吸附器机架推车、Scroll 泵及压缩机面板实物标号 (V3~V9)
            </div>
          </div>
        </div>
      </section>


      <!-- ============================================== -->
      <!-- 第二部分：低温气路再生与洗气八步法 (宽幅 50:50 一半一半对称布局) -->
      <!-- ============================================== -->
      <section id="sec-cryo-steps" class="space-y-8">
        
        <div class="bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-10 border border-slate-200/80 dark:border-slate-800 shadow-sm">
          <div class="flex items-center gap-3.5 border-b border-slate-100 dark:border-slate-800 pb-5 mb-3">
            <span class="p-3 rounded-xl bg-sky-500 text-white font-bold text-xl shadow-sm">2</span>
            <div>
              <h2 class="h2-title font-bold text-slate-900 dark:text-white tracking-tight">
                低温循环气路升温、冷阱再生与洗气除杂八步法（C级授权维护）
              </h2>
              <p class="text-sm text-slate-500 dark:text-slate-400">
                用于确认存在污染或吸附性能下降后的受控维护；标准插杆基准温度通常为 <strong class="text-brand-600 dark:text-brand-400">1.65–1.8 K</strong>，实际结果取决于插杆与热负载
              </p>
            </div>
          </div>
          <div class="signal-panel signal-authorized rounded-xl bg-red-50 dark:bg-red-950/40 border border-red-300 dark:border-red-800 p-4 text-sm text-red-800 dark:text-red-200" data-signal="🔒 C级 · 执行门槛">
            <strong>执行门槛：</strong>仅限完成专项培训的授权维护人员，在负责人批准、双人复核、管路残压确认、通风与气体安全条件满足后执行。普通用户不得拆接气路、加热吸附器或回充工作氦。
          </div>
          <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed mt-4">
            开始前必须核对本机阀门编号、压力表量程、气体纯度、原厂文件版本和设备序列号。网页复选框仅作临时进度提示，不构成正式维护记录。
          </p>
          <div class="mt-4 p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 flex flex-wrap items-center gap-3 text-xs sm:text-sm">
            <span class="font-bold text-slate-800 dark:text-slate-200">🏷️ 操作类型快速识别标识：</span>
            <span class="manual-tag">✋ 现场物理手动</span>
            <span class="text-slate-600 dark:text-slate-300 text-xs mr-3">（扳动物理手阀、插拔波纹管卡箍、操作硬件总开关、温控器通电）</span>
            <span class="software-tag">💻 软件界面控制</span>
            <span class="text-slate-600 dark:text-slate-300 text-xs">（attoDRY 软件设置目标温、切换电磁阀、点击 Start/Cool Down）</span>
          </div>
          <nav class="process-rail" aria-label="八步维护流程阶段地图">
            <a href="#step-1" class="phase-card group"><span class="phase-index">Ⅰ</span><strong>升温与隔离</strong><small>步骤 1–2 · 解吸、转泵与粗抽验证</small></a>
            <a href="#step-3" class="phase-card group"><span class="phase-index">Ⅱ</span><strong>吸附器再生</strong><small>步骤 3–4 · 烘烤、排杂与真空脱气</small></a>
            <a href="#step-5" class="phase-card group"><span class="phase-index">Ⅲ</span><strong>主管路净化</strong><small>步骤 5–7 · 深抽、洗气与工作氦回充</small></a>
            <a href="#step-8" class="phase-card group"><span class="phase-index">Ⅳ</span><strong>复位与验收</strong><small>步骤 8 · 恢复连接并验证降温性能</small></a>
          </nav>
        </div>

        <section id="sec-gas-roadmap" class="gas-roadmap rounded-2xl p-6 sm:p-8 lg:p-9 border border-sky-200 dark:border-slate-600" aria-labelledby="gas-roadmap-title">
          <div class="relative flex flex-col lg:flex-row lg:items-end justify-between gap-4 border-b border-sky-200 dark:border-slate-600 pb-5">
            <div>
              <span class="tag-badge bg-violet-50 dark:bg-violet-500/20 text-violet-700 dark:text-violet-200 border border-violet-200 dark:border-violet-400/40">🔒 C级授权维护 · 双人复核</span>
              <h2 id="gas-roadmap-title" class="h2-title font-extrabold text-slate-900 dark:text-white mt-2">核心洗气与闭式循环气路再生：八步完整操作路线图</h2>
              <p class="text-sm text-slate-600 dark:text-slate-300 mt-1">升温解吸 → 抽空检漏 → 吸附器再生 → 深度脱气 → 全回路抽空 → 3N₂+1He洗气 → 工作氦回充 → 降温验收</p>
            </div>
            <p class="text-xs text-amber-800 dark:text-amber-200 lg:text-right max-w-md rounded-xl bg-amber-50/90 dark:bg-amber-500/10 border border-amber-200 dark:border-amber-400/20 px-3 py-2"><strong>参数边界：</strong>图中数值用于对应本实验室现有步骤；执行前必须以本机序列号文件、批准参数卡和当前压力表量程复核。</p>
          </div>

          <div class="gas-preflight mt-5" aria-label="洗气执行前置条件">
            <div>① 负责人书面批准，操作者完成专项培训</div>
            <div>② 双人核对阀号、管路对象与残余压力</div>
            <div>③ 通风、氧亏监测和气瓶固定状态正常</div>
            <div>④ 气体纯度、泵站、规管和原厂文件齐备</div>
          </div>

          <div class="gas-route-grid" aria-label="八步洗气操作主线">
            <a href="#step-1" class="gas-step gas-step-1">
              <div class="gas-step-head"><span class="gas-step-num">01</span><span class="gas-step-tag">软件＋现场</span></div>
              <h3>全系统升温与气路隔离</h3>
              <p>Reservoir升至室温，使管壁和冷阱杂质充分解吸；按批准阀态隔离Cryo回路。</p>
              <span class="gas-target">目标：300 K；完成后回设 3.7 K</span>
            </a>
            <a href="#step-2" class="gas-step gas-step-2">
              <div class="gas-step-head"><span class="gas-step-num">02</span><span class="gas-step-tag">现场＋泵站</span></div>
              <h3>转接泵站、初抽与保压检漏</h3>
              <p>确认转接密封，先机械泵粗抽，再启动分子泵精抽，并完成静态保压观察。</p>
              <span class="gas-target">&lt;10 mbar → 约10⁻⁴ mbar → 保压30 min</span>
            </a>
            <a href="#step-3" class="gas-step gas-step-3">
              <div class="gas-step-head"><span class="gas-step-num">03</span><span class="gas-step-tag">加热＋N₂排杂</span></div>
              <h3>吸附剂烘烤再生</h3>
              <p>隔离吸附器两端，经侧向排气并以氮气保护加热；定时巡检流量和气源消耗。</p>
              <span class="gas-target">加热约8 h；每1–2 h巡检</span>
            </a>
            <a href="#step-4" class="gas-step gas-step-4">
              <div class="gas-step-head"><span class="gas-step-num">04</span><span class="gas-step-tag">高真空脱气</span></div>
              <h3>吸附器侧向抽空脱气</h3>
              <p>停止加热并按顺序隔离气源，将分子泵接至侧向阀，持续抽除已解吸杂质。</p>
              <span class="gas-target">7–8 h；目标 &lt;10⁻⁵ mbar</span>
            </a>
            <a href="#step-5" class="gas-step gas-step-5">
              <div class="gas-step-head"><span class="gas-step-num">05</span><span class="gas-step-tag">全回路深抽</span></div>
              <h3>循环主管路深度抽真空</h3>
              <p>恢复批准的全回路连通阀态，对循环主管路、储气罐和相关支路统一深抽。</p>
              <span class="gas-target">≥12 h；压力趋势稳定并通过检漏</span>
            </a>
            <a href="#step-6" class="gas-step gas-step-6">
              <div class="gas-step-head"><span class="gas-step-num">06</span><span class="gas-step-tag">核心洗气</span></div>
              <h3>3次N₂＋1次He梯度洗气</h3>
              <p>每轮执行“受控充气—充分置换—再次抽空”，前三轮使用高纯N₂，末轮使用高纯He。</p>
              <span class="gas-target">每轮约950–1000 → 10 mbar；共4轮</span>
            </a>
            <a href="#step-7" class="gas-step gas-step-7">
              <div class="gas-step-head"><span class="gas-step-num">07</span><span class="gas-step-tag">工作氦回充</span></div>
              <h3>定量回充与杜瓦抽空</h3>
              <p>按本机参数卡向Dump回充高纯⁴He，同时完成低温杜瓦高真空准备和管路隔离。</p>
              <span class="gas-target">本机记录目标：约950 mbar ⁴He</span>
            </a>
            <a href="#step-8" class="gas-step gas-step-8">
              <div class="gas-step-head"><span class="gas-step-num">08</span><span class="gas-step-tag">复位＋降温</span></div>
              <h3>阀门复位与自动降温验证</h3>
              <p>手动完全打开步骤 7 关闭的全部手阀，开启水冷与压缩机；点击 Cool Down 软件自动调配电磁阀降温至 1.65 K（软件阀门无需手动打开）。</p>
              <span class="gas-target">极限基准参考：1.65 K</span>
            </a>
          </div>

          <div class="gas-gates">
            <div class="gas-gate gas-stop"><strong>⛔ 任一步立即停止：</strong>阀号或管路对象无法确认、压力异常上升、检漏不通过、气体纯度不明、通风／氧亏监测异常或人员出现不适。</div>
            <div class="gas-gate gas-accept"><strong>✓ 最终放行：</strong>阀态与连接复位、无泄漏报警、工作气压与真空达标、自动降温曲线通过本机历史基线比较、日志和工单完整。</div>
          </div>
        </section>

        <!-- 步骤 1 (50:50 宽幅布局) -->
        <article id="step-1" class="step-card bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-9 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-6 transition hover:border-brand-400 dark:hover:border-brand-600 card-print">
          <div class="flex items-start justify-between gap-4 border-b border-slate-100 dark:border-slate-800 pb-4">
            <div class="flex items-center gap-3.5">
              <div class="step-badge bg-brand-50 text-brand-700 dark:bg-brand-950 dark:text-brand-300 border border-brand-200 dark:border-brand-800">
                01
              </div>
              <div>
                <h3 class="h3-title font-bold text-slate-900 dark:text-white">步骤 1：Reservoir 全系统升温至室温（300 K）</h3>
                <div class="flex flex-wrap gap-2 mt-1.5">
                  <span class="tag-badge bg-amber-100 text-amber-800 dark:bg-amber-900/50 dark:text-amber-200">⏱️ 耗时：~20 小时</span>
                  <span class="tag-badge bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300">🌡️ 目标：300 K</span>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-3">
              <button type="button" onclick="recordStartTime(1, 'Reservoir 升温 (300K)', 20)" class="text-xs font-semibold px-3 py-1.5 rounded-lg bg-sky-50 text-sky-700 dark:bg-sky-950/60 dark:text-sky-300 border border-sky-200 dark:border-sky-800 hover:bg-sky-100 transition">⏱️ 开始计时</button>
              <label class="flex items-center gap-2 text-sm font-semibold text-slate-700 dark:text-slate-300 cursor-pointer select-none bg-slate-100 dark:bg-slate-800 px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-brand-50 hover:text-brand-600 dark:hover:bg-brand-950 transition">
                <input type="checkbox" data-step="1" data-hours="20" class="step-checkbox w-4 h-4 text-brand-600 rounded focus:ring-brand-500" onchange="updateProgress()">
                <span>标记完成</span>
              </label>
            </div>
          </div>

          <!-- 50:50 一半一半对称网格 -->
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
            
            <!-- 左侧 50%：详细文字说明 -->
            <div class="flex flex-col justify-between space-y-4 text-slate-700 dark:text-slate-200 leading-relaxed text-sm sm:text-base">
              <div class="space-y-2">
                <div class="font-bold text-slate-900 dark:text-white text-base sm:text-lg flex items-center gap-2">
                  <span class="text-brand-600">🎯</span> 核心机理与目的：
                </div>
                <p class="text-slate-600 dark:text-slate-300">
                  当设备长时间停机时，Reservoir 和超导磁体温度缓慢上升，内部吸附冷阱饱和失效并释放出大量杂质气体。必须首先将整个 attoDRY（包括 Sample、VTI 与 Reservoir）主动升温至 <span class="param-pill bg-amber-100 text-amber-900 dark:bg-amber-950 dark:text-amber-200">300 K（室温）</span>，使管壁与冷阱内附着的杂质气体完全解吸。
                </p>
              </div>

              <!-- 阀门速查微卡片 -->
              <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700 text-xs font-mono grid grid-cols-3 gap-2 text-center">
                <div><span class="text-slate-400 block text-[10px]">Scroll 泵</span><strong class="text-red-500">OFF (关)</strong></div>
                <div><span class="text-slate-400 block text-[10px]">Cryo 进/出</span><strong class="text-red-500">CLOSED (关)</strong></div>
                <div><span class="text-slate-400 block text-[10px]">Dump 进/出</span><strong class="text-emerald-500">OPEN (开)</strong></div>
              </div>

              <div class="bg-slate-50 dark:bg-slate-800/80 p-5 rounded-2xl border border-slate-200 dark:border-slate-700 space-y-3">
                <div class="font-bold text-slate-900 dark:text-slate-100 text-base flex items-center gap-2">
                  <span class="text-sky-600">🛠️</span> 标准操作四阶段：
                </div>
                <div class="space-y-3 text-sm sm:text-base">
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
                </div>
              </div>

              <div class="p-4 sm:p-5 rounded-2xl bg-red-50 dark:bg-red-950/40 border-2 border-red-300 dark:border-red-800/80 text-sm sm:text-base text-red-900 dark:text-red-200 font-medium leading-relaxed">
                🚨 <strong>关键安全红线</strong>：等待升温至室温（约 20 小时）。当 Reservoir 升至 300 K 之后，<strong>必须立刻在软件中将 <code>Target temperature [K]</code> 重新调回 3.7 K</strong>！以防止后续降温阶段加热器发生干烧故障。
              </div>
            </div>

            <!-- 右侧 50%：配图展示 -->
            <div class="flex flex-col justify-between space-y-2">
              <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 shadow-sm flex items-center justify-center p-3 h-full">
                <img src="images/slide_3.jpg" alt="升温设置界面与压缩机、水冷机开关" loading="lazy" decoding="async" class="w-full h-auto max-h-[520px] object-contain rounded-xl img-zoom" onclick="openLightbox(this.src, '步骤 1：软件升温设置 300K、Expert 气路状态及压缩机、水冷机关闭面板')" />
              </div>
              <p class="text-center text-xs sm:text-sm text-slate-500 font-medium">📷 图 2.1：升温控制面板、Expert 气路阀门及水冷机/压缩机电源开关</p>
            </div>

          </div>
        </article>

        <!-- 步骤 2 (50:50 宽幅布局) -->
        <article id="step-2" class="step-card bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-9 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-6 transition hover:border-brand-400 dark:hover:border-brand-600 card-print">
          <div class="flex items-start justify-between gap-4 border-b border-slate-100 dark:border-slate-800 pb-4">
            <div class="flex items-center gap-3.5">
              <div class="step-badge bg-brand-50 text-brand-700 dark:bg-brand-950 dark:text-brand-300 border border-brand-200 dark:border-brand-800">
                02
              </div>
              <div>
                <h3 class="h3-title font-bold text-slate-900 dark:text-white">步骤 2：转移分子泵至压缩机并进行粗抽保压验证</h3>
                <div class="flex flex-wrap gap-2 mt-1.5">
                  <span class="tag-badge bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-200">⏱️ 耗时：~1.5 小时</span>
                  <span class="tag-badge bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300">🎯 指标：&lt; 10 mbar &rarr; 10⁻⁴ mbar</span>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-3">
              <button type="button" onclick="recordStartTime(2, '转移分子泵初抽', 1.5)" class="text-xs font-semibold px-3 py-1.5 rounded-lg bg-sky-50 text-sky-700 dark:bg-sky-950/60 dark:text-sky-300 border border-sky-200 dark:border-sky-800 hover:bg-sky-100 transition">⏱️ 开始计时</button>
              <label class="flex items-center gap-2 text-sm font-semibold text-slate-700 dark:text-slate-300 cursor-pointer select-none bg-slate-100 dark:bg-slate-800 px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-brand-50 hover:text-brand-600 dark:hover:bg-brand-950 transition">
                <input type="checkbox" data-step="2" data-hours="1.5" class="step-checkbox w-4 h-4 text-brand-600 rounded focus:ring-brand-500" onchange="updateProgress()">
                <span>标记完成</span>
              </label>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
            
            <!-- 左侧 50% -->
            <div class="flex flex-col justify-between space-y-4 text-slate-700 dark:text-slate-200 leading-relaxed text-sm sm:text-base">
              <div class="space-y-2">
                <div class="font-bold text-slate-900 dark:text-white text-base sm:text-lg flex items-center gap-2">
                  <span class="text-brand-600">🎯</span> 硬件转接与目的：
                </div>
                <p class="text-slate-600 dark:text-slate-300">
                  拆除低温腔体处的波纹管连接，将 Pfeiffer HiCUBE 移动分子泵机组通过金属波纹管连接至<strong>压缩机顶部的服务连通口（Bypass 和 Service 手阀接口）</strong>，卡紧 KF 卡箍并检查氟胶密封圈。
                </p>
              </div>

              <!-- 阀门速查微卡片 -->
              <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700 text-xs font-mono grid grid-cols-3 gap-2 text-center">
                <div><span class="text-slate-400 block text-[10px]">V3 (Service)</span><strong class="text-emerald-500">OPEN (开)</strong></div>
                <div><span class="text-slate-400 block text-[10px]">V4 (Bypass)</span><strong class="text-emerald-500">OPEN (开)</strong></div>
                <div><span class="text-slate-400 block text-[10px]">分子泵接口</span><strong class="text-brand-600">压缩机 Service</strong></div>
              </div>
              
              <div class="bg-slate-50 dark:bg-slate-800/80 p-5 rounded-2xl border border-slate-200 dark:border-slate-700 space-y-3">
                <div class="font-bold text-slate-900 dark:text-slate-100 text-base flex items-center gap-2">
                  <span class="text-sky-600">🛠️</span> 抽气时序与保压检漏步骤：
                </div>
                <div class="space-y-3 text-sm sm:text-base">
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
                </div>
              </div>
            </div>

            <!-- 右侧 50% -->
            <div class="flex flex-col justify-between space-y-2">
              <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 shadow-sm flex items-center justify-center p-3 h-full">
                <img src="images/slide_5.jpg" alt="转移分子泵与管路确认" loading="lazy" decoding="async" class="w-full h-auto max-h-[520px] object-contain rounded-xl img-zoom" onclick="openLightbox(this.src, '步骤 2：拆解低温腔波纹管、转移至压缩机顶部服务口、开启机械泵与管路确认')" />
              </div>
              <p class="text-center text-xs sm:text-sm text-slate-500 font-medium">📷 图 2.2：分子泵转移接驳、手阀操作与气路验证</p>
            </div>

          </div>
        </article>

        <!-- 步骤 3 (50:50 宽幅布局) -->
        <article id="step-3" class="step-card bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-9 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-6 transition hover:border-brand-400 dark:hover:border-brand-600 card-print">
          <div class="flex items-start justify-between gap-4 border-b border-slate-100 dark:border-slate-800 pb-4">
            <div class="flex items-center gap-3.5">
              <div class="step-badge bg-brand-50 text-brand-700 dark:bg-brand-950 dark:text-brand-300 border border-brand-200 dark:border-brand-800">
                03
              </div>
              <div>
                <h3 class="h3-title font-bold text-slate-900 dark:text-white">步骤 3：Reservoir 升温至室温后吸附剂加热烘烤再生</h3>
                <div class="flex flex-wrap gap-2 mt-1.5">
                  <span class="tag-badge bg-orange-100 text-orange-800 dark:bg-orange-900/50 dark:text-orange-200">⏱️ 加热耗时：8h 左右</span>
                  <span class="tag-badge bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-200">🔍 巡检：1~2h 检查氮气流速与消耗</span>
                  <span class="tag-badge bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300">⚡ 连接电源即开始加热</span>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-3">
              <button type="button" onclick="recordStartTime(3, '吸附剂加热烘烤再生', 8)" class="text-xs font-semibold px-3 py-1.5 rounded-lg bg-sky-50 text-sky-700 dark:bg-sky-950/60 dark:text-sky-300 border border-sky-200 dark:border-sky-800 hover:bg-sky-100 transition">⏱️ 开始计时</button>
              <label class="flex items-center gap-2 text-sm font-semibold text-slate-700 dark:text-slate-300 cursor-pointer select-none bg-slate-100 dark:bg-slate-800 px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-brand-50 hover:text-brand-600 dark:hover:bg-brand-950 transition">
                <input type="checkbox" data-step="3" data-hours="8" class="step-checkbox w-4 h-4 text-brand-600 rounded focus:ring-brand-500" onchange="updateProgress()">
                <span>标记完成</span>
              </label>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
            
            <!-- 左侧 50% -->
            <div class="flex flex-col justify-between space-y-4 text-slate-700 dark:text-slate-200 leading-relaxed text-sm sm:text-base">
              <div class="space-y-2">
                <div class="font-bold text-slate-900 dark:text-white text-base sm:text-lg flex items-center gap-2">
                  <span class="text-brand-600">🎯</span> 核心操作与时机原则：
                </div>
                <p class="text-slate-600 dark:text-slate-300">
                  <strong>当 Reservoir 温度上升到室温后，对吸附剂进行加热。</strong>此时吸附剂微孔中吸附的水汽与杂质气体受热释放脱附，必须将两端主阀关紧隔离系统，通过侧向阀门排气，彻底排出解吸杂质。
                </p>
              </div>

              <!-- 阀门速查微卡片 -->
              <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700 text-xs font-mono grid grid-cols-3 gap-2 text-center">
                <div><span class="text-slate-400 block text-[10px]">V7 / V9 (两端主阀)</span><strong class="text-red-500">CLOSED (关紧封起)</strong></div>
                <div><span class="text-slate-400 block text-[10px]">V8 (侧向阀门)</span><strong class="text-emerald-500">OPEN (打开排气)</strong></div>
                <div><span class="text-slate-400 block text-[10px]">气体巡检</span><strong class="text-blue-600">1~2h 查流速消耗</strong></div>
              </div>
              
              <div class="bg-slate-50 dark:bg-slate-800/80 p-5 rounded-2xl border border-slate-200 dark:border-slate-700 space-y-3">
                <div class="font-bold text-slate-900 dark:text-slate-100 text-base flex items-center gap-2">
                  <span class="text-sky-600">🛠️</span> 阀门设定与加热执行步骤：
                </div>
                <ul class="space-y-3 text-sm sm:text-base list-none">
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
                </ul>
              </div>
            </div>

            <!-- 右侧 50% -->
            <div class="flex flex-col justify-between space-y-2">
              <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 shadow-sm flex items-center justify-center p-3 h-full">
                <img src="images/slide_7.jpg" alt="冲洗过滤器（再生）实物图" loading="lazy" decoding="async" class="w-full h-auto max-h-[520px] object-contain rounded-xl img-zoom" onclick="openLightbox(this.src, '步骤 3：过滤器上下主阀关紧两端封起、侧向打开排气、HK-06温控仪加热8h、停加热5分钟关侧向阀')" />
              </div>
              <p class="text-center text-xs sm:text-sm text-slate-500 font-medium">📷 图 2.3：过滤器上下主阀 (V7/V9 关紧封起)、侧向阀门 (V8 打开) 与 HK-06 温控器</p>
            </div>

          </div>
        </article>

        <!-- 步骤 4 (50:50 宽幅布局) -->
        <article id="step-4" class="step-card bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-9 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-6 transition hover:border-brand-400 dark:hover:border-brand-600 card-print">
          <div class="flex items-start justify-between gap-4 border-b border-slate-100 dark:border-slate-800 pb-4">
            <div class="flex items-center gap-3.5">
              <div class="step-badge bg-brand-50 text-brand-700 dark:bg-brand-950 dark:text-brand-300 border border-brand-200 dark:border-brand-800">
                04
              </div>
              <div>
                <h3 class="h3-title font-bold text-slate-900 dark:text-white">步骤 4：通过侧向阀门连接泵对吸附剂抽真空脱气</h3>
                <div class="flex flex-wrap gap-2 mt-1.5">
                  <span class="tag-badge bg-purple-100 text-purple-800 dark:bg-purple-900/50 dark:text-purple-200">⏱️ 耗时：7 ~ 8 小时</span>
                  <span class="tag-badge bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300">🎯 极限真空：&lt; 10⁻⁵ mbar</span>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-3">
              <button type="button" onclick="recordStartTime(4, '吸附剂侧向抽真空脱气', 7.5)" class="text-xs font-semibold px-3 py-1.5 rounded-lg bg-sky-50 text-sky-700 dark:bg-sky-950/60 dark:text-sky-300 border border-sky-200 dark:border-sky-800 hover:bg-sky-100 transition">⏱️ 开始计时</button>
              <label class="flex items-center gap-2 text-sm font-semibold text-slate-700 dark:text-slate-300 cursor-pointer select-none bg-slate-100 dark:bg-slate-800 px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-brand-50 hover:text-brand-600 dark:hover:bg-brand-950 transition">
                <input type="checkbox" data-step="4" data-hours="7.5" class="step-checkbox w-4 h-4 text-brand-600 rounded focus:ring-brand-500" onchange="updateProgress()">
                <span>标记完成</span>
              </label>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
            
            <!-- 左侧 50% -->
            <div class="flex flex-col justify-between space-y-4 text-slate-700 dark:text-slate-200 leading-relaxed text-sm sm:text-base">
              <div class="space-y-2">
                <div class="font-bold text-slate-900 dark:text-white text-base sm:text-lg flex items-center gap-2">
                  <span class="text-brand-600">🎯</span> 脱气活化逻辑与操作原则：
                </div>
                <p class="text-slate-600 dark:text-slate-300">
                  <strong>加热完后，对吸附剂进行抽真空，通过侧向阀门抽，即将侧向阀门打开，然后连接泵，将吸附剂抽真空。</strong>在冷阱与系统主管路完全隔离的状态下，利用分子泵直接连接侧向端口进行深度高真空脱气，使吸附剂恢复超低温下的极强吸附能力。
                </p>
              </div>

              <!-- 阀门速查微卡片 -->
              <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700 text-xs font-mono grid grid-cols-3 gap-2 text-center">
                <div><span class="text-slate-400 block text-[10px]">V7 / V9 (两端主阀)</span><strong class="text-red-500">CLOSED (关)</strong></div>
                <div><span class="text-slate-400 block text-[10px]">V8 (侧向抽气阀)</span><strong class="text-emerald-500">OPEN (开)</strong></div>
                <div><span class="text-slate-400 block text-[10px]">分子泵接口</span><strong class="text-purple-600">直连侧向阀门</strong></div>
              </div>
              
              <div class="bg-slate-50 dark:bg-slate-800/80 p-5 rounded-2xl border border-slate-200 dark:border-slate-700 space-y-3">
                <div class="font-bold text-slate-900 dark:text-slate-100 text-base flex items-center gap-2">
                  <span class="text-sky-600">🛠️</span> 标准侧向抽真空操作规程：
                </div>
                <ul class="space-y-3 text-sm sm:text-base list-none">
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
                </ul>
              </div>
            </div>

            <!-- 右侧 50% -->
            <div class="flex flex-col justify-between space-y-2">
              <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 shadow-sm flex items-center justify-center p-3 h-full">
                <img src="images/slide_8.jpg" alt="抽真空过滤器实物图" loading="lazy" decoding="async" class="w-full h-auto max-h-[520px] object-contain rounded-xl img-zoom" onclick="openLightbox(this.src, '步骤 4：关闭上下直通阀、转接环连接分子泵至侧向阀门口打开抽高真空')" />
              </div>
              <p class="text-center text-xs sm:text-sm text-slate-500 font-medium">📷 图 2.4：KF 转接环连接分子泵至过滤器侧向阀门 (V8) 抽真空</p>
            </div>

          </div>
        </article>

        <!-- 步骤 5 (50:50 宽幅布局) -->
        <article id="step-5" class="step-card bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-9 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-6 transition hover:border-brand-400 dark:hover:border-brand-600 card-print">
          <div class="flex items-start justify-between gap-4 border-b border-slate-100 dark:border-slate-800 pb-4">
            <div class="flex items-center gap-3.5">
              <div class="step-badge bg-brand-50 text-brand-700 dark:bg-brand-950 dark:text-brand-300 border border-brand-200 dark:border-brand-800">
                05
              </div>
              <div>
                <h3 class="h3-title font-bold text-slate-900 dark:text-white">步骤 5：全系统循环主管路深度抽真空</h3>
                <div class="flex flex-wrap gap-2 mt-1.5">
                  <span class="tag-badge bg-indigo-100 text-indigo-800 dark:bg-indigo-900/50 dark:text-indigo-200">⏱️ 耗时：12+ 小时 (通宵)</span>
                  <span class="tag-badge bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300">🔄 全回路连通抽气</span>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-3">
              <button type="button" onclick="recordStartTime(5, '全系统通宵抽真空', 12)" class="text-xs font-semibold px-3 py-1.5 rounded-lg bg-sky-50 text-sky-700 dark:bg-sky-950/60 dark:text-sky-300 border border-sky-200 dark:border-sky-800 hover:bg-sky-100 transition">⏱️ 开始计时</button>
              <label class="flex items-center gap-2 text-sm font-semibold text-slate-700 dark:text-slate-300 cursor-pointer select-none bg-slate-100 dark:bg-slate-800 px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-brand-50 hover:text-brand-600 dark:hover:bg-brand-950 transition">
                <input type="checkbox" data-step="5" data-hours="12" class="step-checkbox w-4 h-4 text-brand-600 rounded focus:ring-brand-500" onchange="updateProgress()">
                <span>标记完成</span>
              </label>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
            
            <!-- 左侧 50% -->
            <div class="flex flex-col justify-between space-y-4 text-slate-700 dark:text-slate-200 leading-relaxed text-sm sm:text-base">
              <div class="space-y-2">
                <div class="font-bold text-slate-900 dark:text-white text-base sm:text-lg flex items-center gap-2">
                  <span class="text-brand-600">🎯</span> 系统并网与目的：
                </div>
                <p class="text-slate-600 dark:text-slate-300">
                  将活化完毕的吸附冷阱重新并入主循环气路，利用分子泵对整个闭环循环管线、储气罐以及腔体内部进行长时间深度高真空排空，彻底消除死角残留。
                </p>
              </div>

              <!-- 阀门速查微卡片 -->
              <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700 text-xs font-mono grid grid-cols-3 gap-2 text-center">
                <div><span class="text-slate-400 block text-[10px]">全套电磁阀</span><strong class="text-emerald-500">OPEN (全开)</strong></div>
                <div><span class="text-slate-400 block text-[10px]">V7/V9 & V8</span><strong class="text-emerald-500">OPEN (全通)</strong></div>
                <div><span class="text-slate-400 block text-[10px]">建议运行</span><strong class="text-indigo-600">通宵连续抽空</strong></div>
              </div>
              
              <div class="bg-slate-50 dark:bg-slate-800/80 p-5 rounded-2xl border border-slate-200 dark:border-slate-700 space-y-3">
                <div class="font-bold text-slate-900 dark:text-slate-100 text-base flex items-center gap-2">
                  <span class="text-sky-600">🛠️</span> 操作时序与抽空阶梯：
                </div>
                <div class="space-y-3 text-sm sm:text-base">
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
                </div>
              </div>
            </div>

            <!-- 右侧 50% -->
            <div class="flex flex-col justify-between space-y-2">
              <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 shadow-sm flex items-center justify-center p-3 h-full">
                <img src="images/slide_9.jpg" alt="抽真空管路实物图" loading="lazy" decoding="async" class="w-full h-auto max-h-[520px] object-contain rounded-xl img-zoom" onclick="openLightbox(this.src, '步骤 5：分子泵接压缩机、打开全套阀门与软件监控界面')" />
              </div>
              <p class="text-center text-xs sm:text-sm text-slate-500 font-medium">📷 图 2.5：管路重连、软件气路全开与长时间抽空状态</p>
            </div>

          </div>
        </article>

        <!-- 步骤 6 (50:50 宽幅布局) -->
        <article id="step-6" class="step-card bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-9 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-6 transition hover:border-brand-400 dark:hover:border-brand-600 card-print">
          <div class="flex items-start justify-between gap-4 border-b border-slate-100 dark:border-slate-800 pb-4">
            <div class="flex items-center gap-3.5">
              <div class="step-badge bg-brand-50 text-brand-700 dark:bg-brand-950 dark:text-brand-300 border border-brand-200 dark:border-brand-800">
                06
              </div>
              <div>
                <h3 class="h3-title font-bold text-slate-900 dark:text-white">步骤 6：高纯气体梯度洗气净化（3次 N₂ + 1次 He）</h3>
                <div class="flex flex-wrap gap-2 mt-1.5">
                  <span class="tag-badge bg-emerald-100 text-emerald-800 dark:bg-emerald-900/50 dark:text-emerald-200">⏱️ 耗时：~14 小时</span>
                  <span class="tag-badge bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300">🧪 充抽置换净化</span>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-3">
              <button type="button" onclick="recordStartTime(6, '梯度洗气净化', 14)" class="text-xs font-semibold px-3 py-1.5 rounded-lg bg-sky-50 text-sky-700 dark:bg-sky-950/60 dark:text-sky-300 border border-sky-200 dark:border-sky-800 hover:bg-sky-100 transition">⏱️ 开始计时</button>
              <label class="flex items-center gap-2 text-sm font-semibold text-slate-700 dark:text-slate-300 cursor-pointer select-none bg-slate-100 dark:bg-slate-800 px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-brand-50 hover:text-brand-600 dark:hover:bg-brand-950 transition">
                <input type="checkbox" data-step="6" data-hours="14" class="step-checkbox w-4 h-4 text-brand-600 rounded focus:ring-brand-500" onchange="updateProgress()">
                <span>标记完成</span>
              </label>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
            
            <!-- 左侧 50% -->
            <div class="flex flex-col justify-between space-y-4 text-slate-700 dark:text-slate-200 leading-relaxed text-sm sm:text-base">
              <div class="space-y-2">
                <div class="font-bold text-slate-900 dark:text-white text-base sm:text-lg flex items-center gap-2">
                  <span class="text-brand-600">🎯</span> 动态置换原理：
                </div>
                <p class="text-slate-600 dark:text-slate-300">
                  基于「高纯气稀释扩散 &rarr; 深度排空抽取」的动态置换原理，通过 3 轮高纯氮气洗涤和 1 轮高纯氦气洗涤，将微孔和管道深处最微量的不可凝杂质彻底置换清除。
                </p>
              </div>

              <!-- 阀门速查微卡片 -->
              <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700 text-xs font-mono grid grid-cols-3 gap-2 text-center">
                <div><span class="text-slate-400 block text-[10px]">充气上限</span><strong class="text-emerald-500">1000 mbar</strong></div>
                <div><span class="text-slate-400 block text-[10px]">抽空指标</span><strong class="text-blue-500">&lt; 10 mbar</strong></div>
                <div><span class="text-slate-400 block text-[10px]">轮次配比</span><strong class="text-purple-600">3次 N₂ + 1次 He</strong></div>
              </div>
              
              <div class="bg-slate-50 dark:bg-slate-800/80 p-5 rounded-2xl border border-slate-200 dark:border-slate-700 space-y-3">
                <div class="font-bold text-slate-900 dark:text-slate-100 text-base flex items-center gap-2">
                  <span class="text-sky-600">🛠️</span> 梯度洗气操作标准：
                </div>
                <div class="space-y-3 text-sm sm:text-base">
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
                </div>
              </div>
            </div>

            <!-- 右侧 50% -->
            <div class="flex flex-col justify-between space-y-2">
              <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 shadow-sm flex items-center justify-center p-3 h-full">
                <img src="images/slide_10.jpg" alt="洗气界面与压力表位置" loading="lazy" decoding="async" class="w-full h-auto max-h-[520px] object-contain rounded-xl img-zoom" onclick="openLightbox(this.src, '步骤 6：洗气进气口、Dump 充气至 950-1000mbar 及 Cryo-in 抽至 10mbar 压力位置')" />
              </div>
              <p class="text-center text-xs sm:text-sm text-slate-500 font-medium">📷 图 2.6：充气进气接头与软件压力监测点（1:Cryo-out, 2:Dump, 3:Cryo-in）</p>
            </div>

          </div>
        </article>

        <!-- 步骤 7 (50:50 宽幅布局) -->
        <article id="step-7" class="step-card bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-9 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-6 transition hover:border-brand-400 dark:hover:border-brand-600 card-print">
          <div class="flex items-start justify-between gap-4 border-b border-slate-100 dark:border-slate-800 pb-4">
            <div class="flex items-center gap-3.5">
              <div class="step-badge bg-brand-50 text-brand-700 dark:bg-brand-950 dark:text-brand-300 border border-brand-200 dark:border-brand-800">
                07
              </div>
              <div>
                <h3 class="h3-title font-bold text-slate-900 dark:text-white">步骤 7：补充工作氦气与低温杜瓦抽真空</h3>
                <div class="flex flex-wrap gap-2 mt-1.5">
                  <span class="tag-badge bg-teal-100 text-teal-800 dark:bg-teal-900/50 dark:text-teal-200">⏱️ 耗时：~1 小时</span>
                  <span class="tag-badge bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300">🎯 充注目标：950 mbar ⁴He</span>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-3">
              <button type="button" onclick="recordStartTime(7, '补充工作氦气', 1)" class="text-xs font-semibold px-3 py-1.5 rounded-lg bg-sky-50 text-sky-700 dark:bg-sky-950/60 dark:text-sky-300 border border-sky-200 dark:border-sky-800 hover:bg-sky-100 transition">⏱️ 开始计时</button>
              <label class="flex items-center gap-2 text-sm font-semibold text-slate-700 dark:text-slate-300 cursor-pointer select-none bg-slate-100 dark:bg-slate-800 px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-brand-50 hover:text-brand-600 dark:hover:bg-brand-950 transition">
                <input type="checkbox" data-step="7" data-hours="1" class="step-checkbox w-4 h-4 text-brand-600 rounded focus:ring-brand-500" onchange="updateProgress()">
                <span>标记完成</span>
              </label>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
            
            <!-- 左侧 50% -->
            <div class="flex flex-col justify-between space-y-4 text-slate-700 dark:text-slate-200 leading-relaxed text-sm sm:text-base">
              <div class="space-y-2">
                <div class="font-bold text-slate-900 dark:text-white text-base sm:text-lg flex items-center gap-2">
                  <span class="text-brand-600">🎯</span> 氦气充注与绝热维护：
                </div>
                <p class="text-slate-600 dark:text-slate-300">
                  为闭环循环系统补充超纯工作介质氦气（⁴He），并为低温腔体的外层真空绝热杜瓦（Vacuum Dewar）进行高真空抽取维护，保障超低温工况下的绝热性能。
                </p>
              </div>

              <!-- 阀门速查微卡片 -->
              <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700 text-xs font-mono grid grid-cols-3 gap-2 text-center">
                <div><span class="text-slate-400 block text-[10px]">Dump 充氦</span><strong class="text-teal-600">950 mbar</strong></div>
                <div><span class="text-slate-400 block text-[10px]">Cryo-out / Dump-out</span><strong class="text-red-500">CLOSED (关)</strong></div>
                <div><span class="text-slate-400 block text-[10px]">外杜瓦真空</span><strong class="text-brand-600">分子泵独立抽</strong></div>
              </div>
              
              <div class="bg-slate-50 dark:bg-slate-800/80 p-5 rounded-2xl border border-slate-200 dark:border-slate-700 space-y-3">
                <div class="font-bold text-slate-900 dark:text-slate-100 text-base flex items-center gap-2">
                  <span class="text-sky-600">🛠️</span> 充气与杜瓦维护六步法：
                </div>
                <ul class="space-y-2.5 text-sm sm:text-base list-none">
                  <li><span class="software-tag">💻 软件设置</span>关闭分子泵与 Scroll Pump；在软件 Expert 界面中<strong>关闭 <code>Cryo-out</code> 与 <code>Dump-out</code></strong> 气控阀。</li>
                  <li class="manual-action-card">
                    <span class="manual-tag">✋ 现场手动</span><strong>手动关紧压缩机后部手阀（中南大学 1、2 号阀）及过滤器侧阀门（V8）</strong>。
                  </li>
                  <li><span class="manual-tag">✋ 现场手动</span><span class="software-tag">💻 软件配合</span><strong>通过 <code>Dump-in</code> 阀向 Dump 储气罐充入高纯氦气至标准工作压力：<span class="param-pill bg-teal-100 text-teal-900 dark:bg-teal-950 dark:text-teal-200">950 mbar</span></strong>。</li>
                  <li><span class="manual-tag">✋ 现场手动</span>充气完成后<strong>关闭 Dump-in 阀门</strong>，<strong>手动将充气连接软管内残存气体抽至 &lt; 10 mbar 后拆卸接头</strong>。</li>
                  <li class="manual-action-card">
                    <span class="manual-tag">✋ 现场手动</span><strong>杜瓦抽真空转接</strong>：<strong>将 Pfeiffer 分子泵机组推移至 attoDRY 主机，通过波纹管连接至真空杜瓦抽气口并卡紧卡箍，开启分子泵对低温真空绝热杜瓦（Vacuum Dewar）独立抽高真空</strong>。
                  </li>
                </ul>
              </div>
            </div>

            <!-- 右侧 50% -->
            <div class="flex flex-col justify-between space-y-2">
              <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 shadow-sm flex items-center justify-center p-3 h-full">
                <img src="images/slide_11.jpg" alt="补气与真空杜瓦抽真空" loading="lazy" decoding="async" class="w-full h-auto max-h-[520px] object-contain rounded-xl img-zoom" onclick="openLightbox(this.src, '步骤 7：DUMP 补气至 950mbar、关闭相关阀门并对真空杜瓦抽高真空')" />
              </div>
              <p class="text-center text-xs sm:text-sm text-slate-500 font-medium">📷 图 2.7：Dump 补气 950mbar 界面与杜瓦抽空连接</p>
            </div>

          </div>
        </article>

                <!-- 步骤 8 (50:50 宽幅布局) -->
        <article id="step-8" class="step-card bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-9 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-6 transition hover:border-brand-400 dark:hover:border-brand-600 card-print">
          <div class="flex items-start justify-between gap-4 border-b border-slate-100 dark:border-slate-800 pb-4">
            <div class="flex items-center gap-3.5">
              <div class="step-badge bg-emerald-50 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800">
                08
              </div>
              <div>
                <h3 class="h3-title font-bold text-slate-900 dark:text-white">步骤 8：系统复位与自动化降温启动（目标极限 1.65 K）</h3>
                <div class="flex flex-wrap gap-2 mt-1.5">
                  <span class="tag-badge bg-emerald-100 text-emerald-800 dark:bg-emerald-900/50 dark:text-emerald-200">❄️ 自动制冷降温</span>
                  <span class="tag-badge bg-teal-100 text-teal-800 dark:bg-teal-900/50 dark:text-teal-200">⏱️ 降温耗时：约 3–4 小时</span>
                  <span class="tag-badge bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300">🎯 极限基准温度：1.65 K</span>
                  <span class="tag-badge bg-purple-100 text-purple-800 dark:bg-purple-900/50 dark:text-purple-200">🧲 超导磁场就绪：±9 T</span>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-3">
              <button type="button" onclick="recordStartTime(8, '自动化降温', 3.5)" class="text-xs font-semibold px-3 py-1.5 rounded-lg bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800 hover:bg-emerald-100 transition">⏱️ 开始计时</button>
              <label class="flex items-center gap-2 text-sm font-semibold text-slate-700 dark:text-slate-300 cursor-pointer select-none bg-slate-100 dark:bg-slate-800 px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-brand-50 hover:text-brand-600 dark:hover:bg-brand-950 transition">
                <input type="checkbox" data-step="8" data-hours="3.5" class="step-checkbox w-4 h-4 text-brand-600 rounded focus:ring-brand-500" onchange="updateProgress()">
                <span>标记完成</span>
              </label>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
            
            <!-- 左侧 50%：操作规程与核心要则 -->
            <div class="flex flex-col justify-between space-y-4 text-slate-700 dark:text-slate-200 leading-relaxed text-sm sm:text-base">
              <div class="space-y-2">
                <div class="font-bold text-slate-900 dark:text-white text-base sm:text-lg flex items-center gap-2">
                  <span class="text-emerald-600">🎯</span> 阀门物理复位与闭环自动化降温：
                </div>
                <p class="text-slate-600 dark:text-slate-300">
                  完成步骤 7 的工作氦气充注（Dump 950 mbar）与杜瓦高真空维护后，系统具备超高纯净度循环环境。<strong>在降温前，必须将步骤 7 中现场手动关闭的阀门全部打开</strong>，然后才可以开启水冷和压缩机启动降温；<strong>软件上的电磁气控阀由 attoDRY 控制系统全自动调配开启，严禁或无需在软件上手动打开</strong>。
                </p>
              </div>

              <!-- 阀门复位速查微卡片 -->
              <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700 text-xs font-mono grid grid-cols-3 gap-2 text-center">
                <div><span class="text-slate-400 block text-[10px]">步骤7手动手阀</span><strong class="text-emerald-600">全部手动旋开 (开)</strong></div>
                <div><span class="text-slate-400 block text-[10px]">软件电磁气控阀</span><strong class="text-sky-600">Cool Down 自动接管</strong></div>
                <div><span class="text-slate-400 block text-[10px]">硬件外围状态</span><strong class="text-brand-600">水冷＋压缩机开启</strong></div>
              </div>

              <!-- 核心防呆警示框：现场手动 vs 软件自动 -->
              <div class="p-4 rounded-xl bg-amber-50 dark:bg-amber-950/40 border-2 border-amber-300 dark:border-amber-700 space-y-2 text-xs sm:text-sm">
                <div class="font-bold text-amber-900 dark:text-amber-200 flex items-center gap-2 text-sm sm:text-base">
                  <span>⚠️</span> 降温前置关键防呆警示（物理手动 vs 软件自控）：
                </div>
                <ul class="space-y-1.5 text-amber-800 dark:text-amber-300 list-disc list-inside">
                  <li><strong>【物理手动必须全部打开】</strong>：必须现场<strong>手动将步骤 7 中关闭的所有物理阀门全部旋开（压缩机后部中南大学 1、2 号阀、过滤器侧阀门 V8 及管路运行手阀）</strong>。必须在上述手阀全部开通后方可启动降温，严禁在手阀关闭状态下开启压缩机制冷！</li>
                  <li><strong>【软件气控阀全自动操作】</strong>：步骤 7 在软件中关闭的气控阀（<code>Cryo-out</code>、<code>Dump-out</code> 及 <code>Scroll Pump</code>），<strong>在点击 <code>Cool Down</code> 按钮后系统会自动进行操作与时序开启，不用在软件上手动打开</strong>，避免人工误操作干扰自动化制冷时序！</li>
                </ul>
              </div>

              <!-- 降温启动四步执行卡片 -->
              <div class="bg-slate-50 dark:bg-slate-800/80 p-5 rounded-2xl border border-slate-200 dark:border-slate-700 space-y-3">
                <div class="font-bold text-slate-900 dark:text-slate-100 text-base flex items-center gap-2">
                  <span class="text-emerald-600">🛠️</span> 降温启动四步执行规范：
                </div>
                <ul class="space-y-3 text-sm sm:text-base list-none">
                  <li class="manual-action-card">
                    <span class="manual-tag">✋ 现场手动</span><strong>1. 样品腔充交换气</strong>：<br>
                    手动向样品腔（Sample Space）充入适量交换气体（Exchange Gas），恢复腔体与样品之间的低温热传导路径。
                  </li>
                  <li class="manual-action-card">
                    <span class="manual-tag">✋ 现场手动</span><strong>2. 打开步骤 7 关闭的全部手动阀门（核心前置条件）</strong>：<br>
                    • <strong>手动拧开压缩机后部手阀（中南大学 1、2 号阀）</strong>，打通压缩机进气与排气主循环管路；<br>
                    • <strong>手动拧开过滤器侧阀门（V8）及管路运行手阀</strong>；<br>
                    • <strong>杜瓦抽气口复位</strong>：停止分子泵抽杜瓦，拆除金属波纹管，确保杜瓦抽气盲板与卡箍牢固锁紧密封。
                  </li>
                  <li class="manual-action-card">
                    <span class="manual-tag">✋ 现场手动</span><strong>3. 开启水冷机与压缩机总电源</strong>：<br>
                    • <strong>手动开启中和循环水冷机总电源</strong>（确认水温 &lt; 25℃、循环水压正常稳定）；<br>
                    • <strong>手动旋转开启 CRYOMECH 氦压缩机电源总开关</strong>。
                  </li>
                  <li>
                    <span class="software-tag">💻 软件自控</span><strong>4. 点击 Cool Down 启动自动降温（无需手动操作软件阀门）</strong>：<br>
                    在 attoDRY 控制软件主界面直接<strong>点击 <code>Cool Down</code> 按钮</strong>。系统会自动调配电磁气控阀与闭环制冷循环，<strong>软件上的阀门会自动操作开启，不用手动打开</strong>，系统全自动平稳降温至 <strong class="text-brand-600">1.65 K</strong> 极限基温。
                  </li>
                </ul>
              </div>

            </div>

            <!-- 右侧 50%：原厂指导 slide_12 -->
            <div class="flex flex-col justify-between space-y-2">
              <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 shadow-sm flex items-center justify-center p-3 h-full">
                <img src="images/slide_12.jpg" alt="降温与阀门操作说明" loading="lazy" decoding="async" class="w-full h-auto max-h-[520px] object-contain rounded-xl img-zoom" onclick="openLightbox(this.src, '步骤 8：样品腔补气、打开图7关闭的阀门、开水冷与压缩机、软件点击降温自动开启')" />
              </div>
              <p class="text-center text-xs sm:text-sm text-slate-500 font-medium">📷 图 2.8：降温启动操作指引（样品腔补气、打开图7关闭阀门、开水冷与压缩机及软件自动开启降温）</p>
            </div>

          </div>
        </article>

      </section>


      <!-- ============================================== -->
      <!-- 第三部分：管路拓扑 P&ID 与全步骤阀门状态矩阵 -->
      <!-- ============================================== -->
      <section id="sec-pid-mapping" class="content-section bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-10 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-8">
        <div class="flex items-center gap-3.5 border-b border-slate-100 dark:border-slate-800 pb-5">
          <span class="p-3 rounded-xl bg-sky-500 text-white font-bold text-xl shadow-sm">3</span>
          <div>
            <h2 class="h2-title font-bold text-slate-900 dark:text-white tracking-tight">
              管路拓扑 P&ID 与全步骤阀门状态矩阵速查
            </h2>
            <p class="text-sm text-slate-500 dark:text-slate-400">attoDRY 2100 标准管路工程原理图及各步骤阀门开关状态详查矩阵</p>
          </div>
        </div>

        <!-- 单张居中清晰展示 P&ID 示意图 (宽幅高清晰度) -->
        <div class="space-y-3">
          <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-700 bg-white p-6 sm:p-8 shadow-sm flex items-center justify-center">
            <img src="images/slide_13.jpg" alt="P&ID 示意图" loading="lazy" decoding="async" class="w-full max-w-4xl h-auto object-contain img-zoom" onclick="openLightbox(this.src, 'attoDRY 2100 标准管路结构示意图 (P&ID) 详图标注')" />
          </div>
          <p class="text-center text-sm text-slate-500 dark:text-slate-400 font-medium">
            📷 图 3.1：attoDRY 2100 系统标准管路原理图（标注 V1~V9、Cryo-in/out、Dump-in/out、Service、Bypass 及真空计位置，点击可全屏高清放大）
          </p>
        </div>

        <!-- 阀门状态矩阵 -->
        <div id="sec-valve-matrix" class="mt-8 space-y-3.5">
          <div class="flex items-center justify-between">
            <h3 class="font-bold text-base sm:text-lg text-slate-900 dark:text-white flex items-center gap-2">
              <span>🎛️</span> 8 大步骤阀门状态速查矩阵 (Valve Matrix)
            </h3>
            <span class="text-xs sm:text-sm text-slate-400">🟢 开 / 🔴 关 / ⚙️ 特殊状态</span>
          </div>

          <div class="overflow-x-auto rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm">
            <table class="w-full text-left text-xs sm:text-sm text-slate-700 dark:text-slate-200">
              <caption class="sr-only">八步气路维护流程的阀门状态矩阵</caption>
              <thead class="bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-100 font-bold border-b border-slate-200 dark:border-slate-700 text-center">
                <tr class="border-b border-slate-200 dark:border-slate-700 text-xs uppercase tracking-wider">
                  <th rowspan="2" class="p-3.5 text-left text-sm border-r border-slate-200 dark:border-slate-700">步骤序号与名称</th>
                  <th colspan="5" class="p-2 bg-amber-500/10 text-amber-700 dark:text-amber-300 border-r border-slate-200 dark:border-slate-700 font-bold">✋ 现场物理手动阀门组</th>
                  <th colspan="3" class="p-2 bg-sky-500/10 text-sky-700 dark:text-sky-300 border-r border-slate-200 dark:border-slate-700 font-bold">💻 attoDRY 软件气控电磁阀组</th>
                  <th class="p-2 bg-purple-500/10 text-purple-700 dark:text-purple-300 font-bold">外设泵组</th>
                </tr>
                <tr>
                  <th class="p-2.5 text-amber-800 dark:text-amber-300 font-bold">后阀 1/2<br><span class="text-[10px] font-normal opacity-80">(V1/V2)</span></th>
                  <th class="p-2.5">V3<br><span class="text-[10px] font-normal opacity-80">(Service)</span></th>
                  <th class="p-2.5">V4<br><span class="text-[10px] font-normal opacity-80">(Bypass)</span></th>
                  <th class="p-2.5">V7/V9<br><span class="text-[10px] font-normal opacity-80">(直通)</span></th>
                  <th class="p-2.5 border-r border-slate-200 dark:border-slate-700">V8<br><span class="text-[10px] font-normal opacity-80">(侧阀)</span></th>
                  <th class="p-2.5">Scroll泵</th>
                  <th class="p-2.5">Cryo 进/出</th>
                  <th class="p-2.5 border-r border-slate-200 dark:border-slate-700">Dump 进/出</th>
                  <th class="p-2.5 text-left text-xs">分子泵连接位置</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 dark:divide-slate-800 text-center font-mono">
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50">
                  <td class="p-3.5 text-left font-sans font-bold text-slate-900 dark:text-white text-sm border-r border-slate-100 dark:border-slate-800">1. Reservoir 升温</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-red-500 font-bold border-r border-slate-100 dark:border-slate-800">关</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-emerald-500 font-bold border-r border-slate-100 dark:border-slate-800">开</td>
                  <td class="p-3 text-left font-sans text-slate-400">停用</td>
                </tr>
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50">
                  <td class="p-3.5 text-left font-sans font-bold text-slate-900 dark:text-white text-sm border-r border-slate-100 dark:border-slate-800">2. 气路初抽保压</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-red-500 font-bold border-r border-slate-100 dark:border-slate-800">关</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold border-r border-slate-100 dark:border-slate-800">开</td>
                  <td class="p-3 text-left font-sans text-brand-600 font-bold">接压缩机 Service 口</td>
                </tr>
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50">
                  <td class="p-3.5 text-left font-sans font-bold text-slate-900 dark:text-white text-sm border-r border-slate-100 dark:border-slate-800">3. 吸附剂加热再生</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-red-500 font-bold">关 (封起)</td>
                  <td class="p-3 text-emerald-500 font-bold border-r border-slate-100 dark:border-slate-800">开 (排气)</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-red-500 font-bold border-r border-slate-100 dark:border-slate-800">关</td>
                  <td class="p-3 text-left font-sans text-orange-600 font-bold">加热套加热 8h 左右</td>
                </tr>
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50">
                  <td class="p-3.5 text-left font-sans font-bold text-slate-900 dark:text-white text-sm border-r border-slate-100 dark:border-slate-800">4. 吸附剂侧向抽真空</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-emerald-500 font-bold border-r border-slate-100 dark:border-slate-800">开 (抽气)</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-red-500 font-bold border-r border-slate-100 dark:border-slate-800">关</td>
                  <td class="p-3 text-left font-sans text-purple-600 font-bold">接过滤器侧向阀门抽空</td>
                </tr>
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50">
                  <td class="p-3.5 text-left font-sans font-bold text-slate-900 dark:text-white text-sm border-r border-slate-100 dark:border-slate-800">5. 全管路深度抽真空</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold border-r border-slate-100 dark:border-slate-800">开</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold border-r border-slate-100 dark:border-slate-800">开</td>
                  <td class="p-3 text-left font-sans text-brand-600 font-bold">接压缩机 Service 口</td>
                </tr>
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50">
                  <td class="p-3.5 text-left font-sans font-bold text-slate-900 dark:text-white text-sm border-r border-slate-100 dark:border-slate-800">6. 循环洗气 (N₂/He)</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-red-500 font-bold border-r border-slate-100 dark:border-slate-800">关</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold border-r border-slate-100 dark:border-slate-800">开</td>
                  <td class="p-3 text-left font-sans text-emerald-600 font-bold">接 N₂/He 气瓶与抽空</td>
                </tr>
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 bg-sky-50/40 dark:bg-sky-950/20">
                  <td class="p-3.5 text-left font-sans font-bold text-sky-900 dark:text-sky-300 text-sm border-r border-slate-100 dark:border-slate-800">7. 充工作氦气(950mbar)</td>
                  <td class="p-3 text-red-600 font-extrabold bg-red-100/60 dark:bg-red-950/60">关 (手动)</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-red-600 font-extrabold bg-red-100/60 dark:bg-red-950/60 border-r border-slate-100 dark:border-slate-800">关 (手动)</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-red-500 font-bold">关</td>
                  <td class="p-3 text-teal-500 font-bold border-r border-slate-100 dark:border-slate-800">进开/出关</td>
                  <td class="p-3 text-left font-sans text-teal-600 font-bold">移至主机抽真空杜瓦</td>
                </tr>
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 bg-emerald-50/40 dark:bg-emerald-950/20">
                  <td class="p-3.5 text-left font-sans font-bold text-emerald-900 dark:text-emerald-300 text-sm border-r border-slate-100 dark:border-slate-800">8. 自动降温至 1.65 K</td>
                  <td class="p-3 text-emerald-700 font-extrabold bg-emerald-100/80 dark:bg-emerald-950/80">必须手动开</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-500 font-bold">开</td>
                  <td class="p-3 text-emerald-700 font-extrabold bg-emerald-100/80 dark:bg-emerald-950/80 border-r border-slate-100 dark:border-slate-800">手动开</td>
                  <td class="p-3 text-emerald-500 font-bold">自控</td>
                  <td class="p-3 text-emerald-500 font-bold">自控</td>
                  <td class="p-3 text-emerald-500 font-bold border-r border-slate-100 dark:border-slate-800">自控</td>
                  <td class="p-3 text-left font-sans text-slate-400">杜瓦保温完成拆除</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

          <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 text-xs sm:text-sm text-slate-600 dark:text-slate-300 space-y-1.5 leading-relaxed">
            <div class="font-bold text-slate-900 dark:text-white flex items-center gap-2">
              <span>💡</span> 阀门矩阵关键操作要则说明：
            </div>
            <div>• <strong>步骤 8 降温物理手阀复位【必须全部手动开启】</strong>：在启动降温前，必须现场手动将步骤 7 中关紧的物理手阀（压缩机后部中南大学 1、2 号阀、V3、V4、过滤器侧阀门 V8 等）全部打开，确保主循环管路彻底畅通。</div>
            <div>• <strong>软件电磁气控阀【软件全自动时序调配】</strong>：矩阵中标注为“自控”的阀门（Scroll 泵、Cryo 进/出、Dump 进/出），在 attoDRY 软件主界面点击 <code>Cool Down</code> 按钮后由程序全自动按制冷时序接管和控制开启，<strong>无需（也切勿）在软件界面上手动打开</strong>。</div>
          </div>


      </section>


      <!-- ============================================== -->
      <!-- 第四部分：Pfeiffer HiCUBE 分子泵机组操作 (50:50 宽幅布局) -->
      <!-- ============================================== -->
      <section id="sec-pfeiffer-dcu" class="content-section bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-10 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-6">
        <div class="flex items-center gap-3.5 border-b border-slate-100 dark:border-slate-800 pb-5">
          <span class="p-3 rounded-xl bg-sky-500 text-white font-bold text-xl shadow-sm">4</span>
          <div>
            <h2 class="h2-title font-bold text-slate-900 dark:text-white tracking-tight">
              Pfeiffer HiCUBE 分子泵机组参数与指令速查
            </h2>
            <p class="text-sm text-slate-500 dark:text-slate-400">DCU 200 显示控制面板核心参数代码与按键操作规范</p>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
          
          <!-- 左侧 50%：参数表 -->
          <div class="overflow-hidden rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm flex flex-col justify-between">
            <table class="w-full text-left text-xs sm:text-sm text-slate-700 dark:text-slate-200">
              <caption class="sr-only">Pfeiffer HiCUBE 泵站参数和按键速查表</caption>
              <thead class="bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-100 font-bold border-b border-slate-200 dark:border-slate-700">
                <tr>
                  <th class="p-4 text-sm">参数代码 / 按键</th>
                  <th class="p-4 text-sm">功能定义</th>
                  <th class="p-4 text-sm">操作与设置方法</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 dark:divide-slate-800">
                <tr>
                  <td class="p-4 font-mono font-bold text-brand-600 text-sm sm:text-base">[ 023 ]</td>
                  <td class="p-4 font-semibold">分子泵马达</td>
                  <td class="p-4 text-xs sm:text-sm">设为 <code>off</code> 仅机械干泵运转（粗抽）；设为 <code>on</code> 启动分子泵高速运转（精抽）。</td>
                </tr>
                <tr>
                  <td class="p-4 font-mono font-bold text-brand-600 text-sm sm:text-base">[ 340 ]</td>
                  <td class="p-4 font-semibold">真空度读数</td>
                  <td class="p-4 text-xs sm:text-sm">实时显示规管测量真空度（单位：hPa / mbar）。</td>
                </tr>
                <tr>
                  <td class="p-4 font-mono font-bold text-amber-600 text-sm sm:text-base">《 | 》</td>
                  <td class="p-4 font-semibold">进入设置</td>
                  <td class="p-4 text-xs sm:text-sm"><strong>同时按住左右两个方向键</strong>，解锁并进入系统参数配置。</td>
                </tr>
                <tr>
                  <td class="p-4 font-mono font-bold text-amber-600 text-sm sm:text-base">《 / 》</td>
                  <td class="p-4 font-semibold">菜单切换</td>
                  <td class="p-4 text-xs sm:text-sm">按上下箭头按键在不同参数代码之间轮换切换。</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- 右侧 50%：实验室三大铁律 -->
          <div class="bg-slate-50 dark:bg-slate-800/80 p-6 rounded-2xl border border-slate-200 dark:border-slate-700 text-sm sm:text-base space-y-3 flex flex-col justify-center">
            <div class="font-bold text-red-600 dark:text-red-400 flex items-center gap-2 text-base sm:text-lg">
              <span>⚠️</span> 分子泵实验室使用三大铁律：
            </div>
            <ul class="list-disc list-inside space-y-2 text-slate-600 dark:text-slate-300 leading-relaxed pl-1">
              <li><strong>禁止大气直启</strong>：前级真空度必须优于 <strong>&lt; 10 mbar</strong> 后，方可启动分子泵马达（023 on），严禁大气直连带压运转。</li>
              <li><strong>防冲击与震动</strong>：分子泵转子处于 ~90,000 rpm 极高转速，运转时严禁强烈搬动、撞击或倾斜推车机架。</li>
              <li><strong>破真空顺序</strong>：停机时必须先关分子泵，等待转速降至安全转速以下，方可缓慢从放气口充入干燥氮气破真空。</li>
            </ul>
          </div>

        </div>
      </section>


      <!-- ============================================== -->
      <!-- 第五部分：关键参数汇总与实验室安全红线 -->
      <!-- ============================================== -->
      <section id="sec-summary-safety" class="content-section bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-10 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-8">
        <div class="flex items-center gap-3.5 border-b border-slate-100 dark:border-slate-800 pb-5">
          <span class="p-3 rounded-xl bg-sky-500 text-white font-bold text-xl shadow-sm">5</span>
          <div>
            <h2 class="h2-title font-bold text-slate-900 dark:text-white tracking-tight">
              关键工艺参数汇总与实验室安全红线
            </h2>
            <p class="text-sm text-slate-500 dark:text-slate-400">极限温度、超导磁场范围、重要压力阈值及必须遵守的 4 大实验室安全准则</p>
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-center space-y-1.5 shadow-sm">
            <div class="text-sm font-semibold text-slate-500 dark:text-slate-400">Reservoir 升温/回设温度</div>
            <div class="text-xl sm:text-2xl font-bold text-brand-600 font-mono">300 K &rarr; 3.7 K</div>
            <div class="text-xs text-red-500 font-semibold">达 300K 必须调回 3.7K</div>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-center space-y-1.5 shadow-sm">
            <div class="text-sm font-semibold text-slate-500 dark:text-slate-400">超导磁场工作范围</div>
            <div class="text-xl sm:text-2xl font-bold text-purple-600 font-mono">±9 T (Tesla)</div>
            <div class="text-xs text-purple-600 font-medium">带超导开关 (PSH) 闭环持场</div>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-center space-y-1.5 shadow-sm">
            <div class="text-sm font-semibold text-slate-500 dark:text-slate-400">多级洗气置换轮次</div>
            <div class="text-xl sm:text-2xl font-bold text-emerald-600 font-mono">3次 N₂ + 1次 He</div>
            <div class="text-xs text-slate-400 font-medium">充 1000mbar &rarr; 抽 10mbar</div>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-center space-y-1.5 shadow-sm">
            <div class="text-sm font-semibold text-slate-500 dark:text-slate-400">Dump 终极充氦压力</div>
            <div class="text-xl sm:text-2xl font-bold text-teal-600 font-mono">950 mbar</div>
            <div class="text-xs text-teal-600 font-semibold">高纯 ⁴He 定量回充</div>
          </div>
        </div>

        <!-- 4大安全红线卡片 (2x2 宽幅对称网格) -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4">
          <div class="signal-panel signal-stop p-6 rounded-2xl border-2 border-red-200 dark:border-red-900/60 bg-red-50/60 dark:bg-red-950/20 space-y-2" data-signal="⛔ 禁止操作">
            <div class="font-bold text-base sm:text-lg text-red-900 dark:text-red-300 flex items-center gap-2">
              <span>⛔</span> 1. 严格禁止带压开启高真空分子泵
            </div>
            <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed">
              管路压力高于 10 mbar 时严禁开启分子泵马达（023），必须先由机械干泵建立前级粗真空，否则高密度气流冲击将导致分子泵涡轮叶片严重损毁。
            </p>
          </div>

          <div class="signal-panel signal-caution p-6 rounded-2xl border-2 border-amber-200 dark:border-amber-900/60 bg-amber-50/60 dark:bg-amber-950/20 space-y-2" data-signal="! 二次确认">
            <div class="font-bold text-base sm:text-lg text-amber-900 dark:text-amber-300 flex items-center gap-2">
              <span>⚠️</span> 2. 磁体电源断电双重开关规范
            </div>
            <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed">
              关闭磁体电源时，必须先按前面板软开关，再扳断后部物理硬件总电源开关；上电时先开后总开关，再按前软开关。严禁直接拔插主供电电源线。
            </p>
          </div>

          <div class="signal-panel signal-stop p-6 rounded-2xl border-2 border-blue-200 dark:border-blue-900/60 bg-blue-50/60 dark:bg-blue-950/20 space-y-2" data-signal="⛔ 压力红线">
            <div class="font-bold text-base sm:text-lg text-blue-900 dark:text-blue-300 flex items-center gap-2">
              <span>🔒</span> 3. 充气超压防护与管道排空气密性
            </div>
            <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed">
              洗气与回充工作氦气时，充气压力绝对不可超过 1000 mbar（严禁超压！）。充气结束后必须将外接软管内残存气体抽至 10 mbar 以下再行拆卸。
            </p>
          </div>

          <div class="signal-panel signal-emergency p-6 rounded-2xl border-2 border-purple-200 dark:border-purple-900/60 bg-purple-50/60 dark:bg-purple-950/20 space-y-2" data-signal="SOS · 失超应急">
            <div class="font-bold text-base sm:text-lg text-purple-900 dark:text-purple-300 flex items-center gap-2">
              <span>🧲</span> 4. ±9 T 强磁场运行与失超（Quench）防护
            </div>
            <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed">
              励磁/退磁时严格遵循设定的电流升降速率限制；严禁在通电状态下强行拔掉磁体大电流引线；5 Gauss 安全警戒线范围内严禁放置任何铁磁性工具。
            </p>
          </div>
        </div>

      </section>


      <!-- ============================================== -->
      <!-- 第六部分：常见故障检测、排错与专题规程（其他问题检测与修复） -->
      <!-- ============================================== -->
      <section id="sec-troubleshooting" class="content-section bg-gradient-to-b from-amber-500/10 via-white to-white dark:from-amber-950/30 dark:via-slate-900 dark:to-slate-900 rounded-2xl p-6 sm:p-8 lg:p-10 border-2 border-amber-300 dark:border-amber-700/70 shadow-sm space-y-8 relative overflow-hidden">
        
        <!-- 标签 -->
        <div class="absolute -right-12 top-6 bg-amber-500 text-white font-bold text-xs py-1 px-12 rotate-45 shadow-sm uppercase tracking-wider">
          故障排查与修复
        </div>

        <div class="flex items-center gap-3.5 border-b border-amber-200 dark:border-amber-800/80 pb-5">
          <span class="p-3 rounded-xl bg-amber-500 text-white font-bold text-xl shadow-md shadow-amber-500/20">🛠️</span>
          <div>
            <h2 class="h2-title font-bold text-slate-900 dark:text-white tracking-tight">
              6. 常见故障检测、排错与专题规程（其他问题检测与修复）
            </h2>
            <p class="text-sm text-amber-800 dark:text-amber-300 font-medium">
              汇总超导磁体电源网络连接排错、±9T 超导磁体安全操作、气路冰堵判断、真空不良与水冷报警等专题诊断与修复方案
            </p>
          </div>
        </div>

        <!-- 专题一：磁体电源连接 SU / GHS 网络通信与排错规程 (50:50 方案对比) -->
        <div id="sec-magnet-su" class="space-y-6 pt-2">
          <div class="flex items-center gap-2.5">
            <span class="px-3 py-1 rounded-lg bg-amber-500 text-white text-xs font-bold font-mono">专题 6.1</span>
            <h3 class="h3-title font-bold text-slate-900 dark:text-white">磁体电源连接 SU / GHS 网络通信与排错规程</h3>
          </div>

          <!-- 原理与机制解析 -->
          <div class="bg-amber-50/90 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800 rounded-2xl p-6 text-amber-950 dark:text-amber-200 space-y-3">
            <div class="font-bold flex items-center gap-2 text-base sm:text-lg">
              <span>🔍</span> 故障现象与核心排错原则
            </div>
            <p class="text-sm sm:text-base leading-relaxed">
              <strong>故障现象</strong>：磁体电源与上位机/SU 发生通讯中断、控制软件显示<strong>红色通讯错误（Error）</strong>、网络握手超时或 IP 丢失。<br>
              <strong>排错原则</strong>：先完成不会改变设备状态的网络与日志检查；只有在确认磁体处于原厂认可的安全状态、参数已备份且获得设备负责人或 attocube 支持授权后，才允许进行电源循环或底层配置。<strong>通信故障本身不构成恢复出厂默认的理由。</strong>
            </p>
          </div>

          <!-- 50:50 方案对比卡片 -->
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
            
            <!-- 方案 A：标准推荐时序流程 (50%) -->
            <div class="signal-panel signal-check rounded-2xl border-2 border-emerald-300 dark:border-emerald-700/70 bg-emerald-50/50 dark:bg-emerald-950/20 p-6 space-y-4 shadow-sm flex flex-col justify-between" data-signal="✓ A级 · 只读核验">
              <div>
                <div class="flex items-center justify-between border-b border-emerald-200 dark:border-emerald-800 pb-3 mb-3">
                  <div class="font-bold text-emerald-900 dark:text-emerald-300 flex items-center gap-2 text-base sm:text-lg">
                    <span>✅</span> A级：只读诊断与无损恢复
                  </div>
                  <span class="tag-badge bg-emerald-200 dark:bg-emerald-900 text-emerald-800 dark:text-emerald-200 text-xs">
                    普通用户上限
                  </span>
                </div>

                <ol class="space-y-3 text-sm sm:text-base text-slate-700 dark:text-slate-200 list-decimal list-outside ml-4 leading-relaxed">
                  <li>
                    <strong>记录现场状态</strong>：保存错误代码、时间、磁场设定值/读数、PS Heater 状态、温度、软件版本和网络界面截图。
                  </li>
                  <li>
                    <strong>检查物理链路</strong>：核对 RJ45 指示灯、网线、交换机端口和机柜电源指示；不得拔除磁体大电流引线。
                  </li>
                  <li>
                    <strong>检查网络配置</strong>：只读取本机 IP、子网和连接模式，与批准的设备参数卡逐项比对，不修改未知字段。
                  </li>
                  <li>
                    <strong>检查控制服务</strong>：确认 SU/GHS 或 eNSPIRE 页面是否可访问，并导出可用日志。
                  </li>
                  <li>
                    <strong>停止条件</strong>：若磁体状态不可确认、出现失超/过温/过压/电流不一致报警，立即停止排错并联系负责人。
                  </li>
                  <li>
                    <strong>提交支持信息</strong>：携带设备序列号、参数卡、截图和日志联系实验室负责人或 attocube 支持。
                  </li>
                </ol>
              </div>
            </div>

            <!-- 方案 B：快速重置备选流程 (50%) -->
            <div class="signal-panel signal-authorized rounded-2xl border border-blue-200 dark:border-blue-800/70 bg-blue-50/40 dark:bg-blue-950/20 p-6 space-y-4 shadow-sm flex flex-col justify-between" data-signal="🔒 C级 · 书面授权">
              <div>
                <div class="flex items-center justify-between border-b border-blue-200 dark:border-blue-800 pb-3 mb-3">
                  <div class="font-bold text-blue-900 dark:text-blue-300 flex items-center gap-2 text-base sm:text-lg">
                    <span>🔒</span> C级：受控电源循环与参数恢复
                  </div>
                  <span class="tag-badge bg-blue-200 dark:bg-blue-900 text-blue-800 dark:text-blue-200 text-xs">
                    厂商/工程师
                  </span>
                </div>

                <ol class="space-y-3 text-sm sm:text-base text-slate-700 dark:text-slate-200 list-decimal list-outside ml-4 leading-relaxed">
                  <li>
                    <strong>取得书面授权</strong>：由设备负责人或 attocube 支持确认具体控制器、磁体和电源型号适用的恢复步骤。
                  </li>
                  <li>
                    <strong>锁定磁体安全状态</strong>：确认实际电流/磁场、Persistent Mode、PS Heater、储能及引线电流均满足原厂断电条件，并由第二人复核。
                  </li>
                  <li>
                    <strong>备份后再操作</strong>：保存磁体常数、限流、限压、斜率、失超保护和网络配置；禁止以通用默认值覆盖本机参数。
                  </li>
                  <li>
                    <strong>按原厂时序恢复</strong>：仅执行序列号对应服务文件给出的断电、上电和握手流程；完成后核对全部保护参数并进行零场验收。
                  </li>
                </ol>
              </div>

              <div class="mt-4 p-4 rounded-xl bg-white/90 dark:bg-slate-900/90 border border-blue-200 dark:border-blue-800 text-xs sm:text-sm text-slate-600 dark:text-slate-300 space-y-1.5">
                <div class="font-bold text-red-700 dark:text-red-300 text-sm">⛔ 明确禁止：</div>
                <div>• 未确认磁体安全状态时，不得关闭磁体电源或恢复默认。</div>
                <div>• 不得凭网页中的通用数值重建磁体参数；缺少备份时必须联系厂商。</div>
              </div>
            </div>

          </div>
        </div>

        <!-- 专题四：±9 T 超导磁体充退磁与闭环持场标准操作规程 (Master SOP) -->
        <div id="sec-magnet-sop" class="space-y-5 pt-4 border-t border-amber-200 dark:border-amber-800/60">
          <div class="flex items-center gap-2.5">
            <span class="px-3 py-1 rounded-lg bg-purple-600 text-white text-xs font-bold font-mono">专题 6.4</span>
            <h3 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white">±9 T 超导磁体充退磁、持场（Persistent Mode）与失超防护规程</h3>
          </div>

          <div class="signal-panel signal-stop rounded-xl bg-red-50 dark:bg-red-950/40 border border-red-300 dark:border-red-800 p-4 text-sm text-red-800 dark:text-red-200" data-signal="⛔ 参数未核验则停止">
            <strong>参数来源边界：</strong>以下仅描述控制逻辑，不给出可替代原厂文件的时间或斜率。最大场强、允许斜率、PS Heater 加热/冷却时间、磁体常数和安全温度必须从本机批准参数卡读取；未填写参数卡时禁止励磁。
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 text-sm sm:text-base">
            
            <!-- 阶段 1：励磁升场 -->
            <div class="signal-panel signal-routine p-5 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 space-y-2.5 shadow-sm" data-signal="▶ 标准操作">
              <div class="font-bold text-purple-700 dark:text-purple-300 flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-purple-100 dark:bg-purple-900/80 text-purple-700 dark:text-purple-200 text-xs flex items-center justify-center font-bold">1</span>
                励磁升场 (Ramp Up)
              </div>
              <ul class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 space-y-1.5 leading-relaxed list-disc list-inside">
                <li>确认控制器显示 <strong>Magnet Ready</strong> 或本机原厂文件规定的等效安全状态，且所有联锁正常。</li>
                <li>按本机参数卡开启超导开关加热器（<strong>PS Heater: ON</strong>），等待规定时间并确认引线电流与磁体电流一致。</li>
                <li>输入不超过本机额定值的目标场强与批准斜率，双人核对后启动 <code>Ramp</code>。</li>
              </ul>
            </div>

            <!-- 阶段 2：闭环持场 -->
            <div class="signal-panel signal-check p-5 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 space-y-2.5 shadow-sm" data-signal="✓ 状态核验">
              <div class="font-bold text-emerald-700 dark:text-emerald-300 flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-emerald-100 dark:bg-emerald-900/80 text-emerald-700 dark:text-emerald-200 text-xs flex items-center justify-center font-bold">2</span>
                超导持场 (Persistent Mode)
              </div>
              <ul class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 space-y-1.5 leading-relaxed list-disc list-inside">
                <li>到达目标场强并稳定后，按本机参数卡关闭加热器（<strong>PS Heater: OFF</strong>）并等待规定冷却时间。</li>
                <li>仅在控制器确认超导开关闭合后，按原厂流程将引线电流回零并确认 Persistent Mode 状态。</li>
                <li>记录目标场、实际场、电流、时间和状态；Persistent Mode 可降低外部电源扰动，但不应表述为“彻底隔绝噪声”。</li>
              </ul>
            </div>

            <!-- 阶段 3：退磁与应急 -->
            <div class="signal-panel signal-emergency p-5 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 space-y-2.5 shadow-sm" data-signal="SOS · 应急处置">
              <div class="font-bold text-red-700 dark:text-red-300 flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-red-100 dark:bg-red-900/80 text-red-700 dark:text-red-200 text-xs flex items-center justify-center font-bold">3</span>
                退磁与失超处理 (Ramp to Zero)
              </div>
              <ul class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 space-y-1.5 leading-relaxed list-disc list-inside">
                <li>退磁前按本机原厂流程匹配引线电流与持场电流；任何不一致报警均应立即停止。</li>
                <li>确认 PS Heater 已按规定重新接管后，再以批准斜率执行 <code>Ramp to Zero</code>。</li>
                <li><strong>失超应急</strong>：停止实验、人员撤离危险区域、保持通风并执行实验室氧亏/磁体应急预案；未经检查批准禁止再次励磁。</li>
              </ul>
            </div>

          </div>
        </div>

        <!-- 专题二：低温气路冰堵与无法降温排错 -->
        <div class="space-y-4 pt-4 border-t border-amber-200 dark:border-amber-800/60">
          <div class="flex items-center gap-2.5">
            <span class="px-3 py-1 rounded-lg bg-sky-600 text-white text-xs font-bold font-mono">专题 6.2</span>
            <h3 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white">系统未达到本机基准温度范围 / 循环异常排查</h3>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm sm:text-base">
            <div class="p-5 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 space-y-2 shadow-sm">
              <div class="font-bold text-slate-900 dark:text-slate-100 text-base">1. 观察压力指标反弹</div>
              <p class="text-slate-600 dark:text-slate-300 leading-relaxed text-sm">降温停滞在 10K~50K 时，观察 Cryo-in 与 Cryo-out 压差是否异常飙升或骤降，此为典型节流阀冰堵表征。</p>
            </div>
            <div class="p-5 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 space-y-2 shadow-sm">
              <div class="font-bold text-slate-900 dark:text-slate-100 text-base">2. 检查冷阱饱和状态</div>
              <p class="text-slate-600 dark:text-slate-300 leading-relaxed text-sm">长期闲置可能伴随吸附性能下降，但不能仅凭停机时长判定饱和。应先对照历史降温曲线、压力、泵速和报警记录，由授权人员决定是否执行再生。</p>
            </div>
            <div class="p-5 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 space-y-2 shadow-sm">
              <div class="font-bold text-slate-900 dark:text-slate-100 text-base">3. 样品腔交换气确认</div>
              <p class="text-slate-600 dark:text-slate-300 leading-relaxed text-sm">检查样品腔是否已注入适量 Exchange Gas。无交换气会导致样品无法与低温冷头建立有效热传导。</p>
            </div>
          </div>
        </div>

        <!-- 专题三：真空度与水冷机报警 (50:50 宽幅布局) -->
        <div class="space-y-4 pt-4 border-t border-amber-200 dark:border-amber-800/60">
          <div class="flex items-center gap-2.5">
            <span class="px-3 py-1 rounded-lg bg-sky-600 text-white text-xs font-bold font-mono">专题 6.3</span>
            <h3 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white">杜瓦真空不良与水冷机联锁故障排查</h3>
          </div>
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 text-sm sm:text-base">
            <div class="p-5 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 space-y-2 shadow-sm">
              <div class="font-bold text-slate-900 dark:text-slate-100 text-base">杜瓦真空绝热不良（外壁结霜/出汗）</div>
              <p class="text-slate-600 dark:text-slate-300 leading-relaxed text-sm">降温过程中若低温腔体外壳结霜或凝露，说明外杜瓦真空度恶化。需在常温下使用分子泵对真空杜瓦端口独立抽取至 &lt; 10⁻⁴ mbar。</p>
            </div>
            <div class="p-5 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 space-y-2 shadow-sm">
              <div class="font-bold text-slate-900 dark:text-slate-100 text-base">中和水冷机高温 / 水流报警</div>
              <p class="text-slate-600 dark:text-slate-300 leading-relaxed text-sm">按本机水冷机、压缩机铭牌和批准参数卡核对供水温度、流量、压力与水质。不得把 25℃ 作为所有配置通用阈值；出现联锁时记录报警代码后检查液位、滤网和循环状态。</p>
            </div>
          </div>
        </div>

      </section>

      <section id="sec-maintenance" class="content-section bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 lg:p-10 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-8">
        <div class="flex items-center gap-3.5 border-b border-slate-100 dark:border-slate-800 pb-5">
          <span class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xl shadow-sm">7</span>
          <div>
            <h2 class="h2-title font-bold text-slate-900 dark:text-white">日常操作主线与分级维护计划</h2>
            <p class="text-sm text-slate-500 dark:text-slate-400">将普通用户的日常流程与授权维护、厂商服务明确分开</p>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-4 gap-4">
          <div class="signal-panel signal-check rounded-2xl border border-sky-200 dark:border-sky-900 bg-sky-50/70 dark:bg-sky-950/30 p-5" data-signal="✓ 开机前核验"><div class="font-extrabold text-sky-800 dark:text-sky-200">1 · 开机前</div><ul class="mt-2 text-sm space-y-1.5 list-disc list-inside"><li>确认操作者授权与实验预约</li><li>检查水冷、泄漏、供电和报警</li><li>确认磁体区域已清场</li><li>记录初始温度、压力和磁场</li></ul></div>
          <div class="signal-panel signal-routine rounded-2xl border border-indigo-200 dark:border-indigo-900 bg-indigo-50/70 dark:bg-indigo-950/30 p-5" data-signal="▶ 标准操作"><div class="font-extrabold text-indigo-800 dark:text-indigo-200">2 · 自动降温</div><ul class="mt-2 text-sm space-y-1.5 list-disc list-inside"><li>按插杆专用SOP完成样品装载</li><li>确认真空/交换气对象与端口</li><li>调用已批准的自动降温预设</li><li>保存起始时间和趋势日志</li></ul></div>
          <div class="signal-panel signal-caution rounded-2xl border border-purple-200 dark:border-purple-900 bg-purple-50/70 dark:bg-purple-950/30 p-5" data-signal="! 持续监控"><div class="font-extrabold text-purple-800 dark:text-purple-200">3 · 测量期间</div><ul class="mt-2 text-sm space-y-1.5 list-disc list-inside"><li>温度和磁场均不超过参数卡</li><li>使用批准的温变/场变斜率</li><li>持续监控联锁与压力趋势</li><li>异常时先保存日志再处置</li></ul></div>
          <div class="signal-panel signal-check rounded-2xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800/70 p-5" data-signal="✓ 结束验收"><div class="font-extrabold text-slate-800 dark:text-slate-200">4 · 结束与交接</div><ul class="mt-2 text-sm space-y-1.5 list-disc list-inside"><li>按项目批准状态退磁或安全持场</li><li>执行自动升温/待机预设</li><li>防止取样时结露污染</li><li>导出日志并完成正式交接</li></ul></div>
        </div>

        <div class="overflow-x-auto rounded-2xl border border-slate-200 dark:border-slate-700">
          <table class="w-full text-left text-sm">
            <caption class="text-left p-4 font-bold bg-slate-100 dark:bg-slate-800">维护频次、责任层级与记录要求</caption>
            <thead class="bg-slate-50 dark:bg-slate-800/60"><tr><th class="p-3">频次</th><th class="p-3">检查内容</th><th class="p-3">责任层级</th><th class="p-3">记录</th></tr></thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800">
              <tr><td class="p-3 font-bold">每次使用</td><td class="p-3">报警、温度/压力/磁场初终值、水冷状态、异常事件</td><td class="p-3">A级</td><td class="p-3">正式实验日志 + 控制器日志</td></tr>
              <tr><td class="p-3 font-bold">每周</td><td class="p-3">外观、软管、接头、泄漏痕迹、过滤器压差/状态、机柜通风</td><td class="p-3">A级检查 / B级处置</td><td class="p-3">点检表</td></tr>
              <tr><td class="p-3 font-bold">每月</td><td class="p-3">降温基线趋势、真空性能、泵站累计时间、水冷水质与滤网</td><td class="p-3">B级</td><td class="p-3">趋势报告</td></tr>
              <tr><td class="p-3 font-bold">年度</td><td class="p-3">联锁与应急预案、磁场安全边界、传感器/规管校验状态、参数备份</td><td class="p-3">负责人/厂商</td><td class="p-3">年度维护报告</td></tr>
              <tr><td class="p-3 font-bold">20,000 h</td><td class="p-3">分子筛吸附器更换评估；以本机原厂维护要求为准</td><td class="p-3">C级</td><td class="p-3">工单、部件批次与验收</td></tr>
            </tbody>
          </table>
        </div>

        <div class="rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 p-5 text-sm space-y-2">
          <div class="font-bold text-slate-900 dark:text-white">公开资料核验入口</div>
          <div class="flex flex-wrap gap-2">
            <a class="source-chip hover:text-brand-600" href="https://www.attocube.com/en/products/cryostats/closed-cycle-cryostats/attodry2100" target="_blank" rel="noopener noreferrer">attocube 产品与性能范围</a>
            <a class="source-chip hover:text-brand-600" href="https://www.attocube.com/en/products/cryostats/accessories-cryostats" target="_blank" rel="noopener noreferrer">真空附件与 20,000 h 吸附器</a>
            <a class="source-chip hover:text-brand-600" href="https://www.attocube.com/en/products/cryostats/enspire" target="_blank" rel="noopener noreferrer">eNSPIRE 日志与控制</a>
            <a class="source-chip hover:text-brand-600" href="https://www.attocube.com/en/ressources/services-and-support/support-request" target="_blank" rel="noopener noreferrer">序列号支持请求</a>
          </div>
          <p class="text-slate-500 dark:text-slate-400">公开网页不能替代随设备交付的序列号专用操作/服务手册。需要修改底层参数或维护闭式循环气路时，必须调取原厂文件。</p>
        </div>
      </section>

      <!-- 实验交接与备忘便签 (LocalStorage 自动保存) -->
      <section class="bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-4 no-print">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2.5 font-bold text-base sm:text-lg text-slate-900 dark:text-white">
            <span>📝</span> 临时交接便签（非正式操作日志）
          </div>
          <div class="flex items-center gap-3"><button type="button" onclick="exportNotes()" class="text-xs text-brand-600 hover:underline">导出便签</button><button type="button" onclick="clearNotes()" class="text-xs text-slate-400 hover:text-red-500 transition underline">清空</button></div>
        </div>
        <p class="text-xs text-amber-700 dark:text-amber-300">仅保存在当前浏览器，可能因清理数据、更换电脑或无痕模式而丢失；请导出并归档到实验室正式记录系统。</p>
        <textarea id="labNotes" rows="4" aria-label="临时实验交接便签" placeholder="建议包含：日期、操作者、样品、初终温度/磁场/压力、报警代码和交接事项..." 
                  class="w-full text-xs sm:text-sm p-3.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:bg-white dark:focus:bg-slate-900 transition leading-relaxed"></textarea>
      </section>

    </main>
  </div>

  <!-- 实验室常用换算与速查工具箱 Modal -->
  <div id="toolboxModal" role="dialog" aria-modal="true" aria-labelledby="toolboxTitle" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm hidden items-center justify-center p-4 transition-all duration-200" onclick="toggleToolbox()">
    <div class="bg-white dark:bg-slate-900 max-w-2xl w-full rounded-2xl border border-slate-200 dark:border-slate-700 shadow-2xl p-6 sm:p-8 space-y-6" onclick="event.stopPropagation()" tabindex="-1">
      <div class="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-3">
        <div id="toolboxTitle" class="flex items-center gap-2.5 font-bold text-lg text-slate-900 dark:text-white">
          <span>🧮</span> 实验室换算与速查工具箱
        </div>
        <button type="button" onclick="toggleToolbox()" aria-label="关闭换算工具箱" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 text-xl font-bold">&times;</button>
      </div>

      <!-- 压力与真空单位换算器 -->
      <div class="space-y-3 bg-slate-50 dark:bg-slate-800/60 p-4.5 rounded-xl border border-slate-200 dark:border-slate-700">
        <div class="font-bold text-xs sm:text-sm text-slate-800 dark:text-slate-200 flex items-center gap-2">
          <span>🌪️</span> 气压 / 真空度多单位即时换算
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
          <div>
            <label class="text-[11px] text-slate-500 block mb-1">毫巴 (mbar/hPa)</label>
            <input type="number" id="unit_mbar" oninput="convertPressure('mbar')" class="w-full p-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-800 font-mono font-bold text-brand-600" placeholder="950" />
          </div>
          <div>
            <label class="text-[11px] text-slate-500 block mb-1">帕斯卡 (Pa)</label>
            <input type="number" id="unit_pa" oninput="convertPressure('pa')" class="w-full p-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-800 font-mono" placeholder="95000" />
          </div>
          <div>
            <label class="text-[11px] text-slate-500 block mb-1">托 (Torr / mmHg)</label>
            <input type="number" id="unit_torr" oninput="convertPressure('torr')" class="w-full p-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-800 font-mono" placeholder="712.5" />
          </div>
          <div>
            <label class="text-[11px] text-slate-500 block mb-1">磅力/平方英寸 (psi)</label>
            <input type="number" id="unit_psi" oninput="convertPressure('psi')" class="w-full p-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-800 font-mono" placeholder="13.78" />
          </div>
        </div>
      </div>

      <!-- 磁场升场时间预估计算器 -->
      <div class="space-y-3 bg-purple-50/50 dark:bg-purple-950/20 p-4.5 rounded-xl border border-purple-200/80 dark:border-purple-900/60">
        <div class="font-bold text-xs sm:text-sm text-purple-900 dark:text-purple-200 flex items-center gap-2">
          <span>🧲</span> ±9 T 磁场扫场耗时预估计算器
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
          <div>
            <label class="text-[11px] text-slate-500 block mb-1">起始场强 B₁ (T)</label>
            <input type="number" id="mag_b1" value="0" step="0.1" class="w-full p-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-800 font-mono" />
          </div>
          <div>
            <label class="text-[11px] text-slate-500 block mb-1">目标场强 B₂ (T)</label>
            <input type="number" id="mag_b2" value="0" step="0.1" class="w-full p-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-800 font-mono" />
          </div>
          <div>
            <label class="text-[11px] text-slate-500 block mb-1">扫场速率 (T/min)</label>
            <input type="number" id="mag_rate" value="" step="0.01" min="0.01" placeholder="按本机参数卡" class="w-full p-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-800 font-mono" />
          </div>
        </div>
        <div class="flex items-center justify-between pt-1">
          <button type="button" onclick="calcMagTime()" class="px-4 py-2 rounded-lg bg-purple-600 text-white font-semibold text-xs hover:bg-purple-700 transition">计算预计耗时</button>
          <span id="magTimeResult" class="font-mono font-bold text-purple-700 dark:text-purple-300 text-xs" aria-live="polite">请输入本机批准斜率</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 图片全屏高清灯箱 (Lightbox Modal) -->
  <div id="imgModal" role="dialog" aria-modal="true" aria-labelledby="modalCaption" class="fixed inset-0 z-50 bg-black/95 backdrop-blur-md hidden items-center justify-center p-4 transition-all duration-200" onclick="closeLightbox()">
    <div class="relative max-w-6xl w-full flex flex-col items-center" onclick="event.stopPropagation()" tabindex="-1">
      <button type="button" onclick="closeLightbox()" class="absolute -top-12 right-0 text-white hover:text-slate-300 font-bold text-2xl p-1">&times; 关闭 (ESC)</button>
      <img id="modalImg" src="" alt="放大图片" class="max-h-[85vh] w-auto max-w-full rounded-xl shadow-2xl object-contain bg-slate-900" />
      <p id="modalCaption" class="text-center text-sm text-slate-200 mt-3 font-semibold px-5 py-2 rounded-full bg-slate-800/90 border border-slate-700"></p>
    </div>
  </div>

  <!-- 页面底部 -->
  <footer class="mt-16 bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 py-8 text-center text-xs sm:text-sm text-slate-400 no-print">
    <div class="max-w-[1560px] mx-auto px-4 space-y-1.5">
      <p class="font-semibold text-slate-600 dark:text-slate-300">attocube attoDRY 2100 / WITec Confocal Raman & Photoluminescence System Operation Manual</p>
      <p>极限基准温度: 1.65 K · 超导磁场: ±9 T · 整理归档于实验室文档库 · 支持在主流浏览器中阅读、搜索、字号自适应缩放或另存为 PDF 文件</p>
    </div>
  </footer>

  <!-- 交互脚本与 ScrollSpy 导航高亮 -->
  <script>
    window.addEventListener('scroll', () => {
      const winScroll = document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('scrollProgressBar').style.width = scrolled + '%';

      // ScrollSpy 高亮当前章节与步骤
      const sections = document.querySelectorAll('section[id], article[id]');
      let currentId = '';
      sections.forEach(sec => {
        const top = sec.offsetTop - 120;
        if (winScroll >= top) {
          currentId = sec.getAttribute('id');
        }
      });
      
      document.querySelectorAll('.toc-link, .toc-sublink').forEach(link => {
        link.classList.remove('toc-active');
        if (link.getAttribute('href') === '#' + currentId) {
          link.classList.add('toc-active');
        }
      });
    });

    function setFontScale(scale) {
      document.body.classList.remove('font-scale-sm', 'font-scale-md', 'font-scale-lg', 'font-scale-xl');
      document.body.classList.add('font-scale-' + scale);
      
      ['sm', 'md', 'lg', 'xl'].forEach(s => {
        const btn = document.getElementById('btn-font-' + s);
        if (s === scale) {
          btn.className = 'px-2.5 py-1 text-xs font-semibold rounded bg-white dark:bg-slate-700 text-brand-600 dark:text-brand-400 shadow-sm transition';
        } else {
          btn.className = 'px-2.5 py-1 text-xs font-semibold rounded hover:bg-white dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition';
        }
      });
      localStorage.setItem('attocube_font_scale', scale);
    }

    const savedFont = localStorage.getItem('attocube_font_scale') || 'md';
    setFontScale(savedFont);

    function toggleDarkMode() {
      const isDark = document.documentElement.classList.toggle('dark');
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
      document.getElementById('themeIcon').innerText = isDark ? '☀️' : '🌓';
    }

    if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.classList.add('dark');
      document.getElementById('themeIcon').innerText = '☀️';
    }

    function openLightbox(src, caption) {
      window.lastFocusedElement = document.activeElement;
      document.getElementById('modalImg').src = src;
      document.getElementById('modalCaption').innerText = caption || '';
      const modal = document.getElementById('imgModal');
      modal.classList.remove('hidden');
      modal.classList.add('flex');
      modal.querySelector('button').focus();
    }

    function closeLightbox() {
      const modal = document.getElementById('imgModal');
      modal.classList.remove('flex');
      modal.classList.add('hidden');
      if (window.lastFocusedElement) window.lastFocusedElement.focus();
    }

    function toggleToolbox() {
      const modal = document.getElementById('toolboxModal');
      if (modal.classList.contains('hidden')) {
        window.lastFocusedElement = document.activeElement;
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        modal.querySelector('button').focus();
      } else {
        modal.classList.remove('flex');
        modal.classList.add('hidden');
        if (window.lastFocusedElement) window.lastFocusedElement.focus();
      }
    }

    function formatEngineering(value) {
      if (!Number.isFinite(value)) return '';
      const absolute = Math.abs(value);
      if (absolute !== 0 && (absolute < 0.001 || absolute >= 1000000)) return value.toExponential(4);
      return Number(value.toPrecision(6)).toString();
    }

    function convertPressure(source) {
      let mbar = NaN;
      if (source === 'mbar') {
        mbar = parseFloat(document.getElementById('unit_mbar').value);
      } else if (source === 'pa') {
        mbar = parseFloat(document.getElementById('unit_pa').value) / 100;
      } else if (source === 'torr') {
        mbar = parseFloat(document.getElementById('unit_torr').value) / 0.750061683;
      } else if (source === 'psi') {
        mbar = parseFloat(document.getElementById('unit_psi').value) / 0.0145037738;
      }

      if (!Number.isFinite(mbar) || mbar < 0) {
        ['mbar', 'pa', 'torr', 'psi'].filter(unit => unit !== source).forEach(unit => document.getElementById('unit_' + unit).value = '');
        return;
      }
      if (source !== 'mbar') document.getElementById('unit_mbar').value = formatEngineering(mbar);
      if (source !== 'pa') document.getElementById('unit_pa').value = formatEngineering(mbar * 100);
      if (source !== 'torr') document.getElementById('unit_torr').value = formatEngineering(mbar * 0.750061683);
      if (source !== 'psi') document.getElementById('unit_psi').value = formatEngineering(mbar * 0.0145037738);
    }

    function calcMagTime() {
      const b1 = parseFloat(document.getElementById('mag_b1').value);
      const b2 = parseFloat(document.getElementById('mag_b2').value);
      const rate = parseFloat(document.getElementById('mag_rate').value);
      const result = document.getElementById('magTimeResult');
      if (![b1, b2, rate].every(Number.isFinite) || rate <= 0) {
        result.innerText = '请输入有效场强和本机批准斜率';
        return;
      }
      const delta = Math.abs(b2 - b1);
      const minutes = (delta / rate);
      result.innerText = `理论时间: ~${minutes.toFixed(1)} 分钟（ΔB = ${delta.toFixed(2)} T；不含稳定与PCS等待）`;
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeLightbox();
        const tb = document.getElementById('toolboxModal');
        if (!tb.classList.contains('hidden')) toggleToolbox();
      }
    });

    function recordStartTime(stepNum, stepName, hours) {
      const now = new Date();
      const timeStr = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
      const targetTime = new Date(now.getTime() + hours * 3600 * 1000);
      const targetStr = targetTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', month: 'numeric', day: 'numeric' });
      alert(`⏱️ 已记录【步骤 ${stepNum}：${stepName}】开始时间：${timeStr}\\n预计需耗时 ${hours} 小时，预计完成时间约为：${targetStr}。\\n\\n请在实验过程中密切关注压力读数！`);
    }

    function updateProgress() {
      const checkboxes = document.querySelectorAll('.step-checkbox');
      let done = 0;
      let remainingHours = 0;
      const state = {};
      
      checkboxes.forEach(cb => {
        const step = cb.getAttribute('data-step');
        const hours = parseFloat(cb.getAttribute('data-hours') || 0);
        state[step] = cb.checked;
        if (cb.checked) {
          done++;
        } else {
          remainingHours += hours;
        }
      });
      
      localStorage.setItem('attocube_steps_state', JSON.stringify(state));
      document.getElementById('progressPercent').innerText = `${done}/8 完成`;
      document.getElementById('stepProgressFill').style.width = `${(done / 8) * 100}%`;
      
      if (remainingHours > 0) {
        document.getElementById('remainingTimeText').innerText = `预计剩余: ~${remainingHours.toFixed(1)} 小时`;
      } else {
        document.getElementById('remainingTimeText').innerText = `🎉 所有再生步骤已全部完成！`;
      }
    }

    function loadProgress() {
      const saved = localStorage.getItem('attocube_steps_state');
      if (saved) {
        try {
          const state = JSON.parse(saved);
          document.querySelectorAll('.step-checkbox').forEach(cb => {
            const step = cb.getAttribute('data-step');
            if (state[step]) cb.checked = true;
          });
        } catch (e) {}
      }
      updateProgress();
    }

    function resetChecklist() {
      if (confirm('确认重置所有步骤的标记状态吗？')) {
        document.querySelectorAll('.step-checkbox').forEach(cb => cb.checked = false);
        updateProgress();
      }
    }

    // 实验交接便签 LocalStorage 存储
    const notesArea = document.getElementById('labNotes');
    if (notesArea) {
      notesArea.value = localStorage.getItem('attocube_lab_notes') || '';
      notesArea.addEventListener('input', (e) => {
        localStorage.setItem('attocube_lab_notes', e.target.value);
      });
    }
    function clearNotes() {
      if (confirm('确认清空交接便签内容吗？')) {
        notesArea.value = '';
        localStorage.removeItem('attocube_lab_notes');
      }
    }

    function exportNotes() {
      const text = notesArea ? notesArea.value.trim() : '';
      if (!text) {
        alert('便签为空，没有可导出的内容。');
        return;
      }
      const stamp = new Date().toISOString().replace(/[:.]/g, '-');
      const blob = new Blob([`attoDRY 2100 临时交接便签\n导出时间：${new Date().toLocaleString()}\n\n${text}\n`], { type: 'text/plain;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `attoDRY2100-临时便签-${stamp}.txt`;
      link.click();
      URL.revokeObjectURL(url);
    }

    document.getElementById('quickSearch').addEventListener('input', function(e) {
      const q = e.target.value.trim().toLowerCase();
      const sections = document.querySelectorAll('.step-card, .content-section');
      if (!q) {
        sections.forEach(s => s.style.display = '');
        return;
      }
      sections.forEach(s => {
        const text = s.innerText.toLowerCase();
        if (text.includes(q)) {
          s.style.display = '';
        } else {
          s.style.display = 'none';
        }
      });
    });

    document.querySelectorAll('.img-zoom').forEach(img => {
      img.setAttribute('tabindex', '0');
      img.setAttribute('role', 'button');
      img.setAttribute('aria-label', `${img.alt || '设备图片'}，按回车放大`);
      img.addEventListener('keydown', event => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          img.click();
        }
      });
    });

    loadProgress();
  </script>
</body>
</html>
"""

# Write only to the project directory so regeneration cannot silently overwrite
# an unrelated external artifact location.
# The manual is a local/offline artifact. Eager-loading prevents zero-height
# placeholders when users jump directly to a high-resolution procedure image.
html_template = html_template.replace('loading="lazy"', 'loading="eager"')
html_template = html_template.replace(' max-h-[520px]', '')
EQUIPMENT_DIR = Path(__file__).resolve().parents[1]
output_path = EQUIPMENT_DIR / '低温设备使用手册.html'
output_path.write_text(html_template, encoding='utf-8', newline='\n')
print(f'Controlled review HTML manual saved to {output_path}')
