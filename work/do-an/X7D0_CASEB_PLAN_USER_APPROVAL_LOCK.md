# X7D0 CASE B PLAN USER APPROVAL LOCK

Date: 2026-10-06  
Status: `USER_APPROVED / LOCKED`

## Decision

The user explicitly approved ("chốt") the Case B Evidence & Presentation Plan after independent final external review.

Reviewer-final source:

`feature/x7d0-ch3-caseb-plan@87e9ec8d04125d9953391bafc06345e5c78392eb`

Final external review:

`work/do-an/X7D0_CASEB_PLAN_EXTERNAL_REVIEW_R2_FINAL.md`

Result:
- Score: **99/100 — PASS**
- Blockers: **0**

## Locked Section 3.4 plan

- 3.4.1. Thực thi vô hiệu hóa giao thức SMBv1 và kiểm tra trạng thái máy chủ cục bộ
- 3.4.2. Đo đạc lại kịch bản NSE từ xa và đối chiếu kết quả đa tầng

## Locked presentation allocation

- **Bảng 3.5**
- **Hình 3.7** — After Local
- **Hình 3.8** — Protocol retest

Image decisions:
- 01 Before = DROP
- 02 Action = DROP
- 03 After Local = KEEP
- 04 NSE02 Protocols = KEEP
- 05 combined NSE04 = OPTIONAL / DROP

Provisional crop rectangles:
- Hình 3.7: `x=0, y=30, width=872, height=310`
- Hình 3.8: `x=0, y=24, width=1280, height=400`

## Locked technical boundaries

- `SMBv1 disabled != FS-SMB1 uninstalled`
- `SMBv1 disabled != PATCHED`
- `445 OPEN != vulnerable`
- remaining SMB2/3 dialect values do not prove full workload continuity
- `UNKNOWN / NO USABLE SCRIPT RESULT`
- `UNKNOWN != SAFE`
- local `UNPATCHED` independent from remote `UNKNOWN`
- no false-negative classification
- no invented NTSTATUS/IPC$/negotiation failure cause
- missing `SMBv1_Remediation_06_Raw_Evidence.png` remains a metadata/staging discrepancy and is not evidence

## Numbering consequence

Next available numbering:
- **Bảng 3.6**
- **Hình 3.9**

## Workflow consequence

The X7D0 plan artifacts may be explicitly integrated into `feature/ch3-integration`.

Per the user-approved Word-checkpoint workflow:
1. WR1 Demo 1 Word review now starts.
2. WR2 Demo 2 Word review follows only after WR1 approval.
3. X7D1 Section 3.4 prose remains blocked until WR1 + WR2 are both approved.
