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
