# X7B1 EXTERNAL REVIEW R1 — SECTION 3.2 SCENARIO 1

Date: 2026-10-06  
Branch: `feature/x7b1-ch3-scenario1-draft`  
Executor R1 candidate: `2bff0dead870f838284a02eea148f4c468263584`  
Verdict: **88/100 — REVISE_BLOCKING**

## 1. Executive finding

The draft is academically well structured and the approved presentation geometry has been implemented correctly:

- exactly 1 H2 + 2 H3;
- exactly 1 Bảng 3.3;
- exactly 2 figures;
- B2/B3/B4 are not turned into screenshot spam;
- B5/B6 crops are clear and traceable;
- no Scenario 2 outcome is leaked;
- no Chapter 4 recommendation/risk section is introduced.

However, the prose is not yet ready for user approval because several sentences go beyond what the direct evidence supports or blur the locked local-vs-remote boundary. There is also an internal provenance inconsistency inherited from X7B0 and a claim-map self-review indexing error.

No redesign is required. R2 must be a bounded correction.

## 2. Score

| Category | Score |
|---|---:|
| Structure / reader flow | 20/20 |
| Table / figure implementation | 20/20 |
| Crop quality / traceability | 20/20 |
| Technical wording discipline | 15/20 |
| Internal traceability / provenance | 13/20 |
| **Total** | **88/100** |

Blocking corrections: **5 bounded issues**.

## 3. What passes

### 3.1 Structure and thesis-reader flow — PASS

The two-H3 structure works well:

- 3.2.1 moves from host discovery to target confirmation to remote port state;
- 3.2.2 moves from service/version fingerprint to SMB protocol profile.

This reads as an experimental result sequence rather than a command transcript.

### 3.2 Bảng 3.3 — PASS WITH WORDING LOCK

The table is compact, result-oriented and suitable for A4.

The reviewer-final table wording from X7B0 is preserved correctly.

Do not redesign the table in R2.

### 3.3 Figures and crops — PASS

Independent visual inspection confirms both derived figures are readable and preserve the required evidence.

Actual SHA-256 independently recomputed from the repository bytes:

- B5 source `Scenario1_B5_SMB_Version.png`:
  `05699e248fa66ab224adc6809fb057a282d86c29c3ce2851823e07bd874f6466`
- B6 source `Scenario1_B6_SMB_NSE_A.png`:
  `b5b236cbe695b530b44e0af592f010f1f49bef9f5da427b9958fd9020bd651f8`
- Hình 3.4 derived:
  `513f3356792eec5f449003a43f5fa8520a7fda94d8e10d4edbb6ef62fc064964`
- Hình 3.5 derived:
  `45faf0f03f57ce35707e1825f555fcbb6ad5e9fdee5daac7f849351ec2360a66`

The crop manifest R1 uses these actual values and is correct.

Approved rectangles are implemented correctly:

- Hình 3.4: `(0, 24, 1280, 310)`
- Hình 3.5: `(0, 24, 1280, 710)`

No crop redesign is required.

## 4. Blocking correction A — B3 and B4 prose overclaim

### B3

Current prose says the ARP check:

`bảo đảm tính sẵn sàng trước khi triển khai các phép đo tiếp theo`

The direct evidence proves only that the target was observed `up` at that step.

Required wording direction:

`xác nhận mục tiêu vẫn đang trực tuyến trước khi thực hiện các phép đo tiếp theo`

Do not use:
- bảo đảm;
- sẵn sàng tiếp nhận kết nối;
- service availability.

### B4

Current prose says:

`dịch vụ chia sẻ tệp trên máy chủ mục tiêu hoàn toàn có thể tiếp cận được qua đường truyền mạng nội bộ`

This moves from TCP port evidence to an application-level service conclusion and uses an unnecessary absolute.

Direct evidence supports only:

- TCP 139/445 observed `OPEN`;
- SYN-ACK returned;
- observation from the Kali vantage point.

Required wording direction:

`Từ góc nhìn của trạm Kali, hai cổng TCP 139 và 445 của mục tiêu được ghi nhận ở trạng thái OPEN và phản hồi SYN-ACK.`

Keep:
`445 OPEN != vulnerable`.

## 5. Blocking correction B — remove Chapter 4-like "safe if patched" claim

Current B6 prose includes:

`Một hệ thống kích hoạt SMBv1 vẫn có thể được bảo vệ an toàn nếu đã được áp dụng đầy đủ các bản vá bảo mật tương ứng.`

Remove this sentence entirely.

Reasons:

1. it is not a measured Scenario 1 result;
2. it introduces a generalized security/safety claim;
3. it requires external support if retained;
4. it belongs to later discussion/mitigation logic, not the measured-results section;
5. "an toàn" is too broad for the evidence.

