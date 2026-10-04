# Báo cáo di chuyển hệ thống văn phong

- Ngày kiểm tra: 2026-10-04
- Công cụ: `.agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py`
- Phạm vi: `CHAPTER_1.md`, `CHAPTER_2.md`
- Chế độ: tư vấn biên tập; chưa phải kiểm tra xuất bản.
- Quyết định bảo toàn: không tự sửa tài liệu đã khóa và không thay đổi khẳng định kỹ thuật nếu chưa kiểm tra nguồn.

## Kết quả

| Tài liệu | Câu dài `VI011` | Mở đoạn lặp `VI012` | Rule cụm từ `VI001–VI010` | Trạng thái |
|---|---:|---:|---:|---|
| `CHAPTER_1.md` | 17 | 1 | 0 | Cần biên tập nhịp câu trước G5/G6 |
| `CHAPTER_2.md` | 12 | 2 | 0 | Cần biên tập nhịp câu trước G5/G6 |

## Nhận định

- Hai chương không kích hoạt các mẫu sáo ngữ, quy nguồn mơ hồ hoặc tự xếp hạng trong nhóm rule `VI001–VI010`.
- Điểm cần xử lý chính là câu chứa quá nhiều mệnh đề kỹ thuật. Khi tách câu, phải giữ nguyên quan hệ điều kiện, cơ chế và giới hạn suy luận.
- Các cảnh báo mở đoạn lặp cần được đọc trong ngữ cảnh. Nếu sự lặp xuất phát từ cách dẫn chiếu sơ đồ hoặc một mẫu mô tả có chủ đích, có thể giữ và ghi lý do.
- Linter không xác nhận tính đúng của thông tin SMB, mã lỗi, phiên bản, tham số hoặc trích dẫn. Phần đó vẫn thuộc review nguồn và review kỹ thuật.

## Trình tự xử lý

1. Khóa lại nguồn và phạm vi của đoạn cần sửa.
2. Tách câu tại ranh giới giữa cơ chế, điều kiện và hệ quả; không thay bằng câu ngắn rời rạc.
3. So sánh từng citation trước và sau khi sửa.
4. Chạy lại linter; phân loại từng cảnh báo còn lại thành `FIX`, `KEEP_WITH_REASON` hoặc `FALSE_POSITIVE`.
5. Chỉ sau khi nội dung được duyệt mới sinh lại DOCX và kiểm tra trực quan toàn bộ trang.

## Điều kiện kết thúc

Báo cáo này chưa phải xác nhận G5 hoặc G6. Trạng thái chỉ chuyển sang đạt khi mọi sửa đổi có diff được duyệt, không còn lỗi xuất bản và DOCX mới đã qua vòng render–review.

## Kết quả sau biên tập nguồn và giọng ngày 2026-10-04

Các số liệu ở bảng đầu là kết quả trước biên tập. Bản hiện hành không còn cảnh báo VI011; còn ba cảnh báo VI012 dưới đây. Nội dung kỹ thuật không được chứng nhận đúng chỉ bằng kết quả lint.

| Tệp / dòng hiện hành | Rule | Quyết định | Lý do |
|---|---|---|---|
| CHAPTER_1.md:22, 79, 151, 233 | VI012 | FALSE_POSITIVE | Cả bốn là caption sơ đồ, cùng tiền tố do quy tắc đánh số hình, không phải đoạn mở lập luận lặp máy móc |
| CHAPTER_2.md:70, 110, 298, 317, 378 | VI012 | KEEP_WITH_REASON | Có cả dẫn chiếu và caption; dùng mã sơ đồ để người đọc tìm đúng hình trong mô tả phương pháp, không thêm câu chuyển ý chỉ để né lint |
| CHAPTER_2.md:206, 219, 232 | VI012 | KEEP_WITH_REASON | Các dòng Input của kỹ thuật 1–3 cần cùng cấu trúc để đối chiếu lệnh và tiền điều kiện; hợp đồng chương quy định mười trường mô tả kỹ thuật |

FIX đã thực hiện: tách các quan hệ độc lập trong câu; thu hẹp câu vượt nguồn, bỏ mô tả nội bộ chưa kiểm chứng; gộp phần tổng kết thành đoạn liên tục. Giữ các quan hệ cơ chế → hệ quả rõ theo lựa chọn tác giả. Việc bỏ tuyên bố tối ưu AES không có nguồn được ghi trong REVISION_PASS_2026_10_04.md; không biến một nhãn thiếu nguồn thành câu mơ hồ.

## Kết quả sau lượt tăng chiều sâu

Các dòng và kết quả phía trên là lịch sử. Bản hiện hành có ba cảnh báo VI012, không còn VI011. Câu 71 đơn vị trong phần FEA đã được FIX: tách chuỗi ba hệ quả, giữ mạch cơ chế và điều kiện. Không cắt các đoạn giải thích để giảm số cảnh báo.

| Tệp / dòng hiện hành | Rule | Quyết định | Lý do |
|---|---|---|---|
| CHAPTER_1.md:22, 77, 147, 232 | VI012 | FALSE_POSITIVE | Caption sơ đồ có tiền tố và số chương theo chức năng đánh số |
| CHAPTER_1.md:129, 213, 274 | VI012 | KEEP_WITH_REASON | Cả ba ví dụ cần nêu rõ giả định để phân biệt minh họa với dữ liệu lab; không đổi nhãn chỉ nhằm tránh lặp |
| CHAPTER_2.md:51, 91, 245, 264, 326 | VI012 | KEEP_WITH_REASON | Dẫn chiếu và caption giúp nối diễn giải với sơ đồ tương ứng |

Linter chạy sau review cơ chế và nguồn. Citation cấu trúc, độ rõ lập luận và tính đúng của nguồn được đánh giá riêng trong DEPTH_REVIEW_2026_10_04.md. Không dùng kết quả này làm điểm chất lượng học thuật hoặc chứng nhận Word cuối.
