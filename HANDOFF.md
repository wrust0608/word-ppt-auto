# Bàn giao dự án luận văn

> **CURRENT OVERRIDE — 2026-10-06**
>
> Mọi hướng dẫn bàn giao 2026-10-04 ở phần dưới là lịch sử nếu mâu thuẫn với trạng thái mới.
>
> Điểm bắt đầu hiện hành cho agent:
> 1. `work/do-an/PROJECT_STATE.md` — đọc **Current State Summary 2026-10-06** ở đầu file.
> 2. `work/do-an/CHAPTER_3_CONTRACT.md`.
> 3. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`.
> 4. `work/do-an/CHAPTER_3_SECTION_EVIDENCE_MAP.md`.
> 5. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`.
> 6. Artifact/prompt của phase hiện hành.
>
> Chương 2 đã USER APPROVED và final DOCX đã PASS. X6 evidence-prep đã PASS. Chương 3 dùng sectioned workflow; prompt monolithic X7 cũ không được chạy. X7A đang/đã chờ G0 governance reconciliation theo DEC-51.
>
> Nếu nội dung phía dưới yêu cầu quay lại duyệt giọng, coi demo data chưa có, hoặc tiếp tục roadmap 2–6 như current work, đó là trạng thái lịch sử.


> Cập nhật mới nhất 2026-10-04: sau phản hồi bản báo cáo thiếu chiều sâu, đã viết lại cơ chế và lập luận trong CHAPTER_1/2; chi tiết và ánh xạ citation ở work/do-an/DEPTH_REVIEW_2026_10_04.md. Thống kê các lượt trước phía dưới là lịch sử; PROJECT_STATE.md có trạng thái hiện hành. Giọng đã chốt, không yêu cầu duyệt lại. Chương sửa chưa duyệt, Word chưa dựng lại.

> Giọng tác giả: DEC-23 bổ sung mục tiêu và 13 nguyên tắc về cách tư duy, lựa chọn kỹ thuật, dữ liệu cụ thể và diễn đạt theo nội dung; đã đồng bộ AUTHOR_VOICE.md và mẫu hồ sơ. Không ép khuôn đoạn, độ dài hoặc nhịp câu.

> Đây là điểm bắt đầu bắt buộc cho mọi agent tiếp quản repository. Không dựa vào lịch sử chat để suy đoán trạng thái.

## 1. Mục tiêu đang thực hiện

Tiếp tục hoàn thiện hệ thống và dự án luận văn tiếng Việt theo chuỗi kiểm chứng:

`NotebookLM → sổ nguồn → ma trận luận điểm → giọng tác giả → chương Markdown → kiểm định → DOCX → render từng trang`

Đề tài hiện hành là đồ án an toàn thông tin về kiểm thử và đánh giá an ninh giao thức SMB trong môi trường lab. Các tài liệu SMB chỉ là dữ liệu của dự án này, **không phải khuôn cứng của skill soạn luận văn tổng quát**.

## 2. Thứ tự đọc bắt buộc

1. `AGENTS.md`.
2. `.agents/skills/thesis-research-and-writing/SKILL.md`.
3. `.agents/skills/thesis-research-and-writing/references/project-memory.md`.
4. `work/do-an/PROJECT_STATE.md` — nguồn trạng thái chuẩn.
5. `work/do-an/ROADMAP_2_6.md`.
6. Artifact của bước đang làm:
   - nguồn: `SOURCE_LEDGER.md`, `CLAIM_MATRIX.md`;
   - giọng: `AUTHOR_VOICE.md`, `AUTHOR_VOICE_CALIBRATION.md`;
   - chương mẫu: `CHAPTER_1.md`, `PILOT_CHAPTER_REVIEW.md`;
   - Word: `DOCX_QA_REPORT.md`, `PUBLICATION_CHECKLIST.md`.

Nếu nội dung trong file mâu thuẫn với `PROJECT_STATE.md`, phải báo mâu thuẫn trước khi sửa. Quyết định cũ được giữ để truy vết; quyết định tái kiểm định mới hơn có quyền mở lại artifact cũ nhưng không được xóa lịch sử.

