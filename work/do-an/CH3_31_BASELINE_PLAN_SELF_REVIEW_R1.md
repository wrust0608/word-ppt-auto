# BÁO CÁO TỰ ĐÁNH GIÁ KẾ HOẠCH BẰNG CHỨNG MỤC 3.1 BASELINE R2 (CH3_31_BASELINE_PLAN_SELF_REVIEW_R1)

- **Trạng thái:** `X7A0_BASELINE_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7A0 R2 — Correct Baseline Evidence & Presentation Plan`
- **Ngày thực hiện:** 2026-10-06
- **Ghi chú chuẩn mực:** Báo cáo này trình bày kết quả tự rà soát kỹ thuật khách quan của phiên bản R2 theo quy trình hai bước (Two-Pass Policy) sau khi tiếp thu đầy đủ các yêu cầu trong báo cáo đánh giá ngoài `X7A0_BASELINE_PLAN_EXTERNAL_REVIEW_R1.md`. Tác giả không tự ý công bố `PASS`; kết quả nghiệm thu cuối cùng phụ thuộc vào đánh giá ngoài (External Review) và sự phê duyệt của người dùng.

---

## 1. Bảng Chỉ Số Thống Kê Tổng Hợp R2 (Summary Metrics)

| Chỉ số kiểm tra (Audit Metric) | Số lượng thực tế | Ghi chú chi tiết |
|---|:---:|---|
| **Tổng số ảnh chụp màn hình baseline đã thẩm tra** | **13** | Thẩm tra 100% tệp PNG trong `work/do-an/chapter3/evidence/baseline/` |
| **Số lượng ảnh phân loại KEEP (Giữ lại)** | **3** | `Windows_PreDemo_01_Network_SMB.png`, `Windows_PreDemo_02_Firewall.png`, `Windows_MS17010_02_Hotfix.png` |
| **Số lượng ảnh phân loại OPTIONAL (Dự phòng)** | **3** | `Windows_MS17010_01_SrvSysVersion.png`, `Kali_to_Windows_Connectivity.png`, `Windows_FirewallPrep_04_Scope.png` |
| **Số lượng ảnh phân loại DROP (Loại bỏ)** | **7** | `Kali_PreDemo_01`, `Kali_PreDemo_02`, `Windows_Baseline_01`, `04`, `05`, `06`, `07` |
| **Số lượng bảng biểu đề xuất cho Mục 3.1** | **2** | Bảng 3.1 (Mạng, SMB và Tường lửa) và Bảng 3.2 (Bản vá và Mốc phục hồi) |
| **Số lượng hình ảnh đề xuất cho Mục 3.1** | **3** | Hình 3.1 (Mạng & SMB), Hình 3.2 (Quy tắc tường lửa), Hình 3.3 (srv.sys & Danh mục bản vá) |
| **Số lượng luận điểm ánh xạ (Claim-Map Rows)** | **16** | 16 claims (`BASE-C01` đến `BASE-C16`), 100% đạt trạng thái `VERIFIED` |
| **Số lượng mã Stable Evidence ID thuộc nhóm `BL-*`** | **0** | Đã loại bỏ 100% mã BL-*; chuyển đổi toàn bộ sang `ENV-CORE-01` đến `ENV-CORE-05` |
| **Số lượng từ ngữ suy diễn cô lập tuyệt đối** | **0** | Đã loại bỏ hoàn toàn các cụm từ "hoàn toàn cô lập", "ngăn chặn hoàn toàn Internet" |
| **Số lượng nhận định quy kết nguyên nhân ICMP do tường lửa** | **0** | Đã chuyển thành quan sát hiện tượng thuần túy: ARP REACHABLE, ICMP 0 phản hồi |
| **Số lượng nhận định sức khỏe dịch vụ ("hoạt động bình thường")** | **0** | Đã chuyển sang ghi nhận trạng thái kỹ thuật: Running / Automatic |
| **Số lượng tệp bằng chứng kịch bản khác bị rò rỉ** | **0** | Đảm bảo cách ly 100% bằng chứng mốc xuất phát baseline |
| **Số lượng tệp văn xuôi Mục 3.1 bị tạo trước** | **0** | Tuân thủ tuyệt đối quy tắc ZERO PROSE của pha lập kế hoạch Pass 0 |

