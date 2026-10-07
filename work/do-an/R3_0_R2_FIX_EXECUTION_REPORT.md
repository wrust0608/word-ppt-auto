# BÁO CÁO THỰC THI HIỆU CHỈNH R3-0 (REVISION R2)

- **Ngày thực thi:** 2026-10-08 (Asia/Saigon).
- **Nhánh làm việc:** `feature/ch3-redesign-evidence-first-r1`.
- **Candidate base R1:** `4f9d3f059f96d8b44ef6c83e0c2b20301245ce3e`.
- **Lộ trình căn cứ:** `work/do-an/ROADMAP_CH3_REDESIGN_EVIDENCE_FIRST_2026_10_07.md` (commit `170aa24293b2cf8e579abb1ecf60920bca418bd9`).
- **Nhiệm vụ:** Hiệu chỉnh toàn diện cổng R3-0 (Evidence & Visual Blueprint) khắc phục triệt để các điểm tồn tại F01–F09 theo yêu cầu của Báo cáo thẩm định độc lập R1 (`work/do-an/R3_0_EVIDENCE_VISUAL_BLUEPRINT_EXTERNAL_REVIEW_R1.md`) và prompt chỉ đạo (`work/do-an/prompts/R3_0_R2_FIX_EVIDENCE_VISUAL_BLUEPRINT.md`).
- **Trạng thái cổng sau thực thi:** `R3_0_REVISE_BLOCKING / PENDING_R2_INDEPENDENT_REVIEW` (Chờ ChatGPT thẩm định độc lập R2; chưa mở R3-1).

---

## 1. DANH SÁCH TÀI LIỆU THAY ĐỔI TRONG ĐỢT R2

1. `work/do-an/CH3_REDESIGN_EVIDENCE_VISUAL_BLUEPRINT_R1.md` (Hiệu chỉnh nâng cấp lên Revision R2).
2. `work/do-an/CH3_REDESIGN_TABLE_FIGURE_LEDGER_R1.md` (Hiệu chỉnh nâng cấp lên Revision R2).
3. `work/do-an/CH3_REDESIGN_CONTENT_MIGRATION_MAP_R1.md` (Hiệu chỉnh nâng cấp lên Revision R2, bổ sung ma trận 41 claim).
4. `work/do-an/PROJECT_STATE.md` (Cập nhật CURRENT OVERRIDE ghi nhận hoàn tất R2, chờ thẩm định độc lập).
5. `work/do-an/R3_0_R2_FIX_EXECUTION_REPORT.md` (Tạo mới báo cáo thực thi R2).

*Lưu ý bảo toàn:* Báo cáo thẩm định độc lập R1 (`work/do-an/R3_0_EVIDENCE_VISUAL_BLUEPRINT_EXTERNAL_REVIEW_R1.md`) được giữ nguyên vẹn để phục vụ truy vết lịch sử kiểm tra. Toàn bộ `CHAPTER_2.md`, `CHAPTER_3_DRAFT_R2.md`, DOCX và 83 tệp bằng chứng staging tuyệt đối không bị thay đổi.

---

## 2. BẢNG TỔNG HỢP XỬ LÝ CÁC ĐIỂM TỒN TẠI (FINDINGS F01–F09)

