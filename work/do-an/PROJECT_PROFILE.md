# Hồ sơ dự án

## Nhận diện

- Mã dự án: do-an
- Tên công trình: Xây dựng mô hình kiểm thử lỗ hổng SMB trên Windows bằng Kali Linux
- Loại công trình: Đồ án chuyên ngành An toàn thông tin
- Ngành/chuyên ngành: An toàn thông tin (Khoa Công nghệ Thông tin - HUIT)
- Ngôn ngữ: Tiếng Việt
- Tác giả/nhóm tác giả:
  - Lâm Gia Bảo (MSSV: 2033216350, Lớp: 12DHBM03)
  - Nguyễn Minh Thắng (MSSV: 2033216558, Lớp: 12DHBM03)
  - Nguyễn Hoài Tiến (MSSV: 2033216575, Lớp: 12DHBM09)
- Người hướng dẫn: ThS. Ngô Quốc Huy (thông tin liên hệ được lưu cục bộ trong `CONTACTS.local.md`, không đưa lên Git)
- Thời hạn: 10 tuần (24/08/2026 - 18/10/2026)

## Vấn đề nghiên cứu

- Bối cảnh: Server Message Block (SMB) là giao thức truyền thông mạng nội bộ mặc định trên Windows, vận hành ở cấp nhân (kernel-mode driver srv.sys / srv2.sys). Các lỗ hổng quản lý bộ nhớ trong SMBv1, tiêu biểu là MS17-010 (CVE-2017-0144 / EternalBlue), cho phép thực thi mã từ xa (RCE) không cần chứng thực, gây ra các cuộc tấn công mạng nghiêm trọng trên phạm vi toàn cầu như WannaCry.
- Vấn đề cần giải quyết:
  1. Phân tích kiến trúc, dialect negotiation, session setup và cơ chế xử lý gói tin của SMB qua cổng TCP 139/445; làm rõ sự khác biệt giữa SMBv1, SMBv2 và SMBv3.
  2. Phân tích cơ chế phát sinh lỗi bộ nhớ dẫn đến MS17-010 trong driver srv.sys.
  3. Xây dựng mô hình mạng lab cô lập, quy trình nhận diện dịch vụ, quét đánh giá và tiêu chí xác minh trạng thái an toàn của SMB.
  4. Đề xuất và phân tích các giải pháp giảm thiểu: cập nhật bản vá, vô hiệu hóa SMBv1, cấu hình tường lửa cổng 445 và phân đoạn mạng.
- Vì sao vấn đề quan trọng: SMBv1 vẫn còn tồn tại trong nhiều hệ thống mạng doanh nghiệp để tương thích thiết bị cũ; việc hiểu rõ bề mặt tấn công và phương pháp hardening đa tầng là yêu cầu cốt lõi trong bảo mật hạ tầng mạng.
- Khoảng trống ban đầu: Thực tế đánh giá an ninh thường đồng nhất việc "mở cổng 445" hoặc "bật SMBv1" với "tồn tại lỗ hổng MS17-010"; thiếu tiêu chí phân định rõ ràng giữa nhận diện dịch vụ và xác minh lỗ hổng thực tế; thiếu bảng đối chiếu trước - sau phòng thủ.

## Phạm vi

- Đối tượng nghiên cứu: Giao thức SMB (v1, v2, v3), nhóm lỗ hổng MS17-010 (trọng tâm CVE-2017-0144), công cụ kiểm thử (Kali Linux, Nmap, NSE script, Metasploit Framework) và các cơ chế phòng thủ Windows/Firewall.
- Phạm vi nội dung: Nghiên cứu lý thuyết nền tảng, cơ chế lỗ hổng, thiết kế kiến trúc lab cô lập, kịch bản kiểm thử bảo mật và quy trình phòng thủ đa tầng.
- Nội dung ngoài phạm vi: **Tránh các phần liên quan đến demo và kết quả demo thực tế theo chỉ thị của người dùng** ở giai đoạn hiện tại. Không tự tạo kết quả thực nghiệm hay log khai thác giả lập.
- Giới hạn đạo đức, pháp lý hoặc an toàn: Mọi hoạt động kiểm thử chỉ được thực hiện trong môi trường mạng ảo cô lập (Host-only / Internal Network) với cơ chế snapshot; nghiêm cấm quét hoặc khai thác ra mạng thực; tuân thủ quy tắc an toàn thông tin và chỉ thị của GVHD.

## Nguồn lực

- Notebook URL/ID: `[CẤU HÌNH CỤC BỘ — KHÔNG LƯU TRONG GIT]`
- Dữ liệu hiện có:
  - `work/do-an/inputs/ATTT_DACN_01_DeCuongChiTiet.docx` (Đề cương chi tiết đã duyệt)
  - `work/do-an/inputs/đề mục tham khảo.docx` (Đề mục tham khảo và bản nháp phần 1.1)
- Tài liệu bắt buộc:
  - Bản tin bảo mật Microsoft Security Bulletin MS17-010
  - Microsoft Learn: Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows
  - NVD: CVE-2017-0144 Detail
  - Nmap Official Guide & smb-vuln-ms17-010 NSE Script Documentation
  - Metasploit Framework Documentation
  - Windows Internals (Part 1 & Part 2, ấn bản 7)
- Mẫu văn bản thật của tác giả: `work/do-an/inputs/đề mục tham khảo.docx` (mục 1.1)
- Hồ sơ giọng tác giả: `work/do-an/AUTHOR_VOICE.md`
- Công cụ được phép: NotebookLM MCP, OfficeCLI, Nmap, Metasploit, VMware Workstation / VirtualBox.
- Quy định hoặc template áp dụng: `profiles/HUIT_2024.md` (Hồ sơ quy định trình bày Đồ án/Luận văn HUIT 2024).

## Yêu cầu đầu ra

- Độ dài dự kiến: Theo quy định Đồ án chuyên ngành HUIT (khoảng 40 - 70 trang tùy cấu trúc).
- Định dạng đầu ra: Markdown chuẩn và DOCX (xuất bản qua OfficeCLI).
- Chuẩn trích dẫn: IEEE số trong ngoặc vuông ([1], [2]...), danh mục tài liệu xếp theo thứ tự xuất hiện.
- Các sản phẩm phụ: Sơ đồ kiến trúc lab, bảng ma trận phân tích trước - sau phòng thủ, slide thuyết trình (khi hoàn thành).
- Cổng cần người dùng/GVHD phê duyệt: Toàn bộ từ `G0_INTAKE` đến `G6_PUBLICATION`.
