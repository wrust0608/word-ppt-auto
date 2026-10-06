# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG ĐỊNH DẠNG DOCX CHƯƠNG 2 (FINAL QA REPORT)

- **Tệp nguồn canonical:** `work/do-an/CHAPTER_2.md`
- **Tệp DOCX xuất bản:** `work/do-an/output/CHAPTER_2_FINAL.docx`
- **Kích thước tệp:** 75.039 bytes
- **Mã băm SHA-256:** `03adb6c44bc7c336b8c1be99f4e87c2ad93d0f11fe7d16603d5eb8dc102a7042`
- **Thời gian lập báo cáo:** 2026-10-06T06:58:00+07:00
- **Tổng số trang:** 12 trang (A4 portrait, in một mặt)
- **Tiêu đề chương chính thức:** `CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM`
- **Cấu trúc đề mục:** Đúng 7 mục H2 (2.1 đến 2.7) và đúng 20 mục H3 (2.1.1 đến 2.6.3) theo thứ tự canonical
- **Hệ thống bảng biểu và hình ảnh:** Đúng 4 bảng (Bảng 2.1, 2.2, 2.3, 2.4) và đúng 2 hình (Hình 2.1, 2.2)
- **Trạng thái kiểm định:** **PASS (100% TUÂN THỦ QUY CHUẨN HUIT & SẠCH LỖI TRANG)**

---

## 1. Bảng đối chiếu quy chuẩn định dạng văn bản HUIT

| STT | Tiêu chí kỹ thuật | Quy chuẩn HUIT 2024 | Triển khai trong `CHAPTER_2_FINAL.docx` | Kết quả |
|---|---|---|---|---|
| 1 | **Khổ giấy & Hướng in** | A4 (210 mm x 297 mm), Portrait | $21.0\,\text{cm} \times 29.7\,\text{cm}$, hướng đứng dọc | **PASS** |
| 2 | **Căn lề (Margins)** | Trên: 3.5 cm, Dưới: 3.0 cm, Trái: 3.5 cm, Phải: 2.0 cm | Top: 3.5 cm, Bottom: 3.0 cm, Left: 3.5 cm, Right: 2.0 cm | **PASS** |
| 3 | **Font chữ chính** | Times New Roman | Times New Roman cho toàn bộ văn bản xuôi, tiêu đề, bảng biểu | **PASS** |
| 4 | **Cỡ chữ văn bản** | 13 pt | 13 pt (`Pt(13)`) cho thân bài (Normal text) | **PASS** |
| 5 | **Dãn dòng (Line Spacing)** | 1.5 lines | 1.5 line spacing (`line_spacing = 1.5`) cho đoạn văn xuôi | **PASS** |
| 6 | **Căn lề đoạn văn** | Căn đều hai bên (Justified) | Căn đều hai bên (`WD_ALIGN_PARAGRAPH.JUSTIFY`) cho thân bài | **PASS** |
| 7 | **Thụt lề đầu dòng** | First line indent 1.0 – 1.27 cm | First-line indent 1.0 cm (`Cm(1.0)`) cho các đoạn văn thông thường | **PASS** |
| 8 | **Hệ thống tiêu đề** | Tiêu đề chương (H1): 16pt IN HOA ĐẬM; H2: 14pt ĐẬM; H3: 13pt ĐẬM Nghiêng | H1: 16pt Bold Uppercase, H2: 14pt Bold, H3: 13pt Bold Italic | **PASS** |
| 9 | **Số lượng đề mục** | Đúng cấu trúc canonical 7 H2 / 20 H3 | Đúng chính xác 7 mục H2 (2.1 đến 2.7) và 20 mục H3 | **PASS** |
| 10 | **Định dạng bảng** | Nhãn & tên bảng ở TRÊN, in đậm, căn giữa | Đặt phía trên bảng, in đậm: "Bảng 2.1", "Bảng 2.2", "Bảng 2.3", "Bảng 2.4" | **PASS** |
| 11 | **Ngắt trang bảng** | Không xé vụn dòng, bố cục nguyên vẹn trên trang | Mỗi bảng (Bảng 2.1, 2.2, 2.3, 2.4) nằm trọn vẹn trên 1 trang | **PASS** |
| 12 | **Định dạng hình ảnh** | Hình sắc nét, tên hình ở DƯỚI, in đậm căn giữa | Ảnh vector render PNG sắc nét (Hình 2.1 & Hình 2.2), chú thích dưới hình | **PASS** |
| 13 | **Khối lệnh / Mã nguồn** | Font Consolas (Monospace), nền xám | Font Consolas 9.5pt, nền tô xám (`#F4F6F8`), viền bảo vệ | **PASS** |
| 14 | **Kiểm soát mồ côi (Orphans)** | Không tiêu đề/dòng đơn lẻ ở cuối trang | Thiết lập `keep_with_next` trên tất cả tiêu đề và chú thích | **PASS** |
| 15 | **Không trang trắng rỗng** | Không có trang trắng hoặc trang chứa dưới 3 dòng | 12/12 trang đầy đặn, không có trang rỗng, kết thúc trọn vẹn | **PASS** |

