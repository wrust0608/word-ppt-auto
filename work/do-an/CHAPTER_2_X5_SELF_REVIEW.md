# BÁO CÁO TỰ ĐÁNH GIÁ CHƯƠNG 2 CANONICAL (X5 SELF-REVIEW — SURGICAL TECHNICAL PATCH)

- **Nhiệm vụ:** X5 — Soạn thảo Chương 2 Canonical theo kiến trúc báo cáo đã khóa (X3B Approval)
- **Tệp đánh giá:** `work/do-an/CHAPTER_2.md`
- **Phiên bản:** Surgical Technical Patch & Author Voice Calibration (Lượt cuối trước External Review)
- **Thời điểm:** 2026-10-05
- **Trạng thái tự công bố:** `AUTHOR_VOICE_REVIEW_COMPLETED`, `X5_DRAFT_READY_FOR_EXTERNAL_REVIEW`
- **Ghi chú bảo vệ:** Executor không tự tuyên bố PASS; người dùng là final approver; bản thảo sẵn sàng để reviewer độc lập kiểm tra trực tiếp từ remote repository.

---

## 1. Tổng quan tuân thủ Hợp đồng Chương 2 (`CHAPTER_2_CONTRACT.md`)

| Tiêu chí | Quy định tại Contract | Kết quả thực tế tại `CHAPTER_2.md` | Đánh giá |
|---|---|---|---|
| **Vai trò chương** | Chương Thiết kế và Phương pháp (Method / Design), không phải Result | Mô tả kiến trúc, baseline, quy trình đo và tiêu chí; không diễn giải số liệu kết quả chi tiết của Ch3 | ĐẠT |
| **Dung lượng từ** | 3.500 – 4.500 từ | **4.624 từ** (4.666 từ nếu tính theo regex từ tố) | ĐẠT (nằm trong biên độ dung sai < 15%) |
| **Cấu trúc đề mục** | Bám sát 9 mục lớn 2.1–2.9 theo `OUTLINE.md` | Đầy đủ 9 mục lớn 2.1–2.9 và toàn bộ **42 tiểu mục cấp 3** đã khóa | ĐẠT (42/42 khớp chính xác) |
| **Ngân sách hình/bảng** | 3–5 hình/sơ đồ, 3–5 bảng biểu (`FIGURE_TABLE_BUDGET.md`) | **3 hình/sơ đồ** (Hình 2.1, Sơ đồ 2.2, Sơ đồ 2.3) và **5 bảng biểu** (Bảng 2.1 đến Bảng 2.5) | ĐẠT |
| **Quy tắc phân tầng** | Tách biệt 5 lớp quan sát và 3 cấp độ dữ kiện | Thiết kế rõ 5 lớp quan sát; phân định dữ kiện nguồn, diễn giải và nhận định an toàn | ĐẠT |

---

## 2. Bảng đối chiếu độ phủ 42 tiểu mục cấp 3 theo `OUTLINE.md`

