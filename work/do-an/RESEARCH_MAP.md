# Bản đồ nghiên cứu

Trạng thái: `LOCKED_CANONICAL_2026_10_05`

## Vấn đề trung tâm

Đánh giá an ninh SMB không thể đồng nhất cổng TCP 445 mở, SMBv1 được chấp nhận, tín hiệu từ công cụ quét và trạng thái bản vá của hệ điều hành. Đề tài xây dựng một quy trình kiểm thử có kiểm soát để phân biệt các lớp bằng chứng này, sau đó đánh giá tác động và giới hạn của các biện pháp giảm thiểu ở lớp giao thức và lớp mạng.

## Khoảng trống cần xử lý

1. Nhầm lẫn giữa reachability, SMB protocol state, remote vulnerability signal và local patch ground truth.
2. Thiếu quy trình kiểm thử có khả năng truy vết bằng raw output, ảnh canonical và trạng thái cục bộ.
3. Thiếu đối chiếu rõ ràng giữa patching, vô hiệu hóa SMBv1 và network access control.
4. Dễ diễn giải sai kết quả âm tính/bất định của scanner thành “an toàn”.

## Câu hỏi nghiên cứu

| ID | Câu hỏi | Phương pháp/bằng chứng | Tiêu chí hoàn thành |
|---|---|---|---|
| RQ1 | Kiến trúc, negotiation/session/resource access và sự khác biệt bảo mật giữa SMBv1, SMBv2, SMBv3 là gì? | Microsoft/Open Specs, tài liệu SMB security, nguồn học thuật | Giải thích đúng cơ chế và bảng so sánh phục vụ phần thực nghiệm |
| RQ2 | MS17-010 liên quan tới cơ chế xử lý SMB nào, điều kiện tác động và ý nghĩa an ninh ra sao? | Microsoft MS17-010, NVD, nguồn kỹ thuật đã xác minh | Phân biệt bulletin/CVE, cơ chế lỗi, điều kiện và tác động |
| RQ3 | Mô hình lab và quy trình kiểm thử nào cho phép phân biệt reachability, protocol state, remote detection signal và local patch ground truth một cách an toàn, truy vết được? | VirtualBox Host-Only, snapshot, Nmap/NSE, Windows local state, Evidence IDs | Lab canonical + Scenario 1/2 + inference boundaries |
| RQ4 | Các lớp giảm thiểu ảnh hưởng như thế nào tới bề mặt giao thức, khả năng tiếp cận và trạng thái host; hiệu quả và giới hạn của từng lớp là gì? | Before/after Case B/C, Microsoft/NIST, local ground truth | Ma trận so sánh và khuyến nghị defense-in-depth không overclaim |

## Mục tiêu

| ID | Mục tiêu | RQ | Sản phẩm/bằng chứng |
|---|---|---|---|
| O1 | Hệ thống hóa cơ sở lý thuyết SMB | RQ1 | Chương 1 |
| O2 | Phân tích MS17-010 và bề mặt tấn công | RQ2 | Chương 1 |
| O3 | Thiết kế và mô tả lab canonical cùng quy trình kiểm thử có kiểm soát | RQ3 | Chương 2 + Evidence Map |
| O4 | Phân tích kết quả và đánh giá các lớp giảm thiểu | RQ4 | Chương 3–4, ma trận Baseline/Case B/Case C |

## Phương pháp

| ID | Phương pháp | Đầu vào | Đầu ra | Giới hạn |
|---|---|---|---|---|
| M1 | Phân tích tài liệu kỹ thuật/học thuật | Microsoft, NVD, Nmap, NIST, Rapid7 và nguồn đã xác minh | Nền lý thuyết/claim nguồn | Không dùng NotebookLM như nguồn trích dẫn |
| M2 | Thiết kế lab ảo hóa cô lập | VirtualBox, Kali, Windows Server 2012 R2, Host-Only, snapshot | Sơ đồ, cấu hình và baseline | Môi trường ảo hóa, một target chính |
| M3 | Kiểm thử an ninh có kiểm soát | Scenario 1/2, raw Nmap/NSE, local Windows state | AUTHOR_DATA có Evidence ID | Không có canonical exploit/RCE result; remote NSE04 có thể UNKNOWN |
| M4 | Differential before/after testing | Baseline, Case B, Case C | So sánh tác động từng mitigation | Case A patch chưa có canonical evidence |
| M5 | Phân tích rủi ro và khuyến nghị | Kết quả canonical + nguồn hardening | Chương 4, residual risk, recommendation | Không định lượng ngoài dữ liệu |

## Phạm vi và giả định

- Trong phạm vi: demo canonical Scenario 1/2, Case B, Case C; local patch ground truth; đánh giá giới hạn công cụ.
- Ngoài phạm vi kết quả: exploit/RCE thành công, performance benchmark, Case A patch nếu chưa audit được evidence.
- Giả định: kết luận chỉ áp dụng trong topology/vantage point và trạng thái hệ thống đã ghi nhận.
- Ràng buộc: không bịa data; raw evidence ưu tiên hơn summary; UNKNOWN được giữ là UNKNOWN.

## Tiêu chí đánh giá toàn công trình

1. Mỗi RQ có câu trả lời hoặc giới hạn rõ.
2. 100% experimental result claims trong Chương 3 truy tới Evidence ID.
3. Không có unresolved raw/prose conflict.
4. Phân biệt SOURCE_FACT, AUTHOR_DATA, INTERPRETATION và PROPOSAL.
5. Không đồng nhất OPEN, SMBv1 enabled, UNKNOWN, UNPATCHED và FILTERED.
6. Mọi recommendation quan trọng có nguồn hoặc được ghi rõ là proposal.
7. Báo cáo, DOCX và slide cùng dùng một canonical truth.
