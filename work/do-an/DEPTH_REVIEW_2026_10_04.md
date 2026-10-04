# Sửa chiều sâu lập luận Chương 1–2 ngày 2026-10-04

Trạng thái: DEPTH_REVISED_REVIEW_PENDING. Lượt này tiếp nhận phản hồi bản báo cáo thiếu chiều sâu và không giải thích rõ vấn đề. Hai chương đã được sửa trực tiếp; báo cáo này chỉ lưu phạm vi và căn cứ thay đổi, không thay cho nội dung chương.

## Nội dung đã viết lại

| Vấn đề ở bản trước | Diễn giải đã bổ sung | Vị trí đọc |
|---|---|---|
| Liệt kê thế hệ SMB và thuật toán nhưng chưa giải thích mục đích | Gộp thao tác giảm lượt chờ; signing kiểm tra toàn vẹn; encryption bảo vệ dữ liệu truyền; tính năng hỗ trợ chưa bằng đã dùng | Chương 1, 1.1.3 |
| Chuỗi Negotiate/Session Setup/Tree Connect chỉ là tên bước | Mỗi bước trả lời phiên bản, danh tính hay tài nguyên; xác thực có thể nhiều lượt; quyền tài nguyên được xét riêng | Chương 1, 1.1.5 |
| Root cause FEA được mô tả như tự động dẫn tới SYSTEM | Quan hệ vùng nhớ cấp phát/lượng ghi; ví dụ 64/80 byte giả định; tràn có thể làm dừng hệ thống; thực thi là bước tiếp cần điều kiện | Chương 1, 1.2.3 |
| Nhãn công cụ và giới hạn chủ yếu thành danh sách | Giải thích mất phản hồi, lỗi IPC$ và phản hồi thăm dò; ba Server cùng mở cổng có rủi ro khác nhau | Chương 1, 1.3.2–1.3.3, 1.4.2 |
| Các biện pháp phòng thủ mới là danh mục | Phân tích vị trí tác động của vá, tắt SMBv1, lọc mạng; ghép phép kiểm tra điều kiện với tác vụ Client | Chương 1, 1.4.3; Chương 2, 2.3 |
| Thiết kế mạng chưa giải thích lý do chọn | Hai nguồn ở VLAN khác nhau phân biệt chặn theo nguồn với mất dịch vụ; phản hồi kết nối SMB khác một kết nối ngược mới | Chương 2, 2.2 |
| Mười trường kỹ thuật lặp lời mô tả nhưng còn lỗi suy luận | Thêm đoạn giải thích trước bảng, giữ đủ mười trường; không giả định R trước khi đo; thiếu phản hồi phiên bản là Unknown | Chương 2, 2.4 |
| Ma trận và khôi phục chỉ là thủ tục | Mã lượt nối bằng chứng cùng thời điểm; PCAP đa điểm định vị chiều lỗi; snapshot trở về khác với nghiệp vụ sẵn sàng | Chương 2, 2.5 |

Các đoạn dùng quan hệ cơ chế → hệ quả có điều kiện rõ. Đã bỏ nhãn phụ trong phần phiên bản SMB và chuyển trạng thái thành diễn giải liên tục. Bảng mười trường giữ để đối chiếu tiêu chí theo hợp đồng, không thay thế phân tích.

## Nguồn và giới hạn

Đã đọc gốc Microsoft, Nmap, Rapid7 và NIST theo vị trí ghi ở SOURCE_LEDGER. Bổ sung S029 cho script phiên bản và S030 cho scanner phụ trợ, thay vì viện dẫn module khai thác cho mọi hành vi scanner. Chỉnh năm S007 thành 2025 và S023 thành 2024 theo ngày cập nhật thật; năm truy cập không dùng làm năm xuất bản.

Ví dụ 64/80 byte và các tình huống Server đều ghi rõ giả định. Không chạy lab, không tạo log, không điền ma trận bằng chứng. Giữ phạm vi DEC-03, mô hình ba VLAN và bốn trạng thái đã chốt. Không sửa hợp đồng LOCKED chứa công thức iff và giá trị giả định; bản chương dùng quan hệ điều kiện cần và trạng thái theo bằng chứng, mâu thuẫn hợp đồng vẫn ghi ở PROJECT_STATE.

## Dung lượng và đánh số

Chương 1: 7,364 đơn vị; Chương 2: 5,136 đơn vị. Đếm theo khoảng trắng, gồm nội dung bảng, loại khối mã/sơ đồ và bibliography. Đây là thước đo biên tập nhất quán, không phải đếm từ vựng tiếng Việt. Chương 1 nằm trong 7.000–8.500; Chương 2 cao hơn trần hợp đồng 4.500 nhưng dưới biên 15% (5.175). Chương 2 đã rút mô tả lặp để giữ phân tích mới trong biên đó; không tự đổi ngân sách LOCKED.

Ánh xạ sau lượt sửa: số cũ là danh mục tại commit 89ad169; những nguồn bổ sung được ghi riêng.

| Chương | Số trước → số hiện hành |
|---|---|
| CHAPTER_1.md | 1→1, 2→2, 3→3, 5→4, 4→7, 6→8, 7→9, 8→10, 9→11, 10→12, 11→13, 12→14, 13→15, 14→16, 15→17, 16→18, 17→19, 18→21; bổ sung tạm 19→5, tạm 20→20, tạm 21→22, tạm 22→6 |
| CHAPTER_2.md | 1→1, 2→2, 3→3, 4→4, 5→5, 6→6, 7→7, 8→10; bổ sung tạm 9→8, tạm 10→9 |

## Kiểm tra và phần còn mở

Citation cấu trúc riêng chương: Chương 1 có 78 lượt/22 mục; Chương 2 có 20 lượt/10 mục, không thiếu hoặc mồ côi. Đây là kiểm tra cấu trúc; review nội dung nguồn ở các hàng phía trên mới xác định phạm vi hỗ trợ. Một câu 71 đơn vị đã được sửa để tách chuỗi ba hệ quả nhưng giữ quan hệ nhân quả. Các cảnh báo caption và ví dụ giả định được ghi quyết định trong STYLE_REVIEW.

Chưa có dữ liệu lab, chưa hợp nhất IEEE toàn báo cáo và chưa dựng Word mới. Bản Word cũ không chứa lượt sửa này. Nội dung chương đang chờ phản hồi tác giả; không tự gắn PASS G5/G6 từ linter hoặc kiểm thử repository.

S031 bổ sung cho SHA-512, quan hệ giá trị băm → tạo khóa và ngoại lệ guest/anonymous; vị trí Summary/Overview/Pre-auth integrity hash. Đây là phần giải thích mới trong 1.1.3, chưa phải cấu hình được thử trên Windows 7.

Kiểm tra hoàn tất: validate_project.py đạt; unittest 7/7 đạt; citation audit riêng hai chương đạt; git diff --check không có lỗi whitespace. Lint còn ba cảnh báo đã phân loại. Các kiểm tra này không xác nhận kết quả thực nghiệm hoặc bản Word mới.
