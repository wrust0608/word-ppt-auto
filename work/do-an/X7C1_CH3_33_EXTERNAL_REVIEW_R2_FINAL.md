# X7C1 EXTERNAL REVIEW R2 — FINAL

Date: 2026-10-06  
Branch: `feature/x7c1-ch3-scenario2-draft`  
Executor R2 candidate: `092280ba0036fe7bf6c487035de3164dcd2b13f3`  
Verdict: **99/100 — PASS / WAITING_FOR_USER_APPROVAL**

## 1. Executive finding

X7C1 R2 resolves all blocking issues identified in the R1 external review.

Section 3.3 is now technically bounded, evidence-led, and suitable for user approval.

No further executor correction round is required.

Blockers: **0**.

## 2. Score

| Category | Score |
|---|---:|
| Structure / experimental flow | 20/20 |
| Table / figure / crop implementation | 20/20 |
| UNKNOWN / UNPATCHED interpretation discipline | 20/20 |
| Evidence-bounded technical wording | 20/20 |
| Student-facing academic voice | 19/20 |
| **Total** | **99/100** |

## 3. R1 blockers — CLOSED

Confirmed corrected:

1. NSE-SMB-02 wording now reports only the five dialects recorded by `smb-protocols`; broader “support/negotiation” semantics were removed.
2. `[dangerous, but default]` is treated as literal Nmap annotation rather than a vulnerability conclusion.
3. NSE-SMB-03 now reports the remote signing observation directly and keeps it independent from local signing flags.
4. NSE-SMB-04 wording now separates:
   - visible/raw observation;
   - project classification;
   - interpretation boundary.
5. Completion wording is reduced to direct facts:
   - output reaches `Nmap done`;
   - shell prompt appears afterward;
   - no corresponding error message is displayed.
6. Missing-output cause is not invented.
7. Section 3.1 local `UNPATCHED` is referenced rather than re-derived with broader patch language.
8. Student-facing exploitation scope was simplified.
9. Self-review word-count and forbidden-term claims now match the final draft bytes.

## 4. Structure and presentation — PASS

Section 3.3 retains exactly:

- 1 H2;
- 2 H3;
- 1 Bảng 3.4;
- 1 Hình 3.6.

No NSE01/02/03 screenshot was added.

This remains the preferred thesis-reader geometry.

## 5. Independent text verification — PASS

Independent repository-byte checks on the R2 draft confirm:

- total words: **1,872**;
- prose words: **1,356**;
- H2 count: **1**;
- H3 count: **2**;
- Bảng 3.4 count: **1**;
- Hình 3.6 embed count: **1**.

The executor changed exactly the three authorized files:

- `CH3_33_SCENARIO2_DRAFT_R1.md`;
- `CH3_33_SCENARIO2_DRAFT_SELF_REVIEW_R1.md`;
- `CH3_33_SCENARIO2_CROP_MANIFEST_R1.md`.

The derived Hình 3.6 image was not regenerated.

## 6. NSE-SMB-01 — PASS

The section records:

- TCP 139 OPEN;
- TCP 445 OPEN;
- SYN-ACK;
- TTL 128.

The interpretation remains bounded:

`445 OPEN != vulnerable`.

The prose does not claim:
- successful SMB session;
- successful file sharing;
- authenticated access;
- MS17-010 vulnerability.

## 7. NSE-SMB-02 — PASS

The draft states only that `smb-protocols` records:

- `NT LM 0.12 (SMBv1)`;
- `2.0.2`;
- `2.1`;
- `3.0`;
- `3.0.2`.

The annotation `[dangerous, but default]` is reported as tool output.

The boundary remains:

`SMBv1 enabled != MS17-010 confirmed`.

No “necessary condition” / “prerequisite” theory is introduced.

## 8. NSE-SMB-03 — PASS

The direct remote result is preserved:

`Message signing enabled but not required`

for dialect 3.0.2.

The draft explicitly keeps this observation independent from local signing flags and does not generalize it to all dialects.

## 9. NSE-SMB-04 — PASS

### Direct observation

The draft correctly reports:

- the command uses `--script smb-vuln-ms17-010`;
- target is up;
- TCP 445 is OPEN;
- output reaches `Nmap done`;
- a shell prompt appears afterward;
- no `Host script results:` block appears;
- no corresponding error message is displayed in the recorded output.

### Project classification

`UNKNOWN / NO USABLE SCRIPT RESULT`

