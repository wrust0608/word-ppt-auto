# Kế hoạch đối soát bibliography Chương 1

- Ngày: 2026-10-04.
- Trạng thái hiện hành: `APPLIED_REVIEW_PENDING`; xem REVISION_PASS_2026_10_04.md.
- Bảng tuyến ban đầu dưới đây được giữ để truy vết. Số IEEE và nội dung chương đã được đồng bộ trong lượt biên tập tiếp theo; dùng ánh xạ trong báo cáo mới.
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


## Đọc nguồn gốc đầu tiên ngày 2026-10-04

Đọc trực tiếp nguồn gốc qua web; không phải tái kiểm tra nguồn trong NotebookLM.

- S020: trang Microsoft hiện có tiêu đề “What is Microsoft SMB Protocol and CIFS Protocol?”, Last updated 2025-07-10. Các mục Overview hỗ trợ chức năng file sharing, printing, authentication, locking, named pipes và mô hình request/response Client–Server. Không đủ để chứng minh chi tiết driver nội bộ Windows. URL: https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview
- S006: Last updated 2025-11-27. Đã đọc mục giới thiệu, SMB components và SMB dialects; hỗ trợ vai trò Client/Server, UNC, read/create/update file và bảng phiên bản. Không dùng overview này để chứng minh kiến trúc user/kernel. URL: https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview
- S018: mở mã nguồn hiện hành; tìm chuỗi `unsafe` không thấy. Đây là dấu hiệu cần kiểm tra lại phát biểu Chương 2 về `--script-args unsafe=0`, chưa kết luận rằng tất cả thư viện/phiên bản Nmap không có cơ chế liên quan. Cần đọc code và thư viện phụ thuộc trước sửa quyết định kỹ thuật. URL: https://svn.nmap.org/nmap/scripts/smb-vuln-ms17-010.nse

Năm 2026 trong ledger của S006/S020 trước đây là sai lệch với ngày cập nhật hiển thị, đã đổi sang 2025 và ghi ngày truy cập riêng. Chưa áp dụng citation vào chương.
