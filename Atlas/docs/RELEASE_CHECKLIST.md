# Release Checklist

**Status:** Experimental  
**Version:** 1.0.0  
**Owner:** Atlas Studio  
**Review date:** 2026-10-07  
**Change history:** 1.0.0 - Added Atlas v1 release checklist.

## Purpose

Use this checklist before approving an Atlas release on `master`.

## Checklist

1. Run `.\.venv\Scripts\python.exe -m pytest -v`.
2. Run `.\.venv\Scripts\python.exe .\tools\build_workbook.py`.
3. Confirm `Atlas/excel/Atlas_Business_OS_v1.0.0.xlsx` opens in local Excel.
4. Export workbook sheets for review and confirm no broken formulas or clipped critical headers.
5. Run `.\.venv\Scripts\python.exe .\tools\release_audit.py`.
6. Review warnings and confirm every accepted warning is documented.
7. Confirm evidence dates and confidence levels still reflect reality.
8. Confirm `Atlas/docs/VERIFICATION_REPORT.md` matches the latest audit and test state.
9. Review `git status --short` and `git diff --check`.
10. Commit only planned Atlas release files.

## Approval rules

- Any schema mismatch, broken internal link, missing prompt, missing evidence reference, or workbook contract failure blocks release.
- Low-confidence hypotheses may ship only as documented warnings, not hidden assumptions.
- Workbook regeneration must happen from source records, never manual cell edits.
