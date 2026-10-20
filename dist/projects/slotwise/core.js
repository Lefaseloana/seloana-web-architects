export function parseCSV(text){
 const rows=[];let row=[],cell='',quoted=false;
 text=text.replace(/^\uFEFF/,'');
 for(let i=0;i<text.length;i++){const c=text[i];if(c==='"'){if(quoted&&text[i+1]==='"'){cell+='"';i++;}else if(!quoted&&cell!=='')throw Error('Quotes must start at the beginning of a field.');else quoted=!quoted;}else if(c===','&&!quoted){row.push(cell);cell='';}else if((c==='\n'||c==='\r')&&!quoted){if(c==='\r'&&text[i+1]==='\n')i++;row.push(cell);if(row.some(x=>x!==''))rows.push(row);row=[];cell='';}else cell+=c;}
 if(quoted)throw Error('Unclosed quoted field.');row.push(cell);if(row.some(x=>x!==''))rows.push(row);if(rows.length<2)throw Error('Include a header row and at least one data row.');const width=rows[0].length;if(rows.some(r=>r.length!==width))throw Error('Every row must have the same number of columns.');if(rows[0].some(h=>!h.trim())||new Set(rows[0]).size!==width)throw Error('Column names must be non-empty and unique.');return {headers:rows[0],rows:rows.slice(1)};
}
export function stats(values){const nums=values.map(v=>String(v).trim()).filter(v=>v!==''&&Number.isFinite(Number(v))).map(Number);if(!nums.length)return null;const a=[...nums].sort((a,b)=>a-b),sum=nums.reduce((a,b)=>a+b,0);return {count:a.length,sum,mean:sum/a.length,min:a[0],max:a.at(-1),median:a.length%2?a[(a.length-1)/2]:(a[a.length/2-1]+a[a.length/2])/2};}
export function contrast(a,b){const lum=h=>{if(!/^#[0-9a-f]{6}$/i.test(h))throw Error('Use a six-digit hex colour.');let v=[1,3,5].map(i=>parseInt(h.slice(i,i+2),16)/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4);return v[0]*.2126+v[1]*.7152+v[2]*.0722};let x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);}
export function findPath(width,height,walls,start,end,mode='bfs'){const blocked=new Set(walls),queue=[start],seen=new Set([start]),parent=new Map(),visited=[];while(queue.length){const cur=mode==='dfs'?queue.pop():queue.shift();visited.push(cur);if(cur===end){let path=[end];while(parent.has(path[0]))path.unshift(parent.get(path[0]));return {path,visited};}const x=cur%width,y=Math.floor(cur/width);for(const [nx,ny]of[[x+1,y],[x,y+1],[x-1,y],[x,y-1]]){let n=ny*width+nx;if(nx>=0&&nx<width&&ny>=0&&ny<height&&!blocked.has(n)&&!seen.has(n)){seen.add(n);parent.set(n,cur);queue.push(n)}}}return {path:[],visited};}
export function overlaps(a,b){return a.date===b.date&&a.start<b.end&&b.start<a.end;}
export function validSlot(a){return Boolean(a.date&&/^\d{2}:\d{2}$/.test(a.start)&&/^\d{2}:\d{2}$/.test(a.end)&&a.start<a.end);}
export function remainingSeconds(deadline,now=Date.now()){return Math.max(0,Math.ceil((deadline-now)/1000));}
export function escapeHTML(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
export function readStore(key,fallback){try{return JSON.parse(localStorage.getItem(key))??fallback}catch{return fallback}}
export function writeStore(key,value){try{localStorage.setItem(key,JSON.stringify(value));return true}catch{const el=document.querySelector('#status');if(el)el.textContent='Browser storage is unavailable. Changes will last only for this session.';return false}}
export function download(name,content,type='text/plain'){const url=URL.createObjectURL(new Blob([content],{type}));const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000)}
export const $=s=>document.querySelector(s);
export const uid=()=>globalThis.crypto?.randomUUID?.()??String(Date.now()+Math.random());
