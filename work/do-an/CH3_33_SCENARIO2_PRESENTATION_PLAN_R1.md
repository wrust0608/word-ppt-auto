# KẾ HOẠCH TRÌNH BÀY DỮ LIỆU MỤC 3.3 SCENARIO 2 (CH3_33_SCENARIO2_PRESENTATION_PLAN_R1)

- **Trạng thái:** `R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7C0 R2 — Correct Scenario 2 Evidence/Presentation Plan`
- **Ràng buộc tuyệt đối:** **TUYỆT ĐỐI KHÔNG SOẠN VĂN XUÔI BÁO CÁO (ZERO REPORT PROSE)**. Tài liệu này chỉ thiết kế câu hỏi người đọc, cấu trúc tiểu mục H3, thiết kế bảng biểu báo cáo sinh viên theo hướng kết quả đo đạc (result-oriented), kế hoạch bố trí hình ảnh kèm khung cắt cúp dự kiến có thể tái lập, phương án trình bày kết quả âm tính/không xác định của NSE-SMB-04, phân định ranh giới độc lập giữa mốc chuẩn cục bộ và quan sát từ xa, và chuyển tiếp ý niệm sang Kịch bản tiếp theo (Case B).

---

## 1. Câu Hỏi Trọng Tâm Dành Cho Người Đọc Luận Văn (Reader Question)

> *Từ góc nhìn của một trạm kiểm thử từ xa qua mạng (Kali Linux), bốn phép đo NSE chuyên dụng ghi nhận được những trạng thái cổng và thuộc tính giao thức SMB nào, kết quả thực thi kịch bản kiểm tra MS17-010 thực sự trả về điều gì, và mối quan hệ phương pháp luận giữa quan sát không xác định từ xa (UNKNOWN) với hiện trạng thiếu bản vá cục bộ (UNPATCHED) được lý giải như thế nào?*

Câu hỏi này định hình Mục 3.3 thành một **phân tích thực nghiệm nghiêm ngặt về giới hạn của phép đo an toàn thông tin**:
1. Thiết lập rõ các điều kiện tiền đề về tầng mạng và giao thức (cổng mở, phương ngữ hỗ trợ, cơ chế ký số) qua NSE-SMB-01 đến NSE-SMB-03.
2. Trình bày trung thực kết quả thực thi kịch bản `smb-vuln-ms17-010` (NSE-SMB-04) khi công cụ quét không in ra phán quyết lỗ hổng.
3. Làm rõ sự tồn tại độc lập giữa kết quả đo đạc từ xa (`UNKNOWN / NO USABLE SCRIPT RESULT`) và hiện trạng cấu hình cục bộ (`UNPATCHED`), giải thích vì sao kết quả từ xa không thể suy diễn thành "hệ thống an toàn" (`UNKNOWN != SAFE`) và mốc cục bộ không thể tự động biến kết quả quét từ xa thành "khẳng định có lỗ hổng".

---

## 2. Đề Xuất Bố Cục Tiểu Mục H3 (Proposed Subsection Structure)

### 2.1. Đánh giá các phương án phân chia tiểu mục
- **Phương án 4 tiểu mục (1 H3 cho mỗi lệnh NSE):** Chia cắt quá vụn vặt văn bản, biến báo cáo thành nhật ký thực thi lệnh (command log), lặp lại các quan sát đã trình bày ở Mục 3.2.
- **Phương án 3 tiểu mục (Cổng/Giao thức, Ký số, MS17-010):** Vẫn bị phân mảnh, ký số (NSE-SMB-03) chỉ gồm một kết quả đơn lẻ không đủ dung lượng học thuật cho một tiểu mục H3 độc lập.
- **Phương án 2 tiểu mục (Khuyến nghị chính thức):** Nhóm theo hai cụm tư duy kỹ thuật rõ ràng: (1) Khảo sát các điều kiện kết nối và thuộc tính giao thức tiền đề; (2) Thực nghiệm kiểm tra dấu hiệu MS17-010 và đối chiếu giới hạn phân loại. Bố cục này đồng bộ với quy mô 2 H3 đã được phê duyệt ở Mục 3.1 và Mục 3.2.

### 2.2. Bố cục đề xuất chính thức

