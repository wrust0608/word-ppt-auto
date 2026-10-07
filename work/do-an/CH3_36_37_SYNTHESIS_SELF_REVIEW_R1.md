# TỰ ĐÁNH GIÁ BẢN THẢO MỤC 3.6 VÀ 3.7 CHƯƠNG 3 (CH3_36_37_SYNTHESIS_SELF_REVIEW_R1)

- **Trạng thái:** `X7F_CH3_36_37_R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7F — Synthesis Authoring: Section 3.6 & Section 3.7`
- **Ngày thực hiện:** 2026-10-07
- **Đối tượng đánh giá:** [CH3_36_37_SYNTHESIS_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md)
- **Tài liệu tham chiếu:**
  * [X7F_WRITE_CH3_36_37_SYNTHESIS.md](file:///e:/word_ppt-auto/work/do-an/prompts/X7F_WRITE_CH3_36_37_SYNTHESIS.md)
  * [CH3_31_BASELINE_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_31_BASELINE_DRAFT_R1.md)
  * [CH3_32_SCENARIO1_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md)
  * [CH3_33_SCENARIO2_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md)
  * [CH3_34_CASEB_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_34_CASEB_DRAFT_R1.md)
  * [CH3_35_CASEC_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_35_CASEC_DRAFT_R1.md)

---

## 1. Tổng Hợp Chỉ Số Bản Thảo (Synthesis Metrics)

| Chỉ số kiểm tra | Yêu cầu thiết kế | Thực tế đạt được | Đánh giá |
|---|---|---|---|
| **Số từ văn xuôi Mục 3.6 (Prose words 3.6)** | 650 – 900 từ | **834 từ** (không tính Bảng 3.7) | **ĐẠT** |
| **Số từ văn xuôi Mục 3.7 (Prose words 3.7)** | 250 – 400 từ | **293 từ** | **ĐẠT** |
| **Tổng số từ văn xuôi (Total prose words)** | 900 – 1.300 từ | **1.127 từ** | **ĐẠT** |
| **Số đoạn văn xuôi (Paragraph count)** | ~8 – 11 đoạn | **9 đoạn** (6 đoạn Mục 3.6, 3 đoạn Mục 3.7) | **ĐẠT** |
| **Cấu trúc tiêu đề H2** | Đúng 2 H2 (`3.6`, `3.7`) | 2 H2 chuẩn: `3.6. So sánh kết quả thực nghiệm` và `3.7. Tổng kết chương` | **ĐẠT** |
| **Cấu trúc tiêu đề H3** | Không có H3 phát sinh | 0 H3 (đúng thiết kế chuẩn) | **ĐẠT** |
| **Số lượng bảng biểu** | Đúng 1 bảng (`Bảng 3.7`) | 1 bảng (`Bảng 3.7`, 5 cột, 8 hàng dữ liệu so sánh) | **ĐẠT** |
| **Số lượng hình ảnh** | 0 hình ảnh mới | 0 hình mới, tuyệt đối không có Hình 3.12 | **ĐẠT** |
| **Kiểm tra linter học thuật** | 0 lỗi / 0 cảnh báo | `lint_vi_academic.py`: 0 phát hiện | **ĐẠT** |

---

## 2. Kiểm Tra Cấu Trúc Và Nguồn Gốc Dữ Liệu Bảng 3.7 (Table 3.7 Audit)

- **Tên bảng:** *Bảng 3.7. So sánh trạng thái thực nghiệm giữa đường cơ sở, Case B và Case C*
- **Cấu trúc 5 cột:**
  `Tiêu chí so sánh | Đường cơ sở / Kịch bản 1–2 | Case B — Vô hiệu hóa SMBv1 | Case C — Kiểm soát bằng pfSense | Nhận xét thực nghiệm`
- **Đối soát nguồn gốc 8 hàng tiêu chí:**
  1. *Lớp can thiệp:* Trích từ Mục 3.1, 3.4.1 và 3.5.1. Phân biệt rõ kết nối trực tiếp Host-Only, cấu hình máy chủ Windows và cầu nối pfSense Layer 2.
  2. *Trạng thái cổng TCP 139:*
     - Đường cơ sở: `OPEN (syn-ack)` (Mục 3.2).
     - Case B: Ghi nhận trung thực **`Không đo lại trong Case B`** (Mục 3.4 chỉ đo lại cổng 445; tuyệt đối không tự suy diễn là OPEN).
     - Case C: `FILTERED (no-response)` (Mục 3.5.2).
  3. *Trạng thái cổng TCP 445:*
     - Đường cơ sở: `OPEN (syn-ack)` (Mục 3.2, 3.3).
     - Case B: `OPEN (syn-ack)` (Mục 3.4.2).
     - Case C: `FILTERED (no-response)` (Mục 3.5.2).
  4. *Phương ngữ SMB quan sát được:*
     - Đường cơ sở: 5 phương ngữ từ SMBv1 (`NT LM 0.12`) đến SMBv3 (`3.0.2`) (Mục 3.2).
     - Case B: 4 phương ngữ (`2.0.2`, `2.1`, `3.0`, `3.0.2`), `NT LM 0.12` bị loại bỏ (Mục 3.4.2).
     - Case C: Ghi nhận trung thực **`Không có phép đo tương ứng trong Case C`** (Mục 3.5 không quét danh sách phương ngữ; tuyệt đối không tự điền danh sách từ baseline).
  5. *Cấu hình giao thức SMBv1 cục bộ (`EnableSMB1Protocol`):*
     - Đường cơ sở: `True` (Mục 3.1).
     - Case B: `False` (Mục 3.4.1).
     - Case C: `True` (Mục 3.5.2).
  6. *Dịch vụ chia sẻ tệp và listener cục bộ:* `LanmanServer : Running` và listener 139/445 hiện diện trong cả 3 trường hợp (Mục 3.1, 3.4.1, 3.5.2).
  7. *Trạng thái bản vá hệ thống cục bộ:* Cả 3 trường hợp duy trì phân loại `UNPATCHED` dựa trên driver `srv.sys` phiên bản `6.3.9600.16421` (Mục 3.1, 3.4.1, 3.5.2).
  8. *Phán quyết kiểm tra MS17-010 từ xa:* Cả 3 trường hợp duy trì phân loại `UNKNOWN` (`UNKNOWN != SAFE`) (Mục 3.3, 3.4.2, 3.5.2).

---

## 3. Kiểm Tra Ranh Giới Kỹ Thuật Và Phương Pháp Luận (Epistemic Boundary Audit)

1. **Tính trung thực với các dữ liệu không đo lại:**
   - Case B không đo lại cổng 139 $\rightarrow$ ghi nhận chính xác: `Không đo lại trong Case B`.
   - Case C không có phép đo liệt kê phương ngữ $\rightarrow$ ghi nhận chính xác: `Không có phép đo tương ứng trong Case C`.
2. **Không xếp hạng giải pháp hoặc khuyến nghị:**
   - Tuyệt đối không có các phát biểu so sánh hơn/kém: không có `Case B tốt hơn Case C`, không có `pfSense hiệu quả hơn/tối ưu hơn`.
   - Khẳng định theo cấu trúc tầng: *“Hai can thiệp tạo ra các thay đổi quan sát được ở hai lớp khác nhau.”*
   - Không đưa ra tỷ lệ giảm thiểu rủi ro (risk reduction %), không đưa ra khuyến nghị kiến trúc phòng thủ theo chiều sâu (defense in depth), không lấn sân sang Chương 4.
3. **Các bất đẳng thức ranh giới thực nghiệm:**
   - Tích hợp tự nhiên, mạch lạc trong văn bản:
     * `445 OPEN != vulnerable`
     * `SMBv1 enabled != MS17-010 confirmed`
     * `SMBv1 disabled != PATCHED`
     * `FILTERED != PATCHED`
     * `UNKNOWN != SAFE`
4. **Xử lý nhật ký pfSense:**
   - Ghi nhận ngắn gọn, khách quan: lưu lượng SMB SYN tương ứng bị chặn trên pfSense; không lặp lại tranh luận nhãn luật hay quy thuộc tên quy tắc cụ thể.
5. **Đóng phạm vi thực nghiệm Chương 3 (Mục 3.7):**
   - Tóm tắt cô đọng 3 giai đoạn: đường cơ sở, Case B và Case C.
   - Nhấn mạnh nguyên lý đa tầng: quan sát mạng từ xa, cấu hình dịch vụ hệ điều hành và bản vá nhị phân là 3 lớp thông tin riêng biệt, phải xác định độc lập.
   - Đoạn kết khép lại phạm vi thực nghiệm Chương 3 một cách tự nhiên mà không kích hoạt Chương 4.

---

## 4. Kiểm Tra Toàn Văn Các Chuỗi Nghiêm Cấm (Problematic Concepts Audit)

Đã quét tự động kiểm tra trên toàn bộ bản thảo [CH3_36_37_SYNTHESIS_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md):

| Chuỗi ký tự kiểm tra | Số lần xuất hiện | Đánh giá |
|---|---|---|
| `hiệu quả hơn` | **0** | **SẠCH** |
| `tốt hơn` | **0** | **SẠCH** |
| `tối ưu` | **0** | **SẠCH** |
| `khuyến nghị` | **0** | **SẠCH** |
| `nên áp dụng` | **0** | **SẠCH** |
| `không có lỗ hổng` | **0** | **SẠCH** |
| `not vulnerable` | **0** | **SẠCH** |
| `false negative` | **0** | **SẠCH** |
| `bypass` | **0** | **SẠCH** |
| `exploit` | **0** | **SẠCH** |
| `Evidence ID` | **0** | **SẠCH** |
| `Claim ID` | **0** | **SẠCH** |
| `truth matrix` | **0** | **SẠCH** |
| `canonical` | **0** | **SẠCH** |
| `governance` | **0** | **SẠCH** |
| `gate` | **0** | **SẠCH** |
| Suy đoán TCP 139 mở trong Case B | **0** | **SẠCH** |
| Suy đoán phương ngữ SMB trong Case C | **0** | **SẠCH** |

---

## 5. Kết Luận Tự Đánh Giá

Bản thảo tổng hợp Mục 3.6 và Mục 3.7 (R1) hoàn toàn đáp ứng trọn vẹn yêu cầu nhiệm vụ X7F: dung lượng văn xuôi chuẩn mực (1.127 từ), cấu trúc so sánh khoa học, trung thực tuyệt đối với các vùng dữ liệu không đo đạc, không đưa ra nhận định xếp hạng chủ quan, và khép lại toàn bộ Chương 3 một cách tự nhiên, chuẩn mực.

Trạng thái sẵn sàng: **`X7F_CH3_36_37_R1_READY_FOR_EXTERNAL_REVIEW`**
