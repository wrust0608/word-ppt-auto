# CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ CÔNG CỤ KIỂM THỬ SMB

Chương 1 thiết lập nền tảng lý thuyết và cơ sở đo đạc kỹ thuật cho toàn bộ quá trình khảo sát, đánh giá an toàn dịch vụ chia sẻ tệp Server Message Block (SMB) cùng lỗ hổng bảo mật MS17-010. Thay vì tiếp cận các công cụ quét mạng như các phần mềm tự động hóa đơn thuần, nội dung chương tập trung làm rõ bản chất giao thức, cơ chế xử lý nội bộ của hệ điều hành và mối quan hệ kỹ thuật giữa các tín hiệu quan sát từ xa với trạng thái an ninh thực tế trên máy chủ mục tiêu.

Nội dung chương được tổ chức nhằm phân định rạch ròi năm bình diện kỹ thuật cốt lõi: khả năng tiếp cận dịch vụ qua cổng mạng tầng giao vận, bề mặt phơi nhiễm của các phương ngữ giao thức, dấu hiệu phản hồi từ kịch bản quét từ xa, trạng thái cập nhật bản vá nội bộ trên hệ điều hành và các tầng kiểm soát phòng thủ tương ứng. Sự phân tách này cung cấp cơ sở phương pháp luận trực tiếp để xây dựng mô hình thực nghiệm, quy trình thu thập dữ liệu và tiêu chí đánh giá kết quả trong các chương tiếp theo.

## 1.1. Tổng quan về giao thức SMB

### 1.1.1. Khái niệm và vai trò của SMB trong hệ điều hành Windows

Giao thức chia sẻ tài nguyên qua mạng (Server Message Block – SMB) là giao thức truyền thông tầng ứng dụng cho phép máy khách (Client) gửi yêu cầu truy cập tệp, thư mục và các tài nguyên do máy chủ (Server) quản lý. Ngoài chức năng chia sẻ tệp, SMB còn hỗ trợ in ấn qua mạng, xác thực truy cập, khóa tệp và trao đổi dữ liệu liên tiến trình thông qua cơ chế đường ống định danh (Named Pipes) [1]. Trong phạm vi đề tài, các chức năng này được xem xét dựa trên chuỗi tương tác yêu cầu – phản hồi giữa Client và Server trên phân đoạn mạng nội bộ.

Trên hệ điều hành Windows, SMB có thể truyền tải trực tiếp trên giao thức TCP qua cổng 445 (Direct-hosted SMB) hoặc vận hành thông qua lớp bọc NetBIOS over TCP/IP trên cổng TCP 139 [2]. Trạng thái lắng nghe của các cổng mạng là dấu hiệu ban đầu xác định khả năng tiếp cận dịch vụ ở tầng giao vận. Tuy nhiên, việc cổng mở chưa phản ánh cấu hình bên trong; các bước kiểm tra tiếp theo bắt buộc phải xác định phương ngữ SMB được chấp nhận và phản ứng xử lý cụ thể của dịch vụ máy chủ.

### 1.1.2. Mô hình Client – Server

Mô hình hoạt động của SMB dựa trên kiến trúc Client – Server chuẩn mực. Client là thực thể khởi tạo kết nối và gửi yêu cầu truy cập tài nguyên từ xa; Server là thực thể tiếp nhận, xử lý yêu cầu và phản hồi kết quả. Khi một ứng dụng truy cập đường dẫn tài nguyên dùng chung theo định dạng Universal Naming Convention (chẳng hạn `\\Server\Share`), Client bắt đầu tiến trình thiết lập kết nối tới Server [3]. Hai tên gọi này thể hiện vai trò trong phiên giao tiếp giao thức, không đồng nhất với phiên bản hay chủng loại hệ điều hành: một máy trạm Windows hoàn toàn có thể đóng vai trò Server khi mở thư mục chia sẻ, đồng thời đóng vai trò Client khi truy cập tài nguyên của máy tính khác.

Trong quá trình đánh giá an toàn, cần phân định rạch ròi giữa khả năng kết nối mạng tới Server với quyền hạn khai thác một tài nguyên cụ thể. Trạng thái phản hồi của dịch vụ ở tầng mạng, kết quả thiết lập phiên xác thực và quyền hạn truy cập tài nguyên là các lớp thông tin độc lập; đề tài ghi nhận chúng theo từng bước đo đạc chuyên biệt.

```text
Client                                 Server
   |---------- Yêu cầu truy cập ---------->|
   |<--------- Phản hồi xử lý ------------|
   |           Tài nguyên chia sẻ          |
```
*Sơ đồ 1.1: Quan hệ yêu cầu – phản hồi giữa Client và Server trong giao thức SMB.*

### 1.1.3. Phân biệt SMBv1, SMBv2 và SMBv3

Sự phát triển của giao thức SMB qua các thế hệ SMBv1, SMBv2 và SMBv3 phản ánh hai chuyển biến kỹ thuật lớn: tối ưu hóa hiệu năng truyền tải dữ liệu và nâng cấp toàn diện các cơ chế an ninh. Một thế hệ giao thức mới có thể hỗ trợ nhiều tính năng tiên tiến, nhưng việc tính năng đó có thực sự được kích hoạt hay không phụ thuộc hoàn toàn vào kết quả thương lượng cụ thể giữa hai đầu kết nối và chính sách cấu hình của hệ điều hành. Do đó, việc đánh giá an ninh phải căn cứ vào phương ngữ (dialect) thực tế được chấp nhận, thay vì suy đoán dựa trên tên gọi của hệ điều hành [3], [4].

Ở thế hệ SMBv1, phần lớn các thao tác tệp đòi hỏi chuỗi yêu cầu và phản hồi tuần tự riêng lẻ. Khi Client phải chờ phản hồi của từng gói tin trước khi gửi thao tác tiếp theo, độ trễ mạng làm suy giảm đáng kể tốc độ trao đổi dữ liệu. Thế hệ SMBv2 khắc phục hạn chế này bằng cơ chế gộp lệnh (Compounding), cho phép đưa nhiều lệnh liên quan vào trong cùng một thông điệp trao đổi [3]. Chẳng hạn, một chuỗi tác vụ gồm mở tệp, đọc dữ liệu và đóng tệp có thể được gộp lại, giúp giảm thiểu đáng kể số lần bắt tay qua mạng.

Cơ chế ký số gói tin (SMB Signing) và cơ chế mã hóa dữ liệu (SMB Encryption) giải quyết hai bài toán an ninh độc lập. SMB Signing cho phép bên nhận xác thực nguồn gốc và kiểm tra tính toàn vẹn của dữ liệu thông qua chữ ký mật mã được tính toán từ khóa phiên; nếu dữ liệu bị thay đổi trên đường truyền, việc kiểm tra chữ ký sẽ phát hiện sai lệch. Signing bảo vệ tính toàn vẹn nhưng không bảo vệ tính bí mật của nội dung đối với kẻ nghe lén trên đường truyền. Thuật toán ký số tiến hóa từ hàm băm MD5 ở SMBv1, sang HMAC-SHA256 ở SMB 2.0.2 và thuật toán khối AES-CMAC từ SMB 3.0; chuẩn AES-128-GMAC được bổ sung trên các hệ điều hành mới hơn [5]. Trong nghiên cứu này, không áp đặt các đặc tính an ninh của các thế hệ hệ điều hành mới (như mã hóa mặc định hay thuật toán GMAC) cho máy chủ Windows Server 2012 R2 trong mô hình thực nghiệm.

Thế hệ SMBv3 bổ sung tính năng mã hóa toàn diện (SMB Encryption) nhằm bảo vệ tính bí mật của dữ liệu truyền tải mà không cần tới hạ tầng VPN hay IPsec. Microsoft cho phép áp dụng mã hóa linh hoạt ở cấp độ từng thư mục chia sẻ hoặc trên toàn bộ máy chủ [4]. Cơ chế này bảo vệ dữ liệu trên đường truyền, khác hoàn toàn với các giải pháp mã hóa dữ liệu lưu trú trên đĩa cứng như BitLocker hay EFS. Do đó, việc quan sát thấy một hệ thống hỗ trợ SMB 3.x chưa đồng nghĩa với việc kết nối cụ thể đang được mã hóa nếu chính sách máy chủ không bắt buộc.

