# BÁO CÁO LỰA CHỌN VÀ ĐÁNH GIÁ HÌNH ẢNH MỤC 3.4 CASE B (CH3_34_CASEB_FIGURE_SELECTION_R1)

- **Trạng thái:** `R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7D0 R1 — Case B Evidence & Presentation Plan`
- **Mục tiêu:** Thẩm tra toàn diện bằng chứng thị giác Kịch bản giảm thiểu Case B (Vô hiệu hóa SMBv1), phân loại giá trị gia tăng từng ảnh, ngăn chặn triệt để tình trạng "album ảnh chụp màn hình", và đề xuất khung cắt cúp dự kiến có thể tái lập phục vụ trang in A4.
- **Phạm vi thẩm tra thực tế:** Toàn bộ 12 tệp bằng chứng Case B canonical đã stage tại `work/do-an/chapter3/evidence/case_b/`:
  - 5 tệp ảnh chụp màn hình trực tiếp: `SMBv1_Remediation_01_Before.png`, `SMBv1_Remediation_02_Action.png`, `SMBv1_Remediation_03_After_Local.png`, `SMBv1_Remediation_04_NSE02_Protocols.png`, `SMBv1_Remediation_05_NSE04_MS17010.png`
  - 2 bộ ba tệp thô máy đọc (`.nmap`, `.xml`, `.gnmap` cho `NSE-SMB-02_protocols` và `NSE-SMB-04_ms17010`, tổng cộng 6 tệp)
  - 1 tệp siêu dữ liệu thực thi: `SMBv1_Remediation_Run_Manifest.txt`

---

## 1. Kiểm Toán Sai Lệch Siêu Dữ Liệu (Staged Evidence & Metadata Discrepancy Audit)

Trong quá trình đối soát giữa tệp điều hành `SMBv1_Remediation_Run_Manifest.txt` và thư mục lưu trữ canonical `work/do-an/chapter3/evidence/case_b/`, ghi nhận một sai lệch siêu dữ liệu bắt buộc phải khóa ranh giới:

1. **Nội dung tệp manifest ghi chép:**
   - Dòng 57–59: `EXPECTED: 6`, `ACTUAL: 6`, `MISSING: 0`
   - Dòng 60: `SCREENSHOT RAW EVIDENCE: SMBv1_Remediation_06_Raw_Evidence.png`
2. **Thực tế thư mục canonical staged:**
   - Thư mục `work/do-an/chapter3/evidence/case_b/` chỉ có đúng **5 tệp ảnh chụp màn hình** (từ `01` đến `05`), 2 bộ ba raw Nmap (6 tệp) và 1 manifest, tổng cộng đúng **12 tệp**.
   - Tệp `SMBv1_Remediation_06_Raw_Evidence.png` **hoàn toàn không tồn tại** trong kho bằng chứng staged.
3. **Quy tắc xử lý bắt buộc trong kế hoạch:**
   - Ghi nhận đây là một **sai lệch siêu dữ liệu (metadata/staging discrepancy)** giữa bản ghi manifest lịch sử và thư mục bằng chứng thực tế.
   - **Tuyệt đối không tự ý tạo ra, không phục hồi giả định, không coi tệp `06` là tồn tại, và không trích dẫn tệp `06`** như một nguồn chứng minh.
   - **Tuyệt đối không sử dụng dòng `EXPECTED: 6 / ACTUAL: 6`** trong manifest để tuyên bố có 6 ảnh chụp màn hình đã stage.
   - Mọi phân tích và đề xuất trình bày chỉ dựa trên **12 tệp bằng chứng thực tế hiện hữu**.

---

## 2. Bảng Đánh Giá Chi Tiết Toàn Bộ 5 Ảnh Chụp Màn Hình Case B

