# ROADMAP — TÁI CẤU TRÚC CHƯƠNG 3 THEO LOGIC THỰC NGHIỆM VÀ EVIDENCE-FIRST

- Trạng thái: `USER_APPROVED_ARCHITECTURE / ROADMAP_ACTIVE`
- Ngày: 2026-10-07
- Branch: `feature/ch3-redesign-evidence-first-r1`
- Căn cứ phê duyệt: người dùng đã chốt kiến trúc Chương 3 mới sau khi rà soát repo, evidence và tham khảo cấu trúc khóa luận/đồ án ATTT.
- Mục tiêu: tái cấu trúc Chương 3 để người đọc không chuyên vẫn hiểu rõ tác giả đang kiểm tra gì, tại sao thực hiện từng bước, kết quả thay đổi ra sao; đồng thời bảo toàn 100% technical truth và truy vết evidence.
- Không chạy lại demo nếu evidence hiện có đủ.
- Không sửa Chương 2.
- Không mở Chương 4.
- Không dựng lại DOCX cho tới khi toàn bộ Chương 3 mới được user phê duyệt.

## 1. Kiến trúc Chương 3 đã được người dùng chốt

# CHƯƠNG 3. THỰC NGHIỆM VÀ KẾT QUẢ KIỂM THỬ DỊCH VỤ SMB

## 3.1. Mục tiêu và tổ chức thực nghiệm
### 3.1.1. Mục tiêu kiểm chứng
### 3.1.2. Luồng thực nghiệm

## 3.2. Xác lập trạng thái ban đầu của hệ thống
### 3.2.1. Trạng thái mạng và dịch vụ SMB
### 3.2.2. Trạng thái bản vá MS17-010

## 3.3. Khảo sát dịch vụ SMB từ trạm Kali Linux
### 3.3.1. Phát hiện máy chủ và khả năng tiếp cận SMB
### 3.3.2. Nhận diện giao thức và các đặc tính SMB
### 3.3.3. Tổng hợp kết quả khảo sát

## 3.4. Kiểm tra dấu hiệu MS17-010
### 3.4.1. Kết quả kiểm tra từ xa bằng Nmap/NSE
### 3.4.2. Đối chiếu với trạng thái bản vá trên Windows

## 3.5. Thực nghiệm vô hiệu hóa SMBv1 trên máy chủ
### 3.5.1. Trạng thái trước và sau khi vô hiệu hóa SMBv1
### 3.5.2. Kết quả kiểm tra lại từ Kali Linux
### 3.5.3. Tổng hợp sự thay đổi quan sát được

## 3.6. Thực nghiệm kiểm soát truy cập SMB bằng pfSense
### 3.6.1. Bố trí pfSense và kiểm soát lưu lượng SMB
### 3.6.2. Kết quả kiểm tra lại từ Kali Linux
### 3.6.3. Đối chiếu kết quả tại Kali, pfSense và Windows

## 3.7. Đối chiếu kết quả các trạng thái thực nghiệm
### 3.7.1. Đối chiếu trạng thái ban đầu và sau các can thiệp
### 3.7.2. Những thay đổi và yếu tố không thay đổi

## 3.8. Tổng kết chương

## 2. Luồng lập luận bắt buộc

`Mục tiêu kiểm chứng → trạng thái xuất phát → quan sát từ Kali → kiểm tra MS17-010 → can thiệp tại host → đo lại → can thiệp trên network path → đo lại → đối chiếu ba trạng thái → chuyển Chương 4`.

Chương 3 phải cho người đọc hiểu được câu chuyện ngay cả khi họ không có nền tảng ATTT. Thuật ngữ kỹ thuật và screenshot là bằng chứng cho câu chuyện, không được thay thế câu chuyện.

## 3. Evidence hierarchy và truth locks

Evidence precedence giữ nguyên:
`direct raw/local/visual > metadata lineage > historical/supporting > old report prose`.

Bắt buộc giữ:
- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `UNKNOWN != SAFE`
- `FILTERED != PATCHED`
- `SMBv1 disabled != PATCHED`
- local patch state độc lập với remote NSE verdict.
- Không canonical exploitation success, RCE, reverse shell, Meterpreter.
- Không Case A patch experiment; không đổi baseline thành Case A.
- Case B TCP139 không được tái đo.
- Case B port retest không có `--reason`; không gán `syn-ack`.
- Case C exact named-rule attribution vẫn unresolved.
- Không dựng unified wall-clock timeline giữa Kali/pfSense/Windows.
- Local SMB signing và remote SMB signing là hai quan sát khác nguồn.
- Không invent nguyên nhân cho NSE không có usable result.

## 4. Chiến lược tận dụng ảnh bằng chứng

Không áp dụng giới hạn ảnh cứng kiểu “tối đa 8” nếu giới hạn đó làm mất logic. Tuy nhiên vẫn chống screenshot spam.

