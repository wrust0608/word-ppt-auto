# ROADMAP REVIEW — PRE-X7A CHAPTER 3

> **STATUS OVERRIDE 2026-10-07:** Đây là audit lịch sử trước khi X7A bắt đầu. Không dùng phần “roadmap beyond Chapter 3” làm next action. Current authority: `ROADMAP_CURRENT_CH2_CH3_2026_10_07.md`.

Date: 2026-10-06  
Reviewer role: Lecturer / thesis-project reviewer in Information Security  
Verdict: `DIRECTIONALLY_CORRECT / NOT_READY_TO_EXECUTE`

## 1. Overall finding

The sectioned Chapter 3 workflow is the correct direction.

However, execution should not begin yet because the repository still contains several higher-level artifacts whose structure/status conflicts with the new workflow.

The risk is not technical evidence loss. The risk is governance drift: a later executor may follow a stale locked artifact and silently reintroduce a superseded structure.

Therefore X7A should remain on HOLD until the roadmap/governance layer is reconciled.

## 2. What is correct and should be preserved

PASS:
- Chapter 2 is user-approved and its final DOCX has passed.
- X6 evidence staging has passed:
  - 83 staged files;
  - 78 primary/direct;
  - 5 secondary metadata/closure;
  - 0 SHA mismatch.
- R3 technical locks are adequate for Chapter 3.
- The decision to author Chapter 3 section-by-section is academically and operationally sound.
- The intended result flow is correct:
  `baseline -> Scenario 1 -> Scenario 2 -> Case B -> Case C -> synthesis`.
- Chapter 3 / Chapter 4 boundary is directionally correct.

## 3. BLOCKER G1 — master outline drift

`OUTLINE.md` still contains:
- an obsolete 2.1–2.9 Chapter 2 structure;
- an obsolete 3.1–3.8 Chapter 3 structure.

The approved Chapter 2 is now 2.1–2.7.

The new sectioned Chapter 3 intends 3.1–3.7.

Risk:
an executor reading `OUTLINE.md` as LOCKED_CANONICAL may follow a stale structure.

Required before X7A:
- either update OUTLINE.md under explicit change control;
- or mark its Chapter 2/3 structural portion superseded and point to the current approved chapter/section plan.

## 4. BLOCKER G2 — evidence-map section numbering drift

`CHAPTERS_2_4_EVIDENCE_MAP.md` still maps evidence against the old Chapter 2 and old Chapter 3 numbering:
- 2.1–2.8 legacy map;
- 3.4 standalone patch reconciliation;
- 3.5 Case B;
- 3.6 Case C;
- 3.7 result matrix.

The current proposed sectioned Chapter 3 is:
- 3.1 baseline;
- 3.2 Scenario 1;
- 3.3 Scenario 2;
- 3.4 Case B;
- 3.5 Case C;
- 3.6 comparison;
- 3.7 summary.

Required:
create a new current section-to-evidence map or revise the old map under change control.

## 5. BLOCKER G3 — monolithic authoring contract still looks active

`CHAPTER_3_AUTHORING_CONSTRAINTS.md` still has status:
`LOCKED_FOR_X7_DRAFT`

and fixes:
- 7 H2;
- 16 H3;
- 6 tables;
- exactly 8 images.

The new sectioned workflow explicitly removes the global fixed image/table quota and allows each section to have its own evidence geometry.

Required:
mark the monolithic constraints file as superseded by `CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`, or create a new canonical Chapter 3 contract that absorbs the useful technical locks without the obsolete global quotas.

## 6. BLOCKER G4 — project-state header is stale

The beginning of `PROJECT_STATE.md` still says, among other stale items:
- Chapter 2 historical/superseded;
- demo data missing;
- old roadmap status;
- old next action.

Later DEC entries correctly record Chapter 2 approval and X6 PASS.

Risk:
tools/agents that read only the first section may make the wrong decision.

Required:
add a current-state summary at the top or refactor stale status into a clearly historical section.

## 7. BLOCKER G5 — branch integration strategy is incomplete

Current plan creates isolated section branches, but does not define how approved sections become the accumulated Chapter 3 source.

Risk:
- section A–E may each pass independently but use drifting terminology/numbering;
- final stitching may become a rewrite rather than mechanical assembly.

Required branch model:

1. `feature/ch3-integration` — accumulates only user-approved Chapter 3 sections.
2. Section branch X7A is created from integration.
3. After X7A external review + user approval, approved section artifacts are integrated into `feature/ch3-integration`.
4. X7B is then created from the updated integration branch.
5. Repeat through X7F.

This preserves isolation while giving every later section access to already-approved terminology and numbering.

## 8. BLOCKER G6 — per-section claim traceability is not explicit enough

`CHAPTER_3_CONTRACT.md` requires 100% result claims to trace to evidence.

The current X7A artifact set has:
- draft;
- figure selection;
- self-review.

That is not a full claim ledger.

Required for every section:
add a private/internal file:

`CH3_<section>_CLAIM_EVIDENCE_MAP.md`

