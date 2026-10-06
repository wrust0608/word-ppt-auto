# BÁO CÁO TỰ ĐÁNH GIÁ DỰ THẢO MỤC 3.2 SCENARIO 1 (CH3_32_SCENARIO1_DRAFT_SELF_REVIEW_R1)

- **Trạng thái:** `X7B1_CH3_32_SCENARIO1_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7B1 R2 — Correct Section 3.2 Scenario 1 Draft`
- **Tệp dự thảo được đánh giá:** `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md`
- **Branch:** `feature/x7b1-ch3-scenario1-draft`
- **Reviewer Base HEAD:** `91d2d0aac239d774f822c742333d519f39c9dc53`
- **Tổ tiên tích hợp:** `e56458a21f8caffe777113d1e073e083810d4af7`

---

## 1. Kiểm Toán Số Lượng Từ (Word Count Audit)

- **Tổng số từ toàn văn bản (kể cả bảng và cú pháp):** 1.941 từ.
- **Số từ văn xuôi (loại trừ các dòng bảng và cú pháp nhúng ảnh):** 1.454 từ.
- **Số đoạn văn xuôi:** 14 đoạn văn.
- **Đánh giá phạm vi độ dài:** Nằm hoàn hảo trong khung dung lượng mục tiêu (~1.000–1.500 từ văn xuôi) cho Mục 3.2, bảo đảm tính học thuật súc tích, chuẩn mực, loại bỏ các câu từ suy đoán hoặc cam đoan an ninh thừa.

---

## 2. Kiểm Toán Cấu Trúc Đề Mục (Heading Audit)

- **Số lượng tiêu đề H2:** Đúng 1 tiêu đề:
  * `## 3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB`
- **Số lượng tiêu đề H3:** Đúng 2 tiêu đề:
  * `### 3.2.1. Khảo sát trạm mạng và trạng thái mở cổng dịch vụ SMB`
  * `### 3.2.2. Nhận diện phiên bản dịch vụ và đặc tính giao thức SMB`
- **Số lượng tiêu đề H3 phát sinh ngoài kế hoạch:** 0.
- **Số lượng tiêu đề H4 hoặc tiêu đề phụ khác:** 0.
- **Đoạn văn mở đầu:** Có đúng 1 đoạn văn mở đầu ngắn gọn nằm ngay dưới đề mục `3.2`, nêu mục tiêu khảo sát bề mặt phơi bày của dịch vụ SMB từ góc nhìn ngoài của trạm Kali Linux sau khi đã xác lập baseline tại Mục 3.1.

---

## 3. Kiểm Toán Bảng Biểu (Table Audit — Count = 1)

Dự thảo tích hợp đúng 1 bảng số liệu kết quả đo đạc sinh viên độc lập, tuân thủ chặt chẽ kế hoạch trình bày đã phê duyệt:

- **Bảng 3.3:** `Bảng 3.3. Trình tự và kết quả khảo sát dịch vụ SMB từ trạm Kali Linux`
  - Cấu trúc: 4 cột (`Bước khảo sát | Phép đo | Kết quả ghi nhận | Diễn giải trực tiếp / giới hạn`).
  - Gồm 5 hàng kết quả tương ứng B2, B3, B4, B5, B6.
  - Hàng B2: Ghi nhận 4 trạm trực tuyến, trạm `.100` duy trì trạng thái chưa xác định danh tính (`UNKNOWN identity`).
  - Hàng B3: Xác nhận mục tiêu trực tuyến qua ARP đơn điểm trước khi thực hiện các phép quét cổng tiếp theo; không đưa độ trễ (latency) vào bảng kết quả.
  - Hàng B4: Ghi nhận hai cổng TCP 139 và 445 ở trạng thái `OPEN` và phản hồi `syn-ack`, TTL 128; đóng khung ranh giới kỹ thuật `445 OPEN != vulnerable`.
  - Hàng B5: Ghi nhận chuỗi nhận diện dịch vụ và khoảng dấu vết hệ điều hành `Windows Server 2008 R2–2012`, không tuyên bố xác định duy nhất phiên bản 2012 R2.
  - Hàng B6: Liệt kê 5 phương ngữ SMB (NT LM 0.12 [SMBv1], 2.0.2, 2.1, 3.0, 3.0.2), ký số gói tin kích hoạt nhưng không bắt buộc, tính năng SMB2 (DFS, Leasing, Multi-credit) và `smb-os-discovery` không có đầu ra khả dụng (`no usable output`). Không đưa ra kết luận về MS17-010.
  - Bảng không biến thành command log, không chứa Evidence ID hay Claim ID.

