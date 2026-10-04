# CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ CÔNG CỤ KIỂM THỬ SMB

## 1.1. Tổng quan về giao thức SMB

### 1.1.1. Khái niệm và vai trò của SMB

Server Message Block (SMB) là giao thức mạng hoạt động ở tầng ứng dụng (Application Layer), cung cấp cơ chế chia sẻ tệp tin, thư mục, máy in và hỗ trợ giao tiếp liên tiến trình (Inter-Process Communication - IPC) giữa các máy tính qua mạng.

Trên hệ điều hành Windows, SMB là giao thức truyền thông mặc định cho các dịch vụ mạng nội bộ, hoạt động trực tiếp trên nền giao thức TCP qua cổng 445 hoặc kết hợp với tầng NetBIOS over TCP/IP qua cổng 139.

Giao thức vận hành theo mô hình Client - Server, trong đó bên yêu cầu tài nguyên đóng vai trò SMB Client và bên tiếp nhận, kiểm soát, chia sẻ tài nguyên đóng vai trò SMB Server.

**Vai trò trong hệ thống:**

- **Chia sẻ dữ liệu và quản lý tệp tin từ xa:** Cung cấp phương thức cho người dùng và ứng dụng thực hiện các thao tác đọc, ghi, tạo mới, khóa tệp và chỉnh sửa dữ liệu trực tiếp trên các thư mục dùng chung (Network Shares) trong mạng nội bộ.
- **Chia sẻ tài nguyên thiết bị ngoại vi:** Đóng vai trò làm giao thức trung gian điều phối lệnh in ấn và quản lý hàng đợi tài liệu đối với các máy in được chia sẻ chung trong hệ thống mạng.
- **Hỗ trợ giao tiếp liên tiến trình (IPC) và quản trị từ xa:** Cung cấp cơ chế Named Pipes để truyền tải các lệnh gọi thủ tục từ xa (Remote Procedure Call - RPC), phục vụ công tác xác thực tập trung và quản trị hệ thống Windows từ xa.
- **Xác thực và kiểm soát truy cập an toàn:** Tích hợp với các cơ chế xác thực của Windows (NTLM, Kerberos) để định danh người dùng, đàm phán cấp độ bảo mật (dialect negotiation), thiết lập phiên làm việc (Session Setup) và kiểm tra quyền hạn (Access Control List - ACL) trước khi cấp quyền truy cập tài nguyên.

### 1.1.2. Mô hình Client – Server trên Windows

**Kiến trúc tổng thể:**

- Dịch vụ SMB trên Windows được thiết kế và vận hành theo mô hình Client - Server, phân định rõ vai trò giữa bên khởi tạo yêu cầu và bên tiếp nhận, xử lý yêu cầu.
- Phía SMB Client chịu trách nhiệm gửi các yêu cầu kết nối, xác thực và truy cập tệp tin hoặc thiết bị từ xa qua môi trường mạng.
- Phía SMB Server chịu trách nhiệm quản lý, công bố các tài nguyên chia sẻ (Shares), tiếp nhận và phản hồi các yêu cầu từ Client theo quyền hạn đã được cấp phát.

**Các thành phần cốt lõi trên hệ điều hành Windows:**

- **SMB Client (Workstation Service):** Dịch vụ chạy nền trên Windows, phối hợp với trình chuyển hướng mạng (Network Redirector) để điều hướng các thao tác I/O trên tệp tin từ xa qua mạng thay vì hệ thống tệp cục bộ.
- **SMB Server (Server Service):** Dịch vụ tiếp nhận các kết nối mạng đến cổng 139 hoặc 445, chuyển tiếp các yêu cầu xử lý gói tin cho trình điều khiển cấp nhân (Kernel-mode driver như `srv.sys` đối với SMBv1 hoặc `srv2.sys` đối với SMBv2/SMBv3).

**Quy trình tương tác giữa Client và Server:**

- **Bước 1 - Thiết lập kết nối truyền tải:** Client mở kết nối TCP tới cổng 445 (hoặc NetBIOS qua cổng 139) của Server.
- **Bước 2 - Thương lượng giao thức (Negotiate Protocol):** Client gửi danh sách các dialect (phiên bản SMB) hỗ trợ; Server phản hồi để chọn dialect cao nhất mà hai bên cùng tương thích.
- **Bước 3 - Xác thực và thiết lập phiên (Session Setup):** Hai bên trao đổi thông tin định danh (sử dụng cơ chế NTLM hoặc Kerberos) để xác thực người dùng và cấp phát định danh phiên (Session ID).
- **Bước 4 - Kết nối tài nguyên chia sẻ (Tree Connect):** Client gửi yêu cầu kết nối tới một thư mục chia sẻ cụ thể (như `C$`, `IPC$`, hoặc thư mục được chia sẻ công khai) và nhận về một mã định danh kết nối (Tree ID).
- **Bước 5 - Thao tác dữ liệu:** Client thực hiện các lệnh đọc, ghi, tạo mới hoặc đóng tệp tin trên Server dựa trên quyền hạn đã được kiểm tra.

**Đặc điểm vận hành trên Windows:**

- **Tính linh hoạt vai trò:** Một máy tính chạy Windows có thể đồng thời đóng vai trò SMB Client khi truy xuất tài nguyên của máy khác và làm SMB Server khi chia sẻ thư mục của chính nó ra mạng nội bộ.
- **Hoạt động ở Kernel-mode:** Trình điều khiển phía Server chạy trực tiếp trong không gian hệ điều hành nhằm đảm bảo hiệu năng I/O cao, khiến bất kỳ lỗi xử lý gói tin nào tại thành phần này đều có nguy cơ ảnh hưởng trực tiếp đến độ ổn định và an toàn của toàn bộ hệ thống.

