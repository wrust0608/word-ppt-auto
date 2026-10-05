# Command Lineage Matrix — ALL(1).zip

Status: `AUDITED_R2`  
Purpose: distinguish the command recorded by the run manifest/screenshot from the argv recorded by Nmap itself.

## Rule

Two command representations are preserved separately:

- **Operator command**: command string recorded in a run manifest or visible screenshot. This may contain shell wrappers such as `sudo`.
- **Nmap-recorded argv**: command line recorded by Nmap in the `.nmap`, `.xml`, and `.gnmap` outputs. Nmap may normalize ordering and may record `--privileged` even when the operator command does not contain that literal flag.

They are related provenance records, not interchangeable text.

## Raw triad consistency

For all 13 scan groups in the archive:
- `.nmap` header;
- XML root `args`;
- `.gnmap` header

record the same Nmap argv. Result: **13/13 PASS**.

## Scenario 1

| Step | Operator command from `Scenario1_Run_Manifest.txt` | Nmap-recorded argv from raw triplet |
|---|---|---|
| B2 | `sudo nmap -sn -PR 192.168.56.0/24 -T3 --max-retries 2 -oA b2_host_discovery` | `/usr/lib/nmap/nmap -sn -PR -T3 --max-retries 2 -oA b2_host_discovery 192.168.56.0/24` |
| B3 | `sudo nmap -sn -PR 192.168.56.20 -T3 --max-retries 2 -oA b3_target_alive` | `/usr/lib/nmap/nmap -sn -PR -T3 --max-retries 2 -oA b3_target_alive 192.168.56.20` |
| B4 | `sudo nmap -sS -p 139,445 192.168.56.20 -T3 --max-retries 2 --reason -oA b4_smb_ports` | `/usr/lib/nmap/nmap -sS -p 139,445 -T3 --max-retries 2 --reason -oA b4_smb_ports 192.168.56.20` |
| B5 | `sudo nmap -sS -sV --version-intensity 5 -p 139,445 192.168.56.20 -T3 --max-retries 2 -oA b5_smb_version` | `/usr/lib/nmap/nmap -sS -sV --version-intensity 5 -p 139,445 -T3 --max-retries 2 -oA b5_smb_version 192.168.56.20` |
| B6 | `sudo nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities 192.168.56.20 -T3 --max-retries 2 -oA b6_smb_nse` | `/usr/lib/nmap/nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities -T3 --max-retries 2 -oA b6_smb_nse 192.168.56.20` |

B1 is a shell/local-state step: `ip addr show; ip route show`; there is no Nmap raw triplet for B1.

## Scenario 2

| Step | Operator command from `Scenario2_Run_Manifest.txt` | Nmap-recorded argv from raw triplet |
|---|---|---|
| NSE-SMB-01 | `sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20` | `/usr/lib/nmap/nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20` |
| NSE-SMB-02 | `nmap -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20` | `/usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20` |
| NSE-SMB-03 | `nmap -p 445 -n -T3 --max-retries 2 --script smb2-security-mode -oA evidence/nse-smb/NSE-SMB-03_signing 192.168.56.20` | `/usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb2-security-mode -oA evidence/nse-smb/NSE-SMB-03_signing 192.168.56.20` |
| NSE-SMB-04 | `nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20` | `/usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20` |

## Case B

Action:
`Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`

| Retest | Operator command from `SMBv1_Remediation_Run_Manifest.txt` | Nmap-recorded argv from raw triplet |
|---|---|---|
| Protocols | `nmap -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20` | `/usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20` |
| MS17-010 | `nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20` | `/usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20` |

## Case C

| Retest | Operator command from `pfSense_Remediation_Run_Manifest.txt` | Nmap-recorded argv from raw triplet |
|---|---|---|
| Ports | `sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20` | `/usr/lib/nmap/nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20` |
| MS17-010 | `nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20` | `/usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20` |

## Writing rule

- When describing **what the operator executed**, cite/use the manifest command.
- When reproducing **what Nmap recorded in machine-generated output**, use the raw argv.
- Do not infer that `sudo` was or was not used from the raw Nmap header alone.
- Do not rewrite `--privileged` as an operator-entered flag unless a direct operator record shows it.
