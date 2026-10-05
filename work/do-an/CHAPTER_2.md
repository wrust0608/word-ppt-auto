# CHƯƠNG 2. THIẾT KẾ VÀ TRIỂN KHAI MÔ HÌNH THỰC NGHIỆM

Chương 2 trình bày thiết kế kiến trúc môi trường lab và quy trình kiểm thử dịch vụ SMB cùng lỗ hổng MS17-010. Trọng tâm của chương là mô hình thực nghiệm an toàn, tái lập, lưu trữ bằng chứng nguyên bản và phân định năm lớp quan sát từ kết nối mạng đến bản vá nội bộ.

## 2.1. Yêu cầu và nguyên tắc thiết kế

### 2.1.1. Mục tiêu của môi trường thực nghiệm
Môi trường thực nghiệm được thiết kế nhằm khảo sát dịch vụ SMB và đánh giá trạng thái an ninh của lỗ hổng MS17-010 trong điều kiện kiểm soát chặt chẽ. Trọng tâm của mô hình là phân định rõ ràng giữa các lớp quan sát từ xa và sự thật bản vá nội bộ, tạo cơ sở thực chứng để đánh giá hiệu lực của các biện pháp giảm thiểu.

### 2.1.2. Phạm vi, nguyên tắc an toàn và giới hạn đạo đức
Phạm vi thực nghiệm tuân thủ nghiêm ngặt các nguyên tắc kiểm thử an ninh theo hướng dẫn NIST SP 800-115 [1]. Nghiên cứu chỉ áp dụng các kỹ thuật quét cổng, trinh sát dịch vụ và thăm dò logic không phá hủy. Quy trình nghiêm cấm phát tán mã khai thác vũ khí hóa, không thực hiện tấn công chiếm quyền điều khiển và không gây nghẽn dịch vụ mạng.

### 2.1.3. Nguyên tắc cô lập mạng và khả năng khôi phục
Thực nghiệm đòi hỏi cô lập nghiêm ngặt nhằm ngăn ngừa mất ổn định dịch vụ và phát tán gói tin ra hạ tầng dùng chung. Môi trường lab được tách rời hoàn toàn khỏi mạng nội bộ và Internet. Hệ thống áp dụng cơ chế chụp ảnh trạng thái `Before Demo` trước khi phát lệnh đo. Sau mỗi kịch bản can thiệp, máy ảo được hoàn nguyên về mốc ban đầu để loại bỏ sai số lũy tích.

### 2.1.4. Nguyên tắc thu thập, truy vết và bảo toàn bằng chứng
Tính truy vết yêu cầu mọi kết luận đều đối chiếu được với dữ liệu gốc ghi nhận tại thời điểm phát lệnh. Quy trình chuẩn hóa việc lưu trữ raw text log cho tất cả lệnh Nmap và PowerShell. Mỗi tệp dữ liệu được gán mã Stable Evidence ID chuẩn hóa từ sổ đăng ký bằng chứng, ghi rõ thời gian đo và tham số thực thi.

## 2.2. Kiến trúc môi trường thực nghiệm

### 2.2.1. Nền tảng Oracle VirtualBox
Nền tảng Oracle VM VirtualBox 7.2.20 r170876 được lựa chọn làm hạ tầng thực thi cho toàn bộ mô hình lab. Cơ chế mạng Host-Only Adapter liên kết các máy ảo qua switch ảo nội bộ, không bắc cầu ra card mạng vật lý của máy chủ.

Kiến trúc kết nối mạng giữa các thành phần thực nghiệm được mô tả trong Hình 2.1.

```
+-------------------------------------------------------------------------+
|                  NỀN TẢNG ẢO HÓA ORACLE VM VIRTUALBOX                   |
|                                                                         |
|  +-----------------------+                   +-----------------------+  |
|  |     MÁY KIỂM THỬ      |                   |      MÁY MỤC TIÊU     |  |
|  |      KALI LINUX       |                   | WINDOWS SERVER 2012R2 |  |
|  |  (Kernel 6.12.33)     |                   |     (Build 9600)      |  |
|  |  IP: 192.168.56.10/24 |                   |  IP: 192.168.56.20/24 |  |
|  +-----------+-----------+                   +-----------+-----------+  |
|              |                                           |              |
|              +========== MẠNG HOST-ONLY: 192.168.56.0/24 ============+  |
|                                                                         |
|  [Ranh giới kỹ thuật: Không Default Gateway | Không DHCP | Không NAT]   |
+-------------------------------------------------------------------------+
```
*Hình 2.1. Kiến trúc mô hình mạng Host-Only cô lập trong môi trường thực nghiệm*

