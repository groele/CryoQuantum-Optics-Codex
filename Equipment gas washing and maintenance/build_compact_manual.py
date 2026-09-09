# -*- coding: utf-8 -*-
from pathlib import Path

html_content = """<!DOCTYPE html>
<html lang="zh-CN" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>attoDRY 2100 低温与超导磁体实用操作手册 (精炼版 SOP)</title>
  <style>
    :root {
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #475569;
      --border: #e2e8f0;
      --brand: #0284c7;
      --brand-light: #e0f2fe;
      --brand-dark: #0369a1;
      --manual-bg: #fef3c7;
      --manual-text: #92400e;
      --manual-border: #fcd34d;
      --software-bg: #e0f2fe;
      --software-text: #0369a1;
      --software-border: #7dd3fc;
      --danger-bg: #fef2f2;
      --danger-text: #991b1b;
      --danger-border: #fecaca;
      --success-bg: #f0fdf4;
      --success-text: #166534;
      --success-border: #bbf7d0;
    }
    .dark {
      --bg: #0b1120;
      --card-bg: #151e32;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --border: #223049;
      --brand: #38bdf8;
      --brand-light: rgba(14, 165, 233, 0.15);
      --brand-dark: #0284c7;
      --manual-bg: rgba(120, 53, 15, 0.45);
      --manual-text: #fde68a;
      --manual-border: rgba(217, 119, 6, 0.6);
      --software-bg: rgba(8, 47, 73, 0.5);
      --software-text: #bae6fd;
      --software-border: rgba(2, 132, 199, 0.5);
      --danger-bg: rgba(127, 29, 29, 0.4);
      --danger-text: #fca5a5;
      --danger-border: rgba(239, 68, 68, 0.5);
      --success-bg: rgba(20, 83, 45, 0.4);
      --success-text: #86efac;
      --success-border: rgba(34, 197, 94, 0.5);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei UI", sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.7;
      font-size: 15px;
      padding-bottom: 3.5rem;
    }
    .container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 1.25rem;
    }
    
    /* Sticky Top Bar */
    header {
      position: sticky;
      top: 0;
      z-index: 50;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 0.75rem 1.25rem;
      margin-bottom: 1.5rem;
    }
    .dark header {
      background: rgba(21, 30, 50, 0.95);
    }
    .header-content {
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.85rem;
    }
    .header-title h1 {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .header-title p {
      font-size: 0.82rem;
      color: var(--text-muted);
    }
    .header-nav {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      flex-wrap: wrap;
    }
    .nav-link {
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-muted);
      text-decoration: none;
      padding: 0.35rem 0.65rem;
      border-radius: 0.45rem;
      transition: all 0.15s ease;
    }
    .nav-link:hover {
      color: var(--brand);
      background: var(--brand-light);
    }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.4rem 0.8rem;
      border-radius: 0.5rem;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text);
      text-decoration: none;
      transition: all 0.15s ease;
    }
    .btn:hover {
      border-color: var(--brand);
      color: var(--brand);
    }

    /* Key Specs Grid */
    .specs-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 0.85rem;
      margin-bottom: 1.5rem;
    }
    .spec-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 0.75rem;
      padding: 0.85rem 1.15rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    .spec-label {
      font-size: 0.78rem;
      color: var(--text-muted);
      font-weight: 600;
    }
    .spec-val {
      font-size: 1.35rem;
      font-weight: 800;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      color: var(--brand);
      margin-top: 0.1rem;
    }

    /* Progress Banner */
    .progress-box {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 0.75rem;
      padding: 0.85rem 1.25rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.25rem;
      flex-wrap: wrap;
    }
    .progress-bar-wrap {
      flex: 1;
      min-width: 240px;
      background: var(--border);
      height: 9px;
      border-radius: 999px;
      overflow: hidden;
    }
    .progress-bar-fill {
      background: linear-gradient(90deg, #10b981, #06b6d4);
      height: 100%;
      width: 0%;
      transition: width 0.3s ease;
    }

    /* Section Shell */
    .section-block {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 1rem;
      padding: 1.5rem;
      margin-bottom: 2rem;
      box-shadow: 0 1px 4px rgba(0,0,0,0.02);
    }
    .section-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border);
      padding-bottom: 0.85rem;
      margin-bottom: 1.25rem;
      flex-wrap: wrap;
      gap: 0.5rem;
    }
    .section-title {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    /* Step Cards */
    .step-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 0.95rem;
      padding: 1.35rem;
      margin-bottom: 1.5rem;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    .step-card:hover {
      border-color: var(--brand);
      box-shadow: 0 6px 20px rgba(0,0,0,0.05);
    }
    .step-top {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 0.75rem;
      margin-bottom: 1.15rem;
      padding-bottom: 0.85rem;
      border-bottom: 1px dashed var(--border);
    }
    .step-meta {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }
    .step-num-badge {
      width: 32px;
      height: 32px;
      background: var(--brand-light);
      color: var(--brand-dark);
      border-radius: 0.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.92rem;
      font-weight: 800;
      font-family: ui-monospace, SFMono-Regular, monospace;
    }
    .step-heading {
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--text);
    }
    .step-tags {
      display: flex;
      gap: 0.4rem;
      flex-wrap: wrap;
    }
    .tag {
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
      padding: 0.18rem 0.55rem;
      border-radius: 0.35rem;
      font-size: 0.76rem;
      font-weight: 700;
    }
    .tag-manual {
      background: var(--manual-bg);
      color: var(--manual-text);
      border: 1px solid var(--manual-border);
    }
    .tag-software {
      background: var(--software-bg);
      color: var(--software-text);
      border: 1px solid var(--software-border);
    }
    .tag-danger {
      background: var(--danger-bg);
      color: var(--danger-text);
      border: 1px solid var(--danger-border);
    }
    .tag-success {
      background: var(--success-bg);
      color: var(--success-text);
      border: 1px solid var(--success-border);
    }
    .tag-pill {
      font-family: ui-monospace, SFMono-Regular, monospace;
      padding: 0.15rem 0.5rem;
      border-radius: 0.3rem;
      font-weight: 700;
      font-size: 0.8rem;
    }

    /* 50:50 Step Layout that preserves natural aspect ratio */
    .step-layout {
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 1.5rem;
      align-items: stretch;
    }
    @media (max-width: 980px) {
      .step-layout {
        grid-template-columns: 1fr;
      }
    }
    .step-content {
      font-size: 0.92rem;
      line-height: 1.75;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .step-content ol, .step-content ul {
      list-style: none;
      margin-bottom: 0.75rem;
    }
    .step-content li {
      margin-bottom: 0.65rem;
      position: relative;
      padding-left: 1.4rem;
    }
    .step-content li::before {
      content: "▪";
      position: absolute;
      left: 0.3rem;
      color: var(--brand);
      font-weight: bold;
    }
    .step-content strong {
      color: var(--text);
    }
    
    /* Dedicated Image Container: NO STRETCH, NO SQUASH, PRESERVES NATURAL RATIO */
    .step-card-img-wrap {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      background: rgba(0, 0, 0, 0.02);
      border: 1px solid var(--border);
      border-radius: 0.85rem;
      padding: 0.85rem;
      height: 100%;
    }
    .dark .step-card-img-wrap {
      background: rgba(255, 255, 255, 0.02);
    }
    .step-card-img-wrap img {
      width: auto;
      max-width: 100%;
      height: auto;
      max-height: 520px;
      object-fit: contain;
      border-radius: 0.55rem;
      box-shadow: 0 3px 12px rgba(0, 0, 0, 0.06);
      cursor: zoom-in;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      display: block;
      margin: 0 auto;
    }
    .step-card-img-wrap img:hover {
      transform: scale(1.015);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }
    .img-caption {
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-top: 0.5rem;
      text-align: center;
      font-weight: 500;
    }
    
    .callout-box {
      border-radius: 0.55rem;
      padding: 0.7rem 0.95rem;
      margin-top: 0.85rem;
      font-size: 0.85rem;
      line-height: 1.65;
    }
    .callout-warn {
      background: var(--manual-bg);
      border: 1px solid var(--manual-border);
      color: var(--manual-text);
    }
    .callout-danger {
      background: var(--danger-bg);
      border: 1px solid var(--danger-border);
      color: var(--danger-text);
    }
    .callout-success {
      background: var(--success-bg);
      border: 1px solid var(--success-border);
      color: var(--success-text);
    }

    /* P&ID Section Layout */
    .pid-layout {
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 1.5rem;
      align-items: center;
    }
    @media (max-width: 980px) {
      .pid-layout {
        grid-template-columns: 1fr;
      }
    }
    .pid-img-box {
      border: 1px solid var(--border);
      border-radius: 0.85rem;
      padding: 0.85rem;
      background: rgba(0,0,0,0.015);
      text-align: center;
    }
    .pid-img-box img {
      width: auto;
      max-width: 100%;
      height: auto;
      max-height: 540px;
      object-fit: contain;
      border-radius: 0.55rem;
      cursor: zoom-in;
      display: block;
      margin: 0 auto;
    }

    /* Valve Matrix Table */
    .table-scroll {
      overflow-x: auto;
      border: 1px solid var(--border);
      border-radius: 0.75rem;
      margin-bottom: 1rem;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.84rem;
      text-align: center;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    }
    thead th {
      background: rgba(148, 163, 184, 0.08);
      padding: 0.75rem 0.5rem;
      border-bottom: 1px solid var(--border);
      font-weight: 750;
      color: var(--text);
    }
    thead th.group-manual {
      background: rgba(245, 158, 11, 0.12);
      color: #b45309;
      border-bottom: 2px solid #f59e0b;
    }
    thead th.group-software {
      background: rgba(14, 165, 233, 0.12);
      color: #0284c7;
      border-bottom: 2px solid #0284c7;
    }
    thead th.group-pump {
      background: rgba(139, 92, 246, 0.12);
      color: #7c3aed;
      border-bottom: 2px solid #8b5cf6;
    }
    tbody td {
      padding: 0.7rem 0.5rem;
      border-bottom: 1px solid var(--border);
      color: var(--text);
    }
    tbody tr:hover {
      background: rgba(0, 0, 0, 0.015);
    }
    .dark tbody tr:hover {
      background: rgba(255, 255, 255, 0.02);
    }
    .st-open {
      color: #16a34a;
      font-weight: 800;
      background: var(--success-bg);
      padding: 0.18rem 0.45rem;
      border-radius: 4px;
    }
    .st-closed {
      color: #dc2626;
      font-weight: 800;
      background: var(--danger-bg);
      padding: 0.18rem 0.45rem;
      border-radius: 4px;
    }
    .st-auto {
      color: #0284c7;
      font-weight: 800;
      background: var(--software-bg);
      padding: 0.18rem 0.45rem;
      border-radius: 4px;
    }

    /* DCU and Troubleshooting Grids */
    .two-col-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(330px, 1fr));
      gap: 1.25rem;
    }
    .info-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 0.75rem;
      padding: 1.15rem;
      font-size: 0.88rem;
      line-height: 1.7;
    }
    .info-card h4 {
      font-size: 0.98rem;
      font-weight: 800;
      margin-bottom: 0.6rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    /* Lightbox Modal */
    #imgModal {
      display: none;
      position: fixed;
      inset: 0;
      z-index: 100;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(6px);
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      flex-direction: column;
      cursor: zoom-out;
    }
    #imgModal img {
      max-width: 92vw;
      max-height: 86vh;
      width: auto;
      height: auto;
      object-fit: contain;
      border-radius: 0.5rem;
      box-shadow: 0 12px 40px rgba(0,0,0,0.6);
      cursor: default;
    }
    #modalCaption {
      color: #f8fafc;
      margin-top: 0.85rem;
      font-size: 0.92rem;
      text-align: center;
      font-weight: 600;
    }

    /* Print Optimization */
    @media print {
      body { background: white !important; color: black !important; font-size: 10pt !important; padding: 0 !important; }
      header, .btn, .no-print { display: none !important; }
      .container { max-width: 100% !important; padding: 0 !important; }
      .step-card { break-inside: avoid !important; border: 1px solid #aaa !important; margin-bottom: 1.25rem !important; }
      .step-layout { grid-template-columns: 1fr 260px !important; gap: 1rem !important; }
      .step-card-img-wrap img { max-height: 240px !important; }
      .section-block { break-inside: avoid !important; border: 1px solid #aaa !important; margin-bottom: 1rem !important; padding: 1rem !important; }
      table { font-size: 8pt !important; }
      tbody td, thead th { padding: 0.35rem 0.2rem !important; }
      .print-header { display: block !important; border-bottom: 2px solid #000; padding-bottom: 0.5rem; margin-bottom: 1rem; }
    }
    .print-header { display: none; }

    /* =================================================== */
    /* 总体工艺主线与步骤链条 (Workflow Pipeline & Stepper) */
    /* =================================================== */
    .pipeline-container {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 1rem;
      padding: 1.35rem 1.5rem;
      margin-bottom: 2rem;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
    }
    .pipeline-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin-bottom: 1.15rem;
      padding-bottom: 0.85rem;
      border-bottom: 1px dashed var(--border);
    }
    .pipeline-title {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--text);
    }
    .pipeline-phases {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 0.85rem;
      margin-bottom: 1.25rem;
    }
    @media (max-width: 980px) {
      .pipeline-phases {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    @media (max-width: 560px) {
      .pipeline-phases {
        grid-template-columns: 1fr;
      }
    }
    .phase-badge-card {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 0.75rem;
      padding: 0.8rem 0.95rem;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      transition: all 0.2s ease;
      border-top: 3.5px solid var(--brand);
    }
    .phase-badge-card:nth-child(1) { border-top-color: #0284c7; }
    .phase-badge-card:nth-child(2) { border-top-color: #8b5cf6; }
    .phase-badge-card:nth-child(3) { border-top-color: #f59e0b; }
    .phase-badge-card:nth-child(4) { border-top-color: #10b981; }

    .phase-badge-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(0,0,0,0.05);
    }
    .phase-badge-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .phase-roman {
      font-weight: 850;
      font-family: ui-monospace, SFMono-Regular, monospace;
      font-size: 0.78rem;
      color: var(--brand);
      background: var(--brand-light);
      padding: 0.12rem 0.45rem;
      border-radius: 0.35rem;
    }
    .phase-duration {
      font-size: 0.74rem;
      color: var(--text-muted);
      font-weight: 700;
      font-family: monospace;
    }
    .phase-name {
      font-weight: 800;
      font-size: 0.92rem;
      color: var(--text);
    }
    .phase-desc {
      font-size: 0.76rem;
      color: var(--text-muted);
      line-height: 1.45;
    }

    /* 8 步贯穿式节点链条 */
    .stepper-chain-wrap {
      position: relative;
    }
    .stepper-chain {
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      gap: 0.55rem;
      position: relative;
    }
    @media (max-width: 1200px) {
      .stepper-chain {
        grid-template-columns: repeat(4, 1fr);
        gap: 0.75rem;
      }
    }
    @media (max-width: 680px) {
      .stepper-chain {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    .stepper-node {
      background: var(--bg);
      border: 1.5px solid var(--border);
      border-radius: 0.75rem;
      padding: 0.75rem 0.65rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      text-decoration: none;
      color: inherit;
      position: relative;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      cursor: pointer;
      user-select: none;
    }
    .stepper-node:hover {
      border-color: var(--brand);
      background: var(--card-bg);
      box-shadow: 0 4px 16px rgba(2, 132, 199, 0.15);
      transform: translateY(-3px);
    }
    .stepper-node.completed {
      border-color: #16a34a !important;
      background: rgba(22, 163, 74, 0.05);
    }
    .stepper-node.completed .stepper-num {
      background: #16a34a !important;
      color: white !important;
      box-shadow: 0 0 0 2px rgba(22, 163, 74, 0.2);
    }
    .stepper-node.completed .stepper-title {
      color: #15803d;
    }
    .stepper-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.45rem;
    }
    .stepper-num {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: var(--brand-light);
      color: var(--brand-dark);
      font-weight: 850;
      font-size: 0.76rem;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: monospace;
      transition: all 0.2s ease;
    }
    .stepper-time {
      font-size: 0.72rem;
      color: var(--text-muted);
      font-weight: 700;
      font-family: monospace;
      background: rgba(0,0,0,0.03);
      padding: 0.1rem 0.35rem;
      border-radius: 0.25rem;
    }
    .dark .stepper-time {
      background: rgba(255,255,255,0.05);
    }
    .stepper-title {
      font-weight: 800;
      font-size: 0.84rem;
      color: var(--text);
      line-height: 1.3;
      margin-bottom: 0.35rem;
    }
    .stepper-action {
      font-size: 0.72rem;
      color: var(--text-muted);
      line-height: 1.35;
      margin-bottom: 0.5rem;
      flex-grow: 1;
    }
    .stepper-tag-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.25rem;
      margin-top: auto;
    }
    .stepper-node-tag {
      font-size: 0.68rem;
      padding: 0.12rem 0.4rem;
      border-radius: 0.25rem;
      font-weight: 700;
      white-space: nowrap;
    }
    .stepper-arrow {
      font-size: 0.75rem;
      color: var(--text-muted);
      opacity: 0.6;
    }
  </style>
</head>
<body>

  <!-- 顶部悬浮导航栏 -->
  <header>
    <div class="header-content">
      <div class="header-title">
        <h1>
          <span>⚡</span>
          <span>attoDRY 2100 实用操作手册 (精炼版 SOP)</span>
        </h1>
        <p>中南大学实验室 · 超低温 1.65 K / 强磁场 ±9 T 现场实操规范</p>
      </div>
      <nav class="header-nav no-print">
        <a href="#sec-pipeline" class="nav-link">总体步骤链条</a>
        <a href="#sec-pid" class="nav-link">管路原理 (P&ID)</a>
        <a href="#sec-steps" class="nav-link">8 步实操规程</a>
        <a href="#sec-matrix" class="nav-link">阀门状态矩阵</a>
        <a href="#sec-dcu" class="nav-link">分子泵 DCU 指令</a>
        <a href="#sec-faults" class="nav-link">排障与红线</a>
        <button type="button" onclick="window.print()" class="btn" title="打印本手册">
          <span>🖨️ 打印 SOP</span>
        </button>
        <button type="button" onclick="toggleTheme()" class="btn" title="切换深浅模式">
          <span id="themeIcon">🌓 主题</span>
        </button>
      </nav>
    </div>
  </header>

  <div class="container">

    <!-- 打印专有标题 -->
    <div class="print-header">
      <h2 style="font-size: 15pt; font-weight: bold;">attoDRY 2100 低温与超导磁体实用操作手册 (精炼版 SOP)</h2>
      <p style="font-size: 8.5pt; color: #444;">中南大学 WITec 显微拉曼联用平台 · 极限基温 1.65 K · 超导磁场 ±9 T · 现场实操规范指南</p>
    </div>

    <!-- 4 大核心指标看版 -->
    <div class="specs-strip">
      <div class="spec-card">
        <div>
          <div class="spec-label">❄️ 极限基准温度</div>
          <div class="spec-val">1.65 K</div>
        </div>
        <span class="tag tag-success">⁴He 闭环蒸发</span>
      </div>
      <div class="spec-card">
        <div>
          <div class="spec-label">🧲 垂直超导磁场</div>
          <div class="spec-val">±9 T</div>
        </div>
        <span class="tag tag-software">标准斜率 0.5 T/min</span>
      </div>
      <div class="spec-card">
        <div>
          <div class="spec-label">🎯 工作氦气回充量</div>
          <div class="spec-val">950 mbar</div>
        </div>
        <span class="tag tag-manual">≥ 99.999% 高纯⁴He</span>
      </div>
      <div class="spec-card">
        <div>
          <div class="spec-label">🌊 循环水冷机工况</div>
          <div class="spec-val">&lt; 25 ℃</div>
        </div>
        <span class="tag tag-danger">压差 2.5~3.5 bar</span>
      </div>
    </div>

    <!-- 实验打卡进度条 -->
    <div class="progress-box no-print">
      <div style="display: flex; align-items: center; gap: 0.75rem;">
        <span style="font-weight: 750; font-size: 0.92rem;">📋 现场打卡进度：</span>
        <span id="progressPercent" style="font-weight: 800; color: var(--brand); font-family: monospace;">0/8 步完成</span>
      </div>
      <div class="progress-bar-wrap">
        <div id="stepProgressFill" class="progress-bar-fill"></div>
      </div>
      <div style="display: flex; align-items: center; gap: 0.75rem;">
        <span id="remainingTimeText" style="font-size: 0.82rem; color: var(--text-muted); font-weight: 600;">预计总耗时：~56 小时</span>
        <button type="button" onclick="resetChecklist()" class="btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">重置打卡</button>
      </div>
    </div>

    <!-- ============================================== -->
    <!-- 总体工艺主线：八步深度再生与降温全景步骤链条 -->
    <!-- ============================================== -->
    <section id="sec-pipeline" class="pipeline-container">
      <div class="pipeline-header">
        <div class="pipeline-title">
          <span>⛓️</span>
          <span>总体工艺主线：八步深度再生与降温全景链条</span>
        </div>
        <div style="font-size: 0.8rem; color: var(--text-muted); display: flex; align-items: center; gap: 0.75rem;">
          <span>⏱️ 标准全周期工时：<strong>~56 小时</strong></span>
          <span style="color: var(--border);">|</span>
          <span>💡 点击任意步骤卡片即可直达实操规程</span>
        </div>
      </div>

      <!-- 四大工艺阶段卡片 -->
      <div class="pipeline-phases">
        <div class="phase-badge-card">
          <div class="phase-badge-top">
            <span class="phase-roman">阶段 Ⅰ</span>
            <span class="phase-duration">⏱️ ~3 h</span>
          </div>
          <div class="phase-name">升温解吸与回路隔离</div>
          <div class="phase-desc">步骤 01~02 · Reservoir 设温 300 K 充分解吸杂质，切断外围硬件电源，转移分子泵至压缩机顶部服务口 V3 初抽保压。</div>
        </div>

        <div class="phase-badge-card">
          <div class="phase-badge-top">
            <span class="phase-roman">阶段 Ⅱ</span>
            <span class="phase-duration">⏱️ ~16 h</span>
          </div>
          <div class="phase-name">吸附器脱毒烘烤再生</div>
          <div class="phase-desc">步骤 03~04 · HK-06 温控仪加热 8h 彻底活化吸附剂，停热 5min 关气，分子泵转接过滤器侧向阀 V8 深度脱气 8h（&lt;10⁻⁵ mbar）。</div>
        </div>

        <div class="phase-badge-card">
          <div class="phase-badge-top">
            <span class="phase-roman">阶段 Ⅲ</span>
            <span class="phase-duration">⏱️ ~22 h</span>
          </div>
          <div class="phase-name">主管路净化与充氦</div>
          <div class="phase-desc">步骤 05~07 · 全回路深度抽真空 ≥12h，进行 3 轮高纯 N₂ + 1 轮高纯 He 梯度循环洗气，最后定量回充 950 mbar 工作氦并抽杜瓦。</div>
        </div>

        <div class="phase-badge-card">
          <div class="phase-badge-top">
            <span class="phase-roman">阶段 Ⅳ</span>
            <span class="phase-duration">⏱️ ~22 h</span>
          </div>
          <div class="phase-name">复位开启与自动降温</div>
          <div class="phase-desc">步骤 08 · <strong>必须手动完全打开步骤 7 关闭的全部手阀</strong>，开启水冷机与压缩机，软件点击 Cool Down 自动化降温至 1.65 K 极限。</div>
        </div>
      </div>

      <!-- 8 步贯穿式可视化连线流程链条 -->
      <div class="stepper-chain-wrap">
        <div class="stepper-chain">

          <!-- 节点 01 -->
          <div class="stepper-node" id="stepper-node-1" onclick="scrollToStep(1)">
            <div class="stepper-top-bar">
              <span class="stepper-num" id="stepper-num-1">01</span>
              <span class="stepper-time">~2-3h</span>
            </div>
            <div class="stepper-title">升温与断电</div>
            <div class="stepper-action">Reservoir 设温 300K 回设 3.7K；关闭水冷压缩机</div>
            <div class="stepper-tag-row">
              <span class="stepper-node-tag tag-software">💻 设温</span>
              <span class="stepper-arrow">→</span>
            </div>
          </div>

          <!-- 节点 02 -->
          <div class="stepper-node" id="stepper-node-2" onclick="scrollToStep(2)">
            <div class="stepper-top-bar">
              <span class="stepper-num" id="stepper-num-2">02</span>
              <span class="stepper-time">~0.5h</span>
            </div>
            <div class="stepper-title">转泵与初抽</div>
            <div class="stepper-action">分子泵接压缩机 V3；粗抽 &lt;10mbar 保压 30min</div>
            <div class="stepper-tag-row">
              <span class="stepper-node-tag tag-manual">✋ 现场转接</span>
              <span class="stepper-arrow">→</span>
            </div>
          </div>

          <!-- 节点 03 -->
          <div class="stepper-node" id="stepper-node-3" onclick="scrollToStep(3)">
            <div class="stepper-top-bar">
              <span class="stepper-num" id="stepper-num-3">03</span>
              <span class="stepper-time">8h</span>
            </div>
            <div class="stepper-title">烘烤排杂</div>
            <div class="stepper-action">加热套 8h 排杂；关 V7/V9 开 V8；停热 5min 关阀</div>
            <div class="stepper-tag-row">
              <span class="stepper-node-tag tag-manual" style="background:#fef3c7;color:#92400e;">🔥 关键再生</span>
              <span class="stepper-arrow">→</span>
            </div>
          </div>

          <!-- 节点 04 -->
          <div class="stepper-node" id="stepper-node-4" onclick="scrollToStep(4)">
            <div class="stepper-top-bar">
              <span class="stepper-num" id="stepper-num-4">04</span>
              <span class="stepper-time">7~8h</span>
            </div>
            <div class="stepper-title">侧向脱气</div>
            <div class="stepper-action">分子泵接侧向阀 V8；对吸附剂抽高真空 &lt;10⁻⁵ mbar</div>
            <div class="stepper-tag-row">
              <span class="stepper-node-tag tag-manual">🌪️ 侧向抽空</span>
              <span class="stepper-arrow">→</span>
            </div>
          </div>

          <!-- 节点 05 -->
          <div class="stepper-node" id="stepper-node-5" onclick="scrollToStep(5)">
            <div class="stepper-top-bar">
              <span class="stepper-num" id="stepper-num-5">05</span>
              <span class="stepper-time">≥12h</span>
            </div>
            <div class="stepper-title">系统深抽</div>
            <div class="stepper-action">泵接 V3，全开系统手阀与电磁阀；回路深抽 ≥12h</div>
            <div class="stepper-tag-row">
              <span class="stepper-node-tag tag-software">🌐 全回路深抽</span>
              <span class="stepper-arrow">→</span>
            </div>
          </div>

          <!-- 节点 06 -->
          <div class="stepper-node" id="stepper-node-6" onclick="scrollToStep(6)">
            <div class="stepper-top-bar">
              <span class="stepper-num" id="stepper-num-6">06</span>
              <span class="stepper-time">6~8h</span>
            </div>
            <div class="stepper-title">梯度洗气</div>
            <div class="stepper-action">3次高纯 N₂ + 1次高纯 He；950~1000 ⇄ 10 mbar</div>
            <div class="stepper-tag-row">
              <span class="stepper-node-tag tag-pill" style="background:#e0e7ff;color:#3730a3;">🔄 3N₂+1He</span>
              <span class="stepper-arrow">→</span>
            </div>
          </div>

          <!-- 节点 07 -->
          <div class="stepper-node" id="stepper-node-7" onclick="scrollToStep(7)">
            <div class="stepper-top-bar">
              <span class="stepper-num" id="stepper-num-7">07</span>
              <span class="stepper-time">~2h</span>
            </div>
            <div class="stepper-title">充氦抽杜瓦</div>
            <div class="stepper-action">DUMP 充氦至 950mbar；关阀隔离；转泵抽杜瓦真空</div>
            <div class="stepper-tag-row">
              <span class="stepper-node-tag tag-success">🎯 950mbar</span>
              <span class="stepper-arrow">→</span>
            </div>
          </div>

          <!-- 节点 08 -->
          <div class="stepper-node" id="stepper-node-8" onclick="scrollToStep(8)">
            <div class="stepper-top-bar">
              <span class="stepper-num" id="stepper-num-8">08</span>
              <span class="stepper-time">~20-24h</span>
            </div>
            <div class="stepper-title">复位自动降温</div>
            <div class="stepper-action">⚠️ 必须手动全开手阀；开压缩机水冷；软件 Cool Down 自动调控</div>
            <div class="stepper-tag-row">
              <span class="stepper-node-tag tag-danger">❄️ 1.65K 自控</span>
              <span class="stepper-arrow">🏁</span>
            </div>
          </div>

        </div>
      </div>
    </section>



    <!-- ============================================== -->
    <!-- 第一部分：P&ID 管路结构示意图与实物标号 -->
    <!-- ============================================== -->
    <section id="sec-pid" class="section-block">
      <div class="section-header">
        <div class="section-title">
          <span>📐</span>
          <span>第一部分：attoDRY 2100 标准管路结构示意图 (P&ID)</span>
        </div>
        <span style="font-size: 0.78rem; color: var(--text-muted);">图 1.1 · 标注 V1~V9、Cryo 进出、Dump 进出与压力计位置（点击图片放大）</span>
      </div>

      <div class="pid-layout">
        <div class="pid-img-box">
          <img src="images/slide_13.jpg" alt="P&ID 管路原理图" onclick="openModal(this.src, 'attoDRY 2100 标准管路原理图 (P&ID)')" />
          <div class="img-caption">📷 图 1.1：标准管路原理图（V1~V9、电磁阀及压力表位置）</div>
        </div>
        <div class="info-card" style="display: flex; flex-direction: column; justify-content: space-between; height: 100%;">
          <div>
            <h4 style="color: var(--brand);">🏷️ 核心阀门物理对象对照表</h4>
            <ul style="list-style: none; font-size: 0.85rem; line-height: 1.8;">
              <li><strong>V1 / V2 (后阀门)</strong>：主机后部手动进出气阀（贴有“中南大学 1”、“中南大学 2”实物标号）</li>
              <li><strong>V3 (Service)</strong>：压缩机顶部抽真空主维修手阀</li>
              <li><strong>V4 (Bypass)</strong>：压缩机旁通调节手阀</li>
              <li><strong>V7 / V9 (直通阀)</strong>：吸附过滤器上下两端直通隔离阀</li>
              <li><strong>V8 (侧向阀)</strong>：吸附过滤器侧向排气与独立抽空阀</li>
              <li><strong>Cryo-in / out</strong>：低温冷头气动电磁阀（软件控制）</li>
              <li><strong>Dump-in / out</strong>：储气罐进出气动电磁阀（软件控制）</li>
              <li><strong>Scroll Pump</strong>：内置机械干式隔膜循环泵（软件控制）</li>
            </ul>
          </div>
          <div class="callout-box callout-warn" style="margin-top: 0.6rem; font-size: 0.8rem;">
            💡 <strong>辨识核心法则</strong>：后阀 1/2、V3、V4、V7、V8、V9 为<strong>现场物理手阀</strong>；Cryo/Dump 进出及 Scroll 泵为<strong>软件气动电磁阀</strong>。
          </div>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- 第二部分：8 大步骤详细实操规程 -->
    <!-- ============================================== -->
    <section id="sec-steps" class="section-block">
      <div class="section-header">
        <div class="section-title">
          <span>🛠️</span>
          <span>第二部分：气路深度再生与自动化降温 8 大步骤详细规程</span>
        </div>
        <span style="font-size: 0.78rem; color: var(--text-muted);">标准工时：约 56 小时 · 严格按序号执行，严禁颠倒时序</span>
      </div>

      <!-- 步骤 1 -->
      <div class="step-card" id="step-1">
        <div class="step-top">
          <div class="step-meta">
            <span class="step-num-badge">01</span>
            <span class="step-heading">步骤 1：Reservoir 升温至 300 K 并切断外围硬件</span>
            <span class="tag tag-software">💻 软件设温</span>
            <span class="tag tag-manual">✋ 现场断电</span>
            <span class="tag tag-pill" style="background:#f1f5f9; color:#475569;">⏱️ ~2-3h</span>
          </div>
          <label class="step-check-label no-print" style="display:flex; align-items:center; gap:0.35rem; cursor:pointer;">
            <input type="checkbox" data-step="1" data-hours="3" class="step-checkbox" onchange="updateProgress()">
            <span style="font-weight:700; font-size:0.8rem;">标记完成</span>
          </label>
        </div>
        <div class="step-layout">
          <div class="step-content">
            <ol>
              <li><strong>设定升温参数</strong>：<span class="tag tag-software">💻 软件</span> 在 attoDRY 软件 <code>Main</code> &rarr; <code>Temperature Control</code> 中，将 Reservoir Target Temperature 设为 <strong style="color:var(--brand);">300 K</strong>，点击 <code>Start</code> 启动升温。</li>
              <li><strong>配置气路电磁阀</strong>：<span class="tag tag-software">💻 软件</span> 在 <code>Expert</code> 界面中设置：Scroll Pump 设为 <code>OFF</code>、<code>Cryo-out</code> 设为 <code>CLOSED</code>、<code>Cryo-in</code> 设为 <code>CLOSED</code>、<code>Dump-out</code> 设为 <code>OPEN</code>、<code>Dump-in</code> 设为 <code>OPEN</code>。</li>
              <li><strong>切断外围硬件物理总电源</strong>：<span class="tag tag-manual">✋ 现场手动</span>
                <br>• 关闭干式膜泵物理电源开关；
                <br>• 将中和循环水冷机面板开关拨至 <code>STOP / OFF</code>；
                <br>• 将 CRYOMECH 氦压缩机电源总旋钮旋至 <code>OFF</code>。
              </li>
              <li><strong>回设目标防干烧温度</strong>：<span class="tag tag-software">💻 软件</span> 当设备温度升至 300 K 后，立即将 <code>Target temperature [K]</code> 调回至 <strong style="color:var(--brand);">3.7 K</strong>（防止后续冷却降温时加热器持续干烧损坏）。</li>
            </ol>
            <div class="callout-box callout-success">
              🎯 <strong>放行标准</strong>：Reservoir 温度稳定达 300 K，外围压缩机、水冷机及干泵已安全断电，加热目标温度已重设为 3.7 K。
            </div>
          </div>
          <div class="step-card-img-wrap">
            <img src="images/slide_3.jpg" alt="步骤1示意图" onclick="openModal(this.src, '步骤 1：软件升温设置 300K、Expert 气路状态及压缩机、水冷机关闭面板')" />
            <div class="img-caption">📷 图 2.1：升温参数设定与外围硬件关闭</div>
          </div>
        </div>
      </div>

      <!-- 步骤 2 -->
      <div class="step-card" id="step-2">
        <div class="step-top">
          <div class="step-meta">
            <span class="step-num-badge">02</span>
            <span class="step-heading">步骤 2：转移分子泵机组、初抽与管路保压检漏</span>
            <span class="tag tag-manual">✋ 粗抽保压</span>
            <span class="tag tag-pill" style="background:#f1f5f9; color:#475569;">⏱️ ~1h</span>
          </div>
          <label class="step-check-label no-print" style="display:flex; align-items:center; gap:0.35rem; cursor:pointer;">
            <input type="checkbox" data-step="2" data-hours="1" class="step-checkbox" onchange="updateProgress()">
            <span style="font-weight:700; font-size:0.8rem;">标记完成</span>
          </label>
        </div>
        <div class="step-layout">
          <div class="step-content">
            <ol>
              <li><strong>连接分子泵机组</strong>：<span class="tag tag-manual">✋ 现场手动</span> 将 Pfeiffer HiCUBE 分子泵机组推移至压缩机侧，使用专用金属波纹管连接至压缩机顶部的 <strong>Service 抽气口</strong>，锁死 KF 快卸卡箍。</li>
              <li><strong>机械干泵粗抽 (&lt; 10 mbar)</strong>：<span class="tag tag-manual">✋ 现场手动</span>
                <br>• 在 Pfeiffer DCU 200 面板上将参数 <code>023</code>（分子泵马达）设为 <code>off</code>，<strong>仅开启前级干泵进行粗抽</strong>；
                <br>• 手动拧开 Bypass 手阀（V4）与主机后部手阀（中南大学 1、2 号阀）；
                <br>• <span class="tag tag-software">💻 软件</span> 软件中打开 <code>Cryo-in/out</code> 与 <code>Dump-in/out</code>，系统粗抽至 <strong>&lt; 10 mbar</strong>。
              </li>
              <li><strong>开启分子泵深度抽空</strong>：<span class="tag tag-manual">✋ 现场手动</span> 气压降至 10 mbar 以下后，在 DCU 面板将参数 <code>023</code> 设为 <code>on</code> 开启分子泵，深度抽至 <strong>&lt; 10⁻⁵ mbar</strong>。</li>
              <li><strong>隔离保压检漏</strong>：<span class="tag tag-manual">✋ 现场手动</span> 手动拧紧关闭 Service 手阀（V3），切断泵组并保持系统静置 <strong>30 分钟</strong>，观察真空压力表。</li>
            </ol>
            <div class="callout-box callout-success">
              🎯 <strong>放行标准</strong>：系统保压 30 分钟，压力上升率 &Delta;P &lt; 0.5 mbar，证明管路各法兰及密封无外部宏观漏率。
            </div>
          </div>
          <div class="step-card-img-wrap">
            <img src="images/slide_5.jpg" alt="步骤2示意图" onclick="openModal(this.src, '步骤 2：转移分子泵与初抽保压')" />
            <div class="img-caption">📷 图 2.2：分子泵连接至 Service 口初抽</div>
          </div>
        </div>
      </div>

      <!-- 步骤 3 -->
      <div class="step-card" id="step-3">
        <div class="step-top">
          <div class="step-meta">
            <span class="step-num-badge">03</span>
            <span class="step-heading">步骤 3：冷阱吸附剂加热烘烤再生 (8 小时)</span>
            <span class="tag tag-manual">✋ 现场加热</span>
            <span class="tag tag-danger">⚠️ 严格停热顺序</span>
            <span class="tag tag-pill" style="background:#f1f5f9; color:#475569;">⏱️ 8h 连续烘烤</span>
          </div>
          <label class="step-check-label no-print" style="display:flex; align-items:center; gap:0.35rem; cursor:pointer;">
            <input type="checkbox" data-step="3" data-hours="8" class="step-checkbox" onchange="updateProgress()">
            <span style="font-weight:700; font-size:0.8rem;">标记完成</span>
          </label>
        </div>
        <div class="step-layout">
          <div class="step-content">
            <ol>
              <li><strong>隔离过滤器并打开排气口</strong>：<span class="tag tag-manual">✋ 现场手动</span>
                <br>• <strong>封起两端</strong>：手动关紧过滤器上下两端直通主阀（<strong>V7、V9 关紧封起</strong>）；
                <br>• <strong>打开侧阀</strong>：<strong>手动拧开侧向阀门（V8 打开排气）</strong>，释放吸附剂受热析出的杂质气体。
              </li>
              <li><strong>安装加热套并通电</strong>：<span class="tag tag-manual">✋ 现场手动</span> 将专用电加热套紧密包裹在活性炭吸附过滤器外壁，绑紧固定带；连接 HK-06 温控器电源，启动加热。</li>
              <li><strong>恒温烘烤活化</strong>：持续加热活化 <strong>8 小时</strong>，彻底解析吸附材料内部捕集的微量水分、油污与杂质气体。</li>
            </ol>
            <div class="callout-box callout-warn">
              ⚠️ <strong>停热关气四步绝不可倒置</strong>：烘烤结束时，<strong>必须先断开 HK-06 加热器电源停止加热，静置冷却 5 分钟后，方可手动关紧侧向出气口 V8</strong>！严防热态直接封死导致腔体憋压或骤冷回吸！
            </div>
          </div>
          <div class="step-card-img-wrap">
            <img src="images/slide_7.jpg" alt="步骤3示意图" onclick="openModal(this.src, '步骤 3：吸附剂包裹加热套脱气 8h')" />
            <div class="img-caption">📷 图 2.3：包裹加热套、V7/V9关、V8开排气</div>
          </div>
        </div>
      </div>

      <!-- 步骤 4 -->
      <div class="step-card" id="step-4">
        <div class="step-top">
          <div class="step-meta">
            <span class="step-num-badge">04</span>
            <span class="step-heading">步骤 4：转接分子泵至过滤器侧向阀 (V8) 独立抽真空</span>
            <span class="tag tag-manual">✋ 侧向抽空</span>
            <span class="tag tag-pill" style="background:#f1f5f9; color:#475569;">⏱️ ~1-2h</span>
          </div>
          <label class="step-check-label no-print" style="display:flex; align-items:center; gap:0.35rem; cursor:pointer;">
            <input type="checkbox" data-step="4" data-hours="2" class="step-checkbox" onchange="updateProgress()">
            <span style="font-weight:700; font-size:0.8rem;">标记完成</span>
          </label>
        </div>
        <div class="step-layout">
          <div class="step-content">
            <ol>
              <li><strong>拆除加热套并维持主阀关闭</strong>：<span class="tag tag-manual">✋ 现场手动</span> 停热关气冷却后，拆下电加热套。<strong>上下两端直通阀（V7, V9）必须继续保持关紧隔离状态</strong>。</li>
              <li><strong>转接抽气管路</strong>：<span class="tag tag-manual">✋ 现场手动</span> 使用 KF 变径转接环与波纹管，将 Pfeiffer 分子泵机组进气口直接连接至过滤器<strong>侧向阀门端口（V8 接口）</strong>，锁紧卡箍。</li>
              <li><strong>启动侧向高真空抽空</strong>：<span class="tag tag-manual">✋ 现场手动</span> <strong>手动拧开侧向阀门（V8 开）</strong>，在 DCU 启动分子泵机组，对刚烘烤活化完毕的吸附过滤器内部进行 1~2 小时的高真空脱气抽取。</li>
            </ol>
            <div class="callout-box callout-success">
              🎯 <strong>放行标准</strong>：侧向抽空真空计读数达到 &lt; 10⁻⁵ mbar 极限，无残存挥发气体析出。
            </div>
          </div>
          <div class="step-card-img-wrap">
            <img src="images/slide_8.jpg" alt="步骤4示意图" onclick="openModal(this.src, '步骤 4：分子泵连接过滤器侧向阀抽真空')" />
            <div class="img-caption">📷 图 2.4：分子泵转接过滤器侧向阀 (V8)</div>
          </div>
        </div>
      </div>

      <!-- 步骤 5 -->
      <div class="step-card" id="step-5">
        <div class="step-top">
          <div class="step-meta">
            <span class="step-num-badge">05</span>
            <span class="step-heading">步骤 5：系统复位并进行全管路深度连续抽真空 (≥ 12 小时)</span>
            <span class="tag tag-manual">✋ 通宵抽空</span>
            <span class="tag tag-pill" style="background:#f1f5f9; color:#475569;">⏱️ ≥ 12h (建议通宵)</span>
          </div>
          <label class="step-check-label no-print" style="display:flex; align-items:center; gap:0.35rem; cursor:pointer;">
            <input type="checkbox" data-step="5" data-hours="12" class="step-checkbox" onchange="updateProgress()">
            <span style="font-weight:700; font-size:0.8rem;">标记完成</span>
          </label>
        </div>
        <div class="step-layout">
          <div class="step-content">
            <ol>
              <li><strong>复位过滤器阀门</strong>：<span class="tag tag-manual">✋ 现场手动</span> 拆除侧向抽真空管，<strong>手动关紧侧向阀门（V8 关紧）</strong>；<strong>重新手动旋开过滤器上下两端直通主阀（V7, V9 打开导通）</strong>。</li>
              <li><strong>恢复 Service 口连接</strong>：<span class="tag tag-manual">✋ 现场手动</span> 将分子泵机组移回压缩机顶部 Service 口并卡紧卡箍，<strong>手动旋开 Bypass 手阀（V4）与 Service 手阀（V3）</strong>。</li>
              <li><strong>全系统贯通深度连续抽空</strong>：<span class="tag tag-software">💻 软件</span> 开启软件中全部气动阀门与 Scroll 泵；开启分子泵机组，对整个闭环循环管路进行 <strong>12 小时以上（强烈建议通宵）</strong>的极限深冷抽真空。</li>
            </ol>
            <div class="callout-box callout-success">
              🎯 <strong>放行标准</strong>：全系统隔夜连续抽真空后，各主要监测点底压达到 &lt; 10⁻⁵ mbar 数量级，背景本底超净。
            </div>
          </div>
          <div class="step-card-img-wrap">
            <img src="images/slide_9.jpg" alt="步骤5示意图" onclick="openModal(this.src, '步骤 5：全系统管路深度抽真空 12h')" />
            <div class="img-caption">📷 图 2.5：全系统贯通深度抽真空 (建议通宵)</div>
          </div>
        </div>
      </div>

      <!-- 步骤 6 -->
      <div class="step-card" id="step-6">
        <div class="step-top">
          <div class="step-meta">
            <span class="step-num-badge">06</span>
            <span class="step-heading">步骤 6：循环洗气净化 (3 次高纯 N₂ + 1 次高纯 ⁴He)</span>
            <span class="tag tag-software">💻 循环充气</span>
            <span class="tag tag-manual">✋ 换瓶抽洗</span>
            <span class="tag tag-pill" style="background:#f1f5f9; color:#475569;">⏱️ ~1.5h</span>
          </div>
          <label class="step-check-label no-print" style="display:flex; align-items:center; gap:0.35rem; cursor:pointer;">
            <input type="checkbox" data-step="6" data-hours="1.5" class="step-checkbox" onchange="updateProgress()">
            <span style="font-weight:700; font-size:0.8rem;">标记完成</span>
          </label>
        </div>
        <div class="step-layout">
          <div class="step-content">
            <ol>
              <li><strong>隔离抽真空并连接气瓶</strong>：<span class="tag tag-manual">✋ 现场手动</span> 手动关紧 Service 手阀（V3），关闭分子泵；将高纯氮气钢瓶减压阀出口软管连接至充气口。</li>
              <li><strong>3 次高纯氮洗气置换</strong>：
                <br>• <span class="tag tag-software">💻 软件</span> 通过 <code>Dump-in</code> 阀向系统充入高纯 N₂ 至 <strong>950 ~ 1000 mbar</strong>；
                <br>• 静置保压渗透 <strong>10 分钟</strong>；
                <br>• <span class="tag tag-manual">✋ 现场</span> 开启分子泵抽空系统至 <strong>&lt; 10 mbar</strong>；
                <br>• <strong>严格重复以上充放洗气操作共 3 次</strong>。
              </li>
              <li><strong>1 次高纯氦终末洗气</strong>：
                <br>• 拆下氮气瓶，连接高纯 ⁴He 气瓶；通过 <code>Dump-in</code> 充入 950 mbar ⁴He 进行置换冲刷；
                <br>• 最后再次启动分子泵将残留气体深度抽尽至极限真空。
              </li>
            </ol>
            <div class="callout-box callout-warn">
              ⚠️ <strong>安全红线</strong>：充气压力严禁超过 1050 mbar，防止过压击穿膜片或损坏真空测量规管！
            </div>
          </div>
          <div class="step-card-img-wrap">
            <img src="images/slide_10.jpg" alt="步骤6示意图" onclick="openModal(this.src, '步骤 6：循环洗气 (3次氮气+1次氦气)')" />
            <div class="img-caption">📷 图 2.6：充放气循环置换与压力表位</div>
          </div>
        </div>
      </div>

      <!-- 步骤 7 -->
      <div class="step-card" id="step-7" style="border-left: 4px solid #0284c7;">
        <div class="step-top">
          <div class="step-meta">
            <span class="step-num-badge" style="background:#e0f2fe; color:#0369a1;">07</span>
            <span class="step-heading">步骤 7：补充工作氦气 (950 mbar) 与低温真空杜瓦抽真空</span>
            <span class="tag tag-manual" style="background:#fee2e2; color:#b91c1c;">✋ 现场关紧手阀</span>
            <span class="tag tag-software">💻 软件充氦</span>
            <span class="tag tag-pill" style="background:#f1f5f9; color:#475569;">⏱️ ~1h</span>
          </div>
          <label class="step-check-label no-print" style="display:flex; align-items:center; gap:0.35rem; cursor:pointer;">
            <input type="checkbox" data-step="7" data-hours="1" class="step-checkbox" onchange="updateProgress()">
            <span style="font-weight:700; font-size:0.8rem;">标记完成</span>
          </label>
        </div>
        <div class="step-layout">
          <div class="step-content">
            <ol>
              <li><strong>软件关闭抽真空与相关电磁阀</strong>：<span class="tag tag-software">💻 软件</span> 关闭分子泵与 Scroll 泵；在 <code>Expert</code> 界面中<strong>关闭 <code>Cryo-out</code> 与 <code>Dump-out</code></strong> 气控阀。</li>
              <li><strong>【现场关键动作】手动关紧所有手阀</strong>：<span class="tag tag-manual" style="color:#b91c1c; font-weight:bold;">✋ 现场手动</span> <strong>必须手动关紧压缩机后部手阀（中南大学 1、2 号阀）及过滤器侧阀门（V8）</strong>。</li>
              <li><strong>定量充注标准工作氦气</strong>：<span class="tag tag-software">💻 软件</span> 通过 <code>Dump-in</code> 向储气罐充入高纯 ⁴He 至标准工作压力：<strong style="color:var(--brand);">950 mbar</strong>。</li>
              <li><strong>抽除残气并拆除充气管</strong>：<span class="tag tag-manual">✋ 现场手动</span> 充气完成后关闭 Dump-in，手动将软管内残留气体抽至 &lt; 10 mbar 后拆除充气接头。</li>
              <li><strong>独立抽取低温杜瓦高真空</strong>：<span class="tag tag-manual">✋ 现场手动</span> 将 Pfeiffer 分子泵推至 attoDRY 主机，通过波纹管卡紧连接至<strong>真空杜瓦（Vacuum Dewar）抽气口</strong>，开启分子泵对低温真空绝热杜瓦独立抽高真空，保障绝热性能。</li>
            </ol>
            <div class="callout-box callout-warn">
              ⚠️ <strong>核心防呆提示</strong>：步骤 7 中关闭的“后部手阀 1、2 号”是关键物理隔离点，必须确切关紧，防止补气或抽杜瓦时窜气！
            </div>
          </div>
          <div class="step-card-img-wrap">
            <img src="images/slide_11.jpg" alt="步骤7示意图" onclick="openModal(this.src, '步骤 7：DUMP 补气 950mbar 与杜瓦抽真空')" />
            <div class="img-caption">📷 图 2.7：关闭后阀 1/2 号并抽杜瓦真空</div>
          </div>
        </div>
      </div>

      <!-- 步骤 8 -->
      <div class="step-card" id="step-8" style="border-left: 4px solid #10b981;">
        <div class="step-top">
          <div class="step-meta">
            <span class="step-num-badge" style="background:#dcfce7; color:#15803d;">08</span>
            <span class="step-heading">步骤 8：系统复位与自动化降温启动（目标极限基温 1.65 K）</span>
            <span class="tag tag-manual" style="background:#dcfce7; color:#15803d;">✋ 现场必须全开手阀</span>
            <span class="tag tag-software">💻 Cool Down 自控</span>
            <span class="tag tag-pill" style="background:#f1f5f9; color:#475569;">⏱️ ~3-4h 自动降温</span>
          </div>
          <label class="step-check-label no-print" style="display:flex; align-items:center; gap:0.35rem; cursor:pointer;">
            <input type="checkbox" data-step="8" data-hours="3.5" class="step-checkbox" onchange="updateProgress()">
            <span style="font-weight:700; font-size:0.8rem;">标记完成</span>
          </label>
        </div>
        <div class="step-layout">
          <div class="step-content">
            <ol>
              <li><strong>样品腔充入适量交换气</strong>：<span class="tag tag-manual">✋ 现场手动</span> 手动向样品腔（Sample Space）充入适量热交换气体（Exchange Gas），恢复测试腔体与样品之间的低温热传导路径。</li>
              <li><strong>【核心前置条件】全部现场手动打开步骤 7 关闭的阀门</strong>：<span class="tag tag-manual" style="color:#15803d; font-weight:bold;">✋ 现场手动</span>
                <br>• <strong>必须现场手动旋开压缩机后部手阀（中南大学 1、2 号阀）</strong>，彻底打通进气与回气回路；
                <br>• <strong>手动完全拧开过滤器侧阀门（V8）及管路运行手阀</strong>；
                <br>• <strong>停止分子泵抽杜瓦</strong>，拆除波纹管并恢复杜瓦盲板卡箍密封。
              </li>
              <li><strong>开启水冷机与压缩机总电源</strong>：<span class="tag tag-manual">✋ 现场手动</span>
                <br>• <strong>开启中和循环水冷机总电源</strong>（检查确认冷却水温 &lt; 25 ℃、水压正常稳定）；
                <br>• <strong>旋转开启 CRYOMECH 氦压缩机电源总开关</strong>，压缩机进入就绪运行状态。
              </li>
              <li><strong>点击 Cool Down 启动全自动降温</strong>：<span class="tag tag-software">💻 软件自控</span>
                <br>• 在 attoDRY 控制软件主界面直接点击 <strong><code>Cool Down</code></strong> 按钮；
                <br>• <strong>【软件全自动操作】步骤 7 在软件中关闭的气动阀门（Cryo-out, Dump-out 及 Scroll 泵），由系统自动调配开启并执行制冷循环，无需在软件上手动打开！</strong>
                <br>• 系统全自动降温并平稳直达 <strong style="color:var(--brand);">1.65 K</strong> 极限基温。
              </li>
            </ol>
            <div class="callout-box callout-danger">
              ⛔ <strong>不可逾越的安全红线</strong>：
              <br>1. <strong>现场手阀必须全开</strong>：步骤 7 关闭的物理手阀（后阀 1/2 号等）必须在降温前全部手动旋开！若手阀未开强行开启压缩机，会导致循环回路憋压甚至设备严重损毁！
              <br>2. <strong>软件阀门无需人工干预</strong>：点击 Cool Down 即可，严禁或无需在软件 Expert 界面手动强开电磁阀，避免扰乱系统自动化状态机控制！
            </div>
          </div>
          <div class="step-card-img-wrap">
            <img src="images/slide_12.jpg" alt="步骤8示意图" onclick="openModal(this.src, '步骤 8：样品腔补气、开图7阀门、开水冷压缩机及软件自动降温')" />
            <div class="img-caption">📷 图 2.8：开图7阀门、开水冷压缩机与自动降温</div>
          </div>
        </div>
      </div>

    </section>

    <!-- ============================================== -->
    <!-- 第三部分：全步骤阀门状态速查矩阵 -->
    <!-- ============================================== -->
    <section id="sec-matrix" class="section-block">
      <div class="section-header">
        <div class="section-title">
          <span>🎛️</span>
          <span>第三部分：8 大步骤管路阀门状态一览矩阵 (Valve Status Matrix)</span>
        </div>
        <span style="font-size: 0.78rem; color: var(--text-muted);">
          <span class="st-open">开</span> 物理旋开 / <span class="st-closed">关</span> 物理旋紧 / <span class="st-auto">自控</span> 软件程序自控开启
        </span>
      </div>

      <div class="table-scroll">
        <table>
          <thead>
            <tr class="border-b border-slate-200 dark:border-slate-700 text-xs">
              <th rowspan="2" style="width: 17%; text-align: left; padding-left: 0.85rem;">步骤序号与名称</th>
              <th colspan="5" class="group-manual">✋ 现场物理手动阀门组</th>
              <th colspan="3" class="group-software">💻 attoDRY 软件气控电磁阀组</th>
              <th class="group-pump">外设泵组</th>
            </tr>
            <tr>
              <th style="color:#b45309;">后阀 1/2 (V1/V2)</th>
              <th>V3 (Service)</th>
              <th>V4 (Bypass)</th>
              <th>V7/V9 (直通)</th>
              <th>V8 (侧向)</th>
              <th>Scroll 泵</th>
              <th>Cryo 进/出</th>
              <th>Dump 进/出</th>
              <th style="text-align: left; padding-left: 0.5rem;">分子泵连接口</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="text-align: left; font-weight: bold; padding-left: 0.85rem;">1. Reservoir 升温 (300K)</td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-open">开</span></td>
              <td style="text-align: left; padding-left: 0.5rem; color:#64748b;">停用断电</td>
            </tr>
            <tr>
              <td style="text-align: left; font-weight: bold; padding-left: 0.85rem;">2. 气路初抽保压 (&lt;10mbar)</td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td style="text-align: left; padding-left: 0.5rem; color:#0284c7; font-weight:bold;">接压缩机 Service 口</td>
            </tr>
            <tr>
              <td style="text-align: left; font-weight: bold; padding-left: 0.85rem;">3. 吸附剂加热再生 (8h)</td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed" style="background:#fee2e2;">关 (封起)</span></td>
              <td><span class="st-open" style="background:#fef3c7; color:#b45309;">开 (排气)</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td style="text-align: left; padding-left: 0.5rem; color:#f59e0b; font-weight:bold;">温控器套加热 (8h)</td>
            </tr>
            <tr>
              <td style="text-align: left; font-weight: bold; padding-left: 0.85rem;">4. 吸附剂侧向抽真空</td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-open" style="background:#e0f2fe; color:#0369a1;">开 (抽空)</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td style="text-align: left; padding-left: 0.5rem; color:#8b5cf6; font-weight:bold;">接过滤器侧阀 V8</td>
            </tr>
            <tr>
              <td style="text-align: left; font-weight: bold; padding-left: 0.85rem;">5. 全系统深度抽空 (≥12h)</td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td style="text-align: left; padding-left: 0.5rem; color:#0284c7; font-weight:bold;">移回 Service 口 (通宵)</td>
            </tr>
            <tr>
              <td style="text-align: left; font-weight: bold; padding-left: 0.85rem;">6. 循环洗气 (3N₂+1He)</td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td style="text-align: left; padding-left: 0.5rem; color:#10b981; font-weight:bold;">接气瓶充洗＋抽空</td>
            </tr>
            <tr style="background: rgba(2, 132, 199, 0.05);">
              <td style="text-align: left; font-weight: bold; padding-left: 0.85rem; color:#0284c7;">7. 充氦(950mbar)+抽杜瓦</td>
              <td><span class="st-closed" style="background:#fee2e2; border:1px solid #f87171;">关 (手动)</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-closed" style="background:#fee2e2; border:1px solid #f87171;">关 (手动)</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span class="st-closed">关</span></td>
              <td><span style="color:#0284c7; font-weight:800;">进开/出关</span></td>
              <td style="text-align: left; padding-left: 0.5rem; color:#0284c7; font-weight:bold;">移至主机抽真空杜瓦</td>
            </tr>
            <tr style="background: rgba(16, 185, 129, 0.06);">
              <td style="text-align: left; font-weight: bold; padding-left: 0.85rem; color:#16a34a;">8. 自动降温至 1.65 K</td>
              <td><span class="st-open" style="background:#dcfce7; border:1px solid #4ade80;">必须手动开</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open">开</span></td>
              <td><span class="st-open" style="background:#dcfce7; border:1px solid #4ade80;">手动开</span></td>
              <td><span class="st-auto">自控</span></td>
              <td><span class="st-auto">自控</span></td>
              <td><span class="st-auto">自控</span></td>
              <td style="text-align: left; padding-left: 0.5rem; color:#64748b;">拆除并密封杜瓦盲板</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout-box callout-warn" style="font-size: 0.82rem;">
        💡 <strong>阀门状态特别说明</strong>：标注为“自控”的阀门（Scroll 泵、Cryo 进出、Dump 进出），在点击 <code>Cool Down</code> 按钮后由 attoDRY 控制系统自动调配执行，<strong>无需操作人员在软件 Expert 界面手动开启</strong>！
      </div>
    </section>

    <!-- ============================================== -->
    <!-- 第四部分：Pfeiffer HiCUBE 分子泵机组指令速查 -->
    <!-- ============================================== -->
    <section id="sec-dcu" class="section-block">
      <div class="section-header">
        <div class="section-title">
          <span>⚙️</span>
          <span>第四部分：Pfeiffer HiCUBE 分子泵机组 DCU 200 参数与控制方法</span>
        </div>
        <span style="font-size: 0.78rem; color: var(--text-muted);">粗抽与高真空切换核心参数与面板按键指引</span>
      </div>

      <div class="two-col-grid">
        <div class="info-card">
          <h4 style="color: var(--brand);">💻 DCU 200 常用参数代码表</h4>
          <table style="text-align: left; margin-top: 0.5rem; font-size: 0.82rem;">
            <thead>
              <tr>
                <th style="padding: 0.45rem;">代码</th>
                <th style="padding: 0.45rem;">参数名称</th>
                <th style="padding: 0.45rem;">功能定义与设置值</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><code>023</code></td>
                <td><strong>Motor pump</strong></td>
                <td><strong>分子泵电机开关</strong>：<code>off</code>=仅开前级干泵(粗抽)；<code>on</code>=启动分子泵(高真空)</td>
              </tr>
              <tr>
                <td><code>579</code></td>
                <td><strong>SetRotSpd</strong></td>
                <td><strong>设定额定转速</strong>：默认设定转速值 (Hz)，一般不需更改</td>
              </tr>
              <tr>
                <td><code>309</code></td>
                <td><strong>ActualSpd</strong></td>
                <td><strong>实际转速读数</strong>：实时监测分子泵转速 (Hz)，满速达标判定</td>
              </tr>
              <tr>
                <td><code>303</code></td>
                <td><strong>Current</strong></td>
                <td><strong>驱动电机电流</strong>：实时电流 (A)，负载异常时快速排查</td>
              </tr>
              <tr>
                <td><code>310</code></td>
                <td><strong>TempPmpBot</strong></td>
                <td><strong>分子泵底部温度</strong>：过热报警监测 (&lt; 65 ℃ 正常)</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="info-card">
          <h4 style="color: #b45309;">⌨️ DCU 200 面板参数修改三步法</h4>
          <ol style="margin-top: 0.5rem; padding-left: 1.35rem; font-size: 0.85rem;">
            <li><strong>翻阅定位参数</strong>：按面板上的 <code>▲</code> 或 <code>▼</code> 方向键，上下滚动屏幕直到显示目标参数（如 <code>023 Motor pump</code>）。</li>
            <li><strong>进入编辑状态</strong>：按下中间的确认键（<code>Enter / ↵</code>），此时参数设定值开始闪烁。</li>
            <li><strong>修改并确认保存</strong>：通过 <code>▲</code> / <code>▼</code> 将值调至目标状态（如从 <code>on</code> 改为 <code>off</code>），再次按下 <code>Enter</code> 确认保存。</li>
          </ol>
          <div class="callout-box callout-warn" style="margin-top: 0.85rem; font-size: 0.8rem;">
            ⚠️ <strong>防呆操作规范</strong>：粗抽时必须先改 <code>023=off</code>，严禁在大气压（&gt; 10 mbar）下直接开启分子泵电机，避免叶片高速旋转冲击损坏！
          </div>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- 第五部分：高频故障排除与安全红线 -->
    <!-- ============================================== -->
    <section id="sec-faults" class="section-block">
      <div class="section-header">
        <div class="section-title">
          <span>🚨</span>
          <span>第五部分：高频异常排查与现场四大安全红线</span>
        </div>
        <span style="font-size: 0.78rem; color: var(--text-muted);">应急响应处置与安全防护底线</span>
      </div>

      <div class="two-col-grid" style="margin-bottom: 1.25rem;">
        <div class="info-card">
          <h4>🛠️ 常见操作异常与应急处理</h4>
          <ul style="padding-left: 1.35rem; font-size: 0.85rem; line-height: 1.8;">
            <li><strong>初抽保压压升过快 (&Delta;P &gt; 0.5 mbar)</strong>：法兰或波纹管卡箍未卡紧，重新涂抹真空脂密封，检查 O 型圈有无压痕或灰尘。</li>
            <li><strong>中和水冷机报警停机</strong>：检查循环水过滤网是否堵塞，确认回水温度是否 &lt; 25 ℃，确认补水箱液位在正常刻度内。</li>
            <li><strong>降温速率过慢或极限基温停滞在 3 K 左右</strong>：检查样品腔交换气体是否补入不足，检查外层绝热杜瓦真空度是否下降，检查后部手阀是否全部完全拧开。</li>
            <li><strong>DCU 报警代码 Err001 / Err006</strong>：转速过慢或轴承过载，立即切断电源并检查泵入口有无异物或背压超标。</li>
          </ul>
        </div>

        <div class="info-card" style="background: var(--danger-bg); border-color: var(--danger-border);">
          <h4 style="color: var(--danger-text);">⛔ 实验室四大安全红线 (不可违反)</h4>
          <ol style="padding-left: 1.35rem; font-size: 0.85rem; line-height: 1.8; color: var(--danger-text);">
            <li><strong>步骤 8 手阀未开严禁启机</strong>：降温前必须确认压缩机后部手阀（中南大学 1、2 号）完全手动旋开，严禁手阀关闭下开启压缩机！</li>
            <li><strong>软件电磁气控阀严禁强行干预</strong>：点击 Cool Down 后由系统自控时序，严禁在软件 Expert 界面手动强行打开电磁阀。</li>
            <li><strong>吸附剂烘烤停热关气严禁颠倒</strong>：步骤 3 活化结束必须先停止加热 5 分钟后，方可手动关紧侧向阀 V8 出气口！</li>
            <li><strong>气瓶充气减压严禁超压</strong>：洗气与回充压力严禁超过 1050 mbar，必须安装双级高纯减压阀严密监视！</li>
          </ol>
        </div>
      </div>
    </section>

  </div>

  <!-- 图片放大 Lightbox 模态框 -->
  <div id="imgModal" onclick="closeModal()">
    <div style="position: relative; max-width: 95vw; display: flex; flex-direction: column; align-items: center;" onclick="event.stopPropagation()">
      <button type="button" onclick="closeModal()" style="position: absolute; -top: 40px; right: 0; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); color: white; border-radius: 2rem; padding: 0.25rem 0.85rem; font-size: 0.85rem; cursor: pointer; font-weight: bold; margin-bottom: 0.5rem;">✕ 关闭 (ESC)</button>
      <img id="modalImg" src="" alt="放大图" style="max-width: 94vw; max-height: 84vh; width: auto; height: auto; object-fit: contain; border-radius: 0.5rem; box-shadow: 0 12px 40px rgba(0,0,0,0.6); cursor: default;">
      <div id="modalCaption" style="color: #f8fafc; margin-top: 0.85rem; font-size: 0.92rem; text-align: center; font-weight: 600;"></div>
    </div>
  </div>

  <script>
    // Lightbox Modal
    function openModal(src, caption) {
      document.getElementById('modalImg').src = src;
      document.getElementById('modalCaption').innerText = caption || '';
      document.getElementById('imgModal').style.display = 'flex';
    }
    function closeModal() {
      document.getElementById('imgModal').style.display = 'none';
    }
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeModal();
    });

    // Theme Toggle
    function toggleTheme() {
      const html = document.documentElement;
      if (html.classList.contains('dark')) {
        html.classList.remove('dark');
        localStorage.setItem('attocube_theme', 'light');
        document.getElementById('themeIcon').innerText = '🌙 暗色';
      } else {
        html.classList.add('dark');
        localStorage.setItem('attocube_theme', 'dark');
        document.getElementById('themeIcon').innerText = '☀️ 亮色';
      }
    }
    if (localStorage.getItem('attocube_theme') === 'dark' || (!localStorage.getItem('attocube_theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.classList.add('dark');
      document.getElementById('themeIcon').innerText = '☀️ 亮色';
    }


    // Scroll To Step with visual highlight
    function scrollToStep(stepNum) {
      const el = document.getElementById('step-' + stepNum);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        el.style.transition = 'box-shadow 0.3s ease, border-color 0.3s ease';
        el.style.borderColor = 'var(--brand)';
        el.style.boxShadow = '0 0 0 4px rgba(2, 132, 199, 0.35)';
        setTimeout(() => {
          el.style.borderColor = '';
          el.style.boxShadow = '';
        }, 1600);
      }
    }

    // Step Checkbox Persistence
    function updateProgress() {
      const checkboxes = document.querySelectorAll('.step-checkbox');
      let done = 0;
      let remainingHours = 0;
      const state = {};

      checkboxes.forEach(cb => {
        const step = cb.getAttribute('data-step');
        const hours = parseFloat(cb.getAttribute('data-hours') || 0);
        state[step] = cb.checked;
        const node = document.getElementById('stepper-node-' + step);
        const num = document.getElementById('stepper-num-' + step);
        if (cb.checked) {
          done++;
          if (node) node.classList.add('completed');
          if (num) num.innerHTML = '✓';
        } else {
          remainingHours += hours;
          if (node) node.classList.remove('completed');
          if (num) num.innerHTML = (step < 10 ? '0' : '') + step;
        }
      });

      localStorage.setItem('attocube_compact_steps_state', JSON.stringify(state));
      document.getElementById('progressPercent').innerText = `${done}/8 步完成`;
      document.getElementById('stepProgressFill').style.width = `${(done / 8) * 100}%`;

      if (remainingHours > 0) {
        document.getElementById('remainingTimeText').innerText = `预计剩余工时：~${remainingHours.toFixed(1)} 小时`;
      } else {
        document.getElementById('remainingTimeText').innerText = `🎉 8 个再生步骤已全部完成！`;
      }
    }

    function loadProgress() {
      const saved = localStorage.getItem('attocube_compact_steps_state');
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
      if (confirm('确认清空所有步骤的打卡标记吗？')) {
        document.querySelectorAll('.step-checkbox').forEach(cb => cb.checked = false);
        updateProgress();
      }
    }

    loadProgress();
  </script>
</body>
</html>
"""

output_path = Path(__file__).resolve().parent / "低温设备操作速查卡_简化版.html"
output_path.write_text(html_content, encoding="utf-8", newline="\n")
print(f"Refined practical manual saved to {output_path}")
