# MỞ ĐẦU

## 1. Lý do chọn đề tài

Giao thức chia sẻ tài nguyên qua mạng (Server Message Block – SMB) cho phép các máy Windows truy cập tệp và tài nguyên được chia sẻ. Bên gửi yêu cầu truy cập (Client) kết nối tới bên cung cấp và xử lý yêu cầu (Server); một máy có thể đảm nhiệm cả hai vai trò tùy kết nối [1]. Vì dịch vụ này trực tiếp phục vụ việc sử dụng dữ liệu, lỗi trong xử lý yêu cầu SMB cần được xem xét cùng với điều kiện truy cập tới Server.

Tháng 3 năm 2017, Microsoft công bố thông báo bảo mật MS17-010 để xử lý sáu lỗ hổng liên quan đến SMBv1, gồm các lỗi thực thi mã từ xa và một lỗi tiết lộ thông tin. CVE-2017-0144 là một lỗ hổng được định danh trong nhóm này [2]. EternalBlue là tên mã khai thác; tài liệu module của Rapid7 mô tả cách khai thác lỗi xử lý bộ nhớ của SMBv1 [3]. Ba tên gọi có liên quan nhưng không cùng nghĩa: MS17-010 xác định phạm vi cập nhật bảo mật, mã CVE định danh lỗ hổng, còn EternalBlue chỉ phương tiện khai thác.

WannaCry cho thấy mối liên hệ giữa lỗ hổng SMB và khả năng lây lan mã độc. Phân tích của Microsoft ghi nhận mã độc sử dụng mã khai thác SMB để lan sang máy Windows chưa cài cập nhật tương ứng [4]. Kiểm tra bản vá cần được thực hiện cùng khảo sát dịch vụ.

Trong đồ án, vấn đề cần giải quyết là xác định một kết quả kiểm tra thực sự chứng minh được điều gì. Cổng TCP 445 mở cho biết có thể tiếp cận dịch vụ từ vị trí kiểm tra; kết quả đó chưa xác định phiên bản SMB hay bản vá [5]. Tương tự, Microsoft cung cấp cách quản lý việc bật, tắt SMBv1 riêng với các phiên bản sau [6], nên cấu hình giao thức cần được đối chiếu cùng trạng thái cập nhật [2]. Nếu gộp các trạng thái này, việc đánh giá phòng thủ cũng dễ nhầm giữa dịch vụ bị chặn và lỗi đã được sửa.

Đề tài “Xây dựng mô hình kiểm thử lỗ hổng SMB trên Windows bằng Kali Linux” tập trung làm rõ quan hệ giữa cơ chế giao thức, điều kiện ảnh hưởng và bằng chứng kiểm thử để đánh giá đúng tác động của biện pháp phòng thủ.

## 2. Mục tiêu nghiên cứu

### 2.1. Mục tiêu tổng quát

Đề tài nghiên cứu cơ chế SMB trên Windows và nhóm lỗ hổng được xử lý trong MS17-010, lấy CVE-2017-0144 làm trọng tâm phân tích. Trên cơ sở đó, đồ án thiết kế mô hình kiểm thử bằng Kali Linux và phương pháp so sánh trước, sau phòng thủ. Mục tiêu là giải thích được điều kiện dẫn tới mỗi kết luận, thay vì chỉ ghi nhận kết quả của công cụ.

### 2.2. Mục tiêu kỹ thuật cụ thể

Mục tiêu thứ nhất là giải thích vai trò Client, Server và trình tự thương lượng phiên bản, xác thực, thiết lập phiên, truy cập tài nguyên. Các đặc tính của SMBv1, SMBv2 và SMBv3 được so sánh theo chức năng.

Mục tiêu thứ hai là phân tích cơ chế lỗi, hệ điều hành bị ảnh hưởng và điều kiện liên quan đến CVE-2017-0144; phân biệt phạm vi MS17-010 với mã khai thác EternalBlue. Phân tích phải gắn tác động dự kiến với điều kiện kỹ thuật tương ứng.

