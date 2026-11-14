const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const logo=fs.readFileSync('/home/claude/hub/icons/logo.svg','utf8');
const shot=async(w,h,html,out,scale=1)=>{const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:scale});await p.setContent(`<html><body style="margin:0">${html}</body></html>`);await p.screenshot({path:out,omitBackground:true});await p.close();};
await shot(256,256,`<div style="width:256px;height:256px">${logo.replace('<svg','<svg width="256" height="256"')}</div>`,'logo256.png');
const font='font-family:Segoe UI,Arial,sans-serif';
await shot(164,314,`<div style="width:164px;height:314px;background:linear-gradient(160deg,#2a1a0c 0%,#1b1c1d 55%,#141516 100%);position:relative;overflow:hidden;${font}">
 <div style="position:absolute;left:-40px;bottom:-60px;width:220px;height:220px;border-radius:50%;border:2px solid rgba(255,115,0,.25)"></div>
 <div style="position:absolute;left:-10px;bottom:-30px;width:150px;height:150px;border-radius:50%;border:2px solid rgba(255,115,0,.18)"></div>
 <div style="position:absolute;left:22px;top:34px;width:120px;height:120px">${logo.replace('<svg','<svg width="120" height="120"')}</div>
 <div style="position:absolute;left:0;right:0;top:170px;text-align:center;color:#fff;font-weight:800;font-size:17px;letter-spacing:.3px">PrintFlow Studio</div>
 <div style="position:absolute;left:0;right:0;top:194px;text-align:center;color:#ff8a2e;font-size:10.5px;font-weight:600">Prepress Automation Suite</div>
 <div style="position:absolute;left:14px;right:14px;top:222px;height:2px;background:linear-gradient(90deg,transparent,#ff7300,transparent)"></div>
 <div style="position:absolute;left:0;right:0;bottom:16px;text-align:center;color:#9a9a9a;font-size:9px;font-style:italic">Designed by Mr. Haii<br>In Thành Đạt</div></div>`,'welcome.png');
await shot(150,57,`<div style="width:150px;height:57px;background:#fff;position:relative;${font}">
 <div style="position:absolute;right:8px;top:6px;width:45px;height:45px">${logo.replace('<svg','<svg width="45" height="45"')}</div></div>`,'header.png');
await b.close()})();
