# CHƯƠNG 2. THIẾT KẾ MÔ HÌNH VÀ PHƯƠNG PHÁP THỰC NGHIỆM

Chương 2 thiết lập kiến trúc môi trường lab và phương pháp thực nghiệm khảo sát dịch vụ SMB cùng việc đánh giá an ninh lỗ hổng MS17-010. Nội dung bao gồm hạ tầng mạng cô lập, cấu hình baseline mục tiêu, mô hình năm lớp quan sát độc lập và quy trình thu thập dữ liệu thô. Chương chuẩn hóa hai kịch bản khảo sát, thiết kế kiểm thử vi sai và xác lập khung đánh giá kết quả cho Chương 3.

## 2.1. Thiết kế nghiên cứu và phạm vi thực nghiệm

### 2.1.1. Mục tiêu của mô hình thực nghiệm
Mô hình thực nghiệm thiết lập môi trường an toàn có kiểm soát nhằm khảo sát dịch vụ SMB và đánh giá nhận diện lỗ hổng MS17-010 từ xa. Trọng tâm nghiên cứu là phân định năm lớp quan sát độc lập từ mạng đến bản vá nội bộ. Nghiên cứu không khai thác xâm nhập, chỉ đối chiếu cấu hình máy chủ với phản hồi mạng.

### 2.1.2. Phạm vi và nguyên tắc an toàn
Phạm vi thực nghiệm giới hạn ở giao tiếp mạng của dịch vụ LanmanServer trên Windows Server. Kỹ thuật áp dụng gồm quét TCP SYN, nhận diện phiên bản và kiểm tra logic giao thức phi phá hủy từ Kali Linux theo NIST SP 800-115 [1]. Mô hình loại trừ payload khai thác, không can thiệp bộ nhớ và không gây sập hệ thống. Kiểm thử chỉ thực hiện trong mạng ảo nội bộ, không gửi gói ra Internet.

### 2.1.3. Nguyên tắc cô lập, tái lập và kiểm soát biến
Môi trường lab cách ly ở tầng L2 và L3 qua mạng Host-Only VirtualBox, không bắc cầu, không NAT và không có default route ra Internet. Mỗi kịch bản triển khai trên trạng thái ban đầu đồng nhất. Trong kiểm thử vi sai, hệ thống thiết lập snapshot `Before Demo`. Mọi thay đổi cấu hình đều hoàn nguyên về mốc chuẩn, ngăn ngừa tích lũy trạng thái làm sai lệch phép đo.

## 2.2. Kiến trúc và trạng thái ban đầu của môi trường lab

### 2.2.1. Kiến trúc VirtualBox và mạng Host-Only
Hạ tầng thực nghiệm xây dựng trên VirtualBox 7.2.20 r170876, kết nối qua switch ảo Host-Only `192.168.56.0/24`. Hệ thống tắt DHCP, không gán Default Gateway và không dùng DNS. Mỗi máy ảo ở baseline chỉ gắn một NIC ảo, bảo đảm gói tin truyền trực tiếp qua switch L2, không qua định tuyến hay lọc gói của máy vật lý.

[HÌNH 2.1 — Kiến trúc mô hình mạng Host-Only cô lập trong môi trường thực nghiệm baseline]
- Mục đích: Trực quan hóa kết nối mạng cô lập giữa Kali Linux và Windows Server 2012 R2.
- Thành phần: Switch ảo Host-Only `192.168.56.0/24`, Kali (`192.168.56.10`), Windows (`192.168.56.20`), 1 NIC/VM, không NAT.
- Chú thích: Hình 2.1. Kiến trúc mô hình mạng Host-Only cô lập trong môi trường thực nghiệm baseline.
- Nguồn căn cứ: ENV-CORE-01, ENV-CORE-05, ENV-CORE-06, ENV-CORE-07.

### 2.2.2. Máy kiểm thử Kali Linux
Máy kiểm thử sử dụng Kali Linux 64-bit nhân Kernel 6.12.33-amd64 theo tài liệu Kali Linux [2], cấp phát 2 vCPU và 4096 MB RAM. Giao diện `eth0` gán IP tĩnh `192.168.56.10/24`. Bảng định tuyến chỉ chứa tuyến trực tiếp cho mạng `192.168.56.0/24`, không có default route ra Internet ở trạng thái baseline pre-demo. Công cụ đo đạc gồm Nmap 7.99 cùng kịch bản NSE tại `/usr/share/nmap/scripts/`.

