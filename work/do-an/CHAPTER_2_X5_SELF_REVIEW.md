# BÁO CÁO TỰ ĐÁNH GIÁ CHƯƠNG 2 — PHIÊN BẢN PRODUCT-ALIGNED R2 (MICRO-PATCH)
## (X5 PRODUCT-ALIGNED SELF-REVIEW R2)

**Thời điểm thực hiện:** 2026-10-06
**Vai trò thực hiện:** Executor / Writing Agent
**Tài liệu đánh giá:** `work/do-an/CHAPTER_2.md`
**Nhánh làm việc:** `feature/x5-chapter-2-product-aligned`
**Candidate R1 gốc:** `1e1cc9edc191efb2a03e6b20807fa82d32841448`
**Căn cứ chỉ đạo:** `origin/main:work/do-an/prompts/X5_PRODUCT_ALIGNED_R2_MICRO_PATCH.md`
**Báo cáo thẩm định ngoài R1:** `origin/main:work/do-an/X5_PRODUCT_ALIGNED_EXTERNAL_REVIEW_R1.md` (89/100 — REVISE_MINOR_BLOCKING)
**Trạng thái đề xuất:** `X5_PRODUCT_ALIGNED_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

---

## 1. Tổng quan cấu trúc và dung lượng R2

- **Tiêu đề chương:** `# CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM`
- **Số lượng phân mục:** Khóa tuyệt đối **7 H2** và **20 H3** (0 H4), không thêm/bớt/đổi thứ tự:
  - 2.1. Phạm vi và mô hình thực nghiệm (2.1.1, 2.1.2, 2.1.3)
  - 2.2. Chuẩn bị và xác nhận trạng thái ban đầu (2.2.1, 2.2.2, 2.2.3, 2.2.4, 2.2.5)
  - 2.3. Kịch bản 1 — Khảo sát dịch vụ SMB bằng Nmap (2.3.1, 2.3.2, 2.3.3)
  - 2.4. Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE (2.4.1, 2.4.2, 2.4.3)
  - 2.5. Kiểm thử hai biện pháp giảm thiểu đã thực hiện (2.5.1, 2.5.2, 2.5.3)
  - 2.6. Dữ liệu thực nghiệm và nguyên tắc sử dụng (2.6.1, 2.6.2, 2.6.3)
  - 2.7. Tổng kết chương
- **Dung lượng từ:** **3.778 từ** (nằm trong biên độ thiết kế 3.200 – 3.800 từ).
- **Kiến trúc trực quan và bảng biểu:**
  - 02 sơ đồ Mermaid:
    - Hình 2.1: Sơ đồ topo kết nối mạng ở trạng thái baseline trên VirtualBox (`192.168.56.0/24`).
    - Hình 2.2: Sơ đồ kiến trúc mạng pfSense Transparent Bridge trong kịch bản Case C (`bridge0` và Management Plane `192.168.57.0/24`).
  - 04 bảng phương pháp và thiết kế đo đạc:
    - Bảng 2.1: Thông số kỹ thuật của các máy ảo trong môi trường thực nghiệm.
    - Bảng 2.2: Quy trình các bước thực hiện trong Kịch bản 1 (B1 đến B6).
    - Bảng 2.3: Danh mục 4 phép đo trong Kịch bản 2 (NSE-SMB-01 đến NSE-SMB-04).
    - Bảng 2.4: Thiết kế các kịch bản thực nghiệm và kế hoạch đo đạc đối chiếu (Baseline, Case B, Case C; không có Case A).
- **Hệ thống trích dẫn:** Trích dẫn chuẩn IEEE với 11 tài liệu tham khảo (`[1]` đến `[11]`), xuất hiện tuần tự nghiêm ngặt theo thứ tự `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`.

---

## 2. Ma trận đóng các điểm khuyến nghị từ Báo cáo thẩm định R1 (R1 Issue-Closure Matrix)

