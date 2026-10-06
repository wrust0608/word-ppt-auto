# BÁO CÁO TỰ ĐÁNH GIÁ DỰ THẢO MỤC 3.2 SCENARIO 1 (CH3_32_SCENARIO1_DRAFT_SELF_REVIEW_R1)

- **Trạng thái:** `X7B1_CH3_32_SCENARIO1_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7B1 — Draft Chapter 3 Section 3.2 Scenario 1`
- **Tệp dự thảo được đánh giá:** `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md`
- **Branch:** `feature/x7b1-ch3-scenario1-draft`
- **Starting Base HEAD:** `77b778c992742fb40837706655165dc0fa8b6e9f`
- **Tổ tiên tích hợp:** `e56458a21f8caffe777113d1e073e083810d4af7`

---

## 1. Kiểm Toán Số Lượng Từ (Word Count Audit)

- **Tổng số từ toàn văn bản (kể cả bảng và cú pháp):** 2.062 từ.
- **Số từ văn xuôi (loại trừ các dòng bảng và cú pháp nhúng ảnh):** 1.580 từ.
- **Số đoạn văn xuôi:** 14 đoạn văn.
- **Đánh giá phạm vi độ dài:** Nằm trong khung dung lượng mục tiêu (~1.200–1.800 từ văn xuôi) cho Mục 3.2, bảo đảm tính học thuật đầy đủ, không lan man, không viết vắn tắt thiếu cơ sở.

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
  - Hàng B3: Xác nhận mục tiêu trực tuyến qua ARP đơn điểm; không đưa độ trễ (latency) vào bảng kết quả.
  - Hàng B4: Ghi nhận trạng thái mở cổng `139/tcp` và `445/tcp` (`OPEN`), phản hồi `syn-ack`, TTL 128; đóng khung ranh giới kỹ thuật `445 OPEN != vulnerable`.
  - Hàng B5: Ghi nhận chuỗi nhận diện dịch vụ và khoảng dấu vết hệ điều hành `Windows Server 2008 R2–2012`, không tuyên bố xác định duy nhất phiên bản 2012 R2.
  - Hàng B6: Liệt kê 5 phương ngữ SMB (NT LM 0.12 [SMBv1], 2.0.2, 2.1, 3.0, 3.0.2), ký số gói tin kích hoạt nhưng không bắt buộc, tính năng SMB2 (DFS, Leasing, Multi-credit) và `smb-os-discovery` không có đầu ra khả dụng (`no usable output`). Không đưa ra kết luận về MS17-010.
  - Bảng không biến thành command log (không chứa cú pháp lệnh quét dài, không lặp lại nội dung Chương 2), không chứa Evidence ID hay Claim ID.

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

- Tệp thuyết minh cắt cúp: `work/do-an/CH3_32_SCENARIO1_CROP_MANIFEST_R1.md` đã được khởi tạo đầy đủ.
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

## 6. Ma Trận Đối Chiếu Đoạn Văn – Luận Điểm (Paragraph-to-Claim Audit)