### 2.2.3. Máy mục tiêu Windows Server 2012 R2
Máy mục tiêu cài Windows Server 2012 R2 Standard Evaluation 64-bit Build 9600 (RTM), cấp phát 2 vCPU và 4096 MB RAM, gán IP tĩnh `192.168.56.20/24` cùng phân đoạn L2. Hệ thống vận hành dịch vụ máy chủ tệp LanmanServer (Server Service), cung cấp chia sẻ tệp qua giao thức SMB, giữ nguyên bản trước khi áp dụng chính sách an toàn.

### 2.2.4. Baseline mạng, SMB và Windows Firewall
Ở trạng thái ban đầu, dịch vụ LanmanServer đặt `Automatic` và đang `Running`. Hệ thống mở socket TCP 445 (Direct-hosted SMB) và TCP 139 (NetBIOS over TCP/IP) theo Microsoft [3]. Cả SMBv1 và SMBv2/v3 đều kích hoạt mặc định (`EnableSMB1Protocol = True`, `EnableSMB2Protocol = True`, `FS-SMB1` Installed). Windows Firewall chỉ cho phép TCP 139 và 445 từ `192.168.56.10`, nhóm File and Printer Sharing không mở toàn bộ. Thông số kỹ thuật tổng hợp trong Bảng 2.1.

Bảng 2.1. Thông số kỹ thuật của các nút mạng và dịch vụ trong môi trường thực nghiệm baseline

| Tham số kỹ thuật | Máy kiểm thử (Kali Linux) | Máy mục tiêu (Windows Server) | Ý nghĩa thiết kế |
| :--- | :--- | :--- | :--- |
| **Hệ điều hành** | Kali Linux (Kernel 6.12.33-amd64) | Windows Server 2012 R2 Eval | Chuẩn kiểm thử |
| **Số hiệu bản dựng** | Kali Rolling (Nmap 7.99) | Build 9600 (Trạng thái RTM) | Phiên bản RTM |
| **Địa chỉ IP / Mask** | `192.168.56.10/24` (Gán tĩnh) | `192.168.56.20/24` (Gán tĩnh) | Tách biệt L3 |
| **Giao diện mạng** | 1 Host-Only NIC | 1 Host-Only NIC | Cô lập L2, không NAT/Bridge |
| **Cổng dịch vụ đo** | Cổng nguồn ngẫu nhiên dải cao | TCP 139, TCP 445 lắng nghe | Khảo sát socket |
| **Trạng thái SMB nội bộ** | N/A (Đóng vai trò máy quét) | SMB1=True, SMB2=True | Mặc định hệ điều hành |
| **Chính sách tường lửa** | Không áp dụng lọc gói ra | Cho phép TCP 139/445 từ .10 | Ủy quyền tối thiểu |
| **Tài nguyên cấp phát** | 2 vCPU, 4096 MB RAM | 2 vCPU, 4096 MB RAM | Cân bằng tài nguyên |

### 2.2.5. Baseline bản vá MS17-010 và snapshot
Lệnh `Get-HotFix` xác nhận máy chủ chưa cài bản vá KB4012213 hoặc KB4012216 theo Security Bulletin MS17-010 [4]. Driver `srv.sys` tại `C:\Windows\System32\drivers\srv.sys` có phiên bản số `6.3.9600.16421`, thấp hơn ngưỡng an toàn `6.3.9600.18604` theo Microsoft [5]. Trạng thái bản vá nội bộ là `UNPATCHED`. Sau khi hoàn tất baseline, điểm phục hồi `Before Demo` được tạo trên cả hai máy ảo để hoàn nguyên trạng thái giữa các thử nghiệm vi sai.

## 2.3. Phương pháp thu thập và diễn giải bằng chứng

