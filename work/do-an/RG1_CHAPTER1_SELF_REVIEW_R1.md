# BÁO CÁO TỰ ĐÁNH GIÁ CHƯƠNG 1 (RG1_CHAPTER1_SELF_REVIEW_R1)
## BÀI KIỂM THỬ GIẢNG VIÊN (LECTURER TEST) — VÒNG HIỆU CHỈNH R2

- **Giai đoạn thực hiện:** RG1 R2 — Hiệu chỉnh giới hạn kỹ thuật và chuẩn hóa nguồn học thuật sau Independent External Review R1.
- **Tệp được đánh giá:** `work/do-an/CHAPTER_1.md`
- **Tệp đối chiếu liên quan:** `work/do-an/RG1_CHAPTER1_SOURCE_AUDIT_R1.md`, `work/do-an/RG1_CHAPTER1_CHANGELOG_R1.md`
- **Nhánh:** `feature/rg1-ch1-argument-realignment`
- **Thời gian lập:** 06/10/2026

---

## 1. Kết quả kiểm tra chi tiết theo 11 tiêu chí đánh giá học thuật

### Tiêu chí 1: Chương 1 có sử dụng Windows Server 2012 R2 là hệ điều hành mục tiêu thực nghiệm duy nhất không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Mục 1.1.3 (Dòng 52): Định danh Windows Server 2012 R2 là hệ điều hành mục tiêu thực nghiệm của đồ án.
  - Bảng 1.3 (Dòng 115): Gán nhãn duy nhất `Máy chủ mục tiêu thực nghiệm (KB4012213 / KB4012216, srv.sys >= 6.3.9600.18604)` cho Windows Server 2012 R2.
  - Mục 1.2.4 (Dòng 159–162): Dẫn chứng 3 căn cứ kỹ thuật có cơ sở: (1) là đối tượng mục tiêu thực nghiệm thực tế và thuộc danh mục MS17-010 [7]; (2) Microsoft có tài liệu hỗ trợ kỹ thuật chính thức Article 4023262 [21]; (3) nền tảng hỗ trợ đồng thời cả SMBv1 và SMBv2/SMBv3 phục vụ việc đối chiếu độc lập giữa các trục bằng chứng.
  - Toàn văn bản không còn bất kỳ câu nào coi Windows 7 là máy mục tiêu lab.

---

### Tiêu chí 2: Công cụ Metasploit có hoàn toàn vắng mặt trong tư cách công cụ thực nghiệm không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Mục 1.3.4 là `Cơ sở xác minh trạng thái bản vá cục bộ trên Windows Server 2012 R2`, hoàn toàn không có Metasploit.
  - Toàn bộ từ khóa `Metasploit`, `ms17_010_eternalblue`, `auxiliary/scanner`, `exploit/windows` đạt 0 lượt xuất hiện trong văn xuôi phân tích và bảng đo đạc. Từ khóa URL trong danh mục tài liệu tham khảo cho nguồn Rapid7 [14] (S013) được phân loại chính xác là đường dẫn thư mục học thuật.
  - Bảng 1.4 và Sơ đồ 1.4 chỉ ghi nhận các công cụ thực tế: Nmap, NSE, PowerShell, pfSense.

---

### Tiêu chí 3: Việc thực nghiệm kiểm chứng khai thác RCE có hoàn toàn vắng mặt không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Mục 1.2.1 (Dòng 92): Nêu rõ đồ án tập trung vào phương pháp luận khảo sát, nhận diện dấu hiệu dịch vụ và kiểm chứng bản vá, hoàn toàn không thực hiện hành vi khai thác xâm nhập hay thực thi mã trái phép trong mô hình thực nghiệm.
  - Mục 1.2.3 (Dòng 133): Khẳng định đồ án không thực hiện chuỗi tấn công can thiệp bộ nhớ hay tạo phiên đặc quyền `SYSTEM` trong phòng thí nghiệm; đề tài chỉ sử dụng lý thuyết FEA để hiểu rõ cơ chế lỗi bên trong của driver `srv.sys`.
  - Không tồn tại bất kỳ "Cấp độ 4 Exploit Validation" nào trong mô hình đánh giá.

---

