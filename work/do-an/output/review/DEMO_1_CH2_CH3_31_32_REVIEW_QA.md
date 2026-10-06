# DEMO 1 WORD REVIEW QA REPORT (WR1)

**Tài liệu:** `work/do-an/output/review/DEMO_1_CH2_CH3_31_32_REVIEW.docx`
**Ngày thực hiện:** 2026-10-06
**Trạng thái nghiệm thu:** `WR1_DEMO1_WORD_R1_READY_FOR_EXTERNAL_REVIEW`
**Mục tiêu:** Tạo snapshot tài liệu Word review hoàn chỉnh cho Demo 1 gồm toàn bộ Chương 2 (approved) và Chương 3 (tiêu đề, Mục 3.1 approved, Mục 3.2 approved).

---

## 1. THÔNG SỐ VÀ MÃ BĂM TÀI LIỆU (INTEGRITY & SHA-256)

### 1.1. Nguồn đầu vào (Canonical Inputs)

| Thành phần | Đường dẫn | SHA-256 Checksum |
| :--- | :--- | :--- |
| **Baseline DOCX** | `work/do-an/output/CHAPTER_2_FINAL.docx` | `03adb6c44bc7c336b8c1be99f4e87c2ad93d0f11fe7d16603d5eb8dc102a7042` |
| **Markdown 3.1** | `work/do-an/CH3_31_BASELINE_DRAFT_R1.md` | `6dd9de3cc979316e975964e56dcdf412dfb0b67fdcc232a30e02b7a00aea830a` |
| **Markdown 3.2** | `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md` | `acc8ce44caf80c9f9b9c8eb53f44880ba8509112cf36d55a6447aeb7577281af` |
| **Hình 3.1** | `work/do-an/chapter3/presentation/3_1/Hinh_3_1_Network_SMB.png` | `8dca03f2121e4807e034451e460c847efef28c249d4ce2b836e3eaec2f04adb4` |
| **Hình 3.2** | `work/do-an/chapter3/presentation/3_1/Hinh_3_2_Firewall.png` | `4804161192a806be15df49abc2efbab4f6673ab4c9e85074c423ce405f003c64` |
| **Hình 3.3** | `work/do-an/chapter3/presentation/3_1/Hinh_3_3_SrvSys_Hotfix.png` | `b495b35e07011775f2005aa3f02104cf4438b6dee7cbb43f7eed13561644e9e6` |
| **Hình 3.4** | `work/do-an/chapter3/presentation/3_2/Hinh_3_4_SMB_Version.png` | `513f3356792eec5f449003a43f5fa8520a7fda94d8e10d4edbb6ef62fc064964` |
| **Hình 3.5** | `work/do-an/chapter3/presentation/3_2/Hinh_3_5_SMB_NSE.png` | `45faf0f03f57ce35707e1825f555fcbb6ad5e9fdee5daac7f849351ec2360a66` |

### 1.2. Sản phẩm đầu ra (Review Snapshot Output)

| Sản phẩm | Đường dẫn | SHA-256 Checksum | Số trang (Word / PDF) |
| :--- | :--- | :--- | :---: |
| **Review DOCX** | `work/do-an/output/review/DEMO_1_CH2_CH3_31_32_REVIEW.docx` | `0affc468d7dd7fa31219da2d60fc4a1a0874fed2ca3e0b7f2f8da96c7230311b` | **23 trang** |

---

## 2. KIỂM ĐỊNH CẤU TRÚC VÀ ĐỊNH LƯỢNG (STRUCTURAL AUDIT)

