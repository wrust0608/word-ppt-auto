# Kế hoạch đối soát bibliography Chương 1

- Ngày: 2026-10-04.
- Trạng thái: `PLANNED_NOT_APPLIED`.
- Không đổi số IEEE hoặc nội dung chương trong lượt này.
- Bảng dưới là tuyến kiểm tra dựa trên ledger hiện hành, chưa xác nhận mọi phát biểu có thể thay nguồn nguyên trạng. Chỉ gán số mới theo lần xuất hiện sau khi sửa được duyệt.

| Số cũ / nguồn | Tuyến xử lý | Giới hạn cần kiểm chứng |
|---|---|---|
| [1] S001 | Đối chiếu khái niệm/chức năng với S020, S006; phiên bản với S021/S022 | Không dùng overview để thay mọi lý thuyết mạng trong sách |
| [2] S002 | Giữ nếu câu khớp tài liệu gốc | Hành vi lựa chọn cổng phải có điều kiện theo Windows/cấu hình |
| [3] S003; [4] S004 | Đối chiếu phần giao thức với S021/S022, lỗ hổng với S013; giữ RECHECK cho nội dung nội bộ Windows | Đặc tả giao thức không chứng minh kiến trúc driver/user-mode/kernel-mode; cần nguồn riêng hoặc thu hẹp câu |
| [5] S005 | Giữ sau kiểm tra bulletin/KB | Không khái quát mọi CVE thành một cơ chế FEA |
| [6] S006 | Cập nhật URL/tên tài liệu hiện hành trong ledger | Phải xác minh ngày phiên bản; năm 2026 trong ledger chưa tự chứng minh năm xuất bản |
| [7] S007; [8] S008 | Giữ sau kiểm tra theo dialect/hệ điều hành | Không gộp thuật toán mọi SMBv3 hoặc thao tác mọi Windows |
| [9] S009 | Chính sách tường lửa đối chiếu S025; retest đối chiếu S024; phát biểu khác kiểm riêng | Không thay toàn sách McNab bằng một hướng dẫn tường lửa |
| [10] S010; [11] S011; [12] S012; [13] S013 | Giữ và kiểm phạm vi từng câu | Phân biệt EternalSynergy, EternalBlue, EternalRomance và cảnh báo rủi ro |
| [14] S014 | Đối chiếu các phát biểu WannaCry với S015; nếu cần chỉ báo CISA thì tìm bản chính thức | Không đổi citation sang S015 khi nguồn đó không hỗ trợ chi tiết; không tự giữ số liệu chưa đọc |
| [15] S015 | Giữ nếu nội dung khớp | Kiểm lại số liệu, ngày và phạm vi mô tả |
| [16] S016 | Mô tả Kali đối chiếu S026; ủy quyền/quy trình đối chiếu S024 | Snapshot/cấu hình cụ thể là đề xuất thiết kế, không giả làm khuyến nghị nguyên văn NIST |
| [17] S017; [18] S018 | Giữ, kiểm đúng mục/mã nguồn | Phân biệt dấu hiệu NSE với khai thác; xác minh phiên bản và tham số an toàn từ code |
| [19] S019 | Module cụ thể đối chiếu S013; kiến trúc framework cần tài liệu gốc công cụ | Trang module không thay toàn bộ sách Metasploit |

## Quy trình áp dụng sau duyệt giọng

1. Liệt kê mọi câu đang dẫn nhóm RECHECK và ghi source mới hỗ trợ toàn bộ/một phần/không hỗ trợ.
2. Đọc đoạn gốc và ghi vị trí thật; không bịa số trang hoặc dùng NotebookLM thay nguồn.
3. Thu hẹp phát biểu khi bằng chứng chỉ hỗ trợ một phần; giữ nhãn thiếu nguồn cho phần còn mở.
4. Lập bảng source ID → số IEEE mới theo thứ tự xuất hiện; đồng bộ citation/bibliography trong một diff.
5. Review nghĩa và chạy citation audit, linter; trình tác giả duyệt chương trước xuất DOCX.

## Mâu thuẫn hồ sơ cần xử lý

Claim matrix cũ vẫn có câu “Không còn mâu thuẫn nguồn / toàn bộ 19 tài liệu”; ledger có 7 nguồn RECHECK. Các truy vấn Q001/Q002 từng CLOSED còn dựa vào S003/S009 chưa khả dụng. Các trạng thái này cần mở lại, không dùng làm chứng cứ đã hoàn tất.
