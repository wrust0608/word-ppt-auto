# CHƯƠNG 2. THIẾT KẾ VÀ TRIỂN KHAI MÔ HÌNH THỰC NGHIỆM

Chương 2 thiết kế môi trường kiểm thử SMB dựa trên cơ sở lý thuyết ở Chương 1. Mô hình gồm các phân vùng mạng, chuỗi cấu hình phòng thủ và điểm thu thập dữ liệu để xác định điều kiện của đường tấn công đang xét. Client hợp lệ được bố trí riêng nhằm kiểm tra ảnh hưởng của biện pháp phòng thủ lên hoạt động chia sẻ tệp.

---

## 2.1. YÊU CẦU VÀ NGUYÊN TẮC THIẾT KẾ MÔ HÌNH THỰC NGHIỆM

### 2.1.1. Nguyên tắc đạo đức nghề nghiệp và phạm vi kiểm thử được ủy quyền

Phạm vi kiểm thử gồm các máy ảo do nhóm quản lý trong lab; địa chỉ mục tiêu, tác vụ được phép và điều kiện dừng phải được xác định trước theo nguyên tắc lập kế hoạch kiểm thử của NIST [1]. Chương này thiết kế phương pháp, chưa trình bày kết quả demo. Các thao tác có khả năng gây mất ổn định chỉ được xét trên mục tiêu đã lưu điểm khôi phục và dữ liệu thử nghiệm. Khi xảy ra sự cố, lượt thử được dừng để lưu bằng chứng và phục hồi, thay vì tiếp tục thử trên trạng thái đã bị tác động.

### 2.1.2. Yêu cầu về tính cô lập và kiểm soát rủi ro mạng

Tính cô lập phải được xác định bằng cấu hình đường kết nối. Các card mạng lab chỉ nối vào hệ thống chuyển mạch ảo nội bộ; không dùng kết nối chuyển tiếp tới mạng cơ sở đào tạo hoặc Internet thật. Gateway của các máy trỏ về tường lửa lab, địa chỉ được quản lý riêng và WAN chỉ là mạng mô phỏng. Trước lượt thử cần kiểm tra tuyến và các card đang hoạt động, vì một card bổ sung có thể tạo đường kết nối ngoài thiết kế. Log và dữ liệu phát sinh được giữ trong phạm vi nghiên cứu.

Tường lửa vừa thực thi chính sách giữa các phân vùng vừa tạo điểm quan sát lưu lượng. Theo nguyên tắc chính sách lọc của NIST, quy tắc cần bám nguồn, đích và dịch vụ được phép [2]. Trong lab, yêu cầu này được cụ thể hóa bằng hai nguồn truy cập riêng: trạm kiểm thử và Client nghiệp vụ. Cấu hình cô lập giúp giới hạn phạm vi tác động; snapshot phục vụ phục hồi mục tiêu khi phép thử gây sự cố.

### 2.1.3. Mô hình chuỗi điều kiện của đường tấn công (Causal-Chain Model)

Đường tấn công được phân thành khả năng tiếp cận mạng ($R$), phản hồi SMB ($S$), chấp nhận SMBv1 ($D$), trạng thái lỗ hổng ($V$), thực thi mã thành công ($E$) và kênh kết nối ngược ($C$). Trong cấu hình lab, thực thi thành công cần:

$$E \implies R \land S \land D \land V$$

Chiều suy luận ngược không được bảo đảm: các điều kiện cần cùng thỏa mãn chưa chứng minh $E$, vì bước thực thi còn phụ thuộc vào công cụ và trạng thái mục tiêu. Kịch bản dùng kết nối ngược còn cần $C$ để có phiên tương tác. Không dùng kết quả $E$ làm tiền điều kiện để suy ra chính nó.

