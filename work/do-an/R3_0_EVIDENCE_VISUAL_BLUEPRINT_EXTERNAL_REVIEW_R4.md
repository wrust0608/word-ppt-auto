# Independent review R4 — 2026-10-08

Candidate: `ac53515e766efa8ef4eba550183df13589d61997`.

**FAIL / REWORK.** Kiến trúc giữ nguyên; nguồn chuyển dịch vẫn chứa dữ kiện sai mới. Không mở R3-1. Không dùng kết quả kiểm repository để thay kết luận nguồn.

## Phần đã đạt

53 hàng bảng được định danh đúng vị trí, schema Bảng 3.5 có SMB1/SMB2/FS-SMB1 riêng và Bảng 3.7 có chức năng tổng hợp riêng. C-RULE-02/03 và ETM-C-02 đã sửa; fragment ledger đã bỏ. Lệnh operator/argv và giới hạn Section 21 tiếp tục được giữ. Mạch baseline → khảo sát → đối chiếu → hai nhánh độc lập → tổng hợp phù hợp; chưa phải prose để chứng nhận giọng tác giả.

## F01 — Dữ kiện mới không khớp nguồn (blocking)

Migration SRC-TBL-18, SRC-NAR-04 và Claim-12 đổi snapshot thành `BASE-CLEAN-2026-10-04`. Nguồn Before_Demo_Snapshots.txt ghi tên `Before Demo`, không có tên mới. Phục hồi exact name; không tự đặt alias giống một snapshot thật.

SRC-TBL-20 và Claim-14 ghi B3 latency 0.00037s, MAC 08:00:27:0B:DA:B7. Raw scenario1/b3_target_alive.nmap:3–4 ghi 0.00034s và 08:00:27:55:71:CE. Nếu không cần các giá trị này để lập luận thì bỏ khỏi main narrative có lý do; nếu giữ phải chép đúng và cite raw. Không gọi là nguyên vẹn khi thêm số liệu khác.

## F02 — Nguồn hotfix bị gán sai (blocking)

SRC-TBL-16 và Claim-10 trỏ Final_PreDemo_Audit.txt Section 3 cho danh sách sáu hotfix. Tệp này có trạng thái driver/ngưỡng nhưng không có Get-HotFix hay danh sách sáu KB. Dùng Windows_MS17010_02_Hotfix.png và artifact thực sự có inventory. Giữ ranh giới không ghi nhận trong inventory đã thu thập, không khẳng định toàn bộ lịch sử update.

## F03 — Công cụ/coverage chưa chứng minh điều báo cáo tuyên bố

scratch/build_migration_map.py chứa chuỗi Markdown viết sẵn rồi ghi ra tệp; không đọc/parsing CHAPTER_3_DRAFT_R2.md để sinh exact rows. Đó là generator, không phải chứng cứ trích xuất máy. 53 labels/locators hiện khớp đếm bảng nhưng báo cáo phải nói đúng cách tạo/kiểm. Cần extractor read-only từ nguồn và so sánh line/label với inventory; không chạy generator để ghi đè trong audit.

79 mục đang gồm 53 rows + 26 narrative blocks; thời lượng retire nằm bên trong SRC-NAR-23 vốn REUSE, không có mục RETIRE riêng. Không thể nói 78 MOVE + 1 RETIRE như 79 action đơn nhất. Hoặc tách thành đơn vị riêng/tính lại, hoặc ghi block có partial retire; không tăng số cho đẹp. Coverage chỉ trong inventory đã xác lập, không lời đảm bảo tuyệt đối mọi fact đã được bảo toàn.

## F04 — Locator vẫn cần kiểm nội dung

Claim-28 trỏ dòng196 của bản cũ là SMB1, không phải TCP139 not remeasured. Ghi rõ đây là giới hạn bổ sung theo phạm vi lệnh/locks; không gán nó cho hàng cũ không chứa thông tin. Claim-29 raw dòng5 là header, kết quả port ở6; muốn chứng minh thiếu --reason phải trỏ dòng1. Claim-30 đoạn4–6 chưa bao toàn bộ raw để xác lập không có script results; dùng full output1–9. Ghi đúng locator/loại suy luận, không chỉ sửa số dòng cho khác bản trước.

## Hướng sửa

Giữ phần đã đạt. R5 chỉ sửa dữ kiện/nguồn/locator, công cụ kiểm và cách báo coverage; không viết lại blueprint. Dùng WRITING_POLICY.md: chọn dữ kiện phục vụ câu hỏi, không tự thêm chi tiết để làm bảng có vẻ sâu. Lý do chưa PASS là source attribution và giá trị sai, không phải sở thích văn phong.

## Kiểm tra độc lập

83/83 staging hashes khớp, mismatch0; blobs Ch2/Ch3 cũ/DOCX giữ đúng khóa. Validator PASS, tests7/7 PASS, diff check PASS. Chưa sửa artifact executor/evidence/chương; chưa commit/push. Các kiểm tra không xác nhận tính đúng của những claim trên. Next: executor sửa hẹp R5, reviewer kiểm; PASS vẫn cần user chốt.
