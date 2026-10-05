# BÁO CÁO TỰ ĐÁNH GIÁ CHƯƠNG 2 THEO PHONG CÁCH DEMO / THỰC NGHIỆM
## (X5 DEMO-STYLE SELF-REVIEW R2)

**Thời điểm thực hiện:** 2026-10-05
**Vai trò thực hiện:** Executor / Writing Agent
**Tài liệu đánh giá:** `work/do-an/CHAPTER_2.md`
**Tài liệu nghiên cứu tham chiếu:** `work/do-an/X5_DEMO_STYLE_REFERENCE_REVIEW.md`
**Nhánh làm việc:** `feature/x5-chapter-2-demo-style`
**Căn cứ chỉ đạo:** `CHANGE_REQUEST_CR-2026-10-05-X5-DEMO-STYLE.md` và `X5_DEMO_STYLE_EXTERNAL_REVIEW_R1.md`
**Trạng thái đề xuất:** `X5_DEMO_STYLE_R2_READY_FOR_EXTERNAL_REVIEW`

---

## 1. Tổng quan cấu trúc và dung lượng

- **Tiêu đề chương:** `# CHƯƠNG 2. XÂY DỰNG MÔ HÌNH THỰC NGHIỆM VÀ KỊCH BẢN DEMO`
- **Số lượng phân mục:** Giữ nguyên chính xác **7 H2** và **20 H3** (100% đúng cấu trúc quy định, không thêm bớt phân mục).
- **Dung lượng từ:** **3.637 từ** (nằm trọn vẹn trong khoảng ngân sách yêu cầu **3.200 – 3.800 từ**, ngắn gọn hơn R1, loại bỏ triệt để các nội dung thừa).
- **Kiến trúc trực quan:**
  - 02 sơ đồ trực quan Mermaid: Hình 2.1 (Sơ đồ topo mạng lab VirtualBox) và Hình 2.2 (Lưu đồ 6 bước thực thi Demo 1).
  - 02 bảng tổng hợp tinh gọn: Bảng 2.1 (Thông số kỹ thuật các máy trạm trong môi trường thử nghiệm) và Bảng 2.2 (Ma trận kiểm tra vi sai trước và sau can thiệp).
  - Khối lệnh bash và PowerShell tường minh, có chú giải tham số và ranh giới an toàn.
- **Hệ thống trích dẫn:** Trích dẫn chuẩn IEEE với 11 nguồn tài liệu tham khảo (`[1]` đến `[11]`), xuất hiện tuần tự từ 1 đến 11 trong văn bản. Không đặt phân mục `# TÀI LIỆU THAM KHẢO` riêng trong file `CHAPTER_2.md` theo đúng quy định phân cấp tài liệu tổng hợp của đồ án.

---

## 2. Đối chiếu quy tắc nghiên cứu tham khảo (Reference-Pattern Compliance)

Dưới đây là phần trả lời 6 câu hỏi bắt buộc dựa trên báo cáo nghiên cứu tham khảo đã được hiệu chỉnh minh bạch về mức độ truy cập (`X5_DEMO_STYLE_REFERENCE_REVIEW.md`):

### 2.1. Chương 2 đã áp dụng pattern nào từ research?
1. **Sơ đồ topo trước, bảng cấu hình chi tiết sau:** Mở đầu Mục 2.1 bằng Sơ đồ topo mạng (Hình 2.1) trước khi trình bày bảng thông số, giúp người đọc nắm bắt tổng thể cấu trúc kết nối trước khi xem chi tiết.
2. **Quy tụ toàn bộ thông số môi trường vào 1 bảng duy nhất:** Bảng 2.1 tổng hợp đầy đủ phần cứng, hệ điều hành, bản dựng, địa chỉ IP, card mạng, cổng và dịch vụ lắng nghe, tránh phân mảnh thông tin rải rác.
3. **Cấu trúc demo 4 phần chuẩn mực:** Cả Demo 1 và Demo 2 đều được tổ chức theo luồng: *Mục tiêu & phạm vi $\rightarrow$ Điều kiện ban đầu $\rightarrow$ Quy trình từng bước & Câu lệnh $\rightarrow$ Nội dung quan sát & Ranh giới an ninh*.
4. **Tách biệt tuyệt đối quy trình và kết quả (Separation of Procedure and Results):** Toàn bộ số liệu quét thực tế, bảng chi tiết kết quả NSE, ảnh chụp màn hình terminal và đánh giá chuyên sâu được bảo lưu hoàn toàn cho Chương 3. Chương 2 chỉ tập trung mô tả phương pháp, kịch bản, câu lệnh và điều kiện quan sát.
5. **Khối lệnh có định dạng rõ ràng kèm chú thích cờ lệnh:** Mọi câu lệnh Nmap và PowerShell đều được đóng khung code block và diễn giải mục đích từng tham số (`-sn`, `-sS`, `-sV`, `-Pn`, `--reason`, `--script`, `-oA`).

