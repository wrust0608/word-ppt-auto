# X7J FINAL CHAPTERS 2+3 PRODUCT REVIEW — EXTERNAL REVIEW R1

Date: 2026-10-07  
Branch: `feature/x7j-final-ch2-ch3-review-r1`  
Executor candidate: `fbe8cb7422ed59088effc7bdc857e4653837dd62`

Verdict: **REVISE_MINOR_BLOCKING**  
Score: **95/100**

## 1. Independent verification

The reviewer independently verified:

- current branch HEAD exactly matches the executor candidate;
- X7J did not modify:
  - `work/do-an/CHAPTER_2.md`;
  - `work/do-an/CHAPTER_3_DRAFT_R2.md`;
  - `work/do-an/output/CHAPTER_2_3_REVIEW.docx`;
- Chapter 2 and Chapter 3 source blobs remain locked and unchanged;
- the X7I frozen DOCX remains the product under review;
- method/result mapping for the major experimental families is materially coherent;
- Chapter 2 B6 includes `smb2-capabilities`, and Chapter 3 contains the corresponding observed capability results, so there is no missing B6 result;
- the actual Chapter 2/3 product preserves the core technical truth locks and does not require reopening.

The combined Word product itself remains a valid final-review candidate.

## 2. Why X7J R1 cannot PASS yet

The blocker is not the Word document.

The blocker is the X7J review artifact itself, specifically its Defense Readiness section and some absolute language in the handoff.

X7J is the final reviewer gate. Its own explanations must be at least as evidence-bounded as the locked report. Several drafted defense answers introduce claims that the report does not establish.

## 3. Required correction A — Host-Only answer overclaims isolation/repeatability

Current X7J defense wording says Host-Only:

`triệt tiêu hoàn toàn nguy cơ rò rỉ lưu lượng quét mạng ra bên ngoài`

and:

`bảo đảm tính khả lặp 100% của môi trường thực nghiệm`.

The locked Chapter 2 wording is narrower:
- Host-Only NIC only;
- no NAT/Bridged;
- no default route;
- this **limits the connection path within the lab**.

The report does not prove absolute elimination of all leakage risk or 100% reproducibility.

Required correction:
- use bounded wording such as:
  `giới hạn đường kết nối của hai máy ảo trong mạng lab và giảm ảnh hưởng từ mạng ngoài`;
- do not use `triệt tiêu hoàn toàn` or `100%` reproducibility claims.

## 4. Required correction B — port 139/445 rationale adds unsupported MS17-010 driver-path claim

Current X7J answer says MS17-010 in `srv.sys` processes both port-139 and port-445 traffic.

The locked Chapters 2+3 establish:
- TCP 139 = NetBIOS Session Service;
- TCP 445 = Direct-hosted SMB;
- both are part of the SMB service surface measured by this project.

They do not use the experimental evidence to prove a detailed causal driver-processing path for both ports.

Required correction:
- answer only that the project measures both standard SMB service paths because the scenario scope covers SMB exposure on 139 and 445;
- avoid a new driver-path claim unless it already exists as an explicitly supported cited theory statement in the locked report.

## 5. Required correction C — patched-SMBv1 wording uses “safe” too broadly

Current X7J answer says that if KB4012213 is installed, SMBv1 can operate “an toàn”.

The locked logic is:
- SMBv1 enabled does not itself confirm MS17-010;
- local patch state must be assessed independently;
- no global safety claim follows from one patch condition.

Required correction:
- say that an enabled SMBv1 configuration and MS17-010 patch state are independent observations;
- do not characterize the whole server/protocol as `safe`.

## 6. Required correction D — UNKNOWN explanation must remain cause-agnostic

Current X7J answer says the script:
- sends a particular kind of probe;
- completes without detecting a confirming sign.

The locked Chapter 3 states more strictly:
- Nmap completed;
- no usable `Host script results:` block appeared;
- the project classifies the outcome as `UNKNOWN / NO USABLE SCRIPT RESULT`;
- **the cause of the missing usable output is not established by the evidence**.

