# Evidence Audit R2 — ALL(1).zip

Status: `AUDITED_WITH_ONE_BOUNDED_CONFLICT`  
Date: 2026-10-06  
Scope: normalized evidence layer for Chapters 2–4.

## 1. Audit objective

The goal is not to make a claim of philosophical or cryptographic “absolute certainty”. The goal is to make every report fact:
1. traceable to exact source bytes;
2. reproducible from the archive;
3. bounded by evidence grade;
4. protected against chronology and summary-prose errors;
5. explicit when direct artifacts conflict.

## 2. Source-package integrity

Verified source archive:
- name: `ALL(1).zip`;
- compressed size: 28,547,199 bytes;
- SHA-256: `dc63f3ba5ed514f0c6b5e947474baca712c15a4c08c42b2228e421512cb04ff3`;
- regular files: 174;
- extracted file bytes total: 30,910,261 bytes.

Extension counts:
- PNG: 104
- TXT: 24
- NMAP: 13
- XML: 13
- GNMAP: 13
- DOCX: 6
- LOG: 1

A full byte-level inventory is stored in:
`FULL_ARCHIVE_MANIFEST_ALL_2026_10_06.csv`.

## 3. Rebuilt classification

The earlier legacy counts in `EVIDENCE_REGISTER.md` are superseded by the full-file audit.

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

Detected exact byte duplicates:
1. `Windows_Baseline_02_SystemInfo_OS.png` == `Windows_Baseline_03_SystemInfo_Hotfix.png`.
2. `pfSense_05_Bridge_Filtering.png` == `pfSense_tunables.png`.

Superseded but not byte-identical:
- `pfSense_CaseC_09_NSE01_Ports.png` is superseded by `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`.

## 4. Machine-generated Nmap consistency

All 13 canonical scan groups contain the expected three siblings:
- `.nmap`;
- `.xml`;
- `.gnmap`.

For every group, Nmap argv is identical across:
- `.nmap` first-line header;
- XML root `args`;
- `.gnmap` first-line header.

Result: **13/13 triplets PASS**.

The observable states/scripts were also cross-checked between human-readable Nmap output and XML:
- Scenario 1 B4/B5: TCP 139/445 open.
- Scenario 1 B6: protocols/capabilities/signing; no usable `smb-os-discovery`.
- Scenario 2 01: ports open.
- Scenario 2 02: SMBv1 + SMB2/3 dialects.
- Scenario 2 03: signing enabled but not required.
- Scenario 2 04: no host-script verdict.
- Case B protocols: SMB1 absent, SMB2/3 remain.
- Case B MS17-010: no host-script verdict.
- Case C ports: 139/445 filtered, no-response.
- Case C MS17-010: 445 filtered, no host-script verdict.

## 5. Command provenance correction

A defect was found in the first normalized layer: it sometimes treated shell/operator commands and Nmap-recorded argv as one “exact command”.

This is now corrected by `COMMAND_LINEAGE_MATRIX.md`.

Key rule:
- `sudo` belongs to operator-command provenance when recorded in manifest/screenshot.
- `--privileged` belongs to Nmap raw provenance when recorded in Nmap argv.
- Neither is silently copied into the other representation.

## 6. Chronology locks

### Kali tool state
`Kali_Baseline.txt` is an early state where Nmap was not yet installed. It is **not** the final demo baseline.

The later final pre-demo audit records:
- Kali `192.168.56.10/24`;
- no default route;
- Nmap 7.99;
- required NSE scripts present.

### Snapshot timing
`Final_PreDemo_Audit.txt` at approximately 08:20 records `Before Demo Exists: NO`.

`Before_Demo_Snapshots.txt` at approximately 08:22 records `Before Demo` as current on Kali and Windows.

Therefore the final state is: snapshots exist. The two files represent different points in chronology, not conflicting final truth.

### Case C
`RUN4_PAUSE_STATE_REPORT.txt` contains both failed/paused historical material and a later Section 21 `FINAL BOUNDED COMPLETION CLOSURE`.

Only the final closure may support final Case C chronology; earlier diagnostic sections remain troubleshooting/history.

