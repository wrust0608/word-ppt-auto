# BÁO CÁO TỰ ĐÁNH GIÁ DỰ THẢO MỤC 3.3 SCENARIO 2 (CH3_33_SCENARIO2_DRAFT_SELF_REVIEW_R1)

- **Trạng thái:** `X7C1_CH3_33_SCENARIO2_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7C1 R2 — Correct Section 3.3 Scenario 2 Draft`
- **Tệp dự thảo được đánh giá:** `work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md`
- **Branch:** `feature/x7c1-ch3-scenario2-draft`
- **Reviewer Base HEAD:** `f911bcd3e4c2a541efc90bb3e383b0107ec74dd5`
- **Tổ tiên tích hợp (Base commit):** `d589e51e81aa0a3b87980ac73cef0d81ca330e17`

---

## 1. Kiểm Toán Số Lượng Từ (Word Count Audit)

- **Tổng số từ toàn văn bản (kể cả bảng Markdown và cú pháp nhúng ảnh):** 1.872 từ.
- **Số từ văn xuôi (loại trừ các dòng bảng Markdown, tiêu đề đề mục và cú pháp nhúng ảnh):** 1.356 từ.
- **Số đoạn văn xuôi:** 14 đoạn văn.
- **Đánh giá phạm vi độ dài:** Nằm hoàn toàn trong khung dung lượng mục tiêu R2 (~1.300–1.550 từ văn xuôi). So với bản R1 (1.719 từ văn xuôi), bản R2 đã tinh gọn được 363 từ văn xuôi thông qua việc:
  * Loại bỏ các câu lý thuyết an ninh chung về cơ chế ký số gói tin;
  * Tinh gọn đoạn viện dẫn trạng thái bản vá cục bộ `UNPATCHED`, tham chiếu trực tiếp đến kết quả đã khóa tại Mục 3.1 mà không tái suy diễn chi tiết số nhị phân hay danh mục hotfix;
  * Rút gọn đoạn ranh giới khai thác trong văn xuôi sinh viên, loại bỏ việc liệt kê danh mục công cụ khai thác (`Meterpreter`, `reverse shell`);
  * Bỏ các diễn giải lặp lại về nguyên tắc `UNKNOWN != SAFE`.

---

## 2. Kiểm Toán Cấu Trúc Đề Mục (Heading Audit)

- **Số lượng tiêu đề H2:** Đúng 1 tiêu đề:
  * `## 3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE`
- **Số lượng tiêu đề H3:** Đúng 2 tiêu đề:
  * `### 3.3.1. Khảo sát điều kiện kết nối và thuộc tính giao thức SMB (NSE-SMB-01 đến NSE-SMB-03)`
  * `### 3.3.2. Đánh giá dấu hiệu lỗ hổng MS17-010 và đối chiếu trạng thái bản vá (NSE-SMB-04)`
- **Số lượng tiêu đề H3 phát sinh ngoài kế hoạch:** 0.
- **Số lượng tiêu đề H4 hoặc tiêu đề phụ khác:** 0.
- **Đoạn văn mở đầu:** Có đúng 1 đoạn văn mở đầu ngắn gọn nằm ngay dưới đề mục `3.3`, nêu rõ mục tiêu khảo sát các thuộc tính kỹ thuật và thăm dò dấu hiệu MS17-010 từ trạm Kali Linux nhắm vào máy chủ mục tiêu Windows Server 2012 R2 bằng tập kịch bản NSE chuyên biệt.

---

## 3. Kiểm Toán Bảng Biểu (Table Audit — Count = 1)

Dự thảo tích hợp đúng 1 bảng tổng hợp kết quả đo đạc sinh viên độc lập, tuân thủ nghiêm ngặt nguyên tắc tiếp cận hướng kết quả (result-oriented), không biến thành command log:

- **Bảng 3.4:** `Bảng 3.4. Trình tự và kết quả các phép đo NSE trên dịch vụ SMB từ trạm Kali Linux`
  - Cấu trúc: 4 cột (`Phép đo | Mục tiêu kỹ thuật | Kết quả ghi nhận trực tiếp | Phân loại & Ranh giới kết luận`).
  - Gồm 4 hàng tương ứng với 4 phép đo NSE thành phần:
    * **NSE-SMB-01:** Ghi nhận cổng `139/tcp` và `445/tcp` ở trạng thái `OPEN`, phản hồi `syn-ack`, TTL 128; phân loại là cổng dịch vụ mở (Open Ports); đóng khung ranh giới kỹ thuật `445 OPEN != vulnerable`.
    * **NSE-SMB-02:** Mục tiêu kỹ thuật đã hiệu chỉnh: `Khảo sát các phương ngữ SMB được ghi nhận từ xa`. Tiêu đề phân loại: `Các phương ngữ SMB được ghi nhận`. Ghi nhận 5 phương ngữ (`NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, `3.0.2`) kèm chú thích nguyên văn `[dangerous, but default]`; đóng khung ranh giới kỹ thuật `SMBv1 enabled != MS17-010 confirmed`.
    * **NSE-SMB-03:** Ghi nhận kịch bản `smb2-security-mode` trên phương ngữ 3.0.2 xác định chính sách ký số là `Message signing enabled but not required`; đóng khung kết quả quan sát từ xa độc lập với cờ cấu hình cục bộ và không khái quát hóa cho toàn bộ phương ngữ.
    * **NSE-SMB-04:** Cổng 445/tcp mở, phiên quét đạt dòng `Nmap done`, không xuất hiện khối kết quả `Host script results:`, không có thông báo lỗi hiển thị; phân loại phương pháp luận là `UNKNOWN / NO USABLE SCRIPT RESULT`; nêu rõ UNKNOWN không phải chuỗi ký tự nguyên văn của Nmap. Wording phân loại đã hiệu chỉnh: *"Kết quả này chỉ cho phép phân loại là chưa xác định trong phạm vi phép đo; nguyên nhân của việc không có đầu ra script khả dụng không được xác lập. UNKNOWN != SAFE."*
  - Bảng không chứa mã nội bộ (Evidence ID, Claim ID) hay đường dẫn tệp trong kho lưu trữ.

---

## 4. Kiểm Toán Hình Ảnh (Figure Audit — Count = 1) & Đường Dẫn Tệp

Dự thảo nhúng duy nhất 1 hình ảnh phái sinh phục vụ trình bày:

- **Hình 3.6:**
  - Cú pháp nhúng: `![Hình 3.6. Kết quả thực thi kịch bản smb-vuln-ms17-010 từ trạm Kali Linux](chapter3/presentation/3_3/Hinh_3_6_MS17010_NSE.png)`
  - Tệp vật lý tồn tại trên đĩa: `work/do-an/chapter3/presentation/3_3/Hinh_3_6_MS17010_NSE.png`.
  - Kích thước: 1280 × 330 px.
  - Mã băm SHA-256: `8f7a343fe9ab100a187a5ab4fe85cac320e9350cf5d59df0c4d78e385a137bdc` (bảo tồn nguyên vẹn 100%, không tái tạo ảnh trong R2).
- **Quy tắc cắt giảm:** Tuyệt đối không tạo ảnh chụp màn hình riêng cho NSE-SMB-01, NSE-SMB-02, NSE-SMB-03 theo đúng quyết định của Kế hoạch trình bày X7C0 đã được phê duyệt.

---

## 5. Kiểm Toán Tệp Thuyết Minh Cắt Cúp (Crop-Manifest Audit)

- Tệp thuyết minh cắt cúp: `work/do-an/CH3_33_SCENARIO2_CROP_MANIFEST_R1.md` đã được hiệu chỉnh câu từ theo đúng các dữ kiện thị giác trực tiếp:
  - **Tệp nguồn:** `work/do-an/chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png` (1280 × 800 px, SHA-256: `c970e56481a920061416949ea7543dcb96f1f2f99635dbe201131073202e14ac`).
  - **Khung cắt cúp chuẩn hóa:** `x=0, y=24, width=1280, height=330`.
  - **Tệp phái sinh:** `work/do-an/chapter3/presentation/3_3/Hinh_3_6_MS17010_NSE.png` (1280 × 330 px, SHA-256: `8f7a343fe9ab100a187a5ab4fe85cac320e9350cf5d59df0c4d78e385a137bdc`).
  - **Câu từ ranh giới tại dòng 40:** Đã thay thế cụm từ suy diễn *"phiên quét kết thúc bình thường"* bằng dữ kiện quan sát trực tiếp: *"đầu ra đạt đến dòng Nmap done, dấu nhắc shell xuất hiện sau đó"*.
  - Toàn bộ đường dẫn, mã băm SHA, kích thước và khung cắt cúp được giữ nguyên vẹn 100%.

---

## 6. Ma Trận Đối Chiếu Đoạn Văn – Luận Điểm Đã Hiệu Chỉnh (Paragraph-to-Claim Audit R2)

Toàn bộ văn bản dự thảo R2, Bảng 3.4 và Hình 3.6 được ánh xạ đầy đủ 100% với 15 luận điểm kỹ thuật trong `work/do-an/CH3_33_SCENARIO2_CLAIM_EVIDENCE_MAP_R1.md` (`S2-C01` đến `S2-C15`):

| Claim ID | Tiểu mục | Nội dung luận điểm đã phê duyệt | Vị trí thể hiện trong văn bản R2 | Đánh giá ranh giới kỹ thuật R2 |
|---|---|---|---|---|
| `S2-C01` | 3.3.1 | Cổng dịch vụ TCP 139 ở trạng thái mở từ xa | Đoạn 2 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 1) | Ghi nhận TCP 139 OPEN, phản hồi SYN-ACK, TTL=128 từ trạm Kali; không suy diễn kết nối phiên SMB thành công hay chia sẻ tệp sẵn sàng. |
| `S2-C02` | 3.3.1 | Cổng dịch vụ TCP 445 ở trạng thái mở từ xa | Đoạn 2 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 1) | Ghi nhận TCP 445 OPEN, phản hồi SYN-ACK, TTL=128 từ trạm Kali; chỉ phản ánh khả năng tiếp cận ở tầng giao vận. |
| `S2-C03` | 3.3.1 | Ranh giới kỹ thuật: Cổng 445 mở không đồng nghĩa với tồn tại lỗ hổng | Đoạn 2 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 1) | Khóa chặt ranh giới kỹ thuật: `445 OPEN != vulnerable`; không đồng nhất cổng mở với nguy cơ bị tấn công hay tồn tại lỗ hổng. |
| `S2-C04` | 3.3.1 | NSE-SMB-02 ghi nhận 5 phương ngữ SMB, bao gồm SMBv1 | Đoạn 3 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 2) | Kịch bản `smb-protocols` ghi nhận 5 phương ngữ (`NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, `3.0.2`); giữ nguyên chú thích nguyên văn `[dangerous, but default]` như một annotation mặc định của công cụ. |
| `S2-C05` | 3.3.1 | Ranh giới kỹ thuật: Hỗ trợ SMBv1 không đồng nghĩa với xác nhận lỗ hổng MS17-010 | Đoạn 3 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 2) | Khóa chặt ranh giới kỹ thuật: `SMBv1 enabled != MS17-010 confirmed`; không dùng các lập luận về "điều kiện cần", "điều kiện tiên quyết", hay "tính chất mất an toàn". |
| `S2-C06` | 3.3.1 | Chính sách ký số gói tin SMB từ xa là kích hoạt nhưng không bắt buộc | Đoạn 4 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 3) | Kịch bản `smb2-security-mode` trên phương ngữ 3.0.2 ghi nhận `Message signing enabled but not required`. Đã bỏ lý giải lý thuyết về tính toàn vẹn gói tin hay nghĩa vụ của client. |
| `S2-C07` | 3.3.1 | Ranh giới kỹ thuật: Quan sát ký số từ xa và cờ cấu hình ký số cục bộ độc lập với nhau | Đoạn 4 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 3) | Quan sát thăm dò từ xa của Nmap trên phương ngữ cụ thể duy trì độc lập với cờ cấu hình nội bộ tại Mục 3.1; không khái quát hóa cho mọi phương ngữ và không hòa giải trực tiếp hai tầng đo đạc. |
| `S2-C08` | 3.3.2 | Lệnh Nmap được thực thi với tùy chọn `--script smb-vuln-ms17-010` | Đoạn 1 & Đoạn 3 Tiểu mục 3.3.2, Bảng 3.4 (Hàng 4) | Ghi nhận: *"Phép đo NSE-SMB-04 được thực hiện bằng lệnh Nmap có tùy chọn --script smb-vuln-ms17-010 nhắm vào TCP 445 của 192.168.56.20."* Đã bỏ cụm từ "được kích hoạt", "gọi kịch bản chuyên biệt". |
| `S2-C09` | 3.3.2 | Đầu ra NSE-SMB-04 đạt đến dòng hoàn tất `Nmap done` | Đoạn 3 Tiểu mục 3.3.2, Bảng 3.4 (Hàng 4) | Đầu ra ghi nhận đạt đến dòng thông báo hoàn tất `Nmap done`, dấu nhắc shell xuất hiện sau đó; không có thông báo lỗi hiển thị; đã bỏ cách nói "kết thúc bình thường" hay "trả về bình thường". |
| `S2-C10` | 3.3.2 | Không xuất hiện khối kết quả `Host script results:` | Đoạn 3 Tiểu mục 3.3.2, Bảng 3.4 (Hàng 4) | Khối kết quả `Host script results:` không xuất hiện trong đầu ra ghi nhận; không có thông báo lỗi hiển thị; không bịa đặt bất kỳ kết quả NSE lịch sử nào. |
| `S2-C11` | 3.3.2 | Phân loại kỹ thuật kết quả từ xa là `UNKNOWN / NO USABLE SCRIPT RESULT` | Đoạn 4 Tiểu mục 3.3.2, Bảng 3.4 (Hàng 4) | Phân loại phương pháp luận chuẩn xác là `UNKNOWN / NO USABLE SCRIPT RESULT`; nêu rõ UNKNOWN không phải chuỗi ký tự nguyên văn do Nmap in ra màn hình. Nguyên nhân vắng mặt đầu ra không được xác lập từ bộ bằng chứng hiện có. |
| `S2-C12` | 3.3.2 | Ranh giới kỹ thuật: Kết quả không xác định từ xa không đồng nghĩa với an toàn | Đoạn 5 Tiểu mục 3.3.2, Bảng 3.4 (Hàng 4) | Khóa chặt nguyên tắc an toàn thông tin cốt lõi: `UNKNOWN != SAFE`; kịch bản không phát hiện lỗ hổng không đồng nghĩa với máy chủ an toàn; không tự suy diễn thành VULNERABLE, SAFE, NOT VULNERABLE hay PATCHED. |
| `S2-C13` | 3.3.2 | Mốc chuẩn xuất phát cục bộ duy trì trạng thái chưa cài bản vá (UNPATCHED) | Đoạn 6 Tiểu mục 3.3.2 | Viện dẫn chuẩn mực: *"Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa."* Đã loại bỏ đoạn tái suy diễn rườm rà về `srv.sys` và hotfix. |
| `S2-C14` | 3.3.2 | Ranh giới kỹ thuật: Mốc UNPATCHED cục bộ không biến kết quả từ xa thành VULNERABLE | Đoạn 6 Tiểu mục 3.3.2 | Hai trục thông tin độc lập: mốc cục bộ UNPATCHED không biến kết quả từ xa thành VULNERABLE; kết quả từ xa UNKNOWN không phủ định hiện trạng thiếu bản vá để coi máy chủ an toàn; không dùng ngôn từ âm tính giả (false negative). |
| `S2-C15` | 3.3.2 | Ranh giới phạm vi: Kịch bản 2 hoàn toàn không chứa kết quả khai thác hoặc RCE | Đoạn 7 Tiểu mục 3.3.2 | Câu văn R2 chuẩn mực: *"Về ranh giới phạm vi, Kịch bản 2 dừng ở phạm vi rà quét NSE; không có bước khai thác hoặc kết quả thực thi mã từ xa được ghi nhận trong kịch bản này."* Đã loại bỏ danh mục công cụ (`Meterpreter`, `reverse shell`). |

