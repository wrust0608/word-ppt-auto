# X7C0 R2 — CORRECT SCENARIO 2 EVIDENCE/PRESENTATION PLAN

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7c0-ch3-scenario2-plan`  
R1 candidate: `4868942a5a6c86eb3feb03ce6110edfbcd2892e2`

## 0. Objective

Correct only the bounded issues identified in:

`work/do-an/X7C0_SCENARIO2_PLAN_EXTERNAL_REVIEW_R1.md`

Do not redesign the approved direction.

Preserve:

- 2 proposed H3;
- 1 proposed Bảng 3.4;
- NSE01 image DROP;
- NSE02 image DROP;
- NSE03 image DROP;
- NSE04 image KEEP as tentative Hình 3.6;
- no second UNKNOWN-vs-UNPATCHED mini-table;
- provisional NSE04 crop rectangle;
- all core UNKNOWN / UNPATCHED independence locks.

Do **not** write Section 3.3 prose.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7c0-ch3-scenario2-plan
git pull --ff-only origin feature/x7c0-ch3-scenario2-plan
git status --short
git rev-parse HEAD
```

Read first:

1. `work/do-an/X7C0_SCENARIO2_PLAN_EXTERNAL_REVIEW_R1.md`
2. the four X7C0 R1 artifacts;
3. all Scenario 2 raw `.nmap` outputs;
4. `Scenario2_Run_Manifest.txt`;
5. `work/do-an/evidence/ALL_2026_10_06/COMMAND_LINEAGE_MATRIX.md`;
6. approved Section 3.1 patch wording;
7. approved Chapter 2 Case B method.

## 2. Allowed files to modify

Modify only:

- `work/do-an/CH3_33_SCENARIO2_FIGURE_SELECTION_R1.md`
- `work/do-an/CH3_33_SCENARIO2_PRESENTATION_PLAN_R1.md`
- `work/do-an/CH3_33_SCENARIO2_CLAIM_EVIDENCE_MAP_R1.md`
- `work/do-an/CH3_33_SCENARIO2_PLAN_SELF_REVIEW_R1.md`

Do not modify evidence, Section 3.1/3.2, numbering ledger, truth matrix, R3 locks, Chapter 2, or later sections.

## 3. Keep the presentation geometry locked for R2

Do not redesign:

- 2 H3;
- Bảng 3.4 only;
- NSE01/02/03 screenshots DROP;
- NSE04 screenshot KEEP as tentative Hình 3.6;
- no second tiny comparison table.

The purpose of R2 is factual and methodological precision.

## 4. Correct the transition — no “Baseline Case A”

Remove every use of:

`Baseline Case A`.

Case A is not a completed canonical experiment.

Use:

`baseline`
or
`trạng thái baseline`.

The conceptual transition should say only:

- baseline + Scenario 1 + Scenario 2 have been completed;
- the next section changes one controlled factor: SMBv1 server configuration;
- selected measurements are repeated for comparison.

Do not say Case B repeats “all” measurements.

Approved Case B retests are selected measurements corresponding to:

- protocol/dialect retest;
- MS17-010 script retest.

Do not reveal their results.

Avoid broad `đánh giá hiệu quả` language in this transition; effectiveness analysis belongs to Chapter 4.

## 5. Correct NSE-SMB-01 public wording

Remove:

`Hai cổng dịch vụ SMB sẵn sàng tiếp nhận kết nối qua mạng.`

Use direct evidence:

`Từ trạm Kali, TCP 139 và 445 được ghi nhận ở trạng thái OPEN và phản hồi SYN-ACK.`

Keep:

`445 OPEN != vulnerable`.

Do not infer:
- successful SMB session;
- authenticated access;
- file-sharing workload availability.

## 6. Correct SMBv1 wording

Remove every student-facing or allowed-wording statement that calls SMBv1:

- `điều kiện cần`;
- `điều kiện tiên quyết cho khả năng bị ảnh hưởng`.

Use direct measured wording:

`NSE-SMB-02 ghi nhận NT LM 0.12 (SMBv1) cùng 2.0.2, 2.1, 3.0 và 3.0.2.`

The Nmap annotation `[dangerous, but default]` may be reported only as literal tool output.

Keep:

`SMBv1 enabled != MS17-010 confirmed`.

Do not introduce exploitability theory.

## 7. Correct NSE-SMB-04 evidence vs classification

Maintain these direct facts:

- command/output records `--script smb-vuln-ms17-010`;
- target is up;
- 445/tcp is OPEN;
- output reaches `Nmap done`;
- no `Host script results:` block appears;
- no corresponding error message is displayed in the recorded output.

Use bounded command wording such as:

`Lệnh Nmap được thực thi với tùy chọn --script smb-vuln-ms17-010.`

Do not require wording that claims internal script-loading mechanics.

Separate:

### Direct observation
`No Host script results / no usable result block is printed.`

from:

### Project classification
`UNKNOWN / NO USABLE SCRIPT RESULT`.

Explicitly state that UNKNOWN is **not** a literal Nmap string.

Do not say:
- screenshot “proves UNKNOWN”;
- image proves every possible network/script cause has been excluded;
- absence of output was definitely not caused by any hidden condition.

Remove unnecessary absolutes:
- `hoàn toàn vắng mặt`;
- `không thể thay thế`.

