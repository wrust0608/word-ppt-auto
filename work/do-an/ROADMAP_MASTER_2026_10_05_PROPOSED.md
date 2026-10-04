> **STATUS OVERRIDE 2026-10-05:** Tài liệu này hiện **KHÔNG ĐƯỢC THỰC THI**. Theo yêu cầu người dùng, phải hoàn thành và audit `ROADMAP_BLUEPRINT_2026_10_05.md` trước. Chỉ sau khi blueprint đạt tiêu chí coverage/logic/evidence/HUIT và không còn BLOCKER mới được tái cấu trúc tài liệu này thành roadmap thực thi.

# ROADMAP MASTER ĐỀ XUẤT — ĐỒ ÁN SMB/NMAP/NSE–MS17-010

Trạng thái: `SUPERSEDED_PENDING_BLUEPRINT_AUDIT / NOT_EXECUTABLE`  
Ngày đánh giá: 2026-10-05  
Mục đích: thay thế vai trò “master roadmap” mà `ROADMAP_2_6.md` hiện không đảm nhiệm; **không ghi đè ROADMAP_2_6.md**. Roadmap cũ được giữ như sub-roadmap phục hồi chất lượng nguồn/giọng/DOCX.

## 1. Kết luận audit roadmap hiện tại

`ROADMAP_2_6.md` phù hợp như một pipeline:
`NotebookLM -> source QA -> author voice -> pilot chapter -> DOCX audit`.

Nó không đủ làm roadmap tổng thể cho đồ án vì chưa có các cổng riêng cho:
- đối soát đề cương với dữ liệu demo thật;
- inventory và provenance của khối evidence lớn;
- Scenario 1 / Scenario 2;
- remediation Case B / Case C;
- negative/UNKNOWN results;
- chapter contracts Chương 2–4;
- tổng hợp risk/mitigation;
- defense package/slide/Q&A/demo recovery.

Theo đề cương chi tiết, riêng nhóm công việc CLO3 về xây dựng kịch bản, môi trường, triển khai lab, khảo sát SMB, xác minh MS17-010, thực nghiệm, phòng thủ, retest và minh chứng chiếm 4.5/10; đánh giá trước–sau thêm 0.5/10. Vì vậy demo/evidence phải là workstream hạng nhất, không phải một nhãn `[CẦN DỮ LIỆU]` nằm dưới bước viết chương.

## 2. Nguyên tắc master roadmap

1. Đề cương chi tiết + quy định HUIT > quyết định repo cũ > evidence thật > logic nghiên cứu > giọng > linter.
2. Raw evidence/local ground truth > manifest/summary > screenshot > báo cáo thực nghiệm cũ.
3. Không viết chương dài nếu chưa khóa chapter contract và evidence map của chương đó.
4. Không biến UNKNOWN/negative result thành failure của đồ án; phải phân tích giới hạn đo.
5. Phân biệt ba lớp phòng thủ:
   - patching;
   - protocol hardening;
   - network access control.
6. Mỗi kết quả Chương 3 phải có provenance.
7. Hình trong thân bài chỉ giữ hình phục vụ luận điểm; troubleshooting/ảnh lặp chuyển phụ lục.
8. DOCX chỉ xuất sau G5 synthesis.
9. Tạo thêm cổng dự án `G7_DEFENSE` sau G6 để chuẩn bị slide, Q&A, demo và phục hồi.

---

# PHASE M0 — GOVERNANCE & REQUIREMENT RECONCILIATION

## Mục tiêu
Khóa “đồ án đang phải chứng minh điều gì” trước khi viết Chương 2–4.

## Công việc
- Đối chiếu:
  - `ATTT_DACN_01_DeCuongChiTiet.docx`;
  - `INSTITUTION_PROFILE.md`;
  - `PROJECT_PROFILE.md`;
  - `RESEARCH_MAP.md`;
  - `PROJECT_STATE.md`;
  - `EXPERIMENTAL_TRUTH_MATRIX.md`.
- Ghi rõ các drift:
  - chỉ thị cũ “tránh demo” đã lỗi thời;
  - Windows 7 / 3 VLAN / Client đối chứng là thiết kế lịch sử, không phải canonical;
  - Case C cũ Windows Firewall không phải canonical;
  - Case A patch chưa có evidence canonical;
  - Metasploit có trong đề cương/công cụ nghiên cứu nhưng không phải kết quả canonical hiện tại.