Required correction:
- preserve exactly that bounded interpretation;
- do not infer internal script behavior or the reason the script returned no usable verdict.

## 7. Required correction E — Case B defense answer overclaims SMB negotiation and attack-path blocking

Current X7J answer says disabling SMBv1:
- makes the server reject negotiation of NT LM 0.12;
- blocks the attack path through SMBv1.

The approved Case B evidence only establishes:
- `EnableSMB1Protocol=False`;
- `NT LM 0.12` does not appear in the remote retest dialect list;
- TCP445 remains OPEN;
- local patch state remains UNPATCHED;
- remote MS17 verdict remains UNKNOWN.

The project explicitly forbids inferring successful/failed SMB negotiation or broader workload behavior from this evidence.

Required correction:
- state only the observed configuration and retest changes;
- retain `SMBv1 disabled != PATCHED`;
- remove “reject negotiation” and “blocks attack path” claims.

## 8. Required correction F — Case C answer introduces speculative attack-path/risk scenario

Current X7J answer adds:
`Nếu kẻ tấn công xâm nhập từ cùng phân đoạn hoặc đường vòng, nguy cơ vẫn tồn tại.`

That is a plausible security scenario, but it is not an observed result of Chapters 2+3 and belongs to later risk/recommendation analysis if the user ever opens that scope.

Required correction:
- limit the answer to:
  - Kali observes FILTERED/no-response;
  - pfSense logs matching blocked SMB SYN traffic;
  - Windows remains locally UNPATCHED;
  - therefore `FILTERED != PATCHED`;
- remove the speculative attacker-path scenario.

## 9. Required correction G — reason for not running exploit must match documented scope

Current X7J answer says exploit/RCE/Meterpreter were not run to avoid unknown kernel-crash risk.

The locked Chapter 2 says:
- the experimental scope is non-invasive scanning;
- it does not send exploit payloads;
- it records service responses.

Required correction:
- answer that exploitation was outside the approved experimental scope and the project intentionally used non-invasive measurement;
- do not invent a specific crash/BSOD rationale unless directly supported by locked source material.

## 10. Executor-summary inconsistency — NSE-SMB labels

The executor's user-facing execution summary states an incorrect mapping:
- NSE-SMB-01 = `smb2-security-mode`;
- NSE-SMB-02 = `smb2-capabilities`;
- NSE-SMB-03 = `smb-protocols`.

The locked report and the committed X7J review table correctly define:
- NSE-SMB-01 = port 139/445 scan;
- NSE-SMB-02 = `smb-protocols`;
- NSE-SMB-03 = `smb2-security-mode`;
- NSE-SMB-04 = `smb-vuln-ms17-010`.

R2 handoff/review must explicitly preserve the correct mapping and must not repeat the erroneous user-facing summary.

## 11. Product-level verdict

Independent review of the actual locked Chapters 2+3 product finds:

- method ↔ result progression: **PASS**;
- major experiment families: **PASS**;
- B1–B6 coverage including `smb2-capabilities`: **PASS**;
- Scenario 2 mapping in the report: **PASS**;
- technical truth boundaries: **PASS**;
- terminology in the locked product: **PASS**;
- combined Word artifact identity/layout: already **X7I FINAL PASS**.

Therefore:
- **do not reopen Chapter 2**;
- **do not reopen Chapter 3**;
- **do not regenerate the DOCX**.

Only X7J review/handoff language needs correction.

## 12. Gate

Current verdict:

`X7J_R1_REVISE_MINOR_BLOCKING`

Run one bounded X7J R2 correction.

R2 may edit only:
- `work/do-an/X7J_FINAL_CH2_CH3_REVIEW_R1.md`;
- `work/do-an/X7J_FINAL_CH2_CH3_EXECUTOR_HANDOFF_R1.md`;
- `work/do-an/PROJECT_STATE.md` as needed.

Do not edit or regenerate the report product.

After correction, stop at:

`X7J_R2_READY_FOR_INDEPENDENT_REVIEW`.
