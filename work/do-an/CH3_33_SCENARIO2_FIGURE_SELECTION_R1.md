# BÁO CÁO LỰA CHỌN VÀ ĐÁNH GIÁ HÌNH ẢNH MỤC 3.3 SCENARIO 2 (CH3_33_SCENARIO2_FIGURE_SELECTION_R1)

- **Trạng thái:** `R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7C0 R2 — Correct Scenario 2 Evidence/Presentation Plan`
- **Phạm vi thẩm tra:** Toàn bộ 17 tệp bằng chứng Kịch bản 2 đã stage tại `work/do-an/chapter3/evidence/scenario2/`, bao gồm:
  - 4 tệp ảnh chụp terminal trực tiếp: `Scenario2_NSE01_Ports.png`, `Scenario2_NSE02_Protocols.png`, `Scenario2_NSE03_Signing.png`, `Scenario2_NSE04_MS17010.png`
  - 4 bộ ba tệp thô máy đọc (`.nmap`, `.xml`, `.gnmap` cho các phép đo NSE-SMB-01 đến NSE-SMB-04, tổng cộng 12 tệp)
  - 1 tệp siêu dữ liệu thực thi: `Scenario2_Run_Manifest.txt`
- **Nguyên tắc lựa chọn và răn đe chống Screenshot Spam:**
  1. **Không mặc định giữ lại mọi ảnh có sẵn:** Kịch bản 2 có 4 ảnh chụp terminal, nhưng không giữ toàn bộ 4 ảnh chỉ vì chúng tồn tại. Phải đánh giá độc lập giá trị gia tăng của từng ảnh đối với người đọc luận văn.
  2. **Xử lý trùng lặp thông tin với Mục 3.2:** Các phép đo NSE-SMB-01, NSE-SMB-02, NSE-SMB-03 có nội dung quan sát trùng lặp với các bước B4 và B6 đã được trình bày chi tiết tại Mục 3.2 (Bảng 3.3 và Hình 3.5). Do đó, các kết quả lặp lại này được tích hợp súc tích vào bảng kết quả tổng hợp thay vì phân tán thành nhiều hình chụp terminal.
  3. **Đánh giá đặc thù của ảnh kết quả âm tính / không xác định (Negative/Indeterminate Result):** Ảnh `Scenario2_NSE04_MS17010.png` tuy có lượng dòng đầu ra ngắn (không xuất hiện khối kết quả script), nhưng mang giá trị chứng minh trực quan: lệnh Nmap được thực thi với tùy chọn `--script smb-vuln-ms17-010`, phiên quét hoàn tất và không xuất hiện khối kết quả phán quyết lỗ hổng. Tuyệt đối không tự động loại bỏ (DROP) ảnh NSE-SMB-04 chỉ vì đầu ra thưa thớt.
  4. **Bảo tồn tính toàn vẹn bằng chứng gốc:** 100% byte của các tệp ảnh gốc được giữ nguyên vẹn. Pha X7C0 chỉ đề xuất tọa độ cắt cúp dự kiến (provisional crop rectangle) phục vụ trang in A4, không tạo tệp ảnh phái sinh thực tế.
  5. **Đánh số tạm thời:** Tiếp nối sổ bộ `CHAPTER_3_NUMBERING_LEDGER.md`, bảng tiếp theo bắt đầu từ **Bảng 3.4**, hình tiếp theo bắt đầu từ **Hình 3.6**.

---

## 1. Bảng Đánh Giá Chi Tiết Toàn Bộ 4 Ảnh Chụp Màn Hình Kịch Bản 2