### 2.2.2. Máy kiểm thử Kali Linux
Máy kiểm thử sử dụng bản phân phối Kali Linux 64-bit (nhân Linux Kernel 6.12.33-amd64) theo tài liệu chuẩn của dự án Kali Linux [2], phục vụ đánh giá an ninh mạng chuyên nghiệp. Máy ảo được cấu hình 2 vCPU và 4096 MB RAM, gán địa chỉ IP tĩnh `192.168.56.10/24`. Bộ công cụ Nmap cùng thư viện NSE được cài đặt sẵn để thực thi các kịch bản kiểm tra dịch vụ SMB.

### 2.2.3. Máy mục tiêu Windows Server 2012 R2
Máy mục tiêu là đối tượng đánh giá, cài đặt Windows Server 2012 R2 Standard Evaluation 64-bit (Build 9600), cấu hình 2 vCPU và 4096 MB RAM, gán địa chỉ IP tĩnh `192.168.56.20/24`. Dịch vụ chia sẻ tệp LanmanServer mở socket lắng nghe trên cổng TCP 445 cho Direct-hosted SMB và TCP 139 cho NetBIOS over TCP/IP theo tài liệu kỹ thuật của Microsoft [3].

### 2.2.4. Mạng Host-Only và bảng địa chỉ IP
Mạng Host-Only sử dụng dải địa chỉ IPv4 `192.168.56.0/24`, tắt dịch vụ DHCP và không cấu hình Default Gateway hay DNS. Thông số chi tiết của các nút mạng và phân bổ tài nguyên phần cứng được tổng hợp trong Bảng 2.1.

*Bảng 2.1. Thông số kỹ thuật của các nút mạng trong môi trường thực nghiệm*

| Tham số cấu hình | Máy kiểm thử (Kali Linux) | Máy mục tiêu (Windows Server) | Ghi chú kỹ thuật |
| :--- | :--- | :--- | :--- |
| **Hệ điều hành** | Kali Linux (Kernel 6.12.33) | Windows Server 2012 R2 Eval | Nền tảng 64-bit chuẩn hóa |
| **Số hiệu bản dựng** | Kali Rolling (Nmap 7.99) | Build 9600 (Trạng thái RTM) | Xác định mã định danh OS |
| **Địa chỉ IP / Mask**| `192.168.56.10 / 24` | `192.168.56.20 / 24` | Gán tĩnh, tắt DHCP |
| **Cổng đo đạc** | Dải cổng cao ngẫu nhiên | TCP 139, TCP 445 | LanmanServer lắng nghe |
| **Mạng ảo hóa** | Host-Only Adapter | Host-Only Adapter | Không Gateway, cô lập |
| **Tài nguyên** | 2 vCPU, 4096 MB RAM | 2 vCPU, 4096 MB RAM | Đủ tài nguyên đo đạc |

### 2.2.5. Kiểm tra kết nối trong phạm vi lab
Trước khi đo đạc bảo mật, quy trình kiểm tra kết nối hai chiều bằng ICMP Echo Request (`ping`) giữa `192.168.56.10` và `192.168.56.20`. Kết quả xác nhận độ trễ truyền gói tin dưới 1 ms và tỷ lệ mất gói bằng 0%, bảo đảm kênh truyền vật lý đạt độ tin cậy.

## 2.3. Chuẩn bị trạng thái baseline

### 2.3.1. Trạng thái hệ điều hành và dịch vụ SMB
Đường cơ sở phản ánh cấu hình dịch vụ nguyên bản. Dịch vụ LanmanServer đặt ở chế độ tự động chạy (`Running`), mở socket lắng nghe trên hệ thống.

### 2.3.2. Trạng thái SMBv1/SMB2 và TCP 139/445
Trên Windows Server 2012 R2 mặc định, cả SMBv1 và SMBv2/SMB3 đều bật để tương thích ngược. Lệnh `Get-SmbServerConfiguration` xác nhận hai giao thức hoạt động, mở cổng TCP 139 và 445.