---

## 2. Thẩm Tra Cấu Trúc Đề Mục H3 Và Bảng Biểu Sinh Viên (Student-Facing Presentation Audit)

Kế hoạch R2 đã khắc phục triệt để các hạn chế của bản R1 về tính chất kiểm toán nội bộ và định dạng cồng kềnh:

1. **Chuẩn hóa đề mục H3 ngắn gọn:**
   - Sử dụng chính xác 2 tiêu đề ngắn gọn theo chuẩn học thuật:
     * `3.1.1. Trạng thái mạng và dịch vụ SMB`
     * `3.1.2. Trạng thái bản vá và mốc phục hồi`
   - Loại bỏ hoàn toàn các từ ngữ kiểm toán ("kiểm toán", "Single Source of Truth") và phụ đề tiếng Anh khỏi tiêu đề đề mục.

2. **Thiết kế 2 bảng báo cáo sinh viên độc lập:**
   - Thay thế bảng 16 hàng 5 cột cồng kềnh bằng 2 bảng gọn nhẹ, phù hợp khổ in A4 portrait:
     * **Bảng 3.1:** *Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc* (Cột: `Hạng mục | Giá trị ghi nhận | Ghi chú`).
     * **Bảng 3.2:** *Trạng thái bản vá và mốc phục hồi* (Cột: `Hạng mục | Giá trị ghi nhận | Ghi chú / căn cứ đối chiếu ngắn`).
   - Loại bỏ 100% tên tệp bằng chứng, mã Evidence ID/Claim ID và cột đánh giá rủi ro/hiệu quả khỏi thiết kế bảng hiển thị cho sinh viên.
   - Lược bỏ hàng thử nghiệm ICMP nhận 0 phản hồi khỏi bảng chính để tránh gây nhiễu và tránh quy kết nguyên nhân chủ quan.

---

## 3. Thẩm Tra Chuyên Sâu Trạng Thái Bản Vá (Patch-State Special Audit)

Kế hoạch R2 tiếp tục bảo tồn và siết chặt các ranh giới kỹ thuật cốt lõi:

1. **Phân định rõ rệt giữa chuỗi hiển thị và phiên bản số nhị phân:**
   - Chuỗi `FileVersion String` hiển thị: `6.3.9600.16384 (winblue_rtm.130821-1623)`.
   - Giá trị phiên bản số nhị phân cấu thành từ 4 trường (`FileMajorPart.FileMinorPart.FileBuildPart.FilePrivatePart`): `6.3.9600.16421`.
2. **Cơ sở đối chiếu toán học:**
   - Phép so sánh toán học trực tiếp với tài liệu Microsoft được thực hiện trên phiên bản số nhị phân: `6.3.9600.16421 < 6.3.9600.18604`.
   - Ngưỡng tối thiểu `6.3.9600.18604` được chứng thực từ tài liệu hỗ trợ chính thức của Microsoft (Article ID 4023262, Source ID: `S032`).
3. **Mã bản vá áp dụng chính xác cho Windows Server 2012 R2:**
   - Bản vá bảo mật độc lập: `KB4012213` (Security Only).
   - Bản cập nhật tích lũy hàng tháng: `KB4012216` (Monthly Rollup).
   - Tuyệt đối không xuất hiện các mã bản vá của hệ điều hành khác (`KB4012212`, `KB4012215` = 0).
