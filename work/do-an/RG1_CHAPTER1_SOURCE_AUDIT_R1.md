# KIỂM TOÁN NGUỒN HỌC THUẬT VÀ DỮ LIỆU KỸ THUẬT CHƯƠNG 1 (RG1_CHAPTER1_SOURCE_AUDIT_R1)
## BẢN TÁI THIẾT LẬP TOÀN DIỆN TỪ SOURCE_LEDGER.MD CHÍNH THỨC (R2)

- **Giai đoạn thực hiện:** RG1 R2 — Hiệu chỉnh giới hạn kỹ thuật và chuẩn hóa nguồn học thuật sau Independent External Review R1.
- **Tệp được kiểm toán:** `work/do-an/CHAPTER_1.md`
- **Tệp căn cứ thẩm quyền:** `work/do-an/SOURCE_LEDGER.md`
- **Nhánh:** `feature/rg1-ch1-argument-realignment`
- **Thời gian lập:** 06/10/2026

---

## 1. Bảng đối chiếu 1:1 giữa danh mục trích dẫn Chương 1 và SOURCE_LEDGER.md

Toàn bộ 21 mục tài liệu tham khảo trong Chương 1 được đối chiếu trực tiếp với các dòng nguồn đã được thẩm định trong `SOURCE_LEDGER.md`. Tuyệt đối không suy diễn mã nguồn từ số thứ tự trích dẫn, không sử dụng nguồn ở trạng thái `RECHECK` làm nguồn chứng minh, và không đưa vào các nguồn giả định không có trong sổ nguồn.

