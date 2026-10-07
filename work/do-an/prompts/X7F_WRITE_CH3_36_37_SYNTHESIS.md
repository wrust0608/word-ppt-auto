# X7F — WRITE SECTIONS 3.6 AND 3.7

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7f-ch3-synthesis`  
Approved integration base: `26fbf8b36857e7c0149207ae694e25bfd2110b0c`

## 0. Objective

Write the final two sections of Chapter 3:

`3.6. So sánh kết quả thực nghiệm`

`3.7. Tổng kết chương`

Use only the already user-approved outputs of Sections 3.1–3.5.

This is a synthesis task.

Do not open new raw evidence.
Do not create new screenshots.
Do not rerun experiments.
Do not assemble the whole Chapter 3 yet.
Do not build Word.
Do not modify Chapter 2.
Do not open Chapter 4.

## 1. Start and lineage

Run:

```bash
git fetch origin
git checkout feature/x7f-ch3-synthesis
git pull --ff-only origin feature/x7f-ch3-synthesis
git status --short
git rev-parse HEAD
git merge-base --is-ancestor 26fbf8b36857e7c0149207ae694e25bfd2110b0c HEAD
```

If lineage fails, STOP.

## 2. Mandatory read order

Read fully:

1. `work/do-an/ROADMAP_CURRENT_CH2_CH3_2026_10_07.md`
2. `work/do-an/PROJECT_STATE.md`
3. `work/do-an/CHAPTER_3_CONTRACT.md`
4. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
5. `work/do-an/CHAPTER_3_SECTION_EVIDENCE_MAP.md`
6. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
7. approved Section 3.1:
   `work/do-an/CH3_31_BASELINE_DRAFT_R1.md`
8. approved Section 3.2:
   `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md`
9. approved Section 3.3:
   `work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md`
10. approved Section 3.4:
    `work/do-an/CH3_34_CASEB_DRAFT_R1.md`
11. approved Section 3.5:
    `work/do-an/CH3_35_CASEC_DRAFT_R1.md`
12. final external reviews/user locks for 3.1–3.5 when needed to confirm a boundary.

Do not inspect or introduce unapproved evidence outside these approved outputs unless the manager explicitly asks later.

## 3. Locked headings

Use exactly:

### `3.6. So sánh kết quả thực nghiệm`

### `3.7. Tổng kết chương`

No H3 is required by default.

Add an H3 only if absolutely necessary for readability; the default target is no additional H3.

## 4. Presentation policy

Use:
- exactly one comparison table:
  **Bảng 3.7**
- no new figure;
- therefore no Hình 3.12 in X7F.

Bảng 3.7 is the main synthesis device.

Do not reproduce earlier screenshots.
Do not create a screenshot collage.

## 5. Purpose of Section 3.6

Section 3.6 must compare the already-approved observations.

It must NOT retell Sections 3.1–3.5 in sequence.

The reader should be able to answer:

1. What was observed at baseline?
2. What changed after Case B?
3. What changed after Case C?
4. What remained unchanged?
5. Which layer did each intervention affect?

The comparison should make the distinction between:
- host protocol configuration;
- remote network visibility;
- local patch state;
- remote MS17-010 verdict.

## 6. Bảng 3.7

Use title:

`Bảng 3.7. So sánh trạng thái thực nghiệm giữa đường cơ sở, Case B và Case C`

Recommended columns:

`Tiêu chí so sánh | Đường cơ sở / Kịch bản 1–2 | Case B — Vô hiệu hóa SMBv1 | Case C — Kiểm soát bằng pfSense | Nhận xét thực nghiệm`

Keep the table compact enough for A4.

Use only rows that add comparative value.

Recommended row families:

1. Lớp can thiệp
2. TCP 139 quan sát từ Kali
3. TCP 445 quan sát từ Kali
4. Phương ngữ SMB quan sát được
5. SMB1 local configuration
6. LanmanServer / local listeners
7. Local patch state
8. Remote MS17-010 result

Important details:

### Baseline
- 139 OPEN
- 445 OPEN
- SMB dialect list includes:
  `NT LM 0.12`, `2.0.2`, `2.1`, `3.0`, `3.0.2`
- SMB1=True
- LanmanServer=Running
- local listeners 139/445 present
- patch state UNPATCHED
- remote MS17 result UNKNOWN

### Case B
- intervention layer = SMB server configuration on Windows
- SMB1=False
- SMB2=True
- FS-SMB1 remains Installed
- LanmanServer=Running at recorded point
- TCP 445 remains OPEN in the selected retest
- dialect retest records:
  `2.0.2`, `2.1`, `3.0`, `3.0.2`
- `NT LM 0.12` does not appear in the retest list
- patch state remains UNPATCHED
- remote MS17 result remains UNKNOWN

For TCP 139 in Case B:
- if it was not re-measured in the approved Case B output, write:
  `Không đo lại trong Case B`
or equivalent.
Do NOT infer OPEN from baseline.

### Case C
- intervention layer = tested network path via pfSense Transparent Bridge
- TCP 139 = FILTERED/no-response from Kali
- TCP 445 = FILTERED/no-response from Kali
- no standard SMB dialect retest result should be invented for Case C
- local SMB1=True
- SMB2=True
- LanmanServer=Running
- local listeners 139/445 present
- patch state UNPATCHED
- remote MS17 result remains UNKNOWN

For rows not measured in a case:
use:
`Không đo lại`
or:
`Không có phép đo tương ứng trong kịch bản`

Never fill gaps by inference.

## 7. Core empirical comparisons

The prose after/before Bảng 3.7 should explain concisely:

### A. Baseline
The starting condition exposes SMB services remotely from Kali and locally records an UNPATCHED Windows state.

Do not convert this into a vulnerability verdict.

### B. Case B
The host-side SMB1 server configuration changes.

Observed remote effect:
- SMB1 dialect no longer appears in the selected dialect retest;
- TCP 445 remains OPEN;
- SMB2/3 dialect values remain recorded.

Local patch classification remains UNPATCHED.
Remote MS17 result remains UNKNOWN.

Meaning:
- changing protocol configuration changes one layer;
- it is not the same as patching.

### C. Case C
The tested network path is filtered by pfSense.

Observed remote effect:
- TCP 139/445 become FILTERED/no-response from Kali;
- corresponding SMB SYN traffic is recorded as Block on pfSense.

Windows-local recorded state remains:
- SMB1=True;
- SMB2=True;
- LanmanServer=Running;
- local listeners present;
- UNPATCHED.

Remote MS17 result remains UNKNOWN.

Meaning:
- network filtering changes remote visibility/reachability on the tested path;
- it is not the same as changing the Windows patch state.

## 8. Important comparison boundaries

Keep these distinctions visible but do not repeat them excessively:

- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `SMBv1 disabled != PATCHED`
- `FILTERED != PATCHED`
- `UNKNOWN != SAFE`

Use them where they matter.

Do not create a paragraph that merely lists all five inequalities mechanically.

## 9. Do not rank controls

Section 3.6 is empirical comparison only.

Do not say:
- Case B is better than Case C;
- Case C is more effective;
- defense in depth is recommended;
- patching is the best solution;
- pfSense is the optimal solution;
- disable SMBv1 is insufficient as a recommendation;
- risk reduced by X%;
- one control is more secure.

Those belong outside Chapter 3.

You may state:

`Hai can thiệp tạo ra các thay đổi quan sát được ở hai lớp khác nhau.`

That is an empirical structural comparison, not a recommendation.

## 10. Rule-label conflict

Do not re-open a long discussion of the Case C label conflict.

If Bảng 3.7 mentions pfSense log, use only:

`Matching SMB SYN traffic recorded as Block`

Do not name the exact matched rule.

The detailed disclosure already exists in Section 3.5.

## 11. Timebase

Do not mention or compare displayed timestamps.

No global chronology is needed in Section 3.6.

## 12. Section 3.6 length

Target:
- approximately **650–900 prose words**, excluding Bảng 3.7.

Use the table to compress repetition.

Do not repeat full results from earlier sections.

A useful flow:

1. short comparison opening;
2. Bảng 3.7;
3. 3–5 synthesis paragraphs:
   - baseline vs Case B;
   - baseline vs Case C;
   - Case B vs Case C;
   - inference boundaries.

## 13. Purpose of Section 3.7

Section 3.7 closes Chapter 3.

It should answer:

**What did the experimental chapter establish, and what did it not establish?**

Use only conclusions already supported by 3.1–3.6.

No new evidence.
No new table.
No new figure.

## 14. Section 3.7 content

Keep concise.

Must summarize:

- baseline confirmed the test environment and local UNPATCHED state;
- Scenario 1 established SMB service visibility/open ports/dialects;
- Scenario 2 produced an inconclusive remote MS17 verdict: UNKNOWN;
- Case B changed SMB1 server configuration and the selected dialect retest;
- Case C changed remote port visibility on the tested path while Windows-local patch state remained UNPATCHED;
- remote scanner state and local patch state are distinct evidence layers.

Must preserve:

`UNKNOWN != SAFE`

`FILTERED != PATCHED`

Do not:
- recommend a final solution;
- introduce risk rankings;
- discuss cost;
- discuss implementation strategy for an enterprise;
- introduce Chapter 4 content;
- claim exploitability;
- claim safety.

## 15. Section 3.7 final paragraph

End Chapter 3 naturally.

Preferred concept:

`Nhìn chung, các phép đo cho thấy việc thay đổi cấu hình giao thức và việc lọc lưu lượng trên đường mạng tạo ra những thay đổi quan sát được ở các lớp khác nhau, trong khi trạng thái bản vá cục bộ của máy chủ vẫn phải được xác định độc lập. Các kết quả này khép lại phạm vi đo đạc thực nghiệm của Chương 3 và là cơ sở để tiếp tục đánh giá ở các phần sau khi phạm vi báo cáo được mở.`

Do not explicitly open Chapter 4 as an active next task.

## 16. Section 3.7 length

Target:
- approximately **250–400 prose words**.

Total X7F prose target:
- approximately **900–1,300 words** excluding Bảng 3.7.

Keep it concise because Sections 3.1–3.5 are already substantial.

## 17. Academic voice

Write in natural Vietnamese academic style.

Prefer:
- `kết quả đo`
- `ghi nhận`
- `so sánh`
- `trạng thái quan sát từ xa`
- `trạng thái cục bộ`
- `phân loại UNPATCHED`
- `không có phép đo tương ứng`

Avoid:
- governance;
- gate;
- Evidence ID;
- Claim ID;
- canonical;
- truth matrix;
- QA terminology;
- "100%";
- "chứng minh tuyệt đối";
- marketing/security certainty.

Do not sound like an internal audit memo.

## 18. Required output files

Create exactly:

- `work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md`
- `work/do-an/CH3_36_37_SYNTHESIS_SELF_REVIEW_R1.md`

Do not create:
- figure-selection artifact;
- crop manifest;
- new images;
- new raw evidence;
- Chapter 3 assembled file;
- Word/PDF.

## 19. Self-review

Create:

`work/do-an/CH3_36_37_SYNTHESIS_SELF_REVIEW_R1.md`

Report:
- prose word count for 3.6;
- prose word count for 3.7;
- total prose word count;
- H2/H3 count;
- table count;
- figure count;
- Bảng 3.7 presence;
- no Hình 3.12;
- every Bảng 3.7 row traced to an approved section;
- every "Không đo lại" / "Không có phép đo tương ứng" case audited;
- no invented Case B TCP139 state;
- no invented Case C dialect state;
- no effectiveness/risk ranking;
- no recommendation;
- no new evidence;
- no Chapter 4 leakage;
- no internal QA/governance vocabulary in student-facing prose.

Do not self-declare external PASS.

Final state:

`X7F_CH3_36_37_R1_READY_FOR_EXTERNAL_REVIEW`

## 20. Required searches

Search the draft for problematic concepts:

- `hiệu quả hơn`
- `tốt hơn`
- `tối ưu`
- `khuyến nghị`
- `nên áp dụng`
- `an toàn`
- `không có lỗ hổng`
- `not vulnerable`
- `patched`
- `false negative`
- `Case B.*139`
- `Case C.*NT LM 0.12`
- `Case C.*2.0.2`
- `Case C.*2.1`
- `Case C.*3.0`
- `Case C.*3.0.2`
- `bypass`
- `exploit`
- Evidence ID
- Claim ID
- gate
- governance.

Manually inspect allowed contextual occurrences such as `UNPATCHED` or `FILTERED != PATCHED`.

## 21. QA

Run:

```bash
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md
git diff --check
```

You may run project validation.

Do not modify infrastructure.

## 22. Git

Commit:

`draft(ch3): write sections 3.6 and 3.7 R1`

Push:

`feature/x7f-ch3-synthesis`

Do not merge.

## 23. Handoff

Return:

1. branch;
2. starting SHA;
3. final local/remote SHA;
4. created files;
5. 3.6 prose word count;
6. 3.7 prose word count;
7. total prose word count;
8. Bảng 3.7 row summary;
9. audit of missing/unmeasured cells;
10. baseline/Case B/Case C comparison audit;
11. inference-boundary audit;
12. no-ranking/no-recommendation audit;
13. Chapter 3 conclusion audit;
14. QA;
15. clean git status.

Final state:

`X7F_CH3_36_37_R1_READY_FOR_EXTERNAL_REVIEW`

Then STOP.

Do not assemble Chapter 3.
Do not build Word.
Do not modify Chapter 2.
Do not open Chapter 4.
