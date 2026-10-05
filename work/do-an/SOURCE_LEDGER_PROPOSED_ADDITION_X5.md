# ĐỀ XUẤT BỔ SUNG NGUỒN VÀO SỔ NGUỒN — X5 STRUCTURAL REWRITE

Trạng thái: `PROPOSED_FOR_CHANGE_CONTROL`
Ngày lập: 2026-10-05
Agent: Executor / Writing Agent
Phạm vi: Đề xuất bổ sung tài liệu kỹ thuật hỗ trợ ngưỡng phiên bản tệp driver `srv.sys` phục vụ Chương 2 và Chương 3.

---

## 1. Thông tin nguồn đề xuất

| Thuộc tính | Chi tiết |
| :--- | :--- |
| **Mã đề xuất (Proposed ID)** | `S032` (hoặc định danh theo quyết định của External Reviewer) |
| **Tác giả / Cơ quan xuất bản** | Microsoft Support |
| **Năm xuất bản / Cập nhật** | 2017 (Cập nhật lưu trữ Microsoft Support) |
| **Tiêu đề tài liệu** | How to verify that MS17-010 is installed |
| **Loại tài liệu** | Hướng dẫn kỹ thuật hỗ trợ chính thức (Official Support Article / Verification Guide) |
| **Mã định danh tài liệu** | Article ID: 4023057 |
| **Đường dẫn URL** | `https://support.microsoft.com/en-us/help/4023057/how-to-verify-that-ms17-010-is-installed` |
| **Trạng thái đối soát** | `CANDIDATE_FOR_VERIFICATION` |

---

## 2. Luận điểm và dữ kiện kỹ thuật được hỗ trợ

1. **Xác thực ngưỡng phiên bản số của tệp driver `srv.sys` trên Windows Server 2012 R2:**
   Tài liệu cung cấp bảng đối chiếu chính thức giữa các gói cập nhật MS17-010 và số hiệu phiên bản nhị phân tối thiểu của tệp driver hạt nhân `srv.sys` cho từng phiên bản hệ điều hành Windows. Cụ thể đối với Windows Server 2012 R2:
   - Phiên bản unpatched gốc (RTM): `srv.sys` có số hiệu `6.3.9600.16421`.
   - Ngưỡng phiên bản đã được vá an toàn (patched threshold): `srv.sys >= 6.3.9600.18604`.

2. **Hỗ trợ phương pháp kiểm tra trạng thái bản vá nội bộ (Local Patch State):**
   Cung cấp cơ sở chính thức cho việc sử dụng lệnh PowerShell kiểm tra thuộc tính tệp `srv.sys` kết hợp đối soát mã cập nhật (`Get-HotFix`), độc lập hoàn toàn với kết quả rà quét từ xa qua mạng.

---

## 3. Lý do kỹ thuật cần bổ sung

- **Khoảng trống của nguồn hiện hành:** Security Bulletin MS17-010 (`S005` trong `SOURCE_LEDGER.md`) chỉ liệt kê danh mục CVE và các mã Knowledge Base tổng thể (KB4012213, KB4012216), nhưng không trình bày bảng chi tiết số hiệu phiên bản nhị phân (file version / binary build) của các driver thành phần.
- **Tính chuẩn xác của Experimental Truth Matrix:** Ma trận sự thật thực nghiệm canonical của đề tài (`EXPERIMENTAL_TRUTH_MATRIX.md`) đã khóa dữ kiện `srv.sys 6.3.9600.16421 < 6.3.9600.18604` làm căn cứ phân định trạng thái `UNPATCHED`. Việc bổ sung tài liệu hỗ trợ này giúp khép kín chuỗi truy vết từ quy định ma trận đến tài liệu sơ cấp của nhà sản xuất hệ điều hành.

---

## 4. Vị trí sử dụng trong Chương 2

- **Mục 2.2.5 (Baseline bản vá MS17-010 và snapshot):** Cung cấp căn cứ đối chiếu cho nhận định tệp driver `srv.sys` tại đường dẫn `C:\Windows\System32\drivers\srv.sys` có số hiệu `6.3.9600.16421` thấp hơn ngưỡng an toàn `6.3.9600.18604`.
- **Mục 2.6.4 (Vai trò của cập nhật bản vá):** Hỗ trợ lập luận về cơ chế khắc phục lỗ hổng mức nhân thông qua việc thay thế tệp nhị phân driver.
- **Mục 2.7.3 (Remote vulnerability signal và local patch state):** Cung cấp tiêu chí phân định hai trục độc lập trong khung đối soát bằng chứng giữa tín hiệu quét từ xa và trạng thái hệ điều hành nội bộ.

---

## 5. Kiến nghị quản trị

- Kính trình External Reviewer xem xét và đưa vào quy trình Change Control cập nhật `SOURCE_LEDGER.md` tại thời điểm phù hợp.
- Trong bản nháp Chương 2 hiện tại, trích dẫn được đánh số theo thứ tự xuất hiện tuần tự là `[5]` mà không tự ý sửa đổi file khóa `SOURCE_LEDGER.md`.
