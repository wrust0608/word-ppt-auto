## 3.1. Trạng thái baseline trước đo đạc

Việc xác định và ghi nhận trạng thái ban đầu (baseline) của hệ thống máy chủ mục tiêu trước khi thực hiện các kịch bản thực nghiệm là điều kiện cần thiết nhằm bảo đảm tính lặp lại và tính khách quan cho toàn bộ quá trình đo đạc. Mốc xuất phát này cung cấp các thông số định lượng cụ thể về cấu hình địa chỉ mạng, trạng thái hoạt động của dịch vụ chia sẻ tệp Server Message Block (SMB) và chính sách tường lửa. Thiết lập này cũng xác định mức độ cập nhật bản vá an ninh thực tế trên hệ điều hành Windows Server 2012 R2. Các dữ liệu đo đạc cục bộ thu thập tại thời điểm này đóng vai trò mốc tham chiếu độc lập để so sánh, đối chiếu với các tín hiệu phản hồi mạng đo được từ trạm kiểm thử trong các giai đoạn tiếp theo.

### 3.1.1. Trạng thái mạng và dịch vụ SMB

Môi trường thực nghiệm được thiết lập trên nền tảng ảo hóa với hai máy ảo chính gồm trạm kiểm thử Kali Linux và máy chủ mục tiêu Windows Server 2012 R2. Cả hai máy ảo đều được cấu hình duy nhất một bộ điều hợp mạng chế độ Host-Only Adapter, không gắn thêm card mạng NAT hay Bridged, qua đó giới hạn đường truyền dữ liệu trong phạm vi phân đoạn mạng thử nghiệm nội bộ. Bảng định tuyến trên trạm Kali Linux ghi nhận dải mạng cục bộ 192.168.56.0/24 qua giao diện eth0 với địa chỉ IP 192.168.56.10/24 và không kích hoạt tuyến đường mặc định (default route). Tương tự, máy chủ Windows Server 2012 R2 được gán địa chỉ IP 192.168.56.20/24 trên giao diện mạng Ethernet và bảng định tuyến cục bộ cũng không định tuyến kết nối ra bên ngoài mạng phân đoạn.

Kiểm tra kết nối tầng liên kết dữ liệu giữa hai máy ảo cho thấy bảng phân giải địa chỉ ARP trên trạm kiểm thử ghi nhận địa chỉ IP 192.168.56.20 ứng với địa chỉ phần cứng 08:00:27:55:71:ce ở trạng thái kết nối trực tiếp (REACHABLE). Tuy nhiên, phép thử gửi gói tin ICMP Echo Request từ trạm Kali Linux đến địa chỉ 192.168.56.20 ghi nhận tỷ lệ mất gói 100% khi không nhận được phản hồi. Hiện tượng mất gói tin ICMP được ghi nhận như một đặc tính quan sát thực tế trong cấu hình mạng ban đầu mà không gắn với bất kỳ kết luận chủ quan nào về nguyên nhân kiểm soát của tường lửa.

Trên máy chủ mục tiêu, dịch vụ chia sẻ tệp cốt lõi LanmanServer được xác nhận đang vận hành ở trạng thái Running với chế độ khởi động tự động (Automatic). Thành phần tính năng FS-SMB1 phục vụ giao thức SMBv1 hiển thị trạng thái đã cài đặt (Installed) trên hệ điều hành. Kiểm tra cấu hình cấu trúc dịch vụ SMB nội bộ ghi nhận hai cờ EnableSMB1Protocol và EnableSMB2Protocol đều mang giá trị True, chứng minh ngăn xếp SMB của máy chủ được thiết lập sẵn sàng đàm phán cả giao thức SMBv1 cùng các phiên bản SMB2 hoặc SMB3. Đối với cơ chế bảo vệ tính toàn vẹn dữ liệu, các thuộc tính EnableSecuritySignature và RequireSecuritySignature đều mang giá trị False, phản ánh thiết lập hệ thống cục bộ không ép buộc ký số các gói tin trao đổi. Kiểm tra trạng thái cổng mạng cục bộ qua tiến trình hệ thống (PID 4) xác nhận máy chủ đang mở cổng lắng nghe trên cổng TCP 445 ứng với giao thức IPv6/IPv4 và cổng TCP 139 trên địa chỉ IPv4 192.168.56.20.

Bảng 3.1 tổng hợp chi tiết các thông số mạng, dịch vụ chia sẻ tệp và cấu hình tường lửa ghi nhận được trên hai máy ảo tại thời điểm xuất phát.

**Bảng 3.1. Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc**

