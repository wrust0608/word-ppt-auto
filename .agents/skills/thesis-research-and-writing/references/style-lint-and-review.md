# Lint văn phong và review

Đọc tài liệu này sau khi bằng chứng và logic của bản nháp đã ổn định.

## Công cụ

Chạy:

```powershell
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py <file.md>
```

Dùng `--json` khi cần lưu kết quả máy đọc được. Có thể truyền nhiều tệp.

## Cách diễn giải

- `ERROR`: vi phạm có khả năng làm hỏng tính học thuật, ví dụ nguồn mơ hồ trong một khẳng định thực chất hoặc nhãn chưa xử lý ở bản chuẩn bị xuất bản.
- `WARNING`: dấu hiệu cần người biên tập xem xét trong ngữ cảnh.
- `INFO`: thống kê hoặc cấu trúc đáng chú ý, không bắt buộc sửa.

Không duyệt hoặc loại một chương chỉ bằng tổng số cảnh báo. Báo cáo phải nêu dòng, mẫu phát hiện, quyết định `FIX`, `KEEP_WITH_REASON` hoặc `FALSE_POSITIVE` và lý do.

## Thứ tự review chương

1. Đối chiếu claim matrix, nguồn, số liệu và trích dẫn.
2. Kiểm tra câu hỏi, kết luận, cầu nối lập luận và giới hạn.
3. Cắt nội dung không phục vụ mục tiêu.
4. Hiệu chỉnh theo loại phần và `AUTHOR_VOICE.md`.
5. Chạy linter; xử lý từng cảnh báo có ý nghĩa.
6. Đọc liền toàn chương để phát hiện nhịp, thuật ngữ và chuyển đoạn.
7. Cập nhật `REVIEW_REPORT.md`; không âm thầm sửa quyết định đã khóa.

## Giới hạn

Linter dùng heuristic tiếng Việt, không phải AI detector, bộ kiểm tra đạo văn hay trình xác minh sự thật. Nó không được:

- thay thế review nguồn và claim matrix;
- tự thêm citation, số liệu hoặc trải nghiệm;
- ép mọi câu về cùng độ dài;
- cấm câu bị động hoặc ngôi thứ nhất ngoài ngữ cảnh;
- sửa trực tiếp DOCX mà không phản ánh lại vào Markdown.
