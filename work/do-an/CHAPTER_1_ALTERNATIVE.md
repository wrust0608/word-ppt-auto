# CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ CÔNG CỤ KIỂM THỬ SMB

## 1.1. Kiến trúc giao thức SMB và cơ chế quản lý truyền thông trên Windows

### 1.1.1. Bản chất, vai trò của SMB và cơ chế giao tiếp liên tiến trình qua Named Pipes

Giao thức chia sẻ tài nguyên qua mạng (Server Message Block – SMB) là giao thức truyền thông ở tầng ứng dụng, cung cấp cơ chế truy cập tệp tin, máy in và các tài nguyên dùng chung trong mạng cục bộ của hệ điều hành Windows [1]. Khi hệ thống vận hành, các tương tác chia sẻ tài nguyên được trừu tượng hóa dưới dạng yêu cầu từ Client và phản hồi từ Server, giúp các ứng dụng làm việc với tệp tin ở xa tương tự như trên hệ thống lưu trữ cục bộ [1].

Bên cạnh chức năng truyền tệp tin thông thường, SMB giữ vai trò nền tảng cho cơ chế truyền thông liên tiến trình (Inter-Process Communication – IPC) thông qua đường ống định danh (Named Pipes) [1]. Cơ chế này cho phép các tiến trình mạng gửi và nhận dữ liệu qua lại mà không cần tự xây dựng giao thức truyền thông riêng biệt. Các dịch vụ hệ thống trọng yếu trên Windows, bao gồm dịch vụ quản lý máy chủ qua `\PIPE\srvsvc` hoặc dịch vụ xác thực bảo mật qua `\PIPE\lsarpc`, đều giao tiếp dựa trên Named Pipes thông qua tài nguyên chia sẻ ngầm định mang tên `IPC$` [1].

Kiến trúc SMB phân định rõ ràng vai trò giữa Client và Server. Client chịu trách nhiệm khởi tạo yêu cầu, đóng gói thông điệp và xử lý dữ liệu trả về; Server chịu trách nhiệm phân tích cú pháp yêu cầu, kiểm tra quyền truy cập và thực thi các thao tác trên tài nguyên [1]. Trên hệ điều hành Windows, thành phần Server được thực thi trực tiếp trong không gian nhân (Kernel Mode) thông qua các trình điều khiển thiết bị: `srv.sys` đối với SMBv1 và `srv2.sys` đối với SMBv2 cùng SMBv3 [1]. Việc các trình điều khiển này vận hành ở mức đặc quyền nhân đồng nghĩa với việc bất kỳ sai sót nào trong khâu xử lý thông điệp mạng đều có nguy cơ đe dọa trực tiếp sự ổn định và an ninh của toàn bộ hệ điều hành [1].

```text
+-----------------------------------------------------------+
|                   Không gian Người dùng                   |
|     Ứng dụng nghiệp vụ / Dịch vụ hệ thống Windows        |
+-----------------------------------------------------------+
                              |
                     Yêu cầu truy cập UNC
                              v
+-----------------------------------------------------------+
|                     Không gian Nhân                       |
|   Trình điều khiển SMB Server (srv.sys / srv2.sys)        |
|        - Quản lý phiên và quyền hạn (Session / Tree)       |
|        - Phân tích cú pháp thông điệp và giao dịch        |
|        - Giao tiếp liên tiến trình: Named Pipes (IPC$)    |
+-----------------------------------------------------------+
                              |
               Thông điệp SMB đã được đóng gói
                              v
+-----------------------------------------------------------+
|                    Tầng Vận chuyển                        |
|   Direct-hosted SMB (TCP 445)  /  NetBIOS over TCP (139)  |
+-----------------------------------------------------------+
```
*Sơ đồ 1.1: Mô hình phân tầng kiến trúc và ranh giới xử lý của dịch vụ SMB trên hệ điều hành Windows.*

### 1.1.2. Phân định cơ chế truyền tải: Direct-hosted SMB (TCP 445) và NetBIOS over TCP/IP (TCP 139)

Kênh truyền tải của dịch vụ SMB trên Windows trải qua quá trình tiến hóa gắn liền với sự thay đổi của kiến trúc mạng Internet. Ban đầu, SMB phụ thuộc vào giao diện NetBIOS over TCP/IP (NBT), vận hành trên cổng TCP 139 [2]. Trong mô hình này, việc thiết lập phiên truyền thông đòi hỏi một lớp bao bọc trung gian NetBIOS Session Service cùng quá trình phân giải tên NetBIOS máy trạm, làm gia tăng số lượng bản tin trao đổi và hạn chế khả năng định tuyến trên các mạng diện rộng [2].

Kể từ phiên bản Windows 2000, Microsoft bổ sung cơ chế Direct-hosted SMB vận hành trực tiếp trên cổng TCP 445 [2]. Trong cơ chế này, các thông điệp SMB được truyền trực tiếp trên nền giao thức TCP/IP mà không cần lớp tiêu đề NetBIOS, chỉ sử dụng một tiêu đề 4 byte để định nghĩa độ dài của thông điệp [2]. Cải tiến này giúp loại bỏ hoàn toàn sự phụ thuộc vào dịch vụ phân giải tên WINS, cho phép phân giải địa chỉ thông qua hệ thống phân giải tên miền (DNS) tiêu chuẩn, giảm độ trễ mạng và tối ưu hóa lưu lượng truyền tải dữ liệu [2].

Khi một máy trạm Windows khởi tạo kết nối chia sẻ tài nguyên tới một máy chủ trong mạng, hệ điều hành triển khai cơ chế bắt tay đồng thời nhằm duy trì tính tương thích ngược [2]. Cụ thể, Windows phát đi song song hai gói tin TCP SYN tới cả cổng 445 và cổng 139 của máy đích [2]. Nếu máy đích phản hồi gói tin TCP SYN-ACK trên cổng 445 trước, kết nối Direct-hosted SMB sẽ được thiết lập ngay lập tức, đồng thời yêu cầu tới cổng 139 sẽ bị hủy bỏ thông qua gói tin TCP RST [2]. Ngược lại, nếu cổng 445 bị chặn hoặc máy đích không hỗ trợ kết nối trực tiếp, hệ thống sẽ tự động lùi bước (fallback) để thiết lập phiên qua cổng 139 nếu dịch vụ NetBIOS còn hoạt động [2].

Ý nghĩa an ninh của cơ chế này là bề mặt tấn công của dịch vụ SMB không chỉ giới hạn ở một cổng duy nhất. Một trạm kiểm thử an ninh nếu chỉ tập trung rà soát cổng TCP 445 mà bỏ qua cổng TCP 139 có thể bỏ sót các đường dẫn kết nối tiềm ẩn, đặc biệt trong các hệ thống doanh nghiệp còn duy trì các máy chủ hoặc thiết bị ngoại vi đời cũ [2]. Do đó, việc đánh giá khả năng tiếp cận dịch vụ bắt buộc phải được tiến hành đồng thời trên cả hai cổng truyền tải [2].

### 1.1.3. Máy trạng thái giao thức SMB: Chuỗi giao dịch thương lượng, xác thực và liên kết tài nguyên

Mọi hoạt động truyền thông dữ liệu trong giao thức SMB đều phải tuân thủ nghiêm ngặt một máy trạng thái hữu hạn (State Machine) gồm ba giai đoạn bắt buộc trước khi dữ liệu tệp tin có thể được đọc hoặc ghi [3], [4]:

1. **Pha thương lượng giao thức (Negotiate Protocol):** Client gửi một danh sách chứa toàn bộ các dialect (phương ngữ giao thức) mà mình hỗ trợ [3], [4]. Server tiếp nhận danh sách, đối chiếu với các dialect được kích hoạt trên hệ thống và phản hồi lựa chọn dialect chung cao nhất mà cả hai bên cùng hỗ trợ [3], [4]. Thông điệp phản hồi từ Server đồng thời xác lập các tham số vận hành cốt lõi: kích thước bộ đệm truyền nhận tối đa, năng lực hỗ trợ ký số và mã nhận diện hệ thống [3], [4].
2. **Pha thiết lập phiên làm việc (Session Setup):** Sau khi dialect được thống nhất, Client gửi thông điệp yêu cầu xác thực danh tính người dùng [3], [4]. Quá trình này có thể diễn ra qua nhiều lượt trao đổi thông điệp xác thực bảo mật (Security Blob) dựa trên giao thức NTLM hoặc Kerberos. Trong quá trình trao đổi nhiều lượt, Server có thể phản hồi mã trạng thái `STATUS_MORE_PROCESSING_REQUIRED`, biểu thị rằng quá trình xác thực đang tiếp diễn bình thường chứ không phải lỗi [4]. Khi quá trình xác thực hoàn tất thành công, Server tạo lập ngữ cảnh bảo mật và cấp phát một mã định danh phiên: `UID` (User ID) trong SMBv1 hoặc `SessionId` 64-bit trong SMBv2/SMBv3 [3], [4].
3. **Pha liên kết tài nguyên (Tree Connect):** Khi đã sở hữu mã định danh phiên hợp lệ, Client gửi yêu cầu kết nối tới một tài nguyên chia sẻ cụ thể theo đường dẫn tài nguyên chuẩn (ví dụ: `\\Server\Data` hoặc `\\Server\IPC$`) [3], [4]. Server kiểm tra quyền hạn của danh tính người dùng đối với tài nguyên được yêu cầu. Nếu được cấp phép, Server trả về mã định danh kết nối tài nguyên: `TID` (Tree ID) trong SMBv1 hoặc `TreeId` trong SMBv2/SMBv3 [3], [4].

