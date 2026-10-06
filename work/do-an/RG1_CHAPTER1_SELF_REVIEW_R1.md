# BÁO CÁO TỰ ĐÁNH GIÁ CHƯƠNG 1 (RG1_CHAPTER1_SELF_REVIEW_R1)
## BÀI KIỂM THỬ GIẢNG VIÊN (LECTURER TEST)

- **Giai đoạn thực hiện:** RG1 — Chỉnh lý toàn diện Chương 1 theo lập luận thực nghiệm chuẩn mực.
- **Tệp được đánh giá:** `work/do-an/CHAPTER_1.md`
- **Nhánh:** `feature/rg1-ch1-argument-realignment`
- **Thời gian lập:** 06/10/2026

---

## 1. Kết quả kiểm tra chi tiết theo 11 tiêu chí đánh giá

### Câu hỏi 1: Chương 1 có sử dụng Windows Server 2012 R2 là hệ điều hành mục tiêu thực nghiệm duy nhất không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Tại Mục 1.1.3 (Dòng 52): "Hệ điều hành mục tiêu thực nghiệm của đồ án — Windows Server 2012 R2 — hỗ trợ đồng thời cả ba thế hệ SMB..."
  - Tại Bảng 1.3 (Dòng 115): Dòng Windows Server 2012 R2 được định danh là `Máy chủ mục tiêu thực nghiệm (KB4012213 / KB4012216, srv.sys >= 6.3.9600.18604)`.
  - Tại Mục 1.2.4 (Dòng 149–168): Đề tài dành trọn vẹn tiểu mục để giải thích lý do lựa chọn Windows Server 2012 R2 dựa trên 3 tiêu chí kỹ thuật: tính đại diện máy chủ doanh nghiệp, tài liệu xác minh bản vá chính thức Article 4023262 của Microsoft, và tính độc lập của các trục bằng chứng.
  - Hoàn toàn không còn bất kỳ câu văn nào coi Windows 7 là máy mục tiêu lab (đã rà soát 0 lượt xuất hiện của cụm từ "Windows 7" trong vai trò mục tiêu thực nghiệm).

---

### Câu hỏi 2: Công cụ Metasploit có hoàn toàn vắng mặt trong tư cách công cụ thực nghiệm không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Tiêu đề cũ `1.3.4. Nền tảng kiểm thử Metasploit Framework` đã được thay thế hoàn toàn bằng `1.3.4. Cơ sở xác minh trạng thái bản vá cục bộ trên Windows Server 2012 R2`.
  - Toàn bộ từ khóa liên quan như `Metasploit`, `ms17_010_eternalblue`, `auxiliary/scanner`, `exploit/windows` đã bị xóa bỏ 100% khỏi văn bản (kết quả grep search: 0 hits).
  - Bảng 1.4 và Sơ đồ 1.4 không còn bất kỳ dòng đo đạc hay module quét/khai thác nào của Metasploit; chỉ sử dụng Nmap, NSE, PowerShell và pfSense.

---

### Câu hỏi 3: Việc thực nghiệm kiểm chứng khai thác RCE có hoàn toàn vắng mặt không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Mô hình thực nghiệm của đề tài chỉ đo đạc các phản ứng giao thức không xâm nhập (safe probe), đọc banner, kiểm tra cấu hình nội bộ và trạng thái cổng mạng.
  - Toàn bộ khái niệm "Cấp độ 4: Thực thi mã thử nghiệm (Exploitation Validation)" trong bản thảo cũ đã bị loại bỏ hoàn toàn.
  - Tại Mục 1.2.1 (Dòng 92): Nêu rõ "đồ án tập trung vào phương pháp luận khảo sát, nhận diện dấu hiệu dịch vụ và kiểm chứng trạng thái bản vá an toàn, hoàn toàn không thực hiện hành vi khai thác xâm nhập hay thực thi mã trái phép trong mô hình thực nghiệm."
  - Tại Mục 1.2.3 (Dòng 133): Nêu rõ "đề tài hoàn toàn không thực hiện chuỗi tấn công khai thác vùng nhớ hay tạo phiên `SYSTEM` trong phòng thí nghiệm; đề tài chỉ sử dụng lý thuyết FEA để hiểu rõ cơ chế lỗi bên trong của driver `srv.sys`..."