### 2.3.3. Cấu hình Windows Firewall phục vụ phép đo
Chính sách Windows Firewall được điều chỉnh có kiểm soát để đo đạc chuẩn xác. Nhóm kích hoạt luật `File and Printer Sharing (SMB-In)` cho địa chỉ `192.168.56.10`, bảo đảm phản hồi phản ánh đúng logic dịch vụ.

### 2.3.4. Xác định trạng thái bản vá MS17-010 và srv.sys
Trạng thái bản vá được kiểm tra trực tiếp trên máy mục tiêu. Lệnh `Get-HotFix` xác nhận chưa cài đặt bản vá KB4012213 hoặc KB4012216. Tệp trình điều khiển `srv.sys` tại đường dẫn hệ thống ghi nhận phiên bản `6.3.9600.16421`, thấp hơn ngưỡng an toàn `6.3.9600.18604` theo khuyến cáo trong bản tin bảo mật MS17-010 của Microsoft [4], xác lập sự thật mặt đất nội bộ là `UNPATCHED`.

### 2.3.5. Kiểm tra Nmap và NSE script trên Kali
Tại máy kiểm thử Kali Linux, lệnh `nmap --version` xác nhận phiên bản Nmap đang hoạt động theo chuẩn phát hành công cụ quét mạng của Gordon Lyon [5]. Thư mục `/usr/share/nmap/scripts/` chứa đầy đủ các kịch bản: `smb-protocols.nse`, `smb-security-mode.nse`, `smb2-security-mode.nse` và `smb-vuln-ms17-010.nse`.

### 2.3.6. Snapshot Before Demo và phương án phục hồi
Sau khi chuẩn hóa baseline, snapshot `Before Demo` được tạo trên máy ảo mục tiêu. Sau mỗi kịch bản can thiệp, hệ thống hoàn nguyên về mốc này để bảo đảm tính độc lập giữa các lượt đo.

## 2.4. Phương pháp kiểm thử và mô hình bằng chứng

### 2.4.1. Các lớp quan sát: reachability, service, protocol, remote signal, local ground truth
Quy trình thực nghiệm xây dựng mô hình quan sát phân tách năm lớp nhằm tránh nhầm lẫn giữa các cấp độ thông tin mạng, tạo thành chuỗi suy luận logic có kiểm soát. Cấu trúc phân loại năm lớp quan sát và phương thức thu thập bằng chứng được chuẩn hóa trong Bảng 2.2.

*Bảng 2.2. Phân loại các lớp quan sát và cơ chế thu thập dữ liệu trong mô hình kiểm thử*

| Lớp quan sát | Đối tượng đo đạc | Công cụ thực hiện | Dữ liệu đầu ra kỳ vọng | Ý nghĩa an toàn |
| :--- | :--- | :--- | :--- | :--- |
| **1. Reachability** | Kết nối tầng mạng IP | `ping` (ICMP Echo) | Round-trip time, packet loss | Xác nhận thông tuyến |
| **2. Port & Service**| Cổng TCP 139, 445 | `nmap -sS -p139,445` | `open`, `closed`, `filtered` | Xác định bề mặt dịch vụ |
| **3. Protocol State** | Phương ngữ và ký số SMB | `smb-protocols`, `smb*-mode` | Danh sách dialects, Signing | Tính năng giao thức bật |
| **4. Remote Signal** | Thăm dò lỗ hổng từ xa | `smb-vuln-ms17-010.nse` | `VULNERABLE`, `UNKNOWN` | Tín hiệu suy diễn từ xa |
| **5. Ground Truth** | Bản vá và mã tệp nội bộ | `Get-HotFix`, `srv.sys` | Mã hotfix, version `srv.sys` | Bằng chứng xác thực nội bộ |

### 2.4.2. Quy tắc phân biệt dữ kiện, diễn giải và kết luận
Báo cáo kỹ thuật tách bạch ba khái niệm: Dữ kiện nguồn (Source Fact), Diễn giải kỹ thuật (Interpretation) và Kết luận an ninh (Security Assertion). Kết luận an ninh chỉ hình thành khi có sự hội tụ giữa dữ kiện từ xa và sự thật nội bộ.

