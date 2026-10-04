# CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ CÔNG CỤ KIỂM THỬ SMB

## 1.1. Tổng quan về giao thức SMB

### 1.1.1. Khái niệm và vai trò của SMB trong hệ điều hành Windows

Giao thức chia sẻ tài nguyên qua mạng (Server Message Block – SMB) cho phép Client gửi yêu cầu truy cập tệp và các tài nguyên do Server cung cấp. Ngoài chia sẻ tệp, SMB còn hỗ trợ in qua mạng, xác thực truy cập, khóa tệp và trao đổi dữ liệu qua đường ống định danh (Named Pipes) [1]. Trong phạm vi đề tài, các chức năng này được xem xét theo quan hệ yêu cầu – phản hồi giữa Client và Server.

Trên Windows, SMB có thể truyền trực tiếp qua TCP 445 hoặc, với phiên bản và cấu hình hỗ trợ, qua dịch vụ phiên NetBIOS trên TCP 139 [2]. Việc nhận diện cổng là bước đầu để xác định đường kết nối; các bước tiếp theo cần kiểm tra phiên bản SMB được chấp nhận và phản hồi của dịch vụ.

### 1.1.2. Mô hình Client – Server

Client là thành phần gửi yêu cầu truy cập tài nguyên từ xa; Server là thành phần cung cấp tài nguyên và xử lý các yêu cầu đó. Khi ứng dụng truy cập đường dẫn chia sẻ (Universal Naming Convention – UNC), chẳng hạn `\\Server\Share`, Client khởi tạo kết nối tới Server [3]. Hai tên gọi chỉ vai trò trong giao tiếp SMB, không đồng nhất với tên phiên bản Windows: một máy có thể vừa cung cấp thư mục chia sẻ, vừa truy cập tài nguyên trên máy khác.

Trong kiểm thử, cần phân biệt việc kết nối được tới Server với việc được phép sử dụng một tài nguyên. Phản hồi của dịch vụ, kết quả thiết lập phiên và quyền truy cập tài nguyên là những thông tin khác nhau; đề tài ghi nhận chúng theo bước kiểm tra tương ứng.

```text
Client                         Server
   |---- Yêu cầu truy cập ------->|
   |<--- Phản hồi xử lý -----------|
   |       Tài nguyên chia sẻ      |
```
*Sơ đồ 1.1: Quan hệ yêu cầu – phản hồi giữa Client và Server trong SMB.*

### 1.1.3. Phân biệt SMBv1, SMBv2 và SMBv3

Giao thức Server Message Block đã trải qua ba thế hệ phiên bản chính, phản ánh sự thay đổi về hiệu năng truyền tải và cơ chế an toàn thông tin [3]:

#### 1. Phiên bản SMBv1 (CIFS)
SMBv1 sử dụng tập lệnh lớn và nhiều thao tác đòi hỏi các lượt yêu cầu – phản hồi (request–response) riêng biệt, làm tăng độ trễ và lưu lượng trao đổi (chatty protocol) của giao thức [3]. Về mặt an ninh, SMBv1 không hỗ trợ mã hóa luồng dữ liệu, cơ chế ký số (SMB Signing) dựa trên hàm băm MD5 [4], [5].

#### 2. Phiên bản SMBv2
Được Microsoft giới thiệu từ Windows Vista và Windows Server 2008 nhằm thay thế SMBv1. SMBv2 bổ sung tính năng gộp lệnh (Compounding) cho phép ghép nhiều yêu cầu (ví dụ: mở tệp, đọc tệp, đóng tệp) trong một gói tin duy nhất [3]. SMBv2 nâng cấp cơ chế ký số chống giả mạo lên thuật toán HMAC-SHA256, mở rộng bộ nhớ đệm và hỗ trợ xử lý I/O bất đồng bộ, giúp nâng cao hiệu năng và độ ổn định [3].

#### 3. Phiên bản SMBv3
Được giới thiệu từ Windows 8 và Windows Server 2012, tiếp tục hoàn thiện trên Windows 10 và Windows Server 2016 với các cơ chế bảo mật theo từng dialect cụ thể [3], [5]:
- **SMB 3.0 (Windows 8 / Server 2012):** Bổ sung tính năng mã hóa dữ liệu đầu cuối (SMB Encryption) ở tầng ứng dụng bằng thuật toán mã hóa khối đối xứng AES-128-CCM (Counter with CBC-MAC), không cần triển khai IPsec để dùng SMB Encryption. Cơ chế này nâng cấp cơ chế ký số sang thuật toán AES-128-CMAC. SMB 3.0 còn bổ sung cơ chế thương lượng phương ngữ an toàn (Secure Dialect Negotiation) nhằm ngăn chặn kẻ tấn công đứng giữa can thiệp sửa đổi gói tin Negotiate để hạ cấp giao thức [5].
- **SMB 3.0.2 (Windows 8.1 / Server 2012 R2):** Từ phiên bản hệ điều hành này, Windows cung cấp khả năng quản trị cho phép gỡ bỏ hoặc vô hiệu hóa hoàn toàn tính năng SMBv1 thông qua công cụ quản lý của hệ điều hành [5], [6].
- **SMB 3.1.1 (Windows 10 / Server 2016 trở lên):** Bổ sung chế độ mã hóa AES-128-GCM (Galois/Counter Mode); tích hợp cơ chế bảo vệ tính toàn vẹn tiền xác thực (Pre-authentication Integrity). Cơ chế này dùng SHA-512 trên chuỗi thông điệp thương lượng (Negotiate và Session Setup) trước khi phiên xác thực hoàn tất. Nếu kẻ tấn công can thiệp làm sai lệch năng lực bảo mật hoặc ép hạ cấp giao thức, chuỗi băm sẽ không khớp và kết nối bị hủy bỏ [5].

*Mối liên hệ với đề tài:* Khi SMBv1 bị vô hiệu hóa, máy chủ không còn tiếp nhận các yêu cầu SMBv1 thuộc bề mặt khai thác của MS17-010; vì vậy nguy cơ khai thác nhóm lỗ hổng này qua SMBv1 được loại bỏ trong cấu hình đó [5], [6].

*Bảng 1.1: So sánh đặc tính kỹ thuật cơ bản giữa SMBv1, SMBv2 và SMBv3 [3], [5], [6].*

