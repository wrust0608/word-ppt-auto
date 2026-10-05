# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG ĐỊNH DẠNG DOCX CHƯƠNG 2 (FINAL QA REPORT)

- **Tệp nguồn canonical:** `work/do-an/CHAPTER_2.md`
- **Tệp DOCX xuất bản:** `work/do-an/output/CHAPTER_2_FINAL.docx`
- **Kích thước tệp:** 75.863 bytes
- **Mã băm SHA-256:** `28aae856b5e974688f201c8b75b08f30e47e90fa81b8a53c66014d14eb1e8989`
- **Thời gian lập báo cáo:** 2026-10-06T06:05:00+07:00
- **Tổng số trang:** 13 trang (A4 portrait, in một mặt)
- **Trạng thái kiểm định:** **PASS (100% TUÂN THỦ QUY CHẾ HUIT & SẠCH LỖI TRANG)**

---

## 1. Bảng đối chiếu quy chuẩn định dạng văn bản HUIT

| STT | Tiêu chí kỹ thuật | Quy chuẩn HUIT 2024 | Triển khai trong `CHAPTER_2_FINAL.docx` | Kết quả |
|---|---|---|---|---|
| 1 | **Khổ giấy & Hướng in** | A4 (210 mm x 297 mm), Portrait | $21.0\,\text{cm} \times 29.7\,\text{cm}$, hướng đứng dọc | **PASS** |
| 2 | **Căn lề (Margins)** | Trên: 3.5 cm, Dưới: 3.0 cm, Trái: 3.5 cm, Phải: 2.0 cm | Top: 3.5 cm, Bottom: 3.0 cm, Left: 3.5 cm, Right: 2.0 cm | **PASS** |
| 3 | **Font chữ chính** | Times New Roman | Times New Roman cho toàn bộ văn bản xuôi, tiêu đề, bảng biểu | **PASS** |
| 4 | **Cỡ chữ văn bản** | 13 pt | 13 pt (`Pt(13)`) cho thân bài (Normal text) | **PASS** |
| 5 | **Dãn dòng (Line Spacing)** | 1.5 lines | 1.5 line spacing (`line_spacing = 1.5`) | **PASS** |
| 6 | **Căn lề đoạn văn** | Căn đều hai bên (Justified) | `WD_ALIGN_PARAGRAPH.JUSTIFY` cho 100% đoạn văn thân bài | **PASS** |
| 7 | **Thụt lề đầu dòng** | First line indent 1.0 – 1.27 cm | First-line indent 1.0 cm (`Cm(1.0)`) cho các đoạn văn thông thường | **PASS** |
| 8 | **Hệ thống tiêu đề** | Tiêu đề chương (H1): 16pt IN HOA ĐẬM; H2: 14pt ĐẬM; H3: 13pt ĐẬM Nghiêng | H1: 16pt Bold Uppercase, H2: 14pt Bold, H3: 13pt Bold Italic | **PASS** |
| 9 | **Số lượng đề mục** | Đúng cấu trúc canonical 7 H2 / 20 H3 | Đúng chính xác 7 mục H2 (2.1 đến 2.7) và 20 mục H3 | **PASS** |
| 10 | **Định dạng bảng** | Nhãn & tên bảng ở TRÊN, in đậm, căn giữa/trái | Đặt phía trên bảng, in đậm: "Bảng 2.1", "Bảng 2.2", "Bảng 2.3", "Bảng 2.4" | **PASS** |
| 11 | **Ngắt trang bảng** | Tiêu đề lặp lại khi sang trang, không xé vụn dòng | Bảng 2.2 thiết lập `cantSplit` cho mọi hàng và `tblHeader` lặp lại tiêu đề trang 7 | **PASS** |
| 12 | **Định dạng hình ảnh** | Hình sắc nét, tên hình ở DƯỚI, in đậm căn giữa | Ảnh PNG độ phân giải cao (Hình 2.1 & Hình 2.2), chú thích phía dưới căn giữa | **PASS** |
| 13 | **Khối lệnh / Mã nguồn** | Font Consolas (Monospace), nền xám | Font Consolas 10pt, nền tô xám nhạt (`#F2F4F7`), viền bảo vệ | **PASS** |
| 14 | **Kiểm soát mồ côi (Orphans)** | Không tiêu đề/dòng đơn lẻ ở cuối trang | Bật `keep_with_next` trên tất cả tiêu đề và chú thích bảng/hình | **PASS** |
| 15 | **Không trang trắng rỗng** | Không có trang trắng hoặc trang chứa dưới 3 dòng | 13/13 trang đầy đặn, không có trang rỗng, trang cuối kết thúc trọn vẹn | **PASS** |

