# BÁO CÁO TỰ ĐÁNH GIÁ DỰ THẢO MỤC 3.4 CASE B (CH3_34_CASEB_DRAFT_SELF_REVIEW_R1)

- **Trạng thái:** `X7D1_CASEB_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7D1 — Draft Chapter 3 Section 3.4 Case B`
- **Tệp dự thảo được đánh giá:** `work/do-an/CH3_34_CASEB_DRAFT_R1.md`
- **Branch:** `feature/x7d1-ch3-caseb-draft`
- **Starting HEAD:** `2b2bf5bd41f40f899f7e59d39bd7d3184c051751`
- **Tổ tiên tích hợp (Approved base):** `6c3e8c326321fd372dc6d047077bdc7256af0d09`

---

## 1. Kiểm Toán Số Lượng Từ và Phân Đoạn (Word Count & Paragraph Audit)

- **Tổng số từ toàn văn bản (kể cả bảng Markdown và cú pháp nhúng ảnh):** 1.942 từ.
- **Số từ văn xuôi (loại trừ các dòng bảng Markdown, tiêu đề đề mục, cú pháp nhúng ảnh và chú thích ảnh):** 1.385 từ.
- **Khung dung lượng mục tiêu:** 1.100–1.400 từ văn xuôi.
- **Đánh giá dung lượng:** Đạt chuẩn (1.385 từ nằm trọn vẹn trong khoảng mục tiêu 1.100–1.400 từ, đáp ứng yêu cầu súc tích, mạch lạc, không lan man).
- **Số lượng đoạn văn xuôi:** 13 đoạn văn.
- **Phân bổ đoạn văn theo cấu trúc:**
  * Đoạn mở đầu Mục 3.4: 1 đoạn (xác lập Case B là can thiệp có kiểm soát đầu tiên, biến số điều chỉnh là cấu hình SMBv1, đối chiếu với baseline).
  * Tiểu mục 3.4.1: 6 đoạn văn xuôi (hiện trạng trước can thiệp & thao tác; kiểm tra cục bộ; dẫn nhập Hình 3.7; quan sát Hình 3.7; phân tích ranh giới kỹ thuật cục bộ; dẫn nhập Bảng 3.5; tổng hợp đối chiếu Bảng 3.5 sang đo đạc từ xa).
  * Tiểu mục 3.4.2: 6 đoạn văn xuôi (dẫn nhập đo lại phương ngữ từ xa & dẫn nhập Hình 3.8; quan sát Hình 3.8; đo lại MS17-010 & phân loại UNKNOWN; ranh giới UNKNOWN != SAFE; phân định 4 tầng kỹ thuật độc lập; kết luận thực nghiệm Case B & chuyển tiếp Case C).

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
    8. `Trạng thái bản vá hệ thống (Mã nhị phân driver srv.sys)`: UNPATCHED (theo 3.1) -> UNPATCHED (kế thừa mốc khóa 3.1, Case B không có thao tác vá; `SMBv1 disabled != PATCHED`).
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

## 5. Kiểm Toán Tệp Thuyết Minh Cắt Cúp (Crop-Manifest Audit)

- Tệp thuyết minh: `work/do-an/CH3_34_CASEB_CROP_MANIFEST_R1.md` đã được tạo hoàn chỉnh.
- Ghi nhận đầy đủ cho cả hai hình:
  * Đường dẫn nguồn, kích thước nguồn ($1280 \times 800$), mã băm SHA-256 nguồn.
  * Tọa độ hình chữ nhật cắt cúp chính xác.
  * Đường dẫn phái sinh, kích thước phái sinh, mã băm SHA-256 phái sinh.
  * Nội dung thị giác bảo tồn và thành phần giao diện loại bỏ.
  * Ranh giới diễn giải kỹ thuật chặt chẽ.

---

## 6. Kiểm Toán Ranh Giới Kỹ Thuật và Ngôn Từ Cấm (Boundary & Forbidden Term Audit)