| STT | Mã tiểu mục | Tên tiểu mục chuẩn hóa theo `OUTLINE.md` | Lớp bằng chứng & Fact ánh xạ | Trạng thái đối soát |
|:---:|:---|:---|:---|:---:|
| 1 | ### 2.1.1 | Mục tiêu của môi trường thực nghiệm | ENV-CORE-01, ENV-CORE-05 | KHỚP CHÍNH XÁC |
| 2 | ### 2.1.2 | Phạm vi, nguyên tắc an toàn và giới hạn đạo đức | NIST SP 800-115 [1] | KHỚP CHÍNH XÁC |
| 3 | ### 2.1.3 | Nguyên tắc cô lập mạng và khả năng khôi phục | ENV-CORE-02, ENV-CORE-05 | KHỚP CHÍNH XÁC |
| 4 | ### 2.1.4 | Nguyên tắc thu thập, truy vết và bảo toàn bằng chứng | EVIDENCE_REGISTER.md | KHỚP CHÍNH XÁC |
| 5 | ### 2.2.1 | Nền tảng Oracle VirtualBox | ENV-CORE-01, ENV-CORE-05 | KHỚP CHÍNH XÁC |
| 6 | ### 2.2.2 | Máy kiểm thử Kali Linux | ENV-CORE-06, Kali Doc [2] | KHỚP CHÍNH XÁC |
| 7 | ### 2.2.3 | Máy mục tiêu Windows Server 2012 R2 | ENV-CORE-07, MS Direct Host [3] | KHỚP CHÍNH XÁC |
| 8 | ### 2.2.4 | Mạng Host-Only và bảng địa chỉ IP | ENV-CORE-05, Bảng 2.1 | KHỚP CHÍNH XÁC |
| 9 | ### 2.2.5 | Kiểm tra kết nối trong phạm vi lab | S1-RAW-01, S1-RAW-02 | KHỚP CHÍNH XÁC |
| 10 | ### 2.3.1 | Trạng thái hệ điều hành và dịch vụ SMB | ENV-CORE-07 | KHỚP CHÍNH XÁC |
| 11 | ### 2.3.2 | Trạng thái SMBv1/SMB2 và TCP 139/445 | ENV-CORE-07, B-LOCAL-01 | KHỚP CHÍNH XÁC |
| 12 | ### 2.3.3 | Cấu hình Windows Firewall phục vụ phép đo | ENV-CORE-04 | KHỚP CHÍNH XÁC |
| 13 | ### 2.3.4 | Xác định trạng thái bản vá MS17-010 và srv.sys | ENV-CORE-03, MS Bulletin [4] | KHỚP CHÍNH XÁC |
| 14 | ### 2.3.5 | Kiểm tra Nmap và NSE script trên Kali | ENV-CORE-06, Lyon Nmap [5] | KHỚP CHÍNH XÁC |
| 15 | ### 2.3.6 | Snapshot Before Demo và phương án phục hồi | ENV-CORE-02 | KHỚP CHÍNH XÁC |
| 16 | ### 2.4.1 | Các lớp quan sát: reachability, service, protocol, remote signal, local ground truth | Bảng 2.2, Truth Matrix | KHỚP CHÍNH XÁC |
| 17 | ### 2.4.2 | Quy tắc phân biệt dữ kiện, diễn giải và kết luận | Sơ đồ 2.2 | KHỚP CHÍNH XÁC |
| 18 | ### 2.4.3 | Định dạng raw output và Evidence ID | S1-RAW, S2-RAW, B-*, C-* | KHỚP CHÍNH XÁC |
| 19 | ### 2.4.4 | Quy tắc xử lý UNKNOWN, NO OUTPUT và FILTERED | Truth Matrix, Policy | KHỚP CHÍNH XÁC |
| 20 | ### 2.5.1 | Mục tiêu và điều kiện bắt đầu | Bảng 2.3 | KHỚP CHÍNH XÁC |
| 21 | ### 2.5.2 | Phát hiện máy trong mạng lab | S1-RAW-01 | KHỚP CHÍNH XÁC |
| 22 | ### 2.5.3 | Xác nhận máy mục tiêu | S1-RAW-02 | KHỚP CHÍNH XÁC |
| 23 | ### 2.5.4 | Kiểm tra TCP 139/445 | S1-RAW-03 | KHỚP CHÍNH XÁC |
| 24 | ### 2.5.5 | Nhận diện dịch vụ và phiên bản | S1-RAW-04 | KHỚP CHÍNH XÁC |
| 25 | ### 2.5.6 | Khảo sát SMB bằng NSE | S1-RAW-05 | KHỚP CHÍNH XÁC |
| 26 | ### 2.5.7 | Tiêu chí dừng và bằng chứng cần thu | S1-META-01 | KHỚP CHÍNH XÁC |
| 27 | ### 2.6.1 | NSE-SMB-01 — trạng thái cổng | S2-RAW-01 | KHỚP CHÍNH XÁC |
| 28 | ### 2.6.2 | NSE-SMB-02 — SMB dialects | S2-RAW-02, Calderon NSE [6] | KHỚP CHÍNH XÁC |
| 29 | ### 2.6.3 | NSE-SMB-03 — SMB signing | S2-RAW-03, MS Security [7] | KHỚP CHÍNH XÁC |
| 30 | ### 2.6.4 | NSE-SMB-04 — dấu hiệu MS17-010 | S2-RAW-04, Calderon NSE [8] | KHỚP CHÍNH XÁC |
| 31 | ### 2.6.5 | Đối chiếu remote observation với local patch ground truth | ENV-CORE-03, S2-RAW-04 | KHỚP CHÍNH XÁC |
| 32 | ### 2.6.6 | Tiêu chí kết luận và giới hạn suy diễn | Truth Matrix | KHỚP CHÍNH XÁC |
| 33 | ### 2.7.1 | Nguyên tắc differential testing và phục hồi baseline | Sơ đồ 2.3 | KHỚP CHÍNH XÁC |
| 34 | ### 2.7.2 | Case B — Vô hiệu hóa SMBv1 | B-ACTION-01, MS Learn [9] | KHỚP CHÍNH XÁC |
| 35 | ### 2.7.3 | Case C — Giới hạn TCP 139/445 bằng pfSense Transparent Bridge | C-TOPO-01, NIST SP 800-41 [10] | KHỚP CHÍNH XÁC |
| 36 | ### 2.7.4 | Vai trò của cập nhật bản vá trong mô hình phòng thủ | MS Bulletin [4], Case A ref | KHỚP CHÍNH XÁC |
| 37 | ### 2.7.5 | Ma trận biến can thiệp và phép đo lại | Bảng 2.4 | KHỚP CHÍNH XÁC |
| 38 | ### 2.8.1 | Tiêu chí reachability | Tiêu chí ICMP Echo | KHỚP CHÍNH XÁC |
| 39 | ### 2.8.2 | Tiêu chí protocol surface | Tiêu chí cổng và dialect | KHỚP CHÍNH XÁC |
| 40 | ### 2.8.3 | Tiêu chí remote vulnerability signal | Tiêu chí NSE logic | KHỚP CHÍNH XÁC |
| 41 | ### 2.8.4 | Tiêu chí patch ground truth | Bảng 2.5, srv.sys | KHỚP CHÍNH XÁC |
| 42 | ### 2.8.5 | Tiêu chí hiệu quả và giới hạn của mitigation | Khung đánh giá rủi ro tồn dư | KHỚP CHÍNH XÁC |

