"""Portable smoke tests. Requires Playwright and Chromium; no network sources.

Run: python scripts/test_check_html.py
"""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


CHECKER = Path(__file__).with_name('check_html.py')


class HtmlChecks(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def run_page(self, content):
        page = self.root / 'sample.html'
        page.write_text(content, encoding='utf-8')
        out = self.root / 'report'
        result = subprocess.run(
            [sys.executable, str(CHECKER), str(page), '--out', str(out)],
            capture_output=True, text=True, encoding='utf-8', timeout=60,
        )
        report = out / 'report.json'
        self.assertTrue(report.exists(), result.stdout + result.stderr)
        return result, json.loads(report.read_text(encoding='utf-8'))

    def test_readable_bilingual_page(self):
        result, report = self.run_page('''<!doctype html><html lang="zh-CN">
        <meta charset="utf-8"><style>
        body {margin:20px;font:18px sans-serif;line-height:1.5}
        main {max-width:60ch} svg {max-width:100%}
        </style><body><main><h1>操作说明 / Procedure</h1>
        <p>先验证数据——再发布。Validate the data before publication.</p>
        <svg viewBox="0 0 280 60" width="280" height="60">
        <text x="10" y="30">Input</text><text x="150" y="30">Output</text>
        </svg></main></body></html>''')
        self.assertEqual(result.returncode, 0, report)
        self.assertTrue(report['passed'])
        self.assertFalse(report['semantic_validation'])
        self.assertEqual(len(report['views']), 2)
        for view in report['views']:
            self.assertEqual(view['language'], 'zh-CN')
            self.assertGreater(view['visible_text_length'], 20)
            self.assertTrue(Path(view['screenshot']).is_file())

    def test_detects_faults_and_blocks_external_resources(self):
        result, report = self.run_page('''<!doctype html><html lang="en">
        <meta charset="utf-8"><body>
        <div style="width:3000px">Too wide</div>
        <div style="height:10px;overflow:hidden"><p>Clipped content</p></div>
        <svg width="150" height="60">
        <text x="10" y="30">Overlap</text><text x="10" y="30">Overlap</text>
        <text x="200" y="30">Outside</text></svg>
        <img src="https://example.invalid/blocked.png">
        <script>throw new Error('fixture error')</script></body></html>''')
        self.assertEqual(result.returncode, 1, report)
        self.assertFalse(report['passed'])
        self.assertTrue(report['blocked'])
        self.assertTrue(report['js_errors'])
        expected = {'page-overflow', 'clipped-content', 'svg-label-overlap', 'svg-label-outside'}
        for view in report['views']:
            self.assertTrue(expected <= {item['rule'] for item in view['issues']}, view)

    def test_existing_output_is_not_overwritten(self):
        page = self.root / 'sample.html'
        page.write_text('<html><body>Example</body></html>', encoding='utf-8')
        out = self.root / 'report'
        out.mkdir()
        sentinel = out / 'report.json'
        sentinel.write_text('preserve this', encoding='utf-8')
        result = subprocess.run(
            [sys.executable, str(CHECKER), str(page), '--out', str(out)],
            capture_output=True, timeout=10,
        )
        self.assertEqual(result.returncode, 2)
        self.assertEqual(sentinel.read_text(encoding='utf-8'), 'preserve this')


if __name__ == '__main__':
    unittest.main()
