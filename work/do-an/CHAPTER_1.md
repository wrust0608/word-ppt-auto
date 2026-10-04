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

Sự khác biệt giữa SMBv1, SMBv2 và SMBv3 cần được xem xét ở hai phương diện: cách tổ chức thao tác truy cập tài nguyên và cơ chế bảo vệ dữ liệu trao đổi. Một phiên bản mới có thể bổ sung cả hai, nhưng khả năng được giao thức hỗ trợ chưa đồng nghĩa với tính năng đã được sử dụng trong một kết nối cụ thể. Vì vậy, việc đánh giá phải dựa vào phiên bản được thương lượng và chính sách của hai đầu kết nối, thay vì chỉ dựa vào tên hệ điều hành [3], [4].

Ở SMBv1, nhiều thao tác truy cập tệp cần các lượt yêu cầu và phản hồi riêng. Khi Client phải chờ phản hồi trước khi gửi thao tác tiếp theo, độ trễ mạng được cộng vào thời gian hoàn thành công việc. SMBv2 bổ sung khả năng gộp lệnh (Compounding), cho phép đưa nhiều thao tác liên quan vào cùng một lần trao đổi [3]. Chẳng hạn, với một tác vụ gồm mở, đọc và đóng tệp, việc giảm số lượt trao đổi có thể giảm thời gian chờ giữa các thao tác. Đây là giải thích về cơ chế; đề tài chưa đo mức cải thiện hiệu năng trong lab.

Cơ chế ký dữ liệu SMB (SMB Signing) và mã hóa dữ liệu SMB (SMB Encryption) giải quyết những vấn đề khác nhau. Signing cho bên nhận kiểm tra tính toàn vẹn của nội dung bằng chữ ký được tính từ dữ liệu và khóa của phiên; khi nội dung bị sửa trên đường truyền, việc kiểm tra chữ ký có thể phát hiện sai lệch. Signing không có mục đích che giấu nội dung với bên có thể quan sát lưu lượng. Các thuật toán ký thay đổi từ MD5 ở SMBv1, HMAC-SHA256 ở SMB 2.0.2 đến AES-CMAC ở SMB 3.0; AES-128-GMAC được bổ sung trên Windows Server 2022 và Windows 11 [5]. Không áp đặc tính của các hệ thống mới này cho máy Windows 7 trong lab.

SMBv3 bổ sung Encryption để bảo vệ nội dung khi truyền qua mạng; Client và Server đều phải hỗ trợ SMB 3.x và có cấu hình tương ứng. Microsoft cho phép áp dụng mã hóa ở mức thư mục chia sẻ hoặc toàn Server. Cơ chế này bảo vệ dữ liệu trên đường truyền, khác với mã hóa dữ liệu lưu trên đĩa bằng EFS hoặc BitLocker [4]. Do đó, khi kiểm tra một hệ thống có SMBv3, cần xác định kết nối có thực sự dùng mã hóa hay không; chỉ nhìn thấy một phiên bản SMB 3.x chưa trả lời được câu hỏi này.

SMB 3.1.1 còn có cơ chế bảo vệ tính toàn vẹn trước xác thực (Pre-authentication Integrity), sử dụng SHA-512 trên chuỗi trao đổi thương lượng và thiết lập phiên. Giá trị băm được đưa vào quá trình tạo khóa phiên, nên thay đổi nội dung trao đổi có thể khiến các bên không kiểm tra được chữ ký bằng khóa tương ứng. Tài liệu Microsoft cũng giới hạn cơ chế này đối với phiên guest và nặc danh, vì không có khóa được suy xuất [6]. Theo phạm vi Microsoft mô tả, cơ chế này bảo vệ trước việc hạ cấp từ SMB 3.1.1 xuống SMB 2.x, nhưng không bảo vệ một kết nối bị hạ xuống SMB 1.0 [4]. Vì vậy, vẫn phải xem việc loại bỏ SMBv1 là một cấu hình cần kiểm tra riêng.

Với đề tài này, thay đổi có ý nghĩa trực tiếp là Server còn tiếp nhận SMBv1 hay không. MS17-010 sửa các lỗi trong xử lý SMBv1; vá hệ thống làm thay đổi phần triển khai bị lỗi, còn vô hiệu hóa SMBv1 làm mất đường giao tiếp tới phần xử lý đó [7], [8]. Hai biện pháp tác động ở những vị trí khác nhau, nên Chương 2 dùng phép kiểm tra bản vá và phép thương lượng giao thức để phân biệt chúng. Việc kiểm tra Client hợp lệ tiếp tục sử dụng SMBv2 cũng giúp xác định tác động lên chức năng chia sẻ tệp.

*Bảng 1.1: So sánh đặc tính kỹ thuật cơ bản giữa SMBv1, SMBv2 và SMBv3 [3], [4], [5], [8], [6].*

| Đặc tính kỹ thuật | SMBv1 (CIFS) | SMBv2 (2.0.2 / 2.1) | SMBv3 (3.0 / 3.0.2 / 3.1.1) |
|---|---|---|---|
| **Hệ điều hành đại diện** | Windows XP / Windows 7 khi bật SMBv1 | Windows Vista / Server 2008 | Windows 8 / Server 2012 trở lên, tùy dialect |
| **Cơ chế xử lý lệnh** | Tuần tự từng bước | Hỗ trợ gộp lệnh (Compounding) | Gộp lệnh tối ưu |
| **Cổng mạng kết nối** | TCP 139 và TCP 445 | TCP 445 | TCP 445 |
| **Ký số (SMB Signing)** | MD5-based | HMAC-SHA256 | AES-CMAC (3.0 / 3.0.2); GMAC trên một số hệ thống mới hỗ trợ SMB 3.1.1 |
| **Mã hóa dữ liệu** | Không có SMB Encryption tích hợp | Không hỗ trợ | AES-128-CCM (3.0); AES-128-GCM (3.1.1) |
| **Bảo vệ tiền xác thực** | Không hỗ trợ | Không hỗ trợ | Chỉ SMB 3.1.1: Pre-authentication Integrity dùng SHA-512 |
| **Cơ chế bảo vệ nổi bật** | Giao thức legacy, không có encryption tích hợp | Ký số HMAC-SHA256, hỗ trợ gộp lệnh | Mã hóa khối AES và bảo vệ toàn vẹn tùy dialect |

