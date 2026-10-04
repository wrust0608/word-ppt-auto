# EXECUTION PLAN — ĐỒ ÁN SMB/NMAP/NSE–MS17-010

Trạng thái: `ACTIVE / X0_IN_PROGRESS`  
Ngày: 2026-10-05  
Nguồn: `ROADMAP_BLUEPRINT_2026_10_05.md`, `ROADMAP_BLUEPRINT_REAUDIT_2026_10_05.md`, `EXPERIMENTAL_TRUTH_MATRIX.md`.

## 1. Nguyên tắc thực thi

1. Không làm lại phần đã có nếu artifact hiện hành còn hợp lệ.
2. Artifact LOCKED chỉ được sửa khi có quyết định reopen rõ.
3. Evidence canonical chi phối Chương 2–4.
4. Báo cáo cũ chỉ là historical reference.
5. Mỗi phase có input, output, gate và reviewer riêng.
6. Không chạy DOCX trước G5 synthesis.
7. Không chạy defense package trước khi nội dung báo cáo đã khóa.
8. Chương 3 là high-risk chapter và được ưu tiên QA cao nhất.

## 2. Trạng thái nền hiện tại

### Đã có và có thể tái sử dụng
- `INSTITUTION_PROFILE.md`
- `AUTHOR_VOICE.md`
- `SOURCE_LEDGER.md` (có mục RECHECK)
- `CLAIM_MATRIX.md` (cần realign cho Chương 2–4)
- `CHAPTER_1.md` (review pending)
- `EXPERIMENTAL_TRUTH_MATRIX.md`
- evidence canonical Scenario 1 / Scenario 2 / Case B / Case C
- QA lịch sử của DOCX

### Có nhưng stale / conflict
- `PROJECT_PROFILE.md`: còn chỉ thị “tránh demo”, công cụ/platform chưa khớp canonical.
- `RESEARCH_MAP.md`: M3/M4 còn stale; ngôn ngữ mitigation quá mạnh.
- `OUTLINE.md`: lệch với evidence canonical.
- `CHAPTER_ARGUMENT.md`: Windows 7 / 3 VLAN / Client đối chứng lịch sử.
- `CHAPTER_2.md`: không còn đại diện cho lab canonical.
- `ROADMAP_2_6.md`: chỉ là sub-roadmap writing/recovery.
- Word cũ: historical/rebuild required.

## 3. Phase X0 — Requirement & Governance Reconciliation

### Input
Blueprint, đề cương chi tiết, HUIT profile, Project Profile, Research Map, Truth Matrix.

### Công việc
- tạo `REQUIREMENT_RECONCILIATION.md`;
- tạo `RUBRIC_TRACEABILITY_MATRIX.md`;
- tạo `TEAM_RESPONSIBILITY_MATRIX.md`;
- tạo `CHANGE_CONTROL.md`;
- xác định artifact stale và đề xuất reopen.

### Output
4 artifact trên + proposal patch cho Project Profile/Research Map.

### Gate X0
PASS khi:
- mọi CLO/rubric có section/deliverable/evidence owner;
- không còn chỉ thị stale chưa được ghi nhận;
- change-control rõ;
- reviewer duyệt.

### Reviewer
Assistant QA + User final approval.

## 4. Phase X1 — Canonical Evidence Governance

### Input
ALL evidence + Experimental Truth Matrix.

### Công việc
- tạo `EVIDENCE_REGISTER.md`;
- tạo `EVIDENCE_CONFLICT_REPORT.md`;
- tạo `CANONICAL_EVIDENCE_SHA256.txt` nếu toàn bộ canonical files truy cập được;
- tạo `NEGATIVE_RESULT_POLICY.md`;
- khóa stable Evidence IDs;
- phân loại CANONICAL / SUPPORTING / TROUBLESHOOTING / HISTORICAL / EXCLUDED.

### Gate X1
PASS khi:
- 100% experimental claims dự kiến có evidence ID;
- raw vs summary conflict = 0 unresolved;
- Scenario 1/2/Case B/Case C có lineage rõ;
- secret/privacy scan không blocker.

