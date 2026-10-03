# CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ CÔNG CỤ KIỂM THỬ SMB

## 1.1. Tổng quan về giao thức SMB

### 1.1.1. Khái niệm và vai trò của SMB trong hệ điều hành Windows

Server Message Block (SMB) là giao thức truyền thông mạng hoạt động tại tầng ứng dụng (Application Layer) trong mô hình OSI, cung cấp cơ chế chia sẻ tệp tin, thư mục, máy in và hỗ trợ giao tiếp liên tiến trình (Inter-Process Communication - IPC) giữa các máy tính trong mạng nội bộ [1]. Trên hệ điều hành Windows, SMB là giao thức truyền thông mặc định cho các dịch vụ chia sẻ tài nguyên, vận hành trực tiếp trên nền giao thức TCP qua cổng 445 hoặc thông qua tầng trung gian NetBIOS over TCP/IP (NBT) qua cổng 139 [2].

Trong kiến trúc hệ thống Windows, giao thức SMB đảm nhiệm bốn vai trò kỹ thuật chính:
1. **Chia sẻ tệp tin và dữ liệu từ xa:** Cho phép người dùng và ứng dụng thực hiện các thao tác đọc, ghi, tạo mới, khóa tệp và điều chỉnh thuộc tính trực tiếp trên các thư mục chia sẻ qua mạng (Network Shares) với trải nghiệm tương tự thao tác trên hệ thống tệp cục bộ [3].
2. **Quản lý thiết bị in ấn nội bộ:** Hỗ trợ tiếp nhận lệnh in, chuyển tiếp luồng dữ liệu in và điều phối hàng đợi tài liệu đối với các máy in dùng chung [2].
3. **Giao tiếp liên tiến trình (IPC) và quản trị từ xa:** Cung cấp cơ chế đường ống định danh (Named Pipes) phục vụ việc truyền tải các lệnh gọi thủ tục từ xa (Remote Procedure Call - RPC). SMB Named Pipes hỗ trợ một số cơ chế RPC và các tác vụ quản trị từ xa của Windows, đặc biệt đối với các dịch vụ được triển khai qua named pipe [3], [4].
4. **Xác thực và kiểm soát quyền truy cập:** Tích hợp với hệ thống an ninh nội tại của Windows (sử dụng giao thức xác thực NTLM hoặc Kerberos), cho phép máy chủ kiểm tra danh tính và đối chiếu quyền hạn của người dùng trước khi cấp quyền thao tác với tài nguyên [4].

### 1.1.2. Mô hình Client – Server

Dịch vụ SMB trên hệ điều hành Windows vận hành theo mô hình Client – Server, được phân định giữa không gian người dùng (User Mode) và không gian nhân hệ điều hành (Kernel Mode) [3]:

- **Phía SMB Client:** Dịch vụ Workstation (tiến trình `LanmanWorkstation`) tại User Mode tiếp nhận yêu cầu truy xuất tài nguyên mạng từ các ứng dụng người dùng thông qua đường dẫn UNC (Universal Naming Convention, dạng `\\Server\Share\File`). Yêu cầu này sau đó được chuyển giao xuống trình chuyển hướng mạng ở tầng kernel để đóng gói thành bản tin SMB và truyền qua ngăn xếp mạng TCP/IP [3].
- **Phía SMB Server:** Dịch vụ Server (tiến trình `LanmanServer`) tại User Mode quản lý cấu hình chia sẻ, đồng thời sử dụng trình điều khiển chế độ nhân trực tiếp để xử lý các gói tin mạng nhận về. Đối với các phiên bản SMBv1, thành phần điều khiển cốt lõi trong kernel là driver `srv.sys` [3], [4].

Việc xử lý phân tích cú pháp (parsing) bản tin và thực thi các thao tác I/O của SMB Server ngay trong Kernel Mode giúp tối ưu hiệu năng truyền tải dữ liệu. Tuy nhiên, kiến trúc này đặt ra rủi ro kỹ thuật: nếu driver xử lý gói tin trong kernel xuất hiện lỗi kiểm tra biên bộ nhớ, kẻ tấn công có thể lợi dụng để thực thi mã với đặc quyền của tài khoản hệ thống (`NT AUTHORITY\SYSTEM`), hoặc gây lỗi dừng hệ điều hành (màn hình xanh - BSOD) [3], [5].

```
+-------------------------------------------------------------------------+
|                                USER MODE                                |
|  +---------------------------+           +---------------------------+  |
|  |     Ứng dụng người dùng   |           |    Dịch vụ quản trị       |  |
|  +-------------+-------------+           +-------------+-------------+  |
|                | API I/O                               | RPC / Named    |
|                v                                       v     Pipes      |
|  +---------------------------+           +---------------------------+  |
|  | LanmanWorkstation Service |           |   LanmanServer Service    |  |
|  +---------------------------+           +---------------------------+  |
+------------------------------------+------------------------------------+
                                     | Chuyển giao I/O
+------------------------------------+------------------------------------+
|                               KERNEL MODE                               |
|  +---------------------------+           +---------------------------+  |
|  |    Trình chuyển hướng     |           |     SMB Server Driver     |  |
|  |     (Network Client)      |           |         (srv.sys)         |  |
|  +-------------+-------------+           +-------------^-------------+  |
|                | Đóng gói bản tin                      | Phân tích cú   |
|                v                                       | pháp bản tin   |
|  +---------------------------+           +-------------+-------------+  |
|  |    Ngăn xếp TCP/IP        |           |    Ngăn xếp TCP/IP        |  |
|  |       (tcpip.sys)         |<=========>|       (tcpip.sys)         |  |
|  +---------------------------+  TCP 445  +---------------------------+  |
|          [SMB Client]           TCP 139          [SMB Server]           |
+-------------------------------------------------------------------------+
```
*Sơ đồ 1.1: Kiến trúc phân tầng Client – Server của dịch vụ SMB trên Windows.*

### 1.1.3. Phân biệt SMBv1, SMBv2 và SMBv3

Giao thức Server Message Block đã trải qua ba thế hệ phiên bản chính, phản ánh sự thay đổi về hiệu năng truyền tải và cơ chế an toàn thông tin [1], [6]:

#### 1. Phiên bản SMBv1 (CIFS)
Được phát triển từ những năm 1980 và tích hợp sâu từ các thế hệ Windows NT/2000/XP. SMBv1 hỗ trợ hơn 100 mã lệnh điều khiển (`SMB_COM_*`). SMBv1 sử dụng tập lệnh lớn và nhiều thao tác đòi hỏi các lượt yêu cầu – phản hồi (request–response) riêng biệt, làm tăng độ trễ và lưu lượng trao đổi (chatty protocol) của giao thức [1], [6]. Về mặt an ninh, SMBv1 không hỗ trợ mã hóa luồng dữ liệu, cơ chế ký số (SMB Signing) dựa trên hàm băm MD5; cấu trúc driver xử lý `srv.sys` phức tạp, tiềm ẩn nhiều lỗi quản lý bộ nhớ [5], [7].

#### 2. Phiên bản SMBv2
Được Microsoft giới thiệu từ Windows Vista và Windows Server 2008 nhằm thay thế SMBv1. SMBv2 tinh giản tập mã lệnh xuống còn 19 lệnh tiêu chuẩn (`SMB2_*`), bổ sung tính năng gộp lệnh (Compounding) cho phép ghép nhiều yêu cầu (ví dụ: mở tệp, đọc tệp, đóng tệp) trong một gói tin duy nhất [6]. SMBv2 nâng cấp cơ chế ký số chống giả mạo lên thuật toán HMAC-SHA256, mở rộng bộ nhớ đệm và hỗ trợ xử lý I/O bất đồng bộ, giúp nâng cao hiệu năng và độ ổn định [3], [6].

#### 3. Phiên bản SMBv3
Được giới thiệu từ Windows 8 và Windows Server 2012, tiếp tục hoàn thiện trên Windows 10 và Windows Server 2016 với các cơ chế bảo mật theo từng dialect cụ thể [6], [7]:
- **SMB 3.0 (Windows 8 / Server 2012):** Bổ sung tính năng mã hóa dữ liệu đầu cuối (SMB Encryption) ở tầng ứng dụng bằng thuật toán mã hóa khối đối xứng AES-128-CCM (Counter with CBC-MAC), loại bỏ sự phụ thuộc vào hạ tầng IPsec; nâng cấp cơ chế ký số sang thuật toán AES-128-CMAC; đồng thời bổ sung cơ chế đàm phán phương ngữ an toàn (Secure Dialect Negotiation) nhằm ngăn chặn kẻ tấn công đứng giữa can thiệp sửa đổi gói tin Negotiate để hạ cấp giao thức [7].
- **SMB 3.0.2 (Windows 8.1 / Server 2012 R2):** Tối ưu hóa hiệu năng của thuật toán AES trong xử lý dữ liệu. Đồng thời từ phiên bản hệ điều hành này, Windows cung cấp khả năng quản trị cho phép gỡ bỏ hoặc vô hiệu hóa hoàn toàn tính năng SMBv1 thông qua công cụ quản lý của hệ điều hành [7], [8].
- **SMB 3.1.1 (Windows 10 / Server 2016 trở lên):** Bổ sung chế độ mã hóa AES-128-GCM (Galois/Counter Mode); tích hợp cơ chế bảo vệ tính toàn vẹn tiền xác thực (Pre-authentication Integrity). Cơ chế này sử dụng hàm băm SHA-512 tính toán trên chuỗi bản tin đàm phán (Negotiate và Session Setup) từ trước khi phiên xác thực hoàn tất; nếu kẻ tấn công can thiệp làm sai lệch năng lực bảo mật hoặc ép hạ cấp giao thức, chuỗi băm sẽ không khớp và kết nối bị hủy bỏ [7].

*Mối liên hệ với đề tài:* Dịch vụ SMBv2 và SMBv3 vận hành trên driver tách biệt (`srv2.sys`) chứ không sử dụng driver `srv.sys` của SMBv1. Khi SMBv1 bị vô hiệu hóa, máy chủ không còn tiếp nhận các yêu cầu SMBv1 thuộc bề mặt khai thác của MS17-010; vì vậy nguy cơ khai thác nhóm lỗ hổng này qua SMBv1 được loại bỏ trong cấu hình đó [7], [8].

*Bảng 1.1: So sánh đặc tính kỹ thuật cơ bản giữa SMBv1, SMBv2 và SMBv3 [1], [3], [6], [7], [8].*

| Đặc tính kỹ thuật | SMBv1 (CIFS) | SMBv2 (2.0.2 / 2.1) | SMBv3 (3.0 / 3.0.2 / 3.1.1) |
|---|---|---|---|
| **Hệ điều hành đầu tiên** | Windows 2000 / XP | Windows Vista / Server 2008 | Windows 8 / Server 2012 / Win 10 |
| **Số lượng mã lệnh** | Hơn 100 mã lệnh (`SMB_COM_*`) | 19 mã lệnh (`SMB2_*`) | 19 mã lệnh tiêu chuẩn |
| **Cơ chế xử lý lệnh** | Tuần tự từng bước | Hỗ trợ gộp lệnh (Compounding) | Gộp lệnh tối ưu |
| **Cổng mạng kết nối** | TCP 139 và TCP 445 | TCP 445 | TCP 445 |
| **Ký số (SMB Signing)** | MD5-based | HMAC-SHA256 | AES-CMAC (3.0 / 3.0.2); GMAC trên một số hệ thống mới hỗ trợ SMB 3.1.1 |
| **Mã hóa dữ liệu** | Không có SMB Encryption tích hợp | Không hỗ trợ | AES-128-CCM (3.0); AES-128-GCM (3.1.1) |
| **Bảo vệ tiền xác thực** | Không hỗ trợ | Không hỗ trợ | Chỉ SMB 3.1.1: Pre-authentication Integrity dùng SHA-512 |
| **Cơ chế bảo vệ nổi bật** | Giao thức legacy, không có encryption tích hợp | Ký số HMAC-SHA256, hỗ trợ gộp lệnh | Mã hóa khối AES và bảo vệ toàn vẹn tùy dialect |

### 1.1.4. Phân tích cổng mạng TCP 139 và TCP 445

Để trao đổi dữ liệu giữa Client và Server, hệ điều hành Windows sử dụng hai cổng dịch vụ mạng chính với cơ chế hoạt động khác nhau [1], [2]:

- **Cổng TCP 139 (NetBIOS over TCP/IP - NBT):** Là cổng giao tiếp truyền thống của SMB thời kỳ đầu, vận hành qua tầng trung gian NetBIOS Session Service (RFC 1001/1002). Để gửi gói tin SMB tới cổng 139, hai máy trạm bắt buộc phải thiết lập phiên NetBIOS trước tiên và phân giải tên máy thông qua WINS hoặc phát quảng bá (Broadcast). Cơ chế này phụ thuộc vào cấu hình tên NetBIOS, độ trễ cao và khó định tuyến qua các mạng diện rộng [1].
- **Cổng TCP 445 (Direct-hosted SMB):** Được đưa vào sử dụng từ Windows 2000 nhằm loại bỏ tầng trung gian NetBIOS. Các gói tin SMB được đóng gói trực tiếp trên giao thức TCP (chỉ kèm theo một tiêu đề ngắn 4-byte chỉ thị độ dài). Cổng 445 hỗ trợ phân giải địa chỉ trực tiếp qua DNS hoặc kết nối thẳng bằng địa chỉ IP, tối ưu tốc độ truyền tải và tương thích với hạ tầng định tuyến IP hiện đại [2], [3].

**Cơ chế thử cổng và lùi bước (Fallback):**
Khi một máy trạm Windows khởi tạo kết nối tới máy chủ chia sẻ tệp, ngăn xếp mạng mặc định sẽ gửi đồng thời hai gói tin bắt tay TCP SYN đến cả cổng 445 và cổng 139 của máy đích [2]:
- Nếu cổng 445 phản hồi trước (SYN-ACK), Client sẽ hoàn tất bắt tay trên cổng 445 và phát gói RST để hủy kết nối trên cổng 139. Phiên làm việc sau đó diễn ra trực tiếp qua cổng 445.
- Nếu cổng 445 bị chặn hoặc không phản hồi nhưng cổng 139 phản hồi, kết nối sẽ tự động lùi về vận hành qua cổng 139 (nếu máy trạm chưa vô hiệu hóa NetBIOS) [2].

Cơ chế này có ý nghĩa đối với thực nghiệm: phát hiện cổng TCP 445 ở trạng thái `open` cho thấy có dịch vụ đang lắng nghe trên cổng thường được sử dụng cho Direct-hosted SMB; cần thực hiện bước nhận diện dịch vụ hoặc đàm phán SMB để xác nhận. Đồng thời khi thực hiện phòng thủ, nếu chỉ chặn cổng 445 mà bỏ quên cổng 139 (kèm NetBIOS) thì bề mặt phơi nhiễm SMB vẫn chưa được xử lý đầy đủ [2], [9].

### 1.1.5. Quy trình trao đổi bản tin cơ bản

Quá trình giao tiếp giữa SMB Client và SMB Server tuân thủ trình tự thiết lập phiên ba giai đoạn trước khi có thể thao tác với dữ liệu hoặc thực thi lệnh [2], [3], [4]:

1. **Giai đoạn 1: Thỏa thuận giao thức (Negotiate Protocol):**
   Ngay sau khi hoàn tất bắt tay 3 bước TCP, Client gửi bản tin `Negotiate Request` chứa danh sách các chuỗi định danh phiên bản (Dialect) mà nó hỗ trợ (ví dụ: `"NT LM 0.12"` cho SMBv1, hoặc các mã hex cho SMBv2/v3). Server đối chiếu với cấu hình nội tại, chọn ra dialect cao nhất mà hai bên cùng hỗ trợ để phản hồi trong bản tin `Negotiate Response`, kèm theo các thông số an ninh sơ bộ (yêu cầu ký số, khả năng hỗ trợ bảo mật) [2], [4].
2. **Giai đoạn 2: Thiết lập phiên làm việc (Session Setup):**
   Client gửi bản tin `Session Setup Request` đính kèm thông tin xác thực danh tính (thông qua giao thức NTLM hoặc Kerberos). Trong môi trường kiểm thử hoặc với cấu hình mở, phiên kết nối có thể ở dạng vô danh (Anonymous / Null Session). Server kiểm tra thông tin, xác thực danh tính và phản hồi bản tin `Session Setup Response` kèm theo mã định danh phiên: **UID** (đối với SMBv1) hoặc **Session ID** (đối với SMBv2/v3) [3], [4].
3. **Giai đoạn 3: Gắn kết tài nguyên (Tree Connect):**
   Sau khi có UID hoặc Session ID hợp lệ, Client gửi bản tin `Tree Connect Request` chỉ định đường dẫn tài nguyên chia sẻ qua định dạng UNC, ví dụ: `\\Server\ShareName` hoặc kết nối vào đường ống chia sẻ liên tiến trình `\\Server\IPC$` (Inter-Process Communication). Server kiểm tra danh sách quyền truy cập (ACL); nếu hợp lệ, Server phản hồi bản tin `Tree Connect Response` và cấp phát một mã định danh liên kết: **TID** (đối với SMBv1) hoặc **Tree ID** (đối với SMBv2/v3) [3].

Từ thời điểm này, mọi thao tác đọc, ghi tệp hoặc giao tiếp RPC qua Named Pipes đều phải đính kèm đồng thời cặp định danh phiên và định danh kết nối tương ứng (`UID/TID` trong SMBv1, hoặc `Session ID/Tree ID` trong SMBv2/v3).

```
Client                                                              Server
  │                                                                   │
  │─── 1. Bắt tay 3 bước TCP (SYN -> SYN-ACK -> ACK) ────────────────>│ (Port 445/139)
  │                                                                   │
  │─── 2. Negotiate Protocol Request (Danh sách Dialects) ───────────>│
  │<──    Negotiate Protocol Response (Dialect được chọn + Security) ─│
  │                                                                   │
  │─── 3. Session Setup Request (Xác thực NTLM / Null Session) ──────>│
  │<──    Session Setup Response (Cấp phát UID [v1] / Session ID) ────│
  │                                                                   │
  │─── 4. Tree Connect Request (Đường dẫn tài nguyên: \\Server\IPC$) ─>│
  │<──    Tree Connect Response (Cấp phát TID [v1] / Tree ID) ────────│
  │                                                                   │
  │─── 5. Thao tác dữ liệu / Gọi lệnh RPC qua Named Pipes ───────────>│
  │<──    Kết quả phản hồi từ Server ─────────────────────────────────│
```
*Sơ đồ 1.2: Trình tự trao đổi bản tin cơ bản trong giao tiếp SMB giữa Client và Server.*

---

## 1.2. Lỗ hổng bảo mật MS17-010

### 1.2.1. Tổng quan về bản tin an ninh MS17-010

