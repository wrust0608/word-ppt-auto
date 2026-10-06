# BẢNG KÊ CẮT CÚP HÌNH ẢNH MỤC 3.1 BASELINE (CH3_31_BASELINE_CROP_MANIFEST_R1)

- **Trạng thái:** `COMPLETED_AND_VERIFIED`
- **Pha thực hiện:** `X7A1 — Draft Chapter 3 Section 3.1 Baseline`
- **Ngày thực hiện:** 2026-10-06
- **Nguyên tắc bảo tồn bằng chứng:**
  1. Tuyệt đối không chỉnh sửa byte của các tệp bằng chứng gốc tại `work/do-an/chapter3/evidence/baseline/`.
  2. Kích thước nguồn được xác định chính xác bằng phương pháp lập trình trước khi thực hiện cắt cúp.
  3. Chỉ tạo bản phái sinh phục vụ trình bày tại `work/do-an/chapter3/presentation/3_1/`.
  4. Đã kiểm tra trực quan từng ảnh phái sinh, bảo đảm không làm mất bất kỳ thông số kỹ thuật hay ngữ cảnh nào cần thiết cho bài viết.
  5. Tuyệt đối không chỉnh màu, không làm sắc nét nhân tạo, không chú thích đè hoặc thêm bất kỳ ký hiệu đồ họa nào.

---

## 1. Bảng Kê Chi Tiết Các Hình Ảnh Phái Sinh (Derived Images Manifest)

### 1.1. Hình 3.1 — Trạng thái mạng, dịch vụ SMB và các cổng lắng nghe trên Windows Server 2012 R2 trước thực nghiệm
- **Tệp nguồn (Source Path):** `work/do-an/chapter3/evidence/baseline/Windows_PreDemo_01_Network_SMB.png`
- **SHA-256 nguồn:** `e3744451374e9544f29dda79b06bd1e8df122119ef046b20dfb9f396d65a0b34`
- **Kích thước nguồn (Source Dimensions):** $1280 \times 800\,\text{px}$
- **Tệp phái sinh (Derived Path):** `work/do-an/chapter3/presentation/3_1/Hinh_3_1_Network_SMB.png`
- **SHA-256 phái sinh:** `8dca03f2121e4807e034451e460c847efef28c249d4ce2b836e3eaec2f04adb4`
- **Kích thước phái sinh:** $874 \times 642\,\text{px}$
- **Chế độ (Mode):** `CROP`
- **Khung cắt cúp thực tế (Crop Rectangle):** `(left=54, top=52, right=928, bottom=694)`
- **Nội dung thị giác được bảo tồn:**
  * Toàn bộ thanh tiêu đề cửa sổ PowerShell (`Administrator: Windows PowerShell`) và các nút điều khiển cửa sổ.
  * Đường viền màu lục lam (cyan) bao quanh cửa sổ PowerShell và thanh cuộn bên phải.
  * Thuộc tính giao diện mạng `Ethernet 192.168.56.20/24`.
  * Lệnh `Get-NetRoute` và bảng định tuyến cục bộ (không có default route).
  * Lệnh `Get-Service LanmanServer` và trạng thái `Running`.
  * Lệnh `Get-WindowsFeature FS-SMB1` và trạng thái `Installed`.
  * Lệnh `Get-SmbServerConfiguration` hiển thị `EnableSMB1Protocol : True`, `EnableSMB2Protocol : True`, `EnableSecuritySignature : False`, `RequireSecuritySignature : False`.
  * Lệnh `Get-NetTCPConnection` hiển thị cổng lắng nghe TCP 445 (`::`) và TCP 139 (`192.168.56.20`).
  * Lệnh lấy thuộc tính `srv.sys` hiển thị phiên bản số nhị phân `6.3.9600.16421`.
- **Thành phần giao diện bị loại bỏ:**
  * Dải menu màu xám phía trên cửa sổ PowerShell ($y < 52\,\text{px}$).
  * Vùng màn hình desktop Server Manager trống bên phải ($x > 928\,\text{px}$).
  * Thanh taskbar và phần chân màn hình bên dưới ($y > 694\,\text{px}$).