| Tệp ảnh gốc (File) | Phép đo (Measurement) | Nội dung hiển thị trực tiếp (Directly shows) | Tính độc bản so với Mục 3.2? (Unique vs 3.2?) | Bảng có thể thay thế? (Better as table?) | Giá trị chứng minh kết quả âm tính? (Negative-result value?) | Độ sắc nét (Legibility) | Cần cắt cúp? (Crop needed?) | Phân loại (KEEP / OPTIONAL / DROP) | Lý do & Đề xuất sử dụng (Reason & Proposed use) |
|---|---|---|---|---|---|---|---|---|---|
| `Scenario2_NSE01_Ports.png` | NSE-SMB-01 | Terminal Kali thực thi lệnh: `sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20`. Kết quả: `139/tcp open netbios-ssn syn-ack ttl 128`, `445/tcp open microsoft-ds syn-ack ttl 128`, địa chỉ MAC VirtualBox. | **Không**. Hoàn toàn trùng lặp với kết quả B4 đã phân tích ở Mục 3.2 (Bảng 3.3). | **Có hoàn toàn**. Dữ liệu 2 dòng cổng và lý do phản hồi `syn-ack` được đưa vào một hàng của Bảng 3.4. | Không có (kết quả ghi nhận trạng thái cổng mở). | Tốt (1280×800), chữ sắc nét trên nền tối. | Có (loại bỏ panel và vùng trống). | **DROP** | **Loại bỏ**. Tránh lặp lại ảnh chụp terminal cho hai dòng trạng thái cổng đã được khẳng định từ Mục 3.2. Bảng 3.4 thể hiện trọn vẹn thông tin này. |
| `Scenario2_NSE02_Protocols.png` | NSE-SMB-02 | Terminal Kali thực thi lệnh: `nmap -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20`. Kết quả: Cổng 445 mở; `smb-protocols` liệt kê 5 phương ngữ (`NT LM 0.12 [SMBv1]`, `2.0.2`, `2.1`, `3.0`, `3.0.2`). | **Không**. Cả 5 phương ngữ này đã được minh chứng thị giác trực tiếp trong Hình 3.5 tại Mục 3.2. | **Có hoàn toàn**. Bảng 3.4 tóm lược đầy đủ danh sách 5 phương ngữ. | Không có (kết quả ghi nhận phương ngữ thông thường). | Tốt (1280×800), chữ rõ ràng. | Có (loại bỏ panel và vùng trống). | **DROP** | **Loại bỏ**. Không cần thêm một ảnh riêng chỉ để hiển thị lại 5 phương ngữ SMB đã có ở Hình 3.5. Trình bày trong Bảng 3.4 giúp tiết kiệm diện tích trang in. |
| `Scenario2_NSE03_Signing.png` | NSE-SMB-03 | Terminal Kali thực thi lệnh: `nmap -p 445 -n -T3 --max-retries 2 --script smb2-security-mode -oA evidence/nse-smb/NSE-SMB-03_signing 192.168.56.20`. Kết quả: Cổng 445 mở; `smb2-security-mode` trên phương ngữ 3.0.2 ghi nhận `Message signing enabled but not required`. | **Không**. Kết quả signing trên phương ngữ 3.0.2 đã xuất hiện trực quan trong cây script của Hình 3.5 tại Mục 3.2. | **Có hoàn toàn**. Chỉ gồm 3 dòng kết quả script, tích hợp hoàn hảo vào hàng tương ứng của Bảng 3.4. | Không có. | Tốt (1280×800). | Có. | **DROP** | **Loại bỏ**. Nội dung quá ngắn (3 dòng kết quả) và trùng lặp thông tin với Hình 3.5. Bảng 3.4 là định dạng trình bày tối ưu nhất. |
| `Scenario2_NSE04_MS17010.png` | NSE-SMB-04 | Terminal Kali thực thi lệnh: `nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`. Kết quả: Host up, 445/tcp open, scan hoàn tất; không xuất hiện khối kết quả `Host script results:`; không có thông báo lỗi hiển thị trong đầu ra ghi nhận; shell prompt trở lại bình thường. | **Có (Độc bản & Cốt lõi)**. Đây là phép đo duy nhất thực thi kịch bản chuyên dụng kiểm tra lỗ hổng `smb-vuln-ms17-010`. Chưa từng xuất hiện ở Mục 3.1 hay 3.2. | Bảng 3.4 ghi nhận phân loại `UNKNOWN / NO USABLE SCRIPT RESULT`, ảnh cung cấp bằng chứng thị giác trực tiếp cho thấy lệnh Nmap được thực thi với tùy chọn `--script smb-vuln-ms17-010`, mục tiêu trực tuyến, cổng 445 mở, quét hoàn tất và không xuất hiện phán quyết lỗ hổng. | **Rất cao (Bằng chứng trực tiếp cho kết quả vắng mặt script output)**. Minh chứng trực quan cho thấy phiên quét kết thúc bình thường và không trả về khối `Host script results:`, đồng thời không có thông báo lỗi hiển thị trong đầu ra ghi nhận. | Rất tốt (1280×800), dòng lệnh và dấu nhắc lệnh sắc nét. | Có (cắt bỏ thanh panel Kali và vùng trống phía dưới). | **KEEP (Ưu tiên 1)** | **Hình 3.6 (Tạm thời)**. Bằng chứng thực nghiệm trung tâm của Kịch bản 2, hỗ trợ quan sát trực tiếp về việc Nmap không trả về phán quyết lỗ hổng từ xa. |

