import playwright from '/Users/josenicolassantiagomoreno/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright-core/index.js';
import { fileURLToPath } from 'node:url';
import { mkdir } from 'node:fs/promises';
const root = new URL('./', import.meta.url);
await mkdir(new URL('output/pdf/', root), { recursive: true });
const browser = await playwright.chromium.launch({ headless: true, executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' });
try {
  const page = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
  await page.goto(new URL('plan-accion-practiverso-12-31-octubre-2026.html', root).href, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({ media: 'print' });
  const layout = await page.locator('.page').evaluateAll(pages => pages.map((p, i) => {
    const footer = p.querySelector('.footer').getBoundingClientRect();
    const last = p.querySelector('.footer').previousElementSibling.getBoundingClientRect();
    return { page: i + 1, footerGap: Math.round(footer.top - last.bottom), width: p.offsetWidth, height: p.offsetHeight };
  }));
  if (layout.some(p => p.footerGap < 15)) throw new Error('Contenido demasiado cerca del pie: ' + JSON.stringify(layout));
  await page.pdf({ path: fileURLToPath(new URL('output/pdf/plan-accion-practiverso-12-31-octubre-2026.pdf', root)), format: 'A4', printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  console.log(JSON.stringify({ printLayout: layout }));
  await page.emulateMedia({ media: 'screen' });
  await page.setViewportSize({ width: 390, height: 844 });
  console.log(JSON.stringify(await page.evaluate(() => ({ mobileWidth: innerWidth, contentWidth: document.documentElement.scrollWidth }))));
} finally { await browser.close(); }
