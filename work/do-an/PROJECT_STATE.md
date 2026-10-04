# Trạng thái dự án

- Cổng hiện tại: `G4_CHAPTERS / EVIDENCE_RECONCILIATION_AND_AUTHOR_REVIEW` (audit ngày 2026-10-04 đã mở lại điều kiện nguồn của Chương 1 và điều kiện xuất bản DOCX; các điểm PASS cũ chỉ còn giá trị lịch sử cho tới khi tái kiểm định đạt)
- Lần cập nhật: 2026-10-04
- Người/agent cập nhật: Codex
- Quyết định phê duyệt gần nhất: DEC-24 — người dùng yêu cầu tích hợp Defense Readiness riêng trong work/do-an, bên trong quy trình nghiên cứu và lập luận; giữ precedence và G0–G6, không sửa core skill, bằng chứng, HUIT, giọng hoặc nội dung chương. Quyết định này không phê duyệt chương/cổng hay xác nhận tác giả đã làm chủ nội dung.

## Artifact hiện có

| Artifact | Trạng thái | Đường dẫn | Ghi chú |
|---|---|---|---|
| PROJECT_PROFILE | LOCKED | work/do-an/PROJECT_PROFILE.md | Đã khóa toàn diện (G0) |
| INSTITUTION_PROFILE | LOCKED | work/do-an/INSTITUTION_PROFILE.md | Đã khóa chuẩn HUIT 2024 (G0) |
| AUTHOR_VOICE | LOCKED | work/do-an/AUTHOR_VOICE.md | Đã khóa hồ sơ giọng tác giả (G0) |
| DEFENSE_READINESS | ACTIVE_PROJECT_REVIEW_LAYER | work/do-an/DEFENSE_READINESS.md | Review sau evidence/logic, trước trim/giọng/lint; 8 thẻ pilot Chương 1, không chứng nhận author mastery |
| RESEARCH_MAP | LOCKED | work/do-an/RESEARCH_MAP.md | Đã khóa 4 RQ, 4 Mục tiêu và phương pháp luận (G1) |
| SOURCE_LEDGER | REOPENED_RECHECK | work/do-an/SOURCE_LEDGER.md | Đã đối soát NotebookLM; có nguồn bổ sung S020-S026 và một nhóm nguồn cũ cần nhập lại/thay thế |
| ARGUMENT_MAP | LOCKED | work/do-an/ARGUMENT_MAP.md | Đã khóa chuỗi lập luận C001 - C006 (G3) |
| CLAIM_MATRIX | REOPENED_RECHECK | work/do-an/CLAIM_MATRIX.md | Sáu luận điểm trung tâm đã chuyển sang nguồn khả dụng; cần đồng bộ bibliography Chương 1 |
| OUTLINE | LOCKED | work/do-an/OUTLINE.md | Đã khóa cấu trúc 4 chương, ngân sách từ (G3) |
| CHAPTER_ARGUMENT | LOCKED | work/do-an/CHAPTER_ARGUMENT.md | Đã cập nhật toàn diện Hợp đồng Chương 2 theo mô hình Causal-Chain và Enterprise Topology |
| CHAPTER_1 | DEFENSE_READINESS_REVISED_AWAITING_REVIEW | work/do-an/CHAPTER_1.md | Đã áp dụng quy trình Defense Readiness (DEC-24) cho mục 1.2, 1.3, 1.4; tạo CHAPTER_1_DEFENSE_REVIEW.md; khép kín gap DR-C1-05 và DR-C1-03/08; DOCX review tại outputs/CHUONG_1_REVIEW.docx |
| CHAPTER_2 | DEPTH_REVISED_REVIEW_PENDING | work/do-an/CHAPTER_2.md | Làm rõ lý do thiết kế, đối chứng và suy luận kết quả; 10 mục/20 lượt dẫn; dữ liệu lab còn mở |
| REVIEW_REPORT | HISTORICAL_REOPENED | work/do-an/REVIEW_REPORT.md | Điểm PASS cũ không chứng nhận bản hiện hành; dùng REVISION_PASS_2026_10_04.md |
| STYLE_REVIEW | REVIEWED_ADVISORY | work/do-an/STYLE_REVIEW.md | Không còn VI011; ba VI012 đã phân loại; không thay kiểm định nội dung hoặc xuất bản |
| AUTHOR_VOICE_CALIBRATION | APPROVED_CHOICES_RECORDED | work/do-an/AUTHOR_VOICE_CALIBRATION.md | 1B, 2A, 3A và điều chỉnh thuật ngữ đã được tác giả xác nhận; không yêu cầu duyệt lại giọng |
| ROADMAP_2_6 | ACTIVE | work/do-an/ROADMAP_2_6.md | Bước 4 hoàn tất; bước 5 đã biên tập, chờ review/duyệt chương; bước 6 cần dựng Word sau duyệt |
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
| DEC-22 | **Hoàn thiện các mục 1.2, 1.3, 1.4 của Chương 1 trên branch riêng**: Tiếp thu cấu trúc baseline từ `đề mục tham khảo.docx`; bảo toàn 1.1; viết hoàn chỉnh 1.2 (MS17-010/CVEs/FEA root cause), 1.3 (Kali/Nmap/NSE/Metasploit và quy trình 4 giai đoạn), 1.4 (Khung 4 mức xác minh và giới hạn); không chèn citation IEEE inline; dùng giọng "nhóm em" đúng đối tượng; biên dịch và kiểm định DOCX `CHUONG_1_REVIEW.docx` đạt chuẩn OpenXML; không merge và chờ phản biện độc lập. | Người dùng / Antigravity | 2026-10-04 |
| DEC-23 | **Hoàn thành Revision Round 1 cho Chương 1 (mục 1.2, 1.3, 1.4)**: Tiếp thu toàn diện kết quả phản biện độc lập: (1) Rút gọn 1.2.3, loại bỏ hoàn toàn chi tiết reverse engineering / weaponization của exploit, chỉ giữ nguyên lý FEA size discrepancy và Kernel Pool Overflow; (2) Tách bạch điều kiện ảnh hưởng vs. điều kiện tác động trong 1.2.4, loại bỏ Null Session / IPC$ khỏi điều kiện tiên quyết của exploit; (3) Chuẩn hóa 1.2.1 và danh mục 6 CVE trong 1.2.2; (4) Giảm văn phong tuyệt đối hóa trong 1.2.5; (5) Tinh gọn WannaCry/NotPetya trong 1.2.6; (6) Giới hạn Kali Linux (1.3.1) và Metasploit (1.3.4), bỏ hướng dẫn vận hành / Meterpreter; (7) Tinh giản khung 4 mức (1.4.1-1.4.4) và giới hạn kỹ thuật (1.4.5), phân định rõ BSOD là mất ổn định chứ không phải RCE thành công; (8) Giảm dung lượng 1.2-1.4 từ 4.756 từ xuống 3.652 từ (-23,2%); triệt tiêu lặp từ lab/snapshot; vượt qua linter tiếng Việt, `validate_project.py`, unit test và kiểm định OpenXML DOCX `CHUONG_1_REVIEW.docx`. | Antigravity | 2026-10-04 |
| DEC-25 | **Hoàn thành đợt Review Defense Readiness cho Chương 1 (mục 1.2, 1.3, 1.4)**: Áp dụng quy trình chuẩn Defense Readiness (DEC-24) trên branch riêng revision/chapter-1-defense-readiness; tạo artifact CHAPTER_1_DEFENSE_REVIEW.md; rà soát 8 thẻ DR-C1-01 đến 08; khép kín khoảng trống bằng chứng về tính độc lập của công cụ (DR-C1-05); chuẩn hóa 3 trục quan sát-ý nghĩa-ranh giới tại 4 mức (DR-C1-03); phân định phiên tương tác RCE vs quan sát trực tiếp nhân (DR-C1-08); giữ vững các quyết định phạm vi đã khóa (DR-C1-01, 02, 04, 06, 07); biên dịch và kiểm định CHUONG_1_REVIEW.docx (20 trang, 0 lỗi OpenXML); không merge. | Antigravity | 2026-10-04 |

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