---

## 2. Nhật ký kiểm tra trực quan từng trang (100% Page Visual Inspection Log)

Tài liệu được chuyển đổi sang PDF và kết xuất thành ảnh PNG độc lập độ phân giải cao ($1654 \times 2338$ pixels) để kiểm định trực quan từng trang:

### Trang 1 (`page_01.png`):
- **Phạm vi nội dung:**
  - Tiêu đề Chương 2: `CHƯƠNG 2: THIẾT KẾ MÔ HÌNH THỰC NGHIỆM VÀ PHƯƠNG PHÁP THU THẬP BẰNG CHỨNG`.
  - Mục 2.1: `Mục tiêu và phạm vi thiết kế thực nghiệm`.
  - Mục 2.1.1: `Mục tiêu kỹ thuật trọng tâm`.
  - Mục 2.1.2: `Phạm vi và các giới hạn kiểm thử`.
- **Đánh giá hình thức:** Trình bày trang trọng, lề trên 3.5 cm chuẩn xác, cỡ chữ và dãn dòng 1.5 chuẩn, phân cấp tiêu đề rõ nét.
- **Trạng thái:** **PASS**.

### Trang 2 (`page_02.png`):
- **Phạm vi nội dung:**
  - Hình 2.1: Sơ đồ phân tầng kiểm thử giao thức SMB và phạm vi áp dụng giải pháp phòng thủ.
  - Chú thích hình: `Hình 2.1: Sơ đồ phân tầng kiểm thử giao thức SMB và phạm vi áp dụng giải pháp phòng thủ` (căn giữa, in đậm).
  - 4 đoạn giải thích các tầng L1, L2, L3 và phạm vi phòng thủ tương ứng.
- **Đánh giá hình thức:** Sơ đồ đồ họa vector kết xuất PNG sắc nét, căn lề trung tâm cân đối, chú thích gắn liền hình, không tràn lề.
- **Trạng thái:** **PASS**.

### Trang 3 (`page_03.png`):
- **Phạm vi nội dung:**
  - Mục 2.1.3: `Mô hình ánh xạ mục tiêu nghiên cứu với phương pháp thực nghiệm`.
  - Bảng 2.1: `Bảng 2.1: Ánh xạ mục tiêu nghiên cứu với phương pháp thực nghiệm và cơ sở bằng chứng` (7 hàng: RQ1 đến RQ4 và các trường mục tiêu).
  - Đoạn kết luận mục 2.1.3: "Bảng 2.1 làm rõ ranh giới phương pháp...".
  - Mục 2.2: `Kiến trúc mạng và cấu hình trạm thực nghiệm`.
  - Mục 2.2.1: `Cấu hình phân đoạn mạng Host-Only`.
- **Đánh giá hình thức:** Bảng 2.1 hiển thị trọn vẹn 100% trên trang 3, không bị cắt dở, độ rộng các cột vừa vặn lề trang.
- **Trạng thái:** **PASS**.

### Trang 4 (`page_04.png`):
- **Phạm vi nội dung:**
  - Tiếp tục mục 2.2.1 (đoạn bullet về dải mạng và cơ chế cô lập).
  - Mục 2.2.2: `Trạm phát động kiểm thử Kali Linux` (cấu hình phần cứng ảo hóa, vai trò trạm quét).
  - Mục 2.2.3: `Máy chủ mục tiêu Windows Server 2012 R2` (thông số OS, vai trò mục tiêu kiểm thử).
- **Đánh giá hình thức:** Bố cục đều đặn, không có dòng mồ côi, khoảng cách giữa các heading và đoạn văn hài hòa.
- **Trạng thái:** **PASS**.