---

## 4. Kiểm Toán Hình Ảnh (Figure Audit — Count = 2) & Đường Dẫn Tệp

Dự thảo nhúng đúng 2 hình ảnh phái sinh phục vụ trình bày:

1. **Hình 3.4:**
   - Cú pháp nhúng: `![Hình 3.4. Kết quả thăm dò phiên bản dịch vụ SMB từ xa bằng công cụ Nmap](chapter3/presentation/3_2/Hinh_3_4_SMB_Version.png)`
   - Tệp vật lý tồn tại: `work/do-an/chapter3/presentation/3_2/Hinh_3_4_SMB_Version.png` (kích thước 1280 × 310 px).
2. **Hình 3.5:**
   - Cú pháp nhúng: `![Hình 3.5. Kết quả phân tích phương ngữ, tính năng và chính sách ký số SMB bằng tập kịch bản Nmap NSE](chapter3/presentation/3_2/Hinh_3_5_SMB_NSE.png)`
   - Tệp vật lý tồn tại: `work/do-an/chapter3/presentation/3_2/Hinh_3_5_SMB_NSE.png` (kích thước 1280 × 710 px).
- **Không tạo ảnh riêng cho B2, B3, B4** theo đúng quy định tại Kế hoạch trình bày X7B0.

---

## 5. Kiểm Toán Tệp Thuyết Minh Cắt Cúp (Crop-Manifest Audit)

- Tệp thuyết minh cắt cúp: `work/do-an/CH3_32_SCENARIO1_CROP_MANIFEST_R1.md` được giữ nguyên vẹn.
- Thông số kỹ thuật ảnh gốc và ảnh cắt cúp:
  * **Hình 3.4:**
    - Nguồn: `work/do-an/chapter3/evidence/scenario1/Scenario1_B5_SMB_Version.png` (1280 × 800 px, SHA-256: `05699e248fa66ab224adc6809fb057a282d86c29c3ce2851823e07bd874f6466`).
    - Khung cắt cúp: `x=0, y=24, width=1280, height=310`.
    - Phái sinh: `work/do-an/chapter3/presentation/3_2/Hinh_3_4_SMB_Version.png` (1280 × 310 px, SHA-256: `513f3356792eec5f449003a43f5fa8520a7fda94d8e10d4edbb6ef62fc064964`).
  * **Hình 3.5:**
    - Nguồn: `work/do-an/chapter3/evidence/scenario1/Scenario1_B6_SMB_NSE_A.png` (1280 × 800 px, SHA-256: `b5b236cbe695b530b44e0af592f010f1f49bef9f5da427b9958fd9020bd651f8`).
    - Khung cắt cúp: `x=0, y=24, width=1280, height=710`.
    - Phái sinh: `work/do-an/chapter3/presentation/3_2/Hinh_3_5_SMB_NSE.png` (1280 × 710 px, SHA-256: `45faf0f03f57ce35707e1825f555fcbb6ad5e9fdee5daac7f849351ec2360a66`).
- Cả hai ảnh phái sinh giữ nguyên vẹn câu lệnh Nmap thực thi, các dòng kết quả đo đạc trọng tâm, prompt kết thúc phiên lệnh; loại bỏ thanh công cụ máy ảo (24 px phía trên) và khoảng đen trống không mang dữ liệu (phía dưới).
- Cả hai tệp ảnh bằng chứng gốc trong `work/do-an/chapter3/evidence/scenario1/` được bảo tồn nguyên vẹn (1280 × 800 px, không can thiệp byte).

