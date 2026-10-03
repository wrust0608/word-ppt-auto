# Trạng thái dự án

- Cổng hiện tại: `G4_CHAPTERS / EVIDENCE_RECONCILIATION_AND_AUTHOR_REVIEW` (audit ngày 2026-10-04 đã mở lại điều kiện nguồn của Chương 1 và điều kiện xuất bản DOCX; các điểm PASS cũ chỉ còn giá trị lịch sử cho tới khi tái kiểm định đạt)
- Lần cập nhật: 2026-10-04
- Người/agent cập nhật: Codex
- Quyết định phê duyệt gần nhất: Tích hợp hệ thống giọng tác giả và kiểm soát văn phong mới nhưng bảo toàn toàn bộ quy định HUIT, dữ liệu và quyết định học thuật đã khóa; audit mới được phép mở lại trạng thái nguồn/DOCX khi bằng chứng thực tế mâu thuẫn với nhãn PASS cũ.

## Artifact hiện có

| Artifact | Trạng thái | Đường dẫn | Ghi chú |
|---|---|---|---|
| PROJECT_PROFILE | LOCKED | work/do-an/PROJECT_PROFILE.md | Đã khóa toàn diện (G0) |
| INSTITUTION_PROFILE | LOCKED | work/do-an/INSTITUTION_PROFILE.md | Đã khóa chuẩn HUIT 2024 (G0) |
| AUTHOR_VOICE | LOCKED | work/do-an/AUTHOR_VOICE.md | Đã khóa hồ sơ giọng tác giả (G0) |
| RESEARCH_MAP | LOCKED | work/do-an/RESEARCH_MAP.md | Đã khóa 4 RQ, 4 Mục tiêu và phương pháp luận (G1) |
| SOURCE_LEDGER | REOPENED_RECHECK | work/do-an/SOURCE_LEDGER.md | Đã đối soát NotebookLM; có nguồn bổ sung S020-S026 và một nhóm nguồn cũ cần nhập lại/thay thế |
| ARGUMENT_MAP | LOCKED | work/do-an/ARGUMENT_MAP.md | Đã khóa chuỗi lập luận C001 - C006 (G3) |
| CLAIM_MATRIX | REOPENED_RECHECK | work/do-an/CLAIM_MATRIX.md | Sáu luận điểm trung tâm đã chuyển sang nguồn khả dụng; cần đồng bộ bibliography Chương 1 |
| OUTLINE | LOCKED | work/do-an/OUTLINE.md | Đã khóa cấu trúc 4 chương, ngân sách từ (G3) |
| CHAPTER_ARGUMENT | LOCKED | work/do-an/CHAPTER_ARGUMENT.md | Đã cập nhật toàn diện Hợp đồng Chương 2 theo mô hình Causal-Chain và Enterprise Topology |
| CHAPTER_1 | LEGACY_PASS_REOPENED | work/do-an/CHAPTER_1.md | Citation khép kín về hình thức nhưng một nhóm nguồn chưa khả dụng trong NotebookLM; xem PILOT_CHAPTER_REVIEW.md |
| CHAPTER_2 | READY_FOR_APPROVAL | work/do-an/CHAPTER_2.md | **Bản thảo Chương 2 hoàn thiện sau tự phản biện theo mô hình Causal-Chain** (413 dòng, 4 bảng, 3 sơ đồ ASCII, 9 trích dẫn IEEE xuất hiện tuần tự 100%, Điểm: 9.5/10 PASS) |
| REVIEW_REPORT | PASS | work/do-an/REVIEW_REPORT.md | Báo cáo đánh giá Chương 2 theo mô hình Causal-Chain & 5 điểm tự hoàn thiện (Điểm: 9.5/10 PASS) |
| STYLE_REVIEW | OPEN | work/do-an/STYLE_REVIEW.md | Audit di chuyển: Chương 1 có 18 và Chương 2 có 14 cảnh báo cần phân loại trước G5/G6; không có rule sáo ngữ `VI001–VI010` |
| AUTHOR_VOICE_CALIBRATION | READY_FOR_AUTHOR_REVIEW | work/do-an/AUTHOR_VOICE_CALIBRATION.md | Chờ tác giả sửa/xác nhận tối thiểu ba cách diễn đạt trước khi khóa giọng |
| ROADMAP_2_6 | ACTIVE | work/do-an/ROADMAP_2_6.md | Bước 2 xong; bước 3 còn recheck; bước 4 chờ người dùng; bước 5-6 đã audit nhưng chưa qua cổng |
| PILOT_CHAPTER_REVIEW | FIX_REQUIRED | work/do-an/PILOT_CHAPTER_REVIEW.md | Ghi lỗi nguồn, bibliography và 18 cảnh báo văn phong của Chương 1 |
| DOCX_QA_REPORT | REBUILD_REQUIRED | work/do-an/DOCX_QA_REPORT.md | DOCX cũ validation đạt nhưng chưa publication-ready; cần sinh lại từ Markdown đã duyệt |
| PUBLICATION_CHECKLIST | BLOCKED | work/do-an/PUBLICATION_CHECKLIST.md | Chờ nguồn, giọng tác giả, chương mẫu và render từng trang |