### Trang 5 (`page_05.png`):
- **Phạm vi nội dung:**
  - Mục 2.2.4: `Trạm tường lửa pfSense trong kịch bản phòng thủ mức mạng` (cấu hình hai giao diện LAN/WAN trong chế độ cầu nối trong suốt).
  - Mục 2.2.5: `Cơ chế kiểm soát snapshot và tính lặp lại của môi trường` (quy trình chụp và hoàn nguyên snapshot `Before Demo`).
- **Đánh giá hình thức:** Trang đầy đặn, căn lề hai bên chuẩn, không bị tràn dòng.
- **Trạng thái:** **PASS**.

### Trang 6 (`page_06.png`):
- **Phạm vi nội dung:**
  - Mục 2.3: `Trạng thái kiểm toán tiền thực nghiệm và mốc chuẩn xuất phát`.
  - Mục 2.3.1: `Phương pháp kiểm toán trạng thái hệ thống`.
  - Mục 2.3.2: `Kết quả kiểm toán mốc chuẩn xuất phát trước thực nghiệm`.
  - Chú thích: `Bảng 2.2: Bảng kiểm toán mốc chuẩn xuất phát của máy chủ mục tiêu trước thực nghiệm`.
  - Bảng 2.2 phần 1: Hàng tiêu đề + Hàng B1 (`Winver`), B2 (`Network`), B3 (`Service LanmanServer`), B4 (`SMBv1 Registry`).
- **Đánh giá hình thức:** Bảng 2.2 bắt đầu trang 6 với chú thích gắn kết chặt chẽ (`keep_with_next`), các hàng B1–B4 ngắt tự nhiên ở đáy trang mà không bị xé vụn văn bản trong ô.
- **Trạng thái:** **PASS**.

### Trang 7 (`page_07.png`):
- **Phạm vi nội dung:**
  - Bảng 2.2 phần 2: Hàng tiêu đề lặp lại tự động (`tblHeader`), tiếp nối hàng B5 (`Firewall Scope`), B6 (`Hotfix KB4012212 / KB4012215`).
  - Đoạn văn trailing của mục 2.3.2: "Dữ liệu kiểm toán tại Bảng 2.2 xác lập mốc chuẩn xuất phát...".
  - Mục 2.3.3: `Ranh giới suy luận từ trạng thái mốc chuẩn xuất phát` (đoạn dẫn, 2 gạch đầu dòng phân định ranh giới, đoạn tổng kết).
- **Đánh giá hình thức:** Kỹ thuật chia bảng đạt chuẩn xuất bản: có hàng tiêu đề lặp lại, văn bản phân bố đều, không có khoảng trống thừa.
- **Trạng thái:** **PASS**.

### Trang 8 (`page_08.png`):
- **Phạm vi nội dung:**
  - Mục 2.4: `Kịch bản 1: Phương pháp rà quét cổng và dịch vụ SMB`.
  - Mục 2.4.1: `Quy trình quét và thứ tự thực thi`.
  - Mục 2.4.2: `Dòng lệnh thao tác và tham số kỹ thuật`.
  - Bảng 2.3: `Bảng 2.3: Bảng dòng lệnh thao tác và tham số kỹ thuật Kịch bản 1` (toàn bộ 4 hàng lệnh Nmap B3, B4, B5, B6 với tham số chi tiết).
  - Đoạn trailing mục 2.4.2: "Các dòng lệnh tại Bảng 2.3 được thực thi...".
- **Đánh giá hình thức:** Bảng 2.3 nằm trọn vẹn trên trang 8, font lệnh Consolas rõ ràng, không bị tràn ô.
- **Trạng thái:** **PASS**.

### Trang 9 (`page_09.png`):
- **Phạm vi nội dung:**
  - Mục 2.4.3: `Tiêu chí xác định trạng thái mở cổng và nhận diện dịch vụ`.
  - Mục 2.5: `Kịch bản 2: Phương pháp kiểm định lỗ hổng an ninh SMB`.
  - Mục 2.5.1: `Mô hình phân loại bằng chứng năm lớp`.
  - Bảng 2.4: `Bảng 2.4: Mô hình phân loại bằng chứng năm lớp áp dụng cho kiểm thử giao thức SMB` (toàn bộ 3 hàng phân loại L1/L2, L3, L4/L5).
  - Đoạn văn trailing mục 2.5.1: "Biện pháp cập nhật bản vá chính thức của nhà sản xuất...".
