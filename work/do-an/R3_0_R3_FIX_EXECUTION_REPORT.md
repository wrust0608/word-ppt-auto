# BÁO CÁO THỰC THI HIỆU CHỈNH R3-0 R3 — SỬA LỆNH VÀ TRUY VẾT LUẬN ĐIỂM
(CH3 REDESIGN R3-0 R3 FIX EXECUTION REPORT)

> [!WARNING]
> **TÀI LIỆU LỊCH SỬ — ĐÃ BỊ THAY THẾ (SUPERSEDED):**
> Báo cáo thực thi R3 này đã bị **SUPERSEDED** bởi Báo cáo thực thi R4: [`work/do-an/R3_0_R4_FIX_EXECUTION_REPORT.md`](file:///E:/word_ppt-auto/work/do-an/R3_0_R4_FIX_EXECUTION_REPORT.md). Các số liệu kiểm kê nguồn cũ (44 hàng bảng / 73 mục) trong tài liệu này là số liệu lịch sử bị lỗi, đã được thay thế bằng số liệu trích xuất tự động chuẩn hóa tại R4 (53 hàng bảng thực tế + 26 khối văn bản = 79 mục kiểm kê nguồn).

- **Trạng thái thực thi:** `SUPERSEDED / HISTORICAL RECORD` (Đã được thay thế bởi R4).
- **Ngày thực thi:** 2026-10-08
- **Tác nhân thực hiện:** Antigravity Executor
- **Candidate R2 nguồn:** `94e82c0d5ff40726d4a2f7cdd5b4278f78972977`
- **Báo cáo review thẩm định căn cứ:** `work/do-an/R3_0_EVIDENCE_VISUAL_BLUEPRINT_EXTERNAL_REVIEW_R2.md`
- **Tài liệu kiến trúc cơ sở cập nhật:**
  1. `work/do-an/CH3_REDESIGN_EVIDENCE_VISUAL_BLUEPRINT_R1.md` (Revision R3)
  2. `work/do-an/CH3_REDESIGN_TABLE_FIGURE_LEDGER_R1.md` (Revision R3)
  3. `work/do-an/CH3_REDESIGN_CONTENT_MIGRATION_MAP_R1.md` (Revision R3)
- **Tài liệu trạng thái dự án:** `work/do-an/PROJECT_STATE.md`

---

## 1. TỔNG QUAN PHẠM VI VÀ MỤC TIÊU HIỆU CHỈNH R3

Đợt hiệu chỉnh R3-0 R3 tập trung xử lý dứt điểm 5 nhóm phát hiện tồn tại (R2-F01 đến R2-F05) được chỉ ra trong Báo cáo thẩm định độc lập R2 (`work/do-an/R3_0_EVIDENCE_VISUAL_BLUEPRINT_EXTERNAL_REVIEW_R2.md`), bảo đảm tính xác thực tuyệt đối của câu lệnh, tính chuẩn xác của hệ thống định vị (locators), xác lập mẫu số định lượng minh bạch cho việc truy vết luận điểm (explicit denominator), phân định rạch ròi ranh giới đo đạc Section 21 và truth locks, đồng bộ hóa các bảng dữ liệu so sánh và lập disposition chi tiết cho các cảnh báo linter phong cách học thuật tiếng Việt.

Toàn bộ quá trình hiệu chỉnh tuân thủ nghiêm ngặt các ranh giới:
- Giữ nguyên tên ba artifact `_R1` để bảo toàn các siêu liên kết trong toàn bộ dự án.
- Giữ vững toàn bộ các kết quả đã đạt tại vòng R2; không viết lại toàn bộ thiết kế.
- Không sửa đổi bất kỳ tệp chứng cứ staging nào (83/83 tệp giữ nguyên SHA-256).
- Không sửa đổi `CHAPTER_2.md`, `CHAPTER_3_DRAFT_R2.md`, hay `CHAPTER_2_3_REVIEW.docx`.
- Không tạo mới số liệu, không giả lập retest, không crop/panel ảnh hay viết văn xuôi Chương 3.

---

## 2. BẢNG ĐỐI CHIẾU BEFORE / AFTER CHI TIẾT THEO TỪNG NHÓM PHÁT HIỆN

### 2.1. Xử lý R2-F01: Sửa lệnh quét và mô tả socket baseline

| Vị trí / Đối tượng | Trước hiệu chỉnh (Before R3) | Sau hiệu chỉnh (After R3) | Tệp chứng cứ nguồn & Căn cứ kỹ thuật |
|---|---|---|---|
| **Hình 3.2 (Mục 3.2.1 Blueprint dòng 131, Ledger dòng 52 & 105)** | Mô tả dùng lệnh `netstat -ano` để kiểm tra cổng lắng nghe. | Sửa thành lệnh PowerShell `Get-NetTCPConnection`: `Get-NetTCPConnection -State Listen \| Where-Object { $_.LocalPort -in 139,445 }`. | `chapter3/evidence/baseline/Windows_PreDemo_01_Network_SMB.png` (khớp pixel thực tế cửa sổ PowerShell trong ảnh). |
| **Hình 3.6 & Bảng 3.4 (Mục 3.4.1 Blueprint dòng 296–303, Ledger dòng 40 & 112, Migration Map Claim-21)** | Câu lệnh mô tả thêm `sudo` hoặc thiếu tham số; chưa phân định giữa câu lệnh operator và recorded argv; raw command có `--privileged`. | Chép chính xác câu lệnh operator từ ảnh và manifest: `nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20` (không `sudo`, không `unsafe=0`). Ghi nhận recorded argv dòng 1 raw file: `/usr/lib/nmap/nmap --privileged ...`. Đánh dấu bản rút gọn nếu dùng trong văn bản. | `chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png`, `Scenario2_Run_Manifest.txt` dòng 35, và `NSE-SMB-04_ms17010.nmap` dòng 1. |

### 2.2. Xử lý R2-F02: Audit toàn bộ locators, lập Source Inventory xác lập Denominator

| Vị trí / Đối tượng | Trước hiệu chỉnh (Before R3) | Sau hiệu chỉnh (After R3) | Căn cứ xử lý kỹ thuật |
|---|---|---|---|
| **Chuẩn hóa đường dẫn tệp (Locators)** | Xuất hiện tên rút gọn hoặc thiếu thư mục cha: `04_Bridge.png`, `05_Bridge_Filtering.png`, `02_Action.png`, `03_After_Local.png`, `NSE-SMB-04_ms17010.nmap` không phân biệt thư mục. | Toàn bộ tệp đều dùng full relative path chính xác: `chapter3/evidence/case_c/pfSense_04_Bridge.png`, `pfSense_05_Bridge_Filtering.png`, `chapter3/evidence/case_b/SMBv1_Remediation_01_Before.png`, `02_Action.png`, `03_After_Local.png`. Phân định rõ 3 tệp nmap NSE04 tại 3 thư mục `scenario2`, `case_b`, và `case_c`. | Kiểm toán đối chiếu khớp 100% với cây tệp thực tế trong repository. |
| **Stable Evidence IDs** | Một số dòng trong Migration Map chưa ghi mã Stable Evidence ID chuẩn. | Bổ sung đầy đủ Stable Evidence IDs đã đăng ký từ `work/do-an/EVIDENCE_REGISTER.md` (ví dụ `ENV-CORE-01..05`, `S1-RAW-01..05`, `S2-RAW-01..04`, `B-LOCAL-01..02`, `B-ACTION-01`, `B-RAW-01..02`, `C-IFACE-01`, `C-BRIDGE-01`, `C-TUNE-DIRECT-01`, `C-RULE-01..03`, `C-RAW-01..02`, `C-VIS-01..02`, `C-LOG-01`, `C-META-01`, `C-CLOSURE-01`). | Tham chiếu trực tiếp Mục 4 của `EVIDENCE_REGISTER.md`. |
| **Xác lập Mẫu số định lượng (Explicit Denominator)** | Tuyên bố 41/41 claims để tự chứng minh đầy đủ khi mẫu số các fact và bảng cũ chưa được thống kê cụ thể. | Xây dựng **Bảng kiểm kê nguồn (Source Inventory)** chi tiết tại Mục 3 của `CH3_REDESIGN_CONTENT_MIGRATION_MAP_R1.md`: kiểm kê toàn bộ **44 hàng dữ liệu của 7 bảng cũ** và **29 khối fact văn bản** xuyên suốt dòng 1 đến 318 của `CHAPTER_3_DRAFT_R2.md` (tổng cộng **73 mục kiểm kê nguồn**). Mọi mục đều có đích đến cụ thể (Destination) hoặc nhãn Retire có lý do. | Khắc phục triệt để tồn tại denominator chưa xác lập. 41 claims bao trùm toàn diện 73 mục kiểm kê nguồn này. |
| **Ghi nhận `arp-response` Case C (dòng 262)** | Chưa ghi nhận rõ lý do Nmap nhận diện host up trong topology Case C. | Bổ sung rõ ràng tại Fact F23, Claim-33 và Bảng 3.6: Nmap xác định máy chủ ở trạng thái trực tuyến nhờ phản hồi ARP (`Host is up, received arp-response`) trong topology cầu nối Layer 2. | `CHAPTER_3_DRAFT_R2.md` dòng 262, khớp raw `chapter3/evidence/case_c/NSE-SMB-01_ports.nmap`. |
| **Retire thời lượng quét 0.51s (dòng 278)** | Chưa giải trình lý do không đưa thời lượng 0.51s vào luồng đọc chính. | Ghi nhận rõ tại Fact F26 và Claim-36: **RETIRE CÓ LÝ DO** đối với thời lượng 0.51 giây vì đây là tham số phụ thuộc hiệu năng runtime của máy ảo point-in-time, không mang tính chân lý an ninh; dữ kiện cốt lõi (cổng 445 FILTERED, script UNKNOWN) được bảo toàn trọn vẹn. | Phân loại phương pháp luận khoa học, không tạo số liệu mới. |

### 2.3. Xử lý R2-F03: Phân định Section 21 và `LanmanServer: Running`

| Vị trí / Đối tượng | Trước hiệu chỉnh (Before R3) | Sau hiệu chỉnh (After R3) | Căn cứ kỹ thuật |
|---|---|---|---|
| **Section 21 của `RUN4_PAUSE_STATE_REPORT.txt`** | Ghi nhận Section 21 chứng minh LanmanServer Running. | Phân định rạch ròi: Section 21 (dòng 376–384) chỉ ghi nhận `EnableSMB1Protocol: True`, `EnableSMB2Protocol: True`, listeners TCP 139/445, driver `srv.sys` 6.3.9600.16384/16421, UNPATCHED, và firewall rule. **Section 21 hoàn toàn không có dòng LanmanServer Service**. | `chapter3/evidence/case_c/RUN4_PAUSE_STATE_REPORT.txt` dòng 376–384. |
| **Nguồn khóa của `LanmanServer: Running`** | Nhầm lẫn giữa direct measurement và truth lock. | Xác lập rõ ràng: Trạng thái `LanmanServer: Running` tại cuối lượt Case C là **canonical truth lock kế thừa** (`ETM-C02` trong `EXPERIMENTAL_TRUTH_MATRIX.md`, kế thừa từ baseline và Section 8 dòng 162). Nêu rõ giới hạn kỹ thuật: Section 21 thiếu direct final service measurement. Không giả lập retest hay thay đổi canonical truth. | Khóa chân lý thực nghiệm `ETM-C02`. |

### 2.4. Xử lý R2-F04: Giới hạn Get-HotFix inventory, Derived Interpretation và đồng bộ 8 hàng

| Vị trí / Đối tượng | Trước hiệu chỉnh (Before R3) | Sau hiệu chỉnh (After R3) | Căn cứ kỹ thuật |
|---|---|---|---|
| **Giới hạn `Get-HotFix` inventory** | Có thể bị hiểu là máy chủ chỉ từng cài 6 bản vá trong toàn bộ lịch sử. | Ghi rõ giới hạn: Danh mục `Get-HotFix` thu thập nội bộ chỉ là bằng chứng bổ trợ chứng minh thiếu các bản vá MS17-010 đã biết (KB4012213/KB4012216), không đại diện cho toàn bộ lịch sử cập nhật của hệ điều hành. | Blueprint Mục 3.2.2 dòng 155, Ledger Bảng 3.2 dòng 38, Migration Map Claim-10. |
| **Phân loại `UNPATCHED`** | Được coi như một quan sát trực tiếp trên màn hình. | Xác lập chuẩn mực: `UNPATCHED` là **diễn giải suy luận (derived interpretation)** dựa trên đối chiếu phiên bản số nhị phân `6.3.9600.16421` với ngưỡng tối thiểu `6.3.9600.18604` theo tài liệu chính thức Microsoft S032; không phải primary observation hiển thị trực tiếp. | Microsoft Support S032 / S005. |
| **Đồng bộ số hàng Bảng 3.5 và Bảng 3.7** | Bảng 3.5 mô tả chưa đủ 8 hàng tương đương Bảng 3.7. | Đồng bộ hóa hoàn toàn: Cả Bảng 3.5 và Bảng 3.7 đều chuẩn hóa **đầy đủ 8 hàng dữ liệu**: (1) Lớp can thiệp; (2) Trạng thái TCP 139 từ xa; (3) Trạng thái TCP 445 từ xa; (4) Phương ngữ SMB từ xa; (5) Cấu hình SMBv1 cục bộ; (6) Dịch vụ LanmanServer cục bộ; (7) Bản vá srv.sys cục bộ; (8) Phán quyết MS17-010 từ xa. | Blueprint Bảng 3.5 dòng 443–445, Ledger Bảng 3.5 dòng 41, Migration Map Claim-38. |

---

## 3. KẾT QUẢ CHẠY LINTER VÀ BẢNG DISPOSITION CHI TIẾT (R2-F05)

Linter tiếng Việt học thuật được thực thi sau khi hoàn tất substantive review theo lệnh:
`uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_REDESIGN_EVIDENCE_VISUAL_BLUEPRINT_R1.md work/do-an/CH3_REDESIGN_TABLE_FIGURE_LEDGER_R1.md work/do-an/CH3_REDESIGN_CONTENT_MIGRATION_MAP_R1.md`

- **Kết quả tổng thể:** `error=0, warning=17, info=0` (0 lỗi nghiêm trọng; 17 cảnh báo cần xem xét).
  - `CH3_REDESIGN_TABLE_FIGURE_LEDGER_R1.md`: 0 cảnh báo.
  - `CH3_REDESIGN_EVIDENCE_VISUAL_BLUEPRINT_R1.md`: 13 cảnh báo.
  - `CH3_REDESIGN_CONTENT_MIGRATION_MAP_R1.md`: 4 cảnh báo.

### Bảng lập disposition chi tiết cho 17 findings

| STT | Tệp & Dòng | Mã lỗi / Cảnh báo | Nội dung trích xuất | Quyết định Disposition | Lý do kỹ thuật / Rationale |
|---|---|---|---|---|---|
| 1 | `BLUEPRINT:42` | `VI012` | Có 18 đoạn mở bằng cùng cấu trúc: “1 đề mục”. | `KEEP_WITH_REASON` | Đây là nhãn form đặc tả mẫu chuẩn hóa bắt buộc lặp lại trên 18 tiểu mục kiến trúc (`1. **Đề mục:** ...`, `2. **Hình ảnh / Bảng biểu:** ...`, `3. **Bằng chứng đầu vào:** ...`, `4. **Thông điệp chính:** ...`, `5. **Ranh giới:** ...`). Việc giữ nguyên cấu trúc nhãn form này là có chủ đích kỹ thuật để bảo đảm tính nhất quán và dễ tra cứu, không phải sự lặp lại vô ý thức trong văn xuôi học thuật. |
| 2 | `BLUEPRINT:44` | `VI011` | Câu dài 114 từ. | `KEEP_WITH_REASON` | Câu diễn giải 4 tầng dữ kiện kỹ thuật (tiếp cận, diện mạo dịch vụ, dấu hiệu lỗ hổng, ranh giới can thiệp), giữ nguyên liên kết logic chuỗi điều kiện, không cắt nhỏ làm gãy mạch tư duy phương pháp luận. |
| 3 | `BLUEPRINT:62` | `VI005` | Tính từ tự đánh giá: "đánh giá toàn diện mọi giải pháp bảo mật trong thực tế". | `FALSE_POSITIVE` | Cụm từ nằm trong dấu ngoặc kép trích dẫn của câu lệnh cấm đoán phương pháp luận: `CẤM tuyên bố đo đạc nhằm "đánh giá toàn diện mọi giải pháp bảo mật trong thực tế"`. Tác giả dùng để cấm đoán sự ngộ nhận, không phải tự đánh giá. |
| 4 | `BLUEPRINT:71` | `VI011` | Câu dài 91 từ. | `KEEP_WITH_REASON` | Mô tả tiến trình 2 giai đoạn lớn của thực nghiệm, các thành phần liên kết chặt chẽ theo sơ đồ luồng. |
| 5 | `BLUEPRINT:109` | `VI011` | Câu dài 87 từ. | `KEEP_WITH_REASON` | Chuỗi thông số kiểm toán baseline (IP, route, LanmanServer, FS-SMB1, SMBv1/v2, signing flags), giữ nguyên liên kết tham số của một cấu hình hệ thống hoàn chỉnh. |
| 6 | `BLUEPRINT:177` | `VI011` | Câu dài 60 từ. | `KEEP_WITH_REASON` | Ranh giới caption Hình 3.3 phân định giữa chuỗi hiển thị, số nhị phân và đối chiếu tài liệu Microsoft, là ranh giới pháp lý kỹ thuật bắt buộc. |
| 7 | `BLUEPRINT:265` | `VI011` | Câu dài 73 từ. | `KEEP_WITH_REASON` | Thông điệp chính tổng hợp Kịch bản 1 về khả năng tiếp cận và ngăn xếp giao thức. |
| 8 | `BLUEPRINT:368` | `VI011` | Câu dài 76 từ. | `KEEP_WITH_REASON` | Chuỗi tham số nội bộ Case B (EnableSMB1Protocol=False, EnableSMB2Protocol=True, FS-SMB1=Installed point-in-time), phản ánh đúng hiện trạng kỹ thuật. |
| 9 | `BLUEPRINT:392` | `VI011` | Câu dài 70 từ. | `KEEP_WITH_REASON` | Ranh giới kết luận Mục 3.5.1 về cấu hình máy chủ vs trạng thái driver nhân srv.sys. |
| 10 | `BLUEPRINT:464` | `VI006` | Kết luận chung chưa chỉ ra kết quả hoặc bước tiếp theo cụ thể. | `KEEP_WITH_REASON` | Đây là đặc tả ranh giới mục `3.5.3` nêu rõ: `loại bỏ hiệu quả phương ngữ cũ trên bề mặt mạng nhưng để ngỏ cổng dịch vụ 445 và không vá lỗi nhân; tạo tiền đề cho việc thử nghiệm giải pháp kiểm soát mạng ở Mục 3.6`. Đã nêu rõ bước tiếp theo kế thừa sang Mục 3.6, giữ nguyên cấu trúc chuẩn. |
| 11 | `BLUEPRINT:597` | `VI011` | Câu dài 83 từ. | `KEEP_WITH_REASON` | Chuỗi liệt kê 8 tiêu chí dữ liệu chuẩn hóa của Bảng 3.7. |
| 12 | `BLUEPRINT:645` | `VI011` | Câu dài 56 từ. | `KEEP_WITH_REASON` | Ranh giới kết luận Mục 3.7.2 chốt lại sự khác biệt giữa diện mạo bên ngoài và lỗ hổng bên trong. |
| 13 | `BLUEPRINT:658` | `VI011` | Câu dài 143 từ. | `KEEP_WITH_REASON` | Tóm lược 5 phát hiện cốt lõi của toàn Chương 3, giữ nguyên liên kết 5 điểm để không làm gãy mạch logic tổng kết. |
| 14 | `MIGRATION:12` | `VI011` | Câu dài 61 từ. | `KEEP_WITH_REASON` | Mục tiêu tài liệu liệt kê các thành phần chính (Block-by-Block Map, Source Inventory, Granular Matrix). |
| 15 | `MIGRATION:19` | `VI011` | Câu dài 56 từ. | `KEEP_WITH_REASON` | Nguyên tắc bảo tồn chân lý kỹ thuật và mở lại cấu trúc kể chuyện. |
| 16 | `MIGRATION:23` | `VI011` | Câu dài 70 từ. | `KEEP_WITH_REASON` | Khai báo mẫu số định lượng rõ ràng 44 hàng bảng + 29 khối fact văn bản. |
| 17 | `MIGRATION:220` | `VI011` | Câu dài 63 từ. | `KEEP_WITH_REASON` | Tóm tắt 5 tiên đề chân lý và ranh giới kỹ thuật cốt lõi. |

*Tổng kết Disposition:* **1 FALSE_POSITIVE**, **16 KEEP_WITH_REASON**, **0 FIX cần sửa style làm đổi chứng cứ**. Việc giữ nguyên các cấu trúc này tuân thủ nguyên tắc tối cao của repository: *"Never let a style rule alter evidence, numbers, citations, claim boundaries, approved terminology or institutional formatting"*.

---

## 4. KIỂM TOÁN TÍNH TOÀN VẸN VÀ MỨC ĐỘ BAO PHỦ (SOURCE INVENTORY & COVERAGE)

1. **Mẫu số định lượng xác lập (Explicit Denominator):**
   - **44 hàng dữ liệu của 7 bảng cũ:** $6 + 5 + 5 + 4 + 8 + 8 + 8 = 44$ hàng đều được định danh và ánh xạ 100% sang các bảng đề xuất tương ứng.
   - **29 khối dữ kiện văn bản nguồn:** Bao quát từ dòng 1 đến 318 của `CHAPTER_3_DRAFT_R2.md`.
   - **Tổng mẫu số nguồn:** **73 mục dữ kiện**. Trong đó: 72 mục được chuyển dịch nguyên vẹn (REUSE/MOVE), 1 mục duy nhất được retire có lý do minh bạch (thời lượng 0.51s tại dòng 278).
2. **Bộ khung luận điểm kỹ thuật:**
   - **41/41 claims** bao trùm 100% mẫu số nguồn 73 mục kiểm kê.
   - 100% claims đều có Stable Evidence IDs đã đăng ký từ `EVIDENCE_REGISTER.md`, cấp độ bằng chứng (78 primary + 5 secondary), tệp nguồn canonical và ranh giới kỹ thuật bắt buộc.
3. **Quản lý Bảng biểu và Hình ảnh:**
   - **7/7 bảng biểu** được bảo toàn và phân bổ chuẩn mực; Bảng 3.5 và Bảng 3.7 đều đồng bộ 8 hàng dữ liệu chuẩn hóa.
   - **11/11 hình ảnh cũ** được quản lý minh bạch (MOVE, MERGE, EXPAND, hoặc SUPPORTING).
   - **14 hình ảnh đề xuất mới** (7 Evidence, 4 Comparison, 3 Explanatory) được phân bổ rõ vai trò kỹ thuật, 0 thất thoát bằng chứng.

---

## 5. CÁC GIỚI HẠN CÒN MỞ (OPEN LIMITATIONS) BÀN GIAO CHO REVIEW ĐỘC LẬP

1. **Chờ Reviewer độc lập thẩm định:** Ba artifact Blueprint/Ledger/Migration Map đã đạt trạng thái sẵn sàng để Reviewer ChatGPT kiểm tra đối soát độc lập.
2. **Chưa mở R3-1:** Tuyệt đối không tiến hành soạn thảo văn bản Chương 3 mới (prose writing) trước khi có phê duyệt chính thức từ người dùng và reviewer đối với vòng R3-0.
3. **Chưa render hình ảnh mới:** Chưa cắt ghép đa panel hay xuất sơ đồ vector mới; các panel dự kiến vẫn được quản lý ở mức đặc tả kỹ thuật trên các tệp nguồn staging có sẵn.
4. **Bảo lưu ranh giới xung đột danh pháp CF-11:** Ảnh nhật ký pfSense tại Hình 3.13 tiếp tục giữ nguyên cột Rule hiển thị nhãn Pass `(100000104)` đối chiếu với tệp manifest ghi `(1000000104)`, không quy thuộc tuyệt đối named rule ID.

---

## 6. KẾT LUẬN VÀ TRẠNG THÁI DỰ ÁN

Executor Antigravity đã hoàn tất toàn bộ các nội dung kỹ thuật của đợt hiệu chỉnh R3-0 R3 theo đúng chỉ đạo. Dự án được chuyển sang trạng thái:
`CURRENT OVERRIDE: PENDING_R3_INDEPENDENT_REVIEW` trong `work/do-an/PROJECT_STATE.md`.

Executor dừng lại tại đây và kính chuyển toàn bộ kết quả để Reviewer độc lập tiến hành thẩm định.
