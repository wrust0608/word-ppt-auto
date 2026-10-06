# BÁO CÁO LỰA CHỌN VÀ ĐÁNH GIÁ HÌNH ẢNH MỤC 3.1 BASELINE (CH3_31_BASELINE_FIGURE_SELECTION_R1)

- **Trạng thái:** `R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7A0 R2 — Correct Baseline Evidence & Presentation Plan`
- **Phạm vi thẩm tra:** Toàn bộ 13 tệp ảnh chụp màn hình đã stage tại `work/do-an/chapter3/evidence/baseline/`
- **Nguyên tắc cốt lõi:**
  1. **Chống lạm dụng ảnh chụp màn hình (Anti-Screenshot Spam):** Chỉ giữ ảnh (`KEEP`) khi và chỉ khi ảnh đó trực tiếp chứng minh một thuộc tính kỹ thuật có giá trị mà bảng tổng hợp hoặc văn xuôi không thể truyền tải một cách thuyết phục bằng chứng thị giác.
  2. **Bảo tồn tính toàn vẹn bằng chứng:** Tuyệt đối không chỉnh sửa tệp ảnh gốc. Mọi đề xuất cắt cúp (`crop`) chỉ nhằm tối ưu hóa việc trình bày bố cục bản in, giữ nguyên ngữ cảnh kỹ thuật trọng yếu.
  3. **Ưu tiên bảng biểu:** Dữ liệu cấu hình hệ điều hành, tham số mạng và danh mục bản vá được ưu tiên đưa vào Bảng 3.1 và Bảng 3.2.
  4. **Chính sách cắt cúp không khóa tọa độ cứng (Non-rigid crop policy):** Trong pha lập kế hoạch R2, không khóa cứng tọa độ pixel; chỉ mô tả vùng thông tin cần giữ, vùng giao diện thừa có thể loại bỏ, ngữ cảnh bắt buộc bảo tồn và mục đích trình bày.

---

## 1. Bảng Đánh Giá Chi Tiết Toàn Bộ 13 Ảnh Chụp Màn Hình Mốc Xuất Phát

