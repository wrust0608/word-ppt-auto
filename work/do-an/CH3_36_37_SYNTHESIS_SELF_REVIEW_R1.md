# TỰ ĐÁNH GIÁ BẢN THẢO MỤC 3.6 VÀ 3.7 CHƯƠNG 3 — VÒNG HIỆU CHỈNH R2 (CH3_36_37_SYNTHESIS_SELF_REVIEW_R1)

- **Trạng thái:** `X7F_CH3_36_37_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7F R2 — Correct Sections 3.6 & 3.7 Synthesis`
- **Ngày thực hiện:** 2026-10-07
- **Đối tượng đánh giá:** [CH3_36_37_SYNTHESIS_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md)
- **Tài liệu tham chiếu:**
  * [X7F_R2_CORRECT_CH3_36_37.md](file:///e:/word_ppt-auto/work/do-an/prompts/X7F_R2_CORRECT_CH3_36_37.md)
  * [X7F_CH3_36_37_EXTERNAL_REVIEW_R1.md](file:///e:/word_ppt-auto/work/do-an/X7F_CH3_36_37_EXTERNAL_REVIEW_R1.md)
  * [CH3_31_BASELINE_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_31_BASELINE_DRAFT_R1.md)
  * [CH3_32_SCENARIO1_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md)
  * [CH3_33_SCENARIO2_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md)
  * [CH3_34_CASEB_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_34_CASEB_DRAFT_R1.md)
  * [CH3_35_CASEC_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_35_CASEC_DRAFT_R1.md)

---

## 1. Tổng Hợp Chỉ Số Bản Thảo R2 (R2 Synthesis Metrics)

| Chỉ số kiểm tra | Yêu cầu thiết kế R2 | Thực tế đạt được R2 | Đánh giá |
|---|---|---|---|
| **Số từ văn xuôi Mục 3.6** | 650 – 800 từ | **745 từ** (không tính Bảng 3.7) | **ĐẠT** |
| **Số từ văn xuôi Mục 3.7** | 230 – 330 từ | **316 từ** | **ĐẠT** |
| **Tổng số từ văn xuôi** | 900 – 1.300 từ | **1.061 từ** | **ĐẠT** |
| **Số đoạn văn xuôi** | ~8 – 10 đoạn | **9 đoạn** (6 đoạn Mục 3.6, 3 đoạn Mục 3.7) | **ĐẠT** |
| **Cấu trúc tiêu đề H2** | Đúng 2 H2 | 2 H2: `3.6` và `3.7` (0 H3 phát sinh) | **ĐẠT** |
| **Bảng biểu** | Đúng 1 bảng (4 cột) | 1 bảng (`Bảng 3.7`, 4 cột, 8 hàng tiêu chí) | **ĐẠT** |
| **Hình ảnh** | 0 hình ảnh mới | 0 hình mới, không có Hình 3.12 | **ĐẠT** |
| **Kiểm tra linter học thuật** | 0 lỗi / 0 cảnh báo | `lint_vi_academic.py`: 0 phát hiện | **ĐẠT** |

---

## 2. Báo Cáo Xử Lý Các Điểm Hiệu Chỉnh R2 (R2 Correction Audit)

### 2.1. Chuẩn hóa trạng thái TCP 445 trong Case B
- **Đã xóa bỏ:** Không còn bất kỳ xuất hiện nào của `OPEN (syn-ack)` đối với Case B.
- **Thực tế áp dụng:** Trong Bảng 3.7 và toàn bộ văn bản, Case B TCP 445 chỉ được ghi nhận là **`OPEN`** (do phép đo kiểm tra lại Case B không dùng tùy chọn `--reason`).
- **Đường cơ sở và Case C:** Baseline giữ `OPEN (syn-ack)`; Case C giữ `FILTERED (no-response)`.

### 2.2. Chuẩn hóa diễn đạt phương ngữ SMB (loại bỏ overclaim về đàm phán/workload)
- **Đã loại bỏ:** Các cụm từ suy diễn như `chấp thuận đàm phán`, `được hỗ trợ đầy đủ`, `loại bỏ thành công SMBv1`, `dịch vụ chấp thuận`.
- **Thực tế áp dụng:**
  * Baseline: `smb-protocols` ghi nhận 5 phương ngữ (`NT LM 0.12`, `2.0.2`, `2.1`, `3.0`, `3.0.2`).
  * Case B: `smb-protocols` ghi nhận `2.0.2`, `2.1`, `3.0`, `3.0.2`; phương ngữ `NT LM 0.12` không xuất hiện trong danh sách phương ngữ của phép đo lại.
  * Case C: Ghi nhận trung thực `Không có phép đo tương ứng trong Case C`.
  * Không suy diễn về tính tương thích workload hay thành công của quá trình bắt tay giao thức.

### 2.3. Loại bỏ việc gán nguyên nhân cho cổng 445 mở trong Case B
- **Đã loại bỏ:** Không gán nguyên nhân `để phục vụ SMB2/3` hay `do LanmanServer tiếp tục vận hành`.
- **Thực tế áp dụng:** Thuần túy quan sát thực nghiệm: *“Trong phép đo lại Case B, TCP 445 được ghi nhận OPEN.”*

### 2.4. Tinh chỉnh tiêu chí dịch vụ cục bộ (Bảng 3.7)
- **Điều chỉnh tiêu chí:** Đổi hàng bảng thành **`LanmanServer cục bộ`** nhằm tránh suy diễn về listener 139/445 khi Mục 3.4 không khóa phép đo listener cục bộ.
- **Thực tế ghi nhận:**
  * Baseline: `Running`.
  * Case B: `Running (tại thời điểm kiểm tra)`.
  * Case C: `Running (trạng thái ghi nhận cuối lượt)`.

### 2.5. Loại bỏ ngôn từ suy diễn trạng thái liên tục / zero downtime
- **Đã loại bỏ:** `duy trì trong mọi kịch bản`, `trạng thái nội bộ không thay đổi`, `giữ nguyên trạng cấu hình và dịch vụ`.
- **Thực tế áp dụng:** Dùng đúng ngôn ngữ kiểm thử ghi nhận theo mốc: `tại thời điểm kiểm tra`, `trạng thái ghi nhận cuối lượt Case C`, `Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá`.

### 2.6. Chuẩn hóa diễn đạt trạng thái bản vá / nhị phân
- **Đã loại bỏ:** `không can thiệp tệp nhị phân`, `không làm thay đổi phân loại bản vá nhị phân`, `mã nguồn`.
- **Thực tế áp dụng:** *“Trạng thái bản vá tiếp tục được phân loại UNPATCHED; Case B/Case C không ghi nhận thao tác cài bản vá.”* Bảo toàn các bất đẳng thức: `SMBv1 disabled != PATCHED`, `FILTERED != PATCHED`.

### 2.7. Chuẩn hóa so sánh Case C trên đường mạng
- **Thực tế áp dụng:** *“Trong Case C, từ trạm Kali, TCP 139/445 được ghi nhận FILTERED/no-response; đồng thời pfSense ghi nhận lưu lượng SMB SYN tương ứng bị Block trên đường thử nghiệm.”* Không khẳng định tường lửa là nguyên nhân tuyệt đối cho mọi tuyến đường mạng; không khơi lại tranh luận nhãn luật.

### 2.8. Loại bỏ nguyên nhân gán cho kết quả UNKNOWN
- **Đã loại bỏ:** Mọi dạng `UNKNOWN do...`, `do thiếu dữ kiện`, `do kịch bản không thu được...`.
- **Thực tế áp dụng:** *“Phép đo không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT. Nguyên nhân của việc không có đầu ra script khả dụng không được xác lập từ bộ bằng chứng hiện có.”* Bảo toàn `UNKNOWN != SAFE`.

### 2.9. Tinh chỉnh câu chữ Mục 3.7
- Case B: *“sau Case B, NT LM 0.12 không xuất hiện trong danh sách phương ngữ của phép đo lại, trong khi TCP 445 vẫn được ghi nhận OPEN.”* (Không dùng `Case B loại bỏ...`).
- Case C: *“trong Case C, TCP 139 và 445 được ghi nhận FILTERED/no-response từ trạm Kali.”* (Không dùng `Case C đưa... về FILTERED`).

### 2.10. Tinh gọn Bảng 3.7 từ 5 cột về 4 cột (tối ưu hóa cho A4)
- **Cấu trúc 4 cột chuẩn:**
  `Tiêu chí so sánh | Đường cơ sở / Kịch bản 1–2 | Case B — Vô hiệu hóa SMBv1 | Case C — Kiểm soát bằng pfSense`
- **Loại bỏ:** Cột thứ 5 (*Nhận xét thực nghiệm*) đã được lược bỏ hoàn toàn; các diễn giải kỹ thuật được chuyển tải súc tích trong phần văn xuôi phía dưới bảng.
- **8 hàng tiêu chí đối chiếu:**
  1. *Lớp can thiệp*
  2. *Trạng thái cổng TCP 139 từ xa (Từ trạm Kali Linux)*
  3. *Trạng thái cổng TCP 445 từ xa (Từ trạm Kali Linux)*
  4. *Phương ngữ SMB quan sát được (Từ trạm Kali Linux)*
  5. *Cấu hình giao thức SMBv1 cục bộ (`EnableSMB1Protocol`)*
  6. *LanmanServer cục bộ (Trên Windows Server 2012 R2)*
  7. *Trạng thái bản vá hệ thống cục bộ (driver `srv.sys`)*
  8. *Phán quyết kiểm tra MS17-010 từ xa (`smb-vuln-ms17-010`)*

---

## 3. Kiểm Tra Toàn Văn Các Chuỗi Ký Tự Nghiêm Cấm

Đã quét kiểm tra tự động bằng biểu thức chính quy trên [CH3_36_37_SYNTHESIS_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md):

| Chuỗi ký tự / Mẫu regex | Số lần phát hiện | Đánh giá |
|---|---|---|
| `Case B.*syn-ack` | **0** | **SẠCH** |
| `chấp thuận đàm phán` | **0** | **SẠCH** |
| `hỗ trợ đầy đủ` | **0** | **SẠCH** |
| `loại bỏ thành công` | **0** | **SẠCH** |
| `để phục vụ SMB2/3` | **0** | **SẠCH** |
| `do dịch vụ LanmanServer` | **0** | **SẠCH** |
| `duy trì trong mọi kịch bản` | **0** | **SẠCH** |
| `trạng thái nội bộ.*không thay đổi` | **0** | **SẠCH** |
| `giữ nguyên trạng` | **0** | **SẠCH** |
| `không can thiệp tệp nhị phân` | **0** | **SẠCH** |
| `mã nguồn` | **0** | **SẠCH** |
| `UNKNOWN do` | **0** | **SẠCH** |
| `do thiếu dữ kiện` | **0** | **SẠCH** |
| `do kịch bản kiểm tra` | **0** | **SẠCH** |
| `Case B loại bỏ` | **0** | **SẠCH** |
| `Case C đưa` | **0** | **SẠCH** |
| `hiệu quả hơn` / `tốt hơn` / `tối ưu` | **0** | **SẠCH** |
| `khuyến nghị` / `nên áp dụng` | **0** | **SẠCH** |
| `không có lỗ hổng` / `not vulnerable` | **0** | **SẠCH** |
| `false negative` / `bypass` / `exploit` | **0** | **SẠCH** |

---

## 4. Kết Luận Tự Đánh Giá R2

Bản thảo R2 đã xử lý dứt điểm 100% các điểm phản biện từ External Review R1:
- Chuẩn hóa trạng thái cổng TCP 445 trong Case B thành `OPEN` (không gán `syn-ack`).
- Loại bỏ hoàn toàn ngôn từ overclaim về đàm phán/workload và các câu giải thích nguyên nhân cho 445 hay UNKNOWN.
- Cải tiến Bảng 3.7 về 4 cột tinh gọn, đạt độ sắc nét và tối ưu cho trình bày A4.
- Đưa dung lượng văn xuôi về đúng khoảng lý tưởng (Mục 3.6: 745 từ; Mục 3.7: 316 từ; Tổng: 1.061 từ).

Trạng thái sẵn sàng: **`X7F_CH3_36_37_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`**