Sau khi hoàn tất cả ba pha, mọi yêu cầu đọc, ghi hoặc thao tác trên đường ống định danh đều phải mang theo cặp định danh (`UID`/`TID` hoặc `SessionId`/`TreeId`) tương ứng để Server định tuyến ngữ cảnh xử lý chính xác [3], [4]. Trong kiểm thử an ninh, việc phân định rõ từng pha giúp xác định chính xác ranh giới mà công cụ đạt tới. Việc vượt qua bước kết nối tới tài nguyên `IPC$` là điều kiện tiên quyết để gửi các gói tin thăm dò lỗ hổng vào hệ thống nhân [3], [4].

```text
Client                                                     Server
  |                                                          |
  |--------- 1. Yêu cầu thương lượng (Negotiate Request) --->|
  |<-------- Phản hồi chấp thuận Dialect cao nhất -----------|
  |                                                          |
  |--------- 2. Yêu cầu thiết lập phiên (Session Setup) ----->|
  |<-------- Cấp phát định danh phiên (UID / SessionId) -----|
  |                                                          |
  |--------- 3. Yêu cầu kết nối tài nguyên (Tree Connect) --->|
  |<-------- Cấp phát định danh cây tài nguyên (TID) --------|
  |                                                          |
  |========= Kênh truyền thông nghiệp vụ / Named Pipes ======|
  |                                                          |
```
*Sơ đồ 1.2: Chuỗi trạng thái giao tiếp chuẩn của giao thức SMB giữa Client và Server.*

### 1.1.4. Tiến hóa kiến trúc và ranh giới an ninh: SMBv1, SMBv2 và SMBv3

Quá trình phát triển từ SMBv1 đến SMBv3 phản ánh sự thay đổi căn bản trong tư duy thiết kế an ninh mạng của Microsoft, từ mô hình tin cậy nội bộ sang mô hình phòng thủ theo chiều sâu trước các nguy cơ giả mạo và nghe lén dữ liệu [5], [6].

SMBv1 (CIFS) được thiết kế từ những năm 1980, phục vụ các mạng cục bộ quy mô nhỏ [5]. Do cấu trúc thông điệp phức tạp với hơn một trăm lệnh và lệnh con khác nhau, việc xử lý dữ liệu đòi hỏi trình điều khiển `srv.sys` phải thực hiện nhiều phép tính toán và chuyển đổi cấu trúc phức tạp trong nhân [3], [5]. SMBv1 vận hành theo cơ chế tuần tự đơn lẻ (Chatty Protocol), mỗi thao tác tệp đều cần một cặp yêu cầu và phản hồi riêng biệt, dẫn đến suy giảm hiệu năng nghiêm trọng khi độ trễ mạng tăng cao [5]. Về mặt an ninh, SMBv1 không tích hợp mã hóa dữ liệu và cơ chế ký số phụ thuộc vào thuật toán băm MD5 vốn tồn tại điểm yếu va chạm mật mã [6], [7].

SMBv2 ra đời cùng Windows Vista và Windows Server 2008 nhằm giải quyết triệt để các hạn chế của phiên bản tiền nhiệm [5]. Số lượng lệnh trong SMBv2 được tinh giản xuống còn 19 lệnh, với tiêu đề gói tin cố định 64 byte giúp tăng tốc độ phân tích cú pháp của hệ điều hành [4], [5]. Đặc biệt, SMBv2 giới thiệu kỹ thuật gộp lệnh (Compounding), cho phép Client đóng gói nhiều thao tác liên quan (như mở tệp, đọc dữ liệu và đóng tệp) vào một thông điệp duy nhất, giảm thiểu đáng kể số lượng chuyến đi - về của gói tin trên mạng [4], [5]. Về mặt an ninh, SMBv2 loại bỏ thuật toán MD5 và thay thế bằng HMAC-SHA256 cho cơ chế ký số, nâng cao khả năng chống giả mạo gói tin [6], [7].

SMBv3, xuất hiện từ Windows 8 và Windows Server 2012, bổ sung các khả năng bảo mật chuyên sâu phục vụ môi trường ảo hóa và trung tâm dữ liệu [5], [6]:
- **Mã hóa dữ liệu đầu - cuối (SMB Encryption):** Tích hợp thuật toán mã hóa khối chuẩn công nghiệp AES-128-CCM trên SMB 3.0 và AES-128-GCM trên SMB 3.1.1 [6]. Tính năng này bảo vệ tính bí mật của dữ liệu truyền tải trên mạng mà không cần thiết lập các đường hầm VPN hoặc cấu hình IPsec phức tạp [6].
- **Cơ chế ký số tiên tiến (Advanced SMB Signing):** Chuyển đổi sang sử dụng thuật toán AES-CMAC trên SMB 3.0 và hỗ trợ thêm AES-128-GMAC trên các hệ điều hành hiện đại, đảm bảo tính toàn vẹn thông điệp với hiệu năng tính toán cao [6], [7].
- **Bảo vệ tính toàn vẹn tiền xác thực (Pre-authentication Integrity):** Được triển khai trên dialect SMB 3.1.1, cơ chế này sử dụng thuật toán băm SHA-512 để tính toán giá trị băm tích lũy trên toàn bộ các gói tin thương lượng và thiết lập phiên ban đầu [6], [8]. Giá trị băm này được đưa vào quá trình dẫn xuất khóa mã hóa của phiên, ngăn chặn hoàn toàn nguy cơ kẻ tấn công can thiệp vào giữa để ép buộc hai bên hạ cấp (Downgrade Attack) dialect từ SMB 3.1.1 xuống SMB 2.x [6], [8].

Tuy nhiên, tài liệu kỹ thuật của Microsoft lưu ý rằng cơ chế Pre-authentication Integrity chỉ bảo vệ việc hạ cấp giữa các dialect SMB 3.x và 2.x, không thể tự động bảo vệ một máy chủ nếu máy chủ đó vẫn duy trì tính năng SMBv1 [6], [8]. Do đó, việc vô hiệu hóa hoàn toàn SMBv1 trên toàn bộ các nút mạng vẫn là yêu cầu bảo mật bắt buộc đối với hạ tầng công nghệ thông tin [8].

*Bảng 1.1: So sánh đối chiếu kiến trúc và cơ chế an ninh giữa SMBv1, SMBv2 và SMBv3 [3], [4], [5], [6], [7], [8].*

| Đặc tính kỹ thuật | SMBv1 (CIFS) | SMBv2 (2.0.2 / 2.1) | SMBv3 (3.0 / 3.0.2 / 3.1.1) |
|---|---|---|---|
| **Hệ điều hành đại diện** | Windows 2000, XP, Windows 7 khi bật SMBv1 | Windows Vista, Windows Server 2008, Windows 7 | Windows 8, Windows 10, Windows 11, Windows Server 2012–2022 |
| **Cổng mạng hỗ trợ** | TCP 139 (NetBIOS) và TCP 445 (Direct-hosted) | TCP 445 | TCP 445 |
| **Cấu trúc lệnh** | Phức tạp, hơn 100 mã lệnh và lệnh phụ | Chuẩn hóa, tinh giản còn 19 mã lệnh | Chuẩn hóa 19 mã lệnh, tối ưu hóa cấu trúc |
| **Cơ chế xử lý yêu cầu** | Tuần tự đơn lẻ từng lệnh (Chatty) | Hỗ trợ gộp lệnh (Compounding) | Hỗ trợ gộp lệnh và đa kênh (Multichannel) |
| **Ký số toàn vẹn (Signing)** | Dựa trên hàm băm MD5 | Thuật toán HMAC-SHA256 | Thuật toán AES-CMAC (3.0) / AES-128-GMAC (3.1.1) |
| **Mã hóa kênh truyền** | Không hỗ trợ mã hóa tích hợp | Không hỗ trợ mã hóa tích hợp | Mã hóa AES-128-CCM (3.0) / AES-128-GCM (3.1.1) |
| **Toàn vẹn tiền xác thực** | Không hỗ trợ | Không hỗ trợ | Pre-authentication Integrity dựa trên SHA-512 (3.1.1) |
| **Trình điều khiển nhân** | `srv.sys` | `srv2.sys` | `srv2.sys` |

---

## 1.2. Bản chất kỹ thuật và cơ chế phát sinh lỗ hổng MS17-010

### 1.2.1. Tổng quan thông báo bảo mật MS17-010 và phân loại 6 mã CVE

Vào ngày 14 tháng 03 năm 2017, Microsoft chính thức phát hành thông báo bảo mật định kỳ mang mã hiệu **MS17-010** với mức độ đánh giá "Nghiêm trọng" (Critical) [9]. Cơ sở dữ liệu NIST NVD đồng thời ghi nhận các định danh chi tiết, tiêu biểu là CVE-2017-0144 [10]. Bản tin này công bố các bản vá nhằm khắc phục một nhóm gồm 6 lỗ hổng bảo mật nằm trong cách thức xử lý gói tin của trình điều khiển SMBv1 (`srv.sys`) trên hệ điều hành Windows [9].