| Tệp ảnh gốc (File) | Giai đoạn Case B | Nội dung hiển thị trực tiếp (Directly shows) | Tính độc bản so với Mục 3.1–3.3? (Unique vs earlier sections?) | Bảng có thể thay thế? (Better as table?) | Giá trị đối chiếu Trước/Sau (Before/After value) | Độ sắc nét (Legibility) | Cần cắt cúp? (Crop needed?) | Phân loại (KEEP / OPTIONAL / DROP) | Lý do & Đề xuất sử dụng (Reason & Proposed use) |
|---|---|---|---|---|---|---|---|---|---|
| `SMBv1_Remediation_01_Before.png` | Trước can thiệp (Before local) | PowerShell console: `LanmanServer` Running; `FS-SMB1` Installed; `EnableSMB1Protocol : True`; `EnableSMB2Protocol : True` | **Không**. Các thuộc tính này hoàn toàn trùng lặp với mốc chuẩn baseline đã được khóa và trình bày trực quan tại Mục 3.1 (Hình 3.2). | **Có hoàn toàn**. 4 thuộc tính được tích hợp trọn vẹn vào cột "Trước can thiệp" của Bảng 3.5. | Thấp (chỉ nhắc lại trạng thái baseline đã biết). | Tốt (1280×800), chữ trắng trên nền xanh PowerShell. | Có (loại bỏ thanh tiêu đề và khoảng trống). | **DROP** | **Loại bỏ**. Tránh lặp lại ảnh chụp trạng thái ban đầu của Windows Server đã được xác lập từ Mục 3.1. Cột baseline trong Bảng 3.5 thể hiện đầy đủ thông tin này mà không tốn diện tích trang in. |
| `SMBv1_Remediation_02_Action.png` | Thao tác can thiệp (Action) | PowerShell console: thực thi lệnh `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`; dấu nhắc lệnh trở lại bình thường, không có đầu ra (zero stdout). | **Không mang thông tin thị giác mới**. Chỉ hiển thị một dòng lệnh duy nhất không có dữ liệu trả về. | **Có hoàn toàn**. Thao tác thực thi câu lệnh cấu hình được mô tả mạch lạc trong văn xuôi và ghi nhận trong Bảng 3.5. | Rất thấp (không có dữ liệu kết quả để đối chiếu). | Tốt (1280×800). | Có. | **DROP** | **Loại bỏ**. Không đưa vào báo cáo một ảnh chụp màn hình chỉ để hiển thị một dòng lệnh không có kết quả đầu ra. Việc này gây lãng phí trang in và tạo cảm giác "nhật ký thao tác" (command log). |
| `SMBv1_Remediation_03_After_Local.png` | Sau can thiệp cục bộ (After local) | PowerShell console: `EnableSMB1Protocol : False`; `EnableSMB2Protocol : True`; `FS-SMB1` Installed; `LanmanServer` Running. | **Có (Độc bản & Trọng yếu)**. Minh chứng trực tiếp kết quả thay đổi cấu hình nội bộ của máy chủ sau can thiệp: SMBv1 chuyển thành False, SMB2 giữ True, tính năng Windows vẫn Installed, và dịch vụ Server tiếp tục Running. | Bảng 3.5 ghi nhận các giá trị này, nhưng ảnh chụp cung cấp bằng chứng thị giác gốc không thể bác bỏ về hiện trạng cục bộ ngay sau can thiệp. | **Rất cao (Bằng chứng cục bộ cốt lõi)**. Chứng minh trực quan sự phân tách: tắt cấu hình SMBv1 nhưng tính năng hệ điều hành không bị gỡ bỏ (`SMBv1 disabled != FS-SMB1 uninstalled`). | Rất tốt (1280×800), các dòng trạng thái sắc nét, rõ ràng. | Có (cắt bỏ thanh tiêu đề PowerShell, thanh tác vụ Windows và vùng trống phía dưới). | **KEEP (Ưu tiên 1)** | **Hình 3.7 (Tạm thời)**. Bằng chứng thực nghiệm trung tâm về trạng thái máy chủ cục bộ sau can thiệp, chứng minh SMB1=False trong khi FS-SMB1 vẫn Installed và LanmanServer vẫn Running. |
| `SMBv1_Remediation_04_NSE02_Protocols.png` | Đo đạc lại giao thức từ xa (Protocol retest) | Terminal Kali Linux: `nmap -p 445 -n -T3 --max-retries 2 --script smb-protocols 192.168.56.20`. Kết quả: `445/tcp open`, kịch bản `smb-protocols` ghi nhận 4 phương ngữ: `2.0.2`, `2.1`, `3.0`, `3.0.2`. `NT LM 0.12 (SMBv1)` hoàn toàn vắng mặt. | **Có (Độc bản & Trọng yếu)**. Khác biệt rõ rệt so với Hình 3.5 ở Mục 3.2: phương ngữ SMBv1 đã biến mất khỏi danh sách đàm phán, trong khi các phương ngữ SMB2/3 vẫn được ghi nhận. | Bảng 3.5 tóm lược danh sách phương ngữ, nhưng ảnh cung cấp bằng chứng trực quan về phản hồi đo đạc từ xa của Nmap. | **Rất cao (Bằng chứng từ xa cốt lõi)**. Minh chứng hiệu ứng quan sát được từ xa của việc can thiệp: phương ngữ SMBv1 không còn xuất hiện trong đàm phán mạng. | Rất tốt (1280×800), phông chữ terminal Kali sắc nét trên nền tối. | Có (cắt bỏ panel trên desktop Kali và vùng đen trống phía dưới terminal). | **KEEP (Ưu tiên 2)** | **Hình 3.8 (Tạm thời)**. Bằng chứng thực nghiệm trung tâm từ góc nhìn trạm quét từ xa, chứng minh trực quan sự biến mất của phương ngữ SMBv1 trong khi cổng 445 vẫn mở và SMB2/3 vẫn phản hồi. |
| `SMBv1_Remediation_05_NSE04_MS17010.png` | Đo đạc lại MS17-010 từ xa (Retest tổng hợp) | Terminal Kali Linux: chứa cả hai lượt quét liên tiếp: (1) `smb-protocols` (hiển thị 4 phương ngữ SMB2/3); (2) `smb-vuln-ms17-010` (hiển thị cổng 445 mở, hoàn tất `Nmap done`, không xuất hiện `Host script results:`). | **Bán độc bản**. Phần quét phương ngữ trùng với ảnh 04; phần MS17-010 hiển thị kết quả quét hoàn tất không có phán quyết (tương tự như Hình 3.6 ở Mục 3.3). | Bảng 3.5 thể hiện rõ ràng cả hai kết quả đo lại này. | Trung bình đối với A4: chứa cả hai kết quả nhưng khiến khung hình dài và chữ bị thu nhỏ nếu đặt trên một trang portrait. | Rất tốt (1280×800). | Có (cắt bỏ panel trên và khoảng trống dưới). | **OPTIONAL / DROP** | **Dự phòng / Loại bỏ trong phương án chính**. Trong phương án 2 hình khuyến nghị, ảnh này được loại bỏ (DROP) để tránh quá tải thị giác trên trang in A4 và tránh lặp lại cấu trúc hiển thị trống của kịch bản MS17-010 đã có ở Hình 3.6. Được lưu giữ làm phương án dự phòng nếu hội đồng yêu cầu gom 2 phép đo lại vào 1 ảnh terminal duy nhất. |