Mục tiêu thứ ba là thiết kế mô hình thực nghiệm và bộ tiêu chí phân biệt bốn mức: phát hiện dịch vụ, nhận diện SMBv1, phát hiện dấu hiệu lỗ hổng và xác minh theo bằng chứng. Vai trò Nmap, bộ kịch bản kiểm tra của Nmap (Nmap Scripting Engine – NSE) và Metasploit Framework được xác định theo từng bước.

Mục tiêu thứ tư là đề xuất cập nhật bản vá, vô hiệu hóa SMBv1, giới hạn kết nối và phân đoạn mạng; xác định cách kiểm tra lại từng biện pháp. Việc đánh giá cần xét cả rủi ro còn lại và khả năng Client tiếp tục truy cập tài nguyên cần thiết.

## 3. Đối tượng và phạm vi nghiên cứu

Đối tượng nghiên cứu gồm cơ chế SMB trên Windows, các lỗ hổng trong phạm vi MS17-010 và công cụ phục vụ kiểm thử. SMBv2, SMBv3 được dùng để đối chiếu đặc tính giao thức; phân tích lỗ hổng tập trung vào SMBv1 và CVE-2017-0144. Kali Linux là môi trường công cụ, Nmap/NSE phục vụ khảo sát và kiểm tra dấu hiệu, còn Metasploit Framework được xem xét trong bước xác minh.

Phạm vi thực nghiệm dự kiến là các máy ảo và thành phần mạng trong mô hình đồ án, xét trạng thái bản vá, cấu hình SMB và đường kết nối tới Server. Đề tài không khảo sát tỷ lệ máy dễ bị tấn công trong doanh nghiệp hoặc so sánh toàn bộ công cụ kiểm thử.

Ở giai đoạn hiện tại, phần thực nghiệm chưa được dùng làm căn cứ kết luận. Log, kết quả lệnh và đối chiếu trước, sau sẽ được bổ sung khi có dữ liệu thực tế. Phân tích tài liệu và thiết kế phương pháp không thay thế cho kết quả chạy mô hình.

## 4. Phương pháp tiếp cận và quy trình nghiên cứu

Đề tài kết hợp phân tích tài liệu với thiết kế mô hình và so sánh. Tài liệu Microsoft xác định hành vi giao thức, phạm vi cập nhật; tài liệu gốc của công cụ giải thích phép kiểm tra. Hướng dẫn NIST SP 800-115 cung cấp cơ sở tổ chức lập kế hoạch, kiểm tra, phân tích phát hiện và đề xuất giảm thiểu [7]. Đồ án cụ thể hóa quy trình theo câu hỏi nghiên cứu.

Trình tự nghiên cứu bắt đầu bằng xác định cơ chế và điều kiện ảnh hưởng, sau đó thiết kế mô hình cùng tiêu chí kết luận. Bước khảo sát xác định khả năng kết nối và giao thức; bước kiểm tra lỗ hổng đối chiếu phản hồi công cụ với cấu hình, bản vá. Khi bằng chứng không đủ, kết quả được giữ ở mức chưa xác định thay vì chuyển thành kết luận máy đã được vá.

Phương pháp so sánh sử dụng cùng tiêu chí trước và sau thay đổi. Bản vá tác động tới xử lý yêu cầu, còn tường lửa kiểm soát lưu lượng giữa máy hoặc mạng [2], [8]; hai biện pháp cần được đánh giá theo tác động khác nhau. Nếu máy kiểm thử không kết nối được sau thay đổi, cần xét đường kết nối trước khi kết luận về lỗ hổng. Khả năng truy cập từ Client cũng là tiêu chí đối chiếu để tránh xem việc mất chức năng chia sẻ là một kết quả phòng thủ đầy đủ.

## 5. Nguyên tắc an toàn và giới hạn kiểm thử

Mọi thao tác chỉ được thực hiện trên hệ thống thuộc quyền sở hữu hoặc được cho phép rõ ràng. Phạm vi máy, phương pháp và điều kiện dừng phải được xác định trước lượt kiểm tra, phù hợp với yêu cầu lập kế hoạch đánh giá của NIST [7]. Mạng thực nghiệm phải được cô lập; máy Windows chưa vá không được đưa ra mạng thật hoặc Internet. Kết nối mạng cầu nối (Bridged Adapter) không được dùng cho máy mục tiêu.

