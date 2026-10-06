# BẢNG KÊ CẮT CÚP HÌNH ẢNH MỤC 3.4 CASE B (CH3_34_CASEB_CROP_MANIFEST_R1)

- **Trạng thái:** `COMPLETED_AND_VERIFIED`
- **Pha thực hiện:** `X7D1 — Draft Chapter 3 Section 3.4 Case B`
- **Ngày thực hiện:** 2026-10-07
- **Nguyên tắc bảo tồn bằng chứng:**
  1. Tuyệt đối không chỉnh sửa byte của các tệp bằng chứng gốc tại `work/do-an/chapter3/evidence/case_b/`.
  2. Kích thước nguồn được xác định chính xác ($1280 \times 800\,\text{px}$) và mã băm SHA-256 được đối soát bằng mã lệnh trước khi thực hiện cắt cúp.
  3. Chỉ tạo bản phái sinh phục vụ trình bày báo cáo tại `work/do-an/chapter3/presentation/3_4/`.
  4. Đã kiểm tra trực quan từng ảnh phái sinh, bảo đảm không làm mất bất kỳ thông số kỹ thuật hay ngữ cảnh dòng lệnh nào cần thiết cho bài viết.
  5. Tuyệt đối không chỉnh màu, không làm sắc nét nhân tạo, không chú thích đè hoặc thêm bất kỳ ký hiệu đồ họa nào.

---

## 1. Bảng Kê Chi Tiết Các Hình Ảnh Phái Sinh (Derived Images Manifest)

### 1.1. Hình 3.7 — Trạng thái cấu hình SMB, tính năng FS-SMB1 và dịch vụ LanmanServer sau khi vô hiệu hóa SMBv1
- **Tệp nguồn (Source Path):** `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_03_After_Local.png`
- **SHA-256 nguồn:** `2f762508ec98da3b6ed75813c32ed5622cbe1c982e6e6e2907086152e9a6a6ad`
- **Kích thước nguồn (Source Dimensions):** $1280 \times 800\,\text{px}$
- **Tệp phái sinh (Derived Path):** `work/do-an/chapter3/presentation/3_4/Hinh_3_7_After_Local.png`
- **SHA-256 phái sinh:** `b7df43e54f69490c8fdbd82cd273dc834657dc3ec90a96981b3c3897f7e5b9b1`
- **Kích thước phái sinh (Derived Dimensions):** $872 \times 310\,\text{px}$
- **Chế độ (Mode):** `CROP`
- **Khung cắt cúp thực tế (Crop Rectangle):** `x = 0, y = 30, width = 872, height = 310` (tương ứng vùng tọa độ `[left=0, top=30, right=872, bottom=340]`)
- **Nội dung thị giác được bảo tồn:**
  * Lệnh PowerShell kiểm tra cấu hình: `Get-SmbServerConfiguration | Select-Object EnableSMB1Protocol,EnableSMB2Protocol,EnableSecuritySignature,RequireSecuritySignature`.
  * Bảng giá trị cấu hình tương ứng: `EnableSMB1Protocol` mang giá trị `False`, `EnableSMB2Protocol` mang giá trị `True`, `EnableSecuritySignature` mang giá trị `False`, `RequireSecuritySignature` mang giá trị `False`.
  * Lệnh kiểm tra tính năng hệ thống: `Get-WindowsFeature FS-SMB1 | Select-Object Name,InstallState`.
  * Kết quả trạng thái cài đặt tính năng: `FS-SMB1` mang giá trị `Installed`.
  * Lệnh kiểm tra dịch vụ máy chủ: `Get-Service LanmanServer | Select-Object Name,Status,StartType`.
  * Kết quả trạng thái dịch vụ: `LanmanServer` ở trạng thái `Running` (chế độ khởi động `Running`).
  * Dấu nhắc lệnh `PS C:\Users\Administrator>` xuất hiện trở lại tại cuối phiên kiểm tra.
- **Thành phần giao diện bị loại bỏ:**
  * Thanh tiêu đề của cửa sổ console PowerShell ($y < 30\,\text{px}$).
  * Vùng màn hình nền desktop và watermark Windows Server bên phải cửa sổ console ($x > 872\,\text{px}$).
  * Thanh tác vụ Windows Server ở cạnh đáy màn hình ($y > 760\,\text{px}$).
  * Vùng không gian nền console màu đen trống trải phía dưới dấu nhắc lệnh ($y > 340\,\text{px}$).
