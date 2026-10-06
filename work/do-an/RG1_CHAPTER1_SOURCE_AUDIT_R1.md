# KIỂM TOÁN NGUỒN HỌC THUẬT VÀ DỮ LIỆU KỸ THUẬT CHƯƠNG 1 (RG1_CHAPTER1_SOURCE_AUDIT_R1)

- **Giai đoạn thực hiện:** RG1 — Chỉnh lý toàn diện Chương 1 theo lập luận thực nghiệm chuẩn mực.
- **Tệp được kiểm toán:** `work/do-an/CHAPTER_1.md`
- **Nhánh:** `feature/rg1-ch1-argument-realignment`
- **Thời gian lập:** 06/10/2026

---

## 1. Bản đồ đối chiếu nguồn học thuật theo từng mục kỹ thuật

Toàn bộ các luận điểm, tham số kỹ thuật và cơ chế giao thức trong Chương 1 được bảo đảm đối chiếu 1:1 với các nguồn tài liệu sơ cấp và thứ cấp đã được kiểm chứng trong `SOURCE_LEDGER.md`.

| Mục trong Chương 1 | Nội dung kỹ thuật chính | Nguồn sơ cấp / Chuẩn quốc tế | Mã Ledger trong `SOURCE_LEDGER.md` | Chỉ số trích dẫn trong Chương 1 |
| :--- | :--- | :--- | :--- | :--- |
| **1.1.1 – 1.1.2** | Tổng quan kiến trúc SMB, mô hình Client-Server | Microsoft Official Learn, MS-SMB Specification | S020, S002 | [1], [2] |
| **1.1.3** | Tiến hóa SMBv1, SMBv2, SMBv3, mã định danh phương ngữ | Microsoft MS-SMB, MS-SMB2 Specifications | S002, S006 | [2], [3] |
| **1.1.4** | Cơ chế đóng gói NetBIOS over TCP port 139 và Direct-hosted SMB port 445 | IETF RFC 1001, RFC 1002 | S005 | [4] |
| **1.1.5** | Quy trình bắt tay SMB, NegProt, SessionSetup, TreeConnect, IPC$, Signing | Microsoft MS-SMB, MS-SMB2, SMB Security Enhancements | S002, S006, S028 | [2], [3], [5] |
| **1.2.1** | Thông báo bảo mật MS17-010, phân loại mức độ nghiêm trọng Critical | Microsoft Security Bulletin MS17-010 | S007 | [6] |
| **1.2.2** | 6 mã CVE (CVE-2017-0143 đến CVE-2017-0148) và danh mục bản vá cho các dòng Windows | Microsoft MS17-010, NIST NVD (CVE-2017-0143..0148), KB4012213, KB4012216 | S001, S007, S010, S011, S012, S013, S022, S023 | [6], [7], [8], [9], [10], [11], [12], [13] |
| **1.2.3** | Cơ chế kỹ thuật CVE-2017-0144, tràn bộ nhớ FEA (DWORD vs WORD), driver `srv.sys`, Pool Grooming | Rapid7 Technical Analysis (EternalBlue), NIST CVE-2017-0144 | S001, S025 | [7], [14] |
| **1.2.4** | Điều kiện hệ thống dễ bị tổn thương, lý do chọn Windows Server 2012 R2 | Microsoft MS17-010, Microsoft Support Article 4023262 | S007, S032 | [6], [21] |
| **1.2.5** | Đánh giá tác động an ninh C-I-A, nguy cơ sập nhân (BSOD) | Rapid7 Technical Analysis | S025 | [14] |
| **1.2.6** | Các chiến dịch tấn công thực tế (WannaCry, NotPetya) | CISA Technical Alerts TA17-132A, TA17-181A | S014, S031 | [15], [16] |
| **1.3.1** | Hệ điều hành trạm kiểm thử độc lập Kali Linux | Kali Linux Official Documentation | S017 | [17] |
| **1.3.2** | Cơ chế quét cổng Nmap SYN (`-sS`) và nhận diện dịch vụ (`-sV`) | Nmap Official Network Scanning Guide (Gordon Lyon) | S018 | [18] |
| **1.3.3** | Nền tảng Nmap Scripting Engine, logic `smb-vuln-ms17-010`, `smb-protocols`, `smb2-security-mode` | Nmap Official NSE Documentation & Script Sources | S018, S019, S026, S029 | [18], [19], [20] |
| **1.3.4** | Cơ sở xác minh bản vá nội bộ Windows Server 2012 R2, Hotfix KB4012213/KB4012216, tệp `srv.sys` | Microsoft Support Article 4023262, KB4012213, KB4012216 | S022, S023, S032 | [8], [9], [21] |
| **1.3.5** | Liên kết lý thuyết với 8 phép đo thực nghiệm lab | Tổng hợp các nguồn chuẩn sơ cấp Nmap, Microsoft, pfSense | S007, S008, S015, S018, S019, S032 | [6], [18], [19], [21], v.v. |
| **1.4.1** | Mô hình bốn trục bằng chứng độc lập | Cơ sở phương pháp luận đối chiếu chéo | S018, S019, S032 | [18], [19], [21] |
| **1.4.2** | Giới hạn kỹ thuật, phân biệt lỗi thu thập vs lỗi diễn giải, ranh giới `UNKNOWN != SAFE` | Nmap NSE Reference Guide, Microsoft Support | S018, S019, S032 | [18], [19], [21] |
| **1.4.3** | Ba tầng kiểm soát phòng thủ (Patching, Protocol Hardening, Network Access Control) | Microsoft Support (KB2696547), pfSense Documentation, Microsoft MS17-010 | S007, S008, S015, S032 | [6], [21], v.v. |

