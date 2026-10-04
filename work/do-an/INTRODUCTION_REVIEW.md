# Introduction Review

Ngày 2026-10-04. Báo cáo này thay thế đánh giá ở commit 632bfe4. Người dùng đã cho phép lập IEEE chung từ Mở đầu, giữ nguyên hai chương và ghi bảng chuyển đổi khi ghép. Hợp đồng/ma trận riêng đã được lập trước viết tại INTRODUCTION_CONTRACT.md.

## Content

- Nguồn canonical: INTRODUCTION.md. Ngân sách 1.200–1.500 đơn vị khoảng trắng, không tính heading, citation và bibliography; số cuối sẽ chốt khi QA.
- Sections: đủ 1–7 và hai tiểu mục 2.1/2.2; đã bỏ các nhãn phụ không cần thiết, sửa số mục bị lặp.
- Citation count: 12 lượt, 8 nguồn, xuất hiện đầu tiên [1]–[8]. Bibliography Word trích xuất từ bảng chung, không phải hệ số riêng.
- Unsupported claim count: 0 sau review phạm vi bản mới, không suy ra từ lint. Đã bỏ tuyên bố phổ biến trong doanh nghiệp, số nạn nhân/thiệt hại, NotPetya dẫn nhầm nguồn, kernel/SYSTEM tự động, triệt tiêu nguy cơ và đóng góp mới chưa chứng minh. Mục tiêu, phương pháp, giá trị được viết như đề xuất.

| IEEE / Ledger | Nội dung kiểm | Vị trí nguồn gốc đã đọc | Giới hạn giữ lại |
|---|---|---|---|
| [1] S006 | Chia sẻ tài nguyên, Client/Server và cả hai vai trò trên một máy | Microsoft Learn, SMB components | Không nói tất cả thành phần chạy trong nhân |
| [2] S005 | Tháng 3/2017, sáu CVE, RCE/tiết lộ thông tin, CVE-2017-0144, sửa xử lý yêu cầu | MS17-010, bảng CVE và Vulnerability Information | Không dùng bulletin cho chi tiết FEA hoặc tự đạt SYSTEM |
| [3] S013 | EternalBlue là mã khai thác lỗi bộ nhớ; cảnh báo crash | Rapid7, Description | Không đồng nhất cả nhóm CVE; crash không chứng minh thành công |
| [4] S015 | WannaCry lây lan qua khai thác SMB trên máy chưa cập nhật | Microsoft Security Blog, Attack vector và Protection | Bài gốc có cách ghi CVE khác; chỉ dùng cho cơ chế lây lan, không ánh xạ CVE hoặc quy mô nạn nhân |
| [5] S002 | Direct-hosted SMB dùng TCP 445 | Microsoft Learn, More information | Giới hạn suy luận từ cổng mở là phân tích, không nói cổng mở chứng minh SMB/phiên bản/bản vá |
| [6] S008 | Quản lý bật/tắt SMBv1 phân biệt với SMBv2/v3 | Microsoft Learn, Use the command line or Registry Editor, Detect/Enable/Disable SMB | Không coi cấu hình giao thức là bản vá |
| [7] S024 | Lập kế hoạch, kiểm tra, phân tích, giảm thiểu; phạm vi, ủy quyền, điều kiện dừng | CSRC Abstract; PDF NIST SP 800-115 §6.5, trang in 6-10 đến 6-12 | Quy trình riêng là vận dụng NIST; cô lập/không Bridged là nguyên tắc đề cương/dự án |
| [8] S025 | Tường lửa kiểm soát lưu lượng giữa máy/mạng | CSRC Abstract, SP 800-41 Rev.1 | Không coi tường lửa sửa lỗi xử lý yêu cầu |

Đọc trực tiếp nguồn gốc ngày 2026-10-04; URL trong bibliography và SOURCE_LEDGER. NotebookLM không có công cụ trong lượt này; không tuyên bố đã nhập hoặc đồng bộ notebook. Khả năng kết nối khác trạng thái lỗ hổng và kiểm tra Client là lập luận thiết kế, không quan sát lab. Không thêm nguồn chưa xác minh.

### IEEE toàn báo cáo

