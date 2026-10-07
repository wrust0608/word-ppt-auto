# BẢNG KÊ CẮT CÚP HÌNH ẢNH MỤC 3.5 CASE C (CH3_35_CASEC_CROP_MANIFEST_R1)

- **Trạng thái:** `COMPLETED_AND_VERIFIED`
- **Pha thực hiện:** `X7E1 — Draft Chapter 3 Section 3.5 Case C`
- **Ngày thực hiện:** 2026-10-07
- **Nguyên tắc bảo tồn bằng chứng:**
  1. Tuyệt đối không chỉnh sửa byte của các tệp bằng chứng gốc tại `work/do-an/chapter3/evidence/case_c/`.
  2. Kích thước nguồn và mã băm SHA-256 được đối soát độc lập bằng mã lệnh trước và sau khi thực hiện cắt cúp.
  3. Chỉ tạo 3 tệp phái sinh chuẩn phục vụ trình bày báo cáo tại `work/do-an/chapter3/presentation/3_5/`.
  4. Đã thẩm tra trực quan từng ảnh phái sinh bằng mắt, bảo đảm toàn bộ dòng lệnh, ngữ cảnh giao diện, nhãn quy tắc, địa chỉ IP và cờ giao thức được giữ trọn vẹn, sắc nét.
  5. Tuyệt đối không chỉnh màu, không làm sắc nét nhân tạo, không chú thích đè hoặc thêm bất kỳ ký hiệu đồ họa nào.
  6. Đặc biệt đối với Hình 3.11, tuyệt đối không cắt bỏ cột Rule nhằm che giấu mâu thuẫn nhãn luật; sự không thống nhất giữa nhãn thị giác và manifest được bảo tồn nguyên trạng.

---

## 1. Bảng Kê Chi Tiết Các Hình Ảnh Phái Sinh (Derived Images Manifest)

### 1.1. Hình 3.9 — Cấu hình quy tắc kiểm soát lưu lượng SMB và thứ tự sắp xếp trên giao diện CASE_C_KALI của pfSense
- **Tệp nguồn (Source Path):** `work/do-an/chapter3/evidence/case_c/pfSense_08_Rule_Order.png`
- **SHA-256 nguồn:** `6029ea7c923c297aa9bc65c3c551a17e1d4f569a2c98f78846a39c69e22aeb45`
- **Kích thước nguồn (Source Dimensions):** $485 \times 731\,\text{px}$
- **Tệp phái sinh (Derived Path):** `work/do-an/chapter3/presentation/3_5/Hinh_3_9_pfSense_Rule_Order.png`
- **SHA-256 phái sinh:** `5b8a4a3b26c6aca6b667e5a4ee256c48dcdd555324e2f7ed0755ae80eba06285`
- **Kích thước phái sinh (Derived Dimensions):** $470 \times 340\,\text{px}$
- **Chế độ (Mode):** `CROP`
- **Khung cắt cúp thực tế (Crop Rectangle):** `x = 15, y = 190, width = 470, height = 340` (vùng tọa độ `[left=15, top=190, right=485, bottom=530]`)
- **Nội dung thị giác được bảo tồn:**
  * Bảng điều hướng giao diện chọn tab: `Floating`, `WAN`, `LAN`, `CASE_C_KALI` (được gạch chân đỏ kích hoạt), `CASE_C_WINDOWS`.
  * Tiêu đề danh mục quy tắc: `Rules (Drag to Change Order)`.
  * Dòng tiêu đề các cột: `States`, `Protocol`, `Source`, `Port`, `Destination`, `Port`.
  * Hàng quy tắc Dòng 1 (Block SMB): Biểu tượng chặn màu đỏ kèm biểu tượng ghi log, `IPv4 TCP`, nguồn `192.168.56.10`, cổng nguồn `*`, đích `192.168.56.20`, cổng đích `SMB_Ports` (139, 445).
  * Hàng quy tắc Dòng 2 (Pass baseline): Biểu tượng cho phép màu xanh, `IPv4 *`, nguồn `192.168.56.10`, cổng nguồn `*`, đích `192.168.56.20`, cổng đích `*`.
  * Hàng nút thao tác danh mục quy tắc bên dưới (`Add`, `Delete`, `Toggle`, `Copy`, `Save`).
- **Thành phần giao diện bị loại bỏ:**
  * Cảnh báo mật khẩu mặc định màu hồng phía trên ($y < 190\,\text{px}$).
  * Logo pfSense Community Edition và thanh menu trên cùng.
  * Vùng lề trắng ngoài rìa trái màn hình ($x < 15\,\text{px}$).
  * Chân trang bản quyền Netgate và liên kết giấy phép ($y > 530\,\text{px}$).
