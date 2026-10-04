# Đánh giá Defense Readiness: Chương 1 (Mục 1.2, 1.3, 1.4)

- **Dự án:** Đồ án chuyên ngành An toàn thông tin (`work/do-an`)
- **Tài liệu đánh giá:** [work/do-an/CHAPTER_1.md](file:///e:/word_ppt-auto/work/do-an/CHAPTER_1.md) (các mục 1.2, 1.3, 1.4)
- **Quy tắc áp dụng:** [work/do-an/DEFENSE_READINESS.md](file:///e:/word_ppt-auto/work/do-an/DEFENSE_READINESS.md) (DEC-24 và DEC-26, ngày 2026-10-04)
- **Thời điểm thực hiện:** 2026-10-04
- **Trạng thái:** `DEFENSE_REVIEW_IN_PROGRESS`
- **Nguyên tắc cốt lõi:** Fail-Closed — UNRESOLVED IS VALID.

---

## 1. Phạm vi Review

Đánh giá tính sẵn sàng bảo vệ (Defense Readiness), cơ sở bằng chứng (Evidence) và quyền làm chủ lập luận của tác giả (Ownership) đối với ba mục trọng tâm của Chương 1:
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

| Card ID | Tiêu đề | Claim Type | Evidence Key | Ownership Key | Text Action | Status |
|---|---|---|:---:|:---:|:---:|:---:|
| **DR-C1-01** | Trọng tâm CVE-2017-0144 | method/design decision | PASS | FAIL | NO_TEXT_CHANGE | `AUTHOR_CONFIRM` |
| **DR-C1-02** | Cơ sở của khung 4 mức | interpretation / method | PASS | PASS | NO_TEXT_CHANGE | `READY` |
| **DR-C1-03** | Ranh giới chứng minh từng mức | interpretation / conclusion | PASS | FAIL | NO_TEXT_CHANGE | `AUTHOR_CONFIRM` |
| **DR-C1-04** | Chuỗi công cụ kiểm thử | method/design decision | PASS | FAIL | NO_TEXT_CHANGE | `AUTHOR_CONFIRM` |
| **DR-C1-05** | Tính độc lập giữa NSE & MSF | interpretation / conclusion | PASS | NOT_APPLICABLE | NO_TEXT_CHANGE | `READY` |
| **DR-C1-06** | Đối chiếu Black-box vs White-box | interpretation / method | PASS | FAIL | NO_TEXT_CHANGE | `AUTHOR_CONFIRM` |
| **DR-C1-07** | Mức độ làm chủ cơ chế FEA | source fact / interpretation | PASS | FAIL | NO_TEXT_CHANGE | `AUTHOR_CONFIRM` |
| **DR-C1-08** | Mức 4 và giới hạn kết luận | conclusion / method | PASS | FAIL | NO_TEXT_CHANGE | `AUTHOR_CONFIRM` |

---

## 4. Chi Tiết Từng Defense Card Sau Khi Rà Soát (Chuẩn 15 Trường)

### DR-C1-01 — Trọng tâm CVE-2017-0144

| Field | Content |
|---|---|
| Section / Claim ID | §1.2.1–1.2.2; C002; RQ2/O2 |
| Claim type | method/design decision; author decision đối với lý do gán cho nhóm |
| Claim | Đồ án lấy CVE-2017-0144 làm trọng tâm nghiên cứu trong nhóm MS17-010. |
| Evidence / Data | RESEARCH_MAP (RQ2, O2); DEC-06; DEC-09; CLAIM_MATRIX (C002); S005, S011, S013. |
| Evidence boundary | Phạm vi đã được duyệt là quyết định đề cương; không dùng cơ chế một CVE đại diện cho toàn bộ các CVE trong bulletin. Chưa có dữ liệu thực nghiệm lab tại Chương 1. |
| Evidence key | PASS |
| Author ownership evidence | Chưa có văn bản/phản hồi trực tiếp của tác giả giải thích vì sao chọn CVE-2017-0144 thay vì các CVE khác (như CVE-2017-0145). Quyết định phạm vi LOCKED (DEC-06/DEC-09) chỉ chứng minh phạm vi đề tài, không phải bằng chứng tác giả làm chủ câu trả lời bảo vệ. |
| Ownership key | FAIL |
| Why needed | Xác định đối tượng phân tích trọng tâm để RQ2 không bị phân tán thành mọi lỗi SMB. |
| Author must explain | Phân biệt giữa bản tin, danh mục CVE và mã khai thác; giải thích căn cứ chọn CVE-2017-0144 làm trọng tâm kỹ thuật của đồ án. |
| Author response | [CHƯA CÓ PHẢN HỒI TÁC GIẢ] |
| Likely defense question | Vì sao chọn CVE-2017-0144 làm trọng tâm thay vì CVE-2017-0145 và phần nào của MS17-010 không thể suy ra từ việc phân tích CVE này? |
| Text action | NO_TEXT_CHANGE |
| Status | AUTHOR_CONFIRM |
| Review trace | Antigravity / 2026-10-04 / PROJECT_STATE.md (DEC-24, DEC-26) |

---

### DR-C1-02 — Vì sao dùng khung bốn mức

| Field | Content |
|---|---|
| Section / Claim ID | §1.4 (1.4.1–1.4.5); C003; RQ3/O3 |
| Claim type | interpretation; method/design decision |
| Claim | Đánh giá trạng thái SMB và MS17-010 phân định rạch ròi 4 mức độ: (1) Cổng tiếp cận, (2) Phiên bản SMBv1, (3) Dấu hiệu nghi ngờ qua thăm dò lỗi, (4) Xác minh tác động thực tế có kiểm soát; không dùng kết luận nhị phân có/không lỗ hổng. |
| Evidence / Data | CLAIM_MATRIX (C003); DEC-12, DEC-17, DEC-18; S017, S018, S022, S029, S030, S013. |
| Evidence boundary | Khung là phương pháp tổ chức dữ liệu do nhóm xây dựng cho đề tài, không phải tiêu chuẩn quốc tế độc lập. Nguồn cho từng phép đo không tự chứng minh tính độc lập giữa các mức. |
| Evidence key | PASS |
| Author ownership evidence | Tác giả đã trực tiếp xác nhận lý do lựa chọn khung 4 mức tại `AUTHOR_VOICE.md` (mục "Dấu ấn riêng của công trình", dòng 67–71; phê duyệt tại DEC-05 và DEC-22 — Phê duyệt ba lựa chọn giọng 1B, 2A, 3A, ngày 2026-10-04, vị trí: mục “Quyết định mới: phê duyệt giọng ngày 2026-10-04” trong PROJECT_STATE.md): "Phân định rạch ròi 4 cấp độ... Lý do thật: Tránh dương tính giả; ngăn chặn nguy cơ crash hệ thống (BSOD) do corrupt kernel pool khi chạy module khai thác; và đảm bảo không phá vỡ tính tương thích của hệ thống mạng." |
| Ownership key | PASS |
| Why needed | Nối dữ liệu công cụ với tiêu chí và kịch bản ở các chương sau; ngăn ngừa chẩn đoán sai và rủi ro sập hệ thống lab. |
| Author must explain | Nêu câu hỏi riêng của từng mức, lý do không gộp thành một nhãn nhị phân và cách xử lý khi chưa đủ dữ liệu quan sát. |
| Author response | "Tránh dương tính giả; ngăn chặn nguy cơ crash hệ thống (BSOD) do corrupt kernel pool khi chạy module khai thác; và đảm bảo không phá vỡ tính tương thích của hệ thống mạng." (trích nguyên văn xác nhận từ `AUTHOR_VOICE.md` dòng 67–71). |
| Likely defense question | Bốn mức giải quyết vấn đề kỹ thuật gì mà một nhãn 'vulnerable' thông thường không thể giải quyết? |
| Text action | NO_TEXT_CHANGE |
| Status | READY |
| Review trace | Antigravity / 2026-10-04 / AUTHOR_VOICE.md dòng 67–71 (DEC-05 / DEC-22 — Phê duyệt ba lựa chọn giọng 1B, 2A, 3A, ngày 2026-10-04, mục "Quyết định mới: phê duyệt giọng ngày 2026-10-04" trong PROJECT_STATE.md) |

---

### DR-C1-03 — Mỗi mức chứng minh và không chứng minh gì

| Field | Content |
|---|---|
| Section / Claim ID | §1.3.2–1.3.3, §1.4.1–1.4.4; C003 |
| Claim type | interpretation; conclusion |
| Claim | Mỗi mức có điều quan sát được, điều suy luận có điều kiện và ranh giới kết luận: SYN-ACK chỉ chứng minh tầng giao vận; dialect SMBv1 không quan sát trực tiếp driver trong nhân; mã lỗi 0xC0000205 chỉ là chỉ báo phân nhánh lỗi; BSOD là mất ổn định chứ không phải thực thi mã thành công. |
| Evidence / Data | S017, S029, S018, S030, S013; CLAIM_MATRIX (C003). |
| Evidence boundary | Cấm suy diễn từ phản hồi giao vận sang tầng ứng dụng, từ dialect sang trạng thái nội tại, từ crash sang khai thác thành công. Chưa có dữ liệu đo lab tại Chương 1. |
| Evidence key | PASS |
| Author ownership evidence | Chưa có văn bản ghi nhận tác giả tự trình bày ranh giới suy luận cho từng mức trước hội đồng. Quyết định chuẩn hóa 3 khối chỉ là giải pháp kỹ thuật của bản thảo. |
| Ownership key | FAIL |
| Why needed | Ngăn kết luận port open = SMBv1 = vulnerable = exploitable; cốt lõi phương pháp luận của đồ án. |
| Author must explain | Với từng mức, chỉ ra điều quan sát trực tiếp, điều suy ra có điều kiện và điều hoàn toàn chưa biết. Phân biệt không xác minh được với đã chứng minh an toàn. |
| Author response | [CHƯA CÓ PHẢN HỒI TÁC GIẢ] |
| Likely defense question | Nếu cổng 445 mở nhưng yêu cầu SMB không phản hồi, hoặc khai thác gây BSOD, nhóm được kết luận gì về mặt khoa học? |
| Text action | NO_TEXT_CHANGE |
| Status | AUTHOR_CONFIRM |
| Review trace | Antigravity / 2026-10-04 / DEFENSE_READINESS.md pilot review |

---

### DR-C1-04 — Chuỗi Nmap $\to$ NSE $\to$ Metasploit

| Field | Content |
|---|---|
| Section / Claim ID | §1.3.2–1.3.5; C003/C004; RQ3/O3 |
| Claim type | method/design decision |
| Claim | Công cụ được bố trí theo tiến trình tuần tự: Nmap quét cổng $\to$ NSE nhận diện dialect và chỉ báo $\to$ Metasploit xác minh sâu khi có điều kiện kiểm soát. |
| Evidence / Data | RESEARCH_MAP (M3, O3); DEC-13; CLAIM_MATRIX (C003, C004); S017, S018, S029, S030, S013. |
| Evidence boundary | Tên công cụ không tự chứng minh độ sâu hoặc hiệu quả; thứ tự thiết kế không chứng minh mọi bước đã được chạy trên thực tế lab. |
| Evidence key | PASS |
| Author ownership evidence | Chưa có bản giải thích chính thức của tác giả về lý do vận hành cụ thể cho chuỗi thứ tự này (ngoài định hướng an toàn chung). |
| Ownership key | FAIL |
| Why needed | Gắn lựa chọn công cụ với tiến trình trinh sát an ninh, giảm thiểu rủi ro tác động tiêu cực đến mục tiêu khi chưa rõ thông tin. |
| Author must explain | Trình bày đầu vào, đầu ra của từng bước và lý do vì sao không chạy Metasploit exploit ngay từ đầu. |
| Author response | [CHƯA CÓ PHẢN HỒI TÁC GIẢ] |
| Likely defense question | Vì sao module auxiliary scanner không thay thế được bước xác minh tác động và vì sao quy trình không bắt đầu ngay bằng module khai thác? |
| Text action | NO_TEXT_CHANGE |
| Status | AUTHOR_CONFIRM |
| Review trace | Antigravity / 2026-10-04 / DEFENSE_READINESS.md pilot review |

---

### DR-C1-05 — Đối chiếu công cụ có độc lập không

| Field | Content |
|---|---|
| Section / Claim ID | §1.3.4–1.3.5; C003 |
| Claim type | interpretation; conclusion (source fact đối chiếu mã nguồn) |
| Claim | Nmap NSE (`smb-vuln-ms17-010.nse`) và Metasploit scanner (`smb_ms17_010`) là hai bản cài đặt khác nhau của cùng một logic kỹ thuật thăm dò (dùng chung tín hiệu IPC$/FID 0 và bắt mã lỗi 0xC0000205); chúng KHÔNG phải là hai nguồn bằng chứng độc lập về trạng thái an ninh của máy chủ. |
| Evidence / Data | S018 (mã nguồn NSE), S030 (mã nguồn Metasploit scanner `smb_ms17_010.rb`), SOURCE_LEDGER đối chiếu cơ chế IPC$/FID 0. |
| Evidence boundary | Việc đối chiếu chéo chỉ giúp kiểm chứng tính nhất quán về xử lý cú pháp của công cụ kiểm thử, không loại trừ được nguyên nhân sai số logic chung từ phía máy chủ hoặc chính sách mạng. |
| Evidence key | PASS |
| Author ownership evidence | Claim phát biểu chính xác sự thật kỹ thuật đối chiếu mã nguồn (hai công cụ không độc lập). Không gán quyết định hay giả định chủ quan cho tác giả. |
| Ownership key | NOT_APPLICABLE |
| Why needed | Ngăn chặn ngụy biện "hai công cụ cùng báo là bằng chứng độc lập khẳng định chắc chắn 100%". |
| Author must explain | Phân biệt giữa đối chiếu cách cài đặt phần mềm và độc lập về nguồn tín hiệu/giả định kỹ thuật; chỉ ra khả năng cả hai công cụ cùng nhận định sai nếu máy chủ có phản hồi bất thường. |
| Author response | [CHƯA CÓ PHẢN HỒI TÁC GIẢ] |
| Likely defense question | Khi cả hai công cụ Nmap NSE và Metasploit scanner cùng báo vulnerable, điều đó có loại trừ được khả năng âm tính giả hoặc dương tính giả do cấu hình máy chủ hay không? |
| Text action | NO_TEXT_CHANGE |
| Status | READY |
| Review trace | Antigravity / 2026-10-04 / SOURCE_LEDGER S018, S030 đối chiếu mã nguồn |

---

### DR-C1-06 — Đối chiếu hộp đen và trạng thái nội tại

| Field | Content |
|---|---|
| Section / Claim ID | §1.4.5; C003/C004 |
| Claim type | interpretation; method/design decision |
| Claim | Quan sát từ xa qua mạng (Black-box) cần được đối chiếu với thông tin cấu hình nội tại (White-box: bản vá KB, cấu hình Registry SMBv1) để giới hạn kết luận về máy chủ. |
| Evidence / Data | CHAPTER_ARGUMENT mục 2 & 3; DEC-17, DEC-18; CLAIM_MATRIX (C003, C004); S005, S008, S024. |
| Evidence boundary | Đây là nguyên tắc phương pháp luận định hướng cho việc thiết kế lab ở Chương 2, không phải kết quả thực nghiệm đã thu thập ở Chương 1. |
| Evidence key | PASS |
| Author ownership evidence | Quyết định thiết kế đã khóa tại DEC-18 (phân định Attacker Vantage Point vs. Server Internal State). Tuy nhiên, chưa có phản hồi của tác giả giải thích cụ thể cách đối chiếu khi có mâu thuẫn giữa hai góc nhìn khi bảo vệ. |
| Ownership key | FAIL |
| Why needed | Nối giới hạn quan sát mạng với phương pháp đối chứng nội tại ở Chương 2. |
| Author must explain | Vì sao cùng một phản hồi mạng có thể phản ánh các trạng thái nội tại khác nhau; dữ liệu nào phân biệt giữa chặn kết nối mạng với cập nhật vá lỗi. |
| Author response | [CHƯA CÓ PHẢN HỒI TÁC GIẢ] |
| Likely defense question | Khi NSE không phát hiện dấu hiệu lỗ hổng, nhóm kiểm tra bản vá và cấu hình như thế nào trước khi kết luận hệ thống an toàn? |
| Text action | NO_TEXT_CHANGE |
| Status | AUTHOR_CONFIRM |
| Review trace | Antigravity / 2026-10-04 / DEFENSE_READINESS.md pilot review |

---

### DR-C1-07 — Mức FEA cần làm chủ

| Field | Content |
|---|---|
| Section / Claim ID | §1.2.3; C002; RQ2/O2 |
| Claim type | source fact; interpretation |
| Claim | Nguyên nhân kỹ thuật của CVE-2017-0144 là sự sai lệch kích thước trong quá trình chuyển đổi cấu trúc FEA sang định dạng NT trong SMBv1, dẫn đến cấp phát bộ nhớ đệm nhân không đủ và gây Kernel Pool Overflow; trình bày ở mức nguyên lý nhân quả mà không phụ thuộc vào tên hàm cụ thể hoặc chi tiết reverse engineering mã khai thác. |
| Evidence / Data | S013 (Rapid7 Exploit Analysis), S005 (Microsoft MS17-010); CLAIM_MATRIX (C002); DEC-09, DEC-12, DEC-13. |
| Evidence boundary | Đồ án giải thích nguyên lý nhân quả (kích thước cấp phát vs. ghi thực tế), không tự nhận đã dịch ngược mã máy của driver `srv.sys`. |
| Evidence key | PASS |
| Author ownership evidence | Chưa có văn bản tác giả tự xác nhận mức độ làm chủ và cách giải thích chuỗi nhân quả FEA này trước câu hỏi hội đồng. |
| Ownership key | FAIL |
| Why needed | Trả lời RQ2 về cơ chế phát sinh lỗi bộ nhớ ở mức nguyên lý, tránh bị chất vấn sâu vào chi tiết khai thác ngoài tầm đề tài đại học. |
| Author must explain | Giải thích chuỗi nhân quả: dữ liệu FEA $\to$ tính/chuyển đổi kích thước $\to$ vùng nhớ cấp phát không phù hợp $\to$ ghi vượt giới hạn bộ đệm $\to$ Kernel Pool Overflow $\to$ nguy cơ mất ổn định hoặc tạo điều kiện cho thực thi mã. |
| Author response | [CHƯA CÓ PHẢN HỒI TÁC GIẢ] |
| Likely defense question | Nhóm có thể giải thích chuỗi nhân quả từ cấu trúc FEA đến lỗi tràn bộ nhớ nhân mà không cần phụ thuộc vào mã khai thác chi tiết không? |
| Text action | NO_TEXT_CHANGE |
| Status | AUTHOR_CONFIRM |
| Review trace | Antigravity / 2026-10-04 / DEFENSE_READINESS.md pilot review |

---

### DR-C1-08 — Cấp 4 và giới hạn kết luận xuyên chương

| Field | Content |
|---|---|
| Section / Claim ID | §1.4.4–1.4.5; C003/C004 |
| Claim type | conclusion; method/design decision |
| Claim | Xác minh Mức 4 thiết lập phiên tương tác chỉ chứng minh thực thi mã từ xa ở tầng hệ thống; không được đồng nhất với quan sát trực tiếp vùng nhớ nhân. Hiện tượng BSOD chỉ chứng minh hệ thống mất ổn định (ảnh hưởng tính sẵn sàng), không phải khai thác thành công. |
| Evidence / Data | DEC-17, DEC-18; CHAPTER_ARGUMENT mục 4; S013, S024. |
| Evidence boundary | Crash không phải là RCE thành công. Chương 1 không có log thực nghiệm lab. Phân định rõ giữa quan sát gián tiếp qua mạng và quan sát trực tiếp kernel. |
| Evidence key | PASS |
| Author ownership evidence | Chưa có xác nhận chính thức của tác giả về cách trả lời hội đồng khi bị chất vấn về việc tại sao BSOD không được tính là thành công. |
| Ownership key | FAIL |
| Why needed | Bảo đảm tính liêm chính học thuật, ngăn chặn kết luận vượt bằng chứng trong Chương 2 và Chương 3. |
| Author must explain | Phân biệt rõ giữa mục tiêu thực thi mã (RCE) và hiện tượng từ chối dịch vụ (DoS/BSOD); giải thích vì sao shell tương tác không đồng nghĩa với quan sát trực tiếp bộ nhớ nhân. |
| Author response | [CHƯA CÓ PHẢN HỒI TÁC GIẢ] |
| Likely defense question | Phiên chạy với quyền SYSTEM có tự chứng minh nhóm quan sát được mã thực thi trong kernel không? |
| Text action | NO_TEXT_CHANGE |
| Status | AUTHOR_CONFIRM |
| Review trace | Antigravity / 2026-10-04 / DEFENSE_READINESS.md pilot review |

---

## 5. Những Nội Dung Đã SIMPLIFY và Lược Bỏ

1. **Lược bỏ chi tiết Reverse Engineering mã khai thác và tên hàm nội bộ trong 1.2.3:**
   - Xóa bỏ việc giải thích phép tràn số 16-bit dạng `0x10040 -> 0x0040`.
   - Xóa bỏ con số cụ thể "64 byte" hay cơ chế sắp xếp vùng nhớ `srvnet.sys` chi tiết.
   - Xóa bỏ mô tả ghi đè con trỏ hàm (`function pointer`) và điều hướng CPU.
   - Lược bỏ tên các hàm xử lý nội bộ (`SrvOs2FeaListSizeToNt`, `SrvOs2FeaToNt`) theo yêu cầu SIMPLIFY của DR-C1-07, rút về nguyên lý chuỗi nhân quả chuyển đổi FEA để giảm bề mặt chất vấn không cần thiết.
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
2. **Nguyên lý chuỗi nhân quả FEA trong 1.2.3:**
   - *Lý do giữ:* Giữ trọn vẹn chuỗi nhân quả kỹ thuật (dữ liệu FEA $\to$ tính/chuyển đổi kích thước $\to$ cấp phát bộ đệm không tương ứng $\to$ ghi vượt biên $\to$ Kernel Pool Overflow) để giải thích cơ sở phát sinh lỗi bộ nhớ phục vụ RQ2/O2 mà không đưa vào tên hàm nội bộ hay mã khai thác chi tiết.
3. **Mã trạng thái NT Status `0xC0000205` và `0xC0000022` trong 1.3.3 và 1.4.3:**
   - *Lý do giữ:* Đây là cơ sở cốt lõi để script NSE và Metasploit scanner phân nhánh kết luận; giúp sinh viên bảo vệ được câu hỏi "dựa vào đâu mà công cụ biết máy chủ chưa vá hay đã chặn truy cập?".
4. **Mô hình cấu trúc 3 phần tại mỗi mức ở 1.4 (Dấu hiệu quan sát – Ý nghĩa kỹ thuật – Ranh giới kết luận):**
   - *Lý do giữ:* Đây là đóng góp phương pháp luận quan trọng nhất của Chương 1, nối trực tiếp cơ sở lý thuyết với thiết kế thực nghiệm ở Chương 2 và phân tích ở Chương 3.

---

## 7. Các Điểm Cần Tác Giả Lưu Ý và Chuẩn Bị Khi Bảo Vệ

1. **Về số liệu thực nghiệm:** Toàn bộ Chương 1 chỉ dừng ở mức cơ sở lý thuyết và tiêu chí phương pháp luận. Tác giả không tự nhận đã có số liệu đo đạc thực tế trong lab ở chương này (các kết quả lab thuộc Chương 2, 3 và hiện đang giữ nhãn `[CẦN DỮ LIỆU]` theo đúng quyết định DEC-03).
2. **Về việc lựa chọn CVE-2017-0144:** Lý do trực tiếp của tác giả cho việc chọn CVE-2017-0144 thay vì các CVE khác chưa được xác nhận. Giữ DR-C1-01 = AUTHOR_CONFIRM.

---

## 8. Các Câu Hỏi Bảo Vệ Quan Trọng Nhất Dự Kiến

1. **Hỏi:** *Tại sao cổng TCP 445 mở không đồng nghĩa với việc hệ thống có lỗ hổng MS17-010?*
   - **Tác giả cần làm chủ (Author must explain):**
     - Khả năng tiếp cận ở tầng giao vận (Transport reachability);
     - Phiên bản giao thức SMB được hỗ trợ (SMB dialect);
     - Trạng thái bản vá và lỗ hổng nội tại của hệ thống (Patch / vulnerability state);
     - Ranh giới giữa khả năng tiếp cận và khả năng khai thác (Exploitability boundary).
   - **Phản hồi của tác giả:** [CHƯA CÓ PHẢN HỒI TÁC GIẢ]
2. **Hỏi:** *Nếu Nmap NSE báo `State: VULNERABLE`, điều đó đã chứng minh kẻ tấn công chắc chắn chiếm được quyền điều khiển máy chủ chưa?*
   - **Tác giả cần làm chủ (Author must explain):**
     - Kịch bản kiểm tra sử dụng mã phản hồi làm chỉ báo nghi ngờ (Script uses response code as indicator);
     - Chỉ báo qua mạng không đồng nghĩa với quan sát trực tiếp bộ nhớ nhân (Indicator != direct kernel observation);
     - Chỉ báo lỗ hổng không đồng nghĩa với việc khai thác thành công (Indicator != exploit success).
   - **Phản hồi của tác giả:** [CHƯA CÓ PHẢN HỒI TÁC GIẢ]
3. **Hỏi:** *Khi kịch bản kiểm tra trả về mã lỗi `STATUS_ACCESS_DENIED` (`0xC0000022`), ta có được kết luận máy chủ đã được vá an toàn hay không?*
   - **Tác giả cần làm chủ (Author must explain):**
     - Kết quả phản hồi có thể phụ thuộc vào chính sách hoặc cấu hình kiểm soát truy cập (Result may depend on access policy/configuration);
     - Phản hồi từ chối truy cập không phải là bằng chứng máy chủ đã được vá an toàn (Denial != proof of patch/safety).
   - **Phản hồi của tác giả:** [CHƯA CÓ PHẢN HỒI TÁC GIẢ]
4. **Hỏi:** *Công cụ quét của Metasploit (`smb_ms17_010`) và kịch bản Nmap NSE có phải là hai bằng chứng độc lập không?*
   - **Tác giả cần làm chủ (Author must explain):**
     - Hai bản cài đặt phần mềm khác nhau (Two implementations);
     - Cùng chia sẻ một tín hiệu logic và giả định kỹ thuật thăm dò (Shared signal / assumption);
     - Việc đối chiếu chéo công cụ không tạo ra bằng chứng an ninh độc lập mới (Comparison != independent evidence).
   - **Phản hồi của tác giả:** [CHƯA CÓ PHẢN HỒI TÁC GIẢ]
5. **Hỏi:** *Hiện tượng màn hình xanh (BSOD) khi chạy kiểm chứng có được coi là khai thác thành công không?*
   - **Tác giả cần làm chủ (Author must explain):**
     - Hiện tượng phản ánh sự mất ổn định và tác động đến tính sẵn sàng của hệ thống (Instability / availability impact);
     - Lỗi dừng / crash không phải là bằng chứng thực thi mã thành công (Crash != proof of RCE);
     - Lỗi dừng / crash không đủ cơ sở để tự kết luận nguyên nhân gốc rễ cụ thể (Crash != proof of exact root cause);
     - Xác minh thực thi mã thành công đòi hỏi bằng chứng trực tiếp về thực thi mã có kiểm soát theo thiết kế thực nghiệm.
   - **Phản hồi của tác giả:** [CHƯA CÓ PHẢN HỒI TÁC GIẢ]