---

## 6. Ma Trận Đối Chiếu Đoạn Văn – Luận Điểm Đã Tái Lập (Corrected Paragraph-to-Claim Audit)

Ma trận đối chiếu được tái lập chính xác 100% theo đúng `CH3_32_SCENARIO1_CLAIM_EVIDENCE_MAP_R1.md` (từ `S1-C01` đến `S1-C13`), xóa bỏ hoàn toàn sự dịch chuyển mã claim trong R1:

| Claim ID | Tiểu mục | Nội dung luận điểm đã phê duyệt | Vị trí thể hiện trong văn bản R2 | Đánh giá ranh giới kỹ thuật R2 |
|---|---|---|---|---|
| `S1-C01` | 3.2.1 | Phát hiện 4 trạm mạng hoạt động trong dải mạng nội bộ qua ARP | Đoạn 1 Tiểu mục 3.2.1, Bảng 3.3 (B2) | Quét ARP toàn dải `192.168.56.0/24` phát hiện 4 thực thể (`.1`, `.10`, `.20`, `.100`). |
| `S1-C02` | 3.2.1 | Định danh của thực thể `192.168.56.100` chưa xác định (`UNKNOWN identity`) | Đoạn 1 Tiểu mục 3.2.1, Bảng 3.3 (B2) | Thực thể `.100` duy trì nghiêm ngặt `UNKNOWN identity`; không gán vai trò hay suy đoán. |
| `S1-C03` | 3.2.1 | Kiểm tra tính trực tuyến của máy chủ mục tiêu trước khi quét cổng | Đoạn 1 Tiểu mục 3.2.1, Bảng 3.3 (B3) | Thăm dò ARP đơn điểm xác nhận `.20` vẫn đang trực tuyến (`Host is up`) trước các phép đo tiếp theo. Đã bỏ cụm từ "bảo đảm tính sẵn sàng". |
| `S1-C04` | 3.2.1 | Cổng dịch vụ TCP 139 (netbios-ssn) ở trạng thái mở từ xa | Đoạn 2 Tiểu mục 3.2.1, Bảng 3.3 (B4) | Từ góc nhìn trạm Kali, cổng 139/tcp được ghi nhận ở trạng thái `OPEN` và phản hồi gói tin `syn-ack`, TTL 128. |
| `S1-C05` | 3.2.1 | Cổng dịch vụ TCP 445 (microsoft-ds) ở trạng thái mở từ xa | Đoạn 2 Tiểu mục 3.2.1, Bảng 3.3 (B4) | Từ góc nhìn trạm Kali, cổng 445/tcp được ghi nhận ở trạng thái `OPEN` và phản hồi gói tin `syn-ack`, TTL 128. |
| `S1-C06` | 3.2.1 | Ranh giới kỹ thuật: Cổng 445 mở không đồng nghĩa với tồn tại lỗ hổng | Đoạn 2 Tiểu mục 3.2.1, Bảng 3.3 (B4) | Khóa chặt ranh giới: `445 OPEN != vulnerable`. Đã loại bỏ khẳng định "dịch vụ chia sẻ tệp ... hoàn toàn có thể tiếp cận". |
| `S1-C07` | 3.2.2 | Dấu vết phiên bản dịch vụ từ xa của Nmap trên cổng 139 và 445 | Đoạn dẫn Hình 3.4, Hình 3.4, Đoạn sau Hình 3.4, Bảng 3.3 (B5) | Cổng 139 là `netbios-ssn`, cổng 445 là `Server 2008 R2 - 2012 microsoft-ds`; `Service Info: OS: Windows`. |
| `S1-C08` | 3.2.2 | Ranh giới kỹ thuật: Dấu vết phiên bản là khoảng nhận diện, không định danh chính xác 2012 R2 | Đoạn sau Hình 3.4, Bảng 3.3 (B5) | Nmap chỉ khu biệt trong khoảng dấu vết `Windows Server 2008 R2–2012`; các phản hồi từ xa chưa đủ căn cứ để định danh chính xác duy nhất phiên bản Windows Server 2012 R2 (đã bỏ "hoàn toàn không thể"). |
| `S1-C09` | 3.2.2 | Máy chủ hỗ trợ 5 phương ngữ SMB, bao gồm phương ngữ cũ SMBv1 | Đoạn dẫn Hình 3.5, Hình 3.5, Đoạn 1 sau Hình 3.5, Bảng 3.3 (B6) | Hỗ trợ 5 phương ngữ (NT LM 0.12 [SMBv1], 2.0.2, 2.1, 3.0, 3.0.2); khóa chặt `SMBv1 enabled != MS17-010 confirmed`. Đã xóa hoàn toàn câu phỏng đoán an toàn nếu có bản vá. |
| `S1-C10` | 3.2.2 | Chính sách ký số gói tin SMB từ xa là kích hoạt nhưng không bắt buộc | Đoạn 2 sau Hình 3.5, Bảng 3.3 (B6) | Ghi nhận `Message signing enabled but not required`. Nêu rõ đây là quan sát từ xa và độc lập với cấu hình cục bộ tại Mục 3.1 (đã bỏ cụm từ "phù hợp với"). |
| `S1-C11` | 3.2.2 | Các khả năng kỹ thuật SMB2 được ghi nhận trên từng phương ngữ | Đoạn 2 sau Hình 3.5, Bảng 3.3 (B6) | DFS trên 2.0.2; DFS, Leasing, Multi-credit trên 2.1, 3.0, 3.0.2. |
| `S1-C12` | 3.2.2 | Kịch bản `smb-os-discovery` không mang lại kết quả khả dụng | Đoạn 3 sau Hình 3.5, Bảng 3.3 (B6) | Ghi nhận khách quan `no usable output`; không suy diễn tường lửa chặn; không coi là bằng chứng an toàn. |
| `S1-C13` | 3.2.2 | Ranh giới tổng thể Kịch bản 1: Không đưa ra kết luận về lỗ hổng MS17-010 | Đoạn kết luận Mục 3.2, Bảng 3.3 (B6) | Kịch bản 1 chưa đưa ra phán quyết MS17-010; chuyển tiếp sang Mục 3.3 sử dụng các phép đo NSE chuyên biệt để kiểm tra dấu hiệu liên quan (không hứa "xác minh chính xác"). |

