# WR1 — BUILD DEMO 1 WORD REVIEW SNAPSHOT

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/wr1-demo1-word-review-v2`  
Approved integration base: `1512bbe03935d8e2b989694f01e90583b0b89319`

## 0. Objective

Create a complete Word review snapshot for **Demo 1** so the user can read the work as a real formatted report before the project continues.

This is a publication/formatting checkpoint, not a content-authoring phase.

The DOCX must contain exactly:

1. the full approved Chapter 2;
2. Chapter 3 title;
3. approved Section 3.1;
4. approved Section 3.2.

Do **not** include:
- Section 3.3;
- Case B / Section 3.4;
- Case C;
- Sections 3.5–3.7;
- Chapter 4;
- placeholders for unfinished sections.

The user must be able to read the document as a coherent report snapshot through Demo 1.

## 1. Start and lineage

Run:

```bash
git fetch origin
git checkout feature/wr1-demo1-word-review-v2
git pull --ff-only origin feature/wr1-demo1-word-review-v2
git status --short
git rev-parse HEAD
git merge-base --is-ancestor 1512bbe03935d8e2b989694f01e90583b0b89319 HEAD
```

The last command must succeed.

If lineage is wrong, STOP.

## 2. Mandatory read order

Read:

1. `work/do-an/PROJECT_STATE.md`
2. `work/do-an/DEMO_WORD_REVIEW_WORKFLOW.md`
3. `work/do-an/AUTHOR_VOICE.md`
4. `.agents/skills/thesis-research-and-writing/references/docx-production.md`
5. `work/do-an/output/CHAPTER_2_FINAL_DOCX_QA.md`
6. `work/do-an/CHAPTER_2.md`
7. `work/do-an/CH3_31_BASELINE_DRAFT_R1.md`
8. `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md`
9. `work/do-an/X7A1_CH3_31_EXTERNAL_REVIEW_R2_FINAL.md`
10. `work/do-an/X7B1_CH3_32_EXTERNAL_REVIEW_R2_FINAL.md`
11. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`

Use the current approved Markdown/DOCX artifacts only.

Do not reopen technical claims.

## 3. Canonical content sources

### Chapter 2

Content source:
`work/do-an/CHAPTER_2.md`

Validated formatting baseline:
`work/do-an/output/CHAPTER_2_FINAL.docx`

Use the validated Chapter 2 DOCX as the preferred base/template so the already-reviewed Chapter 2 formatting is preserved.

Do not rewrite Chapter 2.

### Chapter 3 — Demo 1 result scope

Use exactly:

`work/do-an/CH3_31_BASELINE_DRAFT_R1.md`

and:

`work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md`

Insert before Section 3.1 the chapter title:

`CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH`

Do not add any later Chapter 3 sections.

## 4. Approved Chapter 3 presentation images

Use exactly these existing approved presentation files.

### Section 3.1
- `work/do-an/chapter3/presentation/3_1/Hinh_3_1_Network_SMB.png`
- `work/do-an/chapter3/presentation/3_1/Hinh_3_2_Firewall.png`
- `work/do-an/chapter3/presentation/3_1/Hinh_3_3_SrvSys_Hotfix.png`

### Section 3.2
- `work/do-an/chapter3/presentation/3_2/Hinh_3_4_SMB_Version.png`
- `work/do-an/chapter3/presentation/3_2/Hinh_3_5_SMB_NSE.png`

Do not regenerate, sharpen, annotate, recolor, recrop or replace these images.

Do not use raw evidence screenshots where an approved presentation image already exists.

## 5. Output files

Create:

`work/do-an/output/review/DEMO_1_CH2_CH3_31_32_REVIEW.docx`

and:

`work/do-an/output/review/DEMO_1_CH2_CH3_31_32_REVIEW_QA.md`

Create the `review/` directory if needed.

Do not overwrite:

`work/do-an/output/CHAPTER_2_FINAL.docx`

## 6. Review marker

This file is not the final submission.

Add a small first-page-only header:

`BẢN REVIEW — CHƯA PHẢI BẢN NỘP CUỐI — DEMO 1`

Formatting:
- Times New Roman;
- 8–9 pt;
- italic;
- centered;
- black or neutral gray only;
- inside the header area;
- do not alter the body margin or push Chapter 2 text down.

Use a different-first-page header if necessary so the marker appears only on page 1.

Do not add an invented university cover page.

Do not add decorative design.

## 7. Document structure

The document body must begin directly with Chapter 2 and continue into Chapter 3.

Expected body sequence:

