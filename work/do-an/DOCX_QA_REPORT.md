# Báo cáo kiểm định bản Word

- Tài liệu: `BAO_CAO_DO_AN_CHUONG_1_2.docx`.
- Ngày: 2026-10-04.
- Trạng thái: `FAIL_REBUILD_FROM_APPROVED_MARKDOWN`.
- Phạm vi: audit bản hiện có; không sửa DOCX hoặc chương chưa được tái duyệt.

## Kết quả kiểm tra

Đã hoàn tất render native bằng OfficeCLI và xem riêng đủ 53 trang trong lượt tiếp quản trước. Mỗi ảnh trang có kích thước 794 × 1122; trang 17–53 được tách từ bản render liên tục 794 × 41.514. 53 ảnh trang và contact sheet giữ cục bộ tại `.tmp/docx-qa/do-an/officecli-render/`, được gitignore. Không dùng contact sheet thay cho việc xem từng trang. Lượt này lưu kết quả đã kiểm tra, không tuyên bố bản mới đã nghiệm thu.

OpenXML validation trước đạt; OfficeCLI ghi 475 đoạn ngoài bảng, 15.446 từ. XML có 883 đoạn kể cả trong bảng. Audit cũ ghi 2.007 run và 855 đoạn có định dạng trực tiếp, 323 issues OfficeCLI, 22 cảnh báo accessibility mức trung bình.

**Đính chính font:** thống kê cũ bỏ sót font kế thừa từ style nên kết luận Consolas chiếm phần lớn là sai. Kiểm tra có tính kế thừa trên document.xml cho thấy Times New Roman 82.879 ký tự, Consolas 13.892, Cambria Math 1.618. TNR chiếm phần lớn; Consolas dùng nhiều trong code/sơ đồ. Vẫn cần kiểm tra cỡ chữ/font theo chức năng khi dựng lại.

| Hạng mục | Kết quả |
|---|---|
| A4 và lề | Audit cấu trúc trước đạt: trái 3,5; phải 2; trên 3,5; dưới 3 cm |
| Heading | Có 6 Heading 1, 13 Heading 2, 37 Heading 3, 3 Heading 4 |
| TOC | Không có trường TOC; mục lục tĩnh sai số trang |
| Số trang | Thân bài bắt đầu ở trang 6 và in số 6, chưa khởi động lại từ 1 theo institutional profile |
| Giãn dòng | Có 382 spacing line=276 (1,15), 75 line=288 (1,2). Institutional profile ghi 1,5; DEC-19 mô tả 1,3. Đối chiếu mẫu gốc trước dựng lại, giữ lịch sử quyết định |
| Trang trắng/glyph | Không phát hiện trang trắng hoàn toàn hoặc mất glyph tiếng Việt rõ ràng trong lượt xem |
| Nghiệm thu | FAIL: còn lỗi công thức, ngắt trang, mục lục và nhãn dữ liệu |

## Lỗi trực quan theo trang

Số dưới đây là trang vật lý, trùng số in phần thân của bản hiện có. Đã xem toàn bộ trang 1–53; các nhóm dưới đây ghi những lỗi quan sát được, không chỉ trang mẫu.

| Trang | Lỗi cần xử lý khi dựng lại |
|---|---|
| 1; 6–53 | Màu xanh, trang trí bìa, header chữ nghiêng: đối chiếu mẫu HUIT và bỏ phần không được mẫu cho phép |
| 2–5 | Mục lục/danh mục tĩnh, nhãn trang xuống dòng. Mục lục ghi Chương 2 trang 20, heading thật ở trang 29 |
| 7–8 | Sơ đồ 1.1 chia qua trang, caption tách khỏi phần lớn hình |
| 9–10 | Bảng so sánh qua trang nhưng thiếu header lặp |
| 14 | Các ô bản dựng/KB hiện nguyên `<br>` |
| 21–22 | Bảng 1.4 bị ngắt giữa hàng header |
| 22–23 | Hàng Bảng 1.5 bị chia trang, thiếu header lặp |
| 24–25; 39–40 | Tiêu đề mục danh sách ở cuối trang, nội dung ở trang kế |
| 26–28 | Danh mục nối ngay sau tổng kết; một mục tách giữa trang 27–28; cần đối chiếu ngắt trang và hanging indent |
| 30–47; 50; 52 | Công thức hiện nguyên lệnh LaTeX, dollar/underscore: cần chuyển OMML hoặc biểu thức đúng, bảo toàn nghĩa |
| 33–34 | Sơ đồ topology chia qua hai trang |
| 34–35 | Bảng IP cột quá hẹp, từ/subnet bị bẻ; hàng Target-Win7 chia trang |
| 38–39 | Bảng trạng thái quá hẹp, ký hiệu chưa chuyển đúng, chú giải kéo sang trang sau |
| 45–46 | Khối cấu hình chia qua hai trang |
| 48 | Bảng kỹ thuật có tiêu đề cột bị bẻ nhỏ, lệnh/mã trạng thái chia khó đọc |
| 48–49 | Sơ đồ 2.2 tách dòng cuối/caption sang trang sau |
| 49 | Ma trận 10 cột quá chật và còn `[CẦN DỮ LIỆU]`; giữ nhãn tới khi có bằng chứng hoặc ngoại lệ tác giả duyệt |
| 50–51 | Sơ đồ rollback chia trang |
| 52–53 | Bibliography đánh số lại theo chương; phải kiểm tra IEEE xuyên tài liệu khi ghép, không suy từ audit từng chương |

## Điều kiện dựng lại

Markdown được tác giả duyệt là nguồn chuẩn. Chờ calibration, đối soát nguồn và review chương trước khi sinh DOCX mới. Áp style tập trung, TOC tự động, công thức đúng, bảng/sơ đồ không chia bất hợp lý. Sau dựng lại phải render và xem mọi trang của phiên bản mới. Không gắn `PUBLICATION_READY` cho bản hiện có.
