# Defense Readiness

- Phạm vi: lớp review **project-local**, chỉ áp dụng cho `work/do-an`.
- Quyết định: DEC-24 (tích hợp ban đầu) và DEC-26 (hardening fail-closed), người dùng yêu cầu trực tiếp ngày 2026-10-04.
- Trạng thái artifact: `RULE / TEMPLATE / HARD TEST SPECIFICATION`. Không lưu trạng thái hoạt động hiện hành (Active State) của các thẻ; Active State của DR-C1-01 ... DR-C1-08 được lưu độc quyền tại `work/do-an/CHAPTER_1_DEFENSE_REVIEW.md` (Single Source of Truth).
- Nguyên tắc cốt lõi: **FAIL-CLOSED — UNRESOLVED IS VALID**.

---

## 1. Mục đích và Nguyên tắc Fail-Closed

Defense Readiness kiểm tra người đứng tên đồ án cần hiểu và bảo vệ được phần nào của các luận điểm, diễn giải và quyết định quan trọng. Một phát biểu đúng, có nguồn và được viết rõ vẫn cần được xét về vai trò trong nghiên cứu, giới hạn bằng chứng và phần tác giả phải giải thích khi bảo vệ.

Đây không phải AI detector, không tạo lỗi hoặc làm văn bản “giống người”. Lớp này không thay evidence review, không thay author voice, không tạo dữ liệu, trải nghiệm, quyết định hoặc lý do của tác giả. Author voice xét cách tác giả diễn đạt; Defense Readiness xét nội dung tác giả cần làm chủ. Hai trách nhiệm được giữ riêng.

### Nguyên tắc Fail-Closed: UNRESOLVED IS VALID

- **Unresolved is valid:** Một đợt review được coi là hoàn thành tốt và trung thực khoa học ngay cả khi còn các thẻ ở trạng thái:
  - `AUTHOR_CONFIRM`
  - `EVIDENCE_GAP`
  - `SIMPLIFY`
  - `REMOVE_CANDIDATE`
- **Số lượng READY không phải là KPI:** Agent TUYỆT ĐỐI KHÔNG được coi số lượng thẻ `READY` cao là thước đo thành công hay KPI của lượt làm việc.
- **Cấm tối ưu đóng thẻ:** Nghiêm cấm viết, lập luận hoặc hành động theo các mục tiêu:
  - “đóng tất cả card”
  - “0 AUTHOR_CONFIRM”
  - “0 EVIDENCE_GAP”
  - “khép toàn bộ gap”
- **Ý nghĩa của trạng thái mở:** Trạng thái còn mở chỉ là thất bại nếu agent che giấu hoặc làm sai lệch nó; việc tồn tại trạng thái mở phản ánh đúng thực tế nghiên cứu và là cơ sở để tác giả làm việc tiếp.

Thứ tự ưu tiên giữ nguyên: yêu cầu hiện tại → quy định/mẫu chính thức → quyết định đã khóa → nguồn/dữ liệu đã xác minh → quy trình nghiên cứu và lập luận → giọng tác giả → linter. Defense Readiness nằm **bên trong quy trình nghiên cứu và lập luận**; không đứng cao hơn HUIT, quyết định LOCKED, nguồn, dữ liệu hoặc claim boundary. Không tạo G7, G4.5 hoặc đổi cấu trúc G0–G6.

---

## 2. Phân biệt Ba Loại Bằng Chứng

Tuyệt đối không được trộn lẫn ba loại bằng chứng sau:

1. **SOURCE EVIDENCE (Bằng chứng nguồn):**
   - Chứng minh fact kỹ thuật, cơ chế giao thức, quy chuẩn hoặc quan sát thực nghiệm từ nguồn tài liệu chuẩn hoặc mã nguồn đã xác minh.
2. **PROJECT DECISION (Quyết định dự án):**
   - Chứng minh dự án đã lựa chọn phạm vi, giả định hoặc phương pháp luận (ghi nhận trong `PROJECT_STATE.md`, `RESEARCH_MAP.md`, `OUTLINE.md`, các quyết định `DEC`).
   - Quyết định này chỉ chứng minh **phạm vi đã được duyệt**, KHÔNG tự chứng minh tác giả đã hiểu hoặc giải thích được lý do kỹ thuật.
