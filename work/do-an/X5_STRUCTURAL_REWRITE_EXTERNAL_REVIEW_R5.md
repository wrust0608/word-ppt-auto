# X5 STRUCTURAL REWRITE — FINAL EXTERNAL REVIEW ROUND 5

Ngày: 2026-10-05  
Candidate branch: `feature/x5-chapter-2-structural-revision`  
Candidate commit: `97faf32564191ab0b590bf02e287c6c4935cbbdc`  
Kết luận: `CP5-TECH PASS / LOCKED CANDIDATE FOR USER REVIEW`

## 1. Điểm hội đồng

| Hạng mục | Điểm |
|---|---:|
| Compliance / workflow | 15/15 |
| Academic depth / reasoning | 19/20 |
| Technical accuracy | 19/20 |
| Sources / traceability | 15/15 |
| Structure | 10/10 |
| Academic style / author voice | 9/10 |
| QA / artifact consistency | 9/10 |
| **Tổng** | **96/100** |

Blocker: **0**.

## 2. Kết luận phản biện

R5 đạt ngưỡng khóa kỹ thuật/học thuật của Chương 2.

Cấu trúc 8 H2 / 27 H3 đáp ứng đúng vai trò Chương 2:
- thiết kế nghiên cứu và phạm vi;
- kiến trúc/baseline;
- mô hình bằng chứng;
- thiết kế Scenario 1;
- thiết kế Scenario 2;
- differential mitigation;
- framework đánh giá;
- tổng kết dẫn sang Chương 3.

Không còn yêu cầu structural rewrite.

## 3. Điểm mạnh học thuật

### 3.1. Logic nghiên cứu
Mô hình năm lớp quan sát là trục lập luận mạnh nhất:
1. Reachability
2. Port & Service
3. Protocol State
4. Remote Vulnerability Signal
5. Local Patch State

Mô hình giữ đúng các ranh giới:
- TCP 445 open không đồng nghĩa SMBv1;
- SMBv1 không đồng nghĩa MS17-010 vulnerable;
- UNKNOWN không đồng nghĩa SAFE;
- FILTERED không đồng nghĩa PATCHED;
- disable SMBv1 không đồng nghĩa PATCHED.

### 3.2. Ranh giới Chương 2 / Chương 3
R5 đã giữ đúng HOW / WITH WHAT / UNDER WHAT CONDITIONS.
Observed results chi tiết được dành cho Chương 3.

Baseline facts chỉ xuất hiện khi cần xác lập trạng thái xuất phát.

### 3.3. Kỹ thuật
Các lỗi kỹ thuật qua R1–R4 đã được đóng:
- pfSense tunables đúng canonical;
- B2 subnet discovery / B3 target verification tách đúng;
- -sV không bị dùng để suy exact OS;
- smb-vuln-ms17-010 bám official behavior: IPC$ + transaction on FID 0 + status-code interpretation;
- NO OUTPUT không còn causal inference;
- FILTERED được giữ trung tính;
- Case A reference only;
- S032 patch-version source đã verified;
- Windows Firewall baseline giữ đúng scoped rule.

## 4. R5 panel revisions closure

MR-01 đến MR-10 đều được đóng:
- UNKNOWN/NO USABLE wording;
- SMB Server configuration wording;
- Table 2.1 same-subnet semantics;
- Reachability terminology;
- TCP RST semantics;
- SMB signing scope;
- Case B criterion wording;
- giảm repo jargon;
- research objective wording;
- safety wording.

Không phát hiện regression mới có tính blocker.

## 5. Source / evidence

- Stable Evidence IDs không bị làm sai.
- Case A không được nâng thành observed result.
- Microsoft S032 hỗ trợ file-version threshold.
- Nmap source hỗ trợ script mechanism.
- Citation numbering [1]–[11] tuần tự.
- Không yêu cầu bibliography riêng cuối Chương 2 vì bibliography được quản lý toàn báo cáo.

## 6. QA

Executor report xác nhận:
- validator PASS;
- 7/7 unit tests PASS;
- academic linter 0 error / 0 warning;
- git diff --check PASS;
- citation sequence confirmed;
- clean working tree;
- local SHA = remote SHA.

External Reviewer đã xác minh remote commit trực tiếp.

## 7. Non-blocking publication notes

Các điểm sau KHÔNG mở lại X5 và có thể xử lý khi synthesis/publication nếu cần:
- Có thể thay cụm “ngưỡng an toàn” bằng “ngưỡng phiên bản đã cập nhật” để sát nghĩa Microsoft hơn.
- Có thể đổi “máy trạm” ở host discovery thành “host/nút mạng” nếu muốn tránh nghĩa workstation.
- Có thể Việt hóa cột “Local Ground Truth” thành “Trạng thái bản vá nội bộ” trong bước publication polish.

Không điểm nào ảnh hưởng technical truth hoặc logic nghiên cứu.

## 8. Gate decision

- Score: **96/100**
- Blocker: **0**
- `CP5-TECH = PASS`
- Candidate: `97faf32564191ab0b590bf02e287c6c4935cbbdc`
- Candidate status: `CHAPTER_2_LOCKED_CANDIDATE_FOR_USER_REVIEW`
- `CP5-USER = PENDING`
- `X6 = BLOCKED`

External Reviewer dừng tại đây để người dùng đọc trực tiếp Chương 2.
