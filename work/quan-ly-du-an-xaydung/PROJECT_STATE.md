# Trạng thái dự án

- Cổng hiện tại: `G4_CHAPTERS` / Soạn thảo & Phản biện câu hỏi học thuật
- Lần cập nhật: 2026-10-04
- Người/agent cập nhật: Codex
- Quyết định phê duyệt gần nhất: Di chuyển dự án sang hệ thống giọng tác giả và kiểm soát Word mới; giữ nguyên quy định UTC, nguồn pháp lý và các quyết định nội dung đã có.

## Artifact hiện có

| Artifact | Trạng thái | Đường dẫn | Ghi chú |
|---|---|---|---|
| PROJECT_PROFILE | READY | `work/quan-ly-du-an-xaydung/PROJECT_PROFILE.md` | Hồ sơ đề tài Quản lý dự án ĐTXD công trình |
| INSTITUTION_PROFILE | READY | `work/quan-ly-du-an-xaydung/INSTITUTION_PROFILE.md` | Chuẩn định dạng luận văn / đề án Trường ĐH Giao thông Vận tải Hà Nội |
| RESEARCH_MAP | READY | `work/quan-ly-du-an-xaydung/RESEARCH_MAP.md` | Khung nghiên cứu tổng thể và các tình huống trọng tâm |
| SOURCE_LEDGER | READY | `work/quan-ly-du-an-xaydung/SOURCE_LEDGER.md` | Sổ cái nguồn pháp lý và học thuật chuẩn |
| DE_AN_TRA_LOI_CAU_HOI | COMPLETED | `work/quan-ly-du-an-xaydung/DE_AN_TRA_LOI_CAU_HOI.md` | Bộ câu trả lời chuyên sâu 5 câu hỏi, trọng tâm câu 4 & 5 |
| REVIEW_REPORT_PHAN_BIEN | COMPLETED | `work/quan-ly-du-an-xaydung/REVIEW_REPORT_PHAN_BIEN.md` | Báo cáo phản biện đa tầng 4 cấp độ (Pháp lý, Kỹ thuật, Kinh tế, Hiện trường) |
| AUTHOR_VOICE | PROVISIONAL | `work/quan-ly-du-an-xaydung/AUTHOR_VOICE.md` | Chờ mẫu 250–400 từ hoặc 2–5 trang do tác giả hiệu chỉnh trước khi khóa |
| STYLE_REVIEW | OPEN | `work/quan-ly-du-an-xaydung/STYLE_REVIEW.md` | 13 cảnh báo tư vấn cần phân loại trước lần xuất bản tiếp theo |

## Quyết định đã khóa

| ID | Quyết định | Người duyệt | Ngày |
|---|---|---|---|
| DEC-01 | Tên môn học / đề tài: "Quản lý dự án đầu tư xây dựng công trình" | Người dùng | 2026-09-15 |
| DEC-02 | NotebookLM ID: `767c069e-9f17-4e80-83eb-c02a790966c5` | Người dùng | 2026-09-15 |
| DEC-03 | Cơ sở đào tạo: Trường Đại học Giao thông Vận tải Hà Nội (UTC) | Người dùng | 2026-09-15 |
| DEC-04 | Tập trung chuyên sâu tối đa cho Câu 4 (Mất đồng bộ Thiết kế - Thi công - Cung ứng) và Câu 5 (Quyết định Ban QLDA làm chậm 3 nhà thầu) | Người dùng | 2026-09-15 |
| DEC-05 | Áp dụng quy trình Phản biện đa tầng 4 cấp độ để tối ưu hóa bài làm đạt điểm tuyệt đối (10/10) | Người dùng | 2026-09-15 |
| DEC-06 | Tích hợp hệ thống văn phong mới theo nguyên tắc quy định UTC và bằng chứng có ưu tiên cao hơn mọi rule phong cách; không tiếp tục dùng điểm tự chấm hoặc mức “giống người” làm tiêu chí chất lượng | Người dùng / Codex | 2026-10-04 |

## Nguồn mới

| Source ID | Trạng thái | Ghi chú |
|---|---|---|
| NBLM-01 | CONNECTED | NotebookLM notebook `767c069e-9f17-4e80-83eb-c02a790966c5` |
| S002 - S007 | VERIFIED | Hệ thống Luật Xây dựng, Đấu thầu, Đầu tư công và các NĐ 15, 10, 06/2021/NĐ-CP |

## Vấn đề còn mở

| ID | Nhãn | Mô tả | Ảnh hưởng | Hành động tiếp theo |
|---|---|---|---|---|
| ISS-01 | `[CẦN TÁC GIẢ XÁC NHẬN]` | Kiểm tra nhu cầu xuất bản sang định dạng file DOCX in ấn theo chuẩn UTC | Cổng xuất bản G6 | Sẵn sàng xuất DOCX khi người dùng yêu cầu |
| ISS-02 | `[CẦN TÁC GIẢ XÁC NHẬN]` | Chưa có mẫu giọng viết được tác giả hiệu chỉnh | Không được phép sáng tác dấu ấn cá nhân hoặc trải nghiệm hiện trường | Duyệt mẫu 250–400 từ trong `AUTHOR_VOICE.md` trước khi khóa giọng |
| ISS-03 | `STYLE_REVIEW_OPEN` | 13 cảnh báo về tự gắn nhãn chất lượng, câu dài và mở đoạn lặp | Chưa đủ điều kiện xuất bản theo hệ thống mới | Biên tập có diff, chạy publication lint và render DOCX theo chuẩn UTC |

## Bước tiếp theo duy nhất

Người dùng cung cấp hoặc hiệu chỉnh mẫu giọng 250–400 từ, sau đó duyệt các sửa đổi trong `STYLE_REVIEW.md`; chỉ xuất DOCX sau khi publication lint và vòng render–review theo chuẩn UTC đạt yêu cầu.