Prefer:
`không xuất hiện`.

Do not emphasize `1.35 seconds` in the proposed public Bảng 3.4 or future prose. It may remain as an internal factual note only.

Keep:
`UNKNOWN != SAFE`.

## 8. Correct the local UNPATCHED cross-reference

Do not independently broaden/re-derive Section 3.1.

Preferred public plan wording:

`Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa.`

If the internal claim map retains supporting detail, use the exact approved facts:

- numeric `srv.sys = 6.3.9600.16421`;
- Microsoft minimum updated threshold = `6.3.9600.18604`;
- observed local hotfix inventory does not record KB4012213, KB4012216, or a mapped superseding update containing the MS17-010 fix;
- local classification = UNPATCHED.

Do not write an omniscient statement that all replacement rollups were absent from machine history.

Keep:
`local UNPATCHED != remote VULNERABLE verdict`.

## 9. Correct command provenance

In the self-review:

- replace incorrect `Nmap 7.95` with direct raw `Nmap 7.99`;
- do not synthesize the raw header;
- use exact direct raw/command-lineage wording.

For NSE02/03/04 preserve:

- operator command/screenshot layer: no `--privileged`;
- Nmap-recorded argv layer: contains `--privileged`.

Do not claim why `--privileged` appears unless an approved source establishes the mechanism.

Do not add `sudo`, `-Pn` or other options to the wrong layer.

## 10. Correct measurement-label vs internal-ID terminology

`NSE-SMB-01` through `NSE-SMB-04` are approved **measurement labels** from Chapter 2.

They are allowed in student-facing prose and Bảng 3.4.

Do not call them internal Evidence IDs.

Internal identifiers that must stay out of student-facing report text include:

- `S2-RAW-01` etc.;
- `S2-IMG-04`;
- `S2-C01` etc.;
- repository paths.

Correct the inconsistent rule in the presentation plan.

## 11. Correct exploitation-scope claim

For `S2-C15`, remove unsupported wording that describes the NSE script as:

`không gửi mã khai thác tấn công`.

Use the project-level evidence boundary:

`Không có bước khai thác canonical và không có artifact/kết quả RCE, reverse shell hoặc Meterpreter trong Kịch bản 2.`

Do not characterize internal packet or payload behavior of the script.

## 12. Figure-selection wording cleanup

Keep NSE04 as KEEP.

For its value, use:

- command visibly specifies the MS17-010 script;
- port 445 is open;
- Nmap completes;
- no Host script result block appears.

Do not state that the image proves:
- no typo could exist in any sense;
- no network/script cause is possible;
- UNKNOWN as a literal tool verdict.

The image supports the direct observation; the plan supplies the bounded UNKNOWN classification.

Keep the provisional crop:

`x=0, y=24, width=1280, height=330`.

Do not create the crop in X7C0.

## 13. Self-review updates

Update self-review to explicitly verify:

- `Baseline Case A` count = 0;
- wrong `Nmap 7.95` count = 0;
- public/table `sẵn sàng tiếp nhận` count = 0;
- SMBv1 `điều kiện cần/điều kiện tiên quyết` claim count = 0;
- measurement labels NSE-SMB-01..04 remain allowed;
- internal Stable Evidence IDs remain absent from proposed student-facing content;
- NSE04 direct-observation vs UNKNOWN-classification distinction is explicit;
- local UNPATCHED wording matches approved Section 3.1;
- Case B transition says selected retests, not all measurements;
- no false-negative language;
- no exploit/RCE claim;
- no evidence bytes changed;
- no Section 3.3 prose created.

Do not self-declare external PASS.

Final executor state:

`X7C0_SCENARIO2_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

## 14. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

Also perform searches for:

- `Baseline Case A`
- `Nmap 7.95`
- `sẵn sàng tiếp nhận`
- `điều kiện tiên quyết cho khả năng bị ảnh hưởng`
- `điều kiện cần về mặt giao thức`
- `không gửi mã khai thác`
- `lặp lại toàn bộ`

All must be 0 in current operational/allowed wording after correction, except where old wording is quoted solely in an internal correction-history note; prefer removing it entirely.

Verify:
- no VULNERABLE verdict assigned to NSE04;
- no SAFE / NOT VULNERABLE / PATCHED;
- no FALSE NEGATIVE;
- no invented NTSTATUS;
- no cause invented for missing output;
- no local/remote signing reconciliation.

## 15. Git

Commit:

`fix(ch3): correct scenario2 presentation plan R2`

Push:

`feature/x7c0-ch3-scenario2-plan`

Do not merge.

## 16. Handoff

Return:

1. starting SHA;
2. local/remote R2 SHA;
3. modified file list;
4. before/after summary for all 7 reviewer issues;
5. screenshot decision (must remain 1 KEEP / 3 DROP);
6. Bảng 3.4 design summary;
7. NSE04 direct-observation vs classification audit;
8. UNPATCHED vs UNKNOWN audit;
9. Case B transition correction;
10. command-lineage correction;
11. measurement-label/internal-ID correction;
12. claim-map row count;
13. QA results;
14. clean git status.

Final state:

`X7C0_SCENARIO2_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Then STOP.

Do not open X7C1.
Do not write Section 3.3.
Do not open X7D.
Do not write Chapter 4.
