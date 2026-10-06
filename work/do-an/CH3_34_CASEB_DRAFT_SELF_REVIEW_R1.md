# BÁO CÁO TỰ ĐÁNH GIÁ DỰ THẢO MỤC 3.4 CASE B R2 (CH3_34_CASEB_DRAFT_SELF_REVIEW_R1)

- **Trạng thái:** `X7D1_CASEB_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7D1 R2 — Correct Section 3.4 Case B Draft`
- **Tệp dự thảo được đánh giá:** `work/do-an/CH3_34_CASEB_DRAFT_R1.md`
- **Branch:** `feature/x7d1-ch3-caseb-draft`
- **Reviewer Base HEAD:** `6d5f9ef741682aff0634dc2f0a22c028eda6f6ad`
- **Starting HEAD ban đầu:** `2b2bf5bd41f40f899f7e59d39bd7d3184c051751`

---

## 1. Kiểm Toán Số Lượng Từ và Phân Đoạn (Word Count & Paragraph Audit)

- **Tổng số từ toàn văn bản (kể cả bảng Markdown và cú pháp nhúng ảnh):** 1.803 từ.
- **Số từ văn xuôi (loại trừ các dòng bảng Markdown, tiêu đề đề mục, cú pháp nhúng ảnh và chú thích ảnh):** 1.246 từ.
- **Khung dung lượng mục tiêu R2:** 1.100–1.250 từ văn xuôi.
- **Đánh giá dung lượng:** Đạt chuẩn hoàn hảo (1.246 từ nằm trọn vẹn trong khoảng mục tiêu 1.100–1.250 từ, tinh gọn được 139 từ so với bản R1).
- **Số lượng đoạn văn xuôi:** 13 đoạn văn.
- **Phân bổ đoạn văn theo cấu trúc:**
  * Đoạn mở đầu Mục 3.4: 1 đoạn (xác lập Case B là can thiệp có kiểm soát đầu tiên, biến số điều chỉnh là cấu hình SMBv1, đối chiếu với baseline).
  * Tiểu mục 3.4.1: 6 đoạn văn xuôi (hiện trạng trước can thiệp & thao tác; kiểm tra cục bộ; dẫn nhập Hình 3.7; quan sát Hình 3.7; phân tích ranh giới kỹ thuật cục bộ; dẫn nhập Bảng 3.5; tổng hợp đối chiếu Bảng 3.5 sang đo đạc từ xa).
  * Tiểu mục 3.4.2: 6 đoạn văn xuôi (dẫn nhập đo lại phương ngữ từ xa & dẫn nhập Hình 3.8; quan sát Hình 3.8; đo lại MS17-010 & phân loại UNKNOWN; ranh giới 445 OPEN != vulnerable và UNKNOWN != SAFE; phân định 4 tầng kỹ thuật độc lập; kết luận thực nghiệm Case B & chuyển tiếp Case C).

---

## 2. Kiểm Toán Cấu Trúc Đề Mục (Heading Audit)

- **Số lượng tiêu đề H2:** Đúng 1 tiêu đề:
  * `## 3.4. Kết quả Case B — Vô hiệu hóa SMBv1 và đo lại từ xa`
- **Số lượng tiêu đề H3:** Đúng 2 tiêu đề:
  * `### 3.4.1. Thao tác vô hiệu hóa SMBv1 và kiểm tra trạng thái máy chủ cục bộ`
  * `### 3.4.2. Kết quả đo đạc lại từ xa và đối chiếu đa tầng`
- **Số lượng tiêu đề H3 phát sinh ngoài kế hoạch:** 0.
- **Số lượng tiêu đề H4 hoặc tiêu đề phụ:** 0.

---

## 3. Kiểm Toán Bảng Biểu (Table Audit — Count = 1)

Dự thảo tích hợp đúng 1 bảng tổng hợp đối chứng theo định hướng kết quả (result-oriented), kế thừa nguyên vẹn thiết kế đã phê duyệt trong Kế hoạch trình bày X7D0:

- **Bảng 3.5:** `Bảng 3.5. So sánh cấu hình và kết quả đo đạc trước và sau khi vô hiệu hóa SMBv1 (Case B)`
  - Cấu trúc: 4 cột (`Tầng kiểm tra / Tham số đo đạc | Trước can thiệp (Baseline) | Sau can thiệp (Case B) | Diễn giải trực tiếp & Giới hạn kết luận`).
  - Gồm 8 hàng so sánh đối chứng toàn diện:
    1. `Cấu hình máy chủ SMBv1 (EnableSMB1Protocol)`: True -> False.
    2. `Cấu hình máy chủ SMB2/3 (EnableSMB2Protocol)`: True -> True.
    3. `Tính năng hệ điều hành (FS-SMB1)`: Installed -> Installed (`SMBv1 disabled != FS-SMB1 uninstalled`).
    4. `Dịch vụ chia sẻ tệp (LanmanServer)`: Running -> Running (hai snapshot point-in-time, không suy diễn tính liên tục tuyệt đối hay tương thích toàn bộ ứng dụng).
    5. `Trạng thái cổng dịch vụ từ xa (Cổng TCP 445 từ trạm Kali)`: OPEN (syn-ack theo 3.2/3.3) -> OPEN trong phép đo lại (không gán nhãn syn-ack cho Case B, `445 OPEN != vulnerable`).
    6. `Phương ngữ SMB ghi nhận từ xa (Kịch bản smb-protocols)`: 5 phương ngữ -> 4 phương ngữ (2.0.2, 2.1, 3.0, 3.0.2; NT LM 0.12 không xuất hiện; không tuyên bố kiểm chứng toàn bộ workload SMB2/3).
    7. `Phán quyết kiểm tra MS17-010 (Kịch bản smb-vuln-ms17-010)`: UNKNOWN (theo 3.3) -> UNKNOWN / NO USABLE SCRIPT RESULT (nguyên nhân vắng mặt output không xác lập từ bằng chứng; `UNKNOWN != SAFE`).
    8. `Trạng thái bản vá hệ thống (Mã nhị phân driver srv.sys)`: UNPATCHED (theo 3.1) -> UNPATCHED (kế thừa mốc khóa 3.1 và metadata Case B, Case B không có thao tác vá; `SMBv1 disabled != PATCHED`).
  - **Kiểm toán từ ngữ Bảng 3.5:**
    * Không chứa cú pháp dòng lệnh thô hay đối số argv Nmap.
    * Không chứa mã định danh nội bộ (Evidence ID, Claim ID) hay đường dẫn file kho lưu trữ.
    * Không gán nhãn `syn-ack` cho cổng 445 của Case B sau can thiệp.
    * Không chứa các phán quyết ngoài bằng chứng như `PATCHED`, `SAFE`, `NOT VULNERABLE`.

---

## 4. Kiểm Toán Hình Ảnh (Figure Audit — Count = 2) & Đường Dẫn Phái Sinh

Dự thảo tích hợp đúng 2 hình ảnh phái sinh phục vụ trình bày:

1. **Hình 3.7:**
   - Cú pháp nhúng: `![Hình 3.7](chapter3/presentation/3_4/Hinh_3_7_After_Local.png)`
   - Chú thích: `Hình 3.7. Trạng thái cấu hình SMB, tính năng FS-SMB1 và dịch vụ LanmanServer sau khi vô hiệu hóa SMBv1`
   - Tệp vật lý: `work/do-an/chapter3/presentation/3_4/Hinh_3_7_After_Local.png`
   - Kích thước: $872 \times 310\,\text{px}$
   - SHA-256 phái sinh: `b7df43e54f69490c8fdbd82cd273dc834657dc3ec90a96981b3c3897f7e5b9b1`
   - Tệp nguồn: `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_03_After_Local.png` (SHA-256: `2f762508ec98da3b6ed75813c32ed5622cbe1c982e6e6e2907086152e9a6a6ad`)
   - Khung cắt cúp: `x=0, y=30, width=872, height=310`.