Đặc biệt, SMB 3.1.1 bổ sung cơ chế kiểm tra tính toàn vẹn trước xác thực (Pre-authentication Integrity), sử dụng hàm băm mật mã SHA-512 trên chuỗi thông điệp thương lượng và thiết lập phiên ban đầu [6]. Giá trị băm này được đưa vào quá trình sinh khóa phiên, giúp ngăn chặn kẻ tấn công trên đường truyền can thiệp để hạ cấp phương ngữ giao thức. Tuy nhiên, theo tài liệu kỹ thuật của Microsoft, cơ chế này chỉ ngăn chặn việc hạ cấp giữa các phương ngữ từ SMB 2.x lên SMB 3.x, không thể bảo vệ nếu kết nối bị ép lùi về giao thức legacy SMBv1 [4]. Vì vậy, việc vô hiệu hóa cấu hình giao thức SMBv1 là biện pháp cần thiết nhằm giảm thiểu bề mặt tiếp xúc của giao thức cũ.

Đối với đề tài này, điểm mấu chốt là xác định liệu máy chủ có chấp nhận kết nối qua SMBv1 hay không. Thông báo bảo mật MS17-010 xử lý các lỗi nghiêm trọng nằm trong chính đoạn mã triển khai của SMBv1 (`srv.sys`); cập nhật bản vá là sửa đổi mã nguồn lỗi bên trong driver, trong khi cấu hình vô hiệu hóa SMBv1 giúp loại bỏ phương ngữ cũ khỏi danh sách thương lượng từ xa [7], [8]. Hai giải pháp tác động vào hai tầng khác nhau, do đó đề tài sử dụng phép đo đạc phương ngữ giao thức độc lập với phép kiểm tra bản vá nội bộ.

*Bảng 1.1: So sánh đặc tính kỹ thuật cơ bản giữa SMBv1, SMBv2 và SMBv3 [3], [4], [5], [8], [6].*

| Đặc tính kỹ thuật | SMBv1 (CIFS) | SMBv2 (2.0.2 / 2.1) | SMBv3 (3.0 / 3.0.2 / 3.1.1) |
|---|---|---|---|
| **Hệ điều hành đại diện** | Windows XP / Windows Server 2003; tồn tại trên Windows 7 / Windows Server 2012 R2 khi bật SMBv1 | Windows Vista / Server 2008 / Windows 7 | Windows 8 / Server 2012 trở lên, tùy dialect (Server 2012 R2 hỗ trợ 3.0 và 3.0.2) |
| **Cơ chế xử lý lệnh** | Tuần tự từng bước | Hỗ trợ gộp lệnh (Compounding) | Gộp lệnh tối ưu |
| **Cổng mạng kết nối** | TCP 139 và TCP 445 | TCP 445 | TCP 445 |
| **Ký số (SMB Signing)** | MD5-based | HMAC-SHA256 | AES-CMAC (3.0 / 3.0.2); GMAC trên một số hệ thống mới hỗ trợ SMB 3.1.1 |
| **Mã hóa dữ liệu** | Không có SMB Encryption tích hợp | Không hỗ trợ | AES-128-CCM (3.0); AES-128-GCM (3.1.1) |
| **Bảo vệ tiền xác thực** | Không hỗ trợ | Không hỗ trợ | Chỉ SMB 3.1.1: Pre-authentication Integrity dùng SHA-512 |
| **Cơ chế bảo vệ nổi bật** | Giao thức legacy, không có encryption tích hợp | Ký số HMAC-SHA256, hỗ trợ gộp lệnh | Mã hóa khối AES và bảo vệ toàn vẹn tùy dialect |

### 1.1.4. Phân tích cổng mạng TCP 139 và TCP 445

Dịch vụ chia sẻ tệp SMB trên hệ điều hành Windows sử dụng hai cổng mạng tiêu chuẩn: TCP 139 và TCP 445. Cổng TCP 139 gắn liền với dịch vụ phiên NetBIOS (NetBIOS Session Service – NBT), đóng vai trò lớp bọc trung gian hỗ trợ phân giải tên và tương thích với các kiến trúc mạng cũ. Ngược lại, cổng TCP 445 cho phép triển khai cơ chế Direct-hosted SMB, truyền tải trực tiếp các gói tin SMB trên nền giao thức TCP/IP mà không phụ thuộc vào tiêu đề NetBIOS [2].

Khi truyền trực tiếp qua cổng TCP 445, thông điệp SMB sử dụng tiêu đề 4 byte chỉ định độ dài dữ liệu trước khi gửi phần thân gói tin. Khi cả hai cơ chế Direct-hosted SMB và NetBIOS over TCP/IP cùng được bật trên máy tính Windows, hệ điều hành sẽ phát song song yêu cầu kết nối tới cả hai cổng 139 và 445; kết nối của cổng nào phản hồi thành công trước sẽ được lựa chọn để thiết lập phiên truyền thông [2].

Trong quy trình đánh giá an toàn thông tin, trạng thái mở (OPEN) của cổng TCP 445 chỉ khẳng định dịch vụ mạng đang lắng nghe ở tầng giao vận và phản hồi gói tin kết nối. Trạng thái này không cấu thành căn cứ chứng minh hệ thống dính lỗ hổng bảo mật (`445 OPEN != vulnerable`). Tương tự, nếu cổng TCP 139 còn mở, hệ thống vẫn duy trì một bề mặt tiếp cận phụ qua NetBIOS. Việc đóng cổng bằng chính sách tường lửa chỉ giới hạn khả năng tiếp cận trên đường truyền chứ không làm thay đổi trạng thái cập nhật phần mềm nội bộ của máy chủ (`FILTERED != PATCHED`).

### 1.1.5. Quy trình trao đổi yêu cầu và phản hồi

Quá trình truy cập một tài nguyên chia sẻ từ xa qua SMB được chuẩn hóa thành ba giai đoạn kế tiếp nhau: thương lượng giao thức (`NEGOTIATE`), thiết lập phiên xác thực (`SESSION_SETUP`) và kết nối tài nguyên chia sẻ (`TREE_CONNECT`) [9]. Việc phân định rõ ba giai đoạn này giúp cô lập chính xác nguyên nhân khi một phép đo kiểm thử không thành công: do không tương thích phương ngữ, thất bại ở khâu xác thực danh tính hay do bị từ chối quyền truy cập tài nguyên.

Trong giai đoạn thương lượng (Negotiate), Client gửi danh sách các phương ngữ mà mình hỗ trợ; Server xem xét và lựa chọn phương ngữ cao nhất mà cả hai bên cùng tương thích. Bước này quyết định cấu trúc gói tin và các thuật toán an ninh sẽ được áp dụng cho toàn bộ phiên truyền thông. Tiếp đó, giai đoạn thiết lập phiên (Session Setup) tiến hành trao đổi thông tin xác thực danh tính người dùng (thường qua giao thức NTLM hoặc Kerberos). Giai đoạn này có thể đòi hỏi nhiều lượt trao đổi dữ liệu, do đó phản hồi mã trạng thái `STATUS_MORE_PROCESSING_REQUIRED` thể hiện tiến trình đang tiếp diễn bình thường chứ không phải xác thực thất bại [9]. Sau khi phiên làm việc được thiết lập, Client gửi yêu cầu kết nối tới tài nguyên chia sẻ cụ thể (`TREE_CONNECT`) để nhận mã định danh tài nguyên (Tree ID – TID) [10].

Trong SMBv1, các định danh được quản lý qua mã User ID (UID) và Tree ID (TID); trong SMBv2/v3, các trường này được chuẩn hóa thành `SessionId` (64-bit) và `TreeId` (32-bit) [9], [10]. Khi phân tích an ninh mạng, việc giải mã đúng các trường định danh này kết hợp với mã trạng thái NT Status là điều kiện tiên quyết để đánh giá tính xác thực của luồng dữ liệu.

