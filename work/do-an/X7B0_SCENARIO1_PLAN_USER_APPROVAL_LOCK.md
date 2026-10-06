# X7B0 SCENARIO 1 PLAN USER APPROVAL LOCK

Date: 2026-10-06  
Status: `USER_APPROVED / LOCKED`

## Decision

The user explicitly approved ("chốt") the Scenario 1 Evidence & Presentation Plan for Chapter 3 Section 3.2 after independent final external review.

Reviewer-final source:

`feature/x7b0-ch3-scenario1-plan@16ec564816a8bedbb1514ba0b8d3a57a63093d21`

Final external review:

`work/do-an/X7B0_SCENARIO1_PLAN_EXTERNAL_REVIEW_R2_FINAL.md`

Result:

- Score: **98/100 — PASS**
- Blockers: **0**

## Locked Section 3.2 structure

- 3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB
- 3.2.1. Khảo sát trạm mạng và trạng thái mở cổng dịch vụ SMB
- 3.2.2. Nhận diện phiên bản dịch vụ và đặc tính giao thức SMB

## Locked table

- **Bảng 3.3. Trình tự và kết quả khảo sát dịch vụ SMB từ trạm Kali Linux**

## Locked figures

- **Hình 3.4** — source: `Scenario1_B5_SMB_Version.png`
- **Hình 3.5** — source: `Scenario1_B6_SMB_NSE_A.png`

Figure decision:
- B4 screenshot = DROP
- B5 screenshot = KEEP
- B6 screenshot = KEEP
- no dedicated B2/B3 screenshots

Provisional crop rectangles approved for X7B1 implementation:

- Hình 3.4 / B5 source 1280×800:
  `x=0, y=24, width=1280, height=310`
- Hình 3.5 / B6 source 1280×800:
  `x=0, y=24, width=1280, height=710`

## Locked technical boundaries

- `.56.100 = UNKNOWN identity`
- `445 OPEN != vulnerable`
- B5 fingerprint = `Microsoft Windows Server 2008 R2–2012` only
- SMBv1 observation != MS17-010 confirmation
- remote signing = `enabled but not required`
- `smb-os-discovery = no usable output`
- Scenario 1 does not produce an MS17-010 verdict

## Numbering consequence

Next available numbering after the approved Section 3.2 plan:

- **Bảng 3.4**
- **Hình 3.6**

## Consequence

The approved X7B0 planning artifacts may be explicitly integrated into `feature/ch3-integration`.

After integration, X7B1 may open for:
- Section 3.2 prose only;
- approved B5/B6 presentation crops;
- crop manifest;
- self-review.

Scenario 2 remains blocked until Section 3.2 prose passes external review + user approval.
