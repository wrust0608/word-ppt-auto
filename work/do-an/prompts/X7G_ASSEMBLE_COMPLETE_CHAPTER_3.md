# X7G — MECHANICALLY ASSEMBLE COMPLETE CHAPTER 3

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7g-ch3-assembly`  
Approved integration base: `14123b8736d34ffb51b9190701c6c0c191da8fd7`

## 0. Mandatory global checkpoint

Before doing anything, re-check the entire current product roadmap.

Read first:

1. `work/do-an/ROADMAP_CURRENT_CH2_CH3_2026_10_07.md`
2. `work/do-an/PROJECT_STATE.md`
3. `work/do-an/CHAPTER_3_CONTRACT.md`
4. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`

Confirm:

- Chapter 2 is already locked and is NOT modified in X7G.
- Sections 3.1–3.7 are individually user-approved and locked.
- Bảng 3.1–3.7 are locked.
- Hình 3.1–3.11 are locked.
- next unused numbers are Bảng 3.8 / Hình 3.12.
- X7G is only mechanical Chapter 3 assembly.
- X7H whole-Chapter-3 review is still mandatory after X7G.
- X7I Word assembly is BLOCKED until X7H review + explicit user approval of complete Chapter 3.
- Chapter 1 enrichment / old WR1/WR2 intermediate Word workflow remain abandoned/cancelled.
- Chapter 4 remains dormant.

If any current repository state contradicts this sequence, STOP and report it.

## 1. Start and lineage

Run:

```bash
git fetch origin
git checkout feature/x7g-ch3-assembly
git pull --ff-only origin feature/x7g-ch3-assembly
git status --short
git rev-parse HEAD
git merge-base --is-ancestor 14123b8736d34ffb51b9190701c6c0c191da8fd7 HEAD
```

If lineage fails, STOP.

## 2. Objective

Create one complete Markdown Chapter 3 from the already-approved section files.

This is a **mechanical assembly task**, not a new writing task.

Create:

`work/do-an/CHAPTER_3_COMPLETE_R1.md`

with exact chapter title:

`# CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH`

Then include the approved sections in this exact order:

1. `work/do-an/CH3_31_BASELINE_DRAFT_R1.md`
2. `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md`
3. `work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md`
4. `work/do-an/CH3_34_CASEB_DRAFT_R1.md`
5. `work/do-an/CH3_35_CASEC_DRAFT_R1.md`
6. `work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md`

## 3. Critical assembly rule

Default behavior: **copy each approved section verbatim**.

Do not:
- paraphrase;
- rewrite;
- shorten;
- expand;
- change technical claims;
- alter table wording;
- alter captions;
- renumber tables/figures;
- alter image paths;
- replace terminology;
- "improve" prose.

X7H owns whole-chapter editorial review/compression.

In X7G, preserve the exact approved content so X7H can review the real integrated chapter without hidden edits.

Allowed mechanical changes only:
- insert the H1 Chapter 3 title above Section 3.1;
- ensure exactly one blank line between assembled source files;
- remove accidental duplicate trailing/leading blank lines at section boundaries;
- normalize final newline at EOF.

No sentence-level editing is authorized.

## 4. Required heading order

The assembled file must contain exactly this H2 sequence:

1. `## 3.1. Trạng thái baseline trước đo đạc`
2. `## 3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB`
3. `## 3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE`
4. `## 3.4. Kết quả Case B — Vô hiệu hóa SMBv1 và đo lại từ xa`
5. `## 3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense`
6. `## 3.6. So sánh kết quả thực nghiệm`
7. `## 3.7. Tổng kết chương`

Expected H3 headings:

- 3.1.1
- 3.1.2
- 3.2.1
- 3.2.2
- 3.3.1
- 3.3.2
- 3.4.1
- 3.4.2
- 3.5.1
- 3.5.2

No H3 under 3.6 or 3.7.

## 5. Locked numbering

The complete chapter must contain exactly:

### Tables
- Bảng 3.1
- Bảng 3.2
- Bảng 3.3
- Bảng 3.4
- Bảng 3.5
- Bảng 3.6
- Bảng 3.7

No duplicate.
No missing table number.
No Bảng 3.8.

### Figures
- Hình 3.1
- Hình 3.2
- Hình 3.3
- Hình 3.4
- Hình 3.5
- Hình 3.6
- Hình 3.7
- Hình 3.8
- Hình 3.9
- Hình 3.10
- Hình 3.11

