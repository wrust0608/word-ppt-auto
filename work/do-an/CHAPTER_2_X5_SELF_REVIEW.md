# BÁO CÁO TỰ ĐÁNH GIÁ CHƯƠNG 2 — PHIÊN BẢN PRODUCT-ALIGNED
## (X5 PRODUCT-ALIGNED SELF-REVIEW R1)

**Thời điểm thực hiện:** 2026-10-06
**Vai trò thực hiện:** Executor / Writing Agent
**Tài liệu đánh giá:** `work/do-an/CHAPTER_2.md`
**Nhánh làm việc:** `feature/x5-chapter-2-product-aligned`
**Căn cứ chỉ đạo:** `CHANGE_REQUEST_CR-2026-10-06-X5-PRODUCT-ALIGNED.md` và `origin/main:work/do-an/prompts/X5_REWRITE_CHAPTER_2_PRODUCT_ALIGNED.md`
**Căn cứ khóa dữ liệu:** `EVIDENCE_AUDIT_R3_FINAL_LOCK.md`, `COMMAND_LINEAGE_MATRIX.md`, `TIMEBASE_AND_CROSS_LAYER_LOCKS.md`, `EXPERIMENTAL_TRUTH_MATRIX.md`
**Trạng thái đề xuất:** `X5_PRODUCT_ALIGNED_R1_READY_FOR_EXTERNAL_REVIEW`

---

## 1. Tổng quan cấu trúc và dung lượng

- **Tiêu đề chương:** `# CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM`
- **Số lượng phân mục:** Khóa cố định **7 H2** và **20 H3** (0 H4), đúng 100% theo cấu trúc prompt chính thức:
  - 2.1. Phạm vi và mô hình thực nghiệm (2.1.1, 2.1.2, 2.1.3)
  - 2.2. Chuẩn bị và xác nhận trạng thái ban đầu (2.2.1, 2.2.2, 2.2.3, 2.2.4, 2.2.5)
  - 2.3. Kịch bản 1 — Khảo sát dịch vụ SMB bằng Nmap (2.3.1, 2.3.2, 2.3.3)
  - 2.4. Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE (2.4.1, 2.4.2, 2.4.3)
  - 2.5. Kiểm thử hai biện pháp giảm thiểu đã thực hiện (2.5.1, 2.5.2, 2.5.3)
  - 2.6. Dữ liệu thực nghiệm và nguyên tắc sử dụng (2.6.1, 2.6.2, 2.6.3)
  - 2.7. Tổng kết chương
- **Dung lượng từ:** **3.773 từ** (nằm trọn vẹn trong ngân sách yêu cầu **3.200 – 3.800 từ**, bám sát dung lượng thực nghiệm của R4).
- **Kiến trúc trực quan và bảng biểu:**
  - 02 sơ đồ Mermaid:
    - Hình 2.1: Sơ đồ topo kết nối mạng ở trạng thái baseline trên VirtualBox (`192.168.56.0/24`).
    - Hình 2.2: Sơ đồ kiến trúc mạng pfSense Transparent Bridge trong kịch bản Case C (phân tách Data Plane qua `bridge0` và Management Plane qua `192.168.57.0/24`).
  - 04 bảng tổng hợp chuẩn hóa:
    - Bảng 2.1: Thông số kỹ thuật của các máy ảo trong môi trường thực nghiệm.
    - Bảng 2.2: Quy trình các bước thực hiện trong Kịch bản 1 (B1 đến B6).
    - Bảng 2.3: Danh mục 4 phép đo trong Kịch bản 2 (NSE-SMB-01 đến NSE-SMB-04).
    - Bảng 2.4: Thiết kế các kịch bản thực nghiệm và kế hoạch đo đạc đối chiếu (Baseline, Case B, Case C; loại bỏ hoàn toàn Case A).
- **Hệ thống trích dẫn:** Trích dẫn chuẩn IEEE với 11 nguồn tài liệu tham khảo (`[1]` đến `[11]`), xuất hiện tuần tự nghiêm ngặt theo thứ tự `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`.

---

## 2. Ma trận kiểm tra tính tương thích Product-Aligned (Product Alignment Audit Matrix)

