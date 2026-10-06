# X7C0 EXTERNAL REVIEW R2 — FINAL

Date: 2026-10-06  
Branch: `feature/x7c0-ch3-scenario2-plan`  
Executor R2 candidate: `41b17ab0242b59bb0810aac4cc1baa40fe6e8169`  
Verdict after bounded reviewer micro-fixes: **99/100 — PASS / WAITING_FOR_USER_APPROVAL**

## 1. Executive finding

X7C0 R2 resolves all blocking issues from the R1 external review.

The Scenario 2 Evidence & Presentation Plan is now suitable for user approval.

No further executor correction round is required.

Blockers: **0**.

## 2. Score

| Category | Score |
|---|---:|
| Evidence coverage / isolation | 20/20 |
| Academic structure / reader flow | 20/20 |
| Figure/table selection | 20/20 |
| Technical interpretation boundaries | 20/20 |
| Provenance / student-facing discipline | 19/20 |
| **Total** | **99/100** |

## 3. R1 blockers — CLOSED

Confirmed corrected:

1. `Baseline Case A` removed; baseline is not treated as a completed Case A experiment.
2. Case B transition now describes one controlled SMBv1 change and selected retests only.
3. NSE-SMB-01 is bounded to TCP 139/445 OPEN + SYN-ACK from the Kali vantage point.
4. SMBv1 is no longer described as a necessary/prerequisite condition for vulnerability.
5. NSE-SMB-04 direct observation is separated from the project classification `UNKNOWN / NO USABLE SCRIPT RESULT`.
6. Local `UNPATCHED` reuses the approved Section 3.1 formulation and remains independent from the remote result.
7. Provenance/terminology corrections are complete:
   - Nmap 7.99;
   - no unsupported causal explanation for `--privileged`;
   - NSE-SMB-01..04 treated as measurement labels;
   - internal IDs remain internal;
   - S2-C15 no longer characterizes internal exploit-payload behavior.

## 4. Locked presentation recommendation — PASS

Recommended structure for user approval:

- `3.3.1. Khảo sát điều kiện kết nối và thuộc tính giao thức SMB (NSE-SMB-01 đến NSE-SMB-03)`
- `3.3.2. Đánh giá dấu hiệu lỗ hổng MS17-010 và đối chiếu trạng thái bản vá (NSE-SMB-04)`

Recommended presentation:

- **Bảng 3.4** — one compact result-oriented table covering NSE-SMB-01..04;
- NSE01 screenshot — DROP;
- NSE02 screenshot — DROP;
- NSE03 screenshot — DROP;
- NSE04 screenshot — KEEP as tentative **Hình 3.6**;
- no second two-cell UNKNOWN-vs-UNPATCHED table.

This is the preferred geometry for a thesis reader because it removes repetition from Section 3.2 and gives the visually unique evidence slot to the MS17-010-specific measurement.

## 5. NSE-SMB-04 interpretation — PASS

The plan now distinguishes:

### Direct observation

- command/output records `--script smb-vuln-ms17-010`;
- target is up;
- TCP 445 is OPEN;
- recorded output reaches `Nmap done`;
- no `Host script results:` block appears;
- no corresponding error message is displayed in the recorded output.

### Project classification

`UNKNOWN / NO USABLE SCRIPT RESULT`

The plan explicitly states that `UNKNOWN` is not a literal Nmap string.

The following remain forbidden:

- SAFE;
- NOT VULNERABLE;
- VULNERABLE;
- PATCHED;
- FALSE NEGATIVE;
- invented NTSTATUS;
- invented cause for the absent script result.

`UNKNOWN != SAFE` remains locked.

## 6. Local patch state independence — PASS

Section 3.1 remains authoritative for the local patch-state classification:

`UNPATCHED`.

The Scenario 2 plan does not overwrite either axis:

- remote NSE result remains UNKNOWN;
- local patch state remains UNPATCHED.

No conversion is made from:

`UNPATCHED -> remote VULNERABLE`

or:

`UNKNOWN -> SAFE/PATCHED`.

## 7. Command lineage — PASS

Direct raw Scenario 2 evidence records Nmap 7.99.

The two provenance layers are kept separate:

- operator command/screenshot for NSE02/03/04 does not contain `--privileged`;
- Nmap-recorded argv does contain `--privileged`.

The plan does not claim a cause for that difference.

No `sudo`, `-Pn` or other option is inserted into the wrong provenance layer.

## 8. Reviewer bounded micro-fixes after R2

The reviewer applied final non-substantive precision edits:

1. replaced wording that said the target “supports/negotiates five dialects” with the direct statement that `smb-protocols` **recorded five dialects**;
2. replaced “scan completed normally” with the directly visible fact that output **reached the `Nmap done` line**;
3. removed language implying the absent NSE04 verdict itself establishes a cause or tool limitation; the plan now states the result is UNKNOWN and the reason for absent usable script output is not established.

These edits do not change:
- H3 structure;
- Bảng 3.4;
- image KEEP/DROP decision;
- crop rectangle;
- numbering;
- claim count;
- experimental result.

## 9. Figure/crop plan — PASS

Tentative Hình 3.6 source:

`Scenario2_NSE04_MS17010.png`

Independently verified SHA-256:

`c970e56481a920061416949ea7543dcb96f1f2f99635dbe201131073202e14ac`

Source dimensions:

`1280 × 800`

Approved provisional crop:

`x=0, y=24, width=1280, height=330`

No derived crop has been created in X7C0, which is correct.

## 10. Lecturer / thesis-defense assessment

From an Information Security examiner perspective, the plan is now strong and defensible:

- repeated port/dialect/signing observations are summarized instead of duplicated visually;
- the unique figure is reserved for the MS17-010-specific measurement;
- the report will visibly demonstrate that the dedicated script was invoked and no usable script-result block appeared;
- uncertainty is preserved rather than forced into a positive or negative vulnerability verdict;
- local patch-state evidence and remote script evidence are presented as separate measurement axes;
- the transition to Case B changes a controlled variable and does not prematurely evaluate mitigation effectiveness.

The one-point deduction is editorial only and does not require another gate.

## 11. Final gate

External review: **PASS**.

Current state:

`X7C0_PASS_WAITING_FOR_USER_APPROVAL`

Do not open X7C1 yet.

On explicit user approval:

1. mark X7C0 USER APPROVED / LOCKED;
2. lock the 2-H3 Section 3.3 structure;
3. lock Bảng 3.4;
4. lock NSE04 as Hình 3.6;
5. explicitly integrate the approved X7C0 planning artifacts into `feature/ch3-integration`;
6. update numbering so next available becomes Bảng 3.5 / Hình 3.7;
7. create X7C1 from the new integration HEAD;
8. X7C1 may create the approved Hình 3.6 crop + crop manifest and write Section 3.3 prose only;
9. X7D remains blocked until Section 3.3 prose passes external review + user approval.
