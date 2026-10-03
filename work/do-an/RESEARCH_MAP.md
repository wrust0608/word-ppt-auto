# Bản đồ nghiên cứu

## Vấn đề trung tâm

Nguy cơ an ninh bắt nguồn từ việc duy trì giao thức SMBv1 không an toàn trên các hệ thống Windows trong mạng nội bộ, dẫn đến nguy cơ bị tấn công thực thi mã từ xa mức nhân qua nhóm lỗ hổng MS17-010 (tiêu biểu là EternalBlue / CVE-2017-0144); đồng thời giải quyết yêu cầu xây dựng quy trình kiểm thử đánh giá có kiểm soát và giải pháp phòng thủ đa tầng có đối chứng.

## Khoảng trống cần xử lý

1. Nhầm lẫn phổ biến giữa trạng thái "cổng 445 đang mở / SMBv1 đang bật" với trạng thái "hệ thống thực sự tồn tại lỗ hổng MS17-010 chưa được vá".
2. Thiếu quy trình kiểm thử an toàn trong môi trường mạng cô lập có cơ chế kiểm soát rủi ro và khôi phục sự cố.
3. Thiếu khung đối chiếu toàn diện về hiệu quả và rủi ro tương thích khi triển khai các biện pháp phòng thủ SMB (cập nhật bản vá, vô hiệu hóa SMBv1, giới hạn cổng 445, phân đoạn mạng).

## Câu hỏi nghiên cứu

| ID | Câu hỏi | Có thể trả lời bằng | Tiêu chí hoàn thành |
|---|---|---|---|
| RQ1 | Kiến trúc, cơ chế bắt tay (dialect negotiation, session setup, tree connect) và sự khác biệt về bảo mật giữa SMBv1, SMBv2, SMBv3 trên Windows là gì? | Phân tích tài liệu kỹ thuật Microsoft, chuẩn giao thức và giáo trình chuyên ngành | Lập bảng so sánh chi tiết các đặc tính bảo mật, mã lệnh, mã hóa, signing và cổng dịch vụ giữa 3 phiên bản |
| RQ2 | Cơ chế phát sinh lỗi bộ nhớ dẫn đến nhóm lỗ hổng MS17-010 (CVE-2017-0144) trong driver srv.sys là gì và điều kiện tác động thực tế ra sao? | Phân tích bản tin bảo mật MS17-010, cơ sở dữ liệu NVD, Windows Internals | Làm rõ cơ chế xử lý gói tin sai trong kernel, điều kiện cần và mức độ ảnh hưởng đến CIA |
| RQ3 | Mô hình lab cô lập cần được thiết kế như thế nào để phục vụ quét, nhận diện và xác minh an toàn trạng thái SMB mà không vi phạm nguyên tắc đạo đức? | Thiết kế kiến trúc mạng ảo Host-only/Internal, phân bổ IP, snapshot, quy trình Nmap/NSE | Bản vẽ sơ đồ lab, bảng tham số cấu hình mạng và bộ tiêu chí xác minh 4 mức |
| RQ4 | Các biện pháp phòng thủ kỹ thuật nào giúp triệt tiêu nguy cơ MS17-010 và những rủi ro tương thích hệ thống cần lường trước là gì? | Nghiên cứu tài liệu hardening của Microsoft, phân tích tác động tương thích | Bảng ma trận so sánh trước-sau phòng thủ và danh mục khuyến nghị đa tầng |

## Mục tiêu

| ID | Mục tiêu | Câu hỏi liên quan | Sản phẩm/bằng chứng |
|---|---|---|---|
| O1 | Hệ thống hóa cơ sở lý thuyết về kiến trúc và giao thức SMB trên Windows | RQ1 | Báo cáo Chương 1 (mục 1.1) với sơ đồ luồng bản tin và bảng so sánh SMBv1-v3 |
| O2 | Phân tích chuyên sâu cơ chế kỹ thuật và bề mặt tấn công của MS17-010 | RQ2 | Báo cáo Chương 1 (mục 1.2) với phân tích CVE, driver srv.sys và ma trận điều kiện ảnh hưởng |
| O3 | Thiết kế kiến trúc lab cô lập và xây dựng bộ tiêu chí xác minh trạng thái an toàn SMB | RQ3 | Thiết kế Chương 2 & Tiêu chí Chương 1 (mục 1.4); kịch bản kiểm thử có kiểm soát |
| O4 | Đề xuất giải pháp phòng thủ đa tầng, đánh giá rủi ro và phân tích tương thích | RQ4 | Báo cáo Chương 4 với ma trận trước-sau phòng thủ và hướng dẫn hardening |

## Phương pháp

| ID | Phương pháp | Đầu vào | Đầu ra | Giới hạn |
|---|---|---|---|---|
| M1 | Phân tích tài liệu học thuật và tiêu chuẩn kỹ thuật | MS17-010, RFC, Microsoft Learn, Windows Internals | Báo cáo lý thuyết và sơ đồ cơ chế | Phụ thuộc vào tài liệu chính thống công bố |
| M2 | Thiết kế kiến trúc mô hình thực nghiệm ảo hóa | Yêu cầu cô lập lab, sơ đồ kết nối, dải địa chỉ IP | Sơ đồ mạng lab, bảng thông số máy ảo | Giới hạn trong môi trường ảo hóa nội bộ |
| M3 | Phương pháp kiểm thử an ninh mạng theo chuẩn có kiểm soát | Công cụ Kali Linux, Nmap, NSE, Metasploit | Kịch bản kiểm thử, tiêu chí xác minh trạng thái | **Hiện tại tránh demo và kết quả demo thực tế theo chỉ thị người dùng** |
| M4 | Phân tích so sánh và đánh giá rủi ro | Trạng thái trước và sau khi áp dụng biện pháp bảo vệ | Bảng so sánh trước-sau, danh mục khuyến nghị | Cần xác thực thực tế khi có số liệu demo |

## Phạm vi và giả định

- Trong phạm vi: Kiến trúc giao thức SMB (v1, v2, v3); lỗ hổng MS17-010 / CVE-2017-0144; công cụ Nmap, NSE, Metasploit trong Kali Linux; biện pháp phòng thủ (patch, disable SMBv1, firewall 445, network segmentation).
- Ngoài phạm vi: **Tránh các phần liên quan đến demo và kết quả demo thực tế ở giai đoạn hiện tại (theo yêu cầu người dùng)**; không phát tán mã độc; không kiểm thử ngoài môi trường lab cô lập.
- Giả định: Môi trường lab được cách ly hoàn toàn với mạng bên ngoài; máy ảo Windows mục tiêu hỗ trợ cơ chế snapshot.
- Ràng buộc: Tuân thủ quy định trình bày HUIT 2024; tuân thủ thời hạn 10 tuần; tuân thủ nguyên tắc không bịa dữ liệu.

## Tiêu chí đánh giá toàn công trình

1. Tính chính xác kỹ thuật: Phân biệt rõ ràng giữa các khái niệm (cổng mở vs dịch vụ chạy vs lỗ hổng tồn tại).
2. Tính hệ thống: Lập luận có cấu trúc xuyên suốt từ cơ chế giao thức -> nguyên nhân lỗ hổng -> phương pháp phát hiện -> giải pháp phòng thủ.
3. Tính trung thực học thuật: Mọi khẳng định kỹ thuật đều có trích dẫn nguồn chuẩn (Microsoft, NIST, Nmap, giáo trình); các phần chưa có dữ liệu thực nghiệm được gắn nhãn `[CẦN DỮ LIỆU]` thay vì suy đoán.