| Đặc tính kỹ thuật | SMBv1 (CIFS) | SMBv2 (2.0.2 / 2.1) | SMBv3 (3.0 / 3.0.2 / 3.1.1) |
|---|---|---|---|
| **Hệ điều hành đầu tiên** | Windows 2000 / XP | Windows Vista / Server 2008 | Windows 8 / Server 2012 / Win 10 |
| **Cơ chế xử lý lệnh** | Tuần tự từng bước | Hỗ trợ gộp lệnh (Compounding) | Gộp lệnh tối ưu |
| **Cổng mạng kết nối** | TCP 139 và TCP 445 | TCP 445 | TCP 445 |
| **Ký số (SMB Signing)** | MD5-based | HMAC-SHA256 | AES-CMAC (3.0 / 3.0.2); GMAC trên một số hệ thống mới hỗ trợ SMB 3.1.1 |
| **Mã hóa dữ liệu** | Không có SMB Encryption tích hợp | Không hỗ trợ | AES-128-CCM (3.0); AES-128-GCM (3.1.1) |
| **Bảo vệ tiền xác thực** | Không hỗ trợ | Không hỗ trợ | Chỉ SMB 3.1.1: Pre-authentication Integrity dùng SHA-512 |
| **Cơ chế bảo vệ nổi bật** | Giao thức legacy, không có encryption tích hợp | Ký số HMAC-SHA256, hỗ trợ gộp lệnh | Mã hóa khối AES và bảo vệ toàn vẹn tùy dialect |

### 1.1.4. Phân tích cổng mạng TCP 139 và TCP 445

SMB có thể sử dụng TCP 139 qua dịch vụ phiên NetBIOS (NetBIOS Session Service), hoặc TCP 445 khi truyền trực tiếp trên TCP/IP (Direct-hosted SMB). Microsoft mô tả SMB 1.0 và CIFS có thể dùng NetBIOS, trong khi SMB 2.0.2 từ Windows Vista và Windows Server 2008 sử dụng TCP 445 [2]. Hai cổng vì vậy cần được phân biệt theo phiên bản và cấu hình, không xem là hai đường kết nối tương đương cho mọi phiên bản SMB.

Với TCP 445, dữ liệu SMB có tiêu đề bốn byte chỉ độ dài. Khi cả Direct-hosted SMB và NetBIOS đều được bật, Windows thử hai phương thức đồng thời và sử dụng phương thức phản hồi trước [2]. Tài liệu này không đủ để khẳng định Client luôn ưu tiên 445, luôn gửi RST tới 139 hoặc có mức giảm độ trễ xác định.

Trong đề tài, kết quả cổng 445 ở trạng thái `open` chỉ xác nhận khả năng tiếp cận một dịch vụ đang lắng nghe; cần kiểm tra tiếp để nhận diện SMB và phiên bản được chấp nhận. Khi thiết kế phòng thủ, cổng 139 cũng phải được xem xét nếu cấu hình còn cho phép SMB qua NetBIOS. Việc đóng một cổng không tự chứng minh hệ thống đã được vá MS17-010.

### 1.1.5. Quy trình trao đổi yêu cầu và phản hồi

Client và Server trước hết thương lượng phiên bản SMB được sử dụng, sau đó thiết lập phiên và kết nối tới tài nguyên chia sẻ. Đặc tả SMB2 minh họa chuỗi `NEGOTIATE`, `SESSION_SETUP` và `TREE_CONNECT`; sau khi hoàn tất, Client sử dụng các định danh được Server cấp để tiếp tục truy cập tài nguyên [7].

Với SMBv1/CIFS, Server trả mã định danh người dùng của phiên (User ID – UID) trong phản hồi thiết lập phiên và mã định danh kết nối tài nguyên (Tree ID – TID) khi kết nối tới tài nguyên thành công [8]. Với SMBv2/v3, các trường tương ứng là `SessionId` và `TreeId` [7]. Cách biểu diễn phụ thuộc vào phiên bản, nên cần đọc đúng cấu trúc giao thức khi phân tích dữ liệu bắt gói.

Trong lab, kết quả thương lượng được dùng để xác định Server có chấp nhận SMBv1 hay không. Việc thiết lập phiên và truy cập `IPC$` cần được ghi riêng vì cấu hình xác thực có thể khiến phép thăm dò không hoàn tất. Không suy ra trạng thái bản vá chỉ từ việc Client bị từ chối kết nối tài nguyên.

```text
Client                                 Server
   |---------- Thương lượng ------------->|
   |<--------- Phiên bản được chọn --------|
   |---------- Thiết lập phiên ------------>|
   |<--------- Kết quả và định danh phiên --|
   |---------- Kết nối tài nguyên --------->|
   |<--------- Kết quả và định danh kết nối-|
```
*Sơ đồ 1.2: Các bước thiết lập giao tiếp SMB trước khi sử dụng tài nguyên.*

---

## 1.2. Lỗ hổng bảo mật MS17-010

### 1.2.1. Tổng quan về thông báo bảo mật MS17-010

Vào tháng 03 năm 2017, Microsoft phát hành thông báo bảo mật định kỳ mang mã hiệu **MS17-010** nhằm khắc phục các lỗ hổng nghiêm trọng trong việc xử lý gói tin của dịch vụ SMBv1 trên hệ điều hành Windows [4]. Nhóm lỗ hổng này ảnh hưởng tới hầu hết các phiên bản Windows lưu hành tại thời điểm đó, bao gồm Windows Vista, Windows 7, Windows 8.1, Windows 10, cùng các dòng máy chủ Windows Server 2008, 2012 và 2016. Do tính chất nghiêm trọng, Microsoft sau đó đã phát hành thêm bản vá cho các hệ điều hành đã dừng hỗ trợ như Windows XP và Windows Server 2003 [4].

Các lỗ hổng thực thi mã từ xa trong thông báo MS17-010 cho phép kẻ tấn công gửi các thông điệp SMBv1 được chế tạo đặc biệt tới máy chủ mục tiêu. Trong nhiều trường hợp, việc khai thác có thể được thực hiện từ xa mà không cần thông tin xác thực hợp lệ [4]. Trong phạm vi đề tài, CVE-2017-0144 / EternalBlue được lựa chọn làm trường hợp kiểm thử chính.

### 1.2.2. Phân loại các mã CVE và danh mục bản vá theo hệ điều hành

