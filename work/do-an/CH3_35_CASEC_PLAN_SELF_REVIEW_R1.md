# BÁO CÁO TỰ ĐÁNH GIÁ KẾ HOẠCH BẰNG CHỨNG MỤC 3.5 CASE C R2 (CH3_35_CASEC_PLAN_SELF_REVIEW_R1)

- **Trạng thái:** `X7E0_CASEC_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7E0 R2 — Correct Case C Evidence & Presentation Plan`
- **Ngày thực hiện:** 2026-10-07
- **Ghi chú chuẩn mực:** Báo cáo này trình bày kết quả tự rà soát kỹ thuật sau khi khắc phục triệt để toàn bộ 8 nhóm tồn tại được chỉ ra trong Báo cáo Thẩm định Ngoài Độc lập R1 (`work/do-an/X7E0_CASEC_PLAN_EXTERNAL_REVIEW_R1.md`). Executor **tuyệt đối không tự ý công bố kết quả PASS**; trạng thái nghiệm thu chính thức chỉ được xác lập sau khi có quyết định thẩm định ngoài độc lập cuối cùng và sự phê duyệt chính thức của người dùng.

---

## 1. Bảng Chỉ Số Thống Kê Tổng Hợp Kế Hoạch Case C R2 (Summary Metrics)