### 2.3.1. Các lớp quan sát
Mô hình phân tách năm lớp quan sát độc lập nhằm loại trừ suy diễn sai lệch giữa các tầng thông tin. Lớp 1 (Reachability) xác định thông tuyến IP. Lớp 2 (Port & Service Exposure) khảo sát trạng thái cổng TCP 139, 445. Lớp 3 (Protocol Surface & Features) kiểm tra dialect và ký số. Lớp 4 (Remote Vulnerability Signal) ghi nhận phản hồi kịch bản NSE. Lớp 5 (Local Patch State) xác thực bản vá qua driver `srv.sys`. Chi tiết chuẩn hóa trong Bảng 2.2.

Bảng 2.2. Phân loại các lớp quan sát và cơ chế thu thập dữ liệu trong mô hình kiểm thử

| Lớp quan sát | Đối tượng đo đạc | Công cụ / Phương thức | Dữ liệu đầu ra kỳ vọng | Ý nghĩa an toàn thông tin |
| :--- | :--- | :--- | :--- | :--- |
| **1. Reachability** | Khả năng định tuyến L3 | ICMP Echo Request / ARP probe | Phản hồi trực tiếp, RTT | Thông tuyến IP |
| **2. Port & Service** | Cổng TCP 139, TCP 445 | `nmap -sS -sV -p139,445` | Trạng thái cổng, lý do, banner | Bề mặt tiếp xúc |
| **3. Protocol State** | Dialect và cờ tính năng | `smb-protocols`, `smb2-security-mode` | Danh sách dialect, chính sách ký số | Bề mặt giao thức |
| **4. Remote Signal** | Thăm dò dấu hiệu lỗ hổng | `smb-vuln-ms17-010.nse` | Phân loại trạng thái script output | Dấu hiệu từ xa |
| **5. Local Patch State** | Bản cập nhật và driver nhân | `Get-HotFix`, phiên bản `srv.sys` | Mã KB cập nhật, version `srv.sys` | Xác thực nội bộ |

[HÌNH 2.2 — Mô hình năm lớp quan sát và ranh giới suy luận an toàn]
- Mục đích: Trực quan hóa quan hệ phân tầng giữa năm lớp quan sát và ranh giới suy luận an toàn.
- Thành phần: Năm khối lớp quan sát, mũi tên thu thập dữ liệu và các ranh giới suy luận (`445 open != SMBv1`, `SMBv1 != MS17-010`, `UNKNOWN != SAFE`, `FILTERED != PATCHED`).
- Chú thích: Hình 2.2. Mô hình năm lớp quan sát và ranh giới suy luận an toàn.
- Nguồn căn cứ: ENV-CORE-01, ENV-CORE-03, S1-RAW-03, S1-RAW-05, S2-RAW-04.

### 2.3.2. Dữ liệu thô và khả năng truy vết
Mọi phép đo từ Kali Linux được lưu đồng thời dưới ba định dạng chuẩn Nmap (`-oA`): `.nmap`, `.xml` và `.gnmap`. Thứ tự ưu tiên bằng chứng tuân thủ năm cấp độ: dữ liệu thô từ công cụ hoặc trạng thái OS có độ ưu tiên cao nhất, kế tiếp là biên bản thực thi của lượt đo canonical. Các cấp tiếp theo gồm ảnh chụp màn hình kiểm chứng, tài liệu đặc tả giao thức cùng mã nguồn kịch bản, và tài liệu lịch sử tham khảo. Mỗi bằng chứng gắn mã chuẩn (`ENV-CORE-*`, `S1-RAW-*`, `S2-RAW-*`, `B-RAW-*`, `C-RAW-*`) bảo đảm khả năng truy vết minh bạch.

