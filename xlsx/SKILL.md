---
name: xlsx
description: Create, edit, restructure, audit or fix Excel workbooks (.xlsx, .xlsm) and financial models. Use whenever a task produces or changes a spreadsheet, adds formulas, tabs or rows to someone else's workbook, builds a model with inputs, calculations and outputs, or checks a workbook for errors, broken references or hardcoded numbers. Not for slide decks or plain CSV dumps where no workbook is wanted.
license: MIT. scripts/xlsx_restructure.py is MIT (Nous Research), see THIRD_PARTY_NOTICES.md.
compatibility: Python with openpyxl. Editing files that contain charts, pivots or macros, and recalculation, need Microsoft Excel on Windows with pywin32. Does not use LibreOffice.
metadata:
  author: Hogan Tong
  version: "1.0.0"
  created: "2026-10-05"
---

# Excel workbooks

Four rules. They are not optional.

1. Formulas, not pasted numbers.
2. Other people's files: keep their formatting, use Excel itself when openpyxl would damage something, and never overwrite the original by default.
3. Model layout: separate inputs, calculations and outputs, label every input's unit, keep constants out of calc formulas, and mark input cells visibly.
4. No delivery until the workbook has been recalculated in Excel with zero error cells and the task's own checks pass.

## 1. Formulas, not values

- Every derived number goes into the cell as an Excel formula (`ws["D10"] = "=SUM(D2:D9)"`), so the user can audit it and it updates when inputs change. Never calculate in Python and paste the result.
- Only these may be static values: raw inputs, source data pulls (prices, holdings, index weights) labelled with source and as-of date, and dates and labels.
- If a value really has to be pasted (a snapshot or a file for a system upload), say so in a note beside it, e.g. "Snapshot of X as of 2026-10-05, values only."
- openpyxl writes formulas without calculating them. The file has no cached values until Excel recalculates it, so never judge a result from Python's view of the file. Recalculate first (section 4).
- Use English function names and commas in formulas, as openpyxl writes them. No dynamic-array spills or LAMBDA unless the user's Excel version is known to support them.

## 2. Editing someone else's workbook

Default: never touch the original. Write to a copy or a new named file (`<name>_v2.xlsx`, `<name>_edited.xlsx`) in the folder the user asked for, and tell them the path. Overwrite the original only if they explicitly ask.

Pick the engine first by checking what the file contains:

```
python -c "import zipfile,sys;n=zipfile.ZipFile(sys.argv[1]).namelist();print(sorted({p.split('/')[1] for p in n if p.startswith('xl/') and '/' in p[3:]}))" FILE
```

- If the file contains charts, drawings, media, pivotTables, pivotCache, slicers, a vbaProject.bin, ctrlProps, activeX or a data model, or if it's an .xlsm or .xlsb: **edit through Excel COM**. openpyxl drops charts, images and pivots on save and strips macros. See `references/excel-com.md`.
- Plain grid, formats and formulas only: openpyxl is fine. Load with `load_workbook(path)`, not `data_only=True`, because saving a data_only workbook replaces every formula with its last value. Use `keep_links=True` (the default). After saving, spot-check that fonts, fills, number formats, column widths and conditional formats survived.
- Match the existing house style (fonts, colours, number formats, layout). Add to their structure. Don't reorganise it unless asked.
- Before changing a cell, check whether anything depends on it. Inserting or deleting rows and columns breaks references unless Excel or a reference-aware tool does it:
  - Excel COM: `ws.Rows(5).Insert()`. Excel moves every reference, chart and name itself. Preferred for anyone else's file.
  - openpyxl-only files: `scripts/xlsx_restructure.py`. It writes a new `<name>_restructured.xlsx` by default and refuses files with charts, pivots or VBA. See `references/restructuring.md`.
  - Never use bare openpyxl `insert_rows` or `delete_cols`. They move cells but leave formulas pointing at the old addresses.

## 3. Financial-model conventions

Layout:
- Keep inputs, calculations and outputs on separate tabs: `Inputs`, `Calc` (or one tab per calculation block) and `Output` or `Summary`. A small model can use clearly separated, labelled blocks on one sheet instead. Data pulls go on their own `Data_<source>` tab with source and as-of date at the top.
- Calculations flow one way: Inputs → Calc → Output. Outputs never feed back into inputs, and there are no circular references unless the user asks for one and iteration is documented.
- Within a block, keep the same formula across a row or column. If one cell breaks the pattern, comment it.

