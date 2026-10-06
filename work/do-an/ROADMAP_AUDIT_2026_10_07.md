# ROADMAP AUDIT — CURRENT PRODUCT TARGET 2026-10-07

Status: `FINAL_AUDIT / APPLIED_TO_CURRENT_ROADMAP`

## 1. User-defined product target

The current milestone is not "finish the entire thesis".

The current product target is:

1. keep the already user-approved Chapter 2 locked;
2. finish all of Chapter 3;
3. review Chapter 3 as one coherent chapter, not merely as individually passing sections;
4. user-approve the complete Chapter 3;
5. only then assemble locked Chapter 2 + approved Chapter 3 into one Word document;
6. perform a final document-level review so the user can read and evaluate the combined Chapters 2–3;
7. STOP and wait for explicit user instruction before opening any later chapter/workstream.

This is the authoritative interpretation of the current objective.

## 2. What the roadmap got right

Preserve:
- canonical evidence over historical report prose;
- Chapter 2 remains locked during Chapter 3 production;
- sectioned Chapter 3 workflow;
- `feature/ch3-integration` as approved-section accumulation branch;
- section-level figure/table numbering locks;
- separation between Chapter 3 measured results and later risk/recommendation analysis;
- technical locks: `445 OPEN != vulnerable`, `SMBv1 enabled != MS17-010 confirmed`, `UNKNOWN != SAFE`, `SMBv1 disabled != PATCHED`, `FILTERED != PATCHED`.

## 3. Roadmap drift found

### DRIFT-01 — Intermediate Word checkpoints were invented
WR1/WR2 were not part of the original Chapter 3 execution plan. They interrupted Chapter 3 and created a false dependency.

Decision:
- WR1 = preview artifact only;
- WR2 = do not open;
- no DOCX assembly until complete Chapter 3 is approved.

### DRIFT-02 — Chapter 1/report-wide enrichment was opened without user scope
Decision:
- all RG1/report-wide enrichment branches are abandoned;
- they are not part of the current roadmap.

### DRIFT-03 — Historical roadmap auto-opens Chapter 4
Decision:
- Chapter 4 is dormant/backlog;
- it does not auto-open after Chapter 3;
- explicit user instruction is required after the combined Chapters 2–3 review.

### DRIFT-04 — Section-level PASS risked becoming more important than chapter-level readability
Sections 3.1–3.3 already contain approximately 4,321 prose words before Case B, Case C and synthesis.

Risk:
- repeated 139/445 observations;
- repeated SMB dialect list;
- repeated UNKNOWN/UNPATCHED boundaries;
- QA-like prose rather than one coherent result chapter.

Decision:
- X7H must include whole-chapter coherence and compression;
- section approval locks technical meaning/evidence allocation, not every redundant sentence;
- editorial trimming/reordering may occur at X7H only if technical meaning is unchanged;
- technical meaning changes require explicit section reopen.

### DRIFT-05 — Internal governance can leak into the product
Claim maps, Evidence IDs, scores and gates are internal QA only.

Decision:
- final prose is judged by academic readability, technical correctness and visible demo logic;
- a clean branch/test suite alone is never enough for product PASS.

### DRIFT-06 — Authority files contained stale next actions
Before this audit:
- PROJECT_STATE still described 3.1 -> X7B as immediate work;
- NUMBERING_LEDGER still made X7D1 depend on WR1/WR2;
- SECTIONED_AUTHORING_PLAN ended at a standalone Chapter 3 DOCX;
- old execution roadmap would continue to Chapter 4 automatically.

These are superseded by the current roadmap.

## 4. Product-shape requirement

Final Chapter 3 must read as:

`baseline -> Scenario 1 -> Scenario 2 -> Case B -> Case C -> comparison -> chapter conclusion`

not:

`QA record -> screenshot explanation -> repeated inference warning -> another QA record`.

Whole-chapter review must check:
- narrative progression;
- repetition/compression;
- section balance;
- figure/table value;
- academic voice;
- technical integrity;
- Chapter 3 boundary.

## 5. Current authority

`work/do-an/ROADMAP_CURRENT_CH2_CH3_2026_10_07.md`

Only tasks in that roadmap are executable for the current milestone.
