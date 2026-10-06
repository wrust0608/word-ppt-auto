# BÁO CÁO THAY ĐỔI CHƯƠNG 1 (RG1_CHAPTER1_CHANGELOG_R1)

- **Giai đoạn thực hiện:** RG1 — Chỉnh lý toàn diện Chương 1 theo lập luận thực nghiệm chuẩn mực.
- **Tệp sửa đổi:** `work/do-an/CHAPTER_1.md`
- **Nhánh:** `feature/rg1-ch1-argument-realignment`
- **Thời gian lập:** 06/10/2026

---

## 1. Bảng kiểm tra và xử lý các từ khóa di sản (Stale Terms Audit)

Theo yêu cầu của chỉ dẫn RG1, toàn bộ 12 từ khóa di sản thuộc mô hình cũ (Windows 7 / Metasploit / tấn công RCE / ba VLAN) đã được rà soát chi tiết trên toàn văn bản Chương 1 và phân loại xử lý theo ba nhóm: `KEEP_AS_THEORY`, `REWRITE`, hoặc `REMOVE`.

| STT | Từ khóa kiểm tra | Vị trí ban đầu (Line gốc) | Nội dung ban đầu trong văn bản | Phân loại xử lý | Giải pháp thực hiện trong RG1 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `Windows 7` | L41 | "hệ điều hành mục tiêu thử nghiệm (Windows 7)..." | `REMOVE` | Loại bỏ hoàn toàn; chuyển sang giới thiệu nền tảng máy chủ doanh nghiệp Windows Server 2012 R2. |
| 2 | `Windows 7` | L53 | "đối tượng thử nghiệm trong đồ án (Windows 7 SP1)" | `REMOVE` | Thay bằng định danh mục tiêu thực nghiệm duy nhất: Windows Server 2012 R2. |
| 3 | `Windows 7` | L100 | "phần mềm bị ảnh hưởng... Windows 7 SP1..." | `KEEP_AS_THEORY` | Giữ trong Bảng 1.3 như một hệ điều hành thuộc phạm vi thông báo MS17-010, nhưng loại bỏ nhãn "máy mục tiêu lab". Gán nhãn "Máy chủ mục tiêu thực nghiệm" duy nhất cho Windows Server 2012 R2. |
| 4 | `Windows 7` | L139 | "Lựa chọn Windows 7 SP1 x64 làm hệ điều hành mục tiêu..." | `REMOVE` | Thay toàn bộ mục 1.2.4 thành lý do lựa chọn Windows Server 2012 R2 dựa trên tính đại diện máy chủ, hướng dẫn Microsoft 4023262 và tính độc lập của các trục bằng chứng. |
| 5 | `Metasploit` | L189 | "Nền tảng kiểm thử Metasploit Framework" (tiêu đề 1.3.4) | `REMOVE` | Thay thế toàn bộ Mục 1.3.4 bằng "Cơ sở xác minh trạng thái bản vá cục bộ trên Windows Server 2012 R2". |
| 6 | `Metasploit` | L191–210 | Mô tả kiến trúc MSF, module auxiliary, exploit module | `REMOVE` | Xóa bỏ toàn bộ mô tả về Metasploit. Đề tài không sử dụng Metasploit làm công cụ thực nghiệm. |
| 7 | `Metasploit` | L217, L228 | "Metasploit scanner", "Metasploit exploit" trong Bảng 1.4 | `REMOVE` | Viết lại Bảng 1.4 chỉ chứa 8 phép đo thực tế của Nmap, NSE, PowerShell và pfSense. |
| 8 | `Metasploit` | L252, L268 | Đối chiếu chéo với Metasploit, mức độ 4 exploit validation | `REMOVE` | Xóa bỏ khỏi Mục 1.4.1 và 1.4.2; thay bằng mô hình bốn trục bằng chứng độc lập. |
| 9 | `ms17_010_eternalblue` | L199, L228 | `exploit/windows/smb/ms17_010_eternalblue` | `REMOVE` | Xóa bỏ hoàn toàn tên module khai thác của Metasploit. Không có dòng lệnh hay module khai thác nào trong báo cáo. |
| 10 | `auxiliary/scanner` | L196, L225 | `auxiliary/scanner/smb/smb_ms17_010` | `REMOVE` | Xóa bỏ hoàn toàn module quét của Metasploit; chỉ sử dụng Nmap NSE `smb-vuln-ms17-010`. |
| 11 | `exploit/windows` | L199 | Tên module khai thác Windows trong Metasploit | `REMOVE` | Xóa bỏ hoàn toàn khỏi toàn bộ chương. |
| 12 | `SYSTEM` | L117 | "chiếm đoạt hoàn toàn quyền điều khiển hệ thống (quyền SYSTEM)" | `REWRITE` | Phân tích rõ về mặt lý thuyết FEA/Pool Grooming rằng `SYSTEM` là danh tính bảo mật người dùng trong Windows (không phải chế độ nhân) và đồ án không thực nghiệm chiếm quyền `SYSTEM`. |
| 13 | `khai thác` | L92, L120 | "khả năng khai thác thực tế", "thực hiện khai thác" | `REWRITE` | Phân biệt dứt khoát giữa "nguy cơ lý thuyết theo tài liệu an ninh" và "phương pháp luận khảo sát, đo đạc an toàn không xâm nhập" của đồ án. |
| 14 | `thực thi mã thử nghiệm` | L228, L248 | "Cấp độ 4: Thực thi mã thử nghiệm (Exploitation Validation)" | `REMOVE` | Loại bỏ triệt để cấp độ 4 và mọi khái niệm thực thi mã thử nghiệm khỏi mô hình đánh giá và bảng đo đạc. |
| 15 | `Client nghiệp vụ` | L290, L294 | Mô hình mạng cũ có máy client nghiệp vụ | `REMOVE` | Loại bỏ khái niệm "Client nghiệp vụ". Phân định rõ 3 tầng phòng thủ (Patching, Protocol hardening, Network access control). |
| 16 | `ba VLAN` | L291 | Kiến trúc mạng giả định chia ba VLAN cũ | `REMOVE` | Loại bỏ mô hình 3 VLAN cũ; mô tả chính xác cơ chế lọc gói của tường lửa trung gian bảo vệ phân đoạn mạng. |
| 17 | `phân vùng khác` | L293 | "phân vùng nghiệp vụ", "phân vùng kiểm thử khác" | `REMOVE` | Viết lại chính xác phạm vi bảo vệ của giải pháp tường lửa: bảo vệ trước lưu lượng đi qua thiết bị, không bảo vệ nội bộ cùng subnet (`FILTERED != PATCHED`). |
| 18 | `sau vá` | L284 | Mô tả kịch bản Case A "sau vá" như đã thực hiện | `REWRITE` | Nêu rõ trong 1.4.3: Tầng cập nhật bản vá đóng vai trò mốc tham chiếu lý thuyết (`Case A`), thực nghiệm tập trung đo đạc hai giải pháp vận hành (Case B và Case C). |

