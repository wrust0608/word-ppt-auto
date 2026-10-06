# BÁO CÁO LỰA CHỌN VÀ ĐÁNH GIÁ HÌNH ẢNH MỤC 3.2 SCENARIO 1 (CH3_32_SCENARIO1_FIGURE_SELECTION_R1)

- **Trạng thái:** `R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7B0 R2 — Correct Scenario 1 Evidence/Presentation Plan`
- **Phạm vi thẩm tra:** Toàn bộ 19 tệp bằng chứng Kịch bản 1 đã stage tại `work/do-an/chapter3/evidence/scenario1/`, bao gồm 3 tệp ảnh chụp màn hình (`Scenario1_B4_SMB_Ports.png`, `Scenario1_B5_SMB_Version.png`, `Scenario1_B6_SMB_NSE_A.png`), 5 bộ ba tệp thô máy đọc (`.nmap`, `.xml`, `.gnmap` cho các bước B2–B6) và 1 tệp manifest (`Scenario1_Run_Manifest.txt`).
- **Nguyên tắc lựa chọn:**
  1. **Chống lạm dụng ảnh chụp màn hình (Anti-Screenshot Spam):** Không biến báo cáo thành album ảnh chụp màn hình terminal. Chỉ giữ ảnh khi hình ảnh công cụ trực tiếp củng cố độ tin cậy và giá trị trực quan cho người đọc mà bảng tổng hợp không thể thay thế trọn vẹn.
  2. **Ưu tiên bảng biểu cho dữ liệu ngắn:** Các kết quả phát hiện trạm mạng (B2), kiểm tra trực tuyến (B3) và trạng thái mở cổng (B4) được tích hợp vào Bảng 3.3 thay vì phân tán thành các ảnh chụp terminal rời rạc.
  3. **Bảo tồn tính toàn vẹn bằng chứng:** Tuyệt đối không chỉnh sửa byte của tệp ảnh gốc. Không tạo ảnh cắt cúp trong pha X7B0.
  4. **Chính sách cắt cúp có thể tái lập (Reproducible provisional crop rectangle):** Xác định tọa độ nguồn `(x, y, width, height)` dự kiến để sẵn sàng cho pha tạo ảnh phái sinh, loại bỏ giao diện thừa nhưng bảo tồn 100% ngữ cảnh kỹ thuật.
  5. **Số hiệu tạm thời (Tentative Numbering):** Tiếp nối `CHAPTER_3_NUMBERING_LEDGER.md`, bảng tiếp theo bắt đầu từ **Bảng 3.3**, hình tiếp theo bắt đầu từ **Hình 3.4**.

---

## 1. Bảng Đánh Giá Chi Tiết Toàn Bộ 3 Ảnh Chụp Màn Hình Kịch Bản 1

