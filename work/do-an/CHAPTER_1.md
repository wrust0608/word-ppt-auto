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

Vào tháng 03 năm 2017, Microsoft phát hành bản tin an ninh định kỳ MS17-010 nhằm xử lý một nhóm gồm 6 lỗ hổng bảo mật nghiêm trọng trong driver xử lý giao thức SMBv1 (`srv.sys`) của hệ điều hành Windows. Đây là bản tin an ninh tổng hợp bao trùm nhiều lỗ hổng khác nhau, chứ không đại diện cho một lỗi kỹ thuật đơn lẻ.

Bản chất của các lỗ hổng trong MS17-010 bắt nguồn từ việc giao thức SMBv1 được thiết kế từ giai đoạn đầu của mạng máy tính cá nhân, khi các yêu cầu kiểm soát biên dữ liệu và xác thực chặt chẽ chưa được đặt ra đầy đủ. Do driver `srv.sys` vận hành trực tiếp trong không gian nhân (Kernel Mode) nhằm tối ưu tốc độ xử lý I/O mạng, bất kỳ sai sót nào trong việc cấp phát và quản lý bộ nhớ đệm tại đây cũng tạo ra nguy cơ đe dọa trực tiếp đến toàn bộ hệ điều hành.

Phạm vi ảnh hưởng của MS17-010 bao phủ hầu hết các thế hệ Windows lưu hành tại thời điểm công bố, bao gồm Windows Vista, Windows 7, Windows 8.1, Windows 10 (các bản dựng đầu) cùng các hệ điều hành máy chủ Windows Server 2008, 2012 và 2016. Do mức độ nguy hiểm đặc biệt cao, Microsoft thậm chí đã phải phát hành bản vá ngoại lệ cho cả những phiên bản đã kết thúc vòng đời hỗ trợ chính thức như Windows XP và Windows Server 2003.

Trong phạm vi đồ án, nhóm em tập trung nghiên cứu lỗ hổng thực thi mã từ xa không cần xác thực trong nhóm này để làm rõ bản chất rủi ro của dịch vụ SMBv1, đồng thời xây dựng quy trình kiểm thử và đối chứng phòng thủ có kiểm soát.

### 1.2.2. Các CVE liên quan

Bản tin bảo mật MS17-010 khắc phục 6 mã định danh lỗ hổng an ninh (Common Vulnerabilities and Exposures - CVE), gồm 5 lỗ hổng thực thi mã từ xa (Remote Code Execution - RCE) và 1 lỗ hổng làm lộ thông tin (Information Disclosure):

- **CVE-2017-0143 (RCE):** Lỗ hổng phát sinh từ việc xử lý sai các thông điệp giao dịch phụ (Transaction2) trong SMBv1, liên quan trực tiếp đến các công cụ khai thác mang tên EternalSynergy và EternalRomance.
- **CVE-2017-0144 (RCE):** Lỗi tràn vùng đệm bộ nhớ nhân trong quá trình chuyển đổi danh sách thuộc tính tệp mở rộng (FEA) của SMBv1. Đây là lỗ hổng cốt lõi bị vũ khí hóa bởi mã khai thác EternalBlue.
- **CVE-2017-0145 (RCE):** Lỗi trong cách SMBv1 xử lý tham số bộ nhớ khi nhận các yêu cầu giao dịch bất thường, liên quan đến mã khai thác EternalRomance.
- **CVE-2017-0146 (RCE):** Lỗi giải phóng và tái sử dụng con trỏ bộ nhớ không an toàn trong driver `srv.sys`, liên quan đến công cụ EternalChampion.
- **CVE-2017-0147 (Information Disclosure):** Lỗ hổng cho phép rò rỉ dữ liệu từ không gian bộ nhớ nhân về phía client thông qua các thông điệp phản hồi SMBv1 không được xóa trắng dữ liệu trước khi gửi.
- **CVE-2017-0148 (RCE):** Lỗi kiểm tra tính hợp lệ của tham số trong các gói tin giao dịch SMB liên tiếp, cho phép can thiệp vào luồng xử lý của hệ thống.

