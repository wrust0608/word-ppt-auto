# X7G R2 — BOUNDED CORRECTION OF COMPLETE CHAPTER 3 ASSEMBLY

Status: AUTHORIZED CORRECTION ONLY
Date: 2026-10-07
Branch: `feature/x7g-ch3-assembly-approved-r1`
R1 candidate: `31822eb71981faffcfe433791caed9b65045c501`
Review: `work/do-an/X7G_CH3_ASSEMBLY_EXTERNAL_REVIEW_R1.md`

## Scope

Correct only the two minor assembly defects identified by the independent reviewer.

Do not reopen or edit any approved source-section file.

## Required edits in CHAPTER_3_DRAFT_R1.md

### 1. Normalize canonical H2 titles

Replace:

`## 3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE`

with:

`## 3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010`

Replace:

`## 3.4. Kết quả Case B — Vô hiệu hóa SMBv1 và đo lại từ xa`

with:

`## 3.4. Kết quả Case B — Vô hiệu hóa SMBv1`

These are whole-chapter heading normalizations required by the canonical contract. Do not change the source section files.

### 2. Remove internal citation marker

Remove exactly the internal HTML comment containing:

`CITE-ANCHOR: S005, S032; final IEEE numbering deferred to global normalization gate`

Do not change the surrounding prose.

## Forbidden

Do not:
- edit any other prose;
- alter technical claims;
- add/delete evidence;
- add/delete tables or figures;
- change numbering;
- create Bảng 3.8 or Hình 3.12;
- edit Chapter 2;
- create DOCX/PDF;
- open X7H.

## Verification

After the edits, independently verify:

- H1 = 1;
- H2 = 7 and all H2 titles match `CHAPTER_3_CONTRACT.md`;
- H3 = 10;
- Bảng 3.1–3.7 remain present and ordered;
- Hình 3.1–3.11 remain present and ordered;
- no Bảng 3.8 / Hình 3.12;
- `CITE-ANCHOR` count = 0;
- no other internal workflow/governance marker in student-facing chapter;
- all technical locks remain unchanged;
- all six approved source files themselves are byte/blob unchanged;
- the only content diff in `CHAPTER_3_DRAFT_R1.md` is the two H2 title normalizations plus removal of the one HTML comment.

Rerun:
- unit tests;
- Vietnamese academic linter;
- `git diff --check`;
- project validation if available.

Update:
- `X7G_CH3_ASSEMBLY_SELF_REVIEW_R1.md` to document R2;
- `X7G_CH3_ASSEMBLY_EXECUTOR_HANDOFF_R1.md` with the R2 commit and verification.

## Stop state

The only allowed completion state is:

`X7G_R2_READY_FOR_INDEPENDENT_REVIEW`

Commit and push the bounded correction, report the exact diff and QA results, then STOP.

Do not authorize X7H.
