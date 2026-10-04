# Đánh giá Defense Readiness: Chương 1 (Mục 1.2, 1.3, 1.4)

- **Dự án:** Đồ án chuyên ngành An toàn thông tin (`work/do-an`)
- **Tài liệu đánh giá:** [work/do-an/CHAPTER_1.md](file:///e:/word_ppt-auto/work/do-an/CHAPTER_1.md) (các mục 1.2, 1.3, 1.4)
- **Quy tắc áp dụng:** [work/do-an/DEFENSE_READINESS.md](file:///e:/word_ppt-auto/work/do-an/DEFENSE_READINESS.md) (DEC-24, ngày 2026-10-04)
- **Thời điểm thực hiện:** 2026-10-04
- **Trạng thái:** `DEFENSE_REVIEW_IN_PROGRESS`

---

## 1. Phạm vi Review

Đánh giá tính sẵn sàng bảo vệ (Defense Readiness), cơ sở bằng chứng (Evidence) và tính chặt chẽ của lập luận (Logic) đối với ba mục trọng tâm của Chương 1:
- **Mục 1.2:** Lỗ hổng bảo mật MS17-010 (1.2.1 – 1.2.6)
- **Mục 1.3:** Công cụ phục vụ kiểm thử (1.3.1 – 1.3.5)
- **Mục 1.4:** Tiêu chí xác minh trạng thái SMB và MS17-010 (1.4.1 – 1.4.5)

Mục 1.1 được bảo toàn nguyên vẹn; không sửa đổi các quyết định đã khóa (LOCKED), không đưa ra số liệu thực nghiệm giả định, và không merge vào branch chính.

---

## 2. Các Luận Điểm Trọng Tâm Liên Quan

1. **C002 (Nguyên nhân lỗ hổng):** Bản tin MS17-010 bao gồm 6 CVE khác nhau; trong đó CVE-2017-0144 phát sinh từ lỗi kiểm soát kích thước dữ liệu FEA trong driver `srv.sys` ở Kernel Mode, cho phép thực thi mã từ xa mà không yêu cầu xác thực.
2. **C003 (Phương pháp luận nhận diện và xác minh):** Đánh giá an ninh SMB phải phân định rạch ròi 4 mức độ: (1) Khả năng tiếp cận cổng, (2) Nhận diện giao thức SMBv1, (3) Dấu hiệu lỗ hổng qua thăm dò phản hồi, và (4) Xác minh tác động thực tế có kiểm soát.
3. **C004 (An toàn kiểm thử):** Các phép đo mạng từ xa (Black-box) có giới hạn cố hữu; kết quả từ công cụ quét chỉ là chỉ báo kỹ thuật, không thể thay thế cho việc xác minh trạng thái nội tại (White-box) và cần kiểm soát rủi ro mất ổn định hệ thống.

---

## 3. Bảng Tổng Hợp Defense Cards (DR-C1-01 đến DR-C1-08)

| Card ID | Tiêu đề | Claim Type | Trạng thái ban đầu | Trạng thái sau rà soát | Hướng xử lý nội dung trong Chapter 1 |
|---|---|---|:---:|:---:|---|
| **DR-C1-01** | Trọng tâm CVE-2017-0144 | method/design decision | `AUTHOR_CONFIRM` | `READY` (đã truy vết) | Nêu rõ căn cứ lựa chọn bám sát RQ2/O2; không tự gán cảm xúc cá nhân. |
| **DR-C1-02** | Cơ sở của khung 4 mức | interpretation / method | `AUTHOR_CONFIRM` | `READY` (đã truy vết) | Giữ vững 4 mức phân định theo quyết định của tác giả tại AUTHOR_VOICE (DEC-05). |
| **DR-C1-03** | Ranh giới chứng minh từng mức | interpretation / conclusion | `EVIDENCE_GAP` | `SIMPLIFY` / Khép Gap | Phân định rạch ròi 3 trục tại mỗi mức: Quan sát trực tiếp, Ý nghĩa kỹ thuật, Ranh giới kết luận. |
| **DR-C1-04** | Chuỗi công cụ kiểm thử | method/design decision | `AUTHOR_CONFIRM` | `READY` (đã truy vết) | Trình bày theo luồng: Đầu vào $\to$ Quan sát $\to$ Đầu ra $\to$ Tiền đề bước sau. |
| **DR-C1-05** | Tính độc lập giữa NSE & MSF | interpretation / conclusion | `EVIDENCE_GAP` | Khép Gap / Sửa nội dung | **Sửa sai lệch kỹ thuật:** Khẳng định NSE và MSF scanner dùng chung tín hiệu logic (không độc lập); chỉ là hai bản cài đặt khác nhau. |
| **DR-C1-06** | Đối chiếu Black-box vs White-box | interpretation / method | `AUTHOR_CONFIRM` | `READY` (đã truy vết) | Xác định là nguyên tắc phương pháp luận định hướng cho Chương 2/3, không tuyên bố là kết quả đã làm. |
| **DR-C1-07** | Mức độ làm chủ cơ chế FEA | source fact / interpretation | `AUTHOR_CONFIRM` | `SIMPLIFY` | Giữ nguyên lý tính sai kích thước $\to$ Kernel Pool Overflow; giữ tên hàm ở dạng tham chiếu kỹ thuật, không sa đà exploit RE. |
| **DR-C1-08** | Mức 4 và giới hạn kết luận | conclusion / method | `EVIDENCE_GAP` | Khép Gap / Sửa nội dung | Phân biệt rõ việc đạt phiên tương tác (RCE) với việc quan sát trực tiếp vùng nhớ nhân từ xa; BSOD là mất ổn định chứ không phải RCE. |

---

## 4. Chi Tiết Từng Defense Card Sau Khi Rà Soát

### DR-C1-01 — Trọng tâm CVE-2017-0144
- **Mục liên quan:** §1.2.1, §1.2.2.
- **Loại claim:** `method/design decision`.
- **Khẳng định:** Đồ án chọn CVE-2017-0144 làm đối tượng nghiên cứu và kiểm thử trung tâm trong nhóm MS17-010.
- **Bằng chứng hỗ trợ:** RESEARCH_MAP (RQ2, O2); DEC-06 (phê duyệt G1); DEC-09 (Hợp đồng Chương 1); CLAIM_MATRIX (C002); nguồn S005, S011, S013.
- **Truy vết xác nhận của tác giả:**
  - Quyết định: `DEC-06` (Khóa bản đồ nghiên cứu 4 RQ và 4 Mục tiêu, ngày 2026-09-12).
  - Vị trí: Dòng DEC-06 trong bảng quyết định `PROJECT_STATE.md`.
  - Nội dung: Tác giả trực tiếp phê duyệt RQ2 ("Cơ chế phát sinh lỗi bộ nhớ dẫn đến nhóm lỗ hổng MS17-010 (CVE-2017-0144)...") và O2 làm trọng tâm.
- **Ranh giới bằng chứng:** Việc chọn CVE-2017-0144 là quyết định phạm vi kỹ thuật của đồ án; không dùng cơ chế của CVE này để đại diện cho toàn bộ 5 CVE còn lại trong bản tin MS17-010.
- **Tác giả cần giải thích:** MS17-010 gồm 6 CVE khác nhau; CVE-2017-0144 đại diện cho lỗi tràn bộ nhớ nhân qua SMBv1 FEA không cần xác thực, trực tiếp phục vụ mục tiêu đánh giá dịch vụ mạng của đồ án.
- **Trạng thái:** `READY`.

---

### DR-C1-02 — Vì sao dùng khung bốn mức
- **Mục liên quan:** §1.4 (1.4.1 – 1.4.5).
- **Loại claim:** `method/design decision`, `interpretation`.
- **Khẳng định:** Đánh giá trạng thái SMB và MS17-010 cần phân rã thành 4 mức quan sát thay vì chỉ đưa ra kết luận nhị phân có/không lỗ hổng.
- **Bằng chứng hỗ trợ:** CLAIM_MATRIX (C003); DEC-12, DEC-17, DEC-18; nguồn S017, S018, S022, S029, S030, S013.
- **Truy vết xác nhận của tác giả:**
  - Quyết định: `DEC-05` (Phê duyệt cổng G0_INTAKE, ngày 2026-09-12) và `AUTHOR_VOICE.md` (mục "Dấu ấn riêng của công trình", dòng 67–71).
  - Vị trí: Dòng DEC-05 trong bảng quyết định và mục "Hiệu chỉnh đã được tác giả duyệt ngày 2026-10-04" trong `PROJECT_STATE.md`.
  - Nội dung tác giả đã xác nhận: "Những lựa chọn do tác giả trực tiếp đưa ra: Phân định rạch ròi 4 cấp độ: Phát hiện cổng 445 mở $\to$ Nhận diện phiên bản SMBv1 $\to$ Dấu hiệu nghi ngờ qua NSE $\to$ Xác minh lỗ hổng bằng phản hồi gói tin chuẩn. Lý do thật: Tránh dương tính giả; ngăn chặn nguy cơ crash hệ thống (BSOD) do corrupt kernel pool khi chạy module khai thác; và đảm bảo không phá vỡ tính tương thích của hệ thống mạng."
- **Ranh giới bằng chứng:** Khung 4 mức là phương pháp luận cấu trúc dữ liệu thực nghiệm do nhóm xây dựng cho đề tài, không phải tiêu chuẩn quốc tế độc lập.
- **Tác giả cần giải thích:** Giải thích được tại sao một cổng mở không chứng minh được lỗ hổng và tại sao cần từng bậc thông tin để tránh chẩn đoán sai.
- **Trạng thái:** `READY`.

---

### DR-C1-03 — Mỗi mức chứng minh và không chứng minh gì
- **Mục liên quan:** §1.3.2, §1.3.3, §1.4.1 – §1.4.4.
- **Loại claim:** `interpretation`, `conclusion`.
- **Khẳng định:** Mỗi mức có điều quan sát được, điều suy luận có điều kiện và điều hoàn toàn chưa thể kết luận.
- **Bằng chứng hỗ trợ:** S017 (Nmap port scanning), S029 (`smb-protocols.nse`), S018 (`smb-vuln-ms17-010.nse`), S013 (Metasploit).
- **Phân tích khoảng trống (Evidence Gap cũ):**
  - Mức 1 (TCP SYN-ACK): Chỉ chứng minh cổng có dịch vụ lắng nghe ở tầng giao vận; chưa chứng minh dịch vụ đó đang xử lý SMB ở tầng ứng dụng bình thường.
  - Mức 2 (Dialect `NT LM 0.12`): Chứng minh dịch vụ chấp thuận giao thức SMBv1; không quan sát trực tiếp được driver `srv.sys` trong kernel từ góc nhìn mạng.
  - Mức 3 (Mã lỗi 0xC0000205): Là chỉ báo logic về việc máy chủ phân nhánh xử lý lỗi; không chứng minh chắc chắn việc khai thác sẽ thành công. Mã lỗi 0xC0000022 cũng không chứng minh máy đã vá an toàn (có thể do cấu hình chặn tài khoản nặc danh).
  - Mức 4 (Can thiệp): Can thiệp thất bại không đồng nghĩa máy chủ an toàn; BSOD chỉ chứng minh mất tính sẵn sàng chứ không chứng minh thực thi mã thành công.
- **Cách xử lý trong văn bản:** Chuẩn hóa từng tiểu mục 1.4.1–1.4.4 thành 3 khối rõ ràng:
  - *Dấu hiệu quan sát (Observation):* Dữ liệu gói tin thu nhận.
  - *Ý nghĩa kỹ thuật (Interpretation):* Kết luận có điều kiện ở tầng giao thức.
  - *Ranh giới kết luận (Inference Boundary):* Các điều chưa biết và không được suy diễn.
- **Trạng thái:** `SIMPLIFY` (Khép kín Evidence Gap bằng cách chuẩn hóa ranh giới suy luận).

---

### DR-C1-04 — Chuỗi Nmap $\to$ NSE $\to$ Metasploit
- **Mục liên quan:** §1.3.2 – §1.3.5.
- **Loại claim:** `method/design decision`.
- **Khẳng định:** Công cụ được triển khai theo chuỗi lũy tiến: Nmap quét cổng $\to$ NSE nhận diện dialect và dấu hiệu $\to$ Metasploit xác minh sâu hơn khi có điều kiện.
- **Bằng chứng hỗ trợ:** RESEARCH_MAP (M3, O3); DEC-13; CLAIM_MATRIX (C003, C004); S017, S018, S026, S027, S030, S013.
- **Truy vết xác nhận của tác giả:**
  - Quyết định: `DEC-06` (G1_RESEARCH_DESIGN) và `AUTHOR_VOICE.md` (Lý do chọn chuỗi công cụ có kiểm soát).
  - Vị trí: Dòng DEC-06 trong `PROJECT_STATE.md`.
  - Nội dung: Chuỗi công cụ phản ánh tiến trình trinh sát an ninh: giảm thiểu tối đa các gói tin can thiệp sâu khi chưa xác định được khả năng tiếp cận và phiên bản dịch vụ.
- **Tác giả cần giải thích:** Tại sao không chạy Metasploit ngay từ đầu? (Vì rủi ro làm crash dịch vụ/hệ thống do lỗi kernel pool nếu chạy mù quáng trên mục tiêu không phù hợp).
- **Trạng thái:** `READY`.

---

### DR-C1-05 — Đối chiếu công cụ có độc lập không (Khép Gap quan trọng)
- **Mục liên quan:** §1.3.4, §1.3.5.
- **Loại claim:** `interpretation`, `conclusion`.
- **Vấn đề phát hiện trong bản nháp cũ:**
  - Bản thảo cũ ghi: "Mô-đun `auxiliary/scanner/smb/smb_ms17_010` thực hiện quét độc lập, cung cấp dữ liệu đối chiếu chéo với kịch bản NSE nhằm tăng độ tin cậy của chỉ báo lỗ hổng" (dòng 252).
  - **Sai lệch kỹ thuật:** Cả kịch bản Nmap `smb-vuln-ms17-010.nse` (S018) và mô-đun Metasploit `auxiliary/scanner/smb/smb_ms17_010.rb` (S030) đều gửi cùng một dạng gói tin giao dịch thăm dò tới tài nguyên `IPC$` và cùng bắt mã trạng thái phản hồi `STATUS_INSUFF_SERVER_RESOURCES` (`0xC0000205`). Chúng sử dụng **cùng một tín hiệu kỹ thuật và cùng một cơ chế phân nhánh lỗi**, nên **hoàn toàn không phải là hai nguồn bằng chứng độc lập (independent sources)**!
  - Việc hai công cụ cùng báo dương tính chỉ giúp loại trừ lỗi phân tích cú pháp (parsing bug) của từng phần mềm cụ thể, chứ không loại trừ được các nguyên nhân sai số từ phía máy chủ (ví dụ chính sách mạng hoặc phản hồi bất thường).
- **Điều chỉnh bắt buộc trong Chương 1:**
  - Bỏ từ "độc lập" khi nói về hai công cụ quét này.
  - Viết chính xác: Đây là hai bản cài đặt (implementations) khác nhau của cùng một phương pháp thăm dò logic. Việc đối chiếu giúp kiểm chứng chéo sự nhất quán trong khâu phân tích cú pháp của công cụ kiểm thử, nhưng không tạo ra thêm bằng chứng mới độc lập về trạng thái máy chủ.
- **Trạng thái:** `Khép Gap / Đã sửa nội dung`.

---

### DR-C1-06 — Đối chiếu hộp đen và trạng thái nội tại
- **Mục liên quan:** §1.4.5.
- **Loại claim:** `interpretation`, `method/design decision`.
- **Khẳng định:** Mọi quan sát từ xa qua mạng (Black-box) đều có giới hạn; kết quả kiểm thử cần được đối chiếu với thông tin cấu hình nội tại (White-box: danh mục KB, trạng thái Registry/PowerShell của SMBv1) để đưa ra kết luận chuẩn xác.
- **Bằng chứng hỗ trợ:** S005 (bản tin MS17-010), S008 (thủ tục kiểm tra cấu hình SMB trên Windows), S024 (NIST SP 800-115); CHAPTER_ARGUMENT mục 2 & 3; DEC-17, DEC-18.
- **Truy vết xác nhận của tác giả:**
  - Quyết định: `DEC-18` (Chuẩn hóa góc nhìn trạm kiểm thử Attacker Vantage Point vs. trạng thái nội tại máy chủ Server Internal State, ngày 2026-09-12).
  - Vị trí: Dòng DEC-18 trong bảng quyết định `PROJECT_STATE.md`.
- **Ranh giới bằng chứng:** Nêu rõ đây là nguyên tắc phương pháp luận khoa học định hướng cho việc thiết kế lab ở Chương 2 và đánh giá ở Chương 3, không tự nhận là nhóm đã thu thập đầy đủ dữ liệu thực nghiệm nội tại ở giai đoạn Chương 1.
- **Trạng thái:** `READY`.

---

### DR-C1-07 — Mức FEA cần làm chủ
- **Mục liên quan:** §1.2.3.
- **Loại claim:** `source fact`, `interpretation`.
- **Khẳng định:** Root cause của CVE-2017-0144 là sự sai lệch giữa việc tính toán kích thước vùng nhớ (dùng hàm `SrvOs2FeaListSizeToNt`) và lượng dữ liệu thực tế được ghi vào (dùng hàm `SrvOs2FeaToNt`), dẫn đến tràn bộ đệm nhân (Kernel Pool Overflow).
- **Bằng chứng hỗ trợ:** S013 (Rapid7 Exploit Analysis), S005 (Microsoft Bulletin MS17-010).
- **Đánh giá mức độ cần thiết:**
  - Chi tiết về tên hai hàm xử lý FEA là đủ để minh chứng nguyên lý sai lệch kích thước mà không sa đà vào các kỹ thuật phân tích nhị phân phức tạp (như đảo ngược mã máy, phân tích địa chỉ hex, kỹ thuật xoay chuyển pool grooming chi tiết).
  - Nhóm em cần làm chủ chuỗi nhân quả: Kích thước tính thiếu $\to$ Cấp phát vùng đệm nhỏ $\to$ Ghi dữ liệu vượt quá $\to$ Tràn bộ nhớ nhân (Kernel Pool Overflow) $\to$ Nguy cơ BSOD hoặc thực thi mã.
- **Trạng thái:** `SIMPLIFY` (Giữ nguyên lý nhân quả cốt lõi, lược bỏ mọi chi tiết exploit development).

---

### DR-C1-08 — Cấp 4 và giới hạn kết luận xuyên chương
- **Mục liên quan:** §1.4.4.
- **Loại claim:** `conclusion`, `method/design decision`.
- **Khẳng định:** Xác minh Mức 4 thiết lập phiên tương tác chứng minh khả năng thực thi mã từ xa với đặc quyền cao; tuy nhiên, không được đồng nhất phiên tương tác từ xa với việc "quan sát trực tiếp bên trong không gian nhân". Hiện tượng BSOD chỉ chứng minh hệ thống mất ổn định (tính sẵn sàng bị ảnh hưởng), không được tính là khai thác thành công.
- **Bằng chứng hỗ trợ:** S013, S024; DEC-17, DEC-18.
- **Phân tích khoảng trống:** Bản nháp Chương 1 cần bảo đảm không khẳng định vượt quá những gì công cụ từ xa ghi nhận được. Khi trạm kiểm thử nhận được shell tương tác, đó là bằng chứng về quyền thực thi mã ở tầng ứng dụng/hệ thống, còn luồng xử lý trong nhân chỉ được suy luận gián tiếp.
- **Cách xử lý trong văn bản:** Ghi rõ ranh giới kết luận tại mục 1.4.4 để bảo đảm tính nhất quán xuyên suốt sang Chương 2 và Chương 3.
- **Trạng thái:** `Khép Gap / Đã sửa nội dung`.

---

## 5. Những Nội Dung Đã SIMPLIFY và Lược Bỏ

1. **Lược bỏ hoàn toàn chi tiết Reverse Engineering mã khai thác trong 1.2.3:**
   - Xóa bỏ việc giải thích phép tràn số 16-bit dạng `0x10040 -> 0x0040`.
   - Xóa bỏ con số cụ thể "64 byte" hay cơ chế sắp xếp vùng nhớ `srvnet.sys` chi tiết.
   - Xóa bỏ mô tả ghi đè con trỏ hàm (`function pointer`) và điều hướng CPU.
   - *Lý do:* Không phục vụ trực tiếp cho RQ2 và O2; khiến sinh viên dễ bị chất vấn vượt quá phạm vi đề tài đồ án đại học.
2. **Sửa sai lệch kỹ thuật về tính "độc lập" của Nmap NSE và Metasploit Scanner trong 1.3.4 và 1.3.5:**
   - Xóa bỏ nhận định "quét độc lập" và "tăng độ tin cậy của chỉ báo".
   - Thay bằng: "hai công cụ triển khai cùng một kỹ thuật thăm dò logic, giúp kiểm chứng chéo khâu phân tích cú pháp của phần mềm kiểm thử nhưng không tạo thêm bằng chứng mới độc lập".
   - *Lý do:* Khép kín `DR-C1-05`, bảo đảm tính trung thực khoa học khi bảo vệ trước hội đồng.
3. **Loại bỏ hướng dẫn vận hành khai thác trong 1.3.4 và 1.4.4:**
   - Không nhắc đến Meterpreter, Command Shell, SYSTEM token hay cú pháp payload.
   - Định nghĩa Mức 4 tập trung vào 3 trạng thái kết quả có thể xảy ra: Xác minh thành công, Không xác minh được, và Hệ thống mất ổn định (BSOD).
4. **Cắt giảm văn phong tuyệt đối hóa trong 1.2.5 và sáo ngữ lịch sử trong 1.2.6:**
   - Mô tả tác động CIA trung tính, thận trọng.
   - Rút gọn WannaCry và NotPetya thành mỗi chiến dịch một đoạn ngắn làm dẫn chứng thực tế cho sự cố lây lan qua SMBv1, không biến thành bài tường thuật lịch sử malware.

---

## 6. Những Nội Dung Chủ Động Giữ Lại và Lý Do

1. **Bảng 6 CVE trong 1.2.2:**
   - *Lý do giữ:* Bắt buộc để người đọc và hội đồng thấy rõ MS17-010 là một gói cập nhật xử lý nhiều lỗ hổng, giải thích cơ sở chọn CVE-2017-0144 làm trọng tâm mà không đánh đồng toàn bộ bulletin vào một lỗi duy nhất.
2. **Tên hai hàm `SrvOs2FeaListSizeToNt` và `SrvOs2FeaToNt` trong 1.2.3:**
   - *Lý do giữ:* Làm mốc kỹ thuật cụ thể phân biệt giữa bước tính toán kích thước vùng đệm và bước sao chép dữ liệu, giải thích rõ nguyên nhân trực tiếp phát sinh lỗi tràn bộ nhớ nhân mà không cần đi sâu vào mã máy.
3. **Mã trạng thái NT Status `0xC0000205` và `0xC0000022` trong 1.3.3 và 1.4.3:**
   - *Lý do giữ:* Đây là cơ sở cốt lõi để script NSE và Metasploit scanner phân nhánh kết luận; giúp sinh viên bảo vệ được câu hỏi "dựa vào đâu mà công cụ biết máy chủ chưa vá hay đã chặn truy cập?".
4. **Mô hình cấu trúc 3 phần tại mỗi mức ở 1.4 (Dấu hiệu quan sát – Ý nghĩa kỹ thuật – Ranh giới kết luận):**
   - *Lý do giữ:* Đây là đóng góp phương pháp luận quan trọng nhất của Chương 1, nối trực tiếp cơ sở lý thuyết với thiết kế thực nghiệm ở Chương 2 và phân tích ở Chương 3.

---

## 7. Các Điểm Còn Cần Tác Giả Lưu Ý / Xác Nhận Khi Bảo Vệ

1. **Về số liệu thực nghiệm:** Toàn bộ Chương 1 chỉ dừng ở mức cơ sở lý thuyết và tiêu chí phương pháp luận. Sinh viên không được tự nhận đã có số liệu đo đạc thực tế trong lab ở chương này (các kết quả lab thuộc Chương 2, 3 và hiện đang giữ nhãn `[CẦN DỮ LIỆU]` theo đúng quyết định DEC-03).
2. **Về việc lựa chọn CVE-2017-0144:** Sinh viên cần chuẩn bị câu trả lời bảo vệ: Đồ án tập trung vào CVE-2017-0144 vì đây là lỗ hổng thực thi mã từ xa không cần chứng thực tác động vào dịch vụ SMBv1, có bề mặt tấn công mở rộng nhất trên cổng 445 và có công cụ kiểm thử chuẩn hóa; các CVE khác như CVE-2017-0145 đòi hỏi chứng thực hoặc các gói tin đặc thù khác.

---

## 8. Các Câu Hỏi Bảo Vệ Quan Trọng Nhất Dự Kiến

1. **Hỏi:** *Tại sao cổng TCP 445 mở không đồng nghĩa với việc hệ thống có lỗ hổng MS17-010?*
   - **Gợi ý bảo vệ:** Cổng 445 chỉ là cổng tiếp nhận kết nối ở tầng giao vận của dịch vụ Direct-hosted SMB. Một máy chủ Windows hiện đại hoặc máy đã cài bản vá vẫn mở cổng 445 để chia sẻ tệp hợp lệ. Chỉ khi hệ thống đồng thời hỗ trợ SMBv1 và chưa cập nhật bản vá khắc phục lỗi trong `srv.sys` thì lỗ hổng mới tồn tại.
2. **Hỏi:** *Nếu Nmap NSE báo `State: VULNERABLE`, điều đó đã chứng minh kẻ tấn công chắc chắn chiếm được quyền điều khiển máy chủ chưa?*
   - **Gợi ý bảo vệ:** Chưa. Script NSE chỉ gửi gói tin thăm dò và quan sát phản hồi lỗi `0xC0000205` để suy đoán hệ thống đang chạy nhánh mã chưa vá. Để thực thi mã thành công trên thực tế còn phụ thuộc vào kiến trúc hệ điều hành, bố cục bộ nhớ nhân tại thời điểm đó và việc vượt qua các cơ chế bảo vệ mà không làm sập máy chủ.
3. **Hỏi:** *Khi kịch bản kiểm tra trả về mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`), ta có được kết luận máy chủ đã được vá an toàn hay không?*
   - **Gợi ý bảo vệ:** Không được kết luận máy chủ đã vá. Mã lỗi từ chối truy cập thường xuất hiện khi máy chủ áp dụng chính sách chặn kết nối nặc danh (Null Session) vào `IPC$`. Khi đó, gói tin thăm dò bị chặn trước khi chạm đến nhánh mã kiểm tra, dẫn đến tình huống âm tính giả dù hệ điều hành có thể chưa hề được cập nhật bản vá.
4. **Hỏi:** *Công cụ quét của Metasploit (`smb_ms17_010`) và kịch bản Nmap NSE có phải là hai bằng chứng độc lập không?*
   - **Gợi ý bảo vệ:** Không. Hai công cụ này sử dụng cùng một logic kỹ thuật thăm dò (gửi yêu cầu giao dịch qua `IPC$` và bắt mã lỗi trả về). Việc chạy cả hai công cụ chỉ giúp loại trừ lỗi phần mềm của trạm kiểm thử, không phải là hai nguồn bằng chứng độc lập về an ninh của máy chủ.
5. **Hỏi:** *Hiện tượng màn hình xanh (BSOD) khi chạy kiểm chứng có được coi là khai thác thành công không?*
   - **Gợi ý bảo vệ:** Không. BSOD chỉ chứng minh lỗi quản lý bộ nhớ nhân đã bị kích hoạt làm hỏng vùng nhớ và hệ điều hành buộc phải dừng để tự bảo vệ (ảnh hưởng tính sẵn sàng). Xác minh thực thi mã thành công đòi hỏi phải chuyển hướng luồng thực thi và xác lập được quyền tương tác có kiểm soát trên mục tiêu mà không làm sập hệ thống.