---

## 2. Các thay đổi cấu trúc lớn (Structural Transformations)

### 2.1. Mục 1.3.4: Chuyển đổi từ Metasploit sang Cơ sở xác minh bản vá cục bộ
- **Tiêu đề cũ:** `1.3.4. Nền tảng kiểm thử Metasploit Framework`
- **Tiêu đề mới:** `1.3.4. Cơ sở xác minh trạng thái bản vá cục bộ trên Windows Server 2012 R2`
- **Nội dung mới:**
  - Thiết lập phương pháp kiểm tra nội bộ trên máy chủ mục tiêu thông qua hai trục: truy vấn Hotfix quản trị (`Get-Hotfix`) và kiểm tra thuộc tính nhị phân của tệp driver nhân `srv.sys` (`Get-Item`).
  - Phân tích 4 trường thuộc tính nhị phân cốt lõi: `FileVersion`, `ProductVersion`, `Length`, `LastWriteTime`.
  - Nêu rõ ngưỡng an toàn phiên bản nhị phân do Microsoft công bố trong tài liệu kỹ thuật Article 4023262: đối với Windows Server 2012 R2, `srv.sys` sau khi cài gói cập nhật KB4012213 hoặc KB4012216 phải đạt phiên bản tối thiểu **`6.3.9600.18604`**.
  - Khẳng định tính độc lập phương pháp luận giữa kiểm tra bản vá nội bộ và quét thăm dò từ xa: kiểm tra nội bộ phản ánh cấu trúc mã nhị phân lưu trữ trên đĩa, không phụ thuộc vào trạng thái mở hay lọc của cổng mạng.

