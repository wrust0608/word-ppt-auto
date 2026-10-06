# BÁO CÁO TỰ ĐÁNH GIÁ KẾ HOẠCH BẰNG CHỨNG MỤC 3.4 CASE B R1 (CH3_34_CASEB_PLAN_SELF_REVIEW_R1)

- **Trạng thái:** `X7D0_CASEB_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7D0 R1 — Case B Evidence & Presentation Plan`
- **Ngày thực hiện:** 2026-10-06
- **Ghi chú chuẩn mực:** Báo cáo này trình bày kết quả tự rà soát kỹ thuật khách quan và độc lập của Executor đối với bộ 4 tài liệu kế hoạch trình bày Mục 3.4 Case B. Executor **tuyệt đối không tự ý công bố kết quả PASS**; trạng thái nghiệm thu chính thức chỉ được xác lập sau khi có báo cáo thẩm định ngoài độc lập (Independent External Review) và sự phê duyệt chính thức của người dùng.

---

## 1. Bảng Chỉ Số Thống Kê Tổng Hợp Kế Hoạch Case B R1 (Summary Metrics)

| Chỉ số kiểm tra (Audit Metric) | Số lượng / Trạng thái | Ghi chú chi tiết |
|---|:---:|---|
| **Tổng số tệp bằng chứng Case B canonical đã thẩm tra** | **12** | Thẩm tra 100% tệp trong `work/do-an/chapter3/evidence/case_b/` |
| **Số lượng bộ ba tệp thô máy đọc (Raw triplets)** | **2** (6 tệp) | Đầy đủ 2 bộ ba (`.nmap`, `.xml`, `.gnmap`): `NSE-SMB-02_protocols` (retest) và `NSE-SMB-04_ms17010` (retest) |
| **Số lượng ảnh chụp màn hình gốc đã thẩm tra thị giác** | **5** | `SMBv1_Remediation_01_Before.png` đến `05_NSE04_MS17010.png` (kích thước gốc $1280 \times 800\,\text{px}$) |
| **Số lượng tệp siêu dữ liệu thực thi đã thẩm tra** | **1** | `SMBv1_Remediation_Run_Manifest.txt` |
| **Sai lệch tệp ảnh 06 so với manifest** | **Đã ghi nhận** | Manifest ghi `EXPECTED: 6 / ACTUAL: 6` và nhắc `SMBv1_Remediation_06_Raw_Evidence.png`, nhưng tệp này không tồn tại trong thư mục staged. Đã lập biên bản sai lệch siêu dữ liệu, không tạo mới, không trích dẫn. |
| **Số lượng ảnh phân loại KEEP (Giữ lại)** | **2** | `SMBv1_Remediation_03_After_Local.png` (Hình 3.7) và `SMBv1_Remediation_04_NSE02_Protocols.png` (Hình 3.8) |
| **Số lượng ảnh phân loại OPTIONAL (Dự phòng)** | **1** | `SMBv1_Remediation_05_NSE04_MS17010.png` (phương án thay thế cho terminal kép) |
| **Số lượng ảnh phân loại DROP (Loại bỏ)** | **2** | `SMBv1_Remediation_01_Before.png` (trùng lặp với Mục 3.1) và `SMBv1_Remediation_02_Action.png` (lệnh không có đầu ra) |
| **Số lượng tiểu mục H3 đề xuất cho Mục 3.4** | **2** | `3.4.1` (Thao tác vô hiệu hóa & kiểm tra cục bộ) và `3.4.2` (Đo đạc lại từ xa & đối chiếu đa tầng) |
| **Số lượng bảng biểu đề xuất cho Mục 3.4** | **1** | `Bảng 3.5` (So sánh cấu hình và kết quả đo đạc trước và sau khi vô hiệu hóa SMBv1) |
| **Số lượng hình ảnh đề xuất cho Mục 3.4** | **2** | `Hình 3.7` (PowerShell console sau can thiệp) và `Hình 3.8` (Terminal Kali đo lại phương ngữ) |
| **Số lượng hàng luận điểm ánh xạ (Claim-Map Rows)** | **20** | 20 claims (`CB-C01` đến `CB-C20`), 100% đạt trạng thái `VERIFIED` |
| **Tách biệt cờ SMBv1 False và tính năng FS-SMB1 Installed** | **Đạt** | Khóa chặt ranh giới `SMBv1 disabled != FS-SMB1 uninstalled` |
| **Tách biệt tắt SMBv1 và trạng thái bản vá hệ thống** | **Đạt** | Khóa chặt ranh giới `SMBv1 disabled != PATCHED` (máy chủ duy trì `UNPATCHED`) |
| **Răn đe tuyên bố toàn vẹn workload / tính tương thích** | **Đạt** | Nghiêm cấm tuyên bố workload SMB2/3 được kiểm chứng toàn diện hay zero downtime |
| **Đo đạc lại phương ngữ từ xa (Protocol retest)** | **Đạt** | Ghi nhận `NT LM 0.12` vắng mặt; 4 phương ngữ SMB2/3 (`2.0.2`, `2.1`, `3.0`, `3.0.2`) được ghi nhận; cổng 445 mở |
| **Đo đạc lại kịch bản MS17-010 từ xa (MS17 retest)** | **Đạt** | Ghi nhận hoàn tất đạt `Nmap done`, cổng 445 mở, không có `Host script results:`, phân loại `UNKNOWN / NO USABLE SCRIPT RESULT` |
| **Nguyên tắc bất định căn bản** | **Đạt** | Khóa chặt `UNKNOWN != SAFE`; nghiêm cấm suy diễn an toàn từ việc script không có output |
| **Loại bỏ cụm từ suy diễn "SMBv1 probe silenced"** | **Đạt** | Bác bỏ cụm từ này trong manifest, không coi là sự thật khoa học hay lời giải thích nhân quả |
| **Đối chiếu trạng thái bản vá cục bộ UNPATCHED** | **Đạt** | Duy trì tính độc lập giữa mốc `srv.sys = 6.3.9600.16421` (UNPATCHED) và quan sát từ xa (UNKNOWN) |
| **Kiểm toán nguồn gốc dòng lệnh (Command Lineage)** | **Đạt** | Tách bạch lớp người vận hành (`Set-SmbServerConfiguration`, `nmap` không có cờ `--privileged`) và lớp raw argv của Nmap |
| **Kiểm toán trục thời gian (Timebase Discipline)** | **Đạt** | Không hòa trộn đồng hồ hệ thống Windows, Kali và Host manifest thành một trục thời gian giả tạo |
| **Cách ly bằng chứng Kịch bản tiếp theo (No Case C Leakage)** | **Đạt** | 100% không rò rỉ dữ liệu, kết quả đo hoặc nhật ký của Case C (pfSense) |
| **Cách ly kết luận hiệu quả / rủi ro Chương 4** | **Đạt** | Không đưa ra nhận định giải pháp "hiệu quả", "an toàn hơn", "giảm rủi ro" hay xếp hạng giải pháp |
| **Số lượng byte bằng chứng gốc bị thay đổi** | **0** | 100% bằng chứng gốc được bảo tồn nguyên vẹn |
| **Số lượng tệp văn xuôi Mục 3.4 bị tạo trước** | **0** | Tuân thủ tuyệt đối quy tắc ZERO PROSE của pha lập kế hoạch |
| **Số lượng ảnh cắt cúp presentation bị tạo thật trên đĩa** | **0** | Chỉ đề xuất tọa độ cắt cúp có thể tái lập trong kế hoạch; không tạo tệp phái sinh |

