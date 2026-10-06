# WR1 DEMO 1 WORD EXTERNAL REVIEW R1 — FINAL

Date: 2026-10-06  
Branch: `feature/wr1-demo1-word-review-v2`  
Executor candidate: `e6f11eeb7285af9cf57db220b85d71e9ab2e64d8`  
Review artifact: `work/do-an/output/review/DEMO_1_CH2_CH3_31_32_REVIEW.docx`

Verdict: **99/100 — PASS / WAITING_FOR_USER_APPROVAL**

## 1. Executive finding

WR1 is acceptable as the Demo 1 Word review snapshot.

The actual DOCX was independently inspected at OOXML level rather than accepting the executor QA narrative at face value.

The Word file itself is structurally correct and preserves the approved report scope:
- full Chapter 2;
- Chapter 3 title;
- approved Section 3.1;
- approved Section 3.2;
- no later Chapter 3 result section.

No DOCX regeneration is required.

Blockers: **0**.

## 2. Independent actual-DOCX checks

The actual committed DOCX contains the correct canonical heading sequence.

Confirmed:
- Heading 1 count = 2;
- Heading 2 count = 9;
- Heading 3 count = 24.

The Chapter 2 headings in the actual DOCX match `CHAPTER_2.md`, including:
- `2.2. Chuẩn bị và xác nhận trạng thái ban đầu`;
- `2.3. Kịch bản 1 — Khảo sát dịch vụ SMB bằng Nmap`;
- `2.4. Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE`.

The actual Chapter 3 headings are exactly:
- 3.1;
- 3.1.1;
- 3.1.2;
- 3.2;
- 3.2.1;
- 3.2.2.

No 3.3 heading is published.

## 3. Table and figure audit

Seven report-table titles are present:
- Bảng 2.1–2.4;
- Bảng 3.1–3.3.

Seven report-figure captions/drawings are present:
- Hình 2.1–2.2;
- Hình 3.1–3.5.

The DOCX contains ten OOXML table objects in total because the three Chapter 2 command/code boxes are also implemented as one-row tables. This is expected and is not a report-table numbering defect.

For report tables:
- header-row repeat is present;
- row-splitting protection is present;
- Bảng 3.3 is structurally prepared for continuation across pages.

## 4. Page and section geometry audit

Actual OOXML page settings:
- A4 portrait;
- top ≈ 3.5 cm;
- bottom ≈ 3.0 cm;
- left ≈ 3.5 cm;
- right ≈ 2.0 cm.

The document uses a first-page-only review header:
`BẢN REVIEW — CHƯA PHẢI BẢN NỘP CUỐI — DEMO 1`.

The section has `titlePg` enabled and only the first-page header relationship is defined.

The Chapter 3 heading has an explicit page-break-before property, so Chapter 3 begins on a fresh page as required.

The stored Word pagination markers are consistent with the executor-reported 23-page layout.

## 5. Figure sizing audit

Seven drawing objects are present.

Displayed widths are approximately:
- Hình 2.1: 14.8 cm;
- Hình 2.2: 15.2 cm;
- Hình 3.1: 13.2 cm;
- Hình 3.2: 13.2 cm;
- Hình 3.3: 13.8 cm;
- Hình 3.4: 14.0 cm;
- Hình 3.5: 12.8 cm.

All are within the usable portrait-page width.

No additional or unapproved report image is embedded.

## 6. Internal-authoring leakage audit

Independent inspection confirms the published document does not contain:
- `CITE-ANCHOR`;
- raw Mermaid source;
- raw Markdown image syntax.

The first-page review banner is the only review marker embedded in the Word body/header layer.

## 7. Scope audit

WR1 remains a Demo 1 snapshot.

Chapter 3 contains only Sections 3.1 and 3.2.

The report does not publish:
- Section 3.3 content;
- Case B result section;
- Case C result section;
- Chapter 4.

The approved forward sentence at the end of 3.2 that points to future Mục 3.3 is not treated as later-section leakage.

## 8. Executor visual QA evidence

The executor:
- exported the DOCX through Microsoft Word COM to PDF;
- rendered all 23 PDF pages to 200-DPI PNGs;
- performed page-by-page inspection;
- corrected an initial 24th-page two-line spill;
- re-rendered after layout changes;
- checked heading orphans;
- checked figure/caption page alignment;
- checked table-title placement;
- finished with 23 pages.

The final reported visual result is consistent with the actual DOCX geometry and stored pagination information.

## 9. Reviewer-side QA correction

One bounded defect was found in the QA Markdown, not in the Word document.

The QA report's Heading-2 detail list retained three historical Chapter 2 labels even though the actual DOCX uses the correct canonical headings.

Reviewer-side correction:
- corrected 2.2 label;
- corrected 2.3 label;
- corrected 2.4 label.

This correction changes QA metadata only.

The DOCX itself remains byte-for-byte unchanged:
SHA-256 reported by executor:
`0affc468d7dd7fa31219da2d60fc4a1a0874fed2ca3e0b7f2f8da96c7230311b`.

## 10. Lecturer / document-level assessment

As a review snapshot, the document now succeeds at the intended goal: a lecturer can read Chapter 2 and then immediately see the baseline and Demo 1 results in normal report form rather than as disconnected Markdown artifacts.

The transition from method (Chapter 2) to measured result (3.1–3.2) is visible and the selected figures/tables are sufficient for defense-oriented reading.

No new technical-claim issue was introduced by DOCX assembly.

The one-point deduction is editorial: the original QA Markdown contained three stale heading labels. The actual Word document was correct, and the QA metadata has been corrected reviewer-side.

## 11. Final gate

External review: **PASS**.

Current state:

`WR1_PASS_WAITING_FOR_USER_APPROVAL`

Do not start WR2 yet.

Do not open X7D1.

On explicit user approval of the Word snapshot:
1. mark WR1 USER APPROVED / LOCKED;
2. integrate the WR1 review artifacts into `feature/ch3-integration`;
3. open WR2 from the resulting integration HEAD;
4. WR2 must contain full Chapter 2 + approved Sections 3.1–3.3;
5. X7D1 remains blocked until WR2 also passes external review + user approval.