| Số trích dẫn [n] | Mã nguồn Ledger | Trạng thái Ledger | Tác giả / Cơ quan xuất bản | Năm | Tiêu đề tài liệu theo `SOURCE_LEDGER.md` | Vai trò bảo chứng kỹ thuật trong Chương 1 |
| :---: | :---: | :---: | :--- | :---: | :--- | :--- |
| **[1]** | **S020** | `VERIFIED` | Microsoft Learn | 2025 | What is Microsoft SMB Protocol and CIFS Protocol? | Khái niệm giao thức SMB/CIFS, phạm vi chức năng chia sẻ tệp và xác thực |
| **[2]** | **S002** | `VERIFIED` | Microsoft Learn | 2026 | Direct hosting of SMB over TCP/IP | Cơ chế đóng gói NetBIOS over TCP (139) và Direct hosting SMB qua cổng TCP 445 |
| **[3]** | **S006** | `VERIFIED` | Microsoft Learn | 2025 | What is SMB File Sharing for Windows and Windows Server? | Tiến hóa các thế hệ SMBv1, SMBv2, SMBv3 và tính năng gộp lệnh Compounding |
| **[4]** | **S007** | `VERIFIED` | Microsoft Learn | 2025 | SMB security enhancements | Cơ chế mã hóa SMB Encryption và giới hạn bảo vệ trước việc hạ cấp giao thức |
| **[5]** | **S023** | `VERIFIED` | Microsoft Learn | 2024 | What is Server Message Block signing? | Cơ chế ký số SMB Signing, thuật toán MD5/HMAC-SHA256/AES-CMAC và tính toàn vẹn |
| **[6]** | **S031** | `VERIFIED` | Microsoft | n.d. | SMB 3.1.1 Pre-authentication integrity in Windows 10 | Cơ chế kiểm tra tính toàn vẹn trước xác thực SHA-512 trong SMB 3.1.1 |
| **[7]** | **S005** | `VERIFIED` | Microsoft | 2017 | Microsoft Security Bulletin MS17-010 – Critical | Thông báo bảo mật chính thức MS17-010, phạm vi ảnh hưởng và phân loại Critical |
| **[8]** | **S008** | `VERIFIED` | Microsoft Learn | 2025 | Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows | Hướng dẫn cấu hình vô hiệu hóa SMBv1 máy chủ qua lệnh PowerShell `Set-SmbServerConfiguration` |
| **[9]** | **S022** | `VERIFIED` | Microsoft Open Specifications | 2026 | [MS-SMB2]: Server Message Block (SMB) Protocol Versions 2 and 3 | Đặc tả kỹ thuật giao thức SMBv2/v3, cấu trúc đàm phán phương ngữ và mã trạng thái |
| **[10]** | **S028** | `VERIFIED` | Microsoft | n.d. | MS-CIFS: Per SMB Session; Receiving a Tree Connect Response | Đặc tả phiên làm việc CIFS/SMBv1, định danh UID, TID và tài nguyên chia sẻ ngầm `IPC$` |
| **[11]** | **S010** | `VERIFIED` | Microsoft Security Response Center (MSRC) | 2017 | Eternal Synergy Exploit Analysis | Phân tích kỹ thuật của Microsoft về cơ chế khai thác giao thức và các biến thể lỗ hổng |
| **[12]** | **S011** | `VERIFIED` | NIST | 2017 | CVE-2017-0144 Detail | Bản ghi lỗ hổng bảo mật CVE-2017-0144 trên cơ sở dữ liệu quốc gia NVD |
| **[13]** | **S012** | `VERIFIED` | Microsoft Threat Intelligence | 2017 | New ransomware, old techniques: Petya adds-worm capabilities | Phân tích cơ chế phát tán qua giao thức SMB và phá hủy cấu trúc MBR của mã độc NotPetya |
| **[14]** | **S013** | `VERIFIED` | Rapid7 | 2017 | MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption | Phân tích kỹ thuật lỗi ép kiểu FEA (DWORD vs WORD) trong `srv.sys` và Pool Grooming |
| **[15]** | **S025** | `VERIFIED` | K. Scarfone and P. Hoffman, NIST | 2009 | SP 800-41 Rev. 1: Guidelines on Firewalls and Firewall Policy | Hướng dẫn chuẩn mực về chính sách tường lửa, kiểm soát cổng và phân đoạn mạng |
| **[16]** | **S015** | `VERIFIED` | Microsoft Threat Intelligence | 2017 | WannaCrypt ransomware worm targets out-of-date systems | Báo cáo của Microsoft về cơ chế lây lan mã độc WannaCry qua SMB trên máy chưa vá |
| **[17]** | **S026** | `VERIFIED` | Kali Linux Project | n.d. | What is Kali Linux? | Tài liệu giới thiệu hệ điều hành kiểm thử chuyên dụng Kali Linux làm trạm đo đạc |
| **[18]** | **S017** | `VERIFIED` | Gordon Lyon | 2009 | Nmap Network Scanning: The Official Nmap Project Guide | Cơ sở lý thuyết quét cổng TCP SYN (`-sS`), nhận diện dịch vụ (`-sV`) và kiến trúc NSE |
| **[19]** | **S018** | `VERIFIED` | Paulino Calderon & Nmap Project | 2017 | smb-vuln-ms17-010.nse Script Source Code | Mã nguồn kịch bản NSE: opcode `0x25`, `PeekNamedPipe` `0x2300`, mã phản hồi NT Status |
| **[20]** | **S029** | `VERIFIED` | Paulino Calderon / Nmap Project | n.d. | smb-protocols.nse Script Source Code | Mã nguồn kịch bản NSE khảo sát danh mục phương ngữ SMB được máy chủ hỗ trợ |
| **[21]** | **S032** | `VERIFIED` | Microsoft Support | 2017 | How to verify that MS17-010 is installed | Hướng dẫn kỹ thuật kiểm tra bản vá MS17-010: KB và phiên bản `srv.sys` tối thiểu |

*Xác nhận kiểm toán:* 100% (21/21) tài liệu tham khảo trong Chương 1 đều có mã định danh đối ứng tồn tại trong `SOURCE_LEDGER.md` và đều ở trạng thái **`VERIFIED`**. Tuyệt đối không sử dụng bất kỳ nguồn nào trong nhóm `RECHECK` (như S001, S003, S004, S009, S014, S016, S019) để bảo chứng cho các luận điểm trong chương.

