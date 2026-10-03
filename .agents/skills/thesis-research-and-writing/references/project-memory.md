# Bộ nhớ và bàn giao dự án

`PROJECT_STATE.md` là nguồn trạng thái duy nhất giữa các phiên. Không dựa vào lịch sử chat để quyết định cổng hoặc nội dung đã được duyệt.

## Cập nhật sau mỗi lượt

Ghi:

- Cổng hiện tại.
- Artifact đã tạo hoặc sửa.
- Quyết định đã được phê duyệt.
- Nguồn mới và trạng thái xác minh.
- Giả định đang dùng.
- Nhãn thiếu thông tin còn mở.
- Rủi ro hoặc mâu thuẫn.
- Một bước tiếp theo cụ thể.

Không ghi toàn bộ hội thoại hoặc log tool vào state. Chỉ ghi thông tin giúp một agent mới tiếp tục đúng.

## Bàn giao

Một agent nhận bàn giao phải:

1. Đọc state.
2. Đọc artifact được state liên kết.
3. Đối chiếu trạng thái cổng với các file thực tế.
4. Báo điểm không nhất quán.
5. Chỉ tiếp tục sau khi đã hiểu quyết định khóa.

## Thay đổi quyết định cũ

Không sửa im lặng. Ghi quyết định cũ, quyết định mới, lý do, artifact bị ảnh hưởng và phạm vi cần viết lại.

