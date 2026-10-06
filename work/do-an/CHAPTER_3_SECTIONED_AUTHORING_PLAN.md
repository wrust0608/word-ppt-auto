# CHAPTER 3 SECTIONED AUTHORING PLAN

Status: `LOCKED_FOR_SECTIONED_WORKFLOW`  
Date: 2026-10-06  
Primary review role: Lecturer / thesis-project reviewer in Information Security.

## 1. Decision

The previous monolithic X7 drafting approach is superseded.

Chapter 3 will be authored and externally reviewed **section by section** because the evidence structure differs materially between:
- baseline;
- Scenario 1;
- Scenario 2;
- Case B;
- Case C;
- final comparison.

This workflow is designed to prevent:
- image overload;
- reuse of one rigid layout for unlike experiments;
- result leakage across sections;
- interpretation drift;
- premature synthesis before each evidence block is individually understood.

## 2. High-level structure remains stable

# CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH

## 3.1. Trạng thái baseline trước đo đạc
## 3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB
## 3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010
## 3.4. Kết quả Case B — Vô hiệu hóa SMBv1
## 3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense
## 3.6. So sánh kết quả thực nghiệm
## 3.7. Tổng kết chương

The detailed H3 structure may be refined **inside each section** after reviewing that section's evidence.

Do not globally force every section into the same number of H3, tables or screenshots.

## 3. Section-by-section workflow

### X7A — 3.1 Baseline
Purpose:
- establish the starting condition;
- show what was verified locally before measurements;
- establish local patch state and restore point.

Evidence family:
- final pre-demo audit;
- Windows local SMB/service state;
- firewall scope;
- srv.sys / hotfix state;
- Before Demo snapshot;
- Host-Only configuration.

Likely presentation:
- one compact baseline table;
- 2–3 selected screenshots;
- short explanation of local patch classification.

No Scenario 1/2 results.

### X7B — 3.2 Scenario 1
Purpose:
- narrate the sequential discovery/scanning workflow as measured results.

Evidence family:
- B2 host discovery;
- B3 target alive;
- B4 TCP 139/445;
- B5 service/version;
- B6 SMB NSE profile;
- final Scenario 1 screenshots.

Likely presentation:
- one result table aligned to B2–B6;
- screenshots chosen by information value, likely B4/B5/B6;
- direct explanation of open ports, fingerprint range, dialects, signing, capabilities;
- .56.100 remains UNKNOWN.

This section may use more figures than baseline because the output changes across steps.

### X7C — 3.3 Scenario 2
Purpose:
- present four independent NSE measurements;
- make the negative/inconclusive MS17-010 result understandable.

Evidence family:
- NSE-SMB-01 through NSE-SMB-04 raw triplets;
- final Scenario 2 screenshots;
- local patch baseline only for cross-check.

Likely presentation:
- one 4-row measurement table;
- selected screenshots from protocol/signing/MS17-010;
- explicit remote UNKNOWN vs local UNPATCHED distinction.

This section should not copy Scenario 1 content except where needed for continuity.

### X7D — 3.4 Case B
Purpose:
- show controlled before/action/after state;
- show protocol-level retest after SMBv1 disable.

Evidence family:
- before local state;
- action;
- after local state;
- smb-protocols retest;
- smb-vuln-ms17-010 retest.

Likely presentation:
- before/after comparison table;
- paired local-state screenshot(s);
- protocol retest screenshot;
- optional MS17 screenshot if it adds value.

This section is a **state-transition** narrative, not a scan-sequence narrative.

### X7E — 3.5 Case C
Purpose:
- show the network-control mechanism and its measured effect.

Evidence family:
- interface assignment;
- bridge;
- bridge filtering;
- block rule config;
- rule order;
- port retest;
- firewall log;
- MS17 retest;
- local Windows state.

Likely presentation:
- one configuration/result table or two smaller tables if readability requires;
- rule-order/config image;
- filtered Nmap result;
- firewall Block log;
- MS17-010 result if necessary;
- explicit bounded rule-label conflict.

