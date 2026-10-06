# BÁO CÁO TỰ ĐÁNH GIÁ KẾ HOẠCH BẰNG CHỨNG MỤC 3.5 CASE C R1 (CH3_35_CASEC_PLAN_SELF_REVIEW_R1)

- **Trạng thái:** `X7E0_CASEC_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7E0 — Case C Evidence & Presentation Plan`
- **Ngày thực hiện:** 2026-10-07
- **Ghi chú chuẩn mực:** Báo cáo này trình bày kết quả tự rà soát kỹ thuật khách quan và độc lập của Executor đối với toàn bộ các sản phẩm kế hoạch chuẩn bị cho Mục 3.5 — Case C (Kiểm soát lưu lượng SMB bằng tường lửa pfSense). Executor **tuyệt đối không tự ý công bố kết quả PASS**; trạng thái nghiệm thu chính thức chỉ được xác lập sau khi có báo cáo thẩm định ngoài độc lập (Independent External Review) và sự phê duyệt chính thức của người dùng.

---

## 1. Bảng Chỉ Số Thống Kê Tổng Hợp Kế Hoạch Case C R1 (Summary Metrics)

| Chỉ số kiểm tra (Audit Metric) | Số lượng / Trạng thái | Ghi chú chi tiết |
|---|:---:|---|
| **Tổng số tệp bằng chứng Case C canonical đã thẩm tra** | **17** | Thẩm tra 100% tệp trong `work/do-an/chapter3/evidence/case_c/` |
| **Số lượng bộ ba tệp thô máy đọc (Raw triplets)** | **2** (6 tệp) | Đầy đủ 2 bộ ba (`.nmap`, `.xml`, `.gnmap`): `NSE-SMB-01_ports` và `NSE-SMB-04_ms17010` |
| **Số lượng ảnh chụp màn hình gốc đã thẩm tra thị giác** | **9** | `pfSense_03` đến `pfSense_08`, `pfSense_CaseC_09`, `pfSense_10`, `pfSense_CaseC_11` |
| **Số lượng tệp siêu dữ liệu & kiểm toán tiến trình đã thẩm tra** | **2** | `pfSense_Remediation_Run_Manifest.txt` và `RUN4_PAUSE_STATE_REPORT.txt` |
| **Số lượng ảnh phân loại KEEP (Giữ lại chính thức)** | **3** | `pfSense_08_Rule_Order.png` (Hình 3.9), `pfSense_CaseC_09` (Hình 3.10), `pfSense_10` (Hình 3.11) |
| **Số lượng ảnh phân loại OPTIONAL (Dự phòng có kiểm soát)** | **2** | `pfSense_04_Bridge.png` và `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` (Hình 3.12 dự phòng) |
| **Số lượng ảnh phân loại DROP (Loại bỏ hoàn toàn)** | **4** | `pfSense_03_Interface_Assignment.png`, `pfSense_05_Bridge_Filtering.png`, `pfSense_06_Baseline_Pass_Rule.png`, `pfSense_07_Block_Rule_Config.png` |
| **Số lượng tiểu mục H3 đề xuất cho Mục 3.5** | **2** | `3.5.1` (Cầu nối pfSense & chính sách quy tắc) và `3.5.2` (Đo đạc từ xa, đối chiếu nhật ký & máy chủ) |
| **Số lượng bảng biểu đề xuất cho Mục 3.5** | **1** | `Bảng 3.6` (So sánh cấu hình, lưu lượng mạng và trạng thái hệ thống trước và sau can thiệp) |
| **Số lượng hình ảnh đề xuất cho Mục 3.5 (Phương án chính)** | **3** | `Hình 3.9` (Thứ tự quy tắc), `Hình 3.10` (Trạng thái cổng FILTERED), `Hình 3.11` (Nhật ký chặn lưu lượng SYN) |
| **Số lượng hàng luận điểm ánh xạ (Claim-Map Rows)** | **22** | 22 claims (`CC-C01` đến `CC-C22`), 100% đạt trạng thái `VERIFIED` |
| **Bảo tồn mâu thuẫn nhãn luật nhật ký tường lửa** | **Đạt** | Giữ nguyên mâu thuẫn giữa nhãn ảnh log (`100000104`) và manifest (`1000000104`), không che giấu |
| **Tuyệt đối không overclaim nhãn quy tắc từ ảnh log** | **Đạt** | Không viết log chứng minh quy tắc Block khớp; chỉ kết luận lưu lượng SMB SYN bị chặn trên pfSense |
| **Xử lý ranh giới trục thời gian (Timebase Boundary)** | **Đạt** | Không đồng bộ hóa giả tạo giữa 03:20 Kali và 14:20 pfSense; ưu tiên không đưa timestamp vào văn xuôi |
| **Phân định nguồn gốc trạng thái Windows cục bộ** | **Đạt** | Trạng thái máy chủ cục bộ kế thừa từ baseline Mục 3.1 và `RUN4_PAUSE_STATE_REPORT.txt`, không gán cho ảnh pfSense |
| **Khóa chặt nguyên lý `FILTERED != PATCHED`** | **Đạt** | Cổng bị lọc từ xa không đồng nghĩa với máy chủ đã được vá; máy chủ duy trì `UNPATCHED` |
| **Khóa chặt nguyên lý `UNKNOWN != SAFE`** | **Đạt** | Kịch bản MS17-010 không có đầu ra khả dụng (`UNKNOWN`); tuyệt đối không suy diễn thành SAFE |
| **Loại bỏ suy diễn về việc bypass tường lửa** | **Đạt** | Không tuyên bố bypass tường lửa chắc chắn sẽ khai thác thành công |
| **Tuân thủ quy tắc ZERO REPORT PROSE** | **Đạt** | 0 dòng văn xuôi báo cáo Mục 3.5 được soạn thảo trước; chỉ tạo 4 tệp kế hoạch |
| **Tuân thủ quy tắc ZERO DERIVED CROPS** | **Đạt** | 0 tệp ảnh cắt cúp phái sinh được tạo thật trên đĩa; chỉ đề xuất tọa độ dự kiến có thể tái lập |
| **Cách ly kết luận hiệu quả / rủi ro Chương 4** | **Đạt** | Không đưa ra nhận định giải pháp "hiệu quả", "an toàn hơn", "giảm thiểu rủi ro" hay xếp hạng giải pháp |
| **Không sửa đổi hạ tầng dự án** | **Đạt** | Không thay đổi file mã nguồn hay file cấu hình hạ tầng |

