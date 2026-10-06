# BÁO CÁO LỰA CHỌN VÀ ĐÁNH GIÁ HÌNH ẢNH MỤC 3.1 BASELINE (CH3_31_BASELINE_FIGURE_SELECTION_R1)

- **Trạng thái:** `PLAN_LOCKED_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7A0 — Baseline Evidence & Presentation Plan`
- **Phạm vi thẩm tra:** Toàn bộ 13 tệp ảnh chụp màn hình đã stage tại `work/do-an/chapter3/evidence/baseline/`
- **Nguyên tắc cốt lõi:**
  1. **Chống lạm dụng ảnh chụp màn hình (Anti-Screenshot Spam):** Chỉ giữ ảnh (`KEEP`) khi và chỉ khi ảnh đó trực tiếp chứng minh một thuộc tính kỹ thuật có giá trị mà bảng tổng hợp hoặc văn xuôi không thể truyền tải một cách thuyết phục bằng chứng thị giác.
  2. **Bảo tồn tính toàn vẹn bằng chứng:** Tuyệt đối không chỉnh sửa tệp ảnh gốc. Mọi đề xuất cắt cúp (`crop`) chỉ nhằm tối ưu hóa việc trình bày bố cục bản in, giữ nguyên ngữ cảnh kỹ thuật trọng yếu.
  3. **Ưu tiên bảng biểu:** Dữ liệu cấu hình hệ điều hành, tham số mạng và danh mục bản vá được ưu tiên tuyệt đối đưa vào Bảng 3.1.

---

## 1. Bảng Đánh Giá Chi Tiết Toàn Bộ 13 Ảnh Chụp Màn Hình Mốc Xuất Phát

