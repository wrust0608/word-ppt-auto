# CHƯƠNG 2. XÂY DỰNG MÔ HÌNH THỰC NGHIỆM VÀ KỊCH BẢN DEMO

Chương 2 trình bày thiết kế, cài đặt môi trường mạng thực nghiệm cô lập và chuẩn hóa các kịch bản demo khảo sát an toàn dịch vụ SMB cùng lỗ hổng MS17-010.

Nội dung trọng tâm gồm cấu hình trạm kiểm thử Kali Linux và trạm mục tiêu Windows Server 2012 R2. Đồ án xây dựng hai kịch bản demo rà quét bằng Nmap và NSE, thiết lập quy trình kiểm thử vi sai cho các biện pháp giảm thiểu (vô hiệu hóa SMBv1 và tường lửa pfSense), đồng thời chuẩn hóa dữ liệu thu thập phục vụ Chương 3.

## 2.1. Mô hình thực nghiệm

### 2.1.1. Mục tiêu của mô hình
Mô hình thực nghiệm được xây dựng nhằm cung cấp không gian kiểm thử an toàn, độc lập và có thể tái lập [1]. Mục tiêu chính gồm:
1. **Khảo sát bề mặt dịch vụ:** Đánh giá cấu hình SMB, nhận diện trạng thái cổng TCP 139, 445 và phân loại phiên bản giao thức đang chạy.
2. **Thăm dò dấu hiệu an ninh:** Kiểm tra chỉ dấu liên quan đến lỗ hổng MS17-010 qua các gói tin thăm dò chuẩn hóa của NSE mà không gây gián đoạn hệ thống.
3. **Đo đạc hiệu quả giảm thiểu:** So sánh sự thay đổi trạng thái mạng và kết quả quét trước và sau can thiệp phòng thủ.
4. **Bảo đảm an toàn kiểm thử:** Giới hạn lưu lượng trong môi trường lab nội bộ, ngăn lưu lượng thoát ra mạng bên ngoài.

### 2.1.2. Sơ đồ và thành phần của mô hình
Mô hình gồm trạm kiểm thử Kali Linux và trạm mục tiêu Windows Server 2012 R2, kết nối trực tiếp qua mạng Host-Only ảo hóa.

```mermaid
flowchart LR
    subgraph HostOnlyNetwork [Mạng Host-Only cô lập: 192.168.56.0/24]
        direction LR
        Attacker["Trạm kiểm thử (Kali Linux)<br/>192.168.56.10/24<br/>Kernel 6.12.33-amd64"]
        Target["Trạm mục tiêu (Windows Server 2012 R2)<br/>192.168.56.20/24<br/>Build 9600 (RTM)"]
        Attacker <-->|"Lưu lượng TCP 139, 445<br/>(Giới hạn nội bộ)"| Target
    end
```

Hình 2.1. Sơ đồ topo kết nối mạng thực nghiệm trên VirtualBox

Cả hai máy ảo cùng thuộc dải mạng `192.168.56.0/24`. Trong kịch bản mở rộng ở Mục 2.5.3, máy ảo tường lửa pfSense được tích hợp ở giữa theo mô hình cầu nối trong suốt (Transparent Bridge) để lọc gói mà không thay đổi địa chỉ IP hai đầu.

### 2.1.3. Thông số môi trường thực nghiệm
Thông số phần cứng, hệ điều hành và cấu hình mạng được tổng hợp trong Bảng 2.1.

Bảng 2.1. Thông số kỹ thuật của các máy ảo trong môi trường thực nghiệm

