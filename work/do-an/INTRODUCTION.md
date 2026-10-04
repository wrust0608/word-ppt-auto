# MỞ ĐẦU

## 1. Lý do chọn đề tài

Giao thức chia sẻ tài nguyên qua mạng (Server Message Block – SMB) là giao thức truyền thông tiêu chuẩn ở tầng ứng dụng trên hệ điều hành Windows. Giao thức này cung cấp các dịch vụ nền tảng bao gồm chia sẻ tệp tin, điều phối máy in và truyền thông liên tiến trình (Inter-Process Communication – IPC) thông qua đường ống định danh (Named Pipes). Do đóng vai trò cốt lõi trong hạ tầng quản trị, các thành phần xử lý dịch vụ SMB được thiết kế vận hành trực tiếp trong không gian nhân hệ điều hành (Kernel Mode). Trình điều khiển `srv.sys` chịu trách nhiệm xử lý SMBv1 và `srv2.sys` xử lý các thế hệ SMBv2 cùng SMBv3.

Mặc dù Microsoft đã liên tục phát triển các phiên bản SMBv2 và SMBv3 với nhiều cơ chế mật mã bảo vệ, phiên bản cũ SMBv1 (CIFS) vẫn tồn tại phổ biến trong nhiều hạ tầng mạng nội bộ. Việc duy trì SMBv1 chủ yếu xuất phát từ nhu cầu tương thích ngược với các thiết bị ngoại vi đời cũ như máy in mạng, máy quét tài liệu hoặc thiết bị lưu trữ NAS. Bề mặt tấn công của SMBv1 đặc biệt nguy hiểm do giao thức này được thiết kế từ thập niên 1980. Ở thời điểm đó, các cơ chế mã hóa kênh truyền và bảo vệ tính toàn vẹn thông điệp hiện đại chưa được tích hợp.

Vào tháng 03 năm 2017, Microsoft phát hành bản tin an ninh định kỳ MS17-010 nhằm khắc phục một nhóm gồm 6 lỗ hổng nghiêm trọng trong trình điều khiển `srv.sys` [1]. Trong nhóm này, lỗ hổng thực thi mã từ xa CVE-2017-0144 trở thành tâm điểm đe dọa khi bị vũ khí hóa bởi mã khai thác EternalBlue [2]. Lỗ hổng cho phép kẻ tấn công gửi các gói tin giao dịch SMBv1 được chế tạo đặc biệt qua cổng TCP 445 hoặc TCP 139. Thao tác này kích hoạt lỗi tràn vùng đệm bộ nhớ nhân (Kernel Pool Overflow) để thực thi mã tùy ý với đặc quyền `NT AUTHORITY\SYSTEM` mà không cần thông tin xác thực [1], [2].

Thảm họa an ninh mạng bùng phát qua chiến dịch mã độc tống tiền WannaCry vào tháng 05 năm 2017 đã chứng minh tính chất nguy hiểm của lỗ hổng này [3]. Bằng cách tích hợp mã khai thác EternalBlue vào cơ chế sâu mạng tự động lây lan, WannaCry đã quét và xâm nhập hàng trăm nghìn hệ thống Windows chưa được vá lỗi trên toàn cầu [3]. Nhiều cơ sở y tế, ngân hàng và mạng viễn thông trọng yếu bị gián đoạn hoạt động. Ngay sau đó, chiến dịch mã độc NotPetya tiếp tục lợi dụng nhóm lỗ hổng MS17-010 để lây lan ngang trong các hệ thống doanh nghiệp, gây thiệt hại nghiêm trọng [1], [3].

Trong thực tế quản trị, nhiều tổ chức vẫn gặp khó khăn khi phân định ranh giới kỹ thuật. Một sai lầm phổ biến là đồng nhất trạng thái mở cổng mạng TCP 445 hoặc bật SMBv1 với việc hệ thống chắc chắn tồn tại lỗ hổng MS17-010 [4]. Đồng thời, các quy trình kiểm thử hiện nay thường thiếu khung kiểm soát rủi ro, dễ dẫn đến hiện tượng treo cứng máy chủ hoặc sập hệ điều hành (lỗi màn hình xanh BSOD) khi tương tác với bộ nhớ nhân. Ngoài ra, việc triển khai phòng vệ đa tầng cũng đặt ra bài toán xung đột gay gắt giữa yêu cầu siết chặt an ninh và nhu cầu duy trì tính tương thích nghiệp vụ [4].

