# R3-0 — Independent review of evidence and visual blueprint R1

- Ngày review: 2026-10-08 (Asia/Saigon).
- Candidate: `4f9d3f059f96d8b44ef6c83e0c2b20301245ce3e`.
- Base roadmap: `170aa24293b2cf8e579abb1ecf60920bca418bd9`.
- Branch: `feature/ch3-redesign-evidence-first-r1`.
- Verdict: **FAIL / REWORK — cần sửa R3-0 trước khi trình người dùng chốt**.
- Current gate: `R3_0_REVISE_BLOCKING`; chưa mở R3-1.

## 1. Kết luận

Ba tài liệu R1 đã bám kiến trúc 3.1–3.8 và đề xuất sử dụng ảnh theo nhóm bằng chứng, so sánh và sơ đồ giải thích. Candidate chỉ thêm đúng ba tài liệu R3-0. Chương 2, Chương 3 cũ, DOCX và evidence không bị sửa.

R1 chưa đủ điều kiện duyệt. Hướng dẫn crop có chỗ mô tả sai ảnh thật; các kết luận được phép viết vượt khỏi giới hạn đã khóa; bảng đối chiếu chưa phân biệt đầy đủ phép đo không thực hiện với phép đo không có kết luận. Ledger và trạng thái dự án cũng cần sửa. Giữ kiến trúc đã duyệt, sửa ba tài liệu chuẩn bị; không cần thiết kế lại roadmap hay chạy thêm demo.

## 2. Căn cứ và phạm vi kiểm tra

Đã đối chiếu handoff người dùng ngày 07/10/2026, roadmap redesign, state hiện có, ba artifact R1, Markdown Chương 2/3, truth matrix, final R3 evidence lock, timebase/cross-layer locks, evidence-use policy, command-lineage matrix, evidence index và raw output liên quan.

Đã mở trực tiếp các ảnh: `Windows_MS17010_01_SrvSysVersion.png`, `Windows_PreDemo_01_Network_SMB.png`, `Scenario1_B6_SMB_NSE_A.png`, `pfSense_07_Block_Rule_Config.png`, `pfSense_08_Rule_Order.png`, `pfSense_10_Block_Log_CANONICAL.png` và bản trích có sẵn `presentation/3_5/Hinh_3_11_pfSense_Block_Log.png`. Ảnh log gốc rất dài; bản hiển thị thu nhỏ không đủ đọc chi tiết, nên đối chiếu các dòng log bằng bản trích có sẵn. Đây là review kế hoạch sử dụng ảnh; không tuyên bố đã kiểm tra thị giác toàn bộ 34 ảnh, crop mới, layout panel hoặc trang Word mới.

Kiểm tra độc lập:

| Hạng mục | Kết quả |
|---|---|
| Working tree trước review | Sạch |
| Phạm vi candidate so với roadmap commit | Chỉ thêm ba artifact R3-0 |
| Checksum evidence staging | 83/83 khớp `CHAPTER_3_EVIDENCE_SHA256.csv`; 0 mismatch |
| Phân hạng evidence | 78 primary/direct; 5 secondary metadata/closure |
| Số ảnh PNG trong evidence staging | 34 |
| Blob Chương 2 | `55ffb13acb3398c7ab29d6d5abbb369e5d26f3d0` |
| Blob Chương 3 cũ | `40d2a895bc970f88d7260b3138b8a701f5eb0a8c` |
| Blob DOCX cũ | `276278b1fb3e2f74acd11f6cb42b66df8c9b0ca9` |
| SHA-256 DOCX cũ | `3c9ac6b6bfa1d259f92856a6c6b48ec398178e927f9beb06f5c0c37749dd3db2` |

Checksum chứng minh các tệp staging giữ nguyên so với manifest đã khóa; không thay thế review nội dung và không phải audit lại ZIP gốc.

## 3. Các điểm bắt buộc sửa

### F01 — Crop srv.sys phải mô tả đúng PowerShell và giữ hai phiên bản

Vị trí: Blueprint dòng 153, phần 3.2.2; Ledger Hình 3.3 và Hình 3.7.