### 2.3.3. Quy tắc xử lý UNKNOWN, NO OUTPUT và FILTERED
Đề tài áp dụng chính sách xử lý kết quả âm tính và bất định với ba trạng thái quan sát:
- Trạng thái `UNKNOWN`: Phép đo đã thực thi nhưng phản hồi không đủ điều kiện kết luận. Nguyên tắc cốt lõi: `UNKNOWN != SAFE`; kết quả không xác định không được suy diễn thành an toàn.
- Hiện tượng `NO OUTPUT / NO USABLE SCRIPT RESULT`: Kịch bản quét kết thúc nhưng không có kết quả trong tệp thô. Phương pháp ghi nhận đây là hiện tượng quan sát thực tế, không tự đoán nguyên nhân chủ quan.
- Trạng thái `FILTERED`: Định nghĩa theo Gordon Lyon [6], cổng bị lọc khi máy quét không nhận phản hồi hoặc nhận lỗi ICMP unreachable. Nguyên tắc cốt lõi: `FILTERED != PATCHED`; cổng bị lọc chỉ phản ánh đường truyền, không chứng minh máy chủ đã vá hay tắt dịch vụ.

### 2.3.4. Ranh giới suy luận
Các ranh giới suy luận ngăn chặn diễn giải vượt quá phạm vi bằng chứng thực nghiệm:
- Cổng TCP 139 hoặc 445 `open` chỉ chứng minh socket phản hồi TCP, không chứng minh dịch vụ bật SMBv1 hay có lỗ hổng.
- Chấp thuận dialect SMBv1 (`NT LM 0.12`) chỉ chứng minh hỗ trợ chuẩn cũ, không khẳng định lỗ hổng MS17-010 khai thác được.
- Tín hiệu thăm dò từ xa `UNKNOWN` không phủ nhận trạng thái `UNPATCHED` của hệ điều hành bên trong.
- Trạng thái `UNPATCHED` nội bộ phản ánh cấu hình hệ thống, không tương đương việc khai thác thực thi mã từ xa thành công nếu thiếu điều kiện kích hoạt.

## 2.4. Thiết kế Kịch bản 1 — Khảo sát dịch vụ SMB

### 2.4.1. Mục tiêu và trình tự thực hiện
Kịch bản 1 khảo sát tuần tự bề mặt dịch vụ SMB theo hướng phi phá hủy. Trình tự gồm tám bước chuẩn hóa: (1) kiểm tra IP và định tuyến Kali; (2) phát hiện nút mạng qua ARP probe; (3) xác nhận máy mục tiêu `192.168.56.20` sẵn sàng; (4) quét SYN cổng TCP 139, 445 (`-sS`); (5) nhận diện phiên bản dịch vụ và OS (`-sV`); (6) thực thi bốn kịch bản NSE an toàn; (7) lưu trữ dữ liệu thô `-oA`; (8) xác lập ranh giới dữ liệu theo từng lớp quan sát.

### 2.4.2. Bộ phép đo và bằng chứng cần thu
Bộ phép đo Kịch bản 1 gồm bốn bước chính. Phép đo B2/B3 xác nhận máy mục tiêu hoạt động tầng L2 (`nmap -sn`). Phép đo B4 quét SYN cổng TCP 139, 445 thu thập cờ `syn-ack` theo Gordon Lyon [6]. Phép đo B5 nhận diện dịch vụ `microsoft-ds` và `netbios-ssn` (`-sV`). Phép đo B6 thu thập dialect SMB theo Paulino Calderon [7], cờ ký số theo Microsoft [8] và năng lực giao thức qua bốn kịch bản NSE an toàn. Chi tiết chuẩn hóa trong Bảng 2.3.

Bảng 2.3. Thiết kế các bước đo và dữ liệu kỳ vọng trong Kịch bản 1 — Khảo sát dịch vụ SMB

| Bước đo | Lệnh thực thi chính | Bằng chứng cần thu | Lớp quan sát | Mục tiêu kỹ thuật |
| :--- | :--- | :--- | :--- | :--- |
| **B2/B3** | `nmap -sn 192.168.56.20` | `b2_host_discovery.*`, `b3_target_alive.*` | Reachability | Kiểm tra kết nối L2 |
| **B4** | `nmap -sS -p139,445 -Pn ... -oA b4_smb_ports` | `b4_smb_ports.nmap/xml` | Port & Service | Trạng thái cổng TCP |
| **B5** | `nmap -sV -p139,445 -Pn ... -oA b5_smb_version` | `b5_smb_version.nmap/xml` | Port & Service | Nhận diện dịch vụ OS |
| **B6** | `nmap -p139,445 --script <safe_nse> ... -oA b6_smb_nse` | `b6_smb_nse.nmap/xml` | Protocol State | Bề mặt SMB và ký số |

