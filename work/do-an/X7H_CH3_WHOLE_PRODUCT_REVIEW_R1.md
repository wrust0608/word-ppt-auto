# X7H WHOLE CHAPTER 3 — EXTERNAL PRODUCT REVIEW R1

Date: 2026-10-07  
Branch: `feature/x7h-ch3-whole-review`  
Source: `work/do-an/CHAPTER_3_COMPLETE_R1.md`  
X7G mechanical assembly: PASS

Verdict: **92/100 — REVISE_MINOR_BLOCKING**

## 1. Overall assessment

Chapter 3 is technically coherent and evidence-complete, but it is not yet ready for user approval as a finished thesis chapter.

No experiment must be rerun.
No technical section must be reopened.
No new evidence is needed.

The remaining work is whole-chapter editorial work:
- remove cross-section repetition created by independently approved sections;
- normalize a few phrases to the strictest evidence wording already locked later in the chapter;
- improve transitions;
- remove internal/QA-like wording from student-facing prose;
- normalize figure-caption presentation;
- finish with a cleaner chapter-level opening and ending.

The technical meaning, table numbering and figure allocation remain locked.

## 2. Global roadmap checkpoint

Current authoritative sequence remains:

`X7H whole-Chapter-3 review/edit -> user approval of complete Chapter 3 -> X7I Chapter 2+3 DOCX -> X7J final combined review -> STOP`

Still forbidden:
- Chapter 2 rewrite;
- Chapter 1 enrichment;
- Chapter 4 drafting;
- intermediate Word snapshots;
- new evidence;
- demo rerun;
- new figures/tables unless a factual blocker is discovered.

## 3. What already passes

### Technical progression — PASS
The chapter has the correct research flow:

`baseline -> Scenario 1 -> Scenario 2 -> Case B -> Case C -> comparison -> conclusion`

### Evidence coverage — PASS
- Bảng 3.1–3.7 retained;
- Hình 3.1–3.11 retained;
- all image paths resolve;
- no new Hình 3.12;
- no new Bảng 3.8.

### Technical locks — PASS
The complete chapter preserves:
- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `SMBv1 disabled != PATCHED`
- `FILTERED != PATCHED`
- `UNKNOWN != SAFE`

No canonical exploitation result, no SAFE verdict and no Chapter 4 recommendation appears.

### Section balance — generally PASS
The evidence-heavy Sections 3.1–3.5 are proportionate to their data.
Sections 3.6–3.7 are appropriately shorter.

## 4. Editorial blocker A — 3.2 and 3.3 repeat the same port/dialect/signing story too heavily

Sections 3.2 and 3.3 were approved independently, so when assembled they repeat:
- TCP 139/445 OPEN + SYN-ACK;
- the full five-dialect list;
- signing enabled but not required;
- the same boundaries around OPEN and SMBv1.

This weakens the chapter flow because 3.3 reads partly like a second version of 3.2.

### X7H action

Keep:
- Bảng 3.4 with NSE-SMB-01 to NSE-SMB-04;
- the direct technical facts;
- Hình 3.6;
- the transition to the MS17-specific result.

Compress the prose of 3.3.1:
- one short opening paragraph;
- one concise paragraph grouping NSE-SMB-01 to NSE-SMB-03 as confirmation of the conditions already observed in 3.2;
- rely on Bảng 3.4 for the detailed repeated values.

Do not delete the measurements.
Do not alter Bảng 3.4 facts.
Do not invent any new interpretation.

## 5. Editorial blocker B — UNKNOWN explanation is repeated too many times

`UNKNOWN / NO USABLE SCRIPT RESULT` is correctly handled, but the same methodological explanation is repeated in:
- Bảng 3.4;
- 3.3.2;
- Bảng 3.5 / 3.4.2;
- Bảng 3.6 / 3.5.2;
- 3.6;
- 3.7.

The reader only needs the full explanation once.

### X7H action

