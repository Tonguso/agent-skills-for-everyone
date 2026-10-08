# Offline HTML check

Prerequisites: Python 3.9+, Playwright 1.48+ and its installed Chromium browser. Check only trusted/generated HTML; JavaScript runs. A fresh context has no saved login/profile. Network blocking is not a security sandbox. No dependencies are installed by this tool. If setup is authorized, install with `python -m pip install "playwright>=1.48"` followed by `python -m playwright install chromium`.

Use UTF-8, an appropriate html lang (for example zh-CN), inline CSS/SVG and local system font stacks. The input must be self-contained: other local files and network fetches are blocked. This restriction belongs to this checker, not to every deliverable.

Run from the skill directory, replacing the input and output paths:
```sh
python scripts/check_html.py "path/to/example.html" --out "path/to/example-check"
```
The output directory must be NEW to avoid overwriting prior work. Default viewports: 1280 and 390 pixels, height 900. For another intended width add `--widths 1440 800 390`. At most five widths, 320-2560px each. Screenshots are bounded to 6000px; exceeding this limit is a reported blocker, not a partial-page pass. An internal 45-second alarm terminates long execution. Outer execution should also stay bounded.

Outputs: report.json and screen-WIDTH.png. Exit 0 means measured rules passed; 1 means defects found; 2 means prerequisites/input/rendering failed. Report fields include viewport issues, blocked requests, JavaScript errors, observed document language and visible-text length. No English-only word counting, dash/emoji bans or visual-style restrictions are applied.

Rules: unintended page-wide horizontal overflow; overflow in non-scrolling boxes; hidden/clip vertical truncation; SVG label bounds and pairwise collisions (bounding-box heuristics); broken images; JS errors; attempts to fetch external resources. Intentional local horizontal/vertical scroll containers are allowed but still require human inspection.

Limits: does not verify semantics, sources, arrow correctness, missing steps, complete accessibility/contrast, general HTML element collisions, interactive states, font glyph coverage or print pagination. SVG checks can flag intentional overlaps and miss issues outside their heuristics. Look at screenshots, assess exceptions, fix actual defects and rerun. A layout pass is never a correctness certificate. Printing requires a separate print render and inspection.

Failure: preserve report/draft and disclose blocked checks. Follow the user's existing authorization and the host's permissions for any dependency installation. Do not fall back to authenticated profiles. If output exists, choose a new directory rather than overwrite.

Run the bundled smoke tests with `python scripts/test_check_html.py`. They generate temporary English/Chinese and faulty HTML, check fresh renderer results, and require the same browser dependencies.