Đặc biệt, trong các phép đo an toàn liên quan đến MS17-010, kịch bản kiểm tra từ xa cần hoàn tất bước thương lượng SMBv1 và kết nối thành công tới tài nguyên chia sẻ ngầm `IPC$` (Named Pipe) trước khi có thể gửi gói tin thăm dò nghiệp vụ. Nếu kết nối tới `IPC$` thất bại do chính sách máy chủ chặn xác thực nặc danh (anonymous access), kịch bản quét sẽ không thể thu thập được tín hiệu phản hồi cần thiết; khi đó kết quả ghi nhận phải là không xác định (`UNKNOWN`), tuyệt đối không được suy diễn rằng hệ thống đã an toàn (`UNKNOWN != SAFE`). Ngược lại, việc thiết lập phiên và kết nối `IPC$` thành công chỉ chứng minh dịch vụ cho phép trao đổi dữ liệu ban đầu, hoàn toàn chưa đủ căn cứ để kết luận máy chủ có tồn tại lỗ hổng hay không.

```text
Client                                 Server
   |---------- Thương lượng (Negotiate) ------->|
   |<--------- Phương ngữ được chấp thuận ------|
   |---------- Thiết lập phiên (Session Setup) ->|
   |<--------- Xác thực thành công & SessionId -|
   |---------- Kết nối tài nguyên (Tree Connect)->|
   |<--------- Cấp quyền truy cập & TreeId ------|
```
*Sơ đồ 1.2: Các bước thiết lập giao tiếp SMB trước khi truy cập tài nguyên chia sẻ.*

---

## 1.2. Lỗ hổng bảo mật MS17-010

### 1.2.1. Tổng quan về thông báo bảo mật MS17-010

Vào tháng 03 năm 2017, Microsoft phát hành bản tin bảo mật định kỳ mang mã hiệu **MS17-010** (Microsoft Security Bulletin MS17-010 – Critical) nhằm khắc phục hàng loạt lỗ hổng an ninh đặc biệt nghiêm trọng trong dịch vụ SMBv1 trên hệ điều hành Windows [7]. Nhóm lỗ hổng này ảnh hưởng đến hầu hết các phiên bản Windows đang vận hành tại thời điểm đó, từ các hệ điều hành máy trạm như Windows Vista, Windows 7, Windows 8.1, Windows 10 cho đến các nền tảng máy chủ doanh nghiệp gồm Windows Server 2008, Windows Server 2008 R2, Windows Server 2012, Windows Server 2012 R2 và Windows Server 2016 [7].

Về mặt lý thuyết an toàn thông tin, các lỗ hổng nghiêm trọng nhất trong bản tin MS17-010 cho phép kẻ tấn công thực thi mã từ xa (Remote Code Execution – RCE) thông qua việc gửi các gói tin SMBv1 được cấu tạo đặc biệt tới máy chủ mục tiêu. Do lỗi phát sinh ngay tại tầng xử lý giao thức của driver nhân, việc khai thác trong nhiều trường hợp có thể diễn ra từ xa qua mạng mà không yêu cầu tài khoản xác thực hợp lệ [7]. Tuy nhiên, cần phân biệt rạch ròi giữa nguy cơ lý thuyết và phạm vi nghiên cứu của đồ án: đồ án tập trung vào phương pháp luận khảo sát, nhận diện dấu hiệu dịch vụ và kiểm chứng trạng thái bản vá an toàn, hoàn toàn không thực hiện hành vi khai thác xâm nhập hay thực thi mã trái phép trong mô hình thực nghiệm.

### 1.2.2. Phân loại các mã CVE và danh mục bản vá theo hệ điều hành

Bản tin bảo mật MS17-010 xử lý đồng thời 6 mã định danh lỗ hổng bảo mật (CVE) khác nhau liên quan đến cơ chế xử lý thông điệp của giao thức SMBv1 [7]. Các mã CVE này có sự khác biệt về cơ chế phát sinh lỗi nội bộ và tác động an ninh, như được tổng hợp tại Bảng 1.2.

*Bảng 1.2: Phân loại các mã CVE trong thông báo bảo mật Microsoft MS17-010 [7], [11], [12], [13].*

| Mã CVE | Định danh tham chiếu kỹ thuật | Phân loại theo nguồn chính thức | Tác động an ninh | Vai trò trong nghiên cứu |
|---|---|---|---|---|
| **CVE-2017-0143** | EternalSynergy [11] | SMBv1 Remote Code Execution Vulnerability | Thực thi mã từ xa | Tham chiếu đối sánh kỹ thuật |
| **CVE-2017-0144** | EternalBlue [12] | SMBv1 Remote Code Execution Vulnerability; lỗi xử lý thuộc tính FEA trong `srv.sys` | Thực thi mã từ xa | Đối tượng phân tích cơ chế trọng tâm |
| **CVE-2017-0145** | EternalRomance [13] | SMBv1 Remote Code Execution Vulnerability | Thực thi mã từ xa | Tham chiếu đối sánh kỹ thuật |
| **CVE-2017-0146** | Không gắn tên riêng | SMBv1 Remote Code Execution Vulnerability | Thực thi mã từ xa | Thuộc phạm vi bản tin MS17-010 |
| **CVE-2017-0147** | Không gắn tên riêng | SMBv1 Information Disclosure Vulnerability | Lộ lọt thông tin | Thuộc phạm vi bản tin MS17-010 |
| **CVE-2017-0148** | Không gắn tên riêng | SMBv1 Remote Code Execution Vulnerability | Thực thi mã từ xa | Thuộc phạm vi bản tin MS17-010 |

Để khắc phục nhóm lỗ hổng trên, Microsoft phát hành các gói cập nhật an ninh tương ứng cho từng thế hệ hệ điều hành. Danh mục mã bản vá chính thức được tổng hợp tại Bảng 1.3, trong đó chỉ rõ mã bản vá áp dụng cho môi trường máy chủ mục tiêu của đề tài.

*Bảng 1.3: Danh mục mã bản vá KB chính thức của Microsoft theo hệ điều hành Windows [7], [21].*

| Hệ điều hành | Kiến trúc | Bản vá Security Only | Bản vá Monthly Rollup / Cumulative | Ý nghĩa đối với mô hình nghiên cứu |
|---|---|---|---|---|
| **Windows Server 2012 R2** | x64 | **KB4012213** | **KB4012216** | **Môi trường mục tiêu thực nghiệm của đề tài (srv.sys ngưỡng >= 6.3.9600.18604)** |
| **Windows 8.1** | x86 và x64 | **KB4012213** | **KB4012216** | Nền tảng máy trạm cùng thế hệ kernel với Server 2012 R2 |
| **Windows Server 2012** | x64 | **KB4012214** | **KB4012217** | Phiên bản máy chủ thế hệ Windows 8 |
| **Windows 7 SP1** | x86 và x64 | **KB4012212** | **KB4012215** | Hệ điều hành máy trạm tham chiếu trong tài liệu lịch sử |
| **Windows Server 2008 R2 SP1** | x64 | **KB4012212** | **KB4012215** | Tương đồng mã bản vá với Windows 7 SP1 |
| **Windows 10** | Bản dựng 1507 / 1511 / 1607 | Không áp dụng | **KB4012606** (1507)<br>**KB4013198** (1511)<br>**KB4013429** (1607) | Áp dụng mô hình bản cập nhật tích lũy |
| **Windows Server 2016** | Bản dựng 1607 | Không áp dụng | **KB4013429** | Tương đồng bản vá với Windows 10 Version 1607 |
| **Windows Vista SP2 / Server 2008 SP2** | x86 và x64 | **KB4012598** | Không áp dụng | Bản cập nhật an ninh độc lập |
| **Windows XP SP3 / Server 2003 SP2** | x86 và x64 | **KB4012598** | Không áp dụng | Bản vá khẩn cấp phát hành ngoài chu kỳ hỗ trợ |

### 1.2.3. Cơ chế kỹ thuật của lỗ hổng CVE-2017-0144 và mã khai thác EternalBlue

Lỗ hổng CVE-2017-0144 phát sinh từ sai lệch xử lý danh sách thuộc tính mở rộng của tệp (File Extended Attributes – FEA) trong driver dịch vụ chia sẻ tệp nhân hệ điều hành `srv.sys`. Theo tài liệu phân tích kỹ thuật của Rapid7, hàm chuyển đổi kích thước danh sách `SrvOs2FeaListSizeToNt` tồn tại sự không nhất quán giữa kiểu dữ liệu số nguyên 32-bit (DWORD) và kiểu 16-bit (WORD); hệ quả là hàm chuyển đổi dữ liệu kế tiếp `SrvOs2FeaToNt` thực hiện phép sao chép bộ nhớ `memmove` với kích thước lớn hơn vùng đệm đã được cấp phát, dẫn tới hiện tượng tràn bộ đệm vùng nhớ nhân (Kernel Non-Paged Pool Corruption) [14].

