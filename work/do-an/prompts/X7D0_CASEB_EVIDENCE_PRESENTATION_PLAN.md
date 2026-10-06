# X7D0 — CASE B EVIDENCE & PRESENTATION PLAN ONLY

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7d0-ch3-caseb-plan`  
Approved integration base: `f6f3bf39fb9616cbf0d9f8fc3705868d44de7c9d`

## 0. Objective

Prepare the evidence and presentation plan for Chapter 3 Section 3.4 only:

`3.4. Kết quả Case B — Vô hiệu hóa SMBv1 và đo lại từ xa`

Do **not** write Section 3.4 report prose yet.

Case B is a controlled configuration intervention:

`before -> action -> after local -> protocol retest -> MS17-010 retest`

The plan must show what changed and what did **not** change without converting protocol hardening into patching or safety.

Highest reviewer standard:

- technically correct;
- easy for a thesis examiner to follow;
- before/after logic visible immediately;
- compact on A4;
- no screenshot album;
- no command-log style;
- no “SMBv1 disabled = patched/safe” overclaim;
- no “SMB2/3 still visible = workload fully validated” overclaim.

## 1. Start and lineage

Run:

```bash
git fetch origin
git checkout feature/x7d0-ch3-caseb-plan
git pull --ff-only origin feature/x7d0-ch3-caseb-plan
git status --short
git rev-parse HEAD
git merge-base --is-ancestor f6f3bf39fb9616cbf0d9f8fc3705868d44de7c9d HEAD
```

The last command must succeed.

If the branch does not descend from the approved integration commit, STOP.

## 2. Mandatory read order

Read:

1. `work/do-an/PROJECT_STATE.md`
2. `work/do-an/CHAPTER_3_CONTRACT.md`
3. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
4. `work/do-an/CHAPTER_3_SECTION_EVIDENCE_MAP.md`
5. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
6. `work/do-an/CHAPTER_3_SECTION_CLAIM_MAP_TEMPLATE.md`
7. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md` — Case B rows only
8. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
9. `work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
10. `work/do-an/evidence/ALL_2026_10_06/COMMAND_LINEAGE_MATRIX.md` — Case B only
11. `work/do-an/chapter3/CHAPTER_3_RESULT_MATRIX.md` — Case B only
12. `work/do-an/chapter3/CHAPTER_3_EVIDENCE_INDEX.md` — Case B only
13. `work/do-an/AUTHOR_VOICE.md`
14. approved `work/do-an/CHAPTER_2.md` — Case B method only
15. approved `work/do-an/CH3_31_BASELINE_DRAFT_R1.md` — patch-state continuity only
16. approved `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md` — SMB protocol baseline continuity only
17. approved `work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md` — pre-intervention NSE state only
18. all Case B staged evidence under:
    `work/do-an/chapter3/evidence/case_b/`

Do not use historical report prose or old remediation summary text as experimental truth.

Evidence priority:

`direct raw/local/visual > metadata lineage > historical/support > old summary prose`.

## 3. Evidence isolation and staged-file audit

Inspect **all 12 currently staged Case B files**:

### Raw protocol retest triplet
- `NSE-SMB-02_protocols.nmap`
- `NSE-SMB-02_protocols.xml`
- `NSE-SMB-02_protocols.gnmap`

### Raw MS17-010 retest triplet
- `NSE-SMB-04_ms17010.nmap`
- `NSE-SMB-04_ms17010.xml`
- `NSE-SMB-04_ms17010.gnmap`

### Direct screenshots
- `SMBv1_Remediation_01_Before.png`
- `SMBv1_Remediation_02_Action.png`
- `SMBv1_Remediation_03_After_Local.png`
- `SMBv1_Remediation_04_NSE02_Protocols.png`
- `SMBv1_Remediation_05_NSE04_MS17010.png`

### Metadata
- `SMBv1_Remediation_Run_Manifest.txt`

Visually inspect all 5 screenshots.

### Mandatory discrepancy audit

The manifest references:

`SMBv1_Remediation_06_Raw_Evidence.png`

but this file is **not present in the canonical staged Case B folder**.

Do not:
- invent it;
- create it;
- count it as a staged screenshot;
- cite it as direct evidence;
- treat the manifest’s `EXPECTED: 6 / ACTUAL: 6` line as proof that six staged screenshots exist.

Record this as a **metadata/staging discrepancy** in the internal plan/self-review.

The canonical plan must rely on the 12 staged files actually present.

## 4. Locked Case B facts

### 4.1 Before intervention

Direct screenshot records:

- `LanmanServer` = Running;
- `FS-SMB1` = Installed;
- `EnableSMB1Protocol = True`;
- `EnableSMB2Protocol = True`.

This is the immediate local pre-intervention state.

Do not infer more than the visible/configured facts.

### 4.2 Action

Direct screenshot / command lineage records:

`Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`

Maximum conclusion:

- the configuration command was executed;
- the subsequent after-state confirms the intended SMB1 server setting changed.

Do not call this:
- patch installation;
- feature uninstall;
- driver update;
- OS update.

### 4.3 After local state

Direct screenshot records:

- `EnableSMB1Protocol = False`;
- `EnableSMB2Protocol = True`;
- `FS-SMB1 = Installed`;
- `LanmanServer = Running`.

Therefore:

- SMBv1 is disabled at the SMB server configuration level;
- SMB2 remains enabled;
- the Windows feature remains installed;
- LanmanServer remains running.

Critical lock:

`SMBv1 disabled != FS-SMB1 uninstalled`.

Critical lock:

`SMBv1 disabled != PATCHED`.

Do not claim:
- all SMB2/3 workloads were validated;
- no user/business interruption occurred;
- service continuity was fully proven.

### 4.4 Protocol retest

Direct raw Case B `smb-protocols` output records:

- `445/tcp open`;
- `NT LM 0.12 (SMBv1)` is absent;
- remaining recorded dialects:
  - `2.0.2`
  - `2.1`
  - `3.0`
  - `3.0.2`.

Allowed conclusion:

- SMBv1 no longer appears in the measured remote dialect list;
- the listed SMB2/3 dialects remain observable from Kali.

Do not say:
- TCP 445 closed;
- “SMBv1 removed from the operating system”;
- all modern SMB workloads are healthy;
- interoperability is fully validated.

### 4.5 MS17-010 retest

Direct raw output records:

- target up;
- `445/tcp open`;
- output reaches `Nmap done`;
- no `Host script results:` block appears.

Required classification:

`UNKNOWN / NO USABLE SCRIPT RESULT`

Keep:

`UNKNOWN != SAFE`.

Do not use the manifest phrase:

`SMBv1 probe silenced`

as a factual causal explanation.

That phrase is metadata interpretation and is **not established by the raw output**.

Do not invent:
- “Couldn't negotiate SMBv1”;
- NTSTATUS;
- IPC$ cause;
- script failure;
- safe/not vulnerable/patched verdict.

### 4.6 Patch state

Approved Section 3.1 remains authoritative:

`UNPATCHED`.

Case B changes SMBv1 configuration; it does not install the OS patch.

Keep separate:

- protocol configuration state;
- Windows feature installation state;
- local patch state;
- remote NSE verdict.

Do not merge these into one “security state”.

## 5. Before/after comparison discipline

Case B is the first controlled intervention section.

The report should make the change easy to see:

### Before
- SMB1=True
- SMB2=True
- FS-SMB1=Installed
- LanmanServer=Running
- pre-intervention remote dialect list included SMBv1, as already approved in Sections 3.2/3.3
- remote MS17 result = UNKNOWN, as already approved in Section 3.3

### Action
- SMB1 server configuration set to False.

### After
- SMB1=False
- SMB2=True
- FS-SMB1=Installed
- LanmanServer=Running
- remote dialect retest no longer lists NT LM 0.12
- 2.0.2 / 2.1 / 3.0 / 3.0.2 remain observable
- remote MS17 result remains UNKNOWN
- local patch classification remains UNPATCHED

The plan may use approved earlier-section results for the “before” comparison, but must not duplicate earlier screenshots unnecessarily.

## 6. Interpretation boundary

Allowed Chapter 3 wording concepts:

- “thay đổi cấu hình SMBv1 quan sát được”;
- “sau can thiệp, SMBv1 không còn xuất hiện trong danh sách phương ngữ của phép đo lại”;
- “SMB2/3 vẫn được ghi nhận trong phép đo lại”;
- “trạng thái bản vá cục bộ vẫn được phân loại UNPATCHED”;
- “kết quả NSE MS17-010 từ xa vẫn UNKNOWN”.

Avoid Chapter 4 conclusions such as:

- “biện pháp hiệu quả”;
- “giảm rủi ro”;
- “an toàn hơn”;
- “đã khắc phục lỗ hổng”;
- “đã loại bỏ nguy cơ”;
- security ranking.

Section 3.4 should report **observed before/after effects**, not a final effectiveness judgment.

## 7. Command-lineage lock

Case B action command:

`Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`

Retest operator commands from manifest do not contain `--privileged`.

Raw Nmap-recorded argv contains `--privileged`.

Keep provenance layers separate.

Do not invent:
- `sudo`;
- `-Pn`;
- reboot commands;
- feature-uninstall commands;
- patch-install commands.

If exact Nmap commands are unnecessary in Chapter 3 presentation, prefer measurement labels.

## 8. Timebase discipline

Do not compare Windows screenshot clock, Kali Nmap raw timestamps and host manifest timestamp as if they share one wall clock/timezone.

Use:
- Case B run lineage;
- Before / Action / After filenames;
- manifest sequence;
- raw command/output correspondence.

Do not construct a synthetic cross-system timestamp chronology.

## 9. Redundancy with Sections 3.1–3.3

Case B should not repeat entire earlier evidence.

Explicitly evaluate:

- whether the dedicated `Before` screenshot is still useful or redundant with approved pre-intervention sections;
- whether `Action` deserves a figure or is better expressed in prose/table;
- whether `After_Local` is the highest-value local figure;
- whether `NSE02_Protocols` is the highest-value remote figure because it shows SMBv1 disappearance;
- whether `NSE04_MS17010` is redundant with Section 3.3 Hình 3.6 and better summarized in the table.

Important visual fact:

`SMBv1_Remediation_05_NSE04_MS17010.png` contains both the protocol retest and the MS17-010 retest in one terminal screenshot.

Evaluate whether that makes it more useful than the separate NSE02 image, or whether its density hurts A4 readability.

Do not automatically retain all five screenshots.

## 10. Required output A — figure selection

Create:

`work/do-an/CH3_34_CASEB_FIGURE_SELECTION_R1.md`

For all 5 screenshots record:

| File | Case B stage | Directly shows | Unique vs earlier sections? | Better as table? | Before/after value | Legibility | Crop needed? | KEEP / OPTIONAL / DROP | Reason |
|---|---|---|---|---|---|---|---|---|---|

Selection principles:

- evidence value, not screenshot count;
- make the controlled change visible;
- avoid repeating Section 3.1–3.3 figures;
- retain enough visual evidence for a defense panel to understand the intervention and its measured consequence.

Next available numbering:

- **Bảng 3.5**
- **Hình 3.7**

Numbers remain tentative until external review + user approval.

## 11. Required output B — presentation plan

Create:

`work/do-an/CH3_34_CASEB_PRESENTATION_PLAN_R1.md`

Do not write final prose.

### 11.1 Reader question

State one sentence that Section 3.4 must answer.

The question should center on:

- what changed when SMBv1 server configuration was disabled;
- what remained unchanged locally;
- what changed in the remote dialect measurement;
- what the MS17-010 retest did and did not establish.

### 11.2 Proposed H3 structure

Choose the smallest useful structure.

Strong candidate to evaluate:

- local before/action/after configuration;
- remote retest and bounded comparison.

Do not create one H3 per screenshot or command.

### 11.3 Proposed table(s)

At minimum consider one compact before/action/after/retest table.

A useful shape to evaluate:

`Giai đoạn | Thuộc tính / phép đo | Trước can thiệp | Sau can thiệp / retest | Giới hạn kết luận`

or another A4-readable structure.

The table must make these distinctions visible:

- SMB1 True -> False;
- SMB2 True -> True;
- FS-SMB1 Installed -> Installed;
- LanmanServer Running -> Running;
- remote NT LM 0.12 present before -> absent in Case B retest;
- SMB2/3 dialects still recorded;
- 445 remains OPEN in retests;
- remote MS17 result UNKNOWN before -> UNKNOWN after;
- local patch state remains UNPATCHED.

Do not imply that a value not directly re-measured after intervention was “unchanged” unless canonical evidence supports it.

Do not turn the table into a raw command list.

### 11.4 Figure placement

For each KEEP figure specify:

- tentative figure number;
- exact reader observation before the image;
- direct result after the image;
- what the image does **not** prove.

### 11.5 Before/after comparison wording

Plan explicit wording boundaries:

Allowed:
- “SMB1 True -> False”
- “NT LM 0.12 present before / not present in the Case B protocol retest”
- “SMB2/3 dialects listed in the retest remain observable”

Forbidden:
- “SMBv1 vulnerability removed”
- “MS17-010 fixed”
- “system safe”
- “all SMB functionality preserved”
- “zero downtime”
- “no business impact”

### 11.6 Transition to Case C

Provide only a conceptual transition.

Meaning:

- Case B changes host protocol configuration;
- the next case examines a different intervention layer: network-path filtering/control;
- do not reveal Case C results.

Do not evaluate which mitigation is “better” in Chapter 3.

## 12. Required output C — claim-evidence map

Create:

`work/do-an/CH3_34_CASEB_CLAIM_EVIDENCE_MAP_R1.md`

Use the current claim-map template.

At minimum create separate internal claims for:

- before SMB1=True;
- before SMB2=True;
- before FS-SMB1 Installed;
- before LanmanServer Running;
- action command executed;
- after SMB1=False;
- after SMB2=True;
- after FS-SMB1 still Installed;
- after LanmanServer Running;
- SMB1 disabled != feature uninstalled;
- SMB1 disabled != patched;
- Case B protocol retest 445 OPEN;
- NT LM 0.12 absent from retest;
- 2.0.2/2.1/3.0/3.0.2 recorded in retest;
- remaining dialects do not prove workload validation;
- Case B MS17-010 retest no usable Host script result;
- remote classification remains UNKNOWN;
- UNKNOWN != SAFE;
- local patch state remains UNPATCHED;
- local UNPATCHED and remote UNKNOWN remain independent.

Do not use the manifest’s unsupported `SMBv1 probe silenced` phrase as a claim.

Internal IDs must not be designed for student-facing prose.

## 13. Required output D — plan self-review

Create:

`work/do-an/CH3_34_CASEB_PLAN_SELF_REVIEW_R1.md`

Report:

- staged Case B file count = 12;
- raw triplets inspected = 2;
- screenshots visually inspected = 5;
- manifest inspected = 1;
- missing/non-staged `SMBv1_Remediation_06_Raw_Evidence.png` discrepancy;
- KEEP / OPTIONAL / DROP counts;
- proposed H3 count;
- proposed table count;
- proposed figure count;
- claim-map row count;
- before/action/after traceability audit;
- SMB1 False vs FS-SMB1 Installed distinction audit;
- SMB1 disabled vs PATCHED audit;
- SMB2/3 workload-overclaim audit;
- protocol retest audit;
- MS17 retest UNKNOWN audit;
- `UNKNOWN != SAFE` audit;
- local UNPATCHED audit;
- command-lineage audit;
- timebase audit;
- no Case C leakage;
- no Chapter 4 effectiveness/risk leakage;
- unresolved presentation questions.

Do not self-declare external PASS.

Final executor state:

`X7D0_CASEB_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`

## 14. Crop policy

X7D0 is planning-only.

Do not create presentation crops yet.

For every KEEP/OPTIONAL screenshot that would benefit from cropping, record:

- source path;
- source SHA-256;
- source dimensions;
- provisional `x, y, width, height`;
- required content to preserve;
- safe-to-remove UI/background;
- A4 readability reason;
- interpretation boundary.

Do not create composites or montages unless explicitly approved later.

Do not annotate images.

Original evidence bytes must remain unchanged.

## 15. Academic reviewer test

Before handoff, test the design as if defending before an Information Security lecturer.

Without repository knowledge, the reader must be able to answer:

1. What was the SMB1/SMB2 state immediately before intervention?
2. What exact setting was changed?
3. What was the local SMB1/SMB2/feature/service state afterward?
4. Was the SMB1 Windows feature uninstalled?
5. Did the local patch state change?
6. What changed in the remote dialect retest?
7. What remained observable after intervention?
8. Did TCP 445 remain reachable?
9. Did the MS17-010 script produce a usable verdict afterward?
10. Why does disabling SMB1 not equal PATCHED or SAFE?
11. Why does observing SMB2/3 dialects not prove full workload continuity?

If the proposed design cannot answer these directly, revise it.

## 16. Student-facing style constraints

Future Section 3.4 must read like an undergraduate Information Security experimental-results section.

Prefer:

- “trước can thiệp”;
- “sau can thiệp”;
- “kết quả đo lại”;
- “ghi nhận”;
- “không còn xuất hiện trong danh sách phương ngữ”;
- “trạng thái bản vá cục bộ vẫn được phân loại UNPATCHED”.

Avoid:

- canonical;
- ground truth;
- gate;
- governance;
- Evidence ID;
- Claim ID;
- audit layer;
- “mitigation effective”;
- “risk reduced”;
- “safe”;
- “fully compatible”;
- “no downtime”.

Do not write like a remediation compliance memo.

## 17. Forbidden in X7D0

Do not create:

- `CH3_34_CASEB_DRAFT_R1.md`;
- final Section 3.4 prose;
- presentation crop files;
- Case C plan/prose;
- Section 3.5;
- comparison/synthesis;
- Chapter 4;
- final DOCX.

Do not modify:

- approved Sections 3.1–3.3;
- source evidence bytes;
- Experimental Truth Matrix;
- R3 locks;
- numbering ledger;
- Chapter 2.

## 18. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

Additionally verify:

- no Section 3.4 draft file exists;
- no presentation crop was created;
- all 12 staged Case B files inspected;
- all 5 screenshots visually inspected;
- the non-staged `SMBv1_Remediation_06_Raw_Evidence.png` is not treated as evidence;
- no Case C evidence used;
- no `PATCHED` classification for Case B;
- no SAFE / NOT VULNERABLE;
- no false-negative language;
- no invented `Couldn't negotiate SMBv1`;
- no invented NTSTATUS/IPC$ cause;
- no workload-continuity claim;
- no feature-uninstall claim;
- no reboot claim;
- no operator/raw argv conflation;
- no Chapter 4 effectiveness/risk conclusion.

