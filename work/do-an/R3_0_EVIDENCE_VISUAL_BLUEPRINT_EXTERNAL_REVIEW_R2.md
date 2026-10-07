# R3-0 — Independent review R2

Ngày: 2026-10-08. Candidate: `94e82c0d5ff40726d4a2f7cdd5b4278f78972977`.

**Kết luận: FAIL / REWORK, phạm vi sửa hẹp. Chưa chốt R3-0; chưa mở R3-1.** Báo cáo thực thi không thay thế việc đối chiếu nguồn. Các sửa tốt của R2 được giữ, không yêu cầu thiết kế lại toàn bộ.

## Những phần đã đạt

Hai phiên bản srv.sys được phân biệt đúng; luồng Case B/Case C là hai nhánh độc lập; Running của Case B được giới hạn tại thời điểm kiểm tra; TCP 139 không đo lại; Case C dialect NOT MEASURED và MS17 UNKNOWN được tách khỏi trạng thái filtered. CF-11 và giới hạn timebase vẫn giữ. Kiểm kê 34 ảnh khớp 7 KEEP, 7 MERGE, 15 SUPPORTING, 5 RETIRE; đề xuất 14 hình gồm 7 evidence, 4 comparison, 3 explanation. Chương 4 chưa mở.

## Các điểm cần sửa

### R2-F01 — Lệnh quét và nội dung ảnh chưa đúng nguồn (blocking)

Blueprint dòng 298–299 thêm sudo vào operator command và lược mất tham số nhưng gọi là recorded argv. Ảnh Scenario2_NSE04_MS17010.png và manifest ghi operator:

`nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`

Raw `chapter3/evidence/scenario2/NSE-SMB-04_ms17010.nmap:1` ghi:

`/usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`

Chép nguyên văn hoặc ghi rõ bản rút gọn, không thêm sudo. Không có unsafe=0. Blueprint dòng 131 và ledger mô tả netstat trong ảnh baseline, nhưng ảnh thật dùng Get-NetTCPConnection. Sửa mô tả crop theo pixel thật.

### R2-F02 — Ma trận chưa chứng minh coverage/truy vết đầy đủ (blocking)

41 dòng không tự chứng minh 100% nội dung cũ. Claim-14 trỏ dòng 95 là separator thay vì hàng B4 dòng 98; Claim-15 trỏ dòng 96 là B2 thay vì fingerprint dòng 99; Claim-16 trỏ dòng 97 là B3 thay vì hàng NSE dòng 100; Claim-17 bỏ dòng 122 chứa capabilities. Claim-28 dùng dòng 195 separator; Claim-30 dùng dòng 204 trống. Phải kiểm lại toàn bộ locator, không chỉ các ví dụ này.

Claim-20 dùng tên 02_protocols.nmap/03_signing.nmap không tồn tại; Claim-31 dùng 04_Bridge.png/05_Bridge_Filtering.png không tồn tại; ledger có 02_Action.png/03_After_Local.png tương tự. Các tên NSE-SMB-04_ms17010.nmap không kèm case bị mơ hồ vì tồn tại trong ba thư mục. Blueprint còn b{2..6}_*.nmap. Dùng đường dẫn repo đầy đủ và locator raw/khối nội dung; Evidence ID có sẵn phải trỏ artifact định nghĩa ID, không đặt tên tệp vào cột ID rồi coi là đã định danh.

Lập inventory các fact/hàng bảng cũ → giữ/chuyển/rút gọn/retire có lý do → destination mới và nguồn. Ví dụ host up with arp-response ở dòng 262 chưa có fact đích rõ; thời lượng 0.51 giây dòng 278 có thể retire nhưng phải ghi quyết định. Phân biệt bảng/caption/diễn giải trùng lặp; không buộc giữ mọi câu chữ. Chỉ công bố coverage khi denominator có inventory kiểm được.

### R2-F03 — Section 21 bị gán dữ kiện không có (blocking)

Claim-37 gán LanmanServer Running cho Section 21 của RUN4_PAUSE_STATE_REPORT.txt. Section 21 bắt đầu dòng 333; block Windows dòng 376–384 có SMB1/2=True, listeners, hai phiên bản driver và UNPATCHED, nhưng không có LanmanServer. Running ở dòng 162 thuộc đoạn trước, không phải final closure.

Giữ technical truth lock Running; tách nguồn theo từng fact. Truy nguồn khóa ETM-C02 trong EXPERIMENTAL_TRUTH_MATRIX.md và lineage hỗ trợ; nêu giới hạn nếu không có phép đo dịch vụ trực tiếp cuối lượt. Không đổi truth lock, không nâng đoạn troubleshooting thành final retest, không giả định baseline là final evidence.

### R2-F04 — Wording và số hàng cần đồng bộ

Blueprint dòng 155, Claim-10 và caption/hình liên quan: đổi khẳng định thiếu hoàn toàn bản vá thành không ghi nhận KB4012213/KB4012216 trong local Get-HotFix inventory đã thu thập. Inventory bổ trợ, không đại diện toàn bộ lịch sử cập nhật. Phân loại UNPATCHED dựa numeric driver và ngưỡng chính thức; claim tổng hợp phải ghi là diễn giải có nguồn, không coi chính nó là primary observation.

Blueprint dòng 443/445 vẫn nói 7 tiêu chí/7 hàng, nhưng liệt kê 8. Đồng bộ Bảng 3.5 là 8 hàng; Bảng 3.7 cũng 8 hàng.

### R2-F05 — Lint disposition chưa đủ

Linter độc lập ghi 16 cảnh báo: 13 VI011, 1 VI005, 1 VI006, 1 VI012. Báo cáo executor xử lý 15, bỏ VI012 tại Blueprint dòng 42 (18 nhãn Đề mục theo form). KEEP_WITH_REASON cho nhãn lặp có cấu trúc; không sửa form chỉ để hết cảnh báo. VI005 là câu bị cấm trong checklist: FALSE_POSITIVE. VI006 tại dòng 464 giữ với lý do kết luận Case B có ranh giới cụ thể. 13 VI011 giữ với lý do đây là đặc tả/ma trận, chưa là prose xuất bản; kiểm lại khi drafting. Ghi từng finding/location thay vì một tổng số thiếu mục.

## Kiểm tra độc lập và giới hạn

- 83/83 staged SHA-256 khớp CSV; mismatch 0.
- Blob Ch2: 55ffb13acb3398c7ab29d6d5abbb369e5d26f3d0; Ch3 cũ: 40d2a895bc970f88d7260b3138b8a701f5eb0a8c; DOCX cũ: 276278b1fb3e2f74acd11f6cb42b66df8c9b0ca9. Không thay đổi.
- Đã đối chiếu tài liệu R2, raw/closure và ảnh liên quan các finding; không tuyên bố đã visual QA toàn bộ 34 ảnh.
- Project validator PASS; unit tests 7/7 PASS; git diff --check PASS. Lint hai artifact review/prompt mới không có finding. Các kiểm tra tự động này không chứng minh source attribution đúng; kết luận gate dựa các finding phía trên.

Next action duy nhất: Antigravity sửa R3-0 theo prompt R3, rồi reviewer kiểm độc lập. Sau PASS vẫn cần người dùng chốt trước khóa numbering/mở R3-1.