Xuất phát từ những yêu cầu thực tiễn trên, đề tài **“Xây dựng mô hình kiểm thử lỗ hổng SMB trên Windows bằng Kali Linux”** được triển khai nghiên cứu. Đề tài tập trung hệ thống hóa kiến trúc giao thức, làm rõ bản chất kỹ thuật của lỗ hổng MS17-010, thiết lập quy trình kiểm thử an toàn trong lab cô lập và đề xuất chiến lược phòng thủ đa tầng có đối chứng.

## 2. Mục tiêu nghiên cứu

### 2.1. Mục tiêu tổng quát

Nghiên cứu cơ sở lý thuyết và kiến trúc phân tầng của giao thức SMB trên Windows. Phân tích nguyên nhân gốc rễ và cơ chế lỗi bộ nhớ nhân của nhóm lỗ hổng MS17-010 với trọng tâm là CVE-2017-0144. Thiết kế và xây dựng mô hình phòng thí nghiệm mạng ảo cô lập nhằm chuẩn hóa quy trình kiểm thử an ninh có kiểm soát rủi ro. Đề xuất và phân tích chiến lược phòng thủ đa tầng nhằm triệt tiêu nguy cơ khai thác mà vẫn bảo đảm tính tương thích nghiệp vụ của hệ thống.

### 2.2. Mục tiêu kỹ thuật cụ thể

Để đạt được mục tiêu tổng quát, đề tài xác lập 4 mục tiêu kỹ thuật cụ thể tương ứng với các câu hỏi nghiên cứu của đồ án:

1. **Mục tiêu 1 (O1):** Hệ thống hóa kiến trúc giao thức SMB trên Windows. Phân định cơ chế truyền tải qua cổng TCP 445 (Direct-hosted SMB) và TCP 139 (NetBIOS over TCP/IP). Làm rõ chuỗi máy trạng thái giao thức gồm thương lượng dialect, thiết lập phiên và liên kết tài nguyên qua Named Pipes trên tài nguyên chia sẻ `IPC$`. So sánh đối chiếu kiến trúc và đặc tính an ninh giữa SMBv1, SMBv2 và SMBv3.
2. **Mục tiêu 2 (O2):** Làm rõ cơ chế kỹ thuật của nhóm lỗ hổng MS17-010 và mã khai thác EternalBlue. Phân tích lỗi cắt ngắn số nguyên khi xử lý thuộc tính mở rộng tệp tin (FEA) trong hàm `SrvOs2FeaListSizeToNt`, dẫn tới tràn vùng đệm Non-Paged Pool trong hàm `SrvOs2FeaToNt` của trình điều khiển `srv.sys`. Phân tích kỹ thuật dàn xếp bộ nhớ nhân (Kernel Pool Grooming) và nguy cơ gây sập hệ thống (BSOD).
3. **Mục tiêu 3 (O3):** Thiết kế kiến trúc phòng thí nghiệm mạng ảo cô lập gồm 3 phân vùng mạng (VLAN) định tuyến qua tường lửa. Xây dựng thang đo nhận thức luận 4 cấp độ thẩm định an ninh SMB. Chuẩn hóa quy trình kiểm thử có kiểm soát sử dụng Kali Linux, Nmap, kịch bản NSE và nền tảng Metasploit Framework.
4. **Mục tiêu 4 (O4):** Xây dựng và đánh giá chiến lược phòng thủ đa tầng gồm cập nhật bản vá nhị phân (KB), vô hiệu hóa hoàn toàn SMBv1, kiểm soát tường lửa và phân đoạn mạng. Phân tích bài toán cân bằng giữa bảo mật và tính tương thích nghiệp vụ đối với các thiết bị mạng đời cũ.

## 3. Đối tượng và phạm vi nghiên cứu

### 3.1. Đối tượng nghiên cứu

Đối tượng nghiên cứu của đề tài bao gồm các thành phần công nghệ và công cụ kỹ thuật sau:
- Giao thức truyền thông Server Message Block (các thế hệ SMBv1/CIFS, SMBv2 và SMBv3) cùng các dịch vụ liên quan trên hệ điều hành Windows.
- Nhóm lỗ hổng an ninh MS17-010 trong trình điều khiển nhân `srv.sys`, trọng tâm là lỗ hổng thực thi mã từ xa CVE-2017-0144 và cơ chế hoạt động của mã khai thác EternalBlue.
- Hệ thống công cụ trinh sát mạng và kiểm thử an ninh chuyên dụng: hệ điều hành Kali Linux, công cụ quét mạng Nmap, kịch bản Nmap Scripting Engine (`smb-protocols.nse`, `smb-vuln-ms17-010.nse`) và nền tảng kiểm thử xâm nhập Metasploit Framework.
- Các cơ chế phòng thủ mạng và hệ điều hành: gói cập nhật bản vá nhị phân Microsoft Knowledge Base (KB), chính sách vô hiệu hóa SMBv1 qua PowerShell/Registry/GPO, cấu hình tường lửa Windows Firewall và giải pháp phân đoạn mạng (VLAN).

