# EVIDENCE INGEST — ALL(1).zip (2026-10-06)

Status: `AUDITED_R2_WITH_BOUNDED_CONFLICT`

## 1. Source package

- User-supplied archive: `ALL(1).zip`
- Archive size: 28,547,199 bytes
- SHA-256: `dc63f3ba5ed514f0c6b5e947474baca712c15a4c08c42b2228e421512cb04ff3`
- Regular files: 174
- Extracted file bytes: 30,910,261
- Full byte inventory: `FULL_ARCHIVE_MANIFEST_ALL_2026_10_06.csv`

Extension counts:
- PNG 104
- TXT 24
- NMAP 13
- XML 13
- GNMAP 13
- DOCX 6
- LOG 1

The archive is a provenance/evidence container only. Its directory structure is not a report outline.

## 2. Evidence precedence

1. machine-generated raw output / direct local-state evidence;
2. direct canonical screenshot;
3. final manifest or bounded final closure when consistent with direct evidence;
4. summary interpretation;
5. historical report.

A lower-grade artifact may add a fact only when it does not conflict with a higher-grade artifact and the evidence grade remains explicit.

## 3. Baseline identity

- Oracle VM VirtualBox 7.2.20; later records support exact build `7.2.20r175154`.
- Kali `192.168.56.10/24`.
- Windows Server 2012 R2 Standard Evaluation Build 9600 `192.168.56.20/24`.
- Baseline network: one Host-Only NIC per Kali/Windows VM; no NAT/Bridged NIC; no default route in final pre-demo VM state.
- Host-Only `192.168.56.0/24`; host adapter `.56.1/24`; DHCP disabled.
- Nmap 7.99 in final pre-demo state.
- `Before Demo` snapshot exists/current after the snapshot step.

Windows:
- LanmanServer Running/Automatic.
- TCP 139/445 Listening.
- SMB1=True; SMB2=True; FS-SMB1 Installed.
- scoped custom Windows Firewall allow rule for TCP 139/445 from `.56.10`; default File and Printer Sharing group not opened wholesale.

Patch:
- displayed FileVersion String `6.3.9600.16384`;
- numeric `srv.sys 6.3.9600.16421`;
- Microsoft mapping threshold `6.3.9600.18604`;
- project local classification `UNPATCHED`.

## 4. Command lineage

Do not treat shell/operator command and Nmap raw argv as identical strings.

Authoritative matrix:
`COMMAND_LINEAGE_MATRIX.md`.

All 13 scan groups have consistent `.nmap/.xml/.gnmap` argv: **13/13 PASS**.

## 5. Scenario 1 observations

Raw supports:
- B2: `.56.1`, `.56.20`, `.56.100`, `.56.10` observed up at that measurement.
- B3: target `.56.20` up.
- B4: TCP 139/445 open, `syn-ack ttl 128`.
- B5: 139 Windows netbios-ssn; 445 Microsoft Windows Server 2008 R2–2012 microsoft-ds fingerprint.
- B6: SMBv1 NT LM 0.12 plus 2.0.2/2.1/3.0/3.0.2; 3.0.2 signing enabled but not required; listed capabilities; no usable `smb-os-discovery` output.

No MS17-010 verdict may be derived from Scenario 1.

## 6. Scenario 2 observations

Raw supports:
- 139/445 open;
- SMBv1 + SMB2/3 dialects;
- signing enabled but not required;
- `smb-vuln-ms17-010`: host/445 reachable but no Host script result/verdict.

Classification:
`UNKNOWN / NO USABLE SCRIPT RESULT`.

Local patch state remains a separate axis:
`UNPATCHED`.

## 7. Case B

Direct/local and raw evidence supports:
- before: SMB1=True, SMB2=True, FS-SMB1 Installed, LanmanServer Running;
- action: `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`;
- after: SMB1=False, SMB2=True, FS-SMB1 still Installed, LanmanServer Running;
- protocol retest: NT LM 0.12 absent; SMB2/3 dialects remain;
- MS17-010 retest: no Host script result/verdict;
- local patch state remains UNPATCHED.

Do not adopt summary-only causal explanations for the missing NSE verdict.

## 8. Case C

Case C is a separate topology and must not be projected backward into baseline.

Direct screenshots support:
- CASE_C_KALI=em2; CASE_C_WINDOWS=em3;
- bridge0 contains both Case C member interfaces;
- `pfil_member=1`, `pfil_bridge=0`;
- configured BLOCK IPv4 TCP rule on CASE_C_KALI, source `.56.10`, destination `.56.20`, SMB_Ports, logging enabled;
- block row above pass row.

Final manifest/closure additionally supports:
- data-plane Internal Networks `ATTT-PFS-KALI` and `ATTT-PFS-WIN`;
- management Host `.57.1` ↔ pfSense em1 `.57.2`;
- `pfil_onlyip=1`;
- pfSense CE 2.9.0-RELEASE;
- snapshot `Before Case C`.

Canonical raw supports:
- 139/445 filtered/no-response from Kali;
- MS17-010 retest: 445 filtered, no script verdict.

### Case C log conflict
The canonical log screenshot directly shows blocked TCP SYN from `.56.10` to `.56.20:139/445` on CASE_C_KALI at the scan time.

But the screenshot's visible rule label is `CASE C baseline pass Kali to Windows (100000104)`, while the manifest/closure claims `CASE C - Block SMB Kali to Windows (1000000104)`.

Therefore exact named-rule attribution is unresolved.

Allowed:
- pfSense path blocked the matching SMB SYN traffic during the canonical scan.

Not allowed:
- the log screenshot definitively proves that the configured named Block rule was the matched rule.

The existence/configuration/order of the Block rule is independently direct evidence.

## 9. Chronology locks

1. `Kali_Baseline.txt` predates Nmap installation; final pre-demo audit supersedes it for tool state.
2. Pre-demo audit at ~08:20 precedes creation of `Before Demo`; snapshot verification at ~08:22 establishes final snapshot state.
3. `RUN4_PAUSE_STATE_REPORT.txt` is mixed chronology; only Section 21 is final closure.
4. Case C pre-repair/aborted/debug artifacts are not canonical result evidence.
5. Case A patching is not a completed experiment in this package.

## 10. Classification rebuild

The full-file audit supersedes prior legacy count summaries:

- PRIMARY_RAW 39
- PRIMARY_VISUAL 33
- PRIMARY_LOCAL_STATE 5
- SECONDARY_META 4
- SECONDARY_INTERPRETATION 4
- SUPPORTING 35
- SUPPORTING_BASELINE 7
- HISTORICAL_EARLY_STATE 7
- TROUBLESHOOTING 31
- SOURCE_AUTHORITY 3
- HISTORICAL_REFERENCE 2
- STYLE_REFERENCE 1
- EXCLUDED_BYTE_DUPLICATE 2
- EXCLUDED_SUPERSEDED 1

Total 174.

## 11. Audit references

- `EVIDENCE_AUDIT_R2_ALL_2026_10_06.md`
- `FULL_ARCHIVE_MANIFEST_ALL_2026_10_06.csv`
- `COMMAND_LINEAGE_MATRIX.md`
- `CANONICAL_EVIDENCE_MAP_ALL_ZIP.md`
- `CANONICAL_NMAP_TEXT_OUTPUTS.md`
- `EVIDENCE_USE_POLICY_ALL_ZIP.md`

## 12. Report-architecture boundary

This ingest is not an outline. Report structure is designed independently, then claims are bound to these artifacts.