$R$ được xét bằng lưu lượng và chính sách; $S$ cần phản hồi SMB, còn $D$ cần phản hồi thương lượng. $V$ được đánh giá bằng dấu hiệu thăm dò cùng build, bản vá và cấu hình. $E,C$ cần bằng chứng thực thi và kết nối tương ứng [3], [4]. Ví dụ giả định, Server chỉ chấp nhận SMBv2 có thể thỏa $R,S$ nhưng không thỏa $D$. Server chấp nhận SMBv1 nhưng không tạo phiên chưa chỉ ra lỗi ở thực thi hay đường ngược. Tách các điều kiện giúp phân biệt hai kết quả này.

Mỗi điều kiện được ghi `True`, `False` hoặc `Unknown`; giá trị cuối chỉ phần chưa đủ dữ liệu. Khi bước trước bị chặn, không gán mọi bước sau bằng `False`. Một điều kiện cần được xác nhận không thỏa mãn cho phép kết luận đường tấn công đang xét bị chặn tại cấu hình và nguồn kiểm tra đó.

---

## 2.2. THIẾT KẾ KIẾN TRÚC MẠNG LAB DOANH NGHIỆP MÔ PHỎNG

### 2.2.1. Cấu trúc mạng phân đoạn 3 VLAN

Mô hình tách Server tại VLAN 10, trạm kiểm thử tại VLAN 20 và Client hợp lệ tại VLAN 30; địa chỉ chi tiết ở Bảng 2.1. Hai trạm truy cập phục vụ hai góc quan sát trên cùng Server: nguồn kiểm thử có tiếp cận được không và nguồn nghiệp vụ còn sử dụng tài nguyên được không. Nếu chỉ có một nguồn, bị từ chối truy cập sẽ khó phân biệt với mất dịch vụ. VLAN tạo sự phân chia mạng; kiểm soát giữa các vùng phụ thuộc đường định tuyến và chính sách tường lửa [2].

### 2.2.2. Nguyên lý Inter-VLAN Routing và Firewall Inspection

Firewall/UTM là điểm định tuyến giữa các VLAN (Inter-VLAN Routing), với các địa chỉ gateway `192.168.10.1`, `192.168.20.1` và `192.168.30.1`. Switch chỉ chuyển mạch lớp 2, không tạo tuyến thay thế giữa các phân vùng. Các chính sách được kiểm tra tại điểm định tuyến này và log được thu tại đây. Mạng WAN mô phỏng `172.16.0.0/24` không có đường kết nối tới Internet thật.

Kiểm tra trạng thái kết nối (Stateful Inspection) phân biệt một kết nối mới với các gói thuộc kết nối đã được chấp nhận. NIST mô tả bảng trạng thái dùng thông tin địa chỉ, cổng và trạng thái kết nối để hỗ trợ quyết định lọc [2]. Trong lab, phản hồi từ Server trong kết nối SMB tới cổng 445 cần được phân biệt với một kết nối TCP mới do Server khởi tạo tới trạm kiểm thử. Cho phép phản hồi của kết nối SMB không tự đồng nghĩa với cho phép kết nối mới đó.

Ở $S_0$, $S_1$ và $S_2$, thiết kế cho phép trạm kiểm thử tại VLAN 20 truy cập TCP 139/445 của mục tiêu, đồng thời có quy tắc riêng cho kênh thử nghiệm từ mục tiêu về `192.168.20.10:4444`. Quy tắc sau phục vụ đánh giá $C$ khi dùng kết nối ngược, nên phải được ghi riêng với quy tắc truy cập SMB. Nếu có bằng chứng thực thi nhưng kết nối ngược bị chặn, nguyên nhân không tạo được phiên tương tác có thể nằm ở đường trở về; không được dùng kết quả này để xác nhận mục tiêu đã vá.