| Hạng mục | Giá trị ghi nhận | Ghi chú |
|---|---|---|
| Địa chỉ IP và mạng con Kali Linux | `192.168.56.10/24` (giao diện `eth0`) | Tuyến mạng cục bộ `192.168.56.0/24`, không cấu hình default route |
| Địa chỉ IP và mạng con Windows Server | `192.168.56.20/24` (giao diện `Ethernet`) | Bảng định tuyến cục bộ, không cấu hình default route |
| Cấu hình card mạng VirtualBox | 1 card Host-Only Adapter trên mỗi máy ảo | Cấu hình giới hạn đường truyền trong phân đoạn lab, không cấu hình card NAT hay Bridged |
| Dịch vụ chia sẻ tệp (LanmanServer) | `Running` (chế độ khởi động `Automatic`) | Dịch vụ SMB đang chạy cục bộ trên máy chủ mục tiêu |
| Tính năng Windows FS-SMB1 | `Installed` | Thành phần SMBv1 được cài đặt sẵn trên hệ điều hành |
| Cấu hình phương ngữ SMB cục bộ | `EnableSMB1Protocol : True`<br>`EnableSMB2Protocol : True` | Máy chủ kích hoạt hỗ trợ SMBv1 và SMB2/SMB3 ở mức cấu hình nội bộ |
| Chính sách ký số gói tin SMB nội bộ | `EnableSecuritySignature : False`<br>`RequireSecuritySignature : False` | Thiết lập ký số cục bộ không bắt buộc |
| Trạng thái lắng nghe cổng cục bộ | TCP 445 (`::`)<br>TCP 139 (`192.168.56.20`) | Tiến trình hệ thống đang lắng nghe cục bộ trên cổng 139 và 445 |
| Trạng thái hồ sơ Windows Firewall | Domain: `True`, Private: `True`, Public: `True` | Toàn bộ 3 hồ sơ tường lửa Windows đều được kích hoạt bảo vệ |
| Nhóm quy tắc chia sẻ tệp mặc định | 16 quy tắc `File and Printer Sharing` đều `False` | Các quy tắc chia sẻ tệp mặc định đều bị vô hiệu hóa |
| Quy tắc tường lửa tùy biến | Tên: `ATTT Lab SMB 139-445`<br>Action: `Allow`, Direction: `Inbound`<br>Protocol: `TCP`, LocalPort: `{139, 445}` | Quy tắc cho phép có phạm vi RemoteAddress giới hạn duy nhất tại `192.168.56.10` |

Hình 3.1 trình bày kết quả kiểm tra tổng hợp cấu hình mạng, trạng thái dịch vụ chia sẻ tệp và các cổng lắng nghe trên máy chủ Windows Server 2012 R2 thông qua giao diện Windows PowerShell trước thực nghiệm.

![Hình 3.1. Trạng thái mạng, dịch vụ SMB và các cổng lắng nghe trên Windows Server 2012 R2 trước thực nghiệm](chapter3/presentation/3_1/Hinh_3_1_Network_SMB.png)

Các dữ liệu hiển thị trên Hình 3.1 xác thực cấu hình mạng thực tế của giao diện Ethernet với địa chỉ 192.168.56.20/24, cùng với trạng thái vận hành của dịch vụ LanmanServer và việc cài đặt tính năng FS-SMB1. Cần phân định rõ ràng giữa trạng thái mở cổng lắng nghe nội bộ và khả năng tiếp cận dịch vụ từ xa qua mạng. Việc tiến trình hệ thống đang mở cổng lắng nghe trên cổng TCP 139 và TCP 445 chỉ phản ánh khả năng sẵn sàng xử lý yêu cầu kết nối nội bộ tại máy chủ. Trạng thái cổng này có hiển thị mở (OPEN) đối với các trạm quét từ bên ngoài hay không phụ thuộc trực tiếp vào chính sách kiểm soát gói tin của hệ thống tường lửa trung gian.