---

## 2. Xác nhận nguồn và thuật ngữ xác minh bản vá trên Windows Server 2012 R2

Căn cứ tài liệu kỹ thuật chính thức của Microsoft (**Microsoft Support Article 4023262: "How to verify that MS17-010 is installed"** — Mã Ledger: **S032** [21]):

1. **Chuẩn hóa thuật ngữ khoa học:**
   - Tuyệt đối không sử dụng các cụm từ suy diễn quá mức như "ngưỡng an toàn" hay "chứng chỉ an toàn toàn diện".
   - Thuật ngữ chuẩn xác được xác lập: **"Phiên bản tệp `srv.sys` tối thiểu đã cập nhật đối với MS17-010"** (tiếng Anh: *Minimum updated srv.sys version for MS17-010*).
2. **Giá trị kỹ thuật đối chiếu cho Windows Server 2012 R2:**
   - Gói cập nhật tương ứng: **KB4012213** (Security Only) hoặc **KB4012216** (Monthly Rollup) [7], [21].
   - Tệp driver nhân chịu trách nhiệm: `C:\Windows\System32\drivers\srv.sys`.
   - Giá trị phiên bản số nguyên tối thiểu đã cập nhật:
     $$\mathbf{srv.sys \geq 6.3.9600.18604}$$
3. **Ranh giới phân loại kỹ thuật:**
   - Máy chủ có tệp `srv.sys` đạt từ `6.3.9600.18604` trở lên được phân loại là **đã cập nhật đối với MS17-010**.
   - Máy chủ có phiên bản thấp hơn giá trị trên (ví dụ phiên bản gốc RTM `6.3.9600.16384`) được phân loại là **chưa cập nhật bản vá (`UNPATCHED`) đối với MS17-010**.
   - Tiêu chí này giới hạn trong phạm vi các lỗ hổng được xử lý trong bản tin MS17-010, không suy diễn thành sự an toàn tuyệt đối của toàn bộ hệ điều hành trước mọi nguy cơ khác.

---

## 3. Xác nhận cơ chế mã nguồn và ranh giới suy luận của kịch bản Nmap NSE

Căn cứ mã nguồn chính thức của kịch bản `smb-vuln-ms17-010.nse` (Mã Ledger: **S018** [19]):

1. **Ý nghĩa kỹ thuật của các mã phản hồi NT Status:**
   - Mã `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`): Được mã nguồn kịch bản sử dụng làm tín hiệu đặc trưng của nhánh xử lý trên hệ thống chưa cập nhật bản vá $\rightarrow$ kịch bản xuất `State: VULNERABLE`.
   - Mã `STATUS_ACCESS_DENIED` (`0xC0000022`) và `STATUS_INVALID_HANDLE` (`0xC0000008`): Được mã nguồn ghi nhận là có khả năng đã được vá (`likely patched`) $\rightarrow$ kịch bản xuất chuỗi thông báo `This system is patched.`.
   - *Ranh giới giải thích:* Không tự ý suy diễn các giả định nguyên nhân nội bộ như "driver đã được bổ sung cơ chế kiểm soát tham số", mà chỉ mô tả chính xác ánh xạ mã lỗi theo đúng mã nguồn kịch bản.
2. **Phạm vi nhận diện và mã CVE:**
   - Kịch bản `smb-vuln-ms17-010.nse` là công cụ nhận diện từ xa đối với bản tin MS17-010 nói chung; trong siêu dữ liệu kết quả xuất, kịch bản gắn định danh tham chiếu với mã CVE-2017-0143.
   - Kết quả kịch bản phản ánh tín hiệu phát hiện từ xa, không tự cấu thành bằng chứng chứng minh trực tiếp khả năng khai thác thành công lỗ hổng CVE-2017-0144 hay mã khai thác EternalBlue trên máy chủ mục tiêu.