| Tệp ảnh gốc (File) | Nội dung hiển thị trực tiếp (Directly shows) | Thông tin độc bản? (Unique info?) | Bảng có thể thay thế? (Table can replace?) | Độ sắc nét & Bố cục (Legibility) | Cần cắt cúp? (Crop needed?) | Phân loại (KEEP / OPTIONAL / DROP) | Đề xuất sử dụng (Proposed use) |
|---|---|---|---|---|---|---|---|
| `Kali_PreDemo_01_Network_Tools.png` | Cửa sổ terminal Kali: `ip address` (192.168.56.10/24), `ip route` (192.168.56.0/24), `nmap --version` (7.99), tạo thư mục `evidence/nse-smb` | Không. Đây là thông số môi trường cơ bản của trạm kiểm thử | Có. Bảng 3.1 trình bày IP, routing và phiên bản Nmap gọn gàng hơn | Tốt (1280x800), nhưng nền desktop xanh chiếm phần lớn diện tích | Có (cắt cửa sổ terminal nếu dùng) | **DROP** | Loại bỏ. Toàn bộ tham số mạng Kali được tích hợp trọn vẹn vào Bảng 3.1. |
| `Kali_PreDemo_02_NSE_Scripts.png` | Trợ giúp tĩnh của Nmap (`nmap --script-help`) cho `smb-protocols` và `smb-vuln-ms17-010` | Không. Chỉ là văn bản tài liệu trợ giúp có sẵn của Nmap | Có. Trích dẫn tài liệu chuẩn hoặc ghi chú nguồn | Tốt, chữ sắc nét | Không | **DROP** | Loại bỏ. Không phản ánh trạng thái thực nghiệm của môi trường lab. |
| `Kali_to_Windows_Connectivity.png` | Kiểm tra kết nối từ Kali tới Windows: hai yêu cầu ICMP Echo không nhận được phản hồi (100% packet loss), kèm `ip neigh` xác nhận ARP `192.168.56.20 lladdr 08:00:27:55:71:ce REACHABLE` | Có một phần. Chứng minh trạng thái láng giềng ARP L2 là REACHABLE trong khi hai gói ICMP không có phản hồi | Có. Bảng 3.1 có thể ghi nhận hoặc lược bỏ để tập trung vào dữ liệu quét cổng | Tốt, chữ rõ ràng | Có (cắt riêng cửa sổ dòng lệnh) | **OPTIONAL** | Ảnh dự phòng. Giữ làm ảnh tùy chọn nếu cần minh chứng trạng thái láng giềng L2 giữa hai máy trước khi quét; không đưa vào kế hoạch chính để tránh gán nguyên nhân thiếu căn cứ. |
| `Windows_Baseline_01_Winver.png` | Hộp thoại About Windows: Windows Server 2012 R2 Standard Evaluation, Version 6.3 (Build 9600) trên nền Server Manager | Không. Chỉ là hộp thoại nhận diện phiên bản hệ điều hành cơ bản | Có. Bảng 3.1 công bố phiên bản hệ điều hành và số Build chuẩn xác | Tốt, giao diện sắc nét | Có (cắt hộp thoại Winver) | **DROP** | Loại bỏ. Hộp thoại Windows cơ bản không cung cấp giá trị kỹ thuật sâu về an ninh. |
| `Windows_Baseline_04_SMB_Service.png` | PowerShell: `Get-Service LanmanServer` hiển thị Name: LanmanServer, Status: Running | Không. Thông tin đơn lẻ, bị trùng lặp | Có. Hoàn toàn tích hợp vào Bảng 3.1 | Kém. Cửa sổ hẹp, nhiều khoảng trống đen, cột StartType bị che khuất | Không | **DROP** | Loại bỏ. Bố cục kém và bị thay thế hoàn toàn bởi ảnh kiểm toán tổng hợp `Windows_PreDemo_01_Network_SMB.png`. |
| `Windows_Baseline_05_SMB_Features.png` | PowerShell: `Get-WindowsFeature FS-SMB1` hiển thị trạng thái `[X] Installed` | Không. Chỉ thể hiện một thuộc tính cài đặt tính năng | Có. Tích hợp vào Bảng 3.1 | Trung bình. Quá ít thông tin trên diện tích ảnh lớn | Không | **DROP** | Loại bỏ. Mật độ thông tin thấp, được tích hợp trong ảnh tổng hợp. |
| `Windows_Baseline_06_SMB_Config.png` | PowerShell: `Get-SmbServerConfiguration` hiển thị EnableSMB1Protocol=True, EnableSMB2Protocol=True, SecuritySignature=False | Không. Bị trùng lặp | Có. Tích hợp vào Bảng 3.1 | Trung bình. Cửa sổ đen chiếm diện tích lớn | Không | **DROP** | Loại bỏ. Trùng lặp hoàn toàn với dữ liệu cấu hình trong Bảng 3.1 và ảnh tổng hợp. |
| `Windows_Baseline_07_Firewall.png` | PowerShell: Profiles Domain/Private/Public True, 4 luật File and Printer Sharing đầu tiên False | Không. Hiển thị bị cắt cụt tên luật hiển thị (DisplayName) | Có. Tích hợp vào Bảng 3.1 | Kém. Tên luật bị ẩn, không đủ thông tin kết luận | Không | **DROP** | Loại bỏ. Bị thay thế hoàn toàn bởi `Windows_PreDemo_02_Firewall.png`. |
| `Windows_FirewallPrep_04_Scope.png` | PowerShell: Profiles Enabled=True, 16 luật File and Printer Sharing đều False, cổng 139 và 445 đang Listen | Có một phần. Chứng minh trạng thái cổng lắng nghe và luật mặc định bị tắt | Có. Bảng 3.1 trình bày mạch lạc hơn | Khá tốt. Nửa màn hình trái | Có (cắt cửa sổ PowerShell) | **OPTIONAL** | Ảnh dự phòng. Có thể dùng nếu cần minh chứng bổ trợ về cổng 139/445 đang Listen cục bộ trên Windows. |
| `Windows_MS17010_01_SrvSysVersion.png` | PowerShell: 1) FileVersion String `6.3.9600.16384 (winblue_rtm.130821-1623)`; 2) Trích xuất phiên bản số nhị phân `$vi.FileMajorPart...` = `6.3.9600.16421` | Cao. Minh chứng sự khác biệt kỹ thuật giữa chuỗi hiển thị và phiên bản số nhị phân của `srv.sys` | Có thể đối chiếu trong Bảng 3.2 | Rất cao. Chữ trắng trên nền xanh PowerShell rất sắc nét | Có | **OPTIONAL** | Ảnh dự phòng. Chuyển sang OPTIONAL vì ảnh `Windows_MS17010_02_Hotfix.png` (Hình 3.3) đã chứa toàn bộ thông tin phiên bản srv.sys này kèm thêm danh mục kiểm kê hotfix. |
| `Windows_MS17010_02_Hotfix.png` | PowerShell: Chuỗi FileVersion hiển thị, trích xuất phiên bản số nhị phân `6.3.9600.16421`, và lệnh `Get-HotFix` hiển thị 6 bản vá hệ thống từ ngày 21/03/2014 | **CỰC KỲ CAO (HỢP NHẤT)**. Tập hợp đầy đủ cả thuộc tính phiên bản driver `srv.sys` và danh mục bản vá thực tế trên một màn hình duy nhất | Bảng 3.2 đối chiếu số liệu, nhưng ảnh này là bằng chứng thị giác trực tiếp nguyên gốc mạnh nhất cho trạng thái bản vá | Rất tốt. Cửa sổ PowerShell rõ ràng; thông báo Action Center ở góc phải taskbar có thể loại bỏ bằng crop | **CÓ** (cắt bỏ thanh taskbar) | **KEEP (ƯU TIÊN 3)** | **Hình 3.3 (Tạm thời)**. Minh chứng thuộc tính phiên bản driver `srv.sys` và danh mục bản vá ghi nhận trên máy chủ mục tiêu. |
| `Windows_PreDemo_01_Network_SMB.png` | PowerShell: Hợp nhất kiểm toán toàn diện gồm IP Ethernet 192.168.56.20, routing, LanmanServer Running, FS-SMB1 Installed, cờ SMB server, cổng lắng nghe 139/445 và phiên bản số srv.sys 6.3.9600.16421 | **RẤT CAO (HỢP NHẤT)**. Cung cấp cái nhìn trực quan tổng thể về cấu hình mạng, dịch vụ chia sẻ tệp và các cổng đang lắng nghe cục bộ | Bảng 3.1 tổng hợp thông số, nhưng ảnh này là minh chứng trực tiếp không thể thiếu cho cấu hình dịch vụ trước thử nghiệm | Tốt. Cửa sổ hiển thị tuần tự các khối lệnh kiểm toán | **CÓ** (cắt bỏ phần desktop Server Manager trống) | **KEEP (ƯU TIÊN 1)** | **Hình 3.1 (Tạm thời)**. Minh chứng trạng thái mạng, dịch vụ SMB và các cổng lắng nghe trên máy chủ trước thực nghiệm. |
| `Windows_PreDemo_02_Firewall.png` | PowerShell: Cấu hình quy tắc tường lửa tùy biến `ATTT Lab SMB 139-445` (Inbound Allow, TCP 139/445, RemoteAddress duy nhất `192.168.56.10`), 3 profile True, 16 luật chia sẻ tệp mặc định False | **RẤT CAO**. Chứng minh quy tắc kiểm soát chủ động giới hạn phạm vi nguồn truy cập SMB từ trạm Kali theo cấu hình quan sát được | Bảng 3.1 tóm tắt, nhưng ảnh này là bằng chứng thị giác thuyết phục nhất về thiết lập quy tắc tường lửa tùy biến | Rất cao. Các khối lệnh phân chia rõ ràng, không có khoảng trống thừa | **CÓ** (cắt bỏ phần Server Manager nền) | **KEEP (ƯU TIÊN 2)** | **Hình 3.2 (Tạm thời)**. Minh chứng cấu hình quy tắc tường lửa tùy biến kiểm soát phạm vi nguồn truy cập dịch vụ SMB. |

