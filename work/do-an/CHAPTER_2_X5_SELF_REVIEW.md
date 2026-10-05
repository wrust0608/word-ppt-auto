# BÁO CÁO TỰ ĐÁNH GIÁ VIẾT LẠI CẤU TRÚC CHƯƠNG 2 (X5 R5 SELF-REVIEW)

**Thời điểm thực hiện:** 2026-10-05
**Vai trò thực hiện:** Executor / Writing Agent
**Tài liệu đánh giá:** `work/do-an/CHAPTER_2.md`
**Nhánh làm việc:** `feature/x5-chapter-2-structural-revision`
**Căn cứ đánh giá:** `X5_STRUCTURAL_REWRITE_EXTERNAL_REVIEW_R4.md`, `PROJECT_STATE.md` (DEC-32, DEC-33), `SOURCE_LEDGER.md`
**Trạng thái đề xuất:** `X5_STRUCTURAL_REWRITE_R5_READY_FOR_FINAL_EXTERNAL_REVIEW`

---

## 1. Kiểm tra cấu trúc và tính duy nhất của từng phần (Structure & Role Uniqueness)

### 1.1. Tuân thủ đề cương đã khóa (Canonical Outline Match)
Bản thảo Chương 2 tuân thủ tuyệt đối cấu trúc được Người dùng phê duyệt tại Change Request CR-2026-10-05-X5 và DEC-30:
- **Tiêu đề chương:** `# CHƯƠNG 2. THIẾT KẾ MÔ HÌNH VÀ PHƯƠNG PHÁP THỰC NGHIỆM`
- **Số lượng phân mục:** Đạt chính xác **8/8 H2** và **27/27 H3**.
- **Thứ tự và định danh:** 100% heading giữ nguyên văn bản canonical, không thêm heading mới, không bớt heading, không đổi tên, không đảo thứ tự.
- **Không hồi quy cấu trúc cũ:** Loại bỏ hoàn toàn mô hình phân mảnh cũ.
- **Ngân sách hình và bảng:** Giữ nguyên 4 vị trí chờ hình vẽ và 5 bảng biểu chuẩn tắc.

### 1.2. Tính duy nhất vai trò của từng phân mục (Role Uniqueness Audit)
Mỗi cụm phân mục trong Chương 2 thực hiện đúng một chức năng duy nhất, loại bỏ hiện tượng chồng lấn:
- **Mục 2.1 (Thiết kế nghiên cứu và phạm vi thực nghiệm):** Giải trình lý do thiết kế phương pháp, phạm vi an toàn phi phá hủy theo NIST SP 800-115 [1], nguyên tắc cô lập L2/L3 và kiểm soát biến thông qua snapshot. Không mô tả tham số chi tiết của máy ảo (để dành cho 2.2).
- **Mục 2.2 (Kiến trúc và trạng thái ban đầu của môi trường lab):** Xác lập chính xác các thành phần môi trường xuất phát (VirtualBox, Kali, Windows Server 2012 R2, cấu hình LanmanServer, trạng thái driver `srv.sys` unpatched). Không bàn luận về kịch bản quét.
- **Mục 2.3 (Phương pháp thu thập và diễn giải bằng chứng):** Định nghĩa mô hình 5 lớp quan sát, cơ chế lưu trữ dữ liệu thô `-oA`, quy tắc xử lý kết quả âm tính/bất định (`UNKNOWN`, `NO OUTPUT`, `FILTERED`) và các ranh giới suy luận an toàn.
- **Mục 2.4 (Thiết kế Kịch bản 1 — Khảo sát dịch vụ SMB):** Thiết kế quy trình 8 bước và các phép đo B2–B6 khảo sát bề mặt dịch vụ SMB phi phá hủy. Không đề cập lỗ hổng MS17-010.
- **Mục 2.5 (Thiết kế Kịch bản 2 — Đánh giá cấu hình SMB và MS17-010):** Thiết kế 4 phép đo tuần tự NSE-SMB-01 đến 04 và cơ chế đối soát 2 trục giữa tín hiệu từ xa và trạng thái bản vá nội bộ.
- **Mục 2.6 (Thiết kế kiểm thử các biện pháp giảm thiểu):** Thiết kế phương pháp kiểm thử vi sai, phân định rõ ràng giữa làm cứng giao thức (Case B), kiểm soát mạng (Case C) và sửa lỗi trong nhân (Case A đối chứng lý thuyết).
- **Mục 2.7 (Khung đánh giá kết quả):** Thiết lập ma trận tiêu chí đánh giá kết quả cho từng lớp quan sát, định hình khung phân tích để Chương 3 sử dụng khi báo cáo số liệu thực tế.
- **Mục 2.8 (Tổng kết chương):** Tóm lược phương pháp luận và dẫn dắt sang Chương 3.

