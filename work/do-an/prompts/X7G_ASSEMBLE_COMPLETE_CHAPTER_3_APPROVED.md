# X7G — ASSEMBLE COMPLETE APPROVED CHAPTER 3

Status: AUTHORIZED
Date: 2026-10-07
Branch: `feature/x7g-ch3-assembly-approved-r1`
Base integration HEAD: `5cedb4d183d9cf58c60fd4553b264768726d0c80`

## Mandatory checkpoint

Before editing, read the current roadmap, PROJECT_STATE, Chapter 3 contract, sectioned authoring plan, evidence map, numbering ledger, Experimental Truth Matrix, all R3 locks, and the approved Section 3.1–3.7 drafts.

Historical/cancelled workflows must not be used to choose actions.

## Scope

Mechanically assemble the USER APPROVED / LOCKED Sections 3.1–3.7 into:

`work/do-an/CHAPTER_3_DRAFT_R1.md`

Use only the approved section drafts already present in the repository.

Preserve:
- the canonical Chapter 3 title and section order;
- all approved technical meaning;
- Bảng 3.1–3.7;
- Hình 3.1–3.11;
- all canonical evidence, timebase, provenance, interpretation, and wording boundaries recorded in the current locks.

X7F allocates no new figure.

## Allowed

Only:
- combine approved sections;
- normalize heading hierarchy and cross-references;
- clean transitions;
- remove obvious duplicate sentences caused by assembly;
- normalize terminology without changing technical meaning;
- normalize table/figure placement;
- fix trivial grammar, punctuation, and spacing that do not alter meaning.

## Forbidden

Do not:
- add evidence;
- add a result claim;
- reinterpret technical results;
- create a new table or figure;
- create Bảng 3.8 or Hình 3.12;
- add recommendations or ranking;
- reopen an approved section;
- edit Chapter 2;
- open Chapter 4;
- create DOCX/PDF;
- open X7H automatically.

If a factual or technical change appears necessary, do not make it. Record it as a blocker for independent review.

## Product quality

The result must read as one coherent Vietnamese academic chapter rather than pasted independent review notes.

Check the complete flow:

baseline -> Scenario 1 -> Scenario 2 -> Case B -> Case C -> comparison -> conclusion.

Do not over-compress approved content. Whole-chapter editorial review belongs to X7H.

## Required outputs

Create:
1. `work/do-an/CHAPTER_3_DRAFT_R1.md`
2. `work/do-an/X7G_CH3_ASSEMBLY_SELF_REVIEW_R1.md`
3. `work/do-an/X7G_CH3_ASSEMBLY_EXECUTOR_HANDOFF_R1.md`

Self-review must report:
- source sections assembled;
- heading order;
- Bảng 3.1–3.7 order;
- Hình 3.1–3.11 order;
- confirmation that no new numbering was introduced;
- cross-reference/transition/duplicate cleanup performed;
- every non-format wording edit;
- canonical-lock compliance;
- any unresolved conflict;
- git diff summary;
- tests/linter/diff-check actually run.

The executor handoff must enable independent review without trusting the executor's own PASS statement.

## Stop state

The only allowed completion state is:

`X7G_ASSEMBLY_READY_FOR_INDEPENDENT_REVIEW`

Commit the required artifacts, report the execution result, then STOP.

Do not authorize or execute X7H.