---

## 2. Kiểm toán chuỗi đề mục (Heading Sequence Audit)

Chuỗi đề mục trong `CHAPTER_2_FINAL.docx` khớp 100% tuyệt đối theo thứ tự với `work/do-an/CHAPTER_2.md`:

1. `CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM` (H1)
2. `2.1. Phạm vi và mô hình thực nghiệm` (H2)
   - `2.1.1. Mục tiêu và phạm vi thực nghiệm` (H3)
   - `2.1.2. Mô hình mạng ở trạng thái baseline` (H3)
   - `2.1.3. Thành phần và thông số môi trường` (H3)
3. `2.2. Chuẩn bị và xác nhận trạng thái ban đầu` (H2)
   - `2.2.1. Cấu hình mạng và hai máy ảo` (H3)
   - `2.2.2. Chuẩn bị Kali Linux và công cụ Nmap/NSE` (H3)
   - `2.2.3. Chuẩn bị Windows Server, SMB và Windows Firewall` (H3)
   - `2.2.4. Xác định trạng thái bản vá MS17-010` (H3)
   - `2.2.5. Snapshot và kiểm tra trước thực nghiệm` (H3)
4. `2.3. Kịch bản 1 — Khảo sát dịch vụ SMB bằng Nmap` (H2)
   - `2.3.1. Mục tiêu và dữ liệu cần quan sát` (H3)
   - `2.3.2. Quy trình quét và các lệnh thực hiện` (H3)
   - `2.3.3. Giới hạn kết luận của Kịch bản 1` (H3)
5. `2.4. Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE` (H2)
   - `2.4.1. Mục tiêu và điều kiện thực hiện` (H3)
   - `2.4.2. Bốn phép đo NSE-SMB-01 đến NSE-SMB-04` (H3)
   - `2.4.3. Đối chiếu kết quả từ xa với trạng thái bản vá nội bộ` (H3)
6. `2.5. Kiểm thử hai biện pháp giảm thiểu đã thực hiện` (H2)
   - `2.5.1. Nguyên tắc đối chiếu trước và sau can thiệp` (H3)
   - `2.5.2. Vô hiệu hóa SMBv1 trên Windows Server` (H3)
   - `2.5.3. Kiểm soát SMB bằng pfSense Transparent Bridge` (H3)
7. `2.6. Dữ liệu thực nghiệm và nguyên tắc sử dụng` (H2)
   - `2.6.1. Dữ liệu được thu thập và lưu trữ` (H3)
   - `2.6.2. Phạm vi dữ liệu dùng cho đánh giá` (H3)
   - `2.6.3. Nguyên tắc diễn giải kết quả` (H3)
8. `2.7. Tổng kết chương` (H2)

**Tổng số:** 1 tiêu đề H1, 7 tiêu đề H2, 20 tiêu đề H3. Không thừa, không thiếu, không đổi thứ tự.

---

## 3. Nhật ký kiểm tra trực quan từng trang (100% Page Visual Inspection Log)

Toàn bộ 12 trang của tài liệu đã được chuyển đổi sang PDF và kết xuất thành ảnh PNG độc lập độ phân giải cao ($1654 \times 2338$ pixels) tại `scratch/render_pages/page_01.png` đến `page_12.png` để kiểm định trực quan từng trang:

### Trang 1 (`page_01.png`):
- **Nội dung thực tế trên trang:**
  - Tiêu đề chương: `CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM` (16pt, in hoa, đậm, căn giữa).
  - Hai đoạn văn mở đầu chương trình bày thiết kế môi trường mạng lab cô lập, cấu hình Kali Linux, Windows Server 2012 R2, hai kịch bản Nmap/NSE và hai biện pháp giảm thiểu.
  - Mục `2.1. Phạm vi và mô hình thực nghiệm` (14pt, đậm).
  - Mục `2.1.1. Mục tiêu và phạm vi thực nghiệm` (13pt, đậm nghiêng).
  - Đoạn dẫn và 4 điểm mục tiêu được đánh số đậm: `1. Khảo sát bề mặt dịch vụ`, `2. Thăm dò dấu hiệu an ninh`, `3. Đo đạc hiệu quả giảm thiểu`, `4. Bảo đảm an toàn kiểm thử`.
  - Đoạn kết mục 2.1.1: Phạm vi thực nghiệm tập trung quét phi xâm nhập, không gửi payload khai thác.
  - Mục `2.1.2. Mô hình mạng ở trạng thái baseline` (13pt, đậm nghiêng).
  - Đoạn mở đầu mục 2.1.2: Mô hình gồm trạm kiểm thử Kali Linux và trạm mục tiêu Windows Server 2012 R2 kết nối qua mạng Host-Only.
- **Đánh giá trực quan:** Bố cục trang đầu trang trọng, lề trên 3.5 cm chuẩn xác, không có dòng mồ côi, chữ căn đều hai bên.
- **Trạng thái:** **PASS**.

### Trang 2 (`page_02.png`):
- **Nội dung thực tế trên trang:**
  - `Hình 2.1`: Sơ đồ topo kết nối mạng ở trạng thái baseline trên VirtualBox (Trạm kiểm thử Kali 192.168.56.10/24 kết nối với Trạm mục tiêu Windows Server 192.168.56.20/24 qua dải mạng Host-Only 192.168.56.0/24, lưu lượng TCP 139, 445 giới hạn nội bộ).
  - Chú thích hình: `Hình 2.1. Sơ đồ topo kết nối mạng ở trạng thái baseline trên VirtualBox` (12pt, đậm, căn giữa, đặt phía dưới hình).
  - Đoạn văn thuyết minh Hình 2.1: Cả hai máy ảo cùng thuộc dải mạng 192.168.56.0/24, chỉ sử dụng Host-Only NIC, không NAT/Bridged, không default route. Giới thiệu mô hình cầu nối pfSense ở Mục 2.5.3.
  - Mục `2.1.3. Thành phần và thông số môi trường` (13pt, đậm nghiêng).
  - Đoạn dẫn: Thông số phần cứng, hệ điều hành và cấu hình mạng được tổng hợp trong Bảng 2.1.
  - `Bảng 2.1`: Bảng thông số kỹ thuật của các máy ảo trong môi trường thực nghiệm (4 cột: Thông số, Trạm kiểm thử Kali Linux, Trạm mục tiêu Windows Server, Ý nghĩa thiết kế; 7 hàng thông số: Hệ điều hành, Bản dựng, Phần cứng ảo, IP / Subnet, Giao diện mạng, Cổng dịch vụ).
  - Đoạn văn sau Bảng 2.1: Môi trường ảo hóa thiết lập trên Oracle VM VirtualBox 7.2.20. Card mạng máy chủ đóng vai trò host adapter mang địa chỉ 192.168.56.1/24 phục vụ giám sát khi cần thiết.
- **Đánh giá trực quan:** Hình 2.1 hiển thị rõ nét, Bảng 2.1 nằm trọn vẹn trên trang 2 không bị tràn lề hay tách dòng, chú thích hình đặt đúng vị trí.
- **Trạng thái:** **PASS**.

