# X7I R2 — FIX WORD HEADING STRUCTURE AND COMPLETE REAL 44-PAGE VISUAL QA

Status: AUTHORIZED BOUNDED CORRECTION
Date: 2026-10-07
Branch: `feature/x7i-ch2-ch3-docx-review-r1`
R1 candidate: `e35c590dd3d2b0938e36d63a3fe91f0753310002`
External review: `work/do-an/X7I_CH2_CH3_DOCX_EXTERNAL_REVIEW_R1.md`

## 0. Scope

Correct only the X7I R1 document-structure and QA defects identified by the independent reviewer.

Do not change approved Chapter 2 or Chapter 3 wording.

## 1. Fix true Word heading styles for Chapter 3

Update the deterministic builder so that Chapter 3 heading paragraphs are real Word headings, not only visually formatted Normal paragraphs.

Required:
- Chapter 3 chapter title → Heading 1 / outline level 0;
- Chapter 3 H2 → Heading 2 / outline level 1;
- Chapter 3 H3 → Heading 3 / outline level 2.

Preserve the current visible formatting exactly:
- H1: 16 pt bold uppercase centered;
- H2: 14 pt bold;
- H3: 13 pt bold italic.

Do not rename any heading.
Do not modify Chapter 2.

After rebuilding, audit paragraph styles/outline levels from the DOCX itself, not by text regex alone.

Expected full combined hierarchy:
- H1 = 2;
- H2 = 14;
- H3 = 30.

## 2. Perform a genuine complete visual inspection

Rebuild the DOCX after the heading-style fix.

Render the final candidate to PDF and then one PNG per page.

You must actually open and inspect every rendered page, sequentially:
- page 01;
- page 02;
- ...
- page 44, or every page of the final render if pagination changes.

The prior R1 trace only demonstrated explicit viewing of 12 pages. R2 must not repeat that gap.

For every final page, record:
- page number;
- main content/section;
- PASS or FIXED;
- any defect found;
- if fixed, what layout-only change was made.

Do not claim “all pages visually inspected” unless all final page images were actually opened/inspected.

If a fix changes pagination, regenerate page images and repeat inspection for the resulting final page set.

## 3. Mandatory visual checks per page

Check:
- text clipping/overlap;
- table overflow;
- row/cell splitting defects;
- header-row repetition;
- orphan headings;
- figure/caption separation;
- image readability;
- missing glyphs/font substitution;
- blank pages;
- margin consistency;
- Chapter 2→3 page break;
- footer/page-number consistency.

## 4. Verify actual DOCX margins

Programmatically verify the final document section dimensions:

- A4 portrait;
- top = 3.5 cm;
- bottom = 3.0 cm;
- left = 3.5 cm;
- right = 2.0 cm.

Correct the R1 executor/handoff wording that accidentally swapped top/bottom values.

Do not alter margins if the actual DOCX is already correct.

## 5. Preserve content locks

Source blobs must remain unchanged:

- Chapter 2:
  `55ffb13acb3398c7ab29d6d5abbb369e5d26f3d0`
- Chapter 3:
  `40d2a895bc970f88d7260b3138b8a701f5eb0a8c`

Preserve:
- Bảng 2.1–2.4;
- Bảng 3.1–3.7;
- Hình 2.1–2.2;
- Hình 3.1–3.11;
- all technical truth locks.

No new Bảng 3.8 / Hình 3.12.

## 6. Chapter 2 regression guard

Chapter 2 must remain visually equivalent to the approved reference.

If the rebuild changes any of the first 12 pages, investigate and restore the reference layout unless the difference is strictly a benign metadata/style-structure change with zero visible effect.

Record the result.

## 7. Required R2 outputs

Update:
1. `work/do-an/output/CHAPTER_2_3_REVIEW.docx`
2. `work/do-an/output/CHAPTER_2_3_REVIEW_DOCX_QA.md`
3. `work/do-an/scripts/build_ch2_ch3_docx.py`
4. `work/do-an/X7I_CH2_CH3_DOCX_EXECUTOR_HANDOFF_R1.md`
5. `work/do-an/PROJECT_STATE.md` only as needed to record the R2 ready-for-review state.

The QA report must truthfully distinguish automated checks from human/visual page inspection.

## 8. Automated QA

Rerun:
- DOCX open/parse check;
- heading-style/outline-level audit;
- heading text/count audit;
- table/figure count audit;
- margin audit;
- technical forbidden/required phrase gates;
- Office/OpenXML validation available in the environment;
- project validation;
- unit tests;
- `git diff --check`.

Automated checks do not replace the full page-image inspection.

## 9. Stopping rule

The only allowed completion state is:

`X7I_R2_READY_FOR_INDEPENDENT_REVIEW`

Do not:
- open X7J;
- edit Chapter 2/3 content;
- add Chapter 1/4;
- declare final combined-document PASS yourself.

Commit, push, return the full R2 execution report, then STOP.
