# X7A0 R2 — CORRECT BASELINE EVIDENCE & PRESENTATION PLAN

Status: `READY_FOR_EXECUTOR`
Branch: `feature/x7a0-ch3-baseline-plan`

## 0. Objective

Correct the X7A0 R1 planning artifacts only.

Do not write Section 3.1 prose.
Do not open X7A1.

Read first:
`origin/main:work/do-an/X7A0_BASELINE_PLAN_EXTERNAL_REVIEW_R1.md`

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7a0-ch3-baseline-plan
git pull --ff-only origin feature/x7a0-ch3-baseline-plan
git status --short
git rev-parse HEAD
```

Current reviewer-cleaned R2 starting HEAD:
`668cc5d697b98cdccd26707289bef4944f9ec320`

Record this as `R2_BASE_SHA` before editing.

Do not trust the R1 handoff SHA. The R1 handoff SHA was incorrect.

## 2. Current authority

Read:

1. `origin/main:work/do-an/PROJECT_STATE.md`
2. `origin/main:work/do-an/X7A0_BASELINE_PLAN_EXTERNAL_REVIEW_R1.md`
3. `origin/main:work/do-an/CHAPTER_3_CONTRACT.md`
4. `origin/main:work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
5. `origin/main:work/do-an/CHAPTER_3_SECTION_EVIDENCE_MAP.md`
6. `origin/main:work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
7. `origin/main:work/do-an/CHAPTER_3_SECTION_CLAIM_MAP_TEMPLATE.md`
8. `origin/main:work/do-an/EVIDENCE_REGISTER.md`
9. current baseline staged evidence and X7A0 R1 files.

The monolithic prompt:
`work/do-an/prompts/X7_DRAFT_CHAPTER_3_WITH_EVIDENCE.md`
is SUPERSEDED / DO NOT EXECUTE.

Do not modify it.

## 3. Files allowed to modify

Modify only:

- `work/do-an/CH3_31_BASELINE_FIGURE_SELECTION_R1.md`
- `work/do-an/CH3_31_BASELINE_PRESENTATION_PLAN_R1.md`
- `work/do-an/CH3_31_BASELINE_CLAIM_EVIDENCE_MAP_R1.md`
- `work/do-an/CH3_31_BASELINE_PLAN_SELF_REVIEW_R1.md`

You may rename their internal status to R2-ready, but do not create a prose draft.

Do not modify:
- staged evidence;
- Chapter 2;
- any old/superseded prompt;
- integration/governance files;
- Scenario 1/2/Case B/Case C material.

## 4. H3 structure

Use exactly:

### 3.1.1. Trạng thái mạng và dịch vụ SMB
### 3.1.2. Trạng thái bản vá và mốc phục hồi

Do not use long audit-style headings.
Do not add English parenthetical labels.

## 5. Student-facing table plan

Replace the one 16-row five-column audit table with two compact report tables.

### Bảng 3.1 — Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc

Use only student-facing columns:

| Hạng mục | Giá trị ghi nhận | Ghi chú |

Candidate rows may include:
- Kali IP / route state;
- Windows IP / route state;
- VirtualBox NIC state;
- LanmanServer;
- FS-SMB1 installed;
- EnableSMB1Protocol;
- EnableSMB2Protocol;
- local signing flags;
- local TCP 139/445 listening;
- Windows Firewall profiles;
- default File and Printer Sharing group disabled;
- custom rule scoped to .56.10.

Do not include:
- artifact filenames;
- Evidence IDs;
- “security significance” column;
- risk/effectiveness language.

### Bảng 3.2 — Trạng thái bản vá và mốc phục hồi

Use:

| Hạng mục | Giá trị ghi nhận | Ghi chú / căn cứ đối chiếu ngắn |

Candidate rows:
- FileVersion String;
- numeric srv.sys;
- Microsoft minimum updated version;
- KB4012213 / KB4012216 mapping;
- observed hotfix inventory wording;
- local classification UNPATCHED;
- Before Demo snapshots.

Do not put raw evidence filenames in the report table design.

## 6. Remove absolute isolation language

Forbidden:
- `ngăn chặn hoàn toàn kết nối ra ngoài Internet`
- `môi trường lab hoàn toàn cô lập`
- `cách ly tuyệt đối 100%`

Allowed:
- one Host-Only NIC per VM;
- no NAT/Bridged NIC in final baseline;
- no default route;
- observed configuration limits VM network paths to the lab segment.

Do not claim every possible host-mediated path is impossible.

## 7. Remove ICMP causality

Do not say:
`ping failed because Windows Firewall blocked ICMP`.

If the connectivity image remains in the plan:
- direct observation only:
  - ARP neighbor .56.20 = REACHABLE;
  - two ICMP Echo requests received no replies.

Recommended:
- keep `Kali_to_Windows_Connectivity.png` OPTIONAL;
- omit ICMP from the main baseline report table because it is not needed to establish the baseline and Scenario 1 later gives cleaner target-availability data.

## 8. Correct bounded technical wording

### LanmanServer
Use:
`Running / Automatic`.

Do not say:
`hoạt động bình thường`.

### Local SMB protocol flags
Use:
- `EnableSMB1Protocol=True`
- `EnableSMB2Protocol=True`

Do not turn this into a remote dialect list.
Remote dialect observations belong to Scenario 1.

### Local signing
Use:
- `EnableSecuritySignature=False`
- `RequireSecuritySignature=False`

Do not call it:
- default OS policy;
- exploit prerequisite;
- remote signing result.

### Local ports
Use:
- `TCP 139/445 listening locally`.

Do not call the local listener row remote `OPEN`.

### Firewall
Allowed:
- custom allow rule covers TCP 139/445 with RemoteAddress .56.10;
- default File and Printer Sharing group observed disabled.

Do not infer:
- all other IPs are definitely blocked by every possible rule.

### Hotfix inventory
Use:
`Observed hotfix inventory does not show KB4012213, KB4012216, or a mapped superseding update containing the MS17-010 fix.`

Do not write:
- all rollups after 2017 are absent;
- exhaustive lifetime update history is known.

### Snapshot
Use:
`Before Demo snapshots are recorded for both VMs as the defined restore point.`

Do not claim perfect/identical reproducibility from the snapshot alone.

## 9. Stable Evidence IDs

Keep section-local Claim IDs:
`BASE-Cxx`

But the Stable Evidence ID column must use only registered IDs.

Use:
- `ENV-CORE-01` — final pre-demo audit;
- `ENV-CORE-02` — Before Demo snapshot verification;
- `ENV-CORE-03` — MS17-010 local patch mapping/state;
- `ENV-CORE-04` — Windows Firewall lab-rule audit;
- `ENV-CORE-05` — Host-Only/NIC configuration.

Remove every:
`BL-xx`

Do not invent a new evidence namespace.

Direct screenshot/file paths remain in the direct artifact column.

## 10. Figure selection — R2 target

After reviewer direct inspection, set:

### KEEP
1. `Windows_PreDemo_01_Network_SMB.png`
   - consolidated local network/route/SMB/listener/numeric version view.

2. `Windows_PreDemo_02_Firewall.png`
   - custom rule, source scope, profiles, default File and Printer Sharing group state.

3. `Windows_MS17010_02_Hotfix.png`
   - display FileVersion + numeric srv.sys + observed hotfix inventory.

### OPTIONAL
At minimum:
- `Windows_MS17010_01_SrvSysVersion.png`
- `Kali_to_Windows_Connectivity.png`
- `Windows_FirewallPrep_04_Scope.png`

### DROP
The remaining low-information/redundant baseline screenshots.

Expected classification:
- KEEP = 3
- OPTIONAL = 3
- DROP = 7

Tentative numbering:
- Hình 3.1 = Windows_PreDemo_01_Network_SMB
- Hình 3.2 = Windows_PreDemo_02_Firewall
- Hình 3.3 = Windows_MS17010_02_Hotfix

Numbers remain tentative until user approval.

## 11. Crop planning

Do not lock pixel coordinates in R2.

For each KEEP image record only:
- source path;
- source SHA-256;
- visual region that must remain;
- irrelevant UI region that may be removed;
- context that must never be cropped out;
- presentation purpose.

Exact pixels will be determined when a derived crop is actually created and source dimensions are programmatically verified.

## 12. Figure caption boundaries

### Hình 3.1
Caption describes:
local network/SMB state shown in the pre-demo PowerShell audit.

Do not claim every table value is visible if the image does not show it.

### Hình 3.2
Caption describes:
Windows Firewall custom rule and source scope.

Do not claim the screenshot proves all other sources are blocked.

### Hình 3.3
Caption describes:
display/numeric srv.sys values and observed hotfix inventory.

Do not put `UNPATCHED` directly in the caption.

UNPATCHED is a combined conclusion from:
- numeric version;
- observed hotfix inventory;
- Microsoft mapping.

## 13. Claim-map corrections

At minimum ensure rows for:
- Kali IP/route;
- Windows IP/route;
- Host-Only NIC state;
- LanmanServer;
- FS-SMB1;
- SMB1/SMB2 local flags;
- local signing flags;
- local 139/445 listeners;
- firewall profile/default-group state;
- custom rule scope;
- display FileVersion;
- numeric srv.sys;
- Microsoft threshold/KB mapping;
- bounded hotfix inventory;
- UNPATCHED classification;
- Before Demo snapshot.

If the ICMP/ARP claim remains internal, phrase only the direct observation and do not include it as a main public-table row.

## 14. Status wording

Do not call the plan:
`PLAN_LOCKED`

before external review/user approval.

Use:
`R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

