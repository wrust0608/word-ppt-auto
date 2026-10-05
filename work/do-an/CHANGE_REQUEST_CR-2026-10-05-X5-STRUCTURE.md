# CHANGE REQUEST CR-2026-10-05-X5-STRUCTURE

Trạng thái: `APPROVED_BY_USER`  
Ngày: 2026-10-05  
Phạm vi: Chương 2 — cấu trúc và tái biên soạn nội dung.

## 1. Lý do thay đổi

Bản X5 trước đã đạt CP5-TECH 96/100 và 0 blocker về kỹ thuật/evidence, nhưng người dùng yêu cầu phản biện lại ở cấp cấu trúc trước khi xét nội dung.

Kết luận: cấu trúc cũ 9 H2 / 42 H3 quá phân mảnh, có nhiều heading ngắn và vai trò chồng lấn giữa baseline, evidence, snapshot, scenario và evaluation.

Người dùng đã trực tiếp duyệt cấu trúc mới dưới đây và yêu cầu dùng nó làm khung điều khiển cho việc viết lại Chương 2.

## 2. Cấu trúc Chương 2 được duyệt

# CHƯƠNG 2. THIẾT KẾ MÔ HÌNH VÀ PHƯƠNG PHÁP THỰC NGHIỆM

## 2.1. Thiết kế nghiên cứu và phạm vi thực nghiệm
### 2.1.1. Mục tiêu của mô hình thực nghiệm
### 2.1.2. Phạm vi và nguyên tắc an toàn
### 2.1.3. Nguyên tắc cô lập, tái lập và kiểm soát biến

## 2.2. Kiến trúc và trạng thái ban đầu của môi trường lab
### 2.2.1. Kiến trúc VirtualBox và mạng Host-Only
### 2.2.2. Máy kiểm thử Kali Linux
### 2.2.3. Máy mục tiêu Windows Server 2012 R2
### 2.2.4. Baseline mạng, SMB và Windows Firewall
### 2.2.5. Baseline bản vá MS17-010 và snapshot

## 2.3. Phương pháp thu thập và diễn giải bằng chứng
### 2.3.1. Các lớp quan sát
### 2.3.2. Dữ liệu thô và khả năng truy vết
### 2.3.3. Quy tắc xử lý UNKNOWN, NO OUTPUT và FILTERED
### 2.3.4. Ranh giới suy luận

## 2.4. Thiết kế Kịch bản 1 — Khảo sát dịch vụ SMB
### 2.4.1. Mục tiêu và trình tự thực hiện
### 2.4.2. Bộ phép đo và bằng chứng cần thu
### 2.4.3. Điều kiện dừng và giới hạn kết luận

## 2.5. Thiết kế Kịch bản 2 — Đánh giá cấu hình SMB và MS17-010
### 2.5.1. Bốn phép đo NSE-SMB-01 đến NSE-SMB-04
### 2.5.2. Đối chiếu remote signal với trạng thái bản vá nội bộ
### 2.5.3. Giới hạn kết luận

## 2.6. Thiết kế kiểm thử các biện pháp giảm thiểu
### 2.6.1. Nguyên tắc kiểm thử vi sai
### 2.6.2. Case B — Vô hiệu hóa SMBv1
### 2.6.3. Case C — pfSense Transparent Bridge
### 2.6.4. Vai trò của cập nhật bản vá
### 2.6.5. Ma trận biến can thiệp và phép đo lại

## 2.7. Khung đánh giá kết quả
### 2.7.1. Reachability và service exposure
### 2.7.2. Protocol surface
### 2.7.3. Remote vulnerability signal và local patch state
### 2.7.4. Hiệu quả và giới hạn của biện pháp giảm thiểu

## 2.8. Tổng kết chương

Tổng: 8 H2, 25 H3.

## 3. Vai trò duy nhất của từng cụm

- 2.1 trả lời: vì sao thiết kế như vậy, phạm vi ở đâu, biến được kiểm soát ra sao.
- 2.2 trả lời: lab gồm những gì và trạng thái xuất phát là gì.
- 2.3 trả lời: đo bằng loại bằng chứng nào và được suy luận tới đâu.
- 2.4 chỉ mô tả Scenario 1.
- 2.5 chỉ mô tả Scenario 2.
- 2.6 chỉ mô tả mitigation/differential testing.
- 2.7 chỉ định nghĩa tiêu chí dùng để đọc kết quả ở Chương 3.
- 2.8 khép chương và chuyển sang Chương 3.

## 4. Quy tắc cấu trúc

- Không thêm H3 mới nếu không có Change Request.
- Không gộp hoặc đổi tên H2/H3.
- Không đưa pfSense vào topology baseline; pfSense chỉ xuất hiện chính thức tại Case C.
- Không đưa result thực nghiệm chi tiết vào Chương 2 ngoài baseline fact cần thiết để định nghĩa trạng thái xuất phát.
- Chương 2 trả lời HOW / WITH WHAT / UNDER WHAT CONDITIONS.
- Chương 3 trả lời WHAT HAPPENED.
- Không lặp snapshot/evidence ở nhiều mục nếu vai trò đã được giao cho một mục cụ thể.
- Một heading phải có chức năng riêng; không tạo heading chỉ để chứa một đoạn ngắn.

## 5. Truth boundary giữ nguyên

Không thay đổi:
- EXPERIMENTAL_TRUTH_MATRIX;
- Evidence Register;
- Negative Result Policy;
- Scenario 1 không kết luận MS17-010;
- Scenario 2 remote verdict = UNKNOWN / NO USABLE SCRIPT RESULT;
- local patch state = UNPATCHED;
- SMBv1 disabled != patched;
- FILTERED != patched;
- Case A = theoretical/reference only cho tới khi có canonical evidence.

## 6. Trạng thái workflow

- Candidate cũ commit `ba0cd980a0075427959567d4793dc1e35b95773d` được giữ làm baseline kỹ thuật đã kiểm định.
- CP5-TECH cũ không tự động áp dụng cho bản cấu trúc mới.
- X5 được REOPEN có kiểm soát cho structural rewrite.
- Nhánh làm việc: `feature/x5-chapter-2-structural-revision`.
- Bản viết lại phải qua external review mới trước khi trình người dùng.
- X6 vẫn BLOCKED.
