# X7D0 R2 — CORRECT CASE B EVIDENCE/PRESENTATION PLAN

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7d0-ch3-caseb-plan`  
R1 candidate: `90f821a4080639fd3e494a153a82359873585716`

## 0. Objective

Correct only the bounded issues identified in:

`work/do-an/X7D0_CASEB_PLAN_EXTERNAL_REVIEW_R1.md`

Do not redesign the Case B section.

Preserve:
- 2 proposed H3;
- 1 Bảng 3.5;
- 03 After Local KEEP;
- 04 NSE02 Protocols KEEP;
- 01 Before DROP;
- 02 Action DROP;
- 05 combined NSE04 OPTIONAL / DROP;
- no Section 3.4 prose;
- no presentation crops created.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7d0-ch3-caseb-plan
git pull --ff-only origin feature/x7d0-ch3-caseb-plan
git status --short
git rev-parse HEAD
```

Read first:

1. `work/do-an/X7D0_CASEB_PLAN_EXTERNAL_REVIEW_R1.md`
2. all four X7D0 R1 plan artifacts;
3. Case B raw `.nmap` files;
4. all five Case B screenshots;
5. `SMBv1_Remediation_Run_Manifest.txt`;
6. approved Sections 3.1 and 3.3 for the UNPATCHED / UNKNOWN cross-reference.

## 2. Allowed files to modify

Modify only:

- `work/do-an/CH3_34_CASEB_FIGURE_SELECTION_R1.md`
- `work/do-an/CH3_34_CASEB_PRESENTATION_PLAN_R1.md`
- `work/do-an/CH3_34_CASEB_CLAIM_EVIDENCE_MAP_R1.md`
- `work/do-an/CH3_34_CASEB_PLAN_SELF_REVIEW_R1.md`

Do not modify:
- source evidence;
- approved Sections 3.1–3.3;
- numbering ledger;
- truth matrix;
- R3 locks;
- Chapter 2;
- integration branch.

## 3. Fix TCP 445 Case B retest

Direct Case B raw only prints:

`445/tcp open microsoft-ds`

It does **not** print `syn-ack`.

Therefore:

- remove post-intervention `syn-ack` from Bảng 3.5;
- do not say Case B 445 “accepted a connection”;
- use:
  `Từ trạm Kali, TCP 445 được ghi nhận ở trạng thái OPEN trong phép đo lại.`

The earlier pre-intervention value may reference approved Scenario evidence if clearly identified as the earlier measurement.

Keep:

`445 OPEN != vulnerable`.

## 4. Restore direct dialect wording

Remove/rewrite:

- `đàm phán thành công`;
- `phản hồi đàm phán thành công`;
- `khả năng bắt tay giao thức`;
- universal `hoàn toàn vắng mặt`;
- statements that the target “supports” more than the output directly establishes.

Use:

`Kịch bản smb-protocols ghi nhận 2.0.2, 2.1, 3.0 và 3.0.2; NT LM 0.12 (SMBv1) không xuất hiện trong danh sách phương ngữ của phép đo lại.`

For CB-C15 use:

`Việc các phương ngữ 2.0.2, 2.1, 3.0 và 3.0.2 được ghi nhận trong phép đo lại không chứng minh toàn bộ workload SMB2/3 đã được kiểm chứng.`

Do not call this a successful handshake.

## 5. Correct LanmanServer continuity wording

Remove:

`Dịch vụ máy chủ không bị gián đoạn tiến trình`

and any equivalent no-interruption claim.

Use:

`LanmanServer được ghi nhận ở trạng thái Running trước và sau can thiệp.`

Boundary:

- two point-in-time states do not prove zero downtime;
- do not claim no transient interruption;
- do not claim user/application session continuity.

In claim map, replace `hoạt động bình thường` with `được ghi nhận ở trạng thái Running`.

## 6. Keep local SMB2 property separate from remote dialect result

For the `EnableSMB2Protocol` row:

Do not say:

`tiếp tục cho phép đàm phán SMB2/SMB3`.

Use only:

`Thuộc tính EnableSMB2Protocol được ghi nhận True trước và sau can thiệp.`

The remote dialect row separately reports 2.0.2 / 2.1 / 3.0 / 3.0.2.

Do not use the local flag to prove the remote result.

## 7. Correct patch-state provenance

Keep the approved project fact:

`local patch state remains UNPATCHED`.

But do not represent it as a direct post-intervention screenshot measurement.

Preferred Bảng 3.5 wording:

Before:
`UNPATCHED (Mục 3.1)`

After:
`UNPATCHED — Case B không ghi nhận thao tác cài bản vá`

Limit:

`Đây là trạng thái cục bộ được kế thừa từ mốc đã khóa và metadata run lineage; ảnh After Local không trực tiếp hiển thị srv.sys/hotfix.`

Do not claim:
- the after-local screenshot proves the driver version;
- 100% of claims use direct/raw Case B evidence.

Update the self-review/direct-evidence percentage statement accordingly.

For CB-C19 identify evidence layers honestly:
- approved baseline local evidence;
- Case B manifest metadata;
- action scope.

Do not overstate metadata as raw evidence.

## 8. Correct NSE04 UNKNOWN wording

Replace any wording equivalent to:

`absence reflects a limitation of remote detection`

with:

`Phép đo lại không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT. Nguyên nhân của việc không có đầu ra script khả dụng không được xác lập từ bộ bằng chứng hiện có. UNKNOWN != SAFE.`

Do not say:
- false negative;
- scanner limitation caused it;
- SMBv1 probe silenced;
- negotiation failed;
- script failed;
- SAFE / NOT VULNERABLE / PATCHED.

## 9. Revise Hình 3.7 crop proposal