### 2.4.3. Điều kiện dừng và giới hạn kết luận
Kịch bản 1 dừng ngay sau khi ghi nhận đầu ra của bốn kịch bản NSE an toàn tại bước B6 và lưu trữ thành công các tệp nhật ký thô, không mở rộng sang khai thác. Kịch bản 1 chỉ phục vụ xác định tính khả dụng kênh truyền và phác họa bề mặt dịch vụ. Kết quả Kịch bản 1 không dùng để tuyên bố máy chủ có hay không có lỗ hổng MS17-010, không kết luận hệ thống an toàn hay dễ tổn thương, và không khẳng định khả năng khai thác. Dữ liệu quan sát chi tiết thuộc nội dung Chương 3.

## 2.5. Thiết kế Kịch bản 2 — Đánh giá cấu hình SMB và MS17-010

### 2.5.1. Bốn phép đo NSE-SMB-01 đến NSE-SMB-04
Kịch bản 2 gồm bốn phép đo tuần tự: NSE-SMB-01 quét SYN cổng TCP 139, 445; NSE-SMB-02 kiểm tra hỗ trợ SMBv1 (`NT LM 0.12`) qua `smb-protocols` [7]; NSE-SMB-03 đánh giá ký số SMB2/SMB3 qua `smb2-security-mode` [8]; NSE-SMB-04 thăm dò MS17-010 qua `smb-vuln-ms17-010` [9]. Kịch bản NSE-SMB-04 kết nối IPC$, gửi `SMB_COM_TRANSACTION` với hàm `PeekNamedPipe` (opcode 0x2300) đến đường ống vô hiệu để quan sát phản hồi lỗi từ nhân OS.

[HÌNH 2.3 — Quy trình thực nghiệm hai kịch bản khảo sát và đánh giá an ninh SMB]
- Mục đích: Trực quan hóa trình tự đo từ Kịch bản 1 đến Kịch bản 2 và ranh giới kết luận tương ứng.
- Thành phần: Các bước B2-B6 của Kịch bản 1, bốn phép đo NSE-SMB-01 đến 04 của Kịch bản 2, lưu trữ dữ liệu thô `-oA` và điểm chặn ranh giới suy luận độc lập với trạng thái bản vá nội bộ.
- Chú thích: Hình 2.3. Quy trình thực nghiệm hai kịch bản khảo sát và đánh giá an ninh SMB.
- Nguồn căn cứ: S1-RAW-01 đến S1-RAW-06, S2-RAW-01 đến S2-RAW-04.

### 2.5.2. Đối chiếu remote signal với trạng thái bản vá nội bộ
Kịch bản 2 đối soát trên hai trục độc lập: tín hiệu từ xa qua máy quét và trạng thái bản vá nội bộ từ máy chủ. Tín hiệu từ xa phản ánh góc nhìn mạng; nếu kịch bản NSE không nhận đủ phản hồi để phân loại, kết quả ghi nhận là `UNKNOWN / NO USABLE SCRIPT RESULT`. Tín hiệu bất định không phủ định trạng thái `UNPATCHED` nội bộ khi đối chiếu số hiệu driver `srv.sys` (`6.3.9600.16421 < 6.3.9600.18604`). Trạng thái unpatched phản ánh khiếm khuyết trong nhân, còn tín hiệu bất định phản ánh giới hạn quan sát từ xa. Dữ liệu quan sát thực tế thuộc nội dung Chương 3.

### 2.5.3. Giới hạn kết luận
Phép đo NSE-SMB-04 là kỹ thuật thăm dò dấu hiệu an ninh dựa trên logic giao thức, không phải quy trình khai thác. Phương pháp cấm chuyển đổi trạng thái kết quả từ `UNKNOWN / NO USABLE SCRIPT RESULT` sang `VULNERABLE`, `SAFE` hay `NOT VULNERABLE` nếu thiếu dữ liệu chứng minh. Phán quyết an ninh cuối cùng phải kết hợp giữa quan sát từ xa và căn cứ bản vá nội bộ, tránh nhận định phiến diện từ công cụ đơn lẻ.

