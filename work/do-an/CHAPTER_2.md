# CHƯƠNG 2. THIẾT KẾ VÀ TRIỂN KHAI MÔ HÌNH THỰC NGHIỆM

Chương 2 trình bày thiết kế môi trường lab và quy trình kiểm thử dịch vụ SMB cùng lỗ hổng MS17-010. Nội dung tập trung vào kiến trúc mạng cô lập, cơ chế snapshot, quy trình lưu trữ dữ liệu thô và mô hình năm lớp quan sát từ kết nối mạng đến bản vá nội bộ.

## 2.1. Yêu cầu và nguyên tắc thiết kế

### 2.1.1. Mục tiêu của môi trường thực nghiệm
Môi trường lab phục vụ khảo sát dịch vụ SMB và đánh giá an ninh lỗ hổng MS17-010 qua việc phân định quan sát từ xa và bản vá nội bộ. Do máy mục tiêu chưa vá, lab giới hạn kết nối trực tiếp giữa hai máy ảo qua Host-Only nhằm duy trì phân lập an toàn và thuận tiện truy nguyên lưu lượng.

### 2.1.2. Phạm vi, nguyên tắc an toàn và giới hạn đạo đức
Phạm vi thực nghiệm tuân thủ hướng dẫn NIST SP 800-115 [1], chỉ áp dụng kỹ thuật quét cổng, trinh sát dịch vụ và kiểm tra logic giao thức phi phá hủy. Quy trình không phát tán mã khai thác, không tấn công chiếm quyền điều khiển và không gây nghẽn dịch vụ.

### 2.1.3. Nguyên tắc cô lập mạng và khả năng khôi phục
Tại trạng thái pre-demo đã khóa, hai máy ảo chỉ sử dụng card mạng Host-Only, không cấu hình NAT hoặc Bridged và trạm Kali không có default route ra Internet. Nhằm phục vụ kiểm thử vi sai, snapshot `Before Demo` trên máy mục tiêu được xác định làm mốc thiết kế chuẩn để phục hồi baseline giữa các biến can thiệp, tránh việc thay đổi của kịch bản trước ảnh hưởng tới kết quả của kịch bản sau.

### 2.1.4. Nguyên tắc thu thập, truy vết và bảo toàn bằng chứng
Tính truy vết đòi hỏi mọi nhận định kỹ thuật đều đối chiếu được với dữ liệu gốc. Khi cần kiểm tra lại, Evidence ID cho phép quay về đúng raw file hoặc ảnh trạng thái tương ứng. Quy trình ưu tiên raw log và XML hơn ảnh chụp hoặc bản tóm tắt: ảnh có thể bị cắt xén, tóm tắt đã qua diễn giải, do đó tệp nhật ký thô là căn cứ đối chiếu cao nhất.

## 2.2. Kiến trúc môi trường thực nghiệm

### 2.2.1. Nền tảng Oracle VirtualBox
Nền tảng Oracle VM VirtualBox 7.2.20 r170876 làm hạ tầng thực thi cho mô hình lab. Cơ chế mạng Host-Only Adapter liên kết các máy ảo qua switch ảo nội bộ, không bắc cầu ra card mạng vật lý của máy chủ. Kiến trúc kết nối giữa các thành phần thực nghiệm được mô tả trong Hình 2.1.

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
Máy kiểm thử sử dụng bản phân phối Kali Linux 64-bit (nhân Kernel 6.12.33-amd64) theo tài liệu dự án Kali Linux [2]. Máy ảo cấu hình 2 vCPU, 4096 MB RAM, gán IP tĩnh `192.168.56.10/24`. Bộ công cụ Nmap cùng thư viện NSE được cài đặt sẵn để thực thi các kịch bản kiểm tra dịch vụ SMB.

### 2.2.3. Máy mục tiêu Windows Server 2012 R2
Máy mục tiêu cài Windows Server 2012 R2 Standard Evaluation 64-bit (Build 9600), cấu hình 2 vCPU, 4096 MB RAM, gán IP tĩnh `192.168.56.20/24`. Dịch vụ LanmanServer mở socket lắng nghe trên TCP 445 (Direct-hosted SMB) và TCP 139 (NetBIOS over TCP/IP) theo Microsoft [3].