### Reviewer
Assistant QA.

## 5. Phase X2 — Research & Argument Realignment

### Input
X0 + X1 + Source Ledger.

### Công việc
- đề xuất sửa `PROJECT_PROFILE.md`;
- đề xuất sửa `RESEARCH_MAP.md`;
- tạo `ARGUMENT_MAP_2_4_PROPOSED.md`;
- tạo `CLAIM_MATRIX_2_4.md`;
- khóa distinction SOURCE_FACT / AUTHOR_DATA / INTERPRETATION / PROPOSAL.

### Gate X2
PASS khi:
- RQ1–RQ4 có evidence/method khả thi;
- O1–O4 không đòi exploit success;
- Case A không bị nhận là canonical nếu chưa audit;
- wording không overclaim.

### Reviewer
Assistant QA + User approval nếu thay LOCKED artifact.

## 6. Phase X3 — Report Architecture Freeze

### Input
X0–X2.

### Công việc
- tạo `OUTLINE_2_4_PROPOSED.md`;
- tạo `CHAPTERS_2_4_EVIDENCE_MAP.md`;
- tạo `CHAPTER_2_CONTRACT.md`;
- tạo `CHAPTER_3_CONTRACT.md`;
- tạo `CHAPTER_4_CONTRACT.md`;
- tạo figure/table budget;
- xác định appendix plan.

### Gate X3A — WBS_FREEZE
Toàn bộ work item đủ và dependency rõ.

### Gate X3B — REPORT_OUTLINE_FREEZE
PASS khi:
- mỗi heading có nhiệm vụ;
- mỗi result heading có evidence ID;
- không có mục chỉ “giới thiệu công cụ”;
- Ch2/Ch3/Ch4 tách rõ method/result/analysis;
- reviewer và user duyệt.

### Reviewer
Assistant QA + User final approval.

## 7. Phase X4 — Chapter 1 Final Review

### Lý do
Chương 1 đã có nền tảng mạnh, không viết lại từ đầu.

### Công việc
- kiểm source recheck;
- sửa technical inaccuracies còn lại;
- đảm bảo nền lý thuyết phục vụ Ch2–4;
- tránh pfSense/tool exposition quá mức;
- citation audit;
- style/lint;
- review toàn chương.

### Gate X4
PASS khi:
- không claim sai MS17-010/CVE;
- SMB signing/dialect chính xác;
- không lặp Ch2–4;
- source/citation pass;
- user duyệt.

## 8. Phase X5 — Chapter 2 Production

### Công việc
Viết từ contract đã khóa:
- yêu cầu thiết kế;
- VirtualBox/Kali/Windows Server 2012 R2;
- Host-Only;
- IP/NIC;
- SMB/Firewall prep;
- patch baseline;
- tools;
- snapshot;
- thiết kế Scenario 1;
- thiết kế Scenario 2;
- thiết kế Case B/C;
- evidence collection method;
- evaluation criteria.

### Gate X5
PASS khi:
- method/result separation rõ;
- mọi config fact có evidence;
- đủ tái lập;
- không troubleshooting diary;
- reviewer chấm >= 90/100;
- user duyệt.

## 9. Phase X6 — Chapter 3 Production (Critical)

### Công việc
- pre-test state;
- Scenario 1;
- Scenario 2;
- local patch reconciliation;
- Case B;
- Case C;
- summary matrix;
- negative/UNKNOWN findings;
- inference boundaries.

### QA bắt buộc
- 100% result claim -> Evidence ID;
- prose/raw consistency;
- raw > screenshot > summary;
- no historical contamination;
- no exploit claim;
- no fake verdict.

### Gate X6
PASS khi:
- 100% traceability;
- 0 unresolved raw/prose conflict;
- Truth Matrix compliance 100%;
- reviewer chấm >= 92/100;
- user duyệt.

## 10. Phase X7 — Chapter 4 Production

