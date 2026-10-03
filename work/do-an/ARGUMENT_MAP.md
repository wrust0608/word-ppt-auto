# Bản đồ lập luận

## Kết luận trung tâm dự kiến

Việc duy trì giao thức SMBv1 trong hệ sinh thái Windows tạo ra bề mặt tấn công mức nhân (kernel-mode) đặc biệt nguy hiểm thông qua các lỗ hổng quản lý bộ nhớ MS17-010 (tiêu biểu: CVE-2017-0144 / EternalBlue). Để bảo đảm an toàn hệ thống, công tác đánh giá an ninh phải phân định nghiêm ngặt giữa việc "nhận diện dịch vụ mở" và "xác minh lỗ hổng thực tế"; đồng thời công tác phòng thủ phải triển khai chiến lược bảo vệ đa tầng (vá lỗi, vô hiệu hóa hoàn toàn SMBv1, giới hạn cổng 445 và phân đoạn mạng) đi kèm đánh giá rủi ro tương thích thiết bị cũ.

## Chuỗi lập luận

| Claim ID | Luận điểm | Loại | Phụ thuộc vào | Phản biện chính | Giới hạn |
|---|---|---|---|---|---|
| C001 | SMB là giao thức truyền thông mạng lõi chạy ở Kernel-mode (`srv.sys`); SMBv2 và SMBv3 được thiết kế lại để khắc phục cơ bản điểm yếu kiến trúc và bảo mật của SMBv1 | Nền tảng | S002, S007, S008, S009 | Nhiều hệ thống vẫn buộc phải bật SMBv1 để tương thích máy in/NAS cũ | Phân tích tập trung vào môi trường Windows |
| C002 | Nhóm lỗ hổng MS17-010 xuất phát từ lỗi xử lý gói tin SMBv1 trong driver nhân `srv.sys`, cho phép thực thi mã từ xa (RCE) với quyền SYSTEM mà không cần chứng thực | Nguyên nhân | S001, S006, S008 | Bản vá đã phát hành từ 2017 | Bề mặt tấn công vẫn tồn tại nếu hệ thống không được cập nhật |
| C003 | Đánh giá an ninh SMB phải phân biệt rõ ràng 4 mức: phát hiện cổng 445 mở, nhận diện phiên bản SMBv1, nghi ngờ dấu hiệu lỗ hổng và xác minh lỗ hổng thực tế | Phương pháp | S003, S004, S011 | Quét cổng thông thường dễ đưa ra kết luận dương tính giả | Phụ thuộc vào độ chính xác của NSE script và banner grab |
| C004 | Khai thác thử nghiệm lỗ hổng SMB mức nhân có rủi ro cao gây sụp đổ hệ thống (BSOD / Kernel Crash), bắt buộc phải vận hành trong mô hình lab cô lập có snapshot phục hồi | An toàn | S010, S012 | Thử nghiệm trong lab không mô phỏng hoàn toàn độ trễ mạng thực tế | Áp dụng trong phạm vi lab được cấp phép |
| C005 | Vô hiệu hóa SMBv1 và áp dụng bản vá tích lũy là biện pháp phòng thủ triệt để nhất; tường lửa chặn TCP 445 và phân đoạn mạng giúp chống lây lan ngang (lateral movement) | Phòng thủ | S001, S002, S011 | Tắt cổng 445 có thể làm tê liệt dịch vụ chia sẻ tệp nội bộ | Cần cấu hình tường lửa phân vùng có chọn lọc |
| C006 | Quá trình hardening SMB đòi hỏi đánh giá rủi ro tương thích và rủi ro còn lại, không thể áp dụng cứng nhắc một chính sách cho toàn bộ hạ tầng | Thực tiễn | S002, S011 | Doanh nghiệp ưu tiên tính sẵn sàng của ứng dụng hơn bảo mật | Cần lộ trình thay thế thiết bị cũ |

## Quan hệ giữa các luận điểm

```
C001 (Kiến trúc SMB & srv.sys) ──> C002 (Cơ chế lỗi MS17-010 tại Kernel)
                                          │
    ┌─────────────────────────────────────┴─────────────────────────────────────┐
    ▼                                                                           ▼
C003 (Phân định tiêu chí kiểm thử)                                      C005 (Chiến lược phòng thủ đa tầng)
    │                                                                           │
    ▼                                                                           ▼
C004 (Kiểm soát an toàn lab cô lập)                                     C006 (Đánh giá tương thích & rủi ro)
```

## Cách giải thích cạnh tranh

| ID | Cách giải thích khác | Bằng chứng ủng hộ | Cách xử lý trong luận văn |
|---|---|---|---|
| ALT-01 | Chỉ cần cấu hình tường lửa biên chặn cổng TCP 445 từ Internet là hệ thống mạng nội bộ đã an toàn tuyệt đối trước MS17-010 | Hầu hết các cuộc tấn công ban đầu quét qua Internet | Bác bỏ tính an toàn tuyệt đối: Kẻ tấn công hoặc phần mềm độc hại (WannaCry) một khi xâm nhập được vào 1 máy trạm nội bộ qua phishing/USB sẽ quét cổng 445 trong mạng LAN để lây lan ngang. Do đó phòng thủ nội bộ là bắt buộc |
| ALT-02 | Chỉ cần cập nhật bản vá MS17-010 là đủ, không cần thiết phải vô hiệu hóa giao thức SMBv1 | Hệ thống đã vá lỗi sẽ miễn nhiễm với mã khai thác EternalBlue đã biết | Bác bỏ: SMBv1 vốn có cấu trúc thiết kế lỗi thời, không hỗ trợ mã hóa dữ liệu, dùng hàm băm MD5 yếu và dễ bị tấn công SMB Relay. Tắt hoàn toàn SMBv1 là khuyến nghị bắt buộc của Microsoft |

## Điều chưa thể kết luận

- Chưa thể kết luận định lượng về độ trễ truyền tệp và tác động tài nguyên thực tế trên các dòng máy chủ doanh nghiệp quy mô lớn, do đề tài hiện tại giới hạn thực nghiệm trên môi trường ảo hóa lab cô lập và **tuân thủ chỉ thị tránh số liệu demo thực tế của tác giả**.
