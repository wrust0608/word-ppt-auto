# MA TRẬN CHUYỂN DỊCH NỘI DUNG CHƯƠNG 3 (CH3 REDESIGN CONTENT MIGRATION MAP R1)

- **Cổng trạng thái:** `R3-0_READY_FOR_EXTERNAL_REVIEW`
- **Tài liệu căn cứ lộ trình:** `work/do-an/ROADMAP_CH3_REDESIGN_EVIDENCE_FIRST_2026_10_07.md`
- **Tài liệu kiến trúc cơ sở:** `work/do-an/CH3_REDESIGN_EVIDENCE_VISUAL_BLUEPRINT_R1.md`
- **Sổ đăng ký bảng/hình:** `work/do-an/CH3_REDESIGN_TABLE_FIGURE_LEDGER_R1.md`
- **Bản thảo nguồn cần chuyển dịch:** `work/do-an/CHAPTER_3_DRAFT_R2.md` (318 dòng văn bản đã được phê duyệt ở kiến trúc cũ)
- **Nhánh làm việc canonical:** `feature/ch3-redesign-evidence-first-r1`
- **Commit khởi tạo:** `170aa24293b2cf8e579abb1ecf60920bca418bd9`
- **Mục tiêu tài liệu:** Thiết lập bản đồ chuyển dịch từng khối nội dung (Block-by-Block Migration Map) từ cấu trúc cũ sang 8 đề mục Chương 3 mới (3.1 đến 3.8); chỉ định rõ hành động xử lý cho từng đoạn văn, lý do biến đổi, các tiên đề kỹ thuật được bảo toàn và chiến lược nâng cấp văn phong giúp người đọc không chuyên vẫn nắm bắt mạch lạc câu chuyện khoa học.

---

## 1. NGUYÊN TẮC CHUYỂN DỊCH NỘI DUNG (MIGRATION PRINCIPLES)

1. **Bảo tồn chân lý kỹ thuật, tái cấu trúc kiến trúc diễn ngôn:**
   - Việc phê duyệt bản thảo cũ (`CHAPTER_3_DRAFT_R2.md`) bảo vệ tính xác thực của các dữ kiện kỹ thuật (technical truth) và bằng chứng đo đạc; việc người dùng mở lại (reopen) kiến trúc Chương 3 cho phép viết lại cách kể chuyện (narrative) và tổ chức lại các đề mục mà không làm mất đi bất kỳ sự thật khoa học nào.
   - Cấm tự ý sửa đổi số liệu, địa chỉ IP, cờ giao thức, phiên bản driver, hoặc làm sai lệch kết quả đo đạc.
2. **Hệ thống nhãn hành động chuẩn mực (Action Tags):**
   - `REUSE`: Giữ nguyên dữ kiện kỹ thuật và cấu trúc lập luận cốt lõi, tinh chỉnh văn phong cho tự nhiên và chuẩn mực tiếng Việt học thuật.
   - `MOVE`: Chuyển nguyên khối nội dung hoặc bảng biểu sang đề mục mới tương ứng trong cấu trúc 8 phần.
   - `REWRITE`: Viết lại cách diễn đạt, thay đổi góc nhìn từ "nhật ký thực thi lệnh" sang "dẫn dắt câu chuyện khoa học giải đáp câu hỏi của người đọc".
   - `MERGE`: Gộp các đoạn phân mảnh hoặc các kết quả đo tương đồng vào một khối thống nhất để tăng tính liên kết.
   - `TRIM`: Lược bỏ các diễn đạt rườm rà, các đoạn lặp lại suy diễn, hoặc các mô tả mang tính liệt kê giao thức không cần thiết.
   - `RETIRE FROM MAIN NARRATIVE`: Đưa các chi tiết bổ trợ hoặc các ảnh cấu hình trùng lặp ra khỏi mạch đọc chính, lưu giữ đầy đủ ở tầng đối soát và kho bằng chứng bổ trợ (supporting evidence).
   - `TECHNICAL SOURCE ONLY`: Dữ liệu chỉ dùng làm căn cứ đối chiếu và kiểm toán kỹ thuật ngầm, không biến thành văn bản diễn giải trực tiếp.
3. **Mô hình nhịp điệu diễn ngôn cho từng phần (5-Beat Narrative Rhythm):**
   Mỗi đề mục trong cấu trúc mới sau này khi viết ở gate R3-1 bắt buộc phải tuân thủ nhịp điệu 5 bước:
   $$\text{Câu hỏi người đọc} \longrightarrow \text{Bằng chứng đo đạc} \longrightarrow \text{Kết quả quan sát trực tiếp} \longrightarrow \text{Ý nghĩa kỹ thuật trực tiếp} \longrightarrow \text{Cầu nối logic}$$

---

## 2. MA TRẬN ÁNH XẠ TỔNG THỂ CÁC ĐỀ MỤC (SECTION-LEVEL MIGRATION)

