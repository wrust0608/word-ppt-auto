# BẢNG KÊ CẮT CÚP HÌNH ẢNH MỤC 3.3 SCENARIO 2 (CH3_33_SCENARIO2_CROP_MANIFEST_R1)

- **Trạng thái:** `COMPLETED_AND_VERIFIED`
- **Pha thực hiện:** `X7C1 — Draft Chapter 3 Section 3.3 Scenario 2`
- **Ngày thực hiện:** 2026-10-06
- **Nguyên tắc bảo tồn bằng chứng:**
  1. Tuyệt đối không chỉnh sửa byte của các tệp bằng chứng gốc tại `work/do-an/chapter3/evidence/scenario2/`.
  2. Kích thước nguồn được xác định chính xác ($1280 \times 800\,\text{px}$) và mã băm SHA-256 được đối soát trước khi thực hiện cắt cúp.
  3. Chỉ tạo duy nhất một tệp phái sinh phục vụ trình bày báo cáo tại `work/do-an/chapter3/presentation/3_3/Hinh_3_6_MS17010_NSE.png`.
  4. Đã kiểm tra trực quan ảnh phái sinh, bảo đảm toàn bộ dòng lệnh, trạng thái cổng, dòng hoàn tất và dấu nhắc lệnh được giữ nguyên vẹn.
  5. Tuyệt đối không chỉnh màu, không làm sắc nét nhân tạo, không chú thích đè hoặc thêm bất kỳ ký hiệu đồ họa nào.

---

## 1. Bảng Kê Chi Tiết Hình Ảnh Phái Sinh (Derived Image Manifest)

### Hình 3.6 — Kết quả thực thi kịch bản smb-vuln-ms17-010 từ trạm Kali Linux
- **Tệp nguồn (Source Path):** `work/do-an/chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png`
- **SHA-256 nguồn:** `c970e56481a920061416949ea7543dcb96f1f2f99635dbe201131073202e14ac`
- **Kích thước nguồn (Source Dimensions):** $1280 \times 800\,\text{px}$
- **Tệp phái sinh (Derived Path):** `work/do-an/chapter3/presentation/3_3/Hinh_3_6_MS17010_NSE.png`
- **SHA-256 phái sinh:** `8f7a343fe9ab100a187a5ab4fe85cac320e9350cf5d59df0c4d78e385a137bdc`
- **Kích thước phái sinh (Derived Dimensions):** $1280 \times 330\,\text{px}$
- **Chế độ (Mode):** `CROP`
- **Khung cắt cúp thực tế (Crop Rectangle):** `x = 0, y = 24, width = 1280, height = 330` (tương ứng vùng tọa độ `[left=0, top=24, right=1280, bottom=354]`)
- **Nội dung thị giác được bảo tồn:**
  * Dòng dấu nhắc lệnh terminal của trạm kiểm thử Kali Linux (`┌──(kali㉿10)-[~]`).
  * Toàn bộ câu lệnh Nmap đã thực thi: `nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`.
  * Dòng khởi động Nmap 7.99 và địa chỉ IP mục tiêu `192.168.56.20`.
  * Dòng trạng thái `Host is up (0.00047s latency)`.
  * Bảng trạng thái cổng: `445/tcp open microsoft-ds`.
  * Dòng địa chỉ MAC mục tiêu: `MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)`.
  * Thông báo hoàn tất phiên quét: `Nmap done: 1 IP address (1 host up) scanned in 1.35 seconds`.
  * Dòng dấu nhắc lệnh terminal trả về (`┌──(kali㉿10)-[~] └─$`).
- **Thành phần giao diện bị loại bỏ:**
  * Thanh panel hệ thống trên cùng của Kali XFCE desktop ($y < 24\,\text{px}$).
  * Vùng không gian nền terminal trống trải màu đen phía dưới ($y > 354\,\text{px}$, chiếm 446 pixel chiều cao).
- **Lý do cắt cúp:** Loại bỏ vùng nền terminal đen không mang thông tin, tối ưu hóa tỷ lệ khung hình trên trang in A4 portrait giúp tăng kích thước phông chữ dòng lệnh và cải thiện độ rõ nét cho người đọc.
- **Ranh giới kỹ thuật được bảo tồn:**
  * Bức ảnh minh chứng quan sát trực tiếp rằng đầu ra đạt đến dòng Nmap done, dấu nhắc shell xuất hiện sau đó, cổng 445 mở, không xuất hiện khối kết quả `Host script results:`, và không có thông báo lỗi hiển thị trong đầu ra ghi nhận.
  * Bức ảnh không tự nó chứng minh máy chủ an toàn hay đã được vá lỗi (`UNKNOWN != SAFE`).
  * Phân loại kỹ thuật tương ứng của đề án là `UNKNOWN / NO USABLE SCRIPT RESULT` (đây là phân loại phương pháp luận, không phải chuỗi ký tự nguyên văn do Nmap in ra).