### 2.2. Pattern nào chủ động không dùng?
1. **Chụp ảnh từng thao tác cài đặt (Next-Click Screenshotting):** Không đưa vào ảnh chụp cài đặt VirtualBox hay Windows. Toàn bộ cấu hình được mô tả qua tham số mạng và lệnh PowerShell tự động hóa.
2. **Lạm dụng heading phân mảnh (Heading Spam):** Không chia nhỏ mục thành H4/H5. Cấu trúc được khóa ở 7 H2 và 20 H3 với độ dài đồng đều và tập trung.
3. **Chép lại lý thuyết nền tảng:** Không trình bày lại cơ chế hoạt động chi tiết của giao thức SMB hay mã khai thác EternalBlue trong chương mô tả thực nghiệm.
4. **Bảng biểu lặp lại văn bản:** Bảng 2.1 và Bảng 2.2 đóng vai trò bảng tổng hợp tra cứu nhanh, không sao chép nguyên văn các đoạn văn xuôi.
5. **Tuyệt đối không lấy công cụ, log và thao tác ngoài evidence:** Không đưa `tcpdump`, `tshark`, file `.pcap`, `Event Viewer` từ các đồ án tham khảo bên ngoài vào đề tài hiện tại vì không có trong bộ evidence được phê duyệt.

### 2.3. Có đoạn nào vẫn giống leader/QA report không?
- **Không.** Toàn bộ từ ngữ mang tính quản trị nội bộ hoặc biên bản kiểm duyệt (như "Canonical baseline", "Truth matrix", "Gate", "DEC-xx", "CP5-TECH", "Evidence ID", mô hình 5 lớp bằng chứng) đã bị loại bỏ 100%.
- Văn bản thể hiện văn phong học thuật kỹ thuật của đồ án sinh viên: khách quan, trực diện, mạch lạc và tập trung vào thao tác thực hành an toàn mạng.

### 2.4. Có đoạn nào còn quá trừu tượng không?
- **Không.** Mọi bước thực hiện đều gắn liền với tham số kỹ thuật thực tế:
  - Địa chỉ IP cụ thể: `192.168.56.10/24`, `192.168.56.20/24`, gateway ảo `192.168.56.1/24`.
  - Cổng mạng và dịch vụ: TCP 139, TCP 445, dịch vụ `LanmanServer`.
  - Phiên bản tệp thực thi: `srv.sys` phiên bản `6.3.9600.16421` (so với mốc cập nhật tối thiểu `6.3.9600.18604`).
  - Câu lệnh Nmap và PowerShell đầy đủ tham số có thể chạy lại trực tiếp trong phòng thí nghiệm.

### 2.5. Người đọc có thể làm theo Demo 1 và Demo 2 không?
- **Hoàn toàn làm theo được.** Người đọc chỉ cần thiết lập VirtualBox Host-Only theo Bảng 2.1, cấu hình IP tĩnh và dịch vụ theo Mục 2.2, sau đó thực thi tuần tự 6 bước trong Mục 2.3.2 (Demo 1) và kịch bản chuẩn trong Mục 2.4.2 (Demo 2) là có thể tái hiện chính xác môi trường và thu được các tệp kết quả thô `-oA`.

### 2.6. Có phần nào có thể cắt mà không mất thông tin không?
- Bản thảo R2 đã được tinh gọn từ 3.863 từ (R1) xuống 3.637 từ. Toàn bộ các đoạn diễn giải lan man, giải thích thừa thãi về cơ chế nhánh bộ nhớ không sử dụng, hoặc các bảng lặp dữ liệu đã được cắt giảm. Mọi câu văn hiện hành đều chứa đựng dữ liệu kỹ thuật và ranh giới an toàn cần thiết.

---

## 3. Bảng kiểm tra tính chân lý kỹ thuật từng khẳng định (Technical Claim Audit)

Bảng dưới đây kiểm tra chi tiết từng khẳng định kỹ thuật trong văn bản Chương 2 đối chiếu với Truth Matrix và baseline đã được phê duyệt:

| Claim kỹ thuật | Nguồn đối chiếu (Repo/Baseline) | Kết quả | Ghi chú kiểm định chi tiết |
|---|---|:---:|---|
| **Demo 1 Flow:** Đủ 6 bước chuẩn hóa (B1: IP/route $\rightarrow$ B2: Quét subnet $\rightarrow$ B3: Kiểm tra target $\rightarrow$ B4: Quét SYN 139/445 $\rightarrow$ B5: Quét version $\rightarrow$ B6: Safe NSE). Dừng lại ở `-oA`, không khai thác. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M01), Lecturer Scenario | **PASS** | Phục hồi trọn vẹn 6 bước canonical tại Mục 2.3.2 và Lưu đồ Hình 2.2; không dùng ping thay thế Nmap discovery; nêu rõ nguyên tắc `445 open != vulnerable`. |
| **Demo 2 Command:** `nmap -p445 --script smb-vuln-ms17-010 -Pn -oA <name> 192.168.56.20`, không có `unsafe=0`. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M02), Nmap NSEDoc | **PASS** | Loại bỏ hoàn toàn `--script-args unsafe=0` (0 lần xuất hiện). Không mô tả cơ chế nhánh khai thác bộ nhớ. Mô tả đúng cơ chế chính thức: kết nối pipe IPC$, gửi transaction trên FID 0, phân tích mã trạng thái trả về. |
| **Demo 2 Status Code & Boundary:** Chỉ nhắc `STATUS_INSUFF_SERVER_RESOURCES`; kết quả không khả dụng là `UNKNOWN / NO USABLE SCRIPT RESULT`; `UNKNOWN != SAFE`. Không dùng confusion matrix. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M02), `NEGATIVE_RESULT_POLICY.md` | **PASS** | Loại bỏ `STATUS_INVALID_HANDLE` không cần thiết. Loại bỏ toàn bộ ma trận nhầm lẫn (`True Positive`, `True Negative`, `False Positive`, `Sai lệch cảnh báo` = 0). Xác định chuẩn ranh giới an ninh. |
| **Mitigation Table:** Bảng 2.2 dùng cột "Nội dung cần kiểm tra lại", không dùng "Kết quả kỳ vọng". | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M03) | **PASS** | Bảng 2.2 liệt kê nội dung kiểm tra lại cho Baseline, Case B, Case C và ghi chú Case A là `REFERENCE ONLY / NOT MEASURED`. Không khẳng định trước kết quả thực nghiệm. |
| **Case B Action:** Chỉ dùng `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`, không có lệnh khởi động lại. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M03), PowerShell Docs | **PASS** | Lệnh duy nhất được đưa vào là `Set-SmbServerConfiguration` (Mục 2.5.2). `Restart-Computer -Force` xuất hiện 0 lần. |
| **Case B Retest & Boundary:** Kiểm tra lại bằng `smb-protocols` và `smb-vuln-ms17-010`. Ranh giới: `SMBv1 disabled != PATCHED`. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M03), Evidence Register | **PASS** | Retest đúng 2 phép kiểm có evidence thực tế. Khẳng định rõ việc tắt SMBv1 làm giảm bề mặt tấn công nhưng không làm thay đổi trạng thái bản vá của hệ điều hành. |
| **Case C Firewall Version:** pfSense CE 2.9.0. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M03), Evidence Register | **PASS** | Ghi nhận chính xác `pfSense CE 2.9.0` tại Mục 2.1, Bảng 2.1 và Mục 2.5.3. Phiên bản cũ `pfSense 2.7.2` xuất hiện 0 lần. |
| **Case C Rule & Tunables:** Rule chặn nguồn `192.168.56.10` tới đích `192.168.56.20`, cổng TCP 139, 445, bật logging. Đủ 3 tham số nhân `pfil`. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M03) | **PASS** | Mô tả đầy đủ chính sách lọc mạng có hướng và có ghi log. Giữ nguyên 3 tunable `net.link.bridge.pfil_member = 1`, `pfil_bridge = 0`, `pfil_onlyip = 1`. |
| **Case C Result Leakage Prevention:** Không viết "cổng chuyển sang filtered" như kết quả đã diễn ra. Ranh giới: `FILTERED != PATCHED`. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M03), Chapter 2 Scope | **PASS** | Văn bản viết: "Sau khi áp dụng luật, quét lại TCP 139/445 từ Kali Linux để kiểm tra sự thay đổi khả năng tiếp cận dịch vụ qua tường lửa." Kết quả cụ thể dành cho Chương 3. |
| **Case A Representation:** Rút ngắn còn 1 đoạn; là giải pháp lý thuyết tham chiếu (`REFERENCE ONLY / NOT MEASURED`); mốc cập nhật `srv.sys = 6.3.9600.18604` là phiên bản tối thiểu, không gọi là ngưỡng an toàn tuyệt đối. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M03), `NEGATIVE_RESULT_POLICY.md` | **PASS** | Trình bày súc tích trong 1 đoạn tại Mục 2.5.4. Không khẳng định lab đã cập nhật bản vá. Sử dụng cụm từ "ngưỡng phiên bản driver đã cập nhật". |
| **Patch Baseline:** Hệ thống ở trạng thái `UNPATCHED`; `srv.sys` đạt `6.3.9600.16421`; vắng mặt KB4012213/KB4012216. | `EXPERIMENTAL_TRUTH_MATRIX.md` (TRUTH-M01), Evidence Register | **PASS** | Thể hiện nhất quán tại Bảng 2.1, Mục 2.2.3 và Mục 2.4.1. |
| **Snapshot Wording:** Snapshot Before Demo là mốc phục hồi phương pháp luận khi cần đưa lab về baseline trước khi đổi biến can thiệp. | `EXPERIMENTAL_TRUTH_MATRIX.md`, Lecturer Scenario | **PASS** | Mô tả đúng vai trò kiểm soát biến phương pháp luận; không khẳng định sau mỗi ca đều đã restore snapshot trên thực tế. |
| **Data Collection Scope:** Chỉ thu thập Nmap raw (`.nmap`, `.xml`, `.gnmap`), screenshot terminal/VirtualBox, cấu hình Windows và log pfSense. | `EVIDENCE_REGISTER.md`, Section 23/24 Directive | **PASS** | Loại bỏ hoàn toàn `tcpdump`, `tshark`, `.pcap`, `Event Viewer`, timestamp screenshot requirement. |