## Quyết định đã khóa

| ID | Quyết định | Người duyệt | Ngày |
|---|---|---|---|
| DEC-01 | Sử dụng NotebookLM notebook được chỉ định trong cấu hình cục bộ (ID không lưu trong Git) | Người dùng | 2026-09-12 |
| DEC-02 | Hoàn tất cấu hình môi trường NotebookLM MCP và OfficeCLI | Hệ thống | 2026-09-12 |
| DEC-03 | **Ràng buộc phạm vi**: Tránh các phần liên quan đến demo và kết quả demo thực tế ở giai đoạn hiện tại theo yêu cầu của tác giả | Người dùng | 2026-09-12 |
| DEC-04 | Chuẩn trích dẫn: IEEE số trong ngoặc vuông, xếp theo thứ tự xuất hiện | Đề cương chi tiết | 2026-09-12 |
| DEC-05 | **Phê duyệt cổng G0_INTAKE**: Khóa toàn diện hồ sơ dự án, quy chế đào tạo HUIT và giọng tác giả | Người dùng | 2026-09-12 |
| DEC-06 | **Phê duyệt cổng G1_RESEARCH_DESIGN**: Khóa bản đồ nghiên cứu 4 RQ và 4 Mục tiêu | Người dùng | 2026-09-12 |
| DEC-07 | **Khóa cổng G2_EVIDENCE**: Khóa sổ nguồn tài liệu chính thống | Hệ thống | 2026-09-12 |
| DEC-08 | **Phê duyệt cổng G3_ARGUMENT**: Khóa bản đồ lập luận, claim matrix và đề cương chi tiết | Người dùng | 2026-09-12 |
| DEC-09 | **Phê duyệt Hợp đồng Chương 1**: Khóa phạm vi ban đầu của Chương 1 | Người dùng | 2026-09-12 |
| DEC-10 | **Tiếp thu Báo cáo phản biện Chương 1**: Tinh giản 40% dung lượng, tập trung vào thực nghiệm lab và lý thuyết phòng thủ | Người dùng / Hệ thống | 2026-09-12 |
| DEC-11 | **Chuẩn hóa kỹ thuật v2.1**: Tách bảng KB theo hệ điều hành, phân định dialect SMBv3 và sơ bộ mã NT Status | Hệ thống | 2026-09-12 |
| DEC-12 | **Chuẩn hóa toàn diện Chương 1 v3.0 đạt ngưỡng 9/10**: Chuẩn hóa mã lỗi Nmap NSE, root cause FEA, phân định dialect SMB 3.0/3.1.1, phân biệt -sV và Cấp độ 1, gỡ bỏ từ ngữ AI | Người dùng / Hệ thống | 2026-09-12 |
| DEC-13 | **Xử lý Báo cáo phản biện Vòng 4 (v3.1)**: Chuẩn hóa Bảng 1.2 CVE, bảng KB, Rapid7 module, nguồn kiểm toán | Người dùng / Hệ thống | 2026-09-12 |
| DEC-14 | **Tiếp thu Báo cáo thẩm định Vòng 5, nâng chuẩn chính thức Chương 1 đạt 9.0/10 PASS**: Khóa 19 tài liệu tham khảo IEEE xuất hiện tuần tự [1]–[19]; xóa bài báo chưa xác minh, thay bằng CISA TA17-132A và Microsoft Threat Intelligence; trỏ chính xác module Rapid7 và source NSE; bổ sung nguồn Microsoft SMB security, Direct-host SMB, MSRC Eternal Synergy và Microsoft Petya Blog; sửa lối nói Stop-and-wait và mở đầu CIA | Người dùng / Hệ thống | 2026-09-12 |
| DEC-15 | **Khóa hoàn tất Chương 1 (PASS 9.0/10) và phê duyệt Hợp đồng Chương 2**: Phê duyệt hợp đồng Chương 2 bám sát RQ3, Mục tiêu O3 và Đề cương chi tiết HUIT | Người dùng / Hệ thống | 2026-09-12 |
| DEC-16 | **Hoàn thành bản thảo ban đầu Chương 2**: Soạn thảo bản thảo sơ bộ Chương 2 | Hệ thống | 2026-09-12 |
| DEC-17 | **Tái cấu trúc toàn diện Chương 2 theo mô hình Causal-Chain và Enterprise Topology (PASS 9.2/10)**: Xóa bỏ topology flat Host-only, thiết lập mạng doanh nghiệp 3 VLAN qua Tường lửa/UTM định tuyến liên VLAN duy nhất, Core Switch L2 thuần túy; mô hình hóa đường tấn công $(R, S, D, V, E, C)$; chuẩn hóa máy trạng thái đơn biến 4 nấc snapshot ($S_0 \to S_1 \to S_2 \to S_3$) trên cùng một Windows 7 target; bổ sung trạm Client VLAN 30 làm đối chứng nghiệp vụ dương tính; bạch hộp hóa 5 kỹ thuật theo cấu trúc 10 mục; siết chặt tiêu chí Cấp 4 (BSOD/Crash tính là FAIL); thiết kế Ma trận bằng chứng gán nhãn `[CẦN DỮ LIỆU]`; xóa sạch từ ngữ tuyệt đối hóa; chuẩn hóa 9 trích dẫn IEEE tuần tự 100% | Người dùng / Hệ thống | 2026-09-12 |
| DEC-18 | **Hoàn tất tinh chỉnh 5 điểm kỹ thuật sâu sau tự phản biện (PASS 9.5/10)**: (1) Phân định rõ ràng góc nhìn trạm kiểm thử (Attacker Vantage Point) vs. trạng thái nội tại máy chủ (Server Internal State) tại Bảng 2.2 ($S_3$); (2) Quy định rõ chính sách Firewall hai chiều Ingress/Egress cho kênh kết nối ngược ($C$); (3) Bổ sung cơ sở học thuật của chuỗi 4 trạng thái theo Hardening Lifecycle vs. không gian tổ hợp $2^3 = 8$; (4) Làm rõ cơ sở kỹ thuật bắt buộc của các tham số an toàn `--script-args unsafe=0` và `set MaxExploitAttempts 1` chống hỏng kernel pool; (5) Rà soát và loại bỏ sạch sẽ các từ ngữ tuyệt đối hóa cuối cùng ("bẻ gãy hoàn toàn" $\to$ "loại bỏ khả năng / bị bẻ gãy có kiểm chứng trên thực tế") | Người dùng / Hệ thống | 2026-09-12 |
| DEC-19 | **Biên dịch và kiểm định thành công Báo cáo Word hoàn chỉnh Chương 1 và 2 (`BAO_CAO_DO_AN_CHUONG_1_2.docx`)**: Tạo tài liệu Word chuẩn quy chế HUIT 2024 (Khổ A4, lề Trên 3.5cm, Dưới 3.0cm, Trái 3.5cm, Phải 2.0cm, font Times New Roman, dãn dòng 1.3, Trang bìa chính quy HUIT, Mục lục tổng quát, Danh mục từ viết tắt, Danh mục bảng biểu, Danh mục hình vẽ & sơ đồ, toàn văn Chương 1 v3.2 và Chương 2 v2.0, 9 bảng biểu chuẩn hóa, 7 sơ đồ ASCII đóng hộp, trích dẫn IEEE tuần tự). Đã kiểm định OpenXML schema qua `officecli validate` đạt chuẩn tuyệt đối không có lỗi | Người dùng / Hệ thống | 2026-09-12 |
| DEC-20 | **Di chuyển sang hệ thống kiểm soát văn phong và Word mới**: giữ nguyên thứ tự ưu tiên quy định HUIT → quyết định đã khóa → bằng chứng → lập luận → giọng tác giả → linter; không tối ưu theo AI detector hoặc điểm tự chấm; không tự sửa chương đã khóa | Người dùng / Codex | 2026-10-04 |
| DEC-21 | **Mở lại có kiểm soát trạng thái nguồn, Chương 1 và DOCX sau audit thực tế**: Notebook từng có 0 nguồn dù ledger cũ ghi có; sau nạp lại có 19 nguồn dùng được nhưng một nhóm nguồn cũ vẫn cần recheck. Chương 1 giữ lịch sử PASS nhưng chưa qua cổng nguồn mới. DOCX giữ lịch sử OpenXML PASS nhưng chưa đạt xuất bản vì thiếu TOC tự động, nhiều định dạng trực tiếp/cảnh báo và chưa xem riêng từng trang. Không xóa các quyết định cũ; dùng báo cáo audit để xác định việc phải sửa. | Codex | 2026-10-04 |

