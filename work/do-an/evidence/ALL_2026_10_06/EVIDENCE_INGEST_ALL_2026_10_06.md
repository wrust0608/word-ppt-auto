# EVIDENCE INGEST — ALL(1).zip (2026-10-06)

Status: `INGESTED_FOR_CH2_CH3_CH4`

## 1. Source package

- User-supplied archive: `ALL(1).zip`
- Archive size: 28,547,199 bytes
- SHA-256: `dc63f3ba5ed514f0c6b5e947474baca712c15a4c08c42b2228e421512cb04ff3`
- Extracted files: 174
- Experimental/evidence files under the five evidence groups: 168
- Additional DOCX/reference files at archive root: 6

This ingest does **not** reuse the archive's directory structure as a report outline. The archive is treated only as a provenance container for factual evidence.

## 2. Evidence precedence

1. Machine-generated raw output / local operating-system state / firewall log.
2. Final run manifest matching the raw output.
3. Screenshot from the same final/canonical run.
4. Summary text.
5. Historical report / DOCX.

If a lower-priority artifact adds a claim not present in the higher-priority artifact, the claim is not promoted to fact without independent support.

## 3. Final experimental identity reconstructed from evidence

### Baseline lab
- Hypervisor family/version used by final product: Oracle VM VirtualBox 7.2.20.
- A later host-repair/case-C record identifies the installed build as `7.2.20r175154`.
- Kali: `192.168.56.10/24`.
- Windows Server 2012 R2 Standard Evaluation Build 9600: `192.168.56.20/24`.
- Baseline network: one Host-Only NIC per Kali/Windows VM; no NAT NIC and no Bridged NIC; no default route to Internet inside either VM at pre-demo audit.
- Host-Only network: `192.168.56.0/24`; host adapter `192.168.56.1/24`; VirtualBox DHCP disabled.
- Nmap at final pre-demo state: 7.99.
- Final pre-demo snapshot: `Before Demo` on Kali and Windows.

### Windows SMB baseline
- LanmanServer: Running / Automatic.
- TCP 139 and TCP 445: Listening locally.
- SMB1=True; SMB2=True.
- FS-SMB1: Installed.
- Default File and Printer Sharing rule group: not opened wholesale.
- Custom inbound lab rule: TCP 139/445, source `192.168.56.10`.

### MS17-010 local patch baseline
- OS: Windows Server 2012 R2 Build 9600 x64.
- Direct update mapping: KB4012213 / KB4012216; superseding updates also relevant.
- Microsoft minimum updated `srv.sys`: `6.3.9600.18604`.
- Local `srv.sys` FileVersion String: `6.3.9600.16384`.
- Local numeric version: `6.3.9600.16421`.
- Local installed hotfix inventory in mapping file contains six 2014 updates and no 2017+ MS17-010-containing update.
- Final local classification: `UNPATCHED`.

## 4. Exact experiment lineage reconstructed from raw data

### Scenario 1 — service discovery and SMB enumeration

Exact raw command lineage:
- B2: `nmap -sn -PR -T3 --max-retries 2 -oA b2_host_discovery 192.168.56.0/24`
- B3: `nmap -sn -PR -T3 --max-retries 2 -oA b3_target_alive 192.168.56.20`
- B4: `nmap -sS -p 139,445 -T3 --max-retries 2 --reason -oA b4_smb_ports 192.168.56.20`
- B5: `nmap -sS -sV --version-intensity 5 -p 139,445 -T3 --max-retries 2 -oA b5_smb_version 192.168.56.20`
- B6: `nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities -T3 --max-retries 2 -oA b6_smb_nse 192.168.56.20`

Primary observations:
- B2 observed `.56.1`, `.56.20`, `.56.100`, and `.56.10` up at that measurement time.
- B3 target `.56.20` up.
- B4 TCP 139/445 open, `syn-ack ttl 128`.
- B5 fingerprint: 139 Windows netbios-ssn; 445 Microsoft Windows Server 2008 R2–2012 microsoft-ds.
- B6 SMB dialects: NT LM 0.12 (SMBv1), 2.0.2, 2.1, 3.0, 3.0.2.
- B6 signing: 3.0.2, message signing enabled but not required.
- B6 capabilities: DFS; Leasing and Multi-credit on applicable SMB2/3 dialects.
- `smb-os-discovery` produced no usable output in the raw result.

### Scenario 2 — MS17-010 assessment

Exact raw commands:
- NSE-SMB-01: `nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20`
- NSE-SMB-02: `nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20`
- NSE-SMB-03: `nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb2-security-mode -oA evidence/nse-smb/NSE-SMB-03_signing 192.168.56.20`
- NSE-SMB-04: `nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`

Primary observations:
- NSE-SMB-01: 139/445 open.
- NSE-SMB-02: SMBv1 NT LM 0.12 plus SMB2/3 dialects.
- NSE-SMB-03: signing enabled but not required.
- NSE-SMB-04: host/445 reachable, but raw output contains no Host script result and no vulnerability verdict.
- Allowed classification: `UNKNOWN / NO USABLE SCRIPT RESULT`.