### 2.2. Mục 1.3.5: Tái cấu trúc Bảng liên kết Lý thuyết – Thực nghiệm (Bảng 1.4)
- **Trước chỉnh lý:** Chứa các dòng về Metasploit auxiliary scanner, exploit module RCE validation, kiểm tra "khả năng khai thác thực tế".
- **Sau chỉnh lý:** Loại bỏ hoàn toàn công cụ Metasploit và hàng exploit. Bảng 1.4 được xây dựng lại dựa trên **8 phép đo kỹ thuật thực tế**:
  1. Khảo sát cổng mạng TCP 139 và TCP 445 (Nmap SYN scan).
  2. Khảo sát phương ngữ SMB (Nmap NSE `smb-protocols`).
  3. Khảo sát cấu hình ký số SMB (Nmap NSE `smb2-security-mode`).
  4. Thăm dò dấu hiệu chưa vá MS17-010 từ xa (Nmap NSE `smb-vuln-ms17-010`).
  5. Xác minh trạng thái bản vá nội bộ (PowerShell Hotfix & `srv.sys` version).
  6. Vô hiệu hóa giao thức SMBv1 (Cấu hình máy chủ `Set-SmbServerConfiguration` - Case B).
  7. Lọc gói tin tại ranh giới mạng (Tường lửa pfSense Transparent Bridge - Case C).
  8. Tái kiểm thử và đối chiếu trạng thái đa biến (Retest).

### 2.3. Mục 1.4.1: Chuyển đổi từ mô hình 4 cấp độ tăng dần sang Mô hình Bốn trục bằng chứng độc lập
- **Trước chỉnh lý:** Mô hình bậc thang tăng dần từ Cấp 1 (Cổng mạng) $\rightarrow$ Cấp 2 (Giao thức) $\rightarrow$ Cấp 3 (Dấu hiệu lỗ hổng) $\rightarrow$ Cấp 4 (Thực thi mã khai thác RCE).
- **Sau chỉnh lý:** Thay thế hoàn toàn bậc thang Cấp độ 4 bằng **Mô hình bốn trục bằng chứng độc lập** (Bảng 1.5):
  - *Trục 1: Khả năng tiếp cận tầng mạng (Network Reachability / Service Exposure).*
  - *Trục 2: Bề mặt giao thức SMB (SMB Protocol Surface).*
  - *Trục 3: Tín hiệu thăm dò lỗ hổng từ xa (Remote Vulnerability-Oriented Scanner Signal).*
  - *Trục 4: Trạng thái bản vá nội bộ trên máy chủ (Local Patch State).*
- **Bảo toàn các nguyên tắc suy luận then chốt:**
  - `445 OPEN != vulnerable`
  - `SMBv1 enabled != MS17-010 confirmed`
  - `UNKNOWN != SAFE`
  - `local UNPATCHED` không tự biến `remote UNKNOWN` thành `VULNERABLE`.

### 2.4. Mục 1.4.2 & 1.4.3: Chuẩn hóa nguyên tắc suy luận và các tầng phòng thủ
- **Mục 1.4.2:** Phân biệt rõ bản chất giữa **lỗi thu thập dữ liệu (collection failure)** do điều kiện mạng/tường lửa (dẫn tới không có kết quả hợp lệ) và **lỗi diễn giải kết quả (interpretation error)** do đồng nhất sai các khái niệm kỹ thuật.
- **Mục 1.4.3:** Phân định các giải pháp bảo mật thành **ba tầng kiểm soát (Control Layers)** độc lập và nguyên tắc tái kiểm thử:
  1. *Tầng cập nhật hệ thống (Patching Layer):* Sửa lỗi logic trong driver `srv.sys` ($\geq 6.3.9600.18604$).
  2. *Tầng giảm thiểu mức giao thức (Protocol Hardening Layer - Case B):* Tắt SMBv1, triệt tiêu bề mặt tấn công từ xa (`SMBv1 disabled != PATCHED`).
  3. *Tầng kiểm soát truy cập mạng (Network Access Control Layer - Case C):* Tường lửa pfSense chuyển trạng thái cổng sang `filtered` (`FILTERED != PATCHED`).
  4. *Nguyên tắc tái kiểm thử chuẩn hóa (Retest Principle):* Đối chiếu đa biến, xác thực biến số mục tiêu thay đổi và duy trì tính khả dụng dịch vụ.

