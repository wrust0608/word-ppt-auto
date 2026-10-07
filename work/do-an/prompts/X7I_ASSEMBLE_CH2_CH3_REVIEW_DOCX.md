# X7I — ASSEMBLE LOCKED CHAPTER 2 + LOCKED CHAPTER 3 INTO REVIEW DOCX

Status: AUTHORIZED
Date: 2026-10-07
Branch: `feature/x7i-ch2-ch3-docx-review-r1`
Base integration HEAD: `636e2c01d8dae0e5202f2d5c08b565f1ef8dfd2f`

## 0. Mandatory global checkpoint

Before editing or generating anything, read and obey:

1. `work/do-an/ROADMAP_CURRENT_CH2_CH3_2026_10_07.md`
2. `work/do-an/PROJECT_STATE.md`
3. `work/do-an/X7H_CH3_WHOLE_USER_APPROVAL_LOCK.md`
4. `work/do-an/CHAPTER_2.md`
5. `work/do-an/CHAPTER_3_DRAFT_R2.md`
6. `work/do-an/output/CHAPTER_2_FINAL_DOCX_QA.md`
7. `work/do-an/INSTITUTION_PROFILE.md`
8. current Chapter 2 / Chapter 3 contracts and numbering locks.

Do not use historical WR1/WR2 Word snapshots, abandoned Chapter 1 enrichment, premature X7G/X7H branches, or any older report DOCX as content authority.

Current gate is X7I only.

## 1. Locked content sources

The only content sources for this combined review document are:

### Chapter 2
`work/do-an/CHAPTER_2.md`

Expected Git blob:
`55ffb13acb3398c7ab29d6d5abbb369e5d26f3d0`

Status:
`USER APPROVED / CONTENT_LOCKED / FINAL_DOCX_PASS`

### Chapter 3
`work/do-an/CHAPTER_3_DRAFT_R2.md`

Expected Git blob:
`40d2a895bc970f88d7260b3138b8a701f5eb0a8c`

Status:
`USER APPROVED / CONTENT_LOCKED / X7H_FINAL_PASS`

If either blob/content source differs unexpectedly from the authorized branch state, STOP and report the drift before building the DOCX.

## 2. Visual/style reference

Use the already approved Chapter 2 Word file as the formatting reference:

`work/do-an/output/CHAPTER_2_FINAL.docx`

Its final QA record is:

`work/do-an/output/CHAPTER_2_FINAL_DOCX_QA.md`

Recorded SHA-256 from the approved QA:
`03adb6c44bc7c336b8c1be99f4e87c2ad93d0f11fe7d16603d5eb8dc102a7042`

Recorded Chapter 2 reference layout:
- 12 pages;
- A4 portrait;
- top 3.5 cm;
- bottom 3.0 cm;
- left 3.5 cm;
- right 2.0 cm;
- Times New Roman 13 pt body;
- 1.5 line spacing;
- justified body;
- first-line indent 1.0 cm;
- H1 16 pt bold uppercase;
- H2 14 pt bold;
- H3 13 pt bold italic;
- table title above;
- figure caption below;
- no blank pages;
- every page visually inspected.

Verify the actual local reference file hash before relying on it. If it does not match the approved QA hash, report the discrepancy and do not silently substitute another historical DOCX.

The approved Markdown remains the content authority. The Chapter 2 DOCX is a layout/style reference, not permission to reintroduce stale content.

## 3. Objective

Create one review Word document containing:

1. locked Chapter 2;
2. page break;
3. locked Chapter 3.

Output:

`work/do-an/output/CHAPTER_2_3_REVIEW.docx`

This is a Chapters 2+3 review product only.

Do NOT add:
- cover page;
- front matter;
- Chapter 1;
- Chapter 4;
- report-wide conclusion;
- bibliography invented for this review;
- slides/defense content.

## 4. No-content-rewrite rule

X7I is formatting/assembly only.

Do not rewrite, shorten, expand, paraphrase, “improve”, translate or reinterpret any Chapter 2 or Chapter 3 prose.

