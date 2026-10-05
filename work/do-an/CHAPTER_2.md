# CHƯƠNG 2. THIẾT KẾ MÔ HÌNH VÀ PHƯƠNG PHÁP THỰC NGHIỆM

Chương 2 thiết lập kiến trúc lab và phương pháp thực nghiệm khảo sát dịch vụ SMB cùng việc đánh giá an ninh MS17-010. Nội dung gồm hạ tầng mạng cô lập, baseline máy mục tiêu, mô hình năm lớp quan sát độc lập và quy trình thu thập dữ liệu thô. Chương chuẩn hóa hai kịch bản khảo sát, thiết kế kiểm thử vi sai và xác lập khung đánh giá kết quả cho Chương 3.

## 2.1. Thiết kế nghiên cứu và phạm vi thực nghiệm

### 2.1.1. Mục tiêu của mô hình thực nghiệm
Mô hình thực nghiệm thiết lập môi trường kiểm thử an toàn nhằm khảo sát dịch vụ SMB và đánh giá khả năng nhận diện dấu hiệu MS17-010 từ xa. Trọng tâm nghiên cứu là phân định năm lớp quan sát độc lập từ mạng đến bản vá nội bộ. Đề tài không khai thác xâm nhập, chỉ đối chiếu cấu hình máy chủ với phản hồi mạng.

### 2.1.2. Phạm vi và nguyên tắc an toàn
Phạm vi thực nghiệm giới hạn ở giao tiếp mạng dịch vụ LanmanServer trên Windows Server. Kỹ thuật áp dụng gồm quét TCP SYN, nhận diện phiên bản và kiểm tra logic giao thức phi phá hủy từ Kali Linux theo NIST SP 800-115 [1]. Mô hình loại trừ payload khai thác, không can thiệp bộ nhớ, không thực hiện thao tác có chủ đích gây sập hoặc gián đoạn hệ thống. Kiểm thử diễn ra trong mạng nội bộ, không gửi gói ra Internet.

### 2.1.3. Nguyên tắc cô lập, tái lập và kiểm soát biến
Môi trường lab cách ly ở tầng L2 và L3 qua mạng Host-Only VirtualBox, không bắc cầu, không NAT, không default route ra Internet. Mỗi kịch bản bắt đầu từ trạng thái đồng nhất. Trong kiểm thử vi sai, snapshot `Before Demo` trên hai máy ảo cung cấp khả năng tái lập trạng thái, dùng phục hồi baseline trước khi đổi biến can thiệp, tránh tích lũy sai lệch.

## 2.2. Kiến trúc và trạng thái ban đầu của môi trường lab

### 2.2.1. Kiến trúc VirtualBox và mạng Host-Only
Hạ tầng thực nghiệm xây dựng trên VirtualBox 7.2.20 r170876, kết nối qua switch ảo Host-Only `192.168.56.0/24`, tắt DHCP, không gán Default Gateway. Mỗi máy ảo ở baseline chỉ gắn một NIC ảo, hoạt động trong mạng Host-Only, không bắc cầu (Bridged) và không dùng NAT.

[HÌNH 2.1 — Kiến trúc mô hình mạng Host-Only cô lập trong môi trường thực nghiệm baseline]
- Mục đích: Trực quan hóa kết nối mạng cô lập giữa Kali Linux và Windows Server 2012 R2.
- Thành phần: Switch ảo Host-Only `192.168.56.0/24`, Kali (`192.168.56.10`), Windows (`192.168.56.20`), 1 NIC/VM, không NAT.
- Chú thích: Hình 2.1. Kiến trúc mô hình mạng Host-Only cô lập trong môi trường thực nghiệm baseline.
- Nguồn căn cứ: ENV-CORE-01, ENV-CORE-05, ENV-CORE-06, ENV-CORE-07.

### 2.2.2. Máy kiểm thử Kali Linux
Máy kiểm thử dùng Kali Linux 64-bit nhân Kernel 6.12.33-amd64 theo tài liệu Kali Linux [2], cấp phát 2 vCPU và 4096 MB RAM. Giao diện `eth0` gán IP tĩnh `192.168.56.10/24`. Bảng định tuyến chỉ chứa tuyến trực tiếp cho mạng `192.168.56.0/24`, không có default route ra Internet ở baseline pre-demo. Công cụ đo gồm Nmap 7.99 và kịch bản NSE tại `/usr/share/nmap/scripts/`.

