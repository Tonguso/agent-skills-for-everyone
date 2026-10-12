"""Original minimal offline layout probe. Trusted HTML only; not a sandbox."""
import argparse
import json
import sys
import threading
import os
from pathlib import Path

PROBE = r"""() => {
 const issues=[];
 const add=(rule,detail)=>{if(issues.length<100)issues.push({rule,detail});};
 const label=e=>e.id || e.tagName.toLowerCase();
 const shown=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0;};
 const hits=(a,b)=>a.left<b.right-1&&b.left<a.right-1&&a.top<b.bottom-1&&b.top<a.bottom-1;
 if(document.documentElement.scrollWidth>innerWidth+2)add('page-overflow',`${document.documentElement.scrollWidth}px in ${innerWidth}px`);
 for(const e of document.body.querySelectorAll('*')){
   if(!shown(e)||e.closest('svg'))continue;
   const s=getComputedStyle(e);
   if(s.display==='inline')continue;
   if(!['auto','scroll'].includes(s.overflowX)&&e.clientWidth>0&&e.scrollWidth>e.clientWidth+2)add('box-overflow',label(e));
   if(['hidden','clip'].includes(s.overflowY)&&e.scrollHeight>e.clientHeight+2)add('clipped-content',label(e));
   if(e.tagName==='IMG'&&(!e.complete||e.naturalWidth===0))add('broken-image',label(e));
 }
 for(const svg of document.querySelectorAll('svg')){
   if(!shown(svg))continue;
   const frame=svg.getBoundingClientRect();
   const texts=[...svg.querySelectorAll('text')].filter(shown);
   for(let i=0;i<texts.length;i++){
     const a=texts[i].getBoundingClientRect();
     if(a.left<frame.left-2||a.right>frame.right+2||a.top<frame.top-2||a.bottom>frame.bottom+2)add('svg-label-outside',texts[i].textContent);
     for(let j=i+1;j<texts.length;j++)if(hits(a,texts[j].getBoundingClientRect()))add('svg-label-overlap',texts[i].textContent+' / '+texts[j].textContent);
   }
 }
 // Arrow geometry, in each figure's own user units. Arrows = line/path/polyline with a marker.
 const vis=e=>{const s=getComputedStyle(e);return s.display!=='none'&&s.visibility!=='hidden';};
 const segD=(p,a,b)=>{const dx=b[0]-a[0],dy=b[1]-a[1],L=dx*dx+dy*dy;let t=L?((p[0]-a[0])*dx+(p[1]-a[1])*dy)/L:0;t=Math.max(0,Math.min(1,t));return Math.hypot(p[0]-a[0]-t*dx,p[1]-a[1]-t*dy);};
 const edgeD=(p,P)=>Math.min(...P.map((a,i)=>segD(p,a,P[(i+1)%P.length])));
 const inPoly=(p,P)=>{let c=false;for(let i=0,j=P.length-1;i<P.length;j=i++){const a=P[i],b=P[j];if((a[1]>p[1])!==(b[1]>p[1])&&p[0]<(b[0]-a[0])*(p[1]-a[1])/(b[1]-a[1])+a[0])c=!c;}return c;};
 const parsePath=d=>{const t=d.match(/[A-Za-z]|-?(?:\d+\.?\d*|\.\d+)(?:e[-+]?\d+)?/gi)||[];const pts=[];let i=0,c='',x=0,y=0,sx=0,sy=0;const n=()=>parseFloat(t[i++]);
   while(i<t.length){if(/[A-Za-z]/.test(t[i]))c=t[i++];const r=c===c.toLowerCase();
     switch(c.toUpperCase()){
       case 'M':x=(r?x:0)+n();y=(r?y:0)+n();sx=x;sy=y;pts.push([x,y]);c=r?'l':'L';break;
       case 'L':x=(r?x:0)+n();y=(r?y:0)+n();pts.push([x,y]);break;
       case 'H':x=(r?x:0)+n();pts.push([x,y]);break;
       case 'V':y=(r?y:0)+n();pts.push([x,y]);break;
       case 'Z':x=sx;y=sy;pts.push([x,y]);break;
       default:return null;}}
   return pts;};
 [...document.querySelectorAll('svg')].forEach((svg,si)=>{
   if(!shown(svg)||!svg.getScreenCTM())return;
   const S=svg.getScreenCTM().inverse();
   const tf=e=>{const m=S.multiply(e.getScreenCTM());return (x,y)=>{const q=new DOMPoint(x,y).matrixTransform(m);return [q.x,q.y];};};
   const vb=svg.viewBox.baseVal;
   const V=vb&&vb.width?[vb.x,vb.y,vb.width,vb.height]:[0,0,svg.width.baseVal.value,svg.height.baseVal.value];
   const fig='figure '+(si+1);
   const shapes=[];
   for(const e of svg.querySelectorAll('rect,polygon,circle,ellipse')){
     if(!vis(e)||e.closest('marker,defs,pattern,clipPath,mask'))continue;
     const f=tf(e),g=k=>e[k].baseVal.value;
     if(e.tagName==='rect'){const x=g('x'),y=g('y'),w=g('width'),h=g('height');
       if(w*h>=0.5*V[2]*V[3])continue;
       shapes.push({poly:[f(x,y),f(x+w,y),f(x+w,y+h),f(x,y+h)]});}
     else if(e.tagName==='polygon'){const P=[];for(let k=0;k<e.points.numberOfItems;k++){const q=e.points.getItem(k);P.push(f(q.x,q.y));}if(P.length>2)shapes.push({poly:P});}
     else{const c=f(g('cx'),g('cy')),sc=Math.hypot(...f(1,0).map((v,k)=>v-f(0,0)[k]));
       const rx=(e.tagName==='circle'?g('r'):g('rx'))*sc,ry=(e.tagName==='circle'?g('r'):g('ry'))*sc;
       shapes.push({ell:[c[0],c[1],rx,ry]});}
   }
   const bd=(p,s)=>s.poly?edgeD(p,s.poly):Math.abs(Math.hypot((p[0]-s.ell[0])/s.ell[2],(p[1]-s.ell[1])/s.ell[3])-1)*Math.min(s.ell[2],s.ell[3]);
   const inside=(p,s)=>s.poly?inPoly(p,s.poly):Math.hypot((p[0]-s.ell[0])/s.ell[2],(p[1]-s.ell[1])/s.ell[3])<1;
   const texts=[...svg.querySelectorAll('text')].filter(shown).map(e=>{const b=e.getBBox(),f=tf(e),c=[f(b.x,b.y),f(b.x+b.width,b.y+b.height)];
     return {name:e.textContent.trim(),box:[Math.min(c[0][0],c[1][0]),Math.min(c[0][1],c[1][1]),Math.max(c[0][0],c[1][0]),Math.max(c[0][1],c[1][1])]};});
   for(const e of svg.querySelectorAll('line,path,polyline')){
     if(!vis(e)||e.closest('marker,defs'))continue;
     const cs=getComputedStyle(e),end=cs.markerEnd!=='none',start=cs.markerStart!=='none';
     if(!end&&!start)continue;
     let raw;
     if(e.tagName==='line')raw=[[e.x1.baseVal.value,e.y1.baseVal.value],[e.x2.baseVal.value,e.y2.baseVal.value]];
     else if(e.tagName==='polyline'){raw=[];for(let k=0;k<e.points.numberOfItems;k++){const q=e.points.getItem(k);raw.push([q.x,q.y]);}}
     else raw=parsePath(e.getAttribute('d')||'');
     const id=`${fig} ${e.id||e.tagName}`;
     if(!raw){add('svg-arrow-curve',id+': curve or arc command; use straight segments');continue;}
     const f=tf(e);let P=raw.map(q=>f(q[0],q[1])).filter((q,k,a)=>!k||Math.hypot(q[0]-a[k-1][0],q[1]-a[k-1][1])>0.01);
     if(!end)P=P.reverse();
     if(P.length<2)continue;
     const r=q=>`(${q[0].toFixed(0)},${q[1].toFixed(0)})`,tag=`${id} ${r(P[0])}->${r(P[P.length-1])}`;
     const segs=P.slice(1).map((q,k)=>[P[k],q]);
     if(segs.some(([a,b])=>Math.abs(a[0]-b[0])>0.5&&Math.abs(a[1]-b[1])>0.5))add('svg-arrow-diagonal',tag);
     if(P.some(q=>q[0]<V[0]||q[1]<V[1]||q[0]>V[0]+V[2]||q[1]>V[1]+V[3]))add('svg-arrow-outside',tag);
     const tip=P[P.length-1],gap=shapes.length?Math.min(...shapes.map(s=>bd(tip,s))):Infinity;
     if(gap>1)add('svg-arrow-gap',`${tag}: tip ${gap===Infinity?'has no target shape':gap.toFixed(1)+' from nearest border'}`);
     const mid=(cs.markerEnd!=='none'?cs.markerEnd:cs.markerStart).match(/#([^")]+)/),mk=mid&&document.getElementById(mid[1]);
     const ml=mk?mk.markerWidth.baseVal.value*(mk.getAttribute('markerUnits')==='userSpaceOnUse'?1:(parseFloat(cs.strokeWidth)||1)):0;
     const len=segs.reduce((s,[a,b])=>s+Math.hypot(b[0]-a[0],b[1]-a[1]),0);
     if(len-ml<20)add('svg-arrow-short',`${tag}: shaft ${(len-ml).toFixed(1)} beyond marker`);
     const samples=segs.flatMap(([a,b])=>{const n=Math.max(1,Math.ceil(Math.hypot(b[0]-a[0],b[1]-a[1])/2));return Array.from({length:n+1},(_,k)=>[a[0]+(b[0]-a[0])*k/n,a[1]+(b[1]-a[1])*k/n]);});
     for(const s of shapes){
       if(inside(P[0],s)&&bd(P[0],s)>2||inside(tip,s)&&bd(tip,s)>2)continue; // container, not an obstacle
       if(samples.some(q=>inside(q,s)&&bd(q,s)>2)){add('svg-arrow-through-box',tag);break;}
     }
     for(const t of texts){const b=t.box;
       if(samples.some(q=>q[0]>b[0]-1&&q[0]<b[2]+1&&q[1]>b[1]-1&&q[1]<b[3]+1))add('svg-label-on-line',`${tag} / ${t.name}`);}
   }
 });
 return {language:document.documentElement.lang,text:document.body.innerText,issues};
}"""

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('page', type=Path)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--widths', type=int, nargs='+', default=[1280, 390])
    args = parser.parse_args()
    if not 1 <= len(args.widths) <= 5 or any(not 320 <= w <= 2560 for w in args.widths):
        parser.error('Use 1-5 widths, each 320-2560 pixels.')
    page_path = args.page.resolve()
    if not page_path.is_file() or page_path.stat().st_size > 2_000_000:
        parser.error('Input must be an existing HTML file of at most 2 MB.')
    try:
        page_path.read_text(encoding='utf-8')
        args.out.mkdir(parents=True, exist_ok=False)
    except (OSError, UnicodeError) as exc:
        print(f'Input/output unavailable: {exc}', file=sys.stderr)
        return 2
    report = {'input': str(page_path), 'semantic_validation': False, 'views': [], 'blocked': [], 'js_errors': []}
    # Bounded total runtime, including browser startup. Parent command is bounded too.
    def deadline():
        print('Rendering exceeded 45 seconds; no pass claimed.', file=sys.stderr, flush=True)
        os._exit(2)
    timer = threading.Timer(45, deadline)
    timer.daemon = True
    timer.start()
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context(service_workers='block', accept_downloads=False)
            uri = page_path.as_uri()
            def route(request_route):
                if request_route.request.url == uri:
                    request_route.continue_()
                else:
                    report['blocked'].append(request_route.request.url)
                    request_route.abort()
            context.route('**/*', route)
            context.route_web_socket('**/*', lambda ws: ws.close())
            page = context.new_page()
            page.set_default_timeout(5000)
            page.on('pageerror', lambda error: report['js_errors'].append(str(error)))
            for width in args.widths:
                page.set_viewport_size({'width': width, 'height': 900})
                page.goto(uri, wait_until='load', timeout=10000)
                page.evaluate('() => document.fonts.ready')
                data = page.evaluate(PROBE)
                data['width'] = width
                data['visible_text_length'] = len(data.pop('text'))
                height = page.evaluate('Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)')
                if height > 6000:
                    data['issues'].append({'rule': 'render-limit', 'detail': f'{height}px exceeds 6000px; split page or inspect separately'})
                else:
                    image = args.out / f'screen-{width}.png'
                    page.screenshot(path=str(image), full_page=True, timeout=5000)
                    data['screenshot'] = str(image.resolve())
                report['views'].append(data)
            context.close()
            browser.close()
        report['passed'] = not (report['blocked'] or report['js_errors'] or any(v['issues'] for v in report['views']))
        code = 0 if report['passed'] else 1
    except Exception as exc:
        report['passed'] = False
        report['error'] = str(exc)
        code = 2
    finally:
        timer.cancel()
    (args.out / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'exit': code, 'report': str((args.out / 'report.json').resolve())}))
    return code

if __name__ == '__main__':
    sys.exit(main())