### Tiêu chí 4: Cơ sở lý thuyết có giải thích thỏa đáng vì sao nhóm lỗ hổng MS17-010 đặc biệt nghiêm trọng không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Mục 1.2.3 phân tích sâu cơ chế tràn bộ nhớ nhân tại hàm `SrvOs2FeaToNt` trong driver `srv.sys` do ép kiểu không an toàn DWORD $\rightarrow$ WORD ($L_{write} > L_{alloc}$) [14].
  - Giải thích cơ chế kỹ thuật Pool Grooming điều hướng con trỏ hàm `srvnet!SrvNetWskReceiveComplete`.
  - Phân tích rủi ro đối với bộ ba C-I-A tại Mục 1.2.5; nêu rõ sự cố hỏng bộ nhớ nhân có thể gây lỗi dừng hệ thống (BSOD) khiến tính sẵn sàng là tác động cần xem xét (đã loại bỏ ngôn ngữ xếp hạng xác suất vô căn cứ).
  - Dẫn chứng hai chiến dịch mã độc WannaCry [16] và NotPetya [13] dựa trên các báo cáo chính thức của Microsoft Threat Intelligence (đã loại bỏ số liệu quy đổi tiền tệ không có nguồn).

---

### Tiêu chí 5: Người đọc có phân biệt được rạch ròi bốn trạng thái: cổng mạng, phương ngữ, tín hiệu quét lỗ hổng và trạng thái bản vá không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Bảng 1.5 tại Mục 1.4.1 phân định độc lập bốn trục bằng chứng:
    1. *Trục 1 (Reachability):* Cổng TCP 139/445 mở chỉ xác nhận dịch vụ tiếp nhận kết nối giao vận (`445 OPEN != vulnerable`).
    2. *Trục 2 (Protocol Surface):* Phương ngữ `NT LM 0.12` xác nhận dịch vụ hỗ trợ SMBv1, nhưng không đồng nghĩa hệ thống chưa vá (`SMBv1 enabled != MS17-010 confirmed`).
    3. *Trục 3 (Scanner Signal):* Nmap NSE đo đạc phản ứng NT Status từ xa; nếu không có kết quả hợp lệ, ghi nhận trạng thái không xác định (`UNKNOWN != SAFE`).
    4. *Trục 4 (Local Patch State):* Trạng thái kiểm tra Hotfix và tệp `srv.sys` nội bộ độc lập với góc nhìn từ xa; local `UNPATCHED` không tự biến remote `UNKNOWN` thành `VULNERABLE`.

---

### Tiêu chí 6: Chương 1 có giải thích đầy đủ vì sao việc xác minh bản vá cục bộ là bắt buộc không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Mục 1.3.4 phân tích rằng tín hiệu quét từ xa phụ thuộc vào đường truyền mạng và các điều kiện lọc gói trung gian.
  - Bản vá sửa đổi trực tiếp mã nhị phân của tệp driver nhân `srv.sys` trên đĩa cứng; việc xác minh trực tiếp 4 trường thuộc tính nhị phân của tệp (`FileMajorPart`, `FileMinorPart`, `FileBuildPart`, `FilePrivatePart`) và Hotfix là phương pháp duy nhất để kiểm tra cấu trúc mã nguồn đã được cập nhật hay chưa.
  - Nêu rõ chuẩn kỹ thuật Microsoft Article 4023262: phiên bản tệp `srv.sys` tối thiểu đã cập nhật đối với MS17-010 là **`6.3.9600.18604`** [21]. Đạt phiên bản này chỉ xác thực hệ thống đã cập nhật đối với MS17-010, không chứng nhận an toàn toàn hệ thống.

---

### Tiêu chí 7: Phần nguyên tắc giảm thiểu có phân biệt rõ ràng ba tầng kiểm soát: cập nhật hệ thống, làm cứng giao thức và kiểm soát mạng không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Mục 1.4.3 phân định ba tầng kiểm soát độc lập và nguyên tắc tái kiểm thử:
    1. *Tầng cập nhật hệ thống (Patching Layer):* Thay thế tệp `srv.sys` ($\geq 6.3.9600.18604$), giải quyết lỗi logic được công bố trong bản tin MS17-010 (mốc tham chiếu lý thuyết). Đã loại bỏ hoàn toàn các từ ngữ tuyệt đối hóa như "hoàn toàn miễn nhiễm", "triệt để tận gốc".
    2. *Tầng giảm thiểu mức giao thức (Protocol Hardening Layer – Case B):* Tắt cấu hình SMBv1 qua PowerShell (`Set-SmbServerConfiguration -EnableSMB1Protocol $false`), làm giảm bề mặt tiếp xúc của giao thức và loại bỏ `NT LM 0.12` khỏi danh sách đàm phán đo đạc. Phân biệt rõ với gỡ gói tính năng (`FS-SMB1 uninstalled`) và giữ vững: `SMBv1 disabled != PATCHED`. Đã loại bỏ các từ "triệt tiêu hoàn toàn", "đóng kín bề mặt".
    3. *Tầng kiểm soát truy cập mạng (Network Access Control Layer – Case C):* Tường lửa lọc gói tin tại ranh giới mạng theo chuẩn NIST SP 800-41 Rev. 1 [15], hạn chế khả năng tiếp cận dịch vụ qua đường truyền kiểm soát. Không làm lộ kết quả thực nghiệm Chương 3 (`open -> filtered`), không đưa giả định sai về subnet. Giữ vững: `FILTERED != PATCHED`.
    4. *Nguyên tắc tái kiểm thử (Retest):* Phân biệt rõ khuyến nghị vận hành thực tế (kiểm tra tương thích ứng dụng) với phạm vi đo đạc của đề tài (chỉ kiểm tra lại các biến số/dialect/NSE đã khóa). Khẳng định việc còn lại các phương ngữ SMB2/3 không tự chứng minh mọi tải công việc nghiệp vụ hoạt động liên tục.