Việc phân biệt các mã CVE giúp làm rõ rằng MS17-010 không đồng nhất hoàn toàn với chỉ một lỗ hổng. Trong số này, CVE-2017-0144 là lỗ hổng nguy hiểm nhất do có khả năng bị khai thác từ xa qua mạng mà không đòi hỏi tài khoản người dùng, đồng thời là đối tượng trung tâm được nhóm em phân tích kỹ thuật và thẩm định trong môi trường thực nghiệm.

### 1.2.3. Cơ chế xử lý yêu cầu SMBv1 dẫn đến lỗ hổng

Lỗ hổng CVE-2017-0144 phát sinh trong quá trình driver `srv.sys` xử lý các thuộc tính tệp mở rộng (Full Extended Attributes - FEA). Đây là cấu trúc dữ liệu được SMBv1 hỗ trợ nhằm duy trì tính tương thích ngược với hệ điều hành OS/2 cũ.

Khi client gửi một gói tin yêu cầu thuộc nhóm giao dịch (cụ thể là lệnh `SMB_COM_TRANSACTION2` với hàm phụ `SMB2_TRANS2_SET_PATH_INFORMATION`), gói tin này mang theo một danh sách các thuộc tính FEA định dạng OS/2 (gọi là `FEA_LIST`). Để Windows hiểu và áp dụng được các thuộc tính này lên hệ thống tệp NTFS, driver `srv.sys` phải chuyển đổi danh sách trên sang định dạng nội bộ của Windows NT (`FILE_FULL_EA_INFORMATION`). Quá trình này diễn ra qua hai hàm nội bộ liên tiếp trong nhân hệ điều hành:

- **Khâu tính toán kích thước vùng đệm (`SrvOs2FeaListSizeToNt`):** Hàm này duyệt qua từng phần tử trong danh sách `FEA_LIST` để tính toán tổng số byte cần thiết nhằm cấp phát một vùng nhớ trong bộ nhớ nhân không phân trang (Non-Paged Pool). Tuy nhiên, biến lưu trữ kích thước đầu ra của hàm này được khai báo bằng kiểu số nguyên không dấu 16-bit (WORD / `unsigned short`), có giá trị tối đa là 65.535 byte (0xFFFF). Khi kẻ tấn công gửi một danh sách FEA được cố tình chế tạo với kích thước thực tế lớn hơn 65.535 byte, hiện tượng cắt ngắn số nguyên (Integer Truncation) sẽ xảy ra. Ví dụ, một danh sách có tổng kích thước thực tế là 0x10040 byte (65.600 byte) khi bị ép kiểu về 16-bit sẽ chỉ còn lại giá trị 0x0040 (64 byte).
- **Khâu cấp phát và sao chép dữ liệu (`SrvOs2FeaToNt`):** Dựa trên kết quả tính toán sai lệch của bước trước, hệ điều hành chỉ cấp phát một vùng đệm nhỏ có kích thước 64 byte trong Non-Paged Pool. Sau đó, hàm `SrvOs2FeaToNt` thực hiện sao chép nội dung từng thuộc tính FEA vào vùng đệm này. Trong quá trình duyệt và sao chép dữ liệu, hàm lại sử dụng kích thước thực tế của từng phần tử FEA mà không kiểm tra lại biên tổng của vùng đệm đã cấp phát. Do đó, dữ liệu sao chép bị tràn ra ngoài phạm vi 64 byte được chỉ định, gây ra hiện tượng tràn vùng đệm nhân (Kernel Pool Overflow).

Dữ liệu tràn sẽ ghi đè lên các cấu trúc điều khiển bộ nhớ liền kề trong Non-Paged Pool. Trong các công cụ khai thác vũ khí hóa như EternalBlue, kẻ tấn công kết hợp lỗi này với kỹ thuật dàn xếp bộ nhớ nhân (Kernel Pool Grooming). Bằng cách gửi liên tục các gói tin mạng để sắp đặt vị trí các khối bộ đệm của driver mạng `srvnet.sys` nằm ngay phía sau vùng đệm bị tràn, mã khai thác có thể ghi đè chính xác lên các con trỏ hàm tiếp nhận dữ liệu. Khi driver mạng gọi con trỏ hàm này để xử lý gói tin tiếp theo, luồng thực thi của CPU sẽ bị điều hướng sang đoạn mã tùy ý chạy dưới đặc quyền tối cao của nhân hệ điều hành (`NT AUTHORITY\SYSTEM`).