| Mã | Tóm tắt yêu cầu từ Review R1 | Vị trí sửa đổi trong các Artifact R2 | Căn cứ kỹ thuật & Giải pháp đã thực hiện | Kết quả |
|---|---|---|---|---|
| **F01** | **Crop srv.sys:** Cửa sổ PowerShell (không phải tab Details). Giữ cả FileVersion hiển thị `6.3.9600.16384` và phiên bản số `6.3.9600.16421`. Dẫn nguồn Microsoft S032 (ngưỡng 18604). Nhãn tổng hợp ngoài pixel ảnh. | - Blueprint: Mục 3.2.2, Hình 3.3, Hình 3.7.<br>- Ledger: Bảng 3.2, Hình 3.3, Hình 3.7.<br>- Migration: Claim-07, Claim-08, Claim-09. | Mô tả chuẩn xác cửa sổ PowerShell gồm lệnh truy vấn và lệnh ghép 4 trường số; chỉ dẫn crop giữ trọn vẹn cả chuỗi hiển thị và kết quả số `6.3.9600.16421`; trích dẫn trực tiếp nguồn chính thức Microsoft Support S032/S005 thay vì dùng mapping nội bộ làm external authority; yêu cầu mọi nhãn tổng hợp (UNPATCHED) đặt ngoài pixel ảnh. | **RESOLVED** |
| **F02** | **Xóa unsafe=0 trong NSE04:** Lệnh thực nghiệm không có `unsafe=0`. Giữ kết luận UNKNOWN / NO USABLE SCRIPT RESULT; nguyên nhân nội bộ chưa xác lập. Phân biệt operator command và Nmap argv. | - Blueprint: Mục 3.4.1, 3.4.2, Hình 3.6.<br>- Ledger: Bảng 3.4, Hình 3.6.<br>- Migration: Claim-21, Claim-22. | Xóa bỏ hoàn toàn cụm `unsafe=0` khỏi toàn bộ tài liệu; phân biệt rõ lệnh chuẩn hóa của operator (`sudo nmap -p 445 --script smb-vuln-ms17-010 192.168.56.20`) với argv Nmap ghi nhận (`--privileged`); giữ nguyên phân loại UNKNOWN / NO USABLE SCRIPT RESULT; ghi rõ nguyên nhân nội bộ của script chưa được xác lập từ bằng chứng trực tiếp. | **RESOLVED** |
| **F03** | **Khôi phục giới hạn Case B:** Thay "không gián đoạn / không làm sập" bằng point-in-time Running và danh sách dialect quan sát được. Cổng 139 không đo lại; cổng 445 OPEN không có `--reason`. Trạng thái bản vá kế thừa baseline/metadata. | - Blueprint: Mục 3.5.1, 3.5.2, 3.5.3, Hình 3.8, Hình 3.9.<br>- Ledger: Bảng 3.5, Hình 3.8, Hình 3.9.<br>- Migration: Claim-26, Claim-27, Claim-28, Claim-29. | Thay toàn bộ kết luận suy diễn bằng dữ kiện đo được: `LanmanServer` được ghi nhận Running tại thời điểm kiểm tra; retest ghi nhận 4 dialect (2.0.2..3.0.2) vắng mặt NT LM 0.12; khẳng định rõ chưa chứng minh tính liên tục dịch vụ, sự thành công/thất bại của phiên SMB hay tải công việc thực tế; ghi nhận TCP 139 NOT REMEASURED, TCP 445 OPEN không có `--reason`; xác định trạng thái bản vá kế thừa baseline và metadata, ảnh After Local không đo lại srv.sys/hotfix. | **RESOLVED** |
| **F04** | **Phân biệt Case C không đo dialect với cổng FILTERED:** Ô phương ngữ Case C ghi NOT MEASURED, không suy diễn từ cổng FILTERED. Giữ local SMB1/SMB2 hàng riêng. Remote MS17 giữ UNKNOWN / NO USABLE SCRIPT RESULT. | - Blueprint: Mục 3.6.2, 3.6.3, 3.7.1, Bảng 3.7.<br>- Ledger: Bảng 3.6, Bảng 3.7.<br>- Migration: Claim-36, Claim-38. | Ô phương ngữ từ xa của Case C trong ma trận so sánh Bảng 3.7 ghi rõ **`Không có phép đo tương ứng trong Case C / NOT MEASURED`**; tách riêng cấu hình nội bộ SMB1=True, SMB2=True thành hàng độc lập; giữ nguyên phán quyết quét từ xa MS17-010 là `UNKNOWN / NO USABLE SCRIPT RESULT` (không tạo nhãn lai "UNKNOWN/Filtered"); xóa bỏ suy diễn "script không gửi được gói thăm dò". | **RESOLVED** |
| **F05** | **Nguồn và timebase Case C:** Windows cuối lượt trỏ Section 21 của `RUN4_PAUSE_STATE_REPORT.txt` (secondary metadata). Đối chiếu Nmap và pfSense theo lineage và tuple (IP, port, TCP SYN), không ghép đồng hồ. Bảo lưu CF-11. | - Blueprint: Mục 3.6.1, 3.6.3, Hình 3.13, Bảng 3.6.<br>- Ledger: Bảng 3.6, Hình 3.13.<br>- Migration: Claim-34, Claim-35, Claim-37. | Xác định nguồn trạng thái Windows cuối lượt Case C là **Section 21 của `case_c/RUN4_PAUSE_STATE_REPORT.txt`** (cấp chứng cứ secondary metadata/closure, phần trước là troubleshooting); đối chiếu lưu lượng Nmap và log pfSense dựa trên run lineage và bộ 4 thông số (IP nguồn, IP đích, cổng, cờ TCP SYN), không giả định đồng bộ đồng hồ tuyệt đối; bảo lưu nguyên vẹn xung đột nhãn quy tắc CF-11 không cắt cúp ảnh và không quy thuộc đích danh named rule ID. | **RESOLVED** |
| **F06** | **Claim coverage & truy vết 100%:** Thiết lập ma trận claim chi tiết kèm Claim ID, locator blob/dòng, Evidence ID, cấp độ chứng cứ, ranh giới. Giữ chi tiết capabilities (DFS, Leasing, Multi-credit) và signing độc lập. Khai báo cách đếm 317/318 dòng. | - Migration: Toàn bộ Mục 3 (Ma trận truy vết 41 claim) và Mục 1.<br>- Blueprint: Mục 3.3.2, Bảng 3.3.<br>- Ledger: Bảng 3.3, Hình 3.5. | Xây dựng Ma trận truy vết chi tiết từng luận điểm (Granular Claim Traceability Matrix) gồm 41 claim định danh (`Claim-01` đến `Claim-41`) với mẫu số 100% bao phủ toàn bộ văn bản và bảng biểu của `CHAPTER_3_DRAFT_R2.md` (blob `40d2a895bc970f88d7260b3138b8a701f5eb0a8c`); khai báo minh bạch phương pháp đếm dòng: 317 dòng nội dung theo Get-Content/splitlines và 318 dòng hiển thị kèm ký tự xuống dòng cuối tệp; giữ nguyên vẹn giá trị chi tiết `smb2-capabilities` (DFS trên 2.0.2..3.0.2, Leasing và Multi-credit trên 2.1..3.0.2); tách bạch signing quan sát từ xa với cờ cấu hình nội bộ. | **RESOLVED** |
| **F07** | **Sơ đồ luồng & ranh giới hai ca:** Hình 3.1 tách 2 nhánh độc lập (Host Case B vs Network Case C) từ mốc phục hồi phù hợp. Không mô tả Case C kế thừa Case B; không bịa mốc thời gian rollback. Hình 3.14 phân định hai vị trí can thiệp, không gộp cấu hình. Không dùng nhãn canonical "Case A". Chuyển đánh giá rủi ro/khuyến nghị sang Chương 4. | - Blueprint: Mục 3.1.2, 3.4.2, 3.5.3, 3.7.2, Hình 3.1, Hình 3.14.<br>- Ledger: Hình 3.1, Hình 3.14.<br>- Migration: Mục 3.1, 3.7, Claim-39, Claim-40, Claim-41. | Thiết kế lại Hình 3.1 tách thành 2 nhánh thực nghiệm độc lập (Host-level Case B vs Network-path Case C) đều xuất phát từ mốc phục hồi kiểm chứng (Before Demo snapshot), xóa bỏ hoàn toàn giả định Case C kế thừa cấu hình của Case B; không tự bịa đặt mốc thời gian rollback; thiết kế Hình 3.14 thể hiện hai vị trí can thiệp riêng rẽ, không làm người đọc hiểu lầm là cấu hình gộp; loại bỏ nhãn "Case A" khỏi các ca thực nghiệm canonical; chuyển toàn bộ các nội dung về đánh giá rủi ro, chính sách bản vá, compensating controls và khuyến nghị chiến lược sang Chương 4. | **RESOLVED** |
| **F08** | **Thống nhất số hiệu, nguồn và thống kê trong Ledger:** Sửa Old No Hình 3.4; sửa bảng lệch cột `Kali_to_Windows_Connectivity.png`; thống kê 34 ảnh canonical (KEEP 7, MERGE 7, SUPPORTING 15, RETIRE 5); 14 hình đề xuất (7 Evidence, 4 Comparison, 3 Explanatory); Bảng 3.7 giữ nguyên 8 hàng dữ liệu; phân định 78 primary và 5 secondary staging files; dùng đường dẫn chính xác theo thư mục. | - Ledger: Toàn bộ Section 1, 2, 3, 4, 5, 6.<br>- Blueprint: Mục 4 (Reconciled Audit).<br>- Migration: Mục 1, Mục 3. | Sửa Old No Hình 3.4 thành "Không có hình riêng trong Draft R2 (được bổ sung từ evidence B4 có sẵn)", hành động `NEW (Evidence presentation)`; xóa ô thừa `baseline/` sửa lỗi lệch cột tại dòng 13 của bảng kiểm toán ảnh; chuẩn hóa thống kê kiểm toán 34 ảnh canonical: KEEP 7, MERGE 7, SUPPORTING 15, RETIRE 5; chuẩn hóa 14 hình đề xuất: 7 Evidence, 4 Comparison, 3 Explanatory; bảo toàn nguyên vẹn 8 hàng dữ liệu chuẩn hóa của Bảng 3.7 cũ; phân định rạch ròi 83 tệp staging gồm 78 chứng cứ sơ cấp và 5 chứng cứ thứ cấp; chuẩn hóa toàn bộ đường dẫn nguồn theo thư mục cụ thể (`chapter3/evidence/...`). | **RESOLVED** |
| **F09** | **Đồng bộ bộ nhớ hiện hành (State):** Cập nhật `PROJECT_STATE.md` ghi nhận hoàn tất R2 chờ thẩm định độc lập; kiến trúc Chương 3 reopened, technical locks giữ nguyên; Chương 2 locked; numbering proposed; Chương 4 dormant. Không tự ghi APPROVED hay mở R3-1. | - `work/do-an/PROJECT_STATE.md` (CURRENT OVERRIDE). | Cập nhật mục CURRENT OVERRIDE trong `PROJECT_STATE.md`: ghi nhận executor đã hoàn thành sửa chữa Revision R2 cho ba artifact R3-0, gate hiện tại là `R3_0_REVISE_BLOCKING / PENDING_R2_INDEPENDENT_REVIEW`, chờ ChatGPT Reviewer thẩm định độc lập; sau reviewer PASS vẫn cần người dùng phê duyệt chốt R3-0 mới được khóa số hiệu và mở R3-1; tuyệt đối không tự ý ghi USER APPROVED hay mở R3-1. | **RESOLVED** |