| Tệp ảnh gốc (File) | Nội dung hiển thị trực tiếp (Directly shows) | Thông tin độc bản? (Unique info?) | Bảng có thể thay thế? (Table can replace?) | Độ sắc nét & Bố cục (Legibility) | Cần cắt cúp? (Crop needed?) | Phân loại (KEEP / OPTIONAL / DROP) | Đề xuất sử dụng (Proposed use) |
|---|---|---|---|---|---|---|---|
| `Kali_PreDemo_01_Network_Tools.png` | Cửa sổ terminal Kali: `ip address` (192.168.56.10/24), `ip route` (192.168.56.0/24), `nmap --version` (7.99), tạo thư mục `evidence/nse-smb` | Không. Đây là thông số môi trường cơ bản của trạm kiểm thử | Có. Bảng 3.1 trình bày IP, routing và phiên bản Nmap gọn gàng hơn | Tốt (1280x800), nhưng nền desktop xanh chiếm phần lớn diện tích | Có (cắt cửa sổ terminal nếu dùng) | **DROP** | Loại bỏ. Toàn bộ tham số mạng Kali được tích hợp trọn vẹn vào Bảng 3.1. |
| `Kali_PreDemo_02_NSE_Scripts.png` | Trợ giúp tĩnh của Nmap (`nmap --script-help`) cho `smb-protocols` và `smb-vuln-ms17-010` | Không. Chỉ là văn bản tài liệu trợ giúp có sẵn của Nmap | Có. Trích dẫn tài liệu chuẩn hoặc ghi chú nguồn | Tốt, chữ sắc nét | Không | **DROP** | Loại bỏ. Không phản ánh trạng thái thực nghiệm của môi trường lab. |
| `Kali_to_Windows_Connectivity.png` | Lệnh `ping -c 2 192.168.56.20` bị mất gói 100% (do Windows Firewall chặn ICMP), kèm `ip neigh` xác nhận ARP `08:00:27:55:71:ce REACHABLE` | Có một phần. Chứng minh tính thông mạng L2 thành công dù L3 ICMP bị chặn | Có. Bảng 3.1 có thể ghi nhận trạng thái kết nối mạng L2/L3 | Tốt, chữ rõ ràng | Có (cắt riêng cửa sổ dòng lệnh) | **OPTIONAL** | Ảnh dự phòng. Sử dụng nếu phản biện yêu cầu bằng chứng thị giác về việc kiểm tra thông mạng hai máy trước khi quét cổng. |
| `Windows_Baseline_01_Winver.png` | Hộp thoại About Windows: Windows Server 2012 R2 Standard Evaluation, Version 6.3 (Build 9600) trên nền Server Manager | Không. Chỉ là hộp thoại nhận diện phiên bản hệ điều hành cơ bản | Có. Bảng 3.1 công bố phiên bản hệ điều hành và số Build chuẩn xác | Tốt, giao diện sắc nét | Có (cắt hộp thoại Winver) | **DROP** | Loại bỏ. Hộp thoại Windows cơ bản không cung cấp giá trị kỹ thuật sâu về an ninh. |
| `Windows_Baseline_04_SMB_Service.png` | PowerShell: `Get-Service LanmanServer` hiển thị Name: LanmanServer, Status: Running | Không. Thông tin đơn lẻ, bị trùng lặp | Có. Hoàn toàn tích hợp vào một dòng của Bảng 3.1 | Kém. Cửa sổ hẹp, nhiều khoảng trống đen, cột StartType bị che khuất | Không | **DROP** | Loại bỏ. Bố cục kém và bị thay thế hoàn toàn bởi bảng tổng hợp. |
| `Windows_Baseline_05_SMB_Features.png` | PowerShell: `Get-WindowsFeature FS-SMB1` hiển thị trạng thái `[X] Installed` | Không. Chỉ thể hiện một thuộc tính cài đặt tính năng | Có. Tích hợp vào Bảng 3.1 | Trung bình. Quá ít thông tin trên diện tích ảnh lớn | Không | **DROP** | Loại bỏ. Không đủ mật độ thông tin để giữ một hình riêng trong báo cáo. |
| `Windows_Baseline_06_SMB_Config.png` | PowerShell: `Get-SmbServerConfiguration` hiển thị EnableSMB1Protocol=True, EnableSMB2Protocol=True, SecuritySignature=False | Không. Bị trùng lặp | Có. Tích hợp vào Bảng 3.1 | Trung bình. Cửa sổ đen chiếm diện tích lớn | Không | **DROP** | Loại bỏ. Trùng lặp hoàn toàn với dữ liệu cấu hình trong Bảng 3.1. |
| `Windows_Baseline_07_Firewall.png` | PowerShell: Profiles Domain/Private/Public True, 4 luật File and Printer Sharing đầu tiên False | Không. Hiển thị bị cắt cụt tên luật hiển thị (DisplayName) | Có. Tích hợp vào Bảng 3.1 | Kém. Tên luật bị ẩn, không đủ thông tin kết luận | Không | **DROP** | Loại bỏ. Bị thay thế hoàn toàn bởi `Windows_FirewallPrep_04_Scope.png` và `Windows_PreDemo_02_Firewall.png`. |
| `Windows_FirewallPrep_04_Scope.png` | PowerShell: Profiles Enabled=True, 16 luật File and Printer Sharing đều False, cổng 139 và 445 đang Listen | Có một phần. Chứng minh trạng thái cổng lắng nghe và luật mặc định bị tắt | Có. Bảng 3.1 trình bày mạch lạc hơn | Khá tốt. Nửa màn hình trái | Có (cắt cửa sổ PowerShell) | **OPTIONAL** | Ảnh dự phòng. Có thể dùng nếu cần minh chứng cục bộ về cổng 139/445 đang Listen trên Windows. |
| `Windows_MS17010_01_SrvSysVersion.png` | PowerShell: 1) FileVersion String `6.3.9600.16384 (winblue_rtm.130821-1623)`; 2) Trích xuất phiên bản số `$vi.FileMajorPart...` = `6.3.9600.16421` | **CỰC KỲ CAO (ĐỘC BẢN)**. Trực tiếp minh chứng sự khác biệt kỹ thuật giữa chuỗi hiển thị và phiên bản số nhị phân của `srv.sys` | Bảng so sánh được số liệu, nhưng ảnh này là bằng chứng thị giác không thể thay thế cho câu hỏi nghiên cứu cốt lõi | Rất cao. Chữ trắng trên nền xanh PowerShell rất sắc nét, màn hình sạch, không bị popup rác | **CÓ**. Đề xuất cắt bỏ phần desktop trống bên phải, tập trung trọn vẹn vào cửa sổ PowerShell | **KEEP (ƯU TIÊN 1)** | **Hình 3.1 (Tạm thời)**. Minh chứng thuộc tính phiên bản driver `srv.sys` tại mốc xuất phát. |
| `Windows_MS17010_02_Hotfix.png` | Giống ảnh 01 kèm thêm lệnh `Get-HotFix` hiển thị 6 bản vá từ 21/03/2014; có popup "Action Center" ở góc phải taskbar | Có. Hiển thị danh sách 6 hotfix trên hệ thống | Có. Danh sách 6 hotfix đưa vào Bảng 3.1 vừa khoa học vừa tránh được popup rác | Khá tốt, nhưng góc dưới phải có bong bóng Action Center làm giảm tính chỉn chu | Cần cắt bỏ thanh taskbar có popup | **OPTIONAL** | Ảnh dự phòng. Nếu phản biện yêu cầu ảnh chụp danh sách hotfix; ưu tiên đưa danh sách hotfix vào bảng biểu. |
| `Windows_PreDemo_01_Network_SMB.png` | Hợp nhất kiểm toán toàn diện: IP Ethernet 192.168.56.20, routes, LanmanServer Running, FS-SMB1 Installed, SMB config, Listeners 139/445, và phiên bản số srv.sys 6.3.9600.16421 | Có. Kiểm toán tập trung toàn bộ cấu hình mạng và dịch vụ SMB cục bộ | Có. Bảng 3.1 tổng hợp toàn diện các tham số này | Khá tốt, nhưng chữ hơi nhỏ do dồn nhiều lệnh | Có (cắt riêng cửa sổ PowerShell) | **OPTIONAL** | Ảnh dự phòng. Minh chứng kiểm toán toàn diện cấu hình máy chủ trước demo nếu không dùng ảnh tường lửa riêng. |
| `Windows_PreDemo_02_Firewall.png` | Cấu hình quy tắc tường lửa `ATTT Lab SMB 139-445`: Inbound Allow, TCP 139/445, RemoteAddress chỉ duy nhất `192.168.56.10`; Profiles True; 16 luật FPS False | **RẤT CAO**. Chứng minh cơ chế an ninh chủ động giới hạn phạm vi quét từ Kali, giải thích nguyên nhân cô lập lưu lượng | Bảng tóm tắt được, nhưng ảnh này có giá trị minh chứng thị giác thuyết phục về thiết kế an ninh lab | Rất cao. Các khối lệnh phân chia rõ ràng, không có khoảng trống thừa | **CÓ**. Đề xuất cắt bỏ phần desktop Server Manager trống bên phải | **KEEP (ƯU TIÊN 2)** | **Hình 3.2 (Tạm thời)**. Minh chứng cấu hình quy tắc tường lửa máy chủ kiểm soát phạm vi kết nối SMB. |

