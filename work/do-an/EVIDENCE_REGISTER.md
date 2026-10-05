# EVIDENCE REGISTER — X1

Trạng thái: `X1_REVIEW_PENDING`
Ngày: 2026-10-05
Nguồn: `ALL.zip` do người dùng cung cấp.

## 1. Phân loại toàn gói evidence

- Tổng file evidence trong 5 nhóm `00_Environment` → `04_Remediation_pfSense`: **168**
- `CANONICAL`: **109**
- `SUPPORTING`: **35**
- `TROUBLESHOOTING`: **23**
- `EXCLUDED_DUPLICATE`: **1**

Quy tắc ưu tiên: raw/local state > manifest/summary > screenshot > historical report.

## 2. Core canonical evidence dùng để ánh xạ claim

| ID | Artifact | Vai trò | Claim tối đa |
|---|---|---|---|
| ENV-CORE-01 | `00_Environment.../PreDemo/Final_PreDemo_Audit.txt` | Canonical pre-demo state | OS/network/tool/SMB state tại thời điểm trước demo |
| ENV-CORE-02 | `00_Environment.../PreDemo/Before_Demo_Snapshots.txt` | Snapshot lineage | snapshot `Before Demo` |
| ENV-CORE-03 | `00_Environment.../PatchBaseline/MS17-010_Official_Mapping.txt` | Local patch ground truth | Windows target = UNPATCHED theo mapping đã đối chiếu |
| ENV-CORE-04 | `00_Environment.../FirewallPrep/Windows_FirewallPrep_Final.txt` | Windows firewall prep | phạm vi rule phục vụ lab |
| ENV-CORE-05 | `00_Environment.../Network/VirtualBox_HostOnly_Config.txt` | Network design | Host-Only baseline |
| ENV-CORE-06 | `00_Environment.../Baseline/Kali/Kali_Baseline.txt` | Kali baseline | IP/route/tool baseline |
| ENV-CORE-07 | `00_Environment.../Baseline/Windows/Windows_Baseline.txt` | Windows baseline | OS/SMB/service/firewall baseline |
| S1-RAW-01 | `01_Scenario1.../raw/b2_host_discovery.*` | Scenario 1 host discovery | target/subnet host observation |
| S1-RAW-02 | `01_Scenario1.../raw/b3_target_alive.*` | Target reachability | target alive at measurement time |
| S1-RAW-03 | `01_Scenario1.../raw/b4_smb_ports.*` | TCP 139/445 | ports open from Kali; no vulnerability inference |
| S1-RAW-04 | `01_Scenario1.../raw/b5_smb_version.*` | Service fingerprint | SMB/microsoft-ds service fingerprint |
| S1-RAW-05 | `01_Scenario1.../raw/b6_smb_nse.*` | SMB NSE enumeration | SMB dialect/signing/capability observations only |
| S1-META-01 | `Scenario1_Run_Manifest.txt` + `Scenario1_Summary.txt` | Run metadata | subordinate to raw |
| S2-RAW-01 | `02_Scenario2.../raw/NSE-SMB-01_ports.*` | Reachability | 139/445 open |
| S2-RAW-02 | `02_Scenario2.../raw/NSE-SMB-02_protocols.*` | Protocols | NT LM 0.12 + SMB2/3 dialect observations |
| S2-RAW-03 | `02_Scenario2.../raw/NSE-SMB-03_signing.*` | Signing | signing observation only |
| S2-RAW-04 | `02_Scenario2.../raw/NSE-SMB-04_ms17010.*` | MS17-010 remote probe | `UNKNOWN / NO USABLE SCRIPT RESULT` |
| S2-META-01 | `Scenario2_Run_Manifest.txt` + `Scenario2_Summary.txt` | Run metadata | subordinate to raw |
| B-LOCAL-01 | `SMBv1_Remediation_01_Before.png` | Case B before state | SMB1 enabled before intervention |
| B-ACTION-01 | `SMBv1_Remediation_02_Action.png` | Intervention | SMB1 disable action |
| B-LOCAL-02 | `SMBv1_Remediation_03_After_Local.png` | Case B after state | SMB1 disabled; other local states as shown |
| B-RAW-01 | `03_Remediation_SMBv1.../raw/NSE-SMB-02_protocols.*` | Protocol retest | NT LM 0.12 no longer appears; SMB2/3 remain |
| B-RAW-02 | `03_Remediation_SMBv1.../raw/NSE-SMB-04_ms17010.*` | MS17-010 retest | remote verdict remains UNKNOWN |
| B-META-01 | `SMBv1_Remediation_Run_Manifest.txt` + `SMBv1_Remediation_Summary.txt` | Case B metadata | subordinate to raw/local state |
| C-TOPO-01 | `pfSense_04_Bridge.png` + `pfSense_05_Bridge_Filtering.png` | Case C topology | transparent bridge/filtering setup |
| C-RULE-01 | `pfSense_06_Baseline_Pass_Rule.png` | baseline rule | pre-block pass behavior |
| C-RULE-02 | `pfSense_07_Block_Rule_Config.png` + `pfSense_08_Rule_Order.png` | block policy | configured TCP 139/445 block in correct order |
| C-RAW-01 | `04_Remediation_pfSense.../raw/NSE-SMB-01_ports.*` | reachability retest | 139/445 filtered from Kali |
| C-LOG-01 | `pfSense_10_Block_Log_CANONICAL.png` | causal attribution | pfSense rule blocked matching SMB SYN traffic |
| C-RAW-02 | `04_Remediation_pfSense.../raw/NSE-SMB-04_ms17010.*` | MS17-010 retest | cannot classify through filtered path; UNKNOWN |
| C-META-01 | `pfSense_Remediation_Run_Manifest.txt` + `pfSense_Remediation_Summary.txt` | Case C metadata | subordinate to raw/log |

