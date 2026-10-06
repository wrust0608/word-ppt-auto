# X7C1 — DRAFT CHAPTER 3 SECTION 3.3 SCENARIO 2

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7c1-ch3-scenario2-draft`  
Approved integration base: `d589e51e81aa0a3b87980ac73cef0d81ca330e17`

## 0. Objective

Write the first review draft of Chapter 3 Section 3.3 only:

`3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE`

Use the user-approved X7C0 Scenario 2 Evidence & Presentation Plan.

This phase must produce a student-facing experimental-results section with:

- exactly 2 locked H3 subsections;
- exactly 1 locked result table: Bảng 3.4;
- exactly 1 locked figure: Hình 3.6;
- approved derived crop + crop manifest for NSE-SMB-04;
- strict separation between direct observation and project classification;
- strict separation between remote `UNKNOWN` and local `UNPATCHED`;
- no Case B result leakage;
- no Chapter 4 risk/recommendation discussion.

Do not create a final DOCX.

## 1. Start and lineage

Run:

```bash
git fetch origin
git checkout feature/x7c1-ch3-scenario2-draft
git pull --ff-only origin feature/x7c1-ch3-scenario2-draft
git status --short
git rev-parse HEAD
git merge-base --is-ancestor d589e51e81aa0a3b87980ac73cef0d81ca330e17 HEAD
```

The last command must succeed.

Record the starting HEAD before editing.

If the branch does not descend from the approved integration commit, STOP.

## 2. Mandatory read order

Read:

1. `work/do-an/PROJECT_STATE.md`
2. `work/do-an/CHAPTER_3_CONTRACT.md`
3. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
4. `work/do-an/X7C0_SCENARIO2_PLAN_USER_APPROVAL_LOCK.md`
5. `work/do-an/X7C0_SCENARIO2_PLAN_EXTERNAL_REVIEW_R2_FINAL.md`
6. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
7. `work/do-an/CH3_33_SCENARIO2_PRESENTATION_PLAN_R1.md`
8. `work/do-an/CH3_33_SCENARIO2_FIGURE_SELECTION_R1.md`
9. `work/do-an/CH3_33_SCENARIO2_CLAIM_EVIDENCE_MAP_R1.md`
10. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md` — Scenario 2 rows only
11. `work/do-an/chapter3/CHAPTER_3_RESULT_MATRIX.md` — Scenario 2 only
12. `work/do-an/chapter3/CHAPTER_3_EVIDENCE_INDEX.md` — Scenario 2 only
13. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
14. `work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
15. `work/do-an/evidence/ALL_2026_10_06/COMMAND_LINEAGE_MATRIX.md` — Scenario 2 only
16. `work/do-an/AUTHOR_VOICE.md`
17. approved `work/do-an/CHAPTER_2.md` — Section 2.4 and Case B transition context only
18. approved `work/do-an/CH3_31_BASELINE_DRAFT_R1.md` — local UNPATCHED context only
19. approved `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md` — continuity/redundancy context only
20. all Scenario 2 evidence under:
    `work/do-an/chapter3/evidence/scenario2/`

Do not use old report prose as experimental truth.

Evidence precedence:

`direct raw/visual > metadata/manifest > historical/support > old report prose`.

## 3. Files allowed to create

Create:

- `work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md`
- `work/do-an/CH3_33_SCENARIO2_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_33_SCENARIO2_CROP_MANIFEST_R1.md`

Create exactly one derived presentation image under:

`work/do-an/chapter3/presentation/3_3/`

Use exactly:

`Hinh_3_6_MS17010_NSE.png`

Do not modify source evidence.

Do not modify approved X7C0 planning artifacts.

Do not modify Sections 3.1 or 3.2.

## 4. Locked section structure

The draft must contain exactly:

```text
## 3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE

### 3.3.1. Khảo sát điều kiện kết nối và thuộc tính giao thức SMB (NSE-SMB-01 đến NSE-SMB-03)

