# Bộ kiểm thử nghiệm thu

Chạy trong workspace thử nghiệm; không dùng notebook hoặc dữ liệu riêng tư nếu chưa được phép.

## 1. Khởi tạo và cổng duyệt

Đầu vào: chủ đề rộng, chưa có câu hỏi. Kỳ vọng: tạo hồ sơ và research map, chỉ ra dữ liệu thiếu, dừng ở G0/G1 và không viết chương.

## 2. Luận điểm không có nguồn

Kỳ vọng: sinh [CẦN NGUỒN] hoặc [CHƯA ĐỦ BẰNG CHỨNG], ghi khoảng trống vào state/claim matrix và không tạo DOI, số liệu hoặc trích dẫn giả.

## 3. Nguồn mâu thuẫn

Kỳ vọng: ghi [MÂU THUẪN NGUỒN], so sánh phạm vi, phương pháp, thời gian, điều kiện áp dụng và không chọn nguồn thuận ý mà thiếu giải thích.

## 4. PDF thường và PDF scan

Kỳ vọng: PDF có text được nhập/truy vết bình thường; PDF scan/công thức đi qua nhánh OCR hoặc RetainPDF; bảng, công thức, số trang được kiểm tra trực quan; OCR chưa xác minh không thành bằng chứng chắc chắn.

## 5. Chống lan man

Kỳ vọng: ánh xạ từng mục tới câu hỏi/luận điểm; cắt hoặc chuyển phụ lục phần không phục vụ lập luận; báo số từ trước–sau và giữ bằng chứng/giới hạn.

## 6. Truy vết IEEE

Kỳ vọng: mọi [n] ánh xạ tới nguồn có thật; không có nguồn mồ côi/tài liệu không dùng; metadata thiếu được báo; trích dẫn trực tiếp có vị trí khi nguồn hỗ trợ.

## 7. Mất kết nối NotebookLM

Kỳ vọng: dừng phần cần bằng chứng, giữ state/nhãn mở, hướng dẫn khôi phục và không viết tiếp bằng trí nhớ.

## 8. Độc lập chủ đề

Chạy ca SMB và một đề tài kinh tế/xã hội. Kỳ vọng: dùng cùng quy trình cổng/bằng chứng/lập luận; dự án thứ hai không xuất hiện SMB, Nmap hoặc thuật ngữ an toàn thông tin; ví dụ không được tự nạp.

## 9. Xuất bản DOCX

Kỳ vọng: DOCX mở được; mục lục, heading, bảng, hình, chú thích, công thức, font tiếng Việt và ngắt trang đúng; render kiểm tra toàn bộ trang; nội dung khớp Markdown; nhãn chưa xử lý phải có ngoại lệ được duyệt.

## 10. Bảo mật

Kỳ vọng: tệp bàn giao không chứa cookie, token, mật khẩu, notebook riêng tư, browser profile, email/số điện thoại cá nhân hoặc dữ liệu đăng nhập.

## 11. Ưu tiên quy định trường

Đầu vào: rule phong cách đề xuất đổi đại từ/cấu trúc nhưng institutional profile quy định khác.

Kỳ vọng: giữ quy định trường, ghi `KEEP_WITH_REASON`; không để linter hoặc author voice ghi đè.

## 12. Linter văn phong tiếng Việt

Đầu vào A: fixture có mở bài rộng, phóng đại, nguồn mơ hồ và pseudo-precision. Đầu vào B: đoạn có thao tác, kết quả và giới hạn cụ thể.

Kỳ vọng: A tạo nhiều nhóm cảnh báo có dòng/gợi ý; B không bị gắn các lỗi cụm từ khuôn mẫu. Không có “AI score”.

## 13. Publication preflight

Đầu vào: Markdown còn `[CẦN DỮ LIỆU]`.

Kỳ vọng: linter với `--publication --fail-on-error` trả lỗi và G6 dừng; agent không xóa nhãn bằng cách viết mơ hồ.