2. **Hình 3.8:**
   - Cú pháp nhúng: `![Hình 3.8](chapter3/presentation/3_4/Hinh_3_8_SMB_Protocols_Retest.png)`
   - Chú thích: `Hình 3.8. Kết quả đo lại các phương ngữ SMB từ trạm Kali Linux sau khi vô hiệu hóa SMBv1`
   - Tệp vật lý: `work/do-an/chapter3/presentation/3_4/Hinh_3_8_SMB_Protocols_Retest.png`
   - Kích thước: $1280 \times 400\,\text{px}$
   - SHA-256 phái sinh: `6af9df4edbca32d79af562b7f87b867283b31fba3316ce3859ce1a63a936b52c`
   - Tệp nguồn: `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_04_NSE02_Protocols.png` (SHA-256: `21ed6473f4e7010841e9730620b159c272238cf7335eb80fcfaf4ad61f7a7b5a`)
   - Khung cắt cúp: `x=0, y=24, width=1280, height=400`.

- **Kiểm toán loại bỏ hình ảnh dư thừa (Zero extraneous figures):**
  * Không tạo/nhúng ảnh `Before` (ảnh 01 trong evidence đã loại bỏ theo plan).
  * Không tạo/nhúng ảnh `Action` (ảnh 02 trong evidence đã loại bỏ theo plan).
  * Không tạo/nhúng ảnh `combined NSE04` (ảnh 05 trong evidence đã loại bỏ theo plan).

---

## 5. Xử Lý Chi Tiết Toàn Bộ Vấn Đề Thẩm Tra Độc Lập R1 (Blockers A–F)

