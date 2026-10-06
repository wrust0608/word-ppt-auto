# DEMO WORD REVIEW WORKFLOW

Status: `LOCKED_USER_REVIEW_WORKFLOW_2026_10_06`

## 1. Purpose

The user requires Word-level review checkpoints in addition to Markdown/evidence review.

The purpose is to let the user inspect the report as a real formatted document after each major demo, rather than waiting until the end of Chapter 3.

These DOCX checkpoints are review artifacts, not permission to rewrite approved technical content.

## 2. Required Word checkpoints

### WR1 — Demo 1 review snapshot

Build after Scenario 1 / Section 3.2 is approved.

Contents:

- approved full Chapter 2;
- approved Chapter 3 Section 3.1;
- approved Chapter 3 Section 3.2.

Do not include unfinished Section 3.3–3.7 placeholders.

Output target:

`work/do-an/output/review/DEMO_1_CH2_CH3_31_32_REVIEW.docx`

Purpose:
- review the complete report state through Demo 1;
- inspect page layout, tables, figures, captions, section continuity and readability.

### WR2 — Demo 2 review snapshot

Build after Scenario 2 / Section 3.3 is approved and after WR1 receives user approval.

Contents:

- approved full Chapter 2;
- approved Chapter 3 Sections 3.1–3.3.

Do not include unfinished Section 3.4–3.7 placeholders.

Output target:

`work/do-an/output/review/DEMO_2_CH2_CH3_31_33_REVIEW.docx`

Purpose:
- review the complete report state through Demo 2;
- verify that Scenario 1 and Scenario 2 read coherently together in formatted Word.

### WR3 — Full Chapter 2 + Chapter 3 review

Build only after Sections 3.4, 3.5, 3.6 and 3.7 are also approved and Chapter 3 assembly has passed its own section-level gates.

Contents:

- approved full Chapter 2;
- complete approved Chapter 3 Sections 3.1–3.7.

Output target:

`work/do-an/output/review/CHAPTER_2_3_FULL_REVIEW.docx`

Purpose:
- perform full-document review of Chapters 2–3 before Chapter 4 proceeds;
- review technical continuity, numbering, cross-references, tables/figures, layout and author voice at document scale.

## 3. Gate order

Current order becomes:

1. WR1 Demo 1 DOCX build
2. independent Word review
3. user approval
4. WR2 Demo 2 DOCX build
5. independent Word review
6. user approval
7. resume X7D0 Case B planning
8. complete X7D/X7E/X7F
9. assemble complete Chapter 3
10. WR3 Chapter 2 + Chapter 3 full DOCX build
11. independent full-document review
12. user approval
13. only then proceed to Chapter 4

X7D0 may already exist as a prepared branch, but execution is paused until WR1 and WR2 are approved.

## 4. DOCX content rule

Word checkpoints are mechanical publication snapshots.

Allowed:
- combine approved content;
- apply locked HUIT formatting;
- insert approved figures/tables;
- update DOCX-native TOC/list fields;
- page-break/layout adjustments;
- keep-with-next / table row pagination;
- caption placement;
- image scaling/cropping already approved;
- fix purely presentational defects.

Forbidden without explicit content reopen:
- rewrite approved claims;
- reinterpret evidence;
- change result wording;
- renumber approved tables/figures;
- add new technical conclusions;
- silently repair content by changing canonical Markdown.

If Word layout exposes a substantive content problem, record it as a review issue and reopen the relevant Markdown only after reviewer/user approval.

## 5. Formatting baseline

Reuse the validated Chapter 2 DOCX formatting baseline:

- A4 portrait;
- margins: top 3.5 cm, bottom 3.0 cm, left 3.5 cm, right 2.0 cm;
- Times New Roman;
- body 13 pt;
- 1.5 line spacing;
- justified body text;
- first-line indent 1.0 cm;
- chapter heading 16 pt bold uppercase;
- H2 14 pt bold;
- H3 13 pt bold italic;
- table title above table;
- figure caption below figure;
- keep headings/captions with following objects;
- avoid split rows where practical;
- code/command text in a readable monospaced font.

Do not invent a new visual theme.

## 6. Review-document markers

Each checkpoint DOCX must clearly state on the cover/header:

`BẢN REVIEW — CHƯA PHẢI BẢN NỘP CUỐI`

Do not label the checkpoint `FINAL` or `PUBLICATION READY`.

Approved section numbering inside the report must remain unchanged.

## 7. Required DOCX QA

For every WR checkpoint:

1. validate generated DOCX structure;
2. compute SHA-256;
3. render to PDF;
4. render every PDF page to an image;
5. visually inspect 100% of pages;
6. report:
   - total pages;
   - headings;
   - table count;
   - figure count;
   - broken captions;
   - split tables;
   - cropped images;
   - orphan/widow heading issues;
   - blank pages;
   - overflow/out-of-margin content;
   - broken Vietnamese characters;
   - inconsistent font/spacing;
   - unresolved cross-references;
   - citation placeholders / deferred global IEEE normalization.

A successful schema/Office validation alone is not enough.

## 8. Review sequence

After each generated DOCX:

- executor stops;
- independent reviewer inspects content + rendered pages;
- reviewer issues PASS or correction prompt;
- user must explicitly approve;
- only then next workflow gate opens.

## 9. Final Chapter 2 + 3 review

WR3 is stricter than WR1/WR2.

In addition to page QA, it must review:

- continuity between Chapter 2 method and Chapter 3 results;
- every table/figure numbering sequence;
- every cross-reference;
- duplicated explanations across chapters;
- terms SMBv1/SMB2/3/MS17-010/signing/UNKNOWN/UNPATCHED/FILTERED;
- Chapter 3 / Chapter 4 boundary;
- author voice consistency;
- whether every experiment designed in Chapter 2 has a corresponding bounded result in Chapter 3;
- whether any result appears in Chapter 3 without a method basis in Chapter 2.

Only after WR3 external review + user approval may Chapter 4 open.
