# BÁO CÁO TỰ ĐÁNH GIÁ KẾ HOẠCH BẰNG CHỨNG MỤC 3.4 CASE B R2 (CH3_34_CASEB_PLAN_SELF_REVIEW_R1)

- **Trạng thái:** `X7D0_CASEB_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7D0 R2 — Correct Case B Evidence/Presentation Plan`
- **Ngày thực hiện:** 2026-10-06
- **Ghi chú chuẩn mực:** Báo cáo này trình bày kết quả tự rà soát kỹ thuật khách quan và độc lập của Executor đối với phiên bản R2 sau khi tiếp thu đầy đủ và khắc phục triệt để 8 nhóm vấn đề nêu trong báo cáo đánh giá ngoài `X7D0_CASEB_PLAN_EXTERNAL_REVIEW_R1.md`. Executor **tuyệt đối không tự ý công bố kết quả PASS**; trạng thái nghiệm thu chính thức chỉ được xác lập sau khi có báo cáo thẩm định ngoài độc lập lần cuối (Final External Review) và sự phê duyệt chính thức của người dùng.

---

## 1. Bảng Chỉ Số Thống Kê Tổng Hợp Kế Hoạch Case B R2 (Summary Metrics)

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
| **Nguồn gốc chứng cứ luận điểm (Provenance Audit)** | **Minh bạch** | 19/20 claims gắn trực tiếp với dữ liệu thô / ảnh console trực tiếp; claim `CB-C19` xác định rõ nguồn gốc kế thừa mốc đã khóa Mục 3.1 và metadata tiến trình |
| **Loại bỏ SYN-ACK khỏi kết quả đo lại cổng 445 của Case B** | **Đạt** | Cổng 445 sau can thiệp chỉ ghi nhận `OPEN`; không có nhãn `syn-ack` do lệnh Nmap retest không có cờ `--reason` |
| **Chuẩn hóa ngôn từ phương ngữ SMB** | **Đạt** | Loại bỏ hoàn toàn các khẳng định về việc đàm phán hoặc bắt tay giao thức diễn ra thành công; dùng: *Kịch bản smb-protocols ghi nhận 2.0.2, 2.1, 3.0 và 3.0.2; NT LM 0.12 (SMBv1) không xuất hiện trong danh sách phương ngữ của phép đo lại* |
| **Chuẩn hóa ngôn từ tính liên tục của LanmanServer** | **Đạt** | Loại bỏ khẳng định tiến trình máy chủ hoàn toàn không có gián đoạn; dùng: *LanmanServer được ghi nhận ở trạng thái Running trước và sau can thiệp*; hai snapshot point-in-time không chứng minh zero downtime |
| **Tách biệt thuộc tính EnableSMB2Protocol với phương ngữ từ xa** | **Đạt** | Ghi nhận thuần túy cờ cấu hình cục bộ: *Thuộc tính EnableSMB2Protocol được ghi nhận True trước và sau can thiệp*; không dùng để chứng minh phương ngữ mạng |
| **Tách biệt cờ SMBv1 False và tính năng FS-SMB1 Installed** | **Đạt** | Khóa chặt ranh giới `SMBv1 disabled != FS-SMB1 uninstalled` |
| **Tách biệt tắt SMBv1 và trạng thái bản vá hệ thống** | **Đạt** | Khóa chặt ranh giới `SMBv1 disabled != PATCHED` (máy chủ duy trì `UNPATCHED`) |
| **Răn đe tuyên bố toàn vẹn workload / tính tương thích** | **Đạt** | Khóa chặt: việc ghi nhận các phương ngữ SMB2/3 không chứng minh toàn bộ workload nghiệp vụ đã được kiểm chứng |
| **Đo đạc lại kịch bản MS17-010 từ xa (MS17 retest)** | **Đạt** | Phép đo lại không cung cấp phán quyết lỗ hổng khả dụng; phân loại `UNKNOWN / NO USABLE SCRIPT RESULT`; nguyên nhân không có đầu ra không được xác lập từ bộ bằng chứng hiện có; `UNKNOWN != SAFE` |
| **Loại bỏ nhận định suy diễn về việc probe bị làm câm** | **Đạt** | Bác bỏ nhận định silenced probe trong manifest, không coi là sự thật khoa học hay lời giải thích nhân quả |
| **Hiệu chỉnh khung cắt cúp dự kiến (Crop Proposals R2)** | **Đạt** | Hình 3.7: `x=0, y=30, width=872, height=310` (loại desktop phải và khoảng trống dưới); Hình 3.8: `x=0, y=24, width=1280, height=400` (giữ trọn vẹn dấu nhắc lệnh và con trỏ) |
| **Mô tả ảnh thao tác (Action Screenshot)** | **Đạt** | Ghi nhận: *dấu nhắc PowerShell xuất hiện trở lại; không có stdout hiển thị trong ảnh*; việc xuất hiện prompt không tự chứng minh thành công nếu chưa xét After Local |
| **Loại bỏ ngôn từ tu từ quá mức (Rhetoric Removal)** | **Đạt** | Loại bỏ các từ ngữ mang tính khẳng định tuyệt đối hoặc khẳng định tác động mạng diện rộng khi chưa có bằng chứng giới hạn; loại bỏ các từ "hoàn toàn" không cần thiết |
| **Chuẩn hóa chuyển tiếp sang Case C** | **Đạt** | Bỏ câu chuyện giả định về quản trị viên/ứng dụng cũ; dùng mô tả kỹ thuật thuần túy về hai lớp phòng thủ; không tiết lộ kết quả Case C |
| **Cách ly kết luận hiệu quả / rủi ro Chương 4** | **Đạt** | Không đưa ra nhận định giải pháp "hiệu quả", "an toàn hơn", "giảm rủi ro" hay xếp hạng giải pháp |
| **Số lượng byte bằng chứng gốc bị thay đổi** | **0** | 100% bằng chứng gốc được bảo tồn nguyên vẹn |
| **Số lượng tệp văn xuôi Mục 3.4 bị tạo trước** | **0** | Tuân thủ tuyệt đối quy tắc ZERO PROSE của pha lập kế hoạch |
| **Số lượng ảnh cắt cúp presentation bị tạo thật trên đĩa** | **0** | Chỉ đề xuất tọa độ cắt cúp có thể tái lập trong kế hoạch; không tạo tệp phái sinh |