## Nguồn tài liệu

| Source ID | Trạng thái | Ghi chú |
|---|---|---|
| S001, S003, S004, S009, S016, S019 | RECHECK/NO | Chưa có toàn văn hợp lệ trong NotebookLM; phải nhập lại hoặc thay bằng nguồn khả dụng trước khi dùng. |
| S014 | RECHECK/ERROR | URL CISA cũ không nhập được; cần nguồn thay thế còn truy cập được. |
| S006 | VERIFIED/YES | Đã chuyển sang URL Microsoft Learn hiện hành. |
| S002, S005, S007, S008, S010-S013, S015, S017, S018, S020-S026 | VERIFIED/YES | Nguồn khả dụng đã được nhập/đối soát; xem metadata chi tiết trong SOURCE_LEDGER.md. |

## Vấn đề còn mở

| ID | Nhãn | Mô tả | Ảnh hưởng | Hành động tiếp theo |
|---|---|---|---|---|
| ISS-01 | `[CẦN DỮ LIỆU]` | Dữ liệu log, ảnh chụp màn hình và kết quả chạy demo thực nghiệm lab | Các phần thực nghiệm (Chương 2, 3, 4) chưa ghi nhận kết quả chạy thật | Duy trì nhãn `[CẦN DỮ LIỆU]`, tập trung vào kiến trúc lab, tham số an toàn và kịch bản chuẩn hóa |
| ISS-02 | `STYLE_REVIEW_OPEN` | 32 cảnh báo tư vấn về nhịp câu và mở đoạn trong Chương 1–2 | Chưa đủ điều kiện tuyên bố kiểm tra văn phong G5/G6 theo hệ thống mới | Phân loại từng cảnh báo, duyệt diff, chạy publication lint và sinh lại DOCX trước lần bàn giao kế tiếp |
| ISS-03 | `[CẦN NGUỒN]` | Bibliography Chương 1 còn sử dụng các nguồn `[1]`, `[3]`, `[4]`, `[9]`, `[14]`, `[16]`, `[19]` chưa khả dụng; `[6]` dùng URL cũ | Chương 1 chưa thể qua cổng bằng chứng dù đánh số IEEE đúng | Lập bảng ánh xạ nguồn cũ sang nguồn Notebook hiện hành; nhập/thay nguồn rồi kiểm tra lại từng luận điểm |
| ISS-04 | `[CẦN TÁC GIẢ XÁC NHẬN]` | Mẫu hiệu chỉnh giọng đã tạo nhưng chưa có sửa đổi/xác nhận trực tiếp của tác giả | Không được khóa bước 4 hoặc áp giọng cá nhân lên toàn chương | Yêu cầu tác giả sửa/xác nhận tối thiểu ba cách diễn đạt trong AUTHOR_VOICE_CALIBRATION.md |
| ISS-05 | `DOCX_REBUILD_REQUIRED` | DOCX cũ thiếu TOC field, có nhiều direct formatting, 323 cảnh báo OfficeCLI; đã render/xem đủ 53 trang và phát hiện lỗi công thức, bảng/sơ đồ, mục lục | Không đủ điều kiện gắn nhãn publication-ready | Sau khi Markdown được duyệt, sinh DOCX mới và thực hiện vòng render, xem từng trang, sửa và render lại |