| Chỉ số kiểm tra (Audit Metric) | Số lượng / Trạng thái | Ghi chú chi tiết |
|---|:---:|---|
| **Tổng số tệp bằng chứng Case C canonical đã thẩm tra** | **17** | Thẩm tra 100% tệp trong `work/do-an/chapter3/evidence/case_c/` |
| **Số lượng bộ ba tệp thô máy đọc (Raw triplets)** | **2** (6 tệp) | Đầy đủ 2 bộ ba (`.nmap`, `.xml`, `.gnmap`): `NSE-SMB-01_ports` và `NSE-SMB-04_ms17010` |
| **Số lượng ảnh chụp màn hình gốc đã thẩm tra thị giác** | **9** | `pfSense_03` đến `pfSense_08`, `pfSense_CaseC_09`, `pfSense_10`, `pfSense_CaseC_11` |
| **Số lượng tệp siêu dữ liệu & kiểm toán tiến trình đã thẩm tra** | **2** | `pfSense_Remediation_Run_Manifest.txt` và `RUN4_PAUSE_STATE_REPORT.txt` |
| **Số lượng ảnh phân loại KEEP (Giữ lại chính thức)** | **3** | `pfSense_08_Rule_Order.png` (Hình 3.9), `pfSense_CaseC_09` (Hình 3.10), `pfSense_10` (Hình 3.11) |
| **Số lượng ảnh phân loại OPTIONAL / DROP** | **6** | 2 OPTIONAL/DROP (`pfSense_04`, `pfSense_CaseC_11`); 4 DROP (`pfSense_03`, `05`, `06`, `07`) |
| **Số lượng tiểu mục H3 đề xuất cho Mục 3.5** | **2** | `3.5.1` (Cầu nối pfSense & chính sách quy tắc) và `3.5.2` (Đo đạc từ xa, đối chiếu nhật ký & máy chủ) |
| **Số lượng bảng biểu đề xuất cho Mục 3.5** | **1** | `Bảng 3.6` (So sánh cấu hình, lưu lượng mạng và trạng thái hệ thống trước và sau can thiệp) |
| **Số lượng hình ảnh đề xuất cho Mục 3.5 (Phương án chính)** | **3** | `Hình 3.9` (Thứ tự quy tắc), `Hình 3.10` (Trạng thái cổng FILTERED), `Hình 3.11` (Nhật ký chặn lưu lượng SYN) |
| **Số lượng hàng luận điểm ánh xạ (Claim-Map Rows)** | **22** | 22 claims (`CC-C01` đến `CC-C22`), 100% đạt trạng thái `VERIFIED` |
| **Bảo tồn mâu thuẫn nhãn luật nhật ký tường lửa** | **Đạt** | Giữ nguyên mâu thuẫn giữa nhãn ảnh log (`100000104`) và manifest (`1000000104`), không che giấu |
| **Tuyệt đối không overclaim nhãn quy tắc từ ảnh log** | **Đạt** | Không viết log chứng minh quy tắc Block khớp; chỉ kết luận lưu lượng SMB SYN bị chặn trên pfSense |
| **Xử lý ranh giới trục thời gian (Timebase Boundary)** | **Đạt** | Không đồng bộ hóa giả tạo giữa 03:20 Kali và 14:20 pfSense; ưu tiên không đưa timestamp vào văn xuôi |
| **Phân định nguồn gốc trạng thái Windows cục bộ** | **Đạt** | Trạng thái máy chủ cục bộ point-in-time kế thừa từ baseline Mục 3.1 và `RUN4_PAUSE_STATE_REPORT.txt` |
| **Khóa chặt nguyên lý `FILTERED != PATCHED`** | **Đạt** | Cổng bị lọc từ xa không đồng nghĩa với máy chủ đã được vá; máy chủ duy trì `UNPATCHED` |
| **Khóa chặt nguyên lý `UNKNOWN != SAFE`** | **Đạt** | Phép đo NSE04 phân loại `UNKNOWN / NO USABLE SCRIPT RESULT`; không gán nguyên nhân cơ chế nội bộ |
| **Thay thế cụm từ nhân quả bằng đối chiếu liên tầng** | **Đạt** | Bỏ "bằng chứng nhân quả liên tầng", "xác lập quan hệ nhân quả", "bắt nguồn từ"; dùng "đối chiếu liên tầng" |
| **Hiệu chỉnh tọa độ crop dự kiến Hình 3.9** | **Đạt** | Điều chỉnh về `x ≈ 15, y ≈ 190, width ≈ 470, height ≈ 340`, bao quát tab `CASE_C_KALI`, tiêu đề và 2 luật |
| **Đánh dấu crop Hình 3.11 là PROVISIONAL ONLY** | **Đạt** | Nguồn ảnh $1359 \times 17637\,\text{px}$, bắt buộc tái thẩm tra thị giác trước khi tạo crop ở bước X7E1 |
| **Làm sạch tham chiếu kho chỉ mục bằng chứng** | **Đạt** | Xóa bỏ triệt để tham chiếu tới `CHAPTER_3_EVIDENCE_INDEX.md` và mã chưa đăng ký |
| **Tuân thủ quy tắc ZERO REPORT PROSE** | **Đạt** | 0 dòng văn xuôi báo cáo Mục 3.5 được soạn thảo trước; chỉ chỉnh sửa 4 tệp kế hoạch |
| **Tuân thủ quy tắc ZERO DERIVED CROPS** | **Đạt** | 0 tệp ảnh cắt cúp phái sinh được tạo thật trên đĩa |

---

## 2. Kiểm Toán Chi Tiết 8 Nhóm Khắc Phục Theo Review R1

### 2.1. Nhóm 1: Không gán nguyên nhân cơ chế cho việc script NSE04 không có phán quyết
- **Vấn đề R1:** Kế hoạch cũ gán lý do "do cổng 445 bị chặn nên script không nhận được phản hồi để thực thi".
- **Khắc phục R2:** Đã xóa bỏ hoàn toàn mọi giả định cơ chế nội bộ. Sử dụng chuẩn mực câu văn thống nhất:
  *"Phép đo NSE-SMB-04 ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT. Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có."*
  Đồng thời khóa chặt nguyên tắc phương pháp luận: `UNKNOWN != SAFE`.

