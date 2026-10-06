# X7 — DRAFT CHAPTER 3 WITH EMBEDDED EVIDENCE

Status: READY_FOR_EXECUTOR
Branch: feature/x7-chapter-3-draft

## 0. Objective

Write the first complete review draft of Chapter 3 as a student graduation-project results chapter.

Embed selected real evidence images directly in the Markdown draft.

This is NOT the final DOCX.
Do NOT write Chapter 4.

## 1. Start

Run:
git fetch origin
git checkout feature/x7-chapter-3-draft
git pull --ff-only origin feature/x7-chapter-3-draft
git status --short
git rev-parse HEAD

## 2. Mandatory read order

Read:
1. origin/main:work/do-an/CHAPTER_3_AUTHORING_CONSTRAINTS.md
2. work/do-an/chapter3/CHAPTER_3_RESULT_MATRIX.md
3. work/do-an/chapter3/CHAPTER_3_EVIDENCE_INDEX.md
4. work/do-an/chapter3/CHAPTER_3_FIGURE_PLAN.md
5. work/do-an/chapter3/CHAPTER_3_EVIDENCE_SHA256.csv
6. origin/main:work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md
7. origin/main:work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md
8. origin/main:work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md
9. origin/main:work/do-an/SOURCE_LEDGER.md
10. origin/main:work/do-an/AUTHOR_VOICE.md
11. origin/main:work/do-an/CHAPTER_2.md

## 3. Output files

Create only:
- work/do-an/CHAPTER_3_DRAFT_R1.md
- work/do-an/CHAPTER_3_DRAFT_R1_SELF_REVIEW.md

Do not create final DOCX.
Do not create Chapter 4.
Do not alter evidence files.

## 4. Structure

Use exactly the 7 H2 / 16 H3 structure in CHAPTER_3_AUTHORING_CONSTRAINTS.md.

Do not add or remove numbered headings.

## 5. Opening

Use one short opening paragraph.

State:
- Chapter 3 presents measured results from Chapter 2 scenarios;
- tables and selected evidence images are used;
- broader risk/recommendation discussion is reserved for Chapter 4.

Do not explain repository/evidence governance.

## 6. Section 3.1

Create Bảng 3.1 containing:
- Kali IP;
- Windows IP;
- Host-Only / no default route state;
- LanmanServer;
- local TCP 139/445 listening;
- SMB1/SMB2 state;
- Windows Firewall scope;
- numeric srv.sys;
- MS17-010 patch classification;
- Before Demo snapshot.

Embed exactly:
![Hình 3.1. Phiên bản hiển thị của tệp srv.sys trên máy Windows Server 2012 R2 trước thực nghiệm](chapter3/evidence/baseline/Windows_MS17010_01_SrvSysVersion.png)

Before image: introduce what is visible.
After image:
- screenshot shows display FileVersion String only;
- UNPATCHED requires numeric local version + observed hotfix inventory + official Microsoft mapping.

Do not say the lab is completely isolated.

## 7. Section 3.2

Create Bảng 3.2 summarizing B2–B6.

Include:
- .56.100 = UNKNOWN identity;
- 139/445 OPEN;
- B5 fingerprint range;
- dialect list;
- signing enabled but not required;
- capabilities;
- smb-os-discovery no usable output.

Embed exactly:
![Hình 3.2. Kết quả NSE trong Kịch bản 1 ghi nhận các dialect SMB và chính sách ký số từ xa](chapter3/evidence/scenario1/Scenario1_B6_SMB_NSE_A.png)

Do not repeat command blocks.
Do not claim B5 fingerprint alone proves Windows Server 2012 R2.

## 8. Section 3.3

Create Bảng 3.3 covering NSE-SMB-01 through NSE-SMB-04.

Key result:
NSE-SMB-04 = UNKNOWN / NO USABLE SCRIPT RESULT.

Embed exactly:
![Hình 3.3. Kết quả kiểm tra smb-vuln-ms17-010 không trả về phán quyết lỗ hổng có thể sử dụng](chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png)

After figure:
- 445 is open;
- no Host script result / vulnerability verdict;
- remote classification UNKNOWN;
- local patch state independently UNPATCHED.

Do not call it a false negative.
Do not invent a cause.

## 9. Section 3.4

Create Bảng 3.4 as before/after comparison.

Show:
- SMB1 True -> False locally;
- SMB2 remains True;
- LanmanServer remains Running;
- 445 remains open remotely;
- SMBv1 dialect disappears;
- SMB2/3 dialects remain observable;
- MS17-010 remote result remains UNKNOWN;
- patch state remains UNPATCHED.

Embed exactly:
![Hình 3.4. Trạng thái cấu hình SMB trên Windows Server sau khi vô hiệu hóa SMBv1](chapter3/evidence/case_b/SMBv1_Remediation_03_After_Local.png)

![Hình 3.5. Kết quả kiểm tra lại smb-protocols sau Case B cho thấy SMBv1 không còn xuất hiện trong danh sách dialect](chapter3/evidence/case_b/SMBv1_Remediation_04_NSE02_Protocols.png)

Do not claim SMB2/3 workload was tested.
Do not claim patched or safe.

## 10. Section 3.5

