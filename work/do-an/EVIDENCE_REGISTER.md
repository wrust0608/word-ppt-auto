# EVIDENCE REGISTER — ALL(1).zip AUDITED R2

Trạng thái: `CANONICAL_EVIDENCE_REGISTER_R2`  
Ngày audit: 2026-10-06  
Nguồn byte gốc: `ALL(1).zip`

## 1. Identity của gói nguồn

- ZIP size: **28,547,199 bytes**
- SHA-256: `dc63f3ba5ed514f0c6b5e947474baca712c15a4c08c42b2228e421512cb04ff3`
- Regular files: **174**
- Extracted bytes: **30,910,261**

Full inventory:
`work/do-an/evidence/ALL_2026_10_06/FULL_ARCHIVE_MANIFEST_ALL_2026_10_06.csv`

Forensic review:
`work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R2_ALL_2026_10_06.md`

## 2. Phân loại toàn bộ 174 file

| Class | Count |
|---|---:|
| PRIMARY_RAW | 39 |
| PRIMARY_VISUAL | 33 |
| PRIMARY_LOCAL_STATE | 5 |
| SECONDARY_META | 4 |
| SECONDARY_INTERPRETATION | 4 |
| SUPPORTING | 35 |
| SUPPORTING_BASELINE | 7 |
| HISTORICAL_EARLY_STATE | 7 |
| TROUBLESHOOTING | 31 |
| SOURCE_AUTHORITY | 3 |
| HISTORICAL_REFERENCE | 2 |
| STYLE_REFERENCE | 1 |
| EXCLUDED_BYTE_DUPLICATE | 2 |
| EXCLUDED_SUPERSEDED | 1 |
| **TOTAL** | **174** |

Các số đếm X1 cũ `109 canonical / 35 supporting / 23 troubleshooting / 1 duplicate` được **supersede** bởi phân loại R2 này vì R2 kiểm kê toàn bộ 174 file theo exact path + SHA-256.

## 3. Thứ tự ưu tiên bằng chứng

1. Machine-generated raw output hoặc direct local-state artifact.
2. Direct screenshot của đúng trạng thái/lượt canonical.
3. Final run manifest / final bounded closure nếu không mâu thuẫn direct evidence.
4. Summary/interpretation.
5. Historical reports.

Nếu direct artifact và manifest mâu thuẫn:
- giữ cả hai;
- gắn `CONFLICTING_EVIDENCE`;
- không “hòa giải” bằng suy đoán;
- claim tối đa phải bám direct artifact.

## 4. Core stable IDs

Exact archive paths, SHA-256 và evidence grade nằm tại:

`work/do-an/evidence/ALL_2026_10_06/CANONICAL_EVIDENCE_MAP_ALL_ZIP.md`

### Environment
- `ENV-CORE-01`: final pre-demo audit.
- `ENV-CORE-02`: final `Before Demo` snapshot verification.
- `ENV-CORE-03`: MS17-010 local patch mapping/state.
- `ENV-CORE-04`: final Windows Firewall lab-rule audit.
- `ENV-CORE-05`: baseline Host-Only/NIC configuration.
- `ENV-HIST-01`: early Kali pre-Nmap state; **not final demo baseline**.
- `ENV-SUP-01`: early Windows baseline; subordinate to final state.

### Scenario 1
- `S1-RAW-01` subnet discovery.
- `S1-RAW-02` target alive.
- `S1-RAW-03` TCP 139/445.
- `S1-RAW-04` service/version.
- `S1-RAW-05` SMB NSE.
- `S1-META-01` operator-command/run metadata.

### Scenario 2
- `S2-RAW-01` ports.
- `S2-RAW-02` protocols.
- `S2-RAW-03` signing.
- `S2-RAW-04` MS17-010 remote probe.
- `S2-META-01` operator-command/run metadata.

### Case B
- `B-LOCAL-01` before.
- `B-ACTION-01` disable action.
- `B-LOCAL-02` after.
- `B-RAW-01` protocol retest.
- `B-RAW-02` MS17-010 retest.
- `B-META-01` operator-command/run metadata.