---

## 2. Tổng Hợp Phân Loại Và Đề Xuất Bộ Hình Ảnh Cuối Cùng

### 2.1. Thống Kê Phân Loại
- **Tổng số ảnh đã thẩm tra:** 13 ảnh.
- **Số lượng KEEP (Giữ lại):** 2 ảnh (`Windows_MS17010_01_SrvSysVersion.png`, `Windows_PreDemo_02_Firewall.png`).
- **Số lượng OPTIONAL (Dự phòng):** 3 ảnh (`Kali_to_Windows_Connectivity.png`, `Windows_MS17010_02_Hotfix.png`, `Windows_PreDemo_01_Network_SMB.png`).
- **Số lượng DROP (Loại bỏ):** 8 ảnh (`Kali_PreDemo_01`, `Kali_PreDemo_02`, `Windows_Baseline_01`, `Windows_Baseline_04`, `Windows_Baseline_05`, `Windows_Baseline_06`, `Windows_Baseline_07`, `Windows_FirewallPrep_04`).

### 2.2. Đề Xuất Bộ Hình Ảnh Chính Thức Cho Mục 3.1 (Tentative Numbering)

1. **Hình 3.1 (Tạm thời):**
   - **Tệp nguồn:** `work/do-an/chapter3/evidence/baseline/Windows_MS17010_01_SrvSysVersion.png`
   - **SHA-256 nguồn:** `2f8c1b7ce276919c72bb40a75fbeacdef81f2fa98695758df27f8772bdc149c8`
   - **Chú thích đề xuất:** *Hình 3.1. Phiên bản hiển thị và phiên bản số của tệp srv.sys trên máy chủ Windows Server 2012 R2 trước thực nghiệm*
   - **Vai trò chứng minh:** Xác nhận trực quan chuỗi FileVersion hiển thị `6.3.9600.16384` và phiên bản số nhị phân `6.3.9600.16421`. Kết luận trạng thái bản vá cục bộ (UNPATCHED) được thực hiện thông qua việc đối chiếu với ngưỡng cập nhật tối thiểu `6.3.9600.18604` của Microsoft và danh mục hotfix trong Bảng 3.1.
   - **Yêu cầu cắt cúp (Crop Proposal):** Cắt giữ lại toàn bộ cửa sổ PowerShell (tọa độ khoảng $X: 0 \rightarrow 875\,\text{px}, Y: 0 \rightarrow 960\,\text{px}$ trên ảnh gốc $1440 \times 900\,\text{px}$), loại bỏ phần nền Server Manager trống bên phải để phóng to cỡ chữ, đảm bảo khả năng đọc hoàn hảo trên trang in A4.

