# X7D0 EXTERNAL REVIEW R2 — FINAL

Date: 2026-10-06  
Branch: `feature/x7d0-ch3-caseb-plan`  
Executor R2 candidate: `492b90fcdf7f31b1e4e10f04d3a818f69d0429ef`  
Verdict: **99/100 — PASS / WAITING_FOR_USER_APPROVAL**

## 1. Executive finding

X7D0 R2 resolves all blocking issues from the R1 external review.

The Case B evidence/presentation plan is now suitable for user approval.

No further executor correction round is required.

Blockers: **0**.

## 2. Score

| Category | Score |
|---|---:|
| Evidence/staging coverage | 20/20 |
| Before/action/after structure | 20/20 |
| Table/figure selection | 20/20 |
| Technical interpretation boundaries | 20/20 |
| Academic/editorial precision | 19/20 |
| **Total** | **99/100** |

## 3. Scope verification — PASS

Independent diff check confirms R2 modifies exactly the four authorized planning files:

- `CH3_34_CASEB_CLAIM_EVIDENCE_MAP_R1.md`
- `CH3_34_CASEB_FIGURE_SELECTION_R1.md`
- `CH3_34_CASEB_PLAN_SELF_REVIEW_R1.md`
- `CH3_34_CASEB_PRESENTATION_PLAN_R1.md`

No Section 3.4 prose or presentation crop was created.

## 4. R1 blockers — CLOSED

Confirmed corrected:

1. post-intervention Case B TCP 445 no longer carries unsupported `syn-ack`;
2. dialect wording is reduced to values recorded by `smb-protocols`;
3. `LanmanServer=Running` is treated as point-in-time state, not proof of uninterrupted operation;
4. local `EnableSMB2Protocol=True` is kept separate from the remote dialect result;
5. local `UNPATCHED` provenance is stated honestly as inherited approved baseline + run metadata/action scope, not direct After Local screenshot evidence;
6. remote MS17-010 result remains `UNKNOWN / NO USABLE SCRIPT RESULT` without assigning a cause;
7. Hình 3.7 and Hình 3.8 crop proposals were tightened and visually bounded;
8. speculative/rhetorical wording and the unsupported enterprise narrative in the Case C transition were removed.

## 5. Main presentation geometry — PASS

Locked recommendation for user approval:

### Section structure
- `3.4.1. Thực thi vô hiệu hóa giao thức SMBv1 và kiểm tra trạng thái máy chủ cục bộ`
- `3.4.2. Đo đạc lại kịch bản NSE từ xa và đối chiếu kết quả đa tầng`

### Table
- one **Bảng 3.5** only:
  `So sánh cấu hình và kết quả đo đạc trước và sau khi vô hiệu hóa SMBv1 (Case B)`

### Figure decision
- 01 Before = DROP
- 02 Action = DROP
- 03 After Local = KEEP -> tentative **Hình 3.7**
- 04 NSE02 Protocols = KEEP -> tentative **Hình 3.8**
- 05 combined NSE04 = OPTIONAL / DROP in standard layout

This is the preferred thesis-reader geometry.

## 6. Bảng 3.5 — PASS

The table correctly separates:

- SMB1 configuration: True -> False;
- SMB2 configuration: True -> True;
- FS-SMB1: Installed -> Installed;
- LanmanServer: Running before / Running after;
- TCP 445: earlier OPEN observation / Case B retest OPEN;
- dialect list: prior five values / Case B four recorded values;
- MS17 remote classification: UNKNOWN -> UNKNOWN;
- local patch classification: UNPATCHED -> UNPATCHED with explicit provenance boundary.

Important corrections now present:

- no Case B post-retest SYN-ACK is claimed;
- `EnableSMB2Protocol=True` is not used as proof of remote protocol negotiation;
- Running before/after is not converted into a zero-downtime statement;
- patch-state inheritance is disclosed.

## 7. Remote protocol retest — PASS

Direct Case B raw output records:

- host up;
- `445/tcp open microsoft-ds`;
- `smb-protocols` lists:
  - 2.0.2
  - 2.1
  - 3.0
  - 3.0.2
- `NT LM 0.12 (SMBv1)` does not appear in the retest list.

The plan no longer calls this a successful negotiation or successful handshake.

The interpretation remains bounded:

- these four dialect values were recorded;
- SMBv1 does not appear in the measured retest list;
- this does not establish full SMB2/3 workload validation.

## 8. Local post-intervention state — PASS

Hình 3.7 plan is evidence-bounded:

- `EnableSMB1Protocol=False`;
- `EnableSMB2Protocol=True`;
- `FS-SMB1=Installed`;
- `LanmanServer=Running`.

The plan correctly preserves:

`SMBv1 disabled != FS-SMB1 uninstalled`

and:

`SMBv1 disabled != PATCHED`.

The point-in-time `Running` state is not treated as proof of zero downtime or uninterrupted application sessions.

## 9. MS17-010 retest — PASS

Direct observation remains:

- target up;
- TCP 445 OPEN;
- output reaches `Nmap done`;
- no `Host script results:` block;
- no corresponding error message displayed in recorded output.

Project classification remains:

`UNKNOWN / NO USABLE SCRIPT RESULT`

The plan correctly states:

- the cause for absent usable script output is not established;
- `UNKNOWN != SAFE`;
- no FALSE NEGATIVE;
- no invented NTSTATUS/IPC$;
- no `SMBv1 probe silenced` causal claim;
- no SAFE / NOT VULNERABLE / PATCHED conclusion.

## 10. UNPATCHED provenance — PASS

The plan now distinguishes evidence layers correctly.

The After Local screenshot itself does not show `srv.sys` or hotfix inventory.

The Case B report may retain:

`UNPATCHED`

because it is grounded in:
- the approved local patch state from Section 3.1;
- run metadata stating no patch-state change / unchanged `srv.sys`;
- the intervention scope, which records an SMB server configuration change rather than patch installation.

The self-review no longer claims that all claims are direct/raw Case B observations.

## 11. Crop plans — PASS

### Hình 3.7

Source:
`SMBv1_Remediation_03_After_Local.png`

Proposed crop:
`x=0, y=30, width=872, height=310`

Independent visual review confirms this is a substantially better A4 crop than R1 because it removes:
- the right-side desktop/watermark;
- taskbar;
- large blank console area.

It preserves the required PowerShell command/output blocks and final prompt.

### Hình 3.8

Source:
`SMBv1_Remediation_04_NSE02_Protocols.png`

Proposed crop:
`x=0, y=24, width=1280, height=400`

Independent visual review confirms this preserves:
- full command;
- TCP 445 state;
- all four dialects;
- `Nmap done`;
- returned shell prompt/cursor with safe lower padding.

No crop is created at X7D0, which is correct.

## 12. File-06 discrepancy — PASS

The plan correctly records:

- manifest references `SMBv1_Remediation_06_Raw_Evidence.png`;
- that file is absent from the staged Case B evidence folder;
- canonical staged total = 12 files;
- staged screenshots = 5.

The missing file is not invented, restored, or cited as evidence.

## 13. Case C transition — PASS

The transition is now appropriately narrow:

`Case B changes host-level SMB configuration; Case C examines a different control layer on the network path using pfSense Transparent Bridge.`

No Case C result is leaked.

No comparative effectiveness conclusion is made.

## 14. Lecturer / thesis-defense assessment

From an Information Security examiner perspective, the Case B plan is now defensible.

A reader can distinguish:

- protocol configuration change;
- Windows feature installation state;
- point-in-time service state;
- remote dialect observation;
- local patch state;
- remote vulnerability-script classification.

The important defense questions now have clean answers:

- disabling SMBv1 does not uninstall FS-SMB1;
- disabling SMBv1 does not patch MS17-010;
- seeing SMB2/3 dialects does not prove full application/workload continuity;
- TCP 445 staying OPEN does not imply vulnerability;
- remote UNKNOWN does not imply SAFE;
- local UNPATCHED does not force a remote VULNERABLE verdict.

The one-point deduction is editorial only and does not require another revision gate.

## 15. Final gate

External review: **PASS**.

Current state:

`X7D0_PASS_WAITING_FOR_USER_APPROVAL_WORD_REVIEW_DEFERRED`

Do not integrate X7D0 yet.

Do not start WR1/WR2 yet.

Do not open X7D1.

On explicit user approval:

1. mark X7D0 USER APPROVED / LOCKED;
2. explicitly integrate approved X7D0 plan artifacts into `feature/ch3-integration`;
3. lock Bảng 3.5 and Hình 3.7–3.8 numbering allocation for Case B planning;
4. then begin the previously approved Word-checkpoint sequence:
   - WR1 Demo 1 review snapshot;
   - independent review + user approval;
   - WR2 Demo 2 review snapshot;
   - independent review + user approval;
5. only after WR1 + WR2 approval may X7D1 Section 3.4 prose open.