| Tệp ảnh gốc (File) | Bước đo (Step) | Nội dung hiển thị trực tiếp (Directly shows) | Thông tin độc bản? (Unique info?) | Bảng có thể thay thế? (Table can replace?) | Độ sắc nét & Bố cục (Legibility) | Cần cắt cúp? (Crop needed?) | Phân loại (KEEP / OPTIONAL / DROP) | Lý do & Đề xuất sử dụng (Reason & Proposed use) |
|---|---|---|---|---|---|---|---|---|
| `Scenario1_B4_SMB_Ports.png` | B4 | Terminal Kali thực thi quét TCP SYN cổng 139, 445: `sudo nmap -sS -p 139,445 192.168.56.20 -T3 --max-retries 2 --reason -oA b4_smb_ports`. Kết quả: `139/tcp open netbios-ssn syn-ack ttl 128`, `445/tcp open microsoft-ds syn-ack ttl 128`, địa chỉ MAC `08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)`. | **Không**. Toàn bộ trạng thái 2 cổng (139, 445 open) được lặp lại nguyên vẹn trong ảnh B5 và B6. | **Có hoàn toàn**. Dữ liệu 2 dòng cổng và lý do phản hồi `syn-ack` được trình bày gọn gàng, trang trọng trong Bảng 3.3. | Tốt (1280x800), chữ sắc nét, nhưng chỉ có 2 dòng dữ liệu cổng trên toàn bộ cửa sổ terminal rộng. | Có (nếu dùng cần cắt cửa sổ terminal). | **DROP** | **Loại bỏ**. Tránh tạo ảnh cho dữ liệu quá ngắn (2 dòng cổng). Bảng 3.3 thể hiện trọn vẹn thông tin B4, giúp tiết kiệm diện tích trang in A4 và tránh phong cách album ảnh. |
| `Scenario1_B5_SMB_Version.png` | B5 | Terminal Kali thực thi thăm dò phiên bản dịch vụ: `sudo nmap -sS -sV --version-intensity 5 -p 139,445 192.168.56.20 -T3 --max-retries 2 -oA b5_smb_version`. Kết quả: `139/tcp open netbios-ssn Microsoft Windows netbios-ssn`, `445/tcp open microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds`, dòng nhận diện `Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows`. | **Có**. Minh chứng trực tiếp chuỗi nhận diện dấu vết phiên bản dịch vụ từ xa của Nmap (`Microsoft Windows Server 2008 R2 - 2012`). | Bảng 3.3 ghi nhận chuỗi phiên bản, nhưng ảnh cung cấp bằng chứng thị giác trực tiếp cho thấy Nmap chỉ nhận diện được dải phiên bản chứ không định danh chính xác Windows Server 2012 R2. | Tốt (1280x800), chữ trắng trên nền xám terminal rõ ràng. | **Có** (cắt bỏ phần màn hình desktop Kali xung quanh). | **KEEP (Ưu tiên 2)** | **Hình 3.4 (Tạm thời)**. Minh chứng trực quan cho kết quả thăm dò dịch vụ/phiên bản từ xa, xác lập ranh giới kỹ thuật rằng Nmap chỉ giới hạn dấu vết trong dải 2008 R2–2012. *(Có thể chuyển thành OPTIONAL nếu hội đồng yêu cầu cô đọng tối đa số lượng hình).* |
| `Scenario1_B6_SMB_NSE_A.png` | B6 | Terminal Kali thực thi tập kịch bản NSE: `sudo nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities 192.168.56.20 -T3 --max-retries 2 -oA b6_smb_nse`. Kết quả: Cổng 139/445 open; `smb-protocols` liệt kê 5 phương ngữ (NT LM 0.12 [SMBv1], 2.0.2, 2.1, 3.0, 3.0.2); `smb2-capabilities` liệt kê tính năng (DFS, Leasing, Multi-credit); `smb2-security-mode` ghi nhận `Message signing enabled but not required`; hoàn toàn không có khối kết quả của `smb-os-discovery`. | **Rất cao (Độc bản & Dày đặc)**. Cung cấp bằng chứng thị giác toàn diện về các phương ngữ được hỗ trợ, cấu hình ký số, tính năng SMB2 và chứng minh thực nghiệm việc `smb-os-discovery` không có đầu ra khả dụng. | Bảng 3.3 tóm lược tham số, nhưng cây cấu trúc kết quả script trên terminal là bằng chứng thực nghiệm trực tiếp mạnh nhất cho cấu hình giao thức SMB. | Rất tốt (1280x800), phân cấp thụt lề cây dữ liệu script hiển thị mạch lạc. | **Có** (cắt bỏ viền desktop thừa bên ngoài). | **KEEP (Ưu tiên 1)** | **Hình 3.5 (Tạm thời)** [hoặc Hình 3.4 nếu B5 chuyển thành OPTIONAL]. Bằng chứng thị giác then chốt chứng minh việc hỗ trợ SMBv1 song song với SMB 2.x/3.x, chính sách ký số không bắt buộc và sự vắng mặt đầu ra của script định danh hệ điều hành. |

---

## 2. Đánh Giá Sự Vắng Mặt Của Ảnh Chụp Màn Hình B2 và B3

Trong bộ bằng chứng đã stage tại `work/do-an/chapter3/evidence/scenario1/`, hai bước B2 và B3 chỉ có các tệp máy đọc thô (`.nmap`, `.xml`, `.gnmap`), không có tệp ảnh chụp màn hình PNG chuyên biệt:

1. **Bước B2 — Phát hiện trạm mạng (`b2_host_discovery.*`):**
   - *Bản chất kỹ thuật:* Lệnh quét ARP toàn dải `/usr/lib/nmap/nmap -sn -PR -oA b2_host_discovery 192.168.56.0/24` phát hiện 4 địa chỉ IP trực tuyến (`192.168.56.1`, `192.168.56.10`, `192.168.56.20`, `192.168.56.100`).
   - *Đánh giá trình bày:* Việc hiển thị 4 dòng địa chỉ IP thông qua hàng tương ứng trong Bảng 3.3 là hoàn toàn đầy đủ, khoa học và mạch lạc.
   - *Đánh giá ảnh phái sinh:* Tuyệt đối **không tạo ảnh giả lập/ảnh phái sinh** từ văn bản thô. Điều này không mang lại giá trị học thuật gia tăng và vi phạm nguyên tắc bảo tồn tính trung thực của bằng chứng thực nghiệm.

2. **Bước B3 — Kiểm tra mục tiêu trực tuyến (`b3_target_alive.*`):**
   - *Bản chất kỹ thuật:* Lệnh thăm dò ARP đơn điểm nhắm vào `192.168.56.20` xác nhận máy chủ trực tuyến.
   - *Đánh giá trình bày:* Bước này về mặt thông tin đóng vai trò bước đệm logic xác nhận mục tiêu trước khi quét cổng. Bảng 3.3 phản ánh bước này như một mắt xích trong quy trình thực nghiệm (ghi nhận mục tiêu ở trạng thái trực tuyến). Việc không có ảnh chụp màn hình là hoàn toàn bình thường và không ảnh hưởng đến tính toàn vẹn của báo cáo.

---

## 3. Tổng Hợp Phân Loại Và Đề Xuất Bộ Hình Ảnh Cho Mục 3.2

### 3.1. Thống Kê Phân Loại
- **Tổng số tệp ảnh đã thẩm tra:** 3 ảnh.
- **Số lượng KEEP (Giữ lại):** 2 ảnh (`Scenario1_B5_SMB_Version.png`, `Scenario1_B6_SMB_NSE_A.png`) trong phương án tiêu chuẩn; hoặc 1 ảnh (`Scenario1_B6_SMB_NSE_A.png`) trong phương án tối giản.
- **Số lượng DROP (Loại bỏ):** 1 ảnh (`Scenario1_B4_SMB_Ports.png`).
- **Số lượng tạo mới:** 0 (Tuyệt đối không tạo ảnh tổng hợp giả mạo cho B2/B3).

### 3.2. Phương Án Phân Bổ Hình Ảnh Đề Xuất (Phương Án Tiêu Chuẩn — 2 Hình)

1. **Hình 3.4 (Tạm thời):**
   - **Tệp nguồn:** `work/do-an/chapter3/evidence/scenario1/Scenario1_B5_SMB_Version.png`
   - **SHA-256 nguồn:** `05699e248fa66ab224adc6809fb057a282d86c29c3ce2851823e07bd874f6466`
   - **Kích thước gốc:** $1280 \times 800\,\text{px}$.
   - **Chú thích đề xuất:** *Hình 3.4. Kết quả thăm dò phiên bản dịch vụ SMB từ xa bằng công cụ Nmap*
   - **Vai trò chứng minh:** Minh chứng khách quan rằng công cụ quét từ xa nhận diện chuỗi dịch vụ cổng 139 là `Microsoft Windows netbios-ssn` và cổng 445 là `Microsoft Windows Server 2008 R2 - 2012 microsoft-ds`.
   - **Ranh giới diễn giải:** Bức ảnh chứng minh dải phiên bản do Nmap ước lượng; tuyệt đối không khẳng định bức ảnh này chứng minh hệ điều hành đích là Windows Server 2012 R2.
   - **Khung cắt cúp đề xuất có thể tái lập (Provisional Reproducible Crop Rectangle):**
     * *Tọa độ nguồn đề xuất:* `x = 0, y = 24, width = 1280, height = 310` (tương ứng vùng `[left=0, top=24, right=1280, bottom=334]`).
     * *Vùng thông tin phải giữ:* Dòng lệnh Nmap `-sV` (tại $y \approx 65$), toàn bộ bảng kết quả `PORT STATE SERVICE VERSION`, dòng `MAC Address`, dòng `Service Info`, thông báo hoàn thành của Nmap và dòng dấu nhắc lệnh kế tiếp (kết thúc tại $y \approx 312$).
     * *Giao diện thừa loại bỏ:* Thanh panel trên cùng của Kali XFCE ($y < 24$) và vùng không gian terminal trống phía dưới ($y > 334$).
     * *Mục đích trình bày:* Loại bỏ 466 pixel trống phía dưới, tối ưu hóa tỷ lệ khung hình trên trang in A4 portrait giúp cỡ chữ dòng lệnh to, rõ ràng.

