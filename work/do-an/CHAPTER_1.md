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

Vào tháng 03 năm 2017, Microsoft phát hành bản tin an ninh MS17-010 nhằm khắc phục một nhóm gồm sáu lỗ hổng bảo mật liên quan đến cách thức thành phần SMBv1 Server trên hệ điều hành Windows tiếp nhận và xử lý các yêu cầu được chế tạo đặc biệt. Nhóm lỗ hổng này bao gồm năm lỗ hổng thực thi mã từ xa (Remote Code Execution - RCE) và một lỗ hổng tiết lộ thông tin (Information Disclosure). Đây là bản tin an ninh tổng hợp bao trùm nhiều vấn đề kỹ thuật khác nhau, không phải là một lỗi đơn lẻ.

Khi thành phần máy chủ xử lý dữ liệu mạng trong không gian nhân (Kernel Mode), các thiếu sót trong quản lý bộ nhớ tại trình điều khiển `srv.sys` có thể ảnh hưởng trực tiếp đến tính ổn định hoặc sự an toàn của toàn bộ hệ điều hành. Bản tin an ninh này áp dụng cho nhiều phiên bản hệ điều hành Windows còn được hỗ trợ tại thời điểm công bố.

Trong phạm vi đề cương và mục tiêu nghiên cứu của đồ án, CVE-2017-0144 được lựa chọn làm đối tượng phân tích trọng tâm nhằm làm rõ cơ chế phát sinh lỗi trong dịch vụ SMBv1, đồng thời phục vụ việc xây dựng quy trình kiểm thử và đối chứng phòng thủ có kiểm soát.

### 1.2.2. Các CVE liên quan

Bản tin MS17-010 xử lý sáu mã lỗ hổng bảo mật (Common Vulnerabilities and Exposures - CVE) được phân định theo loại tác động kỹ thuật:

- **CVE-2017-0143:** Lỗ hổng thực thi mã từ xa (Remote Code Execution - RCE) trong thành phần SMBv1 Server.
- **CVE-2017-0144:** Lỗ hổng thực thi mã từ xa (Remote Code Execution - RCE) liên quan đến việc xử lý dữ liệu thuộc tính tệp mở rộng (FEA) trong SMBv1.
- **CVE-2017-0145:** Lỗ hổng thực thi mã từ xa (Remote Code Execution - RCE) trong thành phần SMBv1 Server.
- **CVE-2017-0146:** Lỗ hổng thực thi mã từ xa (Remote Code Execution - RCE) trong thành phần SMBv1 Server.
- **CVE-2017-0147:** Lỗ hổng tiết lộ thông tin (Information Disclosure) cho phép rò rỉ dữ liệu từ bộ nhớ phía máy chủ.
- **CVE-2017-0148:** Lỗ hổng thực thi mã từ xa (Remote Code Execution - RCE) trong thành phần SMBv1 Server.

Sự phân định này cho thấy bản tin MS17-010 bao gồm năm lỗ hổng thực thi mã từ xa và một lỗ hổng tiết lộ thông tin với các điều kiện kỹ thuật khác nhau, không phải là một lỗi đơn nhất. Trong danh mục trên, đồ án lựa chọn CVE-2017-0144 làm đối tượng phân tích trọng tâm để nghiên cứu sâu về cơ chế quản lý bộ nhớ và điều kiện tác động trong môi trường lab.

### 1.2.3. Cơ chế xử lý yêu cầu SMBv1 dẫn đến lỗ hổng

Lỗ hổng CVE-2017-0144 phát sinh trong quá trình trình điều khiển `srv.sys` của Windows tiếp nhận và xử lý cấu trúc danh sách thuộc tính tệp mở rộng (Full Extended Attributes - FEA) được gửi qua các gói tin giao dịch của SMBv1.

