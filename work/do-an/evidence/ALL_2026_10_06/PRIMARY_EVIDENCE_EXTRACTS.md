# Primary Evidence Extracts — ALL(1).zip

Status: `AUDITED_R2`

Source archive SHA-256:
`dc63f3ba5ed514f0c6b5e947474baca712c15a4c08c42b2228e421512cb04ff3`

This is a convenience extract. Exact paths/hashes are in `CANONICAL_EVIDENCE_MAP_ALL_ZIP.md`; full inventory is in `FULL_ARCHIVE_MANIFEST_ALL_2026_10_06.csv`.

## Environment / final local state

- Kali `192.168.56.10/24`; no default route; Nmap 7.99.
- Windows `192.168.56.20/24`; no default route.
- LanmanServer Running/Automatic.
- SMB1=True; SMB2=True; FS-SMB1 Installed.
- TCP 139/445 Listening.
- `srv.sys` displayed FileVersion `6.3.9600.16384`; numeric `6.3.9600.16421`.
- project local patch classification: `UNPATCHED`.
- custom Windows Firewall rule: TCP 139/445 from `.56.10`; default File and Printer Sharing group not opened wholesale.
- final snapshots: `Before Demo` current on Kali and Windows after the snapshot step.

## Scenario 1

- B2 subnet discovery: `.56.1`, `.56.20`, `.56.100`, `.56.10` up.
- B3: `.56.20` up.
- B4: 139/445 open, syn-ack ttl 128.
- B5: 139 Windows netbios-ssn; 445 Windows Server 2008 R2–2012 microsoft-ds fingerprint.
- B6: NT LM 0.12 (SMBv1), 2.0.2, 2.1, 3.0, 3.0.2.
- B6: 3.0.2 signing enabled but not required.
- B6: capabilities include DFS, Leasing and Multi-credit as shown.
- `smb-os-discovery`: no usable output.

Exact operator vs raw command forms: `COMMAND_LINEAGE_MATRIX.md`.

## Scenario 2

- NSE-SMB-01: 139/445 open.
- NSE-SMB-02: SMBv1 + SMB2/3 dialects.
- NSE-SMB-03: signing enabled but not required.
- NSE-SMB-04: 445 open, no Host script result, no vulnerability verdict.
- remote classification: `UNKNOWN / NO USABLE SCRIPT RESULT`.
- local patch classification remains independently `UNPATCHED`.

## Case B

Direct local state:
- before: SMB1=True, SMB2=True, FS-SMB1 Installed, LanmanServer Running.
- action: `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`.
- after: SMB1=False, SMB2=True, FS-SMB1 Installed, LanmanServer Running.

Raw retest:
- SMBv1 dialect absent; SMB2/3 remain.
- 445 open for MS17-010 retest; no Host script verdict.
- remote classification remains UNKNOWN.
- patch state remains UNPATCHED.

## Case C

Direct screenshots:
- CASE_C_KALI=em2; CASE_C_WINDOWS=em3.
- bridge0 contains both Case C member interfaces.
- `pfil_member=1`, `pfil_bridge=0`.
- Block IPv4 TCP rule configured on CASE_C_KALI:
  - source `.56.10`;
  - destination `.56.20`;
  - SMB_Ports;
  - logging enabled;
  - description `CASE C - Block SMB Kali to Windows`.
- block row is above pass row.

Final manifest/closure:
- data plane uses `ATTT-PFS-KALI` and `ATTT-PFS-WIN`;
- management Host `.57.1` ↔ pfSense em1 `.57.2`;
- `pfil_onlyip=1`;
- pfSense CE 2.9.0-RELEASE.

Raw retest:
- 139/445 filtered, no-response.
- 445 filtered for MS17-010 retest; no script verdict.

Firewall log direct observation:
- red-X blocked action;
- interface CASE_C_KALI;
- source `.56.10`;
- destination `.56.20:139` and `:445`;
- TCP SYN;
- scan-time entries.

Conflict:
- visible rule label in screenshot: `CASE C baseline pass Kali to Windows (100000104)`;
- manifest/closure attribution: `CASE C - Block SMB Kali to Windows (1000000104)`.

Therefore the log proves blocked matching traffic in the pfSense path but **not** the exact named-rule attribution.

## Exclusions / caution

- `Kali_Baseline.txt` is early pre-Nmap history.
- Case C debug/pre-repair attempts are noncanonical.
- Summary causal explanations for no NSE output are not facts unless direct evidence supports them.
- Case A patching is not a completed experiment.
- Archive folder hierarchy is not a report outline.