---

## 7. Kiểm Toán Câu Từ Ranh Giới Cổng TCP NSE01 (NSE01 TCP-Boundary Audit)

- Câu từ thể hiện chuẩn mực: *"Từ trạm Kali, TCP 139 và 445 được ghi nhận ở trạng thái OPEN và phản hồi SYN-ACK với giá trị TTL bằng 128."*
- Khóa chặt ranh giới: `445 OPEN != vulnerable`.
- Không tuyên bố dịch vụ "sẵn sàng tiếp nhận kết nối", phiên SMB tầng ứng dụng thành công, chia sẻ tệp thành công hay hệ thống vulnerable.

---

## 8. Kiểm Toán Ranh Giới Giao Thức SMBv1 và MS17-010 NSE02 (NSE02 Dialect Wording Audit)

- Câu văn R2: *"Kịch bản smb-protocols ghi nhận 5 phương ngữ: NT LM 0.12 (SMBv1), 2.0.2, 2.1, 3.0 và 3.0.2. Trong đầu ra ghi nhận của Nmap, phương ngữ NT LM 0.12 đi kèm chú thích nguyên văn [dangerous, but default]; đây là annotation mặc định của công cụ quét, không phải là kết luận hay phán quyết về lỗ hổng. Về mặt phương pháp luận, sự hiện diện của phương ngữ SMBv1 trong kết quả đo không đồng nghĩa với việc máy chủ đã được xác nhận dính lỗ hổng MS17-010 (SMBv1 enabled != MS17-010 confirmed)."*
- Đã loại bỏ hoàn toàn các cụm từ bị gắn cờ:
  * `hỗ trợ 5 phương ngữ` = 0.
  * `hỗ trợ đàm phán` = 0.
  * `Hỗ trợ đa phương ngữ` = 0.
  * `tính chất mất an toàn` = 0.
  * `tính tương thích ngược` = 0.
  * `đàm phán và lập danh mục ... chấp thuận` = 0.

