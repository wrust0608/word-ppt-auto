# CHATGPT CURRENT HANDOFF — SMB ACADEMIC PROJECT

Date: 2026-10-06  
Audience: new ChatGPT reviewer/QA chat  
Status: `CURRENT_CANONICAL_HANDOFF`

## 1. Roles

- User: final approver and prompt relay.
- ChatGPT: lecturer/reviewer, technical QA, decision co-owner.
- Antigravity/agent: executor only. It may draft, run commands, crop presentation images and produce QA artifacts, but it must not redefine scope or self-approve.

Primary review perspective:
**Information Security lecturer / thesis-project reviewer.**

Highest standard:
**Đúng kỹ thuật — dễ hiểu — đúng trọng tâm — nhìn ra ngay phần demo — đủ sức bảo vệ trước hội đồng.**

Do not accept agent self-declared PASS without independent inspection.

## 2. Repository and tool rule

Repository:
`wrust0608/word-ppt-auto`

For project state/content:
- use the GitHub connector;
- do not use public web search as a substitute for repository truth.

If current branch/state matters, verify remote branch HEAD before making a decision.

## 3. Current project state

### Chapter 2
- USER APPROVED.
- CONTENT LOCKED.
- Final DOCX PASS.
- Do not reopen unless user explicitly requests it.

### Chapter 3 workflow
Chapter 3 is authored section-by-section.

Current H2 structure:
- 3.1 Baseline
- 3.2 Scenario 1
- 3.3 Scenario 2
- 3.4 Case B
- 3.5 Case C
- 3.6 Comparison
- 3.7 Summary

Workflow:
- X7A = 3.1
- X7B = 3.2
- X7C = 3.3
- X7D = 3.4
- X7E = 3.5
- X7F = 3.6+3.7
- X7G = mechanical assembly
- X7H = full Chapter 3 review

Each section:
1. evidence/presentation plan;
2. external review;
3. user approval;
4. prose draft;
5. external review;
6. user approval;
7. integration;
8. only then next section opens.

## 4. Current exact gate

Current gate:
`X7A1_PASS_WAITING_FOR_USER_APPROVAL`

Section 3.1 R2 executor candidate:
`c2acf1b4bc41c4260f14416fd217b94bf4f829c7`

Reviewer-final Section 3.1 branch HEAD:
`2d4690e8c40c870abd19019c0d51b31456a9229c`

Branch:
`feature/x7a1-ch3-baseline-draft`

Final external review:
`work/do-an/X7A1_CH3_31_EXTERNAL_REVIEW_R2_FINAL.md`

Final score:
`99/100 — PASS`

Blockers:
`0`

The reviewer made one final bounded route-wording micro-fix after executor R2.

**X7B is still BLOCKED.**

Do not integrate/open X7B until the user explicitly approves Section 3.1 prose.

## 5. Section 3.1 locked design

H2:
`3.1. Trạng thái baseline trước đo đạc`

H3:
- `3.1.1. Trạng thái mạng và dịch vụ SMB`
- `3.1.2. Trạng thái bản vá và mốc phục hồi`

Locked tables:
- Bảng 3.1 — Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc
- Bảng 3.2 — Trạng thái bản vá và mốc phục hồi

Locked figures:
- Hình 3.1 — Windows_PreDemo_01_Network_SMB.png
- Hình 3.2 — Windows_PreDemo_02_Firewall.png
- Hình 3.3 — Windows_MS17010_02_Hotfix.png

Next available numbering:
- Bảng 3.3
- Hình 3.4

Presentation crops are already created and externally reviewed.

## 6. Current Section 3.1 artifacts

On:
`feature/x7a1-ch3-baseline-draft`

Read:
- `work/do-an/CH3_31_BASELINE_DRAFT_R1.md`
- `work/do-an/CH3_31_BASELINE_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_31_BASELINE_CROP_MANIFEST_R1.md`
- `work/do-an/chapter3/presentation/3_1/Hinh_3_1_Network_SMB.png`
- `work/do-an/chapter3/presentation/3_1/Hinh_3_2_Firewall.png`
- `work/do-an/chapter3/presentation/3_1/Hinh_3_3_SrvSys_Hotfix.png`