| Thông số | Trạm kiểm thử (Kali Linux) | Trạm mục tiêu (Windows Server) | Ý nghĩa thiết kế |
| :--- | :--- | :--- | :--- |
| **Hệ điều hành** | Kali Linux (Kernel 6.12.33-amd64) [2] | Windows Server 2012 R2 Eval | Môi trường chuẩn hóa |
| **Bản dựng** | Kali Rolling (Nmap 7.99) | Build 9600 (RTM nguyên bản) | Tái hiện máy chưa vá |
| **Phần cứng ảo** | 2 vCPU, 4096 MB RAM | 2 vCPU, 4096 MB RAM | Đồng nhất tài nguyên |
| **IP / Subnet** | `192.168.56.10/24` (Tĩnh) | `192.168.56.20/24` (Tĩnh) | Cố định địa chỉ mạng |
| **Giao diện mạng**| 1 Host-Only NIC (`eth0`) | 1 Host-Only NIC (`Ethernet`) | Cách ly, không Internet |
| **Cổng dịch vụ** | Cổng nguồn ngẫu nhiên | TCP 139 và TCP 445 [3] | Khảo sát socket SMB |
| **Dịch vụ SMB** | Máy khách gửi yêu cầu | LanmanServer: `Running` | Dịch vụ chia sẻ tệp |
| **Tường lửa** | Cho phép gửi gói ra lab | Mở TCP 139, 445 từ `.10` | Ủy quyền trạm quét |

Việc chuẩn hóa phần cứng và địa chỉ IP tĩnh giúp loại bỏ yếu tố gây nhiễu, bảo đảm tính nhất quán cho các phép đo.

## 2.2. Cài đặt và cấu hình môi trường

### 2.2.1. Cấu hình mạng Host-Only trên VirtualBox
Môi trường thực nghiệm được triển khai trên Oracle VM VirtualBox 7.2.20 r170876:
- **Tạo giao diện mạng:** Khởi tạo card mạng Host-Only với dải địa chỉ IPv4 `192.168.56.0/24`, địa chỉ adapter máy chủ là `192.168.56.1/24`.
- **Vô hiệu hóa DHCP:** Tắt VirtualBox DHCP Server để ngăn cấp phát IP động, bảo đảm tính cố định cho cấu hình tĩnh.
- **Cách ly mạng:** Không dùng card mạng NAT hay Bridged, không đặt Default Gateway nhằm giới hạn lưu lượng trong môi trường lab.

### 2.2.2. Cấu hình máy Kali Linux
Trạm kiểm thử sử dụng Kali Linux 64-bit (Kernel 6.12.33-amd64) [2]:
- **Cấu hình mạng:** Thiết lập địa chỉ IPv4 tĩnh `192.168.56.10/24` trên giao diện `eth0`.
- **Công cụ rà quét:** Sử dụng Nmap 7.99 cùng bộ thư viện kịch bản NSE chuẩn hóa phục vụ thu thập thông tin và đánh giá an ninh.

### 2.2.3. Cấu hình máy Windows Server 2012 R2
Trạm mục tiêu sử dụng Windows Server 2012 R2 Standard Evaluation 64-bit:
- **Cấu hình mạng:** Gán địa chỉ tĩnh `192.168.56.20/24` trên giao diện `Ethernet`.
- **Trạng thái hệ thống:** Giữ nguyên bản dựng Build 9600 (RTM), không cài đặt bất kỳ gói rollup nào để làm hệ thống đối chứng trước khi áp dụng các biện pháp an ninh.

### 2.2.4. Cấu hình SMB và Windows Firewall
Dịch vụ chia sẻ tệp và tường lửa trên trạm mục tiêu được cấu hình qua PowerShell:
- **Kích hoạt dịch vụ:** Dịch vụ SMB (`LanmanServer`) đặt chế độ khởi động tự động (`Automatic`) và đang chạy (`Running`). Dịch vụ lắng nghe trên TCP 445 (Direct-hosted SMB) và TCP 139 (NetBIOS Session Service qua TCP/IP) [3].
- **Trạng thái giao thức:** Cả SMBv1 và SMBv2 đều được bật (`EnableSMB1Protocol = True`, `EnableSMB2Protocol = True`), tính năng hệ thống `FS-SMB1` được cài đặt đầy đủ.
- **Tường lửa:** Windows Firewall bật (`Enabled`), tạo luật Inbound cho phép TCP 139 và TCP 445 từ `192.168.56.10`, ngăn chặn truy cập ngoài phạm vi kiểm thử.