## Bước tiếp theo duy nhất

Trình người dùng `AUTHOR_VOICE_CALIBRATION.md` và yêu cầu họ sửa hoặc xác nhận tối thiểu ba cách diễn đạt. Sau khi được duyệt, cập nhật `AUTHOR_VOICE.md`, đối soát/thay các nguồn Chương 1 còn lỗi, xử lý có kiểm soát 18 cảnh báo của chương mẫu và chạy lại citation audit/style lint trước khi xin duyệt chương. Chưa viết Chương 3 và chưa sinh lại DOCX trong khi cổng này còn mở.


## Hoàn tất audit tiếp quản 2026-10-04

- Đã đồng bộ commit bàn giao b81dae1; không sửa nội dung chương hoặc DOCX.
- Bước 6: `AUDIT_COMPLETE_REBUILD_REQUIRED`. Đã render native và xem riêng đủ 53 trang, lưu lỗi theo trang trong DOCX_QA_REPORT.md. Đây là hoàn tất audit bản cũ, không phải hoàn tất G6.
- Đính chính font: TNR chiếm phần lớn khi tính kế thừa style (82.879 ký tự), Consolas 13.892, Cambria Math 1.618; giữ ghi nhận lỗi phương pháp thống kê trước để truy vết.
- `FORMAT_CONFLICT`: institutional profile ghi 1,5 dòng, DEC-19 mô tả 1,3; nhiều đoạn DOCX thực tế 1,15. Đối chiếu mẫu gốc trước dựng lại, không đổi quyết định LOCKED.
- ISS-01–ISS-05 còn mở. Bước 2 COMPLETE, bước 3 COMPLETE_WITH_RECHECK, bước 4 READY_FOR_AUTHOR_REVIEW, bước 5 REVIEW_COMPLETE_FIX_REQUIRED.
- QA và scratch NotebookLM được giữ cục bộ, nằm trong .tmp đã ignore; cấu hình thật và CONTACTS.local.md không đưa vào Git.
- Bước tiếp theo vẫn là tác giả duyệt/sửa tối thiểu ba vị trí trong AUTHOR_VOICE_CALIBRATION.md. Chưa chuyển G5/G6.