Nhóm lỗ hổng này ảnh hưởng đến hầu hết các phiên bản Windows đang lưu hành tại thời điểm phát hành, bao gồm Windows Vista, Windows 7, Windows 8.1, Windows 10, cùng các hệ điều hành máy chủ từ Windows Server 2008 đến Windows Server 2016 [9]. Trước tính chất đặc biệt nguy hiểm của lỗ hổng, Microsoft sau đó đã đưa ra quyết định ngoại lệ khi phát hành bổ sung các bản vá khẩn cấp cho cả các hệ điều hành đã hết vòng đời hỗ trợ chính thức như Windows XP và Windows Server 2003 [9].

Bản tin MS17-010 xử lý 6 mã định danh lỗ hổng (CVE) khác nhau, trong đó có 5 lỗ hổng thực thi mã từ xa (RCE) và 1 lỗ hổng tiết lộ thông tin bộ nhớ nhân [9], [10]. Mỗi mã CVE đại diện cho một sai sót kỹ thuật cụ thể trong mã nguồn của `srv.sys`, tương ứng với các công cụ khai thác mạng do nhóm tin tặc Shadow Brokers làm rò rỉ [9], [10], [11], [12], [13].

*Bảng 1.2: Phân loại 6 mã CVE trong thông báo bảo mật Microsoft MS17-010 [9], [10], [11], [12], [13].*

| Mã CVE | Tên mã khai thác liên hệ | Phân loại kỹ thuật theo Microsoft | Tác động an ninh | Vai trò trong nghiên cứu |
|---|---|---|---|---|
| **CVE-2017-0143** | **EternalSynergy** [11] | SMBv1 Remote Code Execution Vulnerability | RCE (Thực thi mã từ xa) | Đối chứng kỹ thuật trong nhóm MS17-010 |
| **CVE-2017-0144** | **EternalBlue** [10], [13] | SMBv1 Remote Code Execution Vulnerability | RCE (Thực thi mã từ xa) | **Đối tượng nghiên cứu và thực nghiệm trọng tâm** |
| **CVE-2017-0145** | **EternalRomance** [12] | SMBv1 Remote Code Execution Vulnerability | RCE (Thực thi mã từ xa) | Đối chứng phân tích bề mặt tấn công |
| **CVE-2017-0146** | EternalChampion [9] | SMBv1 Remote Code Execution Vulnerability | RCE (Thực thi mã từ xa) | Thuộc nhóm lỗ hổng MS17-010 |
| **CVE-2017-0147** | Không định danh riêng [9] | SMBv1 Information Disclosure Vulnerability | Information Disclosure (Lộ bộ nhớ) | Lỗ hổng hỗ trợ thu thập địa chỉ nhân |
| **CVE-2017-0148** | Không định danh riêng [9] | SMBv1 Remote Code Execution Vulnerability | RCE (Thực thi mã từ xa) | Thuộc nhóm lỗ hổng MS17-010 |

Trong 6 mã CVE nêu trên, **CVE-2017-0144** được lựa chọn làm đối tượng nghiên cứu và thực nghiệm trọng tâm của đề tài [10]. Đây là lỗ hổng cốt lõi được mã khai thác EternalBlue sử dụng, cho phép thực thi mã tùy ý từ xa mà không đòi hỏi thông tin xác thực từ phía người dùng [10], [13].

### 1.2.2. Cơ chế lỗi nhân của CVE-2017-0144: Sai lệch chuyển đổi kiểu dữ liệu FEA trong srv.sys

Lỗ hổng CVE-2017-0144 bắt nguồn từ một sai sót toán học trong quá trình xử lý danh sách thuộc tính mở rộng của tệp tin (File Extended Attributes – FEA) trong trình điều khiển `srv.sys` [13]. Tính năng này vốn được thiết kế để duy trì khả năng tương thích ngược với hệ điều hành OS/2 cũ của IBM khi giao tiếp qua giao thức SMBv1 [13].

Khi Client gửi một yêu cầu giao dịch `SMB_COM_TRANSACTION2` chứa danh sách thuộc tính mở rộng, hệ điều hành Windows Server cần chuyển đổi danh sách này từ định dạng OS/2 FEA sang định dạng Windows NT FEA nội bộ trước khi ghi xuống hệ thống tệp tin [13]. Quá trình này được thực thi thông qua hai hàm kế tiếp nhau trong `srv.sys`:

1. Hàm tính toán kích thước bộ nhớ: `SrvOs2FeaListSizeToNt` có nhiệm vụ duyệt qua danh sách các thuộc tính OS/2 FEA do Client gửi lên để tính toán tổng dung lượng bộ nhớ cần cấp phát nhằm chứa cấu trúc NT FEA tương ứng [13].
2. Hàm chuyển đổi và sao chép dữ liệu: `SrvOs2FeaToNt` sau đó sẽ tiến hành chuyển đổi từng trường dữ liệu và sử dụng hàm sao chép bộ nhớ `memmove` để ghi dữ liệu vào vùng đệm đã được cấp phát [13].

Lỗi phát sinh do sự không nhất quán về kiểu dữ liệu giữa hai hàm này [13]. Trong hàm `SrvOs2FeaListSizeToNt`, giá trị kích thước được tính toán dưới dạng một biến kiểu DWORD (số nguyên không dấu 32-bit). Tuy nhiên, khi chuyển kết quả kích thước sang hàm cấp phát, giá trị này bị ép kiểu hoặc gán vào một biến kiểu WORD (số nguyên không dấu 16-bit) [13].

Hiện tượng cắt ngắn số nguyên (Integer Truncation) xảy ra khi kẻ tấn công chế tạo một danh sách FEA có tổng kích thước thực tế lớn hơn $65.535$ byte (giá trị tối đa của một số nguyên 16-bit). Khi đó, giá trị kích thước 32-bit bị mất đi các bit bậc cao, chỉ giữ lại phần dư 16-bit bậc thấp [13]. 

Để làm rõ cơ chế khái niệm này, gọi $L_{alloc}$ là kích thước bộ nhớ được hệ điều hành cấp phát và $L_{write}$ là kích thước dữ liệu thực tế được ghi bởi hàm `memmove`. Trong điều kiện vận hành hợp lệ, hệ thống luôn đảm bảo điều kiện $L_{write} \leq L_{alloc}$. Khi lỗi cắt ngắn số nguyên xảy ra, giá trị $L_{alloc}$ nhận về kích thước bị thu nhỏ nghiêm trọng, dẫn tới trạng thái bất đẳng thức:

$$L_{write} > L_{alloc}$$

Do hàm sao chép `SrvOs2FeaToNt` vẫn duyệt qua toàn bộ dữ liệu thực tế của danh sách FEA theo độ dài gốc, thao tác `memmove` sẽ sao chép dữ liệu vượt ra ngoài phạm vi biên của vùng đệm đã cấp phát, gây ra hiện tượng tràn bộ nhớ nhân (Kernel Pool Overflow) [13].

```text
Yêu cầu SMB_COM_TRANSACTION2 từ Client (chứa danh sách FEA kích thước lớn)
                           |
                           v
Hàm SrvOs2FeaListSizeToNt tính toán kích thước (DWORD 32-bit)
                           |
                           v
       Cắt ngắn số nguyên xuống WORD 16-bit (Tràn số)
                           |
                           v
Cấp phát bộ nhớ vùng đệm nhân với kích thước nhỏ (L_alloc)
                           |
                           v
Hàm SrvOs2FeaToNt thực hiện sao chép dữ liệu thực tế (L_write)
                           |
             [ Điểm va chạm: L_write > L_alloc ]
                           |
                           v
Ghi đè dữ liệu vượt biên vùng đệm Non-Paged Pool (Kernel Overflow)
```
*Sơ đồ 1.3: Dòng chảy logic và cơ chế phát sinh lỗi tràn bộ nhớ nhân trong trình điều khiển srv.sys.*

### 1.2.3. Cơ chế tràn bộ đệm Non-Paged Pool, kỹ thuật Pool Grooming và rủi ro sập hệ thống (BSOD)

Bộ nhớ nhân của Windows phân chia thành hai khu vực chính: Paged Pool và Non-Paged Pool. Paged Pool có thể hoán đổi ra đĩa cứng khi thiếu RAM, trong khi Non-Paged Pool luôn thường trực trong RAM vật lý để phục vụ các trình điều khiển thiết bị. Trình điều khiển `srv.sys` cấp phát các vùng đệm tiếp nhận dữ liệu mạng trên vùng Non-Paged Pool [13].

