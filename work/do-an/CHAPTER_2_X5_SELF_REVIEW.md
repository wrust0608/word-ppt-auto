# BÁO CÁO TỰ ĐÁNH GIÁ CHƯƠNG 2 THEO PHONG CÁCH DEMO / THỰC NGHIỆM
## (X5 DEMO-STYLE SELF-REVIEW R3)

**Thời điểm thực hiện:** 2026-10-05
**Vai trò thực hiện:** Executor / Writing Agent
**Tài liệu đánh giá:** `work/do-an/CHAPTER_2.md`
**Tài liệu nghiên cứu tham chiếu:** `work/do-an/X5_DEMO_STYLE_REFERENCE_REVIEW.md`
**Nhánh làm việc:** `feature/x5-chapter-2-demo-style`
**Căn cứ chỉ đạo:** `CHANGE_REQUEST_CR-2026-10-05-X5-DEMO-STYLE.md` và `X5_DEMO_STYLE_EXTERNAL_REVIEW_R2.md`
**Trạng thái đề xuất:** `X5_DEMO_STYLE_R3_READY_FOR_FINAL_EXTERNAL_REVIEW`

---

## 1. Tổng quan cấu trúc và dung lượng

- **Tiêu đề chương:** `# CHƯƠNG 2. XÂY DỰNG MÔ HÌNH THỰC NGHIỆM VÀ KỊCH BẢN DEMO`
- **Số lượng phân mục:** Khóa cố định **7 H2** và **20 H3** (100% khớp đề cương, không thay đổi cấu trúc).
- **Dung lượng từ:** **3.679 từ** (nằm trọn vẹn trong khoảng ngân sách yêu cầu **3.200 – 3.800 từ**).
- **Kiến trúc trực quan:**
  - 02 sơ đồ trực quan Mermaid: Hình 2.1 (Sơ đồ topo mạng lab VirtualBox) và Hình 2.2 (Lưu đồ 6 bước thực thi Demo 1).
  - 02 bảng tổng hợp tinh gọn: Bảng 2.1 (Thông số kỹ thuật các máy trạm trong môi trường thử nghiệm) và Bảng 2.2 (Ma trận kiểm tra vi sai trước và sau can thiệp).
  - Khối lệnh bash và PowerShell tường minh, có chú giải tham số và ranh giới an toàn.
- **Hệ thống trích dẫn:** Trích dẫn chuẩn IEEE với 11 nguồn tài liệu tham khảo (`[1]` đến `[11]`), xuất hiện tuần tự từ 1 đến 11 trong văn bản. Không đặt phân mục `# TÀI LIỆU THAM KHẢO` riêng trong file `CHAPTER_2.md` (quản lý ở tài liệu tổng hợp đồ án).

---

## 2. Ma trận khắc phục các phát hiện từ External Review R2 (R2 Issue Closure Matrix)