3. **AUTHOR OWNERSHIP EVIDENCE (Bằng chứng làm chủ của tác giả):**
   - Chứng minh tác giả đã trực tiếp xác nhận lý do, hiểu rõ cơ chế hoặc tự đưa ra giải thích bảo vệ (ghi nhận trong `AUTHOR_VOICE.md`, chat-derived recorded decisions, hoặc phản hồi thật từ người dùng).

Một artifact có thể hỗ trợ nhiều loại bằng chứng, nhưng reviewer phải chỉ rõ artifact hỗ trợ loại nào. **Tuyệt đối không suy diễn:** “DEC-X đã khóa phương pháp $\to$ tác giả làm chủ lý do $\to$ READY” nếu không có Author Ownership Evidence cụ thể.

---

## 3. Quy tắc Two-Key cho READY

Mỗi Defense Card bắt buộc phải trải qua hai bước kiểm tra độc lập trước khi xác định trạng thái:

### A. EVIDENCE KEY (`PASS` / `FAIL`)
`EVIDENCE KEY = PASS` chỉ khi thỏa mãn toàn bộ các điều kiện:
- Nguồn tài liệu hoặc dữ liệu hỗ trợ đúng claim hiện tại;
- Claim không phát biểu mạnh hơn mức nguồn/dữ liệu hỗ trợ;
- Không dựa duy nhất vào artifact stale, reopened hoặc conflicting;
- Không biến phương pháp dự kiến (planned method) thành kết quả quan sát (observed result);
- Ranh giới bằng chứng (evidence boundary) được ghi rõ ràng, chỉ rõ những gì chưa biết.

### B. OWNERSHIP KEY (`PASS` / `FAIL` / `NOT_APPLICABLE`)
Áp dụng bắt buộc cho:
- Author decision (quyết định của tác giả);
- Method/design decision (quyết định phương pháp hoặc thiết kế);
- Rationale được gán cho nhóm nghiên cứu;
- Critical interpretation trọng yếu mà tác giả cần bảo vệ trước hội đồng.

`OWNERSHIP KEY = PASS` chỉ khi:
- Có phản hồi hoặc xác nhận thật của tác giả đã tồn tại trong lịch sử dự án (`AUTHOR_VOICE.md`, các quyết định chat-derived đã ghi nhận) hoặc được người dùng trực tiếp cung cấp trong phiên;
- Bắt buộc truy vết được: artifact hoặc quyết định cụ thể, nội dung xác nhận, ngày và ID/tên quyết định nếu có.
- **Lưu ý quyết định đã khóa:** Quyết định `LOCKED` KHÔNG tự động làm `OWNERSHIP KEY = PASS`. Ví dụ: RQ2 đã khóa chọn CVE-2017-0144 chỉ chứng minh phạm vi đã chọn, không chứng minh tác giả đã trả lời được câu hỏi “vì sao chọn CVE-2017-0144 thay vì CVE-2017-0145?”.

`OWNERSHIP KEY = NOT_APPLICABLE` chỉ áp dụng cho:
- Fact kỹ thuật thuần túy từ tài liệu/mã nguồn khách quan (source fact) không chứa đựng lựa chọn phương pháp hoặc diễn giải chủ quan của tác giả.

---

## 4. Bảng Suy Diễn Trạng Thái Bắt Buộc (Derivation Rule)

Trước khi gán Status cho mỗi thẻ, reviewer bắt buộc phải ghi rõ kết quả đánh giá của hai khóa:
- `Evidence key:` PASS / FAIL
- `Ownership key:` PASS / FAIL / NOT_APPLICABLE

Sau đó, suy ra trạng thái bắt buộc theo bảng sau:

| Evidence Key | Ownership Key | Điều kiện bổ sung | Status bắt buộc |
|:---:|:---:|---|:---:|
| **FAIL** | Bất kỳ | - | `EVIDENCE_GAP` |
| **PASS** | **FAIL** | - | `AUTHOR_CONFIRM` |
| **PASS** | **PASS** hoặc **NOT_APPLICABLE** | Mức chi tiết vượt nhu cầu của RQ/phương pháp | `SIMPLIFY` |
| Bất kỳ | Bất kỳ | Nội dung không phục vụ RQ/O/method/institution | `REMOVE_CANDIDATE` |
| **PASS** | **PASS** hoặc **NOT_APPLICABLE** | Không có vấn đề simplify hoặc remove; vượt qua counter-review | **`READY`** |

**Agent TUYỆT ĐỐI KHÔNG được ghi đè (override) bảng suy diễn này.** Mọi trạng thái `READY` không thỏa mãn đồng thời cả hai điều kiện trên đều bị coi là không hợp lệ.

---

## 5. Tuyệt Đối Không Tự Viết Câu Trả Lời Thay Tác Giả

Defense Readiness phục vụ công tác rà soát và chuẩn bị cho tác giả, không làm thay tác giả:

- **ĐƯỢC PHÉP TẠO:**
  - `Likely defense question`: Dự báo các câu hỏi chất vấn tiềm tàng từ hội đồng.
  - `Author must explain`: Xác định cụ thể phạm vi kiến thức và lập luận mà tác giả cần nắm vững và giải thích.
- **CẤM TỰ TẠO:**
  - “Gợi ý bảo vệ”
  - “Câu trả lời mẫu”
  - “Sinh viên nên trả lời rằng...”
  - Các đoạn trả lời hoàn chỉnh có thể bị sao chép hoặc coi như lời của tác giả.
- **Quy định về Author response:**
  - Khi chưa có phản hồi thực sự từ tác giả, trường `Author response` BẮT BUỘC ghi chính xác:
    `[CHƯA CÓ PHẢN HỒI TÁC GIẢ]`
  - Tuyệt đối không tự điền bất kỳ nội dung nào thay thế.
  - Chỉ sau khi người dùng trực tiếp cung cấp câu trả lời trong một lượt tương tác khác, agent mới được ghi lại trung thực nội dung đó và tiến hành review lại thẻ.

---

## 6. Quy Tắc Đối Với Artifact LOCKED / STALE / REOPENED

Nếu một artifact mang nhãn `LOCKED` nhưng trong `PROJECT_STATE.md` hoặc các báo cáo audit mới hơn có ghi nhận:
- `stale`;
- `reopened`;
- `conflict` (hoặc `CONFLICT_LOCKED`);
- `historical only`;
- `superseded in practice`;
- `needs reconciliation`;

Thì artifact đó **KHÔNG ĐƯỢC PHÉP DÙNG ĐƠN ĐỘC** để:
- Đánh giá `PASS` cho Evidence Key;
- Đánh giá `PASS` cho Ownership Key;
- Chuyển bất kỳ thẻ nào sang trạng thái `READY`.

**Yêu cầu xử lý:**
- Phải đối chiếu với quyết định hoặc audit mới hơn;
- Ghi rõ mâu thuẫn trong `Evidence boundary`;
- Giữ nguyên trạng thái mở (`EVIDENCE_GAP` hoặc `AUTHOR_CONFIRM`) cho đến khi xung đột được giải quyết chính thức.
- Thứ tự ưu tiên (precedence) hiện hành của repository luôn được tôn trọng tuyệt đối.

---

## 7. Schema Trạng Thái Là Closed Enum và Trường Text Action

### A. Closed Enum cho Status
Chỉ được phép sử dụng chính xác 5 giá trị trạng thái sau:
1. `READY`
2. `SIMPLIFY`
3. `AUTHOR_CONFIRM`
4. `EVIDENCE_GAP`
5. `REMOVE_CANDIDATE`

**NGHIÊM CẤM tạo hoặc sử dụng các trạng thái ngoài schema**, ví dụ:
- `CLOSED`
- `FIXED`
- `RESOLVED`
- `GAP CLOSED`
- `KHÉP GAP`
- `ĐÃ SỬA NỘI DUNG`
- `ACCEPTED`
- `READY (đã truy vết)`

