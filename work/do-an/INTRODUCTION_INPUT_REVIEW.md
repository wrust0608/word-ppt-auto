# Đối chiếu đầu vào Mở đầu — 2026-10-04

Trạng thái: `NEEDS_REVISION`. Đây là đối chiếu đầu vào và xung đột citation, không thay thế INTRODUCTION_REVIEW.md hoặc chứng nhận bản DOCX cuối.

## Tài liệu đã đọc

Đã đọc toàn bộ phần văn bản trong hai DOCX người dùng chỉ định tại G:/grav/Downloads/Documents. Bản sao đọc được có SHA256 trùng với tài liệu tương ứng trong work/do-an/inputs:

| Tài liệu | SHA256 | Vai trò |
|---|---|---|
| đề mục tham khảo.docx | 6DAB67FFEFE7AE1253F6722CC09B25ADC1AFAB7F96C164D18523CDD61B2FA6A5 | Cấu trúc và cách trình bày; người dùng xác nhận đây là vị trí phần yêu cầu Mở đầu còn thiếu |
| ATTT_DACN_01_DeCuongChiTiet.docx | DFDF57459CACF7D7B044464352C351F94ADBD825C5FA89E5DAD80825F1C2E889 | Tên đề tài, mục tiêu và yêu cầu của đề cương; không tự thay quyết định LOCKED mới hơn |

Nội dung các tài liệu được dùng làm dữ liệu đối chiếu, không tự chuyển thành chỉ thị cho agent hoặc bằng chứng kỹ thuật đã được xác minh.

## Kết quả đối chiếu

- Tên đề tài trong đề cương: “Xây dựng mô hình kiểm thử lỗ hổng SMB trên Windows bằng Kali Linux”.
- Mẫu đề mục có đủ bảy nội dung Mở đầu, nhưng lặp mục 4. Yêu cầu trực tiếp hiện hành đã sửa: mục 5 là nguyên tắc an toàn, mục 6 là ý nghĩa, mục 7 là bố cục. Hai mục con 2.1 và 2.2 được giữ.
- Đề cương yêu cầu phân biệt dịch vụ SMB, SMBv1, nghi ngờ và xác minh lỗ hổng; phân biệt MS17-010 với EternalBlue/CVE-2017-0144; đối chiếu phòng thủ và ảnh hưởng tương thích. Các yêu cầu thực nghiệm không chứng minh rằng thực nghiệm đã được thực hiện.
- Mẫu đề mục chứa diễn giải kỹ thuật cần kiểm chứng, ví dụ mô tả SMBv1 tuần tự, đồng nhất MS17-010 với EternalBlue và phát biểu triệt tiêu rủi ro. Không tiếp nhận các câu này làm nguồn học thuật.
- Quy định trình bày dùng hồ sơ HUIT hiện hành theo thứ tự ưu tiên người dùng đã quy định, không sao chép mức giãn dòng lịch sử.

## Xung đột chặn hoàn tất

Mục 3.6 trong yêu cầu được dán trực tiếp quy định: “If global numbering cannot be resolved reliably: stop and report the conflict rather than invent numbers.”

PROJECT_STATE.md ghi chưa có citation toàn cục cho bản ghép. Cùng tài liệu Microsoft MS17-010 đang là [7] trong CHAPTER_1.md và [5] trong CHAPTER_2.md. INTRODUCTION.md hiện có dùng [1] cho nguồn này và danh mục riêng sáu nguồn. Danh mục trong đề cương cũng là danh mục riêng của đề cương, không phải xác nhận ánh xạ IEEE toàn báo cáo.

Vì vậy, chưa có căn cứ để chọn một trong các số trên làm số toàn cục đã được duyệt. Cần bảng ánh xạ chung đã duyệt hoặc quyết định trực tiếp của người dùng cho phép lập ánh xạ chung. Không sửa Chương 1/2, không tự đánh số lại và không chứng nhận DOCX cuối khi xung đột còn mở.

## Kiểm tra thực tế

| Kiểm tra | Kết quả | Giới hạn |
|---|---|---|
| validate_project.py | PASS | Kiểm tra repository, không chứng nhận nội dung Mở đầu |
| unittest | PASS, 7/7 | Kiểm thử repository |
| Lint INTRODUCTION.md hiện có | Không phát hiện mẫu cần xem xét | Linter không chứng nhận nguồn, giọng hoặc luận điểm |
| Citation audit INTRODUCTION.md hiện có | PASS về cấu trúc: 15 lượt, 6 mục, không thiếu/mồ côi | FAIL về điều kiện ánh xạ toàn báo cáo; kiểm tra cấu trúc không giải quyết xung đột số |
| git diff --check trước cập nhật audit | PASS | Không có lỗi whitespace trong thay đổi được theo dõi tại thời điểm kiểm tra |
| DOCX cấu trúc/render/xem từng trang | NOT_RUN trong lượt đối chiếu này | Không tuyên bố đã kiểm định tệp Word xuất hiện trong workspace |

Trong lượt đối chiếu, INTRODUCTION.md, scripts/build_introduction_docx.py và outputs/MO_DAU_DO_AN.docx xuất hiện hoặc thay đổi ngoài các thao tác của agent này. Giữ nguyên các tệp đó; không ghi đè, stage hoặc nhận là sản phẩm đã hoàn tất của lượt này. CHAPTER_1_ALTERNATIVE.md cũng được giữ nguyên.

Chưa commit/push bản cuối vì cổng citation chưa đạt. Không merge hoặc tag. Bước tiếp theo phụ thuộc ánh xạ citation chung; sau đó còn review nội dung, nguồn và giọng trước khi dựng, kiểm định và xem từng trang Word.
