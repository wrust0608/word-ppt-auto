# X7J R2 — BOUND FINAL REVIEW / DEFENSE READINESS TO LOCKED EVIDENCE

Status: AUTHORIZED BOUNDED CORRECTION
Date: 2026-10-07
Branch: `feature/x7j-final-ch2-ch3-review-r1`
R1 candidate: `fbe8cb7422ed59088effc7bdc857e4653837dd62`
External review: `work/do-an/X7J_FINAL_CH2_CH3_EXTERNAL_REVIEW_R1.md`

## 0. Scope

Correct only the X7J review and handoff language identified by the independent reviewer.

The actual Chapters 2+3 product remains LOCKED and must not be modified.

Forbidden:
- editing `CHAPTER_2.md`;
- editing `CHAPTER_3_DRAFT_R2.md`;
- editing/regenerating `CHAPTER_2_3_REVIEW.docx`;
- changing tables/figures;
- opening Chapter 1 or Chapter 4;
- adding experiments/evidence.

## 1. Preserve the correct NSE-SMB mapping

Use exactly:

- `NSE-SMB-01` = TCP 139/445 port scan with reason;
- `NSE-SMB-02` = `smb-protocols`;
- `NSE-SMB-03` = `smb2-security-mode`;
- `NSE-SMB-04` = `smb-vuln-ms17-010`.

Do not repeat the incorrect mapping that appeared in the executor's user-facing R1 execution summary.

## 2. Correct Defense Readiness answer 1 — Host-Only

Remove absolute language:
- `triệt tiêu hoàn toàn`;
- `khả lặp 100%`.

Use only the documented basis:
- Host-Only NIC;
- no NAT/Bridged;
- no default route;
- limits connection paths within the lab.

## 3. Correct answer 2 — why TCP139 and TCP445

State:
- TCP139 = NetBIOS Session Service;
- TCP445 = Direct-hosted SMB;
- both are in the SMB service surface defined by the project scenario;
- measuring both provides the complete project-scoped remote service view.

Do not add a new statement that `srv.sys` is proven by this experiment to process both flows.

## 4. Correct answer 3 — SMBv1 enabled vs patch state

Preserve:
`SMBv1 enabled != MS17-010 confirmed`.

Say:
- protocol support and patch state are separate observations;
- exact local patch classification must be established independently.

Do not use global `safe` wording.

## 5. Correct answer 4 — why NSE-SMB-04 is UNKNOWN

Use only:
- Nmap completed;
- no usable Host-script verdict was present;
- project classification = `UNKNOWN / NO USABLE SCRIPT RESULT`;
- cause is not established;
- `UNKNOWN != SAFE`.

Do not describe an inferred internal cause or claim that the script “did not detect a confirming sign”.

## 6. Correct answer 5 — Case B

Use only observed facts:
- `EnableSMB1Protocol=False`;
- `NT LM 0.12` absent from retest dialect list;
- TCP445 remains OPEN;
- local patch = UNPATCHED;
- remote MS17 = UNKNOWN;
- `SMBv1 disabled != PATCHED`.

Remove:
- “server rejects negotiation”;
- “blocks the SMBv1 attack path”;
- any successful/failed negotiation claim.

## 7. Correct answer 6 — Case C

Use only:
- TCP139/445 = FILTERED/no-response from Kali;
- pfSense records matching blocked SMB SYN traffic;
- Windows local patch state remains UNPATCHED;
- `FILTERED != PATCHED`.

Remove speculative attacker-bypass/same-segment scenarios.

## 8. Correct answer 7 — why no exploit

Use only the documented experimental scope:
- non-invasive scanning/measurement;
- no exploit payloads were part of the approved experiment.

Do not invent a BSOD/kernel-crash reason.

## 9. Tone down absolute review language

Replace claims such as:
- `làm chủ hoàn toàn`;
- `khả lặp 100%`;
- `bảo vệ thành công`;
- `mọi câu hỏi phản biện`;

with bounded reviewer language:
- `có cơ sở để giải thích`;
- `sẵn sàng ở phạm vi Chương 2–3`;
- `không phát hiện blocker trong phạm vi đã kiểm`.

The review should read like a lecturer assessment, not promotional copy.

## 10. Preserve all findings that independently passed

Keep:
- method ↔ result mapping;
- B1–B6 coverage;
- `smb2-capabilities` result coverage;
- terminology findings that are actually supported;
- technical-lock audit;
- duplication/flow assessment;
- DOCX identity;
- X7I final-pass status.

## 11. Required outputs

Update only:

1. `work/do-an/X7J_FINAL_CH2_CH3_REVIEW_R1.md`
2. `work/do-an/X7J_FINAL_CH2_CH3_EXECUTOR_HANDOFF_R1.md`
3. `work/do-an/PROJECT_STATE.md`

Report:
- exact sentences changed;
- confirmation product sources/DOCX unchanged;
- source blob/hash verification;
- final X7J verdict proposed for independent review.

## 12. Stop state

The only allowed completion state is:

`X7J_R2_READY_FOR_INDEPENDENT_REVIEW`

Do not mark the milestone complete yourself.
Do not provide a new DOCX.
Commit, push, then STOP.
