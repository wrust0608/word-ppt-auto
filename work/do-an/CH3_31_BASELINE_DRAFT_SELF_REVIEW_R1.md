# BÁO CÁO TỰ ĐÁNH GIÁ DỰ THẢO MỤC 3.1 BASELINE (CH3_31_BASELINE_DRAFT_SELF_REVIEW_R1)

- **Trạng thái:** `X7A1_CH3_31_BASELINE_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7A1 R2 — Correct Section 3.1 Baseline Draft`
- **Tệp dự thảo được đánh giá:** `work/do-an/CH3_31_BASELINE_DRAFT_R1.md`
- **Branch:** `feature/x7a1-ch3-baseline-draft`
- **R1 Base HEAD:** `9c180faab36738626976665059db507e06954725`

---

## 1. Kiểm Toán Số Lượng Từ (Word Count Audit)

- **Tổng số từ toàn văn bản (kể cả bảng và cú pháp):** 2.033 từ.
- **Số từ văn xuôi (loại trừ các dòng bảng và cú pháp nhúng ảnh):** 1.411 từ.
- **Đánh giá phạm vi độ dài:** Nằm hoàn hảo trong khoảng mục tiêu 1.000–1.500 từ văn xuôi cho Tiểu mục 3.1, đảm bảo tính súc tích, mạch lạc và đúng trọng tâm sau khi lược bỏ đoạn ICMP/ARP và tinh gọn các diễn giải lý thuyết không cần thiết.

---

## 2. Kiểm Toán Cấu Trúc Đề Mục (Heading Audit)

- **Số lượng tiêu đề H2:** Đúng 1 tiêu đề:
  * `## 3.1. Trạng thái baseline trước đo đạc`
- **Số lượng tiêu đề H3:** Đúng 2 tiêu đề:
  * `### 3.1.1. Trạng thái mạng và dịch vụ SMB`
  * `### 3.1.2. Trạng thái bản vá và mốc phục hồi`
- **Số lượng tiêu đề H3 phát sinh ngoài kế hoạch:** 0.
- **Số lượng tiêu đề H4 hoặc tiêu đề phụ khác:** 0.
- **Đoạn văn mở đầu:** Có đúng 1 đoạn văn mở đầu ngắn gọn nằm ngay dưới đề mục `3.1`, xuất hiện cụm từ chuẩn `trạng thái ban đầu (baseline)` tại vị trí phù hợp đầu tiên, tập trung vào vai trò tạo mốc tham chiếu nhất quán thay vì tuyên bố bảo đảm tính khách quan/lặp lại tuyệt đối.

---

## 3. Kiểm Toán Bảng Biểu (Table Audit — Count = 2)

Dự thảo tích hợp đúng 2 bảng số liệu sinh viên độc lập, tuân thủ chặt chẽ kế hoạch trình bày:

1. **Bảng 3.1:** `Bảng 3.1. Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc`
   - Cấu trúc: 3 cột (`Hạng mục | Giá trị ghi nhận | Ghi chú`).
   - Đã điều chỉnh tên hàng: `Cấu hình giao thức SMB Server` (thay cho `Cấu hình phương ngữ SMB cục bộ`), ghi chú nêu rõ cả hai thuộc tính cục bộ đều có giá trị True mà không suy diễn phương ngữ đàm phán từ xa.
   - Hàng hồ sơ tường lửa: ghi nhận `Cả ba hồ sơ Windows Firewall có Enabled=True` thay cho câu từ bảo vệ tuyệt đối.
   - Không chứa tên tệp, Evidence ID, Claim ID, kết quả ICMP hay phán xét hiệu quả/rủi ro.
2. **Bảng 3.2:** `Bảng 3.2. Trạng thái bản vá và mốc phục hồi`
   - Cấu trúc: 3 cột (`Hạng mục | Giá trị ghi nhận | Ghi chú / căn cứ đối chiếu ngắn`).
   - Hàng ngưỡng cập nhật: sử dụng chuẩn xác `ngưỡng phiên bản cập nhật tối thiểu` (loại bỏ chữ "an toàn").
   - Hàng hotfix: sử dụng ngôn từ đóng khung giới hạn trong danh mục quan sát được.
   - Hàng mốc khôi phục: ghi nhận cho cả hai máy ảo ở trạng thái poweroff tại thời điểm xác minh.

---

## 4. Kiểm Toán Hình Ảnh (Figure Audit — Count = 3) & Đường Dẫn Tệp

Dự thảo nhúng đúng 3 hình ảnh phái sinh phục vụ trình bày:

