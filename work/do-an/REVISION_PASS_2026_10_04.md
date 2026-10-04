# Biên tập nguồn, lập luận và giọng viết Chương 1–2

Trạng thái: REVISED_REVIEW_PENDING. Đây là báo cáo thay đổi của bản thảo Markdown, không phải phê duyệt chương hoặc bản Word cuối. Người dùng xác nhận không còn yêu cầu chỉnh giọng; không yêu cầu duyệt lại AUTHOR_VOICE.

## Thay đổi đã áp dụng

Đã thay cách dịch thô bằng tên đối tượng cụ thể: yêu cầu/phản hồi SMB, thông điệp SMB khi nói đến cấu trúc, gói tin TCP khi nói đến lưu lượng; thay phần mô tả Client–Server bằng vai trò chức năng có nguồn, bỏ sơ đồ nội bộ Windows chưa được kiểm chứng. Mở đầu và tổng kết được viết thành các đoạn liên tục. Các bảng, bước thao tác cần đối chiếu vẫn được giữ.

Chương 1 đã thay nguồn khái niệm SMB, quy trình giao tiếp, chính sách tường lửa, Kali và Metasploit bằng tài liệu gốc công khai. Không dùng overview thay mọi nội dung sách: các câu về lịch sử, số lệnh, tối ưu AES, mô hình driver và các chi tiết không cần cho luận điểm nhưng chưa có nguồn phù hợp đã được bỏ hoặc thu hẹp. Đã bỏ CISA lỗi truy cập khỏi danh mục đang sử dụng; phần WannaCry chỉ giữ các nhận định đã đọc trong Microsoft, bỏ số liệu hơn 150 quốc gia chưa đối chiếu. Các sách cũ vẫn ở ledger RECHECK để truy vết, không còn là bằng chứng được viện dẫn trong bản thảo mới.

Chương 2 được sửa từ lời khẳng định kết quả sang thiết kế kiểm chứng. Bảng trạng thái là giả thuyết cấu hình, không phải số liệu đo. Không gán các trạng thái phía sau là False chỉ vì không truy cập được Server. Đã thay công thức khi-và-chỉ-khi có tính vòng tròn bằng quan hệ điều kiện cần và nêu giới hạn của mô hình. Bốn trạng thái là chuỗi tích lũy: kết quả thất bại tại trạng thái sau chưa chứng minh riêng hiệu quả của biện pháp mới. Giữ nguyên thiết kế ba VLAN và chuỗi cấu hình đã chọn, không tự mở rộng sang tám tổ hợp thử nghiệm.

Đã bỏ lời khẳng định `unsafe=0` bảo đảm an toàn, bỏ thời gian rollback dưới 10 giây như kết quả đã đo, bỏ nhận định thử lại gần như chắc chắn gây mã BSOD cụ thể. Nmap/Metasploit scanner được mô tả là kiểm tra chéo, không gọi hai phép thăm dò cùng dấu hiệu là bằng chứng hoàn toàn độc lập. Quyền SYSTEM trong output cũng không tự chứng minh kiểm soát toàn bộ nhân. Những kết quả cần chạy thật tiếp tục có nhãn `[CẦN DỮ LIỆU]` theo DEC-03.

## Nguồn gốc đã đối chiếu trong lượt này

| Nguồn | Vị trí thực đã đọc | Quyết định |
|---|---|---|
| S020 – Microsoft SMB/CIFS Overview | Overview; chức năng; request/response | Dùng cho khái niệm và vai trò cơ bản, không dùng chứng minh driver |
| S006 – SMB File Sharing Overview | SMB components; SMB dialects | Dùng cho vai trò Client/Server và UNC; sửa URL/năm theo ledger |
| S002 – Direct hosting of SMB over TCP/IP | Summary; More information; cập nhật 2026-02-12 | Chỉ nêu thử hai phương thức khi đều bật; bỏ diễn giải luôn ưu tiên 445 và RST |
| S022 – MS-SMB2 | Connecting to a Share by Using an SMB2 Negotiate, đoạn SESSION_SETUP và TREE_CONNECT | Xác nhận SessionId/TreeId và trình tự, không dùng chứng minh nội bộ Windows |
| S028 – MS-CIFS | Per SMB Session; 3.2.5.4 Receiving a Tree Connect Response | Xác nhận UID/TID và quan hệ phiên–tài nguyên |
| S018 – mã NSE | check_ms17010; action; mã CVE gán trong báo cáo | Phân biệt dấu hiệu, lỗi kiểm tra và khai thác; CVE trong báo cáo hiện hành là 2017-0143, không xác nhận riêng 2017-0144 |
| Tài liệu NSE và thư viện gốc | Script Arguments; smb.lua start_ex; smbauth.lua, vulns.lua tìm unsafe | Không tìm thấy cơ sở cho diễn giải unsafe ở phiên bản nguồn hiện hành. Không khái quát mọi phiên bản lịch sử; phải ghi phiên bản lab khi triển khai |
| S013 – Rapid7 EternalBlue | Description | Hỗ trợ lỗi FEA, pool grooming, nguy cơ BSOD/reboot; không hỗ trợ khẳng định tần suất gần như chắc chắn |
| S024 – NIST SP 800-115 | Appendix B, Rules of Engagement Template | Tham khảo phạm vi/điều kiện kiểm thử; snapshot và số lần thử là thiết kế riêng của đề tài |
| S025 – NIST SP 800-41 Rev.1 | Chính sách deny by default, PDF trang 28; ghi nhật ký chính sách, PDF trang 33 | Dùng cho chính sách lọc lưu lượng; sơ đồ VLAN/IP là đề xuất, không phải mô hình được NIST xác nhận |
| S015 – Microsoft WannaCrypt | Spreading capability; Protection against the WannaCrypt attack | Thu hẹp phần lịch sử theo nội dung đọc được |
| S026 – Kali | About Kali Linux | Mô tả nền tảng, không suy diễn dùng Kali tự bảo đảm cô lập |
| S027 – Rapid7 Framework | Metasploit Framework; Finding Modules | Mô tả nền tảng và loại module |