---

## 2. Kiểm Toán Chi Tiết 15 Tiêu Chí Đánh Giá Bắt Buộc

### 2.1. Tiêu chí 1: Thẩm tra toàn diện 17 tệp bằng chứng Case C
- **Yêu cầu:** Kiểm tra toàn bộ 17 tệp bằng chứng đã stage tại `work/do-an/chapter3/evidence/case_c/`.
- **Kết quả:** ĐÃ HOÀN THÀNH. Đã kiểm tra chi tiết cả 6 tệp raw Nmap (`.nmap`, `.xml`, `.gnmap`), 2 tệp điều hành/kiểm toán (`RUN4_PAUSE_STATE_REPORT.txt`, `pfSense_Remediation_Run_Manifest.txt`) và toàn bộ 9 ảnh chụp màn hình.

### 2.2. Tiêu chí 2: Thẩm tra thị giác toàn bộ 9 ảnh chụp màn hình
- **Yêu cầu:** Trực tiếp thẩm tra thị giác, đọc nội dung và xác định độ phân giải của cả 9 tệp ảnh.
- **Kết quả:** ĐÃ HOÀN THÀNH. Đã xem trực quan từng tệp ảnh thông qua công cụ đọc ảnh, xác định chính xác kích thước gốc từ $485 \times 654\,\text{px}$ đến $1359 \times 17637\,\text{px}$ và nội dung hiển thị thực tế.

### 2.3. Tiêu chí 3: Phân loại KEEP / OPTIONAL / DROP có lý giải khoa học
- **Yêu cầu:** Mỗi ảnh phải được đánh giá KEEP, OPTIONAL hoặc DROP; không chọn ảnh chỉ vì ảnh tồn tại.
- **Kết quả:** ĐÃ HOÀN THÀNH. Bảng đánh giá chi tiết trong `CH3_35_CASEC_FIGURE_SELECTION_R1.md` đã phân loại rõ: 3 KEEP, 2 OPTIONAL, 4 DROP, đi kèm lý giải chặt chẽ về giá trị độc bản so với văn bản và bảng biểu.