---

## 3. BẢNG KIỂM TRA ĐỐI SOÁT VÀ TOÀN VẸN DỮ LIỆU

### 3.1. Kiểm tra Git Blobs và SHA-256

| Đối tượng kiểm tra | Giá trị mong muốn / Giá trị đã khóa | Kết quả thực đo trên Repository | Đánh giá |
|---|---|---|---|
| Blob `work/do-an/CHAPTER_2.md` | `55ffb13acb3398c7ab29d6d5abbb369e5d26f3d0` | `55ffb13acb3398c7ab29d6d5abbb369e5d26f3d0` | **KHỚP 100% (UNCHANGED)** |
| Blob `work/do-an/CHAPTER_3_DRAFT_R2.md` | `40d2a895bc970f88d7260b3138b8a701f5eb0a8c` | `40d2a895bc970f88d7260b3138b8a701f5eb0a8c` | **KHỚP 100% (UNCHANGED)** |
| Blob `work/do-an/output/CHAPTER_2_3_REVIEW.docx` | `276278b1fb3e2f74acd11f6cb42b66df8c9b0ca9` | `276278b1fb3e2f74acd11f6cb42b66df8c9b0ca9` | **KHỚP 100% (UNCHANGED)** |
| SHA-256 `CHAPTER_2_3_REVIEW.docx` | `3c9ac6b6bfa1d259f92856a6c6b48ec398178e927f9beb06f5c0c37749dd3db2` | `3c9ac6b6bfa1d259f92856a6c6b48ec398178e927f9beb06f5c0c37749dd3db2` | **KHỚP 100% (UNCHANGED)** |
| Checksum 83 tệp evidence staging | Khớp 100% `CHAPTER_3_EVIDENCE_SHA256.csv` | 83/83 tệp khớp 100%, 0 mismatch | **KHỚP 100% (UNCHANGED)** |