### 1.1.4. Phân tích cổng mạng TCP 139 và TCP 445

SMB có thể sử dụng TCP 139 qua dịch vụ phiên NetBIOS (NetBIOS Session Service), hoặc TCP 445 khi truyền trực tiếp trên TCP/IP (Direct-hosted SMB). Microsoft mô tả SMB 1.0 và CIFS có thể dùng NetBIOS, trong khi SMB 2.0.2 từ Windows Vista và Windows Server 2008 sử dụng TCP 445 [2]. Hai cổng vì vậy cần được phân biệt theo phiên bản và cấu hình, không xem là hai đường kết nối tương đương cho mọi phiên bản SMB.

Với TCP 445, dữ liệu SMB có tiêu đề bốn byte chỉ độ dài. Khi cả Direct-hosted SMB và NetBIOS đều được bật, Windows thử hai phương thức đồng thời và sử dụng phương thức phản hồi trước [2]. Do đường truyền được chọn còn phụ thuộc vào cấu hình hai đầu, kết quả quan sát trên một cổng phải được đọc cùng với phương thức kết nối được sử dụng trong lượt kiểm tra.

Trong đề tài, kết quả cổng 445 ở trạng thái `open` chỉ xác nhận khả năng tiếp cận một dịch vụ đang lắng nghe; cần kiểm tra tiếp để nhận diện SMB và phiên bản được chấp nhận. Khi thiết kế phòng thủ, cổng 139 cũng phải được xem xét nếu cấu hình còn cho phép SMB qua NetBIOS. Việc đóng một cổng không tự chứng minh hệ thống đã được vá MS17-010.

### 1.1.5. Quy trình trao đổi yêu cầu và phản hồi

Có thể theo dõi quá trình truy cập `\\Server\Share` qua ba câu hỏi: hai bên dùng phiên bản nào, phiên được thiết lập với danh tính nào và phiên đó kết nối tới tài nguyên nào. Đặc tả SMB2 minh họa các bước tương ứng là `NEGOTIATE`, `SESSION_SETUP` và `TREE_CONNECT` [9]. Phân biệt ba bước giúp xác định một lỗi xảy ra ở khâu tương thích giao thức, xác thực hay kết nối tài nguyên.

Trong bước thương lượng (Negotiate), Client đưa ra các phiên bản có thể sử dụng và Server trả lại lựa chọn phù hợp. Kết quả này xác định cách hai bên diễn giải những yêu cầu tiếp theo. Trong bước thiết lập phiên (Session Setup), hai bên trao đổi dữ liệu xác thực; bước này có thể cần nhiều lượt trao đổi, nên một phản hồi `STATUS_MORE_PROCESSING_REQUIRED` chưa phải là xác thực thất bại [9]. Sau khi phiên được thiết lập, Client mới yêu cầu kết nối tới một tài nguyên chia sẻ. Việc xác thực danh tính và quyền sử dụng tài nguyên là hai lớp kiểm soát khác nhau: Server còn xét quyền truy cập của người dùng đối với tài nguyên [5].

Các định danh trong phản hồi giúp gắn yêu cầu tiếp theo với đúng ngữ cảnh. SMBv1/CIFS dùng mã định danh người dùng của phiên (User ID – UID) và mã định danh kết nối tài nguyên (Tree ID – TID); SMBv2/v3 dùng `SessionId` và `TreeId` [9], [10]. Khi phân tích lưu lượng, cần đọc định danh cùng loại lệnh và mã trạng thái, vì phản hồi thương lượng thành công không thể thay cho bằng chứng kết nối tới một tài nguyên cụ thể.

Trong lab, phép kiểm tra phiên bản dừng ở câu hỏi Server có chấp nhận SMBv1 hay không. Phép thăm dò MS17-010 đi xa hơn, cần thiết lập phiên và kết nối `IPC$` trước khi gửi yêu cầu kiểm tra. Nếu thất bại ở bước kết nối `IPC$`, người kiểm thử chưa quan sát được phản hồi của phép thăm dò; vì vậy, không được lấy việc bị từ chối tài nguyên làm bằng chứng rằng Server đã vá. Ngược lại, một phiên được thiết lập hợp lệ chỉ cho thấy bước xác thực hoàn tất, chưa chứng minh phần xử lý SMBv1 không có lỗi.

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

Vào tháng 03 năm 2017, Microsoft phát hành thông báo bảo mật định kỳ mang mã hiệu **MS17-010** nhằm khắc phục các lỗ hổng nghiêm trọng trong việc xử lý gói tin của dịch vụ SMBv1 trên hệ điều hành Windows [7]. Nhóm lỗ hổng này ảnh hưởng tới hầu hết các phiên bản Windows lưu hành tại thời điểm đó, bao gồm Windows Vista, Windows 7, Windows 8.1, Windows 10, cùng các dòng máy chủ Windows Server 2008, 2012 và 2016. Do tính chất nghiêm trọng, Microsoft sau đó đã phát hành thêm bản vá cho các hệ điều hành đã dừng hỗ trợ như Windows XP và Windows Server 2003 [7].