2. **Hình 3.5 (Tạm thời):**
   - **Tệp nguồn:** `work/do-an/chapter3/evidence/scenario1/Scenario1_B6_SMB_NSE_A.png`
   - **SHA-256 nguồn:** `b5b236cbe695b530b44e0af592f010f1f49bef9f5da427b9958fd9020bd651f8`
   - **Kích thước gốc:** $1280 \times 800\,\text{px}$.
   - **Chú thích đề xuất:** *Hình 3.5. Kết quả phân tích phương ngữ, tính năng và chính sách ký số SMB bằng tập kịch bản Nmap NSE*
   - **Vai trò chứng minh:** Minh chứng 5 phương ngữ SMB được hỗ trợ (đặc biệt là phương ngữ cũ NT LM 0.12 / SMBv1), chính sách ký số ở trạng thái `enabled but not required`, các khả năng kỹ thuật SMB2 (DFS, Leasing, Multi-credit) và sự vắng mặt thực tế của khối kết quả `smb-os-discovery`.
   - **Ranh giới diễn giải:** Bức ảnh không đưa ra phán quyết về lỗ hổng MS17-010; việc `smb-os-discovery` không có đầu ra chỉ được trình bày như một kết quả đo thực tế, không suy diễn nguyên nhân lỗi hay liên hệ với trạng thái an ninh.
   - **Khung cắt cúp đề xuất có thể tái lập (Provisional Reproducible Crop Rectangle):**
     * *Tọa độ nguồn đề xuất:* `x = 0, y = 24, width = 1280, height = 710` (tương ứng vùng `[left=0, top=24, right=1280, bottom=734]`).
     * *Vùng thông tin phải giữ:* Toàn bộ khối lệnh Nmap NSE đầy đủ (tại $y \approx 65$), toàn bộ cây kết quả của `smb-protocols`, `smb2-capabilities`, `smb2-security-mode` và dòng dấu nhắc lệnh kế tiếp (kết thúc tại $y \approx 712$).
     * *Giao diện thừa loại bỏ:* Thanh panel trên cùng của Kali XFCE ($y < 24$) và phần chân terminal trống phía dưới ($y > 734$).
     * *Mục đích trình bày:* Tối ưu hóa độ rõ nét của cấu trúc cây phân cấp script trên trang in A4.

### 3.3. Phương Án Thay Thế Rút Gọn (Lean Alternative — 1 Hình)
- Trong trường hợp phản biện hoặc người dùng yêu cầu tiết kiệm diện tích tối đa cho Mục 3.2:
  * Chuyển `Scenario1_B5_SMB_Version.png` thành **OPTIONAL** và chỉ trình bày chuỗi phiên bản trong Bảng 3.3.
  * Giữ duy nhất `Scenario1_B6_SMB_NSE_A.png` làm **Hình 3.4 (Tạm thời)**.
  * Ưu điểm: Mục 3.2 trở nên cực kỳ gọn gàng (1 bảng, 1 hình).
  * Nhược điểm: Mất đi bằng chứng thị giác trực tiếp về ranh giới nhận diện phiên bản hệ điều hành của Nmap.
- **Khuyến nghị của Executor:** Áp dụng Phương án Tiêu chuẩn (2 hình: Hình 3.4 và Hình 3.5) để bảo đảm tính trực quan cho cả hai khía cạnh: nhận diện dịch vụ (B5) và phân tích giao thức (B6).