Để làm rõ bản chất cơ chế này về mặt toán học khái niệm, gọi $L_{alloc}$ là dung lượng vùng nhớ được cấp phát trong nhân và $L_{write}$ là khối lượng dữ liệu thực tế được ghi trong quá trình sao chép. Trong điều kiện hoạt động bình thường, hệ điều hành luôn bảo đảm ràng buộc $L_{write} \leq L_{alloc}$. Khi phép tính kích thước bị sai lệch do ép kiểu dữ liệu không an toàn, điều kiện bất thường $L_{write} > L_{alloc}$ xuất hiện, khiến lượng dữ liệu chênh lệch ghi đè lên các cấu trúc dữ liệu liền kề nằm ngoài phạm vi bộ đệm.

Hiện tượng tràn bộ nhớ và việc thực thi mã lệnh là hai bước kỹ thuật hoàn toàn phân biệt. Việc ghi đè ngoài biên bộ nhớ trước hết làm hỏng các cấu trúc dữ liệu nhân của hệ thống; nếu vùng nhớ bị ghi đè không được kiểm soát chặt chẽ, hệ điều hành sẽ phát hiện bất thường và kích hoạt cơ chế dừng khẩn cấp (màn hình xanh chết chóc – BSOD) để bảo vệ tính toàn vẹn phần cứng. Để chuyển hướng dòng thực thi, kỹ thuật khai thác EternalBlue phải kết hợp hiện tượng tràn bộ đệm với kỹ thuật sắp xếp vùng nhớ nhân (Pool Grooming) nhằm bố trí cấu trúc bộ đệm mạng `srvnet` ngay sau vùng đệm bị tràn, từ đó làm thay đổi con trỏ hàm xử lý tại `srvnet!SrvNetWskReceiveComplete` [14].

Về mặt lý thuyết khai thác, nếu mã độc can thiệp thành công vào con trỏ hàm trong không gian nhân, luồng thực thi có thể được điều hướng về vùng nhớ chứa mã tải trọng, từ đó tạo ra tiến trình hoạt động với quyền `SYSTEM` — danh tính bảo mật người dùng có đặc quyền tối cao trong Windows. Cần lưu ý rằng `SYSTEM` / `LocalSystem` là ngữ cảnh bảo mật và tài khoản người dùng có đặc quyền cao trong Windows; việc quan sát một tiến trình thực thi dưới ngữ cảnh bảo mật `SYSTEM` không đồng nghĩa và không tự chứng minh mã lệnh đang thực thi trực tiếp ở chế độ nhân (Kernel Mode). Trong nghiên cứu này, đề tài hoàn toàn không thực hiện chuỗi tấn công can thiệp bộ nhớ hay tạo phiên đặc quyền `SYSTEM` trong phòng thí nghiệm; đề tài chỉ sử dụng lý thuyết FEA để hiểu rõ cơ chế lỗi bên trong của driver `srv.sys`, qua đó giải thích vì sao gói cập nhật của Microsoft xử lý các lỗ hổng thuộc phạm vi bản tin MS17-010.

```text
Sai lệch tính kích thước danh sách FEA (DWORD vs WORD)
                     |
                     v
Cấp phát vùng đệm nhân thiếu dung lượng (L_write > L_alloc)
                     |
                     v
Ghi đè dữ liệu ngoài biên trong hàm SrvOs2FeaToNt
                     |
        +------------+------------+
        |                         |
        v                         v
Lỗi hỏng cấu trúc nhân     Sắp xếp bộ nhớ nhân (Pool Grooming)
        |                         |
        v                         v
Kích hoạt dừng hệ thống    Chuyển hướng thực thi tại srvnet
     (BSOD / Crash)         (Nguy cơ lý thuyết gây RCE)
```
*Sơ đồ 1.3: Sơ đồ hóa cơ chế phát sinh lỗi tràn bộ đệm FEA và các hệ quả an ninh tiềm ẩn.*

### 1.2.4. Điều kiện hệ thống có nguy cơ bị khai thác

Để một máy tính Windows nằm trong diện có nguy cơ đối với lỗ hổng CVE-2017-0144, hệ thống phải đồng thời thỏa mãn các điều kiện kỹ thuật sau đây [7], [12], [14]:

1. **Hệ điều hành thuộc danh mục ảnh hưởng:** Hệ thống vận hành phiên bản Windows nằm trong danh mục công bố của MS17-010 [7]. Trong mô hình thực nghiệm của đề tài, **Windows Server 2012 R2 Standard x64** được lựa chọn làm máy chủ mục tiêu duy nhất vì các căn cứ kỹ thuật rõ ràng:
   - Đây là đối tượng mục tiêu thực nghiệm thực tế được triển khai trong nghiên cứu và thuộc danh mục các hệ điều hành chịu ảnh hưởng trực tiếp của bản tin MS17-010 [7];
   - Microsoft công bố tài liệu hỗ trợ kỹ thuật chính thức quy định cụ thể danh mục bản vá (KB4012213 hoặc KB4012216) và phiên bản tệp nhị phân `srv.sys` tối thiểu đã cập nhật đối với MS17-010 (Article 4023262) [21];
   - Nền tảng này cho phép khảo sát đồng thời cả giao thức SMBv1 và các phương ngữ SMBv2/SMBv3, hỗ trợ kiểm chứng độc lập giữa kết quả thăm dò từ xa và trạng thái bản vá cục bộ.
2. **Tính năng SMBv1 đang được kích hoạt:** Driver nhân `srv.sys` đang hoạt động và dịch vụ `LanmanServer` chấp nhận các phiên làm việc sử dụng giao thức SMBv1 [8].
3. **Cổng dịch vụ có thể tiếp cận qua mạng:** Cổng TCP 445 hoặc TCP 139 ở trạng thái mở (OPEN) và không bị ngăn chặn bởi tường lửa cá nhân hay tường lửa mạng [15].
4. **Hệ thống chưa cài đặt bản vá an ninh MS17-010:** Hệ điều hành chưa được cài đặt gói cập nhật KB4012213 hoặc KB4012216, thể hiện qua việc phiên bản số của driver `srv.sys` thấp hơn phiên bản tối thiểu đã cập nhật đối với MS17-010 do Microsoft quy định [7], [21].
5. **Khả năng thiết lập phiên truyền thông:** Dịch vụ SMB cho phép kết nối mạng và thiết lập phiên làm việc để tiếp cận giao diện xử lý của driver `srv.sys` [7], [12].

**Nguyên tắc phân định ranh giới:** Việc mở cổng 445 hoặc bật tính năng SMBv1 là điều kiện cần về mặt phơi nhiễm dịch vụ, hoàn toàn không đồng nghĩa với việc hệ thống có lỗ hổng (`SMBv1 enabled != MS17-010 confirmed`). Một máy chủ đã cập nhật bản vá tương ứng vẫn mở cổng TCP 445 để phục vụ chia sẻ tệp thông thường; khi đáp ứng tiêu chí phiên bản của Microsoft, hệ thống được phân loại là đã cập nhật đối với các lỗ hổng trong bản tin MS17-010 dù cổng 445 vẫn mở và phương ngữ SMBv1 vẫn được phản hồi [7], [8], [21].

### 1.2.5. Tác động an toàn thông tin

Tác động an toàn của nhóm lỗ hổng MS17-010 được phân tích dựa trên bộ ba thuộc tính an ninh kinh điển: Tính bí mật (Confidentiality), Tính toàn vẹn (Integrity) và Tính sẵn sàng (Availability) của hệ thống:

- **Về tính bí mật:** Nguy cơ phát sinh khi kẻ tấn công lợi dụng việc thực thi mã để truy xuất trái phép dữ liệu nhạy cảm lưu trữ trên máy chủ hoặc đọc trộm thông tin tài khoản quản trị hệ thống.
- **Về tính toàn vẹn:** Nguy cơ xuất hiện khi mã khai thác sửa đổi cấu hình dịch vụ, tiêm mã độc vào các tiến trình hệ thống hoặc phá hủy cấu trúc tệp dữ liệu lưu trữ.
- **Về tính sẵn sàng:** Do lỗi tràn bộ đệm diễn ra trong không gian bộ nhớ nhân (Kernel Pool), sự cố làm hỏng cấu trúc bộ nhớ trong quá trình tấn công có thể dẫn tới lỗi dừng hệ thống (màn hình xanh chết chóc – BSOD), khiến máy chủ mục tiêu bị gián đoạn hoạt động [14]. Vì vậy, tính sẵn sàng là một tác động an ninh quan trọng cần được xem xét trong đánh giá rủi ro.

