import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { existsSync, mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { spawn } from 'node:child_process';

const ROOT = new URL('..', import.meta.url);
const HTML_FILE = '低温量子光学测试系统手册.html';
const CDP_ENDPOINT = process.env.UI_TEST_CDP_ENDPOINT || 'http://127.0.0.1:9224';
const HTTP_ENDPOINT = process.env.UI_TEST_HTTP_ENDPOINT || 'http://127.0.0.1:8765';

const wait = ms => new Promise(resolve => setTimeout(resolve, ms));

async function targets() {
  try {
    const response = await fetch(`${CDP_ENDPOINT}/json`);
    if (!response.ok) return null;
    return await response.json();
  } catch {
    return null;
  }
}

async function ensureServer() {
  try {
    const response = await fetch(`${HTTP_ENDPOINT}/${encodeURIComponent(HTML_FILE)}`, { signal: AbortSignal.timeout(1000) });
    if (response.ok) return null;
  } catch { /* start the local server below */ }

  const server = createServer(async (request, response) => {
    const pathname = decodeURIComponent(new URL(request.url, HTTP_ENDPOINT).pathname);
    const file = pathname === '/' ? HTML_FILE : pathname.replace(/^\//, '');
    if (file !== HTML_FILE) {
      response.writeHead(404).end('Not found');
      return;
    }
    try {
      response.writeHead(200, { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' });
      response.end(await readFile(new URL(file, ROOT)));
    } catch {
      response.writeHead(404).end('Not found');
    }
  });
  await new Promise((resolve, reject) => {
    server.once('error', reject);
    server.listen(8765, '127.0.0.1', resolve);
  });
  return server;
}

async function ensureBrowser() {
  let list = await targets();
  if (list?.some(target => target.type === 'page' && target.webSocketDebuggerUrl)) return { process: null, list, server: null };

  const edge = process.env.EDGE_BIN || [
    'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
    'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
    'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  ].find(existsSync);
  if (!edge) throw new Error('No Chromium/Edge executable found. Set EDGE_BIN to a browser executable.');
  const profile = mkdtempSync(join(tmpdir(), 'ui-test-browser-'));
  const browser = spawn(edge, [
    '--headless=new', '--disable-gpu', '--no-sandbox', '--no-first-run', '--no-default-browser-check',
    '--remote-debugging-address=127.0.0.1', '--remote-debugging-port=9224', '--remote-allow-origins=*',
    `--user-data-dir=${profile}`, 'about:blank',
  ], { stdio: 'ignore', windowsHide: true });
  for (let attempt = 0; attempt < 50; attempt += 1) {
    list = await targets();
    if (list?.some(target => target.type === 'page' && target.webSocketDebuggerUrl)) break;
    await wait(200);
  }
  if (!list?.some(target => target.type === 'page' && target.webSocketDebuggerUrl)) {
    browser.kill();
    throw new Error('Chromium launched but its remote-debugging endpoint did not become ready.');
  }
  return { process: browser, list, server: null };
}

export async function openPage() {
  const server = await ensureServer();
  let browser;
  try {
    browser = await ensureBrowser();
  } catch (error) {
    server?.close();
    throw error;
  }
  const list = browser.list;
  const page = list.find(target => target.type === 'page' && target.webSocketDebuggerUrl);
  const socket = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => {
    socket.addEventListener('open', resolve, { once: true });
    socket.addEventListener('error', reject, { once: true });
  });
  let messageId = 0;
  const pending = new Map();
  socket.addEventListener('message', event => {
    const message = JSON.parse(event.data);
    const callback = pending.get(message.id);
    if (callback) { pending.delete(message.id); callback(message); }
  });
  function send(method, params = {}) {
    const id = ++messageId;
    socket.send(JSON.stringify({ id, method, params }));
    return new Promise((resolve, reject) => {
      pending.set(id, message => message.error ? reject(message.error) : resolve(message.result));
    });
  }
  let closed = false;
  const cleanup = () => {
    if (closed) return;
    closed = true;
    socket.close();
    browser.process?.kill();
    server?.close();
  };
  process.once('exit', cleanup);
  return {
    send,
    close() {
      cleanup();
      process.removeListener('exit', cleanup);
    },
  };
}