Các lỗ hổng thực thi mã từ xa trong thông báo MS17-010 cho phép kẻ tấn công gửi các thông điệp SMBv1 được chế tạo đặc biệt tới máy chủ mục tiêu. Trong nhiều trường hợp, việc khai thác có thể được thực hiện từ xa mà không cần thông tin xác thực hợp lệ [7]. Trong phạm vi đề tài, CVE-2017-0144 / EternalBlue được lựa chọn làm trường hợp kiểm thử chính.

### 1.2.2. Phân loại các mã CVE và danh mục bản vá theo hệ điều hành

Thông báo bảo mật MS17-010 xử lý một nhóm gồm 6 mã định danh lỗ hổng phổ biến (CVE) được Microsoft liệt kê trong thông báo [7]. Không đồng nhất mọi CVE với cơ chế lỗi FEA của EternalBlue. Để trình bày rõ ràng, nội dung được phân tách thành hai bảng: Bảng 1.2 mô tả đặc tính kỹ thuật từng CVE và Bảng 1.3 liệt kê danh mục mã bản vá KB chính thức theo từng phiên bản hệ điều hành.

*Bảng 1.2: Phân loại các mã CVE trong thông báo bảo mật Microsoft MS17-010 [7], [11], [12], [13].*

| Mã CVE | Liên hệ exploit | Phân loại theo nguồn chính thức | Tác động | Vai trò trong đồ án |
|---|---|---|---|---|
| **CVE-2017-0143** | **EternalSynergy** [11] | SMBv1 Remote Code Execution Vulnerability | RCE | Tham chiếu trong nhóm MS17-010 |
| **CVE-2017-0144** | **EternalBlue** [12] | SMBv1 Remote Code Execution Vulnerability; EternalBlue khai thác lỗi xử lý FEA trong `srv.sys` | RCE | **Mục tiêu thực nghiệm chính** |
| **CVE-2017-0145** | **EternalRomance** [13] | SMBv1 Remote Code Execution Vulnerability | RCE | Tham chiếu lịch sử / đối chiếu |
| **CVE-2017-0146** | Không gắn nickname | SMBv1 Remote Code Execution Vulnerability | RCE | Thuộc phạm vi MS17-010 |
| **CVE-2017-0147** | Không gắn nickname | SMBv1 Information Disclosure Vulnerability | Information Disclosure | Thuộc phạm vi MS17-010 |
| **CVE-2017-0148** | Không gắn nickname | SMBv1 Remote Code Execution Vulnerability | RCE | Thuộc phạm vi MS17-010 |

Sau Bảng 1.2, đề tài chỉ phân tích sâu cơ chế của CVE-2017-0144, vì đây là mục tiêu thực nghiệm trung tâm của kịch bản lab.

*Bảng 1.3: Danh mục mã bản vá KB chính thức của Microsoft theo hệ điều hành Windows [7].*

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

CVE-2017-0144 liên quan đến việc xử lý danh sách thuộc tính mở rộng của tệp (File Extended Attributes – FEA) trong phần triển khai SMBv1. Rapid7 mô tả phép tính kích thước ở `SrvOs2FeaListSizeToNt` có sai lệch giữa giá trị DWORD và WORD; quá trình chuyển đổi ở `SrvOs2FeaToNt` sau đó có thể tràn bộ đệm trong thao tác sao chép `memmove` [14]. Điểm cần giải thích là mối quan hệ giữa kích thước dùng để cấp phát và lượng dữ liệu thực sự được ghi, vì gửi một yêu cầu khác thường chưa tự tạo ra thực thi mã.

Để diễn giải quan hệ này, gọi $L_{alloc}$ là kích thước vùng nhớ được cấp phát và $L_{write}$ là lượng dữ liệu được ghi trong quá trình chuyển đổi. Đây là hai đại lượng khái niệm phục vụ phân tích, không phải số đo của lab. Một thao tác ghi trong phạm vi hợp lệ cần bảo đảm $L_{write} \leq L_{alloc}$. Khi khâu tính kích thước và khâu chuyển đổi không nhất quán, có thể xuất hiện $L_{write} > L_{alloc}$; phần ghi vượt giới hạn khi đó tác động vào vùng nhớ nằm ngoài bộ đệm dự kiến. Sai lệch không chỉ nằm ở dữ liệu của tệp, mà có thể làm thay đổi dữ liệu đang được hệ điều hành sử dụng để xử lý các kết nối.

Tràn bộ nhớ và thực thi mã là hai bước khác nhau. Ghi ngoài giới hạn có thể làm hỏng một vùng dữ liệu không phù hợp và khiến hệ điều hành dừng, thay vì tạo ra quyền thực thi cho bên gửi yêu cầu. EternalBlue kết hợp lỗi này với việc bố trí vùng nhớ (Pool Grooming) để tác động tới cấu trúc thích hợp; Rapid7 xác định việc chuyển hướng thực thi diễn ra về sau tại `srvnet!SrvNetWskReceiveComplete` [14]. Vì vậy, trạng thái bộ nhớ và cấu hình mục tiêu có ý nghĩa đối với kết quả của một lượt thử, còn nhãn chưa vá chỉ phản ánh một điều kiện của đường tấn công.