GLOBAL_CITATION_MAP.md/json bao phủ 23 định danh VERIFIED theo thứ tự Mở đầu → Chương 1 → Chương 2, ghi SHA256 và bảng chuyển số. MS17-010 là [2] chung, Chương 1 [7] → [2], Chương 2 [5] → [2]. Hai chương canonical giữ nguyên. Bản ghép tạm audit có 110 lượt/23 mục, lần xuất hiện đầu tiên [1]–[23], không thiếu/mồ côi. Audit số không chứng nhận nội dung hai chương. Chương chưa viết sẽ nối tiếp; không đánh số nguồn tương lai trước. Trang/PDF NIST, locale Microsoft Learn, mục con đặc tả và sách Nmap không URL đã được đối chiếu định danh.

## Author voice

Giữ Client/Server, giải thích thuật ngữ lần đầu, đoạn liên tục, câu trực tiếp và câu ghép có quan hệ rõ. Không ép nhịp hoặc độ dài, không bịa động cơ/trải nghiệm/quyết định cá nhân, không tối ưu detector. Đã bỏ thuật ngữ thô, lời tự đánh giá và chi tiết mức hàm không cần cho Mở đầu. Giá trị ở mục 6 là dự kiến có điều kiện dữ liệu.

Lint tư vấn/publication: 0 error, 1 warning VI012. **KEEP_WITH_REASON**: bốn đoạn mục tiêu mở “Mục tiêu thứ ...” để đối chiếu bốn mục tiêu song song O1–O4, không áp khuôn này cho đoạn khác. --publication --fail-on-error đạt vì không có lỗi; không gọi là 0 cảnh báo.

## Scope

- Invented experimental results: NO, count 0; không log/ảnh/số liệu giả.
- Detailed lab/evidence/rollback section added: NO, count 0; không bảng trạng thái, lệnh, tham số hoặc khối quản lý.
- Safety outside Section 5: NO, count 0; ủy quyền, cô lập, không Bridged, dừng và phục hồi chỉ ở mục 5. Phương pháp khảo sát/đối chiếu ở mục 4 và phòng thủ là đối tượng nghiên cứu.
- Chưa có dữ liệu thực nghiệm được nói rõ ở mục 3; không xóa marker các chương khác, không nhận đã chạy lab.

## Word QA

- DOCX path: work/do-an/outputs/MO_DAU_DO_AN.docx.
- HUIT hiện hành: A4; lề trên 3,5/dưới 3/trái 3,5/phải 2 cm; TNR 13pt, giãn dòng 1,5; trước 0/sau 6pt, thụt 1,25cm, căn đều. Dùng ưu tiên hồ sơ HUIT, không sao chép mức 1,3/1,15 lịch sử.
- Title 16pt, Heading 1 14pt, Heading 2 13pt; styles thật, đen; keep-with-next và widow control. PAGE Ả Rập giữa chân trang, từ 1. Bibliography hanging indent riêng. Không trang trí hoặc corporate theme.
- Mẫu tuần 2 và đề mục dùng cho giọng/cấu trúc, không phải template package để sao chép lỗi.
- DOCX validation/heading audit/style consistency/page count: PENDING sau dựng.

## Render QA

PENDING. Chỉ nhận ảnh render mới của chính bản Word cuối; sẽ xem từng trang và ghi bảng.

## Publication checklist riêng Mở đầu

- [x] Hợp đồng và ma trận riêng sẵn sàng trước viết.
- [x] Nguồn, logic, phạm vi và giọng đã review; cảnh báo đã phân loại.
- [x] IEEE chung được người dùng cho phép; hai chương giữ nguyên.
- [x] Không placeholder thiếu thông tin hoặc dữ liệu giả trong Mở đầu.
- [ ] Word cấu trúc/styles/font/unicode/citation/PAGE và tương đương Markdown đạt.
- [ ] Render mới và xem từng trang, không còn lỗi bố cục.
- [ ] validate_project, unittest, git diff --check cuối lượt đạt.

PUBLICATION_CHECKLIST.md toàn luận văn vẫn BLOCKED; kiểm định riêng Mở đầu không mở cổng các chương/dữ liệu còn thiếu.

## Final status

CONTENT_REVIEW_PASSED_WORD_QA_PENDING
