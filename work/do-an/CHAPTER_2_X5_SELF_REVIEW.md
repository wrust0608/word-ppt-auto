# BÁO CÁO TỰ ĐÁNH GIÁ VIẾT LẠI CẤU TRÚC CHƯƠNG 2 (X5 R4 SELF-REVIEW)

**Thời điểm thực hiện:** 2026-10-05
**Vai trò thực hiện:** Executor / Writing Agent
**Tài liệu đánh giá:** `work/do-an/CHAPTER_2.md`
**Nhánh làm việc:** `feature/x5-chapter-2-structural-revision`
**Căn cứ đánh giá:** `X5_STRUCTURAL_REWRITE_EXTERNAL_REVIEW_R3.md`, `PROJECT_STATE.md` (DEC-31, DEC-32), `SOURCE_LEDGER.md`
**Trạng thái đề xuất:** `X5_STRUCTURAL_REWRITE_R4_READY_FOR_EXTERNAL_REVIEW`

---

## 1. Kiểm tra cấu trúc và tính duy nhất của từng phần (Structure & Role Uniqueness)

### 1.1. Tuân thủ đề cương đã khóa (Canonical Outline Match)
Bản thảo Chương 2 tuân thủ tuyệt đối cấu trúc được Người dùng phê duyệt tại Change Request CR-2026-10-05-X5 và DEC-30:
- **Tiêu đề chương:** `# CHƯƠNG 2. THIẾT KẾ MÔ HÌNH VÀ PHƯƠNG PHÁP THỰC NGHIỆM`
- **Số lượng phân mục:** Đạt chính xác **8/8 H2** và **27/27 H3**.
- **Thứ tự và định danh:** 100% heading giữ nguyên văn bản canonical, không thêm heading mới, không bớt heading, không đổi tên, không đảo thứ tự.
- **Không hồi quy cấu trúc cũ:** Loại bỏ hoàn toàn mô hình phân mảnh cũ.

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

## 2. Kiểm toán các điểm sửa đổi kỹ thuật vòng R4 (R4 Final Technical Micro-Patch)

Vòng R4 giải quyết dứt điểm toàn bộ blocker và các điểm tinh chỉnh độ chính xác từ `X5_STRUCTURAL_REWRITE_EXTERNAL_REVIEW_R3.md`:

| STT | Vấn đề R3 nêu | Hành động xử lý trong R4 | Vị trí cập nhật trong CHAPTER_2.md | Kết quả kiểm toán |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **BLOCKER: Cơ chế `smb-vuln-ms17-010` sai nguồn** | Bỏ hoàn toàn `PeekNamedPipe (opcode 0x2300)`; bám sát Nmap NSEDoc chính thức: kết nối `IPC$`, thực hiện giao dịch SMB trên FID 0 và phân tích mã trạng thái phản hồi để tìm dấu hiệu MS17-010 [9] | Mục 2.5.1 | `PeekNamedPipe` = 0, `0x2300` = 0 |
| **2** | **Case C rule wording chứa SYN** | Chuyển thành "Luật chặn TCP có bật ghi log, áp dụng từ `192.168.56.10` tới `192.168.56.20` trên các cổng 139 và 445"; chuyển gói SYN về log quan sát thuộc Chương 3 | Mục 2.6.3 | Khớp C-RULE-02 |
| **3** | **Rò rỉ tập dialect trong 2.7.2** | Thay thế exact dialect set `SMB 2.0.2 đến 3.0.2` bằng cụm trung tính `các dialect SMB2/SMB3`; danh sách dialect cụ thể thuộc Chương 3 | Mục 2.7.2 | `SMB 2.0.2 đến 3.0.2` = 0 |
| **4** | **Patch baseline precision trong 2.2.5** | Phản ánh đầy đủ canonical mapping: không ghi nhận KB4012213 hoặc KB4012216, không ghi nhận bản cập nhật thay thế tương ứng theo mapping, `srv.sys < 6.3.9600.18604` xác nhận UNPATCHED | Mục 2.2.5 | Đầy đủ mapping |
| **5** | **Tuyệt đối hóa patching trong 2.6.4** | Bỏ cụm "biện pháp duy nhất tác động trực tiếp"; chuyển thành "Patching là biện pháp trực tiếp thay đổi trạng thái bản vá của implementation bị ảnh hưởng bởi MS17-010 trong driver nhân `srv.sys` [4], [5]" | Mục 2.6.4 | `biện pháp duy nhất` = 0 |
| **6** | **Diễn giải trạng thái UNPATCHED trong 2.5.2** | Bỏ nhận định "phản ánh khiếm khuyết trong nhân"; sửa thành "Trạng thái `UNPATCHED` cho biết hệ thống chưa đạt mức cập nhật được Microsoft xác minh cho MS17-010; trạng thái này không tự chứng minh khai thác thành công" | Mục 2.5.2 | Khách quan, chuẩn mực |
| **7** | **Đánh giá Case B trong 2.7.4** | Bỏ câu dạng actual result ("tính sẵn sàng SMB2/3 vẫn được quan sát"); chuyển thành tiêu chí kiểm tra: "đồng thời kiểm tra các dialect SMB2/SMB3 còn khả dụng trong phép thương lượng sau can thiệp hay không" | Mục 2.7.4 | Tiêu chí phương pháp |
| **8** | **Văn phong tổng kết chương trong 2.8** | Bỏ "bảo đảm an toàn kiểm thử" và "tạo cơ sở chuẩn xác"; chuyển thành "giới hạn phạm vi kết nối của lab và hỗ trợ kiểm soát rủi ro trong quá trình thử nghiệm" và "làm cơ sở để Chương 3 trình bày dữ liệu đo đạc thực tế" | Mục 2.8 | `bảo đảm an toàn kiểm thử` = 0 |