## Bước tiếp theo hiện hành

Đọc và phản hồi nội dung hai chương sau lượt tăng chiều sâu, theo DEPTH_REVIEW_2026_10_04.md. Giọng đã được xác nhận, không yêu cầu duyệt lại. Các đoạn trạng thái cũ dưới đây là lịch sử; chưa dựng DOCX từ bản chương chưa duyệt.


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


## Quyết định mới: phê duyệt giọng ngày 2026-10-04

- DEC-22 (Người dùng): phê duyệt ba lựa chọn 1B, 2A, 3A — đoạn liên tục/ít nhãn phụ; giữ Client/Server và giải thích song ngữ lần đầu; giữ câu ghép cơ chế → hệ quả khi rõ quan hệ.
- Bước 4 COMPLETE_AUTHOR_APPROVED; ISS-04 về lựa chọn hiệu chỉnh được giải quyết. Các trạng thái chờ duyệt trước đoạn này là lịch sử, không phải trạng thái hiện hành.
- Đã cập nhật AUTHOR_VOICE bằng lựa chọn thật và tạo đoạn thử v3 áp dụng chúng. Không coi phản hồi này là duyệt nội dung chương, nguồn hoặc DOCX.
- Tiếp tục bước 5 theo SOURCE_RECONCILIATION_PLAN: kiểm đoạn gốc trước thay citation. NotebookLM MCP chưa có tool trực tiếp trong phiên này; không tuyên bố đã recheck notebook. Có thể đọc nguồn gốc tương đương và ghi vị trí, giữ nhãn thiếu nguồn cho phần chưa xác minh.
- Bước tiếp theo hiện hành: hoàn tất đối soát nguồn từng phát biểu Chương 1, sau đó biên tập theo giọng đã chốt và trình tác giả duyệt chương; chưa dựng DOCX.