### 2.2.5. Kiểm tra bản vá MS17-010 và tạo snapshot
Trước khi thực hiện demo, hiện trạng an ninh trạm mục tiêu được kiểm tra nghiêm ngặt:
- **Kiểm tra bản vá:** Lệnh `Get-HotFix` trên PowerShell xác nhận không ghi nhận các bản vá KB4012213, KB4012216 hoặc các bản cập nhật thay thế trong danh mục đối chiếu [4].
- **Xác thực driver nhân:** Phiên bản driver `srv.sys` tại `C:\Windows\System32\drivers\srv.sys` đạt `6.3.9600.16421`, thấp hơn ngưỡng phiên bản đã cập nhật tối thiểu `6.3.9600.18604` [5], xác nhận hệ thống ở trạng thái chưa vá (`UNPATCHED`).
- **Mốc khôi phục:** Thiết lập snapshot `Before Demo` trên cả hai máy ảo VirtualBox để giữ làm mốc phục hồi khi cần đưa môi trường trở về baseline trước khi đổi biến can thiệp.

## 2.3. Kịch bản Demo 1 — Khảo sát dịch vụ SMB bằng Nmap

### 2.3.1. Mục tiêu và phạm vi
Kịch bản Demo 1 tập trung khảo sát bề mặt dịch vụ SMB từ góc độ người đánh giá an ninh:
- **Mục tiêu:** Xác định trạng thái socket trên cổng TCP 139 và TCP 445, nhận diện phiên bản dịch vụ và các dialect SMB được máy chủ hỗ trợ.
- **Phạm vi:** Giới hạn trong các kỹ thuật quét phi xâm nhập, không gửi payload khai thác, dừng lại sau khi lưu kết quả và không gây gián đoạn máy mục tiêu.

### 2.3.2. Quy trình và các lệnh thực hiện
Quy trình khảo sát của Demo 1 gồm 6 bước kỹ thuật canonical trên trạm Kali Linux:

- **Bước 1 (B1): Kiểm tra cấu hình IP và bảng định tuyến của trạm kiểm thử:**
```bash
ip addr show eth0
ip route
```
Thao tác này xác nhận giao diện mạng `eth0` đã nhận đúng địa chỉ IP `192.168.56.10/24` và bảng định tuyến trực tiếp trong subnet mà không có gateway ngoài ý muốn.

- **Bước 2 (B2): Quét phát hiện các trạm hoạt động trong toàn bộ subnet:**
```bash
nmap -sn 192.168.56.0/24 -oA demo1_b2_subnet_discovery
```
Tùy chọn `-sn` thực hiện host discovery mà không quét cổng, ghi nhận danh sách các máy trạm đang phản hồi trong dải mạng.

- **Bước 3 (B3): Xác nhận riêng khả năng phản hồi của trạm mục tiêu:**
```bash
nmap -sn 192.168.56.20 -oA demo1_b3_target_alive
```
Bước này kiểm tra độc lập tính sẵn sàng của riêng máy mục tiêu `192.168.56.20` trước khi tiến hành các phép đo dịch vụ.

- **Bước 4 (B4): Quét trạng thái cổng TCP 139 và TCP 445** bằng kỹ thuật TCP SYN [6]:
```bash
nmap -sS -p139,445 -Pn --reason -oA demo1_b4_smb_ports 192.168.56.20
```

- **Bước 5 (B5): Nhận diện dịch vụ và phiên bản:**
```bash
nmap -sV -p139,445 -Pn -oA demo1_b5_smb_version 192.168.56.20
```

- **Bước 6 (B6): Khảo sát đặc trưng an toàn giao thức SMB qua 4 kịch bản NSE an toàn** (`smb-protocols` [7], `smb-os-discovery`, `smb2-security-mode` [8], `smb2-capabilities`):
```bash
nmap -p139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities \
    -Pn -oA demo1_b6_smb_nse 192.168.56.20
```