Do lỗi xảy ra trực tiếp trong vùng nhớ Non-Paged Pool của nhân, nếu quá trình dàn xếp bộ nhớ gặp sai lệch, hệ điều hành sẽ phát sinh lỗi dừng và sập màn hình xanh (BSOD). Điều này giải thích vì sao các thao tác can thiệp vào lỗ hổng luôn đi kèm rủi ro lớn đối với tính sẵn sàng của máy chủ.

### 1.2.4. Điều kiện ảnh hưởng và điều kiện khai thác

Trong đánh giá an ninh, việc phân định rạch ròi giữa điều kiện để một hệ thống tồn tại lỗ hổng và điều kiện để lỗ hổng đó có thể bị khai thác thực tế là yêu cầu bắt buộc:

**Điều kiện ảnh hưởng (Hệ thống có tồn tại lỗ hổng hay không):**

- Hệ điều hành đang chạy là phiên bản Windows nằm trong diện bị lỗi (chẳng hạn Windows 7 SP1 x64, Windows Server 2008 R2...).
- Tính năng SMBv1 đang được bật và driver `srv.sys` đang nạp trong nhân để xử lý các yêu cầu mạng.
- Hệ điều hành chưa được cài đặt bản cập nhật an ninh MS17-010 (ví dụ gói cập nhật KB4012212 hoặc KB4012215 đối với Windows 7).

**Điều kiện khai thác (Cuộc tấn công có thể thực hiện thành công hay không):**

- Kẻ tấn công có đường truyền mạng thông suốt tới cổng dịch vụ SMB (cổng TCP 445 hoặc TCP 139) của máy chủ mục tiêu.
- Tường lửa mạng hoặc tường lửa cục bộ Windows Firewall không chặn các cổng này và không lọc các gói tin giao dịch SMB bất thường.
- Máy chủ mục tiêu chấp nhận thương lượng dialect SMBv1 (`NT LM 0.12`).
- Máy chủ cho phép thiết lập phiên làm việc (kể cả phiên nặc danh Null Session) để kết nối tới tài nguyên chia sẻ quản trị liên tiến trình `IPC$`.
- Trạng thái phân bổ bộ nhớ nhân của máy chủ đủ ổn định để kỹ thuật dàn xếp Non-Paged Pool hoàn tất mà không kích hoạt lỗi màn hình xanh BSOD.

Từ sự phân định trên, có thể thấy trạng thái mở cổng TCP 445 và bật SMBv1 chỉ là điều kiện cần về mặt kết nối dịch vụ. Một máy tính dù đang mở cổng 445 và bật SMBv1 nhưng đã được cập nhật bản vá KB tương ứng thì driver `srv.sys` đã được sửa đổi để kiểm tra chặt chẽ kích thước FEA, do đó hoàn toàn không thể bị khai thác. Ngược lại, một máy tính tồn tại lỗ hổng nhưng đặt sau tường lửa chặn cổng 445 thì kẻ tấn công từ bên ngoài phân vùng mạng cũng không thể tiếp cận để khai thác.

### 1.2.5. Tác động của lỗ hổng

Tác động của lỗ hổng CVE-2017-0144 thuộc nhóm MS17-010 được xem xét toàn diện qua ba yếu tố bảo đảm an toàn thông tin:

