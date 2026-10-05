# Editing through Excel COM (pywin32)

Use this for any workbook containing charts, images, pivots, slicers, form controls, VBA (.xlsm) or .xlsb, or whenever fidelity matters more than speed. Excel itself does the save, so nothing is dropped.

## Safe session

```python
import shutil, pythoncom, win32com.client
src = r"C:\work\Their_Model.xlsx"
dst = r"C:\work\Their_Model_edited.xlsx"   # never the original unless the user says so
shutil.copy2(src, dst)

pythoncom.CoInitialize()
app = wb = None
try:
    app = win32com.client.DispatchEx("Excel.Application")  # private instance, not the user's open Excel
    app.Visible = False
    app.DisplayAlerts = False
    app.AskToUpdateLinks = False
    app.AutomationSecurity = 3            # msoAutomationSecurityForceDisable: macros never run
    app.ScreenUpdating = False
    wb = app.Workbooks.Open(dst, UpdateLinks=0, ReadOnly=False)
    ws = wb.Worksheets("Calc")

    ws.Rows(5).Insert()                   # Excel shifts every reference, name, chart range
    ws.Range("B5").Formula = "=SUM(B6:B9)"    # write formulas with .Formula (English, commas)
    ws.Range("A5").Value = "Subtotal"
    ws.Range("B6").NumberFormat = "#,##0.00"

    app.CalculateFull()
    wb.Save()                             # keeps the original file format
finally:
    if wb is not None:
        wb.Close(SaveChanges=False)
    if app is not None:
        app.Quit()
    pythoncom.CoUninitialize()
```

Rules:
- Always use `DispatchEx`, not `Dispatch`. Dispatch can attach to the user's own open Excel and close their work.
- Always use `try/finally` with `Quit()`. A crashed script leaves an invisible EXCEL.EXE. Check with `Get-Process EXCEL` and stop only the instances the script started. If the user might have Excel open, ask before killing anything.
- To save under a new name or format, use `wb.SaveAs(path, FileFormat)`: 51 for .xlsx, 52 for .xlsm, 50 for .xlsb. Never save an .xlsm as 51, because that strips the macros.
- Large files can take minutes. If your shell has a command timeout, launch the script detached and poll it.
- Read values back with `ws.Range("B5").Value` after calculating. For bulk reads use `ws.Range("A1:Z500").Value`, which returns a tuple of rows. Don't loop cell by cell, because every COM call has a cost.
- Use `ws.Range(...).Formula2` for dynamic-array formulas only if the Excel build supports them.
- Copying a sheet: `ws.Copy(After=wb.Worksheets(wb.Worksheets.Count))`.
- Don't refresh external data connections or pivot caches unless asked. That can reach network sources.

Afterwards, run the QA in SKILL.md section 4 on `dst`.
