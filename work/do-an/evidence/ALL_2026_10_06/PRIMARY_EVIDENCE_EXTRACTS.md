# Primary Evidence Extracts — ALL(1).zip

Purpose: keep a compact, repo-local snapshot of the primary evidence needed for Chapters 2–4 so future agents do not have to reconstruct experimental truth from summaries or folder names.

Source archive SHA-256:
`dc63f3ba5ed514f0c6b5e947474baca712c15a4c08c42b2228e421512cb04ff3`

This file preserves selected direct observations. The full archive remains the provenance source; hashes in `CANONICAL_EVIDENCE_MAP_ALL_ZIP.md` bind these extracts to source artifacts.

## Environment / local state

### Final pre-demo
- Kali: `192.168.56.10/24`
- Kali default route to Internet: none
- Nmap: 7.99
- Windows: `192.168.56.20/24`
- Windows default route to Internet: none
- LanmanServer: Running
- FS-SMB1: Installed
- SMB1=True
- SMB2=True
- TCP 445: Listen
- TCP 139: Listen
- `srv.sys` numeric: `6.3.9600.16421`
- Microsoft minimum updated: `6.3.9600.18604`
- local classification: `UNPATCHED`
- custom Windows Firewall rule: `ATTT Lab SMB 139-445`, local ports 139/445, remote source `192.168.56.10`
- default File and Printer Sharing group: disabled

### Final snapshots
Kali:
- `Basic`
- `Before Demo` current

Windows:
- `Basic`
- `Before Demo` current

## Scenario 1 raw observations

### B2 — subnet discovery
Command:
`nmap -sn -PR -T3 --max-retries 2 -oA b2_host_discovery 192.168.56.0/24`

Observed up:
- 192.168.56.1
- 192.168.56.20
- 192.168.56.100
- 192.168.56.10

### B3 — target alive
Command:
`nmap -sn -PR -T3 --max-retries 2 -oA b3_target_alive 192.168.56.20`

Observed:
- target 192.168.56.20 up

### B4 — ports
Command:
`nmap -sS -p 139,445 -T3 --max-retries 2 --reason -oA b4_smb_ports 192.168.56.20`

Observed:
- 139/tcp open netbios-ssn — syn-ack ttl 128
- 445/tcp open microsoft-ds — syn-ack ttl 128

### B5 — service/version
Command:
`nmap -sS -sV --version-intensity 5 -p 139,445 -T3 --max-retries 2 -oA b5_smb_version 192.168.56.20`

Observed:
- 139/tcp open netbios-ssn — Microsoft Windows netbios-ssn
- 445/tcp open microsoft-ds — Microsoft Windows Server 2008 R2 - 2012 microsoft-ds

### B6 — SMB NSE
Command:
`nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities -T3 --max-retries 2 -oA b6_smb_nse 192.168.56.20`

Observed:
- dialect NT LM 0.12 (SMBv1)
- dialect 2.0.2
- dialect 2.1
- dialect 3.0
- dialect 3.0.2
- 3.0.2 message signing enabled but not required
- capabilities include DFS; Leasing and Multi-credit where shown
- no usable `smb-os-discovery` output

## Scenario 2 raw observations

### NSE-SMB-01
Command:
`nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20`

Observed:
- 139/tcp open — syn-ack ttl 128
- 445/tcp open — syn-ack ttl 128

### NSE-SMB-02
Command:
`nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20`

Observed:
- NT LM 0.12 (SMBv1)
- 2.0.2
- 2.1
- 3.0
- 3.0.2

### NSE-SMB-03
Command:
`nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb2-security-mode -oA evidence/nse-smb/NSE-SMB-03_signing 192.168.56.20`

Observed:
- 3.0.2 message signing enabled but not required

### NSE-SMB-04
Command:
`nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`

Observed:
- host up
- 445/tcp open
- no Host script results
- no vulnerability verdict

Classification:
`UNKNOWN / NO USABLE SCRIPT RESULT`

## Case B — disable SMBv1

Before:
- SMB1=True
- SMB2=True
- FS-SMB1 Installed
- LanmanServer Running
- patch UNPATCHED

Action:
`Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`

After local:
- SMB1=False
- SMB2=True
- FS-SMB1 Installed
- LanmanServer Running
- TCP 139/445 listening
- Windows Firewall lab rule unchanged
- `srv.sys 6.3.9600.16421` unchanged / UNPATCHED

Protocol retest:
`nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20`

Observed:
- SMBv1 NT LM 0.12 absent
- 2.0.2, 2.1, 3.0, 3.0.2 remain

MS17-010 retest:
`nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`

Observed:
- 445/tcp open
- no Host script results
- no vulnerability verdict

Classification:
`UNKNOWN / NO USABLE SCRIPT RESULT`

## Case C — pfSense transparent bridge

Data plane:
`Kali .56.10 -> ATTT-PFS-KALI -> em2 -> bridge0 -> em3 -> ATTT-PFS-WIN -> Windows .56.20`

Management plane:
`Host .57.1 <-> Host-Only #2 <-> pfSense em1 .57.2`

pfSense:
- CE 2.9.0-RELEASE
- bridge0 members em2/em3
- pfil_member=1
- pfil_bridge=0
- pfil_onlyip=1
- block rule on CASE_C_KALI/em2:
  - IPv4 TCP
  - source 192.168.56.10
  - destination 192.168.56.20
  - destination ports 139/445
  - logging enabled
- block rule above baseline pass rule

Canonical port retest:
`sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20`

Observed:
- host up, arp-response
- 139/tcp filtered — no-response
- 445/tcp filtered — no-response

Canonical pfSense log:
- matching rule `CASE C - Block SMB Kali to Windows`
- interface CASE_C_KALI
- source 192.168.56.10
- destination 192.168.56.20
- TCP SYN to ports 139/445
- action Block

Canonical MS17-010 retest:
`nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`

Observed:
- host up
- 445/tcp filtered
- no vulnerability verdict

Windows local state remains:
- SMB1=True
- SMB2=True
- TCP 139/445 listening
- `srv.sys 6.3.9600.16421`
- UNPATCHED
- Windows Firewall baseline allow rule unchanged

## Exclusions / caution

- Do not treat `Kali_Baseline.txt` as final tool baseline; it predates Nmap installation.
- Do not treat Case C pre-repair/debug attempts as canonical.
- Do not adopt causal explanations for missing NSE output from summary prose unless independently proven.
- Do not treat Case A patching as completed experiment.
- Do not treat archive folders as report headings.