---

## 4. Ma trận khắc phục hồi quy kỹ thuật (Technical Regression Closure Matrix)

| STT | Vấn đề phát hiện từ External Review R1 | Giải pháp khắc phục trong R2 | Trạng thái |
|:---:|---|---|:---:|
| 1 | Bảng tài liệu tham khảo tuyên bố quan sát chi tiết nhưng thiếu chứng minh mức độ truy cập (PTIT restricted). | Cập nhật bảng nguồn 7 cột trong `X5_DEMO_STYLE_REFERENCE_REVIEW.md`, ghi nhận rõ `METADATA_ONLY`, `FULL_TEXT`, `UNVERIFIED`. Loại bỏ nguồn unverified. | **CLOSED** |
| 2 | Demo 1 bị rút gọn thành 4 bước, bỏ kiểm tra IP/route và dùng ping thay Nmap discovery. | Phục hồi đủ 6 bước canonical: B1 IP/route, B2 Subnet discovery, B3 Target discovery, B4 SYN scan, B5 Service detection, B6 Safe NSE. Vẽ lại lưu đồ Hình 2.2. | **CLOSED** |
| 3 | Demo 2 sử dụng cờ `--script-args unsafe=0` và giải thích về nhánh khai thác bộ nhớ. | Xóa bỏ hoàn toàn `unsafe=0` và diễn giải nhánh bộ nhớ. Giữ đúng lệnh chuẩn và cơ chế chính thức trên pipe IPC$ và FID 0. | **CLOSED** |
| 4 | Demo 2 đưa vào phân tích mã lỗi `STATUS_INVALID_HANDLE` và thuật ngữ confusion matrix. | Loại bỏ `STATUS_INVALID_HANDLE` và các thuật ngữ `True Positive`, `True Negative`, `False Positive`. Đưa về phán quyết `UNKNOWN / NO USABLE SCRIPT RESULT`. | **CLOSED** |
| 5 | Bảng mitigation (Bảng 2.2) sử dụng cột "Kết quả kỳ vọng" và các tuyên bố chủ quan. | Đổi tên cột thành "Nội dung cần kiểm tra lại". Xóa bỏ mọi từ ngữ "triệt tiêu", "an toàn triệt để", "máy an toàn". | **CLOSED** |
| 6 | Case B tự thêm lệnh `Restart-Computer -Force`. | Xóa lệnh khởi động lại. Chỉ giữ lệnh duy nhất `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`. | **CLOSED** |
| 7 | Case B mô tả chạy lại toàn bộ NSE-SMB-01 đến 04 như một dữ kiện thực tế. | Giới hạn retest ở 2 phép kiểm có bằng chứng: `smb-protocols` và `smb-vuln-ms17-010`. | **CLOSED** |
| 8 | Case C sử dụng sai phiên bản `pfSense 2.7.2`. | Đổi toàn bộ sang phiên bản chuẩn `pfSense CE 2.9.0`. | **CLOSED** |
| 9 | Case C mô tả rule chặn chung chung và khẳng định "cổng chuyển sang filtered". | Mô tả cụ thể rule chặn có hướng (từ .10 đến .20) trên cổng 139, 445 có log. Xóa khẳng định kết quả rò rỉ sang Chương 3. | **CLOSED** |
| 10 | Case A dài dòng và diễn đạt như đã thực hiện vá lỗi trong lab. | Rút ngắn còn 1 đoạn súc tích, định vị rõ là giải pháp đối chứng lý thuyết (`REFERENCE ONLY / NOT MEASURED`). | **CLOSED** |
| 11 | Snapshot được mô tả như đã thực hiện restore sau mỗi ca đo. | Chuyển thành mô tả phương pháp luận: mốc phục hồi khi cần đưa môi trường về baseline trước khi can thiệp. | **CLOSED** |
| 12 | Tự tiện bổ sung `tcpdump`, `tshark`, `.pcap`, `Event Viewer` từ các báo cáo tham khảo. | Loại bỏ toàn bộ các công cụ và dạng log không có trong bằng chứng thực tế của đề tài. | **CLOSED** |