---

## 2. Tổng Hợp Phân Loại Và Đề Xuất Bộ Hình Ảnh R2

### 2.1. Thống Kê Phân Loại
- **Tổng số ảnh đã thẩm tra:** 13 ảnh.
- **Số lượng KEEP (Giữ lại):** 3 ảnh (`Windows_PreDemo_01_Network_SMB.png`, `Windows_PreDemo_02_Firewall.png`, `Windows_MS17010_02_Hotfix.png`).
- **Số lượng OPTIONAL (Dự phòng):** 3 ảnh (`Windows_MS17010_01_SrvSysVersion.png`, `Kali_to_Windows_Connectivity.png`, `Windows_FirewallPrep_04_Scope.png`).
- **Số lượng DROP (Loại bỏ):** 7 ảnh (`Kali_PreDemo_01`, `Kali_PreDemo_02`, `Windows_Baseline_01`, `Windows_Baseline_04`, `Windows_Baseline_05`, `Windows_Baseline_06`, `Windows_Baseline_07`).

### 2.2. Đề Xuất Bộ Hình Ảnh Chính Thức Cho Mục 3.1 (Tentative Numbering)

1. **Hình 3.1 (Tạm thời):**
   - **Tệp nguồn:** `work/do-an/chapter3/evidence/baseline/Windows_PreDemo_01_Network_SMB.png`
   - **SHA-256 nguồn:** `e3744451374e9544f29dda79b06bd1e8df122119ef046b20dfb9f396d65a0b34`
   - **Chú thích đề xuất:** *Hình 3.1. Trạng thái mạng, dịch vụ SMB và các cổng lắng nghe trên máy chủ Windows Server 2012 R2 trước thực nghiệm*
   - **Vai trò chứng minh:** Minh chứng trực quan các lệnh PowerShell kiểm toán mạng (IP 192.168.56.20), dịch vụ LanmanServer (Running / Automatic), tính năng FS-SMB1 Installed, cờ hỗ trợ SMB cục bộ, các cổng TCP 139/445 đang lắng nghe và phiên bản số nhị phân srv.sys 6.3.9600.16421.
   - **Ranh giới chú thích và diễn giải:** Chú thích chỉ mô tả các thuộc tính mạng và dịch vụ hiển thị trong giao diện PowerShell. Không tuyên bố bức ảnh chứng minh mọi giá trị tham số trong Bảng 3.1 nếu vùng ảnh crop không bao hàm giá trị đó; không đồng nhất trạng thái cổng lắng nghe cục bộ với trạng thái `OPEN` nhìn từ xa qua mạng.
   - **Kế hoạch cắt cúp đề xuất (Crop Proposal):**
     * *Vùng thông tin phải giữ:* Cửa sổ PowerShell chính hiển thị các lệnh kiểm toán mạng, dịch vụ LanmanServer, cấu hình SMB server, cổng lắng nghe và phiên bản srv.sys.
     * *Giao diện thừa loại bỏ:* Nền Server Manager trống bên phải và thanh taskbar bên dưới.
     * *Ngữ cảnh bắt buộc bảo tồn:* Tiêu đề cửa sổ PowerShell, các câu lệnh đã thực thi và các khối kết quả đầu ra.
     * *Mục đích trình bày:* Tăng kích thước phông chữ, bảo đảm người đọc xem rõ từng tham số trên trang in A4.