| Đề mục cấu trúc cũ (Old Sections) | Tên đề mục cũ | Đề mục cấu trúc mới (New Sections) | Tên đề mục mới đề xuất | Chiến lược chuyển dịch chính |
|---|---|---|---|---|
| *Chưa có đề mục tương ứng* | *Nằm rải rác ở lời mở đầu và Chương 2* | **3.1. Mục tiêu và tổ chức thực nghiệm**<br>• 3.1.1. Mục tiêu kiểm chứng<br>• 3.1.2. Luồng thực nghiệm | Mục tiêu kiểm chứng và Luồng thực nghiệm | **NEW & REWRITE**: Xây dựng phần dẫn nhập chiến lược, giải thích rõ mục tiêu kiểm chứng an toàn (không exploit) và sơ đồ luồng 6 giai đoạn (Hình 3.1 mới). |
| **3.1. Trạng thái baseline trước đo đạc**<br>• 3.1.1. Trạng thái mạng và dịch vụ SMB<br>• 3.1.2. Trạng thái bản vá và mốc phục hồi | Trạng thái baseline trước đo đạc | **3.2. Xác lập trạng thái ban đầu của hệ thống**<br>• 3.2.1. Trạng thái mạng và dịch vụ SMB<br>• 3.2.2. Trạng thái bản vá MS17-010 | Xác lập trạng thái ban đầu của hệ thống | **MOVE & RESTRUCTURE**: Tách bạch rõ ràng giữa trạng thái mạng/dịch vụ (3.2.1) và trạng thái bản vá nội bộ UNPATCHED (3.2.2); tối ưu hóa hình ảnh sang Hình 3.2 và Hình 3.3. |
| **3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB**<br>• 3.2.1. Khảo sát trạm mạng và trạng thái mở cổng<br>• 3.2.2. Nhận diện phiên bản và đặc tính giao thức | Khảo sát dịch vụ SMB (Kịch bản 1) | **3.3. Khảo sát dịch vụ SMB từ trạm Kali Linux**<br>• 3.3.1. Phát hiện máy chủ và khả năng tiếp cận SMB<br>• 3.3.2. Nhận diện giao thức và các đặc tính SMB<br>• 3.3.3. Tổng hợp kết quả khảo sát | Khảo sát dịch vụ SMB từ trạm Kali Linux | **MOVE & REWRITE**: Xóa bỏ cách đặt tiêu đề theo mã quy trình B2–B6; xây dựng narrative từ góc nhìn trạm kiểm thử: có máy chủ $\to$ tiếp cận được cổng $\to$ nhận diện phương ngữ $\to$ tổng hợp bảng dữ liệu. |
| **3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010**<br>• 3.3.1. Khảo sát điều kiện kết nối và thuộc tính (NSE01–03)<br>• 3.3.2. Đánh giá dấu hiệu MS17-010 và đối chiếu bản vá (NSE04) | Kiểm tra dấu hiệu MS17-010 (Kịch bản 2) | **3.4. Kiểm tra dấu hiệu MS17-010**<br>• 3.4.1. Kết quả kiểm tra từ xa bằng Nmap/NSE<br>• 3.4.2. Đối chiếu với trạng thái bản vá trên Windows | Kiểm tra dấu hiệu MS17-010 | **MOVE, TRIM & EXPAND**: Tinh giản NSE01–03 làm bối cảnh xác nhận; tập trung phân tích NSE04 (Hình 3.6 UNKNOWN); mở rộng mục 3.4.2 chuyên sâu đối chiếu giữa Remote UNKNOWN và Local UNPATCHED (Hình 3.7 mới). |
| **3.4. Kết quả Case B — Vô hiệu hóa SMBv1**<br>• 3.4.1. Thao tác vô hiệu hóa và kiểm tra cục bộ<br>• 3.4.2. Đo đạc lại từ xa và đối chiếu đa tầng | Vô hiệu hóa SMBv1 (Case B) | **3.5. Thực nghiệm vô hiệu hóa SMBv1 trên máy chủ**<br>• 3.5.1. Trạng thái trước và sau khi vô hiệu hóa SMBv1<br>• 3.5.2. Kết quả kiểm tra lại từ Kali Linux<br>• 3.5.3. Tổng hợp sự thay đổi quan sát được | Thực nghiệm vô hiệu hóa SMBv1 trên máy chủ | **MOVE & RESTRUCTURE**: Tái cấu trúc theo chuỗi hành động trực quan: Trước/Sau nội bộ (3.5.1 với Hình 3.8 3-panel) $\to$ Đo lại từ xa (3.5.2 với Hình 3.9) $\to$ Bảng tổng hợp thay đổi (3.5.3 với Bảng 3.5). |
| **3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense**<br>• 3.5.1. Thiết lập cầu nối và chính sách kiểm soát<br>• 3.5.2. Đo đạc từ xa, đối chiếu nhật ký và trạng thái máy chủ | Kiểm soát SMB bằng pfSense (Case C) | **3.6. Thực nghiệm kiểm soát truy cập SMB bằng pfSense**<br>• 3.6.1. Bố trí pfSense và kiểm soát lưu lượng SMB<br>• 3.6.2. Kết quả kiểm tra lại từ Kali Linux<br>• 3.6.3. Đối chiếu kết quả tại Kali, pfSense và Windows | Thực nghiệm kiểm soát truy cập SMB bằng pfSense | **MOVE & EXPAND**: Bổ sung sơ đồ kiến trúc Transparent Bridge (Hình 3.10 mới); trình bày cấu hình rule order (Hình 3.11); kết quả filtered (Hình 3.12); phân tích đối chiếu 3 bên có bảo lưu xung đột nhãn quy tắc CF-11 (Hình 3.13). |
| **3.6. So sánh kết quả thực nghiệm** | So sánh kết quả thực nghiệm | **3.7. Đối chiếu kết quả các trạng thái thực nghiệm**<br>• 3.7.1. Đối chiếu trạng thái ban đầu và sau các can thiệp<br>• 3.7.2. Những thay đổi và yếu tố không thay đổi | Đối chiếu kết quả các trạng thái thực nghiệm | **MOVE & RESTRUCTURE**: Tách thành 2 tiểu mục: 3.7.1 tập trung vào ma trận dữ liệu Bảng 3.7; 3.7.2 phân định bản chất hai vị trí can thiệp (Host vs. Network Path) qua sơ đồ Hình 3.14 mới. |
| **3.7. Tổng kết chương** | Tổng kết chương | **3.8. Tổng kết chương** | Tổng kết chương | **MOVE & REWRITE**: Viết lại cô đọng, trang trọng, tóm lược 5 phát hiện then chốt và chuyển giao dữ kiện sạch cho Chương 4 thảo luận rủi ro. |

---

## 3. BẢN ĐỒ CHUYỂN DỊCH CHI TIẾT TỪNG ĐOẠN VĂN BẢN (BLOCK-BY-BLOCK MIGRATION)

### 3.1. Nhóm nội dung Dẫn nhập và Mục tiêu thực nghiệm (Mục 3.1 mới)