Mô hình luồng dữ liệu thu thập và đối chiếu được thể hiện trong Sơ đồ 2.2.

```
+-------------------------------------------------------------------------+
|                  LUỒNG THU THẬP VÀ ĐỐI CHIẾU DỮ LIỆU                    |
|                                                                         |
|  [ĐẦU RA CÔNG CỤ ĐO]   ----->  [DỮ KIỆN NGUỒN: Mã lỗi, phản hồi thô]    |
|                                          |                              |
|                                          v                              |
|                                [DIỄN GIẢI KỸ THUẬT: Đặc tả giao thức]   |
|                                          |                              |
|  [SỰ THẬT NỘI BỘ]      ----->  [ĐỐI CHIẾU VI SAI HAI CHIỀU]             |
|                                          |                              |
|                                          v                              |
|                                [KẾT LUẬN AN NINH CÓ RANH GIỚI]          |
+-------------------------------------------------------------------------+
```
*Sơ đồ 2.2. Luồng thu thập dữ liệu và phân tách các lớp quan sát*

### 2.4.3. Định dạng raw output và Evidence ID
Dữ liệu kiểm thử được lưu trữ dạng raw log và ảnh chụp theo hệ thống Stable Evidence ID trong `EVIDENCE_REGISTER.md`:
- `ENV-CORE-01` đến `ENV-CORE-07`: Môi trường mạng, trạm Kali, máy chủ Windows Server 2012 R2, tường lửa và snapshot `Before Demo`.
- `S1-RAW-01` đến `S1-RAW-05` và `S1-META-01`: Dữ liệu thô rà quét mạng, cổng TCP 139/445 và dịch vụ SMB trong Kịch bản 1.
- `S2-RAW-01` đến `S2-RAW-04` và `S2-META-01`: Dữ liệu bốn kỹ thuật NSE (trạng thái cổng, phương ngữ, ký số, MS17-010) trong Kịch bản 2.
- `B-LOCAL-01`, `B-ACTION-01`, `B-LOCAL-02`, `B-RAW-01`, `B-RAW-02`, `B-META-01`: Bằng chứng can thiệp vô hiệu hóa SMBv1 Case B.
- `C-TOPO-01`, `C-RULE-01`, `C-RULE-02`, `C-RAW-01`, `C-LOG-01`, `C-RAW-02`, `C-META-01`: Bằng chứng cấu hình pfSense và log chặn lọc Case C.
Quy định này bảo đảm mọi kết luận đều truy vết trực tiếp tới dữ liệu gốc nguyên bản.

### 2.4.4. Quy tắc xử lý UNKNOWN, NO OUTPUT và FILTERED
Quy trình thiết lập quy tắc chặt chẽ cho các phản hồi không xác định:
- Trạng thái `UNKNOWN` hoặc `NO USABLE SCRIPT RESULT`: Công cụ quét không nhận được dữ liệu hợp lệ; dữ kiện này không được suy diễn thành hệ thống an toàn.
- Trạng thái `NO OUTPUT`: Kịch bản NSE không in kết quả, phản ánh điều kiện kích hoạt chưa thỏa mãn.
- Trạng thái `FILTERED`: Cổng không phản hồi do có thiết bị lọc gói tin trung gian, không đồng nghĩa với việc lỗ hổng đã được vá.

## 2.5. Thiết kế Kịch bản 1 — Khảo sát dịch vụ SMB bằng Nmap

### 2.5.1. Mục tiêu và điều kiện bắt đầu
Kịch bản 1 khảo sát bề mặt dịch vụ SMB từ góc độ nút mạng chưa xác thực, gồm phát hiện máy, quét cổng và nhận diện phiên bản. Bảng 2.3 tổng hợp thông số thiết kế kịch bản kiểm thử.

*Bảng 2.3. Thiết kế các kịch bản kiểm thử dịch vụ SMB và thông số thực thi NSE*