| Tiêu chí | Quy định WR1 | Thực tế đạt được | Đánh giá |
| :--- | :---: | :---: | :---: |
| **Heading 1 (Chương)** | 2 | 2 | **PASS** |
| **Heading 2 (Mục lớn)** | 9 | 9 | **PASS** |
| **Heading 3 (Tiểu mục)** | 24 | 24 | **PASS** |
| **Bảng số liệu báo cáo** | 7 (Bảng 2.1–2.4, 3.1–3.3) | 7 | **PASS** |
| **Hình minh họa** | 7 (Hình 2.1–2.2, 3.1–3.5) | 7 | **PASS** |
| **Tổng số trang** | Bố cục tự nhiên, không trang trắng | 23 trang | **PASS** |
| **Orphan Heading / Caption** | 0 | 0 | **PASS** |
| **First-page Header** | Bắt buộc (chỉ trang 1) | Có (Trang 1 duy nhất) | **PASS** |
| **Ngắt trang Chương 2 -> 3** | Sạch, không trang trắng | Sạch (Trang 12 -> 13) | **PASS** |

### 2.1. Chi tiết Heading 1 (2 mục)
1. `CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM` (Trang 1)
2. `CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH` (Trang 13)

### 2.2. Chi tiết Heading 2 (9 mục)
- **Chương 2 (7 mục):**
  1. `2.1. Phạm vi và mô hình thực nghiệm` (Trang 1)
  2. `2.2. Chuẩn bị và xác nhận trạng thái ban đầu của hệ thống` (Trang 3)
  3. `2.3. Kịch bản 1 — Khảo sát dịch vụ SMB bằng kỹ thuật thông thường` (Trang 5)
  4. `2.4. Kịch bản 2 — Nhận diện dịch vụ SMB và kiểm tra dấu hiệu liên quan đến MS17-010 bằng Nmap NSE` (Trang 6)
  5. `2.5. Kiểm thử hai biện pháp giảm thiểu đã thực hiện` (Trang 8)
  6. `2.6. Dữ liệu thực nghiệm và nguyên tắc sử dụng` (Trang 10)
  7. `2.7. Tổng kết chương` (Trang 12)
- **Chương 3 (2 mục):**
  8. `3.1. Trạng thái baseline trước đo đạc` (Trang 13)
  9. `3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB` (Trang 19)

### 2.3. Chi tiết Heading 3 (24 mục)
- **Chương 2 (20 mục):**
  1. `2.1.1. Mục tiêu và phạm vi thực nghiệm` (Trang 1)
  2. `2.1.2. Mô hình mạng ở trạng thái baseline` (Trang 1)
  3. `2.1.3. Thành phần và thông số môi trường` (Trang 2)
  4. `2.2.1. Cấu hình mạng và hai máy ảo` (Trang 3)
  5. `2.2.2. Chuẩn bị Kali Linux và công cụ Nmap/NSE` (Trang 3)
  6. `2.2.3. Chuẩn bị Windows Server, SMB và Windows Firewall` (Trang 3)
  7. `2.2.4. Xác định trạng thái bản vá MS17-010` (Trang 4)
  8. `2.2.5. Snapshot và kiểm tra trước thực nghiệm` (Trang 4)
  9. `2.3.1. Mục tiêu và dữ liệu cần quan sát` (Trang 5)
  10. `2.3.2. Quy trình quét và các lệnh thực hiện` (Trang 5)
  11. `2.3.3. Giới hạn kết luận của Kịch bản 1` (Trang 6)
  12. `2.4.1. Mục tiêu và điều kiện thực hiện` (Trang 6)
  13. `2.4.2. Bốn phép đo NSE-SMB-01 đến NSE-SMB-04` (Trang 7)
  14. `2.4.3. Đối chiếu kết quả từ xa với trạng thái bản vá nội bộ` (Trang 7)
  15. `2.5.1. Nguyên tắc đối chiếu trước và sau can thiệp` (Trang 8)
  16. `2.5.2. Vô hiệu hóa SMBv1 trên Windows Server` (Trang 8)
  17. `2.5.3. Kiểm soát SMB bằng pfSense Transparent Bridge` (Trang 9)
  18. `2.6.1. Dữ liệu được thu thập và lưu trữ` (Trang 10)
  19. `2.6.2. Phạm vi dữ liệu dùng cho đánh giá` (Trang 11)
  20. `2.6.3. Nguyên tắc diễn giải kết quả` (Trang 11)
