# X6 R2 — REGENERATE CHAPTER 2 DOCX AND CORRECT CHAPTER 3 PREP

Status: `READY_FOR_EXECUTOR`
Branch: `feature/x6-ch3-evidence-prep`

## 0. Scope

This is a corrective pass only.

Do:
1. regenerate the Chapter 2 final DOCX from the locked approved Chapter 2;
2. regenerate its QA report from the actual rendered pages;
3. correct the Chapter 3 evidence index/result matrix/figure plan/structure proposal.

Do not:
- change `work/do-an/CHAPTER_2.md`;
- change staged evidence bytes;
- alter SHA CSV rows unless a bookkeeping label/count is wrong;
- add new experiments;
- draft Chapter 3 prose;
- merge main.

Read first:
`origin/main:work/do-an/X6_EVIDENCE_PREP_EXTERNAL_REVIEW_R1.md`.

## 1. Checkout and verify starting state

```bash
git fetch origin
git checkout feature/x6-ch3-evidence-prep
git pull --ff-only origin feature/x6-ch3-evidence-prep
git status --short
git rev-parse HEAD
```

Starting candidate:
`bdaafd77ff3e03b573a852809025559159096529`

## 2. Regenerate Chapter 2 DOCX from the locked Markdown

Source of truth:
`origin/main:work/do-an/CHAPTER_2.md`

Do not use:
- legacy Chapter 2 drafts;
- previous DOCX builder content hardcoded from old structures;
- old QA page descriptions;
- “five-layer evidence” versions of Chapter 2.

Create/replace:
`work/do-an/output/CHAPTER_2_FINAL.docx`

The generated document must contain exactly this heading sequence:

```text
CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM

2.1. Phạm vi và mô hình thực nghiệm
2.1.1. Mục tiêu và phạm vi thực nghiệm
2.1.2. Mô hình mạng ở trạng thái baseline
2.1.3. Thành phần và thông số môi trường

2.2. Chuẩn bị và xác nhận trạng thái ban đầu
2.2.1. Cấu hình mạng và hai máy ảo
2.2.2. Chuẩn bị Kali Linux và công cụ Nmap/NSE
2.2.3. Chuẩn bị Windows Server, SMB và Windows Firewall
2.2.4. Xác định trạng thái bản vá MS17-010
2.2.5. Snapshot và kiểm tra trước thực nghiệm

2.3. Kịch bản 1 — Khảo sát dịch vụ SMB bằng Nmap
2.3.1. Mục tiêu và dữ liệu cần quan sát
2.3.2. Quy trình quét và các lệnh thực hiện
2.3.3. Giới hạn kết luận của Kịch bản 1

2.4. Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE
2.4.1. Mục tiêu và điều kiện thực hiện
2.4.2. Bốn phép đo NSE-SMB-01 đến NSE-SMB-04
2.4.3. Đối chiếu kết quả từ xa với trạng thái bản vá nội bộ

2.5. Kiểm thử hai biện pháp giảm thiểu đã thực hiện
2.5.1. Nguyên tắc đối chiếu trước và sau can thiệp
2.5.2. Vô hiệu hóa SMBv1 trên Windows Server
2.5.3. Kiểm soát SMB bằng pfSense Transparent Bridge

2.6. Dữ liệu thực nghiệm và nguyên tắc sử dụng
2.6.1. Dữ liệu được thu thập và lưu trữ
2.6.2. Phạm vi dữ liệu dùng cho đánh giá
2.6.3. Nguyên tắc diễn giải kết quả

2.7. Tổng kết chương
```

Use the current committed:
- `work/do-an/output/figures/hinh_2_1.png` for baseline topology;
- `work/do-an/output/figures/hinh_2_2.png` for pfSense topology.

These two images were independently reviewed and are aligned with the locked chapter.

## 3. DOCX formatting

Keep the approved formatting requirements:
- A4 portrait;
- one-sided;
- top 3.5 cm;
- bottom 3.0 cm;
- left 3.5 cm;
- right 2.0 cm;
- Times New Roman 13 pt body;
- 1.5 line spacing;
- justified body;
- proper Heading styles;
- table title above;
- figure caption below;
- command blocks monospace;
- no raw Mermaid.

Do not optimize layout by changing the approved Chapter 2 wording.

## 4. Automated DOCX content-drift gate

After building DOCX, create a machine-readable text/heading audit.

At minimum verify:
- title exact match;
- H2 count = 7;
- H3 count = 20;
- heading text and order exact match;
- tables = Bảng 2.1, 2.2, 2.3, 2.4 from the locked Markdown;
- figures = Hình 2.1 baseline topology, Hình 2.2 pfSense topology;
- exact Scenario 1 commands present;
- exact Scenario 2 operator commands present;
- exact Case B command/retests present.