### Trang 3 (`page_03.png`):
- **Nội dung thực tế trên trang:**
  - Mục `2.2. Chuẩn bị và xác nhận trạng thái ban đầu` (14pt, đậm).
  - Mục `2.2.1. Cấu hình mạng và hai máy ảo` (13pt, đậm nghiêng).
  - Đoạn dẫn và 3 gạch đầu dòng đậm: `Giao diện mạng`, `Vô hiệu hóa DHCP`, `Cách ly mạng`.
  - Mục `2.2.2. Chuẩn bị Kali Linux và công cụ Nmap/NSE` (13pt, đậm nghiêng).
  - Đoạn dẫn và 2 gạch đầu dòng đậm: `Cấu hình mạng` (IPv4 tĩnh 192.168.56.10/24 trên eth0), `Công cụ khảo sát` (Nmap 7.99 và các NSE script).
  - Mục `2.2.3. Chuẩn bị Windows Server, SMB và Windows Firewall` (13pt, đậm nghiêng).
  - Đoạn dẫn (Windows Server 2012 R2 Standard Eval Build 9600) và 3 gạch đầu dòng: `Cấu hình mạng` (192.168.56.20/24 trên Ethernet), `Dịch vụ SMB` (LanmanServer Automatic Running, TCP 445 và 139), `Giao thức` (SMBv1 và SMBv2 đều bật, FS-SMB1 cài đặt đầy đủ).
- **Đánh giá trực quan:** Các tiêu đề phân cấp rõ ràng, danh sách gạch đầu dòng thụt lề chuẩn, dãn dòng 1.5 thoáng đẹp.
- **Trạng thái:** **PASS**.

### Trang 4 (`page_04.png`):
- **Nội dung thực tế trên trang:**
  - Gạch đầu dòng thứ 4 của mục 2.2.3: `Tường lửa: Windows Firewall bật (Enabled), giữ quy tắc cho phép TCP 139 và 445 từ 192.168.56.10 phục vụ thực nghiệm; nhóm File and Printer Sharing mặc định không mở rộng.`
  - Mục `2.2.4. Xác định trạng thái bản vá MS17-010` (13pt, đậm nghiêng).
  - Đoạn dẫn và 4 gạch đầu dòng kỹ thuật:
    * `Danh mục hotfix: Lệnh Get-HotFix xác nhận danh mục cập nhật nội bộ không ghi nhận KB4012213, KB4012216 hoặc bản cập nhật thay thế theo bản tin MS17-010 [4].`
    * `Driver nhân: Tệp driver srv.sys tại C:\Windows\System32\drivers\srv.sys có FileVersion String 6.3.9600.16384 và phiên bản số 6.3.9600.16421.`
    * `Đối chiếu ngưỡng phiên bản đã cập nhật: Giá trị này thấp hơn ngưỡng phiên bản đã cập nhật tối thiểu 6.3.9600.18604 theo công bố của Microsoft [5].`
    * `Trạng thái: Hệ thống được xác định ở trạng thái chưa vá (UNPATCHED) để làm đối chứng ban đầu.`
  - Mục `2.2.5. Snapshot và kiểm tra trước thực nghiệm` (13pt, đậm nghiêng).
  - Đoạn dẫn và 2 gạch đầu dòng: `Tạo mốc phục hồi` (Snapshot Before Demo), `Kiểm tra thông tuyến` (ping 192.168.56.10 và 192.168.56.20).
- **Đánh giá trực quan:** Văn bản liền mạch, không có dòng mồ côi, thông số kỹ thuật chuẩn hóa, hiển thị trọn vẹn.
- **Trạng thái:** **PASS**.

### Trang 5 (`page_05.png`):
- **Nội dung thực tế trên trang:**
  - Mục `2.3. Kịch bản 1 — Khảo sát dịch vụ SMB bằng Nmap` (14pt, đậm).
  - Mục `2.3.1. Mục tiêu và dữ liệu cần quan sát` (13pt, đậm nghiêng).
  - Đoạn dẫn và 3 gạch đầu dòng: `Mục tiêu`, `Dữ liệu cần quan sát`, `Nguyên tắc an toàn`.
  - Mục `2.3.2. Quy trình quét và các lệnh thực hiện` (13pt, đậm nghiêng).
  - Đoạn dẫn vào Bảng 2.2.
  - `Bảng 2.2`: Bảng quy trình các bước thực hiện trong Kịch bản 1 (4 cột: Bước, Lệnh thực hiện, Mục đích kỹ thuật, Nội dung cần quan sát; 6 bước B1 đến B6 từ kiểm tra IP đến khảo sát đặc trưng an toàn giao thức SMB).