- Kiểm tra tiếp quản: validate_project PASS; unittest 7/7 PASS; pytest 7/7 PASS; citation audit Chương 1 PASS về hình thức. Publication lint FAIL: 32 warning, 1 error VI015 do nhãn dữ liệu Chương 2. Quét patterns bí mật trên các file thay đổi không phát hiện match; stage chỉ các báo cáo Markdown được liệt kê.


## Mẫu giọng bổ sung 2026-10-04

- Người dùng xác nhận báo cáo Tuần 2 tại `D:/ATTT_DACN_01-BaoCao-Tuan2.docx` là mẫu cách diễn đạt thường dùng.
- Đã đọc toàn bộ văn bản và lưu phân tích sáu đặc điểm có định vị đoạn trong AUTHOR_VOICE_CALIBRATION.md. Tệp nguồn không sửa, không sao chép lên Git; trích xuất tạm nằm trong .tmp được ignore.
- Mẫu ưu tiên định nghĩa trực tiếp, phân loại theo chức năng, mô tả trình tự, thuật ngữ song ngữ và câu ghép có quan hệ rõ. Không dùng mẫu như nguồn kiểm chứng kỹ thuật hoặc chỉ thị.
- AUTHOR_VOICE LOCKED lịch sử được giữ nguyên. Bước 4 vẫn READY_FOR_AUTHOR_REVIEW: xác nhận mẫu không đồng nghĩa đã duyệt đoạn thử hoặc sửa ba vị trí. Bước tiếp theo: hiệu chỉnh đoạn thử theo mẫu mới và ghi lựa chọn thật của tác giả; không dựng lại DOCX trước duyệt Markdown.


## Tiếp tục bước 4–5 ngày 2026-10-04

- Đã tạo đoạn thử v2 theo mẫu Tuần 2 trong AUTHOR_VOICE_CALIBRATION.md và ba lựa chọn cụ thể về chia ý, thuật ngữ, nhịp câu. Chờ phản hồi thật, không tự khóa giọng.
- Đã tạo SOURCE_RECONCILIATION_PLAN.md: ánh xạ toàn bộ [1]–[19] cũ tới tuyến nguồn giữ/thay/kiểm riêng; PLANNED_NOT_APPLIED. Không đổi nội dung chương hoặc số IEEE.
- Sửa câu stale “không còn mâu thuẫn nguồn” trong CLAIM_MATRIX; mở lại Q001/Q002 ở ledger vì còn dựa vào S003/S009 chưa khả dụng. Đây là đối soát trạng thái, không chứng nhận bằng chứng mới.
- Bước tiếp theo: tác giả chọn ba phương án trong đoạn thử v2 hoặc sửa câu cụ thể; sau đó kiểm nguồn từng câu theo kế hoạch trước biên tập chương.