Về mặt nguyên lý, khi nhận yêu cầu chứa danh sách FEA từ trạm khách, trình điều khiển phía máy chủ phải thực hiện chuyển đổi định dạng dữ liệu sang cấu trúc bộ nhớ nội bộ của hệ điều hành. Quá trình này bao gồm khâu tính toán dung lượng bộ nhớ cần thiết, sau đó cấp phát vùng đệm trong bộ nhớ nhân (Kernel Pool) và sao chép các phần tử dữ liệu vào vùng đệm tương ứng.

Lỗi an ninh xuất hiện từ sự sai lệch trong việc kiểm soát và chuyển đổi kích thước dữ liệu: dung lượng bộ nhớ được tính toán và cấp phát ban đầu nhỏ hơn lượng dữ liệu thực tế cần sao chép. Hậu quả là thao tác ghi dữ liệu vượt ra ngoài phạm vi ranh giới của vùng đệm đã cấp phát trong không gian nhân (Kernel Pool Overflow).

Do sự cố xảy ra trực tiếp trong không gian nhân của hệ điều hành, việc ghi vượt biên bộ nhớ này có thể làm hư hại cấu trúc dữ liệu liền kề, dẫn đến tình trạng mất ổn định hoặc phát sinh lỗi dừng hệ thống. Trong điều kiện kiểm thử phù hợp, sự sai lệch bố cục bộ nhớ này có thể bị lợi dụng để tạo tiền đề cho việc thực thi mã lệnh từ xa.

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

Như vậy, mở cổng mạng không đồng nghĩa với việc hỗ trợ SMBv1, hỗ trợ SMBv1 không đồng nghĩa với hệ thống chưa vá, và sự tồn tại của lỗ hổng cũng không bảo đảm việc can thiệp khai thác sẽ thành công.

### 1.2.5. Tác động của lỗ hổng

Tác động của lỗ hổng CVE-2017-0144 thuộc nhóm MS17-010 được xem xét qua ba mục tiêu an toàn thông tin cơ bản:

- **Tính bảo mật (Confidentiality):** Nếu kỹ thuật can thiệp đạt được quyền thực thi mã ở mức đặc quyền cao, dữ liệu lưu trữ trên máy chủ, thông tin cấu hình và các phiên giao tiếp đều đứng trước nguy cơ bị truy cập trái phép.
- **Tính toàn vẹn (Integrity):** Trong phạm vi quyền hạn đạt được, dữ liệu hoặc cấu hình dịch vụ trên hệ thống có thể bị chỉnh sửa hoặc can thiệp trái phép.
- **Tính sẵn sàng (Availability):** Do tác động vào không gian nhân, việc xử lý dữ liệu bất thường hoặc thao tác bộ nhớ không tương thích có thể gây mất ổn định hoặc lỗi dừng hệ thống. Ngoài ra, việc dịch vụ SMB ngừng phản hồi cũng làm gián đoạn khả năng chia sẻ tài nguyên mạng.

Khác với các lỗi đòi hỏi sự tương tác của người dùng, yêu cầu khai thác lỗ hổng này có thể truyền tải trực tiếp qua gói tin mạng, khiến nguy cơ ảnh hưởng diện rộng trở nên rõ rệt nếu dịch vụ SMBv1 được mở ra môi trường không tin cậy.

### 1.2.6. Mối liên hệ với các cuộc tấn công thực tế

Tác động thực tế của nhóm lỗ hổng MS17-010 đã được minh họa qua các sự cố an ninh mạng diện rộng trong năm 2017:

- **Chiến dịch mã độc WannaCry (Tháng 05/2017):** Khai thác lỗ hổng SMBv1 chưa vá để tự động lây nhiễm qua cổng TCP 445 trong mạng nội bộ và trên Internet nhằm phát tán mã độc tống tiền.
- **Chiến dịch mã độc NotPetya (Tháng 06/2017):** Tận dụng kỹ thuật can thiệp vào SMBv1 để lây lan nhanh chóng giữa các máy tính trong cùng hạ tầng mạng doanh nghiệp, gây gián đoạn nghiêm trọng hoạt động của nhiều tổ chức.