| Tên kịch bản / Phép đo | Lệnh thực thi đại diện | Cổng mục tiêu | Mục tiêu kỹ thuật chính | Dữ liệu đầu ra cốt lõi |
| :--- | :--- | :--- | :--- | :--- |
| **Kịch bản 1 — Phát hiện** | `nmap -sn 192.168.56.0/24` | Không quét cổng | Rà quét máy đang hoạt động trong mạng lab | Địa chỉ IP, MAC của máy chủ |
| **Kịch bản 1 — Quét cổng** | `nmap -sS -sV -p139,445 ...` | TCP 139, 445 | Xác định trạng thái cổng và dịch vụ | Trạng thái `open`, LanmanServer |
| **Kịch bản 2 — NSE-SMB-01**| `nmap -p139,445 192.168.56.20` | TCP 139, 445 | Thiết lập mốc đối chứng trạng thái cổng | Trạng thái cổng baseline |
| **Kịch bản 2 — NSE-SMB-02**| `nmap -p445 --script smb-protocols` | TCP 445 | Liệt kê danh sách phương ngữ SMB | Danh sách dialects (1.0, 2.02..)|
| **Kịch bản 2 — NSE-SMB-03**| `nmap -p445 --script smb*-mode` | TCP 445 | Kiểm tra chính sách ký số thông điệp | Trạng thái signing enabled |
| **Kịch bản 2 — NSE-SMB-04**| `nmap -p445 --script smb-vuln*` | TCP 445 | Thăm dò dấu hiệu logic lỗ hổng MS17-010 | Dấu hiệu phản hồi từ xa |

### 2.5.2. Phát hiện máy trong mạng lab
Pha đầu của Kịch bản 1 thực hiện Ping Scan (`-sn`) trên dải `192.168.56.0/24`. Nmap gửi ARP Request tới từng IP trong lab. Phản hồi ARP Reply xác nhận sự hiện diện của máy mục tiêu cùng địa chỉ MAC card mạng ảo.

### 2.5.3. Xác nhận máy mục tiêu
Khi ghi nhận IP hoạt động `192.168.56.20`, quy trình đối chiếu MAC với VirtualBox để xác nhận đúng mục tiêu, tránh quét nhầm card host `192.168.56.1`. IP này được cố định cho toàn bộ phép đo.

### 2.5.4. Kiểm tra TCP 139/445
Kỹ thuật SYN Stealth Scan (`-sS`) được áp dụng cho cổng TCP 139 và 445. Gói tin SYN-ACK từ máy chủ xác nhận cổng `open`. Nmap gửi gói RST để giải phóng phiên mà không duy trì kết nối đầy đủ.

### 2.5.5. Nhận diện dịch vụ và phiên bản
Để xác định tiến trình lắng nghe, Nmap kích hoạt dò phiên bản dịch vụ (`-sV`). Chuỗi thăm dò nhận diện dịch vụ `netbios-ssn` trên cổng 139 và `microsoft-ds` của Windows Server 2012 R2 trên cổng 445.

### 2.5.6. Khảo sát SMB bằng NSE
Kịch bản NSE cơ bản thu thập định danh máy chủ không cần quyền quản trị. Bản tin đàm phán ghi nhận tên NetBIOS, domain và dấu thời gian, khẳng định dịch vụ SMB xử lý yêu cầu bình thường.

### 2.5.7. Tiêu chí dừng và bằng chứng cần thu
Kịch bản 1 kết thúc khi ghi nhận đầy đủ trạng thái mở của TCP 139/445 và định danh dịch vụ `microsoft-ds`. Dữ liệu xuất ra được lưu trữ nguyên bản vào các tệp nhật ký thô thuộc họ `S1-RAW` (từ `S1-RAW-01` đến `S1-RAW-05`) cùng tệp siêu dữ liệu `S1-META-01`, làm mốc tham chiếu cho Kịch bản 2.

## 2.6. Thiết kế Kịch bản 2 — Đánh giá cấu hình SMB và MS17-010 bằng NSE

### 2.6.1. NSE-SMB-01 — trạng thái cổng
Phép đo `NSE-SMB-01` thiết lập đường cơ sở độc lập về trạng thái cổng trước khi chạy script chuyên sâu. Phép quét tập trung vào TCP 139 và 445, bảo đảm kênh truyền ổn định trước khi gửi bản tin phức tạp.