- **Lý do cắt cúp:** Loại bỏ cảnh báo tài khoản và thông tin chân trang thừa, tập trung thị giác vào ngữ cảnh giao diện `CASE_C_KALI`, thứ tự hai quy tắc Block và Pass, và cờ ghi nhật ký được kích hoạt.
- **Ranh giới kỹ thuật được bảo tồn:**
  * Bức ảnh trực tiếp minh chứng quy tắc Block SMB nằm trên quy tắc Pass baseline trong cấu hình pfSense.
  * Bức ảnh không tự chứng minh lưu lượng thực tế đã bị chặn trên đường truyền (cần đối chiếu với nhật ký Hình 3.11).
  * Bức ảnh không chứa thông tin về trạng thái máy chủ Windows mục tiêu.

---

### 1.2. Hình 3.10 — Kết quả đo đạc trạng thái cổng SMB từ trạm Kali Linux qua đường thử nghiệm pfSense
- **Tệp nguồn (Source Path):** `work/do-an/chapter3/evidence/case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`
- **SHA-256 nguồn:** `de266abb4fa3e8412cfc091975d714bb4bf1168a2e3d7f6cba7d7276f22dfba7`
- **Kích thước nguồn (Source Dimensions):** $1280 \times 800\,\text{px}$
- **Tệp phái sinh (Derived Path):** `work/do-an/chapter3/presentation/3_5/Hinh_3_10_Nmap_Filtered.png`
- **SHA-256 phái sinh:** `da342f6fb9909da67fd38caedf73e2f848ac3c65306ec5993f864f9260418942`
- **Kích thước phái sinh (Derived Dimensions):** $660 \times 505\,\text{px}$
- **Chế độ (Mode):** `CROP`
- **Khung cắt cúp thực tế (Crop Rectangle):** `x = 195, y = 120, width = 660, height = 505` (vùng tọa độ `[left=195, top=120, right=855, bottom=625]`)
- **Nội dung thị giác được bảo tồn:**
  * Dòng menu terminal (`Session`, `Actions`, `Edit`, `View`, `Help`).
  * Lệnh chuyển thư mục và dấu nhắc shell: `cd /home/kali/run4_casec_canonical`.
  * Toàn bộ câu lệnh Nmap đã thực thi: `sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20`.
  * Dòng thông tin khởi động Nmap 7.99 và địa chỉ IP mục tiêu `192.168.56.20`.
  * Dòng xác nhận máy chủ trực tuyến: `Host is up, received arp-response (0.00054s latency)`.
  * Bảng trạng thái hai cổng SMB:
    - `139/tcp filtered netbios-ssn no-response`
    - `445/tcp filtered microsoft-ds no-response`
  * Dòng địa chỉ MAC: `MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)`.
  * Dòng thông báo hoàn tất phiên quét: `Nmap done: 1 IP address (1 host up) scanned in 1.33 seconds`.
  * Dấu nhắc shell terminal trả về: `┌──(kali㉿10)-[~/run4_casec_canonical] └─$`.
- **Thành phần giao diện bị loại bỏ:**
  * Vùng màn hình nền desktop Kali Linux bên trái ($x < 195\,\text{px}$) và bên phải ($x > 855\,\text{px}$).
  * Thanh panel hệ thống XFCE trên đỉnh màn hình ($y < 120\,\text{px}$) và cạnh đáy ($y > 625\,\text{px}$).
- **Lý do cắt cúp:** Loại bỏ toàn bộ hình nền máy tính và thanh tác vụ ngoài cửa sổ console, tập trung khung nhìn vào nội dung cửa sổ lệnh Nmap từ lúc phát lệnh đến khi trả về dấu nhắc shell.
- **Ranh giới kỹ thuật được bảo tồn:**
  * Bức ảnh minh chứng từ trạm Kali, cổng 139 và 445 hiển thị trạng thái `filtered` với lý do `no-response`.
  * Trạng thái `filtered` không đồng nghĩa với cổng đóng (`closed`) và không đồng nghĩa với dịch vụ cục bộ bị tắt (`FILTERED != CLOSED`).
  * Trạng thái cổng bị lọc từ xa không đồng nghĩa với máy chủ đã được vá lỗ hổng (`FILTERED != PATCHED`).

---