| Vị trí trong dự thảo | Luận điểm phê duyệt | Nội dung quan sát và ranh giới thể hiện | Đánh giá ranh giới |
|---|---|---|---|
| Đoạn mở đầu Mục 3.2 | Khái quát Kịch bản 1 | Tiến trình khảo sát tuần tự từ tầng mạng, giao vận đến ứng dụng từ trạm Kali Linux | Trung tính, không kết luận sớm |
| Đoạn 1 Tiểu mục 3.2.1 | `S1-C01`, `S1-C02` | Quét ARP toàn dải 192.168.56.0/24 phát hiện 4 IP (.1, .10, .20, .100) | Ghi nhận khách quan 4 thực thể |
| Đoạn 1 Tiểu mục 3.2.1 | `S1-C02` | Địa chỉ .10 là Kali, .20 là Windows Server chỉ định; .100 mang trạng thái `UNKNOWN identity` | Không gán danh tính hay suy đoán vai trò của .100 |
| Đoạn 1 Tiểu mục 3.2.1 | `S1-C03`, `S1-C04` | Quét ARP đơn điểm xác nhận máy chủ .20 trực tuyến (`Host is up`) | Chỉ xác nhận tính trực tuyến; không phân tích độ trễ; không tuyên bố SMB sẵn sàng |
| Đoạn 2 Tiểu mục 3.2.1 | `S1-C05`, `S1-C06` | Quét TCP SYN ghi nhận cả 139/tcp và 445/tcp ở trạng thái `OPEN`, phản hồi `SYN-ACK`, TTL 128 | Chứng minh dịch vụ tiếp cận được từ ngoài qua mạng nội bộ |
| Đoạn 2 Tiểu mục 3.2.1 | `S1-C07` | Trạng thái mở cổng tầng giao vận không đồng nghĩa với tồn tại lỗ hổng bảo mật | Khóa chặt ranh giới: `445 OPEN != vulnerable` |
| Bảng 3.3 & Câu dẫn | `S1-C01` đến `S1-C13` | Bảng tổng hợp trình tự 5 bước khảo sát B2–B6 | Cấu trúc bảng kết quả, không phải command log |
| Đoạn dẫn trước Hình 3.4 | Kế hoạch bố trí Hình 3.4 | Dẫn nhập mục đích thăm dò dịch vụ và phiên bản hệ điều hành từ xa qua cổng 139/445 | Dẫn nhập tự nhiên trước hình ảnh |
| Câu chú thích & Hình 3.4 | Kế hoạch bố trí Hình 3.4 | Nhúng `Hinh_3_4_SMB_Version.png` | Hiển thị rõ ràng câu lệnh và kết quả quét Nmap -sV |
| Đoạn sau Hình 3.4 | `S1-C08`, `S1-C09` | Cổng 139 là netbios-ssn, cổng 445 là Server 2008 R2 - 2012 microsoft-ds; khoảng dấu vết 2008 R2–2012 | Nêu rõ Nmap chỉ khu biệt khoảng phiên bản, không thể định danh chính xác 2012 R2 |
| Đoạn sau Hình 3.4 | `S1-C09` | Khẳng định phiên bản 2012 R2 bắt nguồn từ cấu hình mốc xuất phát cục bộ tại Mục 3.1 | Tách biệt nguồn gốc thông tin cục bộ và kết quả thăm dò từ xa |
| Đoạn dẫn trước Hình 3.5 | Kế hoạch bố trí Hình 3.5 | Dẫn nhập mục đích thực thi 4 kịch bản Nmap NSE (`smb-protocols`, `smb2-capabilities`, `smb2-security-mode`, `smb-os-discovery`) | Dẫn nhập tự nhiên trước hình ảnh |
| Câu chú thích & Hình 3.5 | Kế hoạch bố trí Hình 3.5 | Nhúng `Hinh_3_5_SMB_NSE.png` | Hiển thị rõ ràng câu lệnh Nmap NSE và 3 cây kết quả |
| Đoạn 1 sau Hình 3.5 | `S1-C10` | Hỗ trợ 5 phương ngữ (NT LM 0.12 [SMBv1], 2.0.2, 2.1, 3.0, 3.0.2); hỗ trợ SMBv1 là tương thích ngược | Khóa chặt: `SMBv1 enabled != MS17-010 confirmed` |
| Đoạn 2 sau Hình 3.5 | `S1-C11` | Tính năng SMB2: 2.0.2 hỗ trợ DFS; 2.1..3.0.2 hỗ trợ DFS, Leasing, Multi-credit; ký số kích hoạt nhưng không bắt buộc | Ghi nhận đúng thuộc tính kỹ thuật và đối chiếu chính sách ký số mốc 3.1 |
| Đoạn 3 sau Hình 3.5 | `S1-C12` | Kịch bản `smb-os-discovery` hoàn toàn không có đầu ra khả dụng (`no usable output`) | Ghi nhận hiện tượng khách quan; không suy diễn nguyên nhân tường lửa; không coi là miễn nhiễm |
| Đoạn kết luận Mục 3.2 | `S1-C13` | Tổng kết bề mặt tiếp xúc SMB; các quan sát chưa cấu thành phán quyết MS17-010; chuyển tiếp sang Mục 3.3 | Không kết luận sớm MS17-010; không rò rỉ kết quả Kịch bản 2 |

---

## 7. Kiểm Toán Tính Tinh Gọn B2/B3 (B2/B3 Redundancy Audit)

- B2 và B3 được tích hợp gọn gàng trong cùng một đoạn văn đầu tiên của Tiểu mục 3.2.1.
- B3 được trình bày đúng vai trò là bước kiểm tra tính liên tục của mục tiêu trước khi quét cổng.
- Không tạo ảnh riêng cho B2 hay B3.
- Không đưa chỉ số độ trễ (latency RTT 0.00030s) vào bảng kết quả hay văn xuôi để tránh suy diễn sai thành thước đo hiệu năng dịch vụ.
- Không tuyên bố B3 chứng minh dịch vụ SMB đang sẵn sàng hay hoạt động.

---

## 8. Kiểm Toán Danh Tính Thực Thể .56.100 (.56.100 Identity Audit)

