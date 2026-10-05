# X6 EXTERNAL REVIEW R1 — CHAPTER 2 DOCX + CHAPTER 3 EVIDENCE PREP

Date: 2026-10-06  
Candidate: `bdaafd77ff3e03b573a852809025559159096529`  
Branch: `feature/x6-ch3-evidence-prep`  
Verdict: `61/100 — REVISE_BLOCKING`

## 1. Executive verdict

The staging workflow is materially useful and the byte-integrity work is strong, but X6 cannot pass yet.

There are two blocker classes:

1. the Chapter 2 DOCX QA record is demonstrably based on a legacy Chapter 2 structure rather than the locked product-aligned Chapter 2;
2. the Chapter 3 preparation matrices contain multiple factual/interpretive regressions against the R3 evidence locks.

Chapter 3 prose remains blocked.

## 2. Score

| Category | Score |
|---|---:|
| Scope / workflow compliance | 11/15 |
| Chapter 2 DOCX artifact consistency | 5/20 |
| Evidence integrity / SHA traceability | 15/15 |
| Technical accuracy of Chapter 3 preparation | 11/20 |
| Result-logic discipline | 7/15 |
| Structure / figure planning | 7/10 |
| QA consistency | 5/5 |
| **Total** | **61/100** |

Blockers: **2 classes / multiple findings**.

## 3. PASS — evidence byte integrity

Verified from candidate:
- 83 staged files in `CHAPTER_3_EVIDENCE_SHA256.csv`;
- 0 SHA mismatch;
- all staged files are byte-identical to the recorded source archive path/hash;
- role distribution is:
  - 39 `PRIMARY_RAW`;
  - 33 `PRIMARY_VISUAL`;
  - 5 `PRIMARY_LOCAL_STATE`;
  - 1 `PRIMARY_VISUAL_WITH_BOUNDED_CONFLICT`;
  - 4 `SECONDARY_META`;
  - 1 `SECONDARY_META_CLOSURE`.

Therefore the handoff wording “83 primary evidence files” is inaccurate.

Correct wording:
- **83 staged files total**;
- **78 primary/direct evidence files**;
- **5 secondary metadata/closure files**.

The 91 remaining archive files may remain preserved/non-main, but this count is an archive classification statement, not evidence of report relevance.

## 4. BLOCKER A — Chapter 2 DOCX QA is for the wrong Chapter 2

Locked Chapter 2 on `main` is:

`CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM`

with:
- 2.1 Phạm vi và mô hình thực nghiệm;
- 2.2 Chuẩn bị và xác nhận trạng thái ban đầu;
- 2.3 Kịch bản 1;
- 2.4 Kịch bản 2;
- 2.5 Hai biện pháp giảm thiểu;
- 2.6 Dữ liệu thực nghiệm;
- 2.7 Tổng kết.

But `work/do-an/output/CHAPTER_2_FINAL_DOCX_QA.md` describes a legacy document containing:
- chapter title “THIẾT KẾ MÔ HÌNH THỰC NGHIỆM VÀ PHƯƠNG PHÁP THU THẬP BẰNG CHỨNG”;
- “mô hình ánh xạ mục tiêu nghiên cứu”;
- “trạng thái kiểm toán tiền thực nghiệm”;
- “mô hình phân loại bằng chứng năm lớp”;
- a decision-tree figure for MS17-010;
- legacy section numbering and content.

This is incompatible with the locked Chapter 2.

Therefore:
- the reported 13-page visual PASS is invalid as a QA record for the approved Chapter 2;
- the current DOCX cannot be accepted until regenerated and revalidated from the locked source.

The committed standalone figures `hinh_2_1.png` and `hinh_2_2.png` were independently inspected and are consistent with the current product-aligned Chapter 2:
- baseline Host-Only topology;
- pfSense transparent-bridge topology.

They may be reused.

## 5. BLOCKER B1 — wrong MS17-010 KB mapping

The staged source artifact itself correctly records Windows Server 2012 R2:
- KB4012213 — Security Only;
- KB4012216 — Monthly Rollup;
- minimum updated `srv.sys 6.3.9600.18604`.

However the evidence index/result matrix incorrectly use:
- KB4012212;
- KB4012215.

Those are not the locked mapping for this Windows Server 2012 R2 target.

Required:
- replace every Chapter 3 prep reference to KB4012212/KB4012215 with the locked KB4012213/KB4012216 mapping;
- retain superseding-update language where appropriate;
- distinguish FileVersion String `6.3.9600.16384` from numeric `6.3.9600.16421`.

## 6. BLOCKER B2 — .56.100 was re-identified

Evidence index S1-01 currently writes:
`.56.100 (DHCP/DHCP lease daemon)`

while its own forbidden-inference cell says the host is UNKNOWN.

This directly violates the R3 lock.

Required:
- .56.100 = observed host only;
- identity = UNKNOWN;
- do not label it DHCP, pfSense or another device.

Also avoid calling .56.1 a “Gateway” in Scenario 1 result language. It is established as the VirtualBox Host-Only host adapter; the baseline VMs have no default route.

## 7. BLOCKER B3 — SMB signing overinterpretation

Current prep states:
- `enabled but not required` means unsigned connections are accepted as a condition for probe payload;
- “tiền điều kiện tiếp nhận gói tin thăm dò không ký số”.

This is unnecessary and stronger than the evidence needs.