| STT | Vấn đề khuyến nghị tại Review R1 | Vị trí áp dụng | Giải pháp kỹ thuật xử lý trong Micro-Patch R2 | Kết quả |
|:---:|---|---|---|:---:|
| 1 | **BLOCKER 1 — Result leakage trong bảng phương pháp:** Cột quan sát Bảng 2.2 và 2.3 chứa giá trị đo đạc thực tế (`syn-ack`, `NT LM 0.12`, danh sách dialect cụ thể). | Bảng 2.2 (B4, B5, B6) & Bảng 2.3 (NSE-01..04) | Thay toàn bộ giá trị kết quả đo bằng định nghĩa trường cần quan sát:<br/>- B4: `Trạng thái cổng và trường REASON do Nmap trả về`<br/>- B5: `Chuỗi service/version fingerprint do Nmap trả về`<br/>- B6: `Danh sách dialect SMB, chính sách ký số và các capability do script trả về`<br/>- NSE-01: `Trạng thái TCP 139/445 và trường REASON`<br/>- NSE-02: `Danh sách dialect SMB do script trả về`<br/>- NSE-03: `Chính sách ký số SMB do script trả về`<br/>- NSE-04: `Script output / verdict nếu có` | **CLOSED** |
| 2 | **BLOCKER 2 — Nghĩa nhân quả của `FILTERED` bị suy diễn:** Khẳng định gói tin bị chặn trên đường truyền gán định trước nguyên nhân tường lửa. | Mục 2.6.3 (Quy tắc 4) | Chuẩn hóa theo định nghĩa Nmap chuẩn:<br/>`FILTERED cho biết Nmap không nhận đủ phản hồi để phân loại cổng là open hay closed; trạng thái này không chứng minh máy chủ đã được vá.` Không gán nguyên nhân chặn đường truyền chung trong Chương 2; để Chương 3 đối chiếu log pfSense. | **CLOSED** |
| 3 | **Suy diễn SMBv1 cần thắt chặt:** Câu văn cũ có thể tạo suy luận `SMBv1 enabled + UNPATCHED = MS17-010 confirmed`. | Mục 2.3.3 & Mục 2.6.3 | Thay cả hai vị trí bằng phát biểu chuẩn hóa:<br/>`SMBv1 được bật chỉ cho thấy giao thức liên quan còn được hỗ trợ; trạng thái này không đủ để xác nhận MS17-010. Việc đánh giá cần đối chiếu thêm trạng thái bản vá nội bộ và kết quả kiểm tra từ xa.` (Loại bỏ hoàn toàn cụm `điều kiện giao thức cần`). | **CLOSED** |
| 4 | **Diễn đạt Case B quá tuyệt đối:** Câu `nhằm loại bỏ hoàn toàn việc hỗ trợ` và `không yêu cầu khởi động lại máy` chưa sát thực tế. | Mục 2.5.2 | Đổi thành:<br/>- `nhằm vô hiệu hóa SMBv1 trong cấu hình SMB Server`<br/>- `Trong kịch bản không thực hiện bước khởi động lại máy, tính năng FS-SMB1 vẫn duy trì cài đặt trên hệ thống.` | **CLOSED** |
| 5 | **Thuật ngữ trạng thái bản vá:** Cụm từ `ngưỡng an toàn` ngụ ý ngưỡng phiên bản đơn lẻ là an toàn tuyệt đối. | Mục 2.2.4 | Đổi gạch đầu dòng thành:<br/>`Đối chiếu ngưỡng phiên bản đã cập nhật: Giá trị này thấp hơn ngưỡng phiên bản đã cập nhật tối thiểu 6.3.9600.18604 theo công bố của Microsoft [5].` | **CLOSED** |
| 6 | **Diễn đạt cô lập mạng quá tuyệt đối:** Các cụm `loại trừ kết nối mạng ngoài`, `bảo đảm tính khép kín`, `bảo đảm lưu lượng chỉ lưu chuyển cục bộ`. | Mục 2.1.1, 2.1.2, 2.2.1 | Thống nhất cách mô tả chuẩn xác dựa trên bằng chứng lab:<br/>`Ở trạng thái baseline, hai máy ảo chỉ sử dụng Host-Only NIC, không cấu hình NAT/Bridged và không có default route, qua đó giới hạn đường kết nối của chúng trong mạng lab.` | **CLOSED** |
| 7 | **Làm rõ tiêu chí chọn lọc dữ liệu:** Diễn đạt loại trừ dữ liệu pre-repair/troubleshooting dễ gây hiểu lầm là bỏ rơi dữ liệu. | Mục 2.6.2 | Làm rõ: Dữ liệu thử nghiệm sơ bộ, kiểm tra phục hồi (HostRepair) hoặc gián đoạn vẫn được lưu trữ đầy đủ để phục vụ truy vết kỹ thuật. Nhóm dữ liệu này không được dùng làm tập kết quả chính nhằm bảo đảm tính khách quan và nhất quán của kết quả đánh giá. Chương 3 sử dụng phiên chạy chuẩn hóa hoàn chỉnh để đánh giá. | **CLOSED** |
| 8 | **Thông số nhân Case C pfil:** Tránh ngụ ý một ảnh chụp màn hình chứng minh trực tiếp cả 3 tham số. | Mục 2.5.3 | Giữ nguyên 3 tham số `pfil_member=1`, `pfil_bridge=0`, `pfil_onlyip=1`; mô tả khách quan là cấu hình System Tunables của pfSense, không khẳng định sai lệch về bằng chứng ảnh. Giữ nguyên ranh giới không gán nhãn luật cụ thể từ log có xung đột label. | **CLOSED** |
| 9 | **Lược bỏ văn phong tự khen ngợi:** Cụm từ `tạo lập nền tảng khoa học vững chắc` mang tính tự đánh giá. | Mục 2.7 | Thay thế bằng câu văn học thuật trung tính:<br/>`Các tệp kết quả và nguyên tắc diễn giải trên được dùng làm cơ sở phân tích tại Chương 3.` | **CLOSED** |