Allowed transformations are presentation-only:
- apply Word styles;
- remove Markdown syntax while preserving visible text;
- render inline code/commands appropriately;
- convert Markdown tables into Word tables;
- embed the already approved images;
- apply page/section breaks;
- wrap text inside cells/command blocks without changing words;
- apply caption formatting;
- apply keep-with-next / keep-together / repeat-header-row / row-no-split behavior.

If clean layout appears to require changing the actual wording or a technical fact, do not make that edit. Record it as a blocker for independent review.

## 5. Required combined structure

The combined DOCX must contain exactly:

### Chapter titles
- `CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM`
- `CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH`

Chapter 3 must start on a new page.

### Heading counts
- H1: exactly 2;
- H2: exactly 14 total;
  - Chapter 2: 7;
  - Chapter 3: 7;
- H3: exactly 30 total;
  - Chapter 2: 20;
  - Chapter 3: 10.

Do not renumber or rename any locked heading.

## 6. Tables and figures

### Chapter 2
Preserve:
- Bảng 2.1–2.4;
- Hình 2.1–2.2.

### Chapter 3
Preserve:
- Bảng 3.1–3.7;
- Hình 3.1–3.11.

Combined expected:
- 11 report tables total;
- 13 report figures total.

Forbidden:
- Bảng 3.8;
- Hình 3.12;
- any new numbered table/figure.

### Table formatting
- table title above table;
- title centered and bold;
- Times New Roman;
- header row bold;
- repeat header row when a table continues across pages;
- prevent row splitting where practical;
- do not shrink the entire document to fit a wide table;
- use sensible column widths and wrapping;
- if a table must span pages, preserve one table and repeat its header rather than inventing a second table number;
- Bảng 3.7 must remain readable in portrait A4.

### Figure formatting
- use the already approved image files referenced by the locked Markdown;
- no recropping or evidence alteration in X7I;
- preserve aspect ratio;
- center figures;
- figure caption below, centered and bold, consistent with Chapter 2 final style;
- ensure screenshot text remains readable at normal page zoom.

Do not leave Markdown image syntax in the DOCX.

## 7. Code/commands

For command blocks:
- preserve exact command text;
- use the existing Chapter 2 final style as reference;
- monospace font such as Consolas 9.5 pt is acceptable;
- preserve gray/background treatment if used by the approved Chapter 2 final style;
- no command rewriting.

Do not introduce:
- `-Pn`;
- new `--privileged` operator commands;
- changed output filenames;
- changed Case B/Case C command syntax.

## 8. Citations and internal markers

Preserve visible citations exactly as present in the locked Markdown sources.

Do not:
- invent new citation numbers;
- renumber citations;
- invent bibliography entries;
- insert internal Evidence IDs;
- insert `CITE-ANCHOR`;
- insert X7/QA/governance markers;
- insert Markdown comments.

If citation normalization would require changing locked content, report it for later review instead of silently changing it.

## 9. Chapter 2 regression guard

The first 12 pages of the approved Chapter 2 reference already passed full visual QA.

During combined assembly:
- Chapter 2 text/content must remain equivalent to locked `CHAPTER_2.md`;
- Chapter 2 layout should remain visually consistent with `CHAPTER_2_FINAL.docx`;
- adding Chapter 3 must not damage or reflow Chapter 2 unnecessarily.

Render the approved Chapter 2 reference and the combined DOCX.

Compare the Chapter 2 portion page-by-page against the approved reference:
- headings;
- tables;
- figures;
- code blocks;
- page breaks;
- text clipping;
- spacing;
- margins.

If page numbering/footer behavior legitimately differs because of combined-document assembly, document that difference explicitly. Do not accept other unexplained visual regression.

## 10. Mandatory render-and-inspect loop

A successful DOCX write/open or OOXML validation is NOT enough.

Required loop:

1. build the combined DOCX;
2. render DOCX -> PDF for QA;
3. render PDF/DOCX output -> one PNG per page;
4. inspect **every page at 100%/normal zoom**;
5. fix any visual defect;
6. render again after every layout-sensitive correction;
7. repeat until all pages PASS.