Một vụ tràn bộ nhớ trong Non-Paged Pool nếu xảy ra một cách ngẫu nhiên sẽ lập tức làm hỏng các tiêu đề quản lý bộ nhớ (Pool Chunk Headers) của các khối liền kề. Ngay khi hệ điều hành phát hiện sự sai lệch này, cơ chế tự bảo vệ nhân của Windows sẽ lập tức kích hoạt lỗi dừng hệ thống (BugCheck), dẫn tới hiện tượng sập nguồn và xuất hiện màn hình xanh chết chóc (Blue Screen of Death – BSOD) [13]. Các mã lỗi dừng phổ biến nhất khi tràn bộ nhớ nhân không kiểm soát gồm có `KERNEL_MODE_EXCEPTION_NOT_HANDLED` (`0x0000001E`), `PAGE_FAULT_IN_NONPAGED_AREA` (`0x00000050`) và `DRIVER_IRQL_NOT_LESS_OR_EQUAL` (`0x000000D1`) [13].

Để chuyển hóa một lỗi tràn bộ đệm có nguy cơ gây sập hệ thống thành khả năng thực thi mã lệnh có kiểm soát, mã khai thác EternalBlue sử dụng kỹ thuật dàn xếp bộ nhớ nhân (Kernel Pool Grooming) [13]. Kỹ thuật này đòi hỏi người kiểm thử phải gửi một chuỗi gói tin SMB được tính toán chính xác nhằm ép buộc trình quản lý bộ nhớ của Windows giải phóng và tái cấp phát các khối bộ đệm trong Non-Paged Pool theo một trật tự xác định [13]:

1. **Tạo lập lỗ hổng bộ nhớ (Hole Punching):** Mã khai thác liên tục cấp phát và giải phóng các khối bộ đệm có kích thước tương ứng, tạo ra các ô trống vừa vặn trong Non-Paged Pool [13].
2. **Xếp đặt cấu trúc mục tiêu:** Ngay phía sau ô trống được chuẩn bị cho khối đệm bị tràn của `srv.sys`, mã khai thác kích hoạt việc tạo lập cấu trúc bộ đệm kết nối của trình điều khiển mạng `srvnet.sys` [13].
3. **Kích hoạt lỗi tràn và ghi đè con trỏ:** Khi thao tác tràn bộ đệm tại `SrvOs2FeaToNt` diễn ra, dữ liệu tràn sẽ tràn qua biên và ghi đè chính xác lên cấu trúc `SRVNET_BUFFER` liền kề, thay đổi con trỏ hàm xử lý kết nối tại `srvnet!SrvNetWskReceiveComplete` trỏ tới địa chỉ chứa mã nhị phân thực thi (Shellcode) do người gửi đưa vào trước đó [13].
4. **Chiếm quyền thực thi mức nhân:** Khi một gói tin mạng tiếp theo được gửi tới trạm mạng, trình điều khiển `srvnet.sys` kích hoạt hàm ủy thác tại con trỏ vừa bị ghi đè, khiến CPU chuyển hướng thực thi Shellcode trực tiếp trong không gian nhân (Ring 0) [13].

Sau khi Shellcode thực thi thành công trong không gian nhân, nó tiến hành thao tác sao chép mã thông báo bảo mật (Token Stealing) từ tiến trình hệ thống `System` sang tiến trình đích, mang lại phiên tương tác có quyền hạn tối cao `NT AUTHORITY\SYSTEM` [13].

Tuy nhiên, do Non-Paged Pool là môi trường động chịu ảnh hưởng liên tục từ các hoạt động mạng của toàn bộ hệ điều hành, kỹ thuật Pool Grooming mang tính chất phi tất định. Bất kỳ một gói tin mạng ngẫu nhiên nào chen ngang vào quá trình sắp đặt bộ nhớ đều có thể làm sai lệch vị trí các khối đệm, biến nỗ lực khai thác thành một sự cố BSOD làm gián đoạn hoàn toàn dịch vụ của máy chủ mục tiêu [13]. Đây là căn cứ kỹ thuật bắt buộc để đề tài đưa ra yêu cầu cô lập mạng và thiết lập cơ chế sao lưu snapshot trong kịch bản kiểm thử [13].

### 1.2.4. Điều kiện khai thác và mức độ ảnh hưởng tới bộ ba an toàn thông tin (CIA)

Để một hệ thống máy tính Windows thực sự có nguy cơ bị khai thác bởi lỗ hổng CVE-2017-0144, hệ thống đó bắt buộc phải thỏa mãn đồng thời toàn bộ 5 điều kiện kỹ thuật sau [9], [10], [13]:

1. **Hệ điều hành thuộc danh mục ảnh hưởng:** Máy tính cài đặt phiên bản Windows nằm trong danh sách công bố của Microsoft (Windows Vista đến Windows 10 các bản dựng đầu; Windows Server 2008 đến Windows Server 2016) [9]. Trong phạm vi thực nghiệm của đề tài, Windows 7 SP1 x64 được lựa chọn làm máy chủ mục tiêu do tính phổ biến lịch sử và được hỗ trợ đầy đủ bởi các công cụ kiểm thử [13].
2. **Dịch vụ SMBv1 đang hoạt động:** Tính năng SMBv1 chưa bị vô hiệu hóa trong hệ điều hành và trình điều khiển `srv.sys` đang được nạp để tiếp nhận các yêu cầu giao dịch mạng [8], [14].
3. **Cổng dịch vụ có thể tiếp cận qua mạng:** Cổng TCP 445 (hoặc TCP 139) ở trạng thái mở và đường truyền mạng không bị lọc hoặc ngăn chặn bởi tường lửa cục bộ hay thiết bị an ninh biên [2], [15].
4. **Hệ điều hành chưa được cài đặt bản vá:** Máy tính chưa cập nhật gói cập nhật an ninh MS17-010 phù hợp tương ứng với phiên bản Windows đang vận hành [9].
5. **Đặc quyền truy cập không ràng buộc:** Lỗ hổng cho phép khai thác từ xa hoàn toàn không đòi hỏi tài khoản xác thực hợp lệ trên hệ thống mục tiêu, biến mọi máy tính mở cổng trở thành đối tượng tiềm năng [9], [10].

Xét theo tam giác an toàn thông tin (Confidentiality – Integrity – Availability / CIA), tác động của CVE-2017-0144 đạt mức độ nghiêm trọng tối đa trên cơ sở dữ liệu NVD (điểm CVSS v3.0 là 9.8 / Critical) [10]:
- **Tính bí mật (Confidentiality):** Bị xâm phạm toàn diện. Do kẻ tấn công đạt được quyền điều khiển mức `SYSTEM`, toàn bộ tệp tin dữ liệu lưu trữ, cơ sở dữ liệu xác thực SAM (Security Account Manager) và các bí mật mật mã trong bộ nhớ RAM đều có thể bị đọc và trích xuất trái phép [10].
- **Tính toàn vẹn (Integrity):** Bị phá vỡ triệt để. Quyền thực thi mức nhân cho phép kẻ tấn công chỉnh sửa tùy ý các tệp tin hệ thống, thay đổi cấu hình bảo mật, chèn cửa sau (Backdoor như DoublePulsar) hoặc mã hóa toàn bộ dữ liệu máy chủ [10].
- **Tính sẵn sàng (Availability):** Bị triệt tiêu nghiêm trọng. Nguy cơ phát sinh lỗi BSOD trong quá trình khai thác hoặc việc hệ thống bị phá hủy bản ghi khởi động (MBR) khiến máy chủ ngừng hoạt động hoàn toàn, làm gián đoạn mọi dịch vụ nghiệp vụ phụ thuộc [10], [13].

### 1.2.5. Danh mục bản vá KB chính thức và bài học từ các chiến dịch mã độc toàn cầu

Để loại bỏ hoàn toàn các lỗi quản lý bộ nhớ thuộc nhóm MS17-010, Microsoft đã phát hành các gói cập nhật nhị phân cho từng dòng hệ điều hành [9]. Bảng 1.3 liệt kê danh mục mã định danh bản cập nhật kiến thức (Knowledge Base – KB) chính thức cần được kiểm tra đối chiếu khi thẩm định trạng thái an ninh của máy chủ mục tiêu.

*Bảng 1.3: Danh mục mã bản vá KB chính thức của Microsoft theo hệ điều hành Windows [9].*

| Hệ điều hành | Phiên bản / Kiến trúc | Bản cập nhật chỉ bảo mật (Security Only) | Bản cập nhật tích lũy tháng (Monthly Rollup / Cumulative) | Ý nghĩa đối với môi trường lab |
|---|---|---|---|---|
| **Windows 7 SP1** | x86 và x64 | **KB4012212** | **KB4012215** | Đối tượng kiểm nghiệm chính trước và sau vá |
| **Windows Server 2008 R2 SP1** | x64 | **KB4012212** | **KB4012215** | Mã bản vá tương đồng với Windows 7 SP1 |
| **Windows 8.1** | x86 và x64 | **KB4012213** | **KB4012216** | Mục tiêu so sánh trên hệ điều hành thế hệ kế tiếp |
| **Windows Server 2012 R2** | x64 | **KB4012213** | **KB4012216** | Phiên bản máy chủ tương ứng Windows 8.1 |
| **Windows Server 2012** | x64 | **KB4012214** | **KB4012217** | Phiên bản máy chủ thế hệ Windows 8 |
| **Windows 10** | RTM (1507)<br>Bản dựng 1511<br>Bản dựng 1607 | Không áp dụng (chỉ có bản tích lũy) | **KB4012606** (1507)<br>**KB4013198** (1511)<br>**KB4013429** (1607) | Windows 10 áp dụng mô hình cập nhật tích lũy |
| **Windows Server 2016** | Bản dựng 1607 | Không áp dụng | **KB4013429** | Tương đồng bản vá với Windows 10 Version 1607 |
| **Windows XP SP3** | x86 | **KB4012598** | Không áp dụng | Bản vá khẩn cấp phát hành ngoài vòng đời hỗ trợ |
| **Windows Server 2003 SP2** | x86 và x64 | **KB4012598** | Không áp dụng | Bản vá khẩn cấp phát hành ngoài vòng đời hỗ trợ |