4. **Kiểm kê danh mục bản vá ghi nhận được (Hotfix Inventory):**
   - Lệnh `Get-HotFix` ghi nhận 6 bản vá hệ thống từ ngày 21/03/2014 (KB2919355, KB2919442, KB2937220, KB2938772, KB2939471, KB2949621).
   - Danh mục ghi nhận không chứa KB4012213, KB4012216 hoặc bản vá thay thế chứa bản sửa lỗi MS17-010. Không suy diễn rằng nắm rõ toàn bộ lịch sử cài đặt trọn đời ngoài danh mục quan sát được.
5. **Cơ sở xác lập phán quyết `UNPATCHED`:**
   - Kết luận `UNPATCHED` được xác lập dựa trên bộ ba căn cứ: **numeric local version + observed hotfix inventory + official Microsoft mapping**.
   - **Ranh giới nghiêm ngặt:** Tuyệt đối không đưa chữ "UNPATCHED" trực tiếp vào tiêu đề Hình 3.3. Ảnh chụp màn hình một mình KHÔNG tự chứng minh trạng thái UNPATCHED nếu không đối chiếu chéo với bảng kiểm kê bản vá và tài liệu chính thức của Microsoft.
   - Trạng thái chưa vá cục bộ của hệ điều hành độc lập với tín hiệu quét từ xa qua mạng và không đồng nghĩa với việc lỗ hổng chắc chắn bị khai thác thành công qua mạng.

---

## 4. Thẩm Tra Tính Cách Ly Bằng Chứng (Evidence-Isolation Audit)

- **Các tệp được sử dụng:** Chỉ sử dụng duy nhất các tệp bằng chứng thuộc thư mục `work/do-an/chapter3/evidence/baseline/`:
  * Các tệp văn bản kiểm toán: `Final_PreDemo_Audit.txt`, `Before_Demo_Snapshots.txt`, `MS17-010_Official_Mapping.txt`, `VirtualBox_HostOnly_Config.txt`, `Windows_FirewallPrep_Final.txt`.
  * Các ảnh chụp màn hình baseline tương ứng.
  * Tài liệu tham chiếu ngoài: `S032`, `S005` từ `SOURCE_LEDGER.md`.
- **Cách ly với các kịch bản khác:**
  * Tuyệt đối không sử dụng bất kỳ tệp dữ liệu nào từ `scenario1/` (B2–B6 Nmap discovery).
  * Không sử dụng dữ liệu từ `scenario2/` (NSE scripts).
  * Không sử dụng dữ liệu từ `case_b/` (vô hiệu hóa SMBv1).
  * Không sử dụng dữ liệu từ `case_c/` (pfSense bridge).
  * Không đưa ra bất kỳ kết luận hay nhận định phân tích rủi ro/khuyến nghị nào thuộc phạm vi Chương 4.

---

## 5. Thẩm Tra Mã Bằng Chứng Ổn Định (Stable Evidence IDs Audit)

- Đã rà soát và loại bỏ 100% các mã tự tạo `BL-*` khỏi `CH3_31_BASELINE_CLAIM_EVIDENCE_MAP_R1.md`.
- Toàn bộ 16 hàng luận điểm chỉ sử dụng duy nhất các mã Stable Evidence ID đã đăng ký trong `EVIDENCE_REGISTER.md`:
  * `ENV-CORE-01`: Kiểm toán tổng hợp mốc xuất phát trước demo (`Final_PreDemo_Audit.txt`, `Windows_PreDemo_01_Network_SMB.png`).
  * `ENV-CORE-02`: Xác thực điểm khôi phục `Before Demo` snapshot (`Before_Demo_Snapshots.txt`).
  * `ENV-CORE-03`: Kiểm tra và đối chiếu trạng thái bản vá MS17-010 cục bộ (`MS17-010_Official_Mapping.txt`, `Windows_MS17010_02_Hotfix.png`).
  * `ENV-CORE-04`: Kiểm toán cấu hình quy tắc tường lửa lab (`Windows_FirewallPrep_Final.txt`, `Windows_PreDemo_02_Firewall.png`).
  * `ENV-CORE-05`: Cấu hình mạng Host-Only Adapter (`VirtualBox_HostOnly_Config.txt`, `Kali_to_Windows_Connectivity.png`).