### `3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE`

- **`3.3.1. Khảo sát điều kiện kết nối và thuộc tính giao thức SMB (NSE-SMB-01 đến NSE-SMB-03)`**
  * *Nội dung kỹ thuật:*
    - Trình bày kết quả xác nhận trạng thái mở của cổng TCP 139 và 445 từ trạm Kali Linux với mã phản hồi `syn-ack` và TTL 128 (NSE-SMB-01).
    - Phân tích danh mục 5 phương ngữ SMB được hệ thống mục tiêu đàm phán và hỗ trợ, bao gồm phương ngữ kế thừa `NT LM 0.12 (SMBv1)` và các phương ngữ SMB2/3 (NSE-SMB-02).
    - Phân tích chính sách ký số gói tin SMB từ xa ghi nhận trên phương ngữ 3.0.2 là được hỗ trợ nhưng không bắt buộc (`Message signing enabled but not required`) (NSE-SMB-03).
  * *Phương thức thể hiện:* Sử dụng Bảng 3.4 (3 hàng đầu) để hệ thống hóa súc tích, mạch lạc; không sử dụng ảnh chụp màn hình riêng cho NSE-SMB-01, NSE-SMB-02, NSE-SMB-03 nhằm tránh dư thừa dữ liệu (vì đã được minh chứng một phần ở Mục 3.2).
  * *Ranh giới kỹ thuật:* Nhấn mạnh trạng thái mở của cổng 445 chỉ phản ánh khả năng tiếp cận dịch vụ qua mạng chứ không đồng nghĩa với việc tồn tại lỗ hổng an ninh (`445 OPEN != vulnerable`); sự hiện diện của phương ngữ SMBv1 không đồng nghĩa với việc xác nhận hệ thống dính lỗ hổng MS17-010 (`SMBv1 enabled != MS17-010 confirmed`).

- **`3.3.2. Đánh giá dấu hiệu lỗ hổng MS17-010 và đối chiếu trạng thái bản vá (NSE-SMB-04)`**
  * *Nội dung kỹ thuật:*
    - Trình bày tiến trình thực thi kịch bản `smb-vuln-ms17-010` từ trạm Kali Linux: lệnh Nmap được thực thi với tùy chọn `--script smb-vuln-ms17-010`, mục tiêu trực tuyến, cổng 445 mở, phiên quét ghi nhận thông báo hoàn tất `Nmap done`, không xuất hiện khối kết quả `Host script results:`, và không có thông báo lỗi hiển thị trong đầu ra ghi nhận (NSE-SMB-04).
    - Xác lập phân loại kỹ thuật giới hạn chuẩn xác: `UNKNOWN / NO USABLE SCRIPT RESULT` (lưu ý rõ UNKNOWN là phân loại phương pháp luận của đề án, không phải chuỗi ký tự nguyên văn do Nmap in ra).
    - Phân tích ranh giới phương pháp luận: Khẳng định nguyên tắc bất định `UNKNOWN != SAFE` (việc không có phán quyết lỗ hổng không đồng nghĩa với việc hệ thống an toàn).
    - Đối chiếu độc lập với hiện trạng bản vá cục bộ đã khóa tại Mục 3.1: *Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa.* Giải thích tính độc lập giữa hai trục dữ liệu, bác bỏ các suy diễn sai lệch (không suy diễn mốc cục bộ biến kết quả từ xa thành có lỗ hổng, tuyệt đối không dùng thuật ngữ "âm tính giả / false negative").
  * *Phương thức thể hiện:* Bảng 3.4 (hàng thứ 4 tổng kết NSE-SMB-04); Hình 3.6 (minh chứng thị giác trực tiếp phiên quét hoàn tất không có phán quyết); phần luận bàn ranh giới bằng văn xuôi chặt chẽ (bounded prose).

---

## 3. Thiết Kế Bảng Biểu Báo Cáo Sinh Viên (Student-Facing Tables)

Thiết kế **1 bảng tổng hợp duy nhất (Bảng 3.4)** theo định hướng kết quả (result-oriented), cô đọng toàn bộ 4 phép đo NSE.

### Bảng 3.4 — Trình tự và kết quả các phép đo NSE trên dịch vụ SMB từ trạm Kali Linux