Thực tế lịch sử an ninh mạng ghi nhận hai chiến dịch tấn công quy mô toàn cầu khai thác trực tiếp lỗ hổng MS17-010 [12], [15]:
- **Chiến dịch mã độc tống tiền WannaCry (tháng 05/2017):** Kết hợp mã khai thác EternalBlue với cơ chế sâu máy tính (Worm), tự động quét dải mạng Internet và mạng nội bộ để lây nhiễm vào các máy trạm Windows chưa vá [15]. Khi xâm nhập thành công, mã độc mã hóa toàn bộ dữ liệu tệp tin và đòi tiền chuộc bằng tiền mã hóa, gây tê liệt hàng loạt cơ sở y tế, ngân hàng và cơ quan viễn thông trên thế giới [15].
- **Chiến dịch mã độc phá hoại NotPetya (tháng 06/2017):** Tận dụng mã khai thác EternalBlue và EternalRomance thuộc nhóm MS17-010 để lây lan ngang (Lateral Movement) trong mạng doanh nghiệp [12]. Khác với WannaCry, NotPetya ghi đè trực tiếp bảng phân vùng và bản ghi khởi động chính (MBR) của ổ cứng mà không có cơ chế khôi phục, nhằm mục đích phá hoại hạ tầng công nghệ thông tin diện rộng [12].

Hai chiến dịch trên là minh chứng thực tế khẳng định việc phân tích cơ chế, xây dựng quy trình phát hiện sớm và áp dụng các biện pháp phòng thủ cho dịch vụ SMB là yêu cầu cấp thiết đối với công tác bảo vệ an ninh mạng [12], [15].

---

## 1.3. Phương pháp luận và bộ công cụ kiểm thử an ninh SMB trong môi trường Lab

### 1.3.1. Nguyên tắc kiểm thử an ninh có kiểm soát theo chuẩn NIST SP 800-115 và vai trò của trạm Kali Linux

Kiểm thử an ninh mạng là một quá trình kỹ thuật đòi hỏi phương pháp luận chuẩn xác nhằm thu thập bằng chứng thực tế mà không gây ảnh hưởng tiêu cực tới hệ thống mục tiêu [16]. Đề tài áp dụng các nguyên tắc kỹ thuật từ hướng dẫn đánh giá và kiểm thử an toàn thông tin NIST SP 800-115 do Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ ban hành [16].

Theo NIST SP 800-115, quy trình kiểm thử kỹ thuật bao gồm bốn pha tuần tự: Lập kế hoạch (Planning), Thu thập thông tin và phát hiện (Discovery), Thẩm định tấn công (Attack/Verification) và Báo cáo khắc phục (Reporting) [16]. Trong môi trường phòng thí nghiệm, mọi hành động kiểm thử đều phải tuân thủ nghiêm ngặt ranh giới an toàn [16]. Các thao tác chỉ thực thi trên máy ảo cô lập có phân đoạn mạng. Đồng thời, việc lưu lại ảnh chụp nhanh trạng thái (snapshot) là bắt buộc trước khi tiến hành các thao tác có nguy cơ gây hỏng bộ nhớ [16].

Nhằm chuẩn hóa môi trường thực thi, đề tài sử dụng hệ điều hành **Kali Linux** làm trạm kiểm thử trung tâm [17]. Kali Linux là bản phân phối mã nguồn mở dựa trên Debian, tích hợp sẵn hệ thống công cụ kiểm thử xâm nhập và thẩm định an ninh tiêu chuẩn [17]. Việc sử dụng một trạm kiểm thử đồng nhất giúp đảm bảo tính lặp lại (Reproducibility) của các phép đo kiểm, tránh sự sai lệch do các thư viện mạng không đồng bộ giữa các môi trường [17].

### 1.3.2. Kỹ thuật trinh sát cổng và nhận diện dịch vụ mạng bằng Nmap

Nmap (Network Mapper) là công cụ nền tảng được triển khai ở pha đầu tiên nhằm thu thập thông tin về khả năng tiếp cận dịch vụ mạng của mục tiêu [18]. Đề tài áp dụng kỹ thuật quét **TCP SYN Scan** (tham số `-sS`) do tính chất nhanh chóng và khả năng hạn chế tối đa việc tạo lập phiên kết nối đầy đủ [18].

Cơ chế vận hành của TCP SYN Scan dựa trên quy trình bắt tay ba bước của tầng truyền tải [18]:
- Trạm quét Kali gửi một gói tin mang cờ TCP SYN tới cổng đích (TCP 445 hoặc TCP 139) [18].
- Nếu cổng ở trạng thái mở (`open`), máy chủ mục tiêu sẽ phản hồi bằng một gói tin TCP mang cờ SYN-ACK [18]. Trạm quét ngay lập tức gửi lại một gói tin TCP mang cờ RST để giải phóng kết nối, ghi nhận trạng thái cổng là `open` [18].
- Nếu cổng ở trạng thái đóng (`closed`), máy chủ mục tiêu sẽ lập tức phản hồi bằng một gói tin TCP mang cờ RST [18].
- Nếu gói tin SYN không nhận được phản hồi sau số lần thử lại, hoặc trạm quét nhận về thông điệp báo lỗi ICMP, Nmap sẽ phân loại trạng thái cổng là bị lọc (`filtered`) [18]. Kết quả này biểu thị rằng có thiết bị tường lửa hoặc chính sách kiểm soát đang ngăn chặn đường truyền [18].

Sau khi xác định cổng mở, Nmap triển khai kỹ thuật nhận diện dịch vụ (**Version Detection**, tham số `-sV`) [18]. Khác với việc chỉ đọc số hiệu cổng mặc định, tùy chọn `-sV` gửi các gói tin thăm dò ở tầng ứng dụng [18]. Phản hồi nhận về được đối chiếu với cơ sở dữ liệu mẫu dấu hiệu để xác định chính xác tên phần mềm máy chủ và phiên bản dịch vụ (ví dụ: `microsoft-ds`) [18]. Cần nhấn mạnh rằng việc Nmap hiển thị `microsoft-ds` chỉ chứng minh dịch vụ SMB đang lắng nghe, hoàn toàn chưa khẳng định máy chủ có tồn tại lỗ hổng MS17-010 hay không [18].

### 1.3.3. Cơ chế thăm dò phát hiện dấu hiệu MS17-010 qua Nmap Scripting Engine (NSE)

Nmap Scripting Engine (NSE) mở rộng khả năng của Nmap thông qua việc thực thi các kịch bản viết bằng ngôn ngữ Lua [18]. Trong công tác đánh giá an ninh giao thức SMB và lỗ hổng MS17-010, đề tài sử dụng hai tập lệnh NSE trọng tâm [19], [20]:

1. **Kịch bản nhận diện phương ngữ `smb-protocols.nse`:** Kịch bản này khởi tạo kết nối SMB và gửi một gói tin `Negotiate Protocol Request` chứa danh sách đầy đủ các dialect [19]. Phản hồi từ máy chủ cho biết dialect cao nhất được chấp thuận. Nếu dialect `"NT LM 0.12"` xuất hiện trong kết quả, điều đó chứng minh tính năng SMBv1 đang được kích hoạt trên hệ thống [19].
2. **Kịch bản kiểm tra an toàn `smb-vuln-ms17-010.nse`:** Đây là kịch bản thuộc nhóm `safe` và `vuln`, được thiết kế để nhận diện dấu hiệu chưa vá lỗ hổng MS17-010 mà không kích hoạt việc tràn bộ nhớ hay gây nguy cơ sập hệ thống [20].

