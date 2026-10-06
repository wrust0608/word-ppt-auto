# X7D0 EXTERNAL REVIEW R1 — CASE B PLAN

Date: 2026-10-06  
Branch: `feature/x7d0-ch3-caseb-plan`  
Executor R1 candidate: `90f821a4080639fd3e494a153a82359873585716`  
Verdict: **88/100 — REVISE_BLOCKING**

## 1. Executive finding

The overall Case B presentation design is strong and should be preserved:

- 2 H3;
- 1 compact Bảng 3.5;
- Hình 3.7 = after-local state;
- Hình 3.8 = protocol retest;
- before/action screenshots dropped from the main report;
- combined NSE04 screenshot kept only as optional;
- no Section 3.4 prose;
- no Case C result leakage;
- manifest/file-06 discrepancy correctly detected.

No structural redesign is required.

However, R1 contains several evidence-boundary regressions and one direct factual transcription error in Bảng 3.5. These must be corrected before user approval.

## 2. Score

| Category | Score |
|---|---:|
| Evidence coverage / staging audit | 20/20 |
| Structure / reader flow | 19/20 |
| Figure selection | 18/20 |
| Technical wording discipline | 15/20 |
| Claim/provenance fidelity | 16/20 |
| **Total** | **88/100** |

Blocker groups: **8 bounded corrections**.

## 3. What passes

### 3.1 Staging discrepancy — PASS

The plan correctly identifies that the manifest references:

`SMBv1_Remediation_06_Raw_Evidence.png`

while the canonical staged Case B folder contains only five screenshots.

Keep this handling exactly:

- 12 staged files;
- 5 staged screenshots;
- do not invent file 06;
- do not cite file 06;
- do not use `EXPECTED: 6 / ACTUAL: 6` as proof of six staged screenshots.

### 3.2 Main visual strategy — PASS

The preferred 2-figure strategy is academically sound:

- Hình 3.7: local state after intervention;
- Hình 3.8: remote protocol retest.

The choices avoid repeating:
- the earlier baseline image;
- a command-only action screenshot;
- a visually redundant MS17-010 no-verdict screenshot already conceptually represented in Section 3.3.

### 3.3 Core technical boundaries — PASS

The plan correctly preserves:

- `SMBv1 disabled != FS-SMB1 uninstalled`;
- `SMBv1 disabled != PATCHED`;
- `UNKNOWN != SAFE`;
- local `UNPATCHED` independent from remote `UNKNOWN`;
- no full SMB2/3 workload validation;
- no Case C result leakage;
- no Chapter 4 effectiveness/risk conclusion.

These must remain locked.

## 4. Blocking correction A — Case B retest does not contain SYN-ACK evidence

Bảng 3.5 currently presents the post-intervention TCP 445 state as:

`OPEN (Phản hồi syn-ack)`.

This is not supported by the Case B retest raw output.

Direct Case B `NSE-SMB-02_protocols.nmap` records:

`445/tcp open microsoft-ds`

but the command does not include `--reason` and the output does not print `syn-ack`.

Required correction:

- before/intervention baseline may retain the previously approved pre-intervention observation if clearly sourced to earlier Scenario evidence;
- Case B after/retest must say only:
  `445/tcp OPEN`.

Do not copy `syn-ack` from Scenario 2 into the Case B retest.

Also replace:

`Cổng 445/tcp tiếp tục mở và tiếp nhận kết nối qua mạng từ trạm Kali`

with the bounded form:

`Từ trạm Kali, TCP 445 được ghi nhận ở trạng thái OPEN trong phép đo lại.`

Keep:

`445 OPEN != vulnerable`.

## 5. Blocking correction B — dialect wording regresses to negotiation/support semantics

R1 repeatedly uses stronger wording:

- `đàm phán thành công`;
- `phản hồi đàm phán thành công`;
- `khả năng bắt tay giao thức`;
- `phương ngữ ... chấp thuận`;
- `SMB2/3 vẫn phản hồi`.