2. **Hình 3.2 (Tạm thời):**
   - **Tệp nguồn:** `work/do-an/chapter3/evidence/baseline/Windows_PreDemo_02_Firewall.png`
   - **SHA-256 nguồn:** `60847` bytes / SHA-256: `c685573c3c1d00460d49d8718cc02a48ef8bceda26ce5cac1ab913e1db0d7077`
   - **Chú thích đề xuất:** *Hình 3.2. Cấu hình quy tắc tường lửa tùy biến kiểm soát phạm vi truy cập dịch vụ SMB trên máy chủ mục tiêu*
   - **Vai trò chứng minh:** Xác nhận chính sách kiểm soát an ninh tại máy chủ: quy tắc `ATTT Lab SMB 139-445` chỉ cho phép lưu lượng TCP cổng 139/445 từ duy nhất trạm Kali `192.168.56.10`, trong khi các profile tường lửa đều bật và 16 quy tắc chia sẻ tệp mặc định đều bị vô hiệu hóa.
   - **Yêu cầu cắt cúp (Crop Proposal):** Cắt giữ lại cửa sổ PowerShell chính (tọa độ khoảng $X: 50 \rightarrow 990\,\text{px}, Y: 60 \rightarrow 900\,\text{px}$), loại bỏ thanh taskbar và phần Server Manager nền.

---

## 3. Lý Do Loại Bỏ Các Ảnh Trùng Lặp (Redundancy & Rejection Rationales)

1. **Nhóm ảnh môi trường Kali (`Kali_PreDemo_01`, `Kali_PreDemo_02`):**
   - Các lệnh `ip address`, `ip route` và `nmap --version` chỉ cung cấp các giá trị tham số cấu hình cơ bản (192.168.56.10/24, kernel route, Nmap 7.99). Việc đưa ảnh chụp terminal của các lệnh này vào báo cáo gây loãng tài liệu; bảng tổng hợp trình bày các tham số này chuẩn mực và tiết kiệm không gian hơn.
   - Ảnh trợ giúp NSE scripts chỉ hiển thị tài liệu văn bản tĩnh có sẵn của công cụ, không mang tính chứng minh dữ liệu thực nghiệm.
2. **Nhóm ảnh Windows đơn lẻ (`Windows_Baseline_01`, `04`, `05`, `06`, `07`):**
   - Đây là các ảnh chụp từng lệnh PowerShell rời rạc trong quá trình chuẩn bị ban đầu. Hầu hết các ảnh này có thông tin thưa thớt, cửa sổ chiếm diện tích lớn nhưng chỉ có 1-2 dòng văn bản, bố cục trống trải và đã bị thay thế hoàn toàn bởi ảnh kiểm toán hợp nhất `Windows_PreDemo_01` hoặc Bảng 3.1.
3. **Ảnh `Windows_MS17010_02_Hotfix.png`:**
   - Mặc dù có lệnh `Get-HotFix`, ảnh chụp này bị lỗi hiển thị do bong bóng thông báo "View messages in Action Center" xuất hiện ở khay hệ thống, làm giảm tính nghiêm túc khoa học. Danh mục 6 bản vá được đưa vào Bảng 3.1 giúp người đọc dễ tra cứu số hiệu KB và ngày cài đặt hơn rất nhiều so với nhìn ảnh chụp.