---

## 2. Kiểm toán đóng các yêu cầu sửa đổi nhỏ từ hội đồng (R4 Panel Minor Revision Closure: MR-01 → MR-10)

Vòng R5 hoàn tất việc đóng toàn diện 10 khuyến nghị sửa đổi nhỏ (MR-01 đến MR-10) nêu tại `X5_STRUCTURAL_REWRITE_EXTERNAL_REVIEW_R4.md`:

| Mã | Nội dung yêu cầu từ Hội đồng | Hành động xử lý trong R5 | Vị trí cập nhật trong CHAPTER_2.md | Kết quả kiểm toán |
| :--- | :--- | :--- | :--- | :--- |
| **MR-01** | **Xóa causal wording của NO USABLE RESULT** | Bỏ "nếu kịch bản NSE không nhận đủ phản hồi để phân loại"; thay bằng "nếu script không cung cấp verdict usable, kết quả được phân loại `UNKNOWN / NO USABLE SCRIPT RESULT`", không gán nguyên nhân | Mục 2.5.2 | Đạt chuẩn Negative Result Policy |
| **MR-02** | **Chuẩn hóa thuật ngữ cấu hình SMB Server** | Bỏ "điều chỉnh dịch vụ LanmanServer"; sửa thành "Thao tác chỉ thay đổi cấu hình SMB Server, không gỡ tính năng `FS-SMB1` và không thay đổi driver `srv.sys` (`SMBv1 disabled != PATCHED`)" | Mục 2.6.2 | Khớp lệnh PowerShell |
| **MR-03** | **Sửa lỗi logic 'Tách biệt L3' trong Bảng 2.1** | Hai máy thuộc cùng dải `192.168.56.0/24`. Thay "Tách biệt L3" tại cột Ý nghĩa thiết kế thành "Địa chỉ tĩnh trong cùng mạng lab" | Bảng 2.1 (Mục 2.2.4) | Khớp kiến trúc mạng |
| **MR-04** | **Chuẩn hóa thuật ngữ Reachability** | Bảng 2.2 sửa "Khả năng định tuyến L3" thành "Khả năng hiện diện / tiếp cận trong mạng lab". Mục 2.7.1 phân loại thành "có phản hồi trong phép tiền kiểm hoặc không ghi nhận phản hồi trong phép tiền kiểm" | Bảng 2.2 và Mục 2.7.1 | Bao hàm cả ARP/ICMP |
| **MR-05** | **Chuẩn hóa phản hồi TCP Closed** | Thay `closed (nhận RST-ACK)` thành `closed (nhận phản hồi RST, cổng đóng)` theo đúng ngữ nghĩa Nmap SYN scan | Mục 2.7.1 | Khớp Nmap documentation |
| **MR-06** | **Thu hẹp phạm vi đánh giá signing** | Bỏ "đánh giá khả năng chống tấn công chuyển tiếp"; chuyển thành mục tiêu phương pháp: "nhằm đánh giá chính sách ký số SMB và mức độ bắt buộc ký" | Mục 2.7.2 | Đúng phạm vi Chương 2 |
| **MR-07** | **Loại bỏ result-like wording ở Case B** | Bỏ nhận định "cổng TCP 445 vẫn mở"; thay bằng quan hệ phương pháp: "việc vô hiệu hóa SMBv1 không đồng nghĩa đóng TCP 445; phép retest cần kiểm tra khả năng tiếp cận SMB2/SMB3 sau can thiệp" | Mục 2.7.4 | Ranh giới phương pháp |
| **MR-08** | **Giảm biệt ngữ nội bộ (Repo Jargon)** | Thay `canonical` -> "lượt đo chính thức" / "bộ dữ liệu thực nghiệm hiện hành"; `implementation` -> "thành phần SMB bị ảnh hưởng"; `reason` -> "lý do phân loại"; ổn định dùng "bề mặt dịch vụ" và "bề mặt tấn công" | Mục 2.3.2, 2.4.2, 2.6.2, 2.6.4, 2.7.4, Bảng 2.2, Bảng 2.3 | Văn phong khoa học tự nhiên |
| **MR-09** | **Chuẩn hóa mục tiêu nghiên cứu câu đầu** | Sửa "đánh giá nhận diện MS17-010 từ xa" thành "đánh giá khả năng nhận diện dấu hiệu MS17-010 từ xa" | Mục 2.1.1 | Chính xác và tự nhiên |
| **MR-10** | **Chuẩn hóa phát biểu an toàn (Safety Wording)** | Bỏ claim kết quả tuyệt đối "không gây sập hệ thống"; sửa thành "không thực hiện thao tác có chủ đích gây sập hoặc gián đoạn hệ thống" | Mục 2.1.2 | Cam kết phương pháp |