Ở $S_3$, quy tắc chặn và ghi log được áp dụng cho lưu lượng TCP 139/445 từ VLAN 20 tới VLAN 10, còn truy cập TCP 445 từ VLAN 30 vẫn được cho phép. Khi xác nhận lưu lượng kiểm thử bị chặn tại chiều vào, đề tài có thể kết luận đường tấn công này bị gián đoạn ở $R$. Không từ đó suy ra quy tắc chiều ra đã chặn mọi kết nối ngược: hiệu lực của quy tắc chiều ra là câu hỏi khác và cần phép kiểm tra riêng nếu được đưa vào phạm vi đánh giá.

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
| **Attacker-Kali** | Pentest Subnet | 20 | `192.168.20.10/24` | `192.168.20.1` | Cổng 4444 chỉ mở khi kiểm tra kênh ngược trong lab | Trạm phát sinh lưu lượng kiểm thử (Nmap, Metasploit) |
| **Target-Win7** | Server Subnet | 10 | `192.168.10.20/24` | `192.168.10.1` | TCP 445 (`microsoft-ds`), TCP 139 (`netbios-ssn`) | Đối tượng kiểm thử đơn biến qua 4 trạng thái snapshot |
| **Client-WinUser**| User Subnet | 30 | `192.168.30.50/24` | `192.168.30.1` | Client SMB Workstation | Đối chứng nghiệp vụ dương tính (Positive Business Control) |

---

## 2.3. MÔ HÌNH MÁY TRẠNG THÁI ĐƠN BIẾN (SINGLE-VARIABLE CAUSAL STATE MACHINE)

### 2.3.1. Thiết kế chuỗi 4 trạng thái Snapshot trên cùng một hệ thống mục tiêu

Đề tài dùng một máy ảo Windows 7 SP1 x64 qua chuỗi $S_0 \to S_1 \to S_2 \to S_3$. Cách này giữ chung hệ điều hành và cấu hình nền, rồi bổ sung từng biện pháp theo thứ tự. Mỗi trạng thái được lưu snapshot và kèm hồ sơ build, bản vá, SMBv1, quy tắc mạng. Trước lượt thử cần xác nhận lại hồ sơ; snapshot không tự bảo đảm mọi hoạt động nền hoặc bố cục bộ nhớ đều giống nhau.

Ở $S_0$, mục tiêu dự kiến là Windows 7 SP1 x64 Build 7601, chưa vá MS17-010, SMBv1 bật và cho phép trạm kiểm thử truy cập TCP 139/445. Cần đối chiếu cả cập nhật thay thế; thiếu riêng KB4012212 chưa đủ để xác nhận chưa vá [5]. $S_1$ bổ sung KB4012212 phù hợp, giữ SMBv1 và chính sách mạng để kiểm tra thay đổi ở $V$. Nếu cổng đóng sau cập nhật, phải giải thích trước khi quy kết phản hồi thăm dò cho bản vá.

$S_2$ giữ bản vá và vô hiệu hóa Server SMBv1 theo hướng dẫn cho phiên bản Windows tương ứng [6]. Thương lượng mới kiểm tra thay đổi ở $D$, tác vụ Client kiểm tra khả năng sử dụng SMBv2. $S_3$ giữ cấu hình đó, chặn TCP 139/445 từ VLAN 20 tới VLAN 10 và cho phép TCP 445 từ VLAN 30. Lưu lượng cùng log kiểm tra thay đổi ở $R$; nguồn hợp lệ kiểm tra riêng chức năng Server.

Chuỗi này có tính tích lũy: $S_2$ có cả bản vá và việc tắt SMBv1, còn $S_3$ có thêm phân đoạn mạng. Do đó, so sánh việc tạo phiên giữa $S_0$ và $S_3$ không xác định được đóng góp riêng của từng biện pháp. Các chuyển tiếp liền kề chỉ hỗ trợ phân tích khi phép đo tương ứng xác nhận điều kiện đã thay đổi: bản vá và dấu hiệu tại $S_1$, phiên bản tại $S_2$, đường tiếp cận tại $S_3$. Thiết kế chưa bao gồm mọi tổ hợp phòng thủ, nên không dùng nó để suy ra hiệu quả độc lập hoặc tương tác của mọi tổ hợp.

### 2.3.2. Vai trò đối chứng nghiệp vụ dương tính của trạm Client tại VLAN 30