### 2.6.2. NSE-SMB-02 — SMB dialects
Đối với phương ngữ giao thức, phép đo `NSE-SMB-02` sử dụng script `smb-protocols.nse` [6] để liệt kê danh mục phương ngữ SMB máy chủ chấp nhận. Bản tin đàm phán `SMB_COM_NEGOTIATE` được gửi đi, khẳng định sự hiện diện thực tế của SMBv1 (`NT LM 0.12`) trên hệ thống.

### 2.6.3. NSE-SMB-03 — SMB signing
Chính sách ký số thông điệp (Message Signing) được kiểm tra trong phép đo `NSE-SMB-03` qua script `smb-security-mode.nse` và `smb2-security-mode.nse` nhằm rà soát các tính năng an ninh mở rộng của SMB theo tài liệu của Microsoft [7]. Dữ liệu thu được xác định hai trạng thái: tính năng ký số được hỗ trợ (`message_signing: enabled`) và tính năng ký số có bắt buộc (`message_signing: required`).

### 2.6.4. NSE-SMB-04 — dấu hiệu MS17-010
Dấu hiệu lỗ hổng MS17-010 được thăm dò chuyên biệt trong phép đo `NSE-SMB-04` qua script `smb-vuln-ms17-010.nse`. Script kết nối tài nguyên `IPC$` và gửi bản tin `SMB_COM_TRANSACTION2` thăm dò phi phá hủy theo cấu trúc mã nguồn của Calderon [8], phân tích phản hồi từ `srv.sys` để đưa ra phán quyết an ninh.

### 2.6.5. Đối chiếu remote observation với local patch ground truth
Quy trình đối chiếu kết quả `smb-vuln-ms17-010.nse` với sự thật nội bộ gồm phiên bản `srv.sys` (6.3.9600.16421) và log `Get-HotFix`. Phương pháp này làm rõ tín hiệu từ xa có phản ánh đúng thực trạng chưa vá lỗi hay không.

### 2.6.6. Tiêu chí kết luận và giới hạn suy diễn
Kịch bản 2 xác định ranh giới suy diễn: kết quả NSE chỉ phản ánh dấu hiệu từ xa tại thời điểm phát lệnh, không thay thế kiểm tra nhân hệ điều hành. Quy trình nghiêm cấm suy diễn máy chủ an toàn khi công cụ gặp lỗi kết nối.

## 2.7. Thiết kế kiểm thử biện pháp giảm thiểu

### 2.7.1. Nguyên tắc differential testing và phục hồi baseline
Kiểm thử vi sai xem mỗi giải pháp giảm thiểu là một biến can thiệp độc lập. Hệ thống bắt đầu từ snapshot `Before Demo`, áp dụng can thiệp, đo lại Kịch bản 1 và 2, rồi hoàn nguyên về đường cơ sở.

Trình tự vòng lặp kiểm thử vi sai và đối chiếu đa tầng được mô tả trong Sơ đồ 2.3.

```
+-------------------------------------------------------------------------+
|                  QUY TRÌNH KIỂM THỬ VI SAI VÀ ĐỐI CHIẾU                 |
|                                                                         |
|  [SNAPSHOT BEFORE DEMO] ----> [ÁP DỤNG CAN THIỆP PHÒNG THỦ]             |
|  (Trạng thái mốc sạch)        (Case B: Tắt SMBv1 / Case C: pfSense)     |
|           ^                                      |                      |
|           |                                      v                      |
|           |                           [ĐO LẠI KỊCH BẢN 1 & 2]           |
|           |                           (Quét cổng, NSE protocols, vuln)  |
|           |                                      |                      |
|           |                                      v                      |
|   [HOÀN NGUYÊN SNAPSHOT] <---- [SO SÁNH SAI KHÁC VỚI BASELINE]          |
|   (Loại bỏ sai số đo)       (Định lượng hiệu quả bảo vệ)             |
+-------------------------------------------------------------------------+
```
*Sơ đồ 2.3. Mô hình quy trình kiểm thử vi sai và đối chiếu đa lớp*

### 2.7.2. Case B — Vô hiệu hóa SMBv1
Biện pháp Case B can thiệp cấu hình giao thức theo hướng dẫn của Microsoft [9]. Lệnh `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` được thực thi và máy chủ khởi động lại. Can thiệp này loại bỏ SMB 1.0 khỏi đàm phán, trong khi SMB 2.x/3.x vẫn hoạt động trên cổng 445.