1. **Hình 3.1:**
   - Cú pháp nhúng: `![Hình 3.1. Trạng thái mạng, dịch vụ SMB và các cổng lắng nghe trên Windows Server 2012 R2 trước thực nghiệm](chapter3/presentation/3_1/Hinh_3_1_Network_SMB.png)`
   - Tệp vật lý tồn tại: `work/do-an/chapter3/presentation/3_1/Hinh_3_1_Network_SMB.png` (874x642 px).
2. **Hình 3.2:**
   - Cú pháp nhúng: `![Hình 3.2. Cấu hình Windows Firewall giới hạn nguồn truy cập TCP 139/445 từ trạm Kali Linux](chapter3/presentation/3_1/Hinh_3_2_Firewall.png)`
   - Tệp vật lý tồn tại: `work/do-an/chapter3/presentation/3_1/Hinh_3_2_Firewall.png` (874x642 px).
3. **Hình 3.3:**
   - Cú pháp nhúng: `![Hình 3.3. Phiên bản srv.sys và danh mục hotfix ghi nhận trên Windows Server 2012 R2](chapter3/presentation/3_1/Hinh_3_3_SrvSys_Hotfix.png)`
   - Tệp vật lý tồn tại: `work/do-an/chapter3/presentation/3_1/Hinh_3_3_SrvSys_Hotfix.png` (872x450 px).

---

## 5. Kiểm Toán Báo Cáo Cắt Cúp Hình Ảnh (Crop-Manifest Audit)

- Tệp thuyết minh cắt cúp: `work/do-an/CH3_31_BASELINE_CROP_MANIFEST_R1.md` được giữ nguyên vẹn.
- Toàn bộ 3 tệp ảnh bằng chứng gốc trong `work/do-an/chapter3/evidence/baseline/` được bảo tồn nguyên vẹn (1280x800 px, không can thiệp byte).
- Cả 3 tệp ảnh presentation phái sinh được giữ nguyên vẹn từ R1 (đạt độ sắc nét cao, không có lỗi thị giác).

---

## 6. Ma Trận Đối Chiếu Đoạn Văn – Luận Điểm R2 (Paragraph-to-Claim Audit)

