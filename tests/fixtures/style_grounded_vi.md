# Kiểm tra cấu hình dịch vụ

Thử nghiệm so sánh hai cấu hình trên cùng máy đích và cùng tập yêu cầu. Cấu hình A cho phép lưu lượng TCP đến dịch vụ; cấu hình B chặn lưu lượng này tại tường lửa máy đích. Mỗi cấu hình được đo ba lần sau khi khôi phục snapshot.

Ở cấu hình A, máy kiểm thử thiết lập được kết nối trong cả ba lần đo. Khi chuyển sang cấu hình B, không lần đo nào hoàn tất bắt tay TCP. Kết quả chỉ chứng minh tác dụng của luật tường lửa trong topology phòng lab; nó không cho phép kết luận về các mạng có thiết bị trung gian hoặc chính sách định tuyến khác.

Sự khác biệt trên trả lời câu hỏi của mục này: luật chặn làm mất đường kết nối quan sát được từ vị trí máy kiểm thử. Phần tiếp theo kiểm tra liệu dịch vụ nội bộ vẫn hoạt động hay đã bị vô hiệu hóa.