---

## 3. Phân Tích Chuyên Sâu Về Giá Trị Thị Giác Và Trình Bày A4

### 3.1. Đánh giá tính dư thừa của ảnh Trước (01) và Thao tác (02)
- **Ảnh `01_Before`:** Tại Mục 3.1, luận văn đã trình bày chi tiết và phê duyệt Hình 3.2 minh chứng đầy đủ dịch vụ `LanmanServer` Running, tính năng `FS-SMB1` Installed, và các cờ cấu hình SMB1/SMB2 kích hoạt. Nếu đưa lại ảnh `01_Before` vào Mục 3.4, người đọc sẽ thấy một ảnh chụp PowerShell có nội dung gần như tương tự. Do đó, việc chuyển thông số ban đầu vào cột "Trước can thiệp" của Bảng 3.5 là giải pháp tối ưu.
- **Ảnh `02_Action`:** Lệnh PowerShell `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` được thực thi mà không có thông báo hay bảng dữ liệu nào xuất hiện trên màn hình console (chỉ trở về dấu nhắc `PS C:\>`). Một bức ảnh chụp dòng lệnh trơ trọi không đem lại giá trị học thuật hay phân tích kỹ thuật. Thao tác này được trình bày chuẩn xác qua văn bản và đối chiếu với kết quả ở ảnh `03_After_Local`.