Planning artifacts:
- `work/do-an/CH3_31_BASELINE_FIGURE_SELECTION_R1.md`
- `work/do-an/CH3_31_BASELINE_PRESENTATION_PLAN_R1.md`
- `work/do-an/CH3_31_BASELINE_CLAIM_EVIDENCE_MAP_R1.md`

## 7. Current authorities — read in this order

1. `work/do-an/PROJECT_STATE.md`
2. this file
3. `work/do-an/CHAPTER_3_CONTRACT.md`
4. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
5. `work/do-an/CHAPTER_3_SECTION_EVIDENCE_MAP.md`
6. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
7. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`
8. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
9. `work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
10. `work/do-an/SOURCE_LEDGER.md`
11. `work/do-an/AUTHOR_VOICE.md`
12. current phase-specific external review / prompt.

Historical/superseded if conflicting:
- old detailed Chapter 2/3 structures in `OUTLINE.md`;
- old numbering in `CHAPTERS_2_4_EVIDENCE_MAP.md`;
- monolithic `CHAPTER_3_AUTHORING_CONSTRAINTS.md`;
- `ROADMAP_2_6.md`;
- monolithic X7 full-chapter prompt.

## 8. Canonical lab truth

Platform:
- Oracle VirtualBox only.

Baseline:
- Kali: `192.168.56.10/24`
- Windows Server 2012 R2: `192.168.56.20/24`
- Host-Only `192.168.56.0/24`
- one NIC per VM in final baseline;
- no NAT/Bridged NIC in final baseline;
- no default route.

Windows baseline:
- LanmanServer Running / Automatic
- local TCP 139/445 listening
- SMB1=True
- SMB2=True
- FS-SMB1 Installed
- Windows Firewall enabled
- custom inbound TCP 139/445 allow rule scoped to Kali .56.10
- default File and Printer Sharing group observed disabled

Patch state:
- display FileVersion = `6.3.9600.16384`
- numeric srv.sys = `6.3.9600.16421`
- Microsoft minimum updated = `6.3.9600.18604`
- relevant KB = KB4012213 / KB4012216 or mapped superseding update
- local classification = `UNPATCHED`

Snapshot:
- `Before Demo` exists for both VMs.

## 9. Scenario 1 truth

Sequential B2–B6 survey.

Observed:
- .56.1 up
- .56.10 up
- .56.20 up
- .56.100 up, identity UNKNOWN
- target .56.20 up
- TCP 139/445 OPEN
- fingerprint Windows Server 2008 R2–2012 range
- dialects:
  - NT LM 0.12
  - 2.0.2
  - 2.1
  - 3.0
  - 3.0.2
- remote signing: enabled but not required
- capabilities: use only recorded values
- smb-os-discovery: no usable output

Never infer exact OS from fingerprint alone.
Scenario 1 does not prove MS17-010.

## 10. Scenario 2 truth

NSE01:
- 139/445 open

NSE02:
- SMBv1 + SMB2/3 dialects observed

NSE03:
- signing enabled but not required

NSE04:
- 445 open
- no usable Host script vulnerability verdict
- result = `UNKNOWN / NO USABLE SCRIPT RESULT`

Never call UNKNOWN:
- SAFE
- NOT VULNERABLE
- VULNERABLE
- false negative

Local UNPATCHED and remote UNKNOWN are independent facts.

## 11. Case B truth

Actual action:
`Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`

Observed:
- SMB1 True -> False
- SMB2 remains True
- FS-SMB1 remains Installed
- LanmanServer remains Running
- local listeners remain
- firewall unchanged
- patch state remains UNPATCHED
- remote SMBv1 dialect disappears
- SMB2/3 dialects remain observable
- remote MS17 result remains UNKNOWN

Do not claim:
- patched;
- safe;
- full SMB2/3 workload validation.

## 12. Case C truth