Client tại VLAN 30 là đối chứng cho khả năng phục vụ tác vụ hợp lệ. Ở mỗi trạng thái, `Client-WinUser` (`192.168.30.50`) thiết lập kết nối tới `\192.168.10.20\ShareData` bằng tài khoản được cấp quyền, đọc tệp thử nghiệm, ghi trong phạm vi cho phép và đọc lại để đối chiếu nội dung. Đọc và ghi được ghi riêng vì quyền đọc chưa chắc bao gồm quyền ghi. Phiên bản SMB được xác định từ dữ liệu kết nối; chỉ dùng `Get-SmbConnection` khi Windows Client thực tế hỗ trợ lệnh này.

Trước lượt sau thay đổi cấu hình, Client phải đóng phiên cũ và thiết lập kết nối mới. Xem một tệp đã mở hoặc dữ liệu còn trong bộ nhớ đệm chưa chứng minh Server đang phục vụ yêu cầu mới. Nếu VLAN 20 bị từ chối nhưng Client hợp lệ vẫn hoàn thành tác vụ, kết quả phù hợp với mục tiêu hạn chế theo nguồn. Nếu cả hai đều thất bại, phải kiểm tra Server, chính sách mạng và xác thực. Đối chứng đo chức năng chia sẻ tệp trong lab, chưa đại diện cho mọi ứng dụng hoặc tải của một tổ chức.

*Bảng 2.2: Trạng thái dự kiến và bằng chứng cần thu*

| Trạng thái | Thay đổi cấu hình | Phép kiểm tra chính | Đối chứng Client |
|---|---|---|---|
| $S_0$ | Cấu hình gốc | Đường mạng, SMBv1, bản vá, dấu hiệu và tác động | Thương lượng, đọc, ghi |
| $S_1$ | Bổ sung bản vá | Cập nhật và phản hồi thăm dò | SMBv2, đọc, ghi |
| $S_2$ | Giữ vá, tắt SMBv1 | Phản hồi thương lượng | SMBv2, đọc, ghi |
| $S_3$ | Giữ $S_2$, chặn VLAN 20 | Lưu lượng và log theo nguồn | SMBv2, đọc, ghi |

Các giá trị là thiết kế, chưa phải số đo; dữ liệu thật được lưu ở Bảng 2.4. Thiếu bằng chứng vẫn ghi `[CẦN DỮ LIỆU]`.

### 2.3.3. Kiểm chứng vị trí chặn đường tấn công và khả năng phục vụ Client

Kết luận về phòng thủ cần kết hợp điều kiện đã thay đổi với tác vụ hợp lệ. “Không tạo được phiên thử nghiệm” chưa phân biệt bản vá, từ chối giao thức, chặn mạng, lỗi công cụ hay sự cố mục tiêu. Do chuỗi có tính tích lũy, các trạng thái sau phải được đọc qua phép đo riêng ở Bảng 2.2; kết quả cuối nêu điều kiện đã xác nhận và phần còn chưa xác định.

---

## 2.4. PHƯƠNG PHÁP LUẬN VÀ CHUẨN HÓA KỸ THUẬT THEO MÔ HÌNH BẠCH HỘP

Năm kỹ thuật có nhiệm vụ khác nhau: khảo sát đường tiếp cận, kiểm tra phiên bản, nhận diện dấu hiệu chưa vá, đối chiếu công cụ và xác minh tác động. Mỗi kỹ thuật giữ mười thành phần theo hợp đồng chương; Metasploit được dùng theo vai trò scanner hoặc module khai thác [7]. Phần diễn giải nêu cách dùng kết quả, còn bảng ghi đầu vào, tiêu chí và ranh giới suy luận để đối chiếu giữa các lượt.

### 2.4.1. Kỹ thuật 1: Khảo sát tiếp cận và nhận diện dịch vụ (TCP SYN Scan & Service Detection)

Phép khảo sát được dùng để đánh giá đường kết nối nên không được giả định trước $R = \text{True}$. Quét SYN xét phản hồi ở tầng TCP; nhận diện `-sV` tiếp tục xét phản hồi dịch vụ. Hai bước trả lời hai câu hỏi khác nhau. SYN-ACK cho thấy cổng có phản hồi, còn việc Server xử lý SMB cần bằng chứng ứng dụng [3].