Ví dụ giả định để minh họa, một vùng nhớ được cấp phát 64 byte nhưng thao tác ghi sử dụng 80 byte sẽ có 16 byte vượt giới hạn. Các con số này không phải kích thước FEA hay dữ liệu của EternalBlue. Chúng cho thấy việc kiểm tra đúng kích thước yêu cầu ở một bước chưa đủ nếu bước chuyển đổi sau đó sử dụng một kích thước khác.

Sai lệch tính kích thước làm phát sinh nguy cơ ghi ngoài bộ đệm, từ đó dữ liệu ngoài bộ đệm có thể bị thay đổi. Hệ quả có thể là mất ổn định hoặc chuyển hướng thực thi, tùy vùng nhớ bị tác động và cách khai thác sử dụng lỗi. Vì vậy, một lượt thử không tạo được phiên chưa đủ để phủ nhận lỗ hổng, đồng thời một lần BSOD cũng chưa chứng minh thực thi mã thành công.

Trong đề tài, quan sát từ xa được đối chiếu với bản dựng Windows, bản vá, trạng thái SMBv1 và dữ liệu của lượt thử. Bằng chứng lệnh chạy với quyền `SYSTEM` cho biết quyền của phiên quan sát được; `SYSTEM` là danh tính bảo mật của Windows, không đồng nhất với chế độ thực thi trong nhân (Kernel Mode). Muốn khẳng định chi tiết thao tác trong nhân cần bằng chứng tương ứng, còn output của phiên tương tác chỉ hỗ trợ kết luận về tác động đã xác nhận. Cách phân định này được dùng làm tiêu chí đánh giá ở Chương 2.

```text
Sai lệch tính kích thước FEA
             |
             v
Lượng dữ liệu ghi vượt vùng nhớ được cấp phát
             |
             v
Dữ liệu ngoài bộ đệm bị thay đổi
             |
             +----> Mất ổn định / dừng hệ thống
             |
             +----> Có thể chuyển hướng thực thi khi đủ điều kiện
```
*Sơ đồ 1.3: Quan hệ giữa lỗi kích thước FEA, ghi ngoài bộ đệm và các hệ quả có thể xảy ra.*

### 1.2.4. Điều kiện hệ thống có nguy cơ bị khai thác

Để một hệ thống Windows nằm trong phạm vi có thể bị khai thác CVE-2017-0144, cần xem xét các điều kiện kỹ thuật sau [7], [12], [14]:
1. **Hệ điều hành:** Đang sử dụng phiên bản Windows thuộc danh mục bị ảnh hưởng (từ Windows XP đến Windows 10 các bản dựng đầu, hoặc Windows Server 2003 đến 2016) [7]. Trong phạm vi thực nghiệm, đề tài lựa chọn Windows 7 SP1 x64 làm máy mục tiêu do thuộc nhóm hệ điều hành bị ảnh hưởng và được module Metasploit hỗ trợ trong kịch bản kiểm thử của đề tài [14].
2. **Tính năng SMBv1 đang được kích hoạt:** Driver xử lý `srv.sys` đang hoạt động và tiếp nhận các yêu cầu giao dịch SMBv1 [8].
3. **Cổng dịch vụ mạng có thể tiếp cận được:** Cổng TCP 445 (hoặc TCP 139) ở trạng thái mở và không bị chặn bởi tường lửa mạng hoặc tường lửa cục bộ [15].
4. **Chưa cài đặt bản vá an ninh MS17-010:** Hệ điều hành chưa được cập nhật gói vá bảo mật tương ứng theo danh mục ở Bảng 1.3 [7].
5. **Đặc điểm xác thực:** CVE-2017-0144 có thể được khai thác từ xa mà không yêu cầu tài khoản xác thực hợp lệ khi dịch vụ SMBv1 mục tiêu có thể tiếp cận [7], [12]. Việc sử dụng `IPC$` trong đề tài chủ yếu xuất hiện ở cơ chế thăm dò của kịch bản Nmap và được phân tích chi tiết tại Mục 1.3.3.

**Nguyên tắc đánh giá:** Cần phân biệt giữa việc "hệ thống mở cổng 445" hoặc "hệ thống đang bật SMBv1" với việc "hệ thống có lỗ hổng MS17-010". Một máy tính đã cài đặt bản vá bảo mật vẫn mở cổng 445 để phục vụ chia sẻ tệp bình thường, nhưng driver `srv.sys` đã được bổ sung đoạn mã kiểm tra tính hợp lệ của tham số, do đó không còn bị ảnh hưởng bởi lỗi tràn bộ nhớ này [7], [8].

### 1.2.5. Tác động an toàn thông tin

Tác động của CVE-2017-0144 cần được đánh giá theo tính bí mật, toàn vẹn và sẵn sàng của tài nguyên. NVD phân loại đây là lỗ hổng có thể dẫn tới thực thi mã từ xa [12]. Tuy nhiên, từ khả năng thực thi mã tới từng hậu quả cụ thể còn có những bước cần kiểm chứng: mã chạy với quyền nào, có thể tiếp cận dữ liệu nào và đã thực hiện thao tác gì.

Về tính bí mật, nguy cơ phát sinh khi phiên thực thi có quyền đọc dữ liệu mà bên khởi tạo không được phép truy cập qua chức năng chia sẻ tệp thông thường. Về tính toàn vẹn, nguy cơ phát sinh khi quyền thực thi cho phép sửa nội dung hoặc cấu hình ngoài phạm vi được cấp cho người dùng. Hai nguy cơ có thể cùng xuất hiện, nhưng bằng chứng đọc được một tệp không tự chứng minh đã sửa được tệp đó. Trong lab, dữ liệu thử nghiệm và tác vụ xác minh phải được xác định trước, để kết luận gắn với tài nguyên và thao tác đã quan sát.