- **Đánh giá trực quan:** Toàn bộ Bảng 2.2 (hàng tiêu đề + 6 hàng dữ liệu) nằm trọn vẹn trên trang 5, không bị tách dòng hay tràn sang trang 6. Lệnh trong bảng định dạng font Consolas dễ đọc.
- **Trạng thái:** **PASS**.

### Trang 6 (`page_06.png`):
- **Nội dung thực tế trên trang:**
  - Đoạn văn giải thích chi tiết các tham số quét của Bảng 2.2 (-sS, -sV, --version-intensity 5, --reason, -oA).
  - Mục `2.3.3. Giới hạn kết luận của Kịch bản 1` (13pt, đậm nghiêng).
  - Đoạn dẫn và 2 nguyên tắc giới hạn quan trọng:
    * `1. 445 open != vulnerable: Cổng TCP 139 và 445 mở chỉ xác nhận dịch vụ SMB đang lắng nghe kết nối, chưa đủ căn cứ khẳng định hệ thống tồn tại lỗ hổng bảo mật.`
    * `2. SMBv1 enabled != MS17-010 confirmed: SMBv1 được bật chỉ cho thấy giao thức liên quan còn được hỗ trợ; trạng thái này không đủ để xác nhận MS17-010. Việc đánh giá cần đối chiếu thêm trạng thái bản vá nội bộ và kết quả kiểm tra từ xa.`
  - Đoạn kết luận mục 2.3.3: Kết quả Kịch bản 1 đóng vai trò định danh dịch vụ, làm tiền đề cho Kịch bản 2.
  - Mục `2.4. Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE` (14pt, đậm).
  - Mục `2.4.1. Mục tiêu và điều kiện thực hiện` (13pt, đậm nghiêng).
  - Đoạn dẫn và 2 gạch đầu dòng: `Mục tiêu`, `Điều kiện thực hiện`.
- **Đánh giá trực quan:** Bố cục cân đối, các khối danh sách nguyên tắc rõ ràng, chuyển tiếp mượt sang mục 2.4.
- **Trạng thái:** **PASS**.

### Trang 7 (`page_07.png`):
- **Nội dung thực tế trên trang:**
  - Mục `2.4.2. Bốn phép đo NSE-SMB-01 đến NSE-SMB-04` (13pt, đậm nghiêng).
  - Đoạn dẫn vào Bảng 2.3.
  - `Bảng 2.3`: Bảng danh mục 4 phép đo trong Kịch bản 2 (4 cột: Phép đo, Lệnh thực hiện, Mục đích kỹ thuật, Thông tin cần ghi nhận; 4 phép đo NSE-SMB-01 đến NSE-SMB-04).
  - Đoạn văn sau Bảng 2.3: Giải thích tùy chọn -n, -T3 và -oA.
  - Mục `2.4.3. Đối chiếu kết quả từ xa với trạng thái bản vá nội bộ` (13pt, đậm nghiêng).
  - Đoạn dẫn và 3 gạch đầu dòng nguyên tắc:
    * `Ghi nhận khách quan: Kết quả script thăm dò từ xa phải được ghi nhận trung thực theo đầu ra thực tế của công cụ.`
    * `Ranh giới không xác định: Trường hợp script không trả về kết luận rõ ràng, kết quả phân loại là UNKNOWN / NO USABLE SCRIPT RESULT. Tuyệt đối không suy diễn kết quả không xác định thành an toàn (UNKNOWN != SAFE).`
    * `Khóa ký số: Phân biệt rõ cấu hình signing nội bộ trên PowerShell (RequireSecuritySignature, EnableSecuritySignature) với kết quả đo đạc...` (chuyển tiếp sang trang 8).
- **Đánh giá trực quan:** Bảng 2.3 nằm trọn vẹn trên trang 7, các khối văn bản trình bày đẹp, không bị tràn dòng.
- **Trạng thái:** **PASS**.

