# X7H R1 — EDIT COMPLETE CHAPTER 3 AS ONE THESIS CHAPTER

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7h-ch3-whole-review`  
Base: complete Chapter 3 assembled and X7G mechanically approved.

## 0. Objective

Perform the whole-Chapter-3 editorial pass required by the roadmap.

Read and execute:

`work/do-an/X7H_CH3_WHOLE_PRODUCT_REVIEW_R1.md`

The goal is not to rewrite the experiments.

The goal is to turn the mechanically concatenated Chapter 3 into one coherent, natural Vietnamese Information Security thesis chapter while preserving every locked technical fact.

## 1. Mandatory global checkpoint

Before editing, read:

1. `work/do-an/ROADMAP_CURRENT_CH2_CH3_2026_10_07.md`
2. `work/do-an/PROJECT_STATE.md`
3. `work/do-an/CHAPTER_3_CONTRACT.md`
4. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
5. `work/do-an/X7H_CH3_WHOLE_PRODUCT_REVIEW_R1.md`
6. `work/do-an/CHAPTER_3_COMPLETE_R1.md`

Confirm:
- Chapter 2 is locked and must not be changed;
- 3.1–3.7 technical facts are user-approved;
- Bảng 3.1–3.7 are locked;
- Hình 3.1–3.11 are locked;
- no Hình 3.12 / Bảng 3.8;
- X7I Word is blocked until X7H PASS + user approval;
- Chapter 4 is dormant.

## 2. Start

Run:

```bash
git fetch origin
git checkout feature/x7h-ch3-whole-review
git pull --ff-only origin feature/x7h-ch3-whole-review
git status --short
git rev-parse HEAD
```

Do not work on another branch.

## 3. Source preservation

Do NOT modify the individually approved source files:
- `CH3_31_BASELINE_DRAFT_R1.md`
- `CH3_32_SCENARIO1_DRAFT_R1.md`
- `CH3_33_SCENARIO2_DRAFT_R1.md`
- `CH3_34_CASEB_DRAFT_R1.md`
- `CH3_35_CASEC_DRAFT_R1.md`
- `CH3_36_37_SYNTHESIS_DRAFT_R1.md`

They remain approval records.

Create the polished whole-chapter product from:
`CHAPTER_3_COMPLETE_R1.md`.

## 4. Output files

Create exactly:

- `work/do-an/CHAPTER_3_COMPLETE_R2.md`
- `work/do-an/CHAPTER_3_WHOLE_EDIT_SELF_REVIEW_R1.md`

Do not overwrite R1.

No DOCX/PDF.

## 5. Keep the locked structure

Keep:
- H1 Chapter 3;
- H2 3.1–3.7;
- approved H3 structure;
- Bảng 3.1–3.7;
- Hình 3.1–3.11;
- all image paths.

No new section.
No new table.
No new figure.

## 6. Add a short Chapter 3 opening

Immediately after the H1, add about 70–110 words introducing the chapter flow:

`baseline -> Scenario 1 -> Scenario 2 -> Case B -> Case C -> comparison -> conclusion`.

Do not repeat Chapter 2 methodology.
Do not make new claims.

## 7. Compress 3.2 -> 3.3 repetition

Keep Section 3.2 as the main detailed presentation of:
- port state;
- service fingerprint;
- dialects;
- capabilities;
- signing.

In Section 3.3.1:
- do not re-explain all those facts in long separate paragraphs;
- state that NSE-SMB-01 to 03 reconfirm the technical conditions used before the MS17-specific test;
- retain the measured values;
- rely on Bảng 3.4 for detailed row-by-row data.

Keep Bảng 3.4 unchanged in technical values.

Do not delete NSE-SMB-01/02/03.

## 8. Consolidate UNKNOWN explanation

Keep the full explanation in 3.3.2.

It must preserve:
- no `Host script results:`;
- UNKNOWN / NO USABLE SCRIPT RESULT;
- UNKNOWN is project classification, not literal Nmap text;
- cause is not established;
- UNKNOWN != SAFE;
- local UNPATCHED is independent from remote UNKNOWN.

In 3.4, 3.5, 3.6 and 3.7:
- shorten repeated explanation;
- retain the classification and relevant boundary;
- refer back to 3.3 when natural.

Do not assign a cause.

## 9. Remove duplicate transitions

At:
- 3.3 -> 3.4;
- 3.4 -> 3.5;
- 3.5 -> 3.6;

avoid announcing the next section twice.

Keep one clean transition only.

Prefer to keep the next section opening and shorten the preceding ending.

## 10. Normalize strict evidence wording

Replace looser early wording:

- `phương ngữ được máy chủ chấp nhận`
- `hệ thống chấp nhận phương ngữ`
- `Phương ngữ hỗ trợ`

with bounded wording:

- `phương ngữ được ghi nhận`
- `smb-protocols ghi nhận...`
- `Phương ngữ ghi nhận`

For NSE-SMB-01:
prefer:
`TCP 139/445 tiếp tục được ghi nhận OPEN và phản hồi SYN-ACK từ góc nhìn trạm Kali`

rather than using the remote result to assert a stronger local-state conclusion.

Do not change the measured values.

## 11. Clean student-facing vocabulary

In student prose, prefer:

- `đề tài` instead of `đề án`;
- `mô hình mạng` instead of naked `topology`;
- `trạng thái ghi nhận cuối lượt` instead of `metadata cuối`;
- `bản ghi của lượt thực nghiệm` instead of `siêu dữ liệu tiến trình thực nghiệm`;
- `tại thời điểm kiểm tra` instead of `point-in-time`;
- natural Vietnamese instead of `workload`;
- `phán quyết khả dụng` in prose instead of naked `usable`.

EXCEPTION:
the locked classification string:
`UNKNOWN / NO USABLE SCRIPT RESULT`
must remain unchanged.

Do not remove necessary technical terms:
- SMB;
- Nmap;
- NSE;
- Transparent Bridge;
- pfSense;
- SYN-ACK;
- FILTERED;
- OPEN;
- UNPATCHED.

## 12. Case C rule-label discrepancy

Keep the discrepancy visible.

Do not hide it.

But shorten the audit-like wording.

Required meaning:
- log screenshot shows a label inconsistent with the run record;
- therefore Hình 3.11 proves matching traffic was Blocked;
- it does not prove the exact named rule matched.

Exact labels may appear once.

## 13. Normalize figure captions

Use one convention for all 11 figures:

```markdown
![Hình 3.x](relative/path.png)
*Hình 3.x. Caption text*
```

Preserve:
- number;
- path;
- caption meaning.

Do not regenerate or rename images.

Do not alter bytes.

## 14. Repeated openings

Fix the linter repetition caused by multiple paragraphs opening with:
`Sau khi xác...`

Diversify naturally.

Do not use mechanical synonym substitution.

## 15. Chapter 3 ending

Shorten the final sentence.

Do not write:
`...tiếp tục đánh giá ở các phần sau khi phạm vi báo cáo được mở rộng.`

End cleanly, for example:

`Các kết quả này khép lại phạm vi đo đạc thực nghiệm của Chương 3.`

No Chapter 4 opening.

## 16. Compression

Aim to remove approximately 600–900 redundant prose words if possible.

Priority:
1. 3.3 repetition of 3.2;
2. repeated UNKNOWN explanation;
3. duplicate transitions;
4. QA-like evidence-management wording.

Do NOT remove:
- unique facts;
- locked table rows;
- locked figures;
- rule-label discrepancy;
- patch-version evidence;
- comparison table.

## 17. Technical locks

Must remain true:

- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `SMBv1 disabled != PATCHED`
- `FILTERED != PATCHED`
- `UNKNOWN != SAFE`

Also:
- Case B TCP445 = OPEN only; no post-Case-B syn-ack;
- Case B TCP139 was not remeasured;
- Case C has no dialect retest to synthesize;
- Case C exact named-rule attribution remains unresolved;
- local UNPATCHED is independent from remote UNKNOWN;
- no exploitation/RCE result.

## 18. STOP rule for technical changes

If you believe a factual value needs to change:
STOP.

Do not edit it.

Report it as:
`TECHNICAL_REOPEN_REQUIRED`.

X7H is authorized only for editorial/coherence changes that preserve technical meaning.

## 19. Self-review

Create:
`work/do-an/CHAPTER_3_WHOLE_EDIT_SELF_REVIEW_R1.md`

Include:
- R1 vs R2 prose word count;
- per-section prose word count;
- total tables = 7;
- total figures = 11;
- H1/H2/H3 counts;
- repeated-opening audit;
- 3.2/3.3 redundancy audit;
- UNKNOWN repetition audit;
- terminology cleanup audit;
- figure-caption normalization audit;
- image-path and image-SHA unchanged audit;
- technical-lock audit;
- no new claim/evidence audit;
- no Chapter 4 leakage;
- no source-section modifications.

Do not self-declare external PASS.

Final state:
`X7H_CH3_COMPLETE_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

## 20. QA

Run:

```bash
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_3_COMPLETE_R2.md
git diff --check
uv run python scripts/validate_project.py
```

Verify:
- all 11 image paths exist;
- all 11 source image hashes unchanged;
- no Bảng 3.8;
- no Hình 3.12;
- source section files unchanged.

## 21. Git

Commit:

`edit(ch3): refine complete Chapter 3 whole-chapter R2`

Push:

`feature/x7h-ch3-whole-review`

Do not merge.

## 22. Handoff

Return:
1. branch;
2. starting SHA;
3. final local/remote SHA;
4. created files;
5. R1 vs R2 prose word counts;
6. per-section word counts;
7. 3.2/3.3 compression summary;
8. UNKNOWN consolidation summary;
9. transition cleanup summary;
10. terminology normalization summary;
11. figure-caption normalization summary;
12. technical-lock audit;
13. source-section unchanged audit;
14. image SHA/path audit;
15. QA;
16. clean git status.

Then STOP.

Do not build Word.
Do not edit Chapter 2.
Do not open Chapter 4.