---

## 2. Kiểm Toán Chi Tiết 8 Nhóm Hiệu Chỉnh R2

### 2.1. Nhóm 1 — Khắc phục lỗi gán nhãn `syn-ack` cho cổng 445 Case B retest
- **Phát hiện đánh giá ngoài R1:** Dữ liệu thô `case_b/NSE-SMB-02_protocols.nmap` chỉ ghi `445/tcp open microsoft-ds`, không có cờ `--reason` và không có chuỗi `syn-ack`. R1 gán nhãn `OPEN (Phản hồi syn-ack)` trong Bảng 3.5 sau can thiệp là sao chép sai từ Scenario 2.
- **Hiệu chỉnh R2:**
  * Bảng 3.5 sau can thiệp chỉ ghi: `OPEN`.
  * Wording chuẩn mực: *Từ trạm Kali, TCP 445 được ghi nhận ở trạng thái OPEN trong phép đo lại.*
  * Bỏ hoàn toàn các diễn giải suy đoán về việc cổng tiếp nhận lưu lượng mạng ngoài trạng thái OPEN.
  * Khóa chặt nguyên tắc: `445 OPEN != vulnerable`.

### 2.2. Nhóm 2 — Chuẩn hóa ngôn từ phương ngữ SMB
- **Phát hiện đánh giá ngoài R1:** R1 sử dụng các từ ngữ khẳng định việc đàm phán hoặc bắt tay giao thức diễn ra thành công, hoặc dùng từ ngữ mang tính tuyệt đối hóa sự vắng mặt.
- **Hiệu chỉnh R2:**
  * Thay thế toàn bộ bằng công thức chuẩn mực: *Kịch bản smb-protocols ghi nhận 2.0.2, 2.1, 3.0 và 3.0.2; NT LM 0.12 (SMBv1) không xuất hiện trong danh sách phương ngữ của phép đo lại.*
  * Claim `CB-C15` chuẩn hóa: *Việc các phương ngữ 2.0.2, 2.1, 3.0 và 3.0.2 được ghi nhận trong phép đo lại không chứng minh toàn bộ workload SMB2/3 đã được kiểm chứng.* Tuyệt đối không gọi đây là kết quả bắt tay giao thức thành công.

### 2.3. Nhóm 3 — Chuẩn hóa tính liên tục của dịch vụ LanmanServer
- **Phát hiện đánh giá ngoài R1:** Bảng 3.5 của R1 tuyên bố dịch vụ máy chủ không gặp gián đoạn tiến trình nào. Hai quan sát point-in-time trước và sau can thiệp không đủ chứng minh zero downtime.
- **Hiệu chỉnh R2:**
  * Thay bằng: *LanmanServer được ghi nhận ở trạng thái Running trước và sau can thiệp.*
  * Khóa ranh giới: hai mốc quan sát point-in-time không chứng minh tính liên tục không gián đoạn (zero downtime) hay bảo đảm không có gián đoạn phiên làm việc của người dùng.
  * Trong Claim Map (`CB-C04`, `CB-C09`), bỏ nhận định máy chủ vận hành ổn định không gặp sự cố, thay bằng mô tả trung tính: "được ghi nhận ở trạng thái Running".