### 2.2.3. Máy mục tiêu Windows Server 2012 R2
Máy mục tiêu cài Windows Server 2012 R2 Standard Evaluation 64-bit Build 9600 (RTM), cấp phát 2 vCPU và 4096 MB RAM, gán IP tĩnh `192.168.56.20/24`. Hệ thống vận hành dịch vụ LanmanServer (Server Service), chia sẻ tệp qua SMB, giữ nguyên bản trước khi can thiệp chính sách an toàn.

### 2.2.4. Baseline mạng, SMB và Windows Firewall
Ở trạng thái ban đầu, dịch vụ LanmanServer đặt `Automatic` và đang `Running`. Hệ thống mở socket TCP 445 (Direct-hosted SMB) và TCP 139 (NetBIOS over TCP/IP) theo Microsoft [3]. Cấu hình baseline ghi nhận `EnableSMB1Protocol = True`, `EnableSMB2Protocol = True`, `FS-SMB1` đang cài đặt. Windows Firewall chỉ cho phép TCP 139 và 445 từ `192.168.56.10`, nhóm File and Printer Sharing không mở toàn bộ. Thông số kỹ thuật tổng hợp tại Bảng 2.1.

Bảng 2.1. Thông số kỹ thuật của các nút mạng và dịch vụ trong môi trường thực nghiệm baseline

| Tham số kỹ thuật | Máy kiểm thử (Kali Linux) | Máy mục tiêu (Windows Server) | Ý nghĩa thiết kế |
| :--- | :--- | :--- | :--- |
| **Hệ điều hành** | Kali Linux (Kernel 6.12.33-amd64) | Windows Server 2012 R2 Eval | Chuẩn kiểm thử |
| **Số hiệu bản dựng** | Kali Rolling (Nmap 7.99) | Build 9600 (Trạng thái RTM) | Phiên bản RTM |
| **Địa chỉ IP / Mask** | `192.168.56.10/24` (Gán tĩnh) | `192.168.56.20/24` (Gán tĩnh) | Địa chỉ tĩnh trong cùng mạng lab |
| **Giao diện mạng** | 1 Host-Only NIC | 1 Host-Only NIC | Cô lập L2, không NAT/Bridge |
| **Cổng dịch vụ đo** | Cổng nguồn ngẫu nhiên dải cao | TCP 139, TCP 445 lắng nghe | Khảo sát socket |
| **Trạng thái SMB nội bộ** | N/A (Đóng vai trò máy quét) | SMB1=True, SMB2=True | Trạng thái baseline đã kiểm tra |
| **Chính sách tường lửa** | Không áp dụng lọc gói ra | Cho phép TCP 139/445 từ .10 | Ủy quyền tối thiểu |
| **Tài nguyên cấp phát** | 2 vCPU, 4096 MB RAM | 2 vCPU, 4096 MB RAM | Cân bằng tài nguyên |

### 2.2.5. Baseline bản vá MS17-010 và snapshot
Lệnh `Get-HotFix` xác nhận máy chủ không ghi nhận bản cập nhật KB4012213 hoặc KB4012216 theo MS17-010 [4], đồng thời không ghi nhận bản cập nhật thay thế tương ứng theo mapping. Driver `srv.sys` tại `C:\Windows\System32\drivers\srv.sys` có phiên bản số `6.3.9600.16421`, thấp hơn ngưỡng an toàn `6.3.9600.18604` theo Microsoft [5]. Đối chiếu hai căn cứ xác định trạng thái bản vá nội bộ là `UNPATCHED`. Snapshot `Before Demo` được chuẩn bị trên cả hai máy ảo làm mốc phục hồi chuẩn giữa các thử nghiệm vi sai.

## 2.3. Phương pháp thu thập và diễn giải bằng chứng

