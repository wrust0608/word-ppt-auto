# X7E0 — CASE C EVIDENCE & PRESENTATION PLAN

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7e0-ch3-casec-plan`  
Approved integration base: `a64511438d5cb787d55039c067ec52899758f78a`

## 0. Objective

Prepare the evidence and presentation plan for Chapter 3 Section 3.5:

`3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense`

This is **Pass 0 only**.

Your job is to decide how Case C should be presented in the final thesis chapter after inspecting every canonical Case C artifact.

Do not write Section 3.5 prose.
Do not create crops.
Do not assemble Chapter 3.
Do not build Word.

## 1. Start and lineage

Run:

```bash
git fetch origin
git checkout feature/x7e0-ch3-casec-plan
git pull --ff-only origin feature/x7e0-ch3-casec-plan
git status --short
git rev-parse HEAD
git merge-base --is-ancestor a64511438d5cb787d55039c067ec52899758f78a HEAD
```

If lineage is wrong, STOP.

## 2. Mandatory read order

Read fully:

1. `work/do-an/ROADMAP_CURRENT_CH2_CH3_2026_10_07.md`
2. `work/do-an/PROJECT_STATE.md`
3. `work/do-an/CHAPTER_3_CONTRACT.md`
4. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
5. `work/do-an/CHAPTER_3_SECTION_EVIDENCE_MAP.md`
6. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
7. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`
8. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
9. `work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
10. approved Sections 3.1–3.4 only as context:
    - `CH3_31_BASELINE_DRAFT_R1.md`
    - `CH3_32_SCENARIO1_DRAFT_R1.md`
    - `CH3_33_SCENARIO2_DRAFT_R1.md`
    - `CH3_34_CASEB_DRAFT_R1.md`
11. every file under:
    `work/do-an/chapter3/evidence/case_c/`

Do not use historical report prose as experimental truth.

## 3. Inspect every Case C staged artifact

The staged Case C family currently contains 17 files.

### Raw Nmap
- `NSE-SMB-01_ports.gnmap`
- `NSE-SMB-01_ports.nmap`
- `NSE-SMB-01_ports.xml`
- `NSE-SMB-04_ms17010.gnmap`
- `NSE-SMB-04_ms17010.nmap`
- `NSE-SMB-04_ms17010.xml`

### Metadata / lineage
- `RUN4_PAUSE_STATE_REPORT.txt`
- `pfSense_Remediation_Run_Manifest.txt`

### Candidate screenshots — visually inspect all 9
- `pfSense_03_Interface_Assignment.png`
- `pfSense_04_Bridge.png`
- `pfSense_05_Bridge_Filtering.png`
- `pfSense_06_Baseline_Pass_Rule.png`
- `pfSense_07_Block_Rule_Config.png`
- `pfSense_08_Rule_Order.png`
- `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`
- `pfSense_10_Block_Log_CANONICAL.png`
- `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png`

For each screenshot, classify:
- KEEP
- OPTIONAL
- DROP

and explain what unique information it contributes.

Do not select screenshots merely because they exist.

## 4. Canonical Case C story

The section must eventually answer:

**What changed when SMB traffic from Kali to Windows was placed behind a pfSense Transparent Bridge filtering policy, and what remained unchanged on the Windows host?**

The result sequence is:

`topology/control path -> filtering policy -> rule order -> Nmap port retest -> pfSense block log -> MS17 retest -> unchanged local Windows state`

The plan must make this progression visible without turning the section into a screenshot album.

## 5. Locked Case C facts

### Topology / control
- Case C canonical control = **pfSense Transparent Bridge**, not Windows Firewall.
- Kali: `192.168.56.10`
- Windows: `192.168.56.20`
- pfSense bridge path:
  - Kali side -> `CASE_C_KALI / em2`
  - `bridge0`
  - Windows side -> `CASE_C_WINDOWS / em3`
- management network is separate and is not the tested SMB path.
- Windows and Kali tested IPs remain `192.168.56.10/24` and `192.168.56.20/24`.

### Policy
Configured policy:
- BLOCK IPv4 TCP
- source `192.168.56.10`
- destination `192.168.56.20`
- ports 139 and 445
- logging enabled
- placed above the baseline PASS rule.

The configured rule itself is supported by direct configuration/order evidence.

### Canonical Nmap port retest
Raw canonical result:

- host up, ARP response;
- `139/tcp filtered netbios-ssn no-response`;
- `445/tcp filtered microsoft-ds no-response`.

Allowed conclusion:
- from Kali in the Case C topology, TCP 139/445 are observed FILTERED.

Do not say:
- Windows service stopped;
- ports are locally closed;
- patched;
- safe.

### pfSense log
Direct log screenshot supports:
- action = Block;
- interface = CASE_C_KALI;
- source = .56.10;
- destination = .56.20:139 and :445;
- TCP SYN.

Allowed:
`matching SMB SYN traffic was blocked in the pfSense path during the canonical Case C port-scan event.`

### Critical rule-label conflict
This is non-negotiable.

The direct screenshot `pfSense_10_Block_Log_CANONICAL.png` visibly shows the rule label:

`CASE C baseline pass Kali to Windows (100000104)`

The manifest/final closure attributes the traffic to:

`CASE C - Block SMB Kali to Windows (1000000104)`

This conflict is unresolved.

Therefore the final report may NOT say:

> the log screenshot proves the exact named rule "CASE C - Block SMB Kali to Windows" matched.

The configured Block rule and its ordering may be proven by their own configuration screenshots.

The log screenshot proves only the matching SMB SYN traffic was blocked in the pfSense path.

The plan must explicitly describe how this conflict will be presented or bounded.

Do not hide it.

### MS17-010 retest
Raw canonical result:
- host up;
- `445/tcp filtered microsoft-ds`;
- no Host script results;
- no usable vulnerability verdict.

Required classification:

`UNKNOWN / NO USABLE SCRIPT RESULT`

Do not say:
- SAFE;
- NOT VULNERABLE;
- PATCHED;
- false negative;
- script failed because pfSense;
- exact script-internal cause.

The report may state the directly observed 445 FILTERED state and absence of a usable script verdict.

### Local Windows state
Case C final metadata records:
- SMB1=True;
- SMB2=True;
- LanmanServer Running;
- local TCP 139/445 listening;
- patch state UNPATCHED;
- no host-side Case C block rule added.

Use correct provenance.

Do not imply the pfSense screenshots directly prove these Windows-local values.

Core boundary:

`FILTERED != PATCHED`

and network filtering does not rewrite the host's local protocol/patch state.

## 6. Do not reuse bad wording from the final closure

The final bounded closure contains some academically over-strong summary wording.

Do NOT reuse statements equivalent to:
- "eliminating remote exploitable exposure";
- "target remains intrinsically vulnerable";
- bypassing the firewall means exploitation succeeds;
- remediation effectiveness is absolutely verified;
- any risk/effectiveness ranking.

Those belong outside Chapter 3 or exceed the evidence.

Use raw/direct observations and the locked truth matrix instead.

## 7. Timebase boundary

Do not globally align timestamps from Kali, pfSense UI, Windows and host metadata.

Important:
- Kali canonical port scan text shows ~03:20:18;
- pfSense UI shows matching rows ~14:20:18–14:20:19;
- clocks/timezones are not independently normalized.

Allowed:
- corresponding scan/log events are supported by traffic tuple, lineage and observed repeated offset.

Do not write:
- "at exactly the same wall-clock time";
- a synthetic unified timeline across systems.

Prefer to omit displayed timestamps from student-facing prose unless necessary.

## 8. Plan the H3 structure

Section H2 is fixed:

`3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense`

Propose the **smallest natural H3 structure**, preferably 2 H3 unless the evidence genuinely requires 3.

A likely pattern is:

1. configuration/control-path;
2. measured result and local-state cross-check.

But inspect the evidence first and justify your proposal.

Do not mechanically copy Case B's structure if the evidence shape differs.

## 9. Table strategy

Next available table:

`Bảng 3.6`

Prefer **one result-oriented comparison table** if it remains readable.

It should compress the key before/after/control-layer observations rather than duplicate every pfSense setting.

Possible row families to evaluate:
- tested network path/control;
- TCP 139;
- TCP 445;
- pfSense log observation;
- remote MS17-010 result;
- local SMB1 state;
- local service/listener state;
- local patch state.

Do not finalize rows before inspecting all evidence.

A second table is allowed only if one table becomes unreadable or mixes configuration and result concepts badly.

Do not use tables as raw-log dumps.

## 10. Figure strategy

Next available figure:

`Hình 3.9`

Case C is the widest evidence family, but figure count must still be minimal.

Evaluate whether the final section really needs separate visual proof for:

- bridge topology/configuration;
- Block rule configuration/order;
- canonical FILTERED Nmap result;
- pfSense Block log;
- MS17-010 filtered result.

Avoid:
- one image for every setup screen;
- redundant screenshots that are already summarized in a table;
- tiny unreadable multi-screen montages.

Do not create a montage in X7E0.

For every KEEP screenshot propose:
- tentative figure number starting at Hình 3.9;
- exact student-facing purpose;
- whether crop is needed;
- approximate crop rectangle after visual inspection;
- what must remain visible;
- what can be removed.

Do not create the crop yet.

## 11. Figure-selection questions

For each candidate screenshot ask:

1. Does it prove something the table/prose cannot show as efficiently?
2. Will a lecturer immediately understand why this image is present?
3. Is the text readable on A4 after cropping?
4. Is it direct evidence or only context?
5. Does it risk exposing the rule-label conflict incorrectly?
6. Is another selected screenshot already proving the same thing?

KEEP only when the answer justifies the page space.

## 12. Claim-evidence map

Create a Case C claim-evidence map.

For each proposed report claim record:
- claim;
- evidence file(s);
- evidence type:
  - direct raw;
  - direct visual;
  - metadata/lineage;
- maximum allowed wording;
- forbidden inference.

At minimum cover:
- transparent bridge/control path;
- configured block policy;
- block-before-pass ordering;
- filtered 139/445 observation;
- blocked matching SMB SYN traffic;
- unresolved exact named-rule attribution;
- remote MS17 result UNKNOWN;
- unchanged local SMB1/SMB2/service/patch state with correct provenance;
- `FILTERED != PATCHED`.

Do not create internal Evidence IDs for student-facing prose.

## 13. Candidate narrative boundaries

The eventual prose should not claim:

- the Windows SMB service was disabled;
- local 139/445 listeners disappeared;
- Windows was patched;
- Windows SMBv1 was disabled;
- remote SAFE/NOT VULNERABLE;
- exact named-rule match from the log screenshot;
- "pfSense completely eliminates MS17-010";
- bypass means exploit success;
- clocks are synchronized;
- filtered state equals protection at every source/path.

Keep the Case C conclusion empirical:

- the tested path from Kali shows 139/445 filtered;
- matching SMB SYN traffic appears as blocked in pfSense logs;
- local Windows protocol/patch state remains unchanged according to Case C local/closure evidence;
- MS17 remote result remains UNKNOWN.

## 14. Output artifacts — Pass 0 only

Create exactly:

- `work/do-an/CH3_35_CASEC_FIGURE_SELECTION_R1.md`
- `work/do-an/CH3_35_CASEC_PRESENTATION_PLAN_R1.md`
- `work/do-an/CH3_35_CASEC_CLAIM_EVIDENCE_MAP_R1.md`
- `work/do-an/CH3_35_CASEC_PLAN_SELF_REVIEW_R1.md`

Do not create:
- Section 3.5 prose;
- crop manifest;
- derived images;
- Word/PDF;
- Section 3.6/3.7 text.

## 15. Self-review

The self-review must verify:

- all 17 staged Case C files inspected;
- all 9 screenshots visually inspected;
- KEEP/OPTIONAL/DROP decision for every screenshot;
- smallest justified table count;
- smallest justified figure count;
- H3 proposal;
- exact rule-label conflict preserved;
- no named-rule attribution overclaim;
- no timestamp synchronization claim;
- no `FILTERED = PATCHED`;
- no SAFE/NOT VULNERABLE;
- no Windows-local state attributed to pfSense screenshot;
- no Case C result prose accidentally written;
- no Chapter 4 effectiveness/risk ranking.

Do not self-declare external PASS.

Final state:

`X7E0_CASEC_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`

## 16. QA

Run:

```bash
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

You may run `scripts/validate_project.py`, but do not modify project infrastructure if it reports the known manager-prompt Markdown false positive.

No infrastructure changes are allowed.

## 17. Git

Commit:

`plan(ch3): design Case C evidence presentation R1`

Push:

`feature/x7e0-ch3-casec-plan`

Do not merge.

## 18. Handoff

Return:

1. branch;
2. starting SHA;
3. local/remote SHA;
4. files created;
5. full 17-file evidence inspection confirmation;
6. 9-screenshot KEEP/OPTIONAL/DROP table;
7. proposed H3 structure;
8. proposed Bảng 3.6 design;
9. proposed Hình 3.9+ allocation;
10. crop proposals;
11. rule-label-conflict handling;
12. timebase handling;
13. local-state provenance handling;
14. forbidden-claim audit;
15. project QA;
16. clean git status.

Final state:

`X7E0_CASEC_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`

Then STOP.

Do not write Section 3.5 prose.
Do not create crops.
Do not open X7F.
Do not assemble Chapter 3.
Do not build Word.
Do not modify Chapter 2.
Do not open Chapter 4.
