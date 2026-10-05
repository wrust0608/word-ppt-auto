# X5 STRUCTURAL REWRITE — EXTERNAL REVIEW ROUND 2

Ngày: 2026-10-05  
Candidate branch: `feature/x5-chapter-2-structural-revision`  
Candidate commit: `ac0ee9e1750e1cbac36ae21fbd22c15e9f9c3c0e`  
Kết luận: `REVISE_BLOCKING / STRUCTURE_RETAINED`

## 1. Score

| Hạng mục | Điểm |
|---|---:|
| Compliance / workflow | 14/15 |
| Academic depth / reasoning | 18/20 |
| Technical accuracy | 13/20 |
| Sources / traceability | 12/15 |
| Structure | 10/10 |
| Author Voice / readability | 9/10 |
| QA / artifact consistency | 8/10 |
| **Tổng** | **84/100** |

Blocker: YES.

## 2. Điều đã đạt

- Remote commit tồn tại thật và fetch được từ GitHub.
- Commit chỉ thay đúng 3 file executor được phép: CHAPTER_2, self-review, proposed source addition.
- User-approved structure giữ đúng 8 H2 / 27 H3.
- Word count khoảng 4.4k, nằm trong target.
- Mô hình 5 lớp đã được khôi phục.
- Fabricated NSE message R1 đã bị xóa.
- NO OUTPUT đã quay về observational wording.
- Stable Evidence ID đã được dùng lại phần lớn đúng.
- Validator, 7 unit tests, linter và diff check được executor báo PASS.
- S032 Microsoft Support được External Reviewer xác minh độc lập và chấp thuận đưa vào SOURCE_LEDGER.

## 3. Blocker A — pfSense bridge tunable sai canonical

Mục 2.6.3 hiện ghi:

`net.link.bridge.pfil_bridge = 1`

Canonical Case C dùng:
- `net.link.bridge.pfil_member = 1`
- `net.link.bridge.pfil_bridge = 0`
- `net.link.bridge.pfil_onlyip = 1`

Filtering được áp trên member interface trong topology canonical; không được đảo thành pfil_bridge=1.

Phải sửa mô tả Case C và figure/table note liên quan nếu có.

## 4. Blocker B — B2/B3 Scenario 1 bị gộp sai scope

Mục 2.4.2 đang gộp B2/B3 thành:

`nmap -sn 192.168.56.20`

Canonical:
- B2 = host discovery trên `192.168.56.0/24`;
- B3 = xác nhận target `192.168.56.20`.

Phải tách mục tiêu/lệnh và bằng chứng tương ứng S1-RAW-01 / S1-RAW-02.

## 5. Blocker C — -sV và result leakage

Mục 2.4 đang mô tả `-sV` như nhận diện service + OS và kể các observed service names/reason.

Sửa:
- `-sV` = service/version detection;
- exact OS lấy từ local baseline, không từ service fingerprint;
- Chương 2 chỉ mô tả dữ liệu cần thu;
- `syn-ack`, `microsoft-ds`, `netbios-ssn` là observed result và chuyển sang Chương 3.

Bảng 2.3 phải đổi “Nhận diện dịch vụ OS” thành “Nhận diện dịch vụ/phiên bản”.

## 6. Blocker D — Evidence ID không tồn tại

Hình 2.3 ghi:

`S1-RAW-01 đến S1-RAW-06`

Stable register chỉ có:
- S1-RAW-01 ... S1-RAW-05
- S1-META-01

Sửa source note.

## 7. Blocker E — Snapshot restore phrasing biến design thành event

Các câu:
- “Mọi thay đổi cấu hình đều hoàn nguyên...”
- “môi trường lab luôn phục hồi về baseline sạch...”

vẫn đọc như sự kiện thực tế đã xảy ra sau mỗi can thiệp.

Current evidence chứng minh snapshot tồn tại và Negative Result Policy yêu cầu restore giữa biến can thiệp, nhưng không có artifact riêng cho từng restore event.