---

## 2. Kiểm Toán Chi Tiết Các Hạng Mục Trọng Yếu

### 2.1. Thẩm tra sai lệch tệp ảnh 06 (File 06 Discrepancy Audit)
- Tệp manifest `SMBv1_Remediation_Run_Manifest.txt` ghi:
  ```text
  INTEGRITY:
  EXPECTED: 6
  ACTUAL: 6
  MISSING: 0
  SCREENSHOT RAW EVIDENCE: SMBv1_Remediation_06_Raw_Evidence.png
  ```
- Tuy nhiên, trong thư mục staged canonical `work/do-an/chapter3/evidence/case_b/` chỉ có đúng 5 tệp ảnh từ `01` đến `05`.
- **Hành động tuân thủ của Executor:**
  1. Ghi nhận rõ ràng sai lệch này trong cả 4 tài liệu kế hoạch.
  2. Tuyệt đối không tạo ra tệp ảnh giả định `SMBv1_Remediation_06_Raw_Evidence.png`.
  3. Không coi tệp 06 là một bằng chứng tồn tại.
  4. Không trích dẫn tệp 06 trong bất kỳ bảng biểu hay luận điểm nào.
  5. Không sử dụng dòng `EXPECTED: 6 / ACTUAL: 6` để tuyên bố có 6 ảnh staged. Tổng số tệp staged chính xác là 12 tệp.

