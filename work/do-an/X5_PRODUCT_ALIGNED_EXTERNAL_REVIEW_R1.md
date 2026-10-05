# X5 PRODUCT-ALIGNED — EXTERNAL REVIEW R1

Date: 2026-10-06  
Candidate: `1e1cc9edc191efb2a03e6b20807fa82d32841448`  
Branch: `feature/x5-chapter-2-product-aligned`  
Verdict: `89/100 — REVISE_MINOR_BLOCKING`

## 1. Score

| Category | Score |
|---|---:|
| Compliance / workflow | 14/15 |
| Academic depth / reasoning | 18/20 |
| Technical accuracy | 16/20 |
| Sources / traceability | 14/15 |
| Structure | 10/10 |
| Academic style / readability | 9/10 |
| QA / artifact consistency | 8/10 |
| **Total** | **89/100** |

Presentation direction: PASS.  
Product alignment: PASS with micro-corrections.  
Blocking issues: 2 logical + several wording corrections.

## 2. What is now correct

- Remote SHA verified; candidate is exactly one commit ahead of demo-style R4.
- Only `CHAPTER_2.md` and self-review changed.
- 7 H2 / 20 H3 retained.
- Case A removed from performed experiment design.
- Scenario 1 operator commands now match command lineage and contain no prose-added `-Pn`.
- Scenario 2 contains all four operator commands and does not convert raw `--privileged` into operator input.
- Case B uses the actual action and only the two actual retests.
- Case C has a separate transparent-bridge topology and does not overwrite baseline topology.
- Case C does not claim exact named-rule attribution from the conflicting firewall-log label.
- `.56.100` is not identified.
- Cross-system clock warning is present.
- Chapter 3 remains unopened.

## 3. BLOCKER 1 — result leakage still exists in Chapter 2 tables

The executor claims no result leakage, but the method tables still contain outcome-specific values.

Examples:
- Scenario 1 B4 “`syn-ack`”
- Scenario 1 B6 “`NT LM 0.12`, SMBv2/v3”
- Scenario 2 NSE-SMB-02 “Sự xuất hiện của `NT LM 0.12`”
- Scenario 2 NSE-SMB-03 wording can be generalized to the returned signing policy rather than implying a known measured outcome.

Chapter 2 should define what fields are observed, not populate them with the final observed values.

Patch:
- B4 -> “trạng thái cổng và trường REASON”.
- B5 -> “chuỗi service/version fingerprint”.
- B6 -> “danh sách dialect trả về; signing policy; capability fields”.
- NSE-SMB-01 -> “port state and reason”.
- NSE-SMB-02 -> “danh sách dialect SMB trả về”.
- NSE-SMB-03 -> “chính sách ký số SMB được script trả về”.
- NSE-SMB-04 -> “script output / verdict nếu có”.

Actual `syn-ack`, `NT LM 0.12`, concrete dialect list and actual UNKNOWN verdict belong to Chapter 3.

## 4. BLOCKER 2 — FILTERED causality regressed

2.6.3 currently says:
“FILTERED ... cho biết gói tin bị chặn trên đường truyền”.

This violates the locked negative-result policy.

Generic meaning must be:
“FILTERED cho biết Nmap không nhận đủ phản hồi để phân loại cổng là open hay closed; trạng thái này không chứng minh máy chủ đã được vá.”

For Case C, Chapter 3 may correlate the filtered scan with direct pfSense log evidence. The generic Chapter 2 rule must not pre-assign the cause.

## 5. SMBv1 inference needs tightening

2.3.3 and 2.6.3 currently use wording close to:
“SMBv1 is a necessary protocol condition; exploit risk depends on patch state.”

This can imply SMBv1 + UNPATCHED is enough to confirm MS17-010/exploitability.

Use:
“SMBv1 được bật chỉ cho thấy giao thức liên quan còn được hỗ trợ; trạng thái này không đủ để xác nhận MS17-010. Việc đánh giá cần đối chiếu thêm trạng thái bản vá nội bộ và kết quả kiểm tra từ xa.”

## 6. Case B wording is too absolute

2.5.2 currently says:
“nhằm loại bỏ hoàn toàn việc hỗ trợ giao thức kế thừa SMBv1.”

The actual action changes SMB Server configuration:
`Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`

But `FS-SMB1` remains installed and the statement should not imply all SMBv1 components/roles are removed.

Use:
“nhằm vô hiệu hóa SMBv1 ở cấu hình SMB Server”.

Also change:
“không yêu cầu khởi động lại máy”
to:
“trong kịch bản không thực hiện bước khởi động lại máy”.

This states what was done, not a universal product requirement.

## 7. Patch wording

2.2.4 heading/bullet phrase “Đối chiếu ngưỡng an toàn” should be:
“Đối chiếu ngưỡng phiên bản đã cập nhật”.

Do not imply version threshold alone is a universal safety threshold.

The local hotfix sentence should remain bounded to observed inventory / project mapping.

## 8. Isolation wording

Several phrases remain more absolute than the evidence supports:
- “loại trừ kết nối mạng ngoài”
- “bảo đảm tính khép kín”
- “bảo đảm lưu lượng chỉ lưu chuyển cục bộ”

Final pre-demo evidence supports:
- one Host-Only NIC per Kali/Windows;
- no NAT/Bridged NIC;
- no default route inside those VMs.

Prefer:
“không cấu hình NAT/Bridged hoặc default route cho hai VM ở baseline, qua đó giới hạn đường kết nối của chúng trong mạng lab.”

Do not generalize to every possible host-forwarding path.

## 9. 2.6.2 evidence-selection wording

The current exclusion wording can sound like discarded inconvenient data.

Clarify:
- troubleshooting/pre-repair/aborted data remain preserved for traceability;
- they are not used as the main result set because they are not the final completed run;
- final/canonical run is used for Chapter 3 result claims.

This avoids the appearance of cherry-picking.

## 10. Case C pfil wording

`pfil_member=1` and `pfil_bridge=0` wording is consistent with pfSense documentation.

`pfil_onlyip=1` wording “chỉ truyền gói IP qua bridge” is consistent with FreeBSD bridge documentation, but in this project its value is metadata-supported rather than directly screenshot-proven.

No technical rewrite is required; simply avoid claiming the screenshot itself proves all three values.

## 11. Style polish

2.7:
“Hệ thống dữ liệu đa định dạng cùng 5 nguyên tắc ... tạo lập nền tảng khoa học vững chắc”

is self-evaluative.

Replace with:
“Các tệp kết quả và nguyên tắc diễn giải trên được dùng làm cơ sở phân tích tại Chương 3.”

## 12. Gate decision

- Structure 7 H2 / 20 H3: LOCKED.
- Product-aligned direction: PASS.
- Candidate R1: REVISE_MINOR_BLOCKING.
- No new research or restructuring.
- R2 must be a micro-patch only.
- CP5-USER: PENDING.
- X6 / Chapter 3: BLOCKED.