- **Số hiệu dự kiến:** `Bảng 3.4` (Tiếp nối Bảng 3.1, 3.2 của Mục 3.1 và Bảng 3.3 của Mục 3.2).
- **Câu hỏi của người đọc được trả lời:** *Các phép đo NSE tuần tự từ trạm Kali Linux ghi nhận được những thuộc tính kỹ thuật nào trên cổng dịch vụ SMB, và kịch bản smb-vuln-ms17-010 trả về phán quyết gì đối với máy chủ mục tiêu?*
- **Cấu trúc cột chuẩn hóa:** `Phép đo | Mục tiêu kỹ thuật | Kết quả ghi nhận trực tiếp | Phân loại & Ranh giới kết luận`

| Phép đo | Mục tiêu kỹ thuật | Kết quả ghi nhận trực tiếp | Phân loại & Ranh giới kết luận |
|---|---|---|---|
| **NSE-SMB-01** | Kiểm tra trạng thái và phản hồi tầng giao vận của các cổng dịch vụ SMB | Cổng `139/tcp` và `445/tcp` ở trạng thái `OPEN`; phản hồi `syn-ack`, giá trị TTL bằng 128 | **Cổng dịch vụ mở (Open Ports)**<br>Từ trạm Kali, TCP 139 và 445 được ghi nhận ở trạng thái OPEN và phản hồi SYN-ACK. Trạng thái cổng mở phản ánh khả năng tiếp cận dịch vụ qua mạng, không đồng nghĩa với việc tồn tại lỗ hổng an ninh (`445 OPEN != vulnerable`). |
| **NSE-SMB-02** | Khảo sát danh mục các phương ngữ SMB được hệ thống mục tiêu hỗ trợ đàm phán | Kịch bản `smb-protocols` ghi nhận 5 phương ngữ:<br>• `NT LM 0.12 (SMBv1)`<br>• `2.0.2`, `2.1`<br>• `3.0`, `3.0.2`<br>Chú thích `[dangerous, but default]` là đầu ra nguyên văn của công cụ | **Hỗ trợ đa phương ngữ (SMBv1 Enabled)**<br>Hệ thống duy trì hỗ trợ phương ngữ SMBv1 kế thừa cùng các phương ngữ SMB2/3. Sự hiện diện của phương ngữ SMBv1 không đồng nghĩa với việc xác nhận máy chủ tồn tại lỗ hổng MS17-010 (`SMBv1 enabled != MS17-010 confirmed`). |
| **NSE-SMB-03** | Khảo sát cấu hình bảo mật và chính sách ký số gói tin SMB từ xa | Kịch bản `smb2-security-mode` (trên phương ngữ 3.0.2) ghi nhận:<br>• Ký số thông điệp: `enabled but not required` | **Ký số không bắt buộc (Signing Not Required)**<br>Chính sách ký số gói tin SMB từ xa ở trạng thái kích hoạt nhưng không bắt buộc đối với phương ngữ kiểm tra. Kết quả quan sát từ xa độc lập với các cờ cấu hình cục bộ và không khái quát hóa cho toàn bộ phương ngữ. |
| **NSE-SMB-04** | Kiểm tra dấu hiệu lỗ hổng an ninh MS17-010 bằng kịch bản chuyên dụng | Cổng 445/tcp mở; kết quả quét ghi nhận thông báo `Nmap done`; không xuất hiện khối kết quả `Host script results:`; không có thông báo lỗi hiển thị trong đầu ra ghi nhận | **Không xác định (UNKNOWN / NO USABLE SCRIPT RESULT)**<br>Kịch bản quét không sinh ra phán quyết an ninh khả dụng. Phân loại UNKNOWN là phân loại phương pháp luận của đề án, không phải chuỗi ký tự nguyên văn của Nmap. Kết quả này phản ánh giới hạn của phép đo từ xa, tuyệt đối không đồng nghĩa với việc hệ thống an toàn (`UNKNOWN != SAFE`). |