### 2.2.4. Mạng Host-Only và bảng địa chỉ IP
Mạng Host-Only sử dụng dải IPv4 `192.168.56.0/24`, tắt DHCP và không cấu hình Default Gateway hay DNS. Thông số chi tiết của các nút mạng và phân bổ tài nguyên phần cứng được tổng hợp trong Bảng 2.1.

*Bảng 2.1. Thông số kỹ thuật của các nút mạng trong môi trường thực nghiệm*

| Tham số cấu hình | Máy kiểm thử (Kali Linux) | Máy mục tiêu (Windows Server) | Ghi chú kỹ thuật |
| :--- | :--- | :--- | :--- |
| **Hệ điều hành** | Kali Linux (Kernel 6.12.33) | Windows Server 2012 R2 Eval | Nền tảng 64-bit |
| **Số hiệu bản dựng** | Kali Rolling (Nmap 7.99) | Build 9600 (Trạng thái RTM) | Mã định danh OS |
| **Địa chỉ IP / Mask**| `192.168.56.10/24` | `192.168.56.20/24` | Gán tĩnh, tắt DHCP |
| **Cổng đo đạc** | Dải cổng cao ngẫu nhiên | TCP 139, TCP 445 | LanmanServer lắng nghe |
| **Mạng ảo hóa** | Host-Only Adapter | Host-Only Adapter | Cô lập L2 |
| **Tài nguyên** | 2 vCPU, 4096 MB RAM | 2 vCPU, 4096 MB RAM | VirtualBox |

### 2.2.5. Kiểm tra kết nối trong phạm vi lab
Trước khi đo đạc dịch vụ SMB, quy trình kiểm tra khả năng tiếp cận mạng bằng ICMP Echo Request (`ping`) giữa `192.168.56.10` và `192.168.56.20`. Bước tiền điều kiện này giúp loại trừ lỗi cấu hình mạng ảo trước khi đo dịch vụ; số liệu định lượng cụ thể được trình bày tại Chương 3.

## 2.3. Chuẩn bị trạng thái baseline

### 2.3.1. Trạng thái hệ điều hành và dịch vụ SMB
Đường cơ sở phản ánh cấu hình dịch vụ nguyên bản. Dịch vụ LanmanServer đặt ở chế độ tự động chạy (`Running`), mở socket lắng nghe trên hệ thống.

### 2.3.2. Trạng thái SMBv1/SMB2 và TCP 139/445
Ở baseline canonical của máy Windows Server 2012 R2, cả SMBv1 và SMBv2/SMB3 đều ở trạng thái kích hoạt. Lệnh PowerShell `Get-SmbServerConfiguration` xác nhận `EnableSMB1Protocol` và `EnableSMB2Protocol` đều mang giá trị `True` trước khi thực hiện các phép đo từ xa.

### 2.3.3. Cấu hình Windows Firewall phục vụ phép đo
Windows Firewall mặc định có thể lọc lưu lượng SMB từ mạng ngoài. Để phản hồi phản ánh đúng trạng thái dịch vụ LanmanServer, nhóm kích hoạt luật `File and Printer Sharing (SMB-In)` cho phép TCP 139 và 445 riêng cho địa chỉ `192.168.56.10`.

### 2.3.4. Xác định trạng thái bản vá MS17-010 và srv.sys
Trạng thái bản vá được kiểm tra trên máy mục tiêu. Lệnh `Get-HotFix` xác nhận chưa cài đặt bản vá KB4012213 hoặc KB4012216. Tệp driver `srv.sys` ghi nhận phiên bản `6.3.9600.16421`, thấp hơn ngưỡng `6.3.9600.18604` theo tài liệu MS17-010 [4]. Do công cụ quét từ xa có thể trả về kết quả UNKNOWN, thông tin hotfix và `srv.sys` được giữ như trục đối chứng độc lập, xác định trạng thái bản vá nội bộ là `UNPATCHED`.

### 2.3.5. Kiểm tra Nmap và NSE script trên Kali
Tại trạm Kali Linux, lệnh `nmap --version` xác nhận phiên bản Nmap đang hoạt động theo Gordon Lyon [5]. Thư mục `/usr/share/nmap/scripts/` chứa đầy đủ các kịch bản: `smb-protocols.nse`, `smb-security-mode.nse`, `smb2-security-mode.nse` và `smb-vuln-ms17-010.nse`.