Cơ chế logic bóc tách từ mã nguồn của `smb-vuln-ms17-010.nse` được vận hành qua ba bước tuần tự [20]:
- **Bước 1 (Thiết lập phiên và kết nối IPC$):** Kịch bản sử dụng thư viện SMB nội tại để kết nối tới cổng 445, thương lượng SMBv1 và thực hiện Session Setup [20]. Sau đó, kịch bản gửi yêu cầu `Tree Connect` tới tài nguyên chia sẻ `\\Target\IPC$` để nhận về một `TID` hợp lệ [20].
- **Bước 2 (Gửi gói tin thăm dò giao dịch đặc biệt):** Sau khi liên kết thành công với `IPC$`, kịch bản gửi một yêu cầu giao dịch `SMB_COM_TRANSACTION` (opcode `0x25`) chứa lệnh con `PeekNamedPipe` (mã hàm `0x2300`) trên đường ống định danh `\PIPE\` [20]. Trong yêu cầu này, kịch bản cố tình thiết lập hai trường tham số độ dài bộ đệm đạt giá trị tối đa: `Max Parameter Count = 0xFFFF` và `Max Data Count = 0xFFFF` [20].
- **Bước 3 (Phân tích mã trạng thái lỗi NT Status phản hồi từ Kernel):**
  - *Dấu hiệu hệ thống chưa vá (VULNERABLE):* Trên các hệ điều hành chưa cài đặt bản vá MS17-010, trình điều khiển `srv.sys` khi tiếp nhận tham số độ dài $0xFFFF$ vượt quá khả năng xử lý sẽ rơi vào một nhánh lỗi logic nội bộ và trả về mã lỗi NT Status đặc trưng là `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`) [20]. Nhận diện chính xác mã lỗi này, kịch bản kết luận hệ thống có dấu hiệu phù hợp với trạng thái chưa vá và thông báo `State: VULNERABLE` [20].
  - *Dấu hiệu hệ thống đã vá an toàn:* Trên các hệ điều hành đã được cài đặt bản vá MS17-010, Microsoft đã bổ sung đoạn mã kiểm tra tính hợp lệ của tham số ngay tại hàm điều phối giao dịch. Do đó, yêu cầu bất thường bị từ chối sớm và máy chủ phản hồi mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc `STATUS_INVALID_HANDLE` (`0xC0000008`) [20]. Kịch bản ghi nhận dấu hiệu an toàn này và xuất thông báo hệ thống đã được vá [20].

Ranh giới kỹ thuật quan trọng của phép thăm dò này nằm ở bước xác thực. Nếu việc kết nối tới tài nguyên `IPC$` bị từ chối do máy chủ chặn phiên nặc danh, kịch bản sẽ không thể gửi gói tin `PeekNamedPipe` [20]. Khi đó, kết quả trả về là không thể xác định, không đồng nghĩa với việc hệ thống đã an toàn [20].

### 1.3.4. Thẩm định xâm nhập có kiểm soát với nền tảng Metasploit Framework

Metasploit Framework là nền tảng kiểm thử xâm nhập mã nguồn mở cung cấp môi trường tích hợp cho việc phát triển, kiểm tra và thực thi các mô-đun an ninh [21]. Trong phạm vi đề tài, Metasploit được ứng dụng theo hai cấp độ độc lập nhằm phục vụ công tác đối chứng chéo và thẩm định thực nghiệm [13], [22]:

- **Mô-đun phụ trợ (Auxiliary Scanner):** Sử dụng mô-đun `auxiliary/scanner/smb/smb_ms17_010` [22]. Tương tự như kịch bản NSE, mô-đun này khởi tạo kết nối SMB tới tài nguyên `IPC$` và phát gói tin thăm dò `PeekNamedPipe` để kiểm tra phản hồi mã lỗi `0xC0000205` [22]. Việc sử dụng mô-đun này cho phép đối chiếu chéo kết quả nhận diện giữa hai bộ công cụ khác nhau nhằm loại bỏ sai số phần mềm [22].
- **Mô-đun khai thác có kiểm soát (Exploit Module):** Sử dụng mô-đun `exploit/windows/smb/ms17_010_eternalblue` [13]. Đây là công cụ hiện thực hóa kỹ thuật Kernel Pool Grooming và kích hoạt lỗi tràn FEA trong `srv.sys` nhằm thẩm định khả năng thực thi mã lệnh thực tế trên máy chủ Windows 7 trong môi trường lab cô lập [13].

Quy trình vận hành công cụ được tổ chức thành 4 giai đoạn logic chặt chẽ, từ khảo sát bề mặt tới thẩm định thực nghiệm theo Sơ đồ 1.4.

```text
+-----------------------------------------------------------+
| Giai đoạn 1: Quét trinh sát cổng mạng                     |
| Công cụ: Nmap (-sS -p 139,445)                            |
| Kết quả: Xác định trạng thái cổng TCP 445 / 139 (open)     |
+-----------------------------------------------------------+
                              |
                              v
+-----------------------------------------------------------+
| Giai đoạn 2: Định danh phiên bản dịch vụ và Dialect       |
| Công cụ: Nmap (-sV, --script smb-protocols)               |
| Kết quả: Nhận diện microsoft-ds và dialect NT LM 0.12     |
+-----------------------------------------------------------+
                              |
                              v
+-----------------------------------------------------------+
| Giai đoạn 3: Thăm dò dấu hiệu phản hồi logic nhân         |
| Công cụ: Nmap (--script smb-vuln-ms17-010) / MSF Scanner  |
| Kết quả: Ghi nhận mã phản hồi NT Status 0xC0000205        |
+-----------------------------------------------------------+
                              |
                              v