| Thành phần | Thiết kế phép kiểm tra |
|---|---|
| Input | `nmap -sS -sV -p 139,445 -n -Pn --reason 192.168.10.20` |
| Preconditions | Mục tiêu thuộc lab; trạm có quyền quét SYN và cấu hình mạng đã ghi. |
| Internal Mechanism | SYN-ACK tương ứng `open`, RST tương ứng `closed`; thiếu phản hồi hoặc một số mã ICMP tương ứng `filtered` [3]. |
| Observation Point | Lưu lượng tại Kali, tường lửa và mục tiêu khi cần xác định đường gói tin. |
| Success Criterion | Có phản hồi cổng và kết quả nhận diện phù hợp SMB; lưu riêng hai kết quả. |
| Failure Criterion | `closed` hoặc `filtered`; chưa quy nguyên nhân cho tường lửa nếu thiếu đối chứng. |
| Output / Evidence | Output văn bản/XML, `reason`, lưu lượng của lượt tương ứng. |
| Inference Boundary | Hỗ trợ đánh giá tiếp cận; $S$ cần phản hồi SMB. Chưa kết luận phiên bản hoặc lỗ hổng. |
| Limitation | Mất phản hồi chưa phân biệt mất gói, chặn mạng hay máy đích dừng. |
| Defense Breakpoint | Quy tắc mạng hướng tới $R$; kiểm chứng ở $S_3$. |

### 2.4.2. Kỹ thuật 2: Thăm dò phiên bản SMB (Dialect Negotiation Probe)

Phép thương lượng trả lời Server có chấp nhận SMBv1 hay không. Script gọi `smb.list_dialects` và xuất danh sách hỗ trợ; mã nguồn còn có nhánh không nhận được phiên bản nào và lưu ý khả năng phản hồi bị chặn [8]. Vì vậy, không có output khác với nhận phản hồi hợp lệ chỉ chấp nhận SMBv2. Cũng không mô tả mọi phiên bản như các chuỗi trong một yêu cầu SMBv1 duy nhất.

| Thành phần | Thiết kế phép kiểm tra |
|---|---|
| Input | `nmap -p 445 --script smb-protocols 192.168.10.20` |
| Preconditions | Đã xác định đường kết nối và phản hồi SMB để diễn giải kết quả phiên bản. |
| Internal Mechanism | Dùng thư viện SMB để nhận diện các phiên bản được chấp nhận [8]. |
| Observation Point | Output script và yêu cầu/phản hồi thương lượng trong lưu lượng. |
| Success Criterion | Có bằng chứng Server chấp nhận `NT LM 0.12`, tương ứng $D = \text{True}$. |
| Failure Criterion | Chỉ chấp nhận SMBv2 trở lên: $D = \text{False}$; thiếu phản hồi: `Unknown`. |
| Output / Evidence | Danh sách hỗ trợ, lỗi và phản hồi thương lượng tương ứng. |
| Inference Boundary | Xác định giao thức được chấp nhận; chưa xác nhận MS17-010. |
| Limitation | Phụ thuộc khả năng nhận phản hồi; phải đọc kèm lỗi. |
| Defense Breakpoint | Vô hiệu hóa SMBv1 hướng tới $D$; kiểm chứng ở $S_2$. |

### 2.4.3. Kỹ thuật 3: Phát hiện dấu hiệu MS17-010 bằng Nmap NSE

Phép thăm dò cần đi tới `IPC$` và nhận phản hồi Transaction trước khi có thể đánh giá dấu hiệu. Các nhánh mã trạng thái được giải thích tại Mục 1.3.3. Trong mã nguồn hiện hành, nhánh không hoàn tất phép kiểm tra cũng có thể mang nhãn `NOT_VULN`, nên phải lưu lỗi và ghi `Unknown` khi chưa đủ dữ liệu [4].