2. **Hình 3.2 (Tạm thời):**
   - **Tệp nguồn:** `work/do-an/chapter3/evidence/baseline/Windows_PreDemo_02_Firewall.png`
   - **SHA-256 nguồn:** `c685573c3c1d00460d49d8718cc02a48ef8bceda26ce5cac1ab913e1db0d7077`
   - **Chú thích đề xuất:** *Hình 3.2. Cấu hình quy tắc tường lửa tùy biến kiểm soát phạm vi nguồn truy cập dịch vụ SMB trên máy chủ mục tiêu*
   - **Vai trò chứng minh:** Minh chứng chính sách kiểm soát an ninh tại máy chủ: quy tắc tùy biến `ATTT Lab SMB 139-445` (Inbound Allow, TCP 139/445) với phạm vi địa chỉ nguồn từ xa chỉ định duy nhất `192.168.56.10`, trong khi 3 hồ sơ tường lửa đều bật và 16 quy tắc chia sẻ tệp mặc định đều bị vô hiệu hóa.
   - **Ranh giới chú thích và diễn giải:** Chú thích mô tả quy tắc tường lửa tùy biến và phạm vi nguồn tương ứng. Không tuyên bố bức ảnh này tự nó chứng minh mọi nguồn IP khác đều bị chặn trên mọi phương diện.
   - **Kế hoạch cắt cúp đề xuất (Crop Proposal):**
     * *Vùng thông tin phải giữ:* Cửa sổ PowerShell hiển thị 5 khối lệnh kiểm toán tường lửa (thuộc tính quy tắc tùy biến, hồ sơ tường lửa, danh sách luật mặc định).
     * *Giao diện thừa loại bỏ:* Thanh taskbar và phần nền Server Manager mờ phía sau.
     * *Ngữ cảnh bắt buộc bảo tồn:* Tên quy tắc `ATTT Lab SMB 139-445`, cổng `{139, 445}`, địa chỉ nguồn `192.168.56.10`, trạng thái 3 profile `True` và số lượng 16 luật mặc định `False`.
     * *Mục đích trình bày:* Loại bỏ chi tiết giao diện thừa, làm nổi bật chính sách kiểm soát an ninh mạng của máy chủ.