+-----------------------------------------------------------+
| Giai đoạn 4: Thẩm định xâm nhập có kiểm soát              |
| Công cụ: Metasploit (ms17_010_eternalblue trong lab cô lập)|
| Kết quả: Xác minh khả năng thực thi mã mức SYSTEM         |
+-----------------------------------------------------------+
```
*Sơ đồ 1.4: Quy trình 4 giai đoạn phối hợp công cụ kiểm thử an ninh giao thức SMB.*

### 1.3.5. Bảng liên kết kiến thức lý thuyết và các bước thực nghiệm lab

Để xây dựng mối liên kết xuyên suốt giữa các khái niệm lý thuyết và thao tác thực nghiệm, Bảng 1.4 hệ thống hóa từng nội dung cơ sở với mục tiêu quan sát và công cụ kiểm thử tương ứng được thiết kế cho môi trường phòng thí nghiệm.

*Bảng 1.4: Ma trận ánh xạ giữa cơ sở lý thuyết, mục tiêu quan sát và công cụ kiểm thử lab.*

| Khái niệm lý thuyết | Vấn đề an ninh cần làm rõ | Mục tiêu quan sát trong lab | Công cụ và cú pháp thực thi |
|---|---|---|---|
| **Cổng mạng TCP 445 / 139** | Cổng dịch vụ SMB có phơi nhiễm ra ngoài mạng hay không | Trạng thái cổng `open`, `closed` hoặc `filtered` | Nmap: `nmap -sS -p 139,445 <Target_IP>` |
| **Phương ngữ SMB Dialect** | Máy chủ có chấp nhận giao tiếp qua giao thức legacy SMBv1 không | Sự hiện diện của dialect `"NT LM 0.12"` | Nmap: `nmap -p 445 --script smb-protocols <Target_IP>` |
| **Dấu hiệu lỗi nhân srv.sys** | Trình điều khiển có phản hồi mã lỗi đặc trưng của bản chưa vá không | Phản hồi mã lỗi `STATUS_INSUFF_SERVER_RESOURCES` | Nmap: `nmap -p 445 --script smb-vuln-ms17-010 <Target_IP>` |
| **Đối chứng chéo công cụ** | Đảm bảo tính nhất quán của dấu hiệu nhận diện trên nhiều công cụ | Kết quả phát hiện tương đồng giữa NSE và Metasploit | MSF: `use auxiliary/scanner/smb/smb_ms17_010` |
| **Trạng thái bản vá Windows** | Xác nhận gói cập nhật an ninh MS17-010 đã được tích hợp chưa | Sự xuất hiện của gói cập nhật `KB4012212` hoặc `KB4012215` | Windows Target: `Get-HotFix -Id KB4012212, KB4012215` |
| **Khả năng khai thác thực tế** | Lỗ hổng có thể bị lợi dụng để đạt quyền thực thi nhân hay không | Phiên tương tác đặc quyền `NT AUTHORITY\SYSTEM` | MSF: `use exploit/windows/smb/ms17_010_eternalblue` |
| **Xác minh sau phòng thủ** | Biện pháp bảo vệ có loại bỏ hoàn toàn bề mặt tấn công không | Sự thay đổi trạng thái cổng, từ chối SMBv1 hoặc mã lỗi đã vá | Chạy lại toàn bộ bộ công cụ kiểm thử (Retest) |

---

## 1.4. Khung nhận thức luận thẩm định 4 cấp độ và chiến lược phòng thủ đa tầng

### 1.4.1. Khung thang đo 4 cấp độ thẩm định trạng thái SMB và lỗ hổng MS17-010

Một trong những hạn chế phổ biến trong công tác đánh giá an toàn thông tin là việc suy diễn vội vã từ trạng thái mở cổng mạng sang kết luận hệ thống có lỗ hổng nguy hiểm. Để đảm bảo tính khoa học và độ tin cậy của kết quả đánh giá, đề tài xây dựng một thang đo nhận thức luận gồm 4 cấp độ thẩm định kỹ thuật tăng dần theo Bảng 1.5.

*Bảng 1.5: Khung thang đo 4 cấp độ thẩm định an ninh dịch vụ và trạng thái lỗ hổng SMB.*

| Cấp độ | Định danh cấp độ | Dấu hiệu quan sát kỹ thuật | Ý nghĩa an ninh hệ thống | Ranh giới và giới hạn kết luận |
|---|---|---|---|---|
| **Cấp độ 1** | **Khả năng tiếp cận cổng dịch vụ (Port Reachability)** | Cổng TCP 445 hoặc TCP 139 phản hồi gói tin `SYN-ACK` trong phép quét TCP SYN | Có một dịch vụ đang mở cổng lắng nghe kết nối từ mạng | **Chưa thể kết luận về lỗ hổng.** Cổng mở là trạng thái bình thường của dịch vụ chia sẻ tệp tin, chưa chứng minh cấu hình bên trong |
| **Cấp độ 2** | **Chấp thuận phương ngữ SMBv1 (Dialect Exposure)** | Máy chủ phản hồi chấp thuận dialect `"NT LM 0.12"` trong quá trình Negotiate | Tính năng SMBv1 đang hoạt động; bề mặt tấn công của giao thức legacy bị phơi nhiễm | **Chưa đủ cơ sở khẳng định tồn tại lỗ hổng.** Máy tính có thể đã được cài đặt bản vá an ninh nhưng quản trị viên chưa tắt tính năng SMBv1 |
| **Cấp độ 3** | **Dấu hiệu phản hồi logic nhân (Response Signature)** | Máy chủ phản hồi mã lỗi `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`) trước yêu cầu thăm dò `PeekNamedPipe` vào `IPC$` | Logic xử lý trong trình điều khiển `srv.sys` trùng khớp với mẫu hành vi của hệ điều hành chưa được vá | **Chưa chứng minh khai thác thành công.** Dấu hiệu phản hồi chỉ ra sự tồn tại của nhánh mã lỗi; nếu truy cập nặc danh bị chặn thì không đo được |
| **Cấp độ 4** | **Thẩm định xâm nhập có kiểm soát (Exploitability)** | Kích hoạt thành công phiên thực thi mã với quyền hạn `NT AUTHORITY\SYSTEM` trong môi trường lab cô lập | Cấu hình máy chủ tồn tại lỗ hổng CVE-2017-0144 và có thể bị khai thác điều khiển từ xa | **Chỉ thực hiện trong mạng lab cô lập.** Phép thử đòi hỏi các điều kiện bộ nhớ ngặt nghèo và luôn đi kèm rủi ro gây sập hệ thống (BSOD) |

### 1.4.2. Phân tích giới hạn kỹ thuật và phương pháp loại trừ dương tính giả / âm tính giả

Mối quan hệ logic giữa 4 cấp độ trong khung thẩm định là quan hệ điều kiện cần (Necessary Condition), hoàn toàn không phải quan hệ điều kiện đủ (Sufficient Condition):

$$\text{Cấp độ 1} \nLeftarrow \text{Cấp độ 2} \nLeftarrow \text{Cấp độ 3} \nLeftarrow \text{Cấp độ 4}$$

- Cấp độ 1 là điều kiện cần để thực hiện Cấp độ 2. Nếu cổng 445 bị đóng hoặc bị tường lửa chặn (`filtered`), trạm kiểm thử không thể gửi gói tin thương lượng dialect.
- Cấp độ 2 là điều kiện cần để xảy ra Cấp độ 3. Nếu máy chủ đã tắt hoàn toàn SMBv1, yêu cầu thương lượng dialect `"NT LM 0.12"` sẽ bị từ chối ngay lập tức, triệt tiêu khả năng kích hoạt các hàm xử lý trong `srv.sys`.
- Cấp độ 3 là chỉ báo kỹ thuật có độ tin cậy cao cho thấy sự hiện diện của mã nguồn chưa vá, nhưng chỉ có Cấp độ 4 mới chứng minh được khả năng biến lỗi bộ nhớ thành quyền thực thi mã lệnh thực tế.

Trong thực tế kiểm thử, hai loại sai lệch sau đây cần được nhận diện và xử lý triệt để:
1. **Sai lệch dương tính giả (False Positive):** Xảy ra khi người kiểm thử chỉ dựa vào việc cổng 445 mở (Cấp độ 1) hoặc việc máy chủ hỗ trợ SMBv1 (Cấp độ 2) để vội vã đưa ra cảnh báo hệ thống bị nhiễm MS17-010. Một máy chủ Windows được quản trị tốt vẫn có thể mở cổng 445 để phục vụ chia sẻ dữ liệu và bật SMBv1 để tương thích máy in, nhưng đã được cài đặt đầy đủ gói vá `KB4012215`. Khi đó, trình điều khiển `srv.sys` đã được sửa đổi và hoàn toàn miễn nhiễm trước lỗi tràn FEA [9], [14].
2. **Sai lệch âm tính giả (False Negative):** Xảy ra khi công cụ quét (như kịch bản NSE) ghi nhận kết quả không phát hiện lỗ hổng do máy chủ cấu hình chặn hoàn toàn việc kết nối nặc danh tới tài nguyên `IPC$` [20]. Khi đó, công cụ không thể gửi được gói tin thăm dò `PeekNamedPipe` và xuất thông báo mặc định. Người kiểm thử thiếu kinh nghiệm có thể nhầm lẫn kết quả này với việc máy chủ đã an toàn, trong khi lỗ hổng vẫn tồn tại nguyên vẹn trong nhân và có thể bị khai thác bởi bất kỳ người dùng nào có tài khoản hợp lệ trong mạng nội bộ [20].

Để triệt tiêu các sai lệch trên, đề tài áp dụng nguyên tắc kiểm chứng chéo (Cross-verification). Phương pháp này kết hợp quan sát mạng từ xa với việc kiểm tra đối chiếu trực tiếp cấu hình nội tại thông qua danh mục bản vá và trạng thái dịch vụ trên máy chủ mục tiêu [9], [14].

### 1.4.3. Chiến lược phòng thủ chiều sâu (Defense-in-Depth) và bài toán cân bằng tương thích nghiệp vụ

Dựa trên phân tích bản chất kỹ thuật của giao thức SMB và cơ chế lỗi MS17-010, đề tài đề xuất mô hình phòng thủ chiều sâu gồm ba tầng bảo vệ độc lập nhưng hỗ trợ lẫn nhau [8], [9], [15], [23]:

```text
+-----------------------------------------------------------+
| Tầng 1: Cập nhật bản vá nhị phân (Binary Patching)        |
| - Cài đặt gói cập nhật KB tương ứng (KB4012212 / KB4012215)|
| - Vá trực tiếp mã nguồn srv.sys trong nhân hệ điều hành   |
+-----------------------------------------------------------+
                              |
                              v
+-----------------------------------------------------------+
| Tầng 2: Triệt tiêu bề mặt tấn công (Surface Reduction)    |
| - Vô hiệu hóa hoàn toàn giao thức legacy SMBv1             |
| - Tháo gỡ trình điều khiển srv.sys ra khỏi bộ nhớ nhân   |
+-----------------------------------------------------------+
                              |
                              v