- Chuẩn hóa thời gian dự án: giữ ngày 24/08/2026–18/10/2026; ghi conflict nếu tài liệu gọi đây là “10 tuần” trong khi thông báo HUIT hiện hành gọi là 08 tuần.

## Exit criteria
- Không còn yêu cầu phạm vi stale trong artifact điều phối.
- RQ/O/method không đòi một kết quả mà evidence hiện tại không thể trả lời.
- Mọi conflict được ghi, không xóa lịch sử.

## Artifact
- `REQUIREMENT_RECONCILIATION.md`
- đề xuất patch cho `PROJECT_PROFILE.md`, `RESEARCH_MAP.md` (chưa áp nếu LOCKED).

---

# PHASE M1 — CANONICAL EVIDENCE CONTROL

## Mục tiêu
Biến khối demo lớn thành evidence set có thể audit.

## Công việc
- Dùng `EXPERIMENTAL_TRUTH_MATRIX.md` làm nền.
- Tạo inventory toàn bộ evidence canonical:
  - Environment/Baseline;
  - Scenario 1;
  - Scenario 2;
  - Case B;
  - Case C.
- Mỗi artifact có:
  - ID;
  - path;
  - loại;
  - timestamp nếu có;
  - scenario/step;
  - claim được hỗ trợ;
  - claim không được phép suy ra.
- Tạo SHA-256 manifest cho **canonical evidence set** nếu có thể, để dùng đúng nghĩa “integrity check”.
- Phân loại:
  - CANONICAL;
  - SUPPORTING;
  - TROUBLESHOOTING;
  - HISTORICAL;
  - EXCLUDED.
- Kiểm tra raw `.nmap/.xml/.gnmap` khớp screenshot/summary.
- Xác nhận không có credential/secret trong artifact dùng công khai.

## Exit criteria
- 100% claim thực nghiệm dự kiến trong Chương 3 có ít nhất một evidence ID.
- Raw/summary conflict = 0 unresolved.
- Evidence canonical và troubleshooting không trộn lẫn.

## Artifact
- `EVIDENCE_REGISTER.md`
- `CANONICAL_EVIDENCE_SHA256.txt`
- `EVIDENCE_CONFLICT_REPORT.md`

---

# PHASE M2 — RESEARCH/ARGUMENT REALIGNMENT

## Mục tiêu
Khớp câu hỏi nghiên cứu và lập luận với kết quả demo thật.

## Công việc
- RQ1/RQ2: lý thuyết SMB/MS17-010.
- RQ3: lab + quy trình phát hiện/xác minh có kiểm soát.
- RQ4: đánh giá các lớp giảm thiểu.
- Không dùng từ “triệt tiêu nguy cơ” nếu evidence chỉ chứng minh giảm exposure trong phạm vi cụ thể.
- Khóa các kết luận trung tâm:
  1. OPEN != SMBv1 enabled.
  2. SMBv1 enabled != remote vulnerability verdict.
  3. UNKNOWN != safe/patched.
  4. Local patch baseline có thể xác định host UNPATCHED độc lập với remote scanner.
  5. Disable SMBv1 thay protocol surface, không patch driver.
  6. pfSense thay reachability từ nguồn thử, không thay local patch/protocol state.
- Case A: proposal/reference unless evidence được audit.

## Exit criteria
- Mỗi RQ có phương pháp + evidence/nguồn khả thi.
- Không có mục tiêu yêu cầu exploit success nếu exploit không thuộc canonical run.
- Claim Matrix phân biệt `AUTHOR_DATA`, `SOURCE_FACT`, `INTERPRETATION`, `PROPOSAL`.

## Artifact
- `ARGUMENT_MAP_2_4_PROPOSED.md`
- `CLAIM_MATRIX_2_4.md`

---

# PHASE M3 — OUTLINE + CHAPTER CONTRACTS + EVIDENCE MAP

## Mục tiêu
Khóa cấu trúc trước prose.

## Chương 2 — Thiết kế và xây dựng mô hình thực nghiệm
Câu hỏi: lab và phương pháp đo được thiết kế như thế nào để kết quả có thể truy vết và phục hồi?

Phải có:
- VirtualBox/Kali/Windows Server 2012 R2;
- Host-Only baseline;
- IP/cấu hình;
- SMB/Firewall prep;
- patch baseline;
- tools/NSE;
- snapshot;
- thiết kế Scenario 1;
- thiết kế Scenario 2;
- thiết kế retest Case B/C;
- quy tắc thu bằng chứng.

Không biến Chương 2 thành nhật ký cài đặt.

## Chương 3 — Thực nghiệm và kết quả
Câu hỏi: các phép đo thực tế cho thấy gì?