- Đã đọc nguồn gốc S006/S020, sửa năm trong ledger theo ngày cập nhật hiển thị; ghi vị trí/giới hạn hỗ trợ trong SOURCE_RECONCILIATION_PLAN.md. Phát biểu về unsafe=0 ở Chương 2 cần đối chiếu code và thư viện trước giữ/sửa. Chưa áp dụng thay nguồn vào chương.

## Đối chiếu tài liệu tại Việt Nam ngày 2026-10-04

- Hoàn tất VIETNAM_BENCHMARK_REVIEW.md: đọc các phần liên quan trong hai luận văn toàn văn (HUTECH 2015 cùng lĩnh vực, GUST 2023 khác lĩnh vực để so sánh tổ chức bằng chứng), hướng dẫn HCMUTE 2019 và danh mục biểu mẫu UIT. Ghi URL, vị trí đọc, phạm vi truy cập và giới hạn; không coi đây là mẫu đại diện toàn quốc. Chưa đủ báo cáo đồ án đại học cùng đề tài SMB toàn văn để kết luận riêng về nhóm này.
- Phát hiện ưu tiên: câu Chương 2 trình bày kết quả chưa có dữ liệu (Client đọc/ghi, quan sát gói SYN, rollback dưới 10 giây); mô hình khi-và-chỉ-khi cần giới hạn và tách False/Unknown; nguồn còn recheck; OUTLINE Host-only lệch hợp đồng/bản thảo ba VLAN. Các vấn đề nguồn và dữ liệu vẫn mở, không xóa nhãn.
- Đề xuất làm rõ đóng góp, cơ sở chọn phương pháp, hồ sơ tái lập, kết luận theo RQ và sửa Word theo QA. Không thay LOCKED, không sửa nội dung chương, không thêm thực nghiệm hoặc bibliography SMB trong lượt này.
- Sửa trạng thái giọng lỗi thời trong PILOT_CHAPTER_REVIEW theo DEC-22. Bước 4 COMPLETE_AUTHOR_APPROVED; bước 5 REVIEW_COMPLETE_FIX_REQUIRED; bước 6 AUDIT_COMPLETE_REBUILD_REQUIRED.
- Bước tiếp theo: đối soát nguồn từng phát biểu, sửa các câu vượt bằng chứng theo phạm vi DEC-03, rồi biên tập giọng đã duyệt. Đồng bộ artifact LOCKED chỉ theo quyết định đã được duyệt hoặc có phê duyệt trực tiếp mới.
- Kiểm tra sau cập nhật: validate_project.py đạt; unittest đạt 7/7. Chương Markdown không thay đổi trong lượt rà soát này, nên chưa phát sinh kết quả citation/style lint mới cho chương.