- **Lý do cắt cúp:** Loại bỏ 40% diện tích màn hình nền trống không mang thông tin, giúp phóng to cỡ chữ lên khoảng 146% trên trang in A4, người đọc có thể đọc rõ từng dòng lệnh và kết quả mà không cần phóng đại.
- **Ranh giới kỹ thuật được bảo tồn:** Không cắt mất bất kỳ dòng lệnh PowerShell nào; giữ nguyên bản chất hiển thị của trạng thái lắng nghe cục bộ (không suy diễn thành remote OPEN).

---

### 1.2. Hình 3.2 — Cấu hình Windows Firewall giới hạn nguồn truy cập TCP 139/445 từ trạm Kali Linux
- **Tệp nguồn (Source Path):** `work/do-an/chapter3/evidence/baseline/Windows_PreDemo_02_Firewall.png`
- **SHA-256 nguồn:** `c685573c3c1d00460d49d8718cc02a48ef8bceda26ce5cac1ab913e1db0d7077`
- **Kích thước nguồn (Source Dimensions):** $1280 \times 800\,\text{px}$
- **Tệp phái sinh (Derived Path):** `work/do-an/chapter3/presentation/3_1/Hinh_3_2_Firewall.png`
- **SHA-256 phái sinh:** `4804161192a806be15df49abc2efbab4f6673ab4c9e85074c423ce405f003c64`
- **Kích thước phái sinh:** $874 \times 642\,\text{px}$
- **Chế độ (Mode):** `CROP`
- **Khung cắt cúp thực tế (Crop Rectangle):** `(left=54, top=52, right=928, bottom=694)`
- **Nội dung thị giác được bảo tồn:**
  * Thanh tiêu đề cửa sổ PowerShell (`Administrator: Windows PowerShell`).
  * Đường viền cửa sổ và thanh cuộn bên phải.
  * Khối 1: `DisplayName: ATTT Lab SMB 139-445`, `Enabled: True`, `Direction: Inbound`, `Action: Allow`, `Profile: Any`.
  * Khối 2: Lọc cổng với `Protocol: TCP`, `LocalPort: {139, 445}`, `RemotePort: Any`.
  * Khối 3: Lọc địa chỉ với `LocalAddress: Any`, `RemoteAddress: 192.168.56.10`.
  * Khối 4: `Get-NetFirewallProfile` hiển thị `Domain: True`, `Private: True`, `Public: True`.
  * Khối 5: Lệnh kiểm tra nhóm quy tắc `File and Printer Sharing` hiển thị `Name: False`, `Count: 16`.
- **Thành phần giao diện bị loại bỏ:**
  * Dải menu xám phía trên ($y < 52\,\text{px}$).
  * Nền Server Manager mờ bên phải ($x > 928\,\text{px}$).
  * Thanh taskbar và phần chân màn hình ($y > 694\,\text{px}$).
- **Lý do cắt cúp:** Tập trung toàn bộ thị giác vào 5 khối lệnh kiểm toán tường lửa, loại bỏ các chi tiết giao diện thừa.
- **Ranh giới kỹ thuật được bảo tồn:** Bảo toàn trọn vẹn thông tin quy tắc cho phép cụ thể đối với `.56.10` và trạng thái tắt của 16 luật chia sẻ tệp mặc định; không suy diễn thành việc mọi địa chỉ IP khác bị chặn trên mọi phương diện.

---

