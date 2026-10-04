# Roadmap xác nhận hệ thống từ NotebookLM tới DOCX

- Phạm vi: dự án `do-an` về kiểm thử lỗ hổng SMB.
- Ngày bắt đầu: 2026-10-04.
- Nguyên tắc: thực hiện tuần tự; bước sau có thể được audit nhưng không được tuyên bố khóa nếu cổng trước còn cần tác giả phê duyệt.

| Bước | Mục tiêu | Điều kiện đạt | Artifact/Bằng chứng | Trạng thái |
|---|---|---|---|---|
| 2 | Kiểm tra kết nối NotebookLM thật | MCP khởi động, xác thực, đúng notebook, có nguồn, câu hỏi biết trước trả lời đúng và nêu giới hạn | Health check, smoke test, `SOURCE_LEDGER.md` | `COMPLETE` |
| 3 | Nạp và khóa kho nguồn khả dụng | Nguồn trung tâm có metadata, vị trí và trạng thái Notebook; nguồn không có toàn văn bị hạ trạng thái | `SOURCE_LEDGER.md`, `CLAIM_MATRIX.md` | `COMPLETE_WITH_RECHECK` |
| 4 | Hiệu chỉnh giọng tác giả | Có mẫu gốc, đoạn thử 250–400 từ và sửa đổi thật của tác giả | `AUTHOR_VOICE.md`, `AUTHOR_VOICE_CALIBRATION.md` | `COMPLETE_AUTHOR_APPROVED` |
| 5 | Thực hiện một chương thí điểm | Review claim–source, citation, logic, Defense Readiness, trim, giọng, linter; mọi cảnh báo có quyết định; tác giả duyệt | `CHAPTER_1.md`, `PILOT_CHAPTER_REVIEW.md`, `DEFENSE_READINESS.md` | `REVIEW_COMPLETE_FIX_REQUIRED` |
| 6 | Kiểm tra vòng xuất Word | Publication lint, audit DOCX, render toàn bộ trang, ghi lỗi và kiểm tra lại sau sửa | `PUBLICATION_CHECKLIST.md`, `DOCX_QA_REPORT.md` | `AUDIT_COMPLETE_REBUILD_REQUIRED` |

## Defense Readiness trong workflow dự án — DEC-24 & DEC-26 (Fail-Closed Hardening)

Đây là bước review project-local nằm trong quy trình nghiên cứu và lập luận; giữ nguyên thứ tự ưu tiên và cấu trúc G0–G6. Không thay nguồn/dữ liệu, claim boundary, HUIT, quyết định LOCKED hoặc author voice. Chi tiết và thẻ pilot tại `DEFENSE_READINESS.md`; READY không phải user approval và không cho phép agent tự PASS author mastery hay tuyên bố chapter PASS.

Nguyên tắc cốt lõi: **FAIL-CLOSED — UNRESOLVED IS VALID**. Một lượt review hoàn thành tốt dù còn các thẻ mở (`AUTHOR_CONFIRM`, `EVIDENCE_GAP`, `SIMPLIFY`, `REMOVE_CANDIDATE`). Cấm coi số lượng READY là KPI và cấm tối ưu đóng thẻ. Áp dụng quy tắc **Two-Key cho READY** (Evidence Key + Ownership Key; quyết định LOCKED không thay thế cho author ownership). Bắt buộc chạy **Pre-flight Rule Version Check** (báo `DEFENSE_RULE_VERSION_MISMATCH` và STOP nếu thiếu patch) và **Counter-Review** cho mọi thẻ READY. Cấm tự sinh câu trả lời bảo vệ thay tác giả; bắt buộc dùng `[CHƯA CÓ PHẢN HỒI TÁC GIẢ]`. Schema trạng thái là closed enum 5 giá trị; tách bạch trường `Text action`.

Trong G4 chapter review, áp dụng: **Evidence review → Logic review → Defense Readiness review → Trim/Simplify → Academic register / Author Voice → Lint → Author/User approval**. Chỉ lập thẻ cho phần trọng tâm hoặc chi tiết sâu cần bảo vệ, không cho từng câu; thiếu evidence quay lại kiểm nguồn/logic, không dùng simplify để che khoảng trống. Nội dung bắt buộc được giữ; REMOVE_CANDIDATE chỉ là đề xuất có căn cứ.

Trong G5 synthesis, kiểm tra:

- Quyết định phương pháp/thiết kế xuyên chương có nhất quán với quyết định đã khóa không.
- Kết luận có vượt nguồn, dữ liệu hoặc mức quan sát không; EVIDENCE_GAP chưa xử lý không được xem là đạt.
- Chi tiết sâu có phục vụ RQ, mục tiêu, phương pháp hoặc claim chính không.
- Claim trọng tâm có thẻ READY có căn cứ (kèm Review trace), hoặc AUTHOR_CONFIRM đã được người dùng xử lý và phản hồi được đối chiếu/cập nhật vào thẻ chưa. Không coi AUTHOR_CONFIRM còn chờ là đã đóng.

