# BẢNG KÊ CẮT CÚP HÌNH ẢNH MỤC 3.2 SCENARIO 1 (CH3_32_SCENARIO1_CROP_MANIFEST_R1)

- **Trạng thái:** `COMPLETED_AND_VERIFIED`
- **Pha thực hiện:** `X7B1 — Draft Chapter 3 Section 3.2 Scenario 1`
- **Ngày thực hiện:** 2026-10-06
- **Nguyên tắc bảo tồn bằng chứng:**
  1. Tuyệt đối không chỉnh sửa byte của các tệp bằng chứng gốc tại `work/do-an/chapter3/evidence/scenario1/`.
  2. Kích thước nguồn được xác định chính xác ($1280 \times 800\,\text{px}$) bằng phương pháp lập trình trước khi thực hiện cắt cúp.
  3. Chỉ tạo bản phái sinh phục vụ trình bày báo cáo tại `work/do-an/chapter3/presentation/3_2/`.
  4. Đã kiểm tra trực quan từng ảnh phái sinh, bảo đảm không làm mất bất kỳ thông số kỹ thuật hay ngữ cảnh nào cần thiết cho bài viết.
  5. Tuyệt đối không chỉnh màu, không làm sắc nét nhân tạo, không chú thích đè hoặc thêm bất kỳ ký hiệu đồ họa nào.

---

## 1. Bảng Kê Chi Tiết Các Hình Ảnh Phái Sinh (Derived Images Manifest)

### 1.1. Hình 3.4 — Kết quả thăm dò phiên bản dịch vụ SMB từ xa bằng công cụ Nmap
- **Tệp nguồn (Source Path):** `work/do-an/chapter3/evidence/scenario1/Scenario1_B5_SMB_Version.png`
- **SHA-256 nguồn:** `05699e248fa66ab224adc6809fb057a282d86c29c3ce2851823e07bd874f6466`
- **Kích thước nguồn (Source Dimensions):** $1280 \times 800\,\text{px}$
- **Tệp phái sinh (Derived Path):** `work/do-an/chapter3/presentation/3_2/Hinh_3_4_SMB_Version.png`
- **SHA-256 phái sinh:** `513f3356792eec5f449003a43f5fa8520a7fda94d8e10d4edbb6ef62fc064964`
- **Kích thước phái sinh (Derived Dimensions):** $1280 \times 310\,\text{px}$
- **Chế độ (Mode):** `CROP`
- **Khung cắt cúp thực tế (Crop Rectangle):** `x = 0, y = 24, width = 1280, height = 310` (tương ứng vùng tọa độ `[left=0, top=24, right=1280, bottom=334]`)
- **Nội dung thị giác được bảo tồn:**
  * Dòng dấu nhắc lệnh terminal của trạm kiểm thử Kali Linux (`┌──(kali㉿10)-[~/evidence/scenario1]`).
  * Toàn bộ câu lệnh Nmap đã thực thi: `sudo nmap -sS -sV --version-intensity 5 -p 139,445 192.168.56.20 -T3 --max-retries 2 -oA b5_smb_version`.
  * Dòng thông tin khởi động Nmap 7.99 và địa chỉ IP mục tiêu `192.168.56.20`.
  * Bảng trạng thái cổng và phiên bản dịch vụ: cổng 139/tcp (`open netbios-ssn Microsoft Windows netbios-ssn`) và cổng 445/tcp (`open microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds`).
  * Dòng thông tin địa chỉ MAC mục tiêu `08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)`.
  * Dòng nhận diện hệ điều hành suy đoán: `Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows`.
  * Thông báo hoàn thành phiên quét và dòng dấu nhắc lệnh trả về.
- **Thành phần giao diện bị loại bỏ:**
  * Thanh panel hệ thống trên cùng của Kali XFCE ($y < 24\,\text{px}$).
  * Vùng không gian nền terminal trống trải phía dưới ($y > 334\,\text{px}$, chiếm 466 pixel chiều cao).
- **Lý do cắt cúp:** Loại bỏ vùng nền terminal đen trống không mang thông tin, tối ưu hóa tỷ lệ khung hình trên trang in A4 portrait giúp tăng kích thước phông chữ và độ rõ nét cho người đọc.
- **Ranh giới kỹ thuật được bảo tồn:** Giữ nguyên toàn vẹn dòng kết quả nhận diện phiên bản; không suy diễn bức ảnh này chứng minh hệ điều hành đích là Windows Server 2012 R2 chính xác (chỉ chứng minh khoảng nhận diện của Nmap là `2008 R2 - 2012`).