## 2.6. Thiết kế kiểm thử các biện pháp giảm thiểu

### 2.6.1. Nguyên tắc kiểm thử vi sai
Kiểm thử vi sai đo lường tác động của từng giải pháp can thiệp kỹ thuật. Phương pháp đòi hỏi: (1) giữ cố định tham số môi trường cơ sở; (2) chỉ áp dụng duy nhất một biến can thiệp phòng vệ độc lập tại một thời điểm; (3) thực hiện lại chính xác bộ phép đo quy chuẩn. Nhờ snapshot `Before Demo`, môi trường lab luôn phục hồi về baseline sạch trước khi triển khai can thiệp mới, bảo đảm tính độc lập giữa các lần đo.

### 2.6.2. Case B — Vô hiệu hóa SMBv1
Case B thực hiện làm cứng giao thức (Protocol Hardening) ở tầng ứng dụng theo Microsoft [10]. Trên máy chủ Windows Server 2012 R2, lệnh PowerShell `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` chuyển `EnableSMB1Protocol` sang `False`, từ chối kết nối SMBv1. Thao tác chỉ điều chỉnh cấu hình dịch vụ LanmanServer, không gỡ tính năng `FS-SMB1`, và không chỉnh sửa driver `srv.sys`. Tắt SMBv1 không đồng nghĩa hệ thống đã vá (`SMBv1 disabled != PATCHED`). Dịch vụ tiếp tục mở cổng TCP 445 cho SMBv2/v3. Quy trình đo lại gồm phép đo `NSE-SMB-02` (dialect) và `NSE-SMB-04` (MS17-010).

### 2.6.3. Case C — pfSense Transparent Bridge
Case C kiểm soát khả năng tiếp cận mạng bằng tường lửa theo NIST SP 800-41 Rev. 1 [11]. pfSense không thuộc topology baseline ban đầu mà được chèn dưới dạng cầu nối trong suốt (Transparent Bridge) giữa Kali và Windows. Hai giao diện ảo ghép thành bridge interface, lọc gói qua `net.link.bridge.pfil_bridge = 1`, giữ nguyên IP tĩnh Kali (`192.168.56.10/24`) và Windows (`192.168.56.20/24`). Luật chặn có log chặn gói TCP SYN từ `192.168.56.10` đến cổng 139 và 445 của mục tiêu. Tường lửa chỉ tác động đường truyền, không đổi cấu hình nội bộ (SMB1 vẫn `True`) hay trạng thái bản vá (`UNPATCHED`). Cổng bị lọc không đồng nghĩa máy chủ đã vá (`FILTERED != PATCHED`). Quy trình đo lại gồm `NSE-SMB-01`, đối soát log pfSense và `NSE-SMB-04`.

### 2.6.4. Vai trò của cập nhật bản vá
Cập nhật bản vá chính thức (Case A / Patching) là biện pháp duy nhất tác động trực tiếp vào căn nguyên lỗ hổng trong driver nhân `srv.sys` [4], [5]. Bản vá KB4012213 hoặc KB4012216 sửa lỗi tràn bộ đệm trong hàm xử lý thuộc tính OS/2 FEA khi nhân xử lý yêu cầu SMBv1. Nghiên cứu phân định ba tầng phòng thủ độc lập. Cập nhật bản vá loại bỏ điểm yếu trong nhân. Làm cứng giao thức (Case B) vô hiệu hóa tính năng ở tầng ứng dụng, còn kiểm soát mạng (Case C) chặn đường tiếp cận từ bên ngoài. Trong tập dữ liệu thực nghiệm canonical hiện hành, cập nhật bản vá đóng vai trò khung đối chứng lý thuyết và khuyến nghị kỹ thuật; đề tài không trình bày Case A như kịch bản đã thực nghiệm hoàn tất.

### 2.6.5. Ma trận biến can thiệp và phép đo lại
Để chuẩn hóa kiểm thử vi sai, các can thiệp kỹ thuật được tổng hợp trong ma trận thiết kế tại Bảng 2.4, chỉ rõ biến can thiệp độc lập, trạng thái kỳ vọng và bộ phép đo cần thực hiện lại.

