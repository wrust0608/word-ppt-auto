# Antigravity — R3-0 R5, sửa dữ kiện và kiểm nguồn

Đọc WRITING_POLICY.md, CURRENT OVERRIDE và review R4. Candidate ac53515e766efa8ef4eba550183df13589d61997. Giữ schema/kiến trúc đã đạt; không viết lại toàn bộ artifact.

1. Sửa F01 toàn bộ occurrences: snapshot tên thật Before Demo; B3 raw latency0.00034s và MAC08:00:27:55:71:CE hoặc bỏ chi tiết không cần với quyết định retire rõ. Không thêm alias/số mới.
2. F02: hotfix chỉ dùng artifact thật có inventory; Final_PreDemo_Audit không có danh sách hotfix. Đối chiếu pixel/khối trước cite. Phân loại diễn giải và giới hạn inventory đúng.
3. F03: tạo extractor/checker read-only đọc CHAPTER_3_DRAFT_R2.md, trích exact labels/lines và so sánh inventory. build_migration_map là generator chứa content viết sẵn; không mô tả là extractor. Audit tất cả con số/tên mới trong migration so với đúng nguồn. Báo count/action đúng: partial retire trong block không biến thành1 mục riêng. Không tuyên bố100% nếu chưa kiểm denominator/facts.
4. F04: kiểm toàn bộ locator có hỗ trợ claim, gồm Claim28/29/30 trong review. Giới hạn mới từ raw/locks phải ghi là bổ sung, không giả làm nội dung hàng cũ. Ghi kết quả kiểm đường dẫn, ID↔file và exact source sample, không chỉ số lượng.
5. Báo cáo R5 và state PENDING_R5_INDEPENDENT_REVIEW; ghi phần đã sửa và hạn chế. Chạy substantive review, lint/disposition, validator/tests/diff,83hash/blobs. Không sửa báo cáo review lịch sử, chứng cứ/chương khóa/DOCX. Không crop/panel/demo/Ch4/R3-1. Commit/push theo quyền executor, báo exact commit và kết thúc lượt bằng final handover; không để UI Working sau khi hoàn tất.