Do not create the crop.

The current `1280×730` crop is rejected because it retains large irrelevant desktop/blank regions.

Visually re-evaluate the screenshot and propose a tight rectangle around the PowerShell evidence.

Start from approximately:

`x=0, y=30, width=872, height=310`

Adjust only if direct visual verification requires a few pixels.

The final proposed crop must preserve:

- complete wrapped `Get-SmbServerConfiguration` command;
- SMB1/SMB2/signing output row;
- `Get-WindowsFeature FS-SMB1` result;
- `Get-Service LanmanServer` result;
- final PowerShell prompt.

It should remove:
- title bar;
- right-side desktop / Windows watermark;
- taskbar;
- large blank PowerShell area below the evidence.

Record exact source SHA/dimensions and final provisional rectangle.

## 10. Revise Hình 3.8 crop proposal

Do not create the crop.

The current crop ending around y=384 risks clipping the returned shell prompt.

Re-evaluate visually.

Start from approximately:

`x=0, y=24, width=1280, height=400`.

The final proposal must preserve:

- full operator command;
- host/445 state;
- all four dialects;
- `Nmap done`;
- complete shell prompt/cursor.

Leave safe lower padding.

## 11. Remove unsupported/generalized rhetoric

### Action screenshot

Replace:

`dấu nhắc lệnh trở lại bình thường`

with:

`dấu nhắc PowerShell xuất hiện trở lại; không có stdout hiển thị trong ảnh.`

The action screenshot alone does not prove success; the after-state records the configuration result.

### Figure-selection prose

Remove/rewrite:
- `không thể bác bỏ`;
- `đã tác động ra mạng ngoài`;
- excessive `hoàn toàn`;
- other persuasive rhetoric not needed for technical reporting.

### Case C transition

Remove the hypothetical enterprise story about administrators being unable to modify servers due to legacy applications/policies.

Use only:

`Case B thay đổi cấu hình giao thức ở máy chủ; Case C tiếp tục khảo sát một lớp kiểm soát khác trên đường truyền mạng bằng pfSense Transparent Bridge.`

Do not reveal Case C results.

## 12. Preserve main figure decisions

Keep exactly:

- 01 Before = DROP
- 02 Action = DROP
- 03 After Local = KEEP -> tentative Hình 3.7
- 04 NSE02 Protocols = KEEP -> tentative Hình 3.8
- 05 combined NSE04 = OPTIONAL / DROP

Do not introduce a new figure.

## 13. Preserve Bảng 3.5 concept

Keep one table only.

Retain the 8-row comparison concept if it remains readable.

Correct:
- post 445 SYN-ACK;
- LanmanServer no-interruption wording;
- local SMB2 vs remote dialect semantics;
- patch-state provenance;
- dialect wording;
- UNKNOWN wording.

Do not add raw command strings to the student-facing table.

## 14. Self-review truthfulness

Rebuild self-review after final edits.

It must accurately report:

- 12 staged files;
- 5 screenshots;
- file 06 discrepancy;
- 2 KEEP / 1 OPTIONAL / 2 DROP;
- 2 H3;
- 1 table;
- 2 figures;
- claim count;
- which claims use direct/raw evidence vs approved baseline/metadata;
- no unsupported 100% direct/raw claim;
- no Case B SYN-ACK after claim;
- no “successful negotiation” wording;
- no no-interruption claim;
- no scanner-cause claim for UNKNOWN;
- no Case C result leakage.

Do not self-declare external PASS.

Final executor state:

`X7D0_CASEB_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

## 15. Required searches

Search all four plan artifacts for:

- `đàm phán thành công`
- `phản hồi đàm phán thành công`
- `khả năng bắt tay giao thức`
- `không bị gián đoạn tiến trình`
- `hoạt động bình thường`
- `tiếp nhận kết nối qua mạng`
- `phản ánh giới hạn nhận diện`
- `SMBv1 probe silenced`
- `không thể bác bỏ`
- `đã tác động ra mạng ngoài`

In allowed/operational wording, counts must be 0.

Also verify:
- no post-Case-B `syn-ack`;
- no SAFE / NOT VULNERABLE / PATCHED verdict;
- no false negative;
- no invented NTSTATUS / IPC$ / Couldn't negotiate SMBv1;
- no full workload continuity claim;
- no feature-uninstall claim;
- no reboot claim;
- no Case C result;
- no Chapter 4 effectiveness/risk conclusion.

Historical quoted forbidden phrases in a correction-history note should preferably be removed rather than retained.

## 16. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

Confirm:
- no Section 3.4 draft exists;
- no crop file exists;
- source evidence unchanged;
- only the four allowed plan files changed.

## 17. Git

Commit:

`fix(ch3): correct Case B presentation plan R2`

Push:

`feature/x7d0-ch3-caseb-plan`

Do not merge.

## 18. Handoff

Return:

1. starting SHA;
2. local/remote R2 SHA;
3. modified file list;
4. before/after summary for all reviewer blocker groups;
5. final screenshot decision;
6. final H3/table/figure design;
7. corrected TCP 445 audit;
8. corrected dialect wording audit;
9. LanmanServer point-in-time audit;
10. local SMB2-vs-remote-dialects audit;
11. UNPATCHED provenance audit;
12. UNKNOWN wording audit;
13. final crop proposals for Hình 3.7 and Hình 3.8;
14. file-06 discrepancy audit;
15. self-review truthfulness audit;
16. required-search results;
17. QA results;
18. clean git status.

Final state:

`X7D0_CASEB_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Then STOP.

Do not open X7D1.
Do not write Section 3.4.
Do not start WR1/WR2 yet.
Do not open X7E.
Do not write Chapter 4.