Path:
Kali .56.10 -> pfSense bridge -> Windows .56.20

Management:
Host .57.1 <-> pfSense .57.2

Observed:
- configured block TCP .56.10 -> .56.20 ports 139/445
- rule order shown
- 139/445 from Kali become filtered/no-response
- MS17 remote result = UNKNOWN/inaccessible
- pfSense log directly shows matching .56.10 -> .56.20:139/445 TCP SYN entries with Block action
- local Windows state remains SMB1=True, SMB2=True, LanmanServer Running, local 139/445 listening, UNPATCHED

Critical conflict:
visible firewall log Rule label conflicts with manifest/closure naming.

Therefore:
- allowed: matching SMB SYN traffic was blocked in the pfSense path
- forbidden: screenshot proves the exact named block rule matched

FILTERED != PATCHED.

## 13. Global interpretation locks

Always preserve:
- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `UNKNOWN != SAFE`
- `FILTERED != PATCHED`
- `SMBv1 disabled != PATCHED`
- local patch state != remote NSE verdict
- .56.100 identity remains UNKNOWN

No exploit / reverse shell / Meterpreter / RCE was part of the canonical experiment.

No completed Case A patch experiment exists.

## 14. Timebase and evidence rules

Systems do not share a proven common wall-clock/timezone.

Do not globally sort screenshots/logs by displayed timestamp.

Direct/raw/local/visual evidence outranks:
- summary;
- metadata;
- old report prose.

Case C rule-label conflict must stay visible where relevant.

Do not use old report prose as ground truth.

## 15. Citation policy

Current Section 3.1 correction:
- wrong visible [4]/[5] patch citations were removed.
- internal non-rendering anchor:
  `<!-- CITE-ANCHOR: S005, S032; final IEEE numbering deferred to global normalization gate -->`

Meaning:
- S005 = Microsoft MS17-010 bulletin
- S032 = Microsoft Support verification guide

Do not invent a final numeric IEEE label now.

Global IEEE numbering is deferred to publication-wide normalization.

Do not expose Source IDs in rendered student prose.

## 16. Student-facing voice

Academic Vietnamese.
Neutral third person.
Simple, defendable wording.

Prefer:
- `đề tài`
- `kết quả đo`
- `trạng thái ghi nhận`
- direct observed values.

Avoid:
- audit/governance language
- canonical
- truth matrix
- gate
- evidence layer
- claim IDs / evidence IDs
- corporate QA terminology
- detector-evasion language
- repetitive filler

Chapter 3 = measured results + bounded interpretation.
Chapter 4 = risk/CIA/recommendations/residual risk/strategy.

## 17. Branch model

Accumulation branch:
`feature/ch3-integration`

Current recorded integration HEAD before Section 3.1 completion:
`74a76bdf5f7921849ba38de93135794c8214c7a9`

Do NOT merge Section 3.1 yet.

After explicit user approval of Section 3.1:
1. integrate approved Section 3.1 artifacts into `feature/ch3-integration`;
2. update numbering/current state;
3. only then create X7B0 branch from the new integration HEAD;
4. X7B0 is Scenario 1 evidence/presentation planning only, not prose immediately.

## 18. Immediate next-action rule

At chat start, do not proactively open X7B.

First:
- verify remote HEADs;
- read DEC-60 and the final R2 review;
- understand that Section 3.1 is PASS but waiting for user approval.

If user says `chốt` / approves Section 3.1:
- record user approval;
- integrate Section 3.1;
- update current-state/numbering ledger if needed;
- create X7B0 planning branch from new integration HEAD;
- prepare Scenario 1 plan prompt.

If the user asks to inspect/review Section 3.1:
- inspect reviewer-final HEAD `2d4690e8...`;
- do not regress to executor candidate `c2acf1...`.

## 19. Latest decision record

Latest decision:
`DEC-60 — X7A1 Section 3.1 R2 passes final external review`

Final score:
`99/100 — PASS`

Current state:
`X7A1_PASS_WAITING_FOR_USER_APPROVAL`

This state has priority over earlier DEC entries.
