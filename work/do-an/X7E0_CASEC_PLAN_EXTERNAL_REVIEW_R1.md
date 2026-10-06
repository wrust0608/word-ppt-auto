# X7E0 CASE C EVIDENCE & PRESENTATION PLAN — EXTERNAL REVIEW R1

Date: 2026-10-07  
Branch: `feature/x7e0-ch3-casec-plan`  
Executor candidate: `fe4aef1a7cce7bf5782cb8d6c9d3edfa10f08a26`

Verdict: **87/100 — REVISE_BLOCKING**

## 1. Overall finding

The R1 plan is directionally strong.

Keep:
- the 2-H3 structure;
- one Bảng 3.6;
- the three-figure main strategy:
  - Hình 3.9 = rule order/configuration;
  - Hình 3.10 = canonical Nmap FILTERED result;
  - Hình 3.11 = pfSense Block log;
- Hình 3.12 NSE04 remains OPTIONAL/DROP in the standard layout;
- the rule-label conflict remains explicit;
- the timebase warning remains explicit;
- Windows-local state remains provenance-separated from pfSense screenshots.

This is the right product shape for Case C.

No structural redesign is required.

R2 must correct several evidence-boundary and presentation-precision problems before the plan can be user-approved.

## 2. What passes

### Evidence coverage — PASS
The executor inspected all 17 staged files and all 9 screenshots.

### Figure-count strategy — PASS
Three main figures are justified and sufficiently distinct:
1. control configuration/order;
2. measured network result;
3. corresponding firewall log observation.

The bridge screenshot can remain OPTIONAL/DROP because Chapter 2 already contains the Case C Transparent Bridge topology (Hình 2.2) and Section 3.5 should prioritize measured results rather than repeat the full setup.

### H3 structure — PASS
Keep exactly:
- `3.5.1. Thiết lập cầu nối pfSense và chính sách kiểm soát lưu lượng SMB`
- `3.5.2. Kết quả đo đạc từ xa, đối chiếu nhật ký tường lửa và trạng thái máy chủ`

### Rule-label conflict handling — PASS in concept
The plan correctly preserves:
- direct log label: `CASE C baseline pass Kali to Windows (100000104)`;
- manifest/closure attribution: `CASE C - Block SMB Kali to Windows (1000000104)`;
- exact named-rule attribution remains unresolved.

Keep the allowed conclusion:
`matching SMB SYN traffic was blocked in the pfSense path`.

## 3. Blocker A — MS17-010 cause is invented in multiple plan artifacts

R1 repeatedly states or implies:
- because TCP 445 was filtered, the NSE script could not interact with the service;
- because the port was blocked, the script did not execute/produce output;
- Nmap "automatically hides" Host script results due to the filtered port.

This exceeds the canonical evidence boundary.

The raw Case C NSE04 evidence proves only:
- host up;
- `445/tcp filtered microsoft-ds`;
- no `Host script results:` block;
- no usable vulnerability verdict.

Required R2 wording:

`Phép đo NSE-SMB-04 ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT.`

And:

`Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có.`

Do not say:
- "do cổng bị chặn nên script không thể tương tác";
- "script không nhận được dữ liệu để thực thi";
- "Nmap tự động ẩn kết quả";
- script failed because pfSense.

This correction must be applied in:
- figure-selection note;
- presentation plan;
- claim-evidence map;
- self-review.

## 4. Blocker B — Bảng 3.6 misstates the baseline as having no firewall/filter

R1 uses phrases such as:
- `Không qua thiết bị lọc`;
- `Cho phép kết nối mặc định`;
- `Chưa có tường lửa`;
- `Chưa có bộ lọc`.

These are inaccurate as general baseline statements because the Windows host already had its baseline Windows Firewall profile/rule state.

Case C's intervention is specifically the addition of **pfSense on the tested network path**, not the transition from "no firewall" to "a firewall".

Required Bảng 3.6 baseline wording:

### Network path
Before:
`Host-Only baseline; chưa có pfSense trên đường thử nghiệm Kali → Windows`

After:
`Đường thử nghiệm đi qua pfSense Transparent Bridge`

### pfSense policy
Before:
`Chưa áp dụng ruleset pfSense Case C trên đường thử nghiệm`

After:
`BLOCK TCP .56.10 → .56.20:139/445, logging enabled`

### Rule order
Before:
`Không áp dụng đối với pfSense Case C`

After:
`BLOCK nằm trên PASS`

### pfSense log
Before:
`Không có log pfSense tương ứng vì pfSense chưa nằm trên đường baseline`

After:
`Ghi nhận Block đối với matching TCP SYN tới 139/445`

Do not say the baseline had no firewall at all.

## 5. Blocker C — several absolute/causal statements exceed the measured scope

Correct these classes of wording:

### Current:
`toàn bộ lưu lượng ... bắt buộc phải đi xuyên qua cầu nối`

Use:
`Trong topology Case C, đường thử nghiệm Kali → Windows được bố trí đi qua bridge0 của pfSense.`

Do not make a universal statement about every possible host/network path.

### Current:
`máy chủ hoàn toàn không trải qua bất kỳ thay đổi cấu hình hay bản vá nào`

Use:
`Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá trên Windows; metadata cuối Case C ghi nhận SMB1=True, SMB2=True, LanmanServer Running và patch state UNPATCHED.`

### Current:
`dịch vụ SMBv1 chứa lỗ hổng vẫn tồn tại nguyên vẹn`

Forbidden.

Use only:
- SMB1 local configuration remains True;
- local patch state remains UNPATCHED.

