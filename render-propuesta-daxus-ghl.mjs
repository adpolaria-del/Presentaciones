import playwright from '/Users/josenicolassantiagomoreno/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright-core/index.js';
import { fileURLToPath } from 'node:url';
const root = new URL('./', import.meta.url);
const browser = await playwright.chromium.launch({ headless: true, executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' });
try {
  const page = await browser.newPage({viewport:{width:1100,height:1400}});
  await page.goto(new URL('propuesta-curso-daxus-ghl.html',root).href,{waitUntil:'load'});
  await page.evaluate(()=>document.fonts.ready);
  await page.emulateMedia({media:'print'});
  const layout=await page.locator('.page').evaluateAll(ps=>ps.map((p,i)=>({page:i+1,gap:Math.round(p.querySelector('.foot').getBoundingClientRect().top-p.querySelector('main').getBoundingClientRect().bottom),height:p.offsetHeight,width:p.offsetWidth})));
  console.log(JSON.stringify({layout}));
  if(layout.some(x=>x.gap<15))throw new Error('Contenido muy cerca del pie');
  await page.pdf({path:fileURLToPath(new URL('output/pdf/propuesta-curso-daxus-ghl.pdf',root)),format:'A4',printBackground:true,preferCSSPageSize:true,margin:{top:0,right:0,bottom:0,left:0}});
  await page.emulateMedia({media:'screen'});
  await page.setViewportSize({width:390,height:844});
  const mobile=await page.evaluate(()=>({viewport:innerWidth,content:document.documentElement.scrollWidth}));
  console.log(JSON.stringify({mobile}));
  if(mobile.content>mobile.viewport)throw new Error('Desbordamiento en móvil');
}finally{await browser.close();}