The internal PDF and page PNGs are QA intermediates only. Do not commit/deliver them unless specifically needed for debugging.

Check every page for:
- clipped text;
- overlapping objects;
- broken table wrapping;
- cells outside margins;
- split captions;
- heading orphan/widow problems;
- figures separated from captions;
- unreadable screenshots;
- font substitution;
- missing glyphs;
- accidental blank pages;
- inconsistent margins;
- broken Chapter 2 -> Chapter 3 page break.

## 11. Word styles/layout rules

Use HUIT/current approved Chapter 2 format:

- A4 portrait, one-sided;
- margins: 3.5 / 3.0 / 3.5 / 2.0 cm (top/bottom/left/right);
- Times New Roman 13 pt body;
- line spacing 1.5;
- body justified;
- first-line indent approximately 1.0 cm for ordinary prose;
- Heading 1: 16 pt, bold, uppercase, centered;
- Heading 2: 14 pt, bold;
- Heading 3: 13 pt, bold italic;
- no decorative header/footer;
- preserve approved page-number behavior unless a combined-document requirement forces a documented change;
- no manual empty-paragraph padding to force pages.

Use proper Word paragraph styles rather than plain bold text where practical.

Set `keep_with_next` for headings/captions as needed.

## 12. Mandatory structural/content audits

Before final commit verify:

### Structure
- H1 = 2;
- H2 = 14;
- H3 = 30;
- tables = 11;
- figures = 13;
- Chapter 3 begins on a new page;
- no Chapter 1/4/front matter added.

### Chapter 2
- exact locked heading order;
- Bảng 2.1–2.4;
- Hình 2.1–2.2;
- no legacy chapter structure;
- no content rewrite.

### Chapter 3
- exact locked heading order;
- Bảng 3.1–3.7;
- Hình 3.1–3.11;
- no Bảng 3.8/Hình 3.12;
- no internal workflow markers;
- no content rewrite.

### Technical gates
Preserve at minimum:
- `445 OPEN != vulnerable`;
- `SMBv1 enabled != MS17-010 confirmed`;
- `SMBv1 disabled != PATCHED`;
- `FILTERED != PATCHED`;
- `UNKNOWN != SAFE`;
- no canonical exploitation/RCE/reverse shell/Meterpreter;
- no completed Case A patch experiment.

## 13. Required outputs

Create:

1. `work/do-an/output/CHAPTER_2_3_REVIEW.docx`
2. `work/do-an/output/CHAPTER_2_3_REVIEW_DOCX_QA.md`
3. `work/do-an/X7I_CH2_CH3_DOCX_EXECUTOR_HANDOFF_R1.md`

You may create/reuse a deterministic DOCX build script if needed. If a new persistent script is introduced, document why and keep it narrowly scoped to this approved assembly task.

### QA report must include
- final DOCX SHA-256;
- final file size;
- final page count;
- render method;
- confirmation every page was inspected;
- page-by-page PASS/fix log;
- Chapter 2 reference comparison result;
- heading/table/figure counts;
- image readability result;
- table overflow result;
- blank-page result;
- margin/font/spacing audit;
- source Markdown blob SHAs;
- any unavoidable formatting-only deviation and justification.

### Executor handoff must include
- branch;
- base integration SHA;
- final candidate commit;
- output paths;
- exact build commands/scripts;
- DOCX SHA-256;
- page count;
- structural audit;
- content-drift audit;
- visual QA summary;
- tests/validation;
- clean git status.

## 14. Project QA

Run:
- repository unit tests;
- project validation;
- `git diff --check`;
- any existing DOCX structural/heading/image audit used by the project.

Do not consider automated QA a substitute for page-by-page visual inspection.

## 15. Gate and stopping rule

The only allowed completion state is:

`X7I_DOCX_READY_FOR_INDEPENDENT_REVIEW`

Do NOT:
- declare X7I final PASS yourself;
- open X7J;
- edit Chapter 2/3 content;
- create Chapter 4;
- expand to a full thesis;
- create slides/defense artifacts.

Commit and push the required X7I artifacts, return the execution report, then STOP.
