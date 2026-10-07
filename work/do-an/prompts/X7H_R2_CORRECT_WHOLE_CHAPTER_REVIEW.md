# X7H R2 — CORRECT WHOLE-CHAPTER EDITORIAL TECHNICAL DRIFT

Status: AUTHORIZED BOUNDED CORRECTION
Date: 2026-10-07
Branch: `feature/x7h-ch3-whole-review-approved-r1`
R1 candidate: `01cc66de9845395777ced08801d5816ab1f938fe`
Review: `work/do-an/X7H_CH3_WHOLE_REVIEW_EXTERNAL_REVIEW_R1.md`

## Mandatory scope

Correct only the four evidence/technical wording drifts identified by the independent reviewer.

Do not edit any USER APPROVED / LOCKED source-section file.
Edit only the whole-chapter candidate and the X7H self-review/handoff artifacts needed to document R2.

## Correction 1 — Case C topology

In `CHAPTER_3_DRAFT_R2.md`, remove the routing implication from the Case C opening.

Current problematic wording includes:
`được định tuyến qua tường lửa pfSense hoạt động ở chế độ Transparent Bridge (Layer 2)`

Use bounded Layer-2 wording, for example:
`được bố trí đi qua tường lửa pfSense hoạt động ở chế độ Transparent Bridge (Layer 2)`

Do not introduce router/L3 semantics.

## Correction 2 — baseline firewall rule scope

Remove:
`bảo đảm bề mặt dịch vụ tại baseline chỉ mở cho trạm kiểm thử chỉ định`

Use configuration-bounded wording that says:
- the custom rule allows TCP 139/445 from source `192.168.56.10`;
- default File and Printer Sharing rules were observed disabled;
- actual remote reachability is verified separately by the following network measurements.

Do not claim global exclusivity of service exposure.

## Correction 3 — local hotfix inventory

Remove:
`danh sách cập nhật dừng ở năm 2014`

Use evidence-bounded wording such as:
`sáu mục Get-HotFix quan sát được đều có ngày cài đặt trong năm 2014`

Keep the UNPATCHED classification grounded in:
- numeric `srv.sys = 6.3.9600.16421`;
- Microsoft minimum updated threshold `6.3.9600.18604`;
- relevant updates not observed in the local inventory.

Do not turn the observed inventory into a complete update-history claim.

## Correction 4 — Nmap fingerprint scope

Remove the generalized capability claim:
`Nmap ... không thể tự định danh chính xác ... nếu thiếu dữ liệu xác thực cục bộ`

Use measurement-bounded wording:
- in this measurement, Nmap returned the Windows Server 2008 R2–2012 fingerprint range;
- the recorded remote responses were insufficient to uniquely identify Windows Server 2012 R2;
- the exact target OS version is established from independently verified local baseline data.

Do not generalize what Nmap can or cannot do outside this measurement.

## Preserve all other X7H R1 editorial improvements

Do not revert the legitimate readability improvements unless necessary for the four corrections above.

No other prose change is authorized in this correction round.

## Verification

After correction, verify:
- R2 candidate differs from X7H R1 candidate only at the four authorized passages;
- 1 H1 / 7 canonical H2 / 10 H3;
- Bảng 3.1–3.7 unchanged;
- Hình 3.1–3.11 unchanged;
- no Bảng 3.8 / Hình 3.12;
- all technical locks remain intact;
- no `định tuyến qua` wording for Transparent Bridge;
- no global firewall-exclusivity claim;
- no complete-history hotfix wording;
- Nmap statement is bound to the recorded measurement;
- no Chapter 4 recommendation/risk-ranking leakage;
- no internal QA/governance marker in student-facing prose.

Rerun:
- unit tests;
- Vietnamese academic linter;
- `git diff --check`;
- project validation.

Update:
- `X7H_CH3_WHOLE_REVIEW_SELF_REVIEW_R1.md`;
- `X7H_CH3_WHOLE_REVIEW_EXECUTOR_HANDOFF_R1.md`.

## Stop state

The only allowed completion state is:

`X7H_R2_READY_FOR_INDEPENDENT_REVIEW`

Commit and push, report the exact four corrections and QA results, then STOP.

Do not open X7I.
Do not create DOCX/PDF.
Do not declare the complete Chapter 3 user-approved.