Các tham số rà quét chính gồm `-sn` (phát hiện trạm), `-sS` (quét TCP SYN nửa mở), `-sV` (nhận diện dịch vụ) và `-p139,445` (chỉ định cổng SMB). Tùy chọn `-Pn` giúp bỏ qua ping ICMP, `--reason` hiển thị cờ phản hồi, `--script` thực thi kịch bản an toàn và `-oA` xuất đồng thời 3 định dạng tệp thô. Quy trình dừng lại sau khi lưu dữ liệu, không thực hiện hành vi khai thác.

### 2.3.3. Nội dung cần quan sát và giới hạn kết luận
Trong quá trình thực hiện Demo 1, người thực nghiệm ghi nhận các trường thông tin:
1. **Trạng thái cổng:** Ghi nhận cờ phản hồi tại trường `REASON` (gói `syn-ack` khẳng định socket mở).
2. **Tên dịch vụ:** Đối soát chuỗi dịch vụ (`microsoft-ds` trên cổng 445 hoặc `netbios-ssn` trên cổng 139).
3. **Danh sách dialect SMB:** Kiểm tra sự hiện diện của `NT LM 0.12` (SMBv1) cùng các dialect SMBv2/v3.
4. **Cấu hình ký số:** Kiểm tra cờ `message_signing` (bắt buộc hay tùy chọn).

*Ranh giới kết luận:* Cổng mở và sự hiện diện của SMBv1 chỉ xác nhận bề mặt dịch vụ đang hoạt động, chưa đủ căn cứ kết luận máy chủ có lỗ hổng (`open != vulnerable`). Kết luận an ninh cần tiếp tục được kiểm chứng ở các bước tiếp theo.

## 2.4. Kịch bản Demo 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE

### 2.4.1. Mục tiêu và điều kiện ban đầu
Kịch bản Demo 2 mở rộng đánh giá an ninh bằng kịch bản NSE để nhận diện dấu hiệu của lỗ hổng MS17-010:
- **Mục tiêu:** Thăm dò phản ứng của máy chủ SMB trước gói tin nghiệp vụ chuẩn hóa của NSE, đối chiếu trạng thái để xác định nguy cơ mà không làm gián đoạn máy chủ.
- **Điều kiện ban đầu:** Hoàn thành Demo 1, xác nhận hai cổng TCP 139 và 445 đang mở, dịch vụ SMB phản hồi và máy ảo đã lưu mốc snapshot `Before Demo`.

### 2.4.2. Quy trình kiểm tra NSE-SMB-01 đến NSE-SMB-04
Quy trình Demo 2 chuẩn hóa thành 4 phép đo tuần tự từ `NSE-SMB-01` đến `NSE-SMB-04`:
1. `NSE-SMB-01`: Quét kiểm tra trạng thái cổng TCP 139 và 445 để xác nhận kênh truyền sẵn sàng.
2. `NSE-SMB-02`: Chạy `smb-protocols` kiểm chứng sự hiện diện của dialect SMBv1 (`NT LM 0.12`).
3. `NSE-SMB-03`: Chạy `smb2-security-mode` xác định trạng thái ký số gói tin SMB.
4. `NSE-SMB-04`: Chạy kịch bản chuyên dụng `smb-vuln-ms17-010` để thăm dò dấu hiệu lỗ hổng:
```bash
nmap -p445 --script smb-vuln-ms17-010 -Pn -oA demo2_ms17010 192.168.56.20
```

Về cơ chế kỹ thuật, kịch bản `smb-vuln-ms17-010` kết nối pipe `IPC$`, gửi gói tin giao dịch SMB (transaction) tới mã định danh tệp FID 0 và phân tích mã lỗi trả về từ máy chủ [9]. Nếu máy chủ chưa được cập nhật bản vá, nó phản hồi mã lỗi đặc trưng `STATUS_INSUFF_SERVER_RESOURCES`, qua đó Nmap ghi nhận dấu hiệu lỗ hổng.