Đọc trực tiếp nguồn gốc là xác minh tương đương cho những vị trí trên, không phải tái kiểm tra NotebookLM. Phiên này không có công cụ NotebookLM; không ghi đã nhập nguồn mới hoặc xác nhận tình trạng notebook hiện tại. Các nguồn lịch sử VERIFIED khác chưa được chứng nhận lại toàn bộ bởi lượt này.

URL bổ sung: [MS-SMB2](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-smb2/c9efe8ca-ff34-44d0-bfbe-58a9b9db50d4), [MS-CIFS Tree Connect](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cifs/c7cb45aa-f923-4cd4-a9d5-4a1418e41d42), [MS-CIFS Session](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cifs/c42729fb-c655-424f-8d9a-44825d609b86), [NSE documentation](https://nmap.org/nsedoc/scripts/smb-vuln-ms17-010.html), [smb.lua](https://svn.nmap.org/nmap/nselib/smb.lua), [smbauth.lua](https://svn.nmap.org/nmap/nselib/smbauth.lua), [vulns.lua](https://svn.nmap.org/nmap/nselib/vulns.lua). Các nguồn chính đã có URL trong ledger và bibliography.

## Ánh xạ số dẫn cũ sang bản thảo mới

Số cũ là số ở bản trước lượt biên tập, không phải source ID. Đây là ánh xạ danh tính nguồn/tuyến thay thế; không hàm ý mọi câu cũ được giữ nguyên.

| Số Chương 1 cũ | Số mới | Source ID / xử lý |
|---|---|---|
| 1 | 1 | S020 thay sách; thu hẹp định nghĩa |
| 2 | 2 | S002; sửa phạm vi lựa chọn cổng |
| 3 | 7 | S022 thay tuyến giao thức; bỏ các câu nội bộ chưa hỗ trợ |
| 4 | 8 | S028 thay tuyến UID/TID; bỏ các câu nội bộ chưa hỗ trợ |
| 5 | 4 | S005 |
| 6 | 3 | S006 |
| 7 | 5 | S007 |
| 8 | 6 | S008 |
| 9 | 13 | S025 thay chính sách firewall; phần CIA viết lại |
| 10 | 9 | S010 |
| 11 | 10 | S011 |
| 12 | 11 | S012 |
| 13 | 12 | S013 |
| 14 | Bỏ | S014 chưa khả dụng; phần lịch sử thu hẹp và dùng S015 |
| 15 | 14 | S015 |
| 16 | 15 | S026 cho Kali; không dùng để chứng minh mọi thao tác lab |
| 17 | 16 | S017 |
| 18 | 17 | S018 |
| 19 | 18 | S027 thay mô tả Framework |

| Số Chương 2 cũ | Số mới | Source ID / xử lý |
|---|---|---|
| 1 | 1 | S024 thay tuyến phạm vi/quy trình |
| 2 | 2 | S025 thay tuyến chính sách mạng |
| 3 | 8 | S013 cho phần FEA có hỗ trợ; thu hẹp diễn giải |
| 4 | 5 | S005 |
| 5 | 8 | S013 |
| 6 | 7 | S027 cho Framework; không thay sách cho mọi chi tiết |
| 7 | 6 | S008 |
| 8 | 3 | S017 |
| 9 | 4 | S018 |

Hai chương hiện có danh mục riêng. Khi ghép báo cáo phải đánh số IEEE toàn cục theo thứ tự xuất hiện, không nối nguyên hai danh mục hoặc coi kiểm tra riêng chương là kiểm tra bản ghép.

## Kiểm tra và việc còn lại

Citation cấu trúc đạt: Chương 1 có 88 lượt dẫn/18 mục; Chương 2 có 32 lượt dẫn/8 mục; không thiếu, mồ côi hoặc sai thứ tự trong từng chương. Lint tư vấn không còn cảnh báo câu dài; ba cảnh báo lặp cấu trúc còn lại đã phân loại ở STYLE_REVIEW.md. Các nhãn dữ liệu là giới hạn thật, không được xóa để làm publication lint đạt.

Cần review nội dung bản đã sửa trước khi phê duyệt chương. Mâu thuẫn OUTLINE Host-only/ngân sách và hợp đồng ba VLAN vẫn cần đồng bộ theo lịch sử quyết định; lượt này không thay artifact LOCKED. DOCX cũ chưa được dựng lại vì Markdown chưa được duyệt. Không coi nhãn PASS/điểm số cũ là đánh giá bản thảo hiện hành.

Kiểm tra repository sau cập nhật: validate_project.py đạt; unittest đạt 7/7; git diff --check không có lỗi whitespace. Công cụ trung gian và kết quả JSON được giữ trong .tmp đã ignore; không phải sản phẩm bàn giao.