---

### Câu hỏi 4: Cơ sở lý thuyết có giải thích thỏa đáng vì sao nhóm lỗ hổng MS17-010 đặc biệt nghiêm trọng không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Mục 1.2.3 phân tích sâu cơ chế tràn bộ nhớ nhân tại hàm `SrvOs2FeaToNt` trong driver `srv.sys` do ép kiểu không an toàn DWORD $\rightarrow$ WORD ($L_{write} > L_{alloc}$).
  - Giải thích cơ chế kỹ thuật Pool Grooming điều hướng con trỏ hàm `srvnet!SrvNetWskReceiveComplete`.
  - Phân tích mức độ rủi ro đối với bộ ba C-I-A tại Mục 1.2.5, đặc biệt nhấn mạnh nguy cơ sập nhân (BSOD) gây mất tính sẵn sàng hệ thống.
  - Dẫn chứng hai chiến dịch tấn công quy mô toàn cầu WannaCry và NotPetya tại Mục 1.2.6 để khẳng định tính cấp thiết trong bảo mật dịch vụ SMB.

---

### Câu hỏi 5: Người đọc có phân biệt được rạch ròi bốn trạng thái: cổng mạng, phương ngữ, tín hiệu quét lỗ hổng và trạng thái bản vá không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Bảng 1.5 tại Mục 1.4.1 phân tách độc lập bốn trục bằng chứng:
    1. *Khả năng tiếp cận tầng mạng (TCP 139/445):* Cổng `open` chỉ xác nhận dịch vụ phản hồi kết nối giao vận (`445 OPEN != vulnerable`).
    2. *Bề mặt giao thức SMB:* Phương ngữ `NT LM 0.12` xác nhận tính năng SMBv1 tồn tại, nhưng không đồng nghĩa hệ thống chưa vá (`SMBv1 enabled != MS17-010 confirmed`).
    3. *Tín hiệu thăm dò lỗ hổng từ xa (Nmap NSE):* Dấu hiệu `VULNERABLE` dựa trên mã lỗi `STATUS_INSUFF_SERVER_RESOURCES`; trường hợp bị chặn mạng xuất trạng thái không xác định (`UNKNOWN != SAFE`).
    4. *Trạng thái bản vá nội bộ:* Dựa trên Hotfix và phiên bản nhị phân `srv.sys`; trạng thái nội bộ không làm biến đổi kết quả quét từ xa nếu góc nhìn mạng bị thiếu dữ liệu.

---

### Câu hỏi 6: Chương 1 có giải thích đầy đủ vì sao việc xác minh bản vá cục bộ là bắt buộc không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Mục 1.3.4 phân tích rằng các phép quét từ xa phụ thuộc hoàn toàn vào đường truyền mạng và các điều kiện lọc gói trung gian.
  - Bản vá cập nhật mã nguồn driver `srv.sys` nằm trên đĩa cứng hệ điều hành; phương pháp duy nhất để kiểm tra cấu trúc mã nguồn đã được sửa lỗi triệt để hay chưa là truy vấn trực tiếp thuộc tính nhị phân của tệp `srv.sys` và mã định danh Hotfix theo tài liệu hướng dẫn kỹ thuật Article 4023262 của Microsoft.
  - Nêu rõ ngưỡng an toàn phiên bản nhị phân `srv.sys` $\geq 6.3.9600.18604$.

---

### Câu hỏi 7: Phần nguyên tắc giảm thiểu có phân biệt rõ ràng ba tầng kiểm soát: cập nhật hệ thống, làm cứng giao thức và kiểm soát mạng không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Mục 1.4.3 phân định rõ ba tầng kiểm soát độc lập:
    1. *Tầng cập nhật hệ thống (Patching Layer):* Thay thế mã nhị phân driver `srv.sys` ($\geq 6.3.9600.18604$), giải quyết triệt để lỗi gốc. Nêu rõ đây là mốc tham chiếu lý thuyết.
    2. *Tầng giảm thiểu mức giao thức (Protocol Hardening Layer - Case B):* Tắt SMBv1 bằng PowerShell, triệt tiêu bề mặt đàm phán phương ngữ cũ nhưng không thay đổi tệp `srv.sys` trên đĩa (`SMBv1 disabled != PATCHED`).
    3. *Tầng kiểm soát truy cập mạng (Network Access Control Layer - Case C):* Tường lửa pfSense Transparent Bridge cô lập cổng ở tầng mạng, chuyển trạng thái sang `filtered` nhưng không giải quyết nguy cơ nội bộ cùng phân đoạn (`FILTERED != PATCHED`).
    4. *Nguyên tắc tái kiểm thử (Retest):* Xác thực biến số mục tiêu đã thay đổi và chức năng hợp lệ không bị gián đoạn.