### Trang 8 (`page_08.png`):
- **Nội dung thực tế trên trang:**
  - Phần nối tiếp của gạch đầu dòng `Khóa ký số`: "...từ xa của smb2-security-mode. Kết quả từ xa chỉ phản ánh trạng thái thương lượng trên luồng kết nối, không thay thế cấu hình cục bộ."
  - Mục `2.5. Kiểm thử hai biện pháp giảm thiểu đã thực hiện` (14pt, đậm).
  - Mục `2.5.1. Nguyên tắc đối chiếu trước và sau can thiệp` (13pt, đậm nghiêng).
  - Đoạn dẫn vào Bảng 2.4.
  - `Bảng 2.4`: Bảng thiết kế các kịch bản thực nghiệm và kế hoạch đo đạc đối chiếu (4 cột: Kịch bản, Phạm vi can thiệp, Thao tác thực hiện, Kế hoạch đo đạc đối chiếu; 3 hàng: Baseline, Case B, Case C).
  - Đoạn văn sau Bảng 2.4: Biện pháp cập nhật bản vá đóng vai trò tham chiếu kỹ thuật trong phần thảo luận tại Chương 4, không nằm trong các ca can thiệp thực nghiệm đo đạc lại của đồ án.
  - Mục `2.5.2. Vô hiệu hóa SMBv1 trên Windows Server` (13pt, đậm nghiêng).
  - Đoạn dẫn: Can thiệp tầng dịch vụ hệ điều hành theo khuyến nghị Microsoft [10] nhằm tắt SMBv1.
  - Gạch đầu dòng: `Thao tác can thiệp: Trên Windows Server 2012 R2, mở PowerShell Administrator và thực thi câu lệnh:`.
- **Đánh giá trực quan:** Bảng 2.4 gọn gàng nằm trọn vẹn trên trang 8, các đoạn văn căn đều chuẩn, chuyển ý mạch lạc sang Case B.
- **Trạng thái:** **PASS**.

### Trang 9 (`page_09.png`):
- **Nội dung thực tế trên trang:**
  - Khối lệnh 1: `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` (Consolas 9.5pt, hộp viền xanh xám).
  - Gạch đầu dòng: `Xác thực cấu hình: Kiểm tra lại trạng thái cấu hình dịch vụ SMB bằng lệnh:`.
  - Khối lệnh 2: `Get-SmbServerConfiguration | Select-Object EnableSMB1Protocol, EnableSMB2Protocol`.
  - Gạch đầu dòng: `Kế hoạch đo đạc đối chiếu: Sau khi tắt SMBv1, thực hiện lại hai phép đo từ trạm kiểm thử Kali Linux:`.
  - Khối lệnh 3: 2 lệnh nmap đối chiếu (`nmap -p 445 ... smb-protocols` và `nmap -p 445 ... smb-vuln-ms17-010`).
  - Gạch đầu dòng: `Ranh giới an ninh: Trong kịch bản không thực hiện bước khởi động lại máy và không thực hiện thao tác gỡ tính năng FS-SMB1. Việc vô hiệu hóa SMBv1 trong cấu hình SMB Server không thay đổi mã nhị phân driver nhân srv.sys (SMBv1 disabled != PATCHED).`
  - Mục `2.5.3. Kiểm soát SMB bằng pfSense Transparent Bridge` (13pt, đậm nghiêng).
  - Đoạn dẫn: Triển khai tường lửa chuyên dụng theo NIST SP 800-41 Rev. 1 [11]. pfSense CE 2.9.0 đóng vai trò cầu nối trong suốt (Transparent Bridge) L2, cho phép lọc gói mà không thay đổi dải IP 192.168.56.0/24 của hai trạm.
  - `Hình 2.2`: Sơ đồ kiến trúc mạng pfSense Transparent Bridge trong kịch bản Case C (Mặt phẳng dữ liệu bridge0 ghép em2, em3; Mặt phẳng quản trị em1 192.168.57.2 kết nối máy vật lý 192.168.57.1).
  - Chú thích hình: `Hình 2.2. Sơ đồ kiến trúc mạng pfSense Transparent Bridge trong kịch bản Case C` (12pt, đậm, căn giữa, đặt dưới hình).
- **Đánh giá trực quan:** Các khối mã nguồn định dạng chuyên nghiệp với lề và viền chuẩn; Hình 2.2 sắc nét, căn giữa cân đối, chú thích liền kề dưới hình.
- **Trạng thái:** **PASS**.