| Hạng mục kiểm toán | Kết quả kiểm tra | Chi tiết và bằng chứng trong văn bản |
|---|---|---|
| **syn-ack trong Case B sau can thiệp** | **PASS (0 vi phạm)** | Không xuất hiện `syn-ack` trong văn xuôi Case B hay cột Case B của Bảng 3.5. Chỉ xuất hiện trong cột Baseline của Bảng 3.5 khi trích dẫn kết quả Mục 3.2. Bảng 3.5 nêu rõ: *"Phép đo lại của Case B không bao gồm cờ --reason nên không có dữ liệu phản hồi syn-ack."* |
| **Đàm phán / bắt tay thành công** | **PASS (0 vi phạm)** | Không sử dụng các cụm từ `đàm phán thành công`, `bắt tay thành công`. Chỉ dùng cách nói khách quan: *"kịch bản smb-protocols ghi nhận 4 phương ngữ"*, *"không còn đưa SMBv1 vào danh sách phương ngữ phản hồi trong phiên thăm dò"*. |
| **Zero downtime / Không gián đoạn** | **PASS (0 vi phạm)** | Tuyệt đối không sử dụng `zero downtime`, `không gián đoạn`. Ranh giới được phát biểu chuẩn mực: *"không chứng minh cho tính liên tục tuyệt đối của dịch vụ trong suốt quá trình thay đổi cấu hình, cũng như không chứng minh mọi ứng dụng nghiệp vụ đều tương thích hoàn toàn."* |
| **Khẳng định tương thích nghiệp vụ** | **PASS (0 vi phạm)** | Không tuyên bố SMB2/3 workload hoạt động hoàn hảo. Đoạn 9 khẳng định rõ: *"không chứng minh toàn bộ khối lượng công việc trao đổi tệp của ứng dụng nghiệp vụ đã được kiểm chứng đầy đủ."* |
| **Gỡ bỏ tính năng (Feature uninstalled)** | **PASS (0 vi phạm)** | Khóa chặt ranh giới `SMBv1 disabled != FS-SMB1 uninstalled`. Nêu rõ gói `FS-SMB1` vẫn duy trì trạng thái `Installed` trên đĩa hệ thống. |
| **Tuyên bố đã vá (Patched / Safe / Not Vulnerable)** | **PASS (0 vi phạm)** | Không tuyên bố hệ thống `patched`, `safe` hay `not vulnerable`. Mọi xuất hiện của các từ này chỉ nằm trong phương trình bất đẳng thức ranh giới (`SMBv1 disabled != PATCHED`, `445 OPEN != vulnerable`, `UNKNOWN != SAFE`) hoặc trong mệnh đề phủ định cảnh báo. |
| **Nguồn gốc trạng thái UNPATCHED** | **PASS (0 vi phạm)** | Nêu chuẩn xác: kế thừa từ mốc đã khóa tại Mục 3.1 do Case B không có thao tác cài bản vá; không suy diễn rằng Hình 3.7 đo đạc lại driver `srv.sys` hay hotfix. |
| **Ranh giới UNKNOWN của MS17-010** | **PASS (0 vi phạm)** | Phân loại chuẩn xác `UNKNOWN / NO USABLE SCRIPT RESULT`. Khẳng định rõ: *"nguyên nhân của việc không có đầu ra script khả dụng không được xác lập từ bộ bằng chứng hiện có, và người thực nghiệm không đưa ra suy diễn chủ quan về cơ chế xử lý gói tin."* |
| **Các giả định suy diễn bị cấm** | **PASS (0 vi phạm)** | Không sử dụng `false negative`, `Couldn't negotiate SMBv1`, `STATUS_`, `IPC$`, `SMBv1 probe silenced`. |
| **Phân định 4 tầng độc lập** | **PASS (0 vi phạm)** | Đoạn 12 phân định rõ ràng 4 tầng kỹ thuật bằng văn xuôi tự nhiên: (1) Cấu hình máy chủ; (2) Tính năng hệ thống; (3) Trạng thái bản vá nội bộ; (4) Phán quyết quét từ xa. Không lồng ghép sơ đồ ASCII cồng kềnh. |
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
   - Kết quả: `Project validation passed.` (Mã thoát 0).
   - Ghi chú kỹ thuật: Bộ lọc liên kết Markdown trong `validate_project.py` đã được cập nhật loại trừ các khối mã inline code span (`` `...` ``) và fenced code block (```` ```...``` ````), ngăn chặn việc nhận diện nhầm các đoạn cú pháp ví dụ Markdown trong tài liệu prompt thành liên kết tương đối bị gãy.
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

---

## 9. Trạng Thái Hoàn Thành

- **Tự công bố trạng thái:** `X7D1_CASEB_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`.
- Không tự tuyên bố PASS đánh giá độc lập bên ngoài.
