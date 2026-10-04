# Introduction Review

## Content
- **Word count**: 3,780 từ (nguồn Markdown `work/do-an/INTRODUCTION.md`), 3,757 từ (bản Word `work/do-an/outputs/MO_DAU_DO_AN.docx`).
- **Sections**: Đầy đủ 7 mục chính theo yêu cầu, đã sửa lỗi trùng số thứ tự mục 4 của đề cương tham khảo cũ:
  1. Lý do chọn đề tài
  2. Mục tiêu nghiên cứu (2.1. Mục tiêu tổng quát, 2.2. Mục tiêu kỹ thuật cụ thể)
  3. Đối tượng và phạm vi nghiên cứu (3.1. Đối tượng nghiên cứu, 3.2. Phạm vi nghiên cứu)
  4. Phương pháp tiếp cận và quy trình nghiên cứu (4.1. Phương pháp tiếp cận, 4.2. Quy trình nghiên cứu)
  5. Nguyên tắc an toàn và giới hạn kiểm thử (5.1. Cam kết đạo đức & pháp lý, 5.2. Cô lập mạng, 5.3. Kiểm soát tác động & snapshot, 5.4. Dừng kiểm thử khẩn cấp, 5.5. Giới hạn kiểm thử)
  6. Ý nghĩa khoa học và giá trị thực tiễn (6.1. Ý nghĩa khoa học, 6.2. Giá trị thực tiễn)
  7. Bố cục của báo cáo
  - Danh mục: TÀI LIỆU THAM KHẢO (chuẩn IEEE [1]–[6]).
- **Citation count**: 15 lượt trích dẫn trong nội dung, sử dụng 6 nguồn tài liệu chuẩn IEEE [1]–[6], sắp xếp tuần tự theo thứ tự xuất hiện đầu tiên:
  - [1] Microsoft Security Bulletin MS17-010 (S005, VERIFIED)
  - [2] NIST CVE-2017-0144 Detail (S011, VERIFIED)
  - [3] Microsoft Threat Intelligence WannaCrypt (S015, VERIFIED)
  - [4] Microsoft Learn Detect, enable, and disable SMBv1, SMBv2, and SMBv3 (S008, VERIFIED)
  - [5] NIST SP 800-115 Technical Guide to InfoSec Testing (S024, VERIFIED)
  - [6] NIST SP 800-41 Rev. 1 Guidelines on Firewalls (S025, VERIFIED)
  - *Ghi chú xung đột đánh số toàn cục*: Theo mục 3.6 của chỉ thị, ghi nhận sự khác biệt giữa đánh số cục bộ của phần Mở đầu độc lập [1]–[6] và số thứ tự nguồn trong Chương 1 (MS17-010 là [7]) và Chương 2 (MS17-010 là [5]) trước khi toàn bộ luận văn được hợp nhất danh mục tài liệu tham khảo chung. Không tự ý sửa đổi số trong các chương đã khóa.
- **Unsupported claim count**: 0. Tất cả các luận điểm kỹ thuật, ranh giới giao thức (Direct-hosted SMB TCP 445 vs. NBT TCP 139), cơ chế lỗi bộ nhớ nhân (`srv.sys`, `SrvOs2FeaListSizeToNt`, `SrvOs2FeaToNt`, Non-Paged Pool) đều dựa trên tài liệu chuẩn đã thẩm định.

## Author voice
- **Rules checked**:
  - Tuân thủ quy chuẩn học thuật tiếng Việt: không dùng đại từ nhân xưng phiếm chỉ, không sáo rỗng cảm tính, không quảng cáo thương mại.
  - Phân định chuẩn xác ba khái niệm: Bản tin an ninh MS17-010 (Security Bulletin của Microsoft), Lỗ hổng an ninh CVE-2017-0144 (Lỗ hổng tràn vùng đệm nhân), và Mã khai thác EternalBlue (Exploit tool vũ khí hóa).
  - Không đồng nhất cổng mở TCP 445 / bật SMBv1 với việc chắc chắn tồn tại lỗ hổng MS17-010.
  - Linter văn phong tiếng Việt học thuật (`lint_vi_academic.py`): Đạt 0 lỗi, 0 cảnh báo.
- **Remaining advisory warnings**: 0.

## Scope
- **Invented experimental results**: NO. Tuyệt đối không sáng tác kết quả demo, không giả mạo log quét mạng, không tạo screenshot giả hay số liệu đo lường chưa thực hiện.
- **Detailed lab/evidence/rollback section added**: NO. Không đưa các khối hướng dẫn quản lý lab chi tiết hoặc cấu hình rollback vào phần Mở đầu (các nội dung này dành riêng cho Chương 2 và Chương 3).
- **Safety outside Section 5**: NO. Toàn bộ các nguyên tắc an toàn, đạo đức nghề nghiệp, cô lập mạng, snapshot và dừng khẩn cấp được gom trọn vẹn và duy nhất trong Mục 5.

## Word QA
- **DOCX path**: `work/do-an/outputs/MO_DAU_DO_AN.docx`
- **DOCX validation result**: `Validation passed: no errors found` (`officecli validate`).
- **Heading audit**:
  - `Title`: 1 ("MỞ ĐẦU", 18pt bold, căn giữa, không có đường kẻ trang trí).
  - `Heading 1`: 8 mục (1., 2., 3., 4., 5., 6., 7. và TÀI LIỆU THAM KHẢO; 14pt bold, căn trái, `keep_with_next=True`).
  - `Heading 2`: 13 tiểu mục (2.1, 2.2, 3.1, 3.2, 4.1, 4.2, 5.1–5.5, 6.1, 6.2; 13pt bold, căn trái, `keep_with_next=True`).
  - Phân cấp mục đúng quy chuẩn Word heading styles, không dùng đoạn Normal in đậm giả heading.