| Khối nội dung nguồn trong Draft R2 | Vị trí đích trong cấu trúc mới | Hành động (Action Tag) | Dữ kiện kỹ thuật bảo toàn | Kế hoạch chuyển dịch & Cải tiến cách kể chuyện |
|---|---|---|---|---|
| *Chưa có khối tương ứng trong Draft R2* (chỉ có dòng 1: Tiêu đề chương) | **3.1.1. Mục tiêu kiểm chứng** | **NEW / REWRITE** | Bám sát Mục tiêu O3, O4 và Câu hỏi nghiên cứu RQ3, RQ4 trong `RESEARCH_MAP.md`. 4 biến dữ kiện: reachability, protocol state, remote detection, local patch state. Không exploit/RCE. | Soạn mới đoạn dẫn nhập định hướng: Giải thích vì sao cần thực nghiệm, mục tiêu không phải để biểu diễn tấn công mà để phân lập rạch ròi 4 tầng dữ kiện và kiểm chứng hai giải pháp giảm thiểu rủi ro. |
| *Chưa có khối tương ứng trong Draft R2* | **3.1.2. Luồng thực nghiệm** | **NEW / REWRITE** | Chuỗi tiến trình 6 giai đoạn logic: Baseline $\to$ Kịch bản 1 $\to$ Kịch bản 2 $\to$ Case B $\to$ Case C $\to$ Đối chiếu tổng hợp. Các điểm hoàn nguyên snapshot `Before Demo`. | Soạn mới đoạn văn mô tả tiến trình thực nghiệm; kết nối trực tiếp với **Hình 3.1 mới** (Sơ đồ quy trình thực nghiệm) giúp người đọc hình dung toàn bộ bức tranh trước khi đi vào số liệu chi tiết. |

---

### 3.2. Nhóm nội dung Mốc chuẩn xuất phát (Old 3.1 $\to$ New 3.2)

| Khối nội dung nguồn trong Draft R2 | Dòng nguồn | Vị trí đích | Hành động (Action Tag) | Dữ kiện kỹ thuật bảo toàn | Kế hoạch chuyển dịch & Cải tiến cách kể chuyện |
|---|---|---|---|---|---|
| Đoạn mở đầu Old 3.1 (Mốc xuất phát, tham chiếu...) | Dòng 4–6 | **3.2 (Đoạn mở đầu)** | **REWRITE & MOVE** | Mốc tham chiếu nhất quán; 4 nhóm thông số: mạng, dịch vụ, tường lửa, bản vá. | Giữ nguyên ý nghĩa mốc chuẩn; viết lại mạch lạc hơn: Mốc xuất phát là "thước đo đối chứng độc lập" để thẩm định mọi thay đổi sau này. |
| Đoạn 1 Old 3.1.1 (Môi trường ảo hóa Host-Only, không default route, IP hai máy) | Dòng 10–11 | **3.2.1 (Đoạn 1)** | **REUSE & MOVE** | VirtualBox Host-Only cô lập; Kali `192.168.56.10/24` (`eth0`); Windows `192.168.56.20/24` (`Ethernet`); không default route, không card NAT/Bridged. | Giữ nguyên 100% dữ kiện kỹ thuật; chỉnh sửa câu văn nhấn mạnh tính cô lập an toàn của phân đoạn lab. |
| Đoạn 2 Old 3.1.1 (Dịch vụ LanmanServer, FS-SMB1, EnableSMB1/2=True, signing cục bộ False, socket Listen) | Dòng 12–13 | **3.2.1 (Đoạn 2)** | **REUSE & MOVE** | `LanmanServer` Running/Automatic; `FS-SMB1` Installed; `EnableSMB1Protocol : True`, `EnableSMB2Protocol : True`; signing cục bộ False; socket lắng nghe TCP 445 (`::`) và TCP 139 (`192.168.56.20`). | Tách bạch rõ cấu hình cục bộ với quan sát mạng; giải thích cho người đọc hiểu vì sao dịch vụ SMB đang sẵn sàng phục vụ trên máy chủ. |
| Tham chiếu và Bảng 3.1 cũ (Trạng thái mạng, dịch vụ SMB và Windows Firewall) | Dòng 14–31 | **3.2.1 (Bảng 3.1 mới)** | **MOVE & EXPAND** | Toàn bộ 11 hàng dữ liệu kiểm toán mốc xuất phát. | Chuyển nguyên vẹn cấu trúc bảng sang Bảng 3.1 mới; bổ sung thêm ghi chú ngắn về quy tắc tường lửa tùy biến. |
| Đoạn phân tích và Hình 3.1 cũ (`Windows_PreDemo_01_Network_SMB.png`) | Dòng 32–37 | **3.2.1 (Hình 3.2 mới)** | **MOVE (Số mới: Hình 3.2)** | Xác thực IP, dịch vụ, tính năng FS-SMB1 và socket lắng nghe trên PowerShell. Socket lắng nghe cục bộ != cổng mở trên mạng. | Chuyển thành Hình 3.2 mới; văn phong giải thích tập trung vào việc chứng minh hệ điều hành đã sẵn sàng dịch vụ ở mốc ban đầu. |
| Đoạn phân tích firewall và Hình 3.2 cũ (`Windows_PreDemo_02_Firewall.png`) | Dòng 38–45 | **3.2.1 (Đoạn 3)** | **MERGE & TRIM / RETIRE FIGURE** | 3 profile Windows Firewall Enabled=True; 16 quy tắc chia sẻ tệp mặc định False; quy tắc tùy biến `ATTT Lab SMB 139-445` cho phép duy nhất IP .56.10. | Giữ nguyên dữ kiện cấu hình tường lửa trong văn bản phân tích và Bảng 3.1; chuyển ảnh Hình 3.2 cũ vào kho Supporting để giảm tải thị giác, tập trung vào Hình 3.2 chính. |
| Đoạn 1 & 2 Old 3.1.2 (Kiểm tra srv.sys, FileVersion, ghép phiên bản số nhị phân, đối chiếu KB4012213/KB4012216) | Dòng 48–51 | **3.2.2 (Đoạn 1 & 2)** | **REUSE & MOVE** | Tệp `srv.sys` tại `C:\Windows\System32\drivers\srv.sys`; FileVersion hiển thị `6.3.9600.16384`; phiên bản số nhị phân `6.3.9600.16421`; ngưỡng tối thiểu Microsoft `6.3.9600.18604`; $6.3.9600.16421 < 6.3.9600.18604$. | Giữ nguyên lập luận toán học và kỹ thuật; giải thích rõ cho người đọc hiểu vì sao chuỗi hiển thị khác với số nhị phân và vì sao kết luận máy chủ chưa vá lỗi. |
| Đoạn 3 Old 3.1.2 (Kiểm tra Get-HotFix, 6 bản vá năm 2014, thiếu bản vá MS17-010) | Dòng 52–53 | **3.2.2 (Đoạn 3)** | **REUSE & MOVE** | `Get-HotFix` ghi nhận 6 bản cập nhật ngày 21/03/2014; hoàn toàn thiếu KB4012213 hoặc KB4012216. | Giữ nguyên danh mục hotfix; làm rõ đây là căn cứ độc lập thứ hai củng cố trạng thái chưa vá lỗi của máy chủ. |
| Đoạn 4 & 5 Old 3.1.2 (Phân loại UNPATCHED, Snapshot Before Demo) | Dòng 54–57 | **3.2.2 (Đoạn 4)** | **REUSE & MOVE** | Phân loại trạng thái bản vá cục bộ: **UNPATCHED**. Mốc phục hồi Snapshot `Before Demo` trên cả 2 VM tắt máy. | Tái khẳng định nguyên tắc: UNPATCHED là sự thật nội bộ, không tự sinh ra phán quyết từ xa khi chưa quét mạng. |
| Tham chiếu và Bảng 3.2 cũ (Trạng thái bản vá và mốc phục hồi) | Dòng 58–71 | **3.2.2 (Bảng 3.2 mới)** | **MOVE** | Bảng đối chiếu srv.sys, hotfix và snapshot. | Chuyển nguyên vẹn sang Bảng 3.2 mới. |
| Đoạn phân tích và Hình 3.3 cũ (Ghép srv.sys và hotfix) | Dòng 72–77 | **3.2.2 (Hình 3.3 mới)** | **MOVE (Giữ số: Hình 3.3)** | Ảnh ghép 2 panel: Thuộc tính srv.sys + Danh mục Get-HotFix. | Giữ nguyên Hình 3.3 làm bằng chứng thị giác trực tiếp cho trạng thái UNPATCHED nội bộ. |
| Đoạn chuyển tiếp Old 3.1 $\to$ 3.2 cũ | Dòng 78–79 | **3.2.2 (Đoạn kết)** | **REWRITE** | Cầu nối sang Kịch bản 1. | Viết lại câu nối: Sau khi xác lập xong mốc chuẩn xuất phát (dịch vụ chạy, máy chưa vá), bước tiếp theo là ra ngoài mạng để quan sát xem trạm Kali nhìn thấy những gì. |