Do not infer exploitable/vulnerable service state from those two facts.

### Current:
`bằng chứng nhân quả liên tầng` / `trạng thái filtered bắt nguồn từ...`

Prefer:
`đối chiếu liên tầng`.

Allowed:
`Kết quả Nmap ghi nhận 139/445 FILTERED, đồng thời log pfSense ghi nhận matching SMB SYN traffic bị Block trên đường pfSense trong lượt Case C.`

Do not claim a stronger causal proof than the locked evidence permits.

## 6. Blocker D — Hình 3.9 proposed crop contradicts its own preservation requirement

R1 proposes:

`x=20, y=370, width=455, height=240`

while saying the crop must preserve:
- the selected `CASE_C_KALI` tab;
- `Rules (Drag to Change Order)`;
- both Block and Pass rows.

Visual inspection of the 485x731 source shows that starting at `y=370` removes the `CASE_C_KALI` tab and risks clipping the top of the rules-table heading.

R2 requirement:
- revise the provisional crop after visual inspection;
- use an approximate geometry around:
  `x≈15, y≈185–200, width≈470, height≈320–350`
  and verify that it preserves:
  - `CASE_C_KALI`;
  - rules-table heading;
  - full Block row;
  - full Pass row.
- remove the insecure-password warning and footer.

No crop is created in X7E0; this is still a provisional plan.

The Hình 3.10 crop is acceptable in principle.

For Hình 3.11, retain the crop as provisional only and explicitly require exact visual verification before the derived image is created, because the source is 1359x17637 and the current y-range is approximate.

## 7. Blocker E — internal claim map references a non-existent evidence-index file / invented registry assertion

R1 says its IDs are registered in:

`CHAPTER_3_SECTION_EVIDENCE_MAP.md` and `CHAPTER_3_EVIDENCE_INDEX.md`.

The current repository does not contain `CHAPTER_3_EVIDENCE_INDEX.md`.

Also, the claim map should not imply every `C-IMG-08`–`C-IMG-11` identifier is an already registered stable ID unless the current authoritative evidence registry actually contains it.

R2 requirement:
- remove the reference to non-existent `CHAPTER_3_EVIDENCE_INDEX.md`;
- do not invent registry status;
- either:
  1. use the evidence-family identifiers explicitly present in current authoritative files; or
  2. simplify the claim map to evidence filenames + evidence type (direct raw / direct visual / metadata-lineage), which is sufficient for X7E0.

Do not create a new evidence-index file.

## 8. Blocker F — rule-order semantics are over-explained inside a Chapter 3 result plan

R1 says:
- first-match "guarantees" the SMB block occurs first;
- if the Block rule were below Pass it would be "completely ineffective".

This is unnecessary for Chapter 3 and is stronger than needed.

The direct evidence needed in Chapter 3 is:
- the configured Block rule exists;
- it is displayed above the Pass rule.

R2 requirement:
- keep the observed order;
- remove absolute language such as `bảo đảm`, `vô hiệu hóa hoàn toàn`;
- do not turn Section 3.5 into a firewall-theory tutorial.

If rule-processing semantics need explanation later, they must be sourced appropriately; Chapter 3 can simply refer to the configured ordering and the measured/log observations.

## 9. Blocker G — local-state wording must remain point-in-time / provenance-bounded

R1 sometimes uses:
- `duy trì hoàn toàn không đổi`;
- `mã nhị phân srv.sys giữ nguyên`;
- `dịch vụ tiếp tục hoạt động` as if continuous uptime was measured.

Required:
- use point-in-time state language:
  - Case C metadata records SMB1=True;
  - SMB2=True;
  - LanmanServer=Running;
  - local listeners 139/445 present;
  - patch classification UNPATCHED.
- state that no Case C patch/config action is recorded.
- do not claim continuous uptime, zero interruption, or omniscient binary-history continuity.

For `srv.sys`, if used:
- identify `6.3.9600.16421` as the canonical numeric version used for patch classification;
- do not confuse it with the displayed file-version string `6.3.9600.16384`.

## 10. Presentation decision retained for R2

Keep the primary three-figure strategy:

- Hình 3.9 — `pfSense_08_Rule_Order.png`
- Hình 3.10 — `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`
- Hình 3.11 — `pfSense_10_Block_Log_CANONICAL.png`

Keep:
- `pfSense_04_Bridge.png` = OPTIONAL/DROP;
- `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` = OPTIONAL/DROP in the standard layout.

Reason:
Chapter 2 already contains the Transparent Bridge topology. Section 3.5 should use page space primarily for control configuration, measured FILTERED result and firewall log.

## 11. R2 scope

Modify only the four X7E0 plan files:

- `work/do-an/CH3_35_CASEC_FIGURE_SELECTION_R1.md`
- `work/do-an/CH3_35_CASEC_PRESENTATION_PLAN_R1.md`
- `work/do-an/CH3_35_CASEC_CLAIM_EVIDENCE_MAP_R1.md`
- `work/do-an/CH3_35_CASEC_PLAN_SELF_REVIEW_R1.md`

No prose.
No crops.
No evidence changes.
No infrastructure changes.
No Chapter 2/4 changes.

## 12. Final gate

Current verdict:

`X7E0_CASEC_PLAN_R1_REVISE_BLOCKING`

After R2:
- independently recheck the four plan files;
- visually recheck Hình 3.9/3.10 source geometry and Hình 3.11 crop intent;
- if clean, issue final external PASS and wait for explicit user approval before X7E1 prose.