### 3.2. Giá trị cốt lõi của ảnh Sau can thiệp cục bộ (03_After_Local)
- Ảnh `03_After_Local` là bằng chứng then chốt chứng minh việc can thiệp cấu hình đã thực sự diễn ra và có hiệu lực trên máy chủ:
  1. `EnableSMB1Protocol : False` (Cấu hình máy chủ SMBv1 đã tắt).
  2. `EnableSMB2Protocol : True` (SMB2/3 vẫn tiếp tục kích hoạt).
  3. `FS-SMB1 : Installed` (Tính năng thành phần của hệ điều hành vẫn tồn tại, không bị gỡ bỏ).
  4. `LanmanServer : Running` (Dịch vụ chia sẻ tệp của Windows vẫn đang hoạt động).
- Bức ảnh này là mỏ neo trực quan giúp khóa chặt hai kết luận phương pháp luận bắt buộc:
  - `SMBv1 disabled != FS-SMB1 uninstalled`
  - `SMBv1 disabled != PATCHED`

### 3.3. So sánh lựa chọn giữa `04_NSE02_Protocols` và `05_NSE04_MS17010`
- **Phương án chọn ảnh 04 (`NSE02_Protocols`):**
  - Trọng tâm của ảnh 04 là **kết quả quan sát dương tính có sự thay đổi rõ rệt**: phương ngữ SMBv1 cũ (`NT LM 0.12`) hoàn toàn biến mất khỏi danh sách dialect, chỉ còn lại `2.0.2`, `2.1`, `3.0`, `3.0.2`.
  - Đây là bằng chứng đo đạc từ xa trực quan nhất cho thấy việc thay đổi cấu hình cục bộ đã tác động ra mạng ngoài.
  - Chiều cao nội dung terminal vừa phải ($y \approx 24$ đến $384$, khoảng 360 px), tỷ lệ khung hình rất đẹp khi dàn trang A4 portrait, giúp cỡ chữ dòng lệnh và bảng phương ngữ hiển thị to, rõ ràng.
- **Phương án chọn ảnh 05 (`NSE04_MS17010`):**
  - Ảnh 05 chụp lại cả hai lần chạy lệnh trong cùng một cửa sổ terminal: lượt quét protocols phía trên và lượt quét ms17-010 phía dưới.
  - Tuy nhiên, phần quét `smb-vuln-ms17-010` phía dưới chỉ hiển thị: cổng 445 mở, `Nmap done`, không có khối `Host script results:`. Nội dung này hoàn toàn tương tự như Hình 3.6 ở Mục 3.3 (vẫn là kết quả UNKNOWN).
  - Chiều cao nội dung của ảnh 05 lên tới hơn 520 px. Khi chèn vào trang A4 portrait, ảnh sẽ chiếm gần nửa trang hoặc buộc phải co nhỏ lại, làm giảm độ sắc nét và khả năng đọc của người chấm luận văn.
- **Kết luận đánh giá:** Ảnh `04_NSE02_Protocols` mang giá trị thông tin thị giác cao hơn hẳn cho việc minh chứng hiệu ứng thay đổi phương ngữ. Kết quả đo lại kịch bản MS17-010 được hệ thống hóa chuẩn xác qua Bảng 3.5 và văn xuôi phân định ranh giới.

---

## 4. Tổng Hợp Phân Bổ Hình Ảnh Đề Xuất Cho Mục 3.4

### 4.1. Thống kê phân loại
- **Tổng số tệp ảnh đã thẩm tra:** 5 ảnh.
- **Số lượng KEEP (Giữ lại):** 2 ảnh (`SMBv1_Remediation_03_After_Local.png`, `SMBv1_Remediation_04_NSE02_Protocols.png`).
- **Số lượng OPTIONAL (Dự phòng):** 1 ảnh (`SMBv1_Remediation_05_NSE04_MS17010.png`).
- **Số lượng DROP (Loại bỏ):** 2 ảnh (`SMBv1_Remediation_01_Before.png`, `SMBv1_Remediation_02_Action.png`).
- **Số lượng tệp ảnh tạo mới trên đĩa:** 0 (Tuân thủ nghiêm ngặt quy tắc chỉ lập kế hoạch).

