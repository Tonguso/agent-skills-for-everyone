# xlsx_restructure.py: reference-aware row and column insert and delete

Adapted from Hermes (MIT, Nous Research, commit 79af3f6). Use it for openpyxl-only workbooks, usually ones you built. For anyone else's file, or anything with charts or pivots, use Excel COM (`references/excel-com.md`).

```
python scripts\xlsx_restructure.py book.xlsx --sheet Data --insert-rows 4        # 1 row before row 4
python scripts\xlsx_restructure.py book.xlsx --sheet Data --delete-rows 5:2      # rows 5-6
python scripts\xlsx_restructure.py book.xlsx --sheet Data --insert-cols B:1 --out new.xlsx
```

One operation per run. It prints a JSON report of every rewrite.

Safety (changes from upstream):
- The default output is `<name>_restructured.xlsx` beside the input. The input is never overwritten unless you pass `--in-place`. An existing `--out` file is refused unless you pass `--overwrite`.
- It refuses .xlsm files, and any file containing charts, drawings or images, pivots, slicers, timelines, VBA, form or ActiveX controls, or a data model, because openpyxl would lose them on save. `--allow-lossy` overrides this. Use it only on a throwaway copy and say so.

What it rewrites:
- A1 references in every sheet's formulas: relative, absolute, ranges and sheet-qualified (`'My Sheet'!A1`). String literals are left alone. References into a deleted region become `#REF!`, so check the report.
- Merged ranges (expanded if they span the insertion point), autofilter, freeze panes, data-validation and conditional-format ranges, table refs on the edited sheet, workbook and sheet-scoped defined names, row heights and column widths.

What it does not handle (check these by hand):
- Whole-row references such as `3:5` (whole-column `A:A` needs no change for row inserts, but column inserts don't shift it either).
- Conditional-format rule formulas, chart series, images and shapes (the file is refused anyway unless --allow-lossy).
- Array or shared formulas stored as objects rather than text, structured table references (`Table1[Col]`), INDIRECT and OFFSET text addresses, and external-workbook references.
- Tables on other sheets that point at the edited sheet.

Test evidence (2026-10-05): we built a workbook with two sheets, cross-sheet formulas, absolute and quoted refs, a defined name (`Rate`), a string literal that looks like a reference, and merged cells above and across the insertion point, then inserted one row at Data!4. Every reference shifted as expected (`SUM(Data!A2:A6)` became `A2:A7`, `$A$4` became `$A$5`, `Rate` `$A$3:$A$5` became `$A$3:$A$6`, merge `C3:D5` became `C3:D6`, the literal was unchanged, the source file was untouched). Excel recalculated a copy: 6/6 value checks passed with zero error cells. The refusal paths for charts, an in-place target and an existing output were exercised and all refused.