---

## 9. Kiểm Toán Tính Độc Lập Của Ký Số Gói Tin NSE03 (NSE03 Signing Independence Audit)

- Câu văn R2: *"Trên phương ngữ 3.0.2 được ghi nhận, kịch bản trả về kết quả Message signing enabled but not required. Đây là quan sát thăm dò từ xa của kịch bản Nmap trên phương ngữ cụ thể này và được duy trì độc lập với các cờ cấu hình nội bộ tại Mục 3.1. Kết quả này không được khái quát hóa cho các phương ngữ khác và không dùng để đối chiếu hay hòa giải trực tiếp với thiết lập trong hệ điều hành."*
- Đã loại bỏ lý thuyết an ninh rộng về "bảo vệ tính toàn vẹn gói tin" và nghĩa vụ ký số của các trạm khách.

---

## 10. Kiểm Toán Quan Sát Trực Tiếp Phép Đo NSE04 (NSE04 Direct-Observation Audit)

- Bằng chứng lệnh và đầu ra hiển thị:
  * Câu lệnh: *"Phép đo NSE-SMB-04 được thực hiện bằng lệnh Nmap có tùy chọn --script smb-vuln-ms17-010 nhắm vào TCP 445 của 192.168.56.20."* (Đã bỏ "được kích hoạt", "gọi kịch bản chuyên biệt").
  * Đầu ra hoàn tất: *"Đầu ra ghi nhận đạt đến dòng thông báo hoàn tất Nmap done, dấu nhắc shell xuất hiện sau đó, và không có thông báo lỗi hiển thị trong đầu ra ghi nhận."* (Đã bỏ "kết thúc bình thường", "trả về bình thường").
  * Hiện diện đầu ra kịch bản: **Không xuất hiện** khối `Host script results:`.