---

## 2. Xác nhận ngưỡng bản vá kỹ thuật trên Windows Server 2012 R2

Căn cứ tài liệu hỗ trợ kỹ thuật chính thức của Microsoft (**Microsoft Support Article 4023262: "How to verify that MS17-010 is installed"** [21]):

1. **Gói cập nhật tương ứng cho Windows Server 2012 R2:**
   - Bản cập nhật an ninh hàng tháng (Monthly Rollup): **KB4012216** [9].
   - Bản cập nhật an ninh độc lập (Security Only): **KB4012213** [8].
2. **Tệp driver nhân đích và 4 trường thuộc tính nhị phân:**
   - Tệp chịu trách nhiệm: `C:\Windows\System32\drivers\srv.sys`.
   - Bốn trường thuộc tính cần trích xuất: `FileVersion`, `ProductVersion`, `Length` (kích thước tệp byte), `LastWriteTime` (thời điểm ghi tệp).
3. **Ngưỡng phiên bản an toàn tối thiểu (Version Threshold):**
   - Microsoft công bố rõ ràng trong Article 4023262: Đối với Windows Server 2012 R2 (nhánh LDR/GDR), phiên bản tệp `srv.sys` sau khi cài đặt gói cập nhật tháng 03/2017 phải đạt giá trị tối thiểu là:
     $$\text{Ngưỡng an toàn } srv.sys \geq \mathbf{6.3.9600.18604}$$
   - Bất kỳ giá trị nào nhỏ hơn `6.3.9600.18604` (chẳng hạn phiên bản gốc RTM `6.3.9600.16384`) đều xác nhận máy chủ chưa được cập nhật bản vá khắc phục lỗi logic trong xử lý danh sách FEA.

---

## 3. Xác nhận ranh giới diễn giải kịch bản Nmap NSE

Căn cứ tài liệu đặc tả mã nguồn Nmap và kịch bản `smb-vuln-ms17-010.nse` [19]:

1. **Cơ chế thăm dò:**
   - Kịch bản thực hiện thăm dò an toàn bằng cách gửi lệnh `PeekNamedPipe` (mã hàm `0x2300`) trên đường ống `\PIPE\` thông qua kết nối chia sẻ ngầm `IPC$`.
2. **Ranh giới trạng thái mã trạng thái phản hồi:**
   - `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`): Máy chủ phản hồi mã lỗi tài nguyên đặc thù của driver chưa vá $\rightarrow$ Kịch bản xuất `State: VULNERABLE`.
   - `STATUS_ACCESS_DENIED` (`0xC0000022`) hoặc `STATUS_INVALID_HANDLE` (`0xC0000008`): Máy chủ đã áp dụng kiểm soát tham số $\rightarrow$ Kịch bản xuất `This system is patched`.
3. **Ranh giới trạng thái không xác định (`UNKNOWN / NO USABLE SCRIPT RESULT`):**
   - Khi kịch bản không thể kết nối tới cổng SMB, cổng bị lọc (`filtered`), kết nối mạng bị ngắt (timeout) hoặc phiên xác thực nặc danh tới `IPC$` bị từ chối, kịch bản kết thúc mà không thể gửi hoặc không nhận được gói tin phản hồi của phép thăm dò `PeekNamedPipe`.
   - Nmap không in ra khối kết luận trạng thái lỗ hổng.
   - **Ranh giới phương pháp luận bắt buộc:** Đề tài xác lập nguyên tắc **`UNKNOWN != SAFE`**. Việc không quan sát được phản hồi từ xa không đồng nghĩa với việc máy chủ an toàn; đây là giới hạn của góc nhìn mạng từ trạm kiểm thử.

---

## 4. Xác nhận hướng dẫn vô hiệu hóa giao thức SMBv1

Căn cứ tài liệu kỹ thuật của Microsoft (**Microsoft Support KB2696547: "How to detect, enable and disable SMBv1, SMBv2, and SMBv3 in Windows"** [10]):

1. **Phương pháp thực thi trên Windows Server 2012 R2:**
   - Sử dụng PowerShell cmdlet chính thức:
     ```powershell
     Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
     ```
   - Câu lệnh này cập nhật cấu hình dịch vụ máy chủ SMB nội bộ để từ chối khởi tạo giao thức SMBv1.
2. **Tác động kỹ thuật đối với bề mặt mạng:**
   - Máy chủ ngừng thương lượng phương ngữ `NT LM 0.12`. Khi trạm kiểm thử gửi yêu cầu Negotiate Protocol chứa SMBv1, máy chủ chỉ chấp thuận nếu trạm kiểm thử hỗ trợ SMBv2/SMBv3; nếu chỉ yêu cầu SMBv1, kết nối sẽ bị hủy bỏ ngay lập tức.
3. **Ranh giới phòng thủ (Defense Boundary):**
   - Việc tắt SMBv1 triệt tiêu đường truyền khai thác từ xa nhưng **không làm thay đổi cấu trúc mã nhị phân hay nâng cấp phiên bản của tệp `srv.sys` trên ổ đĩa** (`SMBv1 disabled != PATCHED`).

---

## 5. Rà soát các khẳng định bị loại bỏ do không đủ căn cứ nguồn

Trong quá trình chỉnh lý RG1, một số nội dung trong bản thảo cũ đã được rà soát và loại bỏ triệt để nhằm bảo đảm tính trung thực học thuật tuyệt đối:

1. **Loại bỏ việc gọi Windows 7 là đối tượng thực nghiệm:** Bản thảo cũ đề cập Windows 7 SP1 là mục tiêu lab; điều này mâu thuẫn với cấu trúc thực nghiệm thực tế sử dụng máy chủ doanh nghiệp Windows Server 2012 R2. Nội dung này đã bị loại bỏ hoàn toàn khỏi các phần mô tả thực nghiệm.
2. **Loại bỏ công cụ Metasploit Framework:** Bản thảo cũ dành một tiểu mục lớn giới thiệu Metasploit và các module khai thác/quét. Do đề tài hiện tại áp dụng phương pháp luận đo đạc phản ứng an toàn qua Nmap/NSE và xác minh bản vá nội bộ qua PowerShell, Metasploit không tham gia vào mô hình thực nghiệm và đã được loại bỏ 100%.
3. **Loại bỏ khẳng định về việc thực nghiệm khai thác RCE / phiên SYSTEM:** Đề tài không thực hiện hành vi khai thác xâm nhập tạo phiên tải trọng trong lab. Khái niệm RCE và quyền `SYSTEM` chỉ được giữ lại trong phần phân tích lý thuyết về mức độ nguy hiểm của CVE-2017-0144 theo tài liệu của Rapid7.
4. **Loại bỏ mô hình ba VLAN và Client nghiệp vụ:** Bản thảo cũ đề cập đến các phân vùng mạng nghiệp vụ và Client nghiệp vụ không tồn tại trong thiết kế mạng thực nghiệm thực tế. Nội dung này đã được thay thế bằng mô tả khách quan về cơ chế lọc gói của tường lửa trung gian Transparent Bridge (Case C).