+-----------------------------------------------------------+
| Tầng 3: Kiểm soát phân đoạn và tường lửa (Containment)    |
| - Chặn cổng TCP 139 và 445 tại tường lửa biên mạng       |
| - Phân đoạn mạng nội bộ, giới hạn quyền truy cập dịch vụ  |
+-----------------------------------------------------------+
```
*Sơ đồ 1.5: Mô hình chiến lược phòng thủ chiều sâu ba tầng đối với giao thức SMB.*

1. **Tầng 1 – Cập nhật bản vá nhị phân (Binary Patching):** Đây là biện pháp kỹ thuật căn bản nhất. Việc cài đặt gói cập nhật an ninh chính thức từ Microsoft (như `KB4012215` trên Windows 7) sẽ thay thế trình điều khiển `srv.sys` cũ bằng phiên bản đã được sửa đổi, bổ sung các phép kiểm tra kích thước tham số hợp lệ, loại bỏ hoàn toàn khả năng tràn bộ đệm tại hàm `SrvOs2FeaToNt` [9].
2. **Tầng 2 – Triệt tiêu bề mặt tấn công giao thức (Attack Surface Reduction):** Mặc dù bản vá giải quyết được lỗ hổng đã biết, bản thân giao thức SMBv1 vẫn tồn tại các rủi ro cấu trúc cố hữu do thiếu vắng các cơ chế mật mã hiện đại [5], [8]. Do đó, giải pháp triệt để và bền vững nhất là vô hiệu hóa hoàn toàn giao thức SMBv1 trên toàn bộ hệ thống máy trạm và máy chủ thông qua PowerShell, Registry hoặc chính sách nhóm (Group Policy Object – GPO) [8], [14]. Khi SMBv1 bị tắt, trình điều khiển `srv.sys` sẽ không được nạp vào bộ nhớ, triệt tiêu vĩnh viễn bề mặt tấn công liên quan đến phiên bản này [8], [14].
3. **Tầng 3 – Kiểm soát phân đoạn mạng và tường lửa (Perimeter Filtering & Network Segmentation):** Theo khuyến nghị an ninh mạng của NIST SP 800-41 Rev. 1, các cổng dịch vụ chia sẻ tệp tin nội bộ như TCP 139 và TCP 445 tuyệt đối không được phép phơi nhiễm trực tiếp ra mạng Internet hoặc các vùng mạng không tin cậy [23]. Tường lửa biên phải thiết lập chính sách chặn triệt để lưu lượng SMB ở cả hai chiều vào và ra [23]. Đồng thời, trong mạng nội bộ doanh nghiệp, cần triển khai các chính sách phân đoạn mạng (VLAN segmentation) và kiểm soát truy cập nhằm ngăn chặn nguy cơ lây lan ngang của mã độc khi một máy trạm bị xâm nhập [15], [23].

**Bài toán cân bằng giữa an ninh và tương thích nghiệp vụ:**
Trong thực tế quản trị mạng doanh nghiệp, rào cản lớn nhất khi vô hiệu hóa SMBv1 là tính tương thích thiết bị [8], [14]. Nhiều máy in mạng, máy quét scan-to-SMB hoặc thiết bị lưu trữ NAS thế hệ cũ chỉ hỗ trợ giao thức CIFS/SMBv1 [8], [14]. Nếu quản trị viên tắt bỏ SMBv1 đột ngột mà không khảo sát, các hoạt động in ấn và lưu trữ nghiệp vụ sẽ bị đình trệ [8], [14].

Để giải quyết bài toán xung đột này, giải pháp khả thi là triển khai phân đoạn mạng cách ly chuyên biệt [14], [23]. Các thiết bị bắt buộc phải dùng SMBv1 được gom vào một phân vùng mạng riêng có tường lửa kiểm soát nghiêm ngặt. Phân vùng này chỉ được phép giao tiếp với một máy chủ chia sẻ tệp tin trung gian được chỉ định, không kết nối trực tiếp tới phân vùng máy trạm người dùng [14], [23]. Đối với toàn bộ hạ tầng máy tính hiện đại còn lại, hệ thống bắt buộc phải tắt hoàn toàn SMBv1 và kích hoạt các tính năng ký số (SMB Signing) cùng mã hóa (SMB Encryption) của SMBv3 để đảm bảo an ninh tối đa [6], [7], [8].

---

## TỔNG KẾT CHƯƠNG 1

Chương 1 đã hệ thống hóa toàn diện cơ sở lý thuyết về kiến trúc giao thức SMB, bản chất kỹ thuật của nhóm lỗ hổng MS17-010 và phương pháp luận ứng dụng bộ công cụ kiểm thử an ninh trong môi trường thực nghiệm.

Về mặt kiến trúc giao thức, nghiên cứu làm rõ vai trò của SMB trong chia sẻ tài nguyên và truyền thông liên tiến trình qua Named Pipes. Bản chất giữa Direct-hosted SMB (TCP 445) và NetBIOS over TCP/IP (TCP 139) được phân định rõ ràng. Chuỗi máy trạng thái từ thương lượng dialect, thiết lập phiên đến liên kết tài nguyên cũng được phân tích chi tiết. Sự so sánh đối chiếu giữa ba thế hệ SMBv1, SMBv2 và SMBv3 đã chứng minh sự tiến hóa vượt bậc về năng lực bảo vệ dữ liệu, đặc biệt là các cơ chế mã hóa AES và bảo vệ tính toàn vẹn tiền xác thực Pre-authentication Integrity của SMBv3.

Về mặt cơ chế lỗ hổng, nghiên cứu giải phẫu nguyên nhân gốc rễ của CVE-2017-0144. Sai sót toán học trong khâu cắt ngắn số nguyên tại hàm `SrvOs2FeaListSizeToNt` dẫn tới việc cấp phát thiếu bộ nhớ và gây tràn vùng đệm Non-Paged Pool trong hàm `SrvOs2FeaToNt`. Bản chất phi tất định của kỹ thuật Kernel Pool Grooming và rủi ro gây sập hệ thống (BSOD) đã được chứng minh, làm sáng tỏ tính cấp thiết của việc áp dụng bản vá KB và loại bỏ giao thức cũ.

Về mặt phương pháp luận kiểm thử, đề tài đã xây dựng thang đo nhận thức luận 4 cấp độ thẩm định, phân định rạch ròi giữa khả năng tiếp cận cổng, sự hiện diện của giao thức, dấu hiệu mã lỗi phản hồi từ nhân và năng lực khai thác thực tế. Khung thang đo này giúp triệt tiêu hoàn toàn các sai lệch dương tính giả và âm tính giả trong đánh giá an ninh. Cuối cùng, chiến lược phòng thủ chiều sâu ba tầng kết hợp cùng giải pháp phân đoạn mạng đã giải quyết hài hòa bài toán xung đột giữa yêu cầu bảo mật nghiêm ngặt và tính tương thích nghiệp vụ của hệ thống.

Toàn bộ các luận điểm lý thuyết, cơ chế mã phản hồi và tiêu chí đánh giá được xác lập trong Chương 1 định hướng trực tiếp cho các bước tiếp theo. Đây là cơ sở để thiết kế kiến trúc lab cô lập, cấu hình mạng và xây dựng kịch bản kiểm thử thực nghiệm trong Chương 2.

---

## TÀI LIỆU THAM KHẢO

[1] Microsoft, "What is Microsoft SMB Protocol and CIFS Protocol?," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview

[2] Microsoft, "Direct hosting of SMB over TCP/IP," Microsoft Learn, 2026. [Online]. Available: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/direct-hosting-of-smb-over-tcpip

[3] Microsoft, "[MS-SMB]: Server Message Block (SMB) Protocol," Microsoft Open Specifications, 2026. [Online]. Available: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-smb/f210069c-7086-4dc2-885e-861d837df688

[4] Microsoft, "[MS-SMB2]: Server Message Block (SMB) Protocol Versions 2 and 3," Microsoft Open Specifications, 2026. [Online]. Available: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-smb2/

[5] Microsoft, "What is SMB File Sharing for Windows and Windows Server?," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview

[6] Microsoft, "SMB security enhancements," Microsoft Learn, Jul. 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security

[7] Microsoft, "What is Server Message Block signing?," Microsoft Learn, Oct. 2024. [Online]. Available: https://learn.microsoft.com/windows-server/storage/file-server/smb-signing-overview

[8] Microsoft, "SMB 3.1.1 Pre-authentication integrity in Windows 10," Microsoft Learn, archived Open Specifications blog. [Online]. Available: https://learn.microsoft.com/en-us/archive/blogs/openspecification/smb-3-1-1-pre-authentication-integrity-in-windows-10

[9] Microsoft, "Microsoft Security Bulletin MS17-010 - Critical," Microsoft Learn / Security TechCenter, Mar. 2017. [Online]. Available: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010

[10] National Institute of Standards and Technology (NIST), "CVE-2017-0144 Detail," National Vulnerability Database (NVD), Mar. 2017. [Online]. Available: https://nvd.nist.gov/vuln/detail/CVE-2017-0144

[11] Microsoft Security Response Center (MSRC), "Eternal Synergy Exploit Analysis," Microsoft, 2017. [Online]. Available: https://msrc.microsoft.com/blog/2017/05/eternal-synergy-exploit-analysis/

[12] Microsoft Threat Intelligence, "New ransomware, old techniques: Petya adds-worm capabilities," Microsoft Security Blog, Jun. 2017. [Online]. Available: https://www.microsoft.com/en-us/security/blog/2017/06/27/new-ransomware-old-techniques-petya-adds-worm-capabilities/

[13] Rapid7, "MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption," Rapid7 Exploit Database, 2017. [Online]. Available: https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/

[14] Microsoft Learn, "Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3

[15] Microsoft Threat Intelligence, "WannaCrypt ransomware worm targets out-of-date systems," Microsoft Security Blog, May 2017. [Online]. Available: https://www.microsoft.com/en-us/security/blog/2017/05/12/wannacrypt-ransomware-worm-targets-out-of-date-systems/

[16] National Institute of Standards and Technology (NIST), "Technical Guide to Information Security Testing and Assessment," NIST Special Publication 800-115, 2008. [Online]. Available: https://csrc.nist.gov/pubs/sp/800/115/final

[17] Kali Linux Project, "What is Kali Linux?," Kali Linux Documentation. [Online]. Available: https://www.kali.org/docs/introduction/what-is-kali-linux/

[18] G. Lyon, *Nmap Network Scanning: The Official Nmap Project Guide to Network Discovery and Vulnerability Scanning*. Sunnyvale, CA: Insecure.Com LLC, 2009. [Online]. Available: https://nmap.org/book/

[19] P. Calderon and Nmap Project, "smb-protocols.nse Script Source Code," Nmap Project. [Online]. Available: https://svn.nmap.org/nmap/scripts/smb-protocols.nse

[20] P. Calderon and Nmap Project, "smb-vuln-ms17-010.nse Script Source Code," Nmap Project, 2017. [Online]. Available: https://svn.nmap.org/nmap/scripts/smb-vuln-ms17-010.nse

[21] Rapid7, "Metasploit Framework," Metasploit Documentation. [Online]. Available: https://docs.rapid7.com/metasploit/msf-overview/

[22] Rapid7, "MS17-010 SMB RCE Detection," Metasploit Framework, source code. [Online]. Available: https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/scanner/smb/smb_ms17_010.rb

[23] National Institute of Standards and Technology (NIST), "Guidelines on Firewalls and Firewall Policy," NIST Special Publication 800-41 Rev. 1, 2009. [Online]. Available: https://csrc.nist.gov/pubs/sp/800/41/r1/final