### 1.1.3. SMBv1, SMBv2 và SMBv3

Giao thức Server Message Block trên Windows được phân loại thành ba phiên bản chính với sự khác biệt về cấu trúc lệnh, tốc độ truyền tải và tính an toàn:

**Phiên bản SMBv1 (CIFS):**

- SMBv1 vận hành với hơn 100 mã lệnh và sử dụng cơ chế trao đổi dữ liệu tuần tự từng bước. Cách thức này tạo ra nhiều lượt truyền nhận qua lại không cần thiết, làm đường truyền mạng bị trễ và giảm hiệu năng rõ rệt.
- Về mặt bảo mật, SMBv1 không hỗ trợ mã hóa luồng dữ liệu và chỉ dùng thuật toán MD5 cũ để kiểm tra gói tin. Đặc biệt, driver hệ thống `srv.sys` của Windows khi xử lý các gói tin SMBv1 gặp lỗi quản lý bộ nhớ nghiêm trọng, dẫn đến nhóm lỗ hổng thực thi mã từ xa MS17-010 (EternalBlue) cho phép kẻ tấn công chiếm quyền điều khiển máy tính mà không cần tài khoản đăng nhập.

**Phiên bản SMBv2:**

- Được Microsoft đưa vào từ Windows Vista và Windows Server 2008 nhằm thay thế hoàn toàn SMBv1. Điểm cải tiến lớn nhất là bộ mã lệnh được rút gọn từ hơn 100 lệnh xuống còn 19 lệnh tiêu chuẩn, đồng thời bổ sung tính năng gộp nhiều yêu cầu vào một gói tin duy nhất để tiết kiệm băng thông và giảm thời gian phản hồi.
- SMBv2 tổ chức lại việc quản lý phiên làm việc và kết nối tài nguyên rõ ràng hơn, đồng thời nâng cấp cơ chế chống sửa đổi gói tin lên chuẩn HMAC-SHA256, giúp bảo vệ dữ liệu trao đổi không bị can thiệp trái phép trên đường truyền.

**Phiên bản SMBv3:**

- Được phát triển từ Windows 8 và Windows Server 2012, kế thừa nền tảng của SMBv2 và bổ sung các cơ chế bảo mật mạnh mẽ cho hệ thống mạng hiện đại:
  - **Mã hóa dữ liệu đầu cuối (SMB Encryption):** Dùng thuật toán chuẩn AES (AES-CCM, AES-GCM) trực tiếp ở tầng ứng dụng, giúp chống nghe lén và đánh cắp thông tin mà không cần thiết lập thêm hạ tầng IPsec phức tạp.
  - **Chống sửa đổi gói tin (SMB Signing):** Sử dụng các thuật toán AES-CMAC và AES-GMAC để xác thực nguồn gốc và đảm bảo gói tin gửi đi không bị chèn ép hay chỉnh sửa.
  - **Tối ưu tốc độ và dự phòng mạng:** Hỗ trợ SMB Multichannel để gộp băng thông và dự phòng lỗi qua nhiều card mạng cùng lúc; hỗ trợ SMB Direct qua công nghệ RDMA giúp truyền tệp tốc độ cao mà không làm quá tải CPU máy chủ.

### 1.1.4. Quy trình thỏa thuận phiên bản kết nối SMB

**Khái niệm về SMB Dialect:**

Trong giao thức SMB, Dialect là thuật ngữ dùng để chỉ phiên bản cụ thể hoặc tập hợp quy chuẩn giao tiếp mà Client và Server sử dụng để hiểu nhau. Mỗi thế hệ Windows được phát triển đều hỗ trợ thêm các dialect mới, đồng thời duy trì khả năng tương thích ngược với các dialect cũ hơn. Ví dụ:

- **SMBv1:** Sử dụng các chuỗi định danh dạng văn bản, tiêu biểu là `NT LM 0.12` (chuẩn SMBv1 phổ biến nhất trên Windows NT/2000/XP/7).
- **SMBv2:** Sử dụng mã số hiệu, gồm SMB 2.0.2 (Windows Vista), SMB 2.1 (Windows 7 / Server 2008 R2).
- **SMBv3:** Gồm SMB 3.0 (Windows 8 / Server 2012), SMB 3.0.2 (Windows 8.1) và SMB 3.1.1 (Windows 10 / Server 2016 trở lên).

**Mục đích của quá trình thương lượng (Negotiate Protocol):**

Thương lượng dialect là bước giao tiếp bắt buộc đầu tiên ngay sau khi hai máy tính thiết lập thành công kết nối TCP (qua cổng 445 hoặc 139). Quá trình này giúp hai bên thống nhất phiên bản giao thức cao nhất mà cả hai cùng hỗ trợ, đồng thời thiết lập các tham số vận hành ban đầu như: kích thước bộ nhớ đệm tối đa, cơ chế xác thực hỗ trợ, yêu cầu bật/tắt tính năng chống sửa đổi gói tin (SMB Signing) và khóa mã hóa.

**Quy trình đàm phán giữa Client và Server:**

Quá trình này diễn ra qua hai bản tin trao đổi cơ bản:

- **Gói tin yêu cầu thương lượng (Negotiate Request):** Client gửi đến Server một danh sách chứa tất cả các dialect mà nó có thể hỗ trợ, sắp xếp theo thứ tự từ phiên bản mới nhất đến các phiên bản cũ hơn.
- **Gói tin phản hồi thương lượng (Negotiate Response):** Server tiếp nhận danh sách, đối chiếu với các dialect mà nó đã kích hoạt và chọn ra phiên bản cao nhất chung giữa hai hệ thống để phản hồi lại Client. Nếu hai bên không tìm được phiên bản tương thích chung, kết nối mạng sẽ bị hủy bỏ ngay lập tức.

### 1.1.5. Xác thực và thiết lập phiên

**Mục đích của việc thiết lập phiên:**

Sau khi hoàn tất thỏa thuận phiên bản giao thức, Client và Server phải thực hiện quy trình xác thực và thiết lập phiên làm việc (Session Setup). Mục đích của quá trình này là kiểm tra danh tính người dùng hoặc máy tính yêu cầu kết nối, gán quyền hạn tương ứng và cấp một mã định danh phiên (Session ID đối với SMBv2/v3 hoặc UID đối với SMBv1) để duy trì kênh giao tiếp an toàn cho các yêu cầu kế tiếp.

**Các cơ chế xác thực phổ biến:**

- **Xác thực NTLM (NTLMv1/NTLMv2):** Hoạt động theo cơ chế hỏi - đáp (Challenge - Response), thường được sử dụng trong mô hình mạng ngang hàng (Workgroup) hoặc dùng để tương thích ngược khi hệ thống chưa có hạ tầng quản lý người dùng tập trung.
- **Xác thực Kerberos:** Là cơ chế mặc định và có tính an toàn cao trong môi trường quản lý tập trung (Active Directory Domain Services), dựa trên việc cấp và kiểm tra các vé chứng thực (Tickets) để tránh truyền dữ liệu nhạy cảm qua mạng.
- **Kết nối ẩn danh (Anonymous / Null Session):** Cho phép Client gửi yêu cầu kết nối mà không cần tài khoản hay mật khẩu, thường dùng để truy vấn sơ bộ thông tin máy chủ hoặc kết nối tới tài nguyên chia sẻ ngầm định `IPC$`.

**Quy trình trao đổi bản tin:**

Quá trình xác thực và khởi tạo phiên làm việc diễn ra qua các bước tuần tự:

- **Gửi gói yêu cầu thiết lập phiên (Session Setup Request):** Client gửi gói tin chứa thông tin định danh người dùng hoặc dữ liệu xác thực (NTLM token hoặc Kerberos ticket) tới Server.
- **Xác minh và phản hồi kết quả (Session Setup Response):** Server kiểm tra tính hợp lệ của tài khoản trong cơ sở dữ liệu cục bộ hoặc gửi sang máy chủ quản lý miền (Domain Controller). Khi thông tin chính xác, Server cấp phát mã Session ID và gửi trả về Client. Kể từ thời điểm này, mọi thao tác truy cập dữ liệu của Client đều phải đính kèm mã định danh phiên này để Server kiểm soát quyền hạn.

### 1.1.6. Chia sẻ và truy cập tài nguyên

**Mục đích của việc kết nối tài nguyên (Tree Connect):**

Sau khi hoàn tất bước xác thực và nhận được mã phiên (Session ID), Client cần kết nối trực tiếp đến một vùng tài nguyên cụ thể do Server cung cấp để bắt đầu làm việc. Quá trình này được gọi là gắn kết tài nguyên (Tree Connect). Máy chủ sẽ kiểm tra quyền hạn của tài khoản trên tài nguyên đó và phản hồi một mã định danh kết nối (Tree ID - TID) để theo dõi xuyên suốt quá trình thao tác.

**Các loại tài nguyên chia sẻ trên hệ điều hành Windows:**

- **Thư mục chia sẻ thông thường:** Các thư mục dữ liệu do người dùng hoặc quản trị viên tạo ra để phục vụ nhu cầu trao đổi tệp tin trong mạng nội bộ, được kiểm soát quyền hạn bằng danh sách truy cập (Share Permissions và NTFS Permissions).
- **Tài nguyên chia sẻ quản trị (Administrative Shares):** Các vùng chia sẻ ngầm định có ký tự `$` ở cuối tên (như `C$`, `D$`, `ADMIN$`), phục vụ mục đích quản trị hệ thống từ xa và chỉ cho phép các tài khoản thuộc nhóm Quản trị viên (Administrators) truy cập.
- **Tài nguyên chia sẻ đặc biệt (IPC$ - Inter-Process Communication):** Đây là vùng chia sẻ không chứa tệp tin thực tế, mà đóng vai trò làm kênh truyền dữ liệu trung gian (Named Pipes) phục vụ giao tiếp giữa các tiến trình và hỗ trợ các lệnh gọi từ xa (RPC) giữa các máy tính Windows.

**Quy trình kết nối:**

- **Gửi yêu cầu kết nối (Tree Connect Request):** Client gửi gói tin chứa đường dẫn tài nguyên cần truy cập kèm theo mã Session ID đã được cấp trước đó.
- **Phản hồi cấp quyền (Tree Connect Response):** Server đối chiếu quyền hạn truy cập của tài khoản với tài nguyên yêu cầu nếu hợp lệ, Server trả về mã định danh Tree ID (TID).
- **Thực thi lệnh đọc/ghi dữ liệu:** Mọi thao tác tệp tin kế tiếp (như tạo mới, đọc, ghi hoặc xóa tệp) đều phải sử dụng đồng thời bộ đôi mã Session ID và Tree ID để Server xác thực tính hợp lệ trước khi cho phép thực thi.