---

## 11. Kiểm Toán Phân Loại Kỹ Thuật UNKNOWN (UNKNOWN Classification Audit)

- Phân loại kỹ thuật chuẩn xác của đề án: **`UNKNOWN / NO USABLE SCRIPT RESULT`**.
- Khẳng định tường minh: `UNKNOWN` là phân loại phương pháp luận của đề án, **không phải chuỗi ký tự nguyên văn do Nmap in ra màn hình**.
- Wording nguyên nhân đầu ra vắng mặt: *"Nguyên nhân của việc không có đầu ra script khả dụng không được xác lập từ bộ bằng chứng hiện có."* (Đã bỏ cách nói khẳng định tuyệt đối "nguyên nhân không thể xác định").
- Tuyệt đối không bịa đặt mã lỗi NTSTATUS, quyền IPC$, tài khoản guest, và không tuyên bố kịch bản bị thất bại (failed).

---

## 12. Kiểm Toán Ranh Giới An Toàn UNKNOWN != SAFE (UNKNOWN != SAFE Audit)

- Xác lập nguyên tắc an toàn thông tin cốt lõi: **`UNKNOWN != SAFE`**.
- Việc kịch bản quét từ xa không đưa ra phán quyết lỗ hổng hoàn toàn không đồng nghĩa với việc máy chủ mục tiêu an toàn, miễn nhiễm hoặc đã được cập nhật bản vá.
- Tuyệt đối không gán bất kỳ phán quyết nào sau đây cho kết quả phép đo NSE-SMB-04: `VULNERABLE`, `SAFE`, `NOT VULNERABLE`, hay `PATCHED`.

---