- **Lý do cắt cúp:** Loại bỏ các vùng giao diện hệ điều hành và khoảng đen vô ích, tập trung thị giác vào ba lệnh kiểm tra cấu hình, tính năng và dịch vụ cốt lõi, bảo đảm hiển thị rõ ràng trên khổ giấy báo cáo.
- **Ranh giới kỹ thuật được bảo tồn:**
  * Bức ảnh minh chứng cấu hình `EnableSMB1Protocol` hiển thị giá trị `False`, `EnableSMB2Protocol` hiển thị `True`, gói tính năng `FS-SMB1` vẫn `Installed`, và dịch vụ `LanmanServer` được ghi nhận `Running` tại thời điểm kiểm tra.
  * Bức ảnh không chứng minh tính năng SMBv1 đã bị gỡ bỏ khỏi hệ điều hành Windows (`SMBv1 disabled != FS-SMB1 uninstalled`).
  * Bức ảnh không chứng minh máy chủ đã được cài đặt bản vá bảo mật MS17-010 (`SMBv1 disabled != PATCHED`); bức ảnh không trực tiếp hiển thị tệp driver `srv.sys` hay danh mục hotfix.
  * Bức ảnh không chứng minh tính liên tục không gián đoạn (zero downtime) của dịch vụ hay sự tương thích của toàn bộ ứng dụng nghiệp vụ hiện đại.

---

### 1.2. Hình 3.8 — Kết quả đo lại các phương ngữ SMB từ trạm Kali Linux sau khi vô hiệu hóa SMBv1
- **Tệp nguồn (Source Path):** `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_04_NSE02_Protocols.png`
- **SHA-256 nguồn:** `21ed6473f4e7010841e9730620b159c272238cf7335eb80fcfaf4ad61f7a7b5a`
- **Kích thước nguồn (Source Dimensions):** $1280 \times 800\,\text{px}$
- **Tệp phái sinh (Derived Path):** `work/do-an/chapter3/presentation/3_4/Hinh_3_8_SMB_Protocols_Retest.png`
- **SHA-256 phái sinh:** `6af9df4edbca32d79af562b7f87b867283b31fba3316ce3859ce1a63a936b52c`
- **Kích thước phái sinh (Derived Dimensions):** $1280 \times 400\,\text{px}$
- **Chế độ (Mode):** `CROP`
- **Khung cắt cúp thực tế (Crop Rectangle):** `x = 0, y = 24, width = 1280, height = 400` (tương ứng vùng tọa độ `[left=0, top=24, right=1280, bottom=424]`)
- **Nội dung thị giác được bảo tồn:**
  * Dòng dấu nhắc shell terminal của trạm kiểm thử Kali Linux (`┌──(kali㉿10)-[~/remediation_smbv1]`).
  * Toàn bộ câu lệnh Nmap đã thực thi: `nmap -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20`.
  * Dòng thông tin khởi động Nmap 7.99 và địa chỉ IP mục tiêu `192.168.56.20`.
  * Dòng trạng thái `Host is up (0.00043s latency)`.
  * Bảng trạng thái cổng: `445/tcp open microsoft-ds`.
  * Dòng địa chỉ MAC mục tiêu: `MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)`.
  * Khối kết quả `Host script results:` dưới kịch bản `smb-protocols` liệt kê đúng 4 phương ngữ: `2.0.2`, `2.1`, `3.0`, và `3.0.2`.
  * Sự vắng mặt của phương ngữ cũ `NT LM 0.12 (SMBv1)` trong danh sách phương ngữ.
  * Thông báo hoàn tất phiên quét: `Nmap done: 1 IP address (1 host up) scanned in 5.38 seconds`.
  * Dòng dấu nhắc shell terminal trả về (`┌──(kali㉿10)-[~/remediation_smbv1] └─$`).
- **Thành phần giao diện bị loại bỏ:**
  * Thanh panel hệ thống trên cùng của Kali XFCE desktop ($y < 24\,\text{px}$).
  * Vùng không gian nền terminal trống trải màu đen phía dưới ($y > 424\,\text{px}$, chiếm 376 pixel chiều cao).
- **Lý do cắt cúp:** Loại bỏ vùng nền terminal đen không mang thông tin, tối ưu hóa tỷ lệ khung hình trên trang in A4 portrait giúp tăng kích thước phông chữ và độ sắc nét cho các dòng kết quả phương ngữ.
- **Ranh giới kỹ thuật được bảo tồn:**
  * Bức ảnh minh chứng kịch bản `smb-protocols` ghi nhận các phương ngữ `2.0.2`, `2.1`, `3.0`, `3.0.2`; phương ngữ cũ `NT LM 0.12 (SMBv1)` không xuất hiện trong danh sách phương ngữ của phép đo lại.
  * Cổng 445/tcp vẫn ở trạng thái OPEN. Bức ảnh không chứng minh cổng 445 đã bị đóng.
  * Bức ảnh không chứng minh việc đàm phán hay bắt tay giao thức diễn ra thành công ngoài danh mục phương ngữ quan sát được.
  * Bức ảnh không chứng minh toàn bộ các ứng dụng nghiệp vụ sử dụng SMB2/3 hoạt động hoàn hảo hay không gặp lỗi kết nối thực tế.
  * Bức ảnh không đưa ra phán quyết về lỗ hổng MS17-010.
