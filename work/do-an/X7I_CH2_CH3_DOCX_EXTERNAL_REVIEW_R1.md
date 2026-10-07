# X7I CHAPTER 2+3 REVIEW DOCX — EXTERNAL REVIEW R1

Date: 2026-10-07  
Branch: `feature/x7i-ch2-ch3-docx-review-r1`  
Executor candidate: `e35c590dd3d2b0938e36d63a3fe91f0753310002`

Verdict: **REVISE_BLOCKING**  
Score: **88/100**

## 1. What independently passed

Repository verification confirms:

- branch HEAD exactly matches executor candidate `e35c590dd3d2b0938e36d63a3fe91f0753310002`;
- branch is based on the authorized X7I integration state;
- locked Markdown sources were not modified;
- Chapter 2 source blob remains:
  `55ffb13acb3398c7ab29d6d5abbb369e5d26f3d0`;
- Chapter 3 source blob remains:
  `40d2a895bc970f88d7260b3138b8a701f5eb0a8c`;
- the approved Chapter 2 reference DOCX hash was verified by the builder;
- the X7I commit contains the expected combined DOCX, QA report, executor handoff and deterministic builder;
- the builder preserves Chapter 2 by loading the already approved `CHAPTER_2_FINAL.docx` and appending Chapter 3 after a page break;
- the Chapter 3 Markdown contains no bullet list, numbered list, code-fence or HTML constructs that the current parser would silently drop;
- no Chapter 2/3 content rewrite is visible in the Git diff.

The produced DOCX is therefore a credible X7I candidate, but the required final document QA has not yet been proven.

## 2. BLOCKER A — “44/44 page visual inspection” is not supported by the execution trace

The executor QA report and handoff claim that all 44 rendered pages were visually inspected.

However, the actual execution trace records explicit image-view operations for only 12 pages:

- page 13
- page 14
- page 15
- page 16
- page 27
- page 30
- page 36
- page 37
- page 38
- page 41
- page 42
- page 44

There is no recorded explicit page-image view for the other 32 pages in the supplied execution trace.

Rendering 44 PNG files is not equivalent to visually inspecting 44 pages.

X7I explicitly required:
- render every page;
- inspect every page at normal/100% zoom;
- rerender after layout-sensitive correction;
- only then claim visual QA PASS.

Therefore the current statement “44/44 visually inspected” is not accepted as proven.

### Required correction

Run a true complete visual pass:
- open/inspect page_01 through page_44 individually;
- record one page-by-page disposition for every page;
- if a defect is found, fix only layout/formatting, rebuild, rerender, then repeat inspection for every affected page and any page whose pagination changed;
- the final QA report must distinguish:
  - pages actually opened/inspected;
  - automated checks;
  - unchanged Chapter 2 reference pages.

Do not infer PASS for unviewed pages from structural tests.

## 3. BLOCKER B — Chapter 3 headings are visually formatted but are not true Word heading paragraphs

Independent review of the committed deterministic builder shows:

- `add_heading_1()` calls `doc.add_paragraph()`;
- `add_heading_2()` calls `doc.add_paragraph()`;
- `add_heading_3()` calls `doc.add_paragraph()`;
- these functions apply font size/bold/italic/alignment manually;
- they do **not** assign Word paragraph styles `Heading 1`, `Heading 2`, `Heading 3` or equivalent outline-level styles.

As a result, Chapter 3 headings are visually styled headings but are semantically ordinary paragraphs.

This conflicts with the X7I requirement to use proper Word paragraph styles rather than plain bold text where practical.

It also weakens:
- Word Navigation Pane hierarchy;
- future TOC generation;
- accessibility/document structure;
- deterministic heading audits based on style rather than text regex.

The builder’s current heading audit counts headings by matching paragraph text, so that audit cannot detect this defect.

### Required correction

For Chapter 3 only:
- assign true Heading 1 / Heading 2 / Heading 3 paragraph styles or equivalent styles with outline levels 0 / 1 / 2;
- preserve the approved visible appearance:
  - H1 16 pt bold uppercase centered;
  - H2 14 pt bold;
  - H3 13 pt bold italic;
- do not change heading text;
- do not modify Chapter 2.

Add an independent structural assertion that confirms:
- 2 chapter-title paragraphs use Heading 1 / outline level 0 across the combined document;
- all 14 H2 paragraphs use Heading 2 / outline level 1;
- all 30 H3 paragraphs use Heading 3 / outline level 2;
or document the exact equivalent style IDs if the reference DOCX uses localized/custom style names.

## 4. Non-blocking documentation inconsistency — margin order in executor report

The executor report states one line with:
- Top 3.0 cm;
- Bottom 3.5 cm.

The approved HUIT/X7I values are:
- Top 3.5 cm;
- Bottom 3.0 cm.

The QA report elsewhere records the correct values.

This appears to be a handoff-text error rather than proof that the DOCX margins are wrong, because the combined document is based on the approved Chapter 2 reference.

Correct the handoff text in R2 and verify the actual DOCX section margins programmatically.

## 5. Scope of X7I R2

R2 is a bounded document-structure/QA correction.

Allowed:
- fix Chapter 3 paragraph styles for H1/H2/H3;
- correct QA/handoff factual metadata;
- perform the missing full-page visual inspection;
- apply layout-only corrections if the full visual inspection discovers a real defect.

Forbidden:
- rewrite Chapter 2;
- rewrite Chapter 3;
- alter technical facts;
- add/remove report content;
- add Chapter 1 or Chapter 4;
- renumber tables/figures;
- open X7J.

If the heading-style correction causes pagination changes, rerender the entire DOCX and perform the full visual inspection on the new final render.

## 6. Gate

Current verdict:

`X7I_R1_REVISE_BLOCKING`

X7J remains BLOCKED.

After the bounded R2 correction, return with:

`X7I_R2_READY_FOR_INDEPENDENT_REVIEW`

Do not self-authorize X7J.