### 3.2. Bảng kiểm tra mức độ bao phủ (Coverage Reconciliation)

| Hạng mục kiểm tra | Định mức / Mẫu số (Denominator) | Số lượng đã ánh xạ và xử lý trong R2 | Trạng thái đối soát |
|---|---|---|---|
| Luận điểm kỹ thuật cũ (Claim Coverage) | 41 claims (`Claim-01` đến `Claim-41`) | 41/41 claims được phân bổ đích đến, nguồn chứng cứ và ranh giới | **100% COVERAGE** |
| Ảnh canonical trong kho bằng chứng | 34 ảnh PNG (33 visual + 1 bounded conflict) | 34 ảnh (KEEP 7, MERGE 7, SUPPORTING 15, RETIRE 5) | **100% RECONCILED** |
| Hình ảnh đề xuất trong Chương 3 mới | 14 hình (7 Evidence, 4 Comparison, 3 Explanatory) | 14 hình được thiết kế chi tiết crop/panel/caption ranh giới | **100% ACCOUNTED** |
| Bảng biểu đề xuất trong Chương 3 mới | 7 bảng (Bảng 3.1 đến Bảng 3.7) | 7 bảng được thiết kế đầy đủ, Bảng 3.7 giữ nguyên 8 hàng dữ liệu chuẩn | **100% ACCOUNTED** |
| Phân loại 83 tệp chứng cứ staging | 83 tệp staging | 78 primary/direct evidence + 5 secondary metadata/closure | **100% CLASSIFIED** |