- **Tính bảo mật (Confidentiality):** Mức độ ảnh hưởng là tối đa. Khi mã khai thác thực thi trong không gian nhân với quyền `SYSTEM`, kẻ tấn công có thể đọc toàn bộ dữ liệu lưu trữ trên các ổ đĩa, truy cập trực tiếp vào bộ nhớ của tiến trình xác thực `lsass.exe` để trích xuất mật khẩu dạng văn bản rõ hoặc mã băm NTLM của các tài khoản đăng nhập trên máy.
- **Tính toàn vẹn (Integrity):** Bị can thiệp tuyệt đối. Kẻ tấn công có toàn quyền sửa đổi, xóa bỏ tệp tin hệ thống, thay đổi chính sách bảo mật, cài đặt các phần mềm độc hại hoặc cấy cửa sau (backdoor) chạy ngầm để duy trì quyền kiểm soát lâu dài.
- **Tính sẵn sàng (Availability):** Bị đe dọa nghiêm trọng. Quá trình khai thác bộ nhớ nhân rất dễ dẫn đến lỗi làm sập hệ thống (BSOD) khiến dịch vụ bị gián đoạn tức thì. Ngoài ra, kẻ tấn công có thể cố tình tắt máy, khóa dịch vụ hoặc mã hóa toàn bộ dữ liệu máy chủ để tống tiền.

Đặc điểm khiến CVE-2017-0144 trở nên đặc biệt nguy hiểm là lỗ hổng này không đòi hỏi bất kỳ sự tương tác nào từ phía người dùng (Zero-click) và không yêu cầu cung cấp tài khoản hay mật khẩu hợp lệ trước đó. Đây là đặc tính kỹ thuật biến lỗ hổng thành cửa ngõ lý tưởng cho các cuộc tấn công tự động trên quy mô lớn.

### 1.2.6. Mối liên hệ với các cuộc tấn công thực tế

Nguy cơ kỹ thuật của MS17-010 đã được minh chứng cụ thể thông qua các sự cố an ninh mạng chấn động thế giới xuất hiện vào năm 2017:

- **Chiến dịch mã độc tống tiền WannaCry (Tháng 05/2017):** Mã khai thác EternalBlue bị nhóm tin tặc Shadow Brokers làm rò rỉ vào tháng 04/2017. Chỉ một tháng sau, tác giả của WannaCry đã tích hợp mã khai thác này vào một sâu mạng (worm) tự động. WannaCry quét liên tục các cổng TCP 445 trên Internet và mạng nội bộ, tự động xâm nhập các máy Windows chưa vá và mã hóa toàn bộ dữ liệu để đòi tiền chuộc. Vụ tấn công đã lây nhiễm hàng trăm nghìn máy tính tại hơn 150 quốc gia, làm tê liệt hệ thống của nhiều bệnh viện, ngân hàng và cơ quan công quyền.
- **Chiến dịch mã độc NotPetya (Tháng 06/2017):** NotPetya tiếp tục sử dụng các mã khai thác trong nhóm MS17-010 (kết hợp giữa EternalBlue và EternalRomance) để lây lan với tốc độ cao trong mạng nội bộ của các tập đoàn đa quốc gia. Khác với WannaCry, NotPetya ngụy trang dưới dạng mã độc tống tiền nhưng mục tiêu thực chất là phá hoại: mã độc cố tình ghi đè Master Boot Record (MBR) của ổ cứng, khiến dữ liệu không thể phục hồi và gây thiệt hại kinh tế ước tính hàng tỷ USD.

Các chiến dịch thực tế này phản ánh bài học quản trị sâu sắc: lỗ hổng giao thức kết hợp với sự chậm trễ cập nhật bản vá và việc duy trì SMBv1 có thể biến mạng nội bộ thành môi trường lây nhiễm diện rộng. Nhận thức rõ điều này, nhóm em xác định việc xây dựng phương pháp kiểm tra an toàn và có kiểm soát là yêu cầu cấp thiết để nhận diện và phòng vệ dịch vụ SMB.

---

## 1.3. Công cụ phục vụ kiểm thử

### 1.3.1. Kali Linux

Trong đồ án này, Kali Linux được nhóm em sử dụng làm trạm kiểm thử (Testing Workstation) chuyên dụng. Hệ điều hành cung cấp nền tảng dòng lệnh tập trung, cho phép thực thi đồng bộ các công cụ mạng, quản lý cấu hình giao tiếp và ghi nhận nhật ký (log) chi tiết trong suốt quá trình thử nghiệm.