| Thành phần | Thiết kế phép kiểm tra |
|---|---|
| Input | `nmap -p 445 --script smb-vuln-ms17-010 -n -Pn 192.168.10.20` |
| Preconditions | Tiếp cận được SMBv1, thiết lập phiên và kết nối `IPC$` theo cấu hình xác thực. |
| Internal Mechanism | Gửi `SMB_COM_TRANSACTION` với `PeekNamedPipe` và đọc NT Status [4]. |
| Observation Point | Output/lỗi NSE và phản hồi SMB tại Kali, mục tiêu. |
| Success Criterion | Nhận phản hồi hợp lệ `0xC0000205`, phù hợp dấu hiệu chưa vá. |
| Failure Criterion | `0xC0000022`/`0xC0000008` trong phản hồi thăm dò phù hợp nhánh đã vá; không hoàn tất: `Unknown`. |
| Output / Evidence | Output, lỗi, mã trạng thái, dữ liệu cấu hình và bản vá để đối chiếu. |
| Inference Boundary | Dấu hiệu ở Cấp độ 3; nhãn CVE-2017-0143 của script không xác nhận riêng CVE-2017-0144. |
| Limitation | Xác thực hoặc lỗi mạng có thể ngăn phép thăm dò; nhóm `safe` không bảo đảm không tác động. |
| Defense Breakpoint | Bản vá hướng tới $V$; chưa được coi là đã đạt nếu chỉ thiếu output. |

### 2.4.4. Kỹ thuật 4: Đối chiếu bằng Metasploit Auxiliary Scanner

Scanner phụ trợ cũng kết nối `IPC$`, gửi yêu cầu và xét `STATUS_INSUFF_SERVER_RESOURCES` [9]. So sánh với NSE có thể phát hiện khác biệt do cấu hình hoặc xử lý phản hồi, nhưng hai công cụ cùng dựa vào một dấu hiệu chưa tạo đối chứng độc lập về bản vá. Đối chứng khác loại là trạng thái cập nhật trên mục tiêu và dữ liệu mạng.

| Thành phần | Thiết kế phép kiểm tra |
|---|---|
| Input | Module `auxiliary/scanner/smb/smb_ms17_010`, mục tiêu `192.168.10.20`. |
| Preconditions | Tiếp cận SMBv1 và thiết lập được phiên tới `IPC$`. |
| Internal Mechanism | Thăm dò FID 0 và phân loại mã trạng thái [9]. |
| Observation Point | Console và lưu lượng của lượt scanner. |
| Success Criterion | Phản hồi phù hợp dấu hiệu chưa vá và được module nhận diện. |
| Failure Criterion | Phản hồi phù hợp nhánh không thấy dấu hiệu; lỗi kết nối hoặc không nhận diện: chưa đủ kết luận. |
| Output / Evidence | Log đầy đủ, mã phản hồi và cấu hình tùy chọn module. |
| Inference Boundary | Đối chiếu Cấp độ 3, chưa xác nhận thực thi mã. |
| Limitation | Kết quả chịu ảnh hưởng phiên bản module, xác thực và các tùy chọn kiểm tra bổ sung. |
| Defense Breakpoint | Bản vá hoặc tắt SMBv1 tác động vào $V$ hoặc $D$; phải đối chiếu phép đo riêng. |

### 2.4.5. Kỹ thuật 5: Xác minh tác động trong lab bằng Metasploit Exploit Module

Kỹ thuật này chuyển từ nhận diện dấu hiệu sang kiểm tra tác động quan sát được. Cơ chế FEA và bố trí vùng nhớ đã phân tích tại Mục 1.2.3; ở đây trọng tâm là tiêu chí phân biệt thực thi mã, kênh tương tác và sự cố. Rapid7 ghi nhận module có thể gây mất ổn định hoặc BSOD [10]. Giới hạn một lần thử là quy tắc vận hành của đề tài, không phải bảo đảm an toàn của module.