### 3.2. Phạm vi nghiên cứu

Phạm vi nghiên cứu của đề tài được giới hạn trong các điều kiện kỹ thuật sau:
- **Phạm vi không gian thực nghiệm:** Mọi hoạt động khảo sát, quét mạng, thăm dò dấu hiệu và kiểm thử xâm nhập chỉ triển khai trong phòng thí nghiệm ảo hóa cô lập (sử dụng VMware Workstation / VirtualBox). Môi trường lab được cấu hình mạng nội bộ không kết nối Internet. Máy chủ mục tiêu đại diện là Windows 7 SP1 x64 (phiên bản thuộc diện ảnh hưởng tiêu biểu của MS17-010) và máy trạm kiểm thử là Kali Linux.
- **Phạm vi nội dung và phương pháp:** Tập trung nghiên cứu cơ chế giao thức, nguyên nhân lỗ hổng ở cấp độ nhân, thiết kế kiến trúc lab an toàn, chuẩn hóa quy trình nhận diện dịch vụ và xây dựng ma trận đối chứng trước – sau phòng thủ.
- **Ranh giới loại trừ (Out of Scope):** Đề tài không thực hiện quét mạng, thăm dò hoặc khai thác trên các hệ thống thông tin thực tế ngoài phòng thí nghiệm. Không phát tán mã khai thác ra mạng thực. Đề tài tuân thủ chỉ thị chưa đưa kết quả demo, log hoặc ảnh chụp thực nghiệm thực tế vào giai đoạn báo cáo hiện tại; phần đo lường sẽ hoàn thiện ở các giai đoạn sau.

## 4. Phương pháp tiếp cận và quy trình nghiên cứu

### 4.1. Phương pháp tiếp cận

Đề tài kết hợp đồng bộ các phương pháp tiếp cận kỹ thuật sau nhằm bảo đảm tính khoa học và chuẩn xác:
- **Phương pháp phân tích tài liệu kỹ thuật chuẩn:** Nghiên cứu các tài liệu đặc tả giao thức chính thức của Microsoft ([MS-SMB], [MS-SMB2], [MS-CIFS]), các bản tin an ninh (MS17-010), cơ sở dữ liệu NIST NVD (CVE-2017-0144) và hướng dẫn an ninh Microsoft Learn [1], [2], [4].
- **Phương pháp mô phỏng thực nghiệm trên môi trường ảo hóa:** Xây dựng mô hình lab mạng ảo độc lập nhằm quan sát trực quan các hành vi giao thức, bắt giữ lưu lượng mạng và đối chiếu các phản hồi kỹ thuật.
- **Phương pháp kiểm thử an ninh mạng theo chuẩn có kiểm soát:** Áp dụng phương pháp luận kiểm thử kỹ thuật theo tiêu chuẩn NIST SP 800-115 [5]. Phương pháp kết hợp quan sát mạng từ xa (Black-box) với việc kiểm tra đối chiếu cấu hình nội tại của hệ điều hành (White-box).
- **Phương pháp so sánh và đối chứng kỹ thuật:** Đánh giá hiệu lực của các biện pháp bảo vệ thông qua việc so sánh trạng thái an ninh của máy chủ mục tiêu trước và sau khi áp dụng từng lớp phòng thủ theo các tiêu chí chuẩn hóa [6].

### 4.2. Quy trình nghiên cứu