| Vị trí trong dự thảo | Luận điểm kế thừa | Nội dung thực tế trong văn bản R2 | Đánh giá ranh giới câu từ R2 |
|---|---|---|---|
| Đoạn mở đầu Mục 3.1 | Khái quát mốc xuất phát | Nêu vai trò mốc tham chiếu nhất quán để đối chiếu các phép đo tiếp theo | Đã bỏ tuyên bố bảo đảm lặp lại/khách quan |
| Đoạn 1 Tiểu mục 3.1.1 | `BASE-C01`, `BASE-C02`, `BASE-C03` | Cấu hình IP Kali (.56.10), Windows (.56.20), card Host-Only, không default route | Giới hạn đường truyền trong phân đoạn lab; không dùng "hoàn toàn cô lập" |
| Đoạn ICMP/ARP | `BASE-C04` | **Đã xóa toàn bộ khỏi văn bản báo cáo sinh viên** | Phù hợp khuyến nghị Reviewer R1; mã claim nội bộ vẫn lưu ở Claim Map |
| Đoạn 2 Tiểu mục 3.1.1 | `BASE-C05`, `BASE-C06`, `BASE-C07`, `BASE-C08` | LanmanServer Running/Automatic, FS-SMB1 Installed, cờ SMB1/SMB2 True (cục bộ), ký số False (cục bộ), netstat 139/445 Listen | Nêu rõ đây là cờ cấu hình cục bộ; không suy diễn đàm phán phương ngữ hay ký số từ xa; không dùng nhãn "SMB2/SMB3" |
| Bảng 3.1 & Câu dẫn | `BASE-C01` đến `BASE-C10` | Bảng thông số mạng, dịch vụ và tường lửa | Trình bày dữ liệu quan sát trực tiếp, không chứa thuật ngữ kiểm toán |
| Câu dẫn & Hình 3.1 | Kế hoạch bố trí Hình 3.1 | Dẫn nhập cửa sổ PowerShell tổng hợp cấu hình mạng và dịch vụ | Dẫn nhập chuẩn trước hình ảnh |
| Đoạn sau Hình 3.1 | `BASE-C08` | Socket 139/445 ở trạng thái Listen; trạng thái lắng nghe cục bộ không tự xác định trạng thái cổng nhìn từ Kali | Đã loại bỏ hoàn toàn cụm từ "tường lửa trung gian" |
| Đoạn tường lửa 3.1.1 | `BASE-C09`, `BASE-C10` | 3 profile Enabled=True, 16 luật chia sẻ tệp False, luật tùy biến Inbound Allow TCP 139/445 từ nguồn .56.10 | Chỉ mô tả cấu hình; không tuyên bố lưu lượng chắc chắn đi qua hay chặn toàn bộ IP khác |
| Câu dẫn & Hình 3.2 | Kế hoạch bố trí Hình 3.2 | Dẫn nhập thuộc tính quy tắc tường lửa tùy biến và hồ sơ tường lửa | Dẫn nhập chuẩn trước hình ảnh |
| Đoạn sau Hình 3.2 | `BASE-C10` | Xác nhận quy tắc tùy biến được cấu hình cho .56.10; khả năng tiếp cận dịch vụ từ Kali được kiểm tra ở phần tiếp theo | Tuân thủ nguyên văn câu văn đóng khung ranh giới theo yêu cầu Reviewer R1 |
| Đoạn 1 Tiểu mục 3.1.2 | `BASE-C11` | Chuỗi hiển thị FileVersion 6.3.9600.16384 của srv.sys | Đã loại bỏ lý thuyết tổng quát về chuỗi RTM tĩnh; chỉ nêu giá trị quan sát |
| Đoạn 2 Tiểu mục 3.1.2 | `BASE-C12`, `BASE-C13` | Phiên bản số nhị phân 6.3.9600.16421; ngưỡng cập nhật tối thiểu 6.3.9600.18604 theo MS17-010 và Support 4023262 | Dùng "ngưỡng phiên bản đã cập nhật tối thiểu" (bỏ "an toàn"); trích dẫn nguồn tự nhiên |
| CITE-ANCHOR | `S005`, `S032` | `<!-- CITE-ANCHOR: S005, S032; final IEEE numbering deferred to global normalization gate -->` | Đặt đúng comment không render; loại bỏ các nhãn số [4]/[5] sai ngữ cảnh toàn cục |
| Đoạn 3 Tiểu mục 3.1.2 | `BASE-C14` | Danh mục Get-HotFix 6 mục năm 2014; không ghi nhận KB4012213, KB4012216 hoặc bản thay thế | Đã loại bỏ cụm "hoàn toàn không xuất hiện"; dùng ngôn từ đóng khung quan sát được |
| Đoạn 4 Tiểu mục 3.1.2 | `BASE-C15` | UNPATCHED là phân loại trạng thái bản vá cục bộ và không tự tạo ra phán quyết lỗ hổng từ xa | Rút gọn ranh giới, không phân tích gói tin khai thác sâu ở Mục 3.1 |
| Đoạn 5 Tiểu mục 3.1.2 | `BASE-C16` | Snapshot Before Demo ghi nhận cho cả hai máy ảo ở trạng thái poweroff làm mốc phục hồi | Đã loại bỏ tuyên bố bảo đảm tái lập hoàn toàn/đồng nhất |
| Bảng 3.2 & Câu dẫn | `BASE-C11` đến `BASE-C16` | Bảng trạng thái bản vá và mốc phục hồi | Đối chiếu rõ ràng, súc tích |
| Câu dẫn & Hình 3.3 | Kế hoạch bố trí Hình 3.3 | Dẫn nhập thuộc tính driver srv.sys và bảng hotfix | Dẫn nhập chuẩn trước hình ảnh |
| Đoạn sau Hình 3.3 | `BASE-C11`, `BASE-C12`, `BASE-C14` | Hai nhóm dữ liệu phiên bản và hotfix dùng cùng ngưỡng Microsoft để phân loại bản vá cục bộ | Đã thay thế câu tự đánh giá phương pháp bằng phát biểu khách quan |
| Đoạn kết Tiểu mục 3.1 | Chuyển tiếp ý niệm sang 3.2 | Trên cơ sở trạng thái baseline này, Mục 3.2 trình bày các kết quả khảo sát SMB từ trạm Kali Linux | Câu chuyển tiếp trung tính, không khẳng định hệ thống "sẵn sàng" như kết quả kỹ thuật |

---

## 7. Rà Soát Tìm Kiếm Ranh Giới Kỹ Thuật R2 (Technical-Boundary Search Audit)