- **Style consistency**:
  - Font chữ: 100% Times New Roman đồng nhất (195 run elements).
  - Cỡ chữ: 18pt (Title), 14pt (Heading 1), 13pt (Heading 2 & Normal body), 10pt (Footer page numbers).
  - Giãn dòng: 1.5 lines chuẩn HUIT 2024.
  - Giãn đoạn: Spacing Before 0pt, Spacing After 6pt (Normal body), Spacing After 4pt (Lists).
  - Căn lề: Căn đều hai bên (Justified) cho toàn bộ đoạn văn thân bài.
  - Thụt đầu dòng: 1.25 cm cho đoạn văn tiêu chuẩn; thụt lề treo (hanging indent) cho danh sách có thứ tự, danh sách gạch đầu dòng và tài liệu tham khảo.
  - Căn lề trang A4 chuẩn HUIT 2024: Trên 3.5 cm, Dưới 3.0 cm, Trái 3.5 cm, Phải 2.0 cm.
  - Màu sắc: Đen thuần túy (RGB 0, 0, 0), không dùng theme màu xanh/teal doanh nghiệp, không biểu tượng trang trí.
- **Page count**: 12 trang.

## Render QA
Đã kết xuất hình ảnh gốc (`--render native` qua Word trên Windows) và kiểm tra trực quan chi tiết từng trang:

| Page | Visual status | Issues found | Action |
|---|---|---|---|
| 1 | PASS | Phát hiện đường kẻ ngang màu xanh dưới tiêu đề "MỞ ĐẦU" sinh ra từ style Title mặc định của Word. | Đã loại bỏ hoàn toàn thuộc tính `pBdr` khỏi Title style và Title paragraph; tiêu đề "MỞ ĐẦU" hiện thuần đen, không đường kẻ trang trí. |
| 2 | PASS | Không phát hiện lỗi. Đoạn văn căn đều, thụt dòng 1.25cm chuẩn xác. Mục 2 và tiểu mục 2.1 hiển thị liền mạch với nội dung. | Giữ nguyên. |
| 3 | PASS | Không phát hiện lỗi. Mục 2.2 cùng danh sách mục tiêu kỹ thuật O1–O4 thụt lề treo chuẩn, in đậm tiêu đề con rõ ràng. | Giữ nguyên. |
| 4 | PASS | Không phát hiện lỗi. Mục 3 Đối tượng và phạm vi nghiên cứu, 3.1 và đầu 3.2 hiển thị cân đối. | Giữ nguyên. |
| 5 | PASS | Không phát hiện lỗi. Các điểm thuộc 3.2 (tiếp), Mục 4 Phương pháp tiếp cận và quy trình nghiên cứu, 4.1 hiển thị rõ ràng. | Giữ nguyên. |
| 6 | PASS | Không phát hiện lỗi. Kết thúc 4.1 và trọn vẹn Mục 4.2 Quy trình nghiên cứu 5 bước hiển thị đẹp mắt, không tràn dòng đơn độc. | Giữ nguyên. |
| 7 | PASS | Không phát hiện lỗi. Mục 5 Nguyên tắc an toàn và giới hạn kiểm thử, 5.1 và 5.2 hiển thị mạch lạc. | Giữ nguyên. |
| 8 | PASS | Tiểu mục 5.5 ở cuối trang chỉ có 1 dòng dẫn giải, các bullet bị đẩy sang trang 9. | Đã kích hoạt `keep_with_next=True` cho các dòng dẫn giải kết thúc bằng dấu hai chấm; Word đã tự động dời trọn vẹn tiểu mục 5.5 sang đầu trang 9, loại bỏ hoàn toàn hiện tượng heading/intro mồ côi. |
| 9 | PASS | Không phát hiện lỗi. Tiểu mục 5.5 hiển thị trọn vẹn ở đầu trang, tiếp nối là Mục 6 Ý nghĩa khoa học và giá trị thực tiễn cùng tiểu mục 6.1. | Giữ nguyên. |
| 10 | PASS | Không phát hiện lỗi. Tiểu mục 6.2 và đầu Mục 7 Bố cục của báo cáo hiển thị trang nhã, đúng phân cấp. | Giữ nguyên. |
| 11 | PASS | Không phát hiện lỗi. Phần còn lại của Mục 7 (các chương 1–4, Kết luận, Tài liệu tham khảo) kết thúc gọn gàng ở trang 11. | Giữ nguyên. |
| 12 | PASS | Mục TÀI LIỆU THAM KHẢO trước đó bị chia cắt khiến mục [3] bị đứt đoạn liên kết sang trang sau. | Đã cấu hình ngắt trang (`page_break_before=True`) cho tiêu đề TÀI LIỆU THAM KHẢO và `keep_together=True` cho từng mục tài liệu; toàn bộ 6 nguồn [1]–[6] hiển thị trọn vẹn, đẹp mắt trên trang 12. |

Tất cả 12 trang đều đã được thẩm định trực quan độc lập và xác nhận đạt yêu cầu chất lượng xuất bản học thuật.

## Final status
READY_FOR_INDEPENDENT_REVIEW