Nhận thức rõ nguy cơ gây mất ổn định hệ thống, đề tài xây dựng quy trình đánh giá dựa trên các kỹ thuật thăm dò an toàn (safe probe) và đo đạc phản ứng giao thức, tuyệt đối không áp dụng các kỹ thuật can thiệp vùng nhớ nhân trong quá trình kiểm thử.

### 1.2.6. Khái quát các chiến dịch tấn công thực tế liên quan

Sự nguy hiểm của MS17-010 đã được chứng minh qua các sự cố an ninh mạng gây chấn động toàn cầu trong lịch sử:

- **Mã độc tống tiền WannaCry (tháng 05/2017):** Khai thác cơ chế tương tự EternalBlue để tự động quét cổng TCP 445 và phát tán dạng sâu (worm) qua các máy tính Windows chưa cập nhật bản vá; báo cáo của Microsoft ghi nhận sự cố này nhấn mạnh tính cấp thiết của việc áp dụng bản vá MS17-010 và hạn chế kết nối SMB không cần thiết [16].
- **Mã độc NotPetya (tháng 06/2017):** Kết hợp các kỹ thuật lây lan qua giao thức SMB với hành vi phá hủy cấu trúc bản ghi khởi động (MBR) trên các hệ thống Windows chưa được vá lỗi, theo phân tích của Microsoft Threat Intelligence [13].

Các chiến dịch này nhấn mạnh tầm quan trọng cấp thiết của việc xây dựng một quy trình kỹ thuật chuẩn xác nhằm khảo sát bề mặt tiếp xúc của dịch vụ SMB, kiểm tra dấu hiệu lỗ hổng và triển khai các giải pháp phòng thủ đa tầng có kiểm chứng.

---

## 1.3. Công cụ và cơ sở đo đạc thực nghiệm

### 1.3.1. Hệ điều hành kiểm thử Kali Linux

Kali Linux là bản phân phối Linux mã nguồn mở chuyên dụng dựa trên nền tảng Debian, tích hợp sẵn hệ sinh thái các công cụ đánh giá an toàn thông tin và kiểm thử mạng tiêu chuẩn [17]. Trong mô hình thực nghiệm của đề tài, Kali Linux được bố trí đóng vai trò **trạm kiểm thử độc lập (vantage point)**.

Trạm kiểm thử này đảm nhiệm chức năng phát đi các yêu cầu thăm dò mạng, thực thi các kịch bản đánh giá giao thức SMB và ghi nhận toàn bộ phản hồi từ xa dưới dạng các tệp nhật ký nguyên bản (`.nmap`, `.xml`). Việc sử dụng Kali Linux trong phân đoạn mạng thử nghiệm bảo đảm tính nhất quán của môi trường phát sinh lưu lượng kiểm thử và tạo điều kiện tái lập chính xác các phép đo.

### 1.3.2. Công cụ quét mạng Nmap

Nmap (Network Mapper) là công cụ quét mạng chuẩn mực trong nghiên cứu an toàn thông tin, đóng vai trò phương tiện thu thập dữ liệu chính ở các tầng giao vận và ứng dụng [18]. Trong đề tài, Nmap được triển khai qua hai chế độ đo đạc cốt lõi:

1. **Quét cổng TCP SYN (`-sS`):** Kỹ thuật quét bán mở gửi gói tin TCP SYN tới cổng đích. Nếu nhận được phản hồi `SYN-ACK`, cổng được ghi nhận ở trạng thái mở (`open`); nếu nhận phản hồi `RST`, cổng ở trạng thái đóng (`closed`); nếu không có phản hồi sau các lượt gửi lại hoặc nhận mã lỗi ICMP, cổng được phân loại là bị lọc (`filtered`) [18]. Trạng thái `open` trên hai cổng TCP 139 và 445 là chỉ dấu kỹ thuật xác nhận dịch vụ đang tiếp nhận kết nối giao vận từ trạm kiểm thử.
2. **Thăm dò phiên bản dịch vụ (`-sV`):** Nmap gửi các gói tin thăm dò ở tầng ứng dụng và đối chiếu dữ liệu phản hồi với cơ sở dữ liệu mẫu nhận dạng (service fingerprints) [18]. Đối với cổng TCP 445, Nmap trả về chuỗi định danh dịch vụ và khoảng phiên bản hệ điều hành ước lượng (chẳng hạn `Windows Server 2008 R2 - 2012`). Kết quả này chỉ cung cấp khoảng dấu vết phiên bản từ xa, chưa đủ căn cứ để định danh duy nhất bản phát hành Windows Server 2012 R2 nếu không có dữ liệu đối chiếu nội bộ.

### 1.3.3. Tự động hóa kiểm tra an toàn với Nmap Scripting Engine (NSE)

Nmap Scripting Engine (NSE) mở rộng khả năng đo đạc của Nmap thông qua các kịch bản viết bằng ngôn ngữ Lua [18]. Đề tài khai thác hai kịch bản NSE chính phục vụ đánh giá SMB:

- **Kịch bản `smb-protocols.nse`:** Gửi yêu cầu thương lượng giao thức chứa danh sách các phương ngữ từ cổ điển đến hiện đại, sau đó phân tích phản hồi của máy chủ để trích xuất toàn bộ các phương ngữ được chấp nhận [20]. Việc xuất hiện phương ngữ `NT LM 0.12` xác thực bề mặt SMBv1 vẫn đang tồn tại trên máy chủ.
- **Kịch bản `smb-vuln-ms17-010.nse`:** Thuộc nhóm kịch bản an toàn (`safe`) và kiểm tra lỗ hổng (`vuln`), được thiết kế để phát hiện dấu hiệu chưa cập nhật bản vá MS17-010 thông qua việc đo đạc phản ứng xử lý thông điệp hợp lệ của dịch vụ từ xa [19]. Cần lưu ý rằng kịch bản này là một công cụ nhận diện từ xa đối với thông báo bảo mật MS17-010 nói chung; trong phần siêu dữ liệu và kết quả xuất, kịch bản gắn định danh tham chiếu với mã CVE-2017-0143 [19]. Do đó, kết quả từ kịch bản này phản ánh tín hiệu phát hiện từ xa của công cụ quét, không tự cấu thành bằng chứng chứng minh trực tiếp khả năng khai thác thành công lỗ hổng CVE-2017-0144 hay kỹ thuật EternalBlue trên máy chủ mục tiêu.