### 2.2. Nhóm 2: Chuẩn hóa dữ liệu đường cơ sở trong Bảng 3.6
- **Vấn đề R1:** Mô tả trạng thái trước can thiệp là "không có tường lửa", "không qua thiết bị lọc" trong khi Windows Firewall baseline đã tồn tại.
- **Khắc phục R2:** Đã chuẩn hóa toàn bộ các hàng trong Bảng 3.6:
  - Đường truyền mạng: *"Host-Only baseline; chưa có pfSense trên đường thử nghiệm Kali → Windows."*
  - Chính sách pfSense: *"Chưa áp dụng ruleset pfSense Case C trên đường thử nghiệm."*
  - Thứ tự quy tắc: *"Không áp dụng đối với pfSense Case C."*
  - Nhật ký pfSense: *"Không có log pfSense tương ứng vì pfSense chưa nằm trên đường baseline."*

### 2.3. Nhóm 3: Thu hẹp và loại bỏ các tuyên bố quá tuyệt đối hóa
- **Vấn đề R1:** Sử dụng các cụm từ tuyệt đối như "toàn bộ lưu lượng bắt buộc phải đi qua", "máy chủ hoàn toàn không trải qua bất kỳ thay đổi nào", "dịch vụ SMBv1 chứa lỗ hổng vẫn tồn tại nguyên vẹn".
- **Khắc phục R2:**
  - Về topology: Chuẩn hóa thành *"Trong topology Case C, đường thử nghiệm Kali → Windows được bố trí đi qua bridge0 của pfSense."*
  - Về trạng thái máy chủ Windows: Chuẩn hóa thành *"Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá trên Windows; metadata cuối Case C ghi nhận SMB1=True, SMB2=True, LanmanServer=Running, các listener cục bộ 139/445 hiện diện và patch state UNPATCHED."*
  - Bỏ triệt để cụm từ "dịch vụ SMBv1 chứa lỗ hổng vẫn tồn tại nguyên vẹn"; chỉ khẳng định cấu hình cục bộ SMB1 duy trì True và trạng thái phân loại bản vá duy trì UNPATCHED.
  - Xác lập chính xác phiên bản số so sánh bản vá của `srv.sys` là `6.3.9600.16421` (không nhầm lẫn với chuỗi hiển thị `6.3.9600.16384`).

### 2.4. Nhóm 4: Thay thế ngôn ngữ nhân quả bằng đối chiếu liên tầng
- **Vấn đề R1:** Lạm dụng các thuật ngữ "bằng chứng nhân quả liên tầng", "xác lập mối quan hệ nhân quả", "FILTERED bắt nguồn từ việc pfSense...".
- **Khắc phục R2:** Thay thế toàn bộ bằng thuật ngữ khoa học *"đối chiếu liên tầng"*. Mẫu câu chuẩn mực tại mục 3.5.2 và ma trận luận điểm:
  *"Trong lượt Case C, Nmap ghi nhận TCP 139/445 ở trạng thái FILTERED, đồng thời log pfSense ghi nhận lưu lượng TCP SYN tương ứng từ Kali tới các cổng này bị Block trên đường pfSense. Đối chiếu liên tầng giữa phép đo Nmap và nhật ký pfSense cho thấy sự tương ứng về địa chỉ nguồn/đích, cổng dịch vụ và hành vi kiểm soát mạng."*

### 2.5. Nhóm 5: Tinh chỉnh tọa độ crop dự kiến cho Hình 3.9
- **Vấn đề R1:** Tọa độ R1 (`x=20, y=370, width=455, height=240`) cắt mất bối cảnh tab `CASE_C_KALI` và có nguy cơ cắt tiêu đề bảng quy tắc.
- **Khắc phục R2:** Điều chỉnh khung cắt cúp dự kiến về vùng `x ≈ 15, y ≈ 190, width ≈ 470, height ≈ 340` (vùng `[15, 190, 485, 530]`):
  - Bảo toàn đầy đủ: Ngữ cảnh tab `CASE_C_KALI`, tiêu đề `Rules (Drag to Change Order)`, trọn vẹn hàng quy tắc Block SMB (Dòng 1) và Pass baseline (Dòng 2).
  - Loại bỏ: Cảnh báo mật khẩu không an toàn phía trên ($y < 190$) và thanh cuộn/chân trang ($y > 530$).
  - Nhắc nhở: Chưa tạo ảnh cắt cúp thật ở bước này.

