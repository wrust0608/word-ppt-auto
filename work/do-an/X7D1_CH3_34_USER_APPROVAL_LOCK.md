# X7D1 SECTION 3.4 CASE B — USER APPROVAL LOCK

Date: 2026-10-07  
Status: `USER APPROVED / LOCKED`

The user explicitly approved ("chốt") the final reviewed Section 3.4 Case B after the final external review PASS.

## Locked content

Section:
- `3.4. Kết quả Case B — Vô hiệu hóa SMBv1 và đo lại từ xa`
- `3.4.1. Thao tác vô hiệu hóa SMBv1 và kiểm tra trạng thái máy chủ cục bộ`
- `3.4.2. Kết quả đo đạc lại từ xa và đối chiếu đa tầng`

Locked presentation:
- `Bảng 3.5`
- `Hình 3.7` — local after-state
- `Hình 3.8` — remote SMB dialect retest

Locked technical meaning:
- SMB1 server configuration: True -> False;
- SMB2 configuration remains True;
- FS-SMB1 remains Installed;
- LanmanServer is observed Running before/after as point-in-time observations;
- TCP 445 remains OPEN in the Case B retest;
- NT LM 0.12 (SMBv1) does not appear in the retest dialect list;
- local patch classification remains UNPATCHED;
- remote MS17-010 result remains UNKNOWN / NO USABLE SCRIPT RESULT.

Locked inference boundaries:
- `SMBv1 disabled != FS-SMB1 uninstalled`
- `SMBv1 disabled != PATCHED`
- `445 OPEN != vulnerable`
- `UNKNOWN != SAFE`

## Approved artifacts

- `work/do-an/CH3_34_CASEB_DRAFT_R1.md`
- `work/do-an/CH3_34_CASEB_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_34_CASEB_CROP_MANIFEST_R1.md`
- `work/do-an/chapter3/presentation/3_4/Hinh_3_7_After_Local.png`
- `work/do-an/chapter3/presentation/3_4/Hinh_3_8_SMB_Protocols_Retest.png`
- `work/do-an/X7D1_CH3_34_EXTERNAL_REVIEW_R1.md`
- `work/do-an/X7D1_CH3_34_EXTERNAL_REVIEW_R2_FINAL.md`

## Next numbering

- next table: `Bảng 3.6`
- next figure: `Hình 3.9`

## Next workflow step

Only after explicit integration of the approved Section 3.4 artifacts into `feature/ch3-integration` may Case C planning open.

No Word assembly.
No Chapter 2 rewrite.
No Chapter 4.