The direct output only establishes that `smb-protocols` listed four dialects in the retest.

Required wording:

`smb-protocols ghi nhận 2.0.2, 2.1, 3.0 và 3.0.2; NT LM 0.12 (SMBv1) không xuất hiện trong danh sách phương ngữ của phép đo lại.`

Use:
- `được ghi nhận`;
- `không xuất hiện trong danh sách phương ngữ của phép đo lại`.

Avoid:
- `đàm phán thành công`;
- `bắt tay thành công`;
- `hỗ trợ đầy đủ`;
- universal `hoàn toàn vắng mặt` outside the bounded measured list.

Claim `CB-C15` must also be narrowed:
the remaining dialects prove only that those values were recorded by `smb-protocols`, not a broader “successful handshake” claim.

## 6. Blocking correction C — point-in-time Running does not prove uninterrupted service

Bảng 3.5 currently says:

`Dịch vụ máy chủ không bị gián đoạn tiến trình`.

The direct evidence only records:

- `LanmanServer = Running` before;
- `LanmanServer = Running` after.

Two point-in-time observations do not prove there was no transient interruption between them.

Required wording:

`LanmanServer được ghi nhận ở trạng thái Running trước và sau can thiệp.`

Keep the boundary:

- this does not prove workload continuity;
- this does not prove zero downtime;
- this does not prove uninterrupted user sessions.

Similarly, internal claim wording should not say the service was “hoạt động bình thường”; use only `Running`.

## 7. Blocking correction D — `EnableSMB2Protocol=True` must stay a configuration fact

The student-facing table currently interprets:

`EnableSMB2Protocol=True`

as:

`Cấu hình máy chủ tiếp tục cho phép đàm phán các phương ngữ SMB2 và SMB3 hiện đại`.

This unnecessarily merges the local configuration property with the remote dialect result.

Required correction:

For the local row, state only:

`Thuộc tính EnableSMB2Protocol được ghi nhận True trước và sau can thiệp.`

The separate remote `smb-protocols` row may report the four dialects observed afterward.

Do not use the local flag to establish remote protocol negotiation.

## 8. Blocking correction E — local patch status must not be presented as 100% direct Case B evidence

The project lock allows Case B to retain local patch classification:

`UNPATCHED`.

However, the post-intervention screenshot does **not** display `srv.sys` or hotfix inventory.

The unchanged post-intervention patch statement comes from:
- the approved Section 3.1 local patch classification;
- Case B manifest metadata saying `srv.sys ... unchanged`;
- the fact that the recorded Case B action is a server-configuration command rather than patch installation.

Therefore:

1. keep `UNPATCHED` as an approved cross-reference;
2. do not claim the Case B screenshot directly proves `srv.sys` stayed unchanged;
3. do not claim “100% of 20 claims use direct/raw evidence” because `CB-C19` uses baseline + metadata lineage;
4. in Bảng 3.5, prefer:
   `UNPATCHED (theo trạng thái cục bộ đã khóa tại Mục 3.1; Case B không ghi nhận thao tác cài bản vá)`
   rather than repeating the exact driver version as if re-measured after intervention.

If exact `srv.sys` is retained internally, identify it as inherited baseline/metadata support, not a direct after-local screenshot result.

## 9. Blocking correction F — NSE04 UNKNOWN wording must preserve the same precision as Section 3.3

Claim `CB-C18` says the absence of a verdict:

`phản ánh giới hạn nhận diện của phép đo`.

This was explicitly removed in the reviewer-final Scenario 2 workflow because it assigns an explanation to the missing result.

Required wording:

`Phép đo lại không cung cấp phán quyết lỗ hổng khả dụng; vì vậy kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT. Nguyên nhân của việc không có đầu ra script khả dụng không được xác lập từ bộ bằng chứng hiện có. UNKNOWN != SAFE.`

Do not say:
- Nmap failed;
- scanner limitation caused it;
- SMBv1 probe was silenced;
- negotiation failed;
- false negative.

## 10. Blocking correction G — crop proposals need revision

### Hình 3.7