## 19. Git

Allowed new files only:

- `work/do-an/CH3_34_CASEB_FIGURE_SELECTION_R1.md`
- `work/do-an/CH3_34_CASEB_PRESENTATION_PLAN_R1.md`
- `work/do-an/CH3_34_CASEB_CLAIM_EVIDENCE_MAP_R1.md`
- `work/do-an/CH3_34_CASEB_PLAN_SELF_REVIEW_R1.md`

Commit:

`plan(ch3): design caseB evidence presentation R1`

Push:

`feature/x7d0-ch3-caseb-plan`

Do not merge.

## 20. Handoff

Return:

1. branch;
2. starting SHA;
3. local/remote SHA;
4. created file list;
5. staged file count;
6. screenshot selection summary;
7. H3 structure;
8. table design;
9. figure design;
10. before/action/after presentation decision;
11. remote protocol-retest presentation decision;
12. MS17-010 retest presentation decision;
13. missing `SMBv1_Remediation_06_Raw_Evidence.png` discrepancy handling;
14. SMB1-disabled-vs-patched boundary audit;
15. workload-overclaim audit;
16. command-lineage audit;
17. claim-map row count;
18. QA results;
19. clean git status.

Final state:

`X7D0_CASEB_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`

Then STOP.

Do not open X7D1.
Do not write Section 3.4.
Do not open X7E.
Do not write Chapter 4.