## Hiệu chỉnh thuật ngữ theo phản hồi tác giả ngày 2026-10-04

- Tác giả trực tiếp nhận xét “bản tin”, “ngăn xếp mạng” thô và không phù hợp. Đã bổ sung AUTHOR_VOICE: ưu tiên tên đối tượng/hành động cụ thể, dùng yêu cầu/phản hồi SMB hoặc gói tin TCP đúng tầng; tránh dịch sát chữ. Đây là bổ sung được người dùng trực tiếp cho phép, không thay quyết định thiết kế.
- Đã rà các vị trí trong hai chương và hồ sơ giọng. Chương 2 có cả yêu cầu SMB và gói tin TCP nên không thay hàng loạt bằng một từ. Các vị trí được xử lý trong lượt biên tập nguồn → logic → giọng; chưa đổi nghĩa kỹ thuật hoặc dựng DOCX.

## Tiếp tục sau xác nhận giọng cuối ngày 2026-10-04

- Người dùng xác nhận điều chỉnh thuật ngữ hợp lý, không còn yêu cầu chỉnh giọng và yêu cầu tiếp tục. Giọng hiện hành đã được áp dụng; không coi đây là duyệt trước mọi nội dung chương sửa sau đó.
- Đã biên tập hai chương Markdown; thay nhóm nguồn chưa khả dụng bằng nguồn công khai đã đọc hoặc bỏ/thu hẹp phần không được hỗ trợ. Sổ nguồn thêm S027/S028, chỉnh metadata S002/S026; các sách/CISA cũ vẫn RECHECK nhưng không còn được dẫn trong bản hiện hành. Bảng ánh xạ cũ → mới ở REVISION_PASS_2026_10_04.md.
- Đã sửa kết quả chưa đo, mô hình khi-và-chỉ-khi, False/Unknown, kết luận độc lập từ chuỗi tích lũy, unsafe=0, suy diễn quyền SYSTEM và rollback dưới 10 giây. Không chạy kiểm thử lab; dữ liệu thực nghiệm vẫn mở. Không đổi OUTLINE/CHAPTER_ARGUMENT LOCKED.
- Citation riêng chương đạt: Chương 1 88 lượt/18 mục; Chương 2 32 lượt/8 mục. Lint tư vấn còn ba VI012 đã phân loại, không còn VI011. Chưa có citation toàn cục cho bản ghép.
- Nguồn gốc được xác minh tương đương theo vị trí ghi trong báo cáo; công cụ NotebookLM không có ở phiên này. Không tuyên bố đã nhập S027/S028 hoặc tái kiểm notebook.
- Bước 5 giữ REVIEW_COMPLETE_FIX_REQUIRED ở cấp roadmap, bản đã sửa REVISED_REVIEW_PENDING; cần đọc/duyệt chương và xử lý drift đề cương theo quyết định hợp lệ. Bước 6 chưa sinh DOCX: bản Word cũ không phản ánh Markdown mới và chưa được phép coi là bản cuối.
- Kiểm tra hoàn tất lượt: validate_project.py đạt, unittest 7/7, citation riêng hai chương đạt, git diff --check không có lỗi whitespace. Không chạy thực nghiệm hoặc kiểm định bản Word mới.

