# Cổng chất lượng

Đọc tài liệu này khi bắt đầu hoặc kết thúc một giai đoạn.

## G0 Intake

Phải có:

- Loại công trình và đối tượng đọc.
- Đề tài hoặc vùng vấn đề.
- Thời hạn và quy định cơ sở đào tạo.
- Phạm vi dữ liệu có thể sử dụng.
- Notebook hoặc kế nguồn dự kiến.
- Hồ sơ giọng tác giả đã có nguồn mẫu hoặc được ghi `PROVISIONAL`.

Đầu ra: `PROJECT_PROFILE.md`, `INSTITUTION_PROFILE.md`, `AUTHOR_VOICE.md`, `PROJECT_STATE.md`.

## G1 Research design

Phải có:

- Vấn đề không viết như một chủ đề chung.
- Câu hỏi có thể trả lời.
- Mục tiêu khớp câu hỏi.
- Phương pháp và bằng chứng khả thi.
- Phạm vi, giả định và tiêu chí đánh giá.

Đầu ra: `RESEARCH_MAP.md`.

## G2 Evidence

Phải có:

- Nguồn nền đủ cho khái niệm và bối cảnh.
- Nguồn chính cho các luận điểm trung tâm.
- Metadata và vị trí bằng chứng.
- Danh sách khoảng trống và truy vấn tiếp theo.
- Không có nguồn giả hoặc nguồn chưa đọc được đánh dấu verified.

Đầu ra: `SOURCE_LEDGER.md`.

## G3 Argument

Phải có:

- Kết luận trung tâm và chuỗi luận điểm.
- Claim Matrix cho toàn bộ luận điểm quan trọng.
- Phản biện và giới hạn.
- Đề cương có nhiệm vụ và ngân sách cho từng mục.
- Không có chương chỉ để “giới thiệu công cụ” nếu công cụ không phải đối tượng nghiên cứu.

Đầu ra: `ARGUMENT_MAP.md`, `CLAIM_MATRIX.md`, `OUTLINE.md`.

## G4 Chapters

Mỗi chương phải qua:

- Kiểm tra câu hỏi và kết luận chương.
- Kiểm tra nguồn và dữ liệu.
- Kiểm tra logic và độ sâu.
- Kiểm tra trùng lặp.
- Kiểm tra ngân sách từ.
- Hiệu chỉnh đúng ngữ vực của loại phần và hồ sơ giọng đã duyệt.
- Chạy linter tiếng Việt sau review logic; xử lý mỗi cảnh báo bằng `FIX`, `KEEP_WITH_REASON` hoặc `FALSE_POSITIVE`.
- Đọc liền toàn chương để phát hiện nhịp đều, chuyển đoạn lặp và kết luận khuôn mẫu.
- Phê duyệt của người dùng.

Đầu ra: hợp đồng chương, bản nháp và review report.

## G5 Synthesis

Phải xác nhận:

- Tất cả câu hỏi nghiên cứu đã được trả lời hoặc ghi rõ chưa thể trả lời.
- Mục tiêu, phương pháp, kết quả và kết luận nhất quán.
- Kết luận không đưa ra bằng chứng mới.
- Không còn citation mồ côi hoặc tài liệu tham khảo không được dùng.
- Thuật ngữ, số liệu và tên gọi thống nhất.
- Đại từ, mức chắc chắn, cách mở/kết mục và giọng tác giả nhất quán nhưng không san phẳng khác biệt chức năng giữa các chương.
- Linter toàn văn không còn lỗi; cảnh báo giữ lại đều có lý do trong review report.

Đầu ra: bản Markdown hoàn chỉnh và review report toàn cục.

## G6 Publication

Phải xác nhận:

- Định dạng theo institutional profile.
- Mục lục và số trang đúng.
- Bảng, hình, phương trình và phụ lục đúng quy tắc.
- DOCX đã render và mọi trang đã được xem.
- Không có secret, comment nội bộ, nhãn chưa xử lý hoặc placeholder trong bản nộp.
- Đã chạy linter với `--publication --fail-on-error` trên Markdown đã khóa trước khi tạo DOCX.
- Nội dung trong DOCX khớp bản Markdown đã qua review; không “humanize” riêng trên tệp Word.

Đầu ra: DOCX cuối, `PUBLICATION_CHECKLIST.md` và biên bản QA.