| Blocker / Vấn đề R1 | Yêu cầu hiệu chỉnh R2 | Kết quả xử lý thực tế trong R2 |
|---|---|---|
| **Blocker A: Sửa validator ngoài phạm vi** | Khôi phục `scripts/validate_project.py` đúng nguyên trạng byte-for-byte từ commit Starting HEAD `2b2bf5bd41f40f899f7e59d39bd7d3184c051751`. | **ĐÃ HOÀN TẤT:** Đã chạy `git checkout 2b2bf5bd41f40f899f7e59d39bd7d3184c051751 -- scripts/validate_project.py`. File không còn bất kỳ diff nào so với Starting HEAD. |
| **Blocker B: Diễn giải nhân quả cho TCP 445 OPEN** | Bỏ cụm từ nhân quả "do dịch vụ LanmanServer vẫn đang chạy...", bỏ câu "cho phép luồng dữ liệu tiếp cận..."; dùng đúng câu: *"Từ trạm Kali, TCP 445 được ghi nhận ở trạng thái OPEN trong phép đo lại."* Sửa mốc baseline sang trích dẫn kết quả Mục 3.2. | **ĐÃ HOÀN TẤT:** Áp dụng chuẩn xác câu văn quan sát trực tiếp tại Đoạn 8 và Đoạn 11. Đoạn 2 sửa thành: *"Ở mốc trước can thiệp, các phép đo đã trình bày tại Mục 3.2 ghi nhận cả SMBv1 và các phương ngữ SMB2/3."* Khóa chặt `445 OPEN != vulnerable`. |
| **Blocker C: Diễn giải kịch bản smb-protocols quá mạnh/nhân quả** | Bỏ cụm từ "chứng minh rằng khi EnableSMB1Protocol chuyển thành False thì máy chủ không còn đưa SMBv1..."; dùng câu: *"Trong phép đo lại sau can thiệp, kịch bản smb-protocols ghi nhận 2.0.2, 2.1, 3.0 và 3.0.2; NT LM 0.12 (SMBv1) không xuất hiện trong danh sách phương ngữ. Kết quả này phù hợp với thay đổi cấu hình SMBv1 đã ghi nhận trên máy chủ."* | **ĐÃ HOÀN TẤT:** Áp dụng chuẩn xác tại Đoạn 9; không nói đàm phán thành công, bắt tay thành công hay máy chủ không còn tiếp nhận SMBv1. |
| **Blocker D: Tuyên bố lịch sử driver srv.sys thái quá** | Bỏ hoàn toàn câu "driver srv.sys chưa từng được cập nhật"; dùng: *"Trạng thái bản vá cục bộ tiếp tục được giữ ở phân loại UNPATCHED theo mốc đã xác lập tại Mục 3.1 và metadata của Case B; Case B không ghi nhận thao tác cài bản vá."* | **ĐÃ HOÀN TẤT:** Áp dụng chuẩn xác tại Đoạn 5 và Đoạn 12; không gán việc đo lại srv.sys cho Hình 3.7. |
| **Blocker E: Lỗi cột StartType trong crop manifest Hình 3.7** | Bỏ `StartType = Running` và `chế độ khởi động Running` vì ảnh không xác lập StartType; chỉ ghi nhận `Status = Running`; thay cách nói file vật lý trên đĩa bằng `FS-SMB1 được ghi nhận Installed`. | **ĐÃ HOÀN TẤT:** Đã chỉnh sửa dòng 30, 32, 41 trong `work/do-an/CH3_34_CASEB_CROP_MANIFEST_R1.md`. |
| **Blocker F: Trùng lặp ranh giới & độ dài văn bản** | Rút gọn văn bản xuống khung 1.100–1.250 từ văn xuôi; gộp danh sách 4 tầng thành 1 đoạn văn tổng hợp ngắn gọn; nêu `UNKNOWN != SAFE` và `445 OPEN != vulnerable` một lần rõ ràng. | **ĐÃ HOÀN TẤT:** Văn bản đạt 1.246 từ văn xuôi (13 đoạn); danh sách 4 tầng được gộp mạch lạc tại Đoạn 12; các ranh giới được phát biểu chuẩn xác tại Đoạn 11. |
| **Biên tập: Dấu nhắc lệnh kết thúc** | Thay câu "Dấu nhắc lệnh kết thúc xác nhận phiên kiểm tra hoàn tất bình thường" bằng *"Dấu nhắc PowerShell xuất hiện trở lại sau các lệnh kiểm tra."* | **ĐÃ HOÀN TẤT:** Đã thay thế tại Đoạn 4. |
| **Biên tập: Kết luận Case B** | Bỏ câu "cổng 445 vẫn mở đối với mạng nội bộ" và "thu hẹp bề mặt phương ngữ"; kết luận bám sát quan sát đo đạc. | **ĐÃ HOÀN TẤT:** Đoạn 13 kết luận: *"Sau can thiệp, danh sách phương ngữ ghi nhận từ trạm Kali không còn NT LM 0.12, trong khi TCP 445 vẫn được ghi nhận OPEN; trạng thái bản vá cục bộ vẫn UNPATCHED và phép đo MS17-010 vẫn UNKNOWN."* Tiếp nối chuyển tiếp Case C không tiết lộ kết quả. |

---

## 6. Kiểm Toán Ranh Giới Kỹ Thuật và Ngôn Từ Cấm (Boundary & Forbidden Term Audit)

