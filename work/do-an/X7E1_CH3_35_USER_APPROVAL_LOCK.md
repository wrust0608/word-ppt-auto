# X7E1 SECTION 3.5 CASE C — USER APPROVAL LOCK

Date: 2026-10-07  
Status: `USER APPROVED / LOCKED`

The user explicitly approved ("chốt") the final reviewed Section 3.5 Case C after the final external review PASS.

## Locked content

Section:
- `3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense`
- `3.5.1. Thiết lập cầu nối pfSense và chính sách kiểm soát lưu lượng SMB`
- `3.5.2. Kết quả đo đạc từ xa, đối chiếu nhật ký tường lửa và trạng thái máy chủ`

Locked presentation:
- `Bảng 3.6`
- `Hình 3.9` — pfSense rule order/configuration
- `Hình 3.10` — Nmap 139/445 FILTERED result
- `Hình 3.11` — pfSense Block log

No standard Hình 3.12 is used in Section 3.5.

## Locked technical meaning

- The tested Kali → Windows path is arranged through pfSense Transparent Bridge in Case C.
- From Kali:
  - TCP 139 = FILTERED / no-response;
  - TCP 445 = FILTERED / no-response.
- pfSense log records matching TCP SYN traffic to 139/445 as Block on the tested path.
- The visible rule label in the log conflicts with the Case C run record; therefore the screenshot is not used to prove the exact named rule matched.
- Remote MS17-010 classification remains:
  `UNKNOWN / NO USABLE SCRIPT RESULT`.
- No internal script-failure cause is established.
- Windows-local recorded state remains:
  - SMB1=True;
  - SMB2=True;
  - LanmanServer=Running;
  - local listeners 139/445 present;
  - patch state UNPATCHED.
- `FILTERED != PATCHED`
- `UNKNOWN != SAFE`

## Locked presentation-crop artifacts

- `work/do-an/chapter3/presentation/3_5/Hinh_3_9_pfSense_Rule_Order.png`
- `work/do-an/chapter3/presentation/3_5/Hinh_3_10_Nmap_Filtered.png`
- `work/do-an/chapter3/presentation/3_5/Hinh_3_11_pfSense_Block_Log.png`

Hình 3.11 remains a tight log crop without the source table-heading row; its field interpretation was checked against the complete source screenshot. No montage or artificial annotation is used.

## Approved artifacts

- `work/do-an/CH3_35_CASEC_DRAFT_R1.md`
- `work/do-an/CH3_35_CASEC_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_35_CASEC_CROP_MANIFEST_R1.md`
- `work/do-an/chapter3/presentation/3_5/Hinh_3_9_pfSense_Rule_Order.png`
- `work/do-an/chapter3/presentation/3_5/Hinh_3_10_Nmap_Filtered.png`
- `work/do-an/chapter3/presentation/3_5/Hinh_3_11_pfSense_Block_Log.png`
- `work/do-an/X7E1_CH3_35_EXTERNAL_REVIEW_R1.md`
- `work/do-an/X7E1_CH3_35_EXTERNAL_REVIEW_R2_FINAL.md`

## Next numbering

- next table: `Bảng 3.7`
- next figure: `Hình 3.12`

## Next workflow step

Only after explicit integration into `feature/ch3-integration` may the synthesis step open:

- Section 3.6 — compare the approved empirical states/results;
- Section 3.7 — close Chapter 3.

No new raw evidence.
No new standard screenshots by default.
No Word assembly.
No Chapter 2 rewrite.
No Chapter 4.