Tuy nhiên, bản thân Kali Linux chỉ là môi trường vận hành chứ không tự động phát hiện hay phân tích lỗ hổng của mục tiêu. Độ chính xác và tính an toàn của quá trình đánh giá phụ thuộc hoàn toàn vào cách thiết lập từng công cụ cụ thể. Nhóm em cấu hình card mạng ảo của trạm kiểm thử ở chế độ nội bộ cô lập (Host-only Network hoặc Internal Network) nhằm ngăn chặn triệt để nguy cơ các gói tin thăm dò thoát ra hạ tầng mạng bên ngoài.

Với vai trò điểm xuất phát trong chuỗi kiểm tra, Kali Linux là nơi khởi tạo mọi kết nối trinh sát và phân tích lưu lượng đến máy chủ Windows mục tiêu.

### 1.3.2. Nmap

Nhóm em sử dụng Nmap (Network Mapper) cho bước trinh sát mạng ban đầu nhằm xác định các máy chủ đang hoạt động và kiểm tra trạng thái của hai cổng dịch vụ TCP 139 và TCP 445.

Dữ liệu thu được từ Nmap phản ánh khả năng tiếp cận dịch vụ ở tầng giao vận:
- `Open`: Cổng mạng đang có tiến trình lắng nghe và phản hồi gói tin TCP SYN-ACK trước yêu cầu SYN từ trạm kiểm thử.
- `Closed`: Cổng mạng phản hồi gói tin RST, cho thấy không có dịch vụ nào đang tiếp nhận kết nối.
- `Filtered`: Gói tin thăm dò bị hủy bỏ hoặc nhận thông báo ICMP Unreachable do tường lửa ngăn chặn.

Bên cạnh đó, tùy chọn `-sV` giúp định danh sơ bộ tên dịch vụ ứng dụng như `microsoft-ds` hoặc `netbios-ssn`.

Mặc dù vậy, kết quả từ Nmap chỉ dừng lại ở việc xác nhận cổng dịch vụ có mở hay không từ góc nhìn mạng. Trạng thái cổng 445 `Open` không đồng nghĩa với việc máy chủ hỗ trợ SMBv1 hay tồn tại lỗ hổng MS17-010. Do đó, Nmap đảm nhiệm vai trò sàng lọc ở Mức 1, làm tiền đề để lựa chọn mục tiêu cho các bước phân tích sâu hơn.

### 1.3.3. Nmap Scripting Engine

Nmap Scripting Engine (NSE) mở rộng khả năng tương tác của Nmap lên tầng ứng dụng thông qua các kịch bản viết bằng ngôn ngữ Lua. Trong đồ án, hai kịch bản chuyên biệt được nhóm em sử dụng gồm:

- **Kịch bản `smb-protocols.nse`:** Gửi gói tin `Negotiate Protocol Request` mang danh sách các dialect SMB để phân tích gói tin phản hồi từ máy chủ, qua đó nhận diện việc hệ thống có chấp thuận giao thức SMBv1 (`NT LM 0.12`) hay không.
- **Kịch bản `smb-vuln-ms17-010.nse`:** Thăm dò an toàn dấu hiệu của bản tin MS17-010 bằng cách kết nối vào tài nguyên chia sẻ quản trị `IPC$` và gửi yêu cầu kiểm tra qua Named Pipe (sử dụng lệnh `SMB_COM_TRANSACTION2` với hàm `PeekNamedPipe`).