### 2.3.6. Snapshot Before Demo và phương án phục hồi
Snapshot `Before Demo` được tạo trên máy ảo sau khi hoàn tất baseline. Việc giữ snapshot giúp hai can thiệp độc lập (Case B đổi dịch vụ trên Server và Case C lọc cổng trên đường mạng) đều xuất phát từ cùng mốc sạch, tránh can thiệp trước gây nhiễu can thiệp sau.

## 2.4. Phương pháp kiểm thử và mô hình bằng chứng

### 2.4.1. Các lớp quan sát: reachability, service, protocol, remote signal, local ground truth
Quy trình phân tách quan sát thành năm lớp độc lập nhằm tránh nhầm lẫn: cổng mở không đồng nghĩa dịch vụ chấp nhận SMBv1, và hỗ trợ SMBv1 không đồng nghĩa lỗ hổng có thể khai thác. Năm lớp này phân định từ kết nối mạng, bề mặt cổng, dialect giao thức, dấu hiệu từ xa đến bản vá nội bộ (Bảng 2.2).

*Bảng 2.2. Phân loại các lớp quan sát và cơ chế thu thập dữ liệu trong mô hình kiểm thử*

| Lớp quan sát | Đối tượng đo đạc | Công cụ thực hiện | Dữ liệu đầu ra kỳ vọng | Ý nghĩa an toàn |
| :--- | :--- | :--- | :--- | :--- |
| **1. Reachability** | Tầng mạng IP | `ping` (ICMP Echo) | RTT, tỷ lệ nhận phản hồi | Xác nhận thông tuyến |
| **2. Port & Service**| Cổng TCP 139, 445 | `nmap -sS -p139,445` | `open`, `closed`, `filtered` | Bề mặt dịch vụ |
| **3. Protocol State** | Dialect và ký số SMB | `smb-protocols`, `smb2-security-mode` | Danh sách dialects, Signing | Tính năng giao thức |
| **4. Remote Signal** | Thăm dò lỗ hổng từ xa | `smb-vuln-ms17-010.nse` | `VULNERABLE`, `UNKNOWN` | Tín hiệu từ xa |
| **5. Ground Truth** | Bản vá và driver nội bộ | `Get-HotFix`, `srv.sys` | Mã hotfix, version `srv.sys` | Trạng thái nội bộ |

### 2.4.2. Quy tắc phân biệt dữ kiện, diễn giải và kết luận
Báo cáo kỹ thuật phân định ba cấp độ thông tin: Dữ kiện nguồn (đầu ra thô từ công cụ), Diễn giải kỹ thuật (áp dụng đặc tả giao thức để phân tích phản hồi) và Kết luận an ninh. Kết luận an ninh chỉ hình thành khi đối chiếu quan sát từ xa với bản vá nội bộ trong ranh giới kiểm thử rõ ràng. Luồng xử lý được thể hiện trong Sơ đồ 2.2.

```
+-------------------------------------------------------------------------+
|                  LUỒNG THU THẬP VÀ ĐỐI CHIẾU DỮ LIỆU                    |
|                                                                         |
|  [ĐẦU RA CÔNG CỤ ĐO]   ----->  [DỮ KIỆN NGUỒN: Mã lỗi, phản hồi thô]    |
|                                          |                              |
|                                          v                              |
|                                [DIỄN GIẢI KỸ THUẬT: Đặc tả giao thức]   |
|                                          |                              |
|  [TRẠNG THÁI NỘI BỘ]   ----->  [ĐỐI CHIẾU VI SAI HAI CHIỀU]             |
|                                          |                              |
|                                          v                              |
|                                [KẾT LUẬN AN NINH CÓ RANH GIỚI]          |
+-------------------------------------------------------------------------+
```
*Sơ đồ 2.2. Luồng thu thập dữ liệu và phân tách các lớp quan sát*