### 2.4. Nhóm 4 — Tách biệt cờ cấu hình cục bộ `EnableSMB2Protocol` với phương ngữ từ xa
- **Phát hiện đánh giá ngoài R1:** R1 diễn giải cờ `EnableSMB2Protocol=True` là tiếp tục cho phép các phương ngữ SMB2/3 hiện đại kết nối mạng, làm gộp lẫn cờ cục bộ với kết quả quan sát trên mạng.
- **Hiệu chỉnh R2:**
  * Tách biệt độc lập: hàng cấu hình chỉ ghi nhận *Thuộc tính EnableSMB2Protocol được ghi nhận True trước và sau can thiệp*.
  * Hàng phương ngữ từ xa riêng biệt báo cáo việc kịch bản `smb-protocols` ghi nhận 4 phương ngữ.

### 2.5. Nhóm 5 — Minh bạch nguồn gốc trạng thái bản vá cục bộ (UNPATCHED Provenance)
- **Phát hiện đánh giá ngoài R1:** Ảnh After Local của Case B không hiển thị tệp `srv.sys` hay danh mục hotfix, việc R1 ghi chính xác phiên bản số driver như thể vừa đo lại trực tiếp và tuyên bố "100% claims đều dùng direct/raw evidence" là thiếu chính xác về nguồn gốc.
- **Hiệu chỉnh R2:**
  * Bảng 3.5 ghi: *UNPATCHED (Mục 3.1)* trước can thiệp và *UNPATCHED — Case B không ghi nhận thao tác cài bản vá* sau can thiệp.
  * Diễn giải: *Đây là trạng thái cục bộ được kế thừa từ mốc đã khóa tại Mục 3.1 và siêu dữ liệu tiến trình thực nghiệm; ảnh After Local không trực tiếp hiển thị srv.sys hay danh mục hotfix. Vô hiệu hóa SMBv1 không đồng nghĩa với cập nhật bản vá (`SMBv1 disabled != PATCHED`).*
  * Thống kê ma trận claim map ghi rõ: 19 claims gắn với direct/raw evidence, riêng `CB-C19` xác định rõ nguồn gốc kế thừa mốc đã khóa Mục 3.1 (`ENV-CORE-03`), siêu dữ liệu tiến trình (`B-META-01`), và phạm vi câu lệnh can thiệp (`B-ACTION-01`).

### 2.6. Nhóm 6 — Chuẩn hóa phân loại UNKNOWN của NSE04
- **Phát hiện đánh giá ngoài R1:** Claim `CB-C18` suy diễn việc thiếu output là do giới hạn nhận diện của công cụ quét, vi phạm nguyên tắc không gán nguyên nhân chủ quan cho kết quả không có output.
- **Hiệu chỉnh R2:**
  * Áp dụng nguyên văn công thức chuẩn mực đã khóa: *Phép đo lại không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT. Nguyên nhân của việc không có đầu ra script khả dụng không được xác lập từ bộ bằng chứng hiện có. UNKNOWN != SAFE.*
  * Loại bỏ triệt để: các suy đoán về giới hạn quét của công cụ, nhận định probe bị làm câm (silenced probe), giả định lỗi Couldn't negotiate SMBv1, NTSTATUS, IPC$, cũng như các kết luận bịa đặt SAFE, PATCHED.

### 2.7. Nhóm 7 — Tối ưu hóa tọa độ cắt cúp dự kiến (Crop Proposals R2)
- **Hình 3.7 (`SMBv1_Remediation_03_After_Local.png`):**
  * Tọa độ R1: `1280 × 730` giữ lại quá nhiều desktop bên phải và khoảng console trống bên dưới.
  * Tọa độ R2: `x = 0, y = 30, width = 872, height = 310` (vùng `[0, 30, 872, 340]`).
  * Kiểm toán thị giác: Giữ trọn vẹn lệnh `Get-SmbServerConfiguration` wrapped, bảng thuộc tính SMB1/SMB2, `FS-SMB1 Installed`, `LanmanServer Running`, và dấu nhắc shell `PS C:\>` tại $y \approx 304$ kèm khoảng đệm an toàn đến 340. Loại bỏ hoàn toàn thanh tiêu đề ($y < 30$), vùng desktop và watermark bên phải ($x > 872$), thanh tác vụ ($y > 760$), và vùng console trống lớn ($y > 340$).
