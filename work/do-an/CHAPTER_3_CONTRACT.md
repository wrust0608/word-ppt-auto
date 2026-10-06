# CHAPTER 3 CONTRACT — CURRENT CANONICAL

Trạng thái: `LOCKED_SECTIONED_WORKFLOW_2026_10_06`

## 1. Câu hỏi của chương

Các phép đo thực tế cho thấy gì về:
- trạng thái baseline;
- khả năng tiếp cận TCP 139/445;
- trạng thái giao thức SMB;
- tín hiệu MS17-010 từ xa;
- trạng thái bản vá cục bộ;
- thay đổi sau Case B và Case C?

## 2. Kết luận mục tiêu

Chương 3 phải cho người đọc thấy, bằng dữ liệu thực nghiệm:
- baseline có TCP 139/445 có thể tiếp cận từ Kali, SMBv1 hiện diện và local patch state là UNPATCHED;
- remote smb-vuln-ms17-010 không sinh usable verdict, nên remote classification = UNKNOWN;
- Case B làm SMBv1 biến mất khỏi phép thương lượng đã đo nhưng không patch host;
- Case C làm 139/445 từ Kali chuyển sang filtered/no-response trong đường dẫn pfSense, trong khi local patch state của Windows không đổi;
- pfSense log ghi matching SMB SYN traffic bị Block, nhưng exact named-rule attribution vẫn unresolved.

## 3. Cấu trúc H2 hiện hành

# CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH

## 3.1. Trạng thái baseline trước đo đạc
## 3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB
## 3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010
## 3.4. Kết quả Case B — Vô hiệu hóa SMBv1
## 3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense
## 3.6. So sánh kết quả thực nghiệm
## 3.7. Tổng kết chương

Chi tiết H3, số bảng và số hình được khóa **theo từng section sau khi evidence/presentation plan của section đó được review**.

Không có quota toàn chương cố định cho H3, bảng hoặc ảnh.

## 4. Workflow bắt buộc

Chương 3 được thực hiện theo từng phần:

- X7A — 3.1 Baseline
- X7B — 3.2 Scenario 1
- X7C — 3.3 Scenario 2
- X7D — 3.4 Case B
- X7E — 3.5 Case C
- X7F — 3.6 + 3.7
- X7G — mechanical Chapter 3 assembly
- X7H — whole-Chapter-3 coherence/technical review + user approval
- X7I — after X7H approval only: assemble locked Chapter 2 + approved Chapter 3 into one review DOCX
- X7J — final combined Chapters 2+3 review + user evaluation, then STOP

Mỗi section có hai bước nội dung:
1. evidence/presentation plan;
2. prose draft sau khi plan được review.

Mỗi section chỉ được mở sau khi section trước được approved và tích hợp vào `feature/ch3-integration`.

## 5. Artifact bắt buộc cho mỗi section

Mỗi section phải có:

- `*_FIGURE_SELECTION.md`
- `*_CLAIM_EVIDENCE_MAP.md`
- `*_DRAFT_R*.md`
- `*_SELF_REVIEW.md`

Claim map là internal QA artifact, không được đưa vào báo cáo sinh viên.

## 6. Quy tắc truy vết claim

100% experimental result claim trong prose phải ánh xạ được tới:
- direct/raw evidence;
- stable Evidence ID;
- external verified source nếu claim dùng quy tắc/threshold bên ngoài.

Raw/direct evidence có quyền cao hơn summary/meta.

Metadata/manifest chỉ dùng cho lineage/context khi direct evidence đã tồn tại.

## 7. Technical locks

- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `UNKNOWN != SAFE`
- `FILTERED != PATCHED`
- `SMBv1 disabled != PATCHED`
- .56.100 identity = UNKNOWN
- remote NSE signal độc lập với local patch state
- Case C exact named-rule attribution = unresolved conflict
- không có canonical exploitation/RCE/reverse shell/Meterpreter
- Case A patch không phải completed experiment

Patch baseline:
- FileVersion String: `6.3.9600.16384`
- numeric srv.sys: `6.3.9600.16421`
- Microsoft minimum updated: `6.3.9600.18604`
- relevant KB mapping: KB4012213 / KB4012216 or superseding update
- local classification: `UNPATCHED`

## 8. Chapter 3 / Chapter 4 boundary

Chương 3:
- measured result;
- direct before/after;
- bounded direct interpretation;
- factual comparison.

Chương 4:
- CIA impact;
- risk/severity;
- mitigation effectiveness judgment;
- recommendation;
- residual risk;
- patch strategy;
- enterprise deployment implications.

Không đưa risk ranking hoặc recommendation vào Chương 3.

## 9. Figure policy

Không có số lượng ảnh cố định cho toàn chương.

Mỗi section:
- review toàn bộ screenshot liên quan;
- KEEP / OPTIONAL / DROP;
- chỉ giữ ảnh có giá trị chứng minh riêng;
- ưu tiên bảng nếu bảng truyền đạt tốt hơn screenshot.

Nếu cần crop:
- giữ nguyên source evidence;
- tạo derived presentation copy;
- ghi source path + source SHA-256 + crop purpose/rectangle trong derivation note;
- không crop bỏ context làm thay đổi nghĩa.

## 10. Numbering policy

Số Hình/Bảng chỉ được khóa sau khi section được user-approved.

Counter hiện hành được quản lý tại:
`work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`.

Section sau bắt đầu từ counter đã khóa của integration branch.

Không renumber section đã approved nếu không có explicit reopen.

## 11. Integration policy

Nhánh tích hợp hiện hành:
`feature/ch3-integration`.

Mỗi section branch phải sinh từ HEAD hiện hành của integration branch.

Sau external review + user approval:
- approved section artifacts được tích hợp vào integration branch;
- terminology/numbering của section đó trở thành dependency cho section kế tiếp.

Final Chapter 3 assembly chỉ được phép ghép các section đã approved.

Section approval locks experimental facts, evidence allocation, figure/table numbering and technical meaning. During X7H, editorial compression, duplicate-sentence removal and transition cleanup are allowed when they do not change technical meaning. Any factual/technical meaning change requires explicit reopen of the affected section.

No Chapter 2+3 DOCX may be assembled before X7H user approval.

## 12. Exclusions

Không dùng:
- Case A như kết quả thực nghiệm;
- historical reports làm ground truth;
- troubleshooting/pre-repair như main result;
- fabricated NTSTATUS;
- remote SAFE/VULNERABLE/NOT VULNERABLE khi raw không có verdict;
- internal governance jargon làm cấu trúc báo cáo.

## 13. Size

Không khóa số từ theo section trước khi xem evidence.

Target toàn Chương 3 is not a quota. Sections 3.1–3.3 already contain substantial prose, so X7D–X7F must be concise and X7H must actively remove cross-section repetition. The final criterion is a coherent, defense-ready chapter, not the sum of independently maximized sections.


## 14. Current product stop — DEC-91

For the current milestone:
- Chapter 4 is dormant;
- no standalone final Chapter 3 DOCX is required;
- after X7H user approval, X7I combines the locked Chapter 2 with the approved Chapter 3;
- X7J reviews that combined Chapters 2+3 product with the user;
- after X7J, STOP until explicit new user scope.
