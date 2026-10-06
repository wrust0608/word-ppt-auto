# X7B1 EXTERNAL REVIEW R2 — FINAL

Date: 2026-10-06  
Branch: `feature/x7b1-ch3-scenario1-draft`  
Executor R2 candidate: `407fadb7d8b6413be6b2c67c6c8991f04f4a186c`  
Verdict after bounded reviewer micro-fixes: **99/100 — PASS / WAITING_FOR_USER_APPROVAL**

## 1. Executive finding

X7B1 R2 resolves all blocking issues identified in the R1 external review.

Section 3.2 now presents Scenario 1 as a coherent experimental result sequence and remains within the evidence actually observed.

No further executor correction round is required.

Blockers: **0**.

## 2. Score

| Category | Score |
|---|---:|
| Structure / reader flow | 20/20 |
| Table / figure implementation | 20/20 |
| Crop quality / provenance | 20/20 |
| Technical interpretation boundaries | 20/20 |
| Student-facing academic voice | 19/20 |
| **Total** | **99/100** |

## 3. R1 blockers — CLOSED

The following issues are confirmed corrected:

1. B3 now records only that the target remained online before subsequent measurements.
2. B4 is limited to TCP 139/445 observed OPEN + SYN-ACK from the Kali vantage point.
3. The generalized "safe if patched" sentence was removed.
4. Remote `smb2-security-mode` is explicitly independent from local signing flags.
5. B5 wording no longer uses a universal impossibility claim.
6. The transition to 3.3 no longer promises a definitive MS17-010 verdict.
7. X7B0 B5/B6 source SHA metadata now matches actual repository bytes.
8. The self-review claim mapping is realigned to approved `S1-C01..S1-C13`.

## 4. Structure and presentation — PASS

Locked Section 3.2 structure remains:

- `3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB`
- `3.2.1. Khảo sát trạm mạng và trạng thái mở cổng dịch vụ SMB`
- `3.2.2. Nhận diện phiên bản dịch vụ và đặc tính giao thức SMB`

Locked presentation remains:

- Bảng 3.3 only;
- Hình 3.4 from B5;
- Hình 3.5 from B6;
- no B2/B3/B4 screenshot.

This remains the preferred thesis-reader geometry.

## 5. Evidence fidelity — PASS

Independent comparison against B2–B6 raw outputs confirms:

- B2 observed four hosts:
  `.56.1`, `.56.10`, `.56.20`, `.56.100`;
- `.56.100` remains UNKNOWN identity;
- B3 only establishes target `.56.20` as up;
- B4 records TCP 139/445 OPEN with SYN-ACK, TTL 128;
- B5 records the range `Microsoft Windows Server 2008 R2–2012`;
- B6 records dialects `NT LM 0.12`, `2.0.2`, `2.1`, `3.0`, `3.0.2`;
- B6 records `Message signing enabled but not required`;
- B6 capabilities remain bounded to values printed by Nmap;
- `smb-os-discovery` has no usable output.

Scenario 1 does not produce an MS17-010 verdict.

## 6. Figure/crop integrity — PASS

Previously verified repository-byte SHA-256 values remain the accepted provenance:

Source:
- B5: `05699e248fa66ab224adc6809fb057a282d86c29c3ce2851823e07bd874f6466`
- B6: `b5b236cbe695b530b44e0af592f010f1f49bef9f5da427b9958fd9020bd651f8`

Derived:
- Hình 3.4: `513f3356792eec5f449003a43f5fa8520a7fda94d8e10d4edbb6ef62fc064964`
- Hình 3.5: `45faf0f03f57ce35707e1825f555fcbb6ad5e9fdee5daac7f849351ec2360a66`

Crop rectangles remain:
- Hình 3.4: `(0, 24, 1280, 310)`
- Hình 3.5: `(0, 24, 1280, 710)`

Both derived figures were visually inspected in the prior external review and preserve the required command/result context.

## 7. Reviewer bounded micro-fixes after R2

The reviewer applied four non-substantive wording refinements to improve defense-readiness:

1. `SMB Direct Hosted (TCP 445)` was replaced with the evidence-aligned label `Microsoft-DS (TCP 445)`, avoiding confusion with SMB Direct/RDMA terminology.
2. A general statement about Nmap capability was narrowed to `Kết quả Nmap trong lần đo này...`.
3. The SMBv1 paragraph now reports the actual Nmap annotation `[dangerous, but default]` directly rather than paraphrasing it into a broader security-risk statement.
4. `smb-os-discovery hoàn toàn không trả về...` was narrowed to `không trả về...`.

These edits do not change any claim, evidence interpretation, table, figure, numbering or experimental result.

## 8. Lecturer / thesis-defense assessment

From an Information Security examiner perspective, Section 3.2 is now defensible:

- the reader sees the B2→B6 progression without being forced through command logs;
- the distinction between host-up, port-open, service fingerprint and protocol profile is clear;
- B5 demonstrates the limitation of remote fingerprinting instead of overstating OS identification;
- B6 presents protocol evidence while keeping SMBv1 separate from MS17-010 confirmation;
- local and remote signing observations are kept as independent facts;
- negative output from `smb-os-discovery` is reported transparently;
- the transition to Scenario 2 motivates the next experiment without promising an outcome.

The remaining one-point deduction is editorial rather than technical and does not require another revision gate.

## 9. Final gate

External review: **PASS**.

Current state:

`X7B1_PASS_WAITING_FOR_USER_APPROVAL`

Do not integrate Section 3.2 yet.

Do not open X7C yet.

On explicit user approval:
1. mark Section 3.2 USER APPROVED / LOCKED;
2. explicitly integrate the completed Section 3.2 artifacts into `feature/ch3-integration`;
3. retain Bảng 3.3 and Hình 3.4–3.5;
4. verify next numbering remains Bảng 3.4 / Hình 3.6;
5. create X7C0 from the new integration HEAD;
6. X7C0 must be **Scenario 2 Evidence & Presentation Plan ONLY**;
7. do not write Section 3.3 prose until the X7C0 plan passes external review + user approval.