### 2.3.1. Các lớp quan sát
Mô hình phân tách năm lớp quan sát độc lập nhằm loại trừ suy diễn sai lệch giữa các tầng. Lớp 1 (Reachability) xác định thông tuyến IP. Lớp 2 (Port & Service) khảo sát cổng TCP 139, 445. Lớp 3 (Protocol State) kiểm tra dialect và ký số. Lớp 4 (Remote Signal) ghi nhận phản hồi kịch bản NSE. Lớp 5 (Local Patch State) xác thực bản vá qua driver srv.sys. Chi tiết chuẩn hóa trong Bảng 2.2.

Bảng 2.2. Phân loại các lớp quan sát và cơ chế thu thập dữ liệu trong mô hình kiểm thử

| Lớp quan sát | Đối tượng đo đạc | Công cụ / Phương thức | Dữ liệu đầu ra kỳ vọng | Ý nghĩa an toàn thông tin |
| :--- | :--- | :--- | :--- | :--- |
| **1. Reachability** | Khả năng hiện diện / tiếp cận trong mạng lab | ICMP Echo Request / ARP probe | Phản hồi trực tiếp, RTT | Thông tuyến IP |
| **2. Port & Service** | Cổng TCP 139, TCP 445 | `nmap -sS -sV -p139,445` | Trạng thái cổng, lý do, banner | Bề mặt dịch vụ |
| **3. Protocol State** | Dialect và cờ tính năng | `smb-protocols`, `smb2-security-mode` | Danh sách dialect, chính sách ký số | Bề mặt giao thức |
| **4. Remote Signal** | Thăm dò dấu hiệu lỗ hổng | `smb-vuln-ms17-010.nse` | Phân loại trạng thái script output | Dấu hiệu từ xa |
| **5. Local Patch State** | Bản cập nhật và driver nhân | `Get-HotFix`, phiên bản `srv.sys` | Mã KB cập nhật, version `srv.sys` | Xác thực nội bộ |

[HÌNH 2.2 — Mô hình năm lớp quan sát và ranh giới suy luận an toàn]
- Mục đích: Trực quan hóa quan hệ phân tầng giữa năm lớp quan sát và ranh giới suy luận an toàn.
- Thành phần: Năm khối lớp quan sát, mũi tên thu thập dữ liệu và các ranh giới suy luận (`445 open != SMBv1`, `SMBv1 != MS17-010`, `UNKNOWN != SAFE`, `FILTERED != PATCHED`).
- Chú thích: Hình 2.2. Mô hình năm lớp quan sát và ranh giới suy luận an toàn.
- Nguồn căn cứ: ENV-CORE-01, ENV-CORE-03, S1-RAW-03, S1-RAW-05, S2-RAW-04.

### 2.3.2. Dữ liệu thô và khả năng truy vết
Phép đo từ Kali Linux được lưu dưới ba định dạng chuẩn (`-oA`): `.nmap`, `.xml` và `.gnmap`. Thứ tự ưu tiên bằng chứng gồm: dữ liệu thô hoặc trạng thái OS cao nhất, kế tiếp là biên bản thực thi lượt đo chính thức, ảnh chụp kiểm chứng, đặc tả giao thức, mã nguồn kịch bản và tài liệu lịch sử. Mỗi bằng chứng gắn mã chuẩn (`ENV-CORE-*`, `S1-RAW-*`, `S2-RAW-*`, `B-RAW-*`, `C-RAW-*`) bảo đảm tính truy vết.

### 2.3.3. Quy tắc xử lý UNKNOWN, NO OUTPUT và FILTERED
Đề tài áp dụng chính sách xử lý kết quả âm tính và bất định:
- Trạng thái `UNKNOWN`: Phép đo thực thi nhưng phản hồi không đủ điều kiện kết luận (`UNKNOWN != SAFE`), cấm suy diễn thành an toàn.
- Hiện tượng `NO OUTPUT / NO USABLE SCRIPT RESULT`: Kịch bản kết thúc nhưng không có kết quả trong tệp thô, ghi nhận hiện tượng quan sát thực tế, không suy đoán chủ quan.
- Trạng thái `FILTERED`: Theo Gordon Lyon [6], cổng bị lọc khi máy quét không nhận phản hồi hoặc nhận lỗi ICMP unreachable (`FILTERED != PATCHED`), chỉ phản ánh đường truyền, không chứng minh máy chủ đã vá hay tắt dịch vụ.