---

## 4. KẾT QUẢ THỰC CHẠY CÁC CÔNG CỤ KIỂM THỬ VÀ LINTER

### 4.1. Kiểm tra tính toàn vẹn dự án (Project Validation)
- Lệnh thực thi: `uv run python scripts/validate_project.py`
- Kết quả: `Project validation passed.` (Exit code: 0).

### 4.2. Kiểm tra bộ kiểm thử đơn vị (Unit Tests)
- Lệnh thực thi: `uv run python -m unittest discover -s tests -p "test_*.py"`
- Kết quả: `Ran 7 tests in 0.005s — OK` (7/7 tests passed; Exit code: 0).

### 4.3. Kiểm tra bộ quy chuẩn văn phong học thuật tiếng Việt (Style Linter)
- Lệnh thực thi: `uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_REDESIGN_EVIDENCE_VISUAL_BLUEPRINT_R1.md work/do-an/CH3_REDESIGN_TABLE_FIGURE_LEDGER_R1.md work/do-an/CH3_REDESIGN_CONTENT_MIGRATION_MAP_R1.md`
- Kết quả: `error=0, warning=16, info=0` (Exit code: 0).
- **Biên bản đánh giá và xử lý các cảnh báo:**
  - *Cảnh báo VI011 (13 cảnh báo về câu dài):* Xuất hiện tại các mục định nghĩa thông điệp chính hoặc danh mục liệt kê điều kiện tiên quyết trong Blueprint và Migration Map. Quyết định: **KEEP_WITH_REASON**. Đây là tài liệu quy chuẩn kỹ thuật (specification blueprint) nội bộ, các câu này chứa chuỗi danh sách điều kiện kỹ thuật, mã tham số hoặc các biến thực nghiệm bắt buộc phải đi cùng nhau để bảo đảm tính chặt chẽ logic; không phải văn xuôi xuất bản và không được cắt vụn làm mất liên kết điều kiện.
  - *Cảnh báo VI005 (1 cảnh báo tại Blueprint dòng 62):* Trích xuất câu `CẤM tuyên bố đo đạc nhằm "đánh giá toàn diện mọi giải pháp bảo mật trong thực tế"`. Quyết định: **FALSE_POSITIVE / KEEP_WITH_REASON**. Đây là mệnh lệnh cấm đoán tiêu cực (negative boundary constraint) trong đặc tả thiết kế nhằm ngăn ngừa tác giả overclaim; từ ngữ nằm trong dấu ngoặc kép trích dẫn hành vi bị cấm, không phải tác giả tự dùng tính từ đánh giá.
  - *Cảnh báo VI006 (1 cảnh báo tại Blueprint dòng 464):* Trích xuất câu tóm lược ranh giới kết luận section của Case B. Quyết định: **KEEP_WITH_REASON**. Nội dung đã chỉ rõ giới hạn kỹ thuật (cổng 445 vẫn mở, driver chưa vá) làm tiền đề kế thừa cho Kịch bản Case C tiếp theo.
  - *Table Figure Ledger:* Đạt chuẩn hoàn hảo, `0 error, 0 warning`.

