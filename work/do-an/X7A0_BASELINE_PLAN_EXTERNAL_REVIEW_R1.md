# X7A0 EXTERNAL REVIEW R1 — BASELINE EVIDENCE & PRESENTATION PLAN

Date: 2026-10-06  
Branch: `feature/x7a0-ch3-baseline-plan`  
Remote candidate HEAD: `9cf53d151896b0e7ff75f5e13a4b8e85b90efdb9`  
Verdict: `81/100 — REVISE_BLOCKING / NO PROSE YET`

## 1. Executive finding

The candidate is useful and should be revised, not discarded.

Strong work:
- all 13 baseline screenshots were inventoried;
- screenshot spam was actively reduced;
- patch-state distinction between display FileVersion and numeric srv.sys was preserved;
- no 3.1 prose was created;
- no evidence byte was changed;
- the candidate correctly stopped before X7A1.

However, the plan cannot be approved yet because:
1. the planned student-facing table still looks like an internal audit table;
2. multiple claims overstate what the evidence proves;
3. Stable Evidence IDs were replaced by invented BL-* IDs;
4. the proposed figure set is not optimal after direct reviewer inspection;
5. an out-of-scope superseded prompt was modified;
6. the handoff reported the wrong remote commit SHA.

## 2. Score

| Category | Score |
|---|---:|
| Scope discipline | 9/15 |
| Evidence inventory / image review | 18/20 |
| Student-facing presentation design | 12/20 |
| Technical claim accuracy | 16/20 |
| Claim/evidence traceability | 9/15 |
| Governance / numbering discipline | 9/10 |
| QA / handoff accuracy | 8/10 |
| **Total** | **81/100** |

Blockers: 5 substantive classes + 1 handoff defect.

## 3. PASS — evidence inventory

The 13-image inventory is complete.

The following DROP decisions are sound:
- Kali NSE help image;
- basic Winver image;
- isolated low-density Windows service/feature/config images;
- partial firewall screenshot where stronger final audit screenshots exist.

The anti-screenshot-spam principle is correct.

## 4. BLOCKER A — public table design is too audit-like and too wide

Current Bảng 3.1 proposal has five columns:
- parameter block;
- audit attribute;
- observed value;
- evidence file;
- security significance / technical boundary.

This is inappropriate for the student-facing report.

Problems:
- raw evidence filenames should remain in the internal claim map, not in the report table;
- “security significance” starts drifting toward Chapter 4;
- five verbose columns plus 16 rows will be difficult to read in A4 portrait with HUIT margins;
- terminology such as “kiểm toán”, “Single Source of Truth”, “audit attribute” makes the report sound like internal QA.

Required R2 design:

### Bảng 3.1 — Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc
Recommended columns:
- Hạng mục
- Giá trị ghi nhận
- Ghi chú

### Bảng 3.2 — Trạng thái bản vá và mốc phục hồi
Recommended columns:
- Hạng mục
- Giá trị ghi nhận
- Ghi chú / căn cứ đối chiếu ngắn

No evidence filenames in visible report tables.
No Evidence IDs in visible report tables.
No risk/effectiveness judgment.

Two smaller tables are preferred over one 16-row five-column table.

## 5. BLOCKER B — absolute network-isolation wording

Remove statements equivalent to:
- “ngăn chặn hoàn toàn kết nối ra ngoài Internet”;
- “môi trường lab hoàn toàn cô lập về mặt định tuyến IP”;
- “cách ly tuyệt đối 100%”.

Allowed:
- final baseline records one Host-Only NIC per VM;
- no NAT/Bridged NIC is configured for the two VMs;
- no default route is present;
- therefore the observed VM configuration limits their network path to the lab segment.

Do not claim every possible host-mediated escape path is impossible.

## 6. BLOCKER C — ICMP causality is not directly proven

Current plan/claim map says the ping packets were dropped “do chính sách tường lửa”.

Direct evidence supports:
- two ICMP Echo attempts received no replies / 100% loss;
- neighbor entry for .56.20 is REACHABLE.

It does not directly prove which Windows Firewall rule caused the lack of ICMP reply.

Required:
- either omit the ICMP row from the public baseline table;
- or phrase only the direct observation:
  `ARP neighbor state was REACHABLE while the two ICMP Echo requests received no replies.`

Do not assign cause.

Recommended: omit this row from the main baseline table because it adds noise and Scenario 1 later establishes remote target availability more clearly.

## 7. BLOCKER D — several other claims overreach

Correct these:

### LanmanServer
Current:
“dịch vụ đang hoạt động bình thường”

Use:
`LanmanServer = Running; StartType = Automatic`.

No workload-health claim.

### SMB1/SMB2 local configuration
Current wording implies exact SMB2/SMB3 dialect negotiation from local enable flags.

Use only:
`EnableSMB1Protocol=True; EnableSMB2Protocol=True`.

Actual remote dialect list belongs to Scenario 1.

### Local SMB signing
Remove “chính sách mặc định của hệ điều hành”.

Use only the observed local configuration:
`EnableSecuritySignature=False; RequireSecuritySignature=False`.

Keep it separate from remote signing result in Scenario 1/2.

### Local ports
Use:
`TCP 139/445 are listening locally`.

Do not call this remote `OPEN`.

### Firewall scope
The custom rule is scoped to source `.56.10`.

Do not infer from that single rule:
“all other source IPs are blocked”.