## 3. Supporting evidence classes

- Installation/basic screenshots and tool-install screenshots: `SUPPORTING`.
- VM config text and auxiliary pfSense interface/tunable screenshots: `SUPPORTING`.
- HostRepair, pfSense console experiments, PHP/touch/ctrl+c/repair logs: `TROUBLESHOOTING`.
- `pfSense_CaseC_09_NSE01_Ports.png`: `EXCLUDED_DUPLICATE`; canonical file is `_CANONICAL.png`.

## 4. Stable-ID rule

Chương 2–4 phải trỏ tới các ID core ở mục 2. Nếu cần một screenshot phụ, Evidence Map được phép trỏ path cụ thể nhưng claim vẫn phải neo vào raw/local-state core evidence tương ứng.

## 5. Provenance boundary

Evidence gốc hiện nằm trong gói `ALL.zip` do người dùng cung cấp, không mặc định commit binary vào Git. Repo lưu:
- stable Evidence ID;
- canonical path trong archive;
- SHA-256 manifest;
- conflict policy;
- inference boundary.

Nếu agent không truy cập được `ALL.zip` hoặc byte gốc, phải dừng phần cần evidence thay vì tái tạo từ report cũ.


## 6. ALL(1).zip normalized ingest — 2026-10-06

The user supplied a newer packaged product archive `ALL(1).zip`. It was independently extracted and audited without using its folder structure as a report outline.

Source provenance:
- archive size: 28,547,199 bytes;
- archive SHA-256: `dc63f3ba5ed514f0c6b5e947474baca712c15a4c08c42b2228e421512cb04ff3`;
- total extracted files: 174;
- experimental/evidence files inside the five evidence groups: 168;
- root reference/DOCX files: 6.

Normalized ingest files:
- `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_INGEST_ALL_2026_10_06.md`
- `work/do-an/evidence/ALL_2026_10_06/CANONICAL_COMMANDS_FROM_ALL_ZIP.md`
- `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_USE_POLICY_ALL_ZIP.md`
- `work/do-an/evidence/ALL_2026_10_06/CANONICAL_EVIDENCE_MAP_ALL_ZIP.md`

These files supersede memory-based reconstruction of exact commands, run chronology, and canonical-vs-troubleshooting classification.

Important lineage corrections locked by the ingest:
1. `Kali_Baseline.txt` is historical pre-tool state: Nmap was not yet installed.
2. Final pre-demo state later contains Nmap 7.99 and all required NSE scripts.
3. `Final_PreDemo_Audit.txt` at 08:20 precedes creation of `Before Demo`; `Before_Demo_Snapshots.txt` at 08:22 is the final snapshot state.
4. VirtualBox report prose should use 7.2.20; exact build `7.2.20r175154` is supported by later Case C/repair evidence if revision is needed.
5. Case C pre-repair/aborted/debug artifacts remain preserved but are excluded from canonical experimental conclusions.
6. No canonical Case A patch experiment exists in the archive.

For Chapters 2–4, exact Nmap command flags must come from `CANONICAL_COMMANDS_FROM_ALL_ZIP.md`, not from earlier prose drafts.