---

## 2. Đánh Giá Giá Trị Thị Giác Của Ảnh Kết Quả Âm Tính NSE-SMB-04

Một phản biện học thuật phổ biến đối với các kết quả kiểm thử an toàn thông tin là cần làm rõ tính khách quan của phép đo khi công cụ không hiển thị phán quyết lỗ hổng.

Ảnh chụp màn hình `Scenario2_NSE04_MS17010.png` cung cấp các bằng chứng thị giác trực tiếp hỗ trợ cho kết quả này:
1. **Dòng lệnh thực thi:** Ghi nhận tùy chọn `--script smb-vuln-ms17-010` được chỉ định trên cổng 445 tới IP mục tiêu `192.168.56.20`.
2. **Trạng thái kết nối và cổng:** Hiển thị `Host is up` và `445/tcp open microsoft-ds`.
3. **Tiến trình hoàn tất:** Thông báo hoàn tất phiên quét `Nmap done: 1 IP address (1 host up) scanned`.
4. **Không xuất hiện khối kết quả script:** Giữa dòng cổng 445 và thông báo kết thúc quét không xuất hiện khối `Host script results:`, và không có thông báo lỗi hiển thị trong đầu ra ghi nhận.
5. **Dấu nhắc lệnh khép kín:** Dấu nhắc lệnh `┌──(kali㉿10)-[~] └─$` trở lại bình thường.

Ảnh chụp màn hình hỗ trợ cho **quan sát trực tiếp** (direct observation) về sự vắng mặt của khối kết quả script. Phân loại kỹ thuật tương ứng của đề án là **`UNKNOWN / NO USABLE SCRIPT RESULT`**; đây là phân loại phương pháp luận chứ không phải là chuỗi ký tự nguyên văn do Nmap in ra màn hình. Việc giữ lại ảnh `Scenario2_NSE04_MS17010.png` làm **Hình 3.6** là hoàn toàn chuẩn xác và giúp báo cáo tập trung, tránh dư thừa hình ảnh.

---

## 3. Tổng Hợp Phân Bổ Hình Ảnh Cho Mục 3.3

### 3.1. Thống kê phân loại
- **Tổng số tệp ảnh đã thẩm tra:** 4 ảnh.
- **Số lượng KEEP (Giữ lại):** 1 ảnh (`Scenario2_NSE04_MS17010.png`).
- **Số lượng DROP (Loại bỏ):** 3 ảnh (`Scenario2_NSE01_Ports.png`, `Scenario2_NSE02_Protocols.png`, `Scenario2_NSE03_Signing.png`).
- **Số lượng tạo mới:** 0.