The paragraph only needs to preserve:

`SMBv1 observed != MS17-010 confirmed`.

## 6. Blocking correction C — local signing and remote signing must remain independent

Current prose states that the remote `smb2-security-mode` result:

`phù hợp với cấu hình ký số cục bộ đã ghi nhận tại Mục 3.1`

This is not allowed.

The project-wide lock explicitly requires:

- local signing flags do not establish remote signing result;
- remote signing observation and local configuration are separate facts.

Required correction:

State only that B6 remotely recorded:

`Message signing enabled but not required`.

If cross-reference is retained, it must explicitly preserve independence, for example:

`Đây là kết quả quan sát từ xa của smb2-security-mode và được ghi nhận độc lập với các cờ cấu hình cục bộ tại Mục 3.1.`

Do not describe the two layers as matching/confirming each other unless a dedicated cross-layer claim has been approved.

## 7. Blocking correction D — narrow B5 absolute and final transition

### B5

Current prose says exact identification is:

`hoàn toàn không thể nếu chỉ dựa trên các phản hồi từ xa này`

That is stronger than needed.

Use:

`các phản hồi từ xa này chưa đủ căn cứ để định danh chính xác duy nhất phiên bản Windows Server 2012 R2`.

This preserves the actual measurement limit without making a universal impossibility claim.

### Final transition

Current ending says Scenario 2 will:

`xác minh chính xác liệu ... có bị ảnh hưởng bởi lỗ hổng ... hay không`

Because the actual later remote result may remain UNKNOWN, the transition should not promise a definitive verdict.

Use a bounded transition such as:

`Mục 3.3 tiếp tục sử dụng các phép đo NSE chuyên biệt để kiểm tra dấu hiệu liên quan đến MS17-010.`

Do not reveal the Scenario 2 outcome.

## 8. Blocking correction E — provenance and self-review traceability

### 8.1 X7B0 figure-selection SHA metadata

The approved X7B0 figure-selection artifact currently contains incorrect SHA-256 metadata:

Incorrect historical values:
- B5: `18fbe98f79fbe44147cf75cf145377f0a8c2bdf14f24d62b9a1da87ec44ee789`
- B6: `63200a40f0d2c949c25bb3ca5dbe003ba732c48bf0a0be3b76a084eb87cf1aa2`

Actual repository-byte SHA-256 values:
- B5: `05699e248fa66ab224adc6809fb057a282d86c29c3ce2851823e07bd874f6466`
- B6: `b5b236cbe695b530b44e0af592f010f1f49bef9f5da427b9958fd9020bd651f8`

R2 is authorized to correct **only these two SHA metadata fields** in:

`work/do-an/CH3_32_SCENARIO1_FIGURE_SELECTION_R1.md`

This is a provenance-only factual correction.

It does **not** reopen:
- figure choice;
- crop rectangles;
- numbering;
- captions;
- user approval of X7B0.

### 8.2 Self-review claim numbering

The R1 self-review claim audit is not aligned with the approved claim map.

Examples:
- approved `S1-C04` = TCP 139 OPEN, but self-review uses C04 for B3 continuity;
- approved `S1-C05` = TCP 445 OPEN;
- approved `S1-C06` = `445 OPEN != vulnerable`;
- subsequent claim numbers are therefore shifted in the self-review summary.

R2 must rebuild the paragraph/table/figure-to-claim audit directly from:

`CH3_32_SCENARIO1_CLAIM_EVIDENCE_MAP_R1.md`

Do not infer claim numbering from memory.

Also remove/correct the self-review mention of a B3 `0.00030s` latency; direct B3 raw is `0.00034s`, and no exact latency is needed in the public prose anyway.

## 9. Lecturer / defense-readiness assessment

The section is close to a strong student report.

What works:
- the demo sequence is immediately visible;
- B2/B3 are concise;
- the table avoids screenshot clutter;
- B5 teaches the reader the precision limit of fingerprinting;
- B6 provides direct protocol-level evidence;
- the section ends with an appropriate handoff to the vulnerability-oriented scenario.

What currently weakens defense-readiness:
- application-level wording is occasionally stronger than the measured TCP evidence;
- one sentence drifts into a broad security assurance claim;
- local/remote signing is incorrectly presented as mutually confirming;
- the internal provenance record contains stale SHA values.

These are correctable without changing the section architecture.

## 10. Final gate

Verdict:

`X7B1_R1_REVISE_BLOCKING`

Do not open X7C.

R2 must be a bounded correction only.

After R2, perform a final independent external review again before asking the user to approve Section 3.2.