3. **Ranh giới trạng thái không xác định (`UNKNOWN / NO USABLE SCRIPT RESULT`):**
   - Về mặt lý thuyết: Tiến trình quét có thể không thu được phản hồi thăm dò tại các giai đoạn kết nối khác nhau (kết nối mạng, phiên `IPC$`, hoặc nhận gói tin). Khi không có phản hồi hợp lệ cho lệnh `PeekNamedPipe`, kịch bản kết thúc mà không xuất khối kết luận lỗ hổng.
   - Về mặt thực nghiệm đồ án: Đề tài ghi nhận nguyên trạng kết quả của kịch bản là không có kết luận khả dụng mà không tự ý gán cho một nguyên nhân giả định cụ thể nào.
   - Nguyên tắc bất biến: **`UNKNOWN != SAFE`**.

---

## 4. Xác nhận hướng dẫn vô hiệu hóa giao thức SMBv1

Căn cứ tài liệu hỗ trợ kỹ thuật của Microsoft (**Microsoft Learn: "Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows"** — Mã Ledger: **S008** [8]):

1. **Phương pháp cấu hình trên Windows Server 2012 R2:**
   - Thực thi qua câu lệnh PowerShell quản trị:
     ```powershell
     Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
     ```
2. **Phân biệt ranh giới kỹ thuật giữa cấu hình và tính năng:**
   - Việc tắt cấu hình giao thức trên máy chủ (`EnableSMB1Protocol = $false`) có bản chất kỹ thuật hoàn toàn khác với việc gỡ bỏ gói tính năng Windows (`FS-SMB1 uninstalled`).
   - Đề tài bảo toàn nghiêm ngặt hai ranh giới:
     - **`SMBv1 disabled != FS-SMB1 uninstalled`**
     - **`SMBv1 disabled != PATCHED`** (tắt cấu hình giao thức máy chủ loại bỏ phương ngữ `NT LM 0.12` khỏi danh sách đàm phán từ xa, nhưng không làm thay đổi hay nâng cấp phiên bản tệp nhị phân `srv.sys` trên đĩa cứng).
3. **Loại bỏ ngôn ngữ tuyệt đối hóa:**
   - Không sử dụng các từ ngữ mang tính tuyệt đối hóa như "triệt tiêu hoàn toàn", "đóng kín hoàn toàn bề mặt", "mọi gói tin bị chặn".
   - Mô tả chính xác: Biện pháp cấu hình này làm giảm bề mặt tiếp xúc của giao thức và loại bỏ phương ngữ SMBv1 khỏi danh sách đàm phán trong các phép đo đạc lại.

---

## 5. Rà soát các chiến dịch mã độc WannaCry và NotPetya

Căn cứ các báo cáo phân tích mối đe dọa chính thức của Microsoft Threat Intelligence:
1. **Mã độc WannaCry (Mã Ledger: S015 [16]):**
   - Dẫn chứng theo báo cáo *Microsoft Threat Intelligence (2017)*: Mã độc tự động quét cổng TCP 445 và phát tán dạng sâu (worm) qua các máy tính Windows chưa cập nhật bản vá MS17-010.
   - Không sử dụng nguồn CISA TA17-132A (do mã S014 đang ở trạng thái `RECHECK`).
2. **Mã độc NotPetya (Mã Ledger: S012 [13]):**
   - Dẫn chứng theo báo cáo *Microsoft Threat Intelligence (2017)*: Mã độc kết hợp cơ chế lây lan qua giao thức SMB với hành vi phá hoại cấu trúc bản ghi khởi động (MBR) trên các hệ thống chưa được vá lỗi.
   - Loại bỏ các số liệu thiệt hại định lượng quy đổi tiền tệ không có trong nguồn tài liệu được kiểm chứng.