### Quy tắc sử dụng nhãn phép đo và dữ liệu loại khỏi Bảng 3.4:
- **ĐƯỢC PHÉP:** `NSE-SMB-01` đến `NSE-SMB-04` là các nhãn phép đo (measurement labels) được phê chuẩn từ phương pháp thực nghiệm tại Chương 2, được phép xuất hiện trong Bảng 3.4 và văn bản báo cáo.
- **CẤM:** Không đưa cú pháp dòng lệnh thô hoặc danh sách đối số argv của Nmap (`--max-retries 2`, `-T3`, `-oA evidence/...`).
- **CẤM:** Không đưa mã định danh quản trị nội bộ như Stable Evidence ID (`S2-RAW-01`), Claim ID (`S2-C01`), hay đường dẫn tệp trong kho lưu trữ (`NSE-SMB-01_ports.nmap`).
- **CẤM:** Không đưa các thuật ngữ ngoài phạm vi quan sát như `VULNERABLE`, `SAFE`, `NOT VULNERABLE`, `PATCHED`, `FALSE NEGATIVE`.
- **CẤM:** Không nhấn mạnh chỉ số thời gian `1.35 seconds` trong bảng công khai vì không mang giá trị phân tích an ninh.

### Đánh giá phương án tạo bảng so sánh độc lập thứ hai:
- Đã thẩm tra kỹ lưỡng đề xuất tạo thêm một bảng siêu nhỏ so sánh:
  `Phán quyết từ xa (NSE-SMB-04): UNKNOWN` đối chiếu với `Hiện trạng bản vá cục bộ (Mục 3.1): UNPATCHED`.
- **Kết luận:** **Không tạo thêm bảng thứ hai**. Một bảng chỉ gồm 2 ô thông tin sẽ làm phân mảnh không gian trình bày và tạo cảm giác bảng biểu mang tính thủ tục hành chính. Toàn bộ nội dung phân định ranh giới giữa hai trục thông tin này được trình bày bằng **văn xuôi có ranh giới chặt chẽ (bounded prose)** trong Tiểu mục 3.3.2, bảo đảm tính học thuật cao và mạch tư duy liền mạch cho người đọc.

---

## 4. Kế Hoạch Bố Trí Hình Ảnh (Figure Placement Directives)

Theo kết quả thẩm tra tại `CH3_33_SCENARIO2_FIGURE_SELECTION_R1.md`, bố trí duy nhất **1 hình ảnh (Hình 3.6)** trong Tiểu mục `3.3.2`:

### Hình 3.6 (Tạm thời) — Kết quả thực thi kịch bản smb-vuln-ms17-010 từ trạm Kali Linux
- **Vị trí đề xuất:** Đặt trong Tiểu mục `3.3.2`, ngay sau đoạn mô tả việc thực thi phép đo NSE-SMB-04.
- **Câu văn dẫn nhập đề xuất:**
  *"Hình 3.6 thể hiện giao diện dòng lệnh và kết quả thực thi kịch bản smb-vuln-ms17-010 nhắm vào cổng 445 của máy chủ mục tiêu từ trạm kiểm thử Kali Linux."*
- **Quan sát trực tiếp được phép diễn giải:**
  1. Lệnh Nmap được thực thi với tùy chọn `--script smb-vuln-ms17-010` trên cổng 445 tới IP mục tiêu `192.168.56.20`.
  2. Máy chủ mục tiêu trực tuyến (`Host is up`), cổng `445/tcp open microsoft-ds`, địa chỉ MAC xác nhận môi trường mạng nội bộ.
  3. Tiến trình quét hoàn tất với thông báo `Nmap done: 1 IP address (1 host up) scanned`.
  4. Giữa dòng cổng 445 và thông báo kết thúc quét không xuất hiện khối kết quả `Host script results:`, không có thông báo lỗi hiển thị trong đầu ra ghi nhận, và dấu nhắc shell trở lại bình thường.
