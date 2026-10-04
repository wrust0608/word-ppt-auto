# ROADMAP BLUEPRINT AUDIT — 2026-10-05

Đối tượng: `ROADMAP_BLUEPRINT_2026_10_05.md`  
Trạng thái kết luận: `CONDITIONAL_PASS / NOT_ACTIVE`

# 1. Kết luận

Blueprint đã bao phủ phần lớn vòng đời đồ án và phản ánh đúng việc demo/evidence là workstream trọng tâm. Tuy nhiên **chưa được kích hoạt làm roadmap thực thi** vì còn một số khoảng trống quản trị có thể gây drift khi giao cho agent.

Điểm tổng hợp: **93.4/100 — CONDITIONAL PASS**.

Không có lỗi làm mất toàn bộ kiến trúc, nhưng có **5 blocker cần sửa trước khi ACTIVE**.

# 2. Chấm theo cổng Q

| Tiêu chí | Điểm | Ngưỡng | Kết luận |
|---|---:|---:|---|
| Coverage toàn đồ án | 96/100 | 95 | PASS |
| Logic / dependency | 92/100 | 90 | PASS |
| Demo / evidence control | 97/100 | 95 | PASS |
| Academic integrity | 97/100 | 95 | PASS |
| HUIT compliance | 95/100 | 95 | PASS |
| Governance / change control | 84/100 | không blocker | FAIL/BLOCKER |
| Defense readiness | 94/100 | 90 | PASS |

# 3. Điểm mạnh

## 3.1. Bao phủ đúng khối lượng demo
Blueprint đã tách riêng:
- baseline/environment;
- Scenario 1;
- Scenario 2;
- Case B;
- Case C;
- historical/non-canonical evidence;
- evidence register và QA.

Đây là cải tiến lớn so với ROADMAP_2_6 cũ.

## 3.2. Phân biệt đúng các lớp bằng chứng
Có tuyến:
`source fact -> author data -> interpretation -> proposal`.

Có tuyến thực nghiệm:
`reachability -> protocol -> remote vulnerability signal -> local patch ground truth -> mitigation`.

Điều này phù hợp với quy tắc integrity của repo và Experimental Truth Matrix.

## 3.3. Kiến trúc báo cáo đầy đủ
Đã bao phủ:
- front matter;
- mở đầu;
- Chương 1–4;
- kết luận;
- tài liệu tham khảo;
- phụ lục;
- synthesis;
- DOCX;
- defense.

## 3.4. Đã chống được lỗi “viết trước, tìm evidence sau”
Blueprint đặt Evidence/Claim/Contract trước chapter production.

## 3.5. Defense đã trở thành workstream chính thức
Có slide, Q&A, evidence quick index, demo runbook, rollback và rehearsal.

# 4. BLOCKER phải sửa trước khi ACTIVE

## BLK-01 — Chưa có Change-Control / Decision-Control riêng
Hiện blueprint có nguồn ưu tiên nhưng chưa có quy trình khi:
- người dùng đổi phạm vi;
- GVHD yêu cầu thay nội dung;
- phát hiện evidence mới;
- phục hồi Case A;
- một artifact LOCKED phải mở lại.

Cần thêm:
- Change Request;
- impact analysis;
- người có quyền duyệt;
- artifact bị ảnh hưởng;
- rollback/decision log;
- cấm agent tự đổi scope.

## BLK-02 — Chưa có Rubric Traceability Matrix chính thức
Blueprint có HUIT/CLO nhưng chưa bắt buộc ánh xạ từng tiêu chí chấm sang:
- section báo cáo;
- evidence;
- deliverable;
- gate.

Cần artifact:
`RUBRIC_TRACEABILITY_MATRIX.md`.

Nếu không có, có nguy cơ báo cáo tốt về kỹ thuật nhưng bỏ sót tiêu chí được chấm điểm.

## BLK-03 — Chưa khóa “Evidence Storage & Provenance Boundary”
Evidence hiện đến từ gói ngoài repo và có thể quá lớn để commit.

Cần quy định:
- evidence nào nằm trong repo;
- evidence nào nằm external/local;
- canonical path;
- cách trích dẫn/định danh;
- cách hash;
- cách bàn giao;
- cách agent đọc mà không làm mất provenance.

Nếu không, Evidence ID có thể ổn về logic nhưng đường dẫn bị gãy khi đổi máy/agent.

## BLK-04 — Chưa có Author/Team Contribution & Review Responsibility Matrix
Đề tài nhóm và quá trình bảo vệ cần biết:
- ai chịu trách nhiệm phần nào;
- ai kiểm tra chéo;
- ai vận hành demo;
- ai trả lời lý thuyết;
- ai giữ evidence/rollback.

Không cần đưa chi tiết nội bộ vào thân báo cáo, nhưng roadmap cần quản trị.