Fail the build if any legacy phrase is found:
- `PHƯƠNG PHÁP THU THẬP BẰNG CHỨNG`
- `mô hình phân loại bằng chứng năm lớp`
- `Mô hình ánh xạ mục tiêu nghiên cứu`
- `Trạng thái kiểm toán tiền thực nghiệm`
- `Cây quyết định phân loại trạng thái kiểm định lỗ hổng`
- old Chapter 2 section names inconsistent with the locked list.

Record this audit in:
`work/do-an/output/CHAPTER_2_FINAL_DOCX_QA.md`

## 5. Fresh visual QA only

Delete/replace the stale QA narrative.

Render the new DOCX again.

Inspect every rendered page.

The QA report must describe the actual page contents that exist in this new DOCX.

Do not copy page descriptions from any earlier DOCX.

Report:
- actual page count;
- each page checked;
- no clipping;
- no table overflow;
- figures readable;
- no blank page;
- headings correct;
- exact chapter title correct;
- content-drift gate PASS;
- DOCX SHA-256.

## 6. Correct Chapter 3 MS17-010 mapping

The staged source artifact records the locked Windows Server 2012 R2 mapping:

- KB4012213 — Security Only;
- KB4012216 — Monthly Rollup;
- minimum updated srv.sys = `6.3.9600.18604`.

Correct every erroneous Chapter 3 prep reference to:
- KB4012213;
- KB4012216.

Remove all report-prep references that incorrectly use:
- KB4012212;
- KB4012215.

Keep:
- FileVersion String = `6.3.9600.16384`;
- numeric version = `6.3.9600.16421`;
- numeric local version is the value compared with Microsoft minimum.

Do not state that the screenshot alone proves UNPATCHED.
The UNPATCHED classification is based on local numeric version + observed hotfix inventory + official Microsoft mapping.

## 7. Correct Scenario 1 host identity

In all Chapter 3 prep:
- .56.1 = VirtualBox Host-Only host adapter where identity is supported;
- .56.10 = Kali;
- .56.20 = Windows target;
- .56.100 = **UNKNOWN identity**.

Remove:
- DHCP;
- DHCP daemon;
- Gateway;
- any specific identity for .56.100.

## 8. Correct SMB signing interpretation

Allowed:
`Message signing enabled but not required`

Interpret only as:
- remote Nmap observation of SMB signing policy.

Do not say:
- it is a prerequisite for MS17-010;
- it proves unsigned exploit payload acceptance;
- it “satisfies” an exploitation condition.

Keep local PowerShell signing properties separate.

## 9. Correct Case B interpretation

Allowed:
- before: SMB1=True;
- action: `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`;
- after: SMB1=False, SMB2=True, LanmanServer Running;
- remote retest: SMBv1 dialect absent, SMB2/3 dialects remain observable;
- remote MS17-010 retest = UNKNOWN / NO USABLE SCRIPT RESULT;
- local patch state remains UNPATCHED.

Do not say:
- file-sharing workloads were verified normal;
- modern SMB service was fully validated;
- no disruption was proven.

For the action screenshot:
prefer “the command was executed; the after-state confirms the intended configuration change”
rather than relying on absence of an error message alone.

## 10. Correct Case C result logic

### CC port-scan row
Direct raw fact only:
- 139/tcp filtered, no-response;
- 445/tcp filtered, no-response.

Allowed interpretation from this row:
- from the Kali vantage point through the Case C path, Nmap does not receive enough response to classify 139/445 as open or closed.

Do not assign firewall causality in the raw-scan row.

### CC firewall-log row
Direct log fact:
- Block action visible;
- CASE_C_KALI;
- .56.10 -> .56.20:139/445;
- TCP SYN.

Allowed:
- matching SMB SYN traffic was blocked in the pfSense path.

Preserve:
- exact rule-label conflict;
- no named-rule attribution.

### Combined Case C interpretation
Allowed:
- Nmap reports 139/445 filtered/no-response;
- separate pfSense logs show corresponding matching SMB SYN traffic being blocked;
- 445 is inaccessible for the MS17-010 probe from that vantage point;
- remote MS17-010 verdict remains UNKNOWN/inaccessible;
- Windows local state remains SMB1=True, SMB2=True, ports locally listening, patch UNPATCHED.

Forbidden:
- “all attack surface completely eliminated”;
- “L1/L2 attack surface completely isolated”;
- “script completely disabled”;
- “server remains vulnerable”;
- “internal vulnerability remains intact”;
- “firewall removed the vulnerability”;
- SAFE / NOT VULNERABLE.

## 11. Correct Figure Plan

### Figure for srv.sys
Caption should describe the observed displayed version only.