Kịch bản đưa ra đánh giá dựa trên mã trạng thái NT Status trả về từ nhân hệ điều hành:
- Nếu nhận mã lỗi bộ nhớ `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`), hệ thống bộc lộ dấu hiệu chưa được cài đặt bản vá MS17-010 và kịch bản xuất kết luận `State: VULNERABLE`.
- Nếu nhận mã lỗi truy cập `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc yêu cầu bị từ chối, hệ thống có dấu hiệu đã được cập nhật an toàn.

Điểm cần lưu ý là kịch bản NSE chỉ phân tích mã lỗi logic từ một gói tin thăm dò chứ không tiến hành khai thác bộ nhớ. Kết quả này có thể phát sinh âm tính giả nếu máy chủ chặn kết nối nặc danh vào `IPC$`. Vì vậy, NSE đóng vai trò cầu nối ở Mức 2 và Mức 3, cung cấp các chỉ báo kỹ thuật quan trọng trước khi quyết định thực hiện các bước xác minh sâu hơn.

### 1.3.4. Metasploit Framework

Metasploit Framework được nhóm em sử dụng trong phạm vi lab cô lập nhằm thực hiện các tác vụ quét đối chiếu và khai thác kiểm chứng. Khung công cụ này được áp dụng theo hai hướng:

- **Mô-đun phụ trợ (Auxiliary Module):** Sử dụng `auxiliary/scanner/smb/smb_ms17_010` để rà quét độc lập, tạo nguồn dữ liệu đối chiếu chéo với kịch bản NSE nhằm nâng cao độ tin cậy của chỉ báo lỗ hổng.
- **Mô-đun khai thác có kiểm soát (Exploit Module):** Sử dụng `exploit/windows/smb/ms17_010_eternalblue` để xác minh trực tiếp khả năng thực thi mã lệnh của CVE-2017-0144 trên máy ảo mục tiêu.

Khác với các công cụ quét thụ động, Metasploit cung cấp bằng chứng trực tiếp về mức độ ảnh hưởng. Việc mở thành công phiên tương tác với đặc quyền `NT AUTHORITY\SYSTEM` khẳng định lỗ hổng có thể bị lợi dụng để chiếm quyền kiểm soát máy chủ hoàn toàn. Ngược lại, nếu quá trình can thiệp thất bại, công cụ cũng ghi nhận các phản ứng bất thường của hệ thống.

Do việc can thiệp vào bộ nhớ Non-Paged Pool tiềm ẩn rủi ro gây sập hệ điều hành (BSOD), mô-đun khai thác chỉ được nhóm em vận hành trên các máy ảo đã lưu ảnh chụp trạng thái (snapshot) và tuân thủ nghiêm ngặt nguyên tắc an toàn lab. Trong chuỗi đánh giá, Metasploit giữ vai trò công cụ thẩm định ở Mức 4.

### 1.3.5. Vai trò của các công cụ trong quy trình kiểm thử

Các công cụ nêu trên không hoạt động rời rạc mà được nhóm em phối hợp thành một chuỗi quy trình 4 giai đoạn nối tiếp nhau một cách chặt chẽ:

- **Giai đoạn 1 - Khởi tạo và thiết lập:** Hệ điều hành Kali Linux cung cấp môi trường thực nghiệm an toàn, cô lập với mạng ngoài, định tuyến kết nối tới dải mạng máy ảo mục tiêu.
- **Giai đoạn 2 - Quét mạng và xác định cổng:** Nmap thực hiện quét cổng TCP 139 và 445 để xác định máy chủ mục tiêu có mở dịch vụ SMB hay không. Nếu cổng đóng hoặc bị lọc, quy trình dừng lại để ghi nhận trạng thái mạng.
- **Giai đoạn 3 - Nhận diện dialect và thăm dò dấu hiệu:** Nmap NSE (kịch bản `smb-protocols` và `smb-vuln-ms17-010`) cùng Metasploit Auxiliary kiểm tra xem máy chủ có hỗ trợ SMBv1 và có phản hồi mã lỗi đặc trưng của bản tin MS17-010 hay không.
- **Giai đoạn 4 - Thẩm định có kiểm soát:** Khi các dấu hiệu kỹ thuật ở Giai đoạn 3 trùng khớp, Metasploit Exploit được kích hoạt trên môi trường lab đã lưu snapshot để xác minh khả năng thực thi mã thực tế.

Cách tiếp cận đa tầng này giúp quy trình kiểm thử của nhóm em tránh được sai lầm phổ biến là vội vàng kích hoạt mã khai thác khi chưa hiểu rõ trạng thái dịch vụ. Đồng thời, phương pháp này bảo đảm mỗi kết luận an ninh đều có căn cứ kỹ thuật rõ ràng tương ứng với từng lớp công cụ.

---

## 1.4. Tiêu chí xác minh trạng thái SMB và MS17-010

### 1.4.1. Phát hiện dịch vụ SMB

Tiêu chí Mức 1 tập trung xác định sự hiện diện của dịch vụ SMB trên đường truyền mạng giữa trạm kiểm thử và máy chủ mục tiêu.

- **Dấu hiệu kỹ thuật:** Trạm kiểm thử gửi các gói tin TCP SYN tới cổng TCP 445 (Direct-hosted SMB) hoặc TCP 139 (NetBIOS Session Service). Trạng thái cổng được xác nhận là `Open` khi máy chủ phản hồi gói tin TCP SYN-ACK.
- **Ý nghĩa an ninh:** Kết quả này chứng minh máy chủ đang vận hành một dịch vụ lắng nghe trên cổng SMB và trạm kiểm thử có thể tiếp cận được dịch vụ đó qua mạng.
- **Ranh giới đánh giá:** Việc mở cổng 445 hoặc 139 **hoàn toàn không đồng nghĩa với việc hệ thống có lỗ hổng**. Bất kỳ máy chủ Windows nào có chia sẻ dữ liệu hoặc tham gia quản trị nội bộ đều mở các cổng này. Đây là điều kiện cần về khả năng tiếp cận mạng trước khi tiến hành các bước kiểm tra tiếp theo.

### 1.4.2. Nhận diện SMBv1

Sau khi xác định cổng dịch vụ mở, Mức 2 kiểm tra xem dịch vụ SMB của máy chủ có chấp thuận giao tiếp bằng giao thức cũ SMBv1 hay không.

- **Tiêu chí giao thức:** Trạm kiểm thử gửi gói tin `Negotiate Protocol Request` chứa danh sách các dialect SMB, bao gồm chuỗi định danh `NT LM 0.12`. Nếu máy chủ phản hồi bằng gói tin `Negotiate Protocol Response` lựa chọn dialect này, hệ thống được ghi nhận là có hỗ trợ SMBv1.
- **Bản chất rủi ro:** Kết quả này khẳng định máy chủ đang duy trì giao thức legacy với cơ chế bảo mật yếu, đồng thời driver `srv.sys` đang được nạp trong bộ nhớ nhân để xử lý các gói tin này.
- **Ranh giới kết luận:** Máy chủ chấp thuận SMBv1 **chưa đủ cơ sở để khẳng định hệ thống tồn tại lỗ hổng MS17-010**. Nhiều hệ thống Windows đã được cập nhật bản vá an ninh nhưng vẫn bật SMBv1 để duy trì tương thích với thiết bị mạng cũ. Khi đó, mã nguồn xử lý trong `srv.sys` đã được Microsoft sửa đổi an toàn.

### 1.4.3. Xác định dấu hiệu lỗ hổng

Mức 3 đi sâu vào việc thu thập các phản hồi kỹ thuật để nhận diện dấu hiệu driver `srv.sys` chưa được cài đặt bản cập nhật an ninh MS17-010.

- **Phản hồi từ dịch vụ:** Trạm kiểm thử thiết lập phiên kết nối tới tài nguyên chia sẻ quản trị `IPC$` và gửi gói tin giao dịch thăm dò an toàn qua Named Pipe:
  - *Dấu hiệu chưa vá:* Máy chủ phản hồi mã trạng thái `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`). Đây là phản xạ đặc trưng của nhánh mã `srv.sys` cũ khi xử lý yêu cầu bộ nhớ bất thường.
  - *Dấu hiệu đã vá hoặc an toàn:* Máy chủ phản hồi mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`), mã lỗi handle không hợp lệ, hoặc từ chối thực hiện yêu cầu giao dịch.