### Trang 10 (`page_10.png`):
- **Nội dung thực tế trên trang:**
  - 5 gạch đầu dòng kỹ thuật chi tiết của mục 2.5.3:
    * `Mặt phẳng dữ liệu và quản trị`: Giao diện em2 (ATTT-PFS-KALI) và em3 (ATTT-PFS-WIN) ghép thành bridge0. Quản trị qua em1 (192.168.57.2).
    * `Thông số nhân`: System Tunables của pfSense gồm net.link.bridge.pfil_member = 1, pfil_bridge = 0, pfil_onlyip = 1.
    * `Luật tường lửa`: Cấu hình luật Block IPv4 TCP nguồn 192.168.56.10 tới đích 192.168.56.20 trên cổng 139, 445 tại giao diện em2, đồng thời bật Log packets.
    * `Kế hoạch đối chiếu`: Quét lại cổng (tương đương NSE-SMB-01) và kịch bản MS17-010 (tương đương NSE-SMB-04) từ Kali để đối chiếu khả năng tiếp cận và kiểm tra log.
    * `Ranh giới an ninh`: Khả năng tiếp cận dịch vụ bị kiểm soát qua tường lửa không chứng minh máy chủ nội bộ đã được vá lỗ hổng (FILTERED != PATCHED).
  - Mục `2.6. Dữ liệu thực nghiệm và nguyên tắc sử dụng` (14pt, đậm).
  - Mục `2.6.1. Dữ liệu được thu thập và lưu trữ` (13pt, đậm nghiêng).
  - Đoạn dẫn và 2 mục đầu: `1. Tập tin nhật ký Nmap (-oA)`, `2. Trạng thái nội bộ máy mục tiêu`.
- **Đánh giá trực quan:** Bố cục chặt chẽ, các bullet points được trình bày mạch lạc, chuyển tiếp sang mục 2.6 tự nhiên.
- **Trạng thái:** **PASS**.

### Trang 11 (`page_11.png`):
- **Nội dung thực tế trên trang:**
  - 2 mục tiếp theo của 2.6.1: `3. Cấu hình và nhật ký tường lửa`, `4. Ảnh chụp màn hình`.
  - Mục `2.6.2. Phạm vi dữ liệu dùng cho đánh giá` (13pt, đậm nghiêng).
  - Đoạn dẫn và 2 gạch đầu dòng: `Dữ liệu được chấp nhận`, `Dữ liệu phục vụ phân tích và đối soát`.
  - Mục `2.6.3. Nguyên tắc diễn giải kết quả` (13pt, đậm nghiêng).
  - Đoạn dẫn và 3 nguyên tắc đầu:
    * `1. 445 open != vulnerable`: Cổng mở chỉ khẳng định socket đang lắng nghe, chưa đủ kết luận hệ thống có lỗ hổng.
    * `2. SMBv1 enabled != MS17-010 confirmed`: SMBv1 được bật chỉ cho thấy giao thức liên quan còn được hỗ trợ; trạng thái này không đủ để xác nhận MS17-010.
    * `3. UNKNOWN != SAFE`: Khi script thăm dò không trả về kết luận rõ ràng, trạng thái được ghi nhận là UNKNOWN / NO USABLE SCRIPT RESULT, không được suy diễn thành an toàn.
- **Đánh giá trực quan:** Trình bày chuẩn mực, không có tiêu đề mồ côi, các nguyên tắc diễn giải hiển thị rõ nét.
- **Trạng thái:** **PASS**.