R1 yêu cầu cắt tab Details của hộp thoại Properties. Ảnh thật là cửa sổ PowerShell, hiển thị cả FileVersion `6.3.9600.16384` và phép ghép bốn trường số cho kết quả `6.3.9600.16421`. Hướng dẫn hiện tại vừa chỉ tới giao diện không tồn tại, vừa không bắt buộc giữ phép đo số quan trọng nhất.

Sửa: giữ lệnh và output FileVersion, lệnh ghép bốn trường và kết quả số. Phân biệt ảnh gốc với presentation crop cũ và panel mới dự kiến. Hình 3.7 phải dẫn đủ nguồn local numeric, hotfix và source mapping; không chỉ ghép FileVersion hiển thị rồi gắn nhãn UNPATCHED. Các nhãn tổng hợp đặt ngoài pixel evidence. Dẫn nguồn Microsoft đã có trong ledger, đặc biệt S032, khi dùng ngưỡng bản vá; file mapping nội bộ không thay thế nguồn chính thức.

### F02 — Bỏ chế độ unsafe=0 không có trong lệnh thực nghiệm

Vị trí: Blueprint dòng 311, phần 3.4.2.

Raw `scenario2/NSE-SMB-04_ms17010.nmap` và command-lineage matrix không ghi `--script-args unsafe=0`. Không được gắn tùy chọn này vào phép đo để giải thích kết quả. Giữ mô tả: cổng 445 OPEN, scan hoàn tất, không có usable script verdict; dự án phân loại UNKNOWN / NO USABLE SCRIPT RESULT; nguyên nhân chưa xác lập.

### F03 — Khôi phục giới hạn Case B về dịch vụ và phương ngữ

Vị trí: Blueprint dòng 365, 376, 398, 414; Migration dòng 110–116; Ledger Hình 3.9 và mapping nguồn.

Các câu “không làm gián đoạn”, “không làm sập dịch vụ”, “phản hồi bình thường” và “danh sách đàm phán” vượt quá dữ kiện point-in-time và danh sách dialect được quan sát. Chương 3 cũ dòng 188 đã ghi rõ giới hạn này.

Sửa: LanmanServer được ghi nhận Running trước và sau tại thời điểm kiểm tra; retest liệt kê `2.0.2, 2.1, 3.0, 3.0.2`, không có NT LM 0.12. Không khẳng định phiên SMB thành công/thất bại, dịch vụ liên tục hoặc workload SMB2/3 đã kiểm chứng. Giữ TCP139 NOT REMEASURED, TCP445 OPEN không có dữ liệu `--reason` trong retest Case B. Patch state sau Case B kế thừa baseline và metadata lượt chạy; ảnh After Local không đo lại srv.sys/hotfix.

### F04 — Phân biệt Case C không đo dialect với không tiếp cận được cổng

Vị trí: Blueprint 3.7.1 dòng 550–557; Migration các hàng so sánh; Ledger Bảng 3.7.

Trong Case C, canonical retest có scan cổng và MS17-010; không có phép đo `smb-protocols` tương ứng. R1 điền các ô SMBv1/SMB2/3 là “Không tiếp cận được”, trong khi bảng cũ ghi “Không có phép đo tương ứng trong Case C”. Kết quả FILTERED của scan cổng không thay thế một phép đo dialect chưa chạy.

Sửa: ô phương ngữ từ xa Case C ghi **KHÔNG CÓ PHÉP ĐO TƯƠNG ỨNG / NOT MEASURED**. Local SMB1=True/SMB2=True nằm ở hàng riêng. Scan MS17-010 giữ UNKNOWN / NO USABLE SCRIPT RESULT; không thay bằng một classification mới UNKNOWN/Filtered. FILTERED là trạng thái cổng. Bỏ suy diễn “script không thể gửi gói thăm dò” hay nguyên nhân nội bộ của script, kể cả khi summary/metadata cũ có diễn giải đó.

### F05 — Chỉ rõ nguồn cuối lượt Windows và giới hạn đối chiếu thời gian

Vị trí: Blueprint 3.6.3 dòng 516–538; Ledger Hình 3.13 và Bảng 3.6.