- Thực thể `192.168.56.100` được mô tả chính xác là có phản hồi trong phân đoạn mạng nhưng danh tính duy trì trạng thái chưa xác định (`UNKNOWN identity`).
- Dự thảo tuyệt đối không đưa ra bất kỳ giả định hay suy đoán nào về vai trò, hệ điều hành hay nguồn gốc của địa chỉ này.

---

## 9. Kiểm Toán Câu Từ Trạng Thái Mở Cổng B4 (B4 Remote-Port Wording Audit)

- Cả hai cổng `139/tcp` và `445/tcp` được mô tả là ở trạng thái mở (`OPEN`), căn cứ trên phản hồi gói tin `syn-ack` với TTL 128.
- Khẳng định rõ ràng: trạng thái mở cổng chỉ phản ánh khả năng kết nối mạng ở tầng giao vận và không đồng nghĩa với việc tồn tại lỗ hổng bảo mật (`445 OPEN != vulnerable`).
- Không xuất hiện nhầm lẫn về địa chỉ MAC hay sai lệch tầng giao thức.

---

## 10. Kiểm Toán Ranh Giới Dấu Vết Phiên Bản B5 (B5 Fingerprint-Boundary Audit)

- Dự thảo ghi nhận trung thực chuỗi dịch vụ `Microsoft Windows Server 2008 R2 - 2012 microsoft-ds` và dòng `Service Info: OS: Windows`.
- Nêu rõ đây là khoảng dấu vết phiên bản (`fingerprint range` trong khoảng `Windows Server 2008 R2–2012`), công cụ Nmap từ xa hoàn toàn không thể định danh chính xác duy nhất phiên bản Windows Server 2012 R2.
- Việc xác định máy chủ chạy Windows Server 2012 R2 được chỉ rõ là dựa trên cấu hình mốc xuất phát cục bộ đã kiểm chứng độc lập tại Mục 3.1.
- Không sử dụng B5 để kết luận về sự tồn tại của lỗ hổng.

---

## 11. Kiểm Toán Giao Thức, Ký Số và Tính Năng B6 (B6 Protocol/Signing/Capability Audit)