Về tính sẵn sàng, Rapid7 ghi nhận khả năng mất ổn định, BSOD hoặc khởi động lại khi sử dụng module [14]. Đề tài do đó đánh giá riêng việc máy mục tiêu còn hoạt động và Client còn đọc, ghi được tài nguyên sau phép kiểm tra. Nếu mục tiêu dừng hệ thống mà không có bằng chứng thực thi lệnh, kết quả là sự cố làm gián đoạn dịch vụ. Nếu phiên thử nghiệm hoạt động và Client vẫn truy cập được, điều đó cũng chưa chứng minh tính bí mật hoặc toàn vẹn được bảo vệ. Việc ghi riêng các tác động giúp tránh gom mọi kết quả vào một nhãn thành công hoặc thất bại.

### 1.2.6. Khái quát các chiến dịch tấn công thực tế liên quan

Sự kết hợp giữa lỗ hổng MS17-010 và mã khai thác EternalBlue đã được ghi nhận trong các sự cố an ninh mạng diện rộng trên thế giới [13], [16]:

- **WannaCry (tháng 05/2017):** Microsoft ghi nhận mã độc có khả năng lây sang các máy Windows chưa vá trong mạng nội bộ và quét địa chỉ Internet. Hướng dẫn phòng vệ nhấn mạnh cập nhật MS17-010, tắt SMBv1 và hạn chế kết nối SMB từ các nguồn không được phép [16].
- **Mã độc NotPetya (Tháng 06/2017):** NotPetya sử dụng mã khai thác liên quan đến MS17-010 (bao gồm EternalBlue và EternalRomance) để lây lan qua mạng nội bộ. Mục tiêu chính của NotPetya là phá hoại cấu trúc hệ thống tệp và bản ghi khởi động (MBR), khiến hệ thống không thể khôi phục, gây thiệt hại cho nhiều tập đoàn vận tải và hạ tầng quốc tế [13].

Các sự cố này cho thấy việc kiểm tra, xác minh và áp dụng các biện pháp phòng thủ cho dịch vụ SMB là nhiệm vụ kỹ thuật có ý nghĩa thực tiễn trong quản trị hệ thống.

---

## 1.3. Công cụ phục vụ kiểm thử

### 1.3.1. Hệ điều hành kiểm thử Kali Linux

Kali Linux là bản phân phối Linux mã nguồn mở dựa trên Debian, phục vụ kiểm thử xâm nhập và đánh giá an toàn thông tin [17]. Đề tài lựa chọn Kali làm trạm kiểm thử để tổ chức các công cụ khảo sát và thu thập dữ liệu trong cùng một môi trường. Việc dùng Kali không tự tạo tính cô lập; điều đó phụ thuộc vào cấu hình mạng ảo và phạm vi kết nối của lab.

Trước khi kiểm thử, cần ghi phiên bản Kali, phiên bản công cụ và các thành phần đã cài đặt. Hồ sơ này giúp đối chiếu kết quả giữa các lượt chạy, thay vì giả định mọi bản Kali đều có cùng công cụ và hành vi.

### 1.3.2. Công cụ quét mạng Nmap

Nmap (Network Mapper) được dùng trước hết để khảo sát trạng thái cổng và nhận diện dịch vụ. Với quét TCP SYN (`-sS`), phản hồi `SYN-ACK` được diễn giải là `open`, phản hồi `RST` là `closed`; không nhận được phản hồi sau các lần thử lại hoặc nhận một số mã ICMP unreachable được diễn giải là `filtered` [18]. Nhãn `filtered` vì vậy mô tả giới hạn quan sát từ trạm quét, chưa chỉ ra thiết bị nào đã chặn hoặc liệu máy đích có đang hoạt động.

Sau bước quét cổng, nhận diện dịch vụ (`-sV`) dùng các yêu cầu thăm dò và đối chiếu phản hồi để nhận diện dịch vụ lắng nghe [18]. Việc thấy tên `microsoft-ds` giúp định hướng phép kiểm tra SMB, nhưng tên này chưa cho biết Server chấp nhận SMBv1 hay đã cài bản vá MS17-010. Hai câu hỏi đó cần phép kiểm tra giao thức và trạng thái mục tiêu riêng.

Trong mô hình của đề tài, cổng 445 mở là bằng chứng để chuyển sang kiểm tra phản hồi SMB. Nếu cổng đóng hoặc bị lọc, người kiểm thử cần xác định lý do trước khi diễn giải các bước sau. Chẳng hạn, không có kết quả của script do đường truyền bị chặn khác với nhận được một phản hồi SMB cho thấy không còn dấu hiệu chưa vá. Sự khác biệt này quyết định việc ghi trạng thái là `False` hay `Unknown` trong Chương 2.

### 1.3.3. Tự động hóa kiểm tra an toàn với Nmap Scripting Engine (NSE)

Nmap Scripting Engine (NSE) cho phép thực thi các tập kịch bản viết bằng ngôn ngữ Lua để tự động hóa các tác vụ kiểm tra an toàn nâng cao [18], [19]. Đối với dịch vụ SMB và lỗ hổng MS17-010:
- **Script `smb-protocols.nse`:** Nhận diện danh sách phiên bản được Server chấp nhận, trong đó `NT LM 0.12` biểu thị SMBv1 [20].
- **Script `smb-vuln-ms17-010.nse`:** Nmap xếp kịch bản này vào nhóm `safe` và `vuln`; kịch bản dùng phản hồi SMB để nhận biết dấu hiệu chưa vá MS17-010 [19]. Phân loại `safe` không phải bảo đảm mọi cấu hình mục tiêu đều không chịu tác động.