---

### Câu hỏi 8: Mô hình mạng giả định cũ (ba VLAN, Client nghiệp vụ, phân vùng khác) có hoàn toàn bị loại bỏ không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Đã rà soát và xóa bỏ toàn bộ các cụm từ: "Client nghiệp vụ", "ba VLAN", "phân vùng khác".
  - Mô tả chính xác thiết kế mạng: trạm kiểm thử độc lập (Kali Linux) và máy chủ mục tiêu (Windows Server 2012 R2) được phân tách qua thiết bị tường lửa trung gian Transparent Bridge pfSense.

---

### Câu hỏi 9: Chương 1 có chuẩn bị nền tảng tự nhiên và trực tiếp phục vụ Chương 2 không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Bảng 1.4 liên kết trực tiếp các khái niệm lý thuyết với các tham số cấu hình, công cụ và câu lệnh đo đạc thực tế trong phòng thí nghiệm.
  - Sơ đồ 1.4 định hình quy trình đo đạc 4 pha logic: Khảo sát mạng $\rightarrow$ Khảo sát giao thức $\rightarrow$ Thăm dò lỗ hổng an toàn $\rightarrow$ Xác minh nội bộ và tái kiểm thử đa biến.
  - Phần Tổng kết Chương 1 khẳng định việc phân tách bốn trục bằng chứng đặt nền móng phương pháp luận vững chắc cho việc thiết kế kiến trúc lab, xây dựng kịch bản đo đạc và tiêu chí đánh giá kết quả trong Chương 2.

---

### Câu hỏi 10: Danh mục tài liệu tham khảo có đầy đủ, tuần tự và có căn cứ không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Danh mục gồm 21 tài liệu tham khảo chính thức, chuẩn hóa theo định dạng IEEE.
  - Đánh số tuần tự từ `[1]` đến `[21]`, 100% tài liệu đều được trích dẫn cụ thể trong thân bài (không có trích dẫn mồ côi hay trích dẫn thiếu).
  - Đã loại bỏ các trích dẫn Metasploit cũ (`[21]`, `[22]`) và bổ sung tài liệu chuẩn Microsoft Support Article 4023262 (`[21]`).

---

### Câu hỏi 11: Văn phong có đúng chuẩn báo cáo kỹ thuật của sinh viên đại học Việt Nam, không chứa biệt ngữ quản trị/QA không?
- **Đánh giá:** **PASS**
- **Căn cứ chứng minh:**
  - Giọng văn trang trọng, khách quan, sử dụng ngôi thứ ba trung tính ("đồ án", "nghiên cứu", "người đánh giá").
  - Hoàn toàn không sử dụng các từ ngữ quy trình nội bộ: `canonical`, `gate`, `Evidence ID`, `ground truth`, `governance` (kết quả rà soát: 0 hits).
  - Các lập luận chuyển ý diễn ra mạch lạc, tự nhiên; các thuật ngữ kỹ thuật chuyên ngành tiếng Anh đều có phần giải nghĩa tiếng Việt chuẩn xác kèm theo.

---

## 2. Kết luận chung

Tất cả 11/11 tiêu chí trong Bài kiểm thử giảng viên (Lecturer Test) đều đạt kết quả **PASS**. Văn bản Chương 1 đã hoàn toàn thoát khỏi tàn dư của mô hình cũ, thiết lập cơ sở lý thuyết chuẩn mực và vững chắc, sẵn sàng bàn giao sang bước đánh giá độc lập bên ngoài.
