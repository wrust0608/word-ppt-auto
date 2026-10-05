# X5 DEMO-STYLE — FINAL EXTERNAL REVIEW R3

Ngày: 2026-10-05  
Candidate branch: `feature/x5-chapter-2-demo-style`  
Candidate commit: `df674075e8b6c76e9a7f906db5be26c010e4e700`  
Kết luận: `PASS_PRESENTATION / FINAL_MICRO_PATCH_REQUIRED`

## 1. Score

| Hạng mục | Điểm |
|---|---:|
| Compliance / workflow | 15/15 |
| Academic depth / reasoning | 18/20 |
| Technical accuracy | 17/20 |
| Sources / traceability | 12/15 |
| Structure | 10/10 |
| Academic style / readability | 10/10 |
| QA / artifact consistency | 10/10 |
| **Tổng** | **92/100** |

Presentation blocker: NO.  
Technical/source micro-blocker: YES.

## 2. Kết luận hội đồng

Demo-style R3 đã đạt đúng hướng người dùng yêu cầu:
- đơn giản;
- dễ đọc;
- tập trung vào dựng lab và demo;
- không còn phong cách leader/QA;
- 7 H2 / 20 H3 hợp lý;
- Demo 1, Demo 2 và Case B/C nhìn vào là hiểu cách thực hiện.

Không được mở lại cấu trúc.

## 3. Điểm cần sửa 1 — SMBv1 wording vẫn hơi vượt ranh giới

Mục 2.6.2 hiện viết gần nghĩa:

“Bật SMBv1 chỉ là điều kiện giao thức cần; nguy cơ bị tổn thương phụ thuộc vào việc nhân hệ điều hành đã được vá lỗi hay chưa.”

Câu này có thể khiến người đọc suy ra:
SMBv1 enabled + UNPATCHED => MS17-010 confirmed.

Trong project hiện hành:
- SMBv1 enabled != MS17-010 confirmed;
- local UNPATCHED != remote exploitability;
- remote NSE verdict canonical vẫn UNKNOWN.

Sửa thành:

“SMBv1 được bật chỉ cho thấy giao thức liên quan còn được hỗ trợ; trạng thái này không đủ để xác nhận MS17-010.”

Có thể thêm:
“Việc đánh giá cần đối chiếu thêm trạng thái bản vá nội bộ và kết quả kiểm tra từ xa.”

## 4. Điểm cần sửa 2 — Research TL03 gắn nhầm PTIT handle

R3 ghi:
- Vũ Thu Trang — “Nghiên cứu triển khai hệ thống giám sát an ninh cho doanh nghiệp vừa và nhỏ sử dụng Splunk”
- handle `HVCNBCVT/4983`

External verification cho thấy:
- `HVCNBCVT/4983` là một record Splunk/Sysmon khác;
- record của Vũ Thu Trang là `HVCNBCVT/3493`.

Sửa TL03:
`https://dlib.ptit.edu.vn/handle/HVCNBCVT/3493`

Không dùng 4983 cho Vũ Thu Trang.

## 5. Minor consistency — Case A table label

Bảng 2.2 đang ghi:
“Case A — Cập nhật bản vá KB4012213”

Trong prose, applicable update đúng là:
- KB4012213;
- KB4012216;
- hoặc superseding update.

Để không tạo cảm giác chỉ KB4012213 là lựa chọn duy nhất, đổi tên row thành:

“Cập nhật bản vá MS17-010”

hoặc:
“Cập nhật Windows theo MS17-010”.

Giữ Case A = reference only / not measured.

## 6. Minor clarity — before/after wording

2.5.1 hiện nói dùng “cùng một tập hợp lệnh Nmap và NSE” cho các ca.

Canonical evidence không hoàn toàn cùng một tập ở Case B và Case C.

Đổi thành:

“Sau mỗi can thiệp, thực hiện lại các phép đo tương ứng để so sánh với trạng thái ban đầu.”

Đơn giản hơn và chính xác hơn.

## 7. Minor style — bỏ jargon còn không cần thiết

Ở 2.4.3:
- “Remote Signal” -> “Kết quả kiểm tra từ xa”.
- Giữ “Trạng thái bản vá nội bộ”.

Ở 2.5.4:
- “Bộ evidence hiện hành” -> “Bộ dữ liệu thực nghiệm hiện có”.

Ở 2.7:
- “Hệ thống dữ liệu thô đa định dạng cùng 5 nguyên tắc diễn giải an toàn tạo lập nền tảng khoa học vững chắc”
  -> câu đơn giản hơn, ví dụ:
  “Các tệp kết quả và nguyên tắc diễn giải trên được dùng làm cơ sở phân tích ở Chương 3.”

Không cần văn phong tự đánh giá chất lượng.

## 8. Các phần đã PASS — không được sửa rộng

- 7 H2 / 20 H3.
- Demo 1 B1-B6.
- Demo 2 command.
- smb-vuln-ms17-010 IPC$ / FID 0 wording.
- UNKNOWN policy.
- FILTERED policy.
- Case B action/retest.
- pfSense CE 2.9.0.
- pfSense rule/tunables.
- Case A reference-only.
- data collection scope.
- no governance jargon.
- no unsupported tools.

## 9. Gate

Sau micro-patch:
- structure phải vẫn 7/20;
- word count không cần tăng;
- không thêm section;
- không thêm nguồn ngoài;
- không rewrite.

## 10. Decision

- Presentation: PASS.
- Structure: LOCKED.
- Technical/source R3: final micro-patch required.
- X5 remains OPEN only for these 5 corrections.
- CP5-USER PENDING.
- X6 BLOCKED.
