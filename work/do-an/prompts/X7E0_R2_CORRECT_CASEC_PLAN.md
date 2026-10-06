# X7E0 R2 — CORRECT CASE C EVIDENCE & PRESENTATION PLAN

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7e0-ch3-casec-plan`  
R1 candidate: `fe4aef1a7cce7bf5782cb8d6c9d3edfa10f08a26`

## 0. Objective

Apply a bounded R2 correction to the Case C Pass-0 plan based on:

`work/do-an/X7E0_CASEC_PLAN_EXTERNAL_REVIEW_R1.md`

Do not redesign the section.

Keep:
- 2 H3;
- one Bảng 3.6;
- three primary figures (Hình 3.9–3.11);
- explicit rule-label conflict;
- timebase boundary;
- local-state provenance boundary.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7e0-ch3-casec-plan
git pull --ff-only origin feature/x7e0-ch3-casec-plan
git status --short
git rev-parse HEAD
```

The branch must contain the reviewer R1 and this prompt.

Read:
1. `work/do-an/X7E0_CASEC_PLAN_EXTERNAL_REVIEW_R1.md`
2. all four X7E0 R1 plan files
3. `EXPERIMENTAL_TRUTH_MATRIX.md`
4. `EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
5. `TIMEBASE_AND_CROSS_LAYER_LOCKS.md`

## 2. Allowed modifications

Modify only:

- `work/do-an/CH3_35_CASEC_FIGURE_SELECTION_R1.md`
- `work/do-an/CH3_35_CASEC_PRESENTATION_PLAN_R1.md`
- `work/do-an/CH3_35_CASEC_CLAIM_EVIDENCE_MAP_R1.md`
- `work/do-an/CH3_35_CASEC_PLAN_SELF_REVIEW_R1.md`

No other file may change.

## 3. Remove all causal explanations for the missing NSE04 verdict

Search all four files for wording equivalent to:

- `do cổng bị chặn`
- `do cổng 445 bị lọc`
- `script không thể tương tác`
- `không nhận được dữ liệu để thực thi`
- `Nmap tự động ẩn`
- `script failed because pfSense`

Replace with the direct evidence boundary:

`Phép đo NSE-SMB-04 ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT.`

And where useful:

`Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có.`

Keep:
`UNKNOWN != SAFE`.

Do not invent a script-internal cause.

## 4. Correct Bảng 3.6 baseline language

The Case C baseline did not mean "no firewall".

Windows Firewall baseline already existed.

Correct these concepts:

### Network path — before
Use:
`Host-Only baseline; chưa có pfSense trên đường thử nghiệm Kali → Windows`

Not:
`Không qua thiết bị lọc`.

### pfSense policy — before
Use:
`Chưa áp dụng ruleset pfSense Case C trên đường thử nghiệm`

Not:
`Cho phép kết nối mặc định`.

### Rule order — before
Use:
`Không áp dụng đối với pfSense Case C`

Not:
`Chưa có bộ lọc` as a universal claim.

### pfSense log — before
Use:
`Không có log pfSense tương ứng vì pfSense chưa nằm trên đường baseline`

Not:
`Chưa có tường lửa`.

Do not rewrite the historical Windows Firewall baseline.

## 5. Narrow topology/control wording

Replace universal wording such as:

`toàn bộ lưu lượng ... bắt buộc phải đi xuyên qua...`

with:

`Trong topology Case C, đường thử nghiệm Kali → Windows được bố trí đi qua bridge0 của pfSense.`

Do not claim every possible path in the host/network is controlled.

## 6. Narrow local Windows-state wording

Remove:
- `hoàn toàn không trải qua bất kỳ thay đổi`;
- `duy trì hoàn toàn không đổi`;
- continuous-uptime implications;
- lifetime binary-history implications.

Use:

`Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá trên Windows. Metadata cuối Case C ghi nhận SMB1=True, SMB2=True, LanmanServer=Running, các listener cục bộ 139/445 hiện diện và patch state UNPATCHED.`

If using `srv.sys`:
- numeric patch-comparison version = `6.3.9600.16421`;
- do not confuse it with display FileVersion string `6.3.9600.16384`.

Never write:
`dịch vụ SMBv1 chứa lỗ hổng vẫn tồn tại nguyên vẹn`.

Use:
- SMB1 local configuration remains True;
- patch classification remains UNPATCHED.

## 7. Replace strong causal language with bounded cross-layer comparison

Remove phrases equivalent to:
- `bằng chứng nhân quả liên tầng`;
- `xác lập mối quan hệ nhân quả`;
- `filtered bắt nguồn từ việc...`;
- `chứ không phải lỗi đường truyền ngẫu nhiên`.

Use:

`đối chiếu liên tầng`

and:

`Trong lượt Case C, Nmap ghi nhận TCP 139/445 ở trạng thái FILTERED, đồng thời log pfSense ghi nhận matching TCP SYN traffic từ Kali tới các cổng này bị Block trên đường pfSense.`

Preserve:
- rule-label conflict;
- no unified wall-clock claim.

## 8. Fix Hình 3.9 provisional crop

The R1 crop:

`x=20,y=370,w=455,h=240`

does not preserve the selected `CASE_C_KALI` area as claimed and risks clipping the rules-table title.

Re-inspect `pfSense_08_Rule_Order.png`.

Revise to a provisional crop approximately around:

`x≈15, y≈185–200, width≈470, height≈320–350`

Exact values may differ after visual inspection.

The crop must preserve:
- selected `CASE_C_KALI` context;
- `Rules (Drag to Change Order)`;
- full Block row;
- full Pass row.

Remove:
- insecure-password warning;
- footer.

No crop file is created yet.

## 9. Hình 3.10 / Hình 3.11 crop handling

### Hình 3.10
The current proposal is acceptable in principle.

Verify that the crop preserves:
- full Nmap command;
- Host is up / arp-response;
- both 139 and 445 FILTERED/no-response rows;
- MAC line;
- Nmap done.

### Hình 3.11
Because the source is 1359x17637:
- keep the current crop as PROVISIONAL only;
- explicitly require exact visual verification before X7E1 creates the derived crop;
- do not call the current y range "final".

The crop must preserve:
- log column headings needed for interpretation;
- matching Block rows for 139/445;
- visible conflicting Rule label if that column is used in the figure.

Do not crop away the conflict and then write as if it does not exist.

## 10. Remove nonexistent evidence-index / invented stable-ID registration claim

The current repo does not contain:

`CHAPTER_3_EVIDENCE_INDEX.md`.

Remove that reference.

Do not claim `C-IMG-08`–`C-IMG-11` are registered stable IDs unless an existing authoritative registry actually defines them.

Preferred simplification:
- evidence filename(s);
- evidence type:
  - direct raw;
  - direct visual;
  - metadata/lineage;
- maximum allowed wording;
- forbidden inference.

Internal IDs are optional and must not be invented.

Do not create a new index file.

## 11. Simplify rule-order explanation

Keep the direct observation:
- Block rule is displayed above Pass.

Remove:
- `bảo đảm` language;
- claims that moving it below would make it "completely ineffective";
- unnecessary firewall-theory tutorial prose.

The report result section needs the configured order, not a long theoretical derivation.

## 12. Preserve the accepted three-figure strategy

Primary:
- Hình 3.9 = `pfSense_08_Rule_Order.png`
- Hình 3.10 = `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`
- Hình 3.11 = `pfSense_10_Block_Log_CANONICAL.png`

OPTIONAL/DROP:
- `pfSense_04_Bridge.png`
- `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png`

Do not add a fourth standard figure.

Chapter 2 already contains the bridge topology.

## 13. Required searches

Search all four plan files for problematic concepts:

- `do cổng bị chặn`
- `do cổng 445`
- `không thể tương tác`
- `không nhận được dữ liệu`
- `tự động ẩn`
- `nhân quả`
- `bắt nguồn từ`
- `hoàn toàn không thay đổi`
- `tồn tại nguyên vẹn`
- `không qua thiết bị lọc`
- `cho phép kết nối mặc định`
- `chưa có tường lửa`
- `CHAPTER_3_EVIDENCE_INDEX`
- `C-IMG-08`
- `C-IMG-09`
- `C-IMG-10`
- `C-IMG-11`

Any remaining occurrence must be manually justified; preferably zero for the problematic forms.

## 14. Self-review updates

Update self-review to verify:

- 17 files inspected;
- 9 screenshots visually inspected;
- 3 KEEP / 2 OPTIONAL / 4 DROP unless a correction is explicitly justified;
- 2 H3;
- 1 Bảng 3.6;
- 3 main figures;
- corrected baseline wording;
- no NSE04 causal mechanism;
- no exact named-rule attribution;
- corrected Hình 3.9 crop proposal;
- Hình 3.11 crop remains provisional;
- no nonexistent index reference;
- no invented stable-ID registry claim;
- Windows-local state is point-in-time/provenance-bounded.

Do not self-declare external PASS.

## 15. QA

Run:

```bash
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

You may run `validate_project.py`, but do not modify infrastructure to make it pass.

## 16. Git

Commit:

`fix(ch3): correct Case C presentation plan R2`

Push:

`feature/x7e0-ch3-casec-plan`

Do not merge.

## 17. Handoff

Return:
1. starting reviewer HEAD;
2. final local/remote SHA;
3. changed files;
4. all R1 blockers and exact fixes;
5. corrected Bảng 3.6 baseline rows;
6. NSE04 cause-boundary audit;
7. local-state wording audit;
8. cross-layer wording audit;
9. revised Hình 3.9 crop proposal;
10. Hình 3.11 provisional-crop statement;
11. evidence-index/ID cleanup audit;
12. rule-label conflict audit;
13. QA;
14. clean git status.

Final state:

`X7E0_CASEC_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Then STOP.

Do not write Section 3.5 prose.
Do not create crops.
Do not open X7F.
Do not assemble Chapter 3.
Do not build Word.
