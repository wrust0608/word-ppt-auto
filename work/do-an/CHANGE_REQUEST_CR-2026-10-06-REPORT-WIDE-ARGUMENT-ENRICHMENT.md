# CHANGE REQUEST — REPORT-WIDE ARGUMENT ENRICHMENT

ID: `CR-2026-10-06-REPORT-WIDE-ARGUMENT-ENRICHMENT`  
Status: `APPROVED_BY_USER / OPEN_FOR_CONTROLLED_EXECUTION`  
Date: 2026-10-06

## User directive

The user explicitly requested that the report be improved by independently studying reports/theses in the same cybersecurity / vulnerability-assessment domain, then strengthening the logic, argumentation and rationale for why the lab and measurement design were built, while preserving the framework already developed for the report as a whole.

## Why this change request is necessary

The current experimental truth and Chapter 2/Chapter 3 evidence workflow are substantially stronger than the historical prose architecture.

A report-wide audit found that Chapter 1 still contains stale remnants from an older experimental design, including:
- references to Windows 7 as the lab target;
- statements assigning Metasploit an active canonical role;
- exploit/RCE validation language that is outside the canonical run;
- a tool-flow diagram that ends in Metasploit exploitation.

These statements conflict with the current canonical research map:
- target: Windows Server 2012 R2;
- no canonical exploitation/RCE result;
- remote NSE-SMB-04 = UNKNOWN / NO USABLE SCRIPT RESULT;
- local patch state = UNPATCHED;
- Case B = protocol hardening;
- Case C = network access-control mitigation.

Therefore the report must be argument-aligned before final assembly.

## Scope

This change request authorizes controlled revision of report argumentation across Chapters 1–4.

It authorizes:
1. correcting stale narrative and scope in Chapter 1;
2. strengthening the rationale behind experimental design choices in Chapter 2;
3. retrofitting Chapter 3 prose with stronger reader logic while preserving all approved experimental facts/evidence;
4. using the same argument architecture when drafting remaining Chapter 3 sections;
5. authoring Chapter 4 around the resulting defense-in-depth interpretation after Chapter 3 is complete;
6. final report-wide transition, redundancy and thesis-defense review.

It does **not** authorize:
- changing experimental truth;
- inventing additional measurements;
- converting UNKNOWN to SAFE/NOT VULNERABLE/VULNERABLE;
- adding a canonical exploit/RCE result;
- inventing a Case A patch experiment;
- replacing approved screenshots/evidence without a separate evidence decision;
- collapsing Chapter 3 results into Chapter 4 analysis.

## WR1 disposition

The existing WR1 Demo 1 DOCX remains a technically valid formatting snapshot but is **not user-approved as final editorial content**.

WR1 is retained as a layout/reference baseline only.

Do not integrate WR1 as a final report milestone until the new report-wide argument enrichment has been applied and the corresponding Word snapshot is regenerated/reviewed.

## Execution strategy

The report-wide rewrite must not be performed as one uncontrolled monolithic edit.

Required order:

1. `RG0` — report-wide research + argument contract (manager-owned).
2. `RG1` — Chapter 1 canonical realignment and argument enrichment.
3. `RG2` — Chapter 2 rationale and methodological enrichment.
4. `RG3` — Chapter 3 retrofit of completed sections + continuation under the same logic.
5. `RG4` — Chapter 4 analysis/recommendation.
6. `RG5` — full-report assembly, citation normalization, redundancy review and DOCX QA.

Each prose phase requires external review and user approval before being locked.

## Priority of truth

Experimental truth and evidence locks remain higher authority than stylistic/argument enrichment.

The enrichment layer may improve:
- why a choice was made;
- what question a step answers;
- how one measurement logically leads to the next;
- what can and cannot be inferred;
- why each mitigation case exists.

It may not change what actually happened in the lab.