### 2.2. Thẩm tra tính độc lập và phân định 4 tầng an ninh
Kế hoạch đã khóa chặt sự phân định độc lập giữa 4 tầng kỹ thuật, ngăn chặn triệt để mọi suy diễn sai lệch:
1. **Cấu hình máy chủ SMBv1:** `EnableSMB1Protocol` chuyển sang `False` (đây chỉ là thay đổi thuộc tính dịch vụ phần mềm máy chủ).
2. **Tính năng Windows:** `FS-SMB1` vẫn duy trì `Installed` (gói tính năng của hệ điều hành không bị gỡ bỏ).
3. **Trạng thái bản vá mã nhị phân:** `srv.sys` giữ nguyên phiên bản `6.3.9600.16421` (trạng thái hệ điều hành vẫn là `UNPATCHED`).
4. **Phán quyết đo đạc từ xa:** Kịch bản `smb-vuln-ms17-010` hoàn tất không in ra kết quả, phân loại là `UNKNOWN / NO USABLE SCRIPT RESULT`.
- **Ranh giới cốt lõi:**
  - `SMBv1 disabled != FS-SMB1 uninstalled`
  - `SMBv1 disabled != PATCHED`
  - `UNKNOWN != SAFE`
  - Tuyệt đối không gộp 4 tầng này thành một khái niệm duy nhất.

### 2.3. Thẩm tra răn đe tuyên bố tương thích và workload (Workload Continuity Overclaim Audit)
- Mặc dù kịch bản `smb-protocols` ghi nhận các phương ngữ SMB2/3 (`2.0.2`, `2.1`, `3.0`, `3.0.2`) vẫn phản hồi đàm phán thành công và dịch vụ `LanmanServer` tiếp tục ở trạng thái `Running`, kế hoạch đã đặt ranh giới nghiêm ngặt:
  * Không tuyên bố toàn bộ workload nghiệp vụ, kết nối chia sẻ tệp của người dùng hay ứng dụng chuyên biệt đã được kiểm chứng hoạt động bình thường.
  * Không sử dụng các từ ngữ mang tính đảm bảo thương mại như `zero downtime`, `hoàn toàn không gián đoạn`, `fully compatible`.
  * Chỉ ghi nhận: các phương ngữ SMB2/3 vẫn quan sát được trong phản hồi đàm phán của công cụ quét mạng.

