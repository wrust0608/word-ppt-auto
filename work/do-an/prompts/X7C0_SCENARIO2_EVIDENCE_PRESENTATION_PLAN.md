# X7C0 — SCENARIO 2 EVIDENCE & PRESENTATION PLAN ONLY

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7c0-ch3-scenario2-plan`  
Approved integration base: `e4b59086f32084752f3df1f3733fa05a407816d7`

## 0. Objective

Prepare the evidence and presentation plan for Chapter 3 Section 3.3 only:

`3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE`

Do **not** write Section 3.3 report prose yet.

Scenario 2 is not a continuation of Scenario 1 screenshot layout. It consists of four separate NSE measurements:

- NSE-SMB-01 — TCP 139/445 reachability
- NSE-SMB-02 — SMB dialects
- NSE-SMB-03 — SMB signing
- NSE-SMB-04 — MS17-010 NSE script

The plan must determine how to present these results to a thesis reader with special care for the negative/indeterminate NSE-SMB-04 result.

Highest reviewer standard:

- technically correct;
- immediately understandable to a thesis examiner;
- compact on A4;
- evidence-led rather than command-led;
- explicit about uncertainty;
- no conversion of `UNKNOWN` into a security verdict;
- no QA/audit-report style in student-facing design.

## 1. Start and lineage

Run:

```bash
git fetch origin
git checkout feature/x7c0-ch3-scenario2-plan
git pull --ff-only origin feature/x7c0-ch3-scenario2-plan
git status --short
git rev-parse HEAD
git merge-base --is-ancestor e4b59086f32084752f3df1f3733fa05a407816d7 HEAD
```

The last command must succeed.

If this branch does not descend from the approved integration commit, STOP.

## 2. Mandatory read order

Read:

1. `work/do-an/PROJECT_STATE.md`
2. `work/do-an/CHAPTER_3_CONTRACT.md`
3. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
4. `work/do-an/CHAPTER_3_SECTION_EVIDENCE_MAP.md`
5. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
6. `work/do-an/CHAPTER_3_SECTION_CLAIM_MAP_TEMPLATE.md`
7. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md` — Scenario 2 rows
8. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
9. `work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
10. `work/do-an/evidence/ALL_2026_10_06/COMMAND_LINEAGE_MATRIX.md` — Scenario 2 rows
11. `work/do-an/chapter3/CHAPTER_3_RESULT_MATRIX.md` — Scenario 2 rows only
12. `work/do-an/chapter3/CHAPTER_3_EVIDENCE_INDEX.md` — Scenario 2 rows only
13. `work/do-an/AUTHOR_VOICE.md`
14. approved `work/do-an/CHAPTER_2.md` — Section 2.4 only
15. approved `work/do-an/CH3_31_BASELINE_DRAFT_R1.md` — local patch context only
16. approved `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md` — continuity/redundancy comparison only

Do not use historical report prose as ground truth.

Evidence priority:

`direct raw/visual > metadata/manifest > historical/support > old report prose`.

## 3. Evidence isolation

Inspect **all 17 staged Scenario 2 files** under:

`work/do-an/chapter3/evidence/scenario2/`

Expected family:

### NSE-SMB-01
- `NSE-SMB-01_ports.nmap`
- `NSE-SMB-01_ports.xml`
- `NSE-SMB-01_ports.gnmap`
- `Scenario2_NSE01_Ports.png`

### NSE-SMB-02
- `NSE-SMB-02_protocols.nmap`
- `NSE-SMB-02_protocols.xml`
- `NSE-SMB-02_protocols.gnmap`
- `Scenario2_NSE02_Protocols.png`

### NSE-SMB-03
- `NSE-SMB-03_signing.nmap`
- `NSE-SMB-03_signing.xml`
- `NSE-SMB-03_signing.gnmap`
- `Scenario2_NSE03_Signing.png`

### NSE-SMB-04
- `NSE-SMB-04_ms17010.nmap`
- `NSE-SMB-04_ms17010.xml`
- `NSE-SMB-04_ms17010.gnmap`
- `Scenario2_NSE04_MS17010.png`

### Context
- `Scenario2_Run_Manifest.txt`

Do not inspect Case B or Case C evidence in X7C0.

Approved Section 3.1 and 3.2 may be used only for:
- continuity;
- redundancy assessment;
- independent local patch-state cross-reference.

## 4. Locked Scenario 2 facts

### NSE-SMB-01 — ports

Direct raw observation:

- target `192.168.56.20` up;
- `139/tcp OPEN`;
- `445/tcp OPEN`;
- reason: `syn-ack ttl 128`.

Maximum conclusion:
- TCP 139/445 were remotely reachable/open from Kali at this measurement.

Forbidden:
- vulnerability;
- authenticated SMB access;
- exploitation readiness;
- firewall causality.

Lock:
`445 OPEN != vulnerable`.

### NSE-SMB-02 — protocols

Direct raw observation:

- `445/tcp open`;
- `smb-protocols` records:
  - `NT LM 0.12 (SMBv1) [dangerous, but default]`
  - `2.0.2`
  - `2.1`
  - `3.0`
  - `3.0.2`.

Maximum conclusion:
- SMBv1 and the listed SMB2/3 dialects were observed from Kali.

Forbidden:
- SMBv1 presence = MS17-010;
- exploitability;
- "dangerous" = vulnerability verdict.

Lock:
`SMBv1 enabled != MS17-010 confirmed`.

### NSE-SMB-03 — signing

Direct raw observation:

- `445/tcp open`;
- `smb2-security-mode`;
- dialect shown: `3.0.2`;
- `Message signing enabled but not required`.

Maximum conclusion:
- this is the remote script observation for signing on the recorded dialect/output.

Do not generalize to every SMB dialect.

Do not reconcile it with local PowerShell signing flags.

Lock:
local signing observation and remote signing observation are independent facts.

### NSE-SMB-04 — MS17-010

Direct raw observation:

- command invokes `smb-vuln-ms17-010`;
- target up;
- `445/tcp open`;
- scan completes;
- **no Host script results / no vulnerability verdict is printed**.

Required remote classification:

`UNKNOWN / NO USABLE SCRIPT RESULT`

This classification is an evidence interpretation, not a literal Nmap word printed on screen.

Forbidden classifications:
- VULNERABLE
- SAFE
- NOT VULNERABLE
- PATCHED
- FALSE NEGATIVE
- exploit succeeded / exploit failed
- any invented NTSTATUS
- any invented reason for the missing script output

Do not say the script "failed" unless direct output contains an error. The direct output shows a completed scan without a usable script verdict.

Lock:
`UNKNOWN != SAFE`.

## 5. Independent local patch state

Approved baseline Section 3.1 records local patch classification:

`UNPATCHED`

This is an independent local fact.

Scenario 2 must keep two separate axes:

- remote NSE-SMB-04 result = `UNKNOWN / NO USABLE SCRIPT RESULT`;
- local patch state = `UNPATCHED`.

Forbidden:
- UNPATCHED => remotely VULNERABLE;
- remote UNKNOWN => SAFE/PATCHED;
- disagreement => false negative;
- using one axis to overwrite the other.

The plan must explicitly decide the cleanest student-facing way to show this distinction:
- bounded prose;
- one compact comparison row/table;
- or another minimal design.

Do not create an audit-style matrix unless it materially improves reader comprehension.

## 6. Command-lineage lock

Do not merge operator command text with Nmap-recorded argv.

Scenario 2 operator commands are defined in Chapter 2 / manifest.

For NSE-SMB-02/03/04:
- operator/screenshot command does **not** contain `--privileged`;
- raw Nmap-recorded argv contains normalized `--privileged`.

These are two provenance layers.

Do not "correct" one into the other.

If exact commands are not necessary for Chapter 3 presentation, prefer method/script labels rather than command duplication.

Do not invent `sudo`, `-Pn`, or any other option.

## 7. Redundancy with approved Section 3.2

Scenario 2 repeats some observations already seen in Scenario 1:

- NSE-SMB-01 overlaps with Section 3.2 B4 ports;
- NSE-SMB-02 overlaps with Section 3.2 B6 dialects;
- NSE-SMB-03 overlaps with Section 3.2 B6 signing.

Do not automatically remove them: they are defined independent Scenario 2 measurements.

But do not make the report feel duplicated.

The presentation plan must decide:

- which repeated results belong in a compact table;
- which screenshots still add independent evidentiary value;
- whether NSE01/02/03 images are redundant enough to DROP/OPTIONAL;
- which figure best demonstrates the Scenario 2-specific point.

In particular, assess NSE-SMB-04 separately:
its sparse screenshot may have high evidentiary value because it visibly shows:
- the `smb-vuln-ms17-010` script was invoked;
- TCP 445 remained open;
- the scan completed;
- no Host script result/verdict was emitted.

Do not assume sparse output = low-value image.

## 8. Required output A — figure selection

Create:

`work/do-an/CH3_33_SCENARIO2_FIGURE_SELECTION_R1.md`

Inspect all four screenshots visually and all raw triplets.

For every screenshot record:

| File | Measurement | Directly shows | Unique vs Section 3.2? | Better as table? | Negative-result value? | Legibility | Crop needed? | KEEP / OPTIONAL / DROP | Reason |
|---|---|---|---|---|---|---|---|---|---|

Do not retain all four merely because four exist.

Do not drop NSE-SMB-04 merely because it lacks a Host script block.

Numbering starts from:

- next table: **Bảng 3.4**
- next figure: **Hình 3.6**

Numbers are tentative until external review + user approval.

## 9. Required output B — presentation plan

Create:

`work/do-an/CH3_33_SCENARIO2_PRESENTATION_PLAN_R1.md`

Do not write final prose.

### 9.1 Reader question

State in one sentence what Section 3.3 must answer.

A suitable intellectual question is not simply "What commands were run?"

It should center on:
- what the dedicated NSE measurements observed;
- what the MS17-010 script did and did not establish;
- how remote UNKNOWN coexists with local UNPATCHED.

### 9.2 Proposed H3 structure

Choose the smallest useful H3 structure after inspecting evidence.

Do not default to one H3 per NSE command.

Possible conceptual grouping to evaluate:
- SMB preconditions/protocol characteristics (NSE01–03);
- MS17-010 script result and interpretation boundary (NSE04 + local patch cross-reference).

This is only a candidate. Decide from evidence/readability.

### 9.3 Proposed table(s)

At least consider one compact result table covering NSE01–04.

For each proposed table specify:
- tentative number;
- exact reader question;
- columns;
- rows;
- direct evidence;
- allowed interpretation;
- what must stay out.

Possible result-oriented columns:

`Phép đo | Nội dung kiểm tra | Kết quả ghi nhận | Giới hạn kết luận`

Do not include raw command strings unless essential.

Do not include internal Evidence IDs/Claim IDs/file paths in student-facing tables.

Explicitly evaluate whether a second tiny comparison table for:

`Remote NSE verdict = UNKNOWN` vs `Local patch state = UNPATCHED`

adds real value. If bounded prose is cleaner, do not create the table.

### 9.4 Figure placement

For each KEEP figure specify:
- tentative number;
- what the sentence before it tells the reader to inspect;
- what may be stated after it;
- what it does **not** prove.

For NSE-SMB-04, distinguish:
- visible fact: command invoked + completed scan + no Host script result block;
- classification: `UNKNOWN / NO USABLE SCRIPT RESULT`;
- forbidden inference: safe/not vulnerable/vulnerable.

### 9.5 Negative-result presentation

Create a dedicated plan subsection for NSE-SMB-04.

The reader must understand:

1. The script was actually invoked.
2. The scan completed normally.
3. No usable Host script verdict appeared.
4. Therefore the remote classification is UNKNOWN.
5. UNKNOWN is not SAFE.
6. Local UNPATCHED is a separate fact and does not convert UNKNOWN into VULNERABLE.
7. No cause for absent script output is established.

Do not use the term "false negative".

### 9.6 Transition to Case B

Provide only the conceptual transition.

Do not write final prose.

The transition should establish that after the baseline measurements, the next experimental section changes one controlled factor — SMBv1 configuration — and repeats selected measurements.

Do not reveal Case B results.

## 10. Required output C — claim-evidence map

Create:

`work/do-an/CH3_33_SCENARIO2_CLAIM_EVIDENCE_MAP_R1.md`

Use the current claim-map template.

At minimum include separate claims for:

- NSE01 TCP 139 OPEN;
- NSE01 TCP 445 OPEN;
- `445 OPEN != vulnerable`;
- NSE02 five dialects;
- SMBv1 presence does not establish MS17-010;
- NSE03 remote signing result;
- local signing vs remote signing independence;
- NSE04 command/script actually invoked;
- NSE04 scan completed;
- no usable Host script output;
- remote verdict = UNKNOWN;
- UNKNOWN != SAFE;
- local patch baseline = UNPATCHED;
- local UNPATCHED != remote vulnerability verdict;
- Scenario 2 contains no exploit/RCE result.

Internal IDs belong only here.

Do not invent external citations for direct observations.

## 11. Required output D — plan self-review

Create:

`work/do-an/CH3_33_SCENARIO2_PLAN_SELF_REVIEW_R1.md`

Report:

- Scenario 2 staged file count inspected;
- raw triplets inspected = 4;
- screenshots visually inspected = 4;
- KEEP / OPTIONAL / DROP counts;
- proposed H3 count;
- proposed table count;
- proposed figure count;
- claim-map row count;
- redundancy-with-3.2 audit;
- command-lineage audit;
- NSE01 port-boundary audit;
- NSE02 SMBv1/MS17 boundary audit;
- NSE03 signing-layer audit;
- NSE04 no-output audit;
- `UNKNOWN != SAFE` audit;
- local `UNPATCHED` vs remote `UNKNOWN` independence audit;
- no false-negative language;
- no exploit/RCE leakage;
- evidence-isolation audit;
- unresolved presentation questions.

Do not self-declare external PASS.

Final executor state:

`X7C0_SCENARIO2_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`

## 12. Crop policy

X7C0 is planning-only.

Do not create presentation crops yet.

If a crop is recommended, record:
- source path;
- source SHA-256;
- source dimensions;
- provisional `x, y, width, height`;
- required content to preserve;
- content safe to remove;
- reason for A4 readability;
- interpretation boundary.

Original evidence bytes must remain unchanged.

For an NSE-SMB-04 crop, the command line and completed-scan context must remain visible if the figure is intended to support the no-verdict observation.

## 13. Timebase discipline

Do not compare Scenario 2 wall-clock timestamps with Windows/local baseline timestamps to infer causal chronology.

The defined NSE01→NSE04 procedure order may be described from run lineage.

Do not global-sort evidence from different systems by displayed time.

## 14. Academic reviewer test

Before handoff, test the proposed design as if defending before an Information Security lecturer.

Without repository knowledge, the reader must be able to answer:

1. Were TCP 139/445 reachable during Scenario 2?
2. Which SMB dialects were observed?
3. What did the remote signing script report?
4. Was `smb-vuln-ms17-010` actually executed?
5. Did it print a usable vulnerability verdict?
6. What exactly does UNKNOWN mean here?
7. Why is UNKNOWN not SAFE?
8. Why does local UNPATCHED not equal a remote VULNERABLE verdict?
9. Why is no exploitation result claimed?

If the presentation requires internal IDs or governance vocabulary to understand these answers, redesign it.

## 15. Student-facing style constraints

Future Section 3.3 must read like an undergraduate Information Security thesis result section.

Avoid student-facing:
- canonical;
- ground truth;
- truth matrix;
- gate;
- governance;
- Evidence ID;
- Claim ID;
- evidence layer;
- L1/L2/L3/L4/L5;
- repository paths;
- audit-report terminology.

Prefer:
- “kết quả đo”;
- “ghi nhận”;
- “quan sát từ xa”;
- “không có đầu ra khả dụng”;
- “chưa đủ căn cứ kết luận”.

Do not write:
- “scan chứng minh an toàn”;
- “không vulnerable”;
- “false negative”;
- “script thất bại” without direct error evidence.

## 16. Forbidden in X7C0

Do not create:
- `CH3_33_SCENARIO2_DRAFT_R1.md`;
- final Section 3.3 prose;
- presentation crop images;
- Case B plan/prose;
- Case C content;
- synthesis;
- Chapter 4;
- DOCX.

Do not modify:
- approved Section 3.1/3.2 artifacts;
- source evidence bytes;
- Experimental Truth Matrix;
- R3 locks;
- numbering ledger.

## 17. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

Additionally verify:

- no Section 3.3 draft file exists;
- no evidence byte changed;
- all 17 Scenario 2 staged files inspected;
- all four screenshots visually inspected;
- no Case B/C evidence used;
- no `VULNERABLE` result attributed to NSE-SMB-04;
- no `SAFE` / `NOT VULNERABLE`;
- no `FALSE NEGATIVE`;
- no invented NTSTATUS;
- no cause invented for missing output;
- no local/remote signing reconciliation;
- local UNPATCHED kept independent from remote UNKNOWN;
- no exploitation/RCE claim;
- no operator-command / raw-argv conflation.

## 18. Git

Allowed new files:

- `work/do-an/CH3_33_SCENARIO2_FIGURE_SELECTION_R1.md`
- `work/do-an/CH3_33_SCENARIO2_PRESENTATION_PLAN_R1.md`
- `work/do-an/CH3_33_SCENARIO2_CLAIM_EVIDENCE_MAP_R1.md`
- `work/do-an/CH3_33_SCENARIO2_PLAN_SELF_REVIEW_R1.md`

Commit:

`plan(ch3): design scenario2 evidence presentation R1`

Push:

`feature/x7c0-ch3-scenario2-plan`

Do not merge.

## 19. Handoff

Return:

1. branch;
2. starting SHA;
3. local/remote SHA;
4. created file list;
5. staged file count inspected;
6. screenshot selection summary;
7. proposed H3 structure;
8. table design summary;
9. figure design summary;
10. NSE04 negative-result presentation decision;
11. local UNPATCHED vs remote UNKNOWN presentation decision;
12. command-lineage audit;
13. claim-map row count;
14. technical-boundary audit;
15. QA results;
16. clean git status.

Final state:

`X7C0_SCENARIO2_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`

Then STOP.

Do not open X7C1.
Do not write Section 3.3.
Do not open X7D.
Do not write Chapter 4.