---

### Tiêu chí 8: Mô hình mạng giả định cũ (ba VLAN, Client nghiệp vụ, phân vùng khác) có hoàn toàn bị loại bỏ không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Rà soát tự động đạt kết quả: 0 lượt xuất hiện của `Client nghiệp vụ`, 0 lượt của `ba VLAN`, 0 lượt của `phân vùng khác`.
  - Mô tả mạng chuẩn xác: Trạm kiểm thử độc lập (Kali Linux) và máy chủ mục tiêu (Windows Server 2012 R2) được phân tách qua thiết bị tường lửa trung gian kiểm soát đường truyền.

---

### Tiêu chí 9: Chương 1 có chuẩn bị nền tảng tự nhiên và trực tiếp phục vụ Chương 2 không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Sơ đồ 1.4 định hình quy trình 4 pha đo đạc chuẩn mực.
  - Bảng 1.4 liên kết trực tiếp các khái niệm lý thuyết với 8 phép đo kỹ thuật thực tế trong phòng thí nghiệm.
  - Tổng kết Chương 1 khẳng định mô hình bốn trục bằng chứng độc lập đặt nền móng phương pháp luận vững chắc cho thiết kế mô hình thực nghiệm, kịch bản đo đạc và tiêu chí đánh giá trong Chương 2.

---

### Tiêu chí 10: Danh mục tài liệu tham khảo có đầy đủ, tuần tự và có căn cứ không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Danh mục gồm 21 tài liệu chuẩn IEEE [1] đến [21].
  - 100% (21/21) tài liệu đều map trực tiếp vào các nguồn `VERIFIED` trong `SOURCE_LEDGER.md`.
  - 0 nguồn `RECHECK` được sử dụng, 0 nguồn giả định (không có RFC hay pfSense documentation giả định).
  - Khớp nối hoàn hảo: Mọi chỉ số trích dẫn trong thân bài đều có trong danh mục và ngược lại.

---

### Tiêu chí 11: Văn phong có đúng chuẩn báo cáo kỹ thuật của sinh viên đại học Việt Nam, không chứa biệt ngữ quản trị/QA không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Giọng văn trang trọng, chuẩn mực học thuật, sử dụng ngôi thứ ba trung tính ("đồ án", "nghiên cứu", "người đánh giá").
  - Quét tự động các từ khóa quản trị/QA nội bộ: `canonical` (0), `gate` (0), `Evidence ID` (0), `ground truth` (0), `governance` (0).
  - Thuật ngữ kỹ thuật được sử dụng chính xác: `SYSTEM` / `LocalSystem` được định nghĩa là ngữ cảnh bảo mật và tài khoản người dùng có đặc quyền cao; không gán nguyên nhân giả định cho trạng thái UNKNOWN; kết quả âm tính được gọi là "kết quả âm tính theo tiêu chí của phép đo".

---

## 2. Kết luận chung

Tất cả **11/11 tiêu chí** trong Bài kiểm thử giảng viên (Lecturer Test) đều đạt kết quả **PASS**. Không còn bất kỳ sự rò rỉ kết quả thực nghiệm nào, không có khẳng định suy diễn vượt quá bằng chứng nguồn, và toàn bộ hệ thống nguồn học thuật đã được chuẩn hóa đồng bộ với `SOURCE_LEDGER.md`. Văn bản Chương 1 hoàn toàn sẵn sàng cho vòng đánh giá độc lập bên ngoài cuối cùng.