Nếu nội dung văn bản đã được biên tập lại, reviewer phải đánh giá lại cả Evidence Key và Ownership Key cho claim mới, rồi suy ra một trong 5 trạng thái hợp lệ theo đúng bảng Derivation Rule.

### B. Trường riêng biệt: Text Action
Để tách bạch giữa trạng thái nhận thức/bằng chứng (Status) và hành động biên tập văn bản, mỗi thẻ có trường `Text action` độc lập.

Giá trị cho phép của `Text action`:
- `KEEP`: Giữ nguyên văn bản hiện tại.
- `REWRITE`: Cần viết lại câu/đoạn để làm rõ ranh giới hoặc thu hẹp phát biểu.
- `SIMPLIFY`: Cần lược bỏ chi tiết phụ hoặc giảm bớt độ sâu kỹ thuật không cần thiết.
- `REMOVE_PROPOSED`: Đề xuất gỡ bỏ nội dung khỏi chương.
- `NO_TEXT_CHANGE`: Không cần thay đổi văn bản.

*Ví dụ:* `Status = AUTHOR_CONFIRM` kết hợp `Text action = SIMPLIFY` là hoàn toàn hợp lệ. Việc sửa đổi câu chữ không đồng nghĩa với việc vấn đề ownership hay evidence đã được giải quyết.

---

## 8. Phạm Vi Tạo Thẻ (Scope of Defense Cards)

Không biến Defense Readiness thành gánh nặng thủ tục bằng cách tạo thẻ cho từng câu văn hoặc định nghĩa cơ bản.

**Chỉ tạo Defense Card cho:**
- Luận điểm trung tâm (central claim);
- Diễn giải kỹ thuật trọng yếu làm thay đổi mức độ chắc chắn của kết luận (critical interpretation);
- Quyết định phương pháp hoặc thiết kế thực nghiệm (method/design decision);
- Lý do lựa chọn gán cho tác giả/nhóm nghiên cứu (author rationale);
- Kết luận chính của từng mục hoặc chương (major conclusion);
- Luận điểm chuyển tiếp hoặc suy luận xuyên chương (cross-chapter inference);
- Chi tiết kỹ thuật sâu có nguy cơ bị chất vấn “vì sao đồ án cần chi tiết này?”.

**Nguyên tắc vận hành:**
**LOW CARD DENSITY — HIGH REVIEW VALUE** (Mật độ thẻ thấp, giá trị phản biện cao).

---

## 9. Template Chuẩn Hóa Của Defense Card

Mỗi Defense Card bắt buộc phải có đầy đủ 15 trường sau đây:

| Field | Content |
|---|---|
| Section / Claim ID | Vị trí mục trong chương; Claim ID liên kết (C001–C006); RQ/O liên quan |
| Claim type | `source fact` / `interpretation` / `author decision` / `method/design decision` / `conclusion` |
| Claim | Phát biểu cụ thể cần rà soát |
| Evidence / Data | Căn cứ nguồn/dữ liệu/DEC hỗ trợ |
| Evidence boundary | Ranh giới bằng chứng: điều chưa biết, điều không được suy diễn |
| Evidence key | `PASS` / `FAIL` |
| Author ownership evidence | Căn cứ xác nhận thực tế từ tác giả (hoặc ghi rõ chưa có) |
| Ownership key | `PASS` / `FAIL` / `NOT_APPLICABLE` |
| Why needed | Vai trò đối với RQ, mục tiêu hoặc phương pháp của đề tài |
| Author must explain | Yêu cầu tác giả phải giải thích được trước hội đồng |
| Author response | Trích dẫn phản hồi thực của tác giả; nếu chưa có, ghi chính xác: `[CHƯA CÓ PHẢN HỒI TÁC GIẢ]` |
| Likely defense question | Câu hỏi hội đồng có thể chất vấn |
| Text action | `KEEP` / `REWRITE` / `SIMPLIFY` / `REMOVE_PROPOSED` / `NO_TEXT_CHANGE` |
| Status | `READY` / `SIMPLIFY` / `AUTHOR_CONFIRM` / `EVIDENCE_GAP` / `REMOVE_CANDIDATE` |
| Review trace | reviewer / ngày / căn cứ xác nhận cụ thể |