- **Chương 3 (4 mục):**
  21. `3.1.1. Trạng thái mạng và dịch vụ SMB` (Trang 13)
  22. `3.1.2. Trạng thái bản vá và mốc phục hồi` (Trang 16)
  23. `3.2.1. Khảo sát trạm mạng và trạng thái mở cổng dịch vụ SMB` (Trang 19)
  24. `3.2.2. Nhận diện phiên bản dịch vụ và đặc tính giao thức SMB` (Trang 21)

### 2.4. Danh mục 7 Bảng số liệu
1. `Bảng 2.1. Thông số kỹ thuật của các máy ảo trong môi trường thực nghiệm` (Trang 2)
2. `Bảng 2.2. Quy trình các bước thực hiện trong Kịch bản 1` (Trang 5)
3. `Bảng 2.3. Danh mục 4 phép đo trong Kịch bản 2` (Trang 7)
4. `Bảng 2.4. Thiết kế các kịch bản thực nghiệm và kế hoạch đo đạc đối chiếu` (Trang 8)
5. `Bảng 3.1. Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc` (Trang 14)
6. `Bảng 3.2. Trạng thái bản vá và mốc phục hồi` (Trang 18)
7. `Bảng 3.3. Trình tự và kết quả khảo sát dịch vụ SMB từ trạm Kali Linux` (Trang 20–21, lặp tiêu đề cột trên Trang 21)

### 2.5. Danh mục 7 Hình minh họa
1. `Hình 2.1. Sơ đồ topo kết nối mạng ở trạng thái baseline trên VirtualBox` (Trang 2)
2. `Hình 2.2. Sơ đồ kiến trúc mạng pfSense Transparent Bridge trong kịch bản Case C` (Trang 9)
3. `Hình 3.1. Trạng thái mạng, dịch vụ SMB và các cổng lắng nghe trên Windows Server 2012 R2 trước thực nghiệm` (Trang 15)
4. `Hình 3.2. Cấu hình Windows Firewall giới hạn nguồn truy cập TCP 139/445 từ trạm Kali Linux` (Trang 16)
5. `Hình 3.3. Phiên bản srv.sys và danh mục hotfix ghi nhận trên Windows Server 2012 R2` (Trang 18)
6. `Hình 3.4. Kết quả thăm dò phiên bản dịch vụ SMB từ xa bằng công cụ Nmap` (Trang 21)
7. `Hình 3.5. Kết quả phân tích phương ngữ, tính năng và chính sách ký số SMB bằng tập kịch bản Nmap NSE` (Trang 22)

---

## 3. KIỂM TOÁN TÍNH NGUYÊN VẸN VÀ CHỐNG TRÔI NỘI DUNG (CONTENT INTEGRITY AUDIT)

### 3.1. Bảo toàn Chương 2 (Chapter 2 Preservation)
- Toàn bộ 126 đoạn văn bản, 4 bảng số liệu (Bảng 2.1–2.4), 3 hộp lệnh minh họa và 2 hình sơ đồ (Hình 2.1–2.2) của Chương 2 được giữ nguyên 100% không đổi từ `CHAPTER_2_FINAL.docx`.
- Toàn bộ trích dẫn học thuật `[1]` đến `[11]` của Chương 2 được bảo toàn tuyệt đối, không thay đổi số thứ tự hay vị trí.
- Không chỉnh sửa hay ghi đè lên file gốc `work/do-an/output/CHAPTER_2_FINAL.docx`.

### 3.2. Khớp nối nội dung Chương 3 (Chapter 3 Fidelity)
- Toàn bộ câu từ, số liệu đo đạc, tham số và phân tích kỹ thuật trong Mục 3.1 và Mục 3.2 khớp chính xác 100% với hai bản thảo markdown đã được duyệt: `CH3_31_BASELINE_DRAFT_R1.md` và `CH3_32_SCENARIO1_DRAFT_R1.md`.
- Đúng 5 hình crop đã duyệt từ thư mục `work/do-an/chapter3/presentation/` được sử dụng, không recrop, không đổi kích thước điểm ảnh gốc, không dùng ảnh màn hình thô chưa xử lý.