The self-review may mark individual factual claims VERIFIED if their evidence mapping is valid, but must not self-declare the section plan PASS.

## 15. Scope-cleanliness gate

The R1 agent modified the superseded monolithic X7 prompt to make the repository validator pass.

That archival maintenance has now been handled on `main`.

R2:
- do not touch that file;
- do not touch unrelated files.

At completion:
`git diff --name-only 668cc5d697b98cdccd26707289bef4944f9ec320..HEAD`
must show only the four allowed X7A0 planning artifacts.

## 16. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

Also verify:
- no `CH3_31_BASELINE_DRAFT_R1.md`;
- no evidence byte change;
- `BL-` count = 0 in claim map;
- absolute isolation phrases = 0;
- causal ICMP/firewall statement = 0;
- public table design contains no file/evidence-ID column;
- KEEP/OPTIONAL/DROP = 3/3/7;
- two tables proposed;
- three figures proposed;
- no unrelated file modified.

## 17. Git

Commit:

`fix(ch3): correct baseline evidence plan R2`

Push:

`feature/x7a0-ch3-baseline-plan`

Do not merge.

## 18. Handoff

Return:
1. branch;
2. actual local SHA;
3. actual remote SHA;
4. modified file list;
5. H3 titles;
6. table plan count and names;
7. KEEP/OPTIONAL/DROP counts;
8. tentative figure set;
9. Stable Evidence ID audit;
10. overclaim search gates;
11. patch-state boundary audit;
12. scope-cleanliness audit;
13. QA results;
14. clean status.

Final state:
`X7A0_BASELINE_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Stop.

Do not write Section 3.1 prose.
Do not open X7A1.