### 2.7.3. Case C — Giới hạn TCP 139/445 bằng pfSense Transparent Bridge
Biện pháp Case C triển khai tường lửa lọc gói theo hướng dẫn NIST SP 800-41 Rev. 1 [10], dùng pfSense Transparent Bridge chặn lưu lượng TCP 139/445 giữa hai máy ảo:
- Chặn gói TCP đến cổng 139 (`Block TCP * * 139`);
- Chặn gói TCP đến cổng 445 (`Block TCP * * 445`);
- Cho phép ICMP Echo lưu thông để giám sát kết nối mạng.
Cấu hình này kỳ vọng chuyển trạng thái cổng từ `open` sang `filtered`, ngăn gói thăm dò dịch vụ từ xa.

### 2.7.4. Vai trò của cập nhật bản vá trong mô hình phòng thủ
Trong lý thuyết an ninh mạng, cập nhật bản vá chính thức (Case A với gói KB4012213 hoặc KB4012216) là biện pháp căn bản khắc phục lỗi logic trong `srv.sys` [4]. Trong môi trường lab cô lập, Case A đóng vai trò mốc tham chiếu lý thuyết song song với thực nghiệm Case B và C.

### 2.7.5. Ma trận biến can thiệp và phép đo lại
Ma trận biến can thiệp được thiết lập để theo dõi biến động hệ thống qua từng phép đo. Bảng 2.4 tổng hợp ma trận can thiệp và phương án kiểm thử vi sai.

*Bảng 2.4. Ma trận biến can thiệp và phương án kiểm thử giảm thiểu Case B và Case C*

| Trường hợp thực nghiệm | Vị trí áp dụng | Biến can thiệp | Trạng thái cổng 139/445 | SMBv1 | Cơ chế cốt lõi |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Baseline (Mốc đối chứng)**| Không can thiệp | Trạng thái mặc định OS | `open` / `open` | Bình thường | Mốc đối chứng chuẩn |
| **Case B (Tắt SMBv1)** | Cấu hình máy chủ | `EnableSMB1Protocol = $false` | `open` / `open` | Vô hiệu hóa | Loại bỏ giao thức lỗi thời |
| **Case C (Lọc cổng pfSense)**| Cầu nối mạng | Luật chặn TCP 139/445 | `filtered` / `filtered` | Bị chặn mạng | Thu hẹp bề mặt tấn công |
| **Case A (Cập nhật bản vá)** | Nhân hệ điều hành | Gói vá KB4012213 (srv.sys) | `open` / `open` | Hoạt động an toàn | Tham chiếu phân tích lý thuyết |

## 2.8. Tiêu chí đánh giá kết quả

### 2.8.1. Tiêu chí reachability
Tiêu chí reachability xác định khả năng liên lạc tầng mạng dựa trên ICMP Echo. Tỷ lệ mất gói bằng không khẳng định kênh truyền thông suốt. Nếu mất toàn bộ gói tin, quy trình dừng lại để xử lý kết nối trước khi phân tích tầng trên.

### 2.8.2. Tiêu chí protocol surface
Tiêu chí protocol surface đánh giá độ mở của bề mặt dịch vụ qua trạng thái cổng và phương ngữ chấp nhận. Bề mặt dịch vụ tồn tại khi cổng 139/445 ở trạng thái `open`. Bề mặt giao thức tiềm ẩn nguy cơ khi phản hồi `smb-protocols` chứa phương ngữ `NT LM 0.12`.

### 2.8.3. Tiêu chí remote vulnerability signal
Tiêu chí remote vulnerability signal phân loại phản hồi `smb-vuln-ms17-010` theo ba trạng thái: `VULNERABLE` (khẳng định lỗi logic), `NOT VULNERABLE` (từ chối an toàn) và `UNKNOWN / NO USABLE SCRIPT RESULT` (kết nối hủy hoặc lỗi cú pháp).

### 2.8.4. Tiêu chí patch ground truth
Tiêu chí patch ground truth xác lập chân lý nội bộ qua `Get-HotFix` và phiên bản `srv.sys` (ngưỡng an toàn 6.3.9600.18604). Bảng 2.5 chuẩn hóa khung đối sánh giữa dữ kiện từ xa và sự thật nội bộ.