This is the widest evidence section and may legitimately use the most figures.

### X7F — 3.6 + 3.7 Synthesis
Purpose:
- compare only already-reviewed observations;
- summarize Chapter 3.

Evidence family:
- outputs locked from X7A–X7E only.

Likely presentation:
- one comparison matrix;
- no new raw evidence;
- no new screenshots unless external review explicitly requests one.

No risk ranking or recommendation.

## 4. Isolation rule

Each phase may read:
- its own staged evidence family;
- shared baseline facts needed for interpretation;
- R3 evidence locks;
- AUTHOR_VOICE;
- Chapter 2 method section corresponding to that phase.

Each phase should **not** read or use later-phase evidence unless explicitly required for a bounded comparison.

Example:
- X7B Scenario 1 must not use Case B or Case C results.
- X7C Scenario 2 may use local patch baseline only because its purpose includes remote/local cross-check.
- X7D Case B may compare to baseline and its own retest only.
- X7E Case C may compare to baseline and its own retest only.
- X7F may use only the externally approved outputs of X7A–X7E.

## 5. Artifact model

Each phase produces:
- one section draft;
- one section self-review;
- one section figure-selection note.

Naming:

- `CH3_31_BASELINE_DRAFT_R1.md`
- `CH3_31_BASELINE_FIGURE_SELECTION.md`
- `CH3_31_BASELINE_SELF_REVIEW.md`

Then analogously for 3.2, 3.3, 3.4, 3.5.

X7F produces:
- `CH3_36_37_SYNTHESIS_DRAFT_R1.md`
- self-review.

Only after all sections pass external review will they be mechanically assembled into:
`CHAPTER_3_DRAFT_R1.md`

Assembly must preserve approved section prose; no wholesale rewrite during stitching.

## 6. Figure policy

There is **no global fixed figure count** anymore.

Each section selects figures according to:
- information value;
- directness of evidence;
- legibility;
- non-duplication;
- whether a table can communicate the same result better.

For wide screenshots:
- keep original evidence bytes untouched;
- derived crop may be created only for presentation;
- crop must preserve all fields required for the claim;
- record source filename and crop purpose in the section figure-selection note;
- never crop away context that changes the interpretation.

Do not use screenshots simply because they exist.

## 7. Table policy

Tables are section-specific.

A table should be used when it makes multiple observations easier to compare.

Do not force:
- one table per H3;
- identical column structure across different demos;
- raw log content into table cells.

Every table must answer a reader question.

## 8. Academic reader test

Before a section can pass, a lecturer who did not follow the repo process must be able to answer:

1. What was being measured?
2. What was actually observed?
3. Which image/table supports it?
4. What conclusion is justified?
5. What conclusion is not justified?
6. How does this section connect to the next experiment?

If any answer requires reading internal evidence-index terminology, the section is not ready.

## 9. Chapter 3 / Chapter 4 boundary

Chapter 3:
- measured result;
- direct local/remote comparison;
- bounded interpretation;
- factual change before/after.

Chapter 4:
- risk;
- CIA;
- effectiveness judgment;
- solution ranking;
- enterprise recommendation;
- residual risk;
- patch strategy;
- broader lessons.

## 10. Global technical locks

Always preserve:
- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `UNKNOWN != SAFE`
- `FILTERED != PATCHED`
- `SMBv1 disabled != PATCHED`
- .56.100 identity = UNKNOWN;
- local patch state independent of remote NSE signal;
- Case C exact named-rule attribution unresolved;
- no exploitation/RCE/reverse shell/Meterpreter in canonical experiment;
- no Case A patch experiment.

## 11. Gate progression

X7A PASS -> open X7B  
X7B PASS -> open X7C  
X7C PASS -> open X7D  
X7D PASS -> open X7E  
X7E PASS -> open X7F  
X7F PASS -> assemble Chapter 3  
Assembled Chapter 3 -> external review -> user review -> final DOCX.

Do not skip gates.