Vào tháng 03 năm 2017, Microsoft phát hành bản tin an ninh định kỳ mang mã hiệu **MS17-010** nhằm khắc phục các lỗ hổng nghiêm trọng trong việc xử lý gói tin của dịch vụ SMBv1 trên hệ điều hành Windows [5]. Nhóm lỗ hổng này ảnh hưởng tới hầu hết các phiên bản Windows lưu hành tại thời điểm đó, bao gồm Windows Vista, Windows 7, Windows 8.1, Windows 10, cùng các dòng máy chủ Windows Server 2008, 2012 và 2016. Do tính chất nghiêm trọng, Microsoft sau đó đã phát hành thêm bản vá cho các hệ điều hành đã dừng hỗ trợ như Windows XP và Windows Server 2003 [5].

Các lỗ hổng thực thi mã từ xa trong bản tin MS17-010 cho phép kẻ tấn công gửi các bản tin SMBv1 được chế tạo đặc biệt tới máy chủ mục tiêu. Trong nhiều trường hợp, việc khai thác có thể được thực hiện từ xa mà không cần thông tin xác thực hợp lệ [5]. Trong phạm vi đề tài, CVE-2017-0144 / EternalBlue được lựa chọn làm trường hợp kiểm thử chính.

### 1.2.2. Phân loại các mã CVE và danh mục bản vá theo hệ điều hành

Bản tin an ninh MS17-010 xử lý một nhóm gồm 6 mã định danh lỗ hổng phổ biến (CVE) cùng tồn tại trong driver xử lý SMBv1 `srv.sys` [5]. Các công cụ khai thác do nhóm The Shadow Brokers công bố vào tháng 4/2017 đã tận dụng các khiếm khuyết kỹ thuật này để vượt qua cơ chế bảo vệ của Windows [5]. Để trình bày rõ ràng, nội dung được phân tách thành hai bảng: Bảng 1.2 mô tả đặc tính kỹ thuật từng CVE và Bảng 1.3 liệt kê danh mục mã bản vá KB chính thức theo từng phiên bản hệ điều hành.

*Bảng 1.2: Phân loại các mã CVE trong bản tin an ninh Microsoft MS17-010 [5], [10], [11], [12].*

| Mã CVE | Liên hệ exploit | Phân loại theo nguồn chính thức | Tác động | Vai trò trong đồ án |
|---|---|---|---|---|
| **CVE-2017-0143** | **EternalSynergy** [10] | SMBv1 Remote Code Execution Vulnerability | RCE | Tham chiếu trong nhóm MS17-010 |
| **CVE-2017-0144** | **EternalBlue** [11] | SMBv1 Remote Code Execution Vulnerability; EternalBlue khai thác lỗi xử lý FEA trong `srv.sys` | RCE | **Mục tiêu thực nghiệm chính** |
| **CVE-2017-0145** | **EternalRomance** [12] | SMBv1 Remote Code Execution Vulnerability | RCE | Tham chiếu lịch sử / đối chiếu |
| **CVE-2017-0146** | Không gắn nickname | SMBv1 Remote Code Execution Vulnerability | RCE | Thuộc phạm vi MS17-010 |
| **CVE-2017-0147** | Không gắn nickname | SMBv1 Information Disclosure Vulnerability | Information Disclosure | Thuộc phạm vi MS17-010 |
| **CVE-2017-0148** | Không gắn nickname | SMBv1 Remote Code Execution Vulnerability | RCE | Thuộc phạm vi MS17-010 |

Sau Bảng 1.2, đề tài chỉ phân tích sâu cơ chế của CVE-2017-0144, vì đây là mục tiêu thực nghiệm trung tâm của kịch bản lab.

*Bảng 1.3: Danh mục mã bản vá KB chính thức của Microsoft theo hệ điều hành Windows [5].*

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

Nguyên nhân kỹ thuật phát sinh lỗ hổng CVE-2017-0144 liên quan đến lỗi xử lý cấu trúc File Extended Attributes (FEA) trong driver điều khiển `srv.sys` của hệ điều hành Windows khi phân tích các yêu cầu giao dịch SMBv1 [3], [5], [13]. Cơ chế phát sinh và khai thác lỗ hổng được mô tả qua ba bước logic sau:

- **Bước 1: Xử lý dữ liệu giao dịch sai kích thước khi phân tích danh sách FEA.**
  Trong giao thức SMBv1, client có thể gửi thông tin thuộc tính mở rộng của tệp tin thông qua cấu trúc danh sách FEA (`FEA_LIST`). Để truyền tải dữ liệu lớn, client sử dụng các hàm giao dịch (Transaction requests) cho phép chia nhỏ dữ liệu thành nhiều gói bổ sung thứ cấp để server ghép lại trong bộ nhớ [2]. Trong quá trình chuyển đổi danh sách FEA từ định dạng OS/2 sang định dạng NT thông qua hàm nội bộ `SrvOs2FeaToNt` (kèm theo hàm tính toán độ dài `SrvOs2FeaListSizeToNt`), driver `srv.sys` gặp lỗi sai lệch toán học khi ép kiểu kích thước, dẫn đến tính toán sai tổng dung lượng bộ đệm cần thiết [3], [13].
- **Bước 2: Sai lệch tính toán dẫn đến cấp phát vùng nhớ không phù hợp và ghi ngoài biên.**
  Do sai lệch trong việc kiểm tra kích thước danh sách FEA, driver `srv.sys` cấp phát một vùng nhớ trong bộ nhớ nhân (Non-Paged Pool) có dung lượng nhỏ hơn khối dữ liệu thực tế mà client gửi tới. Khi driver thực hiện thao tác sao chép dữ liệu thuộc tính vào bộ nhớ đệm này, dữ liệu thừa đã bị ghi tràn ra ngoài phạm vi vùng nhớ được cấp phát (out-of-bounds write / buffer overflow), làm sai lệch các cấu trúc quản lý bộ nhớ kế cận trong kernel [3], [13].
- **Bước 3: EternalBlue kết hợp lỗi bộ nhớ với kỹ thuật bố trí vùng nhớ để thực thi mã.**
  Mã khai thác EternalBlue gửi một chuỗi gói tin SMB được thiết kế theo trình tự nhằm sắp xếp bố cục các khối nhớ trong Non-Paged Pool (heap grooming). Khi lỗi tràn bộ nhớ xảy ra, dữ liệu ghi đè can thiệp vào các con trỏ điều khiển trong kernel, cho phép chuyển hướng luồng thực thi của bộ xử lý tới đoạn mã thực thi (Shellcode) do kẻ tấn công đưa vào bộ nhớ. Kết quả là đoạn mã được kích hoạt trực tiếp trong không gian nhân với đặc quyền `SYSTEM` [11], [13].

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

