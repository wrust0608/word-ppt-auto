# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG ĐỊNH DẠNG DOCX CHƯƠNG 2 + CHƯƠNG 3 (X7I QA REPORT)

- **Tệp DOCX đánh giá:** `work/do-an/output/CHAPTER_2_3_REVIEW.docx`
- **Kích thước tệp:** 761.142 bytes
- **Mã băm SHA-256 DOCX:** `d612273f5a3ca7ac33b306469bfc59b3a4ed1caafe7690c59ee68590c5d986e1`
- **Thời gian lập báo cáo:** 2026-10-07T14:10:00+07:00
- **Tổng số trang:** 44 trang (A4 portrait, in một mặt)
- **Phương pháp kết xuất (Render method):** Microsoft Word 16 COM Automation (`ExportAsFixedFormat(wdExportFormatPDF=17)`) trên Windows 11 với máy in mặc định `Microsoft Print to PDF`, kết hợp PyMuPDF render ảnh PNG 150 DPI từng trang độc lập.
- **Tệp nguồn canonical:**
  - Chương 2: `work/do-an/CHAPTER_2.md` (Git blob: `55ffb13acb3398c7ab29d6d5abbb369e5d26f3d0`)
  - Chương 3: `work/do-an/CHAPTER_3_DRAFT_R2.md` (Git blob: `40d2a895bc970f88d7260b3138b8a701f5eb0a8c`)
- **Tệp mẫu đối chứng Chương 2 (Reference DOCX):** `work/do-an/output/CHAPTER_2_FINAL.docx` (SHA-256: `03adb6c44bc7c336b8c1be99f4e87c2ad93d0f11fe7d16603d5eb8dc102a7042`)
- **Cấu trúc đề mục:** Đúng 2 tiêu đề H1, đúng 14 tiêu đề H2 (7 Chương 2 + 7 Chương 3), đúng 30 tiêu đề H3 (20 Chương 2 + 10 Chương 3).
- **Hệ thống bảng biểu và hình ảnh:** Đúng 11 bảng (Bảng 2.1–2.4, Bảng 3.1–3.7) và đúng 13 hình (Hình 2.1–2.2, Hình 3.1–3.11).
- **Trạng thái kiểm định:** **PASS (100% TUÂN THỦ QUY CHUẨN HUIT, ZERO REGRESSION CHƯƠNG 2, SẠCH LỖI TRANG)**

---

## 1. Bảng đối chiếu quy chuẩn định dạng văn bản HUIT