The draft correctly states that `UNKNOWN` is not a literal Nmap string.

### Interpretation boundary

The reason for missing usable script output is not established from the available evidence.

The following remain excluded:

- VULNERABLE verdict;
- SAFE verdict;
- NOT VULNERABLE verdict;
- PATCHED verdict;
- FALSE NEGATIVE;
- invented NTSTATUS;
- invented IPC$/authentication cause;
- claim that the script “failed”.

`UNKNOWN != SAFE` is preserved correctly.

## 10. Local UNPATCHED vs remote UNKNOWN — PASS

The public prose uses the approved cross-reference:

`Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa.`

The section keeps the two axes independent:

- local patch state = UNPATCHED;
- remote NSE result = UNKNOWN.

It does not convert:

`UNPATCHED -> VULNERABLE`

or:

`UNKNOWN -> SAFE/PATCHED`.

This is the most important defense boundary in Section 3.3 and is now clear enough for oral examination.

## 11. Figure / crop integrity — PASS

Locked source:

`Scenario2_NSE04_MS17010.png`

Source SHA-256:

`c970e56481a920061416949ea7543dcb96f1f2f99635dbe201131073202e14ac`

Derived Hình 3.6 SHA-256:

`8f7a343fe9ab100a187a5ab4fe85cac320e9350cf5d59df0c4d78e385a137bdc`

Crop:

`x=0, y=24, width=1280, height=330`

The image was visually inspected in the R1 external review and remains unchanged in R2.

The crop manifest wording now uses direct visible facts rather than “completed normally”.

## 12. Self-review fidelity — PASS

The prior R1 contradiction is closed.

R2 self-review now correctly states:

- prose count = 1,356;
- this lies within the R2 target 1,300–1,550;
- final forbidden-term checks are run against the final draft.

Independent checks confirm zero occurrences in the final student prose for the required banned strings, including:

- `hỗ trợ 5 phương ngữ`;
- `hỗ trợ đàm phán`;
- `Hỗ trợ đa phương ngữ`;
- `tính chất mất an toàn`;
- `phản ánh giới hạn của phép đo từ xa`;
- `được kích hoạt`;
- `gọi kịch bản chuyên biệt`;
- `trả về bình thường`;
- `kết thúc bình thường`;
- `ngưỡng cập nhật an toàn tối thiểu`;
- `các bản cập nhật thay thế tương ứng`;
- `Meterpreter`;
- `reverse shell`;
- `Baseline Case A`;
- `âm tính giả`;
- `false negative`;
- internal `S2-RAW`, `S2-IMG`, `S2-C`;
- `-Pn`;
- `STATUS_`;
- `IPC$`.

## 13. Case B transition — PASS

The transition is appropriately bounded:

- baseline + Scenario 1 + Scenario 2 form the pre-intervention observations;
- Case B changes one controlled factor: SMBv1 configuration;
- selected measurements are repeated:
  - protocol/dialect retest;
  - MS17-010 script retest.

The draft does not:
- call baseline “Case A”;
- say all measurements are repeated;
- reveal Case B result;
- claim mitigation effectiveness.

## 14. Lecturer / thesis-defense assessment

From an Information Security examiner perspective, Section 3.3 is now defensible.

The critical oral-defense question:

> “Máy chủ được phân loại cục bộ là UNPATCHED, vậy tại sao Nmap không báo VULNERABLE?”

can now be answered correctly from the report itself:

- local patch-state evidence and remote NSE output are different measurement axes;
- the local axis is UNPATCHED;
- the remote script produces no usable vulnerability verdict;
- therefore the remote result remains UNKNOWN;
- UNKNOWN is not SAFE;
- UNPATCHED is not automatically a remote VULNERABLE verdict.

The report no longer forces either measurement to overwrite the other.

The one-point deduction is editorial only and does not require another revision gate.

## 15. Final gate

External review: **PASS**.

Current state:

`X7C1_PASS_WAITING_FOR_USER_APPROVAL`

Do not integrate Section 3.3 yet.

Do not open X7D yet.

On explicit user approval:

1. mark Section 3.3 USER APPROVED / LOCKED;
2. explicitly integrate the completed Section 3.3 artifacts into `feature/ch3-integration`;
3. retain Bảng 3.4 and Hình 3.6;
4. verify next numbering remains Bảng 3.5 / Hình 3.7;
5. open the next Case B phase as an evidence/presentation-planning gate only;
6. do not write Section 3.4 prose until its plan passes independent external review + user approval.