Allowed:
- custom allow rule applies to TCP 139/445 from .56.10;
- default File and Printer Sharing group was observed disabled.

### Hotfix inventory
Current:
“completely absent all rollups from 2017 onward”.

Too broad.

Use:
`Observed hotfix inventory does not show KB4012213, KB4012216, or a mapped superseding update containing the MS17-010 fix.`

Do not claim exhaustive knowledge of every update ever installed beyond the observed inventory.

### Snapshot
Avoid “ensures identical reproducibility”.

Use:
`Before Demo snapshots were recorded for both VMs and provide the defined restore point for the experiment.`

## 8. BLOCKER E — invented Stable Evidence IDs

The claim map labels the “Stable Evidence ID” column with:
`BL-01 ... BL-16`.

These are not the locked stable IDs.

Current registered baseline IDs are:
- `ENV-CORE-01` — final pre-demo audit;
- `ENV-CORE-02` — Before Demo snapshot verification;
- `ENV-CORE-03` — MS17-010 local patch mapping/state;
- `ENV-CORE-04` — Windows Firewall lab-rule audit;
- `ENV-CORE-05` — Host-Only/NIC configuration.

Required:
- keep section-local Claim IDs `BASE-Cxx` if useful;
- replace BL-* in the Stable Evidence ID column with the registered ENV-CORE IDs;
- keep direct screenshot/file paths in the direct-artifact column.

No new evidence-ID namespace may be invented during section drafting.

## 9. Figure-set decision after direct reviewer inspection

Reviewer independently opened the 13 baseline screenshots.

R2 recommended KEEP set:

### Tentative Hình 3.1
`Windows_PreDemo_01_Network_SMB.png`

Purpose:
- consolidated visual of Windows network/local route, LanmanServer state, FS-SMB1, SMB server flags, local 139/445 listeners and numeric srv.sys.

Do not claim values not visibly shown in the cropped frame.

### Tentative Hình 3.2
`Windows_PreDemo_02_Firewall.png`

Purpose:
- custom rule properties;
- source scope .56.10;
- profiles enabled;
- default File and Printer Sharing group disabled.

### Tentative Hình 3.3
`Windows_MS17010_02_Hotfix.png`

Purpose:
- display FileVersion;
- numeric srv.sys version;
- observed hotfix inventory in one image.

The Action Center popup is presentation noise only and may be removed later by a derived crop without altering evidence content.

Move:
`Windows_MS17010_01_SrvSysVersion.png`
to OPTIONAL because Hình 3.3 already contains the version information plus hotfix inventory.

Keep:
`Kali_to_Windows_Connectivity.png`
as OPTIONAL only; do not use it in R2 public plan unless there is a clear reader need.

Recommended classification after R2:
- KEEP = 3;
- OPTIONAL = 3;
- DROP = 7.

No global figure number is locked yet.

## 10. Crop policy correction

The R1 plan hard-codes approximate pixel coordinates and even contains a Y coordinate exceeding the stated image height in one place.

Do not lock pixel crop rectangles in X7A0 R2.

Record instead:
- source path;
- source SHA-256;
- visual region to preserve;
- context that must not be removed;
- crop purpose.

Exact pixel crop is decided only when the derived presentation image is actually created and its source dimensions are programmatically verified.

## 11. H3 titles — simplify

Use the simpler, student-facing titles already proposed before the agent expanded them:

### 3.1.1. Trạng thái mạng và dịch vụ SMB
### 3.1.2. Trạng thái bản vá và mốc phục hồi

Do not use:
- “kiểm toán” in public heading;
- parenthetical English labels;
- long multi-concept heading strings.

Windows Firewall belongs naturally inside 3.1.1.

## 12. Handoff / scope defect

The candidate handoff reported:
`9cf53d10a402327732ad57f8976b32dc96f5b721`

Actual remote branch HEAD is:
`9cf53d151896b0e7ff75f5e13a4b8e85b90efdb9`.

Use the remote branch HEAD as authority.

The agent also modified:
`work/do-an/prompts/X7_DRAFT_CHAPTER_3_WITH_EVIDENCE.md`

during X7A0, even though that monolithic prompt is superseded and outside the section-plan deliverables.

The path bug in that archival prompt was real, but maintenance should be handled in governance scope, not silently committed by X7A0.

Reviewer has corrected this on `main` by:
- explicitly marking the old prompt SUPERSEDED / DO NOT EXECUTE;
- fixing its archival Markdown image links there.

R2 should sync current governance rather than independently edit the old prompt.

## 13. What should remain unchanged

Keep:
- sectioned workflow;
- plan-only gate;
- no prose before review;
- evidence source bytes;
- 13-image inventory;
- patch-state distinction;
- 100% claim traceability goal;
- Figure/Table numbering remains tentative.

## 14. R2 acceptance gate

R2 must have:
- 2 simple H3 titles;
- 2 compact student-facing tables;
- 3 recommended KEEP figures;
- no evidence filenames in visible report-table design;
- no absolute isolation wording;
- no ICMP-cause attribution;
- no workload-health wording;
- no exact remote dialect inference from local flags;
- no “all other IPs blocked” inference;
- bounded hotfix wording;
- registered `ENV-CORE-*` IDs only;
- no new prose draft;
- no evidence byte change;
- no unrelated file modifications;
- correct remote SHA in handoff.

Final desired state:
`X7A0_BASELINE_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`.

Do not open X7A1.