Thông báo bảo mật MS17-010 xử lý một nhóm gồm 6 mã định danh lỗ hổng phổ biến (CVE) được Microsoft liệt kê trong thông báo [4]. Không đồng nhất mọi CVE với cơ chế lỗi FEA của EternalBlue. Để trình bày rõ ràng, nội dung được phân tách thành hai bảng: Bảng 1.2 mô tả đặc tính kỹ thuật từng CVE và Bảng 1.3 liệt kê danh mục mã bản vá KB chính thức theo từng phiên bản hệ điều hành.

*Bảng 1.2: Phân loại các mã CVE trong thông báo bảo mật Microsoft MS17-010 [4], [9], [10], [11].*

| Mã CVE | Liên hệ exploit | Phân loại theo nguồn chính thức | Tác động | Vai trò trong đồ án |
|---|---|---|---|---|
| **CVE-2017-0143** | **EternalSynergy** [9] | SMBv1 Remote Code Execution Vulnerability | RCE | Tham chiếu trong nhóm MS17-010 |
| **CVE-2017-0144** | **EternalBlue** [10] | SMBv1 Remote Code Execution Vulnerability; EternalBlue khai thác lỗi xử lý FEA trong `srv.sys` | RCE | **Mục tiêu thực nghiệm chính** |
| **CVE-2017-0145** | **EternalRomance** [11] | SMBv1 Remote Code Execution Vulnerability | RCE | Tham chiếu lịch sử / đối chiếu |
| **CVE-2017-0146** | Không gắn nickname | SMBv1 Remote Code Execution Vulnerability | RCE | Thuộc phạm vi MS17-010 |
| **CVE-2017-0147** | Không gắn nickname | SMBv1 Information Disclosure Vulnerability | Information Disclosure | Thuộc phạm vi MS17-010 |
| **CVE-2017-0148** | Không gắn nickname | SMBv1 Remote Code Execution Vulnerability | RCE | Thuộc phạm vi MS17-010 |

Sau Bảng 1.2, đề tài chỉ phân tích sâu cơ chế của CVE-2017-0144, vì đây là mục tiêu thực nghiệm trung tâm của kịch bản lab.

*Bảng 1.3: Danh mục mã bản vá KB chính thức của Microsoft theo hệ điều hành Windows [4].*

| Hệ điều hành | Phiên bản / Kiến trúc | Bản vá Security Only | Bản vá Monthly Rollup / Cumulative | Ghi chú triển khai lab |
|---|---|---|---|---|
| **Windows 7 SP1** | x86 và x64 | **KB4012212** | **KB4012215** | Môi trường mục tiêu chính để kiểm tra trước và sau khi vá |
| **Windows Server 2008 R2 SP1** | x64 | **KB4012212** | **KB4012215** | Tương đồng mã bản vá với Windows 7 SP1 |
| **Windows 8.1** | x86 và x64 | **KB4012213** | **KB4012216** | Mục tiêu đối sánh trên thế hệ Windows mới hơn |
| **Windows Server 2012 R2** | x64 | **KB4012213** | **KB4012216** | Bản vá tương ứng Windows 8.1 |
| **Windows Server 2012** | x64 | **KB4012214** | **KB4012217** | Phiên bản máy chủ thế hệ Windows 8 |
| **Windows 10** | Bản dựng 1507 (RTM)<br>Bản dựng 1511<br>Bản dựng 1607 | Không áp dụng (chỉ có bản tích lũy) | **KB4012606** (1507)<br>**KB4013198** (1511)<br>**KB4013429** (1607) | Windows 10 sử dụng mô hình cập nhật tích lũy Cumulative Update |
| **Windows Server 2016** | Bản dựng 1607 | Không áp dụng | **KB4013429** | Tương đồng bản vá với Windows 10 Version 1607 |
| **Windows Vista SP2 / Server 2008 SP2** | x86 và x64 | **KB4012598** | Không áp dụng | Bản cập nhật an ninh độc lập |
| **Windows XP SP3 / Server 2003 SP2** | x86 và x64 | **KB4012598** | Không áp dụng | Bản vá khẩn cấp phát hành ngoài chu kỳ hỗ trợ |

### 1.2.3. Cơ chế kỹ thuật của lỗ hổng CVE-2017-0144 và mã khai thác EternalBlue

Nguyên nhân kỹ thuật phát sinh lỗ hổng CVE-2017-0144 liên quan đến lỗi xử lý cấu trúc File Extended Attributes (FEA) trong driver điều khiển `srv.sys` của hệ điều hành Windows khi phân tích các yêu cầu giao dịch SMBv1 [12]. Cơ chế phát sinh và khai thác lỗ hổng được mô tả qua ba bước logic sau:

- **Bước 1: Xử lý dữ liệu giao dịch sai kích thước khi phân tích danh sách FEA.**
  Trong giao thức SMBv1, client có thể gửi thông tin thuộc tính mở rộng của tệp tin thông qua cấu trúc danh sách FEA (`FEA_LIST`). Trong quá trình chuyển đổi danh sách FEA từ định dạng OS/2 sang định dạng NT thông qua hàm nội bộ `SrvOs2FeaToNt` (kèm theo hàm tính toán độ dài `SrvOs2FeaListSizeToNt`), driver `srv.sys` gặp lỗi sai lệch toán học khi ép kiểu kích thước, dẫn đến tính toán sai tổng dung lượng bộ đệm cần thiết [12].
- **Bước 2: Sai lệch tính toán dẫn đến cấp phát vùng nhớ không phù hợp và ghi ngoài biên.**
  Do sai lệch trong việc kiểm tra kích thước danh sách FEA, driver `srv.sys` cấp phát một vùng nhớ trong bộ nhớ nhân (Non-Paged Pool) có dung lượng nhỏ hơn khối dữ liệu thực tế mà client gửi tới. Khi driver thực hiện thao tác sao chép dữ liệu thuộc tính vào bộ nhớ đệm này, dữ liệu thừa đã bị ghi tràn ra ngoài phạm vi vùng nhớ được cấp phát (out-of-bounds write / buffer overflow), làm sai lệch các cấu trúc quản lý bộ nhớ kế cận trong kernel [12].
