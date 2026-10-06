# X7E0 CASE C PRESENTATION PLAN — USER APPROVAL LOCK

Date: 2026-10-07  
Status: `USER APPROVED / LOCKED`

The user explicitly approved ("chốt") the final reviewed Case C evidence/presentation plan after the final external review PASS.

## Locked structure

Section:
- `3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense`

H3:
- `3.5.1. Thiết lập cầu nối pfSense và chính sách kiểm soát lưu lượng SMB`
- `3.5.2. Kết quả đo đạc từ xa, đối chiếu nhật ký tường lửa và trạng thái máy chủ`

## Locked presentation

- `Bảng 3.6` — one result-oriented before/after comparison table.
- `Hình 3.9` — `pfSense_08_Rule_Order.png`
- `Hình 3.10` — `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`
- `Hình 3.11` — `pfSense_10_Block_Log_CANONICAL.png`

Standard layout excludes:
- `pfSense_04_Bridge.png` (OPTIONAL/DROP)
- `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` (OPTIONAL/DROP)

No fourth standard figure is approved.

## Locked evidence boundaries

- Case C control = pfSense Transparent Bridge on the tested Kali → Windows path.
- Baseline must not be described as "no firewall"; Windows Firewall already existed.
- TCP 139/445 are observed FILTERED from Kali in Case C.
- pfSense logs record matching TCP SYN traffic being Blocked on the tested path.
- Exact named-rule attribution from the log screenshot is NOT established because the visible log rule label conflicts with the manifest.
- NSE-SMB-04 result remains:
  `UNKNOWN / NO USABLE SCRIPT RESULT`.
- No script-internal cause is established.
- Windows-local metadata remains point-in-time:
  - SMB1=True;
  - SMB2=True;
  - LanmanServer=Running;
  - local listeners 139/445 present;
  - patch state UNPATCHED.
- `FILTERED != PATCHED`
- `UNKNOWN != SAFE`

## Locked crop direction

### Hình 3.9
Provisional approved direction:
- around `x≈15, y≈190, width≈470, height≈340`
- must preserve:
  - CASE_C_KALI context;
  - Rules heading;
  - full Block row;
  - full Pass row.

### Hình 3.10
Crop must preserve:
- full Nmap command;
- Host is up / arp-response;
- 139 FILTERED/no-response;
- 445 FILTERED/no-response;
- MAC;
- Nmap done.

### Hình 3.11
Current coordinates are PROVISIONAL ONLY.

X7E1 must visually inspect the original long screenshot before creating the final crop.

The final crop must preserve:
- necessary log column headings;
- matching Block rows for 139/445;
- the Rule column / visible rule-label conflict if that column is included.

The crop must not hide the unresolved label discrepancy.

## Approved artifacts

- `work/do-an/CH3_35_CASEC_FIGURE_SELECTION_R1.md`
- `work/do-an/CH3_35_CASEC_PRESENTATION_PLAN_R1.md`
- `work/do-an/CH3_35_CASEC_CLAIM_EVIDENCE_MAP_R1.md`
- `work/do-an/CH3_35_CASEC_PLAN_SELF_REVIEW_R1.md`
- `work/do-an/X7E0_CASEC_PLAN_EXTERNAL_REVIEW_R1.md`
- `work/do-an/X7E0_CASEC_PLAN_EXTERNAL_REVIEW_R2_FINAL.md`

## Numbering after this lock

- Bảng 3.6 is allocated to Case C.
- Hình 3.9–3.11 are allocated to Case C.
- Next table: `Bảng 3.7`.
- Next figure: `Hình 3.12`.

## Next workflow step

Only after explicit integration of these approved plan/review artifacts into `feature/ch3-integration` may X7E1 open.

X7E1 may:
- create the three approved derived crops;
- write Section 3.5 prose;
- create crop manifest + self-review.

X7E1 may not:
- add another standard figure;
- write Sections 3.6–3.7;
- assemble Chapter 3;
- build Word;
- modify Chapter 2;
- open Chapter 4.