Create Bảng 3.5 separating:
- rule/order configuration;
- Nmap port result;
- pfSense log observation;
- MS17-010 remote result;
- local Windows state.

Embed exactly:
![Hình 3.6. Thứ tự quy tắc trên giao diện CASE_C_KALI đặt quy tắc chặn SMB trước quy tắc cho phép](chapter3/evidence/case_c/pfSense_08_Rule_Order.png)

![Hình 3.7. Kết quả quét lại TCP 139 và 445 qua đường dẫn Case C ghi nhận trạng thái filtered](chapter3/evidence/case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png)

![Hình 3.8. Nhật ký pfSense ghi nhận các gói TCP SYN SMB tương ứng với hành động Block](chapter3/evidence/case_c/pfSense_10_Block_Log_CANONICAL.png)

Writing order:
1. Nmap reports filtered/no-response.
2. Raw Nmap alone does not establish cause.
3. Separate pfSense log shows matching .56.10 -> .56.20:139/445 TCP SYN traffic with Block action.
4. Exact named-rule attribution remains unresolved.
5. Remote MS17-010 result is UNKNOWN/inaccessible.
6. Local Windows patch state remains UNPATCHED.

Never write that pfSense made the machine safe.

## 11. Section 3.6

Create Bảng 3.6 comparing only measured dimensions:
- TCP 139/445 remote state;
- SMBv1 observable/absent/inaccessible;
- SMB2/3 observable/inaccessible;
- remote MS17-010 signal;
- local SMB1 state where measured;
- local patch state;
- direct network-control observation.

Do not add risk scores, effectiveness ranking, best solution, CIA impact or cost-benefit.

After table: at most two compact paragraphs describing measured differences.

## 12. Section 3.7

2–3 paragraphs maximum.

Summarize empirical findings only:
- baseline exposed SMB 139/445 and supported SMBv1;
- remote MS17-010 script did not return a usable verdict;
- local patch state was UNPATCHED;
- Case B removed SMBv1 from negotiation but did not patch the system;
- Case C changed remote port visibility/access and pfSense logs showed matching SMB SYN Block events;
- broader evaluation moves to Chapter 4.

No recommendations.

## 13. Tables

Exactly 6 tables.
Table title above.
Introduce each table before it appears.
No internal evidence IDs in visible tables.
No raw-log dumps.

## 14. Images

Exactly 8 image embeds listed above.
Use original staged paths.
Do not edit/crop/recolor/annotate source evidence in Draft R1.
Do not add screenshot borders/decorative frames.
Do not show hashes/internal IDs in captions.

## 15. Source and citation rules

Raw experimental observations are project results.

External claims use only VERIFIED entries in SOURCE_LEDGER.md.
Microsoft official source must support KB/version mapping.
Do not invent bibliography numbering.
Do not add standalone bibliography to Chapter 3 draft.

## 16. Style

Follow AUTHOR_VOICE.md.

Do not:
- use repetitive formulaic paragraphs;
- use corporate audit language;
- self-praise;
- invent student experience;
- expose canonical/gate/truth-matrix language;
- use AI-detector language.

## 17. Forbidden meanings

Remove any statement equivalent to:
- machine safe;
- remote NSE confirms MS17-010;
- no MS17-010;
- false negative;
- vulnerability still exists as a remotely proven fact;
- all attack surface removed;
- complete isolation;
- SMB2/3 workload works normally;
- exact pfSense named rule matched the log.

## 18. Self-review

Create CHAPTER_3_DRAFT_R1_SELF_REVIEW.md with:
1. heading count;
2. word count;
3. table count;
4. image count;
5. result-to-evidence map by section;
6. negative-result audit;
7. Chapter 3/4 boundary audit;
8. Case C conflict audit;
9. .56.100 identity audit;
10. citation/source audit;
11. author-voice audit;
12. unresolved concerns.

Do not self-declare PASS.

Final self-review status:
X7_CHAPTER_3_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW

## 19. QA

Run:
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_3_DRAFT_R1.md
uv run python scripts/audit_ieee_citations.py work/do-an/CHAPTER_3_DRAFT_R1.md
git diff --check

Also verify:
- 7 H2;
- 16 H3;
- 6 tables;
- 8 Markdown image embeds;
- all 8 image paths exist;
- no .56.100 identity assignment;
- no fabricated SAFE/NOT VULNERABLE/VULNERABLE;
- no internal Evidence IDs in prose;
- no L1-L5/five-layer report structure;
- no Chapter 4 recommendations.

## 20. Git

Commit message:
draft(ch3): write results chapter R1 with direct evidence

Push branch:
feature/x7-chapter-3-draft

Do not merge main.

## 21. Handoff

Return:
1. local SHA;
2. remote SHA;
3. word count;
4. 7 H2 / 16 H3;
5. 6-table audit;
6. 8-image audit;
7. image-path existence audit;
8. result-evidence section map;
9. negative-result audit;
10. Case B boundary audit;
11. Case C causality/conflict audit;
12. Chapter 3/4 boundary audit;
13. citation audit;
14. QA results;
15. clean status.

Final state:
X7_CHAPTER_3_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW

Stop.
Do not create final DOCX.
Do not write Chapter 4.