- **Ranh giới nghiêm ngặt — Điều hình ảnh TUYỆT ĐỐI KHÔNG chứng minh:**
  * **CẤM:** Không được diễn giải hình ảnh này chứng minh máy chủ mục tiêu an toàn hoặc đã được vá lỗi MS17-010.
  * **CẤM:** Không được diễn giải hình ảnh này chứng minh kịch bản quét "thất bại" (failed) hay "bị tường lửa chặn" khi không có lỗi hiển thị trong đầu ra ghi nhận.
  * **CẤM:** Không được suy diễn bất kỳ mã lỗi nội bộ (NTSTATUS) nào từ giao diện dòng lệnh này.
  * **CẤM:** Không tuyên bố hình ảnh tự nó "chứng minh UNKNOWN"; hình ảnh minh chứng quan sát trực tiếp về sự vắng mặt của khối kết quả kịch bản, còn UNKNOWN là phân loại phương pháp luận giới hạn của đề án.
- **Khung cắt cúp đề xuất có thể tái lập:**
  * *Tệp nguồn:* `work/do-an/chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png` (Kích thước gốc $1280 \times 800\,\text{px}$, SHA-256: `c970e56481a920061416949ea7543dcb96f1f2f99635dbe201131073202e14ac`).
  * *Tọa độ đề xuất:* `x = 0, y = 24, width = 1280, height = 330` (tương ứng vùng `[left=0, top=24, right=1280, bottom=354]`).
  * *Vùng thông tin bảo toàn:* Giữ trọn vẹn từ dòng lệnh Nmap, trạng thái host/cổng, đến thông báo `Nmap done` và dấu nhắc shell tiếp theo.
  * *Giao diện thừa loại bỏ:* Thanh panel desktop Kali ($y < 24$) và 446 pixel màu đen trống phía dưới terminal ($y > 354$).

---

## 5. Kế Hoạch Trình Bày Kết Quả Âm Tính / Không Xác Định (Negative/Indeterminate Result Presentation)

Tiểu mục 3.3.2 phải được cấu trúc để người đọc luận văn nắm bắt trọn vẹn **7 điểm nhận thức phương pháp luận cốt lõi** đối với phép đo NSE-SMB-04:

1. **Lệnh Nmap được thực thi với kịch bản chỉ định:** Bằng chứng dòng lệnh và tệp thực thi ghi nhận lệnh Nmap được thực thi với tùy chọn `--script smb-vuln-ms17-010`.
2. **Phiên quét hoàn tất bình thường:** Phiên quét kết thúc với dòng `Nmap done`, duy trì kết nối tầng giao vận với cổng 445 đang mở, không có thông báo lỗi hiển thị trong đầu ra ghi nhận.
3. **Không xuất hiện phán quyết lỗ hổng:** Công cụ không in ra khối kết quả `Host script results:`, không có thông báo cảnh báo hay phán quyết lỗ hổng nào đối với MS17-010.
4. **Xác lập phân loại kỹ thuật chuẩn xác:** Kết quả của phép đo từ xa được phân loại giới hạn là **`UNKNOWN / NO USABLE SCRIPT RESULT`** (Không xác định / Không có kết quả kịch bản khả dụng). Đây là phân loại phương pháp luận của đề án, không phải chuỗi ký tự nguyên văn do Nmap in ra.
5. **Nguyên tắc bất định căn bản (`UNKNOWN != SAFE`):** Việc một kịch bản rà quét từ xa không đưa ra kết luận lỗ hổng hoàn toàn **không đồng nghĩa** với việc hệ thống mục tiêu an toàn, miễn nhiễm hoặc đã được áp dụng biện pháp phòng vệ trước lỗ hổng MS17-010.
6. **Mốc chuẩn cục bộ không chuyển hóa kết quả từ xa:** *Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa.* Trạng thái thiếu bản vá nội tại không thể dùng để gán ghép hay biến kết quả đo đạc từ xa thành "khẳng định có lỗ hổng" (`VULNERABLE`).
7. **Không suy đoán nguyên nhân vắng mặt đầu ra:** Tuyệt đối không phỏng đoán các nguyên nhân không có trong dữ liệu quan sát trực tiếp (như suy đoán về cơ chế xử lý IPC$, mã phản hồi NTSTATUS, hay giả định kịch bản bị lỗi).

> [!CAUTION]
> **Răn đe thuật ngữ:** Tuyệt đối không sử dụng thuật ngữ **"âm tính giả" (false negative)** để mô tả phép đo NSE-SMB-04 trong văn bản luận văn. Thuật ngữ này giả định trước một kỳ vọng kết quả từ xa và làm sai lệch tính khách quan của phép đo thực nghiệm độc lập.

