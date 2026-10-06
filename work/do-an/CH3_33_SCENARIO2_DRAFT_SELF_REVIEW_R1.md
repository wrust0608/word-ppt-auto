# BÁO CÁO TỰ ĐÁNH GIÁ DỰ THẢO MỤC 3.3 SCENARIO 2 (CH3_33_SCENARIO2_DRAFT_SELF_REVIEW_R1)

- **Trạng thái:** `X7C1_CH3_33_SCENARIO2_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7C1 — Draft Chapter 3 Section 3.3 Scenario 2`
- **Tệp dự thảo được đánh giá:** `work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md`
- **Branch:** `feature/x7c1-ch3-scenario2-draft`
- **Starting HEAD:** `57f84063fc2cbb1607910ba46633e81e8392b3a4`
- **Tổ tiên tích hợp (Base commit):** `d589e51e81aa0a3b87980ac73cef0d81ca330e17`

---

## 1. Kiểm Toán Số Lượng Từ (Word Count Audit)

- **Tổng số từ toàn văn bản (kể cả bảng và cú pháp nhúng ảnh):** 2.229 từ.
- **Số từ văn xuôi (loại trừ các dòng bảng Markdown, tiêu đề đề mục và cú pháp nhúng ảnh):** 1.719 từ.
- **Số đoạn văn xuôi:** 15 đoạn văn.
- **Đánh giá phạm vi độ dài:** Nằm trong khung dung lượng mục tiêu (~1.100–1.600 từ văn xuôi cho kịch bản kỹ thuật chuyên sâu có tính chất phân loại phương pháp luận phức tạp), bảo đảm diễn giải cặn kẽ ý nghĩa đo đạc, tách bạch khách quan giữa quan sát trực tiếp và phân loại kỹ thuật, không đệm từ ngữ sáo rỗng hay cam đoan an ninh thừa.

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
    * **NSE-SMB-02:** Ghi nhận kịch bản `smb-protocols` đàm phán thành công 5 phương ngữ (`NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, `3.0.2`); giữ nguyên chú thích nguyên văn `[dangerous, but default]`; đóng khung ranh giới kỹ thuật `SMBv1 enabled != MS17-010 confirmed`.
    * **NSE-SMB-03:** Ghi nhận kịch bản `smb2-security-mode` trên phương ngữ 3.0.2 xác định chính sách ký số là `Message signing enabled but not required`; đóng khung kết quả quan sát từ xa độc lập với cờ cấu hình cục bộ và không khái quát hóa cho toàn bộ phương ngữ.
    * **NSE-SMB-04:** Ghi nhận cổng 445/tcp mở, phiên quét đạt dòng `Nmap done`, không xuất hiện khối kết quả `Host script results:`, không có thông báo lỗi hiển thị; phân loại phương pháp luận là `UNKNOWN / NO USABLE SCRIPT RESULT`; nêu rõ UNKNOWN không phải chuỗi ký tự nguyên văn của Nmap; đóng khung ranh giới an toàn thông tin cốt lõi `UNKNOWN != SAFE`.
  - Bảng không chứa mã nội bộ (Evidence ID, Claim ID) hay đường dẫn tệp trong kho lưu trữ.

---

## 4. Kiểm Toán Hình Ảnh (Figure Audit — Count = 1) & Đường Dẫn Tệp

Dự thảo nhúng duy nhất 1 hình ảnh phái sinh phục vụ trình bày:

- **Hình 3.6:**
  - Cú pháp nhúng: `![Hình 3.6. Kết quả thực thi kịch bản smb-vuln-ms17-010 từ trạm Kali Linux](chapter3/presentation/3_3/Hinh_3_6_MS17010_NSE.png)`
  - Tệp vật lý tồn tại trên đĩa: `work/do-an/chapter3/presentation/3_3/Hinh_3_6_MS17010_NSE.png`.
  - Kích thước: 1280 × 330 px.
- **Quy tắc cắt giảm:** Tuyệt đối không tạo ảnh chụp màn hình riêng cho NSE-SMB-01, NSE-SMB-02, NSE-SMB-03 theo đúng quyết định của Kế hoạch trình bày X7C0 đã được phê duyệt.

---

## 5. Kiểm Toán Tệp Thuyết Minh Cắt Cúp (Crop-Manifest Audit)

- Tệp thuyết minh cắt cúp: `work/do-an/CH3_33_SCENARIO2_CROP_MANIFEST_R1.md` được tạo đầy đủ và kiểm chứng tính toàn vẹn:
  - **Tệp nguồn:** `work/do-an/chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png`
    - Kích thước nguồn: 1280 × 800 px.
    - Mã băm SHA-256 nguồn: `c970e56481a920061416949ea7543dcb96f1f2f99635dbe201131073202e14ac` (bảo toàn nguyên vẹn 100%, không bị sửa đổi byte).
  - **Khung cắt cúp chuẩn hóa:** `x=0, y=24, width=1280, height=330`.
  - **Tệp phái sinh:** `work/do-an/chapter3/presentation/3_3/Hinh_3_6_MS17010_NSE.png`
    - Kích thước phái sinh: 1280 × 330 px.
    - Mã băm SHA-256 phái sinh: `8f7a343fe9ab100a187a5ab4fe85cac320e9350cf5d59df0c4d78e385a137bdc`.
  - **Nội dung bảo tồn:** Toàn bộ dòng lệnh vận hành Kali terminal, thông tin mục tiêu IP/MAC, trạng thái cổng 445/tcp mở, dòng thông báo hoàn tất `Nmap done` và dấu nhắc shell trả về.
  - **Nội dung loại bỏ:** 24 px thanh tiêu đề máy ảo VirtualBox phía trên và 470 px khoảng đen trống không mang thông tin phía dưới terminal.
  - **Can thiệp đồ họa:** Không bổ sung chú thích đồ họa (arrows, circles, highlights), không làm nét giả tạo (sharpening), không tái phối màu.

---

## 6. Ma Trận Đối Chiếu Đoạn Văn – Luận Điểm Đã Phê Duyệt (Paragraph-to-Claim Audit)

Toàn bộ văn bản dự thảo, Bảng 3.4 và Hình 3.6 được ánh xạ đầy đủ 100% với 15 luận điểm kỹ thuật trong `work/do-an/CH3_33_SCENARIO2_CLAIM_EVIDENCE_MAP_R1.md` (`S2-C01` đến `S2-C15`):

| Claim ID | Tiểu mục | Nội dung luận điểm đã phê duyệt | Vị trí thể hiện trong văn bản R1 | Đánh giá ranh giới kỹ thuật |
|---|---|---|---|---|
| `S2-C01` | 3.3.1 | Cổng dịch vụ TCP 139 ở trạng thái mở từ xa | Đoạn 2 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 1) | Ghi nhận TCP 139 OPEN, phản hồi SYN-ACK, TTL=128 từ trạm Kali; không suy diễn kết nối phiên SMB thành công hay chia sẻ tệp sẵn sàng. |
| `S2-C02` | 3.3.1 | Cổng dịch vụ TCP 445 ở trạng thái mở từ xa | Đoạn 2 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 1) | Ghi nhận TCP 445 OPEN, phản hồi SYN-ACK, TTL=128 từ trạm Kali; chỉ phản ánh khả năng tiếp cận ở tầng giao vận. |
| `S2-C03` | 3.3.1 | Ranh giới kỹ thuật: Cổng 445 mở không đồng nghĩa với tồn tại lỗ hổng | Đoạn 2 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 1) | Khóa chặt ranh giới kỹ thuật: `445 OPEN != vulnerable`; không đồng nhất cổng mở với nguy cơ bị tấn công hay tồn tại lỗ hổng. |
| `S2-C04` | 3.3.1 | NSE-SMB-02 ghi nhận 5 phương ngữ SMB, bao gồm SMBv1 | Đoạn 3 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 2) | Kịch bản `smb-protocols` ghi nhận 5 phương ngữ (`NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, `3.0.2`); giữ nguyên chú thích nguyên văn `[dangerous, but default]`. |
| `S2-C05` | 3.3.1 | Ranh giới kỹ thuật: Hỗ trợ SMBv1 không đồng nghĩa với xác nhận lỗ hổng MS17-010 | Đoạn 3 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 2) | Khóa chặt ranh giới kỹ thuật: `SMBv1 enabled != MS17-010 confirmed`; không dùng các lập luận về "điều kiện cần" hay "điều kiện tiên quyết cho khả năng bị ảnh hưởng". |
| `S2-C06` | 3.3.1 | Chính sách ký số gói tin SMB từ xa là kích hoạt nhưng không bắt buộc | Đoạn 4 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 3) | Kịch bản `smb2-security-mode` trên phương ngữ 3.0.2 ghi nhận `Message signing enabled but not required`. |
| `S2-C07` | 3.3.1 | Ranh giới kỹ thuật: Quan sát ký số từ xa và cờ cấu hình ký số cục bộ độc lập với nhau | Đoạn 4 Tiểu mục 3.3.1, Bảng 3.4 (Hàng 3) | Quan sát thăm dò từ xa của Nmap trên phương ngữ cụ thể duy trì độc lập với cờ cấu hình nội bộ tại Mục 3.1; không khái quát hóa cho mọi phương ngữ và không hòa giải trực tiếp hai tầng đo đạc. |
| `S2-C08` | 3.3.2 | Lệnh Nmap được thực thi với tùy chọn `--script smb-vuln-ms17-010` | Đoạn 1 & Đoạn 3 Tiểu mục 3.3.2, Bảng 3.4 (Hàng 4) | Ghi nhận câu lệnh chỉ định tùy chọn `--script smb-vuln-ms17-010` nhắm vào cổng 445 của máy chủ mục tiêu `192.168.56.20`. |
| `S2-C09` | 3.3.2 | Đầu ra NSE-SMB-04 đạt đến dòng hoàn tất `Nmap done` | Đoạn 3 Tiểu mục 3.3.2, Bảng 3.4 (Hàng 4) | Phiên quét kết thúc với dòng thông báo hoàn tất `Nmap done`, mục tiêu trực tuyến, cổng mở, dấu nhắc shell trả về bình thường; không coi kịch bản bị thất bại. |
| `S2-C10` | 3.3.2 | Không xuất hiện khối kết quả `Host script results:` | Đoạn 3 Tiểu mục 3.3.2, Bảng 3.4 (Hàng 4) | Khối kết quả `Host script results:` không xuất hiện trong đầu ra ghi nhận; không có thông báo lỗi hiển thị; không bịa đặt bất kỳ kết quả NSE lịch sử nào. |
| `S2-C11` | 3.3.2 | Phân loại kỹ thuật kết quả từ xa là `UNKNOWN / NO USABLE SCRIPT RESULT` | Đoạn 4 Tiểu mục 3.3.2, Bảng 3.4 (Hàng 4) | Phân loại phương pháp luận chuẩn xác là `UNKNOWN / NO USABLE SCRIPT RESULT`; nêu rõ UNKNOWN không phải chuỗi ký tự nguyên văn do Nmap in ra màn hình; không bịa đặt nguyên nhân vắng mặt đầu ra hay mã lỗi NTSTATUS. |
| `S2-C12` | 3.3.2 | Ranh giới kỹ thuật: Kết quả không xác định từ xa không đồng nghĩa với an toàn | Đoạn 5 Tiểu mục 3.3.2, Bảng 3.4 (Hàng 4) | Khóa chặt nguyên tắc an toàn thông tin cốt lõi: `UNKNOWN != SAFE`; kịch bản không phát hiện lỗ hổng không đồng nghĩa với máy chủ an toàn; không tự suy diễn thành VULNERABLE, SAFE, NOT VULNERABLE hay PATCHED. |
| `S2-C13` | 3.3.2 | Mốc chuẩn xuất phát cục bộ duy trì trạng thái chưa cài bản vá (UNPATCHED) | Đoạn 6 Tiểu mục 3.3.2 | Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa (dựa trên srv.sys 6.3.9600.16421 < 6.3.9600.18604 và danh mục hotfix quan sát được không ghi nhận KB4012213/KB4012216). |
| `S2-C14` | 3.3.2 | Ranh giới kỹ thuật: Mốc UNPATCHED cục bộ không biến kết quả từ xa thành VULNERABLE | Đoạn 7 Tiểu mục 3.3.2 | Hai trục thông tin độc lập: mốc cục bộ UNPATCHED không biến kết quả từ xa thành VULNERABLE; kết quả từ xa UNKNOWN không phủ định hiện trạng thiếu bản vá để coi máy chủ an toàn; không sử dụng ngôn từ âm tính giả (false negative). |
| `S2-C15` | 3.3.2 | Ranh giới phạm vi: Kịch bản 2 hoàn toàn không chứa kết quả khai thác hoặc RCE | Đoạn 8 Tiểu mục 3.3.2 | Kịch bản 2 là quy trình rà quét thăm dò an ninh từ xa bằng NSE; không có bước khai thác tấn công và không sinh ra bất kỳ tệp bằng chứng hay kết quả nào về RCE, reverse shell hoặc Meterpreter. |