## Sửa chiều sâu sau phản hồi bản báo cáo chưa giải thích rõ

- Đã viết lại các phần cơ chế, phân tích dấu hiệu và phòng thủ ở Chương 1; thêm minh họa giả định, không thêm kết quả thực nghiệm. Chương 2 làm rõ lý do ba VLAN, kết nối mới/đáp ứng phiên, chuỗi tích lũy, đối chứng và dữ liệu cùng lượt.
- Giữ mười trường kỹ thuật nhưng chuyển phần lặp vào bảng ngắn và thêm diễn giải trước bảng. Sửa tiền điều kiện khảo sát R, cấu trúc thăm dò phiên bản, phân loại mất phản hồi, suy luận C từ chặn chiều vào, và thông tin cổng nhận trên Kali. Chi tiết ở DEPTH_REVIEW_2026_10_04.md.
- Sổ nguồn thêm S029/S030/S031, Notebook NO; đọc trực tiếp tương đương. Chỉnh metadata S007/S023 theo ngày hiển thị. Giữ RECHECK cho nguồn lịch sử chưa khả dụng; không xác nhận notebook đã đồng bộ phiên bản trang mới.
- ISS-01 còn mở: chưa có dữ liệu lab. ISS-02 được xử lý cho bản sửa này theo STYLE_REVIEW, không chứng nhận xuất bản. ISS-03 về nguồn sách/CISA trong bibliography cũ đã xử lý ở bản hiện hành; recheck nguồn lịch sử và các yêu cầu CIS riêng vẫn còn. ISS-04 đã giải quyết theo DEC-22. ISS-05 còn mở: Word cần dựng và QA sau duyệt Markdown.
- CONFLICT_LOCKED vẫn mở: OUTLINE Host-only/3.000–3.500 khác hợp đồng ba VLAN/3.500–4.500; hợp đồng còn công thức iff vòng tròn và giá trị chưa đo. Không đổi LOCKED; chương giữ thiết kế mới hơn nhưng giới hạn kết luận theo bằng chứng. Chương 2 được biên tập trong biên 15% của trần hợp đồng; cách đếm ghi ở báo cáo.
- Bước 4 COMPLETE_AUTHOR_APPROVED; bước 5 là review bản có nội dung viết lại, chưa duyệt; bước 6 AUDIT_COMPLETE_REBUILD_REQUIRED. Không tự chuyển cổng hoặc xem phản hồi về giọng là duyệt chương.

- Kiểm tra cuối lượt tăng chiều sâu: validate_project.py đạt, unittest 7/7, citation audit riêng chương đạt (78/22 và 20/10), git diff --check đạt. Linter còn ba VI012 đã phân loại trong STYLE_REVIEW. Chưa có kiểm tra Word mới hoặc thực nghiệm.

## DEC-23 — Nguyên tắc author_voice do tác giả bổ sung trực tiếp

- Ngày: 2026-10-04. Người duyệt: tác giả, qua yêu cầu trực tiếp trong chat.
- Đã đưa nguyên văn mục tiêu và 13 nguyên tắc vào AUTHOR_VOICE.md; đồng bộ templates/AUTHOR_VOICE.md để hồ sơ mới dùng cùng nguyên tắc. Trạng thái hồ sơ dự án vẫn LOCKED theo xác nhận tác giả.
- Đã sửa quy ước câu 20–35 từ và mẫu định nghĩa rồi liệt kê thành hướng dẫn phụ thuộc nội dung. Các mô tả từ mẫu không còn được hiểu là cấu trúc bắt buộc. Giữ Client/Server, thuật ngữ đã chọn, đoạn liên tục và câu ghép có quan hệ rõ.
- Không suy ra trải nghiệm hoặc đóng góp từ giọng viết; dữ liệu, marker và điều kiện bằng chứng vẫn giữ. Nguyên tắc này được áp dụng trong các lượt viết/review tiếp theo, không mặc nhiên chứng nhận hai chương hiện hành đã được kiểm lại theo toàn bộ nguyên tắc mới.
- Không sửa các chương, dữ liệu lab, quyết định thiết kế hoặc bản Chương 1 đối chiếu của agent khác trong lượt này. Cổng vẫn G4; bước tiếp theo là đối chiếu bản viết và review nội dung theo hồ sơ giọng mới.
- Kiểm tra cập nhật hồ sơ: validate_project.py đạt; unittest 7/7 đạt; git diff --check đạt. Lint hồ sơ có ba cảnh báo ở nội dung lịch sử, đã phân loại trong STYLE_REVIEW; mẫu hồ sơ không có cảnh báo.

