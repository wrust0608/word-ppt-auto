# R3-0 R3 — sửa lệnh và truy vết luận điểm

Bạn là executor Antigravity. Đọc HANDOFF.md, CURRENT OVERRIDE trong PROJECT_STATE.md, roadmap redesign và R3_0_EVIDENCE_VISUAL_BLUEPRINT_EXTERNAL_REVIEW_R2.md. Candidate R2: 94e82c0d5ff40726d4a2f7cdd5b4278f78972977.

Chỉ sửa ba artifact blueprint/ledger/migration hiện có cùng báo cáo thực thi R3 và PROJECT_STATE. Giữ tên ba artifact _R1 để bảo toàn liên kết, ghi revision R3 bên trong. Giữ mọi phần R2 đã đạt; không viết lại toàn bộ thiết kế.

1. Xử lý R2-F01: chép chính xác operator và recorded argv từ nguồn, sửa mô tả Get-NetTCPConnection trong ảnh baseline. Không thêm sudo/unsafe=0; bản rút gọn phải được đánh dấu.
2. Xử lý R2-F02: audit toàn bộ locator. Mọi nguồn phải là đường dẫn tệp thật, không wildcard/tên rút gọn mơ hồ; raw có locator, ảnh có vùng/khối; giữ Evidence ID đã định nghĩa và chỉ rõ nơi định nghĩa. Lập source inventory cho fact và từng hàng bảng cũ, ghi destination hoặc retire có lý do. Không dùng 41/41 để tự chứng minh đầy đủ khi denominator chưa xác lập. Ghi rõ arp-response Case C; thời lượng có thể retire có lý do. Không tạo số liệu mới.
3. Xử lý R2-F03 theo từng fact. Section 21 không chứa LanmanServer Running. Giữ truth lock nhưng ghi đúng nguồn khóa và lineage; nêu thiếu direct final service measurement nếu đúng. Không đổi canonical truth hay giả lập retest.
4. Xử lý R2-F04: giới hạn Get-HotFix inventory, ghi derived interpretation đúng loại; đồng bộ Bảng 3.5 và 3.7 đều 8 hàng.
5. Xử lý R2-F05: chạy lint ba artifact sau substantive review, lập disposition từng finding FIX/KEEP_WITH_REASON/FALSE_POSITIVE, bao gồm VI012 nhãn form. Không sửa style làm đổi chứng cứ.
6. Báo cáo R3 nêu before/after, đường dẫn/locator nguồn từng sửa, kiểm tra source inventory/coverage và các giới hạn còn mở. PROJECT_STATE ghi PENDING_R3_INDEPENDENT_REVIEW; không tuyên bố tất cả resolved trước kiểm tra.

Chạy validator, unit tests, git diff --check; đối chiếu 83 SHA-256 và blobs Ch2/Ch3 cũ/DOCX. Không sửa chứng cứ, Ch2, Ch3 cũ, DOCX; không crop/panel/Word/demo/Ch4; không mở R3-1. Không sửa báo cáo review R1/R2. Commit/push theo quyền executor hiện có, báo exact commit và diff scope, rồi STOP để reviewer kiểm. PASS chưa thay thế user chốt.