### 3.3. Xử lý chú thích nội bộ và trích dẫn (Citation Anchor Audit)
- Chuỗi chú thích nội bộ:
  `<!-- CITE-ANCHOR: S005, S032; final IEEE numbering deferred to global normalization gate -->`
  trong `CH3_31_BASELINE_DRAFT_R1.md` đã được lọc bỏ hoàn toàn, **không xuất hiện** trong tài liệu Word.
- Không tự phát minh hay chèn thêm bất kỳ nhãn trích dẫn `[x]` mới nào vào Chương 3.

### 3.4. Rà soát loại trừ phạm vi chưa hoàn thành (Negative Scope Audit)
- **Không chứa Mục 3.3:** Không có tiêu đề hay nội dung của Mục 3.3 (ngoại trừ câu chuyển tiếp hướng tương lai chuẩn mực ở cuối Mục 3.2.2: *"Trên cơ sở đó, Mục 3.3 tiếp tục sử dụng các phép đo NSE chuyên biệt để kiểm tra dấu hiệu liên quan đến MS17-010."*).
- **Không chứa kết quả Case B / Mục 3.4:** Không có nội dung hay bảng kết quả retest của Case B trong Chương 3.
- **Không chứa kết quả Case C:** Không có nội dung retest Case C trong Chương 3.
- **Không chứa Mục 3.5 – 3.7 và Chương 4:** Hoàn toàn không có.
- **Không có placeholder:** Không chứa `TBD`, `TODO`, `placeholder` hoặc khoảng trống chờ.
- **Không chứa thuật ngữ quản trị nội bộ:** Không chứa các nhãn quản lý như `S1-C`, `S2-C`, `Evidence ID`, `Claim ID`, `Gate`, `Ledger`.
- **Không chứa cú pháp markdown thô:** Không có cú pháp ảnh `![...]`, không có khối mã mermaid ```` ```mermaid ````.

---

## 4. QUY CHUẨN ĐỊNH DẠNG HỌC THUẬT (ACADEMIC FORMATTING COMPLIANCE)

- **Khổ giấy:** A4 Portrait tiêu chuẩn (21.0 cm x 29.7 cm).
- **Lề trang:**
  - Lề trên (Top): 3.5 cm
  - Lề dưới (Bottom): 3.0 cm
  - Lề trái (Left): 3.5 cm
  - Lề phải (Right): 2.0 cm
- **Phông chữ:** Times New Roman cho toàn bộ nội dung văn bản và bảng biểu; Consolas cho các định danh lệnh và thông số kỹ thuật nội dòng.
- **Cỡ chữ và giãn dòng:**
  - Văn bản thân (Body text): 13 pt, giãn dòng 1.5 lines, căn đều hai bên (Justified), thụt đầu dòng 1.0 cm.
  - Heading 1 (Tên chương): 16 pt Bold Hoa, căn giữa (Center), `keep_with_next = True`.
  - Heading 2: 14 pt Bold, căn trái (Left), `keep_with_next = True`.
  - Heading 3: 13 pt Bold Nghiêng, căn trái (Left), `keep_with_next = True`.
  - Tên bảng: 12 pt Bold, căn giữa, đặt phía trên bảng, `keep_with_next = True`.
  - Chú thích hình: 12 pt Bold, căn giữa, đặt phía dưới hình.
- **Định dạng bảng OpenXML chuẩn:**
  - Căn giữa trang (`<w:jc w:val="center"/>`).
  - Viền bảng thanh lịch màu xám nhẹ (`#B0B0B0`), bỏ viền dọc bên ngoài.
  - Hàng tiêu đề bảng được tô nền xanh xám trang nhã (`#E8EEF5`), in đậm 10 pt.
  - Thuộc tính lặp lại tiêu đề bảng khi ngắt trang (`<w:tblHeader/>`) được kích hoạt đầy đủ (thể hiện rõ tại Bảng 3.3 trang 20–21).
  - Khóa chống cắt đôi hàng (`<w:cantSplit/>`) trên 100% các hàng của bảng.