Current proposal:

`x=0, y=30, width=1280, height=730`

is poor for A4.

Independent visual inspection shows:
- PowerShell occupies only the left portion of the desktop;
- the proposed crop retains a large irrelevant desktop area on the right;
- it also retains a large blank console region below the useful output.

R2 must propose a tighter crop centered on the PowerShell result region.

Recommended starting rectangle to verify visually:

`x=0, y=30, width≈872, height≈310`

The exact R2 rectangle may vary slightly after direct visual verification, but it must:
- preserve the complete first wrapped command;
- preserve the SMB1/SMB2/signing row;
- preserve the FS-SMB1 result;
- preserve LanmanServer Running;
- preserve the final PowerShell prompt;
- remove the right-side desktop/watermark;
- remove unnecessary blank console area.

Do not create the crop in X7D0.

### Hình 3.8

Current proposal ends at approximately `y=384`.

Independent visual inspection indicates the returned shell prompt sits near the lower boundary.

Re-evaluate and leave safe bottom padding.

Recommended starting rectangle to verify:

`x=0, y=24, width=1280, height≈400`.

The final planned rectangle must preserve:
- full command;
- 445 open;
- all four dialects;
- `Nmap done`;
- complete returned shell prompt/cursor.

Do not silently cut the last prompt line.

## 11. Blocking correction H — remove unsupported/generalized language from plan/self-review

Correct the following classes of wording:

### Action screenshot
Replace:
`dấu nhắc lệnh trở lại bình thường`

with:
`dấu nhắc PowerShell xuất hiện trở lại; không có stdout hiển thị trong ảnh`.

Do not turn this into a success proof by itself.

The after-state is what confirms the intended configuration change.

### Figure-selection rhetoric
Remove phrases such as:
- `bằng chứng ... không thể bác bỏ`;
- `tác động ra mạng ngoài`;
- excessive `hoàn toàn` where a bounded observation is sufficient.

Use neutral academic wording.

### Case C transition
The current transition adds an unsupported operational narrative about administrators being unable to modify servers because of legacy applications/policies.

Remove that speculative scenario.

The transition only needs:

`Case B changes host-level SMB configuration; the next case examines a different control layer on the network path using a transparent firewall bridge.`

Do not justify it with hypothetical enterprise constraints unless separately sourced later.

## 12. Figure decisions remain locked for R2

Do not redesign the main selection:

- 01 Before = DROP;
- 02 Action = DROP;
- 03 After Local = KEEP -> tentative Hình 3.7;
- 04 NSE02 Protocols = KEEP -> tentative Hình 3.8;
- 05 combined NSE04 = OPTIONAL / DROP in the standard layout.

Only crop geometry and wording require correction.

## 13. Table design remains locked for R2

Keep:

- one Bảng 3.5;
- the before/after/retest comparison concept;
- 8-row concept if still A4-readable.

Correct the factual/wording issues above.

Do not add another table unless a concrete A4 readability failure is demonstrated.

## 14. Lecturer / defense-readiness assessment

The Case B design is close to strong thesis material because it visibly separates:

- server configuration;
- Windows feature installation;
- service process state;
- remote dialect observation;
- patch state;
- remote vulnerability-script verdict.

But an examiner could currently challenge the plan with:

- “Where is the SYN-ACK in the Case B raw output?”
- “Why do you call listed dialects a successful negotiation?”
- “Two Running snapshots do not prove no interruption—why does the table say that?”
- “Where was srv.sys re-measured after the intervention?”
- “Why does missing script output prove a scanner limitation?”
- “Why are you keeping half a desktop in Hình 3.7?”

R2 must remove these easy attack points.

## 15. Final gate

Verdict:

`X7D0_R1_REVISE_BLOCKING`

No X7D1.

After R2:
- perform final independent X7D0 external review;
- if PASS, ask user to approve X7D0;
- only after user approval does the previously defined WR1 -> WR2 Word-review sequence begin;
- X7D1 remains blocked until both Word checkpoints are approved.
