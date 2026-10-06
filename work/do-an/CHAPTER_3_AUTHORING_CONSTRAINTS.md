# CHAPTER 3 AUTHORING CONSTRAINTS — RESULTS-ORIENTED STUDENT REPORT

Status: LOCKED_FOR_X7_DRAFT
Date: 2026-10-06
Role perspective: Lecturer / thesis-project reviewer in Information Security.

## 1. Purpose

Chapter 3 is the place where the student shows what was actually observed, where the reader can trace each result to direct evidence, and where before/after changes are stated accurately.

Chapter 3 is NOT:
- an evidence-audit memo;
- a project-management report;
- a second methods chapter;
- a security-risk discussion chapter;
- a screenshot gallery.

Highest criterion:
Đúng kỹ thuật — dễ hiểu — bám sát phép đo — nhìn ra ngay kết quả — đủ sức bảo vệ trước hội đồng.

## 2. External writing principles adopted

The design follows these academic-report conventions:
1. Experimental results should be organized according to the research aims and methods established earlier.
2. Results should be presented with tables and figures, not only descriptive prose.
3. Text introduces tables/figures and guides the reader to the important observation.
4. Negative or inconclusive results must still be reported honestly.
5. Each experiment/result unit should contain a short reminder of purpose, the observed result, supporting table/figure, and a brief direct interpretation.
6. Broader implications, risk, recommendations and theoretical explanation belong mainly in the discussion/evaluation chapter.

These presentation rules are consistent with HUIT assessment criteria for reports/practical reports and common guidance for experimental results chapters. Project technical truth remains controlled by the R3 evidence layer.

## 3. Locked Chapter 3 architecture

# CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH

## 3.1. Trạng thái baseline trước đo đạc
### 3.1.1. Trạng thái mạng và dịch vụ SMB
### 3.1.2. Trạng thái bản vá và mốc phục hồi

## 3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB
### 3.2.1. Phát hiện máy đích và trạng thái cổng
### 3.2.2. Nhận diện dịch vụ SMB
### 3.2.3. Dialect SMB, signing và capability

## 3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010
### 3.3.1. Trạng thái cổng, giao thức và signing trước phép kiểm tra
### 3.3.2. Kết quả kiểm tra bằng smb-vuln-ms17-010
### 3.3.3. Đối chiếu kết quả từ xa với trạng thái bản vá cục bộ

## 3.4. Kết quả Case B — Vô hiệu hóa SMBv1
### 3.4.1. Trạng thái trước và sau can thiệp
### 3.4.2. Kết quả kiểm tra lại giao thức SMB
### 3.4.3. Kết quả kiểm tra lại MS17-010

## 3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense
### 3.5.1. Trạng thái cấu hình kiểm soát lưu lượng
### 3.5.2. Kết quả quét cổng qua đường dẫn pfSense
### 3.5.3. Đối chiếu kết quả Nmap với nhật ký pfSense và trạng thái máy chủ

## 3.6. So sánh kết quả thực nghiệm
### 3.6.1. Ma trận so sánh Baseline, Case B và Case C
### 3.6.2. Các thay đổi quan sát được

## 3.7. Tổng kết chương

H2 count = 7.
H3 count = 16.
H2 is locked. H3 is locked for X7 Draft R1 and may only change after external review.

## 4. Narrative pattern for every H3

Normally:
1. one short sentence recalling the measurement purpose;
2. state the direct result;
3. introduce the table/figure before it appears;
4. present the table/figure;
5. one short paragraph explaining what can be concluded directly;
6. a limitation only if the result could otherwise be misread.

Do not repeat commands already documented in Chapter 2 unless strictly necessary.

## 5. Student-report voice

Use academic Vietnamese for an undergraduate Information Security project.

Preferred:
- direct sentences;
- stable terminology;
- third-person neutral voice;
- exact observed values.

Forbidden as visible report architecture/prose:
canonical, ground truth, truth matrix, evidence layer, evidence grade, gate, governance, locked candidate, source-of-truth, L1/L2/L3/L4/L5 evidence model, ENV/S1/S2/CB/CC internal IDs.

## 6. Chapter 3 / Chapter 4 boundary

Allowed in Chapter 3:
- direct measurements;
- before/after comparison;
- Nmap output state;
- local Windows state;
- patch-state comparison;
- pfSense config/log observation;
- brief direct interpretation;
- bounded correlation supported by independent artifacts.

Reserved for Chapter 4:
- CIA impact;
- risk/severity ranking;
- enterprise recommendations;
- defense-in-depth strategy;
- patch-management policy;
- cost-benefit;
- compatibility policy;
- residual risk;
- real-world exploitability beyond the experiment.

## 7. Negative-result policy

Scenario 2 and Case B:
- smb-vuln-ms17-010 with no usable result = UNKNOWN / NO USABLE SCRIPT RESULT.
- Never SAFE, NOT VULNERABLE or VULNERABLE.
- Never invent NTSTATUS output.