- **Đánh giá hình thức:** Đoạn trailing được kéo lên trang 9 trọn vẹn sau khi tinh chỉnh đệm ô (cell padding) và bỏ đoạn rỗng, kết thúc mục 2.5.1 hoàn chỉnh tại trang 9.
- **Trạng thái:** **PASS**.

### Trang 10 (`page_10.png`):
- **Phạm vi nội dung:**
  - Mục 2.5.2: `Chuỗi kịch bản kiểm tra giao thức và lỗ hổng MS17-010`.
  - Đoạn dẫn và 4 gạch đầu dòng chi tiết cho từng script NSE (kiểm tra cổng, dialect SMBv1/v2, signing, và script MS17-010).
  - 3 khối lệnh Nmap đóng hộp nổi bật (Callout) với font Consolas 10pt trên nền xám nhạt có viền bo thanh lịch.
- **Đánh giá hình thức:** Khởi đầu tự nhiên ở đầu trang 10, phân cấp mạch lạc, không có trang rỗng ở giữa.
- **Trạng thái:** **PASS**.

### Trang 11 (`page_11.png`):
- **Phạm vi nội dung:**
  - Mục 2.5.3: `Ranh giới suy luận cho kết quả kiểm định lỗ hổng`.
  - Đoạn mở đầu mục 2.5.3.
  - Hình 2.2: Cây quyết định phân loại trạng thái kiểm định lỗ hổng MS17-010.
  - Chú thích hình: `Hình 2.2: Cây quyết định phân loại trạng thái kiểm định lỗ hổng MS17-010` (in đậm căn giữa).
  - 5 đoạn phân tích các trường hợp phán quyết (Vulnerable, Not Vulnerable, Unknown, Filtered/No Output, Patch boundary).
- **Đánh giá hình thức:** Cây quyết định hiển thị rõ nét, kích thước chuẩn $15.5\,\text{cm}$, chú thích nằm sát chân hình, văn bản bao quanh đầy đủ.
- **Trạng thái:** **PASS**.

### Trang 12 (`page_12.png`):
- **Phạm vi nội dung:**
  - Mục 2.6: `Thiết kế phương pháp đánh giá giải pháp phòng thủ`.
  - Mục 2.6.1: `Phương pháp vô hiệu hóa giao thức SMBv1 (Case B)` (cơ chế chỉnh sửa registry `SMB1=0`, phương pháp kiểm chứng).
  - Mục 2.6.2: `Phương pháp thiết lập tường lửa cầu nối pfSense (Case C)` (nguyên lý Transparent Bridge, quy tắc lọc gói TCP SYN port 139/445, cấu hình tunables).
- **Đánh giá hình thức:** Bố cục cân đối, các đoạn phân tích kỹ thuật chuẩn xác, không bị dồn ép.
- **Trạng thái:** **PASS**.

### Trang 13 (`page_13.png`):
- **Phạm vi nội dung:**
  - Mục 2.6.3: `Tiêu chí đánh giá tính hiệu quả của giải pháp phòng thủ` (đoạn dẫn, 5 tiêu chí được đánh số, đoạn kết luận).
  - Mục 2.7: `Tóm tắt chương và định hướng phân tích kết quả` (gồm 3 đoạn văn xuôi hoàn chỉnh).
  - Câu kết chương: "Các tệp kết quả và nguyên tắc diễn giải trên được dùng làm cơ sở phân tích tại Chương 3." nằm gọn gàng tại nửa cuối trang 13.
- **Đánh giá hình thức:** Trang cuối chiếm hơn 85% chiều cao trang, kết thúc chương trọn vẹn, không có dòng mồ côi bị tràn sang trang 14.
- **Trạng thái:** **PASS**.

---

## 3. Kết luận nghiệm thu Part A

1. Tệp `CHAPTER_2_FINAL.docx` thỏa mãn 100% các tiêu chí của Quy chế đồ án HUIT 2024.
2. Không còn bất kỳ hiện tượng xé bảng sai quy cách, tràn lề, lỗi khoảng trắng hay dòng mồ côi.
3. Độ dài tài liệu: Đúng 13 trang A4.
4. Đã sẵn sàng nộp và lưu trữ chính thức.
