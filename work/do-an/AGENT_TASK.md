# AGENT TASK — Vòng sửa lý thuyết sau phản biện hội đồng

Trạng thái: ACTIVE — THEORY_REVISION_ROUND_1

## Căn cứ
Đọc `work/do-an/BOARD_REVIEW.md`. Điểm hiện tại của bản lý thuyết: **64/100 — REJECT_ROUND**.

## Mục tiêu
Nâng phần Mở đầu + Chương 1 lên tối thiểu **80/100** theo rubric repo. Không tăng số từ nếu không cần.

## Thứ tự bắt buộc

1. **Citation trước**: mọi claim kỹ thuật quan trọng phải ánh xạ nguồn gốc trong SOURCE_LEDGER và có citation IEEE phù hợp.
2. Rà toàn bộ bảng SMBv1/v2/v3:
   - không trộn tính năng của nhiều dialect/thế hệ Windows mà không ghi điều kiện;
   - tách SMB over QUIC, AES-GMAC, AES-256, RDMA/Multichannel theo phạm vi thực;
   - không áp đặc tính hệ thống hiện đại cho Windows 7 lab.
3. Sửa các câu quá mạnh/không chính xác được liệt kê tại P0-03 của BOARD_REVIEW.
4. Chuẩn hóa Hình/Bảng:
   - số thứ tự;
   - caption;
   - nguồn hoặc “nhóm tự tổng hợp từ [..]”.
5. Viết lại Mở đầu:
   - vấn đề cụ thể;
   - mục tiêu đo được;
   - phương pháp có khả năng tái lập;
   - đóng góp dự kiến;
   - giới hạn.
6. Làm rõ khung bốn mức xác minh:
   - nguồn gốc/đề xuất của nhóm;
   - lý do chia 4 mức;
   - bằng chứng, điều kiện chuyển mức;
   - ranh giới suy luận và Unknown.
7. Cắt nội dung lặp ở 1.1; mỗi kiến thức giữ lại phải phục vụ Chương 2/3 hoặc hardening.
8. Viết lại mục công cụ theo logic: phép đo → output → bằng chứng → inference boundary → limitation → lý do chọn.
9. Không tạo kết quả thực nghiệm.
10. Không dựng DOCX cuối.

## Bài nộp
Cập nhật `AGENT_SUBMISSION.md` với:
- file đã sửa;
- danh sách claim quan trọng đã thay;
- bảng `Claim → Source ID → vị trí nguồn → citation mới`;
- các claim đã hạ mức vì thiếu bằng chứng;
- các điểm còn tranh luận;
- kết quả citation audit/style lint.

Sau đó dừng chờ hội đồng chấm lại.