| Thành phần | Thiết kế phép kiểm tra |
|---|---|
| Input | `exploit/windows/smb/ms17_010_eternalblue`; mục tiêu `192.168.10.20`; trạm nhận kênh thử nghiệm `192.168.20.10:4444`. |
| Preconditions | Đã đối chiếu $R,S,D,V$; đúng cấu hình module; có snapshot và chính sách cho kênh ngược trong lab. |
| Internal Mechanism | Khai thác lỗi FEA kết hợp bố trí vùng nhớ để tìm cách chuyển hướng thực thi [10]. |
| Observation Point | Console, định danh mục tiêu, lưu lượng kênh ngược và trạng thái hệ điều hành. |
| Success Criterion | Có phiên hợp lệ và output lệnh xác minh danh tính, quyền, mục tiêu; không chỉ một thông báo tạo phiên. |
| Failure Criterion | Không có bằng chứng thực thi: chưa đạt Cấp độ 4; có BSOD/reboot/treo: phân loại và lưu bằng chứng sự cố. |
| Output / Evidence | Log lệnh/output, thời điểm, lưu lượng và dấu vết sự cố nếu có. |
| Inference Boundary | `SYSTEM` xác nhận quyền phiên quan sát được, chưa chứng minh kiểm soát toàn bộ nhân hoặc mọi Windows. |
| Limitation | Kênh ngược có thể thất bại riêng; bố cục bộ nhớ và cấu hình ảnh hưởng kết quả. |
| Defense Breakpoint | Đánh giá điều kiện cần bị chặn, chưa quy thất bại riêng cho $V$ khi thiếu dữ liệu. |

Nếu console không tạo được phiên, cần đọc cùng lưu lượng và trạng thái mục tiêu. Không thấy kết nối ngược chưa phân biệt mã chưa thực thi với kênh bị chặn; có BSOD chứng minh sự cố nhưng không chứng minh thực thi thành công. Ngược lại, một phiên trả output `SYSTEM` phải được gắn với đúng mục tiêu và lượt thử. Các chuỗi output nêu trong thiết kế là tiêu chí dự kiến, không phải log đã thu. Sau lượt thử, dừng và kiểm tra trạng thái trước khi khôi phục hoặc tiếp tục; không tự lặp phép khai thác khi chưa phân loại kết quả.

*Bảng 2.3: Bảng đối chiếu các kỹ thuật kiểm thử với các tiền điều kiện và 4 cấp độ trạng thái*

| Kỹ thuật kiểm thử | Công cụ thực thi | Tiền điều kiện kiểm chứng | Cấp độ đối chiếu | Bằng chứng kỹ thuật cốt lõi |
|---|---|:---:|:---:|---|
| **Kỹ thuật 1** | `nmap -sS -sV -p 445` | Khảo sát $R,S$ | **Cấp độ 1** | `SYN-ACK` và phản hồi nhận diện; $S$ cần phản hồi SMB |
| **Kỹ thuật 2** | `nmap --script smb-protocols` | $D$ | **Cấp độ 2** | Phản hồi chấp nhận phương ngữ `NT LM 0.12 (SMBv1)` |
| **Kỹ thuật 3** | `nmap --script smb-vuln-ms17-010` | Dấu hiệu liên quan $V$ | **Cấp độ 3** | `0xC0000205`, cần đối chiếu bản vá/cấu hình |
| **Kỹ thuật 4** | `auxiliary/scanner/smb/smb_ms17_010` | Đối chiếu dấu hiệu $V$ | **Cấp độ 3** | Log scanner, chưa thay kiểm tra bản vá |
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

Bảng 2.4 nối cấu hình mục tiêu với phản hồi và tác động của cùng lượt thử. Các ô chưa có dữ liệu giữ nhãn `[CẦN DỮ LIỆU]`; không điền giả thuyết thành kết quả.

*Bảng 2.4: Ma trận bằng chứng thực nghiệm đối chiếu đa nguồn (Evidence Matrix)*

| Snapshot State | Windows Build & Hotfix | Cấu hình SMBv1 | Trạng thái Routing / Firewall | Nmap Raw Output & Reason | Mã phản hồi NSE (NT Status) | Metasploit Console Log | Bằng chứng Wireshark PCAP | Firewall Drop Log Evidence | Kết luận Cấp độ 1–4 |
|:---:|---|---|---|---|---|---|---|---|:---:|
| **$S_0$** | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` |
| **$S_1$** | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` |
| **$S_2$** | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` |
| **$S_3$** | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` |