Để một hệ thống Windows nằm trong phạm vi có thể bị khai thác CVE-2017-0144, cần xem xét các điều kiện kỹ thuật sau [5], [11], [13]:
1. **Hệ điều hành:** Đang sử dụng phiên bản Windows thuộc danh mục bị ảnh hưởng (từ Windows XP đến Windows 10 các bản dựng đầu, hoặc Windows Server 2003 đến 2016) [5]. Trong phạm vi thực nghiệm, đề tài lựa chọn Windows 7 SP1 x64 làm máy mục tiêu do thuộc nhóm hệ điều hành bị ảnh hưởng và được module Metasploit hỗ trợ trong kịch bản kiểm thử của đề tài [13].
2. **Tính năng SMBv1 đang được kích hoạt:** Driver xử lý `srv.sys` đang hoạt động và tiếp nhận các yêu cầu giao dịch SMBv1 [8].
3. **Cổng dịch vụ mạng có thể tiếp cận được:** Cổng TCP 445 (hoặc TCP 139) ở trạng thái mở và không bị chặn bởi tường lửa mạng hoặc tường lửa cục bộ [9].
4. **Chưa cài đặt bản vá an ninh MS17-010:** Hệ điều hành chưa được cập nhật gói vá bảo mật tương ứng theo danh mục ở Bảng 1.3 [5].
5. **Đặc điểm xác thực:** CVE-2017-0144 có thể được khai thác từ xa mà không yêu cầu tài khoản xác thực hợp lệ khi dịch vụ SMBv1 mục tiêu có thể tiếp cận [5], [11]. Việc sử dụng `IPC$` trong đề tài chủ yếu xuất hiện ở cơ chế thăm dò của kịch bản Nmap và được phân tích chi tiết tại Mục 1.3.3.

**Nguyên tắc đánh giá:** Cần phân biệt giữa việc "hệ thống mở cổng 445" hoặc "hệ thống đang bật SMBv1" với việc "hệ thống có lỗ hổng MS17-010". Một máy tính đã cài đặt bản vá bảo mật vẫn mở cổng 445 để phục vụ chia sẻ tệp bình thường, nhưng driver `srv.sys` đã được bổ sung đoạn mã kiểm tra tính hợp lệ của tham số, do đó không còn bị ảnh hưởng bởi lỗi tràn bộ nhớ này [5], [8].

### 1.2.5. Đánh giá tác động an toàn thông tin theo tam giác CIA

Các lỗ hổng thực thi mã từ xa trong bản tin MS17-010, đặc biệt là CVE-2017-0144 được lựa chọn làm mục tiêu thực nghiệm trong đề tài, có thể cho phép kẻ tấn công đạt khả năng thực thi mã với đặc quyền cao trong không gian nhân. Từ đó, tác động an toàn thông tin được xem xét theo ba trụ cột (tam giác CIA) như sau [3], [9], [11], [13]:

- **Tính bí mật (Confidentiality):** Khi bị khai thác thành công, kẻ tấn công có thể truy cập trái phép vào dữ liệu lưu trữ trên các phân vùng đĩa, cơ sở dữ liệu và bộ nhớ hệ thống. Các thông tin nhạy cảm như tệp tin cấu hình, tài liệu hoặc thông tin xác thực lưu trong bộ nhớ có thể bị thu thập mà không chịu sự kiểm soát của phân quyền tệp cục bộ [3], [9].
- **Tính toàn vẹn (Integrity):** Với quyền hạn chiếm được, kẻ tấn công có khả năng thay đổi tệp tin dữ liệu, can thiệp cấu hình hệ thống, sửa đổi chính sách bảo mật, tạo tài khoản người dùng mới hoặc cài đặt các dịch vụ ngầm nhằm duy trì quyền truy cập trên mục tiêu [9], [11].
- **Tính sẵn sàng (Availability):** Khai thác lỗ hổng có thể dẫn tới việc máy chủ bị tắt, khởi động lại hoặc dữ liệu bị mã hóa/xóa bỏ. Ngoài ra, do can thiệp vào bộ nhớ kernel, nếu mã khai thác gặp lỗi không tương thích với cấu trúc bộ nhớ của bản dựng Windows cụ thể, hệ điều hành có thể gặp lỗi trang nghiêm trọng và rơi vào trạng thái màn hình xanh (BSOD), làm gián đoạn các dịch vụ đang cung cấp [3], [13].

### 1.2.6. Khái quát các chiến dịch tấn công thực tế liên quan

Sự kết hợp giữa lỗ hổng MS17-010 và mã khai thác EternalBlue đã được ghi nhận trong các sự cố an ninh mạng diện rộng trên thế giới [12], [14], [15]:

- **Mã độc tống tiền WannaCry (Tháng 05/2017):** WannaCry kết hợp mã khai thác EternalBlue với tính năng tự quét mạng. Khi lây nhiễm vào một máy tính, mã độc tự động quét cổng TCP 445 của các dải mạng lân cận, khai thác lỗ hổng MS17-010 trên các máy chưa vá để nhân bản và mã hóa tệp tin đòi tiền chuộc [14]. Vụ tấn công đã gây gián đoạn hoạt động của nhiều cơ quan y tế, ngân hàng và doanh nghiệp tại hơn 150 quốc gia [14], [15].
- **Mã độc NotPetya (Tháng 06/2017):** NotPetya sử dụng mã khai thác liên quan đến MS17-010 (bao gồm EternalBlue và EternalRomance) để lây lan qua mạng nội bộ. Mục tiêu chính của NotPetya là phá hoại cấu trúc hệ thống tệp và bản ghi khởi động (MBR), khiến hệ thống không thể khôi phục, gây thiệt hại cho nhiều tập đoàn vận tải và hạ tầng quốc tế [12].

Các sự cố này cho thấy việc kiểm tra, xác minh và áp dụng các biện pháp phòng thủ cho dịch vụ SMB là nhiệm vụ kỹ thuật có ý nghĩa thực tiễn trong quản trị hệ thống.

---

## 1.3. Công cụ phục vụ kiểm thử

### 1.3.1. Hệ điều hành kiểm thử Kali Linux

