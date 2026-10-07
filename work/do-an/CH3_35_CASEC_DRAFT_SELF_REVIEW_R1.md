# TỰ ĐÁNH GIÁ BẢN THẢO MỤC 3.5 CASE C (CH3_35_CASEC_DRAFT_SELF_REVIEW_R1)

- **Trạng thái:** `X7E1_CASEC_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7E1 — Draft Chapter 3 Section 3.5 Case C`
- **Đối tượng đánh giá:** [CH3_35_CASEC_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_35_CASEC_DRAFT_R1.md)
- **Tài liệu tham chiếu:**
  * [X7E1_WRITE_CH3_35_CASEC.md](file:///e:/word_ppt-auto/work/do-an/prompts/X7E1_WRITE_CH3_35_CASEC.md)
  * [CH3_35_CASEC_PRESENTATION_PLAN_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_35_CASEC_PRESENTATION_PLAN_R1.md)
  * [CH3_35_CASEC_CLAIM_EVIDENCE_MAP_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_35_CASEC_CLAIM_EVIDENCE_MAP_R1.md)
  * [CH3_35_CASEC_CROP_MANIFEST_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_35_CASEC_CROP_MANIFEST_R1.md)

---

## 1. Tổng Hợp Chỉ Số Bản Thảo (Draft Metrics)

| Chỉ số kiểm tra | Yêu cầu thiết kế | Thực tế đạt được | Đánh giá |
|---|---|---|---|
| **Số từ phần văn xuôi (Prose word count)** | 1.300 – 1.600 từ | **1.571 từ** (không tính Bảng 3.6 và chú thích ảnh) | **ĐẠT** |
| **Số đoạn văn xuôi (Paragraph count)** | ~12 – 16 đoạn | **15 đoạn** | **ĐẠT** |
| **Cấu trúc tiêu đề H2** | Đúng 1 H2 (`3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense`) | 1 H2 chuẩn | **ĐẠT** |
| **Cấu trúc tiêu đề H3** | Đúng 2 H3 (`3.5.1`, `3.5.2`) | 2 H3 chuẩn, không có H3 phát sinh | **ĐẠT** |
| **Số lượng bảng biểu** | Đúng 1 bảng (`Bảng 3.6`) | 1 bảng (`Bảng 3.6`, 4 cột, 10 hàng dữ liệu) | **ĐẠT** |
| **Số lượng hình ảnh** | Đúng 3 hình (`Hình 3.9`, `Hình 3.10`, `Hình 3.11`) | 3 hình, không thêm Hình 3.12 hay ảnh ghép | **ĐẠT** |
| **Kiểm tra linter học thuật** | Không có lỗi/cảnh báo nghiêm trọng | `lint_vi_academic.py`: 0 lỗi, 0 cảnh báo | **ĐẠT** |

---

## 2. Kiểm Tra Các Thành Phần Trình Bày (Presentation Audit)

### 2.1. Bảng 3.6
- **Tên bảng:** *Bảng 3.6. So sánh cấu hình, lưu lượng mạng và trạng thái hệ thống trước và sau khi áp dụng kiểm soát pfSense (Case C)*
- **Cấu trúc 4 cột:**
  1. `Tầng kiểm tra / Tham số đo đạc`
  2. `Trước can thiệp (Baseline)`
  3. `Sau can thiệp (Case C)`
  4. `Diễn giải trực tiếp & Giới hạn kết luận`
- **10 hàng tham số chuẩn:**
  1. Vị trí kiểm soát mạng / kiến trúc đường truyền
  2. Chính sách lọc pfSense
  3. Thứ tự quy tắc trên giao diện kiểm thử
  4. Trạng thái cổng TCP 139 từ xa
  5. Trạng thái cổng TCP 445 từ xa
  6. Nhật ký tường lửa pfSense
  7. Phán quyết kiểm tra MS17-010 từ xa
  8. Cấu hình giao thức SMBv1 cục bộ
  9. Dịch vụ chia sẻ tệp và listener cục bộ
  10. Trạng thái bản vá hệ thống cục bộ
- **Xác thực diễn đạt Baseline:**
  * Ghi nhận: *"Host-Only baseline; chưa có pfSense trên đường thử nghiệm Kali → Windows"*.
  * Tuyệt đối không dùng các cụm từ sai lệch như *"chưa có firewall"* hoặc *"không qua thiết bị lọc"*, bảo toàn sự hiện diện của Windows Firewall đường cơ sở.

### 2.2. Danh mục hình ảnh và thông số cắt cúp
Toàn bộ hình ảnh đã được kiểm tra trực quan, tạo tệp phái sinh độc lập tại `work/do-an/chapter3/presentation/3_5/` và lập bảng kê chi tiết tại `work/do-an/CH3_35_CASEC_CROP_MANIFEST_R1.md`:

1. **Hình 3.9:**
   - **Tệp nguồn:** `work/do-an/chapter3/evidence/case_c/pfSense_08_Rule_Order.png` ($485 \times 731\,\text{px}$)
   - **SHA-256 nguồn:** `6029ea7c923c297aa9bc65c3c551a17e1d4f569a2c98f78846a39c69e22aeb45`
   - **Khung cắt cúp:** `x = 15, y = 190, width = 470, height = 340`
   - **Tệp phái sinh:** `work/do-an/chapter3/presentation/3_5/Hinh_3_9_pfSense_Rule_Order.png` ($470 \times 340\,\text{px}$)
   - **SHA-256 phái sinh:** `5b8a4a3b26c6aca6b667e5a4ee256c48dcdd555324e2f7ed0755ae80eba06285`
   - **Nội dung:** Giữ tab `CASE_C_KALI`, tiêu đề `Rules (Drag to Change Order)`, đầy đủ hàng quy tắc Block Dòng 1 (cổng 139, 445 kèm cờ ghi log) và hàng Pass baseline Dòng 2; loại bỏ cảnh báo mật khẩu và chân trang.

2. **Hình 3.10:**
   - **Tệp nguồn:** `work/do-an/chapter3/evidence/case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` ($1280 \times 800\,\text{px}$)
   - **SHA-256 nguồn:** `de266abb4fa3e8412cfc091975d714bb4bf1168a2e3d7f6cba7d7276f22dfba7`
   - **Khung cắt cúp:** `x = 195, y = 120, width = 660, height = 505`
   - **Tệp phái sinh:** `work/do-an/chapter3/presentation/3_5/Hinh_3_10_Nmap_Filtered.png` ($660 \times 505\,\text{px}$)
   - **SHA-256 phái sinh:** `da342f6fb9909da67fd38caedf73e2f848ac3c65306ec5993f864f9260418942`
   - **Nội dung:** Giữ trọn câu lệnh Nmap, `Host is up / arp-response`, trạng thái `139/tcp filtered netbios-ssn no-response`, `445/tcp filtered microsoft-ds no-response`, dòng địa chỉ MAC và `Nmap done`.

3. **Hình 3.11:**
   - **Tệp nguồn:** `work/do-an/chapter3/evidence/case_c/pfSense_10_Block_Log_CANONICAL.png` ($1359 \times 17637\,\text{px}$)
   - **SHA-256 nguồn:** `3b8383c54143f8a01eb6201462a6b30877f4b95f27b1a72f54b8b07562a68bc2`
   - **Khung cắt cúp thực tế (thẩm tra trực quan):** `x = 40, y = 15355, width = 1280, height = 220`
   - **Tệp phái sinh:** `work/do-an/chapter3/presentation/3_5/Hinh_3_11_pfSense_Block_Log.png` ($1280 \times 220\,\text{px}$)
   - **SHA-256 phái sinh:** `8333c06da3e35553481d00a7f84c4d65b64dde5a4f7aadc77567d52d113c919b`
   - **Nội dung:** Giữ 4 bản ghi Block màu đỏ đối với lưu lượng `TCP:S` từ `192.168.56.10` tới `192.168.56.20:139/445` trên giao diện `CASE_C_KALI`; **bảo tồn nguyên vẹn cột Rule chứa nhãn xung đột** (`CASE C baseline pass... (100000104)`), tuyệt đối không cắt xén để che giấu.

---

## 3. Kiểm Tra Ranh Giới Kỹ Thuật Và Lập Luận (Epistemic Boundary Audit)

1. **Xử lý mâu thuẫn nhãn quy tắc tại Hình 3.11:**
   - Bản thảo nêu rõ: *"Ảnh nhật ký hiển thị nhãn quy tắc không trùng với tên được ghi trong manifest. Vì vậy, báo cáo chỉ sử dụng ảnh để xác nhận hành động Block đối với lưu lượng SMB SYN tương ứng trên đường truyền, không dùng ảnh này để quy thuộc tuyệt đối cho một tên quy tắc cụ thể."*
   - Không suy đoán nguyên nhân, không giải thích lý do giao diện ghi đè hay gán nhãn sai.

2. **Ranh giới đo đạc cổng và quan hệ nhân quả:**
   - Kết quả đo từ trạm Kali: `139/tcp filtered no-response` và `445/tcp filtered no-response`.
   - Sử dụng khái niệm **"đối chiếu liên tầng"** giữa cổng bị lọc trên Nmap và nhật ký Block trên pfSense.
   - Tuyệt đối không khẳng định "chứng minh quan hệ nhân quả tuyệt đối" hoặc "đồng bộ thời gian giữa Kali và pfSense".

3. **Ranh giới kiểm tra lỗ hổng MS17-010 (NSE-SMB-04):**
   - Phân loại chuẩn xác: `UNKNOWN / NO USABLE SCRIPT RESULT`.
   - Giữ nguyên ranh giới phương pháp luận: *"Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có."*
   - Khẳng định rõ ràng: `UNKNOWN != SAFE`. Không khẳng định "do cổng bị chặn nên script không chạy", không gán nhãn false-negative, SAFE, NOT VULNERABLE hay PATCHED.

4. **Trạng thái máy chủ cục bộ (Windows Local):**
   - Nguồn gốc dữ liệu: trích xuất từ mốc kiểm thử Mục 3.1 và metadata cuối Case C (`RUN4_PAUSE_STATE_REPORT.txt`). Bản thảo nói rõ Case C không có ảnh chụp màn hình Windows mới do không can thiệp trực tiếp máy chủ.
   - Trạng thái ghi nhận point-in-time: `EnableSMB1Protocol : True`, `EnableSMB2Protocol : True`, `LanmanServer : Running`, listener 139/445 hiện diện, trạng thái bản vá `UNPATCHED`.
   - Phiên bản số driver `srv.sys` dùng để phân loại bản vá: `6.3.9600.16421`.
   - Tuyệt đối không khẳng định "zero downtime", "máy chủ không gián đoạn trong mọi thời điểm" hay "pfSense chứng minh trạng thái Windows".
   - Khẳng định cốt lõi: `FILTERED != PATCHED`.

5. **Giới hạn phạm vi chương và mục:**
   - Không đưa ra bảng xếp hạng hiệu quả giữa Case C và Case B trong phần này.
   - Không đưa ra khuyến nghị kiến trúc phòng thủ cho Chương 4.
   - Không có thuật ngữ quản trị nội bộ: Không xuất hiện các mã Claim ID (`CC-C01`...), Evidence ID, gate, governance hay closure trong phần văn xuôi sinh viên.

---

## 4. Kiểm Tra Thuật Ngữ Nghiêm Cấm (Forbidden Terms Check)

Đã thực hiện tìm kiếm toàn văn trong [CH3_35_CASEC_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_35_CASEC_DRAFT_R1.md):
- `do cổng 445`: 0 xuất hiện
- `script không thể`: 0 xuất hiện
- `Nmap tự động`: 0 xuất hiện
- `false negative`: 0 xuất hiện
- `SAFE` (ngoài bất đẳng thức `UNKNOWN != SAFE`): 0 xuất hiện
- `NOT VULNERABLE`: 0 xuất hiện
- `PATCHED` (ngoài bất đẳng thức `FILTERED != PATCHED` và trạng thái `UNPATCHED`): 0 xuất hiện
- `nhân quả`: 0 xuất hiện (thay thế hoàn toàn bằng *đối chiếu liên tầng*)
- `bắt nguồn từ`: 0 xuất hiện
- `hoàn toàn không thay đổi`: 0 xuất hiện
- `zero downtime`: 0 xuất hiện
- `không gián đoạn`: 0 xuất hiện (chỉ xuất hiện 1 lần trong câu phủ định cảnh báo: *"không suy diễn tính liên tục không gián đoạn"*)
- `bảo đảm tuyệt đối`: 0 xuất hiện
- `eliminated exploitability`: 0 xuất hiện
- `intrinsically vulnerable`: 0 xuất hiện
- `CC-C`: 0 xuất hiện

---

## 5. Kết Luận Tự Đánh Giá

Bản thảo Mục 3.5 Case C (R1) hoàn toàn tuân thủ chặt chẽ đề cương, kế hoạch trình bày X7E0 đã được người dùng chốt, bảo tồn nguyên trạng các chứng cứ thực nghiệm và tuân thủ nghiêm ngặt ranh giới tri nhận khoa học.

Trạng thái sẵn sàng: **`X7E1_CASEC_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`**