Phép thăm dò này sử dụng khác biệt trong phản hồi dịch vụ làm dấu hiệu nhận diện; nó không thực hiện chuỗi khai thác FEA và không tìm cách tạo phiên thực thi mã. Để diễn giải một kết quả, cần theo dõi phép kiểm tra đã đi tới đâu trong chuỗi sau:
1. Script dùng thư viện SMB để thiết lập kết nối và thương lượng SMBv1. Sau bước Session Setup theo thông tin xác thực được cấu hình, script gửi Tree Connect tới tài nguyên chia sẻ `\\Target\IPC$` (mặc định tham số `sharename` là `IPC$`) [19].
2. Khi phiên làm việc với `IPC$` được thiết lập, script gửi một yêu cầu giao dịch `SMB_COM_TRANSACTION` (opcode `0x25`) với lệnh `PeekNamedPipe` (mã `0x2300`) trên đường ống định danh `\PIPE\` với các tham số độ dài bộ đệm tối đa (`Max Parameter Count = 0xFFFF`, `Max Data Count = 0xFFFF`) [19].
3. **Phân tích mã trạng thái phản hồi NT Status theo mã nguồn Nmap:**
   - *Dấu hiệu phù hợp hệ thống chưa vá (VULNERABLE):* Nếu máy chủ phản hồi mã lỗi NT Status `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`), phản hồi phù hợp với dấu hiệu mà kịch bản dùng để nhận diện hệ thống chưa vá. Script ghi nhận dấu hiệu này và xuất kết luận `State: VULNERABLE` [19].
   - *Dấu hiệu phù hợp hệ thống đã vá:* Nếu máy chủ phản hồi mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc `STATUS_INVALID_HANDLE` (`0xC0000008`), kịch bản diễn giải đây là dấu hiệu phù hợp với hệ thống đã vá và ghi thông báo `This system is patched` [19]. Cần đối chiếu thêm trạng thái bản vá trên mục tiêu; một thông báo của công cụ không chứng minh hệ thống không còn mọi lỗ hổng.

Khi không kết nối được tới `IPC$`, không đọc được phản hồi hoặc nhận mã trạng thái ngoài các nhánh được nhận diện, phép kiểm tra chưa cung cấp đủ cơ sở để xác định trạng thái bản vá. Mã nguồn vẫn có thể gán `NOT_VULN` trong nhánh không phát hiện dấu hiệu; đề tài phải đọc kèm lỗi và kết quả kiểm tra, thay vì coi nhãn này là bằng chứng máy đã vá [19].

Điểm dễ nhầm là nhãn báo cáo và việc hoàn tất phép kiểm tra. Trong mã nguồn, cả nhánh nhận dấu hiệu phù hợp đã vá và nhánh gặp lỗi kết nối đều có thể đi tới trạng thái `NOT_VULN`; nguyên nhân được lưu riêng trong kết quả kiểm tra [19]. Vì vậy, đề tài giữ cả output và lỗi, rồi đối chiếu với lưu lượng và cấu hình mục tiêu. Nếu không xác định được phép thăm dò đã nhận phản hồi hợp lệ, trạng thái bản vá phải được ghi là chưa xác định.

Ví dụ giả định, một Server cho phép kết nối TCP nhưng từ chối phiên cần để truy cập `IPC$`. Người kiểm thử biết được đường mạng có phản hồi, nhưng chưa quan sát được mã trạng thái của yêu cầu `PeekNamedPipe`. Cài bản vá và thay đổi chính sách xác thực đều có thể làm kết quả công cụ khác đi, song chúng tác động vào những khâu khác nhau. Muốn phân biệt cần kiểm tra bước bị từ chối và danh sách bản vá, thay vì lấy việc không xuất hiện `VULNERABLE` làm bằng chứng duy nhất.

### 1.3.4. Nền tảng kiểm thử Metasploit Framework

Metasploit Framework là nền tảng kiểm tra xâm nhập mô-đun hóa, hỗ trợ chuẩn hóa quy trình thẩm định an toàn thông tin [14], [21]. Trong phạm vi đề tài, Metasploit được phân bổ hai vai trò rõ ràng:
- **Mô-đun phụ trợ (Auxiliary Module):** Sử dụng mô-đun `auxiliary/scanner/smb/smb_ms17_010` để kiểm tra dấu hiệu MS17-010 trong phạm vi đã xác định [22]. Cần lưu ý mô-đun này và script NSE của Nmap là hai implementation khác nhau dùng để tham chiếu chéo về mặt phản ứng dịch vụ. Các đối chứng thực sự khác loại bao gồm: bản dựng Windows (build), danh sách Hotfix/KB đã cài đặt, lưu lượng gói tin (packet capture) và trạng thái tính năng SMBv1 trên máy mục tiêu.
- **Mô-đun khai thác có kiểm soát (Exploit Module):** Sử dụng mô-đun `exploit/windows/smb/ms17_010_eternalblue` trong môi trường phòng thí nghiệm cô lập nhằm thẩm định khả năng thực thi của lỗ hổng CVE-2017-0144 [14]. Payload được giới hạn ở các thao tác xác nhận quyền thực thi; bản thân quá trình khai thác kernel vẫn có nguy cơ gây mất ổn định hoặc phát sinh lỗi màn hình xanh (BSOD), vì vậy thực nghiệm chỉ tiến hành trên máy ảo đã tạo điểm sao lưu phục hồi (snapshot) [14].

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

Sai lệch đánh giá có thể phát sinh ở khâu thu thập dữ liệu hoặc khâu diễn giải. Ở khâu thu thập, phép kiểm tra có thể không tới được dịch vụ, không thiết lập được phiên, hoặc không nhận phản hồi hợp lệ. Khi đó, kết quả thiếu thông tin về trạng thái cần đánh giá. Ở khâu diễn giải, người kiểm thử có thể nhầm dấu hiệu chưa vá với bằng chứng khai thác, hoặc nhầm việc không có phản hồi với việc lỗ hổng đã được khắc phục. Mục 1.3.3 đã phân tích sự khác biệt giữa hai nhánh có thể cùng đi tới nhãn `NOT_VULN` trong mã nguồn NSE [19].

Để giảm sai lệch, đề tài đối chiếu hai loại bằng chứng: phản hồi quan sát từ mạng và trạng thái cấu hình đọc trên mục tiêu. Hai công cụ cùng dùng một dấu hiệu SMB có ích để phát hiện khác biệt trong cách chạy hoặc xử lý phản hồi, nhưng sự đồng thuận của chúng chưa thay thế kiểm tra bản vá. Ngược lại, một danh sách KB cũng chưa mô tả việc Server có đang phục vụ SMBv1 hay trạm kiểm thử có tiếp cận được dịch vụ; cần ghép với phép thương lượng và dữ liệu mạng.

Ví dụ giả định, ba Server đều mở cổng 445 có thể mang ý nghĩa khác nhau: Server thứ nhất chỉ chấp nhận SMBv2; Server thứ hai vẫn chấp nhận SMBv1 nhưng đã vá; Server thứ ba chưa vá và có dấu hiệu phù hợp phép thăm dò. Kết quả giống nhau ở cấp độ cổng không làm ba cấu hình có cùng rủi ro đối với đường tấn công MS17-010. Nếu Server thứ ba không tạo được phiên trong một lượt thử, vẫn phải giữ bằng chứng chưa vá và tìm nguyên nhân của lượt thử, thay vì hạ kết luận chỉ theo việc phiên không xuất hiện.

### 1.4.3. Nguyên tắc giảm thiểu rủi ro và phòng thủ giao thức SMB

Các biện pháp phòng thủ cần được lựa chọn theo vị trí chúng tác động lên đường tấn công. Bản vá MS17-010 sửa phần xử lý bị lỗi trong SMBv1 [7]. Vì vậy, phép kiểm tra sau vá cần xác nhận gói cập nhật phù hợp với hệ điều hành và đối chiếu phản hồi thăm dò; việc cổng 445 vẫn mở không mâu thuẫn với mục tiêu vá, vì Server vẫn có thể cần cung cấp chia sẻ tệp.

Vô hiệu hóa SMBv1 tác động vào khả năng sử dụng giao thức cũ, thay vì sửa nội dung một yêu cầu đã tới phần xử lý. Khi Server không còn chấp nhận SMBv1, đường tấn công SMBv1 đang xét không thể tiếp tục theo cùng trình tự. Microsoft cung cấp cách cấu hình theo từng phiên bản Windows và lưu ý ảnh hưởng tới hệ thống còn phụ thuộc SMBv1 [8]. Do đó, trước khi áp dụng cần xác định Client và ứng dụng cần dùng giao thức nào; sau cấu hình cần kiểm tra cả việc từ chối SMBv1 và việc truy cập hợp lệ qua phiên bản được giữ lại.

Tường lửa và phân đoạn mạng giới hạn nguồn có thể kết nối tới dịch vụ [15]. Trong thiết kế của đề tài, chính sách cho phép Client nghiệp vụ truy cập Server nhưng chặn trạm kiểm thử ở một phân vùng khác. Nếu quy tắc có hiệu lực, trạng thái quan sát từ trạm bị chặn thay đổi dù cấu hình SMB bên trong Server có thể giữ nguyên. Vì vậy, bằng chứng tường lửa có hiệu lực phải gắn với địa chỉ nguồn, đích và cổng được kiểm tra; nó không thay thế bằng chứng đã vá hệ điều hành.

Ba biện pháp bổ sung cho nhau vì sửa lỗi, loại bỏ giao thức cũ và hạn chế đường tiếp cận là ba lớp can thiệp khác nhau. Chỉ có tường lửa thì cấu hình dễ bị ảnh hưởng nếu chính sách bị thay đổi hoặc một nguồn được cho phép bị chiếm quyền. Chỉ có bản vá của nhóm MS17-010 thì chưa trả lời các rủi ro khác của dịch vụ SMB. Đây là phân tích phạm vi tác dụng của từng biện pháp, chưa phải kết luận đã kiểm chứng mọi đường tấn công.

Kiểm thử lại cần đồng thời trả lời hai câu hỏi: điều kiện mà biện pháp hướng tới có thực sự thay đổi không, và Client hợp lệ còn hoàn thành tác vụ cần thiết không. Chẳng hạn, sau khi tắt SMBv1, bằng chứng thích hợp gồm kết quả thương lượng không chấp nhận SMBv1 và kết quả truy cập tệp qua SMBv2. Nếu mọi kết nối đều thất bại do Server dừng, chưa thể xem đó là kết quả phòng thủ đáp ứng yêu cầu nghiệp vụ. Chương 2 cụ thể hóa các cặp phép kiểm tra này trong chuỗi trạng thái có đối chứng.

---

## TỔNG KẾT CHƯƠNG 1

Chương 1 trình bày cơ sở về SMB, các lỗ hổng thuộc thông báo MS17-010 và vai trò của công cụ kiểm thử. Cổng mạng, phiên bản giao thức, phản hồi của phép thăm dò và khả năng thực thi mã được phân biệt thành bốn mức bằng chứng. Kết quả ở một mức chưa đủ để kết luận mức tiếp theo; đặc biệt, cổng mở hoặc SMBv1 đang bật không tự chứng minh hệ thống chưa vá.

Khung phân định này là cách tổ chức đánh giá của đề tài, giúp liên kết kiến thức giao thức với bước quan sát trong lab. Chương 2 sử dụng khung đó để thiết kế trạng thái máy mục tiêu, điểm thu thập dữ liệu và tiêu chí đánh giá phòng thủ. Các giới hạn về xác thực, phản hồi công cụ và tác động lên hệ thống phải được kiểm tra khi áp dụng; phần chưa có dữ liệu thực nghiệm chưa được trình bày như kết quả.


## TÀI LIỆU THAM KHẢO

[1] Microsoft, "What is Microsoft SMB Protocol and CIFS Protocol?," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview

[2] Microsoft, "Direct hosting of SMB over TCP/IP," Microsoft Learn, 2026. [Online]. Available: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/direct-hosting-of-smb-over-tcpip

[3] Microsoft, "What is SMB File Sharing for Windows and Windows Server?," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview

[4] Microsoft, "SMB security enhancements," Microsoft Learn, Jul. 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security

[5] Microsoft, "What is Server Message Block signing?," Microsoft Learn, Oct. 2024. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-signing-overview. [Accessed: Oct. 4, 2026].

[6] Microsoft, "SMB 3.1.1 Pre-authentication integrity in Windows 10," Microsoft Learn, archived Open Specifications blog. [Online]. Available: https://learn.microsoft.com/en-us/archive/blogs/openspecification/smb-3-1-1-pre-authentication-integrity-in-windows-10. [Accessed: Oct. 4, 2026].

[7] Microsoft, "Microsoft Security Bulletin MS17-010 - Critical," Microsoft Learn / Security TechCenter, Mar. 2017. [Online]. Available: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010

[8] Microsoft, "Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3

[9] Microsoft, "[MS-SMB2]: Connecting to a Share by Using an SMB2 Negotiate," Microsoft Open Specifications. [Online]. Available: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-smb2/c9efe8ca-ff34-44d0-bfbe-58a9b9db50d4. [Accessed: Oct. 4, 2026].

[10] Microsoft, "[MS-CIFS]: Common Internet File System (CIFS) Protocol," Microsoft Open Specifications, "Per SMB Session" and sec. 3.2.5.4. [Online]. Available: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cifs/c7cb45aa-f923-4cd4-a9d5-4a1418e41d42; https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cifs/c42729fb-c655-424f-8d9a-44825d609b86. [Accessed: Oct. 4, 2026].

[11] Microsoft Security Response Center (MSRC), "Eternal Synergy Exploit Analysis," Microsoft, 2017. [Online]. Available: https://msrc.microsoft.com/blog/2017/05/eternal-synergy-exploit-analysis/

[12] National Institute of Standards and Technology (NIST), "CVE-2017-0144 Detail," National Vulnerability Database (NVD), Mar. 2017. [Online]. Available: https://nvd.nist.gov/vuln/detail/CVE-2017-0144

[13] Microsoft Threat Intelligence, "New ransomware, old techniques: Petya adds-worm capabilities," Microsoft Security Blog, Jun. 2017. [Online]. Available: https://www.microsoft.com/en-us/security/blog/2017/06/27/new-ransomware-old-techniques-petya-adds-worm-capabilities/

[14] Rapid7, "MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption," Rapid7 Exploit Database, 2017. [Online]. Available: https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/

[15] National Institute of Standards and Technology, Guidelines on Firewalls and Firewall Policy, NIST SP 800-41 Rev. 1, 2009. [Online]. Available: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-41r1.pdf.

[16] Microsoft Threat Intelligence, "WannaCrypt ransomware worm targets out-of-date systems," Microsoft Security Blog, May 2017. [Online]. Available: https://www.microsoft.com/en-us/security/blog/2017/05/12/wannacrypt-ransomware-worm-targets-out-of-date-systems/

[17] Kali Linux, "What is Kali Linux?," Kali Linux Documentation. [Online]. Available: https://www.kali.org/docs/introduction/what-is-kali-linux/. [Accessed: Oct. 4, 2026].

[18] G. Lyon, *Nmap Network Scanning: The Official Nmap Project Guide to Network Discovery and Vulnerability Scanning*. Sunnyvale, CA: Insecure.Com LLC, 2009. [Online]. Available: https://nmap.org/book/; sec. "TCP SYN (Stealth) Scan": https://nmap.org/book/synscan.html.

[19] P. Calderon and Nmap Project, "smb-vuln-ms17-010.nse Script Source Code," Nmap Project, 2017. [Online]. Available: https://svn.nmap.org/nmap/scripts/smb-vuln-ms17-010.nse

[20] P. Calderon and Nmap Project, "smb-protocols.nse Script Source Code," Nmap Project. [Online]. Available: https://svn.nmap.org/nmap/scripts/smb-protocols.nse. [Accessed: Oct. 4, 2026].

[21] Rapid7, "Metasploit Framework," Metasploit Documentation. [Online]. Available: https://docs.rapid7.com/metasploit/msf-overview/. [Accessed: Oct. 4, 2026].

[22] Rapid7, "MS17-010 SMB RCE Detection," Metasploit Framework, source code. [Online]. Available: https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/scanner/smb/smb_ms17_010.rb. [Accessed: Oct. 4, 2026].
