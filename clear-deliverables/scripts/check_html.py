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