R1 đặt Windows baseline audit trong direct evidence cho kết luận về Windows sau Case C. Baseline không phải phép đo local mới sau Case C. Nguồn ghi nhận cuối lượt là metadata/closure, gồm **Section 21** của `case_c/RUN4_PAUSE_STATE_REPORT.txt`; phần trước là troubleshooting. Không nâng nguồn này thành direct screenshot proof.

Sửa: mỗi fact cuối lượt phải trỏ tới phần nguồn hỗ trợ và cấp evidence tương ứng. Những câu “tương ứng thời điểm quét” cần ghi rõ đối chiếu theo run lineage và tuple nguồn/đích/cổng/TCP SYN, không khẳng định cùng wall clock. Được giữ kết luận có giới hạn rằng lưu lượng SMB SYN phù hợp bị Block trên đường pfSense trong lượt canonical. Giữ nguyên cả hai nhãn rule/tracker xung đột; ảnh log không chứng minh đích danh configured Block rule matched.

### F06 — Chưa chứng minh được yêu cầu ánh xạ 100% claim/evidence

Vị trí: Migration dòng 94 và 172–174; Blueprint 3.3.2; Ledger toàn bộ Source canonical/Supported claim.

Migration map có các khối dòng và tên tệp nhưng chưa có ma trận claim → Evidence ID → source locator → đích → boundary đủ kiểm toán. Ví dụ khối nguồn dòng 118–125 chứa `smb2-capabilities`, nhưng hàng migration tóm tắt năm dialect/signing/os-discovery bỏ phần giá trị capabilities cụ thể. Blueprint chỉ nêu DFS/Leasing/Multi-credit chung; Ledger Bảng 3.3 và caption/crop Hình 3.5 không bảo đảm giữ nội dung đó. Không thể dùng một câu tự xác nhận “100%” để chứng nhận coverage.

Sửa: lập danh mục claim có ID ổn định, dẫn Evidence ID sẵn có hoặc ID tệp từ manifest checksum, kèm locator raw/XML/local/visual hoặc metadata Section 21. Giữ DFS trên 2.0.2–3.0.2; Leasing/Multi-credit trên 2.1–3.0.2 ở Bảng 3.3 hoặc đoạn tương ứng. Nếu crop Hình 3.5 giữ capabilities thì ghi rõ; nếu đưa sang bảng thì giữ raw locator. Cả local signing flags và remote signing 3.0.2 phải giữ riêng. Kiểm nguồn dòng từ đúng blob: lệnh Get-Content đếm 317 dòng; con số 318 có thể do cách tính newline nhưng phải khai báo cách đếm, không dùng số dòng thay claim coverage.

### F07 — Sơ đồ phải thể hiện hai ca độc lập và giữ ranh giới Chương 3

Vị trí: Blueprint 3.1.2, 3.4.2 dòng 330, 3.5.3, 3.7.2; Ledger Hình 3.1 và 3.14; Migration phần dẫn nhập và kết luận.

Sơ đồ R1 mô tả tuyến Baseline → Scenario 1 → Scenario 2 → Case B → Case C. Cần phân biệt thứ tự kể chuyện với trạng thái thí nghiệm: Case C ghi SMB1=True, không kế thừa SMB1=False của Case B. Sơ đồ Hình 3.1 phải tách hai nhánh can thiệp từ trạng thái xuất phát phù hợp; mỗi nhánh có retest, rồi comparison. Điểm phục hồi là context có nguồn; không tự bịa thời điểm rollback cụ thể.

Giữ các câu về kết quả đo. Chuyển các chỉ dẫn viết “nguy cơ ... trong nhân”, “yêu cầu cấp thiết ... đa tầng”, compensating controls/remediation và khuyến nghị sang ghi chú thuộc Chương 4; không đưa chúng vào kết luận section Chương 3. Hình 3.14 thể hiện hai vị trí riêng, không làm người đọc tưởng đã đo cấu hình gộp Case B+C. Patching chỉ là nội dung đối chiếu/thảo luận, tránh gọi thành “biện pháp Case A” trong luồng canonical. Không có Case A experiment.

### F08 — Ledger cần thống nhất số hiệu, nguồn và thống kê

Vị trí: Ledger dòng 49, 103, 140, 167–176; Blueprint dòng 674–680.