## 3. Trạng thái thực tế tại thời điểm bàn giao

| Bước | Trạng thái | Ý nghĩa |
|---|---|---|
| 2. Kết nối NotebookLM | `COMPLETE` | Health check và câu hỏi smoke test đã đạt. |
| 3. Nạp/đối soát nguồn | `COMPLETE_WITH_RECHECK` | Có 19 nguồn sử dụng được, nhưng một nhóm nguồn trong bibliography cũ chưa có toàn văn hoặc URL lỗi. |
| 4. Hiệu chỉnh giọng tác giả | `COMPLETE_AUTHOR_APPROVED` | Tác giả chọn 1B, 2A, 3A; giọng đã chốt, chuyển đối soát nguồn Chương 1. |
| 5. Chương thí điểm | `REVIEW_COMPLETE_FIX_REQUIRED` | Cấu trúc và số trích dẫn đạt về hình thức; điều kiện nguồn và văn phong chưa đạt. |
| 6. DOCX | `AUDIT_COMPLETE_REBUILD_REQUIRED` | Đã kiểm tra cấu trúc, render và xem riêng đủ 53 trang; lỗi theo trang nằm trong DOCX_QA_REPORT.md. DOCX phải sinh lại từ Markdown đã duyệt. |

## 4. Kết quả đã kiểm chứng

### NotebookLM và nguồn

- MCP đã xác thực và truy cập đúng notebook cấu hình cục bộ.
- Notebook ban đầu không có nguồn dù ledger cũ ghi đã có.
- Sau đối soát có 19 nguồn sử dụng được; câu hỏi kiểm tra xác định Direct-hosted SMB dùng TCP 445 và nêu đúng giới hạn: cổng mở không tự chứng minh lỗ hổng, phiên bản SMB, bản vá hoặc khả năng khai thác.
- Không ghi ID notebook, cookie, token hoặc browser profile vào prompt bàn giao. Agent phải đọc chúng từ cấu hình cục bộ đã được gitignore.
- `S001`, `S003`, `S004`, `S009`, `S016`, `S019`: `RECHECK/NO` vì chưa có toàn văn hợp lệ trong notebook.
- `S014`: `RECHECK/ERROR` vì URL CISA cũ không nhập được.
- `S006` đã chuyển sang URL Microsoft Learn hiện hành; các nguồn chính thức bổ sung được ghi từ `S020` đến `S026`.

### Chương mẫu

- `CHAPTER_1.md` khoảng 8.536 từ, sát ngân sách 8.500 từ.
- Có 134 lượt dẫn; số IEEE `[1]`–`[19]` liên tục, không thiếu hoặc mồ côi về mặt cấu trúc.
- Không được coi cấu trúc trích dẫn đúng là bằng chứng đúng. Các nguồn `[1]`, `[3]`, `[4]`, `[9]`, `[14]`, `[16]`, `[19]` phải được nhập/xác minh hoặc thay thế; `[6]` phải cập nhật URL.
- Style lint có 18 cảnh báo: 17 câu dài và một kiểu mở đoạn lặp. Mỗi cảnh báo cần quyết định `FIX`, `KEEP_WITH_REASON` hoặc `FALSE_POSITIVE`; không sửa hàng loạt.

### Bản Word hiện có

- File: `work/do-an/BAO_CAO_DO_AN_CHUONG_1_2.docx`.
- OpenXML validation đạt; Word/OfficeCLI phân trang 53 trang, 475 đoạn, 15.446 từ.
- OfficeCLI phát hiện 323 vấn đề, chủ yếu là thiếu first-line indent, khoảng trắng liên tiếp và đoạn trống.
- Không phát hiện trường `TOC`; mục lục hiện tại không được coi là mục lục tự động.
- Có nhiều direct formatting; kết quả kiểm tra font giữa các công cụ chưa hoàn toàn đồng nhất nên phải xác minh bằng render và style audit, không kết luận chỉ từ một thống kê.
- Contact sheet: `.tmp/docx-qa/do-an/officecli-render/contact-sheet.png` (artifact tạm, có thể không được commit).
- Đã hoàn tất render native và xem riêng đủ 53 trang. Ảnh QA được giữ cục bộ và ignore; báo cáo lỗi theo trang đã lưu trong DOCX_QA_REPORT.md.

