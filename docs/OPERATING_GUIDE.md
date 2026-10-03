# Hướng dẫn vận hành

## Tạo dự án mới

Tạo thư mục `work/<project-slug>/` và sao chép các template vào đó. Điền ít nhất:

- Tên đề tài tạm thời.
- Vấn đề cần giải quyết.
- Đối tượng và phạm vi.
- Loại bằng chứng hoặc dữ liệu có thể thu thập.
- Quy định trường áp dụng.
- Notebook URL hoặc ID.
- Thời hạn.

Nếu chưa rõ câu hỏi nghiên cứu, để trống và yêu cầu Antigravity xử lý tại cổng G1; không tự đặt một câu hỏi chỉ để lấp chỗ trống.

## Sử dụng prompt

Sao chép toàn bộ `prompts/ANTIGRAVITY_MASTER_PROMPT.md`, thay các trường trong khối `THÔNG TIN DỰ ÁN`, rồi gửi cho Antigravity.

Agent phải bắt đầu bằng việc đọc skill và các hồ sơ dự án, báo cổng hiện tại, kiểm tra kết nối NotebookLM và chỉ thực hiện công việc của cổng đó.

## Duyệt một cổng

Khi đồng ý, trả lời theo mẫu:

```text
PHÊ DUYỆT G<n>.
Các điều chỉnh bắt buộc: <không có hoặc danh sách>.
Cho phép chuyển sang G<n+1>.
```

Nếu chưa đồng ý:

```text
CHƯA PHÊ DUYỆT G<n>.
Hãy sửa các điểm sau: <danh sách cụ thể>.
```

## Kiểm soát chất lượng chương

Chỉ duyệt một chương khi:

- Câu hỏi chương đã được trả lời.
- Mọi luận điểm quan trọng có nguồn hoặc dữ liệu.
- Có phân tích, không chỉ tóm tắt tài liệu.
- Phân biệt kết quả với diễn giải.
- Nêu giới hạn hoặc điều kiện áp dụng.
- Không có trích dẫn giả hoặc tài liệu tham khảo mồ côi.
- Không còn đoạn không phục vụ mục tiêu chương.
- Ngữ vực đúng chức năng của phần viết và phù hợp `AUTHOR_VOICE.md`.
- Linter đã chạy sau review logic; mọi cảnh báo quan trọng có quyết định và lý do.

Chạy linter:

```powershell
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/<project-slug>/CHAPTER_DRAFT.md
```

Trước xuất bản:

```powershell
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/<project-slug>/THESIS.md --publication --fail-on-error
```

Không chỉnh phong cách trực tiếp trên DOCX. Mọi thay đổi nội dung phải quay lại Markdown chuẩn.

## Tiếp tục sau gián đoạn

Gửi cho Antigravity:

```text
Hãy đọc PROJECT_STATE.md và các artifact được liên kết. Tóm tắt cổng hiện tại, quyết định đã khóa, vấn đề còn mở và bước an toàn tiếp theo. Không viết nội dung mới cho tới khi xác nhận trạng thái nhất quán.
```

## Xử lý lỗi

- MCP không kết nối: không viết khẳng định cần nguồn; ghi lỗi và bước khôi phục vào state.
- Thiếu nguồn: thêm `[CẦN NGUỒN]` và đưa vào research backlog.
- Hai nguồn mâu thuẫn: thêm `[MÂU THUẪN NGUỒN]`, trình bày điều kiện của từng nguồn.
- Thiếu dữ liệu thực nghiệm: thêm `[CẦN DỮ LIỆU]`; không tạo số liệu mẫu trong bản nháp chính.
- Quy định trường mâu thuẫn: ghi cả hai quy định, chọn tài liệu có thẩm quyền hoặc ngày mới hơn và yêu cầu xác nhận trước G6.
- Linter báo false positive: giữ câu, ghi `FALSE_POSITIVE` và lý do; không viết lại chỉ để đạt số cảnh báo thấp.