- **First-page Review Banner:**
  - Văn bản: `BẢN REVIEW — CHƯA PHẢI BẢN NỘP CUỐI — DEMO 1`
  - Định dạng: Times New Roman 8.5 pt, nghiêng, màu xám trung tính (`#787878`), căn giữa.
  - Cấu hình: `different_first_page_header_footer = True`, chỉ xuất hiện tại trang 1, không chiếm dụng hay làm biến dạng lề thân bài viết.

---

## 5. NHẬT KÝ KIỂM TRA THỊ GIÁC 100% TỪNG TRANG (23-PAGE VISUAL AUDIT LOG)

Mỗi trang của tài liệu sau khi chuyển đổi sang PDF qua Word COM engine đã được xuất thành hình ảnh độ phân giải cao 200 DPI và kiểm tra chi tiết:

| Trang | Nội dung chính | Phần tử cấu trúc | Kiểm tra thị giác / Bố cục | Kết quả |
| :---: | :--- | :--- | :--- | :---: |
| **01** | Bắt đầu Chương 2; Phạm vi và mô hình thực nghiệm; Mục tiêu và phạm vi | Header Review; Heading 1; Heading 2 (2.1); Heading 3 (2.1.1, 2.1.2) | Header hiển thị trang nhã, lề chuẩn, ngắt dòng tự nhiên, chữ rõ nét. | **PASS** |
| **02** | Sơ đồ topo mạng baseline; Bảng thông số kỹ thuật máy ảo | Heading 3 (2.1.3); Hình 2.1; Bảng 2.1 | Hình 2.1 và chú thích trên cùng trang; Bảng 2.1 gọn gàng, viền chuẩn. | **PASS** |
| **03** | Chuẩn bị và xác nhận trạng thái ban đầu; Cấu hình mạng; Chuẩn bị Kali & Windows | Heading 2 (2.2); Heading 3 (2.2.1, 2.2.2, 2.2.3) | Tiêu đề phân cấp rõ ràng; thụt lề 1.0 cm đồng nhất; không lỗi font. | **PASS** |
| **04** | Trạng thái Windows Firewall; Xác định trạng thái bản vá; Snapshot Before Demo | Heading 3 (2.2.4, 2.2.5) | Khối văn bản cân đối, thụt dòng đều đặn, không có dòng mồ côi. | **PASS** |
| **05** | Kịch bản 1 — Khảo sát dịch vụ SMB; Quy trình khảo sát; Bảng quy trình các bước | Heading 2 (2.3); Heading 3 (2.3.1, 2.3.2); Bảng 2.2 | Bảng 2.2 hiển thị trọn vẹn, căn giữa; tiêu đề bảng gắn liền thân bảng. | **PASS** |
| **06** | Tham số lệnh quét; Giới hạn kết luận Kịch bản 1; Kịch bản 2 — Nhận diện dịch vụ SMB | Heading 3 (2.3.3); Heading 2 (2.4); Heading 3 (2.4.1) | Các nguyên tắc giới hạn nổi bật; phân đoạn kịch bản 2 mạch lạc. | **PASS** |
| **07** | Bốn phép đo NSE; Danh mục 4 phép đo; Đối chiếu kết quả từ xa với bản vá nội bộ | Heading 3 (2.4.2, 2.4.3); Bảng 2.3 | Bảng 2.3 hiển thị hoàn chỉnh; ba nguyên tắc đối chiếu rõ ràng. | **PASS** |
| **08** | Kiểm thử giải pháp giảm thiểu; Bảng ma trận đối chiếu; Vô hiệu hóa SMBv1 | Heading 2 (2.5); Heading 3 (2.5.1, 2.5.2); Bảng 2.4 | Bảng 2.4 căn giữa chuẩn mực; hộp lệnh PowerShell sắc nét. | **PASS** |
| **09** | Xác thực cấu hình SMBv1; Kiểm soát SMB qua pfSense Bridge; Sơ đồ kiến trúc | Heading 3 (2.5.3); Hình 2.2 | Hình 2.2 và chú thích nằm trọn trên trang; không tràn lề. | **PASS** |
| **10** | Mặt phẳng dữ liệu pfSense; Dữ liệu thực nghiệm; Danh mục dữ liệu thu thập | Heading 2 (2.6); Heading 3 (2.6.1) | Liệt kê 4 nhóm dữ liệu thực nghiệm mạch lạc, thụt dòng chuẩn. | **PASS** |
| **11** | Cấu hình tường lửa; Phạm vi dữ liệu đánh giá; Nguyên tắc diễn giải kết quả | Heading 3 (2.6.2, 2.6.3) | Bố cục trang thoáng, các nguyên tắc diễn giải khoa học, chặt chẽ. | **PASS** |
| **12** | Nguyên tắc FILTERED != PATCHED; Kết thúc Chương 2; Tổng kết chương | Heading 2 (2.7) | Kết thúc Chương 2 tự nhiên tại cuối trang; ngắt trang sạch sẽ sang Chương 3. | **PASS** |
| **13** | Tiêu đề Chương 3; Trạng thái baseline; Trạng thái mạng và dịch vụ SMB | Heading 1; Heading 2 (3.1); Heading 3 (3.1.1) | Bắt đầu trang mới hoàn toàn sau page break; tiêu đề 16 pt Bold Hoa nổi bật. | **PASS** |
| **14** | Chi tiết cấu hình SMB và Firewall; Bảng trạng thái ban đầu hệ thống | Bảng 3.1 | Bảng 3.1 trọn vẹn, viền thanh thoát, đổ bóng tiêu đề `#E8EEF5` trang nhã. | **PASS** |
| **15** | Ảnh cấu hình PowerShell; Phân tích cổng lắng nghe và tường lửa | Hình 3.1 | Hình 3.1 độ nét cao, kích thước 13.2 cm căn giữa; chú thích gắn liền. | **PASS** |
| **16** | Quy tắc tùy biến ATTT Lab; Ảnh Firewall; Trạng thái bản vá và mốc phục hồi | Hình 3.2; Heading 3 (3.1.2) | Hình 3.2 và chú thích cùng trang; Heading 3.1.2 có đoạn văn dẫn ngay dưới. | **PASS** |
| **17** | Chiết xuất phiên bản nhị phân; Danh mục HotFix; Phân loại UNPATCHED | Đoạn phân tích kỹ thuật | Đoạn văn bản liên tục, phân tích đối sánh sắc nét, logic chặt chẽ. | **PASS** |
| **18** | Bảng đối chiếu bản vá và snapshot; Ảnh màn hình srv.sys và hotfix | Bảng 3.2; Hình 3.3 | Bảng 3.2 và Hình 3.3 cùng xuất hiện gọn gàng trên trang 18; bố cục tuyệt đẹp. | **PASS** |
| **19** | Phân tích Hình 3.3; Kịch bản 1 — Khảo sát dịch vụ SMB; Khảo sát trạm mạng | Heading 2 (3.2); Heading 3 (3.2.1) | Chuyển tiếp tự nhiên giữa hai mục lớn; quét ARP và phân tích trạm .100. | **PASS** |
| **20** | Quét cổng TCP SYN; Bảng trình tự và kết quả khảo sát Kịch bản 1 (Phần 1) | Bảng 3.3 (B2 – B5) | Bảng 3.3 bắt đầu trên trang 20; các ô căn giữa/trái cân đối, dễ đọc. | **PASS** |
| **21** | Bảng 3.3 (Phần 2 - B6); Nhận diện phiên bản dịch vụ; Ảnh Nmap service detection | Bảng 3.3 (lặp Header); Heading 3 (3.2.2); Hình 3.4 | Tiêu đề Bảng 3.3 lặp lại chuẩn xác; Hình 3.4 toàn cảnh 14.0 cm sắc nét. | **PASS** |
| **22** | Phân tích phiên bản OS; Bốn kịch bản NSE; Ảnh phân tích NSE SMB | Hình 3.5 | Hình 3.5 kích thước 12.8 cm hiển thị rõ; chú thích và phân tích kết quả liền mạch. | **PASS** |
| **23** | Phân tích chi tiết ba phát hiện NSE; Kết luận bề mặt tiếp xúc SMB | Kết luận Mục 3.2 | Chiếm ~60% chiều cao trang (28 dòng); kết thúc cân đối, không dòng lẻ/mồ côi. | **PASS** |