---

## 3. Kiểm toán rò rỉ kết quả (Result Leakage Audit)

Chương 2 giữ nghiêm ngặt ranh giới: **HOW / WITH WHAT / UNDER WHAT CONDITIONS**, không kể trước kết quả thực nghiệm (**WHAT WAS OBSERVED**):
- **Kịch bản 1:** Trình bày thiết kế lệnh `nmap -sS -sV` và 4 kịch bản NSE an toàn; không công bố danh sách dialect thực tế hay banner chi tiết quan sát được trên cổng 139/445 trong lượt chạy cụ thể (`microsoft-ds` = 0, `netbios-ssn` = 0, `syn-ack` = 0 trong văn phong phương pháp 2.4).
- **Kịch bản 2:** Mô tả cơ chế hoạt động chuẩn của `smb-vuln-ms17-010.nse` (giao dịch SMB trên FID 0 phân tích mã lỗi); không trình bày kết quả quan sát cụ thể hay lỗi chi tiết thu được.
- **Case B:** Trình bày lệnh can thiệp PowerShell `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` và kế hoạch đo lại dialect/NSE-04; không đưa bảng so sánh output trước/sau can thiệp, không khẳng định trạng thái mở cổng thực tế.
- **Case C:** Trình bày cấu hình Transparent Bridge pfSense, cờ `net.link.bridge.pfil_member = 1`, `net.link.bridge.pfil_bridge = 0`, `net.link.bridge.pfil_onlyip = 1` và luật chặn TCP cổng 139/445 có ghi log; không trích xuất log block thực tế của pfSense (gói SYN chỉ thuộc log Chương 3).
- **Đánh giá chung:** Không có hiện tượng rò rỉ kết quả thực nghiệm (No Result Leakage).

---

## 4. Đối soát sự thật kỹ thuật và bằng chứng (Technical Truth & Evidence Audit)

