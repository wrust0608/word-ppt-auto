# Evidence Audit R3 — Final Data Lock for ALL(1).zip

Status: `FINAL_DATA_LOCK_WITH_ONE_BOUNDED_CONFLICT`
Date: 2026-10-06
Scope: factual substrate for Chapters 2–4.

## 1. Independent re-review result

The normalized evidence layer was re-reviewed directly against the user-supplied ZIP rather than only against prior summaries.

Verified independently:
- ZIP SHA-256: `dc63f3ba5ed514f0c6b5e947474baca712c15a4c08c42b2228e421512cb04ff3`;
- regular files: 174;
- extension counts: PNG 104, TXT 24, NMAP 13, XML 13, GNMAP 13, DOCX 6, LOG 1;
- experimental/evidence files in groups 00–04: 168;
- root DOCX/reference files: 6;
- exact byte duplicates: exactly two duplicate pairs;
- 13 Nmap scan groups with complete .nmap/.xml/.gnmap triplets;
- core SHA-256 values in the canonical map match the ZIP bytes checked during review.

## 2. Logic review

### PASS — provenance
Each core claim has:
- exact archive path;
- SHA-256;
- evidence grade;
- bounded claim role.

### PASS — command lineage
Operator-entered commands and Nmap-recorded argv are separated.
No future report may call the raw header the literal shell command.

### PASS — chronology
The layer correctly distinguishes:
- early Kali pre-Nmap state from final pre-demo state;
- pre-snapshot audit from later snapshot creation;
- Case C troubleshooting history from final bounded closure.

### PASS — negative/inconclusive results
The layer preserves:
- Scenario 2 MS17-010 = UNKNOWN / NO USABLE SCRIPT RESULT;
- Case B MS17-010 = UNKNOWN / NO USABLE SCRIPT RESULT;
- Case C 445 filtered with no script verdict.

It does not manufacture SAFE/VULNERABLE/NOT VULNERABLE or missing NTSTATUS values.

### PASS — Case A boundary
No complete Case A patch experiment exists. Patching remains theory/recommendation unless new audited evidence is added.

## 3. Newly strengthened locks in R3

R3 adds four protections that were not explicit enough in R2:
1. cross-system timestamps are different clock domains; never sort global experiment chronology by displayed time strings alone;
2. local SMB-signing PowerShell flags and remote Nmap signing output are retained as separate observations rather than auto-reconciled;
3. B2 host .56.100 remains unidentified; disabled Host-Only DHCP and unrelated host NAT-network configuration must not be used to invent its identity or VM connectivity;
4. MS17-010 mapping artifact is composite: official Microsoft facts require official-source citation; local facts remain locally evidentiary.

Detailed rules:
`TIMEBASE_AND_CROSS_LAYER_LOCKS.md`.

## 4. Bounded unresolved conflict

Exactly one material direct-vs-secondary conflict remains in the canonical Case C evidence:

`pfSense_10_Block_Log_CANONICAL.png` shows matching blocked SMB SYN traffic but displays rule label:
`CASE C baseline pass Kali to Windows (100000104)`.

Manifest/closure attributes the traffic to:
`CASE C - Block SMB Kali to Windows (1000000104)`.

This conflict is preserved, not hidden.

It does not invalidate:
- configured Block-rule existence;
- Block-before-Pass ordering;
- filtered Nmap result;
- observed blocked SMB SYN traffic in pfSense logs.

It only prevents exact named-rule attribution from the log screenshot.

## 5. Accuracy verdict

The data layer is suitable as the authoritative internal factual substrate for Chapters 2–4 **provided all writing obeys the evidence grades and bounded conflict**.

The correct quality claim is:
`HIGH_ASSURANCE / TRACEABLE / BOUNDED_UNCERTAINTY`.

The incorrect quality claim would be:
`ABSOLUTELY CERTAIN / ZERO UNCERTAINTY`.

Absolute certainty cannot be honestly claimed because:
- the Case C rule-label conflict is real;
- some topology/tunable/version facts are supported by final metadata rather than independent direct screenshots;
- cross-system clocks are not normalized by an authenticated common time source.

Preserving these limits is part of accuracy, not a weakness.

## 6. Authoritative read order for future agents

Before writing experimental prose, read in this order:
1. `EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
2. `TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
3. `CANONICAL_EVIDENCE_MAP_ALL_ZIP.md`
4. `COMMAND_LINEAGE_MATRIX.md`
5. `EVIDENCE_USE_POLICY_ALL_ZIP.md`
6. `CANONICAL_NMAP_TEXT_OUTPUTS.md`
7. `EXPERIMENTAL_TRUTH_MATRIX.md`
8. source-specific artifact if the claim needs expansion.

Summary prose and historical reports are never the first authority.

## 7. Gate consequence

- Chapter 2 may now be redesigned against this locked data layer.
- Chapter 3 remains blocked until user explicitly approves revised Chapter 2.
- Chapter 3 must cite/map every result to raw/direct evidence.
- Chapter 4 may only compare verified/bounded states.