---

## 5. Kết quả kiểm tra Search Gate và QA Suite

### 5.1. Kết quả Search Gate (14 chỉ tiêu cấm)
- `unsafe=0`: **0 lần** (Đạt)
- `pfSense 2.7.2`: **0 lần** (Đạt)
- `Restart-Computer -Force`: **0 lần** (Đạt)
- `True Positive`: **0 lần** (Đạt)
- `True Negative`: **0 lần** (Đạt)
- `triệt tiêu MS17-010`: **0 lần** (Đạt)
- `máy an toàn`: **0 lần** (Đạt)
- `an toàn triệt để`: **0 lần** (Đạt)
- `tcpdump`: **0 lần** (Đạt)
- `tshark`: **0 lần** (Đạt)
- `.pcap`: **0 lần** (Đạt)
- `Event Viewer`: **0 lần** (Đạt)
- `# TÀI LIỆU THAM KHẢO`: **0 lần** trong `CHAPTER_2.md` (Đạt)
- `cách ly hoàn toàn`: **0 lần** (Đạt)

### 5.2. Kết quả kiểm tra QA Suite
1. **Linter học thuật tiếng Việt:**
   ```powershell
   uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_2.md
   ```
   *Kết quả:* **error=0, warning=0, info=0** (100% tuân thủ văn phong học thuật, không còn cảnh báo câu dài VI011).

2. **Kiểm tra trích dẫn khoa học:**
   ```powershell
   uv run python scripts/audit_ieee_citations.py work/do-an/CHAPTER_2.md
   ```
   *Kết quả:* **11 trích dẫn IEEE hợp lệ, xuất hiện tuần tự 1..11, không nhảy cóc hay mồ côi**.

3. **Kiểm tra tính toàn vẹn dự án và bộ kiểm thử:**
   ```powershell
   uv run python scripts/validate_project.py
   uv run python -m unittest discover -s tests -p "test_*.py"
   ```
   *Kết quả:* **Validation thành công, 7/7 tests pass**.

4. **Kiểm tra định dạng git:**
   ```powershell
   git diff --check
   ```
   *Kết quả:* **Mã thoát 0, không có lỗi khoảng trắng thừa (trailing whitespace) hay lỗi định dạng**.

---

## 6. Kết luận

Bản thảo Chương 2 phiên bản R2 đã giải quyết triệt để toàn bộ các khuyến nghị từ External Review R1:
- Giữ vững phong cách trình bày đơn giản, trực quan, dễ hiểu của một đồ án thực nghiệm an toàn thông tin.
- Khôi phục 100% tính chân lý kỹ thuật từ R5 baseline và Experimental Truth Matrix.
- Minh bạch hóa căn cứ nghiên cứu tham khảo, loại bỏ toàn bộ các công cụ và giả định không có trong bằng chứng thực tế.
- Đạt chuẩn toàn diện về cấu trúc (7 H2 / 20 H3), dung lượng (3.637 từ) và bộ công cụ kiểm định chất lượng (QA gate).

Trạng thái sẵn sàng: **`X5_DEMO_STYLE_R2_READY_FOR_EXTERNAL_REVIEW`**.