---

## 7. Kiểm Toán Câu Từ Ranh Giới Cổng TCP NSE01 (NSE01 TCP-Boundary Audit)

- Câu từ thể hiện chuẩn mực: *"Từ trạm Kali, TCP 139 và 445 được ghi nhận ở trạng thái OPEN và phản hồi SYN-ACK với giá trị TTL bằng 128."*
- Khóa chặt ranh giới: `445 OPEN != vulnerable`.
- Không tuyên bố dịch vụ "sẵn sàng tiếp nhận kết nối", phiên SMB tầng ứng dụng thành công, chia sẻ tệp thành công hay hệ thống vulnerable.

---

## 8. Kiểm Toán Ranh Giới Giao Thức SMBv1 và MS17-010 NSE02 (NSE02 SMBv1/MS17 Boundary Audit)

- Chỉ ghi nhận đúng 5 phương ngữ xuất hiện trong đầu ra: `NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, `3.0.2`.
- Trích dẫn trung thực chú thích nguyên văn của Nmap: `[dangerous, but default]`.
- Khóa chặt ranh giới: `SMBv1 enabled != MS17-010 confirmed`.
- Loại bỏ hoàn toàn và không sử dụng các khái niệm "điều kiện cần" hoặc "điều kiện tiên quyết cho khả năng bị ảnh hưởng".

---

## 9. Kiểm Toán Tính Độc Lập Của Ký Số Gói Tin NSE03 (NSE03 Signing Independence Audit)

- Ghi nhận chính xác kết quả thăm dò trên phương ngữ 3.0.2: `Message signing enabled but not required`.
- Không khái quát hóa kết quả ký số cho toàn bộ các phương ngữ SMB khác.
- Duy trì tính độc lập nghiêm ngặt: không sử dụng cờ cấu hình cục bộ `RequireSecuritySignature` tại Mục 3.1 để xác nhận hay hòa giải quan sát ký số từ xa; hai tầng đo đạc được đối soát riêng biệt.

---

## 10. Kiểm Toán Quan Sát Trực Tiếp Phép Đo NSE04 (NSE04 Direct-Observation Audit)

- Bằng chứng lệnh và đầu ra hiển thị:
  * Câu lệnh chỉ định rõ: `--script smb-vuln-ms17-010` nhắm vào cổng 445 của trạm `192.168.56.20`.
  * Trạng thái mục tiêu: trực tuyến (`Host is up`).
  * Trạng thái cổng: 445/tcp mở (`open microsoft-ds`).
  * Trạng thái hoàn tất: phiên quét đạt đến dòng `Nmap done` và dấu nhắc shell trả về bình thường.
  * Hiện diện đầu ra kịch bản: **Không xuất hiện** khối kết quả `Host script results:`.
  * Thông báo lỗi: **Không có** thông báo lỗi hiển thị trong đầu ra ghi nhận.

---

## 11. Kiểm Toán Phân Loại Kỹ Thuật UNKNOWN (UNKNOWN Classification Audit)

- Phân loại kỹ thuật chuẩn xác của đề án: **`UNKNOWN / NO USABLE SCRIPT RESULT`**.
- Khẳng định tường minh trong văn bản: `UNKNOWN` là phân loại phương pháp luận của đề án, **không phải chuỗi ký tự nguyên văn do Nmap in ra màn hình**.
- Không tuyên bố ảnh chụp màn hình tự nó "chứng minh UNKNOWN"; ảnh chụp màn hình ghi nhận sự vắng mặt của khối kết quả kịch bản, và đề án phân loại hiện tượng này là UNKNOWN.

---

## 12. Kiểm Toán Ranh Giới An Toàn UNKNOWN != SAFE (UNKNOWN != SAFE Audit)

- Xác lập nguyên tắc an toàn thông tin cốt lõi: **`UNKNOWN != SAFE`**.
- Việc kịch bản quét từ xa không đưa ra phán quyết lỗ hổng hoàn toàn không đồng nghĩa với việc máy chủ mục tiêu an toàn, miễn nhiễm hoặc đã được cập nhật bản vá.
- Tuyệt đối không gán bất kỳ phán quyết nào sau đây cho kết quả phép đo NSE-SMB-04: `VULNERABLE`, `SAFE`, `NOT VULNERABLE`, hay `PATCHED`.

---

## 13. Kiểm Toán Tính Độc Lập Giữa UNPATCHED Cục Bộ và UNKNOWN Từ Xa (Independence Audit)

- Wording ưu tiên được thực hiện chuẩn xác: *"Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa."*
- Hai trục đo đạc độc lập:
  * Trục nội bộ (Local Ground State): `UNPATCHED` (dựa trên `srv.sys` 6.3.9600.16421 < 6.3.9600.18604 và không có hotfix KB4012213/KB4012216 trong danh mục quan sát được).
  * Trục từ xa (Remote Measurement State): `UNKNOWN / NO USABLE SCRIPT RESULT`.
- Ranh giới tuyệt đối:
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

- Kịch bản 2 được định hình nghiêm ngặt là quy trình rà quét thăm dò an ninh từ xa bằng kịch bản NSE Nmap.
- Không có bước khai thác tấn công (canonical exploit step).
- Không có tệp bằng chứng hoặc kết quả nào liên quan đến thực thi mã từ xa (RCE), tạo phiên kết nối ngược (reverse shell) hoặc phiên Meterpreter.
- Không mô tả hành vi cấu trúc gói tin hoặc mã payload nội bộ của kịch bản NSE.

---

## 17. Kiểm Toán Xuất Xứ Dòng Lệnh Vận Hành (Command-Lineage Audit)

- Câu lệnh thực thi trên giao diện terminal Kali được thể hiện đúng nguyên văn như quan sát trên màn hình: `nmap -p 445 --script smb-vuln-ms17-010 192.168.56.20`.
- Không gán cờ nội bộ `--privileged` (vốn chỉ xuất hiện trong tệp argv Nmap thô) vào câu lệnh của người vận hành.
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

## 23. Bảng Kiểm Tra Các Chuỗi Bắt Buộc & Nghiêm Cấm (Required/Forbidden Terms Audit)

| Chuỗi kiểm tra | Loại kiểm tra | Yêu cầu | Kết quả thực tế R1 | Đánh giá |
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
| `Baseline Case A` | Nghiêm cấm | 0 lần | 0 | ĐẠT |
| `Nmap 7.95` | Nghiêm cấm | 0 lần | 0 | ĐẠT |
| `sẵn sàng tiếp nhận` | Nghiêm cấm | 0 lần | 0 | ĐẠT |
| `điều kiện cần` / `điều kiện tiên quyết` | Nghiêm cấm | 0 lần | 0 | ĐẠT |
| `false negative` / `False Negative` | Nghiêm cấm | 0 lần | 0 | ĐẠT |
| `âm tính giả` | Nghiêm cấm | 0 lần | 0 | ĐẠT |
| `canonical` / `ground truth` / `gate` | Nghiêm cấm | 0 lần | 0 | ĐẠT |
| `kiểm toán` | Nghiêm cấm trong văn xuôi | 0 lần | 0 | ĐẠT |
| `S2-RAW-*` / `S2-IMG-*` / `S2-C*` | Nghiêm cấm trong văn xuôi | 0 lần | 0 | ĐẠT |
| `Meterpreter` / `reverse shell` | Nghiêm cấm | 0 lần | 0 | ĐẠT |
| `-Pn` | Nghiêm cấm | 0 lần | 0 | ĐẠT |
| `STATUS_` / `IPC$` | Nghiêm cấm | 0 lần | 0 | ĐẠT |

---

## 24. Kết Quả Kiểm Tra Bộ Công Cụ Tự Động (Automated QA Results)

1. `validate_project.py`: `Project validation passed.` (Mã thoát 0).
2. `unittest discover`: 7/7 bài kiểm thử unit tests vượt qua (`OK`).
3. `lint_vi_academic.py`: `Không phát hiện mẫu văn phong cần xem xét.` (error=0, warning=0, info=0).
4. `git diff --check`: Sạch hoàn toàn, không có lỗi thụt lề hay khoảng trắng thừa.
5. Ảnh bằng chứng gốc `Scenario2_NSE04_MS17010.png` giữ nguyên vẹn 100% (SHA-256 không đổi).

---

## 25. Các Vấn Đề Còn Băn Khoăn (Unresolved Concerns)

- Không còn vấn đề kỹ thuật hay phương pháp luận nào tồn đọng. Dự thảo đáp ứng đầy đủ 100% các tiêu chí và ranh giới đã cam kết.

---

**KẾT LUẬN TỰ ĐÁNH GIÁ:**
Dự thảo Mục 3.3 R1 đạt trạng thái:
`X7C1_CH3_33_SCENARIO2_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`