## 7. Direct-vs-secondary evidence grading for Case C

### Interface and bridge
Direct screenshots support:
- `pfSense_03_Interface_Assignment.png`: CASE_C_KALI=em2 and CASE_C_WINDOWS=em3.
- `pfSense_04_Bridge.png`: bridge0 contains CASE_C_KALI and CASE_C_WINDOWS.

The internal-network names and management plane are also recorded in the final manifest/closure:
- data plane: `ATTT-PFS-KALI` and `ATTT-PFS-WIN`;
- management: Host `.57.1` ↔ pfSense em1 `.57.2`.

### Tunables
Direct screenshot `pfSense_05_Bridge_Filtering.png` proves:
- `net.link.bridge.pfil_member = 1`;
- `net.link.bridge.pfil_bridge = 0`.

The value:
- `net.link.bridge.pfil_onlyip = 1`

is supported by final manifest/closure text, but is not visible in that screenshot. It is therefore classified as **SECONDARY_META_SUPPORTED**, not direct screenshot evidence.

### Rule configuration
Direct screenshots prove:
- a BLOCK IPv4 TCP rule exists on CASE_C_KALI;
- source `.56.10`;
- destination `.56.20`;
- alias `SMB_Ports`;
- logging enabled;
- description `CASE C - Block SMB Kali to Windows`;
- block row is ordered above the pass row.

## 8. Case C firewall-log conflict

A real direct-evidence conflict exists and is intentionally preserved.

The final manifest/closure claims that canonical firewall-log rows match:
- rule `CASE C - Block SMB Kali to Windows`;
- ID `1000000104`.

However, the visible rows at the canonical scan time in:
`pfSense_10_Block_Log_CANONICAL.png`

show:
- red X / blocked action;
- interface CASE_C_KALI;
- source `192.168.56.10`;
- destination `192.168.56.20:139` and `:445`;
- TCP SYN;
- visible rule label `CASE C baseline pass Kali to Windows (100000104)`.

This means the direct screenshot proves that the matching SMB SYN traffic was **blocked in the pfSense path**, but it does **not** prove the manifest's exact named-rule attribution.

Audit classification:
`CONFLICTING_EVIDENCE — RULE_LABEL_ATTRIBUTION_UNRESOLVED`.

Allowed claim:
> During the canonical scan, pfSense firewall logs show blocked TCP SYN traffic from Kali `.56.10` to Windows `.56.20` on TCP 139/445 at CASE_C_KALI.

Not allowed until separately resolved:
> Those log rows are definitively the named `CASE C - Block SMB Kali to Windows` rule.

The configured block rule itself is independently proven by `pfSense_07_Block_Rule_Config.png` and `pfSense_08_Rule_Order.png`.

## 9. Negative-result boundary

The raw evidence continues to support:
- Scenario 2 MS17-010: `UNKNOWN / NO USABLE SCRIPT RESULT`.
- Case B MS17-010: `UNKNOWN / NO USABLE SCRIPT RESULT`.
- Case C: TCP 445 filtered; no MS17-010 verdict.

No summary explanation is allowed to turn no-output into a causal conclusion unless a direct artifact supports it.

## 10. Local patch-state boundary

Local Windows evidence supports:
- FileVersion String visible as `6.3.9600.16384`;
- constructed/numeric version `6.3.9600.16421`;
- Microsoft reference threshold `6.3.9600.18604`;
- local classification `UNPATCHED` under the project's official mapping.

External Microsoft sources in the Source Ledger remain required when this mapping is cited academically.

## 11. Quality verdict

After R2 corrections, the evidence layer is:
- byte-traceable;
- chronology-aware;
- command-lineage-aware;
- explicit about direct vs secondary evidence;
- protected against unsupported negative-result inference;
- explicit about one unresolved Case C rule-label conflict.

Therefore the layer is suitable as the internal factual substrate for revised Chapter 2 and later Chapter 3/4.

It is **not** permissible to describe the package as “100% free of uncertainty”, because the Case C rule-label attribution conflict is real. Accuracy is achieved by preserving and bounding that conflict rather than hiding it.