### 3.3.2. Đánh giá dấu hiệu lỗ hổng MS17-010 và đối chiếu trạng thái bản vá (NSE-SMB-04)
```

No additional numbered H3/H4.

Use one short opening paragraph under 3.3.

Do not write the section as a command log.

The intellectual flow must be:

`remote port state -> dialects -> signing -> dedicated MS17-010 script -> bounded UNKNOWN classification -> independent local UNPATCHED cross-reference`

## 5. Core thesis-reader objective

A lecturer reading only Section 3.3 must be able to answer:

1. Were TCP 139/445 reachable during Scenario 2?
2. Which SMB dialects were recorded?
3. What did `smb2-security-mode` report?
4. Was `smb-vuln-ms17-010` actually specified in the executed command?
5. Did the recorded output produce a usable Host script verdict?
6. What exactly does `UNKNOWN / NO USABLE SCRIPT RESULT` mean?
7. Why is `UNKNOWN != SAFE`?
8. Why does local `UNPATCHED` not convert the remote result into `VULNERABLE`?
9. Why is no exploitation/RCE result claimed?

If the prose needs repository terminology to answer these questions, rewrite it.

## 6. Locked Bảng 3.4

Title:

**Bảng 3.4. Trình tự và kết quả các phép đo NSE trên dịch vụ SMB từ trạm Kali Linux**

Columns:

`Phép đo | Mục tiêu kỹ thuật | Kết quả ghi nhận trực tiếp | Phân loại & Ranh giới kết luận`

Use the user-approved X7C0 table content and reviewer-final wording.

### NSE-SMB-01

Direct observation:

- `139/tcp OPEN`
- `445/tcp OPEN`
- `syn-ack ttl 128`

Allowed interpretation:

`Từ trạm Kali, TCP 139 và 445 được ghi nhận ở trạng thái OPEN và phản hồi SYN-ACK.`

Keep:

`445 OPEN != vulnerable`.

Do not say:
- SMB session succeeded;
- file sharing succeeded;
- service is “ready to accept connections”;
- vulnerability exists.

### NSE-SMB-02

Direct observation from `smb-protocols`:

- `NT LM 0.12 (SMBv1) [dangerous, but default]`
- `2.0.2`
- `2.1`
- `3.0`
- `3.0.2`

Use direct wording:

`smb-protocols ghi nhận 5 phương ngữ...`

Do not turn this into:
- “necessary condition”;
- “prerequisite for vulnerability”;
- vulnerability confirmation.

Keep:

`SMBv1 enabled != MS17-010 confirmed`.

### NSE-SMB-03

Direct observation:

- dialect shown: `3.0.2`
- `Message signing enabled but not required`

Do not generalize to all dialects.

Do not reconcile with local PowerShell/registry signing flags.

Use wording equivalent to:

`Đây là quan sát từ xa của smb2-security-mode và được ghi nhận độc lập với các cờ cấu hình cục bộ tại Mục 3.1.`

### NSE-SMB-04

Direct observation:

- command/output records `--script smb-vuln-ms17-010`;
- target is up;
- TCP 445 is OPEN;
- output reaches `Nmap done`;
- no `Host script results:` block appears;
- no corresponding error message is displayed in the recorded output.

Project classification:

`UNKNOWN / NO USABLE SCRIPT RESULT`

Important:

- `UNKNOWN` is **not** a literal Nmap string;
- the reason for absent usable script output is **not established**;
- no `VULNERABLE`, `SAFE`, `NOT VULNERABLE`, `PATCHED`, or `FALSE NEGATIVE` verdict may be attributed to this measurement.

Keep:

`UNKNOWN != SAFE`.

Do not emphasize scan duration in the public table.

## 7. Placement of Bảng 3.4

Use the table exactly once.

Preferred placement:

- after a concise explanation of NSE-SMB-01..03 at the end of 3.3.1;
- use the fourth row as a compact bridge into 3.3.2.

Do not duplicate the table.

Do not repeat every table cell verbatim in surrounding prose.

The prose should interpret the measurement sequence, while the table supplies compact detail.

## 8. Locked Hình 3.6

Source:

`work/do-an/chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png`

Expected source dimensions:

`1280 × 800`

Expected source SHA-256:

`c970e56481a920061416949ea7543dcb96f1f2f99635dbe201131073202e14ac`

Derived path:

`work/do-an/chapter3/presentation/3_3/Hinh_3_6_MS17010_NSE.png`

Caption:

**Hình 3.6. Kết quả thực thi kịch bản smb-vuln-ms17-010 từ trạm Kali Linux**

Approved crop:

`x=0, y=24, width=1280, height=330`

Must preserve:

- command line containing `--script smb-vuln-ms17-010`;
- target context;
- `445/tcp open microsoft-ds`;
- `Nmap done`;
- returned shell prompt;
- enough terminal context to show direct Nmap output.

Do not:
- annotate;
- add arrows;
- recolor;
- sharpen;
- regenerate text;
- alter source evidence.

## 9. Crop implementation and manifest

Before cropping:

1. calculate source SHA-256;
2. verify dimensions exactly 1280×800;
3. verify source SHA equals:
   `c970e56481a920061416949ea7543dcb96f1f2f99635dbe201131073202e14ac`.

If any check fails, STOP.

Create the derived crop using the approved rectangle only.

After cropping:

1. calculate derived SHA-256;
2. record derived dimensions;
3. visually inspect the output;
4. verify no command/result line required for interpretation is cut;
5. verify source byte remains unchanged.

Create:

`work/do-an/CH3_33_SCENARIO2_CROP_MANIFEST_R1.md`

Record:

- source path;
- source SHA-256;
- source dimensions;
- derived path;
- derived SHA-256;
- mode = CROP;
- exact crop rectangle;
- derived dimensions;
- content preserved;
- UI removed;
- reason;
- interpretation boundary.

If the rectangle unexpectedly cuts required content, do not silently change it. STOP and report.

## 10. Figure placement in prose

### Before Hình 3.6

Direct the reader to inspect:

- the use of `--script smb-vuln-ms17-010`;
- TCP 445 OPEN;
- the `Nmap done` line;
- absence of a `Host script results:` block.

### After Hình 3.6

State only:

- the direct visible observation;
- project classification = `UNKNOWN / NO USABLE SCRIPT RESULT`;
- UNKNOWN is not a literal Nmap verdict;
- reason for absent output is not established;
- `UNKNOWN != SAFE`.

Do not say the image itself “proves UNKNOWN”.

Do not call the script failed.

Do not invent NTSTATUS or protocol-internal cause.

## 11. Local UNPATCHED cross-reference

Section 3.1 is authoritative.

Use a restrained cross-reference:

`Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa.`

You may briefly remind the reader that the local classification came from the approved `srv.sys` / hotfix assessment, but do not re-run or broaden the patch analysis.

Keep two independent axes:

- local patch state = `UNPATCHED`;
- remote NSE-SMB-04 classification = `UNKNOWN`.

Forbidden:

- UNPATCHED => VULNERABLE;
- UNKNOWN => SAFE;
- UNKNOWN => PATCHED;
- UNKNOWN + UNPATCHED => FALSE NEGATIVE.

Do not describe the two axes as contradictory.

## 12. Command-lineage discipline

Student-facing Section 3.3 should normally use measurement labels rather than reproducing full commands.

Allowed measurement labels:

- NSE-SMB-01
- NSE-SMB-02
- NSE-SMB-03
- NSE-SMB-04

Do not expose internal IDs:

- `S2-RAW-*`
- `S2-IMG-*`
- `S2-C*`
- repository paths.

If exact command text is discussed around Hình 3.6, use the operator/screenshot command as displayed.

Do not conflate with Nmap-recorded argv.

For provenance QA only:

- operator/screenshot command for NSE02/03/04 has no `--privileged`;
- raw Nmap argv records `--privileged`;
- do not claim why.

Do not invent `-Pn`, extra `sudo`, or options from another measurement.

## 13. 3.3.1 narrative discipline

NSE-SMB-01..03 repeat some information already observed in Section 3.2.

Therefore:

- keep the prose compact;
- explicitly frame them as dedicated Scenario 2 measurements;
- do not reproduce Hình 3.5;
- do not create separate screenshots;
- do not spend a paragraph on every raw line.

A good 3.3.1 flow:

1. briefly state that the first three measurements establish the remote port/protocol/signing context;
2. summarize NSE01;
3. summarize NSE02;
4. summarize NSE03;
5. present Bảng 3.4 as the compact result synthesis;
6. transition to NSE04.

Do not call these results vulnerability confirmation.

## 14. 3.3.2 narrative discipline

This is the core of Section 3.3.

It should clearly separate:

### Observation
What Nmap visibly/raw-recorded.

### Classification
`UNKNOWN / NO USABLE SCRIPT RESULT`.

### Boundary
`UNKNOWN != SAFE`.

### Independent local fact
`UNPATCHED`.

The reader should not have to infer the distinction.

Avoid excessive methodological meta-language.

Write like a student explaining a difficult experimental result, not an auditor documenting a gate.

## 15. Exploitation boundary

Scenario 2 contains no canonical exploitation step and no canonical artifact/result for:

- RCE;
- reverse shell;
- Meterpreter.

Do not describe internal packet/payload behavior of the NSE script.

Do not say exploitation succeeded or failed.

Do not introduce exploit tools.

## 16. Transition to Section 3.4 / Case B

End Section 3.3 with one short transition only.

Required meaning:

- baseline + Scenario 1 + Scenario 2 establish the pre-intervention observations;
- Case B changes one controlled factor: SMBv1 server configuration;
- selected measurements are repeated:
  - protocol/dialect retest;
  - MS17-010 script retest.

Do not say:
- “Baseline Case A”;
- all measurements are repeated;
- Case B results;
- mitigation is effective;
- risk is reduced.

Effectiveness analysis belongs later.

## 17. Student-facing prose style

Use academic Vietnamese suitable for an undergraduate Information Security project.

Prefer:

- “kết quả đo”;
- “ghi nhận”;
- “quan sát từ xa”;
- “không xuất hiện khối kết quả...”;
- “chưa đủ căn cứ kết luận”;
- “được phân loại là UNKNOWN trong phạm vi phép đo”.

Avoid:

- canonical;
- ground truth;
- gate;
- governance;
- Evidence ID;
- Claim ID;
- evidence layer;
- audit-report tone;
- “chứng minh an toàn”;
- “âm tính giả”;
- broad security assurance.

Use natural paragraph variation.

Target prose length:

approximately **1,100–1,600 words**, excluding table cells/caption where practical.

Do not pad.

## 18. Chapter 3 / Chapter 4 boundary

Allowed:

- measured results;
- direct observations;
- bounded interpretation;
- local-vs-remote distinction;
- comparison with approved earlier Section 3.2 where needed for redundancy/continuity.

Forbidden:

- risk rating;
- CIA analysis;
- remediation recommendation;
- residual risk;
- patch strategy;
- security-program advice;
- “effectiveness” verdict for Case B/C;
- enterprise guidance.

## 19. Claim-map discipline

Use approved internal claims `S2-C01..S2-C15`.

Do not expose claim IDs in student prose.

In self-review, map every substantive paragraph/table/figure to the approved claim map.

Do not invent new technical result claims.

If a sentence cannot map to an approved claim or a purely editorial transition, revise it.

## 20. Citation discipline

Scenario 2 measured observations do not require external citations.

Do not create a new bibliography.

Do not invent IEEE numbering.

For local UNPATCHED, cross-reference Section 3.1 instead of restating external Microsoft evidence unnecessarily.

If an external definition is absolutely needed, first verify it exists in the Source Ledger and reuse the stable source anchor. Prefer omission over unnecessary theory.

## 21. Self-review

Create:

`work/do-an/CH3_33_SCENARIO2_DRAFT_SELF_REVIEW_R1.md`

Include:

1. word count;
2. heading audit;
3. table count = 1;
4. figure count = 1;
5. presentation image existence;
6. crop-manifest audit;
7. paragraph/table/figure-to-claim audit using S2-C01..S2-C15;
8. NSE01 TCP-boundary audit;
9. NSE02 SMBv1/MS17 boundary audit;
10. NSE03 signing independence audit;
11. NSE04 direct-observation audit;
12. UNKNOWN classification audit;
13. `UNKNOWN != SAFE` audit;
14. local UNPATCHED vs remote UNKNOWN independence audit;
15. no false-negative language;
16. no invented NTSTATUS/missing-output cause;
17. no exploitation/RCE leakage;
18. command-lineage audit;
19. measurement-label/internal-ID audit;
20. Case B transition audit;
21. Chapter 3/4 boundary audit;
22. author-voice audit;
23. later-section leakage audit;
24. unresolved concerns.

Do not self-declare external PASS.

Final state:

`X7C1_CH3_33_SCENARIO2_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`

## 22. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md
git diff --check
```