---

## 5. CÁC HẠNG MỤC BẢO LƯU CHƯA GIẢI QUYẾT (UNRESOLVED CANONICAL ITEMS)

Toàn bộ các hạn chế khách quan của bộ dữ liệu thực nghiệm tiếp tục được bảo lưu nghiêm cẩn theo nguyên tắc toàn vẹn khoa học:
1. **Xung đột nhãn quy tắc CF-11:** Ảnh nhật ký pfSense hiển thị nhãn `CASE C baseline pass Kali to Windows (100000104)`, trong khi run manifest gán quy tắc `Block SMB... (1000000104)`. Đề tài bảo lưu nguyên vẹn xung đột này, không cắt cúp ảnh và không quy thuộc tuyệt đối vào một named rule ID cụ thể.
2. **Hệ quy chiếu thời gian giữa Kali và pfSense:** Không có cơ chế đồng bộ đồng hồ NTP tuyệt đối giữa các máy ảo; sự đối chiếu giữa lệnh quét Nmap và bản ghi nhật ký pfSense dựa trên run lineage và bộ 4 thông số mạng (IP nguồn, IP đích, cổng dịch vụ, cờ TCP SYN).
3. **Chính sách ký số SMB nội bộ và quan sát từ xa:** Giữ độc lập giữa cờ cấu hình nội bộ (`EnableSecuritySignature : False`) và quan sát từ xa qua kịch bản NSE (`enabled but not required` trên dialect 3.0.2).
4. **Nguyên nhân nội bộ của kịch bản NSE04 không xuất hiện kết luận:** Giữ nguyên trạng thái thực tế cổng 445 mở, Nmap hoàn tất mà không có khối `Host script results:`; phân loại theo phương pháp luận là `UNKNOWN / NO USABLE SCRIPT RESULT`; tuyệt đối không suy đoán nguyên nhân lỗi nội bộ của kịch bản khi raw evidence không ghi nhận.
5. **Trạm mạng 192.168.56.100:** Giữ nguyên nhãn bắt buộc `UNKNOWN identity`.

---

## 6. KẾT LUẬN VÀ ĐIỂM DỪNG BẮT BUỘC (STOP CONDITION)

- Đợt hiệu chỉnh Revision R2 cho cổng R3-0 đã hoàn tất đầy đủ 100% các yêu cầu F01–F09.
- Ba tài liệu thiết kế R3-0 đã sẵn sàng ở trạng thái chuẩn mực cao nhất để chuyển giao cho ChatGPT Reviewer tiến hành vòng thẩm định độc lập R2 (`R3-0 R2 Independent Review`).
- **ĐIỂM DỪNG BẮT BUỘC (HARD STOP):**
  - Trạng thái: `R3_0_REVISE_BLOCKING / PENDING_R2_INDEPENDENT_REVIEW`.
  - Executor dừng công việc tại đây, không tự ý viết văn xuôi Chương 3 (Zero Prose Drafting), không tạo file crop/panel mới, không tự ý chuyển sang cổng R3-1 khi chưa có reviewer PASS và phê duyệt chính thức từ người dùng.