---

### 3.3. Nhóm nội dung Khảo sát dịch vụ SMB Kịch bản 1 (Old 3.2 $\to$ New 3.3)

| Khối nội dung nguồn trong Draft R2 | Dòng nguồn | Vị trí đích | Hành động (Action Tag) | Dữ kiện kỹ thuật bảo toàn | Kế hoạch chuyển dịch & Cải tiến cách kể chuyện |
|---|---|---|---|---|---|
| Đoạn mở đầu Old 3.2 (Mục tiêu Kịch bản 1, tuần tự các tầng) | Dòng 80–83 | **3.3 (Đoạn mở đầu)** | **REWRITE & MOVE** | Khảo sát bề mặt dịch vụ SMB từ góc nhìn Kali Linux trên cùng phân đoạn Host-Only. | Viết lại từ góc nhìn người quan sát: Đặt câu hỏi "Từ bên ngoài mạng, trạm kiểm thử có thể nhìn thấy những dịch vụ gì trên máy chủ mục tiêu?". |
| Đoạn 1 Old 3.2.1 (Khám phá mạng ARP, 4 IP, host .56.100 UNKNOWN identity, ping .56.20 alive) | Dòng 86–87 | **3.3.1 (Đoạn 1)** | **REUSE & MOVE** | Quét ARP dải .56.0/24 phát hiện 4 IP (.1, .10, .20, .100); `.56.100` mang nhãn bắt buộc `UNKNOWN identity`; `.56.20` phản hồi trực tuyến. | Giữ nguyên 100% dữ kiện; giải thích rõ bước khám phá mạng là điều kiện tiên quyết để xác nhận mục tiêu đang hoạt động trước khi quét cổng. |
| Đoạn 2 Old 3.2.1 (Quét TCP SYN cổng 139 và 445, OPEN syn-ack TTL 128, 445 OPEN != vulnerable) | Dòng 88–89 | **3.3.1 (Đoạn 2)** | **REUSE & MOVE** | Cổng 139/tcp và 445/tcp `OPEN`, phản hồi `syn-ack`, TTL 128. Tiên đề cốt lõi: `445 OPEN != vulnerable`. | Nhấn mạnh sự khác biệt giữa "cổng mở tiếp nhận kết nối" và "tồn tại lỗ hổng an ninh". |
| Tham chiếu và Bảng 3.3 cũ (Trình tự và kết quả khảo sát dịch vụ SMB) | Dòng 90–101 | **3.3.3 (Bảng 3.3 mới)** | **MOVE** | Toàn bộ dữ liệu 5 bước B2 đến B6. | Chuyển bảng xuống tiểu mục 3.3.3 làm bảng tổng hợp dữ liệu chuẩn hóa của Kịch bản 1. |
| Đoạn phân tích Nmap -sV và Hình 3.4 cũ (`Scenario1_B5_SMB_Version.png`) | Dòng 102–111 | **3.3.2 (Đoạn 1)** | **MERGE & MOVE (Hình 3.5 Panel A)** | Dịch vụ 139 netbios-ssn, 445 microsoft-ds; dải fingerprint `Windows Server 2008 R2 - 2012`; không định danh tuyệt đối bản 2012 R2. | Giải thích đặc tính nhận diện từ xa qua fingerprint; ghép ảnh -sV thành Panel A của Hình 3.5 mới. |
| Đoạn phân tích Nmap NSE và Hình 3.5 cũ (`Scenario1_B6_SMB_NSE_A.png`) | Dòng 112–117 | **3.3.2 (Đoạn 2)** | **MERGE & MOVE (Hình 3.5 Panel B)** | 4 script NSE: `smb-protocols`, `smb2-capabilities`, `smb2-security-mode`, `smb-os-discovery`. | Giới thiệu mục tiêu của các kịch bản NSE phân tích chuyên sâu giao thức; ghép ảnh NSE thành Panel B của Hình 3.5 mới. |
| Đoạn 3 nhóm thông tin NSE (5 dialect, SMBv1 dangerous but default, signing enabled but not required, smb-os-discovery no usable output) | Dòng 118–125 | **3.3.2 (Đoạn 3, 4, 5)** | **REUSE & MOVE** | 5 dialect (`NT LM 0.12`, `2.0.2`, `2.1`, `3.0`, `3.0.2`); `SMBv1 enabled != MS17-010 confirmed`; signing policy `enabled but not required`; `smb-os-discovery` không có kết quả khả dụng. | Trình bày mạch lạc 3 phát hiện: hỗ trợ SMBv1 cũ, chính sách ký số mở, và giới hạn của script os-discovery. Không tự ý suy đoán nguyên nhân lỗi. |
| Đoạn tổng kết Kịch bản 1 và cầu nối Old 3.2 $\to$ 3.3 cũ | Dòng 126–127 | **3.3.3 (Đoạn văn tổng hợp)** | **REWRITE & MOVE** | Đã xác định bề mặt SMB mở, có SMBv1, nhưng chưa có phán quyết về MS17-010. | Đúc kết lại ý nghĩa của Kịch bản 1 và mở ra câu hỏi cho Kịch bản 2: Liệu việc máy chủ hỗ trợ SMBv1 có đồng nghĩa với việc tồn tại lỗ hổng MS17-010 hay không? |