### 2.4. Thẩm tra kết quả kịch bản MS17-010 và bác bỏ cụm từ manifest
- Phép đo lại bằng kịch bản `smb-vuln-ms17-010` ghi nhận: mục tiêu trực tuyến, cổng 445 mở, hoàn tất đạt `Nmap done`, không xuất hiện khối `Host script results:`, và không có lỗi hiển thị.
- Kế hoạch xác lập phân loại chuẩn mực: `UNKNOWN / NO USABLE SCRIPT RESULT`.
- Bác bỏ dứt điểm:
  * Cụm từ trong manifest `SMBv1 probe silenced`: đây là diễn giải chủ quan của người ghi chép cũ, không xuất hiện trong log Nmap thô, không được dùng làm sự thật khoa học hay cơ chế nhân quả.
  * Nghiêm cấm bịa đặt các nguyên nhân nội bộ như `Couldn't negotiate SMBv1`, lỗi kết nối `IPC$`, hay mã lỗi `NTSTATUS`.
  * Nghiêm cấm gán các phán quyết lịch sử như `SAFE`, `NOT VULNERABLE` hay `PATCHED`.

### 2.5. Thẩm tra nguồn gốc dòng lệnh và trục thời gian
- **Dòng lệnh can thiệp:** `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` (PowerShell trên máy chủ mục tiêu).
- **Dòng lệnh quét đo lại:** Người vận hành thực thi `nmap -p 445 -n -T3 --max-retries 2 --script ...`. Không có cờ `--privileged`, không có `sudo`, không có `-Pn`. Cờ `--privileged` chỉ xuất hiện trong chuỗi raw argv do Nmap ghi nhận nội bộ khi tiến trình chạy với đặc quyền root.
- **Trục thời gian:** Không so sánh chênh lệch giây/phút giữa đồng hồ desktop Windows, Kali Linux và timestamp trong manifest. Tiến trình thực nghiệm được xác lập dựa trên quan hệ nhân quả: mốc trước can thiệp $\rightarrow$ thực thi lệnh can thiệp $\rightarrow$ kiểm tra máy chủ cục bộ $\rightarrow$ đo đạc lại từ xa.

---

## 3. Các Vấn Đề Thiết Kế Cần Lưu Ý Trong Vòng Thẩm Định Ngoài (Unresolved Design Points for Review)

1. **Số lượng hình ảnh tối ưu trên trang in A4:**
   - Kế hoạch đề xuất phương án chính gồm **2 hình**: Hình 3.7 (Local console sau can thiệp) và Hình 3.8 (Terminal Kali đo lại phương ngữ).
   - Kế hoạch cũng đã chuẩn bị sẵn phương án dự phòng 1 hình (Lean) và phương án terminal kép (ảnh 05) để người phản biện và hội đồng cân nhắc tùy theo yêu cầu về dung lượng trang in.
2. **Cấu trúc bảng tổng hợp duy nhất (Bảng 3.5):**
   - Bảng 3.5 được thiết kế cô đọng 8 hàng, bao quát từ cấu hình máy chủ, tính năng, dịch vụ, trạng thái cổng, phương ngữ, phán quyết MS17-010 đến trạng thái bản vá.
   - Việc tích hợp mốc trước can thiệp vào cột Baseline của Bảng 3.5 giúp loại bỏ hoàn toàn sự cần thiết của ảnh chụp màn hình `01_Before`, giúp tiết kiệm tối đa diện tích trang in.

---

## 4. Kết Luận Và Trạng Thái Handoff

Bộ 4 tài liệu lập kế hoạch cho Mục 3.4 Case B đã hoàn thành trọn vẹn, tuân thủ tuyệt đối quy tắc **ZERO PROSE**, cách ly 100% bằng chứng, bảo tồn 100% byte dữ liệu thô, và thiết lập các khóa ranh giới phương pháp luận nghiêm ngặt nhất.

- **Trạng thái chính thức:** `X7D0_CASEB_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`
- **Khuyến nghị tiếp theo:** Chuyển giao bộ tài liệu cho quy trình Independent External Review để kiểm tra chéo trước khi mở vòng chỉnh sửa hoặc xin phê duyệt chính thức từ người dùng.