Artifact đề xuất:
`TEAM_RESPONSIBILITY_MATRIX.md`.

## BLK-05 — Chưa có “Final Outline Freeze Gate” tách khỏi WBS Freeze
Blueprint hiện chứa cả work breakdown và kiến trúc báo cáo, nhưng hai thứ này không nên khóa cùng lúc.

Cần hai gate:
1. `WBS_FREEZE` — toàn bộ việc phải làm đã đầy đủ.
2. `REPORT_OUTLINE_FREEZE` — mục lục học thuật Chương 1–4 đã được reviewer duyệt.

Chỉ sau REPORT_OUTLINE_FREEZE mới được tạo chapter contracts và prose.

# 5. Major issues không phải blocker

## MAJ-01 — Chương 1 cần tránh phình scope
F3.8 firewall/pfSense/mitigation concepts chỉ nên đủ làm nền cho Chương 4; không biến Chương 1 thành hướng dẫn pfSense.

## MAJ-02 — Mở đầu cần khóa “đóng góp” sau khi Chương 3–4 ổn định
Có thể tạo placeholder contract nhưng không chốt contribution wording quá sớm.

## MAJ-03 — Case A phải có decision branch rõ
Nếu evidence Case A được phục hồi:
- audit;
- xác định có cùng lineage/canonical experiment không;
- nếu khác lineage, chỉ dùng như supplementary experiment.

Nếu không phục hồi:
- giữ ở recommendation/theory.

## MAJ-04 — Cần Negative Result Policy riêng
UNKNOWN/no output không được diễn giải tùy ý.
Đề xuất artifact:
`NEGATIVE_RESULT_POLICY.md`.

## MAJ-05 — Cần figure budget
Dù blueprint có figure selection, nên đặt budget:
- main body: chỉ hình phục vụ claim;
- raw/troubleshooting: appendix;
- tránh một bước lệnh = một screenshot.

## MAJ-06 — Cần reproducibility checklist
Không chỉ lưu command; cần:
- target state;
- source state;
- network state;
- command/options;
- expected observation;
- evidence path;
- rollback state.

# 6. Các đề mục cần bổ sung vào Blueprint

## A7. Change & Decision Control
### A7.1. Change request
### A7.2. Impact analysis
### A7.3. Approval authority
### A7.4. Decision log
### A7.5. Locked artifact reopening
### A7.6. Rollback

## B5. Rubric Traceability
### B5.1. CLO/rubric criterion
### B5.2. Report section
### B5.3. Evidence/deliverable
### B5.4. Acceptance criterion
### B5.5. Completion status

## D9. Evidence Storage & Provenance
### D9.1. Repo-contained evidence
### D9.2. External/local evidence
### D9.3. Stable evidence IDs
### D9.4. Canonical paths
### D9.5. Hashing
### D9.6. Transfer/archive

## A8. Team Responsibility Matrix
### A8.1. Writing ownership
### A8.2. Technical ownership
### A8.3. Evidence ownership
### A8.4. Cross-review
### A8.5. Demo role
### A8.6. Defense role

## G0. Outline Freeze Governance
### G0.1. WBS_FREEZE
### G0.2. REPORT_OUTLINE_FREEZE
### G0.3. Chapter-contract eligibility
### G0.4. Reopen conditions

## D10. Negative / Inconclusive Result Policy
### D10.1. UNKNOWN
### D10.2. NO OUTPUT
### D10.3. FILTERED
### D10.4. Tool failure
### D10.5. Conflicting evidence
### D10.6. Retest policy

## M0. Figure & Table Budget
### M0.1. Main-body figure criteria
### M0.2. Appendix criteria
### M0.3. Redundant screenshot policy
### M0.4. Minimum readability/resolution
### M0.5. Evidence ID in caption/source note

## O19. Reproducibility Checklist
### O19.1. Environment state
### O19.2. Network state
### O19.3. Target state
### O19.4. Commands
### O19.5. Expected/actual observation
### O19.6. Evidence
### O19.7. Rollback

# 7. Quyết định audit

Không kích hoạt:
- B–P execution;
- chapter drafting;
- evidence migration;
- DOCX;
- demo rerun.

Trình tự tiếp theo:
1. Patch blueprint với BLK-01..05 và MAJ cần thiết.
2. Audit lại.
3. Chỉ khi tất cả blocker = 0 và các ngưỡng Q đều đạt, đổi trạng thái thành `APPROVED_MASTER_ROADMAP`.
4. Sau đó mới lập thứ tự execution thực tế.

# 8. Trạng thái

- Blueprint coverage: tốt.
- Logic: tốt.
- Demo/evidence: rất tốt.
- Academic integrity: rất tốt.
- Governance: chưa đủ để ACTIVE.
- **Final: CONDITIONAL PASS — NOT ACTIVE.**