### Case B — disable SMBv1

Before local:
- SMB1=True; SMB2=True; FS-SMB1 Installed; LanmanServer Running.
- Windows custom firewall rule unchanged.
- Local patch state UNPATCHED.

Action:
`Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`

After local:
- SMB1=False.
- SMB2=True.
- FS-SMB1 remains Installed.
- LanmanServer remains Running; TCP 139/445 remain Listening.
- Firewall rule unchanged.
- `srv.sys` remains `6.3.9600.16421` / UNPATCHED.

Retest raw commands:
- `nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20`
- `nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`

Retest observations:
- SMBv1 NT LM 0.12 no longer appears; SMB2/3 2.0.2/2.1/3.0/3.0.2 remain.
- MS17-010 script again yields no Host script result/verdict.
- Allowed remote classification remains UNKNOWN.

### Case C — pfSense transparent bridge

This case uses a different network topology from baseline and must not be back-projected into Scenario 1/2 baseline.

Data plane:
`Kali .56.10 -> ATTT-PFS-KALI -> pfSense em2 -> bridge0 -> pfSense em3 -> ATTT-PFS-WIN -> Windows .56.20`

Management plane:
`Host .57.1 <-> Host-Only #2 <-> pfSense em1 .57.2`

pfSense final product facts:
- pfSense CE 2.9.0-RELEASE.
- Snapshot `Before Case C` present.
- `bridge0` members: em2 + em3.
- Tunables: `pfil_member=1`, `pfil_bridge=0`, `pfil_onlyip=1`.
- Block rule on CASE_C_KALI/em2: IPv4 TCP source `.56.10` destination `.56.20`, destination ports 139/445, logging enabled.
- Block rule is ordered above a baseline pass rule `.56.10 -> .56.20`.
- Windows local SMB/patch state remains unchanged: SMB1=True, SMB2=True, ports listening, patch UNPATCHED.

Canonical retest commands:
- `sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20`
- `nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`

Canonical observations:
- TCP 139/445: `filtered`, reason `no-response`.
- pfSense canonical log screenshot records matching blocked SYN packets for `.56.10 -> .56.20:139/445`.
- MS17-010 retest sees 445 filtered and no script verdict.
- Allowed classification: filtered path + UNKNOWN remote vulnerability verdict; host remains locally UNPATCHED.

## 5. Chronology/conflict notes that must not be re-inferred later

1. `Kali_Baseline.txt` is an early baseline before Nmap installation. It records `nmap: command not found`. It is not the final demo baseline. `Final_PreDemo_Audit.txt` later records Nmap 7.99 and all required scripts present.
2. `Final_PreDemo_Audit.txt` at 08:20 records `Before Demo Exists: NO`. `Before_Demo_Snapshots.txt` at 08:22 records the two `Before Demo` snapshots as current. This is normal chronology, not a contradiction in final state.
3. `Final_PreDemo_Audit.txt` identifies VirtualBox 7.2.20. Later Case C/repair records identify exact installed build `7.2.20r175154`. Report prose can safely use 7.2.20 unless build revision is relevant.
4. Case C contains pre-repair/aborted/debug attempts. They are preserved but excluded from canonical conclusions. Only the final run raw files plus canonical screenshots/log are canonical for Case C.
5. Summary/manifests sometimes supply causal explanations for no script output. Raw data does not. For report writing, `NO USABLE SCRIPT RESULT` must not be assigned a cause unless another direct artifact proves it.
6. pfSense summary text contains stronger claims such as “intrinsically vulnerable” or “eliminating remote exploitable exposure.” These are not adopted as experimental facts. Use bounded raw/log observations instead.
7. No complete Case A patch experiment exists in this package. Patching remains a theoretical/reference mitigation for Chapter 4 unless new audited evidence is added.

## 6. Canonical artifact policy for future Chapters 2–4

Use as primary evidence:
- final pre-demo/local state text;
- raw Nmap `.nmap/.xml/.gnmap` files;
- final/canonical screenshots matching those raw files;
- pfSense canonical block-log screenshot;
- Windows local state screenshots for Case B;
- official Microsoft mapping file only as local mapping record, with external Microsoft source IDs from the Source Ledger for report citation.

Preserve but do not use as main experimental result:
- HostRepair;
- pre-repair/aborted/debug pfSense runs;
- installer/tutorial screenshots unless needed for environment description;
- old DOCX reports;
- summary prose when it exceeds raw evidence.

## 7. Report-architecture boundary

This ingest is not an outline. Folder names such as `00_Environment`, `01_Scenario1`, etc. are provenance only.

Chapter structure must be designed independently around what a reader needs to understand. Evidence paths are mapped to claims after the outline is designed, not vice versa.
