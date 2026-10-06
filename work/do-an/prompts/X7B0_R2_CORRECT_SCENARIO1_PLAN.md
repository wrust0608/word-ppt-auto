# X7B0 R2 — CORRECT SCENARIO 1 EVIDENCE/PRESENTATION PLAN

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7b0-ch3-scenario1-plan`  
R1 candidate: `4a9e40626a14b0ff60d9820df59037e0d5e237e7`

## 0. Objective

Correct the narrow blocking issues identified by:

`work/do-an/X7B0_SCENARIO1_PLAN_EXTERNAL_REVIEW_R1.md`

Do not redesign the approved direction.

Preserve:
- 2 proposed H3;
- 1 proposed Bảng 3.3;
- B4 screenshot DROP;
- B5 screenshot KEEP;
- B6 screenshot KEEP;
- B2/B3 handled without dedicated screenshots;
- all technical boundaries already correct.

Do **not** write Section 3.2 prose.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7b0-ch3-scenario1-plan
git pull --ff-only origin feature/x7b0-ch3-scenario1-plan
git status --short
git rev-parse HEAD
```

Read:
1. `work/do-an/X7B0_SCENARIO1_PLAN_EXTERNAL_REVIEW_R1.md`
2. the four R1 X7B0 artifacts;
3. `work/do-an/chapter3/evidence/scenario1/Scenario1_Run_Manifest.txt`;
4. B2–B6 `.nmap` raw files;
5. the three Scenario 1 screenshots;
6. `work/do-an/CHAPTER_2.md` Scenario 1 method table.

## 2. Allowed files to modify

Modify only:

- `work/do-an/CH3_32_SCENARIO1_FIGURE_SELECTION_R1.md`
- `work/do-an/CH3_32_SCENARIO1_PRESENTATION_PLAN_R1.md`
- `work/do-an/CH3_32_SCENARIO1_CLAIM_EVIDENCE_MAP_R1.md`
- `work/do-an/CH3_32_SCENARIO1_PLAN_SELF_REVIEW_R1.md`

Do not modify evidence, approved Section 3.1, truth matrix, numbering ledger, Chapter 2, or any later section.

## 3. Mandatory correction A — remove invented `-Pn`

There is no `-Pn` in the performed B4/B5/B6 operator lineage.

Exact recorded commands are:

### B4
`sudo nmap -sS -p 139,445 192.168.56.20 -T3 --max-retries 2 --reason -oA b4_smb_ports`

### B5
`sudo nmap -sS -sV --version-intensity 5 -p 139,445 192.168.56.20 -T3 --max-retries 2 -oA b5_smb_version`

### B6
`sudo nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities 192.168.56.20 -T3 --max-retries 2 -oA b6_smb_nse`

Requirements:
- search all four artifacts for `-Pn`;
- final count must be **0**;
- do not replace it with any other invented option;
- where exact syntax is not necessary, use method labels rather than partial commands.

## 4. Mandatory correction B — B4 MAC

Incorrect R1 value:
`08:00:27:1B:32:04`

Direct observed B4 value:
`08:00:27:55:71:CE`

Preferred fix:
- remove the MAC detail from the figure-selection narrative unless needed for a specific claim;
- if retained internally, use only `08:00:27:55:71:CE`.

Final search for `08:00:27:1B:32:04` must return **0**.

## 5. Mandatory correction C — make Bảng 3.3 result-oriented

Keep one table.

Recommended columns:
`Bước khảo sát | Phép đo | Kết quả ghi nhận | Diễn giải trực tiếp / giới hạn`

Use concise method labels rather than command snippets:

- B2: ARP host discovery on `192.168.56.0/24`
- B3: single-target ARP confirmation
- B4: TCP SYN scan of 139/445
- B5: Nmap service/version detection
- B6: Nmap NSE SMB profiling

Do not turn the table into a command log.

B3 public result should be:
`192.168.56.20 được ghi nhận ở trạng thái up`

Do not include `0.00034 s` in the student-facing table unless there is a justified analytical reason. Default: omit it.

## 6. B5 wording refinement

Preserve exactly:
`Microsoft Windows Server 2008 R2–2012`

Do not identify exact Windows Server 2012 R2 from B5.

Prefer:
`kết quả nhận diện dịch vụ/phiên bản của Nmap`

Avoid unnecessary mechanism claims such as `probe/banner`.

## 7. B6 wording refinement

Preserve the direct observations:

- `NT LM 0.12 (SMBv1)`
- `2.0.2`
- `2.1`
- `3.0`
- `3.0.2`
- `Message signing enabled but not required`
- recorded SMB2 capabilities only;
- `smb-os-discovery = no usable output`.

Prefer direct wording such as:
`Nmap smb-protocols ghi nhận ...`

Do not overstate this as vulnerability confirmation or as a stronger negotiation guarantee than the output supports.

## 8. Figure decision remains locked for R2

Do not redesign figure count in this correction.

Keep:
- B4 screenshot = DROP;
- B5 screenshot = KEEP, tentative Hình 3.4;
- B6 screenshot = KEEP, tentative Hình 3.5.

No new image.

No crop file yet.

For each recommended crop, add a **provisional reproducible crop rectangle** using source pixel coordinates:
`x, y, width, height`

The rectangle must preserve:
- full command line relevant to the evidence;
- all result lines required for the planned claim;
- enough context to show the output is from Nmap.

Do not crop the source evidence itself in X7B0.

## 9. Required self-review updates

Update the self-review to explicitly report:

- `-Pn` final search count = 0;
- wrong B4 MAC final search count = 0;
- B3 latency removed from public table design;
- B5 exact-OS overclaim count = 0;
- .56.100 identity remains UNKNOWN;
- MS17-010 verdict count = 0;
- no evidence bytes changed;
- no Section 3.2 prose created.

Do not self-declare PASS.

Final state:
`X7B0_SCENARIO1_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

## 10. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

Also run text checks for:
- `-Pn`
- `08:00:27:1B:32:04`
- `0.00034`
- exact-OS overclaim phrases.

## 11. Git

Commit:
`fix(ch3): correct scenario1 presentation plan R2`

Push:
`feature/x7b0-ch3-scenario1-plan`

Do not merge.

Stop after handoff and wait for final external review.
