# Trạng thái dự án

- Cổng hiện tại: `G4_CHAPTERS` (Chương 1 LOCKED_PASS 9.0/10; Chương 2 TINH_CHINH_HOAN_THIEN đạt 9.5/10 PASS)
- Lần cập nhật: 2026-10-04
- Người/agent cập nhật: Codex
- Quyết định phê duyệt gần nhất: Tích hợp hệ thống giọng tác giả và kiểm soát văn phong mới nhưng bảo toàn toàn bộ quy định HUIT, nguồn, dữ liệu và quyết định học thuật đã khóa; các cảnh báo linter chỉ là đầu vào biên tập trước G5/G6.

## Artifact hiện có

| Artifact | Trạng thái | Đường dẫn | Ghi chú |
|---|---|---|---|
| PROJECT_PROFILE | LOCKED | work/do-an/PROJECT_PROFILE.md | Đã khóa toàn diện (G0) |
| INSTITUTION_PROFILE | LOCKED | work/do-an/INSTITUTION_PROFILE.md | Đã khóa chuẩn HUIT 2024 (G0) |
| AUTHOR_VOICE | LOCKED | work/do-an/AUTHOR_VOICE.md | Đã khóa hồ sơ giọng tác giả (G0) |
| RESEARCH_MAP | LOCKED | work/do-an/RESEARCH_MAP.md | Đã khóa 4 RQ, 4 Mục tiêu và phương pháp luận (G1) |
| SOURCE_LEDGER | LOCKED | work/do-an/SOURCE_LEDGER.md | Đã chuẩn hóa 19 nguồn gốc chính thức (S001 - S019) (G2) |
| ARGUMENT_MAP | LOCKED | work/do-an/ARGUMENT_MAP.md | Đã khóa chuỗi lập luận C001 - C006 (G3) |
| CLAIM_MATRIX | LOCKED | work/do-an/CLAIM_MATRIX.md | Đã cập nhật ma trận luận điểm đồng bộ S001 - S019 (G3) |
| OUTLINE | LOCKED | work/do-an/OUTLINE.md | Đã khóa cấu trúc 4 chương, ngân sách từ (G3) |
| CHAPTER_ARGUMENT | LOCKED | work/do-an/CHAPTER_ARGUMENT.md | Đã cập nhật toàn diện Hợp đồng Chương 2 theo mô hình Causal-Chain và Enterprise Topology |
| CHAPTER_1 | LOCKED_PASS | work/do-an/CHAPTER_1.md | Toàn văn Chương 1 v3.2 hoàn chỉnh (398 dòng, ~5.450 từ, 5 bảng, 4 sơ đồ, 19 tài liệu tham khảo IEEE, Điểm chính thức: 9.0/10 PASS) |
| CHAPTER_2 | READY_FOR_APPROVAL | work/do-an/CHAPTER_2.md | **Bản thảo Chương 2 hoàn thiện sau tự phản biện theo mô hình Causal-Chain** (413 dòng, 4 bảng, 3 sơ đồ ASCII, 9 trích dẫn IEEE xuất hiện tuần tự 100%, Điểm: 9.5/10 PASS) |
| REVIEW_REPORT | PASS | work/do-an/REVIEW_REPORT.md | Báo cáo đánh giá Chương 2 theo mô hình Causal-Chain & 5 điểm tự hoàn thiện (Điểm: 9.5/10 PASS) |
| STYLE_REVIEW | OPEN | work/do-an/STYLE_REVIEW.md | Audit di chuyển: Chương 1 có 18 và Chương 2 có 14 cảnh báo cần phân loại trước G5/G6; không có rule sáo ngữ `VI001–VI010` |

## Quyết định đã khóa

| ID | Quyết định | Người duyệt | Ngày |
|---|---|---|---|
| DEC-01 | Sử dụng NotebookLM notebook `e7b2d815-8b85-47db-95f4-8d0844a60c04` | Người dùng | 2026-09-12 |
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

## Nguồn tài liệu

| Source ID | Trạng thái | Ghi chú |
|---|---|---|
| S001 - S019 | VERIFIED | 19 nguồn tài liệu chính thống (Microsoft Learn, MSRC, NIST NVD, Rapid7, CISA, Nmap Project, sách chuyên khảo học thuật tiêu chuẩn). |

## Vấn đề còn mở

| ID | Nhãn | Mô tả | Ảnh hưởng | Hành động tiếp theo |
|---|---|---|---|---|
| ISS-01 | `[CẦN DỮ LIỆU]` | Dữ liệu log, ảnh chụp màn hình và kết quả chạy demo thực nghiệm lab | Các phần thực nghiệm (Chương 2, 3, 4) chưa ghi nhận kết quả chạy thật | Duy trì nhãn `[CẦN DỮ LIỆU]`, tập trung vào kiến trúc lab, tham số an toàn và kịch bản chuẩn hóa |
| ISS-02 | `STYLE_REVIEW_OPEN` | 32 cảnh báo tư vấn về nhịp câu và mở đoạn trong Chương 1–2 | Chưa đủ điều kiện tuyên bố kiểm tra văn phong G5/G6 theo hệ thống mới | Phân loại từng cảnh báo, duyệt diff, chạy publication lint và sinh lại DOCX trước lần bàn giao kế tiếp |

## Bước tiếp theo duy nhất

Trình người dùng xem xét Chương 2 và `STYLE_REVIEW.md`. Nếu phê duyệt nội dung, thực hiện vòng biên tập có kiểm soát đối với 32 cảnh báo, chạy lại kiểm tra nguồn và publication lint, rồi mới sinh lại DOCX để chuyển sang **Chương 3: Thực nghiệm kiểm thử an ninh giao thức SMB**.