| STT | Vấn đề từ External Review R2 | Giải pháp khắc phục trong R3 | Trạng thái |
|:---:|---|---|:---:|
| 1 | **Blocker A — Windows baseline vượt evidence:** Cụm từ "RTM nguyên bản", "Tái hiện máy chưa vá", "không cài đặt bất kỳ gói rollup nào" suy rộng quá mức. | Bỏ hoàn toàn "RTM", "nguyên bản", "rollup" và "Tái hiện máy chưa vá". Bảng 2.1 ghi "Phiên bản hệ điều hành của máy mục tiêu". Mục 2.2.3 và 2.2.5 chỉ nêu: Windows Server 2012 R2 Standard Evaluation Build 9600, không ghi nhận KB4012213, KB4012216 hoặc superseding update tương ứng, trạng thái bản vá nội bộ là UNPATCHED. | **CLOSED** |
| 2 | **Blocker B — UNKNOWN gán nguyên nhân:** Mục 2.6.2 viết "UNKNOWN ... do cơ chế phản hồi hoặc điều kiện mạng". | Đổi thành: "Khi script không cung cấp verdict usable, kết quả được ghi nhận `UNKNOWN / NO USABLE SCRIPT RESULT` và không được suy diễn thành `SAFE`." Loại bỏ toàn bộ suy đoán nguyên nhân khi raw log không có. | **CLOSED** |
| 3 | **Blocker C — FILTERED gán nguyên nhân tường lửa tổng quát:** Mục 2.6.2 viết "FILTERED ... do tường lửa chặn gói". | Đổi thành: "`FILTERED` cho biết Nmap không nhận đủ phản hồi để phân loại cổng là open hay closed; trạng thái này không chứng minh máy chủ đã được vá." Quy attribution tường lửa được bảo lưu riêng cho Case C ở Chương 3 qua log pfSense. | **CLOSED** |
| 4 | **Blocker D — smb-vuln-ms17-010 wording quá quyết đoán:** Mục 2.4.2 viết máy chưa vá tất yếu phản hồi `STATUS_INSUFF_SERVER_RESOURCES`. | Đổi thành: "Script sử dụng `STATUS_INSUFF_SERVER_RESOURCES` như một dấu hiệu để nhận diện hệ thống có khả năng bị ảnh hưởng bởi MS17-010." Giữ chuẩn cơ chế: pipe IPC$, transaction trên FID 0, status-code analysis. | **CLOSED** |
| 5 | **Minor E — Thuật ngữ nội bộ còn sót:** "canonical" ở 2.3.2 và "Local Ground Truth" ở 2.4.3. | Đổi "canonical" thành "theo kịch bản đã xây dựng"; đổi "Local Ground Truth" thành "Trạng thái bản vá nội bộ". Cả hai từ quản trị repo đều có số lần xuất hiện = 0. | **CLOSED** |
| 6 | **Minor F — Windows Firewall wording quá rộng:** "ngăn chặn truy cập ngoài phạm vi kiểm thử". | Đổi thành: "Windows Firewall bật (`Enabled`), giữ rule cho phép TCP 139 và TCP 445 từ địa chỉ `192.168.56.10` phục vụ lab; nhóm File and Printer Sharing mặc định không được mở toàn bộ." | **CLOSED** |
| 7 | **Minor G — Case B suy diễn kiểm thử workload:** "nhằm vô hiệu hóa SMBv1 và duy trì chia sẻ tệp qua SMBv2/SMBv3". | Đổi thành: "nhằm vô hiệu hóa SMBv1 và giữ SMB2/SMB3 là các phiên bản giao thức còn được phép thương lượng." | **CLOSED** |
| 8 | **Research Artifact — Thiếu handle hoặc URL chung chung:** TL02 handle trống; TL05/TL06 dùng URL thư mục Scribd/Studocu chung. | Cập nhật exact handle cho TL02 (`HVCNBCVT/5000`) và TL03 (`HVCNBCVT/4983`). Hạ TL04, TL05, TL06, TL07 xuống `UNVERIFIED` và loại bỏ hoàn toàn khỏi căn cứ rút ra quy tắc trình bày. | **CLOSED** |
| 9 | **Presentation pattern rút ra vượt quá metadata:** Mạo nhận quan sát screenshot/code-block/topology từ tài liệu chỉ xem được metadata. | Rút gọn kết luận từ metadata PTIT chỉ gồm: cấu trúc 3 chương (Lý thuyết $\rightarrow$ Xây dựng lab $\rightarrow$ Thử nghiệm/Đánh giá) và nguyên tắc tách bạch giữa thiết kế kịch bản và kết quả đo đạc. Các chuẩn mực kỹ thuật khác được ghi nhận là yêu cầu kỹ thuật nội bộ của đề tài. | **CLOSED** |
| 10 | **Safety / polish wording:** Host-Only safety, non-disruptive scope, SMB dialect scope, `-oA` wording. | Đã hiệu chỉnh: "giới hạn đường kết nối của hai máy ảo trong mạng Host-Only theo cấu hình lab", "không thực hiện thao tác có chủ đích gây gián đoạn máy mục tiêu", "xác định các dialect SMB được hỗ trợ", "Các lệnh Nmap trong kịch bản được lưu bằng tham số -oA". | **CLOSED** |

---

## 3. Danh mục nguồn nghiên cứu tham khảo sau khi làm sạch (Research Source Table)

Chi tiết thể hiện tại `work/do-an/X5_DEMO_STYLE_REFERENCE_REVIEW.md`:

| ID | Đơn vị | Tên tài liệu / Đề tài | URL / Handle | Năm | Access level | Nội dung thực sự đọc được |
|:---:|---|---|---|:---:|:---:|---|
| **TL01** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Nghiên cứu và xây dựng các bài thực hành về kỹ thuật phân tích gói tin sử dụng công cụ tcpdump* (Tác giả: Cao Vũ Tùng Lâm, Đỗ Thành Luân; GVHD: ThS. Vũ Minh Mạnh) | `https://dlib.ptit.edu.vn/handle/HVCNBCVT/15481` | 2025 | `METADATA_ONLY` | Tiêu đề, tác giả, năm, tóm tắt đề tài về xây dựng bài thực hành trên nền tảng Labtainer, phân tích gói tin mạng; cấu trúc 3 chương cơ bản (Cơ sở lý thuyết $\rightarrow$ Xây dựng bài thực hành $\rightarrow$ Thử nghiệm và đánh giá). File PDF toàn văn bị hạn chế truy cập. |
| **TL02** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Nghiên cứu triển khai hệ thống giám sát an ninh mạng và điều tra, ứng phó sự cố tập trung sử dụng SPLUNK và SYSMON* (Tác giả: Nguyễn Hoa Cương, Nguyễn Hà Thanh) | `https://dlib.ptit.edu.vn/handle/HVCNBCVT/5000` | 2025 | `METADATA_ONLY` | Metadata đề tài, tác giả, năm; tóm tắt mô hình giám sát an ninh tập trung; phân định phạm vi triển khai cấu hình thu thập log tách biệt với kịch bản thử nghiệm đánh giá sự cố. File PDF toàn văn bị hạn chế truy cập. |
| **TL03** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Nghiên cứu triển khai hệ thống giám sát an ninh cho doanh nghiệp vừa và nhỏ sử dụng Splunk* (Tác giả: Vũ Thu Trang; GVHD: TS. Đinh Trường Duy) | `https://dlib.ptit.edu.vn/handle/HVCNBCVT/4983` | 2024 | `METADATA_ONLY` | Metadata đề tài, tác giả, giảng viên hướng dẫn, tóm tắt phạm vi triển khai máy chủ giám sát, phân nhóm cảm biến thu thập sự kiện; cấu trúc tách biệt giữa phần xây dựng hệ thống và phần thử nghiệm giám sát tấn công. File PDF toàn văn bị hạn chế truy cập. |
| **TL04** | Trường Đại học Công nghệ Thông tin – ĐHQG TP.HCM (UIT) | *Tài liệu hướng dẫn thực hành An toàn mạng máy tính: Lab Quét mạng và Thăm dò lỗ hổng với Nmap* | `https://www.studocu.vn/vn/document/...` | 2024 | `UNVERIFIED` | Liên kết thuộc danh mục lưu trữ tài liệu chung, không có URL trực tiếp tới tài liệu cụ thể có tác giả và năm xác thực mở. **Loại bỏ hoàn toàn khỏi căn cứ rút ra quy tắc trình bày.** |
| **TL05** | Nền tảng chia sẻ học thuật kỹ thuật (Tài liệu chuyên đề ATTT) | *Báo cáo thực hành triển khai tường lửa pfSense và kiểm soát lưu lượng mạng nội bộ* | `https://www.scribd.com/document/` | 2024 | `UNVERIFIED` | Liên kết Scribd thư mục chung, không có mã định danh tài liệu cụ thể để truy vết độc lập. **Loại bỏ hoàn toàn khỏi căn cứ rút ra quy tắc trình bày.** |
| **TL06** | Đại học Công Thương TP.HCM (HUIT) | *Đề tài tường lửa và giải pháp phòng thủ mạng doanh nghiệp* | Không có handle công khai trực tiếp | 2024 | `UNVERIFIED` | Nguồn tham khảo từ danh mục đề tài lưu hành nội bộ, không có URL/handle công khai để xác thực. **Loại bỏ hoàn toàn khỏi căn cứ rút ra quy tắc trình bày.** |
| **TL07** | Học viện Kỹ thuật Mật mã (ACTVN) | *Chuyên đề thực nghiệm hệ thống giám sát an toàn mạng* | Không có handle công khai trực tiếp | 2024 | `UNVERIFIED` | Tài liệu tham khảo lưu hành nội bộ, không có liên kết trực tuyến mở. **Loại bỏ hoàn toàn khỏi căn cứ rút ra quy tắc trình bày.** |

---

## 4. Bảng kiểm tra tính chân lý kỹ thuật từng khẳng định (Technical Claim Audit)

