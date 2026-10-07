# BÁO CÁO TỰ ĐÁNH GIÁ BIÊN TẬP TOÀN BỘ CHƯƠNG 3 (X7H_CH3_WHOLE_REVIEW_SELF_REVIEW_R1)

- **Trạng thái:** `X7H_R1_READY_FOR_INDEPENDENT_REVIEW`
- **Pha thực hiện:** `X7H — Whole-Chapter-3 Product Review`
- **Ngày thực hiện:** 2026-10-07
- **Nhánh làm việc:** `feature/x7h-ch3-whole-review-approved-r1`
- **Base Reviewed X7G State:** `d348b713802593ff82bbab5b460e5eb7e6973b3d`
- **Tập tin kết quả chính:** [CHAPTER_3_DRAFT_R2.md](file:///e:/word_ppt-auto/work/do-an/CHAPTER_3_DRAFT_R2.md)
- **Tập tin cơ sở kỹ thuật:** [CHAPTER_3_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CHAPTER_3_DRAFT_R1.md)
- **Tài liệu tham chiếu:**
  * [X7H_REVIEW_COMPLETE_CHAPTER_3.md](file:///e:/word_ppt-auto/work/do-an/prompts/X7H_REVIEW_COMPLETE_CHAPTER_3.md)
  * [ROADMAP_CURRENT_CH2_CH3_2026_10_07.md](file:///e:/word_ppt-auto/work/do-an/ROADMAP_CURRENT_CH2_CH3_2026_10_07.md)
  * [PROJECT_STATE.md](file:///e:/word_ppt-auto/work/do-an/PROJECT_STATE.md)
  * [CHAPTER_3_CONTRACT.md](file:///e:/word_ppt-auto/work/do-an/CHAPTER_3_CONTRACT.md)
  * [EXPERIMENTAL_TRUTH_MATRIX.md](file:///e:/word_ppt-auto/work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md)

---

## 1. Mục Tiêu & Phạm Vi Biên Tập X7H

Pha X7H thẩm định và biên tập Chương 3 như một chương luận văn hoàn chỉnh, chuyển hóa bản thảo ráp cơ học (R1) thành một văn bản học thuật mạch lạc (R2). Quá trình biên tập tập trung giải quyết:
- Hiện tượng lặp khuôn mẫu chuyển đoạn và mở đầu mục;
- Loại bỏ các câu văn giải thích trùng lặp giữa các mục độc lập;
- Tối ưu hóa độ dài câu và nhịp điệu diễn đạt học thuật tiếng Việt;
- Bảo toàn tuyệt đối 100% dữ kiện kỹ thuật, số hiệu bảng biểu, hình ảnh và các ranh giới phương pháp luận đã khóa.

---

## 2. So Sánh Định Lượng R1 và R2 (Word-Count Comparison)

### 2.1. Toàn bộ chương
| Chỉ số | R1 Assembled | R2 Reviewed | Chênh lệch (Diff) | Nhận xét |
|---|:---:|:---:|:---:|---|
| **Tổng số từ (Total words)** | 11.101 | **10.886** | -215 từ | Tinh gọn các đoạn lặp thừa |
| **Số từ văn xuôi (Prose words)** | 9.444 | **9.229** | -215 từ | Loại bỏ câu trùng, tối ưu chuyển tiếp |
| **Số tiêu đề H1** | 1 | 1 | 0 | Giữ nguyên |
| **Số tiêu đề H2** | 7 | 7 | 0 | Giữ nguyên danh mục canonical |
| **Số tiêu đề H3** | 10 | 10 | 0 | Giữ nguyên cấu trúc tiểu mục |
| **Số bảng biểu** | 7 | 7 | 0 | Bảng 3.1–3.7 giữ nguyên |
| **Số hình ảnh** | 11 | 11 | 0 | Hình 3.1–3.11 giữ nguyên |

### 2.2. So sánh chi tiết theo từng mục (Per-Section Breakdown)
| Mục nội dung | Từ văn xuôi R1 | Từ văn xuôi R2 | Chênh lệch | Đánh giá độ cân bằng |
|---|:---:|:---:|:---:|---|
| **Mục 3.1 — Trạng thái baseline** | 1.383 | **1.359** | -24 | Cân đối, cô đọng cơ sở thực nghiệm |
| **Mục 3.2 — Kịch bản 1 (Khảo sát SMB)** | 1.666 | **1.557** | -109 | Tinh gọn đoạn phân tích dải phiên bản OS |
| **Mục 3.3 — Kịch bản 2 (Dấu hiệu MS17-010)** | 1.684 | **1.609** | -75 | Rút gọn phần chuyển tiếp lặp lại sang Case B |
| **Mục 3.4 — Case B (Vô hiệu hóa SMBv1)** | 1.772 | **1.735** | -37 | Tinh gọn câu mở đầu, tránh lặp lại recap Mục 3.3 |
| **Mục 3.5 — Case C (Kiểm soát pfSense)** | 1.755 | **1.763** | +8 | Cải thiện câu mở đầu, bổ sung tính liên kết |
| **Mục 3.6 — So sánh kết quả thực nghiệm** | 863 | **885** | +22 | Mở rộng tính tổng hợp và đối chiếu hệ thống |
| **Mục 3.7 — Tổng kết chương** | 321 | **321** | 0 | Kết luận chương súc tích, chuẩn mực |

**Nhận xét:** Trọng tâm thực nghiệm cốt lõi (Mục 3.2 đến 3.5) đạt độ cân đối lý tưởng, dao động từ 1.550 đến 1.760 từ văn xuôi mỗi mục. Mục 3.1 xác lập baseline vững chắc (1.359 từ), Mục 3.6 tổng hợp cô đọng (885 từ) và Mục 3.7 kết luận súc tích (321 từ).

---

## 3. Nhật Ký Chi Tiết Các Thay Đổi Biên Tập (Editorial Edits Log)

Toàn bộ 11 điểm điều chỉnh câu từ và chuyển đoạn được thực hiện có kiểm soát:

### 3.1. Mục 3.1 — Trạng thái baseline trước đo đạc
1. **Câu mở đầu chương (Dòng 6):**
   - *R1:* `Việc xác định và ghi nhận trạng thái ban đầu (baseline) của hệ thống máy chủ mục tiêu trước khi thực hiện các kịch bản thực nghiệm nhằm tạo mốc tham chiếu nhất quán để đối chiếu các phép đo tiếp theo. Mốc xuất phát này ghi nhận các thông số định lượng cụ thể...`
   - *R2:* `Trước khi triển khai các kịch bản thực nghiệm, trạng thái ban đầu (baseline) của hệ thống máy chủ mục tiêu được ghi nhận nhằm xác lập mốc tham chiếu nhất quán cho toàn bộ quá trình đo đạc. Mốc xuất phát này bao gồm các thông số định lượng...`
   - *Tác dụng:* Chuyển từ cấu trúc danh từ hóa thụ động sang lối hành văn chủ động, tự nhiên trong văn phong học thuật.
2. **Đoạn dẫn giải Hình 3.2 (Dòng 44):**
   - *R1:* `Hình 3.2 xác nhận quy tắc tùy biến được cấu hình cho TCP 139/445 với phạm vi địa chỉ nguồn 192.168.56.10, đồng thời nhóm File and Printer Sharing mặc định được ghi nhận ở trạng thái tắt...` (lặp lại nguyên văn đoạn 38).
   - *R2:* `Hình 3.2 xác nhận quy tắc cho phép lưu lượng TCP 139/445 hướng tới máy chủ chỉ áp dụng riêng cho địa chỉ nguồn 192.168.56.10, trong khi các quy tắc mặc định đều tắt. Thiết lập này bảo đảm bề mặt dịch vụ tại baseline chỉ mở cho trạm kiểm thử chỉ định; khả năng tiếp cận thực tế từ xa sẽ được kiểm chứng bằng các phép đo mạng tiếp theo.`
   - *Tác dụng:* Nâng cao giá trị diễn giải, tránh lặp lại cơ học các trường quy tắc đã nêu ở văn bản phía trên.
3. **Đoạn dẫn giải Hình 3.3 (Dòng 76):**
   - *R1:* `Hình 3.3 thể hiện chuỗi phiên bản hiển thị 6.3.9600.16384, kết quả tính toán phiên bản số 6.3.9600.16421 qua các trường nhị phân và danh sách 6 bản cập nhật hệ thống từ năm 2014...`
   - *R2:* `Hình 3.3 trực quan hóa hai căn cứ kỹ thuật trên: phiên bản nhị phân 6.3.9600.16421 thấp hơn mốc yêu cầu và danh sách cập nhật dừng ở năm 2014, xác nhận đầy đủ cơ sở phân loại trạng thái bản vá cục bộ là UNPATCHED.`
   - *Tác dụng:* Cô đọng ý nghĩa chứng minh của hình ảnh, không lặp lại danh sách số liệu.

### 3.2. Mục 3.2 — Kịch bản 1 — Khảo sát dịch vụ SMB
4. **Mở đầu Mục 3.2 (Dòng 82) — Giải quyết cảnh báo VI012:**
   - *R1:* `Sau khi xác lập mốc xuất phát chuẩn tại Mục 3.1, tiến trình thực nghiệm Kịch bản 1 được thực hiện nhằm khảo sát...`
   - *R2:* `Dựa trên mốc tham chiếu đã thiết lập tại Mục 3.1, Kịch bản 1 tiến hành khảo sát bề mặt dịch vụ chia sẻ tệp Server Message Block (SMB) trên hệ thống mục tiêu từ góc nhìn của trạm kiểm thử Kali Linux. Trên cùng phân đoạn mạng nội bộ Host-Only, chuỗi đo đạc được triển khai tuần tự từ tầng liên kết dữ liệu, tầng giao vận đến tầng ứng dụng. Tiến trình này bao gồm phát hiện trạm hoạt động, xác nhận mục tiêu trực tuyến, kiểm tra trạng thái mở cổng, thăm dò dấu vết hệ điều hành và phân tích đặc tính giao thức qua tập kịch bản Nmap NSE. Kết quả thu được phản ánh khả năng tiếp cận dịch vụ thực tế trước khi thực hiện các phép đo chuyên sâu về dấu hiệu lỗ hổng.`
   - *Tác dụng:* Xóa bỏ khuôn mẫu lặp "Sau khi xác...", tách câu dài thành 2 câu mạch lạc, nâng cao tính liên kết.
5. **Mở đầu Mục 3.2.2 (Dòng 104) — Giải quyết cảnh báo VI012:**
   - *R1:* `Sau khi xác định hai cổng TCP 139 và 445 mở, trạm kiểm thử tiếp tục thực hiện thăm dò ở tầng ứng dụng...`
   - *R2:* `Với trạng thái mở của hai cổng TCP 139 và 445, trạm kiểm thử tiếp tục thăm dò tầng ứng dụng nhằm nhận diện dịch vụ và dấu vết phiên bản hệ điều hành.`
   - *Tác dụng:* Đa dạng hóa từ ngữ mở đoạn, tránh cấu trúc "Sau khi xác định...".
6. **Diễn giải dải phiên bản Nmap (Dòng 110):**
   - *R1:* `Kết quả hiển thị trên Hình 3.4 ghi nhận cổng TCP 139 gắn liền với dịch vụ Microsoft Windows netbios-ssn... Kết quả này phản ánh đặc tính nhận diện dấu vết từ xa của công cụ quét mạng: Kết quả Nmap trong lần đo này chỉ khu biệt mục tiêu trong một khoảng dấu vết phiên bản (fingerprint range). Các phản hồi từ xa này chưa đủ căn cứ để định danh chính xác duy nhất phiên bản Windows Server 2012 R2...`
   - *R2:* `Dữ liệu trên Hình 3.4 ghi nhận cổng TCP 139 tương ứng với dịch vụ Microsoft Windows netbios-ssn, còn cổng TCP 445 phản hồi chuỗi dịch vụ Microsoft Windows Server 2008 R2 - 2012 microsoft-ds. Thông tin hệ điều hành suy đoán (Service Info) ước lượng mục tiêu trong khoảng Windows Server 2008 R2 – 2012. Kết quả này phản ánh đặc tính nhận diện dấu vết từ xa của công cụ quét mạng. Nmap chỉ khu biệt hệ thống trong một dải phiên bản (fingerprint range) chứ không thể tự định danh chính xác phiên bản Windows Server 2012 R2 nếu thiếu dữ liệu xác thực cục bộ tại Mục 3.1. Đồng thời, thông tin nhận diện dịch vụ này chỉ phản ánh họ hệ điều hành, không cấu thành bằng chứng về việc máy chủ có tồn tại lỗ hổng an ninh hay không.`
   - *Tác dụng:* Tinh gọn đoạn văn, tách câu phức, làm nổi bật ranh giới giữa quan sát từ xa và xác thực cục bộ.

### 3.3. Mục 3.3 — Kịch bản 2 — Kiểm tra dấu hiệu MS17-010
7. **Mở đầu Mục 3.3 (Dòng 130):**
   - *R1:* `Sau khi hoàn tất quá trình rà quét khám phá mạng và dịch vụ SMB trong Kịch bản 1, Kịch bản 2 tập trung khảo sát các thuộc tính kỹ thuật...`
   - *R2:* `Tiếp nối chuỗi khảo sát dịch vụ tại Kịch bản 1, Kịch bản 2 tập trung thăm dò các đặc tính kỹ thuật chuyên sâu và kiểm tra dấu hiệu liên quan đến lỗ hổng an ninh MS17-010. Tiến trình thực nghiệm được triển khai từ trạm kiểm thử Kali Linux nhắm vào máy chủ Windows Server 2012 R2 thông qua tập kịch bản Nmap Scripting Engine (NSE)...`
   - *Tác dụng:* Tạo liên kết chuyển tiếp tự nhiên giữa hai kịch bản liền kề.
8. **Đoạn kết Mục 3.3 (Dòng 171) & Xóa bỏ lặp ý giữa 3.3 và 3.4:**
   - *R1 (Dòng 171 cuối 3.3):* Tóm tắt dài dòng việc chuyển sang Case B bằng cách kể lại chi tiết cấu hình SMBv1.
   - *R1 (Dòng 175 đầu 3.4):* Mở đầu bằng cách kể lại y hệt nội dung dòng 171: `Sau khi xác lập hiện trạng hệ thống ở mốc ban đầu và hoàn thành hai kịch bản khảo sát diện mạo dịch vụ cũng như kiểm tra dấu hiệu MS17-010 (Mục 3.1 đến Mục 3.3), nghiên cứu tiến hành bước can thiệp...`
   - *R2 (Cuối 3.3):* `Sau khi hoàn tất giai đoạn đường cơ sở gồm khảo sát diện mạo dịch vụ (Kịch bản 1) và kiểm tra dấu hiệu MS17-010 bằng NSE (Kịch bản 2), nghiên cứu chuyển sang pha can thiệp có kiểm soát tại Mục 3.4 (Case B) và Mục 3.5 (Case C) nhằm đối chiếu tác động của từng giải pháp giảm thiểu.`
   - *Tác dụng:* Khép lại giai đoạn baseline gãy gọn, mở đường cho cả 2 kịch bản can thiệp Case B và Case C.

### 3.4. Mục 3.4 — Case B — Vô hiệu hóa SMBv1
9. **Mở đầu Mục 3.4 (Dòng 175) — Giải quyết cảnh báo VI012:**
   - *R2:* `Bước can thiệp có kiểm soát đầu tiên (Case B) điều chỉnh một biến số duy nhất: cấu hình vô hiệu hóa giao thức SMBv1 trên máy chủ chia sẻ tệp Windows Server 2012 R2. Mục tiêu của Case B là đánh giá thực nghiệm tác động của biện pháp cấu hình cục bộ lên diện mạo dịch vụ từ xa. Qua đó, trạm kiểm thử Kali Linux đo đạc lại danh mục phương ngữ phản hồi và kết quả thăm dò lỗ hổng để đối chiếu với đường cơ sở.`
   - *Tác dụng:* Đi thẳng vào trọng tâm đơn biến số của Case B, xóa bỏ hoàn toàn đoạn recap trùng lặp và loại bỏ mẫu "Sau khi xác...".

### 3.5. Mục 3.5 — Case C — Kiểm soát SMB bằng pfSense
10. **Mở đầu Mục 3.5 (Dòng 226) — Giải quyết cảnh báo VI012:**
    - *R1:* `Sau khi xác lập đường cơ sở và đánh giá can thiệp vô hiệu hóa SMBv1 ở mức máy chủ (Case B), nghiên cứu triển khai kịch bản can thiệp Case C nhắm vào lớp kiểm soát mạng...`
    - *R2:* `Kịch bản can thiệp Case C khảo sát lớp kiểm soát an ninh trên đường truyền mạng thay vì tác động trực tiếp vào cấu hình máy chủ. Trong mô hình Case C, đường thử nghiệm giữa trạm Kali và máy chủ Windows được định tuyến qua tường lửa pfSense hoạt động ở chế độ Transparent Bridge (Layer 2) nhằm thực thi chính sách lọc gói tin đối với các cổng dịch vụ SMB. Trọng tâm của kịch bản là đo đạc diện mạo dịch vụ từ xa từ trạm Kali, đối chiếu các bản ghi nhật ký tường lửa với kết quả rà quét mạng, và kiểm chứng tính độc lập của trạng thái cấu hình nội bộ trên máy chủ mục tiêu.`
    - *Tác dụng:* Khẳng định ngay tính độc lập và bản chất Layer 2 của Case C, xóa bỏ mẫu "Sau khi xác...".

### 3.6. Mục 3.6 — So sánh kết quả thực nghiệm
11. **Mở đầu Mục 3.6 (Dòng 286) — Giải quyết cảnh báo VI012:**
    - *R1:* `Sau khi xác lập đường cơ sở và đánh giá hai phương án can thiệp tại Mục 3.4 (Case B) và Mục 3.5 (Case C), phần này tổng hợp so sánh các kết quả thực nghiệm...`
    - *R2:* `Trên cơ sở các dữ liệu thu thập được từ đường cơ sở và hai kịch bản can thiệp (Case B và Case C), mục này tổng hợp và đối chiếu có hệ thống các kết quả thực nghiệm. Trọng tâm so sánh nhằm làm rõ những điểm biến đổi và những yếu tố duy trì không đổi giữa diện mạo dịch vụ từ xa, lưu lượng trên đường truyền, cùng trạng thái cấu hình và bản vá nội bộ của máy chủ. Toàn bộ nội dung đối chiếu tuân thủ nguyên tắc chỉ dựa trên các dữ kiện đo đạc đã được xác thực, không mở thêm bằng chứng mới và không suy đoán các thông số nằm ngoài phạm vi thực nghiệm.`
    - *Tác dụng:* Nâng tầm tổng hợp học thuật, khẳng định nguyên tắc phương pháp luận và xóa bỏ mẫu "Sau khi xác...".

---

## 4. Kiểm Tra Toàn Vẹn Số Hiệu & Đường Dẫn Tệp

- **Bảng biểu (Bảng 3.1–3.7):** Đúng 7 bảng, thứ tự giữ nguyên 100%, không phát sinh Bảng 3.8.
- **Hình ảnh (Hình 3.1–3.11):** Đúng 11 hình, thứ tự giữ nguyên 100%, không phát sinh Hình 3.12.
- **Đường dẫn tệp ảnh Markdown:** Toàn bộ 11 đường dẫn đều tồn tại thật trên hệ thống tệp và trỏ đúng vị trí tương ứng.

---

## 5. Rà Soát Khóa Kỹ Thuật & Phòng Tránh Rò Rỉ Nội Dung

1. **Bảo toàn 5 bất đẳng thức phương pháp luận:**
   - `445 OPEN != vulnerable`: Có mặt đầy đủ tại Mục 3.2.1, 3.3.1, 3.4.1, 3.4.2, 3.6.
   - `SMBv1 enabled != MS17-010 confirmed`: Có mặt đầy đủ tại Mục 3.2.2, 3.3.1, 3.6.
   - `SMBv1 disabled != PATCHED`: Có mặt đầy đủ tại Mục 3.4.1, 3.4.2, 3.6.
   - `FILTERED != PATCHED`: Có mặt đầy đủ tại Mục 3.5.2, 3.6.
   - `UNKNOWN != SAFE`: Có mặt đầy đủ tại Mục 3.3.2, 3.4.1, 3.4.2, 3.5.2, 3.6, 3.7.
2. **Không phát sinh thuật ngữ cấm hoặc overclaim:**
   - Không xuất hiện `Meterpreter` hay `reverse shell` (0).
   - Không xuất hiện `khai thác thành công` hay `chiếm quyền điều khiển` (0).
   - Không có phán quyết `SAFE` hay `NOT VULNERABLE` cho máy chủ mục tiêu (0).
   - Không có phán quyết từ xa khẳng định `VULNERABLE` (0).
   - Không có kết quả thực nghiệm bản vá Case A (0).
   - Không có nội dung khuyến nghị/xếp hạng rủi ro thuộc Chương 4 (0).
3. **Không rò rỉ ngôn ngữ quản trị nội bộ:**
   - Không có thẻ chú thích HTML (`<!-- ... -->`) (0).
   - Không có chuỗi `CITE-ANCHOR` (0).
   - Không có giọng điệu biên bản kiểm toán nội bộ (QA-like memo).

---

## 6. Kết Quả Kiểm Thử Thực Tế (QA Verification)

- **Linter học thuật tiếng Việt:**
  `uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_3_DRAFT_R2.md`
  * Kết quả: `Không phát hiện mẫu văn phong cần xem xét.` (error=0, warning=0, info=0).
  * Cảnh báo `VI012` về lặp cấu trúc mở đoạn đã được xử lý triệt để.
- **Bộ kiểm thử tự động (Unit Tests):**
  `uv run python -m unittest discover -s tests -p "test_*.py"`
  * Kết quả: `Ran 7 tests in 0.003s. OK`.
- **Kiểm tra định dạng git diff:**
  `git diff --check`
  * Kết quả: Sạch (0 lỗi khoảng trắng).
- **Kiểm tra xác thực dự án:**
  `uv run python scripts/validate_project.py`
  * Kết quả: `Project validation passed`.

---

## 7. Trạng Thái Hoàn Thành
`X7H_R1_READY_FOR_INDEPENDENT_REVIEW`