3. **Hình 3.3 (Tạm thời):**
   - **Tệp nguồn:** `work/do-an/chapter3/evidence/baseline/Windows_MS17010_02_Hotfix.png`
   - **SHA-256 nguồn:** `c2130e7256c08f592f9f884ec979e505c775cdfb74bc149dfa63fef5335e658f`
   - **Chú thích đề xuất:** *Hình 3.3. Thuộc tính phiên bản tệp driver srv.sys và danh mục bản vá được ghi nhận trên máy chủ mục tiêu*
   - **Vai trò chứng minh:** Minh chứng chuỗi FileVersion hiển thị `6.3.9600.16384`, việc trích xuất phiên bản số nhị phân cấu thành `6.3.9600.16421` và danh mục 6 bản vá hệ thống qua `Get-HotFix` trên cùng một màn hình PowerShell.
   - **Ranh giới chú thích và diễn giải:** Tuyệt đối không đưa chữ "UNPATCHED" trực tiếp vào tiêu đề ảnh; kết luận `UNPATCHED` là kết quả phân tích đối chiếu tổng hợp giữa phiên bản số nhị phân, danh mục bản vá thiếu hụt và ngưỡng tài liệu chính thức của Microsoft trong Bảng 3.2. Không đồng nhất trạng thái chưa vá cục bộ với khả năng khai thác thành công từ xa qua mạng.
   - **Kế hoạch cắt cúp đề xuất (Crop Proposal):**
     * *Vùng thông tin phải giữ:* Cửa sổ PowerShell chứa toàn bộ các lệnh lấy thuộc tính tệp `srv.sys` và bảng kết quả `Get-HotFix`.
     * *Giao diện thừa loại bỏ:* Thanh taskbar và bong bóng thông báo "View messages in Action Center" ở khay hệ thống, phần nền desktop trống.
     * *Ngữ cảnh bắt buộc bảo tồn:* Toàn bộ nội dung lệnh kiểm tra `srv.sys`, các dòng chuỗi/số phiên bản và bảng danh mục 6 hotfix.
     * *Mục đích trình bày:* Loại bỏ popup thông báo không liên quan ở khay hệ thống, bảo đảm tính trang nghiêm khoa học và rõ ràng của bằng chứng bản vá.

---

## 3. Lý Do Loại Bỏ Các Ảnh Trùng Lặp (Redundancy & Rejection Rationales)

1. **Nhóm ảnh môi trường Kali (`Kali_PreDemo_01`, `Kali_PreDemo_02`):**
   - Các lệnh cấu hình mạng Kali (`ip address`, `ip route`) và phiên bản Nmap chỉ cung cấp các giá trị cấu hình cơ bản (192.168.56.10/24, kernel route, Nmap 7.99). Việc đưa ảnh chụp terminal của các lệnh này vào báo cáo gây loãng tài liệu; Bảng 3.1 trình bày các tham số này chuẩn mực và tiết kiệm không gian hơn.
   - Ảnh trợ giúp NSE scripts chỉ hiển thị tài liệu văn bản tĩnh có sẵn của công cụ, không mang tính chứng minh dữ liệu thực nghiệm.
2. **Nhóm ảnh Windows đơn lẻ (`Windows_Baseline_01`, `04`, `05`, `06`, `07`):**
   - Đây là các ảnh chụp từng lệnh PowerShell rời rạc trong quá trình chuẩn bị ban đầu. Hầu hết các ảnh này có thông tin thưa thớt, cửa sổ chiếm diện tích lớn nhưng chỉ có 1-2 dòng văn bản, bố cục trống trải và đã bị thay thế hoàn toàn bởi ảnh kiểm toán hợp nhất `Windows_PreDemo_01_Network_SMB.png` (Hình 3.1) và Bảng 3.1.
3. **Chuyển `Windows_MS17010_01_SrvSysVersion.png` sang OPTIONAL:**
   - Ảnh này chỉ hiển thị phiên bản `srv.sys`. Do ảnh `Windows_MS17010_02_Hotfix.png` (Hình 3.3) đã hiển thị toàn bộ nội dung của ảnh 01 đồng thời cung cấp thêm bảng kiểm kê 6 hotfix hệ thống, việc giữ ảnh 02 và chuyển ảnh 01 sang dự phòng giúp giảm thiểu hoàn toàn sự trùng lặp thị giác.
4. **Giữ `Kali_to_Windows_Connectivity.png` và `Windows_FirewallPrep_04_Scope.png` ở mức OPTIONAL:**
   - Ảnh kết nối mạng Kali-Windows chỉ dùng dự phòng nếu phản biện yêu cầu minh chứng trạng thái láng giềng L2 ARP REACHABLE; việc lược bỏ khỏi kế hoạch chính giúp tránh suy diễn sai về nguyên nhân ICMP không có phản hồi.
   - Ảnh phạm vi tường lửa 04 chỉ mang tính hỗ trợ cho quy tắc tùy biến, đã được phản ánh vượt trội trong `Windows_PreDemo_02_Firewall.png`.
