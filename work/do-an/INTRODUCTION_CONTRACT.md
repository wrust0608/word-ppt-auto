# Hợp đồng phần Mở đầu

Ngày 2026-10-04. Phạm vi: Mở đầu độc lập để review, không chứng nhận hoàn tất các chương hoặc dữ liệu thực nghiệm.

## Quyết định đầu vào

Đủ mục 1–7 và hai tiểu mục 2.1/2.2; đoạn liên tục, ít nhãn phụ; nguyên tắc an toàn chỉ ở mục 5; không khối quản lý trạng thái lab/bằng chứng/rollback. DOCX là đầu ra bắt buộc sau review nội dung, nguồn, giọng, citation và từng trang.

Tác giả đã cho phép lập bảng IEEE chung theo thứ tự xuất hiện từ Mở đầu, giữ nguyên hai chương và ghi bảng chuyển đổi khi ghép. Bảng bao phủ Mở đầu, Chương 1 và Chương 2 hiện có; chương chưa viết sẽ nối tiếp, không suy đoán nguồn tương lai.

Ngân sách thân bài: 1.200–1.500 đơn vị phân cách bằng khoảng trắng theo OUTLINE; biên 15% tối đa 1.725. Không tính tiêu đề/danh mục nguồn. Không kéo dài câu để đạt số từ.

## Nhiệm vụ từng mục và ma trận luận điểm

| Mục | Nhiệm vụ và loại luận điểm | Bằng chứng, giới hạn |
|---|---|---|
| 1 | SOURCE_FACT: vai trò SMB, MS17-010/CVE, EternalBlue, WannaCry; INTERPRETATION: trạng thái dịch vụ khác lỗ hổng | S006 SMB components; S005 bảng CVE/Vulnerability Information; S013 Description; S015 Attack vector; S008 quản lý phiên bản. Không thống kê quy mô hoặc nhận định doanh nghiệp nói chung |
| 2 | PROPOSAL: mục tiêu tổng quát và bốn mục tiêu kiểm chứng được | O1–O4, đề cương; không sửa LOCKED, không bảo đảm hiệu quả trước đo |
| 3 | PROPOSAL: đối tượng, công cụ, phạm vi suy luận | Phạm vi dự án, DEC-03; không chọn lại topology, không xác nhận đã triển khai |
| 4 | SOURCE_FACT: quy trình NIST; PROPOSAL: trình tự và đối chiếu của đồ án | S024 Abstract/chương 6; S025 Abstract; S005 về sửa lỗi. Không nhận quy trình riêng là toàn bộ NIST; không nhận mô hình tích lũy là thí nghiệm độc lập |
| 5 | Nguyên tắc an toàn và giới hạn | S024 chương 6; S013 cảnh báo crash. Không lệnh, tham số, trạng thái snapshot hoặc quy trình rollback chi tiết |
| 6 | PROPOSAL: giá trị dự kiến gắn với sản phẩm | O1–O4; không đóng góp mới/hiệu quả đã chứng minh; giá trị phải kiểm bằng dữ liệu |
| 7 | PROPOSAL: định hướng đọc bốn chương | Cấu trúc đã duyệt; không nhận thực nghiệm đã hoàn thành |

## Thiết kế Word

HUIT: A4; lề trên 3,5 cm, dưới 3 cm, trái 3,5 cm, phải 2 cm; Times New Roman 13 pt, giãn dòng 1,5, trước 0/sau 6 pt, thụt đầu dòng 1,25 cm, căn đều. Title đen 16 pt; Heading 1 đen 14 pt; Heading 2 đen 13 pt; PAGE Ả Rập giữa chân trang. Heading keep-with-next; đoạn widow control. Không cần bảng/hình/trang trí. DOCX mẫu là tham khảo cấu trúc/giọng, không phải template package để sao chép định dạng lịch sử.

Danh mục cuối Mở đầu là trích xuất nguồn đã dùng từ bảng chung, không tạo hệ số độc lập. Khi ghép, bỏ danh mục trích xuất và đặt danh mục chung một lần ở cuối; chuyển số trong bản ghép, không sửa hai chương canonical.

## Nghiệm thu

Review luận điểm/nguồn/phạm vi → giọng → lint tư vấn và publication → citation → cấu trúc Word → render Word gốc → xem mọi trang. PASS chỉ cho kiểm tra đã chạy. Checklist riêng Mở đầu nằm trong INTRODUCTION_REVIEW; checklist toàn luận văn vẫn BLOCKED.