### 2.3.4. Ranh giới suy luận
Các ranh giới suy luận ngăn chặn diễn giải vượt quá phạm vi bằng chứng:
- Cổng TCP 139 hoặc 445 `open` chỉ chứng minh socket phản hồi TCP, không chứng minh dịch vụ bật SMBv1 hay có lỗ hổng.
- Chấp thuận dialect SMBv1 (`NT LM 0.12`) chỉ chứng minh hỗ trợ chuẩn cũ, không khẳng định lỗ hổng MS17-010 khai thác được.
- Tín hiệu từ xa `UNKNOWN` không phủ nhận trạng thái `UNPATCHED` của hệ điều hành nội bộ.
- Trạng thái `UNPATCHED` nội bộ phản ánh cấu hình hệ thống, không tương đương việc khai thác từ xa thành công nếu thiếu điều kiện kích hoạt.

## 2.4. Thiết kế Kịch bản 1 — Khảo sát dịch vụ SMB

### 2.4.1. Mục tiêu và trình tự thực hiện
Kịch bản 1 khảo sát tuần tự bề mặt dịch vụ SMB phi phá hủy qua tám bước: (1) kiểm tra IP và định tuyến Kali; (2) quét phát hiện máy trạm trong dải `192.168.56.0/24`; (3) xác nhận riêng máy mục tiêu `192.168.56.20` hoạt động; (4) quét SYN cổng TCP 139, 445 (`-sS`); (5) nhận diện dịch vụ và phiên bản (`-sV`); (6) thực thi bốn kịch bản NSE an toàn; (7) lưu dữ liệu thô `-oA`; (8) xác lập ranh giới dữ liệu theo từng lớp quan sát.

### 2.4.2. Bộ phép đo và bằng chứng cần thu
Bộ phép đo Kịch bản 1 gồm các bước kỹ thuật chuẩn hóa. Phép đo B2 phát hiện host trong dải `192.168.56.0/24` (`S1-RAW-01`). Phép đo B3 xác nhận riêng máy mục tiêu `192.168.56.20` hoạt động (`S1-RAW-02`). Phép đo B4 quét SYN cổng TCP 139, 445 thu thập trạng thái cổng và lý do phân loại theo Gordon Lyon [6]. Phép đo B5 nhận diện dịch vụ và phiên bản (`-sV`), đối soát thông tin OS từ baseline nội bộ. Phép đo B6 thu thập dialect SMB theo Paulino Calderon [7], ký số theo Microsoft [8] và năng lực giao thức qua bốn kịch bản NSE an toàn (`smb-protocols`, `smb-os-discovery`, `smb2-security-mode`, `smb2-capabilities`). Chi tiết chuẩn hóa trong Bảng 2.3.

Bảng 2.3. Thiết kế các bước đo và dữ liệu kỳ vọng trong Kịch bản 1 — Khảo sát dịch vụ SMB

| Bước đo | Lệnh thực thi chính | Bằng chứng cần thu | Lớp quan sát | Mục tiêu kỹ thuật |
| :--- | :--- | :--- | :--- | :--- |
| **B2** | `nmap -sn 192.168.56.0/24` | `b2_host_discovery.*` (S1-RAW-01) | Reachability | Phát hiện máy trạm trong mạng lab |
| **B3** | `nmap -sn 192.168.56.20` | `b3_target_alive.*` (S1-RAW-02) | Reachability | Xác nhận riêng máy mục tiêu hoạt động |
| **B4** | `nmap -sS -p139,445 -Pn ... -oA b4_smb_ports` | `b4_smb_ports.nmap/xml` (S1-RAW-03) | Port & Service | Trạng thái cổng TCP và lý do phân loại |
| **B5** | `nmap -sV -p139,445 -Pn ... -oA b5_smb_version` | `b5_smb_version.nmap/xml` (S1-RAW-04) | Port & Service | Nhận diện dịch vụ / phiên bản |
| **B6** | `nmap -p139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities ... -oA b6_smb_nse` | `b6_smb_nse.nmap/xml` (S1-RAW-05) | Protocol State | Bề mặt SMB và ký số |

