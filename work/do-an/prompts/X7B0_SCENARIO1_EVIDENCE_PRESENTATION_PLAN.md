# X7B0 — SCENARIO 1 EVIDENCE & PRESENTATION PLAN ONLY

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7b0-ch3-scenario1-plan`  
Base integration commit: `59ba232634046eba7d436607d09b3ec007f03a6f`

## 0. Objective

Prepare the evidence and presentation plan for Chapter 3 Section 3.2 only:

`3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB`

Do **not** write Section 3.2 report prose yet.

This phase must independently determine how the B2–B6 measurement sequence should be presented to a thesis reader. Do not inherit a rigid layout from Section 3.1.

The reviewer standard is not merely repository correctness. The proposed presentation must satisfy a lecturer / thesis-defense reader:

- technically correct;
- easy to understand without repository knowledge;
- focused on the actual experiment;
- makes the demo sequence immediately visible;
- avoids screenshot-album presentation;
- avoids audit/QA/internal-engineering style.

## 1. Start and lineage

Run:

```bash
git fetch origin
git checkout feature/x7b0-ch3-scenario1-plan
git pull --ff-only origin feature/x7b0-ch3-scenario1-plan
git status --short
git rev-parse HEAD
git merge-base --is-ancestor 59ba232634046eba7d436607d09b3ec007f03a6f HEAD
```

The final command must succeed.

If this branch does not descend from integration commit
`59ba232634046eba7d436607d09b3ec007f03a6f`,
STOP.

## 2. Mandatory read order

Read:

1. `work/do-an/PROJECT_STATE.md`
2. `work/do-an/CHAPTER_3_CONTRACT.md`
3. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
4. `work/do-an/CHAPTER_3_SECTION_EVIDENCE_MAP.md`
5. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
6. `work/do-an/CHAPTER_3_SECTION_CLAIM_MAP_TEMPLATE.md`
7. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`
8. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
9. `work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
10. `work/do-an/chapter3/CHAPTER_3_RESULT_MATRIX.md` — Scenario 1 rows only
11. `work/do-an/chapter3/CHAPTER_3_EVIDENCE_INDEX.md` — Scenario 1 rows only
12. `work/do-an/AUTHOR_VOICE.md`
13. `work/do-an/CHAPTER_2.md` — Scenario 1 method only
14. approved Section 3.1 draft only as continuity context:
    `work/do-an/CH3_31_BASELINE_DRAFT_R1.md`

Do not use superseded monolithic X7 instructions, old Chapter 3 numbering, or historical report prose as experimental truth.

## 3. Evidence isolation

Inspect the Scenario 1 evidence family under:

`work/do-an/chapter3/evidence/scenario1/`

Inspect **all staged Scenario 1 files**, not only PNG screenshots.

The staged family includes:

- B2 host discovery: `b2_host_discovery.*`
- B3 target alive: `b3_target_alive.*`
- B4 SMB ports: `b4_smb_ports.*` + `Scenario1_B4_SMB_Ports.png`
- B5 service/version: `b5_smb_version.*` + `Scenario1_B5_SMB_Version.png`
- B6 SMB NSE: `b6_smb_nse.*` + `Scenario1_B6_SMB_NSE_A.png`
- `Scenario1_Run_Manifest.txt` for lineage/context only.

Do not inspect or use Scenario 2, Case B or Case C evidence.

Approved Section 3.1 facts may be used only as background continuity where necessary.

## 4. Locked Scenario 1 facts

The plan must preserve these facts exactly unless direct raw evidence shows a narrower formulation is required.

### B2 — host discovery

Observed up:
- `192.168.56.1`
- `192.168.56.10`
- `192.168.56.20`
- `192.168.56.100`

Identity of:
- `192.168.56.100` = **UNKNOWN**

Do not identify .56.100 by inference, metadata, MAC guess, historical prose or later topology.

### B3 — target alive

- target `192.168.56.20` observed up.

B3 may be redundant in presentation if B2 plus subsequent B4 already communicates the progression sufficiently. Decide academically; do not retain a separate visual merely because the step exists.

### B4 — TCP 139/445

- `139/tcp OPEN`
- `445/tcp OPEN`

This is a remote Nmap observation from the Kali vantage point.

Lock:
`445 OPEN != vulnerable`.

Do not turn OPEN into MS17-010 confirmation.

### B5 — service/version fingerprint

Allowed fingerprint:
`Microsoft Windows Server 2008 R2–2012`

This is an Nmap fingerprint range only.

Do **not** claim B5 remotely identifies the host exactly as Windows Server 2012 R2.

The exact Windows Server 2012 R2 identity comes from controlled lab context/local evidence, not from this fingerprint alone.

### B6 — SMB NSE profile

Observed dialects:
- `NT LM 0.12`
- `2.0.2`
- `2.1`
- `3.0`
- `3.0.2`

Remote signing:
- enabled but not required.

Capabilities:
- report only values directly recorded in raw evidence;
- do not expand capability meaning beyond output.

`smb-os-discovery`:
- **NO USABLE OUTPUT**

Do not convert lack of output into:
- unsupported;
- failed because of a specific cause;
- Windows version proof;
- vulnerability verdict.

Scenario 1 does **not** conclude MS17-010.

## 5. Required output A — figure selection

Create:

`work/do-an/CH3_32_SCENARIO1_FIGURE_SELECTION_R1.md`

Inspect all Scenario 1 visual candidates and the raw outputs behind them.

For every staged PNG/JPG candidate, record:

| File | Step | Directly shows | Unique information? | Better as table? | Legibility | Crop needed? | KEEP / OPTIONAL / DROP | Reason |
|---|---|---|---|---|---|---|---|---|

Current staged screenshots are B4, B5 and B6. Do not assume all three must be retained.

Also explicitly evaluate the absence of dedicated B2/B3 screenshots:
- whether raw-result table presentation is sufficient;
- whether creating a new derived visual from raw text would add real academic value;
- do not fabricate screenshots.

Selection rule:
- choose by information value, not file count;
- prefer a table when a result is short and easily compared;
- retain a screenshot when the original tool output materially improves credibility or understanding;
- avoid consecutive images that repeat the same facts.

Numbering begins from:
- next table: **Bảng 3.3**
- next figure: **Hình 3.4**

Numbers are tentative in X7B0 and become locked only after external review + user approval.

## 6. Required output B — Scenario 1 presentation plan

Create:

`work/do-an/CH3_32_SCENARIO1_PRESENTATION_PLAN_R1.md`

Design Section 3.2 without writing final report paragraphs.

### 6.1 Reader question

State in one sentence what Section 3.2 must answer for a thesis reader.

The section should read as a measured discovery sequence, not as an Nmap command log.

### 6.2 Proposed H3 structure

Decide the smallest useful H3 structure after evidence inspection.

Do not create one H3 for every B2–B6 step by default.

Prefer grouping that reflects the intellectual flow, for example:
- host/port discovery;
- service/protocol characterization;

but choose the final proposal from evidence and readability.

### 6.3 Proposed table(s)

For every proposed table specify:
- tentative number;
- exact reader question answered;
- columns;
- rows;
- which B2–B6 observations appear;
- which evidence supports each row;
- what should remain out of the table;
- whether the table replaces the need for a screenshot.

At least one compact result table should be considered for the B2–B6 sequence.

Do not dump raw Nmap text into cells.

No file paths, Evidence IDs or Claim IDs in the student-facing table design.

### 6.4 Figure placement

For each KEEP figure specify:
- tentative figure number;
- what the sentence before the figure should direct the reader to observe;
- what direct result may be stated after the figure;
- which conclusion the image does **not** prove.

### 6.5 B2/B3 redundancy decision

Make an explicit decision:
- retain both as separate reported steps;
- merge their explanation;
- or let B3 act only as continuity confirmation.

Explain the choice from a lecturer-reader perspective.

### 6.6 B5 fingerprint handling

Explicitly plan wording so the fingerprint remains:
`Microsoft Windows Server 2008 R2–2012`

Do not convert it to exact Windows Server 2012 R2 identification.

### 6.7 B6 negative/limited output handling

Plan how to present:
- dialect list;
- signing result;
- recorded capabilities;
- `smb-os-discovery: no usable output`.

The absence of usable `smb-os-discovery` output should be visible if it helps explain the completeness/limits of the measurement, but it must not dominate the section.

### 6.8 Transition

Provide only the conceptual transition from Scenario 1 to Scenario 2.

Do not write final prose.

The transition should make clear that service/protocol enumeration is not itself an MS17-010 verdict; the vulnerability-oriented NSE measurements are handled separately in 3.3.

## 7. Required output C — claim-evidence map

Create:

`work/do-an/CH3_32_SCENARIO1_CLAIM_EVIDENCE_MAP_R1.md`

Use the current claim-map template.

At minimum include claims for:
- B2 discovered hosts;
- .56.100 UNKNOWN identity;
- B3 target alive;
- 139/tcp OPEN;
- 445/tcp OPEN;
- B5 fingerprint range;
- each recorded B6 dialect grouping;
- remote signing enabled but not required;
- capabilities actually recorded;
- smb-os-discovery no usable output;
- explicit limit that Scenario 1 does not establish MS17-010.

Internal evidence identifiers belong here, not in student prose.

## 8. Required output D — plan self-review

Create:

`work/do-an/CH3_32_SCENARIO1_PLAN_SELF_REVIEW_R1.md`

Report:
- number of Scenario 1 staged files inspected;
- raw triplets inspected for B2–B6;
- screenshot count inspected;
- KEEP / OPTIONAL / DROP counts;
- proposed H3 count;
- proposed table count;
- proposed figure count;
- claim-map row count;
- B2/B3 duplication decision;
- .56.100 identity audit;
- B5 fingerprint-boundary audit;
- B6 signing/dialect/capability audit;
- smb-os-discovery negative-output audit;
- MS17-010 overclaim audit;
- evidence-isolation audit;
- unresolved presentation questions.

Do not self-declare PASS.

Final executor state:
`X7B0_SCENARIO1_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`

## 9. Crop policy

X7B0 is planning-only.

Do not create presentation crops yet.

If a crop is recommended, record:
- source path;
- source SHA;
- source dimensions if available;
- proposed rectangle/content to preserve;
- content that must not be removed;
- reason the crop improves A4 readability.

Original evidence bytes must remain unchanged.

## 10. Academic reviewer test

Before handoff, test the proposed design as if defending before an Information Security lecturer.

Without repository knowledge, a reader must be able to answer:

1. What sequence of measurements was performed?
2. Which hosts were observed and which target was examined further?
3. Were TCP 139 and 445 remotely open?
4. What did Nmap actually say about service/version — and how precise was that fingerprint?
5. Which SMB dialects and signing state were observed?
6. What did `smb-os-discovery` fail to provide?
7. Why does none of this by itself prove MS17-010?

If the reader needs internal IDs, filenames or audit terminology to understand the result, redesign the presentation.

## 11. Student-facing style constraints

The future Section 3.2 must look like a personal academic project report, not an internal QA artifact.

Therefore the plan must avoid student-facing:
- canonical;
- ground truth;
- truth matrix;
- gate;
- governance;
- Evidence ID;
- Claim ID;
- evidence layer;
- L1/L2/L3/L4/L5;
- repository paths.

Tables should be compact enough for A4.

Figures should be evidence, not decoration.

Do not force identical paragraph/formula structure from Section 3.1.

## 12. Forbidden in X7B0

Do not create:
- `CH3_32_SCENARIO1_DRAFT_R1.md`;
- final prose for 3.2;
- presentation crop images;
- Scenario 2 prose/plan;
- Case B/C content;
- synthesis;
- Chapter 4;
- final DOCX.

Do not modify:
- approved Section 3.1 artifacts;
- source evidence bytes;
- Experimental Truth Matrix;
- R3 locks.

## 13. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

Additionally verify:
- no Section 3.2 draft file exists;
- no evidence byte changed;
- all B2–B6 raw artifacts were inspected;
- all Scenario 1 screenshots were visually inspected;
- no later-section evidence was used;
- no exact identity assigned to .56.100;
- no exact OS claim inferred from B5;
- no MS17-010 verdict appears.

## 14. Git and stop condition

Allowed new files:
- `CH3_32_SCENARIO1_FIGURE_SELECTION_R1.md`
- `CH3_32_SCENARIO1_PRESENTATION_PLAN_R1.md`
- `CH3_32_SCENARIO1_CLAIM_EVIDENCE_MAP_R1.md`
- `CH3_32_SCENARIO1_PLAN_SELF_REVIEW_R1.md`

Commit:
`plan(ch3): design scenario1 evidence presentation R1`

Push:
`feature/x7b0-ch3-scenario1-plan`

Do not merge.

Stop after handoff and wait for independent external review.