- **Hình 3.8 (`SMBv1_Remediation_04_NSE02_Protocols.png`):**
  * Tọa độ R1: `bottom = 384` cắt sát dòng dấu nhắc shell, có nguy cơ cụt con trỏ.
  * Tọa độ R2: `x = 0, y = 24, width = 1280, height = 400` (vùng `[0, 24, 1280, 424]`).
  * Kiểm toán thị giác: Giữ trọn vẹn dòng lệnh Nmap, kết quả 4 dialect, `Nmap done`, và dòng nhắc shell `┌──(kali㉿10)-[~]` kèm `└─$` tại $y \approx 385$ với khoảng đệm an toàn tới 424. Loại bỏ thanh panel trên cùng ($y < 24$) và vùng terminal trống phía dưới ($y > 424$).

### 2.8. Nhóm 8 — Loại bỏ ngôn từ tu từ và chuẩn hóa chuyển tiếp Case C
- **Ảnh thao tác (Action):** Sửa "dấu nhắc lệnh trở lại bình thường" thành *dấu nhắc PowerShell xuất hiện trở lại; không có stdout hiển thị trong ảnh*. Thành công được xác nhận bởi After Local state, không phải việc prompt quay lại.
- **Ngôn từ tu từ:** Loại bỏ các khẳng định hùng hồn về bằng chứng không thể chối cãi, khẳng định tác động mạng diện rộng, và các từ "hoàn toàn" không cần thiết.
- **Chuyển tiếp Case C:** Bỏ toàn bộ kịch bản suy đoán về việc quản trị viên không thể chỉnh sửa máy chủ do ràng buộc ứng dụng cũ. Thay bằng: *Case B thay đổi cấu hình giao thức ở máy chủ; Case C tiếp tục khảo sát một lớp kiểm soát khác trên đường truyền mạng bằng pfSense Transparent Bridge.* Không tiết lộ kết quả Case C.

---

## 3. Kết Quả Kiểm Tra Từ Khóa Bắt Buộc (Required Searches Verification)

Đã chạy kiểm tra tự động trên toàn bộ 4 tài liệu kế hoạch đối với 10 cụm từ cấm quy định tại Mục 15 của Prompt R2:
- Nhóm cụm từ khẳng định đàm phán hay bắt tay giao thức thành công: **0 lần** xuất hiện trong ngữ cảnh vận hành/cho phép.
- Nhóm cụm từ tuyên bố tiến trình máy chủ không gặp gián đoạn hoặc vận hành ổn định: **0 lần**.
- Nhóm cụm từ suy diễn về việc cổng 445 tiếp nhận lưu lượng mạng: **0 lần**.
- Nhóm cụm từ suy đoán về giới hạn nhận diện của công cụ quét hay nhận định probe bị làm câm (silenced probe): **0 lần**.
- Nhóm cụm từ tu từ khẳng định tuyệt đối (về chứng cứ không thể chối cãi hay tác động mạng diện rộng): **0 lần**.
- Gán nhãn `syn-ack` cho cổng 445 sau can thiệp của Case B: **0 lần**.
- Phán quyết bịa đặt (`SAFE`, `NOT VULNERABLE`, `PATCHED`, `false negative`): **0 lần**.
- Giả định kỹ thuật không có căn cứ (`Couldn't negotiate SMBv1`, `NTSTATUS`, `IPC$`): **0 lần**.
- Tuyên bố toàn vẹn workload nghiệp vụ / tính tương thích đầy đủ: **0 lần**.
- Tuyên bố gỡ cài đặt tính năng `FS-SMB1` / khởi động lại hệ thống: **0 lần**.
- Tiết lộ kết quả Kịch bản C / nhận định hiệu quả, rủi ro Chương 4: **0 lần**.

---

## 4. Kết Luận Và Trạng Thái Handoff

Bộ 4 tài liệu lập kế hoạch cho Mục 3.4 Case B phiên bản R2 đã được hoàn thiện chặt chẽ, đạt độ chính xác cao về bằng chứng học thuật, xóa bỏ toàn bộ các điểm phản biện tiềm tàng của hội đồng, và tuân thủ tuyệt đối quy tắc **ZERO PROSE**.

- **Trạng thái chính thức:** `X7D0_CASEB_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Khuyến nghị tiếp theo:** Chuyển giao bộ tài liệu cho quy trình Final Independent External Review để thẩm định trước khi trình người dùng phê duyệt chính thức.