Keep the full methodological explanation in Section 3.3.2:
- UNKNOWN is the project classification;
- not literal Nmap output;
- no internal script cause is established;
- UNKNOWN != SAFE;
- local UNPATCHED and remote UNKNOWN are independent evidence layers.

Later sections should be shorter:
- Case B: state that the retest remains UNKNOWN / NO USABLE SCRIPT RESULT and refer to the boundary already established in 3.3.
- Case C: state the same classification and only preserve the Case-C-specific FILTERED observation.
- Section 3.6: compare the three UNKNOWN outcomes without re-explaining the full theory.
- Section 3.7: one concise mention only.

Do not weaken the boundary.
Do not assign a cause.

## 6. Editorial blocker C — duplicated transitions between adjacent sections

Current assembled chapter repeats the same transition twice at several boundaries:

### 3.3 -> 3.4
The end of 3.3 announces Case B, then the opening of 3.4 announces Case B again.

### 3.4 -> 3.5
The end of 3.4 announces Case C, then 3.5 introduces Case C again.

### 3.5 -> 3.6
The end of 3.5 announces the comparison, then 3.6 opens by announcing the comparison again.

### X7H action

At each boundary, retain only one natural transition.

Preferred:
- keep the next section opening strong;
- shorten the preceding section ending to its empirical conclusion.

Do not remove necessary result conclusions.

## 7. Editorial blocker D — terminology should follow the strictest evidence wording

Some early prose is looser than later locked wording.

Examples:
- `các phương ngữ được máy chủ chấp nhận`;
- `hệ thống chấp nhận phương ngữ SMBv1`;
- table wording `Phương ngữ hỗ trợ`.

For whole-chapter consistency, prefer:
- `các phương ngữ được ghi nhận`;
- `smb-protocols ghi nhận...`;
- `Phương ngữ ghi nhận`.

This is a narrowing/editorial normalization only.

Do not claim:
- successful SMB negotiation;
- full workload compatibility;
- application-level success.

Also replace:
- `workload` -> natural Vietnamese wording or remove the term;
- `point-in-time` -> `tại thời điểm kiểm tra`;
- `metadata` / `siêu dữ liệu tiến trình thực nghiệm` -> `bản ghi/trạng thái ghi nhận của lượt thực nghiệm`;
- `topology` in student prose -> `mô hình mạng` where natural;
- `đề án` -> `đề tài` for report voice consistency.

The locked classification string `UNKNOWN / NO USABLE SCRIPT RESULT` must remain unchanged.

## 8. Editorial blocker E — remove internal audit/report-management tone

Examples that sound like an internal QA record rather than a thesis:
- `siêu dữ liệu tiến trình thực nghiệm`;
- `metadata cuối Case C`;
- `đề tài bảo tồn nguyên vẹn sự không thống nhất này như một ranh giới khách quan của bộ bằng chứng thực nghiệm`;
- repeated phrases such as `đề tài xác lập ranh giới phương pháp luận`.

### X7H action

Keep provenance, but phrase it naturally.

Example:
Instead of:
`metadata cuối Case C ghi nhận...`

Use:
`trạng thái ghi nhận cuối lượt Case C cho thấy...`

For the pfSense rule-label discrepancy, keep the disclosure but shorten it:
`Nhãn quy tắc hiển thị trong nhật ký không trùng với tên quy tắc trong tệp ghi nhận lượt chạy; vì vậy Hình 3.11 chỉ được dùng để xác nhận hành động Block đối với lưu lượng tương ứng, không để quy thuộc tuyệt đối cho một tên quy tắc cụ thể.`

The exact labels may remain once if useful for transparency, but do not turn the main narrative into an evidence-audit discussion.

## 9. Editorial blocker F — several phrases can be technically narrowed without reopening facts

### Scenario 2 port wording
Avoid using the remote SYN-ACK result to imply a stronger local-state fact.

Prefer:
`NSE-SMB-01 tiếp tục ghi nhận TCP 139/445 OPEN và phản hồi SYN-ACK từ góc nhìn trạm Kali.`

