# Timebase and Cross-Layer Locks — ALL(1).zip

Status: `FINAL_DATA_LOCK_R3`
Date: 2026-10-06

## 1. Clock-domain lock

Artifacts in the package were produced by different systems with different clock/timezone settings.

Observed pattern:
- Scenario 1 raw Nmap timestamps are around 21:47–21:52 on 2026-10-03, while the Scenario 1 manifest is timestamped 08:54 on 2026-10-04 (+07).
- Scenario 2 raw Nmap timestamps are around 22:07–22:10 on 2026-10-03, while the manifest is timestamped 09:14 on 2026-10-04 (+07).
- Case B raw Nmap timestamps are around 22:29 on 2026-10-03, while the manifest is timestamped 09:31 on 2026-10-04 (+07).
- Case C canonical Nmap port scan starts at 03:20:18 on 2026-10-04, while the pfSense firewall UI shows matching .56.10 -> .56.20:139/445 entries at 14:20:18–14:20:19 on 2026-10-04.
- Windows baseline reports Windows timezone as Pacific Time.

Therefore:
- do not compare timestamp strings from Kali, Windows, pfSense UI, and host manifests as if they share one wall clock;
- do not derive experiment order from cross-system timestamp text alone;
- use run lineage, filenames, manifests, raw command/output correspondence, and same-artifact chronology;
- when a report needs time, use the run date/sequence, not a synthetic unified timestamp unless a timezone conversion is independently established.

The repeated approximately +11 hour offset between Kali Nmap text and host/pfSense records is an observed relationship, but the evidence package does not by itself establish the exact timezone configuration that caused it.

## 2. SMB-signing cross-layer lock

Two direct observations coexist:
- local Windows pre-demo audit:
  - `EnableSecuritySignature=False`
  - `RequireSecuritySignature=False`
- remote Nmap `smb2-security-mode`:
  - dialect 3.0.2
  - `Message signing enabled but not required`

These are records from different observation mechanisms/layers.

Data-layer rule:
- preserve both observations exactly;
- do not overwrite either one;
- do not call them a contradiction without protocol-level source analysis;
- do not translate the local PowerShell flags into the remote NSE wording, or vice versa;
- report remote signing behavior from Nmap when discussing remote observation; report PowerShell properties only when discussing local server configuration.

## 3. Host-discovery identity lock

Scenario 1 B2 directly observed four IP addresses up:
- .56.1
- .56.10
- .56.20
- .56.100

Only identities directly established elsewhere may be named:
- .56.1 = VirtualBox Host-Only host adapter;
- .56.10 = Kali;
- .56.20 = Windows target.

The identity of .56.100 is not established by the canonical evidence layer.

Important:
- VirtualBox Host-Only DHCP is configured but disabled;
- a separate host-side `NatNetwork-Lab` DHCP service exists and is enabled, but final pre-demo VM NIC audits show Kali/Windows are not attached to NAT/Bridged adapters.

Therefore:
- do not label .56.100 as “the DHCP server”, “pfSense”, or another specific node unless new direct evidence identifies it;
- existence of host-side NAT/DHCP configuration does not imply the two baseline lab VMs had NAT connectivity.

## 4. Patch-state wording lock

`MS17-010_Official_Mapping.txt` is a composite artifact containing:
1. copied/reference mapping information about Microsoft updates/version thresholds;
2. local Windows observations.

For report use:
- local observations may be supported by the artifact and direct screenshots/local audits;
- Microsoft update/version-threshold claims must cite the Source Ledger / official Microsoft sources, not the artifact as external authority;
- use wording such as “the local hotfix inventory does not show KB4012213, KB4012216, or a later MS17-010-containing update in the observed inventory” rather than implying an omniscient history of every package ever installed;
- numeric `srv.sys 6.3.9600.16421` versus Microsoft minimum updated `6.3.9600.18604` remains the strongest local patch-state comparison.

## 5. Case C firewall-log clock and rule-label lock

Direct screenshot facts:
- action is Block (red X);
- interface CASE_C_KALI;
- source .56.10;
- destination .56.20:139 and :445;
- TCP SYN;
- visible rows occur at 14:20:18–14:20:19 in the pfSense UI.

Canonical Nmap port scan:
- starts at 03:20:18 in the Kali raw output;
- probes .56.20 ports 139/445;
- reports both filtered/no-response.

The matching seconds/traffic tuple plus the repeated clock-domain offset support that these are corresponding scan/log events. However:
- exact cross-system wall-clock equivalence is not asserted;
- the visible Rule label is `CASE C baseline pass Kali to Windows (100000104)`, conflicting with the manifest/closure’s named Block-rule attribution.

Allowed:
- matching SMB SYN traffic was blocked in the pfSense path during the canonical Case C port-scan event.

Forbidden:
- the log screenshot independently proves that the named configured Block rule `CASE C - Block SMB Kali to Windows` was the rule that matched.

## 6. Report boundary

These locks are data-integrity constraints, not report headings.