**Bắt buộc về Review trace:** Bất kỳ thẻ nào có `Status = READY` nhưng thiếu trường `Review trace` cụ thể đều bị coi là **INVALID READY** (không hợp lệ).

`DEC_ID_COLLISION_HISTORICAL`: Khi Defense Card dẫn DEC-22 hoặc DEC-23, bắt buộc ghi **ID + tên quyết định + ngày + vị trí trong PROJECT_STATE.md** để phân biệt các mục cùng ID lịch sử.

---

## 10. Pre-Flight Rule Version Check

Trước khi thực hiện bất kỳ tác vụ nào có sử dụng hệ thống Defense Readiness:

1. Đọc kỹ `work/do-an/PROJECT_STATE.md`;
2. Đọc kỹ `work/do-an/DEFENSE_READINESS.md`;
3. Xác định commit và đợt review gần nhất của quy tắc Defense Readiness;
4. Kiểm tra xem branch hiện tại có chứa đầy đủ các bản vá (patches) và quy tắc đã được thống nhất trong independent review hay chưa.

**Quy tắc dừng khẩn cấp:**
Nếu phát hiện thiếu bất kỳ patch hoặc quy tắc nào đã được ghi nhận:
**STOP NGAY LẬP TỨC.**

Xuất thông báo lỗi:
```
DEFENSE_RULE_VERSION_MISMATCH
- Phần thiếu: [liệt kê chi tiết quy tắc hoặc patch bị thiếu]
```
TUYỆT ĐỐI KHÔNG được tiếp tục chỉnh sửa chương với phiên bản quy tắc cũ hoặc chưa hoàn thiện. Không được tự giả định "phần thiếu nhỏ nên vẫn làm tiếp".

---

## 11. Quy Trình Phản Biện Ngược Bắt Buộc (Counter-Review)

Sau khi agent hoàn thành việc rà soát và đánh giá các Defense Cards, bắt buộc phải chạy một lượt phản biện ngược độc lập đối với **MỖI THẺ CÓ TRẠNG THÁI READY**.

Với từng thẻ `READY`, reviewer phải tự chất vấn qua 6 câu hỏi:
1. *Evidence nào thực sự cho phép thẻ này đạt READY?*
2. *Có đang sử dụng project decision (DEC/phạm vi đã duyệt) thay cho author ownership không?*
3. *Có bất kỳ bước suy diễn (inference) nào đang bị đánh đồng thành sự thật hiển nhiên (fact) không?*
4. *Nếu lược bỏ toàn bộ những câu giải thích do agent tự viết, liệu có còn bằng chứng thực sự cho thấy tác giả đã xác nhận nội dung này không?*
5. *Có artifact mới hơn nào đang reopen hoặc xung đột với nguồn/quyết định được sử dụng không?*
6. *Thẻ này có lý do xác đáng nào để bị hạ xuống `AUTHOR_CONFIRM`, `EVIDENCE_GAP` hoặc `SIMPLIFY` không?*

**Nguyên tắc xử lý:**
Nếu xuất hiện bất kỳ nghi ngờ hợp lý nào: **DOWNGRADE NGAY LẬP TỨC**. Tuyệt đối không giữ trạng thái `READY` chỉ vì văn bản đã được viết xong hoặc nghe có vẻ xuôi tai.

---

## 12. Bộ 6 Hard Test Cases Chuẩn Hóa

Hệ thống Defense Readiness sau khi hoàn thiện bắt buộc phải xử lý chính xác 6 trường hợp kiểm thử sau:

- **TEST A (Project decision vs. Author mastery):**
  - Tình huống: Dự án đã khóa phạm vi chọn CVE-2017-0144 (qua DEC-06/DEC-09), nhưng chưa có ghi nhận trực tiếp lời giải thích của tác giả về lý do chọn CVE này thay vì các CVE khác.
  - Xử lý: `Evidence key = PASS`, `Ownership key = FAIL` $\to$ **Status bắt buộc: `AUTHOR_CONFIRM`**. Cấm chuyển `READY` chỉ dựa vào `RESEARCH_MAP` hoặc quyết định `LOCKED`.
