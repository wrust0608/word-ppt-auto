# Báo cáo kiểm định bản Word

**Tài liệu:** `BAO_CAO_DO_AN_CHUONG_1_2.docx`  
**Ngày kiểm định:** 2026-10-04  
**Trạng thái:** `FAIL_REBUILD_FROM_APPROVED_MARKDOWN`

## 1. Kết luận ngắn

Bản Word mở và đọc được, có phân cấp heading và khổ trang phù hợp với quy định đã thu thập. Tuy nhiên, đây chưa phải bản đủ điều kiện nộp. Hai lỗi trọng yếu là font thân bài bị lệch mạnh sang Consolas và tài liệu không có trường mục lục tự động. Bản Word cũng được tạo trước khi hoàn tất đối soát nguồn của chương mẫu, vì vậy không được dùng làm nguồn chuẩn để sửa nội dung.

## 2. Kết quả kiểm định cấu trúc

| Hạng mục | Kết quả | Bằng chứng kiểm tra |
|---|---|---|
| Khổ giấy | Đạt | Hai section đều A4, hướng dọc. |
| Lề trang | Đạt | Trái khoảng 3,5 cm; phải 2 cm; trên 3,5 cm; dưới 3 cm. |
| Phân cấp heading | Có cấu trúc | 6 Heading 1, 13 Heading 2, 37 Heading 3, 3 Heading 4. |
| Font | Không đạt | Kiểm tra run cho thấy Consolas chiếm phần lớn ký tự; Times New Roman chỉ chiếm phần nhỏ. |
| Mục lục tự động | Không đạt | Chỉ phát hiện trường `PAGE`; không có trường `TOC`. Mục “Mục lục tổng quát” hiện có nhiều khả năng là nội dung tĩnh. |
| Khả năng bảo trì style | Không đạt | Có 2.007 run và 855 đoạn dùng định dạng trực tiếp, làm tăng nguy cơ lệch kiểu khi sửa hoặc xuất lại. |
| Hình/đồ họa | Cần rà lại | Không phát hiện đối tượng ảnh inline/anchored; các sơ đồ có thể đang là ký tự hoặc đối tượng không được quản lý như hình chuẩn. |
| Khả năng tiếp cận | Cần sửa | Không có lỗi mức cao; có 22 cảnh báo mức trung bình. |
| Render trực quan | Chưa xác nhận | Trình render chuẩn chưa chạy được vì chưa tìm thấy LibreOffice trong môi trường thực thi. Không được xem kiểm tra cấu trúc là thay thế cho kiểm tra từng trang. |

## 3. Nguyên tắc sửa

Không sửa tay tiếp trên bản Word hiện tại. Markdown đã duyệt phải là nguồn chuẩn. Sau khi chương mẫu qua cổng nguồn và giọng tác giả, hệ thống cần sinh lại DOCX, áp style tập trung rồi mới cập nhật mục lục và kiểm tra trang.

## 4. Vòng xuất bản bắt buộc

1. Chốt Markdown đã được duyệt và danh mục nguồn hợp lệ.
2. Sinh DOCX mới từ Markdown.
3. Áp style thân bài Times New Roman theo đúng cỡ chữ/giãn dòng của quy định trường; loại bỏ font Consolas khỏi nội dung thông thường.
4. Tạo heading bằng style Word, không giả heading bằng chữ in đậm hoặc định dạng trực tiếp.
5. Chèn trường mục lục tự động, số trang và danh mục hình/bảng khi có.
6. Chuẩn hóa chú thích hình, bảng, công thức và tham chiếu chéo.
7. Render toàn bộ tài liệu; xem từng trang ở tỷ lệ 100%; sửa lỗi tràn, ngắt trang, hàng cô độc, bảng/hình và font tiếng Việt.
8. Chạy lại kiểm tra cấu trúc, style, mục lục, trích dẫn và khả năng tiếp cận.

## 5. Điều kiện đạt

Bản Word chỉ được gắn nhãn `PUBLICATION_READY` khi không còn lỗi font, có TOC tự động, mọi trang đã được render và xem, không có lỗi bố cục nghiêm trọng, và nội dung xuất ra trùng với Markdown đã duyệt.