Về phương diện kiểm soát truy cập, tường lửa tích hợp Windows Firewall được ghi nhận ở trạng thái kích hoạt trên cả ba hồ sơ mạng gồm Domain, Private và Public. Đồng thời, toàn bộ 16 quy tắc mặc định thuộc nhóm File and Printer Sharing đều bị vô hiệu hóa, ngăn chặn việc mở cổng tự động cho toàn bộ dải mạng. Để phục vụ thực nghiệm an ninh có kiểm soát, một quy tắc tường lửa tùy biến mang tên ATTT Lab SMB 139-445 đã được thiết lập. Quy tắc này cho phép các kết nối đi vào (Inbound Allow) đối với giao thức TCP hướng tới hai cổng đích 139 và 445, song giới hạn phạm vi địa chỉ nguồn từ xa (RemoteAddress) duy nhất tại địa chỉ 192.168.56.10 của trạm Kali Linux. Sự hiện diện của quy tắc này chỉ xác thực việc lưu lượng SMB từ trạm kiểm thử được chấp thuận đi qua tường lửa, mà không cấu thành bằng chứng khẳng định mọi địa chỉ mạng khác đều bị phong tỏa tuyệt đối trên toàn bộ các giao thức.

Hình 3.2 minh chứng các thuộc tính cấu hình của quy tắc tường lửa tùy biến ATTT Lab SMB 139-445 cùng trạng thái các hồ sơ tường lửa trên máy chủ mục tiêu.

![Hình 3.2. Cấu hình Windows Firewall giới hạn nguồn truy cập TCP 139/445 từ trạm Kali Linux](chapter3/presentation/3_1/Hinh_3_2_Firewall.png)

Bằng chứng trực quan từ Hình 3.2 thể hiện chính sách tường lửa đang áp dụng cho cổng 139 và 445. Cấu hình này bảo đảm trạm kiểm thử có thể tương tác với dịch vụ SMB của máy chủ mục tiêu trong các kịch bản khảo sát từ xa, đồng thời loại trừ nguy cơ các thiết bị khác ngoài phân đoạn can thiệp vào quá trình đo đạc.

### 3.1.2. Trạng thái bản vá và mốc phục hồi

Xác định mức độ cập nhật của trình điều khiển nhân srv.sys (Server Driver) là yếu tố quyết định để đánh giá tính chất an ninh của dịch vụ SMB đối với lỗ hổng tràn bộ đệm MS17-010. Trong môi trường Windows, thuộc tính hiển thị FileVersion của tệp thực thi thường là một chuỗi văn bản tĩnh được thiết lập từ thời điểm biên dịch phiên bản phát hành (RTM). Truy vấn tệp srv.sys tại đường dẫn C:\Windows\System32\drivers\srv.sys cho kết quả chuỗi hiển thị là 6.3.9600.16384 (winblue_rtm.130821-1623). Tuy nhiên, chuỗi ký tự hiển thị này không phản ánh chính xác các thay đổi mã nhị phân khi hệ thống được cập nhật qua các gói bảo trì nhỏ.

Để thu được giá trị phiên bản kỹ thuật thực tế, quy trình kiểm tra thực hiện trích xuất và ghép nối bốn trường số nhị phân gồm FileMajorPart, FileMinorPart, FileBuildPart và FilePrivatePart từ tiêu đề tệp driver. Kết quả phép ghép nối xác định phiên bản số thực tế của tệp srv.sys là 6.3.9600.16421. Căn cứ theo thông cáo an ninh MS17-010 [4] và tài liệu hướng dẫn kỹ thuật Article 4023262 của Microsoft [5], ngưỡng phiên bản an toàn tối thiểu của srv.sys đối với nền tảng Windows Server 2012 R2 đã được vá lỗi là 6.3.9600.18604, tương ứng với việc cài đặt gói cập nhật KB4012213 (bản vá bảo mật độc lập) hoặc KB4012216 (bản cập nhật tích lũy tháng). Phép so sánh số học cho thấy giá trị phiên bản số của máy chủ mục tiêu thấp hơn ngưỡng cập nhật an toàn của nhà sản xuất (6.3.9600.16421 < 6.3.9600.18604).

Song song với việc đối chiếu phiên bản tệp driver, danh mục các bản sửa lỗi hệ thống được kiểm kê thông qua lệnh truy vấn Get-HotFix. Kết quả ghi nhận máy chủ chỉ cài đặt đúng 6 bản vá hệ thống (KB2919355, KB2919442, KB2937220, KB2938772, KB2939471 và KB2949621) với ngày cài đặt ghi nhận là 21/03/2014. Trong danh mục cập nhật hiện diện trên hệ thống, hoàn toàn không xuất hiện bản vá KB4012213, KB4012216 hoặc bất kỳ gói cập nhật thay thế nào chứa bản sửa lỗi cho lỗ hổng MS17-010.