Các sự cố này minh chứng rằng việc duy trì dịch vụ SMBv1 chưa được cập nhật bản vá an ninh có thể dẫn đến nguy cơ mất an toàn nghiêm trọng cho toàn bộ hệ thống mạng. Thực tế đó khẳng định tính cần thiết của việc xây dựng phương pháp kiểm thử, đo đạc và phân loại trạng thái an ninh của dịch vụ SMB một cách có kiểm soát.

---

## 1.3. Công cụ phục vụ kiểm thử

### 1.3.1. Kali Linux

Trong đồ án này, Kali Linux được sử dụng làm trạm kiểm thử (Testing Workstation) chuyên dụng. Hệ điều hành cung cấp môi trường tập trung với các tiện ích mạng, thư viện và công cụ kiểm định an ninh để tương tác với máy chủ Windows mục tiêu.

Vai trò của trạm kiểm thử là khởi tạo các yêu cầu thăm dò, quản lý cấu hình kết nối mạng và ghi nhận nhật ký của quá trình đánh giá. Bản thân Kali Linux chỉ đóng vai trò nền tảng điều khiển; sự hiện diện của trạm kiểm thử không phải là bằng chứng về trạng thái an ninh hay lỗ hổng của máy chủ mục tiêu.

### 1.3.2. Nmap

Nmap (Network Mapper) được sử dụng ở bước sàng lọc ban đầu nhằm kiểm tra khả năng tiếp cận dịch vụ qua hai cổng mạng TCP 139 và TCP 445.

Dữ liệu do Nmap cung cấp phản ánh trạng thái cổng ở tầng giao vận:
- `Open`: Cổng mạng có tiến trình lắng nghe và tiếp nhận kết nối TCP (phản hồi gói tin TCP SYN-ACK trước yêu cầu SYN từ trạm kiểm thử).
- `Closed`: Cổng mạng phản hồi gói tin RST, cho thấy không có dịch vụ lắng nghe tiếp nhận kết nối.
- `Filtered`: Gói tin thăm dò không nhận được phản hồi hoặc bị lọc bởi chính sách mạng/tường lửa.

Tùy chọn nhận diện dịch vụ (`-sV`) của Nmap hỗ trợ ghi nhận tên ứng dụng sơ bộ như `microsoft-ds` hoặc `netbios-ssn`. Tuy nhiên, kết quả từ Nmap chỉ xác nhận điểm lắng nghe TCP có thể tiếp cận được từ trạm kiểm thử. Trạng thái cổng 445 `Open` không chứng minh máy chủ hỗ trợ SMBv1, không chứng minh sự tồn tại của lỗ hổng MS17-010 và không đồng nghĩa với việc có thể khai thác được.

### 1.3.3. Nmap Scripting Engine

Nmap Scripting Engine (NSE) mở rộng khả năng kiểm tra lên tầng ứng dụng thông qua các kịch bản viết bằng ngôn ngữ Lua. Hai kịch bản chuyên biệt được sử dụng gồm:

- **Kịch bản `smb-protocols.nse`:** Gửi yêu cầu thương lượng (`Negotiate Protocol Request`) chứa danh sách dialect để ghi nhận phản hồi từ máy chủ, cung cấp bằng chứng về việc hệ thống có chấp thuận giao thức SMBv1 (`NT LM 0.12`) hay không.
- **Kịch bản `smb-vuln-ms17-010.nse`:** Thăm dò chỉ báo kỹ thuật liên quan đến trạng thái MS17-010 bằng cách gửi gói tin giao dịch kiểm tra logic qua giao diện SMB.

Kịch bản đánh giá dựa trên mã trạng thái phản hồi từ máy chủ:
- Khi nhận mã lỗi `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`), kịch bản sử dụng mã phản hồi này làm dấu hiệu cho thấy mục tiêu có khả năng chưa được cập nhật bản vá và đưa ra thông báo cảnh báo. Mã phản hồi này không được coi là bằng chứng quan sát trực tiếp đường thực thi bên trong nhân hệ điều hành.
- Khi nhận mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc yêu cầu bị từ chối, kết quả cho thấy mục tiêu không bộc lộ chỉ báo nghi ngờ theo logic kiểm tra của kịch bản. Tuy nhiên, phản hồi từ chối này không đủ cơ sở để kết luận hệ thống đã được vá an toàn, do việc xử lý gói tin còn phụ thuộc vào chính sách phân quyền và cấu hình phiên kết nối.