Cơ chế vận hành của kịch bản `smb-vuln-ms17-010` diễn ra theo ba bước kỹ thuật chặt chẽ [19]:
1. Kịch bản kết nối tới cổng SMB mục tiêu, thương lượng phương ngữ SMBv1, thực hiện bắt tay Session Setup và kết nối tới tài nguyên chia sẻ ngầm `\\Target\IPC$`.
2. Sau khi có quyền truy cập `IPC$`, kịch bản gửi một thông điệp giao dịch `SMB_COM_TRANSACTION` (opcode `0x25`) với lệnh nghiệp vụ `PeekNamedPipe` (mã hàm `0x2300`) trên đường ống định danh `\PIPE\`, thiết lập các tham số đệm tối đa (`Max Parameter Count = 0xFFFF`, `Max Data Count = 0xFFFF`).
3. **Phân tích mã trạng thái phản hồi NT Status:**
   - *Dấu hiệu phù hợp hệ thống chưa vá (`VULNERABLE`):* Nếu máy chủ phản hồi mã lỗi `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`), phản hồi này trùng khớp với hành vi của driver `srv.sys` nguyên bản chưa được vá lỗi khi xử lý tham số bộ đệm bất thường. Kịch bản ghi nhận dấu hiệu này và xuất trạng thái `State: VULNERABLE` [19].
   - *Dấu hiệu phù hợp hệ thống đã vá:* Nếu máy chủ phản hồi mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc `STATUS_INVALID_HANDLE` (`0xC0000008`), mã nguồn kịch bản ghi nhận trạng thái là có khả năng đã được vá (`likely patched`) và xuất chuỗi thông báo `This system is patched` [19].

**Giới hạn kỹ thuật và nguyên tắc suy luận:** Về mặt lý thuyết kỹ thuật, tiến trình thực thi kịch bản có thể không thu được phản hồi thăm dò tại các giai đoạn khác nhau của luồng kết nối (như gián đoạn kết nối mạng, không thiết lập được phiên tới `IPC$`, hoặc không nhận được gói phản hồi). Khi không có gói tin phản hồi hợp lệ cho phép thăm dò `PeekNamedPipe`, kịch bản kết thúc mà không sinh ra kết luận khẳng định đã vá hay chưa vá, dẫn tới trạng thái **không xác định (`UNKNOWN / NO USABLE SCRIPT RESULT`)** [19]. Cần lưu ý rằng trong mô hình thực nghiệm của đề tài, việc kịch bản không xuất kết quả đánh giá lỗ hổng được ghi nhận nguyên trạng dưới dạng không có kết luận khả dụng mà không tự ý gán cho một nguyên nhân suy diễn cụ thể nào. Đề tài bảo toàn nghiêm ngặt nguyên tắc: **`UNKNOWN != SAFE`**. Trạng thái không có kết quả từ công cụ quét chỉ thể hiện việc thiếu dữ liệu quan sát từ xa, tuyệt đối không được suy diễn thành bằng chứng máy chủ an toàn hay đã được cập nhật bản vá.

### 1.3.4. Cơ sở xác minh trạng thái bản vá cục bộ trên Windows Server 2012 R2

Các kỹ thuật quét mạng từ xa chỉ ghi nhận phản ứng bên ngoài của dịch vụ qua đường truyền, do đó dễ bị tác động bởi cấu hình mạng, tường lửa hoặc chính sách phân quyền tài nguyên. Để có căn cứ khoa học vững chắc, đánh giá an toàn thông tin bắt buộc phải đối chiếu tín hiệu từ xa với **trạng thái bản vá nội bộ (Local Patch State)** được kiểm tra trực tiếp trên hệ điều hành máy chủ mục tiêu.

Theo tài liệu chỉ dẫn kỹ thuật chính thức của Microsoft Support (Article 4023262 – "How to verify that MS17-010 is installed") [21], quy trình xác minh trạng thái bản vá cho nền tảng Windows Server 2012 R2 được thực hiện qua hai phương pháp độc lập:

1. **Phương pháp rà soát danh mục Hotfix:** Sử dụng lệnh quản trị PowerShell `Get-HotFix` để kiểm tra các gói cập nhật hệ thống đã được cài đặt. Đối với Windows Server 2012 R2, bản vá khắc phục MS17-010 được phát hành chính thức qua hai mã định danh:
   - Bản cập nhật chỉ bảo mật (Security Only Quality Update): `KB4012213`;
   - Bản cập nhật tích lũy hàng tháng (Monthly Rollup): `KB4012216` [7], [21].
   Sự hiện diện của ít nhất một trong hai mã KB này (hoặc các bản cập nhật tích lũy thay thế định kỳ trong các tháng tiếp theo) là minh chứng hệ thống đã tiếp nhận gói sửa lỗi từ nhà sản xuất.
2. **Phương pháp đối chiếu phiên bản nhị phân của driver `srv.sys`:** Tệp driver dịch vụ chia sẻ tệp `srv.sys` đặt tại thư mục `C:\Windows\System32\drivers\srv.sys` là nơi trực tiếp chứa đoạn mã bị lỗi. Chuỗi phiên bản hiển thị (`FileVersion`) trên giao diện đồ họa (thường hiển thị chuỗi RTM bản dựng gốc như `6.3.9600.16384`) không thể hiện đầy đủ giá trị sửa đổi nhị phân. Quy trình chuẩn xác đòi hỏi trích xuất 4 trường số nguyên cấu thành phiên bản nhị phân của tệp gồm: `FileMajorPart`, `FileMinorPart`, `FileBuildPart` và `FilePrivatePart`. Theo tài liệu chỉ dẫn kỹ thuật Article 4023262 của Microsoft, đối với Windows Server 2012 R2, **phiên bản tệp `srv.sys` tối thiểu đã cập nhật đối với MS17-010** là **`6.3.9600.18604`** [21]. Bất kỳ máy chủ nào có phiên bản số thực tế thấp hơn giá trị tối thiểu này (chẳng hạn bản gốc RTM `6.3.9600.16384`) đều được phân loại là **chưa cập nhật bản vá (`UNPATCHED`) đối với MS17-010**.

Việc xác định trạng thái bản vá cục bộ tạo thành một **trục bằng chứng độc lập** với tín hiệu quét từ xa: nó phản ánh cấu trúc mã nhị phân lưu trữ trên đĩa cứng của máy chủ mục tiêu, không chịu ảnh hưởng bởi cấu hình tường lửa hay trạng thái cổng mạng. Một hệ thống chưa vá (`UNPATCHED`) vẫn có thể trả về trạng thái quét từ xa là `UNKNOWN` nếu đường truyền bị gián đoạn; ngược lại, việc công cụ quét từ xa không phát hiện dấu hiệu chưa chứng minh được máy chủ đã đạt tiêu chí phiên bản cập nhật đối với MS17-010 của Microsoft.

### 1.3.5. Liên kết cơ sở lý thuyết và các phép đo thực nghiệm lab

Để chuẩn bị phương pháp luận cho việc thiết kế mô hình thực nghiệm trong Chương 2, Sơ đồ 1.4 chuẩn hóa quy trình đo đạc 4 pha kế tiếp nhau, trong khi Bảng 1.4 thiết lập mối liên kết chặt chẽ giữa các khái niệm lý thuyết với biến số đo đạc thực tế, phương pháp thực hiện và ranh giới diễn giải an ninh tương ứng.

```text
[ Pha 1: Khảo sát mạng & cổng ] ──> Nmap (-p 139,445 -sS) ──> Tiếp cận tầng giao vận
                 │
                 ▼
[ Pha 2: Bề mặt giao thức SMB ] ──> NSE (smb-protocols) ────> Nhận diện SMBv1 & dialect
                 │
                 ▼
[ Pha 3: Thăm dò dấu hiệu từ xa] ──> NSE (smb-vuln-ms17-010) -> Đo phản ứng NT Status
                 │
                 ▼