- **Bước 3: EternalBlue kết hợp lỗi bộ nhớ với kỹ thuật bố trí vùng nhớ để thực thi mã.**
  Mã khai thác EternalBlue gửi một chuỗi gói tin SMB được thiết kế theo trình tự nhằm sắp xếp bố cục các khối nhớ trong Non-Paged Pool (heap grooming). Khi lỗi tràn bộ nhớ xảy ra, dữ liệu ghi đè can thiệp vào các con trỏ điều khiển trong kernel, cho phép chuyển hướng luồng thực thi của bộ xử lý tới đoạn mã thực thi (Shellcode) do kẻ tấn công đưa vào bộ nhớ. Kết quả là đoạn mã được kích hoạt trực tiếp trong không gian nhân với đặc quyền `SYSTEM` [10], [12].

```
+-------------------------------------------------------------------------+
| Bước 1: Gửi yêu cầu giao dịch SMBv1 kèm danh sách FEA                   |
|         (Sai lệch tính toán kích thước khi chuyển đổi FEA list)         |
+-------------------------------------------------------------------------+
                                     │
                                     ▼
+-------------------------------------------------------------------------+
| Bước 2: Cấp phát bộ đệm kernel nhỏ hơn dữ liệu thực tế                  |
|         ──> Sao chép dữ liệu gây ghi ngoài vùng nhớ (Buffer Overflow)   |
+-------------------------------------------------------------------------+
                                     │
                                     ▼
+-------------------------------------------------------------------------+
| Bước 3: Ghi đè cấu trúc điều khiển trong bộ nhớ kernel                  |
|         ──> Chuyển hướng luồng xử lý tới Shellcode (Thực thi mã SYSTEM) |
+-------------------------------------------------------------------------+
```
*Sơ đồ 1.3: Mô hình 3 bước phát sinh và khai thác lỗ hổng CVE-2017-0144.*

### 1.2.4. Điều kiện hệ thống có nguy cơ bị khai thác

Để một hệ thống Windows nằm trong phạm vi có thể bị khai thác CVE-2017-0144, cần xem xét các điều kiện kỹ thuật sau [4], [10], [12]:
1. **Hệ điều hành:** Đang sử dụng phiên bản Windows thuộc danh mục bị ảnh hưởng (từ Windows XP đến Windows 10 các bản dựng đầu, hoặc Windows Server 2003 đến 2016) [4]. Trong phạm vi thực nghiệm, đề tài lựa chọn Windows 7 SP1 x64 làm máy mục tiêu do thuộc nhóm hệ điều hành bị ảnh hưởng và được module Metasploit hỗ trợ trong kịch bản kiểm thử của đề tài [12].
2. **Tính năng SMBv1 đang được kích hoạt:** Driver xử lý `srv.sys` đang hoạt động và tiếp nhận các yêu cầu giao dịch SMBv1 [6].
3. **Cổng dịch vụ mạng có thể tiếp cận được:** Cổng TCP 445 (hoặc TCP 139) ở trạng thái mở và không bị chặn bởi tường lửa mạng hoặc tường lửa cục bộ [13].
4. **Chưa cài đặt bản vá an ninh MS17-010:** Hệ điều hành chưa được cập nhật gói vá bảo mật tương ứng theo danh mục ở Bảng 1.3 [4].
5. **Đặc điểm xác thực:** CVE-2017-0144 có thể được khai thác từ xa mà không yêu cầu tài khoản xác thực hợp lệ khi dịch vụ SMBv1 mục tiêu có thể tiếp cận [4], [10]. Việc sử dụng `IPC$` trong đề tài chủ yếu xuất hiện ở cơ chế thăm dò của kịch bản Nmap và được phân tích chi tiết tại Mục 1.3.3.

**Nguyên tắc đánh giá:** Cần phân biệt giữa việc "hệ thống mở cổng 445" hoặc "hệ thống đang bật SMBv1" với việc "hệ thống có lỗ hổng MS17-010". Một máy tính đã cài đặt bản vá bảo mật vẫn mở cổng 445 để phục vụ chia sẻ tệp bình thường, nhưng driver `srv.sys` đã được bổ sung đoạn mã kiểm tra tính hợp lệ của tham số, do đó không còn bị ảnh hưởng bởi lỗi tràn bộ nhớ này [4], [6].

### 1.2.5. Tác động an toàn thông tin

CVE-2017-0144 có thể dẫn tới thực thi mã từ xa; mô-đun EternalBlue cũng có nguy cơ gây mất ổn định, BSOD hoặc khởi động lại trên một số hệ thống [10], [12]. Đề tài vì vậy xem xét cả nguy cơ truy cập hoặc thay đổi dữ liệu trái phép và nguy cơ gián đoạn dịch vụ khi xây dựng tiêu chí đánh giá. Các tác động cụ thể cần được xác định theo quyền thực thi và cấu hình mục tiêu, không coi toàn bộ hậu quả là kết quả đã quan sát trong lab.

Về tính bí mật và toàn vẹn, phép kiểm tra chỉ được dùng để xác nhận tác động trong phạm vi dữ liệu thử nghiệm được phép. Về tính sẵn sàng, cần theo dõi trạng thái máy mục tiêu và khả năng phục vụ Client. Một sự cố BSOD chưa được tính là bằng chứng thực thi mã thành công.

### 1.2.6. Khái quát các chiến dịch tấn công thực tế liên quan

Sự kết hợp giữa lỗ hổng MS17-010 và mã khai thác EternalBlue đã được ghi nhận trong các sự cố an ninh mạng diện rộng trên thế giới [11], [14]:

- **WannaCry (tháng 05/2017):** Microsoft ghi nhận mã độc có khả năng lây sang các máy Windows chưa vá trong mạng nội bộ và quét địa chỉ Internet. Hướng dẫn phòng vệ nhấn mạnh cập nhật MS17-010, tắt SMBv1 và hạn chế kết nối SMB từ các nguồn không được phép [14].
- **Mã độc NotPetya (Tháng 06/2017):** NotPetya sử dụng mã khai thác liên quan đến MS17-010 (bao gồm EternalBlue và EternalRomance) để lây lan qua mạng nội bộ. Mục tiêu chính của NotPetya là phá hoại cấu trúc hệ thống tệp và bản ghi khởi động (MBR), khiến hệ thống không thể khôi phục, gây thiệt hại cho nhiều tập đoàn vận tải và hạ tầng quốc tế [11].