| Claim kỹ thuật | Nguồn đối chiếu (Repo/Baseline) | Kết quả | Ghi chú kiểm định chi tiết |
|---|---|:---:|---|
| **Demo 1 Flow:** Đủ 6 bước chuẩn hóa (B1: IP/route $\rightarrow$ B2: Quét subnet $\rightarrow$ B3: Kiểm tra target $\rightarrow$ B4: Quét SYN 139/445 $\rightarrow$ B5: Quét version $\rightarrow$ B6: Safe NSE). Dừng lại ở `-oA`, không khai thác. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M01), Lecturer Scenario | **PASS** | Thể hiện trọn vẹn tại Mục 2.3.2 và Lưu đồ Hình 2.2; không dùng ping thay thế Nmap discovery; ranh giới an ninh `445 open != vulnerable`. |
| **Demo 2 Command & Mechanism:** `nmap -p445 --script smb-vuln-ms17-010 -Pn -oA <name> 192.168.56.20`, không có `unsafe=0`. Không gắn deterministically trạng thái máy chưa vá với phản hồi. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M02), Nmap NSEDoc | **PASS** | Không sử dụng `unsafe=0`. Mô tả chuẩn: pipe IPC$, transaction trên FID 0, sử dụng `STATUS_INSUFF_SERVER_RESOURCES` như một dấu hiệu nhận diện hệ thống có khả năng bị ảnh hưởng. |
| **Demo 2 Boundary & Negative Policy:** Kết quả không khả dụng là `UNKNOWN / NO USABLE SCRIPT RESULT`; `UNKNOWN != SAFE`. Không tự gán nguyên nhân cơ chế phản hồi/mạng. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M02), `NEGATIVE_RESULT_POLICY.md` | **PASS** | Loại bỏ hoàn toàn giải thích nguyên nhân không có trong evidence. Không dùng confusion matrix. |
| **Mitigation Table:** Bảng 2.2 dùng cột "Nội dung cần kiểm tra lại", không dùng "Kết quả kỳ vọng". | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M03) | **PASS** | Liệt kê nội dung kiểm tra lại cho Baseline, Case B, Case C và Case A là `REFERENCE ONLY / NOT MEASURED`. Không khẳng định trước kết quả thực nghiệm. |
| **Case B Action & Retest:** Chỉ dùng `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`, không có lệnh khởi động lại. Retest bằng `smb-protocols` và `smb-vuln-ms17-010`. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M03), Evidence Register | **PASS** | Lệnh duy nhất được đưa vào là `Set-SmbServerConfiguration`. Ranh giới: `SMBv1 disabled != PATCHED`. Không suy diễn kiểm thử workload chia sẻ tệp. |
| **Case C Firewall Version & Rule:** pfSense CE 2.9.0. Rule chặn nguồn `192.168.56.10` tới đích `192.168.56.20`, cổng TCP 139, 445, bật logging. Đủ 3 tunable `pfil`. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M03) | **PASS** | Đúng phiên bản CE 2.9.0. Đủ chính sách lọc có hướng và 3 tunable nhân. FILTERED được giải thích theo chuẩn Nmap, không gán nguyên nhân tổng quát cho firewall rule trong nguyên tắc chung. |
| **Case A Representation:** Rút ngắn còn 1 đoạn; là giải pháp đối chứng lý thuyết (`REFERENCE ONLY / NOT MEASURED`); mốc cập nhật `srv.sys = 6.3.9600.18604` là phiên bản tối thiểu. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M03), `NEGATIVE_RESULT_POLICY.md` | **PASS** | Trình bày súc tích trong 1 đoạn tại Mục 2.5.4. Không khẳng định lab đã cập nhật bản vá. |
| **Windows Patch Baseline:** Windows Server 2012 R2 Standard Evaluation Build 9600; không ghi nhận KB4012213/KB4012216; trạng thái bản vá nội bộ UNPATCHED. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M01), Evidence Register | **PASS** | Không dùng "RTM nguyên bản", không suy rộng sang toàn bộ lịch sử rollup của máy. Bảng 2.1 ghi "Phiên bản hệ điều hành của máy mục tiêu". |
| **Snapshot Wording:** Snapshot Before Demo là mốc phục hồi phương pháp luận khi cần đưa lab về baseline trước khi đổi biến can thiệp. | `EXPERIMENTAL_TRUTH_MATRIX.md`, Lecturer Scenario | **PASS** | Mô tả đúng vai trò kiểm soát biến phương pháp luận; không khẳng định sau mỗi ca đều đã restore snapshot trên thực tế. |
| **Data Collection Scope:** Chỉ thu thập Nmap raw (`.nmap`, `.xml`, `.gnmap`), screenshot terminal/VirtualBox, cấu hình Windows và log pfSense. | `EVIDENCE_REGISTER.md`, Review Directive | **PASS** | Không chứa `tcpdump`, `tshark`, `.pcap`, `Event Viewer`, timestamp screenshot requirement. |