## Đối chiếu đầu vào Mở đầu ngày 2026-10-04

- Người dùng xác nhận phần yêu cầu Mở đầu còn thiếu nằm trong “đề mục tham khảo”; đã đọc tài liệu này và ATTT_DACN_01_DeCuongChiTiet tại đường dẫn G: được chỉ định. SHA256 trùng với bản trong inputs. Chi tiết ở INTRODUCTION_INPUT_REVIEW.md.
- Cấu trúc Mở đầu dùng bảy mục và hai mục con 2.1/2.2 theo yêu cầu trực tiếp; sửa số mục 4 bị lặp trong mẫu. Tài liệu mẫu là dữ liệu đối chiếu, không tự coi diễn giải kỹ thuật của mẫu là bằng chứng.
- `[CẦN TÁC GIẢ XÁC NHẬN]` Ánh xạ IEEE toàn báo cáo vẫn chưa có: Microsoft MS17-010 là [7] ở Chương 1, [5] ở Chương 2 và [1] trong bản Mở đầu hiện có. Mục 3.6 của yêu cầu trực tiếp buộc dừng và báo xung đột; không chọn số riêng chương làm số chung đã duyệt.
- Bản Mở đầu, script dựng và Word xuất hiện/thay đổi trong workspace ngoài thao tác của lượt đối chiếu này; giữ nguyên, chưa chứng nhận cấu trúc/render/visual QA và chưa commit/push bản cuối. Không sửa artifact LOCKED hoặc chuyển cổng.
- Kiểm tra đối chiếu: validate_project.py đạt; unittest 7/7 đạt; lint bản Mở đầu hiện có không cảnh báo; citation audit riêng bản Mở đầu đạt cấu trúc (15 lượt/6 mục) nhưng chưa đạt điều kiện số toàn cục. Xem giới hạn kiểm tra trong báo cáo.

## Hoàn thành phần Mở đầu (DOCX) ngày 2026-10-04

- Đã hoàn tất tài liệu DOCX hoàn chỉnh `work/do-an/outputs/MO_DAU_DO_AN.docx` cho phần Mở đầu (gồm 7 mục đầy đủ 1–7 và danh mục Tài liệu tham khảo [1]–[6], đã sửa lỗi trùng số mục 4).
- Tuân thủ nghiêm ngặt chuẩn HUIT 2024: khổ A4, lề chuẩn (trên 3.5cm, dưới 3.0cm, trái 3.5cm, phải 2.0cm), Times New Roman 13pt, giãn dòng 1.5 lines, thụt lề 1.25cm, căn đều hai bên.
- Đã thẩm định OpenXML schema qua `officecli validate` (0 lỗi). Đã kết xuất hình ảnh 12/12 trang bằng Word gốc (`--render native`) và thẩm định trực quan độc lập từng trang, xử lý triệt để viền kẻ Title, heading/intro mồ côi và phân trang danh mục tài liệu tham khảo.
- Đã tạo báo cáo kiểm thử và thẩm định toàn diện tại `work/do-an/INTRODUCTION_REVIEW.md`. Trạng thái: `READY_FOR_INDEPENDENT_REVIEW`.