---

### 3.4. Nhóm nội dung Kiểm tra dấu hiệu MS17-010 (Old 3.3 $\to$ New 3.4)

| Khối nội dung nguồn trong Draft R2 | Dòng nguồn | Vị trí đích | Hành động (Action Tag) | Dữ kiện kỹ thuật bảo toàn | Kế hoạch chuyển dịch & Cải tiến cách kể chuyện |
|---|---|---|---|---|---|
| Đoạn mở đầu Old 3.3 (Mục tiêu Kịch bản 2) | Dòng 128–131 | **3.4 (Đoạn mở đầu)** | **REWRITE & MOVE** | Kiểm tra dấu hiệu MS17-010 bằng tập kịch bản Nmap NSE chuyên sâu từ trạm Kali. | Đặt câu hỏi trung tâm: "Khi sử dụng công cụ quét lỗ hổng chuyên dụng kiểm tra MS17-010, hệ thống phản hồi như thế nào và kết quả đó nói lên điều gì?". |
| Đoạn 1, 2, 3 Old 3.3.1 (Phân tích chi tiết NSE01, NSE02, NSE03) | Dòng 132–141 | **3.4.1 (Đoạn 1)** | **TRIM & MERGE** | Tái xác nhận cổng mở (NSE01), 5 phương ngữ (NSE02), chính sách ký số (NSE03). | Tóm gọn 3 phép đo đầu đóng vai trò "kiểm tra điều kiện môi trường" (pre-condition check), tránh viết lặp lại dài dòng toàn bộ nội dung đã phân tích ở 3.3.2. |
| Tham chiếu và Bảng 3.4 cũ (Trình tự và kết quả các phép đo NSE) | Dòng 142–152 | **3.4.1 (Bảng 3.4 mới)** | **MOVE** | Bảng tổng hợp 4 phép đo NSE-SMB-01 đến NSE-SMB-04. | Giữ nguyên cấu trúc Bảng 3.4 trong Mục 3.4.1 làm bảng dữ liệu chuẩn hóa của Kịch bản 2. |
| Đoạn thực thi NSE04 và Hình 3.6 cũ (`Scenario2_NSE04_MS17010.png`) | Dòng 153–161 | **3.4.1 (Đoạn 2 & Hình 3.6 mới)** | **REUSE & MOVE (Giữ số: Hình 3.6)** | Lệnh quét `nmap -p 445 --script smb-vuln-ms17-010 192.168.56.20`; cổng 445 open; `Nmap done`; hoàn toàn không có khối `Host script results:`. | Trình bày trực quan kết quả quét của Nmap qua Hình 3.6; mô tả trung thực hiện tượng công cụ hoàn tất quét mà không in ra kết luận kịch bản. |
| Đoạn phân tích phân loại UNKNOWN và nguyên tắc UNKNOWN != SAFE | Dòng 162–166 | **3.4.1 (Đoạn 3)** | **REUSE & MOVE** | Phân loại dự án: **`UNKNOWN / NO USABLE SCRIPT RESULT`**. Nguyên nhân không được xác lập. Tiên đề an toàn thông tin: **`UNKNOWN != SAFE`**. Không tự gán VULNERABLE/SAFE/NOT VULNERABLE. | Phân tích sâu sắc ranh giới khoa học: "Không phát hiện thấy" không đồng nghĩa với "Hệ thống an toàn"; cảnh báo nguy cơ ngộ nhận trong đánh giá an ninh mạng. |
| Đoạn đối chiếu chéo hai trục Remote UNKNOWN và Local UNPATCHED | Dòng 167–168 | **3.4.2 (Toàn bộ tiểu mục mới)** | **REWRITE, EXPAND & NEW FIGURE (Hình 3.7 mới)** | Trục từ xa: `UNKNOWN / NO USABLE SCRIPT RESULT`. Trục nội bộ: `UNPATCHED`. Hai trục độc lập; local UNPATCHED không biến remote thành VULNERABLE; remote UNKNOWN không biến máy thành SAFE. | Phát triển thành một tiểu mục phân tích độc lập (3.4.2) kèm **Hình 3.7 mới** (Sơ đồ đối chiếu chéo 2 trục dữ kiện). Đây là điểm sáng phương pháp luận quan trọng nhất của đồ án. |
| Đoạn ranh giới không exploit và cầu nối sang các ca can thiệp | Dòng 169–172 | **3.4.2 (Đoạn kết)** | **REUSE & REWRITE** | Không có hoạt động exploit/RCE/Meterpreter trong phạm vi thực nghiệm đã phê duyệt. Cầu nối sang Case B và Case C. | Khẳng định tính nghiêm cẩn của thực nghiệm: không thực hiện hành vi tấn công phá hoại; trước thực trạng máy chủ thiếu bản vá, nghiên cứu chuyển sang đánh giá hai giải pháp giảm thiểu. |

