# BÁO CÁO TỰ ĐÁNH GIÁ KẾ HOẠCH BẰNG CHỨNG MỤC 3.1 BASELINE (CH3_31_BASELINE_PLAN_SELF_REVIEW_R1)

- **Trạng thái:** `X7A0_BASELINE_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7A0 — Baseline Evidence & Presentation Plan`
- **Ngày thực hiện:** 2026-10-06
- **Ghi chú chuẩn mực:** Báo cáo này trình bày kết quả tự rà soát kỹ thuật khách quan theo quy trình hai bước (Two-Pass Policy). Tác giả không tự ý công bố `PASS`; kết quả nghiệm thu cuối cùng phụ thuộc vào đánh giá ngoài (External Review) và sự phê duyệt của người dùng.

---

## 1. Bảng Chỉ Số Thống Kê Tổng Hợp (Summary Metrics)

| Chỉ số kiểm tra (Audit Metric) | Số lượng thực tế | Ghi chú chi tiết |
|---|:---:|---|
| **Tổng số ảnh chụp màn hình baseline đã thẩm tra** | **13** | Thẩm tra 100% tệp PNG trong `work/do-an/chapter3/evidence/baseline/` |
| **Số lượng ảnh phân loại KEEP (Giữ lại)** | **2** | `Windows_MS17010_01_SrvSysVersion.png`, `Windows_PreDemo_02_Firewall.png` |
| **Số lượng ảnh phân loại OPTIONAL (Dự phòng)** | **3** | `Kali_to_Windows_Connectivity.png`, `Windows_MS17010_02_Hotfix.png`, `Windows_PreDemo_01_Network_SMB.png` |
| **Số lượng ảnh phân loại DROP (Loại bỏ)** | **8** | `Kali_PreDemo_01`, `Kali_PreDemo_02`, `Windows_Baseline_01`, `04`, `05`, `06`, `07`, `Windows_FirewallPrep_04` |
| **Số lượng bảng biểu đề xuất cho Mục 3.1** | **1** | Bảng 3.1 tổng hợp toàn diện (Single Source of Truth) gồm 4 khối tham số |
| **Số lượng hình ảnh đề xuất cho Mục 3.1** | **2** | Hình 3.1 (Thuộc tính srv.sys) và Hình 3.2 (Quy tắc tường lửa tùy biến) |
| **Số lượng luận điểm ánh xạ (Claim-Map Rows)** | **16** | 16 claims (`BASE-C01` đến `BASE-C16`), đạt tỷ lệ 100% VERIFIED |
| **Số lượng tệp bằng chứng khác kịch bản bị rò rỉ** | **0** | Đảm bảo cách ly tuyệt đối 100% bằng chứng baseline |
| **Số lượng tệp văn xuôi Mục 3.1 bị tạo trước** | **0** | Tuân thủ tuyệt đối quy tắc ZERO PROSE của pha Pass 0 |

---

## 2. Thẩm Tra Chuyên Sâu Trạng Thái Bản Vá (Patch-State Special Audit)

Kế hoạch trình bày đã bảo tồn nghiêm ngặt và đầy đủ các ranh giới kỹ thuật về trạng thái bản vá MS17-010:

1. **Phân định rõ rệt giữa chuỗi hiển thị và phiên bản số nhị phân:**
   - Chuỗi `FileVersion String` ghi nhận từ giao diện: `6.3.9600.16384 (winblue_rtm.130821-1623)`.
   - Giá trị phiên bản số nhị phân thực tế cấu thành từ 4 trường (`FileMajorPart.FileMinorPart.FileBuildPart.FilePrivatePart`): `6.3.9600.16421`.
2. **Giá trị so sánh toán học:**
   - Phép so sánh toán học trực tiếp với tài liệu của Microsoft được thực hiện trên phiên bản số nhị phân: `6.3.9600.16421 < 6.3.9600.18604`.
   - Ngưỡng tối thiểu `6.3.9600.18604` được chứng thực từ nguồn tài liệu hỗ trợ chính thức của Microsoft (Article ID 4023262, Source ID: `S032`).
3. **Mã bản vá áp dụng chính xác cho Windows Server 2012 R2:**
   - Gói cập nhật bảo mật độc lập: `KB4012213` (Security Only).
   - Gói cập nhật tích lũy hàng tháng: `KB4012216` (Monthly Rollup).
   - Tuyệt đối không xuất hiện các mã bản vá của các hệ điều hành khác (`KB4012212`, `KB4012215` = 0 lượt).
4. **Kiểm kê danh mục bản vá cài đặt (Hotfix Inventory):**
   - Lệnh `Get-HotFix` ghi nhận 6 bản vá hệ thống (KB2919355, KB2919442, KB2937220, KB2938772, KB2939471, KB2949621) đều được cài đặt vào ngày 21/03/2014.
   - Hệ thống hoàn toàn vắng mặt KB4012213, KB4012216 cũng như các bản cập nhật tích lũy thay thế sau năm 2014.
5. **Cơ sở xác lập phán quyết `UNPATCHED`:**
   - Kết luận `UNPATCHED` được xác lập dựa trên bộ ba căn cứ kỹ thuật khách quan: **numeric local version + observed hotfix inventory + official Microsoft mapping**.
   - **Ranh giới bắt buộc:** Ảnh chụp màn hình `srv.sys` một mình KHÔNG tự chứng minh trạng thái UNPATCHED nếu không đối chiếu chéo với bảng kiểm kê bản vá và tài liệu chính thức của Microsoft.
   - Trạng thái chưa vá cục bộ của hệ điều hành độc lập với tín hiệu quét từ xa qua mạng và không đồng nghĩa với việc lỗ hổng chắc chắn bị khai thác thành công qua mạng.