Toàn bộ các khóa sự thật kỹ thuật (Technical Truth Locks) được đối soát khớp 100% với `EXPERIMENTAL_TRUTH_MATRIX.md` và `EVIDENCE_REGISTER.md`:
1. **Môi trường ảo hóa:** Oracle VM VirtualBox 7.2.20 r170876; mạng Host-Only `192.168.56.0/24`; 1 NIC/VM ở baseline; không DHCP, không Default Gateway, không NAT, không Bridged.
2. **Máy kiểm thử:** Kali Linux 64-bit nhân Kernel 6.12.33-amd64; IP tĩnh `192.168.56.10/24`; không có default route Internet ở trạng thái baseline pre-demo; Nmap 7.99.
3. **Máy mục tiêu:** Windows Server 2012 R2 Standard Evaluation 64-bit Build 9600 (RTM); IP tĩnh `192.168.56.20/24`.
4. **Dịch vụ mạng:** LanmanServer ở chế độ `Automatic` và đang `Running`; cổng TCP 139 và 445 đang lắng nghe.
5. **Cấu hình SMB nội bộ:** `EnableSMB1Protocol = True`, `EnableSMB2Protocol = True`, tính năng `FS-SMB1` đang cài đặt.
6. **Tường lửa Windows:** Chỉ cho phép TCP 139 và 445 từ IP máy kiểm thử `192.168.56.10/24`; nhóm "File and Printer Sharing" không mở toàn bộ.
7. **Trạng thái bản vá nội bộ:** Trạng thái `UNPATCHED`; `Get-HotFix` không có KB4012213/KB4012216 hay bản cập nhật thay thế tương ứng; driver `srv.sys` có phiên bản số `6.3.9600.16421` thấp hơn ngưỡng an toàn `6.3.9600.18604`.
8. **Điểm phục hồi:** Snapshot `Before Demo` có trên cả hai máy ảo, phục vụ hoàn nguyên trong quy trình kiểm thử vi sai.
9. **Kịch bản NSE an toàn:** Đúng 4 kịch bản canonical (`smb-protocols`, `smb-os-discovery`, `smb2-security-mode`, `smb2-capabilities`); tuyệt đối không dùng wildcard (`smb-vuln*`).
10. **Phán quyết từ xa NSE-SMB-04:** Khóa cứng định dạng `UNKNOWN / NO USABLE SCRIPT RESULT`.
11. **Case B:** Can thiệp `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` là làm cứng giao thức (Protocol Hardening) mức cấu hình dịch vụ; không phải bản vá, không gỡ tính năng, không thay đổi driver nhị phân.
12. **Case C:** Tường lửa pfSense hoạt động như cầu nối trong suốt (Transparent Bridge) lọc L2/L3 trên member interface (`net.link.bridge.pfil_member = 1`, `net.link.bridge.pfil_bridge = 0`, `net.link.bridge.pfil_onlyip = 1`); pfSense không nằm trong baseline topology ban đầu.
13. **Case A:** Được định vị là đối chứng lý thuyết và khuyến nghị kỹ thuật; không trình bày như kịch bản đã thực nghiệm hoàn tất trong dataset hiện hành.

---

## 5. Nguồn trích dẫn và quản trị nguồn (Source & Citation Audit)

### 5.1. Danh mục trích dẫn tuần tự
Chương 2 sử dụng 11 trích dẫn chuẩn, xuất hiện tuần tự từ `[1]` đến `[11]` không gián đoạn:
- `[1]`: NIST SP 800-115 (Kỹ thuật và nguyên tắc kiểm thử an toàn, xuất hiện tại 2.1.2).
- `[2]`: Tài liệu chính thức Kali Linux (Cấu hình môi trường máy quét, xuất hiện tại 2.2.2).
- `[3]`: Microsoft Learn — Direct hosting of SMB over TCP/IP (Cổng 139/445, xuất hiện tại 2.2.4).
- `[4]`: Microsoft Security Bulletin MS17-010 (Thông tin lỗ hổng và mã KB, xuất hiện tại 2.2.5, 2.6.4).
- `[5]`: Microsoft Support Article 4023057 — How to verify that MS17-010 is installed (Ngưỡng `srv.sys >= 6.3.9600.18604`, xuất hiện tại 2.2.5, 2.6.4, 2.7.3).
- `[6]`: Gordon Lyon — Nmap Network Scanning (Kỹ thuật quét SYN, lý do phân loại, filtered, xuất hiện tại 2.3.3, 2.4.2).
- `[7]`: Paulino Calderon — `smb-protocols.nse` (Thăm dò dialect SMB, xuất hiện tại 2.4.2, 2.5.1).
- `[8]`: Microsoft Learn — SMB signing (Chính sách ký số SMB, xuất hiện tại 2.4.2, 2.5.1).
- `[9]`: Paulino Calderon & Ron Bowes — `smb-vuln-ms17-010.nse` (Cơ chế giao dịch SMB trên FID 0 phân tích mã lỗi phản hồi, xuất hiện tại 2.5.1).
- `[10]`: Microsoft Learn — How to detect, enable, and disable SMBv1 (Lệnh PowerShell tắt SMBv1, xuất hiện tại 2.6.2).
- `[11]`: NIST SP 800-41 Rev. 1 (Hướng dẫn chính sách tường lửa, xuất hiện tại 2.6.3).

### 5.2. Quản lý nguồn S032
Nguồn Microsoft Support Article 4023057 đã được External Reviewer chính thức xác minh và đưa vào `SOURCE_LEDGER.md` trên nhánh `main` với mã `S032`. File `work/do-an/SOURCE_LEDGER_PROPOSED_ADDITION_X5.md` được giữ nguyên trạng thái `APPROVED / INCORPORATED AS S032`.