---

## 6. Thẩm Tra Tính Trùng Lặp & Bố Cục Ảnh R2 (Duplication & Anti-Spam Audit)

- Phân loại ảnh đạt đúng mục tiêu: **KEEP = 3, OPTIONAL = 3, DROP = 7** (tổng số 13 ảnh).
- Bộ ảnh KEEP tối ưu:
  * **Hình 3.1:** `Windows_PreDemo_01_Network_SMB.png` — Cung cấp cái nhìn hợp nhất về mạng, dịch vụ LanmanServer, cờ SMB, cổng lắng nghe 139/445 và phiên bản số srv.sys.
  * **Hình 3.2:** `Windows_PreDemo_02_Firewall.png` — Minh chứng quy tắc tùy biến `ATTT Lab SMB 139-445`, phạm vi địa chỉ nguồn duy nhất `.56.10`, 3 profile True và 16 luật chia sẻ tệp mặc định False.
  * **Hình 3.3:** `Windows_MS17010_02_Hotfix.png` — Tập hợp cả chuỗi FileVersion hiển thị, số nhị phân srv.sys và danh mục 6 hotfix trên cùng một giao diện PowerShell.
- Đã chuyển `Windows_MS17010_01_SrvSysVersion.png` sang OPTIONAL vì Hình 3.3 đã bao hàm toàn bộ thông tin của ảnh này kèm danh mục hotfix, loại bỏ triệt để sự trùng lặp thị giác.
- Chính sách cắt cúp (crop policy) không khóa cứng tọa độ pixel; chỉ mô tả rõ vùng thông tin cần giữ, giao diện thừa loại bỏ, ngữ cảnh bắt buộc bảo tồn và mục đích trình bày.

---

## 7. Các Vấn Đề Trình Bày Sau R2 (Updated Presentation Status)

1. **Vấn đề cấu trúc bảng:** Đã được giải quyết dứt điểm bằng việc tách thành Bảng 3.1 và Bảng 3.2 theo đúng yêu cầu phản biện.
2. **Vấn đề số lượng hình ảnh:** Đã chốt bộ 3 hình KEEP tối ưu, giải quyết trọn vẹn cả nhu cầu minh chứng mạng/dịch vụ, tường lửa và bản vá/hotfix.
3. **Tính sẵn sàng:** Toàn bộ 4 artifact lập kế hoạch của Mục 3.1 đã được hiệu chỉnh đồng bộ, sạch sẽ, không vi phạm ranh giới bằng chứng và sẵn sàng cho đợt thẩm định ngoài cuối cùng.

---

## 8. Trạng Thái Hoàn Thành

Các tài liệu lập kế hoạch cho Mục 3.1 đã hoàn tất hiệu chỉnh R2:
- [`CH3_31_BASELINE_FIGURE_SELECTION_R1.md`](file:///E:/word_ppt-auto/work/do-an/CH3_31_BASELINE_FIGURE_SELECTION_R1.md)
- [`CH3_31_BASELINE_PRESENTATION_PLAN_R1.md`](file:///E:/word_ppt-auto/work/do-an/CH3_31_BASELINE_PRESENTATION_PLAN_R1.md)
- [`CH3_31_BASELINE_CLAIM_EVIDENCE_MAP_R1.md`](file:///E:/word_ppt-auto/work/do-an/CH3_31_BASELINE_CLAIM_EVIDENCE_MAP_R1.md)
- [`CH3_31_BASELINE_PLAN_SELF_REVIEW_R1.md`](file:///E:/word_ppt-auto/work/do-an/CH3_31_BASELINE_PLAN_SELF_REVIEW_R1.md)

**TRẠNG THÁI CUỐI CÙNG:**
`X7A0_BASELINE_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