| Hạng mục kiểm toán | Kết quả kiểm tra | Chi tiết và bằng chứng trong văn bản |
|---|---|---|
| **syn-ack trong Case B sau can thiệp** | **PASS (0 vi phạm)** | Không xuất hiện `syn-ack` trong văn xuôi Case B hay cột Case B của Bảng 3.5. Chỉ xuất hiện trong cột Baseline của Bảng 3.5 khi trích dẫn kết quả Mục 3.2. Bảng 3.5 nêu rõ: *"Phép đo lại của Case B không bao gồm cờ --reason nên không có dữ liệu phản hồi syn-ack."* |
| **Đàm phán / bắt tay thành công** | **PASS (0 vi phạm)** | Không sử dụng các cụm từ `đàm phán thành công`, `bắt tay thành công`. Chỉ dùng cách nói khách quan: *"kịch bản smb-protocols ghi nhận 2.0.2, 2.1, 3.0 và 3.0.2; NT LM 0.12 (SMBv1) không xuất hiện trong danh sách phương ngữ"*. |
| **Zero downtime / Không gián đoạn** | **PASS (0 vi phạm)** | Tuyệt đối không sử dụng `zero downtime`, `không gián đoạn`. Ranh giới được phát biểu chuẩn mực: *"không chứng minh tính liên tục tuyệt đối của dịch vụ trong suốt quá trình thay đổi, cũng như không chứng minh mọi ứng dụng nghiệp vụ đều tương thích hoàn toàn."* |
| **Khẳng định tương thích nghiệp vụ** | **PASS (0 vi phạm)** | Không tuyên bố SMB2/3 workload hoạt động hoàn hảo. Đoạn 9 khẳng định rõ: *"không chứng minh toàn bộ khối lượng công việc trao đổi tệp của ứng dụng nghiệp vụ đã được kiểm chứng đầy đủ."* |
| **Gỡ bỏ tính năng (Feature uninstalled)** | **PASS (0 vi phạm)** | Khóa chặt ranh giới `SMBv1 disabled != FS-SMB1 uninstalled`. Nêu rõ gói tính năng `FS-SMB1` được ghi nhận `Installed`. |
| **Tuyên bố đã vá (Patched / Safe / Not Vulnerable)** | **PASS (0 vi phạm)** | Không tuyên bố hệ thống `patched`, `safe` hay `not vulnerable`. Mọi xuất hiện của các từ này chỉ nằm trong phương trình bất đẳng thức ranh giới (`SMBv1 disabled != PATCHED`, `445 OPEN != vulnerable`, `UNKNOWN != SAFE`) hoặc trong mệnh đề phủ định cảnh báo. |
| **Nguồn gốc trạng thái UNPATCHED** | **PASS (0 vi phạm)** | Nêu chuẩn xác: kế thừa từ mốc đã khóa tại Mục 3.1 và metadata của Case B do Case B không có thao tác cài bản vá; không suy diễn rằng Hình 3.7 đo đạc lại driver `srv.sys` hay hotfix. |
| **Ranh giới UNKNOWN của MS17-010** | **PASS (0 vi phạm)** | Phân loại chuẩn xác `UNKNOWN / NO USABLE SCRIPT RESULT`. Khẳng định rõ: *"nguyên nhân của việc không có đầu ra script khả dụng không được xác lập từ bộ bằng chứng hiện có, và người thực nghiệm không đưa ra suy diễn chủ quan về cơ chế xử lý gói tin."* |
| **Các giả định suy diễn bị cấm** | **PASS (0 vi phạm)** | Không sử dụng `false negative`, `Couldn't negotiate SMBv1`, `STATUS_`, `IPC$`, `SMBv1 probe silenced`, `chưa từng được cập nhật`. |
| **Phân định 4 tầng độc lập** | **PASS (0 vi phạm)** | Đoạn 12 phân định rõ ràng 4 tầng kỹ thuật bằng văn xuôi tự nhiên súc tích: cấu hình SMB, tính năng hệ thống, trạng thái bản vá nội bộ, phán quyết quét từ xa. |
| **Tiết lộ kết quả Case C** | **PASS (0 vi phạm)** | Không tiết lộ kết quả Case C. Chuyển tiếp phương pháp luận chuẩn mực: *"Case B thay đổi cấu hình giao thức ở máy chủ; Case C tiếp tục khảo sát một lớp kiểm soát khác trên đường truyền mạng bằng pfSense Transparent Bridge."* |
| **Tiết lộ phân tích Chương 4** | **PASS (0 vi phạm)** | Không đưa ra kết luận đánh giá rủi ro hay xếp hạng hiệu quả giảm thiểu của Chương 4. |
| **Ngôn ngữ quản trị/QA nội bộ** | **PASS (0 vi phạm)** | Không chứa các thuật ngữ nội bộ như `Evidence ID`, `Claim ID`, `canonical`, `gate`, `governance`, `ground truth`. |