---

## 3. Thẩm Tra Tính Cách Ly Bằng Chứng (Evidence-Isolation Audit)

- **Các tệp được sử dụng:** Chỉ sử dụng duy nhất các tệp bằng chứng thuộc thư mục `work/do-an/chapter3/evidence/baseline/`:
  * 5 tệp văn bản kiểm toán: `Final_PreDemo_Audit.txt`, `Before_Demo_Snapshots.txt`, `MS17-010_Official_Mapping.txt`, `VirtualBox_HostOnly_Config.txt`, `Windows_FirewallPrep_Final.txt`.
  * Các ảnh chụp màn hình baseline tương ứng.
  * Tài liệu tham chiếu ngoài: `S032`, `S005` từ `SOURCE_LEDGER.md`.
- **Cách ly với các kịch bản khác:**
  * Không sử dụng bất kỳ tệp dữ liệu nào từ `scenario1/` (B2–B6 Nmap discovery).
  * Không sử dụng dữ liệu từ `scenario2/` (NSE scripts).
  * Không sử dụng dữ liệu từ `case_b/` (vô hiệu hóa SMBv1).
  * Không sử dụng dữ liệu từ `case_c/` (pfSense bridge).
  * Không đưa ra bất kỳ kết luận hay nhận định phân tích rủi ro nào thuộc phạm vi Chương 4.

---

## 4. Thẩm Tra Tính Trùng Lặp & Tối Ưu Bố Cục (Duplication & Anti-Spam Audit)

- Đã chủ động loại bỏ 8/13 ảnh chụp màn hình có nội dung thưa thớt, bố cục rời rạc hoặc chỉ hiển thị văn bản tĩnh/lệnh đơn lẻ.
- Tích hợp toàn diện các tham số vào Bảng 3.1 giúp tài liệu cô đọng, người đọc nắm bắt toàn bộ 16 tham số cốt lõi trong một bảng tra cứu duy nhất.
- Hai hình ảnh được đề xuất giữ lại (`Hình 3.1` và `Hình 3.2`) đáp ứng tiêu chí cao nhất về tính độc bản thị giác, giải quyết hai câu hỏi then chốt: thuộc tính phiên bản driver nhị phân và chính sách tường lửa cô lập truy cập từ trạm Kali.
- Đã đề xuất phương án cắt cúp cụ thể cho cả hai hình nhằm loại bỏ các vùng không gian trống của màn hình desktop Server Manager, tăng tối đa kích thước font chữ khi chèn vào bản in Word A4.

---

## 5. Những Vấn Đề Trình Bày Mở Xin Ý Kiến Người Phản Biện (Unresolved Presentation Questions)

1. **Cấu trúc Bảng 3.1 (Gom cụm hay tách đôi):**
   - *Phương án A (Hiện tại - Khuyến nghị):* Giữ nguyên Bảng 3.1 là một bảng tổng hợp lớn gồm 4 khối tham số (Hạ tầng mạng, Dịch vụ SMB, Tường lửa, Bản vá & Mốc phục hồi) để tạo ra một "Bảng sự thật duy nhất" (Single Source of Truth) toàn diện ở đầu chương.
   - *Phương án B:* Tách thành 2 bảng riêng biệt: Bảng 3.1 (Hạ tầng mạng & Dịch vụ SMB, đặt tại 3.1.1) và Bảng 3.2 (Chính sách tường lửa, Trạng thái bản vá & Snapshot, đặt tại 3.1.2).  
   *Ý kiến đề xuất:* Phương án A mạch lạc hơn và tiết kiệm không gian tiêu đề bảng.
2. **Số lượng hình ảnh chính thức (2 hay 3 hình):**
   - Hiện tại đề xuất 2 hình (`Hình 3.1`: srv.sys version và `Hình 3.2`: Firewall rule).
   - Nếu người phản biện mong muốn có thêm minh chứng về tính thông mạng L2 giữa Kali và Windows dù ICMP ping bị chặn (100% loss), tệp `Kali_to_Windows_Connectivity.png` có thể được đưa vào làm `Hình 3.3` (tạm thời) sau khi crop cửa sổ terminal.  
   *Ý kiến đề xuất:* Giữ 2 hình là tối ưu, thông số L2 ARP Reachable đã được phản ánh đầy đủ trong Bảng 3.1.

---

## 6. Trạng Thái Hoàn Thành

Tất cả các tài liệu theo yêu cầu của pha `X7A0` đã được tạo lập đầy đủ, nhất quán và tuân thủ 100% quy tắc kỹ thuật:
- [`CH3_31_BASELINE_FIGURE_SELECTION_R1.md`](file:///E:/word_ppt-auto/work/do-an/CH3_31_BASELINE_FIGURE_SELECTION_R1.md)
- [`CH3_31_BASELINE_PRESENTATION_PLAN_R1.md`](file:///E:/word_ppt-auto/work/do-an/CH3_31_BASELINE_PRESENTATION_PLAN_R1.md)
- [`CH3_31_BASELINE_CLAIM_EVIDENCE_MAP_R1.md`](file:///E:/word_ppt-auto/work/do-an/CH3_31_BASELINE_CLAIM_EVIDENCE_MAP_R1.md)
- [`CH3_31_BASELINE_PLAN_SELF_REVIEW_R1.md`](file:///E:/word_ppt-auto/work/do-an/CH3_31_BASELINE_PLAN_SELF_REVIEW_R1.md)

**TRẠNG THÁI CUỐI CÙNG:**  
`X7A0_BASELINE_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`