---

## 3. Kết quả kiểm tra Search Gate và QA Suite

### 3.1. Kết quả Search Gate R2 (10 tiêu chí rà soát nghiêm ngặt)

| Tiêu chí rà soát (Search Gate) | Yêu cầu | Thực tế trong `CHAPTER_2.md` | Kết quả |
|---|:---:|:---:|:---:|
| `syn-ack` trong cột quan sát bảng phương pháp | 0 | 0 (Tổng toàn file: 0) | **PASS** |
| `NT LM 0.12` trong cột quan sát bảng phương pháp | 0 | 0 (Tổng toàn file: 0) | **PASS** |
| `FILTERED = firewall blocked packet` | Không xuất hiện | Không xuất hiện | **PASS** |
| `điều kiện giao thức cần` | 0 | 0 | **PASS** |
| `loại bỏ hoàn toàn việc hỗ trợ` | 0 | 0 | **PASS** |
| `ngưỡng an toàn` | 0 | 0 | **PASS** |
| `loại trừ kết nối mạng ngoài` | 0 | 0 | **PASS** |
| `bảo đảm tính khép kín` | 0 | 0 | **PASS** |
| `bảo đảm lưu lượng chỉ lưu chuyển cục bộ` | 0 | 0 | **PASS** |
| `nền tảng khoa học vững chắc` | 0 | 0 | **PASS** |
| `không yêu cầu khởi động lại máy` | 0 | 0 | **PASS** |

### 3.2. Kết quả kiểm tra QA Suite
1. **Kiểm tra tính hợp lệ đề án (`validate_project.py`):**
   ```powershell
   uv run python scripts/validate_project.py
   # Output: Project validation passed.
   ```
2. **Kiểm tra bộ unit test (`test_*.py`):**
   ```powershell
   uv run python -m unittest discover -s tests -p "test_*.py"
   # Output: Ran 7 tests in 0.004s - OK
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

## 3.3. Hiệu chỉnh sau external final review

External reviewer đã thực hiện một micro-adjustment trực tiếp sau R2 để:
- đưa dung lượng chương xuống dưới ngưỡng 3.800 từ;
- bỏ nốt một số câu có thể bị hiểu như kết quả đo thay vì điều kiện/phương pháp;
- giữ nguyên toàn bộ exact commands, cấu trúc 7 H2 / 20 H3, Case B và topology Case C.

## 4. Kết luận và đề xuất

Bản thảo `work/do-an/CHAPTER_2.md` đã hoàn tất vòng **Micro-Patch R2**:
- Đóng toàn diện 2 vấn đề chặn (BLOCKER 1 & BLOCKER 2) và toàn bộ các điểm hiệu chỉnh văn phong, ngữ nghĩa từ Báo cáo thẩm định ngoài R1.
- Bảo toàn tuyệt đối cấu trúc khóa 7 H2 / 20 H3, các câu lệnh đo đạc gốc, sơ đồ kiến trúc Case C và 5 ranh giới suy luận an toàn.
- Vượt qua 100% các tiêu chí Search Gate và QA suite tự động.

**Trạng thái đề xuất chính thức:**
`X5_PRODUCT_ALIGNED_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
