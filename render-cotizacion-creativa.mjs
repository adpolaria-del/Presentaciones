import playwright from '/Users/josenicolassantiagomoreno/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright-core/index.js';
import { mkdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
const root=new URL('./',import.meta.url);
await mkdir(new URL('output/pdf/',root),{recursive:true});
await mkdir(new URL('tmp/pdfs/cotizacion-creativa/',root),{recursive:true});
const browser=await playwright.chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
try{
const page=await browser.newPage({viewport:{width:1100,height:1300}});
await page.goto(new URL('cotizacion-servicios-creativos-octubre-2026.html',root).href);
await page.evaluate(()=>document.fonts.ready);
await page.emulateMedia({media:'print'});
const check=await page.locator('.page').evaluateAll(pages=>pages.map((p,i)=>({page:i+1,width:p.offsetWidth,height:p.offsetHeight,footerGap:p.querySelector('.footer').getBoundingClientRect().top-p.querySelector('.content').getBoundingClientRect().bottom})));
console.log(JSON.stringify(check));
if(check.some(p=>p.footerGap<15))throw new Error('Insufficient footer clearance');
await page.pdf({path:fileURLToPath(new URL('output/pdf/cotizacion-servicios-creativos-octubre-2026.pdf',root)),format:'A4',printBackground:true,preferCSSPageSize:true});
await page.emulateMedia({media:'screen'});await page.setViewportSize({width:390,height:844});
const mobile=await page.evaluate(()=>({width:innerWidth,contentWidth:document.documentElement.scrollWidth}));
console.log(JSON.stringify({mobile}));if(mobile.width!==mobile.contentWidth)throw new Error('Mobile overflow');
}finally{await browser.close();}