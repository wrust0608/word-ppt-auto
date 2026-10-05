# Hồ sơ dự án

Trạng thái: `LOCKED_CANONICAL_2026_10_05`

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
- Thời gian thực hiện: 24/08/2026 - 18/10/2026. Khác biệt cách gọi số tuần giữa hồ sơ lịch sử và thông báo HUIT được theo dõi trong `REQUIREMENT_RECONCILIATION.md`.

## Vấn đề nghiên cứu

- SMB là giao thức chia sẻ tài nguyên quan trọng trong hệ sinh thái Windows; SMBv1 và nhóm lỗ hổng MS17-010 tạo ra bề mặt rủi ro đáng kể trên hệ thống chưa được hardening.
- Đề tài cần phân biệt rõ bốn lớp: khả năng tiếp cận dịch vụ, trạng thái giao thức, tín hiệu phát hiện từ xa và trạng thái bản vá cục bộ.
- Đề tài xây dựng lab cô lập, thực hiện khảo sát Nmap/NSE có kiểm soát, đối chiếu ground truth cục bộ và đánh giá các lớp giảm thiểu.

## Phạm vi

- Đối tượng nghiên cứu: SMBv1/v2/v3; TCP 139/445; MS17-010 với trọng tâm CVE-2017-0144/EternalBlue; Kali Linux; Nmap/NSE; vai trò của Metasploit; Windows hardening và firewall/network access control.
- Nền tảng thực nghiệm canonical: **Oracle VM VirtualBox**.
- Máy kiểm thử canonical: Kali Linux.
- Máy mục tiêu canonical: Windows Server 2012 R2 Standard Evaluation, Build 9600.
- Mạng baseline canonical: VirtualBox Host-Only, cô lập khỏi Bridged/NAT tại thời điểm pre-demo đã khóa.
- Thực nghiệm canonical hiện có:
  1. Scenario 1 — Nmap SMB 139/445.
  2. Scenario 2 — NSE SMB / MS17-010.
  3. Case B — Vô hiệu hóa SMBv1 và retest.
  4. Case C — pfSense Transparent Bridge chặn TCP 139/445 và retest.
- Trạng thái bản vá baseline canonical: `UNPATCHED` theo local ground truth đã đối chiếu.
- Remote `smb-vuln-ms17-010` canonical: `UNKNOWN / NO USABLE SCRIPT RESULT`.
- Case A patch trong báo cáo lịch sử **không phải canonical result** nếu chưa phục hồi và audit evidence riêng.
- Metasploit nằm trong phạm vi nghiên cứu công cụ/phương pháp, nhưng không có canonical exploit/RCE result trong evidence hiện hành.

## Ngoài phạm vi kết quả

- Không tuyên bố exploit success, RCE, SYSTEM, Meterpreter, reverse shell hoặc BSOD như kết quả canonical khi không có evidence.
- Không quét hoặc khai thác hệ thống ngoài lab được cấp phép.
- Không dùng kết quả lịch sử để lấp khoảng trống raw evidence hiện hành.
- Không định lượng performance/CPU/memory/Event Viewer nếu chưa có artifact đo tương ứng.

## Nguồn lực và evidence

- Notebook URL/ID: `[CẤU HÌNH CỤC BỘ — KHÔNG LƯU TRONG GIT]`.
- Đề cương chi tiết và hai kịch bản giảng viên là nguồn kỹ thuật/định hướng ưu tiên.
- `EXPERIMENTAL_TRUTH_MATRIX.md`: canonical truth gate cho Chương 2–4.
- `EVIDENCE_REGISTER.md`: stable Evidence IDs.
- `CANONICAL_EVIDENCE_SHA256.txt`: checksum của core canonical evidence set.
- `NEGATIVE_RESULT_POLICY.md`: quy tắc UNKNOWN/NO OUTPUT/FILTERED.
- Báo cáo thực nghiệm cũ: `HISTORICAL_REFERENCE`.

## Tài liệu nền bắt buộc

- Microsoft Security Bulletin MS17-010.
- Microsoft Learn về SMBv1/v2/v3 và SMB security.
- NVD cho CVE trọng tâm.
- Nmap Official Guide và NSE documentation/source.
- NIST SP 800-115 và NIST firewall guidance phù hợp.
- Rapid7/Metasploit documentation khi mô tả vai trò công cụ.

## Yêu cầu đầu ra

- Báo cáo Markdown canonical và DOCX theo chuẩn HUIT.
- Trích dẫn IEEE theo thứ tự xuất hiện.
- Sơ đồ lab, bảng trước-sau, evidence map, phụ lục kỹ thuật có chọn lọc.
- Slide bảo vệ, Q&A bank, demo runbook, rollback plan và evidence quick-index.
- Gate dự án: G0–G6 của repo + `G7_DEFENSE` trong Execution Plan hiện hành.

## Quy tắc điều phối

Khi có mâu thuẫn: yêu cầu trực tiếp hiện tại > HUIT/đề cương > quyết định canonical hiện hành > evidence đã xác minh > quy trình repo > author voice. Mọi thay đổi scope hoặc mở lại artifact LOCKED phải qua `CHANGE_CONTROL.md`.