## 5. Quy tắc không được vi phạm

- Markdown đã duyệt là nguồn chuẩn; không sửa nội dung học thuật trực tiếp trong DOCX.
- Không chuyển cổng nếu chưa có phê duyệt rõ của người dùng và bản ghi trong `PROJECT_STATE.md`.
- Không bịa nguồn, DOI, trang, dữ liệu, log, ảnh, thí nghiệm, quan sát hoặc trải nghiệm của tác giả.
- NotebookLM chỉ hỗ trợ truy xuất; chỉ trích dẫn tài liệu gốc.
- Không tự coi các quyết định `PASS` cũ còn hiệu lực nếu audit mới đã mở lại artifact.
- Không tối ưu theo AI detector, không chèn lỗi và không “humanize” trước khi logic/bằng chứng ổn định.
- Giữ nguyên quy định HUIT và các quyết định người dùng đã khóa; repo tham khảo bên ngoài chỉ là lớp hỗ trợ.
- Không commit `.agents/mcp_config.json`, cấu hình NotebookLM cục bộ, cookie, token, profile trình duyệt, notebook ID riêng tư hoặc `CONTACTS.local.md`.

## 6. Trình tự tiếp tục duy nhất

1. Chạy `git status`; kiểm tra file tạm và quét bí mật trước khi stage.
2. Đối chiếu `SOURCE_LEDGER.md`, bibliography Chương 1 và nguồn thực có trong NotebookLM. Không đổi số IEEE hàng loạt khi chưa lập bảng ánh xạ cũ → mới.
3. Dùng `AUTHOR_VOICE.md` với lựa chọn 1B, 2A, 3A và điều chỉnh thuật ngữ đã được xác nhận. Không yêu cầu duyệt lại giọng khi tác giả đã chốt.
4. Sửa Chương 1 theo `PILOT_CHAPTER_REVIEW.md`: nguồn trước, logic sau, văn phong cuối; chạy citation audit và style lint lại.
5. Xin người dùng duyệt chương thí điểm. Chỉ sau đó mới chuyển sang ghép hoặc viết tiếp chương.
6. Sinh lại DOCX từ Markdown đã duyệt; tạo TOC tự động và style tập trung; không vá tiếp bản Word cũ.
7. Render từng trang bằng OfficeCLI/renderer, xem đủ 53 trang hoặc số trang mới, ghi lỗi rồi render lại sau sửa.
8. Chạy kiểm thử repository, kiểm tra secrets, cập nhật `PROJECT_STATE.md`, commit và push khi mọi file stage đều an toàn.

## 7. Lệnh kiểm tra chuẩn

```powershell
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python scripts/audit_ieee_citations.py work/do-an/CHAPTER_1.md --fail-on-error
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_1.md
```

Trước G6, chạy linter với `--publication --fail-on-error` theo hướng dẫn của skill.

## 8. Câu hỏi duy nhất cần người dùng trả lời tiếp

Yêu cầu người dùng mở `work/do-an/AUTHOR_VOICE_CALIBRATION.md`, sửa hoặc xác nhận tối thiểu ba cách diễn đạt và cho biết mẫu đó đã đúng giọng của họ chưa. Không tự vượt qua cổng này.

## Cập nhật mới nhất: giọng đã duyệt

Tác giả chọn 1B, 2A, 3A; bước 4 hoàn tất. Các yêu cầu xin duyệt giọng phía trên đã được đáp ứng, không hỏi lại. Tiếp tục kiểm nguồn và biên tập Chương 1 theo DEC-22, không tự duyệt chương hoặc dựng DOCX.