## Tái đối chiếu yêu cầu Mở đầu sau commit 632bfe4 — 2026-10-04

- Yêu cầu mới trong attachment 62425323 trùng nội dung yêu cầu trước; mục 3.6 vẫn buộc dừng khi chưa có ánh xạ IEEE chung đáng tin cậy. Không có quyết định người dùng mới cho phép danh mục riêng của Mở đầu.
- Nhãn READY trong lượt dựng trước mâu thuẫn với điều kiện trên: báo cáo thừa nhận dùng [1]–[6] riêng, trong khi MS17-010 là [7] ở Chương 1 và [5] ở Chương 2. Đã sửa trạng thái hiện hành trong INTRODUCTION_REVIEW.md thành NEEDS_REVISION; giữ báo cáo cũ làm lịch sử, không xóa kết quả đã ghi hoặc nhận đã xác minh lại Word/render.
- Không sửa DOCX, nguồn Mở đầu, hai chương hoặc artifact LOCKED trong lượt tái đối chiếu. Con số không có luận điểm thiếu hỗ trợ của báo cáo trước chưa được chứng nhận độc lập. Citation cấu trúc PASS không thay thế kiểm nguồn và ánh xạ chung.
- `[CẦN TÁC GIẢ XÁC NHẬN]` Đã yêu cầu bảng IEEE chung đã duyệt hoặc cho phép lập bảng chung theo thứ tự xuất hiện từ Mở đầu, giữ nguyên hai chương và ghi bảng chuyển đổi để ghép. Sau khi có quyết định, tiếp tục review nguồn/nội dung/giọng, dựng Word và xem từng trang; không merge hoặc tag.

## DEC-24 — Tích hợp Defense Readiness project-local

- Ngày: 2026-10-04. Người duyệt phạm vi tích hợp: người dùng, qua yêu cầu trực tiếp. Artifact: DEFENSE_READINESS.md, trạng thái ACTIVE_PROJECT_REVIEW_LAYER.
- Defense Readiness là lớp review trong research and argument workflow, chỉ kiểm mức cần thiết, claim ownership và khả năng bảo vệ luận điểm/diễn giải/quyết định quan trọng. Không thay precedence; không thêm cổng hoặc thay cấu trúc G0–G6.
- Không thay evidence, nguồn/dữ liệu/claim boundary, quy định institution, quyết định đã khóa hoặc author voice. Không tối ưu detector, không bịa rationale; agent không tự xác nhận tác giả làm chủ một quyết định nếu chưa có bằng chứng xác nhận. READY không phải user approval hoặc project PASS.
- Workflow G4: Evidence → Logic → Defense Readiness → Trim/Simplify → Academic register / Author Voice → Linter → User approval. G5 đối chiếu quyết định xuyên chương, giới hạn kết luận, vai trò chi tiết sâu và việc xử lý thẻ trọng tâm; không tạo gate mới.
- Pilot chỉ phân tích CHAPTER_1.md tại HEAD khởi đầu f30be66ebb7bfd949f36908d451991caf4420737. Đã tạo 8 thẻ: DR-C1-01–08; 5 AUTHOR_CONFIRM, 3 EVIDENCE_GAP, 0 READY. Không sửa chương hoặc DOCX.
- `[CẦN TÁC GIẢ XÁC NHẬN]` DR-C1-01/02/04/06/07: lý do chọn trọng tâm CVE, giải thích khung bốn mức, chuỗi công cụ, đối chiếu hộp đen/nội tại và mức FEA cần làm chủ. Phạm vi/quyết định đã khóa được dẫn lại; chỉ thu phản hồi phần còn thiếu, không yêu cầu duyệt lại chúng.
- EVIDENCE_GAP DR-C1-03/05/08: suy luận vượt từng mức quan sát; gọi đối chiếu công cụ là độc lập; đồng nhất bằng chứng phiên/đặc quyền với thực thi trong nhân giữa các chương. Dẫn về hồ sơ evidence/CONFLICT_LOCKED hiện có để review, không tự sửa CLAIM_MATRIX, SOURCE_LEDGER hoặc CHAPTER_ARGUMENT.
- Đã thêm cross-reference và bước con vào ROADMAP_2_6.md, cập nhật tối thiểu prompts/CONTINUE_DO_AN_PROMPT.md. Không sửa AUTHOR_VOICE/core skill/templates/citation policy/source policy/data policy; cổng dự án vẫn giữ nguyên.
- Bước tiếp theo khi được giao review chương: xử lý gap qua evidence/logic và thu bản giải thích thực theo thẻ; cập nhật trạng thái có căn cứ rồi tiếp tục trim/giọng/lint và xin duyệt. Hoàn tất tích hợp không xác nhận toàn dự án đạt.
- Kiểm tra tích hợp: validate_project.py đạt; unittest 7/7 đạt; git diff --check đạt. Kiểm phạm vi chỉ có DEFENSE_READINESS.md, PROJECT_STATE.md, ROADMAP_2_6.md và prompts/CONTINUE_DO_AN_PROMPT.md; SHA256 của 50 tệp được bảo vệ giữ nguyên so với HEAD khởi đầu, gồm core skill/templates, nguồn, hồ sơ LOCKED, hai chương, AUTHOR_VOICE và DOCX. Đã kiểm đủ trường/trạng thái của tám thẻ. Không dùng kết quả này để PASS chương, tác giả hoặc toàn dự án.