### 2.4.3. Định dạng raw output và Evidence ID
Dữ liệu kiểm thử được lưu trữ dạng raw log và ảnh chụp theo hệ thống Stable Evidence ID trong `EVIDENCE_REGISTER.md`:
- `ENV-CORE-01` đến `ENV-CORE-07`: Môi trường mạng, trạm Kali, Windows Server 2012 R2, tường lửa và snapshot `Before Demo`.
- `S1-RAW-01` đến `S1-RAW-05` và `S1-META-01`: Rà quét mạng, cổng TCP 139/445 và dịch vụ SMB (Kịch bản 1).
- `S2-RAW-01` đến `S2-RAW-04` và `S2-META-01`: Bốn kỹ thuật NSE (trạng thái cổng, dialect, ký số, MS17-010) (Kịch bản 2).
- `B-LOCAL-01`, `B-ACTION-01`, `B-LOCAL-02`, `B-RAW-01`, `B-RAW-02`, `B-META-01`: Can thiệp vô hiệu hóa SMBv1 Case B.
- `C-TOPO-01`, `C-RULE-01`, `C-RULE-02`, `C-RAW-01`, `C-LOG-01`, `C-RAW-02`, `C-META-01`: Cấu hình pfSense và log chặn lọc Case C.
Khi cần kiểm tra lại, Evidence ID cho phép truy vết về đúng tệp thô hoặc ảnh trạng thái; trong đó nhật ký thô và XML là căn cứ đối chiếu kỹ thuật cao nhất.

### 2.4.4. Quy tắc xử lý UNKNOWN, NO OUTPUT và FILTERED
Quy tắc xử lý phản hồi từ công cụ quét theo chính sách kết quả phủ định:
- `UNKNOWN / NO USABLE SCRIPT RESULT`: Phép đo thiếu dữ liệu phân loại; đây là giới hạn quan sát từ xa, không xem là an toàn (`UNKNOWN != safe`).
- `NO OUTPUT`: Chỉ mô tả script không cung cấp output usable trong lượt đo; không suy đoán nguyên nhân khi chưa có bằng chứng xác nhận.
- `FILTERED`: Nmap không nhận đủ phản hồi để phân loại cổng open hay closed. Trạng thái này không chứng minh dịch vụ dừng, SMBv1 tắt hay host đã vá (`FILTERED != patched`). Riêng Case C, việc quy thuộc cho pfSense chỉ thực hiện ở Chương 3 khi đối chiếu firewall log canonical.

## 2.5. Thiết kế Kịch bản 1 — Khảo sát dịch vụ SMB bằng Nmap

### 2.5.1. Mục tiêu và điều kiện bắt đầu
Kịch bản 1 khảo sát bề mặt dịch vụ SMB từ góc nhìn máy khách chưa xác thực, gồm phát hiện máy, quét cổng và nhận diện dịch vụ (Bảng 2.3).

*Bảng 2.3. Thiết kế các kịch bản kiểm thử dịch vụ SMB và thông số thực thi NSE*

| Phép đo | Lệnh thực thi đại diện | Cổng mục tiêu | Mục tiêu kỹ thuật | Dữ liệu đầu ra cốt lõi |
| :--- | :--- | :--- | :--- | :--- |
| **Kịch bản 1 — Host Discovery** | `nmap -sn 192.168.56.0/24` | Không quét cổng | Rà quét máy trong mạng lab | IP, MAC máy mục tiêu |
| **Kịch bản 1 — Port Scan** | `nmap -sS -sV -p139,445 ...` | TCP 139, 445 | Xác định trạng thái cổng và dịch vụ | Trạng thái cổng, LanmanServer |
| **Kịch bản 2 — NSE-SMB-01** | `nmap -p139,445 192.168.56.20` | TCP 139, 445 | Mốc đối chứng trạng thái cổng | Trạng thái cổng baseline |
| **Kịch bản 2 — NSE-SMB-02** | `nmap -p445 --script smb-protocols` | TCP 445 | Liệt kê danh sách dialect SMB | Danh sách dialects |
| **Kịch bản 2 — NSE-SMB-03** | `nmap -p445 --script smb2-security-mode` | TCP 445 | Kiểm tra chính sách ký số | Trạng thái message signing |
| **Kịch bản 2 — NSE-SMB-04** | `nmap -p445 --script smb-vuln-ms17-010` | TCP 445 | Thăm dò dấu hiệu logic MS17-010 | Tín hiệu phản hồi từ xa |