Các sự cố này cho thấy việc kiểm tra, xác minh và áp dụng các biện pháp phòng thủ cho dịch vụ SMB là nhiệm vụ kỹ thuật có ý nghĩa thực tiễn trong quản trị hệ thống.

---

## 1.3. Công cụ phục vụ kiểm thử

### 1.3.1. Hệ điều hành kiểm thử Kali Linux

Kali Linux là bản phân phối Linux mã nguồn mở dựa trên Debian, phục vụ kiểm thử xâm nhập và đánh giá an toàn thông tin [15]. Đề tài lựa chọn Kali làm trạm kiểm thử để tổ chức các công cụ khảo sát và thu thập dữ liệu trong cùng một môi trường. Việc dùng Kali không tự tạo tính cô lập; điều đó phụ thuộc vào cấu hình mạng ảo và phạm vi kết nối của lab.

Trước khi kiểm thử, cần ghi phiên bản Kali, phiên bản công cụ và các thành phần đã cài đặt. Hồ sơ này giúp đối chiếu kết quả giữa các lượt chạy, thay vì giả định mọi bản Kali đều có cùng công cụ và hành vi.

### 1.3.2. Công cụ quét mạng Nmap

Nmap (Network Mapper) là công cụ quét mạng và kiểm tra dịch vụ tiêu chuẩn [16]. Trong quy trình kiểm thử SMB, Nmap đảm nhiệm các vai trò cụ thể:
- **Phát hiện trạng thái cổng (`-sS`, `-p 139,445`):** Sử dụng kỹ thuật quét TCP SYN (quét bán mở) để xác định xem cổng TCP 445 hoặc TCP 139 trên máy mục tiêu có đang mở (`open`) hay không mà không cần thiết lập phiên kết nối đầy đủ [16].
- **Nhận diện dịch vụ và phiên bản (`-sV`):** Thực hiện gửi các gói tin thăm dò (probes) tới cổng mở nhằm thu thập biểu ngữ phản hồi, từ đó định danh tên dịch vụ (ví dụ: `microsoft-ds`) và xác định thông tin phiên bản dựa trên cơ sở dữ liệu mẫu phản hồi [16]. Cần lưu ý tùy chọn `-sV` tập trung nhận diện phiên bản của dịch vụ lắng nghe, trong khi việc nhận diện hệ điều hành thuộc về tùy chọn `-O` hoặc các script chuyên biệt.

### 1.3.3. Tự động hóa kiểm tra an toàn với Nmap Scripting Engine (NSE)

Nmap Scripting Engine (NSE) cho phép thực thi các tập kịch bản viết bằng ngôn ngữ Lua để tự động hóa các tác vụ kiểm tra an toàn nâng cao [16], [17]. Đối với dịch vụ SMB và lỗ hổng MS17-010:
- **Script `smb-protocols.nse`:** Gửi các yêu cầu Negotiate với danh sách dialect khác nhau để xác định máy chủ đích có đang chấp nhận giao tiếp qua giao thức SMBv1 (`"NT LM 0.12"`) hay không [16].
- **Script `smb-vuln-ms17-010.nse`:** Nmap xếp kịch bản này vào nhóm `safe` và `vuln`; kịch bản dùng phản hồi SMB để nhận biết dấu hiệu chưa vá MS17-010 [17]. Phân loại `safe` không phải bảo đảm mọi cấu hình mục tiêu đều không chịu tác động.

**Cơ chế kỹ thuật chi tiết của script `smb-vuln-ms17-010.nse`:**
1. Script dùng thư viện SMB để thiết lập kết nối và thương lượng SMBv1. Sau bước Session Setup theo thông tin xác thực được cấu hình, script gửi Tree Connect tới tài nguyên chia sẻ `\\Target\IPC$` (mặc định tham số `sharename` là `IPC$`) [17].
2. Khi phiên làm việc với `IPC$` được thiết lập, script gửi một yêu cầu giao dịch `SMB_COM_TRANSACTION` (opcode `0x25`) với lệnh `PeekNamedPipe` (mã `0x2300`) trên đường ống định danh `\PIPE\` với các tham số độ dài bộ đệm tối đa (`Max Parameter Count = 0xFFFF`, `Max Data Count = 0xFFFF`) [17].
3. **Phân tích mã trạng thái phản hồi NT Status theo mã nguồn Nmap:**
   - *Dấu hiệu phù hợp hệ thống chưa vá (VULNERABLE):* Nếu máy chủ phản hồi mã lỗi NT Status `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`), phản hồi phù hợp với dấu hiệu mà kịch bản dùng để nhận diện hệ thống chưa vá. Script ghi nhận dấu hiệu này và xuất kết luận `State: VULNERABLE` [17].
   - *Dấu hiệu phù hợp hệ thống đã vá:* Nếu máy chủ phản hồi mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc `STATUS_INVALID_HANDLE` (`0xC0000008`), kịch bản diễn giải đây là dấu hiệu phù hợp với hệ thống đã vá và ghi thông báo `This system is patched` [17]. Cần đối chiếu thêm trạng thái bản vá trên mục tiêu; một thông báo của công cụ không chứng minh hệ thống không còn mọi lỗ hổng.

Khi không kết nối được tới `IPC$`, không đọc được phản hồi hoặc nhận mã trạng thái ngoài các nhánh được nhận diện, phép kiểm tra chưa cung cấp đủ cơ sở để xác định trạng thái bản vá. Mã nguồn vẫn có thể gán `NOT_VULN` trong nhánh không phát hiện dấu hiệu; đề tài phải đọc kèm lỗi và kết quả kiểm tra, thay vì coi nhãn này là bằng chứng máy đã vá [17].

Việc diễn giải kết quả quét còn phụ thuộc vào các điều kiện sau:
- *Ảnh hưởng của chính sách hạn chế kết nối nặc danh:* Trong trường hợp không cung cấp thông tin xác thực, kịch bản kiểm tra `smb-vuln-ms17-010.nse` phụ thuộc vào việc kết nối ẩn danh tới tài nguyên `IPC$`. Nếu truy cập nặc danh tới `IPC$` bị chặn (như cấu hình `RestrictAnonymous = 2`) và người kiểm thử không cung cấp thông tin xác thực phù hợp, kịch bản có thể không hoàn tất được phép thăm dò và không xác định được trạng thái, dù driver `srv.sys` trên thực tế có thể chưa được vá. Công cụ có hỗ trợ truyền thông tin xác thực thông qua tham số nếu được cấu hình [17].
- *Ảnh hưởng của thiết bị bảo vệ mạng:* Tường lửa cá nhân hoặc hệ thống ngăn ngừa xâm nhập (IPS) có thể cho phép bắt tay TCP nhưng ngắt kết nối khi nhận yêu cầu Transaction bất thường. Phản hồi khi đó chưa đủ để xác định trạng thái bản vá.
- *Bản chất của kết luận "VULNERABLE":* Kết luận từ công cụ quét chỉ xác nhận *phản hồi của máy chủ khớp với dấu hiệu chưa vá mà kịch bản sử dụng*. Kết luận này chưa chứng minh khả năng thiết lập phiên tương tác khi khai thác. Kết quả còn phụ thuộc vào kiến trúc CPU (x86 hay x64), trạng thái phân mảnh của bộ nhớ Non-Paged Pool (có thể gây sập hệ thống BSOD thay vì cấp shell), và sự ngăn chặn của các giải pháp bảo vệ điểm cuối (EDR/Antivirus) [16], [17].

### 1.3.4. Nền tảng kiểm thử Metasploit Framework

Metasploit Framework là nền tảng kiểm tra xâm nhập mô-đun hóa, hỗ trợ chuẩn hóa quy trình thẩm định an toàn thông tin [12], [18]. Trong phạm vi đề tài, Metasploit được phân bổ hai vai trò rõ ràng:
- **Mô-đun phụ trợ (Auxiliary Module):** Sử dụng mô-đun `auxiliary/scanner/smb/smb_ms17_010` để quét và kiểm tra dấu hiệu lỗ hổng trên dải địa chỉ IP [12]. Cần lưu ý mô-đun này và script NSE của Nmap là hai implementation khác nhau dùng để tham chiếu chéo về mặt phản ứng dịch vụ. Các đối chứng thực sự khác loại bao gồm: bản dựng Windows (build), danh sách Hotfix/KB đã cài đặt, lưu lượng gói tin (packet capture) và trạng thái tính năng SMBv1 trên máy mục tiêu.
- **Mô-đun khai thác có kiểm soát (Exploit Module):** Sử dụng mô-đun `exploit/windows/smb/ms17_010_eternalblue` trong môi trường phòng thí nghiệm cô lập nhằm thẩm định khả năng thực thi của lỗ hổng CVE-2017-0144 [12]. Payload được giới hạn ở các thao tác xác nhận quyền thực thi; bản thân quá trình khai thác kernel vẫn có nguy cơ gây mất ổn định hoặc phát sinh lỗi màn hình xanh (BSOD), vì vậy thực nghiệm chỉ tiến hành trên máy ảo đã tạo điểm sao lưu phục hồi (snapshot) [12].

```
[ Pha 1: Quét cổng ] ──> Nmap (-p 139,445 -sS) ──> Xác định cổng TCP mở
           │
           ▼