- **Mức độ tin cậy:** Cung cấp chỉ báo có độ tin cậy kỹ thuật cao về việc hệ thống mục tiêu đang thiếu gói cập nhật bảo mật của Microsoft.
- **Ranh giới suy luận:** Dấu hiệu ở Mức 3 **mới dừng lại ở mức độ suy đoán có căn cứ, chưa phải bằng chứng khẳng định việc khai thác chắc chắn thành công**. Kết quả này có thể bị sai lệch nếu máy chủ áp dụng chính sách chặn kết nối nặc danh hoặc có thiết bị giám sát lưu lượng mạng can thiệp.

### 1.4.4. Xác minh lỗ hổng

Mức 4 là bước xác thực thực nghiệm nhằm làm rõ khả năng can thiệp bộ nhớ và thực thi mã tùy ý của lỗ hổng CVE-2017-0144 trong môi trường lab cô lập.

- **Xác minh thực nghiệm:** Kích hoạt mô-đun khai thác có kiểm soát để gửi gói tin kích hoạt lỗi tràn vùng đệm Non-Paged Pool:
  - *Xác minh thành công:* Trạm kiểm thử thiết lập được phiên điều khiển tương tác từ xa (Command Shell hoặc Meterpreter) với đặc quyền `NT AUTHORITY\SYSTEM`.
  - *Gián đoạn dịch vụ:* Quá trình can thiệp bộ nhớ thất bại làm máy chủ mục tiêu bị treo cứng hoặc gặp lỗi dừng màn hình xanh (BSOD).
