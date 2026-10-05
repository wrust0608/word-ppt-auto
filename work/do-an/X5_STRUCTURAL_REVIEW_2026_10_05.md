# X5 STRUCTURAL REVIEW — CHAPTER 2

Ngày: 2026-10-05  
Nguồn so sánh: hướng dẫn trình bày khóa luận HUIT và các đồ án ngành An toàn thông tin PTIT giai đoạn 2024–2025.  
Candidate gốc: ba0cd980a0075427959567d4793dc1e35b95773d  
Mục tiêu: phản biện lại logic trình bày sau CP5-TECH, theo yêu cầu trực tiếp của người dùng.

## 1. Kết luận phản biện

Bản CP5-TECH hiện tại đúng kỹ thuật nhưng chưa phải cấu trúc trình bày tối ưu cho một báo cáo đồ án ATTT.

Vấn đề lớn nhất không còn nằm ở evidence hay technical correctness mà ở cách tổ chức chương:
- 9 mục cấp 2 và 42 mục cấp 3 trên khoảng 4,6 nghìn từ làm nội dung bị chia quá vụn;
- nhiều tiểu mục chỉ chứa một đoạn ngắn, tạo cảm giác checklist hoặc tài liệu vận hành;
- các thuật ngữ quản trị nội bộ như canonical, ground truth, Evidence ID xuất hiện quá nhiều trong prose chính;
- ASCII art phù hợp tài liệu kỹ thuật nội bộ nhưng không nên là hình chính của báo cáo Word;
- danh mục tài liệu tham khảo không nên lặp ở cuối riêng Chương 2 khi báo cáo cuối có bibliography chung;
- phần baseline, phương pháp đo, thiết kế kịch bản và tiêu chí đánh giá đang đúng nhưng bị trải ra quá nhiều heading nên quan hệ nguyên nhân → phép đo → tiêu chí không nổi bật.

## 2. Mẫu cấu trúc tham khảo rút ra

Các đồ án ATTT gần chủ đề thực nghiệm thường dùng logic:
1. Cơ sở lý thuyết / tổng quan.
2. Phân tích thiết kế, xây dựng môi trường hoặc phương pháp.
3. Thực nghiệm và đánh giá.

Một số đề tài tách thêm chương kết quả hoặc giải pháp, nhưng điểm chung là chương phương pháp tập trung trả lời:
- môi trường được xây dựng thế nào;
- biến nào được kiểm soát;
- phép đo nào được dùng;
- tiêu chí kết luận là gì.

Dữ liệu quan sát thực tế, ảnh chạy lệnh, log và kết quả so sánh được dành cho chương thực nghiệm.

## 3. Kiến trúc đề xuất cho Chương 2

### 2.1. Mục tiêu, phạm vi và nguyên tắc thực nghiệm
- 2.1.1. Mục tiêu của mô hình
- 2.1.2. Phạm vi và nguyên tắc an toàn
- 2.1.3. Khả năng phục hồi và truy vết bằng chứng

### 2.2. Kiến trúc môi trường lab
- 2.2.1. Mô hình VirtualBox và mạng Host-Only
- 2.2.2. Máy kiểm thử Kali Linux
- 2.2.3. Máy mục tiêu Windows Server 2012 R2
- 2.2.4. Vai trò pfSense trong Case C

### 2.3. Chuẩn bị trạng thái ban đầu
- 2.3.1. Trạng thái mạng, dịch vụ SMB và Windows Firewall
- 2.3.2. Xác định trạng thái bản vá MS17-010
- 2.3.3. Công cụ, snapshot và dữ liệu bằng chứng

### 2.4. Mô hình đo và nguyên tắc diễn giải
- 2.4.1. Các lớp quan sát
- 2.4.2. Quy tắc xử lý UNKNOWN, NO OUTPUT và FILTERED
- 2.4.3. Thu thập và ưu tiên dữ liệu bằng chứng

### 2.5. Thiết kế hai kịch bản kiểm thử
- 2.5.1. Kịch bản 1 — khảo sát dịch vụ SMB
- 2.5.2. Kịch bản 2 — đánh giá cấu hình SMB và dấu hiệu MS17-010
- 2.5.3. Ma trận phép đo và điều kiện dừng

### 2.6. Thiết kế kiểm thử biện pháp giảm thiểu
- 2.6.1. Nguyên tắc kiểm thử vi sai
- 2.6.2. Case B — vô hiệu hóa SMBv1
- 2.6.3. Case C — lọc TCP 139/445 bằng pfSense
- 2.6.4. Vai trò của cập nhật bản vá
- 2.6.5. Ma trận biến can thiệp

### 2.7. Tiêu chí đánh giá
- 2.7.1. Reachability, service và protocol surface
- 2.7.2. Remote signal và trạng thái bản vá nội bộ
- 2.7.3. Hiệu quả và giới hạn của mitigation

### 2.8. Tổng kết chương

Tổng: 8 mục cấp 2, 24 mục cấp 3. Mục tiêu là giảm phân mảnh mà không mất bất kỳ claim hoặc evidence boundary nào.

## 4. Quy tắc biên tập

- Chương 2 chỉ trả lời HOW / WITH WHAT / UNDER WHAT CONDITIONS.
- Chương 3 trả lời WHAT HAPPENED.
- Không dùng kết quả open, filtered, dialect list hay NSE output như kết quả trong Chương 2, trừ các baseline fact cần để định nghĩa trạng thái xuất phát.
- Không biến no-output thành safe.
- Không biến filtered thành patched.
- Không biến SMBv1 disabled thành patched.
- Case A chỉ là tham chiếu lý thuyết cho vai trò patch.
- Giảm thuật ngữ quản trị nội bộ trong prose; giữ chúng ở phụ lục QA/evidence.
- Hình 2.1–2.3 phải được dựng lại dạng sơ đồ vector/diagram khi tạo DOCX; không dùng ASCII art làm hình chính.
- Tài liệu tham khảo được quản lý ở bibliography toàn báo cáo, không lặp danh mục riêng sau mỗi chương.

## 5. Trạng thái

CP5-TECH cũ vẫn được giữ nguyên làm baseline đã kiểm định.  
Nhánh structural revision không thay thế candidate cũ cho tới khi người dùng trực tiếp duyệt bản mới.