---

## 6. LỊCH SỬ TINH CHỈNH BỐ CỤC (LAYOUT CORRECTION & REFINEMENT LOG)

1. **Vấn đề ban đầu (Spillover tại Trang 24):**
   - Bản xuất thử nghiệm ban đầu đạt 24 trang, trong đó trang 24 chỉ chứa đúng 2 dòng cuối của đoạn tổng kết Mục 3.2.2 (*"MS17-010. Trên cơ sở đó, Mục 3.3 tiếp tục sử dụng các phép đo NSE chuyên biệt để kiểm tra dấu hiệu liên quan đến MS17-010."*).
2. **Biện pháp hiệu chỉnh hình học và khoảng cách:**
   - Điều chỉnh độ rộng hiển thị của 5 hình Chương 3 về tỷ lệ vàng tối ưu mà vẫn giữ trọn vẹn độ phân giải và độ đọc được:
     - `Hình 3.1` và `Hình 3.2`: Điều chỉnh độ rộng thành `13.2 cm` (vừa vặn lề 15.5 cm).
     - `Hình 3.3`: Điều chỉnh độ rộng thành `13.8 cm`.
     - `Hình 3.4`: Điều chỉnh độ rộng thành `14.0 cm` (tối ưu hóa tỷ lệ toàn cảnh 4:1).
     - `Hình 3.5`: Điều chỉnh độ rộng thành `12.8 cm` (tối ưu hóa chiều cao ~7.1 cm).
   - Tinh chỉnh khoảng cách đoạn văn bản:
     - Thân đoạn văn (`Normal`): Đặt `space_before = 0 pt`, `space_after = 3 pt` (vẫn đảm bảo giãn dòng 1.5 chuẩn).
     - Heading 2: `space_before = 10 pt`, `space_after = 4 pt`.
     - Heading 3: `space_before = 6 pt`, `space_after = 3 pt`.
     - Chú thích hình và bảng: `space_before = 2 pt`, `space_after = 6 pt`.
   - Ngắt trang chủ động trước Bảng 3.2 (`page_break_before = True`) để Bảng 3.2 và Hình 3.3 xuất hiện đồng nhất, trọn vẹn trên Trang 18 mà không bị bẻ vụn giữa trang 17 và 18.