### 4.2. Phương án Khuyến nghị Chính thức (Phương án Tiêu chuẩn — 2 Hình)

Áp dụng mô hình **1 minh chứng cục bộ + 1 minh chứng từ xa**, bảo đảm tính cân đối hoàn hảo giữa hai tầng thực nghiệm:

#### 1. Hình 3.7 (Tạm thời) — Trạng thái cấu hình máy chủ, tính năng hệ điều hành và dịch vụ SMB cục bộ sau khi vô hiệu hóa SMBv1
- **Tệp nguồn:** `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_03_After_Local.png`
- **SHA-256 nguồn:** `2f762508ec98da3b6ed75813c32ed5622cbe1c982e6e6e2907086152e9a6a6ad`
- **Kích thước gốc:** $1280 \times 800\,\text{px}$.
- **Vị trí đề xuất:** Đặt trong Tiểu mục `3.4.1`, ngay sau đoạn phân tích kết quả thay đổi cấu hình máy chủ cục bộ.
- **Chú thích đề xuất:** *Hình 3.7. Trạng thái cấu hình máy chủ, tính năng hệ thống và dịch vụ LanmanServer cục bộ sau khi vô hiệu hóa SMBv1*
- **Vai trò chứng minh:** Minh chứng khách quan rằng cờ cấu hình `EnableSMB1Protocol` đã chuyển sang giá trị `False`, trong khi `EnableSMB2Protocol` duy trì `True`, tính năng `FS-SMB1` vẫn ở trạng thái `Installed`, và dịch vụ `LanmanServer` tiếp tục hoạt động (`Running`).
- **Ranh giới diễn giải:** Bức ảnh chỉ chứng minh thay đổi cấu hình mức máy chủ; tuyệt đối không chứng minh tính năng Windows đã bị gỡ bỏ, không chứng minh tệp driver `srv.sys` đã được cập nhật bản vá, và không chứng minh tính tương thích toàn diện của mọi ứng dụng nghiệp vụ hiện đại.
- **Khung cắt cúp đề xuất có thể tái lập (Provisional Reproducible Crop Rectangle):**
  - *Tọa độ nguồn đề xuất:* `x = 0, y = 30, width = 1280, height = 730` (tương ứng vùng `[left=0, top=30, right=1280, bottom=760]`).
  - *Vùng thông tin phải giữ:* Toàn bộ khối nội dung console PowerShell hiển thị kết quả của 3 lệnh kiểm tra (`Get-SmbServerConfiguration`, `Get-WindowsFeature FS-SMB1`, `Get-Service LanmanServer`) cùng dấu nhắc lệnh kế tiếp.
  - *Giao diện thừa loại bỏ:* Thanh tiêu đề cửa sổ console ($y < 30$) và thanh tác vụ Windows Server ở đáy màn hình ($y > 760$).
  - *Mục đích trình bày:* Loại bỏ các viền desktop không liên quan, mở rộng diện tích hiển thị văn bản console trên trang in A4 portrait.