Bảng 2.4. Ma trận thiết kế kiểm thử vi sai các biện pháp giảm thiểu

| Kịch bản kiểm thử | Lớp phòng thủ can thiệp | Biến can thiệp kỹ thuật độc lập | Trạng thái máy chủ Windows kỳ vọng | Trạng thái kênh truyền mạng kỳ vọng | Bộ phép đo thực hiện lại |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Baseline** | Không can thiệp | Môi trường xuất phát ban đầu | SMB1=True, srv.sys unpatched | Thông tuyến, 139/445 mở | NSE-SMB-01 đến NSE-SMB-04 |
| **Case B** | Làm cứng giao thức | `EnableSMB1Protocol = $false` | SMB1=False, srv.sys unpatched | Thông tuyến, 445 mở | NSE-SMB-02, NSE-SMB-04 |
| **Case C** | Kiểm soát truy cập mạng | Chèn pfSense Bridge + Block rule 139/445 | SMB1=True, srv.sys unpatched | Lọc 139/445 từ .10 | NSE-SMB-01, log pfSense, NSE-SMB-04 |
| **Case A** *(Đối chứng)* | Cập nhật bản vá | Cài đặt gói cập nhật KB4012213 | SMB1=True, srv.sys >= .18604 | Thông tuyến, 139/445 mở | Đối chứng lý thuyết / Khuyến nghị |

[HÌNH 2.4 — Sơ đồ phương pháp kiểm thử vi sai các biện pháp giảm thiểu]
- Mục đích: Mô tả luồng thực thi kiểm thử vi sai xuất phát từ snapshot Before Demo sang Case B và Case C.
- Thành phần: Mốc `Before Demo`, nhánh Case B (can thiệp PowerShell → đo lại NSE-02/04), nhánh Case C (chèn pfSense Bridge → đo lại NSE-01/log/04), nguyên tắc phục hồi baseline sạch.
- Chú thích: Hình 2.4. Sơ đồ phương pháp kiểm thử vi sai các biện pháp giảm thiểu.
- Nguồn căn cứ: ENV-CORE-02, B-LOCAL-01, B-ACTION-01, B-RAW-01, C-TOPO-01, C-RULE-02, C-RAW-01.

## 2.7. Khung đánh giá kết quả

### 2.7.1. Reachability và service exposure
Tại Lớp 1 (Reachability), tính thông suốt đường truyền dựa trên phản hồi ICMP/ARP, phân loại thành Tiếp cận được (`Reachable`) hoặc Không tiếp cận được (`Unreachable`). Ở Lớp 2 (Service exposure), trạng thái cổng TCP 139 và 445 phân loại thành: `open` (nhận `SYN-ACK`, socket mở); `closed` (nhận `RST-ACK`, cổng đóng); `filtered` (hết thời gian chờ hoặc nhận lỗi ICMP unreachable, có lọc gói). Cổng mở chỉ thể hiện tính tiếp cận dịch vụ, không đại diện cho nguy cơ an ninh nếu chưa kiểm tra các tầng tiếp theo.

### 2.7.2. Protocol surface
Tại Lớp 3 (Protocol surface), việc xem xét bề mặt giao thức tập trung vào hai tiêu chí kỹ thuật. Tiêu chí thứ nhất là danh sách dialect: xác định máy chủ hỗ trợ chuẩn SMBv1 (`NT LM 0.12`) hay chỉ chấp thuận dialect hiện đại (SMB 2.0.2 đến 3.0.2) nhằm đánh giá mức độ thu hẹp bề mặt tấn công. Tiêu chí thứ hai là chính sách ký số SMB: phân loại cơ chế ký thông điệp qua `smb2-security-mode` thành ba mức gồm `disabled`, `enabled but not required`, và `required` để đánh giá khả năng chống tấn công chuyển tiếp.