---

### 3.5. Nhóm nội dung Can thiệp vô hiệu hóa SMBv1 (Old 3.4 $\to$ New 3.5)

| Khối nội dung nguồn trong Draft R2 | Dòng nguồn | Vị trí đích | Hành động (Action Tag) | Dữ kiện kỹ thuật bảo toàn | Kế hoạch chuyển dịch & Cải tiến cách kể chuyện |
|---|---|---|---|---|---|
| Đoạn mở đầu Old 3.4 (Mục tiêu Case B can thiệp một biến số) | Dòng 173–176 | **3.5 (Đoạn mở đầu)** | **REWRITE & MOVE** | Can thiệp một biến số duy nhất: cấu hình tắt SMBv1 trên máy chủ; đo đạc lại từ xa từ trạm Kali. | Dẫn dắt tự nhiên: Để ngăn ngừa nguy cơ khai thác SMBv1 khi chưa thể cài đặt bản vá, giải pháp quản trị đầu tiên được xem xét là vô hiệu hóa giao thức SMBv1 ngay trên máy chủ. |
| Đoạn 1 Old 3.4.1 (Trạng thái trước và lệnh PowerShell thực thi) | Dòng 177–180 | **3.5.1 (Đoạn 1)** | **REUSE & MOVE** | Trạng thái trước: SMB1=True, SMB2=True, LanmanServer Running. Lệnh: `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`. Can thiệp cấu hình runtime, không phải cài patch, không gỡ tính năng. | Mô tả chi tiết hành động quản trị; liên kết với Panel 1 và Panel 2 của **Hình 3.8 mới** (Sequential Action Panel). |
| Đoạn 2 & 3 Old 3.4.1 và Hình 3.7 cũ (Trạng thái sau can thiệp và ranh giới kỹ thuật) | Dòng 181–189 | **3.5.1 (Đoạn 2 & 3)** | **MERGE & EXPAND (Hình 3.8 mới)** | `EnableSMB1Protocol : False`, `EnableSMB2Protocol : True`, `FS-SMB1 : Installed`, `LanmanServer : Running`. Ranh giới: `SMBv1 disabled != FS-SMB1 uninstalled`; `SMBv1 disabled != PATCHED`. | Ghép toàn bộ tiến trình Before $\to$ Action $\to$ After thành **Hình 3.8 mới (3 panel)**; phân tích rõ việc dịch vụ vẫn chạy và gói tính năng vẫn còn trong hệ thống. |
| Tham chiếu và Bảng 3.5 cũ (So sánh Before vs. After Case B) | Dòng 190–205 | **3.5.3 (Bảng 3.5 mới)** | **MOVE** | Bảng so sánh 7 tiêu chí Before vs. After của Case B. | Chuyển bảng xuống tiểu mục 3.5.3 làm bảng tổng kết sự thay đổi quan sát được của Case B. |
| Đoạn 1 & 2 Old 3.4.2 và Hình 3.8 cũ (`SMBv1_Remediation_04_NSE02_Protocols.png`) | Dòng 207–215 | **3.5.2 (Đoạn 1 & Hình 3.9 mới)** | **MOVE (Số mới: Hình 3.9)** | Đo lại kịch bản `smb-protocols`: 4 dialect (2.0.2..3.0.2); `NT LM 0.12 (SMBv1)` hoàn toàn vắng mặt; TCP 445 OPEN. **Lưu ý:** Cổng 139 không đo lại; cổng 445 không có cờ `--reason`. | Trình bày kết quả đo lại từ Kali qua **Hình 3.9 mới**; làm nổi bật việc phương ngữ cũ đã biến mất trên đường truyền nhưng cổng 445 vẫn mở. |
| Đoạn 3 & 4 Old 3.4.2 (Đo lại MS17-010 và ranh giới phương pháp luận) | Dòng 216–219 | **3.5.2 (Đoạn 2)** | **REUSE & MOVE** | Đo lại `smb-vuln-ms17-010` tiếp tục duy trì `UNKNOWN / NO USABLE SCRIPT RESULT`. Ranh giới: 445 OPEN != vulnerable; UNKNOWN != SAFE. | Nhấn mạnh việc quét lại lỗ hổng từ xa vẫn không cho ra kết quả; việc tắt SMBv1 không biến hệ thống thành an toàn tuyệt đối. |
| Đoạn 5 & 6 Old 3.4.2 (Phân tách 4 tầng kỹ thuật, tổng kết thay đổi và cầu nối sang Case C) | Dòng 220–223 | **3.5.3 (Đoạn tổng hợp)** | **REWRITE & MOVE** | Đúc kết Case B: thay đổi danh mục dialect từ xa (mất SMBv1), giữ nguyên cổng 445 mở, giữ nguyên UNPATCHED nội bộ. Cầu nối sang Case C. | Tổng kết ưu điểm (loại bỏ phương ngữ cũ không làm sập dịch vụ) và hạn chế cốt lõi (cổng 445 vẫn mở, driver chưa vá); dẫn dắt sang nhu cầu kiểm soát bằng tường lửa pfSense tại Mục 3.6. |

---

### 3.6. Nhóm nội dung Can thiệp kiểm soát bằng pfSense (Old 3.5 $\to$ New 3.6)