---

## 7. Kiểm Toán Tính Tinh Gọn B2/B3 (B2/B3 Redundancy Audit)

- B2 và B3 được tích hợp gọn gàng trong cùng đoạn văn đầu tiên của Tiểu mục 3.2.1.
- B3 đóng vai trò bước xác nhận mục tiêu vẫn đang trực tuyến trước khi quét cổng. Đã loại bỏ hoàn toàn cách nói "bảo đảm tính sẵn sàng".
- Không tạo ảnh riêng cho B2 hay B3.
- Không đưa thông số độ trễ (latency RTT) vào văn bản hay bảng kết quả vì không mang giá trị phân tích an toàn thông tin.

---

## 8. Kiểm Toán Danh Tính Thực Thể .56.100 (.56.100 Identity Audit)

- Thực thể `192.168.56.100` được ghi nhận trung thực là có phản hồi trong phân đoạn mạng nhưng danh tính duy trì trạng thái chưa xác định (`UNKNOWN identity`).
- Báo cáo tuyệt đối không suy đoán hay gán bất kỳ vai trò nào cho địa chỉ này.

---

## 9. Kiểm Toán Câu Từ Trạng Thái Mở Cổng B4 (B4 Remote-Port Wording Audit)

- Đã loại bỏ câu khẳng định ứng dụng tuyệt đối: *"dịch vụ chia sẻ tệp trên máy chủ mục tiêu hoàn toàn có thể tiếp cận được qua đường truyền mạng nội bộ"*.
- Câu văn R2 chuẩn mực: *"Từ góc nhìn của trạm Kali, hai cổng TCP 139 và 445 của mục tiêu được ghi nhận ở trạng thái mở (OPEN) và phản hồi gói tin SYN-ACK với giá trị thời gian sống TTL bằng 128. Về mặt kỹ thuật an toàn thông tin, trạng thái mở của cổng TCP 445 chỉ phản ánh khả năng tiếp cận ở tầng giao vận và không đồng nghĩa với việc hệ thống tồn tại lỗ hổng bảo mật (445 OPEN != vulnerable)."*