### 2.4. Tiêu chí 4: Số lượng bảng biểu tối giản và hiệu quả (Bảng 3.6)
- **Yêu cầu:** Thiết kế Bảng 3.6 theo định hướng kết quả (result-oriented), đối chiếu các trục thông số trước và sau can thiệp mà không biến thành bãi rác log.
- **Kết quả:** ĐÃ HOÀN THÀNH. Đã thiết kế Bảng 3.6 với 10 hàng dữ liệu chuẩn hóa, bao quát từ kiến trúc mạng, chính sách quy tắc, thứ tự đánh giá, trạng thái cổng 139/445, nhật ký pfSense, kết quả MS17-010 đến trạng thái giao thức, dịch vụ và bản vá cục bộ trên máy chủ. Bảng không chứa argv thô, không rò rỉ ID nội bộ.

### 2.5. Tiêu chí 5: Số lượng hình ảnh tối giản, chống "album ảnh chụp màn hình"
- **Yêu cầu:** Chọn số lượng ảnh ít nhất nhưng đủ để hội đồng hiểu ngay diễn biến thực nghiệm; đề xuất số hiệu hình từ Hình 3.9 trở đi.
- **Kết quả:** ĐÃ HOÀN THÀNH. Đề xuất Phương án A tối ưu chỉ gồm **3 hình**:
  - `Hình 3.9`: Danh sách và thứ tự quy tắc tường lửa pfSense (`pfSense_08_Rule_Order.png`).
  - `Hình 3.10`: Kết quả đo đạc trạng thái cổng SMB từ trạm Kali Linux (`pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`).
  - `Hình 3.11`: Nhật ký pfSense ghi nhận hành động chặn lưu lượng SYN (`pfSense_10_Block_Log_CANONICAL.png`).
  Đồng thời lưu giữ `Hình 3.12` (ảnh quét MS17-010) làm phương án dự phòng (Phương án B) nếu hội đồng yêu cầu.

### 2.6. Tiêu chí 6: Đề xuất cấu trúc H3 cân đối và hợp lý
- **Yêu cầu:** Đề xuất cấu trúc khoảng 2 tiểu mục H3, không rập khuôn máy móc Case B nếu hình thái bằng chứng khác biệt.
- **Kết quả:** ĐÃ HOÀN THÀNH. Đề xuất đúng 2 tiểu mục mạch lạc:
  - `3.5.1. Thiết lập cầu nối pfSense và chính sách kiểm soát lưu lượng SMB`
  - `3.5.2. Kết quả đo đạc từ xa, đối chiếu nhật ký tường lửa và trạng thái máy chủ`

### 2.7. Tiêu chí 7: Xử lý chính xác mâu thuẫn nhãn quy tắc trong nhật ký pfSense
- **Yêu cầu:** Nhận diện và xử lý mâu thuẫn giữa nhãn `CASE C baseline pass... (100000104)` trên ảnh và `CASE C - Block SMB... (1000000104)` trong manifest.
- **Kết quả:** ĐÃ HOÀN THÀNH. Kế hoạch xác định đây là mâu thuẫn nội tại chưa giải quyết (unresolved conflict), bảo tồn nguyên vẹn tính chân thực của dữ liệu và không tự ý sửa đổi.

### 2.8. Tiêu chí 8: Tuyệt đối không overclaim nhãn quy tắc từ ảnh log
- **Yêu cầu:** Cấm viết ảnh log chứng minh quy tắc Block đã match; chỉ được kết luận lưu lượng SMB SYN bị Block trên đường truyền pfSense.
- **Kết quả:** ĐÃ HOÀN THÀNH. Kế hoạch và ma trận luận điểm (`CC-C14`) khóa chặt công thức kết luận duy nhất: *"Lưu lượng TCP SYN tương ứng từ trạm Kali tới các cổng 139 và 445 của máy chủ Windows được ghi nhận bị chặn (Block) trên đường truyền đi qua pfSense."* Sự tồn tại và thứ tự ưu tiên của quy tắc Block được chứng minh độc lập bởi ảnh `pfSense_08`.

### 2.9. Tiêu chí 9: Xử lý ranh giới trục thời gian giữa Kali và pfSense
- **Yêu cầu:** Không đồng bộ hóa đồng hồ giả tạo (Kali 03:20 vs pfSense 14:20); ưu tiên không đưa timestamp vào văn xuôi.
- **Kết quả:** ĐÃ HOÀN THÀNH. Kế hoạch xác lập rõ ranh giới khác biệt miền đồng hồ (clock domain), nghiêm cấm tuyên bố wall-clock tương đương và quy định ưu tiên không đưa timestamp vào văn xuôi báo cáo.