Dựa trên sự kết hợp chặt chẽ giữa phiên bản số nhị phân của tệp driver srv.sys thấp hơn ngưỡng khuyến cáo và danh mục bản vá thiếu hụt gói sửa lỗi tương ứng, trạng thái an ninh của máy chủ mục tiêu được phân loại kỹ thuật là UNPATCHED đối với lỗ hổng MS17-010. Kết luận này là một đánh giá nội bộ thuần túy về mặt cấu hình phần mềm trên máy chủ cục bộ. Trạng thái chưa vá cục bộ không đồng nghĩa với việc hệ thống chắc chắn bị khai thác thành công qua mạng, bởi khả năng khai thác thực tế còn phụ thuộc vào đường truyền mạng, việc đàm phán phương ngữ SMB và cấu trúc gói tin tấn công.

Để đảm bảo tính toàn vẹn và khả năng tái lập cho các kịch bản đo đạc kế tiếp, điểm phục hồi mang tên Before Demo đã được tạo lập cho cả hai máy ảo Kali Linux và Windows Server 2012 R2. Điểm chụp trạng thái này được thực hiện khi máy ảo ở trạng thái tắt hoàn toàn (poweroff), đóng vai trò mốc phục hồi chuẩn để hoàn nguyên môi trường về trạng thái đồng nhất sau mỗi kịch bản thực nghiệm.

Bảng 3.2 tổng hợp các tiêu chí đối chiếu phiên bản driver, danh mục bản vá và mốc phục hồi hệ thống trước khi bắt đầu đo đạc.

**Bảng 3.2. Trạng thái bản vá và mốc phục hồi**

| Hạng mục | Giá trị ghi nhận | Ghi chú / căn cứ đối chiếu ngắn |
|---|---|---|
| Chuỗi phiên bản hiển thị tệp `srv.sys` | `FileVersion: 6.3.9600.16384 (winblue_rtm.130821-1623)` | Chuỗi ký tự thuộc tính hiển thị của tệp driver |
| Phiên bản số nhị phân tệp `srv.sys` | `6.3.9600.16421` | Trích xuất từ 4 trường số FileMajor, FileMinor, FileBuild, FilePrivate |
| Ngưỡng phiên bản cập nhật tối thiểu | `6.3.9600.18604` | Căn cứ tài liệu Microsoft Support (Article 4023262) cho Windows Server 2012 R2 |
| Mã bản vá liên quan khắc phục MS17-010 | `KB4012213` (Security Only) hoặc `KB4012216` (Monthly Rollup) | Các gói cập nhật chính thức áp dụng cho Windows Server 2012 R2 |
| Danh mục bản vá hệ thống ghi nhận | 6 bản vá (KB2919355, KB2919442, KB2937220, KB2938772, KB2939471, KB2949621 cài ngày 21/03/2014) | Danh mục ghi nhận không chứa KB4012213, KB4012216 hoặc bản vá thay thế chứa bản sửa lỗi MS17-010 |
| Phân loại trạng thái bản vá cục bộ | **`UNPATCHED`** | Kết luận đối chiếu: phiên bản số nhị phân thấp hơn ngưỡng tối thiểu ($6.3.9600.16421 < 6.3.9600.18604$) và thiếu bản vá tương ứng |
| Mốc khôi phục môi trường (Snapshot) | `Before Demo` | Điểm phục hồi được ghi nhận cho cả hai máy ảo ở trạng thái tắt máy sạch |

Hình 3.3 thể hiện kết quả kiểm tra thuộc tính phiên bản của driver nhân srv.sys kết hợp danh mục các bản vá hệ thống được ghi nhận trên máy chủ Windows Server 2012 R2.

![Hình 3.3. Phiên bản srv.sys và danh mục hotfix ghi nhận trên Windows Server 2012 R2](chapter3/presentation/3_1/Hinh_3_3_SrvSys_Hotfix.png)

Bằng chứng trên Hình 3.3 thể hiện rõ sự khác biệt giữa chuỗi phiên bản hiển thị 6.3.9600.16384 và kết quả tính toán số phiên bản 6.3.9600.16421 qua các trường nhị phân, cùng danh sách 6 bản cập nhật hệ thống từ năm 2014. Sự phân tách này củng cố tính chuẩn xác của phương pháp xác minh kép khi đánh giá mức độ cập nhật của hệ thống mục tiêu.

Sau khi các thông số mạng, dịch vụ chia sẻ tệp, chính sách tường lửa và trạng thái bản vá cục bộ đã được xác lập đầy đủ tại mốc chuẩn xuất phát, hệ thống sẵn sàng cho các bước kiểm thử tiếp theo. Tiểu mục 3.2 sẽ trình bày kết quả rà quét, phát hiện mục tiêu và định danh dịch vụ SMB từ trạm kiểm thử Kali Linux qua môi trường mạng.