No duplicate.
No missing figure number.
No Hình 3.12.

## 6. Image-path integrity

For every Markdown image reference in the assembled chapter:

- verify the referenced file exists;
- preserve the exact approved relative path;
- do not copy/rename/regenerate an image;
- do not create a montage;
- do not alter image bytes.

Report:
- number of image references;
- number of unique image paths;
- missing paths, if any.

Expected:
- 11 numbered figures;
- all source image paths resolve.

If any image path is broken, do not silently fix it. Report the discrepancy and STOP before inventing a replacement.

## 7. Approved-source integrity

Create:

`work/do-an/CHAPTER_3_ASSEMBLY_SELF_REVIEW_R1.md`

Record for each source file:
- path;
- Git blob SHA or file SHA available from Git;
- first heading;
- last heading/section;
- whether its complete approved text appears exactly once in `CHAPTER_3_COMPLETE_R1.md`.

Use a programmatic exact-content check.

Recommended check:
- read each source file;
- verify source text, after only trimming terminal newline differences, occurs exactly once in assembled text.

Because the H1 title is new, it is outside source-section integrity checks.

If any approved source block does not match exactly, STOP and correct the assembly before committing.

## 8. Cross-reference audit

Check the complete chapter for section references such as:
- Mục 3.1;
- Mục 3.2;
- Mục 3.3;
- Mục 3.4;
- Mục 3.5;
- Mục 3.6.

Do not rewrite them unless they are mechanically broken.

Report:
- any reference to a nonexistent Chapter 3 section;
- any reference to Hình/Bảng numbers that do not exist;
- any obvious forward/backward reference mismatch.

Do not change technical prose in X7G to "improve" a valid reference.

## 9. Whole-chapter structural audit

Report:

- total prose word count;
- H1 count;
- H2 count;
- H3 count;
- table count;
- figure count;
- image reference count;
- section order;
- table number sequence;
- figure number sequence.

Expected structural counts:

- H1: 1
- H2: 7
- H3: 10
- numbered tables: 7
- numbered figures: 11

Do not treat these counts alone as a quality PASS; X7H will perform the full product review.

## 10. No-content-drift audit

Search the assembled file for the major locked technical boundaries:

- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `SMBv1 disabled != PATCHED`
- `FILTERED != PATCHED`
- `UNKNOWN != SAFE`

Also confirm the complete chapter does NOT introduce:
- new SAFE verdict;
- NOT VULNERABLE verdict;
- remote VULNERABLE verdict;
- exploit/RCE/reverse shell/Meterpreter result;
- completed Case A patch experiment;
- Chapter 4 recommendation/risk ranking;
- a new Hình 3.12 or Bảng 3.8.

This is a detection audit only.
Do not rewrite content in X7G.

## 11. Output artifacts

Create exactly:

1. `work/do-an/CHAPTER_3_COMPLETE_R1.md`
2. `work/do-an/CHAPTER_3_ASSEMBLY_SELF_REVIEW_R1.md`

Do not create:
- DOCX;
- PDF;
- new images;
- new tables/figures;
- new evidence;
- Chapter 2+3 combined file;
- Chapter 4 content.

Do not modify any approved source section.

## 12. QA

Run:

```bash
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_3_COMPLETE_R1.md
git diff --check
```

You may run:
`uv run python scripts/validate_project.py`

Do not change infrastructure to force a PASS.

## 13. Git

Commit:

`assemble(ch3): build complete approved Chapter 3 R1`

Push:

`feature/x7g-ch3-assembly`

Do not merge.

## 14. Handoff

Return:

1. branch;
2. starting SHA;
3. final local/remote SHA;
4. created files;
5. source-file exact-match audit;
6. H1/H2/H3 counts;
7. total prose word count;
8. table count + exact Bảng 3.1–3.7 sequence;
9. figure count + exact Hình 3.1–3.11 sequence;
10. image-path existence audit;
11. cross-reference audit;
12. no-content-drift audit;
13. QA results;
14. clean git status.

Final state:

`X7G_CH3_COMPLETE_R1_READY_FOR_WHOLE_CHAPTER_REVIEW`

Then STOP.

Do not open X7H yourself.
Do not build Word.
Do not modify Chapter 2.
Do not open Chapter 4.
