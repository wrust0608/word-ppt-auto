# X7I R3 — FREEZE THE EXACT INSPECTED DOCX

Status: AUTHORIZED BOUNDED CORRECTION
Date: 2026-10-07
Branch: `feature/x7i-ch2-ch3-docx-review-r1`
R2 candidate: `86d4766812d845ad011772cd05d2929893920934`
External review: `work/do-an/X7I_CH2_CH3_DOCX_EXTERNAL_REVIEW_R2.md`

## Objective

Fix only the broken final-artifact proof chain.

R2 correctly fixed Word heading styles and performed a 44-page inspection, but the DOCX was rebuilt again after that inspection. The committed binary therefore does not match the SHA-256 recorded in the R2 QA report.

Do not change report content or intended layout.

## Mandatory sequence

### A. Freeze one final DOCX

1. Verify locked sources remain:
   - Chapter 2 blob:
     `55ffb13acb3398c7ab29d6d5abbb369e5d26f3d0`
   - Chapter 3 blob:
     `40d2a895bc970f88d7260b3138b8a701f5eb0a8c`

2. Run exactly one final build:
   `uv run python work/do-an/scripts/build_ch2_ch3_docx.py`

3. Immediately compute SHA-256 of:
   `work/do-an/output/CHAPTER_2_3_REVIEW.docx`

Call this value `FINAL_DOCX_SHA256`.

### B. Render that exact file

4. Render the exact just-hashed DOCX to PDF.
5. Render every PDF page to PNG.
6. Open and inspect every final page sequentially from page 01 through the final page.
7. Record page-by-page PASS/FIXED.

If a visual defect requires a DOCX/layout fix:
- make the layout-only fix;
- rebuild;
- compute a new hash;
- discard the previous render;
- rerender and reinspect the entire final page set;
- the new hash becomes `FINAL_DOCX_SHA256`.

### C. Freeze after successful inspection

After the final page inspection passes:

**DO NOT RUN THE DOCX BUILDER AGAIN.**

Do not resave the DOCX through Word, python-docx, LibreOffice or another tool after the inspected render unless you are prepared to repeat hashing + full render + full inspection.

Update only:
- `work/do-an/output/CHAPTER_2_3_REVIEW_DOCX_QA.md`
- `work/do-an/X7I_CH2_CH3_DOCX_EXECUTOR_HANDOFF_R1.md`
- `work/do-an/PROJECT_STATE.md`

Record `FINAL_DOCX_SHA256` exactly.

### D. Commit and verify the committed artifact

Commit the final artifacts.

Then verify the exact committed DOCX bytes, for example:

```powershell
git show HEAD:work/do-an/output/CHAPTER_2_3_REVIEW.docx > scratch/committed.docx
```

Use a binary-safe extraction method appropriate for the shell/environment if PowerShell redirection is not binary-safe.

Compute SHA-256 of the extracted committed DOCX.

Required assertion:

`SHA256(committed DOCX) == FINAL_DOCX_SHA256`

Also verify:
- committed file size matches the QA report;
- Git status is clean;
- branch HEAD is pushed to origin.

Do not rebuild after this verification.

## Preserve R2 fixes

Keep:
- real Heading 1/2/3 Word styles;
- full combined heading hierarchy;
- margins 3.5 / 3.0 / 3.5 / 2.0 cm;
- Chapter 2 visual regression guard;
- Chapter 3 layout;
- 11 tables;
- 13 figures;
- all technical truth locks.

No content edit is authorized.

## QA report truth requirement

The final QA report must state:
- final committed DOCX SHA-256;
- final size;
- final page count;
- exact render method;
- that the rendered/inspected DOCX hash equals the committed DOCX hash;
- page-by-page inspection results.

Do not reuse the stale R2 hash
`9853347a66ed0d23a788f0f09f42edfac7cb9beb70d8864736f88b4e6d1145d2`
unless the newly frozen final file independently hashes to that value.

## Automated checks

After the final artifact is frozen, run non-mutating checks only:
- parse/open DOCX;
- heading style/count audit;
- margin audit;
- table/figure audit;
- technical truth gates;
- unit tests;
- project validation;
- `git diff --check`.

Any command that rewrites the DOCX invalidates the render proof and requires a new render/inspection cycle.

## Stop state

The only allowed completion state is:

`X7I_R3_READY_FOR_INDEPENDENT_REVIEW`

Do not open X7J.
Do not edit Chapter 2/3 content.
Commit, push, report the exact final hash chain, then STOP.
