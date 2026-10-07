# X7F SECTIONS 3.6–3.7 — USER APPROVAL LOCK

Date: 2026-10-07  
Status: `USER APPROVED / LOCKED`

The user explicitly approved ("chốt") the final reviewed Sections 3.6 and 3.7 after the final external review PASS.

## Locked content

- `3.6. So sánh kết quả thực nghiệm`
- `3.7. Tổng kết chương`

## Locked presentation

- `Bảng 3.7. So sánh trạng thái thực nghiệm giữa đường cơ sở, Case B và Case C`
- Bảng 3.7 uses 4 columns and 8 comparison rows.
- No new figure is allocated in X7F.
- `Hình 3.12` therefore remains the next available figure number.

## Locked technical synthesis

### Baseline
- TCP 139 = OPEN (syn-ack)
- TCP 445 = OPEN (syn-ack)
- smb-protocols records:
  - NT LM 0.12
  - 2.0.2
  - 2.1
  - 3.0
  - 3.0.2
- SMB1 local = True
- LanmanServer = Running
- local patch classification = UNPATCHED
- remote MS17 = UNKNOWN / NO USABLE SCRIPT RESULT

### Case B
- intervention layer = Windows SMB1 server configuration
- TCP 139 = not remeasured in Case B
- TCP 445 = OPEN
- no post-intervention syn-ack attribution
- smb-protocols records:
  - 2.0.2
  - 2.1
  - 3.0
  - 3.0.2
- NT LM 0.12 does not appear in the retest list
- SMB1 local = False
- LanmanServer = Running at the recorded check
- patch classification = UNPATCHED
- no recorded patch-install action
- remote MS17 = UNKNOWN / NO USABLE SCRIPT RESULT

### Case C
- intervention layer = tested Kali → Windows network path through pfSense Transparent Bridge
- TCP 139 = FILTERED / no-response from Kali
- TCP 445 = FILTERED / no-response from Kali
- no corresponding SMB dialect measurement is synthesized
- SMB1 local = True
- LanmanServer = Running at the recorded final state
- patch classification = UNPATCHED
- no recorded patch-install action
- matching SMB SYN traffic is recorded as Block on pfSense
- remote MS17 = UNKNOWN / NO USABLE SCRIPT RESULT

## Locked inference boundaries

- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `SMBv1 disabled != PATCHED`
- `FILTERED != PATCHED`
- `UNKNOWN != SAFE`

No control ranking.
No recommendation.
No Chapter 4 leakage.
No invented causes for UNKNOWN.
No invented measurements for gaps.

## Approved artifacts

- `work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md`
- `work/do-an/CH3_36_37_SYNTHESIS_SELF_REVIEW_R1.md`
- `work/do-an/X7F_CH3_36_37_EXTERNAL_REVIEW_R1.md`
- `work/do-an/X7F_CH3_36_37_EXTERNAL_REVIEW_R2_FINAL.md`

## Numbering after this lock

- Next table: `Bảng 3.8`
- Next figure: `Hình 3.12`

## Next workflow step

Only after explicit integration into `feature/ch3-integration` may X7G open.

X7G is mechanical Chapter 3 assembly only.

X7G may:
- combine approved Sections 3.1–3.7;
- normalize heading spacing/cross-references;
- clean transitions;
- remove obvious duplicate sentences without changing technical meaning;
- preserve all approved table/figure numbering and image paths.

X7G may not:
- introduce new evidence;
- change technical facts;
- reinterpret results;
- create Word/PDF;
- modify Chapter 2;
- open Chapter 4.

After X7G, X7H performs the whole-Chapter-3 product review before the user is asked to approve the complete chapter.
