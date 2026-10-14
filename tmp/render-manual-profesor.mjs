import pw from '/Users/josenicolassantiagomoreno/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright-core/index.js';
import fs from 'node:fs';
const root='/Users/josenicolassantiagomoreno/Documents/GitHub/Presentaciones';
const out=root+'/tmp/pdfs/manual-profesor-ux-ui';
const b=await pw.chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
const errors=[];
try{
 const p=await b.newPage({viewport:{width:1440,height:1000}});p.on('pageerror',e=>errors.push(e.message));
 await p.goto('file://'+root+'/material-profesor-ux-ui/manual-profesor.html');await p.emulateMedia({media:'print'});
 const layout=await p.locator('.page').evaluateAll(ps=>ps.map((x,i)=>({page:i+1,gap:Math.round(x.querySelector('.foot').getBoundingClientRect().top-x.querySelector('main').getBoundingClientRect().bottom)})));
 console.log(JSON.stringify({layout}));
 if(layout.some(x=>x.gap<12))throw new Error('Revisar espacio al pie');
 await p.pdf({path:root+'/output/pdf/manual-profesor-ux-ui.pdf',format:'A4',printBackground:true,preferCSSPageSize:true,margin:{top:0,right:0,bottom:0,left:0}});
 fs.copyFileSync(root+'/output/pdf/manual-profesor-ux-ui.pdf',root+'/material-profesor-ux-ui/manual-profesor.pdf');

}finally{await b.close();}