### 5.3. Tuân thủ định dạng cuối chương
Chương 2 tuyệt đối **không** tạo mục `## TÀI LIỆU THAM KHẢO` ở cuối file. Mục thư mục tham khảo toàn cục sẽ do quy trình xuất bản tổng thể xử lý.

---

## 6. Văn phong khoa học (Author Voice & Academic Style)

Bản thảo được rà soát kỹ lưỡng theo các nguyên tắc trong `AUTHOR_VOICE.md`:
- **Ngôi xưng:** Sử dụng ngôi thứ ba khách quan, trang trọng ("nghiên cứu", "đề tài", "phương pháp", "mô hình").
- **Tính trực tiếp kỹ thuật:** Câu văn ngắn gọn, trực diện, đi thẳng vào bản chất giao thức và tham số cấu hình.
- **Loại bỏ từ sáo rỗng:** Tuyệt đối không sử dụng các từ ngữ rỗng nghĩa hoặc cảm thán như "toàn diện", "tối ưu", "chuẩn mực", "chặt chẽ", "vô cùng", "rất", "trong bối cảnh hiện nay".
- **Không dịch thô phản cảm:** Tránh các cụm từ dịch máy như "sự thật mặt đất" (thay bằng "trạng thái hệ thống nội bộ" / "căn cứ nội bộ"), "chân lý nội bộ", "ngăn xếp mạng" khi không phân tích network stack.
- **Kiểm soát độ dài câu:** Toàn bộ các câu phức đã được hiệu chỉnh để có độ dài dưới 50 từ, bảo đảm mạch lạc và không vi phạm linter học thuật (error=0, warning=0).

---

## 7. Báo cáo ngân sách Hình và Bảng (Figure & Table Budget)

Chương 2 tích hợp chính xác **5 Bảng biểu** và **4 Vị trí chờ Hình vẽ** (đạt đúng chỉ tiêu 3–5 hình, 3–5 bảng):

### Danh mục Bảng (5 bảng):
1. **Bảng 2.1 (Mục 2.2.4):** Thông số kỹ thuật của các nút mạng và dịch vụ trong môi trường thực nghiệm baseline.
2. **Bảng 2.2 (Mục 2.3.1):** Phân loại các lớp quan sát và cơ chế thu thập dữ liệu trong mô hình kiểm thử.
3. **Bảng 2.3 (Mục 2.4.2):** Thiết kế các bước đo và dữ liệu kỳ vọng trong Kịch bản 1 — Khảo sát dịch vụ SMB.
4. **Bảng 2.4 (Mục 2.6.5):** Ma trận thiết kế kiểm thử vi sai các biện pháp giảm thiểu.
5. **Bảng 2.5 (Mục 2.7.3):** Khung đối chiếu hai chiều giữa tín hiệu quan sát từ xa và trạng thái bản vá nội bộ.

### Danh mục Vị trí chờ Hình vẽ chuyên nghiệp (4 hình):
1. **[HÌNH 2.1] (Mục 2.2.1):** Kiến trúc mô hình mạng Host-Only cô lập trong môi trường thực nghiệm baseline.
2. **[HÌNH 2.2] (Mục 2.3.1):** Mô hình năm lớp quan sát và ranh giới suy luận an toàn.
3. **[HÌNH 2.3] (Mục 2.5.1):** Quy trình thực nghiệm hai kịch bản khảo sát và đánh giá an ninh SMB.
4. **[HÌNH 2.4] (Mục 2.6.5):** Sơ đồ phương pháp kiểm thử vi sai các biện pháp giảm thiểu.

Mỗi vị trí chờ đều có đầy đủ 4 trường thông tin: Mục đích, Thành phần cần thể hiện, Chú thích dự kiến và Nguồn bằng chứng căn cứ (đặc biệt không chứa mã chứng cứ không tồn tại như S1-RAW-06).

---

## 8. Kiểm toán số lượng từ (Word Count Audit)