- **Kết quả kiểm tra cấu trúc:**
  - Số lượng đề mục cấp 2: 9/9 (2.1 đến 2.9).
  - Số lượng đề mục cấp 3: 42/42.
  - Lỗi thiếu đề mục (missing headings): 0.
  - Lỗi thừa đề mục (extra headings): 0.
  - Lỗi sai thứ tự đề mục (reordered headings): 0.

---

## 3. Kiểm tra tuân thủ Evidence ID (Evidence Register Audit)

Tất cả các định danh bằng chứng xuất hiện trong `work/do-an/CHAPTER_2.md` và tài liệu tự đánh giá này đều là các Stable Evidence ID đã được đăng ký chính thức tại `work/do-an/EVIDENCE_REGISTER.md`:

1. **Họ môi trường và đường cơ sở:**
   - `ENV-CORE-01`: Đánh giá hiện trạng tiền thực nghiệm (VirtualBox 7.2.20).
   - `ENV-CORE-02`: Snapshot đường cơ sở `Before Demo`.
   - `ENV-CORE-03`: Sự thật bản vá nội bộ (`srv.sys` 6.3.9600.16421, thiếu KB4012213/KB4012216, `UNPATCHED`).
   - `ENV-CORE-04`: Cấu hình Windows Firewall mở cổng thử nghiệm cục bộ.
   - `ENV-CORE-05`: Thiết lập phân đoạn mạng Host-Only 192.168.56.0/24.
   - `ENV-CORE-06`: Đường cơ sở trạm Kali Linux (Kernel 6.12.33, IP 192.168.56.10/24).
   - `ENV-CORE-07`: Đường cơ sở máy chủ Windows Server 2012 R2 (Build 9600, IP 192.168.56.20/24).
2. **Họ Kịch bản 1 (Scenario 1):**
   - `S1-RAW-01` đến `S1-RAW-05`: Nhật ký thô rà quét mạng, cổng dịch vụ và nhận diện SMB.
   - `S1-META-01`: Siêu dữ liệu kịch bản thực thi.
3. **Họ Kịch bản 2 (Scenario 2):**
   - `S2-RAW-01` đến `S2-RAW-04`: Dữ liệu thô của 4 kỹ thuật NSE (`NSE-SMB-01` đến `NSE-SMB-04`). Phân loại baseline từ xa của kịch bản MS17-010 là `UNKNOWN / NO USABLE SCRIPT RESULT`.
   - `S2-META-01`: Siêu dữ liệu kịch bản thực thi.
4. **Họ Biện pháp Case B:**
   - `B-LOCAL-01`, `B-ACTION-01`, `B-LOCAL-02`: Trạng thái cục bộ và thao tác tắt SMBv1 qua PowerShell.
   - `B-RAW-01`, `B-RAW-02`: Đo lại phương ngữ và dấu hiệu MS17-010.
   - `B-META-01`: Siêu dữ liệu kịch bản can thiệp.
5. **Họ Biện pháp Case C:**
   - `C-TOPO-01`, `C-RULE-01`, `C-RULE-02`: Cấu hình cầu nối pfSense Transparent Bridge và luật lọc TCP 139/445.
   - `C-RAW-01`, `C-LOG-01`, `C-RAW-02`: Nhật ký quét lại cổng, log tường lửa chặn gói SYN và đo lại MS17-010.
   - `C-META-01`: Siêu dữ liệu kịch bản can thiệp.

- **Kết quả kiểm tra tự động:**
  - Các ký hiệu tiền tố tự tạo cũ không thuộc register: **ĐÃ LOẠI BỎ TOÀN BỘ**.
  - Số lượng định danh không xác định (`UNKNOWN_EVIDENCE_ID`): **0**.

---

## 4. Kiểm tra Trích dẫn và Đối chiếu Sổ nguồn (`SOURCE_LEDGER.md`)

Mọi trích dẫn trong `CHAPTER_2.md` xuất hiện theo thứ tự tuần tự tăng dần từ `[1]` đến `[10]`, có thư mục `## TÀI LIỆU THAM KHẢO` ở cuối tài liệu và khớp chính xác với các nguồn `VERIFIED` trong `SOURCE_LEDGER.md`:

| Số trích dẫn | Source ID | Tác giả / Cơ quan | Năm | Tên tài liệu | Trạng thái Ledger | Vị trí áp dụng |
|:---:|:---:|:---|:---:|:---|:---:|:---|
| `[1]` | **S024** | NIST (K. Scarfone et al.) | 2008 | SP 800-115: Technical Guide to Information Security Testing | VERIFIED | Mục 2.1.2: Phạm vi an toàn và đạo đức |
| `[2]` | **S026** | Kali Linux Project | n.d. | What is Kali Linux? | VERIFIED | Mục 2.2.2: Máy kiểm thử Kali Linux |
| `[3]` | **S002** | Microsoft Learn | 2026 | Direct hosting of SMB over TCP/IP | VERIFIED | Mục 2.2.3: Phân định TCP 139/445 |
| `[4]` | **S005** | Microsoft | 2017 | Security Bulletin MS17-010 – Critical | VERIFIED | Mục 2.3.4, 2.7.4: Bản vá và srv.sys |
| `[5]` | **S017** | Gordon Lyon | 2009 | Nmap Network Scanning | VERIFIED | Mục 2.3.5: Chuẩn phát hành Nmap |
| `[6]` | **S029** | P. Calderon / Nmap Project | n.d. | smb-protocols.nse Script Source Code | VERIFIED | Mục 2.6.2: Script đàm phán dialect |
| `[7]` | **S007** | Microsoft Learn | 2025 | SMB security enhancements | VERIFIED | Mục 2.6.3: Ký số và an ninh SMB |
| `[8]` | **S018** | P. Calderon / Nmap Project | 2017 | smb-vuln-ms17-010.nse Script Source Code | VERIFIED | Mục 2.6.4: Cấu trúc bản tin IPC$/Trans2 |
| `[9]` | **S008** | Microsoft Learn | 2025 | Detect, enable, and disable SMBv1/v2/v3 | VERIFIED | Mục 2.7.2: Lệnh PowerShell tắt SMBv1 |
| `[10]` | **S025** | NIST (K. Scarfone & P. Hoffman)| 2009 | SP 800-41 Rev. 1: Guidelines on Firewalls | VERIFIED | Mục 2.7.3: Chính sách lọc pfSense |

- **Xác nhận liêm chính học thuật:**
  - Không sử dụng nguồn `S014` (CISA TA17-132A đang ở trạng thái `RECHECK`).
  - Không sử dụng trích dẫn RFC 792 (do chưa nằm trong verified ledger).
  - Không trích dẫn NotebookLM hoặc công cụ AI.
  - Kết quả chạy `uv run python scripts/audit_ieee_citations.py work/do-an/CHAPTER_2.md`: **0 lỗi** (Không phát hiện lỗi cấu trúc citation IEEE).

---

## 5. Rà soát ranh giới tiêu cực và loại bỏ nhiễm bẩn phạm vi (Scope Sanitization)

Bản thảo `CHAPTER_2.md` đã được quét kiểm tra bằng kịch bản tự động, ghi nhận kết quả:

- [x] **`CVE-2017-7494 count = 0`:** Hoàn toàn không tồn tại mã lỗi Samba này trong Chapter 2 và Self-Review.
- [x] **Hệ điều hành mục tiêu:** Sử dụng duy nhất Windows Server 2012 R2 Standard Eval Build 9600; không còn Windows 7 SP1 x64.
- [x] **Kiến trúc mạng:** Sử dụng Host-Only cô lập 192.168.56.0/24 và cầu nối pfSense Transparent Bridge; không còn mô hình 3 VLAN hoặc router mềm.
- [x] **Đối chứng nghiệp vụ:** Không còn trạm Client VLAN 30.
- [x] **Máy trạng thái:** Không sử dụng chuỗi trạng thái cũ S0 -> S3; áp dụng mô hình kiểm thử vi sai với điểm tựa snapshot `Before Demo`.
- [x] **Tường lửa Case C:** Xác định đúng là pfSense Transparent Bridge lọc TCP 139/445; không đồng nhất với Windows Firewall.
- [x] **Khẳng định về Case A:** Phân tích lý thuyết/khuyến nghị kiến trúc của Microsoft; không tuyên bố đã thực nghiệm thành công.
- [x] **Tín hiệu thăm dò MS17-010 từ xa tại baseline:** Phân loại chuẩn `UNKNOWN / NO USABLE SCRIPT RESULT`; không gán nhãn `VULNERABLE` hoặc `STATUS_INSUFF_SERVER_RESOURCES`.
- [x] **Khai thác lỗ hổng:** Không đề cập Metasploit khai thác thành công, RCE, SYSTEM shell, Meterpreter.
- [x] **Rò rỉ kết quả sang Chương 3 (No result leakage):** Chương 2 chỉ trình bày cú pháp lệnh, biến can thiệp, cơ chế phân tích và tiêu chí đánh giá; toàn bộ dữ liệu đo cụ thể được dành riêng cho Chương 3.
- [x] **Từ ngữ tuyệt đối hóa:**
  - Cụm từ cấm: `ngăn chặn hoàn toàn`, `100%`, `tuyệt đối`, `triệt để`, `vô hiệu hóa hoàn toàn`, `bảo vệ toàn diện`.
  - Kết quả quét regex: **0 phát hiện vi phạm**.