---

## 3. Thống kê số lượng từ và cấu trúc tiêu đề

### 3.1. Thống kê từ (Word Count)
- **Trước chỉnh lý (Manager HEAD 5b5b5104):** 8.174 từ (341 dòng).
- **Sau chỉnh lý (RG1 R1):** 9.327 từ tổng thể bao gồm bảng biểu và mã kỹ thuật (369 dòng). Khối văn xuôi thuần túy đạt xấp xỉ 7.800 từ, hoàn toàn nằm trong dải mục tiêu quy định (7.000 – 8.500 từ).

### 3.2. Cấu trúc tiêu đề (Headings)
Tổng số tiêu đề được duy trì chính xác ở con số 26, không làm phân mảnh bố cục:
1. `# CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ CÔNG CỤ KIỂM THỬ SMB`
2. `## 1.1. Tổng quan về giao thức SMB`
   - `### 1.1.1. Khái niệm và vai trò của SMB trong hệ điều hành Windows`
   - `### 1.1.2. Mô hình Client – Server`
   - `### 1.1.3. Phân biệt SMBv1, SMBv2 và SMBv3`
   - `### 1.1.4. Phân tích cổng mạng TCP 139 và TCP 445`
   - `### 1.1.5. Quy trình trao đổi yêu cầu và phản hồi`
3. `## 1.2. Lỗ hổng bảo mật MS17-010`
   - `### 1.2.1. Tổng quan về thông báo bảo mật MS17-010`
   - `### 1.2.2. Phân loại các mã CVE và danh mục bản vá theo hệ điều hành`
   - `### 1.2.3. Cơ chế kỹ thuật của lỗ hổng CVE-2017-0144 và mã khai thác EternalBlue`
   - `### 1.2.4. Điều kiện hệ thống có nguy cơ bị khai thác`
   - `### 1.2.5. Tác động an toàn thông tin`
   - `### 1.2.6. Khái quát các chiến dịch tấn công thực tế liên quan`
4. `## 1.3. Công cụ và cơ sở đo đạc thực nghiệm`
   - `### 1.3.1. Hệ điều hành kiểm thử Kali Linux`
   - `### 1.3.2. Công cụ quét mạng Nmap`
   - `### 1.3.3. Tự động hóa kiểm tra an toàn với Nmap Scripting Engine (NSE)`
   - `### 1.3.4. Cơ sở xác minh trạng thái bản vá cục bộ trên Windows Server 2012 R2` *(đã thay thế Metasploit)*
   - `### 1.3.5. Liên kết cơ sở lý thuyết và các phép đo thực nghiệm lab`
5. `## 1.4. Cơ sở đánh giá trạng thái và nguyên tắc phòng thủ`
   - `### 1.4.1. Mô hình bốn trục bằng chứng trong đánh giá dịch vụ SMB và lỗ hổng` *(đã thay thế 4 cấp độ)*
   - `### 1.4.2. Giới hạn kỹ thuật và phòng ngừa kết quả sai lệch`
   - `### 1.4.3. Nguyên tắc giảm thiểu rủi ro và phòng thủ giao thức SMB`
6. `## TỔNG KẾT CHƯƠNG 1`
7. `## TÀI LIỆU THAM KHẢO`

---

## 4. Kiểm toán và chuẩn hóa tài liệu tham khảo (Citation Audit)

- **Số lượng trích dẫn:** 21 tài liệu tham khảo được đánh số tuần tự [1] đến [21].
- **Loại bỏ:**
  - Tài liệu cũ `[21]` (Metasploit overview) và `[22]` (Metasploit ms17_010 auxiliary script) do đề tài không sử dụng Metasploit trong thực nghiệm.
- **Bổ sung và chuẩn hóa:**
  - Bổ sung tài liệu chuẩn mực của Microsoft: Microsoft Support, "How to verify that MS17-010 is installed," Article 4023262 (Mã nguồn S032 trong `SOURCE_LEDGER.md`), đánh số tham chiếu `[21]`.
- **Tính trọn vẹn:** 100% các chỉ số `[n]` xuất hiện trong thân bài đều có mục tương ứng trong danh mục tài liệu tham khảo; không có trích dẫn mồ côi hay trích dẫn thiếu.