Đề tài được tổ chức thực hiện theo quy trình 5 bước tuần tự:
- **Bước 1 – Khảo sát nền tảng lý thuyết và thu thập tài liệu:** Thu thập và nghiên cứu các tài liệu chuẩn về giao thức SMB. Phân tích cơ chế truyền tải qua cổng TCP 445/139 và tổng hợp thông tin về nhóm lỗ hổng MS17-010.
- **Bước 2 – Thiết kế kiến trúc lab và xây dựng tiêu chí thẩm định:** Thiết lập sơ đồ mạng lab 3 VLAN cô lập, phân hoạch địa chỉ IP tĩnh, chuẩn bị máy ảo mục tiêu và máy kiểm thử, đồng thời xây dựng thang đo 4 cấp độ thẩm định an ninh.
- **Bước 3 – Xây dựng kịch bản kiểm thử có kiểm soát:** Chuẩn hóa quy trình kiểm thử 4 giai đoạn sử dụng Nmap, NSE script và Metasploit Framework. Mục tiêu là phân định rạch ròi giữa việc mở cổng, hỗ trợ SMBv1, dấu hiệu chưa vá và khả năng khai thác thực tế.
- **Bước 4 – Thiết lập giải pháp phòng thủ đa tầng:** Nghiên cứu và thử nghiệm quy trình cập nhật bản vá KB, vô hiệu hóa hoàn toàn SMBv1, cấu hình quy tắc tường lửa lọc cổng dịch vụ và thiết lập chính sách phân đoạn mạng cách ly.
- **Bước 5 – Đánh giá rủi ro, phân tích tương thích và tổng kết:** Đánh giá mức độ tổn hại an toàn thông tin theo tam giác CIA. Phân tích bài toán tương thích thiết bị ngoại vi và hoàn thiện toàn văn báo cáo đồ án.

## 5. Nguyên tắc an toàn và giới hạn kiểm thử

### 5.1. Cam kết đạo đức nghề nghiệp và tuân thủ pháp lý

Mọi hoạt động nghiên cứu và kiểm thử an ninh trong đề tài đều thực hiện trên tinh thần học thuật nghiêm túc, tuân thủ pháp luật hiện hành và chuẩn mực đạo đức:
- Tuân thủ Luật An toàn thông tin mạng số 86/2015/QH13 của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam. Nghiêm cấm phát tán mã độc, xâm nhập trái phép hoặc gây gián đoạn hệ thống thông tin.
- Chấp hành đầy đủ quy chế đào tạo, nội quy phòng thực hành của Khoa Công nghệ Thông tin – Trường Đại học Công Thương TP. Hồ Chí Minh (HUIT) và đề cương đã được phê duyệt.
- Mọi hoạt động kiểm thử chỉ nhằm nâng cao nhận thức và làm rõ cơ chế tấn công để xây dựng giải pháp phòng thủ. Tuyệt đối không sử dụng công cụ nghiên cứu vào các hành vi gây hại hay xâm phạm quyền riêng tư.

### 5.2. Nguyên tắc cô lập mạng tuyệt đối

Nhằm triệt tiêu rủi ro rò rỉ lưu lượng kiểm thử ra môi trường thực tế, hệ thống phòng thí nghiệm bắt buộc tuân thủ nguyên tắc cách ly mạng:
- Toàn bộ máy ảo tham gia mô hình thực nghiệm (Kali Linux, Windows mục tiêu, máy trạm đối chứng) chỉ liên kết qua các phân vùng mạng ảo nội bộ (Host-only Network hoặc Internal Network).
- Tuyệt đối không sử dụng chế độ card mạng cầu nối (Bridged Adapter) để tránh việc máy ảo nhận địa chỉ IP từ mạng thực của nhà trường hoặc nhà cung cấp dịch vụ mạng.
- Ngắt hoàn toàn kết nối Internet và các cổng giao tiếp vật lý ra bên ngoài trên các máy ảo mục tiêu trong suốt quá trình kiểm thử.

### 5.3. Nguyên tắc kiểm soát tác động và sao lưu trạng thái tức thời (Snapshot)

Do cơ chế khai thác lỗ hổng CVE-2017-0144 can thiệp trực tiếp vào bộ nhớ nhân (Non-Paged Pool), quá trình kiểm thử tiềm ẩn nguy cơ cao gây lỗi hỏng bộ đệm và làm sập hệ điều hành:
- Trước khi kích hoạt bất kỳ công cụ thăm dò hoặc mô-đun khai thác nào, người kiểm thử bắt buộc phải chụp lại ảnh nhanh trạng thái (snapshot) của toàn bộ máy ảo.
- Khi xuất hiện sự cố dừng hệ thống (lỗi màn hình xanh BSOD), tiến trình kiểm thử phải tạm dừng ngay. Hệ thống được khôi phục về snapshot sạch đã lưu trước đó để đưa dịch vụ trở lại ổn định.
- Không tiến hành lặp lại các phép thử can thiệp bộ nhớ khi chưa xác định rõ nguyên nhân sai lệch, nhằm bảo toàn tính toàn vẹn của môi trường thực nghiệm.