### Công việc
- cross-case comparison;
- reachability/protocol/vulnerability/patch distinction;
- Case B evaluation;
- Case C evaluation;
- patching role;
- defense-in-depth;
- residual risk;
- threats to validity;
- compatibility/operational impact;
- recommendations;
- future work.

### Gate X7
PASS khi:
- không đưa evidence thực nghiệm mới;
- mọi recommendation có source/proposal status;
- limitations cụ thể;
- RQ4 được trả lời đúng phạm vi;
- reviewer chấm >= 90/100;
- user duyệt.

## 11. Phase X8 — Front Matter, Introduction, Conclusion, Appendices

### Công việc
- Mở đầu;
- tóm tắt/abstract;
- kết luận và kiến nghị;
- contribution wording;
- acronym list;
- appendix evidence index;
- commands/runbook appendix;
- selected raw outputs.

### Điều kiện
Chỉ khóa contribution/conclusion sau X6/X7.

### Gate X8
PASS khi:
- Intro ↔ results ↔ conclusion nhất quán;
- không claim mới;
- phụ lục không lặp thân bài vô ích.

## 12. Phase X9 — G5 Synthesis

### Công việc
- RQ answer matrix;
- Objective completion matrix;
- global terminology/data consistency;
- IEEE global numbering;
- citation/reference audit;
- cross-reference;
- acronym consistency;
- anti-rambling pass;
- author voice;
- publication lint.

### Gate X9
PASS khi:
- RQ/O closure rõ;
- không orphan source/citation;
- no unresolved labels;
- full Markdown approved.

## 13. Phase X10 — G6 Publication

### Công việc
- tạo DOCX từ Markdown locked;
- HUIT formatting;
- TOC/LoF/LoT;
- numbering;
- references;
- validate;
- render all pages;
- page-by-page QA;
- regenerate.

### Gate X10
PASS khi:
- Word mở không repair;
- publication lint pass;
- mọi trang đã xem;
- không layout blocker;
- Markdown/DOCX cùng version.

## 14. Phase X11 — G7 Defense Package

### Công việc
- slide;
- Q&A bank >=25;
- evidence quick index;
- demo runbook;
- rollback;
- failure-mode plan;
- member role allocation;
- rehearsal.

### Gate X11
PASS khi:
- slide claim khớp report;
- mỗi thành viên bảo vệ được phần lõi;
- có phương án khi NSE04 UNKNOWN;
- demo từ snapshot có thể phục hồi.

## 15. Parallel Workstreams

Có thể song song:
- X1 Evidence Governance với source metadata cleanup của X4.
- Figure/table planning với X3.
- Q&A seed list có thể bắt đầu sau X6 nhưng chỉ khóa sau X9.

Không song song:
- Ch2–4 prose trước X3B.
- Conclusion trước X6/X7.
- DOCX trước X9.
- Defense final trước X9/X10.

## 16. Checkpoints

- CP0: X0 PASS — governance sạch.
- CP1: X1 PASS — evidence sạch.
- CP2: X2 PASS — research logic sạch.
- CP3: X3B PASS — outline freeze.
- CP4: X4 PASS — Ch1 khóa.
- CP5: X5 PASS — Ch2 khóa.
- CP6: X6 PASS — Ch3 khóa.
- CP7: X7 PASS — Ch4 khóa.
- CP8: X9 PASS — full Markdown khóa.
- CP9: X10 PASS — DOCX khóa.
- CP10: X11 PASS — defense ready.

## 17. Ưu tiên thực tế

P0 Critical:
- X0, X1, X2, X3.
P1 Highest academic:
- X6, X7.
P2:
- X5, X4.
P3:
- X8, X9.
P4:
- X10.
P5:
- X11.

Chương 3 được ưu tiên QA cao nhất vì chứa AUTHOR_DATA.

## 18. Điều kiện kích hoạt

Execution Plan chỉ được ACTIVE sau final audit:
- dependency đúng;
- không bỏ rubric;
- không bỏ evidence workstream;
- không có write-before-evidence;
- không có DOCX-before-synthesis;
- không có blocker governance;
- user đã cho phép triển khai.