#### 2. Hình 3.8 (Tạm thời) — Kết quả đo đạc lại các phương ngữ SMB từ trạm Kali Linux sau can thiệp
- **Tệp nguồn:** `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_04_NSE02_Protocols.png`
- **SHA-256 nguồn:** `21ed6473f4e7010841e9730620b159c272238cf7335eb80fcfaf4ad61f7a7b5a`
- **Kích thước gốc:** $1280 \times 800\,\text{px}$.
- **Vị trí đề xuất:** Đặt trong Tiểu mục `3.4.2`, ngay sau đoạn mô tả phép đo đạc lại phương ngữ từ xa bằng kịch bản `smb-protocols`.
- **Chú thích đề xuất:** *Hình 3.8. Kết quả đo đạc lại các phương ngữ SMB từ trạm Kali Linux sau khi vô hiệu hóa SMBv1*
- **Vai trò chứng minh:** Minh chứng khách quan từ trạm kiểm thử Kali Linux rằng cổng `445/tcp` vẫn ở trạng thái `open`, kịch bản `smb-protocols` ghi nhận các phương ngữ `2.0.2`, `2.1`, `3.0`, `3.0.2`, và phương ngữ cũ `NT LM 0.12 (SMBv1)` hoàn toàn không còn xuất hiện trong phản hồi đàm phán.
- **Ranh giới diễn giải:** Bức ảnh chứng minh phương ngữ SMBv1 không còn xuất hiện trong phép thương lượng đã đo; tuyệt đối không chứng minh cổng 445 đã đóng, không chứng minh toàn bộ mã độc SMBv1 không còn khả năng tác động qua các đường dẫn khác, không chứng minh toàn bộ workload nghiệp vụ SMB2/3 đã được kiểm thử, và không đưa ra phán quyết về lỗ hổng MS17-010.
- **Khung cắt cúp đề xuất có thể tái lập (Provisional Reproducible Crop Rectangle):**
  - *Tọa độ nguồn đề xuất:* `x = 0, y = 24, width = 1280, height = 360` (tương ứng vùng `[left=0, top=24, right=1280, bottom=384]`).
  - *Vùng thông tin phải giữ:* Dòng lệnh Nmap `smb-protocols`, trạng thái host/cổng, khối kết quả `Host script results:` liệt kê 4 phương ngữ SMB2/3, thông báo hoàn tất `Nmap done`, và dấu nhắc lệnh shell kế tiếp.
  - *Giao diện thừa loại bỏ:* Thanh panel desktop Kali XFCE trên cùng ($y < 24$) và vùng không gian đen trống phía dưới terminal ($y > 384$, tương ứng hơn 400 pixel trống).
  - *Mục đích trình bày:* Tối ưu hóa tỷ lệ khung hình hiển thị trên A4, cỡ chữ dòng lệnh và kết quả script to, rõ ràng, không bị méo tỷ lệ.

---

## 5. Các Phương Án Thay Thế Dự Phòng (Alternative Options)

### 5.1. Phương án Rút gọn (Lean Alternative — 1 Hình)
- Trong trường hợp dung lượng trang in của đồ án bị giới hạn nghiêm ngặt:
  - Chỉ giữ lại **Hình 3.7 (Tạm thời)** (`SMBv1_Remediation_03_After_Local.png`) làm minh chứng thị giác duy nhất.
  - Kết quả đo lại phương ngữ từ xa được trình bày hoàn toàn trong Bảng 3.5.
  - *Đánh giá:* Rất tinh gọn, nhưng làm giảm tính trực quan của hiệu ứng mạng từ xa (người đọc không nhìn thấy trực tiếp danh sách dialect mới trên terminal Nmap).

### 5.2. Phương án Thay thế Terminal Tổng hợp (Alternative 2 — 2 Hình với Terminal kép)
- Nếu hội đồng yêu cầu phải có bằng chứng thị giác trực tiếp cho cả phép đo lại `smb-vuln-ms17-010`:
  - Thay thế `SMBv1_Remediation_04_NSE02_Protocols.png` bằng `SMBv1_Remediation_05_NSE04_MS17010.png` làm **Hình 3.8 (Tạm thời)**.
  - Khung cắt cúp dự kiến cho ảnh 05:
    * *Tọa độ:* `x = 0, y = 24, width = 1280, height = 520` (vùng `[left=0, top=24, right=1280, bottom=544]`).
    * *Vùng giữ lại:* Bao gồm cả khối lệnh và kết quả của `smb-protocols` lẫn `smb-vuln-ms17-010`.
  - *Nhược điểm:* Khung ảnh cao (520 px), chiếm diện tích lớn trên trang A4; phần kết quả MS17-010 không có output mới so với Mục 3.3, có nguy cơ gây rối mắt cho người đọc.
- **Khuyến nghị chính thức của Executor:** Giữ nguyên **Phương án Khuyến nghị Chính thức (Hình 3.7 là ảnh 03, Hình 3.8 là ảnh 04)**. Đây là phương án khoa học, đẹp mắt và sắc nét nhất trên ấn bản in A4.