### 2.4.3. Đối chiếu với trạng thái bản vá và giới hạn kết luận
Quy trình đánh giá thiết lập nguyên tắc đối chiếu trên hai trục thông tin độc lập:
1. **Trục tín hiệu từ xa (Remote Signal):** Kết quả phân loại từ kịch bản NSE. Nếu kịch bản cung cấp kết luận sử dụng được thì ghi nhận theo đúng kết quả đó; nếu không đủ dữ liệu kết luận thì ghi nhận `UNKNOWN / NO USABLE SCRIPT RESULT`.
2. **Trục trạng thái nội bộ (Local Ground Truth):** Kiểm tra trực tiếp trên Windows Server qua phiên bản driver `srv.sys` và danh sách hotfix từ `Get-HotFix`.

*Ranh giới suy luận an toàn:*
- Kết quả từ xa không xác định không đồng nghĩa máy chủ an toàn (`UNKNOWN != SAFE`).
- Trạng thái nội bộ của hệ điều hành được xác định độc lập với kết quả quét mạng từ xa.

## 2.5. Kiểm thử các biện pháp giảm thiểu

### 2.5.1. Nguyên tắc kiểm thử trước và sau can thiệp
Để đánh giá hiệu quả phòng thủ, đồ án áp dụng phương pháp kiểm thử vi sai theo nguyên tắc trước và sau can thiệp (before-after test).

Quy trình tuân thủ 3 nguyên tắc:
1. **Tính đơn biến:** Chỉ áp dụng một biện pháp can thiệp tại mỗi ca thử; giữ nguyên phần cứng, hệ điều hành và dải IP.
2. **Quy chuẩn bộ phép đo:** Sử dụng cùng một tập hợp lệnh Nmap và kịch bản NSE để đối chiếu.
3. **Mốc phục hồi trạng thái:** Snapshot `Before Demo` được giữ làm mốc phục hồi khi cần đưa môi trường trở về baseline trước khi đổi biến can thiệp.

Bảng 2.2. Ma trận kiểm thử vi sai các giải pháp an toàn dịch vụ SMB

| Trường hợp | Tên giải pháp | Tầng tác động | Mục tiêu can thiệp | Nội dung cần kiểm tra lại |
| :--- | :--- | :--- | :--- | :--- |
| **Baseline** | Chưa can thiệp | Không | Giữ nguyên hiện trạng RTM | Kiểm tra trạng thái cổng TCP 139/445, SMB dialect, tín hiệu NSE và trạng thái bản vá nội bộ. |
| **Case B** | Vô hiệu hóa SMBv1 | Tầng dịch vụ OS | Tắt giao thức kế thừa SMBv1 [10] | Kiểm tra SMBv1 còn xuất hiện hay không, SMB2/3 còn thương lượng không, trạng thái bản vá nội bộ có thay đổi hay không. |
| **Case C** | Tường lửa pfSense Bridge | Tầng mạng (L2/L3) | Chặn cổng TCP 139, 445 [11] | Kiểm tra khả năng tiếp cận TCP 139/445 từ Kali Linux, kiểm tra nhật ký tường lửa có ghi nhận luật chặn không, trạng thái nội bộ Windows có thay đổi hay không. |
| **Case A** | Cập nhật bản vá KB4012213 | Tầng nhân OS (Driver) | Thay đổi trạng thái bản vá trong driver `srv.sys` [4], [5] | Tham chiếu lý thuyết / Không đo đạc trực tiếp (`REFERENCE ONLY / NOT MEASURED`). |

### 2.5.2. Case B — Vô hiệu hóa SMBv1
Biện pháp giảm thiểu thứ nhất (Case B) là làm cứng giao thức (Protocol Hardening) ở tầng ứng dụng theo khuyến nghị của Microsoft [10], nhằm vô hiệu hóa SMBv1 và duy trì chia sẻ tệp qua SMBv2/SMBv3.