Phải có:
- pre-test verification;
- Scenario 1;
- Scenario 2;
- Case B;
- Case C;
- bảng tổng hợp canonical.

Mỗi unit:
`objective -> command/method -> raw evidence -> observation -> classification -> inference boundary`.

## Chương 4 — Đánh giá và khuyến nghị
Câu hỏi: các kết quả có ý nghĩa gì với rủi ro và phòng thủ SMB?

Phải có:
- cross-case comparison;
- remote vs local ground truth;
- negative/UNKNOWN result;
- defense-layer comparison;
- CIA/risk discussion;
- residual risk;
- limitations;
- patch recommendation;
- compatibility/operational impacts;
- future work.

## Exit criteria
- Mỗi heading có nhiệm vụ và kết luận dự kiến.
- Mỗi kết luận thực nghiệm có evidence ID.
- Không có heading chỉ để “giới thiệu công cụ”.
- Người dùng/reviewer duyệt.

## Artifact
- `OUTLINE_2_4_PROPOSED.md`
- `CHAPTERS_2_4_EVIDENCE_MAP.md`
- `CHAPTER_2_CONTRACT.md`
- `CHAPTER_3_CONTRACT.md`
- `CHAPTER_4_CONTRACT.md`

---

# PHASE M4 — WRITE & REVIEW CHAPTER 2

## Mục tiêu
Viết phương pháp/môi trường đủ tái lập, không lẫn kết quả.

## Review bắt buộc
- mọi version/IP/config fact có evidence;
- lý do chọn Host-Only;
- firewall prep giải thích đúng vai trò;
- patch baseline tách khỏi NSE verdict;
- snapshot/recovery có vai trò;
- pfSense chỉ xuất hiện đúng vai trò Case C;
- không chèn troubleshooting không phục vụ phương pháp.

## Gate
Mỗi mục trọng yếu >= 8/12 theo `reasoning-and-writing.md`; citation/data/logic pass; reviewer duyệt.

---

# PHASE M5 — WRITE & REVIEW CHAPTER 3

## Mục tiêu
Đây là chương có tải bằng chứng cao nhất và phải được ưu tiên QA.

## Công việc
- Scenario 1: B1–B7, nhưng chỉ chọn hình canonical cần thiết.
- Scenario 2: NSE-SMB-01..04.
- Baseline local patch ground truth.
- Case B differential test.
- Case C three-vantage-point test: Kali / pfSense / Windows.
- Summary matrix.

## Quy tắc
- `NSE-SMB-04 baseline = UNKNOWN`.
- Negative/empty output phải được ghi đúng như data.
- Không dùng report cũ để bổ sung output raw không tồn tại.
- Không dùng “100%”, “hoàn hảo”, “triệt để”.
- Không biến screenshot thành thay thế cho raw output.
- Không claim exploit/RCE nếu không thực hiện.

## Gate
- 100% result claims truy được tới evidence ID.
- Không conflict với Truth Matrix.
- Không còn `[CẦN DỮ LIỆU]` cho các case canonical đã hoàn tất.
- Các dữ liệu chưa có (Case A, performance, exploit) phải bị loại hoặc đánh nhãn.
- reviewer duyệt.

---

# PHASE M6 — WRITE & REVIEW CHAPTER 4

## Mục tiêu
Biến demo thành tri thức/đánh giá, tránh chỉ kể lại kết quả.

## Phân tích bắt buộc
1. Tại sao port open không đủ.
2. Tại sao SMBv1 không đủ để verdict MS17-010.
3. Giá trị của local patch ground truth khi NSE UNKNOWN.
4. Case B thay đổi điều kiện nào.
5. Case C thay đổi điều kiện nào.
6. Defense-in-depth nhưng không tuyên bố tuyệt đối.
7. Residual risk.
8. Limitations/validity threats:
   - một Windows target;
   - virtual lab;
   - một nguồn kiểm thử;
   - không exploit;
   - remote script UNKNOWN;
   - không Case A canonical;
   - không benchmark performance.

## Gate
- Chương 4 không đưa evidence mới chưa xuất hiện ở Chương 3/nguồn.
- Mọi recommendation có source hoặc được đánh dấu proposal.
- RQ4 được trả lời trong đúng phạm vi.
- reviewer duyệt.

---

# PHASE M7 — G5 SYNTHESIS

## Mục tiêu
Khóa logic toàn báo cáo.