```text
CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM
... approved Chapter 2 content ...

[page break]

CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH

3.1. Trạng thái baseline trước đo đạc
3.1.1. Trạng thái mạng và dịch vụ SMB
3.1.2. Trạng thái bản vá và mốc phục hồi

3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB
3.2.1. Khảo sát trạm mạng và trạng thái mở cổng dịch vụ SMB
3.2.2. Nhận diện phiên bản dịch vụ và đặc tính giao thức SMB
```

No empty 3.3 heading.

No “to be continued” text in the report body.

## 8. Expected structural counts

The final DOCX body must contain:

- chapter titles / Heading 1: **2**
- Heading 2:
  - Chapter 2 = 7
  - Chapter 3 snapshot = 2
  - total = **9**
- Heading 3:
  - Chapter 2 = 20
  - Chapter 3 snapshot = 4
  - total = **24**

Tables:
- Chapter 2 = Bảng 2.1–2.4 = 4
- Chapter 3 = Bảng 3.1–3.3 = 3
- total = **7 tables**

Figures:
- Chapter 2 = Hình 2.1–2.2 = 2
- Chapter 3 = Hình 3.1–3.5 = 5
- total = **7 figures**

If counts differ, STOP and fix before commit.

## 9. Formatting baseline

Preserve the validated HUIT-style formatting from Chapter 2:

- A4 portrait;
- one-sided layout;
- top margin = 3.5 cm;
- bottom margin = 3.0 cm;
- left margin = 3.5 cm;
- right margin = 2.0 cm;
- Times New Roman;
- body = 13 pt;
- body line spacing = 1.5;
- body = justified;
- first-line indent ≈ 1.0 cm;
- chapter heading = 16 pt bold uppercase;
- H2 = 14 pt bold;
- H3 = 13 pt bold italic;
- figure captions below figures;
- table titles above tables;
- captions/titles centered and bold according to the existing Chapter 2 baseline;
- command/code text = readable monospace;
- no decorative boxes/colors outside the already-established command style;
- no landscape pages unless an existing approved source already requires it — WR1 should normally remain portrait.

Do not reduce global font size to fit content.

## 10. Chapter 2 preservation gate

Because Chapter 2 already passed Word QA:

- prefer opening/copying `CHAPTER_2_FINAL.docx` as the starting document;
- do not alter Chapter 2 wording;
- do not renumber Chapter 2;
- do not replace Hình 2.1/Hình 2.2;
- do not change table content.

After appending Chapter 3, verify the Chapter 2 portion still contains:

- exact chapter title;
- 7 H2;
- 20 H3;
- Bảng 2.1–2.4;
- Hình 2.1–2.2;
- visible IEEE markers [1]–[11] exactly as already approved.

Do not regenerate Chapter 2 from an older draft.

## 11. Chapter 3 Markdown conversion rules

Convert the approved Markdown faithfully.

### Headings
Use real Word Heading styles.

### Tables
Convert Markdown tables into real Word tables.

For Bảng 3.1–3.3:
- title above table;
- bold header row;
- repeat header row if table crosses pages;
- do not split individual table rows across pages where practical;
- maintain readable cell widths;
- allow controlled wrapping;
- keep code-like values in monospace where useful;
- do not change wording to make a table fit.

### Figures
Insert the five approved PNGs.

- center images;
- preserve aspect ratio;
- scale to fit within the usable page width;
- do not exceed margins;
- caption directly below;
- keep caption with image;
- do not split image/caption across pages.

### Inline code
Render inline commands, filenames, IPs and code-like values legibly.

Do not expose Markdown backticks in the final Word body unless they are semantically part of a command block.

## 12. Citation-anchor discipline

Section 3.1 contains the internal Markdown comment:

`<!-- CITE-ANCHOR: S005, S032; final IEEE numbering deferred to global normalization gate -->`

This is an internal authoring anchor.

Do **not** render it into the DOCX.

Do not invent a visible IEEE number for it in WR1.

Record in the QA report:

`Chapter 3 global IEEE normalization remains deferred; internal CITE-ANCHOR comments are not published in the review DOCX.`

Preserve Chapter 2 visible citations exactly.

## 13. Content-drift gate

Before visual QA, programmatically audit the generated DOCX.

At minimum verify:

- expected heading counts and exact heading sequence;
- 7 tables;
- 7 figures/images used as report figures;
- Bảng 2.1–2.4 present;
- Bảng 3.1–3.3 present;
- Hình 2.1–2.2 captions present;
- Hình 3.1–3.5 captions present;
- Section 3.3 heading absent;
- Case B / Case C result headings absent;
- Chapter 4 absent;
- internal `CITE-ANCHOR` absent;
- internal `S1-C`, `S2-C`, Evidence IDs, governance/gate text absent;
- Markdown image syntax absent;
- raw Mermaid syntax absent.