- **Thao tác can thiệp:** Trên Windows Server 2012 R2, mở PowerShell Administrator và thực thi câu lệnh:
```powershell
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
```
- **Xác thực cấu hình:** Kiểm tra lại trạng thái cấu hình dịch vụ SMB bằng lệnh:
```powershell
Get-SmbServerConfiguration | Select-Object EnableSMB1Protocol, EnableSMB2Protocol
```
- **Kiểm thử vi sai:** Sau khi tắt SMBv1, thực hiện lại phép kiểm tra protocol (`smb-protocols`) và kịch bản MS17-010 (`smb-vuln-ms17-010`) từ Kali Linux để so sánh sự thay đổi của các dialect và tín hiệu phản hồi.
- **Ranh giới an ninh:** Tắt SMBv1 làm giảm bề mặt giao thức cũ nhưng không đồng nghĩa Windows đã được vá (`SMBv1 disabled != PATCHED`). Phiên bản driver `srv.sys` vẫn giữ nguyên trạng thái cũ nếu chưa áp dụng bản vá.

### 2.5.3. Case C — Kiểm soát TCP 139/445 bằng pfSense
Biện pháp giảm thiểu thứ hai (Case C) đại diện cho giải pháp kiểm soát truy cập và phân đoạn mạng bằng tường lửa chuyên dụng theo chuẩn NIST SP 800-41 Rev. 1 [11].

- **Mô hình triển khai:** Máy ảo pfSense phiên bản CE 2.9.0 được chèn giữa Kali Linux và Windows Server theo kiến trúc cầu nối trong suốt (Transparent Bridge) ở tầng L2. Cấu hình này cho phép lọc gói tin mà không làm thay đổi dải IP `192.168.56.0/24` của hai đầu cuối.
- **Cấu hình thông số nhân:** Trên pfSense, các tham số hệ thống (`System Tunables`) bắt buộc thiết lập:
  - `net.link.bridge.pfil_member = 1`: Bật lọc gói trên giao diện thành viên bridge.
  - `net.link.bridge.pfil_bridge = 0`: Tắt lọc gói trên giao diện bridge tổng để tránh trùng lặp.
  - `net.link.bridge.pfil_onlyip = 1`: Chỉ cho phép lưu lượng IP đi qua cầu nối.
- **Luật kiểm soát:** Thiết lập luật chặn (`Block`) lưu lượng từ địa chỉ nguồn `192.168.56.10` tới đích `192.168.56.20` trên các cổng TCP 139 và TCP 445, đồng thời kích hoạt ghi nhật ký (`Log packets`).
- **Kiểm thử vi sai:** Sau khi áp dụng luật, quét lại TCP 139/445 từ Kali Linux để kiểm tra sự thay đổi khả năng tiếp cận dịch vụ qua tường lửa.
- **Ranh giới an ninh:** Trạng thái bị lọc trên đường truyền không đồng nghĩa máy chủ nội bộ đã được vá lỗi (`FILTERED != PATCHED`).

### 2.5.4. Vai trò của cập nhật bản vá
Cập nhật bản vá là biện pháp trực tiếp thay đổi trạng thái bản vá của hệ điều hành. Đối với Windows Server 2012 R2, các gói cập nhật áp dụng gồm KB4012213, KB4012216 hoặc các bản cập nhật thay thế (superseding update) [4], [5]. Việc cập nhật giúp nâng phiên bản driver `srv.sys` đạt hoặc vượt ngưỡng phiên bản đã cập nhật tối thiểu `6.3.9600.18604` (minimum updated version). Bộ evidence hiện hành không có kịch bản thực nghiệm Case A hoàn chỉnh, do đó Case A đóng vai trò đối chứng lý thuyết để làm rõ sự khác biệt giữa can thiệp tầng nhân, can thiệp cấu hình dịch vụ (Case B) và kiểm soát mạng (Case C).

## 2.6. Thu thập dữ liệu phục vụ đánh giá