| Tiêu chí kiểm tra | Biểu thức tìm kiếm | Kết quả thực tế | Đánh giá |
|---|---|---|---|
| Suy diễn phương ngữ từ cờ cục bộ | `SMB2/SMB3` | **0 lần xuất hiện** | ĐẠT |
| Thuật ngữ tường lửa sai bản chất | `tường lửa trung gian` | **0 lần xuất hiện** | ĐẠT |
| Tuyên bố đảm bảo lưu lượng/loại trừ | `chắc chắn đi qua`, `chấp thuận đi qua`, `bảo đảm trạm kiểm thử có thể tương tác`, `loại trừ nguy cơ` | **0 lần xuất hiện** | ĐẠT |
| Dán nhãn an toàn cho ngưỡng kỹ thuật | `ngưỡng an toàn` | **0 lần xuất hiện** | ĐẠT |
| Khẳng định lịch sử cập nhật tuyệt đối | `hoàn toàn không xuất hiện` | **0 lần xuất hiện** | ĐẠT |
| Tuyên bố tái lập hoàn toàn | `tái lập hoàn toàn`, `bảo đảm tính toàn vẹn`, `trạng thái đồng nhất` | **0 lần xuất hiện** | ĐẠT |
| Nhãn trích dẫn số [4]/[5] sai ngữ cảnh | `[4]`, `[5]` trong văn xuôi hiển thị | **0 lần xuất hiện** | ĐẠT |
| Comment neo trích dẫn không render | `CITE-ANCHOR: S005, S032` | **Đúng 1 lần xuất hiện** | ĐẠT |
| Mã kiểm toán/nội bộ trong văn xuôi | `BL-*`, `BASE-C*`, `ENV-CORE-*`, `Evidence ID`, `Claim ID` | **0 lần xuất hiện** | ĐẠT |
| Thuật ngữ quản trị trong văn xuôi | `canonical`, `truth matrix`, `gate`, `Single Source of Truth`, `kiểm toán`, `audit` | **0 lần xuất hiện** | ĐẠT |
| Tuyên bố cô lập mạng tuyệt đối | `hoàn toàn cô lập`, `tuyệt đối`, `ngăn chặn hoàn toàn Internet` | **0 lần xuất hiện** | ĐẠT |
| Nhãn đánh giá chủ quan dịch vụ | `hoạt động bình thường` | **0 lần xuất hiện** | ĐẠT |
| Quy kết trạng thái cổng sai ranh giới | `remote OPEN`, gán `IP tĩnh` | **0 lần xuất hiện** | ĐẠT |

---

## 8. Kiểm Toán Neo Trích Dẫn & Hoãn Đánh Số IEEE (Citation Anchor Audit)

- **Căn cứ nguồn tài liệu Microsoft:**
  * `S005`: Microsoft Security Bulletin MS17-010 (ánh xạ bản vá KB4012213 / KB4012216).
  * `S032`: Microsoft Support Article 4023262 "How to verify that MS17-010 is installed" (ngưỡng phiên bản srv.sys tối thiểu 6.3.9600.18604 cho Windows Server 2012 R2).
- **Hiện trạng toàn cục dự án:**
  * Danh mục tài liệu tham khảo Chương 1 hiện tại gán: `[4]` = Microsoft SMB security enhancements; `[5]` = Microsoft SMB signing; `[7]` = MS17-010 bulletin.
  * Nguồn `S032` chưa có số hiệu IEEE toàn cục chính thức.
  * Do đó, việc dùng nhãn hiển thị `[4]` và `[5]` trong R1 là không tương thích với danh mục tài liệu toàn cục.
- **Biện pháp xử lý R2:**
  * Đã xóa toàn bộ nhãn số `[4]` và `[5]` khỏi văn xuôi hiển thị.
  * Tên các tài liệu Microsoft được diễn đạt tự nhiên trong câu văn học thuật.
  * Đặt duy nhất một neo trích dẫn nội bộ dạng chú thích Markdown không render:
    `<!-- CITE-ANCHOR: S005, S032; final IEEE numbering deferred to global normalization gate -->`
  * Số hiệu trích dẫn số chính thức sẽ được chuẩn hóa đồng bộ tại cổng chuẩn hóa IEEE toàn đồ án (X11).

---

## 9. Đánh Giá Khách Quan Về Ranh Giới (Objective Boundary Assessment)

- Bản tự đánh giá R2 không tự xưng "100% technical perfection" mà báo cáo trung thực các ranh giới đã hiệu chỉnh:
  * Ranh giới giữa cấu hình cờ cục bộ và đàm phán mạng từ xa đã được tách biệt dứt khoát.
  * Ranh giới giữa cấu hình tường lửa và hành vi truyền gói tin thực tế được bảo toàn (chờ đo đạc ở Mục 3.2).
  * Ranh giới giữa phân loại bản vá cục bộ (UNPATCHED) và khả năng khai thác lỗ hổng từ xa được đóng khung nghiêm ngặt.
  * Đoạn ICMP/ARP đã được lược bỏ khỏi bài viết để tránh làm loãng mạch thông tin cục bộ.
- Dự thảo R2 đã giải quyết toàn diện 7 Blocker (A đến G) và vấn đề trích dẫn nêu trong Báo cáo Thẩm tra Độc lập R1.

---

**KẾT LUẬN TỰ ĐÁNH GIÁ:**
Dự thảo Mục 3.1 R2 đạt trạng thái:
`X7A1_CH3_31_BASELINE_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
