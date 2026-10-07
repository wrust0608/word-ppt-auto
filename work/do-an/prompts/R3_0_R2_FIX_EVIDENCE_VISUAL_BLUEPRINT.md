# Antigravity — sửa R3-0 R2, chưa viết Chương 3

Bạn là executor của dự án **Xây dựng mô hình kiểm thử lỗ hổng SMB trên Windows bằng Kali Linux**. Làm trên branch `feature/ch3-redesign-evidence-first-r1`, tiếp tục candidate R1 `4f9d3f059f96d8b44ef6c83e0c2b20301245ce3e`. Không tạo roadmap mới và không chuyển R3-1.

Review độc lập R1: **FAIL / REWORK**. Đọc `work/do-an/R3_0_EVIDENCE_VISUAL_BLUEPRINT_EXTERNAL_REVIEW_R1.md` và sửa đủ F01–F09. Giữ bản review R1 để truy vết.

## 1. Checkpoint trước thực thi

Đọc HANDOFF.md, override đầu PROJECT_STATE, roadmap `ROADMAP_CH3_REDESIGN_EVIDENCE_FIRST_2026_10_07.md`, skill thesis-research-and-writing và references đúng nhiệm vụ. Những summary X7A1/X7J cũ là lịch sử; handoff trực tiếp và redesign roadmap hiện hành có ưu tiên.

Đọc final R3 evidence lock, `TIMEBASE_AND_CROSS_LAYER_LOCKS.md`, evidence-use policy, command-lineage matrix, canonical evidence map, raw Nmap outputs, truth matrix, Chương 2 locked và Chương 3 cũ đúng blob. Dùng ảnh/raw trực tiếp để xác minh; metadata và prose cũ không được ghi đè direct evidence.

Kiểm working tree trước thay đổi; không ghi đè công việc của người khác. Ghi candidate base và phạm vi diff.

## 2. Phạm vi được sửa

Sửa tại chỗ ba artifact R1 để giữ link hiện có, ghi rõ revision R2 và candidate R1 nguồn:

- `work/do-an/CH3_REDESIGN_EVIDENCE_VISUAL_BLUEPRINT_R1.md`
- `work/do-an/CH3_REDESIGN_TABLE_FIGURE_LEDGER_R1.md`
- `work/do-an/CH3_REDESIGN_CONTENT_MIGRATION_MAP_R1.md`

Được cập nhật `work/do-an/PROJECT_STATE.md` để ghi R2 đã sửa, chờ independent review. Được thêm một báo cáo thực thi R2 chứa bảng F01–F09 và kết quả kiểm tra. Không sửa báo cáo independent review R1.

Không sửa Chương 2, Chương 3 cũ, evidence/raw/manifest/checksum, truth locks, source ledger, ledger numbering cũ hay DOCX. Không viết prose Chương 3 mới. Không tạo crop/panel/vector artifact mới ở lượt này. Không chạy demo, không tạo Case A, không mở Chương 4. Numbering mới vẫn PROPOSED.

## 3. Yêu cầu sửa cụ thể