- **TEST B (Author ownership confirmed):**
  - Tình huống: Tác giả đã trực tiếp xác nhận lý do sử dụng khung 4 mức để tránh false positive, tránh crash kernel pool và bảo toàn tương thích mạng trong `AUTHOR_VOICE.md` (dòng 67–71; được phê duyệt tại DEC-05 và DEC-22 — Phê duyệt ba lựa chọn giọng 1B, 2A, 3A, ngày 2026-10-04, vị trí: mục “Quyết định mới: phê duyệt giọng ngày 2026-10-04” trong PROJECT_STATE.md).
  - Xử lý: `Evidence key = PASS`, `Ownership key = PASS` $\to$ **Status: `READY`** kèm `Review trace` cụ thể: Antigravity / 2026-10-04 / AUTHOR_VOICE.md dòng 67–71 (DEC-05 / DEC-22 — Phê duyệt ba lựa chọn giọng 1B, 2A, 3A, ngày 2026-10-04, mục "Quyết định mới: phê duyệt giọng ngày 2026-10-04" trong PROJECT_STATE.md).
- **TEST C (Công cụ dùng chung tín hiệu kỹ thuật):**
  - Tình huống: Nmap NSE (`smb-vuln-ms17-010.nse`) và Metasploit scanner (`smb_ms17_010`) cùng gửi gói tin thăm dò `IPC$` và cùng bắt mã lỗi `0xC0000205`.
  - Xử lý: Không được gọi đây là hai nguồn bằng chứng độc lập. Đối với claim hẹp khẳng định "hai công cụ là hai bản cài đặt khác nhau của cùng một logic thăm dò, không độc lập về tín hiệu": `Evidence key = PASS`, `Ownership key = NOT_APPLICABLE` $\to$ **Status: `READY`**.
- **TEST D (Biên tập thu hẹp claim):**
  - Tình huống: Agent sửa câu văn vượt bằng chứng thành một câu hẹp hơn, đúng với nguồn.
  - Xử lý: Không được tự động ghi nhận “EVIDENCE_GAP closed”. Reviewer phải đánh giá lại Evidence Key cho claim mới; nếu claim mới đòi hỏi tác giả giải thích, suy ra trạng thái theo đúng Derivation Rule.
- **TEST E (Hiện tượng crash vs. Kernel root cause):**
  - Tình huống: Quá trình kiểm thử gây ra màn hình xanh (BSOD) trên máy chủ nhưng không có công cụ quan sát trực tiếp bộ nhớ nhân từ xa.
  - Xử lý: Tuyệt đối không kết luận “chứng minh lỗi tràn bộ nhớ nhân đã được kích hoạt thành công”. Chỉ được kết luận ở mức quan sát hỗ trợ: hệ thống mất ổn định / ảnh hưởng tính sẵn sàng.
- **TEST F (Agent biết câu trả lời nhưng tác giả chưa phản hồi):**
  - Tình huống: Agent biết rõ câu trả lời kỹ thuật chuẩn xác cho một câu hỏi bảo vệ, nhưng tác giả chưa trực tiếp trả lời.
  - Xử lý: Trường `Author response` BẮT BUỘC ghi `[CHƯA CÓ PHẢN HỒI TÁC GIẢ]`. Tuyệt đối không tự sinh câu trả lời mẫu hoặc gợi ý bảo vệ.

---

## 13. Historical Pilot Examples (HISTORICAL_EXAMPLE_ONLY)