### 2.5.2. Phát hiện máy trong mạng lab
Pha đầu của Kịch bản 1 thực hiện Ping Scan (`-sn`) trên dải `192.168.56.0/24`. Nmap gửi gói ARP Request tới từng IP trong lab để ghi nhận sự hiện diện và địa chỉ MAC của máy mục tiêu.

### 2.5.3. Xác nhận máy mục tiêu
Khi ghi nhận IP `192.168.56.20`, quy trình đối chiếu địa chỉ MAC với VirtualBox để xác nhận đúng máy mục tiêu, tránh nhầm card host (`192.168.56.1`). Địa chỉ IP này được cố định cho toàn bộ các phép đo.

### 2.5.4. Kiểm tra TCP 139/445
Kỹ thuật SYN Stealth Scan (`-sS`) gửi gói TCP SYN đến cổng 139 và 445 để phân loại trạng thái cổng. Khi nhận phản hồi TCP, công cụ gửi gói RST giải phóng phiên mà không duy trì kết nối đầy đủ; kết quả đo được ghi nhận tại Chương 3.

### 2.5.5. Nhận diện dịch vụ và phiên bản
Để xác định tiến trình lắng nghe, Nmap kích hoạt dò phiên bản (`-sV`). phân tích chuỗi định danh dịch vụ trên cổng 139 và 445 theo cơ sở dữ liệu công cụ.

### 2.5.6. Khảo sát SMB bằng NSE
Các kịch bản NSE cơ bản gửi yêu cầu thương lượng SMB ở mức người dùng khách nhằm thu thập định danh máy chủ như tên NetBIOS, domain và dấu thời gian.

### 2.5.7. Tiêu chí dừng và bằng chứng cần thu
Kịch bản 1 dừng khi hoàn tất các bước rà quét và lưu đầy đủ đầu ra thô vào các tệp thuộc họ `S1-RAW` (từ `S1-RAW-01` đến `S1-RAW-05`) kèm siêu dữ liệu `S1-META-01`.

## 2.6. Thiết kế Kịch bản 2 — Đánh giá cấu hình SMB và MS17-010 bằng NSE

### 2.6.1. NSE-SMB-01 — trạng thái cổng
Phép đo `NSE-SMB-01` quét lại trạng thái cổng TCP 139 và 445 trước khi chạy script chuyên sâu, nhằm xác nhận khả năng tiếp cận dịch vụ trước khi gửi các yêu cầu giao thức phức tạp hơn.

### 2.6.2. NSE-SMB-02 — SMB dialects
Đối với dialect giao thức, kỹ thuật `NSE-SMB-02` sử dụng script `smb-protocols.nse` [6] gửi yêu cầu `SMB_COM_NEGOTIATE` để xác định các dialect mà Server chấp nhận; dữ liệu quan sát được chuyển sang Chương 3.

### 2.6.3. NSE-SMB-03 — SMB signing
Chính sách ký số thông điệp được kiểm tra trong phép đo `NSE-SMB-03` qua script `smb2-security-mode.nse` [7], phân biệt trạng thái hỗ trợ (enabled) và bắt buộc (required).

### 2.6.4. NSE-SMB-04 — dấu hiệu MS17-010
Dấu hiệu MS17-010 được thăm dò qua script `smb-vuln-ms17-010.nse` [8]. Script kết nối tài nguyên `IPC$` và gửi yêu cầu `SMB_COM_TRANSACTION2` phi phá hủy để ghi nhận phản hồi từ driver `srv.sys`.

### 2.6.5. Đối chiếu remote observation với local patch ground truth
Quy trình đối chiếu kết quả NSE với trạng thái bản vá nội bộ (`Get-HotFix` và `srv.sys`) làm rõ giới hạn của công cụ quét từ xa, ngăn ngừa việc đồng nhất tín hiệu không xác định với trạng thái an toàn.

### 2.6.6. Tiêu chí kết luận và giới hạn suy diễn
Kết quả NSE phản ánh tín hiệu thăm dò từ xa, không thay thế việc kiểm tra tệp nhân hệ thống. Khi công cụ thiếu phản hồi hoặc trả về trạng thái không xác định, quy trình không cho phép suy diễn máy chủ an toàn.

## 2.7. Thiết kế kiểm thử biện pháp giảm thiểu