## 13. Kiểm Toán Tính Độc Lập Giữa UNPATCHED Cục Bộ và UNKNOWN Từ Xa (Independence Audit)

- Wording ưu tiên được thực hiện chuẩn xác: *"Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa."*
- Đã loại bỏ việc tái diễn giải dài dòng các số hiệu `srv.sys` và hotfix trong Mục 3.3.
- Đã loại bỏ hoàn toàn các cụm từ:
  * `ngưỡng cập nhật an toàn tối thiểu` = 0.
  * `các bản cập nhật thay thế tương ứng` = 0.
- Ranh giới tuyệt đối được bảo tồn:
  * Không dùng `UNPATCHED` để suy diễn kết quả từ xa thành `VULNERABLE`.
  * Không dùng `UNKNOWN` để phủ định hiện trạng thiếu bản vá nhằm tuyên bố hệ thống an toàn hay đã vá (`PATCHED`).

---

## 14. Kiểm Toán Ngôn Từ Âm Tính Giả (No False-Negative Language Audit)

- Rà soát tự động xác nhận số lần xuất hiện của các cụm từ sau trong văn xuôi sinh viên là **0**:
  * `false negative` / `False Negative`: 0.
  * `âm tính giả`: 0.
- Văn bản giải thích rõ: sự khác biệt giữa hai trục quan sát phản ánh khoảng cách tự nhiên giữa kiểm tra cấu hình nội bộ và thăm dò động từ xa qua mạng, hoàn toàn không tự quy kết hay suy đoán kết quả thăm dò từ xa là sai lệch.

---

## 15. Kiểm Toán Không Bịa Đặt Mã Lỗi / Nguyên Nhân Vắng Mặt Đầu Ra (No-Cause / No-NTSTATUS Audit)

- Báo cáo tuyệt đối không suy đoán hay bịa đặt:
  * Không đề cập bất kỳ mã lỗi NTSTATUS nào (như `STATUS_ACCESS_DENIED`, `STATUS_INSUFF_SERVER_RESOURCES`...).
  * Không bịa đặt quyền truy cập `IPC$` hay tài khoản guest.
  * Không đưa ra giả định về nguyên nhân kịch bản không xuất hiện kết quả (như tường lửa chặn, chống quét, rớt gói).
  * Không tuyên bố kịch bản bị "thất bại" (failed) khi công cụ hoàn tất trọn vẹn và in dòng `Nmap done`.

---

## 16. Kiểm Toán Ranh Giới Khai Thác / RCE (Exploitation/RCE Boundary Audit)

- Câu văn sinh viên đã tinh gọn chuẩn mực: *"Về ranh giới phạm vi, Kịch bản 2 dừng ở phạm vi rà quét NSE; không có bước khai thác hoặc kết quả thực thi mã từ xa được ghi nhận trong kịch bản này."*
- Rà soát tự động xác nhận số lần xuất hiện trong văn xuôi sinh viên của các thuật ngữ công cụ khai thác sau là **0**:
  * `Meterpreter`: 0.
  * `reverse shell`: 0.
- Không mô tả hành vi cấu trúc gói tin hoặc mã payload nội bộ của kịch bản NSE.

---

## 17. Kiểm Toán Xuất Xứ Dòng Lệnh Vận Hành (Command-Lineage Audit)

- Câu lệnh thực thi trên giao diện terminal Kali được thể hiện đúng nguyên văn như quan sát trên màn hình: `nmap -p 445 --script smb-vuln-ms17-010 192.168.56.20`.
- Không gán cờ nội bộ `--privileged` vào câu lệnh của người vận hành.
- Không bịa đặt các tùy chọn không có trong bằng chứng như `-Pn`, `sudo`, hoặc các tùy chọn của các phép đo khác.

---

## 18. Kiểm Toán Nhãn Phép Đo và Mã Định Danh Nội Bộ (Measurement-Label / Internal-ID Audit)

- Báo cáo chỉ sử dụng các nhãn phép đo thực nghiệm công khai được phê duyệt: `NSE-SMB-01`, `NSE-SMB-02`, `NSE-SMB-03`, `NSE-SMB-04`.
- Rà soát tự động xác nhận số lần xuất hiện trong văn xuôi sinh viên của các mã quản trị nội bộ sau là **0**:
  * `S2-RAW-*`: 0.
  * `S2-IMG-*`: 0.
  * `S2-C*`: 0.
  * `S2-META-*`: 0.
  * `ENV-CORE-*`: 0.
  * Đường dẫn kho lưu trữ (`work/do-an/...`): 0.