Run the IEEE citation audit only if applicable to this citation-light standalone fragment. If not applicable, record why; do not invent references.

Additionally verify:

- exactly 1 H2 + 2 H3;
- exactly 1 report table;
- exactly 1 report image embed;
- Bảng 3.4 only;
- Hình 3.6 only;
- source image unchanged;
- crop rectangle exactly `0,24,1280,330`;
- no NSE01/02/03 presentation images;
- no `Baseline Case A`;
- no `Nmap 7.95`;
- no `FALSE NEGATIVE` / `âm tính giả` in student prose;
- no VULNERABLE/SAFE/NOT VULNERABLE/PATCHED verdict assigned to NSE04;
- no invented NTSTATUS or cause;
- no local/remote signing reconciliation;
- no UNPATCHED -> VULNERABLE conversion;
- no exact Case B result;
- no Case C;
- no Chapter 4 analysis;
- no internal Evidence/Claim IDs in student prose.

## 23. Git

Commit:

`draft(ch3): write scenario2 section 3.3 R1`

Push:

`feature/x7c1-ch3-scenario2-draft`

Do not merge.

## 24. Handoff

Return:

1. branch;
2. starting SHA;
3. local commit SHA;
4. remote commit SHA;
5. created/modified file list;
6. prose word count;
7. H2/H3 count;
8. table count;
9. figure count;
10. crop-manifest summary with source/derived SHA + exact rectangle;
11. paragraph-to-claim audit summary;
12. NSE01 port wording audit;
13. NSE02 dialect/SMBv1 audit;
14. NSE03 signing independence audit;
15. NSE04 direct-observation audit;
16. UNKNOWN classification audit;
17. UNKNOWN != SAFE audit;
18. UNPATCHED vs UNKNOWN audit;
19. no-cause / no-NTSTATUS audit;
20. exploitation/RCE audit;
21. Case B transition audit;
22. citation audit;
23. QA results;
24. clean git status.

Final state:

`X7C1_CH3_33_SCENARIO2_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`

Then STOP.

Do not open X7D.
Do not write Section 3.4.
Do not write Chapter 4.
Do not create final DOCX.