Also compare extracted Chapter 3 text against the two approved Markdown sources.

Formatting-only changes are allowed.

Technical sentence changes are not.

## 14. Page break discipline

Insert a page break between the end of Chapter 2 and the Chapter 3 title.

Chapter 3 must start on a fresh page.

Do not create an empty page between chapters.

Use keep-with-next for:
- headings;
- table titles;
- figure captions.

Avoid:
- orphaned headings at page bottoms;
- captions separated from their figure/table;
- 1-line fragments from tables where practical.

## 15. Mandatory render-and-inspect QA

This is non-negotiable.

After building the DOCX:

1. render it to PDF;
2. render every PDF page to PNG;
3. visually inspect **100% of pages** at readable/100% zoom;
4. fix defects;
5. re-render after every layout-sensitive fix;
6. repeat until clean.

Do not call the file PASS based only on XML/schema checks.

Temporary render artifacts must stay outside committed report paths and be removed before final git commit unless needed for debugging.

## 16. Visual QA checklist

Inspect every page for:

- text clipping;
- overlap;
- broken Vietnamese glyphs;
- font substitution;
- table overflow;
- table rows split badly;
- over-wide command strings;
- figures too small to read;
- figures crossing margins;
- caption separation;
- headings orphaned at page bottom;
- excessive blank space;
- accidental blank pages;
- broken page break between Chapter 2 and 3;
- inconsistent body font/spacing;
- inconsistent caption/table-title styling;
- image distortion;
- internal authoring comments accidentally visible.

Also inspect whether Chapter 3 visually matches the already-approved Chapter 2 style.

## 17. QA report

Create:

`work/do-an/output/review/DEMO_1_CH2_CH3_31_32_REVIEW_QA.md`

Record:

### Provenance
- branch;
- starting SHA;
- source Markdown paths;
- source file SHA-256;
- Chapter 2 base DOCX SHA-256;
- output DOCX SHA-256.

### Structure
- actual page count;
- H1/H2/H3 counts;
- table count;
- figure count;
- exact table/figure numbering sequence.

### Content drift
- Chapter 2 preservation = PASS/FAIL;
- Chapter 3 3.1/3.2 source match = PASS/FAIL;
- internal CITE-ANCHOR published = yes/no;
- later-section leakage = yes/no.

### Visual inspection
Provide a page-by-page log for **every page**:
- major content on page;
- table/figure present;
- issue found;
- correction made if any;
- final status.

### Layout summary
- clipping;
- overflow;
- blank pages;
- broken captions;
- orphan headings;
- image readability;
- Vietnamese glyphs;
- margin consistency.

Do not copy stale page descriptions from the old Chapter 2 QA report.

The page log must describe the newly rendered WR1 DOCX.

## 18. Review-only status

This is a review snapshot, not a final deliverable.

The QA report must end with:

`WR1_DEMO1_WORD_R1_READY_FOR_EXTERNAL_REVIEW`

Do not write:
- FINAL;
- PUBLICATION READY;
- READY FOR SUBMISSION.

## 19. Files allowed to create/modify

Allowed:
- `work/do-an/output/review/DEMO_1_CH2_CH3_31_32_REVIEW.docx`
- `work/do-an/output/review/DEMO_1_CH2_CH3_31_32_REVIEW_QA.md`

Do not modify:
- `work/do-an/CHAPTER_2.md`
- `work/do-an/output/CHAPTER_2_FINAL.docx`
- approved Chapter 3 Markdown;
- approved presentation PNGs;
- evidence;
- numbering ledger;
- project truth/governance files except no state update is required in this executor task.

Do not create WR2 yet.

## 20. Project QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

Also validate the DOCX opens and is non-zero.

## 21. Git

Commit:

`review(word): build Demo 1 report snapshot`

Push:

`feature/wr1-demo1-word-review-v2`

Do not merge.

## 22. Handoff

Return:

1. branch;
2. starting SHA;
3. local/remote commit SHA;
4. output DOCX path;
5. output DOCX SHA-256;
6. file size;
7. page count;
8. H1/H2/H3 counts;
9. table count + numbering;
10. figure count + numbering;
11. Chapter 2 preservation audit;
12. Chapter 3 source-drift audit;
13. citation-anchor audit;
14. 100% page visual-inspection result;
15. list of any layout corrections made;
16. project QA results;
17. clean git status.

Final state:

`WR1_DEMO1_WORD_R1_READY_FOR_EXTERNAL_REVIEW`

Then STOP.

Do not start WR2.
Do not open X7D1.
Do not write Section 3.4.
Do not open Case C.
Do not write Chapter 4.