### 2.4.3. Điều kiện dừng và giới hạn kết luận
Kịch bản 1 dừng ngay sau khi ghi nhận đầu ra bốn kịch bản NSE an toàn tại bước B6 và lưu tệp nhật ký thô, không mở rộng sang khai thác. Kịch bản 1 chỉ xác định tính khả dụng kênh truyền và phác họa bề mặt dịch vụ. Kết quả không dùng tuyên bố máy chủ có MS17-010, không kết luận an toàn hay dễ tổn thương, không khẳng định khả năng khai thác. Dữ liệu chi tiết thuộc Chương 3.

## 2.5. Thiết kế Kịch bản 2 — Đánh giá cấu hình SMB và MS17-010

### 2.5.1. Bốn phép đo NSE-SMB-01 đến NSE-SMB-04
Kịch bản 2 gồm bốn phép đo tuần tự: NSE-SMB-01 quét SYN cổng TCP 139, 445; NSE-SMB-02 kiểm tra hỗ trợ SMBv1 (`NT LM 0.12`) qua `smb-protocols` [7]; NSE-SMB-03 đánh giá ký số SMB2/SMB3 qua `smb2-security-mode` [8]; NSE-SMB-04 thăm dò an ninh MS17-010. Trong đó, NSE-SMB-04 sử dụng `smb-vuln-ms17-010` để kết nối `IPC$`, thực hiện một giao dịch SMB trên FID 0 và phân tích mã trạng thái phản hồi nhằm tìm dấu hiệu liên quan đến MS17-010 [9].

[HÌNH 2.3 — Quy trình thực nghiệm hai kịch bản khảo sát và đánh giá an ninh SMB]
- Mục đích: Trực quan hóa trình tự đo từ Kịch bản 1 đến Kịch bản 2 và ranh giới kết luận tương ứng.
- Thành phần: Các bước B2-B6 của Kịch bản 1, bốn phép đo NSE-SMB-01 đến 04 của Kịch bản 2, lưu trữ dữ liệu thô `-oA` và điểm chặn ranh giới suy luận độc lập với trạng thái bản vá nội bộ.
- Chú thích: Hình 2.3. Quy trình thực nghiệm hai kịch bản khảo sát và đánh giá an ninh SMB.
- Nguồn căn cứ: S1-RAW-01 đến S1-RAW-05, S1-META-01, S2-RAW-01 đến S2-RAW-04.

### 2.5.2. Đối chiếu remote signal với trạng thái bản vá nội bộ
Kịch bản 2 đối soát trên hai trục độc lập: tín hiệu từ xa qua máy quét và trạng thái bản vá nội bộ từ máy chủ. Tín hiệu từ xa phản ánh góc nhìn mạng; nếu script không cung cấp verdict usable, kết quả được phân loại `UNKNOWN / NO USABLE SCRIPT RESULT`. Tín hiệu bất định không phủ định trạng thái `UNPATCHED` nội bộ khi đối chiếu số hiệu driver `srv.sys` (`6.3.9600.16421 < 6.3.9600.18604`). Trạng thái `UNPATCHED` cho biết hệ thống chưa đạt mức cập nhật được Microsoft xác minh cho MS17-010; trạng thái này không tự chứng minh khai thác thành công, trong khi tín hiệu bất định phản ánh giới hạn quan sát từ xa. Dữ liệu thực nghiệm chi tiết thuộc Chương 3.

### 2.5.3. Giới hạn kết luận
Phép đo NSE-SMB-04 là kỹ thuật thăm dò dựa trên logic giao thức, không phải quy trình khai thác. Phương pháp cấm chuyển trạng thái từ `UNKNOWN / NO USABLE SCRIPT RESULT` sang `VULNERABLE`, `SAFE` hay `NOT VULNERABLE` nếu thiếu chứng cứ. Phán quyết an ninh phải kết hợp quan sát từ xa và bản vá nội bộ, tránh nhận định phiến diện từ công cụ đơn lẻ.