Pilot Chương 1 sau hardening: 8 thẻ (2 READY, 6 AUTHOR_CONFIRM, 0 gap giả định); không sửa chương hoặc nâng trạng thái cổng. Không dùng lớp này để yêu cầu duyệt lại các lựa chọn đã được duyệt.

## Kết quả bước 2

- Kết nối và xác thực bằng persistent session: đạt.
- Notebook: lấy từ cấu hình cục bộ; không lưu ID riêng tư trong Git.
- Phát hiện ban đầu: notebook có 0 nguồn mặc dù ledger cũ ghi `YES`.
- Sau khắc phục: 19 nguồn sử dụng được; hai URL cũ lỗi nhập được giữ ở trạng thái cần xử lý.
- Câu hỏi smoke test: NotebookLM xác định Direct-hosted SMB dùng TCP 445, trỏ đúng tài liệu Microsoft Learn và nêu rõ cổng mở không chứng minh phiên bản SMB, trạng thái bản vá hoặc khả năng khai thác.

## Kết quả bước 3

- Các nguồn chính thức Microsoft, NIST, Nmap, NVD, Rapid7 và Kali đã được nhập.
- S006 được chuyển sang URL Microsoft Learn hiện hành.
- S001, S003, S004, S009, S016 và S019 được hạ xuống `RECHECK/NO` vì notebook chưa có toàn văn hợp lệ.
- S014 được hạ xuống `RECHECK/ERROR` vì URL CISA cũ không nhập được.
- Claim matrix được thay bằng các nguồn đã có trong notebook cho sáu luận điểm trung tâm.
- Việc đánh số IEEE của chương hiện tại vẫn cần vòng biên tập riêng; không tự coi ledger mới là đã đồng bộ với bibliography cũ.

## Cổng cần phê duyệt

Bước 4 chỉ hoàn thành sau khi tác giả sửa hoặc xác nhận đoạn hiệu chỉnh. Audit của bước 5 và 6 được phép chạy để phát hiện lỗi, nhưng không được dùng để tuyên bố Chương 1 hay DOCX đạt bản nộp trước phê duyệt này.

## Điểm tiếp quản

Mọi agent mới bắt đầu tại `HANDOFF.md`, sau đó dùng prompt `prompts/CONTINUE_DO_AN_PROMPT.md`. Không tiếp tục từ nhãn PASS lịch sử nếu chưa đọc các báo cáo audit ngày 2026-10-04.

## Tiến độ hiệu chỉnh sau mẫu Tuần 2

Đoạn thử v2 và ba lựa chọn diễn đạt đã sẵn sàng trong AUTHOR_VOICE_CALIBRATION.md. SOURCE_RECONCILIATION_PLAN.md đã lập tuyến kiểm tra [1]–[19], chưa áp dụng vào chương. Bước 4 vẫn chờ tác giả chọn; bước 5 chưa qua cổng nguồn.

## Phê duyệt bước 4

Tác giả đã chọn 1B, 2A, 3A ngày 2026-10-04; ghi lựa chọn cụ thể trong calibration và AUTHOR_VOICE. Bước 4 hoàn tất hiệu chỉnh. Các ghi nhận chờ duyệt phía trên là lịch sử. Tiếp tục bước 5: kiểm nguồn trước biên tập và xin duyệt chương.

## Lượt biên tập sau xác nhận thuật ngữ

Đã áp dụng giọng và sửa nguồn/logic ở hai chương; xem REVISION_PASS_2026_10_04.md. Nhóm sách/CISA chưa khả dụng không còn được dẫn trong bản hiện hành. Citation cấu trúc riêng từng chương đạt; ba cảnh báo lặp đã phân loại. Bước 5 chưa được nâng thành COMPLETE vì chương sửa chưa được duyệt và artifact LOCKED còn drift. Không dựng DOCX hoặc xóa nhãn dữ liệu để vượt cổng.

## Lượt tăng chiều sâu theo phản hồi tác giả

CHAPTER_1/2 đã được viết lại ở phần cơ chế và diễn giải phương pháp; xem DEPTH_REVIEW_2026_10_04.md. Đây là bản hiện hành thay lượt biên tập ngắn trước đó: 22/10 mục nguồn, vẫn giữ dữ liệu lab chưa có. Bước 5 chưa COMPLETE vì tác giả chưa duyệt nội dung mới; bước 6 chưa dựng Word. Không yêu cầu duyệt lại giọng tác giả.