Kali Linux là bản phân phối Linux mã nguồn mở dựa trên Debian, được cấu hình sẵn các công cụ phục vụ kiểm tra an toàn mạng, đánh giá lỗ hổng và kiểm thử xâm nhập [16]. Trong đề tài, Kali Linux được lựa chọn làm máy trạm kiểm thử nhờ các yếu tố:
- Cung cấp môi trường mạng ổn định, hỗ trợ thao tác gói tin ở mức raw socket phục vụ trinh sát mạng.
- Tích hợp sẵn các bộ công cụ kiểm thử tiêu chuẩn như Nmap, Metasploit Framework, Wireshark và các thư viện hỗ trợ giao thức SMB.
- Đảm bảo môi trường thực nghiệm độc lập với hệ thống Windows mục tiêu [16].

### 1.3.2. Công cụ quét mạng Nmap

Nmap (Network Mapper) là công cụ quét mạng và kiểm tra dịch vụ tiêu chuẩn [17]. Trong quy trình kiểm thử SMB, Nmap đảm nhiệm các vai trò cụ thể:
- **Phát hiện trạng thái cổng (`-sS`, `-p 139,445`):** Sử dụng kỹ thuật quét TCP SYN (quét bán mở) để xác định xem cổng TCP 445 hoặc TCP 139 trên máy mục tiêu có đang mở (`open`) hay không mà không cần thiết lập phiên kết nối đầy đủ [17].
- **Nhận diện dịch vụ và phiên bản (`-sV`):** Thực hiện gửi các gói tin thăm dò (probes) tới cổng mở nhằm thu thập biểu ngữ phản hồi, từ đó định danh tên dịch vụ (ví dụ: `microsoft-ds`) và xác định thông tin phiên bản dịch vụ dựa trên cơ sở dữ liệu mẫu phản hồi của Nmap [17]. Cần lưu ý tùy chọn `-sV` tập trung nhận diện phiên bản của dịch vụ lắng nghe, trong khi việc nhận diện hệ điều hành thuộc về tùy chọn `-O` hoặc các script chuyên biệt.

### 1.3.3. Tự động hóa kiểm tra an toàn với Nmap Scripting Engine (NSE)

Nmap Scripting Engine (NSE) cho phép thực thi các tập kịch bản viết bằng ngôn ngữ Lua để tự động hóa các tác vụ kiểm tra an toàn nâng cao [17], [18]. Đối với dịch vụ SMB và lỗ hổng MS17-010:
- **Script `smb-protocols.nse`:** Gửi các yêu cầu Negotiate với danh sách dialect khác nhau để xác định máy chủ đích có đang chấp nhận giao tiếp qua giao thức SMBv1 (`"NT LM 0.12"`) hay không [17].
- **Script `smb-vuln-ms17-010.nse`:** Đây là kịch bản kiểm tra an toàn tiêu chuẩn (non-intrusive probe) giúp nhận biết dấu hiệu chưa vá MS17-010 mà không thực hiện hành vi khai thác bộ nhớ và không làm gián đoạn dịch vụ [18].