3. **Kết quả kiểm chứng:**
   - Hai dòng lẻ tại trang 24 đã được kéo gọn gàng, tự nhiên về Trang 23.
   - Trang 23 kết thúc hoàn hảo với 28 dòng chữ ngay ngắn, đạt tỷ lệ lấp đầy trang lý tưởng (~60%), không còn hiện tượng trang đuôi hay dòng mồ côi.
   - Tổng số trang toàn tài liệu ổn định chính xác ở **23 trang**.

---

## 7. KẾT LUẬN NGHIỆM THU

Bản Word Review Snapshot `DEMO_1_CH2_CH3_31_32_REVIEW.docx` đã đáp ứng 100% các tiêu chí khắt khe của quy trình WR1:
- Đúng cấu trúc, số lượng heading, số lượng bảng, số lượng hình.
- Bảo toàn tuyệt đối Chương 2 đã nghiệm thu và khớp hoàn toàn nội dung Mục 3.1 & 3.2 đã duyệt.
- Loại bỏ hoàn toàn mã chú thích kỹ thuật nội bộ và không vi phạm bất kỳ giới hạn phạm vi phủ định nào.
- 100% các trang được kiểm định trực quan qua bản render PDF và hình ảnh độ phân giải cao.

Trạng thái chính thức: **`WR1_DEMO1_WORD_R1_READY_FOR_EXTERNAL_REVIEW`**