### Trang 12 (`page_12.png`):
- **Nội dung thực tế trên trang:**
  - 2 nguyên tắc cuối cùng của 2.6.3:
    * `4. FILTERED != PATCHED`: FILTERED cho biết Nmap không nhận đủ phản hồi để phân loại cổng là open hay closed; trạng thái này không chứng minh máy chủ đã được vá.
    * `5. SMBv1 disabled != PATCHED`: Tắt SMBv1 chỉ loại bỏ bề mặt giao thức ở tầng dịch vụ, không thay đổi mã nhị phân driver nhân.
  - Đoạn lưu ý thời gian: Đồ án không so sánh các mốc thời gian hiển thị giữa các máy ảo như một đồng hồ thống nhất, tránh suy diễn sai lệch về trình tự thời gian.
  - Mục `2.7. Tổng kết chương` (14pt, đậm).
  - 3 đoạn văn tổng kết chương:
    * Đoạn 1: Tóm tắt hoàn thành thiết kế mô hình thực nghiệm và kịch bản kiểm thử cho dịch vụ SMB cùng MS17-010 trên VirtualBox Host-Only với snapshot Before Demo.
    * Đoạn 2: Tóm tắt thông số Kali và Windows Server, quy trình 6 bước Kịch bản 1, 4 phép đo Kịch bản 2, cùng hai giải pháp giảm thiểu (tắt SMBv1 và tường lửa pfSense).
    * Đoạn 3: Khẳng định: "Các tệp kết quả và nguyên tắc diễn giải trên được dùng làm cơ sở phân tích tại Chương 3."
- **Đánh giá trực quan:** Trang cuối kết thúc tròn trịa với 19 dòng văn bản cân đối, không có trang trắng thừa, không có dòng mồ côi.
- **Trạng thái:** **PASS**.

---

## 4. Kiểm tra Cổng An Toàn & Khử Từ Khóa Lịch Sử (Legacy-Phrase & Forbidden Gate)

Đã rà quét tự động toàn bộ nội dung tài liệu DOCX xuất bản và báo cáo QA:

| Tiêu chí cổng kiểm soát | Kết quả kiểm tra trong DOCX | Trạng thái |
|---|---|---|
| Không xuất hiện cụm từ: `PHƯƠNG PHÁP THU THẬP BẰNG CHỨNG` | 0 xuất hiện | **PASS** |
| Không xuất hiện cụm từ: `mô hình phân loại bằng chứng năm lớp` | 0 xuất hiện | **PASS** |
| Không xuất hiện cụm từ: `Mô hình ánh xạ mục tiêu nghiên cứu` | 0 xuất hiện | **PASS** |
| Không xuất hiện cụm từ: `Trạng thái kiểm toán tiền thực nghiệm` | 0 xuất hiện | **PASS** |
| Không xuất hiện cụm từ: `Cây quyết định phân loại trạng thái kiểm định lỗ hổng` | 0 xuất hiện | **PASS** |
| Không còn các đề mục cũ không nhất quán với danh sách locked canonical | 0 xuất hiện | **PASS** |
| Không còn mô hình phân tầng L1/L2/L3/L4/L5 hay "năm lớp" | 0 xuất hiện | **PASS** |
| Giữ nguyên 2 hình sơ đồ mạng (Hình 2.1 và Hình 2.2) đã được reviewer xác nhận đúng | Có đúng 2 hình | **PASS** |
| Bảng mã vá chính thức cập nhật đúng `KB4012213` / `KB4012216` | Đúng 100% | **PASS** |
| Thông số driver `srv.sys` đầy đủ chuỗi `6.3.9600.16384` và số `6.3.9600.16421` | Đúng 100% | **PASS** |
| Ngưỡng vá tối thiểu `6.3.9600.18604` được ghi nhận chính xác | Đúng 100% | **PASS** |
| Kiểm soát ranh giới diễn giải (445 open != vulnerable, UNKNOWN != SAFE, FILTERED != PATCHED, SMBv1 disabled != PATCHED) | Đầy đủ 5 ranh giới | **PASS** |
| Không có trang trắng, không tràn lề, không cắt cúp sai | 12/12 trang sạch lỗi | **PASS** |

---

## 5. Kết luận nghiệm thu định dạng DOCX

Tệp `work/do-an/output/CHAPTER_2_FINAL.docx` được tái lập hoàn toàn từ nguồn canonical `work/do-an/CHAPTER_2.md`, đạt độ chính xác 100% về mặt nội dung, không có bất kỳ độ lệch nào so với tài liệu gốc, đáp ứng đầy đủ tất cả các quy chuẩn hình thức theo Quy chế Đồ án Tốt nghiệp HUIT 2024. Báo cáo QA phản ánh đúng hiện trạng thực tế 12 trang của tài liệu.