---

## 5. Kết quả kiểm tra Search Gate và QA Suite

### 5.1. Kết quả Search Gate (15 chỉ tiêu cấm)
- `RTM nguyên bản`: **0 lần** (Đạt)
- `không cài đặt bất kỳ gói rollup nào`: **0 lần** (Đạt)
- `canonical` trong CHAPTER_2.md: **0 lần** (Đạt)
- `Local Ground Truth`: **0 lần** (Đạt)
- `UNKNOWN` + giải thích nguyên nhân ("do cơ chế phản hồi hoặc điều kiện mạng"): **0 lần** (Đạt)
- `FILTERED` + quy attribution chung cho tường lửa ("do tường lửa chặn gói"): **0 lần** (Đạt)
- `ngăn chặn truy cập ngoài phạm vi kiểm thử`: **0 lần** (Đạt)
- `duy trì chia sẻ tệp qua SMBv2/SMBv3`: **0 lần** (Đạt)
- `unsafe=0`: **0 lần** (Đạt)
- `pfSense 2.7.2`: **0 lần** (Đạt)
- `Restart-Computer -Force`: **0 lần** (Đạt)
- `tcpdump`: **0 lần** (Đạt)
- `tshark`: **0 lần** (Đạt)
- `.pcap`: **0 lần** (Đạt)
- `Event Viewer`: **0 lần** (Đạt)
- `# TÀI LIỆU THAM KHẢO` trong `CHAPTER_2.md`: **0 lần** (Đạt)
- `cách ly hoàn toàn`: **0 lần** (Đạt)
- `RTM` (toàn văn): **0 lần** (Đạt)

### 5.2. Kết quả kiểm tra QA Suite
1. **Linter học thuật tiếng Việt:**
   ```powershell
   uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_2.md
   ```
   *Kết quả:* **Không phát hiện mẫu văn phong cần xem xét (error=0, warning=0, info=0)**.

2. **Kiểm tra trích dẫn khoa học IEEE:**
   ```powershell
   uv run python scripts/audit_ieee_citations.py work/do-an/CHAPTER_2.md
   ```
   *Kết quả:* **11 trích dẫn IEEE hợp lệ, xuất hiện tuần tự 1..11, không nhảy cóc hay mồ côi**.

3. **Kiểm tra tính toàn vẹn dự án và bộ kiểm thử:**
   ```powershell
   uv run python scripts/validate_project.py
   uv run python -m unittest discover -s tests -p "test_*.py"
   ```
   *Kết quả:* **Project validation passed, 7/7 tests passed**.

4. **Kiểm tra định dạng git:**
   ```powershell
   git diff --check
   ```
   *Kết quả:* **Mã thoát 0, không có lỗi khoảng trắng thừa (trailing whitespace) hay lỗi định dạng**.

---

## 6. Kết luận

Bản thảo Chương 2 phiên bản R3 đã hoàn thành toàn bộ các micro-patch cuối cùng theo đúng yêu cầu của External Review R2:
- Khóa cố định cấu trúc 7 H2 / 20 H3 và dung lượng 3.679 từ.
- Làm sạch hoàn toàn các suy diễn vượt evidence về baseline Windows, cơ chế script NSE, nguyên tắc UNKNOWN/FILTERED và cấu hình Firewall.
- Loại bỏ toàn bộ thuật ngữ nội bộ repository khỏi văn bản chính.
- Chuẩn hóa và minh bạch hóa danh mục nghiên cứu tham khảo, loại bỏ toàn bộ các nguồn không xác thực được liên kết cụ thể.

Trạng thái sẵn sàng: **`X5_DEMO_STYLE_R3_READY_FOR_FINAL_EXTERNAL_REVIEW`**.
