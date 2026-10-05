# KẾ HOẠCH HÌNH ẢNH VÀ BẢNG BIỂU CHƯƠNG 3 (CHAPTER 3 FIGURE & TABLE PLAN)

- **Trạng thái:** `PLAN_LOCKED_CANONICAL`
- **Nguyên tắc cốt lõi:**
  1. **Chống lạm dụng ảnh chụp màn hình (Anti-Screenshot Spam):** Ưu tiên tuyệt đối việc trình bày số liệu đo đạc qua bảng tổng hợp (Table) định dạng chuẩn khoa học. Chỉ sử dụng ảnh chụp màn hình đối với những bằng chứng thị giác không thể thay thế bằng văn bản thô.
  2. **Bảo tồn tính trung thực của bằng chứng:** Mọi hình ảnh phải truy vết trực tiếp về tệp nguồn canonical, có tọa độ cắt cúp hợp lý, không chèn hình ảnh minh họa giả định.
  3. **Khóa nhãn và chú thích:** Chú thích hình phải mô tả đúng nội dung quan sát thực tế, không đưa ra kết luận vượt quá dữ liệu hiển thị.

---

## 1. Danh Mục Hình Ảnh Đề Xuất Cho Chương 3

| Số hiệu đề xuất | Mục đích chứng minh | Tệp nguồn canonical | Hướng dẫn cắt cúp (Crop Recommendation) | Chú thích dự kiến (Tentative Caption) | Luận điểm được hỗ trợ | Ưu tiên: Bảng hay Ảnh? |
|---|---|---|---|---|---|---|
| **Hình 3.1** | Minh chứng thị giác về trạng thái driver `srv.sys` chưa được cập nhật bản vá MS17-010 tại mốc chuẩn xuất phát | `baseline/Windows_MS17010_01_SrvSysVersion.png` | Cắt tập trung vào tab `Details` của hộp thoại Properties tệp `srv.sys`, làm nổi bật `File version: 6.3.9600.16384` | **Hình 3.1: Thông số phiên bản tệp srv.sys xác nhận trạng thái chưa cập nhật bản vá tại mốc chuẩn xuất phát** | Khẳng định thực tế khách quan rằng máy chủ Windows Server 2012 R2 đang ở trạng thái UNPATCHED đối với lỗ hổng MS17-010 trước khi thử nghiệm. | **ẢNH CẦN THIẾT** (Bằng chứng thị giác thuộc tính hệ thống) |
| **Hình 3.2** | Kiểm chứng trạng thái mở cổng TCP 139 và 445 cùng thông số thời gian sống (TTL) trong Kịch bản 1 | `scenario1/Scenario1_B4_SMB_Ports.png` | Cắt gọn cửa sổ terminal Nmap, hiển thị rõ dòng lệnh `nmap -p 139,445` và bảng trạng thái cổng 139, 445 `open` | **Hình 3.2: Kết quả quét cổng dịch vụ SMB tại Kịch bản 1 xác nhận cổng 139 và 445 ở trạng thái mở** | Chứng minh hai cổng dịch vụ SMB đang mở và tiếp nhận kết nối TCP từ trạm kiểm thử Kali. | **Bảng tóm tắt ưu tiên hơn**, ảnh chỉ đóng vai trò thứ cấp. |
| **Hình 3.3** | Minh chứng sự hiện diện của 5 phương ngữ đàm phán bao gồm SMBv1 (`NT LM 0.12`) trong Kịch bản 2 | `scenario2/Scenario2_NSE02_Protocols.png` | Cắt tập trung phần output của NSE script `smb-protocols`, làm nổi bật danh sách các dialect được hỗ trợ | **Hình 3.3: Kết quả script smb-protocols trong Kịch bản 2 xác nhận máy chủ hỗ trợ phương ngữ SMBv1** | Chứng minh tiền điều kiện giao thức (L3) tồn tại: ngăn xếp máy chủ sẵn sàng đàm phán phiên bản SMBv1 cũ. | **Bảng tóm tắt ưu tiên hơn**, giữ ảnh làm đối chứng trực quan. |
| **Hình 3.4** | Thao tác thực thi lệnh vô hiệu hóa giao thức SMBv1 và trạng thái cấu hình cục bộ sau can thiệp (Case B) | Ghép 2 ảnh: `case_b/SMBv1_Remediation_02_Action.png` và `case_b/SMBv1_Remediation_03_After_Local.png` | Ghép dọc: Nửa trên hiển thị lệnh PowerShell `Set-SmbServerConfiguration`, nửa dưới hiển thị kết quả kiểm tra `EnableSMB1Protocol : False` | **Hình 3.4: Thao tác thực thi lệnh vô hiệu hóa giao thức SMBv1 và kết quả xác nhận cấu hình cục bộ tại Case B** | Khẳng định can thiệp kỹ thuật tắt SMBv1 đã thành công trên máy chủ mà không làm gián đoạn dịch vụ chia sẻ tệp hiện đại. | **ẢNH CẦN THIẾT** (Chứng minh quy trình thực thi can thiệp quản trị) |
| **Hình 3.5** | Đo đạc đối chứng từ xa: Sự biến mất của phương ngữ SMBv1 khỏi danh sách đàm phán sau can thiệp Case B | `case_b/SMBv1_Remediation_04_NSE02_Protocols.png` | Cắt phần output script `smb-protocols` trên trạm Kali, hiển thị rõ chỉ còn các dialect từ SMB 2.0.2 trở lên | **Hình 3.5: Kết quả quét lại từ xa xác nhận phương ngữ SMBv1 đã bị loại bỏ khỏi danh sách đàm phán sau can thiệp Case B** | Khẳng định biện pháp tắt SMBv1 đã triệt tiêu hoàn toàn bề mặt tấn công mức giao thức (L3) từ góc nhìn của trạm quét ngoài mạng. | **ẢNH CẦN THIẾT** (Bằng chứng then chốt chứng minh tính hiệu quả của Case B) |
| **Hình 3.6** | Cấu hình quy tắc lọc gói tin SMB và vị trí ưu tiên thực thi trên giao diện tường lửa pfSense (Case C) | `case_c/pfSense_08_Rule_Order.png` | Cắt khu vực bảng quy tắc của giao diện `CASE_C_KALI`, làm nổi bật hàng quy tắc `Block SMB` nằm ngay phía trên quy tắc `Baseline Pass` | **Hình 3.6: Thứ tự thực thi quy tắc tường lửa pfSense ưu tiên chặn lưu lượng SMB trước quy tắc cho phép** | Khẳng định cơ chế bảo vệ Transparent Bridge được kích hoạt đúng theo nguyên lý First-Match của tường lửa trạng thái. | **ẢNH CẦN THIẾT** (Minh chứng cấu hình kiến trúc an ninh mạng) |
| **Hình 3.7** | Kết quả quét cổng dịch vụ SMB chuyển sang trạng thái lọc (Filtered) sau khi triển khai pfSense (Case C) | `case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` | Cắt cửa sổ terminal Nmap hiển thị cổng 139 và 445 chuyển sang trạng thái `filtered` do `no-response` | **Hình 3.7: Kết quả quét cổng SMB chuyển sang trạng thái filtered dưới sự kiểm soát của tường lửa pfSense** | Khẳng định lưu lượng thăm dò mạng L1/L2 đã bị chặn đứng hoàn toàn trên đường truyền giữa Kali và Windows. | **ẢNH CẦN THIẾT** (Bằng chứng đối chứng then chốt của Case C) |
| **Hình 3.8** | Bằng chứng thực nghiệm nhật ký tường lửa pfSense ghi nhận hành vi chặn các gói tin TCP SYN thăm dò SMB | `case_c/pfSense_10_Block_Log_CANONICAL.png` | Cắt khu vực bảng nhật ký `System Logs / Firewall`, hiển thị rõ các dòng log có biểu tượng Block đỏ từ `.56.10` tới `.56.20:139/445` với cờ SYN | **Hình 3.8: Nhật ký tường lửa pfSense ghi nhận việc chặn các gói tin TCP SYN thăm dò cổng dịch vụ SMB** | Minh chứng trực tiếp và khách quan rằng các gói tin yêu cầu kết nối đã bị pfSense loại bỏ. *(Kèm chú thích bảo lưu: không quy thuộc nhãn rule)* | **ẢNH CẦN THIẾT** (Bằng chứng nhật ký vận hành có tính thuyết phục cao nhất) |

