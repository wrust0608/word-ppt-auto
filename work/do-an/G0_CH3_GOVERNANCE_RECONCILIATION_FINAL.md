# G0 CHAPTER 3 GOVERNANCE RECONCILIATION — FINAL

Date: 2026-10-06  
Verdict: `PASS`

## 1. Purpose

Close roadmap/governance drift before any Chapter 3 prose is authored.

## 2. Reconciled authorities

Current Chapter 3 authority:
- `CHAPTER_3_CONTRACT.md` — current canonical contract;
- `CHAPTER_3_SECTIONED_AUTHORING_PLAN.md` — section-by-section workflow;
- `CHAPTER_3_SECTION_EVIDENCE_MAP.md` — current section numbering/evidence map;
- `CHAPTER_3_NUMBERING_LEDGER.md` — figure/table lock;
- `CHAPTER_3_SECTION_CLAIM_MAP_TEMPLATE.md` — per-section claim traceability.

## 3. Superseded/historical controls

Confirmed:
- `OUTLINE.md` detailed Chapter 2/3 structures are marked superseded;
- `CHAPTERS_2_4_EVIDENCE_MAP.md` old section numbering is marked historical;
- `CHAPTER_3_AUTHORING_CONSTRAINTS.md` monolithic quota is marked superseded;
- `ROADMAP_2_6.md` is marked historical;
- `HANDOFF.md` has a 2026-10-06 current override;
- `prompts/CONTINUE_DO_AN_PROMPT.md` has a 2026-10-06 current override;
- `PROJECT_STATE.md` begins with a current-state summary and explicitly labels the 2026-10-04 artifact snapshot historical.

## 4. Integration branch

Current accumulation branch:
`feature/ch3-integration`

Created from reconciled `main`, then X6 evidence-prep lineage was merged into it.

Merge commit:
`85f28df4c4c2a5409a11c886b826a56c6736044b`

Integration branch verified to contain:
- current governance files;
- 83 staged evidence rows;
- 0 evidence SHA mismatch from X6;
- final Chapter 2 DOCX QA;
- supersession markers for stale authoring artifacts.

## 5. Section branch policy

Every new Chapter 3 phase:
1. starts from current `feature/ch3-integration` HEAD;
2. works only on its section;
3. passes external review;
4. requires user approval;
5. is then integrated before the next section branch is created.

No isolated section branch may be based on an older X6/X7 branch after this point.

## 6. Two-pass policy

For X7A–X7E:

Pass 0:
- evidence inventory;
- figure selection;
- table/presentation design;
- claim-evidence map;
- no report prose.

Pass 1:
- prose draft using approved presentation plan;
- self-review.

## 7. Numbering policy

Current counters:
- next table = Bảng 3.1;
- next figure = Hình 3.1.

Numbers remain tentative until the corresponding section is user-approved.

## 8. Traceability policy

100% major result claims require a section claim-evidence-map row.

Stable Evidence IDs and Source IDs stay internal.
They do not appear in student-facing prose.

## 9. Gate

G0 blockers: 0.

Authorized next phase:
`X7A0 — 3.1 Baseline Evidence & Presentation Plan`

Not authorized yet:
- 3.1 prose;
- Scenario 1;
- Scenario 2;
- Case B;
- Case C;
- Chapter 4.