## 2.6. Thiết kế kiểm thử các biện pháp giảm thiểu

### 2.6.1. Nguyên tắc kiểm thử vi sai
Kiểm thử vi sai đo lường tác động của từng giải pháp can thiệp kỹ thuật theo nguyên tắc: (1) giữ cố định tham số môi trường cơ sở; (2) chỉ áp dụng một biến can thiệp độc lập tại một thời điểm; (3) thực hiện lại chính xác bộ phép đo quy chuẩn. Quy trình yêu cầu sử dụng mốc snapshot `Before Demo` để phục hồi môi trường lab về baseline sạch trước khi triển khai can thiệp mới, bảo đảm tính độc lập giữa các lần đo.

### 2.6.2. Case B — Vô hiệu hóa SMBv1
Case B thực hiện làm cứng giao thức (Protocol Hardening) ở tầng ứng dụng theo Microsoft [10]. Trên máy chủ Windows, lệnh PowerShell `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` chuyển `EnableSMB1Protocol` sang `False`, từ chối kết nối SMBv1. Thao tác chỉ thay đổi cấu hình SMB Server, không gỡ tính năng `FS-SMB1` và không thay đổi driver `srv.sys` (`SMBv1 disabled != PATCHED`). Quy trình đo lại nhằm kiểm tra dialect SMBv1 còn xuất hiện hay không qua `NSE-SMB-02`, khảo sát bề mặt dịch vụ SMBv2/v3 trên cổng TCP 445 và ghi nhận tín hiệu thăm dò qua `NSE-SMB-04`.

### 2.6.3. Case C — pfSense Transparent Bridge
Case C kiểm soát tiếp cận mạng bằng tường lửa theo NIST SP 800-41 Rev. 1 [11]. pfSense không thuộc topology baseline ban đầu mà được chèn làm cầu nối trong suốt (Transparent Bridge) giữa Kali và Windows. Hai giao diện ảo ghép thành bridge interface, lọc gói trên member interface theo cấu hình chuẩn `net.link.bridge.pfil_member = 1`, `net.link.bridge.pfil_bridge = 0` và `net.link.bridge.pfil_onlyip = 1`, giữ nguyên IP tĩnh Kali (`192.168.56.10/24`) và Windows (`192.168.56.20/24`). Luật chặn TCP có bật ghi log, áp dụng từ `192.168.56.10` tới `192.168.56.20` trên các cổng 139 và 445. Tường lửa chỉ tác động đường truyền, không đổi cấu hình nội bộ (SMB1 vẫn `True`) hay trạng thái bản vá (`UNPATCHED`). Cổng bị lọc không đồng nghĩa máy chủ đã vá (`FILTERED != PATCHED`). Quy trình đo lại gồm `NSE-SMB-01`, đối soát log pfSense và `NSE-SMB-04`.

### 2.6.4. Vai trò của cập nhật bản vá
Patching là biện pháp trực tiếp thay đổi trạng thái bản vá của thành phần SMB bị ảnh hưởng bởi MS17-010 trong driver nhân `srv.sys` [4], [5]. Bản vá nâng phiên bản nhị phân driver vượt ngưỡng an toàn. Nghiên cứu phân định ba tầng phòng thủ độc lập: cập nhật bản vá khắc phục căn nguyên lỗ hổng trong nhân; làm cứng giao thức (Case B) vô hiệu hóa tính năng ở tầng ứng dụng; kiểm soát mạng (Case C) chặn đường tiếp cận từ bên ngoài. Trong bộ dữ liệu thực nghiệm hiện hành, bản vá đóng vai trò khung đối chứng lý thuyết và khuyến nghị kỹ thuật; đề tài không trình bày Case A như kịch bản đã thực nghiệm hoàn tất.

### 2.6.5. Ma trận biến can thiệp và phép đo lại
Để chuẩn hóa kiểm thử vi sai, các can thiệp kỹ thuật được tổng hợp trong ma trận thiết kế tại Bảng 2.4, chỉ rõ biến can thiệp độc lập, trạng thái kỳ vọng và bộ phép đo cần thực hiện lại.

