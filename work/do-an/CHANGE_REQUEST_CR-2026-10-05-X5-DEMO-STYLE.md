# CHANGE REQUEST CR-2026-10-05-X5-DEMO-STYLE

Trạng thái: `APPROVED_BY_USER`  
Ngày: 2026-10-05  
Phạm vi: Chương 2 — thay đổi cách trình bày từ technical-review style sang đồ án demo thực nghiệm.

## 1. Lý do thay đổi

Candidate R5 đạt CP5-TECH 96/100 về technical truth, evidence boundary và QA, nhưng người dùng trực tiếp đánh giá cách trình bày chưa phù hợp với một báo cáo đồ án có demo.

Nhận xét của người dùng:
- nội dung đang giống báo cáo trình leader/QA;
- quá nhiều framework/evidence/governance language;
- chưa tạo cảm giác tự nhiên của một chương mô tả dựng lab và kịch bản demo;
- hướng đúng phải đơn giản, dễ hiểu, đúng trọng tâm.

Vì vậy:
- giữ R5 làm technical baseline/reference;
- không dùng cấu trúc R5 làm presentation structure cuối;
- viết lại Chương 2 theo demo-first structure đơn giản hơn;
- không thay đổi Experimental Truth Matrix, Evidence Register, Source Ledger hoặc các technical locks.

## 2. Tiêu đề chương mới

# CHƯƠNG 2. XÂY DỰNG MÔ HÌNH THỰC NGHIỆM VÀ KỊCH BẢN DEMO

## 3. Cấu trúc được người dùng duyệt theo hướng đơn giản

## 2.1. Mô hình thực nghiệm
### 2.1.1. Mục tiêu của mô hình
### 2.1.2. Sơ đồ và thành phần của mô hình
### 2.1.3. Thông số môi trường thực nghiệm

## 2.2. Cài đặt và cấu hình môi trường
### 2.2.1. Cấu hình mạng Host-Only trên VirtualBox
### 2.2.2. Cấu hình máy Kali Linux
### 2.2.3. Cấu hình máy Windows Server 2012 R2
### 2.2.4. Cấu hình SMB và Windows Firewall
### 2.2.5. Kiểm tra bản vá MS17-010 và tạo snapshot

## 2.3. Kịch bản Demo 1 — Khảo sát dịch vụ SMB bằng Nmap
### 2.3.1. Mục tiêu và phạm vi
### 2.3.2. Quy trình và các lệnh thực hiện
### 2.3.3. Nội dung cần quan sát và giới hạn kết luận

## 2.4. Kịch bản Demo 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE
### 2.4.1. Mục tiêu và điều kiện ban đầu
### 2.4.2. Quy trình kiểm tra NSE-SMB-01 đến NSE-SMB-04
### 2.4.3. Đối chiếu với trạng thái bản vá và giới hạn kết luận

## 2.5. Kiểm thử các biện pháp giảm thiểu
### 2.5.1. Nguyên tắc kiểm thử trước và sau can thiệp
### 2.5.2. Case B — Vô hiệu hóa SMBv1
### 2.5.3. Case C — Kiểm soát TCP 139/445 bằng pfSense
### 2.5.4. Vai trò của cập nhật bản vá

## 2.6. Thu thập dữ liệu phục vụ đánh giá
### 2.6.1. Log và ảnh chụp thực nghiệm
### 2.6.2. Nguyên tắc diễn giải kết quả

## 2.7. Tổng kết chương

Tổng: 7 H2 / 20 H3.

## 4. Logic trình bày bắt buộc

Người đọc phải hiểu theo thứ tự tự nhiên:

1. Lab gồm những gì?
2. Cấu hình như thế nào?
3. Demo 1 chạy gì?
4. Demo 2 chạy gì?
5. Thử biện pháp giảm thiểu như thế nào?
6. Kết quả được lưu để Chương 3 phân tích ra sao?

Không biến Chương 2 thành:
- tài liệu governance;
- technical design review;
- evidence framework memo;
- QA report;
- methodology paper.

## 5. Quy tắc nội dung

- Evidence IDs vẫn tồn tại trong repo/self-review, không đưa dày đặc vào prose chính.
- Không dùng các từ nội bộ như canonical, ground truth, truth matrix, gate, CP, locked candidate trong nội dung báo cáo.
- Không lấy mô hình 5 lớp làm xương sống chương. Chỉ giữ các ranh giới suy luận cần thiết ở 2.6.2.
- Không kể kết quả thực nghiệm chi tiết; Chương 3 mới trình bày output/screenshot/result.
- Chương 2 được phép nêu baseline facts để mô tả môi trường thật.
- Mỗi subsection phải trả lời một câu hỏi trực tiếp, không mở rộng thành framework.

## 6. Technical baseline giữ nguyên từ R5

Candidate R5:
`97faf32564191ab0b590bf02e287c6c4935cbbdc`

R5 chỉ dùng để:
- tái sử dụng technical facts chính xác;
- tái sử dụng source mapping;
- tránh hồi quy kỹ thuật;
- KHÔNG tái sử dụng cấu trúc hoặc phong cách presentation.

## 7. Workflow

Branch mới:
`feature/x5-chapter-2-demo-style`

- X5 được REOPEN về presentation/content architecture.
- CP5-TECH của R5 chỉ áp dụng cho technical baseline, không áp dụng cho bản demo-style mới.
- Bản demo-style phải external review lại.
- CP5-USER = PENDING.
- X6 = BLOCKED.