---

## 2. Danh Mục Bảng Biểu Trọng Tâm Cho Chương 3

| Số hiệu đề xuất | Tên bảng dự kiến | Vai trò kỹ thuật | Dữ liệu nguồn tổng hợp |
|---|---|---|---|
| **Bảng 3.1** | **Bảng tổng hợp thông số kiểm toán mốc chuẩn xuất phát trước thực nghiệm** | Hệ thống hóa toàn bộ tham số môi trường mạng, dịch vụ, cấu hình bảo mật và trạng thái bản vá của máy chủ mục tiêu trước khi tiến hành các kịch bản quét. | `Final_PreDemo_Audit.txt`, `MS17-010_Official_Mapping.txt`, `Windows_FirewallPrep_Final.txt`, `VirtualBox_HostOnly_Config.txt` |
| **Bảng 3.2** | **Bảng kết quả rà quét nhận diện dịch vụ và phương ngữ SMB tại Kịch bản 1** | Trình bày tường minh kết quả các bước B2, B3, B4, B5, B6: trạng thái cổng, thời gian trễ, phiên bản dịch vụ nhận diện và danh sách 5 phương ngữ SMB. | `b2_host_discovery.nmap`, `b3_target_alive.nmap`, `b4_smb_ports.nmap`, `b5_smb_version.nmap`, `b6_smb_nse.nmap` |
| **Bảng 3.3** | **Bảng kết quả chuỗi kịch bản kiểm định lỗ hổng an ninh MS17-010 tại Kịch bản 2** | Thống kê kết quả 4 script NSE độc lập, làm rõ tiền điều kiện cổng (NSE01), giao thức (NSE02), signing (NSE03) và phán quyết UNKNOWN của script MS17-010 (NSE04). | `NSE-SMB-01_ports.nmap`, `NSE-SMB-02_protocols.nmap`, `NSE-SMB-03_signing.nmap`, `NSE-SMB-04_ms17010.nmap` |
| **Bảng 3.4** | **Bảng đo đạc đối chứng kết quả trước và sau khi vô hiệu hóa SMBv1 (Case B)** | So sánh trực quan trạng thái cấu hình cục bộ và kết quả thăm dò từ xa giữa trước và sau khi tắt SMBv1 (sự biến mất của dialect SMBv1, cổng 445 vẫn mở, tính độc lập với bản vá). | `case_b/SMBv1_Remediation_Run_Manifest.txt`, `case_b/NSE-SMB-02_protocols.nmap`, `case_b/NSE-SMB-04_ms17010.nmap` |
| **Bảng 3.5** | **Bảng đo đạc đối chứng kết quả kiểm soát lưu lượng qua tường lửa pfSense (Case C)** | So sánh trạng thái mạng trước và sau khi kích hoạt bộ lọc Transparent Bridge: cổng chuyển từ OPEN sang FILTERED, gói tin bị hủy, nhật ký ghi nhận hành vi chặn. | `case_c/pfSense_Remediation_Run_Manifest.txt`, `case_c/NSE-SMB-01_ports.nmap`, `case_c/NSE-SMB-04_ms17010.nmap`, `RUN4_PAUSE_STATE_REPORT.txt` |
| **Bảng 3.6** | **Bảng ma trận so sánh tổng hợp hiệu quả của các biện pháp phòng thủ** | Đánh giá so sánh đa chiều giữa Baseline, Case B và Case C trên các tiêu chí: Bề mặt tấn công L1/L2, Bề mặt tấn công L3, Tính sẵn sàng của dịch vụ, Rủi ro phụ thuộc bản vá hệ thống. | Tổng hợp đối chiếu chéo toàn bộ dữ liệu thực nghiệm từ Bảng 3.1 đến Bảng 3.5. |

---

## 3. Quy Tắc Trình Bày Hình Ảnh Và Bảng Biểu Trong Bản Word

1. **Số lượng hình ảnh:** Khống chế tối đa 8 hình ảnh cốt lõi trong Chương 3 (từ Hình 3.1 đến Hình 3.8), tuyệt đối không chèn dàn trải các ảnh lặp lại.
2. **Số lượng bảng biểu:** Bao gồm 6 bảng biểu chuẩn mực (từ Bảng 3.1 đến Bảng 3.6) làm trụ cột dữ liệu chính xác cho toàn bộ chương.
3. **Độ phân giải & Tỉ lệ:** Ảnh phải được cắt cúp sắc nét, độ phân giải tối thiểu 300 DPI, chiều rộng từ $12.0\,\text{cm}$ đến $15.5\,\text{cm}$, căn giữa trang.
4. **Định dạng chú thích:**
   - Tiêu đề bảng đặt **PHÍA TRÊN** bảng: font Times New Roman 12pt, in đậm, căn giữa.
   - Chú thích hình đặt **PHÍA DƯỚI** hình: font Times New Roman 12pt, in đậm, căn giữa.
