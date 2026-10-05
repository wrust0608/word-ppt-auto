# Evidence Use Policy for ALL(1).zip

## Primary / canonical
- Machine-generated Nmap raw output from final run directories.
- Local Windows/Kali pre-demo state and Windows patch mapping/state.
- Windows Firewall final preparation audit.
- Final snapshot verification.
- Case B local before/action/after screenshots and final raw retests.
- Case C final bridge/rule screenshots, canonical port/MS17-010 screenshots, canonical firewall log, and final raw retests.

## Supporting
- Installation screenshots, Guest Additions, tool installation, generic VM configuration, auxiliary interface screenshots.
- Run manifests when they agree with raw/local state.

## Secondary interpretation only
- `*_Summary.txt`.
- Historical Word reports.

## Troubleshooting / excluded from main result claims
- `HostRepair/*`.
- pfSense console/assign/ip/php/touch/sshd/ctrl-c diagnostics.
- `RUN4_PAUSE_STATE_REPORT.txt` sections describing failed pre-canonical attempts, except its final closure may be used only to locate the final run and must be checked against canonical raw/log artifacts.
- pre-repair/aborted/debug raw attempts referenced by the Case C manifest.

## Negative-result rule
- Scenario 2 NSE-SMB-04: raw has no Host script result -> `UNKNOWN / NO USABLE SCRIPT RESULT`.
- Case B NSE-SMB-04: raw has no Host script result -> `UNKNOWN / NO USABLE SCRIPT RESULT`.
- Case C NSE-SMB-04: 445 filtered; no script verdict -> `UNKNOWN` from this vantage point.
- Do not manufacture `SAFE`, `NOT VULNERABLE`, `VULNERABLE`, or an NTSTATUS not present in raw output.
