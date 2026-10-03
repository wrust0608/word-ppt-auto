# Xuất bản DOCX

Đọc tài liệu này chỉ tại G6 hoặc khi người dùng yêu cầu kiểm tra định dạng Word.

Tiêu chuẩn nghiệm thu chi tiết nằm tại `docs/WORD_QUALITY_STANDARD.md`. Nếu tài liệu đó xung đột với mẫu hoặc quy định chính thức của trường, luôn áp dụng quy định của trường.

## Nguồn chuẩn

- Markdown đã duyệt là nguồn nội dung.
- Institutional profile là nguồn định dạng.
- DOCX mẫu chính thức là nguồn kiểu dáng khi người dùng cung cấp.
- Không tự áp dụng thiết kế trang trí cho tài liệu học thuật.

## Quy trình

1. Khóa bản Markdown và danh mục tham khảo.
2. Xác nhận review report G5, giọng tác giả và linter publication đã đạt; không sửa phong cách lần đầu trong DOCX.
3. Tạo DOCX bằng OfficeCLI hoặc công cụ Word phù hợp.
4. Áp dụng khổ giấy, lề, font, giãn dòng, cấp heading và số trang.
5. Tạo mục lục, danh mục bảng và danh mục hình.
6. Kiểm tra caption, đánh số theo chương và cross-reference.
7. Render DOCX thành từng trang.
8. Xem mọi trang ở mức đủ đọc.
9. Sửa lỗi và render lại cho tới khi không còn lỗi.

## Danh sách kiểm tra

- Không thiếu glyph tiếng Việt.
- Không có bảng vượt lề, hàng bị cắt hoặc cột quá hẹp.
- Hình đủ nét, caption ở đúng vị trí và được nhắc tới trong nội dung.
- Heading không đứng một mình cuối trang.
- Không có trang trắng ngoài chủ ý.
- Số trang và section break đúng.
- Tài liệu tham khảo có hanging indent nếu quy định yêu cầu.
- Không còn placeholder hoặc nhãn thiếu thông tin.
- Không có đoạn bị cắt, lặp hoặc đổi nghĩa so với Markdown chuẩn.
- Không có kiểu nhấn mạnh, màu sắc, hộp văn bản hoặc bố cục trang trí do agent tự thêm nếu mẫu trường không yêu cầu.

Nếu OfficeCLI hoặc renderer không hoạt động, không tuyên bố DOCX đã được kiểm tra trực quan.