### 1.3. Hình 3.3 — Phiên bản srv.sys và danh mục hotfix ghi nhận trên Windows Server 2012 R2
- **Tệp nguồn (Source Path):** `work/do-an/chapter3/evidence/baseline/Windows_MS17010_02_Hotfix.png`
- **SHA-256 nguồn:** `c2130e7256c08f592f9f884ec979e505c775cdfb74bc149dfa63fef5335e658f`
- **Kích thước nguồn (Source Dimensions):** $1280 \times 800\,\text{px}$
- **Tệp phái sinh (Derived Path):** `work/do-an/chapter3/presentation/3_1/Hinh_3_3_SrvSys_Hotfix.png`
- **SHA-256 phái sinh:** `b495b35e07011775f2005aa3f02104cf4438b6dee7cbb43f7eed13561644e9e6`
- **Kích thước phái sinh:** $872 \times 450\,\text{px}$
- **Chế độ (Mode):** `CROP`
- **Khung cắt cúp thực tế (Crop Rectangle):** `(left=0, top=0, right=872, bottom=450)`
- **Nội dung thị giác được bảo tồn:**
  * Toàn bộ thanh tiêu đề cửa sổ PowerShell (`Administrator: Windows PowerShell`).
  * Lệnh lấy `VersionInfo` của `srv.sys` và hai dòng hiển thị `FileVersion` / `ProductVersion: 6.3.9600.16384 (winblue_rtm.130821-1623)`.
  * Lệnh ghép nối 4 trường phiên bản số nhị phân và kết quả `6.3.9600.16421`.
  * Lệnh `Get-HotFix | Sort-Object HotFixID | Format-Table HotFixID, Description, InstalledOn -AutoSize`.
  * Toàn bộ 6 hàng bản vá hiển thị: KB2919355, KB2919442, KB2937220, KB2938772, KB2939471, KB2949621 (đều cài đặt ngày 21/03/2014).
  * Dòng dấu nhắc lệnh kết thúc `PS C:\Users\Administrator> _` kèm khoảng trống xanh vừa đủ bên dưới.
- **Thành phần giao diện bị loại bỏ:**
  * Vùng màn hình desktop Server Manager bên phải ($x > 872\,\text{px}$).
  * Khoảng không gian xanh trống trải bên dưới câu lệnh ($y > 450\,\text{px}$).
  * Thanh taskbar và đặc biệt là bong bóng thông báo "View messages in Action Center" kèm biểu tượng cờ đỏ xuất hiện ở góc dưới bên phải khay hệ thống ($x > 830\,\text{px}, y > 730\,\text{px}$).
- **Lý do cắt cúp:** Loại bỏ hoàn toàn khoảng trống đen/xanh vô nghĩa bên dưới bảng và loại bỏ triệt để popup thông báo hệ thống không liên quan ở góc phải taskbar, mang lại hình ảnh báo cáo nghiêm túc, chuẩn mực học thuật và có tỷ lệ khung hình cân đối (~1.94:1).
- **Ranh giới kỹ thuật được bảo tồn:** Bảo toàn trọn vẹn cả chuỗi hiển thị, phiên bản số nhị phân và toàn bộ danh mục 6 hotfix; không đưa chữ "UNPATCHED" trực tiếp vào ảnh.

---

## 2. Tổng Hợp Kiểm Thẩm Tra Bảng Kê Cắt Cúp

| Số hiệu | Tệp phái sinh | Kích thước nguồn | Kích thước phái sinh | Chế độ | SHA-256 phái sinh (8 ký tự đầu) | Đánh giá kiểm tra trực quan |
|---|---|:---:|:---:|:---:|:---:|---|
| **Hình 3.1** | `Hinh_3_1_Network_SMB.png` | $1280 \times 800$ | $874 \times 642$ | `CROP` | `8dca03f2` | Rất tốt. Chữ sắc nét, không mất dữ liệu mạng/SMB/srv.sys |
| **Hình 3.2** | `Hinh_3_2_Firewall.png` | $1280 \times 800$ | $874 \times 642$ | `CROP` | `48041611` | Rất tốt. 5 khối lệnh kiểm toán tường lửa hiển thị trọn vẹn |
| **Hình 3.3** | `Hinh_3_3_SrvSys_Hotfix.png` | $1280 \times 800$ | $872 \times 450$ | `CROP` | `b495b35e` | Hoàn hảo. Loại bỏ hoàn toàn popup Action Center và taskbar |