[ Pha 4: Xác minh bản vá nội bộ] ──> PowerShell (srv.sys/KB) ─> Đối chiếu phiên bản cập nhật tối thiểu
```
*Sơ đồ 1.4: Quy trình 4 pha đo đạc và xác minh an toàn dịch vụ SMB.*

*Bảng 1.4: Đối chiếu giữa cơ sở lý thuyết và các phép đo thực nghiệm trong lab.*

| Thành phần lý thuyết | Biến số kỹ thuật quan sát | Phương pháp đo đạc trong lab | Ý nghĩa kỹ thuật thu được | Ranh giới diễn giải (Không được suy diễn) |
|---|---|---|---|---|
| **Khả năng tiếp cận dịch vụ** | Trạng thái mở cổng TCP 139 và TCP 445 | Nmap quét TCP SYN (`-sS -p 139,445`) | Cổng lắng nghe và phản hồi gói tin kết nối mạng | Cổng mở không đồng nghĩa với có lỗ hổng (`445 OPEN != vulnerable`) |
| **Bề mặt phương ngữ SMB** | Danh sách các dialect được Server chấp thuận | Nmap NSE `smb-protocols` | Xác định Server có tiếp nhận phương ngữ SMBv1 (`NT LM 0.12`) hay không | Bật SMBv1 không chứng minh dính MS17-010 (`SMBv1 enabled != MS17-010 confirmed`) |
| **Chính sách ký số gói tin** | Trạng thái bắt buộc ký số (Signing policy) | Nmap NSE `smb2-security-mode` | Xác định mức độ thực thi ký số trên các phiên kết nối | Ký số bảo vệ tính toàn vẹn, không thay thế cho bản vá lỗ hổng |
| **Dấu hiệu lỗ hổng từ xa** | Mã lỗi NT Status phản hồi từ lệnh `PeekNamedPipe` | Nmap NSE `smb-vuln-ms17-010` | Đo đạc phản ứng xử lý thông điệp trên `IPC$` | Nếu không có output, kết quả là `UNKNOWN`; không được coi là an toàn (`UNKNOWN != SAFE`) |
| **Trạng thái bản vá nội bộ** | Danh mục Hotfix và phiên bản nhị phân `srv.sys` | Truy vấn PowerShell (`Get-HotFix`, FileVersionInfo) | Đối chiếu với phiên bản tệp `srv.sys` tối thiểu đã cập nhật đối với MS17-010 ($\geq 6.3.9600.18604$) | Trạng thái `UNPATCHED` nội bộ độc lập với việc máy quét từ xa có đọc được kết quả hay không |
| **Giảm thiểu mức giao thức** | Bề mặt thương lượng SMB sau khi cấu hình tắt SMBv1 | Cấu hình PowerShell máy chủ; đo lại qua `smb-protocols` | Xác nhận phương ngữ SMBv1 (`NT LM 0.12`) không còn xuất hiện trong danh sách thương lượng | Tắt SMBv1 giảm bề mặt giao thức đo đạc nhưng không đồng nhất với gỡ tính năng Windows và không làm thay đổi phiên bản driver nhân (`SMBv1 disabled != PATCHED`) |
| **Giảm thiểu mức mạng** | Khả năng tiếp cận dịch vụ qua đường truyền mạng | Thiết lập chính sách lọc gói tin; đo lại qua Nmap | Hạn chế khả năng tiếp cận dịch vụ đối với lưu lượng đi qua đường truyền được kiểm soát; kết quả quan sát cụ thể được trình bày ở Chương 3 | Lọc mạng không tác động tới lưu lượng ngoài đường truyền kiểm soát và không làm thay đổi trạng thái bản vá nội bộ (`FILTERED != PATCHED`) |
| **Tái kiểm thử (Retest)** | Sự biến đổi của các biến số đo đạc trước và sau | Chạy lại toàn bộ chuỗi phép đo Nmap/NSE chuẩn hóa | Đánh giá sự thay đổi của các biến số kỹ thuật mục tiêu được lựa chọn | Xác minh sự biến đổi của các biến số được đo, không cấp chứng nhận an toàn toàn diện và không tự chứng minh mọi tải công việc đều hoạt động liên tục |

---

## 1.4. Cơ sở đánh giá trạng thái và nguyên tắc phòng thủ

### 1.4.1. Mô hình bốn trục bằng chứng trong đánh giá dịch vụ SMB và lỗ hổng

Một thiếu sót phổ biến trong các quy trình kiểm thử an ninh truyền thống là việc sắp xếp các phép đo theo thang bậc tuyến tính tăng dần kết thúc bằng hành vi khai thác xâm nhập. Cách tiếp cận này tạo ra ngộ nhận rằng việc kiểm thử bắt buộc phải dẫn tới việc chiếm quyền điều khiển hệ thống, đồng thời che lấp mối quan hệ độc lập giữa các nguồn dữ liệu kỹ thuật.

Để khắc phục hạn chế trên, đề tài đề xuất **Mô hình bốn trục bằng chứng độc lập (Four-Axis Evidence Model)**. Thay vì coi các kết quả là các nấc thang phụ thuộc lẫn nhau, mô hình xem xét bốn nguồn dữ liệu kỹ thuật có ranh giới và phương pháp thu thập độc lập, được trình bày chi tiết tại Bảng 1.5.

*Bảng 1.5: Khung phân định bốn trục bằng chứng độc lập trong đánh giá dịch vụ SMB.*

| Trục bằng chứng | Đối tượng quan sát kỹ thuật | Nguồn dữ liệu và công cụ | Câu hỏi an ninh được trả lời | Ranh giới kết luận bắt buộc |
|---|---|---|---|---|
| **Trục 1: Tiếp cận tầng mạng (Reachability)** | Trạng thái mở của cổng TCP 139 và 445 | Quét TCP SYN từ xa (`Nmap -sS`) | Gói tin từ trạm kiểm thử có tới được dịch vụ lắng nghe trên máy chủ hay không? | **`445 OPEN != vulnerable`**. Mở cổng chỉ là điều kiện kết nối tầng giao vận. |
| **Trục 2: Bề mặt giao thức (Protocol Surface)** | Danh sách phương ngữ SMB và trạng thái ký số | Nmap NSE `smb-protocols`, `smb2-security-mode` | Máy chủ có chấp nhận trao đổi dữ liệu qua phương ngữ legacy SMBv1 hay không? | **`SMBv1 enabled != MS17-010 confirmed`**. Bật SMBv1 chỉ mở bề mặt giao thức, chưa chứng minh có lỗi. |
| **Trục 3: Tín hiệu từ xa (Scanner Signal)** | Phản ứng mã lỗi NT Status trước gói tin thăm dò | Nmap NSE `smb-vuln-ms17-010` | Dịch vụ có phản hồi mã lỗi đặc trưng của nhánh xử lý chưa vá hay không? | **`UNKNOWN != SAFE`**. Không có tín hiệu phản hồi không đồng nghĩa với hệ thống an toàn. |
| **Trục 4: Bản vá nội bộ (Local Patch State)** | Danh mục Hotfix và phiên bản số driver `srv.sys` | Kiểm tra nội bộ máy chủ qua lệnh PowerShell | Hệ điều hành đã cài gói vá và driver nhân đã đạt phiên bản tối thiểu đã cập nhật đối với MS17-010 hay chưa? | **Local `UNPATCHED` không tự biến remote `UNKNOWN` thành `VULNERABLE`**. Hai trục độc lập. |

Sự phân tách bốn trục bằng chứng này bảo đảm mọi kết luận trong báo cáo đều gắn liền với một nguồn dữ liệu có kiểm chứng, ngăn chặn việc suy diễn vượt quá giới hạn quan sát của công cụ.

### 1.4.2. Giới hạn kỹ thuật và phòng ngừa kết quả sai lệch

Trong quá trình đo đạc thực nghiệm, các sai lệch đánh giá có thể phát sinh từ hai nguồn chính: **lỗi thu thập dữ liệu (collection failure)** và **lỗi diễn giải kết quả (interpretation error)**.

Lỗi thu thập dữ liệu xuất hiện khi tiến trình đo đạc bị gián đoạn giữa chừng do điều kiện môi trường: kết nối mạng bị rớt gói, thời gian chờ vượt ngưỡng (timeout), tường lửa lọc gói tin không phản hồi, hoặc dịch vụ máy chủ từ chối kết nối tới chia sẻ ngầm `IPC$`. Khi đó, công cụ quét mạng không thu thập được gói tin phản hồi của phép thăm dò; đây là tình trạng thiếu thông tin quan sát chứ không phải kết quả âm tính. Người đánh giá nếu không phân biệt được sự khác nhau giữa "không nhận được phản hồi" (no usable output) và "kết quả âm tính theo tiêu chí của phép đo" (negative result) sẽ dễ dàng đưa ra phán quyết sai lệch nghiêm trọng.

Lỗi diễn giải kết quả xuất hiện khi người đánh giá đồng nhất các khái niệm kỹ thuật khác loại: coi việc mở cổng mạng là hệ thống dính lỗ hổng, coi việc tắt phương ngữ cũ là đã cập nhật mã nguồn driver, hoặc sử dụng kết quả kiểm tra bản vá nội bộ để khẳng định một công cụ quét từ xa phải trả về kết quả tương ứng.

Để ngăn ngừa các sai lệch trên, nghiên cứu áp dụng nguyên tắc đối chiếu chéo đa nguồn độc lập. Mỗi quan sát mạng từ xa phải được đặt trong mối tương quan với cấu hình phân đoạn mạng và chính sách tường lửa; đồng thời trạng thái an ninh của máy chủ phải được khẳng định thông qua dữ liệu kiểm tra nội bộ đã được kiểm chứng.

### 1.4.3. Nguyên tắc giảm thiểu rủi ro và phòng thủ giao thức SMB

Dựa trên cơ sở lý thuyết về đường truyền tấn công và bề mặt dịch vụ, các giải pháp phòng thủ an ninh đối với dịch vụ SMB được phân định thành ba **tầng kiểm soát (Control Layers)** độc lập, mỗi tầng có cơ chế tác động và phạm vi hiệu lực riêng biệt:

1. **Tầng cập nhật hệ thống (Patching Layer):**
   - *Cơ chế tác động:* Cài đặt gói cập nhật an ninh chính thức từ Microsoft (KB4012213 hoặc KB4012216) để thay thế tệp driver nhân `srv.sys` cũ bằng phiên bản mới đã được sửa đổi (đạt phiên bản tối thiểu đã cập nhật đối với MS17-010 là $\geq 6.3.9600.18604$ [21]).
   - *Đặc điểm kỹ thuật:* Gói cập nhật của Microsoft xử lý các lỗ hổng được công bố trong bản tin MS17-010. Hệ thống đáp ứng tiêu chí kiểm tra của Microsoft được phân loại là đã cập nhật đối với MS17-010. Tuy nhiên, việc cập nhật driver này không đồng nghĩa với một bảo đảm an toàn tuyệt đối cho toàn bộ hệ thống trước mọi nguy cơ tiềm ẩn khác.
   - *Ranh giới trong nghiên cứu:* Trong phạm vi đồ án, giải pháp cập nhật bản vá đóng vai trò mốc tham chiếu đối chiếu lý thuyết; mô hình thực nghiệm tập trung đo đạc và đánh giá hai giải pháp giảm thiểu vận hành (Case B và Case C) nhằm giải quyết bài toán thực tế khi hệ thống chưa thể cập nhật bản vá ngay lập tức.
2. **Tầng giảm thiểu mức giao thức (Protocol Hardening Layer – Case B):**
   - *Cơ chế tác động:* Vô hiệu hóa cấu hình giao thức SMBv1 trên dịch vụ máy chủ thông qua câu lệnh cấu hình quản trị `Set-SmbServerConfiguration -EnableSMB1Protocol $false` [8].
   - *Đặc điểm kỹ thuật:* Biện pháp này làm giảm bề mặt giao thức của dịch vụ máy chủ; trên luồng đo đạc thực nghiệm, phương ngữ `NT LM 0.12` không còn xuất hiện trong danh sách phương ngữ được máy chủ thương lượng. Cần phân biệt rõ: việc tắt cấu hình giao thức máy chủ (`EnableSMB1Protocol = $false`) khác với việc gỡ bỏ hoàn toàn gói tính năng Windows (`FS-SMB1 uninstalled`).
   - *Ranh giới kỹ thuật:* Đề tài bảo toàn hai ranh giới kỹ thuật cốt lõi: **`SMBv1 disabled != FS-SMB1 uninstalled`** và **`SMBv1 disabled != PATCHED`** (biện pháp cấu hình này không làm thay đổi phiên bản tệp `srv.sys` trên đĩa cứng). Ngoài ra, việc thay đổi giao thức có thể ảnh hưởng tới các thiết bị hoặc ứng dụng đời cũ chỉ hỗ trợ phương ngữ SMBv1.
3. **Tầng kiểm soát truy cập mạng (Network Access Control Layer – Case C):**
   - *Cơ chế tác động:* Thiết lập chính sách tường lửa lọc gói tin tại ranh giới mạng (dựa trên các nguyên tắc phân định tường lửa chuẩn mực như NIST SP 800-41 Rev. 1 [15]) để ngăn chặn lưu lượng hướng tới cổng TCP 139 và 445 trên đường truyền kiểm soát.
   - *Đặc điểm kỹ thuật:* Biện pháp này giới hạn khả năng tiếp cận dịch vụ SMB đối với các luồng lưu lượng đi qua thiết bị kiểm soát. Kết quả đo đạc trạng thái cổng cụ thể của trạm kiểm thử sẽ được trình bày và phân tích chi tiết trong Chương 3.
   - *Ranh giới kỹ thuật:* Lọc mạng chỉ kiểm soát các luồng lưu lượng đi qua đường truyền có đặt chính sách tường lửa; các luồng dữ liệu không đi qua thiết bị kiểm soát nằm ngoài phạm vi tác động của biện pháp này. Đồng thời, việc lọc gói tin ở tầng mạng không làm thay đổi trạng thái bản vá nội bộ của máy chủ (**`FILTERED != PATCHED`**).
4. **Nguyên tắc tái kiểm thử chuẩn hóa (Retest Principle):**
   - Về mặt thực hành quản trị vận hành, việc kiểm thử khả năng tương thích của các ứng dụng sau khi thay đổi giao thức là một khuyến nghị cần thiết. Tuy nhiên, trong phạm vi mô hình thực nghiệm của đề tài, phép đo đạc lại (retest) trong Case B tập trung kiểm chứng sự thay đổi của các biến số kỹ thuật đã xác định trước (xác nhận `NT LM 0.12` không còn xuất hiện trong danh sách dialect được quan sát và ghi nhận phản hồi của kịch bản kiểm tra). Việc quan sát thấy các phương ngữ SMBv2/SMBv3 còn lại không đồng nghĩa với việc chứng minh toàn bộ các tải công việc nghiệp vụ trong thực tế đều hoạt động liên tục không gián đoạn. Tái kiểm thử chỉ xác thực sự thay đổi của các biến số đo đạc cụ thể, không cấp chứng nhận an toàn toàn diện cho hệ thống.

---

## TỔNG KẾT CHƯƠNG 1

Chương 1 đã thiết lập toàn diện cơ sở lý thuyết về kiến trúc giao thức SMB, cơ chế phát sinh lỗi tràn bộ nhớ nhân của nhóm lỗ hổng MS17-010, cùng các phương pháp đo đạc kỹ thuật bằng công cụ Nmap, kịch bản NSE và thủ tục kiểm tra bản vá nội bộ trên nền tảng Windows Server 2012 R2.

Thông qua việc phân tích sâu các cơ chế tương tác tầng mạng và hành vi của hệ điều hành, chương này đã thiết lập **Mô hình bốn trục bằng chứng độc lập**: khả năng tiếp cận tầng mạng (TCP 139/445), bề mặt giao thức SMB (dialects/signing), tín hiệu thăm dò từ xa (Nmap NSE) và trạng thái bản vá nội bộ (Hotfix/srv.sys). Việc phân tách rạch ròi bốn trục bằng chứng này cùng các nguyên tắc suy luận then chốt (`445 OPEN != vulnerable`, `SMBv1 enabled != MS17-010 confirmed`, `UNKNOWN != SAFE`, `FILTERED != PATCHED`) loại bỏ hoàn toàn các nhận định suy diễn cảm tính và đặt nền móng phương pháp luận vững chắc cho việc thiết kế mô hình thực nghiệm, kịch bản đo đạc và tiêu chí đánh giá kết quả trong Chương 2.

---

## TÀI LIỆU THAM KHẢO

[1] Microsoft, "What is Microsoft SMB Protocol and CIFS Protocol?," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview

[2] Microsoft, "Direct hosting of SMB over TCP/IP," Microsoft Learn, 2026. [Online]. Available: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/direct-hosting-of-smb-over-tcpip

[3] Microsoft, "What is SMB File Sharing for Windows and Windows Server?," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview

[4] Microsoft, "SMB security enhancements," Microsoft Learn, Jul. 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security

[5] Microsoft, "What is Server Message Block signing?," Microsoft Learn, Oct. 2024. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-signing-overview. [Accessed: Oct. 4, 2026].

[6] Microsoft, "SMB 3.1.1 Pre-authentication integrity in Windows 10," Microsoft Learn, archived Open Specifications blog. [Online]. Available: https://learn.microsoft.com/en-us/archive/blogs/openspecification/smb-3-1-1-pre-authentication-integrity-in-windows-10. [Accessed: Oct. 4, 2026].

[7] Microsoft, "Microsoft Security Bulletin MS17-010 - Critical," Microsoft Learn / Security TechCenter, Mar. 2017. [Online]. Available: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010

[8] Microsoft, "Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3

[9] Microsoft, "[MS-SMB2]: Server Message Block (SMB) Protocol Versions 2 and 3," Microsoft Open Specifications, 2026. [Online]. Available: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-smb2/

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

[21] Microsoft Support, "How to verify that MS17-010 is installed," Microsoft Support, Article 4023262, 2017. [Online]. Available: https://support.microsoft.com/en-us/security/how-to-verify-that-ms17-010-is-installed
