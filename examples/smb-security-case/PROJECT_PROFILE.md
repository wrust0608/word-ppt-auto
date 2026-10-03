# Hồ sơ ví dụ kiểm thử: đánh giá an toàn dịch vụ SMB

TEST FIXTURE. Không tự động nạp cho dự án khác và không xem đây là chủ đề mặc định.

- Mã dự án: smb-security-case
- Loại: đồ án chuyên ngành an toàn thông tin
- Chủ đề: đánh giá rủi ro trên dịch vụ SMB và kiểm chứng biện pháp giảm thiểu trong môi trường được cấp phép
- Vấn đề: thấy cổng 139/445 mở chưa đủ để kết luận có lỗ hổng; cần chuỗi bằng chứng từ phát hiện, nhận diện phiên bản/cấu hình, xác nhận điều kiện ảnh hưởng đến kiểm chứng và khuyến nghị.
- Câu hỏi chính: quy trình nào giúp đánh giá dịch vụ SMB có khả năng truy vết, hạn chế kết luận dương tính giả và chứng minh được tác dụng của biện pháp giảm thiểu?
- Đối tượng: máy thử nghiệm, dịch vụ SMB và cấu hình mạng trong phòng lab.
- Phạm vi: chỉ tài sản được cấp phép; không quét hoặc khai thác hệ thống bên ngoài.
- Phương pháp: nghiên cứu tài liệu, thiết kế lab, đo trước–sau và đối chiếu kết quả với tiêu chí đã khóa.
- Đóng góp dự kiến: quy trình đánh giá và bộ bằng chứng tái lập được, không phải phát hiện lỗ hổng mới.
- Trích dẫn: IEEE.
- Hồ sơ trình bày: profiles/HUIT_2024.md.

## Tài liệu đầu vào dùng để kiểm thử

- ATTT_DACN_01_DeCuongChiTiet.docx
- ATTT_DACN_01-BaoCao-Tuan2.docx
- KichBan-Nmap-SMB-139-445.docx

Các tài liệu chỉ dùng kiểm tra khả năng trích xuất mục tiêu, tiến độ và độ sâu. Chúng không định hình lõi skill và không là bằng chứng học thuật nếu chưa nhập/xác minh trong NotebookLM.