### 5.4. Nguyên tắc dừng kiểm thử khẩn cấp

Quy trình kiểm thử quy định các điều kiện kích hoạt việc dừng khẩn cấp:
- Dừng ngay lập tức toàn bộ các tác vụ quét mạng và khai thác khi phát hiện lưu lượng mạng có dấu hiệu truyền nhận ra ngoài dải địa chỉ IP nội bộ của lab.
- Dừng kiểm thử khi phát hiện hành vi bất thường của phần mềm ảo hóa hoặc hiện tượng quá tải phần cứng trên máy chủ vật lý.
- Dừng kiểm thử và báo cáo kịp thời xin ý kiến hướng dẫn của Giảng viên khi xuất hiện bất kỳ tình huống kỹ thuật nào vượt ra ngoài phạm vi kịch bản đã phê duyệt.

### 5.5. Giới hạn kiểm thử

Đề tài xác lập các giới hạn kiểm thử khách quan sau:
- Thử nghiệm chỉ tiến hành trên các phiên bản hệ điều hành máy ảo đại diện (Windows 7 SP1 x64) thuộc phạm vi cấp phép; không triển khai trên các hệ thống đang vận hành nghiệp vụ thực tế.
- Đề tài không sáng tác hay giả mạo các dữ liệu log, số liệu đo lường hoặc kết quả khai thác. Các số liệu thực nghiệm thực tế sẽ được triển khai và ghi nhận đầy đủ, trung thực ở các giai đoạn tiếp theo.

## 6. Ý nghĩa khoa học và giá trị thực tiễn

### 6.1. Ý nghĩa khoa học

- **Hệ thống hóa lý thuyết giao thức an ninh mạng:** Đề tài làm sáng tỏ kiến trúc phân tầng, chuỗi máy trạng thái giao dịch và ranh giới an ninh giữa ba thế hệ giao thức SMBv1, SMBv2 và SMBv3. Nghiên cứu chỉ ra các điểm yếu cấu trúc cố hữu của giao thức legacy trong việc duy trì an toàn dữ liệu.
- **Làm rõ cơ chế lỗi bộ nhớ cấp nhân:** Đề tài phân tích nguyên nhân gốc rễ của lỗ hổng CVE-2017-0144 ở mức độ mã nguồn và bộ nhớ nhân. Nghiên cứu làm rõ mối liên hệ giữa lỗi cắt ngắn số nguyên trong chuyển đổi FEA với kỹ thuật dàn xếp Non-Paged Pool và chiếm quyền điều khiển luồng thực thi CPU.
- **Đóng góp về phương pháp luận đánh giá an ninh:** Đề tài xác lập khung thang đo nhận thức luận 4 cấp độ thẩm định trạng thái SMB. Khung này cung cấp cơ sở khoa học để phân định rạch ròi giữa việc mở cổng mạng, chấp thuận phương ngữ giao thức, dấu hiệu mã lỗi phản hồi từ nhân và khả năng thực thi mã thực tế, giúp loại bỏ các kết luận suy diễn thiếu căn cứ.

### 6.2. Giá trị thực tiễn

- **Cung cấp quy trình kiểm thử an toàn cho quản trị viên:** Tài liệu hóa quy trình trinh sát và thẩm định an ninh dịch vụ SMB chuẩn hóa, có thể lặp lại và kiểm soát rủi ro. Kết quả này hỗ trợ chuyên viên an toàn thông tin và quản trị viên mạng đánh giá chính xác bề mặt tấn công của hạ tầng Windows.
- **Hướng dẫn nhận diện và giải mã dấu hiệu kỹ thuật:** Làm rõ ý nghĩa của các mã trạng thái phản hồi NT Status trong kịch bản Nmap NSE và Metasploit. Tài liệu giúp người quản trị phân biệt chính xác giữa máy chủ đã được vá an toàn với các trường hợp bị chặn kết nối nặc danh tới tài nguyên `IPC$`.
- **Đề xuất chiến lược phòng thủ đa tầng khả thi:** Đưa ra giải pháp phòng thủ theo chiều sâu ba tầng và phương án phân đoạn mạng cách ly (Legacy VLAN) thiết thực. Giải pháp này giải quyết hài hòa bài toán xung đột giữa việc nâng cao an toàn thông tin và việc bảo đảm tính liên tục của các dịch vụ nghiệp vụ sử dụng thiết bị cũ.