rather than:
`xác nhận máy chủ đang lắng nghe...`

### Scenario 1 summary
Replace:
`hệ thống chấp nhận phương ngữ SMBv1...`

with:
`Nmap ghi nhận NT LM 0.12 (SMBv1) cùng các phương ngữ SMB2/3...`

### Case C
Prefer:
`trạng thái cổng quan sát từ xa`
over repeated `diện mạo dịch vụ` where that phrase sounds unnatural.

These are evidence-narrowing edits, not factual changes.

## 10. Editorial blocker G — repeated paragraph openings

The academic linter reports repeated openings based on `Sau khi xác...`.

This is visible after assembly because sections were authored independently.

Diversify openings naturally:
- `Từ mốc đường cơ sở ở Mục 3.1,...`
- `Kịch bản 2 tiếp tục...`
- `Ở Case B,...`
- `Đối với Case C,...`

Do not mechanically replace every `Sau khi`; edit only where the chapter rhythm improves.

## 11. Editorial blocker H — figure-caption presentation is inconsistent

Sections 3.1–3.3 put the complete caption inside Markdown image alt text.

Sections 3.4–3.5 use:
- short image alt text;
- separate italic caption line.

The complete chapter should use one consistent figure convention before DOCX assembly.

### X7H action

Normalize all 11 figures to:

`![Hình 3.x](relative/path.png)`

followed by:

`*Hình 3.x. <caption>*`

Keep:
- exact figure number;
- exact image path;
- approved caption meaning.

Do not rename or regenerate image files.

## 12. Editorial blocker I — chapter opening can be more coherent

The chapter currently starts directly at Section 3.1.

Add one short chapter-level introductory paragraph after the H1, with no new technical claims.

It should tell the reader that Chapter 3 presents:
- baseline;
- two measurement scenarios;
- Case B;
- Case C;
- final comparison/conclusion.

Target about 70–110 words.

Do not duplicate Chapter 2 methodology.

## 13. Editorial blocker J — Chapter 3 ending should stop cleanly

Current last sentence:
`...là cơ sở để tiếp tục đánh giá ở các phần sau khi phạm vi báo cáo được mở rộng.`

This is vague and sounds like an automatic opening of later work.

Prefer a clean stop:
`Các kết quả này khép lại phạm vi đo đạc thực nghiệm của Chương 3.`

or a similarly concise sentence.

Do not open Chapter 4.

## 14. Tables and figures — retain all approved allocations

Do not delete:
- Bảng 3.1–3.7;
- Hình 3.1–3.11.

Do not create:
- Bảng 3.8;
- Hình 3.12.

The purpose of X7H is compression of repetitive prose, not removal of approved evidence.

## 15. Compression target

Current chapter is evidence-complete but contains repetition created by section-by-section authoring.

Target:
- remove approximately 600–900 prose words if possible;
- most reduction should come from 3.3 repetition, repeated UNKNOWN explanation and duplicated transitions;
- do not cut unique evidence facts;
- do not shorten tables by removing locked rows;
- do not reduce figure count.

This is a quality target, not a quota.

## 16. Technical reopen rule

Editorial changes above are authorized because they do not change experimental meaning.

STOP and report instead of editing if a proposed change would alter:
- a measured value;
- an IP/port;
- an image/table allocation;
- a patch classification;
- an MS17 classification;
- a before/after state;
- the pfSense rule-label conflict;
- a provenance claim.

Such a change would require explicit technical reopen.

## 17. X7H deliverable expectation

The next draft should read as one thesis chapter, not six independently reviewed artifacts concatenated together.

Success criteria:
- natural progression;
- less repetition;
- every figure/table earns its place;
- technical boundaries preserved;
- student-facing Vietnamese;
- no QA/governance tone;
- no Chapter 4 leakage;
- no DOCX yet.

Current gate:

`X7H_CH3_WHOLE_REVIEW_R1_REVISE_MINOR_BLOCKING`