Required:
- preserve only remote observation:
  `Message signing enabled but not required`;
- interpret as a remote signing policy observation;
- do not turn it into a prerequisite for MS17-010 probing/exploitation.

Keep local PowerShell signing flags separate from remote Nmap signing output.

## 8. BLOCKER B4 — Case B overclaims workload behavior

Current prep uses wording equivalent to:
- “dịch vụ SMBv2/v3 vẫn hoạt động bình thường”;
- intervention succeeded “without disruption of modern file sharing”.

The experiment verifies dialect negotiation after SMBv1 is disabled. It does not validate full file-sharing workloads.

Required:
- say SMB2/SMB3 dialects remain present/negotiable in the remote retest;
- do not claim general workload/service functionality was validated.

## 9. BLOCKER B5 — Case C causality and vulnerability claims are too strong

Current result matrix/index contains phrases equivalent to:
- filtered `due no-response` -> firewall blocked the SYN;
- “ngắt hoàn toàn bề mặt tiếp xúc mạng L1/L2”;
- “toàn bộ bề mặt tấn công ... bị cô lập hoàn toàn”;
- server “vẫn tồn tại lỗ hổng” / “lỗ hổng nội tại vẫn nguyên vẹn”;
- script “bị vô hiệu hóa hoàn toàn”.

These exceed the locked evidence.

Required decomposition:

### Remote Nmap fact
- 139/445 = `filtered`, reason `no-response`.
- This alone does not establish the cause.

### Direct pfSense log fact
- matching TCP SYN traffic from .56.10 to .56.20:139/445 is visibly Blocked on CASE_C_KALI.
- exact named-rule attribution remains unresolved due the visible rule-label conflict.

### Combined bounded interpretation
Allowed:
- from the Kali vantage point through the Case C path, TCP 139/445 are no longer remotely classifiable as open and are inaccessible to the tested connection attempt;
- direct pfSense logs independently show matching SMB SYN traffic being blocked;
- MS17-010 remote result remains UNKNOWN/inaccessible from this vantage point;
- local Windows patch state remains UNPATCHED;
- SMB1 remains enabled locally.

Forbidden:
- firewall “proves vulnerability still exists”;
- “all attack surface eliminated”;
- “machine safe”;
- “script disabled completely”;
- `FILTERED = PATCHED`;
- exact named-rule attribution from the conflicting log screenshot.

## 10. Figure-plan corrections

### srv.sys figure
Do not caption one screenshot as independently “confirming UNPATCHED”.

The screenshot directly shows a displayed file version. UNPATCHED is established by:
- numeric local version;
- official Microsoft minimum/version mapping;
- observed update inventory.

### Case B figure
Remove claim that disabling SMBv1 caused no disruption to modern file sharing.

Use:
- action performed;
- local SMB1=False;
- remote SMB2/3 dialects remain observable.

### Case C figures
Do not caption the Nmap filtered screenshot alone as proof of firewall causality.

Pair:
- filtered/no-response result;
- separate direct pfSense log showing matching blocked SYN traffic.

Do not use “blocked completely”, “eliminated attack surface”, or similar absolutes.

## 11. Structure-proposal corrections

The proposed 7-H2 result-oriented structure is directionally good:

3.1 Baseline  
3.2 Scenario 1  
3.3 Scenario 2  
3.4 Case B  
3.5 Case C  
3.6 Comparison  
3.7 Summary

Keep it.

However, remove front-facing/internal jargon rejected during Chapter 2 review:
- L1/L2/L3/L4/L5 evidence layers;
- “five-layer evidence model”;
- governance/canonical/gate wording as report architecture.

Chapter 3 should read as:
result -> evidence -> bounded interpretation -> comparison.

Do not turn internal evidence taxonomy into the student's report structure.

## 12. Secondary metadata use

`RUN4_PAUSE_STATE_REPORT.txt` and run manifests may remain staged as `SECONDARY_META`.

They must not be presented as primary measurement evidence when direct raw/log/screenshot artifacts exist.

For Case C result tables:
prefer:
- Nmap raw;
- rule/config screenshots;
- canonical firewall log;
- local Windows state.

Use manifests only to recover lineage/context.

## 13. DOCX R2 acceptance criteria

Regenerate `CHAPTER_2_FINAL.docx` strictly from current `origin/main:work/do-an/CHAPTER_2.md`.

Mandatory automated content checks:
- exact chapter title equals locked title;
- exact 7 H2 and 20 H3 sequence matches Markdown;
- four table titles match the current chapter;
- Figure 2.1 = baseline topology;
- Figure 2.2 = pfSense topology;
- no legacy phrases:
  - `PHƯƠNG PHÁP THU THẬP BẰNG CHỨNG`
  - `mô hình phân loại bằng chứng năm lớp`
  - `cây quyết định phân loại trạng thái kiểm định`
  - legacy 2.3/2.4/2.5 heading names.

Generate a fresh QA file from the actual final render. Do not reuse/copy the old QA narrative.

Visually inspect every rendered page after regeneration.

## 14. Gate

- X6 R1: **REVISE_BLOCKING**.
- Chapter 2 content remains LOCKED; only the DOCX build/QA must be regenerated.
- Chapter 3 evidence bytes may remain staged.
- Chapter 3 matrices/index/figure plan/structure proposal require correction.
- Chapter 3 prose remains BLOCKED.