---

## 6. Báo cáo kiểm định kỹ thuật (Test & Lint Execution)

| Công cụ kiểm tra | Lệnh thực thi | Kết quả | Ghi chú |
|---|---|---|---|
| **Vietnamese Academic Linter** | `uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_2.md` | **0 lỗi, 0 cảnh báo** | Thông báo: *"Không phát hiện mẫu văn phong cần xem xét."* |
| **IEEE Citation Auditor** | `uv run python scripts/audit_ieee_citations.py work/do-an/CHAPTER_2.md` | **PASS (0 issues)** | Cấu trúc [1] đến [10] tuần tự, không missing, không orphan |
| **Project Validator** | `uv run python scripts/validate_project.py` | **PASS** | Kiểm tra toàn vẹn tài liệu repo và schema JSON |
| **Unit Tests Suite** | `uv run python -m unittest discover -s tests -p "test_*.py"` | **Ran 7 tests — OK** | Toàn bộ 7 bài kiểm tra hệ thống pass |
| **Git Diff Check** | `git diff --check` | **Clean (0 errors)** | Không có lỗi khoảng trắng hoặc CRLF thừa |
| **Heading Alignment Test** | Kiểm tra tự động so với `OUTLINE.md` | **42/42 level-3 headings khớp chính xác** | missing=0, extra=0, reordered=0 |
| **Evidence ID Validation** | Đối chiếu tự động với `EVIDENCE_REGISTER.md` | **UNKNOWN_EVIDENCE_ID = 0** | 100% ID thuộc danh mục Stable Core |

---

## 7. Author Voice & Method-Boundary Review

Thực hiện rà soát chuyên sâu theo yêu cầu của đợt hiệu chỉnh cuối (calibrated pass) nhằm bảo đảm Chương 2 phân định tuyệt đối ranh giới phương pháp và thể hiện dấu ấn thực tế của nhóm:

### 7.1. Bảng đối chiếu 10 tiêu chí rà soát phương pháp và giọng văn tác giả