| STT | Tiêu chí kiểm định theo Prompt X5 Product-Aligned | Thực hiện trong `CHAPTER_2.md` | Kết quả |
|:---:|---|---|:---:|
| 1 | **Exact operator commands Kịch bản 1:** Đúng lineage B1–B6, không tự thêm cờ `-Pn`. | B1: `ip addr show; ip route show`<br/>B2: `sudo nmap -sn -PR 192.168.56.0/24 -T3 --max-retries 2 -oA b2_host_discovery`<br/>B3: `sudo nmap -sn -PR 192.168.56.20 -T3 --max-retries 2 -oA b3_target_alive`<br/>B4: `sudo nmap -sS -p 139,445 192.168.56.20 -T3 --max-retries 2 --reason -oA b4_smb_ports`<br/>B5: `sudo nmap -sS -sV --version-intensity 5 -p 139,445 192.168.56.20 -T3 --max-retries 2 -oA b5_smb_version`<br/>B6: `sudo nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities 192.168.56.20 -T3 --max-retries 2 -oA b6_smb_nse`<br/>Tuyệt đối không có `-Pn`. | **PASS** |
| 2 | **Exact operator commands Kịch bản 2:** Trình bày đủ cả 4 lệnh NSE-SMB-01 đến NSE-SMB-04; không thêm `--privileged` vào lệnh người dùng. | Trình bày đầy đủ trong Bảng 2.3:<br/>- NSE-SMB-01: `sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20`<br/>- NSE-SMB-02: `nmap -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20`<br/>- NSE-SMB-03: `nmap -p 445 -n -T3 --max-retries 2 --script smb2-security-mode -oA evidence/nse-smb/NSE-SMB-03_signing 192.168.56.20`<br/>- NSE-SMB-04: `nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`<br/>Không có chữ `--privileged` trong văn bản. | **PASS** |
| 3 | **Loại bỏ bản dựng cũ `r170876`:** Sử dụng Oracle VM VirtualBox 7.2.20. | Chỉ ghi nhận: `Oracle VM VirtualBox 7.2.20`. Số lần xuất hiện của `r170876`: 0. | **PASS** |
| 4 | **Loại bỏ Case A khỏi thiết kế thực nghiệm:** Không có hàng Case A trong bảng thực nghiệm, không coi là biện pháp đã thực hiện. | Bảng 2.4 chỉ gồm: Baseline, Case B, Case C. Mục 2.5 tiêu đề là "Kiểm thử hai biện pháp giảm thiểu đã thực hiện". Vai trò bản vá được chuyển về phần xác nhận baseline (2.2.4) và đối chiếu lý thuyết tại Chương 4. | **PASS** |
| 5 | **Mô hình kiến trúc Case C:** Sơ đồ topo Transparent Bridge riêng biệt; phân tách rõ Data Plane và Management Plane. | Hình 2.2 mô tả đúng kiến trúc:<br/>- Data Plane: Kali `192.168.56.10` $
ightarrow$ `ATTT-PFS-KALI` $
ightarrow$ `em2` $
ightarrow$ `bridge0` $
ightarrow$ `em3` $
ightarrow$ `ATTT-PFS-WIN` $
ightarrow$ Windows `192.168.56.20`.<br/>- Management Plane: Host `192.168.57.1` $\leftrightarrow$ Host-Only #2 $\leftrightarrow$ `em1` `192.168.57.2`.<br/>Không biến Case C thành baseline topology. | **PASS** |
| 6 | **Cấu hình Case C Tunables & Rule:** Thể hiện đủ 3 tham số nhân `pfil` và quy tắc chặn có log. | Cấu hình nhân: `net.link.bridge.pfil_member = 1`, `net.link.bridge.pfil_bridge = 0`, `net.link.bridge.pfil_onlyip = 1`.<br/>Luật tường lửa: Action Block, IPv4 TCP, Source `192.168.56.10`, Destination `192.168.56.20`, Port 139, 445, Log enabled tại giao diện `em2`. | **PASS** |
| 7 | **Ranh giới gán nhãn luật tường lửa:** Không khẳng định log chứng minh khớp luật cụ thể do xung đột nhãn. | Đoạn văn mô tả mục đích kiểm tra log tường lửa để đối chiếu khả năng tiếp cận dịch vụ, không khẳng định exact named-rule attribution từ log screenshot. | **PASS** |
| 8 | **Không đồng nhất đồng hồ hệ thống (Timebase lock):** Không so sánh timestamp hiển thị chéo. | Đã quy định rõ tại Mục 2.6.3: đồ án không so sánh các mốc thời gian hiển thị giữa các máy ảo như một đồng hồ thống nhất. | **PASS** |
| 9 | **Không tự nhận diện host `.56.100`:** Không gán nhãn DHCP hay pfSense cho `.56.100`. | B2 chỉ ghi nhận chung: "Khảo sát các trạm hoạt động trong subnet" và "Danh sách IP phản hồi thăm dò ARP trong mạng". Không gán nhãn tùy tiện cho `.56.100`. | **PASS** |
| 10 | **Không leak kết quả đo đạc vào Chương 2:** Chương 2 chỉ mô tả phương pháp, tham số và mục tiêu quan sát. | Các bảng Bảng 2.2, 2.3, 2.4 chỉ nêu "Nội dung cần quan sát" hoặc "Kế hoạch đo đạc đối chiếu", tuyệt đối không chứa giá trị số đo thực tế hay kết luận đánh giá của Chương 3. | **PASS** |
| 11 | **Bảo toàn 5 ranh giới suy luận an toàn:** Thể hiện đầy đủ tại Mục 2.6.3. | 1. `445 open != vulnerable`<br/>2. `SMBv1 enabled != MS17-010 confirmed`<br/>3. `UNKNOWN != SAFE`<br/>4. `FILTERED != PATCHED`<br/>5. `SMBv1 disabled != PATCHED` | **PASS** |

