# Evidence Use Policy for ALL(1).zip

Status: `AUDITED_R2`

## 1. Evidence grades

### PRIMARY_RAW
Machine-generated Nmap `.nmap/.xml/.gnmap` from the final run path. Highest authority for remote scan command argv and output.

### PRIMARY_LOCAL_STATE
Direct text/audit captured from the local system or hypervisor final state.

### PRIMARY_VISUAL
Screenshot directly showing local state, rule configuration/order, or final scan output.

### SECONDARY_META
Run manifest / bounded closure. May support chronology, operator command, topology names, or configuration facts not directly visible elsewhere. It must not override contradictory direct evidence.

### SECONDARY_INTERPRETATION
Summary prose. Use only for navigation/context. Do not promote causal interpretation beyond raw/direct evidence.

### SUPPORTING / HISTORICAL / TROUBLESHOOTING
Preserve for provenance but do not use as primary result evidence.

## 2. Command provenance

Use `COMMAND_LINEAGE_MATRIX.md`.

- Operator command: manifest/screenshot.
- Nmap-recorded argv: raw triplet.
- Do not infer `sudo` from Nmap raw.
- Do not infer operator-entered `--privileged` from Nmap raw.

## 3. Primary result set

Use as primary:
- final pre-demo state and snapshot verification;
- Windows patch/firewall final state;
- Scenario 1 raw triplets;
- Scenario 2 raw triplets;
- Case B local before/action/after + final raw retests;
- Case C direct interface/bridge/rule/order screenshots + final raw retests + canonical firewall log.

## 4. Case C special boundaries

### Tunables
Direct screenshot proves:
- `pfil_member=1`;
- `pfil_bridge=0`.

`pfil_onlyip=1` is supported by final manifest/closure text and is therefore `SECONDARY_META_SUPPORTED`, not screenshot-proven.

### Firewall log
`pfSense_10_Block_Log_CANONICAL.png` directly shows blocked TCP SYN on CASE_C_KALI from `.56.10` to `.56.20:139/445` during the canonical scan.

However, its visible Rule label is:
`CASE C baseline pass Kali to Windows (100000104)`

while the manifest/closure claims:
`CASE C - Block SMB Kali to Windows (1000000104)`.

Therefore:
- allowed: traffic was blocked in the pfSense path;
- not allowed: exact named-rule attribution is proven by the log screenshot.

Classification:
`CONFLICTING_EVIDENCE — RULE_LABEL_ATTRIBUTION_UNRESOLVED`.

The configured Block rule itself is independently proven by `pfSense_07_Block_Rule_Config.png` and rule order by `pfSense_08_Rule_Order.png`.

## 5. Negative-result rule

- Scenario 2 NSE-SMB-04: no Host script result -> `UNKNOWN / NO USABLE SCRIPT RESULT`.
- Case B NSE-SMB-04: no Host script result -> `UNKNOWN / NO USABLE SCRIPT RESULT`.
- Case C NSE-SMB-04: 445 filtered; no script verdict -> `UNKNOWN` from this vantage point.

Never manufacture `SAFE`, `NOT VULNERABLE`, `VULNERABLE`, or an NTSTATUS not present in raw output.

## 6. Exclusions

Do not use as primary experimental result:
- `HostRepair/*`;
- pre-repair/aborted/debug Case C runs;
- console/assign/ip/php/touch/sshd/ctrl-c diagnostics;
- old DOCX reports;
- summary prose that exceeds raw/direct evidence.

`RUN4_PAUSE_STATE_REPORT.txt` is mixed chronology. Only Section 21 final closure may support final Case C chronology; earlier sections remain troubleshooting/history.

## 7. Report architecture

Archive folder names are provenance only. They must not be copied into Chapter 2/3/4 structure.