---

## 19. Kiểm Toán Chuyển Tiếp Sang Kịch Bản Can Thiệp Case B (Case B Transition Audit)

- Đoạn văn chuyển tiếp cuối Mục 3.3 tuân thủ nghiêm ngặt các yêu cầu:
  * Nêu rõ baseline cùng Kịch bản 1 và Kịch bản 2 đã hoàn thành việc xác lập mốc quan sát trước can thiệp.
  * Bước thực nghiệm Case B thay đổi một biến số duy nhất trong mô hình thử nghiệm: cấu hình vô hiệu hóa giao thức SMBv1 trên máy chủ Windows Server 2012 R2.
  * Các phép đo được chọn (kiểm tra phương ngữ và kiểm tra kịch bản MS17-010) được lặp lại để đối chiếu phản hồi từ xa.
- Không gọi mốc xuất phát là "Baseline Case A".
- Không tuyên bố "lặp lại toàn bộ các phép đo".
- Không tiết lộ kết quả đo đạc của Case B.
- Không đưa ra kết luận biện pháp can thiệp là hiệu quả hay làm giảm thiểu rủi ro tại thời điểm này.

---

## 20. Kiểm Toán Ranh Giới Chương 3 và Chương 4 (Chapter 3 / Chapter 4 Boundary Audit)

- Báo cáo thuần túy ghi nhận các kết quả thực nghiệm khách quan trong phòng thí nghiệm.
- Không chứa xếp hạng rủi ro (risk ratings, điểm CVSS, mức độ nghiêm trọng High/Medium/Low).
- Không phân tích bộ ba bảo mật CIA (Confidentiality, Integrity, Availability).
- Không đưa ra bất kỳ khuyến nghị khắc phục, chiến lược áp dụng bản vá hay hướng dẫn quản trị an ninh doanh nghiệp nào.

---

## 21. Kiểm Toán Giọng Văn Tác Giả Sinh Viên (Author-Voice Audit)

- Giọng văn học thuật khách quan, trung tính, phù hợp báo cáo đồ án cá nhân của sinh viên ngành An toàn thông tin.
- Không mang phong cách biên bản kiểm toán (audit memo), tài liệu quản trị (governance document), hay khuôn mẫu tạo tự động.
- Hình ảnh và bảng biểu đều có câu dẫn nhập chỉ dẫn người đọc trước khi hiển thị, và có các đoạn văn phân tích ý nghĩa đo đạc cùng giới hạn kết luận ngay sau đó.

---

## 22. Kiểm Toán Rò Rỉ Nội Dung Các Phần Sau (Later-Section Leakage Audit)

- Không viết nội dung Mục 3.4.
- Không đưa kết quả Case B hay Case C.
- Không đưa nội dung Chương 4.
- Không tạo tệp DOCX cuối cùng.

---

## 23. Bảng Kiểm Tra Các Chuỗi Bắt Buộc & Nghiêm Cấm (Required/Forbidden Terms Audit R2)

Toàn bộ các phép tìm kiếm dưới đây được thực hiện trực tiếp trên các byte văn xuôi sinh viên cuối cùng sau khi hoàn tất chỉnh sửa:

| Chuỗi kiểm tra | Loại kiểm tra | Yêu cầu | Kết quả thực tế R2 | Đánh giá |
|---|---|---|---|---|
| `3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE` | Bắt buộc | Xuất hiện | Có (H2 duy nhất) | ĐẠT |
| `3.3.1. Khảo sát điều kiện kết nối và thuộc tính giao thức SMB (NSE-SMB-01 đến NSE-SMB-03)` | Bắt buộc | Xuất hiện | Có (H3 thứ nhất) | ĐẠT |
| `3.3.2. Đánh giá dấu hiệu lỗ hổng MS17-010 và đối chiếu trạng thái bản vá (NSE-SMB-04)` | Bắt buộc | Xuất hiện | Có (H3 thứ hai) | ĐẠT |
| `Bảng 3.4. Trình tự và kết quả các phép đo NSE trên dịch vụ SMB từ trạm Kali Linux` | Bắt buộc | Xuất hiện | Có (Bảng 3.4 duy nhất) | ĐẠT |
| `Hình 3.6. Kết quả thực thi kịch bản smb-vuln-ms17-010 từ trạm Kali Linux` | Bắt buộc | Xuất hiện | Có (Hình 3.6 duy nhất) | ĐẠT |
| `445 OPEN != vulnerable` | Bắt buộc | Xuất hiện | Có | ĐẠT |
| `SMBv1 enabled != MS17-010 confirmed` | Bắt buộc | Xuất hiện | Có | ĐẠT |
| `Message signing enabled but not required` | Bắt buộc | Xuất hiện | Có | ĐẠT |
| `UNKNOWN / NO USABLE SCRIPT RESULT` | Bắt buộc | Xuất hiện | Có | ĐẠT |
| `UNKNOWN != SAFE` | Bắt buộc | Xuất hiện | Có | ĐẠT |
| `Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa.` | Bắt buộc | Xuất hiện nguyên văn | Có | ĐẠT |
| `hỗ trợ 5 phương ngữ` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `hỗ trợ đàm phán` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `Hỗ trợ đa phương ngữ` | Nghiêm cấm trong văn xuôi/bảng | 0 lần | **0** | ĐẠT |
| `tính chất mất an toàn` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `phản ánh giới hạn của phép đo từ xa` | Nghiêm cấm trong văn xuôi/bảng | 0 lần | **0** | ĐẠT |
| `được kích hoạt` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `gọi kịch bản chuyên biệt` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `trả về bình thường` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `kết thúc bình thường` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `ngưỡng cập nhật an toàn tối thiểu` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `các bản cập nhật thay thế tương ứng` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `Meterpreter` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `reverse shell` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `Baseline Case A` | Nghiêm cấm | 0 lần | **0** | ĐẠT |
| `Nmap 7.95` | Nghiêm cấm | 0 lần | **0** | ĐẠT |
| `sẵn sàng tiếp nhận` | Nghiêm cấm | 0 lần | **0** | ĐẠT |
| `điều kiện cần` / `điều kiện tiên quyết` | Nghiêm cấm | 0 lần | **0** | ĐẠT |
| `false negative` / `False Negative` | Nghiêm cấm | 0 lần | **0** | ĐẠT |
| `âm tính giả` | Nghiêm cấm | 0 lần | **0** | ĐẠT |
| `canonical` / `ground truth` / `gate` | Nghiêm cấm | 0 lần | **0** | ĐẠT |
| `kiểm toán` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `S2-RAW-*` / `S2-IMG-*` / `S2-C*` | Nghiêm cấm trong văn xuôi | 0 lần | **0** | ĐẠT |
| `-Pn` | Nghiêm cấm | 0 lần | **0** | ĐẠT |
| `STATUS_` / `IPC$` | Nghiêm cấm | 0 lần | **0** | ĐẠT |

---

## 24. Kết Quả Kiểm Tra Bộ Công Cụ Tự Động (Automated QA Results)

1. `validate_project.py`: `Project validation passed.` (Mã thoát 0).
2. `unittest discover`: 7/7 bài kiểm thử unit tests vượt qua (`OK`).
3. `lint_vi_academic.py`: `Không phát hiện mẫu văn phong cần xem xét.` (error=0, warning=0, info=0).
4. `git diff --check`: Sạch hoàn toàn, không có lỗi định dạng hay khoảng trắng thừa.
5. Ảnh bằng chứng gốc `Scenario2_NSE04_MS17010.png` giữ nguyên vẹn 100% (SHA-256 không đổi: `c970e56481a920061416949ea7543dcb96f1f2f99635dbe201131073202e14ac`).
6. Ảnh phái sinh `Hinh_3_6_MS17010_NSE.png` giữ nguyên vẹn 100% (SHA-256 không đổi: `8f7a343fe9ab100a187a5ab4fe85cac320e9350cf5d59df0c4d78e385a137bdc`).

---

## 25. Các Vấn Đề Còn Băn Khoăn (Unresolved Concerns)

- Không còn vấn đề kỹ thuật hay phương pháp luận nào tồn đọng. Toàn bộ 6 nhóm vấn đề chặn (Blocking Corrections A, B, C, D, E, F) nêu trong Báo cáo Thẩm tra Độc lập R1 đã được khắc phục triệt để và kiểm chứng tự động.

---

**KẾT LUẬN TỰ ĐÁNH GIÁ:**
Dự thảo Mục 3.3 R2 đạt trạng thái:
`X7C1_CH3_33_SCENARIO2_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