Mỗi hình phải thuộc một trong ba vai trò:
1. **Evidence figure** — ảnh gốc/crop chứng minh một quan sát trực tiếp.
2. **Comparison figure** — ghép/crop các ảnh canonical để thể hiện Before/After hoặc Local/Remote; không sửa nội dung ảnh.
3. **Explanatory figure** — sơ đồ do báo cáo dựng từ facts đã verified; phải ghi rõ là sơ đồ tổng hợp, không giả làm evidence trực tiếp.

### 4.1. 3.1 — hình giải thích bắt buộc
Tạo 1 sơ đồ tổng hợp luồng thực nghiệm:
Baseline → khảo sát SMB → kiểm tra MS17 → hai nhánh can thiệp (SMBv1 tại host / pfSense trên network path) → retest → comparison.
Không dùng screenshot cho hình này.

### 4.2. 3.2 — baseline
Ưu tiên tận dụng:
- `baseline/Windows_PreDemo_01_Network_SMB.png`
- `baseline/Windows_PreDemo_02_Firewall.png` khi cần chứng minh scope đo
- `baseline/Windows_MS17010_01_SrvSysVersion.png`
- `baseline/Windows_MS17010_02_Hotfix.png`
Có thể ghép hợp lý các ảnh cùng một luận điểm, nhưng không che thông tin bất lợi/mâu thuẫn.
Snapshot chỉ là context phục hồi, không chiếm trọng lượng thị giác ngang patch/service state.

### 4.3. 3.3 — khảo sát từ Kali
Ưu tiên:
- `scenario1/Scenario1_B4_SMB_Ports.png`
- `scenario1/Scenario1_B5_SMB_Version.png`
- `scenario1/Scenario1_B6_SMB_NSE_A.png`
B2/B3 chủ yếu đưa vào bảng/text; không cần screenshot riêng nếu không tăng khả năng hiểu.
Trình bày theo “host → ports → service → protocol characteristics”, không theo mã B2–B6 ở mặt tiền.

### 4.4. 3.4 — MS17-010
Ưu tiên:
- `scenario2/Scenario2_NSE04_MS17010.png`
- evidence local srv.sys/hotfix đã dùng ở 3.2.
Tạo một **comparison figure hoặc comparison panel**: Remote = UNKNOWN / Local = UNPATCHED. Panel chỉ tổng hợp hai nguồn đã verified; không được biến UNKNOWN thành output literal của Nmap.
NSE01–03 dùng như confirmation context; tránh lặp screenshot nếu kết quả đã được chứng minh ở 3.3.

### 4.5. 3.5 — Case B
Phải tận dụng rõ chuỗi Before → Action → After → Remote Retest:
- `case_b/SMBv1_Remediation_01_Before.png`
- `case_b/SMBv1_Remediation_02_Action.png`
- `case_b/SMBv1_Remediation_03_After_Local.png`
- `case_b/SMBv1_Remediation_04_NSE02_Protocols.png`
- `case_b/SMBv1_Remediation_05_NSE04_MS17010.png` chỉ khi thực sự cần chứng minh remote UNKNOWN sau Case B.
Ưu tiên ghép Before/Action/After thành một figure sequence dễ đọc thay vì ba hình rời.
Bảng Before/After là thành phần chính; screenshot là chứng cứ.

### 4.6. 3.6 — Case C
Phải giúp người không chuyên nhìn ra topology và điểm kiểm soát.
Evidence hữu ích:
- `case_c/pfSense_03_Interface_Assignment.png`
- `case_c/pfSense_04_Bridge.png`
- `case_c/pfSense_05_Bridge_Filtering.png`
- `case_c/pfSense_07_Block_Rule_Config.png`
- `case_c/pfSense_08_Rule_Order.png`
- `case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`
- `case_c/pfSense_10_Block_Log_CANONICAL.png`
- `case_c/pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` khi cần.
Tạo một explanatory topology figure: Kali .56.10 → pfSense transparent bridge → Windows .56.20, đánh dấu vị trí filter 139/445.
Trong main text ưu tiên rule/order + Nmap FILTERED + firewall log. Interface/bridge/filtering screenshots có thể ghép thành một configuration evidence panel nếu cần chứng minh topology mà không gây screenshot spam.
Không crop để che conflict rule label trong log.

### 4.7. 3.7 — comparison
Không cần screenshot mới.
Tạo bảng tổng hợp theo các lớp:
- host/protocol state;
- remote reachability/observation;
- MS17 remote signal;
- local patch state;
- location of change.
Có thể tạo một explanatory figure “hai vị trí can thiệp” nếu nó làm rõ hơn bảng: Case B tác động host/protocol, Case C tác động network path.

## 5. Nguyên tắc trình bày mỗi phần

Mỗi thực nghiệm phải có nhịp:
`Câu hỏi → trạng thái/context cần thiết → evidence/measurement → kết quả nổi bật → bảng/hình trực quan → kết luận trực tiếp có giới hạn → cầu nối sang phần sau`.