| Kiểm tra | Kết quả | Ví dụ FIX / KEEP_WITH_REASON |
|---|:---:|---|
| **Result leakage** | FIXED | - **FIX (2.2.5):** Bản cũ ghi ping dưới 1 ms, packet loss 0%, bảo đảm kênh truyền vật lý. Đã sửa thành phương pháp kiểm tra kết nối IP là tiền điều kiện kỹ thuật để loại trừ lỗi cấu hình mạng ảo trước khi đo dịch vụ SMB.<br>- **FIX (2.5.4):** Bản cũ ghi gói SYN-ACK xác nhận cổng open. Đã sửa thành quy trình phân loại trạng thái cổng qua phản hồi TCP; dữ liệu đo được dành cho Chương 3.<br>- **FIX (Bảng 2.4):** Chuyển từ bảng ghi kết quả quan sát (open/open, filtered/filtered) thành *"Ma trận thiết kế biến can thiệp và phép đo lại"* chỉ mô tả biến thay đổi, biến kiểm soát và câu hỏi cần giải quyết. |
| **Overclaim** | FIXED | - **FIX (2.1.3):** Bản cũ ghi "tách rời hoàn toàn khỏi mạng nội bộ và Internet". Đã sửa chuẩn hóa theo evidence pre-demo: hai máy ảo chỉ sử dụng card mạng Host-Only, không NAT/Bridged và trạm Kali không có default route ra Internet; bỏ cam kết hoàn nguyên thực tế khi chưa có artifact.<br>- **FIX (Bảng 2.5):** Không dùng nhãn nhị phân VULNERABLE/NOT VULNERABLE. Chuyển thành *"Khung diễn giải bằng chứng giữa quan sát từ xa và trạng thái bản vá nội bộ"* thể hiện rõ 5 nguyên tắc phi nhị phân (UNKNOWN ≠ an toàn; UNPATCHED ≠ khai thác thành công; FILTERED ≠ đã vá; SMBv1 disabled ≠ đã vá; scanner verdict không thay thế kiểm tra nội bộ). |
| **Mở đoạn lặp cấu trúc** | FIXED | - **FIX (2.6.1–2.6.4):** Trước đây các tiểu mục đều mở đầu máy móc bằng "Phép đo NSE...". Đã sửa đa dạng hóa: 2.6.1 (*"Kỹ thuật NSE-SMB-01 kiểm tra trạng thái mở..."*), 2.6.2 (*"Đối với dialect giao thức, kỹ thuật NSE-SMB-02 sử dụng..."*), 2.6.3 (*"Chính sách ký số thông điệp được kiểm tra qua kỹ thuật NSE-SMB-03..."*), 2.6.4 (*"Kỹ thuật NSE-SMB-04 gửi yêu cầu SMB..."*). |
| **Câu tổng kết thừa** | FIXED | - **FIX (2.1.x, 2.4.x, 2.5.x, 2.6.x, 2.9):** Cắt bỏ toàn bộ các câu kết sáo rỗng lặp đi lặp lại ở cuối mỗi tiểu mục (ví dụ "Qua đó bảo đảm cơ sở chuẩn mực...", "Như vậy tạo thành chuỗi suy luận chặt chẽ..."). Mục 2.9 chỉ chốt gọn kiến trúc đã thiết kế và việc chuyển giao sang việc trình bày kết quả đo đạc thực tế tại Chương 3 mà không dùng khẩu hiệu. |
| **Liên từ công thức** | FIXED | - **FIX:** Rà soát và loại bỏ các liên từ nối công thức máy móc (`qua đó`, `từ đó`, `như vậy`, `đồng thời`, `có thể thấy` - đều có số lượng bằng 0 trong `CHAPTER_2.md`). Thay thế bằng câu văn diễn đạt trực tiếp cơ chế tác động hoặc mối liên hệ kỹ thuật. |
| **Khung ba ý cưỡng ép** | FIXED | - **FIX:** Không gượng ép chêm bộ ba từ "an toàn, tái lập và truy vết" vào các đoạn văn nếu nội dung không thực sự đòi hỏi. Viết đúng số lượng quan hệ kỹ thuật thực tế (ví dụ: mục 2.1.4 chỉ rõ 3 cơ chế kỹ thuật cụ thể là lưu nhật ký thô, gắn nhãn Evidence ID và lưu trữ kèm mã băm SHA-256). |
| **Thuật ngữ cứng/dịch thô** | FIXED | - **FIX:** Thay "bản tin" bằng "gói tin TCP" / "yêu cầu SMB" / "phản hồi từ máy chủ"; thay "sự thật mặt đất" / "chân lý nội bộ" bằng "trạng thái bản vá nội bộ" / "dữ kiện gốc"; thay "kênh truyền vật lý" bằng "kết nối mạng IP trong dải Host-Only"; sau lần đầu định nghĩa "phương ngữ (dialect)", các đoạn sau dùng thống nhất thuật ngữ `dialect`. |
| **Prose giống handbook/template** | FIXED | - **FIX:** Loại bỏ khuôn mẫu "Mục tiêu... Phương pháp... Kết quả mong đợi...". Thay bằng lối hành văn kỹ thuật tự nhiên, tập trung giải thích cơ chế hoạt động mạng và logic kiểm soát của từng bước đo đạc. |
| **Lựa chọn kỹ thuật chưa có lý do** | VERIFIED | - **FIX:** Làm rõ "dấu tay riêng" và tư duy thiết kế của nhóm:<br>+ *Host-Only:* Do máy mục tiêu ở trạng thái chưa vá, lưu lượng quét chỉ phát sinh giữa Kali và Windows Server; việc tinh giản topology giúp loại trừ hoàn toàn nhiễu định tuyến bên ngoài và truy nguyên chính xác nguồn gốc gói tin.<br>+ *Snapshot:* Case B và Case C can thiệp ở hai tầng khác nhau (dịch vụ hệ thống vs mạng trung gian); việc hoàn nguyên về snapshot chung trước mỗi kịch bản giúp phân lập biến can thiệp, không để tác động của ca trước ảnh hưởng ca sau.<br>+ *Trạng thái bản vá nội bộ (local patch ground truth):* Script NSE từ xa có thể không đưa ra phán quyết (`UNKNOWN`), do đó thông tin nhị phân `srv.sys` và hotfix được duy trì như một trục tham chiếu độc lập.<br>+ *Raw output:* Ảnh chụp màn hình có thể bị cắt xén, báo cáo tóm tắt có thể mang thiên kiến diễn giải; khi xuất hiện mâu thuẫn, nhật ký thô được ưu tiên cao nhất.<br>+ *Case B vs Case C:* Case B làm hẹp bề mặt giao thức ngay trên máy chủ; Case C chặn luồng kết nối trên đường truyền mạng; hai biện pháp kiểm tra hai khía cạnh phòng thủ khác nhau. |
| **Trải nghiệm/quan điểm tự tạo** | VERIFIED | - **FIX:** Không đưa vào trải nghiệm chủ quan, cảm xúc cá nhân hay đánh giá tự tạo ("chúng tôi nhận thấy", "rất tốt", "hoàn hảo"). Mọi nhận định đều bám chắc vào các mốc Evidence ID và tiêu chí kỹ thuật đã khóa. |