### 1.3. Hình 3.11 — Nhật ký pfSense ghi nhận lưu lượng TCP SYN tới các cổng SMB bị chặn trên đường thử nghiệm
- **Tệp nguồn (Source Path):** `work/do-an/chapter3/evidence/case_c/pfSense_10_Block_Log_CANONICAL.png`
- **SHA-256 nguồn:** `3b8383c54143f8a01eb6201462a6b30877f4b95f27b1a72f54b8b07562a68bc2`
- **Kích thước nguồn (Source Dimensions):** $1359 \times 17637\,\text{px}$
- **Tệp phái sinh (Derived Path):** `work/do-an/chapter3/presentation/3_5/Hinh_3_11_pfSense_Block_Log.png`
- **SHA-256 phái sinh:** `8333c06da3e35553481d00a7f84c4d65b64dde5a4f7aadc77567d52d113c919b`
- **Kích thước phái sinh (Derived Dimensions):** $1280 \times 220\,\text{px}$
- **Chế độ (Mode):** `CROP`
- **Khung cắt cúp thực tế (Crop Rectangle):** `x = 40, y = 15355, width = 1280, height = 220` (vùng tọa độ `[left=40, top=15355, right=1320, bottom=15575]`)
- **Nội dung thị giác được bảo tồn:**
  * 4 sự kiện nhật ký chặn liên tiếp khớp với phép đo cổng Case C:
    1. Sự kiện 1: Biểu tượng Action `X` (Block màu đỏ), thời gian `Oct 4 14:20:18`, giao diện `CASE_C_KALI`, nhãn quy tắc `CASE C baseline pass Kali to Windows (100000104)`, nguồn `192.168.56.10:59801`, đích `192.168.56.20:445`, giao thức `TCP:S`.
    2. Sự kiện 2: Biểu tượng Action `X` (Block màu đỏ), thời gian `Oct 4 14:20:18`, giao diện `CASE_C_KALI`, nhãn quy tắc `CASE C baseline pass Kali to Windows (100000104)`, nguồn `192.168.56.10:59801`, đích `192.168.56.20:139`, giao thức `TCP:S`.
    3. Sự kiện 3: Biểu tượng Action `X` (Block màu đỏ), thời gian `Oct 4 14:20:19`, giao diện `CASE_C_KALI`, nhãn quy tắc `CASE C baseline pass Kali to Windows (100000104)`, nguồn `192.168.56.10:59803`, đích `192.168.56.20:139`, giao thức `TCP:S`.
    4. Sự kiện 4: Biểu tượng Action `X` (Block màu đỏ), thời gian `Oct 4 14:20:19`, giao diện `CASE_C_KALI`, nhãn quy tắc `CASE C baseline pass Kali to Windows (100000104)`, nguồn `192.168.56.10:59803`, đích `192.168.56.20:445`, giao thức `TCP:S`.
  * Cột nhãn quy tắc hiển thị đầy đủ, không bị cắt xén hay che giấu.
- **Thành phần giao diện bị loại bỏ:**
  * Hàng trăm dòng nhật ký hệ thống không liên quan trong trang nhật ký dài 17.637 pixel (gồm các bản ghi IGMP, IPv6 và DHCP ở các mốc thời gian khác).
  * Vùng lề trình duyệt ngoài rìa trái ($x < 40\,\text{px}$) và rìa phải ($x > 1320\,\text{px}$).
- **Lý do cắt cúp:** Thu hẹp từ tệp ảnh toàn trang cực lớn ($17.637\,\text{px}$) về đúng cụm 4 bản ghi lưu lượng SMB SYN bị chặn có liên quan trực tiếp đến đợt đo Case C, bảo đảm độ phân giải văn bản rõ nét khi đưa vào báo cáo.
- **Ranh giới kỹ thuật được bảo tồn:**
  * Bức ảnh minh chứng hành động `Block` đối với lưu lượng `TCP:S` từ `192.168.56.10` tới `192.168.56.20:139` và `192.168.56.20:445` trên giao diện `CASE_C_KALI`.
  * **Mâu thuẫn nhãn quy tắc được bảo tồn nguyên trạng:** Tên quy tắc hiển thị trên ảnh là `CASE C baseline pass Kali to Windows (100000104)` không trùng khớp với tên quy tắc `CASE C - Block SMB Kali to Windows (1000000104)` trong tệp manifest; việc cắt cúp bảo tồn nguyên vẹn cột nhãn này để đối chiếu khách quan và báo cáo không khẳng định tên quy tắc cụ thể nào đã khớp.
  * Bức ảnh không dùng để chứng minh mối quan hệ nhân quả tuyệt đối hay sự đồng bộ đồng hồ tuyệt đối giữa Kali và pfSense.