*Bảng 2.5. Tiêu chí phân loại kết quả kiểm thử và ranh giới suy diễn bảo mật*

| Dữ kiện từ xa (Remote Signal) | Sự thật nội bộ (Local Ground Truth) | Đánh giá an ninh tổng hợp | Ranh giới suy diễn bắt buộc |
| :--- | :--- | :--- | :--- |
| `VULNERABLE` | `UNPATCHED` (srv.sys < .18604) | Nguy cơ khai thác trực tiếp | Bằng chứng hội tụ đầy đủ hai chiều |
| `UNKNOWN / NO RESULT` | `UNPATCHED` (srv.sys < .18604) | Nguy cơ tiềm ẩn chưa xác định | Tín hiệu từ xa bị lỗi, hệ thống vẫn tồn tại lỗ hổng |
| `UNKNOWN / NO RESULT` | `PATCHED` (srv.sys >= .18604) | Không phát hiện nguy cơ | Đã vá lỗi nội bộ, tín hiệu từ xa không mang rủi ro |
| `FILTERED` (Cổng bị chặn) | `UNPATCHED` (srv.sys < .18604) | Bề mặt mạng được bảo vệ | Dịch vụ được che chắn, nhân hệ thống chưa vá lỗi |

### 2.8.5. Tiêu chí hiệu quả và giới hạn của mitigation
Tiêu chí giải pháp đo lường mức độ thu hẹp bề mặt tấn công và tính khả dụng dịch vụ. Case B loại bỏ SMBv1 nhưng có thể ảnh hưởng tương thích; Case C chặn lưu lượng qua mạng nhưng không vá lỗi nội tại máy chủ.

## 2.9. Tổng kết Chương 2

Chương 2 đã thiết lập kiến trúc môi trường lab và quy trình kiểm thử dịch vụ SMB cùng lỗ hổng MS17-010. Mô hình Host-Only bảo đảm cô lập an toàn. Cơ chế snapshot `Before Demo`, mô hình năm lớp quan sát và kiểm thử vi sai bảo đảm tính tái lập của dữ liệu.

Khung tiêu chí đánh giá phân tách rõ dữ kiện nguồn, diễn giải kỹ thuật và kết luận bảo mật. Việc đối chiếu tín hiệu từ xa với sự thật bản vá nội bộ ngăn chặn suy diễn chủ quan. Toàn bộ thiết kế kịch bản và ma trận biến can thiệp là cơ sở chuẩn mực để triển khai thực nghiệm trong Chương 3.

## TÀI LIỆU THAM KHẢO

[1] National Institute of Standards and Technology, Technical Guide to Information Security Testing and Assessment, NIST SP 800-115, 2008. [Online]. Available: https://csrc.nist.gov/pubs/sp/800/115/final

[2] Kali Linux Project, "What is Kali Linux?," Kali Linux Documentation. [Online]. Available: https://www.kali.org/docs/introduction/what-is-kali-linux/

[3] Microsoft Learn, "Direct hosting of SMB over TCP/IP," Microsoft Learn, 2026. [Online]. Available: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/direct-hosting-of-smb-over-tcpip

[4] Microsoft, "Microsoft Security Bulletin MS17-010 - Critical," Microsoft Learn / Security TechCenter, Mar. 2017. [Online]. Available: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010

[5] G. Lyon, Nmap Network Scanning: The Official Nmap Project Guide to Network Discovery and Vulnerability Scanning. Sunnyvale, CA: Insecure.Com LLC, 2009. [Online]. Available: https://nmap.org/book/

[6] P. Calderon and Nmap Project, "smb-protocols.nse Script Source Code," Nmap Project. [Online]. Available: https://svn.nmap.org/nmap/scripts/smb-protocols.nse

[7] Microsoft Learn, "SMB security enhancements," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security

[8] P. Calderon and Nmap Project, "smb-vuln-ms17-010.nse Script Source Code," Nmap Project, 2017. [Online]. Available: https://svn.nmap.org/nmap/scripts/smb-vuln-ms17-010.nse

[9] Microsoft Learn, "Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3

[10] National Institute of Standards and Technology, Guidelines on Firewalls and Firewall Policy, NIST SP 800-41 Rev. 1, 2009. [Online]. Available: https://csrc.nist.gov/pubs/sp/800/41/r1/final
