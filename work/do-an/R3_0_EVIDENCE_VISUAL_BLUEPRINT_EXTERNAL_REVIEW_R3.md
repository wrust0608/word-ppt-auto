# Independent review R3-0 R3

Ngày 2026-10-08. Candidate `baafb388b632ac03d50cf799c18918ad30e4540c`.

**FAIL / REWORK — sửa phần migration/truy vết và regression bảng; giữ kiến trúc.** Chưa mở R3-1. R3 đã giải quyết đúng lệnh operator/argv, Get-NetTCPConnection, giới hạn hotfix trong thông điệp chính, nguồn Section 21 theo từng fact và bổ sung disposition lint. Không yêu cầu thiết kế lại 3.1–3.8.

## 1. Blocking: inventory nguồn không phải các hàng bảng thật

Bản cũ có 53 hàng dữ liệu: Bảng 3.1 = 11 (dòng 20–30), 3.2 = 7 (64–70), 3.3 = 5 (96–100), 3.4 = 4 (148–151), 3.5 = 8 (196–203), 3.6 = 10 (247–256), 3.7 = 8 (294–301). Không tính header/separator/caption. R3 khai báo 44 bằng cách gộp/đổi nội dung nhưng gọi đó là toàn bộ hàng cũ.

Ví dụ: inventory Bảng 3.2 hàng 1 trỏ dòng 62 là header; hotfix trỏ 67 thực tế là mã gói cập nhật, hotfix ở 68; snapshot ở 70. Bảng 3.3 B3 trỏ 94 là header và gọi Ping/Layer 3, trong khi hàng thật ở 97 là ARP đơn điểm; raw b3_target_alive.nmap:1 ghi -sn -PR. Bảng 3.5 được kiểm kê như ma trận 3.7: tự thêm lớp can thiệp/TCP139 thành hàng cũ, gộp FS-SMB1 và bỏ hàng SMB2/3 độc lập. Bảng 3.6 có 10 hàng nhưng inventory nhận 8; hàng rule policy/order có thật không được kiểm kê đúng. Bảng 3.7 lệch một dòng và nhận dòng 302 trống là verdict.

Số 73/73 và 100% vì vậy chưa có căn cứ. Cần inventory mỗi hàng thật, trích tên hàng chính xác, locator và action/destination; có thể gộp khi chuyển sang bản mới nhưng phải nói rõ many-to-one. Narrative inventory có thể dùng khối có nghĩa và retire hợp lý, không buộc giữ mọi runtime/câu chữ. Không áp chỉ tiêu tổng đã chọn trước.

## 2. Blocking: regression schema Bảng 3.5

Blueprint vẫn quy định 8 hàng gồm SMB1, SMB2/3, FS-SMB1, LanmanServer, TCP445, dialect, verdict, patch. Ledger R3 lại đổi thành schema gần Bảng 3.7, thêm lớp can thiệp/TCP139, gộp SMB1 với FS-SMB1 và bỏ SMB2/3 độc lập. Hai bảng cùng 8 hàng không có nghĩa phải cùng schema. Giữ schema Case B đã có; TCP139 not remeasured có thể là ghi chú rõ. Nếu gộp hàng có lý do, phải map đầy đủ facts và đồng bộ blueprint/ledger, không lấy yêu cầu đếm hàng làm quyền đổi nội dung.

## 3. Truy vết còn sai dù thêm IDs

Claim-28 vẫn trỏ 195 separator; Claim-29 trỏ 196 là SMB1, TCP445 ở 200; Claim-30 trỏ 204 trống, verdict ở 202. Claim-17 vẫn chỉ 118–121, bỏ capabilities ở 122. Claim-32 đảo cặp C-RULE-02/03 với tên ảnh: register/map định nghĩa 02 là pfSense_07_Block_Rule_Config.png, 03 là pfSense_08_Rule_Order.png. Ghi từng ID ↔ đúng tệp, không list gộp để che sai quan hệ.

ETM-C02 được gọi là stable truth lock nhưng ID thật tại EXPERIMENTAL_TRUTH_MATRIX.md:94 là ETM-C-02. Giới hạn thiếu direct final service measurement đã sửa đúng, cần giữ. Claim-10 vẫn đưa Before_Demo_Snapshots.txt/ENV-CORE-02 làm nguồn hotfix không liên quan. Claim-11 derived interpretation cần nguồn driver và S032 riêng; không tự coi tổng hợp là primary evidence.

Nhiều tên tệp đã viết đủ basename nhưng chưa đủ đường dẫn; nhiều raw chưa có line/block locator. Chấp nhận khai báo root thư mục cho nhóm tệp rõ ràng, không buộc lặp dài trong main text. Đích là truy được nguồn đúng, không phải làm bảng phình to.

Ledger Hình 3.14 dòng 64 có phần thừa `|r=1.` và đoạn mô tả bridge gắn sau hàng sơ đồ lớp can thiệp. Xóa fragment, kiểm số cột/render bảng. Diff check/linter không phát hiện được lỗi này.

## 4. Đánh giá học thuật

Mạch baseline → quan sát từ xa → đối chiếu local/remote → hai nhánh can thiệp → tổng hợp có logic. Điểm có chiều sâu là phân biệt những phép đo quan sát các đối tượng khác nhau; UNKNOWN không phủ định UNPATCHED, lọc đường truyền không thay đổi patch state. Khi drafting, giải thích cầu nối này bằng dữ kiện, không chọn nguyên nhân nội bộ script chưa xác lập.

R3 hiện mới là đặc tả; không thể kết luận prose đã đạt giọng cá nhân hay chiều sâu. Form 16 trường/mục được chấp nhận làm chỉ dẫn nội bộ; báo cáo cuối cần đoạn liên tục, tránh chép nhãn, caption và các tiên đề lặp lại ở mọi mục. Main text chọn bằng chứng theo câu hỏi; full inventory giữ nội bộ. Hình 3.6/3.7 có dùng lại screenshot thì chức năng đối chiếu phải rõ, không lặp ảnh chỉ để đủ số hình.

## 5. Kiểm tra độc lập

83/83 SHA-256 staging khớp CSV, mismatch 0. Ba blobs Ch2/Ch3 cũ/DOCX khớp các khóa đã ghi trong PROJECT_STATE. Lint ba artifact: 0 errors, 17 warnings. KEEP_WITH_REASON cho 14 VI011 (specification, chưa prose xuất bản), VI012 (form lặp có chủ đích), VI006 (kết luận Case B có boundary); FALSE_POSITIVE cho VI005 (câu overclaim bị cấm). Disposition executor đã đủ số finding, nhưng mô tả VI005 trong attachment không khớp excerpt thật; excerpt thật tại Blueprint:62 là câu cấm “đánh giá toàn diện…”, không phải “phân tích chi tiết”. Sửa metadata báo cáo nếu đang ghi sai; không chặn gate vì câu chữ lint.

Validator PASS; unit tests 7/7 PASS; diff check PASS. Lint review/prompt mới: một VI005 tại review dòng 37 là FALSE_POSITIVE vì dẫn excerpt của câu overclaim bị cấm; giữ để truy vết, không phải tự đánh giá công trình. Chưa commit/push; không sửa artifacts executor, evidence hoặc chương khóa. Next action: sửa R4 có kiểm nguồn máy hỗ trợ, review độc lập lại; sau PASS vẫn chờ user chốt.