### 2.7.1. Nguyên tắc differential testing và phục hồi baseline
Kiểm thử vi sai xem mỗi giải pháp phòng thủ là một biến can thiệp độc lập, xuất phát từ snapshot `Before Demo`, đo lại qua Kịch bản 1 và 2 trước khi chuyển sang biến can thiệp kế tiếp.

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
|   (Mốc đối chứng sạch)       (Định lượng thay đổi bề mặt)               |
+-------------------------------------------------------------------------+
```
*Sơ đồ 2.3. Mô hình quy trình kiểm thử vi sai và đối chiếu đa lớp*

### 2.7.2. Case B — Vô hiệu hóa SMBv1
Case B can thiệp cấu hình giao thức trên máy chủ Windows theo tài liệu Microsoft [9]. Lệnh PowerShell `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` vô hiệu hóa dialect SMBv1 ở mức runtime nhằm khảo sát thay đổi bề mặt dịch vụ; kết quả đo lại được trình bày tại Chương 3.

### 2.7.3. Case C — Giới hạn TCP 139/445 bằng pfSense Transparent Bridge
Case C can thiệp khả năng tiếp cận dịch vụ trên đường mạng theo NIST SP 800-41 Rev. 1 [10]. pfSense Transparent Bridge đóng vai trò tường lửa L2 giữa hai máy ảo:
- Chặn TCP đến cổng 139 (`Block TCP * * 139`);
- Chặn TCP đến cổng 445 (`Block TCP * * 445`);
- Cho phép ICMP Echo để giám sát kết nối mạng.
Khác với Case B đổi cấu hình dịch vụ, Case C chặn lưu lượng trên mạng mà không can thiệp cấu hình hay bản vá trên máy chủ.

### 2.7.4. Vai trò của cập nhật bản vá trong mô hình phòng thủ
Cập nhật bản vá chính thức (Case A với gói KB4012213 hoặc KB4012216) xử lý trực tiếp lỗi logic trong driver `srv.sys` [4]. Trong lab, Case A là mốc tham chiếu lý thuyết để so sánh cơ chế sửa lỗi cấp nhân với các giải pháp giảm thiểu bề mặt tấn công.

### 2.7.5. Ma trận biến can thiệp và phép đo lại
Bảng 2.4 tổng hợp ma trận thiết kế biến can thiệp và phương án đo lại.

*Bảng 2.4. Ma trận thiết kế biến can thiệp và phép đo lại*

| Trường hợp | Biến chủ động thay đổi | Các biến cần giữ | Phép đo lại | Câu hỏi cần trả lời |
| :--- | :--- | :--- | :--- | :--- |
| **Baseline (Mốc đối chứng)** | Không can thiệp | Mặc định OS, mở TCP 139/445 | Kịch bản 1 và 2 | Bề mặt dịch vụ ban đầu phản hồi ra sao? |
| **Case B (Tắt SMBv1)** | `EnableSMB1Protocol True -> False` | IP, LanmanServer, UNPATCHED | Đo lại `smb-protocols` và `smb-vuln-ms17-010` | Server có còn chấp nhận SMBv1 không? |
| **Case C (Lọc cổng pfSense)** | Thêm pfSense Bridge chặn 139/445 | Cấu hình máy chủ (SMB1=True, UNPATCHED) | Đo lại trạng thái cổng, NSE và log pfSense | Chặn cổng trên mạng đổi khả năng tiếp cận ra sao? |
| **Case A (Cập nhật bản vá)** | Gói KB4012213 (srv.sys >= .18604) | Lớp tham chiếu lý thuyết, không đo lại | So sánh lý thuyết với Case B/C | Bản vá sửa driver khác gì giảm thiểu bề mặt? |

## 2.8. Tiêu chí đánh giá kết quả

### 2.8.1. Tiêu chí reachability
Tiêu chí reachability xác định khả năng liên lạc tầng mạng qua ICMP Echo. Tỷ lệ mất gói bằng không khẳng định kết nối thông suốt; nếu mất toàn bộ gói, quy trình dừng để kiểm tra mạng trước khi đo tầng dịch vụ.

### 2.8.2. Tiêu chí protocol surface
Tiêu chí protocol surface đánh giá độ mở dịch vụ qua trạng thái cổng và dialect chấp nhận. Bề mặt dịch vụ mở khi cổng 139/445 ở trạng thái open; bề mặt giao thức tiềm ẩn nguy cơ khi phản hồi `smb-protocols` chứa dialect SMBv1 (`NT LM 0.12`).

### 2.8.3. Tiêu chí remote vulnerability signal
Tiêu chí remote vulnerability signal đánh giá phản hồi `smb-vuln-ms17-010` theo mô hình bằng chứng thực nghiệm, do lệnh canonical không dùng `vulns.showall`:
- `VULNERABLE`: Chỉ ghi khi script thực sự xuất kết quả tường minh khẳng định phát hiện dấu hiệu MS17-010.
- `UNKNOWN / NO USABLE SCRIPT RESULT`: Dùng khi script không đưa ra verdict usable hoặc thiếu dữ liệu; không suy ra không có output là an toàn.
Trạng thái bản vá nội bộ luôn là trục kiểm tra độc lập với tín hiệu từ xa.

### 2.8.4. Tiêu chí patch ground truth
Tiêu chí patch ground truth xác định trạng thái bản vá nội bộ qua `Get-HotFix` và driver `srv.sys` (ngưỡng 6.3.9600.18604). Khung đối sánh được chuẩn hóa trong Bảng 2.5.

*Bảng 2.5. Khung diễn giải bằng chứng giữa quan sát từ xa và trạng thái bản vá nội bộ*

| Quan sát từ xa (Remote Observation) | Trạng thái bản vá nội bộ (Local Ground Truth) | Điều có thể kết luận | Điều chưa được phép kết luận |
| :--- | :--- | :--- | :--- |
| `VULNERABLE` | `UNPATCHED` (srv.sys < .18604) | Tín hiệu từ xa và bản vá nội bộ cùng chỉ ra nguy cơ | Chưa đủ cơ sở khẳng định khai thác RCE thành công |
| `UNKNOWN / NO RESULT` | `UNPATCHED` (srv.sys < .18604) | Phép quét không kết luận; máy chủ chưa vá | Không được xem là hệ thống an toàn (`UNKNOWN != safe`) |
| `UNKNOWN / NO RESULT` | `PATCHED` (srv.sys >= .18604) | Máy chủ đã vá nội bộ; tín hiệu từ xa không mâu thuẫn | Không suy diễn công cụ phát hiện được bản vá |
| `FILTERED` (Đường truy cập bị lọc) | `UNPATCHED` (srv.sys < .18604) | Đường quét từ xa bị lọc; không đủ phản hồi | Không đồng nghĩa hệ thống đã vá (`FILTERED != patched`) |
| `SMBv1 disabled` (Case B) | `UNPATCHED` (srv.sys < .18604) | Đã tắt SMBv1; giảm bề mặt tấn công qua dialect cũ | Không đồng nghĩa driver đã vá (`SMBv1 disabled != patched`) |

### 2.8.5. Tiêu chí hiệu quả và giới hạn của mitigation
Tiêu chí đánh giá giải pháp phòng thủ dựa trên mức thu hẹp bề mặt tấn công và tính khả dụng dịch vụ. Case B loại bỏ SMBv1 ở tầng ứng dụng, ngăn chặn dialect cũ; Case C chặn lưu lượng ở tầng giao vận, che chắn cổng dịch vụ nhưng không thay đổi trạng thái lỗ hổng trong nhân hệ điều hành.

## 2.9. Tổng kết Chương 2

Chương 2 đã xác định thiết kế môi trường lab và quy trình kiểm thử dịch vụ SMB cùng lỗ hổng MS17-010. Mạng Host-Only giữa Kali Linux và Windows Server 2012 R2 tạo môi trường kiểm thử cô lập, trong khi snapshot `Before Demo` phục vụ tái lập trạng thái ban đầu cho các phép đo vi sai.

Hệ thống bằng chứng được tổ chức thành năm lớp quan sát độc lập từ kết nối mạng đến bản vá nội bộ, phân định rõ dữ kiện nguồn, diễn giải kỹ thuật và kết luận an ninh. Các kịch bản khảo sát bề mặt, thăm dò NSE cùng hai biến can thiệp phòng thủ (Case B và Case C) đã được xác lập cụ thể về tham số và tiêu chí đánh giá, làm cơ sở để Chương 3 trình bày dữ liệu đo đạc thực tế.

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