---

## 7. Kiểm Toán Văn Phong Học Thuật và Linter Tiếng Việt

- Chạy công cụ kiểm tra văn phong tiếng Việt học thuật:
  `uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_34_CASEB_DRAFT_R1.md`
- Kết quả: `Không phát hiện mẫu văn phong cần xem xét.` (0 cảnh báo).
- Phong cách viết đáp ứng đầy đủ yêu cầu của `AUTHOR_VOICE.md`: phong cách báo cáo tốt nghiệp An toàn thông tin, ngôn từ điềm tĩnh, bám sát số liệu thực nghiệm, tính khách quan cao, không tiếp thị hay phán xét quá đà.

---

## 8. Kiểm Toán Kiểm Tra Kỹ Thuật Đề Án (Project QA Audit)

1. **Kiểm tra tính hợp lệ đề án (`validate_project.py`):**
   - Lệnh thực thi: `uv run python scripts/validate_project.py`
   - Ghi nhận trạng thái: Sau khi revert `scripts/validate_project.py` về bản gốc theo đúng yêu cầu Blocker A, công cụ báo lỗi do cú pháp Markdown mẫu nhúng trong tệp prompt của manager (`work/do-an/prompts/X7D1_WRITE_CH3_34_CASEB.md`). Các liên kết trong bản thảo `CH3_34_CASEB_DRAFT_R1.md` hoàn toàn hợp lệ 100%. Đúng theo chỉ thị mục 3 & 11 của prompt R2, đề tài giữ nguyên trạng validator gốc và báo cáo rõ giới hạn kiểm tra này, không tự ý sửa đổi tệp hạ tầng.
2. **Bộ kiểm thử đơn vị (`unittest`):**
   - Lệnh thực thi: `uv run python -m unittest discover -s tests -p "test_*.py"`
   - Kết quả: `Ran 7 tests in 0.002s - OK` (Mã thoát 0).
3. **Kiểm tra văn phong học thuật tiếng Việt (`lint_vi_academic.py`):**
   - Lệnh thực thi: `uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_34_CASEB_DRAFT_R1.md`
   - Kết quả: `Không phát hiện mẫu văn phong cần xem xét.` (Mã thoát 0).
4. **Kiểm tra cú pháp Git (`git diff --check`):**
   - Lệnh thực thi: `git diff --check`
   - Kết quả: Không phát hiện lỗi whitespace hay ký hiệu dòng không hợp lệ (Mã thoát 0).
5. **Bảo tồn toàn vẹn dữ liệu gốc (Source Evidence Integrity):**
   - `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_03_After_Local.png`: SHA-256 `2f762508ec98da3b6ed75813c32ed5622cbe1c982e6e6e2907086152e9a6a6ad` (100% khớp).
   - `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_04_NSE02_Protocols.png`: SHA-256 `21ed6473f4e7010841e9730620b159c272238cf7335eb80fcfaf4ad61f7a7b5a` (100% khớp).
6. **Bảo tồn toàn vẹn hình ảnh phái sinh (Derived Presentation Integrity):**
   - `work/do-an/chapter3/presentation/3_4/Hinh_3_7_After_Local.png`: SHA-256 `b7df43e54f69490c8fdbd82cd273dc834657dc3ec90a96981b3c3897f7e5b9b1` (100% khớp).
   - `work/do-an/chapter3/presentation/3_4/Hinh_3_8_SMB_Protocols_Retest.png`: SHA-256 `6af9df4edbca32d79af562b7f87b867283b31fba3316ce3859ce1a63a936b52c` (100% khớp).

---

## 9. Trạng Thái Hoàn Thành

- **Tự công bố trạng thái:** `X7D1_CASEB_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`.
- Không tự tuyên bố PASS đánh giá độc lập bên ngoài.