- Giao thức SMB: Liệt kê đầy đủ 5 phương ngữ gồm `NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, `3.0.2`.
- Khóa ranh giới kỹ thuật: Việc máy chủ hỗ trợ phương ngữ cũ SMBv1 đơn thuần là đặc tính cấu hình dịch vụ tương thích ngược, không đồng nghĩa với việc đã xác nhận hệ thống dính lỗ hổng MS17-010 (`SMBv1 enabled != MS17-010 confirmed`).
- Tính năng SMB2: Ghi nhận chính xác DFS trên phương ngữ 2.0.2; DFS, Leasing và Multi-credit trên các phương ngữ 2.1, 3.0, 3.0.2.
- Ký số gói tin: Ghi nhận trạng thái `enabled but not required` (kích hoạt nhưng không bắt buộc), đối chiếu phù hợp với thiết lập mốc ban đầu tại Mục 3.1.

---

## 12. Kiểm Toán Hiện Tượng smb-os-discovery (smb-os-discovery No-Output Audit)

- Dự thảo ghi nhận sự vắng mặt của khối kết quả `smb-os-discovery` như một quan sát thực tế (`no usable output`), dù câu lệnh thực thi có chỉ định rõ kịch bản này.
- Dự thảo hoàn toàn không tự ý suy diễn nguyên nhân kỹ thuật (không quy kết do tường lửa chặn, không quy kết do hệ thống từ chối).
- Dự thảo không coi sự thiếu hụt dữ liệu đầu ra này là bằng chứng chứng minh hệ thống an toàn hay miễn nhiễm.

---

## 13. Kiểm Toán Ranh Giới Lỗ Hổng MS17-010 (MS17-010 Overclaim Audit)

- Dự thảo khẳng định nhất quán: Kịch bản 1 chỉ khảo sát bề mặt phơi bày và đặc tính giao thức thông thường, hoàn toàn chưa đưa ra phán quyết hay kết luận về lỗ hổng MS17-010.
- Đoạn kết luận Mục 3.2 chuyển tiếp mạch lạc sang Kịch bản 2 tại Mục 3.3 để thực hiện các phép đo kiểm định chuyên sâu bằng kịch bản đánh giá lỗ hổng chuyên biệt.

---

## 14. Kiểm Toán Ranh Giới Chương 3 và Chương 4 (Chapter 3 / Chapter 4 Boundary Audit)

- Không chứa phân loại rủi ro (risk ratings, CVSS, mức độ nghiêm trọng).
- Không bàn luận về bộ ba bảo mật CIA (Confidentiality, Integrity, Availability).
- Không phân tích khả năng khai thác thành công (exploitability) hay kịch bản tấn công RCE.
- Không đưa ra bất kỳ khuyến nghị, giải pháp khắc phục, vô hiệu hóa dịch vụ hay hướng dẫn quản trị an toàn thông tin nào. Toàn bộ các nội dung này thuộc phạm vi Chương 4.

---

## 15. Kiểm Toán Trích Dẫn Tài Liệu (Citation Audit)

- Kịch bản 1 phản ánh kết quả đo đạc thực nghiệm trực tiếp trong phòng thí nghiệm; dự thảo không dẫn nguồn tài liệu tham khảo ngoại lai không cần thiết.
- Không tự ý tạo danh mục tài liệu tham khảo mới, không đánh số IEEE giả định.

---

## 16. Kiểm Toán Giọng Văn Tác Giả Sinh Viên (Author-Voice Audit)

- Giọng văn học thuật tự nhiên, góc nhìn ngôi thứ ba trung tính, phù hợp báo cáo đồ án tốt nghiệp đại học ngành An toàn thông tin.
- Sử dụng các cụm từ quan sát thực nghiệm tự nhiên: "kết quả đo đạc ghi nhận", "từ góc nhìn của trạm kiểm thử Kali Linux", "kết quả quan sát được", "trong lần đo này".
- Toàn bộ hình ảnh đều có câu dẫn nhập chỉ dẫn người đọc quan sát trước khi chèn hình, và có đoạn văn phân tích, diễn giải ý nghĩa kỹ thuật sau hình ảnh. Không có hiện tượng chèn hình hàng loạt (screenshot dump).

---

## 17. Rà Soát Từ Ngữ Bị Cấm (Forbidden-Term Search Audit)

| Từ ngữ / Khái niệm kiểm tra | Biểu thức tìm kiếm | Kết quả thực tế | Đánh giá |
|---|---|---|---|
| Khái niệm quản trị nội bộ | `canonical`, `truth matrix`, `gate`, `governance`, `Single Source of Truth` | **0 lần xuất hiện** | ĐẠT |
| Mã kiểm toán / Mã bằng chứng | `Evidence ID`, `Claim ID`, `S1-C*`, `B2-`, `B3-`, `B4-`, `B5-`, `B6-` trong văn xuôi | **0 lần xuất hiện** | ĐẠT |
| Thuật ngữ kiểm toán | `kiểm toán`, `audit`, `QA memo`, `audit report` | **0 lần xuất hiện** | ĐẠT |
| Cờ lệnh vi phạm lineage | `-Pn` | **0 lần xuất hiện** | ĐẠT |
| Khái niệm tấn công sâu / Khai thác | `Meterpreter`, `Reverse TCP`, `RCE`, `reverse shell`, `khai thác thành công` | **0 lần xuất hiện** | ĐẠT |
| Nội dung phạm vi Chương 4 | `khuyến nghị`, `giải pháp`, `khắc phục`, `đánh giá rủi ro`, `CIA` | **0 lần xuất hiện** | ĐẠT |

---

## 18. Kiểm Toán Tránh Rò Rỉ Nội Dung Các Phần Sau (Later-Section Leakage Audit)

- Không rò rỉ kết quả của Kịch bản 2 / Mục 3.3 (không đề cập đến việc kịch bản lỗ hổng có báo `VULNERABLE` hay không).
- Không đề cập đến Case B (máy đã vá), Case C (bật tường lửa nâng cao).
- Không tự mở và không đề cập đến công việc của pha X7C.

---

## 19. Kết Quả Kiểm Tra Bộ Công Cụ Tự Động (Automated QA Results)

1. `lint_vi_academic.py`:
   - Kết quả: `Không phát hiện mẫu văn phong cần xem xét.` (error=0, warning=0, info=0).
   - Đã tách các câu dài phức tạp để triệt để xóa bỏ cảnh báo VI011.
2. `git diff --check`: Sạch hoàn toàn, không có lỗi định dạng hay khoảng trắng thừa.
3. Kích thước và mã băm SHA-256 của các tệp ảnh phái sinh khớp 100% với tệp thuyết minh cắt cúp.

---

## 20. Các Vấn Đề Còn Băn Khoăn (Unresolved Concerns)

- Không có vấn đề kỹ thuật nào chưa được giải quyết. Toàn bộ các yêu cầu của kế hoạch X7B0 và ràng buộc trong prompt X7B1 đã được thực thi trọn vẹn.

---

**KẾT LUẬN TỰ ĐÁNH GIÁ:**
Dự thảo Mục 3.2 R1 đạt trạng thái:
`X7B1_CH3_32_SCENARIO1_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`