### 1.1.7. Cổng mạng TCP 139 và TCP 445 trong kết nối SMB

Để truyền tải dữ liệu giữa Client và Server, giao thức SMB sử dụng hai cổng dịch vụ mạng chính với cơ chế hoạt động khác nhau tùy thuộc vào phiên bản hệ điều hành:

- **Cổng TCP 139 (Kết nối qua NetBIOS):** Được sử dụng chủ yếu trên các phiên bản Windows đời cũ (Windows 95, 98, NT). Ở phương thức này, dữ liệu SMB không truyền trực tiếp qua giao thức TCP mà phải bọc trong một lớp trung gian là NetBIOS qua TCP/IP (NBT). Trước khi gửi các lệnh SMB, hai máy tính phải hoàn tất bước thiết lập phiên NetBIOS (NetBIOS Session Service). Quá trình tìm kiếm máy tính và phân giải địa chỉ phụ thuộc vào tên máy NetBIOS thay vì dùng hệ thống tên miền DNS.
- **Cổng TCP 445 (Kết nối trực tiếp qua TCP):** Được Microsoft bổ sung từ phiên bản Windows 2000 trở về sau, cho phép giao thức SMB chạy trực tiếp trên nền TCP/IP mà không cần lớp trung gian NetBIOS (Direct Hosted SMB). Cơ chế này loại bỏ phần tiêu đề NetBIOS dư thừa, giúp cấu trúc gói tin đơn giản hơn và tăng tốc độ truyền dữ liệu. Hệ thống phân giải tên máy tính trực tiếp bằng DNS hoặc kết nối thẳng bằng địa chỉ IP, phù hợp với tiêu chuẩn mạng Internet hiện đại.

**Cơ chế tự động lựa chọn cổng kết nối:**

Khi người dùng thực hiện truy cập đến một thư mục chia sẻ, hệ điều hành Windows sẽ tự động gửi đồng thời hai gói tin bắt tay TCP đến cả cổng 445 và cổng 139 của máy đích:
- Nếu cổng 445 phản hồi trước, kết nối SMB trực tiếp sẽ được thiết lập và gói tin kết nối đến cổng 139 bị hủy bỏ.
- Nếu cổng 445 bị chặn hoặc máy đích không hỗ trợ, kết nối sẽ tự động lùi về (fallback) sử dụng cổng 139 qua NetBIOS.

---

## 1.2. Lỗ hổng bảo mật MS17-010

### 1.2.1. Tổng quan về MS17-010

Vào tháng 03 năm 2017, Microsoft phát hành bản tin an ninh MS17-010 nhằm khắc phục sáu lỗ hổng bảo mật liên quan đến giao thức SMBv1 trong hệ điều hành Windows. Nhóm lỗ hổng này bao gồm năm lỗ hổng thực thi mã từ xa (Remote Code Execution - RCE) và một lỗ hổng tiết lộ thông tin (Information Disclosure). Đây là bản tin an ninh tổng hợp bao trùm nhiều vấn đề kỹ thuật khác nhau, không đại diện cho một lỗi đơn lẻ.

Nguyên nhân gốc rễ bắt nguồn từ việc giao thức SMBv1 được thiết kế từ giai đoạn sớm của mạng máy tính, khi các cơ chế kiểm soát biên dữ liệu chưa được hoàn thiện. Do trình điều khiển `srv.sys` vận hành trực tiếp trong không gian nhân (Kernel Mode) nhằm tối ưu hiệu năng I/O, các thiếu sót trong quản lý bộ nhớ tại thành phần này có thể đe dọa trực tiếp đến tính ổn định và an toàn của hệ điều hành. Bản tin ảnh hưởng đến nhiều phiên bản Windows còn lưu hành tại thời điểm công bố.

Trong phạm vi đồ án, nhóm em tập trung vào lỗ hổng thực thi mã từ xa không yêu cầu xác thực trong nhóm này để làm rõ rủi ro của dịch vụ SMBv1, đồng thời xây dựng quy trình kiểm thử và đối chứng phòng thủ có kiểm soát.

### 1.2.2. Các CVE liên quan

Bản tin MS17-010 xử lý sáu mã lỗ hổng (Common Vulnerabilities and Exposures - CVE) với các đặc điểm kỹ thuật khác nhau:

- **CVE-2017-0143 (RCE):** Lỗ hổng thực thi mã từ xa phát sinh từ cách xử lý các thông điệp giao dịch phụ (Transaction2) trong SMBv1 khi nhận chuỗi yêu cầu bất thường.
- **CVE-2017-0144 (RCE):** Lỗ hổng thực thi mã từ xa do lỗi kiểm soát kích thước khi xử lý cấu trúc thuộc tính tệp mở rộng (FEA) trong SMBv1, dẫn đến tràn bộ nhớ nhân.
- **CVE-2017-0145 (RCE):** Lỗ hổng thực thi mã từ xa liên quan đến việc xác thực tham số bộ đệm trong các yêu cầu giao dịch SMBv1.
- **CVE-2017-0146 (RCE):** Lỗ hổng thực thi mã từ xa do xử lý con trỏ và đối tượng bộ nhớ không an toàn trong driver `srv.sys`.
- **CVE-2017-0147 (Information Disclosure):** Lỗ hổng tiết lộ thông tin từ bộ nhớ nhân về phía client thông qua các gói tin phản hồi SMBv1 không được xóa trắng dữ liệu.
- **CVE-2017-0148 (RCE):** Lỗ hổng thực thi mã từ xa do lỗi kiểm tra hợp lệ trong quá trình xử lý các gói tin giao dịch liên tiếp.