Inputs:
- Every input has a label and a unit in the next cell or a Unit column: `bp`, `%`, `USD m`, `shares`, `x`, `days`, `date`. A number without a unit is ambiguous (is `0.5` 0.5%, 50% or 50bp?). Label a unit as the meaning, e.g. "Spread | 35 | bp", and convert inside the calc with a named factor.
- Mark input cells visibly: blue font (0000FF) on a light yellow fill (FFF2CC). Formulas are black, and links to other sheets or files are green (008000). Add a small key on the Inputs tab.
- Name important inputs (defined names such as `FX_USDGBP` or `Fin_Spread_bp`) when that makes formulas easier to read.

Calculations:
- No constants inside calc formulas. `=B5*1.05`, `=C3/365` and `=D2*0.0001` are all wrong. Put 5%, the 365 day-count and the bp-to-decimal 10,000 in labelled input cells and reference them. The only exceptions are 0, 1, and unit conversions that can never change (12 months, 100 for percent display), and even those should carry a comment if they're not obvious.
- No hardcoded overrides typed over a formula. If an override is needed, add an explicit override input and use `=IF(Override<>"",Override,Calc)`.
- Keep formulas short. Split a long nested formula into helper columns with headers.
- Put checks on the Output tab: totals that tie (sum of parts = total, weights = 100%, cash = notional × price), each returning TRUE/FALSE or a difference, plus one overall check cell.

Errors are fixed, not hidden:
- Every #REF!, #DIV/0!, #VALUE!, #N/A and #NAME? is a defect to trace and fix at its source.
- Don't wrap formulas in IFERROR or IFNA by default. A blanket IFERROR turns a broken lookup into a quiet zero or blank, and the total looks fine while being wrong.
- IFERROR or IFNA is allowed only for a specific, expected case. Put the reason in a cell comment or the next column, e.g. "N/A expected: ticker not yet in vendor file; shows blank until listed". Even then, return a visible flag ("MISSING") rather than 0 where a 0 would flow into a sum. Use IFNA in preference to IFERROR so that other errors still surface.
- Guard division explicitly when a zero denominator is legitimate (`=IF(B2=0,"",A2/B2)`), and add a comment saying why it can be zero.

Number formats: thousands separators on large numbers, a stated decimal precision, percentages formatted as %, negatives in brackets or with a minus sign used consistently, and dates as yyyy-mm-dd unless the file already uses another style.

## 4. Before delivery: mandatory QA

1. Save the deliverable. Recalculate a **copy** in Excel (COM: open with macros disabled and `UpdateLinks=0`, `app.CalculateFull()`, save, close; see `references/excel-com.md`). If your environment provides a workbook review or recalculation tool, use it instead.
2. Read the recalculated copy with `load_workbook(copy, data_only=True)` and scan every cell for #REF!, #DIV/0!, #VALUE!, #N/A, #NAME?, #NUM! and #NULL!. The required result is zero error cells.
3. Check the task's own numbers: key totals against values known independently (from source data, a hand calculation or the brief), sum-of-parts ties, and the unit labels on the main inputs and outputs. Derive these checks from the task, not to make the file pass.
4. If the file has external links or data connections, don't refresh them. Say that the affected numbers were not recalculated.
5. Fix and rerun until clean. Rerun after any change.
6. Report what was built or changed, the path, the check results and anything unverified. If a checked value was wrong, say whether the fault was in the model or in the expectation.

## Quick openpyxl patterns

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.workbook.defined_name import DefinedName
INPUT = dict(font=Font(color="0000FF"), fill=PatternFill("solid", fgColor="FFF2CC"))
wb = Workbook(); inp = wb.active; inp.title = "Inputs"
inp.append(["Parameter", "Value", "Unit"])
inp.append(["Notional", 10_000_000, "USD"]); inp.append(["Spread", 35, "bp"]); inp.append(["Day count", 360, "days"])
inp.append(["bp per unit", 10_000, "bp"])  # conversion lives in Inputs too, not in the formula
for r in range(2, 6):
    inp[f"B{r}"].font, inp[f"B{r}"].fill = INPUT["font"], INPUT["fill"]
wb.defined_names["Notional"] = DefinedName("Notional", attr_text="Inputs!$B$2")
calc = wb.create_sheet("Calc")
calc["A1"], calc["B1"], calc["C1"] = "Daily accrual", "=Notional*Inputs!B3/Inputs!B5/Inputs!B4", "USD"
```

## References

- `references/excel-com.md`: editing through Excel COM (pywin32), safely and without running macros.
- `references/restructuring.md`: `xlsx_restructure.py` usage, what it shifts, and its limits.
- `THIRD_PARTY_NOTICES.md`: sources and licences.