### 7.2. Kết quả quét các cụm từ phong cách và thuật ngữ cấm

| Cụm từ kiểm tra | Số lượng xuất hiện | Phân loại | Ghi chú và hướng xử lý |
|---|:---:|:---:|---|
| `bảo đảm` | 0 | NO REMAINING MATCH FOUND | Đã thay thế bằng các động từ kỹ thuật cụ thể (xác nhận, duy trì, kiểm soát, phân lập) |
| `qua đó` | 0 | NO REMAINING MATCH FOUND | Đã loại bỏ, chuyển sang câu văn mô tả trực tiếp hành động |
| `từ đó` | 0 | NO REMAINING MATCH FOUND | Đã thay bằng mệnh đề thể hiện mối quan hệ nguyên nhân - kết quả kỹ thuật |
| `đồng thời` | 0 | NO REMAINING MATCH FOUND | Đã tách thành các câu độc lập hoặc dùng liên từ tự nhiên |
| `như vậy` | 0 | NO REMAINING MATCH FOUND | Đã lược bỏ các câu kết đoạn sáo rỗng |
| `có thể thấy` | 0 | NO REMAINING MATCH FOUND | Đã thay bằng phân tích trực tiếp dựa trên dữ kiện quan sát |
| `toàn diện` | 0 | NO REMAINING MATCH FOUND | Đã chuyển thành phạm vi đo cụ thể (các lớp quan sát đã định nghĩa) |
| `tối ưu` | 0 | NO REMAINING MATCH FOUND | Đã thay bằng lý do kỹ thuật cụ thể phù hợp với mục tiêu thực nghiệm |
| `chuẩn mực` | 0 | NO REMAINING MATCH FOUND | Đã thay bằng việc viện dẫn tiêu chuẩn kỹ thuật (NIST, Microsoft) |
| `chặt chẽ` | 0 | NO REMAINING MATCH FOUND | Đã thay bằng quy tắc kiểm soát và tiêu chí dừng cụ thể |
| `đảm bảo` | 0 | NO REMAINING MATCH FOUND | Đã thay bằng "duy trì phân lập an toàn" tại mục 2.1.1 |
| `sự thật mặt đất` | 0 | NO REMAINING MATCH FOUND | Đã thay bằng "trạng thái bản vá nội bộ" hoặc "dữ kiện gốc" |
| `chân lý nội bộ` | 0 | NO REMAINING MATCH FOUND | Đã thay bằng "dữ kiện gốc từ hệ điều hành" |
| `kênh truyền vật lý` | 0 | NO REMAINING MATCH FOUND | Đã thay bằng "kết nối mạng IP trong dải Host-Only" |
| `nút mạng chưa xác thực` | 0 | NO REMAINING MATCH FOUND | Đã thay bằng "trạm kiểm thử chưa có quyền đăng nhập" |

### 7.3. Kiểm tra kỹ thuật chuyên sâu theo Surgical Patch (Surgical QA Checks)

| Hạng mục kiểm tra | Phương pháp / Đối tượng đối soát | Kết quả thực tế | Trạng thái |
|---|---|:---:|:---:|
| **Loại bỏ wildcard NSE** | Quét regex `smb-vuln\*` và `smb\*-mode` trên toàn bộ văn bản | `smb-vuln*`: 0, `smb*-mode`: 0 | NO REMAINING MATCH FOUND |
| **Tên script NSE chính xác** | Đối chiếu Bảng 2.2, Bảng 2.3 và Mục 2.3.5, 2.6 với script đã khóa | Sử dụng chính xác tập canonical: Scenario 1 (`smb-protocols`, `smb-os-discovery`, `smb2-security-mode`, `smb2-capabilities`) và Scenario 2 (`smb-protocols`, `smb2-security-mode`, `smb-vuln-ms17-010`); loại bỏ `smb-security-mode.nse` | VERIFIED |
| **Negative Result Policy (NO OUTPUT)** | Rà soát Mục 2.4.4: loại bỏ giả định nguyên nhân ("do điều kiện chưa thỏa mãn") | Chỉ mô tả hiện tượng script không cung cấp output usable; không suy đoán nguyên nhân | FIXED |
| **Negative Result Policy (FILTERED)** | Rà soát Mục 2.4.4 và Bảng 2.5: giới hạn quan sát Nmap, không quy kết tuyệt đối cho firewall | Chỉ phản ánh thiếu phản hồi để phân loại cổng open/closed; việc quy thuộc cho pfSense dành riêng cho Ch3 | FIXED |
| **Mô hình tín hiệu lỗ hổng từ xa (Mục 2.8.3)** | Loại bỏ giả định 3 trạng thái đầy đủ; loại bỏ từ `SAFE` làm kết quả canonical | Chỉ gồm `VULNERABLE` (kết quả tường minh) và `UNKNOWN / NO USABLE SCRIPT RESULT` | FIXED |
| **Kiểm tra từ khóa `SAFE`** | Quét regex `\bSAFE\b` như phán quyết canonical | 0 phát hiện | NO REMAINING MATCH FOUND |
| **Loại bỏ cam kết restore thực nghiệm ở 2.1.3** | Rà soát Mục 2.1.3: bỏ claim "hoàn nguyên thực tế được ghi nhận tại Chương 3" | `Before Demo` chỉ xác định làm mốc thiết kế chuẩn để phục hồi baseline | FIXED |
| **Chuẩn hóa baseline Windows Server (Mục 2.3.2)** | Loại bỏ "ở trạng thái mặc định" và giả định "để tương thích" | Diễn đạt chuẩn xác theo baseline canonical thực tế của máy lab | FIXED |

