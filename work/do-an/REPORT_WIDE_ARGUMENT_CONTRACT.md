# REPORT-WIDE ARGUMENT CONTRACT — 2026-10-06

Status: `CANONICAL_CANDIDATE / USER-DIRECTED`

This contract controls argumentation and narrative logic. It does not supersede experimental truth/evidence locks.

## 1. Central claim

The report demonstrates a controlled method for assessing SMB/MS17-010-related exposure by separating four distinct evidence axes:

1. network reachability and service exposure;
2. SMB protocol surface;
3. remote vulnerability-oriented scanner signal;
4. local patch state.

The experiment then measures how two different mitigation layers change observable conditions:

- Case B: protocol hardening by disabling SMBv1;
- Case C: network access control through pfSense Transparent Bridge.

These controls must never be described as equivalent to patch installation.

## 2. Non-negotiable truth boundaries

Always preserve:
- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `UNKNOWN != SAFE`
- `FILTERED != PATCHED`
- `SMBv1 disabled != PATCHED`
- local patch state is independent of remote NSE verdict
- `.56.100` identity = UNKNOWN
- no canonical exploitation/RCE/reverse shell/Meterpreter result
- no completed canonical Case A patch experiment

## 3. Chapter roles

### Chapter 1 — Why the variables matter
Theory and tools only to the depth needed to understand:
- SMB;
- MS17-010;
- measurement signals;
- patch verification;
- mitigation layers.

No canonical experiment result prose.

### Chapter 2 — Why the experiment was designed this way
Explain:
- design choice;
- controlled variable;
- measurement sequence;
- tool choice;
- evidence strategy;
- reproducibility;
- limitations.

No result interpretation beyond measurement criteria.

### Chapter 3 — What was observed
Use:
`question → measurement → observed result → bounded interpretation → next measurement`

No Chapter 4 recommendation/risk conclusion.

### Chapter 4 — What the observations mean
Compare:
- mechanism;
- coverage;
- limitation;
- residual risk;
- operational implication;
- retest need.

No new experimental evidence.

## 4. Required rationale classes

When relevant, prose must state the reason behind:
- platform selection;
- target OS selection;
- Host-Only topology;
- snapshot;
- Nmap/NSE;
- measurement order;
- local patch verification;
- mitigation case selection;
- before/after retesting;
- evidence preservation.

Do not insert a generic "Lý do lựa chọn" paragraph in every subsection. Integrate reasoning naturally.

## 5. Reader-facing style

Prefer:
- "Phép đo này được thực hiện trước ... vì ..."
- "Dữ liệu này trả lời câu hỏi ... nhưng chưa đủ để ..."
- "Để tách biệt hai trạng thái ..., đề tài đối chiếu ..."
- "Sự khác biệt này là cơ sở để thực hiện phép đo tiếp theo ..."
- "Biện pháp này tác động vào ..., trong khi ... được giữ nguyên."

Avoid:
- internal workflow vocabulary;
- QA/gate/evidence-ID language in report prose;
- generic claims such as "tăng cường bảo mật đáng kể";
- repetitive paragraphs that restate table cells;
- tool catalogue prose.

## 6. Source policy

Technical claims:
- use existing verified primary/authoritative sources first;
- any new technical source must enter SOURCE_LEDGER and be verified before publication use.

Structural exemplars:
- may guide organization and reasoning;
- do not automatically become bibliography entries.

## 7. Chapter 1 mandatory correction gate

Before Chapter 1 can pass:
- no sentence may identify Windows 7 as the canonical lab target;
- no sentence may say Metasploit was used in the canonical run;
- no section/table/diagram may claim canonical exploit/RCE validation;
- Windows Server 2012 R2 must be the only canonical target described;
- theory may describe EternalBlue's potential impact, but clearly separate theory from performed experiment.

## 8. Chapter 2 mandatory enrichment gate

The approved 7 H2 / 20 H3 structure is preserved by default.

The chapter must make explicit:
- why Scenario 1 precedes Scenario 2;
- why remote observation and local patch verification are independent;
- why Case B and Case C were chosen as different intervention layers;
- why before/after retest is needed;
- why the evidence set is reproducible.

## 9. Chapter 3 mandatory enrichment gate

Every completed section must:
- have a clear reader question;
- show experiment progression;
- avoid screenshot-album style;
- end with an evidence-bounded conclusion;
- create a natural transition to the next section.

No approved measurement fact may be changed for rhetoric.

## 10. Chapter 4 mandatory enrichment gate

Chapter 4 must answer:
- what risk is actually supported by the evidence;
- what each mitigation changes;
- what it does not change;
- what residual risk remains;
- how patching/protocol hardening/network access control work together;
- what limitations prevent broader generalization;
- what retest is needed.

## 11. Final report quality test

The final report should read as one argument:

`problem → mechanism → measurement design → observations → controlled changes → interpretation → recommendation`

not as:

`theory dump → command list → screenshot list → generic conclusion`.