---

## 10. Kiểm Toán Ranh Giới Dấu Vết Phiên Bản B5 (B5 Fingerprint-Boundary Audit)

- Đã loại bỏ câu từ tuyệt đối: *"hoàn toàn không thể nếu chỉ dựa trên các phản hồi từ xa này"*.
- Câu văn R2 chuẩn mực: *"Các phản hồi từ xa này chưa đủ căn cứ để định danh chính xác duy nhất phiên bản Windows Server 2012 R2."*
- Khẳng định phiên bản Windows Server 2012 R2 chỉ bắt nguồn từ cấu hình mốc xuất phát cục bộ tại Mục 3.1.

---

## 11. Kiểm Toán Giao Thức, Ký Số và Tính Năng B6 (B6 Protocol/Signing/Capability Audit)

- **Xóa bỏ tuyên bố an ninh:** Đã xóa bỏ hoàn toàn câu *"Một hệ thống kích hoạt SMBv1 vẫn có thể được bảo vệ an toàn nếu đã được áp dụng đầy đủ các bản vá bảo mật tương ứng."* Khóa chặt ranh giới `SMBv1 enabled != MS17-010 confirmed`.
- **Tách biệt ký số từ xa và cục bộ:** Đã xóa bỏ cụm từ *"phù hợp với cấu hình ký số cục bộ đã ghi nhận tại Mục 3.1"*. Câu văn R2 nêu rõ: *"Đây là kết quả quan sát từ xa và được ghi nhận độc lập với các cờ cấu hình cục bộ tại Mục 3.1."*

---

## 12. Kiểm Toán Hiện Tượng smb-os-discovery (smb-os-discovery No-Output Audit)

- Dự thảo ghi nhận sự vắng mặt của khối kết quả `smb-os-discovery` như một quan sát thực tế (`no usable output`), dù câu lệnh thực thi có chỉ định rõ kịch bản này.
- Báo cáo không suy diễn nguyên nhân tường lửa chặn hay hệ thống từ chối, và không coi đây là bằng chứng an toàn hay miễn nhiễm.

---

## 13. Kiểm Toán Ranh Giới Lỗ Hổng MS17-010 & Chuyển Tiếp Sang 3.3 (Transition Audit)

- Đã loại bỏ câu hứa hẹn phán quyết: *"Để xác minh chính xác liệu bề mặt dịch vụ SMB đang mở có bị ảnh hưởng bởi lỗ hổng an ninh này hay không..."*.
- Câu văn chuyển tiếp R2 đóng khung thận trọng: *"Trên cơ sở đó, Mục 3.3 tiếp tục sử dụng các phép đo NSE chuyên biệt để kiểm tra dấu hiệu liên quan đến MS17-010."*
- Không rò rỉ kết quả đo đạc của Kịch bản 2 / Mục 3.3.

---

## 14. Kiểm Toán Ranh Giới Chương 3 và Chương 4 (Chapter 3 / Chapter 4 Boundary Audit)

- Không chứa phân loại rủi ro (risk ratings, CVSS, mức độ nghiêm trọng).
- Không bàn luận về bộ ba bảo mật CIA (Confidentiality, Integrity, Availability).
- Không phân tích khả năng khai thác thành công (exploitability) hay kịch bản tấn công RCE.
- Không đưa ra bất kỳ khuyến nghị, giải pháp khắc phục hay hướng dẫn quản trị an toàn thông tin nào.

---

## 15. Kiểm Toán Trích Dẫn Tài Liệu (Citation Audit)

