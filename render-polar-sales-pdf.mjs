import playwright from '/Users/josenicolassantiagomoreno/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright-core/index.js';

const { chromium } = playwright;
const browser = await chromium.launch({
  headless: true,
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
});
const page = await browser.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1 });
await page.goto('file:///Users/josenicolassantiagomoreno/Documents/GitHub/Presentaciones/polar-ia-guia-ventas-usa.html', { waitUntil: 'networkidle' });
await page.emulateMedia({ media: 'print' });
await page.pdf({
  path: '/Users/josenicolassantiagomoreno/Documents/GitHub/Presentaciones/output/pdf/polar-ia-guia-ventas-usa.pdf',
  width: '13.333in',
  height: '7.5in',
  printBackground: true,
  preferCSSPageSize: true,
  margin: { top: 0, right: 0, bottom: 0, left: 0 },
});
await browser.close();
