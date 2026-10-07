# X7H — WHOLE-CHAPTER-3 PRODUCT REVIEW

Status: AUTHORIZED
Date: 2026-10-07
Branch: `feature/x7h-ch3-whole-review-approved-r1`
Base reviewed X7G state: `d348b713802593ff82bbab5b460e5eb7e6973b3d`

## 0. Mandatory global checkpoint

Before editing anything, read and obey:

1. `work/do-an/ROADMAP_CURRENT_CH2_CH3_2026_10_07.md`
2. `work/do-an/PROJECT_STATE.md`
3. `work/do-an/CHAPTER_3_CONTRACT.md`
4. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
5. `work/do-an/CHAPTER_3_SECTION_EVIDENCE_MAP.md`
6. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
7. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`
8. all current R3 evidence/timebase/command-provenance locks
9. `work/do-an/CHAPTER_3_DRAFT_R1.md`
10. `work/do-an/X7G_CH3_ASSEMBLY_EXTERNAL_REVIEW_R2_FINAL.md`

Do not use cancelled or premature X7H/X7G branches as authority.

## 1. Objective

Review the complete Chapter 3 as one real thesis chapter, not as a set of individually approved fragments.

Create a whole-chapter editorial candidate:

`work/do-an/CHAPTER_3_DRAFT_R2.md`

The R1 assembled chapter is the technical baseline. R2 may improve whole-chapter readability only within the editorial authority defined below.

## 2. Mandatory review dimensions

Review the complete flow:

baseline
-> Scenario 1
-> Scenario 2
-> Case B
-> Case C
-> comparison
-> conclusion

Evaluate and correct where justified:

- cross-section repetition;
- unnecessary re-explanation of the same fact;
- section balance;
- transition quality;
- table/figure placement and narrative flow;
- academic Vietnamese naturalness;
- internal QA/audit-memo tone;
- terminology consistency;
- overlong or mechanical paragraphs;
- whether each figure/table actually helps the reader;
- whether the empirical progression is immediately understandable;
- whether Chapter 3 remains defensible sentence by sentence;
- whether any Chapter 4 recommendation/risk-analysis content leaks in.

## 3. Editorial authority

Allowed without reopening a section:

- remove duplicated sentences or duplicated explanations;
- merge or split sentences/paragraphs;
- shorten repetitive wording;
- improve transitions;
- reorder adjacent sentences/paragraphs when factual sequence and technical meaning are unchanged;
- normalize terminology;
- remove internal process language;
- improve captions or surrounding prose only when no factual meaning changes;
- resolve the existing VI012 repeated-opening warning.

Preserve:
- all technical facts;
- all evidence boundaries;
- all locked table/figure numbering;
- all results;
- all source/evidence provenance;
- the canonical section hierarchy.

## 4. Hard stop for factual/technical changes

Do NOT silently make any change that alters:

- a measured value;
- port state;
- dialect observation;
- patch classification;
- NSE verdict;
- chronology/provenance;
- topology;
- causal interpretation;
- evidence strength;
- technical conclusion.

If a factual or technical change appears necessary:
1. do not make it;
2. record the exact sentence and reason;
3. mark it as a blocker requiring explicit reopen of the affected approved section.

## 5. Locked technical boundaries

All current locks remain binding, including:

- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `SMBv1 disabled != PATCHED`
- `FILTERED != PATCHED`
- `UNKNOWN != SAFE`
- local patch state independent from remote NSE verdict
- .56.100 identity remains UNKNOWN
- no canonical exploitation/RCE/reverse shell/Meterpreter
- no completed Case A patch experiment
- baseline must not be renamed Case A

Case B:
- TCP445 = OPEN, not post-intervention OPEN (syn-ack)
- TCP139 was not remeasured
- dialect retest records 2.0.2, 2.1, 3.0, 3.0.2
- NT LM 0.12 does not appear in the retest list
- no successful-negotiation/full-workload claim

Case C:
- TCP139/445 = FILTERED/no-response from Kali
- pfSense supports matching SMB SYN traffic recorded as Block
- do not claim the screenshot proves exact named Block-rule match
- remote MS17 = UNKNOWN / NO USABLE SCRIPT RESULT
- local final state remains SMB1=True, SMB2=True, LanmanServer=Running, local 139/445 listeners present, UNPATCHED

Time/provenance:
- no unified cross-system wall-clock timeline
- preserve operator-command vs Nmap-recorded argv distinction
- local signing flags and remote signing observations remain separate.

## 6. Product-quality target

The final candidate should read like a strong Vietnamese student thesis chapter:

- clear empirical progression;
- concise but not over-compressed;
- natural academic prose;
- minimal repetition;
- no QA/governance tone;
- tables/figures integrated into the narrative;
- conclusions bounded to evidence;
- no Chapter 4 recommendations or risk-ranking leakage.

Do not optimize for an AI detector.

## 7. Required outputs

Create:

1. `work/do-an/CHAPTER_3_DRAFT_R2.md`
2. `work/do-an/X7H_CH3_WHOLE_REVIEW_SELF_REVIEW_R1.md`
3. `work/do-an/X7H_CH3_WHOLE_REVIEW_EXECUTOR_HANDOFF_R1.md`

The self-review must include:

- R1 vs R2 word-count comparison;
- per-section word-count comparison;
- every paragraph/sentence deletion or merge that materially changes wording;
- every transition edit;
- all terminology normalization;
- all figure/table flow changes;
- evidence that no numbering changed;
- evidence that no technical fact changed;
- technical-lock scan;
- Chapter 4 leakage scan;
- internal QA/governance language scan;
- linter result;
- tests;
- `git diff --check`;
- project validation;
- any unresolved issue requiring section reopen.

The executor handoff must make independent review possible without trusting the executor's own conclusion.

## 8. Forbidden

Do not:
- create DOCX/PDF;
- edit Chapter 2;
- open Chapter 4;
- create new evidence;
- create a new table or figure;
- allocate Bảng 3.8 or Hình 3.12;
- change a technical fact;
- declare the complete Chapter 3 user-approved;
- open X7I.

## 9. Stop state

The only allowed completion state is:

`X7H_R1_READY_FOR_INDEPENDENT_REVIEW`

Commit and push the required artifacts, return the execution report, then STOP.

Independent review and explicit user approval of the complete Chapter 3 are still required before X7I.