---

## 3. Kiểm toán rò rỉ kết quả (Result Leakage Audit)

Chương 2 giữ nghiêm ngặt ranh giới: **HOW / WITH WHAT / UNDER WHAT CONDITIONS**, không kể trước kết quả thực nghiệm (**WHAT WAS OBSERVED**):
- **Kịch bản 1:** Trình bày thiết kế lệnh `nmap -sS -sV` và 4 kịch bản NSE an toàn; không công bố danh sách dialect thực tế hay banner chi tiết quan sát được trên cổng 139/445 trong lượt chạy cụ thể (`microsoft-ds` = 0, `netbios-ssn` = 0, `syn-ack` = 0 trong văn phong phương pháp 2.4).
- **Kịch bản 2:** Mô tả cơ chế hoạt động chuẩn của `smb-vuln-ms17-010.nse` (giao dịch SMB trên FID 0 phân tích mã lỗi); không trình bày kết quả quan sát cụ thể hay lỗi chi tiết thu được.
- **Case B:** Trình bày lệnh can thiệp PowerShell `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` và kế hoạch đo lại dialect/NSE-04; không đưa bảng so sánh output trước/sau can thiệp.
- **Case C:** Trình bày cấu hình Transparent Bridge pfSense, cờ `net.link.bridge.pfil_member = 1`, `net.link.bridge.pfil_bridge = 0`, `net.link.bridge.pfil_onlyip = 1` và luật chặn TCP cổng 139/445 có ghi log; không trích xuất log block thực tế của pfSense.
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
11. **Case B:** Can thiệp `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` là làm cứng giao thức (Protocol Hardening) mức dịch vụ; không phải bản vá, không gỡ tính năng, không thay đổi driver nhị phân.
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
- `[6]`: Gordon Lyon — Nmap Network Scanning (Kỹ thuật quét SYN, reason, filtered, xuất hiện tại 2.3.3, 2.4.2).
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
- **Kiểm soát độ dài câu:** Toàn bộ các câu phức đã được hiệu chỉnh để có độ dài dưới 50 từ, bảo đảm mạch lạc và không vi phạm linter học thuật.

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
- **Số từ thực tế đo được:** **4.486 từ** (tính theo biểu thức chuẩn `[0-9A-Za-zÀ-ỹĐđ]+`).
- **Đánh giá:** Nằm hoàn toàn trong khoảng mục tiêu an toàn [3.800, 4.500], mật độ thông tin kỹ thuật cao, cô đọng, không dàn trải.

---

## 9. Search Gate Verification (Kiểm toán từ khóa bắt buộc)

| Khóa kiểm tra | Giá trị yêu cầu | Giá trị thực tế | Đánh giá |
| :--- | :--- | :--- | :--- |
| `PeekNamedPipe` | 0 | 0 | PASS |
| `0x2300` | 0 | 0 | PASS |
| `pfil_bridge = 1` | 0 | 0 | PASS |
| `pfil_bridge=1` | 0 | 0 | PASS |
| `S1-RAW-06` | 0 | 0 | PASS |
| `<safe_nse>` | 0 | 0 | PASS |
| `microsoft-ds` trong văn phong phương pháp 2.4 | 0 | 0 | PASS |
| `netbios-ssn` trong văn phong phương pháp 2.4 | 0 | 0 | PASS |
| `syn-ack` trong văn phong phương pháp 2.4 | 0 | 0 | PASS |
| `SMB 2.0.2 đến 3.0.2` trong 2.7 | 0 | 0 | PASS |
| `biện pháp duy nhất` | 0 | 0 | PASS |
| `bảo đảm an toàn kiểm thử` | 0 | 0 | PASS |
| `Mặc định hệ điều hành` | 0 | 0 | PASS |
| `không dùng DNS` | 0 | 0 | PASS |
| `không qua lọc gói của máy vật lý` | 0 | 0 | PASS |
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

Executor / Writing Agent xác nhận đã hoàn thành toàn diện vòng sửa đổi kỹ thuật chính xác cuối cùng (final technical micro-patch R4) theo đúng tất cả các chỉ thị của External Reviewer R3 và Người dùng.

**Trạng thái bàn giao:**
`X5_STRUCTURAL_REWRITE_R4_READY_FOR_EXTERNAL_REVIEW`