Viết theo phương pháp:
- quy trình yêu cầu dùng `Before Demo` làm mốc phục hồi;
- snapshot cung cấp khả năng đưa môi trường về baseline trước khi đổi biến;
- không claim mỗi restore event đã được ghi nhận nếu thiếu artifact.

## 8. Blocker F — FILTERED vẫn bị diễn giải quá mạnh ở 2.7.1/2.7.3

Mục 2.7.1 hiện kết thúc bằng “có lọc gói”; Bảng 2.5 ghi “Đường truyền bị chặn”.

Ở framework tổng quát:
- Nmap `filtered` = Nmap không thể xác định open/closed vì filtering/no-response/ICMP filtering evidence;
- không quy ngay nguyên nhân cho một firewall cụ thể.

Chỉ Case C ở Chương 3, sau khi đối chiếu C-LOG-01, mới quy thuộc causal attribution cho pfSense rule.

## 9. Blocker G — Case A root-cause claim vượt nguồn đang dẫn

Mục 2.6.4 nói KB4012213/KB4012216 sửa “buffer overflow trong hàm xử lý OS/2 FEA” nhưng chỉ dẫn [4],[5].

S005/S032 hỗ trợ MS17-010 update mapping và file-version verification, không đủ cho root-cause FEA chi tiết.

Chọn một trong hai:
1. đơn giản hóa câu thành patching xử lý lỗ hổng MS17-010 trong SMBv1/driver state; hoặc
2. dẫn thêm S013 Rapid7 cho FEA root-cause.

Ưu tiên phương án 1 ở Chương 2 để không lặp Chương 1.

## 10. Các sửa minor nhưng bắt buộc trước CP5-TECH

### 10.1 Baseline network
- Bỏ “không dùng DNS” nếu không có locked fact cần thiết.
- Bỏ “không qua lọc gói của máy vật lý” vì vượt bằng chứng.
- “SMB1/SMB2 bật mặc định” -> “baseline ghi nhận SMB1=True, SMB2=True”.
- Bảng 2.1 bỏ “Mặc định hệ điều hành”.

### 10.2 Exact Scenario 1 command
Bảng 2.3 không dùng placeholder `<safe_nse>`. Viết exact four scripts:
`smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities`.

### 10.3 Case B
Không khẳng định trong Chương 2 rằng cổng 445 “tiếp tục mở” sau intervention như actual result.
Viết: retest được thiết kế để kiểm tra SMB2/3 availability / protocol surface.

### 10.4 Case A table
Case A không có canonical result. Không cố định:
- SMB1=True;
- 139/445 open;
- một exact KB đã cài.

Đổi row thành reference-only / not measured; nêu applicable MS17-010 update (KB4012213/KB4012216 hoặc superseding update).

### 10.5 Evaluation wording
Case B 2.7.4 không được nói “triệt tiêu ... loại bỏ nguy cơ” hay “máy trạm duy trì kết nối bình thường” như fact tổng quát.
Dùng boundary:
- measured negotiation no longer exposes SMBv1 is criterion;
- SMB2/3 dialect availability does not prove every workload compatibility.

Case C không dùng “che giấu dịch vụ” hoặc suy đoán mọi attacker path.
Nêu rõ control chỉ giảm exposure từ source/path được policy bao phủ.

## 11. Source S032 decision

External Reviewer xác minh Microsoft Support page “How to verify that MS17-010 is installed”.

Nguồn hỗ trợ:
- Windows Server 2012 R2 / Windows 8.1;
- KB4012213, KB4012216 và superseding updates;
- minimum updated `srv.sys = 6.3.9600.18604`;
- file-version + PowerShell verification method.

Decision: `S032 VERIFIED`.

## 12. Workflow state

- Structure: LOCKED, không reopen.
- Candidate R2: REVISE_BLOCKING.
- X5: OPEN for surgical technical patch only.
- CP5-TECH new candidate: NOT YET.
- CP5-USER: PENDING.
- X6: BLOCKED.