- **Mục tiêu quy định:** 3.800 – 4.500 từ.
- **Số từ thực tế đo được:** **4.471 từ** (tính theo biểu thức chuẩn `[0-9A-Za-zÀ-ỹĐđ]+`).
- **Đánh giá:** Nằm hoàn toàn trong khoảng mục tiêu an toàn [3.800, 4.500], sát mức khuyến nghị 4.3k–4.4k, mật độ thông tin kỹ thuật cao, cô đọng, không dàn trải.

---

## 9. Search Gate Verification (Kiểm toán từ khóa bắt buộc)

| Khóa kiểm tra | Giá trị yêu cầu | Giá trị thực tế | Đánh giá |
| :--- | :--- | :--- | :--- |
| `không nhận đủ phản hồi để phân loại` trong 2.5.2 | 0 | 0 | PASS |
| `điều chỉnh dịch vụ LanmanServer` | 0 | 0 | PASS |
| `Tách biệt L3` | 0 | 0 | PASS |
| `Khả năng định tuyến L3` | 0 | 0 | PASS |
| `RST-ACK` trong 2.7.1 | 0 | 0 | PASS |
| `đánh giá khả năng chống tấn công chuyển tiếp` trong 2.7.2 | 0 | 0 | PASS |
| `cổng TCP 445 vẫn mở` trong 2.7.4 | 0 | 0 | PASS |
| `đánh giá nhận diện MS17-010 từ xa` | 0 | 0 | PASS |
| `không gây sập hệ thống` | 0 | 0 | PASS |
| `PeekNamedPipe` | 0 | 0 | PASS |
| `0x2300` | 0 | 0 | PASS |
| `S1-RAW-06` | 0 | 0 | PASS |
| `pfil_bridge = 1` | 0 | 0 | PASS |
| `<safe_nse>` | 0 | 0 | PASS |
| `biện pháp duy nhất` | 0 | 0 | PASS |
| `bảo đảm an toàn kiểm thử` | 0 | 0 | PASS |
| `Mặc định hệ điều hành` | 0 | 0 | PASS |
| `không dùng DNS` | 0 | 0 | PASS |
| `không qua lọc gói của máy vật lý` | 0 | 0 | PASS |
| `microsoft-ds` trong văn phong phương pháp 2.4 | 0 | 0 | PASS |
| `netbios-ssn` trong văn phong phương pháp 2.4 | 0 | 0 | PASS |
| `syn-ack` trong văn phong phương pháp 2.4 | 0 | 0 | PASS |
| `SMB 2.0.2 đến 3.0.2` trong 2.7 | 0 | 0 | PASS |
| `pfil_member = 1` | >= 1 | 1 | PASS |
| `pfil_bridge = 0` | >= 1 | 1 | PASS |
| `pfil_onlyip = 1` | >= 1 | 1 | PASS |

---

## 10. Kết quả kiểm tra chất lượng tự động (Automated QA Results)

| Công cụ kiểm tra | Lệnh thực thi | Kết quả | Ghi chú |
| :--- | :--- | :--- | :--- |
| **Project Validator** | `uv run python scripts/validate_project.py` | **PASS** | Kiểm tra toàn vẹn cấu trúc dự án |
| **Unit Tests** | `uv run python -m unittest discover -s tests -p "test_*.py"` | **PASS** (7/7 tests) | Toàn bộ kiểm thử đơn vị thành công |
| **Academic Linter** | `uv run python .agents/.../lint_vi_academic.py work/do-an/CHAPTER_2.md` | **PASS** (0 err, 0 warn) | Không phát hiện mẫu văn phong cần xem xét |
| **Git Diff Check** | `git diff --check` | **PASS** | Không có khoảng trắng thừa hay lỗi định dạng |
| **Citation Auditor** | `uv run python scripts/audit_ieee_citations.py work/do-an/CHAPTER_2.md` | **CONFIRMED** | 11/11 citation xuất hiện tuần tự [1]–[11] |

---

## 11. Kết luận và đề xuất trạng thái

Executor / Writing Agent xác nhận đã đóng toàn bộ các khuyến nghị sửa đổi nhỏ (MR-01 đến MR-10) từ Hội đồng phản biện R4, hoàn thiện bản thảo Chương 2 đạt chất lượng kỹ thuật và văn phong học thuật cao nhất.

**Trạng thái bàn giao:**
`X5_STRUCTURAL_REWRITE_R5_READY_FOR_FINAL_EXTERNAL_REVIEW`