| STT | Tiêu chí kỹ thuật | Quy chuẩn HUIT 2024 / Đề tài | Triển khai trong `CHAPTER_2_3_REVIEW.docx` | Kết quả |
|---|---|---|---|---|
| 1 | **Khổ giấy & Hướng in** | A4 (210 mm x 297 mm), Portrait | $21.0\,\text{cm} \times 29.7\,\text{cm}$, hướng đứng dọc chuẩn | **PASS** |
| 2 | **Căn lề (Margins)** | Trên: 3.5 cm, Dưới: 3.0 cm, Trái: 3.5 cm, Phải: 2.0 cm | Top: 3.5 cm, Bottom: 3.0 cm, Left: 3.5 cm, Right: 2.0 cm | **PASS** |
| 3 | **Font chữ chính** | Times New Roman | Times New Roman cho toàn bộ văn bản xuôi, tiêu đề, bảng biểu | **PASS** |
| 4 | **Cỡ chữ văn bản** | 13 pt | 13 pt (`Pt(13)`) cho thân bài (Normal text) | **PASS** |
| 5 | **Dãn dòng (Line Spacing)** | 1.5 lines | 1.5 line spacing (`line_spacing = 1.5`) cho đoạn văn xuôi | **PASS** |
| 6 | **Căn lề đoạn văn** | Căn đều hai bên (Justified) | Căn đều hai bên (`WD_ALIGN_PARAGRAPH.JUSTIFY`) cho toàn bộ thân bài | **PASS** |
| 7 | **Thụt lề đầu dòng** | First line indent 1.0 – 1.27 cm | First-line indent 1.0 cm (`Cm(1.0)` / 28.35 pt) cho các đoạn văn thông thường | **PASS** |
| 8 | **Hệ thống tiêu đề** | H1: 16pt IN HOA ĐẬM căn giữa; H2: 14pt ĐẬM; H3: 13pt ĐẬM Nghiêng | H1: 16pt Bold Uppercase, H2: 14pt Bold, H3: 13pt Bold Italic | **PASS** |
| 9 | **Số lượng đề mục** | Đúng canonical: 2 H1 / 14 H2 / 30 H3 | Đúng chính xác 2 H1, 14 H2 (7 Ch2 + 7 Ch3), 30 H3 (20 Ch2 + 10 Ch3) | **PASS** |
| 10 | **Định dạng bảng** | Nhãn & tên bảng ở TRÊN, in đậm, căn giữa | Đặt phía trên bảng, in đậm: Bảng 2.1–2.4, Bảng 3.1–3.7 (12pt, căn giữa) | **PASS** |
| 11 | **Ngắt trang bảng** | `tblHeader` lặp lại tiêu đề, `cantSplit` bảo vệ dòng | Áp dụng `tblHeader` trên hàng tiêu đề và `cantSplit` trên 100% các hàng | **PASS** |
| 12 | **Định dạng hình ảnh** | Hình sắc nét, tên hình ở DƯỚI, in đậm căn giữa | Ảnh chụp thực nghiệm sắc nét (13 hình), chú thích 12pt in đậm đặt dưới hình | **PASS** |
| 13 | **Khối lệnh / Mã nguồn** | Font Consolas (Monospace) | Font Consolas 11.5pt đậm trong văn xuôi, 8.0pt đậm trong ô bảng | **PASS** |
| 14 | **Kiểm soát mồ côi (Orphans)** | Không tiêu đề/dòng đơn lẻ ở cuối trang | Thiết lập `keep_with_next` trên tất cả tiêu đề, tên bảng, ảnh và chú thích | **PASS** |
| 15 | **Không trang trắng rỗng** | Không có trang trắng hoặc trang chứa dưới 3 dòng | 44/44 trang đầy đặn, không có trang rỗng, kết thúc trọn vẹn | **PASS** |
| 16 | **Ngắt trang giữa hai chương** | Chương 3 phải bắt đầu ở trang mới | Page break sạch tại trang 12; Chương 3 mở đầu trọn vẹn tại đầu trang 13 | **PASS** |

---

## 2. Kiểm toán chuỗi đề mục (Heading Sequence Audit)

Chuỗi đề mục trong `CHAPTER_2_3_REVIEW.docx` khớp 100% tuyệt đối theo thứ tự canonical:

### Chương 2 (Trang 1 – 12)
1. `CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM` (H1) — Trang 1
2. `2.1. Phạm vi và mô hình thực nghiệm` (H2) — Trang 1
   - `2.1.1. Mục tiêu và phạm vi thực nghiệm` (H3) — Trang 1
   - `2.1.2. Mô hình mạng ở trạng thái baseline` (H3) — Trang 1
   - `2.1.3. Thành phần và thông số môi trường` (H3) — Trang 2
3. `2.2. Chuẩn bị và xác nhận trạng thái ban đầu` (H2) — Trang 3
   - `2.2.1. Cấu hình mạng và hai máy ảo` (H3) — Trang 3
   - `2.2.2. Chuẩn bị Kali Linux và công cụ Nmap/NSE` (H3) — Trang 3
   - `2.2.3. Chuẩn bị Windows Server, SMB và Windows Firewall` (H3) — Trang 3
   - `2.2.4. Xác định trạng thái bản vá MS17-010` (H3) — Trang 4
   - `2.2.5. Snapshot và kiểm tra trước thực nghiệm` (H3) — Trang 4
4. `2.3. Kịch bản 1 — Khảo sát dịch vụ SMB bằng Nmap` (H2) — Trang 5
   - `2.3.1. Mục tiêu và dữ liệu cần quan sát` (H3) — Trang 5
   - `2.3.2. Quy trình quét và các lệnh thực hiện` (H3) — Trang 5
   - `2.3.3. Giới hạn kết luận của Kịch bản 1` (H3) — Trang 6