NSE thực hiện phép thăm dò logic mà không kích hoạt chuỗi khai thác hoàn chỉnh. Do đó, kết quả từ NSE có giá trị như một chỉ báo kỹ thuật ở tầng ứng dụng, không phải bằng chứng khẳng định việc can thiệp sâu sẽ thành công trên thực tế.

### 1.3.4. Metasploit Framework

Metasploit Framework được sử dụng nhằm mục đích đối chiếu triển khai kiểm thử và thực hiện bước xác minh sâu hơn khi điều kiện thử nghiệm cho phép:

- **Mô-đun phụ trợ (Auxiliary Module):** Mô-đun `auxiliary/scanner/smb/smb_ms17_010` thực thi cùng phương pháp thăm dò logic như kịch bản NSE (dựa trên tương tác qua tài nguyên `IPC$` và mã lỗi phản hồi). Mô-đun này hỗ trợ đối chiếu khâu phân tích cú pháp giữa hai bộ công cụ, nhưng không tạo thành hai nguồn tín hiệu độc lập về trạng thái an ninh của máy chủ.
- **Mô-đun kiểm chứng tác động (Exploit Module):** Mô-đun `exploit/windows/smb/ms17_010_eternalblue` được sử dụng trong môi trường lab có kiểm soát để xác minh khả năng thực thi mã từ xa khi các chỉ báo nghi ngờ đã được ghi nhận.

Khác với các phép thăm dò logic, mô-đun can thiệp sâu tác động trực tiếp vào vùng nhớ của hệ điều hành. Kết quả quan sát (thiết lập phiên tương tác, can thiệp bị từ chối hoặc máy chủ phát sinh lỗi dừng) cần được đối chiếu thận trọng với phiên bản hệ điều hành và cấu hình dịch vụ mục tiêu.

### 1.3.5. Vai trò của các công cụ trong quy trình kiểm thử

Các công cụ được bố trí theo tiến trình kiểm thử tuần tự nhằm tổ chức bằng chứng theo từng mức độ quan sát:

- **Trạm kiểm thử Kali Linux:** Cung cấp môi trường điều hành để thực thi công cụ và lưu trữ nhật ký đo đạc.
- **Nmap:** Xác định khả năng tiếp cận dịch vụ qua trạng thái mở cổng ở tầng giao vận.
- **Nmap Scripting Engine:** Xác định việc chấp thuận dialect SMBv1 và thu thập chỉ báo kỹ thuật nghi ngờ ở tầng ứng dụng.
- **Metasploit Framework:** Đối chiếu kết quả thăm dò cú pháp và thực hiện bước xác minh tác động chuyên sâu trong điều kiện thử nghiệm được kiểm soát.

Tiến trình tuần tự này giúp liên kết dữ liệu thu thập từ diện rộng đến chuyên sâu, phân định rõ ràng giữa việc cổng mạng có thể tiếp cận, giao thức được hỗ trợ, dấu hiệu nghi ngờ và tác động thực tế trên hệ thống.

---

## 1.4. Tiêu chí xác minh trạng thái SMB và MS17-010

### 1.4.1. Phát hiện dịch vụ SMB

Mức 1 xác định khả năng tiếp cận cổng thường dùng cho dịch vụ SMB trên đường truyền mạng giữa trạm kiểm thử và máy chủ mục tiêu:

- **Dấu hiệu quan sát:** Trạm kiểm thử gửi gói tin TCP SYN tới cổng TCP 445 hoặc TCP 139. Trạng thái cổng được ghi nhận là `Open` khi máy chủ phản hồi gói tin TCP SYN-ACK.
- **Ý nghĩa kỹ thuật:** Chứng minh có điểm kết nối TCP đang lắng nghe trên cổng thường dùng cho SMB và trạm kiểm thử có thể tiếp cận được cổng này qua hạ tầng mạng.
- **Ranh giới kết luận:** Trạng thái mở cổng 445 hoặc 139 chỉ phản ánh khả năng tiếp cận ở tầng giao vận, chưa chứng minh dịch vụ SMB ở tầng ứng dụng đang hoạt động bình thường và hoàn toàn không đồng nghĩa với việc hệ thống tồn tại lỗ hổng bảo mật.

### 1.4.2. Nhận diện SMBv1

Mức 2 kiểm tra xem dịch vụ SMB của máy chủ có chấp thuận giao tiếp bằng phiên bản cũ SMBv1 hay không:

- **Tiêu chí giao thức:** Trạm kiểm thử gửi gói tin `Negotiate Protocol Request` chứa danh sách các dialect. Hệ thống được xác nhận có hỗ trợ SMBv1 khi phản hồi bằng gói tin lựa chọn dialect `NT LM 0.12`.
- **Ý nghĩa kỹ thuật:** Khẳng định máy chủ chấp thuận giao tiếp bằng giao thức cũ SMBv1 và sẵn sàng tiếp nhận các yêu cầu thuộc phiên bản này.
- **Ranh giới kết luận:** Việc chấp thuận SMBv1 là điều kiện cần về mặt giao thức, nhưng không quan sát trực tiếp được trạng thái cập nhật bản vá nội tại của trình điều khiển nhân và chưa đủ cơ sở để khẳng định hệ thống có lỗ hổng MS17-010. Một máy chủ Windows đã cập nhật bản vá an ninh đầy đủ vẫn có thể kích hoạt SMBv1 để duy trì tính tương thích với các ứng dụng cũ.

### 1.4.3. Xác định dấu hiệu lỗ hổng

Mức 3 thu thập chỉ báo kỹ thuật liên quan đến trạng thái MS17-010 thông qua phản hồi của dịch vụ SMB:

- **Phản hồi dịch vụ:** Trạm kiểm thử gửi gói tin giao dịch thăm dò không thực hiện chuỗi khai thác hoàn chỉnh qua giao diện SMB (`IPC$`):
  - *Chỉ báo nghi ngờ:* Máy chủ phản hồi mã trạng thái `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`). Mã phản hồi này được kịch bản sử dụng làm dấu hiệu cho thấy hệ thống có khả năng chưa được cập nhật bản vá MS17-010.
  - *Chỉ báo không bộc lộ lỗ hổng:* Máy chủ phản hồi mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc từ chối xử lý yêu cầu thăm dò.
- **Ý nghĩa kỹ thuật:** Cung cấp chỉ báo về sự sai lệch logic phản hồi của hệ thống trước một yêu cầu giao dịch bất thường.
- **Ranh giới kết luận:** Dấu hiệu ở Mức 3 dừng lại ở mức chỉ báo kỹ thuật từ một gói tin thăm dò, không phải bằng chứng bảo đảm việc can thiệp khai thác sẽ thành công. Mặt khác, phản hồi từ chối hoặc không bộc lộ chỉ báo nghi ngờ cũng không chứng minh hệ thống đã an toàn hoặc đã cài bản vá, do kết quả này còn chịu tác động từ chính sách hạn chế kết nối nặc danh hoặc cấu hình dịch vụ.

### 1.4.4. Xác minh lỗ hổng

Mức 4 đại diện cho bước kiểm chứng sâu hơn về khả năng tác động thực tế trong phạm vi môi trường thử nghiệm có kiểm soát:

- **Phương pháp kiểm chứng:** Thực thi kỹ thuật can thiệp để đánh giá phản ứng thực tế của máy chủ mục tiêu. Kết quả được phân định theo ba trạng thái:
  - *Xác minh đạt quyền tương tác:* Kỹ thuật kiểm chứng đạt được quyền thực thi mã hoặc thiết lập phiên điều khiển tương tác trên máy chủ mục tiêu trong điều kiện thử nghiệm. Kết quả này ghi nhận quyền hạn của phiên ở tầng hệ điều hành, không đồng nhất với việc quan sát trực tiếp diễn biến bên trong bộ nhớ nhân từ xa.
  - *Không xác minh được:* Quá trình can thiệp bị từ chối, kết nối bị đóng hoặc hệ thống không phản hồi. Hiện tượng này chỉ phản ánh kỹ thuật kiểm chứng hiện tại chưa phù hợp với mục tiêu, không tự động chứng minh máy chủ đã an toàn hoặc miễn nhiễm với lỗ hổng.
  - *Hệ thống mất ổn định:* Máy chủ bị treo hoặc phát sinh lỗi dừng hệ thống (BSOD). Hiện tượng này phản ánh sự mất ổn định của hệ điều hành trong quá trình kiểm chứng và là bằng chứng tác động đến tính sẵn sàng của mục tiêu trong lượt thử; hiện tượng này không tự xác định nguyên nhân gốc rễ cụ thể và không được coi là xác minh thực thi mã thành công.
- **Ý nghĩa kỹ thuật:** Cung cấp cơ sở thực nghiệm để phân biệt giữa việc chỉ xuất hiện chỉ báo nghi ngờ và khả năng phát sinh tác động thực tế trên hệ thống.
- **Ranh giới kết luận:** Thao tác ở Mức 4 có tính can thiệp cao, chỉ được triển khai trong phạm vi môi trường lab thử nghiệm được kiểm soát chặt chẽ nhằm tránh rủi ro ngoài ý muốn.

### 1.4.5. Giới hạn của phương pháp xác minh

Khi đánh giá kết quả, cần phân định các giới hạn kỹ thuật giữa quan sát mạng từ xa và trạng thái nội tại của hệ thống:

- **Ảnh hưởng của tường lửa và chính sách mạng:** Tường lửa mạng hoặc tường lửa cục bộ nếu chặn cổng hoặc lọc gói tin sẽ làm xuất hiện trạng thái `Filtered`. Trạng thái này chỉ phản ánh đường truyền bị chặn từ góc nhìn của trạm kiểm thử, không phản ánh cấu hình hay mức độ an toàn nội tại của máy chủ.
- **Chính sách kiểm soát truy cập:** Khi máy chủ áp dụng chính sách hạn chế kết nối nặc danh (Null Session) vào tài nguyên `IPC$`, các kịch bản thăm dò ở Mức 3 có thể không nhận được mã phản hồi mong muốn. Tình huống này có thể dẫn đến nhận định âm tính giả dù hệ điều hành mục tiêu chưa được cập nhật bản vá.
- **Khác biệt giữa các phiên bản hệ điều hành:** Cơ chế quản lý bộ nhớ nhân giữa các thế hệ Windows có sự khác biệt. Một kỹ thuật can thiệp có tác động trên phiên bản này có thể chỉ gây lỗi dừng hoặc không hoạt động trên phiên bản khác.
- **Giới hạn của việc quan sát từ bên ngoài (Black-box):** Mọi phép đo từ xa chỉ ghi nhận các biểu hiện trên đường truyền mạng. Để có kết luận toàn diện, nguyên tắc đối chứng đòi hỏi kết quả kiểm tra từ xa cần được đối chiếu với trạng thái nội tại của máy chủ (White-box), bao gồm danh mục bản vá an ninh đã cài đặt và cấu hình kích hoạt thực tế của dịch vụ SMBv1.

Khung tiêu chí bốn mức và các giới hạn kỹ thuật nêu trên là căn cứ phương pháp luận trực tiếp để đồ án xây dựng mô hình thử nghiệm trong Chương 2, đồng thời định hình các kịch bản đo đạc, kiểm chứng và phân tích kết quả đối chứng trong Chương 3.
