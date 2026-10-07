# X7I CHAPTER 2+3 REVIEW DOCX — EXTERNAL REVIEW R2

Date: 2026-10-07  
Branch: `feature/x7i-ch2-ch3-docx-review-r1`  
Executor R2 candidate: `86d4766812d845ad011772cd05d2929893920934`

Verdict: **REVISE_BLOCKING**  
Score: **94/100**

## 1. What R2 successfully fixed

Independent verification confirms:

- current branch HEAD exactly equals `86d4766812d845ad011772cd05d2929893920934`;
- locked Chapter 2 source blob remains:
  `55ffb13acb3398c7ab29d6d5abbb369e5d26f3d0`;
- locked Chapter 3 source blob remains:
  `40d2a895bc970f88d7260b3138b8a701f5eb0a8c`;
- the executor trace now shows explicit page-image view operations for every page from page 01 through page 44;
- the builder now uses true Word `Heading 1`, `Heading 2`, and `Heading 3` paragraph styles and performs style-count assertions;
- the approved margin metadata is corrected to:
  - top 3.5 cm;
  - bottom 3.0 cm;
  - left 3.5 cm;
  - right 2.0 cm;
- no Chapter 2 or Chapter 3 Markdown content source was modified.

Thus both original R1 blockers were addressed in principle.

## 2. New blocking issue — the committed DOCX is not the exact DOCX that was rendered and visually inspected

The R2 execution sequence matters.

The trace shows:

1. build combined DOCX;
2. render it and produce page images;
3. explicitly open page 01 through page 44;
4. calculate the then-current DOCX SHA-256 as:
   `9853347a66ed0d23a788f0f09f42edfac7cb9beb70d8864736f88b4e6d1145d2`;
5. later run `build_ch2_ch3_docx.py` again;
6. later run the builder a second additional time;
7. finally stage and commit the regenerated DOCX.

Therefore the file that was committed was generated **after** the complete visual inspection.

This breaks the required artifact chain:

`final DOCX -> render -> inspect every page -> commit that exact DOCX`.

## 3. Independent hash verification of the committed binary

The reviewer fetched the actual committed file:

`work/do-an/output/CHAPTER_2_3_REVIEW.docx`

from the current R2 branch and independently decoded and SHA-256 hashed the committed bytes.

Committed file:
- size: **761,414 bytes**
- Git blob: `ee5b7968fae6f8439d549187159019566536287b`
- actual SHA-256:
  `c883320257d9625fd38671d7a7cc156d9f92c84706c4c61785ef919db028faca`

R2 QA report claims:
`9853347a66ed0d23a788f0f09f42edfac7cb9beb70d8864736f88b4e6d1145d2`

These hashes do **not** match.

The identical file size does not resolve the issue; DOCX is a ZIP-based binary and a later rebuild can alter package bytes and potentially document state.

This does not prove that the final committed file has a visual defect. It proves that the current visual QA report is not attached to the exact committed artifact.

## 4. Why this remains blocking

X7I's purpose is not merely to show that one temporary build looked correct.

It must prove that the **exact Word file handed to the user**:
- is the file that was rendered;
- is the file whose 44 final pages were inspected;
- has the SHA-256 recorded in QA;
- is the file committed to the branch.

Because the final committed binary differs from the inspected/hash-recorded binary, X7I cannot receive final PASS yet.

## 5. Required R3 correction

No content or layout redesign is requested.

Perform one final artifact-freeze pass:

1. run the builder once to produce the final DOCX;
2. immediately compute its SHA-256;
3. render that exact file to PDF/page PNGs;
4. inspect every final page;
5. do **not** run the DOCX builder again after that render;
6. update QA/handoff reports only;
7. commit the exact inspected DOCX;
8. extract the DOCX back from Git at the committed revision and independently compute its SHA-256;
9. assert that:
   `working-file hash == rendered-file hash == QA-report hash == committed-file hash`;
10. if any hash differs, do not PASS.

If the final DOCX page count remains 44 and the layout has not changed, inspect all 44 final pages again because the artifact itself is newly frozen.

## 6. Scope lock

Do not:
- rewrite Chapter 2;
- rewrite Chapter 3;
- alter headings/tables/figures;
- change the now-correct Word heading styles;
- change margins unless a real defect is found;
- add Chapter 1 or Chapter 4;
- open X7J.

The current heading-style and margin corrections should be preserved exactly.

## 7. Gate

Current verdict:

`X7I_R2_REVISE_BLOCKING`

X7J remains BLOCKED.

The only authorized next completion state is:

`X7I_R3_READY_FOR_INDEPENDENT_REVIEW`