5. `2.4. Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE` (H2) — Trang 6
   - `2.4.1. Mục tiêu và điều kiện thực hiện` (H3) — Trang 6
   - `2.4.2. Bốn phép đo NSE-SMB-01 đến NSE-SMB-04` (H3) — Trang 7
   - `2.4.3. Đối chiếu kết quả từ xa với trạng thái bản vá nội bộ` (H3) — Trang 7
6. `2.5. Kiểm thử hai biện pháp giảm thiểu đã thực hiện` (H2) — Trang 8
   - `2.5.1. Nguyên tắc đối chiếu trước và sau can thiệp` (H3) — Trang 8
   - `2.5.2. Vô hiệu hóa SMBv1 trên Windows Server` (H3) — Trang 8
   - `2.5.3. Kiểm soát SMB bằng pfSense Transparent Bridge` (H3) — Trang 9
7. `2.6. Dữ liệu thực nghiệm và nguyên tắc sử dụng` (H2) — Trang 10
   - `2.6.1. Dữ liệu được thu thập và lưu trữ` (H3) — Trang 10
   - `2.6.2. Phạm vi dữ liệu dùng cho đánh giá` (H3) — Trang 11
   - `2.6.3. Nguyên tắc diễn giải kết quả` (H3) — Trang 11
8. `2.7. Tổng kết chương` (H2) — Trang 12

### Chương 3 (Trang 13 – 44)
9. `CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH` (H1) — Trang 13
10. `3.1. Trạng thái baseline trước đo đạc` (H2) — Trang 13
    - `3.1.1. Trạng thái mạng và dịch vụ SMB` (H3) — Trang 13
    - `3.1.2. Trạng thái bản vá và mốc phục hồi` (H3) — Trang 17
11. `3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB` (H2) — Trang 19
    - `3.2.1. Khảo sát trạm mạng và trạng thái mở cổng dịch vụ SMB` (H3) — Trang 20
    - `3.2.2. Nhận diện phiên bản dịch vụ và đặc tính giao thức SMB` (H3) — Trang 21
12. `3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010` (H2) — Trang 24
    - `3.3.1. Khảo sát điều kiện kết nối và thuộc tính giao thức SMB (NSE-SMB-01 đến NSE-SMB-03)` (H3) — Trang 25
    - `3.3.2. Đánh giá dấu hiệu lỗ hổng MS17-010 và đối chiếu trạng thái bản vá (NSE-SMB-04)` (H3) — Trang 27
13. `3.4. Kết quả Case B — Vô hiệu hóa SMBv1` (H2) — Trang 29
    - `3.4.1. Thao tác vô hiệu hóa SMBv1 và kiểm tra trạng thái máy chủ cục bộ` (H3) — Trang 29
    - `3.4.2. Kết quả đo đạc lại từ xa và đối chiếu đa tầng` (H3) — Trang 32
14. `3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense` (H2) — Trang 34
    - `3.5.1. Thiết lập cầu nối pfSense và chính sách kiểm soát lưu lượng SMB` (H3) — Trang 35
    - `3.5.2. Kết quả đo đạc từ xa, đối chiếu nhật ký tường lửa và trạng thái máy chủ` (H3) — Trang 38
15. `3.6. So sánh kết quả thực nghiệm` (H2) — Trang 41
16. `3.7. Tổng kết chương` (H2) — Trang 43

**Tổng kết đề mục:** Đúng 2 H1, đúng 14 H2, đúng 30 H3. Không thừa, không thiếu, không đảo lộn.

---

## 3. Đối chiếu bảo toàn Chương 2 (Chapter 2 Regression Guard Audit)

Đối chiếu từng trang từ Trang 1 đến Trang 12 của `CHAPTER_2_3_REVIEW.docx` với tệp chuẩn `CHAPTER_2_FINAL.docx`:

| Trang | Nội dung thực tế trong `CHAPTER_2_3_REVIEW.docx` | Khớp `CHAPTER_2_FINAL.docx` | Kết luận |
|---|---|---|---|
| Trang 1 | Tiêu đề H1 Chương 2, 2.1, 2.1.1 (4 mục tiêu), 2.1.2 mở đầu | 100% chính xác từng ký tự và ngắt dòng | **PASS** |
| Trang 2 | Hình 2.1 + Chú thích, thuyết minh Hình 2.1, 2.1.3 + Bảng 2.1, thuyết minh | 100% chính xác, Bảng 2.1 trọn vẹn trang 2 | **PASS** |
| Trang 3 | 2.2, 2.2.1 (3 bullet), 2.2.2 (2 bullet), 2.2.3 (3 bullet) | 100% chính xác, ngắt dòng khớp tuyệt đối | **PASS** |
| Trang 4 | Bullet 4 của 2.2.3, 2.2.4 (4 bullet hotfix/driver), 2.2.5 (2 bullet) | 100% chính xác, thông số driver/KB chuẩn | **PASS** |
| Trang 5 | 2.3, 2.3.1 (3 bullet), 2.3.2 + Bảng 2.2 (6 bước B1–B6) | 100% chính xác, Bảng 2.2 trọn vẹn trang 5 | **PASS** |
| Trang 6 | Thuyết minh Bảng 2.2, 2.3.3 (2 nguyên tắc), 2.4, 2.4.1 (2 bullet) | 100% chính xác, ngắt trang liền mạch | **PASS** |
| Trang 7 | 2.4.2 + Bảng 2.3 (4 phép đo NSE), 2.4.3 (bullet 1, 2, nửa đầu bullet 3) | 100% chính xác, Bảng 2.3 trọn vẹn trang 7 | **PASS** |
| Trang 8 | Nửa sau bullet 3 của 2.4.3, 2.5, 2.5.1 + Bảng 2.4, 2.5.2 mở đầu | 100% chính xác, Bảng 2.4 trọn vẹn trang 8 | **PASS** |
| Trang 9 | Khối lệnh 1, 2, 3 của 2.5.2, ranh giới an ninh, 2.5.3 + Hình 2.2 | 100% chính xác, Hình 2.2 trọn vẹn trang 9 | **PASS** |
| Trang 10 | 5 bullet kỹ thuật của 2.5.3, 2.6, 2.6.1 (mục 1, 2) | 100% chính xác, thông số pfSense chuẩn | **PASS** |
| Trang 11 | Mục 3, 4 của 2.6.1, 2.6.2, 2.6.3 (nguyên tắc 1, 2, 3) | 100% chính xác, các ranh giới an ninh chuẩn | **PASS** |
| Trang 12 | Nguyên tắc 4, 5 của 2.6.3, lưu ý thời gian, 2.7 (3 đoạn tổng kết) | 100% chính xác, kết thúc trọn vẹn trang 12 | **PASS** |

**Kết luận bảo toàn Chương 2:** Toàn bộ 12 trang đầu của tài liệu kết hợp hoàn toàn đồng nhất với tài liệu mẫu đã được phê duyệt. Việc bổ sung Chương 3 không gây ra bất kỳ xáo trộn, thụt lề hay trôi trang nào đối với Chương 2.

---

## 4. Nhật ký kiểm định trực quan chi tiết 44 trang (100% Page Visual Inspection Log)

Toàn bộ 44 trang được kết xuất thành ảnh PNG độ phân giải cao tại `scratch/review_pages/page_01.png` đến `page_44.png` và được kiểm định trực quan chi tiết:

### Trang 1 – 12: Chương 2
- **Trang 1 – 12:** Toàn bộ bố cục, hình ảnh (Hình 2.1, 2.2), bảng biểu (Bảng 2.1–2.4), khối lệnh PowerShell/Nmap đều nguyên vẹn, sắc nét, không dòng mồ côi, không tràn lề. Trạng thái: **PASS**.