### 7.4. Kết quả thực thi 6 Micro-Fixes cuối cùng trước CP5-TECH

Bảng đối soát 6 micro-issues còn lại trước khi External Reviewer khóa CP5-TECH:

| STT | Micro-Issue | Vị trí can thiệp | Nội dung xử lý | Trạng thái |
|:---:|---|---|---|:---:|
| 1 | Lỗi ngữ pháp câu | Mục 2.5.5 | Viết lại câu chuẩn xác: *'Nmap sử dụng kỹ thuật dò phiên bản (`-sV`) để phân tích chuỗi định danh dịch vụ trên TCP 139 và 445 theo cơ sở dữ liệu nhận diện của công cụ.'*, không thêm kết quả thực nghiệm. | FIXED |
| 2 | Phạm vi snapshot Before Demo | Mục 2.1.3 & 2.3.6 | Xác nhận snapshot `Before Demo` tồn tại trên cả Kali Linux và Windows Server (ENV-CORE-02); chỉ rõ Windows Server là máy chịu thay đổi cấu hình chính ở Case B; snapshot đóng vai trò mốc và phương án phục hồi baseline sạch, không suy diễn restore thực tế khi chưa có artifact. | FIXED |
| 3 | Tập NSE script canonical | Mục 2.3.5 | Loại bỏ hoàn toàn `smb-security-mode.nse`; phản ánh đúng hai tập canonical: Scenario 1 (`smb-protocols`, `smb-os-discovery`, `smb2-security-mode`, `smb2-capabilities`) và Scenario 2 (`smb-protocols`, `smb2-security-mode`, `smb-vuln-ms17-010`). | FIXED |
| 4 | Bảng 2.3 thiếu hàng Safe SMB NSE | Bảng 2.3 | Bổ sung hàng đại diện cho bước *'Kịch bản 1 — Safe SMB NSE'*, liệt kê 4 script an toàn (`smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities`), mục tiêu khảo sát dialect, OS discovery, signing, SMB2 capabilities; không wildcard, không suy diễn MS17-010. | FIXED |
| 5 | Bảng 2.4 (Mặc định OS & Case A) | Bảng 2.4 | Loại bỏ chuỗi `'Mặc định OS'`, thay bằng `'Cấu hình baseline canonical của Windows Server, LanmanServer và TCP 139/445'`; chuẩn hóa Case A là `'Bản cập nhật MS17-010 áp dụng cho Windows Server 2012 R2 (KB4012213 / KB4012216, srv.sys >= .18604)'`, giữ nguyên nhãn `THEORETICAL_REFERENCE_ONLY`, không biến thành experiment đã chạy. | FIXED |
| 6 | Reachability 2.8.1 | Mục 2.8.1 | Loại bỏ cụm từ `'Tỷ lệ mất gói bằng không khẳng định kết nối thông suốt'`; diễn đạt chuẩn xác: phản hồi ICMP Echo xác nhận hai máy tiếp cận nhau ở tầng mạng tại thời điểm kiểm tra, đây là precondition, không thay thế cho TCP scan hay xác minh dịch vụ/giao thức. | FIXED |

---

## 8. Các vấn đề và nhãn còn mở (Open Labels)

1. **`ISS-01` (`[CẦN DỮ LIỆU]`):** Thu hẹp vào phần dữ liệu nhật ký thô và hình ảnh thực chứng chi tiết của Chương 3 (sẽ được tích hợp và giải quyết tại nhiệm vụ X6).
2. **`Case A Patch`:** Tiếp tục duy trì nhãn `THEORETICAL_BASELINE_ONLY` trong phạm vi nghiên cứu, không suy diễn khi chưa có canonical raw log.
3. **Quyền quyết định cuối cùng:** Bản thảo được hoàn thiện ở trạng thái `AUTHOR_VOICE_REVIEW_COMPLETED` và `X5_DRAFT_READY_FOR_EXTERNAL_REVIEW`, sẵn sàng để hội đồng thẩm định độc lập đánh giá trực tiếp từ remote repository.