- **Hệ quả thực tế:** Cung cấp minh chứng thực nghiệm xác thực nhất về việc lỗ hổng có thể bị lợi dụng để chiếm đoạt quyền điều khiển cao nhất, đồng thời cảnh báo rủi ro làm tê liệt tính sẵn sàng của máy chủ.
- **Phạm vi áp dụng:** Do can thiệp trực tiếp vào bộ nhớ nhân, việc kiểm tra ở Mức 4 tuyệt đối không được thực hiện trên môi trường thực tế mà chỉ triển khai trong mạng lab cô lập, sau khi đã sao lưu trạng thái máy ảo bằng snapshot.

### 1.4.5. Giới hạn của phương pháp xác minh

Để bảo đảm tính khách quan và khoa học, nhóm em xác lập các giới hạn kỹ thuật cần tính đến khi đánh giá kết quả kiểm thử:

- **Ảnh hưởng của tường lửa:** Tường lửa mạng hoặc tường lửa cục bộ Windows Firewall nếu được cấu hình chặn cổng hoặc lọc gói tin sẽ khiến công cụ ghi nhận trạng thái `Filtered`. Trạng thái này chỉ phản ánh việc đường truyền bị chặn từ vị trí trạm kiểm thử, không phản ánh việc dịch vụ bên trong máy chủ có an toàn hay không.
- **Chính sách hạn chế kết nối nặc danh (Null Session):** Nếu máy chủ Windows được cấu hình cấm hoàn toàn các kết nối nặc danh vào tài nguyên `IPC$`, các kịch bản thăm dò ở Mức 3 sẽ không thể hoàn tất bước thiết lập phiên và không nhận được mã phản hồi NT Status. Khi đó, công cụ có thể báo không phát hiện thấy lỗ hổng (âm tính giả) dù thực tế hệ thống vẫn chưa được vá bản cập nhật MS17-010.
- **Sự khác biệt giữa các phiên bản Windows:** Cùng một lỗ hổng MS17-010 nhưng cấu trúc bộ nhớ nhân và cơ chế bảo vệ của Windows 7 SP1 x64, Windows Server 2008 R2 và Windows 10 có sự khác biệt rõ rệt. Một kỹ thuật khai thác thành công trên Windows 7 có thể gây lỗi BSOD ngay lập tức trên Windows 10 do các cơ chế bảo vệ phân bổ vùng nhớ được tăng cường.
- **Tính phi tuyệt đối của việc quan sát từ bên ngoài:** Mọi công cụ quét mạng từ xa (Black-box) chỉ ghi nhận những phản hồi trên đường truyền, không thể thay thế cho việc kiểm tra cấu hình nội tại của hệ thống. Do đó, để đưa ra kết luận chuẩn xác, nhóm em luôn đối chiếu kết quả kiểm thử từ xa với việc kiểm tra trực tiếp danh mục bản vá KB (Hotfix) và trạng thái tính năng SMBv1 bằng lệnh quản trị trên máy chủ mục tiêu (kiểm tra White-box).

Toàn bộ khung tiêu chí 4 mức và các giới hạn kỹ thuật này tạo thành nền tảng phương pháp luận xuyên suốt, làm cơ sở trực tiếp để nhóm em thiết kế mô hình mạng lab cô lập trong Chương 2 và triển khai thực nghiệm đối chứng trong Chương 3.