---

### 1.2. Hình 3.5 — Kết quả phân tích phương ngữ, tính năng và chính sách ký số SMB bằng tập kịch bản Nmap NSE
- **Tệp nguồn (Source Path):** `work/do-an/chapter3/evidence/scenario1/Scenario1_B6_SMB_NSE_A.png`
- **SHA-256 nguồn:** `b5b236cbe695b530b44e0af592f010f1f49bef9f5da427b9958fd9020bd651f8`
- **Kích thước nguồn (Source Dimensions):** $1280 \times 800\,\text{px}$
- **Tệp phái sinh (Derived Path):** `work/do-an/chapter3/presentation/3_2/Hinh_3_5_SMB_NSE.png`
- **SHA-256 phái sinh:** `45faf0f03f57ce35707e1825f555fcbb6ad5e9fdee5daac7f849351ec2360a66`
- **Kích thước phái sinh (Derived Dimensions):** $1280 \times 710\,\text{px}$
- **Chế độ (Mode):** `CROP`
- **Khung cắt cúp thực tế (Crop Rectangle):** `x = 0, y = 24, width = 1280, height = 710` (tương ứng vùng tọa độ `[left=0, top=24, right=1280, bottom=734]`)
- **Nội dung thị giác được bảo tồn:**
  * Dòng dấu nhắc lệnh terminal của Kali Linux.
  * Toàn bộ câu lệnh thực thi Nmap NSE: `sudo nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities 192.168.56.20 -T3 --max-retries 2 -oA b6_smb_nse` (cho thấy rõ ràng tham số có gọi kịch bản `smb-os-discovery`).
  * Bảng cổng 139 và 445 mở.
  * Cây kết quả kịch bản `smb-protocols` với đầy đủ 5 phương ngữ: `NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, `3.0.2`.
  * Cây kết quả kịch bản `smb2-capabilities` liệt kê tính năng kỹ thuật DFS, Leasing, Multi-credit operations.
  * Khối kết quả kịch bản `smb2-security-mode` xác định `Message signing enabled but not required`.
  * Sự vắng mặt trực quan của khối đầu ra `smb-os-discovery` giữa các kết quả script.
  * Thông báo kết thúc quét và dòng dấu nhắc lệnh trả về.
- **Thành phần giao diện bị loại bỏ:**
  * Thanh panel hệ thống trên cùng của Kali XFCE ($y < 24\,\text{px}$).
  * Phần chân màn hình terminal trống phía dưới ($y > 734\,\text{px}$, 66 pixel chiều cao).
- **Lý do cắt cúp:** Loại bỏ thanh menu không liên quan và phần chân trống, bảo toàn trọn vẹn ngữ cảnh thực thi dòng lệnh và cấu trúc cây dữ liệu script trên khổ giấy A4.
- **Ranh giới kỹ thuật được bảo tồn:** Không thêm bớt bất kỳ ký tự nào; chứng minh trực quan việc hỗ trợ SMBv1 song song với SMB 2.x/3.x, chính sách ký số không bắt buộc và sự vắng mặt thực tế của kết quả `smb-os-discovery`; không suy diễn bức ảnh này chứng minh sự tồn tại của lỗ hổng MS17-010.

---

## 2. Bảng Tổng Hợp Tham Số Cắt Cúp Mục 3.2

| Hình | Tệp nguồn | SHA-256 nguồn | Kích thước nguồn | Tệp phái sinh | SHA-256 phái sinh | Kích thước phái sinh | Khung cắt cúp (x, y, w, h) |
|---|---|---|---|---|---|---|---|
| **Hình 3.4** | `Scenario1_B5_SMB_Version.png` | `05699e248fa66ab224adc6809fb057a282d86c29c3ce2851823e07bd874f6466` | $1280 \times 800$ | `Hinh_3_4_SMB_Version.png` | `513f3356792eec5f449003a43f5fa8520a7fda94d8e10d4edbb6ef62fc064964` | $1280 \times 310$ | `(0, 24, 1280, 310)` |
| **Hình 3.5** | `Scenario1_B6_SMB_NSE_A.png` | `b5b236cbe695b530b44e0af592f010f1f49bef9f5da427b9958fd9020bd651f8` | $1280 \times 800$ | `Hinh_3_5_SMB_NSE.png` | `45faf0f03f57ce35707e1825f555fcbb6ad5e9fdee5daac7f849351ec2360a66` | $1280 \times 710$ | `(0, 24, 1280, 710)` |