**Cơ chế kỹ thuật chi tiết của script `smb-vuln-ms17-010.nse`:**
1. Script thiết lập kết nối TCP tới cổng 445, gửi bản tin đàm phán Negotiate yêu cầu dialect SMBv1, sau đó thực hiện thủ tục Session Setup dưới dạng phiên ẩn danh (Anonymous / Null Session) và gửi Tree Connect vào tài nguyên chia sẻ liên tiến trình `\\Target\IPC$` (mặc định tham số `sharename` là `IPC$`) [18].
2. Khi phiên làm việc với `IPC$` được thiết lập, script gửi một bản tin yêu cầu giao dịch `SMB_COM_TRANSACTION` (opcode `0x25`) với lệnh `PeekNamedPipe` (mã `0x2300`) trên đường ống định danh `\PIPE\` với các tham số độ dài bộ đệm tối đa (`Max Parameter Count = 0xFFFF`, `Max Data Count = 0xFFFF`) [18].
3. **Phân tích mã trạng thái phản hồi NT Status theo mã nguồn Nmap:**
   - *Dấu hiệu phù hợp hệ thống chưa vá (VULNERABLE):* Nếu máy chủ phản hồi mã lỗi NT Status `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`), driver `srv.sys` của mục tiêu đang xử lý giao dịch theo nhánh mã nguồn lỗi chưa được vá. Script ghi nhận dấu hiệu này và xuất kết luận `State: VULNERABLE` [18].
   - *Dấu hiệu phù hợp hệ thống đã vá:* Nếu máy chủ phản hồi mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc `STATUS_INVALID_HANDLE` (`0xC0000008`), logic script xác định mục tiêu đã được áp dụng bản vá sửa lỗi hoặc từ chối xử lý tham số giao dịch bất thường một cách an toàn. Script ghi nhận trạng thái không có lỗ hổng (`State: NOT VULNERABLE`) kèm thông báo `This system is patched` [18].

**Ranh giới kỹ thuật và các trường hợp ngoại lệ của kết luận quét:**
Việc diễn giải kết quả từ script kiểm tra cần lưu ý các ranh giới kỹ thuật cụ thể:
- *Ảnh hưởng của chính sách hạn chế kết nối nặc danh:* Trong trường hợp không cung cấp thông tin xác thực, kịch bản kiểm tra `smb-vuln-ms17-010.nse` phụ thuộc vào việc kết nối ẩn danh tới tài nguyên `IPC$`. Nếu truy cập nặc danh tới `IPC$` bị chặn (như cấu hình `RestrictAnonymous = 2`) và người kiểm thử không cung cấp thông tin xác thực phù hợp, kịch bản có thể không hoàn tất được phép thăm dò và không xác định được trạng thái, dù driver `srv.sys` trên thực tế có thể chưa được vá. Công cụ có hỗ trợ truyền thông tin xác thực thông qua tham số nếu được cấu hình [18].
- *Ảnh hưởng của thiết bị bảo vệ mạng:* Tường lửa cá nhân hoặc hệ thống ngăn ngừa xâm nhập (IPS) có tính năng DPI có thể cho phép bắt tay TCP ban đầu nhưng ngắt kết nối bằng gói TCP RST ngay khi xuất hiện bản tin Transaction dị thường, dẫn đến việc đánh giá sai lệch trạng thái dịch vụ.
- *Bản chất của kết luận "VULNERABLE":* Kết luận từ công cụ quét chỉ xác nhận *máy chủ có phản ứng logic của driver `srv.sys` khớp với mẫu hành vi chưa vá*. Kết luận này không đồng nghĩa với việc một cuộc tấn công khai thác thực tế chắc chắn sẽ cấp được phiên shell tương tác thành công trong mọi trường hợp, bởi việc khai thác thực tế còn phụ thuộc vào kiến trúc CPU (x86 hay x64), trạng thái phân mảnh của bộ nhớ Non-Paged Pool (có thể gây sập hệ thống BSOD thay vì cấp shell), và sự ngăn chặn của các giải pháp bảo vệ điểm cuối (EDR/Antivirus) [17], [18].

### 1.3.4. Nền tảng kiểm thử Metasploit Framework

Metasploit Framework là nền tảng kiểm tra xâm nhập mô-đun hóa, hỗ trợ chuẩn hóa quy trình thẩm định an toàn thông tin [13], [19]. Trong phạm vi đề tài, Metasploit được phân bổ hai vai trò rõ ràng:
- **Mô-đun phụ trợ (Auxiliary Module):** Sử dụng mô-đun `auxiliary/scanner/smb/smb_ms17_010` để quét và kiểm tra dấu hiệu lỗ hổng trên dải địa chỉ IP [13]. Cần lưu ý mô-đun này và script NSE của Nmap là hai implementation khác nhau dùng để tham chiếu chéo về mặt phản ứng dịch vụ. Các đối chứng thực sự khác loại bao gồm: bản dựng Windows (build), danh sách Hotfix/KB đã cài đặt, lưu lượng gói tin (packet capture) và trạng thái tính năng SMBv1 trên máy mục tiêu.
- **Mô-đun khai thác có kiểm soát (Exploit Module):** Sử dụng mô-đun `exploit/windows/smb/ms17_010_eternalblue` trong môi trường phòng thí nghiệm cô lập nhằm thẩm định khả năng thực thi của lỗ hổng CVE-2017-0144 [13]. Payload được giới hạn ở các thao tác xác nhận quyền thực thi; bản thân quá trình khai thác kernel vẫn có nguy cơ gây mất ổn định hoặc phát sinh lỗi màn hình xanh (BSOD), vì vậy thực nghiệm chỉ tiến hành trên máy ảo đã tạo điểm sao lưu phục hồi (snapshot) [13], [16].

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
- **Tác động của thiết bị bảo vệ mạng:** Tường lửa cá nhân hoặc hệ thống ngăn ngừa xâm nhập (IPS) có tính năng DPI có thể cho phép bắt tay TCP ban đầu nhưng ngắt kết nối bằng gói TCP RST ngay khi xuất hiện bản tin Transaction dị thường, dẫn đến việc đánh giá sai lệch trạng thái dịch vụ.
- **Sự khác biệt giữa "Dấu hiệu chưa vá" và "Khả năng khai thác thành công":** Một hệ thống được công cụ báo `VULNERABLE` ở Cấp độ 3 chỉ phản ánh việc driver có phản ứng logic của mẫu hành vi cũ. Việc khai thác thực tế ở Cấp độ 4 còn chịu sự chi phối của kiến trúc CPU (x86 hay x64), mức độ phân mảnh của bộ nhớ Non-Paged Pool (dễ dẫn đến lỗi màn hình xanh BSOD thay vì thực thi shellcode ổn định), và sự ngăn chặn của các giải pháp bảo vệ điểm cuối (Endpoint Protection/EDR).
- **Biện pháp phòng ngừa:** Người kiểm thử cần đối chiếu kết quả Nmap/NSE và Metasploit scanner với phiên bản/build Windows, danh sách Hotfix/KB và trạng thái tính năng SMBv1 trên máy mục tiêu. Dữ liệu bắt gói tin (packet capture) và nhật ký sự kiện (Windows Event Logs) được sử dụng làm bằng chứng bổ sung khi cần phân tích nguyên nhân sai lệch [16], [17].

### 1.4.3. Nguyên tắc giảm thiểu rủi ro và phòng thủ giao thức SMB

Để bảo vệ hệ thống trước nguy cơ từ các lỗ hổng SMB và MS17-010, các nguyên tắc phòng thủ kỹ thuật cần được triển khai đồng bộ theo trình tự:

1. **Cập nhật bản vá an ninh định kỳ (Security Patching):**
   Cài đặt đầy đủ các bản vá an ninh do Microsoft phát hành theo danh mục ở Bảng 1.3 (ví dụ: gói KB4012212 hoặc các bản cập nhật tích lũy). Bản vá sửa đổi logic xử lý kích thước trong driver `srv.sys`, khắc phục nguyên nhân của lỗi tràn bộ đệm mà không làm gián đoạn hoạt động chia sẻ tệp cần thiết [5].
2. **Vô hiệu hóa giao thức SMBv1:**
   Do SMBv1 là giao thức legacy, tiềm ẩn nhiều khiếm khuyết kiến trúc và không hỗ trợ các tính năng an toàn hiện đại, khuyến nghị kỹ thuật là vô hiệu hóa tính năng này trên toàn bộ các máy trạm và máy chủ thông qua PowerShell, Group Policy (GPO) hoặc cài đặt Windows Features khi các ứng dụng không còn yêu cầu tương thích ngược [8].
3. **Kiểm soát và lọc cổng TCP 445 / 139 bằng tường lửa:**
   Cấu hình quy tắc tường lửa (Host Firewall và Network Firewall) để chặn kết nối tới cổng 445 và 139 từ các vùng mạng không tin cậy hoặc từ Internet. Dịch vụ chia sẻ tệp chỉ nên được phép truy cập từ các dải mạng nội bộ hoặc VLAN quản trị xác định [9].
4. **Phân đoạn mạng và cô lập dịch vụ (Network Segmentation):**
   Tách biệt các máy chủ dữ liệu quan trọng vào các phân vùng mạng riêng, áp dụng danh sách kiểm soát truy cập (ACL) giữa các vùng mạng nhằm hạn chế khả năng lây lan ngang (Lateral Movement) nếu một trạm làm việc trong mạng bị xâm nhập [9].
5. **Đánh giá ảnh hưởng tương thích:**
   Trước khi vô hiệu hóa SMBv1 hoặc chặn cổng mạng trong môi trường thực tế, cần rà soát các thiết bị ngoại vi cũ (máy in mạng đời cũ, thiết bị lưu trữ NAS cũ) để có phương án nâng cấp hoặc chuyển tiếp phù hợp, tránh gây gián đoạn nghiệp vụ [8].
6. **Quy trình kiểm thử lại (Retesting):**
   Sau khi áp dụng biện pháp phòng thủ, chạy lại cùng bộ kiểm thử để ghi nhận sự thay đổi trạng thái tương ứng. Kết quả cần chứng minh không còn chỉ báo MS17-010 theo tiêu chí đã xác định, đồng thời ghi nhận riêng trạng thái cổng và phiên bản SMB sau cấu hình [17].

---

## TỔNG KẾT CHƯƠNG 1

Chương 1 đã hệ thống hóa cơ sở lý thuyết về giao thức SMB, bản tin an ninh MS17-010 và các công cụ phục vụ công tác kiểm thử đánh giá an toàn thông tin:
1. Trình bày tổng quan kiến trúc Client – Server của giao thức SMB trên hệ điều hành Windows, phân biệt đặc tính kỹ thuật giữa ba thế hệ SMBv1, SMBv2, SMBv3, làm rõ cơ chế hoạt động của cổng TCP 139 và TCP 445, cùng quy trình trao đổi bản tin cơ bản qua ba giai đoạn: Negotiate Protocol, Session Setup và Tree Connect.
2. Phân tích nhóm lỗ hổng trong bản tin an ninh MS17-010, xây dựng bảng đối chiếu 6 mã CVE và danh mục mã bản vá KB chính thức theo từng phiên bản hệ điều hành; làm rõ nguyên nhân kỹ thuật của lỗ hổng CVE-2017-0144 liên quan đến cấu trúc FEA trong `srv.sys` theo mô hình 3 bước, xác định các điều kiện tồn tại nguy cơ và đánh giá tác động an toàn thông tin theo tam giác CIA.
3. Xác lập vai trò cụ thể của hệ điều hành Kali Linux, công cụ Nmap, Nmap Scripting Engine và Metasploit Framework trong các pha khảo sát, định danh và xác minh an ninh; đồng thời thiết lập bảng liên kết trực tiếp giữa các khái niệm lý thuyết với các bước quan sát và thao tác trong môi trường thực nghiệm.
4. Xây dựng khung phân định 4 cấp độ trạng thái dịch vụ và lỗ hổng nhằm chuẩn hóa nhận định kỹ thuật, chỉ rõ các giới hạn gây kết quả sai lệch và hệ thống hóa 6 nguyên tắc phòng thủ cơ bản để giảm thiểu rủi ro cho dịch vụ SMB.

Những nội dung lý thuyết, khung tiêu chí trạng thái và nguyên tắc phòng thủ được thiết lập trong chương này là cơ sở để tiến hành thiết kế mô hình mạng lab cô lập, cấu hình các máy trạm thực nghiệm và xây dựng kịch bản kiểm thử chi tiết trong Chương 2.

---

## TÀI LIỆU THAM KHẢO

[1] A. S. Tanenbaum, D. Wetherall, and N. Feamster, *Computer Networks*, 6th ed. Boston, MA: Pearson, 2021.

[2] Microsoft, "Direct hosting of SMB over TCP/IP," Microsoft Learn, 2023. [Online]. Available: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/direct-hosting-of-smb-over-tcpip

[3] P. Yosifovich, D. A. Solomon, and A. Ionescu, *Windows Internals, Part 1: System architecture, processes, threads, memory management, and more*, 7th ed. Redmond, WA: Microsoft Press, 2017.

[4] A. Allievi, M. E. Russinovich, D. A. Solomon, and A. Ionescu, *Windows Internals, Part 2*, 7th ed. Redmond, WA: Microsoft Press, 2021.

[5] Microsoft, "Microsoft Security Bulletin MS17-010 - Critical," Microsoft Learn / Security TechCenter, Mar. 2017. [Online]. Available: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010

[6] Microsoft, "Overview of file sharing using the SMB 3 protocol in Windows Server," Microsoft Learn, 2023. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-overview

[7] Microsoft, "SMB security enhancements," Microsoft Learn, 2023. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security

[8] Microsoft, "Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3

[9] C. McNab, *Network Security Assessment: Know Your Network*, 3rd ed. Sebastopol, CA: O'Reilly Media, 2016.

[10] Microsoft Security Response Center (MSRC), "Eternal Synergy Exploit Analysis," Microsoft, 2017. [Online]. Available: https://msrc.microsoft.com/blog/2017/05/eternal-synergy-exploit-analysis/

[11] National Institute of Standards and Technology (NIST), "CVE-2017-0144 Detail," National Vulnerability Database (NVD), Mar. 2017. [Online]. Available: https://nvd.nist.gov/vuln/detail/CVE-2017-0144

[12] Microsoft Threat Intelligence, "New ransomware, old techniques: Petya adds-worm capabilities," Microsoft Security Blog, Jun. 2017. [Online]. Available: https://www.microsoft.com/en-us/security/blog/2017/06/27/new-ransomware-old-techniques-petya-adds-worm-capabilities/

[13] Rapid7, "MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption," Rapid7 Exploit Database, 2017. [Online]. Available: https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/

[14] Cybersecurity and Infrastructure Security Agency (CISA), "Alert (TA17-132A): Indicators Associated With WannaCry Ransomware," US-CERT, May 2017. [Online]. Available: https://www.cisa.gov/news-events/alerts/2017/05/12/indicators-associated-wannacry-ransomware

[15] Microsoft Threat Intelligence, "WannaCrypt ransomware worm targets out-of-date systems," Microsoft Security Blog, May 2017. [Online]. Available: https://www.microsoft.com/en-us/security/blog/2017/05/12/wannacrypt-ransomware-worm-targets-out-of-date-systems/

[16] G. Weidman, *Penetration Testing: A Hands-On Introduction to Hacking*. San Francisco, CA: No Starch Press, 2014.

[17] G. Lyon, *Nmap Network Scanning: The Official Nmap Project Guide to Network Discovery and Vulnerability Scanning*. Sunnyvale, CA: Insecure.Com LLC, 2009.

[18] P. Calderon and Nmap Project, "smb-vuln-ms17-010.nse Script Source Code," Nmap Project, 2017. [Online]. Available: https://svn.nmap.org/nmap/scripts/smb-vuln-ms17-010.nse

[19] D. Kennedy, J. O'Gorman, D. Kearns, and M. Aharoni, *Metasploit: The Penetration Tester's Guide*, 2nd ed. San Francisco, CA: No Starch Press, 2024.