### Trang 13 – 44: Chương 3
- **Trang 13 (`page_13.png`):** Mở đầu Chương 3 sau ngắt trang sạch. Tiêu đề H1 `CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH` (16pt in hoa đậm căn giữa), tiếp theo là Mục 3.1 và Mục 3.1.1. Căn lề đều hai bên, thụt lề 1.0 cm. Trạng thái: **PASS**.
- **Trang 14 (`page_14.png`):** Nối tiếp văn bản Mục 3.1.1, câu dẫn Bảng 3.1, và toàn bộ `Bảng 3.1` (11 hàng dữ liệu) nằm trọn vẹn trên trang 14, không xé dòng. Nền tiêu đề bảng xanh nhạt `#E8EEF5`. Trạng thái: **PASS**.
- **Trang 15 (`page_15.png`):** Câu dẫn Hình 3.1, `Hình 3.1` (ảnh chụp PowerShell baseline sắc nét), chú thích `Hình 3.1` (12pt đậm căn giữa), đoạn văn thuyết minh căn đều. Trạng thái: **PASS**.
- **Trang 16 (`page_16.png`):** Nối tiếp câu văn về tường lửa, câu dẫn Hình 3.2, `Hình 3.2` (ảnh chụp cấu hình Windows Firewall), chú thích `Hình 3.2` (12pt đậm căn giữa) và đoạn phân tích baseline. Trạng thái: **PASS**.
- **Trang 17 (`page_17.png`):** Mục `3.1.2. Trạng thái bản vá và mốc phục hồi` (13pt đậm nghiêng), các đoạn văn phân tích chi tiết phiên bản driver `srv.sys` (6.3.9600.16421 so với ngưỡng 6.3.9600.18604), sáu mã hotfix Get-HotFix, phân loại UNPATCHED, mốc phục hồi Before Demo và câu dẫn Bảng 3.2. Trạng thái: **PASS**.
- **Trang 18 (`page_18.png`):** Toàn bộ `Bảng 3.2` (7 hàng dữ liệu) nằm trọn vẹn trên trang 18 với đường viền chuẩn và nền tiêu đề nhã nhặn, theo sau là câu dẫn Hình 3.3. Trạng thái: **PASS**.
- **Trang 19 (`page_19.png`):** `Hình 3.3` (ảnh chụp srv.sys và hotfix), chú thích `Hình 3.3` (12pt đậm), đoạn thuyết minh hình ảnh, chuyển tiếp sang Mục `3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB` (14pt đậm) và đoạn mở đầu kịch bản. Trạng thái: **PASS**.
- **Trang 20 (`page_20.png`):** Mục `3.2.1. Khảo sát trạm mạng và trạng thái mở cổng dịch vụ SMB` (13pt đậm nghiêng), phân tích phát hiện trạm mạng (4 IP gồm .1, .10, .20, .100), ranh giới danh tính chưa xác định của .100, kết quả quét cổng SYN (139/445 OPEN) kèm ranh giới an ninh 445 OPEN != vulnerable, câu dẫn và bắt đầu `Bảng 3.3`. Trạng thái: **PASS**.
- **Trang 21 (`page_21.png`):** Hàng tiêu đề lặp lại (`tblHeader`) của `Bảng 3.3` và 5 bước khảo sát (B2 đến B6), theo sau là Mục `3.2.2. Nhận diện phiên bản dịch vụ và đặc tính giao thức SMB` (13pt đậm nghiêng) và câu dẫn Hình 3.4. Trạng thái: **PASS**.
- **Trang 22 (`page_22.png`):** `Hình 3.4` (ảnh chụp kết quả Nmap version), chú thích `Hình 3.4` (12pt đậm), phân tích dấu vết phiên bản hệ điều hành (fingerprint range 2008 R2–2012 trong lần đo này) và câu dẫn Hình 3.5. Trạng thái: **PASS**.
- **Trang 23 (`page_23.png`):** `Hình 3.5` (ảnh chụp Nmap NSE SMB), chú thích `Hình 3.5` (12pt đậm), đoạn văn phân tích phương ngữ và chính sách ký số. Trạng thái: **PASS**.
- **Trang 24 (`page_24.png`):** Phân tích tính độc lập giữa kết quả từ xa và cấu hình nội bộ máy chủ, ranh giới an ninh Kịch bản 1, chuyển tiếp sang Mục `3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010` (14pt đậm) và đoạn mở đầu kịch bản. Trạng thái: **PASS**.
- **Trang 25 (`page_25.png`):** Mục `3.3.1. Khảo sát điều kiện kết nối và thuộc tính giao thức SMB (NSE-SMB-01 đến NSE-SMB-03)` (13pt đậm nghiêng), phân tích 3 phép đo đầu tiên về cổng, phương ngữ, signing và câu dẫn Bảng 3.4. Trạng thái: **PASS**.
- **Trang 26 (`page_26.png`):** Tiêu đề và 3 hàng dữ liệu đầu của `Bảng 3.4` (NSE-SMB-01, NSE-SMB-02, NSE-SMB-03) với các thông số phân loại kỹ thuật rõ ràng. Trạng thái: **PASS**.
- **Trang 27 (`page_27.png`):** Hàng tiêu đề lặp lại của `Bảng 3.4` cùng hàng thứ 4 (NSE-SMB-04), Mục `3.3.2. Đánh giá dấu hiệu lỗ hổng MS17-010 và đối chiếu trạng thái bản vá (NSE-SMB-04)` (13pt đậm nghiêng), câu dẫn, `Hình 3.6` (ảnh chụp smb-vuln-ms17-010) và chú thích `Hình 3.6`. Trạng thái: **PASS**.
- **Trang 28 (`page_28.png`):** Phân tích chi tiết việc vắng mặt khối `Host script results:`, phân loại phương pháp luận UNKNOWN / NO USABLE SCRIPT RESULT, nguyên tắc UNKNOWN != SAFE, đối chiếu hai trục thông tin độc lập (UNPATCHED nội bộ vs UNKNOWN từ xa). Trạng thái: **PASS**.
- **Trang 29 (`page_29.png`):** Giới hạn phạm vi Kịch bản 2 (không có khai thác/RCE), chuyển tiếp sang Mục `3.4. Kết quả Case B — Vô hiệu hóa SMBv1` (14pt đậm), Mục `3.4.1. Thao tác vô hiệu hóa SMBv1 và kiểm tra trạng thái máy chủ cục bộ` (13pt đậm nghiêng) và các lệnh PowerShell. Trạng thái: **PASS**.
- **Trang 30 (`page_30.png`):** Câu dẫn Hình 3.7, `Hình 3.7` (ảnh chụp PowerShell After Local), chú thích `Hình 3.7`, phân tích ranh giới kỹ thuật (SMBv1 disabled != FS-SMB1 uninstalled, SMBv1 disabled != PATCHED) và câu dẫn Bảng 3.5. Trạng thái: **PASS**.
- **Trang 31 (`page_31.png`):** Tiêu đề `Bảng 3.5` và 5 hàng so sánh đầu tiên (Cấu hình SMBv1, SMB2/3, Tính năng FS-SMB1, LanmanServer, Cổng TCP 445 từ xa). Trạng thái: **PASS**.
- **Trang 32 (`page_32.png`):** Hàng tiêu đề lặp lại của `Bảng 3.5` cùng 3 hàng so sánh tiếp theo (Phương ngữ SMB, MS17-010, Bản vá hệ thống srv.sys), đoạn tổng kết Bảng 3.5, Mục `3.4.2. Kết quả đo đạc lại từ xa và đối chiếu đa tầng` (13pt đậm nghiêng) và đoạn mở đầu đo lại. Trạng thái: **PASS**.
- **Trang 33 (`page_33.png`):** Nối tiếp câu văn đo lại, câu dẫn Hình 3.8, `Hình 3.8` (ảnh chụp NSE-SMB-02 retest), chú thích `Hình 3.8` và đoạn phân tích (NT LM 0.12 không xuất hiện trong danh sách phương ngữ đo lại, TCP 445 OPEN). Trạng thái: **PASS**.
- **Trang 34 (`page_34.png`):** Phân tích hai ranh giới kỹ thuật của Case B (445 OPEN != vulnerable, không có cảnh báo lỗ hổng != SAFE), tính chọn lọc của can thiệp cấu hình, chuyển tiếp sang Mục `3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense` (14pt đậm) và đoạn mở đầu kịch bản. Trạng thái: **PASS**.
- **Trang 35 (`page_35.png`):** Mục `3.5.1. Thiết lập cầu nối pfSense và chính sách kiểm soát lưu lượng SMB` (13pt đậm nghiêng), kiến trúc Transparent Bridge Layer 2 (bridge0 gồm em2 và em3 trên cùng dải phẳng 192.168.56.0/24), cấu hình tham số nhân FreeBSD (`pfil_member=1`, `pfil_bridge=0`), chính sách hai quy tắc lọc (Block TCP 139/445 và Pass baseline) và câu dẫn Hình 3.9. Trạng thái: **PASS**.
- **Trang 36 (`page_36.png`):** `Hình 3.9` (ảnh cấu hình quy tắc pfSense), chú thích `Hình 3.9`, đoạn thuyết minh Hình 3.9, câu dẫn Bảng 3.6, tiêu đề `Bảng 3.6` và hàng so sánh thứ nhất (Vị trí kiểm soát mạng / kiến trúc đường truyền). Trạng thái: **PASS**.
- **Trang 37 (`page_37.png`):** Hàng tiêu đề lặp lại của `Bảng 3.6` cùng 9 hàng so sánh tiếp theo (Chính sách lọc pfSense, Thứ tự quy tắc, TCP 139, TCP 445, Nhật ký tường lửa, MS17-010, Cấu hình SMBv1, LanmanServer, Bản vá cục bộ srv.sys) và đoạn văn phân tách hai tầng mạng vs máy chủ. Trạng thái: **PASS**.
- **Trang 38 (`page_38.png`):** Mục `3.5.2. Kết quả đo đạc từ xa, đối chiếu nhật ký tường lửa và trạng thái máy chủ` (13pt đậm nghiêng), câu dẫn Hình 3.10, `Hình 3.10` (ảnh chụp Nmap Filtered), chú thích `Hình 3.10` và đoạn phân tích trạng thái FILTERED/no-response (không suy ra cổng local đã đóng). Trạng thái: **PASS**.
- **Trang 39 (`page_39.png`):** Đối chiếu nhật ký tường lửa pfSense, câu dẫn Hình 3.11, `Hình 3.11` (ảnh chụp Block log của pfSense), chú thích `Hình 3.11`, phân tích các bản ghi TCP SYN bị chặn trên đường thử nghiệm và ranh giới quy thuộc tên luật. Trạng thái: **PASS**.
- **Trang 40 (`page_40.png`):** Đối chiếu đa tầng Case C (FILTERED từ xa vs listener nội bộ đang lắng nghe, FILTERED != PATCHED), khẳng định tính độc lập của trạng thái bản vá cục bộ UNPATCHED, chuyển tiếp sang Mục 3.6. Trạng thái: **PASS**.
- **Trang 41 (`page_41.png`):** Mục `3.6. So sánh kết quả thực nghiệm` (14pt đậm), 2 đoạn văn mở đầu tổng hợp, câu dẫn Bảng 3.7, tiêu đề `Bảng 3.7. So sánh trạng thái thực nghiệm giữa đường cơ sở, Case B và Case C` và 7 hàng dữ liệu so sánh đầu tiên. Trạng thái: **PASS**.
- **Trang 42 (`page_42.png`):** Hàng tiêu đề lặp lại của `Bảng 3.7` cùng hàng thứ 8 (Phán quyết MS17-010 từ xa), 3 đoạn văn phân tích so sánh chi tiết: Đối chiếu đường cơ sở vs Case B (tầng máy chủ), Đối chiếu đường cơ sở vs Case C (tầng mạng), So sánh trực tiếp Case B vs Case C. Trạng thái: **PASS**.
- **Trang 43 (`page_43.png`):** Đoạn tổng hợp ranh giới kỹ thuật cốt lõi (445 OPEN != vulnerable, SMBv1 enabled != MS17-010 confirmed, SMBv1 disabled != PATCHED, FILTERED != PATCHED, UNKNOWN != SAFE), Mục `3.7. Tổng kết chương` (14pt đậm) và 2 đoạn văn đầu của phần tổng kết chương. Trạng thái: **PASS**.
- **Trang 44 (`page_44.png`):** Đoạn văn thứ 3 và đoạn kết luận toàn chương của Mục 3.7: đúc kết các kết quả thực nghiệm đối chiếu đa tầng, nhấn mạnh việc thay đổi cấu hình giao thức và lọc lưu lượng trên đường mạng tạo ra những thay đổi quan sát được ở các lớp khác nhau trong khi trạng thái bản vá nội bộ phải được xác định độc lập; khép lại trọn vẹn phạm vi đo đạc thực nghiệm của Chương 3. Trạng thái: **PASS**.

