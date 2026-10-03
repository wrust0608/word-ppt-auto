# NotebookLM và quản lý bằng chứng

Đọc tài liệu này khi xây dựng kho nguồn, truy vấn NotebookLM hoặc kiểm tra một luận điểm.

## Khởi động

1. Khám phá các tool mà server NotebookLM hiện cung cấp.
2. Kiểm tra kết nối và notebook đang được chọn.
3. Liệt kê nguồn trước khi hỏi nội dung.
4. Đối chiếu nguồn với `SOURCE_LEDGER.md`.
5. Không gửi dữ liệu bí mật hoặc tài liệu bị hạn chế nếu hồ sơ dự án chưa cho phép.

Không giả định tên tool cố định. Tìm tool theo năng lực: notebook selection, source listing, source ingestion và source-grounded chat.

## Tiêu chuẩn nguồn

Ưu tiên theo thứ tự phù hợp với ngành:

- Văn bản chính thức, tiêu chuẩn, dữ liệu gốc và tài liệu nhà sản xuất.
- Bài báo phản biện, sách học thuật và kỷ yếu có uy tín.
- Luận án, luận văn và báo cáo kỹ thuật từ kho lưu trữ cơ sở đào tạo.
- Nguồn tổng quan có tác giả và quy trình biên tập rõ.
- Nguồn cộng đồng chỉ dùng để tìm manh mối hoặc minh họa, không làm nền duy nhất cho luận điểm quan trọng.

Đánh giá từng nguồn về thẩm quyền, tính gần với bằng chứng gốc, thời điểm, phạm vi, phương pháp và xung đột lợi ích.

## Chu kỳ truy vấn

### 1. Khảo sát

Yêu cầu NotebookLM xác định khái niệm, trường phái, kết quả chính, khác biệt giữa nguồn và khoảng trống. Không dùng kết quả khảo sát làm đoạn văn cuối.

### 2. Truy vấn luận điểm

Đặt một câu hỏi hẹp cho một luận điểm. Yêu cầu:

- Nguồn nào hỗ trợ.
- Đoạn hoặc trang liên quan nếu có.
- Điều kiện của kết luận.
- Nguồn nào không đồng ý hoặc giới hạn kết luận.
- Phần nào NotebookLM không đủ dữ liệu để trả lời.

### 3. Xác minh

Mở tài liệu gốc hoặc đoạn nguồn. Kiểm tra metadata, nội dung và ngữ cảnh. Ghi vào ledger trước khi viết.

### 4. Tam giác hóa

Với luận điểm trung tâm, ưu tiên hai nguồn độc lập hoặc một nguồn sơ cấp đủ mạnh cộng một nguồn giải thích. Không tạo số lượng nguồn giả tạo khi chỉ có một tài liệu gốc có thẩm quyền.

## Truy vấn phản biện mẫu

```text
Trong các nguồn của notebook, hãy tìm bằng chứng làm suy yếu, giới hạn hoặc đặt điều kiện cho luận điểm sau: <LUẬN ĐIỂM>. Trả về tên nguồn, vị trí, nội dung hỗ trợ/phản bác và phần chưa thể kết luận. Không bổ sung kiến thức ngoài nguồn.
```

## Điều kiện ghi vào Claim Matrix

Một nguồn chỉ được gắn trạng thái `VERIFIED` khi:

- Metadata đủ để lập tài liệu tham khảo.
- Đã đọc đúng đoạn hỗ trợ.
- Phạm vi nguồn phù hợp với phát biểu.
- Không bỏ qua điều kiện quan trọng.
- Có thể nêu chính xác nguồn hỗ trợ toàn bộ hay chỉ một phần luận điểm.

Nếu chỉ biết nguồn thông qua một tài liệu khác, ghi là trích dẫn thứ cấp và không đưa tài liệu gốc chưa đọc vào danh mục tham khảo.