Case C:
- raw Nmap fact = filtered / no-response;
- generic meaning = Nmap did not receive enough response to classify open/closed;
- separate pfSense log fact = matching SMB SYN traffic shown with Block action;
- exact named-rule attribution remains unresolved.

## 8. Patch-state lock

Windows Server 2012 R2:
- display FileVersion String: 6.3.9600.16384;
- numeric srv.sys: 6.3.9600.16421;
- official minimum updated version: 6.3.9600.18604;
- KB mapping: KB4012213 / KB4012216 or superseding update;
- local classification: UNPATCHED.

Local patch state and remote NSE signal are independent.

## 9. Core interpretation locks

- 445 OPEN != vulnerable
- SMBv1 enabled != MS17-010 confirmed
- UNKNOWN != SAFE
- FILTERED != PATCHED
- SMBv1 disabled != PATCHED

Case B:
- SMB1 True -> False locally;
- FS-SMB1 remains installed;
- SMB2=True;
- LanmanServer Running;
- remote SMBv1 dialect disappears;
- SMB2/SMB3 dialects remain observable;
- do not claim full file-sharing workload validation.

## 10. Scenario 1 facts

Report:
- B2: .56.1, .56.10, .56.20, .56.100 observed up;
- .56.100 identity UNKNOWN;
- B3: .56.20 up;
- B4: 139/tcp open, 445/tcp open;
- B5 fingerprint: Microsoft Windows netbios-ssn; Microsoft Windows Server 2008 R2–2012 microsoft-ds;
- B6 dialects: NT LM 0.12, 2.0.2, 2.1, 3.0, 3.0.2;
- signing enabled but not required;
- capabilities as recorded;
- smb-os-discovery no usable output.

Do not identify exact OS version from Nmap fingerprint alone.

## 11. Scenario 2 facts

Report:
- NSE-SMB-01: 139/445 open;
- NSE-SMB-02: SMBv1 + SMB2/3 dialects;
- NSE-SMB-03: signing enabled but not required;
- NSE-SMB-04: 445 open; no Host script result; no usable vulnerability verdict.

Key distinction:
remote result = UNKNOWN;
local patch state = UNPATCHED.

## 12. Case C facts

Report configuration evidence separately from scan results.

- 139/445 filtered/no-response from Kali;
- pfSense log independently shows matching TCP SYN traffic .56.10 -> .56.20:139/445 with Block action;
- exact named-rule attribution remains unresolved;
- local Windows remains SMB1=True, SMB2=True, LanmanServer Running, local 139/445 listening, UNPATCHED.

Never say:
- machine safe;
- all attack surface removed;
- remote vulnerability proven;
- script completely disabled.

## 13. Main result tables

Draft R1 uses exactly 6 main tables:
- Bảng 3.1 — Trạng thái baseline trước đo đạc.
- Bảng 3.2 — Kết quả Kịch bản 1.
- Bảng 3.3 — Kết quả Kịch bản 2.
- Bảng 3.4 — Đối chiếu trước/sau Case B.
- Bảng 3.5 — Kết quả Case C.
- Bảng 3.6 — So sánh Baseline / Case B / Case C.

Tables condense facts; they do not reproduce full raw logs.
Every table is introduced before it appears and followed by concise commentary.

## 14. Evidence images

Draft R1 embeds exactly 8 staged images:

1. Hình 3.1 — chapter3/evidence/baseline/Windows_MS17010_01_SrvSysVersion.png
2. Hình 3.2 — chapter3/evidence/scenario1/Scenario1_B6_SMB_NSE_A.png
3. Hình 3.3 — chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png
4. Hình 3.4 — chapter3/evidence/case_b/SMBv1_Remediation_03_After_Local.png
5. Hình 3.5 — chapter3/evidence/case_b/SMBv1_Remediation_04_NSE02_Protocols.png
6. Hình 3.6 — chapter3/evidence/case_c/pfSense_08_Rule_Order.png
7. Hình 3.7 — chapter3/evidence/case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png
8. Hình 3.8 — chapter3/evidence/case_c/pfSense_10_Block_Log_CANONICAL.png

Do not add screenshots in Draft R1.

Do not edit source evidence. If a crop is later needed, keep the source unchanged and create a derived presentation copy.

## 15. Figure commentary rule

Before every figure:
- tell the reader what to look at.

After every figure:
- state the direct observation;
- explain one immediate meaning;
- state a limitation when necessary.

Captions must not contain conclusions not visible in the figure.

## 16. Citation policy

Experimental observations are project results.

External citations are only needed for external rules/semantics such as:
- Microsoft KB/version mapping;
- Nmap semantics when required.

Use only VERIFIED entries in SOURCE_LEDGER.md.
Do not invent new bibliography numbering.

## 17. Draft size

Target roughly 3,000–4,000 words of prose/commentary, 6 tables, 8 figures.
No padding and no long repeated command blocks.

## 18. Draft status

X7 Draft R1 is a review draft.
No final Chapter 3 DOCX is created in this phase.