Bảng 2.4. Ma trận thiết kế kiểm thử vi sai các biện pháp giảm thiểu

| Kịch bản kiểm thử | Lớp phòng thủ can thiệp | Biến can thiệp kỹ thuật độc lập | Trạng thái máy chủ Windows kỳ vọng | Trạng thái kênh truyền mạng kỳ vọng | Bộ phép đo thực hiện lại |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Baseline** | Không can thiệp | Môi trường xuất phát ban đầu | SMB1=True, srv.sys unpatched | Thông tuyến, 139/445 mở | NSE-SMB-01 đến NSE-SMB-04 |
| **Case B** | Làm cứng giao thức | `EnableSMB1Protocol = $false` | SMB1=False, srv.sys unpatched | Thông tuyến, 445 mở | NSE-SMB-02, NSE-SMB-04 |
| **Case C** | Kiểm soát truy cập mạng | Chèn pfSense Bridge + Block rule 139/445 | SMB1=True, srv.sys unpatched | Lọc 139/445 từ .10 | NSE-SMB-01, log pfSense, NSE-SMB-04 |
| **Case A** *(Đối chứng)* | Cập nhật bản vá | Bản cập nhật MS17-010 áp dụng | Không đo đạc (Đối chứng) | Không đo đạc (Đối chứng) | Đối chứng lý thuyết / Khuyến nghị |

[HÌNH 2.4 — Sơ đồ phương pháp kiểm thử vi sai các biện pháp giảm thiểu]
- Mục đích: Mô tả luồng thực thi kiểm thử vi sai xuất phát từ snapshot Before Demo sang Case B và Case C.
- Thành phần: Mốc `Before Demo`, nhánh Case B (can thiệp PowerShell → đo lại NSE-02/04), nhánh Case C (chèn pfSense Bridge → đo lại NSE-01/log/04), nguyên tắc phục hồi baseline sạch.
- Chú thích: Hình 2.4. Sơ đồ phương pháp kiểm thử vi sai các biện pháp giảm thiểu.
- Nguồn căn cứ: ENV-CORE-02, B-LOCAL-01, B-ACTION-01, B-RAW-01, C-TOPO-01, C-RULE-02, C-RAW-01.

## 2.7. Khung đánh giá kết quả

### 2.7.1. Reachability và service exposure
Tại Lớp 1 (Reachability), tính thông suốt đường truyền dựa trên phản hồi ICMP/ARP, phân loại thành: có phản hồi trong phép tiền kiểm hoặc không ghi nhận phản hồi trong phép tiền kiểm. Ở Lớp 2 (Service exposure), trạng thái cổng TCP 139 và 445 phân loại thành: `open` (nhận `SYN-ACK`, socket mở); `closed` (nhận phản hồi RST, cổng đóng); `filtered` (Nmap không thể xác định cổng open hay closed do filtering hoặc không nhận đủ phản hồi theo cơ chế phân loại của công cụ). Cổng mở chỉ thể hiện tính tiếp cận dịch vụ, không đại diện cho nguy cơ nếu chưa kiểm tra các tầng tiếp theo.

### 2.7.2. Protocol surface
Tại Lớp 3 (Protocol surface), bề mặt giao thức được xem xét theo hai tiêu chí. Tiêu chí thứ nhất là danh sách dialect: xác định máy chủ hỗ trợ SMBv1 (`NT LM 0.12`) hay chỉ chấp thuận các dialect SMB2/SMB3 nhằm đánh giá mức độ thu hẹp bề mặt tấn công. Tiêu chí thứ hai là chính sách ký số SMB: phân loại cơ chế ký qua `smb2-security-mode` thành ba mức `disabled`, `enabled but not required`, và `required` nhằm đánh giá chính sách ký số SMB và mức độ bắt buộc ký.

### 2.7.3. Remote vulnerability signal và local patch state
Tại Lớp 4 (Remote vulnerability signal), kết quả kịch bản `smb-vuln-ms17-010` phân loại thành `VULNERABLE` hoặc `UNKNOWN / NO USABLE SCRIPT RESULT` (`UNKNOWN != SAFE`). Tại Lớp 5 (Local patch state), việc đối soát dựa trên `Get-HotFix` và phiên bản driver `srv.sys` đối chiếu ngưỡng chuẩn `6.3.9600.18604` [5]. Bảng 2.5 chuẩn hóa khung đối chiếu hai chiều giữa quan sát từ xa và trạng thái nội bộ.