Kiểm thử ưu tiên bước khảo sát và đối chiếu ít tác động trước khi xem xét khai thác. Rapid7 cảnh báo module EternalBlue có thể gây mất ổn định, khởi động lại hoặc lỗi màn hình xanh [3]. Phải chuẩn bị khả năng phục hồi và dừng khi có ảnh hưởng ngoài dự kiến; máy bị treo không được coi là bằng chứng khai thác thành công. Kết quả trong một mô hình chỉ có giá trị với cấu hình và điều kiện đã kiểm tra.

## 6. Ý nghĩa khoa học và giá trị thực tiễn

Giá trị dự kiến về mặt học thuật là cách tổ chức quan hệ giữa kiến thức giao thức, điều kiện lỗ hổng và tiêu chí bằng chứng. Việc phân biệt các mức kết luận giúp giải thích vì sao một phản hồi công cụ chưa đủ để chứng minh toàn bộ trạng thái Server. Đồ án vận dụng tài liệu đã công bố, không đặt mục tiêu phát hiện lỗ hổng mới.

Về thực tiễn, mô hình kiểm thử, tiêu chí đối chiếu và khuyến nghị dự kiến hỗ trợ việc đọc kết quả kiểm tra, lựa chọn biện pháp phòng thủ. Hiệu quả và ảnh hưởng tương thích chỉ được đánh giá sau khi có dữ liệu thực tế.

## 7. Bố cục của báo cáo

Chương 1 trình bày cơ sở lý thuyết SMB, MS17-010, công cụ và tiêu chí xác minh. Chương 2 trình bày thiết kế và triển khai mô hình thực nghiệm. Chương 3 dành cho thực nghiệm kiểm thử SMB theo quy trình đã xác định. Chương 4 đối chiếu kết quả, phân tích rủi ro và đưa ra khuyến nghị. Phần kết luận tổng hợp mức đạt mục tiêu, giới hạn và hướng phát triển dựa trên nội dung thực tế của báo cáo.

## TÀI LIỆU THAM KHẢO

[1] Microsoft, "What is SMB File Sharing for Windows and Windows Server?," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview. [Accessed: Oct. 4, 2026].

[2] Microsoft, "Microsoft Security Bulletin MS17-010 – Critical," Microsoft Learn / Security TechCenter, Mar. 2017. [Online]. Available: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010. [Accessed: Oct. 4, 2026].

[3] Rapid7, "MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption," Rapid7 Exploit Database, 2017. [Online]. Available: https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/. [Accessed: Oct. 4, 2026].

[4] Microsoft Threat Intelligence, "WannaCrypt ransomware worm targets out-of-date systems," Microsoft Security Blog, May 2017. [Online]. Available: https://www.microsoft.com/en-us/security/blog/2017/05/12/wannacrypt-ransomware-worm-targets-out-of-date-systems/. [Accessed: Oct. 4, 2026].

[5] Microsoft, "Direct hosting of SMB over TCP/IP," Microsoft Learn, 2026. [Online]. Available: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/direct-hosting-of-smb-over-tcpip. [Accessed: Oct. 4, 2026].

[6] Microsoft, "Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3. [Accessed: Oct. 4, 2026].

[7] K. Scarfone, M. Souppaya, A. Cody, and A. Orebaugh, Technical Guide to Information Security Testing and Assessment, NIST SP 800-115, Sep. 2008. [Online]. Available: https://csrc.nist.gov/pubs/sp/800/115/final. [Accessed: Oct. 4, 2026].

[8] K. Scarfone and P. Hoffman, Guidelines on Firewalls and Firewall Policy, NIST SP 800-41 Rev. 1, Sep. 2009. [Online]. Available: https://csrc.nist.gov/pubs/sp/800/41/r1/final. [Accessed: Oct. 4, 2026].