[ Pha 2: Định danh ] ──> Nmap (-sV) ─────────────> Nhận diện dịch vụ microsoft-ds
           │
           ▼
[ Pha 3: Dấu hiệu ]  ──> Nmap NSE / MSF Aux ─────> Kiểm tra dấu hiệu chưa vá MS17-010
           │
           ▼
[ Pha 4: Thẩm định ] ──> Metasploit (Lab cô lập) ─> Xác minh khả năng thực thi trong lab
```
*Sơ đồ 1.4: Quy trình 4 giai đoạn phối hợp công cụ trong kiểm thử đánh giá an ninh SMB.*

### 1.3.5. Bảng liên kết kiến thức lý thuyết và các bước thực nghiệm lab

Để tạo cầu nối giữa cơ sở lý thuyết và các thao tác trong mô hình thực nghiệm, Bảng 1.4 đối chiếu từng thành phần kiến thức với mục tiêu quan sát và công cụ tương ứng được triển khai trong lab.

*Bảng 1.4: Đối chiếu kiến thức lý thuyết và các bước thực nghiệm trong lab.*

| Khái niệm lý thuyết | Vấn đề kỹ thuật cần làm rõ | Bước quan sát / Thao tác trong lab | Công cụ sử dụng |
|---|---|---|---|
| **Cổng mạng TCP 445 / 139** | Cổng dịch vụ có đang lắng nghe kết nối từ mạng hay không | Quét cổng TCP trên máy mục tiêu để kiểm tra trạng thái `open` | Nmap (`-sS -p 139,445`) |
| **Phiên bản Dialect SMB** | Máy mục tiêu có chấp nhận đàm phán qua SMBv1 không | Gửi gói đàm phán dialect để ghi nhận phiên bản giao thức | Nmap (`--script smb-protocols`) |
| **Dấu hiệu MS17-010** | Driver `srv.sys` có phản hồi mã lỗi đặc trưng của bản chưa vá | Gửi gói tin thăm dò an toàn vào `IPC$` để kiểm tra trạng thái | Nmap (`--script smb-vuln-ms17-010`), MSF Auxiliary |
| **Trạng thái bản vá Windows** | Xác nhận máy chủ đã cài đặt gói cập nhật an ninh hay chưa | Kiểm tra lịch sử cập nhật và danh sách bản vá (Hotfix/KB) | Lệnh `systeminfo` / PowerShell trên Windows |
| **Khả năng khai thác thực tế** | Lỗ hổng CVE-2017-0144 có thể bị lợi dụng để thực thi mã không | Thực nghiệm kiểm tra trong mạng lab cô lập có sao lưu snapshot | Metasploit Framework (`ms17_010_eternalblue`) |
| **Nguyên tắc phòng thủ** | Áp dụng bản vá, tắt SMBv1 hoặc cấu hình chặn cổng bằng firewall | Thực hiện cấu hình phòng thủ trên Windows Target | Windows Update, PowerShell, Windows Firewall |
| **Xác minh lại (Retest)** | Biện pháp phòng thủ có loại bỏ dấu hiệu lỗ hổng hay không | Chạy lại bộ kiểm thử để so sánh kết quả trước và sau | Nmap, NSE script, Metasploit scanner |

---

## 1.4. Cơ sở đánh giá trạng thái và nguyên tắc phòng thủ

### 1.4.1. Nguyên tắc phân định các cấp độ trạng thái dịch vụ và lỗ hổng

Một thiếu sót phổ biến trong đánh giá an ninh là việc suy diễn từ trạng thái mở cổng sang kết luận có lỗ hổng. Để đảm bảo tính khoa học và chính xác, đề tài phân định 4 cấp độ trạng thái kỹ thuật tăng dần theo Bảng 1.5.

*Bảng 1.5: Khung phân định 4 cấp độ trạng thái dịch vụ và lỗ hổng SMB.*

| Cấp độ | Tên gọi kỹ thuật | Dấu hiệu quan sát thực tế | Ý nghĩa an ninh kỹ thuật | Giới hạn kết luận |
|---|---|---|---|---|
| **Cấp độ 1** | Khả năng tiếp cận dịch vụ SMB | Cổng TCP 445 hoặc TCP 139 ở trạng thái `open` qua quét TCP SYN | Cổng mạng đang có dịch vụ lắng nghe; cần thực hiện nhận diện dịch vụ để xác nhận | **Chưa thể kết luận lỗ hổng.** Đây là trạng thái mở cổng mạng, chưa khẳng định cấu hình dịch vụ |
| **Cấp độ 2** | Xác nhận máy chủ chấp nhận SMBv1 | Server chấp thuận dialect `"NT LM 0.12"` khi đàm phán Negotiate | Tính năng SMBv1 chưa bị vô hiệu hóa; bề mặt phơi nhiễm của SMBv1 đang mở | **Chưa đủ cơ sở khẳng định có lỗ hổng.** Máy tính có thể đã được cài bản vá nhưng chưa tắt SMBv1 |
| **Cấp độ 3** | Dấu hiệu phù hợp với hệ thống chưa vá MS17-010 | Server phản hồi mã NT Status `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`) trước gói probe `SMB_COM_TRANSACTION` | Driver `srv.sys` có nhánh xử lý logic trùng khớp với mẫu hành vi chưa được cập nhật bản vá | **Chưa chứng minh khai thác thành công.** Kết quả chỉ cho thấy phản hồi phù hợp với mẫu hành vi chưa vá; nếu truy cập nặc danh bị chặn và không có thông tin xác thực thì script không xác định được trạng thái |
| **Cấp độ 4** | Bằng chứng thực nghiệm cho thấy cấu hình có thể bị khai thác | Phiên kiểm thử có kiểm soát hoàn tất việc thực thi mã thử nghiệm trong lab | Cấu hình máy mục tiêu tồn tại lỗ hổng CVE-2017-0144 và có thể bị khai thác từ xa | Chỉ thực hiện trong mạng lab cô lập; dừng kiểm thử nếu phát sinh tác động ngoài dự kiến |

### 1.4.2. Giới hạn kỹ thuật và phòng ngừa kết quả sai lệch

Trong quá trình trinh sát và kiểm tra an toàn dịch vụ SMB, kết quả ghi nhận từ các công cụ tự động có thể gặp hiện tượng dương tính giả (False Positive) hoặc âm tính giả (False Negative) do các nguyên nhân kỹ thuật:
- **Hạn chế của quyền truy cập nặc danh (Null Session):** Kịch bản kiểm tra `smb-vuln-ms17-010.nse` khi không có thông tin xác thực sẽ phụ thuộc vào việc kết nối ẩn danh tới tài nguyên `IPC$`. Nếu truy cập nặc danh tới `IPC$` bị chặn (như cấu hình `RestrictAnonymous = 2`) và người kiểm thử không cung cấp thông tin xác thực phù hợp, kịch bản có thể không hoàn tất được phép thăm dò và không xác định được trạng thái, dù driver `srv.sys` trên thực tế có thể chưa được vá.
- **Tác động của thiết bị bảo vệ mạng:** Tường lửa cá nhân hoặc hệ thống ngăn ngừa xâm nhập (IPS) có thể cho phép bắt tay TCP nhưng ngắt kết nối khi nhận yêu cầu Transaction bất thường. Phản hồi khi đó chưa đủ để xác định trạng thái bản vá.
- **Sự khác biệt giữa "Dấu hiệu chưa vá" và "Khả năng khai thác thành công":** Một hệ thống được công cụ báo `VULNERABLE` ở Cấp độ 3 chỉ phản ánh việc driver có phản ứng logic của mẫu hành vi cũ. Kết quả ở Cấp độ 4 còn phụ thuộc vào kiến trúc CPU, trạng thái bộ nhớ và giải pháp bảo vệ điểm cuối (Endpoint Protection/EDR). Những yếu tố này cần được ghi nhận khi diễn giải lượt kiểm thử.
- **Biện pháp phòng ngừa:** Người kiểm thử cần đối chiếu kết quả Nmap/NSE và Metasploit scanner với phiên bản/build Windows, danh sách Hotfix/KB và trạng thái tính năng SMBv1 trên máy mục tiêu. Dữ liệu bắt gói tin (packet capture) và nhật ký sự kiện (Windows Event Logs) được sử dụng làm bằng chứng bổ sung khi cần phân tích nguyên nhân sai lệch [16].

### 1.4.3. Nguyên tắc giảm thiểu rủi ro và phòng thủ giao thức SMB

Để bảo vệ hệ thống trước nguy cơ từ các lỗ hổng SMB và MS17-010, các nguyên tắc phòng thủ kỹ thuật cần được triển khai đồng bộ theo trình tự:

1. **Cập nhật bản vá an ninh định kỳ (Security Patching):**
   Cài đặt đầy đủ các bản vá an ninh do Microsoft phát hành theo danh mục ở Bảng 1.3 (ví dụ: gói KB4012212 hoặc các bản cập nhật tích lũy). Bản vá sửa đổi logic xử lý kích thước trong driver `srv.sys`, khắc phục nguyên nhân của lỗi tràn bộ đệm mà không làm gián đoạn hoạt động chia sẻ tệp cần thiết [4].
2. **Vô hiệu hóa giao thức SMBv1:**
   Khi ứng dụng không còn yêu cầu tương thích SMBv1, nên vô hiệu hóa giao thức này theo cách phù hợp với phiên bản Windows [6]. Cần kiểm tra ảnh hưởng lên thiết bị và ứng dụng trước khi áp dụng trong môi trường thực tế.
3. **Kiểm soát và lọc cổng TCP 445 / 139 bằng tường lửa:**
   Cấu hình quy tắc tường lửa (Host Firewall và Network Firewall) để chặn kết nối tới cổng 445 và 139 từ các vùng mạng không tin cậy hoặc từ Internet. Dịch vụ chia sẻ tệp chỉ nên được phép truy cập từ các dải mạng nội bộ hoặc VLAN quản trị xác định [13].
4. **Phân đoạn mạng và cô lập dịch vụ (Network Segmentation):**
   Tách biệt các máy chủ dữ liệu quan trọng vào các phân vùng mạng riêng, áp dụng danh sách kiểm soát truy cập (ACL) giữa các vùng mạng nhằm hạn chế khả năng lây lan ngang (Lateral Movement) nếu một trạm làm việc trong mạng bị xâm nhập [13].
5. **Đánh giá ảnh hưởng tương thích:**
   Trước khi vô hiệu hóa SMBv1 hoặc chặn cổng mạng trong môi trường thực tế, cần rà soát các thiết bị ngoại vi cũ (máy in mạng đời cũ, thiết bị lưu trữ NAS cũ) để có phương án nâng cấp hoặc chuyển tiếp phù hợp, tránh gây gián đoạn nghiệp vụ [6].
6. **Quy trình kiểm thử lại (Retesting):**
   Sau khi áp dụng biện pháp phòng thủ, chạy lại cùng bộ kiểm thử để ghi nhận sự thay đổi trạng thái tương ứng. Kết quả cần chứng minh không còn chỉ báo MS17-010 theo tiêu chí đã xác định, đồng thời ghi nhận riêng trạng thái cổng và phiên bản SMB sau cấu hình [16].

---

## TỔNG KẾT CHƯƠNG 1

Chương 1 trình bày cơ sở về SMB, các lỗ hổng thuộc thông báo MS17-010 và vai trò của công cụ kiểm thử. Cổng mạng, phiên bản giao thức, phản hồi của phép thăm dò và khả năng thực thi mã được phân biệt thành bốn mức bằng chứng. Kết quả ở một mức chưa đủ để kết luận mức tiếp theo; đặc biệt, cổng mở hoặc SMBv1 đang bật không tự chứng minh hệ thống chưa vá.

Khung phân định này là cách tổ chức đánh giá của đề tài, giúp liên kết kiến thức giao thức với bước quan sát trong lab. Chương 2 sử dụng khung đó để thiết kế trạng thái máy mục tiêu, điểm thu thập dữ liệu và tiêu chí đánh giá phòng thủ. Các giới hạn về xác thực, phản hồi công cụ và tác động lên hệ thống phải được kiểm tra khi áp dụng; phần chưa có dữ liệu thực nghiệm chưa được trình bày như kết quả.


## TÀI LIỆU THAM KHẢO

[1] Microsoft, "What is Microsoft SMB Protocol and CIFS Protocol?," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview

[2] Microsoft, "Direct hosting of SMB over TCP/IP," Microsoft Learn, 2026. [Online]. Available: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/direct-hosting-of-smb-over-tcpip

[3] Microsoft, "What is SMB File Sharing for Windows and Windows Server?," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview

[4] Microsoft, "Microsoft Security Bulletin MS17-010 - Critical," Microsoft Learn / Security TechCenter, Mar. 2017. [Online]. Available: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010

[5] Microsoft, "SMB security enhancements," Microsoft Learn, 2023. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security

[6] Microsoft, "Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3

[7] Microsoft, "[MS-SMB2]: Connecting to a Share by Using an SMB2 Negotiate," Microsoft Open Specifications. [Online]. Available: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-smb2/c9efe8ca-ff34-44d0-bfbe-58a9b9db50d4. [Accessed: Oct. 4, 2026].

[8] Microsoft, "[MS-CIFS]: Common Internet File System (CIFS) Protocol," Microsoft Open Specifications, "Per SMB Session" and sec. 3.2.5.4. [Online]. Available: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cifs/c7cb45aa-f923-4cd4-a9d5-4a1418e41d42; https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cifs/c42729fb-c655-424f-8d9a-44825d609b86. [Accessed: Oct. 4, 2026].

[9] Microsoft Security Response Center (MSRC), "Eternal Synergy Exploit Analysis," Microsoft, 2017. [Online]. Available: https://msrc.microsoft.com/blog/2017/05/eternal-synergy-exploit-analysis/

[10] National Institute of Standards and Technology (NIST), "CVE-2017-0144 Detail," National Vulnerability Database (NVD), Mar. 2017. [Online]. Available: https://nvd.nist.gov/vuln/detail/CVE-2017-0144

[11] Microsoft Threat Intelligence, "New ransomware, old techniques: Petya adds-worm capabilities," Microsoft Security Blog, Jun. 2017. [Online]. Available: https://www.microsoft.com/en-us/security/blog/2017/06/27/new-ransomware-old-techniques-petya-adds-worm-capabilities/

[12] Rapid7, "MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption," Rapid7 Exploit Database, 2017. [Online]. Available: https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/

[13] National Institute of Standards and Technology, Guidelines on Firewalls and Firewall Policy, NIST SP 800-41 Rev. 1, 2009. [Online]. Available: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-41r1.pdf.

[14] Microsoft Threat Intelligence, "WannaCrypt ransomware worm targets out-of-date systems," Microsoft Security Blog, May 2017. [Online]. Available: https://www.microsoft.com/en-us/security/blog/2017/05/12/wannacrypt-ransomware-worm-targets-out-of-date-systems/

[15] Kali Linux, "What is Kali Linux?," Kali Linux Documentation. [Online]. Available: https://www.kali.org/docs/introduction/what-is-kali-linux/. [Accessed: Oct. 4, 2026].

[16] G. Lyon, *Nmap Network Scanning: The Official Nmap Project Guide to Network Discovery and Vulnerability Scanning*. Sunnyvale, CA: Insecure.Com LLC, 2009.

[17] P. Calderon and Nmap Project, "smb-vuln-ms17-010.nse Script Source Code," Nmap Project, 2017. [Online]. Available: https://svn.nmap.org/nmap/scripts/smb-vuln-ms17-010.nse

[18] Rapid7, "Metasploit Framework," Metasploit Documentation. [Online]. Available: https://docs.rapid7.com/metasploit/msf-overview/. [Accessed: Oct. 4, 2026].
