# TỰ ĐÁNH GIÁ BẢN THẢO MỤC 3.5 CASE C — VÒNG HIỆU CHỈNH R2 (CH3_35_CASEC_DRAFT_SELF_REVIEW_R1)

- **Trạng thái:** `X7E1_CASEC_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7E1 R2 — Correct Chapter 3 Section 3.5 Case C`
- **Ngày thực hiện:** 2026-10-07
- **Đối tượng đánh giá:** [CH3_35_CASEC_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_35_CASEC_DRAFT_R1.md)
- **Tài liệu tham chiếu:**
  * [X7E1_R2_CORRECT_CH3_35_CASEC.md](file:///e:/word_ppt-auto/work/do-an/prompts/X7E1_R2_CORRECT_CH3_35_CASEC.md)
  * [X7E1_CH3_35_EXTERNAL_REVIEW_R1.md](file:///e:/word_ppt-auto/work/do-an/X7E1_CH3_35_EXTERNAL_REVIEW_R1.md)
  * [CH3_35_CASEC_CROP_MANIFEST_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_35_CASEC_CROP_MANIFEST_R1.md)

---

## 1. Tổng Hợp Chỉ Số Bản Thảo R2 (R2 Draft Metrics)

| Chỉ số kiểm tra | Yêu cầu thiết kế R2 | Thực tế đạt được R2 | Đánh giá |
|---|---|---|---|
| **Số từ phần văn xuôi (Prose word count)** | 1.300 – 1.450 từ | **1.442 từ** (không tính Bảng 3.6 và chú thích ảnh) | **ĐẠT** |
| **Số đoạn văn xuôi (Paragraph count)** | $\le$ 15 đoạn | **15 đoạn** | **ĐẠT** |
| **Cấu trúc tiêu đề H2** | Đúng 1 H2 (`3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense`) | 1 H2 chuẩn | **ĐẠT** |
| **Cấu trúc tiêu đề H3** | Đúng 2 H3 (`3.5.1`, `3.5.2`) | 2 H3 chuẩn, không có H3 phát sinh | **ĐẠT** |
| **Số lượng bảng biểu** | Đúng 1 bảng (`Bảng 3.6`) | 1 bảng (`Bảng 3.6`, 4 cột, 10 hàng dữ liệu thu gọn) | **ĐẠT** |
| **Số lượng hình ảnh** | Đúng 3 hình (`Hình 3.9`, `Hình 3.10`, `Hình 3.11`) | 3 hình, giữ nguyên SHA byte-identical của 3 tệp ảnh | **ĐẠT** |
| **Kiểm tra linter học thuật** | 0 cảnh báo / 0 lỗi | `lint_vi_academic.py`: 0 phát hiện | **ĐẠT** |

---

## 2. Báo Cáo Xử Lý Các Điểm Hiệu Chỉnh R2 (R2 Correction Audit)

### 2.1. Khắc phục dứt điểm ranh giới nguyên nhân kịch bản NSE04 (MS17-010)
- **Đã xóa triệt để:** Ý suy đoán nguyên nhân bên trong script (`không đưa ra phán quyết lỗ hổng do lưu lượng bị chặn`).
- **Câu chuẩn hóa áp dụng:**
  > *“Phép đo NSE-SMB-04 ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT. Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có. Kết quả này không đồng nghĩa với việc máy chủ đã an toàn hay nguy cơ đã được loại bỏ (`UNKNOWN != SAFE`).”*
- **Đánh giá:** Hoàn toàn tuân thủ ranh giới tri nhận, không suy diễn nguyên nhân script không trả về kết quả.

### 2.2. Khắc phục các khẳng định tuyệt đối về máy chủ Windows
- **Đã loại bỏ:** Các phát biểu toàn tri hoặc suy diễn lịch sử nhị phân liên tục (`mã nhị phân máy chủ không tiếp nhận bất kỳ thay đổi nào`, `thuần túy là kết quả kiểm soát mạng của pfSense`).
- **Câu chuẩn hóa áp dụng:**
  > *“Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá trên Windows. Trạng thái ghi nhận cuối lượt Case C cho thấy SMB1=True, SMB2=True, LanmanServer=Running, listener cục bộ 139/445 hiện diện và trạng thái bản vá vẫn được phân loại UNPATCHED dựa trên phiên bản số so sánh bản vá của driver `srv.sys` là `6.3.9600.16421`. Các quan sát FILTERED từ Kali được đối chiếu với các bản ghi Block tương ứng trên pfSense; việc này không làm thay đổi phân loại bản vá cục bộ của máy chủ.”*
- **Đánh giá:** Chuyển sang khẳng định dựa trên thao tác được ghi nhận và trạng thái tại thời điểm kiểm tra, không khẳng định pfSense là nguyên nhân duy nhất cho mọi tuyến mạng.

### 2.3. Xử lý trung thực việc thiếu hàng tiêu đề tại Hình 3.11
- **Giữ nguyên tệp ảnh phái sinh:** `Hinh_3_11_pfSense_Block_Log.png` ($1280 \times 220\,\text{px}$, SHA-256: `8333c06da3...`) với khung cắt cúp `x=40, y=15355, w=1280, h=220`. Không tạo ảnh ghép (montage) và không thêm chú thích nhân tạo vào ảnh.
- **Bổ sung hướng dẫn đọc trường dữ liệu trong văn bản:**
  > *“Trong các dòng log được trích, các trường lần lượt thể hiện hành động xử lý, thời điểm, giao diện, nhãn quy tắc, địa chỉ nguồn, địa chỉ đích và giao thức.”*
- **Cập nhật Bảng kê cắt cúp ([CH3_35_CASEC_CROP_MANIFEST_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_35_CASEC_CROP_MANIFEST_R1.md)):** Ghi rõ khung cắt cúp không chứa hàng tiêu đề cột do tiêu đề nằm ở đỉnh trang nguồn dài 17.637 pixel; thứ tự các trường được kiểm chứng từ giao diện gốc đầy đủ.

### 2.4. Tinh gọn đoạn văn phân tích thứ tự quy tắc (Hình 3.9)
- **Đã loại bỏ:** Lời giải thích mang tính giảng giải cơ chế bộ lọc pf (`Do bộ lọc pf áp dụng nguyên tắc so khớp từ trên xuống... gói tin sẽ khớp... và bị chặn trước...`).
- **Câu chuẩn hóa áp dụng:**
  > *“Hình 3.9 cho thấy quy tắc Block lưu lượng IPv4 TCP tới cổng `SMB_Ports` (Dòng 1) được đặt phía trên quy tắc Pass baseline (Dòng 2) trên giao diện `CASE_C_KALI`, đi kèm cờ ghi nhật ký được kích hoạt. Hình này xác nhận cấu hình và thứ tự hiển thị của ruleset; kết quả xử lý lưu lượng được đối chiếu bằng phép đo Nmap và nhật ký pfSense ở Mục 3.5.2.”*

### 2.5. Chuẩn hóa câu phân giải địa chỉ Layer 2 (ARP)
- **Đã thay thế:** Câu suy diễn `arp-response xác nhận kết nối thông suốt qua bridge0`.
- **Câu chuẩn hóa áp dụng:**
  > *“Kết quả Nmap ghi nhận mục tiêu ở trạng thái up với arp-response trong topology Case C.”* (Tuyến qua cầu nối được xác lập bằng cấu hình kiến trúc, không suy diễn từ riêng dòng ARP).

### 2.6. Làm tự nhiên hóa văn phong sinh viên và xóa bỏ thuật ngữ quản trị nội bộ
- Thay thế thuật ngữ nội bộ:
  * `manifest` $\rightarrow$ `tệp ghi nhận lượt chạy Case C`.
  * `báo cáo kiểm toán tiến trình` $\rightarrow$ `trạng thái/metadata ghi nhận cuối lượt Case C`.
  * `point-in-time` $\rightarrow$ `trạng thái ghi nhận tại thời điểm kiểm tra`.
  * `môi trường lab` $\rightarrow$ `môi trường thử nghiệm`.
  * `bảo đảm tính trong suốt của cầu nối` $\rightarrow$ loại bỏ cụm từ mang tính cam kết tuyệt đối.

### 2.7. Tinh gọn Bảng 3.6
- Giữ nguyên cấu trúc 4 cột, 10 hàng và tiêu đề bảng.
- Rút gọn toàn bộ cột 4 (*Diễn giải trực tiếp & Giới hạn kết luận*) thành các câu ngắn gọn, súc tích:
  * *Vị trí kiểm soát mạng:* Đường thử nghiệm Case C được bố trí qua pfSense Transparent Bridge trên dải mạng `192.168.56.0/24`.
  * *Chính sách lọc:* Ruleset chặn TCP 139/445 từ Kali tới Windows, có bật cờ ghi nhật ký.
  * *Thứ tự quy tắc:* Quy tắc Block SMB_Ports được đặt phía trên quy tắc Pass baseline.
  * *TCP 139:* FILTERED/no-response từ Kali; không suy ra cổng local đã đóng.
  * *TCP 445:* FILTERED/no-response từ Kali; FILTERED != PATCHED.
  * *Nhật ký pfSense:* Lưu lượng SMB SYN tương ứng được ghi nhận Block; không quy thuộc tuyệt đối theo tên rule.
  * *MS17-010:* Không có phán quyết usable; UNKNOWN != SAFE.
  * *SMBv1 cục bộ:* Metadata cuối Case C ghi nhận True; không có thao tác đổi cấu hình SMB.
  * *LanmanServer/listener:* LanmanServer=Running, listener 139/445 hiện diện tại thời điểm kiểm tra.
  * *Bản vá cục bộ:* Vẫn phân loại UNPATCHED; không ghi nhận thao tác cài bản vá.

### 2.8. Tinh chỉnh đoạn kết Mục 3.5
- Loại bỏ ngôn từ đao to búa lớn (`khẳng định nguyên lý phương pháp luận`, `trạng thái an ninh của dịch vụ máy chủ`).
- Viết mạch lạc, thực nghiệm:
  > *“Kết quả Case C cho thấy trạng thái quan sát từ xa trên đường mạng và trạng thái bản vá cục bộ là hai lớp thông tin khác nhau: TCP 139/445 được ghi nhận FILTERED từ Kali, trong khi máy chủ vẫn được phân loại UNPATCHED. Việc cổng dịch vụ bị lọc trên đường thử nghiệm không đồng nghĩa với máy chủ đã được vá lỗi (`FILTERED != PATCHED`). Sự so sánh đối chiếu đa chiều giữa ba trạng thái — đường cơ sở, vô hiệu hóa SMBv1 (Case B) và kiểm soát mạng bằng pfSense (Case C) — sẽ được tổng hợp tại Mục 3.6 tiếp theo.”*

---

## 3. Kiểm Tra Toàn Văn Các Chuỗi Nghiêm Cấm (Problematic Strings Audit)

Đã quét tự động kiểm tra trên toàn bộ bản thảo [CH3_35_CASEC_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_35_CASEC_DRAFT_R1.md):

| Chuỗi ký tự kiểm tra | Số lần xuất hiện | Đánh giá |
|---|---|---|
| `do lưu lượng bị chặn` | **0** | **SẠCH** |
| `do cổng 445` | **0** | **SẠCH** |
| `script không thể` | **0** | **SẠCH** |
| `thuần túy là kết quả` | **0** | **SẠCH** |
| `mã nhị phân máy chủ không tiếp nhận bất kỳ thay đổi` | **0** | **SẠCH** |
| `bảo đảm tính trong suốt` | **0** | **SẠCH** |
| `xác nhận kết nối thông suốt qua cầu nối` | **0** | **SẠCH** |
| `point-in-time` | **0** | **SẠCH** |
| `báo cáo kiểm toán tiến trình` | **0** | **SẠCH** |
| `khẳng định nguyên lý phương pháp luận` | **0** | **SẠCH** |
| `manifest` (trong văn xuôi sinh viên) | **0** | **SẠCH** |
| `nhân quả` | **0** | **SẠCH** |

---

## 4. Xác Thực Tính Bất Biến Của Các Tệp Hình Ảnh (Image SHA Invariance)

| Tệp hình ảnh phái sinh | SHA-256 R1 | SHA-256 R2 | Kết luận |
|---|---|---|---|
| `Hinh_3_9_pfSense_Rule_Order.png` | `5b8a4a3b26c6aca6b667e5a4ee256c48dcdd555324e2f7ed0755ae80eba06285` | `5b8a4a3b26c6aca6b667e5a4ee256c48dcdd555324e2f7ed0755ae80eba06285` | **Trùng khớp 100%** |
| `Hinh_3_10_Nmap_Filtered.png` | `da342f6fb9909da67fd38caedf73e2f848ac3c65306ec5993f864f9260418942` | `da342f6fb9909da67fd38caedf73e2f848ac3c65306ec5993f864f9260418942` | **Trùng khớp 100%** |
| `Hinh_3_11_pfSense_Block_Log.png` | `8333c06da3e35553481d00a7f84c4d65b64dde5a4f7aadc77567d52d113c919b` | `8333c06da3e35553481d00a7f84c4d65b64dde5a4f7aadc77567d52d113c919b` | **Trùng khớp 100%** |

---

## 5. Kết Luận Tự Đánh Giá R2

Bản thảo R2 đã giải quyết trọn vẹn và dứt điểm toàn bộ các điểm phản biện từ External Review R1, đưa dung lượng văn xuôi về đúng khoảng tối ưu (1.442 từ), bảo tồn nghiêm ngặt ranh giới kỹ thuật và tính trung thực của bằng chứng thực nghiệm.

Trạng thái sẵn sàng: **`X7E1_CASEC_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`**