- Kịch bản 1 hoàn toàn đứng trên các kết quả đo đạc thực nghiệm trực tiếp trong phòng thí nghiệm.
- Không tạo danh mục tài liệu tham khảo cục bộ giả định, không đánh số IEEE tuỳ tiện.

---

## 16. Kiểm Toán Giọng Văn Tác Giả Sinh Viên (Author-Voice Audit)

- Giọng văn học thuật tự nhiên, trung tính, phù hợp báo cáo đồ án cá nhân sinh viên.
- Toàn bộ hình ảnh đều có câu dẫn nhập chỉ dẫn người đọc quan sát trước khi chèn hình, và có đoạn văn phân tích, diễn giải ý nghĩa kỹ thuật sau hình ảnh. Không có hiện tượng screenshot dump.

---

## 17. Kết Quả Tìm Kiếm Bắt Buộc (Required-Search Audit)

Rà soát tự động toàn văn bản dự thảo Mục 3.2 R2 cho các chuỗi bắt buộc kiểm tra:

| Chuỗi tìm kiếm bắt buộc | Số lần xuất hiện yêu cầu | Kết quả thực tế R2 | Đánh giá |
|---|---|---|---|
| `bảo đảm tính sẵn sàng` | **0** | **0** | ĐẠT |
| `hoàn toàn có thể tiếp cận` | **0** | **0** | ĐẠT |
| `được bảo vệ an toàn` | **0** | **0** | ĐẠT |
| `phù hợp với cấu hình ký số cục bộ` | **0** | **0** | ĐẠT |
| `hoàn toàn không thể` | **0** | **0** | ĐẠT |
| `xác minh chính xác liệu` | **0** | **0** | ĐẠT |
| `-Pn` | **0** | **0** | ĐẠT |
| `Meterpreter` | **0** | **0** | ĐẠT |
| `reverse shell` | **0** | **0** | ĐẠT |

---

## 18. Thuyết Minh Hiệu Chỉnh Siêu Dữ Liệu SHA Nguồn Hình Ảnh (Provenance SHA Correction)

Đã thực hiện cập nhật chính xác 2 giá trị mã băm SHA-256 nguồn trong `work/do-an/CH3_32_SCENARIO1_FIGURE_SELECTION_R1.md` khớp 100% với byte thực tế trong kho lưu trữ:
- **Hình 3.4 (B5 nguồn):** Đã sửa từ `18fbe98f...` thành `05699e248fa66ab224adc6809fb057a282d86c29c3ce2851823e07bd874f6466`.
- **Hình 3.5 (B6 nguồn):** Đã sửa từ `63200a40...` thành `b5b236cbe695b530b44e0af592f010f1f49bef9f5da427b9958fd9020bd651f8`.
- Toàn bộ quyết định lựa chọn hình ảnh, số hiệu, khung cắt cúp và chú thích được giữ nguyên vẹn.

---

## 19. Kết Quả Kiểm Tra Bộ Công Cụ Tự Động (Automated QA Results)

1. `validate_project.py`: `Project validation passed.` (Mã thoát 0).
2. `unittest discover`: 7/7 bài kiểm thử unit tests vượt qua (`OK`).
3. `lint_vi_academic.py`: `Không phát hiện mẫu văn phong cần xem xét.` (error=0, warning=0, info=0).
4. `git diff --check`: Sạch hoàn toàn, không có lỗi định dạng hay khoảng trắng thừa.
5. Byte bằng chứng gốc và ảnh phái sinh giữ nguyên vẹn 100%.

---

## 20. Các Vấn Đề Còn Băn Khoăn (Unresolved Concerns)

- Không còn vấn đề tồn đọng. Toàn bộ 5 vấn đề chặn (Blocking Corrections A, B, C, D, E) nêu trong Báo cáo Thẩm tra Độc lập R1 đã được xử lý triệt để và kiểm chứng tự động.

---

**KẾT LUẬN TỰ ĐÁNH GIÁ:**
Dự thảo Mục 3.2 R2 đạt trạng thái:
`X7B1_CH3_32_SCENARIO1_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
