# Đề cương lập luận

## Ngân sách toàn văn

- Tổng số từ dự kiến: 18,000 - 24,000 từ (tương đương 50 - 70 trang A4 theo chuẩn HUIT).
- Giới hạn cơ sở đào tạo: Đồ án chuyên ngành từ 40 - 80 trang.
- Phần không tính vào giới hạn: Trang bìa, phụ bìa, nhiệm vụ đề tài, lời cam đoan, mục lục, danh mục từ viết tắt, danh mục bảng/hình, tài liệu tham khảo, phụ lục.

## Cấu trúc chi tiết và phân bổ lập luận

| Phần / Chương | Câu hỏi cần trả lời | Kết luận cần đạt | Claim IDs | Nguồn & Bằng chứng | Ngân sách từ | Ràng buộc loại trừ |
|---|---|---|---|---|---|---|
| **Mở đầu** | Vì sao cần nghiên cứu kiểm thử và phòng thủ SMB trên Windows? Mục tiêu, phạm vi và nguyên tắc an toàn là gì? | Xác lập tính cấp thiết của đề tài, 4 mục tiêu kỹ thuật, phạm vi lab cô lập và cam kết đạo đức an ninh mạng | Nền tảng | Đề cương chi tiết HUIT, [7], [10] | 1,200 - 1,500 từ | Không đưa kết quả thực nghiệm vào mở đầu |
| **Chương 1: Cơ sở lý thuyết và công cụ kiểm thử SMB** | SMB hoạt động ra sao? MS17-010 phát sinh từ đâu? Công cụ và tiêu chí nhận diện/xác minh gồm những gì? | Hệ thống hóa toàn diện kiến trúc SMB, phân tích cơ chế lỗi nhân `srv.sys` của MS17-010, xác định rõ 4 mức tiêu chí nhận diện | C001, C002, C003 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S011 | 7,000 - 8,500 từ | Không viết lan man lịch sử Windows chung |
| **Chương 2: Thiết kế và triển khai mô hình thực nghiệm** | Môi trường lab cô lập cần được thiết kế và cấu hình như thế nào để đảm bảo tính an toàn, khôi phục được và chuẩn hóa kiểm thử? | Thiết lập kiến trúc mạng ảo Host-only cô lập, bảng IP tĩnh, cơ chế snapshot máy ảo và bộ kịch bản kiểm thử có kiểm soát | C004 | S010, S012, Đề cương chi tiết | 3,000 - 3,500 từ | Không cấu hình card mạng Bridged ra Internet |
| **Chương 3: Thực nghiệm kiểm thử SMB** | Quy trình khảo sát, quét NSE và xác minh mức độ tác động của MS17-010 được thực hiện theo những bước chuẩn hóa nào? | Chuẩn hóa phương pháp luận kiểm thử, phân định rõ giữa banner grab và xác minh lỗ hổng thực tế | C003, C004 | S003, S004, S005, S012 | 2,500 - 3,500 từ | **Tránh demo và số liệu demo thực tế theo chỉ thị của tác giả** (gán nhãn `[CẦN DỮ LIỆU]`) |
| **Chương 4: Đánh giá kết quả, phân tích rủi ro và khuyến nghị** | Tác động của MS17-010 tới CIA là gì? Các biện pháp phòng thủ nào triệt để nhất và rủi ro tương thích cần quản lý ra sao? | Thiết lập ma trận trước-sau phòng thủ, xây dựng lộ trình hardening đa tầng (patch, disable SMBv1, firewall, segmentation) | C005, C006 | S001, S002, S011 | 3,500 - 4,500 từ | Không đưa khuyến nghị mơ hồ, chung chung |
| **Kết luận và kiến nghị** | Đề tài đã đạt được những gì so với đề cương? Đâu là giới hạn và hướng phát triển? | Tổng kết các đóng góp lý thuyết và phương pháp luận; chỉ rõ hạn chế thiếu số liệu lab thực tế và đề xuất hướng mở rộng | Tổng kết | Đề cương HUIT | 800 - 1,200 từ | Không kết luận vượt quá phạm vi dữ liệu |

## Mạch chuyển chương (Chapter Transitions)

1. **Từ Mở đầu sang Chương 1**: Sau khi xác lập tính cấp thiết và phạm vi nghiên cứu, Chương 1 xây dựng nền tảng lý thuyết vững chắc về giao thức SMB và giải phẫu chuyên sâu cơ chế lỗi bộ nhớ mức nhân của MS17-010.
2. **Từ Chương 1 sang Chương 2**: Khi cơ chế lỗ hổng và tiêu chí lý thuyết đã sáng tỏ, Chương 2 hiện thực hóa bằng mô hình kiến trúc lab mạng cô lập và kịch bản kiểm thử an toàn.
3. **Từ Chương 2 sang Chương 3**: Dựa trên hạ tầng lab và kịch bản đã duyệt, Chương 3 chuẩn hóa quy trình thực nghiệm từ quét nhận diện cổng đến phương pháp xác minh lỗ hổng có kiểm soát.
4. **Từ Chương 3 sang Chương 4**: Từ các cấp độ phát hiện trong thực nghiệm, Chương 4 nâng tầm lên phân tích rủi ro hệ thống và đề xuất chiến lược phòng thủ đa tầng bền vững.
5. **Từ Chương 4 sang Kết luận**: Đóng gói toàn bộ công trình, đánh giá mức độ hoàn thành so với CLO của đề cương HUIT và vạch ra định hướng nghiên cứu tiếp theo.