Không viết:
`văn bản → screenshot → văn bản → screenshot` như nhật ký thao tác.

Screenshot không tự mang kết luận. Caption chỉ mô tả điều nhìn thấy trực tiếp. Kết luận tổng hợp nằm trong prose/bảng và phải có đủ evidence.

## 6. Migration map từ Chương 3 cũ

- Old 3.1 Baseline → New 3.2; tách phần dẫn logic ra New 3.1.
- Old 3.2 Scenario 1 → New 3.3; bỏ mã workflow khỏi narrative chính.
- Old 3.3 Scenario 2 → New 3.4; NSE01–03 trở thành confirmation context, NSE04 + local cross-check là trọng tâm.
- Old 3.4 Case B → New 3.5; tái trình bày theo Before/Action/After/Retest.
- Old 3.5 Case C → New 3.6; tái trình bày theo topology/config → Kali observation → pfSense log → Windows local cross-check.
- Old 3.6 Comparison → New 3.7; tổ chức theo “what changed / what did not”, không effectiveness ranking.
- Old 3.7 Summary → New 3.8; chỉ tổng kết empirical findings và cầu nối Ch4.
- New 3.1 là nội dung dẫn đường mới nhưng chỉ dùng mục tiêu/phương pháp đã canonical ở Ch1/Ch2; không tạo objective mới.

## 7. Numbering policy

Ledger cũ Bảng 3.1–3.7 / Hình 3.1–3.11 là lịch sử của Chương 3 đã duyệt trước đây.
Vì user đã explicit reopen architecture, **không được giữ numbering cũ một cách máy móc** nếu figure/table flow mới thay đổi.

Trước khi viết prose mới phải lập:
- `CH3_REDESIGN_TABLE_FIGURE_LEDGER_R1.md`
- ánh xạ old number → new number;
- source evidence;
- figure role (evidence/comparison/explanatory);
- caption boundary;
- keep/move/merge/retire/new.

Chỉ khóa numbering mới sau independent review + user approval của visual/evidence blueprint.

## 8. Roadmap execution gates

### R3-0 — Evidence & visual blueprint
Chưa sửa `CHAPTER_3_DRAFT_R2.md`.
Tạo:
1. `CH3_REDESIGN_EVIDENCE_VISUAL_BLUEPRINT_R1.md`
2. `CH3_REDESIGN_TABLE_FIGURE_LEDGER_R1.md`
3. `CH3_REDESIGN_CONTENT_MIGRATION_MAP_R1.md`

Phải map 100% claims/evidence cũ sang kiến trúc mới; xác định ảnh keep/move/merge/retire/new explanatory.
Gate: independent review → user approval.

### R3-1 — Draft 3.1–3.2
Viết mục dẫn đường + baseline mới.
Không mở 3.3+.
Gate: technical + narrative + visual review → user approval.

### R3-2 — Draft 3.3–3.4
Viết remote SMB survey + MS17 cross-check.
Phải kiểm soát repetition Scenario1/Scenario2.
Gate: technical + narrative + visual review → user approval.

### R3-3 — Draft 3.5
Case B theo Before/Action/After/Retest.
Gate: evidence review + user approval.

### R3-4 — Draft 3.6
Case C theo topology/config/remote/log/local.
Gate: evidence review, đặc biệt rule-label conflict + timebase boundary → user approval.

### R3-5 — Draft 3.7–3.8
Comparison + chapter summary.
Không mở risk/recommendation/defense-in-depth.
Gate: whole-argument review + user approval.

### R3-6 — Whole Chapter 3 assembly
Ghép 3.1–3.8, kiểm:
- flow cho người không chuyên;
- không lặp;
- caption/table/figure numbering;
- 100% evidence traceability;
- truth locks;
- transition to Ch4.
Gate: independent whole-Ch3 review → user approval.

### R3-7 — Ch2 ↔ Ch3 coherence check
Đối chiếu locked Ch2 với Ch3 mới.
Chỉ sửa Ch3 nếu cần; Ch2 vẫn locked trừ khi user explicit reopen.
Gate: user approval.

### R3-8 — DOCX rebuild
Chỉ sau khi Ch3 mới được user approved/locked.
Ghép locked Ch2 + new locked Ch3; render 100% pages; visual QA; exact-binary freeze.
Gate: independent review → user final evaluation.

## 9. STOP rules

Ở mỗi gate executor phải STOP.
Không tự chuyển gate.
Không sửa Ch2.
Không mở Ch4.
Không chạy lại experiment.
Không regenerate DOCX trước R3-8.
Không tự tuyên bố user approval.
Không đổi technical truth để làm narrative “đẹp hơn”.

## 10. Authorized next action

**R3-0 — Evidence & visual blueprint only.**

Đây là bước duy nhất được phép tiếp theo. Mục tiêu là thiết kế chính xác cách tái sử dụng toàn bộ evidence/ảnh trước khi viết lại một câu prose nào của Chương 3.