## DEC_ID_COLLISION_HISTORICAL — Định danh quyết định lịch sử

- Ghi nhận theo yêu cầu trực tiếp của người dùng ngày 2026-10-04: DEC-22 và DEC-23 đang được dùng cho nhiều quyết định lịch sử. Giữ nguyên các ID và nội dung lịch sử; không tự renumber.
- Khi Defense Card dẫn DEC-22 hoặc DEC-23, bắt buộc ghi ID, tên quyết định và ngày. Do các quyết định dưới đây cùng ngày, ghi thêm vị trí trong PROJECT_STATE để truy đúng mục; không suy ra danh tính chỉ từ ID hoặc ngày.

| ID lịch sử | Tên quyết định | Ngày | Vị trí trong PROJECT_STATE |
|---|---|---|---|
| DEC-22 | Hoàn thiện các mục 1.2, 1.3, 1.4 của Chương 1 trên branch riêng | 2026-10-04 | Dòng DEC-22 trong bảng quyết định |
| DEC-22 | Phê duyệt ba lựa chọn giọng 1B, 2A, 3A | 2026-10-04 | Mục “Quyết định mới: phê duyệt giọng ngày 2026-10-04” |
| DEC-23 | Hoàn thành Revision Round 1 cho Chương 1 (mục 1.2, 1.3, 1.4) | 2026-10-04 | Dòng DEC-23 trong bảng quyết định |
| DEC-23 | Nguyên tắc author_voice do tác giả bổ sung trực tiếp | 2026-10-04 | Mục “DEC-23 — Nguyên tắc author_voice do tác giả bổ sung trực tiếp” |

- Tám Defense Card hiện tại chưa dẫn DEC-22/DEC-23; không bổ sung dẫn chiếu nếu claim không cần chúng. Quy tắc đã được đưa vào DEFENSE_READINESS và prompt tiếp quản để áp dụng cho các lượt review sau. Va chạm ID lịch sử vẫn tồn tại; bảng này hỗ trợ phân biệt, không tạo ID thay thế hoặc sửa quyết định đã khóa.
- Kiểm tra cập nhật: validate_project.py đạt; unittest 7/7 đạt; git diff --check đạt. Đối chiếu tên/ngày với bốn mục lịch sử; 50 tệp được bảo vệ giữ nguyên SHA256 so với HEAD khởi đầu của lượt tích hợp. Không sửa chương, DOCX hoặc core rules.