### Case C
- `C-IFACE-01`: interface assignment.
- `C-BRIDGE-01`: bridge membership.
- `C-TUNE-DIRECT-01`: direct screenshot proving pfil_member=1 and pfil_bridge=0.
- `C-RULE-01`: baseline pass rule.
- `C-RULE-02`: configured block rule.
- `C-RULE-03`: block-over-pass order.
- `C-RAW-01`: 139/445 filtered retest.
- `C-RAW-02`: MS17-010 retest through filtered path.
- `C-VIS-01`: canonical port screenshot.
- `C-LOG-01`: canonical firewall log, **CONFLICTING rule-label attribution**.
- `C-VIS-02`: canonical MS17-010 screenshot.
- `C-META-01`: final manifest; supports operator commands, topology names, `pfil_onlyip=1`, version/snapshot.
- `C-CLOSURE-01`: mixed chronology; only Section 21 is final closure.

## 5. Nmap raw integrity

There are **13 canonical scan groups**, each with:
- `.nmap`
- `.xml`
- `.gnmap`

For all 13 groups, the Nmap argv is identical across the three formats.

Result: **13/13 PASS**.

Repo-local readable raw snapshot:
`work/do-an/evidence/ALL_2026_10_06/CANONICAL_NMAP_TEXT_OUTPUTS.md`

Operator-vs-raw command lineage:
`work/do-an/evidence/ALL_2026_10_06/COMMAND_LINEAGE_MATRIX.md`

## 6. Chronology locks

1. `Kali_Baseline.txt` is historical pre-Nmap state. Final pre-demo audit supersedes it for tool state.
2. `Final_PreDemo_Audit.txt` records no `Before Demo` snapshot at ~08:20; `Before_Demo_Snapshots.txt` verifies its creation/current state at ~08:22. Final truth: snapshot exists.
3. `RUN4_PAUSE_STATE_REPORT.txt` contains both troubleshooting history and later final closure. Only Section 21 supports final Case C closure.
4. Case C pre-repair/aborted/debug attempts are not canonical result evidence.
5. No complete Case A patch experiment exists.

## 7. Case C evidence-grade lock

### Directly proven
- CASE_C_KALI=em2 and CASE_C_WINDOWS=em3.
- bridge0 membership.
- `pfil_member=1`, `pfil_bridge=0`.
- Block rule config: IPv4 TCP, source `.56.10`, destination `.56.20`, SMB_Ports, logging enabled.
- Block row above pass row.
- canonical retest: 139/445 filtered/no-response.
- canonical MS17-010 retest: 445 filtered, no script verdict.
- firewall log at canonical scan time: blocked TCP SYN from `.56.10` to `.56.20:139/445` on CASE_C_KALI.

### Supported by final metadata, not direct screenshot
- data-plane Internal Network names `ATTT-PFS-KALI`, `ATTT-PFS-WIN`.
- management Host `.57.1` ↔ pfSense em1 `.57.2`.
- `pfil_onlyip=1`.
- pfSense CE 2.9.0-RELEASE.
- snapshot `Before Case C`.

### Unresolved conflict
`C-LOG-01` visible Rule label:
`CASE C baseline pass Kali to Windows (100000104)`

Manifest/closure says:
`CASE C - Block SMB Kali to Windows (1000000104)`.

Allowed claim:
**pfSense log shows the matching SMB SYN traffic was blocked in the pfSense path during the canonical scan.**

Forbidden until resolved:
**the log rows definitively match the configured named Case C Block rule.**

The configured Block rule's existence and order remain independently proven by `C-RULE-02` and `C-RULE-03`.

## 8. Negative result policy

- Scenario 2 MS17-010: `UNKNOWN / NO USABLE SCRIPT RESULT`.
- Case B MS17-010: `UNKNOWN / NO USABLE SCRIPT RESULT`.
- Case C MS17-010: 445 filtered, no verdict -> `UNKNOWN` from that vantage point.
- Local patch state: `UNPATCHED` is independent from remote verdict.

Do not create causes, statuses, NTSTATUS values, exploit success, or safety claims absent from direct evidence.

## 9. Duplicate/exclusion lock

Exact byte duplicates:
1. `Windows_Baseline_02_SystemInfo_OS.png` == `Windows_Baseline_03_SystemInfo_Hotfix.png`.
2. `pfSense_05_Bridge_Filtering.png` == `pfSense_tunables.png`.

Superseded noncanonical:
- `pfSense_CaseC_09_NSE01_Ports.png` -> use `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`.

## 10. Provenance boundary for Chapters 2–4

Archive folders are **not** report sections.

Chapter structure must be designed independently. After structure is approved:
- Chapter 2 maps method/configuration claims to this register.
- Chapter 3 maps each result claim to raw/direct evidence.
- Chapter 4 compares only verified states.

No Chapter 3 prose is permitted before CP5-USER approval of revised Chapter 2.
