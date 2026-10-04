# Báo cáo kiểm định chương mẫu

**Tài liệu:** `CHAPTER_1.md`  
**Ngày kiểm định:** 2026-10-04  
**Trạng thái:** `REVIEW_COMPLETE_FIX_REQUIRED`

> Cập nhật sau biên tập: `REVISED_REVIEW_PENDING`. Các thống kê và số dẫn trong phần kiểm định ban đầu phía dưới là lịch sử. Bản hiện hành dùng 18 mục/88 lượt dẫn; nguồn sách và CISA chưa khả dụng đã được thay, bỏ hoặc thu hẹp theo nguồn gốc. Xem REVISION_PASS_2026_10_04.md và ánh xạ citation trong đó. Lint còn một cảnh báo caption đã phân loại FALSE_POSITIVE; giọng được tác giả xác nhận hoàn tất. Chưa phê duyệt chương hoặc dựng DOCX.

## 1. Kết luận ngắn

Chương 1 có cấu trúc hợp lý, độ dài nằm sát ngân sách và hệ thống trích dẫn IEEE khép kín về mặt hình thức. Tuy nhiên, chương **chưa qua cổng duyệt nội dung** vì một số tài liệu trong danh mục hiện chưa có bản nguồn khả dụng trong NotebookLM. Việc đánh số trích dẫn đúng không thay thế cho kiểm chứng nguồn.

## 2. Kết quả kiểm định

| Hạng mục | Kết quả | Nhận xét |
|---|---|---|
| Phạm vi chương | Đạt có điều kiện | Khoảng 8.536 từ; cao hơn ngân sách 8.500 từ khoảng 0,4%, không tạo sai lệch đáng kể. |
| Phân cấp đề mục | Đạt | Hệ thống heading cấp 1–4 liên tục và phù hợp logic chương. |
| Trích dẫn IEEE về hình thức | Đạt | Có 134 lượt dẫn; sử dụng đủ và liên tục `[1]`–`[19]`; không có tham chiếu mồ côi hoặc số bị thiếu. |
| Điều kiện nguồn NotebookLM | Không đạt | Các nguồn `[1]`, `[3]`, `[4]`, `[9]`, `[14]`, `[16]`, `[19]` chưa có bản nguồn hợp lệ/khả dụng trong NotebookLM hoặc URL hiện lỗi. |
| Độ chính xác metadata | Cần sửa | URL của nguồn `[6]` trong danh mục chương là đường dẫn Microsoft Learn cũ và phải đổi sang nguồn hiện hành. |
| Văn phong | Cần sửa | Bộ kiểm tra phát hiện 18 cảnh báo: 17 câu quá dài và 1 kiểu mở đoạn lặp lại. |
| Dấu ấn tác giả | Đã chốt lựa chọn, chờ áp dụng vào chương | DEC-22 ngày 2026-10-04 ghi lựa chọn thật 1B, 2A, 3A; AUTHOR_VOICE_CALIBRATION đã cập nhật. |

## 3. Các sửa đổi bắt buộc trước khi duyệt chương

1. Nhập bản hợp lệ của các nguồn sách/tài liệu `[1]`, `[3]`, `[4]`, `[9]`, `[16]`, `[19]` vào NotebookLM, hoặc thay từng luận điểm bằng nguồn chính thức/học thuật đã có trong NotebookLM.
2. Thay nguồn `[14]` có URL CISA lỗi bằng nguồn còn truy cập được và kiểm tra lại chính xác luận điểm đang dựa vào nguồn này.
3. Cập nhật nguồn `[6]` sang trang Microsoft Learn hiện hành và đối chiếu lại tên tài liệu, ngày truy cập.
4. Xử lý 17 câu quá dài theo nguyên tắc: mỗi câu chỉ giữ một quan hệ lập luận chính; không tách cơ học làm mất quan hệ nguyên nhân–hệ quả.
5. Viết lại đoạn có cách mở đầu lặp “Sơ đồ 1...” để chuyển từ mô tả hình sang giải thích ý nghĩa của hình đối với luận điểm.
6. Áp dụng bộ dấu giọng đã duyệt theo DEC-22 vào chương sau đối soát nguồn và logic; kiểm tra lại bằng bộ lint, giữ câu ghép cơ chế → hệ quả khi quan hệ rõ.

## 4. Điều kiện chuyển bước

Chỉ đổi trạng thái thành `APPROVED_FOR_MERGE` khi đồng thời thỏa mãn:

- mọi khẳng định học thuật quan trọng truy được tới một nguồn đang có trong NotebookLM và một dòng trong `SOURCE_LEDGER.md`;
- không còn nguồn lỗi hoặc nguồn chỉ được ghi trong danh mục nhưng không có bản để kiểm chứng;
- tác giả đã duyệt mẫu giọng viết;
- các cảnh báo văn phong đã được xử lý hoặc có lý do giữ lại;
- chạy lại kiểm tra trích dẫn không phát sinh tham chiếu thiếu, mồ côi hoặc sai thứ tự.