### 3.2. Phương án phân bổ đề xuất (Phương án Tinh gọn — 1 Hình)

- **Hình 3.6 (Tạm thời):**
  - **Tệp nguồn:** `work/do-an/chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png`
  - **SHA-256 nguồn:** `c970e56481a920061416949ea7543dcb96f1f2f99635dbe201131073202e14ac`
  - **Kích thước gốc:** $1280 \times 800\,\text{px}$.
  - **Chú thích đề xuất:** *Hình 3.6. Kết quả thực thi kịch bản smb-vuln-ms17-010 từ trạm Kali Linux*
  - **Vai trò chứng minh:** Minh chứng khách quan rằng phép đo kiểm tra dấu hiệu MS17-010 đã được thực thi với tùy chọn `--script smb-vuln-ms17-010` trên cổng 445 đang mở, phiên quét hoàn tất bình thường và không trả về khối dữ liệu phán quyết lỗ hổng từ xa.
  - **Ranh giới diễn giải:** Bức ảnh minh chứng quan sát trực tiếp rằng phiên quét hoàn tất mà không xuất hiện khối kết quả kịch bản; phân loại kỹ thuật giới hạn tương ứng là `UNKNOWN / NO USABLE SCRIPT RESULT`. Tuyệt đối không suy diễn bức ảnh này chứng minh máy chủ an toàn hay miễn nhiễm trước lỗ hổng MS17-010 (`UNKNOWN != SAFE`).
  - **Khung cắt cúp đề xuất có thể tái lập (Provisional Reproducible Crop Rectangle):**
    * *Tọa độ nguồn đề xuất:* `x = 0, y = 24, width = 1280, height = 330` (tương ứng vùng `[left=0, top=24, right=1280, bottom=354]`).
    * *Vùng thông tin phải giữ:* Dòng lệnh Nmap `--script smb-vuln-ms17-010` (tại $y \approx 65$), dòng trạng thái `Host is up`, dòng cổng `445/tcp open microsoft-ds`, dòng địa chỉ MAC, thông báo hoàn tất phiên quét `Nmap done` và dấu nhắc lệnh kế tiếp (kết thúc tại $y \approx 332$).
    * *Giao diện thừa loại bỏ:* Thanh panel trên cùng của giao diện desktop Kali ($y < 24$) và vùng terminal đen trống phía dưới ($y > 354$, tương ứng 446 pixel trống).
    * *Mục đích trình bày:* Tối ưu hóa kích thước hiển thị trên trang in A4 portrait, bảo đảm cỡ chữ dòng lệnh và kết quả quét to, rõ ràng, không bị nén tỷ lệ khung hình.

---

## 4. Phương Án Thay Thế Dự Phòng (Phương Án 2 Hình)

Trong trường hợp hội đồng phản biện yêu cầu đối chiếu trực quan danh sách phương ngữ ngay trong Mục 3.3 mà không muốn người đọc phải lật lại Hình 3.5 ở Mục 3.2:
- Chuyển `Scenario2_NSE02_Protocols.png` thành **OPTIONAL (Hình 3.6)**.
- Khi đó `Scenario2_NSE04_MS17010.png` sẽ là **Hình 3.7**.
- Khung cắt cúp dự kiến cho `Scenario2_NSE02_Protocols.png`: `x = 0, y = 24, width = 1280, height = 450`.
- **Khuyến nghị chính thức của Executor:** Áp dụng **Phương án Tinh gọn (1 Hình)**. Toàn bộ thông tin phương ngữ và ký số đã được Bảng 3.4 hệ thống hóa mạch lạc, việc chỉ sử dụng 1 hình cho NSE-SMB-04 giúp bài viết tập trung tối đa vào câu hỏi nghiên cứu trọng tâm của Kịch bản 2 là dấu hiệu lỗ hổng MS17-010.
