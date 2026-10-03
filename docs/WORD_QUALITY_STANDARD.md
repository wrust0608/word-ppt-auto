# Tiêu chuẩn chất lượng bản Word

Tài liệu này quy định lớp kiểm soát cuối đối với DOCX. Các yêu cầu của trường trong `INSTITUTION_PROFILE.md` và mẫu Word chính thức luôn có ưu tiên cao hơn tài liệu này.

## 1. Điều kiện trước khi dựng Word

Chỉ sinh DOCX khi:

- nội dung Markdown đã qua cổng duyệt tương ứng;
- luận điểm, số liệu và trích dẫn đã được kiểm tra;
- các nhãn `[CẦN NGUỒN]`, `[CẦN DỮ LIỆU]` và `[CẦN TÁC GIẢ XÁC NHẬN]` đã được xử lý hoặc được liệt kê rõ trong biên bản bàn giao;
- vòng biên tập lập luận, văn phong và kiểm tra bằng linter đã hoàn tất;
- quy định trình bày của cơ sở đào tạo đã được chuẩn hóa trong `INSTITUTION_PROFILE.md`.

DOCX là sản phẩm xuất bản từ nguồn Markdown đã duyệt, không phải nơi sửa nội dung học thuật lần đầu.

## 2. Thứ tự ưu tiên khi trình bày

1. Mẫu và quy định chính thức của trường.
2. Các quyết định đã khóa trong hồ sơ dự án.
3. Khả năng đọc và tính nhất quán của tài liệu.
4. Quy ước mặc định của hệ thống.

Không thêm màu sắc, khung trang trí, biểu tượng, ảnh nền hoặc hiệu ứng chỉ để tài liệu “trông chuyên nghiệp”. Luận văn cần có hình thức tiết chế, ổn định và phù hợp với văn bản học thuật.

## 3. Các điểm bắt buộc kiểm tra

### Cấu trúc

- tiêu đề chương và mục dùng đúng cấp heading;
- đánh số chương, mục, bảng, hình và công thức nhất quán;
- mục lục lấy từ heading, không gõ tay;
- danh mục bảng, hình và chữ viết tắt khớp với nội dung thực tế;
- phụ lục và tài liệu tham khảo bắt đầu ở vị trí đúng theo quy định.

### Kiểu chữ và đoạn văn

- font, cỡ chữ, giãn dòng, khoảng cách trước–sau và thụt đầu dòng đúng mẫu trường;
- tiếng Việt hiển thị đúng Unicode, không thay font cục bộ ngoài ý muốn;
- không có đoạn cô lập chỉ một dòng ở đầu hoặc cuối trang;
- không dùng dấu cách hoặc dòng trống thủ công để điều khiển bố cục;
- không lạm dụng chữ đậm, chữ nghiêng hay viết hoa.

### Bảng, hình và công thức

- bảng không vượt lề, không chia hàng gây khó đọc và lặp hàng tiêu đề khi sang trang nếu cần;
- hình đủ rõ, đúng tỷ lệ, có nguồn và chú thích;
- tên bảng/hình đặt đúng vị trí theo quy định;
- mọi bảng và hình đều được nhắc tới, giải thích trong nội dung;
- công thức không bị vỡ dòng, ký hiệu được giải thích và đánh số nhất quán.

### Trích dẫn và tài liệu tham khảo

- số IEEE tăng theo lần xuất hiện đầu tiên;
- mọi trích dẫn trong thân bài ánh xạ tới một tài liệu có thật;
- không có tài liệu tham khảo mồ côi;
- metadata không thiếu tác giả, tiêu đề, năm hoặc thông tin xuất bản thiết yếu;
- trích dẫn trực tiếp có vị trí trang hoặc đoạn khi nguồn hỗ trợ.

## 4. Vòng lặp kiểm tra trực quan

Mỗi lần xuất bản phải thực hiện vòng lặp:

1. sinh DOCX từ Markdown đã duyệt;
2. dựng toàn bộ tài liệu thành ảnh hoặc PDF bằng OfficeCLI;
3. xem từng trang, không chỉ trang đầu;
4. ghi lỗi theo trang và theo loại;
5. sửa nguồn Markdown, cấu hình hoặc bộ dựng;
6. sinh lại và kiểm tra lại từ đầu.

Các lỗi cần tìm gồm trang trắng bất thường, heading nằm cuối trang, bảng/hình bị cắt, chú thích tách khỏi đối tượng, mục lục sai số trang, font thay đổi, khoảng trắng lớn và ngắt trang thiếu chủ đích.

## 5. Điều kiện bàn giao

Bản DOCX chỉ được đánh dấu sẵn sàng khi:

- mở được trên Microsoft Word mà không có cảnh báo sửa chữa;
- đã kiểm tra trực quan toàn bộ trang;
- mục lục và các trường tự động đã được cập nhật;
- không còn lỗi mức `ERROR` từ kiểm tra xuất bản;
- mọi sai khác so với mẫu trường đều có quyết định được ghi lại;
- Markdown nguồn, DOCX, bản render và báo cáo kiểm tra cùng thuộc một phiên bản bàn giao.

Không dùng công cụ nhận diện AI hoặc điểm “giống người” làm tiêu chí nghiệm thu. Chất lượng được đánh giá bằng độ đúng, chiều sâu lập luận, khả năng truy vết nguồn, giọng viết đã hiệu chỉnh và mức tuân thủ quy định trình bày.