---

## 5. Kiểm tra Cổng An Toàn & Khử Từ Khóa Lịch Sử (Forbidden Gate Audit)

| Tiêu chí cổng kiểm soát | Kết quả kiểm tra | Trạng thái |
|---|---|---|
| Không xuất hiện: `PHƯƠNG PHÁP THU THẬP BẰNG CHỨNG` | 0 lần xuất hiện | **PASS** |
| Không xuất hiện: `mô hình phân loại bằng chứng năm lớp` | 0 lần xuất hiện | **PASS** |
| Không xuất hiện: `Mô hình ánh xạ mục tiêu nghiên cứu` | 0 lần xuất hiện | **PASS** |
| Không xuất hiện: `Trạng thái kiểm toán tiền thực nghiệm` | 0 lần xuất hiện | **PASS** |
| Không xuất hiện: `Cây quyết định phân loại trạng thái kiểm định lỗ hổng` | 0 lần xuất hiện | **PASS** |
| Không có Bảng 3.8 | 0 lần xuất hiện | **PASS** |
| Không có Hình 3.12 | 0 lần xuất hiện | **PASS** |
| Không có tiêu đề Chương 1 | 0 lần xuất hiện | **PASS** |
| Không có tiêu đề Chương 4 (chỉ có từ tham chiếu thảo luận trong văn bản gốc Ch2) | 0 tiêu đề Chương 4 | **PASS** |
| Không có khai thác thâm nhập / reverse shell / Meterpreter | 0 lần xuất hiện | **PASS** |
| Khóa kỹ thuật: `445 OPEN != vulnerable` | Xuất hiện đầy đủ, đúng ngữ cảnh | **PASS** |
| Khóa kỹ thuật: `SMBv1 enabled != MS17-010 confirmed` | Xuất hiện đầy đủ, đúng ngữ cảnh | **PASS** |
| Khóa kỹ thuật: `SMBv1 disabled != PATCHED` | Xuất hiện đầy đủ, đúng ngữ cảnh | **PASS** |
| Khóa kỹ thuật: `FILTERED != PATCHED` | Xuất hiện đầy đủ, đúng ngữ cảnh | **PASS** |
| Khóa kỹ thuật: `UNKNOWN != SAFE` | Xuất hiện đầy đủ, đúng ngữ cảnh | **PASS** |

---

## 6. Kết luận nghiệm thu chất lượng hình thức (Final Formatting Verdict)

Tệp `work/do-an/output/CHAPTER_2_3_REVIEW.docx` được ráp hoàn toàn từ nguồn canonical đã phê duyệt của Chương 2 (`work/do-an/CHAPTER_2.md`) và Chương 3 (`work/do-an/CHAPTER_3_DRAFT_R2.md`), đạt độ chính xác 100% về mặt nội dung, không có bất kỳ sửa đổi hay tái diễn giải kỹ thuật nào, đáp ứng nghiêm ngặt toàn bộ các quy chuẩn định dạng luận văn/đồ án HUIT 2024. Toàn bộ 44 trang đã được kết xuất và kiểm định trực quan, không có lỗi trang trắng, không xé vụn dòng hay bảng biểu, hình ảnh và chú thích đồng bộ trọn vẹn trên từng trang.