## 7. Bố cục của báo cáo

Báo cáo đồ án chuyên ngành được tổ chức kết cấu thành 4 chương nội dung chính cùng phần Mở đầu, Kết luận và Kiến nghị:

- **Mở đầu:** Trình bày lý do chọn đề tài, mục tiêu nghiên cứu, đối tượng và phạm vi nghiên cứu. Nội dung cũng bao gồm phương pháp tiếp cận, quy trình thực hiện, nguyên tắc an toàn, ý nghĩa khoa học, giá trị thực tiễn và bố cục tổng thể của báo cáo.
- **Chương 1 – Cơ sở lý thuyết và công cụ kiểm thử SMB:** Trình bày kiến trúc giao thức SMB, cơ chế truyền tải qua cổng TCP 139/445, chuỗi máy trạng thái giao dịch, so sánh đối chiếu SMBv1-v3. Giải phẫu bản chất kỹ thuật của nhóm lỗ hổng MS17-010 và lỗi nhân CVE-2017-0144. Giới thiệu bộ công cụ Kali Linux, Nmap, NSE, Metasploit. Thiết lập thang đo 4 cấp độ thẩm định và chiến lược phòng thủ đa tầng.
- **Chương 2 – Thiết kế và triển khai mô hình thực nghiệm:** Trình bày thiết kế kiến trúc lab ảo hóa cô lập (mô hình 3 phân vùng mạng VLAN định tuyến qua tường lửa). Trình bày thông số cấu hình các máy ảo (Kali Linux, Windows 7 Target, Client đối chứng), phân bổ dải địa chỉ IP tĩnh, cơ chế snapshot khôi phục, và kịch bản kiểm thử có kiểm soát theo 4 trạng thái đơn biến.
- **Chương 3 – Thực nghiệm kiểm thử SMB:** Trình bày quy trình và phương pháp luận triển khai thực nghiệm chi tiết theo từng bước. Các bước gồm quét cổng, nhận diện phương ngữ SMB, thăm dò dấu hiệu lỗi qua kịch bản NSE và thẩm định xâm nhập có kiểm soát trong lab cô lập.
- **Chương 4 – Đánh giá kết quả, phân tích rủi ro và khuyến nghị:** Phân tích, tổng hợp và đối chiếu kết quả trạng thái an ninh trước và sau khi áp dụng các biện pháp phòng vệ (vá lỗi KB, tắt SMBv1, cấu hình tường lửa và phân đoạn mạng). Đánh giá rủi ro theo tam giác CIA. Phân tích bài toán tương thích và đề xuất danh mục khuyến nghị bảo mật đa tầng cho hạ tầng doanh nghiệp.
- **Kết luận và kiến nghị:** Tổng kết các kết quả chính đã đạt được so với mục tiêu đề ra, chỉ rõ những mặt hạn chế của đề tài và vạch ra định hướng nghiên cứu, phát triển tiếp theo.
- **Tài liệu tham khảo:** Danh mục các tài liệu học thuật, tiêu chuẩn kỹ thuật quốc tế và tài liệu công cụ được trích dẫn theo chuẩn IEEE.

---

## TÀI LIỆU THAM KHẢO

[1] Microsoft, "Microsoft Security Bulletin MS17-010 – Critical," Microsoft Learn / Security TechCenter, Mar. 2017. [Online]. Available: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010

[2] National Institute of Standards and Technology (NIST), "CVE-2017-0144 Detail," National Vulnerability Database (NVD), Mar. 2017. [Online]. Available: https://nvd.nist.gov/vuln/detail/CVE-2017-0144

[3] Microsoft Threat Intelligence, "WannaCrypt ransomware worm targets out-of-date systems," Microsoft Security Blog, May 2017. [Online]. Available: https://www.microsoft.com/en-us/security/blog/2017/05/12/wannacrypt-ransomware-worm-targets-out-of-date-systems/

[4] Microsoft Learn, "Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows," Microsoft Learn, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3

[5] National Institute of Standards and Technology (NIST), "Technical Guide to Information Security Testing and Assessment," NIST Special Publication 800-115, 2008. [Online]. Available: https://csrc.nist.gov/pubs/sp/800/115/final

[6] National Institute of Standards and Technology (NIST), "Guidelines on Firewalls and Firewall Policy," NIST Special Publication 800-41 Rev. 1, 2009. [Online]. Available: https://csrc.nist.gov/pubs/sp/800/41/r1/final