### 2.10. Tiêu chí 10: Khóa chặt nguyên lý `FILTERED != PATCHED`
- **Yêu cầu:** Cấm tuyệt đối việc đánh đồng trạng thái cổng bị lọc từ xa với việc máy chủ đã được vá lỗi.
- **Kết quả:** ĐÃ HOÀN THÀNH. Ranh giới này được khẳng định nhất quán trong tất cả các tệp kế hoạch, bảng biểu và ma trận luận điểm (`CC-C11`, `CC-C19`, `CC-C20`).

### 2.11. Tiêu chí 11: Khóa chặt nguyên lý `UNKNOWN != SAFE`
- **Yêu cầu:** Cấm tuyệt đối việc suy diễn kết quả quét MS17-010 vắng mặt phán quyết thành hệ thống an toàn hay không có lỗ hổng.
- **Kết quả:** ĐÃ HOÀN THÀNH. Kế hoạch phân loại chuẩn xác kết quả là `UNKNOWN / NO USABLE SCRIPT RESULT` và khóa chặt nguyên tắc `UNKNOWN != SAFE` tại `CC-C16` và `CC-C21`.

### 2.12. Tiêu chí 12: Trình bày trung thực trạng thái máy chủ nội tại với nguồn gốc xuất xứ rõ ràng
- **Yêu cầu:** Không gán trạng thái Windows cục bộ (SMB1 True, LanmanServer Running, UNPATCHED) cho các ảnh chụp của pfSense.
- **Kết quả:** ĐÃ HOÀN THÀNH. Kế hoạch nêu rõ trạng thái máy chủ Windows được kế thừa từ mốc xuất phát Mục 3.1 và siêu dữ liệu kiểm toán `RUN4_PAUSE_STATE_REPORT.txt`, độc lập hoàn toàn với các ảnh chụp WebGUI pfSense.

### 2.13. Tiêu chí 13: Tuân thủ tuyệt đối quy tắc ZERO REPORT PROSE
- **Yêu cầu:** Pha này chỉ chuẩn bị kế hoạch trình bày bằng chứng (Pass 0), tuyệt đối không viết văn xuôi Mục 3.5.
- **Kết quả:** ĐÃ HOÀN THÀNH. 100% tài liệu tạo ra là các tệp kế hoạch, đánh giá hình ảnh, thiết kế bảng và ma trận luận điểm; không có bất kỳ tệp văn xuôi báo cáo nào được tạo trước.

### 2.14. Tiêu chí 14: Tuân thủ tuyệt đối quy tắc ZERO DERIVED CROPS
- **Yêu cầu:** Không tạo tệp cắt cúp ảnh thật trên đĩa ở bước này; chỉ đề xuất tọa độ dự kiến có thể tái lập.
- **Kết quả:** ĐÃ HOÀN THÀNH. Chỉ đề xuất tọa độ `[x, y, width, height]` và mô tả vùng thông tin cần giữ trong `CH3_35_CASEC_FIGURE_SELECTION_R1.md`; không tạo bất kỳ tệp `.png` cắt cúp nào vào thư mục presentation.

### 2.15. Tiêu chí 15: Cách ly hoàn toàn kết luận hiệu quả và đánh giá rủi ro của Chương 4
- **Yêu cầu:** Không đưa nhận định giải pháp "hiệu quả", "loại bỏ rủi ro", "an toàn hơn" hay xếp hạng giải pháp.
- **Kết quả:** ĐÃ HOÀN THÀNH. Đã kiểm toán sạch sẽ toàn bộ các câu chữ được phép sử dụng; mọi kết luận đều dừng lại ở quan sát thực nghiệm khách quan (Empirical Observations).

---

## 3. Kết Luận Tự Đánh Giá

Bộ 4 tài liệu kế hoạch Case C R1:
1. `work/do-an/CH3_35_CASEC_FIGURE_SELECTION_R1.md`
2. `work/do-an/CH3_35_CASEC_PRESENTATION_PLAN_R1.md`
3. `work/do-an/CH3_35_CASEC_CLAIM_EVIDENCE_MAP_R1.md`
4. `work/do-an/CH3_35_CASEC_PLAN_SELF_REVIEW_R1.md`

đã đáp ứng đầy đủ 100% các yêu cầu kỹ thuật và ràng buộc phương pháp luận đặt ra trong prompt `X7E0_CASEC_EVIDENCE_PRESENTATION_PLAN.md`.

Trạng thái sẵn sàng:
`X7E0_CASEC_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`