Mỗi lượt có mã lượt, snapshot, thời điểm, phiên bản công cụ và cấu hình để nối output, log và lưu lượng. Ghép phản hồi trước vá với log sau vá có thể tạo kết luận sai dù từng tệp đúng. Vì vậy, giữ dữ liệu gốc và dẫn phần diễn giải tới đúng tệp, thời điểm hoặc yêu cầu.

Khi bằng chứng không nhất quán, giữ khác biệt để điều tra. Ví dụ giả định, có bản vá nhưng còn dấu hiệu chưa vá thì cần kiểm tra snapshot, hoàn tất cập nhật và địa chỉ mục tiêu. Không chọn riêng kết quả thuận lợi để điền nhãn cuối; ma trận giúp chỉ ra chỗ cần kiểm tra tiếp.

### 2.5.2. Quy trình kiểm chứng lưu lượng đa điểm (Multi-Point PCAP Verification)

Chỉ thấy `filtered` chưa chỉ ra vị trí chặn. Để đánh giá $R$ tại $S_3$, thu đồng thời ba bằng chứng: SYN được phát tại Kali, log tường lửa ghi quy tắc chặn, và lưu lượng tại mục tiêu không có SYN tương ứng. Các bản ghi phải khớp địa chỉ, cổng, giao thức và thời gian; phép bắt gói tại mục tiêu phải hoạt động với đúng giao diện, bộ lọc. Thiếu gói trong một tệp chưa được kiểm tra điều kiện thu thập không có cùng giá trị với xác nhận gói không tới đích.

Nếu mục tiêu nhận SYN nhưng Kali không nhận phản hồi, cần kiểm tra dịch vụ và đường trở về; đó khác với chặn chiều vào. Kiểm tra từ Client hợp lệ giúp phân biệt hạn chế theo nguồn với mất khả năng phục vụ. Ba nguồn thu bổ sung cho nhau để định vị nguyên nhân, thay vì chỉ lặp kết luận của công cụ. Hiện các tệp và log còn `[CẦN DỮ LIỆU]`.

### 2.5.3. Kế hoạch ứng phó sự cố màn hình xanh (BSOD) và quy trình Rollback

Nguy cơ mất ổn định của module đòi hỏi điểm khôi phục và tiêu chí kiểm tra dịch vụ sau sự cố [10]. Sơ đồ 2.3 mô tả trình tự dự kiến:

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

Khi có sự cố, dừng công cụ, lưu thời điểm và bằng chứng quan sát được rồi khôi phục snapshot của trạng thái tương ứng. Không quy một mã lỗi cụ thể cho phép thử nếu chưa có dữ liệu. Sau khôi phục, kiểm tra lại build, bản vá, SMBv1 và quy tắc mạng trước khi thực hiện tác vụ Client.

Khôi phục snapshot và khôi phục nghiệp vụ là hai mốc khác nhau. Máy ảo trở về điểm lưu chưa đủ để xác nhận Server phục vụ được yêu cầu mới. Nếu đo thời gian phục hồi, ghi riêng thời gian thao tác khôi phục và thời gian tới khi Client hoàn tất đọc, ghi tệp. Ping hoặc cổng 445 mở riêng lẻ chưa đo chức năng chia sẻ tệp. Hiện chưa có số đo thời gian và dữ liệu kiểm tra sau khôi phục: `[CẦN DỮ LIỆU]`.

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

[8] P. Calderon and Nmap Project, "smb-protocols.nse Script Source Code," Nmap Project. [Online]. Available: https://svn.nmap.org/nmap/scripts/smb-protocols.nse. [Accessed: Oct. 4, 2026].

[9] Rapid7, "MS17-010 SMB RCE Detection," Metasploit Framework, source code. [Online]. Available: https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/scanner/smb/smb_ms17_010.rb. [Accessed: Oct. 4, 2026].

[10] Rapid7, "MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption," Rapid7 Exploit Database, 2017. [Online]. Available: https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/