1. **F01 — Ảnh srv.sys:** mở ảnh thật. Đây là PowerShell, không có tab Properties/Details. Crop plan giữ FileVersion hiển thị, lệnh ghép bốn trường số và output `6.3.9600.16421`. Hình 3.7 dẫn đủ nguồn local, hotfix, official source; nhãn tổng hợp nằm ngoài pixel ảnh. Ngưỡng/KB dẫn source chính thức đã có, không dùng mapping nội bộ làm external authority.
2. **F02 — NSE04:** xóa `unsafe=0` không có trong measured command. Giữ UNKNOWN / NO USABLE SCRIPT RESULT và nguyên nhân chưa xác lập. Bản lệnh đầy đủ lấy từ đúng source; phân biệt operator command với Nmap-recorded argv. Nếu chỉ nêu lệnh rút gọn, ghi đó là dạng rút gọn, không gọi là literal command đã chạy.
3. **F03 — Case B:** thay kết luận không gián đoạn/không làm sập/bình thường/đàm phán thành point-in-time Running và danh sách dialect quan sát. Ghi rõ chưa chứng minh continuity, negotiation success/failure hoặc workload. TCP139 không đo lại; TCP445 OPEN nhưng không có `--reason` trong retest. Patch sau Case B có nguồn baseline + metadata, không phải ảnh After Local trực tiếp đo driver/hotfix.
4. **F04 — Case C:** bảng dialect ghi NOT MEASURED, không suy từ FILTERED thành kết quả `smb-protocols`. Giữ local SMB1/SMB2 ở hàng riêng. Remote MS17 giữ UNKNOWN / NO USABLE SCRIPT RESULT. Bỏ nguyên nhân nội bộ/script không gửi probe không được direct evidence xác lập.
5. **F05 — Nguồn/timebase:** final local Case C dùng đúng metadata locator, đặc biệt RUN4_PAUSE Section 21; phần troubleshooting trước đó không thành final evidence. Không dùng baseline để giả làm direct local retest. Đối chiếu Nmap/log bằng lineage, tuple IP/cổng/TCP SYN; không ghép đồng hồ. Giữ nguyên hai rule-label/tracker xung đột, không crop che, không quy thuộc exact named rule.
6. **F06 — Claim coverage:** bổ sung ma trận trong migration map: Claim ID, nguồn cũ + blob/locator, Evidence ID/tệp chính xác + cấp evidence, fact được giữ, đích mới, hành động, boundary. Tái sử dụng Evidence ID hiện có; mọi diễn giải trong index cũ vẫn phải đối chiếu raw/lock mới hơn. Map đủ từng hàng bảng và các claim quan trọng. Giữ DFS trên 2.0.2–3.0.2 và Leasing/Multi-credit trên 2.1–3.0.2. Giữ hai observation signing local/remote độc lập. Số dòng không thay claim coverage. Không tự tuyên bố 100% nếu chưa có denominator và đối soát.
7. **F07 — Narrative/flow:** Hình 3.1 tách nhánh host Case B và network Case C, mỗi nhánh retest rồi comparison. Không mô tả Case C kế thừa SMB1=False; không bịa rollback timestamp. Hình 3.14 biểu diễn hai vị trí độc lập, không giả thành cấu hình gộp đã thử. Kết luận Chương 3 chỉ dữ kiện đo/giới hạn trực tiếp; ý nghĩa rủi ro, compensating controls, defense-in-depth và khuyến nghị để Chương 4. Không dùng Case A làm nhãn canonical.
8. **F08 — Ledger:** sửa Old No. Hình port scan mới 3.4; ảnh B4 chưa có figure riêng trong Draft R2. Giữ mapping Hình 3.4 cũ (-sV) → panel A Hình 3.5 mới; Hình 3.2 cũ Firewall → supporting. Sửa bảng lệch cột Kali_to_Windows_Connectivity. Tính lại từ inventory: KEEP7/MERGE7/SUPPORTING15/RETIRE5; 7 evidence +4 comparison +3 explanatory =14 hình. Phân biệt 83 tổng, 78 primary/direct, 5 secondary. Bảng cũ 3.5/3.7 có 8 hàng dữ liệu: giải thích mọi gộp/tách, không ép 7 rồi mất dữ kiện. Dùng path chính xác theo thư mục, bỏ nguồn wildcard/shorthand mơ hồ. Tách ảnh gốc, presentation cũ và panel mới chưa tạo.
9. **F09 — State:** cập nhật đúng R3-0 R2 chờ independent review; Chương 3 architecture reopened, technical/evidence locks giữ; Chương 2 locked, numbering proposed, Chương 4 dormant. Không tự ghi USER APPROVED/PASS final/LOCKED_NUMBERING hay mở R3-1.

Đừng áp một khuôn đoạn máy móc cho tất cả mục. Thay cách kể chuyện phải giữ dữ kiện và giới hạn trước khi chỉnh văn phong.

## 4. Kiểm tra và bàn giao

Chạy validate_project và unittest theo AGENTS.md. Sau review bằng chứng/lập luận, chạy Vietnamese style linter trên ba artifact sửa; mỗi warning cần FIX/KEEP_WITH_REASON/FALSE_POSITIVE có lý do. Đây là tài liệu chuẩn bị nội bộ, chưa G6; không lấy điểm lint để chứng nhận nội dung.

Tính lại checksum 83 tệp; so blob Chương 2/Chương 3 cũ/DOCX với review R1. Kiểm numbering liên tục, mọi item có nguồn/đích/role/action/boundary, đủ 34 ảnh và tổng số phân loại đúng. Kiểm diff không vượt phạm vi. Không stage secret, local config hoặc artifact tạm.

Trả candidate commit, danh sách file sửa, bảng F01–F09 → vị trí sửa/căn cứ, bảng kiểm coverage claim/ảnh/bảng/hình, kết quả kiểm tra thực chạy và unresolved items. Nếu một bước chưa chạy, ghi rõ, không tự PASS.

**STOP tại R3-0 R2 chờ ChatGPT review.** Sau reviewer PASS còn cần người dùng chốt R3-0; chưa được viết 3.1–3.2.