---

## 6. Ranh Giới Kỹ Thuật Độc Lập Giữa Quan Sát Cục Bộ Và Đo Đạc Từ Xa (Independence Discipline)

Mục 3.3 phải duy trì sự phân định rạch ròi giữa hai trục quan sát độc lập đã được xác lập trong thiết kế thực nghiệm:

```
+-----------------------------------------------------------------------------------+
| TRỤC 1: QUAN SÁT CỤC BỘ (LOCAL BASELINE - MỤC 3.1)                                 |
| - Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED                     |
| - Căn cứ: srv.sys = 6.3.9600.16421 thấp hơn ngưỡng tối thiểu 6.3.9600.18604       |
| - Danh mục hotfix quan sát được không ghi nhận KB4012213, KB4012216 hoặc          |
|   bản cập nhật thay thế đã được ánh xạ là chứa bản sửa lỗi MS17-010               |
+-----------------------------------------------------------------------------------+
                                         |
                                         | KHÔNG HÒA GIẢI / KHÔNG SUY DIỄN CHÉO
                                         v
+-----------------------------------------------------------------------------------+
| TRỤC 2: ĐO ĐẠC TỪ XA (REMOTE OBSERVATION - MỤC 3.3)                               |
| - Thăm dò mạng từ trạm Kali Linux qua kịch bản smb-vuln-ms17-010                  |
| - Kết quả: Scan hoàn tất, cổng 445 mở, không xuất hiện Host script results        |
| - Phân loại: UNKNOWN / NO USABLE SCRIPT RESULT (Không có kết quả khả dụng)       |
+-----------------------------------------------------------------------------------+
```

### Các quy tắc cấm suy diễn chéo tuyệt đối:
- **CẤM:** Không được lập luận: *Vì máy chủ cục bộ là UNPATCHED nên kịch bản NSE từ xa là VULNERABLE*.
- **CẤM:** Không được lập luận: *Vì kịch bản NSE từ xa không báo lỗi nên máy chủ là SAFE hoặc PATCHED*.
- **CẤM:** Không được lập luận: *Sự sai khác giữa UNPATCHED và UNKNOWN chứng minh kịch bản Nmap bị lỗi hoặc sinh ra âm tính giả*.
- **Phân định chính sách ký số:**
  * Quan sát từ xa (NSE-SMB-03) ghi nhận `Message signing enabled but not required` trên phương ngữ 3.0.2.
  * Quan sát cục bộ (Mục 3.1) ghi nhận thuộc tính cấu hình máy chủ `RequireSecuritySignature = False`.
  * Hai quan sát này đến từ hai tầng đo đạc khác nhau (đàm phán giao thức qua mạng vs thiết lập cấu hình trong hệ điều hành), không được hòa giải hay dùng quan sát này để xác nhận quan sát kia.

---

## 7. Đoạn Chuyển Tiếp Ý Niệm Sang Kịch Bản Tiếp Theo (Conceptual Transition to Case B)

Sau khi hoàn tất trạng thái baseline và hai kịch bản đo đạc ban đầu (khảo sát bề mặt dịch vụ SMB tại Kịch bản 1 và kiểm tra dấu hiệu MS17-010 bằng NSE tại Kịch bản 2), nghiên cứu chuyển tiếp sang pha thực nghiệm can thiệp có kiểm soát (Case B).

*Ý niệm chuyển tiếp:*
> Bước thực nghiệm tiếp theo thực hiện thay đổi một biến số duy nhất trong mô hình thử nghiệm: tiến hành cấu hình vô hiệu hóa giao thức SMBv1 trên máy chủ Windows Server 2012 R2, sau đó thực hiện lặp lại các phép đo được chọn (bao gồm phép đo kiểm tra phương ngữ và phép đo kiểm tra kịch bản MS17-010) để đối chiếu sự thay đổi về danh mục phương ngữ và phản hồi từ xa từ góc nhìn trạm kiểm thử.

*(Lưu ý: Không tiết lộ bất kỳ số liệu hay kết quả cụ thể nào của Case B tại thời điểm này; các phân tích đánh giá hiệu quả toàn diện thuộc về phạm vi Chương 4).*