### 2.6.1. Log và ảnh chụp thực nghiệm
Để phục vụ phân tích chi tiết và bảo đảm tính minh chứng khoa học ở Chương 3, dữ liệu thực nghiệm được lưu trữ theo các định dạng chuẩn:

1. **Tập tin nhật ký Nmap (`-oA`):** Mọi lệnh quét bắt buộc dùng tham số `-oA <filename>` để xuất ra 3 định dạng đồng thời:
   - Tệp văn bản chuẩn (`.nmap`): Kết quả bảng trực quan, dễ đọc và trích dẫn.
   - Tệp máy đọc (`.xml`): Lưu trữ cấu trúc chi tiết, phục vụ trích xuất tự động qua script.
   - Tệp Grep (`.gnmap`): Hỗ trợ lọc nhanh theo dòng lệnh.
2. **Bằng chứng trực quan và trạng thái hệ thống:** Lưu trữ ảnh chụp màn hình máy ảo VirtualBox và terminal, kết quả lệnh PowerShell kiểm tra trạng thái nội bộ Windows (`Get-HotFix`, `Get-SmbServerConfiguration`), cùng cấu hình luật và nhật ký chặn gói của pfSense ở Case C.

### 2.6.2. Nguyên tắc diễn giải kết quả
Quá trình diễn giải dữ liệu thực nghiệm ở Chương 3 bắt buộc tuân thủ 5 nguyên tắc suy luận an toàn cốt lõi:

1. `445 open != vulnerable`: Cổng TCP 139/445 mở chỉ xác nhận socket đang lắng nghe, chưa đủ căn cứ kết luận máy chủ có điểm yếu an ninh.
2. `SMBv1 enabled != MS17-010 confirmed`: Bật SMBv1 chỉ là điều kiện giao thức cần; nguy cơ bị tổn thương phụ thuộc vào việc nhân hệ điều hành đã được vá lỗi hay chưa.
3. `UNKNOWN != SAFE`: Khi kịch bản NSE trả về kết quả không xác định do cơ chế phản hồi hoặc điều kiện mạng, hệ thống không thể tự động được coi là an toàn.
4. `FILTERED != PATCHED`: Trạng thái cổng bị lọc do tường lửa chặn gói chỉ phản ánh lưu lượng bị chặn trên đường truyền, không đại diện cho trạng thái bản vá nội bộ.
5. `SMBv1 disabled != PATCHED`: Vô hiệu hóa SMBv1 chỉ đóng tính năng ở tầng dịch vụ, không thay đổi mã nhị phân driver nhân `srv.sys`.

## 2.7. Tổng kết chương

Chương 2 đã hoàn thành toàn bộ công tác xây dựng mô hình thực nghiệm và chuẩn hóa các kịch bản demo phục vụ khảo sát an toàn dịch vụ SMB cùng lỗ hổng MS17-010. Mạng ảo Host-Only trên Oracle VM VirtualBox 7.2.20 r170876 thiết lập môi trường kiểm thử cô lập và có khả năng tái lập nhờ snapshot `Before Demo`.

Thông số kỹ thuật trạm kiểm thử Kali Linux và máy mục tiêu Windows Server 2012 R2 đã được chuẩn hóa. Đồ án xây dựng quy trình 6 bước chi tiết cho Kịch bản Demo 1 và 4 phép đo cho Kịch bản Demo 2. Đồng thời, đồ án thiết lập phương pháp kiểm thử vi sai trước và sau can thiệp cho hai giải pháp giảm thiểu gồm vô hiệu hóa SMBv1 và tường lửa pfSense CE 2.9.0.

Hệ thống dữ liệu thô đa định dạng cùng 5 nguyên tắc diễn giải an toàn tạo lập nền tảng khoa học vững chắc. Đây là cơ sở để Chương 3 tiến hành phân tích số liệu đo đạc thực tế và thảo luận chuyên sâu về hiệu quả của các giải pháp phòng thủ.