> **LƯU Ý LỊCH SỬ (HISTORICAL_EXAMPLE_ONLY):**
> Phần này lưu lại các thẻ pilot từ đợt chạy thử nghiệm ban đầu nhằm phục vụ việc kiểm thử mẫu template 15 trường và quy tắc Two-Key.
> **Đây KHÔNG phải là trạng thái hoạt động hiện hành (Active State)**.
> Single Source of Truth cho trạng thái hoạt động hiện hành của các thẻ DR-C1-01 đến DR-C1-08 được lưu trữ và theo dõi độc quyền tại [`work/do-an/CHAPTER_1_DEFENSE_REVIEW.md`](file:///e:/word_ppt-auto/work/do-an/CHAPTER_1_DEFENSE_REVIEW.md).
> Mọi cập nhật trạng thái chỉ được thực hiện trên artifact Defense Review chuyên biệt, không cập nhật song song vào tài liệu quy tắc này.

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
| Claim | Nguyên nhân gốc rễ của CVE-2017-0144 là sự sai lệch kích thước giữa `SrvOs2FeaListSizeToNt` và `SrvOs2FeaToNt`, dẫn đến Kernel Pool Overflow; giữ tên hai hàm làm mốc kỹ thuật, lược bỏ chi tiết reverse engineering mã khai thác. |
| Evidence / Data | S013 (Rapid7 Exploit Analysis), S005 (Microsoft MS17-010); CLAIM_MATRIX (C002); DEC-09, DEC-12, DEC-13. |
| Evidence boundary | Đồ án giải thích nguyên lý nhân quả (kích thước cấp phát vs. ghi thực tế), không tự nhận đã dịch ngược mã máy của driver `srv.sys`. |
| Evidence key | PASS |
| Author ownership evidence | Chưa có văn bản tác giả tự xác nhận mức độ làm chủ và cách giải thích hai hàm này trước câu hỏi hội đồng. |
| Ownership key | FAIL |
| Why needed | Trả lời RQ2 về cơ chế phát sinh lỗi bộ nhớ ở mức nguyên lý, tránh bị chất vấn sâu vào chi tiết khai thác ngoài tầm đề tài đại học. |
| Author must explain | Giải thích chuỗi nhân quả: tính sai kích thước $\to$ cấp phát thiếu $\to$ ghi vượt bộ đệm $\to$ tràn bộ nhớ nhân $\to$ nguy cơ mất ổn định/thực thi mã. |
| Author response | [CHƯA CÓ PHẢN HỒI TÁC GIẢ] |
| Likely defense question | Nếu bỏ tên hai hàm xử lý FEA, nhóm có còn giải thích được cơ chế lỗi và điều kiện tác động không; vì sao cần giữ tên hàm? |
| Text action | SIMPLIFY |
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

## 14. Tổng Hợp Pilot Lịch Sử (Historical Baseline Only)

> **GHI CHÚ:** Bảng tổng hợp dưới đây là số liệu lịch sử tại thời điểm hoàn thành đợt chạy thử ban đầu, phục vụ đối soát hồi quy. Tiến độ và trạng thái hiện hành được quản lý độc quyền tại [`work/do-an/CHAPTER_1_DEFENSE_REVIEW.md`](file:///e:/word_ppt-auto/work/do-an/CHAPTER_1_DEFENSE_REVIEW.md).
- **Tổng số thẻ:** 8 thẻ
- **Phân bổ trạng thái:**
  - `READY`: **2 thẻ** (DR-C1-02, DR-C1-05) — cả hai đều có căn cứ xác nhận cụ thể và vượt qua counter-review.
  - `AUTHOR_CONFIRM`: **6 thẻ** (DR-C1-01, DR-C1-03, DR-C1-04, DR-C1-06, DR-C1-07, DR-C1-08) — phản ánh đúng việc tác giả chưa trực tiếp đưa ra câu trả lời bảo vệ cho các vấn đề này.
  - `EVIDENCE_GAP`: **0 thẻ** (các phát biểu đã được căn chỉnh đúng ranh giới bằng chứng hiện có).
  - `SIMPLIFY`: **0 thẻ** (DR-C1-07 có Text action = SIMPLIFY, nhưng do Ownership key = FAIL nên Status bắt buộc là `AUTHOR_CONFIRM` theo Derivation Rule).
  - `REMOVE_CANDIDATE`: **0 thẻ**.

**Kết luận đánh giá:**
Kết quả này hoàn toàn hợp lệ theo nguyên tắc **UNRESOLVED IS VALID**. Việc còn 6 thẻ `AUTHOR_CONFIRM` không phải là khuyết điểm của đợt review, mà là đầu ra chất lượng cao giúp chỉ rõ cho tác giả những câu hỏi trọng yếu cần chuẩn bị trước khi bảo vệ đồ án.