Việc phân định các mã CVE cho thấy MS17-010 là một tập hợp lỗi với cơ chế khác nhau. Trong số này, CVE-2017-0144 là đối tượng trung tâm được nhóm em phân tích và kiểm chứng trong đồ án do đặc tính không đòi hỏi xác thực tài khoản và mức độ tác động trực tiếp đến dịch vụ SMBv1.

### 1.2.3. Cơ chế xử lý yêu cầu SMBv1 dẫn đến lỗ hổng

Lỗ hổng CVE-2017-0144 liên quan đến quá trình driver `srv.sys` xử lý các thuộc tính tệp mở rộng (Full Extended Attributes - FEA) được gửi qua các gói tin giao dịch của SMBv1. Cấu trúc FEA vốn được duy trì để bảo đảm khả năng tương thích ngược với hệ thống tệp cũ.

Khi client gửi yêu cầu chứa danh sách các thuộc tính FEA, `srv.sys` cần chuyển đổi danh sách này sang cấu trúc định dạng nội bộ của Windows NT. Quá trình xử lý bao gồm hai bước chính:
- Đầu tiên, hàm `SrvOs2FeaListSizeToNt` duyệt qua danh sách để tính toán tổng dung lượng bộ nhớ cần cấp phát trong bộ nhớ nhân (Kernel Pool).
- Sau đó, hệ thống cấp phát vùng đệm và hàm `SrvOs2FeaToNt` tiến hành sao chép các phần tử dữ liệu vào vùng đệm đã tạo.

Vấn đề phát sinh do sai lệch trong khâu kiểm soát và chuyển đổi kích thước dữ liệu: giá trị kích thước được tính toán ở bước đầu bị thiếu hụt so với lượng dữ liệu thực tế được ghi ở bước sau. Hậu quả là hệ điều hành chỉ chuẩn bị một vùng đệm nhỏ hơn nhu cầu, khiến quá trình sao chép ghi dữ liệu vượt ra ngoài phạm vi vùng nhớ dự kiến trong kernel pool (Kernel Pool Overflow).

Lỗi xảy ra trực tiếp trong không gian nhân của hệ điều hành, khiến việc vùng nhớ bị ghi đè có thể dẫn đến tình trạng mất ổn định và phát sinh lỗi dừng (BSOD). Ngoài ra, các mã khai thác như EternalBlue có thể lợi dụng sự sai lệch bố cục bộ nhớ này để thực thi mã lệnh tùy ý với đặc quyền hệ thống cao nhất.

### 1.2.4. Điều kiện ảnh hưởng và điều kiện khai thác

Trong đánh giá an ninh, cần phân định rõ giữa điều kiện để một hệ thống tồn tại lỗ hổng và điều kiện để tác động từ xa có thể xảy ra trên thực tế:

**Điều kiện hệ thống có thể bị ảnh hưởng:**
- Hệ điều hành thuộc danh mục các phiên bản Windows chịu tác động của bản tin MS17-010.
- Dịch vụ SMBv1 đang được kích hoạt và driver `srv.sys` đang hoạt động để tiếp nhận yêu cầu mạng.
- Bản cập nhật an ninh MS17-010 tương ứng chưa được cài đặt trên hệ thống.

**Điều kiện để tác động từ xa có thể xảy ra:**
- Trạm kiểm thử có đường truyền mạng thông suốt đến cổng dịch vụ SMB (TCP 445 hoặc TCP 139) của máy chủ mục tiêu.
- Các luồng giao tiếp SMB cần thiết không bị tường lửa mạng hoặc tường lửa cục bộ ngăn chặn.
- Phiên bản hệ điều hành, cấu trúc dịch vụ và trạng thái bộ nhớ của mục tiêu tương thích với kỹ thuật can thiệp được sử dụng.

Sự phân định này chỉ ra rằng trạng thái mở cổng TCP 445 chỉ là điều kiện tiếp cận ban đầu ở tầng giao vận:
- Một máy chủ mở cổng 445 và hỗ trợ SMBv1 nhưng đã được cập nhật bản vá thì lỗi xử lý dữ liệu trong `srv.sys` đã được khắc phục.
- Ngược lại, một máy chủ tồn tại lỗ hổng nhưng đặt sau tường lửa chặn truy cập SMB từ bên ngoài thì tác động từ xa không thể thực hiện được qua ranh giới mạng đó.

Như vậy, mở cổng mạng không đồng nghĩa với việc hỗ trợ SMBv1, hỗ trợ SMBv1 không đồng nghĩa với hệ thống chưa vá, và sự tồn tại của lỗ hổng cũng không đồng nghĩa với việc khai thác chắc chắn thành công.

### 1.2.5. Tác động của lỗ hổng

Tác động của lỗ hổng CVE-2017-0144 thuộc nhóm MS17-010 được xem xét qua ba khía cạnh an toàn thông tin:

- **Tính bảo mật (Confidentiality):** Nếu mã can thiệp thực thi thành công với đặc quyền cao trong nhân hệ điều hành, các dữ liệu lưu trữ trên máy chủ, thông tin xác thực tài khoản và cấu hình hệ thống đều có nguy cơ bị truy cập trái phép.
- **Tính toàn vẹn (Integrity):** Kẻ tấn công có thể thay đổi dữ liệu, chỉnh sửa tệp tin hệ thống hoặc can thiệp vào các chính sách bảo mật trong phạm vi quyền hạn đạt được.
- **Tính sẵn sàng (Availability):** Do can thiệp trực tiếp vào bộ nhớ cấp nhân, các thao tác xử lý không tương thích rất dễ dẫn đến lỗi dừng hệ thống (BSOD). Bên cạnh đó, kẻ tấn công có thể chủ động làm gián đoạn dịch vụ hoặc khóa tài nguyên.

Điểm đáng lưu ý là lỗ hổng này có thể kích hoạt từ xa qua gói tin mạng mà không bắt buộc phải có sự tương tác của người dùng hay tài khoản đăng nhập trước đó, khiến rủi ro lây lan tự động trở nên đặc biệt nghiêm trọng.

### 1.2.6. Mối liên hệ với các cuộc tấn công thực tế

Tác động thực tế của nhóm lỗ hổng MS17-010 đã được minh chứng qua các sự cố an ninh mạng diện rộng trong năm 2017:

- **Chiến dịch mã độc WannaCry (Tháng 05/2017):** Mã khai thác EternalBlue bị rò rỉ đã được tích hợp vào cơ chế sâu mạng tự động. WannaCry quét cổng TCP 445 trên Internet và mạng nội bộ, tự động lây nhiễm vào các máy Windows chưa vá để mã hóa dữ liệu đòi tiền chuộc, gây ảnh hưởng đến hàng trăm nghìn hệ thống tại nhiều quốc gia.
- **Chiến dịch mã độc NotPetya (Tháng 06/2017):** NotPetya tiếp tục sử dụng các kỹ thuật khai thác trong nhóm MS17-010 để phát tán nhanh chóng trong mạng nội bộ. Mã độc nhắm vào việc phá hoại cấu trúc bản ghi khởi động (MBR) của ổ đĩa, khiến hệ thống không thể khởi động lại và gây gián đoạn hoạt động của nhiều tổ chức.

Các sự cố này cho thấy việc duy trì giao thức cũ SMBv1 kết hợp với sự chậm trễ trong cập nhật bản vá có thể tạo ra rủi ro an ninh nghiêm trọng cho toàn bộ hệ thống mạng. Thực tế đó dẫn đến nhu cầu cần có phương pháp kiểm tra, phân loại trạng thái dịch vụ SMB một cách an toàn và có kiểm soát.

---

## 1.3. Công cụ phục vụ kiểm thử

### 1.3.1. Kali Linux

Trong đồ án này, Kali Linux được nhóm em sử dụng làm trạm kiểm thử (Testing Workstation) chuyên dụng. Hệ điều hành cung cấp môi trường dòng lệnh tập trung, tích hợp sẵn các tiện ích mạng, thư viện và công cụ kiểm định bảo mật cần thiết để tương tác với máy chủ Windows mục tiêu.

Vai trò chính của trạm kiểm thử là khởi tạo các yêu cầu thăm dò, quản lý cấu hình kết nối mạng và ghi nhận nhật ký (log) của quá trình đánh giá. Bản thân Kali Linux chỉ đóng vai trò nền tảng điều khiển; việc đánh giá an ninh phụ thuộc vào phương pháp và kịch bản thực thi của từng công cụ cụ thể được triển khai bên trong.

### 1.3.2. Nmap

Nmap (Network Mapper) được nhóm em sử dụng cho bước trinh sát ban đầu nhằm xác định các máy chủ đang hoạt động và kiểm tra khả năng tiếp cận dịch vụ qua hai cổng mạng TCP 139 và TCP 445.

Dữ liệu do Nmap cung cấp phản ánh trạng thái cổng ở tầng giao vận:
- `Open`: Cổng mạng có tiến trình lắng nghe và tiếp nhận kết nối TCP (phản hồi gói tin TCP SYN-ACK trước yêu cầu SYN từ trạm kiểm thử).
- `Closed`: Cổng mạng không có dịch vụ nào tiếp nhận (phản hồi gói tin RST).
- `Filtered`: Gói tin thăm dò không nhận được phản hồi hoặc bị chặn bởi chính sách tường lửa.

Tùy chọn `-sV` của Nmap hỗ trợ nhận diện sơ bộ tên dịch vụ ứng dụng như `microsoft-ds` hoặc `netbios-ssn`. Tuy nhiên, kết quả từ Nmap chỉ xác nhận cổng dịch vụ có mở từ góc nhìn mạng hay không. Trạng thái cổng 445 `Open` không đồng nghĩa với việc máy chủ hỗ trợ SMBv1, cũng không chứng minh hệ thống tồn tại lỗ hổng MS17-010 hay có thể bị khai thác. Nmap đóng vai trò sàng lọc ở bước đầu tiên để định vị mục tiêu.

### 1.3.3. Nmap Scripting Engine

Nmap Scripting Engine (NSE) mở rộng khả năng kiểm tra của Nmap lên tầng ứng dụng thông qua các kịch bản viết bằng ngôn ngữ Lua. Trong đồ án, hai kịch bản chuyên biệt được nhóm em sử dụng gồm:

- **Kịch bản `smb-protocols.nse`:** Gửi yêu cầu thương lượng (`Negotiate Protocol Request`) chứa danh sách dialect để phân tích phản hồi từ máy chủ, qua đó nhận diện hệ thống có chấp thuận giao thức SMBv1 (`NT LM 0.12`) hay không.
- **Kịch bản `smb-vuln-ms17-010.nse`:** Thăm dò dấu hiệu của MS17-010 bằng cách gửi gói tin giao dịch kiểm tra logic qua giao diện SMB.

Kịch bản đánh giá dựa trên mã trạng thái NT Status trả về từ hệ điều hành máy chủ:
- Nếu nhận mã lỗi bộ nhớ `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`), hệ thống bộc lộ dấu hiệu chưa được vá theo logic kiểm tra và kịch bản đưa ra cảnh báo `State: VULNERABLE`.
- Nếu nhận mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc yêu cầu bị từ chối, phản hồi này phù hợp với trạng thái không bộc lộ dấu hiệu vulnerable theo logic của script. Dù vậy, kết quả này chưa đủ để kết luận độc lập rằng hệ thống đã được vá, vì phản hồi còn chịu ảnh hưởng của chính sách truy cập và cấu hình dịch vụ.

Cần nhấn mạnh rằng NSE chỉ phân tích mã lỗi logic từ một gói tin thăm dò chứ không thực hiện chuỗi khai thác thực tế. Vì vậy, kết quả từ NSE có giá trị như một chỉ báo kỹ thuật, không phải bằng chứng khẳng định việc khai thác chắc chắn thành công.

### 1.3.4. Metasploit Framework

Metasploit Framework được nhóm em sử dụng như một công cụ đối chiếu và xác minh sâu hơn trong phạm vi thực nghiệm:

- **Mô-đun phụ trợ (Auxiliary Module):** Mô-đun `auxiliary/scanner/smb/smb_ms17_010` thực hiện quét độc lập, cung cấp dữ liệu đối chiếu chéo với kịch bản NSE nhằm tăng độ tin cậy của chỉ báo lỗ hổng.
- **Mô-đun khai thác có kiểm soát (Exploit Module):** Mô-đun `exploit/windows/smb/ms17_010_eternalblue` thuộc bước xác minh tác động ở mức sâu hơn, phục vụ việc đánh giá khả năng thực thi mã trên máy chủ mục tiêu.

Khác với các công cụ quét thụ động, mô-đun khai thác tác động trực tiếp vào luồng xử lý bộ nhớ của hệ thống. Kết quả thu được dù thành công, thất bại hay gây mất ổn định dịch vụ đều phải được diễn giải thận trọng cùng với phiên bản hệ điều hành, cấu hình dịch vụ và các điều kiện kỹ thuật đi kèm.

### 1.3.5. Vai trò của các công cụ trong quy trình kiểm thử

Các công cụ được nhóm em phối hợp theo một chuỗi quy trình có thứ tự logic:

- **Trạm kiểm thử Kali Linux:** Cung cấp môi trường điều hành để thực thi đồng bộ các công cụ và ghi nhận dữ liệu.
- **Nmap:** Xác định khả năng tiếp cận dịch vụ qua việc phát hiện các cổng mạng đang mở.
- **Nmap Scripting Engine:** Tương tác ở tầng ứng dụng để nhận diện việc hỗ trợ SMBv1 và thu thập dấu hiệu của MS17-010.
- **Metasploit Framework:** Đóng vai trò đối chiếu độc lập và thực hiện bước xác minh sâu hơn khi các dấu hiệu trước đó đã được xác lập.

Sự liên kết này bảo đảm quá trình kiểm tra diễn ra từ diện rộng đến chuyên sâu, giúp người kiểm thử hiểu rõ bản chất từng lớp thông tin trước khi đưa ra nhận định về an ninh của hệ thống. Đây là cơ sở trực tiếp để xây dựng khung tiêu chí phân loại trạng thái trong mục tiếp theo.

---

## 1.4. Tiêu chí xác minh trạng thái SMB và MS17-010

### 1.4.1. Phát hiện dịch vụ SMB

Mức 1 xác định sự hiện diện của dịch vụ SMB trên đường truyền mạng giữa trạm kiểm thử và máy chủ mục tiêu:

- **Dấu hiệu quan sát:** Trạm kiểm thử gửi gói tin TCP SYN tới cổng TCP 445 hoặc TCP 139. Trạng thái cổng được ghi nhận là `Open` khi máy chủ phản hồi gói tin TCP SYN-ACK.
- **Ý nghĩa:** Chứng minh máy chủ đang vận hành một dịch vụ mạng sẵn sàng tiếp nhận kết nối SMB từ bên ngoài.
- **Ranh giới kết luận:** Trạng thái mở cổng 445 hoặc 139 chỉ phản ánh khả năng kết nối ở tầng giao vận, hoàn toàn không đồng nghĩa với việc hệ thống có lỗ hổng. Mọi máy chủ Windows đang chia sẻ tệp tin hoặc máy in hợp lệ đều mở các cổng này.

### 1.4.2. Nhận diện SMBv1

Mức 2 kiểm tra xem dịch vụ SMB của máy chủ có chấp thuận giao tiếp bằng phiên bản cũ SMBv1 hay không:

- **Tiêu chí giao thức:** Trạm kiểm thử gửi gói tin `Negotiate Protocol Request` chứa danh sách các dialect. Hệ thống được xác nhận có hỗ trợ SMBv1 khi phản hồi bằng gói tin lựa chọn dialect `NT LM 0.12`.
- **Ý nghĩa:** Khẳng định máy chủ duy trì giao thức legacy và nạp driver `srv.sys` để xử lý các gói tin này.
- **Ranh giới kết luận:** Hỗ trợ SMBv1 là điều kiện cần về giao thức, nhưng chưa đủ cơ sở để khẳng định hệ thống tồn tại lỗ hổng MS17-010. Một máy chủ Windows đã cập nhật bản vá vẫn có thể bật SMBv1 để phục vụ tương thích nghiệp vụ mà vẫn an toàn trước lỗi xử lý bộ nhớ.

### 1.4.3. Xác định dấu hiệu lỗ hổng

Mức 3 thu thập các phản hồi kỹ thuật để nhận diện dấu hiệu driver `srv.sys` chưa được cập nhật bản vá an ninh:

- **Phản hồi dịch vụ:** Trạm kiểm thử gửi gói tin giao dịch thăm dò an toàn qua giao diện SMB:
  - *Dấu hiệu chưa vá:* Máy chủ phản hồi mã trạng thái `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`), phản ánh việc nhánh mã xử lý cũ đang vận hành.
  - *Dấu hiệu không bộc lộ lỗ hổng:* Máy chủ phản hồi mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc từ chối xử lý yêu cầu thăm dò.
- **Ý nghĩa:** Cung cấp chỉ báo kỹ thuật về khả năng hệ thống đang thiếu bản cập nhật an ninh tương ứng.
- **Ranh giới kết luận:** Dấu hiệu ở Mức 3 mới dừng ở mức suy đoán có căn cứ từ một yêu cầu thăm dò, không phải là bằng chứng khẳng định việc khai thác chắc chắn thành công. Kết quả này còn chịu ảnh hưởng bởi cấu hình kiểm soát truy cập của máy chủ.

### 1.4.4. Xác minh lỗ hổng

Mức 4 đại diện cho bước kiểm chứng sâu hơn về khả năng tác động thực tế của lỗ hổng trong phạm vi thử nghiệm được kiểm soát:

- **Phương pháp kiểm chứng:** Kích hoạt mô-đun kiểm chứng để đánh giá phản ứng thực tế của máy chủ mục tiêu trước yêu cầu can thiệp. Kết quả được phân định theo ba trạng thái:
  - *Xác minh thành công:* Thiết lập được quyền điều khiển tương tác trên máy chủ mục tiêu, chứng minh lỗ hổng có thể bị lợi dụng để thực thi mã từ xa.
  - *Không xác minh được:* Quá trình can thiệp bị từ chối, kết nối bị đóng hoặc hệ thống không phản hồi, cho thấy điều kiện mục tiêu không phù hợp để thực hiện tác động.
  - *Hệ thống mất ổn định:* Máy chủ bị treo hoặc phát sinh lỗi màn hình xanh (BSOD). Hiện tượng này chứng minh hệ thống bị ảnh hưởng về tính sẵn sàng, nhưng không được coi là xác minh thực thi mã thành công.
- **Ý nghĩa:** Cung cấp cơ sở thực nghiệm rõ ràng nhất để phân biệt giữa việc chỉ tồn tại dấu hiệu và khả năng tác động thực tế.
- **Ranh giới kết luận:** Thao tác ở Mức 4 có tính xâm nhập cao, chỉ được triển khai trong phạm vi môi trường thử nghiệm có kiểm soát chặt chẽ.

### 1.4.5. Giới hạn của phương pháp xác minh

Khi đánh giá kết quả, cần lưu ý một số giới hạn kỹ thuật sau:

- **Ảnh hưởng của tường lửa:** Tường lửa mạng hoặc tường lửa cục bộ nếu chặn cổng hoặc lọc gói tin sẽ làm xuất hiện trạng thái `Filtered`. Trạng thái này chỉ phản ánh đường truyền bị chặn từ góc nhìn của trạm kiểm thử, không phản ánh cấu hình an ninh nội tại của máy chủ.
- **Chính sách kiểm soát truy cập:** Khi máy chủ áp dụng chính sách hạn chế kết nối nặc danh (Null Session) vào tài nguyên `IPC$`, các kịch bản thăm dò ở Mức 3 có thể không nhận được mã phản hồi mong muốn. Tình huống này dễ dẫn đến nguy cơ âm tính giả dù hệ điều hành mục tiêu chưa được cập nhật bản vá.
- **Khác biệt giữa các phiên bản hệ điều hành:** Cơ chế quản lý bộ nhớ nhân giữa các thế hệ Windows có sự khác biệt rõ rệt. Một kỹ thuật kiểm chứng có tác động trên phiên bản này có thể chỉ gây lỗi dừng hoặc không hoạt động trên phiên bản khác.
- **Giới hạn của việc quan sát từ bên ngoài (Black-box):** Mọi phép đo từ xa chỉ ghi nhận phản hồi trên đường truyền mạng. Để có kết luận chính xác, kết quả kiểm tra từ xa nên được đối chiếu với trạng thái nội tại của máy chủ (White-box), bao gồm danh mục bản vá KB đã cài đặt và trạng thái kích hoạt thực tế của dịch vụ SMBv1.

Khung tiêu chí bốn mức và các giới hạn kỹ thuật nêu trên là căn cứ phương pháp luận trực tiếp để đồ án xây dựng mô hình thử nghiệm trong Chương 2, đồng thời định hình các kịch bản đo đạc, kiểm chứng và phân tích kết quả đối chứng trong Chương 3.