---

## 3. Kết quả kiểm tra Search Gate và QA Suite

### 3.1. Kết quả Search Gate (15 chỉ tiêu bắt buộc)
- `r170876`: **0 lần** (Đạt)
- `--privileged`: **0 lần** (Đạt)
- `-Pn` trong Mục 2.3: **0 lần** (Đạt)
- `Remote Signal`: **0 lần** (Đạt)
- `Local Ground Truth`: **0 lần** (Đạt)
- `canonical`: **0 lần** (Đạt)
- `Bộ evidence hiện hành`: **0 lần** (Đạt)
- `Cập nhật bản vá KB4012213` trong bảng: **0 lần** (Đạt)
- `unsafe=0`: **0 lần** (Đạt)
- `pfSense 2.7.2`: **0 lần** (Đạt)
- `Restart-Computer -Force`: **0 lần** (Đạt)
- `tcpdump`: **0 lần** (Đạt)
- `tshark`: **0 lần** (Đạt)
- `.pcap`: **0 lần** (Đạt)
- `Event Viewer`: **0 lần** (Đạt)
- `# TÀI LIỆU THAM KHẢO`: **0 lần** (Đạt)
- Nhận diện võ đoán host `.56.100`: **Không có** (Đạt)

### 3.2. Kết quả kiểm tra QA Suite
1. **Kiểm tra tính hợp lệ đề án (`validate_project.py`):**
   ```powershell
   uv run python scripts/validate_project.py
   # Output: Project validation passed.
   ```
2. **Kiểm tra bộ unit test (`test_*.py`):**
   ```powershell
   uv run python -m unittest discover -s tests -p "test_*.py"
   # Output: Ran 7 tests in 0.003s - OK
   ```
3. **Kiểm tra linter văn phong học thuật tiếng Việt (`lint_vi_academic.py`):**
   ```powershell
   uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_2.md
   # Output: Không phát hiện mẫu văn phong cần xem xét. (error=0, warning=0, info=0)
   ```
4. **Kiểm tra trật tự trích dẫn IEEE (`audit_ieee_citations.py`):**
   ```powershell
   uv run python scripts/audit_ieee_citations.py work/do-an/CHAPTER_2.md
   # Output: first_appearance: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] (Chuỗi trích dẫn hợp lệ, không có lỗi thứ tự IEEE005)
   ```
5. **Kiểm tra định dạng git diff (`git diff --check`):**
   ```powershell
   git diff --check
   # Output: Clean (Không có trailing whitespace, không có lỗi định dạng)
   ```

---

## 4. Kết luận và đề xuất

Bản thảo `work/do-an/CHAPTER_2.md` đã được tái thiết kế hoàn chỉnh theo định hướng **Product-Aligned (R1)**:
- Bám sát 100% dữ liệu thực nghiệm đã khóa tại `EVIDENCE_AUDIT_R3_FINAL_LOCK.md` và `COMMAND_LINEAGE_MATRIX.md`.
- Duy trì phong cách đơn giản, dễ hiểu, trọng tâm, đúng chuẩn báo cáo đồ án an toàn thông tin của R4.
- Đạt 100% các tiêu chí Search Gate và vượt qua toàn bộ bộ công cụ QA kiểm định.

**Trạng thái đề xuất chính thức:**
`X5_PRODUCT_ALIGNED_R1_READY_FOR_EXTERNAL_REVIEW`