## Checklist
- RQ1–RQ4 -> answer matrix.
- O1–O4 -> evidence/deliverable matrix.
- Thuật ngữ, IP, version, snapshot, case naming thống nhất.
- IEEE toàn cục, không đánh số riêng từng chương trong bản cuối.
- Không lặp Chương 1 sang Chương 2/4.
- Intro và Conclusion khớp kết quả thật.
- Kết luận không biến UNKNOWN thành positive/negative verdict.
- Appendix plan.

## Artifact
- `SYNTHESIS_REVIEW.md`
- Markdown full report.

---

# PHASE M8 — G6 PUBLICATION

Giữ quy trình hiện tại của repo:
- publication lint;
- tạo DOCX từ Markdown locked;
- TOC/list of figures/list of tables;
- HUIT formatting;
- render mọi trang;
- page-by-page QA;
- sửa và render lại.

Không bắt đầu trước M7 PASS.

---

# PHASE M9 — G7 DEFENSE PACKAGE (BỔ SUNG CHO ĐỒ ÁN)

## Lý do
Đề cương chấm riêng phong cách báo cáo/slide và yêu cầu nhóm bảo vệ phương pháp, kết quả, giới hạn.

## Deliverables
- slide 12–18 phút hoặc theo GVHD;
- 1 sơ đồ topology chính;
- 1 slide research logic;
- 1 slide Scenario 1;
- 1 slide Scenario 2;
- 1 slide Case B;
- 1 slide Case C;
- 1 slide comparison;
- 1 slide limitations;
- 1 slide recommendation/conclusion;
- Q&A bank tối thiểu 25 câu;
- demo runbook;
- rollback plan/snapshot;
- evidence quick-index để trả phản biện.

## Gate
- mọi slide claim khớp report;
- demo rehearsal từ snapshot đạt;
- không cần Internet thật;
- có phương án nếu NSE04 tiếp tục UNKNOWN;
- mỗi thành viên biết phần mình và phần lõi chung.

---

# 3. Phân bổ ưu tiên theo rubric đề cương

Ưu tiên cao nhất:
1. CLO3 — triển khai/kịch bản/lab/scan/xác minh/phòng thủ/retest/evidence: 4.5 điểm.
2. CLO4 — đánh giá trước–sau và residual risk: 0.5 điểm.
3. CLO2.1 + CLO2.2 — công nghệ/mô hình/vai trò thành phần: 1.25 điểm.
4. CLO1.1 + CLO1.2 — phân tích/lý thuyết: 1.5 điểm.
5. Báo cáo + hình thức: 1.0 điểm.
6. Thái độ + slide: 1.0 điểm.
7. Kế hoạch/phân công: 0.25 điểm.

Do đó roadmap phải dành phần lớn QA cho M1/M3/M5/M6/M9, không phải chỉ cho Chapter 1 và DOCX.

---

# 4. Điểm cần sửa ngay trong repo nếu proposal được duyệt

1. `ROADMAP_2_6.md`: giữ nguyên lịch sử nhưng đổi mô tả thành sub-roadmap “writing/recovery”.
2. `PROJECT_PROFILE.md`: bỏ chỉ thị stale “tránh demo”; VirtualBox là canonical platform hiện tại; Metasploit không được mô tả như kết quả nếu không dùng.
3. `RESEARCH_MAP.md`: cập nhật phương pháp M3/M4 từ “tránh demo” sang evidence canonical; thu hẹp từ ngữ “triệt tiêu”.
4. `OUTLINE.md`: thay outline stale bằng outline đã duyệt theo Chương 2–4.
5. `CHAPTER_ARGUMENT.md`: archive contract Windows 7/3 VLAN; tạo contract canonical mới.
6. `PROJECT_STATE.md`: ghi master roadmap active sau duyệt.
7. Giữ `EXPERIMENTAL_TRUTH_MATRIX.md` làm canonical truth gate.

# 5. Quyết định đề xuất

**Không tiếp tục từ bước 5 của ROADMAP_2_6 như thể đó là bước tiếp theo duy nhất.**

Trình tự nên là:
`M0 -> M1 -> M2 -> M3 -> M4 -> M5 -> M6 -> M7 -> M8 -> M9`.

Hiện trạng thực tế:
- Truth Matrix: đã có, tương đương một phần M1.
- Chương 1/source/voice: có nền tảng tốt.
- Demo canonical: đã có khối evidence lớn nhưng chưa được quản trị đầy đủ thành Evidence Register.
- Outline/Chapter contracts: cần làm lại trước prose.
- DOCX: chưa nên ưu tiên.