Hình port scan mới 3.4 dùng ảnh Scenario1_B4_SMB_Ports, chưa từng là Hình 3.4 trong Draft R2. Hình 3.4 cũ là fingerprint -sV; Hình 3.2 cũ là Windows Firewall. Sửa cột Old No. của hình port thành “không có hình riêng trong Draft R2; thêm từ evidence sẵn có”, hành động NEW evidence presentation, không phải NEW experiment.

Thống kê từ 34 hàng inventory: KEEP=7, MERGE=7, SUPPORTING=15, RETIRE=5. R1 ghi KEEP=6, SUPPORTING=16. Hàng Kali_to_Windows_Connectivity thừa một ô `baseline/`, làm lệch cột. Hình đề xuất có 7 evidence, 4 comparison, 3 explanatory =14; không ghi 6 evidence. Bảng cũ 3.5 và 3.7 đều có 8 hàng dữ liệu, trong khi R1 nhiều chỗ nói 7 tiêu chí; mọi việc gộp/tách phải có mapping rõ, không bỏ dữ kiện.

Chuyển shorthand/wildcard nguồn thành đường dẫn chính xác theo scenario/case để tránh nhầm các tệp trùng basename. Tách ảnh gốc, crop/panel cũ và crop/panel mới chưa tạo. Toàn bộ 83 tệp không đều là direct evidence: 5 tệp là secondary metadata/closure.

### F09 — Đồng bộ bộ nhớ hiện hành

Candidate không cập nhật PROJECT_STATE. Summary cũ vẫn ghi Chương 3 final locked và chờ đánh giá DOCX; HANDOFF.md còn trỏ X7A1. Handoff trực tiếp của người dùng và roadmap redesign mới có ưu tiên cao hơn.

Review này bổ sung override state hiện hành: Chương 3 **architecture reopened**, technical/evidence locks giữ nguyên; numbering mới PROPOSED; R3-0 cần sửa. Không xóa DEC/lịch sử khóa cũ và không tự coi blueprint user-approved. Prompt sửa phải cập nhật state sau thực thi nhưng không được đánh dấu R3-1 authorized.

## 4. Điểm giữ nguyên

- Kiến trúc 3.1–3.8 do người dùng chốt.
- Ý tưởng sơ đồ luồng, panel Before/Action/After, topology bridge và đối chiếu remote/local.
- Giữ 34 ảnh trong kho; SUPPORTING/RETIRE chỉ thay vai trò trong main text, không xóa evidence.
- Ranh giới UNKNOWN, bản vá, Case B TCP139 và CF-11.
- Không sửa Chương 2; không viết prose mới, tạo crop/panel, chạy demo hoặc rebuild Word trong lượt sửa R3-0.

## 5. Bước tiếp theo duy nhất

Antigravity sửa R3-0 theo `prompts/R3_0_R2_FIX_EVIDENCE_VISUAL_BLUEPRINT.md`, trả candidate và bảng F01–F09 → vị trí sửa/căn cứ. ChatGPT review độc lập R2. Chỉ sau reviewer PASS và người dùng chốt R3-0 mới được khóa numbering và mở R3-1.

## 6. Kiểm tra hoàn tất lượt

- `validate_project.py`: PASS.
- Unittest: 7/7 PASS.
- `git diff --check`: PASS.
- Style lint hai tài liệu QA/prompt mới: 0 error, 1 warning VI012 tại review dòng 42 (các dòng 42, 50, 56, 64, 72, 88 cùng mở “Vị trí: Blueprint”). Quyết định **KEEP_WITH_REASON**: đây là nhãn locator nhất quán của từng finding trong biểu mẫu review, giúp executor tìm đúng chỗ sửa; không phải đoạn văn học thuật cần biến đổi nhịp. Prompt không có finding.
- Scope cuối lượt: chỉ PROJECT_STATE, reviewer report và corrective prompt; ba artifact R1 của executor chưa sửa. Không commit/push trong lượt tiếp quản.

Các kiểm tra repository/style không thay đổi verdict nội dung R1. Chưa chạy publication lint hoặc checklist G6 vì không có chương mới được duyệt hay sản phẩm xuất bản mới.