Example:
`Hình 3.1. Phiên bản hiển thị của tệp srv.sys trên máy Windows Server 2012 R2 trước thực nghiệm`

The UNPATCHED conclusion must be made in accompanying table/text with official mapping.

### Case B figure
Do not claim “no disruption” to SMB2/3 workloads.

Use:
- command action;
- local SMB1=False;
- remote dialect retest.

### Case C port figure
Caption:
- observed ports filtered/no-response.

Do not say the screenshot alone proves firewall blocking.

### Case C log figure
May state:
- matching TCP SYN traffic is shown as Block in pfSense log.

Add the bounded conflict note:
- do not attribute exact named rule.

### Case C comparison table
Use raw Nmap + direct pfSense log/config + local state as primary support.

`RUN4_PAUSE_STATE_REPORT.txt` is secondary lineage metadata only.

## 12. Correct Evidence Index and Result Matrix language

Remove/report-fix phrases such as:
- “satisfies payload precondition”;
- “workloads normal”;
- “attack surface completely isolated”;
- “vulnerability still exists”;
- “internal vulnerability intact”;
- “script completely disabled”.

Use only bounded observations.

## 13. Correct Chapter 3 structure proposal

Keep exactly 7 H2:

```text
CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH

3.1. Trạng thái baseline trước đo đạc
3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB
3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010
3.4. Kết quả Case B — Vô hiệu hóa SMBv1
3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense
3.6. So sánh kết quả thực nghiệm
3.7. Tổng kết chương
```

Remove from the proposed public report architecture:
- L1/L2/L3/L4/L5;
- five-layer evidence model;
- canonical/gate/governance vocabulary.

Internal evidence index may keep evidence-strength labels.

Report logic:
- measured result;
- supporting evidence;
- bounded direct interpretation;
- before/after comparison.

Chapter 4 owns:
- CIA impact;
- broad risk assessment;
- mitigation recommendations;
- residual risk;
- patch-management strategy.

## 14. Correct evidence count wording

Do not call all 83 staged files “primary evidence”.

Use:
- total staged = 83;
- primary/direct = 78;
- secondary metadata/closure = 5;
- SHA mismatch = 0.

Do not change byte-identical evidence files just to alter classification text.

## 15. Files allowed to change

Allowed:
- `work/do-an/output/CHAPTER_2_FINAL.docx`
- `work/do-an/output/CHAPTER_2_FINAL_DOCX_QA.md`
- `work/do-an/chapter3/CHAPTER_3_EVIDENCE_INDEX.md`
- `work/do-an/chapter3/CHAPTER_3_RESULT_MATRIX.md`
- `work/do-an/chapter3/CHAPTER_3_FIGURE_PLAN.md`
- `work/do-an/chapter3/CHAPTER_3_STRUCTURE_PROPOSAL.md`
- `work/do-an/chapter3/CHAPTER_3_EVIDENCE_SHA256.csv` only if correcting role labels/bookkeeping without changing source/staged hashes.

Do not change:
- `work/do-an/CHAPTER_2.md`;
- staged evidence bytes under `chapter3/evidence/**`;
- evidence R3 locks;
- Truth Matrix;
- Chapter 4.

Do not create `CHAPTER_3.md`.

## 16. QA

Run:
```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

Also run search gates:
- `KB4012212` -> 0 in chapter3 prep;
- `KB4012215` -> 0 in chapter3 prep;
- `.56.100.*DHCP` -> 0;
- `five-layer` / `năm lớp` in structure proposal -> 0;
- `L1/L2`, `L3`, `L4/L5` in structure proposal -> 0;
- `vẫn tồn tại lỗ hổng` -> 0;
- `lỗ hổng nội tại.*nguyên vẹn` -> 0;
- `bị cô lập hoàn toàn` -> 0;
- `bị vô hiệu hóa hoàn toàn` -> 0.

DOCX content-drift gate must PASS.

## 17. Git

Commit:
`fix(x6): regenerate ch2 docx and correct ch3 evidence logic`

Push:
`feature/x6-ch3-evidence-prep`

Do not merge.

## 18. Handoff

Return:
1. local SHA;
2. remote SHA;
3. DOCX path;
4. DOCX SHA-256;
5. actual page count;
6. exact heading-sequence audit;
7. legacy-phrase gate result;
8. visual QA all-pages result;
9. staged file counts by evidence role;
10. SHA mismatch count;
11. KB mapping gate;
12. .56.100 identity gate;
13. SMB signing boundary gate;
14. Case B wording gate;
15. Case C causality/vulnerability gate;
16. structure-proposal jargon gate;
17. project QA;
18. clean status.

Final state:
`X6_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Stop.

Do not write Chapter 3 prose.