Bảng 2.5. Khung đối chiếu hai chiều giữa tín hiệu quan sát từ xa và trạng thái bản vá nội bộ

| Tín hiệu quan sát từ xa (Remote Signal) | Trạng thái bản vá nội bộ (Local Ground Truth) | Điều được phép kết luận | Điều tuyệt đối cấm kết luận |
| :--- | :--- | :--- | :--- |
| **`VULNERABLE`** | **`UNPATCHED`** (`srv.sys` < .18604) | Đồng thuận xác định nguy cơ | Cấm suy diễn khai thác thành công |
| **`UNKNOWN / NO USABLE RESULT`** | **`UNPATCHED`** (`srv.sys` < .18604) | Thăm dò bất định; máy chủ unpatched | Cấm kết luận an toàn (`UNKNOWN != SAFE`) |
| **`UNKNOWN / NO USABLE RESULT`** | **`PATCHED`** (`srv.sys` >= .18604) | Máy chủ patched; quét từ xa âm tính | Cấm suy diễn công cụ chứng minh bản vá |
| **`FILTERED`** *(Không đủ phản hồi phân loại)* | **`UNPATCHED`** (`srv.sys` < .18604) | Kênh truyền bị lọc hoặc thiếu phản hồi; không đủ dữ liệu đo | Cấm suy diễn an toàn (`FILTERED != PATCHED`) |
| **`SMBv1 disabled`** *(Case B)* | **`UNPATCHED`** (`srv.sys` < .18604) | Tắt SMBv1; thu hẹp bề mặt từ xa | Cấm suy diễn đã vá (`SMBv1 disabled != PATCHED`) |

### 2.7.4. Hiệu quả và giới hạn của biện pháp giảm thiểu
Hiệu quả của giải pháp can thiệp kỹ thuật được đánh giá qua mức độ thu hẹp bề mặt tấn công và tác động khả dụng:
- Tắt SMBv1 (Case B): tiêu chí đánh giá là phiên thương lượng đã đo không còn xuất hiện dialect SMBv1 từ xa, đồng thời kiểm tra các dialect SMB2/SMB3 còn khả dụng trong phép thương lượng sau can thiệp hay không. Giới hạn là phương pháp không sửa mã nhị phân driver `srv.sys` trong nhân; việc vô hiệu hóa SMBv1 không đồng nghĩa đóng TCP 445; phép retest cần kiểm tra khả năng tiếp cận SMB2/SMB3 sau can thiệp, và việc hỗ trợ SMB2/SMB3 không suy diễn rằng mọi hệ thống nghiệp vụ cũ đều tương thích.
- Tường lửa mạng (Case C): tiêu chí đánh giá là mức giảm thiểu bề mặt tấn công trên cổng TCP 139 và 445 từ địa chỉ nguồn và đường truyền được chính sách kiểm soát. Giới hạn là tường lửa không thay đổi cấu hình nội bộ và trạng thái unpatched của máy chủ, không áp dụng cho các luồng mạng ngoài phạm vi chính sách.

## 2.8. Tổng kết chương

Chương 2 đã xác lập kiến trúc môi trường lab và phương pháp thực nghiệm khảo sát dịch vụ SMB cùng đánh giá an ninh MS17-010. Hạ tầng mạng Host-Only giới hạn phạm vi kết nối và hỗ trợ kiểm soát rủi ro thử nghiệm, duy trì khả năng tái lập nhờ snapshot `Before Demo` trên VirtualBox 7.2.20.

Mô hình năm lớp quan sát, cơ chế lưu trữ dữ liệu thô `-oA` và chính sách xử lý kết quả âm tính/bất định thiết lập ranh giới suy luận khoa học. Quy trình hai kịch bản và phương pháp kiểm thử vi sai làm cơ sở để Chương 3 trình bày dữ liệu đo đạc thực tế.