### 2.7.3. Remote vulnerability signal và local patch state
Tại Lớp 4 (Remote vulnerability signal), kết quả kịch bản `smb-vuln-ms17-010` phân loại thành `VULNERABLE` hoặc `UNKNOWN / NO USABLE SCRIPT RESULT` (`UNKNOWN != SAFE`). Tại Lớp 5 (Local patch state), việc đối soát dựa trên `Get-HotFix` và phiên bản driver `srv.sys` đối chiếu ngưỡng chuẩn `6.3.9600.18604` [5]. Bảng 2.5 chuẩn hóa khung đối chiếu hai chiều giữa quan sát từ xa và trạng thái nội bộ.

Bảng 2.5. Khung đối chiếu hai chiều giữa tín hiệu quan sát từ xa và trạng thái bản vá nội bộ

| Tín hiệu quan sát từ xa (Remote Signal) | Trạng thái bản vá nội bộ (Local Ground Truth) | Điều được phép kết luận | Điều tuyệt đối cấm kết luận |
| :--- | :--- | :--- | :--- |
| **`VULNERABLE`** | **`UNPATCHED`** (`srv.sys` < .18604) | Đồng thuận xác định nguy cơ | Cấm suy diễn khai thác thành công |
| **`UNKNOWN / NO USABLE RESULT`** | **`UNPATCHED`** (`srv.sys` < .18604) | Thăm dò bất định; máy chủ unpatched | Cấm kết luận an toàn (`UNKNOWN != SAFE`) |
| **`UNKNOWN / NO USABLE RESULT`** | **`PATCHED`** (`srv.sys` >= .18604) | Máy chủ patched; quét từ xa âm tính | Cấm suy diễn công cụ chứng minh bản vá |
| **`FILTERED`** *(Đường truyền bị chặn)* | **`UNPATCHED`** (`srv.sys` < .18604) | Kênh truyền bị lọc; thiếu dữ liệu đo | Cấm suy diễn an toàn (`FILTERED != PATCHED`) |
| **`SMBv1 disabled`** *(Case B)* | **`UNPATCHED`** (`srv.sys` < .18604) | Tắt SMBv1; thu hẹp bề mặt từ xa | Cấm suy diễn đã vá (`SMBv1 disabled != PATCHED`) |

### 2.7.4. Hiệu quả và giới hạn của biện pháp giảm thiểu
Hiệu quả của giải pháp can thiệp kỹ thuật được xem xét dựa trên mức độ thu hẹp bề mặt tấn công và tính khả dụng dịch vụ:
- Tắt SMBv1 (Case B): triệt tiêu thương lượng SMBv1 từ xa, loại bỏ nguy cơ từ mã độc nhắm vào SMBv1. Máy trạm dùng SMBv2/v3 duy trì kết nối bình thường trên cổng 445. Giới hạn là phương pháp không sửa mã nhị phân driver `srv.sys` trong nhân; cổng 445 vẫn mở và có thể gián đoạn thiết bị cũ.
- Tường lửa mạng (Case C): ngăn chặn luồng lưu lượng đến cổng 139 và 445 từ IP kiểm soát, che giấu dịch vụ. Giới hạn là tường lửa không đổi cấu hình nội bộ và trạng thái unpatched của máy chủ. Kẻ tấn công từ phân đoạn mạng khác vẫn có thể tiếp cận dịch vụ.

## 2.8. Tổng kết chương

Chương 2 đã xác lập kiến trúc môi trường lab và phương pháp thực nghiệm khảo sát dịch vụ SMB cùng việc đánh giá an ninh lỗ hổng MS17-010. Hạ tầng mạng Host-Only cô lập trên VirtualBox 7.2.20 giữa Kali Linux và Windows Server 2012 R2 bảo đảm an toàn kiểm thử và khả năng tái lập nhờ snapshot `Before Demo`.

Mô hình năm lớp quan sát, cơ chế lưu trữ dữ liệu thô `-oA` và chính sách xử lý kết quả âm tính/bất định (`UNKNOWN != SAFE`, `FILTERED != PATCHED`, `SMBv1 disabled != PATCHED`) thiết lập ranh giới suy luận khoa học. Quy trình hai kịch bản và phương pháp kiểm thử vi sai tạo cơ sở chuẩn xác để Chương 3 tiến hành trình bày dữ liệu đo đạc thực tế.