| Khối nội dung nguồn trong Draft R2 | Dòng nguồn | Vị trí đích | Hành động (Action Tag) | Dữ kiện kỹ thuật bảo toàn | Kế hoạch chuyển dịch & Cải tiến cách kể chuyện |
|---|---|---|---|---|---|
| Đoạn mở đầu Old 3.5 (Mục tiêu Case C can thiệp trên đường mạng) | Dòng 224–227 | **3.6 (Đoạn mở đầu)** | **REWRITE & MOVE** | Kiểm soát an ninh trên đường truyền mạng thay vì can thiệp máy chủ; mô hình pfSense Transparent Bridge Layer 2; đo đạc từ xa, đối chiếu nhật ký và kiểm chứng máy chủ. | Đặt câu hỏi dẫn dắt: "Nếu không thay đổi cấu hình máy chủ, liệu việc chặn lưu lượng SMB bằng tường lửa trên đường truyền có cô lập được dịch vụ và bảo vệ hệ thống không?". |
| Đoạn 1 & 2 Old 3.5.1 (Cấu hình bridge0, interface em2/em3, FreeBSD tunables pfil_member=1) | Dòng 228–233 | **3.6.1 (Đoạn 1 & Hình 3.10 mới)** | **EXPAND & NEW FIGURE (Hình 3.10 mới)** | Transparent Bridge Layer 2 (`bridge0`); `CASE_C_KALI = em2`, `CASE_C_WINDOWS = em3`; giữ nguyên subnet phẳng `192.168.56.0/24`; không định tuyến Layer 3; tunables `pfil_member=1`, `pfil_bridge=0`. | Bổ sung **Hình 3.10 mới** (Sơ đồ kiến trúc Transparent Bridge) giúp người đọc hình dung cơ chế bắc cầu trong suốt; giải thích rõ vì sao không cần đổi địa chỉ IP máy chủ. |
| Đoạn 3 Old 3.5.1 và Hình 3.9 cũ (`pfSense_08_Rule_Order.png`) | Dòng 234–240 | **3.6.1 (Đoạn 2 & Hình 3.11 mới)** | **MOVE (Số mới: Hình 3.11)** | Quy tắc Block TCP từ Kali (.56.10) tới Windows (.56.20) cổng 139, 445 có bật Log; xếp ở vị trí Dòng 1, ngay phía trên quy tắc Pass baseline (Dòng 2). | Trình bày minh chứng cấu hình quy tắc qua **Hình 3.11 mới**; làm rõ nguyên tắc tường lửa "First-Match": quy tắc Block phải đứng trước quy tắc Pass. |
| Tham chiếu và Bảng 3.6 cũ (So sánh Before vs. After Case C) | Dòng 241–258 | **3.6.3 (Bảng 3.6 mới)** | **MOVE** | Bảng so sánh các tầng kiểm soát của Case C giữa Baseline và sau can thiệp. | Chuyển bảng xuống tiểu mục 3.6.3 làm bảng đối chiếu đa tầng của Case C. |
| Đoạn 1 & 2 Old 3.5.2 và Hình 3.10 cũ (`pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`) | Dòng 260–268 | **3.6.2 (Toàn bộ tiểu mục & Hình 3.12 mới)** | **MOVE (Số mới: Hình 3.12)** | Quét lại từ Kali bằng Nmap -sS -p 139,445 --reason: cả hai cổng 139 và 445 chuyển sang `filtered` do `no-response`. Tiên đề: `FILTERED != PATCHED`. | Trình bày kết quả đo lại từ Kali qua **Hình 3.12 mới**; giải thích cặn kẽ ý nghĩa của trạng thái filtered: gói tin thăm dò bị "chặn bặt tăm", không nhận được phản hồi. |
| Đoạn 3, 4, 5 Old 3.5.2 và Hình 3.11 cũ (`pfSense_10_Block_Log_CANONICAL.png`) | Dòng 269–277 | **3.6.3 (Đoạn 1 & Hình 3.13 mới)** | **MOVE (Số mới: Hình 3.13)** | Nhật ký pfSense ghi nhận 4 sự kiện Block màu đỏ, lưu lượng TCP SYN từ .56.10 tới .56.20 trên cổng 139/445. **BẢO LƯU XUNG ĐỘT DANH PHÁP (CF-11):** nhãn hiển thị `CASE C baseline pass... (100000104)` đối chiếu với closure `Block SMB... (1000000104)`. Không crop ảnh để che giấu conflict. | Trình bày **Hình 3.13 mới** giữ nguyên độ sắc nét và bảo lưu nguyên vẹn xung đột nhãn quy tắc; khẳng định lưu lượng thực sự bị chặn mà không overclaim về named rule ID. |
| Đoạn 6, 7, 8 Old 3.5.2 (Đo lại MS17-010, trạng thái máy chủ Windows phía sau và ranh giới kỹ thuật) | Dòng 278–284 | **3.6.3 (Đoạn 2 & 3)** | **REUSE & MOVE** | Kịch bản MS17-010 báo cổng filtered $\to$ UNKNOWN. Máy chủ Windows phía sau giữ nguyên cấu hình baseline: SMB1=True, SMB2=True, LanmanServer Running, socket Listen, driver `srv.sys` unpatched. Tiên đề: `FILTERED != PATCHED`. | Làm sáng tỏ bức tranh 3 bên: Kali thấy filtered, pfSense ghi nhận Block, nhưng Windows phía sau vẫn nguyên vẹn dịch vụ và chưa được vá lỗi. Cầu nối sang Mục 3.7. |

---

### 3.7. Nhóm nội dung Đối chiếu kết quả thực nghiệm (Old 3.6 $\to$ New 3.7)