Each row:
- claim ID;
- short report claim;
- source artifact(s);
- Evidence ID(s);
- external source if needed;
- allowed wording;
- boundary;
- status.

This file is internal and must not appear in report prose.

## 9. BLOCKER G7 — figure/table numbering needs a lock protocol

Because sections are authored independently, figure/table numbers can drift.

Required:
after each section is user-approved:
- lock the final figure count/range;
- lock the final table count/range;
- record next available Figure 3.x and Table 3.x numbers.

The next section starts from those counters.

Do not renumber already approved sections unless user explicitly reopens them.

## 10. GLOBAL citation-numbering risk

HUIT requires IEEE references ordered by first appearance in the report.

Current chapter files have historically been reviewed with chapter-local numbering.

Before final publication:
- all chapter-local citation numbers must be normalized against one global bibliography;
- Source IDs are the stable semantic keys;
- numeric IEEE labels are publication-time presentation labels.

For section drafting:
- record Source IDs in internal claim maps;
- avoid introducing unnecessary external citations;
- defer global renumbering to the full-report citation-normalization gate.

This is not a blocker for writing the experimental observations themselves, but it is a blocker for final DOCX publication.

## 11. Image handling refinement

The user's concern about wide/many screenshots is valid.

Recommended two-pass process inside each section:

### Pass A — evidence/presentation plan
- inspect all relevant screenshots;
- KEEP / OPTIONAL / DROP;
- define table shape;
- define crop needs;
- no prose lock yet.

### Pass B — section draft
- write prose using only approved figure set;
- embed original image if readable;
- otherwise create a derived presentation crop.

Derived crop rule:
- source evidence bytes remain untouched;
- every crop has source path + source SHA-256 + crop rectangle/purpose recorded in a section derivation manifest;
- crop must not remove context necessary for the claim.

This is especially important for Scenario 1 and Case C.

## 12. Revised phase model

### G0 — Governance reconciliation
Before any Chapter 3 prose:
- reconcile OUTLINE;
- reconcile evidence-map numbering;
- supersede monolithic X7 constraints;
- refresh PROJECT_STATE current summary;
- create Chapter 3 integration branch;
- define section claim-map template;
- define figure/table numbering ledger.

### X7A — 3.1 Baseline
A0: evidence/figure/table plan  
A1: draft  
A2: external review  
A3: user approval + integration lock

### X7B — 3.2 Scenario 1
B0: B2–B6 evidence/figure/table plan  
B1: draft  
B2: external review  
B3: user approval + integration lock

### X7C — 3.3 Scenario 2
C0: NSE01–04 evidence/figure/table plan  
C1: draft  
C2: external review  
C3: user approval + integration lock

### X7D — 3.4 Case B
D0: before/action/after/retest presentation plan  
D1: draft  
D2: external review  
D3: user approval + integration lock

### X7E — 3.5 Case C
E0: topology/rule/Nmap/log presentation plan  
E1: draft  
E2: external review  
E3: user approval + integration lock

### X7F — 3.6 + 3.7
Use only approved X7A–X7E results.
- comparison matrix;
- measured differences;
- chapter summary;
- no new raw evidence.

### X7G — mechanical Chapter 3 assembly
Assemble only approved section files.
Allowed edits:
- transitions;
- duplicate-sentence removal;
- terminology consistency;
- figure/table references;
- citation placeholders.

Forbidden:
- reinterpreting results;
- adding new evidence;
- changing approved result claims.

### X7H — full Chapter 3 external review + user approval
Only after PASS:
- lock Chapter 3;
- create final Chapter 3 DOCX if needed;
- open Chapter 4.

## 13. Roadmap beyond Chapter 3

After Chapter 3 approval:

### X8 — Chapter 4
First re-review `CHAPTER_4_CONTRACT.md` against approved Chapter 3.
Then author:
- interpretation of baseline;
- Case B/Case C comparison;
- patching role;
- CIA/risk;
- limitations;
- recommendations;
- no new experimental evidence.

### X9 — Chapter 1/source closure
Before final publication:
- close remaining RECHECK/source issues;
- synchronize Chapter 1 claims and bibliography;
- ensure no stale unsupported citation survives.

### X10 — opening/conclusion/front matter
- Introduction;
- conclusion/recommendations summary;
- abstracts;
- acknowledgments/declarations as required;
- lists of abbreviations/tables/figures.

### X11 — global consistency and IEEE normalization
- terminology;
- cross-references;
- figure/table numbering;
- Source ID -> final global IEEE numbering;
- bibliography metadata;
- no orphan citations.

### X12 — final DOCX publication build
- HUIT formatting;
- automatic TOC;
- list of figures/tables;
- section/page numbering;
- render every page;
- visual QA every page;
- fix and re-render until clean.

## 14. Final verdict

The sectioned strategy is the correct authoring strategy.

But X7A should not start until G0 governance reconciliation is complete.

Recommended current state:
`X7A_HOLD_FOR_ROADMAP_RECONCILIATION`.