### 2.6. Nhóm 6: Quản lý tính tạm thời (PROVISIONAL) của crop Hình 3.11 và tính đầy đủ của Hình 3.10
- **Vấn đề R1:** Nguồn ảnh log `pfSense_10` có kích thước cực lớn ($1359 \times 17637\,\text{px}$), tọa độ R1 chưa thể coi là dứt điểm; cần đảm bảo không crop mất cột nhãn mâu thuẫn.
- **Khắc phục R2:**
  - Hình 3.10: Xác nhận vùng cắt giữ trọn vẹn: toàn bộ dòng lệnh Nmap, `Host is up (arp-response)`, cả hai dòng cổng 139 và 445 `filtered / no-response`, địa chỉ MAC và dòng `Nmap done`.
  - Hình 3.11: Đóng nhãn rõ ràng tọa độ crop hiện tại là **PROVISIONAL ONLY**. Bắt buộc người viết phải kiểm tra thị giác trực tiếp vùng log ở bước X7E1 trước khi chốt tọa độ cắt cúp phái sinh. Tuyệt đối không crop bỏ cột Rule để che giấu mâu thuẫn nhãn luật chưa giải quyết.

### 2.7. Nhóm 7: Xóa bỏ tham chiếu tới tài liệu không tồn tại và mã định danh tự phát
- **Vấn đề R1:** Tham chiếu tới tệp `CHAPTER_3_EVIDENCE_INDEX.md` không có trong kho lưu trữ và tự công bố các mã `C-IMG-08` đến `C-IMG-11` là mã đã đăng ký.
- **Khắc phục R2:**
  - Xóa bỏ 100% các tham chiếu tới `CHAPTER_3_EVIDENCE_INDEX.md`.
  - Không tự gán các mã ảnh chưa đăng ký làm stable ID.
  - Tái cấu trúc ma trận luận điểm bám chặt vào: Tệp bằng chứng trực tiếp, Phân loại bằng chứng (`Direct raw`, `Direct visual`, `Metadata/lineage`), Câu văn được phép sử dụng, và Suy diễn bị nghiêm cấm.

### 2.8. Nhóm 8: Đơn giản hóa giải thích thứ tự quy tắc tường lửa
- **Vấn đề R1:** Trình bày lý thuyết tường lửa dài dòng, dùng ngôn từ "bảo đảm tuyệt đối", "hoàn toàn vô hiệu".
- **Khắc phục R2:** Rút gọn và bám sát quan sát thực nghiệm:
  - Chỉ ghi nhận dữ kiện: Quy tắc Block được đặt ở vị trí Dòng 1, nằm phía trên quy tắc Pass baseline ở Dòng 2 trên giao diện `CASE_C_KALI`.
  - Nêu ngắn gọn nguyên tắc đánh giá first-match của bộ lọc pf mà không biến báo cáo thành tài liệu hướng dẫn sử dụng pfSense.

---

## 3. Kết Luận Tự Đánh Giá R2

Bộ 4 tài liệu kế hoạch Case C R2:
1. `work/do-an/CH3_35_CASEC_FIGURE_SELECTION_R1.md`
2. `work/do-an/CH3_35_CASEC_PRESENTATION_PLAN_R1.md`
3. `work/do-an/CH3_35_CASEC_CLAIM_EVIDENCE_MAP_R1.md`
4. `work/do-an/CH3_35_CASEC_PLAN_SELF_REVIEW_R1.md`

đã được hiệu chỉnh hoàn chỉnh, chính xác, khách quan và tuân thủ tuyệt đối các chỉ đạo kỹ thuật tại `prompts/X7E0_R2_CORRECT_CASEC_PLAN.md` và `X7E0_CASEC_PLAN_EXTERNAL_REVIEW_R1.md`.

Trạng thái sẵn sàng:
`X7E0_CASEC_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