| Khối nội dung nguồn trong Draft R2 | Dòng nguồn | Vị trí đích | Hành động (Action Tag) | Dữ kiện kỹ thuật bảo toàn | Kế hoạch chuyển dịch & Cải tiến cách kể chuyện |
|---|---|---|---|---|---|
| Đoạn mở đầu Old 3.6 và Bảng 3.7 cũ (Ma trận so sánh 3 trạng thái thực nghiệm) | Dòng 285–302 | **3.7.1 (Bảng 3.7 mới & Phân tích)** | **MOVE & REUSE** | Ma trận đối chiếu 3 cột: Baseline vs. Case B vs. Case C trên 7 tiêu chí đo được. | Đặt bảng so sánh Bảng 3.7 làm tâm điểm của Mục 3.7.1; phân tích rõ nét sự biến đổi của từng tham số kỹ thuật qua 3 trạng thái. |
| Đoạn đối chiếu Baseline vs. Case B và Baseline vs. Case C | Dòng 303–306 | **3.7.1 (Đoạn phân tích chi tiết)** | **REUSE & MOVE** | So sánh tác động ở tầng cấu hình máy chủ (Case B) và tác động ở tầng đường truyền mạng (Case C). | Làm nổi bật sự tương phản: Case B chỉ tác động lên danh mục phương ngữ, Case C chặn toàn bộ khả năng tiếp cận cổng. |
| Đoạn so sánh trực tiếp Case B vs. Case C và phân định hai tầng can thiệp | Dòng 307–308 | **3.7.2 (Toàn bộ tiểu mục & Hình 3.14 mới)** | **REWRITE, EXPAND & NEW FIGURE (Hình 3.14 mới)** | Phân định rạch ròi hai vị trí can thiệp: Host Layer (Lớp máy chủ) vs. Network Path Layer (Lớp đường mạng). Driver nhân `srv.sys` bất biến (`UNPATCHED`) trong cả hai trường hợp. | Xây dựng **Hình 3.14 mới** (Sơ đồ phân định hai vị trí can thiệp); giải thích cho người đọc hiểu bản chất cả hai đều là "biện pháp giảm thiểu bù đắp", không thay thế được bản vá. |
| Đoạn ranh giới thực nghiệm tổng kết (5 tiên đề chân lý và ranh giới Chương 3) | Dòng 309–310 | **3.7.2 (Đoạn kết)** | **REUSE & MOVE** | 5 tiên đề: 445 OPEN != vulnerable, SMBv1 enabled != MS17-010 confirmed, SMBv1 disabled != PATCHED, FILTERED != PATCHED, UNKNOWN != SAFE. Không ranking chủ quan, không khuyến nghị quản trị. | Khẳng định tính chuẩn mực học thuật: Chương 3 chỉ dừng lại ở các dữ kiện đo đạc thực tế, nhường phần đánh giá rủi ro và chiến lược phòng thủ cho Chương 4. |

---

### 3.8. Nhóm nội dung Tổng kết chương (Old 3.7 $\to$ New 3.8)

| Khối nội dung nguồn trong Draft R2 | Dòng nguồn | Vị trí đích | Hành động (Action Tag) | Dữ kiện kỹ thuật bảo toàn | Kế hoạch chuyển dịch & Cải tiến cách kể chuyện |
|---|---|---|---|---|---|
| Toàn bộ 3 đoạn văn Old 3.7 (Tổng kết chương, tóm lược kết quả và chuyển giao Chương 4) | Dòng 311–318 | **3.8 (Tổng kết chương)** | **REWRITE & MOVE** | Tóm lược 5 phát hiện cốt lõi: (1) Mốc xuất phát UNPATCHED; (2) Diện mạo dịch vụ SMB và SMBv1; (3) Phán quyết UNKNOWN từ xa độc lập với bản vá nội bộ; (4) Hiệu quả loại bỏ phương ngữ của Case B; (5) Hiệu quả lọc gói tin có ghi log của Case C. Bàn giao dữ kiện cho Chương 4. | Viết lại thành một văn bản tổng kết cô đọng, tự nhiên, không rập khuôn; khép lại Chương 3 một cách trọn vẹn và tạo bước đệm hoàn hảo để bước sang Chương 4. |

---

## 4. CHIẾN LƯỢC CẢI TIẾN VĂN PHONG VÀ KHẢ NĂNG TIẾP CẬN CHO ĐỘC GIẢ (NARRATIVE STRATEGY)

Để đạt mục tiêu tối thượng: *"Một người không có kiến thức chuyên sâu ATTT vẫn hiểu tác giả đang làm gì, tại sao làm và từng kết quả chứng minh điều gì"*, bản đồ chuyển dịch nội dung đề xuất 4 giải pháp cụ thể:

1. **Chuyển hóa từ "Nhật ký câu lệnh" sang "Mạch truyện khoa học":**
   - *Cách viết cũ:* "Tiếp theo thực thi lệnh nmap -p 139,445 --reason 192.168.56.20, kết quả hiển thị 139 open, 445 open..."
   - *Cách viết mới (chuẩn hóa ở R3-1):* "Để kiểm tra xem trạm kiểm thử có thể tương tác với máy chủ qua các cổng chia sẻ tệp hay không, một phép quét thăm dò được thực hiện nhắm vào hai cổng dịch vụ tiêu chuẩn là TCP 139 và 445. Kết quả ghi nhận cả hai cổng đều tiếp nhận kết nối và phản hồi gói tin SYN-ACK, xác nhận bề mặt dịch vụ SMB đã sẵn sàng trên đường truyền mạng..."
2. **Làm nổi bật các câu hỏi dẫn dắt tại đầu mỗi đề mục:**
   - Người đọc luôn được định hướng trước: *Phần này trả lời cho câu hỏi gì?* trước khi đối diện với các bảng số liệu hay ảnh terminal.
3. **Giải thích trực quan các thuật ngữ kỹ thuật cốt lõi:**
   - Giải thích ngắn gọn và dễ hiểu các khái niệm: *Cổng mở (Open) nghĩa là gì*, *Cổng bị lọc (Filtered) khác gì với Cổng đóng (Closed)*, *Phương ngữ SMB (Dialect) là gì*, *Tại sao không nhận được kết quả (UNKNOWN) không có nghĩa là an toàn (SAFE)*.
4. **Phân định rạch ròi giữa Quan sát thực tế và Ý nghĩa an ninh:**
   - Luôn tách bạch: *Công cụ nhìn thấy gì trên màn hình* và *Về mặt bảo mật, điều đó chứng minh được đến đâu*. Tuyệt đối không để người đọc ngộ nhận rằng việc thấy cổng mở hay hỗ trợ SMBv1 là đã tấn công thành công máy chủ.

---

## 5. BẢO ĐẢM TÍNH TOÀN VẸN VÀ KHÔNG THẤT THOÁT DỮ LIỆU

- Toàn bộ 318 dòng văn bản và các sự thật kỹ thuật trong `CHAPTER_3_DRAFT_R2.md` đã được ánh xạ 100% sang các đề mục tương ứng trong cấu trúc 8 phần của Chương 3 mới.
- Toàn bộ 7 bảng biểu và 11 hình ảnh cũ được phân bổ rõ ràng (MOVE, MERGE, EXPAND, hoặc SUPPORTING), không có bất kỳ bảng biểu hay hình ảnh nào bị bỏ sót khỏi vòng kiểm soát.
- Mọi ranh giới kỹ thuật cốt lõi (5 tiên đề, xung đột danh pháp CF-11, giới hạn đo đạc Case B, tính độc lập giữa remote và local) được bảo toàn tuyệt đối.
